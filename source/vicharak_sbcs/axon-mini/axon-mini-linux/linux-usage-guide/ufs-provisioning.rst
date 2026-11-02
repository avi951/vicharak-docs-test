.. _axon-mini-ufs-provisioning:

################################
UFS Provisioning Guide
################################

UFS provisioning creates and configures Logical Unit Numbers (LUNs) on a UFS
device so the bootloader, system, and user data can be stored correctly.

.. admonition:: Important Warning
   :class: danger

   UFS provisioning is **OTP (One-Time Programmable)** when the configuration
   is locked.

   Setting these values to ``1`` permanently locks the UFS configuration
   descriptor. After that, you **cannot program or reprovision** the device
   again:

   - ``bConfigDescrLock="1"``
   - ``commit="1"``

   Keep them as ``0`` so the device can still be reprovisioned if needed:

   - ``bConfigDescrLock="0"`` (currently used in our provisioning script)
   - ``commit="0"``

   Do **not** change these to ``1`` unless you intentionally want an
   irreversible, one-time lock.

.. note::

   **UFS provisioning is already done** on Vicharak-shipped UFS modules. Modules
   are verified (including flash validation) before shipment, so you normally do
   **not** need to run provisioning again.

   Run this guide only if:

   - You are using a **brand-new** / unprovisioned UFS module, or
   - You want to change the UFS LUN layout / provisioning configuration.

   For normal OS flashing to an already-provisioned UFS module, go directly to
   :doc:`qdl-raw-image`.

Default UFS device layout
=========================

.. image:: /_static/images/qcs6490-axon-mini/axon-mini-ufs-layout.webp
   :width: 60%
   :alt: Default UFS device layout

UFS device partition layout
---------------------------

The default UFS device provisioning creates eight LUNs (LUN0 to LUN5).

The Linux data and all Linux file system images are stored in LUN0.

Boot well-known LUN (WLUN) ``0xB0`` alternates between LUN1 and LUN2 to provide
a fail-safe backup for the XBL.

The rest of the boot chain is stored in LUN4.

Prerequisites
=============

- Axon Mini with the UFS module seated (power off before connecting the module)
- Host PC with QDL installed (:doc:`qdl-tool-guide`)
- Board in **EDL mode**
- UFS provisioning package (``prog_firehose_ddr.elf`` and ``provision*.xml``)

Download / prepare the provision files from :ref:`axon-mini-downloads` (or the
package supplied with your UFS / BSP release), then extract them:

.. code-block:: console

   unzip provision.zip
   cd provision

Typical contents:

- ``prog_firehose_ddr.elf``
- ``provision_1_3.xml`` (exact filename may vary by package)

Provision UFS
=============

With the board in EDL mode, run QDL with ``-s ufs`` and the provision XML:

.. tab-set::

   .. tab-item:: Linux

      .. code-block:: console

         sudo <qdl_tool_path>/QDL_2.7.1_Linux_x64/qdl -s ufs --allow-fusing prog_firehose_ddr.elf provision_1_3.xml

   .. tab-item:: Windows

      .. code-block:: console

         & "<qdl_tool_path>\QDL_2.7.1_Win_x64\QDL_2.7.1_Win_x64\qdl.exe" -s ufs --allow-fusing .\prog_firehose_ddr.elf .\provision_1_3.xml

On success, QDL reports that UFS provisioning completed. Power-cycle the board
and re-enter **EDL mode** before flashing the OS image.

.. warning::

   Re-provisioning can erase existing UFS contents and change the LUN layout.
   Only provision when required. Never lock the config descriptor unless you
   intentionally want irreversible OTP provisioning.

Next step
=========

After provisioning (if needed), flash the UFS OS image:

:doc:`Axon Mini Image Flashing Guide <qdl-raw-image>`

.. seealso::

   - :ref:`axon-mini-qdl-tool-guide`
   - :doc:`../../storage/ufs`
   - :doc:`../../axon-mini-accessories/axon-mini-ufs`
