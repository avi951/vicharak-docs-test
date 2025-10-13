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

(install-upgrade-tool)=
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


### Download Linux Upgrade Tool

**Download from [Vicharak GitHub](https://github.com/vicharak-in/Linux_Upgrade_Tool)**

```bash
git clone https://github.com/vicharak-in/Linux_Upgrade_Tool
```

(boot-into-maskrom-mode)=

---

### Flash eMMC image in Axon 

:::{tip}
**MaskROM mode** is a special mode that allows the board to be flashed with new firmware.
:::

To get the board into MaskROM mode, follow the steps below:

1. Connect the board to your computer using a **USB-C** cable.

2. To get Axon in MaskRom Mode, Need to press reset button 2-3 times while holding boot button.
 
 [Watch Video tutorial to get Board in MaskRom
    Mode](https://youtu.be/rW-R1MJhBGA?si=25YRNOFCT8KS9C31)

3. Confirm that the board is in MaskROM mode by running the following command:

:::{card} sudo ./upgrade_tool ld

```bash
List of rockusb connected(1)
DevNo=1	Vid=0x2207,Pid=0x350b,LocationID=12	Mode=Maskrom	SerialNo=
```
:::

4. Using `uf` command, you can flash firmware in eMMC.

```bash
sudo ./upgrade_tool uf <Firmware_Image>.img
```

Example:

```bash
sudo ./upgrade_tool uf V1.0_vicharak_axon-6.1-04032025-ubuntu-noble-emmc.img
```

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

:::{note}
Upon completion of the flashing process, the board will automatically reboot twice to install essential packages and apply necessary changes.
Please allow a few minutes for the process to finalize.
:::

:::{tip}
For more guidance, Watch Tutorial video on [How To Flash Image in eMMC ?](https://www.youtube.com/watch?v=O40fGwKvf_c&ab_channel=Vicharak)
:::

### To Erase the flash

```bash
sudo ./upgrade_tool ef <Firmware_Image>
```

Example:

```bash
sudo ./upgrade_tool ef V1.0_vicharak_axon-6.1-04032025-ubuntu-noble-emmc.img
```

:::{warning}
Firmware Image should be the same image which you have flashed in Axon eMMC. 
:::

::::

[comment]: < :::{seealso} >
[comment]: < [axon Linux starting guide](linux-start-guide.md) >
[comment]: < [Frequently Asked Questions](../../faq.rst) >
[comment]: < ::: >
