const launchServer = require('./server/launch-server');
const Path = require('path');
const fs = require('fs');

const child_process = require('child_process');
const program = require('commander');

const demo_output_directory = 'out';

program.parse(process.argv);

// if not already compiled, kickstart certificate generation and compilation
if (!fs.existsSync(`${demo_output_directory}/peliondm.wasm`)) {
    console.log(`NOTE: first-run detected, need to generate dev certificate and build pelion-demo (subsequent invocations won't ne ed it) ...\n`);
    
    console.log(`Generating credentials file ...`);
    const genCertResult = child_process.spawnSync(
        'python', ['generate-certificate.py'], { cwd : 'demos/peliondm' }
    );

    if (genCertResult.status === 0) {
        console.log(genCertResult.stdout.toString());
    } else {
        console.log(genCertResult.stderr.toString());
    }

    console.log(`Building 'pelion-demo' ...`);
    const buildResult = child_process.spawnSync(
        'node',
        [
            'cli.js',
            '-i',
            'demos/peliondm',
            '-o',
            `${demo_output_directory}`,
            '--compiler-opts',
            '-Os'
        ]
    );

    if (buildResult.status === 0) {
        console.log(buildResult.stdout.toString());
    } else {
        console.log(buildResult.stderr.toString());
    }
}

// launch Web Server
launchServer(Path.join(__dirname, 'out'), process.env.PORT || 7829, 3600000 /*1hour cache*/, true /*runtime logs*/, function(err) {
    if (err) return console.error(err);

    // noop
});

