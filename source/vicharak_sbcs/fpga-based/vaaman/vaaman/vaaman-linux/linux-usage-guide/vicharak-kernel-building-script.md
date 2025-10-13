# Vicharak kernel building script

## Introduction to Vicharak kernel building script

:::{admonition} Vicharak kernel build script usage
:class: info

```text
    ─────────────────────────────────────────────────────────────────────
              Vicharak Kernel Build Script - Usage Guide
    ─────────────────────────────────────────────────────────────────────
     Usage: ./vicharak/build.sh [OPTIONS]

     Available Options:
      lunch            | -l    : Prepare the environment for the chosen device
      info             | -i    : Display current kernel setup details
      clean            | -c    : Remove kernel build artifacts
      kernel           | -k    : Compile the Linux kernel image
      kerneldeb        | -K    : Generate a Debian package for the Linux kernel
      update_defconfig | -u    : Update the kernel configuration with the latest changes
      help             | -h    : Display this usage guide
    ─────────────────────────────────────────────────────────────────────
```

:::

Vicharak kernel build script is a collection of scripts written in bash that
makes it easy for users to compile the kernel based on their specific needs.
It offers a set of customization options that can be adjusted as desired.

For example, users can choose whether to use clang or GCC as the compiler for
the kernel compilation, choose between multiple devices, choose the specific
version of the toolchain, select your own toolchain. They can also decide
whether to include the building of kernel modules or not.
This script gives users the flexibility to customize the kernel compilation
process according to their preferences and requirements.

:::{dropdown} Example configuration for Vicharak RK3399 Vaaman

````text
# shellcheck shell=bash
# SPDX-License-Identifier: MIT
# Copyright (C) 2023 Utsav Balar
# Copyright (C) 2023 Vicharak Computers LLP

# Makefile for rk3399_vaaman
# This file contains variables used for building rk3399_vaaman kernel
# To disable build options, comment the line or set it to false

# Device specific
DEVICE_NAME="rk3399_vaaman"
DEVICE_DTB_FILE="rk3399-vaaman-linux"
DEVICE_DEFCONFIG="rockchip_linux_defconfig"
DEVICE_CONFIG_FRAGMENT="rk3399_vaaman.config"
DEVICE_ARCH="arm64"
DEVICE_KERNEL_IMAGE_FILE="${OUT_DIR}/arch/${DEVICE_ARCH}/boot/Image"
DEVICE_DTB_DIR="${OUT_DIR}/arch/${DEVICE_ARCH}/boot/dts/rockchip"

# Build options
# To build kernel with performance configuration
PERF_BUILD=false

# To build kernel with clang
CLANG_BUILD=true

# Build modules along with kernel
MODULES_BUILD=true

# Build debian package
DEB_BUILD=true

# Pack kernel image using extlinux
PACK_KERNEL_BUILD=true

# Device specific clang version
DEVICE_CLANG_VERSION="17"

:::

:::{admonition} Fact
:class: info
This script automates the process of getting the compatible toolchain to
compile the kernel.
:::

**lunch**
: Allows to select the specific device configuration.
For example:
:::{card} ./vicharak/build.sh lunch

```text
    Processing option: lunch
----------------------------------------------------------------
1) galactos_ubuntu.mk
2) rk3399_vaaman.mk
3) rk3588_axon.mk
4) rk3588_axon_mainline.mk
Select device: 2
````

:::

**info**
: Displays the current kernel setup information.

:::{card} ./vicharak/build.sh info

````text
    Processing option: info
----------------------------------------------------------------
    Device Information
----------------------------------------------------------------
    Device Makefile:
    Device Name: rk3399_vaaman
    Device Defconfig: rockchip_linux_defconfig
    Device Config Fragment: rk3399_vaaman.config
    Device DTB: rk3399-vaaman-linux
    Device Compiler: Clang
    Build kernel modules: Yes
    Build Debian package: Yes
    ─────────────────────────────────────────────────────────────────────
              Vicharak Kernel Build Script - Usage Guide
    ─────────────────────────────────────────────────────────────────────
     Usage: ./vicharak/build.sh [OPTIONS]

     Available Options:
      lunch            | -l    : Prepare the environment for the chosen device
      info             | -i    : Display current kernel setup details
      clean            | -c    : Remove kernel build artifacts
      kernel           | -k    : Compile the Linux kernel image
      kerneldeb        | -K    : Generate a Debian package for the Linux kernel
      update_defconfig | -u    : Update the kernel configuration with the latest changes
      help             | -h    : Display this usage guide
    ─────────────────────────────────────────────────────────────────────```
:::

**clean**
: Cleans up the kernel build files.

:::{card} ./vicharak/build.sh clean

:::{dropdown} Click here to see the output
```text
    Processing option: clean
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang toolchain: 17
----------------------------------------------------------------
make[1]: Entering directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
  CLEAN   arch/arm64/crypto
  CLEAN   arch/arm64/kernel/vdso
  CLEAN   certs
  CLEAN   lib/raid6
  CLEAN   lib
  CLEAN   fs/unicode
  CLEAN   security/apparmor
  CLEAN   arch/arm64/kernel/vdso32
  CLEAN   arch/arm64/kernel
  CLEAN   drivers/misc/lkdtm
  CLEAN   security/selinux
  CLEAN   kernel
  CLEAN   arch/arm64/boot
  CLEAN   usr/include
  CLEAN   drivers/firmware/efi/libstub
  CLEAN   net/wireless
  CLEAN   drivers/tty/vt
  CLEAN   usr
  CLEAN   drivers/video/logo
  CLEAN   drivers/scsi
rm -f ./crypto/fips140.ko.rela.*
  CLEAN   vmlinux.symvers modules-only.symvers modules.builtin modules.builtin.modinfo
make[1]: Leaving directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
make[1]: Entering directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
rm -f ./crypto/fips140.ko.rela.*
  CLEAN   scripts/basic
  CLEAN   scripts/dtc
  CLEAN   scripts/kconfig
  CLEAN   scripts/mod
  CLEAN   scripts/selinux/genheaders
  CLEAN   scripts/selinux/mdp
  CLEAN   scripts
  CLEAN   include/config include/generated arch/arm64/include/generated debian .config .config.old .version Module.symvers
make[1]: Leaving directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
````

:::

(build-linux-kernel-image)=

:::

**kernel**
: Builds the linux kernel image.

:::{card} ./vicharak/build.sh kernel

```text
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang: 17
----------------------------------------------------------------
							...
							...
							...
----------------------------------------------------------------
    Build successful!
----------------------------------------------------------------
```

:::

**dtbs**
: Builds the linux dtbs.

:::{card} ./vicharak/build.sh dtbs

```text
    Processing option: dtbs
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang toolchain: 17
----------------------------------------------------------------
make[1]: Entering directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
  UPD     include/config/kernel.release
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-cdn-dp.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-camera-imx219.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-camera-ov5647.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-dsi-waveshare.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-dwc3-0-host.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-dwc3-0-otg.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-fpga-communication.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-i2c2.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-i2c6.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-pwm0.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-pwm1.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-spdif-pin15.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-spdif-pin32.dtbo
  DTCO     arch/arm64/boot/dts/rockchip/overlays/rk3399-vaaman-spi2-jedec-flash.dtbo
make[1]: Leaving directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
```

:::

(build-linux-kernel-debian-package)=

**kerneldeb**
: Builds the linux kernel debian package.

:::{card} ./vicharak/build.sh kerneldeb

```text
    Processing option: kerneldeb
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang toolchain: 17
----------------------------------------------------------------
make[1]: Entering directory '/home/vicharak/vicharak/kernel_rockchip_linux_vicharak/out'
  UPD     include/config/kernel.release
sh ../scripts/package/mkdebian
dpkg-buildpackage -r"fakeroot -u" -a$(cat debian/arch)  -b -nc -uc
dpkg-buildpackage: info: source package linux-5.10.160-vaaman
dpkg-buildpackage: info: source version 20231123-vaaman
dpkg-buildpackage: info: source distribution focal
dpkg-buildpackage: info: source changed by UtsavBalar1231 <utsavbalar1231@gmail.com>
dpkg-architecture: warning: specified GNU system type aarch64-linux-gnu does not match CC system type x86_64-unknown-linux-gnu, try setting a correct CC environment variable
dpkg-buildpackage: info: host architecture arm64
 dpkg-source --before-build .
 debian/rules binary
make KERNELRELEASE=5.10.160-vaaman ARCH=arm64 	KBUILD_BUILD_VERSION=vaaman -f ../Makefile
							...
							...
							...
 dpkg-genbuildinfo --build=binary
 dpkg-genchanges --build=binary >../linux-5.10.160-vaaman_20231123-vaaman_arm64.changes
dpkg-genchanges: info: binary-only upload (no source code included)
 dpkg-source --after-build .
dpkg-buildpackage: info: binary-only upload (no source included)
```

:::

**update_defconfig**
: Updates defconfig with latest changes.

:::{card} ./vicharak/build.sh update_defconfig

```text
    Processing option: update_defconfig
----------------------------------------------------------------
    Building with Clang
----------------------------------------------------------------
----------------------------------------------------------------
    Using standalone clang toolchain: 17
----------------------------------------------------------------
							...
							...
							...
----------------------------------------------------------------
    Updated rockchip_linux_defconfig with savedefconfig
----------------------------------------------------------------
```

:::

**help**
: Displays the help menu.

:::{card} ./vicharak/build.sh help

```text
└─[󰄛] ./vicharak/build.sh help
    ─────────────────────────────────────────────────────────────────────
              Vicharak Kernel Build Script - Usage Guide
    ─────────────────────────────────────────────────────────────────────
     Usage: ./vicharak/build.sh [OPTIONS]

     Available Options:
      lunch            | -l    : Prepare the environment for the chosen device
      info             | -i    : Display current kernel setup details
      clean            | -c    : Remove kernel build artifacts
      kernel           | -k    : Compile the Linux kernel image
      kerneldeb        | -K    : Generate a Debian package for the Linux kernel
      update_defconfig | -u    : Update the kernel configuration with the latest changes
      help             | -h    : Display this usage guide
    ─────────────────────────────────────────────────────────────────────
```

:::

:::{important}

If you face any problems with the build script, please [open an issue on GitHub](https://github.com/vicharak-in/kernel_build_scripts/issues/new)

:::

:::{seealso}

[Flash Rockchip images using Linux_Upgrade_Tool](#rockchip-upgrade-tool-misc)

[Frequently Asked Questions](#faq)

:::
