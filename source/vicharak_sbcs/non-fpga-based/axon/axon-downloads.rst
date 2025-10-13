.. _axon-downloads:

Axon Downloads
================

OS Images
---------

.. list-table::
    :widths: 25 100
    :header-rows: 1

    - - **Operating System**
      - **Variant**
    - - Android
      - `Android 12 <https://downloads.vicharak.in/vicharak-axon/android/>`_
    - - Debian
      - **Coming Soon**
    - - Ubuntu
      - `Jammy 22.04 <https://downloads.vicharak.in/vicharak-axon/ubuntu/22_jammy>`_
    - - Ubuntu
      - `Noble 24.04 <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble>`_
    - - Community Images
      - **Coming Soon**

.. note::

    The images are compressed using XZ. You can use `7zip <https://www.7-zip.org/>`_ or
    `WinRAR <https://www.win-rar.com/>`_ to extract the file.

    For **Linux**, you can use the following command to extract the image:

    .. code-block:: console

        xz -d <image_name>.xz



.. seealso::

    `How to flash the image to the board using Rockchip Tool </vicharak_sbcs/vaaman/vaaman-linux/linux-usage-guide/rockchip-develop-guide>`_


OS Utilities
------------
.. list-table::
    :widths: 25 100
    :header-rows: 1

    - - **Utility**
      - **Download Link**
    - - Rockchip Linux Upgrade Tool
      - `V2.1 <https://github.com/vicharak-in/Linux_Upgrade_Tool>`_
    - - Rockchip RkDevTool
      - `V3.19
        <https://github.com/vicharak-in/rockchip-tools/blob/master/windows/RKDevTool_Release_v3.19.zip>`_
    - - Rockchip Windows Drivers
      - `V5.12
        <https://github.com/vicharak-in/rockchip-tools/blob/master/windows/DriverAssitant_v5.12.zip>`_
    - - Balena Etcher
      - `V1.18.11 <https://github.com/balena-io/etcher/releases/tag/v1.18.11>`_

SoC Documents
-------------
.. TODO: Add datasheet and TRM documents
.. list-table::
    :widths: 25 100
    :header-rows: 1

    - - **File**
      - **Download Link**

    - - Rockchip SoC and BSP Documents
      - `GitHub <https://github.com/vicharak-in/rockchip-docs>`_

Axon Pin-outs Guide
---------------------
.. TODO: Add link for Axon 3D File

`Download Pinouts </_static/files/axon_V0.3_Pinout_Guide.pdf>`_

Mechanical Information
----------------------
.. TODO: Update weight
.. list-table::
    :widths: 25 100
    :header-rows: 1

    - - **Property**
      - **Value**
    - - Dimensions
      - 72mm x 100mm
    - - Weight
      - X grams
    - - Mounting holes
      - 4x M2.5 holes for easy installation

Step File
---------

**Axon Board 3D File**

`Download File </_static/files/AXON_3D_file_V0.3.step.7z>`_

**Axon 3D Printed Case Files**

- Axon Enclosure Installation Guide

.. note::

   The Axon enclosure combines a snap-fit design with screws for added stability, allowing secure and easy access to the board's components.

- Installation Steps

1. Insert the Board
    - Slide the board into the bottom part of the enclosure.

2. Fasten with Screws
    - Use self-tapping screws with the following specifications:
        - **Thread Diameter:** 2.7 mm
        - **Height:** 12 mm
    - Secure the screws gently to avoid overtightening, which can damage the board.

3. Snap-Fit the Top Cover
    - Slide and lock the top on the **right side**.
    - Push down on the **left side** until it snaps into place.

- Opening the Enclosure

1. Locate the area labeled **"PRESS & PULL"** on the lid.
2. Hold and press the lid at the labeled spot.
3. Pull up gently to release the snap-fit and open the enclosure.


`Download File </_static/files/Axon0p3_0p2_Case_121224.zip>`_

.. note::

    The step file is compressed using 7zip. You can use 7zip_ or WinRAR_ to extract the
    file.

    For **Linux**, you can use the following command to extract the image:

    .. code-block:: console

        7z x <image_name>.7z

|

.. TODO: Update the respective links
.. seealso::

    :ref:`Frequently Asked Questions <axon-faq>`
