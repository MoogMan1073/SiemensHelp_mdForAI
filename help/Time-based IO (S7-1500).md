---
title: "Time-based IO (S7-1500)"
package: ProgFBTIOenUS
topics: 8
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Time-based IO (S7-1500)

This section contains information on the following topics:

- [TIO_SYNC: Synchronizing TIO modules (S7-1500)](#tio_sync-synchronizing-tio-modules-s7-1500)
- [TIO_IOLink_IN: Read process input signals with time stamps (S7-1500)](#tio_iolink_in-read-process-input-signals-with-time-stamps-s7-1500)
- [TIO_DI: Reading in edges at digital input and associated time stamps (S7-1500)](#tio_di-reading-in-edges-at-digital-input-and-associated-time-stamps-s7-1500)
- [TIO_DI_ONCE: Reading in edges once at the digital input and associated time stamps (S7-1500)](#tio_di_once-reading-in-edges-once-at-the-digital-input-and-associated-time-stamps-s7-1500)
- [TIO_IOLink_OUT: Output time-controlled process output signals (S7-1500)](#tio_iolink_out-output-time-controlled-process-output-signals-s7-1500)
- [TIO_DQ: Output edges time-controlled at the digital output (S7-1500)](#tio_dq-output-edges-time-controlled-at-the-digital-output-s7-1500)
- [UDT TIO_SYNC_Data (S7-1500)](#udt-tio_sync_data-s7-1500)

## TIO_SYNC: Synchronizing TIO modules (S7-1500)

### Description

TIO_SYNC is the basis for all other TIO instructions. TIO_SYNC synchronizes TIO modules to a shared time basis TIO_Time.

You can synchronize up to 8 TIO modules with TIO_SYNC. All TIO modules must be assigned to the same process image partition (PIP). If you select "0" for the input parameter PIP_Mode, you assign the number of the process image partition at the PIP_PART input parameter.

Additional information on configuration of Time-based IO is available in the [Configuration and parameter assignment](High-precision%20input-output%20with%20time-based%20IO%20%28S7-1500%29.md#configuring-and-parameter-assignment-s7-1500) section.

### Startup characteristics

At the startup of the CPU, the TIO_SYNC instruction receives and checks the input parameters once and initializes the TIO_Time.

You have several options for handling the optional parameters SendClock, AppCycleFactor and ToTimes:

- SendClock, AppCycleFactor and ToTimes can be read in automatically each time the system is started. This results in a time delay during startup, but the values are always consistent.
- Automatically read in SendClock, AppCycleFactor and ToTimes at each startup and apply the read-in values as set values during commissioning. This results in fast subsequent startups, but is inconsistent after changes in the hardware configuration (repeat commissioning necessary).
- Manually define SendClock, AppCycleFactor and ToTimes before the first call of the instruction, for example, in OB100:

  ![Startup characteristics](images/123658084491_DV_resource.Stream@PNG-de-DE.png)

  This results in a fast startup, but you need to manually update the values after changes to the hardware configuration.

  You will find information about the parameters in the table below.

> **Note**
>
> **Automatic reading of SendClock, AppCycleFactor and ToTimes is recommended**
>
> The automatic reading of SendClock, AppCycleFactor and ToTimes is recommended to ensure the consistency of the parameters even with subsequent changes in the hardware configuration. You activate the automatic reading via the parameter value AppCycleFactor = 0.

If startup takes place without errors, the instruction changes to normal operation. In the event of an error, the instruction does not change to normal operation and generates an error message.

### Operating principle

In normal operation, the instruction ensures synchronization of all TIO modules configured at the HWID input.

The calculated TIO_Time for the instructions of the TIO modules is provided at the TIO_SYNC_Data output.

### Reaction to error

The Error output indicates if the instruction was processed correctly. In the event of an error, the cause of the error is displayed at the Status output.

### Parameter

The table below shows the parameters of the TIO_SYNC instruction.

| Parameter | Declaration in library version |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| &lt; V2.0 | ≥ V2.0 | S7-1500 |  |  |  |
| HWID_1 ... HWID_8* | Input |  | HW_IO | 65535 | Hardware identifier for TIO module from hardware configuration |
| PIP_Mode* | Input |  | PIP | 0 | Mode for the data update**:   - 0: OIP model with internal update of the process image by SYNC_PO and SYNC_PI. - 1: OIP model without internal update of the process image - 2: IPO model without internal update of the process image |
| PIP_PART* | Input |  | USInt | 1 | Only relevant if PIP_Mode = 0  Number of the process image partition which is to be updated isochronously. |
| TIO_SYNC_ Data | Output |  | "TIO_ SYNC_ Data" |  | Calculated system time for the TIO instructions of the TIO modules and internal data used for synchronization. See [UDT TIO_SYNC_Data](#udt-tio_sync_data-s7-1500). |
| Status | Output |  | DWord | 16#0 | Status of the instruction: see description of Status parameter |
| Error | Output |  | Bool | False | Error = True: An error has occurred. For detailed information see Status parameter.  Error is reset as soon as the error is corrected. |
| OperatingState |  | Static | Int | 0 | Internal operating state of the instruction:  - 0: Input parameters are checked - 1: Optional parameters are read out - 2: Read-out parameters are checked - 3: Normal operation (all parameters OK, TIO modules synchronized)   As soon as operating state 3 is reached, time stamps can be read in and edges can be output. If you want to repeat the synchronization of the TIO modules and the readout of the optional parameters, you can set the operating state to 0. |
| SendClock | Input | Static | LTime | LT#0ns | Send clock of the sync domain.  Apply the send clock from the PROFINET configuration.   Note: If you use the parameter value AppCycleFactor = 0, SendClock can be left as the default (automatic reading of the parameters). |
| AppCycleFactor |  | Static | UInt | 0 | Application cycle factor:  - Range of values: 0 &lt;= AppCycleFactor &lt;= 85 - 0: SendClock, AppCycleFactor and ToTimes are read in automatically   The application cycle T<sub>APP</sub> is calculated as follows:  T<sub>APP</sub> = AppCycleFactor × SendClock |
| ToTimes |  | Static | LTime array [1...8] | LT#0ns | T<sub>o</sub> for each TIO module: Time for output of isochronous output data.  Note: If you use the parameter value AppCycleFactor = 0, ToTimes can be left as the default (automatic reading of the parameters). |
| * Checked once at startup of the CPU  ** The IPO model (PIP_Mode = 2) provides the shortest response times, but it also places the highest demands on system performance. Processing of all TIO instructions and other program sections must be completed within one send clock. Select the OIP model (PIP_Mode = 0) only if you use only one instance of the TIO_SYNC instruction per process image partition so that the SYNC_PI and SYNC_PO instructions are not called more than once in the isochronous OB. In addition, do not call SYNC_PI and SYNC_PO in the other program sections in the OIP model. |  |  |  |  |  |

> **Note**
>
> The TIO instructions must be called in an "MC-PreServo" OB.
>
> If you use an OB of the "MC-PostServo" type, you can decide separately for each TIO model whether it is used with Motion Control technology objects or with TIO instructions.
>
> If you call TIO_SYNC in an "MC-PostServo" type OB, you need to use PIP_Mode = 2 and also cannot use any reduction ratio.

### Status parameter

Error codes or status information is output as double word at the Status output.

The double word is divided as follows:

| Error code | Meaning |
| --- | --- |
| (DW#16#...) |  |
| z0yywwww | Error of a system function:   - during startup (z = 1) - during normal operation (z = 0)   System functions with subordinate use are coded in yy: See table with error codes.  wwww specifies the RET_VAL of the system function. The error information is available in the help for the system function. |
| z0yy0000 | An error that does not originate in a system function. This error receives a consecutive error number yy.   The error can occur:   - during startup (z = 1) - during normal operation (z = 0) |

**Table with error codes**

| Error code | Meaning | Solution |
| --- | --- | --- |
| (DW#16#...) |  |  |
| 00000000 | No error. | — |
| 1001xxxx | An error has occurred with system function RD_SINFO. The low word xxxx displays the error information of the RET_VAL return value from RD_SINFO. | - Read the description of the RD_SINFO in the STEP 7 (TIA Portal) information system. - Make sure that TIO_SYNC is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10020000 | The read cycle time of the isochronous OB is invalid (LT#0ms or negative).  The instruction can only be used without errors in an isochronous OB. | - Correct the value of the cycle time. - Make sure that TIO_SYNC is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10030000 | The TIO_SYNC instruction is not called in an isochronous OB. The instruction can only be used without errors in an isochronous OB. | Make sure that TIO_SYNC is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10040000 | The assigned value at the PIP_Mode input parameter is outside the valid range of 0 to 2. | Correct the value at the PIP_Mode input parameter. |
| 10050000 | The configured send clock is outside the permitted range of 0 &lt; SendClock &lt;= 4 ms. | Correct the value of the send clock. |
| 0006xxxx* | An error has occurred during execution of the SYNC_PI system function. The low word xxxx displays the error information of the RET_VAL return value from SYNC_PI. | Read the description of the SYNC_PI in the STEP 7 (TIA Portal) information system. |
| 0007xxxx* | An error has occurred during execution of the SYNC_PO system function. The low word xxxx displays the error information of the return value RET_VAL from SYNC_PO. | Read the description of the SYNC_PO in the STEP 7 (TIA Portal) information system. |
| 10080000 | At least one of the hardware identifiers does not belong to a TIO module. | Check the values of input parameters HWID_1 to HWID_8. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. |
| 10090000 | HWID_1 is not a valid hardware identifier.  Possible causes:  - No module with this hardware identifier available. - The CPU went to RUN mode before the module was supplied with voltage. | Check the value of the respective input parameter. In each case, specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| 100A0000 | HWID_2 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 100B0000 | HWID_3 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 100C0000 | HWID_4 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 100D0000 | HWID_5 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 100E0000 | HWID_6 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 100F0000 | HWID_7 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 10100000 | HWID_8 is not a valid hardware identifier.  Possible cause: No module with this hardware identifier available. |  |
| 10110000 | The value at input parameter PIP_PART is outside the valid range of 1 ... 31. | Correct the value at the PIP_PART input parameter. |
| 10120000 | The value "2" is configured at the input parameter PIP_Mode, while the value &gt; 1 (reduction ratio) is configured at the static parameter AppCycleFactor. | Correct the value at the PIP_Mode input parameter. PIP_Mode with the value "2" does not allow a reduction ratio. |
| x0130000 | MC-Servo (OB91) is not isochronous to the bus cycle time. | Correct the value of the cycle time of the MC-Servo to the value of the bus cycle time.  Note:  Calling TIO instructions in an OB of the type "MC-PostServo" with reduction ratio "MC-Servo" can result in incorrect calculation of time stamps. |
| x014xxxx | An error has occurred when reading the data record. The low word xxxx indicates the error information of the instruction RDREC. | Read the description of the instruction RDREC in the STEP 7 (TIA Portal) information system. |
| x0FF0000 | General internal error. | — |
| * Available only when "0" is selected for the input parameter PIP_Mode. |  |  |

## TIO_IOLink_IN: Read process input signals with time stamps (S7-1500)

### Description

You can use the Time-based IO with the TIO_IOLink_IN instruction. TIO_IOLink_IN detects an event at the IO-Link Device and returns the process value including the associated time stamp.

The IO-Link Device must be equipped with the time stamp function and the Port must be in "IO-Link, Time based IN" mode.

### Startup characteristics

During startup of the CPU, the instruction TIO_IOLink_IN applies the input parameters once and checks the following:

- Checking HWID
- Checking whether the Port number is in the range (1 to 4)
- Checking TIO_SYNC_Data.Error: Is an error present at TIO_SYNC?
- Checking T<sub>o</sub> for a positive value
- Checking the setting to type IO-Link
- Checking Port mode regarding configuration for IO-Link Time based IN
- Checking whether the OB is a "Synchronous Cycle" OB
- Checking PortQualifier

If startup takes place without errors, the instruction changes to normal operation. In the event of an error, the instruction does not change to normal operation and generates an error message.

### Functional description

In normal operation, the instruction detects the process data (SA_Data) of an IO-Link Device and the associated time stamp (time = TIO_Time) of the last valid change. Each valid change of the SA_Data with a correctly functioning port is accompanied by a valid time stamp.

You connect the input TIO_SYNC_Data with the output of the same name of the TIO_SYNC instruction. This ensures a shared time basis.

### Reaction to error

The Error output indicates if the instruction was processed correctly. The reasons for the errors are displayed at the Status output.

### Parameter

The table below shows the parameters of the TIO_IOLink_IN instruction.

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| S7-1500 |  |  |  |  |
| HWID* | Input | HW_IO | 0 | Hardware identifier for TIO module from HWCN |
| Port* | Input | USInt | 0 | Port number (1 to 4) of the connected IO-Link Device |
| TIO_SYNC_Data* | Input | "TIO_SYNC_Data" |  | System time provided for the TIO instructions of the TIO modules by the TIO_SYNC instruction. See [UDT TIO_SYNC_Data](#udt-tio_sync_data-s7-1500).  Connect this input parameter with the "TIO_SYNC_Data" output parameter of the TIO_SYNC instruction. |
| TO* | Input | LTime | LT#0ns | T<sub>o</sub>: Time for output of isochronous output data.  Apply T<sub>o</sub> from the ET 200 station (properties of the PROFINET interface). |
| SA_Bit0 | Output | Bool | False | Display of a process data change (bit 0 of SA_Data).  SA_Bit0 is event-oriented. As long as no valid time stamp has been acquired (EventCount = 0), the process data is invalid. |
| SA_Bit1 | Output | Bool | False | Display of a process data change (bit 1 of SA_Data).  SA_Bit1 is event-oriented. As long as no valid time stamp has been acquired (EventCount = 0), the process data is invalid. |
| SA_Data | Output | DWord | 16#0 | Process data SA_Data (Sensor Application Data) |
| TimeStamp | Output | LTime | LT#0ns | Time stamp: Time when a change of the process signal SA-Data took place at the IO-Link Device. |
| EventCount | Output | UInt | 0 | Counter: Is incremented with each new, valid time stamp. The counter is reset with each CPU startup. |
| Status | Output | DWord | 16#0 | Status of the instruction: see description of Status parameter |
| Error | Output | Bool | False | Error = True: An error has occurred. For detailed information see Status parameter.  Error is reset as soon as the error is corrected. |
| * Checked once at startup of the CPU |  |  |  |  |

### Status parameter

Error codes or status information is output as double word at the Status output.

The double word is divided as follows:

| Error code | Meaning |
| --- | --- |
| (DW#16#...) |  |
| z0yywwww | Error of a system function:   - during startup (z = 1) - during normal operation (z = 0)   System functions with subordinate use are coded in yy: See table with error codes.  wwww specifies the RET_VAL of the system function. The error information is available in the help for the system function. |
| z0yy0000 | An error that does not originate in a system function. This error receives a consecutive error number yy.   The error can occur:   - during startup (z = 1) - during normal operation (z = 0) |

**Table with error codes**

| Error code | Meaning | Solution |
| --- | --- | --- |
| (DW#16#...) |  |  |
| 00000000 | No error. | — |
| 10010000 | The assigned number at the Port input parameter is outside the valid range of 1 to 4. | Correct the value at the Port input parameter. |
| 10020000 | The TIO_IOLink_IN instruction is not called in an isochronous OB. The instruction can only be used without errors in an isochronous OB. | Make sure that TIO_IOLink_IN is called in a "Synchronous Cycle" OB. |
| 10030000 | An error occurred when reading the HWID input parameter. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| x0040000 | The data in TIO_SYNC_Data is invalid/incorrect. | Check the TIO_SYNC instruction and the interconnection of its TIO_SYNC_Data output. |
| 1005xxxx | An error has occurred during execution of the RD_SINFO system function. The low word xxxx displays the error information of the RET_VAL return value from RD_SINFO. | - Read the description of the RD_SINFO in the TIA Portal information system. - Make sure that TIO_IOLink_IN is called in a "Synchronous Cycle" OB. |
| 10060000 | Unable to find IO-Link Device.  Possible cause: The module configured using the hardware identifier is not an IO‑Link Master for Time‑based IO. | - Make sure that the configured module is an IO‑Link Master for Time‑based IO. - Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. |
| 10070000 | An internal error occurred during the address calculation. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| 00080000 | TIO module is not synchronized using the TIO_SYNC instruction. | Check the instruction TIO_SYNC. |
| 10090000 | The read cycle time of the isochronous OB is outside the permitted range of 0 &lt; T<sub>APP</sub> &lt;= 16 ms and is therefore invalid.  The instruction can only be used without errors in an isochronous OB. | - Correct the cycle time. - Make sure that TIO_IOLink_IN is called in a "Synchronous Cycle" OB. |
| 100A0000 | The assigned time at the TO input parameter is outside the permitted range of 0 &lt; T<sub>o</sub> &lt;= 4 ms. | Correct the value at the TO input parameter. |
| 100Bxxxx | An error has occurred during execution of the RD_ADDR system function. The low word xxxx displays the error information of the RET_VAL return value from RD_ADDR. | Read the description of the RD_ADDR in the TIA Portal information system. |
| 000C0000 | The converted time stamp is invalid. | Check the connected sensor and the interaction between IO‑Link Master and sensor (e.g., configuration). |
| 000D0000 | The value status PortQualifier of the IO-Link indicates that the process data is invalid. | Check the connected sensor and its configuration. |
| 100E0000 | The configured port mode of the IO-Link is incorrect. | Check the configuration of the connected sensor with S7‑PCT. |
| x0FF0000 | General internal error. | — |

## TIO_DI: Reading in edges at digital input and associated time stamps (S7-1500)

### Description

TIO_DI continuously detects the edges at a digital input of a TIO module and returns the associated time stamps.

### Startup characteristics

During startup of the CPU, the instruction TIO_DI applies the input parameters once and checks the following:

- Checking HWID
- Checking to see if the number of the digital input (Channel) is in the permitted range (depending on addressed module and channel configuration)
- Checking TIO_SYNC_Data.ERROR: Is an error present at TIO_SYNC?
- Checking TIO_SYNC_Data.TO_TIMES for plausibility (0 ms to 4 ms)
- Checking to see whether the OB is isochronous

If startup takes place without errors, the instruction changes to normal operation. In the event of an error, the instruction does not change to normal operation and generates an error message.

### Functional description

In normal operation, the instruction detects the edges at a digital input and the associated time stamps of the last valid, defined edge pair from the preceding isochronous cycle. Use the input parameter EdgeSel to determine the edges for which time stamps are detected.

You connect the input TIO_SYNC_Data with the output of the same name of the TIO_SYNC instruction. This ensures a shared time basis.

The following figure shows an example of the behavior of LEC when a read-in job is started with EdgeSel = 3 (rising and falling edge, order depending on occurrence).

![Functional description](images/124491829131_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| T<sub>APP</sub> | Application cycle |
| Rn | Specified times of a positive DI edge |
| Fn | Specified times of a falling DI edge |

The module can count a maximum of seven edges per application cycle. LEC = 7 means therefore that seven or more edges have been counted.

### Reaction to error

The Error output indicates if the instruction was processed correctly. In the event of an error, the cause of the error is displayed at the Status output.

### Parameter

The table below shows the parameters of the TIO_DI instruction.

| Parameter | Declaration in library version |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| &lt; V2.0 | ≥ V2.0 | S7-1500 |  |  |  |
| HWID* | Input |  | HW_IO | 0 | Hardware identifier for TIO module from hardware configuration |
| Channel* | Input |  | UInt | 0 | Number (0 ... m) of the digital input of the connected TIO module |
| EdgeSel | Input |  | UInt | 3 | Specify the edges for which time stamps are detected:  0<sub>D</sub>: Invalid  1: Two rising edges  2: Two falling edges  3: Rising and falling edge (order depending on occurrence)  4: First rising, then falling edge  5: First falling, then rising edge  6 to 255: Invalid  EdgeSel can be changed during normal operation. |
| DI | Output |  | Bool | False | Status of digital input.  If an inversion of the digital input is configured, this parameter is inverted as well. |
| TimeStampRE | Output |  | LTime | LT#0ns | Time stamp: Time at which a positive edge was detected.  Exception: EdgeSel = 2: Time at which a falling edge has been detected (if multiple falling edges have occurred during the application cycle). |
| TimeStampFE | Output |  | LTime | LT#0ns | Time stamp: Time at which a falling edge was detected.  Exception: EdgeSel = 1: Time at which a rising edge has been detected (if multiple rising edges have occurred during the application cycle). |
| EventCountRE | Output |  | UInt | 0 | Counter: Is incremented with each new, valid time stamp at a positive edge. The counter is reset with each CPU startup. |
| EventCountFE | Output |  | UInt | 0 | Counter: Is incremented with each new, valid time stamp at a falling edge. The counter is reset with each CPU startup. |
| LEC | Output |  | UInt | 0 | Counter: Number of edges for which no time stamp could be saved. The module can count a maximum of seven edges per application cycle. The counter is reset with each new application cycle. |
| Status | Output |  | DWord | 16#0 | Status of the instruction: see description of Status parameter |
| Error | Output |  | Bool | False | Error = True: An error has occurred. For detailed information see Status parameter.  Error is reset as soon as the error is corrected. |
| TIO_SYNC_Data* | Input | InOut | "TIO_ SYNC_ Data" |  | System time provided for the TIO instructions of the TIO modules by the TIO_SYNC instruction. See [UDT TIO_SYNC_Data](#udt-tio_sync_data-s7-1500).  Connect this input parameter with the "TIO_SYNC_Data" output parameter of the TIO_SYNC instruction. |
| * Checked once at startup of the CPU |  |  |  |  |  |

### Status parameter

Error codes or status information is output as double word at the Status output.

The double word is divided as follows:

| Error code | Meaning |
| --- | --- |
| (DW#16#...) |  |
| z0yywwww | Error of a system function:   - during startup (z = 1) - during normal operation (z = 0)   System functions with subordinate use are coded in yy: See table with error codes.  wwww specifies the RET_VAL of the system function. The error information is available in the help for the system function. |
| z0yy0000 | An error that does not originate in a system function. This error receives a consecutive error number yy.   The error can occur:   - during startup (z = 1) - during normal operation (z = 0) |

**Table with error codes**

| Error code | Meaning | Solution |
| --- | --- | --- |
| (DW#16#...) |  |  |
| 00000000 | No error. | — |
| 10010000 | The assigned number of the digital input at the Channel input parameter is outside the permitted range (depending on addressed module and channel configuration). | Correct the value at the Channel input parameter. |
| 10020000 | The TIO_DI instruction is not called in an isochronous OB. The instruction can only be used without errors in an isochronous OB. | Make sure that TIO_DI is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10030000 | An error occurred when reading the HWID input parameter. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| x0040000 | The data in TIO_SYNC_Data is invalid/incorrect. | Check the TIO_SYNC instruction and the interconnection of its TIO_SYNC_Data output. |
| 1005xxxx | An error has occurred during execution of the RD_SINFO system function. The low word xxxx displays the error information of the RET_VAL return value from RD_SINFO. | - Read the description of the RD_SINFO in the STEP 7 (TIA Portal) information system. - Make sure that TIO_DI is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10060000 | No TIO module found.  Possible cause: The module configured using the hardware identifier is not a TIO module. | - Make sure that the configured module is a TIO module. - Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. |
| 10070000 | An internal error occurred during the address calculation. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| 00080000 | TIO module is not synchronized using the TIO_SYNC instruction.  The error code can also indicate that:  - A job was already present before the first run of the instruction. - The assigned number at the Channel input parameter is not a digital input. | Check the instruction TIO_SYNC. |
| 10090000 | The read cycle time of the isochronous OB is outside the permitted range of 0 &lt; T<sub>APP</sub> &lt;= 16 ms and is therefore invalid.  The instruction can only be used without errors in an isochronous OB. | - Correct the cycle time. - Make sure that TIO_DI is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 100A0000 | The time T<sub>O</sub> of the TIO model stored in TIO_SYNC_Data is outside the permissible range of 0 &lt; T<sub>o</sub> &lt;= 4 ms. | Check the instruction TIO_SYNC. |
| 100Bxxxx | An error has occurred during execution of the RD_ADDR system function. The low word xxxx displays the error information of the RET_VAL return value from RD_ADDR. | Read the description of the RD_ADDR in the STEP 7 (TIA Portal) information system. |
| 000C0000 | The converted time stamp is invalid.  Possible cause: Communication error | Check the communication with the TIO module. |
| 000D0000 | The Quality Information of the digital input indicates that an error has occurred at the digital input. | Check the supply voltage L+/1L+/2L+. |
| 000E0000 | The assigned number at the Channel input parameter is not a digital input configured as Timer DI. | - Check the channel configuration (only for TM Timer DIDQ 16x24V). - Check the operating mode of the digital input. |
| 000F0000 | The assigned value at the EdgeSel input parameter is outside the valid range of 1 to 5. | Correct the value at the EdgeSel input parameter. |
| 10100000 | The send clock is outside the permitted range of 0 &lt; SendClock &lt;= 4 ms and is therefore invalid.  The error code can also indicate that   - The data in TIO_SYNC_Data is invalid or does not exist. - The TIO_DI instruction is not called in an isochronous OB. | Correct the send clock. |
| x0130000 | MC-Servo (OB91) is not isochronous to the bus cycle time. | Correct the value of the cycle time of the MC-Servo to the value of the bus cycle time.  Note:  Calling TIO instructions in an OB of the type "MC-PostServo" with reduction ratio "MC-Servo" can result in incorrect calculation of time stamps. |
| 10140000 | The configured value at the HWID input parameter is not present in the structure at the TIO_SYNC_Data parameter. The HWID and TIO_SYNC_Data parameters are not consistent. | Correct the value at the HWID input parameter or the structure at the TIO_SYNC_Data parameter. |
| x0FF0000 | General internal error. | — |

## TIO_DI_ONCE: Reading in edges once at the digital input and associated time stamps (S7-1500)

### Description

TIO_DI_ONCE detects the edges at a digital input of a TIO module **once** and returns the associated time stamps. Alternatively, you can use this instruction to control a timer DI channel that is configured as an edge-triggered enable for another channel.

### Startup characteristics

During startup of the CPU, the instruction TIO_DI_ONCE applies the input parameters once and checks the following:

- Checking HWID
- Checking to see if the number of the digital input (Channel) is in the permitted range (depending on addressed module and channel configuration)
- Checking TIO_SYNC_Data.ERROR: Is an error present at TIO_SYNC?
- Checking TIO_SYNC_Data.TO_TIMES for plausibility (0 ms to 4 ms)
- Checking to see whether the OB is isochronous

If startup takes place without errors, the instruction changes to normal operation. In the event of an error, the instruction does not change to normal operation and generates an error message.

### Functional description: Time stamp detection

In normal operation, the instruction detects the edges at a digital input and the associated time stamps of the **first** valid, defined edge pair after the start of a read-in job. Use the input parameter EdgeSel to determine the edges for which time stamps are detected. To detect a new edge pair, a new positive edge is required at the REQ input parameter of the instruction.

You connect the input TIO_SYNC_Data with the output of the same name of the TIO_SYNC instruction. This ensures a shared time basis.

The figure below shows an example for the reaction of the bits DONE and BUSY at the start of a read-in job (EdgeSel = 4).

![Functional description: Time stamp detection](images/123940083595_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| R | Read-in time of the positive DI edge |
| F | Read-in time of the falling DI edge |

### Functional description: edge-triggered enable

You can use this instruction to control a timer DI channel that is configured as an edge-triggered enable for another channel.

Example:

For a TIO module TM Timer DIDQ 10x24V, the following is configured in the hardware configuration for DQ0/DI0:

- Configuration DQ/DI group = timer DQ with enable
- HW enable by DI0 = edge-triggered
- DQ0 is not inverted

In this case, use the instruction TIO_DQ for DQ0 and the instruction TIO_DI_ONCE for DI0. You can control the enable by means of the input parameters REQ and EdgeSel of TIO_DI_ONCE. As soon as TIO_DI_ONCE has recorded a time stamp according to the value of EdgeSel, the enable is considered granted. You take the enable back by resetting REQ.

The following figure shows an example with EdgeSel = 4n (first positive, then falling edge). In this case the first valid positive edge at DI0 grants the enable for DQ0 after the start of a read-in job.

![Functional description: edge-triggered enable](images/124676635787_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| 1 | Start of enable at positive edge of enable input |
| 2 | End of enable when falling edge at REQ |

If required, you can use the time stamps detected by the instruction for your application.

### Reaction to error

The Error output indicates if the instruction was processed correctly. In the event of an error, the cause of the error is displayed at the Status output.

### Parameter

The table below shows the parameters of the TIO_DI_ONCE instruction.

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| S7-1500 |  |  |  |  |
| REQ | Input | Bool | False | Starts the job at a positive edge. |
| HWID* | Input | HW_IO | 0 | Hardware identifier for TIO module from hardware configuration |
| Channel* | Input | UInt | 0 | Number (0 ... m) of the digital input of the connected TIO module |
| EdgeSel | Input | UInt | 3 | Specify the edges for which time stamps are detected:  0<sub>D</sub>: Invalid  1: Two rising edges  2: Two falling edges  3: Rising and falling edge (order depending on occurrence)  4: First rising, then falling edge  5: First falling, then rising edge  6 to 255: Invalid  If edge-triggered enable is used, the following also applies:  1: Enable at first positive DI edge  2: Enable at first falling DI edge  3: Enable at first DI edge  4: Enable at first positive DI edge  5: Enable at first falling DI edge  EdgeSel can be changed during normal operation. |
| DONE | Output | Bool | False | DONE = True: The job was completed without errors. |
| BUSY | Output | Bool | False | BUSY = True: The job has not yet been completed. |
| Error | Output | Bool | False | Error = True: An error has occurred. For detailed information see Status parameter.  Error is reset as soon as the error is corrected. |
| Status | Output | DWord | 16#0 | Status of the instruction: see description of Status parameter |
| DI | Output | Bool | False | Status of digital input.  If an inversion of the digital input is configured, this parameter is inverted as well. |
| TimeStampRE | Output | LTime | LT#0ns | Time stamp:  EdgeSel = 1: The last but one read-in time at which a positive edge was detected (if multiple positive edges have occurred).  EdgeSel = 2: The last read-in time at which a falling edge was detected (if multiple falling edges have occurred).  EdgeSel = 3; 4; 5: The last read-in time at which a falling edge was detected. |
| TimeStampFE | Output | LTime | LT#0ns | Time stamp:  EdgeSel = 1: The last read-in time at which a positive edge was detected (if multiple positive edges have occurred).  EdgeSel = 2: The last but one read-in time at which a falling edge was detected (if multiple falling edges have occurred).  EdgeSel = 3; 4; 5: The last read-in time at which a positive edge was detected. |
| LEC | Output | UInt | 0 | Counter: Number of edges for which no time stamp could be saved. The module can count a maximum of seven edges during REQ. The counter is reset with the falling edge at REQ. |
| TIO_SYNC_Data* | InOut | "TIO_SYNC_Data" |  | System time provided for the TIO instructions of the TIO modules by the TIO_SYNC instruction. See [UDT TIO_SYNC_Data](#udt-tio_sync_data-s7-1500).  Connect this input parameter with the "TIO_SYNC_Data" output parameter of the TIO_SYNC instruction. |
| Initialized | Static | Bool | False | Instruction is initialized and ready |
| * Checked once at startup of the CPU |  |  |  |  |

### Status parameter

Error codes or status information is output as double word at the Status output.

The double word is divided as follows:

| Error code | Meaning |
| --- | --- |
| (DW#16#...) |  |
| z0yywwww | Error of a system function:   - during startup (z = 1) - during normal operation (z = 0)   System functions with subordinate use are coded in yy: See table with error codes.  wwww specifies the RET_VAL of the system function. The error information is available in the help for the system function. |
| z0yy0000 | An error that does not originate in a system function. This error receives a consecutive error number yy.   The error can occur:   - during startup (z = 1) - during normal operation (z = 0) |

**Table with error codes**

| Error code | Meaning | Solution |
| --- | --- | --- |
| (DW#16#...) |  |  |
| 00000000 | No error. | — |
| 10010000 | The assigned number of the digital input at the Channel input parameter is outside the permitted range (depending on addressed module and channel configuration). | Correct the value at the Channel input parameter. |
| 10020000 | The TIO_DI_ONCE instruction is not called in an isochronous OB. The instruction can only be used without errors in an isochronous OB. | Make sure that TIO_DI_ONCE is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10030000 | An error occurred when reading the HWID input parameter. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| x0040000 | The data in TIO_SYNC_Data is invalid/incorrect. | Check the TIO_SYNC instruction and the interconnection of its TIO_SYNC_Data output. |
| 1005xxxx | An error has occurred during execution of the RD_SINFO system function. The low word xxxx displays the error information of the RET_VAL return value from RD_SINFO. | - Read the description of the RD_SINFO in the STEP 7 (TIA Portal) information system. - Make sure that TIO_DI_ONCE is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10060000 | No TIO module found.  Possible cause: The module configured using the hardware identifier is not a TIO module. | - Make sure that the configured module is a TIO module. - Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. |
| 10070000 | An internal error occurred during the address calculation. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| 00080000 | TIO module is not synchronized using the TIO_SYNC instruction.  The error code can also indicate that:  - A job was already present before the first run of the instruction. - The assigned number at the Channel input parameter is not a digital input. | Check the instruction TIO_SYNC. |
| 10090000 | The read cycle time of the isochronous OB is outside the permitted range of 0 &lt; T<sub>APP</sub> &lt;= 16 ms and is therefore invalid.  The instruction can only be used without errors in an isochronous OB. | - Correct the cycle time. - Make sure that TIO_DI_ONCE is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 100A0000 | The time T<sub>O</sub> of the TIO model stored in TIO_SYNC_Data is outside the permissible range of 0 &lt; T<sub>o</sub> &lt;= 4 ms. | Check the instruction TIO_SYNC. |
| 100Bxxxx | An error has occurred during execution of the RD_ADDR system function. The low word xxxx displays the error information of the RET_VAL return value from RD_ADDR. | Read the description of the RD_ADDR in the STEP 7 (TIA Portal) information system. |
| 000C0000 | The converted time stamp is invalid.  Possible cause: Communication error | Check the communication with the TIO module. |
| 000D0000 | The Quality Information of the digital input indicates that an error has occurred at the digital input. | Check the supply voltage L+/1L+/2L+. |
| 000E0000 | The assigned number at the Channel input parameter is not a digital input configured as Timer DI. | - Check the channel configuration (only for TM Timer DIDQ 16x24V). - Check the operating mode of the digital input. |
| 000F0000 | The assigned value at the EdgeSel input parameter is outside the valid range of 1 to 5. | Correct the value at the EdgeSel input parameter. |
| 10100000 | The send clock is outside the permitted range of 0 &lt; SendClock &lt;= 4 ms and is therefore invalid.  The error code can also indicate that   - The data in TIO_SYNC_Data is invalid or does not exist. - The TIO_DI instruction is not called in an isochronous OB. | Correct the send clock. |
| x0130000 | MC-Servo (OB91) is not isochronous to the bus cycle time. | Correct the value of the cycle time of the MC-Servo to the value of the bus cycle time.  Note:  Calling TIO instructions in an OB of the type "MC-PostServo" with reduction ratio "MC-Servo" can result in incorrect calculation of time stamps. |
| 10140000 | The configured value at the HWID input parameter is not present in the structure at the TIO_SYNC_Data parameter. The HWID and TIO_SYNC_Data parameters are not consistent. | Correct the value at the HWID input parameter or the structure at the TIO_SYNC_Data parameter. |
| x0FF0000 | General internal error. | — |

## TIO_IOLink_OUT: Output time-controlled process output signals (S7-1500)

### Description

You can use Time-based IO with the TIO_IOLink_OUT instruction. TIO_IOLink_OUT lets you activate the output data of an IO-Link Device at a specified time.

The IO-Link Device must be equipped with the time stamp function and the Port must be in "IO-Link, Time based OUT" mode.

### Startup characteristics

During startup of the CPU, the instruction TIO_IOLink_OUT applies the input parameters once and checks the following:

- Checking HWID
- Checking whether the Port number is in the range (1 to 4)
- Checking TIO_SYNC_Data.Error: Is an error present at TIO_SYNC?
- Checking T<sub>o</sub> for a positive value
- Checking the setting to type IO-Link
- Checking Port mode regarding configuration for IO-Link Time based OUT
- Checking whether the OB is a "Synchronous Cycle" OB
- Checking PortQualifier

If startup takes place without errors, the instruction changes to normal operation. The input parameters REQ, Out_Mode, TimeStamp and AA_Data can be changed during normal operation. In the event of an error, the instruction does not change to normal operation and generates an error message.

### Functional description

In normal operation, the instruction sends the process data (AA_Data) to an IO-Link Device. The output data AA_Data are activated at the time defined at the input parameter TimeStamp.

You connect the input TIO_SYNC_Data with the output of the same name of the TIO_SYNC instruction. This ensures a shared time basis.

You start an output job with a positive edge at the "REQ" parameter. You can only start a new job when there is no error pending and no job is active. When starting the output job, the AA_Data (bit 0, 1) are activated on the IO-Link Device at a time defined by TimeStamp. The job is done when the last application cycle is executed before the output time is reached (Done). Status and Error are constantly being updated during the job runtime.

> **Note**
>
> Once the job has been started with a positive edge, you can adapt the output time with the input of a new TimeStamp without having to restart the job.
>
> Constraint:
>
> If the adapted time stamp is less than 16 ms before the output time (TimeStamp - TIO_Time &lt; 16), the last valid time stamp is used.

If you specify the value 0 as TimeStamp, the output is written directly with the data specified at the input AA_Data. This gives you the option to implement a direct control from the TIO module without time stamp in manual mode. You can use the direct control to interrupt an ongoing job.

### Reaction to error

The Error output indicates if the instruction was processed correctly. The reasons for the errors are displayed at the Status output.

### Parameter

The table below shows the parameters of the TIO_IOLink_OUT instruction.

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| S7-1500 |  |  |  |  |
| REQ | Input | Bool | False | Starts the job at a positive edge. |
| HWID* | Input | HW_IO | 0 | Hardware identifier for TIO module from HWCN. |
| TO* | Input | LTime | LT#0ns | T<sub>o</sub>: Time for output of isochronous output data.  Apply T<sub>o</sub> from the ET 200 station (properties of the PROFINET interface). |
| Port* | Input | USInt | 0 | Port number (1 to 4) of the specified IO-Link Device |
| TIO_SYNC_Data* | Input | "TIO_SYNC_Data" |  | System time provided for the TIO instructions of the TIO modules by the TIO_SYNC instruction. See [UDT TIO_SYNC_Data](#udt-tio_sync_data-s7-1500).  Connect this input parameter with the "TIO_SYNC_Data" output parameter of the TIO_SYNC instruction. |
| TimeStamp | Input | LTime | LT#0ns | Time stamp: Time when the process data (AAE1, AAE2) are to be output. |
| AA_Data | Input | Word | 16#0 | Process output data: Date to be output (Word).   Includes AAE1 and AAE2 on bit 0, 1. |
| Busy | Output | Bool | False | Busy = True: The job has not yet been completed. |
| Done | Output | Bool | False | Done = True is displayed for one cycle: The job is signaled as "done, no errors". |
| Error | Output | Bool | False | Error = True: An error has occurred. In this case, BUSY and DONE are set to False. For detailed information see Status parameter.  Error is reset as soon as the error is corrected. |
| Status | Output | DWord | 16#0 | Status of the instruction: see description of Status parameter |
| * Checked once at startup of the CPU |  |  |  |  |

### Status parameter

Error codes or status information is output as double word at the Status output.

The double word is divided as follows:

| Error code | Meaning |
| --- | --- |
| (DW#16#...) |  |
| z0yywwww | Error of a system function:   - during startup (z = 1) - during normal operation (z = 0)   System functions with subordinate use are coded in yy: See table with error codes.  wwww specifies the RET_VAL of the system function. The error information is available in the help for the system function. |
| z0yy0000 | An error that does not originate in a system function. This error receives a consecutive error number yy.   The error can occur:   - during startup (z = 1) - during normal operation (z = 0) |

**Table with error codes**

| Error code | Meaning | Solution |
| --- | --- | --- |
| (DW#16#...) |  |  |
| 00000000 | No error. | — |
| 10010000 | The assigned number at the Port input parameter is outside the valid range of 1 to 4. | Correct the value at the Port input parameter. |
| 10020000 | The TIO_IOLink_OUT instruction is not called in an isochronous OB. The instruction can only be used without errors in an isochronous OB. | Make sure that TIO_IOLink_OUT is called in a "Synchronous Cycle" OB. |
| 10030000 | An error occurred when reading the HWID input parameter. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| x0040000 | The data in TIO_SYNC_Data is invalid/incorrect. | Check the TIO_SYNC instruction and the interconnection of its TIO_SYNC_Data output. |
| 1005xxxx | An error has occurred during execution of the RD_SINFO system function. The low word xxxx displays the error information of the RET_VAL return value from RD_SINFO. | - Read the description of the RD_SINFO in the TIA Portal information system. - Make sure that TIO_IOLink_OUT is called in a "Synchronous Cycle" OB. |
| 10060000 | Unable to find IO-Link Device.  Possible cause:  The module configured using the hardware identifier is not an IO‑Link Master for Time‑based IO. | - Make sure that the configured module is an IO‑Link Master for Time‑based IO. - Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. |
| 10070000 | An internal error occurred during the address calculation. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| 00080000 | TIO module is not synchronized using the TIO_SYNC instruction. | Check the instruction TIO_SYNC. |
| 10090000 | The read cycle time of the isochronous OB is outside the permitted range of 0 &lt; T<sub>APP</sub> &lt;= 16 ms and is therefore invalid.  The instruction can only be used without errors in an isochronous OB. | - Correct the cycle time. - Make sure that TIO_IOLink_OUT is called in a "Synchronous Cycle" OB. |
| 100A0000 | The assigned time at the TO input parameter is outside the permitted range of 0 &lt; T<sub>o</sub> &lt;= 4 ms. | Correct the value at the TO input parameter. |
| 100Bxxxx | An error has occurred during execution of the RD_ADDR system function. The low word xxxx displays the error information of the RET_VAL return value from RD_ADDR. | Read the description of the RD_ADDR in the TIA Portal information system. |
| 000C0000 | The time stamp at the TimeStamp input parameter is invalid. | Check the TimeStamp input parameter. |
| 000D0000 | The value status PortQualifier of the IO-Link indicates that the process data is invalid. | Check the connected sensor and its configuration. |
| 100E0000 | The configured port mode of the IO-Link is incorrect. | Check the configuration of the connected sensor with S7‑PCT. |
| 100F0000 | The read cycle time of the OB of type "Synchronous Cycle" is too long: T<sub>APP</sub> &gt; 16 ms. | Configure a smaller multiple of the send clock as the cycle time. |
| x0FF0000 | General internal error. | — |

## TIO_DQ: Output edges time-controlled at the digital output (S7-1500)

### Description

TIO_DQ enables a digital output of a TIO module to be switched at specified times.

### Startup characteristics

During startup of the CPU, the instruction TIO_DQ applies the input parameters once and checks the following:

- Checking HWID
- Checking to see if the number of the digital input (Channel) is in the permitted range (depending on addressed module and channel configuration)
- Checking TIO_SYNC_Data.Error: Is an error present at TIO_SYNC?
- Checking TIO_SYNC_Data.TO_TIMES for plausibility (0 ms to 4 ms)
- Checking to see whether the OB is isochronous

If startup takes place without errors, the instruction changes to normal operation. The input parameters REQ, Out_Mode, TimeStampRE and TimeStampFE can be changed during normal operation. In the event of an error, the instruction does not change to normal operation and generates an error message.

### Functional description

The instruction outputs edges time-controlled at a digital output during normal operation.

- At the time defined at the TimeStampRE input parameter, a positive edge is output at the digital output.
- At the time defined at the TimeStampFE input parameter, a falling edge is output at the digital output.

Depending on the program execution model, a time stamp must exceed the following value:

| Program execution model | TimeStampRE&gt; ...  TimeStampFE &gt; ... |
| --- | --- |
| IPO model | TIO_Time + T<sub>APP</sub> + T<sub>O</sub> |
| OIP model | TIO_Time + T<sub>APP</sub> + SendClock + T<sub>O</sub> |

Use the input parameter Out_Mode to determine if only one edge or both edges are output.

You connect the input TIO_SYNC_Data with the output of the same name of the TIO_SYNC instruction. This ensures a shared time basis.

You start an output job with a positive edge at the REQ parameter. You can only start a new job when there is no error pending and no job is active. When the output job is started, the digital output is switched at the times defined with TimeStampRE and TimeStampFE.

- If the digital output is already set at time TimeStampRE, the output job is not transferred to the module for the positive edge.
- If the digital output is not set at time TimeStampFE, the output job is not transferred to the module for the negative edge.

This means the digital output is not switched in both cases.

The job is done when the last application cycle is executed before the second output time is reached (DONE). Status and Error are constantly being updated during the job runtime. You can cancel an active output job by changing TimeStampRE or TimeStampFE to an invalid time stamp, e.g. LT#5μs.

The figure below shows an example for the reaction of the bits DONE and BUSY at the start of an output job under the following conditions:

- Out_Mode = 2 (both edges are output)
- The two time stamps are not changed between the start of the job and the output.

![Functional description](images/126423234571_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| T<sub>APP</sub> | Application cycle |
| R1, R2 | Specified times of a positive DQ edge |
| F1, F2 | Specified times of a falling DQ edge |

> **Note**
>
> Once the job has been started with a positive edge at REQ, you can change the output times with a new input of TimeStampRE and TimeStampFE without having to restart the job.
>
> Constraint:
>
> If a changed time stamp is less than two application cycles before the output time (TimeStampRE - TIO_Time &lt; 2*T<sub>APP</sub> or TimeStampFE - TIO_Time &lt; 2*T<sub>APP</sub>), it is not taken into consideration. In this case, the last valid time stamp is used because it was already transferred to the TIO module.

> **Note**
>
> If you specify the same value for TimeStampRE and TimeStampFE, the instruction ignores the job and does not output an edge.

If you specify the value 0 for TimeStampRE or TimeStampFE, you can output the respective edge directly at the digital output with the input parameter Out_Mode = 3. This gives you the option to implement a direct control from the TIO module without time stamp in manual mode. You can use the direct control to interrupt an ongoing job.

### Reaction to error

The Error output indicates if the instruction was processed correctly. In the event of an error, the cause of the error is displayed at the Status output.

### Parameter

The table below shows the parameters of the TIO_DQ instruction.

| Parameter | Declaration in library version |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| &lt; V2.0 | ≥ V2.0 | S7-1500 |  |  |  |
| REQ | Input |  | Bool | False | Starts the job at a positive edge. |
| HWID* | Input |  | HW_IO | 0 | Hardware identifier for TIO module from hardware configuration |
| Channel* | Input |  | UInt | 0 | Number (0 ... m) of the digital output of the connected TIO module |
| Out_Mode | Input |  | UInt | 2 | Specify the output mode for the edges at the digital output:  0: Only rising edge is output (TimeStampRE).  1: Only falling edge is output (TimeStampFE).  2: Both edges are output (TimeStampRE and TimeStampFE).  3: Each edge is output directly if TimeStampRE = 0 or TimeStampFE = 0 If both time stamps have the value "0" or if no time stamp has the value "0", no edge is output.  4 to 255: Invalid |
| TimeStampRE | Input |  | LTime | LT#0ns | Time stamp: Time when a positive edge is to be output. |
| TimeStampFE | Input |  | LTime | LT#0ns | Time stamp: Time when a falling edge is to be output. |
| StatusDQ | Output |  | Bool | False | Actual status of the digital output.   If an inversion of the digital output is configured, StatusDQ is inverted as well.  StatusDQ shows the internal state of the digital output independent of the effect of any configured HW enable. |
| DONE | Output |  | Bool | False | DONE = True is displayed for one cycle: The job was completed without errors. |
| BUSY | Output |  | Bool | False | BUSY = True: The job has not yet been completed. |
| Error | Output |  | Bool | False | Error = True: An error has occurred. In this case, BUSY and DONE are set to False. For detailed information see Status parameter.  Error is reset as soon as the error is corrected. |
| Status | Output |  | DWord | 16#0 | Status of the instruction: see description of Status parameter |
| TIO_SYNC_Data* | Input | InOut | "TIO_ SYNC_ Data" |  | System time provided for the TIO instructions of the TIO modules by the TIO_SYNC instruction. See [UDT TIO_SYNC_Data](#udt-tio_sync_data-s7-1500).  Connect this parameter with the TIO_SYNC_Data output parameter of the TIO_SYNC instruction. |
| * Checked once at startup of the CPU |  |  |  |  |  |

### Status parameter

Error codes or status information is output as double word at the Status output.

The double word is divided as follows:

| Error code | Meaning |
| --- | --- |
| (DW#16#...) |  |
| z0yywwww | Error of a system function:   - during startup (z = 1) - during normal operation (z = 0)   System functions with subordinate use are coded in yy: See table with error codes.  wwww specifies the RET_VAL of the system function. The error information is available in the help for the system function. |
| z0yy0000 | An error that does not originate in a system function. This error receives a consecutive error number yy.   The error can occur:   - during startup (z = 1) - during normal operation (z = 0) |

**Table with error codes**

| Error code | Meaning | Solution |
| --- | --- | --- |
| (DW#16#...) |  |  |
| 00000000 | No error. | — |
| 10010000 | The assigned number of the digital output at the Channel input parameter is outside the permitted range (depending on addressed module and channel configuration). | Correct the value at the Channel input parameter. |
| 10020000 | The TIO_DQ instruction is not called in an isochronous OB. The instruction can only be used without errors in an isochronous OB. | Make sure that TIO_DQ is called in an OB of the type "Synchronous Cycle" or "MC-PostServo". |
| 10030000 | An error occurred when reading the HWID input parameter. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| x0040000 | The data in TIO_SYNC_Data is invalid/incorrect. | Check the TIO_SYNC instruction and the interconnection of its TIO_SYNC_Data output. |
| 1005xxxx | An error has occurred during execution of the RD_SINFO system function. The low word xxxx displays the error information of the RET_VAL return value from RD_SINFO. | - Read the description of the RD_SINFO in the STEP 7 (TIA Portal) information system. - Make sure that TIO_DQ is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 10060000 | No TIO module found.  Possible cause: The module configured using the hardware identifier is not a TIO module. | - Make sure that the configured module is a TIO module. - Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. |
| 10070000 | An internal error occurred during the address calculation. | Check the value at the HWID input parameter. Specify the hardware identifier of the TIO module from its module properties in the hardware configuration. An internal system constant of data type Hw_SubModule is available for the symbolic addressing. |
| x0080000 | TIO module is not synchronized using the TIO_SYNC instruction.  The error code can also indicate that:   - A job was already present before the first run of the instruction. - The assigned number at the Channel input parameter is not a digital output. | Check the instruction TIO_SYNC. |
| 10090000 | The read cycle time of the isochronous OB is LT#0ms or has as negative value and is therefore invalid. Correct the value.   The instruction can only be used without errors in an isochronous OB. | - Correct the cycle time. - Make sure that TIO_DQ is called in a "Synchronous Cycle" or "MC-PostServo" OB. |
| 100A0000 | The time T<sub>O</sub> of the TIO model stored in TIO_SYNC_Data is outside the permissible range of 0 &lt; T<sub>o</sub> &lt;= 4 ms. | Check the instruction TIO_SYNC. |
| 100Bxxxx | An error has occurred during execution of the RD_ADDR system function. The low word xxxx displays the error information of the RET_VAL return value from RD_ADDR. | Read the description of the RD_ADDR in the STEP 7 (TIA Portal) information system. |
| 000C0000 | One or both time stamps at the TimeStampRE and TimeStampFE input parameters are invalid. The error is only signaled for the duration of one application cycle. | Check the TimeStampRE and TimeStampFE input parameters. |
| 000D0000 | The Quality Information of the digital output indicates that an error has occurred at the digital output. | - Check the parameter assignment of the digital output. - Check the supply voltage L+/1L+/2L+. - Check the wiring of the digital output for short-circuit, overload, and overtemperature. |
| 000E0000 | The number configured at the Channel input parameter is not a digital output configured as Timer DQ. | - Check the channel configuration (only for TM Timer DIDQ 16x24V). - Check the operating mode of the digital output. |
| 100F0000 | The read cycle time of the OB of type "Synchronous Cycle" is too long: T<sub>APP</sub> &gt; 16 ms. | Configure a smaller multiple of the send clock as the cycle time. |
| 10100000 | The send clock is outside the permitted range of 0 &lt; SEND_CLOCK &lt;= 4 ms and is therefore invalid.  The error code can also indicate that   - The data in TIO_SYNC_Data is invalid or does not exist. - The TIO_DQ instruction is not called in an isochronous OB. | Correct the send clock. |
| 00110000 | The assigned value at the Out_Mode input parameter is outside the valid range of 0 to 3. | Correct the value at the Out_Mode input parameter. |
| x0130000 | MC-Servo (OB91) is not isochronous to the bus cycle time. | Correct the value of the cycle time of the MC-Servo to the value of the bus cycle time.  Note:  Calling TIO instructions in an OB of the type "MC-PostServo" with reduction ratio "MC-Servo" can result in incorrect calculation of time stamps. |
| 10140000 | The configured value at the HWID input parameter is not present in the structure at the TIO_SYNC_Data parameter. The HWID and TIO_SYNC_Data parameters are not consistent. | Correct the value at the HWID input parameter or the structure at the TIO_SYNC_Data parameter. |
| x0FF0000 | General internal error. | — |

## UDT TIO_SYNC_Data (S7-1500)

### Description

The data type UDT TIO_SYNC_Data contains the central structure and data for synchronization of the modules and passing of the TIO_Time.

### Parameter

| Parameter | Data type | Description |
| --- | --- | --- |
| S7-1500 |  |  |
| TIO_TIME | LTime | Shared time basis (relative time) of the TIO modules |
| PIP_MODE | USInt | Mode for data update (is forwarded by the PIP_Mode input parameter of the TIO_SYNC instruction) |
| APP_CYC | LTime | Application cycle of the "MC-PostServo" or "Synchronous Cycle", "MC-PreServo" OB |
| SEND_CLOCK | LTime | Send clock of sync domain (is forwarded by the SendClock parameter of the TIO_SYNC instruction) |
| SYNC_MODULES | HW_IO array [1...8] | Hardware identifiers of the TIO modules from hardware configuration |
| TO_TIMES | UDInt-Array [1...8] | T<sub>O</sub> for each TIO module: |
| TIO_TIME_BASE | LTime | Internal use |
| TBASE | LTime |  |
| ERROR | Bool |  |
