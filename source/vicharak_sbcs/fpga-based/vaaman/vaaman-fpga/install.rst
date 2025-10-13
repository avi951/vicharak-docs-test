.. _vaaman_fpga_install:

============
Installation 
============


.. tab-set::
        
   .. tab-item:: linux

      The FPGA used on vaaman is efinix's trion T120F324.Efinity IDE is used for  generating the bit/hex stream 
      of your RTL code to run in on FPGA.



      You can download the the software from `here <https://www.efinixinc.com/support/efinity.php>`_.
      (Efinity software provides a free liscense.To get a free license, register at efinix  `Support Center <https://www.efinixinc.com/support/index.php>`_. )

      .. image:: /_static/images/reg.webp
       	 :width: 100%
	

      Run the following command on your terminal to extract the downloaded folder content.

      .. code-block:: 
	
       	 tar -xvf downloaded_folder_name.tar.bz2

      ``cd <efinix-folder>/bin/`` directory and run the following command to setup your IDE

      .. code-block::

       	 source setup.sh

      .. tip::
         Write the above command  at the end of your .bashrc file to avoid writing it every time you start.


      .. Note::

         In some version of ubuntu  after running this command terminal may throw core aborted error.
         This due  missing dev files of libxcb libraries.You can simply install them via 
      
      .. code-block:: 
            
       	 sudo apt install libxcb*

     
      For Installation of drivers , from the <efinix-folder>/bin directory run:

      .. code-block:: shell

       	 sudo ./install_usb_driver.sh
      
      After setting up just writing efinity on your terminal will start the efinity software.

      For  detailed information: see  `software guide <https://www.efinixinc.com/docs/efinity-ug-v13.1.pdf>`_.


   .. tab-item:: Windows

      Double-click the ``efinity_version.msi`` installer package and follow the on-screen instructions or,

      For installing the shortcut in your desktop directory then run this script :

      .. code-block:: shell

       		 <installation directory>/bin/install_desktop.sh

      **Efinity Quick Start**

      For launching the Efinity Graphical User interface (GUI), Double click on the desktop icon.

      <OR> 

      Use the Efinity tool using command line and for lunch use this steps :

      1. For Setup the environment and path:

      .. code-block:: shell

         bin\setup.bat

      2. Launch Efinity GUI : 

      .. code-block:: shell 
         
         bin\setup.bat --run

      3. Run the Efinity  : 
      
      - For changing the Project directory : 

      .. code-block:: shell

         cd %EFINITY_HOME%\project\<project name>

      - Run Efinity :

      .. code-block:: shell

         efx_run.bat <project name>.xml

      4. For help : 

      .. code-block:: shell

       	 efx_run.bat --help

      **Installing USB Drivers** 

      Download the Zadig software(version 2.7 or later) from `zadig.akeo.ie <https://zadig.akeo.ie/>`_.

      Note : Do not need to install in only run this downloaded file.

      **Steps for install the drivers** 

      1. Connect the board to your computer and power it on.
      2. Run Zadig software.
         - Note: Run Zadig as an administrator for persistent USB driver settings.
      3. Choose Options > List All Devices.
      4. For each interface (ending with "Interface N"):
         - Select libusb-win32 from the Driver drop-down list.
         - Click Replace Driver.
      5. Close Zadig software. 

   .. tab-item:: Simulation
      
    Install iVerilog, a free Verilog simulation tool, for compiling and simulating Verilog HDL source code.

    Download the simulator from `bleyer.org/icarus <https://bleyer.org/icarus>`_.
    <OR>
    To access the source code, visit `github.com/steveicarus/iverilog <https://github.com/steveicarus/iverilog>`_.


    **Installing GTKWave**

    GTKWave is an open-source tool used for analyzing post-simulation dumpfiles, providing a graphical interface with a waveform viewer and RTL source code navigator. 
    It's compatible with the iVerilog simulator, making it useful for debugging simulation models and viewing VCD waveform data.

    To download and run the latest Windows version of GTKWave:

    1. Visit `gtkwave - Browse Files at Sourceforge.net <https://sourceforge.net/projects/gtkwave/files/>`_. to locate the Windows files for GTKWave.
    2. Download and unzip the file.
    3. Optionally, add the path to GTKWave's bin folder to your System Variables path if necessary for correct launch.
    4. Execute gtkwave.exe found in the bin directory of the installation folder to run the program.

    **GTKWave Installation in Linux**
 
    For Linux users, use the following commands:

    .. code-block:: shell

         sudo apt-get update
         sudo apt-get install gtkwave 

