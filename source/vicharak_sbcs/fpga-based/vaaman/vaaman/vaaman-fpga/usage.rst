.. _efinix_usage:

Starting with efinity IDE
=========================

Also Refer to : 
 1. `Efinity Software Installation Guide <https://www.efinixinc.com/docs/efinity-installation-v3.4.pdf>`_. 
 2. `Efinity Software User Guide <https://www.efinixinc.com/docs/efinity-ug-v14.1.pdf>`_. 
 3. `Efinix Support Home <https://www.efinixinc.com/support/docs.php?p=e>`_.


**To run your code on  the FPGA, follow these steps:**

.. image:: /_static/images/efinity_home.webp
   :width: 100%


.. image:: /_static/images/Create_Project.webp 
   :width: 100%



After starting the IDE click on files and create a project. Write your project name 
and select trion family  and fpga T120F324. **Timing model should be selected as C3** .

.. image:: /_static/images/Choose_Board.webp
   :width: 100%


In the design tab you can select  your prefereable  HDL. Verilog ,systemverilog and VHDL are supported. Default is verilog.
You can also add your rtl code while the creation of project and specify the top module.

.. image:: /_static/images/Assign_Top_Mod_Verilog_Version.webp
   :width: 100%


In Dashboard , you can add/create your verilog files by right-clicking on design tab under your project.

.. image:: /_static/images/Create_Design_File.webp
   :width: 100%


.. image:: /_static/images/verilog_creation.webp
   :width: 100%



Default gedit editor will pop-up on right side on which you can write your code. Save the code.
`led blinking demo code <https://github.com/vicharak-in/LED_BLINKING_DEMO.git>`_. 

.. image:: /_static/images/Open_Interface_Designer.webp
   :width: 100%


Now you need to  open inferace designer to map your signals to the fpga boards GPIO.

.. image:: /_static/images/Create_Reqd_Block.webp
   :width: 100%


Create a gpio block and configure  your  pins as input/output  mode as per your design


**Setting PLL**



The FPGA have crystall oscillators  which can give frequency upto 74.5Mhz. You can use this crystall oscillators as source
clock and generate the desired frequency via PLL.

.. image:: /_static/images/pll.webp
   :width: 100%



While creating the gpio block for source clock you need to change its connection  type from normal to PLL_CLK_IN. and give this pin any crystall oscillator
in resouce assigner.

.. image:: /_static/images/create_pll_gpio.webp
   :width: 100%


For PLL  you need to create a PLL block as done for gpio. Select the source clk. The selected source clk instance name would
be shown below once selected.

.. image:: /_static/images/Choose_pll_pin.webp
   :width: 100%


Here both automated calculation and manual calculation options are available for setting the  PLL. You can choose any of these
as per your convenience. Here you have to mention your actual clock input which will be fed in the design.

.. image:: /_static/images/connect_pll_output.webp
   :width: 100%


Navigate to the resource assigner to map the pins on board. You can refer to `pinout guide  </_static/files/Vaaman0.3_Pinout_Guide_Rev0.3.pdf>`_ for mapping. By entering the 
package pin the rest of the colums would be to auto-fill

.. image:: /_static/images/Assign_Pins.webp
   :width: 100%


Now check for design issue. It throws error if there's any error in mapping the pins. Now save the interface design.

.. image:: /_static/images/Check_Design.webp
   :width: 100%

You can also give constrains for your design by creating a constrain file with .sdc extension.

.. image:: /_static/images/constrain_create.webp
   :width: 100%


Here you can mention your virtual clock or mention the input/output delay. According to the constrain the software will
perform the placement and routing to meet the desired perfomance.
   
.. image:: /_static/images/constraint_file.webp
   :width: 100%


.. image:: /_static/images/sdc_file.webp
   :width: 100%

Now just press synthesis option to run your entire flow. By default it will run the entire flow of synthesis, placement ,routing and bitsream generation.
You can toggle it off for running one flow at time. After running the entire flow in project directory and outflow/ directory will
generated containing all the generated files at each step.

.. image:: /_static/images/auto_flow.webp
   :width: 100%

Now follow the steps  on :ref:`vaaman-fpga`  to dump your  generated bitstream on FPGA.


===================
How to use Debugger 
===================
Also Refer :
`Efinix Debugger Guide <https://www.efinixinc.com/docs/efinity-tutorial-debugger-v1.2.pdf>`_.

The Efinity software features a hardware Debugger, facilitating signal probing in FPGA designs through the JTAG interface.
The Debugger encompasses two debug cores:

- Configure Virtual I/O (vio) cores using a manual flow and the Profile Editor.
- Configure Logic Analyzer (la) cores either through a manual flow or the automated flow of the Debug Wizard.

The subsequent sections provide detailed guidance on both the automated and manual flows.


Automated debugger
********************
Create a Debug Profile:

1. Open the project.
2. Synthesize the design.
3. Launch the Debug Wizard by clicking its icon in the main icon bar.



.. image:: /_static/images/Debugger_wizard.webp
   :width: 100%


4. Choose "Elaborated Netlist" or "Post-Map" in the Signals from list.
5. Select led and counter buses from the left list and move them to the right using the >> button.

.. image:: /_static/images/steps_wizard.webp
   :width: 100%


6. Keep the Probe Type as default, DATA AND TRIGGER.
7. Proceed to the next step. The wizard generates a debug profile.
8. Ensure "Auto Instantiation" is enabled to integrate the debug profile into your project. Click Finish.



.. image:: /_static/images/finish_wizard.webp 
   :width: 100%

9. The software prompts for recompilation. Click OK.
10. Perform a full compile.



Programming  FPGA for debugger 
******************************


1. Launch the Debugger by choosing Tools > Open Debugger. 


.. image:: /_static/images/debugger.webp
   :width: 100%

2. Ensure the Board is recognized as the USB Target. If not, connect the board and click Refresh USB Targets.
3. Click the Select Image File button.
4. Navigate to the outflow directory and choose bitstream file.
5. Click Start Programming. The console will display programming messages.


.. image:: /_static/images/debugger_steps.webp
   :width: 100%





Observing Probed Signals in Debugger
************************************

1. Initiate Debugger connection.
2. In Trigger Setup tab, add desired nets.
3. Specify trigger conditions (e.g., value).
4. Start Debugger to capture data upon trigger.
5. Upon completion, GTKWave opens automatically to display waveform.
6. Disconnect Debugger to halt operation.


Manual Debugger
***************


Create Debugger Profile
************************

To configure Virtual I/O and Logic Analyzer debug cores in a profile:

1. Open the project.
2. Launch the Debugger via Tools > Open Debugger. Since no debug profile exists, the Profile Editor perspective opens.
3. Add a Virtual I/O core (VIO) using Add Debug Core > Virtual I/O. Configure Probes(input) and source(output) signals as specified (i.e name and width).
4. Add a Logic Analyzer core (LA) via Add Debug Core > Logic Analyzer. Configure probes to capture signals matching VIO settings. the vio0 tab to view captured data in the Value fields.
5. Generate Debug RTL to create necessary debug files.
6. Open debug_top.v and rename "edb_top" as "edb_top_manual."
7. Close the debugger.


Add Debug core in your project 
*******************************

To integrate debug code into your project and compile it:

1. Open the Efinity main window and go to the Project tab.
2. In the Interface Designer, add the JTAG User Tap block, configure it, and generate SDC constraints.
3. Close the Interface Designer.
4. Modify design file by uncommenting specific lines to enable debug code and instantiate debug_top module.
5. Save your changes.
6. Compile the design.


Programm the FPGA  
******************

To program the FPGA:

1. Open Debugger by choosing Tools > Open Debugger.
2. Confirm the Trion T20 Development Board is recognized as the USB Target; refresh if necessary.
3. Select the FPGA configuration file (bitstream) from the outflow directory using the Select Image File button.
4. Initiate programming by clicking Start Programming, and monitor programming messages in the console.


Run the Debugger 
*****************

Observing Probed Signals in Debugger:

1. Connect Debugger and navigate to the la0 tab for trigger setup.
2. Add the desire trigger condition.
3. If want the change the vio0 values and Run the debugger.
4. Then its wait for thrigger, after applying trigger open the GTKWave for checking the debug signal.
5. Disconnect Debugger to stop capturing data.
