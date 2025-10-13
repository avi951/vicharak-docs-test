# Windows RKDevTool

<!-- TODO: Rewrite this with better explanation (https://docs.radxa.com/en/rock5/rock5a/getting-started/rkdevtool) -->

## Pre-Requisites

### USB drivers installation

Download the Rockchip [USB Drivers-Assistant](https://github.com/vicharak-in/rockchip-tools/raw/master/windows/DriverAssitant_v5.12.zip)
and unpack it.

::::{admonition} How to fix **Windows Protected You PC Error**
:class: dropdown

:::{image} ../../\../../_static/images/windows-usb-driver-assistant-run-anyway.webp
:::

::::

Click on `Install` button available on the floating menu.

:::{image} ../../\../../_static/images/windows-usb-driver-assistant-install.webp
:width: 50%
:::

Click on `Yes` button to confirm the installation.

After the installation is complete, click on `OK` button to close the window.

:::{image} ../../\../../_static/images/windows-usb-driver-assistant-install-finished.webp
:width: 50%
:::

### RKDevTool Installation

Download the Rockchip [RKDevTool](https://github.com/vicharak-in/rockchip-tools/raw/master/windows/RKDevTool_Release_v3.19.zip) and unpack it.

Change Tool language to English.

- Open the `RKDevTool` folder and edit the `config.ini` file.
- Change the `Selected` value from `1` to `2` for `Language` option.
- Save the file and close it.

:::{image} ../../\../../_static/images/windows-rkdevtool-language.webp
:width: 50%
:::

Open the RKDevTool folder and run the `RKDevTool.exe` file.

::::{admonition} How to fix **Windows Protected You PC Error**
:class: dropdown

:::{image} ../../\../../_static/images/windows-rkdevtool-run-anyway.webp
:::

::::

:::{image} ../../\../../_static/images/windows-rkdevtool-main-window.webp
:::

## How to use RKDevTool on Windows

Connect the Vaaman board to the PC using the USB cable. You will see the
`Found One LOADER Device` or `Found One MASKROM Device` message in the RKDevTool window.

:::{image} ../../\../../_static/images/windows-rkdevtool-main-window.webp
:width: 78%
:::

:::{tip}
If you don't see the `Found One LOADER Device` or `Found One MASKROM Device`
message, then you need to put the Vaaman board in the `Loader Mode` or `Maskrom Mode`.

Refer to the [How to enter Maskrom Mode](#vaaman-maskrom-mode) for more details.
:::

## Flash eMMC Image to Vaaman board

Once the Vaaman board is booted into **Maskrom mode**, you can flash the **eMMC image** to the board.

:::{image} ../../\../../_static/images/windows-rkdevtool-upgrade-firmware-not-selected.webp
:width: 78%
:::

**1. Click on the `Upgrade Firmware` button from the top bar and select the `firmware` option.**

:::{image} ../../\../../_static/images/windows-rkdevtool-upgrade-firmware-selected.webp
:width: 78%
:::

**2. Select the `firmware` file from the `firmware` folder.**

:::{tip}
You can get the latest firmware from the [Vaaman Downloads](#downloads) page.
:::

**3. Click on the `Upgrade` button to start the flashing process.**

:::{image} ../../\../../_static/images/windows-rkdevtool-upgrade-firmware-success.webp
:width: 78%
:::

**4. Wait for the flashing process to complete.**
