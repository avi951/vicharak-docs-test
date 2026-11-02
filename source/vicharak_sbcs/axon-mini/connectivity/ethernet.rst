#############
Ethernet
#############

.. important::

   Axon Mini provides Gigabit Ethernet ports via our
   :doc:`Dual Gigabit Ethernet HAT <../axon-mini-accessories/axon-mini-dual-ethernet>`
   and
   :doc:`Ethernet and Dual USB 3.0 Hub HAT <../axon-mini-accessories/axon-mini-ethernet-usb3>`
   modules!

These modules connect to the swappable PCIe HAT port (**PCIe 1**) and give
Axon Mini wired Gigabit Ethernet connectivity.

Supported Ethernet Expansion HATs
---------------------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1
   :class: feature-table

   * - **HAT**
     - **Ethernet Ports**
   * - :doc:`Dual Gigabit Ethernet HAT <../axon-mini-accessories/axon-mini-dual-ethernet>`
     - 2 × Gigabit Ethernet (RJ45)
   * - :doc:`Ethernet and Dual USB 3.0 Hub HAT <../axon-mini-accessories/axon-mini-ethernet-usb3>`
     - 1 × Gigabit Ethernet (RJ45) + 2 × USB 3.0

See :doc:`../axon-mini-accessories` for the full list of PCIe expansion modules,
and :doc:`../peripherals/pcie` for PCIe port details.

Connecting the Ethernet HAT
---------------------------

.. note::

   Connect the expansion HAT only while Axon Mini is powered off to avoid damage.

1. Power off Axon Mini and disconnect power.
2. Seat the Ethernet HAT firmly on the swappable **PCIe 1** modular port.
3. Reconnect power and boot the board.
4. Insert one end of an Ethernet cable into an RJ45 port on the HAT and connect
   the other end to a network switch, router, or Ethernet wall outlet.

The Ethernet interface supports auto-negotiation and will automatically
establish a link at the highest speed supported by both the HAT and the
connected network equipment.

Once connected, the link/activity LEDs on the RJ45 connector should illuminate
or blink to indicate a successful network connection.

Verify PCIe Enumeration
-----------------------

After installing the HAT, confirm that the PCIe endpoint is visible:

.. code-block:: bash

   lspci

Expected output:

.. code-block:: console

   0000:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
   0000:01:00.0 USB controller: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller (rev 01)
   0001:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]

The USB controller on **PCIe 1** provides the Ethernet and USB ports on the HAT.
The Realtek USB Ethernet adapter appears on the USB bus (``r8152`` driver):

.. code-block:: bash

   lsusb -t

Expected output:

.. code-block:: console

   /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 5000M
       |__ Port 004: Dev 004, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M

See :doc:`../peripherals/pcie` for more PCIe verification steps.

Linux Support
-------------

Ethernet on these HATs is supported by the Linux kernel. No additional
out-of-tree drivers are required on the official Vicharak image.

Network interfaces are named by the kernel based on the USB topology. With the
Ethernet and Dual USB 3.0 Hub HAT, the interface typically appears as
``enp1s0u4``. Dual Ethernet HATs expose two interfaces.

Basic Linux Commands
--------------------

Check Ethernet Interface
^^^^^^^^^^^^^^^^^^^^^^^^^

List all network interfaces:

.. code-block:: bash

   ip link show

Check the IP address assigned to an Ethernet interface (replace ``enp1s0u4`` with
your interface name):

.. code-block:: bash

   ip addr show enp1s0u4

Expected output when the link is up and DHCP has assigned an address:

.. code-block:: console

   3: enp1s0u4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
       link/ether 9e:8a:93:fc:fe:05 brd ff:ff:ff:ff:ff:ff
       inet 192.168.1.122/24 brd 192.168.1.255 scope global dynamic noprefixroute enp1s0u4

Bring Interface Up or Down
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bring the Ethernet interface up:

.. code-block:: bash

   sudo ip link set enp1s0u4 up

Bring the Ethernet interface down:

.. code-block:: bash

   sudo ip link set enp1s0u4 down

Check Link Status and Speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install ``ethtool`` if not already available:

.. code-block:: bash

   sudo apt install ethtool

Check link status and negotiated speed (replace ``enp1s0u4`` with your interface
name):

.. code-block:: bash

   ethtool enp1s0u4

Test Network Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^^

Check connectivity using ping:

.. code-block:: bash

   ping -c 4 8.8.8.8

Check default gateway and routing table:

.. code-block:: bash

   ip route

Notes
-----

- Use a **CAT5e or higher** Ethernet cable to achieve Gigabit (1000 Mbps) speed.
- Always install or remove the PCIe Ethernet HAT with the board powered off.
- Link LEDs on the HAT RJ45 connector indicate activity and connection status.
- For USB ports on the Ethernet and Dual USB 3.0 Hub HAT, see
  :doc:`../peripherals/usb3`.
