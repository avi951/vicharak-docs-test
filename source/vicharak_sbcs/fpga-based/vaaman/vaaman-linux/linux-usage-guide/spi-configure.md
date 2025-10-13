# How to configure SPI Flash from Linux userspace

**Vicharak Vaaman** contains a shared SPI flash between **Processor** and **FPGA**.
The SPI Flash needs to be configured to use FPGA.

Make sure you are using Vicharak's kernel and system image. Otherwise this guide will
not follow for you.

## Flashing to SPI Flash

For flashing to SPI flash, Vicharak has modified a utility called `flashcp`.

`sudo flashcp <hexfile>.hex`

## Configuring FPGA to use SPI Flash

For configuring FPGA to use SPI Flash use the following command:

`sudo read_from_flash`
