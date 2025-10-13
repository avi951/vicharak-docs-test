############
PERIPLEX CAN
############

.. variable
.. _Connection Reference: https://youtu.be/ZH_CCs12ptg?si=oH_NP-bzYvP39H-k

This section explains how to interact with the CAN network interface nodes generated on Vaaman through Periplex.

How to Generate CAN's on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``5 CAN's``, Your need to create a json file and copy the following content into it. 

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2c": [],
            "gpio": [],
            "pwm": [],
            "ws": [],
            "spi": [],
            "onewire": [],
            "can": [
               {
                  "id": 0,
                  "CAN_TX": "GPIOT_RXP28",
                  "CAN_RX": "GPIOT_RXN28"
               },
               {
                  "id": 1,
                  "CAN_TX": "GPIOL_73",
                  "CAN_RX": "GPIOL_75"
               },
               {
                  "id": 2,
                  "CAN_TX": "GPIOR_173",
                  "CAN_RX": "GPIOL_72"
               },
               {
                  "id": 3,
                  "CAN_TX": "GPIOR_174",
                  "CAN_RX": "GPIOR_178"
               },
               {
                  "id": 4,
                  "CAN_TX": "GPIOT_RXN27",
                  "CAN_RX": "GPIOR_183"
               }
            ],
            "i2s": [],
            "i2cslave": []
         }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``5 CAN's`` is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the 5 CAN's network interface node generated through Periplex like this:

   .. raw:: html

      <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 81%; height: 67px; overflow: auto; white-space: pre-wrap;">
         vicharak@vicharak:/sys/class/net$ ls
         <span style="color:red;">can0</span>  <span style="color:red;">can1</span>  <span style="color:red;">can2</span>  <span style="color:red;">can3</span>  <span style="color:red;">can4</span>  dummy0  eth0  lo  wlan0
      </pre>

How to interact with the generated CAN's ?
==========================================

The Periplex platform dynamically generates ``CAN`` interfaces, which are accessible through device nodes such as:

.. code-block::

   /sys/class/net/can0
   /sys/class/net/can1
   /sys/class/net/can2
   ...


These ``can*`` network interface nodes allow users to communicate with devices on the CAN bus, such as automotive ECUs, industrial controllers, and other CAN-enabled modules, using the SocketCAN framework

Simple send/receive CAN frames
------------------------------

To use ``cansend``, ``candump``, and other CAN utilities, you need to install the can-utils package.
These tools provide user-space utilities for interacting with CAN interfaces via the Linux SocketCAN subsystem.

.. code-block::
   
   sudo apt install can-utils

1. **Identify CAN Interfaces:**

   - You can list available CAN interfaces using:

   .. code-block::

      ip link show

2. **Bring Up a CAN Interface:**

   - To bring up a CAN interface, use the following command:
   .. code-block::

      sudo ip link set <interface> type can bitrate <bitrate_value>

   - Example:
      - to bring up ``can0`` with a bitrate of ``500 kbps``, you would run:

      .. code-block::

         sudo ip link set can0 up type can bitrate 500000

      - ``can0`` is the name of the CAN interface, 
      - ``500000`` is the bitrate in bits per second.

3. **Sending CAN Frames:**
 
   - To send a CAN frame, use the cansend command:
   
   .. code-block::

      sudo cansend <interface> <arbitration_id>#<data_bytes>

   - ``<interface>``: The CAN interface name (like can0).

   - ``<arbitration_id>``: The CAN identifier (11-bit or 29-bit).
      - Standard Frame: 11-bit ID (range: ``0x000`` – ``0x7FF``).
      - Extended Frame: 29-bit ID (range: ``0x00000000`` – ``0x1FFFFFFF``).

   - ``<data_bytes>``: Up to 8 data bytes in hexadecimal format, concatenated without spaces.

   - Example:
      - Send a standard frame with ID ``0x7E8`` and 7 bytes of data:

      .. code-block::

         sudo cansend can0 7E8#11223344556677

      - Send an extended frame with ID ``0x18DAF110`` and 8 bytes of data:

      .. code-block::

         sudo cansend can0 18DAF110#1122334455667788

4. **Receiving CAN Frames:**

   - To receive CAN frames, use the candump command:

   .. code-block::

      sudo candump <interface>

   - Example: 
      - Listen on ``can0``:
      .. code-block::
      
         sudo candump can0

      - To filter by a specific ID, use:

      .. code-block::
      
         sudo candump can0,7E8:7FF

      - ``7E8:7FF`` means show only messages with ID ``0x7E8``.

Example of using the CAN protocol
---------------------------------

This example demonstrates sending and receiving CAN frames using the CAN protocol with an ``HW-021`` CAN transceiver module connected between an ``ESP32-S3`` microcontroller and the ``Vaaman SBC``.

- **Transmitting over the CAN bus** from the ``ESP32-S3`` sends a data frame through the ``HW-021`` transceiver to the ``Vaaman SBC``. The frame contains an arbitration ID (which determines message priority) and up to 8 data bytes (the payload).

- **Receiving from the CAN bus** on the ``Vaaman SBC`` (via the candump command) captures frames sent by the ``ESP32-S3``, allowing the SBC to process control commands, sensor readings, or status updates.

- In reverse, the ``Vaaman SBC`` can also send CAN frames (using cansend) back to the ``ESP32-S3`` through the same ``HW-021`` link, enabling two-way communication.

In this setup, the ``HW-021`` acts as a physical layer transceiver, converting the ``vaaman SBC’s`` and ``ESP32’s`` CAN controller signals into the differential signals required on the CAN bus, ensuring reliable long-distance and noise-immune communication.

.. tip::
   - For guidance on physically wiring two ``HW-021`` CAN transceiver modules, refer to the following YouTube video: `Connection Reference`_.

   - In the video, the presenter demonstrates CAN communication between two ``ESP32`` boards using ``HW-021`` transceivers.

   - For your setup, the same physical wiring concept applies — simply replace one of the ``ESP32`` boards with the ``Vaaman SBC``. The connection between the two ``HW-021`` modules (CANH to CANH, CANL to CANL) remains identical.