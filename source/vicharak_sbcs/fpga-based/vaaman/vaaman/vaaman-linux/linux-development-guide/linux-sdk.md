# Linux SDK

Working with Vicharak computer boards is very easy as we provide all the
necessary source, tools and scripts required to build your own Linux systems.

## Build Linux SDK from source

The Vicharak Linux SDK is based on SDK provided by Rockchip hence, it follows
the conditions and criteria of Rockchip.

Vicharak provides multiple different sources for building your own Linux images.
Take a look at the table below:

:::{list-table}
:header-rows: 1
:class: feature-table

-
  - Linux distribution
  - Version

-
  - Debian
  - Bullseye (11)

-
  - Ubuntu
  - Focal (20.04)

-
  - Ubuntu
  - Jammy (22.04)

-
  - Yocto
  - Mickledore (4.2)

-
  - Buildroot
  - None

-
  - Android
  - 12.1

:::

These sources are available at [Vicharak GitHub](https://github.com/vicharak-in)

### Installing the package dependencies for environment setup

```{warning}
It is recommended to either use **Debian bullseye (11)** or
**Ubuntu focal (20.04)** to build the rootfs image.
```

#### Install source control tools

Building Vicharak linux systems requires both **Git** (For source code management)
and **Repo** (Google-built repository management tool).

Please take a look at [Android's source controls tools setup](https://source.android.com/docs/setup/download)
as we follow the same for building Vicharak's Linux systems.

#### Install package dependencies

:::{important}
Make sure you have properly installed `repo` tool before proceeding.
:::

**The following packages are required to build the rootfs image.**

```bash
sudo apt-get update -y

sudo apt install -y asciidoc autotools-dev bash bc binutils bison \
build-essential bzip2 chrpath cpio curl cvs dblatex default-jre \
device-tree-compiler diffstat expect-dev fakeroot file flex g++ gawk gcc \
gcc-aarch64-linux-gnu gcc-arm-linux-gnueabihf g+conf genext2fs git git-core \
git-gui gitk graphviz gzip intltool lib32stdc++6 libdrm-dev libglade2-dev \
libglib2.0-dev libgtk2.0-dev liblz4-tool libncurses5 libparse-yapp-perl \
libsigsegv2 libssl-dev libudev-dev libusb-1.0-0-dev m4 make mercurial mtools \
openssh-client parted patch patchutils perl python3 python-is-python3 \
qemu-user-static rsync sed subversion swig tar texinfo u-boot-tools unzip w3m \
wget
```

<!-- TODO: Fix when the issues section is available -->

:::{note}
The above packages might not be available to install on your system. Please
try to find the alternatives or solution from the internet.

If you still are unable to install the packages, please contact us through [issues section](#)
:::

### Getting the sources

We have structured our Linux development source code in the same way as the
official Android sources. i.e. we have various manifests with different
branches for different releases of our supported Linux distributions and products.
**repo** tool will take care of the source code syncing and updating.

Take a look at the following table to get the latest sources.

| Manifest         | Tag                 | URL                                                                                |
| ---------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Debian bullseye  | V1.0.2311.000       | https://github.com/vicharak-in/rockchip-linux-manifests/tree/master       |
| Ubuntu Focal     | V1.0.2311.000       | https://github.com/vicharak-in/rockchip-linux-manifests/tree/master       |
| Ubuntu Jammy     | V1.0.2311.000       | https://github.com/vicharak-in/rockchip-linux-manifests/tree/master       |
| Yocto Mickledore | V1.0.2311.000       | https://github.com/vicharak-in/rockchip-linux-manifests/tree/master       |
| Buildroot        | V1.0.2311.000       | https://github.com/vicharak-in/rockchip-linux-manifests/tree/master       |
| Android 12.1     | android-12.1-v1.0.0 | https://github.com/vicharak-in/rockchip-linux-manifests/tree/android-12.1 |

#### Cloning the source

To clone the latest sources, use the following command.

::::{tab-set}

:::{tab-item} Debian bullseye (11)

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b master
```

:::

:::{tab-item} Ubuntu Focal (20.04)

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b master
```

:::

:::{tab-item} Ubuntu Jammy (22.04)

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b master
```

:::

:::{tab-item} Yocto Mickledore (4.2)

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b master
```

:::

:::{tab-item} Buildroot

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b master
```

:::

:::{tab-item} Android 12.1

```bash
repo init --no-tags --no-clone-bundle -u https://github.com/vicharak-in/rockchip-linux-manifests -b android-12.1 -m rk3399-vaaman.xml
```

<!-- TODO: Fix when Android manifest is available -->

:::

::::

:::{tip}
You can also shallow clone entire SDK using `--depth=1` option.
Use the following command to sync the source with shallow history:

```bash
repo init --depth=1 --no-tags --no-clone-bundle -u <url> -b <branch> -m <manifest>
```

:::

#### Syncing the source

To download the code sources from the repositories to your local machine, use the following command.

```bash
repo sync -j$(nproc)
```

### Building the Linux SDK

::::{tab-set}

:::{tab-item} Ubuntu Focal (20.04)
:selected:

After successful syncing of the source, you are now ready to build the Linux SDK.

Enter the SDK source directory, and confirm that your have a `build.sh` file in the current directory.

#### Source the Ubuntu configuration file

The configuration file for Ubuntu Focal (20.04) is located at `device/rockchip/rk3399/vicharak-vaaman-ubuntu.mk`

```bash
./build.sh device/rockchip/rk3399/vicharak-vaaman-ubuntu.mk
```

To ensure successful configuration, the `device/rockchip/.BoardConfig.mk` will
be linked to the effective configuration file. It is recommended to verify
the file to confirm the success of the configuration.

Please note that `rk3399-vaaman-ubuntu.mk` is the configuration file created by
Vicharak for reference. Users can also create their own new configuration files
based on this reference to customize the firmware according to their requirements.

````{admonition} Important configuration details:
:class: tip

(If you intend to create your own firmware, you might need to modify the
following configuration information.)

#### Compile the uboot configuration file

```bash
# U-boot defconfig
export RK_UBOOT_DEFCONFIG=rk3399-vaaman
```

#### Compile the kernel configuration file

```bash
# Kernel defconfig
export RK_KERNEL_DEFCONFIG=rockchip_linux_defconfig
```

#### Compile the kernel DTS used by kernel

```bash
# Kernel DTS
export RK_KERNEL_DTS=rk3399-vaaman-linux
```

#### Partitioning information (very important)

```bash
# parameter for GPT table
export RK_PARAMETER=parameter-vaaman-debian.txt
```

#### Package file for generting eMMC update image

```bash
# packagefile for make update image
export RK_PACKAGE_FILE=rk3399-ubuntu-package-file
```

```bash
# Rootfs linux distribution
export RK_ROOTFS_SYSTEM=ubuntu
```

```bash
# Ubuntu version (focal or jammy)
export RK_UBUNTU_VERSION=focal
```

```bash
# Default desktop environment for Ubuntu (xfce, gnome, mate, base)
export UBUNTU_FLAVOR=xfce
```

```bash
# rootfs image path
export RK_ROOTFS_IMG=ubuntu/ubuntu-focal.img
```

```bash
# DTBO overlays to enable on boot
export VICHARKA_BOOT_ENABLE_OVERLAYS=""
```
````

#### Building the Ubuntu firmware
\
After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh
```
\
The compiled firmware will be located in the `rockdev/pack` directory.

:::

:::{tab-item} Ubuntu Jammy (22.04)

After successful syncing of the source, you are now ready to build the Linux SDK.

Enter the sdk source directory, and confirm that your have a `build.sh` file in the current directory.

#### Source the Ubuntu configuration file

The configuration file for Ubuntu Jammy (22.04) is located at `device/rockchip/rk3399/vicharak-vaaman-ubuntu.mk`

Open the configuration file and change the `RK_UBUNTU_VERSION` to `jammy`

```bash
./build.sh device/rockchip/rk3399/vicharak-vaaman-ubuntu.mk
```

To ensure successful configuration, the `device/rockchip/.BoardConfig.mk` will
be linked to the effective configuration file. It is recommended to verify
the file to confirm the success of the configuration.

Please note that `rk3399-vaaman-ubuntu.mk` is the configuration file created by
Vicharak for reference. Users can also create their own new configuration files
based on this reference to customize the firmware according to their requirements.

````{admonition} Important configuration details:
:class: tip

(If you intend to create your own firmware, you might need to modify the
following configuration information.)

#### Compile the uboot configuration file

```bash
# U-boot defconfig
export RK_UBOOT_DEFCONFIG=rk3399-vaaman
```

#### Compile the kernel configuration file

```bash
# Kernel defconfig
export RK_KERNEL_DEFCONFIG=rockchip_linux_defconfig
```

#### Compile the kernel DTS used by kernel

```bash
# Kernel DTS
export RK_KERNEL_DTS=rk3399-vaaman-linux
```

#### Partitioning information (very important)

```bash
# parameter for GPT table
export RK_PARAMETER=parameter-vaaman-debian.txt
```

#### Package file for generting eMMC update image

```bash
# packagefile for make update image
export RK_PACKAGE_FILE=rk3399-ubuntu-package-file
```

```bash
# Rootfs linux distribution
export RK_ROOTFS_SYSTEM=ubuntu
```

```bash
# Ubuntu version (focal or jammy)
export RK_UBUNTU_VERSION=jammy
```

```bash
# Default desktop environment for Ubuntu (xfce, gnome, mate, base)
export UBUNTU_FLAVOR=xfce
```

```bash
# rootfs image path
export RK_ROOTFS_IMG=ubuntu/ubuntu-jammy.img
```

```bash
# DTBO overlays to enable on boot
export VICHARKA_BOOT_ENABLE_OVERLAYS=""
```
````

#### Building the Ubuntu firmware

After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh
```

The compiled firmware will be located in the `rockdev/pack` directory.

:::

:::{tab-item} Debian bullseye (11)

After successful syncing of the source, you are now ready to build the Linux SDK.

Enter the SDK source directory, and confirm that your have a `build.sh` file in the current directory.

#### Source the Debian configuration file

The configuration file for Vaaman Debian bullseye (11) is located at `device/rockchip/rk3399/vicharak-vaaman-debian.mk`

```bash
./build.sh device/rockchip/rk3399/vicharak-vaaman-debian.mk
```

To ensure successful configuration, the `device/rockchip/.BoardConfig.mk` will be linked to the effective configuration file.
It is recommended to verify the file to confirm the success of the configuration.

Please note that `rk3399-vaaman-debian.mk` is the configuration file created by
Vicharak for reference. Users can also create their own new configuration files
based on this reference to customize the firmware according to their requirements.

````{admonition} Important configuration details:
:class: tip

(If you intend to create your own firmware, you might need to modify the following configuration information.)

#### Compile the uboot configuration file

```bash
# U-boot defconfig
export RK_UBOOT_DEFCONFIG=rk3399-vaaman
```

#### Compile the kernel configuration file

```bash
# Kernel defconfig
export RK_KERNEL_DEFCONFIG=rockchip_linux_defconfig
```

#### Compile the kernel DTS used by kernel

```bash
# Kernel DTS
export RK_KERNEL_DTS=rk3399-vaaman-linux
```

#### Partitioning information (very important)

```bash
# parameter for GPT table
export RK_PARAMETER=parameter-vaaman-debian.txt
```

#### Package file for make update image

```bash
# packagefile for make update image
export RK_PACKAGE_FILE=rk3399-debian-package-file
```

```bash
# Rootfs linux distribution
export RK_ROOTFS_SYSTEM=debian
```

```bash
# Debian version (bullseye)
export RK_DEBIAN_VERSION=bullseye
```

```bash
# Default desktop environment for Debian (lxde, xfce, gnome, mate, base)
export DEBIAN_FLAVOR=lxde
```

```bash
# rootfs image path
export RK_ROOTFS_IMG=debian/linaro-rootfs.img
```

```bash
# DTBO overlays to enable on boot
export VICHARKA_BOOT_ENABLE_OVERLAYS=""
```
````

#### Building the Debian firmware

After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh
```

The compiled firmware will be located in the `rockdev/pack` directory.
:::

:::{tab-item} Buildroot

After successful syncing of the source, you are now ready to build the Linux SDK.

Enter the sdk source directory, and confirm that your have a `build.sh` file in the current directory.

### Source the Buildroot configuration file

The configuration file for Buildroot is located at `device/rockchip/rk3399/vicharak-vaaman-buildroot.mk`

```bash
./build.sh device/rockchip/rk3399/vicharak-vaaman-buildroot.mk
```

To ensure successful configuration, the `device/rockchip/.BoardConfig.mk` will
be linked to the effective configuration file. It is recommended to verify
the file to confirm the success of the configuration.

Please note that `rk3399-vaaman-buildroot.mk` is the configuration file created by
Vicharak for reference. Users can also create their own new configuration files
based on this reference to customize the firmware according to their requirements.

````{admonition} Important configuration details:
:class: tip

(If you intend to create your own firmware, you might need to modify the following configuration information.)

#### Compile the uboot configuration file

```bash
# U-boot defconfig
export RK_UBOOT_DEFCONFIG=rk3399-vaaman
```

#### Compile the kernel configuration file

```bash
# Kernel defconfig
export RK_KERNEL_DEFCONFIG=rockchip_linux_defconfig
```

#### Compile the kernel DTS used by kernel

```bash
# Kernel DTS
export RK_KERNEL_DTS=rk3399-vaaman-linux
```

#### Partitioning information (very important)

```bash
# parameter for GPT table
export RK_PARAMETER=parameter-vaaman-debian.txt
```

#### Package file for make update image

```bash
# packagefile for make update image
export RK_PACKAGE_FILE=rk3399-debian-package-file
```

```bash
# Rootfs linux distribution
export RK_ROOTFS_SYSTEM=buildroot
```

```bash
# rootfs image path
export RK_ROOTFS_IMG=buildroot/rootfs.img
```

```bash
# DTBO overlays to enable on boot
export VICHARKA_BOOT_ENABLE_OVERLAYS=""
```
````

#### Building the Buildroot firmware

After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh
```

The compiled firmware will be located in the `rockdev/pack` directory.

:::

:::{tab-item} Android 12.1

After successful syncing of the source, you are now ready to build the Linux SDK.

Enter the SDK source directory, and confirm that your have a `build.sh` file in the current directory.

### Source the Android 12.1 environment setup

```bash
source build/envsetup.sh
```

The device specific configuration file for Android 12.1 is located at `device/rockchip/rk3399/vaaman.mk`

#### Lunch the device configuration

```bash
lunch vaaman-userdebug
```

### Building the Android 12.1 firmware

After the configuration is complete, you can start compiling the firmware.

```bash
./build.sh -UACKup
```

```{note}
`build.sh` is the firmware build script that can be used to interactively build the firmware.
It can accept command line arguments to customize the build process.

- -U -> Build U-Boot
- -A -> Build Android
- -C -> Build kernel using clang compiler
- -K -> Build kernel
- -u -> Build rockchip update image
- -p -> Pack the firmware
```

After the firmware is compiled, you can find an `update.img` file inside `rockdev/pack`

:::

::::

### Partial compilation feature

:::{warning}
This feature is only supported on Vicharak Debian, Ubuntu and Buildroot systems.
:::

If you only need to compile a certain part of the firmware.
Use the following command to compile the corresponding part of the firmware.

#### Kernel

```bash
./build.sh kernel
```

:::{tip}
There are multiple ways to build kernel on Vicharak build system.

- Extlinux based boot image
  - `./build.sh extboot`

- Linux kernel as debian package
  - `./build.sh kerneldeb`

:::

#### U-boot

```bash
./build.sh uboot
```

#### Recovery

```bash
./build.sh recovery
```

#### Rootfs

```bash
./build.sh rootfs
```

## Packing the firmware

````{admonition} Important
:class: tip

Before packing the firmware, you need to make sure that the firmware has been compiled successfully.

```text
ls -l

├── boot.img -> ~/vicharak/linux_sdk/kernel/boot.img
├── idbloader.img -> ~/vicharak/linux_sdk/u-boot/idbloader.img
├── MiniLoaderAll.bin -> ~/vicharak/linux_sdk/u-boot/rk3399_loader_v1.20.130.bin
├── misc.img -> ~/vicharak/linux_sdk/device/rockchip/rockimg/wipe_all-misc.img
├── parameter.txt -> ~/vicharak/linux_sdk/device/rockchip/RK3399/parameter-ubuntu.txt
├── recovery.img -> ~/vicharak/linux_sdk/buildroot/output/rockchip_rk3399_recovery/images/recovery.img
├── rootfs.img -> ~/vicharak/linux_sdk/ubuntu/ubuntu-focal.img # or ubuntu-jammy.img or linaro-rootfs.img
├── trust.img -> ~/vicharak/linux_sdk/u-boot/trust.img
├── uboot.img -> ~/vicharak/linux_sdk/u-boot/uboot.img
└── userdata.img
```
````

After the firmware is compiled, you can use the following command to pack the firmware.

```bash
./mkfirmware.sh
```

(firmware-file-formats)=

:::{important}

## Understanding Firmware Formats

There are two primary types of firmware formats you'll encounter:

1. **Raw Firmware:**
   - **Description:** Raw Firmware is essentially a direct copy of your storage device, capturing every bit of data as is.
   - **Flashing Tools:**
     - _For SD Card:_
       - **GUI Tools:**
         - `SDCard Installer` (Linux/Windows/MacOS)
         - `Balena Etcher` (Linux/Windows/MacOS)
       - **CLI Tool:**
         - `dd` (Linux)
     - _For eMMC:_
       - **GUI Tool:**
         - `AndroidTool/RKDevTool` (Windows)
       - **CLI Tools:**
         - `upgrade_tool` (Linux/MacOS)
         - `rkdeveloptool` (Linux)

2. **RK Firmware:**
   - **Description:** RK Firmware comes in Rockchip's proprietary format. Specific tools provided by Rockchip are used to flash this firmware onto eMMC or SD Card.
   - **Flashing Tools:**
     - _For SD Card:_
       - **GUI Tool:**
         - `SD Firmware Tool` (Windows)
     - _For eMMC:_
       - **GUI Tool:**
         - `AndroidTool/RKDevTool` (Windows)
       - **CLI Tool:**
         - `upgrade_tool` (Linux)

**Partition Image:**

- **Description:** Partition Image refers to segmented images of different
  parts of the firmware, such as boot.img, kernel.img, and system.img.
  These components are assembled like pieces of a puzzle to form a complete Android system.

- **Usage:**
  - Place each specific image (e.g., kernel.img) into its corresponding
    partition on the SD card or eMMC to construct the complete Android system.

:::

### Pack the firmware into a single image

````{admonition} Important
:class: note

Please make sure that the `tools/linux/Linux_Pack_Firmware/rockdev/package-file` is the correct package file.

The partition information in the package file is very important.
If the partition information is incorrect, the firmware will not be able to boot normally.

The packed firmware image will be located in the `rockdev/pack/` directory.

##### Rockhip Pack Firmware Image (RK Firmware)

Rockchip provides a tool called `Linux_Pack_Firmware` to pack the firmware into a single image.
It uses Rockchip's own image format,
and can be used to flash the firmware to the eMMC of the development board or any SD-card using the tools provided by Rockchip.

```bash
./build.sh updateimg
```


```{seealso} Learn more about the Rockchip parameter.txt file\
[Rockchip parameter.txt](./rockchip-parameter-file.md)
```
````

---

### Vicharak RAW (GPT) Image (Raw Firmware)

Vicharak provides another method to pack the firmware into a single image.
This script uses the GPT image format, and can be used to flash the firmware to
any supported storage media (SD-Card, eMMC or NVMe) using the basic linux
utility such as `dd` or even using `Balena Etcher` tool.

```{seealso}
[How to use Balena Etcher](../../vaaman-sdcard-boot.rst)
```

```bash
./build.sh rawimg
```

```{admonition} More information
For more information about the `Linux_Pack_Firmware` tool or how to flash
firmware on to your board, please refer to the following link.\
[Rockchip Development Guide](../linux-usage-guide/rockchip-develop-guide.md)
```
