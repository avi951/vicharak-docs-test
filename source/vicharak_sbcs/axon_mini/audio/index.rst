.. _axon-mini-audio:

###################
Audio Interface
###################

.. TODO: Add Axon-Mini audio documentation

This section covers audio capabilities of Axon-Mini.

.. toctree::
   :glob:
   :maxdepth: 3
   :titlesonly:

Audio Details
=============

.. TODO: Add Axon-Mini audio interface information

For audio-related questions:

- Check hardware documentation
- Visit `Vicharak Community <https://discuss.vicharak.in>`_

Headphone Output
----------------

- 1 dedicated headphone jack
- Stereo output for headphones

HDMI Audio
----------

- Audio over HDMI output
- Integrated with HDMI display output

DisplayPort Audio
-----------------

- Audio over USB-C DisplayPort
- Integrated with DisplayPort output

Audio Inputs
============

Microphone Input
----------------

- 1 analog microphone input
- Single-ended input

Headphone/Microphone Jack
--------------------------

- Combination input/output option available on some models

Line-In
-------

- 1 analog line-in input
- For connecting external audio sources

Audio Configuration
===================

ALSA Configuration
------------------

Advanced Linux Sound Architecture configuration

PulseAudio
----------

Audio server and daemon configuration

Volume Control
==============

Master Volume
-------------

Per-Device Volume
-----------------

Audio Input Levels
------------------

Recording Audio
===============

Using Linux Audio Recording Tools
---------------------------------

- ALSA record utilities
- ffmpeg for recording
- Other recording software

Audio Formats Support
=====================

Supported Codecs
----------------

- PCM (WAV)
- MP3
- FLAC
- AAC
- Vorbis
- And more

Sample Rates
------------

- 8 kHz to 192 kHz or higher

Bit Depths
----------

- 8-bit, 16-bit, 24-bit, 32-bit

Troubleshooting
===============

No Audio Output
---------------

Audio Input Not Working
-----------------------

Audio Quality Issues
--------------------

Driver and Kernel Module Issues
-------------------------------

For additional support:

- Check kernel logs: ``dmesg | grep -i audio``
- List audio devices: ``aplay -l`` and ``arecord -l``
- Check ALSA mixer: ``alsamixer``

Community Support
=================

For audio-related issues and questions, visit:

- `Vicharak Community <https://discuss.vicharak.in>`_
- Linux Audio Documentation
