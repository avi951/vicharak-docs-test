##############
Wi-Fi
##############

Vicharak-Axon Mini comes with an integrated AMPAK **AP6276S** Wi‑Fi 6E (2.4 GHz / 5 GHz / 6 GHz) and Bluetooth 5.3 module. The antenna connects to the board via a U.FL connector (with onboard virtual antenna / RF switch support).

This document explains how to connect to a Wi-Fi network on a Linux system using command-line tools:

1. Check Wi-Fi Device Status
----------------------------

.. code-block:: bash

   sudo nmcli device status

Ensure that the wireless interface is listed and not marked as ``unavailable``.

2. Enable Wi-Fi
---------------

.. code-block:: bash

   sudo nmcli radio wifi on

3. Scan for Available Networks
------------------------------

.. code-block:: bash

   sudo nmcli device wifi list

4. Connect to the Wi-Fi Network
-------------------------------

.. code-block:: bash

   sudo nmcli device wifi connect "<SSID>" password "<WiFi-Password>"

Replace ``<SSID>`` with the name of the network and ``<WiFi-Password>`` with the password.

5. Check Connection
-------------------

.. code-block:: bash

   nmcli connection show --active

.. code-block:: bash

   ping -c 5 google.com


Troubleshooting
===============

- Use ``dmesg | grep wlan`` or ``journalctl -xe`` to inspect Wi-Fi-related logs.
- Ensure your Wi-Fi driver/module is loaded.

Recommendations
===============

- Use ``nmcli`` or ``nmtui`` for user-friendly configuration on most systems.
