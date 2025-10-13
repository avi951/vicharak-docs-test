(build-u-boot)=

# Updating U-Boot Version Using APT

:::{tip}
U-boot Version : 1.1.12
:::

## Getting U-Boot from APT Source

This section explains how to obtain U-Boot from APT sources and the additional features supported exclusively in these package builds.

### Features Exclusive to APT U-Boot Packages
- **HDMI Console & Bootmenu Support**: Users can access U-Boot logs, the console, and the bootmenu on a display connected with HDMI TX0.
- **Keyboard Shortcuts**:
  - To enter the U-Boot console, start pressing Ctrl + C continuously as soon as the vicharak logo appears on the screen. This will allow you to configure the boot process.
  - To enter the U-Boot bootmenu, start pressing Ctrl + Q continuously as soon as the Vicharak logo appears on the screen. This will allow you to choose the storage device to boot from and also enables the user to select the default boot target device for subsequent boots using Shift + D.

````markdown

    +------------------------------------------------------+
    |               U-Boot Boot Menu (Vicharak)            |
    +------------------------------------------------------+

      Select the boot target to load your OS:

      -> 1. EMMC BOOT
         2. NVME BOOT        <Default>
         3. USB BOOT
         4. SDCARD BOOT
         U-Boot console

      Hit any key to stop autoboot:  6
      Press UP/DOWN to move, ENTER to select
      Press SHIFT + D to set a default boot target

    +------------------------------------------------------+

````

- **UART Console**: Users can also access U-Boot logs via the UART interface. Refer to [this guide](https://docs.vicharak.in/vicharak_sbcs/axon/axon-getting-started/#using-serial-console) for instructions on setting up UART.

### Installation
If you need to obtain U-Boot using the APT package manager, you can do so by running:

```sh
sudo apt update
sudo apt install u-boot-rk3588-axon
```

### First Boot Behavior

When booting from a newly flashed storage device, Axon will perform an initial setup (first boot configuration) and then automatically reboot.

**Important:** After the reboot, Axon will not automatically boot from the same storage device unless it has been explicitly set as the default. Simply selecting the device once from the boot menu does not persist across reboots.

To ensure Axon boots from the same storage medium after first boot:

- Either **reselect** the storage device from the boot menu after reboot, or
- **Set it as the default** before the first boot using **Shift + D** in the boot menu, so it will be used automatically after reboot.

### Potential Issues & Troubleshooting
1. **Keyboard Disconnected During U-Boot**
   - Hot-plugging is not supported in U-boot. If the keyboard is removed while inside U-Boot it will not reconnect automatically. A system reboot is required to detect the keyboard again.
   - If the keyboard does not respond properly, it might be due to an unsupported keyboard. This issue is known and will be addressed in a future update.

2. **Boot console not appearing**
   - Ensure the correct key combination (**Ctrl + C**) is used during boot.
   - If the system boots too quickly, try pressing the key earlier.

## Summary of Features

| Feature                       | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| HDMI Console Support          | U-Boot interaction using HDMI and USB keyboard     |
| Multiple Boot Device Support  | Boot from USB, NVMe, SD Card, or eMMC              |
| Interactive Boot Menu         | Choose boot source during startup                  |
| Default Boot Source Selection | Configure persistent boot priority using Shift + D |
