.. _axon-mini-windows-qdl-tool:

###################
Windows QDL Tool
###################

This guide explains how to install the Qualcomm Device Loader (QDL) on Windows
and flash an image to Axon Mini storage (eMMC or UFS).

Download QDL Tool
=================

Download the Windows QDL package:

`Qualcomm Device Loader (Windows) <https://softwarecenter.qualcomm.com/api/download/software/tools/Qualcomm_Device_Loader/Windows/2.7.1/QDL_2.7.1_Win_x64.zip>`_

Extract the archive, then open the extracted ``QDL_Win_x64`` directory.

Install WinUSB Driver
=====================

1. Open the QDL folder.
2. Run ``install_driver.bat``.

   a. You will see a **File Open - Security Warning** dialog. Click **Run**:

   .. image:: /_static/images/qcs6490-axon-mini/axon-mini-qdl-installation-2.png
      :width: 50%
      :alt: QDL install_driver.bat File Open Security Warning

   b. After that, the terminal should show that the driver was installed
      successfully (``qcserlib.inf``):

   .. image:: /_static/images/qcs6490-axon-mini/axon-mini-qdl-installation-1.png
      :width: 50%
      :alt: QDL WinUSB driver qcserlib.inf installed successfully

.. _axon-mini-windows-enter-edl-mode:

Entering EDL Mode
=================

Before flashing, put Axon Mini into EDL mode:

1. Power off the board (or disconnect power).
2. Hold the **EDL** button.
3. Connect / apply power while holding EDL.
4. Release the EDL button.

The board should enumerate as a Qualcomm download device (**PID ``0x9008``**).

In Device Manager, the board should appear as a Qualcomm download / QDL device
(PID ``9008``):

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-windows-edl.png
   :width: 50%
   :alt: Axon Mini in EDL mode on Windows Device Manager

Flash Image to eMMC
===================

1. Download the Debian eMMC image package (with XML flashing files) from
   :ref:`axon-mini-downloads`.

2. Extract the image package and enter the directory:

.. code-block:: console

   tar -xvf V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc.tar.gz
   cd V1.0_vicharak_axon-mini_7.1_02122024-debian-emmc

3. Put Axon Mini into **EDL mode** (see :ref:`axon-mini-windows-enter-edl-mode`).

4. Run QDL from PowerShell (or Command Prompt):

.. code-block:: console

   & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s emmc --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

Example:

.. code-block:: console

   PS C:\Users\Vicharak\Downloads\QCM6490_bootbinaries\QCM6490_bootbinaries> & "C:\Users\Suraj Sonawane\Downloads\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s emmc --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

Expected output (abbreviated):

.. code-block:: console

   Flashing device (PID 0x9008, serial: 2E5ABDDD)
   device is already in Firehose mode, skipping Sahara
   waiting for Firehose programmer...
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

3. Put Axon Mini into **EDL mode** (see :ref:`axon-mini-windows-enter-edl-mode`).

4. Run QDL from PowerShell (or Command Prompt) with ``-s ufs``:

.. code-block:: console

   & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s ufs --allow-fusing .\prog_firehose_ddr.elf .\rawprogram*.xml .\patch*.xml

.. note::

   ``-s ufs`` selects UFS as the target storage device.

.. note::

   If wildcards are not expanded in your shell, list each ``rawprogram`` /
   ``patch`` XML file explicitly in the command.

5. After a successful flash, disconnect power, then power on the board normally
   (without holding the EDL button).

.. warning::

   Do not interrupt flashing once it has started. Wait until you see
   ``partition 0 is now bootable``.

For the full eMMC / UFS flash overview, see :doc:`qdl-raw-image`.
