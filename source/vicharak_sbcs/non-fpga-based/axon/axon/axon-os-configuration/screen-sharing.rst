##############################
Screen Sharing on Axon via X2Go
##############################

This guide explains how to enable desktop sharing on the Axon single‑board computer using X2Go. It covers installation, configuration, and important notes to facilitate screen sharing from the running display (e.g., :0).

Overview
========

The Axon SBC (RK3588‑based) supports X2Go screen sharing, allowing remote users to view or control the console session. 

Installation
============

On the Axon (server):

.. code-block:: bash

    sudo apt update
    sudo apt install x2goserver x2goserver-xsession 


On the client (PC - Linux):

.. code-block:: bash

    sudo apt update
    sudo apt install x2goclient

Configuring Desktop Sharing
===========================

1. Start desktop sharing on host pc. Run the UI tool:

   .. code-block:: bash

      x2goclient 

   .. image:: /_static/images/rk3588-axon/x2go-client-setup.webp

2. Enter Below things :

   - Host/IP : ``IP`` You can get IP by using ``ip a`` command in Axon.

   - Login : e.g., ``vicharak``

   - Select Session Type : ``mate``

3. You can new session is created on right side. Just click on it and enter default password ``12345`` for ``vicharak`` user.

   .. image:: /_static/images/rk3588-axon/x2go-client-gui.webp
     :width: 60%

4. You can see the GUI Screen on a new box.

Conclusion
==========

Using these steps, you can enable effective console desktop sharing on Axon. 
