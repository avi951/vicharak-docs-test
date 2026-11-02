.. _axon-mini-getting-started:

Getting Started
###############

For Axon Mini, Vicharak has provided all the necessary accessories and
information to get started with the board. This section will guide you through
the initial setup process and provide you with the necessary information to get
started with Axon Mini.

What's in the box?
==================

1. **Axon Mini**
    - Single-board computer optimized for high-performance computing and AI.
    - Powered by Qualcomm Dragonwing QCS6490 SoC (octa-core Qualcomm® Kryo™ 670 CPU).
    - 8GB/16GB LPDDR5 RAM, 32GB eMMC storage, 40-Pin GPIO header.
    - Pre-installed with Debian 13 (Trixie).

What else do you need?
======================

**1. Compatible Power Source** (see :ref:`axon-mini-power-sources`)

**2. HDMI or Type-C DP cable to drive Display Monitor**
 
**3. USB2.0 Keyboard and Mouse**
 
**4. Monitor with HDMI/Type-C DP input**

**5. USB-C to USB-A Male cable (optional)**

**6. 30-Pin GPIO FPC (optional)**

**7. Internet Connection (optional)**

**8. USB to TTL Serial Cable (optional)**

.. note::
    | The items listed above are not included in the box.
    | You can purchase them from the :ref:`axon-mini-accessories` page.

Axon Mini OS Images
===================

    :ref:`axon-mini-downloads`

Axon Mini OS Credentials
========================

.. note::
    Username : vicharak
    
    Password : 12345

- To Go to into ``root`` user, Type ``su`` terminal and Default Password is ``root``.

Axon Mini Button Guide
======================

.. TODO: Add Axon Mini keys/button guide image
..
   .. image::  ../../_static/images/qcs6490-axon-mini/axon-mini-keys-guide.webp
       :width: 70%


1. Power Button
    You can turn on Axon Mini with the power button if it is currently off. When the board is powered off the red LED will on to
    let you know that the board has proper power supply. If you press the power button ( for 1-2 seconds ) then the board will start booting
    up.

2. Reset Button
    You can reboot Axon Mini by pressing reset button.

3. EDL Button
    EDL button is used to put Axon Mini into Emergency Download (EDL) Mode for firmware flashing and recovery.

.. note::
    | *To get Axon Mini into EDL Mode*, hold the EDL button while powering on / connecting power to the board, then release the EDL button.
    | The board will enter Emergency Download Mode (also known as Qualcomm 9008 / QDL mode).

Getting Started with eMMC
=========================

Turning board on
----------------

Axon Mini comes pre-loaded with **Debian** (``Trixie``) operating system on
its ``eMMC`` (embedded MultiMediaCard) storage, and it also offers support for
``UFS`` boot mode.

If users wish to explore different operating systems, they must utilize the
appropriate firmware to program the board accordingly.

For the purpose of this guide, we will focus on the ``eMMC`` storage and the
pre-installed ``Debian (Trixie)``. For UFS boot, see the Available Boot Modes
section below.

Connect a compatible power adapter to the Axon Mini board. Once the power is connected, the board will automatically turn on.

Power the board with a 12V adapter on the dedicated Type-C PD port. See :ref:`axon-mini-power-sources` for the power rating.

.. TODO: Add Axon Mini power details image
..
   .. image:: ../../_static/images/qcs6490-axon-mini/axon-mini-power-details.webp
      :width: 60%

Axon Mini is pre-installed with Debian (``Trixie``) on its eMMC storage.
So, when you power on the board, it will boot from the eMMC storage by default.

Verify the power LED
--------------------

Upon connecting the power cable, the activation of the **Red LED** serves as an
immediate visual indicator of the board's power status. This LED signifies that
the Axon Mini is receiving power, and its illumination provides users with a
tangible confirmation of the successful power connection.

.. TODO: Add Axon Mini power LED image
..
   .. image:: ../../_static/images/qcs6490-axon-mini/axon-mini-power-led.webp
       :width: 50%

Verify the status LED
---------------------

The activation of the **status LED**, marked by a blinking pattern, signifies
the completion of the booting process. This visual cue assures users that the
Axon Mini has successfully booted from its storage medium and is ready for further
configuration.

.. TODO: Add Axon Mini status LED image
..
   .. image:: ../../_static/images/qcs6490-axon-mini/axon-mini-leds.webp
       :width: 50%

.. warning::
   |
   | Please ensure you wait for the system to complete its reboot.
   | This is necessary because the system requires configuration adjustments
   | before you proceed to the next step. Taking the time to allow the system to
   | finish restarting ensures that it is fully set up for the subsequent tasks.

Available Boot Modes
====================

Booting from eMMC
-----------------

Axon Mini boots from ``eMMC`` by default with the pre-installed Debian (``Trixie``) image.
Follow the **Getting Started with eMMC** section above.

Booting from UFS
----------------

.. TODO: Add Axon Mini UFS boot guide

To boot from UFS, please follow the guide below.

    .. TODO: Link Axon Mini UFS boot document here

How to access your Axon Mini board ?
====================================

There are multiple ways to access your Axon Mini. You can connect the Axon Mini
SBC to a monitor using the **HDMI port**, or you can connect it to your
computer headless using **SSH** or **serial console**.

For the initial setup process, we recommend connecting the Axon Mini to a
monitor using the **HDMI port**. Once the initial setup is complete, you can
connect the Axon Mini to your computer using the USB-C port.

.. note::
    If you want to access the **serial console**,
    Skip to the :ref:`Serial Console <axon-mini-serial-console>` section.

    If you want to access the **Axon Mini using SSH**,
    Skip to the :ref:`SSH <axon-mini-ssh>` section.

1. Using HDMI port
------------------

Axon Mini is equipped with an **HDMI port**, which allows for easy
connection to a display. By using an HDMI cable, users
can connect Axon Mini to a monitor or TV with an HDMI input.

This enables direct visual access to the graphical user interface (GUI) or
command-line interface (CLI) on the connected display.

.. TODO: Add Axon Mini HDMI image
..
   .. image:: ../../_static/images/qcs6490-axon-mini/axon-mini-hdmi.webp
       :width: 50%

Connect the HDMI cable to the Axon Mini and the monitor.
Once the cable is connected, the Axon Mini will automatically detect the
monitor and display the output.

.. note::
   If the display is not detected or you see no output after connecting HDMI,
   see the :doc:`HDMI TX documentation <display/display-interfaces>` for
   connection steps, verification commands, and troubleshooting.

.. admonition:: Check out Linux Start Guide
   :class: tip

   Once the Axon Mini is connected to the monitor, you can follow the
   :ref:`Linux Start Guide <axon-mini-linux-start-guide>` to complete the initial setup.

.. _axon-mini-serial-console:

2. Using Serial Console
-----------------------

Axon Mini also provides a serial interface, typically in the form of UART
(Universal Asynchronous Receiver-Transmitter) pins.

Users can access the system's console or terminal interface by connecting to
these serial pins using a serial cable or adapter. This method is often used
for debugging, troubleshooting, or accessing the system when other interfaces
are not available.

Preparation
```````````

To access Axon Mini through the serial interface, you will need the following:

- A computer with a serial terminal application installed
  (such as PuTTY or minicom).
- A USB to UART serial cable or adapter (such as FTDI or PL2303).
- USB-C cable.
- 3 Pin Jumper Wire ( Tx, Rx and GND )

.. warning::

    When UART (FTDI/PL2303) is connected to Axon Mini, and Axon Mini is poweroff. It requires to disconnect it from Axon Mini, in order to turn on Axon Mini Again.

Hardware Setup
``````````````

1. Connect the USB to UART serial cable or adapter to your computer.

2. Connect the serial cable or adapter to Axon Mini.

.. list-table::
   :widths: 20 40 130
   :header-rows: 1
   :class: feature-table

   * - **Serial FTDI Pin**
     - **Header GPIO Pin**
     - **Schematic Name**
   * - GND
     - Pin 6
     - GND
   * - RX
     - Pin 8
     - UART12_TX
   * - TX
     - Pin 10
     - UART12_RX

.. TODO: Add Axon Mini serial UART pins image
..
   .. image:: ../../_static/images/qcs6490-axon-mini/axon-mini-serial-uart-pins.webp
      :width: 50%

.. note::
    When accessing Axon Mini through the serial interface, it is important to
    configure the serial parameters correctly. For QCS6490-based systems,
    the following parameters are typically used:

    | Baud rate: `115200`
    | Data bit: `8`
    | Stop bit: `1`
    | Parity check: `none`
    | Flow control: `none`

.. warning::
   |
   | During the first boot you will see a warning on your serial console.
   | So, please ensure that you wait for the system to complete its reboot.
   | This is necessary because the system requires configuration adjustments
   | before you proceed to the next step. Taking the time to allow the system to
   | finish restarting ensures that it is fully set up for the subsequent tasks.

Running the Serial Console Program
``````````````````````````````````

.. tab-set::

    .. tab-item:: PuTTY (GUI)

        1. Download and install the `PuTTY <https://www.putty.org/>`_ program.

        2. Open the PuTTY program and configure the serial parameters as shown
           in the image below.

        .. image:: /_static/images/qcs6490-axon-mini/axon-mini-Putty_step.webp
           :width: 50%

        3. Click on the **Open** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: TeraTerm (GUI)

        1. Download and install the
           `TeraTerm <https://osdn.net/projects/ttssh2/releases/>`_ program.

        2. Open the TeraTerm program and configure the serial parameters.

        - On the **Setup** menu, click on **Serial port**.
        - Select the serial port number and configure the serial parameters
          as shown in the image below.

        .. image:: /_static/images/qcs6490-axon-mini/axon-mini-teraterm-configuration.webp
           :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: Linux GTK-Term (GUI)

        1. Install the GTK-Term program using the following command:

        .. code-block:: bash

            sudo apt-get install gtkterm

        2. Open the GTK-Term program and configure the serial parameters.

        - On the **File** menu, click on **Port**.
        - Select the serial port number and configure the serial parameters as
          shown in the image below.

        .. image:: /_static/images/qcs6490-axon-mini/gtkterm-configuration.webp
           :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: Minicom (CLI)

        .. note::
            Read minicom configuration from
            :ref:`Linux Minicom guide <axon-mini-minicom-guide>`.

.. _axon-mini-ssh:

3. Using SSH
------------

.. include:: ../common/common-ssh.rst

Axon Mini Boot modes
====================

.. list-table::
   :widths: 20 40
   :header-rows: 1

   * - **Boot Mode**
     - **Description**
   * - Normal Mode
     - Normal boot mode is the default boot mode. In this mode, the board boots
       from the `eMMC` or `UFS` storage. Each partition loads in order and enters
       the system normally.
   * - Fastboot Mode
     - Fastboot mode is used for flashing and updating firmware partitions over USB.
       In this mode, the bootloader waits for host-side fastboot commands. After a
       successful update, the board can reboot into Normal Mode from `eMMC` or `UFS`.
   * - EDL Mode
     - | EDL (Emergency Download) mode is used to `repair` or reflash the board.
         If the bootloader is damaged or the board fails to boot, Axon Mini can enter
         EDL mode (also known as Qualcomm 9008 / QDL mode).
         In this mode, the ROM code waits for the host to transmit the
         flash programmer / firmware through the USB-C port using Qualcomm flash tools
         (for example QDL).

.. seealso::

    :ref:`axon-mini-downloads`
