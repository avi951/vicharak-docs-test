# Linux Upgrade Tool (upgrade_tool)

## What is Linux Upgrade Tool

Rockchip's **Linux Upgrade tool** is a proprietary solution developed by
Rockchip for flashing images onto various storage devices such as `SPI`,
`eMMC`, `SD-card`, and more. Unlike open-source
[rkdeveloptool](https://github.com/rockchip-linux/rkdeveloptool) software,
this tool does not provide access to its source code.

Instead, it is distributed solely in **binary executable** form,
allowing users to utilize the provided executable files for the purpose of
flashing images onto their desired storage devices.

## How to use Linux Upgrade Tool

### Installing required system dependencies

Linux Upgrade Tool requires the following dependencies to be installed on your Debian or Ubuntu system.

```bash
sudo apt-get install libudev-dev libusb-1.0-0-dev
```

---

For other Linux distributions, please refer to the following table for the equivalent package names.

|  Debian/Ubuntu   |    Fedora    | Arch Linux |
| :--------------: | :----------: | :--------: |
|   libudev-dev    |              |            |
| libusb-1.0-0-dev | libusb-devel |   libusb   |

**Download the Linux_Upgrade_Tool from [Vicharak GitHub](https://github.com/vicharak-in/Linux_Upgrade_Tool)**

```bash
git clone https://github.com/vicharak-in/Linux_Upgrade_Tool
```

(boot-into-maskrom-mode)=

---

### Booting the board into MaskROM mode

:::{tip}
**MaskROM mode** is a special mode that allows the board to be flashed with new firmware.
:::

To boot the board into MaskROM mode, follow the steps below:

1. Connect the board to your computer using a **USB-C** cable.

2. Short the `eMMC CLK` on the board to `GND` using [**Pogo Pin**](#vaaman-maskrom-mode) / **tweezer** / **jumper wire**.

:::{admonition} **Alternative Options to boot into MaskROM mode**
:class: tip

You can Refer to the [Alternative MaskROM boot modes](#vaaman-maskrom-mode) for more information.
:::

3. After shorting the `eMMC CLK` to `GND`, You can now release the Pogo pin.

4. Confirm that the board is in MaskROM mode by running the following command:

:::{card} sudo ./upgrade_tool ld

```bash
List of rockusb connected(1)

DevNo=1 Vid=0x2207,Pid=0x330c,LocationID=7143 Mode=Maskrom SerialNo=
```

:::

---

**Linux Upgrade Tool Usage**

```text
sudo ./upgrade_tool

---------------------Tool Usage ---------------------
Help:               H
Version:            V
Log:                LG
------------------Upgrade Command ------------------
ChooseDevice:		CD
ListDevice:		    LD
SwitchDevice:		SD
UpgradeFirmware:	UF <Firmware> [-noreset]
UpgradeLoader:		UL <Loader> [-noreset] [FLASH|EMMC|SPINOR|SPINAND]
DownloadImage:		DI <-p|-b|-k|-s|-r|-m|-u|-t|-re image>
DownloadBoot:		DB <Loader>
EraseFlash:		    EF <Loader|firmware>
PartitionList:		PL
WriteSN:		    SN <serial number>
ReadSN:			    RSN
ReadComLog:		    RCL <File>
CreateGPT:		    GPT <Input Parameter> <Output Gpt>
SwitchStorage:		SSD
----------------Professional Command -----------------
TestDevice:		    TD
ResetDevice:		RD [subcode]
ResetPipe:		    RP [pipe]
ReadCapability:		RCB
ReadFlashID:		RID
ReadFlashInfo:		RFI
ReadChipInfo:		RCI
ReadSecureMode:		RSM
WriteSector:		WS  <BeginSec> <PageSizeK> <PageSpareB> <File>
ReadLBA:		    RL  <BeginSec> <SectorLen> [File]
WriteLBA:		    WL  <BeginSec> [SizeSec] <File>
EraseLBA:		    EL  <BeginSec> <EraseCount>
EraseBlock:		    EB <CS> <BeginBlock> <BlokcLen> [--Force]
RunSystem:		    RUN <uboot_addr> <trust_addr> <boot_addr> <uboot> <trust> <boot>
-------------------------------------------------------
```

:::{tip}
You can use the above command by using `sudo ./upgrade_tool` prefix before any of the command.

**For example to erase flash:**

1. Setup the device into MaskROM mode. Refer to the [How to enter Maskrom Mode](#booting-the-board-into-maskrom-mode) for more details.
2. Run the following command to check if the device is in MaskROM mode:

:::{card} sudo ./upgrade_tool ld

```bash
List of rockusb connected(1)

DevNo=1 Vid=0x2207,Pid=0x330c,LocationID=7143 Mode=Maskrom SerialNo=
```

:::

3. Run the following command to erase the flash:

```bash
sudo ./upgrade_tool ef <firmware file>
```

Example:

```bash
sudo ./upgrade_tool ef V1.0.2311.000-vicharak-debian-bullseye-xfce-emmc.img
```

:::

::::

:::{important} Understand the firmware file formats before flashing

See the [**Firmware File Formats**](#firmware-file-formats)
:::

## Flashing RAW Image (Raw firmware) using upgrade_tool

:::{tip}
RAW images can be flashed to any storage devices such as SD card, NVMe or eMMC
using the `dd` command or the `Linux_Upgrade_Tool`.

In the following example we will use the `dd` command to flash the RAW image
to the on-board eMMC on Vicharak Vaaman.
:::

### Check for connected devices

:::{card} sudo ./upgrade_tool ld

```bash
List of rockusb connected(1)

DevNo=1 Vid=0x2207,Pid=0x330c,LocationID=7143 Mode=Maskrom SerialNo=
```

:::

### Flash the miniloader loader binary

:::{card} sudo ./upgrade_tool db rk3399_loader_xxx.bin

```bash
Download boot ok.
```

:::

### Writing the RAW GPT Image (Raw Firmware) to the storage device

:::{danger}
Make sure to flash the loader first to the storage device.
:::

:::{card} sudo ./upgrade_tool wl 0 <some_gpt_image>.img

Example:

```bash
sudo ./upgrade_tool wl 0 V1.0.2311.000-vicharak-debian-bullseye-xfce-raw.img
```

```bash
Write LBA OK.
```

:::

### Reboot the device

:::{card} sudo ./upgrade_tool rd

```bash
[sudo] password for vicharak:

Reset Device Success!
```

:::

:::{tip}
If you encounter **Reset Device Fail!** then try to manually reboot using the
power button on the board or else try removing and re-inserting the USB
power cable.
:::

---

:::{tip}
**Alternatively you can directly flash update image to eMMC using
`RK Firmware` method.**

`RK Firmware` method can be used to flash the firmware to the eMMC of the
development board or any SD-card using the tools provided by Rockchip.
:::

{#flash-update-img}

## Flash eMMC Image using (RK Firmware) method

:::{card} sudo ./upgrade_tool uf <some_rockchip_image>.img

Example:

```bash
sudo ./upgrade_tool uf V1.0.2311.000-vicharak-debian-bullseye-xfce-emmc.img
```
---
You will see this type of process: 

```bash
[sudo] password for vicharak:
Loading firmware...
Support Type:330C FW Ver:8.1.00 FW Time:2023-07-07 14:11:41
Loader ver:1.1e Loader Time:2023-07-07 14:11:08
Start to upgrade firmware...
Download Boot Start
Download Boot Success
Wait For Maskrom Start
Wait For Maskrom Success
Test Device Start
Test Device Success
Check Chip Start
Check Chip Success
Get FlashInfo Start
Get FlashInfo Success
Prepare IDB Start
Prepare IDB Success
Download IDB Start
Download IDB Success
Download Firmware Start
Download Image... (12%)
```

Once the flash is complete, the board will reboot automatically.

:::

:::{seealso}
[Vaaman Linux starting guide](linux-start-guide.md)

[Frequently Asked Questions](../../faq.rst)
:::
