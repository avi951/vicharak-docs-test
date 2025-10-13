######################
Axon Vicharak Config
######################

**vicharak-config** also has a systemd service that is use configure system. It has many features like enabling
overlays, controlling WiFi and GPIO pins etc.

How to navigate around vicharak-config
======================================

- Use **UP** or **DOWN** key to move the selection across available options.
- Use **RIGHT** or **LEFT** key to move `in` or `out` of the options menu and also,
  allows you to select **<Ok>** or **<Cancel>** option.
- Alternatively, you can also use **TAB** key to switch between them.
- **Enter** key is used to confirm the corresponding option.
- **ESC** key is used to do back to previous menu.

Vicharak Config TUI
---------------------

.. code-block:: console

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


.. note::
    The above menu might be shown differently depending on the terminal style.

.. toctree::
   :maxdepth: 1
   :caption: Available Feature

   Board Backup <backup>
   USB Tethering <usb-tethering>
