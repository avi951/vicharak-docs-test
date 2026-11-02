## GPIO

GPIO stands for General Purpose Input/Output. It refers to configurable digital pins on microcontrollers or embedded systems that can act as either inputs or outputs, allowing them to read signals (like button presses) or control devices (like LEDs). They serve as the basic interface for interacting with external hardware.

Axon Mini has a **40-pin GPIO Header** which can support multiple interfaces like UART, I2C, SPI etc.
It also has a **30-pin GPIO FPC Connector**.

(40-pin-gpio-header)=

### 40-pin GPIO Header

<div style="font-size: 11px; overflow-x: auto;">

| GPIO number | Function4 | Function3  | Function2  | Function1  | PWD/GND | GPIO     | Pin#                       | Pin#                       | GPIO    | PWD/GND | Function1  | Function2  | Function3  | Function4 | GPIO number |
| :---------: | :-------: | :--------: | :--------: | :--------: | :-----: | :------: | :------------------------: | :------------------------: | :-----: | :-----: | :--------: | :--------: | :--------: | :-------: | :---------: |
|             |           |            |            |            | 3.3V    |          | <div class='red'>1</div>   | <div class='red'>2</div>   |         | 5V      |            |            |            |           |             |
|     0       |           |            | I3C0_SDA   | I2C0_SDA   |         | GPIO0    | <div class='green'>3</div> | <div class='red'>4</div>   |         | 5V      |            |            |            |           |             |
|     1       |           |            | I3C0_SCL   | I2C0_SCL   |         | GPIO1    | <div class='green'>5</div> | <div class='black'>6</div> |         | GND     |            |            |            |           |             |
|     36      | I3C1_SDA  | UART9_CTS  | SPI9_MISO  | I2C9_SDA   |         | GPIO36   | <div class='green'>7</div> | <div class='blue'>8</div>  | GPIO50  |         |            | SPI12_SCLK | UART12_TX  |           |     50      |
|             |           |            |            |            | GND     |          | <div class='black'>9</div> | <div class='blue'>10</div> | GPIO51  |         |            | SPI12_CS0  | UART12_RX  |           |     51      |
|     37      | I3C1_SCL  | UART9_RTS  | SPI9_MOSI  | I2C9_SCL   |         | GPIO37   | <div class='green'>11</div>| <div class='blue'>12</div> | GPIO144 |         | I2S_CLOCK  |            |            |           |    144      |
|     38      |           | UART9_TX   | SPI9_SCLK  |            |         | GPIO38   | <div class='green'>13</div>| <div class='black'>14</div>|         | GND     |            |            |            |           |             |
|     39      |           | UART9_RX   | SPI9_CS0   |            |         | GPIO39   | <div class='green'>15</div>| <div class='blue'>16</div> | GPIO32  |         | I2C8_SDA   | SPI8_MISO  | UART8_CTS  |           |     32      |
|             |           |            |            |            | 3.3V    |          | <div class='red'>17</div>  | <div class='blue'>18</div> | GPIO33  |         | I2C8_SCL   | SPI8_MOSI  | UART8_RTS  |           |     33      |
|     57      |           | UART14_RTS | SPI14_MOSI | I2C14_SCL  |         | GPIO57   | <div class='green'>19</div>| <div class='black'>20</div>|         | GND     |            |            |            |           |             |
|     56      |           | UART14_CTS | SPI14_MISO | I2C14_SDA  |         | GPIO56   | <div class='green'>21</div>| <div class='blue'>22</div> | GPIO46  |         | UART11_TX  |            |            |           |     46      |
|     58      |           | UART14_TX  | SPI14_SCLK |            |         | GPIO58   | <div class='green'>23</div>| <div class='blue'>24</div> | GPIO59  |         |            | SPI14_CS0  | UART14_RX  |           |     59      |
|             |           |            |            |            | GND     |          | <div class='black'>25</div>| <div class='blue'>26</div> | GPIO62  |         | UART15_TX  |            |            |           |     62      |
|     40      |           | UART10_CTS | SPI10_MISO | I2C10_SDA  |         | GPIO40   | <div class='green'>27</div>| <div class='blue'>28</div> | GPIO63  |         | UART15_RX  |            |            |           |     63      |
|     41      |           | UART10_RTS | SPI10_MOSI | I2C10_SCL  |         | GPIO41   | <div class='green'>29</div>| <div class='black'>30</div>|         | GND     |            |            |            |           |             |
|     42      |           | UART10_TX  | SPI10_SCLK |            |         | GPIO42   | <div class='green'>31</div>| <div class='blue'>32</div> | GPIO47  |         | UART11_RX  |            |            |           |     47      |
|     43      |           | UART10_RX  | SPI10_CS0  |            |         | GPIO43   | <div class='green'>33</div>| <div class='black'>34</div>|         | GND     |            |            |            |           |             |
|    145      |           |            |            | I2S_WS     |         | GPIO145  | <div class='green'>35</div>| <div class='blue'>36</div> | GPIO48  |         | I2C12_SDA  | SPI12_MISO | UART12_CTS |           |     48      |
|     49      |           | UART12_RTS | SPI12_MOSI | I2C12_SCL  |         | GPIO49   | <div class='green'>37</div>| <div class='blue'>38</div> | GPIO146 |         | I2S_DATA0  |            |            |           |    146      |
|             |           |            |            |            | GND     |          | <div class='black'>39</div>| <div class='blue'>40</div> | GPIO147 |         | I2S_DATA1  |            |            |           |    147      |

</div>

:::{note}
You can find [ GPIO Number Translation: ](#axon-mini-gpio-transaction) for Axon Mini.
:::

(30-pin-gpio-fpc-connector)=

### 30-pin GPIO FPC Connector

| GPIO number | Function4    | Function3    | Function2    | Function1      | GPIO     | Pin#                       | Pin#                       | GPIO    | Function1   | Function2 | Function3 | GPIO number |
| :---------: | :----------: | :----------: | :----------: | :------------: | :------: | :------------------------: | :------------------------: | :-----: | :---------: | :-------: | :-------: | :---------: |
|     161     |              | LPI_GPIO_17  | LPI_I3C_SDA  | LPI_I2C_SDA    | GPIO161  | <div class='green'>1</div> | <div class='blue'>2</div>  | GPIO97  | MI2S0_SCK   |           |           |     97      |
|     162     |              | LPI_GPIO_18  | LPI_I3C_SCL  | LPI_I2C_SCL    | GPIO162  | <div class='green'>3</div> | <div class='blue'>4</div>  | GPIO98  | MI2S0_DATA0 |           |           |     98      |
|     26      |              |              |              | UART6_TX       | GPIO26   | <div class='green'>5</div> | <div class='blue'>6</div>  | GPIO99  | MI2S0_DATA1 |           |           |     99      |
|     27      |              |              |              | UART6_RX       | GPIO27   | <div class='green'>7</div> | <div class='blue'>8</div>  | GPIO100 | MI2S0_WS    |           |           |    100      |
|     163     | LPI_SPI_MISO | LPI_GPIO_19  | LPI_UART_CTS | LPI_I2C_SDA    | GPIO163  | <div class='green'>9</div> | <div class='blue'>10</div> | GPIO101 | MI2S2_SCK   |           |           |    101      |
|     164     | LPI_SPI_MOSI | LPI_GPIO_20  | LPI_UART_RFR | LPI_I2C_SCL    | GPIO164  | <div class='green'>11</div>| <div class='blue'>12</div> | GPIO102 | MI2S2_DATA0 |           |           |    102      |
|     165     | LPI_SPI_SCLK | LPI_GPIO_21  | LPI_UART_TX  |                | GPIO165  | <div class='green'>13</div>| <div class='blue'>14</div> | GPIO103 | MI2S2_WS    |           |           |    103      |
|     166     | LPI_SPI_CS_0 | LPI_GPIO_22  | LPI_UART_RX  |                | GPIO166  | <div class='green'>15</div>| <div class='blue'>16</div> | GPIO104 | MI2S2_DATA1 |           |           |    104      |
|             |              |              |              | NC             |          | <div class='black'>17</div>| <div class='blue'>18</div> | GPIO105 | MI2S1_DATA1 | SEC_MCLK  |           |    105      |
|             |              |              |              | NC             |          | <div class='black'>19</div>| <div class='blue'>20</div> | GPIO106 | MI2S1_SCK   |           |           |    106      |
|     34      |              | UART8_TX     |              | SPI8_SCLK      | GPIO34   | <div class='green'>21</div>| <div class='blue'>22</div> | GPIO107 | MI2S1_DATA0 |           |           |    107      |
|     35      |              | UART8_RX     |              | SPI8_CS0       | GPIO35   | <div class='green'>23</div>| <div class='blue'>24</div> | GPIO108 | MI2S1_WS    |           |           |    108      |
|     96      |              |              |              | PRI_MI2S0_MCLK | GPIO96   | <div class='green'>25</div>| <div class='red'>26</div>  |         | VCC_5V      |           |           |             |
|             |              |              |              | VCC_5V         |          | <div class='red'>27</div>  | <div class='red'>28</div>  |         | VCC_3V3     |           |           |             |
|             |              |              |              | GND            |          | <div class='black'>29</div>| <div class='black'>30</div>|         | GND         |           |           |             |

Before going to configure GPIOs, Need to know some basics:

Let's take one ``GPIO2_B6`` Pin,

|  Pin   |  GPIO    |  GPIO Number  |
| :----: | :------: | :-----------: |
|  10    | GPIO2_B6 |     78        |

- What is GPIO Pin ?
  It is a Pin which locates on the GPIO header on Axon Mini. Axon Mini has a **40-pin GPIO Header** and a **30-pin GPIO FPC Connector**.

- What is GPIO Number ?
  You can get GPIO Number from Axon Mini GPIOs Header Table.

- What is GPIO Chip Num ?
  In ``GPIO2_B6``, 2 means GPIO Chip Number.

- What is GPIO Base Number ?
  It depends on GPIO Chip Number, For example, GPIOCHIP2 has base number = 64

- What is GPIO Line ?
  You can get GPIO Line number by substracting GPIO Base Number from GPIO Number. 


### How GPIO Pins can be configured ?

GPIO Pins can be configured in many ways. For example, you can ``write program`` to function pins according to your
requirement or you can simply run command using ``gpiod`` Command line and you can also use GPIO Pins as UART or I2C
Functionality.

:::{warning}
As mention in table, you can use only one function at a time of GPIO Pin.

Let's take one ``GPIO1_D1`` Pin, You have 3 Function to use this GPIO Pin. Like, UART, I2C, SPI
You can only use any of the above one at a time.
:::


Now, Using ``sudo gpioinfo``, you can figure out which pin is located on which gpiochip and gpio_line.

:::{note}
For GPIO2_B6,

GPIO Pin  = 10

GPIO Line = 14 ( GPIO_NUM - GPIO_BASE_NUMBER for CHIP2 ) ( 78 - 64 ) 

GPIO Chip = 2
:::

:::{code}
    vicharak@axon-mini:~$ sudo gpioinfo
    [sudo] password for vicharak: 
    gpiochip0 - 12 lines:
    	line   0:	unnamed         	input
    	line   1:	unnamed         	input
    	line   2:	unnamed         	input
    	line   3:	unnamed         	input
    	line   4:	unnamed         	input
    	line   5:	unnamed         	input
    	line   6:	unnamed         	input
    	line   7:	unnamed         	input
    	line   8:	unnamed         	input
    	line   9:	unnamed         	input
    	line  10:	unnamed         	input
    	line  11:	unnamed         	input
    gpiochip1 - 10 lines:
    	line   0:	unnamed         	input
    	line   1:	unnamed         	input
    	line   2:	unnamed         	input
    	line   3:	unnamed         	input
    	line   4:	unnamed         	input
    	line   5:	unnamed         	input
    	line   6:	unnamed         	output
    	line   7:	unnamed         	input
    	line   8:	unnamed         	input
    	line   9:	unnamed         	input
    gpiochip2 - 9 lines:
    	line   0:	unnamed         	input
    	line   1:	unnamed         	input
    	line   2:	unnamed         	output
    	line   3:	unnamed         	output
    	line   4:	unnamed         	input
    	line   5:	unnamed         	input
    	line   6:	unnamed         	input
    	line   7:	unnamed         	input
    	line   8:	unnamed         	output
    gpiochip3 - 4 lines:
    	line   0:	unnamed         	input
    	line   1:	unnamed         	input
    	line   2:	unnamed         	input
    	line   3:	unnamed         	input
    gpiochip4 - 176 lines:
    	line   0:	unnamed         	input
    	line   1:	unnamed         	input
    	line   2:	unnamed         	output active-low consumer=perst
    	line   3:	unnamed         	input
    	line   4:	unnamed         	input
    	line   5:	unnamed         	input
    	...
:::

:::{note}
If It shows `gpioinfo` not found, you need to install `gpiod`.

sudo apt update

sudo apt gpiod
:::

### Using C Language

Below Program will configure GPIO Header Pin 10 (GPIO_NUM 78) using gpiod library.

Make sure, you have installed ``libgpiod-dev`` in Axon Mini.

:::{code}

    sudo apt update
    sudo apt-get install -y libgpiod-dev
:::


This code will high GPIO-Pin 10 for 5 sec and again put it in Low.

:::{code}

#include <stdio.h>
#include <gpiod.h>
#include <unistd.h>

#define GPIO_CHIP "/dev/gpiochip2"  // Specify the correct GPIO chip device
#define GPIO_NUMBER 78             // Global GPIO number
#define GPIO_CHIP_BASE 64          // The base GPIO number for gpiochip2 

int main()
{
    struct gpiod_chip *chip;
    struct gpiod_line *line;
    int ret;
    int gpio_line = GPIO_NUMBER - GPIO_CHIP_BASE;  // Local GPIO line number

    // Open the GPIO chip
    chip = gpiod_chip_open(GPIO_CHIP);
    if (!chip)
    {
        perror("Failed to open GPIO chip");
        return EXIT_FAILURE;
    }

    // Get the GPIO line (based on the offset calculated)
    line = gpiod_chip_get_line(chip, gpio_line);
    if (!line)
    {
        perror("Failed to get GPIO line");
        gpiod_chip_close(chip);
        return EXIT_FAILURE;
    }

    // Request the GPIO line as an output and set the initial value to low (0)
    ret = gpiod_line_request_output(line, "gpioset", 0);
    if (ret < 0)
    {
        perror("Failed to request GPIO line as output");
        gpiod_line_release(line);  // Ensure the line is released in case of error
        gpiod_chip_close(chip);
        return EXIT_FAILURE;
    }

    // Set GPIO line 135 to high (enable)
    printf("Setting GPIO %d to high (enabled)\n", GPIO_NUMBER);
    ret = gpiod_line_set_value(line, 1);  // Set value to 1 (high)
    if (ret < 0)
    {
        perror("Failed to set GPIO value");
        gpiod_line_release(line);
        gpiod_chip_close(chip);
        return EXIT_FAILURE;
    }

    // Sleep for a while to keep the pin enabled (you can modify the delay as needed)
    sleep(5);  // Keep the GPIO high for 5 seconds

    // Optionally: Set GPIO line to low (disable) after sleep
    printf("Disabling GPIO %d (set to low)\n", GPIO_NUMBER);
    gpiod_line_set_value(line, 0);  // Set value to 0 (low)

    // Release the GPIO line and close the GPIO chip
    gpiod_line_release(line);
    gpiod_chip_close(chip);

    return 0;
}
:::

1. Compile above code using ``gcc <Code_File_Name.c> -o <Executable_File_Name> -lgpiod``
2. Run executable file using `sudo` as it requires privileges, ``sudo ./<Executable_File_Name>``


### Using gpiod Command Line Tool in Linux

- Install ``gpiod`` Command Line Tool

:::{code}

    sudo apt update
    sudo apt install gpiod
:::

- ``gpiodetect`` - List all GPIO chips present on the system, their names, labels and number of GPIO lines.

- ``gpioinfo`` - List all lines of specified GPIO chips, their names, consumers, direction, active state and additional flags.

- ``gpioget`` - Read values of specified GPIO lines.

- ``gpioset`` - Set values of specified GPIO lines, and potentially keep the lines exported and wait until timeout, user input or signal.

:::{note}
For ``GPIO2_B6``, To set GPIO as High X=1 and Low X=0,

``sudo gpioset gpiochip2 14=<X>``

where, 14 is GPIO Line ( 78 - 64 )
:::

- ``gpiofind`` - Find the GPIO chip name and line offset given the line name.

- ``gpiomon`` - Wait for events on GPIO lines, specifying which events to watch, how many events to process before exiting or if the events should be reported to the console.

### LPI GPIOs

LPI (Low Power Island) GPIOs are available on the **30-pin GPIO FPC Connector**.
They belong to a dedicated low-power domain on the QCS6490 SoC, owned by the
CDSP (Compute DSP), and can stay available for always-on / low-power peripherals
without keeping the main application processor fully active.

#### Available LPI interfaces

| Interface | GPIO pins | Notes |
| :-------: | :-------: | :---- |
| ``LPI_I2C0`` | 161, 162 | Dedicated LPI I2C |
| ``LPI_I2C1`` | 163, 164 | Muxed with LPI SPI / LPI UART |
| ``LPI_SPI`` | 163, 164, 165, 166 | Muxed with LPI I2C1 / LPI UART |
| ``LPI_UART`` | 163, 164, 165, 166 | Muxed with LPI I2C1 / LPI SPI |
| ``LPI_GPIO`` | 161–166 | General-purpose LPI GPIO mode |

:::{warning}
Pins **163–166** are shared. You can enable only **one** of ``LPI_I2C1``,
``LPI_SPI``, or ``LPI_UART`` on those pins at a time.
:::

Refer to the [30-pin GPIO FPC Connector](#30-pin-gpio-fpc-connector) table
for the full pinmux (LPI_GPIO, SPI, UART, I3C, I2C).

### How to change Functionality of GPIO Pin Like, UART, I2C etc  ?

For that, we will soon provide `overlay`, on `vicharak-config`.



:::{seealso}
https://en.wikipedia.org/wiki/General-purpose_input/output
:::
