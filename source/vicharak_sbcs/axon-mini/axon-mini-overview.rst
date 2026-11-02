.. _axon-mini-overview:

Overview
========

The **Axon Mini Computer** (SBC) is powered by Qualcomm's **QCS6490**.

Features
--------

The Axon Mini Single Board Computer (SBC) offers a range of hardware features, including:

.. list-table::
   :widths: 10 50
   :header-rows: 1
   :class: feature-table

   * - **Type**
     - **Feature**
   * - CPU
     - | Qualcomm® Kryo™ 670 octa-core 64-bit
       | Kryo Gold Prime: 1x high-performance core up to 2.7 GHz
       | Kryo Gold: 3x high-performance cores at 2.4 GHz
       | Kryo Silver: 4x low-power cores at 1.9 GHz
   * - Memory
     - 8 GB / 16 GB LPDDR5-3200 MHz SDRAM
   * - Storage
     - | Onboard 32 GB high-speed eMMC 5.1
       | Modular UFS 3.1 storage module (via 2x 30-pin B2B connector)
       | PCIe 3.0 x1 NVMe storage via B2B connector
   * - DSP/NPU
     - Hexagon DSP and 12 TOPS NPU
   * - GPU
     - Qualcomm® Adreno™ 643 (OpenGL® ES 3.2, DX FL12, OpenCL™ 2.0, Vulkan® 1.x)
   * - VPU
     - | Adreno VPU 633
       | Video decode up to 4K@60 for H.264/H.265/VP9
       | Video encode up to 4K@30 for H.264/H.265
       | HDR playback: HDR10 and HDR10+
   * - Display
     - | 1 X HDMI 2.1 TX (up to 4K@60Hz), via onboard eDP-to-HDMI bridge
       | 1 X TYPE-C Alt DisplayPort v1.4 (up to 4K@60Hz)
       | 1 X MIPI DSI (4 lane)
       | Up to 2 displays active at the same time
   * - Audio
     - | 1 X 3.5 mm Audio Jack
       | Speakers x 2
       | Digital Mic x 1
   * - Wireless
     - | Integrated WiFi-BT Combo Module (AMPAK AP6276S)
       | WiFi 2.4 GHz / 5 GHz / 6 GHz 2T2R
       | Bluetooth® 5.3
       | Onboard Virtual Antenna and U.FL Connector with RF Switch
   * - Ethernet
     - Ethernet expansion via PCIe daughter board modules
   * - Camera
     - | 4 X MIPI CSI [4 lanes] at 2.5 Gbps per lane via 30-pin B2B
       | 1 X MIPI CSI [4 lanes] at 2.5 Gbps per lane via 22-pin FPC
   * - PCIE
     - | PCIe 3.0 x1 via B2B Connector for M.Key, E.Key and B.Key Modules
       | PCIe 3.0 x1 via B2B Connector for USB 3.0 and Ethernet port Modules
   * - USB
     - | 2 X USB 2.0 Type-A
       | 1 X TYPE-C USB 3.1 Gen 1 (5 Gbps) with DisplayPort Alt Mode
       | USB 3.0 expansion via PCIe Daughter Board
   * - GPIO
     - | 40-Pin GPIO Header for RPi Compatibility (I2C, I3C, UART, SPI and I2S)
       | 30-Pin FPC connector with 23 extra GPIOs (I2C, I3C, UART, SPI and I2S)
   * - Debug
     - JTAG and UART for Debug

Physical Information
--------------------

.. list-table::
   :header-rows: 1

   * - **Property**
     - **Details**
   * - Weight
     - 41 g
   * - Length
     - 95 mm
   * - Width
     - 65 mm
   * - Height
     - 20 mm

.. TODO: Add Axon Mini dimension image

Use Cases
---------

Axon Mini is designed to cater to a diverse audience, including but not limited to:

**Software Developers:**
    - **Leverage**: Octa-core Qualcomm® Kryo™ 670 CPU (1x Gold Prime up to 2.7 GHz, 3x Gold at 2.4 GHz, 4x Silver at 1.9 GHz), multi-OS support
    - **Ideal For**: Application development, performance optimization, AI-driven software

**Researchers:**
    - **Leverage**: Qualcomm Dragonwing QCS6490 SoC, Hexagon 770 AI Engine (up to 12 dense TOPS), extensive connectivity
    - **Ideal For**: Custom algorithms, experiments, AI and machine learning prototyping

**Hardware Designers:**
    - **Leverage**: 40-Pin GPIO header, 30-Pin FPC connector, multiple interfaces; modular PCIe HAT expansion (Ethernet, USB 3.0, storage)
    - **Ideal For**: Developing, testing, and rapid prototyping of hardware designs

**Hobbyist Users:**
    - **Leverage**: Versatile interfaces, compact design; swappable PCIe HAT modules to add Ethernet, USB, or storage
    - **Ideal For**: Robotics, home automation, multimedia centers, DIY electronics

**AI and Machine Learning Enthusiasts:**
    - **Leverage**: Hexagon 770 AI Engine (up to 12 dense TOPS), major deep learning frameworks support
    - **Ideal For**: Machine learning applications, computer vision tasks

**Multimedia Professionals:**
    - **Leverage**: Adreno VPU 633, HDMI for 4K output, MIPI DSI, USB-C DisplayPort for 4K
    - **Ideal For**: Video editing, streaming, digital signage, AI vision applications

**Educators and Students:**
    - **Leverage**: Hands-on learning tool
    - **Ideal For**: Teaching computing technologies, programming, hardware-software integration

**IoT Implementers:**
    - **Leverage**: WiFi 6E, Bluetooth 5.3, peripheral interfaces; Dual Gigabit Ethernet and Ethernet + USB 3.0 HAT modules via PCIe
    - **Ideal For**: IoT projects, sensor integration, smart cameras, industrial systems

**Gaming and Entertainment:**
    - **Leverage**: Qualcomm® Adreno™ 643 GPU
    - **Ideal For**: Superior gaming experience, multimedia playback
    - **Drivers**: OpenGL® ES 3.2, DirectX® FL 12, OpenCL™ 2.0, Vulkan®

.. tip::

    For more information on the Axon Mini GPIOs, see :doc:`peripherals/gpio`

|

.. seealso::

    :ref:`Getting Started with Vicharak Axon Mini <axon-mini-getting-started>`

    :ref:`Downloads section <axon-mini-downloads>`
