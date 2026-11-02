#################
Speakers
#################

.. TODO: Add Axon Mini speaker connector image

Axon Mini provides **2 × speaker** outputs. Users can connect a broad range of
speakers to the board for stereo analog playback through the onboard audio path.

Hardware Interface
==================

Speaker Specifications
----------------------

- Quantity: 2 × speaker channels (Left / Right)
- Connector Type: (Wire To Board) JST
- MPN: WAFER-125L-2A
- Pin: 2 Pin
- Pitch: 1.25 mm
- Current rating (max): 1A each pin
- Load Impedance: 4 ohm
- Rated Power: 3W

Reference Speaker
=================

User can buy `TR-WS-2014B Ultra-Thin Cavity Speaker <https://techiesms.com/product/tr-ws-2014b-ultra-thin-cavity-speaker/>`_

How to Setup
============

Follow these steps to connect and use speakers with the Axon Mini board.

1. Connect the Speaker
----------------------

Connect your speakers to the Axon Mini board:

* Speaker positive → Speaker output pin on Axon Mini (``SPK_L`` / ``SPK_R``)
* Speaker negative → Axon Mini GND

Ensure connections are secure and properly seated. Power off the board before
wiring speakers.

2. Play Audio through Speaker
-----------------------------

This section describes how to play audio through the speaker connected to the
SBC using ALSA utilities.

Prerequisites
^^^^^^^^^^^^^

Ensure:

* Speakers are properly connected to the SBC
* ALSA utilities are installed

Install if needed:

.. code-block:: bash

   sudo apt install alsa-utils

Step 1: Identify the Speaker Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List available playback devices:

.. code-block:: bash

   aplay -l

Example:

.. code-block:: text

   vicharak@axon-mini:~$ aplay -l
   **** List of PLAYBACK Hardware Devices ****
   ...

* Note the card and device number for the onboard speaker / codec path.
* Use those values in the commands below (example uses ``hw:0,0`` / ``plughw:0,0``).

Step 2: Play Audio File
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   speaker-test -D hw:0,0 -c 2

.. code-block:: bash

   aplay -D plughw:0,0 test.wav

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Select playback device
   * - ``test.wav``
     - Audio file to play

Step 3: Verify Playback
^^^^^^^^^^^^^^^^^^^^^^^

You should hear audio from the connected speakers.

Step 4: Test Speaker with Built-in Sound
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   speaker-test -D plughw:0,0 -c 2 -t wav

Parameter Explanation
,,,,,,,,,,,,,,,,,,,,,

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Meaning
   * - ``-D plughw:0,0``
     - Playback device
   * - ``-c 2``
     - Stereo channels
   * - ``-t wav``
     - WAV test sound

Stop test with:

.. code-block:: text

   Ctrl + C

Supported Audio Formats
^^^^^^^^^^^^^^^^^^^^^^^

ALSA supports:

* WAV (recommended)
* 16-bit PCM
* Mono or Stereo
* Various sample rates (16 kHz, 44.1 kHz, 48 kHz)

Example:

.. code-block:: bash

   aplay -D plughw:0,0 -f S16_LE -r 16000 -c 1 test.wav

Volume Control
^^^^^^^^^^^^^^

Open ALSA mixer:

.. code-block:: bash

   alsamixer

Use:

* Arrow keys → adjust volume
* ``F6`` → select sound card
* ``M`` → mute/unmute

Ensure output is not muted.

----

Troubleshooting
===============

No sound output
---------------

Check device list:

.. code-block:: bash

   aplay -l

Check volume:

.. code-block:: bash

   alsamixer

Ensure:

* Output channel is enabled
* Volume is not muted
* Test speaker hardware directly:

  .. code-block:: bash

     speaker-test -c 2

---

Notes
=====

* Use ``plughw`` for automatic format conversion
* WAV format is recommended for compatibility
* Load impedance must match speaker specifications (4 ohm for Axon Mini)
* Rated power is 3W per channel
