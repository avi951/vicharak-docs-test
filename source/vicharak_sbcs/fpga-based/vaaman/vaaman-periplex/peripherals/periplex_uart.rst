#############
PERIPLEX UART
#############

.. variable 
.. _MINICOM docs: https://linux.die.net/man/1/minicom
 
This section explains how to interact with the ``UART's`` device generated on Vaaman via Periplex.

How to Generate UART's on the Vaaman ?
======================================

1. **Create the json file:**

   - To generate ``5 UART's``, Your need to create a json file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 
   
   .. code-block:: json

         {
            "uart": [
               {
                     "id": 0,
                     "TX": "GPIOT_RXP28",
                     "RX": "GPIOT_RXN28"
               },
               {
                     "id": 1,
                     "TX": "GPIOL_73",
                     "RX": "GPIOL_75"
               },
               {
                     "id": 2,
                     "TX": "GPIOR_173",
                     "RX": "GPIOL_72"
               },
               {
                     "id": 3,
                     "TX": "GPIOR_174",
                     "RX": "GPIOR_178"
               },
               {
                     "id": 4,
                     "TX": "GPIOT_RXN27",
                     "RX": "GPIOR_183"
               }
            ],
            "i2c": [],
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

   - For example, if the JSON configuration for ``5 UART's`` is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``5-UART's`` devices generated through Periplex like this:

   .. raw:: html

        <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 81%; height: 608px; overflow: auto; white-space: pre-wrap;">
            vicharak@vicharak:~$ ls /dev
            autofs           i2c-1         mmcblk0p1    stderr   tty29  tty53     usbmon0      vcsu
            block            i2c-10        mmcblk0p2    stdin    tty3   tty54     usbmon1      vcsu1
            btrfs-control    i2c-4         mmcblk0p3    stdout   tty30  tty55     usbmon2      vcsu2
            bus              i2c-7         mmcblk0p4    sw_sync  tty31  tty56     usbmon3      vcsu3
            cec0             i2c-9         mmcblk0p5    tty      tty32  tty57     usbmon4      vcsu4
            char             iep           mmcblk0p6    tty0     tty33  tty58     usbmon5      vcsu5
            console          iio:device0   mmcblk0p7    tty1     tty34  tty59     usbmon6      vcsu6
            cpu_dma_latency  initctl       mmcblk0p8    tty10    tty35  tty6      v4l          vcsu7
            crypto           input         mmcblk0rpmb  tty11    tty36  tty60     v4l-subdev0  vendor_storage
            disk             kmsg          mpp_service  tty12    tty37  tty61     v4l-subdev1  vhci
            dma_heap         log           mqueue       tty13    tty38  tty62     v4l-subdev2  video0
            dri              loop0         net          tty14    tty39  tty63     vcs          video1
            drm_dp_aux0      loop1         null         tty15    tty4   tty7      vcs1         video2
            fb0              loop2         periplex     tty16    tty40  tty8      vcs2         video3
            fd               loop3         port         tty17    tty41  tty9      vcs3         video4
            full             loop4         ptmx         tty18    tty42  ttyFIQ0   vcs4         video-dec0
            fuse             loop5         pts          tty19    tty43  <span style="color: red; font-weight: bold;">ttyPERI0</span>  vcs5         video-enc0
            gpiochip0        loop6         ram0         tty2     tty44  <span style="color: red; font-weight: bold;">ttyPERI1</span>  vcs6         watchdog
            gpiochip1        loop7         random       tty20    tty45  <span style="color: red; font-weight: bold;">ttyPERI2</span>  vcs7         watchdog0
            gpiochip2        loop-control  rfkill       tty21    tty46  <span style="color: red; font-weight: bold;">ttyPERI3</span>  vcsa         zero
            gpiochip3        mali0         rga          tty22    tty47  <span style="color: red; font-weight: bold;">ttyPERI4</span>  vcsa1        zram0
            gpiochip4        mapper        rk_cec       tty23    tty48  ttyS0     vcsa2
            gpiochip5        media0        rtc          tty24    tty49  ubi_ctrl  vcsa3
            hdmi_hdcp1x      mem           rtc0         tty25    tty5   uhid      vcsa4
            hugepages        mmcblk0       shm          tty26    tty50  uinput    vcsa5
            hwrng            mmcblk0boot0  snd          tty27    tty51  urandom   vcsa6
            i2c-0            mmcblk0boot1  spidev0.0    tty28    tty52  usb-ffs   vcsa7
         </pre>

How to interact with the generated UART's ?
===========================================

The Periplex platform dynamically generates ``UART`` devices, which are accessible through device nodes such as:

.. code-block::
      
   /dev/ttyPERI0
   /dev/ttyPERI1
   /dev/ttyPERI2
   ...

These UART interfaces allow seamless communication between the host system and peripheral devices like microcontrollers, sensors, or other serial-based hardware. 

Example of using the UART protocol
----------------------------------

FTDI USB-to-UART adapter is a popular tool for testing and debugging serial communication, In this setup, we use an FTDI USB-to-UART adapter.The steps below outline how to set up and interact with the generated UART devices.

1. **Connecting the FTDI Adapter**

   - Plug the USB port of FTDI adapter into your your PC.
   - Verify that the adapter is recognized:

   .. code-block::

      sudo dmesg | grep tty

   - You should see an entry like:

   .. code-block::

      [ 123.456789] usb 3-5: ch341-uart converter now attached to ttyUSB0

   - The FTDI adapter typically appears as /dev/ttyUSB0 (or /dev/ttyUSB1 if multiple are connected).
   - After successfully connecting the USB port, plug the UART port of the FTDI adapter into the GPIO pins of the Vaaman board.

2. **Establishing a Serial Connection**

   - You can use a terminal emulator like ``minicom`` to open a session with a UART device, we use ``minicom`` on both side, to enable UART communication, you need to install ``minicom`` on both the side.

   - Use this command to open ``minicom`` on your PC:

   .. code-block::

      sudo apt-get install minicom
      sudo minicom -b 115200 -D /dev/ttyUSB0

   - ``-b 115200``: Sets the baud rate (adjust according to your device's specifications).
   - ``-D /dev/ttyUSB0``: Specifies the UART device to interact with.

   - Use this command to open ``minicom`` on vaaman board:

   .. code-block::

      sudo apt-get install minicom
      sudo minicom -b 115200 -D /dev/ttyPERI0

   - After opening minicom on both sides, simply type characters into minicom, and UART communication between Vaaman and your PC will be established using the FTDI USB-to-UART adapter, You can verify communication by typing some characters in the Minicom session open on your Vaaman board and checking if the data appears in the Minicom session open on your PC.

   .. tip::
      
      - You can refer the `MINICOM docs`_.