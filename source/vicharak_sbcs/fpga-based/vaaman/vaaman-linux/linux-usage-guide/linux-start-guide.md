(linux-start-guide)=

# Vicharak Linux Start Guide

Vicharak Provides multiple linux distributions for Vaaman SBC such as Debian, Ubuntu, Armbian, etc.
This guide will help you to get started with Vicharak linux systems.

## System Management

### Set host name and password

:::{note}
**If you have installed Vicharak Debian or Ubuntu system from the official website,
the default account name and password is:**

username: vicharak

password: 12345
:::

### Vicharak Configuration Tool

Vicharak linux systems includes **vicharak-config** tool which is purely written
using shell scripts that allows users to configure and setup their linux system configuration.

It provides a **TUI** interface to configure different linux specific configurations.
Use `sudo vicharak-config` to get started.

It is supported on all Debian based systems such as Debian buster/bullseye,
Ubuntu focal/jammy and other third party systems such as Armbian.

:::{admonition} Refer to
:class: tip
[**Vicharak config tool guide**](#vicharak-config-tool) for more detailed information.
:::

### Set up automatic Wi-Fi connection on boot

In the following example, we will set up automatic Wi-Fi connection on boot for the
**wlan0** interface. This will be useful if you are using a headless system. That means
you will not need to connect a monitor, keyboard, or mouse to your system to connect to Wi-Fi.

**1. Edit the `/userdata/before.txt` file and add the following lines:**

```text
connect_wi-fi <network name> <password>
```

Example:

```text
connect_wi-fi my-wifi-network my-wifi-password
```

**2. Reboot the system.**

---

## Debugging

(linux-uart-serial-console)=

### UART Serial Console

:::{admonition} Windows users refer to
Getting Started with Vaaman [**UART Serial Console**](../../getting-started.rst#using-serial-console)
:::

#### Preparation

To access Vaaman SBC through the serial interface, A USB to UART serial cable or adapter is required.

[Get arduino compatible FTDI from here](https://amzn.eu/d/hctdJnp)

#### Hardware Setup

1. Connect the USB to UART serial cable or adapter to your computer.

2. Connect the serial cable or adapter to the Vaaman SBC.

:::{list-table}
:widths: 20 40 130
:header-rows: 1

-
  - **Serial FTDI Pin**
  - **Header GPIO Pin**
  - **Schematic Name**
-
  - GND
  - Pin 6
  - GND
-
  - TX
  - Pin 8 (GPIO4_C4)
  - UART2DBG_TX
-
  - RX
  - Pin 10 (GPIO4_C3)
  - UART2DBG_RX

:::

:::{image} ../../../../_static/images/rk3399-vaaman/vaaman-serial-uart-pins.webp
:width: 50%
:::

(minicom-guide)=

#### Serial Console Programs

:::{note}
The baud rate for Vaaman is 1500000
:::

:::::{tab-set}

::::{tab-item} GTK-Term (GUI)

#### Install GTK-Term

You can install GTK-Term by executing the following command:

|       Debian/Ubuntu        |           Fedora           |        Arch Linux        |
| :------------------------: | :------------------------: | :----------------------: |
|     `sudo apt update`      |     `sudo dnf update`      |    `sudo pacman -Syu`    |
| `sudo apt install gtkterm` | `sudo dnf install gtkterm` | `sudo pacman -S gtkterm` |

#### Setting up GTK-Term

Run **GTK-Term** by executing the following command:

```bash
sudo gtkterm
```

#### Configure GTK-Term

To access the configuration settings for GTK-Term,
you can follow either of these methods:

Click on the **Configuration** menu and select **Port**.

OR

Press **Ctrl+Shift+S**.

By using either of these methods, you will be able to access the configuration settings in GTK-Term,
where you can make adjustments to the port settings for your serial connection, as shown in the image below:

:::{image} ../../../../_static/images/gtkterm-configuration.webp
:width: 50%
:::

:::{note}
Ensure that the cable is properly connected to the appropriate serial port on both devices.
:::

::::

::::{tab-item} Minicom (CLI)
:selected: true

#### Install Minicom

For Linux we will use Minicom. Install it with:

```bash
sudo apt install minicom
```

For other Linux distributions, please refer to the following table for the equivalent package names.

|       Debian/Ubuntu        |           Fedora           |        Arch Linux        |
| :------------------------: | :------------------------: | :----------------------: |
|     `sudo apt update`      |     `sudo dnf update`      |    `sudo pacman -Syu`    |
| `sudo apt install minicom` | `sudo dnf install minicom` | `sudo pacman -S minicom` |

#### Setting up Minicom

- Connect the USB to UART converter to your computer and run the following command to find the port name:

```bash
sudo minicom -s
```

**Select `Serial port setup` and press Enter.**

```text
+-----[configuration]------+
| Filenames and paths      |
| File transfer protocols  |
| **Serial port setup**    |
| Modem and dialing        |
| Screen and keyboard      |
| Save setup as dfl        |
| Save setup as..          |
| Exit                     |
| Exit from Minicom        |
+--------------------------+
```

**Change the port name to the one you found in the previous step.**

For example, if the port name is `/dev/modem`, then change it to `/dev/ttyUSB0`.

```text
+-----------------------------------------------------------------------+
| A -    Serial Device      : /dev/ttyUSB0                              |
| B - Lockfile Location     : /var/lock                                 |
| C -   Callin Program      :                                           |
| D -  Callout Program      :                                           |
| E -    Bps/Par/Bits       : 115200 8N1                                |
| F - Hardware Flow Control : Yes                                       |
| G - Software Flow Control : No                                        |
|                                                                       |
|    Change which setting?                                              |
+-----------------------------------------------------------------------+
        | Screen and keyboard      |
        | Save setup as dfl        |
        | Save setup as..          |
        | Exit                     |
        | Exit from Minicom        |
        +--------------------------+
```

**Configure baud rate of serial console according to your USB-UART converter.**

Configure and Press **Enter** to save the settings.

```text
+-----------------+---------[Comm Parameters]----------+----------------+
| A -    Serial De|                                    |                |
| B - Lockfile Loc|     Current: 1500000 8N1           |                |
| C -   Callin Pro| Speed            Parity      Data  |                |
| D -  Callout Pro| A: <next>        L: None     S: 5  |                |
| E -    Bps/Par/B| B: <prev>        M: Even     T: 6  |                |
| F - Hardware Flo| C:   9600        N: Odd      U: 7  |                |
| G - Software Flo| D:  38400        O: Mark     V: 8  |                |
|                 | E: 115200        P: Space          |                |
|    Change which |                                    |                |
+-----------------| Stopbits                           |----------------+
        | Screen a| W: 1             Q: 8-N-1          |
        | Save set| X: 2             R: 7-E-1          |
        | Save set|                                    |
        | Exit    |                                    |
        | Exit fro| Choice, or <Enter> to exit?        |
        +---------+------------------------------------+
```

**Select `Save setup as dfl` and press Enter.**

```text
+-----[configuration]------+
| Filenames and paths      |
| File transfer protocols  |
| Serial port setup        |
| Modem and dialing        |
| Screen and keyboard      |
| **Save setup as dfl**    |
| Save setup as..          |
| Exit                     |
| Exit from Minicom        |
+--------------------------+
```

**Save the settings as a different profile**

If you want to save the settings as a different profile, select Save setup as.. and press Enter.

```text
+-----[configuration]------+
| Filenames and paths      |
| File transfer protocols  |
| Serial port setup        |
| Modem and dialing        |
| Screen and keyboard      |
| Save setup as dfl        |
| **Save setup as..**      |
| Exit                     |
| Exit from Minicom        |
+--------------------------+
```

**Select `Exit` and press Enter**

```text
+-----[configuration]------+
| Filenames and paths      |
| File transfer protocols  |
| Serial port setup        |
| Modem and dialing        |
| Screen and keyboard      |
| Save setup as dfl        |
| Save setup as..          |
| **Exit**                 |
| Exit from Minicom        |
+--------------------------+
```

On successful configuration, you will see the following screen:

```text
Welcome to minicom 2.8
OPTIONS: I18n
Compiled on Jan  9 2021, 12:42:45.
Port /dev/ttyUSB0, 16:33:28
Press CTRL-A Z for help on special keys
```

**To exit Minicom, press `Ctrl-A` followed by `X`.**

:::{admonition} Alternatives to Minicom

- [**PuTTY**](https://www.putty.org/)

- [**Tera Term**](https://osdn.net/projects/ttssh2/releases/)

- [**GTK-Term**](https://github.com/Jeija/gtkterm)
  :::

::::
:::::

## SSH Tutorial

:::{admonition} Windows users refer to
Getting Started with Vaaman [**Using SSH**](../../getting-started.rst#using-ssh)
:::

### SSH Client installation

This guide will cover the installation of default `openssh-server`.

|           Debian/Ubuntu           |              Fedora               |        Arch Linux        |
| :-------------------------------: | :-------------------------------: | :----------------------: |
|         `sudo apt update`         |         `sudo dnf update`         |    `sudo pacman -Syu`    |
| `sudo apt install openssh-client` | `sudo dnf install openssh-client` | `sudo pacman -S openssh` |

### SSH Server installation

|           Debian/Ubuntu           |              Fedora               |        Arch Linux        |
| :-------------------------------: | :-------------------------------: | :----------------------: |
|         `sudo apt update`         |         `sudo dnf update`         |    `sudo pacman -Syu`    |
| `sudo apt install openssh-server` | `sudo dnf install openssh-server` | `sudo pacman -S openssh` |

### SSH Server Configuration

**Enable SSH service to start on boot**

```bash
sudo systemctl enable ssh
```

**Start SSH service**

```bash
sudo systemctl start ssh
```

**Check SSH service status**

```bash
sudo systemctl status ssh
```

:::{note}
If it is active and running, you should see a **active (running)** message.
:::

**Check SSH service port**

```bash
sudo netstat -tulpn | grep ssh
```

**Avahi-daemon installation and configuration**

You can install **Avahi-daemon** using the following commands:

|          Debian/Ubuntu          |             Fedora              |       Arch Linux       |
| :-----------------------------: | :-----------------------------: | :--------------------: |
|        `sudo apt update`        |        `sudo dnf update`        |   `sudo pacman -Syu`   |
| `sudo apt install avahi-daemon` | `sudo dnf install avahi-daemon` | `sudo pacman -S avahi` |

After the installation, **Avahi-daemon** should start automatically.
If it does not, you can start it manually by running:

```bash
sudo systemctl start avahi-daemon
```

**Verify its status by running:**

```bash
sudo systemctl status avahi-daemon
```

**Access Vaaman SBC through SSH**

**you can use either of the following commands:**

> SSH using the IP address

```bash
ssh username@ip_address
```

:::{tip}
Replace **"username"** with the appropriate username for Vaaman and **"ip_address"** with the
actual IP address assigned to Vaaman on the network.
:::

> SSH using the PC name (hostname)

```bash
ssh username@pc-name.local
```

:::{tip}
Replace **"username"** with the appropriate username for Vaaman and **"pc-name"** with the
actual PC name assigned to Vaaman on the network.
:::

:::{warning}
To get access of ``root`` user through SSH, User need to do configuration in SSH manually.
:::

:::{seealso}
[Flash individual images with Linux_Upgrade_Tool](#rockchip-upgrade-tool-misc)

[Frequently Asked Questions](#faq)
:::
