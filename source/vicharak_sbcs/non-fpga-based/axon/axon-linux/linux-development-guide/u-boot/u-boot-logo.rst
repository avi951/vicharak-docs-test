Change U-boot Logo
===================

In ``boot`` partition of the File system, includes ``logo.bmp`` file which appears on screen while booting Vicharak board.

Run ``lsblk`` command to show boot partition.

.. code-block:: bash

     mmcblk0      179:0    0  29.1G  0 disk
    ├─mmcblk0p1  179:1    0     4M  0 part
    ├─mmcblk0p2  179:2    0     4M  0 part
    ├─mmcblk0p3  179:3    0   512M  0 part /boot
    ├─mmcblk0p4  179:4    0   288M  0 part
    ├─mmcblk0p5  179:5    0   256M  0 part /userdata
    └─mmcblk0p6  179:6    0  28.1G  0 part /

User can change u-boot logo to replace ``logo.bmp`` file with their file.

.. warning::

   Make sure, you have to convert any logo file into ``.bmp`` format in order to apply.
