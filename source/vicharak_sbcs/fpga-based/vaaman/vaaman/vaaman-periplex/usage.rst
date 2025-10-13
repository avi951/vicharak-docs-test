Usage guide for Periplex
========================

.. variable 
.. _GPIO docs: https://docs.vicharak.in/_static/files/Vaaman0.3_Pinout_Guide_Rev0.3.pdf
.. _DTS demo: https://www.youtube.com/watch?v=fVuv8Rr6arM
.. _JSON video: https://www.youtube.com/watch?v=iiADhChRriM

What is periplex-sync ?
-----------------------

- ``periplex-sync`` is a command-line tool that can be run on the linux terminal.  
  You can run the following command to get help:

  .. code-block:: console

      vicharak@vicharak:~$ sudo periplex-sync -h
      Usage: periplex-sync <command> [arguments]
      Commands:
          -h/help                                For help                
          -p/path           [Json_file]          Give json file          
          -s/status                              Status of periplex      
          -v/verbose                             Verbose information     
          -a/app            [App name]           Attach applications     


How to use periplex-sync ?
--------------------------

Create the json file
````````````````````

- The ``periplex-sync`` command requires a ``<filename>.json`` configuration file.
- ``<file_name>.json`` is your ``.json`` file defining the peripherals and pin configurations. 

.. tip::
    - You can refer this video to know what is json file `JSON video`_.
    - You can refer this documentation for gpio pins name `GPIO docs`_.

- For example, if you need to configure  ``3-UARTs`` and  ``2-I2Cs`` devices, you can define the ``TX`` and ``RX`` pins for ``UARTs`` and the ``SCL`` and ``SDA`` pins for ``I2Cs`` like this, For :download:`download JSON file </_static/files/periplex1.json>`

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
            }
        ],
        "i2c": [
            {
                "id": 3,
                "SCL": "GPIOT_RXP27",
                "SDA": "GPIOT_RXP24"
            },
            {
                "id": 4,
                "SCL": "GPIOL_63",
                "SDA": "GPIOT_RXN24"
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

.. note::

    1. Increase the ``id`` parameter by 1 sequentially. Gaps in the ``id`` sequence are not allowed.
    2. Duplicate pins are not allowed, for example, each pin (e.g., ``GPIOT_RXP28``) can only be assigned once.
    3. Ensure the ``JSON`` file has the following sequence of peripheral's:

    .. code-block:: json
        
            {
                "uart": [],
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

    4. Do not skip any peripherals. If a peripheral is not required, leave the brackets empty for that peripheral.   

- Run the ``periplex-sync`` command:
.. code-block::

    sudo periplex-sync -p <filename>.json

- When running ``periplex-sync``, you may be prompted to edit the Device Tree Source Overlay (DTS) file.

.. tip::
    For non-linux background, DTS reference documentation, see the video: `DTS demo`_.

- The DTSO file includes specific configuration details that need to be customized for your device.
- If any issues occur during the process, the error message will display on the screen. 

Reboot the board
````````````````

- After making changes in the DTSO, a system reboot is required to apply these configurations.

After reboot
````````````

- After rebooting, all configurations have been successfully applied.
- You got the ``3-UARTs`` and ``2-I2Cs`` devices like this: 

.. raw:: html

    <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 75%; height: 650px; overflow: auto; white-space: pre-wrap;">
        vicharak@vicharak:~$ ls /dev
        block            gpiochip3     mmcblk0       tty0   tty30  tty60        vcs7
        bus              gpiochip4     mmcblk0boot0  tty1   tty31  tty61        vcsa
        char             gpiochip5     mmcblk0boot1  tty2   tty32  tty62        vcsa1
        disk             hdmi_hdcp1x   mmcblk0p1     tty3   tty33  tty63        vcsa2
        dma_heap         hwrng         mmcblk0p2     tty4   tty34  ttyFIQ0      vcsa3
        dri              i2c-0         mmcblk0p3     tty5   tty35  <span style="color:red;">ttyPERI0</span>    vcsa4
        fd               i2c-1         mmcblk0p4     tty6   tty36  <span style="color:red;">ttyPERI1</span>     vcsa5
        hugepages        i2c-4         mmcblk0p5     tty7   tty37  <span style="color:red;">ttyPERI2</span>     vcsa6
        input            i2c-7         mmcblk0p6     tty8   tty38  ttyS0        vcsa7
        mapper           i2c-9         mmcblk0p7     tty9   tty39  ubi_ctrl     vcsu
        mqueue           i2c-10        mmcblk0p8     tty10  tty40  uhid         vcsu1
        net              <span style="color:red;">i2c-11</span>        mmcblk0rpmb   tty11  tty41  uinput       vcsu2
        pts              <span style="color:red;">i2c-12</span>        mpp_service   tty12  tty42  urandom      vcsu3
        shm              iep           null          tty13  tty43  usbmon0      vcsu4
        snd              iio:device0   periplex      tty14  tty44  usbmon1      vcsu5
        usb-ffs          initctl       port          tty15  tty45  usbmon2      vcsu6
        v4l              kmsg          ptmx          tty16  tty46  usbmon3      vcsu7
        autofs           log           ram0          tty17  tty47  usbmon4      vendor_storage
        btrfs-control    loop-control  random        tty18  tty48  usbmon5      vhci
        cec0             loop0         rfkill        tty19  tty49  usbmon6      video-dec0
        console          loop1         rga           tty20  tty50  v4l-subdev0  video-enc0
        cpu_dma_latency  loop2         rk_cec        tty21  tty51  v4l-subdev1  video0
        crypto           loop3         rtc           tty22  tty52  v4l-subdev2  video1
        drm_dp_aux0      loop4         rtc0          tty23  tty53  vcs          video2
        fb0              loop5         spidev0.0     tty24  tty54  vcs1         video3
        full             loop6         stderr        tty25  tty55  vcs2         video4
        fuse             loop7         stdin         tty26  tty56  vcs3         watchdog
        gpiochip0        mali0         stdout        tty27  tty57  vcs4         watchdog0
        gpiochip1        media0        sw_sync       tty28  tty58  vcs5         zero
        gpiochip2        mem           tty           tty29  tty59  vcs6         zram0
    </pre>


.. tip::
    
    For example, you can try diffrent ``json`` configurations: 

    I. **1-UART**, **1-I2C**, **1-GPIO**, **1-PWM**, and **1-SPI**:
    
    - If you need to configure ``1-UART``, ``1-I2C``, ``1-GPIO``, ``1-PWM`` and ``1-SPI`` device, define each peripheral with its specific pins. For ``SPI``, the ``SLAVE`` parameter specifies the number of slave devices. If you set ``SLAVE`` to 2, you must define both ``SLAVE-0`` and ``SLAVE-1`` pins. If only one slave device is used, set ``SLAVE`` to 1 and define only the ``SLAVE-0`` pin. 
    - For :download:`download JSON file </_static/files/periplex2.json>`
    
    II. **26-UARTs**, **10-I2Cs**, and **12-PWMs**:
    
    - If you need to configure  ``26-UARTs``, ``10-I2Cs`` and ``12-PWMs`` devices, you can define the ``TX`` and ``RX`` pins for ``UARTs`` and the ``SCL`` and ``SDA`` pins for ``I2Cs`` and the ``PWM`` pins for ``PWMs``.
    - For :download:`download JSON file </_static/files/periplex3.json>`
    
    
    III. **40-UARTs**:
    
    - If you need to configure ``40-UARTs`` devices, you can define the ``TX`` and ``RX`` pins for ``UARTs``.
    - For :download:`download JSON file </_static/files/periplex4.json>`

.. note::

    - If you want to test a new JSON configuration, it is mandatory to run the ``periplex-sync`` command again to apply your new configuration.