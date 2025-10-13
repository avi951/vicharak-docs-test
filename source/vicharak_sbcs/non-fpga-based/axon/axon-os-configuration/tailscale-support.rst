========================
Tailscale Configutation
========================

.. note::

    We recommend to use Vicharak 6.1 kernel and latest `Ubuntu 24.04 Noble Numbat
    <https://downloads.vicharak.in/vicharak-axon/ubuntu/24_noble/>`_ , in order to support. Flash Image
    using this `Documentation </vicharak_sbcs/axon/axon-linux/linux-usage-guide/rockchip-develop-guide>`_

    .. code::

        sudo apt update
        sudo apt reinstall linux-image-6.1.75-axon linux-headers-6.1.75-axon

    You can also use Kernel linux-image-5.10.160-axon.

Tailscale Setup and Configuration on Linux
==========================================

Tailscale is a mesh VPN based on WireGuard that allows secure and simple networking between devices, even across firewalls and NAT.
This guide explains how to install, configure, and manage Tailscale on Linux systems.

Prerequisites
-------------

- A Linux-based system (Debian, Ubuntu)
- Root privileges (sudo)
- An active internet connection
- A `Tailscale account <https://tailscale.com>`_

Installation
------------

Install via Official Script (Recommended)

`Installation Guide <https://tailscale.com/kb/1031/install-linux>`_

Start and Enable the Service
----------------------------

After installation, start and enable the Tailscale daemon:

.. code-block:: bash

   sudo systemctl enable --now tailscaled

Authenticate with Tailscale
---------------------------

Use the following command to connect the device to your Tailscale network:

.. code-block:: bash

   sudo tailscale up

This will print a URL. Open it in your browser and authenticate using your Tailscale account. Once complete, your device will join the mesh network.

Check Connection Status
-----------------------

View current connection status:

.. code-block:: bash

   tailscale status

Show the device's Tailscale IP address:

.. code-block:: bash

   tailscale ip

Show general information:

.. code-block:: bash

   tailscale version
   tailscale netcheck

Disconnect from Tailscale
-----------------

To disconnect from the network:

.. code-block:: bash

   sudo tailscale down

Troubleshooting
---------------

- Ensure the `tailscaled` service is running:

  .. code-block:: bash

     sudo systemctl status tailscaled

- Re-authenticate if the device gets disconnected:

  .. code-block:: bash

     sudo tailscale up

- Check logs:

  .. code-block:: bash

     journalctl -u tailscaled

Uninstallation
--------------

To uninstall Tailscale:

.. code-block:: bash

   sudo tailscale down
   sudo apt remove tailscale    # Or your distro’s package manager

Links
-----

.. note::

  - `Official site <https://tailscale.com>`_
  - `Documentation <https://tailscale.com/kb/>`_
