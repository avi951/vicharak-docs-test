.. _axon-mini-display:

####################################
Display Interfaces
####################################

Axon Mini supports up to 2 independent displays simultaneously using the QCS6490 display subsystem (Adreno DPU 1075).

Key Features
============

The QCS6490 display subsystem supports the following key features:

- Wayland and Weston with upstream-aligned protocol
- Weston with direct rendering manager (DRM) backend module
- Weston remote desktop protocol (RDP) backend
- DSI interface
- Native eDP 1.4 interface
- DisplayPort over USB Type-C interface

The QCS6490 does not contain multiple independent Video Port controllers like larger SoCs. Instead, it exposes two concurrent display pipelines that can be routed to DSI, native eDP, or DisplayPort. On Axon Mini, the native eDP output from the SoC is routed through an onboard eDP-to-HDMI bridge IC to provide an HDMI 2.1 connector, rather than being broken out as a direct eDP panel connector.

Physical display connectors on the board are mapped internally to these display pipelines through various display interfaces such as HDMI (via eDP bridge), DisplayPort, and MIPI-DSI.

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-displayPipelines.webp
   :width: 60%

Display Pipeline Components
=============================

The diagram above shows the internal stages of the QCS6490 display pipeline, from source surface to physical output:

+----------------------------------------+---------------------------------------------------------+
| Component                              | Description                                             |
+========================================+=========================================================+
| ViG / DMA source surface pipes         | Reads RGB and YUV surfaces from gaming and video        |
|                                        | applications; performs format conversion and quality    |
|                                        | improvements on the source                              |
+----------------------------------------+---------------------------------------------------------+
| Layer mixer                            | Blends and mixes source surfaces together               |
+----------------------------------------+---------------------------------------------------------+
| DSPP (destination surface processor    | Converts, corrects, and adjusts the data based on panel |
| pipes)                                 | characteristics                                         |
+----------------------------------------+---------------------------------------------------------+
| Display stream compression (DSC)       | Reduces bandwidth and power consumption by sending a    |
|                                        | compressed display buffer to the display                |
+----------------------------------------+---------------------------------------------------------+
| Display stream compression interface   | Connects the DSC to the display interface               |
+----------------------------------------+---------------------------------------------------------+
| Display interface (DSI, DisplayPort,   | Generates timings for the connected display peripherals |
| eDP)                                   |                                                         |
+----------------------------------------+---------------------------------------------------------+

Interfaces and Capabilities
============================

The device supports two displays simultaneously and offers various configurations for maximum concurrency, as summarized below.

+------------------------+--------------------------------------------------------------+
| Interface              | Capabilities                                                 |
+========================+==============================================================+
| DSI0                   | FHD+ (1200 × 2520) at 120 fps (8-bit). Supports VESA Display |
|                        | Stream Compression (DSC) 1.2                                 |
+------------------------+--------------------------------------------------------------+
| DisplayPort            | 3840 × 2160 resolution at 30 fps, 24 bpp (requires two lanes |
|                        | at HBR3). Single stream transport (SST) only                 |
+------------------------+--------------------------------------------------------------+
| eDP → HDMI bridge      | Native eDP supports max 3840 × 2160 at 60 fps; on Axon Mini  |
|                        | this is routed through the onboard eDP-to-HDMI bridge IC to  |
|                        | the HDMI 2.1 connector                                       |
+------------------------+--------------------------------------------------------------+

.. note::

   Only two display pipelines are available on the QCS6490, so a maximum of two independent displays can be active at the same time, regardless of how many physical connectors are populated on the board.

   Maximum concurrency:

   - HD+ (1200 × 2520) (8-bit) at 60 fps with DSI primary + 4K at 30 fps DisplayPort
   - Or 1920 × 1080p at 60 fps with eDP (HDMI bridge) primary + 4K at 30 fps DisplayPort

   On Axon Mini, DSI and HDMI (via the eDP bridge) cannot be used simultaneously, since both are driven from the same primary display pipeline path on the QCS6490.

Available Display Interface Ports on Axon Mini
================================================

Axon Mini exposes three physical display interface ports. These connectors are internally mapped to the two available display pipelines.

.. note::

   Although three physical display connectors are available, only two independent displays can be active simultaneously due to the hardware limitation of the QCS6490 display subsystem, and DSI + HDMI cannot be driven together (see above).

Available display interface ports:

1. HDMI 2.1 (via onboard eDP-to-HDMI bridge IC)
2. 4-Lane MIPI-DSI (D-PHY 1.2 / C-PHY 1.2, VESA DSC 1.2)
3. Type-C DP (USB-C, native DisplayPort, single stream transport, HBR3)

Detailed documentation for each interface is provided below:

.. toctree::
   :maxdepth: 3

   HDMI 2.1 (eDP bridge) <display-interfaces>
   MIPI DSI (native)     <mipi-dsi>
   Type-C DisplayPort 1.4 <type-c-dp>

For display-related questions:

- Check hardware documentation
- Visit `Vicharak Community <https://discuss.vicharak.in>`_
