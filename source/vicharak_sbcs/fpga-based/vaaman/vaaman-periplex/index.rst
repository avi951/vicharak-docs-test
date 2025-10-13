########
Periplex
########

This documentation provides detailed information about Periplex on Vicharak’s Reconfigurable Edge Computers (e.g., Vaaman), including its installation and usage. Periplex enables the quick generation of hardware peripherals and offers a simple API for use on Reconfigurable Edge Computers(e.g., Vaaman), a single-board computers with an onboard FPGA. It can link Linux device trees and drivers to the generated hardware using custom or default DTSOs.

Unlike off-the-shelf solutions, Periplex supports an exceptionally high number of peripherals, such as (26 UARTs, 10 I2Cs, and 12 PWMs), (40 UARTs, 10 PWMs), or (20 I2S microphones, 20 I2S speakers), with their drivers pre-built into Linux.

Periplex is a 360-degree solution—it integrates fundamental Linux drivers, FPGA architectures, communication between the CPU and FPGA, and internal FPGA subsystem communication automatically.

Without Periplex, even FPGA developers would struggle for months to build a solution like this. Periplex reduces that effort to seconds. And the best part? It does the same for non-FPGA developers as well.

.. image:: ../../../_static/images/rk3399-vaaman/periplex_flowchart.webp
   :width: 100%
   :align: center

.. toctree::
   :glob:
   :caption: Contents
   :maxdepth: 2
   :titlesonly:

   Installation <install>
   Usage <usage>
   Peripherals <peripherals/index> 
