##############
Bluetooth
##############

The Axon Mini SBC includes an integrated Bluetooth 5.3 interface based on the
**AP6276S** module.
Bluetooth is used for connecting wireless peripherals such as keyboards,
mice, audio devices, and sensors.

Hardware Details
----------------

- **Module**: AMPAK AP6276S
- **Bluetooth Version**: Bluetooth 5.3 / BLE
- **Host Interface**: UART

Linux Support
-------------

Bluetooth is supported using the Linux **BlueZ** stack.
Firmware must be available under ``/lib/firmware/brcm/``.

The Bluetooth controller is typically exposed as ``hci0``.

Using Blueman (GUI Method)
--------------------------

1. Launch Blueman Manager:

   .. code-block:: bash

      blueman-manager

2. Ensure Bluetooth is **ON** (top toolbar).

3. Click **Search** to scan for nearby Bluetooth devices.

4. Select the target device from the list and click **Pair**.

5. Confirm the pairing request on both devices if prompted.

6. After pairing, right-click the device and select **Connect**.

Blueman provides an easy graphical interface for managing Bluetooth devices.

Using bluetoothctl (CLI Method)
-------------------------------

Start Bluetooth control utility:

.. code-block:: bash

   bluetoothctl

Inside the prompt, run:

.. code-block:: bash

   power on

.. code-block:: bash

   scan on

Once the device appears (example MAC address):

Pair device using MAC address:

.. code-block:: bash

   pair AA:BB:CC:DD:EE:FF

Trust device using MAC address:

.. code-block:: bash

   trust AA:BB:CC:DD:EE:FF

Connect device using MAC address:

.. code-block:: bash

   connect AA:BB:CC:DD:EE:FF

Stop scanning and exit:

.. code-block:: bash

   scan off

.. code-block:: bash

   quit

Troubleshooting
---------------

- Check hci device using below command :

.. code-block::

      hciconfig -a

**Expected Device**

.. code-block::

      hci0:	Type: Primary  Bus: UART
      	BD Address: XX:XX:XX:XX:XX:XX  ACL MTU: 1021:8  SCO MTU: 64:1
      	UP RUNNING
      	RX bytes:2823 acl:0 sco:0 events:79 errors:0
      	TX bytes:7087 acl:0 sco:0 commands:98 errors:0
      	Features: 0xbf 0xfe 0xcf 0xfe 0xdb 0xff 0x7b 0x87
      	Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3
      	Link policy: RSWITCH HOLD SNIFF
      	Link mode: PERIPHERAL ACCEPT
      	Name: 'axon-mini'
      	Class: 0x7c0000
      	Service Classes: Rendering, Capturing, Object Transfer, Audio, Telephony
      	Device Class: Miscellaneous,
      	HCI Version: 5.3 (0xc)  Revision: 0x0000
      	LMP Version: 5.3 (0xc)  Subversion: 0x0000
      	Manufacturer: Broadcom Corporation (15)

- Check kernel logs if Bluetooth does not appear:

  .. code-block:: bash

     dmesg | grep -i bluetooth

- Verify firmware files:

  .. code-block:: bash

     ls /lib/firmware/

- You can reinstall firmware by using below command :

.. code-block::

      sudo apt update
      sudo apt install vicharak-firmware

- Reboot after installing firmware or drivers.

Notes
-----

- BLE support depends on kernel and BlueZ version.
