---
title: "SIMATIC Ident"
package: InstructionsIdentenUS
topics: 57
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SIMATIC Ident

This section contains information on the following topics:

- [SIMATIC Ident](#simatic-ident-1)

## SIMATIC Ident

This section contains information on the following topics:

- [Ident manual](#ident-manual)
- [Programming Ident blocks](#programming-ident-blocks)
- [Programming the Ident profile](#programming-the-ident-profile)
- [Error messages](#error-messages)

### Ident manual

You will find detailed information on the Ident profile in the manual "Ident Profile and Ident Blocks, Standard Function for Ident Systems" on the pages of "[Siemens Industry Online Support](https://support.industry.siemens.com/cs/ww/en/ps/14971/man)".

### Programming Ident blocks

This section contains information on the following topics:

- [Configuration/programming](#configurationprogramming)
- [Basic blocks](#basic-blocks)
- [Status blocks](#status-blocks)
- [Tag field blocks](#tag-field-blocks)
- [Advanced blocks](#advanced-blocks)
- [Reset blocks](#reset-blocks)

#### Configuration/programming

You can use the technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident)" or not use it for parameter assignment of the Ident blocks / Ident profile. If you do not use the technology object for parameter assignment, you need the data type "IID_HW_CONNECT". Note that this data type is only contained in library versions < V5.0. SIMATIC S7-300/400 controllers are not compatible with the technology object.

Before you can start parameter assignment of the blocks, you first need to create a variable of the PLC data type "IID_HW_CONNECT". The Ident system or a channel of the Ident system is addressed using the "IID_HW_CONNECT" PLC data type.

##### Addressing the Ident devices

When working with all the instructions/blocks, you require the "IID_HW_CONNECT" data type to address the reader. Setting the command parameters for the Ident profile is handled by the Ident blocks. The Ident profile and the "AdvancedCMD" block also require the "IID_CMD_STRUCT" data type for the parameter assignment of the individual commands. Depending on whether you work with the Ident profile or the Ident blocks, you need to link in and assign parameters for these data types as described in the following sections.

##### Configuring a tag of the "IID_HW_CONNECT" data type

**Follow the steps below to set the parameters for the tag of the "IID_HW_CONNECT" data type for a channel:**

1. Create a new tag in a data block or in the static area of a function block.

   ![Creating a data block](images/66928573579_DV_resource.Stream@PNG-en-US.PNG)

   Creating a data block
2. Specify the address data of the Ident device or the channel.

   - HW_ID: Hardware identifier of the module (only with S7-1200 and S7-1500)
   - CM_CHANNEL: Channel within a module
   - LADDR: I/O address of the module

   You can read out the values of the "HW_ID" and "LADDR" parameters in the device configuration in the properties of the communications module/reader. Enter the parameter values you have read out in the "Start value" column of the corresponding parameters. Reading out parameter values is described below.

**Follow the steps below to read out the parameter values "HW_ID" and "LADDR" for a channel:**

1. Open the network view and double-click on the communications module.

   Reaction: TIA switches to the device view and the properties window of the CM opens.
2. In the "Device overview" tab, select the relevant module.

   The I/O address displayed in the tab corresponds to "LADDR".

   Note that the input and output address must have the same value.
3. In the "Properties > System constants" tab, you will find the hardware identifier that corresponds to the "HW_ID".

   ![The "Hardware identifier" parameter](images/114079829771_DV_resource.Stream@PNG-en-US.png)

   The "Hardware identifier" parameter
4. Transfer the values of "LADDR" and "HW_ID" to the PLC data type "IID_HW_CONNECT" of the reader for which you want to set parameters.

> **Note**
>
> **Setting the user mode**
>
> In the properties of the communication module/reader, make sure that you assign the value "RFID standard profile" to the "User mode" parameter and select the suitable MOBY mode.

With all other communications modules/readers, you will find the two parameters directly in the properties of the module.

The "IID_HW_CONNECT" data type has now been created for a channel. Repeat these steps for every other reader/channel. If you want to use a different channel of the reader/CM, set this using the "CM_CHANNEL" parameter. The "HW_ID" and "LADDR" parameters remain the same for all channels/readers/antennas. With an RF166C or RF18xC/RF18xCI communications module, each reader is assigned to a separate module and has its own "HW_ID" and "LADDR". Please note that the value of the channel always needs to be "1".

All required function blocks and data types are now included in your project and you can now start programming. The "IID_HW_CONNECT" data type has also been created and addressed. You can now start programming the blocks.

> **Note**
>
> **Configure "IID_CMD_STRUCT"**
>
> If you work with the Ident profile or with the "AdvancedCmd" block, you also need to create a further element with the data type "IID_CMD_STRUCT" (Array [1...n]) in the data block you have already created.

##### Creating blocks

Before data can be exchanged with a reader (e.g. reading/writing data), the relevant Ident device must be reset once. When using the Ident blocks, you can use a reset block (e.g. "Reset Reader") for this. An appropriately configured "WRITE-CONFIG" command must be executed when using the Ident profile.

**Requirement**

The "IID_HW_CONNECT" data type has been assigned parameters.

**Follow the steps below to link in a block and to set the call parameters:**

1. Open the program block you have created by double-clicking in the "Project tree > Program blocks" tab.
2. Drag the required block from the instruction register into the program block.
3. Enter the tag you created earlier in the "HW_CONNECT" input parameter.

The block is called and connected to the relevant channel.

> **Note**
>
> **Working with multiple channels/read points**
>
> When you work with multiple channels/read points, you must ensure that the block is called with a separate instance DB for each channel/read point.

> **Note**
>
> **Working with the Ident profile or with the "AdvancedCmd" block**
>
> If you work with the Ident profile or with the "AdvancedCmd" block, you also need to connect the "CMDREF" input parameter with a variable of the "IID_CMD_STRUCT" (Array [1...n]) data type.

#### Basic blocks

This section contains information on the following topics:

- [Read](#read)
- [Read_MV](#read_mv)
- [Reset_Reader](#reset_reader)
- [Set_MV_Program](#set_mv_program)
- [Write](#write)

##### Read

###### Description

The "Read" block reads the user data from the transponder and enters this in the "IDENT_DATA" buffer. The physical address and the length of the data are transferred using the "ADDR_TAG" and "LEN_DATA" parameters. With the RF61xR/RF68xR readers, the block reads the data from memory bank 3 (USER area). Specific access to a certain transponder takes place with the optional "EPCID_UID" and "LEN_ID" parameters.

###### Parameter

The following table shows the parameters of the "Read" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| ADDR_TAG | Input | DWORD | DW#16#0 | Physical address on the transponder where the read starts. You will find more information on addressing in the section "[Transponder addressing of the Ident profile and Ident blocks, standard function for Ident systems manual](https://support.industry.siemens.com/cs/ww/en/ps/14971/man)".  With MV: The length of the read code is located starting at address "0" (2 bytes). The read code is located starting at address "2".<sup> 1)</sup> |
| LEN_DATA | Input | WORD | W#16#0 | Length of the data to be read |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF200, RF300, RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Data buffer in which the read data is stored.  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |
| <sup>1)</sup> You can find additional information on working with optical reader systems in the operating instructions for "SIMATIC MV420 / SIMATIC MV440" and "SIMATIC MV500". |  |  |  |  |

##### Read_MV

###### Description

The "Read_MV" block reads out the read result of an optical reader. The "Read" block must be used to read the configuration. The length of the data to be read is calculated automatically by the block based on the length of the created receive buffer. The actual length of the read result is output in the "LEN_DATA" output parameter. The data will be saved in the "IDENT_DATA" data buffer. If the buffer is too small, the error message "0xE7FE0400" appears and the expected length is output at "LEN_DATA".

To achieve an optimum speed, we recommend that you adapt the length of the data type "IDENT_DATA" so that this is as close as possible to the maximum expected length of the read result (2 bytes code length + read code).

###### Parameter

The following table shows the parameters of the "Read_MV" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| LEN_DATA | Output | WORD | W#16#0 | Length of the read result ≙ 2 bytes code length + read code |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Read result  The length of the read code is located in bytes 0 and 1.  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Reset_Reader

###### Description

Using the "Reset_Reader" block, you can reset all reader types of the Siemens RFID systems as well as the optical readers. When using the "SIMATIC Ident" technology object, you can use the block for all Ident devices that are connected to an S7-1200/-1500. When you are not working with the technology object, you can only use the block for the devices SIMATIC RF120C and SIMATIC RF61xR/RF68xR. The "Reset_Reader" block does not have any device-specific parameters and is executed using the "EXECUTE" parameter.

You can find descriptions of other Reset blocks for operation with the communications modules or optical reader systems in the section "[Reset blocks](#reset-blocks)".

With the "Reset_Reader" block and the other reset blocks, you can interrupt any active Ident block at any time. These blocks are then ended with ""DONE = true" and "ERROR = false"".

###### Parameter

The following table shows the parameters of the "Reset_Reader" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Set_MV_Program

###### Description

You can use the "Set_MV_Program" block to change the program in a camera. The required program number is transferred using the "PROGRAM" parameter.

###### Parameter

The following table shows the parameters of the "Set_MV_Program" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| PROGRAMM | Input | BYTE | B#16#1 | Program number  Range of values: 0x01 ... 0x0F |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Write

###### Description

The "Write" block writes the user data from the "IDENT_DATA" buffer to the transponder. The physical address and the length of the data are transferred using the "ADDR_TAG" and "LEN_DATA" parameters. With the RF61xR/RF68xR readers, the block writes the data to memory bank 3 (USER area). Specific access to a certain transponder takes place with the optional "EPCID_UID" and "LEN_ID" parameters.

###### Parameter

The following table shows the parameters of the "Write" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| ADDR_TAG | Input | DWORD | DW#16#0 | Physical address on the transponder where the write starts. You will find more information on addressing in the section "[Transponder addressing of the Ident profile and Ident blocks, standard function for Ident systems manual](https://support.industry.siemens.com/cs/ww/en/ps/14971/man)".  With MV: Address is always 0. <sup>1)</sup> |
| LEN_DATA | Input | WORD | W#16#0 | Length of the data to be written |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF200, RF300, RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Data buffer with the data to be written.  With MV: The first byte encodes the corresponding MV command.<sup>1)</sup>  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |
| <sup>1)</sup> You can find additional information on working with optical reader systems in the operating instructions for "SIMATIC MV420 / SIMATIC MV440" and "SIMATIC MV500". |  |  |  |  |

#### Status blocks

This section contains information on the following topics:

- [Reader_Status](#reader_status)
- [Tag_Status](#tag_status)

##### Reader_Status

###### Description

The "Reader_Status" block reads status information from the reader or communication module (RF18xC/RF18xCI, RF166C as well as the reader RF360R (FW V2.0 and higher) with the "CM configuration_1" module). For the various reader families, there are different status modes that you can select using the "ATTRIBUTE" parameter.

###### Parameter

The following table shows the parameters of the "Reader_Status" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| ATTRIBUTE | Input | BYTE | B#16#81 | Identifier of the status modes / possible entries:  - RF200: 0x81 - RF300: 0x81, 0x86, 0xEF - RF61xR, RF68xR: 0x89 - MOBY U: 0x81, 0x84, 0x85 - MOBY D: 0x81 |
| - RF18xC, RF18xCI, RF166C, RF360R (ab FW V2.0): 0xA2 |  |  |  |  |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Result values depending on ATTRIBUTES  Note: You can create either an "Array_of_Byte" or a tag with one of the data types from the following table. |

###### Results

Apply the correct data type that is assigned to the ATTRIBUTE value at the "IDENT_DATA" input of the block so that the data can be correctly interpreted.

Note that the UDTs can only be used together with the blocks "Reader_Status" or "Tag_Status".

ATTRIBUTE "0x81" (data type "IID_READSTAT_81_RF2_3_U")

| Name | Type | Comment |
| --- | --- | --- |
| `status_info` | `BYTE` | `Reader status mode` |
| `hardware` | `CHAR` | `Type of hardware` |
| `hardware_version` | `WORD` | `Version of hardware`    `0 = RF310R, RF340R, RF350R; 1 = RF380R, RF260R; 2 = RF310R (ISO), RF210R, RF220R; 3 = RF380R (ISO), RF240R; 4 = RF340R (ISO), RF350R (ISO), RF250R; 5 = RF310R (ISO); 8 = MV400/MV500; A = RF310R Gen2, RF290R; B = RF340R Gen2; C = RF350R Gen2; D = RF380R Gen2; G = RF360R; M = RF280R RS422; N = RF280R RS232` |
| `loader_version` | `WORD` | `Version of loader` |
| `firmware` | `CHAR` | `Type of firmware` |
| `firmware_version_HB` | `BYTE` | `Version of firmware` |
| `firmware_version_LB` | `BYTE` | `Version of firmware` |
| `driver` | `CHAR` | `Type of driver` |
| `driver_version` | `WORD` | `Version of driver` |
| `interface` | `BYTE` | `Type of interface`    `0x01 = RS422; 0x02 = RS232` |
| `baud` | `BYTE` | `Baudrate`    `0x01 = 19.2 kBd; 0x03 = 57.6 kBd; 0x05 = 115.2 kBd; 0x0D = 921 kBd` |
| `reserved1` | `BYTE` | `Reserved` |
| `reserved2` | `BYTE` | `Reserved` |
| `reserved3` | `BYTE` | `Reserved` |
| `distance_limiting_SLG` | `BYTE` | `Distance limiting of Reader` |
| `multitag_SLG` | `BYTE` | `Multitag Reader` |
| `field_ON_control_SLG` | `BYTE` | `Field ON control` |
| `field_ON_time_SLG` | `BYTE` | `Field On time` |
| `sync_SLG` | `BYTE` | `Synchronization with Reader` |
| `status_ant` | `BYTE` | `Status of antenne`    `0x01 = on; 0x02 = off` |
| `stand_by` | `BYTE` | `Time of standby after command` |
| `MDS_control` | `BYTE` | `Presence mode` |

ATTRIBUTE "0x86" (data type "IID_READSTAT_86_RF300")

| Name | Type | Comment |
| --- | --- | --- |
| `status_info` | `BYTE` | `Reader status mode` |
| `FZP` | `BYTE` | `Error counter passive: distortion without communication` |
| `ABZ` | `BYTE` | `Dropout counter` |
| `CFZ` | `BYTE` | `Code error counter` |
| `SFZ` | `BYTE` | `Signature error counter` |
| `CRCFZ` | `BYTE` | `CRC-error counter` |
| `BSTAT` | `BYTE` | `Status of last command` |
| `ASMFZ` | `BYTE` | `Error counter for host interface (ASM)` |
| `reserved0` | `ARRAY [1..17]` | `Reserved` |

ATTRIBUTE "0x6F" (data type "IID_READSTAT_EF_RF300G2")

| Name | Type | Comment |
| --- | --- | --- |
| `status_info` | `SINT` | `Reader status mode` |
| `hardware` | `SINT` | `Type of hardware` |
| `hardware_version` | `INT` | `Version of hardware`    `0 = RF310R, RF340R, RF350R; 1 = RF380R, RF260R; 2 = RF310R (ISO), RF210R, RF220R; 3 = RF380R (ISO), RF240R; 4 = RF340R (ISO), RF350R (ISO), RF250R; 5 = RF310R (ISO); A = RF310R Gen2, RF290R; B = RF340R Gen2; C = RF350R Gen2; G = RF360R; M = RF280R RS422; N = RF280R RS232` |
| `reserved` | `INT` | `Reserved` |
| `loader` | `SINT` | `Type of loader` |
| `loader_version_1` | `SINT` | `Version of loader` |
| `loader_version_2` | `SINT` | `Version of loader` |
| `loader_version_3` | `SINT` | `Version of loader` |
| `loader_version_4` | `SINT` | `Version of loader` |
| `firmware` | `SINT` | `Type of firmware` |
| `firmware_version_1` | `SINT` | `Version of firmware` |
| `firmware_version_2` | `SINT` | `Version of firmware` |
| `firmware_version_3` | `SINT` | `Version of firmware` |
| `firmware_version_4` | `SINT` | `Version of firmware` |
| `reserved1` | `DINT` | `Reserved` |
| `driver` | `SINT` | `Type of driver` |
| `driver_version_1` | `SINT` | `Version of driver` |
| `driver_version_2` | `SINT` | `Version of driver` |
| `reserved2` | `INT` | `Reserved` |

ATTRIBUTE "0xA2" (data type "IID_CM_STATUS_A2") compatible with RF18xC/RF18xCI, RF166C and RF360R (FW V2.0 and higher)

| Name |  |  | Type | Comment |
| --- | --- | --- | --- | --- |
| `Status_info` |  |  | `BYTE` | `CM device status` |
| `hardware_version` |  |  | `BYTE` | `Version of hardware` |
| `firmware_version` |  |  | `ARRAY[1..4] of CHAR` | `Version of firmware` |
| `config ID` |  |  | `DWORD` | `Config_ID as unix timestamp` |
| `serial_number` |  |  | `ARRAY[1..16] of CHAR` | `Serial number` |
| `device_type` |  |  | `BYTE` | `Type of device`    `0x00 = RF185C; 0x01 = RF186C; 0x02 = RF188C; 0x03 = RF186CI; 0x04 = RF188CI; 0x06 = RF166C; 0x07 = RF360R` |
| `upload_request` |  |  | `BYTE` | `Upload request for configuration data` |
| `active_connections` |  |  | `BYTE` | `Active connections`    `0x00 = PLC; 0x01 = OPC UA; 0x02 = XML` |
| `io_mode` |  |  | `BYTE` | `Mode of in-/outputs`    `0x00 = Disabled; 0x01 = Single Input; 0x02 = Single Output; 0x03 = Support of IO link devices/hubs` |
| `low_voltage` |  |  | `BYTE` | `Low voltage warning`    `0x00 = OK; 0x01 = low voltage` |
| `reserved0` |  |  | `BYTE` | `Reserved` |
| `reserved1` |  |  | `BYTE` | `Reserved` |
| `number_serial_interfaces` |  |  | `BYTE` | `Number of serial interfaces supported by CM` |
| `serial_interface_data` |  |  | `ARRAY[1..4] of IID_IN_SERIAL_INTERFACE` |  |
|  | `serial_interface_data[1]` |  | `IID_IN_SERIAL_INTERFACE` |  |
|  |  | `connection_status` | `BYTE` | `Status of communication between reader and CM`    `0x00 = down; 0x01 = up` |
|  |  | `reader_type` | `CHAR` | `Type of connected reader`    `0 = RF310R, RF340R, RF350R; 1 = RF380R, RF260R; 2 = RF310R (ISO), RF210R, RF220R; 3 = RF380R (ISO), RF240R; 4 = RF340R (ISO), RF350R (ISO), RF250R; 5 = RF310R (ISO); 8 = MV400/MV500; A = RF310R Gen2, RF290R; B = RF340R Gen2; C = RF350R Gen2; D = RF380R Gen2; M = RF280R RS422; N = RF280R RS232` |
|  |  | `hardware_error` | `BYTE` | `Hardware error` |
|  |  | `reserved` | `BYTE` | `Reserved` |
|  | `serial_interface_data[2]` |  | `IID_IN_SERIAL_INTERFACE` |  |
|  | `serial_interface_data[3]` |  | `IID_IN_SERIAL_INTERFACE` |  |
|  | `serial_interface_data[4]` |  | `IID_IN_SERIAL_INTERFACE` |  |

ATTRIBUTE "0x89" (data type "IID_READSTAT_89_RF68xR") compatible with RF61xR/RF68xR

| Name | Type | Comment |
| --- | --- | --- |
| `status_info` | `BYTE` | `Reader status mode(Subcommand)` |
| `hardware_version` | `BYTE` | `Version of hardware` |
| `firmware_version` | `ARRAY[1..4] of CHAR` | `Version of firmware` |
| `config ID` | `DWORD` | `Unix timestamp` |
| `inventory_status` | `WORD` | `0 = inventory not active; 1 = inventory active; 2 = presence mode active` |
| `sum_of_filtered_tags` | `WORD` | `All filtered Tags` |
| `filtered_smoothing` | `WORD` | `Filtered Tags trough Smoothing` |
| `filtered_blacklist` | `WORD` | `Filtered Tags trough Blacklist` |
| `filtered_data-filter` | `WORD` | `Filtered Tags trough Data-Filter` |
| `filtered_RSSI_threshold` | `WORD` | `Filtered Tags trough RSSI Threshold` |
| `filtered_RSSI_delta` | `WORD` | `Filtered Tags trough RSSI Delta` |

ATTRIBUTE "0x84" (data type "IID_READSTAT_84_MOBY_U")

| Name | Type | Comment |
| --- | --- | --- |
| `status_info` | `BYTE` | `Reader status mode` |
| `number_MDS` | `BYTE` | `Range 1..24` |
| `UID` | `ARRAY [1..24] of DWord` |  |

**Values of the "ATTRIBUTE" parameter**

You will find more detailed information on the individual status modes in the manuals for the modes "FB 45" and "FB55".

The identifiers of the status modes correspond to the following identifiers in the other manuals:

|  |  |  |
| --- | --- | --- |
| 0x81 | ≙ | 0x01 |
| 0x82 | ≙ | 0x02 |
| 0x83 | ≙ | 0x03 |
| 0x85 | ≙ | 0x05 |
| 0x87 | ≙ | 0x07 |
| 0x88 | ≙ | 0x08 |
| 0x90 | ≙ | 0x10 |
| 0x91 | ≙ | 0x11 |
| 0x92 | ≙ | 0x12 |
| 0xA0 | ≙ | 0x20 |
| 0xA1 | ≙ | 0x21 |

##### Tag_Status

###### Description

The "Tag_Status" block reads the status information of the transponder. For the various transponder types and reader families, there are different status modes that you can select using the "ATTRIBUTE" parameter.

###### Parameter

The following table shows the parameters of the "Tag_Status" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| ATTRIBUTE | Input | BYTE | B#16#0 | Identifier of the status modes / possible entries:  - RF200: 0x83 - RF300 (RF300T): 0x04, 0x82 - RF300 (ISO): 0x83 - RF300 (Gen2): 0x83 - MOBY D: 0x83 <sup>1)</sup> - MOBY U: 0x80 |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Event values depending on attributes  Note: You can create either an "Array_of_Byte" or a tag with one of the data types from the following table. |
| <sup>1)</sup> SLG D10S only |  |  |  |  |

###### Results

Note that the UDTs can only be displayed when the blocks "Reader_Status" or "Tag_Status" are used.

ATTRIBUTE "0x04" ("IID_TAG_STATUS_04_RF300" data type)

| Name | Type | Comment |
| --- | --- | --- |
| `reserved` | `BYTE` |  |
| `status_info` | `BYTE` | `Tag status mode` |
| `UID` | `ARRAY [1..8] of BYTE` |  |
| `MDS_type` | `BYTE` | `Type of Tag`    `0x01 = Tag without FRAM; 0x02 = Tag with FRAM 8K; 0x03 = Tag with FRAM 32K; 0x04 = Tag with FRAM 64K; 0x05 = Tag with FRAM 128K; 0x06 = Tag with FRAM 256K` |
| `Lock_state` | `BYTE` | `Write Protection Status EEPROM` |
| `Reserved1` | `ARRAY[1..6] of BYTE` |  |

ATTRIBUTE "0x82" ("IID_TAG_STATUS_82_RF300" data type)

| Name | Type | Comment |
| --- | --- | --- |
| `reserved` | `BYTE` |  |
| `status_info` | `BYTE` | `Tag status mode` |
| `UID` | `ARRAY [1..8] of BYTE` |  |
| `LFD` | `BYTE` | `Magnetic flux density: correlation between limit-value` |
| `FZP` | `BYTE` | `Error counter passive: distortion without communication` |
| `FZA` | `BYTE` | `Error counter active: distortion during communication` |
| `ANWZ` | `BYTE` | `Presence counter: measure value for presence time` |
| `reserved1` | `ARRAY [1..3] of BYTE` |  |

ATTRIBUTE "0x83" ("IID_TAG_STATUS_83_ISO" data type)

| Name | Type | Comment |
| --- | --- | --- |
| `reserved` | `BYTE` |  |
| `status_info` | `BYTE` | `Tag status mode` |
| `UID` | `ARRAY [1..8] of BYTE` |  |
| `MDS_Type` | `BYTE` | `Type of Tag`    `0x00 = unknown; 0x03 = ISO: MDS D3xx, Infineon; 0x04 = ISO: MDS D4xx, Fujitsu; 0x05 = ISO: MDS D1xx, NXP; 0x06 = ISO: MDS D2xx, TI; 0x07 = ISO: MDS D261, STM; 0x08 = ISO: MDS D5xx, Fujitsu - 8k; 0x11 = RF300 - 0k; 0x12 = RF300 - 8k; 0x13 = RF300 - 32k; 0x14 = RF300 - 64k; 0x21 = MIFARE Classic - 1k, NXP; 0x22 = MIFARE Classic 1k, Infineon; 0x23 = MIFARE Classic 4k, NXP; 0x41 (A) = P2P RF310R Gen2; 0x42 (B) = P2P RF340R Gen2; 0x43 (C) = P2P RF350R Gen2; 0x44 (D) = P2P RF380R Gen2` |
| `IC_version` | `BYTE` | `Chip version` |
| `size_HB` | `BYTE` | `Size of Memory (high Byte)` |
| `size_LB` | `BYTE` | `Size of memory (low Byte)` |
| `lock_state` | `BYTE` | `Write protection status EEPROM` |
| `block_size` | `BYTE` | `Size of a block in addressable memory` |
| `number_of_block` | `BYTE` | `Number of blocks in addressable memory` |

ATTRIBUTE "0x80" ("IID_TAG_STATUS_80_MOBY_U" data type)

| Name | Type | Comment |
| --- | --- | --- |
| `UID` | `ARRAY [1..4] of BYTE` | `Unique indentifier (MDS-Number)` |
| `MDS_type` | `BYTE` | `Type of Tag` |
| `sum_subframe_access_1` | `BYTE` | `Sum of subframe access Byte 1` |
| `sum_subframe_access_2` | `BYTE` | `Sum of subframe access Byte 2` |
| `sum_subframe_access_3` | `BYTE` | `Sum of subframe access Byte 3` |
| `sum_subframe_access_4` | `BYTE` | `Sum of subframe access Byte 4` |
| `sum_searchmode_access_1` | `BYTE` | `Sum of search mode access Byte 1` |
| `sum_searchmode_access_2` | `BYTE` | `Sum of search mode access Byte 2` |
| `ST_date_Week` | `BYTE` | `Date of last sleep-time change (week of year)` |
| `ST_date_Year` | `BYTE` | `Date of last sleep-time change (year)` |
| `battery_left_1` | `BYTE` | `Battery power left (percent) Byte 1` |
| `battery_left_2` | `BYTE` | `Battery power left (percent) Byte 2` |
| `ST` | `BYTE` | `Actual sleep-time on MDS` |

**Values of the "ATTRIBUTE" parameter**

You will find more detailed information on the individual status modes in the manuals for the modes "FB 45" and "FB55".

The identifiers of the status modes correspond to the following identifiers in the other manuals:

|  |  |  |
| --- | --- | --- |
| 0x04 | ≙ | 0x01 |
| 0x82 | ≙ | 0x02 |
| 0x83 | ≙ | 0x03 |
| 0x84 | ≙ | 0x04 |
| 0x85 | ≙ | 0x05 |

#### Tag field blocks

This section contains information on the following topics:

- [Read_Tagfield](#read_tagfield)
- [Write_Tagfield](#write_tagfield)

##### Read_Tagfield

###### Description

Then "Read_Tagfield" block reads data from a tag field of the transponder and makes the formatted information available at the "IDENT_DATA" parameter. A "TO_TagLayout" technology object is transferred at the "TAGLAYOUT" parameter; the respective tag field is selected with the "TAGFIELD" parameter.

The technology object "TO_TagLayout" creates a "<Name of the TO>_Indexes" data block that can be used to select a symbolic tag field at the "TAGFIELD" parameter. In addition, a "<Name of the TO>_Datatypes" data type is made available that can be used to create a tag that contains all tag fields with the respective data types. It can be used to address a symbolic memory area for the tag field at the "IDENT_DATA" parameter.

The tag at the "IDENT_DATA" parameter must match the data type of the tag field. A tag of the type "Array of Byte" is always permitted. Specific access to a certain transponder takes place with the optional "EPCID_UID" and "LEN_ID" parameters.

You will find more information on the technology object "TO_TagLayout" in the section "[Technology object "TO_TagLayout](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_taglayout)"".

###### Parameter

The following table shows the parameters of the instruction "Read_Tagfield":

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAGFIELD | Input | INT | 1 | Selecting a tag field  The value corresponds to the number of the tag field in the technology object "TO_TagLayout".  For symbolic addressing, an element of the created data block "<Name of the TO>_Indexes" can be used. |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF200, RF300, RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| TAGLAYOUT | In/Out | TO_TAGLAYOUT | -- | Technology object "[TO_TagLayout](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_taglayout)" |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident)" of the Ident device |
| IDENT_DATA | In/Out | VARIANT | 0x00 | Data buffer in which the read data is stored.  Variable of the tag field data type or "ARRAY OF BYTE". |

---

**See also**

[Configuration/programming](#configurationprogramming-1)

##### Write_Tagfield

###### Description

The "Write_Tagfield" block writes data from the parameter "IDENT_DATA" to a tag field of the transponder. A "TO_TagLayout" technology object is transferred at the "TAGLAYOUT" parameter; the respective tag field is selected with the "TAGFIELD" parameter.

The technology object "TO_TagLayout" creates a "<Name of the TO>_Indexes" data block that can be used to select a symbolic tag field at the "TAGFIELD" parameter. In addition, a "<Name of the TO>_Datatypes" data type is made available that can be used to create a tag that contains all tag fields with the respective data types. It can be used to address a symbolic memory area for the tag field at the "IDENT_DATA" parameter.

The tag at the "IDENT_DATA" parameter must match the data type of the tag field. A tag of the type "Array of Byte" is always permitted. Specific access to a certain transponder takes place with the optional "EPCID_UID" and "LEN_ID" parameters.

You will find more information on the technology object "TO_TagLayout" in the section "[Technology object "TO_TagLayout](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_taglayout)"".

###### Parameter

The following table shows the parameters of the instruction "Write_Tagfield":

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAGFIELD | Input | INT | 1 | Selecting a tag field  The value corresponds to the number of the tag field in the technology object "TO_TagLayout".  For symbolic addressing, an element of the created data block "<Name of the TO>_Indexes" can be used. |
| LEN_DATA | Input | WORD | W#16#0 | Length of the data to be written |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF200, RF300, RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| TAGLAYOUT | In/Out | TO_TAGLAYOUT | -- | Technology object "[TO_TagLayout](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_taglayout)" |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident)" of the Ident device |
| IDENT_DATA | In/Out | VARIANT | 0x00 | Data buffer with the data to be written.  Variable of the tag field data type or "ARRAY OF BYTE". |

---

**See also**

[Configuration/programming](#configurationprogramming-1)

#### Advanced blocks

This section contains information on the following topics:

- [AdvancedCmd](#advancedcmd)
- [Config_Upload/-_Download](#config_upload-_download)
- [Inventory](#inventory)
- [Read_EPC_Mem](#read_epc_mem)
- [Read_TID](#read_tid)
- [Read_UID](#read_uid)
- [Set_Ant](#set_ant)
- [Set_Param](#set_param)
- [Write_EPC_ID](#write_epc_id)
- [Write_EPC_Mem](#write_epc_mem)

##### AdvancedCmd

###### Description

With the "AdvancedCmd" block, every command can be executed including commands not represented by other blocks. This general structure can be used for all commands and is intended only for trained users.

This block enables you to optionally execute a series of concatenated commands with only one single call of the block. To allow this, the block provides a CMD buffer for 100 commands. All chained commands must be entered starting at the first position in the buffer. For every chained command, the "chained bit" must also be set in the CMD structure. The "chained bit" is not set in the last command in the chain. You will find further information on the "chained bit" in the section "[Chaining](#chaining)".

The entire command structure must be specified in the "CMD" input parameter. You create the structure for the "CMD" parameter in a data block.

###### Parameter

The following table shows the parameters of the "AdvancedCmd" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| CMDSEL | Input | INT | 1 | Selection of the command to be executed "CMDREF";   1 ⇒ 1. Command, ...   The value of the "CMDSEL" parameter can never be > 100. |
| CMDREF | Input | ANY / VARIANT | -- | You will find a detailed description of the parameter in the sections:  - "[Overview of the commands](#overview-of-the-commands)" - "[Command structure](#command-structure)" |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Buffer for data to be written or read.   Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Config_Upload/-_Download

###### Description

Using the "Config_Upload" and "Config_Download" blocks, via the controller program you can read ("Config_Upload") or write ("Config_Download") the configuration of the communication modules RF166C as well as RF18xC/RF18xCI and the reader RF360R (FW V2.0 and higher) as well as RF61xR/RF68xR connected to this controller.

The configuration data is not interpretable data. Save the data on the controller so that it can be written to the reader again if a device is replaced. When multiple readers has the same configuration, you only have to save the configuration data once per reader type. A single backup can be copied to all identically configured readers during the download.

Bytes 6-9 (see table below) contain a configuration ID (CONFIG_ID) with a unique version identifier. With the configuration ID, when performing a "Config_Upload", you can check whether the configuration data read matches the configuration data stored on the controller. You can also use the device status to check the serial number to see if the device has been replaced.

The configuration data has the following structure:

Structure of the configuration data

| Byte | Name |
| --- | --- |
| 0 | Structure identifier (2 bytes) |
| 2 | Length information (4 bytes)  Length of the version identifier and parameter block |
| 6 | Version ID (≙ CONFIG_ID; 4 bytes)  Based on the identifier, you can uniquely identify the configuration. This is a time stamp in Linux format.   The time stamp indicates how many seconds have passed since January 1, 1979, 00:00 (midnight). The identifier is assigned when a configuration is generated. |
| 10 ... end "DATA" | Parameter block |

"Config_Upload/Config_Download" can be executed on every channel of the RF61xR/RF68xR. It is always the same configuration data that is transferred. The configuration data of the reader RF360R as well as the RF166C and RF18xC/RF18xCI communication modules can only be transferred via the "CM Configuration_1" module.

###### Parameter

The following table shows the parameters of the "Config_Upload" instruction:

| Parameter | Declaration | Data type | Default value | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| CONFIG_ID | Output | DWORD | 0x00 | Version identifier (4 bytes)  Based on the identifier, you can uniquely identify the configuration. This is a time stamp in Linux format.   The time stamp indicates how many seconds have passed since January 1, 1979, 00:00 (midnight). The identifier is assigned when a configuration is generated. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| DATA | Input/Output | ANY / VARIANT | -- | Data buffer for configuration data.  The real length of the data depends on the complexity of the configuration and the firmware version of the reader. We recommend a memory size of 4 KB for a standard configuration. If you use advanced reader configurations (filtering) or want to change the configuration in the future without needing to adapt the memory size of "DATA", we recommend a memory size of 8-16 KB.  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

The following table shows the parameters of the "Config_Download" instruction:

| Parameter | Declaration | Data type | Default value | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| DATA | In/Out | ANY / VARIANT | -- | Data buffer for configuration data.  The real length of the data depends on the complexity of the configuration and the firmware version of the reader. We recommend a memory size of 4 KB for a standard configuration. If you use advanced reader configurations (filtering) or want to change the configuration in the future without needing to adapt the memory size of "DATA", we recommend a memory size of 8-16 KB.  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Inventory

###### Description

The "Inventory" block activates the taking of inventories with RF600 readers (RF61xR/RF68xR). With a single inventory, acquisition cycles of all antennas with all polarizations are queried. For example, if 2 antennas are connected to a reader and each has 3 polarizations, then an inventory will include 6 acquisition cycles.

Note that the length of the data buffer ("IDENT_DATA") must correspond to at least the length of the maximum expected data. If more transponders are identified and data read out than have space in the assigned buffer length of "IDENT_DATA", the data of these transponders is lost. This reaction is indicated by the error "0xE7FE0400" (buffer overflow).

You can specify the duration of the inventories using the "DURATION" and "DUR_UNIT" parameters.

There are four different modes that you can select with the "ATTRIBUTE" parameter.

- At the start, a certain duration/number (period of time, number of inventories, number of "Observed" events or identified transponders) is specified. A distinction is made between the following options:

  - Duration

    Take inventories for a specified period of time
  - Number of inventories

    Take a specified number of inventories
  - Number of "Observed" events

    Take inventories until a specified number of transponders have been identified at the same time.

  Inventories are then taken by the reader for this time or number of inventories. When the specified time/number is reached, the block is ended and returns all identified transponders in "IDENT_DATA". In other words, other commands can only be executed when all inventories have been taken completely. The unit (time or number) is specified using "DUR_UNIT" and the value (time value or number) using "DURATION". This mode can be executed using the attributes "0x80" and "0x81". Depending on the attribute, more or less data is supplied about the identified transponders.
- With the attributes "0x86" (start "Presence_Mode") and "0x87" (end "Presence_Mode"), inventories can be taken permanently. The presence of a transponder can then always be queried using "PRESENCE" without needing to start the block with "EXECUTE". No information about the identified transponders is returned when the command executes!

  To obtain information about the identified transponders, use one of the two calls listed above (with time / number of inventories = 0).

  When this mode is active, commands relating to transponders are not executed immediately but only when a transponder is identified. This achieves shorter reaction times since the command is already pending when the transponder enters the antenna field.

  "Presence_Mode" is practical in the context of the "Repeat command" function.

The "NUMBER_TAGS" output parameter is used to output the number of identified transponders. With the attributes "0x80" and "0x81" on completion of the read operation, the sum of all identified transponders is displayed. With the attribute "0x86" the number of currently identified transponders is shown at the "NUMBER_TAGS" output parameter (max. 15),without needing to start the module with "EXECUTE".

###### Parameter

The following table shows the parameters of the "Inventory" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| ATTRIBUTE | Input | BYTE | B#16#0 | Selecting the status mode:  - MOBY U: 0x00 <sup>1)</sup> - RF600: 0x80, 0x81, 0x86, 0x87 |
| DURATION | Input | WORD | W#16#0 | RF61xR, RF68xR: Duration dependent on "DUR_UNIT"  Period of time or number of inventories or number of "Observed" events  Example:   - 0x00 ≙ no inventory - 0x01 ≙ one inventory |
| DUR_UNIT | Input | WORD | W#16#0 | RF61xR, RF68xR: Unit for "DURATION"  - 0x00 ≙ time [ms] - 0x01 ≙ inventories - 0x02 ≙ number of transponders that achieve the "Observed" state |
| NUMBER_TAGS | Output | INT | 0x00 | Number of transponders in the antenna field |
| LEN_DATA | Output | WORD | W#16#0 | Length of the valid data  During command processing = 0 |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#error-messages)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Data buffer for inventory data  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |
| <sup>1)</sup> In multitag mode only |  |  |  |  |

###### Event display

The following data types are not displayed in the TIA Portal for a newly created project in the selection list of the data types. To be able to use these data types, you must manually enter the name of the data type (e.g. "IID_IN_I_81"). After the first use, the data type is automatically listed in the project and also in the selection list.

###### Results for RF600

The number of "TAG_DATA[x]" elements of the data types of the ATTRIBUTE "0x80" and "0x81" depends on the number of transponders to be expected. For this reason, you need to assemble the receive buffer yourself. Note the following structure when creating the receive buffer "IDENT_DATA"/data type:

- The first element "NUM_MDS" is always of the type "WORD".
- The next element "TAG_DATA" is always of the type "ARRAY". The number of transponders to be expected ("n") must be entered in the "ARRAY".

Note that the data types created for the S7-1200/S7-1500 controllers cannot be created directly at the "IDENT_DATA" parameter. You can find information on the topic on the pages of "Siemens Industry Online Support".

The following tables show an example of the structure of the receive buffer "IDENT_DATA"/data type for the ATTRIBUTE "0x80" and "0x81". Since ATTRIBUTE "0x86" and "0x87" do not return any data, their structure is not further executed.

ATTRIBUTE "0x80"

| Name |  |  | Type | Comment |
| --- | --- | --- | --- | --- |
| `NUM_MDS` |  |  | `WORD` | `Number of MDS` |
| `TAG_DATA` |  |  | `ARRAY[1..n]of IID_IN_I_80` | `Length of EPC ID` |
|  | `TAG_DATA[1]` |  | `IID_IN_I_80` |  |
|  |  | `Reserved` | `BYTE` |  |
|  |  | `ID_Len` | `BYTE` | `Length of EPC ID` |
|  |  | `EPC_ID` | `ARRAY[1..62] of BYTE` | `EPC-ID` |
|  |  | `tagPC` | `WORD` |  |
|  | `TAG_DATA[2]` |  | `IID_IN_I_80` |  |
|  | `...` |  | `...` |  |
|  | `TAG_DATA[n]` |  | `IID_IN_I_80` |  |

ATTRIBUTE "0x81"

| Name |  |  | Type | Comment |
| --- | --- | --- | --- | --- |
| `NUM_MDS` |  |  | `WORD` | `Number of MDS` |
| `TAG_DATA` |  |  | `ARRAY[1..n] of IID_IN_I_81` |  |
|  | `TAG_DATA[1]` |  | `IID_IN_1_81` |  |
|  |  | `reserved` | `BYTE` |  |
|  |  | `ID_LEN` | `BYTE` | `EPC length` |
|  |  | `EPC_ID` | `ARRAY[1..62]of BYTE` | `EPC-ID` |
|  |  | `tagPC` | `WORD` |  |
|  |  | `RSSI` | `BYTE` | `RSSI value` |
|  |  | `MaxRSSI` | `BYTE` | `highest RSSI value` |
|  |  | `MinRSSI` | `BYTE` | `lowest RSSI value` |
|  |  | `channel` | `BYTE` | `channel; 1..15_ESTI; 1..53:FCC` |
|  |  | `antenna` | `BYTE` | `antenna; bit coded; Bit 0 = antenna 1; Bit 1 = antenna 2;  Bit 2 = antenna 3; Bit 3 = antenna 4` |
|  |  | `polarization` | `BYTE` | `polarizatuin of antenna; 0=undefined; 1=circular; 2=vertical linear; 3=horizontal` |
|  |  | `time` | `Time_OF_Day` | `S7 timestamp` |
|  |  | `power` | `BYTE` | `power in dBm` |
|  |  | `filterDataAvailable` | `BYTE` | `0=false; 1=true` |
|  |  | `Inventoried` | `WORD` | <sup>1)</sup> |
|  | `TAG_DATA[2]` |  | `IID_IN_1_81` |  |
|  | `...` |  | `...` |  |
|  | `TAG_DATA[n]` |  | `IID_IN_1_81` |  |
| <sup>1)</sup>Indicates how often the transponder was identified via the air interface before it changed to the "Observed" status. |  |  |  |  |

###### Results for MOBY U

ATTRIBUTE "0x00" (data type "IID_INVENT_00_MOBY_U")

| Name |  |  |  | Type | Comment |
| --- | --- | --- | --- | --- | --- |
| `number_MDS` |  |  |  | `WORD` | `Number of MDS` |
| `UID_length` |  |  |  | `WORD` | `length of UID` |
| `UID` |  |  |  | `ARRAY[1..12] of IID_IN_I_8BYTE` |  |
|  | `UID[1]` |  |  | `IID_IN_I_8BYTE` |  |
|  |  | `UID` |  | `ARRAY[1..8] of BYTE` |  |
|  |  |  | `UID[1]` | `BYTE` |  |
|  |  |  | `UID[2]` | `BYTE` |  |
|  |  |  | `UID[3]` | `BYTE` |  |
|  |  |  | `UID[4]` | `BYTE` |  |
|  |  |  | `UID[5]` | `BYTE` |  |
|  |  |  | `UID[6]` | `BYTE` |  |
|  |  |  | `UID[7]` | `BYTE` |  |
|  |  |  | `UID[8]` | `BYTE` |  |
|  | `UID[2]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[3]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[4]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[5]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[6]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[7]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[8]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[9]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[10]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[11]` |  |  | `"IID_IN_I_8BYTE"` |  |
|  | `UID[12]` |  |  | `"IID_IN_I_8BYTE"` |  |

---

**See also**

[Configuration/programming](#configurationprogramming)

##### Read_EPC_Mem

###### Description

The "Read_EPC_Mem" block reads data starting at address 4 from the EPC memory of the RF600 transponder. Access is to bank 1 as of the start address 4. The length of the EPC memory to be read out is specified by the "LEN_DATA" parameter.

###### Parameter

The following table shows the parameters of the "Read_EPC_Mem" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| LEN_DATA | Input | WORD | W#16#0 | Length of the EPC memory to be read out (1 ... 62 bytes) |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Data buffer in which the read EPC memory data is stored.  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Read_TID

###### Description

The "Read_TID" block reads data from the TID memory area (Tag Identification Memory Bank) of the RF600 transponder. The length of the TID to be read is specified by the "LEN_DATA" parameter. The length of the TID varies depending on the transponder and can be found in the transponder data sheet.

###### Parameter

The following table shows the parameters of the "Read_TID" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| LEN_DATA | Input | WORD | W#16#4 | Length of the TID memory to be read |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Read TID  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Read_UID

###### Description

The "Read_UID" block reads the UID of an HF transponder. The UID always has a fixed length of 8 bytes.

###### Parameter

The following table shows the parameters of the "Read_UID" instruction:

| Parameter | Declaration | Data type | Default value | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | UID  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Set_Ant

###### Description

With the aid of the "Set_Ant" block, you can turn antennas on or off. The "Set_Ant_RF300" block can also be used for RF200, MOBY D and MOBY U.

###### Parameter

The following table shows the parameters of the "Set_Ant_RF300" instruction:

| Parameter | Declaration | Data type | Default value | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| ANTENNA | Input | BOOL | FALSE | FALSE = turn antenna off TRUE = turn antenna on |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Set_Param

###### Description

Using the "Set_Param" block, you can change UHF parameters (e.g. the antenna power) on an RF61xR/RF68xR, as well as the date/time parameters of an RF18xC/RF18xCI, RF166C or RF360R (FW V2.0) during runtime.

> **Note**
>
> **Settings saved only temporarily**
>
> Note that the parameters in the "Set_Param" block are only stored temporarily. If the power for the module is interrupted, the stored values are lost and must be set again.

###### Parameter

The following table shows the parameters of the "Write" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| PARMID | Input | DWORD | 0x00 | Parameter identifier |
| VALUE | Input | DWORD | 0x00 | Parameter value |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

###### Values for "PARMID" and "VALUE"

Depending on the Ident device used, the following parameters can be read out with the aid of this block.

Parameter values

| PARMID  (hex) | PARMID  (ASCII) | Parameter | VALUE |
| --- | --- | --- | --- |
| 0x41315057 | A1PW | Antenna 01: Radiated power | Range of values: 0.5 ... 33  Increment: 0.25  Radiated power of the antenna in [dBm].  Bytes 1 and 2 are not used, byte 3 represents the integer and byte 4 the decimal place.  Example: A radiated power of 10.25 dBm represents a "VALUE" of "0x0A19". |
| 0x41325057 | A2PW | Antenna 02: Radiated power |  |
| 0x41335057 | A3PW | Antenna 03: Radiated power |  |
| 0x41345057 | A4PW | Antenna 04: Radiated power |  |
| 0x41315452 | A1TR | Antenna 01: RSSI threshold | Range of values: 0 ... 255  Threshold value for RSSI.   Transponders with lower values are discarded. Value without unit without a direct relationship with the radiated power. |
| 0x41325452 | A2TR | Antenna 02: RSSI threshold |  |
| 0x41335452 | A3TR | Antenna 03: RSSI threshold |  |
| 0x41345452 | A4TR | Antenna 04: RSSI threshold |  |
| 0x5331444C | S1DL | Read point 01: RSSI delta | Range of values: 0 ... 255  Difference for RSSI values.   Transponders with lower values relative to the transponder with the highest RSSI value are discarded. Value without unit without a direct relationship with the radiated power. |
| 0x5332444C | S2DL | Read point 02: RSSI delta |  |
| 0x5333444C | S3DL | Read point 03: RSSI delta |  |
| 0x5334444C | S4DL | Read point 04: RSSI delta |  |
| 0x4131504F | A1PO | Antenna 01: Polarization | Range of values: 0, 1, 2, 4  Polarization of the antenna (for intelligent antennas e.g. internal antenna RF685R)  - 0: default, undefined - 1: circular - 2: vertical linear - 4: horizontal linear   Input is bit coded. Combinations are possible (adding values). |
| 0x4132504F | A2PO | Antenna 02: Polarization |  |
| 0x4133504F | A3PO | Antenna 03: Polarization |  |
| 0x4134504F | A4PO | Antenna 04: Polarization |  |
| 0x52364353 | R6CS | Modulation scheme | Range of values: 32, 33, 34, 35, 37, 65  Modulation scheme of the read point  Specification of which transponder types are identified (ISO 18000-63/-62).  - 32: Tx: 40 Kbps / Rx: 40 Kbps / FM0 - 33: Tx: 40 Kbps / Rx: 62:5 Kbps / Miller4 - 34: Tx: 40 Kbps / Rx: 75 Kbps / Miller4 - 35: Tx: 80 Kbps / Rx: 62:5 Kbps / Miller4 - 37: Tx: 80 Kbps / Rx: 400 Kbps / FM0 - 65: Tx: 40 Kbps / Rx: 40 Kbps / ISO 18000-62 |
| 0x57544348 | WTCH | Date and time | Range of values: 01.01.2000 00:00 a.m. ... 19.01.2038 3:14 a.m.  01.01.2000 01:00 a.m. ≙ 946684800  Date and time (UTC)  Time in seconds since 01/01/1970; Setting of the internal reader/CM clock, whereby the date and time are set. |
| 0x57544F44 | WTOD | Time | Range of values: 0:00 – 23:59 p.m.  S7 time (TOD, UTC)  Milliseconds since midnight; Setting of the internal reader/CM clock, whereby only the time is changed but not the date. |
| 0x57444154 | WDAT | Date | Range of values:  01.01.2000 ... 18.01.2038  S7 date   Days since 01/01/1990; Setting of the internal reader/CM clock, whereby only the date is changed and not the time. |

##### Write_EPC_ID

###### Description

The "Write_EPC_ID" block overwrites the EPC-ID of the RF600 transponder and adapts the length of the EPC-ID in the memory of the transponder. The new EPC-ID length to be written is specified with the "LEN_ID_NEW" parameter and the previous EPC-ID is specified using the "LEN_ID" and "EPCID_UID" parameters.

Make sure that when you execute the block only one transponder is located in the antenna field. This ensures that the identification when writing the ID is unique. If there is more than one transponder in the antenna field, a negative response is returned.

###### Parameter

The following table shows the parameters of the "Write_EPC_ID" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| LEN_ID_NEW | Input | BYTE | W#16#0C | Length of the current EPC-ID |
| LEN_ID | Input | BYTE | B#16#0 | Length of the previous EPC-ID |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Previous EPC ID |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | Any / Variant | 0x00 | Current EPC ID  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

##### Write_EPC_Mem

###### Description

The "Write_EPC_Mem" block overwrites the EPC memory of the RF600 transponder starting at address 4. The length of the EPC memory to be overwritten is specified by the "LEN_DATA" parameter.

###### Parameter

The following table shows the parameters of the "Write_EPC_Mem" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| LEN_DATA | Input | WORD | W#16#0 | Length of the EPC memory to be overwritten (1 ... 62 bytes) |
| LEN_ID | Input | BYTE | B#16#0 | Length of the EPC-ID/UID  Default value: 0x00 ≙ unspecified single tag access (RF61xR, RF68xR) |
| EPCID_UID | Input | ARRAY[1...62] OF BYTE | 0x00 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| PRESENCE | Output | BOOL | FALSE | This bit indicates the presence of a transponder. The displayed value is updated each time the block is called. This parameter does not exist in blocks specific to optical reader systems. |
| HW_CONNECT | In/Out | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| IDENT_DATA | In/Out | ANY / VARIANT | 0x00 | Data buffer with the EPC memory data to be overwritten.  Note: S7-1200/S7-1500: For Variant, currently only an "Array_of_Byte" with a variable length can be created. For Any, other data types/UDTs can also be created. |

#### Reset blocks

This section contains information on the following topics:

- [Reset blocks](#reset-blocks-1)
- [Reset_MOBY_D](#reset_moby_d)
- [Reset_MOBY_U](#reset_moby_u)
- [Reset_MV](#reset_mv)
- [Reset_RF200](#reset_rf200)
- [Reset_RF300](#reset_rf300)
- [Reset_RF600](#reset_rf600)
- [Reset_Univ](#reset_univ)

##### Reset blocks

The reset blocks described in this section are required when you want to operate the optical reader systems or the communication modules without the "SIMATIC Ident" technology object. In order to use these blocks with the RF120C, if you have selected the "Parameters via FB / optical readers" setting in the device configuration.

When using the technology object, you can use the specific reset blocks to change reader parameter assignments other than those set in the technology object during runtime.

Remember that the default value is used automatically for parameters if you do not transfer a value.

##### Reset_MOBY_D

###### Parameter

The following table shows the parameters of the "Reset_MOBY_D" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAG_CONTROL | Input | BOOL | TRUE | Presence check |
| TAG_TYPE | Input | BYTE | 0x01 | Transponder type:   - 0x01 = every ISO transponder |
| RF_POWER | Input | BYTE | 0x00 | Output power  RF power from 0.5 W to 10 W in increments of 0.25 W  (range of values: 0x02 ... 0x28) |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Reset_MOBY_U

###### Parameter

The following table shows the parameters of the "Reset_MOBY_U" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAG_CONTROL | Input | BOOL | TRUE | Presence check |
| DISTANCE | Input | BYTE | 0x23 | Range limitation (range of values: 0x02 ... 0x23 or 0x82 ... 0xA3 for reduced transmit power) |
| MULTITAG | Input | BYTE | 0x01 | Maximum number of transponders that can be processed at the same time in the antenna field.  (Range of values: 0x01 ... 0x12) |
| SCAN_TIME | Input | BYTE | 0x00 | Scanning time: Standby time of the transponder (range of values: 0x00 ... 0xC8) |
| FCON | Input | BYTE | 0x00 | field_ON_control: BERO mode (range of values: 0x00 ... 0x03) |
| FTIM | Input | BYTE | 0x00 | field_ON_time: Time for BERO mode (range of values: 0x00 ... 0xFF) |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Reset_MV

###### Description

To reset cameras of the optical reader systems, call the block and activate the "EXECUTE" parameter.

###### Parameter

The following table shows the parameters of the "Reset_MV" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| PROGRAM | Input | BYTE | 0x00 | Program selection  - B#16#0: Reset without program selection or in the case of diagnostics, the error code for "IN_OP = 0" is shown at the "STATUS" output parameter. - B#16#1 ... B#16#0F: Number of the program to be started  ⇒ Reset with program selection (as of firmware V5.1 of the MV4x0) |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Reset_RF200

###### Parameter

The following table shows the parameters of the "Reset_RF200" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAG_CONTROL | Input | BYTE | 0x01 | Presence check |
| TAG_TYPE | Input | BYTE | 0x01 | Transponder type:   - 0x01 = every ISO transponder - 0x03 = MDS D3xx - optimization |
| RF_POWER | Input | BYTE | 0x04 | Output power; only relevant for RF290R  RF power from 0.5 W to 5 W in increments of 0.25 W (range of values: 0x02 ... 0x14).  Default value 0x04 ≙ 1 W. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Reset_RF300

###### Parameter

The following table shows the parameters of the "Reset_RF300" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAG_CONTROL | Input | BYTE | 0x01 | Presence check  - 0x00 = Off - 0x01 = On - 0x04 = Presence (antenna is off. The antenna is turned on only when a Read or Write command is sent.) |
| TAG_TYPE | Input | BYTE | 0x00 | Transponder type:   - 0x00 = RF300 transponder - 0x01 = every ISO transponder |
| RF_POWER | Input | BYTE | 0x00 | Output power; only relevant for RF380R  RF power from 0.5 W to 2 W in increments of 0.25 W (range of values: 0x02 ... 0x08).  Default value: 0x00 ≙ 1.25 W.  This setting is not necessary with the RF380R readers of the 2nd generation (6GT2801-3BAx0) because the power limits are optimized automatically depending on the reader-transponder distance. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

##### Reset_RF600

###### Parameter

The following table shows the parameters of the "Reset_RF600" (RF620R/RF630R) instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| TAG_CONTROL | Input | BOOL | TRUE | Presence check |
| RADIO_PROFILE | Input | BYTE | 0x01 | Scanning_Time: Wireless profile according to EPC Global  (range of values: 0x01 ... 0x09 depending on the reader variant) |
| POWER_ANT1 | Input | BYTE | 0x00 | Transmit power for antenna 1 or internal antenna  (range of values: 0x00 ... 0x0F) |
| POWER_ANT2 | Input | BYTE | 0x00 | Transmit power for antenna 2 or external antenna  (range of values: 0x00 ... 0x0F) |
| UID_HANDLE | Input | BOOL | FALSE | Meaning of the UID in the command:   True = Handle ID, only the least significant 4 bytes of the UID are evaluated;   False = UID/EPC-ID with a length of 8 bytes |
| BLACK_LIST | Input | BOOL | FALSE | True = Activate Black List |
| TAG_HOLD | Input | BOOL | FALSE | True = Activate Tag Hold |
| PARAM_SET | Input | BYTE | 0x00 | Field_ON_Control  (0 = fast; value range: 0x00, 0x02) |
| CHANNEL_PLAN | Input | BYTE | 0x0F | Field_ON_Time  (value range: 0x00 ... 0x0F; ETSI only) |
| MULTITAG | Input | BYTE | 0x01 | Maximum number of transponders that can be processed at the same time in the antenna field.  (Range of values: 0x01 ... 0x50) |
| ISTM | Input | BOOL | FALSE | TRUE = activate intelligent single tag mode |
| SCANNING_MODE | Input | BOOL | FALSE | TRUE = Activate Scanning mode <sup>1)</sup> |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |
| <sup>1)</sup> Is not currently possible with the Ident blocks. |  |  |  |  |

##### Reset_Univ

###### Description

The "Reset_Univ" block is a universal reset block with which all identification systems can be reset.

###### Parameter

The following table shows the parameters of the "Reset_Univ" instruction:

| Parameter | Declaration | Data type | Default values | Description |
| --- | --- | --- | --- | --- |
| EXECUTE | Input | BOOL | FALSE | There must be a positive edge at this input before the block will execute the command. |
| PARAM | Input | ARRAY[1...16] OF BYTE | 0x00 | Data for reset frame  The data to be set here can be made available by Support when necessary for special settings. |
| DONE | Output | BOOL | FALSE | The job was executed. If the result is positive, this parameter is set. |
| BUSY | Output | BOOL | FALSE | The job is being executed. |
| ERROR | Output | BOOL | FALSE | The job was ended with an error. The error code is indicated in "STATUS". |
| STATUS | Output | DWORD | FALSE | Display of the [error message](#error-messages) if the "ERROR" bit was set. |
| HW_CONNECT | Input/Output | TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident-1)" of the Ident device |
| IID_HW_CONNECT | -- | Global parameter of the type "[IID_HW_CONNECT](#configurationprogramming)" to address the channel/reader and to synchronize the blocks. |  |  |

Structure of the "PARAM" parameter

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Byte** | 1 | 2...5 | 6 | 7...8 | 9 | 10 | 11 | 12 | 13...14 | 15 | 16 |
| **Value**   **(RF200, RF300, MOBY U/D)** | 0x04 | 0x00 | 0x0A | 0x00 | scanning_ time | param | option_1 | distance_ limiting | No. of transponders | field_on_ control | field_on_ time |
| **Value**   **(Freeport)** | 0x04 | 0x00 | 0x0A | 0x00 | 0x00 | 0x00 | option_1 | 0x00 | 0x00 | 0x00 | 0x00 |

### Programming the Ident profile

This section contains information on the following topics:

- [Structure of the Ident profile](#structure-of-the-ident-profile)
- [Data structure of the Ident profile](#data-structure-of-the-ident-profile)
- [Configuration/programming](#configurationprogramming-1)
- [Commands of the Ident profile](#commands-of-the-ident-profile)

#### Structure of the Ident profile

> **Note**
>
> **Parallel operation using Ident blocks and Ident profile is not possible**
>
> Note that the CM or reader cannot be operated at the same time using the Ident blocks and the Ident profile.

The blocks described in the section"[Programming Ident blocks](#programming-ident-blocks)" represent a simplified interface of the Ident profile. If the functionality available with the blocks is not adequate for your application, you can use the Ident profile as an alternative. Using the Ident profile, you can set complex command structures and work with command repetition. The following graphic shows the Ident profile including the commands that can be implemented with it.

> **Note**
>
> **Ident profile for trained users**
>
> The Ident profile is a complex block containing all the functionality of the Ident blocks. The Ident profile was developed specially for trained block users who want to configure complex functions with their own blocks. For untrained users, we recommend using the Ident blocks.

![The input parameters of the Ident profile](images/132210569739_DV_resource.Stream@PNG-en-US.png)

The input parameters of the Ident profile

> **Note**
>
> **Working with multiple channels/read points**
>
> When you work with multiple channels/read points, you must ensure that the block is called with a separate instance DB for each channel/read point.

##### Interface description

Input parameter

| Input parameter | Data type | Default value | Meaning |
| --- | --- | --- | --- |
| HW_CONNECT | IID_HW_CONNECT | -- | Global parameter of the type "IID_HW_CONNECT" to address the channel or the read point and to synchronize the blocks.  The addressing is as described in the section "[Configuration/programming](#configurationprogramming-1)". |
| TO_IDENT | -- | Technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident)" of the Ident device |  |
| EXECUTE | BOOL | FALSE | TRUE = triggers a new command   Before starting you need to set the command and the corresponding parameters in the memory linked to "CMDREF". |
| RPTCMD | BOOL | FALSE | TRUE = Repeat the currently executed command or the command to be executed next by the reader / communication module. |
| SRESET | BOOL | FALSE | TRUE = Cancellation of the command currently processed on the reader/communication module |
| INIT | BOOL | FALSE | TRUE = Reader/communication module executes a restart and is re-assigned parameters  The first command that is sent to a reader / communication module must always be sent with an "INIT". |
| CMDDIM | INT | 10 | Number of commands in the parameter "CMDREF" |
| CMDSEL | INT | 0 | Selection of the command to be executed "CMDREF";   1 ⇒ 1. command, ...  The value of the "CMDSEL" parameter can never be higher than the value of the "CMDDIM" parameter. |
| CMDREF | ARRAY[1...n] of IID_CMD_STRUCT | -- | Command field  The field can hold up to 100 commands. The commands are complex variables of the type "IID_CMD_STRUCT". You can find more information on "CMDREF" in the section "[Overview of the commands](#overview-of-the-commands)". |
| TXREF | ARRAY[1...n] of BYTE | -- | Reference to global memory area for send data.  The memory area can be shared with other block instances. The value "n" of the individual blocks is variable and can be up to 32 KB in size. |
| RXREF | ARRAY[1...n] of BYTE | -- | Reference to global memory area for receive data.  The memory area can be shared with other block instances. The value "n" of the individual blocks is variable and can be up to 32 KB in size. |

Output parameter

| Output parameter | Data type | Default value | Meaning |
| --- | --- | --- | --- |
| DONE | BOOL | FALSE | TRUE = Command was executed free of errors. |
| ERROR | BOOL | FALSE | TRUE = Error was detected.  The error is output in the "STATUS" parameter. The bit is reset automatically when a new command is started. |
| STATUS | DWORD | FALSE | Warning and error  If "ERROR = TRUE" or "WARNING = TRUE", the error or warning information is contained in the "STATUS" parameter. For more information, refer to the section "[Error messages](#error-messages)". |
| WARNING | BOOL | FALSE | TRUE = Warning was detected.  The warning is output in the "STATUS" parameter. If the "ERROR" parameter is not set at the same time, the data was correctly processed. The bit is reset automatically when a new command is started. |
| BUSY | BOOL | FALSE | TRUE = the block is executing a command.  Other commands except for "INIT" and "SRESET" cannot be started. |
| RPTACT | BOOL | FALSE | TRUE = "RPTCMD" is active  The acknowledgment bit shows that the "Repeat mode" of the CM/reader is active. |
| ERR_IREQ | BOOL | FALSE | TRUE = An error has occurred on the communications module or reader (e.g. on start-up of the reader, connection termination or with RF61xR, RF68xR on antenna errors or configuration changes) |
| TPC | BOOL | FALSE | Transponder Presence Changed (only with active "Presence_Mode")  TRUE = A new transponder enters the antenna field of the reader or a transponder has left the antenna field.  The parameter is set to "FALSE" after the successful execution of the next "INVENTORY" (0x80, 0x81, 0x87) or "INIT" command. |
| TP | BOOL | FALSE | Transponder Presence   TRUE = There is a transponder in the antenna field of the reader.  Note on the Freeport protocol: If no "Read" has been sent yet, the presence bit ("TP" or "ANZ_MDS_present") informs that new data has been received and is available to be fetched from the communication module with a "Read" command. |
| UIN0 | BOOL | FALSE | With RFID readers, the number of transponders in the antenna field is indicated. UIN0 ... UIN3 can be interpreted as binary values.  Example:  UIN3 = 0; UIN2 = 0; UIN1 = 1; UIN0 = 1  ⇒ 3 transponders  With optical reader devices, the various states of the reader are displayed.  - UIN0: Corresponds to "IN_OP" bit of the reader - UIN1: Corresponds to "RDY" bit of the reader - UIN2 + UIN3: These two bits are interpreted as an unsigned value (bit 2 is the less significant bit) that represents the number of available decoded codes. If the value = 3, three or more decoded codes are available. |
| UIN1 | BOOL | FALSE |  |
| UIN2 | BOOL | FALSE |  |
| UIN3 | BOOL | FALSE |  |
| TRLEN | INT | 0 | Number of data elements received after successful execution of the command. |

#### Data structure of the Ident profile

Each time the Ident profile is called, you need to supply the parameters ("HW_CONNECT", "CMDREF", "TXREF" and "RXREF") with values as described in section "[Programming the Ident profile](#programming-the-ident-profile)".

The call for the Ident profile is always via the input parameter "HW_CONNECT" and the "IN/OUT" parameters "CMDREF", "TXREF" and "RXREF". All three parameters need to be created in a data block. The relationship between the three "IN/OUT" parameters is described in greater detail below:

- CMDREF (command buffer):

  - Array[1...n] of IID_CMD_STRUCT
- TXREF (send buffer):

  - Array[1...n] of Byte
  - For Any, other data types/UDTs can also be created.
- RXREF (receive buffer):

  - Array[1...n] of Byte
  - For Any, other data types/UDTs can also be created.

![Data structure example of the Ident profile](images/63784234123_DV_resource.Stream@PNG-en-US.png)

Data structure example of the Ident profile

**Explanation of the data structure example**

- CMDREF[1]:

  Command "WRITE-CONFIG", OFFSETBUFFER = 0

  At the "CMDREF[1]" point you need to set the "WRITE-CONFIG" command so that the "INIT/Reset" is correctly executed.
- CMDREF[2]:

  Command "WRITE", OFFSETBUFFER = 15
- CMDREF[3]:

  Command "READ", OFFSETBUFFER = 0

If the "CMDREF[2]" command is selected, a write command is started and the data to be written is fetched starting at byte 15 of the "TXREF" parameter. If the "CMDREF[3]" command is selected, the read data is stored starting at byte 0 in the "RXREF" parameter.

#### Configuration/programming

You can use the technology object "[TO_Ident](SIMATIC%20Ident%20%28TFIdentMainenUS%29.md#technology-object-to_ident)" or not use it for parameter assignment of the Ident blocks / Ident profile. If you do not use the technology object for parameter assignment, you need the data type "IID_HW_CONNECT". Note that this data type is only contained in library versions < V5.0. SIMATIC S7-300/400 controllers are not compatible with the technology object.

Before you can start parameter assignment of the blocks, you first need to create a variable of the PLC data type "IID_HW_CONNECT". The Ident system or a channel of the Ident system is addressed using the "IID_HW_CONNECT" PLC data type.

##### Addressing the Ident devices

When working with all the instructions/blocks, you require the "IID_HW_CONNECT" data type to address the reader. Setting the command parameters for the Ident profile is handled by the Ident blocks. The Ident profile and the "AdvancedCMD" block also require the "IID_CMD_STRUCT" data type for the parameter assignment of the individual commands. Depending on whether you work with the Ident profile or the Ident blocks, you need to link in and assign parameters for these data types as described in the following sections.

##### Configuring a tag of the "IID_HW_CONNECT" data type

**Follow the steps below to set the parameters for the tag of the "IID_HW_CONNECT" data type for a channel:**

1. Create a new tag in a data block or in the static area of a function block.

   ![Creating a data block](images/66928573579_DV_resource.Stream@PNG-en-US.PNG)

   Creating a data block
2. Specify the address data of the Ident device or the channel.

   - HW_ID: Hardware identifier of the module (only with S7-1200 and S7-1500)
   - CM_CHANNEL: Channel within a module
   - LADDR: I/O address of the module

   You can read out the values of the "HW_ID" and "LADDR" parameters in the device configuration in the properties of the communications module/reader. Enter the parameter values you have read out in the "Start value" column of the corresponding parameters. Reading out parameter values is described below.

**Follow the steps below to read out the parameter values "HW_ID" and "LADDR" for a channel:**

1. Open the network view and double-click on the communications module.

   Reaction: TIA switches to the device view and the properties window of the CM opens.
2. In the "Device overview" tab, select the relevant module.

   The I/O address displayed in the tab corresponds to "LADDR".

   Note that the input and output address must have the same value.
3. In the "Properties > System constants" tab, you will find the hardware identifier that corresponds to the "HW_ID".

   ![The "Hardware identifier" parameter](images/114079829771_DV_resource.Stream@PNG-en-US.png)

   The "Hardware identifier" parameter
4. Transfer the values of "LADDR" and "HW_ID" to the PLC data type "IID_HW_CONNECT" of the reader for which you want to set parameters.

> **Note**
>
> **Setting the user mode**
>
> In the properties of the communication module/reader, make sure that you assign the value "RFID standard profile" to the "User mode" parameter and select the suitable MOBY mode.

With all other communications modules/readers, you will find the two parameters directly in the properties of the module.

The "IID_HW_CONNECT" data type has now been created for a channel. Repeat these steps for every other reader/channel. If you want to use a different channel of the reader/CM, set this using the "CM_CHANNEL" parameter. The "HW_ID" and "LADDR" parameters remain the same for all channels/readers/antennas. With an RF166C or RF18xC/RF18xCI communications module, each reader is assigned to a separate module and has its own "HW_ID" and "LADDR". Please note that the value of the channel always needs to be "1".

All required function blocks and data types are now included in your project and you can now start programming. The "IID_HW_CONNECT" data type has also been created and addressed. You can now start programming the blocks.

> **Note**
>
> **Configure "IID_CMD_STRUCT"**
>
> If you work with the Ident profile or with the "AdvancedCmd" block, you also need to create a further element with the data type "IID_CMD_STRUCT" (Array [1...n]) in the data block you have already created.

##### Creating blocks

Before data can be exchanged with a reader (e.g. reading/writing data), the relevant Ident device must be reset once. When using the Ident blocks, you can use a reset block (e.g. "Reset Reader") for this. An appropriately configured "WRITE-CONFIG" command must be executed when using the Ident profile.

**Requirement**

The "IID_HW_CONNECT" data type has been assigned parameters.

**Follow the steps below to link in a block and to set the call parameters:**

1. Open the program block you have created by double-clicking in the "Project tree > Program blocks" tab.
2. Drag the required block from the instruction register into the program block.
3. Enter the tag you created earlier in the "HW_CONNECT" input parameter.

The block is called and connected to the relevant channel.

> **Note**
>
> **Working with multiple channels/read points**
>
> When you work with multiple channels/read points, you must ensure that the block is called with a separate instance DB for each channel/read point.

> **Note**
>
> **Working with the Ident profile or with the "AdvancedCmd" block**
>
> If you work with the Ident profile or with the "AdvancedCmd" block, you also need to connect the "CMDREF" input parameter with a variable of the "IID_CMD_STRUCT" (Array [1...n]) data type.

#### Commands of the Ident profile

This section contains information on the following topics:

- [Overview of the commands](#overview-of-the-commands)
- [Command structure](#command-structure)
- [Commands](#commands)
- [Expanded commands for optical reader systems (MV400/MV500)](#expanded-commands-for-optical-reader-systems-mv400mv500)
- [Effect of the commands](#effect-of-the-commands)
- [Editing commands](#editing-commands)
- [Parameter assignment for starting up and restarting](#parameter-assignment-for-starting-up-and-restarting)
- [Chaining](#chaining)
- [Command repetition](#command-repetition)

##### Overview of the commands

The following table contains all the commands supported by the Ident profile and the "AdvancedCMD" block.

Commands of the Ident profile

| Command | Command code |  | Parameters used | Description |
| --- | --- | --- | --- | --- |
| HEX | ASCII |  |  |  |
| PHYSICAL-READ | 0x70 | 'p' | OFFSETBUFFER, EPCID_UID, LEN_ID, LEN_DATA, ADDR_TAG, MEM_BANK, PSWD | Reads data from a transponder / optical reader system by specifying the physical start address, the length and the password. |
| PHYSICAL-WRITE | 0x71 | 'q' | OFFSETBUFFER, EPCID_UID, LEN_ID, LEN_DATA, ADDR_TAG, MEM_BANK, PSWD | Writes data to a transponder / optical reader system by specifying the physical start address, the length and the password. |
| READER-STATUS | 0x74 | 't' | OFFSETBUFFER, ATTRIBUTES | Reads out the status of the reader. |
| TAG-STATUS | 0x73 | 's' | OFFSETBUFFER, EPCID_UID, LEN_ID, ATTRIBUTES | Reads out the status of a transponder. |
| INVENTORY | 0x69 | 'i' | OFFSETBUFFER, ATTRIBUTES, DURATION, DUR_UNIT | Requests a list of all currently accessible transponders within the antenna range. |
| FORMAT | 0x66 | 'f' | OFFSETBUFFER, EPCID_UID, LEN_ID, LEN_DATA | Initializes the transponder. |
| PUT | 0x65 | 'e' | OFFSETBUFFER, EPCID_UID, LEN_ID, LEN_DATA | Transfers further commands not specified in the standard profile. To this end, a corresponding data structure is defined in the send data buffer for each command. |
| WRITE-ID | 0x67 | ‘g‘ | OFFSETBUFFER, EPCID_UID, LEN_ID, NEW-LEN_ID, PSWD | Writes a new EPC-ID to the transponder. |
| KILL-TAG | 0x6A | ‘j‘ | EPCID_UID, LEN_ID, PSWD | The transponder is permanently deactivated. |
| LOCK-TAG-BANK | 0x79 | ‘y‘ | EPCID_UID, LEN_ID, PSWD, ACTION, MASK | The corresponding memory area of the transponder is blocked as specified. |
| EDIT-BLACKLIST | 0x7A | ‘z‘ | EPCID_UID, LEN_ID, MODE | The black list is processed. The current transponder can be added, all identified transponders added, individual transponders deleted or all transponders deleted. |
| GET-BLACKLIST | 0x6C | ‘l‘ | OFFSETBUFFER | The entire TagIDs are read out from the black list. |
| READ-CONFIG | 0x61 | 'a' | -- | Reads out the parameters from the communications module/reader. |
| WRITE-CONFIG | 0x78 | 'x' | LEN_DATA, CONFIG | Sends new parameters to the communications module/reader. |

##### Command structure

Before you can start a command with "EXECUTE" or "INIT", you need to define the command. To allow simple definition of a command, the command buffer "CMDREF" was created using the "IID_CMD_STRUCT" data type. In the command buffer, you have 100 areas available in which commands can be set. The parameter "CMDSEL" specifies which command [1...n] is started with "EXECUTE".

Remember that the first element in the buffer is always reserved for "INIT". This means that if "INIT" is set, "CMDSEL" must be set to "1" and element "1" in the CMD buffer must be filled with the relevant settings. The following table contains the command structure of the parameters. Not every command uses all parameters.

Command structure of the parameters

| Parameter |  | Data type | Default value | Description |
| --- | --- | --- | --- | --- |
| CMD |  | BYTE | B#16#0 | Command code (compare the table in the section "[Commands of the Ident profile](#commands-of-the-ident-profile)".) |
| ATTRIBUTES |  | BYTE | B#16#0 | Sub command name for several commands (e.g. "READER-STATUS", "INVENTORY", etc.) |
| OFFSETBUFFER |  | INT | 0 | Relative offset within the received data buffer. The parameter specifies the address within the memory area at which the first byte of the received data must be stored or the first byte of the data to be sent is expected.   All subsequent bytes must be stored in ascending addresses. |
| EPCID_UID |  | ARRAY[1...62] OF BYTE | B#16#0 | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| LEN_DATA |  | WORD | W#16#0 | Amount of data to be read/written in bytes |
| ADDR_TAG |  | DWORD | DW#16#0 | Physical start address on the transponder |
| CONFIG |  | BYTE | B#16#0 | - 0x01 = reset, no configuration data - 0x02 = no reset, configuration data to be sent - 0x03 = reset, configuration data to be sent - 0x80 = no reset, only individual parameters |
| CHAINED |  | BOOL | FALSE | - 0x00 = not chained - 0x01 = chained  All chained commands must have this bit set except the last command. The commands are worked through in the order in which they are located in the CMD structure. |
| EXT_UHF |  | STRUCT | -- | Structure for additional parameters |
|  | LEN_ID | BYTE | B#16#0 | Length of the valid data in the "EPCID_UID" field. |
| MEM_BANK | BYTE | B#16#3 | Memory bank on the transponder  - 0x00 = RESERVED - 0x01 = EPC - 0x02 = TID - 0x03 = USER |  |
| PSWD | DWORD | DW#16#0 | Password for transponder access  0x00 ≙ no password |  |
| EDIT_BLACKLIST_MODE | BYTE | B#16#0 | Mode  - 0x00 = add TagID - 0x01 = add all "Observed" transponders - 0x02 = delete TagID - 0x03 = delete all |  |
| INVENTORY_DURATION | WORD | W#16#0 | Duration  Period of time or number of inventories or number of "Observed" events  Example:   - 0x00 ≙ no inventory - 0x01 ≙ one inventory |  |
| INVENTORY_DUR_UNIT | WORD | W#16#0 | Unit for "DURATION"  - 0x00 = time [ms] - 0x01 = inventories - 0x02 = Number of transponders that reach the "Observed" state |  |
| LOCK-TAG-BANK_ACTION | WORD | W#16#0 | Lock-Action (see "EPC Specification") |  |
| LOCK-TAG-BANK_MASK | WORD | W#16#0 | Lock-Mask (see "EPC Specification") |  |

##### Commands

All relevant parameters and parameter values for the individual commands are listed below. Parameters that are not listed receive the default value specified in the previous section.

PHYSICAL-READ

| Parameter | Value / description |
| --- | --- |
| CMD | 0x70 |
| OFFSETBUFFER | Offset in the "RXREF" receive buffer |
| LEN_DATA | Length of received data |
| ADDR_TAG | Address on the transponder |
| CHAINED | - True = chained - False = not chained |
| EPCID_UID | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| LEN_ID | Length of the EPC-ID / UID (2-62 bytes)  Default value: 0x00 ≙ unspecified single tag access |
| MEM_BANK | Memory bank  - 0x00 ≙ Reserved - 0x01 ≙ EPC - 0x02 ≙ TID - 0x03 ≙ USER |
| PSWD | Password  0x00 ≙ no password |
| RXREF | Read data |

PHYSICAL-WRITE

| Parameter | Value / description |
| --- | --- |
| CMD | 0x71 |
| OFFSETBUFFER | Offset in the "TXREF" send buffer |
| LEN_DATA | Length of the data to be written |
| ADDR_TAG | Address on the transponder |
| CHAINED | - True = chained - False = not chained |
| EPCID_UID | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| LEN_ID | Length of the EPC-ID / UID (2-62 bytes)  Default value: 0x00 ≙ unspecified single tag access |
| MEM_BANK | Memory bank  - 0x00 ≙ Reserved - 0x01 ≙ EPC - 0x02 ≙ TID - 0x03 ≙ USER |
| PSWD | Password  0x00 ≙ no password |
| TXREF | Data to be written |

READER-STATUS

| Parameter | Value / description |
| --- | --- |
| CMD | 0x74 |
| OFFSETBUFFER | Offset in the "RXREF" receive buffer |
| ATTRIBUTES | Identifier of the status modes / possible entries:  - RF200: 0x81 - RF300: 0x81, 0x86, 0xEF - RF61xR, RF68xR: 0x89 - MOBY U: 0x81, 0x84, 0x85 - MOBY D: 0x81 |
| - RF18xC/RF18xCI, RF166C, RF360R (FW 2.0 and higher): 0xA2 |  |
| RXREF | Received status data  You will find the data structure of the status modes in the section "[Reader_Status](#reader_status)". |

TAG-STATUS

| Parameter | Value / description |
| --- | --- |
| CMD | 0x73 |
| OFFSETBUFFER | Offset in the "RXREF" receive buffer |
| ATTRIBUTES | Identifier of the status modes / possible entries:  - RF200: 0x83 - RF300 (RF300T): 0x04, 0x82 - RF300 (ISO): 0x83 - RF300 Gen2: 0x83 - MOBY D: 0x83<sup> 1)</sup> - MOBY U: 80 |
| EPCID_UID | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| LEN_ID | Length of the EPC-ID / UID (2-62 bytes)  Default value: 0x00 ≙ unspecified single tag access |
| RXREF | Received status data  You will find the data structure of the status modes in the section "[Tag_Status](#tag_status)". |
| <sup>1)</sup> SLG D10S only |  |

INVENTORY

| Parameter | Value / description |
| --- | --- |
| CMD | 0x69 |
| OFFSETBUFFER | Offset in the "RXREF" receive buffer |
| ATTRIBUTES | Identifier of the status modes / possible entries:  - 0x80 ≙ inventory with brief transponder information - 0x81 ≙ inventory with a lot of transponder information - 0x86 ≙ Presence mode on - 0x87 ≙ Presence mode off |
| INVENTORY_DURATION | Only for 0x80 and 0x81:  Duration  Period of time or number of inventories or number of "Observed" events  Example:   - 0x00 ≙ no inventory - 0x01 ≙ one inventory |
| INVENTORY_DUR_UNIT | Only for 0x80 and 0x81:  Unit for "DURATION"  - 0x00 ≙ time [ms] - 0x01 ≙ inventories - 0x02 ≙ number of transponders that achieve the "Observed" state |
| RXREF | Data received  You will find the data structure of the status modes in the section "[Data structure of the Ident profile](#data-structure-of-the-ident-profile)". |

FORMAT (not with RF200 and RF61xR/RF68xR)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x66 |
| OFFSETBUFFER | Offset in the "TXREF" send buffer |
| LEN_DATA | Length of the parameter data to be sent (15 bytes) |
| EPCID_UID | Buffer for up to 62 bytes EPC-ID, 8 bytes UID or 4 bytes handle ID.  - 2 - 62-byte EPC-ID is entered at the start of the buffer (length is set by "LEN_ID") - 8-byte UID is entered at the start of the buffer ("LEN_ID = 8") |
| LEN_ID | Length of the EPC-ID / UID (2-62 bytes) |
| TXREF | Parameter data to be written |

Structure of the data attachment for the "FORMAT" command with normal addressing

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Byte** | 1...8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| **Value** | 0x00 | 0x06 | 0x03 | 0x00 | INIT-Wert | 0x00 | MSB | LSB |

Explanation of the structure of the data attachment for the "FORMAT" command

| Byte | Description |
| --- | --- |
| Bytes 1...8 | Reserved for security code (must be assigned "0", since SIMATIC RFID has had no code previously) |
| Byte 9 | Length of the following data, here 6 |
| Byte 10 | Permanently set to "0x03" |
| Byte 11 | Permanently set to "0x00" |
| Byte 12 | "INIT" value: The data area of the transponder is written with this value (hex format). |
| Byte 13 | Permanently set to "0x00" |
| Byte 14 | Memory size of the transponder (end address + 1; high byte, hex format) |
| Byte 15 | Memory size of the transponder (end address + 1; low byte, hex format) |

During the initialization of the transponders with the RF300 readers of the 2nd generation, the address information has the following meaning:

- Complete "INIT": Address = 0 or address = memory size of the transponder

  Means that the entire address range is initialized.
- Partial "INIT": Address ≠ 0

  Means that the initialization is up to the specified address.

Memory sizes of the transponders

| Transponder type |  |  | Memory size | INIT duration |
| --- | --- | --- | --- | --- |
| 2 KB  32 KB | MOBY U  MOBY U | RAM <sup>1)</sup>  RAM <sup>1)</sup> | 08 00  80 00 | approx. 1 s  approx. 1.5 s |
| 44 bytes  112 bytes  256 bytes  992 bytes  2000 bytes | MOBY D  MOBY D  MOBY D  MOBY D  MOBY D | I-Code 1  ISO I-Code SLI  ISO Tag-it HF-I  ISO my-d  FRAM | 00 2C  00 70  01 00  03 E0  07 D0 | approx. 0.4 s  approx. 0.5 s  approx. 1 s  approx. 3 s  approx. 3 s |
| 20 bytes  8 KB  32 KB  64 KB | RF300  RF300  RF300  RF300 | EEPROM  FRAM <sup>1)</sup>  FRAM <sup>1)</sup>  FRAM <sup>1)</sup> | 00 14  20 00  80 00  FF 00 | approx. 0.2 s  0.9 s  3.6 s  7.2 s |
| 752 bytes | MOBY E | EEPROM | 02 EF | approx. 1.5 s |
| <sup>1)</sup> The OTP memory is not initialized by this command. |  |  |  |  |

PUT (not with RF61xR/RF68xR)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x65 |
| OFFSETBUFFER | Offset in the "TXREF" send buffer |
| LEN_DATA | Length of the parameter data to be sent |
| TXREF | Parameter data to be written |

Data structure of the PUT command

|  |  |  |
| --- | --- | --- |
| Put_SET_ANT |  | Switches the antenna of the reader off and on.    ![Figure](images/63784378763_DV_resource.Stream@PNG-de-DE.png) |
|  | Mode | RF200/RF300, MOBY U/D:   - 0x01 ≙ antenna on - 0x02 ≙ antenna off |
| Length | 3 |  |
| Put_END |  | Terminates communication with a transponder (MOBY U only).    ![Figure](images/63788854411_DV_resource.Stream@PNG-de-DE.png) |
|  | UID | UID of the transponder |
| Mode | - 0x00 ≙ end processing of the transponder - 0x01 ≙ processing pause of the transponder |  |
| Length | 11 |  |

WRITE-ID (RF61xR/RF68xR only)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x67 |
| OFFSETBUFFER | Offset in the "TXREF" send buffer |
| EPCID_UID | Previous EPC-ID |
| LEN_ID | Length of the previous EPC-ID (2-62 bytes) |
| LEN_DATA | Length of the new EPC-ID |
| PSWD | Password  0x00 ≙ no password |
| TXREF | New EPC-ID |

KILL-TAG (RF61xR/RF68xR only)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x6A |
| EPCID_UID | EPC-ID |
| LEN_ID | Length of the EPC-ID / UID (2-62 bytes) |
| PSWD | Password  must be ≠ 0x00 |

LOCK-TAG-BANK (RF61xR/RF68xR only)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x79 |
| EPCID_UID | EPC-ID |
| LEN_ID | Length of the EPC-ID / UID (2-62 bytes) |
| PSWD | Password  0x00 ≙ no password |
| LOCK_TAG_ BANK_ACTION | See EPC standard |
| LOCK_TAG_ BANK_MASK | See EPC standard |

EDIT-BLACKLIST (RF61xR/RF68xR only)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x7A |
| EDIT_BLACKLIST_MODE | - 0x00 ≙ add EPC-ID - 0x01 ≙ Add all "Observed" transponders - 0x02 ≙ Delete EPC-ID - 0x03 ≙ delete all |
| EPCID_UID | EPC-ID  0x00 ≙ unspecified single tag access <sup>1)</sup> |
| LEN_ID | Length of the EPC-ID (2-62 bytes)  0x00 ≙ unspecified single tag access |
| <sup>1)</sup> If "EDIT_BLACKLIST_MODE" = 0x00 or 0x02 was selected, the EPC-ID including the ID length must be specified. |  |

GET-BLACKLIST (RF61xR/RF68xR only)

| Parameter | Value / description |
| --- | --- |
| CMD | 0x6C |
| OFFSETBUFFER | Offset in the "RXREF" receive buffer |
| RXREF | Read black list IDs |

Result of GET-BLACKLIST

| Name |  |  | Type | Comment |
| --- | --- | --- | --- | --- |
| `NUM_IDS` |  |  | `INT` | `Number of MDS` |
| `TAG_DATA` |  |  | `IID_IN_I_80[n]` |  |
|  | `TAG_DATA[1]` |  | `IID_IN_I_80` |  |
|  |  | `Reserved` | `SINT` |  |
|  |  | `ID_Len` | `SINT` | `Length of EPC ID` |
|  |  | `EPC_ID` | `SINT[1..62]` | `EPC-ID` |
|  | `TAG_DATA[2]` |  | `IID_IN_I_80` |  |
|  | `...` |  | `...` |  |
|  | `TAG_DATA[n]` |  | `IID_IN_I_80` |  |

READ-CONFIG

| Parameter | Value / description |
| --- | --- |
| CMD | 0x61 |
| OFFSETBUFFER | Offset in the "RXREF" receive buffer |
| RXREF | Read reset parameters |

WRITE-CONFIG

| Parameter | Value / description |
| --- | --- |
| CMD | 0x78 |
| OFFSETBUFFER | Offset in the "TXREF" send buffer |
| LEN_DATA | Length of the parameter data |
| CONFIG | - 0x01 ≙ communication reset, no configuration data - 0x02 ≙ no communication reset, configuration data to be sent - 0x03 ≙ communication reset, configuration data to be sent - 0x80 ≙ no communication reset, individual parameters |
| TXREF | Configuration data to be sent |

###### Structure of the configuration data attachment of "WRITE-CONFIG"

**For RF360R, RF61xR/RF68xR and RF18xC/RF18xCI as well as RF166C:**

- When CONFIG = 0x01:

  Reset_Reader; LEN_DATA = 0x00
- When CONFIG = 0x03:

  When replacing a module, it is possible to read all the configuration data from the CM/reader and to store it on the controller. When the module is replaced, this data can then be loaded on the reader from the controller. The command "WRITE-CONFIG" (0x03) is used for the download to the CM/reader and "READ-CONFIG" for the upload from the reader.

  | Byte | Name |
  | --- | --- |
  | 0 | Structure identifier (2 bytes) |
  | 2 | Length information (4 bytes)  Length of the version identifier and parameter block |
  | 6 | Version identifier (4 bytes)  Based on the identifier, you can uniquely identify the configuration. This is a time stamp in Linux format.   The time stamp indicates how many seconds have passed since January 1, 1979, 00:00 (midnight). The identifier is assigned when a configuration is generated. |
  | 10 ... end "DATA" | Parameter block |

  LEN_DATA = Size of the configuration data + 6 bytes
- When CONFIG = 0x80:

  This command allows you to change UHF parameters (e.g. the antenna power) on an RF61xR/RF68xR, as well as the date/time parameters of an RF360R, RF166C or RF18xC/RF18xCI during runtime.

  | Byte | Name |
  | --- | --- |
  | 0 ... 3 | Parameter identification "PARMID" (4 bytes) |
  | 4 ... 7 | Parameter value "VALUE" (4 bytes) |

  You can find possible values for parameter identification and value in section "[Set_Param](#set_param)".  
  LEN_DATA = 0x08

**For RF200, RF300, MOBY D/U and Freeport**

For RF200, RF300, MOBY D/U and Freeport with "CONFIG = 0x03".

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Byte** | 1 | 2...5 <sup>1)</sup> | 6 <sup>2)</sup> | 7...8 | 9 | 10 | 11 | 12 | 13...14 | 15 | 16 |
| **Value**   **(RF200, RF300, MOBY U/D)** | 0x04 | 0x00 | 0x0A 0x05 | 0x00 | scanning_ time | param | option_1 | distance_ limiting | No. of transponders | field_on_ control | field_on_ time |
| **Value**   **(Freeport)** | 0x04 | 0x00 | 0x0A | 0x00 | 0x00 | 0x00 | option_1 | 0x00 | 0x00 | 0x00 | 0x00 |
| <sup>1)</sup> In the communications module RF180C as of V2.2 in conjunction with MOBY U byte 4 is preset with the calendar week and 5 with the year.   <sup>2)</sup> With the readers named in the title of the table the value "0x0A" (LEN_DATA = 0x10) is used in byte 6. In the MOBY I migration in RF300 readers of the 2nd generation the value "0x05" (LEN_DATA = 0x0B) is used. |  |  |  |  |  |  |  |  |  |  |  |

The parameter values of bytes 9 ... 16 are described below.

Parameter values of bytes 9 ... 16

| Byte | Value | RFID system | Meaning |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Byte 9** | scanning_ time | RF200, MOBY D | Bits 0...7: Reserved (to be assigned the value "0"). |  |  |  |
| RF300 | Bit 0...1: Reserved (to be assigned the value "0").  Bit 2...4: Modulation depth  - 0: 0% (default) - 1: 7% - 2: 10% - 3: 15% - 4: 20% - 5 25% - 6: 30% - 7: 100%   Bit 5...7: Input attenuation  - 0: Default (default attenuation stored in the firmware, depending on the reader type and air interface protocol) - 1: 0 dB - 2: 5 dB - 3: 10 dB - 4: 15 dB - 7: -5 dB |  |  |  |  |  |
| MOBY U | The "scanning_time" describes the standby time for the transponder. If the transponder receives a further command before "scanning_time" has expired, this command can be executed immediately. If the transponder receives a command after "scanning_time" has expired, command execution is delayed by the "sleep_time" of the transponder.  The "scanning_time" should only be set when the  - Transponder is processed with several commands and - Execution must be completed within a minimum time   Note that the "scanning_time" affects the working life of the battery. The longer "scanning_time" is set, the shorter the life of the battery. For precise calculations, see the MOBY U manual for configuration, mounting and service. |  |  |  |  |  |
| Value | Description |  |  |  |  |  |
| 0x00 | No standby time (default) |  |  |  |  |  |
| 0x01 | 7 ms standby time |  |  |  |  |  |
| 0x02 | 14 ms standby time |  |  |  |  |  |
| ... | ... |  |  |  |  |  |
| 0xC8 | 1400 ms standby time |  |  |  |  |  |
| **Byte 10** | param | RF200, RF300, MOBY D/U | Setting for the RFID mode and presence check |  |  |  |
| Bit | Description |  |  |  |  |  |
| 7 ... 5 | This parameter switches the presence check on or off on the reader.  Possible values:  - 0: Operation without presence check <sup>1) </sup>Antenna is permanently switched on. - 1: Operation with presence check Antenna is permanently switched on. - 2: RF300 (2nd Generation): Operation without presence check and with semaphore procedure (RF300, ISO 14443 [MIFARE Classic, MOBY E])<sup> </sup>Antenna is permanently switched on. - 3: RF300 (2nd Generation): Operation with presence check and with semaphore procedure (RF300, ISO 14443 [MIFARE Classic, MOBY E]) Antenna is permanently switched on. - 4: Operation without presence check Antenna is switched off. The antenna is only switched on when one of the following commands is sent: Read, Write, Init, Tag-Status - 6: RF300 (2nd Generation): Operation without presence check and with semaphore procedure (RF300, ISO 14443 [MIFARE Classic, MOBY E])   You can find information on the semaphore procedure in the product information "Input parameters for the RF300 system". |  |  |  |  |  |
| <sup>1)</sup> Note on LED behavior with MOBY I migration: In "None present" mode, the LED of the reader stays blue until initial access (Read/Write/Init) to the transponder takes place. The LED flashes green as long as no other access is made or command is executed. As soon as a command is sent, the LED lights up green or orange, depending on whether or not a transponder is within the antenna range. |  |  |  |  |  |  |
| 4 | RF300, 2nd Generation  For RF300 2nd Generation, this parameter enables ECC mode for the transponder types RF300 and ISO 14443 (MIFARE Classic, MOBY E). The value "0" must be entered for all other systems.  Possible values:  - 0: ECC mode is switched off. - 1: ECC mode is switched on.   In ECC mode, the reader can detect bit errors on the transponder with a high degree of probability. If possible, corrected data is returned during read access (the data on the transponder remains unchanged). When write access occurs, the affected data on the transponder is corrected - if possible. ECC mode can only be used for transponders that have been completely initialized with the ECC bit set and are thus ECC formatted. The transponder is divided into blocks of 16 bytes for this, whereby 14 bytes are reserved for user data and 2 bytes for ECC information (CRC). This leads to a reduction of the usable memory volume by approx. 1/8th.  If bit errors have been detected and corrected, the warning "0xF0FE0002" is issued in the "STATUS" output parameter. If the bit error could not be corrected, the error "0xE1FE0700" is output.  Note: Note that only the transponders of type RF300 and ISO 14443 (e.g. MOBY E) are supported in this mode. |  |  |  |  |  |
| Values of bits 3 ... 0 |  |  |  |  |  |  |
| Values of bits 3 ... 0 | Operating mode | Description |  |  |  |  |
| 0 | Reserved | Reserved for the setting with the switch or GSD parameter assignment |  |  |  |  |
| 1 | MOBY I | If RF300 readers of the 2nd generation are to be operated in MOBY I mode, the value = 0x01 must be set.  Short "INIT" (only the "param" and "option_1" parameters are transferred to the reader). |  |  |  |  |
| 5 | MOBY U/D, RF200, RF300 | Single tag mode |  |  |  |  |
| 6 | MOBY U | Multitag mode  - Parameter setting with Multitag > 1 and more than one transponder in the antenna field: the UID parameter must be supplied with the transponder ID. - Parameter setting with Multitag = 1 and only one transponder in the antenna field: the UID parameter can be supplied with the correct transponder ID or zero. |  |  |  |  |
| 7 | MOBY D | Multitag mode |  |  |  |  |
| Note: Note that after a parameter change the CM must be restarted. |  |  |  |  |  |  |
| **Byte 11** | option_1 | RF200, RF300, Freeport, MOBY D/U | This byte is bit-coded. As default, it has the value "B#16#0". With this byte, special controllers can be implemented on the CM/reader. |  |  |  |
| Bit | Description |  |  |  |  |  |
| 1 | Possible values:  - 0 = The flashing of the "ERR" LED in case of an error is not reset. - 1 = Flashing of the "ERR" LED in the event of an error is reset by a "WRITE-CONFIG". With RF200/RF300, this resets the flashing of the "ERR" LED on the communications module and on the reader. With Freeport only the flashing of the "ERR" LED on the communication module is reset. |  |  |  |  |  |
| RF300 (2nd generation) | The following values are permitted: |  |  |  |  |  |
| Value | Description |  |  |  |  |  |
| 0x00 | The flashing LED in the event of an error can only be reset by switching off the power supply to the reader. |  |  |  |  |  |
| 0x01 | The flashing of the LED in the event of an error is reset after the successful execution of a command. This only affects communication errors (e.g. 0xE1FE0200, 0xE2FE0100); other errors are not reset with this. |  |  |  |  |  |
| 0x02 | The flashing of the LED in the event of an error is reset by a "init_run" or "WRITE-CONFIG" with "Init" (RESET). |  |  |  |  |  |
| 0x03 | The flashing of the LED in the event of an error is reset by a "init_run" or "WRITE-CONFIG" with "Init" (RESET) or after the successful execution of a command. |  |  |  |  |  |
| **Byte 12** | distance_ limiting | RF200 | 0x00 (reserved) |  |  |  |
| RF300 (RF350R, RF380R only) | Note: This parameter is intended for trained users. Siemens recommends that untrained users use the default value.  The output line can be set in bit 0...3. This setting does not need to be manually performed for RF380R readers of the 2nd generation (6GT2801-3BAx0) because the power limits are optimized automatically depending on the reader-transponder distance. For reasons of compatibility, this setting can nevertheless be made. Note that the values "02", "03" and "04" bring about a reduction of the power of approximately 50%. Settings outside the range (02 ... 08) have the effect of setting the default value (0.6 W). In this case, there is no error message for reasons of compatibility. |  |  |  |  |  |
| Bit 4...7: Antenna type  (RF350R readers of the 2nd generation)  To improve communication stability. The following values are permitted:  - 0: Unspecified (default) - 1: ANT 1 - 2: ANT 3 - 3: ANT 3S - 4: ANT 8 - 5 ANT 12 - 6: ANT 12 (6GT2398-1CC10 with integrated antenna connecting cable 0.6 m) - 7: ANT 18 - 8: ANT 18 (6GT2398-1CA10 with integrated antenna connecting cable 0.6 m) - 9: ANT 30 |  |  |  |  |  |  |
| MOBY U | Distance limitation |  |  |  |  |  |
| Normal transmit power<sup> 1)</sup> |  | Reduced output power |  |  |  |  |
| 0x05 = 0.5 m  0x0A = 1.0 m  0x0F = 1.5 m  0x14 = 2.0 m  0x19 = 2.5 m  0x1E = 3.0 m  0x23 = 3.5 m |  | 0x85  0x8A  0x8F  0x91  0x99  0x9E  0xA3 | Set reduced transmit power when several readers are positioned close together or when transponders which are located in the vicinity of a reader are detected later or no longer.  Disadvantage: The antenna field becomes smaller and there is less time for communication or positioning must be more precise. |  |  |  |
| <sup>1)</sup> Intermediate values in steps of 0.1 m are possible (0x02, 0x03, ..., 0x23) |  |  |  |  |  |  |
| MOBY D | Transmit power from 0.5 W to 10 W in increments of 0.25 W  Only effective with SLG D10S; a power of 1 W (04 hex) is set for SLG D11S / D12S and cannot be changed. |  |  |  |  |  |
| Value |  | Transmit power |  |  |  |  |
| 0x02 |  | 0.5 W |  |  |  |  |
| ... |  | ... |  |  |  |  |
| 0x10 |  | 4.0 W (default) |  |  |  |  |
| ... |  | ... |  |  |  |  |
| 0x28 |  | 10.0 W |  |  |  |  |
| **Bytes 13...14** | No. of transponders | RF300 | To be assigned the value "0x0001". |  |  |  |
| **Byte 15** | field_on_ control | RF200, RF300, MOBY D | To be assigned the value "0x00". |  |  |  |
| MOBY U | BERO mode; automatic activation/deactivation of the antenna field. The "Antenna ON/OFF" command is superimposed by the BERO mode. |  |  |  |  |  |
| Value | Description of mode |  |  |  |  |  |
| 0x00 | without BEROs; no reader synchronization |  |  |  |  |  |
| 0x01 | One or two BEROs  The BEROs are ORed. The antenna field is turned on during the actuation of a BERO. |  |  |  |  |  |
| 0x02 | One or two BEROs  The 1st BERO switches the antenna field on and the 2nd BERO switches the antenna field off. If there are two BEROs and a "field_ON_time" is set, the antenna field is automatically turned off if the 2nd BERO does not switch within this BERO time.  If no "field_ON_time" is set, the antenna field remains turned on until the 2nd BERO is activated. |  |  |  |  |  |
| 0x03 | Activating reader synchronization over cable connection  You will find further information in the MOBY U manual for configuration, mounting and service. |  |  |  |  |  |
| **Byte 16** | field_on_ time | RF200 | Transponder type |  |  |  |
| 0x01 | Any ISO transponder |  |  |  |  |  |
| RF300 | Selection of the transponder types used  With the value "0x01"/"0x31" (ISO 15693 general), the readers of the 2nd generation always use the ISO commands with which the highest performance can be achieved for the particular transponder. With readers of the 1st generation, the value "0x01" activates the general ISO mode with rudimentary ISO commands. With this setting, the performance is generally limited, but operation is basically guaranteed with every ISO-compatible transponder.  All ISO 15693 transponders (MDS D) specified in the system manual "SIMATIC RF300" support these ISO commands.   The following values can be set: |  |  |  |  |  |
| Value | Transponder type | Description |  |  |  |  |
| 0x00 | RF300 (RF3xxT) | For all transponders of the type "RF3xxT" |  |  |  |  |
| 0x01 | ISO 15693  general | Any ISO transponder  Activation of the general ISO mode with rudimentary ISO commands. With this setting, operation is basically guaranteed with every ISO-compatible transponder. |  |  |  |  |
| 0x03 | ISO 15693 (MDS D3xx; Infineon) | e.g. MDS D324, D339 |  |  |  |  |
| 0x04 | ISO 15693 (MDS D4xx, Fujitsu - 2 KB) | e.g. MDS D421, D422, D423, D424, D425, D426, D428, D460 |  |  |  |  |
| 0x05 | ISO 15693 (MDS D1xx, NXP) | e.g. MDS D100, D124, D126, D139, D150, D165 |  |  |  |  |
| 0x06 | ISO 15693 (MDS D2xx, TI) | e.g. MDS D200 |  |  |  |  |
| 0x07 | ISO 15693 (MDS D261, STM) | e.g. MDS D261 |  |  |  |  |
| 0x08<sup>1)</sup> | ISO 15693 (MDS D5xx, Fujitsu - 8 KB) | e.g. MDS D521, D522, D524, D525, D528 |  |  |  |  |
| 0x10<sup>1)</sup> | RF300 (RF3xxT) | For all transponders of the type "RF3xxT" |  |  |  |  |
| 0x20<sup>1)</sup> | ISO 14443 (MIFARE Classic MOBY E, E6xx) | e.g. MDS E600, E611, E623, E624 |  |  |  |  |
| 0x2F<sup>1)</sup> | ISO 14443  (MIFARE Classic) | Open mode for changing the key material on the MIFARE Classic transponder. You can find information on open mode in the product information "Input parameters for the RF300 system". |  |  |  |  |
| 0x31<sup>1)</sup> | General mode (ISO, RF300, MOBY E) | Activation of the "General Mode" for processing the transponder types RF300, ISO 15693 and ISO 14443 (MIFARE Classic, MOBY E). With this setting, operation is basically guaranteed with every compatible transponder. |  |  |  |  |
| 0x40<sup>1)</sup> | P2P master | Reader turns into a P2P master |  |  |  |  |
| 0x4F<sup>1)</sup> | P2P slave | Reader turns into a P2P slave |  |  |  |  |
| <sup>1)</sup> Applies only to readers of the 2nd generation. |  |  |  |  |  |  |
| Note that individual settings or transponder families can be combined (e.g. ISO 15693 general + RF300). In this case, the relevant hex values need to be combined (ISO 15693 general [0x01] + RF300 [0x10] = 0x11).  Note:  - ISO 15693: The following ISO special functions are not supported:   - AFI (Application Family Identifier)   - DSFID (Data Storage Format Identifier)   - Chip-specific added functions such as EAS, Kill commands, etc. |  |  |  |  |  |  |
| MOBY U | Time for BERO mode (field_ON_control = 02) |  |  |  |  |  |
| Value | Description |  |  |  |  |  |
| 0x00 | Time monitoring is deactivated. The 2nd BERO is needed in order to switch the field off. |  |  |  |  |  |
| 0x01 ... 0xFF | 1 ... 255 s turn on time for the reader antenna field |  |  |  |  |  |
| MOBY D | Transponder type |  |  |  |  |  |
| 0 ... 255 | Transponder type |  |  |  |  |  |
| 0x00 | I-Code 1 (e.g. MDS D139) |  |  |  |  |  |
| 0x01 | ISO transponder |  |  |  |  |  |
| 0x02 | I-Code 1 and ISO transponder |  |  |  |  |  |
| 0x03 | ISO-my-D  (with SLG D10S only; the value "0x01" is set for ISO-my-D with SLG D11S / D12S) |  |  |  |  |  |
| 0x04 | ISO-FRAM  (with SLG D11S / D12S only; the value "0x01" is set for ISOFRAM with SLG D10S) Parameter values of bytes 9 ... 16 |  |  |  |  |  |

##### Expanded commands for optical reader systems (MV400/MV500)

###### The "WRITE-CONFIG" command

During initialization ("INIT"), the Ident profile automatically executes the "WRITE-CONFIG" command. The parameter values of the "WRITE-CONFIG" command depend on whether the Ident profile is used with or without a communications module.

WRITE-CONFIG

| CMD | OFFSET BUFFER | LEN_DATA | CONFIG | TXREF |
| --- | --- | --- | --- | --- |
| 0x78 | Offset in the "TXREF" send buffer | Length of the parameter data | - 0x01 ≙ communication reset without configuration data (LEN_DATA = 0) - 0x03 ≙ communication reset with configuration data to be sent | Configuration data to be sent |

Note that the communication reset without configuration data (CONFIG = 0x01) can only be used if you operate the reader without communications module via PROFINET IO. Reset without configuration data corresponds to the "INIT" command without program selection.

**Structure of the configuration data attachment of "WRITE-CONFIG"**

MV400/MV500 with "CONFIG = 0x03"; "LEN_DATA = 0x10"

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Byte** | 1 | 2...5 | 6 | 7...8 | 9 | 10 | 11 | 12 ... 13 | 14 | 15 | 16 |
| **Value** | 0x04 | 0x00 | 0x0A | 0x00 | 0x00 | 0x25 | 0x02 | 0x00 | 0x01 | 0x00 | 0x00 ... 0x0F <sup>1)</sup> |
| <sup>1)</sup> 0x00: "INIT" without program selection   0x01 ... 0x0F: Number of the program to be started ("INIT" with program selection) |  |  |  |  |  |  |  |  |  |  |  |

###### The "PHYSICAL-WRITE" command

The optical reader systems MV400/MV500 have further commands that can be transferred with the "PHYSICAL-WRITE" command.

PHYSICAL-WRITE

| CMD | OFFSET BUFFER | ADDR_TAG | LEN_DATA | TXREF |
| --- | --- | --- | --- | --- |
| 0x71 | Offset in the "TXREF" send buffer | 0x0000 | Length of data to be sent to the reader: | Attributes with data to be transmitted to the reader. The first "byte" contains the command identifier: |
| - 0x02 | - 0x01 = Program change |  |  |  |
| - 0x01 | - 0x02 = Activate read program number |  |  |  |
| - Match string length + 3 | - 0x03 = Write match string |  |  |  |
| - 0x01 | - 0x04 = Activate read match string |  |  |  |
| - 0x01 | - 0x05 = Set DISA bit |  |  |  |
| - 0x01 | - 0x06 = Reset DISA bit |  |  |  |
| - Total length of the XMATCH user data + 4 | - 0x07 = Write trigger-synchronized match string (XMATCH) |  |  |  |
| - 0x07 | - 0x08 = Set Digital Out |  |  |  |

Command data area "TXREF" command identifier 0x01 (program change)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x01 | "Program change" command identifier |
| 0x0001 | 0x00 ... 0x0F | Number of the program |

Command data area "TXREF" command identifier 0x02 (activate read program number)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x02 | "Read program number" command identifier |

Command data area "TXREF" command identifier 0x03 (write match string)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x03 | Command identifier "Write match string" |
| 0x0001 | 0x00...0xFF | Match string length high byte |
| 0x0002 | 0x00...0xFF | Match string length low byte |
| 0x0003 | -- | 1st character of the match string |
| ... | ... | ... |
| n + 2 | -- | (n-1)th character of the match string |
| n + 3 | -- | nth character of the match string |

Command data area "TXREF" command identifier 0x04 (activate read match string)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x04 | Command identifier "Read match string" |

Command data area "TXREF" command identifier 0x05 (set DISA bit)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x05 | Command identifier "Set DISA bit" |

Command data area "TXREF" command identifier 0x06 (reset DISA bit)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x06 | Command identifier "Reset DISA bit" |

Command data area "TXREF" command identifier 0x07 (XMATCH)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x07 | Command identifier "XMATCH" |
| 0x0001 | 0x00 | Reserved |
| 0x0002 | You will find detailed information in the manual "SIMATIC MV420 / SIMATIC MV440" or "SIMATIC MV500". | XMATCH user data |
| … |  |  |
| 0xN |  |  |

Command data area "TXREF" command identifier 0x08 (set Digital Out)

| Address | Value | Meaning |
| --- | --- | --- |
| 0x0000 | 0x08 | Command identifier "Set Digital Out" |
| 0x0001 | 0x01...0x04 | Number of the logical external signal. Corresponds to "EXT_1", "EXT_2", "EXT_3" and "EXT_4". |
| 0x0002 | 0x00...0x02 | Level of the signal  - 0x00: Set level statically to "low". - 0x01: Set level statically to "high". - 0x02: Set level for configured pulse time to "high". |
| 0x0003 | 0x01...0x07 | Type of logic operation  - 0x01: Logical "OR" - 0x02: Logical "AND" - 0x03: Logical "Exclusive OR" - 0x04: no logic operation - 0x05: Logical "OR not" - 0x06: Logical "AND not" - 0x07: Logical "Exclusive OR not" |
| 0x0004 | 0x00...0x05 | Logical signal linked to.  If the logic operation type is 0x4, the parameter has no significance.  - 0x00: Logical signal "IN_OP" - 0x01: Logical signal "TRD" - 0x02: Logical signal "RDY" - 0x03: Logical signal "READ" - 0x04: Logical signal "MATCH" - 0x05: Logical signal "NOK" |
| 0x0005 | 0x00 | Reserved, must be 0x00 to retain upwards compatibility. |
| 0x0006 | 0x00 | Reserved, must be 0x00 to retain upwards compatibility. |

###### The "PHYSICAL-READ" command

The "PHYSICAL-READ" command is used for the following functions:

- Reading codes
- Follow-on command after "activate read program number" for reading out the program number
- Follow-on command after "activate read match string" for reading out the match string

PHYSICAL-READ

| CMD | OFFSET BUFFER | ADDR_TAG | LEN_DATA | RXREF |
| --- | --- | --- | --- | --- |
| 0x70 | Offset in the "RXREF" send buffer | 0x0000 | Length of the data to be fetched from the reader: | Data fetched from the reader: |
| - ≥ code length +2 | - Code data |  |  |  |
| - = 0x01 | - Program number |  |  |  |
| - ≥ Match string length +2 | - Match string |  |  |  |

##### Effect of the commands

The commands used take effect as follows:

- The input parameters "INIT" and "RESET" interrupt command execution within the communications module.
- The completed message that follows the "INIT" or "SRESET" ("DONE" or "ERROR") always relates to the input parameter "INIT" or "SRESET" and not to the interrupted command.
- The input parameter "INIT" resets communication between the Ident profile and the communications module. Following "hard" resetting of the communications module, the Ident profile automatically transfers the "WRITE-CONFIG" command to the communications module. This is why it is absolutely necessary that you store the "WRITE-CONFIG" command in the first element of the command buffer "CMDREF".
- The "WRITE-CONFIG" command resets all functions within the communications module, with the exception of the communication.
- The parameter "SRESET" interrupts a running command.

##### Editing commands

Follow the steps below to edit the commands:

1. Write the "CMDREF" (Array [1…n]) parameter with the required commands.

   The content of "CMDREF" = [1] is reserved for initialization. It is executed when the "INIT" input of the Ident profile is set and "CMDSEL" is = [1].
2. Transfer the data to be written to the send data buffer "TXBUF".
3. Select the previously written command (Array [1…n]) with the parameter "CMDSEL".
4. Execute the command using the "EXECUTE" parameter ("EXECUTE" = 1").

   Wait until the bits "BUSY = FALSE" and "DONE = TRUE" are set.

   The command is now executed free of errors.

   If "ERROR = TRUE" is set, continue at point 5. Otherwise, continue with Step 6.
5. Evaluate the errors that have occurred.
6. Reset the "EXECUTE" bit.

The following diagram illustrates the running of the Ident profile over time. A command is always started on the positive edge of "EXECUTE", "INIT" or "SRESET".

![General sequence of the Ident profile](images/63499640331_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Case ① | By setting EXECUTE (EXECUTE = 1) the function/instruction is started. If the job was completed successfully (DONE = 1), you need to reset EXECUTE. DONE is reset at the same time. |
| Case ② | EXECUTE is set for only one cycle. As soon as BUSY is set (and DONE is reset), you can reset EXECUTE again. If the job was completed successfully, DONE is set for one cycle. |
| Case ③ | Handling as in Case 1, however with error output. As soon as ERROR is set, the precise error code is available in the STATUS output. ERROR and STATUS retain their value as long as EXECUTE is set. |

General sequence of the Ident profile

##### Parameter assignment for starting up and restarting

The communications module and the reader are restarted by setting the "INIT" parameter. With the parameter, the CM or the reader and the Ident profile are reassigned parameters and synchronized.

An "INIT" is necessary after

- switching on or restarting the SIMATIC controller (OB 100 / Startup)
- turning on the power supply of the CM/reader
- plugging the reader onto the CM
- interruption in PROFIBUS/PROFINET communication
- An error message by the "STATUS" parameter

##### Chaining

With the Ident profile and the "Advanced" block, it is possible to send chained commands. Chained commands are sent in their entirety to the reader without waiting for the results of the first command. This function allows you to execute various transponder commands with one command start.

With both blocks, you have a command buffer of 100 commands available ("Array [1...n]" of the "IID_CMD_STRUCT"). In each command structure, there is a "Chained" bit. This bit must be set for each chained command. In the last chained command, this bit must not be set so that the block recognizes that the chain has ended.

> **Note**
>
> **Chaining function is device-specific**
>
> Please check whether or not the Ident device you are using supports chaining.
>
> At the time of publication of this manual, chaining is not supported by the communication modules RF120C, RF170C and RF180C.

###### Overview of the commands

Overview of the commands with which chaining is possible

| Command | Command code |  | Description |
| --- | --- | --- | --- |
| HEX | ASCII |  |  |
| PHYSICAL-READ | 0x70 | 'p' | Reads data from a transponder / optical reader system by specifying the physical start address, the length and the password. |
| PHYSICAL-WRITE | 0x71 | 'q' | Writes data to a transponder / optical reader system by specifying the physical start address, the length and the password. |
| READER-STATUS | 0x74 | 't' | Reads out the status of a communications module. This command must not be the last command within the chain. |
| TAG-STATUS | 0x73 | 's' | Reads out the status of a transponder. |
| INVENTORY | 0x69 | 'i' | Requests a list of all currently accessible transponders within the antenna range. |
| FORMAT | 0x66 | 'f' | Initializes the transponder. |
| PUT | 0x65 | 'e' | Transfers further commands not specified in the standard profile. To this end, a corresponding data structure is defined in the send data buffer for each command. |
| WRITE-ID | 0x67 | ‘g‘ | RF61xR/RF68xR:  Writes a new EPC-ID to the transponder. |
| KILL-TAG | 0x6A | ‘j‘ | RF61xR/RF68xR:  The transponder is permanently deactivated. |
| LOCK-TAG-BANK | 0x79 | ‘y‘ | RF61xR/RF68xR:  Defines a password for transponder access. |

###### Example of command structure

Example of a command structure with 3 commands (without EPC-ID)

| Command | Parameter | Value | Description |
| --- | --- | --- | --- |
| Command 1 | IID_CMD_STRUCT[2].CMD | 0x69 | Execute an inventory with a duration of 2 inventories. |
| IID_CMD_STRUCT[2].ATTRIBUTES | 0x80 |  |  |
| IID_CMD_STRUCT[2].EXT_UHF. INVENTORY.DURATION | 2 |  |  |
| IID_CMD_STRUCT[2].EXT_UHF. INVENTORY.DUR_UNIT | 1 |  |  |
| IID_CMD_STRUCT[2].OPTIONS.CHAINED | true |  |  |
| Command 2 | IID_CMD_STRUCT[3].CMD | 0x70 | Read 10 bytes from the user bank starting at address 0. |
| IID_CMD_STRUCT[3].EXT_UHF. MEM_BANK | 3 |  |  |
| IID_CMD_STRUCT[3].LEN_DATA | 10 |  |  |
| IID_CMD_STRUCT[3].ADDR_TAG | 0 |  |  |
| IID_CMD_STRUCT[3].OPTIONS.CHAINED | true |  |  |
| Command 3 | IID_CMD_STRUCT[4].CMD | 0x71 | Write 10 bytes to the user bank starting at address 20. |
| IID_CMD_STRUCT[4].EXT_UHF. MEM_BANK | 3 |  |  |
| IID_CMD_STRUCT[4].LEN_DATA | 10 |  |  |
| IID_CMD_STRUCT[4].ADDR_TAG | 20 |  |  |
| IID_CMD_STRUCT[4].OPTIONS.CHAINED | false |  |  |

In the chaining, the entire "IID_CMD_STRUCT" buffer ("IID_CMD_STRUCT[1...n]") can be used. The start of the chain is set with the "CMDSEL" parameter.

If several commands are executed in the chain for which data is returned, the position of the data in the receive buffer "RXREF" can be set for each individual command using the "IID_CMD_STRUCT[x].OFFSETBUFFER" parameter.

> **Note**
>
> **"IID_CMD_STRUCT[1]" reserved for "INIT"**
>
> In the Ident profile, the "IID_CMD_STRUCT[1]" parameter is normally reserved for "INIT". If you want to use "IID_CMD_STRUCT[1]" for another command, make sure that the reset parameters are written into this parameter when there is an "INIT".

##### Command repetition

The Ident profile supports command repetition (Repeat command).

> **Note**
>
> **Command repetition is device-specific**
>
> Please check whether the Ident device you are using supports command repetition.
>
> At the time of publication of this manual, command repetition is supported by the RF61xR/RF68xR readers (as of V3.0) and communications modules ASM 456 (as of V5.0), RF166C and RF18xC/RF18xCI.

###### How it works

After restart (or "INIT") of the reader, the Ident profile transfers the command or command chain once to the reader. Transmission of the command is automatic with the first "EXECUTE". This command (or the last command or the command chain) always remains buffered on the reader. If command repetition is started, the temporarily stored command on the reader is executed again, and the result(s) transferred to the Ident profile.

Make sure that the commands in the "EPCID/UID" parameter to be repeated have the value 0. If the EPC-UID has a different value, an error message is generated.

**Effects of command repetition**

- The data transfer on PROFIBUS/PROFINET is minimized. This reduction has a positive effect particularly with extensive bus configurations and slow transmission speeds.
- The reader processes each transponder regardless of the Ident profile. This has a particularly advantageous effect on gate applications since all transponders are always identified with the full reader scan speed.
- Total data throughput is increased considerably particularly with controllers that have few system resources for acyclic frames.

###### Overview of the commands

Overview of the commands with which command repetition is possible

| Command | Command code |  | Description |
| --- | --- | --- | --- |
| HEX | ASCII |  |  |
| PHYSICAL-READ | 0x70 | 'p' | Reads data from a transponder / optical reader system by specifying the physical start address, the length and the password. |
| PHYSICAL-WRITE | 0x71 | 'q' | Writes data to a transponder / optical reader system by specifying the physical start address, the length and the password. |
| READER-STATUS | 0x74 | 't' | Reads out the status of the reader. |
| TAG-STATUS | 0x73 | 's' | Reads out the status of a transponder. |
| INVENTORY | 0x69 | 'i' | Requests a list of all currently accessible transponders within the antenna range. |
| FORMAT | 0x66 | 'f' | Initializes the transponder. |
| KILL-TAG | 0x6A | ‘j‘ | The transponder is permanently deactivated. |
| LOCK-TAG-BANK | 0x79 | ‘y‘ | Defines a password for transponder access. |

###### Starting command repetition

You have the option of using command repetition with or without transfer of the command. The various procedures are described below.

**Sequence of the repeat command with simultaneous command transfer:**

1. If applicable, enable the "Presence_Mode".
2. Start the command using the input parameter "EXECUTE" while "RPTCMD" is set at the same time. ①

   The command is processed and the result transferred to the Ident profile.

   The Repeat command is activated on the reader.
3. The reader confirms activation with the output parameter "RPTACT" of the Ident profile. The confirmation is made only after the first command has been executed. ②

   The reader executes the command automatically as soon as a transponder is identified in the antenna field.

   If the reader does not support the Repeat command, "RPTACT" remains inactive. If "EXECUTE" is nevertheless set, the error "0xE7FE0900" is output after a timeout of 10 seconds.
4. You can read out the individual results by repeatedly setting the "EXECUTE" input parameter. ③

![Sequence of the repeat command with simultaneous command transfer](images/72181768843_DV_resource.Stream@PNG-de-DE.png)

Sequence of the repeat command with simultaneous command transfer

**Sequence of the repeat command without command transfer:**

This sequence is only possible if the command involved has already been transferred.

1. If applicable, enable the "Presence_Mode".
2. Set the "RPTCMD" input parameter. ①

   The Repeat command is activated on the reader.
3. The reader confirms activation with the output parameter "RPTACT" of the Ident profile. The confirmation is made only after the first command has been executed. ②

   If the reader does not support the Repeat command, "RPTACT" remains inactive. If "EXECUTE" is nevertheless set, the error "0xE7FE0900" is output after a timeout of 10 seconds.
4. You can read out the individual results by repeatedly setting the "EXECUTE" input parameter. ③

![Sequence of the repeat command without command transfer](images/63821070859_DV_resource.Stream@PNG-de-DE.png)

Sequence of the repeat command without command transfer

###### Ending command repetition

You have the option of ending command repetition by resetting "RPTCMD" or using the "INIT" or "SRESET" commands. The various procedures are described below

**Ending the Repeat command and reset "RPTCMD":**

1. Reset the "RPTCMD" input parameter. ①
2. Fetch any existing acknowledgments using the "EXECUTE" input parameter. ②

   The "RPTACT" output parameter remains set by the reader as long as there are acknowledgments present.
3. When there are no more acknowledgments, "RPTACT" is reset by the reader. ③

![Ending the Repeat command by resetting "RPTCMD" (ended normally)](images/63821254539_DV_resource.Stream@PNG-de-DE.png)

Ending the Repeat command by resetting "RPTCMD" (ended normally)

The "RPTACT" output parameter is reset by the reader. Under certain circumstances, it is possible that resetting "RPTACT" will be delayed. In other words, not at the same time as the "DONE" of the last acknowledgment. If the block is now restarted with "EXECUTE" and "RPTACT" is still set although there are no longer any results in the buffer, the block is not ended (BUSY = 1). In this case, you can wait until the next transponders are read out. As an alternative, the block can be ended with "INIT" or "SRESET".

![Ending the Repeat command by resetting "RPTCMD" (the last command remains pending)](images/70710458123_DV_resource.Stream@PNG-de-DE.png)

Ending the Repeat command by resetting "RPTCMD" (the last command remains pending)

> **Note**
>
> **Ending the Repeat command with "INIT" or "SRESET"**
>
> End the Repeat command using the input parameters "INIT" or "SRESET" if it is not known how many transponders were still processed after resetting the "RPTCMD" input parameter.
>
> Normally, an "SRESET" is performed significantly faster because no reset routine is run through.

**Ending the Repeat command with "INIT":**

1. Reset the "RPTCMD" input parameter and set the "INIT" input parameter. ①

   If "RPTCMD" is not reset, the Repeat command is activated again on the reader. This response triggers an error message because there is no command.
2. The reader resets the "RPTACT" output parameter due to the "INIT" input parameter. ②

**Ending the Repeat command with "SRESET":**

1. Reset the "RPTCMD" input parameter and set the "SRESET" input parameter. ①
2. The "DONE" output parameter is set and the reader resets the "RPTACT" output parameter. ②

![Ending the Repeat command with "INIT"/"SRESET"](images/63821305995_DV_resource.Stream@PNG-de-DE.png)

Ending the Repeat command with "INIT"/"SRESET"

###### Data buffer

Permanent command repetition can lead to the data being transferred more slowly to the Ident profile than new transponders are processed. All communication modules and a few readers have a data buffer that is used as buffer for the command sequence (chaining) and for the results (e.g. Repeat command). When the data buffers are full, no new data can be read from or written to the transponder; in other words, newly arriving transponders are no longer processed.

Devices that support command repetition and save results

| Device type | Number of buffers for chained commands and results | Max. user data that can be  processed with command repetition |
| --- | --- | --- |
| RF360R <sup>1)</sup> | 270 | 270 × 1034 bytes = 279 180 bytes |
| 150 | 150 × 480 bytes = 72 000 bytes |  |
| RF61xR/RF68xR | 250 | 250 × 1034 bytes = 258 500 bytes |
| RF180C | 150 | 150 × 233 bytes = 34 950 bytes |
| RF18xC/RF18xCI | 270 | 270 × 1034 bytes = 279 180 bytes |
| RF166C | 270 | 270 × 229 bytes = 61 830 bytes |
| ASM 456 | 150 | 150 × 233 bytes = 34 950 bytes |
| <sup>1)</sup> As of FW > V2.0, the Repeat command is supported. When using the Repeat command, the number of buffers is reduced to 150. |  |  |

The devices listed below support the command repetition and have the necessary data buffer. However, the data buffer is only used as buffer for the command sequence (chaining) and not for saving results.

Devices that support command repetition

| Device type | Buffer number for a concatenated command | Max. user data that can be  processed with command repetition |
| --- | --- | --- |
| RF300 reader; 1st gen. | 245 | 245 × 233 bytes = 57 085 bytes |
| RF300 reader; 2nd gen. <sup>1)</sup> | 299 | 299 × 233 bytes = 69 667 bytes |
| 150 | 150 × 480 bytes = 72 000 bytes |  |
| <sup>1)</sup> As of FW > V1.7, the number of buffers is reduced to 150 by using the "RF300 fast protocol". |  |  |

> **Note**
>
> **Restriction of command repetition**
>
> In the case of RFID systems with unique tag IDs (UID or EPC-ID) (e.g. RF300, RF600, MOBY U), the stored command is only repeated when different transponders enter the antenna field. If the same transponder (identical UID / EPC-ID) enters the antenna field again and again, the transponder will not be processed again.

### Error messages

This section contains information on the following topics:

- [Structure of the "STATUS" output parameter](#structure-of-the-status-output-parameter)
- [Errors from the communications module/reader](#errors-from-the-communications-modulereader)
- [Errors from the optical reader](#errors-from-the-optical-reader)
- [Errors from the bus/backplane bus](#errors-from-the-busbackplane-bus)
- [Warnings](#warnings)

#### Structure of the "STATUS" output parameter

There is always an error status in the Ident profile function if the output parameter "ERROR = TRUE" is set. The error can be analyzed (decoded) using the "STATUS" output parameter.

The "STATUS" output parameter is made up of the following 4 bytes:

Bytes of the "STATUS" output parameter

| Byte | Meaning |
| --- | --- |
| Byte 3 (least significant byte) | Warnings  In this byte, each bit has a separate meaning. |
| Byte 2 | Error code |
| Byte 1 | Error number  This byte defines the meaning of the error code and the warnings. The error numbers have the followinig meaning:  - 0x00 - no error, no warning - 0x81...0x8F - The controller reports an error according to the parameter "x" (0x8x). - 0xFE - error from the Ident profile or communications module/reader |
| Byte 0 | Instruction numbers  - Cx - Error in fieldbus communication - E1 - transponder-related error - E2 - error on the air interface - E4 - reader hardware fault - E5 - error in the communication between reader and FB - E6 - error in the user command - E7 - error message generated by the FB - F0 - Warnings |

#### Errors from the communications module/reader

The causes of these errors can, for example, be as follows:

- Errors have occurred in communication between the CM and the reader or between the reader and the transponder.
- The communications module is unable to process the command.

Byte 3 of the "STATUS" is not relevant for the error messages.

Error messages from communications module/reader or from the Ident profile via the "STATUS" output parameter

| Error message  (hex) | Description |
| --- | --- |
| 0xE1FE0100 | Memory of the transponder cannot be written to   - Transponder memory is defective. - Transponder EEPROM was written too frequently and has reached the end of its service life. - Transponder is write protected (Memory Lock) |
| 0xE1FE0200 | Presence error  The transponder has moved out of the transmission window of the reader. The command was executed only partially.   Read command: "IDENT_DATA" has no valid data.  Write command: The transponder that has just left the antenna field contains an incomplete data record.  Possible causes:  - Operating distance from reader to transponder is not being maintained. - Configuration error: The data record to be processed is too large (in dynamic mode). - With timeout: No transponder in the antenna field |
| 0xE1FE0300 | Address error  The address area of the transponder has been exceeded.  Possible causes:   - Start address at command start is incorrectly set. - Transponder is not the correct type. - The area to be written to is write-protected.   Freeport: Address ≠ "0x0000", "0x0002", "0xFFFF" |
| 0xE1FE0400 | Initialization error  Transponder is unable to execute the initialization command.  Possible causes:  - Transponder is defective. |
| 0xE1FE0500 | The transponder memory is full. |
| 0xE1FE0600 | Error in transponder memory  - The transponder has never been written to or has lost the contents of its memory due to battery failure. Possible causes / action to be taken:   - Replace transponder (if battery bit is set).   - Re-initialize transponder. - RF300: Data storage was not completed correctly for the semaphore procedure. |
| 0xE1FE0700 | - Password error - RF300: ECC error   Possible causes:   - The bit error could not be corrected.   - Transponder data has been lost (transponder defective).   - The transponder was not initialized with the ECC driver.   - The EEPROM memory of the transponder has reached its end of life and the data has been lost.   - The transponder (with FRAM memory) has been stored too hot and has lost information.  It is possible that the transponder can still be used after initialization. |
| 0xE1FE0800 | The transponder in the antenna field does not have the expected UID / EPC ID or has no UID / EPC ID. |
| 0xE1FE0900 | The command is not supported by the transponder. |
| 0xE1FE0A00 | The transponder is read/write-protected. |
| 0xE1FE8100 | The transponder is not responding. |
| 0xE1FE8200 | The transponder password is incorrect. Access is denied. |
| 0xE1FE8300 | The verification of the written transponder data has failed.  Possible causes:  - Transponder is defective. - Transponder is in the limit area. |
| 0xE1FE8400 | General transponder error   Contact Support if needed. |
| 0xE1FE8500 | The transponder has too little power to execute the command.  Possible causes:  - Transponder is in the limit area. - The transmission/radiated power of the reader or antenna is too low. |
| 0xE2FE0100 | Field disturbance on reader  Possible causes:  - The reader is receiving interference pulses from the environment.   - External interference field. The interference field can be detected with the "inductive field indicator" of the mobile reader.   - The distance between two readers is too small and does not correspond to the configuration guidelines.   - The connecting cable to the reader is defective or too long or does not comply with the specification. - Too many transmit errors   The transponder was unable to receive the command or the write data from the communications module correctly even after several attempts.   - The transponder is positioned exactly in the limit area of the transmission window.   - Data transmission to the transponder is being affected by external interference. - CRC sending error   - The transponder reports CRC errors frequently (transponder is positioned in the limit area of the reader; transponder and/or reader has a hardware defect). - Only during initialization: CRC error on receipt of acknowledgment from transponder (cause as for field interference on the reader). - When formatting, the transponder must be in the transmission window of the reader; otherwise, a timeout error will occur, i.e.:   - The transponder is located exactly in the limit area of the transmission window.   - The transponder is defective and consumes too much power.   - The EEPROM transponder was incorrectly configured by "FORMAT". - RF600:   - No ETSI channel is available.   - An incorrect communication standard was selected in the "INIT" command.   - The expert parameter is incorrect.   - The performance check of the ETSI wireless profile is faulty. - Freeport: Negative acknowledgment or bad frame from the reader |
| 0xE2FE0200 | - More transponders are located in the transmission window than can be processed at the same time by the reader. - There is more than one transponder in the transmission window. |
| 0xE2FE8100 | There is no transponder with the required EPC ID/UID in the transmission window or there is no transponder at all in the antenna field. |
| 0xE2FE8200 | The requested data is not available. |
| 0xE2FE8300 | CRC error in reader-transponder communication. |
| 0xE2FE8400 | The selected antenna is not enabled. |
| 0xE2FE8500 | The selected frequency is not enabled. |
| 0xE2FE8600 | The carrier signal is not activated. |
| 0xE2FE8700 | There is more than one transponder in the transmission window. |
| 0xE2FE8800 | General radio protocol error |
| 0xE4FE0100 | Short circuit or overload of the 24 V outputs  - The reader is using too much current. - The reader cable is causing a short-circuit.   Possible consequences:  - The affected output is turned off - All outputs are turned off when total overload occurs - A reset can only be performed by turning the 24 V voltage off and on again - and then starting "Reset_Reader" |
| 0xE4FE0300 | - Error in the connection to the reader; the reader is not answering.   - The cable between the communication module and reader is wired incorrectly or there is a cable break.   - The 24 V supply voltage is not connected or is turned off or has failed briefly.   - Automatic fuse on the communication module has blown.   - Hardware defective.   - Another reader is in the vicinity and is active.   - Execute "INIT"/"WRITE-CONFIG" after correcting the error. - The antenna of the reader is turned off. A tag command to the communications module was started in this status.   - Turn on the antenna with the command "Antenna on/off".   - The antenna is turned on (turned off) and has received an additional turn on (turn off) command. - The mode in the "SET_ANT" command is unknown. - The antenna on the reader is turned off or the antenna or antenna cable is defective. |
| 0xE4FE0400 | - The buffer on the communications module or reader is not adequate to store the command temporarily. - Freeport: New data was received before existing data was retrieved.   - Scan mode: The latest data is lost.With the "Write" command, the oldest acknowledgments are lost without an error message being generated. |
| 0xE4FE0500 | The buffer on the communications module or reader is not adequate to store the data temporarily. |
| 0xE4FE0600 | The command is not permitted in this status or is not supported.  Possible causes:  - The "INIT" command has been concatenated. - RF600: Command repetition was started without "Presence mode". |
| 0xE4FE0700 | Startup message from reader/communication module  The reader or communications module was off and has not yet received a "Reset_Reader" ("WRITE-CONFIG") command.  Possible causes / action to be taken:  - Execute the "INIT" command. - The same physical address in the "IID_HW_CONNECT" parameter is being used more than once. Check your "IID_HW_CONNECT" parameter assignments. - Check the connection to the reader. - The device has not yet been restarted after the change to the transmission speed. |
| 0xE4FE8100 | The specified tag field of the transponder is unknown. |
| 0xE4FE8A00 | General error |
| 0xE4FE8B00 | No or bad configuration data/parameters were transferred.  Possible causes:   - You are accessing a read point that is not configured. |
| 0xE4FE8C00 | - Communication error between Ident profile and communications module. Handshake error.   Possible causes / action to be taken:   - UDT of this communications module is overwritten by other program sections   - Check parameter settings of communications modules in the UDT   - Check the Ident profile command that caused this error   - Start "INIT" after correcting the error - Backplane bus / PROFIBUS DP <sup>1)</sup> / PROFINET error occurred   This error is only indicated when access monitoring has been enabled in the PROFIBUS configuration.   Possible causes / action to be taken:   - Backplane bus / PROFIBUS DP / PROFINET bus connection was interrupted (wire break on the bus; bus connector on the communications module was briefly unplugged).   - Backplane bus / PROFIBUS DP / PROFINET master no longer addressing communications module   - Execute "INIT"   - The communications module has detected a frame interruption on the bus. The backplane bus, PROFIBUS or PROFINET may have been reconfigured (e.g. with HW Config or TIA Portal)   <sup>1)</sup> This error is only indicated when "Watchdog" has been enabled in the PROFIBUS configuration. |
| 0xE4FE8D00 | - Firmware error   Possible causes:    The firmware update was not run completely. - Internal communication error of the communication module/reader   Possible causes / action to be taken:   - Connector contact problem on the communications module / reader   - Hardware of the communication module/reader has a defect; → Send in communication module/reader for repair.   - After eliminating the error, execute the "INIT" command. - Internal monitoring error of the communication module/reader   Possible causes / action to be taken:   - Program execution error on the communications module / reader   - Switch supply voltage to communication module/reader off and on again.   - After eliminating the error, execute the "INIT" command. |
| 0xE4FE8E00 | The current command was aborted by the "WRITE-CONFIG" ("INIT" or "SRESET") command for the bus connector was pulled.  Possible causes:  - Communication with the transponder was aborted by "INIT". - This error can only be reported if there is an "INIT" or "SRESET". |
| 0xE5FE0100 | Incorrect sequence number order (SN) on the reader/communications module |
| 0xE5FE0200 | Incorrect sequence number order (SN) in the Ident profile  Possible cause: User mode "Ident profile/RFID standard profile" is not set in the device configuration. |
| 0xE5FE0400 | Invalid data block number (DBN) on the reader/communications module |
| 0xE5FE0500 | Invalid data block number (DBN) in the Ident profile |
| 0xE5FE0600 | Invalid data block length (DBL) on the reader/communications module |
| 0xE5FE0700 | Invalid data block length (DBL) in the Ident profile |
| 0xE5FE0800 | The previous command is still active or the buffer is full.  A new command was sent to the reader or communication module although the last command is still active.   - The active command can only be aborted with "INIT". - Before a new command can be started, "DONE bit = 1" must be set (exception "INIT"). - Two Ident profile calls were assigned the same "HW_ID", "CM_CHANNEL" and "LADDR" parameter settings. - Two Ident profile calls are using the same pointer. - After eliminating the error, execute the "INIT" command. - When working with command repetition (e.g., fixed code transponder), no data is being fetched from the transponder. The data buffer on the reader/communications module has overflowed. Transponder data has been lost. |
| 0xE5FE0900 | The reader or communications module executes a hardware reset ("INIT_ACTIVE" set to "1"). "INIT" is expected by the Ident profile (bit 15 in the cyclic control word). |
| 0xE5FE0A00 | The "CMD" command code and the relevant acknowledgment do not match. This can be a software error or synchronization error that cannot occur in normal operation. |
| 0xE5FE0B00 | Incorrect sequence of acknowledgement frames (TDB / DBN) |
| 0xE5FE0C00 | Synchronization error (incorrect increment of "AC_H / AC_L" and "CC_H / CC_L" in the cyclic control word). "INIT" had to be executed. |
| 0xE5FE8100 | Communications error between reader and communications module  Access denied |
| 0xE5FE8200 | Communications error between reader and communications module  Resource is occupied |
| 0xE5FE8300 | Communications error between reader and communications module  Functional error of the serial interface |
| 0xE5FE8400 | Communications error between reader and communications module  Other faults/errors |
| 0xE6FE0100 | Unknown command  The Ident profile sends an uninterpretable command to the reader.  Possible causes:  - The "AdvancedCmd" block was supplied with an incorrect "CMD". - The "CMD" input of the "AdvancedCmd" block was overwritten.   Freeport: Incorrect command parameters or unauthorized command chaining (incorrect length specification) |
| 0xE6FE0200 | Invalid command index (CI) |
| 0xE6FE0300 | - The communication module or reader was configured incorrectly.   Possible causes / action to be taken:   - Check the "INPUT" parameters in the Ident profile.   - Check the parameter assignment in HW Config / STEP 7 (TIA Portal).   - "WRITE-CONFIG" command has incorrect parameter settings.   - After a startup, the reader or communications module has still not received an "INIT". - The parameter assignment of the reader or communications module on PROFIBUS/PROFINET was incorrect and the command cannot be executed.   Possible causes / action to be taken:   - Length of the input/output areas too small for the cyclic I/O word.      Correct GSD file being used?   - User data length set with command (e.g. "READ") too high. - Error when processing the command   Possible causes / action to be taken:   - Bad data in the "AdvancedCmd" or "IID_CMD_STRUCT" (e.g. "WRITE" command with length = 0); check "AdvancedCmd" or "IID_CMD_STRUCT" and execute "INIT".   - Reader/communications module hardware defective: The reader or communications module receives bad data with "INIT".   - Inconsistent length specifications in the command - Wrong reset block was selected.   Possible causes / action to be taken:   - Use the reset block suitable for the Ident device.   - Technology object with RF68xR and RF120C: Regardless of the selected Ident device/system, use the "Reset_Reader" function block. |
| 0xE6FE0400 | Presence error  A transponder has passed through the transmission window of a reader without being processed.  - This error message is not reported immediately. Instead, the reader or communication module waits for the next write / read command. This command is replied to immediately with this error and the write/read command is not executed. The next command is executed normally again by the reader/communication module. - You can reset this error status using an "INIT". |
| 0xE6FE0500 | An error has occurred that makes a Reset_Reader ("WRITE-CONFIG") necessary.  Possible causes / action to be taken:  - The "WRITE-CONFIG" command is incorrect. - After eliminating the error, execute an "INIT". - Check the parameter "IID_HW_CONNECT". |
| 0xE6FE8100 | A parameter is missing. |
| 0xE6FE8200 | The parameter has an invalid format. |
| 0xE6FE8300 | The parameter type is invalid. |
| 0xE6FE8400 | Unknown parameter |
| 0xE6FE8500 | The command or the frame has an invalid format. |
| 0xE6FE8600 | The "Inventory" command failed. |
| 0xE6FE8700 | Read access to the transponder has failed. |
| 0xE6FE8800 | Write access to the transponder has failed. |
| 0xE6FE8900 | Writing the EPC ID/UID on the transponder has failed. |
| 0xE6FE8A00 | Enabling write protection on the transponder has failed. |
| 0xE6FE8B00 | The "Kill" command failed. |
| 0xE7FE0100 | In this state, only the "Reset_Reader" command ("WRITE-CONFIG" with "CMDSEL =1" and "CMD = 0x78") is permitted. |
| 0xE7FE0200 | - The command code "CMD" or the value in "CMDSEL" is not permitted.   Possible cause / action to be taken:    - The "CMDSEL" or "CMDDIM" parameter was set incorrectly. Check the parameters.   - The value of the parameter "CMDSEL" must be between 1 and 100 and may never be higher than the value of the "CMDDIM" parameter (max. 100). - With "Read_Tagfield/Write_Tagfield":   Impermissible value in the "TAGFIELD" parameter. The value must be between 1 ... 64. |
| 0xE7FE0300 | The value of the "LEN_DATA" parameter of the command is too long and does not match the global data reserved within the send data buffer (TXBUF). |
| 0xE7FE0400 | The receive data buffer (RXBUF) or the send data buffer (TXBUF) is too small, the buffer created at TXBUF/RXBUF/IDENT_DATA does not have the correct data type or the parameter "LEN_DATA" has a negative value.   Possible cause / action to be taken:   - Check whether the buffers TXBUF/RXBUF/IDENT_DATA are at least as large as specified in "LEN_DATA". - With S7-1200/1500:   - In the Ident instructions, only an "Array of Byte" may be created for TXBUF and RXBUF or IDENT_DATA.   - In the "Tag_Status" and "Reader_Status" blocks, only an "Array of Byte" or the corresponding data types ("IID_TAG_STATUS_XX_XXX" or "IID_READER_STATUS_XX_XXX") may be created. With all other blocks, only an "Array of Byte" may be created. |
| 0xE7FE0500 | Only an "INIT" command is permitted as the next command. All other commands are rejected. |
| 0xE7FE0600 | Wrong data record index of an acyclic data record   Permitted index is in the ranges "101 ... 108" and "-20401 ... -20418". |
| 0xE7FE0700 | The reader or communications module does not respond to "INIT" ("INIT_ACTIVE" is expected in the cyclic status message).   The next steps:   - Check the address parameter "LADDR". |
| 0xE7FE0800 | Timeout during "INIT" (60 seconds) |
| 0xE7FE0900 | Command repetition is not supported. |
| 0xE7FE0A00 | Error during the transfer of the PDU (Protocol Data Unit). |
| 0xE7FE0B00 | The "CMDREF" parameter was set incorrectly. Check the parameter.  The parameter "CMDREF" must be created as "ARRAY of IID_CMD_STRUCT" and may contain a max. of 100 elements. |
| 0xFxFExx00 | An "FxFExxxx" error is identical to the corresponding "ExFExxxx" error (see "ExFExxxx" error). Byte 3 contains additional warning information. |

#### Errors from the optical reader

In the event of error messages, the "IN_OP" signal (in operation) is reset and the "STATE/SF" LED is lit red permanently. In addition, the "Ready" or "Done" bit is reset with a connection via the Ident profile.

If the optical reader is connected to PROFINET IO, these error messages trigger a diagnostics interrupt on the relevant I/O controller. Refer to I/O diagnostics for a description of how to read out and evaluate the diagnostic information made available on the optical reader.

Error messages via the "STATUS" output parameter ("IN_OP" is reset)

| Error message  (hex) | Description |
| --- | --- |
| 0xE1FE0200 | The connection from the internal interface to the image sensor is disrupted.  If the error continues to occur after turning on the device again, contact technical support. |
| 0xE1FE0400 | Transmission error  The send buffer is full because the data cannot be queried in an adequately short time.  Reduce the trigger frequency or process the results faster.   If necessary, change the update time in the PROFINET configuration.  If necessary, the transmission speed of the CM connection can also be increased. To cover short peaks, the image buffer size of the program can be increased on the "Image acquisition", "Control" tab. |
| 0xE1FE0600 | Program cannot be started because there is not enough memory or the program is damaged.  Reduce the memory requirements and repeat "Save program". |
| 0xE1FE0700 | Comparison error  The program could not be created due to bad match settings.  Adapt the match settings or use a suitable test object. |
| 0xE4FE0400 | Internal file error  An error occurred while saving to read-only memory.  Please contact technical support if this error occurs frequently. |
| 0xE4FE0600 | Lamp overload  The connected lamp was overloaded. The configured or default "Maximum duty cycle" in "Options", "Lighting" tab, was exceeded.  Decrease the trigger frequency, reduce the exposure time or use a more powerful lamp. |
| 0xE4FE8400 | Error in last command sequence.  May occur if triggering is too fast. The Ident profile can only process one command before a new command can be executed. |
| 0xE6FE0400 | The program could not be created or saved.  - While the program is being saved, the DISA signal is changed at an invalid point or the time sequence of applied signals is not adhered to.   Check the sequence of applied signals. Start the program saving process again. - The program could not be created.   Adapt the parameter assignment, the placement of test objects in the image or the image quality. - An attempt is being made to save a program under an invalid number via the interface set in "Controller".   Select a program number between 1 and 15. For SIMATIC MV420 SR-B, 1 to 5 and 15 are valid program numbers. |

With the following errors, the "IN_OP" signal (in operation) is not reset and the "STATE/SF" LED is not lit red.

Messages via the "STATUS" output parameter ("IN_OP" is not reset)

| Message  (hex) | Description |
| --- | --- |
| 0xE1FE0300 | Bad parameter in MV command  The command was incorrectly structured. Possible causes:  - The specified address for a "WRITE" command is ≠ "0x0000". - MV command program change    - Length of the data to be written > "0x1".   - Program number transferred is > "0xF".   The transferred program number is not saved. |
| 0xE6FE0100 | Command not permitted or the command was aborted.  The precise error message can be obtained with "INIT" without program selection. Possible causes:   - The send buffer is full. - The program is damaged. - The Ethernet interface is in operation and there is a problem. - The connected lamp is overloaded. - Match string access failed due to missing parameter assignment. |
| 0xE6FE0300 | Initialization with program selection ("INIT"/"WRITE-CONFIG") is not possible. Possible causes:  - Program number transferred is not stored. - Reader is still in self-test. |

#### Errors from the bus/backplane bus

The transport layer of the bus system being used (backplane bus, PROFIBUS, PROFINET) is signaling an error. For precise troubleshooting and analysis, a PROFIBUS tracer can be useful. For PROFINET, the open source software "Wireshark" can be used. The PROFIBUS or PROFINET system diagnostics can provide further information about the cause of the error.

Error messages that start with "80/C0/DE/DF" relate to errors from the bus/backplane bus. You will find details of the error message in the STEP 7 help on the blocks "WRREC" or "RDREC" (SFB52/SFB53).

#### Warnings

Byte 3 of the "STATUS" output parameter indicates warnings if byte 0 of the "STATUS" (function numbers) has the value "Fx" or "Dx".

Possible warnings when working with the Ident profile

| Bytes 0...2 | Byte 3 | Meaning |
| --- | --- | --- |
| FxFExx | Bit 0 | The bit is always set to "0" |
| Bit 1 | The ECC mode has corrected a 1-bit error. |  |
| Bit 2 | Battery low |  |
| Bit 3 | Depends on the manufacturer |  |
| Bit 4 | Depends on the manufacturer |  |
| Bit 5 | Depends on the manufacturer |  |
| Bit 6 | Depends on the manufacturer |  |
| Bit 7 | Depends on the manufacturer |  |
