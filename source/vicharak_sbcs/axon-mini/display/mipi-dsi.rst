##################
MIPI DSI
##################

Axon Mini provides a MIPI-DSI host controller on the Qualcomm **QCS6490**; a
display panel is driven by a DSI bridge/panel driver with appropriate timing,
format, and polarity settings. In standard configurations, **DSI0** on QCS6490
is used for direct or bridged DSI connections to Waveshare or compatible panels.

Getting Started
----------------

Prerequisites
``````````````

- MIPI DSI Display
- Configure Kernel and make overlays according to MIPI-DSI Display
- Vicharak PCB For DSI Display
- Vicharak Flex Cable 30 Pin 0.4mm Pitch Cable (Golden Color)
- Make sure, You have installed latest kernel, If not. Please run command below.

.. code-block::

   sudo apt update
   sudo apt reinstall linux-image-7.1.0-rc4-mini+ linux-headers-7.1.0-rc4-mini+

Configure display timings and panel driver
```````````````````````````````````````````

For Open Source Contribution:

**Vicharak Kernel**

.. code-block:: bash

  https://github.com/vicharak-in/vicharak-linux-kernel.git


- Give support of Display driver and overlays, and compile kernel and add overlays in ``/boot/overlays-<uname -r>-axon-mini`` folder.
  You can look the QCS6490 / Qualcomm device-tree overlay paths in the kernel tree.

- Ensure the kernel panel/bridge driver is configured with the correct mode (e.g., resolution, refresh rate, and color depth) via the device tree overlay or panel driver.

- If a custom timing is required, provide a panel node in the overlay with:
  - display-mode or timing parameters
  - pixel clock, hsync/vsync, and back porch values
  - bus format (e.g., RGB888)

Waveshare 4inch MIPI Display Support
-------------------------------------

`Waveshare 4inch DSI Displays <https://www.waveshare.com/4inch-dsi-lcd.htm>`_

Steps to follow for Configuration
````````````````````````````````````````

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


5. Select overlays as per your connection of MIPI Display on **DSI0** by pressing ``spacebar`` on keyboard, then select ``Ok``.

.. code-block:: console

    ┌──────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
    │ Please select overlays:                                                                  │
    │                                                                                          │
    │  [*] Enable Waveshare 4inch DSI LCD DSI0 Axon Mini                                       │
    │                                                                                          │
    │                     <Ok>                         <Cancel>                                │
    │                                                                                          │
    └──────────────────────────────────────────────────────────────────────────────────────────┘


6. To return back to terminal, press the ``Esc`` key until you exit from it.

7. In order to enable your configuration, Restart your computer or Run command ``sudo reboot`` in terminal.


Verify after reboot
````````````````````

- Check DRM connector status for the DSI panel:

.. code-block:: bash

   ls /sys/class/drm/
   cat /sys/class/drm/card0-*/status
   cat /sys/class/drm/card0-*/modes

- Check kernel **logs** for DSI panel/properties:

.. code-block:: bash

   dmesg | grep -iE 'dsi|display|panel'

- Confirm a display is **active** (if supported by the kernel):

.. code-block:: bash

   ls /sys/class/graphics/fbcon*
   cat /sys/class/graphics/fbcon/name

- Use **modetest** to confirm the DRM/KMS driver is bound and list the connected display along with its supported modes:

.. code-block:: bash

   modetest -M msm -c

Sample output:

.. code-block:: text

   opened device MSM Snapdragon DRM on driver msm (version 1.13.0 at 0)
   Connectors:
   id encoder status name size (mm) modes encoders
   ... connected DSI-1 ...
   modes:
   index name refresh (Hz) hdisp ... vtot
   #0 720x1280 60.00 ...

Troubleshooting
````````````````
- If **dmesg** reports inability to initialize DSI, verify:
  - DSI0 wiring and connector integrity
  - Correct overlay name and that the overlay is loaded
  - Kernel supports the specific MIPI Display
- If the display remains dark, check that a valid panel/bridge device is registered and that the framebuffer is assigned (fb0, fb1, etc.)
- Review documentation for model-specific timing and initialization sequences of Display
