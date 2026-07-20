---
title: "Configuration for point-to-point links (S7-300, S7-400)"
package: HWCConfPtP34enUS
topics: 77
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuration for point-to-point links (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction (S7-300, S7-400)](#introduction-s7-300-s7-400)
- [Basic information (S7-300, S7-400)](#basic-information-s7-300-s7-400)
- [Modbus communication (S7-300, S7-400)](#modbus-communication-s7-300-s7-400)
- [USS communication (S7-300, S7-400)](#uss-communication-s7-300-s7-400)
- [Startup and Diagnostics (S7-300, S7-400)](#startup-and-diagnostics-s7-300-s7-400)

## Introduction (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of the components and interfaces (S7-300, S7-400)](#overview-of-the-components-and-interfaces-s7-300-s7-400)
- [Overview of the instructions (S7-300, S7-400)](#overview-of-the-instructions-s7-300-s7-400)

### Overview of the components and interfaces (S7-300, S7-400)

#### Contents

Table overview of the module variations and their functions.

For CP 340/341/440/441 and ET 200S 1SI

| Module | Interface | Protocols |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | ASCII | 3964(R) | RK512 | Printer driver | Modbus master | Modbus slave | USS master |
| CP 340 | RS232 C | X | X | - | X | - | - | - |
| CP 340 | 20 mA TTY | X | X | - | X | - | - | - |
| CP 340 <sub>1)</sub> | RS422 | X | X | - | X | - | - | - |
| RS485 | X | - | - | - | - | - | - |  |
| CP 341 | RS232 C | X | X | X | X | X <sub>2)</sub> | X <sub>2)</sub> | - |
| CP 341 | 20 mA TTY | X | X | X | X | X <sub>2)</sub> | X <sub>2)</sub> | - |
| CP 341 <sub>1)</sub> | RS422 | X | X | X | X | X <sub>2)</sub> | X <sub>2)</sub> | - |
| RS485 | X | - | - | X | X <sub>2)</sub> | X <sub>2)</sub> | - |  |
| CP 440 | RS422 | X | X | - | - | - | - | - |
| RS485 | X | - | - | - | - | - | - |  |
| CP 441-1 | RS232 C | X | X | - | X | - | - | - |
| CP 441-1 | 20 mA TTY | X | X | - | X | - | - | - |
| CP 441-1 <sub>1)</sub> | RS422 | X | X | - | X | - | - | - |
| RS485 | X | - | - | X | - | - | - |  |
| CP 441-2 | RS232 C | X | X | X | X | X <sub>2)</sub> | X <sub>2)</sub> | - |
| CP 441-2 | 20 mA TTY | X | X | X | X | X <sub>2)</sub> | X <sub>2)</sub> | - |
| CP 441-2 <sub>1)</sub> | RS422 | X | X | X | X | X <sub>2)</sub> | X <sub>2)</sub> | - |
| RS485 | X | - | - | X | - | - | - |  |
| ET 200S 1SI for ASCII and 3964(R) | RS232 C | X | X | - | - | - | - | - |
| RS422 | X | X | - | - | - | - | - |  |
| RS485 | X | - | - | - | - | - | - |  |
| ET 200S 1SI for modbus and USS | RS232 C | - | - | - | - | X | X | X |
| RS422 | - | - | - | - | X | X | - |  |
| RS485 | - | - | - | - | X | X | X |  |
| CPU 313C-2 PtP | RS422 | X | X | - | - | - | - | - |
| RS485 | X | - | - | - | - | - | - |  |
| CPU 314C-2 PtP | RS422 | X | X | X | - | - | - | - |
| RS485 | X | - | - | - | - | - | - |  |
| <sub>1)</sub> The difference between RS422 and RS485 is set in the configuration dialog.   <sub>2)</sub> A loadable driver with a dongle is needed for the Modbus protocol. |  |  |  |  |  |  |  |  |

#### Accompanying signals and data flow control

The RS232C accompanying signals can be controlled with the ASCII, Modbus master and Modbus slave protocols via the RS232C interface.

Data flow control with RTS/CTS is possible with the ASCII and printer driver protocols via the RS 232C interface.

Data flow control with XON/XOFF is possible with the ASCII and printer driver protocols via the RS232C, 20mA TTY and RS422 interfaces.

### Overview of the instructions (S7-300, S7-400)

#### Overview of the instructions

The communication between the CPU, communication module and a communication partner is performed via the instructions and the protocols of the communication module.

The instructions form the software interface between the CPU and the communication module. They must be called cyclically from the user program.

The communication protocols are implemented on the communication module. The protocol is used to adapt the interface of the communication module to the interface of the communication partner.

All tables
Instructions for CP 340
Instructions for CP 341
Instructions for CPU 313C-2 PTP
Instructions for CPU 314C-2 PTP
Instructions for CP 440
Instructions for CP 441
Instructions for ET 200S 1SI
Instructions for Modbus

Instructions for CP 340

| Instruction | Meaning |
| --- | --- |
| [P_SEND](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#p_send-sending-data-s7-300-s7-400) | The instruction P_SEND allows you to send an entire range or a partial range of a data component to a communication partner. |
| [P_RCV](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#p_rcv-receiving-data-s7-300-s7-400) | The instruction P_RCV allows you to receive data from a communication partner and to store them in a data block. |
| [P_PRINT](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#p_print-print-message-text-with-up-to-4-variables-s7-300-s7-400) | The P_PRINT instruction allows you to print a message text with up to 4 variables on a printer. |
| [P_RESET](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#p_print-print-message-text-with-up-to-4-variables-s7-300-s7-400) | The P_RESET instruction allows you to reset the internal receive buffer of the CP 340. |
| [V24_STAT_340](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#v24_stat_340-v24_stat-reading-accompanying-signals-from-the-rs232c-interface-s7-300-s7-400) | The V24_STAT instruction allows you to read the signal states at the RS232C interface of the CP 340-RS232C. |
| [V24_SET_340](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#v24_set_340-v24_set-writing-accompanying-signals-to-the-rs232c-interface-s7-300-s7-400) | The V24_SET instruction allows you to set/reset the outputs on the RS232C interface of the CP 340 RS232C. |

Instructions for CP 341

| Instruction | Meaning |
| --- | --- |
| [P_SND_RK](PtP%20data%20link%20CP%20341%20%28S7-300%2C%20S7-400%29.md#p_snd_rk-fetching-or-sending-data-s7-300-s7-400) | You can use the instruction P_SND_RK to send the entire range or a partial range of a data block to a communication partner, or you can fetch data from the communication partner (using RK512). |
| [P_RCV_RK](PtP%20data%20link%20CP%20341%20%28S7-300%2C%20S7-400%29.md#p_rcv_rk-receive-data-or-provide-data-s7-300-s7-400) | You can use the P_RCV_RK instruction to receive data from a communication partner and store it in a data block or make data available to the communication partner (using RK512). |
| [P_PRINT341](PtP%20data%20link%20CP%20341%20%28S7-300%2C%20S7-400%29.md#p_prt341-print-message-text-with-up-to-4-variables-s7-300-s7-400) | The instruction P_PRINT341 allows you to print a message text with up to 4 variables on a printer. |
| [V24_STAT](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#v24_stat_340-v24_stat-reading-accompanying-signals-from-the-rs232c-interface-s7-300-s7-400) | The V24_STAT instruction allows you to read the signal states at the RS232C interface of the CP 341-RS232C. |
| [V24_SET](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#v24_set_340-v24_set-writing-accompanying-signals-to-the-rs232c-interface-s7-300-s7-400) | The V24_SET instruction allows you to set/reset the outputs on the RS232C interface of the CP 341 RS232C. |

Instructions for CPU 313C-2 PTP

| Instruction | Meaning |
| --- | --- |
| [SEND_PTP](300C%20functions%20%28S7-300%2C%20S7-400%29.md#send_ptp-send-data-ascii-3964r-s7-300-s7-400) | With the instruction SEND_PTP, you can send the entire range or a partial range of a data block to a communication partner. |
| [RCV_PTP](300C%20functions%20%28S7-300%2C%20S7-400%29.md#rcv_ptp-fetch-data-ascii-3964r-s7-300-s7-400) | With the instruction RCV_PTP, you can receive the data from a communication partner and store it in a data block. |
| [RES_RCVB](300C%20functions%20%28S7-300%2C%20S7-400%29.md#rcv_ptp-fetch-data-ascii-3964r-s7-300-s7-400) | You can use the RES_RCVB instruction to reset the receive buffer of the module. |

Instructions for CPU 314C-2 PTP

| Instruction | Meaning |
| --- | --- |
| [SEND_PTP](300C%20functions%20%28S7-300%2C%20S7-400%29.md#send_ptp-send-data-ascii-3964r-s7-300-s7-400) | With the instruction SEND_PTP, you can send the entire range or a partial range of a data block to a communication partner. |
| [RCV_PTP](300C%20functions%20%28S7-300%2C%20S7-400%29.md#rcv_ptp-fetch-data-ascii-3964r-s7-300-s7-400) | With the instruction RCV_PTP, you can receive the data from a communication partner and store it in a data block. |
| [RES_RCVB](300C%20functions%20%28S7-300%2C%20S7-400%29.md#res_rcvb-reset-receive-buffer-ascii-3964r-s7-300-s7-400) | You can use the RES_RCVB instruction to reset the receive buffer of the module. |
| [SEND_RK](300C%20functions%20%28S7-300%2C%20S7-400%29.md#send_rk-send-data-rk-512-s7-300-s7-400) | You can use the SEND_RK instruction to send the entire range or a partial range of a data block to a communication partner using the RK512 protocol. |
| FETCH_RK | You can use the FETCH_RK instruction to request data from the communication partner using the RK512 protocol. |
| [SERVE_RK](300C%20functions%20%28S7-300%2C%20S7-400%29.md#serve_rk-receive-and-provide-data-rk-512-s7-300-s7-400) | You can use the SERVE_RK instruction to receive RK512 protocol data from a communication partner and store it in a data block or make data available to the communication partner. |

Instructions for CP 440

| Instruction | Meaning |
| --- | --- |
| [SEND_440](PtP%20data%20link%20CP%20440%20%28S7-300%2C%20S7-400%29.md#send_440-sending-data-s7-300-s7-400) | With the instruction SEND_440 , you can send the entire range or a partial range of a data block to a communication partner. |
| [RECV_440](PtP%20data%20link%20CP%20440%20%28S7-300%2C%20S7-400%29.md#recv_440-receiving-data-s7-300-s7-400) | With the instruction RECV_440 , you can receive the data from a communication partner and store it in a data block. |
| [RES_RECV](PtP%20data%20link%20CP%20440%20%28S7-300%2C%20S7-400%29.md#res_recv-delete-receive-buffer-s7-300-s7-400) | With the instruction RES_RECV , you can reset the receive buffer of the CP 440. |

Instructions for CP 441

| Instruction | Meaning |
| --- | --- |
| [V24_STAT_441](PtP%20data%20link%20CP%20441%20%28S7-300%2C%20S7-400%29.md#v24_stat_441-reading-accompanying-signals-from-the-rs232c-interface-s7-300-s7-400) | The V24_STAT_441 instruction allows you to read the signal states on the RS232C interface of the CP 441. |
| [V24_SET_441](PtP%20data%20link%20CP%20441%20%28S7-300%2C%20S7-400%29.md#v24_set_441-writing-accompanying-signals-to-the-rs232c-interface-s7-300-s7-400) | The V24_SET_441 instruction allows you to set/reset the outputs on the RS232C interface of the CP 441 . |
| The automation system S7-400 provides a row of instructions that activate and control the communication in the user program between CPU and the communication processor CP 441. These instructions are stored in the memory of the CPU (see below in the section "Instructions from the automation system S7-400"). |  |

Instructions for ET 200S 1SI

| Instruction | Meaning |
| --- | --- |
| [S_SEND](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_send-sending-data-s7-300-s7-400) | The instruction S_SEND allows you to send an entire range or a partial range of a data component to a communication partner. |
| [S_RCV](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_rcv-receiving-data-s7-300-s7-400) | The instruction S_RCV allows you to receive data from a communication partner and to store them in a data block. |
| [S_VSTAT](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_vstat-read-accompanying-signals-at-the-rs-232c-interface-s7-300-s7-400) | The instruction S_VSTAT allows you to read the signal states on the RS 232C-interface of the component ET 200S 1SI. |
| [S_VSET](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_vset-write-accompanying-signals-at-the-rs-232c-interface-s7-300-s7-400) | The instruction S_VSET allows you to set/reset the outputs on the RS 232C-interface of the module ET 200S 1SI. |
| [S_XON](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_xon-assign-parameters-for-xonxoff-data-flow-control-s7-300-s7-400) | With the instruction S_XON , you can set additional settings if the module was set for the flow control XON/XOFF. |
| [S_RTS](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_rts-assign-parameters-for-rtscts-data-flow-control-s7-300-s7-400) | With the instruction S_RTS , you can set additional settings if the module was set for the flow control RTS/CTS. |
| [S_V24](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_v24-assign-parameters-for-data-flow-control-using-automatic-operation-of-the-rs-232c-accompanying-signals-s7-300-s7-400) | With the instruction S_V24 , you can set additional settings if the module was set for the automatic operation of the V.24 signals. |
| [S_MODB](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_modb-modbus-slave-instruction-for-et-200s-1si-s7-300-s7-400) | The S_MODB instruction allows you to establish a communication connection to a Modbus master control system and implement the Modbus addresses in the SIMATIC memory areas. |
| [S_USST](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_usst-send-data-to-a-uss-slave-s7-300-s7-400) | The instruction S_USST processes the transfer of the network data (PZD and PKW data) to the slaves depending on the network data structure being used. |
| [S_USSR](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_ussr-receive-data-from-a-uss-slave-s7-300-s7-400) | The instruction S_USSR processes the reception of the network data (PZD and PKW data) from the slaves depending on the network data structure being used. |
| [S_USSI](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_ussi-initialize-uss-s7-300-s7-400) | If this instruction S_USSI is called upon starting up the S7-system, communication processor DB, network DB and parameter DB are created, which are required for communication. |

Instructions for Modbus

| Instruction | Meaning |
| --- | --- |
| [MODB_341](Modbus%20slave%20%28RTU%29%20%28S7-300%2C%20S7-400%29.md#modb_341-modbus-slave-instruction-for-cp-341-s7-300-s7-400) | With the instruction MODB_341 and the affiliated driver, a communication connection between a modbus master control system and the communication module CP 341 "modbus-capable" slave system is allowed for. |
| [MODB_441](Modbus%20slave%20%28RTU%29%20%28S7-300%2C%20S7-400%29.md#modb_441-modbus-slave-instruction-for-cp-441-s7-300-s7-400) | With the instruction MODB_441 and the affiliated driver, a communication connection between a modbus master control system and the communication module CP 441-2 "modbus-capable" slave system is allowed for. |

#### Instructions from the automation system S7-400

In the following table, you will find the instructions from the automation system S7-400, which are available for communication between CPU and CP 441.

Instructions from the automation system S7-400

| Instruction | Meaning |
| --- | --- |
| BSEND | With the instruction BSEND, you can send data from a S7-data range to a communication partner with a destination. |
| BRCV | With the instruction BRCV, you can receive the data from a communication partner and transfer it to a S7-data range. |
| GET | RK512 only: With the instruction GET, you can fetch the data from a communication partner. |
| PUT | RK512 only: With the instruction PUT, you can send the data to the communication partner with dynamic destination addresses.. |
| PRINT | With the instruction PRINT, you can print a message text on a printer with up to four variables. |
| STATUS | With the instruction STATUS, you can call the status of a communication connection. |

#### Further Information

A detailed description of the instructions from the automation system S7-400 and their settings can be found under: [Overview of the instructions for S7 communication](S7%20communication%20%28S7-300%2C%20S7-400%29.md#overview-of-the-s7-communication-instructions-s7-300-s7-400)

---

**See also**

[P_RESET: Delete receive buffer (S7-300, S7-400)](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#p_reset-delete-receive-buffer-s7-300-s7-400)
  
[S_RCV: receiving data (S7-300, S7-400)](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_rcv-receiving-data-s7-300-s7-400)
  
[S_SEND: Sending Data (S7-300, S7-400)](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#s_send-sending-data-s7-300-s7-400)
  
[FETCH_RK: Fetch data (RK 512)](300C%20functions%20%28S7-300%2C%20S7-400%29.md#fetch_rk-fetch-data-rk-512-s7-300-s7-400)

## Basic information (S7-300, S7-400)

This section contains information on the following topics:

- [Serial transfer of a character (S7-300, S7-400)](#serial-transfer-of-a-character-s7-300-s7-400)
- [Transmission integrity (S7-300, S7-400)](#transmission-integrity-s7-300-s7-400)
- [Data transmission with ASCII driver (S7-300, S7-400)](#data-transmission-with-ascii-driver-s7-300-s7-400)
- [Data transmission with 3964(R) (S7-300, S7-400)](#data-transmission-with-3964r-s7-300-s7-400)
- [Data transmission with Rk512 (S7-300, S7-400)](#data-transmission-with-rk512-s7-300-s7-400)
- [Data transmission with printer driver (S7-300, S7-400)](#data-transmission-with-printer-driver-s7-300-s7-400)
- [Indicator for end of a message freme (S7-300, S7-400)](#indicator-for-end-of-a-message-freme-s7-300-s7-400)
- [Data flow control and secondary signals (S7-300, S7-400)](#data-flow-control-and-secondary-signals-s7-300-s7-400)
- [Interface operating modes (S7-300, S7-400)](#interface-operating-modes-s7-300-s7-400)
- [Initial state of receive line (S7-300, S7-400)](#initial-state-of-receive-line-s7-300-s7-400)
- [CP 440 in a multipoint topology with the RS422/485 protocols (S7-300, S7-400)](#cp-440-in-a-multipoint-topology-with-the-rs422485-protocols-s7-300-s7-400)
- [Receive buffer (S7-300, S7-400)](#receive-buffer-s7-300-s7-400)

### Serial transfer of a character (S7-300, S7-400)

#### Introduction

To exchange data between two or more communication partners, there are different networking possibilities available. The point-to-point connection between two communication partners is the simplest case of information exchange.

#### Point-to-point connection

For the point-to-point connection, the communication module forms the interface between a programmable logic controller and a communication partner. Data is transferred serially with the communication module for the point-to-point connection.

The addressing mechanisms of the selected transmission procedure areimplemented on the communication module. Therefore, the point-to-point connection is closed on the communication module and not on the communication partner, as it is with other connections.

#### Serial data transmission

During serial data transmission, the individual bits from a byte, which must be transferred, are transmitted sequentially in a determined sequence.

#### Unidirectional/bidirectional data traffic

Data transmission with the communication partner is processed independently by the communication module via the serial interface. The communication module is equipped with various drivers to accomplish this.

- unidirectional data traffic:

  - Printer driver
- bidirectional data traffic:

  - ASCII driver
  - 3964(R) procedure
  - Computer connection RK512
  - Modbus/USS

Data transmission via the serial interface is processed by the communication module depending on the physical interface and the selected driver.

#### Unidirectional data traffic - printout

During the printout (printer driver), n bytes of user data are output to a printer. A reception of characters does not occur. Individual control characters for data flow control (for example, XON/XOFF) are exceptions to this.

#### Bidirectional data traffic - operating modes

With bi-directional data traffic, there are two different operating modes for the communication module:

- Half-duplex mode (3964 (R procedure), ASCII driver, RK512, Modbus/USS)

  The data is transferred alternating in both directions between one or multiple communication partners. Half-duplex mode means that everything is sent or received at one point in time. The exceptions to this can be individual control characters for data flow control (for example, XON/XOFF), which can also be received/sent during transmission/reception operation.
- Full-duplex mode (ASCII-driver)

  The data is exchanged simultaneously between one or more communication partners; it may be sent and received at one point in time. Each communication partner must be able to simultaneously operate a transmission and reception set-up.

Only half-duplex mode can be used with an X27 interface module (RS422/485) set to RS485 (2-wire).

#### Asynchronous data transmission

Serial data transmission is performed asynchronously with the communication module. The so-called time grid simultaneous operation (fixed time grid for the transfer of a fixed character string) must only be maintained during the transmission of a character. Each transferred character precedes a synchronization impulse, also referred to as a start bit. The length of the start bit transmission is determined by the clock. The end of the character transfer is formed by the stop bit.

#### Agreements

In addition the start and stop bits, there are other agreements between the two communication partners required for serial data transmission. This includes:

- Transmission speed (baud rate)
- Character and acknowledgement delay time
- Parity
- Number of data bits
- Number of stop bits

#### Character frame

The data between communication module and a communication partner is transmitted via the serial interface in a 10, 11 or 12 bit character frame. Several data formats are available for each character frame. Configure the desired format of the data transmission in the properties dialog of the module. Depending on the particular communication module, not all the theoretically possible character frames (combinations) are available.

#### 10-Bit Character Frame

In the following illustration, three data formats of the 10-bit character frame are shown as an example.

![10-Bit Character Frame](images/25441006987_DV_resource.Stream@PNG-en-US.png)

10-Bit Character Frame

#### 11-Bit Character Frame

In the following illustration, three data formats of the 11-bit character frame are shown as an example.

![11-Bit Character Frame](images/23761134475_DV_resource.Stream@PNG-en-US.png)

11-Bit Character Frame

#### Character Delay Time

The following illustration shows the maximum permissible interval between two received characters within a message frame (character delay time).

![Character Delay Time](images/23761267851_DV_resource.Stream@PNG-en-US.png)

Character Delay Time

### Transmission integrity (S7-300, S7-400)

Transmission integrity plays an important role in the transmission of data and in selection of the transmission procedure. Generally speaking, the more layers of the reference model are applied, the greater the transmission integrity.

#### Classifying the supplied protocols

The figure below illustrates how these protocols of the communication module fit into the reference model:

![Classification of the existing protocols of the communication module in the reference model](images/21365150219_DV_resource.Stream@PNG-en-US.png)

Classification of the existing protocols of the communication module in the reference model

#### Mapping of protocols to the communication modules

| Protocol | CP 340 | CP 341 | CPU 313C-2 PtP | CPU 314C-2 PtP | CP 440 | CP 441 | ET 200S 1SI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Printer driver | ● | ● |  |  |  | ● |  |
| ASCII driver | ● | ● | ● | ● | ● | ● | ● |
| 3964(R) procedure | ● | ● | ● | ● | ● | ● | ● |
| Computer connection RK512 |  | ● |  | ● |  | ●<sup>2)</sup> |  |
| Modbus master |  | ● <sub>1)</sub> |  |  |  | ● <sup>1) 2)</sup> | ● |
| Modbus slave |  | ● <sub>1)</sub> |  |  |  | ● <sup>1) 2)</sup> | ● |
| USS-master |  |  |  |  |  |  | ● |
| <sup>1)</sup> A loadable driver with a dongle is needed for the Modbus protocol.   <sup>2)</sup> only CP 441-2 |  |  |  |  |  |  |  |

#### Transmission Integrity with the printer driver

Data integrity when using the printer driver:

- No data integrity precautions are taken for data transport with the printer driver.
- To prevent data from being lost in the event of the printer receive buffer overflowing, you can work with data flow control (XON/XOFF, RTS/CTS).
- When data is output to the printer, the printer's BUSY signal is evaluated. The communication module receives the BUSY signal as a CTS signal and evaluates it in the same way (see ASCII driver). Note that, when using CTS/RTS flow control, you must set the polarity of the BUSY signal to CTS = "OFF" on the printer.

#### Transmission Integrity with the ASCII driver

Data integrity when using the ASCII driver:

- When data is transmitted via the ASCII driver, there are no data integrity precautions other than the use of a parity bit (can also be canceled, depending on how the character frame is set). This means that, although this type of data transport has a very efficient throughput rate, security is not guaranteed.
- Using the parity bit makes it possible to detect an inverted bit in a character that is to be transmitted. If two or more bits of a character are inverted, this error can no longer be detected.
- To increase transmission integrity, a checksum and length specification for a message frame can be employed. These measures must be implemented by the user.
- A further increase in data integrity can be achieved by means of acknowledgment message frames in response to send or receive message frames. This is the case with high-level protocols for data communication (ISO 7-layer reference model).

#### Transmission Integrity with 3964(R)

**Enhanced data integrity through use of the 3964(R) procedure:**

- The Hamming distance with the 3964(R) is 3. This measures the integrity of a data transmission.
- The 3964(R) procedure ensures high transmission integrity on the transmission line. This high transmission integrity is achieved by means of a specified message-frame setup and release as well as the use of a block check character (BCC).

**Two different procedures for data transmission can be used, either with or without a block check character:**

- Data transmission without a block check character: **3964**
- Data transmission with a block check character: **3964(R)**

In this manual, the designation 3964(R) is used when descriptions and notes refer to both data transmission procedures.

#### Transmission integrity with RK512

Very high data security using RK512:

- The Hamming distance with the RK512 and 3964R is 4. The Hamming distance is a measure of the integrity for a data transmission.
- Using the RK512 computer connection ensures high transmission integrity on the transmission line (because RK512 uses the 3964R procedure for data transport).
- Further processing at the communication partner is ensured (because the RK512 interpreter checks the additional length specification in the header and, after storing the data in the destination data area of the communication partner, generates a message frame acknowledging the success or failure of the data transport).
- The RK512 computer connection independently guarantees the correct use of the 3964R procedure and the analysis/addition of the length specification as well as the generation of the response telegram. There is no user handling! All you need to do is evaluate the positive/negative final acknowledgment.

#### Transmission integrity for Modbus/USS

Data security when using the Modbus/USS driver.

- The Hamming distance for Modbus/USS is 4. The Hamming distance is a measure of the integrity for a data transmission.
- Using Modbus/USS guarantees high transmission integrity on the transmission line (through a CRC16 block check for Modbus and an XOR block check for USS).
- Further processing in the communication partner is assured because both Modbus and USS evaluate additional length information in the header and generate a (time-monitored) acknowledgment message frame relating to the successful/unsuccessful data transmission.

### Data transmission with ASCII driver (S7-300, S7-400)

This section contains information on the following topics:

- [Data Transmission with the ASCII Driver (S7-300, S7-400)](#data-transmission-with-the-ascii-driver-s7-300-s7-400)
- [Sending Data with the ASCII Driver (S7-300, S7-400)](#sending-data-with-the-ascii-driver-s7-300-s7-400)
- [Receiving Data with the ASCII Driver (S7-300, S7-400)](#receiving-data-with-the-ascii-driver-s7-300-s7-400)
- [RS485 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](#rs485-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)
- [RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)
- [Software/hardware handshake (S7-300, S7-400)](#softwarehardware-handshake-s7-300-s7-400)

#### Data Transmission with the ASCII Driver (S7-300, S7-400)

Assignment of the protocols to the communication modules, see: [Overview of the components and interfaces](#overview-of-the-components-and-interfaces-s7-300-s7-400)

##### Introduction

The ASCII driver controls data transmission via a point-to-point connection between the communication processor and a communication partner. This driver contains the physical layer (layer 1).

The structure of the message frames is left open through the S7 user passing on the complete send message frame to the communication processor. For the receive direction, the end criterion of a message must be configured. The structure of the send message frames may differ from that of the receive message frames.

The ASCII driver allows data of any structure (all printable ASCII characters as well as all other characters from 00 through FFH (with 8 data bit character frames) or from 00 through 7FH (with 7 data bit character frames) to be sent and received.

#### Sending Data with the ASCII Driver (S7-300, S7-400)

##### Sending Data

For sending, you specify the number of user data bytes to be transmitted in the length parameter when you call the respective send instruction. For more information, see the section "[Overview of the instructions](#overview-of-the-instructions-s7-300-s7-400)".

When you work with the end criterion "Character Delay Time" when receiving data, the ASCII driver pauses between two message frames when sending. You can call the send instruction at any time, but the ASCII driver only begins output when the time since the last message frame was sent is longer than configured character delay time.

> **Note**
>
> When XON/XOFF flow control is configured, the user data must not contain the configured XON or XOFF characters. The default settings are DC1 = 11H for XON and DC3 = 13H for XOFF.

If you work with the "end delimiter" criterion, you have a choice of three options:

- Send up to and including the end delimiter

  The end delimiter must be included in the data to be sent. Data is sent only up to and including the end delimiter, even if the data length specified in the instruction is longer.
- Send up to the length configured at the instruction

  Data is sent up to the length that is configured at the instruction. The last character must be the end delimiter.
- Send up to the length configured at the instruction and automatically append the end delimiter(s)

  Data is sent up to the length that is configured at the instruction. The end delimiter is automatically appended, in other words the end delimiters must not be included in the data to be sent. 1 or 2 characters more than the number specified at the instruction are sent to the partner, depending on the number of end delimiters.

When you work with the "fixed message frame length" end criterion, the amount of data transferred in the send direction is what you have specified for the length parameter of the instruction. The amount of data transferred in the receive direction, in other words, into the receive DB, is specified at the receiver using the "fixed message frame length" parameter in the properties dialog of the module. The two parameter settings must be identical, in order to ensure correct data traffic. A pause equal to the length of the character delay time (CDT) is inserted between two message frames when sending, to allow the partner to synchronize (recognize start of message frame).

If some other method of synchronization is used, the pause in sending can be deactivated in the properties dialog of the module.

##### Send operation

The figure below illustrates a send operation.

![ASCII driver, sequence of sending data](images/26021383307_DV_resource.Stream@PNG-en-US.png)

ASCII driver, sequence of sending data

#### Receiving Data with the ASCII Driver (S7-300, S7-400)

##### Selectable end criteria

For data transmission using the ASCII driver you can choose between three different end criteria. The end criterion defines when a complete message frame is received. The possible end criteria are as follows:

- After character delay time elapses

  The message frame has neither a fixed length nor a defined end delimiter; the end of the message is defined by a pause on the line (After character delay time elapses).
- On receipt of the end delimiter(s)

  The end of the message frame is marked by one or two defined end delimiters.
- On receipt of fixed number of characters

  The length of the receive message frames is always identical.

##### Code transparency

The code transparency of the procedure depends on the choice of configured end criterion and flow control:

- With one or two end delimiters

  - not code-transparent
- When end criterion is character delay time or fixed message frame length

  - code-transparent
- Code-transparent operation is not possible when the flow control XON/XOFF is used.

Code-transparent means that any character combinations can occur in the user data without the end criterion being recognized.

##### End criterion "After character delay time elapses"

When data is received, the end of the message frame is recognized when the character delay time expires. The received data is accepted from the CPU.

In this case, the character delay time must be set so that it reliably expires between two consecutive message frames. But it should be long enough so that the end of the message frame is not falsely identified whenever the partner in the connection takes a send pause within a message frame.

The figure below illustrates a receive operation with the end criterion "After character delay time elapses".

![Sequence of Receive Operation with End Criterion "Expiration of Character Delay Time"](images/25019358987_DV_resource.Stream@PNG-en-US.png)

Sequence of Receive Operation with End Criterion "Expiration of Character Delay Time"

##### End criterion end delimiter

When data is received, the end of the message frame is recognized when the configured end delimiter(s) arrive. The received data including the end delimiter(s) is accepted from the CPU.

If the character delay time expires while the message frame is being received, the receive operation is terminated. An error message is issued and the message frame fragment is discarded.

If you are working with end delimiters, transmission is not code-transparent, and you must make sure that the end code(s) are not in the user data of the user.

**Note the following when the last character in the received message frame is not the end delimiter.**

- End delimiter elsewhere in the message frame:

  All characters including the end delimiter are entered in the receive DB. The characters following the end delimiter

  - is discarded if the character delay time (CDT) expires at the end of the message frame.
  - is merged with the next message frame if a new message frame is received before the character delay time expires.
- End delimiter not included in message frame:

  The message frame

  - is discarded if the character delay time (CDT) expires at the end of the message frame.
  - is merged with the next message frame if a new message frame is received before the character delay time expires.

The figure below illustrates a receive operation with the end criterion "end delimiter".

![Sequence of receive operation with "End-of-Text Character" end criterion](images/25019670155_DV_resource.Stream@PNG-en-US.png)

Sequence of receive operation with "End-of-Text Character" end criterion

##### End criterion fixed message frame length

When data is received, the end of the message frame is recognized when the configured number of characters has arrived. The received data is accepted from the CPU.

If the character delay time expires before the configured number of characters has been reached, the receive operation is terminated. An error message is issued and the message frame fragment is discarded.

Note the following if the message frame length of the received characters does not match the configured fixed message frame length:

- Message frame length of received characters greater than configured fixed message frame length:

  All characters received after the configured fixed message frame length is reached

  - is discarded if the character delay time (CDT) expires at the end of the message frame.
  - is merged with the next message frame if a new message frame is received before the character delay time expires.
- Message frame length of received characters less than configured fixed message frame length:

  The message frame

  - is discarded if the character delay time (CDT) expires at the end of the message frame.
  - is merged with the next message frame if a new message frame is received before the character delay time expires.

The figure below illustrates a receive operation with the end criterion "fixed message frame length".

![Sequence of receive operation with "Fixed Message Frame Length" end criterion](images/25019712523_DV_resource.Stream@PNG-en-US.png)

Sequence of receive operation with "Fixed Message Frame Length" end criterion

##### Receive buffer of the module

The receive buffer of the module can be up to up to 4096 bytes, depending on the communication module.

During configuration, you can specify if:

- **CP and CPU 31xC-2 PtP**
    
  the receive buffer should be deleted at startup or overwriting of data in the receive buffer should be prevented. You can also specify the value range (1 to 250) for the number of buffered receive message frames.
- **ET 200S 1SI**
    
  the receive buffer should be deleted on startup and if an overwriting of the data in the receive buffer should be avoided. Additionally, you can activate or block the buffering of received message frames.

The receive buffer on the module is a ring buffer:

- If several message frames are entered in the receive buffer of the module, the following applies: it is always the oldest message frame that is sent from the module to the CPU.
- If you only want to transfer the newest message frame, you must:

  - **CP and CPU 31xC-2 PtP**
      
    set "1" as the number of buffered message frames and disable the overwrite protection.
  - **ET 200S 1SI**block the dynamic message frame and disable the overwrite protection.

    > **Note**
    >
    > If constant reading of the received data from the user program is interrupted for a time, you may find that when the received data is requested again, the CPU first receives old message frames from the module before it receives the most recent one.
    >
    > During this interruption, the old message frames were either on the way between the module and CPU or had already been received by the instruction.

#### RS485 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)

##### RS485 mode

When you run the ASCII driver in RS485 mode (half-duplex, two-wire mode), you must take steps in the user program to ensure that only one user sends data at any one time. If two users send data simultaneously, the message frame is corrupted.

##### Switch-over Times for RS485 Module in Half-Duplex Mode

The maximum switch-over time between sending and receiving is 1 ms.

#### RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)

##### RS232C accompanying signals

The following RS232C accompanying signals are available on the modules with the RS232C interface:

|  |  |  |
| --- | --- | --- |
| DCD | (input) | Data carrier detect |
| DTR | (Output) | Data terminal ready;  module ready for operation |
| DSR | (input) | Data set ready;  communication partner ready for operation |
| RTS | (Output) | Request to send,  module ready to send |
| CTS | (input) | Clear to send;  communication partner can receive data from the module (response to RTS = ON of the communication module) |
| RI | (input) | Ring indicator, |

When the module is switched on, the output signals are in the OFF state (inactive).

You can configure the way in which the DTR/DSR and RTS/CTS control signals are used in the properties dialog of the module or control them via instructions in the user program.

##### Operate RS232C accompanying signals

The RS232C accompanying signals can be used as follows:

- When automatic use of all RS232C accompanying signals is configured
- When data flow control (RTS/CTS) is configured
- via the instructions V24_STAT and V24_SET

  > **Note**
  >
  > When automatic operation of the R232C accompanying signals is configured, neither RTS/CTS data flow control nor RTS and DTR control by means of the V24_SET instruction are possible! When RTS/CTS data flow control is configured, RTS control by means of the V24_SET is not possible! On the other hand, it is always possible to read all RS232C accompanying signals using the V24_STAT instruction.

The sections that follow describe how the control and evaluation of the RS232C accompanying signals is handled.

##### Automatic use of accompanying signals

Automatic operation of the RS232C accompanying signals on the communication module is realized as follows:

- As soon as the module is switched by configuration to an operating mode with automatic operation of the RS232C accompanying signals, it sets RTS line to OFF and DTR line to ON (communication module ready for use).

  This prevents sending and receiving of message frames until the DTR line is set to ON. As long as DTR remains set to OFF, no data is received via the RS232C interface. If a send job is made, it is aborted with a corresponding error message.
- When a send job is made, RTS is set to ON and the configured data output waiting time starts. When the data output time elapses and CTS = ON, the data is sent via the RS232C interface.
- If the CTS line is not set to ON within the data output time so that data can be sent, or if CTS changes to OFF during transmission, the send job is aborted and an error message generated.
- Once the data has been sent and the configured clear RTS time has elapsed, the RTS line is set to OFF. The CP does not wait for CTS to change to OFF.
- Data can be received via the RS232C interface as soon as the DSR line is set to ON. If the receive buffer of the communication module threatens to overflow, there is no response from the communication module.
- If DSR changes from ON to OFF, an active send job as well as the receipt of data will be canceled with an error message. The message "DSR = OFF (automatic use of V24 signals)" is entered in the diagnostic buffer of the module .

  > **Note**
  >
  > When automatic operation of the R232C accompanying signals is configured, neither RTS/CTS data flow control nor RTS and DTR control by means of the V24_SET instruction are possible!
  >
  > The "Clear RTS time" must be set in the properties dialog of the module so that the communication partner can receive the last characters of the message frame in their entirety before RTS, and thus the send job, is revoked. The "data output waiting time" must be set so that the communication partner can be ready to receive before the time elapses.

##### Time Diagram

The figure illustrates the chronological sequence of a send job.

![Time diagram of automatic use of the RS232C accompanying signals](images/21376069387_DV_resource.Stream@PNG-en-US.png)

Time diagram of automatic use of the RS232C accompanying signals

##### Tasks of the instruction command V24_STAT/SET

The V24_STAT instruction command allows the status of each RS232C accompanying signal to be determined. The V24_SET allows the DTR and RTS output signals to be controlled.

#### Software/hardware handshake (S7-300, S7-400)

##### Introduction

Handshake protocol to control the flow of data between two communication partners. The use of the handshake procedure prevents data from getting lost during transmission when the two devices are operating at different rates.

##### Handshake procedure

There are essentially two types of handshaking here:

- Software handshaking (e.g. XON/XOFF)
- Hardware handshaking (e.g. RTS/CTS)

Data flow control is implemented as follows on the communication module:

- As soon as the module is switched by configuration to an operating mode with flow control, it sends the XON character or it sets the RTS line to ON.
- When the configured number of message frames is reached, or alternatively 50 characters before the receive buffer overflows (size of the receive buffer: 4096 bytes), the module sends XOFF character or sets the RTS line to OFF. If the communication partner continues to send data regardless of this, the receive buffer overflows and an error message is generated. The data received in the last message frame is discarded.
- As soon as a message frame is retrieved by the S7-CPU and the receive buffer is ready to receive, the module sends the XON character or sets the RTS line to ON.
- If the module receives the XOFF character, or the CTS control signal is set to OFF, the module interrupts the transmission. If neither an XON character is received nor CTS is set to ON after a configured time has elapsed, the transmission is aborted and an appropriate error message (0708H) is entered in the error message area of the module.

  > **Note**
  >
  > When RTS/CTS data flow control is configured, you must fully wire the interface signals in the plug connection. When RTS/CTS data flow control is configured, RTS control by means of the V24_SET is not possible!

### Data transmission with 3964(R) (S7-300, S7-400)

This section contains information on the following topics:

- [Data Transmission with the 3964(R) Procedure (S7-300, S7-400)](#data-transmission-with-the-3964r-procedure-s7-300-s7-400)
- [Control characters (S7-300, S7-400)](#control-characters-s7-300-s7-400)
- [Block Checksum (S7-300, S7-400)](#block-checksum-s7-300-s7-400)
- [Sending data with 3964(R) (S7-300, S7-400)](#sending-data-with-3964r-s7-300-s7-400)
- [Receiving data with 3964(R) (S7-300, S7-400)](#receiving-data-with-3964r-s7-300-s7-400)

#### Data Transmission with the 3964(R) Procedure (S7-300, S7-400)

Assignment of the protocols to the communication modules, see: [Overview of the components and interfaces](#overview-of-the-components-and-interfaces-s7-300-s7-400)

##### Introduction

The 3964(R) procedure controls point-to-point data exchange between the communication processor and a communication partner. As well as the physical layer (layer 1), the 3964(R) procedure also incorporates the data-link layer (layer 2).

##### Startup

The figure below illustrates the start-up of the 3964(R) procedure.

![Flow diagram of the start-up of the 3964(R) procedure](images/21370682891_DV_resource.Stream@PNG-en-US.png)

Flow diagram of the start-up of the 3964(R) procedure

#### Control characters (S7-300, S7-400)

##### Introduction

The RK 512 computer connection provides a very high degree of data integrity. During data transmission, the 3964(R) procedure adds control characters to the information data (data-connection layer). These control characters allow the communication partner to check whether the data has arrived complete and without errors.

##### The Control Characters of the 3964(R) Procedure

The 3964(R) procedure analyzes the following control codes:

- **STX**Start of Text; start of character string for transfer
- **DLE**Data Link Escape; data connection escape
- **ETX**End of Text; end of character string for transfer
- **BCC**Block Check Character (3964(R) only)
- **NAK**Negative Acknowledge

  > **Note**
  >
  > If DLE is transmitted as an information string, it is sent twice so that it can be distinguished from the control code DLE during connection setup and release on the send line (DLE duplication). The receiver then reverses the DLE duplication.

##### Priority

With the 3964(R) procedure, one communication partner must be assigned a higher priority and the other partner a lower priority. If both partners begin connection setup at the same time, the partner with the lower priority will defer its send request.

#### Block Checksum (S7-300, S7-400)

##### Block Checksum

With the 3964(R) transmission protocol, data integrity is increased by the additional sending of a block check character (BCC).

![Block Checksum](images/21370454923_DV_resource.Stream@PNG-en-US.png)

Block Checksum

The block checksum is the even longitudinal parity (EXOR operation on all data bytes) of a sent or received block. Its calculation begins with the first byte of user data (first byte of the message frame) after the connection setup, and ends after the DLE ETX code on connection release.

> **Note**
>
> If DLE duplication occurs, the DLE code is accounted for twice in the BCC calculation.

#### Sending data with 3964(R) (S7-300, S7-400)

##### Process of Data Transmission when Sending

The figure below illustrates the transmission sequence when data is sent with the 3964(R) procedure.

![Data traffic when sending with the 3964(R) procedure](images/26571319307_DV_resource.Stream@PNG-en-US.png)

Data traffic when sending with the 3964(R) procedure

##### Establishing a Send Connection

To establish the connection, the 3964(R) procedure sends the control code STX. If the communication partner responds with the DLE code before the acknowledgment delay time expires, the procedure switches to send mode.

If the communication partner answers with NAK or with any other control code (except for DLE or STX), or the acknowledgment delay time expires without a response, the procedure repeats the connection setup. After the defined number of unsuccessful setup attempts, the procedure aborts the connection setup and sends the NAK code to the communication partner. The communication module enters a corresponding error number in the error message area.

##### Sending Data

If a connection is successfully established, the user data contained in the output buffer of the communication processor is sent to the communication partner with the chosen transmission parameters. The partner monitors the times between incoming characters. The interval between two characters must not exceed the character delay time.

If the communication partner sends the NAK control code during an active send operation, the procedure aborts its transmission of the block and tries again as described above, beginning with connection setup. If a different code is sent, the procedure first waits for the character delay time to expire and then sends the NAK code to change the mode of the communication partner to idle. Then the procedure starts to send the data again with the connection setup STX.

##### Releasing a Send Connection

Once the contents of the buffer have been sent, the procedure adds the codes DLE, ETX and with the 3964R only the block checksum BCC as the end identifier, and waits for an acknowledgment code. If the communication partner sends the DLE code within the acknowledgment delay time, the data block has been received without errors. If the communication partner responds with NAK, any other code (except DLE), or a damaged code, or if the acknowledgment delay time expires without a response, the procedure starts to send the data again with the connection setup STX.

After the defined number of attempts to send the data block, the procedure stops trying and sends an NAK to the communication partner. The communication module reports the error in the error message area.

##### Sending with the 3964(R) Procedure

The figure below illustrates sending with the 3964(R) procedure.

![Flow diagram of sending with the 3964(R) procedure](images/21370315787_DV_resource.Stream@PNG-en-US.png)

Flow diagram of sending with the 3964(R) procedure

#### Receiving data with 3964(R)  (S7-300, S7-400)

##### Process of Data Transmission when Receiving

The figure below illustrates the transmission sequence when data is received with the 3964(R) procedure.

![Data traffic when receiving with the 3964(R) procedure](images/26592913931_DV_resource.Stream@PNG-en-US.png)

Data traffic when receiving with the 3964(R) procedure

> **Note**
>
> As soon as it is ready, the 3964(R) procedure sends a single NAK to the communication partner to set the latter to idle.

##### Establishing a Receive Connection

In idle mode, when there is no send job to be processed, the procedure waits for the communication partner to establish the connection.

If no empty receive buffer is available during a connection setup with STX, a wait time of 400 ms is started. If, after this time, there is no empty receive buffer, the system program reports the error in the error message area of the module. and the procedure sends a NAK and returns to idle mode. Otherwise, the procedure sends a DLE and receives the data as described above.

If the idle procedure receives any control code except for STX or NAK, it waits for the character delay time to expire, then sends the code NAK. The communication module reports the error in the error message area of the module.

##### receiving data

After a successful connection setup, the receive characters that are arrive are stored in the receive buffer. If two consecutive DLE codes are received, only one of these is stored in the receive buffer.

After each receive character, the procedure waits out the character delay time for the next character. If this period expires before another character is received, an NAK is sent to the communication partner. The communication module reports the error in the error message area of the module. The 3964(R) procedure does not initiate a repetition.

If transmission errors occur during receiving (lost character, frame error, parity error, etc.), the procedure continues to receive until the connection is closed. NAK is then sent to the communication partner. A repetition is then expected. If the block still cannot be received after the number of transmission attempts defined in the static parameter set, or if the communication partner does not start the repetition within a block wait time of 4 seconds, the procedure aborts the receive operation. The communication module reports the first transmission error and the final abort in the error message area of the module.

##### Releasing a Receive Connection

When the 3964 procedure detects a DLE ETX character string, it ends the receiving operation and confirms the successfully received block by sending a DLE signal to the communication partner. When errors are found in the received data, it outputs a NAK signal to the communication partner. A repetition is then expected.

If the 3964R procedure recognizes the string DLE ETX BCC, it stops receiving and compares the received block check character with the longitudinal parity calculated internally. If the BCC is correct and no other receive errors have occurred, the CP sends the code DLE to the communication partner. If the BCC is correct and no other receive errors have occurred, the 3964R procedure sends a DLE and returns to idle mode. If the BCC is faulty or a different receiving error occurs, an NAK is sent to the communication partner. A repetition is then expected.

##### Receiving with the 3964(R) Procedure

The figure below illustrates receiving with the 3964(R) procedure.

![Flow diagram of receiving with the 3964(R) procedure (part 1)](images/21373396107_DV_resource.Stream@PNG-en-US.png)

Flow diagram of receiving with the 3964(R) procedure (part 1)

![Flow diagram of receiving with the 3964(R) procedure (part 2)](images/21370372619_DV_resource.Stream@PNG-en-US.png)

Flow diagram of receiving with the 3964(R) procedure (part 2)

### Data transmission with Rk512 (S7-300, S7-400)

This section contains information on the following topics:

- [Data transmission with the RK512 computer connection (S7-300, S7-400)](#data-transmission-with-the-rk512-computer-connection-s7-300-s7-400)
- [Sending data with RK512 (S7-300, S7-400)](#sending-data-with-rk512-s7-300-s7-400)
- [Fetching data with RK512 (S7-300, S7-400)](#fetching-data-with-rk512-s7-300-s7-400)

#### Data transmission with the RK512 computer connection (S7-300, S7-400)

Assignment of the protocols to the communication modules, see: [Overview of the components and interfaces](#overview-of-the-components-and-interfaces-s7-300-s7-400)

##### Introduction

The RK512 computer connection controls data transmission in a point-to-point connection between the communication module and a communication partner.

Unlike the 3964(R) procedure, the RK512 computer connection includes not only the physical layer (layer 1), and the data link layer (layer 2), but also the transport layer (layer 4) of the ISO reference model. The RK512 computer connection also offers greater data security and enhanced addressing options.

##### Response message frame

The RK512 computer connection answers each correctly received command message frame with a response message frame to the client (transport layer). This allows senders to check whether their data has arrived undamaged at the CPU of the communication partner or whether the data they require is available on the CPU of the communication partner.

##### Command message frame

Command message frames are either SEND frames or FETCH frames.

##### SEND frame

A SEND frame is created when the communication module sends a command message frame with user data, and the communication partner replies with a response message frame without user data.

##### FETCH frame

A FETCH frame is created when the communication module sends a command message frame without user data, and the communication partner replies with a response message frame with user data.

##### Continuation message frame

If the volume of data exceeds 128 bytes, SEND and FETCH frames are automatically sent with continuation message frames.

##### Message frame header

With RK512, each message frame begins with a message frame header. It can contain message frame IDs, information on the data destination and source and an error number.

##### Structure of the message frame header

The table below indicates the structure of the header of the command message frame.

Format of the message frame header for the command message frame (RK512)

| Byte | Meaning |
| --- | --- |
| 1 | Message frame ID in command message frames (00H),  in continuation command message frames (FFH) |
| 2 | Message frame ID (00H) |
| 3 | 'A' (41H) for SEND job with destination DB or   'O' (4FH) for SEND job with destination DX or  'E' (45H) for FETCH job |
| 4 | Data to be transmitted consist of (only 'D' possible for sending):  'D' (44H)=data block  'I' (45H) = Input bytes   'O' (41H) = output bytes  'M' (4DH)=flag bytes  'C' (5AH)= counter cells   'T' (54H) = time cells |
| 5 and 6 | Data destination of SEND/PUT job or data source of GET job e.g. byte 5 = DB no., byte 6 = DW no.  (RK512 addressing describes data source and destination with word limits. Conversion to byte addresses in SIMATIC S7 is automatic.) |
| 7 and 8 | Length of high byte Length of data to be transmitted according to type in bytes or  Length of low byte words |
| 9 | Byte number of the communication flag;   FFH is shown here if you have not specified an interprocessor communication flag. |
| 10 | **Bit 0 to 3:** Bit number of the communication flag,   The protocol enters FH here if you have not specified an interprocessor communication flag.   **Bit 4 to 7:** CPU number (number from 1 to 4);  If you have not specified a CPU number but you have specified an interprocessor communication flag, OH is displayed here; if you specified neither a CPU number nor an interprocessor communication flag, FH is shown here. |

The letters in bytes 3 and 4 are ASCII characters.

The header of the continuation command ^message frame consists of bytes 1 to 4 only.

##### Response message frame

Once the command message frame has been transmitted, the RK512 expects a response message frame from the communication partner within the monitoring time. The length of the monitoring time is 20 seconds irrespective of the transmission speed (baud rate).

Depending on the PtP module used, this monitoring time can be reduced by user configuration in the properties dialog of the module. By selecting the "transmission-rate dependent" option, monitoring is performed with the following maximum waiting times:

Transmission-rate dependent monitoring time for response telegram

| Transmission rate | Monitoring time |
| --- | --- |
| - 300 baud | 10 s |
| - 600 baud | 7 s |
| - 1200 baud | 5 s |
| - from 38400 baud | 3 s |

The "grayed" "Maximum wait time" field is used only for showing the configured monitoring time and cannot be edited!

##### Structure and contents of the response message frame

The response message frame consists of 4 bytes and contains information on the progress of the job.

| Byte | Meaning |
| --- | --- |
| 1 | Message frame ID in response message frames (00H),  in continuation response message frames (FFH) |
| 2 | Message frame ID (00H) |
| 3 | Displays 00H |
| 4 | Error number of the communication partner in the response message frame:  - **00H** if transmission was error-free - **> 00H** error number   The error number in the response message frame automatically causes an error number to be entered in the error message area of the module. |

#### Sending data with RK512 (S7-300, S7-400)

##### Process of Data Transmission when Sending

The figure below shows the transmission sequence when sending data with a response message frame using the RK512 computer connection.

![Data traffic when sending with a response frame](images/25943780363_DV_resource.Stream@PNG-en-US.png)

Data traffic when sending with a response frame

##### Sending Data

The SEND job is executed in the following sequence:

- Active partner

  Sends a SEND message frame. This contains a message frame header and data.
- Passive partner

  Receives the message frame, checks the header and the data, and acknowledges it with a response frame after passing the data on to the CPU.
- Active partner

  Receives the response message frame and terminates the SEND job.

  > **Note**
  >
  > If the user data of the SEND job is not received correctly by the CPU or an error occurs in the message frame header, the communication partner enters an error number in the 4th byte of the response message frame. This does not apply when protocol errors occur.

##### Continuation SEND message frame

A continuation SEND job is started when the amount of data exceeds 128 bytes. The procedure is similar to the SEND job.

If more than 128 bytes are sent, the extra bytes are automatically transmitted in one or more continuation message frames. Each continuation SEND frame is acknowledged with a continuation response message frame.

The figure below shows the data transmission sequence when sending a continuation SEND message frame with a continuation response message frame.

The continuation response message frame for the last continuation SEND frame is only sent after successful transfer of the entire user data to the CPU.

![Sequence of a continuation SEND message frame with a continuation response message frame](images/25945065867_DV_resource.Stream@PNG-en-US.png)

Sequence of a continuation SEND message frame with a continuation response message frame

#### Fetching data with RK512 (S7-300, S7-400)

##### Procedure for fetching data with RK512

The figure below shows the transmission sequence when fetching data with a response message frame using the RK512 computer connection.

![Data traffic when fetching with a response message frame](images/26593056267_DV_resource.Stream@PNG-en-US.png)

Data traffic when fetching with a response message frame

##### Fetching data

The FETCH job is executed in the following sequence:

- Active partner

  Sends a FETCH frame. This contains a message frame header.
- Passive partner

  Receives the message frame, checks the header, fetches the data from the CPU, and acknowledges this with a response frame containing the data. This contains the data.
- Active partner

  Receives the response message frame, passes user data received in the response message frame to the CPU, and terminates the FETCH job.

If there is an error number (not equal to 0) in the 4th byte, the response frame does not contain any data.

If more than 128 bytes are requested, the extra bytes are automatically fetched in one or more continuation message frames. Each continuation FETCH frame is acknowledged with a continuation response message frame (with more user data).

After receipt of the last continuation response message frame (with the last user data block), the entire user data are passed to the CPU and the FETCH job is completed.

> **Note**
>
> If the FETCH message frame is not correctly processed by the CPU or if an error occurs in the message frame header, the communication partner enters an error number in the 4th byte of the response message frame. This does not apply when protocol errors occur.

##### Continuation FETCH frame

The figure below shows the transmission sequence when fetching data with a continuation response message frame.

![Sequence of a FETCH frame with a continuation response message frame](images/25945419659_DV_resource.Stream@PNG-en-US.png)

Sequence of a FETCH frame with a continuation response message frame

##### Quasi-full-duplex operation

Quasi-full-duplex mode means: The partners can send command and response frames at any time as long as the other partner is not sending. The maximum nesting depth for command and response frames is "1". The next command message frame, therefore, cannot be processed until the previous one has been answered with a response frame.

It is possible under certain circumstances - when both partners want to send - to transmit a SEND or FETCH message frame from the partner before the response message frame. This can occur, for example, when a SEND or FETCH message frame from the partner is entered in the output buffer of the communication module before the response message frame.

In the following figure, the continuation response message frame for the first SEND frame is only sent after the SEND frame of the partner.

![Quasi-full-duplex operation](images/21374460043_DV_resource.Stream@PNG-en-US.png)

Quasi-full-duplex operation

##### RK512 CPU jobs

The figure below shows the sequences involved in the RK512 computer connection when CPU jobs are made.

![Sequence for data transmission from CPU jobs with RK512](images/21374483211_DV_resource.Stream@PNG-en-US.png)

Sequence for data transmission from CPU jobs with RK512

##### RK512 partner jobs

The figure below shows the sequences involved in the RK512 computer connection when partner jobs are made.

![Flow chart for data transmission from partner jobs with RK512](images/21375620235_DV_resource.Stream@PNG-en-US.png)

Flow chart for data transmission from partner jobs with RK512

### Data transmission with printer driver (S7-300, S7-400)

This section contains information on the following topics:

- [Data transmission with the printer driver (S7-300, S7-400)](#data-transmission-with-the-printer-driver-s7-300-s7-400)

#### Data transmission with the printer driver (S7-300, S7-400)

Assignment of the protocols to the communication modules, see: [Overview of the components and interfaces](#overview-of-the-components-and-interfaces-s7-300-s7-400)

##### Introduction

The printer driver allows you to output message texts with the date and time to a printer. This enables you to monitor simple processes, print error or fault messages or issue instructions to the operating personnel, for example.

The printer driver contains the physical layer (layer 1).

##### Message texts and parameters for printout

In the properties dialog of the module, you configure message text and set the parameters (page layout, character set, control characters) for the printout. Message texts and printout parameters are transmitted to the communication module together with the module parameters when it starts up.

- **Message texts:**

  You can configure message texts with variables and control instructions (e.g. for bold, narrow, wide or italic type and underlining). Each message text is assigned a number during parameter assignment. The printout of a specific message text with CP 441 modules is made by specifying a reference (to the memory cell containing the message text no.) at the send parameters SD_1 to SD_4 of the instruction. With CP 34x modules, this is done by specifying the message text number in a format string when calling the instruction.

  You can also save configured message texts to an external text file (SDB name, max. 8 ASCII characters), and edit them with a suitable editor. In this way, the texts can be translated and then read back, for example.

  Structure of the message text file:

  <Versions number>

  <Number of the message>:<Content the message>
- **Page layout:**

  You can configure the margins, optional line breaks and headers and footers of the page layout.
- **Character set:**

  STEP 7 converts the ANSI character set to the printer character set using a character conversion table. You can change a character conversion table suggested for a printer type in order to include special characters required for a particular language, for example.
- **Control characters:**

  Using a control character table, you can change the control instructions in the message text for printer emulation to switch on and off bold, narrow, wide or italic type and underline, and to add control characters.

##### Variables

Up to 4 variables (3 + text message number) are displayed in a message text. Variable values can be transmitted from the CPU to the communication module. The following variables can be displayed:

- Calculated values of the user program (e.g. fill levels)
- Date and time
- Strings (string variable)
- Other message texts

A conversion instruction must be specified for each variable in the configured message text or in the format string, in which the meaning and the output format of the variable value are encrypted.

##### Format string

You can use the format string to define the appearance and the composition of a message text. The format string can consist of:

- Text (any printable characters, e.g. Fill level l reached at ...!)
- Conversion instructions for variables (such as %N = pointer to the message text number x, where x is a variable value (see Example 2 below))

  For each variable, exactly one conversion instruction must be present in the format string or configured message text. The conversion instructions are applied to the variables according to their order.
- Control instructions with control characters for bold, narrow, wide, italics, underline (e.g. \B = bold on) or with additional control characters you have defined

You can use additional control characters when you enter these characters into the control character table in the properties dialog of the module and configure the new communication module.

##### Other functions

In addition to the output of message texts, you can use the following functions for the printout. You run these functions from a format string.

- Set page number (format string = %P)
- Start new page (format string = \F)
- Print with/without line break (\x at the end of the format string)

Note that a line feed is performed by default for each printout.

##### Examples

**Example 1:** Fill level "200" l reach at "5:30 pm"!

Format string = Fill level %i l reach at %Z!  
Variable 1 = time  
Variable 2 = level

**Example 2:** The chamber pressure "drops"

Format string = %N %S  
Variable 1 = 17 (message text no. 17: The chamber pressure ...)  
Variable 2 = Reference to string (string variable: ... drops)

**Example 3:** (Set page number to 10)

Format string = %P  
Variable 1 = 10 (page number: 10)

##### Printout

To output n bytes of user data to a printer, the format string and the variables of the message text must be specified as parameters when the instruction is called.

During output the data is edited for printing. Preparation for printing is carried out according to the parameters in the properties dialog of the module (page layout, character set, control characters, etc.).

Characters are not received during printout. The exception to this are any flow control characters that have been configured. Any characters received are not adopted.

##### Message text output

The figure below illustrates the sequence of operations at printout.

![Flow chart of printout](images/25946609163_DV_resource.Stream@PNG-en-US.png)

Flow chart of printout

##### Software/hardware handshake

Handshaking controls the data flow between two communication partners. Handshaking ensures that data is not lost in transmissions between devices that work at different speeds.

You can also send printout data with flow control. There are essentially two types of handshaking here:

- Software handshaking (e.g. XON/XOFF)
- Hardware handshaking (e.g. RTS/CTS)

**Implementation of flow control on the communication module for printout is performed as follows:**

- As soon as the communication module is switched by configuration to an operating mode with flow control, it sends the XON character or sets the RTS line to ON.
- If the communication module receives the XOFF character or the CTS control signal is set to OFF, the communication module interrupts the output of characters. If no XON is received or CTS is not set to ON after a configurable time, the printout is interrupted and a corresponding error message (0708H) is generated at the STATUS output of the instruction.

  > **Note**
  >
  > If you configure RTS/CTS flow control, be sure the interface signals used are fully wired in making the plug connection.

##### BUSY signal

The communication module evaluates the "BUSY" control signal of the printer. The printer reports to CP 34x1 its readiness to receive

- With CP 34x 20mA-TTY: With power on RxD line.
- With CP 34x RS232C and CP 34x RS422/485: With CTS = "ON" signal.

  > **Note**
  >
  > If you configure RTS/CTS flow control, you must set the polarity of the BUSY signal on the printer as follows:
  >
  > - BUSY signal: CTS = "OFF"
  >
  > Note that some printers show the BUSY signal using the DTR signal. In this case, you need to rewire the cable to the communication module correspondingly.

### Indicator for end of a message freme (S7-300, S7-400)

#### End criteria

You can choose between three different end criteria for data transmission using the ASCII driver:

- **After character delay time elapses**
- **On receipt of the end delimiter(s)**
- **On receipt of fixed number of characters**

#### Protocol parameters

The following table provides a description of the protocol parameters.

Protocol parameters (ASCII driver)

| Parameters | Description | Value range | Default value |
| --- | --- | --- | --- |
| End detection indicator of a receive message frame | Specifying the criteria that determine the end of message frames. | - After character delay time elapses - On receipt of the end delimiter(s) - On receipt of fixed number of characters | After character delay time elapses |
| End delimiter 1 <sup>1</sup> | Code of the first end detection. | - With 7 data bits: 0 to 7FH (Hex) <sup>2</sup> - With 8 data bits:  0 to FFH (Hex) <sup>2</sup> | 3 (03H = ETX) |
| End delimiter 2 <sup>1</sup> | Code of the second end detection, if selected. | - With 7 data bits: 0 to 7FH (Hex) <sup>2</sup> - With 8 data bits: 0 to FFH (Hex) <sup>2</sup> | 0 |
| <sup>1</sup> Only for the end delimiter end criterion.   <sup>2</sup> Depending on whether you configure 7 or 8 data bits for the character frame. |  |  |  |

#### Further Information

A detailed description of data reception with the ASCII driver can be found in section [Receiving Data with the ASCII Driver](#receiving-data-with-the-ascii-driver-s7-300-s7-400).

### Data flow control and secondary signals (S7-300, S7-400)

#### Introduction

The communication module enables point-to-point communication with SIMATIC modules and with third-party products.

#### Supported interface functions

Different driver functions can be used depending on the interface used:

Functions of the communication module based on the interface employed

|  |  | RS232C |  | 20mA TTY | X27 (RS422/485) |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | RS422* | RS485* |  |  |  |
| **Function CP 441** |  |  |  |  |  |  |  |
| **3964(R) procedure** |  | **●** |  | **●** | **●** | **-** |  |
| **Computer connection RK512** |  | **●** |  | **●** | **●** | **-** |  |
| **ASCII driver:** |  | **●** |  | **●** | **●** | **●** |  |
| - Operation of the RS232C accompanying signals |  | ● |  | - | - | - |  |
| - Controlling/reading the RS232C accompanying signals with instructions |  | ● |  | - | - | - |  |
| - RTS/CTS data flow control |  | ● |  | - | - | - |  |
| - XON/XOFF data flow control |  | ● |  | ● | ● | - |  |
| **Printer driver:** |  | **●** |  | **●** | **●** | **●** |  |
| - RTS/CTS data flow control |  | ● |  | - | - | - |  |
| - XON/XOFF data flow control |  | ● |  | ● | ● | - |  |
| **Function CP 440** |  |  |  |  |  |  |  |
| **3964(R) procedure** |  |  |  |  | **●** |  | **-** |
| **ASCII driver:** |  |  |  |  | **●** |  | **●** |
| - XON/XOFF data flow control |  |  |  |  | ● |  | - |
| **Function CP 341** |  |  |  |  |  |  |  |
| **3964(R) procedure** | **●** |  | **●** |  | **●** |  | **-** |
| **Computer connection RK512** | **●** |  | **●** |  | **●** |  | **-** |
| **ASCII driver:** | **●** |  | **●** |  | **●** |  | **●** |
| - Operation of the RS232C accompanying signals | ● |  | - |  | - |  | - |
| - Controlling/reading the RS232C accompanying signals with instructions | ● |  | - |  | - |  | - |
| - RTS/CTS data flow control | ● |  | - |  | - |  | - |
| - XON/XOFF data flow control | ● |  | ● |  | ● |  | - |
| **Printer driver:** | **●** |  | **●** |  | **●** |  | **●** |
| - RTS/CTS data flow control | ● |  | - |  | - |  | - |
| - XON/XOFF data flow control | ● |  | ● |  | ● |  | - |
| **Function CP 340** |  |  |  |  |  |  |  |
| **3964(R) procedure** | **●** |  | **●** |  | **●** |  | **-** |
| **ASCII driver:** | **●** |  | **●** |  | **●** |  | **●** |
| - Operation of the RS232C accompanying signals | ● |  | - |  | - |  | - |
| - Controlling/reading the RS232C accompanying signals with instructions | ● |  | - |  | - |  | - |
| - RTS/CTS data flow control | ● |  | - |  | - |  | - |
| - XON/XOFF data flow control | ● |  | ● |  | ● |  | - |
| **Printer driver:** | **●** |  | **●** |  | **●** |  | **●** |
| - RTS/CTS data flow control | ● |  | - |  | - |  | - |
| - XON/XOFF data flow control | ● |  | ● |  | ● |  | - |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Function ET 200S 1SI** |  |  |  |  |
| **3964(R) procedure** | **●** |  | **●** | **-** |
| **ASCII driver:** | **●** |  | **●** | **●** |
| - Operation of the RS232C accompanying signals | ● |  | - | - |
| - Controlling/reading the RS232C accompanying signals with instructions | ● |  | - | - |
| - RTS/CTS data flow control | ● |  | - | - |
| - XON/XOFF data flow control | ● |  | ● | - |
| * The difference between RS422 and RS485 is defined by configuration. |  |  |  |  |

#### Application options for the communication modules

Depending on the communication module used, you can establish a point-to-point connection with various Siemens modules and with third-party products:

- SIMATIC S5 through 3964(R) driver or RK512 with corresponding interface module at S5 end
- Siemens BDE-terminals ES 2-family through 3964(R) driver
- MOBY I (ASM 420/421, SIM), MOBY L (ASM 520) and capture station ES 030K through 3964R-driver
- PCs via procedure 3964(R) (development tools exist for programming on the PC: PRODAVE DOS 64R (6ES5 897-2UD11) for MS-DOS, PRODAVE WIN 64R   
  (6ES5 897-2VD01) for Windows or the ASCII driver)
- Bar code reader via 3964(R) driver or ASCII driver
- PLC from other manufacturers via 3964(R), ASCII driver or RK512
- other devices with simple protocol structures via corresponding protocol adjustment with the ASCII driver
- Additional devices that also feature 3964(R) drivers or RK512
- Printer (HP-Deskjet, HP-Laserjet, post script, Epson, IBM)

### Interface operating modes (S7-300, S7-400)

#### Possible interface operating modes

The following table is a summary of the interface operating modes from the various communication modules and protocols.

| Operating mode | Description |
| --- | --- |
| Half-duplex (RS485) two-wire mode. | Operating mode for point-to-point connection or multipoint connection (multipoint) in two-wire mode. The communication module can be the master as well as the slave.  During RS485-mode, the data transmission occurs through two lines (two-wire mode). The two lines are available alternatively for send and receive directions. They can either send or receive (half-duplex). After a send process, it is automatically switched to receive (maximum switch-over time of 1 ms). |
| Full-duplex (RS422), four-wire mode | During RS422-mode, the data transmission occurs through four lines (four-wire mode). There are always two lines available for send and receive directions. They can send and receive simultaneously (full-duplex).   The data is exchanged simultaneously between one or more communication partners, i.e., it can be sent and received at the same time. Each communication partner must be able to simultaneously operate a transmission and reception set-up. |
| Full-duplex (RS 422) four-wire mode (point-to-point connection) <sup>1)</sup> | The communication module can be used in the following topologies in RS422 mode:  - Link between two participants: Point-to-point connection - Connection between numerous stations: Multipoint connection   The communication module can be used as both master and slave. |
| Full-duplex (RS422) four-wire mode (multipoint master) <sup>1)</sup> | The communication module can be used in the following topologies in RS422 mode:  - Link between two participants: Point-to-point connection - Connection between numerous stations: Multipoint connection   The communication module can be used as a multipoint master as well as a multipoint slave.  In the case of a master/slave topology in the RS422 mode:  - The master's sender is interconnected with the receivers of all the slaves. - The slaves' senders are interconnected with the master's receiver. - Only the receiver of the master and the receiver of one slave have a default setting. All the other slaves function without default settings. |
| Full-duplex (RS422) four-wire mode (multipoint slave) <sup>1)</sup> | The communication module can be used in the following topologies in RS422 mode:  - Link between two participants: Point-to-point connection - Connection between numerous stations: Multipoint connection   The communication module can be used as a multipoint master as well as a multipoint slave.  In the case of a master/slave topology in the RS422 mode:  - The master's sender is interconnected with the receivers of all the slaves. - The slaves' senders are interconnected with the master's receiver. - Only the receiver of the master and the receiver of one slave have a default setting. All the other slaves function without default settings. |
| <sup>1)</sup> CP 440 only |  |

### Initial state of receive line (S7-300, S7-400)

#### X27 (RS422/485) interface

The table below contains descriptions of the parameters for the X27 (RS422/485) interface submodule. RS485-mode is not possible with the 3964(R) and RK512 procedures and the printer.

X27 (RS422/485) interface module

| Parameters | Description | Value range | Default value |
| --- | --- | --- | --- |
| Initial state of receive line | **none**: This setting only makes sense with bus-capable special drivers. | None | Signal R(A) 5V, signal R(B) 0V (break detection) <sup>(2)</sup> |
| **Signal R(A) 5V, signal R(B) 0V (break detection)**: Break detection is possible in "Full-duplex (RS 422) four-wire mode" with this setting. | Signal R(A) 5V, signal R(B) 0V (break detection) <sup>(1)</sup> |  |  |
| **Signal R(A) 0V, signal R(B) 5V**: This initial state corresponds to idle (no senders active) in "Half Duplex (RS 485) Two-Wire Mode". No break detection is possible with this setting. | Signal R(A) 0V, signal R(B) 5V |  |  |
| <sup>(1) </sup>Only with "Full-duplex (RS422) four-wire mode"   <sup>(2)</sup> Only with "Full-duplex (RS422) four-wire mode", with "Half-duplex (RS485) two-wire mode" the default setting is signal R (A) 0V, signal R (B) 5V |  |  |  |

#### Initial state of receive line

The figure illustrates the wiring of the receiver at the X27 (RS422/485) interface:

![Wiring of the receiver at the X27 (RS422/485) interface](images/26593766027_DV_resource.Stream@PNG-en-US.png)

Wiring of the receiver at the X27 (RS422/485) interface

### CP 440 in a multipoint topology with the RS422/485 protocols (S7-300, S7-400)

#### Application options

The CP 440 can be used in different topologies in the RS422 and RS485 operating modes.

Distinctions are drawn between connections with:

- Two nodes (**point-to-point**) and
- Several nodes (**multipoint**)

In these cases the CP 440 can be used as:

- **Master** or
- **Slave**.

#### RS422 or RS485 mode for point-to-point connections

![RS422 point-to-point](images/19318199819_DV_resource.Stream@PNG-de-DE.png)

RS422 point-to-point

![RS485 point-to-point](images/19323766411_DV_resource.Stream@PNG-de-DE.png)

RS485 point-to-point

In the case of a **master/slave topology**, there must be an appropriate message frame in the user program. Example: The master sends all the slaves a message frame with address information. All the slaves listen in and compare the address with their own. If the address is the same, the addressed slave sends its answer.

The senders of all slaves must be able to switch to low impedance.

#### RS422 mode in multipoint connections

In the case of a master/slave topology in RS422 mode:

- The master's sender is interconnected with the receivers of all the slaves.
- The slaves' senders are interconnected with the master's receiver.
- Only the receiver of the master and the receiver of one slave have a default setting. All the other slaves function without default settings.

![RS422 multipoint](images/19323777803_DV_resource.Stream@PNG-de-DE.png)

RS422 multipoint

#### RS485 mode in multipoint connections

In the case of a topology in RS485 operation:

- The cable pair is interconnected for the send/receive line of all the nodes.
- Only the receiver of a node has a default setting. All the other modules function without default settings.

![RS485 multipoint](images/19323789195_DV_resource.Stream@PNG-de-DE.png)

RS485 multipoint

The necessary settings are made for the different topologies in the "Interface" section of the properties dialog for the module.

> **Note**
>
> When you run the ASCII driver in RS422 multipoint or RS485 mode, you must take steps in the user program to ensure that only one node sends data at any one time. If two users send data simultaneously, the message frame is corrupted.

### Receive buffer  (S7-300, S7-400)

#### Receive buffer on the module

The following table describes the parameters for the module receive buffer.

Receive buffer from the module - procedure 3964(R) / RK512 / ASCII driver

| Parameters | Description | Value range | Default value |
| --- | --- | --- | --- |
| Clear module receive buffer on startup | The module receive buffer is not deleted at CPU start-up (STOP RUN transition). | No (fixed) | No |
| Use CPU receive mailbox (CP 441 only) | Here you can specify whether a receive mailbox is to be set up on the CPU.  You must set up a receive mailbox if you have not programmed a BRCV instruction for the module in the user program of the CPU.  If you have programmed a BRCV, you must deactivate this parameter, otherwise data will be stored in the receive mailbox defined here instead of being processed by the BRCV. | - Yes - No | No |
| DB number <sup>(1)</sup> | Number of the data block for the receive mailbox on the CPU. | 1 to 65535 (depending on the CPU) | 1 |
| <sup>(1) </sup>Only when "Use CPU Receive Mailbox" = "Yes"   <sup>(2) </sup>Only when "Buffered receive message frames" = "1" |  |  |  |

Receive buffer from the module - additional for ASCII drivers

| Parameters | Description | Value range | Default value |
| --- | --- | --- | --- |
| Buffered receive message frames | Here you can specify the number of receive message frames to be buffered in the receive buffer of the communication module.  If you specify "1" here and deactivate the following parameter "prevent overwrite" and cyclically read the received data from the user program, a current message frame will always be sent to the CPU. | 1 to 250 | 250 |
| Dynamic message frame  ET 200S 1SI | For the reception of messages, you can specify if a message should just be buffered or if the messages should be dynamically buffered.  By activating dynamic message frames, the module can buffer multiple messages with different lengths. The buffer is a ring buffer. If the buffer is full, the oldest message is overwritten, unless the "Prevent overwriting buffers" parameter is enabled. In this case, the newest message is discarded. In both cases, a diagnosis alarm will display saying that data was lost. | - Activated - Blocked | Activated |
| Prevent overwrite | You can deactivate this parameter if the parameter "buffered receive message frames" is set to "1". This authorizes the buffered receive message frame to be overwritten. | - Yes - no <sup>(2)</sup> | Yes |
| <sup>(1) </sup>Only when "Use CPU Receive Mailbox" = "Yes"   <sup>(2) </sup>Only when "Buffered receive message frames" = "1" |  |  |  |

## Modbus communication (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of modbus communication (S7-300, S7-400)](#overview-of-modbus-communication-s7-300-s7-400)
- [Modbus master (S7-300, S7-400)](#modbus-master-s7-300-s7-400)
- [Modbus slave (S7-300, S7-400)](#modbus-slave-s7-300-s7-400)
- [Function codes (S7-300, S7-400)](#function-codes-s7-300-s7-400)
- [Error message area (S7-300, S7-400)](#error-message-area-s7-300-s7-400)

### Overview of modbus communication (S7-300, S7-400)

#### Position in the system environment

The following Modbus description refers to the use of the reloadable driver on the CP 341 (S7 300) and CP 441‑2 (S7 400) communication processors, and the operation of the ET 200S 1SI module in the Modbus/USS model.

#### Function of the coupling

With the appropriately equipped communication modules and the related instructions, you can establish a communication connection between a remote Modbus control system (such as Modicon PLCs or Honeywell TDC3000) and a SIMATIC S7.

The GOULD-MODBUS protocol in the RTU format is used for transmission.

Function codes 01, 02, 03, 04, 05, 06, 08, 15 and 16 are used for communication between a communication module operated as a Modbus slave and a master system.

If a SIMATIC S7 communication module is operated as a Modbus master, function codes 07, 11 and 12 are additionally available.

#### Modbus protocol

The modbus protocol is a communication protocol based on a master/slave and client/server architecture.

The procedure used is a code-transparent, asynchronous half-duplex procedure. Data transmission is carried out without handshake.

#### SIMATIC S7 as a Modbus slave

The master has the initiative for transmission, the CP / S7 CPU works as a slave.

Frame traffic from slave to slave is not possible.

#### SIMATIC S7 as a Modbus master

As master, the communication module initiates transmission and, after outputting a request message frame, it waits for the configured response monitoring time for a response message frame from the slave.

#### Message frame structure

The data exchange "Master-Slave" and/or "Slave-Master" begins with the **slave address**, followed by the **function code**. Then the data are transferred. The structure of the data field depends on the function code used. The CRC check is transmitted at the end of the message frame.

| ADDRESS | FUNCTION | DATA | CRC-CHECK |
| --- | --- | --- | --- |
| Byte | Byte | n byte | 2 byte |

| Symbol | Meaning |
| --- | --- |
| ADDRESS | MODBUS slave address |
| FUNCTION | MODBUS function code |
| DATA | Message frame data: Byte_Count, Coil_Number, Data |
| CRC-CHECK | Message frame checksum |

#### Slave address

The slave address can be within the range of 1 to 255. The address is used to address a defined slave on the bus.

#### Broadcast Message

The master uses slave address 0 to address all slaves on the bus.

**Broadcast messages** are only permitted in conjunction with writing **Function codes 05, 06, 15 and 16**.

A broadcast message is not followed by a response message frame from the slave.

#### Function code

The function code defines the meaning of the message frame. It also defines the structure of a message frame. The following function codes are supported by the communication module:

| Function Code | Function in accordance with MODBUS specification |
| --- | --- |
| 01 | Read Coil Status |
| 02 | Read Input Status |
| 03 | Read Holding Registers |
| 04 | Read Input Registers |
| 05 | Force Single Coil |
| 06 | Preset Single Register |
| 07 | Read Exception Status (only master) |
| 08 | Loop Back Test |
| 11 | Fetch Communications Event Counter (only master) |
| 12 | Fetch Communications Event Log (only master) |
| 15 | Force Multiple Coils |
| 16 | Preset Multiple Registers |

#### Data Field DATA

The data field DATA is used to transfer the function code-specific data such as:

- Bytecount, Coil_Startaddress, Register_Startaddress; Number_of_Coils, Number_of_Registers, ... .

  See section "[Function codes](#function-codes-s7-300-s7-400)".

#### CRC-Check

The end of the message frame is identified by means of the CRC 16 checksum consisting of 2 bytes. It is calculated by the following polynominal: x<sup>16</sup> + x<sup>15</sup> + x<sup>2</sup> + 1.

The low byte is transferred first, followed by the high byte.

#### End of Message Frame

**The loadable driver recognizes the end of the message frame when no transmission takes place during the time period required for the transmission of three and a half characters (3.5 times character delay time**) (see MODBUS Protocol Reference Guide).

This message frame end TIME_OUT is thus dependent on the data transmission rate.

| Data transmission rate | TIME_OUT |
| --- | --- |
| 115200 bps | 0,3 ms |
| 76800 bps | 0,5 ms |
| 57600 bps | 0.7 ms |
| 38400 bps | 1 ms |
| 19200 bps | 2 ms |
| 9600 bps | 4 ms |
| 4800 bps | 8 ms |
| 2400 bps | 16 ms |
| 1200 bps | 32 ms |
| 600 bps | 64 ms |
| 300 bps | 128 ms |

During "Normal operation" the Modbus message frame received by the connection partner is evaluated and checked after the end of frame for TIME_OUTs is received.

During "Interference suppression" the end of frame is recognized by correctly formatted receive frame with a correct CRC code.

#### Exception responses

On recognition of an error in the request message frame from the master, for example, register address illegal, the slave sets the highest value bit in the function code of the response message frame.

This is followed by transmission of one byte of error code, exception code, which describes the reason for the error.

A detailed description of the meaning of the above-mentioned parameters can be found in the “GOULD MODICON Modbus Protocol.”

#### Exception code message frame

The error code response message frame from the slave has the following structure:

- for example, slave address 5, function code 5, exception code 2

**Response frame from the slave EXCEPTION_CODE_xx:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 85H | Function code |
| 02H | Exception code (1...7) |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

On receipt of an error code response message frame by the driver, the current job is completed with error.

An error number corresponding to the received error code (exception code 1-7) is also entered in the error message area.

There is no entry in the target data block.

The following error codes are defined in accordance with the MODBUS Specification:

| Error code | Meaning in accordance with MODBUS Specification | Cause - Short Description * |
| --- | --- | --- |
| 1 | Illegal function | Illegal function code |
| 2 | Illegal data address | Slave has illegal data address |
| 3 | Illegal data value | Slave has illegal data value |
| 4 | Failure in Associated Device | Slave has internal error |
| 5 | Acknowledge | Function is carried out |
| 6 | Busy, Rejected message | Slave is not ready to receive |
| 7 | Negative acknowledgement | The function cannot be carried out. |
| * Check slave for further details. |  |  |

#### RS232C accompanying signals

The following RS232C accompanying signals are available on the communication modules that use the RS232C interface module:

|  |  |  |  |
| --- | --- | --- | --- |
| DCD | (input) | Data carrier detect | Data carrier detected |
| DTR | (Output) | Data terminal ready | Communication module ready |
| DSR | (input) | Data set ready | Communication partner ready for operation |
| RTS | (Output) | Request to send | Communication module ready to send |
| CTS | (input) | Clear to send | Communication partner can receive data from the communication module (response to RTS = ON of the CP) |
| RI | (input) | Ring indicator | Ring indicator |

When the communication module is switched on, the output signals are in the OFF state (inactive).

You can configure the operation of the DTR/DSR and RTS/CTS control signals in the properties dialog of the module or via instructions in the user program.

#### Operating RS232C accompanying signals

The RS232C accompanying signals can be used as follows:

- When the automatic use of all RS232C accompanying signals is configured.
- Via the corresponding instructions. For more information, see the section "[Overview of the instructions](#overview-of-the-instructions-s7-300-s7-400)".

  > **Note**
  >
  > When automatic operation of the RS232C accompanying signals is configured, RTS and DTR cannot be controlled via the corresponding instruction (see section "[Overview of the instructions](#overview-of-the-instructions-s7-300-s7-400)")!
  >
  > On the other hand, it is always possible to read all RS232C accompanying signals using the corresponding instruction.

The following sections describe the basic procedures for control and evaluation of the RS232C accompanying signals.

#### Automatic use of accompanying signals

Automatic operation of the RS232C accompanying signals on the communication module is realized as follows:

- As soon as the communication module is switched by configuration to an operating mode with automatic operation of the RS232C accompanying signals, it sets the RTS line to OFF and the DTR line to ON (communication module ready for use).
- This prevents sending and receiving of message frames until the DTR line is set to ON. As long as DTR remains set to OFF, no data is received via the RS232C interface. If a send job is made, it is aborted with a corresponding error message.
- When a send job is made, RTS is set to ON and the parameterized data output waiting time starts. When the data output time elapses and CTS = ON, the data is sent via the RS232C interface.
- If the CTS line is not set to ON within the data output time so that data can be sent, or if CTS changes to OFF during transmission, the send job is aborted and an error message generated.
- Once the data has been sent and the configured clear RTS time has elapsed, the RTS line is set to OFF. The CP does not wait for CTS to change to OFF.
- Data can be received via the RS232C interface as soon as the DSR line is set to ON. If the receive buffer of the communication module threatens to overflow, there is no response from the communication module.
- If DSR changes from ON to OFF, an active send job as well as the receipt of data will be canceled with an error message. The message "DSR = OFF (automatic operation of V24 signals)" is entered in the diagnostics buffer of the communication module.

  > **Note**
  >
  > When automatic operation of the RS232C accompanying signals is configured, RTS and DTR cannot be controlled via the corresponding instruction! For more information, see the section "[Overview of the instructions](#overview-of-the-instructions-s7-300-s7-400)".

  > **Note**
  >
  > Set "Clear RTS time" in the properties dialog of the module so that the communication partner can receive the last characters of the message frame in their entirety before RTS, and thus the send job, is revoked. The "data output waiting time" must be set such that the communication partner can be ready to receive before the time elapses.

#### Time Diagram

The following figure illustrates the chronological sequence of a send job.

![Time diagram for automatic operation of the RS232C accompanying signals](images/42609978123_DV_resource.Stream@PNG-en-US.png)

Time diagram for automatic operation of the RS232C accompanying signals

### Modbus master (S7-300, S7-400)

This section contains information on the following topics:

- [CP 341 (S7-300, S7-400)](#cp-341-s7-300-s7-400)
- [CP 441-2 (S7-300, S7-400)](#cp-441-2-s7-300-s7-400)
- [ET 200S 1SI (S7-300, S7-400)](#et-200s-1si-s7-300-s7-400)

#### CP 341 (S7-300, S7-400)

This section contains information on the following topics:

- [Data transmission from CPU to communication module with P_SND_RK (CP 341) (S7-300, S7-400)](#data-transmission-from-cpu-to-communication-module-with-p_snd_rk-cp-341-s7-300-s7-400)
- [Data transmission from the communication module to the CPU with P_RCV_RK (CP 341) (S7-300, S7-400)](#data-transmission-from-the-communication-module-to-the-cpu-with-p_rcv_rk-cp-341-s7-300-s7-400)

##### Data transmission from CPU to communication module with P_SND_RK (CP 341) (S7-300, S7-400)

###### Activation

Execution of a MODBUS function code is activated by means of the instruction **P_SND_RK** with an **edge** at the **REQ** input.

Enter ‘S’ for SEND at the SF parameter.

The logical module address is entered at LADDR.

You must enter ‘X’ for expanded data block as the area type of the partner CPU. No values must be specified for the other parameters of the partner CPU (R_...).

This ensures transfer to the driver of the parameters required for the execution of the function code.

###### Data source

When P_SND_RK is activated, the **source data area** specified with the **DB_NO** and **DBB_NO** parameters is transferred to the communication module with the length **LEN**.

###### Length Indication

The length **LEN** depends on the function code used.

| Function code | Length LEN in bytes |
| --- | --- |
| 01 | 6 |
| 02 | 6 |
| 03 | 6 |
| 04 | 6 |
| 05 | 6 |
| 06 | 6 |
| 07 | 2 |
| 08 | 6 |
| 11 | 2 |
| 12 | 2 |
| 15 | >6 |
| 16 | >6 |

If the transferred data quantities differ from those listed above for the individual function codes, the job is not carried out and P_SND_RK rejects it with an edge at output ERROR.

###### SEND Source DB

The parameters required for the execution of a function code must be entered as user data in the source data area.

A detailed description of each P_SND_RK source DB is available in the description of the individual function codes in the section "[Function codes](#function-codes-s7-300-s7-400)".

###### Generation of Message Frames

The request message frames to the slave are generated in accordance with the transferred P_SND_RK source data and sent by the communication module.

First of all the driver checks if the length LEN specified at P_SND_RK corresponds to the length for this function code.

If not, the job is not carried out and it is completed with an edge at output ERROR of the P_SND_RK.

When using function codes other than those listed, the activated job is not carried out either and is completed with ERROR at P_SND_RK.

The “byte counter” and “CRC check” elements in the request message frame are generated by the communication module; an entry in the P_SND_RK source DB is not required.

###### Job Completion for Writing Functions

For writing function codes, the activated P_SND_RK is completed after a response message frame is received without error. This is communicated to the SIMATIC user program by means of an edge at output **DONE** of the P_SND_RK.

If **errors** are detected in the message frame traffic, or if the slave sends an **error code** response message frame, this is reported by an edge at output **ERROR**.

###### Job Completion for Reading Functions

For reading functions, the activated P_SND_RK is completed after the response message frame is received without error **and** complete transfer of the received data to the CPU.

This is communicated to the SIMATIC user program by means of an edge at output **DONE** of the P_SND_RK.

At this time the received data are already available in the CPU.

If **errors** are detected in the message frame traffic, or if the slave sends an **error code** response message frame, this is reported by an edge at output **ERROR**.

In this case no receive data are transferred to the CPU.

###### STATUS Entry on Job Completion

For those instances when a job is completed with **ERROR** at P_SND_RK, an additional error code is entered in the **STATUS** parameter.

The exact cause for the error can be determined with this error code

##### Data transmission from the communication module to the CPU with P_RCV_RK (CP 341) (S7-300, S7-400)

###### Prerequisite

All  **reading**  function codes require a P_RCV_RK.

###### Data destination

When the instruction P_RCV_RK is ready to receive, it accepts the received data from the communication module and enters it into the data destination specified in the parameters **DB_N0** and **DBB_N0**.

###### How Receipt of Data is Displayed

The user is informed of the receipt of data in the CPU by means of an edge at output **NDR**.

At this point the length of the received data block is displayed in the parameter **LEN**.

Completion of the entire modbus job can be recognized at output DONE of the instruction P_SND_RK.

###### How to Handle an Error

In the event of receive or transfer errors, no data is transferred to the CPU. In this case, the instruction P_SND_RK is completed with an edge at the output ERROR.

###### P_RCV_RK Destination DB

The user data received with a reading function code are entered into the P_RCV_RK destination area.

A detailed description of each P_RCV_RK destination DB can be found in section " [Function codes](#function-codes-s7-300-s7-400)".

The length of data entered is displayed an the parameter LEN of P_RCV_RK.

#### CP 441-2 (S7-300, S7-400)

This section contains information on the following topics:

- [Data transmission from CPU to communication module with BSEND (CP 441-2) (S7-300, S7-400)](#data-transmission-from-cpu-to-communication-module-with-bsend-cp-441-2-s7-300-s7-400)
- [Data transmission from the communication module to the CPU with BRCV (CP 441-2) (S7-300, S7-400)](#data-transmission-from-the-communication-module-to-the-cpu-with-brcv-cp-441-2-s7-300-s7-400)

##### Data transmission from CPU to communication module with BSEND (CP 441-2) (S7-300, S7-400)

###### Communication connection

The **Parameter ID** describes the unique communication connection to a communication partner. You must specify the local ID from the data link configuration here

###### Block Relationship

The **Parameter R_ID** describes the unique block relationship within a communication connection.

With this driver, **any** values from **0..255** may be entered for R_ID on BSEND.

In the event of reading jobs, parameter assignment of the associated BRCV must have the same R_ID as BSEND.

###### Activation

Execution of a MODBUS function code is activated by means of the instruction **BSEND** with an **edge** at the **REQ** input.

This ensures transfer to the driver of the parameters required for the execution of the function code.

###### Data source

When BSEND is activated, the **source data area** specified with parameter **SD_1** is transferred to the communication module with the length **LEN**.

###### Length Indication

The length **LEN** depends on the function code used.

| Function code | Length LEN in bytes |
| --- | --- |
| 01 | 6 |
| 02 | 6 |
| 03 | 6 |
| 04 | 6 |
| 05 | 6 |
| 06 | 6 |
| 07 | 2 |
| 08 | 6 |
| 11 | 2 |
| 12 | 2 |
| 15 | >6 |
| 16 | >6 |

If the transferred data quantities differ from the ones listed above for the individual function codes, the job is not carried out and BSEND rejects it with an edge at output ERROR.

###### BSEND Source DB

The parameters required for the execution of a function code must be entered as user data in the source data area.

A detailed description of each BSEND source DB is available in the description of the individual function codes in section "[Function codes](#function-codes-s7-300-s7-400)".

###### Generation of Message Frames

The request message frames to the slave are generated in accordance with the transferred BSEND source data and sent by the communication module.

First of all the driver checks if the length LEN specified at BSEND corresponds to the length for this function code.

If not, the job is not carried out and it is completed with an edge at output ERROR of BSEND.

When using function codes other than those listed, the activated job is not carried out either and is completed with ERROR at BSEND.

The “byte counter” and “CRC check” elements in the request message frame are generated by the communication module; an entry in the BSEND source DB is not required.

###### Job Completion for Writing Functions

For writing function codes, the activated BSEND is completed after a response message frame is received without error.

This is communicated to the SIMATIC user program by means of an edge at output **DONE** of the BSEND.

If **errors** are detected in the message frame traffic, or if the slave sends an **error code** response message frame, this is reported by an edge at output **ERROR**.

###### Job Completion for Reading Functions

For reading functions, the activated BSEND is completed after the response message frame is received without error **and** complete transfer of the received data to the CPU.

This is communicated to the SIMATIC user program by means of an edge at output **DONE** of the BSEND.

At this time the received data are already available in the CPU.

If **errors** are recognized in the data frame traffic, or if the slave sends an **error code** response message frame, this is reported by an edge at output **ERROR**.

In this case no receive data are transferred to the CPU.

###### Entry in the error message area at job completion

For those instances when a job is completed with **ERROR** at BSEND, an additional error code is entered in the error message area.

The exact cause for the error can be determined with this error code.

##### Data transmission from the communication module to the CPU with BRCV (CP 441-2) (S7-300, S7-400)

###### Communication connection

The **Parameter ID** describes the unique communication connection to a communication partner. You must specify the local ID from the data link configuration here.

###### Block Relationship

The **Parameter R_ID** describes the unique block relationship within a communication connection.

All **reading** function codes require a BRCV.   
Parameter assignment of **R_ID** on **BRCV** must be the **same R_ID** as for the corresponding BSEND, which was used to activate this job (any values 0 to 255).

In this way you can program several BSEND / BRCV pairs in the SIMATIC user program.

The response message frames received from the Modbus slave are then stored in different destination areas, depending on the R_ID used for this job.

###### Data destination

When the BRCV instruction is ready to receive, it accepts the received data from the communication module and enters them in the data destination specified in the parameter **RD_1**. This means that the data destination is variable.

###### How Receipt of Data is Displayed

The user is informed of the receipt of data in the CPU by means of an edge at output **NDR**.

At this point the length of the received data block is displayed in the parameter **LEN**.

You can recognized that the entire Modbus job is completed at the DONE output of the BSEND instruction.

###### How to Handle an Error

In the event of receive or transfer errors, no data is transferred to the CPU. In this instance BSEND is completed with an edge at the output ERROR.

###### BRCV Destination DB

The user data received with a reading function code are entered into the BRCV destination area.

The detailed structure of the respective BRCV destination DB is provided in the description of the individual function codes in section "[Function codes](#function-codes-s7-300-s7-400)".

The length of data entered is displayed at the parameter LEN of BRCV.

#### ET 200S 1SI (S7-300, S7-400)

This section contains information on the following topics:

- [Data transmission with the ET 200S 1SI Modbus master (S7-300, S7-400)](#data-transmission-with-the-et-200s-1si-modbus-master-s7-300-s7-400)

##### Data transmission with the ET 200S 1SI Modbus master (S7-300, S7-400)

###### Introduction

Data transmission between the module and CPU using the S_SEND and S_RCV instructions.

###### S_SEND instruction: Send data to a communication partner

The S_SEND and S_RCV instructions must be activated in order to execute a Modbus master job. The S_SEND instruction is activated by an edge at the REQ input when data is to be output to the module. The S_RCV instruction is made ready to receive data from the module with EN_R=1. An S_RCV is required for all reading function codes. The figure below shows the overall behavior of the S_SEND and S_RCV parameters when a Modbus job is executed.

![Time Sequence Chart for Modbus Request](images/26566398603_DV_resource.Stream@PNG-en-US.png)

Time Sequence Chart for Modbus Request

Data transmission is initiated by a positive edge at the REQ input. Data transmission can take several calls (program cycles), depending on the data volume.

The S_SEND instruction can be called cyclically by setting the signal state at parameter input R to "1". This cancels transmission to the module and resets the S_SEND instruction to its initial state. Data that has already been received by the module is still sent to the communication partner. If the signal state remains static at "1" at the input R, sending is disabled.

The address of the ET 200S Modbus/USS serial interface module to be addressed is specified at the LADDR parameter.

The DONE output indicates "Job completed without errors". ERROR indicates error events. If an error has occurred, the corresponding event number is displayed in STATUS. If no error occurs, STATUS has the value 0. DONE and ERROR/STATUS are also output at RESET of S_SEND. The binary result is reset if an error has occurred. If the block is completed without errors, the binary result has the status "1".

###### Modbus master read job

As the interface between the user program and the interface module operates in half-duplex mode you must observe the following items:

After positive acknowledgment of the Modbus master read job, you first have to fetch the receive data from the interface module by calling the S_RCV instruction before starting a new Modbus master send job.

### Modbus slave (S7-300, S7-400)

This section contains information on the following topics:

- [Initialization of the communication module (S7-300, S7-400)](#initialization-of-the-communication-module-s7-300-s7-400)

#### Initialization of the communication module (S7-300, S7-400)

##### Introduction

The Modbus communication instructions ,(MODB_341, MODB_441 and S_MODB) for the loadable Modbus slave driver must be called in the cyclic part of the SIMATIC S7 CPU.

The Modbus communication instruction initializes the CP and executes the Modbus functions that the driver cannot perform independently. The Modbus communication instruction must then also be called in the user program if these function codes are not used by the Modbus master system.

Communication between the CP and the instruction is performed through the CPU operating system functions and instructions BSEND (CP 441-2) or P_SND_RK and P_RCV_RK (CP 341), which are called by the instruction.

##### Startup, initialization

The Modbus communication instruction must be initialized after a warm restart or hot restart of the CPU.

Initialization is triggered by a rising edge at the CP_START input.

The instruction first deletes the instance DB, then it reads the address areas I, O, M, T, C from the CPU and saves them in the instance DB. This allows the write requests from the Modbus master system to be tested to determine if they exceed the range.

With a send request, the CP is informed of the number of the instance DB and the previously successful initialization.

If the initialization ends with errors, no Modbus communication is possible. All requests from the Modbus master system are answered with an exception code message frame.

##### Instance DB

All data relating to the Modbus communication instruction are in an instance data block. This data block is both an instance DB (multi-instances) for the various instructions used, and a work area for the Modbus communication instruction. An additional data area is not required.

The Modbus communication instruction only works with the instance DB and with local data.

The instance DB is read-only.

##### Monitoring time

After power on, the CP needs several seconds for the hardware and memory test until it is ready. Initialization attempts made by the Modbus communication instruction during this time end with an error. Therefore, the initialization job is repeated several times during the monitoring period.

##### Read time interval SYSTAT (CP 441-2 only)

Since a regular SYSTAT read each cycle or every second cycle put an unnecessarily load on the CP and K bus and thereby reduce the data throughput, a time interval can be set for reading the SYSTAT (only relevant for CP 441-2 (MODB_441)).

### Function codes (S7-300, S7-400)

This section contains information on the following topics:

- [Modbus master (RTU) (S7-300, S7-400)](#modbus-master-rtu-s7-300-s7-400)
- [Modbus slave (RTU) (S7-300, S7-400)](#modbus-slave-rtu-s7-300-s7-400)

#### Modbus master (RTU) (S7-300, S7-400)

This section contains information on the following topics:

- [Function Code 01 – Read Output Status (S7-300, S7-400)](#function-code-01-read-output-status-s7-300-s7-400)
- [Function code 02 - Read Input Status (S7-300, S7-400)](#function-code-02---read-input-status-s7-300-s7-400)
- [Function Code 03 - Read Output Registers (S7-300, S7-400)](#function-code-03---read-output-registers-s7-300-s7-400)
- [Function code 04 - Read Input Registers (S7-300, S7-400)](#function-code-04---read-input-registers-s7-300-s7-400)
- [Function Code 05 - Force Single Coil (S7-300, S7-400)](#function-code-05---force-single-coil-s7-300-s7-400)
- [Function code 06 - Preset Single Register (S7-300, S7-400)](#function-code-06---preset-single-register-s7-300-s7-400)
- [Function Code 07 - Read Exception Status (S7-300, S7-400)](#function-code-07---read-exception-status-s7-300-s7-400)
- [Function code 08 - Loop back Diagnostic Test (S7-300, S7-400)](#function-code-08---loop-back-diagnostic-test-s7-300-s7-400)
- [Function code 11 - Fetch Communications Event Counter (S7-300, S7-400)](#function-code-11---fetch-communications-event-counter-s7-300-s7-400)
- [Function Code 12 - Fetch Communications Event Log (S7-300, S7-400)](#function-code-12---fetch-communications-event-log-s7-300-s7-400)
- [Function code 15 - Force Multiple Coils (S7-300, S7-400)](#function-code-15---force-multiple-coils-s7-300-s7-400)
- [Function code 16 - Preset Multiple Registers (S7-300, S7-400)](#function-code-16---preset-multiple-registers-s7-300-s7-400)

##### Function Code 01 – Read Output Status (S7-300, S7-400)

###### Function

This function enables individual bits to be read from the slave.

###### Start address

The **Bit start address** parameter is not checked by the driver and is sent unchanged.

###### Bit number

For **Bit number**, number of coils, any value between **1** and **2040** is permitted (for ET 200S 1SI Modbus up to 2008).

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#1 | Function code |
| +2.0 | bit_startadr | WORD | W#16#0040 | Bit start address |
| +4.0 | bit_number | INT | 16 | Bit number |

###### Example

**Request message frame FUNCTION 01:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 01H | Function code |
| 00H | Bit start address "High" |
| 40H | Bit start address "Low" |
| 00H | Bit number "High" |
| 10H | Bit number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 01:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 01H | Function code |
| 02H | Byte counter |
| 01H | <Data> |
| 17H | <Data> |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name | Type | Current value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD | W#16#1701 | Data |

The driver enters the data of the response message frame into the destination DB **word by word**.

The 1st received byte is entered as the Low Byte of the 1st word “data[1],” the 3rd received byte as the Low Byte of the 2nd word “data[2],” etc.

If fewer than 9 bits or if only one Low Byte was read, the value **00H** is entered into the remaining High Byte of the last word.

##### Function code 02 - Read Input Status (S7-300, S7-400)

###### Function

This function enables individual bits to be read from the slave.

###### Start address

The **Bit start address** parameter is not checked by the driver and is sent unchanged.

###### Bit number

For **Bit number**, number of coils, any value between **1** and **2040** is permitted (for ET 200S 1SI Modbus up to 2008).

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#2 | Function code |
| +2.0 | bit_startadr | WORD | W#16#0120 | Bit start address |
| +4.0 | bit_number | INT | 24 | Bit number |

###### Example

**Request message frame FUNCTION 02:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 02H | Function code |
| 01H | Bit start address "High" |
| 20H | Bit start address "Low" |
| 00H | Bit number "High" |
| 18H | Bit number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 02:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 02H | Function code |
| 03H | Byte counter |
| 04H | <Data> |
| 26H | <Data> |
| 48H | <Data> |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name | Type | Current value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD | W#16#2604 | Data |
| +2.0 | data[2] | WORD | W#16#0048 | Data |

The driver enters the data of the response message frame into the destination DB **word by word**.

The 1st received byte is entered as the Low Byte of the 1st word “data[1],” the 3rd received byte as the Low Byte of the 2nd word “data[2],” etc.

If fewer than 9 bits or if only one Low Byte was read, the value **00H** is entered into the remaining High Byte of the last word.

##### Function Code 03 - Read Output Registers (S7-300, S7-400)

###### Function

This function enables you to read individual registers from the slave.

###### Start address

The **Register start address** parameter is not checked by the driver and is sent unchanged.

###### Register number

**1** Up to a **maximum of 127 registers** (for ET 200S 1SI Modbus max. 125 registers) can be read (1 register = two bytes).

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#3 | Function code |
| +2.0 | reg_startadr | WORD | W#16#0040 | Register start address |
| +4.0 | reg_number | INT | 2 | Register number |

###### Example

**Request message frame FUNCTION 03:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 03H | Function code |
| 00H | Register start address "High" |
| 40H | Register start address "Low" |
| 00H | Register number "High" |
| 02H | Register number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 03:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 03H | Function code |
| 04H | Byte counter |
| 21H | Register address 40H data "High" |
| 23H | Register address 40H data "Low" |
| 25H | Register address 41H data "High" |
| 27H | Register address 41H data "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name | Type | Current value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD | W#16#2123 | Data |
| +2.0 | data[2] | WORD | W#16#2527 | Data |

##### Function code 04 -  Read Input Registers (S7-300, S7-400)

###### Function

This function enables you to read individual registers from the slave.

###### Start address

The **Register start address** parameter is not checked by the driver and is sent unchanged.

###### Register number

**1** Up to a **maximum of 127 registers** (for ET 200S 1SI Modbus max. 125 registers) can be read (1 register = two bytes).

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#4 | Function code |
| +2.0 | reg_startadr | WORD | W#16#0050 | Register start address |
| +4.0 | reg_number | INT | 3 | Register number |

###### Example

**Request message frame FUNCTION 04:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 04H | Function code |
| 00H | Register start address "High" |
| 50H | Register start address "Low" |
| 00H | Register number "High" |
| 03H | Register number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 04:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 04H | Function code |
| 04H | Byte counter |
| 31H | Register address 50H data "High" |
| 32H | Register address 50H data "Low" |
| 33H | Register address 51H data "High" |
| 34H | Register address 51H data "Low" |
| 35H | Register address 52H data "High" |
| 36H | Register address 52H data "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name |  | Type | Current value | Comment |  |
| --- | --- | --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD |  | W#16#3132 |  | Data |
| +2.0 | data[2] | WORD |  | W#16#3334 |  | Data |
| +4.0 | data[3] | WORD |  | W#16#3536 |  | Data |

##### Function Code 05 - Force Single Coil (S7-300, S7-400)

###### Function

This function serves to set or delete individual bits in the slave.

###### Bit address

The **bit address** parameter is not checked by the driver and is sent unchanged.

###### Bit Status

The following two values are permitted as the **bit status**:

- FF00H = Set bit
- 0000H = Delete bit

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#5 | Function code |
| +2.0 | bit_address | WORD | W#16#0019 | Bit address |
| +4.0 | bit_state | WORD | W#16#FF00 | Bit Status |

###### Example

**Request message frame FUNCTION 05:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 05H | Function code |
| 00H | Bit address "High" |
| 19H | Bit address "Low" |
| FFH | Set bit |
| 00H |  |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 05:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 05H | Function code |
| 00H | Bit address "High" |
| 19H | Bit address "Low" |
| FFH | Bit status "High" |
| 00H | Bit status "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

The response message frame is not entered in the receive DB.

##### Function code 06 - Preset Single Register (S7-300, S7-400)

###### Function

This command enables a slave register to be overwritten with a new value.

###### Register address

The **Register address** parameter is not checked by the driver and is sent unchanged.

###### Register value

Any value can be used as the **Register value**.

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#6 | Function code |
| +2.0 | reg_address | WORD | W#16#0180 | Register address |
| +4.0 | reg_value | WORD | W#16#3E7F | Register value |

###### Example

**Request message frame FUNCTION 06:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 06H | Function code |
| 01H | Register address "High" |
| 80H | Register address "Low" |
| 3EH | Register value "High" |
| 7FH | Register value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 06:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 06H | Function code |
| 01H | Register address "High" |
| 80H | Register address "Low" |
| 3EH | Register value "High" |
| 7FH | Register value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

The response message frame is not entered in the receive DB.

##### Function Code 07 - Read Exception Status (S7-300, S7-400)

###### Function

This function code enables 8 event bits to be read from the connected slave.

The start bit number of the event bit is determined by the connected device and therefore does not have to be specified by the SIMATIC user program

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#7 | Function code |

###### Example

**Request message frame FUNCTION 07:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 07H | Function code |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 07:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 07H | Function code |
| 3EH | <Data> |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name | Type | Current value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD | W#16#3Exx | Data |

The driver enters the individual bytes of the response message frame in the **High Byte** in the destination DB data[1].

The low byte of data[1] remains unchanged.

A value of 1 is displayed as the length in the LEN parameter of the receive instruction.

##### Function code 08 - Loop back Diagnostic Test (S7-300, S7-400)

###### Function

This function is used to check the communications connection.

Only **Diagnostic code 0000** is supported with this function code!

###### Diagnostic Code

The only permissible value for the parameter **Diagnostic code** is 0000.

###### Test Value

Any value can be used as the **Test Value**.

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#8 | Function code |
| +2.0 | diag_code | WORD | W#16#0000 | Diagnostic Code |
| +4.0 | test_value | WORD | W#16#A5C3 | Test Value |

###### Example

**Request message frame FUNCTION 08:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 08H | Function code |
| 00H | Diagnostic code "High" |
| 00H | Diagnostic code "Low" |
| A5H | Test value "High" |
| C3H | Test value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 08:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 08H | Function code |
| 00H | Diagnostic code "High" |
| 00H | Diagnostic code "Low" |
| A5H | Test value "High" |
| C3H | Test value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

The slave must return the request message frame received from the master unchanged as an echo.

The response message frame is not entered into an RCV DB.

##### Function code 11 - Fetch Communications Event Counter (S7-300, S7-400)

###### Function

This function code is used to read a **"Status Word"** (2 bytes long) and an **"Event Counter"** (2 bytes long) from the slave.

The meaning of the above parameters is described in detail in the "GOULD MODICON Modbus Protocol".

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#0B | Function code |

###### Example

**Request frame FUNCTION 11:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 0BH | Function code |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 11:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 0BH | Function code |
| FEH | Status Word "High" |
| DCH | Status Word "Low" |
| 01H | Event Counter "High" |
| 08H | Event Counter "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name | Type | Current value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD | W#16#FEDC | Status Word |
| +2.0 | data[2] | WORD | W#16#0108 | Event Counter |

> **Note**
>
> **Use with the ET 200S 1SI distributed I/O**
>
> Please note that when using with the ET 200S 1SI distributed I/O, the entire response frame of the slave, i.e. with Modbus address and function code (additional 2 bytes), is stored in the RCV destination DB. This causes the displacement of the offset for the status word (Offset 2.0) and for the event counter (Offset 4.0).

##### Function Code 12 - Fetch Communications Event Log (S7-300, S7-400)

###### Function

This function code enables the following to be read from the slave.

- 2 Byte **"Status Word"**
- 2 Byte **"Event Counter",**
- 2 Byte **"Message Counter"** and
- 64 Byte **"Event Bytes"**

The meaning of the above parameters is described in detail in the “GOULD MODICON Modbus Protocol.”

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#0C | Function code |

###### Example

**Request message frame FUNCTION 12:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 0CH | Function code |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 12:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 0CH | Function code |
| 46H | Byte counter |
| 87H | Status Word "High" |
| 65H | Status Word "Low" |
| 01H | Event Counter "High" |
| 08H | Event Counter "Low" |
| 02H | Message Counter "High" |
| 20H | Message Counter "Low" |
| 01H | Event Byte 1 |
| 12H | Event Byte 2 |
| : | : |
| C2H | Event Byte 63 |
| D3H | Event Byte 64 |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### RCV destination DB

Content of the RCV destination area:

| Address | Name | Type | Current value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | data[1] | WORD | W#16#8765 | Status Word |
| +2.0 | data[2] | WORD | W#16#0108 | Event Counter |
| +4.0 | data[3] | WORD | W#16#0220 | Message Counter |
| +6.0 | bytedata[1] | BYTE | B#16#01 | Event Byte 1 |
| +7.0 | bytedata[2] | BYTE | B#16#12 | Event Byte 2 |
| : | : |  |  | : |
| +68.0 | bytedata[63] | BYTE | B#16#C2 | Event Byte 63 |
| +69.0 | bytedata[64] | BYTE | B#16#D3 | Event Byte 64 |

##### Function code 15 - Force Multiple Coils (S7-300, S7-400)

###### Function

With this function code, up to 2040 bits (for ET 200S 1SI Modbus max. 1744 bits) can be changed in the slave

###### Start address

The **Bit start address** parameter is not checked by the driver and is sent unchanged.

###### Bit number

For **Bit number**, number of coils, any value between **1** and **2040** is permitted (for ET 200S 1SI Modbus up to 1744).

This specifies how many bits in the slave are to be overwritten.

The "Byte counter" parameter in the request message frame is generated by the driver on the basis of the transferred parameter "Bit number".

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#0F | Function code |
| +2.0 | bit_startadr | WORD | W#16#0058 | Bit start address |
| +4.0 | bit_number | INT | 10 | Bit number |
| +6.0 | coil_state[1] | WORD | W#16#EFCD | Status  Coil 5FH..58H/57H..50H |

###### Example

**Request message frame FUNCTION 15:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 0FH | Function code |
| 00H | Bit address "High" |
| 50H | Bit address "Low" |
| 00H | Bit number "High" |
| 0AH | Bit number "Low" |
| 02H | Byte counter |
| CDH | Status Coil 50H..57H |
| EFH | Status Coil 58H..59H |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 15:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 0FH | Function code |
| 00H | Bit address "High" |
| 50H | Bit address "Low" |
| 00H | Bit number "High" |
| 0AH | Bit number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

The response message frame is not entered in the receive DB.

##### Function code 16 - Preset Multiple Registers (S7-300, S7-400)

###### Function

Function code 16 enables you to overwrite up to **127 registers** in the slave (for ET 200S Modbus 1SI max. 109 registers) with a request message frame.

###### Start address

The **Register start address** parameter is not checked by the driver and is sent unchanged.

###### Register number

**1** Up to a **maximum of 127 registers** (for ET 200S 1SI Modbus max. 109 registers) can be read (1 register = two bytes).

The "Byte counter" parameter in the request message frame is generated by the driver on the basis of the transferred parameter "number of registers".

###### SEND source DB

Structure of SEND source area:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +0.0 | address | BYTE | B#16#5 | Slave address |
| +1.0 | Function | BYTE | B#16#10 | Function code |
| +2.0 | reg_startadr | WORD | W#16#0060 | Register start address |
| +4.0 | reg_number | INT | 3 | Register number |
| +6.0 | reg_data[1] | WORD | W#16#41A1 | Register data |
| +8.0 | reg_data[2] | WORD | W#16#42A2 | Register data |
| +10.0 | reg_data[3] | WORD | W#16#43A3 | Register data |

###### Example

**Request message frame FUNCTION 16:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 10H | Function code |
| 00H | Register address "High" |
| 60H | Register address "Low" |
| 00H | Register number "High" |
| 03H | Register number "Low" |
| 06H | Byte counter |
| 41H | <reg_data[1]> "High" |
| A1H | <reg_data[1]> "Low" |
| 42H | <reg_data[2]> "High" |
| A2H | <reg_data[2]> "Low" |
| 43H | <reg_data[3]> "High" |
| A3H | <reg_data[3]> "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame from slave FUNCTION 16:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address |
| 10H | Function code |
| 00H | Register address "High" |
| 60H | Register address "Low" |
| 00H | Register number "High" |
| 03H | Register number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

The response message frame is not entered in the receive DB.

#### Modbus slave (RTU) (S7-300, S7-400)

This section contains information on the following topics:

- [Function Code 01 – Read Coil (Output) Status (S7-300, S7-400)](#function-code-01-read-coil-output-status-s7-300-s7-400)
- [Function code 02 - Read Input Status (S7-300, S7-400)](#function-code-02---read-input-status-s7-300-s7-400-1)
- [Function Code 03 - Read Output Registers (S7-300, S7-400)](#function-code-03---read-output-registers-s7-300-s7-400-1)
- [Function code 04 - Read Input Registers (S7-300, S7-400)](#function-code-04---read-input-registers-s7-300-s7-400-1)
- [Function Code 05 - Force Single Coil (S7-300, S7-400)](#function-code-05---force-single-coil-s7-300-s7-400-1)
- [Function code 06 - Preset Single Register (S7-300, S7-400)](#function-code-06---preset-single-register-s7-300-s7-400-1)
- [Function code 08 - Loop back Diagnostic Test (S7-300, S7-400)](#function-code-08---loop-back-diagnostic-test-s7-300-s7-400-1)
- [Function code 15 - Force Multiple Coils (S7-300, S7-400)](#function-code-15---force-multiple-coils-s7-300-s7-400-1)
- [Function code 16 - Preset Multiple Registers (S7-300, S7-400)](#function-code-16---preset-multiple-registers-s7-300-s7-400-1)

##### Function Code 01 – Read Coil (Output) Status (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to read individual bits from the SIMATIC memory areas listed below.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_address | bit_number | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | Byte_count n | n byte DATA | CRC |

###### start_address

The MODBUS bit address "**start_address**" is interpreted by the driver as follows:

The driver checks that “start_address” is located within one of the areas which were specified during parameter assignment in the dialog box "**Conversion of MODBUS addressing for FC 01, 05, 15**" (from/to: memory bits, outputs, timers, counters).

|  |  |  |
| --- | --- | --- |
| If the MODBUS bit address **start_address** is located in one of these areas, | access is made to this **SIMATIC memory area** |  |
| from aaaaa to bbbbb | commence at memory bit | M uuuuu.0 |
| from ccccc to ddddd | commence at output | Q ooooo.0 |
| From eeeee to fffff | commence at timer | T ttttt |
| From ggggg to hhhhh | commence at counter | C zzzzz |

The address calculation for access, address conversion, is carried out as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Access beginning with SIMATIC |  | Conversion formula |  |  |  |
| Memory byte | = | ((start_address | – aaaaa) | / 8) | + uuuuu |
| Output byte | = | ((start_address | – ccccc) | / 8) | + ooooo |
| Timer | = | ((start_address | – eeeee) | / 16) | + ttttt |
| Counters | = | ((start_address | – ggggg) | / 16) | + zzzzz |

**Access to “memory bits” and “outputs”**

When accessing SIMATIC areas “Memory bits” and “Outputs,” the remaining Rest Bit_Number is calculated and used to address the relevant bit within the first / last memory or output byte.

**Access to "timers" and "counters"**

With the address calculation, it must be possible to divide the result by 16 without having a left over value:

- (start_address - eeeee)
- (start_address - ggggg)

Only access word-by-word starting from word limit is possible.

###### bit_number

For **bit_number**, number of coils, values between **1** and **2040** (with ET 200S 1SI Modbus max. 1768 bits) are allowed. This number of bits is read.

**Access to "timers" and "counters"**

When accessing SIMATIC areas “Timers” and “Counters,” it must be possible to divide the "bit_number" by 16 (access word-by-word only).

Please note that a maximum of 16 “timers” and/or “counters” can be read if you are using the CP 341.

> **Note**
>
> Note the CPU-specific restrictions.

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function codes FC 01, 05 and 15

| MODBUS address in transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| From 0 to 2047 | commence at memory bit | M 1000.0 |
| From 2048 to 2559 | commence at output | Q 256.0 |
| From 4096 to 4607 | commence at timer | T 100 |
| From 4608 to 5119 | commence at counter | C 200 |

**Request message frame FUNCTION 01:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 01H | Function code FUNC |
| 00H | start_address "High" |
| 40H | start_address "Low" |
| 00H | bit_number "High" |
| 20H | bit_number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Response message frame FUNCTION 01:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 01H | Function code FUNC |
| 04H | Byte_count |
| 01H | <DATA 1> M 1008.0 - M 1008.7 |
| 17H | <DATA 2> M 1009.0 - M 1009.7 |
| 02H | <DATA 3> M 1010.0 - M 1010.7 |
| 18H | <DATA 4> M 1011.0 - M 1011.7 |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

**Address calculation:**

The MODBUS address “start_address” 0040 Hex (64 decimal) is located in the “memory bit” area:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Memory byte | = | ((start_address | - aaaaa) | / 8) | + uuuuu |
|  | = | ((64 | - 0) | / 8) | + 1000 |
|  | = | 1008 ; |  |  |  |

The remaining rest bit_number has the following result:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rest bit_no. | = | ((start_address | - aaaaa) | % 8) | [Modulo 8] |
|  | = | ((64 | - 0) | % 8) |  |
|  | = | 0 ; |  |  |  |

Access is made starting from bit M 1008.0 up to and including M 1011.7.

**Bit number:**

The number of MODBUS bits "bit_number" 0020 Hex (32 decimal) means that 32 bits = 4 bytes are to be read.

###### Further examples

Some other access examples are listed in the table below.

All examples are based on the above area specification.

| start_address |  | Access in SIMATIC beginning |  |  |  |  | -> | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hex | Decimal | (Decimal) |  |  |  |  |  |  |
| 0000 | 0 | Bit memory | ((0 | - 0) | / 8) | + 1000 | -> | M 1000.0 |
| 0021 | 33 | Bit memory | ((33 | - 0) | / 8) | + 1000 | -> | M 1004.1 |
| 0400 | 1024 | Bit memory | ((1024 | - 0) | / 8) | + 1000 | -> | M 1128.0 |
| 0606 | 1542 | Bit memory | ((1542 | - 0) | / 8) | + 1000 | -> | M 1192.6 |
| 0840 | 2112 | Output | ((2112 | - 2048) | / 8) | + 256 | -> | Q 264.0 |
| 09E4 | 2532 | Output | ((2532 | - 2048) | / 8) | + 256 | -> | Q 316.4 |
| 1010 | 4112 | Timers | ((4112 | - 4096) | / 16) | + 100 | -> | T 101 |
| 10C0 | 4288 | Timers | ((4288 | - 4096) | / 16) | + 100 | -> | T 112 |
| 1200 | 4608 | Counters | ((4608 | - 4608) | / 16) | + 200 | -> | C 200 |
| 13E0 | 5088 | Counters | ((5088 | - 4608) | / 16) | + 200 | -> | C 230 |

##### Function code 02 - Read Input Status (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to read individual bits from the SIMATIC memory areas listed below.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_address | bit_number | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | Byte_count n | n byte DATA | CRC |

###### start_address

The MODBUS bit address "**start_address**" is interpreted by the driver as follows:

The driver checks that "start_address" is located within one of the areas which were entered during parameter assignment in the dialog box "**Conversion of MODBUS addressing for FC 02**" (from/to: memory bits, inputs).

|  |  |  |
| --- | --- | --- |
| If the MODBUS bit address is located in area **start_address** , | **SIMATIC memory area** is accessed |  |
| from kkkkk to lllll | commence at memory bit | M vvvvv.0 |
| from nnnnn to rrrrr | from input | I sssss.0 |

The address calculation for access, address conversion, is carried out as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Access beginning with SIMATIC |  | Conversion formula |  |  |  |
| Memory byte | = | ((start_address | – kkkkk) | / 8) | + vvvvv |
| Input byte | = | ((start_address | – nnnnn) | / 8) | + sssss |

###### Access to “memory bits” and “inputs”

When accessing SIMATIC areas “Memory bits” and “Inputs,” the remaining rest bit_number is calculated and used to address the relevant bit within the first / last memory or input byte.

###### bit_number

For **bit_number**, number of coils, values between **1** and **2040** (with ET 200S 1SI Modbus max. 1768 bits) are allowed. This number of bits is read.

> **Note**
>
> Please note the CPU-specific restrictions.

###### Application example

**Example of parameter assignment:**

**Conversion of MODBUS addressing for function code FC 02**

| MODBUS address in transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| from 0 to 4095 | commence at memory bit | M 2000.0 |
| from 4096 to 5119 | commence at input | I 128.0 |

###### Request message frame FUNCTION 02:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 02H | Function code FUNC |
| 10H | start_address "High" |
| 30H | start_address "Low" |
| 00H | bit_number "High" |
| 18H | bit_number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Response message frame FUNCTION 02:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 02H | Function code FUNC |
| 03H | Byte_count |
| 12H | <DATA 1> I 134.0 - I 134.7 |
| 34H | <DATA 2> I 135.0 - I 135.7 |
| 56H | <DATA 3> I 136.0 - I 136.7 |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "start_address" 1030 Hex (4144 decimal) is located in the "Inputs" area:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Input byte | = | ((start_address | - nnnnn) | / 8) | + sssss |
|  | = | ((4144 | - 4096) | / 8) | + 128 |
|  | = | 134 ; |  |  |  |

The remaining rest bit_number has the following result:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rest bit_no. | = | ((start_address | - nnnnn) | % 8) | [Modulo 8] |
|  | = | ((4144 | - 4096) | % 8) |  |
|  | = | 0 ; |  |  |  |

Inputs I 134.0 up to and including I 136.7 are accessed.

###### Bit number:

The number of MODBUS bits "bit_number" 0018 Hex (24 decimal) means that 24 bits = 3 bytes are to be read.

###### Further examples

Some other access examples are listed in the table below.

All examples are based on the above area specification.

| start_address |  | Access in SIMATIC beginning |  |  |  |  | -> | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hex | Decimal | (Decimal) |  |  |  |  |  |  |
| 0000 | 0 | Bit memory | ((0 | - 0) | / 8) | + 2000 | -> | M 2000.0 |
| 0071 | 113 | Bit memory | ((113 | - 0) | / 8) | + 2000 | -> | M 2014.1 |
| 0800 | 2048 | Bit memory | ((2048 | - 0) | / 8) | + 2000 | -> | M 2256.0 |
| 0D05 | 3333 | Bit memory | ((3333 | - 0) | / 8) | + 2000 | -> | M 2416.5 |
| 1000 | 4096 | Input | ((4096 | - 4096) | / 8) | + 128 | -> | I 128.0 |
| 10A4 | 4260 | Input | ((4260 | - 4096) | / 8) | + 128 | -> | I 148.4 |

##### Function Code 03 - Read Output Registers (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to read data words from a data block.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_register | register_number | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | Byte_count n | n/2 register DATA (High, Low) | CRC |

###### start_register

The MODBUS register address "**start_register**" is interpreted by the driver as follows:

![start_register](images/26569415179_DV_resource.Stream@PNG-en-US.png)

For further address generation, the driver uses the “base DB number” (commencing at DB xxxxx) entered in the dialog box "**Conversion of MODBUS addressing for FC 03, 06, 16**" during parameter assignment .

The address calculation for access, address conversion, is carried out as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| Access to SIMATIC |  | Conversion formula |  |
| Data block DB  (resulting DB) | = | (base DB number xxxxx | + start_register offset_DB_No.) |
| Data word DBW | = | (start_register word_No. | ∗ 2) |

###### Calculation formula for start_register

Providing the resulting DB to be read is known, the MODBUS address **start_register** required in the master system can be calculated in accordance with the following formula:

|  |  |  |
| --- | --- | --- |
| start_register | = | ((resulting DB – base DB number) * 512) +  (data word_DBW / 2) |

This is based on even numbered data word numbers only.

###### register_number

For **bit_number**, number of registers, values between **1** and **127** (with ET 200S 1SI Modbus max. 110 bits) are allowed. This number of registers is read. Please observe the following rule:

|  |  |  |
| --- | --- | --- |
| (register_number)<sub>max</sub> | = | 512 - start_register |

> **Note**
>
> Note the CPU-specific restrictions.

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function codes FC 03, 06 and 16

| MODBUS address in  transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| 0 | commence at data block  (base DB number) | DB 800 |

###### Request message frame FUNCTION 03:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 03H | Function code FUNC |
| 00H | start_register "High" |
| 50H | start_register "Low" |
| 00H | register_number "High" |
| 02H | register_number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Response message frame FUNCTION 03:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 03H | Function code FUNC |
| 04H | Byte_count |
| 87H | <DATA 1> DBW 160 "High" |
| 65H | <DATA 2> DBW 160 "Low" |
| 43H | <DATA 3> DBW 161 "High" |
| 21H | <DATA 4> DBW 161 "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "start_register" 0050 Hex (80 decimal) is interpreted as follows:

![Address calculation:](images/18614197899_DV_resource.Stream@PNG-en-US.png)

DB 800, data word DBW 160 is accessed.

###### Register number:

The number of MODBUS registers "register_number" 0002 Hex (2 decimal) means that 2 registers = 2 data words are read.

###### Further examples

Some other access examples are listed in the table below.

|  |  |  | start_register |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| start_register |  | Base DB no. | Offset DB_no. | Word number |  | Resulting DB | DBW |
| Hex | Decimal | Decimal | Decimal | Hex | Decimal | Decimal | Decimal |
| 0000 | 0 | 800 | 0 | 000 | 0 | 800 | 0 |
| 01F4 | 500 | 800 | 0 | 1F4 | 500 | 800 | 1000 |
| 0200 | 512 | 800 | 1 | 000 | 0 | 801 | 0 |
| 02FF | 767 | 800 | 1 | 0FF | 255 | 801 | 510 |
| 0300 | 768 | 800 | 1 | 100 | 256 | 801 | 512 |
| 03FF | 1023 | 800 | 1 | 1FF | 511 | 801 | 1022 |
| 0400 | 1024 | 800 | 2 | 000 | 0 | 802 | 0 |

##### Function code 04 -  Read Input Registers (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to read data words from a data block.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_register | register_number | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | Byte_count n | n/2 register DATA (High, Low) | CRC |

###### start_register

The MODBUS register address "**start_register**" is interpreted by the driver as follows:

![start_register](images/26569415179_DV_resource.Stream@PNG-en-US.png)

For further address generation, the driver uses the “base DB number” (commencing at DB xxxxx) specified in the dialog box "**Conversion of MODBUS addressing for FC4**" .

The address calculation for access, address conversion, is carried out in two steps as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| Access to  SIMATIC |  | Conversion formula |  |
| Data block DB  (resulting DB) | = | (base DB number xxxxx + start_register-offset_DB_no.) |  |
| Data word DBW | = | (start_register word_No. | ∗ 2) |

###### Calculation formula for start_register

Providing the resulting DB to be read is known, the MODBUS address **start_register** required in the master system can be calculated in accordance with the following formula:

|  |  |  |
| --- | --- | --- |
| start_register | = | ((resulting DB – base DB number) * 512) + (data word_DBW / 2) |

Only even numbered data word numbers are permissible.

###### register_number

For **bit_number**, number of registers, values between **1** and **127** (with ET 200S 1SI Modbus max. 110 bits) are allowed. This number of registers is read. Please observe the following rule:

|  |  |  |
| --- | --- | --- |
| (register_number)<sub>max</sub> | = | 512 - start_register |

> **Note**
>
> Note the CPU-specific restrictions.

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function code FC 04

| MODBUS address in transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| 0 | commence at data block  (base DB number) | DB 900 |

###### Request message frame FUNCTION 04:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 04H | Function code FUNC |
| 02H | start_register "High" |
| C0H | start_register "Low" |
| 00H | register_number "High" |
| 03H | register_number "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Response message frame FUNCTION 04:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 04H | Function code FUNC |
| 06H | Byte_count |
| A1H | <DATA 1> DBW 384 "High" |
| A2H | <DATA 2> DBW 384 "Low" |
| A3H | <DATA 3> DBW 385 "High" |
| A4H | <DATA 4> DBW 385 "Low" |
| A5H | <DATA 5> DBW 386 "High" |
| A6H | <DATA 6> DBW 386 "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "start_register" 02C0 Hex (704 decimal) is interpreted as follows:

![Address calculation:](images/24499773067_DV_resource.Stream@PNG-en-US.png)

DB 901, data word DBW 384 is accessed.

###### Register number:

The number of MODBUS registers "register_number" 0003 Hex (3 decimal) means that 3 registers = 3 data words are read.

###### Further examples

Some other access examples are listed in the table below.

|  |  |  | start_register |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| start_register |  | Base DB no. | Offset DB_no. | Word number |  | Resulting DB | DBW |
| Hex | Decimal | Decimal | Decimal | Hex | Decimal | Decimal | Decimal |
| 0000 | 0 | 900 | 0 | 000 | 0 | 900 | 0 |
| 0064 | 100 | 900 | 0 | 064 | 100 | 900 | 200 |
| 00C8 | 200 | 900 | 0 | 0C8 | 200 | 900 | 400 |
| 0190 | 400 | 900 | 0 | 190 | 400 | 900 | 800 |
| 1400 | 5120 | 900 | 10 | 000 | 0 | 910 | 0 |
| 1464 | 5220 | 900 | 10 | 064 | 100 | 910 | 200 |
| 14C8 | 5320 | 900 | 10 | 0C8 | 200 | 910 | 400 |

##### Function Code 05 - Force Single Coil (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to write a bit into the SIMATIC memory of the CPU as listed below.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | coil_address | DATA on/off | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | coil_address | DATA on/off | CRC |

###### coil_address

The MODBUS bit address "**coil_address**" is interpreted by the driver as follows:

The driver checks whether "coil_address" is located within one of the areas which were entered during parameter assignment in the dialog box "**Conversion of MODBUS Addressing for FC 01, 05, 15**" (from/to: memory bits, outputs, timers, counters).

|  |  |  |
| --- | --- | --- |
| If the  MODBUS bit address **coil_address**  is located in the area | the  **SIMATIC memory area** is accessed |  |
| from aaaaa to bbbbb | commence at memory bit | M uuuuu.0 |
| from ccccc to ddddd | commence at output | Q ooooo.0 |

The address calculation for access (address conversion) is carried out as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Access beginning with SIMATIC |  | Conversion formula |  |  |  |
| Memory byte | = | ((coil_address | - aaaaa) | / 8) | + uuuuu |
| Output byte | = | ((coil_address | - ccccc) | / 8) | + ooooo |

###### Access to “memory bits” and “outputs”

When accessing the SIMATIC areas "memory bits" and "outputs", the remaining rest bit_number is calculated and used to address the relevant bit within the memory or output byte.

###### Access to "timers" and "counters"

Access to the SIMATIC timers and counters areas is not permitted with function code FC 05 and is rejected by the driver with an error message frame.

###### DATA on/off

The following two values are permitted as **DATA-on/off**:

- FF00H -> Set bit.
- 0000H -> Delete bit.

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function codes FC 01, 05, 15

| MODBUS address in  transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| from 0 to 2047 | commence at memory bit | M 1000.0 |
| from 2048 to 2559 | commence at output | Q 256.0 |

###### Request message frame FUNCTION 05:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 05H | Function code FUNC |
| 08H | coil_address "High" |
| 09H | coil_address "Low" A257.1 |
| FFH | DATA on/off "High" |
| 00H | DATA on/off "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Reply message frame FUNCTION 05:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 05H | Function code FUNC |
| 08H | coil_address "High" |
| 09H | coil_address "Low" A257.1 |
| FFH | DATA on/off "High" |
| 00H | DATA on/off "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "coil_address" 0809 Hex (2057 decimal) is located in the "outputs" area:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Output byte | = | ((coil_address | - ccccc) | / 8) | + ooooo |
|  | = | ((2057 | - 2048) | / 8) | + 256 |
|  | = | 257 ; |  |  |  |

The remaining rest bit_number has the following result:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rest bit_no. | = | ((coil_address | - ccccc) | % 8) | [Modulo 8] |
|  | = | ((2057 | - 2048) | % 8) |  |
|  | = | 1 ; |  |  |  |

Output Q 257.1 is accessed.

###### Further examples

For further examples of access to memory bits and outputs, refer to FC 01.

##### Function code 06 - Preset Single Register (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to write a data word in a data block of the CPU.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_register | DATA value (High, Low) | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_register | DATA value (High, Low) | CRC |

###### start_register

The MODBUS register address "**start_register**" is interpreted by the driver as follows:

![start_register](images/26569415179_DV_resource.Stream@PNG-en-US.png)

For further address generation, the driver uses the "base DB number" commencing at DB xxxxx entered in the dialog box "**Conversion of MODBUS addressing for FC 03, 06, 16**" during parameter assignment .

The address calculation for access, address conversion, is carried out in two steps as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| Access to  SIMATIC |  | Conversion formula |  |
| Data block DB  (resulting DB) | = | (base DB number xxxxx + start_register-offset_DB_no.) |  |
| Data word DBW | = | (start_register word_No. | ∗ 2) |

###### Calculation formula for start_register

Providing the resulting DB to be written is known, the MODBUS address **start_register** required in the master system can be calculated in accordance with the following formula:

|  |  |  |
| --- | --- | --- |
| start_register | = | ((resulting DB – base DB number) * 512) + (data word_DBW / 2) |

Only even numbered data word numbers are permissible.

###### DATA Value

Any value can be used as the DATA **value**, register value.

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function codes FC 03, 06 and 16

| MODBUS address in transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| 0 | commence at data block  (base DB number) | DB 800 |

###### Request message frame FUNCTION 06:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 06H | Function code FUNC |
| 01H | start_register "High" |
| 80H | start_register "Low" DBW 768 |
| 2BH | DATA value "High" |
| 1AH | DATA value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Reply message frame FUNCTION 06:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 06H | Function code FUNC |
| 01H | start_register "High" |
| 80H | start_register "Low" DBW 768 |
| 2BH | DATA value "High" |
| 1AH | DATA value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "start_register" 0180 Hex (384 decimal) is interpreted as follows:

![Address calculation:](images/18614260107_DV_resource.Stream@PNG-en-US.png)

DB 800, data word DBW 768 is accessed.

###### Further examples

For further access examples, please refer to FC 03.

##### Function code 08 - Loop back Diagnostic Test (S7-300, S7-400)

###### Function

This function is used to check the communications connection.

It has no effect on the S7 CPU, the user programs or user data. The received message frame is returned to the master system by the driver independently.

###### Request message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | Diagnostic code (High,Low) | Test Data | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | Diagnostic code (High,Low) | Test Data | CRC |

###### Diagnostic Code

Only **Diagnostic Code 0000** is supported!

###### Test Data

Any16-bit value.

###### Application example

**Request message frame FUNCTION 08:**

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 08H | Function code FUNC |
| 00H | Diagnostic code "High" |
| 00H | Diagnostic code "Low" |
| A5H | Test value "High" |
| C3H | Test value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Reply message frame FUNCTION 08:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 08H | Function code FUNC |
| 00H | Diagnostic code "High" |
| 00H | Diagnostic code "Low" |
| A5H | Test value "High" |
| C3H | Test value "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

##### Function code 15 - Force Multiple Coils (S7-300, S7-400)

###### Function

This function enables the MODBUS master system to write several bits to the SIMATIC memory areas listed below.

###### Request message frame

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ADDR | FUNC | start_address | quantity | byte_count n | n DATA | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_address | quantity | CRC |

###### start_address

The MODBUS bit address "**start_address**" is interpreted by the driver as follows:

The driver checks whether “start_address” is located within one of the areas which were entered during parameter assignment in the dialog box "**Conversion of MODBUS addressing for FC 01, 05, 15**" (from/to: memory bits, outputs, timers, counters).

|  |  |  |
| --- | --- | --- |
| If the MODBUS bit address is located in area **start_address** , | **SIMATIC memory area** is accessed |  |
| from aaaaa to bbbbb | commence at memory bit | M uuuuu.0 |
| from ccccc to ddddd | commence at output | Q ooooo.0 |

The address calculation for access, address conversion, is carried out as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Access beginning with SIMATIC |  | Conversion formula |  |  |  |
| Memory byte | = | ((start_address | - aaaaa) | / 8) | + uuuuu |
| Output byte | = | ((start_address | - ccccc) | / 8) | + ooooo |

###### Access to “memory bits” and “outputs”

When accessing the SIMATIC areas "memory bits" and "outputs", the remaining rest bit_number is calculated and used to address the relevant bit within the memory or output byte.

###### Access to "timers" and "counters"

Access to the SIMATIC timers and counters areas is not permitted with function code FC 15 and is rejected by the driver with an error message frame.

###### Quantity

For **quantity**, bit number, any value between **1** and **2040** (with ET 200S 1SI Modbus max. 1976 bits) is allowed.

> **Note**
>
> Please note the CPU-specific restrictions.

###### DATA

Any values are contained in the **DATA field** as bit statuses.

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function codes FC 01, 05 and 15

| MODBUS address in transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| from 0 to 2047 | commence at memory bit | M 1000.0 |
| from 2048 to 2559 | commence at output | Q 256.0 |

###### Action:

The MODBUS master system wants to write the following bit statuses on to memory bits M 1144.0 ... M 1144.7 and M 1145.0 ... M 1145.3:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Memory bit M 1144 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | Bit |
|  | ON | ON | OFF | OFF | ON | ON | OFF | ON |  |
|  |  |  |  |  |  |  |  |  |  |
| Memory bit M 1145 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | Bit |
|  | - | - | - | - | ON | OFF | OFF | ON |  |

###### Request message frame FUNCTION 15:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 0FH | Function code FUNC |
| 04H | start_address "High" |
| 80H | start_address "Low" (M 1144.0 ... ) |
| 00H | quantity "High" |
| 0CH | quantity "Low" (12 bits) |
| 02H | bytecount |
| CDH | status coil (M 1144.0 ... M 1144.7) |
| 09H | status coil (M 1145.0 ... M 1145.3) |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Response message frame FUNCTION 15:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 0FH | Function code FUNC |
| 04H | start_address "High" |
| 80H | start_address "Low" |
| 00H | quantity "High" |
| 0CH | quantity "Low" |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "coil_address" 0480 Hex (1152 decimal) is located in the "memory bit" area:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Memory byte | = | ((start_address | - aaaaa) | / 8) | + uuuuu |
|  | = | ((1152 | - 0) | / 8) | + 1000 |
|  | = | 1144 ; |  |  |  |

The remaining rest bit_number has the following result:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rest bit_no. | = | ((start_address | - aaaaa) | % 8) | [Modulo 8] |
|  | = | ((1152 | - 0) | % 8) |  |
|  | = | 0 ; |  |  |  |

Access is made to memory bits commencing at M 1144.0.

###### Further examples

For further examples of access to memory bits and outputs, refer to FC 01.

##### Function code 16 - Preset Multiple Registers (S7-300, S7-400)

###### Function

The function code enables the MODBUS master system to write several data words in a data block of the SIMATIC CPU.

###### Request message frame

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ADDR | FUNC | start_register | quantity | byte_count n | n-DATA (High,Low) | CRC |

###### Response message frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADDR | FUNC | start_register | quantity | CRC |

###### start_register

The MODBUS register address "**start_register**" is interpreted by the driver as follows:

![start_register](images/26569415179_DV_resource.Stream@PNG-en-US.png)

For further address generation, the driver uses the "base DB number" commencing at DB xxxxx entered in the dialog box "**Conversion of MODBUS addressing for FC 03, 06, 16**" during parameter assignment .

The address calculation for access, address conversion, is carried out in two steps as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| Access to SIMATIC |  | Conversion formula |  |
| Data block DB  (resulting DB) | = | (base DB number xxxxx + start_register-offset_DB_no.) |  |
| Data word DBW | = | (start_register word_No. | ∗ 2) |

###### Calculation formula for start_register

Providing the resulting DB to be written is known, the MODBUS address **start_register** required in the master system can be calculated in accordance with the following formula:

|  |  |  |
| --- | --- | --- |
| start_register | = | ((resulting DB – base DB number) * 512) + (data word_DBW / 2) |

Only even numbered data word numbers are permissible.

###### Quantity

For **quantity**, register number, any value between **1** and **127** (with ET 200S 1SI Modbus max. 123 bits) is allowed. Please observe the following rule:

|  |  |  |
| --- | --- | --- |
| (Quantity)<sub>max</sub> | = | 512 - start_register |

> **Note**
>
> Please note the CPU-specific restrictions.

###### DATA (High,Low)

Any value can be used as DATA **DATA (High,Low)** (register value).

###### Application example

**Example of parameter assignment:**

Conversion of MODBUS addressing for function codes FC 03, 06, 16

| MODBUS address in  transmission message frame | SIMATIC memory area |  |
| --- | --- | --- |
| 0 | commence at data block  (base DB number) | DB 800 |

###### Action:

The MODBUS master system wants to write the values CD09 Hex, DE1A Hex and EF2B Hex to data words DBW 100, DBW 102 and DBW 104 of DB 800.

###### Request message frame FUNCTION 16:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 10H | Function code FUNC |
| 00H | start_register "High" |
| 32H | start_register "Low" DBW 100 |
| 00H | quantity "High" |
| 03H | quantity "Low" (3 registers) |
| 06H | bytecount |
| CDH | register value -High (DBW100) |
| 09H | register value -Low |
| DEH | register value -High (DBW102) |
| 1AH | register value -Low |
| EFH | register value -High (DBW104) |
| 2BH | register value -Low |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Response message frame FUNCTION 16:

| Symbol | Meaning |
| --- | --- |
| 05H | Slave address ADDR |
| 10H | Function code FUNC |
| 00H | start_register "High" |
| 32H | start_register "Low" |
| 00H | quantity "High" |
| 03H | quantity "Low" (3 registers) |
| xxH | CRC checksum "Low" |
| xxH | CRC checksum "High" |

###### Address calculation:

The MODBUS address "start_register" 0032 Hex (50 decimal) is interpreted as follows:

![Address calculation:](images/18614291211_DV_resource.Stream@PNG-en-US.png)

DB 800, data word DBW 100 is accessed.

###### Further examples

For further access examples, please refer to FC 03.

### Error message area (S7-300, S7-400)

#### Numbering scheme event class / event number

![Numbering scheme event class / event number](images/25969465867_DV_resource.Stream@PNG-en-US.png)

#### Event classes

| Event class | Meaning |
| --- | --- |
| 2 | Error initializing |
| 5 | Error executing a CPU job |
| 8 | Receive errors |
| 14 (0E<sub>H</sub>) | General processing error |
| 30 (1E<sub>H</sub>) | Error during communication between serial port and the CPU. |

#### Event class / event number

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0201 | No (valid) configuration available. | Provide the module with correct parameters. If necessary, ensure the system is correctly installed. |
| 0502 | Order inadmissible in this operating mode of the serial interface module ET 200S Modbus/USS (example: device interface is not configured). | Evaluate the diagnostic interrupt and rectify the error accordingly. |
| 050E | Invalid telegram length | The send message frame is longer than 224 bytes. The send job was aborted by the ET 200S Modbus/USS module.  Select a shorter telegram length. |
| 0518 | - Transmission length during sending is too large (> 4 Kbyte) - The transmission length during SEND is too small. | Check LEN parameter on SEND. |
| 0530 | Modbus master send job rejected because the response of the communication partner to a previous reading Modbus master send job has not yet been retrieved. | After a successful read Modbus master send job, you must first read the response from the communication partner from the module before you start a new Modbus master send job. |
| 0551 | Frame sequence errors in the communication between the serial interface module ET 200S Modbus/USS and the CPU. The error occurred while transmitting a received message frame of the ET 200S SI serial interface module to the CPU. | The module and the CPU have canceled the transmission. Repeat the receive job. The ET 200S Modbus/USS serial interface module sends the received message again. |
| 0806 | Character delay time ZVZ exceeded | Error by the partner device or repair disruptions on the transmission line. |
| 080A | Overflow of the receive buffer at the master during the reception of the response message frame. | Check the protocol settings of the slave. |
| 080C | A transmission error was recognized in a character (parity error, overrun error, stop bit error (frame)). | Check to see if the disruptions have an effect on the transmission line. If applicable, change the system structure and the cable routing.  Check to see if the protocol parameters for data transmission rate, data bit number, parity, stop bit number are identically set for the communication module and connection partner. |
| 080D | BREAK  The receive line to the partner device is disrupted. | Establish the connection between the devices or switch on the partner device.  During TTY mode, check to see if the line current is flowing in idle state. If applicable, check and change the default setting of the 2-wire receive line R(A), R(B) with an RS422/485 (X27) connection. |
| 0810 | Parity error: There is a break in the connection (line break) between the two communication partners. | Check the connection line of the communication partners or verify that both devices are configured with the same data transmission rate, parity and stop bit number.  Change your system setup or cable wiring. |
| 0811 | Character frame error: There is a break in the connection (line break) between the two communication partners. | Check the connection line of the communication partners or verify that both devices are configured with the same data transmission rate, parity and stop bit number.  Change your system setup or cable wiring. |
| 0812 | Additional characters were received after the CTS serial port was set to OFF. | Reconfigure the communications partner or fetch from the serial interface faster. |
| 0830 | The response monitoring time after sending a request message frame expired without the beginning of the response message frame being recognized. | Check if transmission line is interrupted (interface analyzer may be required).  Check to see if the protocol parameters for data transmission rate, data bit number, parity, stop bit number are identically set for the communication module and connection partner.  In the properties dialog of the module, check if the configured response monitoring time is set high enough.  Check to see if the specified slave address is available. |
| 0831 | The first character of the response message frame from the slave is different from the slave address sent in the request message frame (with "normal" operating mode). | The wrong slave has replied.  Check if transmission line is interrupted (interface analyzer may be required). |
| 0832 | Overflow of the receive buffer in the communication module upon receipt of the response message frame. | Check the protocol settings of the slave. |
| 0833 | Bit or register number for function code FC 15/16 and message frame element byte_count do not match. | Correct the bit/register number or byte_count. |
| 0834 | Illegal bit coding for "Set bit / Reset bit" recognized. | Use only the 0000Hex or FF00Hex codes for FC05. |
| 0835 | Illegal diagnostic subcode (not 0000Hex) at function code FC 08 "Loop back test" recognized. | Use only the subcode 0000Hex for FC08. |
| 0836 | The internally formed value of the CRC 16 checksum does not match the received CRC checksum. | Check the formation of the CRC checksum on the Modbus master system. |
| 0837 | Message frame sequence error: The Modbus master system sent a new request message frame before the last response message frame was transmitted by the driver. | Increase the timeout on the slave response message frame for Modbus master system. |
| 0850 | Length of the receive message frame greater than 224 bytes or greater than the configured message frame length. | Adjust the message frame length of the partner. |
| 0E01 | Error during initialization of the driver-specific SCC process. | Reassign parameters of driver and reload. |
| 0E02 | Error during startup of driver: Wrong SCC process active (SCC driver). The driver cannot function with this SCC driver. | Reassign parameters of driver and reload. |
| 0E03 | Error during startup of driver: Wrong data transmission process active (interface to instructions). The driver cannot work with this data transmission process. | Reassign parameters of driver and reload. |
| 0E04 | Error during startup of driver: Illegal interface submodule. The driver cannot run with the configured interface submodule. | Check and correct the parameter assignment. |
| 0E05 | Error with driver dongle: No dongle plugged in, or inserted dongle is faulty. The driver is not ready to run. | Check if a driver dongle is plugged into the communication module. If the inserted dongle is faulty, replace it with a functioning dongle. |
| 0E06 | Error with driver dongle: The dongle has no valid content. The driver is not ready to run. | Obtain a correct dongle from the SIEMENS office which supplied you with the driver. |
| 0E10 | Internal error procedure:  Default branch in procedure automatic device. | Restart the communication module (POWER_ON) |
| 0E11 | Internal error procedure:  default branch for procedure status Send / Receive. | Restart the communication module (POWER_ON) |
| 0E12 | Internal error active automatic device:  Default branch | Restart the communication module (POWER_ON) |
| 0E13 | Internal error passive automatic device:  Default branch | Restart the communication module (POWER_ON) |
| 0E20 | The number of data bits for this connection must be 8.  The driver is not ready to run. | Correct the parameter assignment of the driver. |
| 0E21 | The multiplication factor set for the character delay time is not within the value range of 1 to 10. The driver is operating with a default setting of 1. | Correct the parameter assignment of the driver. |
| 0E22 | The operating mode set for the driver is illegal.  “Normal operation” or “Interference Suppression” must be specified. The driver is not ready to run. | Correct the parameter assignment of the driver. |
| 0E23 | An illegal value for the response monitoring time has been set:  Valid values are 5 to 65500ms. The driver is not ready to run. | Correct the parameter assignment of the driver. |
| 0E24 | Invalid limits were configured for write access. The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E25 | An invalid "from/to" combination was configured in the specification of the "Conversion of the Modbus addresses with function code FC 01, 05, 15" area.  (Memory bits, outputs, timers, counters area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E26 | An invalid "from/to" combination was configured in the specification of the "Conversion of the Modbus addresses with function code FC 02" area.  (Memory bits, inputs area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E27 | An overlap was configured in the specification of the "Conversion of the Modbus addresses with function code FC 01, 05, 15" area.  (Memory bits, outputs, timers, counters area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E28 | An overlaps was configured in the specification of the "Conversion of the Modbus addresses with function code FC 02" area.  (Memory bits, inputs area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E2E | An error occurred when reading the interface parameter file. The driver is not ready to run. | Restart the communication module (POWER_ON). |
| 0E30 | Internal error during data transmission to CPU:  Unexpected acknowledgment Passive. | Can be ignored if it happens intermittently. |
| 0E31 | Timeout during data transmission to CPU. | Check CP-CPU interface. |
| 0E32 | Error occurred during data transmission to CPU with RCV: Exact failure reason (detailed error) is in SYSTAT before this entry. | Check CP-CPU interface. |
| 0E33 | Internal error during data transmission to CPU:  Illegal status of automatic device | Check CP-CPU interface. |
| : |  |  |
| 0E38 | An error has occurred accessing SIMATIC areas "Memory bit, output, timers, counters, input" with the function code FC 01 or FC 02: For example, input not available or attempt to read beyond the end of the area. | Check whether the addressed SIMATIC area exists and that no attempt was made to access beyond the end of the area. |
| 0E39 | An error has occurred accessing the SIMATIC "Data block" area with the function code FC 03, 04, 06, 16: Data block not available or too short. | Check if the addressed data block exists and is sufficiently long. |
| 0E3A | An error has occurred executing a write job with the function code FC 05, 15: Instance data of the Modbus instruction is not available or too short. | Check if the configured instance DB for the Modbus communication instruction is available and is sufficiently long. |
| 0E3B | Timeout (waiting for acknowledgement) in the execution of a write job by the Modbus communication instruction. | Check the connection configuration as well as CP-CPU interface (BSEND), you may need to reload the Modbus communication instruction. |
| 0E3C | Illegal job with this driver. | Only SEND, RCV, STATUS (CP 441-2 only) permitted |
| 0E40 | Value specified for LEN parameter in the SEND instruction is too low. | Minimum length is 2 bytes. |
| 0E41 | Value specified for LEN parameter in the SEND instruction is too low. A greater length is required for the transferred function code. | The minimum length for this function code is 6 bytes. |
| 0E42 | Transferred function code is illegal. | The only function codes permitted are those listed in the section " [Function codes](#function-codes-s7-300-s7-400) ". |
| 0E43 | Slave address 0 (= Broadcast) not permitted with this function code. | Only use slave address 0 for the suitable function codes. |
| 0E44 | The value of the transferred “Bit number” parameter is not within the range 1 to 2040. | The “Bit number” parameter must be within the range 1 to 2040. |
| 0E45 | The value of the transferred “Register number” parameter is not within the range 1 to 127. | The “Register number” parameter must be within the range 1 to 127. |
| 0E46 | Function codes 15 or 16: The value of the transferred “Bit number” or “Register number” parameter is not within the range 1 to 2040 and/or 1 to 127. | The “Bit number” or “Register number” parameter must be within the range 1 to 2040 and/or 1 to 127. |
| 0E47 | Function codes 15 or 16: The LEN parameter for the SEND instruction does not correspond to the transferred “Bit number” or “Register number” parameter, LEN parameter is too small. | Increase the LEN parameter for SEND until a sufficient amount of user data is transferred to the communication module. A larger amount of user data must be transferred to the communication module because of the “Bit number” or “Register number”. |
| 0E48 | Function code 05: The code specified in SEND source DB for “Set Bit” (FF00H) or “Delete Bit” (0000H) is wrong. | The only permitted codes are FF00H and 0000H. |
| 0E49 | Function code 08: The code specified in SEND source DB for “Diagnostic Code” is wrong. | The only permitted code is “Diagnostic Code” 0000H. |
| 0E50 | In the word-based SIMATIC timers/counters areas, the resulting residual bit number from the Modbus address is ≠ 0. | Only use Modbus addresses that result in valid bit numbers. |
| 0E51 | The received Modbus address is outside the configured "from/to" areas. | Only use addresses as address information in the request message frame that have previously been defined in the configuration. |
| 0E52 | - A SIMATIC area limit was exceeded during an access attempt by the Modbus master system: Resulting DB number < 1 - Write access to an unreleased area (configuration) - Write access to the instance DB of the communication instruction | Access area limited to valid SIMATIC memory areas. |
| 0E53 | A SIMATIC area limit was exceeded during an access attempt by the Modbus master system: For example, overflow from the formation of the resulting DB no. (> 65535) | Access area limited to valid SIMATIC memory areas. |
| 0E54 | Access beyond the configured area end or access beyond the SIMATIC area end. | Access area limited to valid SIMATIC memory areas. |
| 0E55 | Write access to this SIMATIC memory area is not allowed. | Write only to the SIMATIC memory bits, outputs data areas. |
| 0E56 | The coupling cannot be operated because the communication instruction is not running. | Call the Modbus communication instruction in the STEP 7 user program cyclically. You may need to repeat initialization of the communication instruction. |
| 0E57 | An error has occurred executing the Modbus function code in the communication instruction. | Analyze the exact cause. |
| 0E4A | The length of this function code is greater than the maximum length. | The manual contains the maximum lengths for each function code. |
| 0E4F | CP 441: The R_ID specified in the SEND instruction is invalid for this driver. | Only use R_IDs 0 to 255  (00 00 00 00 ... 00 00 00 FFH) |
| CP 341: The R_TYPE specified at the SEND_RK instruction is invalid for this driver. | "X" has to be entered as R_TYP. |  |
| 0E50 | Slave address incorrect: The received slave address is different from the sent slave address. | The wrong slave has replied.  Check if transmission line is interrupted (interface analyzer may be required). |
| 0E51 | Function code incorrect:  The function code received in the response message frame is different from the sent function code. | Check the slave device. |
| 0E52 | Byte Underflow: Amount of characters received is less than should have resulted from the byte counter of the response message frame, or is less than expected with this function code. | Check the slave device. |
| 0E53 | Byte Overflow: Amount of characters received is more than should have resulted from the byte counter of the response message frame, or is more than expected with this function code. | Check the slave device. |
| 0E54 | Byte counter too small: The byte counter received in the response message frame is too small. | Check the slave device. |
| 0E55 | Byte counter wrong: The byte counter received in the response message frame is wrong. | Check the slave device. |
| 0E56 | Echo wrong: The data of the response message frame (amount of bits, ...) echoed from the slave are different from the data sent in the request message frame. | Check the slave device. |
| 0E57 | CRC Check incorrect: An error has occurred on checking the CRC 16 checksum of the response message frame from the slave. | Check the slave device. |
| 0E61 | Response message frame with exception code 01: Illegal function | See “Manual of Slave Device” |
| 0E62 | Response message frame with exception code 02: Illegal data address | See “Manual of Slave Device” |
| 0E63 | Response message frame with exception code 03: Illegal data value | See “Manual of Slave Device” |
| 0E64 | Response message frame with exception code 04: Failure in associated device | See “Manual of Slave Device” |
| 0E65 | Response message frame with exception code 05: Acknowledge | See “Manual of Slave Device” |
| 0E66 | Response message frame with exception code 06: Busy, Rejected message | See “Manual of Slave Device” |
| 0E67 | Response message frame with exception code 07: Negative Acknowledgement | See “Manual of Slave Device” |
| 1E0D | "Job aborted due to warm restart, hot restart or reset" |  |
| 1E0E | Static error calling instruction DP_RDDAT. The RET_VAL return value of the instruction is provided to you in the SFCERR tag in the instance DB for evaluation. | Load the SFCERR tag from the instance DB. |
| 1E0F | Static error calling instruction DP_WRDAT. The RET_VAL return value of the instruction is provided to you in the SFCERR tag in the instance DB for evaluation. | Load the SFCERR tag from the instance DB. |
| 1E10 | Static error calling instruction RD_LGADR. The RET_VAL return value of the instruction is provided to you in the SFCERR tag in the instance DB for evaluation. | Load the SFCERR tag from the instance DB. |
| 1E11 | Static error calling instruction RDSYSST. The RET_VAL return value of the instruction is provided to you in the SFCERR tag in the instance DB for evaluation. | Load the SFCERR tag from the instance DB. |
| 1E20 | Parameter out of range. | Enter a parameter within the range valid for the function module. |
| 1E41 | Number of bytes specified in the LEN parameter of the instruction invalid. | You must stay within a range of values of 1 to 256 bytes. |

## USS communication (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of USS communication (S7-300, S7-400)](#overview-of-uss-communication-s7-300-s7-400)
- [USS-master (S7-300, S7-400)](#uss-master-s7-300-s7-400)

### Overview of USS communication (S7-300, S7-400)

#### Position in the system environment

The following USS description refers to the operation of the ET 200S 1SI module in the Modbus/USS model.

#### Introduction

The USS protocol is a straightforward serial data transmission protocol designed to meet the requirements of drive technology.

The USS protocol defines an access method based on the master-slave principle for communication via a serial bus. One master and up to 31 slaves can be connected to the bus. Master and slaves form a USS network. The data exchanged between master and slave are referred to as network data. The network data block contains the data for the master. The individual slaves are selected by the master using an address character in the message frame. A slave can never send anything without first being initiated by the master. Therefore, direct data transmission between individual slaves is not possible. Communication functions in half-duplex mode. The master function cannot be transferred. The USS system has only one master.

#### Message frame structure

Each message frame begins with a start character (STX), followed by the length specification (LGE) and the address byte (ADR). The data field comes after that. The message frame ends with the block check character (BCC).

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| STX | LGE | ADR | 1 | 2 | ... | N | BCC |

For single-word (16-bit) data in the network data block, the high byte is sent first, followed by the low byte. Correspondingly, with double-word data the high word is sent first, followed by the low word.

The protocol does not identify any tasks in the data fields.

#### Data encryption

The data is encrypted as follows:

- STX: 1 byte, start of text, 02H
- LGE: 1 byte, contains the message frame length as a binary number
- ADR: 1 byte, contains the slave address and message frame type in binary code
- Data fields: One byte each, contents are task-dependent
- BCC: 1 byte, block check character

#### Data transmission procedure

The master ensures cyclic data transmission in message frames. The master addresses all slave nodes one after another with a task message frame. The nodes addressed respond with a response frame. In accordance with the master-slave procedure, the slave must send the response frame to the master after it has received the task message frame. Only then can the master address the next slave.

#### General structure of the network data block

The network data block is split into two areas: the parameter area (PKW) and the process data area (PZD).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| STX | LGE | ADR | Parameter (PKW) | Process data (PZD) | BCC |

- **Parameter area** (PKW)

  The PKW area handles parameter transmission between two communication partners (e.g., the controller and drive). This involves, for example, reading and writing parameter values and reading parameter descriptions and the associated text. The PKW interface generally contains tasks for operation and display, maintenance and diagnostics.
- **Process data area** (PZD)

  The PZD area consists of signals that are required for automation:

  - Control words and setpoints from the master to the slave
  - Status words and actual values from the slave to the master

  The contents of the parameter area and process data area are defined by the slave drives. For additional information on this, refer to the drive documentation.

### USS-master (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of functions (S7-300, S7-400)](#overview-of-functions-s7-300-s7-400)

#### Overview of functions (S7-300, S7-400)

##### Network data transmission sequence

The instructions handle network data transmission in cycles with up to 31 drive slaves, in accordance with the sequence specified in the polling list (configuration DB). Only one job is active for each slave at any one time. The user stores the network data for each slave in a data block (network data block) and calls it from there. As specified in the program definition in the polling list, the data is transmitted to and called from the communications processor via another data storage area (communications processor DB).

Two function calls are required for this procedure (one send and one receive instruction). Another function supports the generation and presetting of the data blocks required for communication.

**Performance features:**

- Creation of data storage areas for communication, depending on the bus configuration
- Presetting of the polling list
- Message frame structure in accordance with the USS specification
- Network data exchange can be parameterized in accordance with the required network data structure
- Execution and monitoring of PKW jobs
- Handling of parameter change reports
- Monitoring of the complete system and error elimination

Various network data structures can be used to send network data. In other words, the content of network data can be selected according to a given application.

Depending on the structure selected, the network data has a PZD area for process data and a PKW area for parameter processing.

In the PKW area, the master can read and write parameter values, and the slave can display parameter changes by means of parameter change reports.

The PZD area contains signals required for process control, such as control words and setpoints from the master to the slave, and status words and actual values from the slave to the master.

The correct sequence for instruction calls is: S_USST, S_SEND, S_RCV, S_USSR. This is important because the outputs of the S_SEND and S_RCV instructions are only valid in the current cycle of the automation system.

The figure below shows the data traffic between the user program and the USS slave.

![Data traffic between the user program and the USS slave](images/23893238155_DV_resource.Stream@PNG-en-US.png)

Data traffic between the user program and the USS slave

##### Further Information

Information about the data blocks used can be found here:

- [Network data DB](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#network-data-db-s7-300-s7-400)
- [Network data DB](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#network-data-db-s7-300-s7-400-1)
- [Communication processor DB](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#communication-processor-db-s7-300-s7-400)

## Startup and Diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Startup characteristics (S7-300, S7-400)](#startup-characteristics-s7-300-s7-400)
- [Diagnostic functions (S7-300, S7-400)](#diagnostic-functions-s7-300-s7-400)

### Startup characteristics (S7-300, S7-400)

#### Startup characteristics

The start of the communication module is divided into the following phases:

- Initialization (POWER ON of the communication module)
- Parameter assignment

#### Initialization

Once the communication module is connected to power and after the completion of a hardware test program, the firmware is prepared for the operation on the communication module.

#### Parameter assignment

During the parameter assignment phase, the communication module receives the module parameters assigned to the current slot. The communication module is now operational.

#### Operating mode transitions

After the communication module starts up, all data between the CPU and the communication module is exchanged via instructions. The operating state transition characteristics of the communication module depends on the operating mode of the CPU.

| Symbol | Meaning |
| --- | --- |
| CPU STOP | Active data transmission from the communication module to the CPU and both sending and receiving jobs are stopped and a warm restart of the connection is initiated. |
| CPU RUN | Unlimited send and receive operation is possible in the RUN state of the CPU. The communication module and the given instruction are synchronized in the first instruction cycle following CPU warm restart,. |
| CPU warm restart | The jobs on the CPU are reset during a warm restart of the CPU; in other words, all active jobs between the CPU and the communication module are automatically cancelled. |
| Hot restart of the CPU | With a hot restart of the CPU, jobs continue to be processed.   With a corresponding configuration in the properties dialog of the module, you can automatically clear the receive buffer on the communication module during CPU startup. |

### Diagnostic functions (S7-300, S7-400)

#### Introduction

The diagnostic functions of the communication module allow errors that have occurred to be located quickly. The following diagnostic options are available to you:

| Symbol | Meaning |
| --- | --- |
| Diagnostics via the display elements of the communication module | The indicators provide information on the operating state or the possible error states of the communication module. The indicators provide an initial overview of any internal or external errors and interface-specific errors. |
| Diagnostics via the STATUS output of the instructions | Instructions have a STATUS output for error diagnostics. This output provides information about communication errors between the communication module and the CPU. You can evaluate the STATUS parameter in the user program. |
| Diagnostics on the SYSTAT error message area <sup>1)</sup> | You can query the status of an interface by programming the STATUS instruction in the user program. By reading the SYSTAT, you obtain detailed information about errors/events that have occurred in communication between the communication module and the associated CPU, as well as the connected communication partner on this interface. |
| Diagnostics via the error numbers in the response message frame | If you are using the RK512 computer connection and an error occurs with a SEND or FETCH message frame at the communication partner, the communication partner sends a response message frame with an error number in the 4th byte. |
| Diagnostics via the diagnostic buffer of the communication module | All errors/events are also entered in the diagnostic buffer <sup>2)</sup> of the communication module.   Similar to the CPU diagnostic buffer, you can also display user-specific information from the CP diagnostic buffer in plain text. |
| Diagnostic interrupt | The communication module can trigger a diagnostic interrupt on the CPU assigned to it. The communication module provides 4 bytes of diagnostic information. The analysis of this information is made via the user program or by reading the CPU diagnostic buffer. |
| <sup>1) </sup>CP 441-1 and CP 441-2 only   <sup>2)</sup> CP 340, ET 200S 1SI modules and CPU31xC-2 PtP have no diagnostic buffer |  |
