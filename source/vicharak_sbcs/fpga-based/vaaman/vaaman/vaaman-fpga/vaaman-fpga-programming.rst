.. _vaaman-fpga:

#########################
 Vaaman FPGA Programming
#########################

.. tab-set::

    .. tab-item:: Uploading BIT files to FPGA

        To upload the BIT file to the FPGA, follow the steps mentioned
        below:

        1. Hardware Connections
        
           Locate the 10-pin headers on the Vaaman board. These can be found from
           the schematic.
        
           Ensure the Vaaman board is powered On.
        
           Connect the USB-to-JTAG Module to the Vaaman board.
        
           While connecting the Programmer module, make sure to follow the
           indicated color code as shown in the image.
        
        .. image:: /_static/images/rk3399-vaaman/FPGA_JTAG_PROG.webp
           :width: 50%
        
        2. Download the BIT file
        
           Download the DEMO BIT file from the `Simple LED Blink Bit Demo </_static/files/sample_led_blink_t120_demo_bit.zip>`_
        
           Unzip the downloaded file.
        
        3. Programming the Flash using Efinity
        
           Open Efinity 2021.2 or later.
        
           Inside the Efinity IDE
        
           -  Refresh USB Target as shown in the image.
           -  Select the Bitstream file to be programmed. (The bitstream file is
              available in the unzipped folder)
           -  Select the JTAG Programming mode.
           -  Start the programming process.
        
        .. image:: /_static/images/rk3399-vaaman/vaaman-efinity-programmer-jtag.webp
           :width: 50%
        
        Wait for the programming to complete. When the programming is complete,
        the FPGA will be configured with the bitstream.

    .. tab-item:: Configure fpga from linux command
        
        - Download the HEX file
        - Download the DEMO HEX file from `Simple LED Blink Hex Demo </_static/files/sample_led_blink_t120_demo_hex.zip>`_
        - Unzip the downloaded file.
       
        - To program the FPGA from the command line, enter the command:
        
        .. code-block:: bash
        
            sudo vaaman-ctl -i <path/to/sample_led_blink_t120_demo_hex.hex>

        - You can get the usage information of the vaaman-ctl tool by using the command:
        
        .. code-block:: bash

            sudo vaaman-ctl -h
            

Verify the FPGA configuration
=============================

Once the programming is complete, you will observe the orange LED on the
Vaaman board blinking.

This indicates that the FPGA is configured with the bitstream.

.. image:: /_static/images/rk3399-vaaman/vaaman-fpga-user-leds.webp
   :width: 50%

.. tip::

   Additionally, you will notice that the four green LEDs on the Vaaman
   board will be blinking in a sequence.
