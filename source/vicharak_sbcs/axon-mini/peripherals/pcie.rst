##############
PCIe 3.0
##############

.. warning::

    We recommend using the latest `Debian 13 trixie
    <https://downloads.vicharak.in/vicharak-axon-mini/>`_ image in order to
    support the configuration below. Flash Image using this
    :doc:`Documentation </vicharak_sbcs/axon-mini/axon-mini-getting-started>`

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-7.1.0-rc4-mini+ linux-headers-7.1.0-rc4-mini+

Introduction
------------

The Qualcomm Dragonwing QCS6490 processor featured on Axon Mini includes two
independent **PCIe Gen 3** controllers. Both controllers operate in
**Root Complex (RC) mode** and provide high-speed data rates of up to
**8 GT/s** per lane. They are used for point-to-point communication with
peripherals like NVMe SSDs, network cards, and expansion HATs.

On QCS6490:

- Both controllers support **PCIe Gen 3 ×1** (one for NVMe storage, one for modular HAT expansion)

PCIe Gen 3 utilizes the following signal lines for data transmission and control:

- **Transmit Differential Pair (TX±)**: Carries high-speed data from the device to the host.
- **Receive Differential Pair (RX±)**: Carries high-speed data from the host to the device.
- **Reference Clock Pair (REFCLK±)**: Supplies a differential reference clock for data synchronization and serialization.
- **PCIe Reset (PERST#)**: Active-low signal to reset the PCIe interface logic on the device.
- **Wake Request (WAKE#, optional)**: Allows the device to signal the host to transition from a low-power state to an active state.
- **Clock Request (CLKREQ#, optional)**: Used by the device to request a clock from the host when transitioning from low-power to active state.

.. _axon-mini-pcie-implementation:

PCIe 3.0 Implementation on Axon Mini
------------------------------------

Axon Mini provides support for 2 PCIe Gen 3 controllers routed to dedicated
modular connectors.

The following table explains the relationship between the PCIe controllers and
the supported interfaces on Axon Mini:

.. list-table::
   :widths: 20 30 30 20
   :header-rows: 1
   :class: feature-table

   * - **Controller**
     - **Supported Protocols**
     - **Hardware Interface**
     - **Constraints**
   * - PCIe 0
     -
       PCIe 3.0 (×1): ``pcie0``

       SATA (via B-key / adapter where supported)
     - Modular NVMe/SATA Connector
     - PCIe (NVMe) and SATA are mutually exclusive
   * - PCIe 1
     -
       PCIe 3.0 (×1): ``pcie1``
     - Swappable PCIe Modular Port
     - Used for swappable PCIe HAT modules (USB 3.0 / Ethernet expansion)


Modular NVMe/SATA Connector (PCIe 0)
====================================

Axon Mini features a dedicated modular connector mapped to **PCIe 0**. This is
designed for high-speed storage devices such as NVMe SSDs (and SATA where the
module/adapter supports it).

.. TODO: Add Axon Mini PCIe NVMe/SATA connector image
..
   .. image:: /_static/images/qcs6490-axon-mini/axon-mini-pcie-nvme.webp
       :width: 80%

Swappable PCIe Modular Port (PCIe 1)
====================================

For expansion, **PCIe 1** is routed to a modular port that supports swappable
HAT modules.

.. TODO: Add Axon Mini PCIe HAT port image
..
   .. image:: /_static/images/qcs6490-axon-mini/axon-mini-pcie-hat.webp
       :width: 80%

Various HATs can be mounted on this connector to expand the board's capabilities, including:

- Dual Ethernet HAT
- Ethernet + Dual USB 3.0 Hub HAT
- Quadruple USB 3.0 Hub HAT

See :doc:`../axon-mini-accessories` for available PCIe expansion modules.

.. warning::
    PCIe 0 supports either NVMe (PCIe) or SATA at a time, not both
    simultaneously on the same modular storage port.

.. _axon-mini-device-tree-overlays:

Verifying Absence of Conflicting Device Tree Overlays
-----------------------------------------------------

To use PCIe, ensure that no other overlays (such as SATA on the storage port)
are conflicting with the controller you intend to use.

**Steps to follow for Configuration**

1. Open a terminal window (``Ctrl+Alt+T``).
2. Run command ``sudo vicharak-config`` in it.
3. Select ``Overlays`` options in it by pressing ``enter`` key.
4. You will see a Warning Page, click on ``yes`` and select ``Manage Overlays`` option.
5. Identify which PCIe port your device is connected to.

   - For **PCIe 0** (NVMe/SATA port), ensure SATA overlays are disabled if you intend to use PCIe (NVMe).

   - For **PCIe 1** (HAT port), ensure the correct PCIe HAT overlay is enabled for your module.

6. To return back to terminal, keep pressing the ``Esc`` key until you exit from it.
7. In order to enable your configuration, Restart your board or Run command ``sudo reboot`` in terminal.

Checking success of PCIe Communication
======================================

.. warning::

    Many embedded platforms and PCIe devices do not support hot plugging. Ensure the device is connected before powering on or initializing the board.

    Always load device-specific drivers and firmware. While the PCIe link may establish without drivers or firmware, most devices will not enumerate or function correctly unless the appropriate driver and firmware are installed.

The ``lspci`` command can be used to check whether the PCIe device has completed training and a link has been established.

Without a PCIe HAT connected, you will typically see only the two root complexes:

.. code-block:: bash

    lspci

Expected output:

.. code-block:: console

    0000:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
    0001:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]

After connecting a PCIe HAT (for example, Ethernet and Dual USB 3.0 Hub HAT or
Quadruple USB 3.0 Hub HAT) and rebooting, the attached endpoint should also
appear:

.. code-block:: bash

    lspci

Expected output with a USB 3.0 HAT connected:

.. code-block:: console

    0000:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
    0000:01:00.0 USB controller: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller (rev 01)
    0001:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]

When both a PCIe HAT (**PCIe 1**) and an NVMe drive (**PCIe 0**) are connected,
``lspci`` should list endpoints on both root complexes:

.. code-block:: bash

    lspci

Expected output:

.. code-block:: console

    0000:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
    0000:01:00.0 USB controller: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller (rev 01)
    0001:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
    0001:01:00.0 Non-Volatile memory controller: YEESTOR Microelectronics Co., Ltd GDRAMARS GMT1000 NVMe SSD (DRAM-less) (rev 01)

The ``dmesg | grep -i pcie`` command can be used to debug whether the PCIe link
has been correctly initialized.

.. code-block:: console

   vicharak@axon-mini:~$ dmesg | grep -i pcie

.. TODO: Add sample dmesg PCIe initialization logs for Axon Mini

.. note::

   On Axon Mini:

   - **PCIe 0** corresponds to the Modular NVMe/SATA Port.
   - **PCIe 1** corresponds to the Swappable PCIe Modular (HAT) Port.

You can also check negotiated link speed and width:

.. code-block:: console

   sudo lspci -vv | grep -E "LnkCap|LnkSta"

For a healthy Gen 3 link, ``LnkSta`` should report Speed **8GT/s** (or the
highest speed supported by both ends) and the expected lane width
(``Width x1`` for PCIe 0 NVMe and PCIe 1 HAT, depending on the attached device).

Testing NVMe Storage (PCIe 0)
-----------------------------

Follow these steps to interface an NVMe device with Axon Mini:

1. Verify proper overlay settings using the :ref:`guide <axon-mini-device-tree-overlays>` to ensure SATA is not overriding PCIe 0.
2. Insert the NVMe into the Modular NVMe/SATA connector and reboot Axon Mini:

.. code-block:: bash

   sudo reboot

3. Use ``lspci`` to check PCIe Link Training Success:

.. code-block:: bash

   lspci

Expected output:

.. code-block:: console

   0001:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
   0001:01:00.0 Non-Volatile memory controller: YEESTOR Microelectronics Co., Ltd GDRAMARS GMT1000 NVMe SSD (DRAM-less) (rev 01)

4. Use ``lsblk`` to check if NVMe is listed under block devices:

.. code-block:: bash

   lsblk | grep nvme

Expected output:

.. code-block:: console

   nvme0n1          259:37   0 119.2G  0 disk
   ├─nvme0n1p1      259:38   0     4M  0 part
   ├─nvme0n1p2      259:39   0     4M  0 part
   ├─nvme0n1p3      259:40   0   512M  0 part
   ├─nvme0n1p4      259:41   0   288M  0 part
   ├─nvme0n1p5      259:42   0   256M  0 part
   └─nvme0n1p6      259:43   0 118.2G  0 part

Check kernel logs to confirm the NVMe driver has bound to the device:

.. code-block:: bash

   dmesg | grep -i nvme

Expected output:

.. code-block:: console

   [    6.389723] nvme nvme0: pci function 0001:01:00.0
   [    6.414891] nvme 0001:01:00.0: enabling device (0000 -> 0002)
   [    6.431128] nvme nvme0: passthrough uses implicit buffer lengths
   [    6.446353] nvme nvme0: allocated 64 MiB host memory buffer (1 segment).
   [    6.463253] nvme nvme0: 8/0/0 default/read/poll queues
   [    6.479051]  nvme0n1: p1 p2 p3 p4 p5 p6

5. If you have ``nvme-cli`` installed, you can use ``smart-log`` to test NVMe health:

.. code-block:: bash

   sudo apt-get install nvme-cli
   sudo nvme list
   sudo nvme smart-log /dev/nvme0n1

Expected output from ``nvme list``:

.. code-block:: console

   Node                  Generic               SN                   Model                                    Namespace  Usage                      Format           FW Rev
   --------------------- --------------------- -------------------- ---------------------------------------- ---------- -------------------------- ---------------- --------
   /dev/nvme0n1          /dev/ng0n1            20260300000000001468 SSD 128GB NVME                           0x1          9.76  GB / 128.04  GB    512   B +  0 B   24B5821D

.. warning::

   The SSD works without manual driver or firmware installation as support is built into the kernel and the SSD has inbuilt firmware.
