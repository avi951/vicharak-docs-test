.. _axon-mini-qdl-tool-guide:

#######################
QDL Flash Tool Guide
#######################

Qualcomm provides the **Qualcomm Device Loader (QDL)** tool for flashing firmware
on Qualcomm SoCs. On Axon Mini, QDL is the primary tool used to flash **Linux**
images to onboard storage while the board is in **EDL (Emergency Download)**
mode.

.. tip::

   Axon Mini supports **EDL mode** (also known as Qualcomm **9008** / QDL mode),
   which allows the board to be flashed with new firmware.

   Use the **Linux QDL Tool** on Linux hosts and the **Windows QDL Tool** on
   Windows hosts.

This tool supports the following operations:

- Downloading / flashing firmware
- Writing partitions from ``rawprogram*.xml`` / ``patch*.xml``
- Fusing / programming via Firehose (``prog_firehose_ddr.elf``)
- Recovering a board that fails to boot normally

.. toctree::
   :caption: Contents
   :maxdepth: 2

   Linux QDL Tool <linux-qdl-tool>
   Windows QDL Tool <windows-qdl-tool>
