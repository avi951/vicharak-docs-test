############
PERIPLEX SPI
############


This section explains how to interact with the ``SPI's`` chip generated on Vaaman via Periplex.

How to Generate SPI's on the Vaaman ?
=====================================

1. **Create the json file:**

   - To generate ``4-SPI's`` chip, Your need to create a json file and copy the following content into it.

   .. tip::
      - how to create the json configuration file for periplex, You can check this :doc:`Usage Guide <../usage>` 

   .. code-block:: json

         {
            "uart": [],
            "i2c": [],
            "gpio": [],
            "pwm": [],
            "ws": [],
            "spi": [
               {
                  "id": 0,
                  "SLAVE": 1,
                  "MISO-IN": "GPIOT_RXP28",
                  "MOSI-OUT": "GPIOL_73",
                  "SLAVE-0": "GPIOR_173",
                  "CLK-OUT": "GPIOR_174"
               },
               {
                   "id": 1,
                   "SLAVE": 1,
                   "MISO-IN": "GPIOT_RXN28",
                   "MOSI-OUT": "GPIOL_75",
                   "SLAVE-0": "GPIOL_72",
                   "CLK-OUT": "GPIOR_178"
               },
               {
                   "id": 2,
                   "SLAVE": 1,
                   "MISO-IN": "GPIOR_168",
                   "MOSI-OUT": "GPIOL_17",
                   "SLAVE-0": "GPIOL_20",
                   "CLK-OUT": "GPIOL_18"
               },
               {
                   "id": 3,
                   "SLAVE": 1,
                   "MISO-IN": "GPIOR_187",
                   "MOSI-OUT": "GPIOL_24",
                   "SLAVE-0": "GPIOL_66",
                   "CLK-OUT": "GPIOL_62"
               }
            ],
            "onewire": [],
            "can": [],
            "i2s": [],
            "i2cslave": []
         }

2. **Run the periplex-sync command:**

   - For example, if the JSON configuration for ``4-SPI's`` chip is stored into the ``device.json`` file, the ``periplex-sync`` command would look like this:

   .. code-block::

     sudo periplex-sync -p device.json

   - After successfully running of ``periplex-sync`` command, It will ask for editing the ``periplex-dtso`` file, press ``1`` for ``yes`` 
     and then press ``Enter`` to continue.
   - This will open the ``periplex-dtso`` file in your default text editor (usually ``vim`` or ``nano``), you need to add the following content into it for create the ``4-SPI's`` chip:

   .. code-block::

         //SPDX-License-Identifier: GPL-2.0+
         //Copyright (C) 2024 Vicharak Computers LLP

         /dts-v1/;
         /plugin/;

         #include "rk3399-vaaman-periplex.dtsi"

         &periplex{

         	periplex_spi4: periplex-spi4 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <3>;
         	        spidev@0 {
                                 compatible = "rockchip,spidev";
                                 status = "okay";
                                 reg = <0>;
                                 spi-max-frequency = <25000000>;
                         };
         	};
         	periplex_spi3: periplex-spi3 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <2>;
         		spidev@0 {
                                 compatible = "rockchip,spidev";
                                 status = "okay";
                                 reg = <0>;
                                 spi-max-frequency = <25000000>;
                         };
         	};
         	periplex_spi2: periplex-spi2 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <1>;
         		spidev@0 {
                                 compatible = "rockchip,spidev";
                                 status = "okay";
                                 reg = <0>;
                                 spi-max-frequency = <25000000>;
                         };
         	};
         	periplex_spi1: periplex-spi1 {
         		status = "okay";
         		compatible = "vicharak,periplex-spi";
         		periplex-id = <0>;
         		spidev@0 {
         		        compatible = "rockchip,spidev";
         		        status = "okay";
         		        reg = <0>;
         		        spi-max-frequency = <25000000>;
         		};
         	};

         };

   - Then save the file and exit the editor. for example, if you use ``vim`` editor, you can do this by pressing ``Esc``, then typing ``:wq`` and pressing ``Enter``.

   - After saving the file, the ``periplex-sync`` command will continue to run and apply the changes to the device tree,it will ask for the reboot. 

3. **Reboot the board:**

   - After rebooting, all configurations have been successfully applied.
   - You will get the ``4-SPI's`` chip generated through Periplex like this:

   .. raw:: html

      <pre style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; width: 71%; height: 67px; overflow: auto; white-space: pre-wrap;">
         vicharak@vicharak:~$ ls /dev/spidev*
         /dev/spidev0.0  <span style="color:red;">/dev/spidev1.0</span>  <span style="color:red;">/dev/spidev2.0</span>  <span style="color:red;">/dev/spidev3.0</span>  <span style="color:red;">/dev/spidev4.0</span>
      </pre>

How to interact with the generated SPI's ?
===========================================

The Periplex platform dynamically exposes SPI controllers as ``spidev`` devices, which can be accessed via paths like:

.. code-block::

   /dev/spidev1.0
   /dev/spidev2.0
   /dev/spidev3.0
   ...

Configuring and Controlling SPI's chip
--------------------------------------

Each SPI chip manages a SPI bus. For example, you want control ``spidev1.0``.

1. **Opens SPI connection:**

   - Opens SPI connection on ``/dev/spidev1.0`` using the ``spidev`` Python library.

2. **Configures SPI settings:**

   - ``Speed``: 25 MHz

   - ``Mode``: 0

   - ``Bits per word``: 8

3. **Supports the following operations:**

   - Write data to the SPI device using ``writebytes()``.

   - Read data from the SPI device using ``readbytes()``.

   - Transfer data (send and receive simultaneously) using xfer2().

4. **Gracefully closes the SPI connection after operations:**

   - ``spi.close_connection()`` is used to safely close the SPI connection after all operations are completed.

- Follow this python script to control the SPI chip:

.. code-block:: python

   #!/usr/bin/env python3
   import spidev
   import sys

   class SimpleSPI:
       def __init__(self, bus=1, device=0):
           """Initialize SPI connection"""
           self.spi = spidev.SpiDev()
           self.bus = bus
           self.device = device

       def open_connection(self):
           """Open SPI connection and configure settings"""
           try:
               self.spi.open(self.bus, self.device)

               # Basic SPI configuration
               self.spi.max_speed_hz = 25000000  # 25MHz
               self.spi.mode = 0  # SPI Mode 0
               self.spi.bits_per_word = 8

               print(f"SPI connection opened: /dev/spidev{self.bus}.{self.device}")
               print(f"Speed: {self.spi.max_speed_hz} Hz, Mode: {self.spi.mode}")
               return True

           except Exception as e:
               print(f"Error opening SPI: {e}")
               return False

       def close_connection(self):
           """Close SPI connection"""
           if self.spi:
               self.spi.close()
               print("SPI connection closed")

       def write_data(self, data):
           """Write data to SPI device"""
           try:
               if isinstance(data, int):
                   data = [data]

               print(f"Writing: {[hex(x) for x in data]}")
               self.spi.writebytes(data)
               return True

           except Exception as e:
               print(f"Write error: {e}")
               return False

       def read_data(self, length):
           """Read data from SPI device"""
           try:
               data = self.spi.readbytes(length)
               print(f"Read: {[hex(x) for x in data]}")
               return data

           except Exception as e:
               print(f"Read error: {e}")
               return None

       def transfer_data(self, tx_data):
           """Transfer data (simultaneous read/write)"""
           try:
               if isinstance(tx_data, int):
                   tx_data = [tx_data]

               # Store original data before xfer2 call
               tx_original = tx_data.copy()

               rx_data = self.spi.xfer2(tx_data)
               print(f"TX: {[hex(x) for x in tx_original]} → RX: {[hex(x) for x in rx_data]}")
               return rx_data

           except Exception as e:
               print(f"Transfer error: {e}")
               return None

   def main():
       """Main function demonstrating basic SPI operations"""
       print("Simple SPI Communication")
       print("=" * 30)

       # Create SPI instance
       spi = SimpleSPI(bus=1, device=0)  # /dev/spidev1.0

       # Open connection
       if not spi.open_connection():
           sys.exit(1)

       try:
           # Basic operations
           print("\n--- Write Operation ---")
           spi.write_data([0x01, 0x02, 0x03])

           print("\n--- Read Operation ---")
           spi.read_data(3)

           print("\n--- Transfer Operation ---")
           spi.transfer_data([0xAA, 0xBB, 0xCC])

       except Exception as e:
           print(f"Error: {e}")

       finally:
           spi.close_connection()

   if __name__ == "__main__":
       main()