######################
MIPI Camera Interface
######################

Axon Mini provides the following MIPI CSI camera interfaces on the Qualcomm
**QCS6490**:

Camera
------

- **4 X MIPI CSI [4 lanes]** at **2.5 Gbps per lane** via **30-pin B2B**
- **1 X MIPI CSI [4 lanes]** at **2.5 Gbps per lane** via **22-pin FPC**

Hardware Required
------------------

- Camera module (**OV5647** or **IMX415**)
- Compatible MIPI CSI flex / adapter for the selected connector
  (30-pin B2B path or 22-pin FPC path)

Steps to follow
----------------

1. Connect the hardware (board powered off)
2. Enable the matching camera overlay (if available on your image)
3. Check / install **qcam** (libcamera)
4. Run the camera

Pre-Requisites
--------------

1. Update packages / kernel as needed:

.. code-block:: console

   vicharak@axon-mini:~$ sudo apt update
   vicharak@axon-mini:~$ sudo apt upgrade

2. Ensure Axon Mini is **powered off** before connecting or disconnecting the
   camera.

.. danger::

   Whenever you connect or remove a camera, the board must be powered off.

How to Attach Camera to Axon Mini
---------------------------------

1. Power off Axon Mini.
2. Connect the camera module to the selected MIPI CSI interface:

   - **30-pin B2B** path (one of the four CSI links), or
   - **22-pin FPC** path

3. Note which CSI port you used — the overlay (if used) must match that port
   and sensor.
4. Power on the board.

Enable Overlays In Axon Mini
----------------------------

If your image provides camera overlays via ``vicharak-config``:

1. Open a terminal (``Ctrl+Alt+T``).
2. Run ``sudo vicharak-config``.
3. Select **Overlays** → **Manage overlays**.
4. Enable the overlay for your sensor (**OV5647** or **IMX415**) and CSI port.
5. Exit and reboot:

.. code-block:: console

   vicharak@axon-mini:~$ sudo reboot

Pre-installation (qcam / libcamera)
-----------------------------------

Capture examples below use **qcam**.

Check if qcam is already available:

.. code-block:: console

   vicharak@axon-mini:~$ qcam --version

If ``qcam`` prints a version, skip to **Run Camera**. If you see
``command not found``, install dependencies and build libcamera.

Install dependencies
====================

.. code-block:: console

   vicharak@axon-mini:~$ sudo apt update
   vicharak@axon-mini:~$ sudo apt install build-essential git pkg-config -y
   vicharak@axon-mini:~$ sudo apt install meson ninja-build -y
   vicharak@axon-mini:~$ sudo apt install python3-pip python3-yaml python3-jinja2 python3-ply python3-pyparsing -y
   vicharak@axon-mini:~$ sudo apt install libyaml-dev libevent-dev -y
   vicharak@axon-mini:~$ sudo apt install libudev-dev libgnutls28-dev openssl libexpat1-dev -y
   vicharak@axon-mini:~$ sudo apt install libdrm-dev -y
   vicharak@axon-mini:~$ sudo apt install libjpeg-dev -y
   vicharak@axon-mini:~$ sudo apt install libglib2.0-dev -y
   vicharak@axon-mini:~$ sudo apt install qt6-base-dev qt6-base-dev-tools qt6-wayland-dev -y
   vicharak@axon-mini:~$ sudo apt install \
       qtbase5-dev \
       qtbase5-dev-tools \
       qtchooser \
       qt5-qmake \
       qttools5-dev \
       qtdeclarative5-dev \
       libqt5opengl5-dev \
       qml-module-qtquick-controls \
       libgles2-mesa-dev \
       qml-module-qtquick2 -y

Build and install libcamera
===========================

.. code-block:: console

   vicharak@axon-mini:~$ git clone https://git.linuxtv.org/libcamera.git
   vicharak@axon-mini:~$ cd libcamera
   vicharak@axon-mini:~/libcamera$ git checkout 02277d4c1a5ae7fee582f635936877435a12db64
   vicharak@axon-mini:~/libcamera$ meson setup build --wipe \
       -Dpipelines=simple \
       -Dcam=enabled \
       -Dgstreamer=disabled \
       -Dv4l2=enabled \
       -Dlc-compliance=disabled \
       -Dqcam=enabled
   vicharak@axon-mini:~/libcamera$ ninja -C build -j$(nproc)
   vicharak@axon-mini:~/libcamera$ sudo ninja -C build install
   vicharak@axon-mini:~/libcamera$ sudo ldconfig

.. note::

   The ``git checkout`` pin is optional. The following test steps are based on
   this libcamera revision.

Set permissions
===============

.. code-block:: console

   vicharak@axon-mini:~$ sudo chmod 666 /dev/dma_heap/*

Run Camera
----------

.. tip::

   Connect a monitor (or use the desktop session) to see the qcam preview.

1. OV5647
=========

1. Open the system desktop terminal.
2. Set permissions (each boot if needed):

.. code-block:: console

   vicharak@axon-mini:~$ sudo chmod 666 /dev/dma_heap/*

3. Start qcam from the libcamera build directory:

.. code-block:: console

   vicharak@axon-mini:~$ cd ~/libcamera/build/src/apps/qcam/
   vicharak@axon-mini:~/libcamera/build/src/apps/qcam/$ ./qcam --stream pixelformat=YUYV,width=1920,height=1080

Or, if ``qcam`` is installed system-wide:

.. code-block:: console

   vicharak@axon-mini:~$ qcam --stream pixelformat=YUYV,width=1920,height=1080

2. IMX415
=========

1. Open the system desktop terminal.
2. Set permissions (each boot if needed):

.. code-block:: console

   vicharak@axon-mini:~$ sudo chmod 666 /dev/dma_heap/*

3. Start qcam from the libcamera build directory:

.. code-block:: console

   vicharak@axon-mini:~$ cd ~/libcamera/build/src/apps/qcam/
   vicharak@axon-mini:~/libcamera/build/src/apps/qcam/$ ./qcam --stream pixelformat=YUYV,width=1920,height=1080

Or, if ``qcam`` is installed system-wide:

.. code-block:: console

   vicharak@axon-mini:~$ qcam --stream pixelformat=YUYV,width=1920,height=1080

.. tip::

   IMX415 may support higher modes. If 1920×1080 works, you can try:

   .. code-block:: console

      vicharak@axon-mini:~$ qcam --stream pixelformat=YUYV,width=3840,height=2160

Troubleshooting
---------------

- ``qcam: command not found`` — complete the libcamera build/install steps above.
- No camera / open fails — confirm cable, CSI port, and overlay for **OV5647**
  or **IMX415**.
- Permission errors on ``/dev/dma_heap/*`` — re-run ``sudo chmod 666 /dev/dma_heap/*``.
