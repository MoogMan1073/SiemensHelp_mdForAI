---
title: "SIMATIC Ident"
package: TFIdentMainenUS
topics: 22
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SIMATIC Ident

This section contains information on the following topics:

- [SIMATIC Ident](#simatic-ident-1)

## SIMATIC Ident

This section contains information on the following topics:

- ["SIMATIC Ident" technology objects](#simatic-ident-technology-objects)
- [Adding a technology object](#adding-a-technology-object)
- [Working with the configuration dialog](#working-with-the-configuration-dialog)
- [Technology object "TO_Ident"](#technology-object-to_ident)
- [Technology object "TO_TagLayout"](#technology-object-to_taglayout)

### "SIMATIC Ident" technology objects

The technology objects of the "SIMATIC Ident" technology object group support you when configuring your SIMATIC Ident devices and systems.

The "SIMATIC Ident" technology object group contains the following technology objects:

- TO_Ident
- TO_TagLayout

#### TO_Ident

The "TO_Ident" technology object is a universal technology object for SIMATIC Ident systems which supports you during system setup, configuration and diagnostics of your SIMATIC Ident devices and systems.

#### TO_TagLayout

You use the "TO_TagLayout" technology object to define transponder memory areas, so-called Tag fields, and give them a unique name. This makes it easier to access them later.

### Adding a technology object

#### Adding a technology object in the project navigator

When you add a technology object, a data block is generated. The configuration of the technology object is stored in this data block.

#### Requirements

To use one of the "SIMATIC Ident" technology objects, the following requirements must be met:

- You have created a project.

  - TO_Ident: From V14 SP1 and higher
  - TO_TagLayout: From V16 and higher
- According to the hardware used, the connected devices were added to the hardware configuration ("Devices &amp; Networks"), networked with each other and configured.
- The project contains at least one S7 controller and at least one Ident device (e.g. communications module, reader, optical reader).

  The following controllers are compatible:

  - S7-1200 as of V4.0
  - S7-1500 as of V1.8
  - ET200pro (CPU 1516pro) as of V1.8
  - ET200SP as of V1.8

#### Procedure

Follow the steps below to add a technology object:

1. Open the CPU folder in the project tree.
2. Open the "Technology objects" folder.
3. Double-click on ""Add new object".

   The "Add new object" dialog box opens.
4. Click the "SIMATIC Ident" button.
5. In the "Version" column select the newest version (as of "V5.0").
6. Select the required technology object.
7. Type in an individual name for the technological object in the "Name" input field.
8. Click "More information" if you want to store your own information for the technology object.
9. Confirm with "OK".

#### Result

The new technology object is created and saved to the "Technological objects" folder in the project tree.

### Working with the configuration dialog

You configure the properties of the technology object in the configuration window. To open the configuration window of the technology object, follow these steps:

1. In the project tree, open the "Technological objects" folder.
2. Open the technology object the project tree.
3. Double-click on the "Configuration" object.

#### Symbols of the configuration window

Symbols in the area navigation of the configuration and Inspector window show additional information about the completeness of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Symbols of the configuration window](images/95593220363_DV_resource.Stream@PNG-de-DE.png) | The configuration contains default values and is complete  The configuration only contains default values. With these preset values you can use the technology object without additional changes. |
| ![Symbols of the configuration window](images/95593236235_DV_resource.Stream@PNG-de-DE.png) | The configuration contains values defined by the user or automatically adapted values and is complete   All input fields of the configuration contain valid values and at least one default value was modified. |
| ![Symbols of the configuration window](images/95593252107_DV_resource.Stream@PNG-de-DE.png) | The configuration is valid but contains unexpected values  At least one input field or a drop down list contains an unexpected value. The corresponding field, or the drop-down list is displayed on a yellow background. When you click on it, the roll-out warning message shows you the cause of the warning. |
| ![Symbols of the configuration window](images/95582951691_DV_resource.Stream@PNG-de-DE.png) | The configuration is incomplete or incorrect  At least one input field or a drop down list contains no or an invalid value. The corresponding field, or the drop-down list, is displayed on a red background. Click the roll-out error message to identify the cause of the error. |

### Technology object "TO_Ident"

This section contains information on the following topics:

- [Technology object "TO_Ident"](#technology-object-to_ident-1)
- [Configuring Ident systems](#configuring-ident-systems)
- [Diagnosing Ident systems](#diagnosing-ident-systems)

#### Technology object "TO_Ident"

##### Introduction

The technology object for SIMATIC Ident products, "TO_Ident", allows simple parameter assignment of an Ident system in the TIA Portal. It provides an interface with simple parameter assignment between the configured hardware and the function blocks in the "SIMATIC Ident" library.

With the aid of the "Configuration" object you can select a configured device, decide on the channel / the read point and if necessary specify the connected Ident system. The technology object therefore automatically determines all the parameters required for operation.

The "Diagnostics" object displays the last 5 error messages signaled by the Ident device to the function blocks. In addition to this for every error message an error description and detailed information about the executed command are displayed.

The following overview shows the basic procedure for adding and configuring a "TO_Ident" technology object.

##### Procedure

Proceed as follows to configure the technology object "TO_Ident":

| Step | Description |
| --- | --- |
| 1 | [Adding a technology object](#adding-a-technology-object) |
| 2 | [Configuring devices using the technology object](#configuring-devices-using-the-technology-object) |
| 3 | [Calling the Ident instruction in the user program](#calling-the-ident-instruction-in-the-user-program) |
| 4 | Load technology object in CPU |
| 5 | [Diagnosing devices](#block-diagnostics) |

#### Configuring Ident systems

This section contains information on the following topics:

- [Configuring devices using the technology object](#configuring-devices-using-the-technology-object)
- [Calling the Ident instruction in the user program](#calling-the-ident-instruction-in-the-user-program)
- [Loading the configuration on the CPU](#loading-the-configuration-on-the-cpu)

##### Configuring devices using the technology object

This section contains information on the following topics:

- [Configuring basic parameters](#configuring-basic-parameters)
- [Configuring Ident device parameters](#configuring-ident-device-parameters)
- [Configuring reader parameters](#configuring-reader-parameters)

###### Configuring basic parameters

In this parameter group, you can configure the module-specific parameters of your system.

Parameters in the "Basic parameters" parameter group

| Parameter | Description |
| --- | --- |
| Ident device | Click "..." and select the Ident device to be configured in the folder "Distributed I/O" or "Local modules".  The following devices can be selected:  - ASM 456 - RF166C - RF120C, RF170C, RF180C - RF185C, RF186C, RF188C, RF186CI, RF188CI - RF360R - RF610R, RF615R - RF680R, RF685R - MV400, MV500      **Show all Ident devices/modules**   If you want to configure an Ident device that is not fully integrated into the current TIA Portal version yet, select the check box "Show all Ident devices/modules". By activating this parameter, the "LADDR" parameter is shown. For detailed information on this function see the following paragraph. |
| Automatic reset | Select/clear the check box if necessary. When the check box is selected, a reset command is always sent automatically to the configured Ident device when necessary. In this case, you no longer need to perform this manually, e.g. after a controller restart or on errors that require a reset.  If an error occurs, the reset is started automatically when the next command is executed. For transponders that are only in the antenna field for a very short time, note that the reset should possibly be performed manually so as not to extend the command runtime of the next command with an automatic reset.  RF600: When presence mode is switched on, an automatic reset after an error ends presence mode. Start presence mode again after an error by first sending an inventory command with "Attribute 16#86" after the error.   MV400/MV500: This function is not available for the MV400/MV500 optical readers. |
| Channel | Open the drop-down list and, if needed, select, the channel of the communications module to which the device to be configured is connected. |
| Reader parameter assignment | Open the drop-down list and select the device/system connected to the Ident device that needs parameter assignment. |
| LADDR | Note that this parameter is only displayed when the "Show all Ident devices/modules" check box was selected.  Enter the I/O address of the selected module. This parameter is preset with the "Channel" and potentially "Read point" parameters. |
| Read point | Requirement: An RF600 reader was selected in the "Reader parameter assignment" parameter.  Open the drop-down list and select the read point to be used. |

**Show all Ident devices/modules**

You can use this function to configure Ident devices that are not fully integrated into the current TIA Portal version yet. In this case you must configure the technology object manually. Note that this setting has an effect on some parameters and functions:

- LADDR

  This parameter value is calculated from the start address of the selected Ident device and the channel. However, this value can be adapted manually.
- Ident device parameters and Web Based Management

  These parameter groups are not supported by the function.
- Reader parameters

  The "Transmission speed" parameter is not supported within this parameter group.
- Diagnostics &gt; Hardware diagnostics

  The hardware diagnostics is not supported by the function.

###### Configuring Ident device parameters

Depending on the selected Ident device, the following Ident device parameters are displayed in this parameter group. The displayed Ident device parameters are adopted automatically from the device configuration of the connected devices.

Note that not all parameter values adopted and displayed from the device configuration of the connected devices are permitted in conjunction with the technology object. If non-permitted values are set in the device configuration you can change these either automatically with the "Autoconfiguration" button or manually using the device configuration.

Parameters in the "Ident device parameters" parameter group

| Parameter | Possible displayed parameter value | Permitted parameter values | Description |
| --- | --- | --- | --- |
| User Mode | Ident profile/RFID standard profile  FB 45 / FC 45   FB 55 / FC 55 | Ident profile/RFID standard profile | With this parameter, you select the block.  Note that only the following parameter values are permitted in conjunction with the technology object.  - Ident profile/RFID standard profile: The program block for the Ident profile/RFID standard profile is used on the controller. |
| MOBY Mode | RF200/RF300/RF600;  MV400/MV500; MOBY U/D   RF680R/RF685R   MOBY I/E   Normal addressing   RF300 file handler   MOBY U file handler  MOBY I file handler | RF200/RF300/RF600; MV400/MV500; MOBY U/D  RF680R/RF685R | With this parameter, you set the mode of the communications module.  Note that only the following parameter values are permitted in conjunction with the technology object.  - RF200/RF300/RF600; MV400/MV500; MOBY U/D - RF680R/RF685R |
| Connected device | Parameters via FB / optical readers | Parameters via FB / optical readers | This parameter is only displayed in conjunction with the communications module RF120C.  Note that only the following parameter values are permitted in conjunction with the technology object.  - Parameters via FB / optical readers |

###### "Autoconfiguration" button

The displayed HWCN parameters are adopted automatically from the device configuration of the connected devices. Note that not all parameter values are permitted in conjunction with the technology object. Non-permitted parameter values are highlighted in color.

Click the "Autoconfiguration", button to set the suitable parameter values automatically (e.g. User Mode). The parameter values of the connected device are prepared for the use of the technology object.

> **Note**
>
> **Behavior with MV400/MV500**
>
> Note that the "Autoconfiguration" button does not work with the optical readers MV400 and MV500. With these devices you need to enter the HWCN parameters in the device configuration of the connected devices manually.

###### Configuring reader parameters

Depending on the set basic parameters, the following reader parameters are displayed in this parameter group.

Overview of the "Reader parameters"

| Reader parameter assignment in "Basic parameters" | Transmission speed<sup> 1)</sup> | Presence check | Reset error LED | HF power | Max. number of transponders | Transponder type |  |  | Verification | Program selection with reset | Byte sequence of the reset parameter [hex] | Config mode<sup> 2)</sup> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISO 15693 | RF300 | MOBY E |  |  |  |  |  |  |  |  |  |  |
| RF200 general | ✓ | ✓ | ✓ | - | ✓ | ✓ | - | - | - | - | - | - |
| RF290R | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - | - | - | - | - |
| RF300 general | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ | - | - | - | - | - |
| RF380R | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - | - | - | - |
| RF300 Gen 2 general | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ | ✓ | ✓ | - | - | - |
| RF360R | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ | ✓ | ✓ | - | - | - |
| RF380R  Gen 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | - | - |
| MV400/MV500 | - | - | - | - | - | - | - | - | - | ✓ | - | - |
| General reader | ✓ | - | - | - | - | - | - | - | - | - | ✓ | ✓ |
| Freeport | ✓ | - | ✓ | - | - | - | - | - | - | - | - | - |
| <sup>1)</sup> Note that this parameter is not displayed when the "Show all Ident devices/modules" check box was selected.   <sup>2)</sup> Note that this parameter is only displayed when the "Show all Ident devices/modules" check box was selected. |  |  |  |  |  |  |  |  |  |  |  |  |

The device-specific parameters of the optical readers SIMATIC MV400 and MV500 as well as the readers SIMATIC RF600 (RF61xR and RF68xR) are set in the WBM of the respective device in case of a direct connection to the controller.

Parameters in the "Reader parameters" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Transmission speed | 19.2 kBd  57.6 kBd  115.2 kBd  921.6 kBd | 115.2 kBd | The selection depends on the communications module and Ident system being used. Note that the value specified here is adopted automatically from the device configuration of the connected devices.  With this parameter, you set the transmission speed between the communications module and reader.   When the RFID reader is connected: After changing the transmission speed, the reader must be turned off and on again (cycle power).   When an optical reader is connected: The transmission speed selected here must match the transmission speed selected in the firmware of the reader. |
| Presence check | On  Off (RF field on)  Off (RF field off) | On | On = As soon as there is a transponder in the antenna field of the reader, its presence is reported.  Off (RF field on) = the presence check in the FB is suppressed. The antenna on the reader is nevertheless turned on as long as it has not been turned off by a command.  Off (HF field off) = the presence check in the FB is suppressed. The antenna is turned on only when a command is sent and it then turns itself off again. |
| Reset error LED | On  Off | On | On = the flashing of the error LED on the communications module is reset by each FB reset.   Off = the error LED always indicates the last error. The display can only be reset by turning off the communications module. |
| On  After a successful command  After a reset command  After a reset or a successful command | On = The flashing LED in the event of an error can only be reset by switching off the power supply to the reader.  After a successful command = The flashing of the LED in the event of an error is reset after the successful execution of a command. This only affects communication errors.  After a reset command = The flashing of the LED in the event of an error is reset by a "init_run" or "WRITE-CONFIG" with "Init" (RESET).  After a reset or a successful command = The flashing of the LED in the event of an error is reset by a "init_run" or "WRITE-CONFIG" with "Init" (RESET) or after the successful execution of a command. |  |  |
| HF power <sup>1)</sup> | 0.50 ... 2.00  0.50 ... 5.00 | 1.00  1.25 | Setting for the output power of the reader  The selectable values depend on the connected device. |
| Max. number of transponders | 1 ... 4 | 1 | Number of transponders expected in the antenna field  The selection depends on the connected device. |
| Reader mode | Normal operation  P2P master  P2P slave | Normal operation | Selection of the required reader mode |
| Transponder type | <sup>1)</sup> | <sup>1)</sup> | Selection of the transponder types used   The selection depends on the connected device. |
| Verification | ☐  ☑ | ☐ | This parameter switches ECC mode on. In ECC mode, the reader can detect bit errors on the transponder with a high degree of probability. If possible, corrected data is returned during read access (the data on the transponder remains unchanged). When write access occurs, the affected data on the transponder is corrected - if possible. If a bit error is detected and corrected, the parameter "ANZ_ECC = True" or "STATUS = 0xF0FE0002" is set. If the error cannot be corrected, error "0x0B" or "0xE2FE0100" is output.  Requirement: The transponder was formatted with a set ECC bit.   Only transponders of type RF300 and ISO 14443 (e.g. MOBY E) are supported. |
| Program selection with reset | No program change  1 ... 15 | No program change | Selection of the program that will be used after restarting the optical reader. If the parameter "No program change" is set, after restarting the device the last active program is selected. |
| Byte sequence of the reset parameter [hex] | <sup>1)</sup> | <sup>1)</sup> | Hexadecimal representation of the byte sequence of the reset parameter of the reader. |
| Config mode | 0 ... 255 | 3 | Specifying the reset settings  Enter whether configuration data (byte sequence) is transferred in case of a reset.  1: No configuration data is transferred in case of a reset.  3: The configuration data is transferred in case of a reset. |
| <sup>1)</sup> You will find a detailed description of this parameter in the following paragraphs: |  |  |  |

###### The "HF power" parameter

The selectable values depend on the value specified in the parameter "Reader parameter assignment".

- RF290R

  - Range of values: 0.50 ... 5.00 W
  - Default value: 1.00 W
- RF380R; RF380R Gen 2

  - Range of values: 0.50 ... 2.00 W
  - Default value: 1.25 W

###### The "Transponder type" parameter

Selection of the transponders used. The selection depends on the value specified in the parameter "Reader parameter assignment". The following transponder types can be selected:

- ISO 15693
- RF300
- MOBY E

If you select "ISO 15693", the following selection options are displayed depending on the reader parameter assignment:

| Reader parameter assignment | Values |
| --- | --- |
| RF200 general | General |
| RF290R | General  MDS D3xx, Infineon |
| RF300 general  RF380R | General  MDS D3xx, Infineon  MDS D4xx, Fujitsu - 2 KB  MDS D1xx, NXP  MDS D200, TI   MDS D261, STM/NXP |
| RF300 Gen 2 general  RF380R Gen 2 | General  MDS D3xx, Infineon  MDS D4xx, Fujitsu - 2 KB  MDS D1xx, NXP  MDS D200, TI   MDS D261, STM/NXP  MDS D5xx, Fujitsu - 8 kB |

###### The parameter "Byte sequence of the reset parameter [hex]"

With this parameter, you can specify the Reset parameter in hexadecimal format. These parameters should only be changed ty trained users.

The following Reset parameters are available:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Byte** | 1 | 2...5 <sup>1)</sup> | 6 | 7...8 | 9 | 10 | 11 | 12 | 13...14 | 15 | 16 |
| **Value** | 0x04 | 0x00 | 0x0A | 0x00 | scanning_ time | param | option_1 | distance_ limiting | multitag | field_on_ control | field_on_ time |
| <sup>1)</sup> In the communications module RF180C as of V2.2 in conjunction with MOBY U byte 4 is preset with the calendar week and 5 with the year. |  |  |  |  |  |  |  |  |  |  |  |

##### Calling the Ident instruction in the user program

###### Procedure

Proceed as follows to call the instruction in the user program:

1. Open the CPU folder in the project tree.
2. Open the "Program blocks" folder.
3. Double-click on the OB for cyclic program execution.

   The block is opened in the working area.
4. In the "Instructions" window open the group "Optional packages" and the "SIMATIC Ident" folder.

   The folder and the subfolders contain the instructions.
5. Select an instruction and drag it to your OB.

   The "Call options" dialog is opened.
6. From the "Name" list select an instance data block or enter the name for a new instance data block.
7. Confirm with "OK".
8. Select the configured technology object and drag it to the parameter "HW_CONNECT".

###### Reset the readers using the "Ident profile" or the "Reset_Reader" block

There are various methods for resetting readers:

- If you work with the Ident blocks, reset all reader types with the "Reset_Reader" block. This transfers the values set in the technology object to the readers.
- If you work with the Ident profile, when you set the "INIT" bit, the values set in the technology object are transferred to the reader.
- If you want to send your own "WRITE CONFIG" command, instead of the "INIT" bit you need to use the "EXECUTE" bit.

If a Reset parameter of the technology object needs to be changed at runtime, the relevant value can be overwritten in the data block of the technology object using the user program. The Reset parameters are located in the data block of the technology object in "Static.CONFIGURATION.param_buffer[]".

You will find detailed information on the Ident profile in the manual "Ident Profile and Ident Blocks, Standard Function for Ident Systems" on the pages of "[Industry Online Support](https://support.industry.siemens.com/cs/ww/en/ps/14971/man)".

##### Loading the configuration on the CPU

After configuration you need to load the changes from the technology object or the S7 controller on the connected devices.according to

**Load to device**

When loading to the devices note that a distinction is made between "Software (changes only)" and "Hardware and software (changes only)". If only changes to the technology object software have been made, loading is performed via the technology object. If changes were made to the hardware and software, loading is via the S7 controller.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Load to device when using the "Autoconfiguration" button**  If the "Autoconfiguration" button was used during configuration, you need to load the changes on the connected devices via the S7 controller ("Hardware and software (changes only)"). |  |

#### Diagnosing Ident systems

This section contains information on the following topics:

- [Calling the diagnostics function](#calling-the-diagnostics-function)
- [Block diagnostics](#block-diagnostics)
- [Hardware diagnostics](#hardware-diagnostics)

##### Calling the diagnostics function

After configuration of the technology object is complete, you can monitor the devices configured in the technology object using the diagnostics function.

###### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the S7 controller.
- The Ident instruction is called in the user program.
- A technology object was created and loaded on the S7 controller-
- The S7 controller is in "RUN" mode.

###### Procedure

To open the display editor for the diagnostics function, follow these steps:

1. In the project tree, open the "Technological objects" folder.
2. Open the relevant technology object in the project tree.
3. Double-click on the "Diagnostics" object.
4. Click on the symbol."Monitor all" to activate the monitoring mode.

##### Block diagnostics

In Block diagnostics you can display the last error messages to occur during command execution.

The following values are read by the technology object and displaed:

Displayed values of "Block diagnostics"

| Displayed values | Description |
| --- | --- |
| Date and time | Shows the date and time when the error occurred. |
| Command | Shows the command with which the error occurred. |
| Error description | Shows a brief description of the error that occurred. |
| Note: The last five error messages are displayed and described in the table. If a new error message is displayed, the previously displayed error messages are moved one line down. A maximum of five error messages are displayed. |  |
| Error message | Shows the error message of the error that occurred |
| Error description | Shows a detailed description of the error that occurred |
| Date and time | Shows the date and time when the error occurred. |
| Command code | Show the command code of the command with which the error occurred. |
| Command | Shows the command with which the error occurred. |
| Attribute | Shows the attribute of the command with which the error occurred. |

##### Hardware diagnostics

In Hardware diagnostics you can display the status parameters of the selected reader and of the transponder currently in the antenna field.

###### Monitoring status

In this area you can update the reader and transponder parameters and reset error counters of the reader.

###### Reader status

The following parameters are read by the technology object and displayed:

Displayed parameters of the "Reader status" area

| Displayed parameters | Description |  |
| --- | --- | --- |
| Hardware type | Hardware type of the reader |  |
| Hardware version | Hardware version of the reader |  |
| Bootloader version | Bootloader version of the reader |  |
| Firmware version | Firmware version of the reader |  |
| Driver type | Driver type of the serial interface of the reader |  |
| Driver version | Driver version of the serial interface of the reader |  |
| Interface | Used serial interface of the reader  Possible values: RS232, RS422 |  |
| Transmission speed | Used transmission speed of the reader  Possible values: 19.2; 57.6; 115.2 kBd |  |
| Distance limiting | Set transmit power of the reader (RF380R) The following values are possible: |  |
| Value | Meaning |  |
| 02 | 0.5 W |  |
| 03 | 0.75 W |  |
| 04 | 1.0 W |  |
| 05 | 1.25 W |  |
| 06 | 1.5 W |  |
| 07 | 1.75 W |  |
| 08 | 2.0 W |  |
| Max. number of transponders | Maximum number of transponders to be expected that may be located in the antenna field at the same time. |  |
| Transponder type | Set transponder type profile  The following values are possible: |  |
| Value | Meaning |  |
| 00 | RF300 (RF3xxT) |  |
| 01 | ISO 15693 general |  |
| 03 | MDS D3xx, Infineon |  |
| 04 | MDS D4xx,Fujitsu - 2 kB |  |
| 05 | MDS D1xx, NXP |  |
| 06 | MDS D2xx, TI |  |
| 07 | MDS D261, ISTM |  |
| 08 | MDS D5xx, Fujitsu - 8 kB |  |
| 10 | RF300 (RF3xxT) |  |
| 20 | ISO 14443 (MOBY E, E6xx) |  |
| 31 | General Mode |  |
| 40 | P2P master |  |
| 41 | P2P master &amp; mixed operation with ISO transponder (MDS Dxxx) |  |
| 50 | P2P master &amp; mixed operation with RF300 transponder |  |
| 4F | P2P slave |  |
| Antenna status | Status of the antenna |  |
| Presence check | Set presence check profile |  |

###### Transponder status

The following parameters are read by the technology object and displayed:

Displayed parameters of the "Transponder status" area

| Displayed parameters | Description |
| --- | --- |
| UID | Unique identifier of the transponder |
| Transponder type | Transponder type (vendor, identification) |
| Version | Version of the transponder chip |
| Lock status of the OTP area | Disabled blocks of the OTP areaon the chip |
| Size of the user memory | Memory size of the user memory in bytes |
| Size of a memory block | Size of the memory blocks of the transponder chip |
| Number of memory blocks | Number of memory blocks of the transponder chip |
| Measured value power flux density | Radiant power that arrives at the transponder.  The lower the value, the more power the transponder receives. |
| Passive error counter | Number of passive errors which occurred |
| Active error counter | Number of errors which occurred  Sum of the signature and CRC errors |
| Presence counter | Time in [ms] that the transponder spent in the antenna field. |

###### Error counter

The following error types are read by the technology object and displayed:

Error types displayed in the "Error counter" area

| Displayed error types | Description |
| --- | --- |
| FZP | Passive error counter  This error counter is an indicator for a disturbed environment (interferences). |
| ABZ | Abort counter  Counter for protocol errors on the air interface for which the transponder aborted communication. |
| CFZ | Code error counter  Counter for disruptions or collisions on the air interface that caused communication to be disturbed. |
| SFZ | Signature error counter  Counter for failed signature encryptions of written data blocks. Only relevant for the transponder type "RF300". |
| CRCFZ | CRC error counter  Counter for failed CRC checks |
| ASMFZ | Error counter for problems on the interface to the host (CM/PC)  Counter for errors on the serial interface |
| **Signal strength** |  |
| AMLI | AM power indicator  Received signal strength [dB] for which amplitude modulation with the transponder was detected. |
| PMLI | PM power indicator  Received signal strength [dB] for which phase modulation with the transponder was detected. |

> **Note**
>
> **Error counter readings**
>
> The displayed error counter readings are counted from the last restart of the reader or the last manual reset of the error counter readings.

### Technology object "TO_TagLayout"

This section contains information on the following topics:

- [Technology object "TO_TagLayout"](#technology-object-to_taglayout-1)
- [Configuring parameters](#configuring-parameters)
- [Loading the configuration on the CPU](#loading-the-configuration-on-the-cpu-1)

#### Technology object "TO_TagLayout"

##### Introduction

By using the technology object "TO_TagLayout", you can divide the memory area of transponders in up to 64 address areas, so-called Tag fields, address these fields symbolically, specify their size and data type, and give them a unique name. By assigning names that are address specific, it will be easier to program the fields later with the "Read_Tagfield" and "Write_Tagfield" blocks.

#### Configuring parameters

In this parameter group, you can configure the address area parameters for the tag fields of your transponder.

Parameters in the "Transponder configuration" parameter group

| Parameter | Description |  |
| --- | --- | --- |
| Transponder family | Select the transponder family for which you want to define tag fields. |  |
| Transponder type | Select the specific transponder type and the transponder version (amount of memory in the transponder) for which you want to define tag fields. |  |
| Lowest  transponder address | Enter the lowest possible transponder address. The lowest address is usually always "0". The following transponder is an exception to this rule:  RF320T: 65280 ("0xFF00")  Note: Note that writing as of address "65408" ("0xFF80") until address "65424" ("0xFF90") irreversibly enables write protection of all RF300 transponders. You can find detailed information on this in the section "Memory configuration of the RF300 transponders" in the "SIMATIC RF300" system manual. |  |
| Highest  transponder address | Enter the highest possible transponder address. The highest address depends on the amount of memory in the transponder and can be derived from the selected transponder in the "Transponder type" parameter.  Note that the highest address is always specified in bytes and that the number "0" is included in the calculation.  Below are just a few examples for the highest transponder address depending on the transponder type: |  |
| Transponder type | Highest transponder address |  |
| MDS D4xx (2000 bytes) | ≙ 1999 ("0x07CF") |  |
| RF340T (32 KB) | ≙ 32764 ("0x7FFC") |  |
| RF630L (64 bytes) | ≙ 63 ("0x003F") |  |
| RF645T (256 bytes) | ≙ 255 ("0x00FF") |  |
| Selection of the  memory bank | Select the memory bank in which you want to create the following tag fields. This parameter is only relevant for transponders of the SIMATIC RF600 product family.  RF600 transponders are divided up into the following four banks:  - Bank 0: Reserved - Bank 1: EPC - Bank 2: TID - Bank 3: USER (user memory) |  |

Changes of the address area parameters are transferred directly to the technology object "TO_TagLayout".

You can create and define the tag fields in this parameter group.

Parameters of the "Tag layout definition" parameter group

| Parameter | Description |
| --- | --- |
| Index | Index number of tag field. Up to 64 tag fields are available for each "TO_TagLayout" technology object. |
| Name | Enter the name of the selected tag field (max. 20 characters). The entered name is automatically displayed in the drop-down list in the "Tag field" parameter or transferred there. |
| Data type | Select the data type of the tag field. Note that the selection of the data type has an effect on the "Elements" and "Length" parameters. |
| Start address | Enter the start address of the selected tag field. The start address must be within the previously defined lowest and highest transponder address. Note that tag fields can be created as a subset of other tag fields, but individual tag fields may not cross or overlap each other. |
| Elements | Display/output of the array/string elements. Note that this parameter value is pre-defined by the "Data type" parameter.  The following values are possible:  - Array: (1 ... 262144) - String: (1 ... 254) |
| Length | Display/output of the tag field length. Note that this parameter value is pre-defined by the "Data type" parameter.   If the "Array" data type was selected, the value is identical to the value in the "Elements" parameter. If the "String" data type was selected, the value specified here is 2 bytes larger than the value in the "Elements" parameter. |
| End address | Display/output of the tag field end address. Note that this parameter value depends on the values entered in the parameters "Data type", "Start address" and "Elements". |
| Create DB/DT | Click the "Create DB/DT" button to create a data block/data type that provides easy access to the defined tag fields. If an existing "TagLayout" technology object was revised, the data block/data type is updated.    The data block contains a list of all tag fields of the technology object with the associated IDs and is used for symbolic selection of a tag field at the "TAGFIELD" parameter of the function blocks "Read_Tagfield" and "Write_Tagfield".   Name of the DB: &lt;Name of the TO&gt;_Indexes  The data type can be used in a data block and supplies the "IDENT_DATA" parameter of the function blocks "Read_Tagfield" and "Write_Tagfield" with the user data.  Name of the DT: &lt;Name of the TO&gt;_data_type |

#### Loading the configuration on the CPU

After configuration, you need to load the changes from the technology object or the S7 controller to the connected device.

**Load to device**

When downloading to the device, note that a distinction is made between "Software (changes only)" and "Hardware and software (changes only)". If only changes to the technology object software have been made, loading is performed via the technology object. If changes were made to the hardware and software, loading is via the S7 controller.
