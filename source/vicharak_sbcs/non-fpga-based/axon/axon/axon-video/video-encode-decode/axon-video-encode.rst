#############
Video Encoder
#############

.. warning::

    We recommend to use Vicharak 6.1 kernel and latest `Ubuntu 24.04 Noble Numbat
    <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble/>`_ , in order to correctly install FFmpeg. Flash Image
    using this `Documentation </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon linux-headers-6.1.75-axon

.. note::

   The RK3588 based Axon board supports hardware encoding with the help of the MPP library. In order to use hardware encoding in Axon you will need to install ffmpeg provided at this link. Generic ffmpeg will not provide Rockchip hardware encoding support.

   .. raw:: html

      <br>

   Install ffmpeg with **Hardware Encoding/Decoding** and **RGA Filters** support using the following command:

   .. code-block:: console

      sudo apt update
      sudo apt install ffmpeg

Introduction
============
FFmpeg is a powerful open-source multimedia framework capable of recording, converting, streaming, and processing audio and video files. It supports a vast range of formats and codecs, making it a go-to solution for media handling across platforms.

For the Axon Board, FFmpeg is compiled with hardware-accelerated encoding/decoding and RGA filters, leveraging the RK3588 SoC to deliver high-performance processing of high-resolution videos.

Basic FFmpeg Commands
=====================
1. List available encoders
--------------------------
This command lists the available Rockchip MPP-based hardware encoders. On Axon, H.264, H.265 (HEVC), and MJPEG hardware-accelerated encoders are supported.

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -hide_banner -encoders | grep rkmpp

.. code-block:: console

   V..... h264_rkmpp           Rockchip MPP H264 encoder (codec h264)
   V..... hevc_rkmpp           Rockchip MPP HEVC encoder (codec hevc)
   V..... mjpeg_rkmpp          Rockchip MPP MJPEG encoder (codec mjpeg)

2. Check available options for an encoder
-----------------------------------------
This will show all the flags that can be used with a particular encoder.

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -hide_banner -h encoder=<encoder_name>

Replace ``<encoder_name>`` with any hardware or software encoder.

3. Encoding a raw file (.yuv)
-----------------------------
This command converts a raw file (.yuv) to the specified encoded format.

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -f rawvideo -pix_fmt yuv420p \
    -s:v 3840x2026 -r 25 -i raw_video.yuv -c:v h264_rkmpp \
    -b:v 10M -maxrate 12M -minrate 8M -g 50 \
    h264_encoded_video.mp4

The command above encodes raw_video.yuv with a pixel format of yuv420p and resolution 3840x2026 to a 25 FPS H.264-encoded video. Below is a description of the flags used:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-f rawvideo``
     - Tells FFmpeg that the input file is a raw video stream without any container or headers.
   * - ``-pix_fmt yuv420p``
     - Specifies the pixel format of the raw input video. Other options include ``yuv422p``, ``rgb24``, ``bgra``, etc.
   * - ``-s:v 3840x2026``
     - Sets the resolution (frame size) of the input video.
   * - ``-r 30``
     - Sets the frame rate (FPS) of the input video.
   * - ``-i input.raw``
     - Specifies the input file name.
   * - ``-c:v libx264``
     - Selects the video codec for encoding.
   * - ``-b:v 10M``
     - Sets the target bitrate to 10 Mbps for the video stream.
   * - ``-maxrate 12M``
     - Sets the maximum bitrate to 12 Mbps to limit bitrate peaks.
   * - ``-minrate 8M``
     - Ensures the encoder maintains at least 8 Mbps.
   * - ``-g 50``
     - Sets the GOP (Group of Pictures) size, inserting a keyframe every 50 frames.
   * - ``h264_encoded_video.mp4``
     - Specifies the name of the output (encoded) file.


.. note::

   Ensure you provide correct values for flags like pix_fmt, resolution, codec, and FPS to avoid encoding errors.

4. Encoding and Streaming a raw file
------------------------------------
This command encodes a raw video (.yuv) and streams it via UDP to an IP address in real time using the ``-re`` flag. The stream is sent to UDP port ``1234`` on the device with IP ``192.168.1.58``. The ``-f mpegts`` flag specifies the MPEG-TS container format.

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -re -f rawvideo -pix_fmt yuv420p \
    -s:v 3840x2026 -r 25 -i raw_video.yuv -c:v h264_rkmpp -b:v 10M \
    -maxrate 12M -minrate 8M -g 50 -f mpegts udp://192.168.1.58:1234

You can receive and play the stream on the other device using FFmpeg or FFplay:

.. tab-set::

   .. tab-item:: Using FFmpeg

      .. code-block:: console

         vicharak@vicharak:~$ ffmpeg -fflags nobuffer -flags low_delay -i udp://@:1234 -f sdl -

   .. tab-item:: Using FFplay

      .. code-block:: console

         vicharak@vicharak:~$ ffplay -fflags nobuffer -flags low_delay udp://@:1234

5. Transcoding a video
----------------------
FFmpeg can be used to transcode a video, i.e. change its encoding format (ex. AV1 to H.265). 

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -i input.mkv -c:v hevc_rkmpp output_hevc.mp4

This command decodes the original encoding (e.g., AV1) and re-encodes it to H.265 (HEVC).
Internally, the flow is: ``AV1 → raw video → H.265``.

To stream the transcoded video via UDP or other protocols, add the ``-f`` flag.

6. Streaming over RTSP
------------------------
You can stream a raw or encoded video using RTSP. Follow these steps to create an RTSP server and stream to it:

a. Start a local RTSP server:

.. code-block:: console

   wget https://github.com/bluenviron/mediamtx/releases/download/v1.12.3/mediamtx_v1.12.3_linux_amd64.tar.gz
   tar xvf mediamtx_v1.12.3_linux_amd64.tar.gz
   chmod +x mediamtx
   ./mediamtx

b. Stream from Axon to the RTSP Server:

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -re -i input.mp4 -c:v h264_rkmpp \
    -b:v 10M -maxrate 12M -minrate 8M -g 50 \
    -f rtsp rtsp://<server-ip>:8554/live.stream

c. Play the stream on a network-connected device (e.g., using VLC):

.. code-block:: console

   vlc rtsp://<server-ip>:8554/live.stream

You may also use FFplay, FFmpeg, or any compatible RTSP player.
