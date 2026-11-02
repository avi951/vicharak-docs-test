##############
SPI
##############

.. warning::

    We recommend to use Linux Kernel 7.1.0-rc4-mini+ and the latest Debian 13
    (Trixie) image from :ref:`axon-mini-downloads`, in order to support below
    overlays. Flash the image using this
    :doc:`QDL Flash Tool Guide <../axon-mini-linux/linux-usage-guide/qdl-tool-guide>`

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-7.1.0-rc4-mini+ linux-headers-7.1.0-rc4-mini+

Introduction
------------

SPI (Serial Peripheral Interface) is a widely used protocol for communication between microcontrollers and peripheral
devices like sensors, displays, and memory devices. Typically, SPI involves dedicated pins such as MOSI (Master Out
Slave In), MISO (Master In Slave Out), SCLK (Serial Clock), and SS (Slave Select).
In Axon Mini, general-purpose I/O (GPIO) pins can be repurposed to function as SPI pins.

Axon Mini provides a total of **4** SPI interfaces on the **40-pin GPIO Header**,
plus **1** LPI SPI (Low Power Island SPI) interface on the **30-pin GPIO FPC Connector**.

- **40-pin GPIO Header:** ``SPI8``, ``SPI9``, ``SPI12``, ``SPI14``
- **30-pin GPIO FPC Connector:** ``LPI_SPI``

.. tip::
    For pinouts, see the :ref:`40-pin GPIO Header <40-pin-gpio-header>`
    and :ref:`30-pin GPIO FPC Connector <30-pin-gpio-fpc-connector>`.


Make Simple spidev1.0 device
----------------------------

How to use GPIO Pins as SPI Protocol ?
======================================

**Steps to follow for Configuration**

1. Open a terminal window (``Ctrl+Alt+T``).

2. Run command ``sudo vicharak-config`` in it.

3. Select ``Overlays`` options in it by pressing ``enter`` key.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────-───────────┐
    │ Please select an option below:                                                           │
    │                                                                                          │
    │                                   System Maintanince                                     │
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


4. You will see Warning Page, click on ``yes`` and select ``Manage Overlays`` options.


.. code-block:: console


    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Configure Device Tree Overlay                                                            │
    │                                                                                          │
    │                                Manage overlays                                           │
    │                                View overlay info                                         │
    │                                Install 3rd party overlay                                 │
    │                                Reset overlays                                            │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘



5. Select overlays ``( SPI1 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

.. code-block:: console

    ┌──────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
    │ Please select overlays:                                                                  │
    │                                                                                          │
    │  [ ] Enable DP connector-split mode Axon V0.3                                            │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI0 D0,1 dphy1 Axon V0.3                      │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI0 D2,3 dphy2 Axon V0.3                      │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI1 D0,1 dphy4 Axon V0.3                      │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on CSI1 D2,3 dphy5 Axon V0.3                      │
    │  [ ] Enable RasPi Camera V1.3 (OV5647) on dphy RX0 Axon V0.3                             │
    │  [ ] Enable RasPi camera V1.3 (OV5647) on dphy RX1 Axon V0.3                             │
    │  [ ] Enable I2C1 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C2 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C5 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C7 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable PWM0 on 30 Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
    │  [ ] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
    │  [*] Enable SPI1 on 30 Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable UART1 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable UART4 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable UART6 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable Waveshare 4inch DSI LCD DPHY TX0 Axon V0.3                                   │
    │  [ ] Enable Waveshare 4inch DSI LCD DPHY TX1 Axon V0.3                                   │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                     <Ok>                         <Cancel>                                │
    │                                                                                          │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.

Check generated Device
======================

1. Open terminal. ( ``Ctrl + Alt + t`` )
2. Run below command :

.. code::

        ls -l /dev/spidev*

You will find ``/dev/spidev1.0`` device is created in ``/dev`` directory.

LPI (Low Power Island) SPI Interface usage
---------------------------------------------

The LPI (Low Power Island) is a dedicated low-power domain on the QCS6490 SoC,
separate from the main application processor (AP) power domain. It is owned
by the CDSP (Compute DSP) on QCS6490 and provides a sensor-core SPI interface
that remains available for low-power/always-on peripherals without requiring
the main AP to be active.

On Axon Mini **30-pin GPIO FPC Connector**, 1 LPI SPI interface is available:

- ``LPI_SPI`` on GPIO Pin (163, 164, 165, 166): shared/muxed with LPI I2C1 and LPI UART on the same pins
