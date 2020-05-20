# pelion-device-simulator

![pelion-device-simulator](https://i.ibb.co/9VKvhgF/pelion-device-simulator.gif)

## Quickstart:

1. Download the developer certificates from the [Device Management Portal](https://portal.mbedcloud.com//):
   1. Log in to the portal with your credentials.
   1. Navigate to **Device identity** > **Certificates**.
   1. Click **New certificate**.
   1. Add a name and an optional description for the certificate, and click **Create certificate**.
   1. Go to **Device identity** > **Certificates** again.
   1. Click on your new certificate.
   1. Click **Download developer C file** to download the file `mbed_cloud_dev_credentials.c`.

2. Copy the `mbed_cloud_dev_credentials.c` file to the peliondm demo folder:

    ```
    cp ~/mbed_cloud_dev_credentials.c demos/peliondm/
    ```
3. Build the docker image:

    ```
    docker build -t pelion/device-simulator .
    ```

4. And run it: (you can use -p accordingly if you want start multiple instances)

    ```
    docker run -p 8002:7829 pelion/device-simulator
    ```

5. Point your web browser to [http://<machine_ip>:8002/view/peliondm](http://<machine_ip>:8002/view/peliondm) replacing `<machine_ip>` with the IP address of your machine.