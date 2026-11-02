=======================================
Axon Mini Video Encoder/Decoder Support
=======================================

The QCS6490 Adreno VPU is a 6th-generation Ultra-HD video engine. It supports
hardware video decode up to **4K@60** and hardware video encode up to **4K@30**.

Applications typically access the VPU through the **V4L2** framework and
**GStreamer** plugins (for example ``v4l2h264enc``, ``v4l2h265enc``,
``v4l2h264dec``, ``v4l2h265dec``, and ``v4l2vp9dec``).

.. toctree::
   :maxdepth: 2

   Video Encoder <axon-mini-video-encode>
   Video Decoder <axon-mini-video-decode>
