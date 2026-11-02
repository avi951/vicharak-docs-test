##################
Type-C DP 1.4
##################

.. TODO: Add Axon Mini Type-C DP image
..
   .. image:: /_static/images/qcs6490-axon-mini/axon-mini-dp.webp
      :width: 80%

Axon Mini provides a Type-C DisplayPort 1.4 interface for high-resolution display output with high video bandwidth. The DP connector on QCS6490 is used for direct connections to DP-compatible displays, projectors, and USB-C docking stations.

Getting Started
---------------

Prerequisites
`````````````
- Type-C DisplayPort 1.4 compatible display, or monitor
- Axon Mini with DP connector
- USB-C cable to your display port(HDMI , VGA , others) in your display

How to use
-----------
1. Connect one end of your USB-C cable to Axon Mini board to the usb-ports shown in image
2. Connect the other end of your USB-C cable to your display
3. You should get the Vichrak configured displayed on your monitor

Configure DisplayPort and video mode
`````````````````````````````````````

1. Check if Display is detected
""""""""""""""""""""""""""""""""

Use **xrandr** to show all supported resolutions and refresh rates available on DP output:

.. code-block:: bash

   xrandr

Example output:

.. code-block:: text

   Screen 0: minimum 320 x 200, current 1280 x 1024, maximum 16384 x 16384
   HDMI-1 disconnected (normal left inverted right x axis y axis)
   HDMI-2 disconnected (normal left inverted right x axis y axis)
   DP-1 disconnected (normal left inverted right x axis y axis)
   DP-2 connected 1280x1024+0+0 (normal left inverted right x axis y axis) 376mm x 301mm
      1280x1024     60.02*+  75.02
      1152x864      75.00
      1024x768      75.03    60.00
      800x600       75.00    68.32
      640x480       75.00    59.94
      720x400       70.08

Key Information from Output
,,,,,,,,,,,,,,,,,,,,,,,,,,,

- Here, DP-2 is shown as connected, which shows that your display has successfully connected to Axon Mini
- Numbers on right = Available refresh rates in Hz
- ``connected`` = Display is detected and connected
- ``disconnected`` = Display not detected

2. Auto-enable Display (Recommended)
""""""""""""""""""""""""""""""""""""

Automatically enable the display with optimal settings:

.. code-block:: bash

   xrandr --output DP-2 --auto

3. Set Custom Resolution and Refresh Rate
"""""""""""""""""""""""""""""""""""""""""

.. note::

   Actual supported resolutions depend on the capabilities of the connected display and the configured DP lanes.

Manually configure display resolution and refresh rate:

.. code-block:: bash

   xrandr --output DP-2 --mode 1280x1024 --rate 60

Common xrandr Parameters
,,,,,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Description
   * - ``--output <name>``
     - Display output name (DP-1, DP-2, HDMI-1, etc.)
   * - ``--mode <resolution>``
     - Resolution in format WIDTHxHEIGHT (e.g., 1280x1024)
   * - ``--rate <frequency>``
     - Refresh rate in Hz (e.g., 60)
   * - ``--auto``
     - Auto-detect and apply optimal settings
   * - ``--off``
     - Disable the display
   * - ``--scale <factor>``
     - Scale output (e.g., 1.0 for normal, 2.0 for 2x zoom)

Troubleshooting
```````````````

- If **dmesg** reports inability to initialize DP, verify:

  - Type-C DP cable and connector integrity
  - Correct overlay name and that the overlay is loaded
  - Kernel supports DP output
  - External display is powered on and set to the correct input

- If the display remains dark, check that:

  - DP display is properly detected in ``xrandr``
  - A valid framebuffer is assigned (fb0, fb1, etc.)
  - Display resolution is supported by the connected monitor

- Review documentation for model-specific DP timing and initialization sequences

- Use ``xrandr`` to manually set display resolution and refresh rate:

  .. code-block:: bash

     xrandr --output DP-1 --mode 1920x1080 --rate 60
