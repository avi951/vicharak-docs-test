############
PERIPLEX I2C
############

This section explains how to interact with the ``I2C's`` device generated on Vaaman via Periplex.

How to Generate I2C's on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``5 I2C's``, Your need to create a json file and copy the following content into it. 

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2c": [
                {
                    "id": 0,
                    "SCL": "GPIOT_RXP28",
                    "SDA": "GPIOT_RXN28"
                },
                {
                    "id": 1,
                    "SCL": "GPIOL_73",
                    "SDA": "GPIOL_75"
                },
                {
                    "id": 2,
                    "SCL": "GPIOR_173",
                    "SDA": "GPIOL_72"
                },
                {
                    "id": 3,
                    "SCL": "GPIOR_174",
                    "SDA": "GPIOR_178"
                },
                {
                    "id": 4,
                    "SCL": "GPIOT_RXN27",
                    "SDA": "GPIOR_183"
                }
            ],
            "gpio": [],
            "pwm": [],
            "ws": [],
            "spi": [],
            "onewire": [],
            "can": [],
            "i2s": [],
            "i2cslave": []
         }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``5 I2C's`` is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``5-I2C's`` devices generated through Periplex like this:
    
   .. raw:: html

        <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 85%; height: 608px; overflow: auto; white-space: pre-wrap;">
            vicharak@vicharak:~$ ls /dev
            autofs           i2c-1         media0        rtc        tty24  tty49     usbmon0      vcsu
            block            i2c-10        mem           rtc0       tty25  tty5      usbmon1      vcsu1
            btrfs-control    <span style="color:red;">i2c-11</span>        mmcblk0       shm        tty26  tty50     usbmon2      vcsu2
            bus              <span style="color:red;">i2c-12</span>        mmcblk0boot0  snd        tty27  tty51     usbmon3      vcsu3
            cec0             <span style="color:red;">i2c-13</span>        mmcblk0boot1  spidev0.0  tty28  tty52     usbmon4      vcsu4
            char             <span style="color:red;">i2c-14</span>        mmcblk0p1     stderr     tty29  tty53     usbmon5      vcsu5
            console          <span style="color:red;">i2c-15</span>        mmcblk0p2     stdin      tty3   tty54     usbmon6      vcsu6
            cpu_dma_latency  i2c-4         mmcblk0p3     stdout     tty30  tty55     v4l          vcsu7
            crypto           i2c-7         mmcblk0p4     sw_sync    tty31  tty56     v4l-subdev0  vendor_storage
            disk             i2c-9         mmcblk0p5     tty        tty32  tty57     v4l-subdev1  vhci
            dma_heap         iep           mmcblk0p6     tty0       tty33  tty58     v4l-subdev2  video0
            dri              iio:device0   mmcblk0p7     tty1       tty34  tty59     vcs          video1
            drm_dp_aux0      initctl       mmcblk0p8     tty10      tty35  tty6      vcs1         video2
            fb0              input         mmcblk0rpmb   tty11      tty36  tty60     vcs2         video3
            fd               kmsg          mpp_service   tty12      tty37  tty61     vcs3         video4
            full             log           mqueue        tty13      tty38  tty62     vcs4         video-dec0
            fuse             loop0         net           tty14      tty39  tty63     vcs5         video-enc0
            gpiochip0        loop1         null          tty15      tty4   tty7      vcs6         watchdog
            gpiochip1        loop2         periplex      tty16      tty40  tty8      vcs7         watchdog0
            gpiochip2        loop3         port          tty17      tty41  tty9      vcsa         zero
            gpiochip3        loop4         ptmx          tty18      tty42  ttyFIQ0   vcsa1        zram0
            gpiochip4        loop5         pts           tty19      tty43  ttyS0     vcsa2
            gpiochip5        loop6         ram0          tty2       tty44  ubi_ctrl  vcsa3
            hdmi_hdcp1x      loop7         random        tty20      tty45  uhid      vcsa4
            hugepages        loop-control  rfkill        tty21      tty46  uinput    vcsa5
            hwrng            mali0         rga           tty22      tty47  urandom   vcsa6
            i2c-0            mapper        rk_cec        tty23      tty48  usb-ffs   vcsa7
        </pre>

How to interact with the generated I2C's ?
===========================================

The Periplex platform dynamically generates ``I2C`` devices, which are accessible through device nodes such as:

.. code-block::
      
   /dev/i2c-11
   /dev/i2c-12
   /dev/i2c-13
   ...

These ``i2c-*`` device nodes allow users to communicate with I2C peripherals such as sensors, EEPROMs, and other slave devices connected to the I2C bus.

Simple set/get I2C values
-------------------------

To use the i2cset, i2cget, and i2cdetect commands, you need to install the i2c-tools package. These tools are part of the i2c-utils package, which provides user-space tools for interacting with I2C devices via the Linux I2C subsystem.

.. code-block::

    sudo apt install i2c-tools

1. **Identify I2C Buses and Devices:**

   - You can list available I2C buses using:

   .. code-block::
    
        i2cdetect -l

   - Each ``i2c-11`` represents an ``I2C`` bus. For example, ``i2c-11`` can communicate with multiple devices, each identified by a unique 7-bit or 10-bit address.

2. **Detect I2C Devices on a Bus:**

   - To scan a particular bus for connected I2C devices, use:

   .. code-block::

        sudo i2cdetect -y <bus_number>

   - ``<bus_number>``: The I2C bus number (like 11 or 12 from the previous command).

   - For example, to scan bus ``11``:

   .. code-block::

        sudo i2cdetect -y 11
   
   - The output shows a grid with device addresses. Devices are listed by their 7-bit addresses.

3. **Reading I2C Device Registers:**

   - To read a register value from a device, use:

   .. code-block::

        sudo i2cget -y <bus_number> <device_address> <register_address>

   - ``<bus_number>``: The I2C bus number (like 11 or 12).

   - ``<device_address>``: The I2C address of the device (like 0x40).

   - ``<register_address>``: The register address to read from.

   - For example, to read register 0x10 from device 0x40 on bus 11:

   .. code-block::

        sudo i2cget -y 11 0x40 0x10

4. **Writing to I2C Device Registers:**

   - To write a value to a device's register, use:

   .. code-block::

        sudo i2cset -y <bus_number> <device_address> <register_address> 

   - ``<value>``: The value to write to the register (like 0xFF).

   - For example, to write 0x20 to register 0x10 of device 0x40 on bus 11:

   .. code-block::

        sudo i2cset -y 11 0x40 0x10 0x20


.. note::

    - Ensure you have the correct permissions to access ``I2C``. Running these commands might require sudo.

    - Use ``i2c-tools`` carefully, as writing invalid values to I2C devices can cause unexpected behavior.

    - The ``-y`` flag skips the interactive confirmation prompt, so use it with caution.


Example of using the I2C protocol
---------------------------------

This example demonstrates reading temperature data using the I2C protocol with a temperature sensor (e.g., TMP102).

- **Writing to the I2C bus** sets the sensor’s configuration or triggers a measurement.
- **Reading from the I2C bus** retrieves the temperature value from the sensor’s internal registers.

Means writing to the I2C device address adjusts its settings, and reading from the address collects sensor data or status.