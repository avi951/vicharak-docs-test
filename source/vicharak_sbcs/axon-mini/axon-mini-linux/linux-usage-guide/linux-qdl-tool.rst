.. _axon-mini-linux-qdl-tool:

#################
Linux QDL Tool
#################

This guide explains how to install the Qualcomm Device Loader (QDL) on Linux
and flash an image to Axon Mini storage (eMMC or UFS).

Download QDL Tool
=================

Download the Linux QDL package:

`Qualcomm Device Loader (Linux) <https://softwarecenter.qualcomm.com/api/download/software/tools/Qualcomm_Device_Loader/Linux/Debian/2.7.1/QDL_2.7.1_Linux_x64.zip>`_

Extract the archive:

.. code-block:: console

   unzip QDL_2.7.1_Linux_x64.zip

Make the ``qdl`` binary executable:

.. code-block:: console

   cd QDL_2.7.1_Linux_x64
   chmod +x ./qdl

.. _axon-mini-linux-enter-edl-mode:

Entering EDL Mode
=================

Before flashing, put Axon Mini into EDL mode:

1. Power off the board (or disconnect power).
2. Hold the **EDL** button.
3. Connect / apply power while holding EDL.
4. Release the EDL button.

The board should enumerate as a Qualcomm download device (**PID ``0x9008``**).

Verify with ``lsusb``:

.. code-block:: console

   lsusb

Expected output:

.. code-block:: console

   Bus 001 Device 068: ID 05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)

Flash Image to eMMC
===================

1. Download the Debian eMMC image package (with XML flashing files) from
   :ref:`axon-mini-downloads`.

2. Extract the image package and enter the directory:

.. code-block:: console

   tar -xvf V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc.tar.gz
   cd V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc

3. Put Axon Mini into **EDL mode** (see :ref:`axon-mini-linux-enter-edl-mode`).

4. Flash the image using QDL:

.. code-block:: console

   sudo <qdl_tool_path>/QDL_2.7.1_Linux_x64/qdl -s emmc --allow-fusing prog_firehose_ddr.elf rawprogram*.xml patch*.xml

Example:

.. code-block:: console

   vicharak@axon-mini:~/Downloads/V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc$ sudo ~/QDL_2.7.1_Linux_x64/qdl -s emmc --allow-fusing prog_firehose_ddr.elf rawprogram*.xml patch*.xml

Expected output (abbreviated):

.. code-block:: console

   Waiting for EDL device
   Flashing device (PID 0x9008, serial: 2E5ABDDD)
   Sahara: sending prog_firehose_ddr.elf (1044480 bytes)
   waiting for Firehose programmer...
   flashed "PrimaryGPT" successfully
   flashed "xbl_a" successfully
   flashed "xbl_b" successfully
   ...
   flashed "system" successfully
   flashed "PrimaryGPT" successfully
   flashed "BackupGPT" successfully
   26 patches applied
   partition 0 is now bootable

.. note::

   ``-s emmc`` selects eMMC as the target storage device.

Flash Image to UFS
==================

.. note::

   UFS provisioning is already done on Vicharak-shipped modules. Provision only
   for a brand-new UFS module or if you need layout changes. See
   :doc:`ufs-provisioning`.

1. Download the Debian UFS image package (with XML flashing files) from
   :ref:`axon-mini-downloads`.

2. Extract the image package and enter the directory.

3. Put Axon Mini into **EDL mode** (see :ref:`axon-mini-linux-enter-edl-mode`).

4. Flash the image using QDL with ``-s ufs``:

.. code-block:: console

   sudo <qdl_tool_path>/QDL_2.7.1_Linux_x64/qdl -s ufs --allow-fusing prog_firehose_ddr.elf rawprogram*.xml patch*.xml

.. note::

   ``-s ufs`` selects UFS as the target storage device.

5. After a successful flash, disconnect power, then power on the board normally
   (without holding the EDL button).

.. warning::

   Do not interrupt flashing once it has started. Wait until you see
   ``partition 0 is now bootable``.

For the full eMMC / UFS flash overview, see :doc:`qdl-raw-image`.
