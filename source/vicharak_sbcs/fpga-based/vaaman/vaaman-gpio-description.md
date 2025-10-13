---
orphan: true
---

(vaaman-gpio-description)=

# Vaaman GPIO Description

Vicharak Vaaman board features a 40-pin GPIO (General-Purpose Input/Output)
header that provides flexible options for connecting and controlling external
devices. Through software settings, you can configure these pins as either
input or output, making them adaptable for various applications.

Out of the 40 pins on the header, 21 are dedicated GPIO pins. These GPIO pins
can also be repurposed for SPI (Serial Peripheral Interface),
UART (Universal Asynchronous Receiver-Transmitter), and
I2C (Inter-Integrated Circuit) functions.

This versatility opens up a wide array of possibilities for interfacing with
different components and facilitating communication with other devices.

:::{tip}
**What? you want more GPIOs?**

Fear not, we have a solution for you. Vaaman board has additional 40-FPGA GPIOs
available to the user.\
These GPIOs are accessible from the FPGA and can be configured to be used inside
your project and applications
:::

<!-- TODO: Add FPGA GPIO user guide and description -->

## GPIO Voltage Level

RK3399 SoC has three multiple GPIO voltage levels. Below table shows the
voltage level of vaaman GPIOs.

:::{list-table}
:widths: 20 40 80
:header-rows: 1

-
  - GPIO
  - Voltage Level
  - Tolerance

-
  - ADC_IN0
  - 1.8V
  - ~1.98V

-
  - GPIO3_C0 (Pin 32)
  - 3.3V
  - ~3.46V

-
  - Other GPIOs
  - 3.0V
  - ~3.15V

:::

## Available GPIOs on Vaaman

Vicharak Vaaman board has total **80 GPIOs** available for user. **40 GPIOs**
are accessible on `40 pin header` and **40 GPIOs** are accessible from `FPGA`.
Below table shows the GPIOs available on Vaaman board.

:::{warning}
Not all functions can be used at the same time. Only one function can be used
or assigned to a GPIO at a time.
:::

### SoC GPIOs Header

| GPIO number | Function2 |  Function1   |   GPIO   |             Pin#             |            Pin#             |   GPIO   |              Function1              | GPIO number |
| :---------: | :-------: | :----------: | :------: | :--------------------------: | :-------------------------: | :------: | :---------------------------------: | :---------: |
|             |           |    +3.3V     |          | <div class='yellow'>1</div>  |  <div class='red'>2</div>   |          |                +5.0V                |             |
|             |           |   I2C7_SDA   |          | <div class='orange'>3</div>  |  <div class='red'>4</div>   |          |                +5.0V                |             |
|             |           |   I2C7_SCL   |          | <div class='orange'>5</div>  | <div class='black'>6</div>  |          |                 GND                 |             |
|     75      |           |   SPI2_CLK   | GPIO2_B3 |  <div class='green'>7</div>  | <div class='green'>8</div>  | GPIO4_C4 | <div class='orange'>UART2_TXD</div> |     148     |
|             |           |     GND      |          |  <div class='black'>9</div>  | <div class='green'>10</div> | GPIO4_C3 | <div class='orange'>UART2_RXD</div> |     147     |
|     146     |           |     PWM0     | GPIO4_C2 | <div class='green'>11</div>  | <div class='green'>12</div> | GPIO4_A3 |              I2S1_SCLK              |     131     |
|     150     |           |     PWM1     | GPIO4_C6 | <div class='green'>13</div>  | <div class='black'>14</div> |          |                 GND                 |             |
|     149     |           |   SPDIF_TX   | GPIO4_C5 | <div class='green'>15</div>  | <div class='green'>16</div> | GPIO4_D2 |                                     |     154     |
|             |           |    +3.3V     |          | <div class='yellow'>17</div> | <div class='green'>18</div> | GPIO4_D4 |                                     |     156     |
|             |           |     +5V      |          |  <div class='red'>19</div>   | <div class='black'>20</div> |          |                 GND                 |             |
|             |           |     GND      |          | <div class='black'>21</div>  | <div class='green'>22</div> | GPIO4_D5 |                                     |     157     |
|             |           |     +5V      |          |  <div class='red'>23</div>   | <div class='black'>24</div> |          |                 GND                 |             |
|             |           |     GND      |          | <div class='black'>25</div>  | <div class='blue'>26</div>  |          |               ADC_IN0               |             |
|     64      |           |   I2C2_SDA   | GPIO2_A0 |  <div class='green'>27</div> | <div class='green'>28</div> | GPIO2_A1 |              I2C2_CLK               |     65      |
|     74      | I2C6_SCL  |   SPI2_TXD   | GPIO2_B2 | <div class='green'>29</div>  | <div class='black'>30</div> |          |                 GND                 |             |
|     73      | I2C6_SDA  |   SPI2_RXD   | GPIO2_B1 | <div class='green'>31</div>  | <div class='green'>32</div> | GPIO3_C0 |              SPDIF_TX               |     112     |
|     76      |           |   SPI2_CSn   | GPIO2_B4 | <div class='green'>33</div>  | <div class='black'>34</div> |          |                 GND                 |             |
|     133     |           | I2S1_LRCK_TX | GPIO4_A5 | <div class='green'>35</div>  | <div class='green'>36</div> | GPIO4_A4 |            I2S1_LRCK_RX             |     132     |
|     158     |           |              | GPIO4_D6 | <div class='green'>37</div>  | <div class='green'>38</div> | GPIO4_A6 |              I2S1_SDI               |     134     |
|             |           |     GND      |          | <div class='black'>39</div>  | <div class='green'>40</div> | GPIO4_A7 |              I2S1_SDO               |     135     |

:::{note}
- The default function of pins marked in <span class="orange">orange</span> are
  specific to this board. For example, Pins 3 and 5 cannot be used as GPIOs
  because they are connected to the I2C bus and are already in use.
- All pins, except those for power supply, are directly connected to the
  System-on-Chip (SoC).
- **Pin 7** is directly connected to the `MIPI CSI` pin on the board.
  Instructions to use UART2 as serial console can be found in
  [Serial Console](#serial-console), and to disable it, refer to
  [Vicharak Config Device tree overlays](#vicharak-config-overlays)
  section.
- Both `UART2` and `UART4` support a wide range of baud rates, including
  **115200bps, 500000bps, 1500000bps,** and more.
- **Pin 8** and **pin 10** of the CPU are used by `UART2` and are not accessible to the user by default.
:::

### FGPA Header

| Function  |     GPIO     |             Pin#             |             Pin#             |     GPIO     | Function  |
| :-------: | :----------: | :--------------------------: | :--------------------------: | :----------: | :-------: |
|   +5.0V   |              |   <div class='red'>1</div>   | <div class='yellow'>2</div>  |              |   +3.3V   |
|   +5.0V   |              |   <div class='red'>3</div>   | <div class='yellow'>4</div>  |              |   +3.3V   |
| LVDS/GPIO |  GPIOT_RXP28 |  <div class='green'>5</div>  |  <div class='green'>6</div>  |  GPIOT_RXN28 | LVDS/GPIO |
|   GPIO    |   GPIOL_73   |  <div class='green'>7</div>  |  <div class='green'>8</div>  |   GPIOL_75   |   GPIO    |
|   GPIO    |   GPIOR_173  |  <div class='green'>9</div>  | <div class='green'>10</div>  |   GPIOL_72   |   GPIO    |
|   GPIO    |   GPIOR_174  | <div class='green'>11</div>  | <div class='green'>12</div>  |   GPIOR_178  |   GPIO    |
|    LED    |  GPIOT_RXN27 | <div class='orange'>13</div> | <div class='green'>14</div>  |   GPIOR_183  |   GPIO    |
|    LED    |  GPIOT_RXP27 | <div class='orange'>15</div> | <div class='orange'>16</div> |  GPIOT_RXP24 |    LED    |
|   GPIO    |   GPIOL_63   | <div class='green'>17</div>  | <div class='orange'>18</div> |  GPIOT_RXP24 |    LED    |
|    GND    |              | <div class='black'>19</div>  | <div class='black'>20</div>  |              |    GND    |
|    GND    |              | <div class='black'>21</div>  | <div class='black'>22</div>  |              |    GND    |
| LVDS/GPIO |  GPIOT_RXN29 |  <div class='blue'>23</div>  |  <div class='blue'>24</div>  |  GPIOT_RXP29 | LVDS/GPIO |
|    CDI    |   GPIOL_22   |  <div class='blue'>25</div>  | <div class='black'>26</div>  |              |    GND    |
|    GND    |              | <div class='black'>27</div>  | <div class='black'>28</div>  |              |    GND    |
|   GPIO    |   GPIOR_168  | <div class='green'>29</div>  | <div class='green'>30</div>  |   GPIOR_187  |   GPIO    |
|   GPIO    |   GPIOL_17   | <div class='green'>31</div>  |  <div class='blue'>32</div>  |   GPIOL_24   |    CDI    |
|    CDI    |   GPIOL_20   |  <div class='blue'>33</div>  | <div class='green'>34</div>  |   GPIOL_66   |   GPIO    |
|    CDI    |   GPIOL_18   |  <div class='blue'>35</div>  | <div class='green'>36</div>  |   GPIOL_62   |   GPIO    |
|    GND    |              | <div class='black'>37</div>  | <div class='black'>38</div>  |              |    GND    |
|   +3.3V   |              | <div class='yellow'>39</div> | <div class='yellow'>40</div> |              |   +3.3V   |

:::{note}

- The default function of pins marked in <span class="orange">orange</span> is
  specific to this board. For example, pin 13, 15, 16 and 16 are used as LEDs
  and they can be used as GPIOs or LVDS pins.
- The pins layout from 29 to 40 follows the standard PMOD pinout. Check the
  [PMOD](https://reference.digilentinc.com/reference/pmod/pmod) page for more
  information.
- LVDS/GPIO pins can either be used as GPIOs or as LVDS pins. To use them as
  GPIOs, refer to [Vicharak FPGA LVDS]().
  section.
- CDI can be normally used as GPIOs.
:::

<!-- TODO: FPGA LVDS guide -->

## GPIO Numbers translation

|            GPIO0             | Number |     |            GPIO1            | Number |     |           GPIO2            | Number |     |           GPIO3           | Number |     |            GPIO4             | Number |
| :--------------------------: | :----: | :-: | :-------------------------: | :----: | :-: | :------------------------: | :----: | :-: | :-----------------------: | :----: | :-: | :--------------------------: | :----: |
| <div class="yellow">A0</div> |   0    |     | <div class="green">A0</div> |   32   |     | <div class="blue">A0</div> |   64   |     | <div class="red">A0</div> |   96   |     | <div class="orange">A0</div> |  128   |
| <div class="yellow">A1</div> |   1    |     | <div class="green">A1</div> |   33   |     | <div class="blue">A1</div> |   65   |     | <div class="red">A1</div> |   97   |     | <div class="orange">A1</div> |  129   |
| <div class="yellow">A2</div> |   2    |     | <div class="green">A2</div> |   34   |     | <div class="blue">A2</div> |   66   |     | <div class="red">A2</div> |   98   |     | <div class="orange">A2</div> |  130   |
| <div class="yellow">A3</div> |   3    |     | <div class="green">A3</div> |   35   |     | <div class="blue">A3</div> |   67   |     | <div class="red">A3</div> |   99   |     | <div class="orange">A3</div> |  131   |
| <div class="yellow">A4</div> |   4    |     | <div class="green">A4</div> |   36   |     | <div class="blue">A4</div> |   68   |     | <div class="red">A4</div> |  100   |     | <div class="orange">A4</div> |  132   |
| <div class="yellow">A5</div> |   5    |     | <div class="green">A5</div> |   37   |     | <div class="blue">A5</div> |   69   |     | <div class="red">A5</div> |  101   |     | <div class="orange">A5</div> |  133   |
| <div class="yellow">A6</div> |   6    |     | <div class="green">A6</div> |   38   |     | <div class="blue">A6</div> |   70   |     | <div class="red">A6</div> |  102   |     | <div class="orange">A6</div> |  134   |
| <div class="yellow">A7</div> |   7    |     | <div class="green">A7</div> |   39   |     | <div class="blue">A7</div> |   71   |     | <div class="red">A7</div> |  103   |     | <div class="orange">A7</div> |  135   |
| <div class="yellow">B0</div> |   8    |     | <div class="green">B0</div> |   40   |     | <div class="blue">B0</div> |   72   |     | <div class="red">B0</div> |  104   |     | <div class="orange">B0</div> |  136   |
| <div class="yellow">B1</div> |   9    |     | <div class="green">B1</div> |   41   |     | <div class="blue">B1</div> |   73   |     | <div class="red">B1</div> |  105   |     | <div class="orange">B1</div> |  137   |
| <div class="yellow">B2</div> |   10   |     | <div class="green">B2</div> |   42   |     | <div class="blue">B2</div> |   74   |     | <div class="red">B2</div> |  106   |     | <div class="orange">B2</div> |  138   |
| <div class="yellow">B3</div> |   11   |     | <div class="green">B3</div> |   43   |     | <div class="blue">B3</div> |   75   |     | <div class="red">B3</div> |  107   |     | <div class="orange">B3</div> |  139   |
| <div class="yellow">B4</div> |   12   |     | <div class="green">B4</div> |   44   |     | <div class="blue">B4</div> |   76   |     | <div class="red">B4</div> |  108   |     | <div class="orange">B4</div> |  140   |
| <div class="yellow">B5</div> |   13   |     | <div class="green">B5</div> |   45   |     | <div class="blue">B5</div> |   77   |     | <div class="red">B5</div> |  109   |     | <div class="orange">B5</div> |  141   |
| <div class="yellow">B6</div> |   14   |     | <div class="green">B6</div> |   46   |     | <div class="blue">B6</div> |   78   |     | <div class="red">B6</div> |  110   |     | <div class="orange">B6</div> |  142   |
| <div class="yellow">B7</div> |   15   |     | <div class="green">B7</div> |   47   |     | <div class="blue">B7</div> |   79   |     | <div class="red">B7</div> |  111   |     | <div class="orange">B7</div> |  143   |
| <div class="yellow">C0</div> |   16   |     | <div class="green">C0</div> |   48   |     | <div class="blue">C0</div> |   80   |     | <div class="red">C0</div> |  112   |     | <div class="orange">C0</div> |  144   |
| <div class="yellow">C1</div> |   17   |     | <div class="green">C1</div> |   49   |     | <div class="blue">C1</div> |   81   |     | <div class="red">C1</div> |  113   |     | <div class="orange">C1</div> |  145   |
| <div class="yellow">C2</div> |   18   |     | <div class="green">C2</div> |   50   |     | <div class="blue">C2</div> |   82   |     | <div class="red">C2</div> |  114   |     | <div class="orange">C2</div> |  146   |
| <div class="yellow">C3</div> |   19   |     | <div class="green">C3</div> |   51   |     | <div class="blue">C3</div> |   83   |     | <div class="red">C3</div> |  115   |     | <div class="orange">C3</div> |  147   |
| <div class="yellow">C4</div> |   20   |     | <div class="green">C4</div> |   52   |     | <div class="blue">C4</div> |   84   |     | <div class="red">C4</div> |  116   |     | <div class="orange">C4</div> |  148   |
| <div class="yellow">C5</div> |   21   |     | <div class="green">C5</div> |   53   |     | <div class="blue">C5</div> |   85   |     | <div class="red">C5</div> |  117   |     | <div class="orange">C5</div> |  149   |
| <div class="yellow">C6</div> |   22   |     | <div class="green">C6</div> |   54   |     | <div class="blue">C6</div> |   86   |     | <div class="red">C6</div> |  118   |     | <div class="orange">C6</div> |  150   |
| <div class="yellow">C7</div> |   23   |     | <div class="green">C7</div> |   55   |     | <div class="blue">C7</div> |   87   |     | <div class="red">C7</div> |  119   |     | <div class="orange">C7</div> |  151   |
| <div class="yellow">D0</div> |   24   |     | <div class="green">D0</div> |   56   |     | <div class="blue">D0</div> |   88   |     | <div class="red">D0</div> |  120   |     | <div class="orange">D0</div> |  152   |
| <div class="yellow">D1</div> |   25   |     | <div class="green">D1</div> |   57   |     | <div class="blue">D1</div> |   89   |     | <div class="red">D1</div> |  121   |     | <div class="orange">D1</div> |  153   |
| <div class="yellow">D2</div> |   26   |     | <div class="green">D2</div> |   58   |     | <div class="blue">D2</div> |   90   |     | <div class="red">D2</div> |  122   |     | <div class="orange">D2</div> |  154   |
| <div class="yellow">D3</div> |   27   |     | <div class="green">D3</div> |   59   |     | <div class="blue">D3</div> |   91   |     | <div class="red">D3</div> |  123   |     | <div class="orange">D3</div> |  155   |
| <div class="yellow">D4</div> |   28   |     | <div class="green">D4</div> |   60   |     | <div class="blue">D4</div> |   92   |     | <div class="red">D4</div> |  124   |     | <div class="orange">D4</div> |  156   |
| <div class="yellow">D5</div> |   29   |     | <div class="green">D5</div> |   61   |     | <div class="blue">D5</div> |   93   |     | <div class="red">D5</div> |  125   |     | <div class="orange">D5</div> |  157   |
| <div class="yellow">D6</div> |   30   |     | <div class="green">D6</div> |   62   |     | <div class="blue">D6</div> |   94   |     | <div class="red">D6</div> |  126   |     | <div class="orange">D6</div> |  158   |
| <div class="yellow">D7</div> |   31   |     | <div class="green">D7</div> |   63   |     | <div class="blue">D7</div> |   95   |     | <div class="red">D7</div> |  127   |     | <div class="orange">D7</div> |  159   |

<!-- TODO: Add FPGA GPIO user guide and description -->

:::{seealso}
[Configure 40-Pin header using vicharak-config utility](#vicharak-config-overlays)
:::
