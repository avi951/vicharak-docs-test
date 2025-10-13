
##############
UART
##############


.. variable

.. _Axon GPIO Header: https://docs.vicharak.in/vicharak_sbcs/axon/axon-gpio-description/#axon-gpios-header

.. warning::

    We recommend to use Vicharak 6.1 kernel and latest `Ubuntu 24.04 Noble Numbat
    <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble/>`_ , in order to support below overlays. Flash Image
    using this `Documentation </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon linux-headers-6.1.75-axon

Introduction
------------

Many embedded boards provide the flexibility to configure GPIO pins to function as UART interfaces, enabling communication between the board and peripheral devices such as sensors, displays, and computers.

This guide explains how to configure GPIO pins as UART on Axon 30 Pins GPIO Header. By converting GPIO pins into UART transmit (TX) and receive (RX) pins, the board can be used for serial communication, expanding the range of connected devices. This configuration is useful when there is no dedicated UART hardware interface available or when additional UART ports are needed.

Axon provides total **4** UARTs including one specific ``UART_2`` ( Pin 2 and Pin 4 ) for debugging on GPIO Header, Like
``UART_1``, ``UART_4``, ``UART_6``.

.. tip::
    To get more information on `Axon GPIO Header`_. 

How to use GPIO Pins as UART Protocol ?
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



5. Select overlays as per your requirement ``( UART1 / UART4 / UART6 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

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
    │  [*] Enable UART1 on 30 Pin GPIO Header Axon V0.3                                        │
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

How to check tty serial device ?
--------------------------------

1. Open terminal. ( ``Ctrl + Alt + t`` )
2. Run below command :

.. code::

    ls -l /dev/ttyS*

If you have turned on ``UART1`` then device ``/dev/ttyS1`` will be generated.

.. note::
    /dev/ttyS9 device is specific for bluetooth, you can find another devices.


Example
-----------

**UART 1 Configuration**

.. list-table::
   :widths: 20 40 130
   :header-rows: 1
   :class: feature-table

   * - **Serial (USB To UART Module) FTDI Pin**
     - **Header GPIO Pin**
     - **Schematic Name**
   * - GND
     - Pin 8
     - GND
   * - TX
     - Pin 10 (GPIO2_B6)
     - UART1_RX_M0
   * - RX
     - Pin 12 (GPIO2_B7)
     - UART1_TX_M0 
        

.. image:: /_static/images/rk3588-axon/axon-gpio-uart1.webp
    :width: 50%


Running the Serial Console Program
-------

.. tab-set::

    .. tab-item:: Linux GTK-TERM (GUI)

        1. Install GTK-Term 

        .. code-block::
            
            sudo apt update
            sudo apt install gtkterm

        2. Open the GTK-Term program and configure the serial parameters.

        .. code-block::
            
            sudo gtkterm

        - On the **Configuration** menu, click on **Port**.
        - Select the serial port number and configure the serial parameters as
          shown in the image below.

        .. image:: /_static/images/rk3588-axon/axon-gpio-uart-gtkterm.webp
            :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

        .. note::
            Set Port and Baudrate according to peripheral requirement. 

    .. tab-item:: Minicom ( CLI )

        1. Install Minicom 

        .. code-block::
            
            sudo apt update
            sudo apt install minicom

        2. Open Minicom

        .. code-block::
            
            sudo minicom -b <BaudRate> -D /dev/ttyS<UART_DEVICE_NUMBER>
        
        .. note::
            
            -b is for Baud Rate.

            -D is for UART tty device.
            
            To Close Minicom Type, ``Ctrl + A`` then ``z``, And Press ``q`` and Select ``Enter``.


    .. tab-item:: WINDOWS - PuTTY (GUI)
    
            1. Download and install the `PuTTY <https://www.putty.org/>`_ program.
    
            2. Open the PuTTY program and configure the serial parameters as shown in the image below.
    
            .. image:: /_static/images/Putty_step.webp
               :width: 50%
    
            3. Click on the **Open** button to open the serial console.
    
            4. You will now be able to access the serial console.
    
    
