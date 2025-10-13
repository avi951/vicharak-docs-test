Vicharak Board Backup
=====================

.. warning::

    We recommend to use Vicharak 6.1 kernel and latest `Ubuntu 24.04 Noble Numbat
    <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble/>`_ , in order to support Board Backup. Flash Image
    using this `Documentation </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon linux-headers-6.1.75-axon

.. _backup_options:

.. note::

	You wont be able to take the backup of a running system. Say, you want to backup data from eMMC, then you would need to boot from another device, such as SD-Card, NVMe or SATA and take the backup after booting from that device.

	Two types of backup have been provided.

	1. Full Backup: This option is used to backup the entire software stack including the loaders, bootloader, kernel and rootfs. This creates a flashable image of the board.
	2. Rootfs Backup: This option is used if you only want to backup the rootfs of your board. It uses the lossless gzip compression and creates a .tar.gz file of your rootfs.

Getting latest vicharak-config
------------------------------

Device Backup can be enabled through the latest update of vicharak-config. To get the latest version of vichrak-config, run commands given below:

.. code:: console

   sudo apt update
   sudo apt install vicharak-config

Board Backup through vicharak-config
------------------------------------

**Steps to follow for Board Backup**

1. Open a terminal window (``Ctrl+Alt+T``).

2. Run command ``sudo vicharak-config`` in it.

3. Select ``Advanced Options`` option in it by pressing ``Enter`` key.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Please select an option below:                                                           │
    │                                                                                          │
    │                                   System Maintenance                                     │
    │                                       Hardware                                           │
    │                                       Overlays                                           │
    │                                     Connectivity                                         │
    │                                   Advanced Options                                       │
    │                                     User Settings                                        │
    │                                     Localization                                         │
    │                                         About                                            │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    │                                                                                          │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

4. Select ``Board Backup`` option.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Please select an option below:                                                           │
    │                                                                                          │
    │                                        Mali GPU                                          │
    │                                     Display Options                                      │
    │                                       VNC Server                                         │
    │                                  USB Advanced features                                   │
    │                                      Board Backup                                        │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

5. Select the device which contains the system which you want to backup. The drive which has booted the system will not be shown as backing up a running system may lead to data corruption.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Select the drive which you want to backup:                                               │
    │                                                                                          │
    │                      /dev/sda	 14.6G  Cruzer\x20Blade   disk                         │
    │                      /dev/mmcblk1	 14.8G  		  disk                         │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

6. Read this :ref:`note <backup_options>` and decide which backup option you want to select. Then, select the required backup option and press ``Enter``. Then, insert a drive in which you want to take your backup into the board. 

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Available Backup Options:                                                                │
    │                                                                                          │
    │                          Full Backup (Creates a flashable image)                         │
    │                          Rootfs Backup (Only copies root filesystem)                     │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

7. Select the drive in which you want to store the backup file. Suppose you want to store backup in ``SanDisk\x203.2Gen1``. Select ``/dev/sda   57.3G   SanDisk\x203.2Gen1   disk`` and press ``Enter``.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Available drives for backup:                                                             │
    │                                                                                          │
    │                          /dev/sda   57.3G   SanDisk\x203.2Gen1   disk                    │
    │                          /dev/sdb   14.6G   Cruzer\x20Blade      disk                    │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

8. Now, select the partition in which you want to store the backup file, and press ``Enter``.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Available partitions for selected disk:                                                  │
    │                                                                                          │
    │                                 /dev/sda1   15G     part                                 │
    │                                 /dev/sda2   15G     part                                 │
    │                                 /dev/sda3   27.3G   part                                 │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

9. You will see Warning Page saying the process will take time. Click on ``yes`` and the backup process will start.

10. Once the Backup is complete you will get the following log in vicharak-config.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ [ OK ] Backup Complete!                                                                  │
    │                                                                                          │
    │ Backup file created at:                                                                  │
    │ /media/vicharak/58fa9c45-0540-42a9-aa79-5911a3f73616/vicharak_axon_backup                │
    │ /axon_rootfs_backup20250709_122223.tar.gz                                                │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

Flashing the backup file to a board
-----------------------------------

.. tab-set::

   .. tab-item:: Full Backup Image

      Rockchip offers the RKDevTool as a fundamental development tool for Windows and MacOS, and the Linux Upgrade Tool for Linux. A loader will be needed to be able to flash the backup image to the board. Download the loader from this `link <https://downloads.vicharak.in/vicharak-axon/rk3588_spl_loader_v1.14.113.bin>`_. Using this tool will flash the board and erase all previous data.

      .. tab-set::

         .. tab-item:: Linux

            1) Enter Maskrom Mode in Axon using this `video guide <https://www.youtube.com/watch?v=rW-R1MJhBGA>`_.

            2) Setup the upgrade_tool using this :ref:`guide <install-upgrade-tool>`. Only follow this guide for downloading and setting up upgrade_tool. Once downloaded, navigate to the directory of upgrade_tool.

            3) Using ``ld`` option of upgrade_tool check whether Axon is being detected.

            .. raw:: html

               <br>

            .. code-block:: console

               $ sudo ./upgrade_tool ld
               List of rockusb connected(1)
               DevNo=1 Vid=0x2207,Pid=0x350b,LocationID=213   Mode=Maskrom   SerialNo=

            4) Use ``db`` option upgrade_tool to load the bootloader binary.

            .. raw:: html

               <br>

            .. code-block:: console

               $ sudo ./upgrade_tool db /path/to/rk3588_spl_loader_v1.xx.xxx.bin
               Download boot ok.

            5) Now using the ``wl`` option write the image to the board.

            .. raw:: html

               <br>

            .. code-block:: console

               $ sudo ./upgrade_tool wl 0 /path/to/backup/axon_full_backupYYYYMMDD_HHMMSS.img
               Start to write axon_full_backup20250712_112731.img at 0x0...
               Write LBA from file (100%)

            6) Finally reset the board using ``rd`` option with upgrade_tool. The backup image has been successfully flashed to the board.

            .. raw:: html

               <br>

            .. code-block:: console

               $ sudo ./upgrade_tool rd
               Reset Device OK.

         .. tab-item:: Windows

            1) Enter Maskrom Mode in Axon using this `video guide <https://www.youtube.com/watch?v=rW-R1MJhBGA>`_.

            2) Install USB Drivers-Assistant and RKDevTool using this :ref:`guide <usb-driver>`. Only follow installation section and return to this document.

            3) You will see ``Found One MASKROM Device`` message in the bottom left corner. If you see ``No Devices Found``, it would mean device not in MASKROM mode.

            4) Click on ``Download Image`` tab and make the following changes. Correctly select paths for the Loader and Image generated during backup and then click on ``Run``.

            .. image:: /_static/images/backup_rkdev.png
               :width: 500px

            5) Flashing image has completed. The board should reset automatically. If it still shows ``Found One MASKROM Device`` message, navigate to the ``Advanced Function`` tab. Then click on ``ResetDevice``.

            .. image:: /_static/images/backup_rstdev.png
               :width: 500px

         .. tab-item:: MacOS

            1) Using these commands install RKDevTool on MacOS.

            .. raw:: html

               <br>

            .. code-block:: console

               % brew install automake autoconf libusb pkg-config git wget
               % git clone https://github.com/rockchip-linux/rkdeveloptool
               % cd rkdeveloptool
               % autoreconf -i
               % ./configure
               % make -j $(nproc)
               % cp rkdeveloptool /opt/homebrew/bin/

            2) Enter Maskrom Mode in Axon using this `video guide <https://www.youtube.com/watch?v=rW-R1MJhBGA>`_.

            3) Use rkdeveloptool command with ``ld`` option to list available devices.

            .. raw:: html

               <br>

            .. code-block:: console

               % rkdeveloptool ld
               DevNo=1   Vid=0x2207,Pid=0x350b,LocationID=104   Maskrom

            4) Use rkdeveloptool command with ``db`` option to load the bootloader in the device.

            .. raw:: html

               <br>

            .. code-block:: console

               % rkdeveloptool db /path/to/rk3588_spl_loader_v1.xx.xxx.bin
               Downloading bootloader succeeded.

            5) Use rkdeveloptool command with ``wl`` option to write the image from 0x0 address.

            .. raw:: html

               <br>

            .. code-block:: console

               % rkdeveloptool wl 0 /path/to/axon_full_backupYYYYMMDD_HHMMSS.img
               Write LBA from file (100%)

            6) Use rkdeveloptool command with ``rd`` option to reset the device.

            .. raw:: html

               <br>

            .. code-block:: console

               % rkdeveloptool rd
               Reset Device OK.

   .. tab-item:: Compressed Rootfs Tar

      .. note::

         If you don’t have access to a Linux host, it is recommended to boot the board from a storage device other than the one where you want to restore the rootfs. For example, if you plan to copy the rootfs to the eMMC, boot the board from an alternative device such as an SD card, SATA drive, NVMe, or USB. Once booted, proceed with step 5 from the Linux guide and use the tar command to copy the rootfs.

         You may use third-party tools to mount an ext4 filesystem like WinSCP on Windows and macFUSE on MacOS, but it is generally not recommended.

      .. tab-set::

         .. tab-item:: Linux

            1) Connect Axon to a PC using a USB Cable.

            2) Follow this :ref:`Using Serial Console guide <axon-serial-console>` to serially connect to Axon.

            3) Reboot the device and quickly press ``Ctrl + c`` to enter the U-Boot console.

            4) From U-Boot Console type ``ums 0 mmc 0``. This will expose the eMMC as a USB connected to the host computer. If you have installed the OS in some other device like SD-Card or NVMe, you can use ``mmc list`` to find out the exact device number for that device. Replace ``ums 0 mmc 0`` by ``ums 0 mmc <device-number>``.

            .. warning::

               If you wish to remove the current root filesystem, ensure that you delete files only from the board’s 6th partition and not from any system-related partitions. Also make sure, not to delete the partition directory itself—remove only the files inside it.

            5) Ensure that the rootfs (6th partition) is mounted, if not mount it manually using ``mount`` command. If you want to remove current rootfs from the board then delete all the data from the mounted partition. Now using ``tar`` command copy the contents of the compressed backup to the device. Then run ``sync`` command to flush the file system buffer, ensuring all the data is written to eMMC.

            .. raw:: html

               <br>

            .. code-block:: console

               $ sudo tar -xvzf /path/to/axon_rootfs_backupYYYYMMDD_HHMMSS.tar.gz -C /path/to/rootfs_partition(6th partition)/of_device/
               $ sync

            6) Now, unmount all the mounted paritions of the exposed disk using the ``umount`` command.

            7) Finally, go to the previously opened serial console of the board and end the ums process using ``Ctrl + c``. Then enter the ``reboot`` command in the u-boot console. Your board will boot into the newly copied rootfs and all the data, packages, environments etc. will be restored.

..
         .. tab-item:: Windows

            Instructions for Windows with rootfs tar go here.

         .. tab-item:: MacOS

            Instructions for macOS with rootfs tar go here.
