.. _axon-mini-qdl-raw-image:

######################################
Axon Mini Image Flashing Guide
######################################

This document explains how to flash OS images to supported storage devices on
Axon Mini using the Qualcomm Device Loader (QDL).

Supported Boot / Flash Devices
==============================

- eMMC
- UFS

Download Image
==============

Download the Axon Mini Debian image package for your target storage (includes
``prog_firehose_ddr.elf``, ``rawprogram*.xml``, and ``patch*.xml``) from
:ref:`axon-mini-downloads`.

Example package names:

.. code-block:: console

   V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc.tar.gz
   V1.0_vicharak_axon-mini_7.1_02122024-debian-ufs.tar.gz

Uncompressing the Image
=======================

.. code-block:: console

   tar -xvf <download_image.tar.gz>
   cd <extracted_image_directory>

The extracted directory should contain files similar to:

- ``prog_firehose_ddr.elf``
- ``rawprogram*.xml``
- ``patch*.xml``
- partition / image binaries referenced by the XML files

Entering EDL Mode
=================

Before flashing, put Axon Mini into EDL mode:

1. Power off the board (or disconnect power).
2. Hold the **EDL** button.
3. Connect / apply power while holding EDL.
4. Release the EDL button.

The board should enumerate as a Qualcomm download device (**PID ``0x9008``**).

Verify enumeration
------------------

.. tab-set::

   .. tab-item:: Linux

      Run ``lsusb``:

      .. code-block:: console

         lsusb

      Expected output:

      .. code-block:: console

         Bus 001 Device 068: ID 05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)

   .. tab-item:: Windows

      In Device Manager, the board should appear as a Qualcomm download / QDL
      device (PID ``9008``):

      .. image:: /_static/images/qcs6490-axon-mini/axon-mini-windows-edl.png
         :width: 50%
         :alt: Axon Mini in EDL mode on Windows Device Manager

.. _axon-mini-flash-image-emmc:

Flashing Image to eMMC
======================

With Axon Mini in **EDL mode**, flash using QDL with ``-s emmc``:

.. tab-set::

   .. tab-item:: Linux

      Follow: :doc:`linux-qdl-tool`

      .. code-block:: console

         sudo <qdl_tool_path>/QDL_2.7.1_Linux_x64/qdl -s emmc --allow-fusing prog_firehose_ddr.elf rawprogram*.xml patch*.xml

   .. tab-item:: Windows

      Follow: :doc:`windows-qdl-tool`

      .. code-block:: console

         & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s emmc --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

.. _axon-mini-flash-image-ufs:

Flashing Image to UFS
=====================

.. note::

   **UFS provisioning is already done** on Vicharak-shipped UFS modules. Modules
   are verified before shipment, so you normally do **not** need to provision
   again before flashing.

   Provisioning is required only if you are flashing a **brand-new** (unprovisioned)
   UFS module, or if you need to change the LUN layout. See
   :doc:`ufs-provisioning` for details.

With Axon Mini in **EDL mode**, flash using QDL with ``-s ufs``:

.. tab-set::

   .. tab-item:: Linux

      Follow: :doc:`linux-qdl-tool`

      .. code-block:: console

         sudo <qdl_tool_path>/QDL_2.7.1_Linux_x64/qdl -s ufs --allow-fusing prog_firehose_ddr.elf rawprogram*.xml patch*.xml

   .. tab-item:: Windows

      Follow: :doc:`windows-qdl-tool`

      .. code-block:: console

         & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s ufs --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

Successful Flash
================

When flashing completes successfully, the tool reports:

.. code-block:: console

   26 patches applied
   partition 0 is now bootable

After that:

1. Disconnect power from Axon Mini.
2. Power on the board normally (do **not** hold the EDL button).
3. The board should boot from the storage you flashed (eMMC or UFS).

.. warning::

   Ensure the board remains in EDL mode and connected over USB for the entire
   flash process. Interrupting the flash can leave the board unbootable until
   it is re-flashed.

.. seealso::

   - :ref:`axon-mini-qdl-tool-guide`
   - :doc:`ufs-provisioning`
   - :ref:`axon-mini-downloads`
   - :ref:`axon-mini-getting-started`
