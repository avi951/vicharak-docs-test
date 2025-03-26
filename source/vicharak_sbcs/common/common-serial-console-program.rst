.. _common-serial-console-program:

.. tab-set::

    .. tab-item:: PuTTY (GUI)

        1. Download and install the `PuTTY <https://www.putty.org/>`_ program.

        2. Open the PuTTY program and configure the serial parameters as shown
		   in the image below.

        .. image:: ../../_static/images/Putty_step.png
           :width: 50%

        3. Click on the **Open** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: TeraTerm (GUI)

        1. Download and install the
            `TeraTerm <https://osdn.net/projects/ttssh2/releases/>`_ program.

        2. Open the TeraTerm program and configure the serial parameters.

        - On the **Setup** menu, click on **Serial port**.
        - Select the serial port number and configure the serial parameters
          as shown in the image below.

        .. image:: ../../_static/images/teraterm-configuration.png
           :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: Linux GTK-Term (GUI)

        1. Install the GTK-Term program using the following command:

        .. code-block:: bash

            sudo apt-get install gtkterm

        2. Open the GTK-Term program and configure the serial parameters.

        - On the **File** menu, click on **Port**.
        - Select the serial port number and configure the serial parameters as
          shown in the image below.

        .. image:: ../../_static/images/gtkterm-configuration.png
           :width: 50%

        3. Click on the **OK** button to open the serial console.

        4. You will now be able to access the serial console.

    .. tab-item:: Minicom (CLI)

        .. note::
            Read minicom configuration from
            :ref:`Linux Minicom guide <minicom-guide>`.

