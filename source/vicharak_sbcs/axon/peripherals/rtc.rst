##############
RTC
##############

The Axon SBC includes a hardware Real-Time Clock (RTC) based on the **HYM8563** chip.
This RTC allows the system to keep accurate time even when the main power is turned off and preserves system time across reboots and power cycles.

.. image:: /_static/images/rk3588-axon/axon-rtc.webp
   :width: 74%

Specification
--------------

- Connector Type: JST
- Pins: 2
- Pitch: 1mm

Hardware Details
----------------

- RTC Chip: HYM8563

.. image:: /_static/images/rk3588-axon/axon-rtc-connector.webp
   :width: 34%


Reference/Buy RTC
------------------

User can buy `Raspberry Pi compatible RTC Battery CR2032 <https://thinkrobotics.com/products/rtc-battery-rpi5?variant=49314316943677>`_
with Rated Voltage 3V (Max Voltage 3.3V )


Linux Support
-------------

To verify detection:

.. code-block:: bash

   dmesg | grep 8563

Expected output:

::

   rtc-hym8563 ... registered as rtc0

Usage
-----

Check RTC time:

.. code-block:: bash

   sudo hwclock --show

Sync system time to RTC:

.. code-block:: bash

   sudo hwclock --systohc

Sync RTC time to system:

.. code-block:: bash

   sudo hwclock --hctosys

Notes
-----

- Interface: I2C0
- Typical I2C Address: 0x51
- RTC requires a backup battery to retain time when powered off
- Without a battery, time will reset after power loss
- Ensure I2C0 is enabled in the device tree for RTC functionality

Warnings
--------

- Ensure correct battery polarity before connecting
- Use a compatible RTC battery with the JST connector
- Do not exceed the recommended voltage rating
