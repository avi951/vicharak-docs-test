-------------------
HDMI TX
-------------------

HDMI 2.1 TX Port on Axon Mini Board
====================================

The Axon Mini board provides an HDMI 2.1 TX port for connecting external displays such as monitors, TVs, or projectors.

Hardware Connection
-------------------

- The Axon Mini board provides:

  - 1 × HDMI TX port

- To connect a display:

  1. Locate the HDMI TX port on the board (labeled **HDMI TX**).
  2. Connect a **High Speed HDMI 2.1 cable** from the board to the display.
  3. Power on both the board and the display.
  4. Set the display input source to the corresponding HDMI port.
  5. Restart the display manager so the HDMI pipeline rebinds to the monitor
     (no full board reboot required):

     .. code-block:: bash

        sudo systemctl restart display-manager

     After LightDM / the desktop session restarts, the login screen or desktop
     should appear on the HDMI display.

Verify HDMI Connection (DRM)
----------------------------

Use the DRM sysfs interface to confirm the HDMI connector status. These commands
work from UART / SSH and do not require an X11 session.

List DRM connectors:

.. code-block:: bash

   ls /sys/class/drm/

Example output:

.. code-block:: text

   card0  card0-HDMI-A-1  card0-Writeback-1  renderD128  version

Check connector status:

.. code-block:: bash

   cat /sys/class/drm/card0-HDMI-A-1/status

Expected when a monitor is attached:

.. code-block:: text

   connected

Check whether the connector is enabled:

.. code-block:: bash

   cat /sys/class/drm/card0-HDMI-A-1/enabled

List supported modes reported by the monitor:

.. code-block:: bash

   cat /sys/class/drm/card0-HDMI-A-1/modes

Example output:

.. code-block:: text

   1920x1080
   1280x720
   1024x768
   800x600
   720x480
   640x480

Read and decode EDID (optional):

.. code-block:: bash

   sudo apt install edid-decode
   sudo cat /sys/class/drm/card0-HDMI-A-1/edid | edid-decode

Force Connector Redetect
------------------------

To ask the DRM stack to redetect the HDMI connector:

.. code-block:: bash

   echo detect | sudo tee /sys/class/drm/card0-HDMI-A-1/status
   sleep 1
   cat /sys/class/drm/card0-HDMI-A-1/status
   cat /sys/class/drm/card0-HDMI-A-1/modes

If the desktop still does not appear on the monitor after redetect, restart the
display manager:

.. code-block:: bash

   sudo systemctl restart display-manager

Troubleshooting: HDMI Not Detected or No Display
------------------------------------------------

Check Physical Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ensure the HDMI cable is securely connected to both the board and the display.
- Verify the display is powered on.
- Confirm the correct HDMI input source is selected on the display.
- Try a different HDMI cable or display if necessary.

Check DRM Status
^^^^^^^^^^^^^^^^

.. code-block:: bash

   ls /sys/class/drm/

Expected output:

.. code-block:: text

   card0  card0-HDMI-A-1  card0-Writeback-1  renderD128  version

.. code-block:: bash

   cat /sys/class/drm/card0-HDMI-A-1/status

Expected output:

.. code-block:: text

   connected

.. code-block:: bash

   cat /sys/class/drm/card0-HDMI-A-1/enabled

Expected output:

.. code-block:: text

   enabled

.. code-block:: bash

   cat /sys/class/drm/card0-HDMI-A-1/modes

Expected output:

.. code-block:: text

   1920x1080
   1280x720
   1024x768
   800x600
   720x480
   640x480

- ``status`` should be ``connected``
- ``enabled`` should be ``enabled`` when the pipeline is active
- ``modes`` should list resolutions (empty modes usually means EDID / link setup failed)

Restart Display Pipeline
^^^^^^^^^^^^^^^^^^^^^^^^

Preferred (no reboot):

.. code-block:: bash

   sudo systemctl restart display-manager

If that does not recover the output:

.. code-block:: bash

   sudo reboot

Check Kernel Messages
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   dmesg | grep -iE 'hdmi|edid|bridge|msm_dp|drm'

Ensure the HDMI / eDP bridge path is probed and that no persistent link errors
remain after reconnecting the display.
