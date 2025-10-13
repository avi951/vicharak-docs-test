:orphan:

.. _vaaman-maskrom-mode:

#####################
 Vaaman Maskrom Mode
#####################

The Vicharak Vaaman board has a special mode called "Maskrom mode."
In this mode, the board can receive commands through a USB connection.
This is useful for tasks like programming and setting up the device.

In Maskrom mode, the Vaaman board can be accessed through multiple pathways,
allowing users flexibility in how they enter this specialized mode.
This mode serves as a bridge between your computer and the board,
facilitating firmware updates, system configurations, and other critical operations.

When you're in Maskrom mode, it's important to follow the steps in this guide
carefully to make sure everything goes smoothly.

This guide will explain how to put your Vicharak Vaaman board into Maskrom mode
using different methods. This will help you make the most of this versatile
single board computer, even if you're new to these things.


Pre-Requisites
---------------

- Vicharak Vaaman board
- Type-C Power Delivery Adapter
- USB to UART Serial Converter (FTDI or PL2303) (optional)
- 2 x USB-C to USB-A Male Cable
- SD-card or NVMe drive (optional as eMMC is already provided)


Methods to enter Maskrom mode
-------------------------------

- Manually shorting the pads using the pogo pin.
- Interrupting the boot process by pressing ``rbrom`` shortcut key from serial console using keyboard.
- Enter maskrom mode from u-boot by running ``rbrom`` command from serial console.
- Pressing the recovery key to enter maskrom mode.

.. note::
    The ``rbrom`` command is only available in u-boot version 2017.09 or
    later. If you are using an older version of u-boot or mainline u-boot, then
    you might not be able to enter maskrom mode.

.. tab-set::

    .. tab-item:: Pogo pins

        .. image:: /_static/images/rk3399-vaaman/vaaman-maskrom-mode.webp
            :width: 50%

        1. Connect Power Delivery ``(PD)`` Cable to Vaaman and connect ``USB Type-C cable`` to the board. 
         
        2. Press the Pogo pin to the pads and continue to hold it.

        .. warning

            Make sure that the SD-Card or NVMe drive is not inserted in the
            board. You may not be able to enter maskrom mode if other storage
            media is inserted.

        3. Press ``Reset`` button on Vaaman.

        4. Release the Pogo pin after the device enumerates on the host.

        5. The device should now be in maskrom mode.
	   You can check verify it by `Linux_Upgrade_Tool <http://github.com/vicharak-in/Linux_Upgrade_Tool>`_ whether device is in Maskrom or not using below command.  

	.. code-block::
		
		./upgrade_tool ld		

        :ref:`Check out Linux Upgrade tool for more details <boot-into-maskrom-mode>`
        
	.. dropdown:: Success Logs in dmesg

            .. code-block::

                [167792.354111] usb 7-1.4.4: new high-speed USB device number 121 using xhci_hcd
                [167792.432282] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167792.432286] usb 7-1.4.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
                [167799.094533] usb 7-1.4.4: USB disconnect, device number 121
                [167802.337917] usb 7-1.4.4: new high-speed USB device number 122 using xhci_hcd
                [167802.416160] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167802.416165] usb 7-1.4.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
                [167815.734169] usb 7-1.4.4: USB disconnect, device number 122
                [167816.418675] usb 7-1.4.4: new high-speed USB device number 123 using xhci_hcd
                [167816.496530] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167816.496535] usb 7-1.4.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
                [167826.230184] usb 7-1.4.4: USB disconnect, device number 123
                [167826.402492] usb 7-1.4.4: new high-speed USB device number 124 using xhci_hcd
                [167826.482774] usb 7-1.4.4: New USB device found, idVendor=2207, idProduct=330c, bcdDevice= 1.00
                [167826.482778] usb 7-1.4.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
                [167826.482779] usb 7-1.4.4: Product: USB-MSC
                [167826.482780] usb 7-1.4.4: Manufacturer: RockChip
                [167826.482781] usb 7-1.4.4: SerialNumber: rockchip
                [167992.118283] usb 7-1.4.4: USB disconnect, device number 124

        .. note::
            If you are not able to enter Maskrom mode on the first try then,
            Reattach the Pogo pin and press the reset key multiple times.

            Try this multiple times until you are able to enter Maskrom mode.

    .. tab-item:: Interrupting boot process

        1. Connect the USB-C cable to the board and your host computer.

        2. Connect the USB to UART serial converter to the board and your
           host computer.

        .. image:: ../../_static/images/rk3399-vaaman/vaaman-serial-uart-pins.webp
           :width: 50%

        3. Power on the board using the power delivery adapter. Open the serial
           console on your host computer.

        4. Quickly press ``CTRL + b`` to interrupt the boot process and force
           the device to enter Maskrom mode.

        5. The device should now be in maskrom mode. Confirm it when the
           LEDs on the board have turned off.

        .. dropdown:: Success Logs

            .. code-block::

                ❯ sudo ./upgrade_tool ld
                Using /home/vicharak/vicharak/rockchip-tools/linux/Linux_Upgrade_Tool/Linux_Upgrade_Tool/config.ini
                List of rockusb connected(1)
                DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=7144	Mode=Maskrom	SerialNo=


    .. tab-item:: U-Boot

        1. Connect the USB-C cable to the board and your host computer.

        2. Connect the USB to UART serial converter to the board and your
           host computer.

        .. image:: ../../_static/images/rk3399-vaaman/vaaman-serial-uart-pins.webp
           :width: 50%

        3. Power on the board using the power delivery adapter.

        4. Interrupt the boot process by pressing ``CTRL + c`` on the serial
            console on your host computer.

        5. Run the ``rbrom`` command to enter maskrom mode.

        6. The device should now be in maskrom mode. Confirm it when the
           LEDs on the board have turned off.

        .. dropdown:: Success Logs

            .. code-block::

                ❯ sudo ./upgrade_tool ld
                Using /home/vicharak/vicharak/rockchip-tools/linux/Linux_Upgrade_Tool/Linux_Upgrade_Tool/config.ini
                List of rockusb connected(1)
                DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=7144	Mode=Maskrom	SerialNo=

    .. tab-item:: Recovery key

        1. Connect the USB cable to the board and power it on using the
           power delivery.

        2. Quickly press recovery key to interrupt the boot process and force
           the device to enter Maskrom mode.

        3. The device should now be in maskrom mode. Confirm it when the
           LEDs on the board have turned off.

        .. dropdown:: Success Logs

            .. code-block::

                ❯ sudo ./upgrade_tool ld
                Using /home/vicharak/vicharak/rockchip-tools/linux/Linux_Upgrade_Tool/Linux_Upgrade_Tool/config.ini
                List of rockusb connected(1)
                DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=7144	Mode=Maskrom	SerialNo=

.. seealso::
        :ref:`Vaaman Linux starting guide <linux-start-guide>`

        :ref:`Frequently Asked Questions <faq>`
