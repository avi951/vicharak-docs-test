3.5 mm Audio Jack
==================

.. TODO: Add Axon Mini audio jack image

The 3.5 mm audio jack on Axon Mini (QCS6490) provides analog stereo output and,
where supported by the hardware, a microphone input.

Key Features
------------

- Analog stereo output via a 3.5 mm TRS jack
- Headset/jack-detect support where implemented by the board
- Full integration with ALSA, and compatibility with PulseAudio or PipeWire

Getting Started
---------------

Prerequisites

- Linux kernel with QCS6490 audio drivers enabled
- Root access
- ALSA utilities installed (``alsa-utils``)

Verification and testing

1. Identify audio devices

.. code-block:: bash

   arecord -l
   aplay -l

Example:

.. code-block:: bash

   vicharak@axon-mini:~$ arecord -l
   **** List of CAPTURE Hardware Devices ****
   ...

.. code-block:: bash

   vicharak@axon-mini:~$ aplay -l
   **** List of PLAYBACK Hardware Devices ****
   ...

2. Determine the target card/PCM for the 3.5 mm jack.

- Review the output from the commands above to locate the card corresponding to
  the onboard audio codec / headphone path.
- If multiple cards are present, select the one associated with the jack output.

3. Test playback

.. code-block:: bash

   aplay -D hw:0,0 /usr/share/sounds/alsa/Front_Center.wav

- ``aplay`` is an ALSA tool designed to play raw audio and basic WAV files. It
  does not have a built-in MP3 decoder.
- If you hear audio, the playback path is functioning for the selected card.
- Replace ``hw:0,0`` with the card/device from your ``aplay -l`` output.

4. Test recording (if a microphone input is available on the jack)

.. code-block:: bash

   arecord -D hw:0,0 -f cd -d 5 test.wav
   aplay test.wav

- If you hear playback of the recorded sample, the mic path is functioning.

5. Adjust volume and mute settings

.. code-block:: bash

   sudo apt-get install -y alsa-utils
   alsamixer

- In the interactive interface, select the correct sound card (``F6``) and ensure
  Master/Headphone/Output are unmuted and at an audible level.

6. To play an **.mp3** file, use a program that can decode MP3s.

Install and use a command-line player such as ``mpg123``, ``mpv``, or ``ffplay``.

For example, using ``mpg123``:

.. code-block:: bash

   sudo apt install mpg123
   mpg123 <Audio>.mp3

7. Optional: using PulseAudio or PipeWire

- If you rely on PulseAudio or PipeWire, ensure the ALSA sink is mapped to the
  3.5 mm output.
- Use a mixer application (``pavucontrol`` or ``pw-cli``) to select the correct
  output device (Headphones or Speaker) and input (Microphone) as needed.

Notes
-----

- Board-specific device-tree or kernel configuration may be required to enable
  the 3.5 mm jack or mic bias.
- Sound servers (PulseAudio/PipeWire) may override ALSA settings; ensure the
  correct sink/source is selected for your application.

See Also
--------

- ALSA Project: Advanced Linux Sound Architecture
- PulseAudio and PipeWire sound servers
- alsa-utils: ``arecord``, ``aplay``, ``amixer``
