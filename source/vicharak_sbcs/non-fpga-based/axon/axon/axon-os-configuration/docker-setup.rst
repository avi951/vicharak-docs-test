################
Docker Setup
################

.. note::

    Ensure that your system is running **Kernel version 6.1** or later, as this version includes the necessary configurations for Docker support.  

    You can install the latest kernel packages from the **Vicharak APT repository** by running:

    .. code-block:: bash

        sudo apt update
        sudo apt upgrade


Setting Up Docker on Axon
=========================

Docker is a containerization platform that allows you to run applications in isolated environments. Follow the steps below to install and configure Docker on your Axon device.

Installing Docker
-----------------

To install Docker, follow the official installation guide:

`Install Docker on Ubuntu <https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository>`_

This guide will walk you through:
    - Adding the official Docker repository  
    - Installing the required dependencies  

After installation, verify Docker by checking the installed version:

.. code-block:: bash

    docker --version

Starting the Docker Service
---------------------------

Once Docker is installed, start its service using:

.. code-block:: bash

    sudo service docker start

To ensure Docker starts automatically on every system boot, enable it using:

.. code-block:: bash

    sudo systemctl enable docker

Verifying the Docker Network Setup
----------------------------------

To confirm that Docker is set up correctly, check the available network interfaces:

.. code-block:: bash

    ip a

If Docker is running properly, you should see an interface named ``docker0`` in the output. This interface is created by Docker to manage container networking.

Troubleshooting: Fixing Docker Daemon Connection Issues
=======================================================

If you encounter the following error while running Docker commands:

``docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?``

It may indicate an issue with the `iptables` backend. Follow these steps to resolve it.

Checking the `iptables` Backend
-------------------------------

Docker requires `iptables` for managing network rules. Some Linux distributions use `nftables` by default, which can cause networking issues. To check which backend is being used, run:

.. code-block:: bash

    sudo update-alternatives --display iptables

If the output shows `nft`, it means `nftables` is in use, which may not be compatible with Docker.

Switching to `iptables` Legacy Mode
-----------------------------------

To resolve potential compatibility problems, switch `iptables` to legacy mode:

.. code-block:: bash

    sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
    sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy

Restarting Docker
-----------------

After switching to `iptables` legacy mode, restart the Docker service to apply the changes:

.. code-block:: bash

    sudo systemctl restart docker

Verifying the Fix
-----------------

Once the Docker service restarts, check if it is running correctly:

.. code-block:: bash

    sudo systemctl status docker

If Docker is now running, verify network connectivity by listing Docker networks:

.. code-block:: bash

    docker network ls

You should see `bridge`, `host`, and `none` networks, confirming that Docker networking is functioning properly.

Summary
=======

1. Install Docker using the official guide.  
2. Start and enable the Docker service.  
3. Verify installation by checking for the `docker0` network interface.  
4. If the Docker daemon is not running, check the `iptables` backend.  
5. If `nftables` is in use, switch to `iptables-legacy`.  
6. Restart Docker and verify that it runs correctly.  

Following these steps ensures that Docker is fully functional on your system, preventing common network and service-related issues.
