#############
PERIPLEX GPIO
#############

This section explains how to interact with the ``GPIO's`` controller generated on Vaaman via Periplex.

How to Generate GPIO's on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``5 GPIO`` controller, Your need to create a json file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

      {
         "uart": [],
         "i2c": [],
         "gpio": [
            {
                  "id": 0,
                  "GPIO-0": "GPIOT_RXP03",
                  "GPIO-1": "GPIOT_RXN03",
                  "GPIO-2": "GPIOT_RXP08",
                  "GPIO-3": "GPIOT_RXN08",
                  "GPIO-4": "GPIOT_RXN21",
                  "GPIO-5": "GPIOT_RXP21",
                  "GPIO-6": "GPIOT_RXP18",
                  "GPIO-7": "GPIOT_RXN18"
            },
            {
                  "id": 1,
                  "GPIO-0": "GPIOT_RXP06",
                  "GPIO-1": "GPIOT_RXN06",
                  "GPIO-2": "GPIOT_RXN01",
                  "GPIO-3": "GPIOT_RXP01",
                  "GPIO-4": "GPIOT_RXP05",
                  "GPIO-5": "GPIOT_RXN05",
                  "GPIO-6": "GPIOT_RXN20",
                  "GPIO-7": "GPIOT_RXP20"
            },
            {
                  "id": 2,
                  "GPIO-0": "GPIOT_RXP19",
                  "GPIO-1": "GPIOT_RXN19",
                  "GPIO-2": "GPIOT_RXP02",
                  "GPIO-3": "GPIOT_RXN02",
                  "GPIO-4": "GPIOT_RXP04",
                  "GPIO-5": "GPIOT_RXN04",
                  "GPIO-6": "GPIOT_RXP07",
                  "GPIO-7": "GPIOT_RXN07"
            },
            {
                  "id": 3,
                  "GPIO-0": "GPIOT_RXP15",
                  "GPIO-1": "GPIOT_RXN15",
                  "GPIO-2": "GPIOT_RXP16",
                  "GPIO-3": "GPIOT_RXN16",
                  "GPIO-4": "GPIOT_RXP09",
                  "GPIO-5": "GPIOT_RXN09",
                  "GPIO-6": "GPIOT_RXN17",
                  "GPIO-7": "GPIOT_RXP17"
            },
            {
                  "id": 4,
                  "GPIO-0": "GPIOT_RXP12",
                  "GPIO-1": "GPIOT_RXN12",
                  "GPIO-2": "GPIOT_RXP14",
                  "GPIO-3": "GPIOT_RXN14",
                  "GPIO-4": "GPIOT_RXP11",
                  "GPIO-5": "GPIOT_RXN11",
                  "GPIO-6": "GPIOT_RXN13",
                  "GPIO-7": "GPIOT_RXP13"
            }
         ],
         "pwm": [],
         "ws": [],
         "spi": [],
         "onewire": [],
         "can": [],
         "i2s": [],
         "i2cslave": []
      }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``5 GPIO`` controller is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``5-GPIO`` controller devices generated through Periplex like this:

   .. raw:: html

      <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 81%; height: 608px; overflow: auto; white-space: pre-wrap;">
         vicharak@vicharak:~$ ls /dev
         autofs           <span style="color:red;">gpiochip9</span>     media0        rtc        tty24  tty49     usbmon0      vcsu
         block            hdmi_hdcp1x   mem           rtc0       tty25  tty5      usbmon1      vcsu1
         btrfs-control    hugepages     mmcblk0       shm        tty26  tty50     usbmon2      vcsu2
         bus              hwrng         mmcblk0boot0  snd        tty27  tty51     usbmon3      vcsu3
         cec0             i2c-0         mmcblk0boot1  spidev0.0  tty28  tty52     usbmon4      vcsu4
         char             i2c-1         mmcblk0p1     stderr     tty29  tty53     usbmon5      vcsu5
         console          i2c-10        mmcblk0p2     stdin      tty3   tty54     usbmon6      vcsu6
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
         <span style="color:red;">gpiochip10</span>       loop3         port          tty17      tty41  tty9      vcsa         zero
         gpiochip2        loop4         ptmx          tty18      tty42  ttyFIQ0   vcsa1        zram0
         gpiochip3        loop5         pts           tty19      tty43  ttyS0     vcsa2
         gpiochip4        loop6         ram0          tty2       tty44  ubi_ctrl  vcsa3
         gpiochip5        loop7         random        tty20      tty45  uhid      vcsa4
         <span style="color:red;">gpiochip6</span>        loop-control  rfkill        tty21      tty46  uinput    vcsa5
         <span style="color:red;">gpiochip7</span>        mali0         rga           tty22      tty47  urandom   vcsa6
         <span style="color:red;">gpiochip8</span>        mapper        rk_cec        tty23      tty48  usb-ffs   vcsa7
      </pre>

How to interact with the generated GPIO's ?
===========================================

The Periplex platform dynamically exposes GPIO controllers as ``gpiochip`` devices, which can be accessed via paths like:

.. code-block::
      
   /dev/gpiochip6
   /dev/gpiochip7
   /dev/gpiochip8
   ...

These ``gpiochip`` devices allow users to control individual GPIO pins, enabling interaction with external hardware components such as LEDs, sensors, and buttons.

Simple set/get GPIO's pin values
--------------------------------

To use the gpioset and gpioget commands, you need to install the libgpiod package. These tools are part of the libgpiod-utils package, which provides user-space tools for interacting with GPIO lines via the Linux GPIO character device interface.

.. code-block::

   sudo apt install libgpiod-utils

Each ``gpiochip`` represents a bank of GPIO pins. For example, ``gpiochip6`` contains pins 1 to 8.

1. **Identify the GPIO Pin:**

   - You can list available GPIO lines using:

   .. code-block::

      gpioinfo

2. **Setting GPIO Pin Values:**

   - To set a GPIO pin value (HIGH or LOW), use the following command:

   .. code-block::
   
         gpioset gpiochip6 <pin_number>=<value>

   - ``<pin_number>``: The pin number (1 to 8).
   - ``<value>``:
      - ``1`` — Set pin ``HIGH`` (active)
      - ``0`` — Set pin ``LOW`` (inactive)

   - For example, Set pin ``1`` to ``LOW``:

   .. code-block::
         
      gpioset gpiochip6 1=0

   - For example, Set pin ``3`` to ``HIGH``:

   .. code-block::

      gpioset gpiochip6 3=1

   - For example, Set multiple pins at once:

   .. code-block::

      gpioset gpiochip6 2=1 4=0

3. **Reading GPIO Pin Values**

   - To check the current value of a GPIO pin, use:

   .. code-block::

      gpioget gpiochip6 <pin_number>

   - For example, Get the value of pin ``5``:

   .. code-block::

      gpioget gpiochip6 5

   - It will output either ``0`` (LOW) or ``1`` (HIGH).

.. note::

   - Ensure you have the correct permissions to access GPIOs. You may need to run these commands with sudo.
      
   - The gpiochip6 represents the GPIO controller, and the pin numbers (1 to 8) correspond to the GPIO lines.

Example of using the GPIO protocol
----------------------------------

This example demonstrates controlling an LED using the GPIO protocol.

- **Setting the GPIO pin high** will turn on the LED.
- **Setting the GPIO pin low** will turn off the LED.

Means **high signal on the GPIO pin** activates the connected device and **low signal on the GPIO pin** deactivates the connected device.