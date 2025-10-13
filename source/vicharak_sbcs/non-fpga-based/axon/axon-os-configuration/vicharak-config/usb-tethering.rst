USB Tethering – Usage Guide
===========================

.. warning::
        ⚠️ **Type-C Mode Switching Issues:** The Type-C0 port may not reliably switch between host and device modes. This feature might interfere with other Type-C peripherals, such as USB pen drives. If issues occur, try replugging the device or switching to a different Type-C port.

The latest version of ``vicharak-config`` introduces **USB Tethering** support for seamless SSH access to your Axon via the **TYPE-C0** USB port. In addition to SSH access, the tethering interface can now **share internet from Ethernet to your host machine** over USB.

Key Features
------------

- Plug-and-play SSH access via USB at a fixed IP (``10.42.0.1``)
- Share internet access over USB when the Axon is connected via Ethernet
- Service control via both TUI and systemd

Getting latest vicharak-config
------------------------------

USB-tethering can be enabled through latest update of vicharak-config. To get latest version of vichrak-config, run  below commands:

    .. code::

        sudo apt update
        sudo apt install vicharak-config

This feature is fully supported only on the latest Linux kernel. We recommend upgrading to the latest kernel version for proper functionality.

    .. code::

        sudo apt update
        sudo apt install u-boot-menu
        sudo apt install linux-image-6.1.75-axon linux-headers-6.1.75-axon
        sudo reboot



Accessing USB Tethering Controls
--------------------------------

From the TUI (``vicharak-config`` interface), go to::

    > Advanced Options
        > USB Tethering

You can enable/disable the Tethering Service.

Service Control via systemd
---------------------------

The service controlling USB tethering is::

    advanced-usb@tethering.service

**Commands:**

- Stop the service:

  .. code-block:: bash

      sudo systemctl stop advanced-usb@tethering.service

- Start the service:

  .. code-block:: bash

      sudo systemctl start advanced-usb@tethering.service

- Disable autostart on boot:

  .. code-block:: bash

      sudo systemctl disable advanced-usb@tethering.service

- Enable autostart on boot:

  .. code-block:: bash

      sudo systemctl enable advanced-usb@tethering.service

SSH Access via USB
------------------

Once enabled, connect your host PC to the **TYPE-C0** port of the Axon and SSH directly:

.. code-block:: bash

    ssh vicharak@10.42.0.1

This eliminates the need for serial console or IP discovery.

Internet Sharing over USB
--------------------------

If your Axon is connected to the internet via Ethernet, the host PC will also get internet access via the USB connection.

This is achieved using appropriate **IP forwarding and iptables NAT rules**, which are applied automatically by the ``advanced-usb@tethering.service``.

Technical Details
-----------------

- **IP Address:** Axon (USB device): ``10.42.0.1``, Host (PC): typically ``10.42.0.2``
- **iptables Rules:** Automatically configured to allow NAT routing from USB (``usb0``) to Ethernet (``eth0``)
- **IP Forwarding:** Automatically enabled during tethering
