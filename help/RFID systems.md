---
title: "RFID systems"
package: SimIdentRFIDenUS
topics: 54
source: Siemens TIA Portal Information System (offline help, en-US)
---


# RFID systems

This section contains information on the following topics:

- [Communications modules](#communications-modules)
- [Reader](#reader)

## Communications modules

This section contains information on the following topics:

- [Communications module RF120C](#communications-module-rf120c)
- [Communications module RF170C](#communications-module-rf170c)
- [RF180C communications module](#rf180c-communications-module)
- [ASM 456 communications module](#asm-456-communications-module)
- [ASM 475 communications module](#asm-475-communications-module)
- [RF166C communications module](#rf166c-communications-module)
- [RF18xC/RF18xCI communication module](#rf18xcrf18xci-communication-module)

### Communications module RF120C

This section contains information on the following topics:

- [Communications module for Ident systems - RF18xC/RF18xCI](#communications-module-for-ident-systems---rf18xcrf18xci)
- [RF120C (V2.0 and higher)](#rf120c-v20-and-higher)
- [RF120C (up to V1.0)](#rf120c-up-to-v10)

#### Communications module for Ident systems - RF18xC/RF18xCI

The SIMATIC RF120C communication module is a module for the SIMATIC S7-1200 controllers. Up to three RF120C modules can be used as a central I/O device in a SIMATIC S7-1200.

The Ident instructions are available for easy programming of the communication modules.

One reader or one optical reader can be operated on an RF120C communication module via an RS232/RS422 interface. As an alternative, you can operate any serial device via the Freeport protocol.

#### RF120C (V2.0 and higher)

This section contains information on the following topics:

- ["Module parameters" parameter group](#module-parameters-parameter-group)
- ["Frame" parameter group](#frame-parameter-group)

##### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the communication module.

Parameters in the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User mode | Ident profile | Ident profile | Selection depends on the communications module and Ident system being used. With this parameter, you select the block:   - Ident profile    The program block for the Ident profile is used on the controller. |
| MOBY mode | RF200/RF300; MV400/MV500  Freeport  MV320  RF1000 | RF200/RF300; MV400/MV500 | With this parameter, you set the mode of the communication module. |
| Transmission  speed | 19.2 kBd  57.6 kBd  115.2 kBd | 115.2 kBd | Selection depends on the communications module and Ident system being used. Note that the value specified here is adopted automatically from the device configuration of the connected devices.  With this parameter, you set the data transmission speed between the communications module and reader.   When an RFID reader is connected: After changing the transmission speed, the reader must be turned off and on again (cycle power).   When an optical reader is connected: The transmission speed selected here must match the transmission speed selected in the firmware of the reader. |
| Diagnostic messages | None  Hard errors | Hard errors | With this parameter, you set whether hardware diagnostic messages will be reported.  - None:   Apart from standard diagnostics, no other alarms are generated. - Hard Errors:   Critical hardware errors/faults are reported by the S7 diagnostics. |
| Interface | RS422  RS232 | RS232 / RS422 | Selection of the interface type that the connected hardware (reader / optical readers) uses.  The default value depends on the interface used.  Note: This parameter is only shown when "MOBY Mode = Freeport" was selected. |

##### "Frame" parameter group

In this parameter group, you can configure all parameters specific to the "Freeport". This parameter group is only displayed when you have selected the value "Freeport" in the "MOBY Mode" parameter.

Parameters in the "Frame" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Data bits | 7  8 | 8 | Selection of the number of bits on which a character is represented. |
| Parity | None  Odd  Even | None | Parity selection  A sequence of data bits can be expanded by a parity bit. With its value "0" or "1", the parity bit is added to the sum of all bits (data bits and parity bits) to form a defined status. This increases data reliability.   - None:    Data is sent without a parity bit. - Odd:    The parity bit is set so that the sum of the data bits (including the parity bit) is odd when the signal state is "1". - Even:    The parity bit is set so that the sum of the data bits (including the parity bit) is even when the signal state is "1". |
| Stop bits | 1  2 | 1 | Selection of the number of stop bits that indicate the end of a character.   The stop bits are appended to every transferred character during transmission. |
| Specifying end detection | After character delay time elapses  On receipt of fixed number of characters  On receipt of the end delimiter(s) | After character delay time elapses | Specifies the end detection of a received frame:   - After character delay time elapses:    The frame has neither a fixed length nor defined end delimiters. The end of a frame is indicated by a gap in the character sequence. The size of this gap is specified by the character delay time. - On receipt of fixed number of characters:    The length of the received frames is always the same. When data is received, the end of the frame is recognized when the set number of characters has been received. - On receipt of the end delimiter(s):    At the end of the frame, there are one or two defined end delimiters. When data is received, the end of the frame is recognized when the configured end delimiter(s) is/are received. |
| No. of end delimiters | 1  2 | 1 | Selection of the number of end delimiters.   A maximum of two end delimiters can be configured. When data is received, the end of the frame is recognized when the selected end delimiter combination is received. |
| 1st end delimiter | 0...255 | 3 | Entry of the first end delimiter of a maximum of two end delimiters for the end criteria "On receipt of the end delimiter(s)". The selected end delimiter or the selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| 2nd end delimiter | 0...255 | 0 | Entry of the second end delimiter of a maximum of two end delimiters for the end criteria "On receipt of the end delimiter(s)". The selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| Frame length | 1...233 / 1...229 | 233 | Entry of the frame length in bytes for the end criterion "On receipt of fixed number of characters". |
| Character delay time | 0...65535 | 150 | Entry of the time [ms] that can elapse until a frame end is recognized. Select the character delay time dependent on the sending behavior of your communication partner. Depending on the data transmission speed the character delay time is limited to a minimum value.  Note that the ASCII driver also pauses between two frames during transmission. |

#### RF120C (up to V1.0)

This section contains information on the following topics:

- ["Reader" parameter group](#reader-parameter-group)
- [Parameter group "Ident device / system"](#parameter-group-ident-device-system)
- ["Reader type" parameter group](#reader-type-parameter-group)

##### "Reader" parameter group

In this parameter group, you can configure all reader-specific parameters of the RF120C.

Parameters of the parameter group "Readers"

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Diagnostics messages | None  Hard errors | Hard errors | With this parameter, you set whether hardware diagnostics messages will be reported.  - None:   Apart from standard diagnostics, no other alarms are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. |
| User mode | Ident profile | Ident profile | Selection depends on the communications module and Ident system being used. With this parameter, you select the block:   - Ident profile    The program block for the Ident profile is used on the controller. |
| Ident device / system | RF200 general  RF290R  RF300 general  RF380R  RF600  SLG D10S  SLG D11S/D12S  MOBY U  General Reader  Parameters via FB / optical readers | RF300 general | Selection of the connected Ident device / system. Depending on the selection you make, the "Ident system" parameter group is adapted. |

##### Parameter group "Ident device / system"

Depending on the set Ident device / system in the "Reader" parameter group, you can configure the following parameters.

Overview of the parameters I

| Ident device / system | Transfer speed | Presence check | Reset ERR LED | HF power | Max. number of transponders | Transponder type | Reader type | Frame |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RF200 general | ✓ | ✓ | ✓ | - | ✓ | ✓ | - | - |
| RF290R | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - |
| RF300 general | ✓ | ✓ | ✓ | - | ✓ | ✓ | - | - |
| RF380R | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - |
| RF600 | ✓ | ✓ | ✓ | - | ✓ | - | ✓ | - |
| SLG D10S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - |
| SLG D11S/D12S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - |

Overview of the parameters II

| Ident device / system | Transmission speed | MOBY mode | Standby time | Presence check | Reset ERR LED | Distance limitation | BERO mode | BERO time | Byte sequence of the reset parameter [hex] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MOBY U | ✓ | - | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| General reader | ✓ | - | - | - | - | - | - | - | ✓ |
| Parameters via FB / optical readers | ✓ | ✓ | - | - | - | - | - | - | - |

###### "Ident device / system" parameter group

Depending on the set basic parameters, you can configure all specific parameters for the selected Ident device/system in this parameter group.

Parameters of the "Ident device / system" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Transmission  speed | 19.2 kBd  57.6 kBd  115.2 kBd | 115.2 kBd | Selection depends on the communications module and Ident system being used. Note that the value specified here is adopted automatically from the device configuration of the connected devices.  With this parameter, you set the data transmission speed between the communications module and reader.   When an RFID reader is connected: After changing the transmission speed, the reader must be turned off and on again (cycle power).   When an optical reader is connected: The transmission speed selected here must match the transmission speed selected in the firmware of the reader. |
| MOBY mode | RF200/RF300/RF600; MV400/MV500; MOBY U/D | RF200/RF300/RF600; MV400/MV500; MOBY U/D | With this parameter, you set the mode of the communications module. |
| Standby time | 0 - 1400 ms | 0 ms | Standby time (scanning_time) for the transponder.  If the transponder receives a further command before the standby time has expired, this command can be executed immediately. If the transponder receives a command after the standby time has expired, command execution is delayed by the "sleep_time" of the transponder. |
| Presence check | On  Off (RF field on)  Off (RF field off) | On | On = As soon as there is a transponder in the antenna field of the reader, its presence is reported.  Off (RF field on ) = the presence check in the FB is suppressed. The antenna on the reader is nevertheless turned on as long as it has not been turned off by a command.  Off (RF field off) = the antenna is turned on only when a command is sent and it then turns itself off again. |
| Reset ERR LED | On  Off | On | On = the flashing of the error LED on the communications module is reset by each FB reset.   Off = the error LED always indicates the last error. The display can only be reset by turning off the communications module. |
| RF power <sup>1)</sup> | 0.50 ... 5.00 | 1.00  1.25 | Setting for the output power of the reader.  The selectable values depend on the connected device. |
| Distance limitation | 0.2 m  0.5 m  1.0 m  1.5 m  2.0 m  2.5 m  3.0 m  3.5 m | 1.5 m | Limitation of the radiation range |
| Max. no. of transponders | 1 ... 40 | 1 | Number of transponders expected in the antenna field.  The selection depends on the connected device. |
| Transponder type | <sup>1)</sup> | <sup>1)</sup> | Selection of the transponder types used. The selection depends on the connected device. |
| Reader type <sup>1)</sup> | RF620R ETSI  RF620R FCC  RF620R CMIIT  RF630R ETSI  RF630R FCC  RF630R CMIIT | RF620R ETSI | Selection of the reader used.  Selecting a reader opens the "Reader type" parameter group. The parameters are described in the table below. |
| BERO mode | Without BEROs  1 or 2 BEROs  1st BERO on, 2nd BERO off  Synchronization due to cable connection | Without BEROs | - Without BEROs   No reader synchronization - 1 or 2 BEROs   The BEROs are ORed. The antenna field is turned on during the actuation of a BERO. - 1st BERO on, 2nd BERO off   The 1st BERO turns the antenna field on and the 2nd BERO turns the antenna field off. If there are two BEROs present and "BERO time in s" is set, the antenna field is turned off automatically if the 2nd BERO does not switch within this BERO time. If no "BERO time in s" is set, the antenna field remains turned on until the 2nd BERO is activated. - Synchronization due to cable connection    Activate reader synchronization via cable connection (see manual for configuring, mounting and service for MOBY U). |
| BERO time | 0 ... 255 s | 0 s | Can only be set if the BERO mode is set to "1st BERO on, 2nd BERO off".  - 0   Timeout monitoring is deactivated. The 2nd BERO is needed in order to switch the field off. - 1 ... 255 s   Activation time for the reader field |
| Byte sequence of the reset parameter [hex] | <sup>1)</sup> | <sup>1)</sup> | Hexadecimal representation of the byte sequence of the reset parameter of the reader. |
| <sup>1)</sup> You can find a detailed description of this parameter in the following paragraphs. |  |  |  |

**The "RF power" parameter**

The selectable values depend on the value specified in the parameter "Ident device / system".

- RF290R

  - Value range: 0.50 ... 5.00 W
  - Default value: 1.00 W
- RF380R

  - Value range: 0.50 ... 2.00 W
  - Default value: 1.25 W

**The "Transponder type" parameter**

Selection of the transponders used. The selection depends on the value specified in the parameter "Ident device / system". The following transponder types can be selected:

"Transponder type" selection option

| "Ident device / system" parameter | Possible values |
| --- | --- |
| RF200 general  RF290R | ISO 15693 |
| RF300 general  RF380R | RF300  ISO 15693 |
| SLG D10S  SLG D11S/D12S | I code  ISO 15693  ISO-FRAM |

**The parameter "Byte sequence of the reset parameter [hex]"**

With this function, you can specify the Reset parameters in hexadecimal format. This setting is intended only for trained users.

The following Reset parameters are available:

Reset parameters

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Byte** | 1 | 2...5 | 6 | 7...8 | 9 | 10 | 11 | 12 | 13...14 | 15 | 16 |
| **Value** | 0x04 | 0x00 | 0x0A | 0x00 | scanning_ time | param | option_1 | distance_ limiting | multitag | field_on_ control | field_on_ time |

##### "Reader type" parameter group

In this parameter group, you can configure all parameters specific to the "Reader type". This parameter group is only displayed when you have selected the value "RF620R/RF630R" in the "Ident device / system" parameter.

Parameters of the "Reader type" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Wireless profile | -- | -- | Selection of the relevant wireless profile for ETSI, FCC or CMIIT. |
| Multitag mode | UID = EPC-ID  (8 bytes)  UID = Handle-ID  (4 bytes)  UID = 0 (single tag) | UID = EPC-ID  (8 bytes) | - UID = EPC-ID (8 bytes)    8-byte UID of bytes 5-12 of 12-byte long EPC ID - UID = Handle-ID (4 bytes)   4-byte UID as handle ID for accessing the transponder with EPC ID of any length |
| Intelligent Single Tag Mode (ISTM) | On  Off | Off | Enabling/disabling the "Intelligent Single Tag Mode ISTM" algorithm <sup>1)</sup> |
| Black list | On  Off | Off | Enabling/disabling the "Black list" <sup>1)</sup> |
| Radiated power internal antenna (RF620R) | 0 ... B | 4 | Setting the radiated power for the internal antenna <sup>1) 2)</sup> |
| Internal antenna (RF620R) | -- | -- | Enabling/disabling the internal antenna.   For the RF620R, you can use the internal or external antenna. |
| Transmit power external antenna connector (RF620R) | 0 ... 9 | 4 | Setting the transmit power for the external antenna <sup>1) 2)</sup> |
| External antenna (SetAnt required) (RF620R) | -- | -- | Activation/deactivation of the external antenna.   For the RF620R, you can use the internal or external antenna. |
| Transmit power ANT 1 (RF630R) | 0 ... 9 | 4 | Setting the transmit power for antenna 1<sup>1) 2)</sup> |
| Transmit power ANT 2 (RF630R) | 0 ... 9 | 4 | Setting the transmit power for antenna 2<sup>1) 2)</sup> |
| Communication speed | Reliable detection  Fast detection | Reliable detection | <sup>1)</sup> |
| Tag hold | On  Off | Off | Enabling/disabling the "Tag hold" <sup>1)</sup> |
| Scanning mode | On  Off | Off | Enabling/disabling the "Scanning mode" <sup>1)</sup> |
| Channel assignment (only with wireless profile ETSI) | -- | -- | Selection of the wireless channels to be used <sup>1)</sup> |
| <sup>1)</sup> You can find additional information in the "RF620R/RF630R" configuration manual.   <sup>2)</sup> The values for the transmit/radiated power of the antennas can be found in the following table. |  |  |  |

The RF620R/RF630R configuration manual is available under the following link: [Configuration manual RF620R/RF630R](https://support.industry.siemens.com/cs/ww/en/view/33287195)

Transmit/radiated power of the antennas

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Hex value | RF630R transmit power | RF620R radiated power (internal antenna) |  |  | RF620R transmit power |
| dBm / (mW) | ETSI  dBm / (mW) ERP | FCC  dBm / (mW) EIRP | CMIIT  dBm / (mW) ERP | dBm / (mW) |  |
| 0  1  ...  4  ...  9  A  B (...F) | 18 / (65)  19 / (80)  ...  22 / (160)  ...  27 / (500)  27 / (500)  27 / (500) | 18 / (65)  19 / (80)  ...  22 / (160)  ...  27 / (500)  28 / (630)  29 / (795) | 20 / (100)  21 / (125)  ...  24 / (250)  ...  29 / (795)  30 / (1000)  31 / (1260) | 18 / (65)  19 / (80)  ...  22 / (160)  ...  27 / (500)  28 / (630)  29 / (795) | 18 / 65)  19 / (80)  ...  22 / (160)  ...  27 / (500)  27 / (500)  27 / (500) |

### Communications module RF170C

This section contains information on the following topics:

- [Communications module for Ident systems - RF170C, RS422/RS232](#communications-module-for-ident-systems---rf170c-rs422rs232)
- ["Module parameters" parameter group](#module-parameters-parameter-group-1)
- ["Message Frame" parameter group](#message-frame-parameter-group)
- ["I/O addresses" parameter group](#io-addresses-parameter-group)

#### Communications module for Ident systems - RF170C, RS422/RS232

The module RF170C RS422/RS232 is a communications module for Ident systems for the I/O system ET 200pro. Several RF170C RS422/RS232 communications modules can be mounted and operated on an IM 154-8 CPU and on an interface module IM 154-1 DP, IM 154-2 DP High Feature or IM 154-4 PN High Feature of the ET 200pro.

A maximum of two readers can be connected to the RF170C RS422/RS232. The connected readers are processed at the same time

The function blocks FB 45, FC 45 and the program block for the Ident profile/RFID standard profile allow simple programming using the SIMATIC S7 tools. The function blocks FB 45, FC 45 and the program block for the Ident profile/RFID standard profile can be operated both on the S7-300 and the S7-400. For the S7-1200 and S7-1500 controllers, the Ident profile must be used.

The transponder data is accessed by means of normal addressing or file handler addressing.

##### Physical addressing of the transponder

Physical addressing of a transponder is also referred to as normal addressing. When using normal addressing you can set up the data structure of a transponder yourself You decide which physical address which data is written to. The addressing of the transponder memory generally begins at the address 0x0000 hex and ends at an end address that corresponds to the size of the transponder memory.

##### File handler addressing of the transponder

With file handler addressing you specify a file name for access to the data. The file name consists of eight ASCII characters. The file handler manages the user data on the transponder independently. You do not need to configure any data structures on the transponder.

#### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the RF170C RS422/RS232.

Parameters in the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User Mode | Ident profile/RFID standard profile  FB 45 / FC 45  FB 55 / FC 55 | Ident profile/RFID standard profile | Selection depends on the communications module and Ident system being used. With this parameter, you select the block:   - Ident profile/RFID standard profile:    The program block for the Ident profile/RFID standard profile is used on the controller. - FB 45 / FC 45:    Single tag mode FB 45 (PROFIBUS/PROFINET) or FC 45 (PROFIBUS) is used on the controller. - FB 55 / FC 55:    Multitag mode. FB 55 (PROFIBUS/PROFINET) or FC 55 (PROFIBUS) is used on the controller. |
| MOBY Mode | RF200/RF300/RF600; MV400/MV500; MOBY U/D  MOBY I/E  MV300  Freeport protocol  RF300 filehandler | RF200/RF300/RF600; MV400/MV500; MOBY U/D | Selection depends on the communications module and Ident system being used. With this parameter, you set the mode of the communications module.  - RF200/RF300/RF600; MV400/MV500; MOBY U/D - MOBY I/E - MV300 - Freeport protocol - RF300 filehandler   Normal addressing: The transponder is addressed with physical addresses. |
| Transmission  speed | 19.2 kBd  57.6 kBd  115.2 kBd | 115.2 kBd | Selection depends on the communications module and Ident system being used. With this parameter, you set the transmission speed between the communications module and reader.   When the RFID reader is connected: After changing the transmission speed, the reader must be turned off and on again.   With a connected optical reader: The transmission speed selected here must match the transmission speed selected in the firmware of the reader. |
| Diagnostics messages | None  Hard errors | None | Selection depends on the communications module and Ident system being used. With this parameter, you set whether hardware diagnostics messages will be reported.  - None:   Apart from standard diagnostics, no other alarms are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. |
| Suppression of  Error LED | None  Channel 1  Channel 2 | None | Disabling the Error LED (ERR) of a channel.   The communications module has two channels to which the readers / optical readers can be connected. The Error LED of the other channel flashes permanently when only one of the channels is being used. With the help of the suppression, you can disable the Error LED of the unused channel. |
| Interface | RS-232  RS-422 | -- | Selection of the interface type that the connected hardware (reader / optical reader) uses. |

#### "Message Frame" parameter group

The "Frame" parameter group is only displayed when you have selected the parameter value "Freeport protocol" in the "MOBY Mode" parameter of the module parameters. In this parameter group, you can configure all parameters specific to the "Freeport protocol".

Parameters in the "Frame" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Data bits | 7  8 | 8 | Selection of the number of bits on which a character is represented. |
| Parity | None  Odd  Even  Fixed value 1  Fixed value 0 | None | Parity selection  A sequence of data bits can be expanded by a parity bit. With its value "0" or "1", the parity bit is added to the sum of all bits (data bits and parity bits) to form a defined status. This increases data reliability.   - None:    Data is sent without a parity bit. - Odd:    The parity bit is set so that the sum of the data bits (including the parity bit) is odd when the signal state is "1". - Even:    The parity bit is set so that the sum of the data bits (including the parity bit) is even when the signal state is "1". - Fixed value 1:    The parity bit is set permanently to the value "1". - Fixed value 0:    The parity bit is set permanently to the value "0". |
| Stop bits | 1  2 | 1 | Selection of the number of stop bits that indicate the end of a character.   The stop bits are appended to every transferred character during transmission. |
| Specifying end detection | After character delay time elapses  On receipt of fixed number of characters  On receipt of the end delimiter(s): | After character delay time elapses | Specifies the end detection of a received frame.   - After character delay time elapses:    The frame has neither a fixed length nor defined end delimiters. The end of a frame is indicated by a gap in the character sequence. The size of this gap is specified by the character delay time. - On receipt of fixed number of characters:    The length of the received frame is always the same. When data is received, the end of the frame is recognized when the set number of characters has been received. - On receipt of the end delimiter(s):    At the end of the frame there are one or two defined end delimiters. When data is received, the end of the frame is recognized when the configured end delimiter(s) is/are received. |
| No. of end delimiters | 1  2 | 1 | Selection of the number of end delimiters.   A maximum of 2 end delimiters can be configured. When data is received, the end of the frame is recognized when the selected end delimiter combination is received. |
| 1st end delimiter | 0...7F / 0...FF | 3 | Entry of the 1st end delimiter of maximum two end delimiters for end criteria "On receipt of the end delimiter(s)". The selected end delimiter or the selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| 2nd end delimiter | 0...7F / 0...FF | 0 | Entry of the 2nd end delimiter of maximum two end delimiters for end criteria "On receipt of the end delimiter(s)". The selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| Frame length | 1...233 / 1...229 | 233 | Entry of the frame length in bytes for the end criterion "On receipt of fixed number of characters". |
| Character delay time | 0...65535 | 15 | Entry of the time [ms] that can elapse until a frame end is recognized. Select the character delay time dependent on the send behavior of your communications partner. Depending on the data transmission speed the character delay time is limited to a minimum value.  Note that the ASCII driver pauses between two message frames when sending. |

#### "I/O addresses" parameter group

##### Inputs

1. Assign a start address to the module.
2. If you want to assign the address area to a process image partition, select the desired process image partition in the "Process image" drop-down list.

##### Outputs

1. Assign a start address to the module.
2. If you want to assign the address area to a process image partition, select the desired process image partition in the "Process image" drop-down list.

> **Note**
>
> Input and output address must be identical.

### RF180C communications module

This section contains information on the following topics:

- [Communications module for Ident systems - RF180C](#communications-module-for-ident-systems---rf180c)
- ["Module parameters" parameter group](#module-parameters-parameter-group-2)

#### Communications module for Ident systems - RF180C

The module RF180C is a communications module for Ident systems for PROFINET IO.

A maximum of two readers can be connected to the RF180C. The connected readers are processed at the same time

The function blocks FB 45, FB 55, and the program block for the RFID standard profile allow simple programming using the SIMATIC S7 tools. The function blocks FB 45, FB 55,and the program block for the RFID standard profile can be operated both on the S7-300 and the S7-400.

The transponder data is accessed by means of normal addressing or file handler addressing.

##### Physical addressing of the transponder

Physical addressing of a transponder is also referred to as normal addressing. When using normal addressing you can set up the data structure of a transponder yourself You decide which physical address which data is written to. The addressing of the transponder memory generally begins at the address 0x0000 hex and ends at an end address that corresponds to the size of the transponder memory.

##### File handler addressing of the transponder

With file handler addressing you specify a file name for access to the data. The file name consists of eight ASCII characters. The file handler manages the user data on the transponder independently. You do not need to configure any data structures on the transponder.

#### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the RF180C.

Parameters in the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User Mode | FB 45  FB 55  FB 56  RFID standard profile | FB 45 | Selection depends on the communications module and and Ident system being used. With this parameter, you select the block:   - FB 45:    Single tag mode FB 45 (PROFIBUS/PROFINET) is used on the controller. - FB 55:    Multitag mode. FB 55 (PROFIBUS/PROFINET) is used on the controller. - FB 56:   Multitag mode. FB 56 (PROFIBUS/PROFINET) is used on the controller. - RFID standard profile    The program block for the RFID standard profile is used on the controller. |
| MOBY Mode | MOBY I/E normal addressing  MOBY I file handler  RF200/RF300/RF600; MOBY U/D normal adr.  MOBY U file handler  RF300 filehandler | RF200/RF300/RF600; MOBY U/D normal addr. | Selection depends on the communications module and and Ident system being used. With this parameter, you set the mode of the communications module.  - MOBY I/E normal addressing - MOBY I file handler - RF200/RF300/RF600; MOBY U/D normal adr. - MOBY U file handler - RF300 filehandler   Normal addressing: The transponder is addressed with physical addresses.   Filehandler: Prior to use, the transponder needs to be formatted. |
| Transmission  speed | 19.2 kBd  57.6 kBd  115.2 kBd | 115.2 kBd | Selection depends on the communications module and and Ident system being used. With this parameter, you set the transmission speed between the communications module and reader.   When the RFID reader is connected: After changing the transmission speed, the reader must be turned off and on again.   With a connected optical reader: The transmission speed selected here must match the transmission speed selected in the firmware of the reader. |
| Diagnostics messages | None  Hard errors  Hard/Soft Errors | None | With this parameter, you set whether hardware diagnostics messages will be reported.  - None:   Apart from standard diagnostics, no other alarms are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. - Hard/Soft Errors:   Critical hardware faults and errors occurring when processing commands are reported by the S7 diagnostics. |
| Suppression of  Error LED | None  Channel 1  Channel 2 | None | Disabling the Error LED (ERR) of a channel.   The communications module has two channels to which the readers / optical readers can be connected. The Error LED of the other channel flashes permanently when only one of the channels is being used. With the help of the suppression, you can disable the Error LED of the unused channel. |

### ASM 456 communications module

This section contains information on the following topics:

- [Communications module for Ident systems - ASM 456](#communications-module-for-ident-systems---asm-456)
- ["Device-specific parameters" parameter group.](#device-specific-parameters-parameter-group)

#### Communications module for Ident systems - ASM 456

The ASM 456 module is a communications module for Ident systems for PROFIBUS DP V1.

A maximum of two readers can be connected to the ASM 456. The connected readers are processed at the same time

The function blocks FB 45, FC 45, FB 55, FC 55, FC 56 and the program block for the Ident profile/RFID standard profile allow simple programming using the SIMATIC S7 tools. The function blocks FB 45, FC 45, FB 55, FC 55, FC 56 and the program block for the Ident profile/RFID standard profile can be operated both on the S7-300 and the S7-400. For the S7-1200 and S7-1500 the Ident profile must be used.

The transponder data is accessed by means of normal addressing or file handler addressing.

##### Physical addressing of the transponder

Physical addressing of a transponder is also referred to as normal addressing. When using normal addressing you can set up the data structure of a transponder yourself You decide which physical address which data is written to. The addressing of the transponder memory generally begins at the address 0x0000 hex and ends at an end address that corresponds to the size of the transponder memory.

##### File handler addressing of the transponder

With file handler addressing you specify a file name for access to the data. The file name consists of eight ASCII characters. The file handler manages the user data on the transponder independently. You do not need to configure any data structures on the transponder.

#### "Device-specific parameters" parameter group.

In this parameter group, you can configure all module-specific parameters of the ASM 456.

Parameters in the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User Mode | Ident profile/RFID standard profile  FB 45 / FC 45  FB 55 / FC 55  FC 56 | Ident profile/RFID standard profile | Selection depends on the communications module and and Ident system being used. With this parameter, you select the block:   - Ident profile/RFID standard profile:    The program block for the Ident profile/RFID standard profile is used on the controller. - FB 45 / FC 45:    Single tag mode FB 45 (PROFIBUS/PROFINET) or FC 45 (PROFIBUS) is used on the controller. - FB 55 / FC 55:    Multitag mode. FB 55 (PROFIBUS/PROFINET) or FC 55 (PROFIBUS) is used on the controller. - FC 56   File handler for S7-300 and S7-400 |
| MOBY Mode | RF200/RF300/RF600; MV400/MV500; MOBY U/D  RF680R/RF685R  MOBY I/E normal addressing  RF300 filehandler  MOBY U file handler  MOBY I File handler | RF200/RF300/RF600; MV400/MV500; MOBY U/D | Selection depends on the communications module and and Ident system being used. With this parameter, you set the mode of the communications module.  - RF200/RF300/RF600; MV400/MV500; MOBY U/D - RF680R/RF685R - MOBY I/E normal addressing - RF300 filehandler - MOBY U file handler - MOBY I file handler   Normal addressing: The transponder is addressed with physical addresses.   Filehandler: Prior to use, the transponder needs to be formatted. |
| Transmission  speed | 19.2 kBd  57.6 kBd  115.2 kBd | 115.2 kBd | Selection depends on the communications module and and Ident system being used. With this parameter, you set the transmission speed between the communications module and reader.   When the RFID reader is connected: After changing the transmission speed, the reader must be turned off and on again.   With a connected optical reader: The transmission speed selected here must match the transmission speed selected in the firmware of the reader. |
| Diagnostics messages | None  Hard errors  Hard/soft errors low priority  Hard/soft errors high priority | None | Selection depends on the communications module and and Ident system being used. With this parameter, you set whether hardware diagnostics messages will be reported.  - None:   Apart from standard diagnostics, no other alarms are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. - Hard/soft errors low priority   Critical hardware errors and errors that occur during command processing are reported by the S7 diagnostics. The "Ext_Diag" bit is not set. - Hard/soft errors high priority   Critical hardware errors and errors that occur during command processing are reported by the S7 diagnostics. The "Ext_Diag" bit is set. |
| Suppression of  Error LED | None  Channel 1  Channel 2 | None | Disabling the Error LED (ERR) of a channel.   The communications module has two channels to which the readers / optical readers can be connected. The Error LED of the other channel flashes permanently when only one of the channels is being used. With the help of the suppression, you can disable the Error LED of the unused channel. |

### ASM 475 communications module

This section contains information on the following topics:

- [What you should know about the ASM 475](#what-you-should-know-about-the-asm-475)

#### What you should know about the ASM 475

##### Introduction

Up to eight ASM 475 interface modules can be plugged in and operated in a rack of the SIMATIC S7-300. If you have a configuration with several racks (max. four racks), the ASM 475 can be plugged in and operated in each rack. This means that with the maximum configuration of a SIMATIC S7-300, 32 ASM 475 modules can be operated.

A maximum of two SLGs (write/read devices) can be connected to the ASM 475. The processing of the connected SLGs is parallel. FC45 allows simple programming using the SIMATIC S7 tools.

FC45 can be used both in the S7-300 and S7-400.

With S7-400, the ASM 475 is connected via an ET 200M.

Note that the

- IM 153-1 must have at least order number 6ES7 153-1AA03-0XB0 or 6ES7 153-1AA83-0XB0 and
- IM 153-2 at least order number 6ES7 153-2AA02-0XB0 or 6ES7 153-2AB01-0XB0.

Access to the MDS data is with normal addressing.

##### Physical addressing of the MDS (mobile data storage)

The physical addressing of an MDS is also known as **normal addressing**. Users set up the structure of the MDS themselves. They know the physical MDS address to which data is written. The addressing of the MDS storage generally begins at 0000 hex and ends at an end address corresponding to the size of the MDS storage.

##### File handler addressing of the MDS

For file handler addressing, the user specifies a file name for access to the data. The file name consists of eight ASCII characters. The file handler manages the user data independently on the MDS. The user does not need to configure data structures on the MDS.

Prior to use, the MDS needs to be formatted.

### RF166C communications module

This section contains information on the following topics:

- [Communications module for Ident systems - RF166C](#communications-module-for-ident-systems---rf166c)
- ["Web Based Management" parameter group](#web-based-management-parameter-group)
- [Parameter group "Module parameters" of the submodules](#parameter-group-module-parameters-of-the-submodules)

#### Communications module for Ident systems - RF166C

The SIMATIC RF166C communications modules are designed for use in all areas of automation. The RF166C module is a communications module for Ident systems for PROFIBUS DP. In addition, the communications module has an Ethernet interface for service purposes and OPC UA communication. Depending on the device type, 1 or 2 readers can be connected to the communications module. The connected readers are processed at the same time

The function block FB 45 and the program block for the Ident profile/RFID standard profile allow simple programming using the SIMATIC S7 tools. The function block FB 45 and the program block for the Ident profile/RFID standard profile can be operated both on the S7-300 and the S7-400. For the S7-1200 and S7-1500 the Ident profile must be used.

The transponder data is accessed by means of normal addressing.

##### Physical addressing of the transponder

Physical addressing of a transponder is also referred to as normal addressing. When using normal addressing you can set up the data structure of a transponder yourself. You decide which physical address which data is written to. The addressing of the transponder memory generally begins at the address "0x0000" and ends at an end address that corresponds to the size of the transponder memory -1.

#### "Web Based Management" parameter group

In this parameter group you can start the Web Based Management.

Parameters in the "Web-based management" parameter group

| Parameter | Description |
| --- | --- |
| IP address | Enter the IP address of the communications module in this input box. This is required to start the Web Based Management of the communications module. |
| Web Based Management | Start Web Based Management of the communications module.  Web Based Management (WBM) offers extensive functions for configuring the communications module.  Requirement: The communications module is connected to a PC/PG via the Ethernet interface. Note that WBM can only be started when the IP address stored in the project has been assigned to the communications module. This means that the TIA configuration must be loaded into the SIMATIC controller. |

#### Parameter group "Module parameters" of the submodules

In this parameter group, you can configure all module-specific parameters of the connected reader. Note that some of the following parameters are module-specific. For some module types, not all parameters are displayed.

Depending on the Ident device that is connected to the respective interface (X21-X22), you must use the matching submodule:

- Freeport: Submodule for connecting SIMATIC RF1000, MV32x and other serial devices.
- Reader: Submodule for connecting the SIMATIC RF200 and RF300 readers, as well as the SIMATIC MV400 and MV500 optical readers
- RF300 fast protocol: Submodule for connecting the SIMATIC RF300 readers (2nd generation, as of FW 1.8)
- RF600: Submodule for connecting the SIMATIC RF600 readers
- Empty: If no device is connected to interface X21, you need to assign an "Empty" submodule to this interface.

With the "Communication" submodule, configurations can be transferred from or to the communications module, and a status query can be performed via the communications module.

Parameters of the parameter group "Module parameters" of the submodules

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User mode | Ident profile / RFID standard profile  FB 45 | Ident profile / RFID standard profile | With this parameter, you select the block:   - Ident profile/RFID standard profile:    Single tag / multitag operation. The program block for the Ident profile is used on the controller. - FB 45:    Single tag mode FB 45 is used in the controller. |
| MOBY mode | RF200/RF300/RF600; MV400/MV500; MOBY U/D normal addr. | RF200/RF300/RF600; MV400/MV500; MOBY U/D normal addr. | With this parameter, you set the mode of the communications module.  - RF200/RF300/RF600; MV400/MV500; MOBY U/D normal addr.   Normal addressing: The transponder is addressed with physical addresses. |
| Transmission speed | 19.2 kBd  57.6 kBd  115.2 kBd  921.6 kBd | 115.2 kBd / 921.6 kBd | Selection depends on the Ident system being used. With this parameter, you set the transmission speed between the communications module and reader.   When an optical reader is connected: The transmission speed selected here must match the transmission speed selected for the reader. |
| Diagnostics messages | None  Hard errors  Hard/soft errors | None | With this parameter, you determine the extent to which the reader-related diagnostic interrupt messages are to be reported.  - None:   No further interrupts are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. - Hard/soft errors:   Critical hardware errors and errors that occur during command processing are reported by the S7 diagnostics. |

**Parameters of the parameter group "Module parameters &gt; Frame" of the submodules (connected readers)**

This parameter group is displayed when you have selected the "Freeport" submodule. In this parameter group, you can configure all parameters specific to the "Freeport".

Parameters of the parameter group "Module parameters &gt; Message frame" of the submodules

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Parity | None  Odd  Even  Fixed value 1  Fixed value 0 | None | Parity selection  A sequence of data bits can be expanded by a parity bit. With its value "0" or "1", the parity bit is added to the sum of all bits (data bits and parity bits) to form a defined status. This increases data reliability.   - None:    Data is sent without a parity bit. - Odd:    The parity bit is set so that the sum of the data bits (including the parity bit) is odd when the signal state is "1". - Even:    The parity bit is set so that the sum of the data bits (including the parity bit) is even when the signal state is "1". - Fixed value 1:    The parity bit is set permanently to the value "1". - Fixed value 0:    The parity bit is set permanently to the value "0". |
| Data bits | 7  8 | 8 | Selection of the number of bits on which a character is represented. |
| Stop bits | 1  2 | 1 | Selection of the number of stop bits that indicate the end of a character.   The stop bits are appended to every transferred character during transmission. |
| Interface | RS422  RS232 <sup>1)</sup> | RS422 | Selection of the interface type that the connected hardware (reader / optical reader) uses. |
| Specifying end detection | After character delay time elapses  On receipt of fixed number of characters  On receipt of the end delimiter(s): | After character delay time elapses | Specifies the end detection of a received frame.   - After character delay time elapses:    The frame has neither a fixed length nor defined end delimiters. The end of a frame is indicated by a gap in the character sequence. The size of this gap is specified by the character delay time. - On receipt of fixed number of characters:    The length of the received frame is always the same. When data is received, the end of the frame is recognized when the set number of characters has been received. - On receipt of the end delimiter(s):    At the end of the frame there are one or two defined end delimiters. When data is received, the end of the frame is recognized when the configured end delimiter is received. |
| No. of end delimiters | 1  2 | 1 | Selection of the number of end delimiters.   A maximum of 2 end delimiters can be configured. When data is received, the end of the frame is recognized when the selected end delimiter combination is received. |
| 1st end delimiter | 0...255 | 3 | Entry of the first end delimiter of a maximum of two end delimiters for the end criteria "On receipt of the end delimiter(s)". The selected end delimiter or the selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| 2nd end delimiter | 0...255 | 0 | Entry of the second end delimiter of a maximum of two end delimiters for the end criteria "On receipt of the end delimiter(s)". The selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| Frame length | 1...233 / 1...229 | 233 | Entry of the frame length in bytes for the end criterion "On receipt of fixed number of characters". |
| Character delay time | 0...65535 | 15 | Entry of the time [ms] that can elapse until a frame end is recognized. Select the character delay time dependent on the send behavior of your communication partner. Depending on the data transmission speed the character delay time is limited to a minimum value.  Note that the ASCII driver also pauses between two telegrams during transmission. |
| <sup>1)</sup> Only in connection with the reader interfaces X21 and X22. |  |  |  |

### RF18xC/RF18xCI communication module

This section contains information on the following topics:

- [Communications module for Ident systems - RF18xC/RF18xCI](#communications-module-for-ident-systems---rf18xcrf18xci-1)
- ["Web Based Management" parameter group](#web-based-management-parameter-group-1)
- ["Configuration management" parameter group](#configuration-management-parameter-group)
- ["Module parameters" parameter group](#module-parameters-parameter-group-3)
- [Parameter group "Module parameters" of the submodules](#parameter-group-module-parameters-of-the-submodules-1)

#### Communications module for Ident systems - RF18xC/RF18xCI

The SIMATIC RF185C, RF186C, RF188C, RF186CI and RF188CI communications modules are designed for use in all areas of automation. The RF18xC/RF18xCI module is a communications module for Ident systems for PROFINET IO and OPC UA. Depending in the device type, 1, 2 or 4 readers can be connected to the communication module. The connected readers are processed at the same time The RF18xCI communications modules have an additional I/O interface over which up to 8 inputs or outputs can be connected.

The function block FB 45 and the program block for the Ident profile/RFID standard profile allow simple programming using the SIMATIC S7 tools. The function block FB 45 and the program block for the Ident profile/RFID standard profile can be operated both on the S7-300 and the S7-400. For the S7-1200 and S7-1500 the Ident profile must be used.

The transponder data is accessed by means of normal addressing.

##### Physical addressing of the transponder

Physical addressing of a transponder is also referred to as normal addressing. When using normal addressing you can set up the data structure of a transponder yourself. You decide which physical address which data is written to. The addressing of the transponder memory generally begins at the address "0x0000" and ends at an end address that corresponds to the size of the transponder memory -1.

#### "Web Based Management" parameter group

In this parameter group you can start the Web Based Management.

Parameters in the "Web-based management" parameter group

| Parameter | Description |
| --- | --- |
| Web Based Management | Start Web Based Management of the communications module.  Web Based Management (WBM) offers extensive functions for configuring the communications module.  Note: WBM can only be started when the IP address stored in the project has been assigned to the communication module. This means that the device name has been assigned and the TIA configuration must be loaded on the SIMATIC controller. |

#### "Configuration management" parameter group

In this parameter group, you can load or save the configuration data.

Parameters of the "Configuration management" parameter group

| Parameter | Description |
| --- | --- |
| User name<sup> 1)</sup> | User name of a user created in the WBM of the communications module  Note that the user must have the required rights. |
| Password<sup> 1)</sup> | Input box for the password of the selected user |
| Load configuration to device | Load configuration data from the STEP 7 project into the communications module. |
| Save configuration in project | Save configuration data of the communications module in the current STEP 7 project. |
| <sup>1)</sup> User name and password must only be entered when the user management of the CM in the WBM is enabled. |  |

##### Requirements

The following requirements must be met to allow configuration data to be loaded or saved:

- The "PROFINET interface [X1]" parameter contains the correct IP address of the communications module.
- The entered user has the required rights to run the download/upload.
- Note that https is not supported with TIA Portal versions ≤ V17.

#### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the communications module.

Parameters of the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Diagnostic interrupt on the device | Off  On | Off | Switch the diagnostic messages of the communications module on/off. |

#### Parameter group "Module parameters" of the submodules

In this parameter group, you can configure all module-specific parameters of the connected reader. Note that some of the following parameters are module-specific. For some module types, not all parameters are displayed.

Depending on the Ident device that is connected to the respective interface (X21-X24), you must use the matching submodule.

- Freeport: Submodule for connecting SIMATIC RF1000, MV32x and other serial devices.
- RF300 fast protocol: Submodule for connecting the SIMATIC RF300 readers (2nd generation, as of FW 1.8)
- Reader: Submodule for connecting the SIMATIC RF200 and RF300 readers, as well as the SIMATIC MV400 and MV500 optical readers

With the "Communication" submodule, configurations can be transferred from or to the communications module, and a status query can be performed via the communications module.

Parameters of the parameter group "Module parameters &gt; General parameters" of the submodules

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User mode | Ident profile / RFID standard profile  FB 45 | Ident profile / RFID standard profile | With this parameter, you select the block:   - Ident profile/RFID standard profile:    Single tag / multitag operation. The program block for the Ident profile is used on the controller. - FB 45:    Single tag mode FB 45 is used in the controller. Only in connection with an S7-300 controller. |
| MOBY mode | RF200/RF300/RF600; MV400/MV500; MOBY U/D normal addr. | RF200/RF300/RF600; MV400/MV500; MOBY U/D normal addr. | With this parameter, you set the mode of the communications module.  - RF200/RF300/RF600; MV400/MV500; MOBY U/D normal addr.   Normal addressing: The transponder is addressed with physical addresses. |
| Transmission speed | 19.2 kBd  57.6 kBd  115.2 kBd  921 kBd | 115.2 kBd / 921 kBd | Selection depends on the Ident system being used. With this parameter, you set the transmission speed between the communications module and reader.   When an optical reader is connected: The transmission speed selected here must match the transmission speed selected for the reader. |
| Diagnostics messages | None  Hard errors  Hard/soft errors | None | With this parameter, you determine the extent to which the reader-related diagnostic interrupt messages are to be reported.  - None:   No further interrupts are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. - Hard/soft errors:   Critical hardware faults and errors occurring when processing commands are reported by the S7 diagnostics. |
| IO mode <sup>1)</sup> | Input  Output  IO-Link | Input | You use this parameter to specify the mode of the IO interface of the communication module:  - Input:    Single digital input - Output:    Single digital output - IO-Link:    Mode for connection of an IO-Link device with digital inputs/outputs. |
| <sup>1)</sup> This parameter is only included for RF18xCI communications modules. |  |  |  |

**Parameters of the parameter group "Module parameters &gt; Frame" of the submodules (connected readers)**

This parameter group is displayed when you have selected the "Freeport" submodule. In this parameter group, you can configure all parameters specific to the "Freeport".

Parameters of the parameter group "Module parameters &gt; Message frame" of the submodules

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Parity | None  Odd  Even  Fixed value 1  Fixed value 0 | None | Parity selection  A sequence of data bits can be expanded by a parity bit. With its value "0" or "1", the parity bit is added to the sum of all bits (data bits and parity bits) to form a defined status. This increases data reliability.   - None:    Data is sent without a parity bit. - Odd:    The parity bit is set so that the sum of the data bits (including the parity bit) is odd when the signal state is "1". - Even:    The parity bit is set so that the sum of the data bits (including the parity bit) is even when the signal state is "1". - Fixed value 1:    The parity bit is set permanently to the value "1". - Fixed value 0:    The parity bit is set permanently to the value "0". |
| Data bits | 7  8 | 8 | Selection of the number of bits on which a character is represented. |
| Stop bits | 1  2 | 1 | Selection of the number of stop bits that indicate the end of a character.   The stop bits are appended to every transferred character during transmission. |
| Interface | RS422  RS232 <sup>1)</sup> | RS422 | Selection of the interface type that the connected hardware (reader / optical reader) uses. |
| Specifying end detection | After character delay time elapses  On receipt of fixed number of characters  On receipt of the end delimiter(s): | After character delay time elapses | Specifies the end detection of a received frame.   - After character delay time elapses:    The frame has neither a fixed length nor defined end delimiters. The end of a frame is indicated by a gap in the character sequence. The size of this gap is specified by the character delay time. - On receipt of fixed number of characters:    The length of the received frame is always the same. When data is received, the end of the frame is recognized when the set number of characters has been received. - On receipt of the end delimiter(s):    At the end of the frame there are one or two defined end delimiters. When data is received, the end of the frame is recognized when the configured end delimiter is received. |
| No. of end delimiters | 1  2 | 1 | Selection of the number of end delimiters.   A maximum of 2 end delimiters can be configured. When data is received, the end of the frame is recognized when the selected end delimiter combination is received. |
| 1st end delimiter | 0...255 | 3 | Entry of the first end delimiter of a maximum of two end delimiters for the end criteria "On receipt of the end delimiter(s)". The selected end delimiter or the selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| 2nd end delimiter | 0...255 | 0 | Entry of the second end delimiter of a maximum of two end delimiters for the end criteria "On receipt of the end delimiter(s)". The selected end delimiter combination limits the length of the frame.  Parameter value depending on the "Data bits" parameter. |
| Frame length | 1...233 / 1...229 | 233 | Entry of the frame length in bytes for the end criterion "On receipt of fixed number of characters". |
| Character delay time | 0...65535 | 15 | Entry of the time [ms] that can elapse until a frame end is recognized. Select the character delay time dependent on the send behavior of your communication partner. Depending on the data transmission speed the character delay time is limited to a minimum value.  Note that the ASCII driver also pauses between two telegrams during transmission. |
| <sup>1)</sup> Only in connection with the reader interfaces X21 and X22. |  |  |  |

## Reader

This section contains information on the following topics:

- [RF680R/RF685R reader](#rf680rrf685r-reader)
- [RF610R/RF615R readers](#rf610rrf615r-readers)
- [Reader RF360R](#reader-rf360r)

### RF680R/RF685R reader

This section contains information on the following topics:

- [Readers RF680R/RF685R for the UHF range](#readers-rf680rrf685r-for-the-uhf-range)
- ["Web Based Management" parameter group](#web-based-management-parameter-group-2)
- ["Module parameters" parameter group](#module-parameters-parameter-group-4)
- ["Configuration management" parameter group](#configuration-management-parameter-group-1)
- ["RFID communication" parameter group](#rfid-communication-parameter-group)
- ["Digital inputs/outputs" parameter group](#digital-inputsoutputs-parameter-group)

#### Readers RF680R/RF685R for the UHF range

The UHF readers RF680R and RF685R are intended for use in logistics and automation, for example on a production line but are equally suitable for applications in logistics. To meet these requirements, the readers were equipped with a high transmit power and degree of protection (IP65). The readers are equipped with extensive diagnostic options and can process ISO 18000-62 and ISO 18000-63 transponders.

The RF685R has one special feature with its internal, adaptive antenna. This significantly increases the reliability of read and write actions even under difficult radio conditions.

The RF680R and RF685R readers are either integrated without problems in SIMATIC S7 automation systems via an integrated PROFINET connector or via the RS-422 interface and the ASM 456 communications module via PROFIBUS. Suitable programming blocks are available. A second Ethernet interface (both M12) can be used for diagnostics during operation so that the connection to the higher-level system does not need to be interrupted.

The WBM (Web Based Management) allows commissioning, configuration and diagnostics of the devices using an Internet browser. This makes additional updates and installation of configuration and diagnostics software unnecessary.

#### "Web Based Management" parameter group

In this parameter group you can start the Web Based Management.

Parameters in the "Web-based management" parameter group

| Parameter | Description |
| --- | --- |
| Web Based Management (WBM) | Starting the Web Based Management of the reader.  The Web Based Management provides a wide range of functions for configuring the readers.  Note: The WBM can only be started if either the PROFINET connection between the CPU and reader is established or the reader was assigned the IP address stored in the project. This means that the device name has been assigned and the TIA configuration must be loaded on the SIMATIC controller. |

#### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the RF680R/RF685R readers.

Parameters in the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| RFID read point alarm | Off  On | Off | Enabling/disabling read-point related diagnostics messages. |

#### "Configuration management" parameter group

In this parameter group, you can load or save the configuration data.

Parameters of the "Configuration management" parameter group

| Parameter | Description |
| --- | --- |
| User name<sup> 1)</sup> | User name of a user created in the WBM of the reader  Note that the user must have the required rights. |
| Password<sup> 1)</sup> | Input box for the password of the selected user |
| Load configuration to device | Load configuration data into the reader from the STEP 7 project. |
| Save configuration in project | Save configuration data of the reader in the current STEP 7 project. |
| <sup>1)</sup> User name and password must only be entered when the user management of the reader in the WBM is enabled. |  |

##### Requirements

The following requirements must be met to allow configuration data to be loaded or saved:

- The "PROFINET interface [X1]" parameter contains the correct IP address of the reader.
- The entered user has the required rights to run the download/upload.
- Note that https is not supported with TIA Portal versions ≤ V17.

#### "RFID communication" parameter group

In this parameter group you can configure the address range of the RFID communication.

Parameters in the "RFID communication" parameter group

| Parameter | Description |
| --- | --- |
| General | General settings  Input boxes for the name of the communication and for a comment. |
| I/O addresses | Specify the I/O address of the reader ("LADDR")  This parameter is used in the "IID_HW_CONNECT" variable. |
| Hardware identifier | Specify the hardware identifier of the reader ("HW-ID")  This parameter is used in the "IID_HW_CONNECT" variable. |

#### "Digital inputs/outputs" parameter group

In this parameter group you can configure the address range of the digital inputs / outputs.

Parameters in the "Digital inputs / outputs" parameter group

| Parameter | Description |
| --- | --- |
| General | General settings  Input boxes for the name of the of the digital inputs / outputs and for a comment. |
| I/O addresses | Specify the I/O address of the digital inputs/outputs  Using the set address range (I/O address), the digital inputs/outputs configured in the WBM of the reader can be accessed. |
| Hardware identifier | Specify the hardware identifier of the digital inputs/outputs. |

### RF610R/RF615R readers

This section contains information on the following topics:

- [RF610R/RF615R readers for the UHF range](#rf610rrf615r-readers-for-the-uhf-range)
- ["Module parameters" parameter group](#module-parameters-parameter-group-5)
- ["Configuration management" parameter group](#configuration-management-parameter-group-2)
- ["RFID communication" parameter group](#rfid-communication-parameter-group-1)
- ["Digital inputs/outputs" parameter group](#digital-inputsoutputs-parameter-group-1)

#### RF610R/RF615R readers for the UHF range

The UHF readers SIMATIC RF610R and RF615R are intended for use in production logistics and distribution. To meet these requirements, the readers were equipped with a high transmit power and degree of protection (IP65). The readers are equipped with extensive diagnostic options and can process ISO 18000-62 and ISO 18000-63 transponders.

The reader is either integrated without problems in SIMATIC S7 automation systems via an integrated PROFINET connector or via the RS-422 interface and the ASM 456 communication module via PROFIBUS. Suitable programming blocks are available.

The WBM (Web Based Management) allows commissioning, configuration and diagnostics of the devices using an Internet browser. This makes additional updates and installation of configuration and diagnostics software unnecessary.

#### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the RF610R/RF615R readers.

Parameters in the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| RFID read point alarm | Off  On | Off | Enabling/disabling read-point related diagnostics messages. |

#### "Configuration management" parameter group

In this parameter group, you can load or save the configuration data.

Parameters of the "Configuration management" parameter group

| Parameter | Description |
| --- | --- |
| User name<sup> 1)</sup> | User name of a user created in the WBM of the reader  Note that the user must have the required rights. |
| Password<sup> 1)</sup> | Input box for the password of the selected user |
| Load configuration to device | Load configuration data into the reader from the STEP 7 project. |
| Save configuration in project | Save configuration data of the reader in the current STEP 7 project. |
| <sup>1)</sup> User name and password must only be entered when the user management of the reader in the WBM is enabled. |  |

##### Requirements

The following requirements must be met to allow configuration data to be loaded or saved:

- The "PROFINET interface [X1]" parameter contains the correct IP address of the reader.
- The entered user has the required rights to run the download/upload.
- Note that https is not supported with TIA Portal versions ≤ V17.

#### "RFID communication" parameter group

In this parameter group you can configure the address range of the RFID communication.

Parameters in the "RFID communication" parameter group

| Parameter | Description |
| --- | --- |
| General | General settings  Input boxes for the name of the communication and for a comment. |
| I/O addresses | Specify the I/O address of the reader ("LADDR")  This parameter is used in the "IID_HW_CONNECT" variable. |
| Hardware identifier | Specify the hardware identifier of the reader ("HW-ID")  This parameter is used in the "IID_HW_CONNECT" variable. |

#### "Digital inputs/outputs" parameter group

In this parameter group you can configure the address range of the digital inputs / outputs.

Parameters in the "Digital inputs / outputs" parameter group

| Parameter | Description |
| --- | --- |
| General | General settings  Input boxes for the name of the of the digital inputs / outputs and for a comment. |
| I/O addresses | Specify the I/O address of the digital inputs/outputs  Using the set address range (I/O address), the digital inputs/outputs configured in the WBM of the reader can be accessed. |
| Hardware identifier | Specify the hardware identifier of the digital inputs/outputs. |

### Reader RF360R

This section contains information on the following topics:

- [Reader RF360R for the HF range](#reader-rf360r-for-the-hf-range)
- ["Web Based Management" parameter group](#web-based-management-parameter-group-3)
- ["Configuration management" parameter group](#configuration-management-parameter-group-3)
- ["Module parameters" parameter group](#module-parameters-parameter-group-6)
- [Parameter group "Module parameters" of the submodules](#parameter-group-module-parameters-of-the-submodules-2)

#### Reader RF360R for the HF range

The HF reader SIMATIC RF360R is designed for use in industrial production for the control and optimization of material flow. To meet these requirements, the readers have a compact design, a high degree of protection (IP67) as well as high data transmission rates. The readers are equipped with extensive diagnostic options and can process RF300 and ISO 15693 transponders.

The reader can be integrated directly into SIMATIC S7 automation systems by using one of the two integrated PROFINET connections. The program blocks for the Ident profile/RFID standard profile allow simple programming using the SIMATIC S7 tools. The program block for the Ident profile/RFID standard profile can be operated in S7-300 as well as S7-400 controllers. For the S7-1200 and S7-1500 the Ident profile must be used. The transponder data is accessed by means of normal addressing. You will find more information on physical addressing of the transponders, also referred to as normal addressing, in the "SIMATIC RF300" System Manual.

The WBM (Web Based Management) allows commissioning, configuration and diagnostics of the devices using a browser. This makes additional updates and installation of configuration and diagnostics software unnecessary.

#### "Web Based Management" parameter group

In this parameter group you can start the Web Based Management.

Parameters in the "Web-based management" parameter group

| Parameter | Description |
| --- | --- |
| Web Based Management (WBM) | Starting the Web Based Management of the reader.  The Web Based Management provides a wide range of functions for configuring the readers.  Note: The WBM can only be started if either the PROFINET connection between the CPU and reader is established or the reader was assigned the IP address stored in the project. This means that the device name has been assigned and the TIA configuration must be loaded on the SIMATIC controller. |

#### "Configuration management" parameter group

In this parameter group, you can load or save the configuration data.

Parameters of the "Configuration management" parameter group

| Parameter | Description |
| --- | --- |
| User name<sup> 1)</sup> | User name of a user created in the WBM of the reader  Note that the user must have the required rights. |
| Password<sup> 1)</sup> | Input box for the password of the selected user |
| Load configuration to device | Load configuration data into the reader from the STEP 7 project. |
| Save configuration in project | Save configuration data of the reader in the current STEP 7 project. |
| <sup>1)</sup> User name and password must only be entered when the user management of the reader in the WBM is enabled. |  |

##### Requirements

The following requirements must be met to allow configuration data to be loaded or saved:

- The "PROFINET interface [X1]" parameter contains the correct IP address of the reader.
- The entered user has the required rights to run the download/upload.
- Note that https is not supported with TIA Portal versions ≤ V17.

#### "Module parameters" parameter group

In this parameter group, you can configure all module-specific parameters of the reader.

Parameters of the "Module parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Diagnostic interrupt of the device | On  Off | On | Switch the diagnostic interrupt messages of the reader on/off. |

#### Parameter group "Module parameters" of the submodules

In this parameter group, you can configure all module-specific parameters of the connected devices. Note that some of the following parameters are module-specific. For some module types, not all parameters are displayed.

With the "Reader configuration_1" submodule, configurations can be transferred from or to the connected device, and a status query can be performed via the device.

Communication between the reader and transponder takes place by means of the "RFID communication_1" submodule.

Parameters of the parameter group "Module parameters &gt; General parameters" of the submodules

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| User mode | Ident profile / RFID standard profile | Ident profile / RFID standard profile | With this parameter, you select the block:   - Ident profile/RFID standard profile:    Single tag / multitag operation. The program block for the Ident profile is used on the controller. |
| Diagnostic interrupt | None  Hard errors  Hard/soft errors | None | With this parameter, you determine the extent to which the reader-related diagnostic interrupt messages are to be reported.  - None:   No interrupts are generated. - Hard errors:   Critical hardware errors are reported by the S7 diagnostics. - Hard/soft errors:   Critical hardware faults and errors occurring when processing commands are reported by the S7 diagnostics. |
