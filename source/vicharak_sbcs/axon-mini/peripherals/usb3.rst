#############
USB 3.1 Gen1
#############

Axon Mini board includes one USB Type-C port, supporting USB 3.1 Gen 1 (5 Gbps) and DisplayPort output.
This guide explains how to use and inspect the Type-C USB 3.1 Gen1 interface on a Linux system.

.. important::

   Axon Mini supports extra USB 3.0 outputs using our :doc:`Quadruple USB 3.0 Hub HAT <../axon-mini-accessories/axon-mini-quad-usb3>` and :doc:`Ethernet and Dual USB 3.0 Hub HAT <../axon-mini-accessories/axon-mini-ethernet-usb3>` modules!

Basic Utilities and Commands
============================

List Connected USB Devices
--------------------------

Use ``lsusb`` to displays information about USB buses and the devices connected to them.

.. code-block:: bash

    lsusb -t

Expected output:

.. code-block:: console

    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 5000M
        |__ Port 001: Dev 002, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
        |__ Port 002: Dev 003, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
        |__ Port 004: Dev 004, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M

What it shows:

- USB Bus number (**Bus 002** is the USB 3.0 ports on the PCIe HAT)

- Negotiated speed (``5000M`` = SuperSpeed / 5 Gbps)

- Device class and driver (for example, ``Mass Storage`` with ``usb-storage``)

.. note::

    **Bus 002** devices operate at SuperSpeed (**5000M** or 5 Gbps). These ports
    are provided by the VIA USB 3.0 controller on the PCIe HAT, which appears in
    ``lspci`` as:

    .. code-block:: bash

       lspci

    Expected output (relevant line):

    .. code-block:: console

       0000:01:00.0 USB controller: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller (rev 01)

    Users can expand Axon Mini with additional high-speed USB 3.0 ports using a
    PCIe HAT. Because these hubs interface directly over the PCIe bus, they offer
    significantly faster data transfer rates (up to 5 Gbps) compared to standard
    USB 2.0 hubs (480 Mbps).

    For more information on expanding with PCIe HATs, see our
    :doc:`../axon-mini-accessories` guide, which includes details on our
    Ethernet/Dual USB 3.0 Hub HAT and Quadruple USB 3.0 Hub HAT.

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

.. code-block:: bash

   sudo cat /sys/kernel/debug/usb/fc000000.usb/mode

It gives you on which mode usb port act as.

- If user has connected pendrive to Axon Mini on the Type-C Port, it acts as ``host`` mode.
- If user has connected Axon Mini to Host pc on the Type-C Port, it acts as ``device`` mode.

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
