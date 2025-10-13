(rockchip-develop-tool)=

# Rockchip Development Tool Guide

Rockchip offers the [**RKDevTool**](#windows-rkdevtool) as a fundamental
development tool for Windows, and [**Linux Upgrade Tool**](#linux-upgrade-tool)
for Linux and mac-OS.

This tool is used to upgrade or flash the firmware on Rockchip SoCs and it is the primary tool
used for flashing **Vaaman Linux** images to the eMMC, SD-Card, or other storage devices.

:::{tip}
Vicharak's rockchip based boards supports **MaskROM mode**, which is a special
operation mode that allows the board to be flashed with new firmware.

We will use [**Linux Upgrade Tool**](#linux-upgrade-tool) for Linux/Mac-OS and
[**RKDevTool**](#windows-rkdevtool) for Windows.
:::

````{admonition} This tool supports following features:
:class: tip

```
- Downloading firmware
- Erasing flash
- Writing firmware
- Reading flash
- Reading information
- Formatting flash
- Resetting device
- Rebooting device
- Upgrading firmware

And many more.
```
````

:::{tip} Understand the firmware file formats before flashing

See the [**Firmware File Formats**](#firmware-file-formats)
:::

```{toctree}
---
caption: Contents
maxdepth: 2
---

windows-rkdevtool
linux-upgrade-tool
```
