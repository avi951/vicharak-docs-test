#############
USB 3.1 Gen1
#############

Axon board includes two USB Type-C ports, each supporting USB 3.1 Gen 1 (5 Gbps) and DisplayPort output.
This guide explains how to use and inspect Type-C USB 3.1 Gen1 interfaces on a Linux system. 

.. image:: /_static/images/rk3588-axon/axon-usb3.webp
   :width: 80%

Basic Utilities and Commands
============================

List Connected USB Devices
--------------------------

Use ``lsusb`` to displays information about USB buses and the devices connected to them.

.. code-block:: bash

    vicharak@vicharak:~$ lsusb -t
    /:  Bus 007.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 480M
    /:  Bus 008.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 5000M
    |__ Port 001: Dev 002, If 0, Class=Mass Storage, Driver=uas, 5000M

What it shows:

- USB Bus number (Bus 007, 008)

- Device number (Device 001)

- Vendor ID and Product ID (0bda:8153)

- Manufacturer and device name

To get verbose information:

.. code-block:: bash

   lsusb -v

To filter by a specific device ID:

.. code-block:: bash

   lsusb -d <vendor>:<product>

.. note::

    Also See: :ref:`usb-debug`.

Host/Device Mode detection
---------------------------

- USB DRD (Dual-Role Device)

+--------------------------------------+-------------------------------+
| **USB controller's base address**    |      **Description**          |
+======================================+===============================+
|          ``fc000000.usb``            |          Type-C0              |
+--------------------------------------+-------------------------------+
|          ``fc400000.usb``            |          Type-C1              |
+--------------------------------------+-------------------------------+

Go into ``root`` user by running ``su`` command. Default root password is ``root``.

.. code-block:: bash

   cat /sys/kernel/debug/usb/fc000000.usb/mode

It gives you on which mode usb port act as.

- If user has connected pendrive to Axon on Type-C0 Port, it acts as ``host`` mode.
- If user has connected Axon to Host pc on Type-C0 Port, it acts as ``device`` mode.

USB Command Reference
=====================

This section lists common Linux commands used to interact with USB devices.

+----------------+-------------------------------+
| **Command**    | **Description**               |
+================+===============================+
| ``lsusb``      | List USB devices              |
+----------------+-------------------------------+
| ``usb-devices``| Detailed USB device info      |
+----------------+-------------------------------+
| ``dmesg``      | Kernel logs and hotplug info  |
+----------------+-------------------------------+
| ``mount``      | Mount USB storage device      |
+----------------+-------------------------------+


.. note::

  Speed values:
   - `1.5` Mbps - USB 1.1 (Low Speed)
   - `12` Mbps - USB 1.1 (Full Speed)
   - `480` Mbps - USB 2.0 (High Speed)
   - `5000` Mbps - USB 3.0 / USB 3.1 Gen1 (SuperSpeed)
