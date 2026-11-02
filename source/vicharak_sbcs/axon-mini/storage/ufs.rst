#############
UFS 3.1
#############

.. warning::
   This accessory/storage option is coming soon.

The Vicharak-Axon Mini board includes a modular UFS connector that supports
UFS 3.1 storage modules. See
:doc:`UFS 3.1 Storage Module <../axon-mini-accessories/axon-mini-ufs>`
for availability.

Once fitted, the module connects to the SoC’s UFS host controller and provides
expandable, high-speed persistent storage used as the primary boot and root
filesystem media for the operating system. The interface utilizes the UFS
protocol over a MIPI M-PHY link, offering robust data transfer, dedicated boot
partitions, and native compatibility with standard SCSI/UFS stacks in modern
Linux kernels where it is exposed as a standard block device.

.. TODO: Add Hardware image for UFS with the Connectors name Power and Signal Connectors.

.. note::
   Connect the UFS storage module while Axon Mini is powered off to avoid any damage.

UFS connectors
----------------

The UFS 3.1 storage module connects to the board through a pair of 30-pin as shown in above picture, 0.4 mm pitch board-to-board connectors: one carrying the high-speed M-PHY signal lanes and reset, and a separate connector dedicated to power delivery.

- **UFS Signal Connector**: carries the differential TX/RX lane pairs, reference clock, and reset signal.
- **UFS Power Connector**: carries the regulated supply rails and mechanical/ground pins for the module.

Keeping signal and power on separate connectors isolates the high-speed M-PHY lanes from supply-rail switching noise.

Signal connector pinout
-----------------------

.. table::

   ====  ====================  ====  ====================
   Pin    Signal                Pin    Signal
   ====  ====================  ====  ====================
   1      GND                   2      UFS_RESET_N
   3      UFS_TX1_N             4      NC
   5      UFS_TX1_P             6      NC
   7      GND                   8      NC
   9      UFS_TX0_N             10     NC
   11     UFS_TX0_P             12     NC
   13     GND                   14     NC
   15     UFS_REFCLK            16     NC
   17     GND                   18     NC
   19     UFS_RX0_N             20     NC
   21     UFS_RX0_P             22     NC
   23     GND                   24     NC
   25     UFS_RX1_N             26     NC
   27     UFS_RX1_P             28     NC
   29     GND                   30     GND
   ====  ====================  ====  ====================

- **Differential pairs**: TX0 (TX0_P/TX0_N) and TX1 (TX1_P/TX1_N) form the two SoC-to-device transmit lanes; RX0 and RX1 form the two device-to-SoC receive lanes, matching the HS-Gear4, 2-lane configuration of the UFS device.
- **UFS_REFCLK**: reference clock supplied to the UFS device by the host.
- **UFS_RESET_N**: active-low hardware reset to the UFS device, driven by the SoC/PMIC.
- **GND pins** are interleaved between differential pairs to maintain signal integrity on the high-speed lanes.
- **NC pins**: unused pins on this connector are left unconnected (no-connect) on this board variant.

Power connector pinout
----------------------

.. table::

   ======  =================  ======  ====================
   Pin     Signal              Pin     Signal
   ======  =================  ======  ====================
   1–13    VREG_L9B_1P2        2–12    NC
   15–21   VREG_L7B_2P5        14–22   NC
   23–27   VREG_L7B_2P5        24–28   NC
   29      GND                 30      GND
   ======  =================  ======  ====================

.. table::

   ======  ======================
   Pin     Signal
   ======  ======================
   MP1     Mechanical/ground pin
   MP2     Mechanical/ground pin
   MP3     Mechanical/ground pin
   MP4     Mechanical/ground pin
   ======  ======================

- **VREG_L9B_1P2**: 1.2 V supply rail, distributed across multiple pins to share current load across the connector.
- **VREG_L7B_2P5**: 2.5 V supply rail, similarly distributed across multiple pins for current capacity.
- **MP1–MP4**: mechanical pins used for connector retention/grounding, not carrying active signal.
- Both connectors are 30-pin, 0.4 mm pitch board-to-board connectors; mating connector part numbers are board-design-internal and not published in this document.

.. note::

   Pin assignments above are derived from the board schematic and should be cross-checked against the latest schematic revision before use in production or rework, particularly for the exact pin ranges driving each power rail on J5.

.. note::

   Actual achievable throughput on the board depends on the QCS6490 UFS host controller's negotiated gear/lane configuration, PHY tuning, and platform-level constraints — not solely on the NAND device's rated maximum.

Boot behavior and partitions
----------------------------

:ref:`You can find UFS Flashing Guide here (Vicharak Docs) <axon-mini-flash-image-ufs>`

UFS interface on QCS6490
--------------------------

The QCS6490 SoC includes a dedicated UFS host controller (UFSHC) compliant with the JEDEC UFS Host Controller Interface (UFSHCI) specification, paired with a MIPI M-PHY for the physical layer.

- Lanes: 2 (TX + RX differential pairs)
- Negotiated Gear: up to HS-Gear4 (Rate B), auto-negotiated at boot by the UFS host controller and device
- Reference clock: provided by the SoC to the UFS device per JEDEC UFS specification
- Power rails: VCC (2.5V, NAND core), VCCQ (1.2V, I/O), and VCCQ2 (if applicable) are sequenced by the PMIC at boot per the UFS device's power-up timing requirements

.. note::

   On Axon Mini the UFS device is provided as a modular storage accessory mated
   to the board-to-board connectors described above, not as an on-board BGA
   package. Seat the module before powering on the board.

Linux device enumeration
--------------------------

On boot, the Linux kernel's UFS host controller driver (``ufs-qcom``) initializes the UFS link and the SCSI subsystem enumerates the UFS device as a standard SCSI disk.

- The UFS device typically appears as ``/dev/sdX`` (e.g., ``/dev/sda``), the same as SATA or USB mass storage.
- UFS-specific logical units (LUs) such as boot LUs, RPMB, and the main user data LU may also appear as separate block devices or under ``/sys/class/scsi_device/``.
- GPT partitions on the UFS device hold the bootloader stages, boot images, and the root filesystem, depending on the board's partition layout.

.. code-block:: bash

   lsblk
   sudo dmesg | grep -i ufs

to verify the UFS device and its partitions are detected correctly.

Using Linux with the UFS interface
-------------------------------------

- Detecting the device and partitions:

  .. code-block:: bash

    lsblk -f
    sudo fdisk -l /dev/sdX
    cat /sys/block/sdX/device/model

- Inspecting UFS-specific attributes (descriptor, health, gear):

  .. code-block:: bash

    cat /sys/class/scsi_device/*/device/model
    find /sys -iname "*ufs*"

- Creating partitions and filesystems (on a spare/user partition, not the boot partitions):

  .. code-block:: bash

    sudo parted /dev/sdX mklabel gpt
    sudo parted -a optimal /dev/sdX mkpart primary ext4 0% 100%
    sudo mkfs.ext4 /dev/sdX1

- Mounting:

  .. code-block:: bash

    sudo mkdir -p /mnt/data
    sudo mount /dev/sdX1 /mnt/data

- Basic health and identification:

  .. code-block:: bash

    sudo smartctl -a /dev/sdX
    sudo blkid
    sudo lsblk -f

.. warning::

   Do not partition, format, or write to the UFS boot/GPT partitions (typically the lowest-numbered partitions on the device) unless you specifically intend to reflash the bootloader or OS image. Refer to the :ref:`UFS Flashing Guide <axon-mini-flash-image-ufs>` for the supported procedure to flash images directly to UFS.

Troubleshooting
---------------

- UFS device not detected:

  - Check kernel boot logs for UFS host controller initialization errors:

    .. code-block:: bash

      dmesg | grep -i ufs

  - Confirm the ``ufs-qcom`` driver loaded successfully and the link came up (look for gear/lane negotiation messages).
  - If the device is missing entirely after a flash operation, the device may need to be re-flashed via the boot/flashing procedure rather than recovered from a running OS.

- Device detected but partitions missing or corrupted:

  .. code-block:: bash

    sudo fdisk -l /dev/sdX
    sudo file -s /dev/sdX1

  - Check for read/write errors in dmesg that may indicate a UniPro link or PHY issue:

    .. code-block:: bash

      dmesg | grep -iE "ufs|unipro|m-phy"

- Slow or inconsistent throughput:

  - Confirm the negotiated HS-Gear and number of active lanes (should be HS-Gear4, 2-lane under normal operation):

    .. code-block:: bash

      dmesg | grep -i "ufshcd"

  - A device that has fallen back to a lower gear (e.g., due to signal integrity issues or thermal throttling) will show noticeably reduced sequential read/write performance compared to the rated values above.

- Data access issues:

  - Check filesystem integrity on user partitions only:

    .. code-block:: bash

      sudo fsck /dev/sdX1

  - Ensure proper mounting options and permissions.
