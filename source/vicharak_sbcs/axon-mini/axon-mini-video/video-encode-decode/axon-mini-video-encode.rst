#############
Video Encoder
#############

Axon Mini uses the Qualcomm **Adreno VPU** on the QCS6490 to accelerate video
encoding. Raw frames (typically YUV from camera or memory) are passed from
user-space applications through the V4L2 stack into the Adreno VPU driver and
firmware, which returns a compressed bitstream for muxing, streaming, or
storage.

Software Architecture
=====================

The following diagram shows the QCS6490 video encoder software architecture:

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-qcs6490-encoder.webp
   :width: 70%
   :alt: QCS6490 video encoder software architecture

**Flow summary**

1. A **Camera Source** (or other YUV source) provides raw **YUV buffers** to the
   application.
2. The application (V4L2 / GStreamer) submits buffers through the **V4L2
   framework** to the **Adreno VPU driver**.
3. The **Adreno VPU** hardware and firmware encode the frames.
4. Compressed **bitstream buffers** return to the application and can be written
   by a **FileMuxer** (for example MP4) or streamed over the network.

Encoder Capabilities
====================

On QCS6490, hardware encode supports **H.264 (AVC)** and **H.265 (HEVC)** up to
**4096×2160 @ 30 fps**. VP9 and AV1 encode are not supported on this SoC.

Codec support
-------------

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - **Codec**
     - **Profiles / levels**
     - **Limits**
   * - H.264 (AVC)
     - Constrained Baseline, Baseline, Main, High, Constrained High; up to level 5
     - Min 128×128; max 4096×2160 or 2160×4096; up to 240 fps; up to 100 Mbps
   * - H.265 (HEVC)
     - Main profile (8-bit), up to level 5.0; Main/High tier
     - Same resolution / fps / bitrate envelope as H.264; vertical tiling for frame width ≥ 960

Supported resolution points
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 20 25

   * - **Resolution**
     - **Frame rate**
     - **Max bitrate**
   * - 1280×720
     - up to 240 fps
     - 100 Mbps
   * - 1920×1088
     - up to 120 fps
     - 100 Mbps
   * - 3840×2160
     - up to 30 fps
     - 100 Mbps
   * - 4096×2160
     - up to 30 fps
     - 100 Mbps

Encoder features
----------------

.. list-table::
   :header-rows: 1
   :widths: 28 42 30

   * - **Feature**
     - **Description**
     - **Codecs**
   * - Input color formats
     - NV12, QC08C
     - H.264, HEVC
   * - Rate control
     - CBR, VBR, MBR
     - H.264, HEVC
   * - Rotation
     - 90° / 180° / 270° before encode (static)
     - H.264, HEVC
   * - Flip
     - Horizontal / vertical flip (static and dynamic)
     - H.264, HEVC
   * - B-frames
     - Up to 1 B-frame between P-frames; up to 1920×1088 @ 60 fps
     - H.264, HEVC
   * - Hierarchical-P
     - Up to 5 layers
     - H.264, HEVC
   * - Slice encode
     - Bits/slice or macroblocks/slice
     - H.264, HEVC
   * - Intra refresh
     - Random refresh; 8-bit and CBR only
     - H.264, HEVC
   * - LTR frames
     - Up to 2 long-term reference frames; CBR only
     - H.264, HEVC
   * - Dynamic controls
     - Sync frame, bitrate, frame rate
     - H.264, HEVC
   * - Multi-instance
     - Up to 16 concurrent instances (subject to macroblock budget)
     - H.264, HEVC

GStreamer plugins commonly used for encode on this platform include
``v4l2h264enc`` and ``v4l2h265enc``.

Use Cases
=========

The following GStreamer use cases demonstrate camera capture and hardware
encode on Axon Mini. Replace ``<IP_address>`` with the board IP where required.
Press ``CTRL + C`` to stop a running pipeline.

One stream - 1080p AVC RTSP from live source
--------------------------------------------

Start the RTSP server in one console:

.. code-block:: console

   gst-rtsp-server -p 8900 -a "<IP_address>" -m /live "( udpsrc name=pay0 port=8554 caps=\"application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96\" )"

Run the encode and stream pipeline:

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc name=camsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse config-interval=-1 ! rtph264pay pt=96 ! udpsink host=<IP_address> port=8554

View the stream from a host PC:

.. code-block:: console

   ffplay -rtsp_transport tcp rtsp://<IP_address>:8900/live

Two streams - 4K AVC and 480p AVC from live source
--------------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc name=camsrc video_0::type=preview ! video/x-raw\(memory:GBM\),format=NV12,width=3840,height=2160,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux1.mp4" camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=640,height=480,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux2.mp4"

Three 1080p AVC streams from live source
----------------------------------------

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc name=camsrc video_0::type=preview ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux1.mp4" camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux2.mp4" camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux3.mp4"

Three streams - 1080p AVC, 1080p HEVC, and 1080p YUV preview
------------------------------------------------------------

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc name=camsrc video_0::type=preview ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux1.mp4" camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h265enc capture-io-mode=5 output-io-mode=5 ! queue ! h265parse ! mp4mux ! queue ! filesink location="/opt/mux_hevc.mp4" camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc ! waylandsink sync=false fullscreen=true enable-last-sample=false

Three streams - 1080p AVC file save, 1080p AVC RTSP, and YUV preview
--------------------------------------------------------------------

Start the RTSP server:

.. code-block:: console

   gst-rtsp-server -p 8900 -a <IP_address> -m /live "( udpsrc name=pay0 port=8554 caps=\"application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96\" )"

Run the pipeline:

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc name=camsrc video_0::type=preview ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse ! mp4mux ! queue ! filesink location="/opt/mux.mp4" camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 ! queue ! h264parse config-interval=-1 ! rtph264pay pt=96 ! udpsink host=<IP_address> port=8554 camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc ! waylandsink fullscreen=true async=true sync=false

Slice-based encoding
--------------------

H.264 - 1280×720, maximum slices per frame = 10:

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1280,height=720,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 extra-controls="controls,slice_partitioning_method=1;" ! filesink location="/opt/encoded.h264"

H.264 - 1920×1080, slices per frame = 3:

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h264enc capture-io-mode=5 output-io-mode=5 extra-controls="controls,slice_partitioning_method=1,number_of_mbs_in_a_slice=2720;" ! filesink location="/opt/encoded.h264"

H.265 - 1280×720, maximum slices per frame = 10:

.. code-block:: console

   gst-launch-1.0 -e qtiqmmfsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1280,height=720,framerate=30/1,compression=ubwc,interlace-mode=progressive,colorimetry=bt601 ! queue ! v4l2h265enc capture-io-mode=5 output-io-mode=5 extra-controls="controls,slice_partitioning_method=1;" ! filesink location="/opt/encoded.h265"

Intra-frame smart codec (H.264)
-------------------------------

.. code-block:: console

   gst-launch-1.0 -ev qtiqmmfsrc noise-reduction=2 video_0::extra-buffers=20 video_0::type=preview name=camsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc ! queue ! scb.sink qtismartcodecbin default-gop=30 max-gop=600 levels-override="LevelsOverride,bitrate_static=160000,bitrate_low=358000,bitrate_medium=700000,bitrate_high=1400000,fr_static=16,fr_low=4,fr_medium=2,fr_high=1;" roi-quality-cfg="ROIQPs,car=2,person=1,tree=-2;" encoder="v4l2h264enc" max-bitrate=4200000 name=scb ! queue ! h264parse ! queue ! mp4mux ! queue ! filesink location=/opt/video.mp4 camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=640,height=480,framerate=15/1 ! queue ! scb.sink_ctrl

Intra-frame smart codec (H.265)
-------------------------------

.. code-block:: console

   gst-launch-1.0 -ev qtiqmmfsrc noise-reduction=2 video_0::extra-buffers=20 video_0::type=preview name=camsrc ! video/x-raw\(memory:GBM\),format=NV12,width=1920,height=1080,framerate=30/1,compression=ubwc ! queue ! scb.sink qtismartcodecbin default-gop=30 max-gop=600 levels-override="LevelsOverride,bitrate_static=160000,bitrate_low=358000,bitrate_medium=700000,bitrate_high=1400000,fr_static=16,fr_low=4,fr_medium=2,fr_high=1;" roi-quality-cfg="ROIQPs,car=2,person=1,tree=-2;" encoder="v4l2h265enc" max-bitrate=4200000 name=scb ! queue ! h265parse ! queue ! mp4mux ! queue ! filesink location=/opt/video.mp4 camsrc. ! video/x-raw\(memory:GBM\),format=NV12,width=640,height=480,framerate=15/1 ! queue ! scb.sink_ctrl

