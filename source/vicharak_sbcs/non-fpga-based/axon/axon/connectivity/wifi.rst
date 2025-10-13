##############
Wi-Fi
##############

.. image:: /_static/images/rk3588-axon/axon-wifi-bt.webp
   :width: 80%

Vicharak Axon comes with a 6252B-SR Integrated RTL8852BS WiFi6 2.4GHz/5GHz dual-band and Antenna is connected to the board via a U.FL connector. The antenna can support WiFi 2.4Ghz, 5GHz, 5.8Ghz antenna and is compatible with 802.11 b/g/n Wi-Fi.

.. image:: /_static/images/rk3588-axon/accessory-wifi-antenna.webp
   :width: 30%

.. danger:: 
    Kindly, attached Antenna on Wifi U.FL connector as mentioned in above picture.

This document explains how to connect to a Wi-Fi network on a Linux system using command-line tools. It covers the following methods:

- ``nmcli`` (NetworkManager CLI)
- ``nmtui`` (NetworkManager Text User Interface)

Prerequisites
=============

- A functional Wi-Fi interface (e.g., ``wlan0`` or ``wlp2s0``)
- Required tools installed:

  .. code-block::

    sudo apt update
    sudo apt-get install network-manager

  
  - For Method A & B: NetworkManager with ``nmcli`` and ``nmtui``

Method A: Using nmcli (NetworkManager)
======================================

1. Check Wi-Fi Device Status
----------------------------

.. code-block:: bash

   nmcli device status

Ensure that the wireless interface is listed and not marked as ``unavailable``.

2. Enable Wi-Fi
---------------

.. code-block:: bash

   nmcli radio wifi on

3. Scan for Available Networks
------------------------------

.. code-block:: bash

   nmcli device wifi list

4. Connect to the Wi-Fi Network
-------------------------------

.. code-block:: bash

   sudo nmcli device wifi connect "<SSID>" password "<WiFi-Password>"

Replace ``<SSID>`` with the name of the network and ``<WiFi-Password>`` with the password.

5. Check Connection
-------------------

.. code-block:: bash

   nmcli connection show --active

Method B: Using nmtui (Text User Interface)
===========================================

``nmtui`` provides a text-based user interface to configure network settings.

1. Start nmtui
--------------

.. code-block:: bash

   sudo nmtui

2. Select "Activate a connection"
---------------------------------

Use arrow keys to navigate and select the Wi-Fi network from the list.

3. Enter Password and Connect
-----------------------------

Once selected, input the Wi-Fi password if prompted and press Enter.

4. Verify the Connection
------------------------

.. code-block:: bash

   nmcli connection show --active

.. code-block:: bash

   ping -c 5 google.com


Use WiFi As Hotspot
====================

 Use `Hotspot Setup </vicharak_sbcs/axon/axon-os-configuration/wifi-hotspot>`_


Troubleshooting
===============

- Use ``dmesg | grep wlan`` or ``journalctl -xe`` to inspect Wi-Fi-related logs.
- Ensure your Wi-Fi driver/module is loaded.

Recommendations
===============

- Use ``nmcli`` or ``nmtui`` for user-friendly configuration on most systems.
