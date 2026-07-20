---
title: "Extended instructions (S7-300, S7-400)"
package: ProgExtInstr34enUS
topics: 249
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Extended instructions (S7-300, S7-400)

This section contains information on the following topics:

- [Date and time (S7-300, S7-400)](#date-and-time-s7-300-s7-400)
- [String + Char (S7-300, S7-400)](#string-char-s7-300-s7-400)
- [Process image (S7-300, S7-400)](#process-image-s7-300-s7-400)
- [Distributed I/O (S7-300, S7-400)](#distributed-io-s7-300-s7-400)
- [PROFIenergy (S7-300, S7-400)](#profienergy-s7-300-s7-400)
- [Module parameter assignment (S7-300, S7-400)](#module-parameter-assignment-s7-300-s7-400)
- [Interrupts (S7-300, S7-400)](#interrupts-s7-300-s7-400)
- [Alarms (S7-300, S7-400)](#alarms-s7-300-s7-400)
- [Diagnostics (S7-300, S7-400)](#diagnostics-s7-300-s7-400)
- [Data block functions (S7-300, S7-400)](#data-block-functions-s7-300-s7-400)
- [Table functions (S7-300, S7-400)](#table-functions-s7-300-s7-400)
- [Addressing (S7-300, S7-400)](#addressing-s7-300-s7-400)
- [Additional functions (S7-300)](#additional-functions-s7-300)

## Date and time (S7-300, S7-400)

This section contains information on the following topics:

- [T_COMP: Compare time tags (S7-300, S7-400)](#t_comp-compare-time-tags-s7-300-s7-400)
- [T_CONV: Convert times and extract (S7-300, S7-400)](#t_conv-convert-times-and-extract-s7-300-s7-400)
- [T_ADD: Add times (S7-300, S7-400)](#t_add-add-times-s7-300-s7-400)
- [T_SUB: Subtract times (S7-300, S7-400)](#t_sub-subtract-times-s7-300-s7-400)
- [T_DIFF: Time difference (S7-300, S7-400)](#t_diff-time-difference-s7-300-s7-400)
- [T_COMBINE: Combine times (S7-300, S7-400)](#t_combine-combine-times-s7-300-s7-400)
- [Time-of-day functions (S7-300, S7-400)](#time-of-day-functions-s7-300-s7-400)
- [Additional standard libraries (S7-300, S7-400)](#additional-standard-libraries-s7-300-s7-400)

### T_COMP: Compare time tags (S7-300, S7-400)

#### Description

You use the instruction to compare the contents of two tags with the data type DT, and output the result of the comparison as return value at parameter OUT. The parameter OUT is set to "1", when the applied comparison condition is satisfied.

The following comparison options can be used:

| Symbol | Description |
| --- | --- |
| EQ | The return value has the signal state “1" if the time is the same at the parameter IN1 and IN2. |
| NE | The return value has the signal state “1" if the time at parameters IN1 and IN2 is not identical. |
| GE | The return value has the signal state "1" if the time at parameter IN1 is greater (more recent) than or equal to the time at parameter IN2 . |
| LE | The return value has the signal state "1" if the time at parameter IN1 is less (less recent) than or equal to the time at parameter IN2. |
| GT | The return value has the signal state “1" if the time at parameter IN1 is greater (more recent) than the time at parameter IN2. |
| LT | The return value has the signal state "1" if the time at parameter IN1 is less (less recent) than the time at parameter IN2 . |

#### Parameter

The following table shows the parameters of the "T_COMP" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | DT | D, L | Value to be compared |
| IN2 | Input | DT | D, L | Value to be compared |
| OUT | Output | BOOL | I, Q, M, D, L | Return value |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### T_CONV: Convert times and extract (S7-300, S7-400)

#### Description

The "T_CONV" instruction is used to convert a DT (DATE_AND_TIME), S5TIME and TIME data types to a DATE, INT, TOD (TIME_OF_DAY), TIME or S5TIME data type.

#### Parameter

You decide the type of conversion by selecting the data types in the instruction boxes of the input and output of the instruction. You can query the result of the conversion at the OUT parameter.

The following table shows the parameters of the "T_CONV" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | DT, S5TIME, TIME | I, Q, M, D, L | Value to be converted. The data format of the tag for parameter IN must match the data type selected using the instruction box. |
| OUT | Return | DATE, INT, TOD, TIME, S5TIME | I, Q, M, D, L | Result of the conversion. The data format of the tag for parameter OUT must match the data type selected using the instruction box. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Examples

Converting data format TIME to data format S5TIME

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Output | TIME | Input variable in the TIME data format. |
| OUT | Input | S5TIME | The function converts the TIME data format to the S5TIME format. The value is rounded down during conversion. If the input parameter is greater than the S5TIME format permits (greater than TIME#02:46:30.000), the result S5TIME#999.3 will be output and the binary result (BR) is set to "0". |

Extraction of the weekday from the DATE_AND_TIME format

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Output | DT | Input variable in the DATE_AND_TIME data format. |
| OUT | Input | INT | The function extracts the weekday from the DATE_AND_TIME (DT) format. The weekday is output in INTEGER format.  1: Sunday  2: Monday  3: Tuesday  4: Wednesday  5: Thursday  6: Friday  7: Saturday |

### T_ADD: Add times (S7-300, S7-400)

#### Description

You use the instruction "T_ADD" to add a duration (format TIME) to a new time (format DT) and output the result as a new time (format DT).

The time DT for the parameter IN1 must be in the range between DT#1990-01-01-00:00:00.000 and DT#2089-12-31-23:59:59.999. The instruction does not run an input check. If the result of the addition is not within the valid range, the result is limited to the corresponding value and the binary result (BR) bit of the status word is set to “0".

#### Parameters

The following table shows the parameters of the "T_ADD" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | DT | D, L | Time in the DT (DATE_AND_TIME) format. |
| IN2 | Input | TIME | I, Q, M, D, L or constant | Duration to be added in the TIME format. |
| OUT | Return | DT | D, L | Result of the addition in the DT (DATE_AND_TIME) format. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### T_SUB: Subtract times (S7-300, S7-400)

#### Description

You use the instruction "T_SUB" to subtract a duration (format TIME) from a time (format DT)and output the result as a new time (format DT).

The time DT for the parameter IN1 must be in the range between DT#1990-01-01-00:00:00.000 and DT#2089-12-31-23:59:59.999. The instruction does not run an input check. If the result of the subtraction is not within the valid range, the result is limited to the corresponding value and the binary result (BR) bit of the status word is set to “0".

#### Parameters

The following table shows the parameters of the "T_SUB" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | DT | D, L | Time in the DT (DATE_AND_TIME) format. |
| IN2 | Input | TIME | I, Q, M, D, L or constant | Duration to be subtracted in the TIME format. |
| OUT | Return | DT | D, L | Result of the subtraction in the DT (DATE_AND_TIME) format. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### T_DIFF: Time difference (S7-300, S7-400)

#### Description

You use the instruction "T_DIFF" to determine the difference between two times by subtracting two times of the DT format. The time at the IN2 input is subtracted form the time at the IN1 input. The result of the subtraction is output at the OUT output in the TIME format.

- If the first time at the IN1 input is greater (younger) than the second time at the IN2 input, the result at the OUT output is positive.
- If the first time at the IN1 input is less (older) than the second time at the IN2 input, the result at the OUT output is negative.

If the result of the subtraction is outside the TIME range, the result is limited to the corresponding value and the binary result (BR) is set to "0".

#### Parameter

The following table shows the parameters of the "T_DIFF" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | DT | D, L | Minuend |
| IN2 | Input | DT | D, L | Subtrahend |
| OUT | Return | TIME | I, Q, M, D, L | Difference in the TIME format. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### T_COMBINE: Combine times (S7-300, S7-400)

#### Description

The "T_COMBINE" instruction combines the DATE and TIME_OF_DAY (TOD) data formats and converts these formats into the DATE_AND_TIME (DT) data format. The instruction does not report any errors.

- The DATE input value must be between DATE#1990-01-01 and DATE#2089-12-31 (will not be checked).
- At the IN2 input value, the TIME_OF_DAY data type is used.
- At the OUT output value, the DATE_AND_TIME data type is output.

#### Parameter

The following table shows the parameters of the "T_COMBINE" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | DATE | D, L or constant | Input tag in the DATE format. |
| IN2 | Input | TOD | D, L or constant | Input tag in the TOD format. |
| OUT | Return | DT | D, L | Return value in the DT format. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Time-of-day functions (S7-300, S7-400)

This section contains information on the following topics:

- [WR_SYS_T: Set time-of-day (S7-300, S7-400)](#wr_sys_t-set-time-of-day-s7-300-s7-400)
- [RD_SYS_T: Read time-of-day (S7-300, S7-400)](#rd_sys_t-read-time-of-day-s7-300-s7-400)
- [TIME_TCK: Read system time (S7-300, S7-400)](#time_tck-read-system-time-s7-300-s7-400)
- [SET_CLKS: Set time-of-day and time-of-day status (S7-400)](#set_clks-set-time-of-day-and-time-of-day-status-s7-400)
- [SNC_RTCB: Synchronize slave clocks (S7-300, S7-400)](#snc_rtcb-synchronize-slave-clocks-s7-300-s7-400)

#### WR_SYS_T: Set time-of-day (S7-300, S7-400)

##### Description

You set the time and the date of the CPU clock with the "WR_SYS_T" instruction. The clock then runs starting from the set time and date. You specify the date and time in the DT data format at the IN input of the instruction. You can use the "[T_COMBINE](#t_combine-combine-times-s7-300-s7-400)" instruction to convert the DATE and TOD formats to the required DT data format.

If the clock is a master clock, the CPU also starts the time-of-day synchronization when the instruction is called. You set the synchronization intervals per configuration. The "WR_SYS_T" instruction cannot be used to pass information about the local time zone or daylight saving time.

At the RET_VAL output, you can query whether errors have occurred during execution of the instruction.

##### Parameter

The following table shows the parameters of the "WR_SYS_T" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | DT | D, L | Date and time |
| RET_VAL | Return | INT | I, Q, M, D, L | Status of the instruction |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| 8080 | Error in date |
| 8081 | Year invalid |
| 8082 | Month invalid |
| 8083 | Day invalid |
| 8084 | Hour information invalid |
| 8085 | Minute information invalid |
| 8086 | Second information invalid |
| 8087 | Nanosecond information invalid |
| 80B0 | The real-time clock has failed |

##### Example

You enter the date and time as DT data type. As an example: for January 15, 2010, 10:30 a.m. and 30 seconds you would enter: DT#2010-01-15-10:30:30 The time-of-day can only be input down to seconds. The day of the week is calculated by "WR_SYS_T" based on the date.

---

**See also**

[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

#### RD_SYS_T: Read time-of-day (S7-300, S7-400)

##### Description

You use the "RD_SYS_T" instruction to read the current date and current time-of-day of the CPU clock. The read data is provided in DT format at the OUT output of the instruction. The provided value does not include information about the local time zone or daylight saving time. At the RET_VAL output, you can query whether errors have occurred during execution of the instruction.

##### Parameter

The following table shows the parameters of the instruction "RD_SYS_T":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| OUT | Output | DT | D,L | Date and time of CPU |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| 8222 | The result is outside the permitted range of values. |
| 8223 | The result cannot be saved in the specified data type. |

---

**See also**

[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

#### TIME_TCK: Read system time (S7-300, S7-400)

##### Description

With the "TIME_TCK" instruction, you read the system time of the CPU. The system time is a time counter that counts from 0 to a maximum of 2147483647 ms. In case of an overflow, the system time is counted again starting with "0". The time scale and the accuracy of the system time is 1 ms. The system time is only influenced by the operating modes of the CPU. You can use the system time, for example, to measure the duration of processes by comparing the results of two "TIME_TCK" calls. The instruction does not provide any error information.

The following table provides an overview of how the system time changes depending on the operating modes of the CPU.

| Mode | System time ... |
| --- | --- |
| Startup | ... is constantly updated. |
| RUN | ... is constantly updated. |
| STOP | ... is stopped and retains the current value. |
| Restart (not with the S7-300) | ... continues with the value saved at the change to STOP mode |
| Warm restart | ... is deleted and restarts with "0". |
| Cold restart | ... is deleted and restarts with "0". |

##### Parameter

The following table shows the parameters of the instruction "TIME_TCK":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Return | TIME | I, Q, M, D, L | The RET_VAL parameter contains  the read system time in the range  from 0 to 2<sup>31</sup> -1 ms. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### SET_CLKS: Set time-of-day and time-of-day status (S7-400)

##### Description

You use the "SET_CLKS" instruction to set the time-of-day of your CPU and the time-of-day status.

> **Note**
>
> Use "SET_CLKS" only if the time-of-day for your CPU is not going to be synchronized. Otherwise, with every synchronization the master clock time-of-day status would be applied. This step would overwrite the value specified with "SET_CLKS".

> **Note**
>
> You can determine the current time-of-day status of your CPU by reading [SZL-ID W#16#0132 Index W#16#0008](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w160008-s7-300-s7-400) using the "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" instruction.

##### Parameters

The following table shows the parameters of the "SET_CLKS" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Operating mode:  - B#16#01: Set time-of-day - B#16#02: Set time-of-day status - B#16#03: Set time-of-day and time-of-day status |
| PDT | Input | DT | D, L | Specified time-of-day |
| CORR | Input | INT | I, Q, M, D, L or constant | Correction value (in 0.5 h pattern)  Possible values: –24 to +26 |
| SUMMER | Input | BOOL | I, Q, M, D, L | Daylight saving time/standard time ID:  - 0 = Standard time - 1 = Daylight saving time |
| ANN_1 | Input | BOOL | I, Q, M, D, L | Announcement hour  1: At the next hourly change daylight saving time is switched over to standard time or vice versa. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error code |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter MODE

Use the MODE parameter to specify whether to change only the time-of-day, only the time-of-day status, or both. This is explained in the table below:

| MODE | Meaning |
| --- | --- |
| B#16#01 | Set time-of-day  The call corresponds to the call of the "SET_CLK" instruction.  The input parameters CORR, SUMMER and ANN_1 are not evaluated. |
| B#16#02 | Set time-of-day status  The input parameter PDT is not evaluated. The remaining input parameters form the following time-of-day status elements:  - Correction value including the sign - Announcement hour - Daylight saving time/standard time indicator   The time-of-day resolution is matched to that of your CPU. The bit for synchronization failure of the time-of-day status is written with FALSE.  The time-of-day remains unchanged. |
| B#16#03 | Set time-of-day and time-of-day status |

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8080 | MODE outside the permitted value range |
| 8081 | CORR outside the permitted value range   (only for MODE = B#16#02 or for MODE = B#16#03) |
| 8082 | PDT outside the permitted value range Illegal date and/or time-of-day |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### SNC_RTCB: Synchronize slave clocks (S7-300, S7-400)

##### Definition: Synchronization of slave clocks

Synchronize slave clocks refers to the transmission of the date and time from the master clock of a bus segment (for example, the S7-400 communication bus, MPI, or S7 backplane bus) to all clock slaves of the bus segment.

##### Description

To ensure that the time-of-day is consistent in all modules on the network, the time-of-day slaves are updated by the system program at regular assignable intervals.

A synchronization can be performed independently from the configured synchronization interval by calling the "SNC_RTCB" instruction. This involves transmitting the date and time from the master clock to the slave clock for all time slaves on an existing bus segment.

Successful synchronization is only possible if "SNC_RTCB" is called on a CPU whose real-time clock was assigned the master clock function for at least one bus segment.

##### Parameter

The following table shows the parameters of the instruction "SNC_RTCB":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred during synchronization. |
| 0001 | The existing clock was not assigned the master clock function for  any of the bus segments. |
| 8xyy | General error information   See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### Additional standard libraries (S7-300, S7-400)

This section contains information on the following topics:

- [Handling of the runtime meter (S7-300, S7-400)](#handling-of-the-runtime-meter-s7-300-s7-400)
- [Local time (S7-300, S7-400)](#local-time-s7-300-s7-400)

#### Handling of the runtime meter (S7-300, S7-400)

This section contains information on the following topics:

- [Runtime meters (S7-300, S7-400)](#runtime-meters-s7-300-s7-400)
- [RTM: Runtime meters (S7-300, S7-400)](#rtm-runtime-meters-s7-300-s7-400)
- [SET_RTM: Set runtime meters (S7-300, S7-400)](#set_rtm-set-runtime-meters-s7-300-s7-400)
- [CTRL_RTM: Start and stop runtime meters (S7-300, S7-400)](#ctrl_rtm-start-and-stop-runtime-meters-s7-300-s7-400)
- [READ_RTM: Read runtime meters (S7-300, S7-400)](#read_rtm-read-runtime-meters-s7-300-s7-400)

##### Runtime meters (S7-300, S7-400)

###### Introduction

The CPUs have a specific quantity of runtime meters (refer to the technical specifications of your CPUs).

- If your CPU is equipped with 16-bit runtime meters, you can set, start, stop, and read them with the "[SET_RTM](#set_rtm-set-runtime-meters-s7-300-s7-400)", "[CTRL_RTM](#ctrl_rtm-start-and-stop-runtime-meters-s7-300-s7-400)" and "[READ_RTM](#read_rtm-read-runtime-meters-s7-300-s7-400)" instructions.
- If your CPU is equipped with 32-bit runtime meters, you can set, start, stop or read them with the "[RTM](#rtm-runtime-meters-s7-300-s7-400)" instruction.

  > **Note**
  >
  > You can also use the "[SET_RTM](#set_rtm-set-runtime-meters-s7-300-s7-400)", "[CTRL_RTM](#ctrl_rtm-start-and-stop-runtime-meters-s7-300-s7-400)" and "[READ_RTM](#read_rtm-read-runtime-meters-s7-300-s7-400)" instructions for the 32-bit runtime meters. In this case, however, the runtime meters operate in the same way as 16-bit runtime meters (range of values: 0 to 32767 hours).
  >
  > See also: [Data record of the partial list extract with SZL-ID W#16#0132 index W#16#000B](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w16000b-s7-300-s7-400).

###### Application

You can use a runtime meter for a variety of applications:

- For measuring the runtime of the CPU
- For measuring the runtime of controlled equipment or connected devices.

###### Characteristics of the runtime meter

When it is started, the runtime meter begins to count starting at the last recorded value. If you want it to start at a different initial value, you must explicitly specify this value ("[SET_RTM](#set_rtm-set-runtime-meters-s7-300-s7-400)" or "[RTM](#rtm-runtime-meters-s7-300-s7-400)" with MODE=4). If the CPU changes to STOP mode, or you stop the runtime meter, the CPU records the current value of the runtime meter. When a warm restart or a cold restart of the CPU is executed, the runtime meter must be restarted ("[CTRL_RTM](#ctrl_rtm-start-and-stop-runtime-meters-s7-300-s7-400)" or "[RTM](#rtm-runtime-meters-s7-300-s7-400)" with MODE=1).

The runtime meters are reset to "0" following an update of the operating system or following a CPU reset to the factory state.

###### Range of values

- CPU with 16-bit runtime meters: 0 to 32 767 hours
- CPU with 32-bit runtime meters: 0 to (2E31) -1 hours = 2,147,483,647 hours

##### RTM: Runtime meters (S7-300, S7-400)

###### Description

With the "RTM" instruction, you can set, start, stop, and read a 32-bit operating hours counter of your CPU.

If you want to read all 32-bit operating hours counters of your CPU, use the "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" instruction with the SZL_ID=W#16#0132 parameter and:

- INDEX=W#16#000B (for the operating hours counters 0 to 7) or
- INDEX=W#16#000C (for the operating hours counters 8 to 15).

See also: [Data record of the partial list extract with SZL-ID W#16#0132 index W#16#000B](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w16000b-s7-300-s7-400)

###### Parameter

The following table shows the parameters of the "RTM" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| NR | Input | BYTE | I, Q, M, D, L or constant | Number of the operating hours counter  Numbering starts with 0.  For information on the number of operating hours counters of your CPU, refer to the technical data. |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Job ID:  - 0: Read out (the status is then written to CQ and the current value to CV). After the operating hours counter has reached (2^31) - 1 hours, it stops at the highest value that can be displayed and outputs an "Overflow" error message. - 1: start (at the last counter value) - 2: stop - 4: set (to the value specified in PV) - 5: set (to the value specified in PV) and then start - 6: set (to the value specified in PV) and then stop |
| PV | Input | DINT | I, Q, M, D, L or constant | New value for the operating hours counter |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| CQ | Output | BOOL | I, Q, M, D, L | Status of the operating hours counter (1: running) |
| CV | Output | DINT | I, Q, M, D, L | Current value of the operating hours counter |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Compatibility to programs developed for a CPU with 16-bit operating hours counters

You can also use the 32-bit operating hours counters with the "[SET_RTM](#set_rtm-set-runtime-meters-s7-300-s7-400)", "[CTRL_RTM](#ctrl_rtm-start-and-stop-runtime-meters-s7-300-s7-400)" and "[READ_RTM](#read_rtm-read-runtime-meters-s7-300-s7-400)" instructions. In this case, however, the 32-bit operating hours counters operate in the same way as 16-bit meters (range of values: 0 to 32767 hours).

The partial list extract with SZL-ID W#16#0132 and the index W#16#0008 displays the 32-bit operating hours counters 0 to 7 in 16-bit mode. This means you can continue to use programs developed for a CPU with 16-bit operating hours counters that use the partial list extract with SZL-ID W#16#0132 and the index W#16#0008 .

###### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8080 | Wrong number for the operating hours counter |
| 8081 | A negative value was passed to the PV parameter. |
| 8082 | Overflow of the operating hours counter |
| 8091 | The MODE input parameter contains an invalid value. |
| 8xyy | General error information  See also:[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### SET_RTM: Set runtime meters (S7-300, S7-400)

###### Description

You use the instruction to set a CPU runtime meter to a specified value. The number of runtime meters you can set depends on the particular CPU you are using.

###### Parameters

The following table shows the parameters of the instruction "SET_RTM":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| NR | Input | BYTE | I, Q, M, D, L or constant | Input NR contains the number of the  runtime meter you want to set.  The numbering starts with "0".  For information on the number of runtime meters of your CPU, refer to the technical data. |
| PV | Input | INT | I, Q, M, D, L or constant | Input PV contains the setting for the  runtime meter. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8080 | Wrong number for the runtime meter |
| 8081 | A negative value was transferred to the PV parameter. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### CTRL_RTM: Start and stop runtime meters (S7-300, S7-400)

###### Description

You use the instruction to start or stop a runtime meter.

###### Parameters

The following table shows the parameters of the "CTRL_RTM" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| NR | Input | BYTE | I, Q, M, D, L or constant | Input NR contains the number of the  runtime meter you want to start or stop.  The numbering starts with "0".  For information on the number of runtime meters of your CPU, refer to the technical data. |
| S | Input | BOOL | I, Q, M, D, L | Input S starts or stops the runtime meter.   - Set the signal state to "0" when you want to stop the runtime meter. - Set the signal state to "1" when you want to start the runtime meter. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8080 | Wrong number for the runtime meter |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### READ_RTM: Read runtime meters (S7-300, S7-400)

###### Description

You use the instruction to read a runtime meter. The instruction provides the current number of operating hours as output data and the status of the counter, that is, "stopped" or "counting".

If the runtime meter runs for longer than 32767 hours, it stops at the count 32767 and outputs the "Overflow" error message.

###### Parameter

The following table shows the parameters of the "READ_RTM" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| NR | Input | BYTE | I, Q, M, D, L, P or constant | Input NR contains the number of the  runtime meter you want to start or stop.  The numbering starts with "0".  For information on the number of runtime meters of your CPU, refer to the technical data. |
| RET_VAL | Return | INT | I, Q, M, D, L, P | If an error occurs while the instruction is being executed, the return value contains an error code. |
| CQ | Output | BOOL | I, Q, M, D, L | Output CQ indicates whether the runtime  meter is running or stopped. The signal  state "0" shows that the runtime meter is  stopped. Signal state "1" shows that the  runtime meter is running. |
| CV | Output | INT | I, Q, M, D, L, P | Output CV indicates the current value of  the runtime meter. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8080 | Wrong number for the runtime meter |
| 8081 | Overflow of the runtime meter |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### Local time (S7-300, S7-400)

This section contains information on the following topics:

- [LOC_TIME: Calculate local time (S7-300, S7-400)](#loc_time-calculate-local-time-s7-300-s7-400)
- [BT_LT: Calculate local time from base time (S7-300, S7-400)](#bt_lt-calculate-local-time-from-base-time-s7-300-s7-400)
- [LT_BT: Calculate base time from local time (S7-300, S7-400)](#lt_bt-calculate-base-time-from-local-time-s7-300-s7-400)
- [S_LTINT: Set time-of-day interrupt using local time (S7-300, S7-400)](#s_ltint-set-time-of-day-interrupt-using-local-time-s7-300-s7-400)
- [SET_SW: Set daylight saving time/standard time without time-of-day status (S7-300, S7-400)](#set_sw-set-daylight-saving-timestandard-time-without-time-of-day-status-s7-300-s7-400)
- [SET_SW_S: Set daylight saving time/standard time with time-of-day status (S7-300, S7-400)](#set_sw_s-set-daylight-saving-timestandard-time-with-time-of-day-status-s7-300-s7-400)
- [TIMESTMP: Transfer time-stamped alarms (S7-300, S7-400)](#timestmp-transfer-time-stamped-alarms-s7-300-s7-400)
- [WS_RULES: Rule DB for converting the base time to local time (S7-300, S7-400)](#ws_rules-rule-db-for-converting-the-base-time-to-local-time-s7-300-s7-400)

##### LOC_TIME: Calculate local time (S7-300, S7-400)

###### Description

The instruction reads the time-of-day status and time-of-day of the CPU and calculates the local time from this information. It only works with S7-400 CPUs. The instruction can be called in OBs of every priority class.

###### Functional description

Internally, "LOC_TIME" uses the " [RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" instruction to read out the module time, the correction value with sign and the daylight-saving time ID from the current time-of-day status of the CPU. "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" errors terminate the block. The error codes are passed to RET_VAL .

The correction value is the number of half-hours between the basic time and local time. It is also identified as daylight-saving or standard time.

If the CPU does not have a valid time status, "LOC_TIME" is terminated with an error.

After successfully reading out the time-of-day status, the time difference based on the correction value is added to the module time and applied to output LT .

The SUMMER output adopts the value of the daylight saving/standard time bit from the time-of-day status.

###### Parameters

The following table shows the parameters of the "LOC_TIME" instruction:

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameters** | **Declaration** | **Data type** | **Description** |
| RET_VAL | Return | INT | Error code |
| LT | Output | DATE_AND_TIME | Local time (**L**ocal **T**ime) |
| SUMMER | Output | BOOL | Daylight saving time identification  - 0: Winter - 1: Summer |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameters RET_VAL, LT and SUMMER

The following table shows the output values and the errors of "LOC_TIME":

|  |  |  |  |
| --- | --- | --- | --- |
| **RET_VAL** | **LT** | **SUMMER** | **Description** |
| 0 | Local time | TRUE/FALSE | Instruction executed without errors |
| 1 | Local time | TRUE/FALSE | No error, but jump in date |
| 8xyy | DT#90-01-01-0:0:0 | FALSE | General error codes of "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" |
| 8091 | DT#90-01-01-0:0:0 | FALSE | No time status |

##### BT_LT: Calculate local time from base time (S7-300, S7-400)

###### Description

The instruction calculates the local time for the base time set at the input.

The base time entered at the BT input is converted to the local time based on data stored in a data block (DB) and output at the LT output.

The data block (DB) contains the number of 30 minute units by which the base and local time differ and the difference between daylight saving and standard time also in units of 30 minutes.

If there is a date overflow in the conversion, this is indicated by a special return value.

The "BT_LT" instruction can be called in OBs of every priority class.

###### Parameter

The following table shows the parameters of the instruction "BT_LT":

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| BT | Input | DATE_AND_TIME | Base time |
| WS_DAT | Input | BLOCK_DB | Information on the time zone and daylight saving/standard time adjustment (rule DB)  At parameter WS_DAT, use a pointer to a data block of type "[WS_RULES](#ws_rules-rule-db-for-converting-the-base-time-to-local-time-s7-300-s7-400)". |
| RET_VAL | Return | INT | Error code |
| LT | Output | DATE_AND_TIME | Local time |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> Parameters of data type BLOCK_DB can only be transferred to FB calls, but not to FC calls.

###### Parameters RET_VAL and LT

The following table shows the output values of "BT_LT":

| RET_VAL | LT | Description |
| --- | --- | --- |
| 0 | Local time | Instruction executed without errors |
| 1 | Local time | No error, but jump in date |
| 8082 | DT#90-01-01-0:0:0 | Invalid data in the rule data block |

##### LT_BT: Calculate base time from local time (S7-300, S7-400)

###### Description

The instruction calculates the base time for the local time set at the input.

The local time entered at input LT is converted to the base time with the help of data stored in a data block (DB) and the result returned at output BT.

The data block (DB) contains the number of 30 minute units by which the base and local time differ and the difference between daylight saving and standard time also in units of 30 minutes. If there is a date overflow in the conversion, this is indicated by a special return value.

Special considerations when switching between daylight saving and standard time:

- At the changeover from standard to daylight saving time, the local time is put forward one hour. This means that the hour in between does not exist.

  At an instant LT within this hour, "LT_BT" "thinks" in daylight saving time. The result is indicated by the return value 4 or 5.
- At the changeover from daylight saving to standard time, the local time is put back one hour. This means that this one hour is passed through twice ("duplicated hour"). (For CE(S)T, the identifiers 2A and 2B are used).

  This prevents unambiguous mapping to a base time at an instant LT of this hour.

  "LT_BT" receives an LT as input parameter and must determine whether the value is a daylight saving or standard time before it converts it to BT. If LT is within the duplicated hour, the LT is interpreted as standard time. This result is indicated by the return value 2 or 3.

The "LT_BT" instruction can be called in OBs of every priority class.

###### Parameter

The following table shows the parameters of the instruction "LT_BT":

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| LT | Input | DATE_AND_TIME | Local time |
| WS_DAT | Input | BLOCK_DB | Information on the time zone and daylight saving/standard time adjustment (rule DB)  At parameter WS_DAT, use a pointer to a data block of type "[WS_RULES](#ws_rules-rule-db-for-converting-the-base-time-to-local-time-s7-300-s7-400)". |
| RET_VAL | Return | INT | Error code |
| BT | Output | DATE_AND_TIME | Base time |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> Parameters of data type BLOCK_DB can only be transferred to FB calls, but not to FC calls.

###### Parameters RET_VAL and BT

The following table shows the output values of "LT_BT":

| RET_VAL | BT | Description |
| --- | --- | --- |
| 0 | Base time | Instruction executed without errors |
| 1 | Base time | No error, but jump in date |
| 2 | Base time | The LT at the input is within the "duplicated" hour. |
| 3 | Base time | As for 2, but with additional date jump |
| 4 | Base time | The LT at the input is within the "prohibited" hour. |
| 5 | Base time | As for 4, but with additional date jump |
| 8082 | DT#90-01-01-0:0:0 | Invalid data in the rule data block |

##### S_LTINT: Set time-of-day interrupt using local time (S7-300, S7-400)

###### Description

The instruction generates the required time-of-day interrupt at the set instant. This time is set in local time.

The local time entered at input LT is converted to the base time using the rule that is stored in a data block (DB).

The data block (DB) contains the number of 30 minute units by which the base and local time differ and the difference between daylight saving and standard time also in units of 30 minutes. The parameters of the specified time-of-day interrupt OB are set and the OB activated with the calculated base time. If there is a date overflow in the conversion, this is indicated by a special return value.

Special considerations when switching between daylight saving and standard time:

- At the changeover from standard to daylight saving time, the local time is put forward one hour. This means that the hour in between does not exist.

  At an instant LT within this hour, "S_LTINT" calculates the time in daylight saving format. This process is indicated by the return value (RET_VAL) 4 or 5.
- At the changeover from daylight saving to standard time, the local time is put back one hour. This means that this one hour is passed through twice ("duplicated hour"). (For CE(S)T, the identifiers 2A and 2B are used).

  This prevents unambiguous mapping to a base time at an instant LT of this hour. "S_LTINT" receives an LT as input parameter and must determine whether the value is a daylight saving or standard time before it converts it to BT. If LT is within the duplicated hour, the LT is interpreted as standard time. This process is indicated by the return value (RET_VAL) 2 or 3.

The "S_LTINT" instruction can be called in OBs of every priority class.

###### Parameter

The following table shows the parameters of the instruction "S_LTINT":

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| OB_NR | Input | INT | Number of the OB to be started (permitted 10 – 17) |
| SDT | Input | DATE_AND_TIME | Start date and time-of-day in local time  See also: "[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)" |
| PERIOD | Input | WORD | Periods from start point SDT onwards:  - W#16#0000 = once - W#16#0201 = once every minute - W#16#0401 = once hourly - W#16#1001 = once daily - W#16#1201 = once weekly - W#16#1401 = once monthly - W#16#1801 = once yearly - W#16#2001 = at month's end |
| WS_DAT | Input | BLOCK_DB | Information on the time zone and daylight saving/standard time adjustment (rule DB)  At parameter WS_DAT, use a pointer to a data block of type "[WS_RULES](#ws_rules-rule-db-for-converting-the-base-time-to-local-time-s7-300-s7-400)". |
| RET_VAL | Return | INT | Error code |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> Parameters of data type BLOCK_DB can only be transferred to FB calls, but not to FC calls.

###### Parameters RET_VAL

| RET_VAL | Description |
| --- | --- |
| 0 | Instruction executed without errors |
| 1 | No error, but jump in date |
| 2 | The LT at the input was within the "duplicated" hour. |
| 3 | As for 2, but with additional date jump |
| 4 | The LT at the input is within the "prohibited" hour. |
| 5 | As for 4, but with additional date jump |
| 8082 | Invalid data in the rule data block |
| 8090 | Incorrect parameter OB_NR |
| 8091 | Incorrect parameter SDT |
| 8092 | Incorrect parameter PERIOD |
| 80A1 | The set start time is in the past. |
| 80A2 | OB is not loaded |
| 80A3 | OB cannot be started |

##### SET_SW: Set daylight saving time/standard time without time-of-day status (S7-300, S7-400)

###### Description

The instruction supports the switch from daylight-saving time to standard time in CPUs that are not equipped with time-of-day status. The instruction "SET_SW" adjusts the CPU clock according to the current time and the adjustment rules in the rule DB.

"SET_SW" is called in the organization block OB1 and in a time-of-day interrupt OB once with the same instance. In the time-of-day interrupt OB, the parameters of the "SET_SW" instruction are not connected. The data block (DB) that contains the rule for the start and end of daylight-saving time is specified at input WS_DAT.

The following figure shows the time chart on which the function of "SET_SW" is based:

![Description](images/18003321355_DV_resource.Stream@PNG-en-US.png)

There are four adjustment times (S<sub>A</sub>, S, W<sub>A</sub>, W) defined. Their precise position is derived from the rules in the rule DB. The notification hours are one hour before the adjustment times and signal the pending adjustment.

A positive edge at the input REQ triggers initialization and activation of the daylight-saving/standard time adjustment. This setting remains valid as long as REQ = 1.

For the time adjustment, "SET_SW" sets the parameters and activates the specified time-of-day interrupt OB with the next changeover time in the mode "once". The time-of-day interrupt OB then takes over control. When it becomes due, it changes the time on the CPU according to the current call time and sets parameters and activates itself for the next changeover time.

If the current time is in segment (3), the time-of-day interrupt OB is set to the start time W<sub>A</sub> ("standard time notification").

On a falling edge at REQ, the daylight-saving/standard time adjustment is disabled.

###### Parameters

The following table shows the parameters of the instruction "SET_SW":

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | BOOL | Control of the changeover |
| WS_DAT | Input | BLOCK_DB | Information on the time zone and daylight-saving/standard time adjustment (rule DB)  At parameter WS_DAT, use a pointer to a data block of type "[WS_RULES](#ws_rules-rule-db-for-converting-the-base-time-to-local-time-s7-300-s7-400)". |
| OB_NR | Input | INT | Number of the time-of-day interrupt to be used |
| STATUS | Output | INT | Error code |
| ISSUMMER | Output | BOOL | 1 = Daylight saving time |
| ANN_1 | Output | BOOL | 1 = notification of a changeover |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> Parameters of data type BLOCK_DB can only be transferred to FB calls, but not to FC calls.

###### Parameters STATUS

| STATUS | Meaning |
| --- | --- |
| 0 | No error |
| 8xyy | General error codes of "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" |
| 8082 | Invalid data in WS_DAT |
| 8083 | The month number for the change to standard time is higher than the month number for the change to daylight-saving time and notification hour for standard time is earlier than the hour for daylight-saving or  the month number for the change to standard time is lower than the month number for the change to daylight-saving time and the notification hour for daylight-saving is earlier than the hour for standard time. |
| 8090 | Illegal OB_NR. (Only time-of-day interrupts permitted: OB10 – OB17, depending on the CPU) |
| 80A2 | Illegal OB_NR: The OB is not loaded on the CPU |
| 80A3 | The OB cannot be started. See also: "[QRY_TINT](#qry_tint-query-status-of-time-of-day-interrupt-s7-300-s7-400)" |

###### Application

"SET_SW" can be used in CPUs that are not equipped with time-of-day status. CPUs with time-of-day status use "[SET_SW_S](#set_sw_s-set-daylight-saving-timestandard-time-with-time-of-day-status-s7-300-s7-400)".

###### Calling OBs

"SET_SW" must be called with the same instance in the following organization blocks (OBs):

- **OB1 (cyclic program):**

  "SET_SW" evaluates the REQ input. Based on the current time, the OB it sets the start of the specified time-of-day interrupt to the next of four possible changeover times and activates the time-of-day interrupt with the 'once' identifier at the positive edge at REQ. The time-of-day interrupt is triggered when this time is reached.
- **OB1x (time-of-day interrupt):**

  OB1x became active because a changeover time was reached. "SET_SW" sets the time on the CPU according to the current time (daylight-saving time!), sets its parameters to the next changeover time and activates it. In segment (5), it sets itself to the daylight-saving time notification (S<sub>A</sub>) of the next year.

"Multiple instances of SET_SW" are not permitted.

You can use the following instructions to query, set and activate the time-of-day interrupt: "[QRY_TINT](#qry_tint-query-status-of-time-of-day-interrupt-s7-300-s7-400)", "[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)", "[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)", "[CAN_TINT](#can_tint-cancel-time-of-day-interrupt-s7-300-s7-400)"

###### Note

Adjusting the CPU time, for example from a PG, when "SET_SW" (REQ = 1) is activated is only permitted without special measures if this does not result in the time being adjusted past one of the changeover points.

If you missed out on one of the changeover points while adjusting the clock, you have to disable daylight-saving/standard time adjustment with REQ = 0 and then restart it with REQ = 1 after having completed the adjustment.

When you set the CPU clock, you must, of course, make sure that you set the daylight-saving time hour in summer.

##### SET_SW_S: Set daylight saving time/standard time with time-of-day status (S7-300, S7-400)

###### Description

The instruction supports the switch from daylight-saving time to standard time in CPUs that are equipped with time-of-day status. The instruction "SET_SW_S" adjusts the CPU clock according to the current time and the adjustment rules in the rule DB.

"SET_SW_S" is called in the organization block OB1 and in a time-of-day interrupt OB 1x with the same instance. In the time-of-day interrupt OB, the parameters of the "SET_SW_S" instruction are not connected. The data block (DB) that contains the rule for the start and end of daylight-saving time is specified at input WS_DAT.

The following figure shows the time chart on which the function of "SET_SW_S" is based:

![Description](images/18003321355_DV_resource.Stream@PNG-en-US.png)

There are four adjustment times (S<sub>A</sub>, S, W<sub>A</sub>, W) defined. Their precise position is derived from the rules in the rule DB. The notification hours are 1 hour before the adjustment times and signal the pending adjustment.

A positive edge at the input REQ triggers initialization and activation of the daylight-saving/standard time adjustment. This setting remains valid as long as REQ = 1.

For the time adjustment, "SET_SW_S" sets the parameters and activates the specified time-of-day interrupt OB with the next changeover time in the mode "once". The time-of-day interrupt OB then takes over control. When it becomes due, it changes the time and the time status on the CPU according to the current call time and sets its parameters and activates itself for the next changeover time.

Example: If the current time is in segment (3), the time-of-day interrupt OB is set to the start time WA ("standard time notification").

On a falling edge at REQ, the daylight-saving/standard time adjustment is disabled.

###### Parameters

The following table shows the parameters of the instruction "SET_SW_S":

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | BOOL | Control of the changeover |
| WS_DAT | Input | BLOCK_DB | Information on the time zone and daylight-saving/standard time adjustment (rule DB)  At parameter WS_DAT, use a pointer to a data block of type "[WS_RULES](#ws_rules-rule-db-for-converting-the-base-time-to-local-time-s7-300-s7-400)". |
| OB_NR | Input | INT | Number of the time-of-day interrupt to be used |
| STATUS | Output | INT | Error code |
| ISSUMMER | Output | BOOL | It is summer (DST) |
| ANN_1 | Output | BOOL | Notification of the adjustment |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> Parameters of data type BLOCK_DB can only be transferred to FB calls, but not to FC calls.

###### Parameter STATUS

| STATUS | Meaning |
| --- | --- |
| 0 | No error |
| 8xyy | General error codes of "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" |
| 8082 | Invalid data in WS_DAT |
| 8083 | The month number for the change to standard time is higher than the month number for the change to daylight-saving time and notification hour for standard time is earlier than the hour for daylight-saving or  the month number for the change to standard time is lower than the month number for the change to daylight-saving time and the notification hour for daylight-saving is earlier than the hour for standard time. |
| 8090 | Illegal OB_NR. (Only time-of-day interrupts permitted: OB10 – OB17, depending on the CPU) |
| 8091 | Time status invalid ('status_valid' in time status set to FALSE) |
| 80A2 | Illegal OB_NR: The OB is not loaded on the CPU |
| 80A3 | The OB cannot be started. (see "[QRY_TINT](#qry_tint-query-status-of-time-of-day-interrupt-s7-300-s7-400)") |

###### Application

"SET_SW_S" can be used in CPUs that are equipped with time-of-day status.

###### Calling OBs

"SET_SW_S" must be called with the same instance in the following organization blocks (OBs):

- **OB1 (cyclic program):**

  "SET_SW_S" evaluates the REQ input. Based on the current time, the OB it sets the start of the specified time-of-day interrupt to the next of four possible changeover times and activates the time-of-day interrupt with the 'once' identifier at the positive edge at REQ. The time-of-day interrupt is therefore triggered when this time is reached.
- **OB1x (time-of-day interrupt):**

  OB1x became active because a changeover time was reached. "SET_SW_S" sets the time-of-day and the time-of-day status on the CPU according to the current time, sets its parameters to the next changeover time and activates it. In segment (5), it sets itself to the daylight-saving notification of the next year.

"Multiple instances of SET_SW_S" are not permitted.

You can use the following instructions to query, set and activate the time-of-day interrupt: "[QRY_TINT](#qry_tint-query-status-of-time-of-day-interrupt-s7-300-s7-400)", "[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)", "[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)", "[CAN_TINT](#can_tint-cancel-time-of-day-interrupt-s7-300-s7-400)"

###### Note

Adjusting the CPU time, for example from a PG, when "SET_SW_S" (REQ = 1) is activated is only permitted without special measures if this does not result in the time being adjusted past one of the changeover points.

If you missed out on one of the changeover points while adjusting the clock, you have to disable daylight-saving/standard time adjustment with REQ = 0 and then restart it with REQ = 1 after having completed the adjustment.

When setting the CPU clock and the time status, make sure that you set the daylight-saving time identifier or the notification hour identifier depending on whether you are setting daylight-saving or standard time.

##### TIMESTMP: Transfer time-stamped alarms (S7-300, S7-400)

###### Description

The instruction transmits messages with time stamp of an IM153-2 to its instance DB. The data is available there for further processing by the user program.

- **IM153-2**

  The IM153-2 detects changes in binary signals, adds a time stamp to them and stores this information in data records with a maximum of 20 messages. With certain events, it outputs special messages. When a data record is ready to be fetched, the IM153-2 triggers a process interrupt.
- **Call in the hardware interrupt OB**

  "TIMESTMP" reads the start information of the process interrupt OB and stores the information relating to the time stamping in a circulating buffer for further processing. "TIMESTMP" can save the data of up to 17 process interrupts.
- **Call in the cyclic OB**:

  During cyclic processing, "TIMESTMP" reads the data record to be fetched using the instruction "[RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400)" (read data record) and stores it in the message buffer MESSAGE. If there are several data records to be fetched, the oldest is read first. If the TIMECONV bit is set at the input, "TIMESTMP" converts all time stamps from the ISP format to the DATE_AND_TIME (DT) format.

  If the parameter is BUFRDY = TRUE, the messages in the message buffer can be further processed by the user program and, for example, transferred to a recipient (HMI device or printer). The number of existing messages is indicated by the MSG_QTY parameter. After processing, the user program must reset BUFRDY to release the message buffer for further messages.

  The BUFNOTREAD parameter indicates the number of received process interrupts for which "TIMESTMP" has not yet read data records from the IM153-2 . With BUFNOTREAD = 15 all data records of the IM153-2 are filled. The IM153-2 will then recognize no additional signal changes. Additional data records that are generated by the IM153-2 at a change of binary signals are lost. The MSGLOST parameter (message loss) is set to "1".

###### Parameter

The following table shows the parameters of the instruction "TIMESTMP":

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| LADDR | Input | INT | Logical address (diagnostic address) of the IM153-2 |
| LADDR2 | Input | INT | Logical address (diagnostic address) of slot 2 of the IM153-2 |
| TIMECONV | Input | BOOL | 1 = convert ISP time stamp to S7-DT format |
| MSG_QTY | Output | INT | Number of valid message in the message buffer |
| BUFNOTREAD | Output | INT | Number of data records of the IM153-2 containing interrupts but not yet read |
| READERR | Output | BOOL | 1 = error reading from the IM153-2 |
| READSTATUS | Output | INT | Return value of instruction "[RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400)" |
| BUFRDY | InOut | BOOL | 1 = message buffer ready |
| MSGLOST | InOut | BOOL | 1 = messages lost |
| MESSAGE | Static | ARRAY[1..20] OF STRUCT | Message buffer for up to 20 messages of the IM153-2 |
| SLOT_NO | ./. | BYTE | Slot number / 2 = special message |
| CH_NO | ./. | BYTE | Channel number / ID of the special message |
| SIGNAL | ./. | BYTE | Signal state / Characteristic of the special message |
| TIME1 | ./. | DWORD | Seconds starting from 1900.0 (ISP)/Year, Month, Day, Hour ((DT) |
| TIME2 | ./. | DWORD | Fractions of seconds (ISP) / Minute, Second, Millisecond, Day of week (DT) |
|  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Hardware configuration

You can only use "TIMESTMP" in configurations that support forwarding of the time-of-day and time stamping of binary signals. These are:

- CPUs

  - CPU 4xx with CP443-5 for forwarding time frames (6GK7443-5DX02-0XE0 and higher), or
  - CPU 4xx with forwarding of time frames (for example, CPU416-2 DP as of firmware version 3.0)
- Distributed I/O

  - Interface module IM153-2 with redundancy capability with time stamping (6ES7153-2AA02 and higher, firmware version V1.2.3 (version 10))

    Or:

    IM153-2 FO with redundancy capability with integrated FO interface (6ES7153-2AB01 and higher, firmware version V1.2.3 and higher (version 9))
  - Digital input SM321 (6ES7321-7BH00-0AB0) isolated 16 DI, 24 V DC, hardware interrupt, diagnostics

    Or:

    Digital input SM321 (6ES7321-7TH00-0AB0) isolated 16 DI, 24 V DC, NAMUR, diagnostic capability, with process control functions

    You should only use time stamping for selected binary signals that are important in your application. It is advisable to distribute these signals over several IM153-2 or over several stations due to the load on PROFIBUS-DP and the IM153-2.

###### Software configuration

- Calling OBs

  "TIMESTMP" must be called with the same instance in the following organization blocks (OBs) and the block parameters must be written and read only in the cyclic program:

  - OB1 (cyclic program) or alternatively a cyclic interrupt OB (OB30 to OB38)
  - OB86 (rack failure)
  - OB100 (startup)

    If you use other startup OBs (OB101, OB102), "TIMESTMP" must be called there as well.
  - OB40 or, if selectable in the hardware configuration, also in other process interrupt OBs (OB41 to OB47)
- Addressing

  - Use a separate instance of "TIMESTMP" for each IM153-2. At the LADDR block input, enter the logical address (diagnostic address) set in the hardware configuration of the IM153-2.
  - If you use the DP master in the "S7-compatible" mode, enter the same value at input LADDR2 as for LADDR. If you use the "DPV1" mode, enter the diagnostic address of slot 2 of the IM153-2 for LADDR2 .
  - If you change addresses during operation, "TIMESTMP" deletes the previously stored process interrupt data.

###### Error handling

If "TIMESTMP" detects unrecoverable errors when reading a data record, "TIMESTMP" sets the READERR parameter to TRUE. The return value of the WR_USMSG instruction is available for further analysis in the READSTATUS parameter. Because "TIMESTMP" possibly reads another data record in the next cycle, READERR and READSTATUS are valid for only one cycle. You should therefore include suitable evaluation in the user program.

If data records are read while the DP master is out of service, "TIMESTMP" will output READERR = TRUE and READSTATUS =80B2h ("The configured slot is not in use").

###### Startup characteristics IM153-2

During startup/warm restart/cold restart, the IM153-2 once again outputs process interrupts for the data records; these interrupts had entries before the startup but these have not been fetched yet.

The IM153-2 enters the following messages in the first free data record:

- Special message "Begin startup data"
- Signal changes that occurred immediately prior to a CPU STOP ("incoming" or "outgoing" according to the parameter setting for the edge)
- Current signal status for all binary signals to be time stamped ("incoming" or "outgoing" according to the parameter setting for the edge)
- Special message "End startup data"

###### Startup characteristics of "TIMESTMP"

If "TIMESTMP" is called in a startup OB (OB100, OB101, OB102), "TIMESTMP" deletes all stored process interrupt data and resets BUFRDY . If data records with interrupts are known but not yet read, "TIMESTMP" sets MSGLOST (message loss) to TRUE. The user program must reset MSGLOST .

###### Response of "TIMESTMP" in OB86 (module failure)

If "TIMESTMP" is called in OB86 and if the event comes from the corresponding IM153-2, "TIMESTMP" reacts as during startup. This is, for example, the case when the IM153-2 fails and returns to operation and when the DP master returns to operation.

###### Redundancy

In H systems with two IM153-2 modules, time stamping is redundant in the following situations:

- There is communication between the two IM153-2 modules via the K bus.
- The updating of the active and passive IM153-2 modules has been completed without error.

Time stamping is interrupted during a failover between active and passive IM153-2 modules. The time for which time stamping is interrupted is indicated with the special message "Redundancy failover start/end".

Normally, the active IM153-2 module informs the passive one of the current I/O status. If this communication is disrupted, the special message "Loss of redundancy information incoming" is output. As soon as communication is possible again between the active and passive IM153-2 modules, the special message "Loss of redundancy information outgoing" is output. Later resynchronization is not possible, in other words, a failover in the case of the IM153-2 causes a loss of messages.

###### Structure of the message buffer

The message buffer contains a data record of the IM153-2. The interpretation of the time stamp depends on the setting of the TIMECONV parameter.

###### Time formats of "TIMESTMP"

If the input is TIMECONV = TRUE , all time stamps are stored in the data type DATE_AND_TIME (BCD format):

The following table shows the structure of the data type DATE_AND_TIME:

| Bytes | Contents | Range |
| --- | --- | --- |
| 0 | Year | 90 … 89  Corresponding to 1990 ... 2089 |
| 1 | Month | 01 ... 12 |
| 2 | Day | 01 ... 31 |
| 3 | Hour | 00 ... 23 |
| 4 | Minute | 00 ... 59 |
| 5 | Second | 00 ... 59 |
| 6 | 2 MSD (most significant decade) of ms | 00 ... 99 |
| 7 (4 MSB) | LSD (least significant decade) of ms | 0 ... 9 |
| 7 (4 LSB) | Day of week | 1 ... 7 (1 = Sunday) |

If the input is TIMECONV = FALSE , all time stamps are stored in ISP format (2 double words).

The following table shows the distribution of the bytes:

| Bytes | Contents | Range |
| --- | --- | --- |
| 0 … 3 | Seconds starting from 1.1.1900 0:00:00.000 | Corresponding to  1.1.1900 ... 6.2.2036 |
| 4 … 7 | Fractions of seconds in multiples of 1/2<sup>32</sup> s | 0 … &lt;1 |

The time conversion is valid in the date range covered by both time formats 1.1.1990 up to and including 6.2.2036.

##### WS_RULES: Rule DB for converting the base time to local time (S7-300, S7-400)

###### Data block of "WS_RULES" type

A data block of the "WS_RULES" type has the following structure.

| Name |  | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| // Conversion base time&lt;-&gt;local time and "Set interrupt according to local time" |  |  |  |  |
| B2L |  | Struct |  |  |
|  | S | INT | 2 | // Offset base-&gt;local time [30 min] in winter, permitted -24 ... +24. |
|  | T | INT | 2 | // Difference standard and daylight-saving time [30 min], permitted: 2 |
| // Rule for: Standard time -&gt; daylight-saving time. Default: Last Sunday in March; 2:00 a.m. |  |  |  |  |
| W2S |  | Struct |  | // in STANDARD TIME |
|  | M | BYTE | B#16#3 | // Month of conversion |
|  | W | BYTE | B#16#9 | // n-th occurrence of the day of the week (1=first, 2=second,..,9=last) |
|  | D | BYTE | B#16#1 | // Day of the week (Sunday = 1) |
|  | H | BYTE | B#16#2 | // Hour |
| // Rule for: Daylight-saving time -&gt; standard time. Default: Last Sunday in October; 3:00 a.m. |  |  |  |  |
| S2W |  |  |  | // in DAYLIGHT-SAVING TIME |
|  | M | BYTE | B#16#10 | // Month of conversion |
|  | W | BYTE | B#16#9 | // n-th occurrence of the day of the week (9 = last) |
|  | D | BYTE | B#16#1 | // Day of the week (Sunday = 1) |
|  | H | BYTE | B#16#3 | // Hour |

> **Note**
>
> **Create data block of "WS_RULES" type**
>
> You can create a data block of type "WS_RULES", by selecting type "WS_RULES" during the creation of a new DB.

> **Note**
>
> All parameters that have the BYTE format are interpreted as BCD values (binary-coded decimal value). W2S is output in standard time; S2W in daylight-saving time. The defining of the daylight-saving/standard time changeover times by a rule has been prescribed in the EU since 2002.

## String + Char (S7-300, S7-400)

This section contains information on the following topics:

- [S_COMP: Compare character strings (S7-300, S7-400)](#s_comp-compare-character-strings-s7-300-s7-400)
- [S_CONV: Convert character string (S7-300, S7-400)](#s_conv-convert-character-string-s7-300-s7-400)
- [ATH: Convert ASCII string to hexadecimal number (S7-300, S7-400)](#ath-convert-ascii-string-to-hexadecimal-number-s7-300-s7-400)
- [HTA: Convert hexadecimal number to ASCII string (S7-300, S7-400)](#hta-convert-hexadecimal-number-to-ascii-string-s7-300-s7-400)
- [Other instructions (S7-300, S7-400)](#other-instructions-s7-300-s7-400)

### S_COMP: Compare character strings (S7-300, S7-400)

#### Description

The instruction compares the contents of two tags in the STRING format and outputs the result of the comparison as a return value. The tags that are to be compared will be interconnected at the IN1 and IN2 inputs. You can only assign a symbolically defined tag for the input parameters.

Use the instruction box to select the comparison condition. If the comparison condition (for example, greater or equal) is satisfied, the signal state is set to "1" on the output parameter OUT .

The following comparison options can be used:

| Symbol | Description |
| --- | --- |
| EQ | The return value has the signal state "1" if the string at the IN1 parameter is the same as the string at the IN2 parameter. |
| NE | The return value has the signal state "1" if the string at the IN1 parameter is not equal to the string at the IN2 parameter. |
| GT <sup>(1)</sup> | The return value has the signal state “1" if the string at the IN1 parameter is greater than the string at the IN2 parameter. |
| LT <sup>(1)</sup> | The return value has the signal state "1" if the string at the IN1 parameter is less than the string at the IN2 parameter. |
| GE <sup>(1)</sup> | The return value has the signal state "1" if the string at the IN1 parameter is greater than or equal to the string at the IN2 parameter. |
| LE <sup>(1)</sup> | The return value has the signal state "1" if the string at the IN1 parameter is less than or equal to the string at the IN2 parameter. |
| <sup>(1)</sup> The characters are compared by their ASCII code (for example, 'a' is greater than 'A'), starting from the left. The first character to be different decides the result of the comparison. If the first characters are the same, the longer string is greater. |  |

#### Parameters

The following table shows the parameters of the instruction "S_COMP":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | STRING* | D, L | Input tag in the STRING format. |
| IN2 | Input | STRING* | D, L | Input tag in the STRING format. |
| OUT | Output | BOOL | I, Q, M, D, L | Result of comparison |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### S_CONV: Convert character string (S7-300, S7-400)

#### Description

You use this instruction to convert the value at the IN input to the data format you have specified in the OUT output. You can use the instruction to convert character strings to integers and floating-point numbers or to convert integers and floating-point numbers to character strings.

> **Note**
>
> **Explicit conversions in SCL**
>
> You can find additional information and SCL-specific features for explicit conversions here:
>
> - [Explicit conversions](Data%20type%20conversion%20for%20S7-300%2C%20S7-400%20%28S7-300%2C%20S7-400%29.md#explicit-conversions-s7-300-s7-400)

#### Converting a character string to integers and floating-point numbers

Following conversions of a character string to integers and floating-point numbers are possible:

- Conversion of a character string to a tag in INT format. The first character in the string may be a sign or a number, the characters which then follow must be numbers. If the length of the string is equal to zero or greater than 6, or if invalid characters are found in the string, no conversion takes place and the binary result (BR) bit of the status word is set to "0". If the result of the conversion is outside the INT range, the result is limited to the corresponding value and the binary result (BR) bit of the status word is set to "0".
- Conversion of a character string to a tag in DINT format. The first character in the string may be a sign or a number, the characters which then follow must be numbers. If the length of the string is equal to zero or greater than 11, or if invalid characters are found in the string, no conversion takes place and the binary result (BR) bit of the status word is set to "0". If the result of the conversion is outside the DINT range, the result is limited to the corresponding value and the binary result (BR) bit of the status word is set to "0".
- Conversion of a character string to a tag in REAL format. The string must have the following format: ±v.nnnnnnnE±xx

  - ± = sign
  - v = 1 digit before the decimal point
  - n = 7 digits after the decimal point
  - x = 2 exponential digits

  If the length of the string is less than 14, or if it is not structured as shown above, no conversion takes place and the binary result (BR) bit of the status word is set to "0". If the result of the conversion is outside the REAL range, the result is limited to the corresponding value and the binary result (BR) bit of the status word is set to "0".

#### Converting an integer and floating-point number to a character string

The following conversions of integers and floating-point numbers to a character string are possible:

- Conversion of a tag in INT format to a character string. The character string is shown preceded by a sign. If the tag specified at the return parameter is too short, no conversion will take place and the binary result (BR) bit of the status word is set to "0". You can only assign a symbolically defined tag for the output parameter.
- Conversion of a tag in DINT format to a character string. The character string is shown preceded by a sign. If the tag specified at the return parameter is too short, no conversion will take place and the binary result (BR) bit of the status word is set to "0". You can only assign a symbolically defined tag for the output parameter.
- Conversion of a tag in REAL format to a character string. The string is shown with 14 digits: ±v.nnnnnnnE±xx

  - ± = sign
  - v = 1 digit before the decimal point
  - n = 7 digits after the decimal point
  - x = 2 exponential digits

  If the tag specified at the return parameter is too short or if no valid floating-point number is specified at the INparameter, no conversion will take place and the binary result (BR) bit of the status word is set to "0". You can only assign a symbolically defined tag for the output parameter.

#### Parameters

The following table shows the parameters of the "S_CONV" instruction:

Parameters for converting a character string to integers and floating-point numbers

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | STRING* | D, L | Value to be converted |
| OUT | Output | INT, DINT, REAL | I, Q, M, D, L | Result of the conversion. |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |

Parameters for converting an integer and floating-point number to a character string

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | INT, DINT, REAL | I, Q, M, D, L or constant | Value to be converted |
| OUT | Output | STRING* | D, L | Result of the conversion |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### ATH: Convert ASCII string to hexadecimal number (S7-300, S7-400)

#### Description

You use the instruction to convert the ASCII string specified at the IN input to a hexadecimal number. The result of the conversion is stored at the address specified by the OUT parameter.

- You specify the number of ASCII characters to be converted with the N parameter.
- A maximum of 65 535 valid ASCII characters can be converted.
- Only the numbers 0 to 9 and upper case letters A to F can be interpreted. All other characters are converted to zeros.

Since 8 bits are required for the ASCII character and only 4 bits for the hexadecimal digit, the output word length is only half of the input word length. The ASCII characters are converted and positioned in the output in the same order as they are read in. If there is an odd number of ASCII characters, the hexadecimal number is padded with zeros in the nibble to the right of the last converted hexadecimal number.

If an invalid ASCII character is detected, it is converted as "0" and an error message is output to the RET_VAL parameter.

#### Parameter

The following table shows the parameters of the "ATH" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | POINTER | D, L | Pointer to the start address of an ASCII string |
| N | Input | WORD | I, Q, M, D, L, P or constant | Number of ASCII characters to be converted |
| RET_VAL | Output | WORD | I, Q, M, D, L, P | Status of the instruction |
| OUT | Output | POINTER | I, Q, M, D, L | Pointer to the address of the result |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#....) | Description |
| --- | --- |
| 0000 | No error |
| 0007 | Invalid character |

#### Example

The instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, the N input parameter is 5 indicating that five ASCII characters are to be converted. The ASCII characters are stored in data block 1 beginning at the address specified by the IN pointer: DB1.DBX10.0. The character string is output at the address specified by the OUT pointer: Start at DB2.DBX0.0 (data block 2). Since there is an odd number of ASCII characters, the last hexadecimal digit contains only zeros in the right nibble, resulting in the hexadecimal value 0xC0.

If the instruction was executed without errors, RET_VAL will be set to the value W#16#0000.

The following table shows examples of the conversion of ASCII character strings to hexadecimal numbers.

| IN | N | OUT | BR status |
| --- | --- | --- | --- |
| '0123' | 4 | 16#0123 | 1 |
| '123AFx1a23' | 10 | 16#123AF01023 | 0 |

The following table shows the ASCII characters and the corresponding hexadecimal values.

| ASCII character | ASCII-coded hexadecimal value | Hexadecimal digit |
| --- | --- | --- |
| "0" | 30 | 0 |
| "1" | 31 | 1 |
| "2" | 32 | 2 |
| "3" | 33 | 3 |
| "4" | 34 | 4 |
| "5" | 35 | 5 |
| "6" | 36 | 6 |
| "7" | 37 | 7 |
| "8" | 38 | 8 |
| "9" | 39 | 9 |
| "A" | 41 | A |
| "B" | 42 | B |
| "C" | 43 | C |
| D | 44 | D |
| E | 45 | E |
| F | 46 | F |

### HTA: Convert hexadecimal number to ASCII string (S7-300, S7-400)

#### Description

You use the instruction to convert the hexadecimal number specified at the IN input to an ASCII string. The result of the conversion is stored at the address specified by the OUT parameter.

You specify the number of hexadecimal bytes to be converted with the N parameter. Since 8 bits are required for the ASCII character and only 4 bits for the hexadecimal digit, the output value is twice as long as the input value. Each nibble of the hexadecimal number is converted to a character while maintaining the original order.

A maximum of 65 635 characters can be written to the ASCII character string. The result of the conversion is represented by the digits 0 to 9 and upper-case letters A to F.

The instruction does not detect any error conditions.

#### Parameter

The following table shows the parameters of the "HTA" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | POINTER* | I, Q, M, D | Start address of the hexadecimal digits |
| N | Input | WORD | I, Q, M, D, L, P or constant | Number of hexadecimal bytes to be converted |
| OUT | Output | POINTER* | D, L | Address at which the result is stored. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Example

The instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, the N input parameter is set to 3 indicating that three hexadecimal characters are to be converted. The hexadecimal bytes are stored in data block 1 beginning at the address specified by the IN pointer: DB1.DBX10.0. The character string is output at the address specified by the OUT pointer: Start at DB2.DBX0.0 (data block 2).

The following table shows examples of the conversion of hexadecimal numbers to ASCII character strings:

| IN | N | OUT | BR status |
| --- | --- | --- | --- |
| W#16#0123 | 2 | '0123' | 1 |
| 16#123AF01023 | 4 | '123AF010' | 0 |

The following table shows the ASCII characters and the corresponding hexadecimal values:

| Hexadecimal digit | ASCII-coded hexadecimal value | ASCII character |
| --- | --- | --- |
| 0 | 30 | "0" |
| 1 | 31 | "1" |
| 2 | 32 | "2" |
| 3 | 33 | "3" |
| 4 | 34 | "4" |
| 5 | 35 | "5" |
| 6 | 36 | "6" |
| 7 | 37 | "7" |
| 8 | 38 | "8" |
| 9 | 39 | "9" |
| A | 41 | "A" |
| B | 42 | "B" |
| C | 43 | "C" |
| D | 44 | "D" |
| E | 45 | "E" |
| F | 46 | "F" |

### Other instructions (S7-300, S7-400)

This section contains information on the following topics:

- [LEN: Determine the length of a character string (S7-300, S7-400)](#len-determine-the-length-of-a-character-string-s7-300-s7-400)
- [CONCAT: Combine character strings (S7-300, S7-400)](#concat-combine-character-strings-s7-300-s7-400)
- [LEFT: Read the left character of a character string (S7-300, S7-400)](#left-read-the-left-character-of-a-character-string-s7-300-s7-400)
- [RIGHT: Read the right characters of a character string (S7-300, S7-400)](#right-read-the-right-characters-of-a-character-string-s7-300-s7-400)
- [MID: Read middle characters of a character string (S7-300, S7-400)](#mid-read-middle-characters-of-a-character-string-s7-300-s7-400)
- [DELETE: Delete characters in a character string (S7-300, S7-400)](#delete-delete-characters-in-a-character-string-s7-300-s7-400)
- [INSERT: Insert characters in a character string (S7-300, S7-400)](#insert-insert-characters-in-a-character-string-s7-300-s7-400)
- [REPLACE: Replace characters in a character string (S7-300, S7-400)](#replace-replace-characters-in-a-character-string-s7-300-s7-400)
- [FIND: Find characters in a character string (S7-300, S7-400)](#find-find-characters-in-a-character-string-s7-300-s7-400)

#### LEN: Determine the length of a character string (S7-300, S7-400)

##### Description

The instruction outputs the current length of a character string (number of valid characters) as return value.

A STRING tag contains two lengths:

- The maximum length (which is specified in square brackets when the tag is defined)
- The current length (this is the number of currently valid characters)

The current length must be smaller than or equal to the maximum length. The number of bytes occupied by a string is 2 greater than the maximum length. A blank string (' ') has the length zero. The maximum length is 254. The instruction does not report any errors.

##### Parameters

The following table shows the parameters of the instruction "LEN":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | STRING* | D, L* * | Input tag in the format STRING; you can only assign a symbolically defined tag for the input parameter. |
| OUT | Return | INT | I, Q, M, D, L | Number of valid characters |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type).  ** With SCL: Constants may also be used. |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### CONCAT: Combine character strings (S7-300, S7-400)

##### Description

The instruction combines two STRING tags into one character string. If the result string is longer than the tag given at the output parameter, the result string is limited to the maximum set length and the binary result (BR) bit of the status word set to "0".

##### Parameters

The following table shows the parameters of the instruction "CONCAT": You can assign only a symbolically defined tag for the parameters.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | STRING* | D, L | Input tag in the STRING format. |
| IN2 | Input | STRING* | D, L | Input tag in the STRING format. |
| OUT | Return | STRING* | D, L | Combined character string |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### LEFT: Read the left character of a character string (S7-300, S7-400)

##### Description

The instruction provides the first L characters of a string.

- If L is greater than the current length of the STRING tag, the input value is returned.
- With L = 0 and with a blank string as the input value, a blank string is returned.
- If L is negative, a blank string is output and the binary result (BR) bit of the status word is set to "0".

##### Parameters

The following table shows the parameters of the instruction "LEFT": You can only assign a symbolically defined tag for the parameter IN and the return value RET_VAL.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | STRING* | D, L | Input tag in the STRING format. |
| L | Input | INT | I, Q, M, D, L or constant | Length of the left character string |
| OUT | Return | STRING* | D, L | Output tag in format STRING |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### RIGHT: Read the right characters of a character string (S7-300, S7-400)

##### Description

The instruction provides the last L characters of a string.

- If L is greater than the current length of the STRING tag, the input value is returned.
- If L is negative, a blank string is returned and the binary result (BR) bit of the status word is set to "0".
- With L = 0 and with a blank string as the input value, a blank string is returned.

##### Parameters

The following table shows the parameters of the instruction "RIGHT": You can only assign a symbolically defined tag for the parameter IN and the return value RET_VAL.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | STRING* | D, L | Input tag in the STRING format. |
| L | Input | INT | I, Q, M, D, L or constant | Length of the right character string |
| OUT | Return | STRING* | D, L | Output tag in format STRING |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### MID: Read middle characters of a character string (S7-300, S7-400)

##### Description

The instruction provides the middle part of a character string (L characters from and including the P character).

- If the total of L and (P-1) exceeds the current length of the STRING tag, a string from the P character to the end of the input value is provided.
- In all other cases (P is outside the current length, P and/or L are equal to zero or negative), a blank string is returned and the binary result (BR) bit of the status word is set to "0".

##### Parameters

The following table shows the parameters of the instruction "MID": You can only assign a symbolically defined tag for the parameter IN and the return value RET_VAL.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | STRING* | D, L | Input tag in the STRING format. |
| L | Input | INT | I, Q, M, D, L or constant | Length of the middle character string |
| P | Input | INT | I, Q, M, D, L or constant | Position of first character |
| OUT | Return | STRING* | D, L | Output tag in format STRING |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### DELETE: Delete characters in a character string (S7-300, S7-400)

##### Description

The instruction deletes (L characters in a character string from and including the P character).

- If L and/or P are equal to zero or if P is greater than the current length of the input string, the input string is returned.
- If the sum of L and P is greater than the input string, the string is deleted up to the end.
- If L and/or P is negative, a blank string is returned and the binary result (BR) bit of the status word is set to ''0".

##### Parameters

The following table shows the parameters of the instruction "DELETE": You can only assign a symbolically defined tag for the parameter IN and the output parameter RET_VAL.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | STRING* | D, L | STRING tag in which the delete is made |
| L | Input | INT | I, Q, M, D, L or constant | Number of characters to be deleted |
| P | Input | INT | I, Q, M, D, L or constant | Position of first character to be deleted |
| OUT | Return | STRING* | D, L | Result string |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### INSERT: Insert characters in a character string (S7-300, S7-400)

##### Description

The instruction adds the character string at the IN2 parameter to the character string at the IN1 parameter after the P character.

- If P equals zero, then the second character string will be inserted before the first character string.
- If P is greater than the actual length of the first character string, then the second character string is appended to the first character string.
- If P is negative, then a blank string will be output and the binary result (BR) of the status word is set to "0".

The binary result (BR) bit is also set to "0" if the result string is longer than the tag specified at the output parameter; in this case the result string is limited to the maximum set length.

##### Parameters

The following table shows the parameters of the instruction "INSERT": You can only assign a symbolically defined tag for the input parameters IN1 and IN2 and the output parameter.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | STRING* | D, L | STRING tag in which the insertion is made |
| IN2 | Input | STRING* | D, L | STRING tag that is to be inserted |
| P | Input | INT | I, Q, M, D, L or constant | Insert position |
| OUT | Return | STRING* | D, L | Result string |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### REPLACE: Replace characters in a character string (S7-300, S7-400)

##### Description

The instruction replaces the number of L characters of the first character string (IN1) starting from and including the P character by the complete second character string (IN2).

- If L equals zero and P does not equal zero, then the first string is returned.
- If L equals zero and P equals zero, then the second string is positioned in front of the first string.
- If L does not equal zero and P equals zero or one, it is replaced starting from and including the first character.
- If P is outside the first string, then the second string is appended to the first string.
- If L and/or P are/is negative, then a blank string will be returned and the binary result (BR) bit of the status word is set to ''0". The binary result (BR) bit is also set to "0" if the result string is longer than the tag specified at the output parameter; in this case the result string is limited to the maximum set length.

##### Parameters

The following table shows the parameters of the instruction "REPLACE": You can only assign a symbolically defined tag for the input parameters IN1 and IN2 and the output parameter.

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | STRING* | D, L | STRING tag in which the insertion is made |
| IN2 | Input | STRING* | D, L | STRING tag that is to be inserted |
| L | Input | INT | I, Q, M, D, L or constant | Number of characters to be replaced |
| P | Input | INT | I, Q, M, D, L or constant | Position of first replaced character |
| OUT | Return | STRING* | D, L | Result string |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### FIND: Find characters in a character string (S7-300, S7-400)

##### Description

The instruction provides the position of the second string (IN2) within the first string (IN1). The search begins left. The first occurrence of the string is reported.

If the second character string does not exist in the first or if both character strings are identical, zero is returned. The instruction does not report any errors.

##### Parameters

The following table shows the parameters of the instruction "FIND": You can only assign a symbolically defined tag for the input parameters IN1 and IN2 .

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | STRING* | D, L | STRING tag in which the search is made |
| IN2 | Input | STRING* | D, L | STRING tag that is searched for |
| OUT | Return | INT | I, Q, M, D, L | Position of the string found |
| * Define the maximum length of the character string if you use the data type STRING in the interface declaration for a temporary variable (you will find further information in the description of the data type). |  |  |  |  |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

## Process image (S7-300, S7-400)

This section contains information on the following topics:

- [UPDAT_PI: Update the process image inputs (S7-300, S7-400)](#updat_pi-update-the-process-image-inputs-s7-300-s7-400)
- [UPDAT_PO: Update the process image outputs (S7-300, S7-400)](#updat_po-update-the-process-image-outputs-s7-300-s7-400)
- [SYNC_PI: Synchronize the process image inputs (S7-300, S7-400)](#sync_pi-synchronize-the-process-image-inputs-s7-300-s7-400)
- [SYNC_PO: Synchronize the process image outputs (S7-300, S7-400)](#sync_po-synchronize-the-process-image-outputs-s7-300-s7-400)

### UPDAT_PI: Update the process image inputs (S7-300, S7-400)

#### Description

With the instruction, you update the OB 1 process image (=process image partition 0) of the inputs or a process image partition input of the inputs defined by configuration.

If you have configured repeated signaling of I/O access errors for the system-side process image update, then the selected process image will be updated constantly.

Otherwise, this update will only be performed if the selected process image partition is not updated by the system, in other words:

- If you have not assigned this process image partition to an interrupt OB,  
    or
- If you selected process image partition 0 and have disabled updating of the OB 1 process image partition during configuration.

  > **Note**
  >
  > Each logical address that you have assigned to a process image partition input table per configuration no longer belongs to the OB 1 process image input table.   
  > When you update a process image partition with "UPDAT_PI", you must not perform a simultaneous update with the "[SYNC_PI](#sync_pi-synchronize-the-process-image-inputs-s7-300-s7-400)" instruction.

System-side updating of the OB 1 process image input table and the process image partitions of inputs that you have assigned to an interrupt OB takes place independently of "UPDAT_PI" calls.

#### Parameter

The following table shows the parameters of the instruction "UPDAT_PI":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PART | Input | BYTE | I, Q, M, D, L or constant | Number of the process image partition input table to  be updated. Maximum value range (depending on the CPU):   0 to 15 (0 means OB 1 process image, n where 1 &lt; n &lt; 15 means process image partition n) |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| FLADDR | Output | WORD | I, Q, M, D, L | Address of the first byte to cause an error  if an access error has occurred. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Illegal value for PART parameter |
| 8091 | The specified process image partition was not yet defined or is not located in the permitted process image area on the CPU. |
| 8092 | The process image partition is being updated by the system with an OB and  you have not configured repeated signaling of all I/O access errors for this purpose. An update with "UPDAT_PI" was not performed. |
| 80A0 | An access error was detected when accessing the I/O. |
| 8xyy | For general error information, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

> **Note**
>
> If you use the instruction for process image partitions of DP standard slaves for which you have defined a consistency area greater than 32 bytes, the error codes of the "[DPRD_DAT](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction are also possible.

### UPDAT_PO: Update the process image outputs (S7-300, S7-400)

#### Description

You use the instruction to transfer the signal states of the OB 1 process image (= process image partition 0) of the outputs or a process image partition of the outputs defined per configuration to the output modules.

If you have specified a consistency range for the selected process image partition, corresponding data is transferred as consistent data to the respective I/O module.

> **Note**
>
> Each logical address you have assigned to a process image partition output table during configuration no longer belongs to the OB 1 process image output table.   
> Outputs that you update with "UPDAT_PO" must not be updated simultaneously with the "[SYNC_PO](#sync_po-synchronize-the-process-image-outputs-s7-300-s7-400)" instruction.

The OB 1 process image output table and the process image partitions of the outputs that you have assigned to an interrupt OB are transferred by the system to the output modules independently of "UPDAT_PO" calls.

#### Parameter

The following table shows the parameters of the instruction "UPDAT_PO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PART | Input | BYTE | I, Q, M, D, L or constant | Number of the process image partition output table to be transferred.   Maximum value range (depending on the CPU): 0 to 15.  (0 means OB 1 process image, n where 1 &lt; n &lt; 15 means process image partition n) |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| FLADDR | Output | WORD | I, Q, M, D, L | Address of the first byte to cause an error  if an access error has occurred. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Illegal value for PART parameter |
| 8091 | The specified process image partition was not yet defined or is not located in the permitted process image area on the CPU. |
| 80A0 | An access error was detected when accessing the I/O. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

> **Note**
>
> If you use the instruction for process image partitions of DP standard slaves for which you have defined a consistency area greater than 32 bytes, the error codes of the "[DPWR_DAT](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction are also possible.

### SYNC_PI: Synchronize the process image inputs (S7-300, S7-400)

#### Description

The "SYNC_PI" is used to update the process image partition of inputs in isochronous mode. A user program linked to a DP cycle or PN send cyle can use this instruction to update input data acquired in a process image partition input table isochronously and consistently.

#### Call

"SYNC_PI" is interruptible and can only be called in OBs 61, 62, 63, and 64.

> **Note**
>
> A call of the "SYNC_PI" instruction in OBs 61 to 64 not allowed unless you have assigned the process image partition concerned to the associated OB in the hardware configuration.
>
> Process image partitions updated with "SYNC_PI" may not be updated by means of "[UPDAT_PI](#updat_pi-update-the-process-image-inputs-s7-300-s7-400)" as well.

#### Parameter

The following table shows the parameters of the instruction "SYNC_PI":

| Parameter | Declaration | Data type | Memory area | Range of values | Description |
| --- | --- | --- | --- | --- | --- |
| PART | Input | BYTE | I, Q, M, D, L or constant | 1 to 30 | Number of the process image partition input table to be updated isochronously. |
| RET_VAL | Return | INT | I, Q, M, D, L | - | Error information |
| FLADDR | Output | WORD | I, Q, M, D, L | - | Address of the first byte to cause an error  if an access error has occurred. |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Event class error code | Explanation |
| --- | --- |
| W#16#0001 | Consistency warning. The update of the process image partition was distributed over two DP and PN cycles. However, the data in one slave or IO device were consistently transferred. |
| W#16#8090 | Illegal value on PART parameter or updating the specified process image partition input table is not permitted in this OB. The process image partition input table was not updated. |
| W#16#8091 | The specified process image partition was not yet defined or is not located in the permitted process image area on the CPU. The process image partition input table was not updated. |
| W#16#80A0 | During updating an access error was detected. The affected inputs were set to "0". |
| W#16#80A1 | The update time is after the permitted access window. The process image partition input table was not updated.  The DP or PN cycle is too short to ensure enough time for processing the instruction. You must therefore increase the TDP (also known as T_DC), Ti, and To timers. |
| W#16#80A2 | Access error with consistency warning  In the case of update of the specified process image partition an access error with simultaneous consistency warning was detected.  - The data of the incorrect inputs was not read by the I/O. In the process image partition of the inputs the involved inputs are set to zero. - The update of the process image partition of the not involved by an access error input data was distributed over two DP and PN cycles. |
| W#16#80C1 | The update time is before the permitted access window. The process image partition input table was not updated. |
| W#16#8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

> **Note**
>
> If you use the "SYNC_PI" instruction for process image partitions of DP standard slaves for which you have defined a consistency area greater than 32 bytes, the error codes of the "[DPRD_DAT](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction are also possible.

### SYNC_PO: Synchronize the process image outputs (S7-300, S7-400)

#### Description

Instruction "SYNC_PO" is used to update a process image partition of outputs in isochronous mode A user program linked to a DP cycle can use this instruction to transfer the calculated output data of a process image partition outputs to the I/O isochronously and consistently.

#### Call

"SYNC_PO" is interruptible and can only be called in OBs 61, 62, 63, and 64.

> **Note**
>
> A call of the "SYNC_PO" instruction in OBs 61 to 64 is only permitted if you have assigned the affected process image partition to the associated OB in the HW configuration.
>
> A process image partition that you update with "SYNC_PO" must not be updated simultaneously with the "[UPDAT_PO](#updat_po-update-the-process-image-outputs-s7-300-s7-400)" instruction.

#### Parameter

The following table shows the parameters of the instruction "SYNC_PO":

| Parameter | Declaration | Data type | Memory area | Range of values | Description |
| --- | --- | --- | --- | --- | --- |
| PART | Input | BYTE | I, Q, M, D, L or constant | 1 to 30 | Number of the process image partition output table to be updated isochronously. |
| RET_VAL | Return | INT | I, Q, M, D, L | - | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| FLADDR | Output | WORD | I, Q, M, D, L | - | Address of the first byte that has caused the error. |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Event class error code | Explanation |
| --- | --- |
| W#16#0001 | Consistency warning. The update of the process image partition was distributed over two DP and PN cycles. However, the data in one slave or IO device were consistently transferred. |
| W#16#8090 | Illegal value in PART parameter, or updating the specified process image partition output table is not permitted in this OB. Outputs were not transferred to the I/O. The process image partition output table remains unchanged. |
| W#16#8091 | The specified process image partition was not yet defined or is not located in the permitted process image area on the CPU. Outputs were not transferred to the I/O. The process image partition output table remains unchanged. |
| W#16#80A0 | In the case of update of the specified process image partition of the outputs an access error was detected. Incorrect outputs were not transferred to the I/O. During process image partition of the outputs, these outputs remain unchanged. |
| W#16#80A1 | Access error with consistency warning  In the case of update of the specified process image partition of the outputs an access error with simultaneous consistency warning was detected.  - The data of the incorrect outputs were not transferred to the I/O. During process image partition of the outputs, the involved outputs remain unchanged. - The update of the process image partition of the not involved by an access error input data was distributed over two DP and PN cycles. |
| W#16#80A2 | The update time is after the permitted access window. Outputs were not transferred to the I/O. The process image partition output table remains unchanged. |
| W#16#80C1 | The update time is before the permitted access window. Outputs were not transferred to the I/O. The process image partition output table remains unchanged. |
| W#16#8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

> **Note**
>
> If you use the "SYNC_PO" instruction for process image partitions of DP standard slaves for which you have defined a consistency area greater than 32 bytes, the error codes of the "[DPWR_DAT](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction are also possible.

## Distributed I/O (S7-300, S7-400)

This section contains information on the following topics:

- [RDREC: Read data record (S7-300, S7-400)](#rdrec-read-data-record-s7-300-s7-400)
- [WRREC: Write data record (S7-300, S7-400)](#wrrec-write-data-record-s7-300-s7-400)
- [GETIO: Read process image (S7-300, S7-400)](#getio-read-process-image-s7-300-s7-400)
- [SETIO: Transfer process image (S7-300, S7-400)](#setio-transfer-process-image-s7-300-s7-400)
- [GETIO_PART: Read process image area (S7-300, S7-400)](#getio_part-read-process-image-area-s7-300-s7-400)
- [SETIO_PART: Transfer process image area (S7-300, S7-400)](#setio_part-transfer-process-image-area-s7-300-s7-400)
- [RALRM: Receive interrupt (S7-300, S7-400)](#ralrm-receive-interrupt-s7-300-s7-400)
- [D_ACT_DP: Enable/disable DP slaves (S7-300, S7-400)](#d_act_dp-enabledisable-dp-slaves-s7-300-s7-400)
- [Additional instructions (S7-300, S7-400)](#additional-instructions-s7-300-s7-400)

### RDREC: Read data record (S7-300, S7-400)

#### Description

You use the instruction to read the data record with the number INDEX from the component addressed using the ID . This may be a module in a central rack or a distributed component (PROFIBUS DP or PROFINET IO).

With MLEN , you specify the maximum number of bytes you want to read. The selected length of the destination area RECORD should have at least the length of MLEN bytes.

The value TRUE for the output parameter VALID indicates that the data record was successfully transferred to the destination area RECORD . In this case, the LEN output parameter contains the length of the read data in bytes.

If an error has occurred during transfer of the data record, this is indicated by the output parameter ERROR . In this case, the output parameter STATUS contains the error information.

> **Note**
>
> If a DPV1 slave is configured via GSD file (GSD rev. 3 and higher) and the DP interface of the DP master is set to "S7 compatible", then you may not read any data records from the I/O modules in the user program with "RDREC". In this case, the DP master addresses the wrong slot (configured slot + 3).
>
> Remedy: set the interface of the DP master to "DPV1".

> **Note**
>
> The interface of the "RDREC" instruction is identical to that in the "RDREC" FB defined in the standard "PROFIBUS and PROFINET Guideline Communication Function Blocks on PROFIBUS DP and PROFINET IO".

#### Functional description

"RDREC" is an instruction that works asynchronously, which means its execution extends over multiple calls. You start the data record transfer by calling RDREC with REQ  = 1.

The job status is displayed via the output parameter BUSY and the two central bytes of output parameter STATUS . The two central bytes of STATUS match the output parameter RET_VAL of the instructions that operate asynchronously.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

The transfer of the data record is complete when the output parameter BUSY has the value FALSE .

As long as the data record transfer is taking place, the destination area must not be changed, neither its length nor its content.

#### Parameter

The following table shows the parameters of the "RDREC" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Transfer data record |
| ID | Input | DWORD | I, Q, M, D, L or constant | Logical address of the DP slave/PROFINET IO component (module or sub-module)  - For an output module, bit 15 has to be set (for example, for address 5: ID:=DW#16#8005). - For  a mixed module, the lower of the two  addresses must be specified. |
| INDEX | Input | INT | I, Q, M, D, L or constant | Data record number |
| MLEN | Input | INT | I, Q, M, D, L or constant | maximum length in bytes of the data record information to be read |
| VALID | Output | BOOL | I, Q, M, D, L | New data record was received and is valid |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The reading process is not yet complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | ERROR = 1: An error occurred during the reading process. |
| STATUS | Output | DWORD | I, Q, M, D, L | Block status or error information  For interpretation of the parameter STATUS , refer to parameter [STATUS](#parameter-status-s7-300-s7-400). |
| LEN | Output | INT | I, Q, M, D, L | Length of the read data record information |
| RECORD | InOut | ANY | I, Q, M, D, L | Destination area for the read data record  Note: Note that for S7-300 CPUs, the parameter RECORD always requires the full specification of the DB parameters (for example: P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> If you use the instruction to read a data record with PROFINET IO, negative values in the INDEX, MLEN and LEN parameters are interpreted as an unsigned 16-bit integer.

### WRREC: Write data record (S7-300, S7-400)

#### Description

You use the instruction to transfer the data record RECORD to the component addressed using ID. This may be a module in a central rack or a distributed component (PROFIBUS DP or PROFINET IO).

With LEN (hidden), you specify in bytes the length of the data record to be transmitted. The selected length of the source area RECORD should have at least the length of LEN bytes.

The value TRUE at output parameter DONE indicates that the data record has been successfully transferred.

If an error has occurred during transfer of the data record, this is indicated by the output parameter ERROR . In this case, the output parameter STATUS contains the error information.

> **Note**
>
> If a DPV1 slave is configured via GSD file (GSD rev. 3 and higher) and the DP interface of the DP master is set to "S7 compatible", then you may not write any data records from the I/O modules to the user program with "WRREC". In this case, the DP master addresses the wrong slot (configured slot + 3).
>
> Remedy: set the interface of the DP master to "DPV1".

> **Note**
>
> The interface of the "WRREC" instruction is identical to that in the "WRREC" instruction defined in the standard "PROFIBUS and PROFINET Guideline Communication Function Blocks on PROFIBUS DP and PROFINET IO".

#### Functional description

"WRREC" is an instruction that works asynchronously, which means its execution extends over multiple calls. You start the data record transfer by calling WRREC with REQ  = 1.

The job status is displayed via the output parameter BUSY and the two central bytes of output parameter STATUS . The two central bytes of STATUS match the output parameter RET_VAL of the instructions that operate asynchronously.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

Note that you must assign the same value to the actual parameter of RECORD for all "WRREC"calls that belong to one and the same job. The same applies to the actual parameters of LEN.

The transfer of the data record is complete when the output parameter BUSY has the value FALSE .

#### Parameter

The following table shows the parameters of the "WRREC" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Transfer data record |
| ID | Input | DWORD | I, Q, M, D, L or constant | Logical address of the DP slave/PROFINET IO component (module or sub-module) Bit 15 must be set for an output module (e.g. for address 5: ID:=DW#16#8005). The smaller of the two addresses must be specified for a mixed module. |
| INDEX | Input | INT | I, Q, M, D, L or constant | Data record number |
| LEN | Input | INT | I, Q, M, D, L or constant | (hidden)  Maximum length of the data record to be transferred in bytes |
| DONE | Output | BOOL | I, Q, M, D, L | Data record was transferred |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The writing process is not yet complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | ERROR = 1: An error occurred during the writing process. |
| STATUS | Output | DWORD | I, Q, M, D, L | Block status or error information  For interpretation of the parameter STATUS , refer to parameter [STATUS](#parameter-status-s7-300-s7-400). |
| RECORD | InOut | ANY | I, Q, M, D, L | Data record  Note: Note that for S7-300 CPUs, the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> If you use the instruction to read a data record with PROFINET IO, negative values in the INDEX and LEN parameters are interpreted as an unsigned 16-bit integer.

### GETIO: Read process image (S7-300, S7-400)

#### Description

You use the instruction to read out all inputs of a DP standard slave/PROFINET IO device. The instruction calls the "[DPRD_DAT](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction. If there was no error during the data transmission, the data that have been read are entered in the destination area indicated by INPUTS .

The destination area must have the same length that you configured for the selected component.

If you read from a DP standard slave with a modular configuration or with several DP identifiers, you can only access the data of one component/DP identifier at the configured start address per "GETIO" call.

#### Parameter

The following table shows the parameters of the instruction "GETIO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ID | Input | DWORD | I, Q, M, D, L or constant | - Low word: logical address of the DP slave/PROFINET IO component (module or sub-module) - High word: irrelevant |
| STATUS | Output | DWORD | I, Q, M, D, L | Contains the error information of "[DPRD_DAT](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" in the form DW#16#40xxxx00 |
| LEN | Output | INT | I, Q, M, D, L | Amount of data read in bytes |
| INPUTS | InOut | ANY | I, Q, M, D | Destination area for the read data. It must have the same length as the area that you configured for the selected DP slave/PROFINET IO component. Only the BYTE data type is permitted. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter STATUS

See also: [DPRD_DAT: Read consistent data of a DP standard slave](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400).

### SETIO: Transfer process image (S7-300, S7-400)

#### Description

You use the "SETIO" instruction to consistently transfer the data from the source area spanned by OUTPUTS to the addressed DP standard slave/PROFINET IO device, and, if necessary, to the process image (if you have configured the relevant address area of the DP standard slave as a consistent range in a process image). "SETIO" calls the instruction "[DPWR_DAT](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)".

The source area must have the same length that you configured for the selected component.

In the case of a DP standard slave with a modular configuration or with several DP identifiers, you can only access one component/DP identifier of the DP slave per "SETIO" call.

#### Parameter

The following table shows the parameters of the instruction "SETIO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ID | Input | DWORD | I, Q, M, D, L or constant | - Low word: logical address of the DP slave/PROFINET IO component (module or sub-module) - High word: irrelevant |
| LEN | Input | INT | I, Q, M, D, L | irrelevant |
| STATUS | Output | DWORD | I, Q, M, D, L | Contains the error information of "[DPWR_DAT](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" in the form DW#16#40xxxx00 |
| OUTPUTS | InOut | ANY | I, Q, M, D | Source area for the data to be written. It must have the same length as the area that you configured for the selected DP slave/PROFINET IO component. Only the BYTE data type is permitted. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter STATUS

See also: [DPWR_DAT: Write consistent data of a DP standard slave](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400).

### GETIO_PART: Read process image area (S7-300, S7-400)

#### Description

You use the "GETIO_PART" instruction to consistently read part of the process image area belonging to a DP standard slave/PROFINET IO device. "GETIO_PART" calls the instruction "UBLKMOV.

> **Note**
>
> You must assign a process image partition input table to the OB in which "GETIO_PART" is called. Before calling "GETIO_PART" you must add the associated DP standard slave or the associated PROFINET IO device to this process image partition input table. If your CPU does not recognize any process image partitions or you want to call "GETIO_PART" in OB 1, you must add the associated DP standard slave or the associated PROFINET IO device to this process image input table before calling "GETIO_PART".

You use the OFFSET and LEN parameters to specify the portion of the process image area to be read for the components addressed by means of their ID.

- If there was no error during the data transmission, ERROR receives the value FALSE, and the data that have been read are entered in the destination area indicated by INPUTS.
- If there was an error during the data transmission, ERROR receives the value TRUE, and STATUS receives the error information of "UBLKMOV".
- If the destination area (parameter INPUTS) is less than LEN, then as many bytes as INPUTS can accept will be transferred. ERROR receives the value FALSE. If the destination area is greater than LEN, then the first LEN bytes of the destination area will be written. ERROR receives the value FALSE.

  > **Note**
  >
  > "GETIO_PART" does not check the process image input table for delimiters between data belonging to different PROFIBUS DP or PROFINET IO components. This means you have to make sure that the process image area specified by means of OFFSET and LEN belongs to one component. Reading of data for more than one component cannot be guaranteed for future systems and compromises the transferability to systems from other manufacturers.

#### Parameter

The following table shows the parameters of the instruction "GETIO_PART":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ID | Input | DWORD | I, Q, M, D, L or constant | - Low word: logical address of the DP slave/PROFINET IO component (module or sub-module) - High word: irrelevant |
| OFFSET | Input | INT | I, Q, M, D, L or constant | Number of the first byte to be read in the process image for the component (smallest possible value: 0) |
| LEN | Input | INT | I, Q, M, D or constant | Amount of bytes to be read |
| STATUS | Output | DWORD | I, Q, M, D, L | Contains the error information of "UBLKMOV" in the form DW#16#40xxxx00, if ERROR = TRUE |
| ERROR | Output | BOOL | I, Q, M, D, L | Error display: ERROR = TRUE if an error occurs when "UBLKMOV" is called. |
| INPUTS | InOut | ANY | I, Q, M, D | Destination area for read data:  - If the destination area is less than LEN, then as many bytes as INPUTS can accept will be transferred. ERROR receives the value FALSE. - If the destination area is greater than LEN, then the first LEN bytes of the destination area will be written. ERROR receives the value FALSE. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters STATUS and ERROR

See instruction "UBLKMOV".

### SETIO_PART: Transfer process image area (S7-300, S7-400)

#### Description

You use the "SETIO_PART" instruction to consistently transfer data from the source area spanned by OUTPUTS into a part of the process image area belonging to a DP standard slave/PROFINET IO device. "SETIO_PART" calls the instruction "UBLKMOV".

> **Note**
>
> You must assign a process image partition input table to the OB in which "SETIO_PART" is called. Before calling "SETIO_PART", you must add the associated DP standard slave or the associated PROFINET IO device to this process image partition output table. If your CPU does not recognize any process image partitions or you want to call "SETIO_PART" in OB 1, you must add the associated DP standard slave or the associated PROFINET IO device to this process image output table before calling "SETIO_PART".

You use the OFFSET and LEN parameters to specify the portion of the process image area to be written for the components addressed by means of their ID.

- If there was no error during the data transmission, ERROR receives the value FALSE.
- If there was an error during the data transmission, ERROR receives the value TRUE, and STATUS receives the error information of "UBLKMOV".
- If the source area (OUTPUTS parameter) is less than LEN, then as many bytes as OUTPUTS can accept will be transferred. ERROR receives the value FALSE. If the source area is greater than LEN, then the first LEN bytes from OUTPUTS will be transferred. ERROR receives the value FALSE.

  > **Note**
  >
  > "SETIO_PART" does not check the process image input table for delimiters between data belonging to different PROFIBUS DP or PROFINET IO components. This means you have to make sure that the process image area specified by means of OFFSET and LEN belongs to one component. Writing of data for more than one component cannot be guaranteed for future systems and compromises the transferability to systems from other manufacturers.

#### Parameter

The following table shows the parameters of the instruction "SETIO_PART":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ID | Input | DWORD | I, Q, M, D, L or constant | - Low word: logical address of the DP slave/PROFINET IO component (module or sub-module) - High word: irrelevant |
| OFFSET | Input | INT | I, Q, M, D, L or constant | Number of the first byte to be written in the process image for the component (smallest possible value: 0) |
| LEN | Input | INT | I, Q, M, D, L or constant | Amount of bytes to be written |
| STATUS | Output | DWORD | I, Q, M, D, L | Contains the error information of "UBLKMOV" in the form DW#16#40xxxx00, if ERROR = TRUE |
| ERROR | Output | BOOL | I, Q, M, D, L | Error display: ERROR = TRUE if an error occurs when "UBLKMOV" is called. |
| OUTPUTS | InOut | ANY | I, Q, M, D | Source area for the data to be written:  - If the source area is less than LEN, then as many bytes as OUTPUTS can accept will be transferred. ERROR receives the value FALSE. - If the source area is greater than LEN, then the first LEN bytes from OUTPUTS will be transferred. ERROR receives the value FALSE. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters STATUS and ERROR

See instruction "UBLKMOV".

### RALRM: Receive interrupt (S7-300, S7-400)

This section contains information on the following topics:

- [Description RALRM (S7-300, S7-400)](#description-ralrm-s7-300-s7-400)
- [Parameter STATUS (S7-300, S7-400)](#parameter-status-s7-300-s7-400)
- [Parameter TINFO (S7-300, S7-400)](#parameter-tinfo-s7-300-s7-400)
- [Parameter AINFO (S7-300, S7-400)](#parameter-ainfo-s7-300-s7-400)
- [Destination area TINFO and AINFO (S7-300, S7-400)](#destination-area-tinfo-and-ainfo-s7-300-s7-400)

#### Description RALRM (S7-300, S7-400)

##### Description

The instruction receives an interrupt with all corresponding information from an I/O module (centralized structure) or from a DP slave or PROFINET IO device component; it supplies this information to its output parameters.

The information in the output parameters contains the start information of the called OB as well as information of the interrupt source.

Call the instruction only within the interrupt OB started by the CPU operating system as a result of the I/O interrupt that is to be examined.

> **Note**
>
> If you call the instruction in an OB whose start event is not an I/O interrupt, the instruction will provide less information to your outputs.
>
> Note that you use different instance DBs when you call the instruction in different OBs. If you evaluate data resulting from an "RALRM" call outside of the associated interrupt OB, you should moreover use a separate instance DB per OB start event.

> **Note**
>
> The interface of the "RALRM" instruction is identical to that in the "RALRM" FB defined in the standard "PROFIBUS and PROFINET Guideline Communication Function Blocks on PROFIBUS DP and PROFINET IO".

##### Calling "RALRM"

You can call the instruction in three operating modes (MODE). These modes are explained in the following table.

| MODE | RALRM ... |
| --- | --- |
| 0 | ... shows the component that triggered the interrupt in the output parameter ID and sets the output parameter NEW to TRUE. |
| 1 | ... writes all output parameters, regardless of the component triggering the interrupt. |
| 2 | ... checks whether the component specified in the F_ID input parameter has triggered the interrupt.  - If not, NEW = FALSE - If yes, NEW = TRUE and all other output parameters are written. |

##### Parameters

The following table shows the parameters of the "RALRM" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | INT | I, Q, M, D, L or constant | Mode |
| F_ID | Input | DWORD | I, Q, M, D, L or constant | Logical start address of the component (module) from which interrupts will be received |
| MLEN | Input | INT | I, Q, M, D, L or constant | Maximum length of the interrupt information to be received, in bytes |
| NEW | Output | BOOL | I, Q, M, D, L | A new interrupt was received. |
| [STATUS](#parameter-status-s7-300-s7-400) | Output | DWORD | I, Q, M, D, L | Error code of the instruction or DP master |
| ID | Output | DWORD | I, Q, M, D, L | Logical start address of the component (module) from which an interrupt was received.  Bit 15 contains the I/O ID: 0 = input address, 1 = output address. |
| LEN | Output | INT | I, Q, M, D, L | Length of the received interrupt information |
| [TINFO](#parameter-tinfo-s7-300-s7-400) | InOut | ANY | I, Q, M, D, L | (task information)   Destination area for OB start and management information  Note: Note that for S7-300 CPUs, the parameter TINFO always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| [AINFO](#parameter-ainfo-s7-300-s7-400) | InOut | ANY | I, Q, M, D, L | (alarm information)   Destination area for header information and additional interrupt information  For AINFO you should provide a length of at least MLEN bytes.  Note: Note that for S7-300 CPUs, the parameter AINFO always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> If you select a destination area TINFO or AINFO that is too short, the instruction cannot enter the full information.
>
> See also: [Destination area TINFO and AINFO](#destination-area-tinfo-and-ainfo-s7-300-s7-400)

#### Parameter STATUS (S7-300, S7-400)

##### Parameter STATUS structure

The STATUS output parameter contains error information. If it is interpreted as ARRAY[1...4] OF BYTE , the error information has the following structure:

| Field element | Name | Meaning |
| --- | --- | --- |
| STATUS[1] | Function_Num | - B#16#00, if no error - Function ID from DPV1-PDU: If an error occurs, B#16#80 will be output (for read data record: B#16#DE, for write data record: B#16#DF). If no DPV1 protocol element is used: B#16#C0. |
| STATUS[2] | Error_Decode | Location of the error ID |
| STATUS[3] | Error_Code_1 | Error ID |
| STATUS[4] | Error_Code_2 | Manufacturer-specific error ID extension |

##### Field element STATUS[2]

STATUS[2] can have the following values:

| Error_Decode (B#16#...) | Source | Meaning |
| --- | --- | --- |
| 00 to 7F | CPU | No error or no warning |
| 80 | DPV1 | Error according to IEC 61158-6 |
| 81 to 8F | CPU | B#16#8x shows an error in the xth call parameter of the instruction. |
| FE, FF | DP profile | Profile-specific error |

##### Field element STATUS[3]

STATUS[3] can have the following values:

| Error_Decode (B#16#...) | Error_Code_1 (B#16#...) | Explanation according to DVP1 | Meaning |
| --- | --- | --- | --- |
| 00 | 00 | - | No error, no warning |
| 70 | 00 | reserved, reject | Initial call; no active data record transfer |
|  | 01 | reserved, reject | Initial call; data record transfer has started |
|  | 02 | reserved, reject | Intermediate call; data record transfer already active |
| 80 | 90 | reserved, pass | Invalid logical start address |
|  | 92 | reserved, pass | Illegal type for ANY pointer |
|  | 93 | reserved, pass | The DP component addressed via ID or F_ID is not configured. |
|  | 95 | - | Error when reading additional interrupt information (when reading out additional interrupt information for central or distributed I/O via an external DP interface, this error will be output as a "group error".)  Note: During link-up and update, the additional interrupt information may not be available temporarily. |
|  | 96 | - | The master CPU is in STOP mode. At that time, an OB was being processed. The instruction "[RALRM](#description-ralrm-s7-300-s7-400)" cannot supply the OB start information, the management information, the header information, or the additional interrupt information. The OB start information can be read with the "[RD_SINFO](#rd_sinfo-read-current-ob-start-information-s7-300-s7-400)" instruction. In addition, you can use the "[DPNRM_DG](#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)" instruction to asynchronously read the current diagnostics frame of the affected DP slave for OBs 4x, 55, 56, 57, 82, and 83 (address information from the OB start information). |
|  | A0 | read error | Negative acknowledgment while reading the module. |
|  | A1 | write error | Negative acknowledgement when writing  to the module |
|  | A2 | module failure | DP protocol error at layer 2 (e.g., slave failure or bus problems) |
|  | A3 | reserved, pass | General communication error or IO device / DP slave is unreachable |
|  | A4 | reserved, pass | Communication on the communication bus disrupted |
|  | A5 | reserved, pass | – |
|  | A7 | reserved, pass | DP slave or module is occupied (temporary error |
|  | A8 | version conflict | DP slave or module reports non-compatible versions |
|  | A9 | feature not supported | Function is not supported by DP slave or module |
|  | AA to AF | user specific | DP slave or module reports a manufacturer-specific error in its application. Please check the documentation from the manufacturer of the DP slave or module. |
|  | B0 | invalid index | Data record not known in module  Illegal data record number ≥ 256 |
|  | B1 | write length error | The length specified in the RECORD parameter is incorrect;  - With "[RALRM](#description-ralrm-s7-300-s7-400)": length error in AINFO, - With "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" and "[WRREC](#wrrec-write-data-record-s7-300-s7-400)": length error in MLEN |
|  | B2 | invalid slot | - The configured slot is  not occupied. - For PROFINET IO and PROFIBUS DP: IO device / DP slave is unreachable |
|  | B3 | type conflict | Actual module type  does not match  specified module type |
|  | B4 | invalid area | DP slave or module reports access to an invalid area |
|  | B5 | state conflict | DP slave or module not ready |
|  | B6 | access denied | DP slave or module denies access |
|  | B7 | invalid range | DP slave or module reports an invalid range for a parameter or value |
|  | B8 | invalid parameter | DP slave or module reports an invalid parameter |
|  | B9 | invalid type | DP slave or module reports an invalid type  - With "[RDREC](#rdrec-read-data-record-s7-300-s7-400)": buffer too small (subsets cannot be read) - With "[WRREC](#wrrec-write-data-record-s7-300-s7-400)": buffer too small (subsets cannot be written) |
|  | BA to BF | user specific | DP slave or module reports a manufacturer-specific error when accessing. Please check the documentation from the manufacturer of the DP slave or module.  Note on value B#16#BA: The following applies for PROFINET in the H system: If a data record job with the return value W#16#80BA is rejected, the job must be repeated. |
|  | C0 | read constrain conflict | With "[WRREC](#wrrec-write-data-record-s7-300-s7-400)": the data can only be written when the CPU is in STOP mode. Note: this means that writing by the user program is not possible. You can only write the data online with PG/PC.  With "[RDREC](#rdrec-read-data-record-s7-300-s7-400)": the module routes the data record, but either no data is present or the data can only be read when the CPU is in STOP mode. Note: if data can only be read when the CPU is in STOP mode, then an evaluation by the user program is not possible. In this case, you can only read the data online with PG/PC. |
|  | C1 | write constrain conflict | The data of the previous write job on the module for the same data record have not yet been processed by the module. |
|  | C2 | resource busy | The module is currently processing the maximum possible  number of jobs for a CPU. |
|  | C3 | resource unavailable | The required operating resources are currently occupied. |
|  | C4 | - | Internal temporary error. Job could not be carried out.  Repeat the job. If this error occurs often, check your installation for sources of electrical interference. |
|  | C5 | - | DP slave or module not available. |
|  | C6 | - | Data record transfer was canceled due to priority class cancellation |
|  | C7 | - | Job aborted due to warm or cold restart on the DP master |
|  | C8 to CF | - | DP slave or module reports a manufacturer-specific resource error. Please check the documentation from the manufacturer of the DP slave or module. |
|  | Dx | user specific | DP slave specific. Refer to the description of the DP slave. |
| 8x (x = 1, ... 9, A, B, C, D, E, F) | 00 to FF | - | Error in y-th call parameter (y = 1, ...15)  - Error_Code_1 = 00: Illegal operating mode - For all other values of Error_Code_1 refer also to: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| FE, FF | 00 to FF | - | Profile-specific error |

##### Field element STATUS[4]

With DPV1 errors, the DP master passes on STATUS[4] to the CPU and the instruction. Without DPV1 error, this value is set to 0, with the following exceptions for the "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" and "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" instructions:

- STATUS[4] contains the target range length from RECORD, if LEN  &gt; the target range length from RECORD
- STATUS[4]=LEN, if the actual data record length &lt; LEN &lt; the target range length from RECORD
- STATUS[4]=0, if STATUS[4] &gt; 255 has to be set.

In PROFINET IO, STATUS[4] has the value 0.

#### Parameter TINFO (S7-300, S7-400)

##### Data structure of the destination area TINFO

| Byte | Meaning |
| --- | --- |
| 0 to 19 | Start information of the OB in which "RALRM" was currently called |
| 20 and 21 | Address, for exact description, see below |
| 22 to 31 | Management information, for exact description, see below |

##### Structure of the address (bytes 20 and 21)

The address contains:

- In a central configuration, the rack number (0-31).

  ![Structure of the address (bytes 20 and 21)](images/18037747979_DV_resource.Stream@PNG-en-US.png)

- In a distributed configuration with PROFIBUS DP

  - The DP master system ID (1-32)
  - The station number (0-127).

    ![Structure of the address (bytes 20 and 21)](images/18038163851_DV_resource.Stream@PNG-en-US.png)

- In a distributed configuration with PROFINET IO:

  - The last two positions in the PROFINET IO system ID (0-15). To obtain the complete PROFINET IO system ID, you must add 100 (decimal) to it.
  - The station number (0-2047).

    ![Structure of the address (bytes 20 and 21)](images/18038182923_DV_resource.Stream@PNG-en-US.png)

##### Structure of the management information in bytes 20 to 25

| Byte no. for TINFO | Data type | Meaning |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | BYTE | central: | 0 |  |  |  |  |  |
|  |  | distributed: | PROFIBUS DP: DP master ID: 1 to 32) |  |  |  |  |  |
|  |  |  | PROFINET IO: see above |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| 21 | BYTE | central: | Module rack number (possible values: 0 to 31) |  |  |  |  |  |
| distributed: | Number of the DP station (possible values: 0 to 127) |  |  |  |  |  |  |  |
|  |  |  | PROFINET IO: see above |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| 22 | BYTE | central: | - 0: Data record 0 or data record 1 |  |  |  |  |  |
| distributed: | Bit 0 to 3: | Slave  type | 0000:  0001:  0010:  0011:  0100 – 0111: 1000:  1001 and higher: |  | DP (data record 0 structure)  DPS7 (data record 0 or data record 1 structure)  DPS7 V1 (data record 0 or data record 1 structure)  DPV1 (structure acc. to PROFIBUS DP standard)  reserved  PROFINET IO (structure acc. to PROFINET IO Standard)  reserved |  |  |  |
|  |  |  | - Bit 4 to 7: | Profile type |  |  | Reserved |  |
|  |  |  |  |  |  |  |  |  |
| 23 | BYTE | central: | - 0 |  |  |  |  |  |
|  |  | distributed: | - Bit 0 to 3: | Interrupt info type |  | 0000: |  | Transparent, which is always the case for PROFINET IO   (interrupt originates from a configured distributed module) |
|  |  |  |  |  |  | 0001: |  | Representative  (interrupt originates from a non-DPV1 slave/non IO device or a slot that is not configured) |
|  |  |  |  |  |  | 0010: |  | Generated   (interrupt generated in the CPU) |
|  |  |  |  |  |  | 0011 and higher: |  | Reserved |
|  |  |  | - Bit 4 to 7: | Structure version |  | 0000:   0001 and higher: |  | Initial  Reserved |
|  |  |  |  |  |  |  |  |  |
| 24 | BYTE | central: | - 0 |  |  |  |  |  |
|  |  | distributed: | **Flags of the PROFIBUS DP master interface module/PROFINET IO controller master interface module** |  |  |  |  |  |
|  |  |  | Bit 0 = 0: | Interrupt originating from an integrated interface  module (PROFINET IO or PROFIBUS DP) |  |  |  |  |
|  |  |  | Bit 0 = 1: | Interrupt originating from an external interface module (PROFINET IO or PROFIBUS DP) |  |  |  |  |
|  |  |  | Bit 1 to 7: | Reserved |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| 25 | BYTE | central: | - 0 |  |  |  |  |  |
|  |  | distributed: | **Flags of the PROFIBUS DP slave interface module** |  |  |  |  |  |
|  |  |  | - Bit 0: | EXT_DIAG_FLAG from the diagnostics message frame, or 0 if this bit does not exist in the interrupt  The bit is 1 if the DP slave is faulty. |  |  |  |  |
|  |  |  | - Bit 1 to 7: | Reserved |  |  |  |  |
|  |  |  | **Flags of the PROFINET IO controller interface module** |  |  |  |  |  |
|  |  |  | - Bit 0: | ARDiagnosisState or 0 if there is no information in the interrupt.  The bit is 1 if the IO device is faulty. |  |  |  |  |
|  |  |  | - Bit 1 to 7: | Reserved |  |  |  |  |

##### Structure of the management information in bytes 26 to 27 with PROFIBUS and a central configuration

| Byte no. for TINFO | Data type | Meaning |  |
| --- | --- | --- | --- |
| 26 and 27 | WORD | central: | 0 |
| WORD | distributed: | PROFIBUS ID number as unique identifier of the PROFIBUS DP slave |  |
| 28 and 29 | WORD | 0 | (Bytes 28 and 29 can be omitted) |
| 30 and 31 | WORD | 0 | (Bytes 30 and 31 can be omitted) |

##### Structure of the management information in bytes 26 to 31 with PROFINET IO

| Byte no. for TINFO | Data type | Meaning |  |
| --- | --- | --- | --- |
| 26 and 27 | WORD | distributed: | PROFINET IO device ID number as unique identifier of the PROFINET IO device |
| 28 and 29 | WORD | distributed: | Manufacturer ID |
| 30 and 31 | WORD | distributed: | ID number of the instance |

#### Parameter AINFO (S7-300, S7-400)

##### Data structure of the destination area AINFO with interrupts from PROFIBUS DP or central I/O devices

The information for PROFINET IO is provided below.

| Byte | Meaning |  |
| --- | --- | --- |
| 0 to 3 | Header information, for exact description, see below |  |
| 4 to 199 | Additional interrupt information: data for the respective interrupt: |  |
| central: | ARRAY[0] to ARRAY[195] |  |
| distributed: | ARRAY[0] to ARRAY[59] |  |

##### Structure of the header information with interrupts from PROFIBUS DP or central IO devices

| Byte | Data type | Meaning |  |  |
| --- | --- | --- | --- | --- |
| 0 | BYTE | Length of the received interrupt information in bytes |  |  |
| central:  distributed: | 4 to 224  4 to 63 |  |  |  |
| 1 | BYTE | central: | Reserved |  |
| distributed: | ID for the interrupt type |  |  |  |
| 1: 2: 3: 4: 5: 6: 31 | Diagnostics interrupt  Process interrupt  Removal interrupt  Insertion interrupt  Status interrupt  Update Interrupt  Failure of an expansion device, DP master system, or DP station |  |  |  |
| 32 to 126: | Manufacturer-specific interrupt |  |  |  |
| 2 | BYTE | Slot number of the component that triggered the interrupt |  |  |
| 3 | BYTE | central: | Reserved |  |
| distributed: | Specifier |  |  |  |
| Bits 0 and 1 | 0: no further information; 1: Incoming event, faulty slot  2: Outgoing event, slot not faulty anymore  3: Outgoing event, slot still faulty |  |  |  |
| Bit 2: | Add_Ack |  |  |  |
| Bits 3 to 7: | Sequence number |  |  |  |

##### Data structure of the destination area AINFO with interrupts from PROFINET IO

| Byte | Meaning |
| --- | --- |
| 0 to 25 | Header information, for exact description, see below |
| 26 to 1431 | Additional interrupt information: Standardized diagnostics data for the respective interrupt:  ARRAY[0] to ARRAY[1405]  Note: The additional interrupt information may also be omitted. |

##### Structure of the header information with interrupts from PROFINET IO

| Byte | Data type | Meaning |
| --- | --- | --- |
| 0 and 1 | WORD | - Bits 0 to 7: Block type - Bits 8 to 15: Reserved |
| 2 and 3 | WORD | Block length |
| 4 and 5 | WORD | Version:  - Bits 0 to 7: low byte - Bits 8 to 15: high byte |
| 6 and 7 | WORD | ID for interrupt type:  - 1: Diagnostics interrupt (incoming) - 2: Process interrupt - 3: Remove module interrupt - 4: Insert module interrupt - 5: Status interrupt - 6: Update interrupt - 7: Redundancy interrupt - 8: Controlled by supervisor - 9: Released by supervisor - 10: Configured module not inserted - 11: Return of the sub-module - 12: Diagnostics interrupt (outgoing) - 13: Slave-to-slave connection alarm - 14: Neighborhood change alarm - 15: Clock synchronization message (bus end) - 16: Clock synchronization alarm (device end) - 17: Network component alarm - 18: Time synchronization alarm (bus end) - 19 to 31: Reserved - 32 to 127: Manufacturer-specific interrupt - 128 to 65535: Reserved |
| 8 to 11 | DWORD | API (Application Process Identifier) |
| 12 to 13 | WORD | Slot number of the component triggering the interrupt (range of values 0 to 65535) |
| 14 to 15 | WORD | Submodule slot number of the component triggering the interrupt (range of values 0 to 65535) |
| 16 to 19 | DWORD | Module identification; specific information on the source of the interrupt |
| 20 to 23 | DWORD | Submodule identification; specific information on the source of the interrupt |
| 24 to 25 | WORD | Interrupt specifier:  - Bits 0 to 10: Sequence number (range of values 0 to 2047) - Bit 11: Channel diagnostics: 0: No channel diagnostics available 1: Channel diagnostics information exists - Bit 12: Status of manufacturer-specific diagnostics: 0: No manufacturer-specific status information available 1: Manufacturer-specific status information available - Bit 13: Status of diagnostics for sub-module: 0: No status information available, all errors have been corrected 1: At least one item of channel diagnostics and/or status information is available - Bit 14: Reserved - Bit 15: Application relationship diagnosis state:   - 0: None of the modules configured within this application relationship reports diagnostics information   - 1: At least one of the modules configured in this AR is reporting diagnostics information |

##### Structure of additional interrupt information with interrupts from PROFINET IO

The additional interrupt information for PROFINET IO depends on the format identifier. It can comprise multiple data blocks with the same or different format identifier. The following format identifiers are available:

- W#16#0000 to W#16#7FFF: Manufacturer-specific diagnostics

| Byte | Data type | Meaning |
| --- | --- | --- |
| 0 to 1 | WORD | Format identifier for the structure of the following data serving as additional interrupt information  W#16#0000 to W#16#7FFF: Manufacturer-specific diagnostics |
| 2 to n | BYTE | See manufacturer's manual. |

- W#16#8000: Channel diagnostics

  Channel diagnostics is output in blocks of 6 bytes each. The additional interrupt information (without format identifier) is only output for disrupted channels.

| Byte | Data type | Meaning |  |
| --- | --- | --- | --- |
| 0 to 1 | WORD | Format identifier for the structure of the following data serving as additional interrupt information  W#16#8000: Channel diagnostics |  |
| 2 to 3 | WORD | Channel number of the component triggering the interrupt (range of values: 0 to 65535):  - W#16#0000 to W#16#7FFF: Channel number of the interface module/sub-module - W#16#8000: The generic substitute for the entire sub-module - W#16#8001 to W#16#FFFF: Reserved |  |
| 4 | BYTE | Bits 0 to 2: | Reserved |
| Bits 3 to 4: | Type of error:  - 0: Reserved - 1: Incoming error - 2: Outgoing error - 3: Outgoing error, other errors present |  |  |
| Bits 5 to 7: | Type of channel:  - 0: Reserved - 1: Input channel - 2: Output channel - 3: Input/output channel |  |  |
| 5 | BYTE | Data format:  - B#16#00: Free data format - B#16#01: Bit - B#16#02: 2 bits - B#16#03: 4 bits - B#16#04: Byte - B#16#05: Word - B#16#06: Double word - B#16#07: 2 double words - B#16#08 to B#16#FF: Reserved |  |
| 6 to 7 | WORD | Type of error:  - W#16#0000: Reserved - W#16#0001: Short circuit - W#16#0002: Undervoltage - W#16#0003: Overvoltage - W#16#0004: Overload - W#16#0005: Overtemperature - W#16#0006: Wire break - W#16#0007: High limit exceeded - W#16#0008: Low limit exceeded - W#16#0009: Error - W#16#000A to W#16#000F: Reserved - W#16#0010 to W#16#001F: Manufacturer-specific - W#16#0020 to W#16#00FF: Reserved - W#16#0100 to W#16#7FFF: Manufacturer-specific - W#16#8000: Device diagnostics available - W#16#8001 to W#16#FFFF: Reserved   Not all channels support every error type. For detailed information, refer to the description of the diagnostics data for the specific device. |  |

> **Note**
>
> The section from "channel number" to "type of error" can occur from 0 to n times.

##### W#16#8001

W#16#8001: MULTIPLE (different types of diagnostics information are transmitted).

In this case, the additional interrupt information is transmitted as blocks of variable length.

| Byte | Data type | Meaning |
| --- | --- | --- |
| 0 to 1 | WORD | Format identifier for the structure of the following data serving as additional interrupt information  W#16#8001: Manufacturer-specific diagnostics and/or channel diagnostics |
| 2 to 3 | WORD | Block type |
| 4 to 5 | WORD | Block length |
| 6 | BYTE | Version: high byte |
| 7 | BYTE | Version: low byte |
| 8 to 11 | DWORD | API (only if low byte of version = 1) |
| 12 to 13 | WORD | Slot number |
| 14 to 15 | WORD | Subslot number |
| 16 to 17 | WORD | Channel number: |
| 18 to 19 | WORD | Channel properties |
| 20 to 21 | WORD | Format identifier:  - W#16#0000 to W#16#7FFF: Manufacturer-specific diagnostics - W#16#8000: Channel diagnostics - W#16#8002: Extended channel diagnostics - W#16#8003: Stepped extended channel diagnostics - W#16#8004 to W#16#80FF: Reserved |
| 22 to n | BYTE | Data depend on the format identifier |

> **Note**
>
> The section starting from "block type" can occur from 1 to n times.

##### W#16#8002

W#16#8002: Extended channel diagnostics

| Byte | Meaning |
| --- | --- |
| 0 to 1 | Format identifier W#16#8002 |
| 2 to 3 | Channel number: |
| 4 to 5 | Channel properties |
| 6 to 7 | Error type |
| 8 to 9 | Additional error value |
| 10 to 13 | Additional error information |

##### W#16#8003

W#16#8003: Stepped extended channel diagnostics

| Byte | Meaning |
| --- | --- |
| 0 to 1 | Format identifier W#16#8003 |
| 2 to 3 | Channel number: |
| 4 to 5 | Channel properties |
| 6 to 7 | Error type |
| 8 to 9 | Additional error value |
| 10 to 13 | Additional error information |
| 14 to 17 | Qualified channel qualifier |

##### W#16#8100

W#16#8100: Maintenance information

| Byte | Meaning |
| --- | --- |
| 0 to 1 | Format identifier W#16#8100 |
| 2 to 3 | Block type |
| 4 to 5 | Block length |
| 6 to 7 | Block version |
| 8 to 9 | Reserved |
| 10 to 13 | Maintenance status |

> **Note**
>
> You can find more detailed information about the structure of the additional alarm information in the Programming Manual SIMATIC PROFINET IO from PROFIBUS DP to PROFINET IO and the current version of IEC 61158-6-10-1.

#### Destination area TINFO and AINFO (S7-300, S7-400)

##### Destination area TINFO and AINFO

Depending on the respective OB in which the instruction "RALRM" is called, the destination areas TINFO and AINFO are only partially written. Refer to the table below to find out which information is entered respectively.

| Interrupt type | OB | TINFO OB status  information | TINFO Management information | AINFO Header information | AINFO Additional interrupt information |  |
| --- | --- | --- | --- | --- | --- | --- |
| Process interrupt | 4x | Yes | Yes | Yes | central: | No |
| distributed: | as supplied by PROFIBUS DP slave/PROFINET IO device |  |  |  |  |  |
| Status interrupt | 55 | Yes | Yes | Yes | Yes | Yes |
| Update interrupt | 56 | Yes | Yes | Yes | Yes | Yes |
| Manufacturer-specific  interrupt | 57 | Yes | Yes | Yes | Yes | Yes |
| I/O redundancy error | 70 | Yes | Yes | No | No | No |
| Diagnostics interrupt | 82 | Yes | Yes | Yes | central: | Data record 1 |
| distributed: | as supplied by PROFIBUS DP slave/PROFINET IO device |  |  |  |  |  |
| Insert/remove  interrupt | 83 | Yes | Yes | Yes | central: | No |
| distributed: | as supplied by PROFIBUS DP slave/PROFINET IO device |  |  |  |  |  |
| Special form of the remove module interrupt:  Controlled by supervisor | 83 | Yes | Yes | Yes | PROFINET IO only |  |
| Special form of the insert module interrupt:  Enabled by supervisor | 83 | Yes | Yes | Yes | PROFINET IO only |  |
| Unconfigured module inserted | 83 | Yes | Yes | Yes | PROFINET IO only |  |
| Rack failure/ station failure | 86 | Yes | Yes | No | No |  |
| ... all other OBs |  | Yes | No | No | No |  |

### D_ACT_DP: Enable/disable DP slaves (S7-300, S7-400)

#### Description

Use the "D_ACT_DP" instruction to specifically deactivate and reactivate configured DP slaves/PROFINET IO devices. In addition, you can determine whether each assigned DP slave or PROFINET IO device is currently activated or deactivated.

If you use the instruction to deactivate an IE/PB Link PN IO type of gateway, then all connected PROFIBUS DP slaves will also cease to function. These failures will be reported.

The instruction cannot be used on PROFIBUS PA field devices that are connected by a DP/PA link to a DP master system.

> **Note**
>
> As long as one or more "D_ACT_DP" jobs are active, you cannot load a changed configuration from the programming device to the CPU (within the scope of CiR).  
> When a changed configuration is loaded from the programming device to the CPU during ongoing operation (CiR), the CPU rejects activation of a "D_ACT_DP" job.
>
> Several runs through the cycle control point are required to perform the disabling or enabling job. Therefore, you cannot wait for the end of such a job in a programmed loop.

#### Parameter

The following table shows the parameters of the "D_ACT_DP" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Level-triggered control parameter REQ=1:  Run activation or deactivation |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Job identifier Possible values:  - 0: Request information on  whether the  addressed component is activated  or  deactivated - 1: Activate the DP slave/PROFINET IO device - 2: Deactivate the DP slave/PROFINET IO device - 3: Activate DP slave/PROFINET IO device and call OB 86 after the change of the activation state has been completed - 4: Deactivate DP slave/PROFINET IO device and call OB 86 after the change of the activation state has been completed |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Any logical address of the DP slave/PROFINET IO device. For an output address, the most significant bit must be set. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | Active code:  - BUSY=1: The job is still active. - BUSY=0: The job was terminated. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Job completed without errors. |
| 0001 | The DP slave/PROFINET IO device is active (this error code is possible only with MODE = 0.) |
| 0002 | The DP slave/PROFINET IO device is deactivated (this error code is possible only with MODE = 0.) |
| 7000 | First call with REQ= 0: The job specified with LADDR is not active; BUSY has the value "0". |
| 7001 | First call with REQ= 1. The job specified with LADDRwas triggered; BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant). The activated job is still active; BUSY has the value "1". |
| 8090 | - You have not configured a module with the address specified in LADDR. - You operate your CPU as I-Slave and you have specified in LADDR an address of this I-Slave. |
| 8092 | The deactivation of the currently addressed DP slave/PROFINET IO device (MODE=2) cannot be canceled by being activated (MODE=1). Activate the component at a later time. |
| 8093 | No DP slave/PROFINET IO device is assigned to the address specified in LADDR (no configuration available) or the MODE parameter is not known. |
| 8094 | You have attempted to activate a device which is potential partner for a tool change port. However, another device is already activated on this tool change port at this time. The activated device will remain activated. |
| 80A1 | The addressed component could not have parameters assigned. (This error code is only possible when MODE = 1.)  Note: "D_ACT_DP" returns this error information only if the activated slave/device fails again during parameter assignment. If the parameter assignment of a single module was unsuccessful, "D_ACT_DP" returns the error information W#16#0000. |
| 80A2 | The addressed DP slave does not return an acknowledgment. (This error information is not available with PROFINET IO devices. The process is not time-monitored by PROFINET.) |
| 80A3 | The DP master/PROFINET IO controller concerned does not support this function. |
| 80A4 | The CPU does not support this function for external DP masters/PROFINET IO controller. |
| 80A6 | Slot error in the DP slave/PROFINET IO device; not all user data can be accessed (this error code is only available when MODE=1).  Note: "D_ACT_DP" returns this error information only if the activated component fails again after parameter assignment and before the end of "D_ACT_DP". If only a single module is unavailable, "D_ACT_DP" returns the error information W#16#0000. |
| 80C1 | D_ACT_DP" was started and will continue with another logical address (this error code is only possible when MODE=1 and MODE=2). |
| 80C3 | - Temporary resource error: The CPU is currently processing the maximum possible number of activation/deactivation jobs. (This error code is only possible when MODE = 1 and MODE = 2.) - The CPU is busy receiving a modified configuration. Currently you can not enable/disable DP slaves/PROFINET IO devices. |
| 80C5 | DP: Jobs not collected by the user are discarded at restart. |
| 80C6 | PROFINET: Jobs not collected by the user are discarded at restart. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### Application

If you configure DP slaves/PROFINET IO devices in a CPU which are not actually present or not currently required, the CPU will nevertheless continue to access these DP slaves/PROFINET IO devices at regular intervals. After the slaves are deactivated, further CPU accessing will stop. With PROFIBUS DP, the fastest possible DP bus cycle can be achieved in this manner and the corresponding error events no longer occur.

#### Examples

From a machine OEM's point of view, there are numerous device options possible in series production of machines. However, each delivered machine includes only one combination of selected options.

Every one of these possible machine options is configured as a DP slave/PROFINET IO device by the manufacturer in order to create and maintain a common user program having all possible options. Use "D_ACT_DP" to deactivate all DP slaves/PROFINET IO devices not present at machine startup.

A similar situation exists for machine tools having numerous tooling options available but actually using only a few of them at any given time. These tools are implemented as DP slaves/PROFINET IO devices. With "D_ACT_DP", the user program activates the tools currently needed and deactivates those required later.

#### Functional description

"D_ACT_DP" is an instruction that works asynchronously, which means its execution extends over multiple calls. You start the job by calling D_ACT_DP with REQ = 1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

#### Identification of a job

If you have started a deactivation or activation job and you call "D_ACT_DP" again before the job is complete, the behavior of the instruction depends on whether or not the new call involves the same job: If the input parameter LADDR matches, then the call will be interpreted as a follow-on call.

#### Deactivating DP slaves/PROFINET IO devices

When you deactivate a DP slave/PROFINET IO device with "D_ACT_DP", its process outputs are set to the configured substitute values or to 0 (safe state). The assigned DP master/PROFINET IO controller does not continue to address this component. Deactivated DP slaves/PROFINET IO devices are not identified as faulty or missing by the error LEDs on the DP master/PROFINET IO controller or CPU.

The process image of the inputs of deactivated DP slaves/PROFINET IO devices is updated with 0, that is, it is handled just as it is for failed DP slaves/PROFINET IO devices.

If you are using your program to directly access the user data of a previously deactivated DP slave/PROFINET IO device, the I/O access error OB (OB 122) is called, and the corresponding start event is entered in the diagnostics buffer. If you attempt to access a deactivated DP slave/PROFINET IO device via an instruction (such as "[RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400)"), you will receive the same error information in RET_VAL as for an unavailable DP slave/PROFINET IO device.

Deactivating a DP slave/PROFINET IO device does not start the program error OB (OB 85), even if its inputs or outputs belong to the system-side process image to be updated. Also there is no entry in the diagnostics buffer.

Whether the deactivation of a DP slave/PROFINET IO device leads to a start of the rack failure OB (OB 86) and an entry in the diagnostics buffer, depends on the MODE parameter:

- MODE = 2: No OB 86 start and no diagnostics buffer entry
- MODE = 4: OB 86 start and diagnostics buffer entry

If a DP station/PNIO station fails after you have deactivated it with "D_ACT_DP", the operating system does not detect the failure. As a result, there is no subsequent start of OB 86 or diagnostics buffer entry.

Applies to PROFIBUS DP: If you wish to deactivate DP slaves functioning as transmitters in slave-to-slave communication, we recommend that you first deactivate the receivers (listeners) that detect which input data the transmitter is transferring to its DP master. Deactivate the transmitter only after you have performed this step.

#### Activating DP slaves/PROFINET IO devices

When you reactivate a DP slave/PROFINET IO device with "D_ACT_DP", this component is configured and assigned parameters by the associated DP master/PROFINET IO controller (as with the return of a failed DP station/PROFINET IO station). This activation is complete when the component is able to transfer user data.

Activating a DP slave/PROFINET IO device does not start the program execution error OB (OB 85), even if its inputs or outputs belong to the system-side process image to be updated. Also there is no entry in the diagnostics buffer.

Whether the deactivation of a DP slave/PROFINET IO device leads to a start of the rack failure OB (OB 86) and an entry in the diagnostics buffer, depends on the MODE parameter:

- MODE = 1: No OB 86 start and no diagnostics buffer entry
- MODE = 3: OB 86 start and diagnostics buffer entry

If you attempt to use "D_ACT_DP" to activate a DP slave that has been deactivated and is physically separated from the DP bus, the instruction will return the error code W#16#80A2 after approximately one minute and the DP slave will remain deactivated. If the slave is reconnected to the DP bus at a later time, it must be reactivated with "D_ACT_DP".

If you attempt to activate a PROFINET IO device that is physically separated from the PROFINET bus, "D_ACT_DP" will remain active. There is no automatic cancellation after a specific period as with DP slaves. You need to manually cancel the running job.

> **Note**
>
> Activating a DP slave/PROFINET IO device may be time-consuming. If you want to cancel a currently running activation job, start "D_ACT_DP" with the same value for LADDR and MODE =2. You repeat the call for "D_ACT_DP" with MODE = 2 until the successful cancellation of the activation job is displayed with RET_VAL =0.

If you wish to activate DP slaves which take part in the slave-to-slave communication, we recommend that you first activate the transmitters and then the receivers (listeners).

#### CPU startup

Depending on the startup mode, the CPU operating system behaves as follows regarding DP slaves/PROFINET IO devices:

- During cold and warm restarts, slaves/devices are activated automatically.

  - With S7-400: Activation of the DP slaves/PROFINET IO devices may take some time. In this case, the CPU continues to run and I/O access errors occur until the activation is complete. The reaction of the CPU depends on the configuration (OB 85 call for I/O access errors) and the program in OB 85. You cannot suppress these I/O access errors.
  - For S7-300: Activation of the DP slaves/PROFINET IO devices may take some time. In this case, the CPU waits until the DP slaves / PROFINET IO devices are activated. The maximum waiting period for activation of the DP slaves / PROFINET IO devices is approx. 1 minute. No I/O access errors occur during this time.
- During a hot restart, the activation status of slaves/devices remains unchanged: Activated slaves/devices remain activated, deactivated slaves/devices remain deactivated.

After the CPU start-up, the CPU cyclically attempts to contact all configured and not deactivated slaves/devices that are either not present or not responding.

> **Note**
>
> A call of "D_ACT_DP" in startup OBs is not supported.

### Additional instructions (S7-300, S7-400)

This section contains information on the following topics:

- [RD_REC: Read data record from I/O (S7-300, S7-400)](#rd_rec-read-data-record-from-io-s7-300-s7-400)
- [WR_REC: Write data record to I/O (S7-300, S7-400)](#wr_rec-write-data-record-to-io-s7-300-s7-400)
- [DPRD_DAT: Read consistent data of a DP standard slave (S7-300, S7-400)](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)
- [DPWR_DAT: Write consistent data of a DP standard slave (S7-300, S7-400)](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)
- [I-device / I-slave (S7-300, S7-400)](#i-device-i-slave-s7-300-s7-400)
- [PROFIBUS (S7-300, S7-400)](#profibus-s7-300-s7-400)
- [ASi (S7-300, S7-400)](#asi-s7-300-s7-400)

#### RD_REC: Read data record from I/O (S7-300, S7-400)

##### Description

Use the instruction to read the data record with the number RECNUM from the addressed module. You start the read process by assigning the value "1" to the input parameter REQ during the call. If the read process could be executed immediately, the instruction returns the value "0" at the output parameter BUSY . If BUSY has the value "1", reading is not yet complete.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400). The data record read is entered in the destination area spanned by the RECORD parameter, providing the data transfer was free of errors.

> **Note**
>
> When you read out a data record with a number greater than one from an FM or a CP you have purchased prior to February 1997 (below referred to as "old modules"), "RD_REC" responds differently than it does in new modules. This special situation is covered in the section "Using old S7-300 FMs and CPs with data record numbers &gt;1" (see below).
>
> If a DPV1 slave is configured via GSD file (GSD rev. 3 and higher) and the DP interface of the DP master is set to "S7 compatible", then you may not read any data records from the I/O modules in the user program with "RD_REC". In this case, the DP master addresses the wrong slot (configured slot + 3).
>
> Remedy: Set the interface of the DP master to "DPV1".

##### Parameter

The following table shows the parameters of the instruction "RD_REC":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Read request |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed  module, you will have to specify the area identifier of the lower address. If  the addresses are identical, you will have to specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical address of the module. For  a mixed module, the lower of the two  addresses must be specified. |
| RECNUM | Input | BYTE | I, Q, M, D, L or constant | Data record number (permitted values: 0 to 240) |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. In addition: the length of the data record actually transferred in bytes (possible values: +1 to +240), if the destination area is greater than the transferred data record and if no error occurred during the transfer. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The reading process is not yet complete. |
| RECORD | Output | ANY | I, Q, M, D, L | Destination area for the data record read. With asynchronous execution of "RD_REC",  make sure that the actual parameters of RECORD have the same length information  for all calls. Only the BYTE data type is permitted.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RECORD

> **Note**
>
> If you want to ensure that the entire data record is always read, select a destination area with a length of 241 bytes. If the data transfer is error-free, RET_VAL contains the actual data record length.

##### Using old S7-300 FMs and CPs with data record numbers &gt; 1

If you want to use the instruction "RD_REC" to read out a data record with a number greater than one from an old S7-300 FM or old S7-300 CP, remember the following points:

- If the destination area is greater than the actual length of the required data record, no data are entered in RECORD . RET_VAL is written with W#16#80B1.
- If the destination area is smaller than the actual length of the required data record, the CPU reads as many bytes beginning at the start of the record as are specified in the length information of RECORD and enters this number of bytes inRECORD . RET_VAL has the value "0".
- If the length specified in RECORD is the same as the actual length of the required data record, the CPU reads the data record and enters it in RECORD . RET_VAL is written with "0".

##### Parameter RET_VAL

- If an error has occurred while the function was being executed, the return value contains an error code.
- If no error occurred during the transfer, RET_VAL contains the following:

  - 0, if the entire destination area was filled with data from the selected data record (the data record can also be incomplete).
  - The length of the data record actually transferred in bytes (possible values: +1 to +240) if the destination area is greater than the transferred data record.

    > **Note**
    >
    > If the general error W#16#8745 occurs, this only indicates that access to at least one byte of the process image was blocked. The data record was read by the module correctly and written to the I/O memory area.

When looking at the "real" error information (error codes W#16#8xyz) in the following table, we distinguish between two cases:

- Temporary errors (error codes W#16#80A2 to 80A4, 80Cx):

  This type of error can possibly be eliminated without user action, meaning it is helpful to call the instruction again (multiple calls, if necessary).

  Example of a temporary error: Resources required are currently in use (W#16#80C3).
- Permanent errors (error codes W#16#809x, 80A0, 80A1, 80Bx):

  This type of error does not correct itself. A new call of the instruction will not be successful until you have eliminated the error. Example of a permanent error: Wrong length specification in RECORD (W#16#80B1).

  > **Note**
  >
  > If you transfer data records to a DPV1 slave with "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)" or if you read data records from a DPV1 slave with RD_REC and if this DPV1 slave operates in DPV1 mode, the DP master evaluates the error information it received from the slave as follows:
  >
  > If the error information lies within the range from W#16#8000 to W#16#80FF or W#16#F000 to W#16#FFFF, the DP master passes the error information to the instruction. If the error information is outside this range, the DP master passes the value W#16#80A2 to the instruction and suspends the slave.
  >
  > For a description of the error information originating from DPV1 slaves, refer to STATUS[3] [Parameter STATUS](#parameter-status-s7-300-s7-400).

##### Parameter RET_VAL for WR_REC and RD_REC

| Error code  (W#16#...) | Explanation | Restriction |
| --- | --- | --- |
| 0000 | No error | - |
| 7000 | First call with REQ=0: No data transfer active; BUSY has the value 0. | - |
| 7001 | First call with REQ=1: Data transfer started; BUSY has the value 1. | Distributed I/O |
| 7002 | Intermediate call (REQ  irrelevant): Data transfer already active; BUSY has the value 1. | Distributed I/O |
| 8090 | Specified logical base address invalid: There is no  assignment in SDB1/SDB2x or there is no base address. | - |
| 8092 | A type other than BYTE is specified in the ANY reference. | For S7-400 only |
| 8093 | This instruction is not permitted for the module specified by LADDR and IOID . (permitted are S7-300 modules for an S7-300, S7-400 modules for an  S7-400, S7-DP modules for an S7-300 and S7-400). | - |
| 80A0 | Negative acknowledgement when reading from the module: Module was removed during the reading process or is defective | With "RD_REC" only |
| 80A1 | Negative acknowledgement when writing to the module: Module was removed during the writing process or is  defective | With "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)" only |
| 80A2 | - DP protocol error at layer 2 (for example, slave failure or bus problems) - For ET200S, data record cannot be read in DPV0 mode. | Distributed I/O |
| 80A3 | DP protocol error with user interface/user | Distributed I/O |
| 80A4 | Communication on the communication bus disrupted | Error occurs between  the CPU and the external DP  interface module. |
| 80B0 | - Instruction not possible for module type. - The module does not recognize the data record. - Data record number 241 not permitted. - With "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)", data records 0 and 1 are not  permitted. | - |
| 80B1 | The length specified in parameter RECORD is incorrect. | - With "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)": Length incorrect - With "RD_REC"  (only when using old  S7-300 FMs and S7-300  CPs): specified length &gt; data record length - With DPNRM_DG: specified length &gt; record length |
| 80B2 | The configured slot is  not occupied. | - |
| 80B3 | Actual module type does not match the specified module  type in SDB1. | - |
| 80B7 | DP slave or module reports an invalid range for a parameter or value. | With "RD_REC" only |
| 80C0 | With "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)": the data can only be written when the CPU is in STOP mode. Note: this means that writing by the user program is not possible. You can only write the data online with PG/PC.  With "RD_REC": the module routes the data record, but either no data is present or the data can only be read when the CPU is in STOP mode. Note: if data can only be read when the CPU is in STOP mode, then an evaluation by the user program is not possible. In this case, you can only read the data online with PG/PC.  With "[DPNRM_DG](#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)": There are no diagnostics data available. | With "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)" or "RD_REC" or "[DPNRM_DG](#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)" |
| 80C1 | The data of the previous write job on the module for the same data record have not yet been processed by the module. | - |
| 80C2 | The module is currently processing the maximum possible  number of jobs for a CPU. | - |
| 80C3 | The required resources (memory, etc.) are currently  occupied. | - |
| 80C4 | Internal temporary error. Job could not be carried out.  Repeat the job. If this error occurs often, check your installation for sources of electrical interference. | - |
| 80C5 | Distributed I/O not available. | Distributed I/O |
| 80C6 | Data record transfer stopped due to priority class abort (restart or background) | Distributed I/O |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) | - |

#### WR_REC: Write data record to I/O (S7-300, S7-400)

##### Description

Use the instruction "WR_REC" to transfer the data record RECORD to the addressed module.

You start the writing process by assigning the value "1" to the input parameter REQ during the call. If the writing process could be executed immediately, the instruction returns the value "0" at the output parameter BUSY. If BUSY has the value "1", writing is not yet complete.

> **Note**
>
> If a DPV1 slave is configured via GSD file (GSD rev. 3 and higher) and the DP interface of the DP master is set to "S7 compatible", then you may not write any data records from the I/O modules to the user program with "WR_REC". In this case, the DP master addresses the wrong slot (configured slot + 3).
>
> Remedy: set the interface of the DP master to "DPV1".

##### Parameters

The following table shows the parameters of the instruction "WR_REC":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Write request |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed  module, you will have to specify the area identifier of the lower address. If  the addresses are identical, you will have to specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical address of the module. For  a mixed module, the lower of the two  addresses must be specified. |
| RECNUM | Input | BYTE | I, Q, M, D, L or constant | Data record number (permitted values: 2 to 240) |
| RECORD | Input | ANY | I, Q, M, D, L | Data record. Only the BYTE data type is permitted.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| RET_VAL | Output | Return | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY= 1: The writing process is not yet complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RECORD

The data to be transferred are read from the RECORD parameter during the first call. If the transfer of the data record takes longer than the duration of one call, the contents of the RECORD parameter are no longer relevant for the subsequent instruction calls (for the same job).

##### Parameter RET_VAL

See also: [RD_REC: Read data record from I/O](#rd_rec-read-data-record-from-io-s7-300-s7-400)

> **Note**
>
> If the general error W#16#8544 occurs, it only indicates that access to at least one byte of the I/O memory area containing the data record was denied. The data transfer was continued.

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

#### DPRD_DAT: Read consistent data of a DP standard slave (S7-300, S7-400)

##### Description

You use the instruction "DPRD_DAT" to consistently read data of a DP standard slave/PROFINET IO device; the maximum length is as follows:

- See the documentation supplied with your CPU for the maximum length.
- If there was no error during the data transmission, the data that have been read are entered in the destination area indicated by RECORD.

The destination area must have the same length that you configured for the selected module. If you read from a DP standard slave with a modular configuration or with several DP identifiers, you can only access the data of one module/DP identifier at the configured start address per "DPRD_DAT" call.

> **Note**
>
> CPUs of the S7-300/400 product range support up to 64 bytes of consistent data. Use instruction "DPRD_DAT" to handle consistent data ranges that exceed 4 bytes. However, you may also use this instruction for a data range of 1 byte. Access errors trigger the output of error code W#16#8090.

> **Note**
>
> **S7-400 CPUs as of firmware version V6.0**
>
> For S7-400 CPUs as of firmware version V6.0, the call of DPRD_DAT is generally accepted for all addresses. This means you can use DPRD_DAT to access addresses for which you have not configured overall consistency.

##### Parameter

The following table shows the parameters of the instruction "DPRD_DAT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Configured start address from the I-area  of the module from which the data will be  read.  Note: The address must be specified in hexadecimal form. For example, start address 100 means: LADDR:=W#16#64. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| RECORD | Output | ANY | I, Q, M, D, L | Destination area for the user data that were read. It must be precisely as long as you have configured for the selected module. Only the BYTE data type is permitted.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

> **Note**
>
> If you access DPV1 slaves, error information of these slaves can be forwarded from the DP master to the instruction. For a description of this error information, refer to STATUS[3] [Parameter STATUS](#parameter-status-s7-300-s7-400).

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | - You have not configured a module for the specified logical base address. - You have ignored the restriction concerning the length of consistent data. (For S7-400 CPUs only up to and including firmware version V5.3; this cause becomes obsolete as of firmware version V6.0.) - You have not entered the start address in the LADDR parameter in hexadecimal format. |
| 8092 | A type other than BYTE is specified in the ANY reference. |
| 8093 | No DP module/PROFINET IO device from which you can read consistent data exists at the logical address specified in LADDR. |
| 80A0 | Access error detected while I/O devices were being accessed. |
| 80B0 | - For S7-300 CPUs (all firmware versions) and S7-400 CPUs up to and including firmware version V5.3: Slave failure on external DP interface module. - For S7-400 CPUs as of firmware version V6.0: Slave failure or access error to non-consistent data at external DP connection (CP also signals to CPU that an error has occurred.) |
| 80B1 | The length of the specified destination area is not identical to the configured user data  length. |
| 80B2 | System error with external DP interface module. |
| 80B3 | System error with external DP interface module. |
| 80C0 | The data haven't yet been read by the module. |
| 80C2 | System error with external DP interface module. |
| 80Fx | System error with external DP interface module. |
| 87xy | System error with external DP interface module. |
| 808x | System error with external DP interface module. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### Application

You require "DPRD_DAT" because you can only read out a maximum of four continuous bytes using the load commands that access the I/O or the process image input table.

> **Note**
>
> If required, you can also read consistent data via the process image of the inputs.
>
> - See the associated documentation to determine whether your S7-300 CPU handles this functionality.
> - All S7-400 CPUs handle this functionality.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **I/O access**  When using "DPRD_DAT", avoid accessing I/O areas that have process image partitions with OB6x connections (isochronous mode interrupts) assigned to them. |  |

##### Data consistency

See also: Section [Data consistency](S7%20communication%20%28S7-300%2C%20S7-400%29.md#data-consistency-s7-300-s7-400).

#### DPWR_DAT: Write consistent data of a DP standard slave (S7-300, S7-400)

##### Description

Use the instruction to consistently transfer the data in RECORD to the addressed DP standard slave/PROFINET IO device, and, if necessary, to the process image (if you have configured the relevant address area of the DP standard slave as a consistent range in a process image).

The following applies for the maximum length of the data that will be transferred: See the documentation supplied with your CPU for the maximum length. The data is transferred synchronously, that is, the write process is completed when the instruction is completed.

The source area must have the same length that you have configured for the selected module. If the DP standard slave has a modular design, you can only access one module of the DP slave.

> **Note**
>
> CPUs of the S7-1200/1500 product range support up to 64 bytes of consistent data. Use instruction "DPWR_DAT" to write consistent data ranges that exceed 4 bytes to a submodule or device. However, you may also use this instruction for a data range of 1 byte. Access errors trigger the output of error code W#16#8090.

> **Note**
>
> **S7-400 CPUs as of firmware version V6.0**
>
> For S7-400 CPUs as of firmware version V6.0, the call of DPWR_DAT is generally accepted for all addresses. This means you can use DPWR_DAT to access addresses for which you have not configured overall consistency.

##### Parameter

The following table shows the parameters of the instruction "DPWR_DAT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Configured start address from the PIQ area of the module to which the data is written.  Note: The address must be specified in hexadecimal form. For example, start address 100 means: LADDR:=W#16#64. |
| RECORD | Input | ANY | I, Q, M, D, L | Source area for the user data to be  written. It must be precisely as long as you have configured for the selected module. Only the BYTE data type is permitted.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |

For more information about the valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

> **Note**
>
> If you access DPV1 slaves, error information of these slaves can be forwarded from the DP master to the instruction. A description of this error information is available in STATUS[3] [Parameter STATUS](#parameter-status-s7-300-s7-400).

| Error code (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 808x | System error with external DP interface module. |
| 8090 | - You have not configured a module for the specified logical base address. - You have ignored the restriction concerning the length of consistent data. (For S7-400 CPUs only up to and including firmware version V5.3; this cause becomes obsolete as of firmware version V6.0.) - You have not entered the start address in the LADDR parameter in hexadecimal format. |
| 8092 | A type other than BYTE is specified in the ANY reference. |
| 8093 | No DP module/PROFINET IO device to which you can write consistent data exists at the logical address specified in LADDR. |
| 80A1 | Access error detected while I/O devices were being accessed. |
| 80B0 | - For S7-300 CPUs (all firmware versions) and S7-400 CPUs up to and including firmware version V5.3: Slave failure on external DP interface module. - For S7-400 CPUs as of firmware version V6.0: Slave failure or access error to non-consistent data at external DP connection (CP also signals to CPU that an error has occurred.) |
| 80B1 | The length of the specified destination area is not identical to the configured user data  length. |
| 80B2 | System error with external DP interface module. |
| 80B3 | System error with external DP interface module. |
| 80C1 | The data of the previous write job on the module have not yet been processed  by the module. |
| 80C2 | System error with external DP interface module. |
| 80Fx | System error with external DP interface module. |
| 85xy | System error with external DP interface module. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### Application

You require the instruction "DPWR_DAT" because you can only write a maximum of four continuous bytes using the transfer commands that access the I/O or the process image output table.

> **Note**
>
> If required, you can also read consistent data via the process image of the inputs.   
> See the associated documentation to determine whether your S7-300 CPU handles this functionality,
>
> - All S7-400 CPUs handle this functionality.
> - Do not use both possibilities concurrently when writing consistent data: Either use "DPWR_DAT" or write via the process image output table.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **I/O access**  When using "DPWR_DAT", avoid accessing I/O areas that have process image partitions with OB6x connections (isochronous mode interrupts) assigned to them. |  |

##### Data consistency

See also: [Data consistency](S7%20communication%20%28S7-300%2C%20S7-400%29.md#data-consistency-s7-300-s7-400).

#### I-device / I-slave (S7-300, S7-400)

This section contains information on the following topics:

- [RCVREC: Receive data record (S7-300, S7-400)](#rcvrec-receive-data-record-s7-300-s7-400)
- [PRVREC: Make data record available (S7-300, S7-400)](#prvrec-make-data-record-available-s7-300-s7-400)
- [SALRM: Send interrupt (S7-300, S7-400)](#salrm-send-interrupt-s7-300-s7-400)

##### RCVREC: Receive data record (S7-300, S7-400)

###### Description

An I-device can receive a data record from a superordinate controller. The receipt takes place in the user program with the instruction "RCVREC" (receive record).

The instruction has the following operating modes:

- Check whether the I-device has a request for a data record receipt.
- Make the data record available to the output parameters.
- Send an answer to the superordinate controller.

You can determine the operating mode executed by the instruction using the input parameter MODE (see below).

The I-device must be in the operating mode RUN or STARTUP.

With MLEN, you specify the maximum number of bytes you want to receive. The selected length of the destination area RECORD should have at least the length of MLEN bytes.

If a data record was received (MODE=1 or MODE=2), the output parameter NEW will indicate that the data record was stored in RECORD. Note that RECORD has a sufficient length. The output parameter LEN contains the actual length of the data record received in bytes.

Set CODE1 and CODE2 to zero for the positive answer to the superordinate controller. If the received data record is to be rejected, enter the negative answer to the superordinate controller in Error Code 1 of the CODE1 and in Error Code 2 of the CODE2.

> **Note**
>
> If the I-device has received a request for a data record receipt, you must recognize the delivery of this request within a certain duration. After recognition, you must send an answer to the superordinate controller within this time period. Otherwise the I-device will experience a timeout error which causes the operating system of the I-device to send a negative answer to the superordinate controller. For information on the value for the time period, please refer to the specifications of your CPU.

The output parameter STATUS receives the error information after the occurrence of an error.

###### Operating modes

You can determine the operating mode of the instruction "RCVREC" with the input parameter MODE. This step will be explained in the following table.

| MODE | Meaning |
| --- | --- |
| 0 | Check whether a request for a data record receipt exists  If a data record from a superordinate controller exists on the I-device, the instruction will only write the output parameters NEW, SLOT, INDEX and LEN. If you call the instruction several times with MODE=0, then the output parameter will only refer to one and the same request. |
| 1 | Receiving a data record for any subslot of the I-device  If a data record from a superordinate controller exists on the I-device for any subslot of the I-device, the instruction will write the output parameter and transfer the data record to the parameter RECORD. |
| 2 | Receiving a data record for a specific subslot of the I-device  If a data record from a superordinate controller exists on the I-device for a specific subslot of the I-device, the instruction will write the output parameter and transfer the data record to the parameter RECORD. |
| 3 | Sending a positive answer to the superordinate controller  The instruction checks the request of the superordinate controller to receive a data record, accepts the existing data record and sends a positive acknowledgement to the superordinate controller. |
| 4 | Sending a negative answer to the superordinate controller  The instruction checks the request of the superordinate controller to receive a data record, rejects the existing data record and sends a negative acknowledgement to the superordinate controller. Enter the reason for the rejection in the input parameters CODE1 and CODE2. |
|  |  |

> **Note**
>
> After the receipt of a data record (NEW=1) you must call "RCVREC" twice to ensure complete processing. You must do this in the following order:
>
> - First call with MODE=1 or MODE=2
> - Second call with MODE=3 or MODE=4

###### Parameter

The following table shows the parameters of the instruction "RCVREC":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | INT | I, Q, M, D, L or constant | Mode |
| F_ID | Input | DWORD | I, Q, M, D, L or constant | Subslot in the transfer area of the I-device for the data record to be received (only relevant for MODE=2). The high word is always set to zero. |
| MLEN | Input | INT | I, Q, M, D, L or constant | Maximum length of the data record to be received in bytes |
| CODE1 | Input | BYTE | I, Q, M, D, L or constant | Zero (for MODE=3) and/or Error Code 1 (for MODE=4) |
| CODE2 | Input | BYTE | I, Q, M, D, L or constant | Zero (for MODE=3) and/or Error Code 2 (forMODE=4) |
| NEW | Output | BOOL | I, Q, M, D, L | - MODE=0: New data record was received - MODE=1 or 2: Data record was transferred to RECORD |
| STATUS | Output | DWORD | I, Q, M, D, L | Error information |
| SLOT | Output | INT | I, Q, M, D, L | Identical to F_ID |
| SUBSLOT | Output | INT | I, Q, M, D, L | Identical to F_ID |
| INDEX | Output | INT | I, Q, M, D, L | Number of the data record received |
| LEN | Output | INT | I, Q, M, D, L | Length of the data record received |
| RECORD | InOut | ANY | I, Q, M, D, L | Destination area for the data record received.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 Byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and results in an error message in the user program. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter STATUS

For information about the interpretation of parameter STATUS, refer to section: [Parameter STATUS](#parameter-status-s7-300-s7-400)

##### PRVREC: Make data record available (S7-300, S7-400)

###### Description

An I-device can receive a request from a superordinate controller to make a data record available. The I-device makes the data record available in the user program with the instruction "PRVREC" (provide record).

The instruction has the following operating modes:

- Check whether the I-device has a request for making a data record available.
- Transfer the requested data record to the superordinate controller.
- Sending an answer to the superordinate controller.

You can determine the operating mode executed by the instruction using the input parameter MODE(see below).

The I-device must be in the operating mode RUN or STARTUP.

Enter the maximum number of bytes the data record to be sent should have with LEN. The selected length of the destination area RECORD should have at least the length of LEN bytes.

If a request to make a data record available exists, (MODE=0), the output parameter NEW will be set to TRUE.

If the request for making a data record available is accepted, write RECORD for the positive answer to the superordinate controller with the requested data record and write zero for CODE1 and CODE2. If the request for making a data record available is to be rejected, enter the negative answer to the superordinate controller in Error Code 1 of the CODE1 and in Error Code 2 of theCODE2.

> **Note**
>
> If the I-device has received a request for making a data record available, you must recognize the delivery of this request within a certain time period. After recognition, you must send an answer to the superordinate controller within this time period. Otherwise the I-device will experience a timeout error which causes the operating system of the I-device to send a negative answer to the superordinate controller. For information on the value for the time period, please refer to the specifications of your CPU.

The output parameter STATUS receives the error information after the occurrence of an error.

###### Operating modes

You can determine the operating mode of the instruction "PRVREC" with the input parameter MODE. This step will be explained in the following table.

| MODE | Meaning |
| --- | --- |
| 0 | Check whether a request for making a data record available exists  If a request from a superordinate controller for making a data record available exists on the I-device, the instruction will only write the output parameters NEW, SLOT, INDEX and RLEN. If you call the instruction several times with MODE=0, then the output parameter will only refer to one and the same request. |
| 1 | Receiving a request for making a data record available for any subslot of the I-device  If such a request from a superordinate controller for any subslot of the I-device exists on the I-device, the instruction will write the output parameter. |
| 2 | Receiving a request for making a data record available for a specific subslot of the I-device  If such a request from a superordinate controller for a specific subslot of the I-device exists on the I-device, the instruction will write the output parameter. |
| 3 | Make the data record available and send a positive answer to the superordinate controller  The instruction checks the request of the superordinate controller to make a data record available, makes the request data record available to RECORD and sends a positive acknowledgement to the superordinate controller. |
| 4 | Sending a negative answer to the superordinate controller  The instruction checks the request of the superordinate controller to make a data record available, rejects this request and sends a negative acknowledgement to the superordinate controller. Enter the reason for the rejection in the input parameters CODE1 and CODE2. |

> **Note**
>
> After the receipt of a request (NEW=1) you must call the instruction twice to ensure complete processing. You must do this in the following order:
>
> - First call with MODE=1 or MODE=2
> - Second call with MODE=3 or MODE=4

###### Parameter

The following table shows the parameters of the instruction "PRVREC":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | INT | I, Q, M, D, L or constant | Mode |
| F_ID | Input | DWORD | I, Q, M, D, L or constant | Subslot in the transfer area of the I-device for the data record to be sent (only relevant for MODE=2). The high word is always set to zero. |
| CODE1 | Input | BYTE | I, Q, M, D, L or constant | Zero (for MODE=3) and/or Error Code 1 (forMODE=4) |
| CODE2 | Input | BYTE | I, Q, M, D, L or constant | Zero (for MODE=3) and/or Error Code 2 (forMODE=4) |
| LEN | Input | INT | I, Q, M, D, L or constant | Maximum length of the data record to be sent in bytes |
| NEW | Output | BOOL | I, Q, M, D, L | The new data record was requested by the superordinate controller. |
| STATUS | Output | DWORD | I, Q, M, D, L | Error information |
| SLOT | Output | INT | I, Q, M, D, L | Identical to F_ID |
| SUBSLOT | Output | INT | I, Q, M, D, L | Identical to F_ID |
| INDEX | Output | INT | I, Q, M, D, L | Number of the data record to be sent |
| RLEN | Output | INT | I, Q, M, D, L | Length of the data record to be sent |
| RECORD | InOut | ANY | I, Q, M, D, L | Data record made available  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 Byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and results in an error message in the user program. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter STATUS

For information about the interpretation of parameter STATUS, refer to section: [Parameter STATUS](#parameter-status-s7-300-s7-400)

##### SALRM: Send interrupt (S7-300, S7-400)

This section contains information on the following topics:

- [Description SALRM (S7-300, S7-400)](#description-salrm-s7-300-s7-400)
- [Parameter ATYPE (S7-300, S7-400)](#parameter-atype-s7-300-s7-400)
- [Parameter ASPEC (S7-300, S7-400)](#parameter-aspec-s7-300-s7-400)
- [Parameter LEN (S7-300, S7-400)](#parameter-len-s7-300-s7-400)
- [Parameters STATUS and ERROR (S7-300, S7-400)](#parameters-status-and-error-s7-300-s7-400)
- [Parameter AINFO (S7-300, S7-400)](#parameter-ainfo-s7-300-s7-400-1)

###### Description SALRM (S7-300, S7-400)

###### Description

You use the instruction to send an interrupt of a slot in the transition area (virtual slot) from the user program of an intelligent slave to the associated DP master. This starts the associated OB in the DP master.

You can send additional interrupt-specific information along with the interrupt. You can use the instruction to read all additional information in the DP master.

The instruction can only be used in S7-compatible mode.

- DP: The master uses a GSD file to integrate the I-slave.
- S7-compatible: The I-slave is connected to a master during configuration.

  > **Note**
  >
  > The interface of the "SALRM" instruction is identical to that in the "SALRM" FB defined in the standard "PROFIBUS and PROFINET Guideline Communication Function Blocks on PROFIBUS DP and PROFINET IO".

###### Functional description

The "SALRM" instruction works asynchronously, that is, its execution extends over multiple calls. You start the interrupt transfer by calling the instruction with REQ = 1.

The sending process remains active until interrupt processing is either acknowledged or canceled by the DP master.

The output parameter BUSY and bytes 2 and 3 of the output parameter STATUS show the status of the job. Bytes 2 and 3 of STATUS match the output parameter RET_VAL of the instructions that operate asynchronously.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

The transfer of the interrupt is complete when the output parameter BUSY has the value FALSE .

###### Identification of the job

When you initiate the transfer of an interrupt to the DP master with the instruction "SALRM" and then call this instruction once again before the current job has been completed, the further response of this instruction will depend on whether or not the new call involves the same job.

If the ID and ATYPE parameters match a still unfinished job, the new call is regarded as a follow-on call.

###### Parameters

The following table shows the parameters of the "SALRM" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Transfer the interrupt |
| ID | Input | DWORD | I, Q, M, D, L or constant | Any logical address of the transition area to the DP master (virtual slots), as viewed from the DP slave, except the diagnostics address of the station and the logical address of slot 2.  The relevant information is found in the low word. Enter zero in the high word. Bit 15 contains the I/O ID: 0 = input address, 1 = output address. |
| [ATYPE](#parameter-atype-s7-300-s7-400) | Input | INT | I, Q, M, D, L or constant | Interrupt type  ID for the interrupt type. Possible values:  - 1: Diagnostics interrupt - 2: Process interrupt |
| [ASPEC](#parameter-aspec-s7-300-s7-400) | Input | INT | I, Q, M, D, L or constant | Interrupt specifier:  - 0: No further information - 1: Incoming event, faulty slot - 2: Outgoing event, slot no longer faulty - 3: Outgoing event, slot still faulty |
| [LEN](#parameter-len-s7-300-s7-400) | Input | INT | I, Q, M, D, L or constant | Length of additional interrupt information to be sent, in bytes  Highest value: 16 |
| DONE | Output | BOOL | I, Q, M, D, L | DONE=1: Interrupt was transferred |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: Interrupt transfer is not yet complete |
| [ERROR](#parameters-status-and-error-s7-300-s7-400) | Output | BOOL | I, Q, M, D, L | ERROR = 1: An error has occurred. |
| [STATUS](#parameters-status-and-error-s7-300-s7-400) | Output | DWORD | I, Q, M, D, L | Error information |
| [AINFO](#parameter-ainfo-s7-300-s7-400-1) | InOut | ANY | I, Q, M, D, L | Interrupt info  Source area for additional interrupt information  Note: Note that for S7-300 CPUs, the parameter AINFO always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Effect of the "SALRM" call on the module status information and the group error LED (SF)

Like every CPU, an intelligent slave has stored the properties of its slots in the module status information.

See also: [SZL-ID W#16#xy91 - module status information](#szl-id-w16xy91---module-status-information-s7-300-s7-400)

When you use "SALRM" to send a diagnostic interrupt, the operating system at the intelligent slave influences the slave-local module status information and the SF LED based on bit 0 in byte 0 in AINFO (this bit is added to the status information as "module faulty"). However, there is no diagnostics buffer entry made in the I-slave, and no diagnostics interrupt OB is started.

###### Consistency of module status information between DP master and I-slave

The following section presents different scenarios and discusses their effects on module status information:

- Station return (results in start of OB 86 in the DP master and in the I-slave)

  The module status information will be affected with I-slave and with S7 master ("module fault" will be reset). If, after a station return, there are faults at the I-slave from the point of view of the user, these must be reported to the DP master by means of an "SALRM" call.
- STOP-RUN transition of the DP master (results in start of OB 82 in the I-slave)

  The module status information on the I-slave remains unchanged. The DP master resets the "module fault" bit in the relevant module status information.  
  To ensure the consistency of module status information between the DP master and I-slave in S7-compatible mode, you must respond to the I-slave as follows:

  - For each error-free virtual slot, you use "SALRM" to send an outgoing diagnostics interrupt to the DP master.
  - For each faulty virtual slot, you use "SALRM" to send an incoming diagnostics interrupt to the DP master.
- STOP-RUN transition of the I-slave (results in start of OB 82 in the DP master)

  The module status information on the DP master remains unchanged and is reset on the I-slave ("module fault" will be reset).  
  To ensure the consistency of module status information between the DP master and I-slave, you must react to the I-slave as follows:

  - For each error-free virtual slot, you use "SALRM" to send an outgoing diagnostics interrupt to the DP master.
  - For each faulty virtual slot, you use "SALRM" to send an incoming diagnostics interrupt to the DP master.

    > **Note**
    >
    > Because "SALRM" functions asynchronously, the "SALRM" calls cannot be completed in the startup OBs. In other words, they must be run in the cyclical program until they are finished.
    >
    > All the above-mentioned differences between the module status information in the master and the I-slave can only occur at those slots that receive diagnostics interrupts by means of "SALRM". This means that the remedies discussed above only apply to such slots.

###### Parameter ATYPE (S7-300, S7-400)

###### Parameter ATYPE

For all permitted values of ATYPE , the following table shows which OB is started in the associated DP master and in which DP mode the given interrupt type is permitted.

| ATYPE | Meaning in DPV1 standard | Associated OB in the S7 DP master | DP mode |  |
| --- | --- | --- | --- | --- |
| DP | S7-compatible |  |  |  |
| 1 | Diagnostics interrupt | Diagnostics interrupt OB (OB82) | – | Yes |
| 2 | Process interrupt | Process interrupt OBs (OBs 40 to 47) | – | Yes |

> **Note**
>
> In addition to the information given in the table above, the extent to which interrupt types can be used can also be restricted by the DP master.

###### Dependency of the interrupt type on the operating mode of the S7 master

For a slave in S7-compatible mode (operated on an S7 master), hardware and diagnostics interrupts can only be sent when the associated DP master is in RUN mode (DP: Operate). If the DP master is in STOP mode (DP: Clear), the interrupt is not sent and "SALRM" provides the error information W#16#80C8. In this case, the user is responsible for sending the interrupt at a later time.

###### Parameter ASPEC (S7-300, S7-400)

###### Parameter ASPEC

According to the applicable standard, this parameter shows the diagnostics status of the virtual slot. For this reason, you can assign a value other than zero to ASPEC only when sending a diagnostics interrupt.

Because the additional S7 interrupt information for a diagnostics interrupt (data record 0) contains incoming/outgoing information (see Diagnostics data&gt;Main byte 0 bit 0), you must write bit 0 (module fault) in byte 0 of the additional interrupt information as follows:

| ASPEC | "Module fault" bit in [AINFO](#parameter-ainfo-s7-300-s7-400-1) |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 0 |
| 3 | 1 |

###### Parameter LEN (S7-300, S7-400)

###### Parameter LEN

In LEN, you specify in bytes the length of the additional interrupt information to be sent. The maximum permitted range of values is 0 to 16.

The following table shows the values LEN can have in the individual modes of an intelligent slave for all possible interrupt types.

| Interrupt type | DP | S7-compatible |
| --- | --- | --- |
| Diagnostics interrupt | – | 4 to 16 |
| Process interrupt | – | 4 |

The following table shows the response of "SALRM" when you assign LEN a value other than the length of [AINFO](#parameter-ainfo-s7-300-s7-400-1) in BYTE.

| Value of LEN | Characteristics of "SALRM" |
| --- | --- |
| &lt;= length specification of AINFO | "SALRM" sends an interrupt to the DP master. The number of bytes of additional interrupt information transmitted is as specified in LEN. |
| Outside the permitted range of values (&lt; 0 or &gt; 16) | "SALRM" does not send an interrupt. Error information: W#16#80B1, STATUS[4]=B#16#FF |
| &gt; Length specification of AINFO | "SALRM" sends an interrupt to the DP master. The amount of bytes of additional interrupt information transmitted is as specified in the length information of AINFO. Error information: W#16#00B1, STATUS[4]= length specification of AINFO |

###### Parameters STATUS and ERROR (S7-300, S7-400)

###### Parameters STATUS and ERROR

The STATUS output parameter contains error information. If it is interpreted as ARRAY[1 ... 4] OF BYTE, the error information has the following structure:

| Array element | Meaning |
| --- | --- |
| STATUS[1] | - B#16#00: No error - B#16#C0: Error detected by I-slave |
| STATUS[2], STATUS[3] | Corresponds to the output parameter RET_VAL of instructions |
| STATUS[4] | B#16#00 with the exception of some length conflicts between LEN and the length of [AINFO](#parameter-ainfo-s7-300-s7-400-1). These exceptions are shown in the next table. |

The following table indicates all specific error information of "SALRM".

| ERROR | STATUS[2,3]  (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Job was executed without errors. If LEN is &lt; length of AINFO, only LEN bytes of additional interrupt information were transmitted. |
| 0 | 00B1 | LEN &gt; length of AINFO. The job was completed. The additional interrupt information specified in AINFO was transmitted. STATUS[4] contains the length of AINFO. |
| 0 | 7000 | Initial call with REQ=0 (empty cycle). No interrupt was sent. BUSY has the value "0". |
| 0 | 7001 | Initial call with REQ=1. The job was initiated. BUSY has the value "1". |
| 0 | 7002 | Intermediate call (REQ irrelevant). The interrupt sent was not yet acknowledged by the DP master. BUSY has the value "1". |
| 1 | 8090 | The address specified in the ID is outside the permitted address range or was not configured. |
| 1 | 8091 | - You have disabled the interrupt in the configuration. - The interrupt is not permitted for this type of slave. |
| 1 | 8092 | Illegal data type in AINFO (BYTE and BLOCK-DB are permitted) |
| 1 | 8093 | ID belongs to a virtual slot from which an interrupt cannot be requested. |
| 1 | 80B0 | ASPEC  - Does not match bit 0 in byte 0 of AINFO - Must have a value of 0 for the interrupt type used - Is outside the permitted range of values |
| 1 | 80B1 | LEN Is outside the permitted range of values. STATUS[4] contains B#16#FF. |
| 1 | 80B5 | Call of "SALRM" in the DP master is not permitted. |
| 1 | 80C3 | The required resources (memory, etc.) are occupied at this time. |
| 1 | 80C5 | Distributed I/O device is not available at this time (e.g., station failure) |
| 1 | 80C8 | The function is not permitted in the current DP master operating mode (the DP master is an S7 master and is in STOP mode). |

###### Parameter AINFO (S7-300, S7-400)

###### Parameter AINFO

The AINFO parameter is the source area for additional interrupt information. As far as the intelligent slave is concerned, you can write any values to this area. However, if you are using a DP master of the S7 family, the additional information sent along with the interrupt must conform to S7 conventions.

If you send a **diagnostics interrupt** ([ATYPE](#parameter-atype-s7-300-s7-400) =1), then you are responsible for appropriate assignment of data record 0 and, if necessary, data record 1.

The following table shows you a recommendation for an S7-compatible assignment. In this case, the "module fault" bit (see above) was already set. Except for the indicated bit, this recommendation corresponds to the default assignment (the one existing after a POWER UP, after a STOP-RUN transition of the intelligent slave, or a station return).

| Data record no. | Assignment |
| --- | --- |
| 0 | B#16#01, 0B, 00, 00 |
| 1 | For S7-compatible mode: data record 0 + 12 bytes with zero |

###### Additional information

See also: [Structure of diagnostic data](#structure-of-diagnostic-data-s7-300-s7-400).

#### PROFIBUS (S7-300, S7-400)

This section contains information on the following topics:

- [DP_PRAL: Trigger hardware interrupt from DP standard slave (S7-300, S7-400)](#dp_pral-trigger-hardware-interrupt-from-dp-standard-slave-s7-300-s7-400)
- [DPSYC_FR: Synchronize DP slaves / Freeze inputs (S7-300, S7-400)](#dpsyc_fr-synchronize-dp-slaves-freeze-inputs-s7-300-s7-400)
- [DPNRM_DG: Read diagnostics data from a DP slave (S7-300, S7-400)](#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)
- [DP_TOPOL: Determine topology for DP master system (S7-300, S7-400)](#dp_topol-determine-topology-for-dp-master-system-s7-300-s7-400)

##### DP_PRAL: Trigger hardware interrupt from DP standard slave (S7-300, S7-400)

###### Description

Use the instruction to trigger a process interrupt on the associated DP master from the user program of an intelligent slave. This interrupt starts OB 40 on the DP master.

Using the input parameter AL_INFO , you can identify the cause of the process interrupt. This interrupt identifier is transferred to the DP master and you can evaluate the identifier in OB 40 (tag OB40_POINT_ADDR).

The requested process interrupt is uniquely specified by the input parameters IOID and LADDR . For each configured address area in the transfer memory, you can trigger exactly one process interrupt at any time.

###### Functional description

"DP_PRAL" works asynchronously, that is, its execution extends over multiple calls. You start the process interrupt request by calling "DP_PRAL" with REQ = 1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The job is complete when execution of OB 40 is complete on the DP master.

> **Note**
>
> If you operate the DP slave as a standard slave, the job is complete as soon as the diagnostics frame is obtained by the DP master.

###### Identification of a job

The input parameters IOID and LADDR uniquely specify the job.

If you have called the "DP_PRAL" instruction on a DP slave and you call this instruction again before the DP master has acknowledged the requested process interrupt, the way in which the instruction reacts depends on whether the new call involves the same job: If the parameters IOID and LADDR match a job that is not yet complete, the call is interpreted as a follow-on call regardless of the value of the parameter AL_INFO and the value W#16#7002 is entered in RET_VAL .

###### Parameter

The following table shows the parameters of the instruction "DP_PRAL":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ=1: Trigger process interrupt on the associated DP master |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Identifier of the address range in the transfer memory (from the point of view of the DP slave):  - B#16#00: Bit15 of LADDR specifies whether an input (Bit15=0) or output address (Bit15=1) will be present. - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed  module, you will have to specify the area identifier of the lower address. If  the addresses are identical, you will have to specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Start address of the address range in the  transfer memory (from the point of view  of the DP slave). If this is a range belonging to a mixed module, the lower of the two addresses must be specified. |
| AL_INFO | Input | DWORD | I, Q, M, D, L or constant | Interrupt ID  This is transferred to OB 40 that is to be started on the associated DP master  (tag OB40_POINT_ADDR).  If you operate the intelligent slave with a  remote master, you must evaluate the  diagnostics frame on the master. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1:  The triggered process interrupt has not  yet been acknowledged by the DP  master. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Job was executed without errors. |
| 7000 | First call with REQ=0. No process interrupt request is active; BUSY has  the value "0". |
| 7001 | First call with REQ=1. A process interrupt request has already been sent to  the DP master; BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant): The triggered process interrupt has not yet  been acknowledged by the DP master; BUSY has the value "1". |
| 8090 | Start address of the address range in the transfer memory is incorrect. |
| 8091 | Interrupt is blocked (block configured by user) |
| 8093 | The parameters IOID and LADDR address a module that is not capable of a  process interrupt request. |
| 80B5 | Call in the DP master not permitted. |
| 80C3 | The required resources (memory, etc.) are occupied at this time. |
| 80C5 | Distributed I/O device is not available at this time (i.e. station failure). |
| 80C8 | The function is not permitted in the current DP master operating mode. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### DPSYC_FR: Synchronize DP slaves / Freeze inputs (S7-300, S7-400)

###### Description

You use the instruction to synchronize one or more groups of DP slaves.

The function involves sending one of the control commands below, or a combination of them, to the relevant groups:

- SYNC (simultaneous output and freezing of output states on the DP slaves)
- UNSYNC (cancels the SYNC control command)
- FREEZE (freeze the input states on the DP slaves and read in the frozen inputs)
- UNFREEZE (cancels the FREEZE control command)

Before you send the control commands listed above, you must assign the DP slaves to groups per configuration. You must know which DP slave is assigned to which group, with which number, and know the reactions of the various groups to SYNC/FREEZE.

> **Note**
>
> Note that the control commands SYNC and FREEZE also remain valid when you perform a warm/cold restart.
>
> Please note also that you may initiate only one SYNC/UNSYNC job or only one FREEZE/UNFREEZE job at a time.

###### Functional description

"DPSYC_FR" works asynchronously, that is, its execution extends over multiple calls. You start the job by calling "DPSYC_FR" with REQ=1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

###### Identification of a job

If you have triggered a SYNC/FREEZE job and called "DPSYC_FR" again before the first job was completed, the response of the instruction depends on whether the new call is for the same job. If the input parameters LADDR, GROUP and MODE match, the call is interpreted as a follow-on call.

###### Writing outputs of DP modules

The writing of outputs of DP modules is triggered as follows:

- By transfer commands to the DP I/O
- By writing the process image output table to the modules (by the operating system at the end of OB 1 or by calling the instruction "[UPDAT_PO](#updat_po-update-the-process-image-outputs-s7-300-s7-400)")
- Calling the "[DPWR_DAT](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction.

In normal operation, the DP master transfers the output bytes cyclically (within the cycle of the PROFIBUS DP bus) to the outputs of the DP slaves.

If you want to have certain output data (possibly distributed on several slaves) applied to the outputs to the process at exactly the same time, you can send the SYNC control command to the relevant DP master using the "DPSYC_FR" instruction.

###### What are the effects of SYNC?

With the SYNC control command, the DP slaves of the selected groups are switched to Sync mode. In other words, the DP master transfers the current output data and instructs the DP slaves involved to freeze their outputs. With the following output message frames, the DP slaves enter the output data in an internal buffer and the state of the outputs remains unchanged.

Following each SYNC control command, the DP slaves of the selected groups apply the output data of their internal buffer to the outputs on the process.

The outputs are only updated cyclically again when you send the UNSYNC control command using the "DPSYC_FR" instruction.

> **Note**
>
> If the DP slaves of the selected group(s) are not currently connected to the network or have failed when the control command was sent, they will not be switched to SYNC mode. This information will not be communicated in the return value of the instruction.

###### Reading input data of DP modules

The input data of the DP modules are read as follows:

- Using load commands to the DP I/O
- When the process image input table is updated (by the operating system at the start of OB 1 or by calling the "[UPDAT_PI](#updat_pi-update-the-process-image-inputs-s7-300-s7-400)" instruction)
- By calling the "[DPRD_DAT](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction.

In normal operation, the DP master receives this input data cyclically (within the cycle of the PROFIBUS DP bus) from its DP slaves and makes them available to the CPU.

If you want to have certain input data (possibly distributed on several slaves) to be read from the process at exactly the same time, send the FREEZE control command to the relevant DP master using the "DPSYC_FR" instruction.

###### What are the effects of FREEZE?

With the FREEZE control command, the DP slaves involved are switched to Freeze mode, in other words the DP master instructs the DP slaves to freeze the current state of the inputs. It then transfers the frozen data to the input area of the CPU.

Following each FREEZE control command, the DP slaves freeze the state of their inputs again.

The DP master only receives the current state of the inputs cyclically again after you have sent the UNFREEZE control command with the "DPSYC_FR" instruction.

> **Note**
>
> If the DP slaves of the selected group(s) are not currently connected to the network or have failed when the control command has been sent, they will not be switched to FREEZE mode. This information will not be communicated in the return value of the instruction.

###### Data consistency

Because the DPSYC_FR functions are asynchronous and can be interrupted by higher priority classes, you should make sure that the process images are consistent with the actual inputs and outputs of the I/O when using the "DPSYC_FR" instruction.

This is guaranteed if you comply with the following consistency rules:

- Define suitable process image partitions for the "SYNC outputs" and the "FREEZE inputs" (only possible on the S7-400). Call the "[UPDAT_PO](#updat_po-update-the-process-image-outputs-s7-300-s7-400)" instruction immediately before each first call of a SYNC job. Call the "[UPDAT_PI](#updat_pi-update-the-process-image-inputs-s7-300-s7-400)" instruction immediately after the respective last call of a FREEZE job.
- As an alternative: Use only direct I/O access for outputs involved in a SYNC job and for inputs involved in a FREEZE job. Do not write to these outputs when a SYNC job is active, and do not read in these inputs when a FREEZE job is active.

###### Use of DPWR_DAT and DPRD_DAT

If you use the "[DPWR_DAT](#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction, it must be complete before you send a SYNC job for the outputs involved.

If you use the "[DPRD_DAT](#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instruction, it must be complete before you send a FREEZE job for the inputs involved.

###### Startup and "DPSYC_FR"

The user alone must take responsibility for sending the SYNC and FREEZE control commands in the startup OBs.

If you want the outputs of one or more groups to be in SYNC mode when the user program starts, you must initialize these outputs during startup and completely execute the "DPSYC_FR" instruction with the SYNC control command.

If you want the inputs of one or more groups to be in FREEZE mode when the user program starts, you must execute the "DPSYC_FR" instruction with the FREEZE control command completely for these inputs during startup.

###### Parameter

The following table shows the parameters of the instruction "DPSYC_FR":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Level-triggered control parameter REQ=1: Triggering of the SYNC/FREEZE job |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical address of the DP master |
| GROUP | Input | BYTE | I, Q, M, D, L or constant | Group selection  Bit 0 = 1: group 1 selected  Bit 1 = 1: group 2 selected  :  Bit 7 = 1: group 8 selected  You can select several groups per job. The value B#16#0 is invalid. |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Job ID (coding complies with EN 50 170 Volume 2, PROFIBUS)  Bit 0: reserved (value 0)  Bit 1: reserved (value 0)  Bit 2:  - = 1: UNFREEZE will be executed - = 0: no meaning   Bit 3:  - = 1: FREEZE will be executed - = 0: no meaning   Bit 4:  - = 1: UNSYNC will be executed - = 0: no meaning   Bit 5:  - = 1: SYNC will be executed - = 0: no meaning   Bit 6: reserved (value 0)  Bit 7: reserved (value 0)    Possible values:  - with exactly one ID per job:   - B#16#04 (UNFREEZE)   - B#16#08 (FREEZE)   - B#16#10 (UNSYNC)   - B#16#20 (SYNC) - with more than one ID per job:   - B#16#14 (UNSYNC, UNFREEZE)   - B#16#18 (UNSYNC, FREEZE)   - B#16#24 (SYNC, UNFREEZE)   - B#16#28 (SYNC, FREEZE) |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code.  Make sure that you evaluate RET_VAL each time the block has been executed. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1:  The SYNC/FREEZE job is not yet complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter RET_VAL

> **Note**
>
> If you access DPV1 slaves, error information of these slaves can be forwarded from the DP master to the instruction. For a description of this error information, refer to STATUS[3], [STATUS](#parameter-status-s7-300-s7-400) parameter.

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Job was executed without errors. |
| 7000 | First call with REQ=0. The job specified with LADDR, GROUP and MODE is not active; BUSY has the value 0. |
| 7001 | First call with REQ=1. The job specified with LADDR, GROUP and MODE was triggered; BUSY has the value 1. |
| 7002 | Intermediate call (REQ  irrelevant). The activated SYNC/FREEZE job is still running; BUSY has  the value 1. |
| 8090 | The module selected with LADDR is not a DP master. |
| 8093 | This instruction is not permitted for the module selected with LADDR (configuration or version of the DP master). |
| 8094 | GROUP parameter is incorrect |
| 8095 | MODE parameter is incorrect |
| 80B0 | The group selected with GROUP is not configured. |
| 80B1 | The group selected with GROUP is not assigned to this CPU. |
| 80B2 | The SYNC job specified with MODE is not permitted on the group selected  with GROUP. |
| 80B3 | The FREEZE job specified with MODE is not permitted on the group selected  with GROUP . |
| 80C2 | Temporary shortage of resources on the DP master: The DP master is  currently processing the maximum number of jobs for a CPU. |
| 80C3 | This SYNC/UNSYNC job cannot be activated at present because only one  SYNC/UNSYNC job can be triggered at a time. Check your user  program. |
| 80C4 | This FREEZE/UNFREEZE job cannot be activated at present because only one  FREEZE/UNFREEZE job can be triggered at a time. Check your user  program. |
| 80C5 | Short circuit directly at DP interface |
| 80C6 | Job aborted due to I/O disconnection by CPU |
| 80C7 | Job aborted due to warm or cold restart on the DP master |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

##### DPNRM_DG: Read diagnostics data from a DP slave (S7-300, S7-400)

###### Description

You use the "DPNRM_DG" instruction to read the current diagnostics data of a DP slave in the form specified in EN 50 170 Volume 2, PROFIBUS. The data that has been read is entered in the target range indicated by RECORD following error-free data transfer.

Refer to the following table for the basic structure of the slave diagnostics data and to the manuals of the DP slaves for further information.

| Byte | Meaning |
| --- | --- |
| 0 | Station status 1 |
| 1 | Station status 2 |
| 2 | Station status 3 |
| 3 | Master station number |
| 4 | Vendor ID (high byte) |
| 5 | Vendor ID (low byte) |
| 6 ... | Additional slave-specific diagnostic information |

###### Functional description

The reading process is executed asynchronously, in other words, it can extend over several calls. The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

###### Call

You start the read process by assigning the value "1" to the input parameter REQ when the instruction is called.

###### Parameter

The following table shows the parameters of the instruction "DPNRM_DG":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Read request |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Configured diagnostic address of the DP  slave  Note: Address must be specified in hexadecimal form, for example, diagnostic address 1022 means: LADDR:=W#16#3FE. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. If no error has occurred, the length of  the data actually transferred is entered in RET_VAL  . |
| RECORD | Output | ANY | I, Q, M, D, L | Destination area for the diagnostics data that were read. Only the BYTE data type is permitted. The minimum length of the data record to be read or the target range is 6. The maximum length of the data record to be sent is 240. Standard slaves can provide more than 240 bytes of diagnostics data up to a maximum of 244 bytes. In this case, the first 240 bytes are transferred to the target range and the overflow bit is set in the data.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1:  The reading process is not yet complete. |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

You will find information on data type conversion in the different programming languages under "[Overview of data type conversion](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)".

###### Parameter RECORD

The CPU evaluates the actual length of the read diagnostics data:

If the length specified for RECORD

- is less than the number of data bytes supplied, the data are discarded and a corresponding error code is entered in RET_VAL.
- is greater than or equal to the number of data bytes supplied, the data are accepted in the destination area and the actual length is entered in RET_VAL as a positive value.

  > **Note**
  >
  > You must ensure that the actual parameters of RECORD correspond in all calls belonging to a job.
  >
  > A job is uniquely identified by the LADDR input parameter.

###### RET_VAL parameter

- If an error occurs while the function is being executed, the return value contains an error code.
- If no errors have occurred during data transfer, RET_VAL contains the length of the data read in bytes as a positive number.

  > **Note**
  >
  > The amount of data read in a DP slave depends on its diagnostics status.

For the evaluation of the error information of the RET_VAL parameter, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val). This chapter also contains the general error information for the instructions. The specific error information of "DPNRM_DG" is a subset of the error information of "[RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400)".

###### Standard slaves with more than 240 bytes of diagnostics data

With standard slaves on which the number of standard diagnostics data is between 241 and 244 bytes, note the following points:

If the length specified for RECORD

- is less than 240 bytes, the data are discarded and a corresponding error code is entered in RET_VAL.
- If the length specified for RECORD is greater than or equal to 240 bytes, the first 240 bytes of the standard diagnostics data are transferred to the target range and the overflow bit is set in the data.

###### System resources for S7-400

When "DPNRM_DG" is called for a job that is not currently processed, CPU resources (memory space) will be occupied for S7-400. You can call "DPNRM_DG" for multiple DP slaves briefly one after the other if you do not exceed the maximum number of "concurrently" active "DPNRM_DG" jobs for your CPU.

If you activate several jobs "simultaneously," all the jobs will be executed without interfering with each other.

If you reach the limits of the system resources, this is indicated in RET_VAL. In this case, repeat the job.

---

**See also**

[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)

##### DP_TOPOL: Determine topology for DP master system (S7-300, S7-400)

###### Description

You use the instruction to trigger the topology determination for a selected DP master system. Calling the instruction will address all diagnostics repeaters on a DP master system.

> **Note**
>
> The topology can only be determined for one DP master system at a time.

Topology determination is the prerequisite for the detailed display of the error location if line errors occur. After configuration and after every change to the physical configuration of a DP master system, you must repeat the topology determination with "DP_TOPOL".

Changes to the physical configuration are:

- Changes in line lengths
- Adding or removing stations or components with repeater function
- Changing station addresses

If an error is reported by a diagnostics repeater, "DP_TOPOL" writes the DPR and DPRI outputs for the duration of one "DP_TOPOL pass. If errors are reported by multiple diagnostics repeaters of the selected DP master system, "DP_TOPOL" writes DPR and DPRI with information regarding the first diagnostics repeater reporting the error. You can read out the entire diagnostic information on the programming device or using the "[DPNRM_DG](#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)" instruction. If no diagnostics repeater reports an error, the DPR and DPRI outputs have the value NULL.

If you want to repeat a topology determination after an error occurs, you must first reset "DP_TOPOL". This is done by calling "DP_TOPOL" with REQ=0 and R=1.

###### Functional description

"DP_TOPOL" works asynchronously, that is, its execution extends over multiple calls. You start determining the bus topology by calling "DP_TOPOL" with REQ=1 . If you want to cancel the process, call "DP_TOPOL" with R=1 .

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

> **Note**
>
> Determining the topology may take several minutes.

###### Identification of a job

The input parameter DP_ID uniquely specifies a job.

If you have called "DP_TOPOL" and you call this instruction again before the topology is re-determined, the manner in which the instruction reacts depends on whether the new call involves the same job: If the DP_ID parameter matches a job that has not yet been completed, then the call is interpreted as a follow-up call and the value W#16#7002 will be entered in RET_VAL. On the other hand, if another job is involved, the CPU rejects it.

###### Parameters

The following table shows the parameters of the "DP_TOPOL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ=1: Trigger topology determination |
| R | Input | BOOL | I, Q, M, D, L | R=1: Cancel topology determination |
| DP_ID | Input | INT | I, Q, M, D, L or constant | DP master system ID of those master systems for which the topology will be determined |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1: Topology determination is not yet complete. |
| DPR | Output | BYTE | I, Q, M, D, L | PROFIBUS address of the diagnostics repeater reporting the error. |
| DPRI | Output | BYTE | I, Q, M, D, L | Measuring segment diagnostics repeater reporting the error:  - Bit 0 = 1: Temporary faults on segment DP2 - Bit 1 = 1: Permanent faults on segment DP2 - Bit 4 = 1: Temporary faults on segment DP3 - Bit 5 = 1: Permanent faults on segment DP3 |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter RET_VAL

When looking at the "real" error information (error codes W#16#8xyz) in the following table, we distinguish between two cases:

- Temporary errors (error codes W#16#80A2 to 80A4, 80C3, 80C5):

  It is possible to eliminate this type of error without user action; in other words, it is advisable to call "DP_TOPOL" again (multiple calls, if necessary).

  Example of a temporary error: Resources required are currently in use (W#16#80C3).
- Permanent errors (error codes W#16#8082, 80B0, 80B2):

  This type of error does not correct itself. A new call of "DP_TOPOL" is only advisable after you have eliminated the error. Example of a permanent error: The DP master/CPU does not support this service. (W#16#80B0).

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Job completed without error. |
| 7000 | First call with REQ=0. Topology determination is not triggered. BUSY has the value "0". |
| 7001 | First call with REQ=1. The request to execute topology determination was sent. BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant): Topology determination is not yet complete. BUSY has the value "1". |
| 7010 | You have attempted to cancel topology identification. But there is no running job with the specified DP_ID. BUSY has the value "0". |
| 7011 | First call with R=1. The cancellation of the topology determination was triggered. BUSY has the value "1". |
| 7012 | Intermediate call: The cancellation of the topology determination is not yet complete. BUSY has the value "1". |
| 7013 | Final call: The topology determination was cancelled. BUSY has the value "0". |
| 8082 | No DP master system is configured with the specified DP_ID. |
| 80A2 | Error during topology determination; for more detailed information, refer to output parameters DPR and DPRI. |
| 80A3 | Error during topology determination: Monitoring time has elapsed (timeout). |
| 80A4 | Communication on the communication bus disrupted |
| 80B0 | The DP master/CPU does not support this service. |
| 80B2 | Error during topology determination: No diagnostics repeater was found at the selected DP master system. |
| 80C3 | Resources required are currently in use. Possible cause: You have initiated a second topology determination (only one topology determination is permitted at one time). |
| 80C5 | The DP master system is currently not available. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### ASi (S7-300, S7-400)

This section contains information on the following topics:

- [ASi_3422: Control AS-i master behavior (S7-300, S7-400)](#asi_3422-control-as-i-master-behavior-s7-300-s7-400)
- [ASI_CTRL: Control AS-i master behavior (S7-300, S7-400)](#asi_ctrl-control-as-i-master-behavior-s7-300-s7-400)

##### ASi_3422: Control AS-i master behavior (S7-300, S7-400)

###### Description

The instruction "ASi_3422" is necessary to use the operating mode "Extended Operation" with CP 342-2. The extended operation allows complete control of the master behavior using the user program. The access to the inputs and outputs takes place as before in the standard operation of the CP 342-2.

Command calls to the CP342-2 occur from the user program via the instruction. You will specify a command call in a send buffer and start the job.

The instruction "ASi_3422" transfers the command call to the CP342-2. The job status will be transferred with the conclusion of the job and possible answer data will be provided in a receive buffer.

###### Call

The instruction must be cyclically called for each CP342-2. Only one job can be processed at a time per CP342-2. A current job cannot be interrupted and the instruction will not monitor the time. The instruction "ASi_3422" is executed uninterruptedly. Calls can thus not be programmed in program priority classes which interrupt each other (for example, with calls in OB 1 and in OB 35).

Configure the command processing in the user program as follows:

1. When restarting the S7 user program, call "ASi_3422" once with the parameter value STARTUP = TRUE.
2. Specify the command call in a send buffer of the user program. Transfer this send buffer with the call parameter SEND.

   You can find more information about the command interfaces and the ASi slave command in the hardware documentation of the communication processor.
3. You may need an answer buffer depending on the command type. Transfer this answer buffer with the call parameter RECV. The answer buffer is not necessary for status information with this interface.
4. Activate the job using parameter ACT=1.
5. Then query the parameters DONE, ERROR and STATUS.

###### Parameters

The following table shows the parameters of the "ASi_3422" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ACT | Input | BOOL | I, Q, M, D, L | The command processing by the function occurs level-triggered, meaning that a command processing will be started if a call is not already being processed as long as ACT = 1 is active. |
| STARTUP | Input | BOOL | I, Q, M, D, L | The instruction will indicate a CPU startup with STARTUP = 1. After the first run, the function STARTUP must be reset by the user. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Module start address  The module start address is to be determined using the information regarding the slot-oriented issuing of addresses to signal modules. |
| SEND | Input | ANY | I, Q, M, D, L | Send buffer  The parameter refers to a memory area in which the command is to be specified by the user, for example: P#DB20.DBX 20.0 Byte 10. |
| RECV | Input | ANY | I, Q, M, D, L | Receive buffer  This buffer is only relevant for commands which deliver answer data. The parameter refers to a memory area in which a command answer is stored. The length of the data area parameterized here is irrelevant, for example: P#DB30.DBX 20.0 Byte 1 |
| DONE | Output | BOOL | Q, M, D, L | DONE = 1 signals ‘job complete without error'. |
| ERROR | Output | BOOL | Q, M, D, L | ERROR = 1 signals ‘job complete with errors'. |
| STATUS | InOut | DWORD | M, D | 1. Word: Job status / error code (see following table); an error code will be generated for 'job complete with error' for more specific error description.  2. Word: Is required by the instruction for internal purposes and may not be changed.  For instruction calls to different logical addresses (LADDR) different double words must be assigned for the parameter STATUS. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

###### Parameter LADDR

The start address of the address area is determined by the slot of CP 342-2.

The CP 342-2 occupies 16 input bytes and 16 output bytes in I/O address area of the S7 automation device (analogous area of the AS). 31 x 4 bits of the 16 byte address area of the CP 342-2 are occupied by the AS-i slave data. The remaining 4 bits are reserved for later applications.

###### Parameters DONE, ERROR and STATUS

If an error occurs during the processing of the function, a "0" will be in the BR bit in addition to the information in ERROR and STATUS mentioned above. The querying of the BR bit is different for LAD and STL user programs:

- LAD: Query using output parameter ENO
- STL: Direct query of the BR bit

The following table contains the possible display in the first word of STATUS dependent upon DONE and ERROR.

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 8181 | Job running. |
| 1 | 0 | 0000 | Job complete with errors. |
| 0 | 1 | 8090 | Address at parameter LADDR invalid. |
| 0 | 1 | 80A0 | Negative acknowledgement when reading from the module. |
| 0 | 1 | 80A1 | Negative acknowledgement when writing  to the module. |
| 0 | 1 | 80B0 | The module does not recognize the data record. |
| 0 | 1 | 80B1 | Data record length entered is incorrect. |
| 0 | 1 | 80C0 | Cannot read data record. |
| 0 | 1 | 80C1 | The requested data record is still being processed. |
| 0 | 1 | 80C2 | Jobs are backed up. |
| 0 | 1 | 80C3 | Resources (memory) occupied. |
| 0 | 1 | 80C4 | Communication error |
| 0 | 1 | 8182 | Meaning: Identification after restart with STARTUP=TRUE (no errors). |
| 0 | 1 | 8184 | Data type of formal operand RECV illegal. |
| 0 | 1 | 8381 | Slave address incorrect |
| 0 | 1 | 8382 | Slave is not activated (not in LAS). |
| 0 | 1 | 8383 | Error in AS interface |
| 0 | 1 | 8384 | Command (in status of CP) illegal. |
| 0 | 1 | 8385 | Slave 0 exists. |
| 0 | 1 | 83A1 | Slave with address to be changed not found at AS interface. |
| 0 | 1 | 83A2 | Slave 0 present. |
| 0 | 1 | 83A3 | Slave with new address already present at AS interface. |
| 0 | 1 | 83A4 | Slave address cannot be deleted. |
| 0 | 1 | 83A5 | Slave address cannot be set. |
| 0 | 1 | 83A6 | Slave address cannot be permanently set. |
| 0 | 1 | 83F8 | Job number unknown. |
| 0 | 1 | 83F9 | EEPROM error |
| 0 | 1 | 8F22 | Range length error when reading a parameter. |
| 8F23 | Range length error when writing a parameter.  This error code indicates that a parameter is located either entirely or partly outside the range of an address, or that the length of a bit range is not a multiple of 8 with an ANY parameter. |  |  |
| 0 | 1 | 8F24 | Range error when reading a parameter. |
| 8F25 | Range error when writing a parameter. This error code indicates that a parameter is located in a range that is illegal for a system function. |  |  |
| 0 | 1 | 8F28 | Alignment error when reading a parameter. |
| 8F29 | Alignment error when writing a parameter. This error code indicates that the reference to parameter is an operand with bit address that is not equal to "0". |  |  |
| 0 | 1 | 8F30 | Parameter is in the read-only global DB. |
| 8F31 | Parameter is in the read-only instance DB.  This error code indicates that a parameter is located in a read-only data block. |  |  |
| 0 | 1 | 8F32 | Parameter contains a DB number which is too large |
| 0 | 1 | 8F3A | The parameter contains the number of a DB that is not loaded. |
| 0 | 1 | 8F42 | An access error occurred while the system was attempting to read a parameter from the peripheral input area. |
| 8F43 | An access error occurred while the system was attempting to write a parameter to the peripheral output area. |  |  |
| 0 | 1 | 8F44 | This error code indicates that the read access to the parameter has been denied. |
| 8F45 | This error code indicates that the write access to the parameter has been denied. |  |  |
| 0 | 1 | 8F7F | Internal error |

##### ASI_CTRL: Control AS-i master behavior (S7-300, S7-400)

This section contains information on the following topics:

- [Description of ASI_CTRL (S7-300, S7-400)](#description-of-asi_ctrl-s7-300-s7-400)
- [ASi commands (S7-300, S7-400)](#asi-commands-s7-300-s7-400)

###### Description of ASI_CTRL (S7-300, S7-400)

###### Description

Using the instruction "ASI_CTRL", you can control the behavior of the AS-i master from the user program of the PLC. The instruction processes the command protocol automatically. It also enables parameter assignment on SIMATIC AS-i masters and reading out information data. The functions and operation of the command interface are detailed in the manual for the AS-i master.

Both centrally inserted AS-i masters and distributed AS-i masters via PROFIBUS DP are supported. Combinations with PROFINET IO (e.g. IE/PB Link PN IO) are also possible.

The schematic diagram below shows the functions of the "ASI_CTRL" instruction:

![Description](images/43354545163_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Start of processing at the REQ parameter. |
| ② | The program sends the required command to the AS-i master via the instruction "RDREC". |
| ③ | The AS-i master processes the command. |
| ④ | The current status of the AS-i master is stored in the input area of the binary data (logical start address). |
| ⑤ | The instruction "ASI_CTRL" cyclically queries and evaluates the 4 status bits. |
| ⑥ | Once command processing is complete, the command job is completed with "RDREC". Depending on the command, the data field of "RDREC" may contain the response data for the command or additional status information. |

###### Dependencies between instruction versions

Version V1.3 of instruction "ASI_CTRL" requires version V1.1 of instruction "WRREC".

Version V1.2 of instruction "ASI_CTRL" requires version V1.1 of instruction "WRREC".

###### Differences in command calls between IE/ AS-i LINK and CPs / DP/AS-i LINK

There are significant differences in how a controller exchanges commands with an AS-i master.

- **IE/AS-i Link** (PROFINET) used the data record interface. The different commands are called with either "Write data record" ("WRREC" instruction) or "Read data record" ("RDREC" instruction) by various data record numbers.
- **S7-300 CPs** and **DP/AS-i Links** (PROFIBUS) use the command interface. All commands are called by data record number 2 with "Write data record" ("WRREC" instruction) plus "Read data record" ("RDREC" instruction). The type of command is defined by the data content in the write job.

###### Changes compared to the instruction "ASi_3422".

The instruction "ASI_CTRL" is a revised version of the instruction "[ASi_3422](#asi_3422-control-as-i-master-behavior-s7-300-s7-400)" and provides improved functionality and compatibility. The specific changes are as follows:

- For writing and reading diagnostic data records, the instructions "[WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400)" and "[RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400)" have been replaced by the instructions "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" and "[WRREC](#wrrec-write-data-record-s7-300-s7-400)". Their function is identical; however, they support data transfer via PROFINET IO.
- The block type of the instruction has been changed from a function (FC) to a function block (FB). "ASI_CTRL" includes an instance block and supports multiple instances.
- The designation of the formal parameters of "ASI_CTRL" complies with the SIMATIC system blocks. There is no STARTUP input parameter. The definition of the STATUS parameter is based on the instructions "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" and "[WRREC](#wrrec-write-data-record-s7-300-s7-400)". The status identifiers for the parameter DONE and the new parameter BUSY have also been adjusted.

###### Operation of the "ASI_CTRL" instruction

The instruction "ASI_CTRL" is an asynchronous function block; in other words, its processing extends over multiple calls.

- A job is started with REQ = TRUE.
- The job status is displayed via the BUSY output parameters and the two central bytes of the output parameter STATUS.
- The BUSY parameter is set during job processing. Upon the first call, STATUS is assigned the value 00700100<sub>H</sub>. Upon all subsequent calls for this job, it is assigned the value 00700200<sub>H</sub>. When the job is complete, the result is output at the parameters DONE or ERROR.

  - If no errors have occurred, DONE is set. For jobs with response data from the AS-i master, this data is provided in the specified receive buffer. In such cases, the STATUS parameter also displays the volume of data supplied in bytes. For jobs without response data, the value 00000000<sub>H</sub> is entered in STATUS.
  - If an error occurs during job processing, ERROR is set. The content of the receive buffer is invalid in such a case. An error code is entered in the STATUS parameter for a more detailed description of the error which has occurred.

###### Number of command calls

If you use the instruction "ASI_CTRL" to send commands, you may not simultaneously send other commands to the same AS-i master with "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" or "[WRREC](#wrrec-write-data-record-s7-300-s7-400)". This also applies to multiple calls of the instruction for the same AS-i master.

The instruction "ASI_CTRL" cannot be run with interruptions. Calls therefore cannot be programmed in program priority classes which interrupt each other (for example with calls in OB 1 and in OB 35).

###### Parameters

The following table shows the parameters of the "ASI_CTRL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = TRUE starts a new job unless a job is already in progress. No edge evaluation takes place. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Start address of the AS-i master in the S7 address space (logical base address). The start address is defined in the hardware configuration when the master is configured. |
| SD | Input | ANY | I, Q, M, D, L | Send buffer  The parameter refers to a memory area in which the command is to be specified (see "[ASi commands](#asi-commands-s7-300-s7-400)").  Example: P#DB101.DBX 0.0 BYTE 223 |
| RD | Input | ANY | I, Q, M, D, L | Receive buffer  This buffer is only relevant for commands which deliver answer data. The parameter refers to a memory area in which a command response is stored (see "[ASi commands](#asi-commands-s7-300-s7-400)").  Example: P#DB102.DBX 224.0 BYTE 221 |
| DONE | Output | BOOL | Q, M, D, L | DONE = TRUE: Job completed without errors. |
| BUSY | Output | BOOL | Q, M, D, L | BUSY = TRUE: Job in process. |
| ERROR | Output | BOOL | Q, M, D, L | ERROR = TRUE: Job aborted with error. |
| STATUS | Output | DWORD | M, D | Job status / error code  See the "STATUS parameter" description. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> **LADDR, SD and RD parameters**
>
> The parameters LADDR, SD and RD must not be changed in any block cycle when a job is in progress: they must remain constant.

###### Parameter STATUS

The following table shows the possible STATUS displays dependent upon DONE and ERROR.

| DONE | BUSY | ERROR | STATUS | Meaning |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 00700000<sub>H</sub> | First call with REQ = FALSE; no active job. |
| 0 | 1 | 0 | 00700100<sub>H</sub> | First call with REQ = TRUE; job has started. |
| 0 | 1 | 0 | 00700200<sub>H</sub> | Subsequent call (REQ irrelevant); job is still in progress. |
| 1 | 0 | 0 | 00000000<sub>H</sub> | Job completed without errors. No response data. |
| 1 | 0 | 0 | 0000xx00<sub>H</sub> | Job completed without errors. Number of xx bytes of response data. |
| 0 | 0 | 1 | C0818400<sub>H</sub> | Data type of formal operand RD invalid. |
| 0 | 0 | 1 | C0818500<sub>H</sub> | Error in communication with AS-i master (incorrect address configured at the LADDR parameter). |
| 0 | 0 | 1 | C0838100<sub>H</sub> | Incorrect AS-i slave address. |
| 0 | 0 | 1 | C0838200<sub>H</sub> | AS-i slave is not enabled (not in LAS). |
| 0 | 0 | 1 | C0838300<sub>H</sub> | Error at the AS interface (the SD parameter may have been set too small). |
| 0 | 0 | 1 | C0838400<sub>H</sub> | The command is not valid with the current AS-i master status. |
| 0 | 0 | 1 | C0838500<sub>H</sub> | There is an AS-i slave with the address "0". |
| 0 | 0 | 1 | C0838600<sub>H</sub> | The AS-i slave has invalid configuration data (I/O or ID codes). |
| 0 | 0 | 1 | C083A100<sub>H</sub> | The AS-i slave addressed has not been found at the AS interface. |
| 0 | 0 | 1 | C083A200<sub>H</sub> | There is an AS-i slave with the address "0". |
| 0 | 0 | 1 | C083A300<sub>H</sub> | There is already an AS-i slave with the new address at the AS interface. |
| 0 | 0 | 1 | C083A400<sub>H</sub> | The AS-i slave address cannot be deleted. |
| 0 | 0 | 1 | C083A500<sub>H</sub> | The AS-i slave address cannot be set. |
| 0 | 0 | 1 | C083A600<sub>H</sub> | The AS-i slave address cannot be permanently saved. |
| 0 | 0 | 1 | C083A700<sub>H</sub> | Error during reading of the extended ID1 code. |
| 0 | 0 | 1 | C083A800<sub>H</sub> | The target address is not plausible (e.g. a B slave address has been used for a standard slave). |
| 0 | 0 | 1 | C083B100<sub>H</sub> | A length error has occurred during string transfer. |
| 0 | 0 | 1 | C083B200<sub>H</sub> | A protocol error has occurred during string transfer. |
| 0 | 0 | 1 | C083F800<sub>H</sub> | Unknown job number or job parameter. |
| 0 | 0 | 1 | C083F900<sub>H</sub> | The AS-i master has detected an EEPROM error. |

###### ASi commands (S7-300, S7-400)

###### Description

The command interface allows the controller and AS-i master to exchange parameter assignment and information data.

These commands

- provide the complete functionality of the M4 master profile of the AS-i master specifications.
- enable the AS-i master to be completely configured from the controller.

  > **Note**
  >
  > **AS-i commands supported**
  >
  > Please see the manual of the relevant AS-i master for the AS-i commands supported and a detailed description.

###### General structure of the send buffer

The general structure of the send buffer for commands and job data is set out in the table below. The area for the command number must always be filled. The number of bytes for the job data can be found in the description of the command (see AS-i master documentation). In this case, "q" refers to the start address of the send buffer.

| Byte | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Meaning |  |  |  |  |  |  |  |  |
| q + 0 | Command number |  |  |  |  |  |  |  |
| q + 1 | Job data |  |  |  |  |  |  |  |
| q + 2 | Job data |  |  |  |  |  |  |  |
| q + ... | Job data |  |  |  |  |  |  |  |

###### General structure of the receive buffer

The general structure of the receive buffer for the command response data is set out in the table below. The number of bytes for the response data depends on the command. Some commands do not return response data, and therefore only require the definition of a virtual receive buffer which is not filled with data. In this case, "n" refers to the start address of the receive buffer.

| Byte | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Meaning |  |  |  |  |  |  |  |  |
| n + 0 | Response data |  |  |  |  |  |  |  |
| n + 1 | Response data |  |  |  |  |  |  |  |
| n + 2 | Response data |  |  |  |  |  |  |  |
| n + ... | Response data |  |  |  |  |  |  |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Memory areas can be overwritten**  If the receive buffer of the "ASI_CTRL" instruction is too short, neighboring memory areas may be overwritten. The length specified in the ANY pointer of the RD parameter when the instruction "ASI_CTRL" is called is irrelevant. The required length for the receive buffer can be found in the description of the command.  The following applies for command numbers 39<sub>H</sub>, 41<sub>H</sub>, 42<sub>H</sub>, 43<sub>H</sub> and 44<sub>H</sub>:  The receive buffer must be 221 bytes long (bytes 0 to 220), even if the command returns less data. Depending on the command, the highest bytes in the receive buffer may be overwritten with zero values by the AS-i master. |  |

###### AS-i commands

A selection of possible AS-i commands is set out in the table below.

| Name | Parameter | Return | Coding |
| --- | --- | --- | --- |
| Set_permanent_parameter (Set_Permanent_Parameter) | Slave address, parameter |  | 00 <sub>H</sub> |
| Get_permanent_parameter (Get_Permanent_Parameter) | Slave address | Parameter | 01 <sub>H</sub> |
| Write_parameter (Write_Parameter) | Slave address, parameter | Parameter echo | 02 <sub>H</sub> |
| Read_parameter (Read_Parameter) | Slave address | Parameter value | 03 <sub>H</sub> |
| Store_actual_parameters (Store_Actual_Parameters) |  |  | 04 <sub>H</sub> |
| Set_configuration_data | Slave address, configuration |  | 25 <sub>H</sub> |
| Get_configuration_data | Slave address | set configuration data | 26 <sub>H</sub> |
| Store_actual_configuration (Store_Actual_Configuration) |  |  | 07 <sub>H</sub> |
| Get_actual_configuration | Slave address | Actual configuration data | 28 <sub>H</sub> |
| Configure_LPS | LPS |  | 29 <sub>H</sub> |
| Set_offline_mode | Mode |  | 0A<sub>H</sub> |
| Select_auto-program | Mode |  | 0B <sub>H</sub> |
| Set_mode | Mode |  | 0C <sub>H</sub> |
| Change_AS–iSlave_address (Change_AS–iSlave_Address) | Address1, Address2 |  | 0D <sub>H</sub> |
| Get_AS-iSlave_status | Slave address | Error record of the AS-i slave | 0F <sub>H</sub> |
| Read_lists_and_flags |  | LDS, LAS, LPS, flags | 30 <sub>H</sub> |
| Get_overall_configuration |  | Actual configuration data, current parameters, LAS, flags | 39 <sub>H</sub> |
| Set_overall_configuration | Overall configuration |  | 3A <sub>H</sub> |
| Write_parameter_list | Parameter list |  | 3C <sub>H</sub> |
| Read_parameter_echo_list |  | Parameter echo list | 33 <sub>H</sub> |
| Write_CTT2_request | Slave address CTT2 string | CTT2 string | 44 <sub>H</sub> |
| Read_version_identifier |  | Version string | 14 <sub>H</sub> |
| Read_AS-i_slave | Slave address | ID code | 17 <sub>H</sub> |
| Read_AS-i_slave_extended_ID1 | Slave address | Extended ID1 code | 37 <sub>H</sub> |
| Write_AS-iSlave_extended_ID1 | Extended ID1 code |  | 3F <sub>H</sub> |
| Read_AS-iSlave_extended_ID2 | Slave address | Extended ID2 code | 38 <sub>H</sub> |
| Read_AS-iSlave_IO | Slave address | I/O configuration | 18 <sub>H</sub> |
| Read_I/O_error_list |  | LPF | 3E <sub>H</sub> |
| Write_AS–i-slave_parameter_string | Slave address, parameter string |  | 40 <sub>H</sub> |
| Read_AS–iSlave_parameter_string | Slave address | Parameter string | 41 <sub>H</sub> |
| Read_AS-iSlave_ID_string | Slave address | ID string | 42 <sub>H</sub> |
| Read_AS-iSlave_diagnostic_string | Slave address | Diagnostic string | 43 <sub>H</sub> |
| Read_AS-i_line_error_counter |  |  | 4A <sub>H</sub> |
| Read_and_clear_AS-i_line_error_counter |  |  | 4B <sub>H</sub> |
| Read_AS-iSlave_error_counter | Slave address |  | 4C <sub>H</sub> |
| Read_and_clear_AS-iSlave_error_counter | Slave address |  | 4D <sub>H</sub> |
| Additional command for DP/ AS-i F-Link: |  |  |  |
| AS–i_status/diag_of_F_slaves |  | Status/diagnostics of all AS-i safe slaves | 51 <sub>H</sub> |

> **Note**
>
> **Re-initializing the AS-i master command interface**
>
> Another command which is not mentioned in the table is command 77 <sub>H</sub>. This call serves to re-initialize the command interface of the AS-i master. Any command which the AS-i master specified is currently processing will be terminated.
>
> As of version V2.1.20 of DP/AS-i LINK Advanced, command 0E <sub>H</sub> is also available. This call enables you to release and block the ground fault monitoring function for a line.

## PROFIenergy (S7-300, S7-400)

This section contains information on the following topics:

- [Description of PROFIenergy (S7-300, S7-400)](#description-of-profienergy-s7-300-s7-400)
- [IO controller (S7-300, S7-400)](#io-controller-s7-300-s7-400)
- [iDevice / iSlave (S7-300)](#idevice-islave-s7-300)

### Description of PROFIenergy (S7-300, S7-400)

#### PROFIenergy

PROFIenergy is a manufacturer- and device-neutral profile for energy management with PROFINET. PROFIenergy enables central, coordinated device shutdown to reduce electricity consumption during breaks in production and unplanned interruptions.

![PROFIenergy](images/44980015883_DV_resource.Stream@PNG-en-US.png)

The PROFINET devices/power modules are switched off via special commands in the user program of the PROFINET IO controller. You do not need additional hardware. The PROFIenergy commands are interpreted directly by the PROFINET devices.

#### PROFIenergy controller (PE controller)

The PE controller is a PLC that activates or deactivates the idle state of slave devices. Specific production components, or complete production lines are deactivated and reactivated via the user program. Commands (e.g. "Start_Pause" and "End_Pause") are sent to the lower-level device using corresponding instructions (function blocks). The commands are sent via the PROFINET communication protocol.

#### PROFIenergy entity (PE entity)

The PE entity receives the PROFIenergy commands of the PE controller and converts these accordingly (e.g. by returning a measured value, or by activating the energy-saving mode). Integration of the PE entity in a device that supports PROFIenergy is based on specific device and manufacturer data.

The PE entity can be implemented, for example:

- Within the proxy of a submodule: The PE commands are valid for the addressed submodule and any existing lower-level submodules.
- Within the proxy of a module: The PE commands are valid for different submodules within the module.

  ![PROFIenergy entity (PE entity)](images/44980105611_DV_resource.Stream@PNG-en-US.png)
- For networked submodules without a proxy function: The PE commands in this case are only valid for the respective submodule.

#### PROFIenergy instructions

- Instructions for IO controller

  - The "[PE_START_END](#pe_start_end-start-and-exit-energy-saving-mode-s7-300-s7-400)" instruction represents the simplest way to activate or deactivate the idle state of the PROFINET devices (PROFIenergy commands "Start_Pause" and "End_Pause"). This is done using a positive and negative signal edge in the instruction.
  - The "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" instruction allows you to transmit all PROFIenergy commands, including "Start_Pause" and "End_Pause". With other commands, you can query the current status of the PROFINET devices or the behavior during breaks, for example.
  - The instruction "[PE_DS3_Write_ET200S](#pe_ds3_write_et200s-set-power-module-switching-behavior-s7-300-s7-400)" is used to define the switching characteristic of up to 8 slots of ET 200S. The instruction is not a PROFIenergy instruction; however, it supplements the PROFIenergy functions for an ET 200S.
- Instruction for iDevices

  The "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction allows you to implement PROFIenergy on iDevices as well. The instruction receives PROFIenergy commands on the iDevice and forwards these to the user program for processing. After processing the command, the user program calls the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction again in order to send the acknowledgement to the IO controller. For these replies, each command offers you a corresponding auxiliary block that supplies the response data to the instruction "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)".

#### PROFIenergy commands (PE commands)

The PE controller transmits PE commands to the PE entity. The PE command can be either a control command to switch a PE entity to the energy-saving mode, or a command to read a status or measured value:

- PI commands for control

  PROFIenergy supports two control commands that can be executed using either the "[PE_Start_End](#pe_start_end-start-and-exit-energy-saving-mode-s7-300-s7-400)" instruction or the "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" instruction:

  - Start_Pause: Starting a suitable energy-saving mode (PE Energy-saving mode)
  - End_Pause: Exiting the energy-saving mode (switch to PE_ready_to_operate mode)
- PI commands for reading a status or measured value

  Certain condition information can be read by the control system using the following status commands with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)":

  - PE_Identify: Reading the list of PE commands supported by the PE entity.
  - PEM_Status: Reading the currently active mode of a PE entity (e.g. PE_ready_to_operate).
  - Query_Modes: Output an overview of all supported energy-saving modes, including the time and energy information
  - Query_Measurement: Output the measured values of a PE entity

#### Example applications

Examples for use of PROFIenergy instructions can be found in the Industry Online Support in the entry "[PROFIenergy - Saving Energy with SIMATIC S7](http://support.automation.siemens.com/WW/view/en/41986454)".

---

**See also**

[Service and Support](http://support.automation.siemens.com/)

### IO controller (S7-300, S7-400)

This section contains information on the following topics:

- [PE_START_END: Start and exit energy-saving mode (S7-300, S7-400)](#pe_start_end-start-and-exit-energy-saving-mode-s7-300-s7-400)
- [PE_CMD: Start and exit energy-saving mode / Read out status information (S7-300, S7-400)](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)
- [PE_DS3_Write_ET200S: Set power module switching behavior (S7-300, S7-400)](#pe_ds3_write_et200s-set-power-module-switching-behavior-s7-300-s7-400)
- [PE_WOL: Starting and stopping energy-saving mode via WakeOnLan (S7-300, S7-400)](#pe_wol-starting-and-stopping-energy-saving-mode-via-wakeonlan-s7-300-s7-400)
- [PROFIenergy commands (S7-300, S7-400)](#profienergy-commands-s7-300-s7-400)

#### PE_START_END: Start and exit energy-saving mode (S7-300, S7-400)

##### Description

The instruction "PE_START_END" is used to start and exit the energy-saving mode of a specified PE entity (e.g. ET 200S).

The instruction "PE_START_END" is used in the PE controller, preferably when only field devices from which energy data does not need to be read out are connected to the corresponding PE devices. Alternatively, the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" can be used to read energy data.

The energy-saving modes are configured in the user program of the PE controller. On completion of the "PE_START_END" instruction, the PE entity reports its current energy-saving mode and outputs this data at parameter PE_MODE_ID.

##### Write and read jobs of the "PE_START_END" instruction.

The instruction "PE_START_END" uses "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" internally to transmit a PROFIenergy command as write job to the PE entity. "PE_START_END" then waits for the acknowledgment frame from the PE entity. The acknowledgement data record is read with the instruction "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" every 100 milliseconds. Until acknowledgment is received from the PE entity, the function repeats the read job for 10 seconds at intervals of 100 milliseconds. The response data returned by the PE entity is also read with the instruction "[RDREC](#rdrec-read-data-record-s7-300-s7-400)".

Below is a flowchart of the write and read jobs:

![Write and read jobs of the "PE_START_END" instruction.](images/44980204299_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the "PE_START_END" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| START | Input | BOOL | I, Q, M, D, L | Transmitting the PE command "Start_Pause" to the PE entity with the address set at parameter ID. |
| END | Input | BOOL | I, Q, M, D, L | Transmitting the PE command "End_Pause" to the PE entity with the address set at parameter ID. |
| ID | Input | DWORD | I, Q, M, D, L or constant | Address of the PE entity (e.g. ET 200S). The address may be taken from the hardware configuration. |
| PAUSE_TIME | Input | TIME | I, Q, M, D, L or constant | Planned pause duration.  - Range:   T#1MS to T#24D20H31M23S647MS - Start value:   T#0MS |
| VALID | Output | BOOL | I, Q, M, D, L | PE command successfully sent. |
| BUSY | Output | BOOL | I, Q, M, D, L | PE command still being processed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Error occurred during processing. The error message is output at the STATUS parameter. |
| STATUS | Output | DWORD | I, Q, M, D, L | Block status / error number (see "STATUS parameter") |
| PE_MODE_ID | Output | BYTE | I, Q, M, D, L | Identification number of energy-saving mode (energy-saving level for the duration of the pause). |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PAUSE_TIME parameter

The parameter PAUSE_TIME is used to set the default duration of the energy-saving period at the PE entity. The PE entity checks whether the pause period is of sufficient length and whether it can be implemented. The minimum pause duration (Time_min_Pause) must be greater than the sum of the times the device needs to switch to energy-saving mode (Time_to_Pause) and to switch back to operating mode (Time_to_Operate).

![PAUSE_TIME parameter](images/44980217227_DV_resource.Stream@PNG-de-DE.png)

ET 200S checks whether the scheduled pause duration is greater than or equal to the minimum pause duration (PM-E_Pause_Min) saved on the ET 200S. This is fixed at 10 seconds. If a shorter pause is used, the power modules (PM-E) of the ET 200S will remain on.

The module does not switch back on automatically at the end of the pause; it remains in OFF mode until the "END" command is sent. This prevents uncoordinated switch-on, which can cause undesired peak loads.

##### Parameter STATUS

Error information is output at the STATUS output parameter. If it is interpreted as ARRAY[1...4] of BYTE, the error information has the following structure:

| Array element | Name | Meaning |
| --- | --- | --- |
| STATUS[1] | Function_Num | Cause of the error  - B#16#**00**: No error - B#16#**DE**: Error during reading of data record - B#16#**DF**: Error during writing of data record - B#16#**C0**: Error message from the instruction or from the communication instructions "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" and "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" used internally. |
| STATUS[2] | Error_Decode | Location of the error ID  - **80**: DPV1 error as defined in IEC 61158-6 or application-specific - **FE**: DP/PNIO profiles - PROFIenergy-specific error |
| STATUS[3] | Error_Code_1 | Error ID  - When Error_Decode = **80**:   - **80**: Simultaneous rising edge at the input parameters START and END.   - **81**: Length conflict at the CMD_PARAM and CMD_PARAM_LEN parameters.   - **82-8F**: Other error messages (reserved) - When Error_Decode = **FE**:   - **01**: "Service Request ID" invalid   - **02**: Incorrect "Request_Reference"   - **03**: "Modifier" invalid   - **04**: "Data Structure Identifier RQ" invalid   - **05**: "Data Structure Identifier RS" invalid   - **06**: "PE energy-saving modes" are not supported   - **07**: "Response" is too long (maximum transmissible length exceeded)   - **08**: "Count" invalid   - **50**: No suitable "energy mode" is available.   - **51**: Time value specified is not supported.   - **52**: "PE_Mode_ID" invalid |
| STATUS[4] | Error_Code_2 | Manufacturer-specific error ID extension |

> **Note**
>
> **Error messages of the instructions RDREC and WRREC**
>
> The instruction "PE_START_END" uses the instructions "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" and "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" for communication. Error messages for these instructions are output in the field elements STATUS[1] to STATUS[4].
>
> Please see the description of the corresponding [STATUS](#parameter-status-s7-300-s7-400) parameter for an explanation of the error codes of the "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" and "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" instructions.

#### PE_CMD: Start and exit energy-saving mode / Read out status information (S7-300, S7-400)

##### Description

The instruction "PE_CMD" is used in the PE controller to start or terminate a pause in the energy-saving mode in the PE entity. "PE_CMD" can be used to read additional information and energy measurement values from a PE entity.

The instruction is best used with PE controllers to which assigned PE devices are connected from which energy measurements are to be read out. If this is not the case, the instruction "[PE_START_END](#pe_start_end-start-and-exit-energy-saving-mode-s7-300-s7-400)" can also be used to start and end the pauses.

##### Transfer of the PROFIenergy commands (PE commands)

The instruction "PE_CMD" transmits a PROFIenergy command to a PE entity.

The instruction can also be used if additional commands are to be added to the PROFIenergy profile in future. The commands which can be used with the current PROFIenergy profile are listed in the description of the CMD and CMD_MODIFIER parameters (see the "CMD and CMD_MODIFIER parameters" table).

- The individual PE commands which are transferred to the PE entity using the instruction are assigned defined "Service_Request_IDs". The Service_Request_IDs 01 to 05 and 16 are assigned at the CMD parameter.
- The two PE commands 04 (Query_Modes) and 16 (Query_Measurement) are defined in more detail with the CMD_MODIFIER parameter.
- Additional values are transferred at the CMD_PARA parameter for individual PE commands (see the description of the individual PE commands). The parameter CMD_PARA_LEN defines the length of the data at the parameter CMD_PARA.

Commands are transmitted without a plausibility check. The response data of the PE entity is saved to the RESPONSE_DATA data area that is addressed by ANY pointer (for information about the response frame contents, refer to the description of the respective PE command).

##### Write and read jobs of the "PE_CMD" instruction.

The instruction "PE_CMD" uses "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" internally to transmit a PROFIenergy command as a write job to the PE entity. "PE_CMD" then waits for the acknowledgment from the PE entity. The acknowledgement data record is read with the instruction "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" every 100 milliseconds. Until acknowledgment is received from the PE entity, the function repeats the read job for 10 seconds at intervals of 100 milliseconds. The response data returned by the PE entity is also read with the instruction "[RDREC](#rdrec-read-data-record-s7-300-s7-400)".

Below is a flowchart of the write and read jobs:

![Write and read jobs of the "PE_CMD" instruction.](images/44980204299_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the "PE_CMD" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Starts transferring the PE command upon a rising edge. |
| ID | Input | DWORD | I, Q, M, D, L or constant | Address of the PE entity  For PROFINET IO devices, you can transfer the address from the hardware configuration. |
| CMD | Input | BYTE | I, Q, M, D, L, P or constant | Service-Request-ID of the PROFIenergy command in accordance with the PROFIenergy profile (see "CMD and CMD_MODIFIER parameters").  Further service request IDs are possible following extensions of the PROFIenergy profile. |
| CMD_MODIFIER | Input | BYTE | I, Q, M, D, L, P or constant | PROFIenergy sub-command  (only when CMD=3 or CMD=16, see "CMD and CMD_MODIFIER parameters")  Further sub-commands are possible following extensions of the PROFIenergy profile. |
| CMD_PARA | Input | ANY | I, Q, M, D, L | Parameters for the PE commands:  - Get mode: PE_mode_ID - Get measurement values: List of Measurement_Ids   The complete Service Data Request is entered. |
| CMD_PARA_LEN | Input | INT | I, Q, M, D, L, P or constant | The actual length of the command parameters (&lt;= length defined in CMD_PARA; is verified by the instruction). |
| RESPONSE_DATA | InOut | ANY | I, Q, M, D, L | PROFIenergy information   May be complete response frame including block header, depending on the command.  Note: If the buffer is too small, only the number of bytes which is specified in the ANY pointer will be entered. |
| VALID | Output | BOOL | I, Q, M, D, L | Command successfully sent. |
| BUSY | Output | BOOL | I, Q, M, D, L | Command still being processed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Error occurred during processing. |
| STATUS | Output | DWORD | I, Q, M, D, L | Block status / error number (see "STATUS parameter"): |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameters CMD and CMD_MODIFIER

| CMD | CMD_ MODIFIER | PROFIenergy command | Description |
| --- | --- | --- | --- |
| 01 | 0 | [Start_Pause](#pi-command-start_pause-s7-300-s7-400) | Start energy-saving mode or switch to a different energy-saving mode. |
| 02 | 0 | [End_Pause](#pi-command-end_pause-s7-300-s7-400) | End energy-saving mode. |
| 03 | 1 | [Query_Modes - List of energy-saving modes](#pi-command-query_modes---list_energy_saving_modes-s7-300-s7-400) | Output the energy-saving modes supported. |
| 2 | [Query_Modes - Get mode](#pi-command-query_modes---get_mode-s7-300-s7-400) | Output attributes of the energy-saving mode currently enabled. |  |
| 04 | 0 | [PEM_Status](#pi-command-pem_status-s7-300-s7-400) | Query status of energy-saving mode. |
| 05 | 0 | [PE_Identify](#pi-command-pe_identify-s7-300-s7-400) | Read out the number and description of PE commands supported. |
| 16 | 1 | [Query_Measurement - Get_Measurement_List](#pi-command-query_measurement---get_measurement_list-s7-300-s7-400) | List of measured values supported by the PE entity. |
| 2 | [Query_Measurement - Get_Measurement_Values](#pi-command-query_measurement---get_measurement_values-s7-300-s7-400) | Output the measured values of the PE entity |  |

##### Parameter STATUS

Error information is output at the STATUS output parameter. If it is interpreted as ARRAY[1...4] of BYTE, the error information has the following structure:

| Array element | Name | Meaning |
| --- | --- | --- |
| STATUS[1] | Function_Num | Cause of the error  - B#16#**00**: No error - B#16#**DE**: Error during reading of data record - B#16#**DF**: Error during writing of data record - B#16#**C0**: Error message from the internal communication instructions "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" and "[WRREC](#wrrec-write-data-record-s7-300-s7-400)". |
| STATUS[2] | Error_Decode | Location of the error ID  - **80**: DPV1 error as defined in IEC 61158-6 or application-specific - **FE**: DP/PNIO profiles - PROFIenergy-specific error |
| STATUS[3] | Error_Code_1 | Error ID  - When Error_Decode = **80**:   - **81**: Length conflict at the CMD_PARA and CMD_PARA_LEN parameters, or maximum data record length (4095 bytes) exceeded.   - **82-8F**: Other error messages (reserved) - When Error_Decode = **FE**:   - **01**: "Service Request ID" invalid   - **02**: Incorrect "Request_Reference"   - **03**: "Modifier" invalid   - **04**: "Data Structure Identifier RQ" invalid   - **05**: "Data Structure Identifier RS" invalid   - **06**: "PE energy-saving modes" are not supported   - **07**: "Response" is too long (maximum transmissible length exceeded)   - **08**: "Count" invalid   - **50**: No suitable energy-saving mode (energy mode) is available.   - **51**: Time value specified is not supported.   - **52**: "PE_Mode_ID" invalid |
| STATUS[4] | Error_Code_2 | Manufacturer-specific error ID extension |

> **Note**
>
> **Error messages of the instructions RDREC and WRREC**
>
> The "PE_CMD" instructions use the "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" and "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" instructions for communication. Error messages for these instructions are output in the field elements STATUS[1] to STATUS[4].
>
> Please see the description of the corresponding [STATUS](#parameter-status-s7-300-s7-400) parameter for an explanation of the error codes of the "[WRREC](#wrrec-write-data-record-s7-300-s7-400)" and "[RDREC](#rdrec-read-data-record-s7-300-s7-400)" instructions.

#### PE_DS3_Write_ET200S: Set power module switching behavior (S7-300, S7-400)

##### Description

The instruction "PE_DS3_Write_ET200S" sends basic settings for power module switching behavior to the ET 200S. The switching behavior of up to 8 slots in the ET 200S (e.g. for power modules) can be defined with the instruction "PE_DS3_Write_ET200S".

> **Note**
>
> This instruction is not part of the PROIenergy profile but instead supplements SIMATIC-specific functions.

##### Parameters

The following table shows the parameters of the "PE_DS3_Write_ET200S" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ENABLE | Input | BOOL | I, Q, M, D, L | A positive edge triggers the transfer of the data record. The data record must be transferred again after voltage OFF/ON. |
| ID | Input | DWORD | I, Q, M, D, L or constant | Address of the ET 200S  The address may be taken from the hardware configuration. |
| SLOT_NO_X | Input | INT | I, Q, M, D, L, P or constant | Slot number of switchable power module X. |
| FUNC_X | Input | INT | I, Q, M, D, L, P or constant | Function of the module in this slot. Use the parameter FUNC_X to define the switching behavior of the PM-E (power module of the ET 200S):  - FALSE:   - With "PAUSE_START":     -No effect on PM-E     -PM-E remains on   - With "PAUSE_STOP":     -Switches PM_E back on - TRUE:   - With "PAUSE_START":     -Switches PM_E off   - With "PAUSE_STOP":     -Switches PM-E back on |
| BUSY | Output | BOOL | I, Q, M, D, L | Transfer not yet complete. |
| DONE | Output | BOOL | I, Q, M, D, L | Transfer completed without errors. |
| ERROR | Output | BOOL | I, Q, M, D, L | Transfer completed with error. |
| STATUS | Output | DWORD | I, Q, M, D, L, P | Error number (see STATUS parameter of the instruction "[PE_Start_End](#pe_start_end-start-and-exit-energy-saving-mode-s7-300-s7-400)") |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### PE_WOL: Starting and stopping energy-saving mode via WakeOnLan (S7-300, S7-400)

This section contains information on the following topics:

- [Description PE_WOL (S7-300, S7-400)](#description-pe_wol-s7-300-s7-400)
- [Parameter COM_RST (S7-300, S7-400)](#parameter-com_rst-s7-300-s7-400)
- [Parameter START (S7-300, S7-400)](#parameter-start-s7-300-s7-400)
- [Parameter END (S7-300, S7-400)](#parameter-end-s7-300-s7-400)
- [PENERGY parameter (S7-300, S7-400)](#penergy-parameter-s7-300-s7-400)
- [Parameter STATUS (S7-300, S7-400)](#parameter-status-s7-300-s7-400-1)

##### Description PE_WOL (S7-300, S7-400)

###### Description

The "PE_WOL" instruction sends the PROFIenergy commands "Start_Pause" and "End_Pause" to multiple PROFIenergy-enabled devices in the PROFINET I/O systems.

Multiple PE devices can be coordinated via the instruction provided that the PE devices support the "Wake on LAN" function over a UDP connection.

The "PE_WOL" instruction can only be executed on a CPU with and integrated Ethernet interface. This CPU should be able to load blocks with a size of about 40 KB. You cannot use the block with PROFINET I/O systems that are connected via an Ethernet CP.

The instruction "PE_WOL" is executed asynchronously.

###### Definition: Wake on LAN

The Wake on LAN function allows data processing equipment to resume working from a state near total shutdown when a special Ethernet packet is received.

For this procedure to work, the data processing equipment must have a network controller that is capable of receiving such a packet.

This packet (Magic Packet™) has a special format. It contains the MAC address of the network adapter 15 times.

###### Selection of devices

The devices are selected using the user data block at the parameter PENERGY. The user DB represents the database for processing multiple devices.

Prior to initialization of "PE_WOL", you must store at least the following information in the user DB:

- ID of the PROFINET I/O system
- Data of the connection which is used for "Wake On LAN".
- Port number which is used for "Wake On LAN".
- For each device

  - Pause time (PauseTime)
  - Switching of the device to the PE_SLEEP_MODE (EnableSleep)

You initialize the "PE_WOL" instruction with the COM_RST parameter. The jobs stored in the user DB are processed one after the other after initialization.

The graphic below illustrates how the PE command "Start_Pause" is transmitted to several devices:

![Selection of devices](images/53068191755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| (1) | Step 1: The bit "CmdStartPause" of the devices to be shut down is set to "1" by the user. |
| (2) | Step 2: The diagnostic addresses of the devices to be shut down (CmdStartPause = "1") are linked to the queue. |
| (3) | Step 3: The bit "CmdStartPause" is reset automatically once the jobs have been linked. |
| (4) | Step 4: The instruction "PE_WOL" processes the jobs as soon as they are linked. |

A PROFIenergy command "CmdStartPause" or "CmdEndPause" can be sent for all recognized devices in the PROFINET IO system via the START and END parameters.

The status of the job processing as well as possible errors during processing are output by the STATUS parameter.

###### Operation of the instruction using the user DB

The operation of the instruction "PE_WOL" can only take place via the user DB. A basic procedure applies in this case:

1. Selection of the command to be executed for a device:

   - START_PAUSE ("CmdStartPause" in user DB)
   - ENDE_PAUSE ("CmdEndPause" in user DB)
   - UPDATE_STATUS ("CmdUpdateStatus" in user DB)
2. Setting the bit for updating ("Update" in the header of the user DB)

   At least one CPU cycle should pass with an "Update" = False between two updates; otherwise, edge detection cannot be guaranteed.

###### Prioritizing the PE commands

The graphic below shows the chronological sequence of three possible commands.

![Prioritizing the PE commands](images/53124216971_DV_resource.Stream@PNG-de-DE.png)

These are processed one after the other, regardless of whether the previous command call was successful or completed with an error.

Only one command is executed if you set two commands, such as "CmdEndPause" and "CmdUpdateStatus" simultaneously. A prioritization is present within the block:

- The command "CmdStartPause" has the highest priority and is therefore always executed if selected.
- The command "CmdEndPause" has the second highest priority.
- The command "CmdUpdateStatus" has the lowest priority.

If all three commands are set at the same time, the commands that are not executed remain preselected. In this case, the next rising edge executes the next command.

###### Parameter

The following table shows the parameters of the "PE_WOL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| [COM_RST](#parameter-com_rst-s7-300-s7-400) | Input | BOOL | I, Q, M, D, L | Resets the block and performs a re-initialization. As long as True is set here, the initialization is started but not yet fully completed.   Only the falling edge continues the initialization and switches to the normal operating mode after initialization. |
| [START](#parameter-start-s7-300-s7-400) | Input | BOOL | I, Q, M, D, L | A rising edge performs a "CmdStartPause" PROFIenergy command for all detected devices that support this function. |
| [END](#parameter-end-s7-300-s7-400) | Input | BOOL | I, Q, M, D, L | A rising edge performs a "CmdEndPause" PROFIenergy command for all detected devices that support this function. |
| [PENERGY](#penergy-parameter-s7-300-s7-400) | InOut | ANY | D | Pointer to the user DB that contains the database for processing multiple devices. |
| [STATUS](#parameter-status-s7-300-s7-400-1) | Output | DWORD | I, Q, M, D, L | Status/error number for the current status of the instruction (see "STATUS parameter"). |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter COM_RST (S7-300, S7-400)

###### Sequence of the initialization routine

You start the initialization of the "PE_WOL" instruction with the COM_RST parameter.

The following flow diagram shows the initialization routine.

![Sequence of the initialization routine](images/53103501707_DV_resource.Stream@PNG-en-US.png)

##### Parameter START (S7-300, S7-400)

###### Sequence of the CmdStartPause command

The flow diagram shows the internally used functions and interaction with a device when executing the CmdStartPause command.

![Sequence of the CmdStartPause command](images/53073802891_DV_resource.Stream@PNG-en-US.png)

##### Parameter END (S7-300, S7-400)

###### Sequence of the CmdEndPause command

The flow diagram shows the internally used functions and interaction with a device when executing the CmdEndPause command.

![Sequence of the CmdEndPause command](images/53107116171_DV_resource.Stream@PNG-en-US.png)

##### PENERGY parameter (S7-300, S7-400)

###### Data block at the PENERGY parameter

The user DB for the "PE_WOL" PROFIenergy instruction represents a data base for processing multiple devices.

The data block is usually divided into two parts. These are:

- Header 110 bytes
- Device section for a maximum of 256 devices each with 100 bytes (Device). These include:

  - Device-specific data (Device)
  - PROFIenergy-specific data (PE)
  - Data for the job processing (Task)
  - User data (UserData)

The individual sections have a certain size, which is constant. Overall, these result in a constant size of 25,746 bytes for the data block.

###### Connection parameter "Connection"

The "PE_WOL" instruction reserves a connection resource in the area of "Open User Communication". This is used as a UDP connection. The following parameters must be defined in the data block for this:

- Connection ID ("Connection.id" parameter)

  The connection ID is an integer within the range of 1 to 32. The default setting is 31. It is used to identify the communication resources allocated by the firmware, for example the send and receive buffers.   
  The connection ID must be unique throughout the CPU.
- Port number that is used for the "Wake on LAN" function ("Header.PortNo" parameter)

  Number of the UDP port via which a "Wake On LAN" packet is sent. These port numbers are part of the communication resources, which are identified and provided by the firmware through the connection ID. The default setting for port 2189 used here is currently not assigned by IANA. The port number is transferred to the connection configuration. This affects the "Connection.local_tsap_id[1]" and "Connection.rem_tsap_id[1]" parameters.
- Interface ID ("Connection.local_device_id" parameter)

  The interface ID is also part of the connection description. This ID identifies the CPU interface to use for this connection. There are several possible valid values.

  However, these need to be adapted to the employed CPU and interface:

  - B#16#01 for ET200S CPU or WinAC RTX with Ethernet interface in subslot IF1
  - B#16#02 for CPU 315(F)-2PN/DP or CPU 317(F)-2PN/DP
  - B#16#03 for CPU 319(F)-2PN/DP
  - B#16#05 for CPU 41x(F)-3PN/DP
  - B#16#06 for WinAC RTX with Ethernet interface in subslot IF2
  - B#16#0B for WinAC RTX with Ethernet interface in subslot IF3
  - B#16#0F for WinAC RTX with Ethernet interface in subslot IF4

###### Structure of the data block

The data block has the following structure:

| Name |  |  |  | Data type | Offset | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| Header |  |  |  | STRUCT | - | Header information |
|  | Update<sup> (1)</sup> |  |  | BOOL | 0.0 | Signal for indicating a change in the data area.  - True = indicates a change by the user. - False = indicates the application of changes. |
| Initialized |  |  | BOOL | 0.1 | Signal indicating the completed initialization.  - True = initialization completed. - False = indicates that the block is not initialized. |  |
| LinkUp |  |  | BOOL | 0.2 | Indicates successful configuration of the Ethernet interface.  - True = interface ready-to-use. - False = interface not yet configured. |  |
| LinkDown |  |  | BOOL | 0.3 | Indicates an unconfigured interface.  - True = interface is not configured. - False = interface is currently being configured or is now configured. |  |
| PROFINET_ID<sup> (1)</sup> |  |  | INT | 2.0 | ID of the PROFINET I/O system |  |
| Reserved |  |  | ARRAY [1..37] OF BYTE | 4.0 | Reserved |  |
| LastDeviceID |  |  | INT | 42.0 | Contains the highest device ID in the PROFINET I/O system. |  |
| PortNo<sup> (1)</sup> |  |  | INT | 44.0 | Port number that is used for the "Wake on LAN" function (default= 2189). |  |
| Connection |  |  | STRUCT | - | Contains the connection configuration of the "Wake on LAN" connection. |  |
|  |  |  | block_length | WORD | 46.0 | Length of the structure (always B#16#40). |
| id<sup> (1)</sup> | WORD | 48.0 | Connection ID |  |  |  |
| connection_type<sup> (1)</sup> | BYTE | 50.0 | Connection type (UDP = B#16#13) |  |  |  |
| active_est<sup> (1)</sup> | BOOL | 51.0 | Active connection establishment (always passive for UDP) |  |  |  |
| local_device_id<sup> (1)</sup> | BYTE | 52.0 | Contains the interface ID (CPU dependent) |  |  |  |
| local_tsap_id_len<sup> (1)</sup> | BYTE | 53.0 | Contains the length in bytes of the own/local UDP port |  |  |  |
| rem_subnet_id_len<sup> (1)</sup> | BYTE | 54.0 | Unused (always B#16#00) |  |  |  |
| rem_staddr_len<sup> (1)</sup> | BYTE | 55.0 | Contains the length of the remote IP address or B#16#00. |  |  |  |
| rem_tsap_id_len <sup>(1)</sup> | BYTE | 56.0 | Contains the length in bytes of the remote UDP port. |  |  |  |
| next_staddr_len<sup> (1)</sup> | BYTE | 57.0 | Contains the length of the default router address (not relevant). |  |  |  |
| local_tsap_id <sup>(1)</sup> | ARRAY[1..8] OF INT | 58.0 | Contains your own local port number. |  |  |  |
| rem_subnet_id<sup> (1)</sup> | ARRAY[1..6] OF BYTE | 74.0 | Unused (always B#16#00) |  |  |  |
| rem_staddr <sup>(1)</sup> | ARRAY[1..6] OF BYTE | 80.0 | Contains the remote IP address. |  |  |  |
| rem_tsap_id <sup>(1)</sup> | ARRAY[1..8] OF INT | 86.0 | Contains the remote UDP port number. |  |  |  |
| next_staddr<sup> (1)</sup> | ARRAY[1..6] OF BYTE | 102.0 | Irrelevant |  |  |  |
| spare<sup> (1)</sup> | WORD | 108.0 |  |  |  |  |
| Device |  |  |  | ARRAY[1..256] OF STRUCT | 110.0 | Array of devices |
|  | Device |  |  | STRUCT | 110.0 | Contains data for each device |
|  |  | DiagID |  | WORD | 110.0 | Diagnostic address of the device. Assigned by the hardware configuration. |
| InterfaceID |  | WORD | 112.0 | Diagnostic address of the device interface. Assigned by the hardware configuration. |  |  |
| MACAdr |  | ARRAY[1..6] OF BYTE | 114.0 | Contains the MAC address of the device. |  |  |
| IPAdr |  | ARRAY[1..4] OF BYTE | 120.0 | Contains the IP address of the device. |  |  |
| OrderID |  | STRUCT | 124.0 | Contains the OrderID of the device. |  |  |
|  | MxLen | BYTE |  | Contains the maximum length of the array. |  |  |
| ActLen | BYTE |  | Contains the current number of data in the array. |  |  |  |
| Data | ARRAY[1..20] CHAR |  | Contains the data. |  |  |  |
|  | PE |  |  | STRUCT | 146.0 | PROFIenergy-specific data. |
|  |  | ModeID |  | BYTE | 146.0 | PE_MODE_ID according to Profienergy specification. |
| Result |  | BYTE | 147.0 | PEErrorCode according to Profienergy specification. |  |  |
| PauseTime <sup>(1)</sup> |  | TIME | 148.0 | Contains the idle time in ms. |  |  |
| TimeToPause |  | TIME | 152.0 | Contains the time it takes for the device to go into Pause mode. |  |  |
| TimeToOperate |  | TIME | 156.0 | Contains the time it takes for the device to go into operating mode. |  |  |
| MinSleepTime |  | TIME | 160.0 | Contains the minimum time of the device in PE_SLEEP_MODE. |  |  |
| SleepToOperate |  | TIME | 164.0 | Contains the time it takes for the device to go from PE_SLEEP_MODE into operating mode. |  |  |
| StatusOperate |  | BOOL | 168.0 | Indicates the operating mode of the device. |  |  |
| StatusPause |  | BOOL | 168.1 | Indicates the device is in Pause mode. |  |  |
| StatusSleep |  | BOOL | 168.2 | Indicates the PE_SLEEP_MODE of the device. |  |  |
| StatusTransitOK |  | BOOL | 168.3 | Indicates the transition from one energy state to another. |  |  |
| StatusInTransit |  | BOOL | 168.4 | Indicates a current state transition. |  |  |
| StatusTransitNOK |  | BOOL | 168.5 | Indicates that the state change was not successful. |  |  |
| StatusError |  | BOOL | 168.6 | Indicates an error with the device. |  |  |
| StatusRetryEx |  | BOOL | 168.7 | Indicates an unsuccessful execution of a command. No more attempts will be made to execute this command. |  |  |
| CmdStartPause <sup>(1)</sup> |  | BOOL | 169.0 | Places a START_PAUSE command for this device in the queue. |  |  |
| CmdEndPause<sup> (1)</sup> |  | BOOL | 169.1 | Places a END_PAUSE command for this device in the queue. |  |  |
| CmdUpdateStatus <sup>(1)</sup> |  | BOOL | 169.2 | Places a PEM_STATUS command for this device in the queue. |  |  |
| EnableSleep<sup> (1)</sup> |  | BOOL | 169.3 | Allows PE_SLEEP_MODE for this device.  - True = device should go to PE_SLEEP_MODE when idle time is too long - False = device may not go into PE_SLEEP_MODE. |  |  |
| Services |  | WORD | 170.0 | Shows all supported PROFIenergy services. |  |  |
|  | UserData<sup> (2)</sup> |  |  | ARRAY[1..24] OF BYTE | 172.0 | User-defined data |
|  | Task |  |  | STRUCT | 196.0 | Job processing |
|  |  | Cmd |  | BYTE | 196.0 | Internal bits for job processing |
| CmdJ |  | BYTE | 197.0 | Internal bits for job processing |  |  |
| TimeStart |  | BOOL | 198.0 | Starts a delay time. |  |  |
| TimeStarted |  | BOOL | 198.1 | The delay time has just started. |  |  |
| TimeDone |  | BOOL | 198.2 | Shows the expiration of the delay time. |  |  |
| Done |  | BOOL | 198.3 | Indicates that this job has been completed. |  |  |
| DelayedCmd |  | BOOL | 198.4 | Indicates that a delayed command is still pending. |  |  |
| IsV1_0 |  | BOOL | 198.5 | Indicates that this device is a Spec. V1.0 device. |  |  |
| IsWakeOnLAN |  | BOOL | 198.6 | Indicates that this device is woken up by "Wake On LAN". |  |  |
| RetryCount |  | BYTE | 199.0 | Repetition counter for PE_COMMANDS |  |  |
| Duration |  | TIME | 200.0 | Contains the value for the delay in ms. |  |  |
| StartTime |  | TIME | 204.0 | Contains the start time for the delay time. |  |  |
| MachineState |  | INT | 208.0 | Contains the internal status of the job. |  |  |
| <sup>(1)</sup> To be filled in by the user.   <sup>(2)</sup> Available for use by the user. |  |  |  |  |  |  |

##### Parameter STATUS (S7-300, S7-400)

###### Parameter STATUS

The output value at the STATUS parameter is divided into three areas:

- Bits 31 to 24: MESSAGE
- Bit 23 to 16: LOCATION
- Bit 15 to 0: INFORMATION

You can learn the meaning of each error code for the three areas in the following tables:

All tables
Possible values for MESSAGE
Possible values for LOCATION
Possible values for INFORMATION

Possible values for MESSAGE

| Error code  (W#16#...) | Description |
| --- | --- |
| 00 | No error. |
| 50 | Instruction initialized. |
| 51 | Determining configuration of the PROFINET I/O system. |
| 52 | The instruction could not determine any configured devices in the PROFINET I/O system. |
| 53 | Determining the logical addresses of configured devices. |
| 54 | Reading interface information out of the devices. |
| 55 | Determining I&amp;M data (data record 0 only) of the configured devices. |
| 56 | Configuring PROFINET interface for sending the "Wake on LAN" MagicPaket™ via UDP. |
| 57 | Determining PROFIenergy capabilities of the connected devices. |
| 62 | Invalid PROFINET I/O system ID detected. The causative number is displayed in the INFORMATION field. |
| 70 | The instruction is initiated and processing jobs. The value in the INFORMATION field contains the number of currently active jobs. |
| 80 | The instruction has lost the initialization during processing of jobs. This generally occurs when either the instance DB or the user DB has been reloaded. |
| FF | Unknown error has occurred. |

Possible values for LOCATION

| Error code  (W#16#...) | Description |
| --- | --- |
| 00 | The instruction is either not initialized or it is idle. |
| 70 | The instruction is waiting for jobs. |
| 71 | The instruction has appended a job to the job list. |
| 72 | The instruction is preparing to send a job. |
| 73 | The instruction is sending a job to a device. |
| 74 | The instruction is waiting for a response from the device. |
| 75 | The instruction is evaluating the response of the device. |
| 76 | The instruction is removing the job from the job list. |
| FF | Unknown error has occurred. |

Possible values for INFORMATION

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No additional information available and no jobs active. |
| 0001 -00FF | 1 – 255 jobs are currently being processed. |
| 8001 | Error at parameter 1 |
| 8002 | Error at parameter 2 |
| 8003 | Error at parameter 3 |
| 8004 | Error at parameter 4 |
| 8005 | Error at parameter 5. This error is reported if there is no interconnection or an invalid interconnection to the user DB.  Possible causes:  - The user DB is too small. - The user DB is write-protected. - There is no user DB in the RAM. - The user DB is invalid for the employed CPU. |
| 8100 | An attempt has been made to place more than the maximum of 256 possible jobs. This is a temporary error, which is resolved by completing a few jobs. The placed jobs are not accepted and must be placed again. |
| 8200 | An attempt has been made to send an invalid or an unsupported PROFIenergy command (PE_COMMAND). |
| 84xx | A communication error has occurred. The number of the device that generated the error is output to "xx". |
| 85xx | An error has been returned from device xx. The number of the device that generated the error is output to "xx". |
| 8600 | The requested wake-up method is currently not supported. |
| FFFF | Unknown error has occurred. |

#### PROFIenergy commands (S7-300, S7-400)

This section contains information on the following topics:

- [PI Command "Start_Pause" (S7-300, S7-400)](#pi-command-start_pause-s7-300-s7-400)
- [PI Command "End_Pause" (S7-300, S7-400)](#pi-command-end_pause-s7-300-s7-400)
- [PI command "Query_modes" - "List_Energy_Saving_Modes" (S7-300, S7-400)](#pi-command-query_modes---list_energy_saving_modes-s7-300-s7-400)
- [PI command "Query_modes" - "Get_Mode" (S7-300, S7-400)](#pi-command-query_modes---get_mode-s7-300-s7-400)
- [PI command "PEM_Status" (S7-300, S7-400)](#pi-command-pem_status-s7-300-s7-400)
- [PI command "PE_Identify" (S7-300, S7-400)](#pi-command-pe_identify-s7-300-s7-400)
- [PI Command "Query_Measurement" - "Get_Measurement_list" (S7-300, S7-400)](#pi-command-query_measurement---get_measurement_list-s7-300-s7-400)
- [PI Command "Query_Measurement" - "Get_Measurement_values" (S7-300, S7-400)](#pi-command-query_measurement---get_measurement_values-s7-300-s7-400)

##### PI Command "Start_Pause" (S7-300, S7-400)

###### Description

Use the PE command "Start_Pause" to start the energy-saving mode. The command Start_Pause can be used to:

- Switch the PE from "ready" state (PE_ready_to_operate) to an energy-saving mode (PE_energy_saving_mode).
- The PE entity can automatically switch between the energy-saving modes.

  Energy consumption can increase or decrease when you switch energy-saving mode.

###### Calling the PI command "Start_Pause"

The command "Start_Pause" is called with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 1 | Call of PE command "Start_Pause". |
| CMD_MODIFIER | 0 | There are no additional specifications of the command call for command "Start_Pause". |
| CMD_PARA_LEN | 4 | Length of the CMD_PARA parameter of 4 bytes. |
| CMD_PARA | ANY | ANY pointer to the value for "Pause_Time" (TIME). |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at at parameter RESPONSE_DATA (see instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| PE_Mode_ID | 1 to 255 | BYTE | Identification number of the energy-saving mode |
| Reserved | 0 | BYTE | - |
|  |  |  |  |

##### PI Command "End_Pause" (S7-300, S7-400)

###### Description

Use the PE command "End_Pause" to terminate the energy-saving mode of the PE entity.

###### Calling the PI command "End_Pause"

The command "End_Pause" is called with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 2 | Call of PE command "End_Pause". |
| CMD_MODIFIER | 0 | There are no additional specifications of the command call for command "End_Pause". |
| CMD_PARA_LEN | 0 | Length of the CMD_PARA parameter of 0 bytes. |
| CMD_PARA | irrelevant | - |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| Time_to_operate | - | DWORD | Expected time it takes to switch to the "PE_ready_to_operate" mode. |

##### PI command "Query_modes" - "List_Energy_Saving_Modes" (S7-300, S7-400)

###### Description

Use PE command "Query_modes" and sub-command (modifier) "List_Energy_Saving_Modes" to output all energy-saving modes (PE_Mode_ID) supported by the PE entity.

The query result is written in the form of a response frame to the data block referenced by theRESPONSE_DATA parameter.

###### Calling the PI command "Query_modes" - "List_Energy_Saving_Modes"

The command "List_Energy_Saving_Modes" is called with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 3 | Call of PE command "Query_modes". |
| CMD_MODIFIER | 1 | Specification of the command call: Select the sub-command "List_Energy_Saving_Modes" to output the number and types of energy-saving modes supported. |
| CMD_PARA_LEN | 0 | Length of the CMD_PARA parameter of 0 bytes. |
| CMD_PARA | irrelevant | - |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| Number_of_PE_ Mode_IDs | 1 | BYTE | Number of energy-saving modes. |
| PE_Mode_IDs | - | Array [...] of BYTE | Array with the IDs of the supported energy-saving modes. The significance of the IDs depends on the PE entity. |
|  |  |  |  |

##### PI command "Query_modes" - "Get_Mode" (S7-300, S7-400)

###### Description

You use the PE command "Query_modes" and the sub-command (modifier) "Get_Mode" to output the attributes of the energy-saving mode which is currently enabled.

###### Calling the PI command "Query_modes" - "Get_Mode"

The call of the command with the instruction "PE_CMD" occurs with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 3 | Call of the PE command "Query_modes" |
| CMD_MODIFIER | 2 | Specification of the command call: Select the sub-command "Get_Mode" to output the status of the mode which is currently enabled. |
| CMD_PARA_LEN | 1 | Length of the CMD_PARA parameter of 1 byte. |
| CMD_PARA | ANY | ANY pointer to the value for PE_MODE_ID. |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| PE_Mode_ID | - 0   "PE_power_off" Mode - 1...254  Energy-saving mode of the PE entity (manufacturer-specific) - 255   "PE_ready_to_operate" Mode | BYTE | ID of the energy-saving mode currently enabled. |
| PE_Mode_Attributes | Bit 0:  - = 0: Only static energy consumer and time values are available. - = 1: Dynamic energy consumer and time values are available.   Bit 1 to 7:  - Reserved | BYTE |  |
| Time_min_Pause <sup>1</sup> | Time difference without date | DWORD | Minimum pause time for the PI mode. The minimum pause time is the sum of the values of the following attributes:  - Time_to_Pause - Time_to_operate - Time_min_length_of_stay   See the description of the "PAUSE_TIME parameter" of the instruction "[PE_START_END: Start and exit energy-saving mode](#pe_start_end-start-and-exit-energy-saving-mode-s7-300-s7-400)". |
| Time_to_Pause <sup>1</sup> | Time difference without date | DWORD | Switch off time: Duration from call of energy-saving mode to start of energy-saving mode (transition duration of PE_ready_to_operate to PE_energy_saving_mode). The switch off time depends on the PE entity. |
| Time_to_operate <sup>1</sup> | Time difference without date | DWORD | Switch on time: Duration of the transition from energy-saving mode (PE_energy_saving_mode) to ready to operate mode (PE_ready_to_operate).  The PE entity calculates the duration dynamically in the output operation. |
| Time_min_length_ of_stay <sup>1</sup> |  | DWORD | Minimum active period of the energy-saving mode on the PE entity. |
| Time_max_length_ of_stay <sup>1</sup> |  | DWORD | Maximum active period of the energy-saving mode on the PE entity. |
| Mode_Power_ Consumption <sup>2</sup> |  | REAL | Power consumption of the PE entity in active energy-saving mode.  Unit: kW |
| Energy_ Consumption_ to_pause <sup>2</sup> |  | REAL | Energy consumption of the PE entity at the transition from the ready to operate mode (PE_ready_to_operate) to the energy-saving mode (PE_energy_saving_mode)  Unit: kWh |
| Energy_ Consumption_ to_operate <sup>2</sup> |  | REAL | Energy consumption of the PE entity at the transition from the energy-saving mode (PE_energy_saving_mode) to the ready to operate mode (PE_ready_to_operate)   Unit: kWh |
| <sup>1</sup> If the duration is infinite, 0xFFFFFFFF will be output. If the duration is zero, "0" will be output.   <sup>2</sup> If the PE entity has no defined energy and power consumption, the "0.0" is output. |  |  |  |

##### PI command "PEM_Status" (S7-300, S7-400)

###### Description

Using PE command "PEM_Status", you can query the currently active energy-saving mode of a PE entity.

###### Calling the PI command "PEM_Status"

The command "PEM_Status" is called with the instruction "PE_CMD" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 4 | Call of PE command "PEM_Status". |
| CMD_MODIFIER | 0 | There are no other specifications of the command call for command "PEM_Status". |
| CMD_PARA_LEN | 0 | Length of the CMD_PARA parameter of 0 bytes. |
| CMD_PARA | irrelevant | - |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| PE_Mode_ID_ Source | - 0   "PE_power_off" mode - 1 to 254   Energy-saving mode of the PE entity (manufacturer-specific) - 255   "PE_ready_to_operate" mode | BYTE | Mode of the PE entity before the PE command is sent. |
| PE_Mode_ID_ Destination | - 0   "PE_power_off" mode - 1 to 254   Energy-saving mode of the PE entity (manufacturer-specific) - 255   "PE_ready_to_operate" mode | BYTE | Mode of the PE entity after a PE command is executed. |
| Time_to_operate | Time difference without date | DWORD | Switch on time: Duration of the transition from energy-saving mode (PE_energy_saving_mode) to ready to operate mode (PE_ready_to_operate).  The PE entity calculates the duration dynamically in the output operation. |
| Remaining_time_to_ destination | Time difference without date | DWORD | Remaining time to switch to another mode. |
| Mode_Power_ Consumption |  | REAL | Power consumption of the PE entity in active energy-saving mode.  Unit: kW |
| Energy_ Consumption_ to_Destination |  | REAL | Energy consumption for the current PI transition  Unit: kWh |
| Energy_ Consumption_ to_operate |  | REAL | Energy consumption of the PE entity at the transition from the energy-saving mode (PE_energy-saving mode) to the ready to operate mode (PE_ready_to_operate)   Unit: kWh |
|  |  |  |  |

##### PI command "PE_Identify" (S7-300, S7-400)

###### Description

Use PE command "PE_Identify" to read the number and description of PE commands supported by the PE entity. The number of specific commands supported depends on the PE entity. As PE_Identify is itself a PE command, at least three supported PE commands will be output upon a positive response: Start_Pause, End_Pause and PE_Identify.

###### Calling the PI command "PE_Identify"

The command "PE_Identify" is called with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 5 | Call of the command "PE_Identify". |
| CMD_MODIFIER | 0 | There are no other specifications of the command call for command "PE_Identify". |
| CMD_PARA_LEN | 0 | Length of the CMD_PARA parameter of 0 bytes. |
| CMD_PARA | irrelevant | - |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| Count <sup>1</sup> | 6 | BYTE | Number of supported PROFIenergy commands |
| Start_Pause | 1 | BYTE | First PE command supported (Service_Request_ID) |
| End_Pause | 2 | BYTE | ... |
| Query_Modes | 3 | BYTE | ... |
| PEM_Status | 4 | BYTE | ... |
| PE_Identify | 5 | BYTE | ... |
| Query_Measurement | 16 | BYTE | Last PE command supported (Service_Request_ID) |
| <sup>1 </sup>The number of commands supported is manufacturer-specific and depends on the PE entity used. The values given are an example of a response frame where all 6 PE commands are supported. |  |  |  |
|  |  |  |  |

##### PI Command "Query_Measurement" - "Get_Measurement_list" (S7-300, S7-400)

###### Description

Use PE command "Query_Measurement" and sub-command (modifier) "Get_measurement_list" to query the specific measured values supported by the PE entity. The supported measured values are output as a list in the data block referenced by the RESPONSE_DATA parameter.

###### Calling the PI command "Query_Measurement" - "Get_Measurement_list"

The command is called with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 16 | Call of the command "Query_Measurement". |
| CMD_MODIFIER | 1 | Specification of the command call: Select the sub-command "Get_Measurement_List" to output a list of supported measured values. |
| CMD_PARA_LEN | 0 | Length of the CMD_PARA parameter of 0 bytes. |
| CMD_PARA | irrelevant | - |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| Count | - | BYTE | Number of measurement IDs |
| reserved | - | BYTE |  |
| ... |  |  |  |
| Measurement_ID | - | WORD | First supported Measurement_ID The Measurement_ID is manufacturer-specific. For more information, refer to the manual of the respective PE entity. |
| Accuracy_Domain | - | BYTE | See"accuracy domain" table. |
| Accuracy_Class | - | BYTE | See "accuracy classes" table. |
| Range | - | REAL | Specifies the scale end value of the measured value (only for accuracy domain 1). The attribute range uses the same unit as defined using attribute Measurement_ID (only one unit is used for each Measurement_ID). |
| ... |  |  |  |
| Measurement_ID | - | WORD | Last supported Measurement_ID |
| Accuracy_Domain | - | BYTE | See"accuracy domain" table. |
| Accuracy_Class | - | BYTE | See "accuracy classes" table. |
| Range | - | REAL | Specifies the scale end value of the measurement value (only for accuracy domain 1). The attribute range uses the same unit as defined using attribute Measurement_ID (only one unit is used for each Measurement_ID). |

###### Accuracy domains

| Accuracy domain | Description |
| --- | --- |
| 0 | Reserved |
| 1 | The accuracy deviation is output in percentages of the scale end value. The percentage of the possible deviation is divided into accuracy classes (see table: accuracy classes of the accuracy domains 1 and 2). |
| 2 | The accuracy deviation is output in percentages of the current measurement value. The percentage of the possible deviation is divided into accuracy classes (see table: accuracy classes of the accuracy domains 1 and 2). |
| 3 | The measuring accuracy adheres to the standard IEC 61557-12.   The function performance classes for performance measurement and monitoring devices (PMD) without external sensors, and the system performance classes for PMD with external sensors, are coded as set out in the "Accuracy classes of accuracy domain 3" table. |
| 4 | The entry of the accuracy adheres to the standard EN 50470-3, chapter 8 (see also table: accuracy classes of accuracy domain 4). |

###### Accuracy classes

Accuracy classes of the accuracy domains 1 and 2

| Accuracy class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meaning** | Reserved | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 1.5% |
|  |  |  |  |  |  |  |  |  |  |
| **Accuracy class** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **&gt;15** |  |
| **Meaning** | 2% | 2.5% | 3% | 5% | 10% | 20% | &gt;20% | Not defined |  |
|  |  |  |  |  |  |  |  |  |  |

Accuracy classes of accuracy domain 3

| Accuracy class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meaning** | Reserved | 0.02 | 0.05 | 0.1 | 0.2 | 0.5 | 1 | 1.5 | 2 |
|  |  |  |  |  |  |  |  |  |  |
| **Accuracy class** | **9** | **10** | **11** | **12** | **13** | **14** | **&gt;13** |  |  |
| **Meaning** | 2.5 | 3 | 5 | 10 | 20 | 20% | Not defined |  |  |
|  |  |  |  |  |  |  |  |  |  |

Accuracy classes of accuracy domain 4

| Accuracy class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | &gt;7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Meaning** | Reserved | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | Not defined |
|  |  |  |  |  |  |  |  |  |

##### PI Command "Query_Measurement" - "Get_Measurement_values" (S7-300, S7-400)

###### Description

Use PE command "Query_Measurement" and sub-command (modifier) "Get_measurement_values" to output a list of measured values supported by the PE entity. The measured values are output as a list in the data block referenced by the RESPONSE_DATA parameter.

###### Calling the PI command "Query_Measurement" - "Get_Measurement_values"

The command is called with the instruction "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)" with the following parameters:

| Parameter | Value | Description |
| --- | --- | --- |
| CMD | 16 | Call of the command "Query_Measurement". |
| CMD_MODIFIER | 2 | Specification of the command call: Select the command "Get_Measurement_Values" to output a list of supported measurement values. |
| CMD_PARA_LEN | 0 | Depends on the number of measurement values. The length of the parameters results from the attribute count and the sum of the lengths of the attributes for the transferred measurement values. |
| CMD_PARA | ANY | ANY pointer to data structure with list of measured values to be queried (see "CMD_PARA parameter"). |

**Parameter** 
**CMD_PARA**

The structure specified with the ANY pointer at the CMD_PARA parameter must have the following setup:

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| Count | - | BYTE | Number of measured values (Measurement-IDs) |
| reserved | 0 | BYTE | Not used |
| Measurement_ID | - | WORD | First measured value queried |
| ... |  |  |  |
| Measurement_ID | - | WORD | Last measured value queried |

###### Response frame (Service Data Response)

The following response frame data of the PE entity is written to the data block that is referenced at parameter RESPONSE_DATA (see "[PE_CMD](#pe_cmd-start-and-exit-energy-saving-mode-read-out-status-information-s7-300-s7-400)"):

| Attribute | Value | Data type | Description |
| --- | --- | --- | --- |
| Count <sup>1</sup> | - | BYTE | Number of measured values (Measurement-IDs) |
| reserved | 0 | BYTE | Not used |
|  |  |  |  |
| Length_of_Structure | 2 to 65535 | WORD | Length of the structure in bytes |
| Measurement_Data_Structure_ID | 1 = simple value | BYTE | Defines the following structure. |
| Measurement_ID | 0 to 65535 | WORD | ID of the supported measurement value. |
| Status_of_ Measurement_Value | 1 to 3 | BYTE | Status of the measurement value:  - 1: Valid - 2: Not supported - 3: Invalid |
| Transmission_Data_Type | - | REAL |  |
| End_of_demand | - | TOD | Optional time stamping with data type TimeOfDay. |
| ... |  |  |  |
| Length_of_Structure | - | WORD | Length of the structure in bytes |
| Measurement_Data_Structure_ID | - | BYTE | Defines the following structure. |
| Measurement_ID | - | WORD | ID of the supported measurement value. |
| Status_of_Measurement_Value | - | BYTE | Status of the measurement value:  - 1: Valid - 2: Not supported - 3: Invalid |
| Transmission_Data_Type | - | REAL |  |
| End_of_demand | - | TOD | Optional time stamping with data type TimeOfDay. |
| <sup>1</sup> If the data length of the measurement values queried exceeds the size of the PDU (Protocol Data Unit) of the protocol layer, the data will not be completely transferred and only the supported measurement values will be output. |  |  |  |

### iDevice / iSlave (S7-300)

This section contains information on the following topics:

- [PE_I_DEV: Control PROFIenergy commands in the I-Device (S7-300)](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)
- [Auxiliary blocks of the instruction PE_I_DEV (S7-300)](#auxiliary-blocks-of-the-instruction-pe_i_dev-s7-300)

#### PE_I_DEV: Control PROFIenergy commands in the I-Device (S7-300)

##### Description

The instruction "PE_I_DEV" is used to process the PROFIenergy profile in the intelligent IO device (iDevice). The functions which are executed by the firmware in standard PROFIenergy-compatible IO devices, such as the ET 200S, are implemented in the iDevice by the instruction "PE_I_DEV" and the corresponding auxiliary blocks:

- The instruction "PE_I_DEV" is called cyclically by the user program of the iDevice and receives all PROFIenergy commands.
- The PROFIenergy response is generated by configuring an auxiliary block. The response in the pause is fully programmable. The response data must be provided within 10 seconds; otherwise, "State conflict 0x80B5" will occur at the STATUS parameter of the instruction in the IO controller.

No specific knowledge of the PROFIenergy standard is required to use the instruction.

##### PROFIenergy auxiliary blocks (PE auxiliary blocks)

The PE auxiliary blocks are used to generate the response frame. Enter the response data (in plain text) at the input parameters of the relevant block.

- For each PROFIenergy command, there is a corresponding auxiliary block for a positive response:

  - PE command "Start_Pause": [PE_Start_RSP](#pe_start_rsp-generate-answer-to-command-at-start-of-pause-s7-300)
  - PE command "End_Pause": [PE_End_RSP](#pe_end_rsp-generate-answer-to-command-at-end-of-pause-s7-300)
  - PE command "Query_modes" - "List_Energy_Saving_Modes": [PE_List_Modes_RSP](#pe_list_modes_rsp-generate-queried-energy-savings-modes-as-answer-s7-300)
  - PE command "Query_modes" - "Get_Mode": [PE_Get_Mode_RSP](#pe_get_mode_rsp-generate-queried-energy-data-as-answer-s7-300)
  - PE command "PEM_Status": [PE_PEM_Status_RSP](#pe_pem_status_rsp-generate-pem-status-as-answer-s7-300)
  - PE command "PE_Identify": [PE_Identify_RSP](#pe_identify_rsp-generate-supported-profienergy-commands-as-answer-s7-300)
  - PE command "Query_Measurement" - "Get_Measurement_list": [PE_Measurement_List_RSP](#pe_measurement_list_rsp-generate-list-of-supported-measured-values-as-answer-s7-300)
  - PE command "Query_Measurement" - "Get_Measurement_values": [PE_Measurement_Value_RSP](#pe_measurement_value_rsp-generate-queried-measured-values-as-answer-s7-300)
- Irrespective of the PROFIenergy command, there is an additional shared auxiliary block for a negative response (see [PE_Error_RSP](#pe_error_rsp-generate-negative-answer-to-command-s7-300)).

##### Interconnection of the auxiliary blocks

The instruction "PE_I_DEV" and the auxiliary blocks are coordinated. Some of the parameters are simply interconnected. The diagram below shows which of the parameters need to be interconnected.

![Interconnection of the auxiliary blocks](images/44980445451_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the instruction "PE_I_DEV":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RESET | Input | BOOL | I, Q, M, D, L | Resets the instruction. |
| ID | Input | DWORD | I, Q, M, D, L or constant | Address of the iDevice  The address may be taken from the hardware configuration. |
| VALID | Input | BOOL | I, Q, M, D, L | The response data for the PROFIenergy controller is ready and can be sent. |
| CMD_PARA | Output | ANY | I, Q, M, D, L | Parameters for:  - Get mode: PE_mode_ID - Get measurement values: List of Measurement_IDs (list of IDs of the tags to be read; either one tag or multiple tags may be read at any given time).   Maximum length: 234 bytes |
| DATA_ERRORRSP | InOut | ANY | I, Q, M, D, L | Pointer to the data area containing the acknowledgment data for the PROFIenergy controller.  This must correspond to the pointer which is also used with the auxiliary blocks. |
| INDEX | Output | INT | I, Q, M, D, L | Data record number of the PROFIenergy record (set at 0x80A0) |
| CMD | Output | INT | I, Q, M, D, L | Service-Request-ID of the PROFIenergy command in accordance with the PROFIenergy profile (see "CMD and CMD_MODIFIER parameters").  Further PE commands (Service-Request-IDs) are possible following extensions of the PROFIenergy profile. |
| CMD_ MODIFIER | Output | INT | I, Q, M, D, L | PROFIenergy sub-command:  - Only when CMD=3 or CMD=16; see "CMD and CMD_MODIFIER parameters". - For all other commands: "0".   Further sub-commands are possible following extensions of the PROFIenergy profile. |
| NEW | Output | BOOL | I, Q, M, D, L | New data available from the PROFIenergy controller. |
| ERROR | Output | BOOL | I, Q, M, D, L | Command completed with error. |
| STATUS | Output | DWORD | I, Q, M, D, L | Error information (see "STATUS parameter"). |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameters CMD and CMD_MODIFIER

| CMD | CMD_ MODIFIER | PROFIenergy command | Description |
| --- | --- | --- | --- |
| 01 | 0 | Start_Pause | Start energy-saving mode or switch to a different energy-saving mode. |
| 02 | 0 | End_Pause | End energy-saving mode. |
| 03 | 1 | Query_Modes - List energy saving Modes | Output the energy-saving modes supported. |
| 2 | Query_Modes - Get Mode | Output attributes of the energy-saving mode currently enabled. |  |
| 04 | 0 | PEM_Status | Query status of energy-saving mode. |
| 05 | 0 | PE_Identify | Read out the number and description of PE commands supported. |
| 16 | 1 | Query_Measurement - Get_Measurement_List | List of measured values supported by the PE entity. |
| 2 | Query_Measurement - Get_Measurement_Values | Output of the measured values of the PE entity. |  |

##### STATUS parameter

Error information is output at the STATUS output parameter. If it is interpreted as ARRAY[1...4] of BYTE, the error information has the following structure:

| Field element | Name | Meaning |
| --- | --- | --- |
| STATUS[1] | Function_Num | Cause of the error  - B#16#**00**: No error - B#16#**DE**: Error during reading of data record - B#16#**DF**: Error during writing of data record - B#16#**C0**: Error message from the instruction "PE_I_DEV" or from the internal communication instructions ""PRVREC" and "RCVREC". |
| STATUS[2] | Error_Decode | Location of the error ID  - **80**: DPV1 error as defined in IEC 61158-6 or application-specific |
| STATUS[3] | Error_Code_1 | Error ID (when Error_Decode = **80**):  - **B1**: Write length error (error in write length or insufficient length information with the data type ANY). |
| STATUS[4] | Error_Code_2 | For PROFINET errors: Output of IO controller error message If no PROFINET error has occurred, the value in STATUS[4] = "0". |

> **Note**
>
> **Error messages of the "PRVREC" and "RCVREC" instructions**
>
> The instruction "PE_I_DEV" uses the instructions "[PRVREC](#prvrec-make-data-record-available-s7-300-s7-400)" and "[RCVREC](#rcvrec-receive-data-record-s7-300-s7-400)" for communication. Error messages for these instructions are output in the field elements STATUS[1] to STATUS[4].
>
> Please see the description of the corresponding [STATUS](#parameter-status-s7-300-s7-400) parameter for an explanation of the error codes of the "PRVREC" and "RCVREC" instructions.

---

**See also**

[RDREC: Read data record (S7-300, S7-400)](#rdrec-read-data-record-s7-300-s7-400)
  
[WRREC: Write data record (S7-300, S7-400)](#wrrec-write-data-record-s7-300-s7-400)

#### Auxiliary blocks of the instruction PE_I_DEV (S7-300)

This section contains information on the following topics:

- [PE_Error_RSP: Generate negative answer to command (S7-300)](#pe_error_rsp-generate-negative-answer-to-command-s7-300)
- [PE_Start_RSP: Generate answer to command at start of pause (S7-300)](#pe_start_rsp-generate-answer-to-command-at-start-of-pause-s7-300)
- [PE_End_RSP: Generate answer to command at end of pause (S7-300)](#pe_end_rsp-generate-answer-to-command-at-end-of-pause-s7-300)
- [PE_List_Modes_RSP: Generate queried energy savings modes as answer (S7-300)](#pe_list_modes_rsp-generate-queried-energy-savings-modes-as-answer-s7-300)
- [PE_Get_Mode_RSP: Generate queried energy data as answer (S7-300)](#pe_get_mode_rsp-generate-queried-energy-data-as-answer-s7-300)
- [PE_PEM_Status_RSP: Generate PEM status as answer (S7-300)](#pe_pem_status_rsp-generate-pem-status-as-answer-s7-300)
- [PE_Identify_RSP: Generate supported PROFIenergy commands as answer (S7-300)](#pe_identify_rsp-generate-supported-profienergy-commands-as-answer-s7-300)
- [PE_Measurement_List_RSP: Generate list of supported measured values as answer (S7-300)](#pe_measurement_list_rsp-generate-list-of-supported-measured-values-as-answer-s7-300)
- [PE_Measurement_Value_RSP: Generate queried measured values as answer (S7-300)](#pe_measurement_value_rsp-generate-queried-measured-values-as-answer-s7-300)

##### PE_Error_RSP: Generate negative answer to command (S7-300)

###### Description

The auxiliary block "PE_Error_RSP" (Response with failure) generates a negative response if the command requested is not supported (either in general or temporarily). Response generation does not depend on the command requested.

###### Parameter

The following table shows the parameters of the "PE_Error_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| ERROR_CODE | Input | BYTE | I, Q, M, D, L or constant | Error number |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_Start_RSP: Generate answer to command at start of pause (S7-300)

###### Description

The auxiliary block "PE_Start_RSP" (Start Pause) generates the response to the PE command [Start_Pause](#pi-command-start_pause-s7-300-s7-400). The instruction returns the energy-saving mode to which the device has switched (PE_MODE_ID parameter).

If the response differs depending on the length of the pause, you can return this fact in the feedback on the energy-saving mode (PE_Mode_ID = 1 for a brief pause, PE_Mode_ID = 2 for a longer pause, etc.).

###### Parameter

The following table shows the parameters of the "PE_Start_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| PE_MODE_ID | Input | BYTE | I, Q, M, D, L or constant | PE mode that the process assumes |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_End_RSP: Generate answer to command at end of pause (S7-300)

###### Description

The auxiliary block "PE_End_RSP" generates the response to the PE command [End_Pause](#pi-command-end_pause-s7-300-s7-400). The response returned is the time required to switch from the current mode to "Ready_To_Operate" mode.

###### Parameter

The following table shows the parameters of the "PE_End_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| Time_to_Operate | Input | DWORD | I, Q, M, D, L or constant | Time required to switch from the current mode to "Ready_To_Operate". |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_List_Modes_RSP: Generate queried energy savings modes as answer (S7-300)

###### Description

The auxiliary block "PE_List_Modes_RSP" generates the response to the PE command [List_Energy_Saving_Modes](#pi-command-query_modes---list_energy_saving_modes-s7-300-s7-400). The response generated includes the number and the IDs of energy-saving modes supported.

###### Parameter

The following table shows the parameters of the "PE_List_Modes_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| CMD_MODIFIER | Input | INT | I, Q, M, D, L or constant | PROFIenergy sub-command (evaluated only if CMD=3, or CMD=16). The parameter must be interconnected with the CMD_MODIFIER output parameter of the "PE_I_DEV" instruction. |
| Number_of_PE_ Mode_IDs | Input | BYTE | I, Q, M, D, L or constant | Number of energy-saving modes supported.  Permitted values: 1 to 254 |
| PE_MODE_ID | Input | ANY | I, Q, M, D, L | Points to the area in which the IDs of the energy-saving modes supported (PE_Mode_ID) are stored.  Valid range: 1 to 254. |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_Get_Mode_RSP: Generate queried energy data as answer (S7-300)

###### Description

The auxiliary block "PE_Get_Mode_RSP" generates the response to the command [Get_Mode](#pi-command-query_modes---get_mode-s7-300-s7-400). The response frame contains the time, performance, or energy data of an energy-saving mode.

###### Parameter

The following table shows the parameters of the "PE_Get_Mode_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| CMD_MODIFIER | Input | INT | I, Q, M, D, L or constant | PROFIenergy sub-command (evaluated only if CMD=3, or CMD=16). The parameter must be interconnected with the CMD_MODIFIER output parameter of the "PE_I_DEV" instruction. |
| PE_Mode_ID | Input | BYTE | I, Q, M, D, L or constant | ID of the energy-saving mode currently enabled. |
| PE_Mode_Attributes | Input | BYTE | I, Q, M, D, L or constant | Additional information regarding energy saving mode |
| Time_min_Pause | Input | DWORD | I, Q, M, D, L or constant | Minimum pause duration for this PE energy-saving mode.  This is the sum of the following three parameters:  - Time_to_Pause - Time_to_operate - Time_min_length_of_stay |
| Time_to_Pause | Input | DWORD | I, Q, M, D, L or constant | Time between the edge at the START parameter (see "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)") and the requested PE energy-saving mode being reached. |
| Time_to_Operate | Input | DWORD | I, Q, M, D, L or constant | Maximum switch-on time to "PE_ready_to_operate". The "Time_to_operate" parameter can be used directly for the relevant calculations. The value may be a static maximum, or be calculated dynamically by the PE entity. |
| Time_min_Lenght_ of_stay | Input | DWORD | I, Q, M, D, L or constant | Minimum dwell time of the PE entity in this PE mode. |
| Time_max_Lenght_of_stay | Input | DWORD | I, Q, M, D, L or constant | Maximum dwell time of the PE entity in this PE mode. |
| Mode_Power_ Consumption | Input | DWORD | I, Q, M, D, L or constant | Energy consumption in the current PE mode in [kW]. |
| Energy_Consum_ to_Pause | Input | DWORD | I, Q, M, D, L or constant | Energy consumption from "PE_ready_to_operate" to the current PE mode in [kWh]. |
| Energy_Consum_ to_operate | Input | DWORD | I, Q, M, D, L or constant | Energy consumption from the current PE mode to "PE_ready_to_operate" in [kWh]. |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_PEM_Status_RSP: Generate PEM status as answer (S7-300)

###### Description

The auxiliary block "PE_PEM_Status_RSP" generates the response to the command [PEM_Status](#pi-command-pem_status-s7-300-s7-400).

###### Parameter

The following table shows the parameters of the "PE_PEM_Status_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| PE_MODE_ID_ Source | Input | BYTE | I, Q, M, D, L or constant | Source and Destination for PEM_STATUS.  Values:  - 0x00: PE_POWER_OFF - 0x01 – 0xFE: manufacturer-specific - 0xFF: PE_READY_TO_OPERATE |
| PE_MODE_ID_ Destination | Input | BYTE | I, Q, M, D, L or constant |  |
| Time_to_Operate<sup>1</sup> | Input | DWORD | I, Q, M, D, L or constant | Maximum switch-on time to "PE_ready_to_operate".  "Time_to_operate" can be used directly for the relevant calculations. The value may be a static maximum, or be calculated dynamically by the PE entity. |
| Remaining_time_ to_destination<sup>1</sup> | Input | DWORD | I, Q, M, D, L or constant | Optional: Time remaining until the requested PE mode. Dynamic value or static maximum value |
| Mode_Power_ Consumption<sup>2</sup> | Input | DWORD | I, Q, M, D, L or constant | Energy consumption in the current PE mode in [kW]. |
| Energy_ Consumption_ to_Destination<sup>2</sup> | Input | DWORD | I, Q, M, D, L or constant | Energy consumption in the time until the requested PE mode in [kW]. |
| Energy_ Consumption_ to_operate<sup>2</sup> | Input | DWORD | I, Q, M, D, L or constant | Energy consumption from the current PE mode to "PE_ready_to_operate" in [kWh]. |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |
| <sup>1</sup> If the time period is unlimited, the maximum value "0xFFFFFFFF" can be specified. If the time period is "Zero", "0x00" can be used.   <sup>2</sup> If no energy consumption value has been defined, "0.0" can be specified. |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_Identify_RSP: Generate supported PROFIenergy commands as answer (S7-300)

###### Description

The auxiliary block "PE_Identify_RSP" generates the response to the command [PE_Identify](#pi-command-pe_identify-s7-300-s7-400). In the response to the command, specify which PROFIenergy commands are supported. Please note that PE_IDENTIFY is itself a PE command and has to be included in the response.

###### Parameter

The following table shows the parameters of the "PE_Identify_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| Start_Pause | Input | BOOL | I, Q, M, D, L or constant | One parameter for each of the relevant PROFIenergy commands:  - 0: PE command is not supported - 1: PE command is supported |
| End_Pause | Input | BOOL | I, Q, M, D, L or constant |  |
| Query_Modes | Input | BOOL | I, Q, M, D, L or constant |  |
| PEM_Status | Input | BOOL | I, Q, M, D, L or constant |  |
| PE_Identify | Input | BOOL | I, Q, M, D, L or constant |  |
| Query_ Measurement | Input | BOOL | I, Q, M, D, L or constant |  |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_Measurement_List_RSP: Generate list of supported measured values as answer (S7-300)

###### Description

The auxiliary block "PE_Measurement_List_RSP" generates the response to the command [Get_measurement_list](#pi-command-query_measurement---get_measurement_list-s7-300-s7-400). In the response, specify which measured values (Measurement-IDs) are supported.

###### Parameter

The following table shows the parameters of the "PE_Measurement_List_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| CMD_MODIFIER | Input | INT | I, Q, M, D, L or constant | PROFIenergy sub-command (evaluated only if CMD=3, or CMD=16). The parameter must be interconnected with the CMD_MODIFIER output parameter of the "PE_I_DEV" instruction. |
| Count | Input | BYTE | I, Q, M, D, L or constant | Number of measured values supported (measurement IDs) |
| Measurement_ List | Input | ANY | D | Pointer to the array with the Measurement_IDs supported.  For information on the structure of the array in accordance with the PROFIenergy profile, see: [PI Command "Query_Measurement" - "Get_Measurement_list"](#pi-command-query_measurement---get_measurement_list-s7-300-s7-400) |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### PE_Measurement_Value_RSP: Generate queried measured values as answer (S7-300)

###### Description

The auxiliary block "PE_Measurement_Value_RSP" generates the response to the command [Get_measurement_values](#pi-command-query_measurement---get_measurement_values-s7-300-s7-400). In the response, return the values of the requested measurements.

###### Parameter

The following table shows the parameters of the "PE_Measurement_Value_RSP" auxiliary block:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PE_I_DEV_NEW | Input | BOOL | I, Q, M, D, L or constant | The parameter must be interconnected with the NEW output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The auxiliary block is only processed if the parameter value is set to "1". |
| CMD | Input | INT | I, Q, M, D, L or constant | Service-Request-ID of the PROFIenergy command   The parameter must be interconnected with the CMD output parameter of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| CMD_MODIFIER | Input | INT | I, Q, M, D, L or constant | PROFIenergy sub-command (evaluated only if CMD=3, or CMD=16). The parameter must be interconnected with the CMD_MODIFIER output parameter of the "PE_I_DEV" instruction. |
| Count | Input | BYTE | I, Q, M, D, L or constant | Number of measured values (Measurement_Values). |
| Measurement_Values | Input | ANY | D | Pointer to the array with the measured values (Measurement_IDs).  For information on the structure of the array in accordance with the PROFIenergy profile, see [PI Command "Query_Measurement" - "Get_Measurement_values"](#pi-command-query_measurement---get_measurement_values-s7-300-s7-400) |
| ACTIVATE | InOut | BOOL | I, Q, M, D, L | The instruction copies the input parameters to the DATA_ERROR_RSP data area at a rising edge at input ACTIVATE. The parameter is then reset by the instruction.  The parameter must be set within 10 seconds after a rising edge is detected at parameter NEW of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. |
| VALID | InOut | BOOL | I, Q, M, D, L | The parameter must be interconnected with the VALID input of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction.   The auxiliary block sets the parameter as soon as the response data for the PROFIenergy controller is available and ready for transmission. |
| DATA_ ERRORRSP | InOut | ANY | D | Pointer on the data area in which the response data is stored. The parameter is identical to the pointer for DATA_ERRORRSP of the "[PE_I_DEV](#pe_i_dev-control-profienergy-commands-in-the-i-device-s7-300)" instruction. The addressed data area contains the complete PROFIenergy frame.   Minimum length: 244 bytes |
| ERROR | Output | BOOL | I, Q, M, D, L | - "0": No error - "1": Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | - "0": No error - "0x80B1": Error in ANY setting, e.g. incorrect range |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

## Module parameter assignment (S7-300, S7-400)

This section contains information on the following topics:

- [Writing and reading data records (S7-300, S7-400)](#writing-and-reading-data-records-s7-300-s7-400)
- [RD_DPAR: Read module data record (S7-300, S7-400)](#rd_dpar-read-module-data-record-s7-300-s7-400)
- [RD_DPARA: Read module data record asynchronously (S7-300)](#rd_dpara-read-module-data-record-asynchronously-s7-300)
- [PARM_MOD: Transfer module data records (S7-300, S7-400)](#parm_mod-transfer-module-data-records-s7-300-s7-400)
- [RD_DPARM: Read data record from configured system data (S7-400)](#rd_dparm-read-data-record-from-configured-system-data-s7-400)
- [WR_PARM: Write module data record (S7-300, S7-400)](#wr_parm-write-module-data-record-s7-300-s7-400)
- [WR_DPARM: Transfer data record (S7-300, S7-400)](#wr_dparm-transfer-data-record-s7-300-s7-400)

### Writing and reading data records (S7-300, S7-400)

#### Principle

Some modules have a write-only system data area to which your program can transfer data records. This area contains data records with numbers from 0 to a maximum of 240. Not every module contains all of the data records (see following table).

Modules can also have a read-only system data area in which your program can read data records. This area contains data records with numbers from 0 to a maximum of 240. Not every module contains all of the data records (see following table).

> **Note**
>
> There are modules that have both system data areas. These are physically separate areas and the only thing they have in common is their logical structure.

#### Write-only system data area

The following table shows the structure of the write-only system data area. This table also shows how the permitted size of the individual data records and which instructions can be used to write them.

| Data record  number | Contents | Size | Restriction | Can be written with instruction |
| --- | --- | --- | --- | --- |
| 0 | Parameter | For S7-300:  2 to 14 Bytes | Can only be written  by an S7-400 | [WR_DPARM](#wr_dparm-transfer-data-record-s7-300-s7-400)    [PARM_MOD](#parm_mod-transfer-module-data-records-s7-300-s7-400) |
| 1 | Parameter | For S7-300:  2 to 14 Bytes  (Data records 0 and 1 together  have a total of exactly 16  bytes.) | - | [WR_PARM](#wr_parm-write-module-data-record-s7-300-s7-400)    [WR_DPARM](#wr_dparm-transfer-data-record-s7-300-s7-400)    [PARM_MOD](#parm_mod-transfer-module-data-records-s7-300-s7-400) |
| 2 to 127 | User data | Each ≤ 240 bytes | - | [WR_PARM](#wr_parm-write-module-data-record-s7-300-s7-400)    [WR_DPARM](#wr_dparm-transfer-data-record-s7-300-s7-400)    [PARM_MOD](#parm_mod-transfer-module-data-records-s7-300-s7-400)    [WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400) |
| 128 to 240 | Parameter | Each ≤ 240 bytes | - | [WR_PARM](#wr_parm-write-module-data-record-s7-300-s7-400)    [WR_DPARM](#wr_dparm-transfer-data-record-s7-300-s7-400)    [PARM_MOD](#parm_mod-transfer-module-data-records-s7-300-s7-400)    [WR_REC](#wr_rec-write-data-record-to-io-s7-300-s7-400) |

#### Read-only system data area

The following table shows the structure of the read-only system data area. This table also shows the permitted size of the individual data records and which instructions can be used to read them.

| Data record   number | Contents | Size | Can be read with instruction |
| --- | --- | --- | --- |
| 0 | Module-specific diagnostic data (set as standard for the entire  system) | 4 bytes | [RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)   (SZL_ID00B1H)   [RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400) |
| 1 | Channel-specific  diagnostic data  (incl. data record 0) | - For S7-300:   16 bytes - with S7-400:   4 to 220 Bytes | [RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)  (SZL_ID00B2H and 00B3H) [RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400) |
| 2 to 127 | User data | Each ≤ 240 bytes | [RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400) |
| 128 to 240 | Diagnostic data | Each ≤ 240 bytes | [RD_REC](#rd_rec-read-data-record-from-io-s7-300-s7-400) |

#### System resources

If you start several asynchronous data record transfers one after the other with only short intervals between them, the allocation of system resources by the operating system ensures that all the jobs are executed and that they do not interfere with each other.

If the limits of the system resources are reached, this is indicated in RET_VAL. You can remedy this temporary error situation by simply repeating the job.

The maximum number of "simultaneously" active jobs of a single instruction type depends on the CPU.

### RD_DPAR: Read module data record (S7-300, S7-400)

#### Description

You use the instruction to read the data record with the number INDEX of the addressed component from the configured system data. This may be a module in a central rack or a distributed component (PROFIBUS DP or PROFINET IO).

The value TRUE for the output parameter VALID indicates that the data record was successfully transferred to the destination area RECORD. In this case, the LEN output parameter contains the length of the read data in bytes.

If an error has occurred during transfer of the data record, this is indicated by the output parameter ERROR . In this case, the output parameter STATUS contains the error information.

#### Functional description

The "RD_DPAR" instruction works asynchronously, that is, its execution extends over multiple calls. You start the data record transfer by calling "RD_DPAR" with REQ = 1.

The output parameter BUSY and bytes 2 and 3 of the output parameter STATUS show the status of the job. Bytes 2 and 3 of STATUS match the output parameter RET_VAL of the instructions that operate asynchronously.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The transfer of the data record is complete when the output parameter BUSY has the value FALSE.

#### Parameter

The following table shows the parameters of the instruction "RD_DPAR":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Read request |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Any logical address of the module  In bit 15 you indicate whether an input address (bit 15 = 0) or an output address (bit 15 = 1) is present. |
| INDEX | Input | INT | I, Q, M, D, L or constant | Data record number |
| VALID | Output | BOOL | I, Q, M, D, L | New data record was received and is valid |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The job is not yet complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | ERROR = 1: An error occurred during the reading process. |
| STATUS | Output | DWORD | I, Q, M, D, L | - Call ID (bytes 2 and 3) or error code - Byte 1: B#16#00, if no error. Otherwise function ID from DPV1-PDU: In the case of error for data record reading B#16#DE, in the case of error for data record writing B#16#DF. If no DPV1 protocol element is used: B#16#C0. - Byte 4: Manufacturer-specific error ID expansion |
| LEN | Output | INT | I, Q, M, D, L | Length of the read data record information |
| RECORD | InOut | ANY | I, Q, M, D, L | Destination area for the read data record  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter ERROR and STATUS

See also: [PARM_MOD: Transfer module data records](#parm_mod-transfer-module-data-records-s7-300-s7-400).

### RD_DPARA: Read module data record asynchronously (S7-300)

#### Description

You use the instruction to read the data record with the number RECNUM of a selected module from the configured system data. The read data record is entered into the destination area spanned by the RECORD parameter.

#### Functional description

The "RD_DPARA" instruction works asynchronously, that is, its execution extends over multiple calls. You start the job by calling the instruction with REQ = 1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

#### Parameter

The following table shows the parameters of the instruction "RD_DPARA":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Read request |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Any address of the module. For an output address, the most significant bit must be set. |
| RECNUM | Input | BYTE | I, Q, M, D, L or constant | Data record number (permitted values: 0 to 240) |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code.  If no error occurred during the transmission, the following two cases are distinguished:  - RET_VAL contains the length of the actually read data record in bytes if the destination area is larger than the read data record. - RET_VAL contains "0" if the length of the read data record is equal to the length of the destination area. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The job is not yet complete. |
| RECORD | Output | ANY | I, Q, M, D, L | Destination area for the data record read. Only the BYTE data type is permitted.  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

See also: [PARM_MOD: Transfer module data records](#parm_mod-transfer-module-data-records-s7-300-s7-400).

### PARM_MOD: Transfer module data records (S7-300, S7-400)

#### Description

You use the instruction "PARM_MOD" to transfer all configured data records of a module to the module. With this instruction, it is irrelevant whether the data records are static or dynamic.

#### Parameter

The following table shows the parameters of the "PARM_MOD" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ= 1: Write request |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed module, the area identifier of the lower address must be specified. If the addresses are identical, specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical base address of the module. For  a mixed module, the lower of the two  addresses must be specified. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The writing process is not yet complete. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Error information

The "real" error information (error codes W#16#8xyz) can be divided into two classes:

- Temporary errors (error codes W#16#80A2 to 80A4, 80Cx):

  This type of error can possibly be eliminated without user action, meaning it is helpful to call the instruction again (multiple calls, if necessary).

  Example of a temporary error: Resources required are currently in use (W#16#80C3).
- Permanent errors (error codes W#16#809x, 80A1, 80Bx, 80Dx):

  This type of error does not correct itself. Retries to call the instruction will only be successful after the error has been eliminated.

  Example of a permanent error: Incorrect length of the data record to be transferred (W#16#80B1).

  > **Note**
  >
  > If you transfer data records to a DPV1 slave with the WR_PARM, WR_DPARM or PARM_MOD instruction and if this slave operates in DPV1 mode, the DP master evaluates the error information it has received from this slave as follows:
  >
  > If the error information lies within the range from W#16#8000 to W#16#80FF or W#16#F000 to W#16#FFFF, the DP master passes the error information to the instruction. If the error information is outside this range, the DP master passes the value W#16#80A2 to the instruction and suspends the slave.

Displays for the "[RD_DPARM](#rd_dparm-read-data-record-from-configured-system-data-s7-400)", "[WR_PARM](#wr_parm-write-module-data-record-s7-300-s7-400)", "[WR_DPARM](#wr_dparm-transfer-data-record-s7-300-s7-400)" and "PARM_MOD" instructions

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation | Restriction |
| --- | --- | --- |
| 0000 | No error | - |
| 7000 | First call with REQ=0: No data transfer active; BUSY has the value 0. | - |
| 7001 | First call with REQ=1: Data transfer triggered; BUSY has the value "1". | Distributed I/O |
| 7002 | Intermediate call (REQ  irrelevant): Data transfer already active; BUSY has the value "1". | Distributed I/O |
| 8090 | Specified logical base address invalid: There is no  assignment in SDB1/SDB2x or there is no base address. | - |
| 8092 | A type other than BYTE is specified in the ANY reference. | Only with S7-400 for  [RD_DPARM](#rd_dparm-read-data-record-from-configured-system-data-s7-400)  and [WR_PARM](#wr_parm-write-module-data-record-s7-300-s7-400) |
| 8093 | This instruction is not permitted for the modules selected withLADDR and IOID. (Permitted are S7-300 modules for an S7-300, S7-400 modules for an  S7-400, S7-DP modules for an S7-300 and S7-400.) | - |
| 80A1 | Negative acknowledgment when sending the data record to  the module (the module was removed or became defective  during transfer). | <sup>1)</sup> |
| 80A2 | DP protocol error at layer 2, possibly hardware/interface fault  in DP slave. | Distributed I/O 1) |
| 80A3 | DP protocol error with user interface/user. | Distributed I/O 1) |
| 80A4 | Communication on the communication bus disrupted | Error occurred between the  CPU and external DP  interface module 1) |
| 80B0 | Instruction for module type not possible, or module does not recognize  the data record. | <sup>1)</sup> |
| 80B1 | The length of the data  record to be sent is  incorrect. For [RD_DPARM](#rd_dparm-read-data-record-from-configured-system-data-s7-400): The length of the destination area  spanned by RECORD is too short. | - |
| 80B2 | The configured slot is  not occupied. | <sup>1)</sup> |
| 80B3 | Actual module type does not match the specified module  type in SDB1. | <sup>1)</sup> |
| 80C1 | The data of the previous write job on the module for the same data record have not yet been processed by the module. | <sup>1)</sup> |
| 80C2 | The module is currently processing the maximum possible  number of jobs for a CPU. | <sup>1)</sup> |
| 80C3 | The required resources (memory, etc.) are currently  occupied. |  |
| 80C4 | Internal temporary error. Job could not be carried out.  Repeat the job. If this error occurs often, check your installation for sources of electrical interference. | <sup>1)</sup> |
| 80C5 | Distributed I/O not available or deactivated. | Distributed I/O <sup>1)</sup> |
| 80C6 | Data record transfer stopped due to priority class abort (restart or background) | Distributed I/O <sup>1)</sup> |
| 80D0 | No entry for the  module in the  corresponding SDB. | - |
| 80D1 | The data record number is not configured in the  corresponding SDB for the module (data record numbers &gt;  241 are rejected). | - |
| 80D2 | The module cannot be assigned parameters according to its type identifier. | - |
| 80D3 | The SDB cannot be accessed since it does not exist. | - |
| 80D4 | SDB structure error: The SDB internal pointer points to a  value outside the SDB. | For S7-300 only |
| 80D5 | The data record is static. | With "[WR_PARM](#wr_parm-write-module-data-record-s7-300-s7-400)" only |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) | - |
| <sup>1) </sup>does not occur in "RD_DPARM" |  |  |

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

### RD_DPARM: Read data record from configured system data (S7-400)

#### Description

You use instruction to read the data record with the number RECNUM of the addressed module from the configured system data. The read data record is entered into the destination area spanned by the RECORD parameter.

#### Parameter

The following table shows the parameters of the instruction "RD_DPARM":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed module, the area identifier of the lower address must be specified. If the addresses are identical, specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical base address of the module. For a mixed module, the lower of the two addresses must be specified. |
| RECNUM | Input | BYTE | I, Q, M, D, L or constant | Data record number (permitted values: 0 to 240) |
| RET_VAL | Return | INT | I, Q, M, D, L | Length of the data record read in bytes if  the read data record fits in the destination area  and no error occurred in the transfer.  If an error occurs while the instruction is  being executed, the return value contains an error code. |
| RECORD | Output | ANY | I, Q, M, D, L | Destination area for the data record read. Only the BYTE data type is permitted. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

See also: [PARM_MOD: Transfer module data records](#parm_mod-transfer-module-data-records-s7-300-s7-400).

### WR_PARM: Write module data record (S7-300, S7-400)

#### Description

You use the instruction to transfer the data record RECORD to the addressed module. Parameters transferred to the module do not overwrite parameters created during configuration.

#### Requirements

The data record to be transferred must not be static. The information concerning which data records of a module are static is provided in the module description.

#### Parameters

The following table shows the parameters of the instruction "WR_PARM":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Write request |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed module, the area identifier of the lower address must be specified. If the addresses are identical, specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical base address of the module. For a mixed module, the lower of the two addresses must be specified. |
| RECNUM | Input | BYTE | I, Q, M, D, L or constant | Data record number |
| RECORD | Input | ANY | I, Q, M, D, L | Data record  Note: Note that for S7-300 CPUs the parameter RECORD always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The writing process is not yet complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RECORD

The data to be transferred are read from the RECORD parameter during the first call. If the transfer of the data record takes longer than the duration of one call, the contents of the RECORD parameter are no longer relevant for the subsequent instruction calls (for the same job).

#### Parameter RET_VAL

See also: [PARM_MOD: Transfer module data records](#parm_mod-transfer-module-data-records-s7-300-s7-400).

> **Note**
>
> **For S7-400 only**
>
> If the general error W#16#8544 occurs, it only indicates that access to at least one byte of the I/O memory area containing the data record was denied. The data transfer was continued.

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

### WR_DPARM: Transfer data record (S7-300, S7-400)

#### Description

You use the instruction to transfer the data record with the number RECNUM from the configuration data to the addressed module. With this instruction, it is irrelevant whether the data record is static or dynamic.

#### Parameter

The following table shows the parameters of the instruction "WR_DPARM":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Write request |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed  module, you will have to specify the area identifier of the lower address. If  the addresses are identical, you will have to specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical base address of the module. For  a mixed module, the lower of the two  addresses must be specified. |
| RECNUM | Input | BYTE | I, Q, M, D, L or constant | Data record number |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The writing process is not yet complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

See also: [PARM_MOD: Transfer module data records](#parm_mod-transfer-module-data-records-s7-300-s7-400).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## Interrupts (S7-300, S7-400)

This section contains information on the following topics:

- [Time-of-day interrupt (S7-300, S7-400)](#time-of-day-interrupt-s7-300-s7-400)
- [Time-delay interrupt (S7-300, S7-400)](#time-delay-interrupt-s7-300-s7-400)
- [Synchronous error events (S7-300, S7-400)](#synchronous-error-events-s7-300-s7-400)
- [Asynchronous error event (S7-300, S7-400)](#asynchronous-error-event-s7-300-s7-400)
- [Multicomputing interrupt (S7-300, S7-400)](#multicomputing-interrupt-s7-300-s7-400)

### Time-of-day interrupt (S7-300, S7-400)

This section contains information on the following topics:

- [Using the instructions SET_TINT, CAN_TINT, ACT_TINT, QRY_TINT (S7-300, S7-400)](#using-the-instructions-set_tint-can_tint-act_tint-qry_tint-s7-300-s7-400)
- [SET_TINT: Set time-of-day interrupt (S7-300, S7-400)](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)
- [CAN_TINT: Cancel time-of-day interrupt (S7-300, S7-400)](#can_tint-cancel-time-of-day-interrupt-s7-300-s7-400)
- [ACT_TINT: Enable time-of-day interrupt (S7-300, S7-400)](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)
- [QRY_TINT: Query status of time-of-day interrupt (S7-300, S7-400)](#qry_tint-query-status-of-time-of-day-interrupt-s7-300-s7-400)

#### Using the instructions SET_TINT, CAN_TINT, ACT_TINT, QRY_TINT (S7-300, S7-400)

##### Definition

A time-of-day interrupt causes the time-triggered call of a time-of-day interrupt OB.

##### Prerequisites for the call

Before a time-of-day interrupt OB can be called by the operating system, the following conditions must be met:

- The time-of-day interrupt OB parameters must be assigned (start date and time, execution)

  - Per configuration, or
  - With the "[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)" instruction in the user program.
- The time-of-day interrupt OB must be activated

  - Per configuration, or
  - with the "[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)" instruction in the user program.
- The time-of-day interrupt OB must not be deselected during configuration.
- The time-of-day interrupt OB must exist in the CPU.
- If you use the "[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)" instruction for setting, and if you have specified the execution of the OB as **once only**, the start date and time must not yet have elapsed; for **periodic execution**, the time-of-day interrupt OB will be started at the next expired period (start time + multiple of the period duration).

  > **Note**
  >
  > You can assign parameters to the time-of-day interrupt using the configuration tool and then activate the interrupt in your user program ("[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)").

##### Purpose of the instructions "SET_TINT", "CAN_TINT", "ACT_TINT" and "QRY_TINT"

You use the instructions to

- set time-of-day interrupts ("[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)")
- delete time-of-day interrupts ("[CAN_TINT](#can_tint-cancel-time-of-day-interrupt-s7-300-s7-400)")
- enable time-of-day interrupts ("[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)")
- query time-of-day interrupts ("[QRY_TINT](#qry_tint-query-status-of-time-of-day-interrupt-s7-300-s7-400)")

##### Effects on the time-of-day interrupt

The following table lists a number of different situations and explains the effect they have on a time-of-day interrupt.

| If ... | Then ... |
| --- | --- |
| a new time-of-day is set   (Calling of "[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)"), | The current time-of-day interrupt is canceled automatically. |
| The time-of-day interrupt will be cancelled   (Calling of "[CAN_TINT](#can_tint-cancel-time-of-day-interrupt-s7-300-s7-400)"), | The start date and time are cleared. The time-of-day  interrupt must then be set again before it can be  activated. |
| The time-of-day interrupt OB does not exist  when it is called, | The priority class error is generated automatically,  which means that the operating system calls OB 85.  If OB 85 does not exist, the CPU changes to STOP. |
| The clock is synchronized or the time of day set forward, | If the start date/time is skipped because the clock is  moved forward:  - The operating system then calls OB 80.<sup>1</sup> - Following OB 80, every skipped time-of-day interrupt  OB is called (once, regardless of the number of  periods that were skipped) provided that it was not  manipulated in OB 80.<sup>2</sup>   If OB 80 does not exist, the CPU changes to STOP. |
| The real-time clock is synchronized or the clock is set back | S7-400 CPUs and CPU 318: If the time-of-day interrupt OBs had already been called  during the time by which the clock has been set  back, they are not called again the second time around.  S7-300 CPUs: The affected time-of-day interrupt OBs are all executed. |
| <sup>1</sup> OB 80 contains encoded start event information, indicating which time-of-day interrupt OBs could not be called due to moving the clock forward. The time of day in the start event information corresponds to the time adjusted forward.   <sup>2</sup> The time of day in the start event information of the time-of-day interrupt OB activated later after being skipped corresponds to the start time of the first skipped time-of-day interrupt. |  |

##### Response to warm restart or cold restart

During a warm restart or a cold restart, all the time-of-day interrupt settings made in the user program by means of instructions are cleared. In this case the parameters set per configuration are effective.

##### Execution of the time-of-day  interrupt OB

The following table shows the different effects of the "execution" parameter. This parameter must be set per configuration or with the "[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)" instruction (input parameter PERIOD).

| Execution of the time-of-day  interrupt OB | Reaction |
| --- | --- |
| None  (can only be set per configuration) | The time-of-day interrupt OB is not executed even when it exists in the  CPU.  Parameter reassignment, which means you can set the time-of-day interrupt ("[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)") in the user program. |
| Once | The time-of-day interrupt is canceled after the time-of-day interrupt OB  has been called. It can then be set and activated again. |
| Periodic  (every minute, hour, day, week,  month, year) | If the start date and time have already passed when the interrupt is  activated, the time-of-day interrupt OB interrupts the cyclic program at  the next possible point "start date/time + multiple of the selected period".  In extremely rare situations, processing of the time-of-day interrupt OB  may not yet be completed when it is called again.   Result:  - Time error, (the operating system calls OB 80; if OB 80 does not  exist, the CPU changes to STOP). - The time-of-day interrupt OB is executed later. |

#### SET_TINT: Set time-of-day interrupt (S7-300, S7-400)

##### Description

With the instruction, you can set the start date and time of the time-of-day interrupt organization blocks. The seconds and milliseconds of the specified start time are ignored and set to "0".

##### Parameter

The following table shows the parameters of the instruction "SET_TINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB started at the time SDT +  multiple of PERIOD (OB 10 to OB 17). |
| SDT | Input | DT | D, L | Start date and time: the seconds and  milliseconds of the specified start time are  ignored and set to 0.  If you want to set a monthly start of a time-of-day interrupt OB, you can only use the days 1, 2, ... 28 as a start date. |
| PERIOD | Input | WORD | I, Q, M, D, L or constant | Periods from start point SDT onwards:  - W#16#0000 = once - W#16#0201 = once every minute - W#16#0401 = once hourly - W#16#1001 = once daily - W#16#1201 = once weekly - W#16#1401 = once monthly - W#16#1801 = once yearly - W#16#2001 = at month's end |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 8091 | Incorrect parameter SDT |
| 8092 | Incorrect parameter PERIOD |
| 80A1 | The set start time is in the past. (This error code occurs only when PERIOD = W#16#0000.) |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### CAN_TINT: Cancel time-of-day interrupt (S7-300, S7-400)

##### Description

You use the instruction to set the start date and time of the time-of-day interrupt organization block. This disables the time-of-day interrupt and the organization block is no longer called.

If you would you like to use the time-of-day interrupt again, you must first set the start time ("[SET_TINT](#set_tint-set-time-of-day-interrupt-s7-300-s7-400)" instruction) and then enable the time-of-day interrupt ("[ACT_TINT](#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)" instruction).

##### Parameter

The following table shows the parameters of the instruction "CAN_TINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB, in which the start date  and time will be canceled (OB 10 to OB 17). |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 80A0 | No start date/time specified for the time-of-day interrupt OB |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### ACT_TINT: Enable time-of-day interrupt (S7-300, S7-400)

##### Description

You use the instruction to activate a time-of-day interrupt organization block.

##### Parameter

The following table shows the parameters of the instruction "ACT_TINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB to be activated (OB 10 to OB 17). |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 80A0 | Start date/time-of day not set for the respective time-of-day interrupt OB. |
| 80A1 | The activated time is in the past. This error only occurs if execution = once is selected. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### QRY_TINT: Query status of time-of-day interrupt (S7-300, S7-400)

##### Description

You use the instruction to display the status of a time-of-day interrupt organization block at the output parameter STATUS .

##### Parameter

The following table shows the parameters of the instruction "QRY_TINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB that will be  queried for status (OB 10 to OB 17). |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the time-of-day interrupt;  see following table. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter STATUS

> **Note**
>
> If RET_VAL contains a value different than zero, you may not evaluate STATUS.

| Bit | Value | Meaning |
| --- | --- | --- |
| 0 | 0 | In Run. |
|  | 1 | During startup. |
| 1 | 0 | The time-of-day interrupt is enabled. |
|  | 1 | The time-of-time interrupt is disabled by "[DIS_IRT](#dis_irt-disable-interrupt-event-s7-300-s7-400)". |
| 2 | 0 | Time-of-day interrupt is not activated or has elapsed. |
|  | 1 | The time-of-day interrupt is activated. |
| 4 | 0 | An OB with an OB number as specified at OB_NR parameter does not exist. |
|  | 1 | An OB with an OB number as specified at OB_NR parameter does exist. |
| Other |  | Always "0" |

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### Time-delay interrupt (S7-300, S7-400)

This section contains information on the following topics:

- [Using time-delay interrupts (S7-300, S7-400)](#using-time-delay-interrupts-s7-300-s7-400)
- [SRT_DINT: Start time-delay interrupt (S7-300, S7-400)](#srt_dint-start-time-delay-interrupt-s7-300-s7-400)
- [CAN_DINT: Cancel time-delay interrupt (S7-300, S7-400)](#can_dint-cancel-time-delay-interrupt-s7-300-s7-400)
- [QRY_DINT: Query time-delay interrupt status (S7-300, S7-400)](#qry_dint-query-time-delay-interrupt-status-s7-300-s7-400)

#### Using time-delay interrupts (S7-300, S7-400)

##### Definition

After you have called the "[SRT_DINT](#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction, the operating system generates an interrupt after the specified delay time has elapsed. The configured time-delay interrupt OB is called.

##### Prerequisites for the call

Before a time-delay interrupt can be called by the operating system, the following conditions must be met:

- The time-delay interrupt OB must be started by the "[SRT_DINT](#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction.
- The time-delay interrupt OB must not be deselected during configuration.
- The time-delay interrupt OB must exist in the CPU.

##### Purpose of the instructions "SRT_DINT", "CAN_DINT" and "QRY_DINT"

You use the instructions to

- Start time-delay interrupts ("[SRT_DINT](#srt_dint-start-time-delay-interrupt-s7-300-s7-400)")
- Cancel time-delay interrupts ("[CAN_DINT](#can_dint-cancel-time-delay-interrupt-s7-300-s7-400)")
- Query time-delay interrupts ("[QRY_DINT](#qry_dint-query-time-delay-interrupt-status-s7-300-s7-400)")

##### Effects on the time-delay interrupt

The following table lists a number of different situations and explains the effect they have on a time-delay interrupt.

| If ... | and ... | Then ... |
| --- | --- | --- |
| A time-delay interrupt is started (by calling "[SRT_DINT](#srt_dint-start-time-delay-interrupt-s7-300-s7-400)") | The time-delay interrupt has  already started, | The delay time is overwritten; the  time-delay interrupt is started  again. |
|  | The time-delay interrupt OB does  not exist at the time of the call, | a diagnostic buffer entry is made and the CPU continues to run. |
|  | The interrupt is started in a startup  OB and the delay time elapses  before the CPU changes to RUN, | The call of the time-delay interrupt  OB is delayed until the CPU is in  RUN mode. |
| The delay time has elapsed, | A previously started time-delay  interrupt OB is still being  executed, | The operating system generates a  time error (calls OB 80). If OB 80  does not exist, the CPU continues to run). |

##### Response to warm restart and cold restart

During a warm restart or a cold restart, all the time-delay interrupt settings made in the user program by means of instructions are cleared.

##### Starting in a startup OB

A time-delay interrupt can be started in a startup OB. Two conditions must be satisfied to call the time-delay OB:

- The delay time must have elapsed.
- The CPU must be in the RUN mode.

If the delay time has elapsed and the CPU is not yet in the RUN mode, the time-delay interrupt OB call is delayed until the CPU is in RUN mode. The time-delay interrupt OB is then called before the first instruction in OB Main [OB 1] is executed.

#### SRT_DINT: Start time-delay interrupt (S7-300, S7-400)

##### Description

You use the instruction to start a time-delay interrupt that calls a time-delay interrupt OB once the assigned delay time has elapsed (DTIME parameter).

With the SIGN parameter, you can enter an identifier that identifies the start of the time-delay interrupt. The values of DTIME and SIGN appear again in the start event information of the specified OB when it is executed.

The maximum time between the "SRT_DINT" instruction call and the start of the time-delay interrupt OB is **one millisecond** less than the assigned time, provided that no interruption events delay the call.

##### Parameter

The following table shows the parameters of the instruction "SRT_DINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB to be started after a  time delay (OB 20 to OB 23). |
| DTIME | Input | TIME | I, Q, M, D, L or constant | Time delay value (1 to 60000 ms)  You can realize longer times, for example, by using a counter in a time-delay interrupt OB. |
| SIGN | Input | WORD | I, Q, M, D, L or constant | Identifier that appears in the start event  information of the OB when the time-delay interrupt OB is called. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 8091 | Incorrect parameter DTIME |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### CAN_DINT: Cancel time-delay interrupt (S7-300, S7-400)

##### Description

You use the instruction to cancel a started time-delay interrupt (see "[SRT_DINT](#srt_dint-start-time-delay-interrupt-s7-300-s7-400)"). The time-delay interrupt OB is not called in this case.

##### Parameters

The following table shows the parameters of the instruction "CAN_DINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB to be canceled (OB 20 to  OB 23). |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 80A0 | Time-delay interrupt has not started. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### QRY_DINT: Query time-delay interrupt status (S7-300, S7-400)

##### Description

You use the instruction to query the status of a time-delay interrupt. Time-delay interrupts are managed by organization blocks OB 20 to OB 23.

##### Parameter

The following table shows the parameters of the instruction "QRY_DINT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L or constant | Number of the OB that will be  queried for status (OB 20 to OB 23). |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the actual parameter of RET_VAL contains an error code. |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the time-delay interrupt, see  following table. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter STATUS

> **Note**
>
> If RET_VAL contains a value different than zero, you may not evaluate STATUS.

| Bit | Value | Meaning |
| --- | --- | --- |
| 0 | 0 | In Run. |
| 1 | During startup. |  |
| 1 | 0 | The time-delay interrupt is enabled. |
| 1 | The time-delay interrupt is disabled by "[DIS_IRT](#dis_irt-disable-interrupt-event-s7-300-s7-400)". |  |
| 2 | 0 | Time-delay interrupt is not activated or has elapsed. |
| 1 | The time-delay interrupt is activated. |  |
| 4 | 0 | An OB with an OB number as specified at OB_NR parameter does not exist. |
| 1 | An OB with an OB number as specified at OB_NR parameter is loaded. |  |
| Other |  | Always "0" |

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Incorrect parameter OB_NR |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### Synchronous error events (S7-300, S7-400)

This section contains information on the following topics:

- [Mask synchronous error events (S7-300, S7-400)](#mask-synchronous-error-events-s7-300-s7-400)
- [MSK_FLT: Mask synchronous error events (S7-300, S7-400)](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)
- [DMSK_FLT: Unmask synchronous error events (S7-300, S7-400)](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)
- [READ_ERR: Read out event status register (S7-300, S7-400)](#read_err-read-out-event-status-register-s7-300-s7-400)

#### Mask synchronous error events (S7-300, S7-400)

##### Introduction

Synchronous errors are programming and access errors. Such errors occur as a result of programming with incorrect operand areas or numbers, or incorrect addresses. **Masking** these synchronous errors means the following:

- Masked synchronous errors do not trigger an error OB call and do not lead to a programmed alternative reaction.
- The CPU "records" the masked errors that have occurred in an error status register.

Masking is carried out by calling the "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)" instruction.

**Unmasking** errors means canceling a previously set mask and clearing the corresponding bit in the event status register of the current priority class. Masking is canceled as follows:

- By calling the "[DMSK_FLT](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)" instruction.
- When the current priority class has been completed (for S7-400 only).

If an error event occurs after it has been unmasked, then the operating system will start the associated error OB. You program OB 121 for the reaction to programming errors and OB 122 for the reaction to access errors.

You can use the "[READ_ERR](#read_err-read-out-event-status-register-s7-300-s7-400)" instruction to read the masked errors that have occurred.

> **Note**
>
> With the S7-300 (except CPU 318), regardless of whether an error is masked or unmasked, the error is entered in the diagnostic buffer and the group error LED of the CPU is illuminated.

##### Handling errors in general

If programming and access errors occur in a user program, you can react to them in different ways:

- You can program an error OB that is called by the operating system when the corresponding error occurs.
- You can disable the error OB call individually for each priority class. In this case, the CPU does not change to STOP when an error of this type occurs in the particular priority class. The CPU enters the error in an error register. From this entry, however, you cannot recognize when or how often the error occurred.

  ![Handling errors in general](images/63734311947_DV_resource.Stream@PNG-en-US.png)

##### Error filter

Synchronous errors are assigned to a particular bit pattern known as the **error filter**. You can find this error filter in the input and output parameters of the "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)", "[DMSK_FLT](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)", and "[READ_ERR](#read_err-read-out-event-status-register-s7-300-s7-400)" instructions.

Synchronous errors are divided into programming and access errors that you can mask using two error filters. The error filters are illustrated in the following figures.

##### Programming error filter

The following figure shows the bit pattern of the error filter for programming errors. The error filter for the programming errors is available in the "PRGFLT_..." parameters (see below "Programming errors, Low-Word" or "Programming errors, High-Word").

![Programming error filter](images/76052787467_DV_resource.Stream@PNG-en-US.png)

##### Non-relevant bits

In the figure above, **x** means ...

|  |  |  |
| --- | --- | --- |
| - ... Input parameters | For "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)", "[DMSK_FLT](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)", "[READ_ERR](#read_err-read-out-event-status-register-s7-300-s7-400)" | = **"0"** |
| - ... Output parameters | For "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)", "[DMSK_FLT](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)" | = **"1"** for S7-300   **="0"** for S7-400 |
| For "[READ_ERR](#read_err-read-out-event-status-register-s7-300-s7-400)" | = **"0"** |  |

##### Access error filter for all CPUs

The following figure shows you the bit pattern of the error filter for access errors. The error mask for access errors is located in the parameters ACCFLT_...

An explanation of the access errors can be found in the following tables (see below).

![Access error filter for all CPUs](images/63734320907_DV_resource.Stream@PNG-en-US.png)

##### Example

The following figure shows the low word of the error filter for access errors with all masked errors for all CPUs.

- As input parameters for "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)"
- As output parameters for "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)"

  ![Example](images/63734325387_DV_resource.Stream@PNG-en-US.png)

##### Programming error low word

The following table lists the errors assigned to the low word of the error filter for programming errors. The possible causes of the errors are also listed.

Possible causes of programming errors, low word

| Error | Event ID (W#16#...) | Error occurs ... |
| --- | --- | --- |
| BCD conversion error | 2521 | ... if the value to be converted is not a BCD number (for example, 5E8). |
| Area length error when reading | 2522 | ... if an addressed operand is not completely within the possible operand range.  Example: MW 320 should be read although the memory area  is only 256 bytes long. |
| Area length error when writing | 2523 | ... if an addressed operand is not completely within the possible operand range.  Example: A value should be written to MW 320 although the  memory area is only 256 bytes long. |
| Range error when reading | 2524 | ... if indirect, area overlapping addressing specifies an incorrect area identifier for the operand.  Example:    Correct: LAR1 P#E 12.0   L W[AR1, P#0.0]   Incorrect: LAR1 P#12.0   L W[AR1, P#0.0]  The range error   is reported during this operation. |
| Range error when writing | 2525 | ... if indirect, area overlapping addressing specifies an incorrect area identifier for the operand.  Example:    Correct: LAR1 P#E 12.0   T W[AR1, P#0.0]   Incorrect: LAR1 P#12.0   T W[AR1, P#0.0]  The range error   is reported during this operation. |
| Timer number error | 2526 | ... if a timer that does not exist is accessed.  Example: SP T [MW 0] where MW 0 = 129; timer 129 should  be started although there are only 128 timers available. |
| Counter number error | 2527 | ... if a counter that does not exist is accessed.  Example: CU C [MW 0] where MW 0 = 600; counter 600  must be accessed although there are only 512 counters  available (CPU 416-1). |
| Alignment error when reading | 2528 | ... if a byte, word, or double-word operand is addressed with a bit address ≠ 0.  Example: Correct: LAR1 P#M12.0   L B[AR1, P#0.0]   Incorrect: LAR1 P#M12.4   L B[AR1, P#0.0] |
| Alignment error when writing | 2529 | ... if a byte, word, or double-word operand is addressed with a bit address ≠ 0.  Example:    Correct: LAR1 P#M12.0   T B[AR1, P#0.0]   Incorrect: LAR1 P#M12.4   T B[AR1, P#0.0] |

##### Programming error high word

The following table lists the errors assigned to the high word of the error filter for programming errors. The possible causes of the errors are also listed.

Possible causes of programming errors, high word

| Error | Event ID (W#16#...) | Error occurs ... |
| --- | --- | --- |
| Write error data block | 2530 | ... if the data block to be written to is read-only. |
| Write error instance data block | 2531 | ... if the instance data block to be written to is read-only. |
| Block number error DB | 2532 | ... if a data block must be opened whose number is  higher than the highest permitted number. |
| Block number error DI | 2533 | ... if an instance data block must be opened whose  number is higher than the highest permitted number. |
| Block number error FC | 2534 | ... if a function is called whose number is higher than the  highest permitted number. |
| Block number error FB | 2535 | ... if a function block is called whose number is higher  than the highest permitted number. |
| DB not loaded | 253A | ... if the data block to be opened is not loaded. |
| Instruction not loaded | 253C to 253F | ... if the called instruction is not loaded. |

##### Access error

The following table lists the errors assigned to the error filter for access errors for all CPUs. The possible causes of the errors are also listed.

| Error | Event ID (W#16#...) | Error occurs ... |
| --- | --- | --- |
| I/O access error  when reading | 2942 | ... if a signal module is not assigned to the address in the  I/O area.  Or  ... if access to this I/O area is not acknowledged within  the specified module monitoring time (timeout). |
| I/O access error  when writing | 2943 | ... if a signal module is not assigned to the address in the  I/O area.  Or  ... if access to this I/O area is not acknowledged within  the specified module monitoring time (timeout). |

#### MSK_FLT: Mask synchronous error events (S7-300, S7-400)

##### Description

You use the instruction to control the reaction of the CPU to synchronous errors. To do this, you mask the respective synchronous errors (for error filters see [Mask synchronous error events](#mask-synchronous-error-events-s7-300-s7-400)). When you call "MSK_FLT", you mask the synchronous errors in the current priority class.

If you set individual bits of the synchronous error filter to "1" in the input parameters, other bits that were set previously retain their value of "1", You obtain new error filters that you can read out using the output parameters. The synchronous errors you have masked do not call an OB but are simply entered in an error register. You can read the error register with the "[READ_ERR](#read_err-read-out-event-status-register-s7-300-s7-400)" instruction.

##### Parameter

The following table shows the parameters of the instruction "MSK_FLT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PRGFLT_SET_MASK | Input | DWORD | I, Q, M, D, L or constant | Programming error to be  masked |
| ACCFLT_SET_MASK | Input | DWORD | I, Q, M, D, L or constant | Access error to be masked |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| PRGFLT_MASKED | Output | DWORD | I, Q, M, D, L | Masked programming errors |
| ACCFLT_MASKED | Output | DWORD | I, Q, M, D, L | Masked access errors |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | None of the errors were already masked. |
| 0001 | At least one of the errors was already masked. Nevertheless the other errors will be masked. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### DMSK_FLT: Unmask synchronous error events (S7-300, S7-400)

##### Description

You use the instruction to unmask the errors masked with "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)". To do this, you must set the corresponding bits of the error filter to "1" in the input parameters. With the "DMSK_FLT" call, you unmask the corresponding synchronous errors of the current priority class. At the same time, the queried entries are cleared in the error register. You can read out the new error filters using the output parameters.

##### Parameters

The following table shows the parameters of the instruction "DMSK_FLT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PRGFLT_ RESET_MASK | Input | DWORD | I, Q, M, D, L or constant | Programming errors to be  unmasked |
| ACCFLT_ RESET_MASK | Input | DWORD | I, Q, M, D, L or constant | Access errors to be  unmasked |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| PRGFLT_ MASKED | Output | DWORD | I, Q, M, D, L | Still masked programming  errors |
| ACCFLT_ MASKED | Output | DWORD | I, Q, M, D, L | Still masked access errors |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | All specified errors were unmasked. |
| 0001 | At least one of the errors was not masked. Nevertheless the other errors will be unmasked. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### READ_ERR: Read out event status register (S7-300, S7-400)

##### Description

You use the instruction to read the error register. The structure of the error register corresponds to that of the programming and access error filters, which you can program as input parameters with "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)" and "[DMSK_FLT](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)".

In the input parameters, you enter the synchronous errors you want to read from the error register. When you call "READ_ERR", you read the required entries from the error register and at the same time clear these entries.

The error register contains information that tells you which of the masked synchronous errors in the current priority class occurred at least once. If a bit is set, this means that the corresponding masked synchronous error occurred at least once.

##### Parameter

The following table shows the parameters of the instruction "READ_ERR":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| PRGFLT_QUERY | Input | DWORD | I, Q, M, D, L or constant | Query programming error |
| ACCFLT_QUERY | Input | DWORD | I, Q, M, D, L or constant | Query access error |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| PRGFLT_CLR | Output | DWORD | I, Q, M, D, L | Programming errors that occurred |
| ACCFLT_CLR | Output | DWORD | I, Q, M, D, L | Access errors that occurred |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | All queried errors are masked. |
| 0001 | At least one of the queried errors is not masked. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### Asynchronous error event (S7-300, S7-400)

This section contains information on the following topics:

- [Delaying and disabling interrupt and asynchronous error events (S7-300, S7-400)](#delaying-and-disabling-interrupt-and-asynchronous-error-events-s7-300-s7-400)
- [DIS_IRT: Disable interrupt event (S7-300, S7-400)](#dis_irt-disable-interrupt-event-s7-300-s7-400)
- [EN_IRT: Enable interrupt event (S7-300, S7-400)](#en_irt-enable-interrupt-event-s7-300-s7-400)
- [DIS_AIRT: Delay execution of higher priority interrupts and asynchronous error events (S7-300, S7-400)](#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)
- [EN_AIRT: Enable execution of higher priority interrupts and asynchronous error events (S7-300, S7-400)](#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)

#### Delaying and disabling interrupt and asynchronous error events (S7-300, S7-400)

##### Purpose of the instructions "DIS_IRT", "EN_IRT", "DIS_AIRT", "EN_AIRT"

You use these instructions to

- Disable processing of interrupts and asynchronous error events with "[DIS_IRT](#dis_irt-disable-interrupt-event-s7-300-s7-400)" for all subsequent CPU cycles.
- Delay higher priority classes with "[DIS_AIRT](#dis_irt-disable-interrupt-event-s7-300-s7-400)" until the end of the OB.
- To re-enable processing of interrupts and asynchronous error events with "[EN_IRT](#en_irt-enable-interrupt-event-s7-300-s7-400)" or "[EN_AIRT](#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)".

You program the processing of interrupts and asynchronous error events in the user program. You must also program the corresponding OBs.

##### Purpose of the instructions "DIS_AIRT" and "EN_AIRT"

Delaying higher priority interrupts and asynchronous error events with the "[DIS_AIRT](#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instruction and then enabling them again with the "[EN_AIRT](#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instruction has the following advantage:

The number of interrupt delays is counted by the CPU. If you have programmed a delay of interrupts and asynchronous error events, the delay cannot be canceled by standard FC calls if the interrupts and asynchronous error events are also disabled and then enabled again in the standard FCs themselves.

##### Interrupt classes

The interrupts are divided into various classes. The following table lists all the interrupt classes and the corresponding OBs.

| Interrupt class | OB |
| --- | --- |
| Time-of-day interrupts | OB 10 to OB 17 |
| Time-delay interrupts | OB 20 to OB 23 |
| Cyclic interrupts | OB 30 to OB 38 |
| Process interrupts | OB 40 to OB 47 |
| Interrupts for DPV1 | OB 55 to OB 57 |
| Multicomputing interrupt | OB 60 |
| Redundancy error interrupts | OB 70, OB 72 |
| Asynchronous error interrupts | OB 80 to OB 87 (se below) |
| Synchronous error interrupts | OB 121, OB 122  (You mask or unmask the execution of synchronous error interrupts with the "[MSK_FLT](#msk_flt-mask-synchronous-error-events-s7-300-s7-400)", "[DMSK_FLT](#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)" and "[READ_ERR](#read_err-read-out-event-status-register-s7-300-s7-400)" instructions) |

##### Asynchronous error events

The following table lists all the asynchronous error events to which you can react with an OB call in the user program.

| Asynchronous error events | OB |
| --- | --- |
| Time error (for example, cycle time exceeded) | OB 80 |
| Power supply error (for example, battery fault) | OB 81 |
| Diagnostics interrupt (for example, defective fuse on a signal module) | OB 82 |
| Insert/remove module interrupt | OB 83 |
| CPU hardware fault (for example, interface error) | OB 84 |
| Program execution error | OB 85 |
| Rack failure | OB 86 |
| Communication error | OB 87 |

#### DIS_IRT: Disable interrupt event (S7-300, S7-400)

##### Description

With the instruction you disable the processing of new interrupts and asynchronous error evetns. Disabling means that if an interrupting event occurs, the operating system of the CPU reacts as follows:

- It **neither** calls an interrupt OB nor an asynchronous error OB,
- **nor** does it trigger the normal reaction if an interrupt OB or asynchronous error OB is not programmed.

If you disable interrupts and asynchronous error events, this remains in effect for all priority classes. The disable can only be canceled with the "[EN_IRT](#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction or by a warm or a cold restart.

Whether the operating system writes interrupts and asynchronous error events to the diagnostics buffer when they occur depends on the input parameter setting you select for MODE.

> **Note**
>
> Remember that when you program the "DIS_IRT" instruction, all interrupts that occur will be discarded.

##### Parameter

The following table shows the parameters of the instruction "DIS_IRT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Specifies which interrupts and asynchronous  errors are disabled. |
| OB_NR | Input | INT | I, Q, M, D, L or constant | OB number |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter MODE

| MODE (B#16#...) | Meaning |
| --- | --- |
| 00 | All newly occurring interrupts and asynchronous error events are disabled. (Synchronous errors  are not disabled.) Assign the value "0" to the OB_NR parameter. Entries continue to be made in the diagnostics buffer. |
| 01 | All newly occurring events belonging to a specified interrupt class are disabled. Identify the interrupt class by specifying it as follows:  - Time-of-day interrupts: 10 - Time-delay interrupts: 20 - Cyclic interrupts: 30 - Process interrupts: 40 - Interrupts for DPV1: 50 - Multicomputing interrupt: 60 - Redundancy error interrupts: 70 - Asynchronous error interrupts: 80   Entries continue to be made in the diagnostics buffer. |
| 02 | All new occurrences of a specified interrupt are disabled. You designate the interrupt  using the OB number. Entries continue to be made in the diagnostics buffer. |
| 80 | All newly occurring interrupts and asynchronous error events are disabled and are no longer entered in the diagnostics buffer. Assign the value "0" to the OB_NR parameter. The operating system enters event W#16#5380 in the diagnostics buffer. |
| 81 | All newly occurring events belonging to a specified interrupt class are disabled and are no longer  entered in the diagnostics buffer. The operating system enters event W#16#5380 in the diagnostics buffer. |
| 82 | All newly occurring events belonging to a specified interrupt are disabled and are no longer entered in  the diagnostics buffer. The operating system enters event W#16#5380 in the diagnostics buffer. |

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | The OB_NR input parameter contains an illegal value. |
| 8091 | The MODE input parameter contains an illegal value. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### EN_IRT: Enable interrupt event (S7-300, S7-400)

##### Description

You use the instruction to enable the processing of new interrupts and asynchronous error events that you have previously disabled with the "[DIS_IRT](#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction. This means that if an interrupting event occurs, the operating system of the CPU reacts in one of the following ways:

- It calls an interrupt OB or asynchronous error OB.

  Or
- It triggers the standard reaction if the interrupt OB or asynchronous error OB is not programmed.

##### Parameters

The following table shows the parameters of the instruction "EN_IRT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Specifies which interrupts and  asynchronous error events will be enabled. |
| OB_NR | Input | INT | I, Q, M, D, L or constant | OB number |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter MODE

| MODE | Meaning |
| --- | --- |
| 0 | All newly occurring interrupts and asynchronous error events are enabled. |
| 1 | All newly occurring events belonging to a specified interrupt class are enabled. Identify the interrupt class by specifying it as follows:  - Time-of-day interrupts: 10 - Time-delay interrupts: 20 - Cyclic interrupts: 30 - Process interrupts: 40 - Interrupts for DPV1: 50 - Multicomputing interrupt: 60 - Redundancy error interrupts: 70 - Asynchronous error interrupts: 80 |
| 2 | All newly occurring events of a specified interrupt are enabled. You designate the interrupt  using the OB number. |

##### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | The OB_NR input parameter contains an illegal value. |
| 8091 | The MODE input parameter contains an illegal value. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### DIS_AIRT: Delay execution of higher priority interrupts and asynchronous error events (S7-300, S7-400)

##### Description

With the instruction you delay the processing of interrupt OBs and asynchronous OBs with priority higher than that of the current OB. You can call the "DIS_AIRT" instruction more than once in an OB. The instruction calls are counted by the operating system. The processing delay is in force until you use the "[EN_AIRT](#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instruction to cancel each delayed processing of interrupt OBs and asynchronous error OBs with "DIS_AIRT", **or** the current OB has been executed.

The pending interrupts or asynchronous error events are processed as soon as the processing delay has been canceled with the "[EN_AIRT](#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instruction or the current OB processing is complete.

##### Parameter

The following table shows the parameters of the instruction "DIS_AIRT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Return | INT | I, Q, M, D, L | Number of delays (= number of  DIS_AIRT calls) |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

The following table shows the return value of "DIS_AIRT" that is output with the RET_VAL parameter.

| Return value | Description |
| --- | --- |
| n | "n" shows the number of processing delays, which is the number of "DIS_AIRT calls, after the instruction is complete  (interrupt processing is only enabled again when n = 0; see "[EN_AIRT](#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)"). |

#### EN_AIRT: Enable execution of higher priority interrupts and asynchronous error events (S7-300, S7-400)

##### Description

With the instruction you re-release the execution of high-priority interrupt events or asynchronous error events delayed with "[DIS_AIRT](#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)". Each individual processing delay must be canceled with the "EN_AIRT" instruction.

##### Example

If, for example, you have delayed interrupts five times with five "[DIS_AIRT](#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" calls, you must cancel each of the interrupt delays using five "EN_AIRT" calls.

##### Parameter

The following table shows the parameters of the instruction "EN_AIRT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Return | INT | I, Q, M, D, L | Number of delays still programmed on  completion of "EN_AIRT" or error message. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

How you evaluate the error information of the RET_VAL parameter is explained in the chapter [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val). This chapter also contains the general error information for the instructions. The following table contains the return value or error information specific to "EN_AIRT" that can be output with the RET_VAL parameter.

| Return value and error  information | Description |
| --- | --- |
| n | "n" shows the number of processing delays, which is the number of "EN_AIRT calls, after the instruction is complete  (interrupt processing is only enabled again when n = 0). |
| W#16#8080 | "EN_AIRT" was called even though interrupt processing has already been enabled. |

### Multicomputing interrupt (S7-300, S7-400)

This section contains information on the following topics:

- [MP_ALM: Multicomputing interrupt (S7-400)](#mp_alm-multicomputing-interrupt-s7-400)

#### MP_ALM: Multicomputing interrupt (S7-400)

##### Description

Calling the instruction during multiprocessing will trigger the multicomputing interrupt. This leads to a synchronized start of OB 60 on all CPUs involved. In single processor mode and when operating with a segmented rack, OB 60 is only started on the CPU on which you called MP_ALM.

Use the input parameter JOB to identify the cause of the multicomputing interrupt. This job identifier is transferred to all associated CPUs, where you can evaluate it in the multicomputing interrupt OB (OB 60).

You can call the instruction at any point in your program. Since the call would be pointless in any mode other than RUN, if it is called in STARTUP mode, the multicomputing interrupt is suppressed. The function value informs you of this.

##### Parameters

The following table shows the parameters of the instruction "MP_ALM":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| JOB | Input | BYTE | I, Q, M, D, L or constant | Job identifier Possible values: 1 to 15 |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | The JOB input parameter contains an illegal value. |
| 80A0 | Execution of OB 60 following the last multicomputing interrupt is not completed  either on the local CPU or on another CPU. |
| 80A1 | Incorrect mode (STARTUP instead of RUN). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## Alarms (S7-300, S7-400)

This section contains information on the following topics:

- [Structure of diagnostic data (S7-300, S7-400)](#structure-of-diagnostic-data-s7-300-s7-400)
- [Structure of channel-specific diagnostic data (S7-300, S7-400)](#structure-of-channel-specific-diagnostic-data-s7-300-s7-400)
- [Instructions for generating PLC alarms with instance DB (S7-400)](#instructions-for-generating-plc-alarms-with-instance-db-s7-400)
- [Instructions for generating PLC alarms without instance DB (S7-300, S7-400)](#instructions-for-generating-plc-alarms-without-instance-db-s7-300-s7-400)
- [WR_USMSG: Write a user diagnostics event to the diagnostic buffer (S7-300, S7-400)](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400)
- [AR_SEND: Send archive data (S7-400)](#ar_send-send-archive-data-s7-400)
- [Others (S7-300, S7-400)](#others-s7-300-s7-400)

### Structure of diagnostic data (S7-300, S7-400)

#### Data record 0 and 1 of the system data

The diagnostic data of a module are located in the data records 0 and 1 of the system data area, see [Writing and reading data records](#writing-and-reading-data-records-s7-300-s7-400):

- Data record 0 contains 4 bytes of diagnostic data that describe the current status of a signal module.
- Data record 1 contains

  - The 4 bytes of diagnostic data, also located in data record 0 and
  - The diagnostic data specific to the module.

#### Structure and contents of the diagnostic data:

This section below describes the structure and contents of the individual bytes of the diagnostic data. The general principle: Whenever an error occurs, the corresponding bit is set to "1."

| Byte | Bit | Meaning | Remark | Data record |
| --- | --- | --- | --- | --- |
| 0 | 0 | Module is defective |  | 0 and 1 |
|  | 1 | Internal error |  |  |
|  | 2 | External error |  |  |
|  | 3 | Channel fault |  |  |
|  | 4 | External voltage failed |  |  |
|  | 5 | Front panel connector not plugged in |  |  |
|  | 6 | No parameter assignment |  |  |
|  | 7 | Wrong parameters in the module |  |  |
| 1 | 0  to  3 | Module class | 0101: Analog module  0000: CPU  1000: Function module  1100: CP  1111: Digital module  0011: DP standard slave   1011: I-slave  0100: IM | 0 and 1 |
|  | 4 | Channel information exists |  |  |
|  | 5 | User information exists |  |  |
|  | 6 | Diagnostic interrupt from substitute |  |  |
|  | 7 | Maintenance requirement (PROFINET IO only) |  |  |
| 2 | 0 | Memory card missing or wrong |  | 0 and 1 |
|  | 1 | Communication problem |  |  |
|  | 2 | Operating mode | 0: RUN  1: STOP |  |
|  | 3 | Cycle monitoring tripped |  |  |
|  | 4 | Internal power supply failed |  |  |
|  | 5 | Battery exhausted |  |  |
|  | 6 | Entire backup failed |  |  |
|  | 7 | Maintenance request (PROFINET IO only) |  |  |
| 3 | 0 | Expansion rack failure |  | 0 and 1 |
|  | 1 | Processor failure |  |  |
|  | 2 | EPROM fault |  |  |
|  | 3 | RAM fault |  |  |
|  | 4 | ADC/DAC error |  |  |
|  | 5 | Fuse tripped |  |  |
|  | 6 | Hardware interrupt lost |  |  |
|  | 7 | Reserved |  |  |
| 4 | 0  to  6 | Channel type | B#16#70: Digital input  B#16#72: Digital output  B#16#71: Analog input  B#16#73: Analog output  B#16#74: FM-POS  B#16#75: FM-REG  B#16#76: FM-COUNT  B#16#77: FM-TECHNO  B#16#78: FM-NCU  B#16#79: To   B#16#7D: Reserved  B#16#7E: US300  B#16#7F: Reserved | 1 |
|  | 7 | Additional channel type exists? | 0: No  1: Yes |  |
| 5 | 0  to  7 | Number of diagnostic bits  output per channel by a  module. | The number of diagnostic bits per  channel is rounded up to byte boundaries | 1 |
| 6 | 0  to  7 | Number of same type channels on a module | If different channel types exist on a  module, the structure is repeated in data  record 1 from byte 4 onwards for each  channel type. | 1 |
| 7 | 0 | Channel error channel 0/ channel group 0 | First byte of the channel error vector (the length of the channel error vector depends on the number of channels and is rounded up to a byte boundary). | 1 |
|  | 1 | Channel error channel 1/ channel group 1 |  |  |
|  | 2 | Channel error channel 2/ channel group 2 |  |  |
|  | 3 | Channel error channel 3/ channel group 3 |  |  |
|  | 4 | Channel error channel 4/ channel group 4 |  |  |
|  | 5 | Channel error channel 5/ channel group 5 |  |  |
|  | 6 | Channel error channel 6/ channel group 6 |  |  |
|  | 7 | Channel error channel 7/ channel group 7 |  |  |
| ... | - | Channel-specific errors (see [Structure of channel-specific diagnostic data](#structure-of-channel-specific-diagnostic-data-s7-300-s7-400) ) |  | 1 |

### Structure of channel-specific diagnostic data (S7-300, S7-400)

#### Channel-specific errors

Starting at the byte immediately following the channel error vector, the channel-specific errors are indicated for each channel of the module. The tables below show the structure of channel-specific diagnostics data for the different channel types. The bits have the following meaning:

- 1 = Error
- 0 = No error

#### Analog input channel

Diagnostics byte for an analog input channel:

| Bit | Meaning | Remark |
| --- | --- | --- |
| 0 | Configuration/parameter  assignment error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN= W#16#8x50 |
| 1 | Common mode error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x51 |
| 2 | P short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x52 |
| 3 | M short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x53 |
| 4 | Wire break | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x54 |
| 5 | Reference channel error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x55 |
| 6 | Measuring range undershoot | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x56 |
| 7 | Measuring range exceeded | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x57 |

#### Analog output channel

Diagnostics byte for an analog output channel

| Bit | Meaning | Remark |
| --- | --- | --- |
| 0 | Configuration/parameter  assignment error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x60 |
| 1 | Common mode error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x61 |
| 2 | P short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x62 |
| 3 | M short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x63 |
| 4 | Wire break | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x64 |
| 5 | 0 | Reserved |
| 6 | No load voltage | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x66 |
| 7 | 0 | Reserved |

#### Digital input channel

diagnostics byte for a digital input channel:

| Bit | Meaning | Remark |
| --- | --- | --- |
| 0 | Configuration/parameter  assignment error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x70 |
| 1 | Ground error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x71 |
| 2 | I/O short circuit (sensor) | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x72 |
| 3 | M short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x73 |
| 4 | Wire break | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x74 |
| 5 | No sensor power supply | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x75 |
| 6 | 0 | Reserved |
| 7 | 0 | Reserved |

#### Digital output channel

Diagnostics byte for a digital output channel:

| Bit | Meaning | Remark |
| --- | --- | --- |
| 0 | Configuration/parameter  assignment error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x80 |
| 1 | Ground error | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x81 |
| 2 | P short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x82 |
| 3 | M short circuit | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x83 |
| 4 | Wire break | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x84 |
| 5 | Fuse tripped | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x85 |
| 6 | No load voltage | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x86 |
| 7 | Overtemperature | Can be signaled with [WR_USMSG](#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400) and EVENTN = W#16#8x87 |

### Instructions for generating PLC alarms with instance DB (S7-400)

This section contains information on the following topics:

- [Introduction to generating PLC alarms with instructions (S7-400)](#introduction-to-generating-plc-alarms-with-instructions-s7-400)
- [NOTIFY_8P: Report up to eight signal changes (S7-400)](#notify_8p-report-up-to-eight-signal-changes-s7-400)
- [ALARM_8: Create PLC alarms without associated values for eight signals (S7-400)](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)
- [ALARM_8P: Create PLC alarms without associated values for eight signals (S7-400)](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)
- [NOTIFY: Report a signal change (S7-400)](#notify-report-a-signal-change-s7-400)
- [ALARM: Create PLC alarms with acknowledgement display (S7-400)](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)

#### Introduction to generating PLC alarms with instructions (S7-400)

##### Instructions for generating block-related alarms

You generate a PLC alarm by calling one of the following instructions in your program:

- "[NOTIFY](#notify-report-a-signal-change-s7-400)"
- "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)"
- "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)"
- "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)"
- "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)"

These instructions have the following properties:

- With "[NOTIFY](#notify-report-a-signal-change-s7-400)" and "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", all 0 -&gt; 1 or 1 -&gt; 0 signal changes detected during the call will cause an alarm to be sent.
- Also for "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)", every signal change detected for a call causes an alarm to be sent, provided acknowledgment-triggered reporting is inactive.  
  If, on the other hand, you have activated the acknowledgment-triggered reporting, then not every detected signal change will cause an alarm to be sent (see below for more information). In this case, a sent alarm is not displayed in the alarm display.
- After the block processing is complete, all of the associated values (SD_i inputs) are detected and the alarm is assigned (refer to "Send and receive parameters" in [Common parameters of instructions for S7 communication](S7%20communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400).)  
  The following applies with regard to the consistency of the associated values compared to higher priority classes: Every associated value SD_i is inherently consistent.
- With status parameters DONE, ERROR and STATUS, you monitor the processing status of the block (refer to "Status parameters" in [Common parameters of instructions for S7 communication](S7%20communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400)).

  > **Note**
  >
  > The parameters ID and EV_ID are only evaluated at the initial call of the block (the actual parameters or the defined values of the instance).

##### Logging on display devices

Before the instructions for generating PLC alarms can send an alarm when a signal change is detected, at least one display device must be logged on for PLC alarms. STATUS parameter = "1" if no login exists.

##### Signal change detection

One alarm memory with two memory locations is available for each instance of an alarm instruction.  
This alarm memory is initially empty. As soon as the instruction detects a signal change at the SIG input or at one of the inputs SIG_1, ... SIG_8, it is entered in the first memory location. It remains occupied until the associated alarm is sent.   
The next detected signal at the SIG or at one of the SIG_1, ... SIG_8 inputs is then entered in the second memory block. If the first memory block is still occupied and additional signals follow, then the second memory block in the alarm memory is always overwritten.  
The loss of this alarm is indicated via the output parameters ERROR and STATUS (ERROR=0, STATUS=11). In addition the logged on display devices get an alarm in this regard with the next alarm that can be sent.  
If he first memory block is free then the second memory block will be transferred into the first. Thus, the second memory block is cleared again.

##### Acknowledgment-triggered reporting

You can reduce alarm traffic ín your system by using acknowledgment-triggered alarm generation with the "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions.

That is, after an incoming alarm has been generated (Signal transition 0 &gt; 1) initially for a signal, subsequent alarms will not be generated until you have acknowledged the first alarm on a display device. The next alarm displayed on the display unit after your acknowledgment is an outgoing alarm (signal transition 1 to 0). Subsequently the alarm cycle restarts with an incoming alarm (signal change from 0 to 1) that must be acknowledged. In this manner you can control the reports of signal change (until the outgoing alarm) via the display device.

You specify the alarm generation method (enable or disable acknowledgment-triggered alarm generation) for the "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions globally for the CPU during configuration.

To ensure consistent alarm evaluation within your system, you should verify that all display devices can handle acknowledgment-triggered reporting.

> **Note**
>
> (Note on display devices that cannot handle acknowledgment-triggered reporting.)
>
> A CPU with enabled acknowledgment-triggered reporting will distribute the alarms only to display devices capable of handling this reporting method. The CPU will not send any alarms if none of the display devices can handle acknowledgment-triggered reporting. This situation is indicated once with ERROR=1 and STATUS=1.

##### Alarm acknowledgment for the instructions "ALARM", "ALARM_8" and "ALARM_8P"

A centralized acknowledgment concept is used. This means that, when you have acknowledged the alarm at a display device, the acknowledgment information is first sent to the CPU that generated the alarm. This then distributes the acknowledgment information to all stations logged on for this purpose.

You always acknowledge a signal and not an individual alarm. If, for example, several rising edges of a signal were indicated and you acknowledge the event entering the state, all previous events with the same alarm number count as having been acknowledged.

##### Acknowledgment display

The "[NOTIFY](#notify-report-a-signal-change-s7-400)" and "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)" instructions have no acknowledgment display. With "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", you can obtain the acknowledgment status from the ACK_UP and ACK_DN output parameters. With "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)", the acknowledgment status is available in the ACK_STATE output parameter. These outputs are updated when the block is called, providing the control parameter EN_R has the value "1".

##### Disabling and enabling alarms with the instruction or display device

In some situations, it may be useful to suppress alarms (e.g. when you reconfigure your system). You can therefore disable and enable alarms at the display device or in your program. Disabling/enabling applies to all stations that are logged on for the particular alarm. A disabled alarm remains disabled until it is enabled again.

You are informed of disabled alarms with the ERROR and STATUS output parameters (ERROR = 1, STATUS = 21).

##### Work memory required by the instructions for generating block-related alarms

For their proper operation, the instructions for generating PLC alarms require a communications data buffer in the work memory of the CPU (code area) that is generally dependent on the associated value. Refer to the table below for information on the size of used memory.

| Instruction | Required space (in bytes) in the work memory of the CPU |
| --- | --- |
| NOTIFY | 200 + 2 * length of the associated values specified at SD_1,...SD_10 at the first call |
| NOTIFY_8P | 200 + 2 * length of the associated values specified at SD_1,...SD_10 at the first call |
| ALARM | 200 + 2 * length of the associated values specified at SD_1,...SD_10 at the first call |
| ALARM_8 | 100 |
| ALARM_8P | 200 + 2 * length of the associated values specified at SD_1,...SD_10 at the first call |
| AR_SEND | 54 |

##### Amount of transferable data

The amount of data that can be transferred using the associated values SD_i of the "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)" and "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions must not exceed a maximum length. This maximum data length is calculated as follows:

maxleng =

min (pdu_local, pdu_remote) - diff - 4 * number of SD_i parameters used

Where:

- min (pdu_local, pdu_remote) is the lowest value of the numbers pdu_lokal and pdu_remote
- pdu_local is the maximum length of the fields of the local CPU (see the technical data of your CPU)
- pdu_remote: the maximum length for display device data blocks
- diff = 48, if acknowledgment-triggered reporting is enabled, and diff = 44 if disabled.

##### Example

A CPU 414-2 is sending alarms via Industrial Ethernet to HMI. Acknowledgment-triggered reporting is disabled.

The associated values SD_1, SD_2 and SD_3 are used.

pdu_local = 480 bytes, pdu_remote = 480 bytes,

Number of SD_i parameters used: 3

Result:

maxleng = min (480, 480) - 44 - 4 * 3 = 480 - 44 - 12 = 424

The maximum length of data that can be transferred per instruction is 424 bytes.

#### NOTIFY_8P: Report up to eight signal changes (S7-400)

##### Description

The "NOTIFY_8P" instruction extends the "[NOTIFY](#notify-report-a-signal-change-s7-400)" instruction to include eight signals.

An alarm is generated if at least one signal transition has been detected. An alarm is always generated at the first call of "NOTIFY_8P". All eight signals have a common alarm ID that is split into eight individual alarms on the display device.

One alarm memory with two memory locations is available for each instance of "NOTIFY_8P". For more information on the caching of signal changes, refer to [Introduction to generating PLC alarms with instructions](#introduction-to-generating-plc-alarms-with-instructions-s7-400).

> **Note**
>
> The display device shows the last two signal transitions, irrespective of alarm loss.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Calling "NOTIFY_8P"**  Before you call "NOTIFY_8P" in an automation system, you must ensure that all connected display devices are familiar with this block. If you fall to heed this instruction the communication between the automation system and the connected display devices will be aborted. In this case you can no longer access your system with its connected display devices. |  |

##### Parameters

The following table shows the parameters of the instruction "NOTIFY_8P":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SIG_i,   1 ≤ i ≤ 8 | Input | BOOL | I, Q, M, D, L | i-(nth) signal to be monitored |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE ID is only evaluated at the first call. |
| EV_ID | Input | C_NOTIFY_8P | I, Q, M, D, L | Alarm number (not allowed: 0) EV_ID is only evaluated at the first call. Subsequently, the alarm number used for the first call applies to every call of "NOTIFY_8P" with the corresponding instance DB.  The alarm number is assigned automatically. This ensures the consistency of the alarm numbers. The alarm number must be unique within your user program. |
| SEVERITY | Input | WORD | I, Q, M, D, L or constant | Weighting of the event  Possible values: 0 to 127 (value 0 means highest weighting); default value: 64  This parameter is irrelevant for processing the alarm. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE: Generation of  alarm is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR: ERROR=TRUE indicates that an error has occurred during processing. For details refer to parameter STATUS. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Displays error information |
| SD_i,  1 ≤ i ≤ 10 | InOut | ANY | I, Q, M, D, T, C | i-th associated value  Only the  BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME   **Note:** When the ANY pointer accesses a DB, the DB must always be specified.  (e.g.: P# DB10.DBX5.0 Byte 10) |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

The following table contains all specific error information for "NOTIFY_8P" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Alarm loss: The previous signal change or the previous alarm could not be sent and is replaced by the current alarm. |
| 0 | 22 | - Error in the pointer to the associated values SD_i:   - relating to the data length or the data type   - No access to associated values in user memory, for example, due to deleted DB or area length error   - The activated alarm is transferred without or, if required, with the maximum possible number of associated values. - The actual parameter you have selected for SEVERITY is higher than the permitted range. The activated alarm is sent with SEVERITY=127. |
| 0 | 25 | Communication has started. The alarm is being processed. |
| 1 | 1 | Communication problems: connection termination or no logon |
| 1 | 4 | At the first call:  - The specified EV_ID is outside the permitted range or - the ANY pointer SD_i has a formal error. - The maximum memory area that can be sent for the CPU per "NOTIFY_8P" has been exceeded. |
| 1 | 10 | Access to local user memory not possible (for example, access to  a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to "NOTIFY_8P" - A global DB was specified instead of an instance DB. |
| 1 | 18 | EV_ID was already used by the "[NOTIFY](#notify-report-a-signal-change-s7-400)", "NOTIFY_8P", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400) " or "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions. |
| 1 | 20 | Not enough work memory. |
| 1 | 21 | The alarm with the specified EV_ID is disabled. |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM_8: Create PLC alarms without associated values for eight signals (S7-400)

##### Description

Except for the non-existing, associated values SD_1, ..., SD_10, the instruction is identical to the "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)" instruction.

##### Parameters

The following table shows the parameters of the "ALARM_8" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter enabled to receive determines whether the output ACK_STATE is updated (EN_R=1) or not (EN_R=0) when the block is called. |
| SIG_i,  1≤i ≤8 | Input | BOOL | I, Q, M, D, L | i-(nth) signal to be monitored |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE ID is only evaluated at the first call. |
| EV_ID | Input | C_ALARM_8 | I, Q, M, D, L | Alarm number (not allowed: 0) EV_ID is only evaluated at the first call. Subsequently, the alarm number used for the first call applies to every call of "ALARM_8" with the corresponding instance DB.  The alarm number is assigned automatically. This ensures the consistency of the alarm numbers. The alarm number must be unique within your user program. |
| SEVERITY | Input | WORD | I, Q, M, D, L or constant | Weighting of the event   Possible values: 0 to 127 (value  0 means highest weighting)  This parameter is irrelevant for processing this alarm. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:  Generation of  alarm is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR: ERROR=TRUE indicates that an error has occurred during processing. For details refer to parameter STATUS. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Displays error information |
| ACK_STATE | Output | WORD | I, Q, M, D, L | Bit array with the current acknowledgement status of all eight alarms (1: Event acknowledged, 0: Event not acknowledged):  - Bits 0 to 7 are mapped to the incoming event of SIG_1 to SIG_8 - Bits 8 to 15 are mapped to the outgoing event of SIG_1 to SIG_8 - Initialization status: W#16#FFFF, that is, all incoming and outgoing events have been acknowledged |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

The following table contains all specific error information for the instruction "ALARM_8" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Alarm loss: The previous signal change or the previous alarm could not be sent and is replaced by the current alarm. |
| 0 | 22 | The actual parameter you have selected for SEVERITY is higher than the permitted range. The activated alarm is sent with SEVERITY=127. |
| 0 | 25 | Communication has started. The alarm is being processed. |
| 1 | 1 | Communication problems: connection termination or no logon  With acknowledgement-triggered reporting active: Temporary display, if display devices do not support acknowledgement-triggered reporting |
| 1 | 4 | At the first call, the specified EV_ID is outside the permitted range. |
| 1 | 10 | Access to local user memory not possible (for example, access to  a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to "ALARM_8" - A global DB was specified instead of an instance DB. |
| 1 | 18 | EV_ID was already used by the "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "ALARM_8" or "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions. |
| 1 | 20 | Not enough work memory. |
| 1 | 21 | The alarm with the specified EV_ID is disabled. |

> **Note**
>
> After the first call, all the bits of the ACK_STATE output are set and it is assumed that the previous values of SIG_i, 1 ≤ i ≤ 8 inputs were 0.

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM_8P: Create PLC alarms without associated values for eight signals (S7-400)

##### Description

The instruction is the extension of "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)" to include eight signals.

As long as you have not enabled acknowledgement-triggered reporting, an alarm will always be generated when a signal transition is detected at one or more signals (exception: a alarm is always sent at the first block call). All eight signals have a common alarm ID that is split into eight separate alarms on the display device. You can acknowledge each individual alarm separately or a group of alarms at once.

Use the output parameter ACK_STATE to further process the acknowledgement status of the specific alarms in your program. If you enable or release an alarm of an "ALARM_8P" instruction, this action always affects the entire "ALARM_8P" instruction. Disabling and enabling of individual signals is not possible.

One alarm memory with two memory locations is available for each instance of "ALARM_8P". For more information on the caching of signal changes, refer to [Introduction to generating PLC alarms with instructions](#introduction-to-generating-plc-alarms-with-instructions-s7-400).

##### Parameters

The following table shows the parameters of the "ALARM_8P" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter enabled to receive determines whether the output ACK_STATE is updated (EN_R=1) or not (EN_R=0) when the block is called. |
| SIG_i,  1≤i ≤8 | Input | BOOL | I, Q, M, D, L | i-(nth) signal to be monitored |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE ID is only evaluated at the first call. |
| EV_ID | Input | C_ALARM_8P | I, Q, M, D, L | Alarm number (not allowed: 0); EV_ID is only evaluated at the first call. Subsequently, the alarm number used for the first call applies to every call of "ALARM_8P" with the corresponding instance DB.  The alarm number is assigned automatically. This ensures the consistency of the alarm numbers. The alarm number must be unique within your user program. |
| SEVERITY | Input | WORD | I, Q, M, D, L or constant | Weighting of the event   Possible values: 0 to 127 (value  0 means highest weighting)  This parameter is irrelevant for processing this alarm. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:  Generation of  alarm is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR ERROR=TRUE indicates that an error has occurred during processing. For details refer to parameter STATUS. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Displays error information |
| ACK_STATE | Output | WORD | I, Q, M, D, L | Bit array with the current acknowledgement status of all eight alarms (1: Event acknowledged, 0: Event not acknowledged):  - Bits 0 to 7 are mapped to the incoming event of SIG_1 to SIG_7 - Bits 8 to 15 are mapped to the outgoing event of SIG_1 to SIG_7 - Initialization status: W#16#FFFF, that is, all incoming and outgoing events have been acknowledged |
| SD_j,  1≤ j ≤10 | InOut | ANY | I, Q, M, D, T, C | j-th associated value  The associated values apply for all alarms. Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME.   **Note:** When the ANY pointer accesses a DB, the DB must always be specified (for example: P# DB10.DBX5.0 byte 10). |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

The following table contains all specific error information for the "ALARM_8P" instruction that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS   (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Alarm loss: The previous signal change or the previous alarm could not be sent and is replaced by the current alarm. |
| 0 | 22 | - Error in the pointer to the associated values SD_i:   - relating to the data length or the data type   - No access to associated values in user memory, for example, due to deleted DB or area length error   - The activated alarm is sent without associated values - The actual parameter you have selected for SEVERITY is higher than the permitted range. The activated alarm is sent with SEVERITY=127 . |
| 0 | 25 | Communication has started. The alarm is being processed. |
| 1 | 1 | Communication problems: Connection termination or no logon.  With acknowledgement-triggered reporting active: Temporary display, if display devices do not support acknowledgement-triggered reporting. |
| 1 | 4 | At the first call:  - The specified EV_ID is outside the permitted range or - the ANY pointer SD_i has a formal error. - The maximum memory area that can be sent for the CPU per "ALARM_8P" has been exceeded. |
| 1 | 10 | Access to local user memory not possible (for example, access to  a deleted DB). |
| 1 | 12 | When the instruction was called:  - An instance DB was specified that does not belong to "ALARM_8P" - A global DB was specified instead of an instance DB. |
| 1 | 18 | EV_ID was already used by the "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" or "ALARM_8P" instructions. |
| 1 | 20 | Not enough work memory. |
| 1 | 21 | The alarm with the specified EV_ID is disabled. |

> **Note**
>
> After the first call, all the bits of the ACK_STATE output are set and it is assumed that the previous values of SIG_i, 1&lt; i &lt; 8 inputs were "0".

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### NOTIFY: Report a signal change (S7-400)

##### Description

The instruction monitors a signal. It generates an alarm both on a rising edge (incoming event) and on a falling edge (outgoing event). You can have up to ten associated values sent with the alarm. The alarm is sent to all stations logged on for this purpose. When the SFB is first called, an alarm with the current signal state is sent.

The associated values are queried when the edge is detected and assigned to the alarm.

One alarm memory with two memory locations is available for each instance of the instruction. For more information on the caching of signal changes, refer to [Introduction to generating PLC alarms with instructions](#introduction-to-generating-plc-alarms-with-instructions-s7-400).

The "NOTIFY" instruction conforms to IEC 1131-5.

##### Parameter

The following table shows the parameters of the instruction "NOTIFY":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SIG | Input | BOOL | I, Q, M, D, L | The signal to be monitored |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE ID is only evaluated at the first call. |
| EV_ID | Input | C_NOTIFY | I, Q, M, D, L | Alarm number (not allowed: 0) EV_ID is only evaluated at the first call. Subsequently, the alarm number used for the first call applies to every call of "NOTIFY" with the corresponding instance DB.  The alarm number is assigned automatically. This ensures the consistency of the alarm numbers. The alarm number must be unique within your user program. |
| SEVERITY | Input | WORD | I, Q, M, D, L or constant | Weighting of the event  Possible values: 0 to 127 (value  0 means highest weighting)  This parameter is irrelevant for processing this alarm. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE: Generation of  alarm is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR ERROR=TRUE indicates that an error has occurred during processing. For details refer to parameter STATUS. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Displays error information |
| SD_i,  1≤i ≤10 | InOut | ANY | I, Q, M, D, T, C | i-th associated value  Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME.   **Note:** When the ANY pointer accesses a DB, the DB must always be specified.  (e.g.: P# DB10.DBX5.0 Byte 10) |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

The following table contains all specific error information that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Alarm loss: The previous signal change or the previous alarm could not be sent and is replaced by the current alarm. |
| 0 | 22 | - Error in the pointer to the associated values SD_i:   - relating to the data length or the data type   - No access to associated values in user memory, for example, due to deleted DB or area length error   - The activated alarm is transferred without or, if required, with the maximum possible number of associated values. - The actual parameter you have selected for SEVERITY is higher than the permitted range. The activated alarm is sent with SEVERITY=127 . |
| 0 | 25 | Communication has started. The alarm is being processed. |
| 1 | 1 | Communication problems: connection termination or no logon |
| 1 | 4 | At the first call:  - The specified EV_ID is outside the permitted range or - the ANY pointer SD_i has a formal error. - The maximum memory area that can be sent for the CPU per "NOTIFY" has been exceeded. |
| 1 | 10 | Access to local user memory not possible (for example, access to  a deleted DB). |
| 1 | 12 | When the instruction was called:  - An instance DB was specified that does not belong to "NOTIFY" - A global DB was specified instead of an instance DB. |
| 1 | 18 | EV_ID was already used by the "NOTIFY", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" or "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions. |
| 1 | 20 | Not enough work memory. |
| 1 | 21 | The alarm with the specified EV_ID is disabled. |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM: Create PLC alarms with acknowledgement display (S7-400)

##### Description

The instruction monitors a signal.

- Default mode (that is, acknowledgement triggered reporting is disabled): The block generates an alarm both on a rising edge (incoming event) and on a falling edge (outgoing event). You can have up to ten associated values sent with the alarm.
- Acknowledgement-triggered reporting is enabled: After an incoming alarm is generated, the block will no longer create alarms for the signal until you have acknowledged this incoming alarm on a display device.

  See also: [Introduction to generating PLC alarms with instructions](#introduction-to-generating-plc-alarms-with-instructions-s7-400).

The alarm is sent to all stations logged on for this purpose.

When the SFB is first called, an alarm with the current signal state is sent.

The ACK_UP output is reset at the rising edge. It is set when your acknowledgement of the incoming event has arrived from a logged on display device.

The situation for the ACK_DN output is analogous: this is reset at the falling edge. It is set when your acknowledgement of the outgoing event is received from a logged on display device. Once your acknowledgement has been received from a logged on display device, the acknowledgement information is passed on to all other stations logged on for this purpose.

One alarm memory with two memory locations is available for each instance of the "ALARM" instruction. For more detailed information on buffering of signal changes, refer to Section "Signal change detection" in [Introduction to generating PLC alarms with instructions](#introduction-to-generating-plc-alarms-with-instructions-s7-400).

The "ALARM" instruction conforms to IEC 1131-5.

##### Parameters

The following table shows the parameters of the "ALARM" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter enabled to receive decides whether the outputs ACK_UP and ACK_DN are updated at the first block call (EN_R=1) or not (EN_R=0). If EN_R=0, then the output  parameters ACK_UP and ACK_DN  remain unchanged. |
| SIG | Input | BOOL | I, Q, M, D, L | The signal to be monitored |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE ID is only evaluated at the first call. |
| EV_ID | Input | C_ALARM | I, Q, M, D, L | Alarm number (not allowed: 0)  EV_ID is only evaluated at the first call. Subsequently, the alarm number used for the first call applies to every call of "ALARM" with the corresponding instance DB. The alarm number will be assigned automatically. This ensures the consistency of the alarm numbers. The alarm number must be unique within your user program. |
| SEVERITY | Input | WORD | I, Q, M, D, L or constant | Weighting of the event   Possible values: 0 to 127 (value  0 means highest weighting)  This parameter is irrelevant for processing this alarm. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:  Generation of  alarm is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR ERROR=TRUE indicates that an error has occurred during processing. For details refer to parameter STATUS. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Displays error information |
| ACK_DN | Output | BOOL | I, Q, M, D, L | Event leaving state was acknowledged  on a display device  Initialization status: 1 |
| ACK_UP | Output | BOOL | I, Q, M, D, L | Incoming event was  acknowledged on a display device  Initialization status: 1 |
| SD_i,  1≤i ≤10 | InOut | ANY | I, Q, M, D, T, C | i-th associated value  Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME.   **Note:** When the ANY pointer accesses a DB, the DB must always be specified. (e.g.: P# DB10.DBX5.0 Byte 10) |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

The following table contains all specific error information for the instruction "ALARM" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS  (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Alarm loss: The previous signal change or the previous alarm could not be sent and is replaced by the current alarm. |
| 0 | 22 | - Error in the pointer to the associated values SD_i:   - Involving the data length or the data type   - No access to associated values in user memory, for example, due to deleted DB or area length error   - The activated alarm is sent without associated values - The actual parameter you have selected for SEVERITY is higher than the permitted range. The activated alarm is sent with SEVERITY=127. |
| 0 | 25 | Communication has started. The alarm is being processed. |
| 1 | 1 | Communication problems: connection termination or no logon  With acknowledgement-triggered reporting active: Temporary display, if display devices do not support acknowledgement-triggered reporting |
| 1 | 4 | At the first call:  - The specified EV_ID is outside the permitted range or - the ANY pointer SD_i has a formal error. - The maximum memory area that can be sent for the CPU per "ALARM " has been exceeded. |
| 1 | 10 | Access to local user memory not possible (for example, access to  a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to ALARM - A global DB was specified instead of an instance DB. |
| 1 | 18 | EV_ID was already used by the "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "ALARM", "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" or "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions. |
| 1 | 20 | Not enough work memory. |
| 1 | 21 | The alarm with the specified EV_ID is disabled. |

> **Note**
>
> After the first call, the ACK_UP and ACK_DN outputs have the value "1" and it is assumed that the previous value of the SIG input was "0".

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

### Instructions for generating PLC alarms without instance DB (S7-300, S7-400)

This section contains information on the following topics:

- [Startup characteristics of the instructions for generating PLC alarms (S7-300, S7-400)](#startup-characteristics-of-the-instructions-for-generating-plc-alarms-s7-300-s7-400)
- [Error behavior of instructions for generating PLC alarms (S7-300, S7-400)](#error-behavior-of-instructions-for-generating-plc-alarms-s7-300-s7-400)
- [Introduction to generating PLC alarms with instructions (S7-300, S7-400)](#introduction-to-generating-plc-alarms-with-instructions-s7-300-s7-400)
- [ALARM_S: Generate alarm message (S7-300, S7-400)](#alarm_s-generate-alarm-message-s7-300-s7-400)
- [ALARM_SQ: Generate alarm message with acknowledgement (S7-300, S7-400)](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)
- [ALARM_D: Create permanently acknowledged PLC alarms (S7-300, S7-400)](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)
- [ALARM_DQ: Create acknowledgeable PLC alarms (S7-300, S7-400)](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)
- [ALARM_SC: Determine acknowledgement status of  the last ALARM_SQ incoming alarm (S7-300, S7-400)](#alarm_sc-determine-acknowledgement-status-of-the-last-alarm_sq-incoming-alarm-s7-300-s7-400)

#### Startup characteristics of the instructions for generating PLC alarms (S7-300, S7-400)

##### Warm restart behavior

During a warm restart, the instance DBs of the instructions for generating PLC alarms are set to the not initialized status. The actual parameters stored in the instance DBs are unchanged. The parameters ID and EV_ID will be re-evaluated at the next block call.

##### Cold restart behavior

During a cold restart, the contents of the instance DBs of the instructions for generating PLC alarms are set to their initial values.

##### Hot restart

During a hot restart, the instructions for generating PLC alarms behave like user function blocks that are capable of resuming execution. They continue from the point of interruption.

##### Memory reset

A memory reset always causes the termination of all connections so that no station is logged on for alarms. The user program is deleted. If you have inserted a FLASH card, the program sections relevant to execution are loaded on the CPU again from the card and the CPU executes a warm or cold restart (implicitly this is always a cold restart, since all user data are initialized after clearing memory).

#### Error behavior of instructions for generating PLC alarms (S7-300, S7-400)

##### Connection termination

The connections assigned to the instances are monitored for termination. If a connection is terminated, the stations involved are removed from the internal CPU list of stations logged on for PLC alarms. Any alarms pending for these stations are deleted.

If other stations are still logged on following a connection termination, they continue to receive alarms. The instructions only stop sending alarms when there are no more connections to any logged on stations. The ERROR and STATUS output parameters indicate this situation (ERROR = 1, STATUS = 1).

##### Error interface to the user program

If an error occurs during the execution of an instruction for generating PLC alarms, the ERROR output parameter is set to "1" and the STATUS output parameter has the corresponding error identifier. You can evaluate this error information in your program.

Examples of possible errors:

- Sending not possible due to lack of resources
- Error accessing one of the signals to be monitored.

#### Introduction to generating PLC alarms with instructions (S7-300, S7-400)

##### Instructions for generating PLC alarms

You can generate a PLC alarm with the following instructions:

- "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)"
- "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)"
- "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)"
- "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)"

These instructions have the following properties:

- The PLC alarms of "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" and "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" sent with signal state "1" can be acknowledged from a logged-on display device. The PLC alarms of "[ALARM_S"](#alarm_s-generate-alarm-message-s7-300-s7-400) and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" are always acknowledged implicitly.
- It is not a detected edge change, but rather every call that generates a PLC alarm.
- After the block processing the associated value SD is completely entered and allocated to the PLC alarm.  
  The following applies for the associated value regarding the consistency relative to higher priority classes: The following are consistent:

  - The simple data types (bit, byte, word, and double word)
  - an array of the data type byte up to a maximum length specific for a CPU

##### ALARM_SC

With the "[ALARM_SC](#alarm_sc-determine-acknowledgement-status-of-the-last-alarm_sq-incoming-alarm-s7-300-s7-400)" instruction, you can:

- Determine the acknowledgement status of the last "incoming alarm" and the signal status at the last call of "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" / "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)", or
- Determine the signal status at the last call of "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" / "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)".

##### Logging on display devices

The instructions for generating PLC alarms only send a PLC alarm when they are called if at least one display device has logged on for PLC alarms.

##### Alarm storage

To avoid alarms being lost when there is a lot of traffic on the communications system, the "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)", "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)", "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" instructions can each buffer two alarms.

If PLC alarms are still lost, you will be informed in RET_VAL. The logged on display devices are informed of this the next time a PLC alarm can be sent.

##### Alarm acknowledgement for the instructions "ALARM_SQ" and "ALARM_DQ"

If you have acknowledged an "incoming alarm" at a display device, this acknowledgement information is first sent to the CPU where the alarm originated. This then distributes the acknowledgement information to all stations logged on for this purpose.

##### Disabling and enabling alarms

You cannot disable and then re-enable PLC alarms that you have generated with "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" or "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" or "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" or "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)".

##### Changes in your program containing "ALARM_SQ" / "ALARM_S" calls

> **Note**
>
> When you download a block with "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" / "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" calls that is already on the CPU, it is possible that the previous block has sent an incoming PLC alarm but that the new block has not sent a corresponding outgoing PLC alarm. This means that the alarm remains in the internal alarm memory of the CPU. This status can also occur if you delete blocks with "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" / "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" calls.
>
> You can remove such PLC alarms from the internal alarm memory of the CPU by changing the CPU to STOP mode and then executing a warm restart or cold restart.

##### Changes in your program containing "ALARM_DQ" / "ALARM_D" calls

Even though your program might contain "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and/or "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" calls, the program modifications described above may cause the PLC alarms to become resident in the internal alarm memory and thus permanently occupy system resources.

In contrast to system resources that were allocated by "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" / "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" calls, you can again release system resources allocated by "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" / "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" calls without having to switch your CPU to STOP mode. The "[DEL_SI](#del_si-delete-dynamically-assigned-system-resources-s7-300-s7-400)" instruction is used for this purpose. Before you enable dynamically-allocated system resources by calling "DEL_SI", it is advisable to use the "READ_SI" instruction to output information regarding the system resources of your CPU that are currently dynamically allocated (see instruction "[READ_SI](#read_si-read-out-dynamically-assigned-system-resources-s7-300-s7-400)").

##### Amount of transferable data

The amount of data that can be transferred using the associated values SD of the "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)", "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)", "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" and "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" instructions must not exceed a maximum length. This maximum data length is calculated as follows:

maxleng = min (pdu_local, pdu_remote) - 48

Where:

- pdu_local: the maximum length of CPU data blocks (SZL_ID W#16#0131, INDEX 1, tag pdu)
- pdu_remote: the maximum length for display device data blocks

##### Example

A CPU 414-2 sends an alarm to a programming device PG 760 (via MPI).

pdu_local = 480 bytes, pdu_remote = 480 bytes,

Result:

maxleng = min (480, 480) - 48 = 480 - 48 = 432

The maximum length of data that can be transferred per instruction is 432 bytes.

#### ALARM_S: Generate alarm message (S7-300, S7-400)

##### Description

With every call, the instruction generates an alarm to which you can append an associated value. The alarm is sent to all stations logged on for this purpose. The instruction provides you with a simple alarm mechanism. You must make sure that you call the instruction only when the value of the alarm-triggering signal SIG is inverted compared to the last call. If this is not the case, then this situation will be indicated in RET_VAL and no alarm will be sent. With the very first call of the instruction you must ensure that the value "1" is applied at the SIG input. Otherwise you will get error information via RET_VAL and no alarm will be sent.

> **Note**
>
> In newly created programs you should use only the "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" instruction (provided your CPU supports this instruction) because they provide improved options for managing system resources.

##### Use of system resources

When alarms are generated the operating system allocates a system resource for the duration of one signal cycle.

The signal cycle lasts from the call with SIG=1 until the next call with SIG=0. If, during the signal cycle, the alarm-generating block is overloaded or deleted, the associated system resource remains assigned until the next restart (warm restart).

##### Acknowledging alarms

Alarms you have sent with "ALARM_S" are always implicitly acknowledged. You can determine the signal state at the last "ALARM_S" call using "[ALARM_SC](#alarm_sc-determine-acknowledgement-status-of-the-last-alarm_sq-incoming-alarm-s7-300-s7-400)".

##### Caching signal states

The ALARM_S" instruction allocates system resources Here among other things the last two signal states, including time stamp and associated value are placed in the buffer. If "ALARM_S" is called at a time when the signal states of the two last "valid" calls have not yet been sent (signal overflow), the current signal state and the last signal state are discarded and an overflow ID is set in the buffer. At the next possible opportunity, the next to last signal and the overflow identifier are sent.

Example:

![Caching signal states](images/18047497355_DV_resource.Stream@PNG-de-DE.png)

If t<sub>0</sub>, t<sub>1</sub> and t<sub>2</sub> are the call times of "ALARM_S". If the signal states of t<sub>0</sub> and t<sub>1</sub> have not yet been sent at the time t<sub>2</sub>, the signal states of t<sub>1</sub> and t<sub>2</sub> will be discarded and the overflow identifier is set at the signal state of t<sub>0</sub>.

##### Instance overflow

If the number of "ALARM_S" calls is greater than the maximum number of CPU system resources, this may result in a lack of resources (instance overflow). This situation is indicated both by the information in RET_VAL as well as by indications at the logged on display devices.

The maximum number of "ALARM_S" calls is dependent on the CPU.

##### Parameter

The following table shows the parameters of the instruction "ALARM_S":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SIG | Input | BOOL | I, Q, M, D, L | The alarm triggering signal |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE |
| EV_ID | Input | C_ALARM_S | I, Q, M, D, L | Alarm number (not allowed: "0") |
| SD | Input | ANY | I, Q, M, D, T, C | Associated value  Maximum length: 12 bytes  Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 0001 | - The length of the associated value exceeds the maximum permitted length. - Access to user memory not possible (for example, access to deleted DB). The alarm is sent. - The associated value points to a value in the local data area. The alarm is sent. (S7-400 only) |
| 0002 | Warning: The last free alarm acknowledge memory was assigned. (S7-400 only) |
| 8081 | The specified EV_ID is outside the permitted range or |
| 8082 | Alarm loss because your CPU has no more resources for generating PLC alarms with instructions. |
| 8083 | Alarm loss, because the same signal transition is already present but could not be sent yet (signal overflow). |
| 8084 | With the current and the previous "ALARM_S", the alarm-triggering signal SIG has the same value. |
| 8085 | There is no logon for the specified EV_ID. |
| 8086 | A call for the specified EV_ID is already being processed in a lower priority class. |
| 8087 | During the first call of "ALARM_S", the alarm-triggering signal had the value "0". |
| 8088 | The specified EV_ID is already in use by another system resource ("ALARM_S", [ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400), [ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM_SQ: Generate alarm message with acknowledgement (S7-300, S7-400)

##### Description

With every call, the instruction generates an alarm to which you can append an associated value. The alarm is sent to all stations logged on for this purpose. "ALARM_SQ" also provides you with a simple alarm mechanism. You must make sure that you call "ALARM_SQ" only when the value of the alarm-triggering signal SIG is inverted to the last call. If this is not the case, then this situation will be indicated in RET_VAL and no alarm will be sent. Thus with the very first call of "ALARM_SQ", you must ensure that the value "1" is applied at the SIG input. Otherwise you will get error information via RET_VAL and no alarm will be sent.

> **Note**
>
> In newly created programs you should use only the "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" instruction (provided your CPU supports this instruction) because they provide improved options for managing system resources.

##### Use of system resources

When alarms are generated with "ALARM_SQ", the operating system allocates a system resource for the duration of one signal cycle.

With "ALARM_SQ", the signal cycle lasts from the call with SIG=1 until the next call with SIG=0. Added to this time interval is possibly also the time until the acknowledgement of the incoming signal by a logged on display device.

If, during the signal cycle, the alarm-generating block is overloaded or deleted, the associated system resource remains assigned until the next restart (warm restart).

##### Acknowledging alarms

On a logged-on display device, you can acknowledge the alarms with signal status "1" sent by "ALARM_SQ". You can determine the acknowledgement status of the last "incoming alarm" and the signal status at the last "ALARM_SQ" call using "[ALARM_SC](#alarm_sc-determine-acknowledgement-status-of-the-last-alarm_sq-incoming-alarm-s7-300-s7-400)".

##### Caching signal states

"ALARM_SQ" allocates system resources Here among other things the last two signal states, including time stamp and associated value are placed in the buffer. If "ALARM_SQ" is called at a time when the signal states of the two last "valid" calls have not yet been sent (signal overflow), the current signal state and the last signal state are discarded and an overflow ID is set in the buffer. At the next possible opportunity, the next to last signal and the overflow identifier are sent.

Example:

![Caching signal states](images/18047849355_DV_resource.Stream@PNG-de-DE.png)

If t<sub>0</sub>, t<sub>1</sub> and t<sub>2</sub> are the call times of "ALARM_SQ". If the signal states of t<sub>0</sub> and t<sub>1</sub> have not yet been sent at the time t<sub>2</sub>, the signal states of t<sub>1</sub> and t<sub>2</sub> will be discarded and the overflow identifier is set at the signal state of t<sub>0</sub>.

##### Instance overflow

If the number of "ALARM_SQ" calls is greater than the maximum number of CPU system resources, this may result in a lack of resources (instance overflow). This situation is indicated both by the information in RET_VAL as well as by indications at the logged on display devices.

The maximum number of "ALARM_SQ" calls is dependent on the CPU.

##### Parameter

The following table shows the parameters of the instruction "ALARM_SQ":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SIG | Input | BOOL | I, Q, M, D, L | The alarm triggering signal |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE |
| EV_ID | Input | C_ALARM_S | I, Q, M, D, L | Alarm number (not allowed: 0) |
| SD | Input | ANY | I, Q, M, D, T, C | Associated value  Maximum length: 12 bytes  Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 0001 | - The length of the associated value exceeds the maximum permitted length. - Access to user memory not possible (for example, access to deleted DB). The alarm is sent. - The associated value points to a value in the local data area. The alarm is sent. (S7-400 only) |
| 0002 | Warning: The last free alarm acknowledge memory was assigned. (S7-400 only) |
| 8081 | The specified EV_ID is outside the permitted range or |
| 8082 | Alarm loss because your CPU has no more resources for generating PLC alarms with instructions. |
| 8083 | Alarm loss, because the same signal transition is already present but could not be sent yet (signal overflow). |
| 8084 | With the current and the previous "ALARM_SQ", the alarm-triggering signal SIG has the same value. |
| 8085 | There is no logon for the specified EV_ID. |
| 8086 | A call for the specified EV_ID is already being processed in a lower priority class. |
| 8087 | During the first call of "ALARM_SQ", the alarm-triggering signal had the value "0". |
| 8088 | The specified EV_ID is already in use by another system resource ([ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400), [ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400), [ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM_D: Create permanently acknowledged PLC alarms (S7-300, S7-400)

##### Description

With every call, the instruction generates a PLC alarm to which you can append an associated value. It conforms to the "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" instruction in this regard.

When alarms are generated with "ALARM_D", the operating system allocates a system resource for the duration of one signal cycle.

With "ALARM_D", the signal cycle lasts from the call with SIG=1 until the next call with SIG=0. If, during the signal cycle, the alarm-generating block is overloaded or deleted, the associated system resource remains assigned until the next restart (warm restart).

Compared to the "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" instruction, "ALARM_D" has an additional functionality that allows it to manage allocated system resources.

- With the help of READ_SI, you can read information regarding allocated system resources.
- With DEL_SI, you can re-enable allocated system resources. This is of special significance for permanently assigned system resources. A currently allocated system resource, for example, stays allocated until the next restart (warm restart) if you delete an FB call that contains "ALARM_D" calls in the course of a program change. When you change the program and reload an FB with "ALARM_D" calls, it may be the case that "ALARM_D" does not generate any more PLC alarms.

The instruction "ALARM_D" contains one parameter more than the "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" instruction, namely the input CMP_ID. You use this input to assign the PLC alarms generated by the "ALARM_D" instruction to logical areas, for example, to parts of the system. If you call "ALARM_D" in an FB, the obvious thing to do is to assign the number of the corresponding instance DB to "CMP_ID".

##### Parameter

The following table shows the parameters of the instruction "ALARM_D":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SIG | Input | BOOL | I, Q, M, D, L | The alarm triggering signal |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE |
| EV_ID | Input | C_ALARM_S | I, Q, M, D, L | Alarm number (not allowed: 0) |
| CMP_ID | Input | DWORD | I, Q, M, D, L or constant | component identifier (not permitted: 0)  ID for the subsystem to which the corresponding alarm is assigned  Recommended values:  - Low word: 1 to 65535 - High word: 0   You will not have any problems with the SIEMENS program package if you comply with these recommendations. |
| SD | Input | ANY | I, Q, M, D, T, C | Associated value  Maximum length: 12 bytes  Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 0001 | - The length of the associated value exceeds the maximum permitted length, or - Access to user memory not possible (for example, access to deleted DB). The alarm is sent. - The associated value points to a value in the local data area. The alarm is sent. (S7-400 only) |
| 0002 | Warning: The last free alarm acknowledge memory was assigned. (S7-400 only) |
| 8081 | The specified EV_ID is outside the permitted range or |
| 8082 | Alarm loss because your CPU has no more resources for generating PLC alarms with instructions. |
| 8083 | Alarm loss, because the same signal transition is already present but could not be sent yet (signal overflow). |
| 8084 | With the current and the previous "ALARM_D", the alarm-triggering signal SIG has the same value. |
| 8085 | There is no logon for the specified EV_ID. |
| 8086 | A call for the specified EV_ID is already being processed in a lower priority class. |
| 8087 | During the first call of "ALARM_D", the alarm-triggering signal had the value "0". |
| 8088 | The specified EV_ID is already in use by another system resource ("[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)", "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)", "[ALARM_DQ"](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)). |
| 8089 | You have assigned the value "0" to CMP_ID. |
| 808A | CMP_ID does not match EV_ID |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM_DQ: Create acknowledgeable PLC alarms (S7-300, S7-400)

##### Description

With every call, the instruction "ALARM_DQ" generates an alarm to which you can append an associated value. They conform to the "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" instruction in this regard.

When alarms are generated with "ALARM_DQ", the operating system allocates a system resource for the duration of one signal cycle.

With "ALARM_DQ", the signal cycle lasts from the call with SIG=1 until the next call with SIG=0. Added to this time interval is possibly also the time until the acknowledgement of the incoming signal by a logged on display device.

If, during the signal cycle, the alarm-generating block is overloaded or deleted, the associated system resource remains assigned until the next restart (warm restart).

The additional functionality of "ALARM_DQ" compared to the "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" instruction allows "ALARM_DQ" to manage occupied system resources .

- With the help of "[READ_SI](#read_si-read-out-dynamically-assigned-system-resources-s7-300-s7-400)", you can read information regarding occupied system resources.
- With "[DEL_SI](#del_si-delete-dynamically-assigned-system-resources-s7-300-s7-400)", you can release occupied system resources again. This is of special significance for permanently assigned system resources. A currently allocated system resource, for example, stays allocated until the next restart (warm restart) if you delete an FB call that contains "ALARM_DQ" calls in the course of a program change. When you change the program and reload an FB with "ALARM_DQ" calls, it may be the case that "ALARM_DQ" does not generate any more alarms.

The "ALARM_DQ" instruction contains one parameter more than the "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" instruction, namely the input CMP_ID. You use this input to assign the alarms generated by the "ALARM_DQ" instruction to logical areas, for example, to parts of the system. If you call "ALARM_DQ" in an FB, the obvious thing to do is to assign the number of the corresponding instance DB to CMP_ID.

##### Parameter

The following table shows the parameters of the instruction "ALARM_DQ":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SIG | Input | BOOL | I, Q, M, D, L | The alarm triggering signal |
| ID | Input | WORD | I, Q, M, D, L or constant | Data channel for alarms: W#16#EEEE |
| EV_ID | Input | C_ALARM_S | I, Q, M, D, L | Alarm number (not allowed: 0) |
| CMP_ID | Input | DWORD | I, Q, M, D, L or constant | component identifier (not permitted: 0); ID for the subsystem to which the corresponding alarm is assigned  Recommended values:  - Low word: 1 to 65535 - High word: 0   You will not have any problems with the SIEMENS program package if you comply with these recommendations. |
| SD | Input | ANY | I, Q, M, D, T, C | Associated value  Maximum length: 12 bytes  Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME |
| RET_VAL | Return | INT | I, Q, M, D, L | Display |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 0001 | - The length of the associated value exceeds the maximum permitted length, or - Access to user memory not possible (for example, access to deleted DB). The alarm is sent. - The associated value points to a value in the local data area. The alarm is sent. (S7-400 only) |
| 0002 | Warning: The last free alarm acknowledge memory was assigned. (S7-400 only) |
| 8081 | The specified EV_ID is outside the permitted range or |
| 8082 | Alarm loss because your CPU has no more resources for generating PLC alarms with instructions. |
| 8083 | Alarm loss, because the same signal transition is already present but could not be sent yet (signal overflow). |
| 8084 | With the current and the previous "ALARM_DQ", the alarm-triggering signal SIG has the same value. |
| 8085 | There is no logon for the specified EV_ID. |
| 8086 | A call for the specified EV_ID is already being processed in a lower priority class. |
| 8087 | During the first call of "ALARM_DQ", the alarm-triggering signal had the value "0". |
| 8088 | The specified EV_ID is already in use by another system resource ([ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400) , [ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400) , [ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)). |
| 8089 | You have assigned the value "0" to CMP_ID . |
| 808A | CMP_ID does not match EV_ID |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

#### ALARM_SC: Determine acknowledgement status of ?the last ALARM_SQ incoming alarm (S7-300, S7-400)

##### Description

You use the instruction to do the following:

- Determine the acknowledgement status of the last "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" / "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" incoming alarm and the status of the alarm-triggering signal when the last "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)" / "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400) " was called, or
- Determine the status of the alarm-triggering signal at the last "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)" / "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" call.

The alarm or the signal is uniquely referenced via the alarm number that you assign here, if you have assigned alarms numbers via the alarm configuration.

The instruction accesses the temporarily allocated memory of the "[ALARM_SQ](#alarm_sq-generate-alarm-message-with-acknowledgement-s7-300-s7-400)", "[ALARM_S](#alarm_s-generate-alarm-message-s7-300-s7-400)", "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" instructions.

##### Parameter

The following table shows the parameters of the instruction "ALARM_SC":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EV_ID | Input | C_ALARM_S | I, Q, M, D, L | Alarm number for which you want to determine the signal state at  the last call or the acknowledgement  status of the last incoming alarm  (only with ALARM_SQ and with ALARM_DQ). |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| STATE | Output | BOOL | I, Q, M, D, L | State of the alarm-triggering signal at the last call |
| Q_STATE | Output | BOOL | I, Q, M, D, L | - If the specified EV_ID parameter belongs to an "ALARM_S" / "ALARM_D" call: "1" - If the specified EV_ID parameter belongs to an "ALARM_SQ" / "ALARM_DQ" call: Acknowledgement status of  the last incoming alarm:   - 0: Not acknowledged   - 1: Acknowledged |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8081 | The specified EV_ID is outside the permitted range or |
| 8082 | No memory location is currently assigned to this EV_ID (possible cause: The  corresponding signal state was never "1" or its signal state has already  returned to "0"). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

---

**See also**

[Creating program alarms (S7-300, S7-400)](Configuring%20alarms.md#creating-program-alarms-s7-300-s7-400)

### WR_USMSG: Write a user diagnostics event to the diagnostic buffer (S7-300, S7-400)

#### Description

You use the instruction to write a user diagnostics result in the diagnostics buffer. You can also send the corresponding user diagnostics alarm to all stations logged on for this purpose (by setting the input parameter SEND = TRUE). If an error occurs, the output parameter RET_VAL provides the error information.

#### Sending user diagnostics alarm

The instruction writes a user diagnostics event to the diagnostics buffer. You can also send the corresponding user diagnostics alarm to all stations logged on for this purpose (by setting the input parameter SEND = TRUE). The user diagnostics alarm is then written to the send buffer and automatically sent to the stations logged on for this purpose.

You can check whether the sending of user diagnostics alarms is currently possible. To do this, call the "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" instruction with the SZL_ID = W#16#0132 and INDEX = W#16#0005 parameters. The fourth word of the data record supplied in this manner indicates whether sending is currently possible (1) or not (0).

![Sending user diagnostics alarm](images/18048649739_DV_resource.Stream@PNG-en-US.png)

#### Send buffer full

The user diagnostics alarm can only be entered in the send buffer if the send buffer is not full. The number of entries that can be made in the send buffer depends on the type of CPU you are using.

If the send buffer is full, then:

- The diagnostics event is nevertheless entered in the diagnostics buffer.
- The RET_VAL parameter indicates that the send buffer is full. (RET_VAL = W#16#8092).

#### Station not logged on

If a user diagnostics alarm is to be sent (SEND = TRUE) and no station is logged on,

- the user diagnostics event will still be entered in the diagnostics buffer.
- the RET_VAL parameter indicates that no station is logged on (W#16#0091 or W#16#8091. The value W#16#8091 appears only with older versions of the CPU.)

#### Structure of an entry

The internal structure of an entry in the diagnostics buffer is as follows:

| Byte | Contents |
| --- | --- |
| 1 and 2 | Event ID |
| 3 | Priority class |
| 4 | OB number |
| 5 and 6 | Reserved |
| 7 and 8 | Additional information 1 |
| 9, 10, 11 and 12 | Additional information 2 |
| 13 to 20 | Time stamp |

#### Event ID

An event ID is assigned to every event.

#### Additional information

This is additional information about the event. The additional information can differ for each event. When you create a user diagnostics event, you can decide on the content of these entries yourself.

When you send a user diagnostics alarm, you can integrate the additional information as associated values in the (event ID-specific) alarm text.

#### Time stamp

The time stamp is of the type Date_and_Time.

#### Parameters

The following table shows the parameters of the "WR_USMSG" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SEND | Input | BOOL | I, Q, M, D, L | Enable the sending of the user  diagnostics alarm to all logged-on  stations |
| EVENTN | Input | WORD | I, Q, M, D, L or constant | Event ID. You assign the event ID. The assignment is not executed by the alarm server. |
| INFO1 | Input | ANY | I, Q, M, D, L | Additional information: 1 word long |
| INFO2 | Input | ANY | I, Q, M, D, L | Additional information: 2 words long |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter SEND

If SEND = TRUE , the user diagnostics alarm will be sent to all logged-on stations. The alarm is only sent if the station is logged on and if the send buffer is not full. The sending of the element is asynchronous to the user program.

#### Parameter EVENTN

The EVENTN parameter contains the event ID of the user event. You can enter event IDs of the form W#16#8xyz , W#16#9xyz, W#16#Axyz, W#16#Bxyz.

IDs in the form W#16#8xyz and W#16#9xyz belong to predefined events, IDs in the form W#16#Axyz and W#16#Bxyz belong to freely defined events.

An incoming event is indicated by x = 1, an outgoing event by x = 0. With events in class A and B: yz is the number assigned in hexadecimal presentation in the alarm configuration for the corresponding alarm.

#### Parameter INFO1

The INFO1 parameter contains information that is one word long. The following data types are permitted for INFO1 :

- WORD
- INT
- ARRAY [0...1] OF CHAR

You can integrate the INFO1 parameter as an associated value in the alarm text and use it to add up-to-date information to the alarm.

#### Parameter INFO2

The INFO2 parameter contains information that is two words long. The following data types are permitted for INFO2 :

- DWORD
- DINT
- REAL
- TIME
- ARRAY [0...3] OF CHAR

You can integrate the INFO2 parameter as an associated value in the alarm text and use it to add up-to-date information to the alarm.

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 0091 | No station logged on (diagnostics event entered in the diagnostics buffer). |
| 8083 | INFO1 data type is not permitted |
| 8084 | INFO2 data type is not permitted |
| 8085 | EVENTN data type is not permitted |
| 8086 | Length of INFO1 is not permitted |
| 8087 | Length of INFO2 is not permitted |
| 8091 | (This error code appears only with older versions of the CPU.)  No station logged on (diagnostics event entered in the diagnostics buffer). |
| 8092 | Sending not possible at present, send buffer full (diagnostics event entered in  the diagnostics buffer). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### AR_SEND: Send archive data (S7-400)

#### Description

The instruction sends archive data to operator control and operating systems logged on for this purpose. These systems inform the CPU of the relevant archive number in the logon message frame. Depending on the memory available on the CPU and the operand area used, the archive data can be up to 65 534 bytes long. The defaults of the operator interface system you are using must be taken into consideration in the structure of the archive data.

The sending process is activated after the block is called and a rising edge is detected at the control input REQ. The start address of the archive data that is to be sent is specified by SD_1, the length of the data field by LEN. Data transfer is asynchronous to the execution of the user program. Successful completion of the send operation is indicated by the value of the DONE status parameter being set to "1". If there is a rising edge at control input R, the current sending process is canceled.

#### Parameters

The following table shows the parameters of the "AR_SEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request |
| R | Input | BOOL | I, Q, M, D, L | Control parameter reset: Current job  aborted |
| ID | Input | WORD | I, Q, M, D or constant | Data channel for alarms: W#16#EEEE ID is only evaluated at the first call. |
| AR_ID | Input | C_AR_SEND | I, Q, M, D, L or constant | Archive number (not permitted: 0); AR_ID is only evaluated at the first call. Subsequently, the archive number used for the first call applies to every call of AR_SEND with the corresponding instance DB.  The archive number is assigned automatically. This ensures the consistency of the archive numbers. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE: Sending  complete |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR: ERROR=TRUE indicates that an error has occurred during processing. For details refer to parameter STATUS. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Displays error information |
| SD_1 | InOut | ANY | I, Q, M, D, T, C | Pointer to archive data. The length specification is not evaluated.   Only the BOOL data types are permitted (not permitted: Bit array, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME.  The archive data must have a destination-system specific structure.   **Note:** When the ANY pointer accesses a DB, the DB must always be specified (for example: P# DB10.DBX5.0 byte 10). |
| LEN | InOut | WORD | I, Q, M, D, L | Length of the data field to be sent in bytes |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

The following table contains all specific error information that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS  (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning: New job not active because the previous job is still busy. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems |
| 1 | 2 | Negative acknowledgement, function cannot be executed |
| 1 | 3 | There is no logon for the specified AR_ID. |
| 1 | 4 | - Error in the archive data pointer SD_1 involving data length or  data type. - At the first call, the specified AR_ID is outside the permitted range. |
| 1 | 5 | Requested reset was executed. |
| 1 | 7 | RESET job irrelevant because the current function was  completed or not activated (block in incorrect status). |
| 1 | 10 | Access to local user memory not possible  (e.g. access to deleted DB) |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to AR_SEND - A global DB was specified instead of an instance DB. |
| 1 | 18 | AR_ID has already been used by an AR_SEND. |
| 1 | 20 | Not enough work memory. |

#### Data consistency

To ensure data consistency, you may only write to the part of the currently used sending area SD_1 after the current send operation is complete. This is the case when the DONE status parameter assumes the value "1".

### Others (S7-300, S7-400)

This section contains information on the following topics:

- [EN_MSG: Enable PLC alarms (S7-400)](#en_msg-enable-plc-alarms-s7-400)
- [DIS_MSG: Disable PLC alarms (S7-400)](#dis_msg-disable-plc-alarms-s7-400)
- [READ_SI: Read out dynamically assigned system resources (S7-300, S7-400)](#read_si-read-out-dynamically-assigned-system-resources-s7-300-s7-400)
- [DEL_SI: Delete dynamically assigned system resources (S7-300, S7-400)](#del_si-delete-dynamically-assigned-system-resources-s7-300-s7-400)

#### EN_MSG: Enable PLC alarms (S7-400)

##### Description

You use this instruction to enable PLC alarms you have disabled. You may have disabled the alarms either on a display device or using "[DIS_MSG](#dis_msg-disable-plc-alarms-s7-400)".

You specify the alarms to be enabled using the MODE and MESGN input parameters. Successful enabling of alarms with the instruction is only possible if the instruction is not already actively enabling alarms.

You start the enable process by assigning the value "1" to the input parameter REQ during the call.

##### Functional description

The enable process is executed asynchronously, in other words, it can extend over several calls from the instruction (see also [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)):

- When the instruction is first called (REQ =1), it checks the input parameters and attempts to assign the required system resources. In the good case, RET_VAL W#16#7001 is entered, BUSY is set, and enabling is triggered.  
  Otherwise the associated error information is entered in RET_VAL and the job is concluded. In this case, BUSY should not be evaluated.
- If there are further calls in the meantime, the value RET_VAL W#16#7002 is entered (job still being executed by the CPU) and BUSY is set. An intermediate call does not affect the current job.
- The last time the instruction is called, the value RET_VALW#16#0000 is entered if no error has occurred. In this case, BUSY is written with 0. If there is an error then the error information is entered in RET_VAL and BUSY should not be evaluated.

##### Parameter

The following table shows the parameters of the instruction "EN_MSG":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Trigger enable |
| MODE | Input | BYTE | I, Q, M, D, L or constant | See the table below for parameters for selecting the alarms to  be enabled; |
| MESGN | Input | DWORD | I, Q, M, D, L or constant | Alarm number  Only relevant when MODE = 6. This allows a single alarm to be enabled. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information (see below); |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The enabling process is not yet  complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter MODE

The following table shows the permitted values for the MODE input parameter.

| Value | Meaning |
| --- | --- |
| 0 | All PLC alarms of the CPU generated with instructions |
| 1 | All CPU PLC alarms generated with instructions, which means all alarms of "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)". |
| 6 | Single alarm of the "PLC alarms generated with instructions" class |

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Enabling was terminated without an error. |
| 7000 | REQ = 0 at first call: enabling was not activated. |
| 7001 | REQ = 1 at first call: enabling was triggered. |
| 7002 | Intermediate call: enabling is already active. |
| 8081 | Error accessing a parameter |
| 8082 | MODE has an illegal value. |
| 8083 | The alarm number is outside the permitted range of values. |
| 8084 | There is no logon for the alarm(s) specified with MODE and possibly MESGN . |
| 80C3 | Enabling of alarm(s) specified via MODE and possibly MESGN , cannot be initiated because another enabling process of "EN_MSG " is currently active. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### DIS_MSG: Disable PLC alarms (S7-400)

##### Description

You use this instruction to disable PLC alarms you have created with instructions. You select alarms to be disabled using the input parameters MODE and MESGN. Calling the "DIS_MSG" instruction and successfully disabling an alarm is only possible if disabling of an alarm is not already active with "DIS_MSG".

Alarms that are ready to be sent when "DIS_MSG" is called but that are still in an internal buffer can no longer be disabled and are sent.

A disabled alarm transmission is indicated at the ERROR and STATUS outputs of the "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" instructions.

You start the process by assigning the value "1" to the input parameter REQ when "DIS_MSG" is called.

##### Functional description

The reading process is executed asynchronously, in other words, it can extend over several calls (see also [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)):

- When it is first called (REQ =1), "DIS_MSG" checks the input parameters and attempts to occupy the required system resources. In the good case, RET_VALW#16#7001 is entered, BUSY is set and disabling is triggered.  
  Otherwise the associated error information is entered in RET_VAL and the job is concluded. In this case, BUSYmust not be evaluated.
- If there are further calls in the meantime, the value RET_VALW#16#7002 is entered (job still being executed by the CPU) and BUSY is set. An intermediate call does not affect the current job.
- The last time the instruction is called, the value RET_VALW#16#0000 is entered if no error has occurred. In this case, BUSY is written with "0". If there is an error then the error information is entered in RET_VAL and BUSY should not be evaluated.

##### Parameter

The following table shows the parameters of the instruction "DIS_MSG":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Trigger disable |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Parameter for selecting the alarms to  be disabled, see following table |
| MESGN | Input | DWORD | I, Q, M, D, L or constant | Alarm number  Alarm number only relevant when  MODE = 5, 6, 7. This allows a  single alarm to be disabled. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error code (see below) |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The disabling process is not yet  complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter MODE

The following table shows the permitted values for the MODE input parameter.

| Value | Meaning |
| --- | --- |
| 0 | All PLC alarms of the CPU generated with instructions |
| 1 | All CPU PLC alarms generated with instructions, which means all alarms of "[NOTIFY](#notify-report-a-signal-change-s7-400)", "[NOTIFY_8P](#notify_8p-report-up-to-eight-signal-changes-s7-400)", "[ALARM](#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8P](#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8](#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)". |
| 6 | Single alarm of the "PLC alarms generated with instructions" class |

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Disabling was terminated without an error. |
| 7000 | REQ = 0 at first call: disabling was not activated. |
| 7001 | REQ = 1 at first call: disabling was triggered. |
| 7002 | Intermediate call: disabling is already active. |
| 8081 | Error accessing a parameter |
| 8082 | MODE has an illegal value. |
| 8083 | The alarm number is outside the permitted range of values. |
| 8084 | There is no logon for the alarm(s) specified with MODE and possibly MESGN . |
| 80C3 | Disabling of alarm(s) specified via MODE and possibly MESGN , cannot be initiated because another disabling process of "DIS_MSG" is currently active. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### READ_SI: Read out dynamically assigned system resources (S7-300, S7-400)

##### Origin of dynamically allocated system resources when generating alarms with the "ALARM_DQ" and "ALARM_D" instructions

For alarm generation with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)", the operating system temporarily allocates memory space in the system memory.

For example, if you delete an FB with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" or "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" calls that was present in the CPU, it may be the case that corresponding system resources remain permanently allocated. If you reload the FB with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" or "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" calls, it may be that the "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" instructions are no longer processed properly.

##### Description

Use the "READ_SI" instruction to read out the currently used system resources that were allocated for alarm generation with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)". This is done via the values of EV_ID and CMP_ID used there. These values are passed on to the "READ_SI" instruction in the SI_ID parameter.

The "READ_SI" instruction has four possible operating modes, which are explained in the following table. You set the requested operating mode via the MODE parameter.

| MODE | Which of the system resources allocated to "ALARM_DQ" / "ALARM_D" are read out? |
| --- | --- |
| 1 | All (calling of "READ_SI" using SI_ID:=0) |
| 2 | The system resources that were allocated to the "ALARM_DQ" / "ALARM_D" call with EV_ID:=ev_id calling of READ_SI using SI_ID:=ev_id) |
| 3 | All system resources that were allocated to the "ALARM_DQ" / "ALARM_D" call with CMP_ID:=cmp_id (calling of using READ_SI using SI_ID:=cmp_id) |
| 0 | Additional system resources that could not be read with the previous call in MODE=1 or MODE=3 because you have selected a destination field SYS_INST that is too small |

##### Functional description

If you have selected a sufficiently large SYS_INST destination area when you called READ_SI with MODE=1 or MODE=3, it will contain the content of all currently occupied system resources selected via the MODE parameter after the call.

If the amount of system resources currently occupied is very large, the runtime will be correspondingly high. That is, a high load on CPU performance may cause the the maximum configurable cycle monitoring time to be exceeded.

You can work around this runtime problem as follows: Select a relatively small SYS_INST destination area. If the instruction cannot enter all of the system resources that will be read out in SYS_INST, this fact will be communicated to you via RET_VAL=W#16#0001. Then call READ_SI with MODE=0 and the same SI_ID as for the previous call until RET_VAL takes on the value W#16#0000.

> **Note**
>
> Because the operating system does not coordinate the READ_SI calls that belong to a read job, you should execute all READ_SI calls in the same priority class.

##### Parameter

The following table shows the parameters of the instruction "READ_SI":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | INT | I, Q, M, D, L or constant | Job identifier  Permitted values:  - 1: Read all system resources - 2: Read the system resources to which "ALARM_DQ"-/ "ALARM_D" = ev_id was allocated when EV_ID = ev_id was called. - 3: Read the system resources to which "ALARM_DQ"-/ "ALARM_D" = ev_id was allocated when CMP_ID = cmp_id was called. - 0: subsequent call |
| SI_ID | Input | DWORD | I, Q, M, D, L or constant | ID for the system resource(s) to be read  Permitted values:  - 0, if MODE=1 - Alarm number ev_id, if MODE=2 - ID cmp_id for identification of the subsystem, if MODE=3 |
| RET_VAL | Return | INT | I, Q, M, D, L | Return value (error information or job status) |
| N_SI | Output | INT | I, Q, M, D, L | Number of system resources output in SYS_INT |
| SYS_INST | Output | ANY | D | Destination area for the read system resources. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 0001 | Not all system resources could be read because the SYS_INST destination range you have selected is too short. |
| 8081 | (only with MODE=2 or 3 ). You have assigned the value 0 to SI_ID . |
| 8082 | (only with MODE=1). You have assigned one of 0 different values to SI_ID . |
| 8083 | (only with MODE=0). You have assigned SI_ID a value other than the value assigned for the preceding call with MODE=1 or 3. |
| 8084 | You have assigned an illegal value to MODE . |
| 8085 | READ_SI is already being processed in another OB. |
| 8086 | The destination area SYS_INST is too small for a system resource. |
| 8087 Or 8092 | The destination area SYS_INST does not exist in a DB or error in the ANY pointer. |
| 8xyy | General error information  See also: [ALARM_D: Create permanently acknowledged PLC alarms](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400) |

##### Destination area parameter SYS_INST - Structure

The destination area for the read assigned system resources must be within a DB. You should appropriately define the destination area as a field of structures; a structure is comprised of the following:

| Structure element | Data type | Description |
| --- | --- | --- |
| SFC_NO | WORD | Number of the instruction allocated by the system resource |
| LEN | BYTE | Length of the structure in bytes, including SFC_NO and LEN: B#16#0C |
| SIG_STAT | BOOL | Signal state |
| ACK_STAT | BOOL | Acknowledgement status of the incoming event (positive edge) |
| EV_ID | DWORD | Alarm number |
| CMP_ID | DWORD | Subsystem ID |

#### DEL_SI: Delete dynamically assigned system resources (S7-300, S7-400)

##### Origin of dynamically allocated system resources when generating alarms with the "ALARM_DQ" and "ALARM_D" instructions

For alarm generation with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)", the operating system temporarily allocates memory space in the system memory.

For example, if you delete an FB with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" or "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" calls that was present in the CPU, it may be the case that corresponding system resources remain permanently allocated. If you reload the FB with "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" / "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" calls, it may be that the "[ALARM_DQ](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400)" and "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" instructions will no longer be processed properly.

##### Description

You use the "DEL_SI" instruction to delete system resources that are currently in use.

"DEL_SI" has three possible operating modes, which are explained in the following table. You set the requested operating mode via the MODE parameter.

| MODE | Which of the system resources allocated to "ALARM_DQ"/ "ALARM_D" will be deleted? |
| --- | --- |
| 1 | All (calling of "DEL_SI" using SI_ID:=0) |
| 2 | The system resources that were allocated to the EV_ID:=ev_id when ["ALARM_DQ"](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400) / [ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400) was called (DEL_SI called using SI_ID:=ev_id) |
| 3 | All system resources to which CMP_ID:=cmp_id was allocated when ["ALARM_DQ"](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400) / [ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400) was called (DEL_SI called with SI_ID:=cmp_id) |

##### Parameter

The following table shows the parameters of the instruction "DEL_SI":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MODE | Input | INT | I, Q, M, D, L or constant | Job identifier  Permitted values:  - 1: delete all system resources - 2: Delete the system resources that were allocated to EV_ID = ev_id when ["ALARM_DQ"](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400) / "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" was called - 3: Delete the system resources that were allocated to CMP_ID = cmp_id when ["ALARM_DQ"](#alarm_dq-create-acknowledgeable-plc-alarms-s7-300-s7-400) / "[ALARM_D](#alarm_d-create-permanently-acknowledged-plc-alarms-s7-300-s7-400)" was called |
| SI_ID | Input | DWORD | I, Q, M, D, L or constant | ID of the system resource(s) to be deleted  Permitted values:  - 0, if MODE=1 - Alarm number ev_id, if MODE=2 - ID cmp_id for identification of the subsystem, if MODE=3 |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8081 | (only with MODE=2 or 3 ). You have assigned the value "0" to SI_ID . |
| 8082 | (only with MODE=1). You have assigned one of "0" different values to SI_ID. |
| 8084 | You have assigned an illegal value to MODE . |
| 8085 | "DEL_SI" is currently being processed. |
| 8086 | Not all selected system resources could be deleted because at least one of them was being processed when "DEL_SI" was called. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## Diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [RD_SINFO: Read current OB start information (S7-300, S7-400)](#rd_sinfo-read-current-ob-start-information-s7-300-s7-400)
- [RDSYSST: Read system status list (S7-300, S7-400)](#rdsysst-read-system-status-list-s7-300-s7-400)
- [System status list (S7-300, S7-400)](#system-status-list-s7-300-s7-400)
- [OB_RT: Determine OB program runtime (S7-400)](#ob_rt-determine-ob-program-runtime-s7-400)
- [C_DIAG: Determine current connection status (S7-400)](#c_diag-determine-current-connection-status-s7-400)

### RD_SINFO: Read current OB start information (S7-300, S7-400)

#### Description

You read the start information with the instruction:

- of the OB last called that has not yet been completely executed, and
- of the startup OB started last.

There is no time stamp in either case. If the call is in OB 100 or OB 101 or OB 102, two identical start information messages will be returned.

#### Parameters

The following table shows the parameters of the instruction "RD_SINFO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| TOP_SI | Output | STRUCT | D, L | Start information of the current OB |
| START_UP_SI | Output | STRUCT | D, L | Start information of the startup OB  last started |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

The instruction provides only general and not specific error information. The general error information and its evaluation are written to the "RET_VAL" output parameter.

See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val).

#### Parameter TOP_SI and START_UP_SI

The output parameters TOP_SI and START_UP_SI are two identically set up structures. Their structure is provided in the following table.

| Structure element | Data type | Description |
| --- | --- | --- |
| EV_CLASS | BYTE | - Bits 0 to 3: Event ID - Bits 4 to 7: Event class |
| EV_NUM | BYTE | Event number |
| PRIORITY | BYTE | Number of the priority class (meaning of B#16#FE: OB not available or disabled or cannot be started in current operating mode) |
| NUM | BYTE | OB number |
| TYP2_3 | BYTE | Data ID 2_3:  Identifies the information entered in ZI2_3 |
| TYP1 | BYTE | Data ID 1:  Identifies the information entered in ZI1 |
| ZI1 | WORD | Additional information 1 |
| ZI2_3 | DWORD | Additional information 2_3 |

> **Note**
>
> The structure elements listed in the above table are identical in content with the temporary tags of an OB.
>
> Please note, however, that temporary tags of the individual OBs can have different names and different data types. Also note that the call interface of each OB includes additional information regarding the date and the time of the OB request.

Bits 4 to 7 of the EV_CLASS structure element contain the event class. The following values are possible here:

- 1: Start events from standard OBs
- 2: Start events from synchronous error OBs
- 3: Start events from asynchronous error OBs

The PRIORITY structure element supplies the priority class belonging to the current OB.

Apart from these two elements, NUM is also relevant. NUM contains the number of the current OB or the startup OB that was started last.

#### Example

OB 80 is the OB that was called last and that has not yet been completely processed and OB 100 is the start-up OB that was started last.

The following table shows the assignment between the structure elements of the TOP_SI parameter of the "RD_SINFO" instruction and the associated local tags of OB 80.

| TOP_SI Structure element | Data type | OB 80 - Associated local tag | Data type |
| --- | --- | --- | --- |
| EV_CLASS | BYTE | OB80_EV_CLASS | BYTE |
| EV_NUM | BYTE | OB80_FLT_ID | BYTE |
| PRIORITY | BYTE | OB80_PRIORITY | BYTE |
| NUM | BYTE | OB80_OB_NUMBR | BYTE |
| TYP2_3 | BYTE | OB80_RESERVED_1 | BYTE |
| TYP1 | BYTE | OB80_RESERVED_2 | BYTE |
| ZI1 | WORD | OB80_ERROR_INFO | WORD |
| ZI2_3 | DWORD | OB80_ERR_EV_CLASS | BYTE |
| OB80_ERR_EV_NUM | BYTE |  |  |
| OB80_OB_PRIORITY | BYTE |  |  |
| OB80_OB_NUM | BYTE |  |  |

The following table shows the assignment between the structure elements of the START_UP_SI parameter of the "RD_SINFO" instruction and the associated local tags of OB 100.

| START_UP_SI Structure element | Data type | OB 100 - Local tag | Data type |
| --- | --- | --- | --- |
| EV_CLASS | BYTE | OB100_EV_CLASS | BYTE |
| EV_NUM | BYTE | OB100_STRTUP | BYTE |
| PRIORITY | BYTE | OB100_PRIORITY | BYTE |
| NUM | BYTE | OB100_OB_NUMBR | BYTE |
| TYP2_3 | BYTE | OB100_RESERVED_1 | BYTE |
| TYP1 | BYTE | OB100_RESERVED_2 | BYTE |
| ZI1 | WORD | OB100_STOP | WORD |
| ZI2_3 | DWORD | OB100_STRT_INFO | DWORD |

### RDSYSST: Read system status list (S7-300, S7-400)

#### Description

With the instruction you read a partial list of the system status lists (SZL) or a SZL partial list extract.

You start the read process by assigning the value "1" to the input parameter REQ when "RDSYSST" is called. If the read process could be executed immediately, the instruction returns the value "0" at the output parameter BUSY. If BUSY has the value "1", reading is not yet complete.

> **Note**
>
> If you call the "RDSYSST" instruction in the diagnostic interrupt OB with the SZL‑IDW#16#00B1 or W#16#00B2 or W#16#00B3 and access the module that initiated the diagnostic interrupt, the system status will be read immediately.
>
> With "RDSYSST", only complete data records will be transferred.

#### System resources

If you start several asynchronous reading processes (the jobs with parameter SZL_IDW#16#00B4 and W#16#4C91 and W#16#4092 and W#16#4292 and W#16#4692 and possibly W#16#00B1 and W#16#00B3) one after the other at brief intervals, the operating system ensures that all the read jobs will be executed and that they do not interfere with each other. If the limits of the system resources are reached, this is indicated in RET_VAL. You can remedy this temporary error situation by repeating the job.

The maximum number of "simultaneously" active jobs of the instruction depends on the CPU.

> **Note**
>
> With S7-400 CPUs, the "RDSYSST" can be used to transfer a maximum of 432 bytes to the destination area.

#### Parameters

The following table shows the parameters of the "RDSYSST" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Trigger processing |
| SZL_ID | Input | WORD | I, Q, M, D, L or constant | SZL‑ID of the partial list or  partial list extract |
| INDEX | Input | WORD | I, Q, M, D, L or constant | Type or number of an object in a  partial list. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs during execution of the instruction, the RET_VAL parameter  contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | TRUE: Reading not yet complete. |
| SZL_HEADER | Output | STRUCT | D, L | See below. |
| DR | Output | ANY | I, Q, M, L, D | Destination area of the read  SZL partial list or the read SZL partial list extract:  - If you have only read out the header information of an SZL partial list,  you should not evaluate DR but  only SZL_HEADER. - Otherwise, the product of LENTHDR and N_DR  indicates  how many bytes were entered in DR. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters SZL_HEADER

The SZL_HEADER parameter is a structure defined as follows:

|  |  |  |
| --- | --- | --- |
| `SZL_HEADER:` |  | `STRUCT` |
|  | `LENTHDR:` | `WORD` |
|  | `N_DR:` | `WORD` |
| `END_STRUCT` |  |  |

LENTHDR is the length of a data record of the SZL partial list or the SZL partial list extract.

- If you have only read out the header information of an SZL partial list, N_DR contains the number of data records belonging to it.
- Otherwise, N_DR contains the number of data records transferred to the destination area.

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 0081 | Result field too short. (Nevertheless as many data records as possible are supplied. The  SZL-Header indicates this number.) |
| 7000 | First call with REQ = 0: No data transfer active; BUSY has the value "0". |
| 7001 | First call with REQ=1: Data transfer triggered; BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant): Data transfer already active; BUSY has the value "1". |
| 8081 | Result field too short (not enough space for one data record). |
| 8082 | SZL_ID is incorrect or is unknown in the CPU or instruction. |
| 8083 | INDEX incorrect or not permitted |
| 8085 | Due to a problem in the system, information is not currently available (for example, due  to a lack of resources). |
| 8086 | The data record cannot be read due to a system error (bus, modules, operating system). |
| 8087 | Data record cannot be read because the module does not exist or does not acknowledge. |
| 8088 | Data record cannot be read because the actual module identifier is different from the  expected module identifier. |
| 8089 | Data record cannot be read because the module is not capable of diagnostics or the data record is not supported. |
| 80A2 | DP protocol error (layer 2 error) (temporary error) |
| 80A3 | DP protocol error with user interface/user (temporary error) |
| 80A4 | Communication problem on communication bus (error occurs between the CPU and the  external DP interface module) |
| 80C5 | Distributed I/O not available (temporary error). |
| 80C6 | Data record transfer stopped due to priority class abort (restart or background) |
| 80D2 | Data record cannot be read because the module is not capable of diagnostics. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

#### Parameters SZL_ID

> **Note**
>
> **Partial lists of S7-CPUs that can be read out**
>
> - The partial lists for S7-300 that can be read out via "RDSYSST" are provided in the corresponding operation list.
> - The partial lists for S7-400 that can be read out via "RDSYSST" are provided in the following table.

| SZL_ID (W#16#...) | Partial list | INDEX (W#16#...) |
| --- | --- | --- |
| **Module ID** |  |  |
| [0111](#szl-id-w16xy11---module-identification-s7-300-s7-400) | An identification data record |  |
| ID of the module | 0001 |  |
| Identification of basic hardware | 0006 |  |
| Identification of the basic firmware | 0007 |  |
| **CPU characteristics** |  |  |
| [0012](#szl-id-w16xy12---cpu-characteristics-s7-300-s7-400) | All characteristics | irrelevant |
| [0112](#szl-id-w16xy12---cpu-characteristics-s7-300-s7-400) | Characteristics of one group |  |
| MC7 processing unit | 0000 |  |
| Time system | 0100 |  |
| System behavior | 0200 |  |
| MC7 language description | 0300 |  |
| Availability of the "[C_DIAG](#c_diag-determine-current-connection-status-s7-400)" instruction | 0400 |  |
| [0F12](#szl-id-w16xy12---cpu-characteristics-s7-300-s7-400) | Only SZL partial header information | irrelevant |
| **User memory areas** |  |  |
| [0113](#szl-id-w16xy13---user-memory-areas-s7-300-s7-400) | A data record for the memory area specified |  |
| Work memory | 0001 |  |
| **System areas** |  |  |
| [0014](#szl-id-w16xy14---system-areas-s7-300-s7-400) | Data records of all system areas | irrelevant |
| [0F14](#szl-id-w16xy14---system-areas-s7-300-s7-400) | Only SZL partial header information | irrelevant |
| **Block types** |  |  |
| [0015](#szl-id-w16xy15---block-types-s7-300-s7-400) | Data records of all block types | irrelevant |
| **Identification of one component** |  |  |
| [001C](#szl-id-w16xy1c---component-identification-s7-300-s7-400) | Identification of all components | irrelevant |
| [011C](#szl-id-w16xy1c---component-identification-s7-300-s7-400) | Identification of one component |  |
| Name of the automation system | 0001 |  |
| Name of the module | 0002 |  |
| System ID of the module | 0003 |  |
| Copyright entry | 0004 |  |
| Serial number of the module | 0005 |  |
| Module type name | 0007 |  |
| Serial number of the memory card | 0008 |  |
| Manufacturer and profile of a CPU module | 0009 |  |
| Location designation of a module | 000B |  |
| [0F1C](#szl-id-w16xy1c---component-identification-s7-300-s7-400) | Only SZL partial header information | irrelevant |
| **Interrupt status** |  |  |
| [0222](#szl-id-w16xy22---interrupt-status-s7-300-s7-400) | Data record for indicated interrupt | OB number |
| **Assignment of process images to CPUs** |  |  |
| [0025](#szl-id-w16xy25---assignment-of-process-image-partitions-to-obs-s7-300-s7-400) | Assignment of all process images to OBs | irrelevant |
| [0125](#szl-id-w16xy25---assignment-of-process-image-partitions-to-obs-s7-300-s7-400) | Assignment of a process image partition to the corresponding OB | Process image partition no. |
| [0225](#szl-id-w16xy25---assignment-of-process-image-partitions-to-obs-s7-300-s7-400) | Assignment of an OB to the corresponding process image partitions | OB no. |
| [0F25](#szl-id-w16xy25---assignment-of-process-image-partitions-to-obs-s7-300-s7-400) | Only SZL partial header information | irrelevant |
| **Communication status data** |  |  |
| [0132](#szl-id-w16xy32---communication-status-data-s7-300-s7-400) | Status data for one communication unit |  |
|  | Diagnostics | 0005 |
|  | Time system | 0008 |
| [0232](#szl-id-w16xy32---communication-status-data-s7-300-s7-400) | Status data for one communication unit |  |
|  | CPU protection level and operator control settings | 0004 |
| Status of the module LEDs (cannot be read out for all  CPUs). |  |  |
| [0174](#szl-id-w16xy74---status-of-the-module-leds-s7-300-s7-400) | Status of an LED | LED ID |
| **DP master system information** |  |  |
| [0090](#szl-id-w16xy90---dp-master-system-information-s7-300-s7-400) | Information regarding all DP master systems known to the CPU | 0000 |
| [0190](#szl-id-w16xy90---dp-master-system-information-s7-300-s7-400) | Information regarding one DP master system | DP master system ID |
| [0F90](#szl-id-w16xy90---dp-master-system-information-s7-300-s7-400) | Only SZL partial header information | 0000 |
| **Module status information (a maximum of 27 data records is supplied)** |  |  |
| [0091](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Status information of all modules/sub-modules inserted | irrelevant |
| [0191](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Status information of all non-deactivated modules/racks with  incorrect module ID | irrelevant |
| [0291](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of all faulty and non-deactivated modules | irrelevant |
| [0391](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of all unavailable modules | irrelevant |
| [0591](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of all sub-modules of the host  module | irrelevant |
| [0991](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of one DP master system | DP master system ID |
| [0C91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of a module in a central  configuration or connected to an integrated DP  interface module or a PROFINET interface module (integrated or external) | Logical base address |
| [4C91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of a module connected to an  external DP interface module | Logical base address |
| [0D91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of all modules in the rack/ station specified (DP or PROFINET) | Rack or DP master system ID and station number or station number and the last two digits of the PNIO subsystem ID |
| [0E91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Module status information of all assigned modules | irrelevant |
| [0F91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) | Only SZL partial header information | irrelevant |
| **Rack/station status information** |  |  |
| [0092](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Expected status of the rack in the central configuration/ stations of a DP master system. | 0 / DP master system  ID |
| [4092](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Expected status of the stations of a DP master system  connected via an external DP interface module. | DP master system ID |
| [0192](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Activation status of the stations of a DP master system that is connected via an integrated DP interface module | DP master system ID |
| [0292](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Current status of the rack in the central configuration /  stations of a DP master system | 0 / DP master system  ID |
| [4292](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Current status of the stations of a DP master system that is connected via an external DP interface module | DP master system ID |
| [0392](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Status of the backup batteries in a rack/module rack of a CPU after at least one battery has failed. | 0 |
| [0492](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Status of the overall battery backup of all racks/module racks of a CPU. | 0 |
| [0592](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Status of the 24 V power supply to all racks/module racks of a CPU | 0 |
| [0692](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Diagnostics status of the expansion racks in the central configuration/ of the stations of a DP master system connected via an  integrated DP interface module | 0 / DP master system  ID |
| [4692](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) | Diagnostics status of the stations of a DP master system connected  via an external DP interface module | DP master system ID |
| **Rack/station status information** |  |  |
| [0094](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) | Expected status of the rack in the central configuration / stations of an IO controller system. | 0 / PNIO subsystem ID |
| [0194](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) | Activation status of a station of an IO controller system that is configured and deactivated | PNIO subsystem ID |
| [0294](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) | Actual status of the rack in the central configuration / stations of an IO controller system | 0 / PNIO subsystem ID |
| [0694](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) | Diagnostic status of the expansion units in the central configuration / stations of an IO controller system. | 0 / PNIO subsystem ID |
| [0794](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) | Maintenance status of the central rack / stations of an IO controller system. | 0 / PNIO subsystem ID |
| [0F94](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) | Only header information | - |
| **Extended DP master system information** |  |  |
| [0195](#szl-id-w16xy95---extended-dp-master-system-profinet-io-system-information-s7-300-s7-400) | Extended information about a DP master system | DP master system ID |
| [0F95](#szl-id-w16xy95---extended-dp-master-system-profinet-io-system-information-s7-300-s7-400) | Only SZL partial header information | 0000 |
| **Module status information PROFINET IO and PROFIBUS DP** |  |  |
| [0696](#szl-id-w16xy96---profinet-io-and-profibus-dp-module-status-information-s7-300-s7-400) | Module status information of all sub-modules of a specified module (only with PROFINET IO on an integrated interface module). | Address with I/O ID |
| [0C96](#szl-id-w16xy96---profinet-io-and-profibus-dp-module-status-information-s7-300-s7-400) | Module status information of a module/sub-module in a central configuration or on an integrated PROFIBUS DP or PROFINET interface module (integrated or external). | Start address with I/O ID |
| **Diagnostics buffer** (a maximum of 21 data records is  supplied) |  |  |
| [00A0](#szl-id-w16xya0---diagnostic-buffer-s7-300-s7-400) | All entries that can be supplied in the currently active  operating mode | irrelevant |
| [01A0](#szl-id-w16xya0---diagnostic-buffer-s7-300-s7-400) | The most recent entries, the number is specified in the  index | Number |
| [0FA0](#szl-id-w16xya0---diagnostic-buffer-s7-300-s7-400) | Only SZL partial header information | irrelevant |
| **Diagnostic data on modules** |  |  |
| [00B1](#szl-id-w1600b1---module-diagnostic-information-s7-300-s7-400) | The first four diagnostics bytes of one module (data record 0) | Logical base address |
| [00B2](#szl-id-w1600b2---diagnostic-data-record-1-with-physical-address-s7-300-s7-400) | All diagnostic data of one module (220 bytes, data record 1) (no DP module) | Rack, slot |
| [00B3](#szl-id-w1600b3---module-diagnostic-data-with-logical-base-address-s7-300-s7-400) | All diagnostic data of one module (220 bytes, data record 1) | Logical base address |
| [00B4](#szl-id-w1600b4---diagnostic-data-of-a-dp-slave-s7-300-s7-400) | Diagnostic data of a DP slave | Configured diagnostics  address |

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

### System status list (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of the system status list (SZL) (S7-300, S7-400)](#overview-of-the-system-status-list-szl-s7-300-s7-400)
- [Structure of a partial SZL list (S7-300, S7-400)](#structure-of-a-partial-szl-list-s7-300-s7-400)
- [SZL-ID (S7-300, S7-400)](#szl-id-s7-300-s7-400)
- [Possible SZL partial lists (S7-300, S7-400)](#possible-szl-partial-lists-s7-300-s7-400)
- [SZL-ID W#16#xy11 - module identification (S7-300, S7-400)](#szl-id-w16xy11---module-identification-s7-300-s7-400)
- [SZL-ID W#16#xy12 - CPU characteristics (S7-300, S7-400)](#szl-id-w16xy12---cpu-characteristics-s7-300-s7-400)
- [SZL-ID W#16#xy13 - user memory areas (S7-300, S7-400)](#szl-id-w16xy13---user-memory-areas-s7-300-s7-400)
- [SZL-ID W#16#xy14 - system areas (S7-300, S7-400)](#szl-id-w16xy14---system-areas-s7-300-s7-400)
- [SZL-ID W#16#xy15 - block types (S7-300, S7-400)](#szl-id-w16xy15---block-types-s7-300-s7-400)
- [SZL-ID W#16#xy1C - component identification (S7-300, S7-400)](#szl-id-w16xy1c---component-identification-s7-300-s7-400)
- [SZL-ID W#16#xy22 - interrupt status (S7-300, S7-400)](#szl-id-w16xy22---interrupt-status-s7-300-s7-400)
- [SZL ID W#16#xy25 - assignment of process image partitions to OBs (S7-300, S7-400)](#szl-id-w16xy25---assignment-of-process-image-partitions-to-obs-s7-300-s7-400)
- [SSL ID W#16#xy32 - Communication status data (S7-300, S7-400)](#ssl-id-w16xy32---communication-status-data-s7-300-s7-400)
- [SZL-ID W#16#xy74 - status of the module LEDs (S7-300, S7-400)](#szl-id-w16xy74---status-of-the-module-leds-s7-300-s7-400)
- [SZL-ID W#16#xy90 - DP master system information (S7-300, S7-400)](#szl-id-w16xy90---dp-master-system-information-s7-300-s7-400)
- [SZL-ID W#16#xy91 - module status information (S7-300, S7-400)](#szl-id-w16xy91---module-status-information-s7-300-s7-400)
- [SZL-ID W#16#xy92 - rack / station status information (S7-300, S7-400)](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400)
- [SZL-ID W#16#0x94 - status information for rack/station (S7-300, S7-400)](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400)
- [SZL-ID W#16#xy95 - extended DP master system / PROFINET IO system information (S7-300, S7-400)](#szl-id-w16xy95---extended-dp-master-system-profinet-io-system-information-s7-300-s7-400)
- [SZL-ID W#16#xy96 - PROFINET IO and PROFIBUS DP module status information (S7-300, S7-400)](#szl-id-w16xy96---profinet-io-and-profibus-dp-module-status-information-s7-300-s7-400)
- [SZL-ID W#16#xy9C - Tool changeover information (PROFINET IO) (S7-300, S7-400)](#szl-id-w16xy9c---tool-changeover-information-profinet-io-s7-300-s7-400)
- [SZL-ID W#16#xyA0 - diagnostic buffer (S7-300, S7-400)](#szl-id-w16xya0---diagnostic-buffer-s7-300-s7-400)
- [SZL-ID W#16#00B1 - module diagnostic information (S7-300, S7-400)](#szl-id-w1600b1---module-diagnostic-information-s7-300-s7-400)
- [SZL-ID W#16#00B2 - diagnostic data record 1 with physical address (S7-300, S7-400)](#szl-id-w1600b2---diagnostic-data-record-1-with-physical-address-s7-300-s7-400)
- [SZL-ID W#16#00B3 - module diagnostic data with logical base address (S7-300, S7-400)](#szl-id-w1600b3---module-diagnostic-data-with-logical-base-address-s7-300-s7-400)
- [SZL-ID W#16#00B4 - diagnostic data of a DP slave (S7-300, S7-400)](#szl-id-w1600b4---diagnostic-data-of-a-dp-slave-s7-300-s7-400)

#### Overview of the system status list (SZL) (S7-300, S7-400)

##### Definition: System status list

The system status list (SZL) describes the current status of an automation system. The contents of the SZL (system status list) can only be read using information functions, contents cannot be modified. The partial lists are virtual lists, in other words, they are only created by the operating system of the CPUs when specifically requested.

You can only read out one partial list using "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)". This chapter describes the partial lists of the system status list that can be read with "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" in the user program, and that have information relating to

- CPUs or to
- modules whose partial lists are not module-specific (for example, SZL IDs W#16#00B1, W#16#00B2, W#16#00B3).

Module-specific partial lists, for example, for CPs and FMs are included in the descriptions of the particular modules.

##### Contents

The system status lists contain information about the following:

- System data
- Module status data in the CPU
- Diagnostics data on modules
- Diagnostics buffer

##### System data

System data are fixed or parameter- assigned characteristic data of a CPU. They provide information about the following:

- The configuration of the CPU
- The status of the priority classes
- Communication

##### Module status data

Module status information describes the current status of the components monitored by the system diagnostics.

##### Diagnostics data on modules

The modules with diagnostics capabilities assigned to a CPU have diagnostics data that are stored directly on the module.

##### Diagnostics buffer

The diagnostics buffer contains diagnostics entries in the order in which they occur.

#### Structure of a partial SZL list (S7-300, S7-400)

##### Basics

You can read a partial list or a partial list extract using "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)". You specify what you want to read using the parameters SZL_ID (System status list ID) and INDEX.

##### Structure

A partial list consists of the following:

- A header and
- the data records.

##### Header

The header of a partial list consists of the following:

- SZL-ID
- INDEX
- Length of a data record of the partial list in bytes
- Number of data records contained in the partial list.

##### Index

With certain partial lists or partial list extracts an object type ID or an object number must be specified. The index is used for this purpose. If it is not required for the information, its contents are irrelevant.

##### Data records

A data record in a partial list has a specific length. This depends on the information in the partial list. How the data words in a data record are used also depends on the particular partial list.

#### SZL-ID (S7-300, S7-400)

##### SZL-ID (System status list ID)

Every partial list within the system status list has a number. You can output a complete partial list or an extract from it. The possible partial list extracts are predefined and are identified by a number. The SZL-ID consists of the number of the partial list, the number of the partial list extract and the module class.

##### Structure

The SZL-ID is one word long. The meaning of the bits in the SZL ID is as follows:

![Structure of SZL-ID](images/19546309643_DV_resource.Stream@PNG-en-US.png)

Structure of SZL-ID

##### Module class

Examples of module classes:

| Module class | Coding (binary) |
| --- | --- |
| CPU | 0000 |
| IM | 0100 |
| FM | 1000 |
| CP | 1100 |

##### Number of the partial list extract

The numbers of the partial list extracts and their meaning depend on the particular system status list to which they belong. With the number of the partial list extract, you specify which subset of a partial list you want to read.

##### Number of the partial List

Using the number of the partial list, you specify which partial list of the system status list you want to read out.

#### Possible SZL partial lists (S7-300, S7-400)

##### Subset

Any one module only has a subset of all the possible partial lists. Which partial lists are available depends on the particular module.

##### Possible SZL partial lists

The following table lists all possible partial lists with the number contained in the SZL-ID (system status list ID).

| Partial list | SZL-ID |
| --- | --- |
| Module ID | [W#16#xy11](#szl-id-w16xy11---module-identification-s7-300-s7-400) |
| CPU characteristics | [W#16#xy12](#szl-id-w16xy12---cpu-characteristics-s7-300-s7-400) |
| User memory areas | [W#16#xy13](#szl-id-w16xy13---user-memory-areas-s7-300-s7-400) |
| System areas | [W#16#xy14](#szl-id-w16xy14---system-areas-s7-300-s7-400) |
| Block types | [W#16#xy15](#szl-id-w16xy15---block-types-s7-300-s7-400) |
| Identification of one component | [W#16#xy1C](#szl-id-w16xy1c---component-identification-s7-300-s7-400) |
| Interrupt status | [W#16#xy22](#szl-id-w16xy22---interrupt-status-s7-300-s7-400) |
| Assignment of partial process images and OBs | [W#16#xy25](#szl-id-w16xy25---assignment-of-process-image-partitions-to-obs-s7-300-s7-400) |
| Communication: Status data | [W#16#xy32](#szl-id-w16xy32---communication-status-data-s7-300-s7-400) |
| Status of the module LEDs | [W#16#xy74](#szl-id-w16xy74---status-of-the-module-leds-s7-300-s7-400) |
| DP master system information | [W#16#xy90](#szl-id-w16xy90---dp-master-system-information-s7-300-s7-400) |
| Module status information | [W#16#xy91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) |
| Rack /station status information | [W#16#xy92](#szl-id-w16xy92---rack-station-status-information-s7-300-s7-400) |
| Rack /station status information | [W#16#xy94](#szl-id-w160x94---status-information-for-rackstation-s7-300-s7-400) |
| Extended DP master system information | [W#16#xy95](#szl-id-w16xy95---extended-dp-master-system-profinet-io-system-information-s7-300-s7-400) |
| Module status information PROFINET IO and PROFIBUS DP | [W#16#xy96](#szl-id-w16xy96---profinet-io-and-profibus-dp-module-status-information-s7-300-s7-400) |
| Diagnostics buffer | [W#16#xyA0](#szl-id-w16xya0---diagnostic-buffer-s7-300-s7-400) |
| Module diagnostic information (data record 0) | [W#16#00B1](#szl-id-w1600b1---module-diagnostic-information-s7-300-s7-400) |
| Module diagnostic information (data record 1), physical address | [W#16#00B2](#szl-id-w1600b2---diagnostic-data-record-1-with-physical-address-s7-300-s7-400) |
| Module diagnostic information (data record 1), logical address | [W#16#00B3](#szl-id-w1600b3---module-diagnostic-data-with-logical-base-address-s7-300-s7-400) |
| Diagnostic data of a DP slave | [W#16#00B4](#szl-id-w1600b4---diagnostic-data-of-a-dp-slave-s7-300-s7-400) |
|  |  |

#### SZL-ID W#16#xy11 - module identification (S7-300, S7-400)

##### Purpose

You obtain the module identification of this module via the partial list with the SZL-ID (system status list ID) W#16#xy11.

##### Header

The header of the SZL with the SZL-IDW#16#xy11 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0111: A single identification data record |
| INDEX | Number of a particular data record  W#16#0001: ID of the module  W#16#0006: Identification of the basic hardware  W#16#0007: Identification of the basic firmware |
| LENTHDR | W#16#001C: One data record is 14 words long (28 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the SZL with the SZL-IDW#16#xy11 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | Number of an identification data record |
| MRPC | 20 bytes | Machine-Readable Product Code  With INDEX W#16#0007: Reserved  With INDEXW#16#0001 and W#16#0006: Machine readable product code of the module; string consists of 19 characters and a blank (20H); such as for CPU 314: "6ES7 314-0AE01-0AB0" |
| ModuleType | 1 word | Reserved |
| OutMod1 | 1 word | With INDEXW#16#0001: Output status of the module  With INDEXW#16#0006 and W#16#0007: "V" and first number of the version ID |
| OutMod2 | 1 word | With INDEXW#16#0001: Reserved  With INDEXW#16#0006 and W#16#0007: remaining numbers of the version  ID |

#### SZL-ID W#16#xy12 - CPU characteristics (S7-300, S7-400)

##### Purpose

CPU modules have different characteristics depending on the hardware being used. An ID is assigned to each of these characteristics. You obtain the characteristics of this module via the partial list with the SZL-ID (system status list ID) W#16#xy12.

##### Header

The header of the partial list with the SZL-IDW#16#xy12 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0012: All characteristics  W#16#0112: Characteristics of a group; you specify the group in the INDEX parameter.  W#16#0F12: Only SZL partial header information |
| INDEX | Group  W#16#0000: MC7 processing unit  W#16#0100: Time system  W#16#0200: System behavior  W#16#0300: MC7 language description of the CPU   W#16#0400: Availability of the "[C_DIAG](#c_diag-determine-current-connection-status-s7-400)" instruction |
| LENTHDR | W#16#0002: One data record is one word long (2 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-IDW#16#xy12 is one word long. An identifier is entered for each characteristic. A characteristic identifier is one word long.

> **Note**
>
> All data records relevant to your CPU will be output. They follow each other in sequence with no gaps.

##### Characteristic identifier

The following table lists all the characteristic identifiers.

| Identifier | Meaning |
| --- | --- |
| W#16#0000 - 00FF | MC7 processing unit (group with index 0000) |
| W#16#0001 | MC7 processing generating code |
| W#16#0002 | MC7 interpreter |
| W#16#0100 - 01FF | Time system (group with index 0100) |
| W#16#0101 | 1 ms resolution |
| W#16#0102 | 10 ms resolution |
| W#16#0103 | No real time clock |
| W#16#0104 | BCD time-of-day format |
| W#16#0105 | All time-of-day functions (set time-of-day, set and read time-of-day, time-of-day synchronization: time-of-day slave and time-of-day master) |
| W#16#0106 | OB_RT is available |
| W#16#0200 - 02FF | System response (group with index 0200) |
| W#16#0201 | Capable of multiprocessor mode |
| W#16#0202 | Cold restart, warm restart and hot restart possible |
| W#16#0203 | Cold restart and hot restart possible |
| W#16#0204 | Warm restart and hot restart possible |
| W#16#0205 | Only warm restart possible |
| W#16#0206 | New distributed I/O configuration is possible during RUN by using predefined resources |
| W#16#0208 | For taking motion control functionality into account |
| W#16#0300 - 03FF | MC7 language description of the CPU (group with index 0300) |
| W#16#0301 | Reserved |
| W#16#0302 | All 32 bit fixed-point instructions |
| W#16#0303 | All floating-point instructions |
| W#16#0304 | sin, asin, cos, acos, tan, atan, sqr, sqrt, ln, exp |
| W#16#0305 | Accumulator 3/accumulator 4 with associated commands (ENT, PUSH, POP, LEAVE) |
| W#16#0306 | Master control relay instructions |
| W#16#0307 | Address register 1 exists with corresponding instructions |
| W#16#0308 | Address register 2 exists with corresponding instructions |
| W#16#0309 | Operations for area-overlapping addressing |
| W#16#030A | Operations for area-internal addressing |
| W#16#030B | All memory-indirect addressing instructions for bit memory (M) |
| W#16#030C | All memory-indirect addressing instructions for data blocks (DB) |
| W#16#030D | All memory-indirect addressing instructions for DI |
| W#16#030E | All memory-indirect addressing instructions for local data |
| W#16#030F | All instructions for parameter transfer in instructions |
| W#16#0310 | Memory bit edge instructions for I |
| W#16#0311 | Memory bit edge instructions for Q |
| W#16#0312 | Memory bit edge instructions for bit memory |
| W#16#0313 | Memory bit edge instructions for data blocks (DB) |
| W#16#0314 | Memory bit edge instructions for DI |
| W#16#0315 | Memory bit edge instructions for local data (LD) |
| W#16#0316 | Dynamic evaluation of the ERAB bit |
| W#16#0317 | Dynamic local data area with the corresponding instructions |
| W#16#0318 | Reserved |
| W#16#0319 | Reserved |
| W#16#0401 | Reserved |
| W#16#0402 | Reserved |
| W#16#0403 | "[C_DIAG](#c_diag-determine-current-connection-status-s7-400)" is available |

#### SZL-ID W#16#xy13 - user memory areas (S7-300, S7-400)

##### Purpose

You obtain information on the memory areas of the module via the partial list with the SZL-ID (system status list ID) W#16#xy13.

##### Header

The header of the partial list with the SZL-IDW#16#xy13 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0113: Data record for a memory area  You use the INDEX parameter to specify the memory area. |
| INDEX | Specification of a memory area (only with SZL-IDW#16#0113)  W#16#0001: Work memory |
| LENTHDR | W#16#0024: One data record is 18 words long (36 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-IDW#16#xy13 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | Index of a memory area  W#16#0001: Work memory |
| Code | 1 word | Memory type:  - W#16#0001: Volatile memory (RAM) - W#16#0002: Non-volatile memory (FEPROM) - W#16#0003: Mixed memory (RAM and FEPROM) |
| Size | 2 words | Total size of the selected memory (total of Area1 and Area2) |
| Mode | 1 word | Logical mode of the memory  - Bit 0: volatile memory area - Bit 1: non-volatile memory area - Bit 2: mixed memory area   for work memory  - Bit 3: code and data separated - Bit 4: code and data together |
| Granularity | 1 word | Always has the value "0" |
| Area1 | 2 words | Size of the volatile memory area in bytes. |
| Reserved1 | 2 words | Size of the volatile memory area being used |
| Block1 | 2 words | Largest free block in the volatile memory area  If "0": no information available or cannot be ascertained. |
| Area2 | 2 words | Size of the non-volatile memory area in bytes |
| Reserved2 | 2 words | Size of the non-volatile memory area being used |
| Block2 | 2 words | Largest free block in the volatile memory area  If "0": no information available or cannot be ascertained. |

#### SZL-ID W#16#xy14 - system areas (S7-300, S7-400)

##### Purpose

You obtain information on the system areas of the module via the partial list with the SZL-ID (system status list ID) W#16#xy14.

##### Header

The header of the partial list with the SZL-IDW#16#xy14 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0014: All system areas of a module  W#16#0F14: Only SZL partial header information |
| INDEX | irrelevant |
| LENTHDR | W#16#0008: One data record is 4 words long (8 bytes) |
| N_DR | Number of data records  You must at least assign a number of 9 data records. If you select a destination area that is too small, "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" does not provide a data record. |

##### Data record

A data record of the partial list with the SZL-IDW#16#xy14 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | Index of the system area  - W#16#0001: Process image input (number in bytes) - W#16#0002: Process output image (number in bytes) - W#16#0003: Bit memory (number in bits)    **Note:** This index is only provided by the CPU, where the number of flags can be shown in one word.  If your CPU does not provide this value, you must evaluate the index W#16#0008 .  - W#16#0004: Times (number) - W#16#0005: Counters (number) - W#16#0006: Number of bytes in the logical address area - W#16#0007: Local data (total local data area of the CPU in bytes)    **Note:** This index is only provided by CPUs, where the length of the entire local data area can be shown in one word.  If your CPU does not provide this value, you must evaluate the index W#16#0009.  - W#16#0008: Bit memory (number in bytes) - W#16#0009: Local data (total local data area of the CPU in kilobytes) |
| code | 1 word | Memory type  - W#16#0001: Volatile memory (RAM) - W#16#0002: Non-volatile memory (FEPROM) - W#16#0003: Mixed memory (RAM and FEPROM) |
| number | 1 word | Number of elements of the system area |
| retentive | 1 word | Number of retentive elements |

#### SZL-ID W#16#xy15 - block types (S7-300, S7-400)

##### Purpose

If you read the partial list with the SZL-ID (system status list ID) W#16#xy15, you obtain the block types that exist on the module.

##### Header

The header of the partial list with the SZL-IDW#16#xy15 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0015: Data records of all block types of a module |
| INDEX | irrelevant |
| LENTHDR | W#16#000A: One data record is 5 words long (10 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-IDW#16#xy15 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | Block type number  - W#16#0800: OB - W#16#0A00: DB - W#16#0B00: SDB - W#16#0C00: FC - W#16#0E00: FB |
| MaxNumber | 1 word | Maximum number of blocks of the type  - Foi OBs: max. possible number of OBs for a CPU - For DBs: max. possible number of DBs including DB0 - For SDBs: max. possible number of SDBs including SDB2 - For FCs and FBs: max. possible number of loadable blocks |
| MaxLenght | 1 word | Maximum total size of the object to be loaded in kilobytes |
| MaxWorkMem | 2 words | Maximum length of the work memory part of a block in bytes |

#### SZL-ID W#16#xy1C - component identification (S7-300, S7-400)

##### Purpose

If you read the partial list with the SZL-ID (system status list ID) W#16#xy1C, you can identify the CPU or the automation system.

##### Header

The header of the partial list with the SZL-IDW#16#xy1C is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract |
| - W#16#001C: Identification of all components - W#16#011C: Identification of one component - W#16#0F1C: Only SZL partial header information |  |
| INDEX | - Identification of components for a partial list extract with the SZL-IDW#16#011C and W#16#031C   - W#16#0001: Name of the automation system   - W#16#0002: Name of the module   - W#16#0003: System ID of the module   - W#16#0004: Copyright entry   - W#16#0005: Serial number of the module   - W#16#0007: Module type name   - W#16#0008: Serial number of the memory card No data record is supplied for modules in which a memory card cannot be inserted.   - W#16#0009: Manufacturer and profile of a CPU module   - W#16#000A: OEM ID of a module (S7-300 only)   - W#16#000B: Location designation of a module   - W#16#000C: Serial number of Sync module 1   - W#16#000D: Serial number of Sync module 2 - Rack no. for the partial list extract with the SZL-IDW#16#021C (Byte0: Rack no., byte1: B#16#00) |
| LENTHDR | W#16#0022: One data record is 17 words long (34 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-IDW#16#xy1C has the following structure:

**INDEX = W#16#0001**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0001 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#01 |
| name | 12 words | Name of the automation system  (max. 24 characters; when using shorter names, the gaps are filled with B#16#00) |
| res | 4 words | Reserved |

**INDEX = W#16#0002**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0002 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#02 |
| name | 12 words | Name of the module  (max. 24 characters; when using shorter names, the gaps are filled with B#16#00 ) |
| res | 4 words | Reserved |

**INDEX = W#16#0003**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0003 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#03 |
| tag | 16 words | Plant identification of the module  (max. 32 characters; when using shorter system IDs the gaps will be filled with B#16#00) |

**INDEX = W#16#0004**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0004 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#04 |
| copyright | 13 words | Constant character sequence  "Original Siemens Equipment" |
| res | 3 words | Reserved |

**INDEX = W#16#0005**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0005 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#05 |
| serialn | 12 words | Serial number of the module; character string with max. length of 24 characters. Shorter names are filled with B#16#00.  Note: The serial numbers for SIMATIC components are unique worldwide. It is permanently affixed to the CPU hardware, in other words it remains unchanged when the firmware is updated. |
| res | 4 words | Reserved |

**INDEX = W#16#0007**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0007 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#07 |
| cputypname | 16 words | Module type name; character string with a max. length of 32 characters. Shorter names are filled with B#16#00. |

**INDEX = W#16#0008**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0008 - For the partial list extracts W#16#011C, W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#08 |
| sn_mc/mmc | 16 words | Serial number of the Memory Card/Micro Memory Card; character string with a max. length of 32 characters. Shorter names are filled with B#16#00.  - Siemens serial number: only serial number, no index - Product serial number (PSN) of an S7 Micro Memory Card: "MMC" plus serial number (PSN) - Serial number of an S7 Memory Card: "MC" plus serial number   The character string ends immediately after "MMC" or "MC" if no Memory Card is installed. |

**INDEX = W#16#0009**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#0009 - For the partial list extracts W#16#021C and W#16#031C: Byte 0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#09 |
| manufacturer_id | 1 word | See PROFIBUS Profile Guidelines Part 1, Identification &amp; Maintenance Functions |
| profile_id | 1 word | See PROFIBUS Profile Guidelines Part 1, Identification &amp; Maintenance Functions |
| profile_specific_typ | 1 word | See PROFIBUS Profile Guidelines Part 1, Identification &amp; Maintenance Functions |
| res | 13 words | Reserved |

**INDEX = W#16#000A**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#000A - For the partial list extracts: W#16#021C and W#16#031C: Byte0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#0A |
| oem_copyright_string | 13 words | OEM copyright ID; character string with a max. length of 20 characters. Shorter names are filled with B#16#00. |
| oem_id | 1 word | OEM-ID. This is assigned by Siemens. |
| oem_add_id | 2 words | OEM-ID supplemental ID. This can be assigned by the user. |

**INDEX = W#16#000B**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - For a standard CPU and the partial list extract W#16#011C: component ID: W#16#000B - For the partial list extracts: W#16#021C and W#16#031C: Byte0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 Byte 1: component ID: B#16#0B |
| loc_id | 16 words | Location designation; character string with a max. length of 32 characters. Shorter names are filled with B#16#00. |

**INDEX = W#16#000C**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - Byte0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 - Byte 1: Component ID: B#16#0C |
| mlfb | 5 words | 10th to 19th character of the order number of Sync module 1 |
| fill | 1 word | Four spaces (ASCII) |
| es | 1 word | Product version (ASCII), e.g. "01" |
| fill | 1 byte | Two spaces (ASCII) |
| vendor_sn | 17 bytes | Serial number |

> **Note**
>
> If Sync module 1 is not available or cannot be identified, the data record will be filled in accordance with the "index" tag with B#16#00.

**INDEX = W#16#000D**

| Name | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - Byte0:   - Bits 0 to 2: Rack no.;   - Bit 3: 0 = Reserve CPU, 1 = Master CPU;   - Bits 4 to 7: 1111 - Byte 1: Component ID: B#16#0D |
| mlfb | 5 words | 10th to 19th character of the order number of Sync module 2 |
| fill | 1 word | Four spaces (ASCII) |
| es | 1 word | Product version (ASCII), e.g. "01" |
| fill | 1 byte | Two spaces (ASCII) |
| vendor_sn | 17 bytes | Serial number |

> **Note**
>
> If Sync module 2 is not available or cannot be identified, the data record will be filled in accordance with the "index" tag with B#16#00.

#### SZL-ID W#16#xy22 - interrupt status (S7-300, S7-400)

##### Purpose

The partial list with the SZL-ID (system status list ID) W#16#xy22 contains information about the current status of interrupt processing and interrupt generation in the module.

##### Header

The header of the partial list with the SZL-IDW#16#xy22 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0222 Data record for specified interrupt The interrupt (OB no.) is specified in the INDEX parameter. |
| INDEX | OB no. or interrupt class (for SZL-IDW#16#0222)  W#16#0000: Free cycle  W#16#000A: Time-of-day interrupt  W#16#0014: Time-delay interrupt  W#16#001E: Cyclic interrupt  W#16#0028: Hardware interrupt  W#16#0032: DP interrupt  W#16#003C: Synchronous cycle interrupt  W#16#0050: Asynchronous error interrupt  W#16#005A: Background  W#16#0064: Startup   W#16#0078: Synchronous error interrupt |
| LENTHDR | W#16#001C: One data record is 14 words long (28 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-IDW#16#xy22 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Info | 10 words | Start info for the given OB, with following exceptions:  - OB 1 provides the current minimum (in bytes 8 and 9) and maximum cycle time (in bytes 10 and 11) (time base: ms, byte count begins at 0). - When a job is active for a time-delay interrupt, bytes 8 and 11 (byte count begins at 0) get the remaining time in ms left of the delay time set as a parameter. - OB 80 contains the configured minimum (in bytes 8 and 9) and maximum cycle time (in bytes 10 and 11) (time base: ms, byte count begins at 0). - Error interrupts without the current information - Interrupts contain the status info from the current parameter settings of the interrupt source. - In the case of synchronous errors, the priority class B#16#7F is entered if the OBs have not been processed yet; otherwise, the priority class of the last call will be entered. - If an OB has several start events and these have not yet occurred at the information time, then event no. W#16#xyzz returned with:   - x: Event class   - zz: Smallest defined number of the group   - y: undefined Otherwise, the number of the last start event that occurred is used. |
| AlarmStatus1 | 1 word | Processing identifiers:  - Bit 0: Interrupt event is caused by parameters   - = 0: Enabled   - = 1: disabled - Bit 1: Interrupt event as per "[DIS_IRT](#dis_irt-disable-interrupt-event-s7-300-s7-400)"   - = 0: Not disabled   - = 1: disabled - Bit 2 = 1: Interrupt source is active (generate job is present for time interrupts (time-of-day interrupt OB started, time-delay interrupt OB started, cyclic interrupt OB was configured) - Bit 4: Interrupt OB   - = 0: Is not loaded   - = 1: Is loaded - Bit 5: Interrupt OB is by TIS   - = 1: disabled - Bit 6: Entry in diagnostic buffer   - = 1: disabled |
| AlarmStatus2 | 1 word | Reaction with non-loaded/disabled OB  - Bit 0 = 1: Disable interrupt source - Bit 1 = 1: Generate interrupt event error - Bit 2 = 1: CPU goes into STOP mode - Bit 3 = 1: Only discard interrupt |
| AlarmStatus3 | 2 words | Discarded by TIS functions:  Bit no. x set means: the event number that is greater by x than the smallest event number of the affected OB is discarded by the TIS function. |

#### SZL ID W#16#xy25 - assignment of process image partitions to OBs (S7-300, S7-400)

##### Purpose

The partial list with the SZL-ID (system status list ID) W#16#xy25 shows you how process image partitions are assigned to the OBs.

This list provides information about

- Process image partitions you have assigned to specific OBs for update by the system
- Process image partitions you have assigned to specific clock synchronization interrupt OBs (OBs 61 to 64). The partial process image is updated here by calling the "[SYNC_PI](#sync_pi-synchronize-the-process-image-inputs-s7-300-s7-400)" and "[SYNC_PO](#sync_po-synchronize-the-process-image-outputs-s7-300-s7-400)".   
  The assignment of DP master systems to the synchronous cycle interrupt OBs is obtained via [SZL W#16#xy95](#szl-id-w16xy95---extended-dp-master-system-profinet-io-system-information-s7-300-s7-400).

##### Header

The header of the partial list with the SZL-IDW#16#xy25 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#0025: Assignment of all process image partitions to the OBs in the CPU - W#16#0125: Assignment of a process image partition to the corresponding OB  Specify the process image partition ID in the INDEX parameter. - W#16#0225: Assignment of the OB to the corresponding process image partitions  Specify the OB number in the INDEX parameter. Note: The clock synchronization interrupt OBs (OBs 61 to 64) are the only ones you can assign to multiple process image partitions. - W#16#0F25: Only SZL partial header information |
| INDEX | - For SZL-ID W#16#0025: irrelevant - For SZL-ID W#16#0125: Process image partition no. - For SZL-ID W#16#0225: OB no. - For SZL-ID W#16#0F25: irrelevant |
| LENTHDR | W#16#0004: One data record is 2 words long (4 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list extract with the SZL-IDW#16#xy25 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| PPI*_nr | 1 byte | Process image partition no. |
| PPI*_use | 1 byte | Type of assignment between process image partitions and the OB:  - Bit 0 = 1: The process image partition of the inputs is assigned to the specified OB for update by the system. - Bit 1 = 1: The process image partition of the outputs is assigned to the specified OB for update by the system. - Bit 2 = 1: The process image partition input table is assigned to the specified synchronous cycle interrupt OB. It can be updated in this OB by calling "[SYNC_PI](#sync_pi-synchronize-the-process-image-inputs-s7-300-s7-400)". - Bit 3 = 1: The process image partition output table is assigned to the specified synchronous cycle interrupt OB. It can be updated in this OB by calling "[SYNC_PO](#sync_po-synchronize-the-process-image-outputs-s7-300-s7-400)". - Bits 4 to 7: 0 |
| ob_nr | 1 byte | OB no. |
| res | 1 byte | Reserved |
| *PPI: Parial Process Image |  |  |

##### Partial list extracts

- Partial list extract with SZL-ID = W#16#0025:  
  The data records of all partial process images you have assigned to an OB in your configuration are returned in ascending order. For partial process images without OB assignment, ob_nr has the value zero. No data record is returned for partial process images.
- Partial list extract with SZL-ID = W#16#0125:  
  A data record is returned if you have assigned the addressed process image partition to an OB in your configuration. No data record is returned if you have not assigned an OB.

  > **Note**
  >
  > OB 1 is permanently assigned to partial process image 0. You always get a data record for the information about partial process image 0.
- Partial list extract with SZL-ID = W#16#0225:  
  A data record is returned for each partial process image that is assigned to the addressed OB. No data record is returned if you have not assigned the addressed process image partition to an OB in your configuration.

  > **Note**
  >
  > Clock synchronization interrupt OBs can be assigned multiple process image partitions. If this is the case, several data records will be returned.
- Partial list extract with SZL-ID = W#16#0F25:  
  The maximum possible number of data records is returned as number.

##### Example of the meaning of data records

| Call parameters of "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" | Returned variables | Explanation |
| --- | --- | --- |
| SZL_ID = W#16#0125, INDEX = W#16#0008 | PPI*_nr = B#16#08, PPI*_use = B#16#03, ob_nr = B#16#15 | A data record is returned. The input and output process image 8 are assigned to OB 21 for system-side process image update. |
| SZL_ID = W#16#0125, INDEX = W#16#0009 | – | No data record is returned. Thus: process image partition 9 is not assigned to any OB. |
| SZL_ID = W#16#0225, INDEX = W#16#003D | PPI*_nr = B#16#0A, PPI*_use = B#16#C0, ob_nr = B#16#3D  PPI*_nr = B#16#10, PPI*_use = B#16#C0, ob_nr = B#16#3D | Two data records are returned. The input and output process images 10 and 16 are assigned to OB 61. These can be updated in OB 61 by calling "[SYNC_PI](#sync_pi-synchronize-the-process-image-inputs-s7-300-s7-400)" and "[SYNC_PO](#sync_po-synchronize-the-process-image-outputs-s7-300-s7-400)". |
| SZL_ID = W#16#0225, INDEX = W#16#0001 | PPI*_nr = B#16#00, PPI*_use = B#16#03, ob_nr = B#16#01 | A data record is returned. The input and output process image 0 are assigned to OB 1. They are updated by the system. |
| *PPI: Parial Process Image |  |  |

#### SSL ID W#16#xy32 - Communication status data (S7-300, S7-400)

This section contains information on the following topics:

- [SZL-ID W#16#xy32 - communication status data (S7-300, S7-400)](#szl-id-w16xy32---communication-status-data-s7-300-s7-400)
- [Data record of the partial list extract with SZL-ID W#16#0132 index W#16#0005 (S7-300, S7-400)](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w160005-s7-300-s7-400)
- [Data record of the partial list extract with SZL-ID W#16#0132 index W#16#0008 (S7-300, S7-400)](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w160008-s7-300-s7-400)
- [Data record of the partial list extract with SZL-ID W#16#0132 index W#16#000B (S7-300, S7-400)](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w16000b-s7-300-s7-400)
- [Data record of the partial list extract with SZL-ID W#16#0132 index W#16#000C (S7-300, S7-400)](#data-record-of-the-partial-list-extract-with-szl-id-w160132-index-w16000c-s7-300-s7-400)
- [Data record of the partial list extract with SZL-ID W#16#0232 index W#16#0004 (S7-300, S7-400)](#data-record-of-the-partial-list-extract-with-szl-id-w160232-index-w160004-s7-300-s7-400)

##### SZL-ID W#16#xy32 - communication status data (S7-300, S7-400)

###### Purpose

If you read the partial list with SZL-IDW#16#xy32 you obtain the communication status data of the module.

###### Header

The header of the partial list with the SZL‑IDW#16#xy32 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL‑ID of the partial list extract  - W#16#0132: Status data for one communication section (always only one data record). Specify the communication section with the INDEX parameter. - W#16#0232: status data for one communication unit. Specify the communication section with the INDEX parameter. |
| INDEX | Communication section  - For SZL‑IDW#16#0132:   - W#16#0005 Diagnostics   - W#16#0008 Time system   - W#16#000B Time system   - W#16#000C Time system - For SZL‑IDW#16#0232:   W#16#0004 CPU protection level, operator switch settings and   version IDs / checksums |
| LENTHDR | W#16#0028: One data record is 20 words long (40 bytes) |
| N_DR | Number of data records |

###### Data record

A data record of the partial list with the SZL-IDW#16#0132 is always 20 words long. The data records have different contents. The contents depend on the INDEX parameter, in other words, on the communication section to which the data record belongs.

##### Data record of the partial list extract with SZL-ID W#16#0132 index W#16#0005 (S7-300, S7-400)

###### Contents

The partial list extract with the SZL-IDW#16#0132 and the IndexW#16#0005 contains information about the diagnostics status of the module.

###### Data record

A data record of the partial list extract with the SZL-IDW#16#0132 and the IndexW#16#0005 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | W#16#0005: Diagnostics |
| ext | 1 word | Extended functions   - 0: No - 1: Yes |
| send | 1 word | Automatic send  - 0: No - 1: Yes |
| possible | 1 word | Sending user-defined diagnostic messages currently possible   - 0: No - 1: Yes |
| res | 16 words | Reserved |

##### Data record of the partial list extract with SZL-ID W#16#0132 index W#16#0008 (S7-300, S7-400)

###### Contents

The partial list extract with the SZL-IDW#16#0132 and the IndexW#16#0008 contains information about the status of the module time system.

###### Data record

A data record of the partial list extract with the SZL-IDW#16#0132 and the IndexW#16#0008 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | W#16#0008: Time system status |
| cycle | 1 word | Reserved |
| corr | 1 word | Correction factor for the time |
| clock 0 | 1 word | Runtime meter 0: time in hours |
| clock 1 | 1 word | Runtime meter 1: time in hours |
| clock 2 | 1 word | Runtime meter 2: time in hours |
| clock 3 | 1 word | Runtime meter 3: time in hours |
| clock 4 | 1 word | Runtime meter 4: time in hours |
| clock 5 | 1 word | Runtime meter 5: time in hours |
| clock 6 | 1 word | Runtime meter 6: time in hours |
| clock 7 | 1 word | Runtime meter 7: time in hours |
| time | 4 words | Current date and time (format: date_and_time) |
| rtm _0 | 1 byte | Runtime meter  Bit x: Overflow of runtime meter x, 0 ≤ x ≤ 7 (Bit = 1: run-time meter is busy) |
| res | 1 byte | Reserved |
| rtmOV _0 | 1 byte | Runtime meter Overflow  Bit x: Overflow of runtime meter x, 0 ≤ x ≤ 7 (Bit = 1: Overflow) |
| res | 1 byte | Reserved |
| status | 1 word | Time status (for bit assignment, see below) |
| res | 3 bytes | Reserved |
| status_valid | 1 byte | Validity of variable status: B#16#01: status valid |

###### Time-of-day status (status)

| Bit | Default value | Description |
| --- | --- | --- |
| 15 | 0 | Sign for the correction value  (0: positive, 1: negative) |
| 14 to 10 | 00000 | Correction value  This parameter allows the basic time in the frame to be corrected to local time:   `Local time = basic time ± correction value * 0.5 h`   This correction takes into account the time zone and the time difference in summer time (daylight savings time) and winter time (standard time). |
| 9 | 0 | Reserved |
| 8 | 0 | Reserved |
| 7 | 0 | Notification hour  This parameter indicates whether the next time adjustment also includes a switchover from summer (daylight savings time) to winter time (standard time) or vice versa. (0: no adjustment made, 1: adjustment made). |
| 6 | 0 | Summer time (daylight savings time)/winter time (standard time) indicator  This parameter indicates whether the local time calculated using the correction value is summer or winter time. )0Ö winter time, 1: summer time) |
| 5 | 0 | Parameter not used by S7. |
| 4 to 3 | 00 | Time resolution  This parameter indicates the resolution of the transmitted clock time. (00: 0.001 s, 01: 0.01 s, 10: 0.1 s, 11: 1 s) |
| 2 | 0 | Parameter not used by S7. |
| 1 | 0 | Parameter not used by S7. |
| 0 | 0 | Synchronization failure  This parameter indicates whether the time transmitted in the message frame from an external time master (e.g. SICLOCK) is synchronized.  (0: synchronization failed, 1: synchronization occurred)   **Note:**  Evaluation of this bit in a CPU is only meaningful if there is continuous external time synchronization. |

##### Data record of the partial list extract with SZL-ID W#16#0132 index W#16#000B (S7-300, S7-400)

###### Contents

The partial list extract with the SZL-IDW#16#0132 and the IndexW#16#000B contains information about the status of 32-bit runtime meter 0 to 7 of the module.

> **Note**
>
> In the partial list extract with the SZL-IDW#16#0132 and the IndexW#16#0008 this runtime meter is displayed as 16-bit runtime meter.  
> With it you can continue to implement programs that were developed for a CPU with 16-bit runtime meters, and which continue to use the partial list extract with the SZL-IDW#16#0132 and the IndexW#16#0008.

###### Data record

A data record of the partial list extract with the SZL-IDW#16#0132 and the index W#16#000B has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | W#16#000B: Time system status |
| rtm _0 | 1 byte | Runtime meter  Bit x: Overflow of runtime meter x, 0 ≤ x ≤ 7 (Bit = 1: run-time meter is busy) |
| res | 1 byte | Reserved |
| rtmOV _0 | 1 byte | Runtime meter overflow  Bit x: Overflow of runtime meter x, 0 ≤ x ≤ 7 (Bit = 1: Overflow) |
| res | 1 byte | Reserved |
| clock 0 | 2 words | Runtime meter 0: time in hours |
| clock 1 | 2 words | Runtime meter 1: time in hours |
| clock 2 | 2 words | Runtime meter 2: time in hours |
| clock 3 | 2 words | Runtime meter 3: time in hours |
| clock 4 | 2 words | Runtime meter 4: time in hours |
| clock 5 | 2 words | Runtime meter 5: time in hours |
| clock 6 | 2 words | Runtime meter 6: time in hours |
| clock 7 | 2 words | Runtime meter 7: time in hours |
| res | 1 word | Reserved |

##### Data record of the partial list extract with SZL-ID W#16#0132 index W#16#000C (S7-300, S7-400)

###### Contents

The partial list extract with the SZL-IDW#16#0132 and the INDEXW#16#000C contains information about the status of 32-bit runtime meter 8 to 15 of the module.

###### Data record

A data record of the partial list extract with the SZL-IDW#16#0132 and the INDEXW#16#000C has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | W#16#000C: Time system status |
| rtm_0 | 1 byte | Runtime meter  Bit x: Status of run-time meter (8+x) , 0 ≤ x ≤ 7 (Bit = 1: run-time meter is busy) |
| res | 1 byte | Reserved |
| rtmOV _0 | 1 byte | Runtime meter overflow  Bit x: Overflow of run-time meter (8+x) , 0 ≤ x ≤ 7 (Bit = 1: Overflow) |
| res | 1 byte | Reserved |
| clock 8 | 2 words | Runtime meter 8: time in hours |
| clock 9 | 2 words | Runtime meter 9: time in hours |
| clock 10 | 2 words | Runtime meter 10: time in hours |
| clock 11 | 2 words | Runtime meter 11: time in hours |
| clock 12 | 2 words | Runtime meter 12: time in hours |
| clock 13 | 2 words | Runtime meter 13: time in hours |
| clock 14 | 2 words | Runtime meter 14: time in hours |
| clock 15 | 2 words | Runtime meter 15: time in hours |
| res | 1 word | Reserved |

##### Data record of the partial list extract with SZL-ID W#16#0232 index W#16#0004 (S7-300, S7-400)

###### Contents

The partial list extract with the SZL-IDW#16#0232 and the Index W#16#0004 contains information about the CPU protection level and the settings of the operator mode switch and checksums of the hardware configuration and the user program.

###### Data record

A data record of the partial list extract with the SZL-IDW#16#0232 and the Index W#16#0004 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| Index | 1 word | - Byte 1:   B#16#04: CPU protection level, operator control settings and checksums - Byte 0:   Standard CPU: B#16#00   Bit 3: 0 = Reserve CPU, 1 = Master CPU   Bits 4 to 7: 1111 |
| ProtLevel_ModeSwitch | 1 word | Protection level set with the mode selector (1, 2, 3) |
| ProtLevel_Par | 1 word | Protection level set in parameters (0, 1, 2, 3; 0: no password, protection level invalid). |
| ProtLevel_Valid | 1 word | Valid protection level of the CPU |
| ModeSwitch | 1 word | Mode selector setting (1:RUN, 2:RUN-P, 3:STOP, 4:MRES,  0:undefined or cannot be determined) |
| Startup_ModeSwitch | 1 word | Startup switch setting (1:CRST, 2:WRST, 0:undefined, does  not exist or cannot be determined) |
| res | 1 word | Reserved |
| ID_Val_CheckSum | 1 word | ID for the validity of the four following checksums (0: invalid) |
| ID_CheckSum1_HWConf | 1 word | Checksum 1 of the hardware configuration (Intel format): Exclusive OR link over the lengths of all system data blocks. |
| ID_CheckSum2_HWConf | 1 word | Checksum 2 of the hardware configuration (Intel format): Exclusive OR link over the checksums of all system data blocks. |
| ID_CheckSum1_UserProg | 1 word | Checksum 1 of the user program (Intel format): Exclusive-or link over the lengths of the following blocks: OBs, DBs, FBs, FCs |
| ID_CheckSum2_UserProg | 1 word | Checksum 2 of the user program (Intel format): Exclusive-or link over the checksums of the following blocks: OBs, DBs, FBs, FCs |
| res | 2 words | Reserved |
| sfc_req | 1 word | Protection level 2 or 3 request by the instruction "PROTECT" (1: request has been made) |
| sfc_act | 1 word | Protection level 2 or 3 activation by the instruction "PROTECT" (1: activated) |
| res | 4 words | Reserved |

#### SZL-ID W#16#xy74 - status of the module LEDs (S7-300, S7-400)

##### Purpose

If you read the partial list with SZL-ID W#16#xy74 with standard CPUs (if present) you obtain the status of the module LEDs.

##### Header

The header of the partial list with the SZL-ID W#16#xy74 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0174 Status of an LED.   You use the INDEX parameter to select the LED. |
| INDEX | LED ID (only relevant for  SZL-IDW#16#0174)  - W#16#0001: SF (group error ) - W#16#0002: INTF (internal fault) - W#16#0003: EXTF (external fault) - W#16#0004: RUN - W#16#0005: STOP - W#16#0006: FRCE (Force) - W#16#0007: CRST (cold restart) - W#16#0008: BAF (battery fault/overload,  short circuit of battery voltage on bus) - W#16#0009: USR (user-defined) - W#16#000A: USR1 (user-defined) - W#16#000B: BUS1F (bus fault interface 1) - W#16#000C: BUS2F (Bus error interface 2) and BUS5F (Bus error interface 5) for the CPUs 414-3 PN/DP,416-3 PN/DP and 416F-3 PN/DP - W#16#0012: IFM1F (interface fault interface module 1) - W#16#0013: IFM2F (interface fault interface module 2) - W#16#0014: BUS3F (bus fault interface 3) - W#16#0015: MAINT (maintenance request) - W#16#0016: DC24V - W#16#0017: BUS5F (bus fault interface 5) - W#16#0080: IF (init failure) - W#16#0081: UF (user failure) - W#16#0082: MF (monitoring failure) - W#16#0083: CF (communication failure) - W#16#0084: TF (task failure) - W#16#00EC: APPL_STATE_RED - W#16#00ED: APPL_STATE_GREEN |
| LENTHDR | W#16#0004: One data record is 2 words long (4 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-ID W#16#xy74 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| CPU_LED_ID | 1 word | - Byte 0:   - Standard CPU: B#16#00   - Bit 3: 0=standby CPU, 1=master CPU   - Bits 4 to 7: 1111 - Byte 1: LED ID |
| LED_on | 1 byte | Status of the LED:  - 0: off - 1: on |
| LED_flash | 1 byte | Flashing status of the LED:  - 0: not flashing - 1: flashing normally (2 Hz) - 2: flashing slowly (0.5 Hz)) |

#### SZL-ID W#16#xy90 - DP master system information (S7-300, S7-400)

##### Purpose

If you read the partial list SZL-IDW#16#xy90, you obtain the status information of all DP master systems known to the CPU.

##### Header

The header of the partial list with the SZL-IDW#16#xy90 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  W#16#0090: Information regarding all DP master systems known to the CPU  W#16#0190: Information regarding one DP master system  W#16#0F90: Only SZL partial header information |
| INDEX | - For the partial list extract with the SZL-IDW#16#0190:   - Low byte: B#16#00   - High byte: DP master system ID - For the partial list extract with the SZL-IDW#16#0090 and W#16#0F90:   - W#16#0000 |
| LENTHDR | W#16#000E: One data record is 7 words long (14 bytes) |
| N_DR | Number of data records  For the partial list extract with the SZL-IDW#16#0190: 0 to 1  For the partial list extract with the SZL-IDW#16#0090:  - For a standard CPU: 0 to 14 |

##### Data record

A data record of the partial list with the IDW#16#xy90 has the following structure:

| Name | Length | Meaning |  |
| --- | --- | --- | --- |
| dp_m_id | 1 byte | DP master system ID |  |
| dp_m_rack | 1 byte | Rack number of the DP master  - For a standard CPU: 0 |  |
| dp_m_slot | 1 byte | Slot of the DP master or   slot of the CPU (with integrated DP interface) |  |
| dp_m_SubModule | 1 byte | - with integrated DP interface: interface number of the DP master:   - 1: X2   - 2: X1   - 3: IF1   - 4: IF2 - with external DP interface: 0 |  |
| logadr | 1 word | logic start address of the DP master |  |
| res | 1 word | Reserved |  |
| res | 1 word | Reserved |  |
| dp_m_state | 1 byte | additional properties of the DP master system |  |
| Bit 0: | DP mode  - 0: S7-compatible - 1: DPV1 |  |  |
| Bit 1: | DP cycle  - 0: not constant bus cycle - 1: constant bus cycle |  |  |
| Bit 2 to 6: | - Reserved |  |  |
| Bit 7: | DP master type  - 0: integrated DP master - 1: external DP master |  |  |
| res | 3 bytes | Reserved |  |

#### SZL-ID W#16#xy91 - module status information (S7-300, S7-400)

##### Purpose

If you read the partial list with SZL-ID W#16#xy91, you obtain the status information of modules assigned to the CPU.

> **Note**
>
> An evaluation of the SZL-ID W#16#xy91 is not possible for a module with packed addresses (ET 200S).

##### Header

The header of the partial list with the SZL-ID W#16#xy91 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#0091 Module status information of all inserted and configured modules/sub-modules of the CPU (S7-400 only) - W#16#0191 Status information of all modules / racks with incorrect module ID that are not disabled (S7-400 only) - W#16#0291 Module status information of all modules that are disrupted and not disabled (S7-400 only) - W#16#0391 Module status information of all modules that are not available (S7-400 only) - W#16#0591 Module status information of all sub-modules of the host  module - W#16#0991 Module status information of one DP master system - W#16#0A91 Status information of all DP sub and master systems (S7-300 only without CPU 318-2 DP) or PROFINET IO systems - W#16#0C91 Module status information of a module in the central rack or on an integrated DP interface module or on a PROFINET interface module over the logical base address - W#16#4C91 Module status information of a module on an external DP interface module using the logical base address   If you use more than four external DP interface modules,RET_VAL W#16#80A4 may occur incorrectly. - W#16#0D91 Module status information of all modules in the specified rack/ station (DP or PROFINET) - W#16#0E91 Module status information of all assigned modules - W#16#0F91 Only SZL partial header information |
| INDEX | - For the partial list extract with the SZL-ID W#16#0C91:   - S7-400:     Bits 0 to 14: Logical base address of the module,      Bit 15: 0 = input, 1 = output   - S7-300:     Bits 0 to 14: Any logical address of the module,      Bit 15: 0 = input, 1 = output - For the partial list extract with the SZL-ID W#16#4C91 (S7-400 only):   - Bits 0 to 14: Logical base address of the module,   - Bit 15: 0 = input / 1 = output - For the partial list extract with the SZL IDs W#16#0091, W#16#0191,W#16#0291, W#16#0391, W#16#0491, W#16#0591, W#16#0A91, W#16#0E91, W#16#0F91:   INDEX is irrelevant, all modules (in rack and in distributed I/O devices) - For the partial list extract with the SZL-ID W#16#0991 (S7-400 only):   W#16#xx00: All modules of a DP master system (xx contains the DP master system ID) - For the partial list extract with the SZL-ID W#16#0D91   - W#16#00xx: All modules and interface modules of a rack (xx contains the number of the rack)   - W#16#xxyy: All modules of a DP station or all IO devices of a PROFINET IO station (PROFIBUS DP: xx contains the DP master system ID, yy the station number; PROFINET IO: Bit 0 to 10: station number, bits 11 to 14: the last two places in the PNIO subsystem ID, bit 15: 1 (see third illustration below for adr1) |
| LENTHDR | W#16#0010: One data record is 8 words long (16 bytes) |
| N_DR | Number of data records; depending on the product the number of records transferred in the "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" can be lower |

In the case of W#16#0091, W#16#0191 and W#16#0F91 two additional data records are supplied per rack:

- A record for the power supply in as far as it exists and has been planned and
- a record for the rack.

The sequence of the records in case of a centralized structure is: PS, Slot 1, Slot 2, ..., Slot 18, rack.

A data record of the partial list with the ID W#16#xy91 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| adr1 | 1 word | - For a central configuration: number of the rack - For a distributed configuration with PROFIBUS DP: DP master system ID, station number - For a distributed configuration with PROFINET IO: bit 15 = 1 (PROFINET IO identifier) the last two places in the PROFINET IO system ID, station number   Note: A PROFINET interface is always handled as a "sub-module in the central configuration", regardless of the use for PROFINET IO. |
| adr2 | 1 word | - For a central configuration and a distributed configuration with PROFIBUS DP: slot number and sub-module slot number - For a distributed configuration with PROFINET IO: slot number Note: A PROFINET interface is always handled as a "sub-module in the central configuration", regardless of the use for PROFINET IO. |
| LogicalAddr | 1 word | First assigned logical I/O address (base address) |
| SetType | 1 word | PROFINET IO: expected (configured ) type (see below) otherwise reserved |
| ActualType | 1 word | PROFINET IO: actual type (see below) otherwise reserved |
| res | 1 word | 00xx=CPU no.1-4 (only S7-400)  for PROFINET IO:  - SZL-ID=W#16#0C91: Number of actually existing sub-modules (without sub-module 0) - SZL-ID=W#16#0D91: Number of sub-modules (without sub-module 0) - SZL-ID=W#16#4C91: Number of actually existing sub-modules (without sub-module 0) - SZL-ID=W#16#4D91: Number of actually existing sub-modules (without sub-module 0) |
| IOStat | 1 word | I/O status  - Bit 0 = 1: Module faulty (detected by diagnostic interrupt) - Bit 1 = 1: module exists - Bit 2 = 1: module does not exist - Bit 3 = 1: module disabled - Bit 4 = 1: station error (only representative slot) - Bit 5 = 1: A CiR event at this module / station is busy or not yet completed - Bit 6 = 1: reserved for S7-400 - Bit 7 = 1: module in local bus segment - Bit 8 to 15: Data ID for logical address (input: B#16#B4, output: B#16#B5, integrated DP interface: B#16#FE, external DP interface: B#16#FF) |
| AreaID_ModuleWidth | 1 word | Area identification/module width  - Bit 0 to 2: Module width - Bit 3: Reserved - Bit 4 to 6: Area ID   - 0 = S7-400   - 1 = S7-300   - 2 = ET area   - 3 = P-area   - 4 = Q-area   - 5 = IM3-area   - 6 = IM4-area - Bit 7: Reserved |

At certain modules the following values are indicated in the record:

| Name | PS  (S7-400 only) | CPU | IFM-CPU  (S7-300) | Rack  (only S7-400) |
| --- | --- | --- | --- | --- |
| adr1 | Number of the rack | Standard information as described above | Standard information as described above | Number of the rack |
| adr2 | W#16#01FF | W#16#0200 or W#16#0200 to W#16#1800 | W#16#0200 | W#16#00FF |
| LogicalAddr | W#16#0000 | W#16#7FFF | W#16#007C | W#16#0000 |
| SetType | Standard information as described above | W#16#00C0 or W#16#0081 or W#16#0082 | W#16#00C0 | Standard information as described above |
| IOStat | W#16#0000 | Standard information as described above | Standard information as described above | W#16#0000 |
| AreaID_ModuleWidth | W#16#0000 | W#16#0011 or W#16#0001 or W#16#0002 | W#16#0011 | W#16#0000 |

##### Parameter adr1

The adr1 parameter contains:

- In a central configuration, the rack number (0-31).

  ![Parameter adr1](images/19552276235_DV_resource.Stream@PNG-en-US.png)
- In a distributed configuration with PROFIBUS DP

  - The DP master system ID (1-32)
  - The station number (0-127).

    ![Parameter adr1](images/19552115851_DV_resource.Stream@PNG-en-US.png)
- In a distributed configuration with PROFINET IO:

  - Identifier bit for PROFINET IO (bit 15)
  - The last two positions in the PROFINET IO system ID (0-15). To obtain the complete PROFINET IO system ID, you must add 100 (decimal) to it.
  - The station number (0-2047).

    ![Parameter adr1](images/19552237579_DV_resource.Stream@PNG-en-US.png)

##### Parameter adr2

The adr2 parameter contains:

- For a central configuration and for distributed configuration with PROFIBUS DP, the slot number and the sub-module slot number.

  ![Parameter adr2](images/19552256907_DV_resource.Stream@PNG-en-US.png)
- For a distributed configuration with PROFINET IO, the slot number.

##### Set type parameter (SetType) and actual type parameter (ActualType) for PROFINET IO

| Type identifier  (W#16#...) | Meaning |
| --- | --- |
| 8100 | Entered for expected (configured) type and actual type if type check is not possible |
| 8101 | Entered for expected (configured) type if a type check is possible |
| 8101 | Entered as actual type if expected = actual |
| 8102 | Entered as actual type if expected &lt;&gt; actual |

#### SZL-ID W#16#xy92 - rack / station status information (S7-300, S7-400)

##### Purpose

If you read the partial list with the SZL-IDW#16#xy92, you obtain information about the expected and the actual hardware configuration of centrally installed racks and stations of a DP master system.

##### Reading out the SZL using "RDSYSST" for an S7-400 CPU

If you read out the partial list with "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" you must strictly ensure that the parameters SZL_ID and INDEX of "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" match each other.

| SZL_ID | INDEX |
| --- | --- |
| W#16#0092 or  W#16#0192 or  W#16#0292 or  W#16#0392 or  W#16#0492 or  W#16#0592 or  W#16#0692 | DP master system ID of a DP master system which is connected via an **integrated** DP connection. |
| : | : |
| W#16#4092 or  W#16#4292 or  W#16#4692 | DP master system ID of a DP master system which is connected via an **external** DP connection. |

##### Header

The header of the partial list with the SZL-IDW#16#xy92 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#0092: Set status of the central racks / stations of a DP master system connected via an integrated DP interface module. - W#16#4092: Set status of the stations of a DP master system  connected via an external DP interface module - W#16#0192: Activation status of the stations of a DP master system that is connected via an integrated DP interface module - W#16#0292: Set status of the central racks / stations of a DP master system connected via an integrated DP interface module. - W#16#0392: Status of the backup batteries in a rack / module rack of a CPU after at least one battery has failed - W#16#0492: Status of the overall battery backup of all racks / module racks of a CPU - W#16#0592: Status of the 24 V power supply to all racks / module racks of a CPU - W#16#4292: Actual status of the stations of a DP master system that is connected via an external DP interface module - W#16#0692: Diagnostics status of the expansion racks in the central configuration / stations of a DP master system connected via an integrated DP interface - W#16#4692: Diagnositics status of the stations of a DP master system connected via an external DP interface |
| INDEX | 0 / DP master system  ID |
| LENTHDR | W#16#0010: Data record is eight words long (16 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the IDW#16#xy92 has the following structure:

| Contents | Length | Meaning |
| --- | --- | --- |
| status_0 to status_15 | 16 bytes | Rack status/ station status or backup status. (The backup status is only relevant for DP modules)  - W#16#0092:   - Bit=0: rack/station not configured   - Bit=1: rack/station not configured - W#16#4092:   - Bit=0: station not configured   - Bit=1: Station configured - W#16#0192:   - Bit=0: Station is not configured or configured and activated   - Bit=1: station is configured and activated - W#16#0292:   - Bit=0: Rack/station failure, deactivated or not configured   - Bit=1: Rack/station exists, activated and has not failed - W#16#4292:   - Bit=0: Station failure, deactivated or not configured   - Bit=1: Station exists, activated and has not failed - W#16#0692:   - Bit=0: All modules of the expansion rack / station exist, are available with no problems and the station is activated   - Bit=1: At least one module of the expansion rack / station is not OK or the station is deactivated - W#16#4692:   - Bit=0: All modules of a station exist, are available with no problems and the station is activated   - Bit=1: At least one module of a station is not OK or the station is deactivated |
| status_0 | 1 byte | Bit 0: Central rack (INDEX = 0) or station 1 (INDEX &lt;&gt; 0)  Bit 1: 1. Expansion rack or station 2    :   :  Bit 7: 7. Expansion rack or station 8 |
| status_1 | 1 byte | Bit 0: 8. Expansion rack or station 9    :   :  Bit 7: 15. Expansion rack or station 16 |
| status_2 | 1 byte | Bit 0: 16. Expansion rack or station 17    :   :  Bit 5: 21. Expansion rack or station 22  Bit 6: 0 or station 23  Bit 7: 0 or station 24 |
| status_3 | 1 byte | Bit 0: 0 or station 25    :   :  Bit 5: 0 or station 30  Bit 6: Expansion rack SIMATIC S5 area or station 31  Bit 7: 0 or station 32 |
| status_4 | 1 byte | Bit 0: 0 or station 33    :   :  Bit 7: 0 or station 40 |
| :  : |  |  |
| status_15 | 1 byte | Bit 0: 0 or station 121    :   :  Bit 7: 0 or station 128 |

#### SZL-ID W#16#0x94 - status information for rack/station (S7-300, S7-400)

##### Purpose

The partial list with the SZL-IDW#16#0x94 contains information about the set and actual configuration of module racks in central configurations and stations of a PROFIBUS DP master system/PROFINET IO controller system.

##### Header

The header of the partial list with the SZL-IDW#16#0y94 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#0094:   Set status of the rack in the central rack / stations of an IO controller system (Status bit = 1: rack/station configured) - W#16#0194:   Activation status of a station of an IO controller system that is configured and deactivated (Status bit =1) - W#16#0294:   Set status of the rack in the central rack / stations of an IO controller system (Status bit = 1: rack/station exists, activated and not failed) - W#16#0694:   Diagnostic status of the expansion units in the central rack / stations of an IO controller system (Status bit = 1: At least one module of the rack/station is disrupted or deactivated) - W#16#0794:   Diagnostic / maintenance status of the central rack / stations of an IO controller system (Status bit = 0: No fault and no maintenance necessary, Status bit = 1: Rack / station has malfunction or / and maintenance required or / and maintenance demanded) - W#16#0F94:   Only header information |
| INDEX | - 0: Central module - 1-32: Distributed module on PROFIBUS DP - 100-115: distributed module on PROFINET IO |
| LENTHDR | Length of the following data record |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the IDW#16#0y94 has the following structure:

| Contents | Length | Meaning |
| --- | --- | --- |
| index | 1 word | - 0: Central module - 1-32: Distributed module on PROFIBUS DP - 100-115: distributed module on PROFINET IO |
| status_0 | BOOL | Group information  - 1: At least one of the following status bits has the value 1 - 0: all the following status bits have the value 0 |
| status_1 | BOOL | Status, station 1 |
| status_2 | BOOL | Status, station 2 |
| .. |  |  |
| status_2047 | BOOL | Status, station 2047 |

A status bit of non-configured racks/stations/devices has the value "0".

> **Note**
>
> **Important difference to the previous SZL-IDW#16#xy92**
>
> Compared to the previous SZL-IDW#16#xy92, the data have been shifted by one bit since bit status_0 is used for group information.

#### SZL-ID W#16#xy95 - extended DP master system / PROFINET IO system information (S7-300, S7-400)

##### Purpose

The partial list with the SZL-IDW#16#xy95 supplies you with extended status information on all DP master systems/PROFINET IO systems known to the CPU. Compared to the partial list with the SZL-IDW#16#xy90, this list contains information about PROFINET IO systems and additional information about the isochronous mode of a DP master system.

##### Header

The header of the partial list with the SZL-IDW#16#xy95 is structured as follows:

| Contents | Meaning |  |  |
| --- | --- | --- | --- |
| SZL-ID | The SZL-ID of the partial list extract |  |  |
|  | W#16#0195: | Extended information on a DP master system/PROFINET IO system |  |
|  | W#16#0F95: | Only SZL partial header information |  |
| INDEX | - For the partial list extract with the SZL-IDW#16#0195:   - Low byte: B#16#00   - High byte: DP master system ID/PROFINET IO system ID - For the partial list extract with the SZL-IDW#16#0F95:   - W#16#0000 |  |  |
| LENTHDR | W#16#0028: |  | one data record is 20 words long (40 bytes) |
| N_DR | Number of data records:  For the partial list extract with the SZL-IDW#16#0195: 0 to 1 |  |  |

##### Data record

A data record of the partial list with the IDW#16#xy95 has the following structure:

| Name | Length | Meaning |  |
| --- | --- | --- | --- |
| dp_m_id | 1 byte | DP master system ID/PROFINET IO system ID |  |
| dp_m_rack | 1 byte | Rack number of the DP master / IO controller  - For a standard CPU: 0 |  |
| dp_m_slot | 1 byte | Slot of the DP master / IO controller or   slot of the CPU (with integrated DP interface) |  |
| dp_m_SubModule | 1 byte | - with integrated DP interface: Interface ID of the DP master / IO controller:   - 1: X2   - 2: X1   - 3: IF1   - 4: IF2 - with external interface: 0 |  |
| LogicalAddr | 2 bytes | Logical start address of the DP master / IO controller |  |
| res | 2 bytes | Reserved |  |
| res | 2 bytes | Reserved |  |
| dp_m_state | 1 byte | - Additional properties of the DP master system / PROFINET IO system |  |
| Bit 0: | DP mode (PROFIBUS DP only)  - 0: S7-compatible - 1: DPV1 |  |  |
| Bit 1: | DP and PN cycle  - 0: not constant bus cycle - 1: constant bus cycle |  |  |
| Bit 2 to 6: | - Reserved |  |  |
| Bit 7: | Type of DP master / IO controller  - 0: integrated DP master / IO controller - 1: external DP master / IO controller |  |  |
| dp_address | 1 byte | DP node number (PROFIBUS address) |  |
| res | 2 bytes | Reserved |  |
| SyncCyclInter_OB | 1 byte | Assigned synchronous cycle interrupt OB (only relevant if the DP cycle is equidistant) |  |
| res | 1 byte | Reserved |  |
| baudrate | 4 bytes | Baud rate of the DP master system and PNIO system as hex value |  |
| IsoDPCycle | 4 bytes | Period of the equidistant DP and PN cycle in μs |  |
| res | 16 bytes | Reserved |  |

#### SZL-ID W#16#xy96 - PROFINET IO and PROFIBUS DP module status information (S7-300, S7-400)

##### Purpose

If you read the partial list with SZL-IDW#16#xy96, you obtain the status information of modules assigned to the CPU.

The information in the partial list with the SZL-IDW#16#xy96 supplements SZL-ID[W#16#xy91](#szl-id-w16xy91---module-status-information-s7-300-s7-400) and provides additional status data on modules and sub-modules.

It provides information specific to PROFINET IO as well as information on PROFIBUS DP modules and central modules.

##### Header

The header of the partial list with the SZL-IDW#16#xy96 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#0696   Module status information of all sub-modules of a specified module (with PROFIBUS DP and central modules, the sub-module level does not exist). - W#16#0C96   Module status information of a module/sub-module located centrally or on a PROFIBUS DP/PROFINET interface via the start address. |
| INDEX | - Bits 0 to 14: Address of the module - Bit 15: 0 = input, 1 = output |
| LENTHDR | Length of the following data record |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the IDW#16#xy96 has the following structure:

| Contents | Length | Meaning |  |  |
| --- | --- | --- | --- | --- |
| LogicalAddr | 1 word | - Bits 0 to 14: Address of the module - Bit 15: 0 = input, 1 = output |  |  |
| System | 1 word | Identifier for the central module/DP master system ID /PROFINET IO system ID:  - 0: Central module - 1-32: Distributed module on PROFIBUS DP - 100-115: distributed module on PROFINET IO |  |  |
| API* | 2 words | Configured user profile for a distributed PROFINET device.  Profiles are sector-specific or technology-specific specifications that go beyond the PROFINET standard.   Profile 0 means that the data correspond to the specification in the PROFINET standard. |  |  |
| Station | 1 word | Rack no./station number/device number |  |  |
| Slot | 1 word | Slot no. |  |  |
| Subslot | 1 word | Sub-module slot (if no sub-module can be inserted, "0" must be entered here) |  |  |
| Offset | 1 word | Offset in user data address area of the associated module |  |  |
| SetType | 7 words | Expected type  The expected type is has a hierarchical structure in PROFINET IO |  |  |
| **Word** | **PROFINET IO** | **PROFIBUS DP** |  |  |
| 1: | Manufacturer number or profile ID (e.g.: W#16#FF00 for PROFIBUS) | 0000 |  |  |
| 2: | Device | 0000 |  |  |
| 3: | Sequential number or profile index | 0000 |  |  |
| 4: | 1. word of the double word for sub-module identification | Type identifier |  |  |
| 5: | 2. word of the double word for sub-module identification | 0000 |  |  |
| 6: | 1. word of the double word for sub-module identification | 0000 |  |  |
| 7: | 2. word of the double word for sub-module identification | 0000 |  |  |
| SetType_UnEqual_ActualType | 1 word | Expected/actual identifier  - Bit 0 = 0: Set matches actual - Bit 0 = 1: Set unequal to actual - Bit 1 to 15: Reserved |  |  |
| res | 1 word | Reserved |  |  |
| IOStat | 1 word | I/O status  - Bit 0 = 1: Module faulty (detected by diagnostic interrupt) - Bit 1 = 1: Module exists  Bit 2 = 1: Module does not exist - Bit 3 = 1: Module disabled  Bit 4 = 1: station error (only representative slot) - Bit 5 = 1: M7: Module can be host module for sub-modules :   S7: A CiR event at this module /station is busy or not yet completed - Bit 6 = 1: reserved for S7-400 - Bit 7 = 1: Module in local bus segment (S7-300 only) - Bit 8 = 1: Module maintenance demanded ("green") - Bit 9 = 1: Module maintenance request ("yellow") - Bit 10 to 15: Reserved |  |  |
| AreaID_ModuleWidth | 1 word | Area identification/module width  - Bit 0 to 2: Module width - Bit 3: Reserved - Bit 4 to 6: Area ID   - 0 = S7‑400   - 1 = S7‑300   - 2 = PROFINET IO (distributed)   - 3 = P-area   - 4 = Q-area   - 5 = IM3-area   - 6 = IM4-area - Bit 7: Reserved - Bit 7: Reserved |  |  |
| res | 5 words | Reserved |  |  |
| * Application Process Instance |  |  |  |  |

##### Partial list with the SZL-IDW#16#0696 for modules on PROFIBUS DP

This results in the error message "sub-module level not present".

#### SZL-ID W#16#xy9C - Tool changeover information (PROFINET IO) (S7-300, S7-400)

##### Purpose

You obtain information on the configured tool changeover and their tools via the partial lists with the SZL-ID W#16#xy9C.

Tool changeover contacts are IO devices that manage tools. A tool can consist of one or several IO devices. Each tool is uniquely assigned to a tool changeover contact port.

In the case of a tool changeover all IO devices that belong to the active tool at the time are deactivated and the IO devices that belong to the new tool are activated. Deactivating and activating take place via the "[D_ACT_DP](#d_act_dp-enabledisable-dp-slaves-s7-300-s7-400)" instruction.

##### Header

The header of the partial list with the SZL-ID W#16#xy9C is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#009C   Information about all tool changeover contacts and their tools on a PROFINET IO system - W#16#019C   Information about all tool changeover contacts on a PROFINET IO system - W#16#029C   Information about a tool changeover contact and its tools - W#16#039C   Information about a tool changeover contact and its IO devices - W#16#0F9C   Only SZL partial header information |
| INDEX | For the partial list extract with the SZL-ID  - W#16#009C: PROFINET IO system ID - W#16#019C: PROFINET IO system ID - W#16#029C: logic address of a tool changeover contact - W#16#039C: logic address of any IO device of a tool - W#16#0F9C: PROFINET IO system ID |
| LENTHDR | W#16#000C (Length of the following data record in byte: 12) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-ID W#16#xy9C has the following structure:

| Contents | Length | Meaning |
| --- | --- | --- |
| StationW | 1 WORD | Station number ( of a data record, could be a tool changeover contact or a tool station) |
| LogAdrW | 1 WORD | - Bits 0 to 14: Address of the module - Bit 15: 0 = input, 1 = output |
| StationWZK | 1 WORD | Station number of a tool head (The tool head is the tool IO device directly connected to the tool changeover contact port.) |
| StationWZW | 1 WORD | Station number of a tool changeover contact |
| SlotWZW | 1 WORD | Slot of a tool changeover contact |
| SubslotWZW | 1 WORD | Submodule slot of a tool changeover contact |

> **Note**
>
> If a tool changeover contact has several ports that manage tools, a data record is supplied for each port.

##### Example

The usage of the individual partial lists is shown once again in the following example.

On the phase of a PROFINET IO system, there are two tool changeover contacts (IOD 3 and IOD 10), whose tools have the following structure:

- Tool changeover contact IOD 3 (IO-Device 3) with the following three tools on the tool changeover contact port 2:

  - Tool 1 (IOD 4, IOD 5 and IOD 6)
  - Tool 2 (IOD 7)
  - Tool 3 (IOD 8 and IOD 9)
- Tool changeover contact IOD 10 with two tool changeover contact ports of which each has two tools

  - Tool changeover contact port 3: Tool 1 (IOD 11 and IOD 12) tool 2 (IOD 13)
  - Tool changeover contact port 4: Tool 1 (IOD 14, IOD 15 and IOD 16), tool 2 (IOD 17 and IOD 18)

The result is the following configuration:

![Example](images/24843046155_DV_resource.Stream@PNG-en-US.png)

The SZL partial lists return the data records for the following IO-Devices:

- Partial list extract with SZL-ID W#16#009C (Index: PROFINET IO system ID): Returns 17 data records for the following IO-Devices:

  - Tool changeover contacts: IOD 3, IOD 10 (for port 3) and IOD 10 (for port 4)
  - Tools: IOD 4, IOD 5, IOD 6, IOD 7, IOD 8, IOD 9, IOD 11, IOD 12, IOD 13, IOD 14, IOD 15, IOD 16, IOD 17 and IOD 18
- Partial list extract with SZL-ID W#16#019C (Index: PROFINET IO system ID): Returns 3 data records for the following IO-Devices:

  - Tool changeover contacts: IOD 3, IOD 10 (for port 3) and IOD 10 (for port 4)
  - Tools: None
- Partial list extract with SZL-ID W#16#029C (Index: Address of IOD 3): Returns 3 data records for the following IO-Devices:

  - Tool changeover contacts: IOD 3
  - Tools: IOD 4, IOD 5, IOD 6, IOD 7, IOD 8 and IOD 9
- Partial list extract with SZL-ID W#16#029C (Index: Address of IOD 10): Returns 10 data records for the following IO-Devices:

  - Tool changeover contacts: IOD 10 (for port 3) and IOD 10 (for port 4)
  - Tools: IOD 11, IOD 12, IOD 13, IOD 14, IOD 15, IOD 16, IOD 17 and IOD 18
- Partial list extract with SZL-ID W#16#039C (Index: Logic address of IOD 4): Returns 3 data records for the following IO-Devices: (This is analog for the logic address of IOD 5 and IOD 6)

  - Tool changeover contacts: None
  - Tools: IOD 4, IOD 5 and IOD 6
- Partial list extract with SZL-ID W#16#039C (Index: Logic address of IOD 13): Returns data record for the following IO-Devices:

  - Tool changeover contacts: None
  - Tools: IOD 13

#### SZL-ID W#16#xyA0 - diagnostic buffer (S7-300, S7-400)

##### Purpose

If you read the partial list with SZL-IDW#16#xyA0 you obtain the entries in the diagnostics buffer of the module.

> **Note**
>
> The S7-300-CPUs return maximum as many data records as the displayed diagnostic buffer entries number in operating mode (default value: 10). The S7-400-CPUs return maximum 21 data records.

##### Header

The header of the partial list with the SZL-IDW#16#xyA0 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | The SZL-ID of the partial list extract  - W#16#00A0: All entries that can be supplied in the currently active  operating mode - W#16#01A0: The most recent entries; you specify the number of most recent entries with the INDEX parameter.   If the number of alarms in the diagnostics buffer is less than the configured maximum number of alarms, the "[RDSYSST](#rdsysst-read-system-status-list-s7-300-s7-400)" instruction may provide invalid values in this partial list extract. You therefore should avoid a non-buffered POWER OFF! - W#16#0FA0: Only SZL partial header information |
| INDEX | Only for SZL-IDW#16#01A0: Number of most recent entries |
| LENTHDR | W#16#0014: One data record is 10 words long (20 bytes) |
| N_DR | Number of data records |

##### Data record

A data record of the partial list with the SZL-IDW#16#xyA0 has the following structure:

| Name | Length in words | Meaning |
| --- | --- | --- |
| ID | 1 word | Event ID |
| info | 5 words | Information about the event and its consequences |
| time | 4 words | Time stamp of the event |

##### Diagnostics buffer

Additional information on events in the diagnostics buffer is available via context-sensitive help for the displayed event.

#### SZL-ID W#16#00B1 - module diagnostic information (S7-300, S7-400)

##### Purpose

If you read the partial list SZL-IDW#16#00B1, you obtain the first 4 diagnostic bytes of a module with diagnostic capability.

##### Header

The header of the partial list with the SZL-IDW#16#00B1 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | W#16#00B1 |
| INDEX | - Bit 0 to 14: Logical base address - Bit 15: 0 = input, 1 = output |
| LENTHDR | W#16#0004: One data record is 2 words long (4 bytes) |
| N_DR | 1 |

##### Data record

A data record of the partial list with the SZL-IDW#16#00B1 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| byte0 | 1 byte | - Bit 0: Module fault/OK (group fault ID) - Bit 1: Internal error - Bit 2: External error - Bit 3: Channel fault - Bit 4: External voltage failed - Bit 5: Front panel connector not plugged in - Bit 6: Module is not configured - Bit 7: Incorrect parameters on module |
| byte1 | 1 byte | - Bit 0 to bit 3: Module class (CPU, FM, CP, IM, SM, ...) - Bit 4: Channel information exists - Bit 5: User information exists - Bit 6: Diagnostic interrupt from substitute - Bit 7: Maintenance requirement (PROFINET IO only) |
| byte2 | 1 byte | - Bit 0: User module is missing or has an error - Bit 1: Communication problem - Bit 2: Operating mode RUN/STOP (0 = RUN, 1 = STOP) - Bit 3: Time monitoring responded (watchdog) - Bit 4: Module internal supply voltage failure - Bit 5: Battery exhausted (BFS) - Bit 6: Entire backup failed - Bit 7: Maintenance request (PROFINET IO only) |
| byte3 | 1 byte | - Bit 0: Expansion unit failure (detected by IM) - Bit 1: Processor failure - Bit 2: EPROM fault - Bit 3: RAM fault - Bit 4: ADC/DAC error - Bit 5: Fuse tripped - Bit 6: Hardware interrupt lost - Bit 7: Reserve (initialized with 0) |

#### SZL-ID W#16#00B2 - diagnostic data record 1 with physical address (S7-300, S7-400)

##### Purpose

If you read the partial list SZL-IDW#16#00B2, you obtain diagnostic data record 1 of a module in a central rack (in other words, not for DP or sub-modules). You specify the module by using the rack and slot number.

##### Header

The header of the partial list with the SZL-IDW#16#00B2 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | W#16#00B2 |
| INDEX | W#16#xxyy:   - xx contains the number of the rack - yy contains the slot number |
| LENTHDR | The length of the data record depends on the module. |
| N_DR | 1 |

##### Data record

The size of a data record of the partial list SZL-IDW#16#00B2 and its contents depend on the particular module. More detailed information in this regard is provided by the respective manual for the module.

#### SZL-ID W#16#00B3 - module diagnostic data with logical base address (S7-300, S7-400)

##### Purpose

If you read the partial list SZL-IDW#16#00B3, you will obtain all diagnostic data of a module. You can also obtain this information for DP and sub-modules. You select the module using its logical base address.

##### Header

The header of the partial list with the SZL-IDW#16#00B3 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | W#16#00B3 |
| INDEX | - Bit 0 to 14: Logical base address - Bit 15: 0 = input, 1 = output |
| LENTHDR | The length of the data record depends on the module. |
| N_DR | 1 |

##### Data record

The size of a data record of a partial list SZL-IDW#16#00B3 and its contents depends on the particular module. More detailed information in this regard is provided by the respective manual for the module.

#### SZL-ID W#16#00B4 - diagnostic data of a DP slave (S7-300, S7-400)

##### Purpose

If you read the partial list SZL-IDW#16#00B4, you will obtain the diagnostic data of a DP slave. This diagnostic data is structured in compliance with EN 50 170 Volume 2, PROFIBUS. You select the module using the diagnostic address you configured.

##### Header

The header of the partial list with the SZL-IDW#16#00B4 is structured as follows:

| Contents | Meaning |
| --- | --- |
| SZL-ID | W#16#00B4 |
| INDEX | Configured diagnostic address of the DP  slave. |
| LENTHDR | Length of a data record. The maximum length is 240 bytes; for standard  slaves, which have a diagnostic data length of more than 240 bytes up to a  maximum of 244 bytes, the first 240 bytes are read and the overflow bit is set  in the data. |
| N_DR | 1 |

##### Data record

A data record of the partial list with the SZL-IDW#16#00B4 has the following structure:

| Name | Length | Meaning |
| --- | --- | --- |
| status1 | 1 byte | Station status1 |
| status2 | 1 byte | Station status2 |
| status3 | 1 byte | Station status3 |
| Station_No | 1 byte | Master station number |
| Vendor_ID_highByte | 1 byte | Vendor ID (high byte) |
| Vendor_ID_lowByte | 1 byte | Vendor ID (low byte) |
| .... | .... | Additional slave-specific diagnostic information |

### OB_RT: Determine OB program runtime (S7-400)

#### Description

With the instruction, you can determine the runtime of individual OBs over different time periods.

> **Note**
>
> The instruction returns the last recorded time values for the required OB, regardless of whether or not this OB is currently being loaded. The data are not reset by deleting or overwriting them but rather only after a warm restart.

#### Parameter

The following table shows the parameters of the instruction "OB_RT":

| Parameters | Declaration | Data type | Memory area | Meaning |
| --- | --- | --- | --- | --- |
| OB_NR | Input | INT | I, Q, M, D, L | OB whose last evaluated times are to be queried. Valid OB numbers are all those in the OB configuration of your CPU, except for OB 121 and OB 122. Synchronous error processing time is included in the time required for processing the OB that has caused the error. Specification of OBs 121 and 122 or OBs that are not implemented in the CPU causes an error message.  For OB_NR=0, the data of the OB in whose context the instruction was called will be transferred. When "OB_RT" is called in OB 121 or OB 122 with OB_NR=0, all time data of the interrupt triggering OB are output, including the time data in OB 12x. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code.  Otherwise, RET_VAL contains the number of the OB for which these data were called. |
| PRIO | Output | INT | I, Q, M, D, L | The priority class of the queried OB is output in PRIO . |
| LAST_RT | Output | DINT | I, Q, M, D, L | Runtime (in microseconds) of the last completed execution of the specified OB. If the OB for which you request the runtimes is currently being processed, the following applies: For the first call of the "OB_RT" instruction during the current execution of the required OB, LAST_RT indicates the run time of the last completed OB execution. With each subsequent call of the "OB_RT" instruction during the current execution of the required OB, LAST_RT  - DW#16#FFFF FFFF indicates, if the required OB has already called an "OB_RT" with OB_NR=0. - The runtime of the last completed OB, if an "OB_RT" call with OB_NR=0 has not occurred in the required OB.   Note: Interruptions caused by OBs with higher priority are not included in LAST_RT . The OB-specific operating system services (such as generation and provision of the OB start information, updating of the process image, updating of the process image partition) are contained in LAST_RT . |
| LAST_ET | Output | DINT | I, Q, M, D, L | Time interval (in microseconds) between the OB call and the end of execution of the specified OB. If the OB for which you want to determine runtimes is currently in process the following applies: For the first call of the "OB_RT" instruction during the current processing of the required OB, the time interval between the last completely executed OB request and the end of processing of the specified OB is specified in LAST_ET . For each subsequent call of the "OB_RT" instruction during current processing of the required OB in LAST_ET  - DW#16#FFFF FFFF indicates, if the required OB has already called an "OB_RT" with OB_NR=0. - The time interval between the last completely executed OB request and the end of execution of the required OB, if an "OB_RT" call with OB_NR=0 has not occurred in the required OB.   Note: Interruptions caused by OBs with higher priority are included in LAST_ET . |
| CUR_T | Output | DINT | I, Q, M, D, L | Timing of the OB request of the specified OB that is currently being processed, as a relative time in microseconds. If the specified OB is currently not being processed, CUR_T will contain the value "0".  Note: The system time is a counter that counts from "0" to "2 147 483 647" microseconds. If an overflow occurs, the counter restarts at "0". |
| CUR_RT | Output | DINT | I, Q, M, D, L | Previous runtime of the current execution of the specified OB in microseconds.CUR_RT is "0", if the OB is not being processed or has not yet been processed. After processing, the runtime is transferred to LAST_RT and CUR_RT is set to zero. Note: Interruptions caused by OBs with higher priority are not included in CUR_RT . The OB-specific operating system services performed until "OB_RT" is called are contained in CUR_RT . |
| CUR_ET | Output | DINT | I, Q, M, D, L | Time elapsed since the request of the specified OB that is currently being processed, in microseconds. CUR_ET is "0", if the specified OB is currently not being processed. After processing, the runtime is transferred to LAST_ET and CUR_ET is set to "0". Note: Interruptions caused by OBs with higher priority are included in CUR_ET . |
| NEXT_ET | Output | DINT | I, Q, M, D, L | If additional calls of the specified OB are queued before the current request has been completed, NEXT_ET indicates the time-to-go between the current time and the time of execution of the next request in microseconds.. NEXT_ET is "0", if no other start event exists besides the start events for this OB that are currently pending or undergoing processing.  WinLC RTX and the S7-400 CPUs do not use this parameter. In these cases, NEXT_ET has the value"FFFF FFFF". Note: Interruptions caused by OBs with higher priority are included in NEXT_ET . |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

The times also include the runtimes for any nested processing of synchronous error interrupts (OB 121, OB 122).

> **Note**
>
> When you declare an OB number in OB_NR that exists in the dynamic project data on your CPU without the OS having called the corresponding OB, or you have not yet downloaded it to the CPU, RET_VAL contains the specified OB number and PRIO contains the configured (default, if required) priority of the specified OB. The runtime parameter (CUR_RT, CUR_ET, LAST_RT, LAST_ET, NEXT_ET) returns the initial value DW#16#FFFF FFFF. For the following restart methods or operating state changes, the runtime parameters are set to their initial value: Warm restart, cold restart, hot restart.

#### Parameter RET_VAL

| Event class error code | Explanation |
| --- | --- |
| 1 to 102 | Number of the OB to which information is being transferred. |
| W#16#8080 | OB_NR parameter contains an illegal value. |
| W#16#8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### C_DIAG: Determine current connection status (S7-400)

#### Description

You use the instruction to determine the current status of all S7 connections and of all fault-tolerant S7 connections (or their partial connections).

Suitable evaluation of these connection data lets you recognize failures of S7 connections as well as of fault-tolerant S7 connections and report these, if necessary, to an operator control and monitoring system. Monitored connections can be a connection between automation systems as well as the connection of an automation system to an operator control and monitoring system.

> **Note**
>
> A change in the operating state of the CPU: RUN -&gt; STOP -&gt;RUN, does not affect the state of the configured connections. Exception: When an H-station changes from the redundant system state to the Stop system state, the partial connections of all fault-tolerant connections to the standby CPU will be disconnected.
>
> After a power failure, on the other hand, all configured connections will be reestablished and this changes the connection status.
>
> When the instruction is called for the first time or after startup, the connection information will differ, depending on whether the last operating mode of the CPU was STOP or POWER OFF.

#### Functional description

The "C_DIAG" instruction functions asynchronously, that is, its execution extends over multiple calls.

You start the job by calling "C_DIAG" with REQ=1.

If the job could be executed immediately, the instruction will return the value "0" at the output parameter BUSY . If BUSY = "1", the job is still active.

#### Call

To recognize the failure of S7 connections and fault-tolerant S7 connections, you call "C_DIAG" in a cyclic interrupt OB that is started, for example, every 10 seconds by the operating system.

Because the status of a connection normally does not change, it is appropriate to copy the connection data to the user program with these cyclic calls only if they have changed since their last call (call with MODE=B#16#02, see below).

The "C_DIAG" instruction has four possible operating modes, which are explained in the following table.

| MODE  (B#16#...) | "C_DIAG" copies connection data to the user program | "C_DIAG" transfers acknowledgement information to the operating system |
| --- | --- | --- |
| 00 | No | Yes |
| 01 | Yes | Yes |
| 02 | - Yes, if connection data have changed - No, if connection data have not changed | Yes |
| 03 | Yes | No |

The status changes of the connection data since the last call of "C_DIAG" (with MODE=B#16#00, 01 or 02) are confirmed by transferring the acknowledgement information to the operating system.

> **Note**
>
> If you operate "C_DIAG" in a cyclic interrupt OB in "Conditional copying" mode (MODE=B#16#02), you must ensure that no initial values are contained in the target range after a cold restart of the CPU. You can achieve this in OB 102 with a single call of "C_DIAG" with "Unconditional copying with acknowledgment" mode (MODE=B#16#01).

#### Parameter

The following table shows the parameters of the instruction "C_DIAG":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request to activate  REQ=1: Initialize the job, if not already started |
| MODE | Input | BYTE | I, Q, M, D, L or constant | Job identifier  Possible values:  - B#16#00: "C_DIAG" does not copy connection data, but merely transfers acknowledgement information to the operating system. - B#16#01: Regardless of the status change, "C_DIAG" copies all connection data to the user program and transfers an acknowledgement information to the operating system. - B#16#02: If connection data have changed, "C_DIAG" will copy them to the user program. If not changed, they are not copied. "In both cases, C_DIAG" transfers an acknowledgement information to the operating system. - B#16#03: "C_DIAG" copies the connection data to the user program, independent of its change status. It does not transfer acknowledgement information to the operating system. |
| RET_VAL | Return | INT | I, Q, M, D, L | Return value (error code or job status) |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1: The job is not yet complete. |
| N_CON | Output | INT | I, Q, M, D, L | Index of the last structure in CON_ARR, with .DIS_PCON or .DIS_CON = TRUE . This means only the first N_CON elements of CON_ARR need to be checked in the user program.  Note: The first structure in the CON_ARR array has the index "1". |
| CON_ARR | Output | ANY | I, Q, M, D, L | Destination area for the read connection data.  Only the BYTE data type is permitted.  A structure is assigned to each connection.  Choose a target range size that can receive all structures even at the maximum number of possible connections for your CPU. This is particularly important after a CPU replacement when the new CPU which has greater connection resources than the previous one. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter CON_ARR

The target range for the read connection data is an array of structures. A structure is assigned to each connection.

Initially, the array does not need to be occupied with valid entries and it may contain invalid entries between two valid entries.

The connections are not sorted by connection reference.

> **Note**
>
> Data consistency of a connection is ensured if you copy connection data from the operating system to the selected target range.

#### Structure organization

| Parameters | Data type | Description |
| --- | --- | --- |
| CON_ID | WORD | Connection reference that you have assigned to this connection during configuration  W#16#FFFF: Invalid ID, which means the connection has not been configured. If CON_ARR[i].DIS_PCON or CON_ARR[i].DIS_CON (see below) is also set, this connection has been reconfigured or deleted since the last call of "C_DIAG". |
| STAT_CON | BYTE | The current status of the S7 connection or fault-tolerant S7 connection  Possible values:  - B#16#00: S7 connection not established - B#16#10: Fault-tolerant S7 connection not established - B#16#01: S7 connection is currently being established - B#16#11: Fault-tolerant S7 connection is currently being established - B#16#02: S7 connection is established - B#16#12: Fault-tolerant S7 connection is established, but is not fault tolerant - B#16#13: Fault-tolerant S7 connection has been established and is fault tolerant |
| PROD_CON | BYTE | Partial connection number of the productive connection  Possible values: 0, 1, 2, 3 |
| STBY_CON | BYTE | Partial connection number of the standby connection (B#16#FF: no standby connection)  Possible values: 0, 1, 2, 3  Note: Only a fault-tolerant S7 connection can have a standby connection. |
| DIS_PCON | BOOL | The transitions W#16#12 -&gt; W#16#13 and W#16#13 -&gt; W#16#12 from CON_ARR[i].STAT_CON since the last instruction call set CON_ARR[i].DIS_PCON to "1". All other status changes of the i connection leave CON_ARR[i].DIS_PCON unchanged.  Note:  - With MODE=B#16#01 and 02 , the operating system bit that corresponds to DIS_PCON is reset when connection data are copied to the target range. - With MODE=B#16#03 , the operating system bit that corresponds to DIS_PCON remains unchanged. |
| DIS_CON | BOOL | Each modification of CON_ARR[i].STAT_CON since the last "C_DIAG" call, with the exception of the transitions W#16#12 -&gt; W#16#13 and W#16#13 -&gt; W#16#12 sets CON_ARR[i].DIS_CON to 1.  Note:  - With MODE=B#16#01 and 02 , the operating system bit that corresponds to "DIS_CON" is reset when connection data are copied to the target range. - With MODE=B#16#03 , the operating system bit that corresponds to DIS_CON remains unchanged. |
| RES0 | BYTE | Reserved (B#16#00) |
| RES1 | BYTE | Reserved (B#16#00) |

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | - MODE=B#16#00, 01 or 02: No connection status change (structure element STAT_CON) since the last call. Job was executed without errors. - MODE=B#16#03: The copy procedure was carried out without errors. |
| 0001 | - MODE=B#16#00, 01 or 02: Connection status change (structure element STAT_CON) with at least one connection since the last call. Job was executed without errors. - MODE=B#16#03: RET_VAL W#16#0001 is not possible: |
| 7000 | First call with REQ=0. The job specified with MODE is not active. BUSY has the value "0". |
| 7001 | First call with REQ=1. The job specified with MODE is not triggered. BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant). The activated job is still running. BUSY has  the value "1". |
| 8080 | The MODE parameter contains an invalid value. |
| 8081 | The CON_ARR parameter contains an illegal data type. |
| 8082 | The length specification in the CON_ARR parameter is too small. The instruction copies no data to the target range. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## Data block functions (S7-300, S7-400)

This section contains information on the following topics:

- [READ_DBL: Read from data block in the load memory (S7-300, S7-400)](#read_dbl-read-from-data-block-in-the-load-memory-s7-300-s7-400)
- [WRIT_DBL: Write to data block in the load memory (S7-300, S7-400)](#writ_dbl-write-to-data-block-in-the-load-memory-s7-300-s7-400)
- [DEL_DB: Delete data block (S7-300, S7-400)](#del_db-delete-data-block-s7-300-s7-400)
- [CREAT_DB: Create data block (S7-300, S7-400)](#creat_db-create-data-block-s7-300-s7-400)
- [CREA_DB: Create data block / retentive (S7-300, S7-400)](#crea_db-create-data-block-retentive-s7-300-s7-400)
- [CREA_DBL: Create data block in the load memory (S7-300, S7-400)](#crea_dbl-create-data-block-in-the-load-memory-s7-300-s7-400)
- [TEST_DB: Test data block (S7-300, S7-400)](#test_db-test-data-block-s7-300-s7-400)

### READ_DBL: Read from data block in the load memory (S7-300, S7-400)

#### Description

With the instruction you copy a DB or an area of a DB in load memory (Micro Memory Card) to the data area of a destination DB. The destination DB must be relevant for execution; that is, it must not be created with the attribute UNLINKED. The content of the load memory is not changed during the copy process.

To ensure data consistency, you must not change the destination area while "READ_DBL" is being executed (which means as long as the BUSY parameter has the value TRUE).

The following restrictions apply to the parameters SRCBLK and DSTBLK:

- For an ANY pointer of the type BOOL, the length must be divisible by 8.
- For an ANY pointer of the type STRING, the length must be equal to 1.

If required, you can determine the length of the source DB with the "[TEST_DB](#test_db-test-data-block-s7-300-s7-400)" instruction.

> **Note**
>
> READ_DBL is processed asynchronously. Therefore, it is not suitable for frequent (or cyclical) reading of tags in the load memory.
>
> Once started, a job is always completed. If the maximum number of simultaneously active "READ_DBL" instructions is reached and you call "READ_DBL" once again at this time in a priority class having higher priority, error code W#16#80C3 will be returned. This means it does not make sense to restart the high-priority job right away.

#### Functional description

The "READ_DBL" instruction works asynchronously, that is, its execution extends over multiple calls. You start the job by calling "READ_DBL" with REQ =1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

#### Parameter

The following table shows the parameters of the instruction "READ_DBL":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Read request |
| SRCBLK | Input | ANY | D | Pointer to data block in the load memory that is to be read from |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The reading process is not yet complete. |
| DSTBLK | Output | ANY | D | Pointer to the data block in the work memory that is to be written to |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| 0081 | The destination area is larger than the source area.  The source area is written completely to the destination area; the remaining bytes of the destination area will not be changed. |
| 7000 | First call with REQ=0: No data transfer active; BUSY has the value "0". |
| 7001 | First call with REQ=1: Data transfer triggered; BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant): Data transfer already active; BUSY has the value "1". |
| 8081 | The source area is larger than the destination area.    **The destination area is fully written. The remaining bytes of the source area are ignored.** |
| 8093 | No data block or a data block that is not in the work memory is specified for the DSTBLK parameter. |
| 80B1 | No data block is specified for the SRCBLK parameter, or the data block specified there is not an object in the load memory (for example, a DB created using "[CREAT_DB](#creat_db-create-data-block-s7-300-s7-400)"). |
| 80B4 | DB with F-attribute must not be read. |
| 80C0 | The destination DB is currently being processed by another instruction or a communication function. |
| 80C3 | The maximum number of simultaneously active "READ_DBL" instructions has already been reached. |
| 827F | Parameter 2 is faulty, possibly an unsupported data type |
| 8xyy | General error codes  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### WRIT_DBL: Write to data block in the load memory (S7-300, S7-400)

#### Description

You use the instruction to transfer the contents of a DB or a DB area from the work memory to a DB or a DB area in the load memory (Micro Memory Card). The source DB must be relevant for execution, which means it must not be created with the attribute UNLINKED. It can, however, have been created with the "CREAT_DB" instruction.

To ensure data consistency, you must not change the source area while "WRIT_DBL" is being executed (which means as long as the BUSY parameter has the value TRUE).

The following restrictions apply to the parameters SRCBLK and DSTBLK:

- For an ANY pointer of the type BOOL , the length must be divisible by 8.
- For an ANY pointer of the type STRING , the length must be equal to 1.

If required, you can determine the length of the destination DB with the "[TEST_DB](#test_db-test-data-block-s7-300-s7-400)" instruction.

"WRIT_DBL" does not change the checksum of the user program if you write a DB that was created using an instruction. However, when a loaded DB is written, the first entry in this DB changes the checksum of the user program.

> **Note**
>
> "WRIT_DBL" is not suitable for frequent (or cyclical) writing of tags in the load memory. This is because the Micro Memory Card technology limits the number of write accesses that can be made to a Micro Memory Card.

#### Functional description

The "WRIT_DBL" instruction works asynchronously, that is, its execution extends over multiple calls. You start the job by calling "WRIT_DBL" with REQ =1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

#### Parameter

The following table shows the parameters of the instruction "WRIT_DBL":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Write request |
| SRCBLK | Input | ANY | D | Pointer to the DB in the work memory that is to be read from |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The writing process is not yet complete. |
| DSTBLK | Output | ANY | D | Pointer to the data block in the load memory that is to be written to. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| 0081 | The destination area is larger than the source area.  The source area is written completely to the destination area. The remaining bytes of the destination area will not be changed. |
| 7000 | First call with REQ=0: No data transfer active; BUSY has the value "0". |
| 7001 | First call with REQ=1: Data transfer triggered; BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant): Data transfer already active; BUSY has the value "1". |
| 8081 | The source area is larger than the destination area.  **The destination area is fully written. The remaining bytes of the source area are ignored.** |
| 8092 | Incorrect operating mode: While "WRIT_DBL" was active, the CPU went into STOP mode. This error code is supplied at the next transition to RUN. Call "WRIT_DBL" again. |
| 8093 | No data block or a data block that is not in the work memory is specified for the SRCBLK parameter. |
| 80B1 | No data block is specified for the DSTBLK parameter, or the data block specified there is not an object in the load memory (for example, a DB created using "[CREAT_DB](#creat_db-create-data-block-s7-300-s7-400)"). |
| 80B4 | DB with F-attribute must not be changed |
| 80C0 | The destination is currently being processed by another instruction or a communication function. Example: You upload a DB from the CPU to the programming device (PG). You want to change the contents of this DB using "WRIT_DBL". |
| 80C3 | The maximum number of simultaneously active "WRIT_DBL" instructions has already been reached. |
| 827F | Parameter 2 is faulty, possibly an unsupported data type |
| 8xyy | General error codes  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### DEL_DB: Delete data block (S7-300, S7-400)

#### Description

You use the instruction to delete a data block located in the work memory and, if present, in the load memory of the CPU. The DB to be deleted must not be open in the current or in any lower priority class, in other words, it must not be entered in either of the two DB registers or in the B stack.

Otherwise, the CPU starts OB 121 when the instruction is called. If OB 121 is not present, the CPU switches to STOP mode. For S7-300 (exception: CPU 318), the DB is deleted without calling OB 121.

> **Note**
>
> It is not advisable to delete instance DBs with "DEL_DB" as this always leads to program errors. Therefore, avoid deleting instance DBs with "DEL_DB".

The following table explains when a DB can be deleted with "DEL_DB".

| If ... | then use "DEL_DB" ... |
| --- | --- |
| the DB was created by calling the "CREAT_DB" instruction, | it can be deleted. |
| was transferred to the CPU and was not created with the attribute "Only store in load memory" | it can be deleted. |
| was created with the attribute "Only store in load memory" | - For S7-300 can be deleted: - For S7-400 cannot be deleted: |
| was created by calling the "CREA_DBL" instruction | can be deleted |
| The DB was stored on the flash card, | it cannot be deleted. |

#### Interrupt ability

The instruction can be interrupted by priority classes of a higher priority. If the instruction is called again there, then this second call will be aborted and W#16#8091 will be entered in RET_VAL .

#### Parameter

The following table shows the parameters of the instruction "DEL_DB":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DB_NUMBER | Input | WORD | I, Q, M, D, L or constant | Number of the DB to be  deleted |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8091 | "DEL_DB" calls were nested and the maximum nesting level of the CPU used was exceeded. |
| 8092 | The "Delete a DB" function cannot be executed currently because  - The "Compress user memory" function is currently active. - You are copying the DB to be deleted from the CPU to an offline project. - The WinAC software CPU has detected an error in the OS of the computer on which WinAC is installed. |
| 80A1 | Error in input parameter DB_NUMBER: the actual parameter selected  - Is "0" - Is greater than the maximum permitted DB number for the CPU used. |
| 80B1 | The DB with the specified number does not exist in the work memory of the CPU. |
| 80B3 | The DB is on a flash card. |
| 80B4 | The DB could not be deleted. Possible causes:  - It belongs to an F-program. - It is an instance DB of a block for S7 communication (for S7-400 only). - It is a technology DB. |
| 80C1 | The "Delete a DB" function cannot be executed at this time due to a temporary resource bottleneck. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### CREAT_DB: Create data block (S7-300, S7-400)

#### Description

You use the instruction to create a data block with no predefined values in the user program. Instead, the DB contains random data. The instruction creates a data block with a number from a specified area and with a predefined size. The instruction assigns the smallest possible number from the specified area to the DB. To create a DB with a specific number, enter the same number for the upper and lower limits of the specified area. You cannot assign the numbers of the DBs already contained in the user program. The length of the DB must be specified with an even number.

#### Interrupt ability

The instruction can be interrupted by higher-priority OBs. If a "CREAT_DB" instruction is called in a higher-priority OB, this call will be rejected with the error code W#16#8091.

#### Parameter

The following table shows the parameters of the instruction "CREAT_DB":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| LOW_LIMIT | Input | WORD | I, Q, M, D, L or constant | The lower limit value is the lowest number in the range of numbers that you can assign to your data block. |
| UP_LIMIT | Input | WORD | I, Q, M, D, L or constant | The upper limit value is the highest number in the range of numbers that you can assign to your data block. |
| COUNT | Input | WORD | I, Q, M, D, L or constant | The count value indicates the number of data bytes that you want to reserve for your data block. You must specify an even number of bytes (maximum 65534). |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| DB_NUMBER | Output | WORD | I, Q, M, D, L | The data block number is the number of the created data block. In case of an error (bit 15 of RET_VAL was set), the value "0" will be entered in DB_NUMBER . |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8091 | You have called CREAT_DB as a nested instruction. |
| 8092 | The "Create a DB" function is currently unavailable because   - The "Compress user memory" function is currently active. - The number of DBs in the CPU has already reached the maximum possible number. - The H-CPU is running link-up or update functions. - The WinAC software CPU has detected an error in the OS of the computer on which WinAC is installed. - The previous Delete is not completed yet |
| 80A1 | Error in the DB number:  - The number is "0" - The number exceeds the CPU-specific DB quantity - Lower limit &gt; upper limit |
| 80A2 | Error in length of DB:  - The length is "0" - The length was specified with an uneven number - The length is greater than the CPU allows |
| 80B1 | There is no DB number free. |
| 80B2 | There is not enough free memory available. |
| 80B3 | There is not enough continuous memory space available (remedy: compress memory!) |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### CREA_DB: Create data block / retentive (S7-300, S7-400)

#### Description

You use the instruction to create a data block with no predefined values in the user program. Instead, the DB contains random data. The instruction creates a data block with a number from a specified area and with a predefined size. The instruction assigns the smallest possible number from the specified area to the DB. To create a DB with a specific number, enter the same number for the upper and lower limits of the specified area. You cannot assign the numbers of the DBs already contained in the user program. The length of the DB must be specified with an even number.

Depending on the selection you have made for the ATTRIB parameter, the DB created has the property RETAIN or NON_RETAIN:

- RETAIN (=retentive) means that the DB is created in the retentive part of the work memory. This means the current values of the DB are retained after each power OFF/power ON transition and every restart (warm restart).
- NON_RETAIN (=non-retentive) means that the DB is created in the non-retentive part of the work memory. This means the current values of the DB are undefined after each power OFF/power ON transition and every restart (warm restart).

If no distinction has been made between retentive and non-retentive work memory, the ATTRIB parameter will be ignored. This means the values of the DB will be retained after each power OFF/power ON transition and every restart (warm restart).

#### Interrupt ability

The "CREA_DB" instruction can be interrupted by higher-priority OBs. If a "CREA_DB" instruction is called in a higher-priority OB, this call will be rejected with the error code W#16#8091 .

#### Parameter

The following table shows the parameters of the instruction "CREA_DB":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| LOW_LIMIT | Input | WORD | I, Q, M, D, L or constant | The lower limit value is the lowest number in the range of numbers that you can assign to your data block. |
| UP_LIMIT | Input | WORD | I, Q, M, D, L or constant | The upper limit value is the highest number in the range of numbers that you can assign to your data block. |
| COUNT | Input | WORD | I, Q, M, D, L or constant | The count value indicates the number of data bytes that you want to reserve for your data block. You must specify an even number of bytes (maximum 65534). |
| ATTRIB | Input | BYTE | I, Q, M, D, L or constant | DB attributes:  - B#16#00: RETAIN - B#16#04: NON_RETAIN |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is  being executed, the return value contains an error code. |
| DB_NUMBER | Output | WORD | I, Q, M, D, L | The data block number is the number of the created data block. In case of an error (bit 15 of RET_VAL was set), the value "0" will be entered in DB_NUMBER . |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8091 | You have called CREA_DB as a nested instruction. |
| 8092 | The "Create a DB" function is currently unavailable because   - The "Compress user memory" function is currently active. - The WinAC software CPU has detected an error in the OS of the computer on which WinAC is installed. |
| 8094 | Invalid value in parameter ATTRIB |
| 80A1 | Error in the DB number:  - The number is "0" - The number exceeds the CPU-specific DB quantity - Lower limit &gt; upper limit |
| 80A2 | Error in length of DB:  - The length is "0" - The length was specified with an uneven number - The length is greater than the CPU allows |
| 80B1 | There is no DB number free. |
| 80B2 | There is not enough free memory available. |
| 80B3 | There is not enough continuous memory space available (remedy: compress memory!) |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### CREA_DBL: Create data block in the load memory (S7-300, S7-400)

#### Description

You use the instruction to create a new data block in the load memory (Micro Memory Card). The instruction creates a data block with a number from a specified area and with a predefined size. The instruction assigns the smallest possible number from the specified area to the DB. To create a DB with a specific number, enter the same number for the upper and lower limits of the range to be specified. You cannot assign the numbers of the DBs already contained in the user program. If a DB with the same number already exists in work memory and/or load memory, or if the DB exists as a copied version, the instruction is terminated and error information is generated.

> **Note**
>
> With the "[TEST_DB](#test_db-test-data-block-s7-300-s7-400)" instruction, you can determine whether a DB with the same number already exists.

The contents of the data area to which the parameter SRCBLK(source block) points are written to the DB. This data area must be a DB or an area from a DB. To ensure data consistency, you must not change this data area while "CREA_DBL" is being executed (which means as long as the BUSY parameter has the value TRUE).

A DB with the READ_ONLY attribute can only be created and initialized using "CREA_DBL".

"CREA_DBL" does not change the checksum of the user program.

#### Functional description

The "CREA_DBL" instruction works asynchronously, that is, its execution extends over multiple calls. You start the job by calling "CREA_DBL" with REQ=1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

#### Parameter

The following table shows the parameters of the instruction "CREA_DBL":

| Parameters | Declaration | Data type | Memory area | Description |  |
| --- | --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Request to create the DB |  |
| LOW_LIMIT | Input | WORD | I, Q, M, D, L | Low limit of the range used by "CREA_DBL" to assign a number to your DB |  |
| UP_LIMIT | Input | WORD | I, Q, M, D, L | Upper limit of the range used by "CREA_DBL" to assign a number to your DB |  |
| COUNT | Input | WORD | I, Q, M, D, L | The count value specifies the quantity of data bytes you want to reserve for your DB. Here you must specify an even number of bytes. |  |
| ATTRIB | Input | BYTE | I, Q, M, D, L | DB properties: |  |
| Bit 0 = 1: | UNLINKED:  The DB exists only in load memory. |  |  |  |  |
| Bit 1 = 1: | READ_ONLY:  The DB is read-only. |  |  |  |  |
| Bit 2 = 1: | NON_RETAIN:  The DB is not retentive. |  |  |  |  |
| Bit 3 to 7: | Reserved |  |  |  |  |
| SRCBLK | Input | ANY | D | Pointer to the data block whose values will be used to initialize the created DB |  |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |  |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = 1: The process is not yet complete. |  |
| DB_NUM | Output | WORD | I, Q, M, D, L | Number of the created DB |  |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| 0081 | The target range is larger than the source range.   The complete source range is written to the target range. The remaining bytes of the target range are filled with 0. |
| 7000 | First call with REQ=0: No data transfer active; BUSY has the value "0". |
| 7001 | First call with REQ=1: Data transfer triggered; BUSY has the value "1". |
| 7002 | Intermediate call (REQ  irrelevant): Data transfer already active; BUSY has the value "1". |
| 8081 | The source range is larger than the target range.    **The complete target range is written. The remaining bytes of the source range are ignored.** |
| 8091 | You have called "CREA_DBL" as a nested instruction. |
| 8092 | The "Create data block" function is currently unavailable because  - The "Compress user memory" function is currently active. - The maximum number of blocks on your CPU has already been reached. |
| 8093 | No data block or a data block that is not in the work memory is specified for the SRCBLK parameter. |
| 8094 | A not yet supported attribute was specified for the ATTRIB parameter. |
| 80A1 | DB number error:  - The number is 0 or is not within the valid range for the CPU (CPU15xx: 60001 to 60999) - The number exceeds the CPU-specific DB quantity - Low limit &gt; high limit |
| 80A2 | DB length error:  - The length is "0" - The length is an odd number - The length is greater than permitted by the CPU |
| 80B1 | No free DB number |
| 80B2 | Insufficient work memory |
| 80BB | Insufficient load memory |
| 80C0 | The destination is currently being processed by another instruction or a communication function. |
| 80C3 | The maximum number of simultaneously active "CREA_DBL" instructions has already been reached. |
| 8xyy | General error codes, for example:  - Source DB does not exist or it is only available as copied version - Source range in DB does not exist   See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### TEST_DB: Test data block (S7-300, S7-400)

#### Description

With the instruction you receive on S7-300 information about a data block that is in the CPU work or load memory, on S7-400 information about a data block that is in the CPU work memory. The instruction determines the number of data bytes in the selected DB and checks whether or not the DB is read only.

#### Parameters

The following table shows the parameters of the instruction "TEST_DB":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DB_NUMBER | Input | WORD | I, Q, M, D, L or constant | Number of the DB to be tested |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| DB_LENGTH | Output | WORD | I, Q, M, D, L | Number of data bytes the selected DB  contains. |
| WRITE_PROT | Output | BOOL | I, Q, M, D, L | Information about the write-protect  identifier of the DB ("1" means read only). |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 80A1 | Error in input parameter DB_NUMBER: the actual parameter selected  - Is "0" - Is greater than the maximum permitted DB number for the CPU used. |
| 80B1 | The DB with the specified number does not exist on the CPU. |
| 80B2 | The DB was created using the keyword UNLINKED. |
| 8xyy | General error information,  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## Table functions (S7-300, S7-400)

This section contains information on the following topics:

- [ATT: Add value to table (S7-300, S7-400)](#att-add-value-to-table-s7-300-s7-400)
- [FIFO: Output first value of the table (S7-300, S7-400)](#fifo-output-first-value-of-the-table-s7-300-s7-400)
- [TBL_FIND: Find value in table (S7-300, S7-400)](#tbl_find-find-value-in-table-s7-300-s7-400)
- [LIFO: Output last value in the table (S7-300, S7-400)](#lifo-output-last-value-in-the-table-s7-300-s7-400)
- [TBL: Execute table instruction (S7-300, S7-400)](#tbl-execute-table-instruction-s7-300-s7-400)
- [TBL_WRD: Copy value from table (S7-300, S7-400)](#tbl_wrd-copy-value-from-table-s7-300-s7-400)
- [WRD_TBL: Link value logically with table element and save (S7-300, S7-400)](#wrd_tbl-link-value-logically-with-table-element-and-save-s7-300-s7-400)
- [DEV: Calculate standard deviation (S7-300, S7-400)](#dev-calculate-standard-deviation-s7-300-s7-400)
- [CDT: Correlated data tables (S7-300, S7-400)](#cdt-correlated-data-tables-s7-300-s7-400)
- [TBL_TBL: Link tables (S7-300, S7-400)](#tbl_tbl-link-tables-s7-300-s7-400)
- [PACK: Collect/distribute table data (S7-300, S7-400)](#pack-collectdistribute-table-data-s7-300-s7-400)

### ATT: Add value to table  (S7-300, S7-400)

#### Description

The instruction supplements the DATA parameter as the next entry in a table and increments the number of entries by one. The table consists of words. You use the instruction to create table entries that are used by "[FIFO](#fifo-output-first-value-of-the-table-s7-300-s7-400)" and "[LIFO](#lifo-output-last-value-in-the-table-s7-300-s7-400)".

- The first entry in a "[FIFO](#fifo-output-first-value-of-the-table-s7-300-s7-400)" or "[LIFO](#lifo-output-last-value-in-the-table-s7-300-s7-400)" table specifies the maximum length of the table.
- The second entry in the table specifies the number of existing entries.
- The third entry in the table contains the first word of data.

  > **Note**
  >
  > When you create the table, initialize the first two entries.

#### Parameter

The following table shows the parameters of the instruction "ATT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DATA | Input | WORD | I, Q, M, D, L, P or constant | Data to be entered in the table. |
| TABLE | Input | *Pointer | I, Q, M, D | Points to the start address of the "FIFO" or "LIFO" table. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

If the number of entries is equal to or greater than the table length, the data will not be added to the table and the signal state of "BR" is set to "0".

#### Example (LAD)

The "ATT" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, DATA is added as the fifth entry in the table and the number of entries is increased from 4 to 5.

If the "ATT" instruction is executed without errors, the signal states of "ENO" and Q 0.0 will be set to "1".

![Example (LAD)](images/18051187595_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW10 = W#16#0006 |
| Number of entries | DBW12 = W#16#0004  DBW14 = W#16#0012  DBW16 = W#16#0029  DBW18 = W#16#0090  DBW20 = W#16#0002  DBW22 = W#16#0000  DBW24 = W#16#0000 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW10 = W#16#0006 |
| Number of entries | DBW12 = W#16#0005  DBW14 = W#16#0012  DBW16 = W#16#0029  DBW18 = W#16#0090  DBW20 = W#16#0002  DBW22 = W#16#0024  DBW24 = W#16#0000 |

### FIFO: Output first value of the table (S7-300, S7-400)

#### Description

The instruction outputs the oldest entry of the "FIFO" table as function value. The number of entries is decremented by one. If there are still entries in the table, these are shifted down. The "FIFO" table consists of words. Use [ATT](#att-add-value-to-table-s7-300-s7-400) to enter values in the "FIFO" table.

- The first entry in the table specifies the maximum length of the table.
- The second entry in the table specifies the number of existing entries.
- The third entry in the table contains the first word of data.

#### Parameter

The following table shows the parameters of the instruction "FIFO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| TABLE | Input | *Pointer | I, Q, M, D | Points to the start address of the "FIFO" table. |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | The oldest entry from the "FIFO" table. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If the "FIFO" table is empty (number of entries = 0), then RET_VAL will remain the same and the signal state of "BR / ENO" will be set to "0".

#### Example (LAD)

"FIFO" is executed if the signal state at input I 0.0 is 1 (activated). In this example, the oldest entry in the table is returned as the function value (MW 2.0). The number of entries is decremented from 5 to 4, and the remaining entries are shifted down in the table.

If "FIFO" is executed without errors, then the signal states of "BR / ENO" and Q 0.0 will be set to "1".

![Example (LAD)](images/18051712651_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW10 = W#16#0006 |
| Number of entries | DBW12 = W#16#0005  DBW14 = W#16#0012  DBW16 = W#16#0029  DBW18 = W#16#0090  DBW20 = W#16#0002  DBW22 = W#16#0024  DBW24 = W#16#0000 |
| RET_VAL | MW2 = W#16#0000 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW10 = W#16#0006 |
| Number of entries | DBW12 = W#16#0004  DBW14 = W#16#0029  DBW16 = W#16#0090  DBW18 = W#16#0002  DBW20 = W#16#0024  DBW22 = W#16#0024  DBW24 = W#16#0000 |
| RET_VAL | MW2 = W#16#0012 |

### TBL_FIND: Find value in table (S7-300, S7-400)

#### Description

You use the instruction to search the memory for patterns. The "TBL_FIND" instruction performs a comparison (CMD parameter) between the source pattern (PATRN parameter) and the entries in the source table (SRC parameter). Starting at the entry specified by the INDX parameter, the instruction searches for the next entry in the table that matches the comparison criteria. The number of the entry is stored in the INDX parameter. If no match is found, the "INDX parameter will point beyond the end of the table and the output of the "TBL_FIND" instruction will be deactivated.

- If CMD = 1, then the "TBL_FIND" instruction searches for the first value that corresponds to the value at the PATRN parameter.
- If CMD = 2, then the "TBL_FIND" instruction searches for the first value that does not correspond to the value at the PATRN parameter.
- The first entry in the table contains the maximum length of the table.
- The second entry in the table contains the first table value.

  > **Note**
  >
  > Make sure that you initialize the first entry (table length) of the table.

#### Parameter

The following table shows the parameters of the instruction "TBL_FIND":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC | Input | *Pointer | I, Q, M, D | Points to the start address of the table. |
| PATRN | Input | *Pointer | I, Q, M, D | Points to the pattern to be searched for. |
| CMD | Input | BYTE | I, Q, M, D, L, P | Specifies the command:  - B#16#01 = equal to - B#16#02 = unequal to |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries:  B#16#02 = BYTE  B#16#04= WORD  B#16#05=INT  B#16#06=DWORD  B#16#07=DINT  B#16#08=REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| INDX | InOut | WORD | I, Q, M, D, L | Table index that provides the following information:  - Input: Number of the entry at which the search starts. - Output: Number of the entry that matches the specified pattern. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following conditions occur, the table values are not changed. The signal state of "BR / ENO" will be set to "0" and the return value will be set accordingly:

| RET_VAL | Explanation |
| --- | --- |
| W#16#0007 | The value of the INDX parameter is higher than the value of the table length. |
| W#16#0008 | No match was found. |
| W#16#0009 | The E_TYPE and/or CMD parameter(s) is/are invalid. |

#### Example (LAD)

The "TBL_FIND" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, because the E_TYPE parameter = "4", data in the table is stored in words, starting at the address pointed to by the SRC parameter. These words are compared with the pattern "5555", which is stored at the address specified by the PATRN parameter. Because CMD = 1, the instruction searches for the first value in the SRC parameter that matches the pattern. The INDX parameter points to the address where the search should begin. After the instruction executes, the INDX parameter specifies the entry number in the table where a match for the pattern was found.

If the "TBL_FIND" instruction is executed without errors, then the signal states of ENO and Q 0.0 will be set to "1", and RET_VAL is set to the value W#16#0000.

The "MOVE" instruction is simply used to reset the value of "MW2" in each cycle.

![Example (LAD)](images/18051752075_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

|  |  |  |
| --- | --- | --- |
| SRC (table length) | DBW0 = W#16#0004  DBW2 = W#16#1111  DBW4 = W#16#3333  DBW6 = W#16#5555  DBW8 = W#16#7777 | The first table entry specifies the length of the find instruction. The value 0004 specifies that the next four entries will be searched. |
| INDX | MW2 = W#16#0000 | INDX is transferred from DW0 (before execution) to DW6 (after execution) because the pattern of DW6 matches the pattern 5555 of PATRN . |
| PATRN | DBW10 = W#16#5555 |  |

**After processing:**

|  |  |  |
| --- | --- | --- |
| INDX | MW2 = W#16#0003 |  |

### LIFO: Output last value in the table (S7-300, S7-400)

#### Description

The instruction outputs the most recent entry of the "LIFO" table as function value. The number of entries is decremented by one. The "LIFO" table consists of words. You can use the [ATT](#att-add-value-to-table-s7-300-s7-400) instruction to enter values in the "LIFO" table.

- The first entry in the table specifies the maximum number of entries in the table (table length).
- The second entry in the table specifies the number of existing entries.
- The third entry in the table contains the first word of data.

#### Parameter

The following table shows the parameters of the instruction "LIFO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| TABLE | Input | *Pointer | I, Q, M, D | Points to the start address of the "LIFO" table. |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | The most recent entry from the "LIFO" table. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If the "LIFO" table is empty (number of entries = 0), then RET_VAL will remain the same and the signal state of "BR / ENO" will be set to "0".

#### Example (LAD)

The "LIFO" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, the most recent entry in the "LIFO" table is returned as the function value (MW 2.0). The number of entries is decremented from 5 to 4.

If "LIFO" is executed without errors, then the signal states of "ENO" and Q 0.0 will be set to "1".

![Example (LAD)](images/18051881483_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW10 = W#16#0006 |
| Number of entries | DBW12 = W#16#0005  DBW14 = W#16#0012  DBW16 = W#16#0029  DBW18 = W#16#0090  DBW20 = W#16#0002  DBW22 = W#16#0024  DBW24 = W#16#0000 |
| RET_VAL | MW2 = W#16#0000 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW10 = W#16#0006 |
| Number of entries | DBW12 = W#16#0004  DBW14 = W#16#0012  DBW16 = W#16#0029  DBW18 = W#16#0090  DBW20 = W#16#0002  DBW22 = W#16#0024  DBW24 = W#16#0000 |
| RET_VAL | MW2 = W#16#0024 |

### TBL: Execute table instruction (S7-300, S7-400)

#### Description

The instruction executes the specified instruction (CMD parameter) with the source table and writes the result to the same entry in the table.

- The first entry in the table specifies the maximum number of entries in the table (table length).
- The second entry in the table contains the first table value.
- If the E_TYPE parameter is set to REAL , the CMD value for ones complement is invalid.

  > **Note**
  >
  > Initialize the first entry when you create the table.

#### Parameter

The following table shows the parameters of the instruction "TBL":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC | Input | *Pointer | I, Q, M, D | Points to the start address of the table. |
| CMD | Input | BYTE | I, Q, M, D, L, P | Specifies the instruction to be executed. The following instructions are valid:  B#16#03 = Ones complement  B#16#04 = Delete  B#16#05 = Negate  B#16#06 = Square root |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries. The following data types are valid:  B#16#04 = WORD  B#16#05 = INT  B#16#06 = DWORD  B#16#07 = DINT  B#16#08 = REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If the CMD parameter or the E_TYPE parameter is invalid, and/or if the CMD parameter and the E_TYPE parameter do not match, then the values in the table will remain the same. The signal state of BR / ENO is set to "0" and RET_VAL will be set to the value W#16#0008 .

#### Example (LAD)

The "TBL" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, the SRC parameter points to the address in the data block that will be processed by the instruction. Because the E_TYPE parameter is 4, data in the table will be stored in words starting at the address specified by the SRC parameter. Because CMD is 4 (clear), all the words in the table will be cleared (set to "0") when the "TBL" instruction executes. The table length value of "5" in the first table entry causes the next five table entries to be cleared.

If the "TBL" instruction is executed without error, the signal states of ENO and Q 0.0 will be set to "1", and RET_VAL will be set to the value W#16#0000.

![Example (LAD)](images/18051958923_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| SRC (table length) | DBW0 = W#16#0005  DBW2 = W#16#2000  DBW4 = W#16#3000  DBW6 = W#16#4000  DBW8 = W#16#5000  DBW10 = W#16#6000 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| SRC (table length) | DBW0 = W#16#0005  DBW2 = W#16#0000  DBW4 = W#16#0000  DBW6 = W#16#0000  DBW8 = W#16#0000  DBW10 = W#16#0000 |

### TBL_WRD: Copy value from table  (S7-300, S7-400)

#### Description

The instruction "TBL_WRD" (copy value from table) copies the entry specified by the INDX parameter from the SRC table to the DEST output. The value of INDX will be incremented if the value is less than the maximum length specified in the first word of the (SRC[0]) table. If the INDX parameter specifies the last table entry, then the output bit will be set to "0" after execution.

- The first entry in the table specifies the maximum number of entries in the table (table length).
- The second entry in the table contains the first table value.

  > **Note**
  >
  > Initialize the first entry when you create the table.

#### Parameter

The following table shows the parameters of the instruction "TBL_WRD":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC | Input | *Pointer | I, Q, M, D | Points to the start address of the table. |
| DEST | Input | *Pointer | I, Q, M, D | Points to the start address of the destination. |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries. The following data types are valid:  - B#16#04 = WORD - B#16#05 = INT - B#16#06 = DWORD - B#16#07 = DINT - B#16#08 = REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| Q | Output | BOOL | Q, M, D, L | Returns the value "0" if the INDX variable contains the last value of the table while calling "TBL_WRD". |
| INDX | InOut | WORD | I, Q, M, L | Number of the entry to be copied. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following conditions occur, "TBL_WRD" will not be executed. The signal state of ENO is set to "0" and the return value will be set accordingly:

| RET_VAL | Explanation |
| --- | --- |
| W#16#0007 | The index is "0". |
| W#16#0008 | E_TYPE is invalid. |
| W#16#0009 | The index is outside the range of the table. |

#### Example

"TBL_WRD" is executed if the signal state at input I 0.0 is 1 (activated). In this example, because E_TYPE = 4 the data word stored in the table entry referenced by SRC is copied to the entry referenced by DEST. The value of INDX points to the table entry to be copied. After "TBL_WRD" executes, the value of INDX is automatically incremented by one entry. If the content of INDX is not the last table entry when "TBL_WRD" is called, output ENO is set to "1" after execution.

If "TBL_WRD" is executed without errors, then the signal states of ENO will be set to "1" and RET_VAL will be set to W#16#0000.

![Example](images/20976344331_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| SRC(table length) | DBW0 = W#16#0004  DBW2 = W#16#2000  DBW4 = W#16#3000  DBW6 = W#16#4000  DBW8 = W#16#5000 |
| INDX | MW1 = W#16#0001 |
| DEST | DBW20 = W#16#0000 |

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| INDX | MW1 = W#16#0002 |
| DEST | DBW20 = W#16#2000 |

### WRD_TBL: Link value logically with table element and save  (S7-300, S7-400)

#### Description

The instruction executes the specified instruction (CMD parameter) with the source item and the entry in the table referenced by the INDX parameter. The instruction executes only as long as the INDX parameter is less than the length of the table stored in the first word of the table.

- The first entry in the table specifies the maximum number of entries in the table (table length).
- The second entry in the table contains the first table value.
- If the data type specified by the E_TYPE parameter is REAL, then the CMD parameter can only be "Transfer".

  > **Note**
  >
  > Initialize the first entry when you create the table.

#### Parameter

The following table shows the parameters of the instruction "WRD_TBL":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC | Input | *Pointer | I, Q, M, D | Points to the source data |
| TABLE | Input | *Pointer | I, Q, M, D | Points to the start of the table. |
| CMD | Input | BYTE | I, Q, M, D, L, P | Indicates the instruction to be executed. The following instructions are valid:  B#16#0E = Transfer  B#16#07 = AND logic operation  B#16#08 = OR logic operation  B#16#09 = EXCLUSIVE OR logic operation |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries. The following data types are valid:  B#16#04 = WORD  B#16#05 = INT  B#16#06 = DWORD  B#16#07 = DINT  B#16#08 = REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns a value W#16#0000 if the instruction executes without errors. |
| Q | Output | BOOL | Q, M, D, L | Is set to "0" if the tag at the INDX parameter contains the number of the last entry in the table. |
| INDX | InOut | WORD | I, Q, M, D, L | Number of the entry on which the instruction will be executed. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following conditions occur, then the "WRD_TBL" instruction will not be executed. The signal state of ENO is set to "0" and the return value will be set accordingly:

| RET_VAL | Explanation |
| --- | --- |
| W#16#0007 | The index is 0. |
| W#16#0008 | CMD parameter or E_TYPE parameter is invalid or CMD parameter and E_TYPE parameter do not match. |
| W#16#0009 | The index is outside the range of the table. |

#### Example (LAD)

The "WRD_TBL" instruction will be executed if the signal state at input I 0.0 is 1 (activated). Because the E_TYPE parameter in this example is "6", the double word of the data in the table is saved at the address specified by TABLE . The first word in the table indicates that the table contains three double words. The INDX value points to the table entry that is to be modified. Because CMD is 8, the instruction performs an OR operation with the value to which the INDX parameter points. Because INDX is 2, the second double word (66665544) is ORed with the value to which the SRC parameter (11111111) points. After the instruction executes, the result of the OR operation (77775555) is written back to the table, and the value of INDX will be automatically incremented by one entry. If the INDX parameter points to the last table entry, the "Q" output bit is set to "0" after execution of the instruction. In this example, the value of INDX is not set to the last entry in this table and the "Q" output is therefore set to "1" after execution.

If the "WRD_TBL" instruction is executed without errors, then the signal states of ENO and Q 0.0 will be set to "1", and RET_VAL is set to the value W#16#0000.

![Example (LAD)](images/18052075147_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| SRC | DBD20 = DW#16#11111111 |
| TABLE (table length) | DBW0 = W#16#0003  DBD2 = DW#16#99998877  DBD6 = DW#16#66665544  DBD10 = DW#16#33332222 |
| INDX | MW1 = W#16#0002 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE (table length) | DBW0 = W#16#0003  DBD2 = DW#16#99998877  DBD6 = DW#16#77775555  DBD10 = DW#16#33332222 |
| INDX | MW1 = W#16#0003 |

### DEV: Calculate standard deviation (S7-300, S7-400)

#### Description

The instruction calculates the standard deviation of a group of values stored in a table ("[TBL](#tbl-execute-table-instruction-s7-300-s7-400)" instruction). The result will be stored in OUT . The standard deviation is calculated according to the following formula:

![Description](images/18052152203_DV_resource.Stream@PNG-en-US.png)

Where:

- Sum = the sum of the values in the "[TBL](#tbl-execute-table-instruction-s7-300-s7-400)" instruction
- N = the number of the values in the "[TBL](#tbl-execute-table-instruction-s7-300-s7-400)" instruction
- Sqsum = the sum of all values in the "[TBL](#tbl-execute-table-instruction-s7-300-s7-400)" instruction squared

All calculations use IEEE floating point values, with any necessary type conversions being done automatically by the "DEV" instruction.

- The first entry in the table contains the number of entries in the table (table length).
- The second entry in the table contains the first table value.
- The size of the table entries and the calculated value (OUT parameter) are specified by the E_TYPE parameter.

#### Parameter

The following table shows the parameters of the instruction "DEV":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| TBL | Input | *Pointer | I, Q, M, D | **Points to the start address of a table of values. |
| OUT | Input | *Pointer | I, Q, M, D | **Points to the address of the computed standard deviation value. |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries. The following data types are valid:  B#16#05 = INT  B#16#07 = DINT  B#16#08 = REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| * Double word pointer format for area-crossing register indirect addressing ** Source and destination block must be identical |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following conditions occur, then the "DEV" instruction will not be executed. The signal state of BR / ENO will be set to "0" and the return value will be set accordingly:

| RET_VAL | Explanation |
| --- | --- |
| W#16#0001 | Invalid memory type for a parameter of "DEV". |
| W#16#0002 | The E_TYPE parameter is invalid. |
| W#16#0004 | The table length is zero. |

#### Example (LAD)

The "DEV" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, there are five table values. This specifies the first word in the table. The table values are of the REAL data type. This fact is indicated by the E_TYPE parameter.

If "DEV" is executed without errors, then the signal states of ENO and Q 0.0 will be set to "1", and RET_VAL will be set to "W#16#0000".

![Example (LAD)](images/18052310155_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| TBL (table length) | DBW100 = W#16#0005  DBD102 = 2.0  DBD106 = 4.0  DBD110 = 8.0  DBD114 = 16.0  DBD118 = 32.0 |
| OUT | DBD130 = 0.0 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| OUT | DBD130 = 12.19836055 |

### CDT: Correlated data tables (S7-300, S7-400)

#### Description

The instruction compares an input value (IN parameter) with an existing table of input values (IN_TBL parameter) and locates the first value that is greater than or equal to the input value. Based on its index, the located value is then used to copy the corresponding output value (OUT parameter) to the table of output values (OUT_TBL parameter).

- The values in the input table must be sorted in ascending order. This means that the lowest value is in the first table entry, the highest value is in the last table entry.
- The size of the input value, the table values and output values are defined by the E_TYPE parameter.
- The first entry in the table contains the number of entries of the table (table length).
- The second entry in the table contains the first table value.
- The number of elements in both tables must be identical and be greater than zero.

  > **Note**
  >
  > Initialize the first entry when you create each table.

#### Parameter

The following table shows the parameters of the instruction "CDT":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN_TBL | Input | *Pointer | I, Q, M, D | Points to the start of the input table. |
| OUT_TBL | Input | *Pointer | I, Q, M, D | Points to the start of the output table. |
| IN | Input | *Pointer | I, Q, M, D | Points to the input table. |
| OUT | Input | *Pointer | I, Q, M, D | Points to the output table. |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries. The following data types are valid:  B#16#05 = INT  B#16#07 = DINT  B#16#08 = REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following conditions occur, CDT will not be executed. The signal state of BR / ENO will be set to "0" and the return value will be set accordingly:

| RET_VAL | Explanation |
| --- | --- |
| W#16#0001 | Invalid memory type specified for a parameter of CDT . |
| W#16#0002 | The E_TYPE parameter is invalid. |
| W#16#0003 | The input and output table lengths do not match. |
| W#16#0004 | The table length is zero. |
| W#16#0007 | No value in the IN_TBL parameter is greater than or equal to the input value. |

#### Example (LAD)

The "CDT" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, the IN_TBL parameter and the OUT_TBL parameter each have five table entries. This is specified by the first word of the respective table. The data type of the table values is INTEGER. This fact is indicated by the E_TYPE parameter. The value of the IN parameter is 22. The value of the IN_TBL parameter that is greater than or equal to "22" is "64" which has an index of "5". The corresponding value in OUT_TBL is "25". The value "25" is therefore written in the OUT parameter.

If the "CDT" instruction is executed without errors, then the signal states of ENO and Q 0.0 will be set to "1" and RET_VAL will be set to W#16#0000 .

![Example (LAD)](images/18052375307_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| IN_TBL (table length) | DBW0 = W#16#0005  DBW2 = 2  DBW4 = 4  DBW6 = 8  DBW8 = 16  DBW10 = 64 |
| OUT_TBL (table length) | DBW100 = W#16#0005  DBW102 = 5  DBW104 = 10  DBW106 = 15  DBW108 = 20  DBW110 = 25 |
| IN | DBW200 = 22 |
| OUT | DBW210 = 0 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| OUT | DBW210 = 25 |

### TBL_TBL: Link tables (S7-300, S7-400)

#### Description

The instruction executes the command specified at the CMD parameter with the corresponding entries of the two source tables (parameters TBL1 and TBL2) and writes the result in the corresponding entries of the destination table (DEST_TBL).

- The data types INT, DINT and REAL are only valid for math instructions.
- The first entry in the table contains the number of entries of the table (table length).
- The number of entries in all of the tables must be the same and be greater than zero.

  > **Note**
  >
  > Initialize the first entry when you create each table.

#### Parameter

The following table shows the parameters of the instruction "TBL_TBL":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| TBL1 | Input | *Pointer | I, Q, M, D | Points to the start of the first source table. |
| TBL2 | Input | *Pointer | I, Q, M, D | Points to the start of the second source table. |
| DEST_TBL | Input | *Pointer | I, Q, M, D | Points to the start of the destination table. |
| CMD | Input | BYTE | I, Q, M, D, L, P | Specifies the command to be performed. The following commands are valid:  B#16#07 = AND logic operation  B#16#08= OR logic operation  B#16#09 = EXCLUSIVE OR logic operation  B#16#0a = Add  B#16#0b = Subtract  B#16#0c = Multiply  B#16#0d = Divide |
| E_TYPE | Input | BYTE | I, Q, M, D, L, P | Specifies the data type of the table entries. The following data types are valid:  B#16#04 = WORD  B#16#05 = INT  B#16#06 = DWORD  B#16#07 = DINT  B#16#08 = REAL |
| RET_VAL | Return | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following conditions occur, then the "TBL_TBL" instruction will not be executed. The signal state of BR / ENO will be set to "0" and the return value will be set accordingly:

| RET_VAL | Explanation |
| --- | --- |
| W#16#0001 | An invalid memory area was specified for a parameter of the "TBL_TBL" instruction. |
| W#16#0002 | The E_TYPE parameter is invalid. |
| W#16#0003 | The input and output table lengths do not match. |
| W#16#0004 | The table length is zero. |
| W#16#0005 | The parameters E_TYPE and CMD do not match. |
| W#16#0006 | The CMD parameter is invalid. |

#### Example (LAD)

The "TBL_TBL" instruction is executed if the signal state at input I 0.0 is 1 (activated). In this example, each of the tables has three table entries. This is specified by the first word of the respective table. The data type of the table values is WORD. E_TYPE specifies this. CMD specifies the command with which TBL1 and TBL2 are to be linked.

If the "TBL_TBL" instruction is executed without errors, then the signal states of ENO and Q 0.0 are set to "1", and RET_VAL is set to the value W#16#0000.

![Example (LAD)](images/18052490379_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| TBL1 (table length) | DBW0 = W#16#0003  DBW2 = W#16#00FF  DBW4 = W#16#FF00  DBW6 = W#16#FFFF |
| TBL2 (table length) | DBW20 = W#16#0003  DBW22 = W#16#1111  DBW24 = W#16#2222  DBW26 = W#16#3333 |
| DEST_TBL (table length) | DBW40 = W#16#0003  DBW42 = W#16#0000  DBW44 = W#16#0000  DBW46 = W#16#0000 |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| DST_TBL (table length) | DBW40 = W#16#0003  DBW42 = W#16#0011  DBW44 = W#16#2200  DBW46 = W#16#3333 |

### PACK: Collect/distribute table data (S7-300, S7-400)

#### Description

The instruction transfers data located between any addresses and a table. The direction of transfer is specified by the DIR parameter. Each operation of the PACK instruction processes up to five blocks with data (P_DATA1 to P_DATA5). If the DIR parameter has the value "to", the PACK instruction transfers data from the addresses to the specified table. If the DIR parameter has the value "from", data is distributed from the table to the specified addresses.

The rules for transferring data "to" a table are as follows:

- Single bits (BOOL) are transferred to the next available bit in the table.
- 8-bit data types are transferred to the next available byte in the table. When a byte is written to the table, unused bits in the previous byte are filled with zeros.
- 16- and 32-bit data types are transferred to the next available word in the table. When a word is written to the table, unused bits in the previous word are filled with zeros.

The rules for transferring data "from” a table are as follows:

- Sections of a table cannot be skipped.
- All specified data of the BOOL type will be transferred from the table.
- 8-bit data types are transferred to the first available byte in the table. Unused bits in the previous byte of the table are not included in the byte that is transferred from the table.
- 16- and 32-bit data types are transferred from the first available word in the table. Unused bits in the previous word of the table are not included in the a word that is transferred from the table.

The following data types are valid for the ANY pointer and are supported by "PACK": BOOL, WORD, INT, BYTE, DINT, REAL, CHAR, DWORD.

#### Parameter

The following table shows the parameters of the instruction "PACK":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| TABLE | Input | *Pointer | I, Q, M, D | Points to the start of the table. |
| P_DATA1 | Input | ANY | I, Q, M, D | Points to the start of the block whose data will be transferred. |
| P_DATA2 | Input | ANY | I, Q, M, D | Points to the start of the block whose data will be transferred. |
| P_DATA3 | Input | ANY | I, Q, M, D | Points to the start of the block whose data will be transferred. |
| P_DATA4 | Input | ANY | I, Q, M, D | Points to the start of the block whose data will be transferred. |
| P_DATA5 | Input | ANY | I, Q, M, D | Points to the start of the block whose data will be transferred. |
| ERR_CODE | Output | WORD | I, Q, M, D, L, P | Returns the value W#16#0000 if the operation executes without errors. |
| DIR | Static | BOOL | I, Q, M, D, L | Direction of transfer. The following signal states are possible: 0=to, 1=from. |
| * Pointer in double-word format for area-crossing, indirect register addressing |  |  |  |  |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

If any of the following error conditions occurs, then the "PACK" instruction will not be executed. The signal state of BR / ENO will be set to "0" and ERR_CODE will be set accordingly:

| ERR_CODE | Explanation |
| --- | --- |
| W#16#0001 | An invalid memory area was specified for a parameter of the "PACK" instruction. |
| W#16#0002 | The "E_TYPE" instruction is invalid. |

#### Example (LAD)

"PACK" is executed if the signal state at input I 0.0 is 1 (activated). In this example, there are four blocks with data being transferred "to" the table.

If "PACK" is executed without errors, then the signal states of ENO and Q 0.0 will be set to "1", and ERR_CODE will be set to "W#16#0000".

> **Note**
>
> You can initialize static parameters with the Data Block Editor.

![Example (LAD)](images/18052554251_DV_resource.Stream@PNG-en-US.png)

**Before processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE | DBB0 = B#16#00  DBB1 = B#16#00  DBB2 = B#16#00  DBB3 = B#16#00  DBB4 = B#16#00  DBB5 = B#16#00 |
| P_DATA1 | M 200.0 = TRUE  M 200.1 = TRUE |
| P_DATA2 | MB210 = B#16#FF |
| P_DATA3 | M 300.0 = TRUE  M 300.1 = TRUE |
| P_DATA4 | MW330 = W#16#FFFF |
| Instance DB PACK_DB |  |
| DIR | DBX58.0 = FALSE |

**After processing:**

| Symbol | Meaning |
| --- | --- |
| TABLE | DBB0 = B#16#03  DBB1 = B#16#FF  DBB2 = B#16#03  DBB3 = B#16#00  DBB4 = B#16#FF  DBB5 = B#16#FF |

## Addressing (S7-300, S7-400)

This section contains information on the following topics:

- [GEO_LOG: Determine start address of a module (S7-300, S7-400)](#geo_log-determine-start-address-of-a-module-s7-300-s7-400)
- [LOG_GEO: Determine the slot belonging to a logical address (S7-300, S7-400)](#log_geo-determine-the-slot-belonging-to-a-logical-address-s7-300-s7-400)
- [RD_LGADR: Determine all logical addresses of a module (S7-300, S7-400)](#rd_lgadr-determine-all-logical-addresses-of-a-module-s7-300-s7-400)
- [GADR_LGC: Query logical start address of a module (S7-300, S7-400)](#gadr_lgc-query-logical-start-address-of-a-module-s7-300-s7-400)
- [LGC_GADR: Determine the slot belonging to a logical address (S7-300, S7-400)](#lgc_gadr-determine-the-slot-belonging-to-a-logical-address-s7-300-s7-400)

### GEO_LOG: Determine start address of a module (S7-300, S7-400)

#### Description

The associated module slot of the module is known from the channel of a signal module. With the "GEO_LOG" you determine the associated start address of the module, which means the smallest I or O address.

If you use the "GEO_LOG" instruction on power modules or modules with packed addresses (ET 200S), then the diagnostics address will be returned.

#### Parameter

The following table shows the parameters of the instruction "GEO_LOG":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MASTER | Input | INT | I, Q, M, D, L or constant | Area ID:  - 0, if the slot in a centralized configuration is located in: Rack 0 to 3 (for S7-300) or 0 to 21 (for S7-400) - 1 to 32: DP master system ID of the associated field device if the slot is located in a field device on PROFIBUS - 100 to 115: PROFINET IO system ID of the associated field device if the slot is located in a field device on PROFINET |
| STATION | Input | INT | I, Q, M, D, L or constant | - Number of the rack if the area identifier = 0. - Device number of field device if area ID&gt; 0 |
| SLOT | Input | INT | I, Q, M, D, L or constant | Slot no. |
| SUBSLOT | Input | INT | I, Q, M, D, L or constant | Sub-module slot (if no sub-module can be inserted, 0 must be entered here) |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| LADDR | Output | WORD | I, Q, M, D, L | Start address of the module  Bit 15 of LADDR indicates whether an input address (bit 15 = 0) or an output address (bit 15 = 1) will be present. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8094 | No subnet was configured with the specified SUBNETID . |
| 8095 | Illegal value for STATION parameter |
| 8096 | Illegal value for SLOT parameter |
| 8097 | Illegal value for SUBSLOT parameter |
| 8099 | The slot is not configured. |
| 809A | The interface module address is not configured for the selected slot. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### LOG_GEO: Determine the slot belonging to a logical address (S7-300, S7-400)

#### Description

With the instruction you determine the module slot as well as the offset in the user data address space belonging to a logical address.

#### Parameter

The following table shows the parameters of the instruction "LOG_GEO":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Any logical address of the module  In bit 15 you indicate whether an input address (bit 15 = 0) or an output address (bit 15 = 1) is present. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| AREA | Output | INT | I, Q, M, D, L | Area ID: indicates how the remaining output parameters are to be interpreted. |
| MASTER | Output | INT | I, Q, M, D, L | Area ID:  - 0, if the slot is located in a centralized configuration: Rack 0 to 3 (for S7-300) or 0 to 21 (for S7-400) - 1 to 32: DP master system ID of the associated field device if the slot is located in a field device on PROFIBUS - 100 to 115: PROFINET IO system ID of the associated field device if the slot is located in a field device on PROFINET |
| STATION | Output | INT | I, Q, M, D, L | No. of the rack when:  - Area ID = 0 - Device number of field device if area ID&gt; 0 |
| SLOT | Output | INT | I, Q, M, D, L | Slot no. |
| SUBSLOT | Output | INT | I, Q, M, D, L | Interface module number |
| OFFSET | Output | INT | I, Q, M, D, L | Offset in user data address area of the associated module |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter AREA

| Value of AREA | System | Meaning of MASTER, STATION, SLOT, SUBSLOT and OFFSET |
| --- | --- | --- |
| 0 | S7-400 | MASTER: 0 STATION: Rack no. SLOT: Slot no. SUBSLOT: 0 OFFSET: Difference between the logical address and the logical base address. |
| 1 | S7-300 | MASTER: 0 STATION: Rack no. SLOT: Slot no. SUBSLOT: 0 OFFSET: Difference between the logical address and the logical base address. |
| 2 | PROFIBUS DP | MASTER: DP master ID STATION: Device number  SLOT: Slot no. in the station SUBSLOT: 0 OFFSET: Offset in user data address area of the associated module |
| PROFINET IO | MASTER: PROFINET IO system ID STATION: Device number  SLOT: Slot no. in the station SUBSLOT: Sub-module number OFFSET: Offset in user data address area of the associated module |  |
| 3 | S5-P area | MASTER: 0 STATION: Rack no. SLOT: Slot number of the adaptation capsule SUBSLOT: 0 OFFSET: Address in the S5 x area |
| 4 | S5-Q area | MASTER: 0 STATION: Rack no. SLOT: Slot number of the adaptation capsule SUBSLOT: 0 OFFSET: Address in the S5 x area |
| 5 | S5-IM3 area | MASTER: 0 STATION: Rack no. SLOT: Slot number of the adaptation capsule OFFSET: Address in the S5 x area |
| 6 | S5-IM4 area | MASTER: 0 STATION: Rack no. SLOT: Slot number of the adaptation capsule SUBSLOT: 0 OFFSET: Address in the S5 x area |

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Specified logical address invalid |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### RD_LGADR: Determine all logical addresses of a module (S7-300, S7-400)

#### Description

You use a logic address of a data block, central submodule or a submodule for PNIO. You use the instruction to determine all the declared logical addresses of this module and the submodule. You have previously configured the assignment of logical addresses to modules and submodules. The "RD_LGADR" instruction enters the determined logical addresses in the PEADDR or PAADDR parameter in ascending order.

#### Parameter

The following table shows the parameters of the instruction "RD_LGADR":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#00: Bit15 of LADDR specifies whether an input (Bit 15=0) or output address (Bit 15=1) is present. - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ) |
| LADDR | Input | WORD | I, Q, M, D, L or constant | One logical address |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| PEADDR | Output | ANY | I, Q, M, D, L | Array for the PI addresses, array elements  must be of the WORD data type. |
| PECOUNT | Output | INT | I, Q, M, D, L | Number of returned PI addresses |
| PAADDR | Output | ANY | I, Q, M, D, L | Array for the PQ addresses, array elements  must be of the WORD data type. |
| PACOUNT | Output | INT | I, Q, M, D, L | Number of returned PQ addresses |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Specified logical address invalid or illegal value for the IOID parameter. |
| 80A0 | Error in the output parameter PEADDR: The data type of the array elements is  not WORD. (This error code only exists for S7-400 and CPU 318.) |
| 80A1 | Error in the output parameter PAADDR: The data type of the array elements is  not WORD. (This error code only exists for S7-400 and CPU 318.) |
| 80A2 | Error in the output parameter PEADDR: The specified array could not  accommodate all the logical addresses. |
| 80A3 | Error in the output parameter PAADDR: The specified array could not  accommodate all the logical addresses. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### GADR_LGC: Query logical start address of a module (S7-300, S7-400)

#### Description

Based on the channel of a signal module, the corresponding module slot and the offset in the user data address area of the module are known. With the "GADR_LGC" instruction you determine the associated logical base address of the module, which means the smallest I or Q address.

If you use the "GADR_LGC" instruction on power modules or modules with packed addresses (ET 200S), then the diagnostics address will be returned.

#### Parameter

The following table shows the parameters of the instruction "GADR_LGC":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SUBNETID | Input | BYTE | I, Q, M, D, L or constant | Area ID:  - 0, if the slot is in one of the racks 0 (central rack) or 1 to 21 (expansion racks). - DP master system ID of the corresponding distributed I/O system if the slot is in a  distributed I/O device. |
| RACK | Input | WORD | I, Q, M, D, L or constant | - Number of the rack if the area identifier is 0. - Device number of the distributed I/O device if the area identifier &gt; 0. |
| SLOT | Input | WORD | I, Q, M, D, L or constant | Slot no. |
| SUBSLOT | Input | BYTE | I, Q, M, D, L or constant | Sub-module slot (if no sub-module can be inserted, 0 must be entered here) |
| SUBADDR | Input | WORD | I, Q, M, D, L or constant | Offset in the user data address area of the  module |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| IOID | Output | BYTE | I, Q, M, D, L | Address area identifier:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   In case of a mixed module, the instruction  supplies the area identifier of the lower  address. If the addresses are equal, then the  instruction will supply the identifier B#16#54. |
| LADDR | Output | WORD | I, Q, M, D, L | Logical base address of the module |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8093 | Invalid value at parameter SUBNETID (the "GADR_LGC" instruction is not valid for PROFINET IO). |
| 8094 | No subnet was configured with the specified SUBNETID . |
| 8095 | Illegal value for RACK parameter |
| 8096 | Illegal value for SLOT parameter |
| 8097 | Illegal value for SUBSLOT parameter |
| 8098 | Illegal value for SUBADDR parameter |
| 8099 | The slot is not configured. |
| 809A | The sub-address of the selected slot is not configured (only possible with central IO devices for CPU and IM). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

### LGC_GADR: Determine the slot belonging to a logical address (S7-300, S7-400)

#### Description

With the instruction you determine the module slot as well as the offset in the user data address space belonging to a logical address.

> **Note**
>
> The "LGC_GADR" instruction cannot be used on a module with packed addresses (ET 200S).

#### Parameters

The following table shows the parameters of the instruction "LGC_GADR":

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IOID | Input | BYTE | I, Q, M, D, L or constant | Address area identifier:  - B#16#00: Bit15 of LADDR specifies whether an input (Bit15=0) or output address (Bit15=1) will be present. - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed  module, you will have to specify the area identifier of the lower address. If  the addresses are identical, you will have to specify B#16#54 . |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical address  For  a mixed module, the lower of the two  addresses must be specified. |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| AREA | Output | BYTE | I, Q, M, D, L | Area ID: indicates how the remaining output parameters are to be interpreted. |
| RACK | Output | WORD | I, Q, M, D, L | Rack no. |
| SLOT | Output | WORD | I, Q, M, D, L | Slot no. |
| SUBADDR | Output | WORD | I, Q, M, D, L | Offset in user data address area of the associated module. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> If you are using an S7-400H automation system in redundant mode and specify the logical address of a module in a connected DP slave when calling the "LGC_GADR" instruction in the LADDR parameter, then the DP master system ID of the active channel will be supplied in the high byte of the RACK parameter. If no active channel exists, the DP master system ID for the associated DP master system is output to the master CPU.

#### Parameter AREA

The output parameter AREA specifies how the output parameters RACK, SLOT and SUBADDR are to be interpreted. The following table explains this dependency.

| Value of AREA | System | Meaning of RACK, SLOT and SUBADDR |
| --- | --- | --- |
| 0 | S7-400 | RACK : Rack no. SLOT : Slot no. SUBADDR : Difference between the logical address and the logical base address. |
| 1 | S7-300 | RACK : Rack no. SLOT : Slot no. SUBADDR : Difference between the logical address and the logical base address. |
| 2 | DP | RACK : (low byte): Device number  RACK : (high byte): DP master ID SLOT : Slot no. in the station SUBADDR : Offset in user data address area of the associated module |
| 3 | S5-P area | RACK : Rack no. SLOT : Slot number of the adaptation capsule  SUBADDR : Address in the S5 x area |
| 4 | S5-Q area | RACK : Rack no. SLOT : Slot number of the adaptation capsule  SUBADDR : Address in the S5 x area |
| 5 | S5-IM3 area | RACK : Rack no. SLOT : Slot number of the adaptation capsule  SUBADDR : Address in the S5 x area |
| 6 | S5-IM4 area | RACK : Rack no. SLOT : Slot number of the adaptation capsule  SUBADDR : Address in the S5 x area |

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8090 | Specified logical address invalid or illegal value for the IOID parameter. |
| 8093 | This instruction is not permitted for the module selected by the parameters IOID and LADDR : |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## Additional functions (S7-300)

This section contains information on the following topics:

- [iSlave (S7-300)](#islave-s7-300)

### iSlave (S7-300)

This section contains information on the following topics:

- [SET_ADDR: Setting network address as own iSlave (S7-300)](#set_addr-setting-network-address-as-own-islave-s7-300)

#### SET_ADDR: Setting network address as own iSlave (S7-300)

##### Description

You can use the instruction to change the DP address of an iSlave DP interface. The addressing is performed via the diagnostics address of the DP interface. For the DP master, the DP slave with the oldest address is discarded from the bus and a DP slave with the new address is included in the bus.

- If the address is already assigned by a station in the DP network, both DP slaves will be discarded from the network.
- If the address is also used as MPI address for the programming device connection, access to the device is possibly disabled. The information about whether the devices are at all accessible is displayed in the "Accessible Devices" dialog.

The network address is not written in the SDB (system data block) and will not be loaded in the work memory. The network address is maintained when the CPU goes to STOP and a warm restart is effected. After a reset or a cold restart, the originally configured address will be used.

The instruction cannot be used for PROFINET IO, because the Ethernet address can be defined as disjoint. If the instruction is used with PROFINET IO, then the error code 16#809B will be output.

##### Functional description

The "SET_ADDR" instruction works asynchronously, which means its execution extends over multiple calls. You start the job by calling "READ_DBL" with REQ =1.

The output parameters RET_VAL and BUSY indicate the status of the job.

##### Parameter

The following table shows the parameters of the "SET_ADDR" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ=1: Function call |
| LADDR | Input | WORD | I, Q, M, D, L or constant | Logical base address |
| ADDR | Input | BYTE | I, Q, M, D, L or constant | New device address |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1: The job is not yet complete. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 700x | The job is not yet complete. Parameter BUSY=1 |
| 8091 | New device address (ADDR) is invalid. |
| 8092 | Station is not an individual slave address of the I-slave |
| 8093 | LADDR is invalid or no interface. |
| 809B | Instruction cannot be executed (for example, the interface is not a DP slave or is active). |
| 80C3 | Insufficient resources (for example, multiple calling of instructions with different parameters). |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
