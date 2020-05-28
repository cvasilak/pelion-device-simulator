# pelion-device-simulator

![pelion-device-simulator](https://i.ibb.co/9VKvhgF/pelion-device-simulator.gif)

## Quick start:

1. Generate an API key from [Pelion Device management Portal](https://portal.mbedcloud.com/).

2. Start the `pelion/device-simulator` container image replacing `CLOUD_SDK_API_KEY` with your key:

    ```
    docker run -it -p 8002:7829 -e CLOUD_SDK_API_KEY=<API_KEY> pelion/device-simulator
    ```

    > NOTE: When the simulator detects that it starts for the first time, it will contact Pelion Device Management Service to generate a developer certificate (if none exists already) and download the credentials needed. It'll will then proceed to build the application. Subsequent invocations to start the container ('`docker start`') will skip this step. 
    
    > TIP: If you share the same '`CLOUD_API_KEY`' between different instances of the container, use a [Docker volume](https://docs.docker.com/storage/volumes/) to preserve the generated artifacts (e.g pass '`-v pelion-vol:/app/out`' when you run your multiple instances to avoid the certificate generation and build steps.),  

3. Point your web browser to [http://<machine_ip>:8002/view/peliondm](http://<machine_ip>:8002/view/peliondm) replacing `<machine_ip>` with the IP address of your machine.