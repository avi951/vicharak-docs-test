#############
Video Decoder
#############

.. warning::

    We recommend to use Vicharak 6.1 kernel and latest `Ubuntu 24.04 Noble Numbat
    <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble/>`_ , in order to correctly install FFmpeg. Flash Image
    using this `Documentation </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon linux-headers-6.1.75-axon
                                                                                
.. note::                                                                       
 
   The RK3588-based Axon board supports hardware encoding via the MPP library. To use hardware encoding on Axon, you must install FFmpeg using commands given below. The generic FFmpeg package does not support Rockchip hardware encoding/decoging.

   .. raw:: html

      <br>

   Install FFmpeg with **Hardware Encoding/Decoding** and **RGA Filter** support using the following commands:

   .. code-block:: console

      sudo apt update
      sudo apt install ffmpeg

Introduction                                                                    
============
FFmpeg is a powerful open-source multimedia framework capable of recording, converting, streaming, and processing audio and video files. It supports a wide range of formats and codecs, making it a go-to solution for media handling across platforms.
                                                                                
On the Axon Board, FFmpeg is compiled with hardware-accelerated encoding/decoding and RGA filters, leveraging the RK3588 SoC to deliver high-performance processing for high-resolution videos.
                                                                                
Basic FFmpeg Commands
=====================
1. List available decoders
--------------------------

This command lists all available Rockchip MPP-based hardware decoders. On Axon, supported decoders include H.263, H.264, H.265 (HEVC), MJPEG, VP8 and VP9. 

.. note::

   AV1 decoding using ``av1_rkmpp`` is not yet supported. You may use the ``libdav1d`` decoder as an alternative.
                                                                                
.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -hide_banner -decoders | grep rkmpp

.. code-block:: console

    V..... av1_rkmpp            Rockchip MPP AV1 decoder (codec av1)
    V..... h263_rkmpp           Rockchip MPP H263 decoder (codec h263)
    V..... h264_rkmpp           Rockchip MPP H264 decoder (codec h264)
    V..... hevc_rkmpp           Rockchip MPP HEVC decoder (codec hevc)
    V..... mjpeg_rkmpp          Rockchip MPP MJPEG decoder (codec mjpeg)
    V..... mpeg1_rkmpp          Rockchip MPP MPEG1VIDEO decoder (codec mpeg1video)
    V..... mpeg2_rkmpp          Rockchip MPP MPEG2VIDEO decoder (codec mpeg2video)
    V..... mpeg4_rkmpp          Rockchip MPP MPEG4 decoder (codec mpeg4)
    V..... vp8_rkmpp            Rockchip MPP VP8 decoder (codec vp8)
    V..... vp9_rkmpp            Rockchip MPP VP9 decoder (codec vp9)

**2. Check available options for a decoder**
---------------------------------------------
This will show all the flags which can be used with a particular decoder.
                                                                                
.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -hide_banner -h decoder=<decoder_name>           
                                                                                
``<decoder_name>`` can be replaced by any hardware or software decoder.         
                                                                                
3. Convert encoded video to a raw video
---------------------------------------

.. warning::

   Raw video files are extremely large in size. Even with the -t flag limiting the duration to 10 seconds, the raw video still occupied 8.8 GB. If your goal is just to play the video, use ffplay. However, if you actually need to decode the video, ensure that your system has sufficient storage space.

This command converts an encoded video to a raw video. Use the ``ffprobe`` command to retrieve parameters like -pix_fmt, resolution, and more.

.. code-block:: console

   vicharak@vicharak:~$ ffprobe -hide_banner input_hevc.mp4

.. code-block:: console

   Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'input_hevc.mp4':
     Metadata:
       major_brand     : isom
       minor_version   : 512
       compatible_brands: isomiso2mp41
       encoder         : Lavf58.76.100
     Duration: 00:03:08.96, start: 0.000000, bitrate: 4476 kb/s
     Stream #0:0[0x1](und): Video: hevc (Main) (hvc1 / 0x31637668), yuv420p(tv, bt709, progressive), 7680x3252 [SAR 1:1 DAR 640:271], 4473 kb/s, 25 fps, 25 tbr, 12800 tbn (default)
       Metadata:
         handler_name    : ISO Media file produced by Google Inc.
         vendor_id       : [0][0][0][0]

We get the following information from the ``ffprobe`` command:

.. csv-table::
   :header: "Property", "Value"
   :widths: 20, 20

   **Encoding Method**, HEVC
   **Pixel Format**, yuv420p
   **Resolution**, 7680x3252
   **Video Bitrate**, 4473 kb/s
   **Frame Rate**, 25 fps

The following command decodes the HEVC video into a raw YUV format using the Rockchip hardware decoder:

.. code-block:: console

   vicharak@vicharak:~$ ffmpeg -nostdin -hide_banner -c:v hevc_rkmpp \
     -i output_hevc.mp4 -t 10 -f rawvideo -pix_fmt yuv420p output.yuv

4. Decoding and playing a video
-------------------------------
You can decode and play a video using ffplay, ffmpeg, or any other player such as VLC.

.. tab-set::

   .. tab-item:: Using FFplay

      .. code-block:: console

         vicharak@vicharak:~$ ffplay -fflags nobuffer -flags low_delay input_video

   .. tab-item:: Using FFmpeg

      .. code-block:: console

         vicharak@vicharak:~$ ffmpeg -fflags nobuffer -flags low_delay -i input_video -f sdl -

   .. tab-item:: Using VLC

      .. code-block:: console

         vicharak@vicharak:~$ vlc input_video

.. note::
   **<input_video>** can refer to any video input source, such as a local file (e.g. **.mp4**), a UDP stream (e.g. **udp://@:1234**), an RTSP stream (**rtsp://<server-ip>:8554/live.stream**), or a live camera feed (e.g. **/dev/video0** or a **webcam/USB camera**).
