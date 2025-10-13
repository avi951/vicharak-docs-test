## GPIO

GPIO stands for General Purpose Input/Output. It refers to configurable digital pins on microcontrollers or embedded systems that can act as either inputs or outputs, allowing them to read signals (like button presses) or control devices (like LEDs). They serve as the basic interface for interacting with external hardware.

Axon has **30-pin GPIO header pins** which can support multiple interfaces like UART, I2C etc.


### Axon GPIOs Header

| GPIO number |  Function4  |  Function3  |  Function2  |  Function1   | PWD/GND  |   GPIO   |             Pin#             |            Pin#              |   GPIO   | PWD/GND |                  Function1                   |  Function2   |  Function3   | Function4  | GPIO number |
| :---------: | :---------: | :---------: | :---------: | :----------: | :-----:  | :------: | :--------------------------: | :--------------------------: | :------: | :-----: | :----------------------------------------:   | :----------: | :--------:   | :--------: | :---------: |
|             |             |             |             |              |    12V   |          |<div class='red'>1</div>      |<div class='orange'>2</div>   | GPIO0_B6 |         | <div class='orange'>UART2_RX_M0(DEBUG)</div> |              |              |            |     14      |
|             |             |             |             |              |    GND   |          |<div class='black'>3</div>    |<div class='orange'>4</div>   | GPIO0_B5 |         | <div class='orange'>UART2_TX_M0(DEBUG)</div> |              |              |            |     13      |
|             |             |             |             |              |    5V    |          |<div class='red'>5</div>      |<div class='black'>6</div>    |          |   GND   |                                              |              |              |            |             |
|             |             |             |             |              |    5V    |          |<div class='red'>7</div>      |<div class='black'>8</div>    |          |   GND   |                                              |              |              |            |             |
|     81      |             |             |UART1_CTSN_M0| I2C2_SCL_M1  |          | GPIO2_C1 |<div class='green'>9</div>    |<div class='green'>10</div>   | GPIO2_B6 |         |                 UART1_RX_M0                  | I2C5_SCL_M4  |              |            |     78      |
|     80      |             |             |UART1_RTSN_M0| I2C2_SDA_M1  |          | GPIO2_C0 |<div class='green'>11</div>   |<div class='green'>12</div>   | GPIO2_B7 |         |                 UART1_TX_M0                  | I2C5_SDA_M4  |              |            |     79      |
|     16      |  PWM1_M0    |             |             |              |          | GPIO0_C0 |<div class='green'>13</div>   |<div class='red'>14</div>     |          | 3.3V    |                                              |              |              |            |             |
|             |             |             |             |              |    GND   |          |<div class='black'>15</div>   |<div class='red'>16</div>     |          | 3.3V    |                                              |              |              |            |             |
|     56      |             | UART6_TX_M2 | SPI1_MISO_M2| I2C7_SCL_M0  |          | GPIO1_D0 |<div class='green'>17</div>   |<div class='green'>18</div>   | GPIO1_D1 |         |                 UART6_RX_M2                  | I2C7_SDA_M0  | SPI1_MOSI_M2 |            |     57      |
|     59      |  PWM1_M1    | UART4_RX_M0 | SPI1_CS0_M2 | I2C1_SDA_M4  |          | GPIO1_D3 |<div class='green'>19</div>   |<div class='green'>20</div>   | GPIO1_D2 |         |                 UART4_TX_M0                  | I2C1_SCL_M4  | SPI1_CLK_M2  | PWM0_M1    |     58      |
|             |             |             |             |              |    GND   |          |<div class='black'>21</div>   |<div class='red'>22</div>     |          | 3.3V    |                                              |              |              |            |             |
|     43      |             |             |             |              |          | GPIO1_B3 |<div class='green'>23</div>   |<div class='red'>24</div>     |          | 1.8V    |                                              |              |              |            |             |
|             |             |             |             |              |    GND   |          |<div class='black'>25</div>   |<div class='black'>26</div>   |          | GND     |                                              |              |              |            |             |
|             |             |             |             |              |          | SARADC_4 |<div class='orange'>27</div>  |<div class='orange'>28</div>  | SARADC_3 |         |                                              |              |              |            |             |
|             |             |             |             |              |          | SARADC_1 |<div class='orange'>29</div>  |<div class='orange'>30</div>  | SARADC_2 |         |                                              |              |              |            |             |

:::{note}
You can find [ GPIO Number Translation: ](#axon-gpio-transaction) for Axon.
:::

Before going to configure GPIOs, Need to know some basics:

Let's take one ``GPIO2_B6`` Pin,

|  Pin   |  GPIO    |  GPIO Number  |
| :----: | :------: | :-----------: |
|  10    | GPIO2_B6 |     78        |

- What is GPIO Pin ?
  It is a Pin which locates on GPIO Header on Axon. Axon has 30 Pins on GPIO header.

- What is GPIO Number ?
  You can get GPIO Number from Axon GPIOs Header Table.

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
    vicharak@vicharak:~$ sudo gpioinfo

    gpiochip2 - 32 lines:
            line   0:      unnamed       unused   input  active-high
            line   1:      unnamed       unused   input  active-high
            line   2:      unnamed       unused   input  active-high
            line   3:      unnamed       unused   input  active-high
            line   4:      unnamed       unused   input  active-high
            line   5:      unnamed       unused   input  active-high
            line   6:      unnamed       unused   input  active-high
            line   7:      unnamed       unused   input  active-high
            line   8:      unnamed       unused   input  active-high
            line   9:      unnamed       unused   input  active-high
            line  10:      unnamed       unused   input  active-high
            line  11:      unnamed       unused   input  active-high
            line  12:      unnamed       unused   input  active-high
            line  13:      unnamed       unused   input  active-high
            line  14:     "PIN_10"       unused   input  active-high
            line  15:     "PIN_12"       unused   input  active-high
            line  16:     "PIN_11"       unused   input  active-high
            line  17:      "PIN_9"       unused   input  active-high
            line  18:      unnamed       unused   input  active-high
            line  19:      unnamed       unused   input  active-high
            line  20:      unnamed       unused   input  active-high
            line  21:      unnamed       unused   input  active-high
            line  22:      unnamed       unused   input  active-high
            line  23:      unnamed       unused   input  active-high
            line  24:      unnamed       unused   input  active-high
            line  25:      unnamed       unused   input  active-high
            line  26:      unnamed       unused   input  active-high
            line  27:      unnamed       unused   input  active-high
            line  28:      unnamed       unused   input  active-high
            line  29:      unnamed       unused   input  active-high
            line  30:      unnamed       unused   input  active-high
            line  31:      unnamed       unused   input  active-high
:::

:::{note}
If It shows `gpioinfo` not found, you need to install `gpiod`.

sudo apt update

sudo apt gpiod
:::

### Using C Language

Below Program will configure GPIO Header Pin 10 (GPIO_NUM 78) using gpiod library.

Make sure, you have installed ``libgpiod-dev`` in Axon.

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

### How to change Functionality of GPIO Pin Like, UART, I2C etc  ?

For that, we will soon provide `overlay`, on `vicharak-config`.



:::{seealso}
https://en.wikipedia.org/wiki/General-purpose_input/output
:::
