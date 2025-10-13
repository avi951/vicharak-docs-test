######################################################
Vicharak-DAO : Remote Access for Vicharak Computers
######################################################

.. warning::

   **Beta Version** : 1.1.0

Through `Vicharak-Dao <https://dao.vicharak.in/>`_, users can connect and enable secure, hassle-free **remote access** to their Vicharak devices from **anywhere in the world**.  
It lets you access the command-line interface of your device directly from your web browser, making remote management quick and reliable.  
Using **WebRTC**, it ensures real-time, low-latency, and secure communication between your device and browser.

.. image:: /_static/images/rk3588-axon/vicharak-dao-axon1.webp
   :width: 98%


Prerequisites
==============

Before you begin, ensure that your Vicharak Board is:

- Connected to the Internet via **Wi-Fi** or **Ethernet**


Install Vicharak-DAO on Vicharak Board
=======================================

On your Vicharak Board, update your system and install **Vicharak-DAO** using:

.. code-block:: bash

   sudo apt update
   sudo apt upgrade
   sudo apt install vicharak-dao


======================================================
Steps to be Done on Vicharak-DAO Website
======================================================

Register Your Account
----------------------

1. Open the `Vicharak-DAO Website <https://dao.vicharak.in/>`_ in your web browser.  
2. **Register** using your **Google** or **GitHub** account.

.. image:: /_static/images/dao-1.webp
   :width: 80%

.. image:: /_static/images/dao-2.webp
   :width: 80%


Add Vicharak Device
---------------------

You can add your device using either **Token** or **Local Network**.


.. warning::

  **Token** : When Vicharak device is connected to Display Monitor (HDMI, Type-C DP etc. ) or SSH through internet.

  **Local Network** : When Vicharak device and Host System both are on same network.

|
**Method 1: Add Using Token**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. On the website, click **Add Device** → **Token** → **Connect Device**.  

.. image:: /_static/images/dao-3.webp
   :width: 80%

.. image:: /_static/images/dao-4.webp
  :width: 80%

.. note::

   Tokens let you add devices securely from **any network** —  
   the device and host computer **do not need to be on the same network**.

2. Enter a name for your device.

.. image:: /_static/images/dao-6.webp
   :width: 80%

3. A **token** will be generated for your device. Copy it.  

.. image:: /_static/images/dao-5.webp
   :width: 80%

4. `Add Token in Vicharak Device <#steps-to-be-done-on-vicharak-board>`_

|
**Method 2: Add Locally**
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. On the website, click **Add Device** → **Locally** → **Connect Device**.  

.. image:: /_static/images/dao-9.webp
   :width: 80%

2. A list of devices connected to the **same network** will appear.  

.. image:: /_static/images/dao-10.webp
   :width: 80%


3. Select your device and enter its configuration details like custom device name for your reference, username and password.

.. note::
  Default credentials:
   - **Username**: ``vicharak``
   - **Password**: ``12345``

.. image:: /_static/images/dao-11.webp
   :width: 80%

======================================================
Steps to be Done on Vicharak Board
======================================================

Add Token (For Token Method)
------------------------------

If you used the **Token** method on the website, you now need to add that token to your device.

.. note::

   You can access your Vicharak Board using:  

   - **Micro HDMI** — Ports Tx0 or Tx1  
   - **Serial Console** — See `Documentation <https://docs.vicharak.in/vicharak_sbcs/axon/axon-getting-started/#using-serial-console>`_ (Baudrate: 1500000)  
   - **SSH** — See `Documentation <https://docs.vicharak.in/vicharak_sbcs/axon/axon-getting-started/#using-ssh>`_ (``vicharak@<IP>``) — both devices must be on the **same network**.  

   Default credentials:  
   - **Username**: ``vicharak``  
   - **Password**: ``12345``  

Run the following command, replacing **<Token>** with the copied token:

.. code-block:: bash

   sudo dao add <Token>

Return to the Vicharak-DAO website and **reload** the dashboard page.  
Your device will now appear in the list.


======================================================
Manage Your Devices
======================================================

To open a remote terminal session:

1. In the `Vicharak-DAO Website <https://dao.vicharak.in/>`_, locate your device.  
2. Click the **Connect ( >_ )** button.  

.. image:: /_static/images/dao-7.webp
   :width: 80%

A secure terminal console will appear in your browser.

.. image:: /_static/images/dao-8.webp
   :width: 80%


======================================================
Update / Uninstall
======================================================

Update your installation:

.. code-block:: bash

   sudo apt update
   sudo apt upgrade

Uninstall completely:

.. code-block:: bash

   sudo apt purge vicharak-dao


======================================================
Troubleshooting
======================================================

If you face any difficulties using ``vicharak-dao``, please post your query on the  
`Vicharak Forum <https://discuss.vicharak.in/>`_ for community and developer support.
