---
orphan: true
---

(axon-gpio-description)=

# Axon GPIO Description

Vicharak Axon board features a 30-pin GPIO (General-Purpose Input/Output)
header that provides flexible options for connecting and controlling external
devices. Through software settings, you can configure these pins as either
input or output, making them adaptable for various applications.

Out of the 30 pins on the header, 9 are dedicated GPIO pins. These GPIO pins
can also be repurposed for SPI (Serial Peripheral Interface),
UART (Universal Asynchronous Receiver-Transmitter), PWM (Pulse Width Modulation) and
I2C (Inter-Integrated Circuit) functions.

This versatility opens up a wide array of possibilities for interfacing with
different components and facilitating communication with other devices.

<!-- TODO: Update Vicharak config to be suitable for Axon -->
## GPIO Voltage Level
RK3588 SoC has three multiple GPIO voltage levels. Below table shows the
voltage level of vaaman GPIOs.

:::{list-table}
:widths: 40 40
:header-rows: 1

-
  - GPIO
  - Voltage Level

-
  - UART debug (Pin 2 and 4)
  - 3.3V

-
  - SARADC
  - 1.8V

-
  - Other GPIOs
  - 3.3V

:::

## Available GPIOs on Axon

Vicharak Axon board has total **30 GPIOs** available for user which
are accessible on `pin header`.
Below table shows the GPIOs available on Axon board.

:::{warning}
Not all functions can be used at the same time. Only one function can be used
or assigned to a GPIO at a time.
:::

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

<!-- TODO: Update Vicharak config and serial console suitable for Axon -->
:::{note}

- The default function of pins marked in <span class="orange">orange</span> are
  specific to this board. For example, Pins 27, 28, 29 and 30 cannot be used as GPIOs
  as they are SARADC pins.
- All pins, except those for power supply, are directly connected to the
  System-on-Chip (SoC).
- `UART2` has a default baudrate to **115200 bps**, Need to change baudrate to **1500000 bps**.
  Here, you can find instructions to use UART2 in [Serial Console](#axon-linux-uart-serial-console), 
  and you can also use another UART provided on GPIO Pin, refer to [Vicharak Config Device tree  overlays](/vicharak_sbcs/axon/peripherals/uart) section.
:::

<!-- TODO: FPGA LVDS guide -->
(axon-gpio-transaction)=

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

<!-- TODO: Update Vicharak config to be suitable for Axon -->

:::{seealso}
[Configure 30-Pin header using vicharak-config utility](#)
**(Will be available soon)**
:::
