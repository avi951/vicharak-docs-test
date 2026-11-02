#############
Video Decoder
#############

Axon Mini uses the Qualcomm **Adreno VPU** on the QCS6490 to accelerate video
decoding. Compressed bitstreams from a file or stream are demuxed in user space,
passed through the V4L2 stack to the Adreno VPU driver and firmware, and returned
as YUV frames for display or further processing.

Software Architecture
=====================

The following diagram shows the QCS6490 video decoder software architecture:

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-qcs6490-decoder.webp
   :width: 70%
   :alt: QCS6490 video decoder software architecture

**Flow summary**

1. A **FileSource** provides a container file (for example MP4 or WebM).
2. A **Demuxer** extracts the compressed **bitstream buffer**.
3. The application (V4L2 / GStreamer) submits bitstream buffers through the
   **V4L2 framework** to the **Adreno VPU driver**.
4. The **Adreno VPU** hardware and firmware decode the stream.
5. Decoded **YUV buffers** return to the application for **Display** or file
   dump.

Decoder Capabilities
====================

On QCS6490, hardware decode supports **H.264**, **H.265 (HEVC)**, and **VP9**
up to **4096×2160 @ 60 fps**. AV1 decode is not supported on this SoC.

Codec support
-------------

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - **Codec**
     - **Profiles / levels**
     - **Limits / notes**
   * - H.264 (AVC)
     - Constrained Baseline, Baseline, Main, High, Constrained High; up to level 5.2
     - Min 96×96; max 4096×2160 or 2160×4096; up to 480 fps; up to 100 Mbps; max 10 slices/frame; FMO, ASO, redundant slices, and interlaced not supported
   * - H.265 (HEVC)
     - Main 8-bit and Main 10-bit up to level 5.1 (HLG)
     - Same resolution / fps / bitrate envelope; max 128 slices/frame; no individual slice-based decoding
   * - VP9
     - Profile 0 (8-bit) and Profile 2 (10-bit) up to 5.1; HLG/PQ
     - Same resolution / fps / bitrate envelope; Profile 2 12-bit not supported

Supported resolution points
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 20 25

   * - **Resolution**
     - **Frame rate**
     - **Max bitrate**
   * - 1280×720
     - up to 480 fps
     - 100 Mbps
   * - 1920×1088
     - up to 240 fps
     - 100 Mbps
   * - 3840×2160
     - up to 60 fps
     - 100 Mbps
   * - 4096×2160
     - up to 60 fps
     - 100 Mbps

Decoder features
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 42 30

   * - **Feature**
     - **Description**
     - **Codecs**
   * - Output color formats
     - NV12, QC08C, QC10C
     - H.264, HEVC, VP9
   * - 10-bit playback
     - Supported for HEVC and VP9
     - HEVC, VP9
   * - HDR
     - HDR10 / HDR10+ playback paths as supported by the media stack
     - HEVC, VP9
   * - Multi-instance
     - Up to 16× 1920×1088 @ 30 fps (subject to macroblock budget)
     - H.264, HEVC, VP9
   * - Concurrent encode + decode
     - Example: 1920×1088 @ 60 decode + 1920×1088 @ 60 encode; or 3840×2160 @ 30 decode + 1920×1088 @ 30 encode
     - Mixed

GStreamer plugins commonly used for decode on this platform include
``v4l2h264dec``, ``v4l2h265dec``, and ``v4l2vp9dec``.

Use Cases
=========

The following GStreamer use cases demonstrate hardware decode and playback on
Axon Mini. Replace ``<h264_file>``, ``<h265_file>``, and ``<vp9_file>`` with
your media file names. Press ``CTRL + C`` to stop a running pipeline.

Single stream video playback (H.264) - display
----------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<h264_file>.mp4 ! qtdemux ! queue ! h264parse ! v4l2h264dec capture-io-mode=5 output-io-mode=5 ! waylandsink enable-last-sample=false fullscreen=true

Single stream video playback (H.264) - save YUV
-----------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<h264_file>.mp4 ! qtdemux ! queue ! h264parse ! v4l2h264dec capture-io-mode=5 output-io-mode=5 ! filesink location="/opt/video.yuv"

Single stream video playback (H.265) - display
----------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<h265_file>.mp4 ! qtdemux ! queue ! h265parse ! v4l2h265dec capture-io-mode=5 output-io-mode=5 ! waylandsink enable-last-sample=false fullscreen=true

Single stream video playback (H.265) - save YUV
-----------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<h265_file>.mp4 ! qtdemux ! queue ! h265parse ! v4l2h265dec capture-io-mode=5 output-io-mode=5 ! filesink location="/opt/video.yuv"

Single stream video playback (VP9) - display
--------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<vp9_file>.webm ! matroskademux ! v4l2vp9dec capture-io-mode=5 output-io-mode=5 ! waylandsink fullscreen=true

Single stream video playback (VP9) - save YUV
---------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<vp9_file>.webm ! matroskademux ! v4l2vp9dec capture-io-mode=5 output-io-mode=5 ! filesink location="/opt/video.yuv"

Two 1080p streams video playback simultaneously
-----------------------------------------------

Run in console 1:

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<1080p_H264_file>.mp4 ! qtdemux ! queue ! h264parse ! v4l2h264dec capture-io-mode=5 output-io-mode=5 ! waylandsink x=0 y=0 width=960 height=540

Run in console 2:

.. code-block:: console

   gst-launch-1.0 -e filesrc location=/opt/<1080p_H264_file>.mp4 ! qtdemux ! queue ! h264parse ! v4l2h264dec capture-io-mode=5 output-io-mode=5 ! waylandsink x=0 y=540 width=960 height=540

Frame skip / frame-rate conversion
----------------------------------

Encode a 1080p@30 AVC file from camera (optional prep step):

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc name=camsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! queue ! mp4mux ! queue ! filesink location=/opt/video.mp4

Decode and re-encode at 15 fps:

.. code-block:: console

   gst-launch-1.0 filesrc location="/opt/video.mp4" ! qtdemux ! queue ! h264parse ! v4l2h264dec capture-io-mode=5 output-io-mode=5 ! videorate ! video/x-raw,framerate=15/1 ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! h264parse ! mp4mux ! queue ! filesink location="/opt/vid2.mp4"

Camera encode → decode → videorate at 20 fps → save:

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! v4l2h264dec capture-io-mode=5 output-io-mode=5 ! videorate ! video/x-raw,framerate=20/1 ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! h264parse ! mp4mux ! queue ! filesink location="/opt/video20fps.mp4"

