##############
PCIe 3.0
##############

The Vicharak-Axon Mini board includes a modular PCIe connector that supports NVMe solid-state drives using the PCI Express (PCIe) Gen 3 interface with one lane (x1).

Specifications
--------------
- Interface: PCIe 3.0 x1
- Protocol: NVMe
- Form factors supported: M-keyed / E-keyed / B-keyed modules via B2B connector (adapter boards may be required for standard M.2 form factors)
- Software support: Linux kernel with NVMe enabled

Hardware installation notes
---------------------------
- Ensure the board is powered off before handling.
- Insert the NVMe drive into the M.2 socket at a ~30-degree angle, aligning the notch with the keying, then press down to seating position and secure with the mounting screw.
- Use a heatsink (optional) if your drive is likely to sustain sustained write workloads to maintain performance and longevity.
- Re-seat if the drive is not detected after the initial insertion.
- If you inserted the NVMe drive while the board is on, reboot the board if you can't detect the NVMe drive.

Usage and management
--------------------

.. note::

  The commands below assume the device is /dev/nvme0n1 and the partition is p1. Run lsblk to confirm your device.



- Installing NVME Cli Tool

  .. code-block:: bash

    sudo apt-get install nvme-cli

- Detecting the device

  Confirm the NVMe endpoint is visible on **PCIe 0**:

  .. code-block:: bash

     lspci

  Expected output:

  .. code-block:: console

     0001:00:00.0 PCI bridge: Qualcomm Technologies, Inc SM8250 PCIe Root Complex [Snapdragon 865/870 5G]
     0001:01:00.0 Non-Volatile memory controller: YEESTOR Microelectronics Co., Ltd GDRAMARS GMT1000 NVMe SSD (DRAM-less) (rev 01)

  List block devices:

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

  List NVMe details with ``nvme-cli``:

  .. code-block:: bash

     sudo nvme list

  Expected output:

  .. code-block:: console

     Node                  Generic               SN                   Model                                    Namespace  Usage                      Format           FW Rev
     --------------------- --------------------- -------------------- ---------------------------------------- ---------- -------------------------- ---------------- --------
     /dev/nvme0n1          /dev/ng0n1            20260300000000001468 SSD 128GB NVME                           0x1          9.76  GB / 128.04  GB    512   B +  0 B   24B5821D

  Or use:

  .. code-block:: bash

     lsblk -o NAME,MODEL,SIZE,MOUNTPOINT

- Checking how many lanes are used by PCIe host interface

  .. code-block:: bash

     sudo lspci -vv -d ::0108 | grep LnkSta

- Partitioning and formatting

  .. code-block:: bash

     sudo fdisk /dev/nvme0n1
     # create partitions as needed
     sudo mkfs.ext4 /dev/nvme0n1p1

- Mounting

  .. code-block:: bash

     sudo mkdir -p /mnt/nvme
     sudo mount /dev/nvme0n1p1 /mnt/nvme

Form factors supported for PCIe 
-------------------------------
.. image:: /_static/images/rk3588-axon/axon-pcie-2230-2242-2260-2280.webp
   :width: 10%

- M.2 M-key PCIe Adapter Board(hat)

  This adapter board provides an M.2 M-key interface for connecting NVMe SSDs to the SBC via PCIe.

  **Features:**

  - M.2 M-key socket for NVMe (PCIe) SSDs
  - Form 2280 is directly supported natively on board
  - Supports SSD form factors: 2230, 2242, 2260 through adapter board
  - Direct PCIe lane routing (no onboard PCIe switch or SATA controller)
  - Passive adapter design

Troubleshooting
---------------
- Not detected by the OS or BIOS

  - Verify the M.2 drive is correctly seated; reseat it if necessary.
  - Update the system firmware/BIOS to the latest version.
  - Try a different NVMe drive to isolate a potential drive issue.
  - Check system logs for NVMe-related messages:

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
- Drive appears but is not mountable

  - Ensure partitions exist and are correctly formatted.
  - Verify file system integrity with fsck or leaved partitions.
  - Confirm proper mounting points and permissions.

