
##############
PWM
##############


.. _Axon GPIO Header: https://docs.vicharak.in/vicharak_sbcs/axon/axon-gpio-description/#axon-gpios-header

.. warning::

    We recommend to use Vicharak 6.1 kernel and latest `Ubuntu 24.04 Noble Numbat
    <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble/>`_ , in order to support below overlays. Flash Image
    using this `Documentation </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon linux-headers-6.1.75-axon

Introduction
-----------

PWM stands for Pulse Width Modulation, a technique used to control the amount of power delivered to a device. PWM generates a digital signal that switches between high (on) and low (off) at a consistent frequency. The key characteristic of PWM is the "duty cycle," which represents the percentage of time the signal remains high in one cycle.

- Axon has total **2** PWMs like, ``PWM0`` and ``PWM1``

.. warning::

    PWM1 can be configured on 2 pins GPIO0_C0 and GPIO1_D3 but with different Mux 0 and 1 accordingly. You can only use
    any one at once.


.. tip::
    To get more information on `Axon GPIO Header`_. 

Understanding Duty Cycle in PWM
-----------

A 50% duty cycle means the signal is high for half the time and low for the other half.

A 100% duty cycle means the signal is always high.

A 0% duty cycle means the signal is always low.

Why Use PWM with GPIO?
---------------------

When a GPIO pin is configured for PWM, it allows you to generate a varying voltage or power level from a simple digital output. This configuration is useful for:

- Controlling motors: PWM signals control motor speed by adjusting the duty cycle, which in turn regulates the average power delivered to the motor.

- Dimming LEDs: Instead of using resistors or analog circuits, you can dim LEDs by controlling the duty cycle of the PWM signal.

- Generating analog signals: Though PWM is a digital signal, when combined with filtering, it can approximate an analog voltage for use in certain types of analog circuits.


How to use GPIO Pins as PWM Protocol ?
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



5. Select overlays as per your requirement ``( PWM0 / PWM1_M0 / PWM1_M1 )`` by pressing ``spacebar`` on keyboard, then select ``Ok``.

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
    │  [ ] Enable UART1 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable UART6 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable UART6 on 30 Pin GPIO Header Axon V0.3                                        │
    │  [ ] Enable PWM0 on 30 Pin GPIO Header Axon V0.3                                         │
    │  [*] Enable PWM1_M0 on 30 Pin GPIO Header Axon V0.3                                      │
    │  [ ] Enable PWM1_M1 on 30 Pin GPIO Header Axon V0.3                                      │
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


Configuring and Controlling PWM's chip
--------------------------------------

Befor you dive into below steps, make sure you are in root user.

.. code-block::

    sudo su


Each PWM chip manages a PWM channel. For example, you want control ``pwmchip0``.

1. **Export a PWM channel:**

   - For export a PWM channel of pwmchip0:

   .. code-block::
      
      echo 0 > /sys/class/pwm/pwmchip0/export
      
2. **Enable a PWM channel and set duty_cycle and period:**

   - Set the period (in nanoseconds)

   - ``Period`` defines the total time for one cycle of the PWM signal.
   
   .. code-block::

      echo 2000000 > /sys/class/pwm/pwmchip0/pwm0/period
      
   - Set the duty cycle (in nanoseconds)
   - ``Duty_cycle`` cycle specifies how long the signal stays high during one period.
   
   .. code-block::

      echo 1500000 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
      
   - Enable the PWM signal
   - ``Enable`` starts the PWM output. 
   
   .. code-block::

      echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable



3. **Disable a PWM channel:**

   - To stop the PWM output:

   .. code-block::
      
      echo 0 > /sys/class/pwm/pwmchip0/pwm0/enable

4. **Unexport the PWM channel:**

   - When you’re done using the PWM channel, it's a good practice to unexport it:

   .. code-block::
      
      echo 0 > /sys/class/pwm/pwmchip0/unexport

Example of using the PWM protocol
----------------------------------

This example demonstrates controlling a **3200 RPM DC motor** using the PWM (Pulse Width Modulation) protocol.

- **Setting a higher duty cycle** increases the motor's speed.
- **Setting a lower duty cycle** decreases the motor's speed.

The motor's rotation speed depends on the duty cycle — running faster with a higher value and slower with a lower value.

1. **Export a PWM Channel**: Prepares the PWM channel for motor control.

2. **Enable and Configure PWM**: Sets the period (cycle duration) and duty cycle (signal high time) to control motor speed, then starts the motor.

3. **Disable PWM**: Stops the motor by halting the output signal.

4. **Unexport PWM Channel**: Releases the PWM channel, resetting it for future use.
