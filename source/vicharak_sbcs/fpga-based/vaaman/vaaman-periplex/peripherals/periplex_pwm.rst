############
PERIPLEX PWM
############


This section explains how to interact with the ``PWM's`` chip generated on Vaaman via Periplex.

How to Generate PWM's on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``5-PWM's`` chip, Your need to create a json file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2c": [],
            "gpio": [],
            "pwm": [
               {
                  "id": 0,
                  "PWM": "GPIOT_RXP28"
               },
               {
                  "id": 1,
                  "PWM": "GPIOL_73"
               },
               {
                  "id": 2,
                  "PWM": "GPIOR_173"
               },
               {
                  "id": 3,
                  "PWM": "GPIOR_174"
               },
               {
                  "id": 4,
                  "PWM": "GPIOT_RXN27"
               }
            ],
            "ws": [],
            "spi": [],
            "onewire": [],
            "can": [],
            "i2s": [],
            "i2cslave": []
         }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``5-PWM's`` chip is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``5-PWM's`` chip generated through Periplex like this:

   .. raw:: html

      <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 81%; height: 67px; overflow: auto; white-space: pre-wrap;">
         vicharak@vicharak:/sys/class/pwm$ ls
         pwmchip0  <span style="color:red;">pwmchip1</span>  <span style="color:red;">pwmchip2</span>  <span style="color:red;">pwmchip3</span>  <span style="color:red;">pwmchip4</span>  <span style="color:red;">pwmchip5</span>
      </pre>

How to interact with the generated PWM's ?
===========================================

The Periplex platform dynamically exposes PWM controllers as ``pwmchip`` devices, which can be accessed via paths like:

.. code-block::

   /sys/class/pwm/pwmchip1
   /sys/class/pwm/pwmchip2
   /sys/class/pwm/pwmchip3
   ...

Configuring and Controlling PWM's chip
--------------------------------------

Each PWM chip manages a PWM channel. For example, you want control ``pwmchip1``.

1. **Export a PWM channel:**

   - For export a PWM channel of pwmchip1:

   .. code-block::
      
      # Export the PWM channel
      echo 0 > /sys/class/pwm/pwmchip1/export
      
2. **Enable a PWM channel and set duty_cycle and period:**

   - For enable and set the duty_cycle and period of pwmchip1: 

   .. code-block::

      # Set the period (in nanoseconds)
      echo 2000000 > /sys/class/pwm/pwmchip1/pwm0/period
      
      # Set the duty cycle (in nanoseconds)
      echo 1500000 > /sys/class/pwm/pwmchip1/pwm0/duty_cycle
      
      # Enable the PWM signal
      echo 1 > /sys/class/pwm/pwmchip1/pwm0/enable

   - ``Period`` defines the total time for one cycle of the PWM signal.
   - ``Duty_cycle`` cycle specifies how long the signal stays high during one period.
   - ``Enable`` starts the PWM output. 


3. **Disable a PWM channel:**

   - To stop the PWM output:

   .. code-block::
      
      echo 0 > /sys/class/pwm/pwmchip1/pwm0/enable

4. **Unexport the PWM channel:**

   - When you’re done using the PWM channel, it's a good practice to unexport it:

   .. code-block::
      
      echo 0 > /sys/class/pwm/pwmchip1/unexport

.. note::

   - The **duty cycle** value must always be less than or equal to the **period** to ensure proper PWM operation.

   - Ensure you have the correct permissions to access PWMs. You may need to run these commands with sudo.

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