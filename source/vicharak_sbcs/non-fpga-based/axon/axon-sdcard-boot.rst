:orphan:

.. _axon-sdcard-boot:

Booting from SD-card
====================

**To make a SD-card bootable, follow these steps:**

Format the SD-card
------------------

Using a suitable file system (such as FAT32 or EXT4) format the SD-card.

.. tab-set::

    .. tab-item:: Windows

        1. Insert the **SD-card** into your computer. Use a USB-to-SD adapter if required.

        2. Open the **File Explorer** and right-click on the SD-card.

        3. Select **Format** from the drop-down menu.

        4. Select the desired file system (e.g., FAT32) and click **Start**.

        5. Click **OK** to confirm the formatting.

    .. tab-item:: Linux

        .. tab-set::
            .. tab-item:: Ubuntu Disks (GUI)

                1. Insert the **SD-card** into your computer. Use USB-to-SD adapter if required.

                2. Open the **Disks** application if you are using a GUI.

                .. image:: ../../_static/images/Disks-overview.webp
                   :width: 50%

                |

                3. Select the SD-card from the left panel.

                .. image:: ../../_static/images/Didsk-sdcard-show.webp
                   :width: 50%

                |

                4. if partition is already present in SD Card then, Click on the **Delete selected partition** icon and select **Delete Partition**.

                .. image:: ../../_static/images/Delete-selected-partition.webp
                   :width: 50%

                |
                
                5. After Deleting **All partition** we can see something like below.

                .. image:: ../../_static/images/deleted-all-patrtition-in-sdcard.webp
                   :width: 50%

                |

                6. Click on **Next** button.

                .. image:: ../../_static/images/Disk-next.webp
                   :width: 50%

                |

                7. Select the desired file system (e.g., FAT32) and click **Create**.

                .. image:: ../../_static/images/create-format-of-ext4.webp
                   :width: 50%

                |

                8. After the successful completion of the process, the **SD card** is formatted with the selected partition.

                .. image:: ../../_static/images/format-complate.webp
                   :width: 50%

                |

            .. tab-item:: Gnome Disks (GUI)

                1. Insert the **SD-card** into your computer. Use USB-to-SD adapter if required.

                2. Open the **Disks** application if you are using a GUI.

                3. Select the SD-card from the left panel.

                4. Click on the **Additional partition options** icon and select **Format Partition**.

                5. Select the desired file system (e.g., FAT32) and click **Next**.

                6. Click **Format** to confirm the formatting.

            .. tab-item:: GNU parted (CLI)

                1. Insert the **SD-card** into your computer. Use USB-to-SD adapter if required.

                2. Open the **terminal** and run the following command to list the available disks:

                .. code-block:: console

                    sudo parted /dev/sdX

                .. note::
                   | You can use the **lsblk** command to list the available disks.
                   | In the above command, sd**X** is the name of the Storage drive.
                   | **`X`** is the number of the Storage drive, it starts from a.

                .. image:: ../../_static/images/parted-overview.webp
                   :width: 50%

                |

                3. the following command to **print** the partition table:

                .. code-block:: console

                    (parted) print

                |

                .. image:: ../../_static/images/parted-partitions-list.webp
                   :width: 50%

                4. **Delete** the existing partitions using the following command:

                .. code-block:: console

                    (parted) rm 1
                    (parted) rm 2
                    ...

                5. After deleting all the partitions, the partition table should look like this:

                .. image:: ../../_static/images/parted-deleted-partitions.webp
                   :width: 50%

                |

                6. Finally, **quit** the parted tool using the following command:

                .. code-block:: console

                    (parted) quit

            .. tab-item:: UNIX fdisk utility (CLI)

                1. Insert the **SD-card** into your computer.

                2. Open the **terminal** and run the following command to list the available disks:

                .. code-block:: console

                    sudo fdisk /dev/sdX

                .. note::
                    | You can use the **lsblk** command to list the available disks.
                    | In the above command, sd**X** is the name of the Storage drive.
                    | **`X`** is the number of the Storage drive, it starts from a.

                3. Press **d** to delete the existing partition. Do this for all the partitions.

                4. After deleting all the partitions, the partition table should be empty.

                5. Finally, press **w** to write the changes to the disk.


Download the bootable image
---------------------------

Obtain the bootable image or operating system files for your desired platform.

.. note::
    | For Axon, you can download the bootable image from the :ref:`Downloads <axon-downloads>` page.
    | The bootable image is available in the `SD-card` section.

Write the image to the SD-card
------------------------------

.. warning::
    | Make sure you have selected the correct SD-card before writing the image.
    | Writing the image to the wrong SD-card will erase all the data on the SD-card.

You can use any disk imaging tool such as Etcher or Win32 Disk Imager to write the image to the SD-card.

For demonstration purposes, we will use the **Balena Etcher tool** to write the image to the SD-card.

.. tab-set::

    .. tab-item:: Balena Etcher (GUI)

        1. Open the **Balena Etcher** tool.

        .. image:: ../../_static/images/balena-start.webp
           :width: 50%

        |

        2. Click on **Select Image** and select the image file.

        .. image:: ../../_static/images/balena-select-image.webp
           :width: 50%

        |

        3. Click on **Select Target** and select the SD-card.

        .. image:: ../../_static/images/balena-select-storage.webp
           :width: 50%

        |

        4. Click on **Flash** to start writing the image to the SD-card.

        .. image:: ../../_static/images/balena-start-flash.webp
           :width: 50%

        |

        5. Once the writing process is complete, click on **Done**.

        .. image:: ../../_static/images/balena-flash-complete.webp
           :width: 50%

    .. tab-item:: UNIX **dd** command (CLI)

        1. Open the **terminal** and run the following command to write the image to the SD-card:

        .. code-block:: console

            sudo dd if=/path/to/image of=/dev/sdX bs=4M status=progress; sync

        .. note::
            | Replace **/path/to/image** with the path to the image file.
            | You can use the **lsblk** command to list the available disks.
            | In the above command, sd**X** is the name of the Storage drive.
            | **`X`** is the number of the Storage drive, it starts from a.

        2. Wait for the writing process to complete.

        3. Once the writing process is complete, Safely eject the **SD-card** from your computer.

Boot from the SD-card
---------------------

After writing the image to the SD-card, follow these steps to boot from the SD-card:

1. Safely eject the **SD-card** from your computer.

2. Insert the **SD-card** into your Axon SBC.

.. image:: ../../_static/images/rk3588-axon/axon-sdcard-boot.webp
   :width: 45%

|

3. **Power-on** the device to initiate the boot process from the SD-card.

Connect the PD cable to the Axon SBC and the PD adapter to the power socket.
Once the power is connected, the board will automatically turn on.

.. danger::
    12V Power Input only! Do not use 5V power input.

.. image:: ../../_static/images/rk3588-axon/axon-power-option.webp
   :width: 45%
