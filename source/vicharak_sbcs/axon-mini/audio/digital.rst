#################
Digital Mic
#################

.. TODO: Add Axon Mini digital mic connector / DMIC image

The Digital Mic (DMIC) input on the Axon Mini board provides a digital
microphone interface for low-noise voice capture. Axon Mini supports
**1 × Digital Mic** (stereo DMIC path where enabled by the platform).

Key Features
------------

- Digital microphone (PDM / DMIC) interface
- Suitable for voice assistants, speech capture, and always-on listening use cases
- Captured through the Linux ALSA stack

Wiring and connectors
---------------------

Connect the digital microphone to the dedicated DMIC connector / pins on
Axon Mini. Power off the board before connecting the mic.

.. note::

   Refer to the Axon Mini pinout / hardware documentation for the exact DMIC
   signal and power pins on your board revision.

How to Setup
------------

1. Connect the digital microphone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Seat the DMIC module on the Axon Mini DMIC connector / pins
* Ensure power and data lines are connected as per the pinout
* Power on the board after the mic is connected

2. Detect the microphone
^^^^^^^^^^^^^^^^^^^^^^^^

Boot Axon Mini and open a terminal.

Run:

.. code-block:: bash

   arecord -l

Example:

.. code-block:: text

   vicharak@axon-mini:~$ arecord -l
   **** List of CAPTURE Hardware Devices ****
   ...

* Identify the capture card/device associated with the digital mic (DMIC) path.
* Note the card and device numbers for the commands below.

3. Record Audio from Digital Microphone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites
"""""""""""""

Ensure:

* Digital microphone is properly connected
* ALSA utilities are installed

Install if needed:

.. code-block:: bash

   sudo apt install alsa-utils

Step 1: Record Audio
""""""""""""""""""""

.. code-block:: bash

   arecord -D plughw:0,0 -f S16_LE -r 16000 -c 2 dmic_test.wav

Replace ``plughw:0,0`` with the DMIC capture device from ``arecord -l``.

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Select DMIC capture device
   * - ``-f S16_LE``
     - 16-bit signed little-endian format
   * - ``-r 16000``
     - Sampling rate (16 kHz)
   * - ``-c 2``
     - Stereo recording (use ``-c 1`` for mono if required)
   * - ``dmic_test.wav``
     - Output file

Step 2: Stop Recording
""""""""""""""""""""""

Press:

.. code-block:: text

   Ctrl + C

Step 3: Playback Recorded Audio
"""""""""""""""""""""""""""""""

.. code-block:: bash

   aplay dmic_test.wav

Recommended Settings for Speech Applications
"""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   arecord -D plughw:0,0 -f S16_LE -r 16000 -c 1 speech_dmic.wav

This configuration is ideal for:

* Speech recognition
* Voice assistants
* Embedded AI applications

Notes
,,,,,

* Use ``plughw`` instead of ``hw`` to allow automatic format conversion
* 16 kHz is sufficient for most voice applications
* Higher sample rates (e.g., 44100 Hz / 48000 Hz) may be used for higher quality

Troubleshooting
---------------

No audio detected
^^^^^^^^^^^^^^^^^

* Confirm the DMIC is seated correctly
* Check ``arecord -l`` for a DMIC / digital capture device
* Verify capture volume in ``alsamixer`` (``F4``)
* Check kernel logs:

  .. code-block:: bash

     dmesg | grep -iE "dmic|snd|audio"

Low audio volume
^^^^^^^^^^^^^^^^

* Increase capture gain in ``alsamixer``
* Move closer to the microphone
* Confirm the correct DMIC device is selected

Verification Checklist
----------------------

* Digital mic is securely connected
* Capture device appears in ``arecord -l``
* Recording works with ``arecord``
* Playback works with ``aplay``
* Capture levels are set in ``alsamixer``
