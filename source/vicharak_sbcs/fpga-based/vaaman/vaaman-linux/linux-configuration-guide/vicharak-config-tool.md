(vicharak-config-tool)=

# Vicharak Linux Configuration Tool

:::{admonition} **Fact**
:class: tip
vicharak-config also has a systemd service that is use configure system
prior to system boot and after the system boots.
:::

:::{admonition} **Vicharak Config TUI**

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Please select an option below:                                                             │
│                                                                                            │
│                                    System Maintaince                                       │
│                                    Hardware                                                │
│                                    Overlays                                                │
│                                    Connectivity                                            │
│                                    Advanced Options                                        │
│                                    User Settings                                           │
│                                    Localization                                            │
│                                    About                                                   │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

```{note}
The above menu might be shown differently depending on the terminal style.
```

:::

## How to navigate around vicharak-config

- Use **UP** or **DOWN** key to move the selection across available options.
- Use **RIGHT** or **LEFT** key to move `in` or `out` of the options menu and also,
  allows you to select **<Ok>** or **<Cancel>** option.
- Alternatively, you can also use **TAB** key to switch between them.
- **Enter** key is used to confirm the corresponding option.
- **ESC** key is used to do back to previous menu.

(vicharak-config-available-features)=

## Available Features

- [System maintenance](#vicharak-config-system-maintenance)
  : Update system packages.

- [Hardware configuration](#vicharak-config-hardware)
  : Capture Camera stream, Enable LEDs, Change thermal governor, DSI mirroring
  and 40-Pin header status.

- [Overlays](#vicharak-config-overlays)
  : Enable/Disable DTBO overlays, Build third-party DTBO, Reset Overlays to default.

- [Connectivity](#vicharak-config-connectivity)
  : Configure network using **nmtui**.

- [Advanced Options](#vicharak-config-advanced-options)
  : Install `Mali GPU` library and enable `OpenGL` emulation support.

- [User Settings](#vicharak-config-user-settings)
  : Change system password and hostname

- [Localization](#vicharak-config-localization)
  : Change Time-Zone/Locale/Keyboard and Wi-Fi Country

(vicharak-config-system-maintenance)=

### System Maintenance

This feature allows you to update the packages and bootloader.

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Please select an option below:                                                             │
│                                                                                            │
│                                    **System Maintaince**                                   │
│                                    Hardware                                                │
│                                    Overlays                                                │
│                                    Connectivity                                            │
│                                    Advanced Options                                        │
│                                    User Settings                                           │
│                                    Localization                                            │
│                                    About                                                   │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### System Update

This option allows you to update the firmware packages that are installed on the
system. It uses `apt-get` to update these packages to their latest versions.

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ System Maintaince                                                                          │
│                                                                                            │
│                                      **System Update**                                     │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

(vicharak-config-hardware)=

### Hardware

This feature allows you to configure different hardware options.

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Please select an option below:                                                             │
│                                                                                            │
│                                    System Maintaince                                       │
│                                    **Hardware**                                            │
│                                    Overlays                                                │
│                                    Connectivity                                            │
│                                    Advanced Options                                        │
│                                    User Settings                                           │
│                                    Localization                                            │
│                                    About                                                   │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Video capture devices

This option allows you to capture the camera frame using `v4l2-ctl`.
It uses `v4l2-ctl` to capture the camera frame.

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Manage on-board hardware                                                                   │
│                                                                                            │
│                             **Video capture devices**                                      │
│                             GPIO LEDs                                                      │
│                             Thermal governor                                               │
│                             Configure DSI display mirroring                                │
│                             40-pin GPIO                                                    │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### GPIO LEDs

This option allows you to enable/disable the LEDs. It changes the leds
triggers by echoing the specific trigger to the LED sysfs.

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Manage on-board hardware                                                                   │
│                                                                                            │
│                             Video capture devices                                          │
│                             **GPIO LEDs**                                                  │
│                             Thermal governor                                               │
│                             Configure DSI display mirroring                                │
│                             40-pin GPIO                                                    │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

- Select any LED to enable/disable/modify its trigger

┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Below are the available LEDs and their triggers.                                           │
│ Select any to update their trigger.                                                        │
│                                                                                            │
│    [*] :power [default-on]                                                                 │
│    [ ] :status [heartbeat]                                                                 │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

- Select the LED trigger from the list of available LED triggers.

┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Please select the new trigger:                                                             │
│                                                                                            │
│    ( ) kbd-shiftllock                                                                      │
│    ( ) kbd-shiftrlock                                                                  ▒   │
│    ( ) kbd-ctrlllock                                                                       │
│    ( ) kbd-ctrlrlock                                                                   ▒   │
│    ( ) mmc2                                                                            ▒   │
│    ( ) timer                                                                           ▒   │
│    ( ) oneshot                                                                         ▒   │
│    (*) disk-activity                                                                   ▒   │
│    ( ) disk-read                                                                       ▒   │
│    ( ) disk-write                                                                          │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

- Upon succesful completion, LED trigger will be updated.

┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│                                                                                            │
│ LED trigger has been updated.                                                              │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                           <Ok>                                             │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Change thermal governor

This option allows you to change the thermal governor. It changes thermal
governor by echoing to the specific sysfs.

```text
- Select thermal governor

┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Please select the thermal governor.                                                        │
│ Recommendation: fanless or DC fan => power_allocator | PWM fan => step_wise                │
│                                                                                            │
│    ( ) power_allocator                                                                     │
│    ( ) user_space                                                                          │
│    (*) step_wise                                                                           │
│    ( ) fair_share                                                                          │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

- Upon succesful completion, thermal governor will be updated.

┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│                                                                                            │
│ Thermal governor has been updated.                                                         │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                           <Ok>                                             │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### DSI mirroring

: This option allows you to enable/disable DSI mirroring. It uses
`vicharak-config` to enable/disable DSI mirroring.

#### 40-Pin GPIO header

This option allows you to enable/disable 40-pin GPIO header. Additionally,
it can be used to check the current state of the 40-pin GPIO header.

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│ Please select the test case:                                                               │
│                                                                                            │
│                                  Set all GPIO to High                                      │
│                                  Set all GPIO to Low                                       │
│                                  **Get all GPIO state**                                    │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                         <Ok>                             <Cancel>                          │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────┤ VICHARAK_CONFIG ├───────────────────────┐
│ Following is the current reading of all supported GPIO pins  │
│                                                              │
│                                                              │
│ 0: Low | 1: High | E: Error                                  │
│                                                              │
│ State  Pin  State                                            │
│        1 2                                                   │
│        3 4                                                   │
│        5 6                                                   │
│ 1      7 8      1                                            │
│        9 10     1                                            │
│ 0     11 12     0                                            │
│ 0     13 14                                                  │
│ 0     15 16     0                                            │
│       17 18     0                                            │
│       19 20                                                  │
│       21 22     0                                            │
│       23 24                                                  │
│       25 26                                                  │
│ 1     27 28     1                                            │
│ 1     29 30                                                  │
│ 1     31 32     1                                            │
│ 1     33 34                                                  │
│ 0     35 36     0                                            │
│ 0     37 38     0                                            │
│       39 40     0                                            │
│                                                              │
│       <Ok>                <Cancel>                           │
└──────────────────────────────────────────────────────────────┘
```

(vicharak-config-overlays)=

### Overlays

This feature allows you to configure different overlays options.

:::{warning}

```text
┌────────────────────────────────────┤ VICHARAK_CONFIG ├─────────────────────────────────────┐
│                                                                                            │
│ WARNING                                                                                    │
│                                                                                            │
│ Overlays, by its nature, require "hidden" knowledge about the running device tree.         │
│ While major breakage is unlikely, this does mean that after kernel update, the overlay may │
│ cease to work.                                                                             │
│                                                                                            │
│ If you accept the risk, select Yes to continue.                                            │
│ Otherwise, select No to go back to previous menu.                                          │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                                                                                            │
│                          <Yes>                             <No>                            │
│                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

:::

- Enable DTBO overlays
  : This option allows you to enable/disable the DTBO overlays. It uses
  `uboot-update` script installed inside rootfs to enable or disable the
  specific dtbo overlay from extlinux configuration.

- Build third-party DTBO
  : This option allows you to build the third-party DTBO. It builds and installs
  the dtbo using the `device-tree-compiler` utility.

(vicharak-config-connectivity)=

### Connectivity

This feature allows you to configure different connectivity options.

- Configure network
  : This option allows you to configure network using `nmtui`.

(vicharak-config-advanced-options)=

### Advanced Options

This feature allows you to configure different advanced options.

- Install GPU library
  : This option allows you to install Mali GPU library and enable OpenGL support.

  It uses `apt install` to install the mali library from `userdata` partition
  and enables the `gl4es` library support for converting OpenGL-ES context to OpenGL.

  :::{tip}
  Use `gl4es` prefix with your desired application to run that application with OpenGL.

  Example: `gl4es supertuxkart`
  :::

(vicharak-config-user-settings)=

### User Settings

This feature allows you to configure different user settings.

- Change system password
  : This option allows you to change the system password. It uses `passwd` to
  change the system password.

- Change hostname
  : This option allows you to change the system hostname. It uses `hostnamectl`
  to change the system hostname.

(vicharak-config-localization)=

### Localization

This feature allows you to configure different localization options.

- Change Time-Zone
  : This option allows you to change the system Time-Zone. It uses `timedatectl`
  to change the system Time-Zone.

- Change Locale
  : It will generate the new locale as per the selection.

---

### USB Tethering

The latest version of `vicharak-config` introduces **USB Tethering** support for seamless SSH access to your Vaaman via the **TYPE-C0** USB port. In addition to SSH access, the tethering interface can now **share internet from Ethernet to your host machine** over USB.

#### Key Features
- Plug-and-play SSH access via USB at a fixed IP (`10.42.0.1`)
- Share internet access over USB when the Vaaman is connected via Ethernet
- Service control via both TUI and systemd

#### Getting latest vicharak-config

USB-tethering can be enabled through latest update of vicharak-config. To get latest version of vichrak-config, run below commands:

:::{warning}
⚠️ **Type-C Mode Switching Issues:** The Type-C0 port may not reliably switch between host and device modes. Enabling this feature might interfere with other Type-C peripherals, such as USB pen drives. If issues occur, try replugging the device or switching to a different Type-C port.
:::

```bash
sudo apt update
sudo apt install vicharak-config
```

This feature is fully supported only on the latest Linux kernels. We recommend upgrading to the latest kernel version for proper functionality.

```bash
sudo apt update
sudo apt install u-boot-menu
sudo apt install linux-5.10.233-vaaman
sudo reboot
```

#### Accessing USB Tethering Controls

From the TUI (`vicharak-config` interface), go to:

```
> Advanced Options
	> USB Tethering
```

You can Enable/Disable USB Tethering.

#### Service Control via systemd

The service controlling USB tethering is:
```
advanced-usb@tethering.service
```

**Commands:**
- Stop the service:
  ```bash
  sudo systemctl stop advanced-usb@tethering.service
  ```
- Start the service:
  ```bash
  sudo systemctl start advanced-usb@tethering.service
  ```
- Disable autostart on boot:
  ```bash
  sudo systemctl disable advanced-usb@tethering.service
  ```
- Enable autostart on boot:
  ```bash
  sudo systemctl enable advanced-usb@tethering.service
  ```

#### SSH Access via USB
Once enabled, connect your host PC to the **TYPE-C0** port of the Vaaman and SSH directly:
```bash
ssh vicharak@10.42.0.1
```
This eliminates the need for serial console or IP discovery.

#### Internet Sharing over USB
If your Vaaman is connected to the internet via Ethernet, the host PC will also get internet access via the USB connection.

This is achieved using appropriate **IP forwarding and iptables NAT rules**, which are applied automatically by the `advanced-usb@tethering.service`.

#### Technical Details
- **IP Address:** Vaaman (USB device): `10.42.0.1`, Host (PC): typically `10.42.0.2`
- **iptables Rules:** Automatically configured to allow NAT routing from USB (`usb0`) to Ethernet (`eth0`)
- **IP Forwarding:** Automatically enabled during tethering
