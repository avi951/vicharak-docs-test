
#######
USB 2.0
#######

.. _usb_usage_linux:

Axon has two USB **2.0 port** ( **480 Mbps** ). This guide explains how to use and inspect USB 2.0 interfaces on a Linux system.

.. image:: /_static/images/rk3588-axon/axon-usb2.webp
   :width: 74%

Basic Utilities and Commands
============================

List Connected USB Devices
--------------------------

Use ``lsusb`` to display information about USB buses and the devices connected to them.

.. code-block:: bash

    vicharak@vicharak:~$ lsusb -t
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=ehci-platform/1p, 480M
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=ohci-platform/1p, 12M
    /:  Bus 005.Port 001: Dev 001, Class=root_hub, Driver=ohci-platform/1p, 12M
    /:  Bus 006.Port 001: Dev 001, Class=root_hub, Driver=ehci-platform/1p, 480M
        |__ Port 001: Dev 005, If 0, Class=Mass Storage, Driver=usb-storage, 480M


What it shows:

- USB Bus number (Bus 003, 004, 005 and 006)

- Device number (Device 001)

- Vendor ID and Product ID 

- Manufacturer and device name

To get verbose information:

.. code-block:: bash

   lsusb -v

To filter by a specific device ID:

.. code-block:: bash

   lsusb -d <vendor>:<product>

.. _usb-debug:

USB Device Speed and Topology
-----------------------------

Use `usb-devices` to print detailed information:

.. code-block:: bash

   usb-devices

Or read from `/sys` directly:

.. code-block:: bash

   cat /sys/bus/usb/devices/usb*/speed

Mount USB Storage Devices
-------------------------

Check kernel log after device is plugged in:

.. code-block:: bash

   dmesg | grep -i usb

Find your device (e.g., `/dev/sda1`) and mount it:

.. code-block:: bash

   sudo fdisk -l
   sudo mount /dev/sda1 /mnt

To unmount:

.. code-block:: bash

   sudo umount /mnt

Live USB Debugging
-------------------

Use ``dmesg`` to view logs:

.. code-block:: bash

   dmesg | grep -i usb

.. code-block:: bash

   dmesg -w   # watch live

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
