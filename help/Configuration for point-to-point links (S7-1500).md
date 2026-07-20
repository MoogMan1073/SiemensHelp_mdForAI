---
title: "Configuration for point-to-point links (S7-1500)"
package: HWCConfPtP15enUS
topics: 46
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuration for point-to-point links (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Basics of serial communication (S7-1500)](#basics-of-serial-communication-s7-1500)
- [Configuring / parameter assignment (S7-1500)](#configuring-parameter-assignment-s7-1500)
- [Programming - communication using instructions (S7-1500)](#programming---communication-using-instructions-s7-1500)
- [Startup and Diagnostics (S7-1500)](#startup-and-diagnostics-s7-1500)

## Introduction (S7-1500)

This section contains information on the following topics:

- [Overview of the communication modules (S7-1500)](#overview-of-the-communication-modules-s7-1500)
- [Overview of the processing steps (S7-1500)](#overview-of-the-processing-steps-s7-1500)
- [Overview of instructions (S7-1500)](#overview-of-instructions-s7-1500)

### Overview of the communication modules (S7-1500)

Automation systems encompass a wide range of components. These also include communication modules. A simple possibility of data exchange is provided by serial communication via point-to-point connections.

Customizing to a wide range of communication partners is possible by setting the communication parameters at a lower layer of the OSI layer model (see section [Transmission security](#transmission-security-s7-1500)).

Communication through point-to-point connection with S7-1500, ET 200MP and ET 200SP takes place exclusively by means of communication modules (CM) with serial interfaces.

SIMATIC S7 offers a number of modules that provide the physical interface and fundamental protocol mechanisms for this application use.

- RS232: An interface that can coordinate the communication between the partners through additional accompanying signals.
- RS422/RS485: An interface that allows longer lines through the use of differential voltages as transmission technology and also enables structures with more than 2 devices through a bus structure (RS485).

Instructions that carry out the coordination between the CPU and CM are available to transfer data from the CPU to the respective modules. They inform the user program about a successful transmission or the receipt of new data. In systems without a SIMATIC CPU, users must program the [function of these instructions themselves](https://support.industry.siemens.com/cs/ww/en/view/59062563).

The function and use of the PtP communication modules is described in this function manual.

#### Overview of components and article numbers

Tabular overview of communication modules and their application suitability

| Communication module | S7-1500 | ET 200MP | ET 200SP | Article number |
| --- | --- | --- | --- | --- |
| CM PtP RS232 BA <sup>1)</sup> | X | X | ‑ | 6ES7540-1AD01-0AA0 |
| CM PtP RS422/485 BA | X | X | ‑ | 6ES7540-1AB01-0AA0 |
| CM PtP RS232 HF <sup>2)</sup> | X | X | ‑ | 6ES7541-1AD01-0AB0 |
| CM PtP RS422/485 HF | X | X | ‑ | 6ES7541-1AB01-0AB0 |
| CM PtP (ET 200SP) | ‑ | ‑ | X | 6ES7137-6AA01-0BA0 |
| <sup>1)</sup> BA = Basic   <sup>2)</sup> HF = High Feature |  |  |  |  |

> **Note**
>
> **CM PtP (ET 200SP) with IM 155-6 MF HF**
>
> The use of different field bus protocols, except Profibus/Profinet, is possible with the interface module IM 155-6 MF HF (6ES7155-6MU00-0CN0). In this case, the instruction library PtP Communication cannot be used. Note the information from the Programming Manual [CM PtP in operation without SIMATIC system instructions](https://support.industry.siemens.com/cs/ww/en/view/59062563). See also the Equipment Manual for the interface module as a download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109773210).

#### Overview of components and interfaces

Tabular overview of communication modules and their functions.

| Communication module | Interface | Protocols |  |  |  |  | Connection technology |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | **Freeport** | **3964(R)** | **Modbus master** | **Modbus slave** | **USS-Master** | **D-Sub  9-pin** | **D-Sub  15-pin** |
| CM PtP RS232 BA | RS232 | X | X | - | - | X | X | - |
| CM PtP RS422/485 BA | RS422 | X | X | - | - | X | - | X |
| RS485 | X | - | - | - | X | - | X |  |
| CM PtP RS232 HF | RS232 | X | X | X | X | X | X | - |
| CM PtP RS422/485 HF | RS422 | X | X | X | X | X | - | X |
| RS485 | X | - | X | X | X | - | X |  |
| CM PtP (ET 200SP) | RS232 | X | X | X | X | X | ET 200SP BaseUnit <sup>1)</sup> |  |
| RS422 <sup>2)</sup> | X | X | X | X | X |  |  |  |
| RS485 | X | - | X | X | X |  |  |  |
| <sup>1)</sup> BaseUnit with terminals instead of D-Sub; assignment depending on physical transmission properties   <sup>2)</sup> The CM PtP communication module can also be used for multi-point coupling in RS422 operation |  |  |  |  |  |  |  |  |

#### Overview of components and data transmission rates

The communication modules can send and receive data with different data transmission rates. The table below shows the assignment to the individual communication modules.

| Communication module | Data transmission rate in bps |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **300** | **600** | **1200** | **2400** | **4800** | **9600** | **19200** | **38400** | **57600** | **76800** | **115200** | **250000** <sup>1)</sup> |
| CM PtP RS232 BA | X | X | X | X | X | X | X | - | - | - | - | - |
| CM PtP RS422/485 BA | X | X | X | X | X | X | X | - | - | - | - | - |
| CM PtP RS232 HF | X | X | X | X | X | X | X | X | X | X | X | - |
| CM PtP RS422/485 HF | X | X | X | X | X | X | X | X | X | X | X | X |
| CM PtP (ET 200SP) | X | X | X | X | X | X | X | X | X | X | X | X |
| <sup>1)</sup> Especially for using the DMX512 protocol with RS485 |  |  |  |  |  |  |  |  |  |  |  |  |

#### Overview of components and receive buffer size

Each communication module has a buffer to cache received frames. The table below shows the assignment of the maximum size of an individual frame as well as the size of the memory for the individual communication modules.

| Module | Receive buffer size KB | Max. frame length KB | Bufferable frames |
| --- | --- | --- | --- |
| CM PtP RS232 BA | 2 | 1 | 255 |
| CM PtP RS422/485 BA | 2 | 1 | 255 |
| CM PtP RS232 HF | 8 | 4 | 255 |
| CM PtP RS422/485 HF | 8 | 4 | 255 |
| CM PtP (ET 200SP) | 4 | 2 | 255 |

#### Accompanying signals and data flow control

- Software data flow control with XON/XOFF

  The Freeport protocol supports data flow control with XON/XOFF via the RS232 and RS422 interfaces.
- Hardware data flow control with RTS/CTS

  The Freeport protocol supports data flow control with RTS/CTS via the RS232 interface.
- Automatic operation of accompanying signals

  The RS232 accompanying signals can be controlled with the Freeport, Modbus master and Modbus slave protocols by means of the RS232 interface. (Only available if hardware data flow control is activated.)

#### Protocols of the communication modules

You may set up a communication connection with different protocols, depending on the communication modules used:

- Freeport: Transmission of ASCII character strings without specified protocol format
- 3964(R): Communication between programmable logic controllers (master/master communication)
- Modbus RTU: Communication between programmable logic controllers (master/slave communication). The communication module can be the master as well as the slave.
- USS: Communication between a programmable logic controller and a drive (master/slave communication). Communication is tailored to the drive technology requirements. The communication module can only be master.

### Overview of the processing steps (S7-1500)

#### Point-to-point connection

The system provides various networking options for the exchange of data between two or more communication partners. The simplest form of data interchange is via a point-to-point connection between two communication partners.

The communication module (CM) forms the interface between a programmable logic controller and a communication partner. Data is sent in serial mode via point-to-point connection with the communication module.

#### Configuring / parameter assignment

Configuring the communication module includes the arrangement of the communication module in the device configuration of STEP 7 (TIA Portal) as well as the settings of the specific protocol parameters in the properties dialog of the communication module (static configuration).

#### Programming

Programming includes the program-specific connection of the communication module to the corresponding CPU by means of the user program. You program the communication module with STEP 7 (TIA Portal).

Communication between CPU, communication module and a communication partner takes place through instructions. A number of instructions are available for the S7-1500 and S7-1200 automation systems. You can use these instructions to initiate and control communication in the user program as well as influence the configuration for runtime (dynamic configuration).

For more information, please refer to [Overview of instructions](#overview-of-instructions-s7-1500) and the STEP 7 (TIA Portal) online help.

### Overview of instructions (S7-1500)

#### Data communication

Two types of data exchange between the CPU and the communication module are possible with the communication modules:

- Acyclic data exchange (Universal)

  The point-to-point instructions communicate with the communication module asynchronously by reading or writing data records.

  Data transmission takes place across several cycles.

  > **Note**
  >
  > **CPU configuration limits**
  >
  > When using the instructions with asynchronous communication, you should take into account the configuration limits of the respective CPU for reading and writing data records. If multiple instructions need to read or write data records simultaneously on a CPU, there may need to be a gap between the calls of each instruction by the user program.
- Cyclic data exchange ([Performance optimized for many short frames](#special-features-for-the-use-of-the-option-for-performance-optimization-s7-1500))

  The point-to-point instructions communicate with the communication module synchronously with the application cycle via the IO data of the communication module.

  The input data comprises 32 bytes, of which 24 bytes are available for the frame. The output data comprises 32 bytes, of which 30 bytes are available for the frame. Using cyclic data optimizes the reaction time, especially if you are using several CM PtPs in parallel.

  > **Note**
  >
  > Cyclic data exchange is available with the instruction library PtP Communication as of V4.0.

#### Overview of the instructions

The communication protocols are implemented on the communication module. The protocol is used to adapt the interface of the communication module to the interface of the communication partner.

Communication between the CPU, the communication module and a communication partner takes place by means of special instructions and protocols that support the corresponding communication modules.

The instructions form the software interface between the CPU and the communication module. They must be called cyclically from the user program. When the instruction library PtP-Communication as of V4.0 is used, the instructions detect independently whether the Performance option is active and adapt the method for the data exchange.

The instructions are part of STEP 7 (TIA Portal). The instructions are available in the "Instructions" task card under Communication &gt; Communication processor. They apply to all listed communication modules if they support the required function.

All tables
Instructions for PtP
Instructions for Modbus
Instructions for USS

Instructions for PtP

| Instruction | Meaning |
| --- | --- |
| [Send_P2P](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#send_p2p-sending-data-s7-1200-s7-1500) | To send data to a communication partner. |
| [Receive_P2P](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#receive_p2p-receiving-data-s7-1200-s7-1500) | To receive data from a communication partner. |
| [Receive_Reset](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#receive_reset-clear-receive-buffer-s7-1200-s7-1500) | To clear the receive buffer of the communication module. |
| [Port_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#port_config-configure-ptp-communication-port-s7-1200-s7-1500) | Dynamically assigning the basic interface parameters. |
| [Send_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#send_config-configure-ptp-sender-s7-1200-s7-1500) | Send parameter assignment; dynamically assigning serial send parameters of a port. |
| [Receive_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#receive_config-configure-ptp-recipient-s7-1200-s7-1500) | Receive parameter assignment; dynamically assigning serial receive parameters of a port. |
| [P3964_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#p3964_config-configuring-the-3964r-protocol-s7-1200-s7-1500) | Protocol configuration; Dynamically configuring the parameters of procedure 3964(R). |
| [Signal_Get](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#signal_get-read-status-s7-1200-s7-1500) | Reading RS232 accompanying signals. |
| [Signal_Set](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#signal_set-set-accompanying-signals-s7-1200-s7-1500) | Setting RS232 accompanying signals. |
| [Get_Features](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#get_features-get-extended-functions-s7-1200-s7-1500) | Reading the extended functions supported by the communication module. |
| [Set_Features](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#set_features-set-extended-functions-s7-1200-s7-1500) | Activating the extended functions supported by the communication module. |

Instructions for Modbus

| Instruction | Meaning |
| --- | --- |
| [Modbus_Master](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus_master-communicate-as-modbus-master-s7-1200-s7-1500) | Communicating as Modbus master via the PtP port. |
| [Modbus_Slave](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus_slave-communicate-as-modbus-slave-s7-1200-s7-1500) | Communicating as Modbus slave via the PtP port. |
| [Modbus_Comm_Load](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus_comm_load-configure-communication-module-for-modbus-s7-1200-s7-1500) | Configuring the port of the communication module for Modbus RTU. |

Instructions for USS

| Instruction | Meaning |
| --- | --- |
| [USS_Port_Scan](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_port_scan-uss_port_scan_31-communication-by-means-of-a-uss-network-s7-1200-s7-1500) | Communication via the USS network. |
| [USS_Drive_Control](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_drive_control-uss_drive_control_31-preparing-and-displaying-data-for-the-drive-s7-1200-s7-1500) | Exchanging data with the drive. |
| [USS_Read_Param](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_read_param-uss_read_param_31-read-data-from-drive-s7-1200-s7-1500) | Reading parameters from the drive. |
| [USS_Write_Param](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_write_param-uss_write_param_31-change-data-in-drive-s7-1200-s7-1500) | Changing parameters in the drive. |

## Basics of serial communication (S7-1500)

This section contains information on the following topics:

- [Serial data transmission (S7-1500)](#serial-data-transmission-s7-1500)
- [Transmission security (S7-1500)](#transmission-security-s7-1500)
- [RS232 mode (S7-1500)](#rs232-mode-s7-1500)
- [RS422 mode (S7-1500)](#rs422-mode-s7-1500)
- [RS485 mode (S7-1500)](#rs485-mode-s7-1500)
- [Handshake procedure (S7-1500)](#handshake-procedure-s7-1500)

### Serial data transmission (S7-1500)

During serial data transmission, the individual bits of a character of information to be transmitted are sent successively in a defined sequence.

#### Bidirectional data traffic - operating mode

In the context of bidirectional data traffic, we distinguish between two operating modes for the communication module:

- Half-duplex operation

  The data is exchanged between the communication partners in both directions alternately. In half-duplex operation one communication partner is sending and the other communication partner is receiving at the same time. In the process one line is alternately used for sending or receiving.
- Full-duplex operation

  The data is exchanged between one or more communication partners in both directions simultaneously, which means you can send and receive data at the same time. This process requires one line for sending and one line for receiving.

#### Data transmission

The so-called time base synchronism (a fixed timing code used in the transmission of a fixed character string) is only upheld during transmission of a character. Each character to be sent is preceded by a synchronization impulse, also called start bit. The length of the start-bit transmission determines the clock pulse. The end of character transmission is formed by one or two stop bits.

#### Declarations

In addition to start and stop bits, additional declarations must be made between the sending and receiving partners before serial transmission can take place. These include:

- Data transmission rate
- Frame start and end criteria (e.g., character delay time)
- Parity
- Number of data bits (7 or 8 bits/characters)
- Number of stop bits (1 or 2)

### Transmission security (S7-1500)

Transmission security plays an important role in the transmission of data and in the selection of the transmission procedure. Generally speaking, the more layers of the reference model are applied, the higher the transmission security.

#### Classification of existing protocols

The figure below illustrates how the protocols of the communication module fit into the reference model.

![Classification of the existing protocols of the communication module in the reference model](images/38697912331_DV_resource.Stream@PNG-en-US.png)

Classification of the existing protocols of the communication module in the reference model

#### Transmission security with Freeport

Transmission security when using Freeport:

- When data is sent with Freeport, there are no data security measures other than the use of a parity bit. This means data transmission with Freeport is very efficient, but data security is not guaranteed. A certain degree of data security can be achieved through parameter assignment of the frame start and frame end conditions.
- Using the parity bit ensures that the inversion of a bit in a character to be sent can be recognized. If two or more bits of a character are inverted, however, there is no guarantee that these errors are still detected.
- To increase transmission security, you can, for example, implement a checksum, a frame length specification, or configurable end conditions. These measures must be implemented by the user.
- A further increase in data security can be achieved by means of acknowledgment frames in response to send or receive frames. This is the case with high-grade protocols for data communication (ISO 7-layer reference model).

#### Transmission security with 3964(R)

The parity bit is used to increase data security; depending on the configuration, it completes the number of data bits to be transmitted to form an even or odd number.

Using the parity bit ensures that the inversion of a bit in a character to be sent can be recognized. If two or more bits of a character are inverted, however, these errors can no longer be reliably detected.

If parity is set to "none", no parity bit is transmitted. This setup reduces transmission security.

Two different procedures for data transmission can be used, either with or without a block check character:

- Data transmission without block check character: **3964**

  Transmission security is achieved by means of a specified frame structure, frame breakdown, and frame repetitions.
- Data transmission with block check character: **3964R**

  The high degree of transmission security is achieved by means of a specified frame structure and breakdown, frame repetitions, as well as inclusion of a block check character (BCC).

In this manual, the term 3964(R) is used when descriptions and notes refer to both data transmission modes.

#### Transmission integrity for Modbus and USS

The parity bit is used to increase transmission security; depending on the configuration, it completes the number of data bits to be transmitted to form an even or odd number.

Using the parity bit ensures that the inversion of a bit in a character to be sent can be recognized. If two or more bits of a character are inverted, however, this error can no longer be clearly detected.

If parity is set to "none", no parity bit is transmitted. This setup reduces transmission security.

The cyclic redundancy check (CRC) is additionally used with Modbus. With this method additional redundancy in the form of a so-called CRC value is added for each data block of the user data before data transmission. This is a check value calculated by using a specific procedure that can be used to detect any errors that may occur during transmission.

A BCC (block check character) is additionally used with USS. The block check character is formed during the receipt and is compared with the received BCC after the entire frame has been read in. If these two characters do not match, the frame is not evaluated. When a character is incorrectly transmitted, an error is reliably detected. When an even number of characters is incorrectly transmitted, an error can no longer be reliably detected.

### RS232 mode (S7-1500)

The following communication modules support RS232 mode:

- CM PtP RS232 BA
- CM PtP RS232 HF
- CM PtP (ET 200SP)

In RS232 mode, data is sent via two lines. A separate line is available for the send direction and the receive direction. Simultaneous sending and receiving is possible (full duplex).

#### RS232 signals

In addition to the TXD, RXD and GND signals, the communication module provides additional RS232 signals when using RS232 hardware:

|  |  |  |
| --- | --- | --- |
| **TXD** | Output | Transmitted data;  Interface is transmitting |
| **RXD** | Input | Received data;  Interface is receiving |
| **GND** |  | Shared ground reference (ground);   isolated |
| **DCD** | Input | Data carrier detect;  Carrier signal when connecting a modem. The communication partner signals that it recognizes incoming data. |
| **DTR** | Output | Data terminal ready;  DTR set to "ON": Communication module switched on, ready for operation  DTR set to "OFF": Communication module not switched on, not ready for operation |
| **DSR** | Input | Data set ready;  DSR set to "ON": Communication partner signals readiness for operation  DSR set to "OFF": Communication partner not switched on, not ready for operation |
| **RTS** | Output | Request to send;  RTS set to "ON": Communication module ready to send; signals to the communication partner that there is data ready to send  RTS set to "OFF": Communication module not ready to send |
| **CTS** | Input | Clear to send;  Communication partner can receive data from the communication module (response to RTS = ON of the communication module)  CTS set to "ON": Signals readiness to receive to the communication partner  CTS set to "OFF": Signals "Not ready to receive" to the communication partner |
| **RI** | Input | Incoming call for connecting a modem (ring indicator) |

After power on of the communication module, the output signals are in the OFF state (inactive).

You configure the operation of the DTR/DSR and RTS/CTS control signals in the user interface of the communication module.

The RS232 signals cannot be influenced in case of:

- configured data flow control "Hardware RTS always switched"

  (corresponds to automatic operation of the accompanying signals)
- configured data flow control "Hardware RTS always ON"

  (corresponds to hardware flow control with RTS/CTS)
- configured data flow control "Hardware RTS always ON, ignore DTR/DSR"

For more information, refer to chapter [Handshake procedure](#handshake-procedure-s7-1500).

#### Connecting cables

The following standard connecting cables of various lengths are available for connecting to a communication partner which also has a 9-pin D-sub male connector:

| Article number | 6ES7902-1AB00-0AA0 | 6ES7902-1AC00-0AA0 | 6ES7902-1AD00-0AA0 |
| --- | --- | --- | --- |
| Product type designation | S7 connecting cable RS232 |  |  |
| Cable length | 5 m | 10 m | 15 m |

The table below shows the pin assignment for the 9-pin D-sub male connector of the respective communication module.

| Male connector* | Pin | Designation | Input/ output | Required/optional for self-fabrication |
| --- | --- | --- | --- | --- |
| ![Connecting cables](images/105034563979_DV_resource.Stream@PNG-de-DE.png) | 1 | DCD | Input | Optional |
| 2 | RXD | Input | Required |  |
| 3 | TXD | Output | Required |  |
| 4 | DTR | Output | Optional |  |
| 5 | GND | — | Required |  |
| 6 | DSR | Input | Optional |  |
| 7 | RTS | Output | Optional |  |
| 8 | CTS | Input | Optional |  |
| 9 | RI | Input | Optional |  |
| * View from the front |  |  |  |  |

The cable or the connector of the listed connecting cables are not available for order as separate items. If you fabricate your own connecting cables you must remember that unconnected inputs at the communication partner may have to be connected to open-circuit potential.

Note that you may only use shielded connector enclosures. A large surface area of the cable shield must be in contact with the connector enclosure on both ends.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Never connect cable shield with GND**  Never connect the cable shield with the GND as this could destroy the interfaces. GND must always be connected on both sides (pin 5), otherwise the interface modules could be destroyed. |  |

The figure below illustrates the cable for a point-to-point connection between a communication module and a communication partner.

![Connecting cables](images/171509615883_DV_resource.Stream@PNG-en-US.png)

### RS422 mode (S7-1500)

The following communication modules support RS422 mode:

- CM PtP RS422/485 BA
- CM PtP RS422/485 HF
- CM PtP (ET 200SP)

In RS422 mode, data is transmitted via two line pairs (four-wire operation). A separate line pair is available for the send direction and the receive direction. Simultaneous sending and receiving is possible (full duplex).

The data can be exchanged simultaneously between two or more communication partners. In RS422 multipoint mode, only one slave may send data at any given time.

#### Interface operating modes

The following table is a summary of the interface operating modes for the various communication modules and protocols.

The communication module can be used in the following topologies in RS422 mode:

- Link between two nodes: Point-to-point connection
- Link between several nodes: Multipoint connection  
  (only available with CM PtP (ET 200SP))

| Operating mode | Description |
| --- | --- |
| Full duplex (RS422) four-wire operation (point-to-point connection) | Both devices have the same priority in this operating mode. |
| Full duplex (RS422) four-wire operation (multipoint master) | The communication module can be used as multipoint master. |
| Full duplex (RS422) four-wire operation (multipoint slave) | The communication module can be used as multipoint slave. |

The following applies for a multipoint master/slave topology in RS422 mode:

- The sender of the master is interconnected with the receivers of all slaves.
- The senders of the slaves are interconnected with the master's receiver.
- Only the receiver of the master and the receiver of one slave have a default setting. All other slaves operate without default settings.

#### RS422 signals

The following signals are present on the communication module when using the RS422 hardware:

|  |  |  |
| --- | --- | --- |
| **T (A) -** | Output | Transmitted data |
| **T (B) +** | Output | Transmitted data |
| **R (A) -** | Input | Received data |
| **R (B) +** | Input | Received data |
| **GND** |  | Functional ground; isolated |

#### Connecting cables

The following standard connecting cables of various lengths are available for connecting to a communication partner which also has a 15-pin D-sub female connector:

| Article number | 6ES7902-3AB00-0AA0 | 6ES7902-3AC00-0AA0 | 6ES7902-3AG00-0AA0 |
| --- | --- | --- | --- |
| Product type designation | S7 connecting cable RS422 |  |  |
| Cable length | 5 m | 10 m | 50 m |

The table below shows the pin assignment of the 15-pin D-sub female connector of the respective communication module.

| Socket<sup>*</sup> | Pin | Designation | Input/output |
| --- | --- | --- | --- |
| ![Connecting cables](images/105034579851_DV_resource.Stream@PNG-de-DE.png) | 1 | - | - |
| 2 | T (A) - | Output |  |
| 3 | - | - |  |
| 4 | R (A) - | Input |  |
| 5 | - | - |  |
| 6 | - | - |  |
| 7 | - | - |  |
| 8 | GND | - |  |
| 9 | T (B) + | Output |  |
| 10 | - | - |  |
| 11 | R (B) + | Input |  |
| 12 | - | - |  |
| 13 | - | - |  |
| 14 | - | - |  |
| 15 | - | - |  |
| * View from the front |  |  |  |

The cable or the connector of the listed connecting cables are not available for order as separate items. If you fabricate your own connecting cables you must remember that unconnected inputs at the communication partner may have to be connected to open-circuit potential.

Note that you may only use shielded connector enclosures. A large surface area of the cable shield must be in contact with the connector enclosure on both ends.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Never connect cable shield with GND**  Never connect the cable shield with the GND as this could destroy the interfaces. GND must always be connected on both ends (pin 8), otherwise the interface modules could be destroyed. |  |

The figure below illustrates the cable for a point-to-point connection between a communication module and a communication partner.

![Connecting cables](images/106909207563_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> This cable type can be used in the following lengths for a communication module as communication partner: max. 1200 m at 19200 baud, max. 500 m at 38400 baud, max. 350 m at 76800 baud, max. 250 m at 115200 baud.

### RS485 mode (S7-1500)

The following communication modules support RS485 mode:

- CM PtP RS422/485 BA
- CM PtP RS422/485 HF
- CM PtP (ET 200SP)

In RS485 mode, data is transmitted via one line pair (two-wire operation). The line pair is available alternately for the send and receive directions. It is possible to either send or receive (half duplex). On completion of a send operation, operation is immediately switched to receive mode (ready to receive). Send mode is reset again as soon as a new send job is received.

#### Interface operating modes

The following table is a summary of the interface operating modes for the various communication modules and protocols.

| Operating mode | Description |
| --- | --- |
| Half duplex (RS485) two-wire operation | Operating mode for point-to-point connection or multipoint connection (multipoint) in two-wire operation. The communication module can be the master as well as the slave. |

If you operate the Freeport in RS485 mode (half duplex, two-wire operation), you must make provisions in the user program to ensure that only one device sends data at any given time. If more than one device sends data at the same time, the frames are corrupted.

Modbus automatically ensures that only one device is sending.

#### Changeover times for RS485 communication module in half duplex mode

A maximum time of 0.1 ms is set for the changeover between sending and receiving.

#### RS485 signals

The following signals are present on the communication module when using the RS485 hardware:

|  |  |  |
| --- | --- | --- |
| R (A)/T (A) - | Input/output | Received/transmitted data |
| R (B)/T (B) + | Input/output | Received/transmitted data |
| GND |  | Functional ground; isolated |

#### Connecting cables

The table below shows the pin assignment of the 15-pin D-sub female connector of the respective communication module.

| Socket* | Pin | Designation | Input/output |
| --- | --- | --- | --- |
| ![Connecting cables](images/105034579851_DV_resource.Stream@PNG-de-DE.png) | 1 | - | - |
| 2 | - | - |  |
| 3 | - | - |  |
| 4 | R (A)/T (A) - | Input/output |  |
| 5 | - | - |  |
| 6 | - | - |  |
| 7 | - | - |  |
| 8 | GND | - |  |
| 9 | - | - |  |
| 10 | - | - |  |
| 11 | R (B)/T (B) + | Input/output |  |
| 12 | - | - |  |
| 13 | - | - |  |
| 14 | - | - |  |
| 15 | - | - |  |
| * View from the front |  |  |  |

When fabricating the connecting cables, you need to remember that unconnected inputs at the communication partner may have to be connected to open-circuit potential.

Note that you may only use shielded connector enclosures. A large surface area of the cable shield must be in contact with the connector enclosure on both ends.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Never connect cable shield with GND**  Never connect the cable shield with the GND as this could destroy the interfaces. GND must always be connected on both ends (pin 8), otherwise the interface modules could be destroyed. |  |

The figure below illustrates the cable for a point-to-point connection between a communication module and a communication partner.

![Connecting cables](images/106909211147_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> This cable type can be used in the following lengths for a communication module as communication partner: max. 1200 m at 19200 baud, max. 500 m at 38400 baud, max. 350 m at 76800 baud, max. 250 m at 115200 baud, max. 200 m at 250000 baud.

### Handshake procedure (S7-1500)

#### Introduction

Handshaking controls the data flow between two communication partners. The use of the handshaking method prevents data loss during transmission if the devices are operating at different speeds.

We can basically distinguish between the following methods:

Overview of methods and interfaces

| Method | RS232 | RS422 | RS485 |
| --- | --- | --- | --- |
| Software data flow control XON/XOFF | X | X | ‑ |
| Hardware data flow control (RTS/CTS) | X | ‑ | ‑ |
| Automatic operation of accompanying signals | X | ‑ | ‑ |
|  |  |  |  |

#### Software data flow control

Software data flow control is implemented as follows on the communication module:

- **XON/XOFF**

  - As soon as the communication module has been set to the "XON/XOFF" operating mode by means of parameter assignment, it sends the XON character, thereby allowing the communication partner to send data.
  - On reaching the configured maximum number of frames, or 16 characters ahead of receive buffer overflow, the communication module sends the XOFF character, thereby requesting that the communication partners stop sending. If the communication partner nonetheless continues to send data, an error message is generated if the receive buffer overflows. Data received in the last frame is discarded.
  - As soon as a frame has been fetched by the CPU and the receive buffer is ready to receive data again, the communication module sends the XON character.
  - If the communication module receives the XOFF character during sending, it cancels the current send operation until it receives a XON again from its communication partner. If no XON is received within a specific configurable time, send operation is canceled and a corresponding error message is output.

    > **Note**
    >
    > You can configure the characters for XON and XOFF (any ASCII character).
    >
    > During parameter assignment of the XON/XOFF software data flow control, user data may not contain any of the configured XON or XOFF characters.

#### Hardware data flow control

> **Note**
>
> The DTR/DSR signals do not have to be wired for "Hardware RTS always ON, ignore DTR/DSR" parameter assignment.
>
> If "Hardware RTS always ON" is configured, it is imperative that you fully wire the interface signals used. Make sure that the local RTS (out) is connected with the CTS (in) of the communication partner and the local CTS is connected with the RTS of the communication partner. Accordingly, the local DTR must be connected with the DSR of the communication partner and the local DSR with the DTR of the communication partner.

![Wiring of the interface signals](images/44377361675_DV_resource.Stream@PNG-de-DE.png)

Wiring of the interface signals

- **Hardware RTS always ON, ignore DTR/DSR**

  - As soon as the communication module has been set to an operating mode with "Hardware RTS always ON" through parameter assignment, it outputs the RTS = ON signal to the communication partner to indicate its ready state.
  - RTS is set to OFF as soon as the configured maximum number of frames or 16 characters before buffer overflow is reached.  
    If the communication partner nonetheless continues to send data, an error message is generated on overflow of the receive buffer. Data received in the last frame is discarded.
  - RTS is reset to ON as soon as the frame has been fetched by the CPU and the receive buffer is ready to receive data again.
  - If CTS switches to OFF during the send operation, the communication module interrupts the send operation until CTS is reset to ON. If CTS is not reset to ON within a specific configurable time, the send operation is canceled and a corresponding error message is output.
- **Hardware RTS always ON**

  The "Hardware RTS always ON" mode corresponds to the "Hardware RTS always ON, ignore DTR/DSR" mode. However, you also need to wire DTR and DSR.

  - As soon as the communication module has been set set to an operating mode with "Hardware RTS always ON" through parameter assignment, it sets DTR = ON and RTS = ON to signal its general ready state to the communication partner.
  - RTS is set to OFF as soon as the configured maximum number of frames or 16 characters before buffer overflow is reached.  
    If the communication partner nonetheless continues to send data, an error message is generated on overflow of the receive buffer. Data received in the last frame is discarded.
  - RTS is reset to ON as soon as the frame has been fetched by the CPU and the receive buffer is ready to receive data again.
  - If CTS switches to OFF during the send operation, the communication module interrupts the send operation until CTS is reset to ON. If CTS is not reset to ON within a specific configurable time, the send operation is canceled and a corresponding error message is output.
  - A switch from DSR = ON to DSR = OFF cancels an active send job and triggers an error message.

#### Automatic operation of accompanying signals

- **Hardware RTS always switched**

  "Hardware RTS always switched" is implemented as follows on the communication module:

  - As soon as the communication module is set to the operating mode with "Hardware RTS always switched" through parameter assignment, it sets the line RTS to OFF and DTR to ON (communication module ready for operation).

    It is not possible to send frames until the DSR line is set to ON. No data is sent via the RS232C interface as long as DSR is set to OFF. A send job is canceled and a corresponding error message is generated.
  - When a send job is pending, RTS is set to ON and the configured RTS ON delay starts. On expiration of the data output time, the system checks whether the communication partner has set CTS to ON. If so, the data is sent via the RS232 interface.
  - If the CTS line is not set to ON within the RTS ON delay, or if CTS changes to OFF during transmission, the send job is aborted and an error message is generated.
  - Once the data has been sent and the configured clear RTS OFF delay has elapsed, the RTS line is set to OFF. The system does not wait for CTS to change to OFF.
  - It is always possible to receive data via the RS232 interface. There will be no reaction if there is a danger of the receive buffer of the communication module overflowing.
  - A switch from DSR = ON to DSR = OFF cancels an active send job and triggers an error message.

    > **Note**
    >
    > Set the "RTS ON delay" in such a way that the communication partner is able to enter the ready to receive state before the time elapses.
    >
    > Set the "RTS OFF delay" in such a way that the communication partner is able to receive the last characters of the frame completely before RTS is set to OFF and the send request is canceled.

    > **Note**
    >
    > When automatic operation of the RS232 signals is configured, RTS and DTR cannot be controlled by means of the corresponding instruction!

#### Time diagram

The figure below shows the chronological sequence of a send job with configured data flow control "Hardware RTS always switched":

![Time diagram for Hardware RTS always switched](images/42585746187_DV_resource.Stream@PNG-en-US.png)

Time diagram for Hardware RTS always switched

#### Additional information

> **Note**
>
> Operation of DTR/DSR or RTS/CTS is accepted by the communication module with the following settings:
>
> - Hardware RTS always ON, ignore DTR/DSR
> - Hardware RTS always ON
> - Hardware RTS always switched

## Configuring / parameter assignment  (S7-1500)

This section contains information on the following topics:

- [Configuring / parameter assignment of a communication module (S7-1500)](#configuring-parameter-assignment-of-a-communication-module-s7-1500)
- [Special features for the use of the option for performance optimization (S7-1500)](#special-features-for-the-use-of-the-option-for-performance-optimization-s7-1500)
- [Communication using Freeport (S7-1500)](#communication-using-freeport-s7-1500)
- [Communication using 3964(R) (S7-1500)](#communication-using-3964r-s7-1500)
- [Communication through Modbus RTU (S7-1500)](#communication-through-modbus-rtu-s7-1500)
- [Communication using USS (S7-1500)](#communication-using-uss-s7-1500)

### Configuring / parameter assignment of a communication module (S7-1500)

The following sections contain explanations on the following protocols and their parameters:

- [Communication using Freeport](#communication-using-freeport-s7-1500)
- [Communication using 3964(R)](#communication-using-3964r-s7-1500)
- [Communication through Modbus RTU](#communication-through-modbus-rtu-s7-1500)
- [Communication using USS](#communication-using-uss-s7-1500)

This information is required to carry out the parameter assignment and subsequently programming of the communication in accordance with the used protocol.

Configuration and parameter assignment are carried out in the device view of STEP 7 (TIA Portal) and in the properties dialog of the communication module. Some configurations can also be changed during runtime by means of the corresponding "Config" instructions (Port_Config, Send_Config, Receive_Config, P3964_Config).

#### Procedure for setting up point-to-point communication

The procedure does not depend on the communication module used.

1. In the device view of the STEP 7 (TIA Portal) hardware editor configure an S7-1500 structure with CPU and communication module.
2. You assign the parameters of the communication module interface (protocol, protocol parameters, addresses) in the "General" area of the "Properties" tab.

### Special features for the use of the option for performance optimization (S7-1500)

From firmware version V2.0 of the communication module, the option for performance optimization is available. This option is suitable if you are exclusively sending and receiving short frames with several communication modules.

The following overview shows the most important differences between not using and using the Performance option:

| Without performance optimization (Universal) | With performance optimization |
| --- | --- |
| Limiting the telegram length depending on the communication module to 1, 2, or 4 KB | Limiting the telegram length to 24 bytes for receive frames and 30 bytes for send frames. Longer frames are rejected. |
| Transmitting a frame requires several cycles of the CPU. The number of cycles increases with the number of communication modules that communicate via data record. | Transmission of a frame requires an application cycle of the CPU and several communication modules can be served in parallel (reaction time optimized, timing behavior improved). |
| Allocation of an address range of 8 bytes of input data and 0 bytes of output data | Allocation of an address range of 32 bytes of input data and 32 bytes of output data |
| Available from firmware version V1.0 of the communication module | Available from firmware version V2.0 of the communication modules |
| Configuration and parameter assignment in the device view of STEP 7 (TIA Portal) and in the Properties dialog of the communication module. The option for performance optimization cannot be changed with "Config" instructions (Port_Config, Send_Config,Receive_Config, P3964_Config). |  |
| Available as of version V1.0 of the instruction libraries PtP Communication, USS Communication and MODBUS (RTU) | Available as of version V4.0 of the instruction library PtP Communication and V5.0 of the instruction libraries USS Communication and MODBUS (RTU) |

> **Note**
>
> **Modbus RTU**
>
> With communication via Modbus RTU with activated performance optimization, there are [restrictions to the configuration limits of the transferred data](#function-codes-s7-1500).

### Communication using Freeport (S7-1500)

This section contains information on the following topics:

- [Procedure for establishing a serial connection with Freeport (S7-1500)](#procedure-for-establishing-a-serial-connection-with-freeport-s7-1500)
- [Data transmission with Freeport (S7-1500)](#data-transmission-with-freeport-s7-1500)
- [Sending data with Freeport (S7-1500)](#sending-data-with-freeport-s7-1500)
- [Receiving data with Freeport (S7-1500)](#receiving-data-with-freeport-s7-1500)
- [Code transparency (S7-1500)](#code-transparency-s7-1500)
- [Receive buffer (S7-1500)](#receive-buffer-s7-1500)
- [Communication via DMX512 (S7-1500)](#communication-via-dmx512-s7-1500)

#### Procedure for establishing a serial connection with Freeport (S7-1500)

##### Requirements

- The hardware is set up and there is an electrical connection to the link partner.
- The project has been created in STEP 7 (TIA Portal) and the CPU has been inserted into the hardware configuration.

##### Procedure - Hardware configuration

1. Insert the CM PtP communication module into the hardware configuration.
2. Set the communication parameters according to the link partner:

   For example, transmission speed, character frame, frame start and frame end

   These parameters are transferred to the CM PtP communication module every time the CPU is started.

##### Procedure - Programming

1. Create the data structure that is to include the data to be transferred.

**Sending data**

1. Insert the instructions from the PtP Communication library: Send_P2P for sending data
2. Interconnect the input and output parameters of the instruction, e.g.:

   - HWID from the system tags at the PORT input
   - Data structure with the data to be sent at the BUFFER input

   Note: During operation, each positive edge at the REQ input will send the specified data area once. The block must be called until DONE indicates that the data was transferred to the module.

   In case of an error, setting ERROR once and displaying the corresponding information in STATUS indicates that the data was not transferred.

**Receiving data:**

1. Insert the instructions from the PtP Communication library: Receive_P2P for sending data
2. Interconnect the input and output parameters of the instruction, e.g.:

   - HWID from the system tags at the PORT input
   - Data structure for storage of received data at the BUFFER input

   Note: A high level at the NDR output during operation indicates that new data was received and stored in the specified data area. The block must be called until NDR=TRUE. The received data can then be analyzed and the RECEIVE_P2P can be called again.

##### **Optional additions**

- Instructions that end in _Config can be used optionally to change the parameters of the hardware configuration during operation of the user program. The changes are not saved in the hardware configuration. They are overwritten at the next restart.
- The instructions Signal_Set and Signal_Get can be used to control the RS232 accompanying signals individually if automatic operation is not a suitable option.

#### Data transmission with Freeport (S7-1500)

##### Introduction

Freeport is a freely programmable frame-based protocol that is also known as ASCII protocol.

The Freeport protocol controls data transmission by means of a point-to-point connection between the communication module and a communication partner. The Freeport protocol contains the physical layer (Layer 1).

The Freeport protocol supports sending and receiving of messages with any structure (all characters from 00H through FFH (for character frames with 8 data bits) or from 00H through 7FH (for character frames with 7 data bits)).

The frame start and end criteria must be configured both for the send and the receive direction. The start and end criteria can be configured differently.

Instructions are available for communication with a communication partner (see [Overview of PtP programming](#overview-of-point-to-point-programming-s7-1500)).

#### Sending data with Freeport (S7-1500)

##### Specifying settings for sending

To send a message, the partner must be informed of the start and end of the message. These settings can be permanently set in the hardware configuration or can be adjusted during runtime by using the instruction Send_Config. You can select one of the following options or also combine them:

- Send break before frame start

  You can specify that an additional Break is sent at the beginning of each message transmission on expiration of the RTS ON delay time.  
  The duration of the "Break" is specified in bit times.

  Compliance with the send break can be deactivated if other mechanisms are used for synchronization.
- Send idle line

  You can specify that an additional "Idle Line" signal is output at the start of each message transmission.   
  The duration of the "Idle Line" is specified in bit times.

  Compliance with the send break can be deactivated if other mechanisms are used for synchronization.
- RTS ON delay

  You can configure the time that has to expire after the RTS (Request to send) before the actual data transmission starts (RS232 only).
- RTS OFF delay

  You can configure the time that has to expire after transmission has been completed before the RTS signal is deactivated (RS232 only).
- Send up to and including the end delimiter

  You can configure the number of end delimiters (1 or 2) and their value.

  All data up to the end delimiter(s) is sent, independent of the selected frame length. The end delimiter must be included in the data to be sent. Data is sent only up to and including the delimiter, even if the specified data length is longer.
- Number of appended characters

  Input of the number of appended characters. Sending takes place up to the configured length. The end delimiter(s) is/are appended automatically. Depending on the number of end delimiters, one to five characters more than the number specified at the instruction are sent to the partner.

  > **Note**
  >
  > If you combine "Send break before frame start", "Send idle line" and "RTS ON delay", these are processed in the order "RTS ON delay", "Send break before frame start" and "Send idle line".

#### Receiving data with Freeport (S7-1500)

##### Specifying the message start

For data transmission with Freeport, you can choose between several different start criteria. The start criterion defines when a frame starts. Once a criterion that indicates the start of the message is met, the data stream is scanned for message end criteria. Here you select the settings that correspond to the properties of the sending communication partner.

Two different methods are available for detecting the message start:

- **Start on any character**

  Any character can be used to define the start of the message (default).

  This means that the first character sent at the start of communication, or after the frame end has been detected, will be identified as the first character of a message.
- **Start on special condition**

  The start of the message is detected based on the following specified conditions.

  - **After detection of a line break**

    The frame start is not accepted unless a break has been received beforehand, in other words, it is compulsory for the partner to send a break before sending a frame.
  - **After detection of an idle line**

    The frame start is not accepted until the configured idle line duration has expired. This procedure requires a minimum interval between two frames.
  - **After receipt of a start character**

    The frame start is detected when the configured start character is identified.
  - **After detection of one or several start sequences**

    The frame start is detected when the configured string with a length of up to five characters is identified. You can configure up to 4 start sequences. The start sequences that are up to 5 characters long can also contain "don't care characters".

**Example:**

Configured start conditions

| Start condition | 1st character | 2nd character | 3rd character | 4th character | 5th character |
| --- | --- | --- | --- | --- | --- |
| 1 | 0x68 | xx | xx | 0x68 | xx |
| 2 | 0x10 | 0xaa | xx | xx | xx |
| 3 | 0xdc | 0xaa | xx | xx | xx |
| 4 | 0xe5 | xx | xx | xx | xx |
| : |  |  |  |  |  |
|  |  |  |  |  |  |

The following message has been received: 68 10 aa 68 bb 10 aa 16

The evaluation of the start criteria begins with the receipt of the first character 0x68.   
The 2nd and 3rd characters are free.   
When the 4th character (second 0x68) is received, the first start condition is met and further evaluation of the message begins.

##### Specifying the message end

You can choose from several different end criteria for data transmission using the Freeport protocol. The end criterion defines the point at which a frame has been received completely.

Configurable end criteria are:

- **Recognize message end by message timeout**
- **Recognize message end by response timeout**
- **After character delay time elapses (default)**
- **After receipt of a fixed frame length**
- **After receipt of a maximum number of characters**
- **Read message length from message**
- **After receipt of an end sequence**

##### Message timeout

When data is received, the end of frame is detected on expiration of the configured time for transferring a frame. Time measurement starts after the start criterion has been met.

##### Response timeout

The response time is used to monitor the response behavior of the communication partner. If a valid frame start is not recognized after the completion of a send job, the send job is acknowledged with a corresponding message.

The actual end criterion has to be configured additionally.

##### Expiration of character delay time

When data is received, the frame end is detected when the configured maximum time between successive characters is exceeded (character delay time). The value is specified in bit times.

In this case, the character delay time must be set in such a way as to ensure that it expires between two consecutive frames. However, it should be of sufficient length to exclude incorrect identification of the end of the frame whenever the communication partner performs a transmission pause within a frame.

> **Note**
>
> For higher data transfer speeds, a value of at least 100 bit times is recommended.

##### Fixed frame length

When data is received, the end of the frame is identified after the configured frame length has been reached.

An error message is output and the frame is discarded if the character delay time expires (if activated) before the fixed frame length has been reached.

Please note the following if the frame length of the received characters does not match the fixed configured frame length:

- All characters received after the fixed configured frame length has been reached will be discarded until a new start criterion is detected.
- An error message is output and the frame is discarded if another (activated) end criterion is met before the fixed frame length has been reached.

##### Maximum number of characters

When receiving data, the end of the frame is recognized after the declared number of characters have arrived.

This setting can be combined with the "Character delay time" settings. The frame received is also assessed as free of error if another end condition occurs, regardless of whether the maximum number of characters has been reached.

Please note the following if the frame length of the received characters does not match the configured maximum frame length:

- All characters received after the configured maximum number of characters has been reached will be discarded until a new start criterion (e.g. "Idle Line") is detected.
- If a different (activated) end criterion is met before the configured maximum number of characters has been reached, this "frame part" is assessed as a valid frame and the partner waits for a new start criterion. All characters received prior to fulfillment of a new start criterion are discarded.

  > **Note**
  >
  > If no further end criterion is activated, the fixed frame length and maximum number of characters will respond in the same way.

##### Message length in the message

When data is received, the frame end is detected when the frame length sent with the received frame has been reached.

The following parameters define the characters to be used for evaluation of the message length:

- **Offset of length field in message**

  In the message, the value defines the position of the character that is to be used to determine the message length.

  You can set values from 0 to 4095 characters, depending on the buffer size.
- **Size of length field**

  This value specifies the number of characters as of the first evaluation position to be used to determine the message length.

  You can set values of 1, 2 and 4 characters.
- **Number of characters not counted in length specification**

  Number of characters appended to the frame without counting towards the frame length. This value defines the number of bytes at the end of the frame which should not be included in the evaluation of the message length.

  You can set values from 0 to 255 characters.

**Example:**

Parameter assignments for "Message length in the message"

| Symbol | Meaning |
| --- | --- |
| Offset of length field in message: | 3rd byte ("2" has to be configured as offset) |
| Size of length field: | 1 byte |
| Number of characters not counted in length specification: | 3 bytes |

| Message |  |  |  |  | Number of characters not counted in length specification |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Start character | Address | Length field |  |  | Checksum | End delimiter |  |
| Byte 1 | Byte 2 | Byte 3 | Byte ... | Byte X | Byte X+1 | Byte X+2 | Byte X+3 |

##### End sequence

When data is received, the end of the frame is identified when the configured end sequence (max. 5 characters) is received. The end sequence which is up to 5 characters long can also contain "don't care characters". The received data is applied by the CPU, including the end sequence.

If you are working with the end sequence, transmission is not code-transparent and you must exclude the presence of end code in the user data.

> **Note**
>
> **Frame end sequence**
>
> If there is only one end delimiter, the entry **must** take place in the 5th line.
>
> If there are two end delimiters, the entries **must** take place in the 4th and 5th line (no gaps).
>
> The same applies to the use of additional characters.

#### Code transparency (S7-1500)

##### Code transparency

Code-transparent means that any character combinations can occur in the user data without the end criterion being recognized.

The code transparency of the procedure depends on the selection of the configured end criterion and flow control:

- With specified end sequence or using XON/XOFF flow control

  - Not code-transparent
- End criterion character delay time, fixed frame length, maximum frame length, message timeout, or response timeout and message length in the message

  - Code-transparent

#### Receive buffer (S7-1500)

##### Receive buffer of the module

The communication modules have a receive buffer that stores the received frames temporarily until they are transmitted to the CPU. The receive buffer is implemented as a ring buffer, which means the frames are transmitted to the CPU in the order in which they were received until the receive buffer is full. If additional frames are received once the buffer is full, the oldest frame is overwritten. If "Prevent overwriting" was configured, a corresponding message is generated when the receive buffer is full. All further frames are rejected until the receive buffer is ready to receive new ones.

During the parameter assignment, you can specify whether the receive buffer should be deleted during startup. You can also specify the range of values (1 to 255) for the number of buffered receive frames.

The receive buffer of the module may have a size of up to 8 KB, depending on the communication module used (see chapter [Introduction](#introduction-s7-1500)). The frame has a maximum length of 4 KB. This means that each communication module is capable of buffering at least two frames.

If you always want to transfer the last frame received to the CPU, you must set the value "1" for the number of buffered frames and deactivate overwrite protection.

> **Note**
>
> If continuous reading of the received data in the user program is interrupted for a certain time, you may find when the receive data is requested again, that the communication module first sends older frames before the CPU receives the most recent one. At the time of interruption, the old frame had already been transmitted from the receive buffer of the communication module and prepared for transmission to the CPU.

#### Communication via DMX512 (S7-1500)

You can use the ET 200SP CM PtP (from firmware version V1.0.5) communication module for communication via DMX512 (Digital Multiplex). For communication via DMX512, the use of the performance optimization option is also possible, provided you use the max. value 29<sub>D</sub> as the highest address.

You can find more information on setting up a DMX512 connection in the FAQ with the entry ID [109778975](https://support.industry.siemens.com/cs/ww/en/view/109778975) in Siemens Industry Online Support.

### Communication using 3964(R) (S7-1500)

This section contains information on the following topics:

- [Procedure for establishing a serial connection with 3964(R) (S7-1500)](#procedure-for-establishing-a-serial-connection-with-3964r-s7-1500)
- [Data transmission with 3964(R) procedure (S7-1500)](#data-transmission-with-3964r-procedure-s7-1500)
- [Control characters (S7-1500)](#control-characters-s7-1500)
- [Block check character (S7-1500)](#block-check-character-s7-1500)
- [Sending data with 3964(R) (S7-1500)](#sending-data-with-3964r-s7-1500)
- [Receiving data with 3964(R) (S7-1500)](#receiving-data-with-3964r-s7-1500)

#### Procedure for establishing a serial connection with 3964(R) (S7-1500)

##### Requirements

- The hardware is set up and there is an electrical connection to the link partner.
- The project has been created in STEP 7 (TIA Portal) and the CPU has been inserted into the hardware configuration.

##### Procedure - Hardware configuration

1. Insert the CM PtP communication module into the hardware configuration.
2. Set the communication parameters according to the link partner:

   For example, transmission speed, character frame, frame start and frame end

   These parameters are transferred to the CM PtP communication module every time the CPU is started.

##### Procedure - Programming

1. Create the data structure that is to include the data to be transferred.

**Sending data**:

1. Insert the instructions from the PtP Communication library: Send_P2P for sending data
2. Interconnect the input and output parameters of the instruction, e.g.:

   - HWID from the system tags at the PORT input
   - Data structure with the data to be sent at the BUFFER input

   Note: During operation, each positive edge at the REQ input will send the specified data area once. The block must be called until DONE indicates that the data was transferred to the module.

   In case of an error, setting ERROR once and displaying the corresponding information in STATUS indicates that the data was not transferred.

**Receiving data:**

1. Insert the instructions from the PtP Communication library: Receive_P2P for sending data
2. Interconnect the input and output parameters of the instruction, e.g.:

   - HWID from the system tags at the PORT input
   - Data structure for storage of received data at the BUFFER input

   Note: A high level at the NDR output during operation indicates that new data was received and stored in the specified data area. The block must be called until NDR=TRUE. The received data can then be analyzed and the RECEIVE_P2P can be called again.

##### Optional additions

- Instructions that end in _Config can be used optionally to change the parameters of the hardware configuration during operation of the user program. The changes are not saved in the hardware configuration. They are overwritten at the next restart.
- The instructions Signal_Set and Signal_Get can be used to control the RS232 accompanying signals individually if automatic operation is not a suitable option.

#### Data transmission with 3964(R) procedure (S7-1500)

##### Introduction

The 3964(R) procedure controls point-to-point data exchange between the communication module and a communication partner and contains both the physical layer (layer 1) and the link layer (layer 2).

Instructions are available for communication with a communication partner (see [Overview of PtP programming](#overview-of-point-to-point-programming-s7-1500)).

#### Control characters (S7-1500)

##### Introduction

During data transmission, the 3964(R) procedure adds control characters to the information data (link layer). The communication partner can use these control characters to check whether it has received all data completely and without errors.

##### Control characters of the 3964(R) procedure

The 3964(R) procedure evaluates the following control characters:

|  |  |  |  |
| --- | --- | --- | --- |
| **STX** | Start of Text | Beginning of the character string to be transmitted | 02H |
| **DLE** | Data Link Escape | Data transmission changeover | 10H |
| **ETX** | End of Text | End of the character string to be transmitted | 03H |
| **NAK** | Negative Acknowledge | Negative acknowledgment | 15H |
| **BCC** | Block Check Character (only with 3964R) | Block check character |  |

BCC is formed and monitored automatically in the communication module. The block check character is not transmitted as frame content to the CPU.

> **Note**
>
> If the DLE character is transmitted as an information character within a frame, it is sent twice (DLE duplication) to distinguish it from the DLE control character during connection establishment and termination. The receiver reverses the DLE duplication.

##### Priority

With the 3964(R) procedure, one communication partner must be assigned a higher and the other a lower priority. If both partners start to establish a connection at the same time, the partner having lower priority will cancel its send job.

#### Block check character (S7-1500)

##### Block check character

With the 3964R transfer protocol, data security is enhanced by sending an additional block check character (BCC = Block Check Character).

The block check character is the even longitudinal parity (EXOR logic operation of all data bytes) of a sent or received block. Its calculation begins with the first byte of user data (first byte of the frame) after the connection establishment, and ends after the DLE ETX character at connection termination.

> **Note**
>
> With DLE duplication, the DLE character is included twice in the BCC calculation.

#### Sending data with 3964(R) (S7-1500)

##### Connection establishment for sending

The 3964(R) procedure sends the STX control character to set up the connection. If the communication partner responds with the DLE character before the acknowledgment delay time expires, the procedure switches to send mode.

If the communication partner answers with NAK or any other character (except for DLE or STX), or the acknowledgment delay time expires without a response, the procedure tries to set up the connection again. After the configured number of unsuccessful setup attempts, the procedure cancels the connection setup and sends the NAK character to the communication partner. The communication module outputs a corresponding error message.

##### Sending data

If the connection is successfully established, the user data contained in the output buffer of the communication module is sent to the communication partner with the selected transmission parameters (a DLE recognized in the user data is doubled during the send job). The communication partner monitors the time intervals between the incoming characters. The interval between two characters must not exceed the character delay time. Monitoring of the character delay time starts immediately after the connection has been established.

If the communication partner sends the NAK character during an active send operation, the procedure cancels the block and repeats it as described above, beginning with connection establishment. If a different character is sent, the procedure first waits for the character delay time to expire and then sends the NAK character to set the communication partner to idle state. Then, the procedure restarts sending with the connection setup STX.

##### Connection termination during sending

Once the contents of the buffer have been sent, the procedure appends the DLE and ETX characters and (only with 3964R) the block checksum BCC as the end identifier, and then waits for an acknowledgment character. If the communication partner sends the DLE characters within the acknowledgment delay time, the data block has been received without errors. If the communication partner responds with NAK, any other character (except DLE), or with a corrupted character, or if the acknowledgment delay time expires without a response, the procedure restarts sending with the connection setup STX.

After the configured number of attempts to send, the procedure stops the process and sends an NAK to the communication partner. The communication module outputs a corresponding error message.

#### Receiving data with 3964(R) (S7-1500)

##### Connection setup for receiving

In idle state, when there is no send job to be processed, the procedure waits for the communication partner to set up the connection.

A wait time is started (wait time = acknowledgment delay time - 10 ms, however, maximum of 400 ms) if no free receive buffer is available during the connection setup with STX. An error message is generated if no free receive buffer is available on expiration of this time. The procedure sends the NAK character and returns to the idle state. Otherwise, the procedure sends a DLE and receives the data as described above.

The acknowledgment delay time should be set to the same value at both communication partners.

If the procedure receives any character (except for STX or NAK) while in idle state, it waits for the character delay time (CDT) to expire and then sends the NAK character. The communication module outputs a corresponding error message.

##### Receiving data

After a successful connection establishment, the incoming receive characters are saved to the receive buffer. If two consecutive DLE characters are received, only one of these is saved to the receive buffer.

After connection has been established and after each receive character, the procedure waits for the next character during the character delay time. If this period expires before another character is received, an NAK is sent to the communication partner. The communication module outputs a corresponding error message. A retry is then expected.

If transmission errors occur during receiving (frame errors, parity errors, etc.), the procedure continues to receive data until the connection is terminated and then sends an NAK to the communication partner. A retry is then expected. If the block still cannot be received without errors after the specified number of transfer attempts, or if the communication partner does not start the retry within a block wait time of 4 seconds, the procedure cancels the receive operation. The communication module reports the first corrupted transfer and the final cancelation.

##### Connection setup for receiving

If the 3964 procedure detects a DLE ETX string, it terminates the receive operation and confirms a successfully received block by sending a DLE to the communication partner. In the case of a receive error, an NAK is sent to the communication partner. A retry is then expected.

The 3964R procedure terminates the receive operation after having detected the DLE ETX BCC string. It compares the received block check character BCC with the internally calculated longitudinal parity. If the BCC is correct and no other receive errors have occurred, the 3964R procedure sends a DLE and returns to the idle state. The communication module informs the control system that new receive data is available.

If the BCC is faulty or a different receive error occurs, an NAK is sent to the communication partner. A retry is then expected.

### Communication through Modbus RTU (S7-1500)

This section contains information on the following topics:

- [Procedure for establishing a serial connection with Modbus RTU (S7-1500)](#procedure-for-establishing-a-serial-connection-with-modbus-rtu-s7-1500)
- [Overview of modbus communication (S7-1500)](#overview-of-modbus-communication-s7-1500)
- [Function Codes (S7-1500)](#function-codes-s7-1500)

#### Procedure for establishing a serial connection with Modbus RTU (S7-1500)

##### Requirements

- The hardware is set up and there is an electrical connection to the link partner.
- The project has been created in STEP 7 (TIA Portal) and the CPU has been inserted into the hardware configuration.

##### Procedure - Hardware configuration

1. Insert the CM PtP communication module into the hardware configuration.
2. Select the Freeport/Modbus protocol.

   Note: With Modbus RTU, most communication parameters are set using the Modbus_Comm_Load instruction during CPU start.
3. Based on the telegram length, decide whether you want to activate the "Performance optimized for many short frames" parameter.

##### Procedure - Programming

1. Create the data structure that is to include the data to be transferred.
2. Integrate the Modbus_Comm_Load instruction into the cyclic sequence for parameter assignment of the communication module.
3. Interconnect the HWID from the system tags at the PORT input.
4. Call the instruction until successful execution is displayed at the DONE output. Do not call the instruction again thereafter unless you want to change the communication parameters.

**Operation as Modbus master**:

1. Insert the Modbus_Master instruction from the MODBUS (RTU) library:
2. Interconnect the data structure with the data to be sent at the BUFFER input.
3. Interconnect the instance DB of the Modbus_Master instruction at the MB_DB input of the Modbus_Comm_Load.

   Note: During operation, each positive edge at the REQ input will process the specified job once. The block must be called until DONE indicates that the data was transferred to the module.

   In case of an error, setting ERROR once and displaying the corresponding information in STATUS indicates that the data was not transferred.

**Operation as Modbus slave:**

1. Insert the Modbus_Slave instruction from the MODBUS (RTU) library**.**
2. Interconnect the data structure with the Modbus hold registers.
3. Enter the Modbus slave address at the MB_ADDR input.
4. Interconnect the instance DB of the Modbus_Slave instruction at the MB_DB input of the Modbus_Comm_Load.

   Note: A high level at the NDR output during operation indicates that new data was received and stored in the specified data area.

#### Overview of modbus communication (S7-1500)

##### Modbus RTU communication

Modbus RTU (Remote Terminal Unit) is a standard protocol for communication in the network and uses the electrical RS232 or RS422/485 connection for serial data transmission between Modbus devices in the network.

Modbus RTU uses a master/slave network in which the entire communication is triggered by only one master device while the slaves can only respond to the request of the master. The master sends a request to a slave address and only this slave address responds to the command (exception: broadcast frames to slave address 0 which are not acknowledged by the slaves).

The procedure used is a code-transparent, asynchronous half-duplex procedure. Data transmission is carried out without handshake.

##### Position in the system environment

The following Modbus description refers to the use of the corresponding communication modules.

- CM PtP RS232 HF
- CM PtP RS422/485 HF
- CM PtP (ET 200SP)

##### Function of the coupling

With the corresponding communication modules and the related instructions, you can establish a communication connection between a remote Modbus control system and a SIMATIC S7.

The GOULD-MODBUS protocol in RTU format is used for the transfer.

Function codes 01, 02, 03, 04, 05, 06, 08, 15 and 16 are used for communication between a communication module operated as a Modbus slave and a master system (see [Function Codes](#function-codes-s7-1500)).

If a SIMATIC S7 communication module is operated as a Modbus master, function codes 11 and 12 are also available.

##### SIMATIC S7 as a Modbus slave

The master has the initiative for transmission, the communication module works as a slave.

Frame traffic from slave to slave is not possible.

The instruction Modbus_Slave makes the data available on a SIMATIC data area in accordance with the mapping specification or stores them.

##### SIMATIC S7 as a Modbus master

As master, the communication module initiates transmission and, after outputting a request frame, it waits for the configured response monitoring time for a response frame from the slave. If the slave does not respond, the master repeats the request in accordance with the configuration before it outputs an error message.

##### frame structure

The data exchange "Master-Slave" and/or "Slave-Master" begins with the **slave address**, followed by the **function code**. The data is then transferred. The structure of the data field depends on the function code used. The CRC check is transmitted at the end of the frame.

| ADDRESS | FUNCTION | DATA | CRC-CHECK |
| --- | --- | --- | --- |
| Byte/Word | Byte | n byte | 2 byte |

| Symbol | Meaning |
| --- | --- |
| ADDRESS | Modbus slave address  - Standard address: 1 to 247 (bytes) - Extended station address: 1 to 65535 (word) |
| FUNCTION | Modbus [Function Codes](#function-codes-s7-1500) |
| DATA | frame data: Management and net data depending on the function code |
| CRC-CHECK | frame checksum |

##### Slave address

The slave address can be range from 1 to 247 (byte) or 1 to 65535 (word). The address is used to address a defined slave on the bus.

##### Broadcast Message

The master uses slave address 0 to address all slaves on the bus.

Broadcast messages are only permitted in conjunction with writing Function codes 05, 06, 15 and 16.

A broadcast message is not followed by a response frame from the slave.

##### Data Field DATA

The data field DATA is used to transfer the function code-specific data such as:

- Bytecount, Coil_Startaddress, Register_Startaddress; Number_of_Coils, Number_of_Registers, ... .

  For details, see "[Function Codes](#function-codes-s7-1500)".

##### CRC-Check

The end of the frame is identified by means of the CRC 16 checksum consisting of 2 bytes. It is calculated by the following polynominal: x<sup>16</sup> + x<sup>15</sup> + x<sup>2</sup> + 1.

The low byte is transmitted first, followed by the high byte.

##### End of frame

The end of frame is recognized when no transmission takes place during the time period required for the transmission of three and a half characters (3.5 times character delay time) (see Modbus Protocol Reference Guide).

This end of frame TIME_OUT therefore depends on the data transmission rate and is indicated in bit times (35 bit times are fix coded internally; further bit times can be configured in addition at the instruction).

The Modbus frame received from the connection partner is evaluated and formally checked after the end of frame TIME_OUT is received.

##### Exception responses

If an error is detected in the request frame from the master – for example, register address illegal – the slave sets the highest value bit in the function code of the response frame.

This step is followed by transmission of a byte exception code that describes the cause of the error.

A detailed description of the meaning of the above-mentioned parameters is available in the "GOULD MODICON Modbus Protocol" (not part of this documentation).

##### Exception code frame

The exception code frame from the slave has the following form:

- for example, slave address 5, function code 5, exception code 2

Response frame from the device EXCEPTION_CODE_xx:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 85H | Function code |
| 02H | Exception code (1...7) |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

On receipt of an exception code frame by the driver, the current job is completed with error.

The following error codes are defined in accordance with the Modbus specification:

| Error code | Meaning in accordance with Modbus specification | Cause - Short Description * |
| --- | --- | --- |
| 1 | Illegal function | Illegal function code |
| 2 | Illegal data address | Slave has illegal data address |
| 3 | Illegal data value | Slave has illegal data value |
| 4 | Failure in Associated Device | Slave has internal error |
| 5 | Acknowledge | Function is carried out |
| 6 | Busy, Rejected message | Slave is not ready to receive |
| 7 | Negative acknowledgement | The function cannot be carried out. |
| * Check slave for further details. |  |  |

##### RS232 mode

The following communication modules support RS232 mode:

- CM PtP RS232 HF
- CM PtP (ET 200SP)

For more information on RS232 mode, see the chapter [RS232 mode](#rs232-mode-s7-1500).

For information on hardware data flow control and on automatic operation of the accompanying signals, refer to the [Handshake procedure](#handshake-procedure-s7-1500) chapter.

##### RS422/485 mode

The following communication modules support RS422/485 mode:

- CM PtP RS422/485 HF
- CM PtP (ET 200SP)

For more information on RS422/485 mode, see the chapters [RS422 mode](#rs422-mode-s7-1500) and [RS485 mode](#rs485-mode-s7-1500).

##### FAQ

For more information, see the following FAQs in the Siemens Industry Online Support:

- Entry ID [68202723](https://support.industry.siemens.com/cs/ww/en/view/68202723)
- Entry ID [58386780](https://support.industry.siemens.com/cs/ww/en/view/58386780)

#### Function Codes (S7-1500)

##### Function codes used without performance optimization

The function code defines the meaning of the frame. It also defines the structure of a frame.

The following function codes are supported by the communication module:

| Function code | Function in accordance with MODBUS specification | Range |
| --- | --- | --- |
| 01 | Read Coil Status | 1 to 2000 bit/request |
| 02 | Read Input Status | 1 to 2000 bit/request |
| 03 | Read Holding Registers | 1 to 124/125 word/request (124 with extended station address) |
| 04 | Read Input Registers | 1 to 124/125 word/request (124 with extended station address) |
| 05 | Force Single Coil | 1 bit/request |
| 06 | Preset Single Register | 1 word/request |
| 08 * | Loop Back Test | Read slave status or reset event counter in the slave |
| 11 * | Fetch Communications Event Counter (only master) | — |
| 15 | Force Multiple Coils | 1 to 1968 bits/request |
| 16 | Preset Multiple Registers | 1 to 123 word/request |
| * Diagnostics information for slave communication |  |  |

Modbus function code 00 sends a broadcast message to all slaves (without slave response).

##### Function codes used with performance optimization

With the [option for performance optimization](#special-features-for-the-use-of-the-option-for-performance-optimization-s7-1500) activated, there are the following restrictions to the configuration limits of the transferred data:

| Function code | Function in accordance with MODBUS specification | CM PtP is Modbus master | CM PtP is Modbus slave |
| --- | --- | --- | --- |
| 01 | Read Coil Status | 1 to 168/160 bits/request (160 with extended station address) | 1 to 216/208 bits/request (208 with extended station address) |
| 02 | Read Input Status | 1 to 168/160 bits/request (160 with extended station address) | 1 to 216/208 bits/request (208 with extended station address) |
| 03 | Read Holding Registers | 1 to 10 word/request | 1 to 13 word/request |
| 04 | Read Input Registers | 1 to 10 word/request | 1 to 13 word/request |
| 05 | Force Single Coil | 1 bit/request | 1 bit/request |
| 06 | Preset Single Register | 1 word/request | 1 word/request |
| 15 | Force Multiple Coils | 1 to 184/176 bits/request (176 with extended station address) | 1 to 136/128 bits/request (128 with extended station address) |
| 16 | Preset Multiple Registers | 1 to 11 word/request | 1 to 8 word/request |

Modbus function code 00 sends a broadcast message to all slaves (without slave response).

##### Assignment of the Modbus addresses to the SIMATIC addresses

The table below shows the assignment of the Modbus addresses to the SIMATIC addresses.

| Modbus |  |  |  | S7-1500 |  |
| --- | --- | --- | --- | --- | --- |
| FC <sup>1)</sup> | Function | Declaration | Address area | Declaration | CPU address |
| 01 | Read bits | Output | 1 - 9999 | Process image of outputs | Q0.0 - Q1249.6 |
| 02 | Read bits | Input | 10001 - 19999 | Process image of inputs | I0.0 - I1249.6 |
| 03 <sup>2)</sup> | Read words | Holding Register | 40001 - 49999 or 400001 - 465535 | DW0 - DW19998 or DW0 - DW131068 | The M address area depends on the CPU |
| 04 | Read words | Input | 30001 - 39999 | Process image of inputs | IW0 to IW19996 |
| 05 <sup>2)</sup> | Write bits | Output | 1 - 9999 | Process image of outputs | Q0.0 to Q1248.7 |
| 06 | Write words | Holding Register | 40001 - 49999 or 400001 - 465535 | DW0 - DW19998 or DW0 - DW131068 | The M address area depends on the CPU |
| 15 | Write bits | Output | 1 - 9999 | Process image of outputs | Q0.0 - Q1249.6 |
| 16 <sup>2)</sup> | Write words | Holding Register | 40001 - 49999 or 400001 - 465535 | DW0 - DW19998 or DW0 - DW131068 | The M address area depends on the CPU |
| 1) FC = function code  2) The value of the HR_Start_Offset determines whether data areas or bit memory address areas can be addressed with the FCs 03, 05 and 16 in the SIMATIC CPU. |  |  |  |  |  |

### Communication using USS (S7-1500)

This section contains information on the following topics:

- [Procedure for establishing a serial connection with USS (S7-1500)](#procedure-for-establishing-a-serial-connection-with-uss-s7-1500)
- [Overview of USS communication (S7-1500)](#overview-of-uss-communication-s7-1500)
- [Overview of functions (S7-1500)](#overview-of-functions-s7-1500)

#### Procedure for establishing a serial connection with USS (S7-1500)

##### Requirements

- The hardware is set up and there is an electrical connection to the link partner.
- The project has been created in STEP 7 (TIA Portal) and the CPU has been inserted into the hardware configuration.

##### Procedure - Hardware configuration

1. Insert the CM PtP communication module into the hardware configuration.
2. Select the Freeport protocol and set the communication parameters.

   Note: The USS functionality is implemented by the instructions.
3. Based on the telegram length, decide whether you want to activate the "Performance optimized for many short frames" parameter.

##### Procedure - Programming

1. Insert the USS_Port_Scan instruction from the USS Communication library.
2. Interconnect the HWID from the system tags at the PORT input.
3. Insert the USS_Drive_Control instruction from the USS Communication library.
4. Interconnect the USS_DB data structure in the instance DB of the USS_Drive_Control instruction to the USS_DB input of the USS_Port_Scan instruction. The data structure contains the data to be transferred for all drives.
5. Insert an additional call of the USS_Drive_Control instruction for each additional axis that is to be connected via the USS interface.

   Use the same instance DB each time. The distinction takes place with the help of the USS address that you specify at the DRIVE input of the USS_Drive_Control instruction. This means you have access to the control and feedback data at the parameters of the respective call for each drive.

#### Overview of USS communication (S7-1500)

##### Position in the system environment

The following USS description refers to the use of the corresponding communication modules.

- CM PtP RS232 BA
- CM PtP RS422/485 BA
- CM PtP RS232 HF
- CM PtP RS422/485 HF
- CM PtP (ET 200SP)

##### Introduction

The USS® protocol (Universal Serial Interface Protocol) is a basic serial data transmission protocol designed to meet the requirements of drive technology.

The USS protocol defines an access method based on the master-slave principle for communication via a serial bus. One master and up to 16 drives (slaves) can be connected to the bus. The individual drives are selected by the master using an address character in the frame. A drive can never send anything without first being initiated by the master. Therefore, direct data transmission between individual drives is not possible. Communication functions in half-duplex mode. The master function cannot be transferred.

Drive technology requires specific response times for the control tasks and therefore strict cyclical frame traffic:

The master continuously sends frames (job frames) to the drives and expects a response frame from each addressed drive.

A drive must send a response frame if

- it has a received a frame without errors and
- it was addressed in this frame.

A drive may not send if these conditions are not met or the drive was addressed in the broadcast.

The connection with the respective drives exists for the master once it receives a response frame from the drive after a specified processing time (response delay time).

##### frame structure

Each frame begins with a start character (STX), followed by the length specification (LGE) and the address byte (ADR). The data field comes after that. The frame ends with the block check character (BCC). The frame length includes the user data (quantity n), the address byte (ADR) and the data verification character (BCC).

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| STX | LGE | ADR | 1 | 2 | ... | N | BCC |

For single-word (16-bit) data, the high byte is sent first followed by the low byte. Correspondingly, with double-word data the high word is sent first, followed by the low word. The length of a frame is specified in bytes.

##### Data encryption

The data is encrypted as follows:

- STX: 1 byte, start of text, 02H
- LGE: 1 byte, contains the frame length as a binary number
- ADR: 1 byte, contains the slave address and frame type in binary code
- Data fields: One byte each, content depending on job
- BCC: 1 byte, block check character

##### Data transmission procedure

The master ensures cyclic data transmission in frames. The master addresses all slave devices one after another with a job frame. The nodes addressed respond with a response frame. In accordance with the master-slave procedure, the slave must send the response frame to the master after it has received the job frame. Only then can the master address the next slave.

##### Data field in the frame

The data field is divided into two areas: the parameter area (PKW) and the process data area (PZD).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| STX | LGE | ADR | Parameter (PKW) | Process data (PZD) | BCC |

- **Parameter area** (PKW)

  The PKW area handles parameter transmission between two communication partners (e.g., controller and drive). This involves, for example, reading and writing parameter values and reading parameter descriptions and the associated text. The PKW interface generally contains jobs for operation and display, maintenance and diagnostics.
- **Process data area** (PZD)

  The PZD area consists of signals that are required for automation:

  - Control words and setpoints from the master to the slave
  - Status words and actual values from the slave to the master

  The contents of the parameter area and process data area are defined by the slave drives.

  For additional information on this, refer to the drive documentation.

#### Overview of functions (S7-1500)

##### Transmission sequence

The instructions process the data transmission cyclically with up to 16 drive slaves. Only one job is active for each drive at any one time.

##### Performance features:

- Creation of data storage areas for communication, depending on the bus configuration
- Execution and monitoring of PKW jobs
- Monitoring of the complete system and troubleshooting
- Communication with the CPU
- Access to the drive functions
- Reading the drive parameters
- Writing the drive parameters

## Programming - communication using instructions (S7-1500)

This section contains information on the following topics:

- [Overview of point-to-point programming (S7-1500)](#overview-of-point-to-point-programming-s7-1500)
- [Overview of Modbus programming (S7-1500)](#overview-of-modbus-programming-s7-1500)
- [Overview of USS programming (S7-1500)](#overview-of-uss-programming-s7-1500)

### Overview of point-to-point programming (S7-1500)

#### Data exchange using Freeport or 3964(R) communication

You must make the send data available in data blocks or in the bit memory address area in the user program of the corresponding CPU. A receive buffer is available in the communication module for the receive data. A corresponding data block is set up in the data block.

In the user program of the CPU, the following instructions carry out the data transfer between the CPU and the communication module.

- Send_P2P
- Receive_P2P

The receive buffer can be deleted with the instruction Receive_Reset.

#### Dynamic configuration by means of the user program

As an alternative to or in addition to the parameter assignment of the communication module interface described in section [Configuring / parameter assignment of a communication module](#configuring-parameter-assignment-of-a-communication-module-s7-1500), it may be advisable in certain application areas to set up the communication dynamically, i.e., program-controlled by a specific application.

All parameters assigned in the properties dialog of the communication module can also be changed during runtime by means of one of the following "Config" instructions:

Port_Config, Send_Config, Receive_Config, P3964_Config

#### Program calls for point-to-point communication - sequence

The figure below shows the function of the point-to-point instructions for communication between the user program and communication partner.

![Program calls for point-to-point communication - sequence](images/88142969355_DV_resource.Stream@PNG-en-US.png)

#### PtP instructions

| Application | Instruction | Description |
| --- | --- | --- |
| Data exchange between CPU, communication module and communication partner (communication) | [Send_P2P](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#send_p2p-sending-data-s7-1200-s7-1500) | The instruction Send_P2P (send point-to-point data) can be used to send data to the communication partner.   Call up the instruction Send_P2P to send data using the Freeport protocol. You have to call the instruction cyclically until you receive a corresponding acknowledgement at the output parameters of the instruction.  Note: During parameter assignment of the XON/XOFF data flow control, user data may not contain any of the configured XON or XOFF characters. Default settings are DC1 = 11H for XON and DC3 = 13H for XOFF. |
| [Receive_P2P](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#receive_p2p-receiving-data-s7-1200-s7-1500) | The instruction Receive_P2P (receive point-to-point data) can be used to pick up the messages received in the communication module from a communication partner.  Call the Receive_P2P instruction cyclically to receive data using the Freeport protocol. The instruction indicates at the NDR parameter if new received data is available.  To signal the start and end of a message transmission, you need to define criteria in the Freeport protocol which identify the start and end of the message. |  |
| Deletion of the receive buffer | [Receive_Reset](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#receive_reset-clear-receive-buffer-s7-1200-s7-1500) | The instruction Receive_Reset (delete receive buffer) allows you to clear the receive buffer of the communication module. |
| Dynamic parameter assignment of the interface or the protocol (optional) | [Port_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#port_config-configure-ptp-communication-port-s7-1200-s7-1500) | You can use the Port_Config instruction (port configuration) to configure basic interface parameters, such as the data transmission rate, parity and data flow control dynamically through your user program. |
| [Send_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#send_config-configure-ptp-sender-s7-1200-s7-1500) | With the instruction Send_Config(send configuration) you can configure serial send parameters, such as RTS ON delay / RTS OFF delay, dynamically for a point-to-point communication interface. |  |
| [Receive_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#receive_config-configure-ptp-recipient-s7-1200-s7-1500) | The instruction Receive_Config (receive parameter assignment) allows you to dynamically assign serial receive parameters to a communication module.  This instruction configures the conditions that specify the start and the end of a received message. |  |
| [P3964_Config](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#p3964_config-configuring-the-3964r-protocol-s7-1200-s7-1500) | The instruction P3964_Config(configure protocol) can be used to dynamically configure protocol parameters of the procedure 3964(R), such as character delay time, priority and block check using your program. |  |
| Operation of RS232 accompanying signals | [Signal_Get](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#signal_get-read-status-s7-1200-s7-1500) | With the Signal_Get instruction (get RS232 signals) you can read the current states of the RS232 signals. |
| [Signal_Set](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#signal_set-set-accompanying-signals-s7-1200-s7-1500) | With the Signal_Set instruction (get RS232 signals), you can set the states of the RS232 signals DTR and RTS. |  |
| Enable Modbus CRC support and diagnostic interrupt | [Get_Features](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#get_features-get-extended-functions-s7-1200-s7-1500) | You can use the instruction Get_Features(get extended functions) to get information on the Modbus support and on generating diagnostic alarms. |
| [Set_Features](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#set_features-set-extended-functions-s7-1200-s7-1500) | If supported by the module, you can use the instruction Set_Features(set extended functions) to activate the generation of diagnostic alarms. |  |

#### Procedure for setting up Freeport or 3964(R) communication

Requirement: The configuration and parameter assignment of a CPU and a communication module in the device view and in the properties dialog of the communication module are complete.

1. In the project navigation for the CPU select the folder "Program blocks" and open the Main (OB1) in the folder by double-clicking it. The program editor opens.
2. From the "Instructions" task card, "Communication" area select the instructions Send_P2P and Receive_P2P and drag-and-drop them into a network of the Main (OB1).
3. Configure the instructions in accordance with your specifications.
4. Download the hardware configuration and the user program to the CPU.

### Overview of Modbus programming (S7-1500)

#### Program calls for Modbus communication - sequence

The figure below shows the function of the Modbus instructions for communication between user program and Modbus device. (The instructions Send_P2P, Receive_P2P and the Config instructions are used downstream).

![Program calls for Modbus communication - sequence](images/154522688779_DV_resource.Stream@PNG-en-US.png)

#### Modbus instructions

| Application | Instruction | Description |
| --- | --- | --- |
| Data exchange between user program and Modbus device (communication) | [Modbus_Master](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus_master-communicate-as-modbus-master-s7-1200-s7-1500) | The Modbus_Master instruction allows you to communicate as Modbus master by means of the PtP port.   The CPU can be used as Modbus RTU master device with the Modbus_Master instruction for communication with one or several Modbus slave devices. |
| [Modbus_Slave](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus_slave-communicate-as-modbus-slave-s7-1200-s7-1500) | The instruction Modbus_Slave allows you to communicate as Modbus slave by means of the PtP port.   The CPU can be used as Modbus RTU slave device with the Modbus_Slave instruction for communication with one Modbus master device. |  |
| Parameter assignment of the interface and the protocol (mandatory) | [Modbus_Comm_Load](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus_comm_load-configure-communication-module-for-modbus-s7-1200-s7-1500) | The instruction Modbus_Comm_Load allows you to configure the port of the communication module for Modbus RTU.   You have to run Modbus_Comm_Load to set up PtP port parameters, such as data transmission rate, parity and flow control. Once you have configured the interface for the Modbus RTU protocol, it can only be used by the instruction Modbus_Master or the instruction Modbus_Slave . |

> **Note**
>
> **Alternative use of Modbus_Slave and Modbus_Master**
>
> A communication module can be operated either as master or as slave.

#### Procedure for setting up Modbus communication

Requirement: The configuration and parameter assignment of a CPU and a communication module in the device view and in the properties dialog of the communication module are complete.

1. In the project navigation for the CPU select the folder "Program blocks" and open the Main (OB1) in the folder by double-clicking it. The program editor opens.
2. From the "Instructions" task card, "Communication" area select the instructions for Modbus communication in accordance with your task and drag-and-drop them into a network of the Main (OB1):

   - The instruction Modbus_Comm_Load configures the port of the communication module for Modbus communication.

     The Modbus_Comm_Load must be called in Main (OB1) until DONE (or ERROR) is reported.
   - The instruction Modbus_Master is used for the Modbus master functionality.
   - The instruction Modbus_Slave is used for the Modbus slave functionality.
3. Configure the instructions in accordance with your specifications.
4. Download the hardware configuration and the user program to the CPU.

---

**See also**

[Overview of instructions (S7-1500)](#overview-of-instructions-s7-1500)

### Overview of USS programming (S7-1500)

#### Program calls for USS communication - sequence

The figure below shows the function of the USS instructions for communication between user program and USS drive. (The instructions Send_P2P, Receive_P2P and the Config instruction are required downstream).

![Program calls for USS communication - sequence](images/51402705291_DV_resource.Stream@PNG-en-US.png)

#### USS instructions

| Application | Instruction | Description |
| --- | --- | --- |
| Data communication between CPU, communication module and USS drive | [USS_Port_Scan](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_port_scan-uss_port_scan_31-communication-by-means-of-a-uss-network-s7-1200-s7-1500) | The USS_Port_Scan instruction allows you to communicate via a communication module with up to 16 drives using a USS network (must be called cyclically).  The instruction USS_Port_Scan controls the communication between CPU and the drives by means of the PtP communication port. A communication with the drive is processed every time you call this function. The instruction USS_Port_Scan is required once:  Since most drives features a configurable internal function that monitors the integrity of the communication based on a timeout, the instruction USS_Port_Scan should be called from a time-controlled OB. |
| Exchange data with USS drive | [USS_Drive_Control](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_drive_control-uss_drive_control_31-preparing-and-displaying-data-for-the-drive-s7-1200-s7-1500) | The USS_Drive_Control instruction allows you to prepare the send data for a drive and to display the received data.  The inputs and outputs of the instruction correspond to the states and operating functions of the drive. The USS_Drive_Control instruction must be called once for each drive. Only one common instance DB is required for all calls of the instruction USS_Drive_Control for a USS network. Interconnect all calls of the instructions USS_Drive_Control for a USS network with the same instance DB.  The USS_Drive_Control instruction should be called from the cyclic Main (OB1) of the main program. |
| Read or modify parameters in USS drive | [USS_Read_Param](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_read_param-uss_read_param_31-read-data-from-drive-s7-1200-s7-1500) | The USS_Read_Param instruction allows you to read parameters from the drive.   You use the USS_Read_Param instruction to read the operating parameters of the drive that controls the internal drive functions.  The USS_Read_Param instruction should be called from the cyclic Main (OB1) of the main program. |
| [USS_Write_Param](USS%20%28S7-1200%2C%20S7-1500%29.md#uss_write_param-uss_write_param_31-change-data-in-drive-s7-1200-s7-1500) | The USS_Write_Param instruction allows you to change parameters in the drive.   The USS_Write_Param instruction should be called from the cyclic Main (OB1) of the main program. |  |

#### Procedure for setting up USS communication

Requirement: The configuration and parameter assignment of a CPU and a communication module in the device view and in the properties dialog of the communication module are complete.

1. In the project tree for the CPU, select the "Program blocks" folder and open the desired time-controlled OB by double-clicking it. The program editor opens.
2. From the "Instructions" task card, "Communication" area select the instruction USS_Port_Scan and drag-and-drop it into a network of a time-controlled OB.

   The instruction USS_Port_Scan allows you to communicate by means of the USS network.
3. In the project navigation for the CPU select the folder "Program blocks" and open the Main (OB1) in the folder by double-clicking it. The program editor opens.
4. From the "Instructions" task card, "Communication" area select the instructions for USS communication in accordance with your task and drag-and-drop them into a network of the Main (OB1):

   - The instruction USS_Drive_Control is used for data exchange with the drive.
   - The instruction USS_Read_Param is used for reading parameters from the drive.
   - The instruction USS_Write_Param is used for changing parameters in the drive.
5. Configure the instructions in accordance with your specifications.
6. Download the hardware configuration and the user program to the CPU.

---

**See also**

[Overview of instructions (S7-1500)](#overview-of-instructions-s7-1500)

## Startup and Diagnostics (S7-1500)

This section contains information on the following topics:

- [Startup characteristics (S7-1500)](#startup-characteristics-s7-1500)
- [Diagnostic functions (S7-1500)](#diagnostic-functions-s7-1500)
- [Diagnostic interrupts (S7-1500)](#diagnostic-interrupts-s7-1500)

### Startup characteristics (S7-1500)

#### Operating mode transitions

After the communication module starts up, all data between the CPU and the communication module is exchanged by means of instructions.

| Symbol | Meaning |
| --- | --- |
| CPU STOP | During a running data transmission communication module ‑ CPU, both a send and a receive job is aborted.  Frames will continue to be received. However, information about this is forwarded to the CPU only after a STOP-RUN transition, provided it has been configured that the receive buffer is not cleared. |
| CPU RUN | Send and receive operation is ensured in the RUN state of the CPU.   With a corresponding configuration in the properties dialog of the communication module, you can automatically clear the receive buffer on the communication module during CPU startup. |

From the view of the communication module, there are no further operating states/operating state transitions.

### Diagnostic functions (S7-1500)

#### Introduction

The diagnostic functions of the communication module allow errors that have occurred to be located quickly. The following diagnostic options are available to you:

| Symbol | Meaning |
| --- | --- |
| Diagnostics by means of the display elements of the communication module | The indicators provide information on the operating mode or the possible error states of the communication module. The indicators provide an initial overview of any internal or external errors and interface-specific errors. For more information refer to the device manual of the corresponding communication module. |
| Diagnostics via the STATUS output of the instructions | Instructions have a STATUS output for error diagnostics; it provides information about communication errors between the communication module and the CPU. You can evaluate the [STATUS parameter](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#error-messages-s7-1200-s7-1500) in the user program (the parameter is present for exactly one cycle). |
| Diagnostic error interrupt | The communication module can trigger a diagnostic error interrupt on the CPU assigned to it. The communication module makes diagnostic information available. The analysis of this information is made via the user program or by reading the CPU diagnostics buffer. |
| Diagnostics via the EventTracePtP data record | With the EventTracePtP data record, you can save and read out the last maximum of 1000 (communication) events and the parameterization of the communication module.  Information on the configuration of the data record can be found in the function manual [CM PtP - Configurations for point-to-point connections](http://support.automation.siemens.com/WW/view/en/59057093). |

### Diagnostic interrupts (S7-1500)

The diagnostics are displayed as plain text in STEP 7 (TIA Portal) in the online and diagnostics view. You can evaluate the error codes with the user program.

The following diagnostics can be signaled:

- Error (9<sub>H</sub>)
- Parameter assignment error (10<sub>H</sub>)
- Wire break (S7-1500/ET 200MP: 109<sub>H</sub>; ET 200SP: 6<sub>H</sub>)
