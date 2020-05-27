const launchServer = require('./server/launch-server');
const Path = require('path');

const child_process = require('child_process');
const program = require('commander');

const demo_output_directory = 'out';

console.log(`Building peliondm-example ...`);

program.parse(process.argv);

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

// launch Web Server
launchServer(Path.join(__dirname, 'out'), process.env.PORT || 7829, 3600000 /*1hour cache*/, true /*runtime logs*/, function(err) {
    if (err) return console.error(err);

    // noop
});

