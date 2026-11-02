##############
I2C
##############

.. variable

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

I2C is a multi-master, multi-slave, packet-switched, single-ended serial communication bus. It's widely used for communication between microcontrollers and low-speed peripherals like sensors, EEPROMs, and real-time clocks. I2C operates with two lines:

    - SCL (Serial Clock Line): Provides the clock for the communication.
    
    - SDA (Serial Data Line): Transfers the data.

Axon Mini provides a total of **6** I2C interfaces on the **40-pin GPIO Header**,
plus **2** LPI I2C (Low Power Island I2C) interfaces on the **30-pin GPIO FPC Connector**.

- **40-pin GPIO Header:** ``I2C0``, ``I2C8``, ``I2C9``, ``I2C10``, ``I2C12``, ``I2C14``
- **30-pin GPIO FPC Connector:** ``LPI_I2C0``, ``LPI_I2C1``

.. note::

    On Axon Mini (QCS6490), I2C buses on the **40-pin GPIO Header** are independent
    of the camera subsystem. CSI uses its own dedicated I2C interfaces, so enabling
    GPIO-header I2C does not conflict with CSI camera operation.

.. tip::
    For pinouts, see the :ref:`40-pin GPIO Header <40-pin-gpio-header>`
    and :ref:`30-pin GPIO FPC Connector <30-pin-gpio-fpc-connector>`.


Key features of I2C include:
----------------------------

- Addressable Devices: Each device connected to the I2C bus has a unique 7- or 10-bit address.

- Simplicity: Requires only two wires, which simplifies the layout.

- Data Speeds: Operates at standard modes (100 kbps), fast modes (400 kbps), and high-speed modes (up to 3.4 Mbps).

- Multi-master: Allows multiple masters to control the bus.


How to use GPIO Pins as I2C Protocol ?
----------------------------------------

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


5. Select overlays as per your requirement ``( I2C1 / I2C2 / I2C5 / I2C7 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

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
    │  [*] Enable I2C1 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C2 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C5 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable I2C7 on 30-Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable PWM0 on 30 Pin GPIO Header Axon V0.3                                         │
    │  [ ] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
    │  [ ] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
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


How to interact with the generated I2C's ?
-------------------------------------------

Now, you can see ``I2C`` devices, which are accessible through device nodes such as:

.. code-block::
      
   ls -l /dev/i2c-*


If you have turned on ``I2C1`` then you can get device like this ``/dev/i2c-1``.

These ``i2c-*`` device nodes allow users to communicate with I2C peripherals such as sensors, EEPROMs, and other slave devices connected to the I2C bus.

Simple set/get I2C values
-------------------------

To use the i2cset, i2cget, and i2cdetect commands, you need to install the i2c-tools package. These tools are part of the i2c-utils package, which provides user-space tools for interacting with I2C devices via the Linux I2C subsystem.

.. code-block::

    sudo apt install i2c-tools

1. **Identify I2C Buses and Devices:**

   - You can list available I2C buses using:

   .. code-block::
    
        sudo i2cdetect -l

   -  In ``i2c-*``, where * represents an ``I2C`` bus number. For example, ``i2c-1`` can communicate with multiple devices, each identified by a unique 7-bit or 10-bit address.

2. **Detect I2C Devices on a Bus:**

   - To scan a particular bus for connected I2C devices, use:

   .. code-block::

        sudo i2cdetect -y <bus_number>

   - ``<bus_number>``: The I2C bus number (like 1 from the previous command).

   - For example, to scan bus ``1``:

   .. code-block::

        sudo i2cdetect -y 1
   
   - The output shows a grid with device addresses. Devices are listed by their 7-bit addresses.

LPI (Low Power Island) I2C Interface usage
-------------------------------------------

The LPI (Low Power Island) is a dedicated low-power domain on the QCS6490 SoC,
separate from the main application processor (AP) power domain. It hosts a
sensor-core QUP interface that stays active independent of AP sleep states,
allowing continuous sensor data acquisition (IMU, pressure, magnetometer, etc.)
with minimal power draw. On QCS6490, this domain is owned and controlled by
the CDSP (Compute DSP), which also performs the sensor-hub role.

On Axon Mini **30-pin GPIO FPC Connector**, 2 LPI I2C interfaces are available:

- ``LPI_I2C0`` on GPIO Pin (161, 162)
- ``LPI_I2C1`` on GPIO Pin (163, 164): shared/muxed with LPI SPI and LPI UART on the same pins
