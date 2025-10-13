
##############
Audio
##############


.. variable

.. _Axon GPIO Header: https://docs.vicharak.in/vicharak_sbcs/axon/axon-gpio-description/#axon-gpios-header


Overview
========
The rockchip-es8388 audio codec, detected as ``card 0`` in Linux, is an I2S-based audio solution used on the Axon platform. It enables both audio input and output functionality through the ES8388 chip, which integrates a DAC (Digital-to-Analog Converter) and an ADC (Analog-to-Digital Converter). This codec interfaces with the system via the I2S bus and is commonly used in designs requiring high-quality analog audio capture and playback.

.. image:: /_static/images/rk3588-axon/axon-analog-speaker.webp
   :width: 60%

Hardware Interface
==================

.. image:: /_static/images/rk3588-axon/axon-audio.webp
   :width: 60%


Speaker Output
--------------

- **Connector Type:** W2B Connector
- **Pin Count:** 2-pin
- **Pin Pitch:** 1.25mm
- **Current Rating:** Max 1A per pin
- **MPN:** WAFER-125L-2A

- **Speaker Specifications:**
  - Load Impedance: 4 ohm
  - Rated Power: 3W

Microphone Input
----------------

- **Type:** Analog Differential Microphone

.. warning::

  If you want to use an **analog single-ended microphone**, connect:
  
  - The **positive wire** of the microphone to the **positive pin** of the mic connector.
  - The **negative wire** of the microphone to **ground** on Axon GPIO Pin Header.
  
  This configuration allows compatibility with both differential and single-ended analog microphones.
  
.. tip::
    To get more information on `Axon GPIO Header`_. 


Device Information
==================

``aplay -l``  lists all sound cards and their playback devices that are recognized by ALSA (Advanced Linux Sound Architecture) on your system.

.. code-block:: bash

   vicharak@vicharak:~$ aplay -l
   **** List of PLAYBACK Hardware Devices ****
   card 0: rockchipes8388 [rockchip-es8388], device 0: dailink-multicodecs ES8323 HiFi-0 [dailink-multicodecs ES8323 HiFi-0]
     Subdevices: 1/1
     Subdevice #0: subdevice #0


This indicates that:

- The ALSA card index is 0.

- The playback device index is 0.

- The hardware device name can be referred as `hw:0,0`.

Playback Using aplay
--------------------

You can use the ALSA `aplay` tool to play WAV audio files using the `rockchip-es8388` codec:

.. code-block:: bash

   aplay -D hw:0,0 test.wav

Where:

- ``-D hw:0,0`` selects the rockchip-es8388 card and its device.

- ``test.wav`` should be a valid ``.wav`` file (preferably 16-bit, 44.1kHz or 48kHz).

Check supported formats:

.. code-block:: bash

   aplay -D hw:0,0 --dump-hw-params /dev/zero

This will print the supported formats, rates, and channel configurations for the device.


.. code-block:: bash

  vicharak@vicharak:~$ aplay -D hw:0,0 --dump-hw-params /dev/zero
  Playing raw data '/dev/zero' : Unsigned 8 bit, Rate 8000 Hz, Mono
  HW Params of device "hw:0,0":
  --------------------
  ACCESS:  MMAP_INTERLEAVED RW_INTERLEAVED
  FORMAT:  S16_LE S24_LE
  SUBFORMAT:  STD
  SAMPLE_BITS: [16 32]
  FRAME_BITS: [32 64]
  CHANNELS: 2
  RATE: [8000 96000]
  PERIOD_TIME: (333 8192000]
  PERIOD_SIZE: [32 65536]
  PERIOD_BYTES: [256 524288]
  PERIODS: [2 4096]
  BUFFER_TIME: (666 16384000]
  BUFFER_SIZE: [64 131072]
  BUFFER_BYTES: [256 524288]
  TICK_TIME: ALL
  --------------------
  aplay: set_params:1371: Sample format non available
  Available formats:
  - S16_LE
  - S24_LE

Setting Volume with amixer
--------------------------

You can adjust the playback volume using `amixer`:

.. code-block:: bash

   amixer -c 0

This shows all controls for the ES8388 device.

Troubleshooting
===============

- **No sound**:
  - Ensure the output device (e.g., speaker or headphone) is connected properly.

  - Use ``alsamixer -c 0`` and check if the output channels are unmuted and have volume.

  - Make sure your ``.wav`` file format matches the supported codec parameters.

- **Permission Denied**:

  - Run commands with ``sudo``, or ensure the user is in the ``audio`` group.

- **Device Busy**:

  - Some other process (like PulseAudio or PipeWire) may be using the device. Try stopping them or use `aplay` with `-D plughw:0,0`.

Useful Commands
================

.. code-block:: bash

   aplay -l                   # List all playback devices
   aplay -D hw:0,0 file.wav   # Play audio using ES8388
   alsamixer -c 0            # Graphical volume control for ES8388
   amixer -c 0               # Command-line mixer settings
   speaker-test -D hw:0,0 -c 2 -t wav  # Test stereo output
