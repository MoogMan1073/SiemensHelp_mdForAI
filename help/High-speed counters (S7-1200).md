---
title: "High-speed counters (S7-1200)"
package: ProgTech1200FaCoenUS
topics: 3
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# High-speed counters (S7-1200)

This section contains information on the following topics:

- [CTRL_HSC: Control high-speed counters (S7-1200)](#ctrl_hsc-control-high-speed-counters-s7-1200)
- [CTRL_HSC_EXT: Control high-speed counter (extended) (S7-1200)](#ctrl_hsc_ext-control-high-speed-counter-extended-s7-1200)

## CTRL_HSC: Control high-speed counters (S7-1200)

### Parameters

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN | INPUT | BOOL | I, Q, M, D, L, T, C | Enable input |
| ENO | OUTPUT | BOOL | I, Q, M, D, L | Enable output |
| HSC | INPUT | HW_HSC | I, Q, M or constant | Hardware address of the high-speed counter (HW-ID) |
| DIR | INPUT | BOOL | I, Q, M, D, L or constant | Enables the new count direction (see NEW_DIR) |
| CV | INPUT | BOOL | I, Q, M, D, L or constant | Enables the new count value (see NEW_CV) |
| RV | INPUT | BOOL | I, Q, M, D, L or constant | Enables the new reference value (see NEW_RV) |
| PERIOD | INPUT | BOOL | I, Q, M, D, L or constant | Enables the new period of a frequency measurement (see NEW_PERIOD) |
| NEW_DIR | INPUT | INT | I, Q, M, D, L or constant | Count direction loaded when DIR = TRUE. |
| NEW_CV | INPUT | DINT | I, Q, M, D, L or constant | Count value loaded when CV = TRUE. |
| NEW_RV | INPUT | DINT | I, Q, M, D, L or constant | Reference value loaded when RV = TRUE. |
| NEW_PERIOD | INPUT | INT | I, Q, M, D, L or constant | Period of the frequency measurement loaded when PERIOD = TRUE. |
| BUSY | OUTPUT | BOOL | I, Q, M, D, L | Processing status * |
| STATUS | OUTPUT | WORD | I, Q, M, D, L | Status of the operation |
| * With a high-speed counter in the CPU or in the signal board, the BUSY parameter always has the value 0. |  |  |  |  |

### Description

With the "Control high-speed counter" instruction, you can make parameter settings and control the high-speed counters supported by the CPU by loading new values into the counter. Execution of the instruction requires that a high-speed counter to be controlled is enabled. You cannot execute multiple "Control high-speed counter" instructions simultaneously in the program for a given high-speed counter.

You can load the following parameter values into a high-speed counter using the "Control high-speed counter" instruction:

- Count direction (NEW_DIR): The count direction defines whether a high-speed counter counts up or down. The count direction is defined by the following values at the NEW_DIR input: 1 = up, -1 = down.

  A change to the count direction with the "Control high-speed counter" instruction is only possible when direction control is set in the parameters by the program. The count direction specified at the NEW_DIR input is loaded into a high-speed counter when the bit at the DIR input is set.
- Count value (NEW_CV): The count value is the initial value at which a high-speed counter starts counting. The count value can be in the range -2147483648 to 2147483647.

  The count value specified at the NEW_CV input is loaded into a high-speed counter when the bit at the CV input is set.
- Reference value (NEW_RV): You can compare the reference value with the current counter value to trigger an alarm. Similar to the counter value, the reference value can be in the range -2147483648 to 2147483647.

  The reference value specified at the NEW_RV input is loaded into a high-speed counter when the bit at the RV input is set.
- Period of the frequency measurement (NEW_PERIOD): The period of the frequency measurement is specified by the following values at the NEW_PERIOD input: 10 = 0.01s, 100 = 0.1s, 1000 = 1s.

  The time period can be updated if the "Measure frequency" function for the specified high-speed counter is configured. The time period specified at the NEW_PERIOD input is loaded into a high-speed counter when the bit at the PERIOD input is set.

The "Control high-speed counter" instruction is only executed if the signal state at the EN input is "1".

The ENO enable output is set only when the EN enable input has signal state "1" and no errors occur during execution of the operation.

When inserting the "Control high-speed counter" instruction, an instance data block is created in which the operation data is saved.

### STATUS parameter

At the STATUS output, you can query whether errors occurred during execution of the "Control high-speed counter" instruction. The following table shows the meaning of the values output at the STATUS output:

| Error code (hexadecimal) | Description |
| --- | --- |
| 0 | No error |
| 80A1 | Hardware identifier of the high-speed counter invalid |
| 80B1 | Count direction (NEW_DIR) invalid |
| 80B2 | Count value (NEW_CV) invalid |
| 80B3 | Reference value (NEW_RV) invalid |
| 80B4 | Period of the frequency measurement (NEW_PERIOD) invalid |
| 80C0 | Multiple access to the high-speed counter |
| 80D0 | The high-speed counter (HSC) is not enabled in the CPU hardware configuration. |

---

**See also**

[Events and OBs (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#events-and-obs-s7-1200)

## CTRL_HSC_EXT: Control high-speed counter (extended) (S7-1200)

### Parameters

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN | INPUT | BOOL | I, Q, M, D, L, T, C | Enable input |
| ENO | OUTPUT | BOOL | I, Q, M, D, L | Enable output |
| HSC | INPUT | HW_HSC | I, Q, M or constant | Hardware address of the high-speed counter (HW-ID) |
| CTRL | INOUT | VARIANT | M, D | Use of a system data type (SDT) |
| DONE | OUTPUT | BOOL | I, Q, M, D, L | Feedback after successful processing instruction |
| BUSY | OUTPUT | BOOL | I, Q, M, D, L | Processing status |
| ERROR | OUTPUT | BOOL | I, Q, M, D, L | Feedback for faulty processing of the instruction |
| STATUS | OUTPUT | WORD | I, Q, M, D, L | Status of the operation |

### Description

With the "Control high-speed counter (extended)" instruction, you can control and assign parameters to the high-speed counters supported by the CPU via the software by loading new values into the counters. Execution of the instruction requires that a high-speed counter to be controlled is enabled. You cannot execute multiple "Control high-speed counter (extended)" instructions simultaneously in the program for a given high-speed counter.

The "Control high-speed counter (extended)" instruction is only executed if the signal state at the EN input is "1". As long as the operation is executing, the bit at the BUSY output is set. Once the operation has executed completely, the bit at the BUSY output is reset.

The ENO enable output is set only when the EN enable input has signal state "1" and no errors occur during execution of the operation.

When the "Control high-speed counter (extended)" instruction is inserted, an instance data block is created in which the operation data is saved.

### Using the system data type HSC_Period

The "Control high-speed counter (extended)" instruction supports the system data type SDT 381 "HSC_Period" for the period measurement.

The "HSC_Period" data type corresponds to an HSC that is configured for the "Period" operating mode. The CTRL_HSC_EXT instruction offers program access to the number of input pulses across a specified measuring interval. This instruction allows the calculation of the period between the input pulses with a resolution in the nanosecond range.

| Byte | Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- | --- |
| 0 … 3 | ElapsedTime | OUT | UDINT | Time between the rising edges of Edge_Count |
| 4 … 7 | EdgeCount | OUT | UDINT | Number of the rising edges within the Elapsed_Time.  If Edge_Count = 0, the Elapsed_Time is the time since the last rising edge. |
| 8.0 | EnHSC | IN | BOOL | Use as an enable input via gate control:   - FALSE: Measurement stopped - TRUE: Measurement enabled |
| 8.6 | EnPeriod | IN | BOOL | Update of the period   - FALSE: No update - TRUE: Update period |
| 10 ... 11 | NewPeriod | IN | INT | Interval of the period measurement in milliseconds.  Permissible values are 10, 100 and 1000. |

ElapsedTime specifies the time in nanoseconds between the last counter events of consecutive measuring intervals. If no counter events occurred during a measuring interval, ElapsedTime outputs the accumulated time since the last counter event. ElapsedTime has a range of 0 to 4,294,967,280 nanoseconds (0x0000 0000 to 0xFFFF FFF0). The return value 4,294,967,295 (0xFFFF FFFF) signals that a period overflow has occurred. An overflow indicates that the period between two pulse edges exceeds 4.295 seconds and that the period cannot be calculated with this instruction. The values from 0xFFFF FFF1 to 0xFFFF FFFE are reserved.

EdgeCount outputs the number of counter events received during the measuring interval. The period can only be calculated if the value of EdgeCount is greater than zero. If ElapsedTime is either 0 (no input pulses received) or OR 0xFFFF FFFF (period overflow), EdgeCount is not valid.

If EdgeCount is valid, calculate the period in nanoseconds by using the following formula: Period = ElapsedTime/EdgeCount

The calculated period value is a mean value from time periods of all the pulses that occur during the measuring interval. If the period of an incoming pulse is greater than the measuring interval (10, 100 or 1000 ms), the period calculation requires several measuring intervals.

The following figures show examples of the period measurement with the instruction:

![Using the system data type HSC_Period](images/88548094347_DV_resource.Stream@PNG-en-US.png)

### STATUS parameter

At the STATUS output, you can query whether errors occurred during execution of the "Control high-speed counter (extended)" instruction. The following table shows the meaning of the values output at the STATUS output:

| Error code (hexadecimal) | Description |
| --- | --- |
| 0 | No error |
| 80A1 | Hardware identifier of the high-speed counter invalid |
| 80C0 | Multiple access to the high-speed counter |
| 80D0 | The high-speed counter (HSC) is not enabled in the CPU hardware configuration. |
