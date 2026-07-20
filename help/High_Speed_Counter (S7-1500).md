---
title: "High_Speed_Counter (S7-1500)"
package: ProgFBHSCenUS
topics: 6
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# High_Speed_Counter (S7-1500)

This section contains information on the following topics:

- [Description High_Speed_Counter (S7-1500)](#description-high_speed_counter-s7-1500)
- [High_Speed_Counter input parameters (S7-1500)](#high_speed_counter-input-parameters-s7-1500)
- [High_Speed_Counter output parameters (S7-1500)](#high_speed_counter-output-parameters-s7-1500)
- [High_Speed_Counter static variables (S7-1500)](#high_speed_counter-static-variables-s7-1500)
- [Error codes of parameter ErrorID (S7-1500)](#error-codes-of-parameter-errorid-s7-1500)

## Description High_Speed_Counter (S7-1500)

### Description

The High_Speed_Counter instruction is used to control the technology module counting and measuring functions via the user program.

### Call

The instruction High_Speed_Counter must be called once per counter, either cyclically or in a time-controlled program. The call is not permitted in an event-controlled interrupt program.

### Operating principle

**Counter value**: The counter value is available at the output parameter CountValue. The counter value is updated at every call of the High_Speed_Counter instruction.

**Measured value**: The technology module updates the measured value asynchronously to the instruction call based on the configured update time. The measured value last determined by the technology module is updated at the output parameter MeasuredValue each time the instruction is called.

The measured value and the counter value are available in parallel in the feedback interface.

**Capture**: The output parameter CaptureStatus = TRUE indicates a valid Capture value at the output parameter CapturedValue.

- A Capture value is captured under the following conditions:

  - A digital input has the parameter assignment "Capture"
  - CaptureEnable = TRUE
  - Edge at digital input with the Capture function
- The output parameter CaptureStatus is reset by a negative edge at the input parameter CaptureEnable.

**Synchronization**: The output parameter SyncStatus = TRUE indicates that a synchronization has occurred.

- The counter value is synchronized under the following conditions:

  - A digital input has the parameter assignment "Synchronization" **or** the incremental encoder has the parameter assignment "Synchronization at signal N"
  - SyncEnable = TRUE
  - The static tag SyncUpDirection (or SyncDownDirection) = TRUE
  - Edge at the digital input with the synchronization function **or** positive edge of the signal N at the encoder input
- The output parameter SyncStatus is reset by a negative edge at

  - the input parameter SyncEnable or
  - the static tag SyncDownDirection or
  - the static tag SyncUpDirection

**Parameter changes via the user program**

Proceed as follows to modify parameters using the user program:

1. Check based on the respective Set tag to determine whether the technology object is ready for the parameter change (Set tag = FALSE) or whether a change job is still running (Set tag = TRUE).  
   The following Set tags in UserCmdFlags are available for this in the static tags of the technology object instance DB:

   - SetReferenceValue0
   - SetReferenceValue1
   - SetUpperLimit
   - SetLowerLimit
   - SetCountValue
   - SetStartValue
   - SetNewDirection
2. If the technology object is ready for the parameter change, modify the relevant static tag.  
   The following static tags of the technology object instance DB are available for this:

   - NewReferenceValue0 / NewReferenceValue0_M (for SetReferenceValue0)
   - NewReferenceValue1 / NewReferenceValue1_M (for SetReferenceValue1)
   - NewUpperLimit
   - NewLowerLimit
   - NewCountValue
   - NewStartValue
   - NewDirection
3. Set the relevant Set tag for execution of the change command.
4. Use the output parameter Error to check whether an error has occurred.  
   If no errors have occurred and the Set tag has been automatically reset by the technology object, the parameter change was successful.

> **Note**
>
> **Changed counting limit**
>
> If the new high counting limit is less than the current counter value, the counter value is set to the low counting limit or the start value according on the parameter assignment. If the new low counting limit is greater than the current counter value, the counter value is set to the high counting limit or the start value according to the parameter assignment.

### Operating mode (High_Speed_Counter V3.0 or higher)

Configure the operating mode in the technology object under "Behavior of DQ0".

The operating mode is indicated by the output parameter CompareMeasuredValue:

| State | Description |
| --- | --- |
| FALSE | Operating mode "Use count value as reference"  The comparison functions work with the counter value. The following static variables are specifically used in this operating mode:  - NewReferenceValue0 - NewReferenceValue1 - CurReferenceValue0 - CurReferenceValue1   The four specific static variables of operating mode "Use measured value as reference" are ignored. |
| TRUE | Operating mode "Use measured value as reference":  The comparison functions work with the measured value. The following static variables are specifically used in this operating mode:  - NewReferenceValue0_M - NewReferenceValue1_M - CurReferenceValue0_M - CurReferenceValue1_M   The four specific static variables of operating mode "Use count value as reference" are ignored. |

### Acknowledgment of events

You acknowledge signaled events using the positive edge of the input parameter EventAck . EventAck must stay set until the technology object has reset the status bits of the following events of the count channel:

- CompResult0
- CompResult1
- ZeroStatus
- PosOverflow
- NegOverflow

### Status of the digital inputs (TM Count and TM PosInput)

You can obtain the status of the digital inputs with the static tags StatusDI0, StatusDI1 or StatusDI2.

### Status of the digital inputs (Compact CPU)

You can obtain the status of the digital inputs with the static tags StatusDI0 and StatusDI1. When a digital input of the Compact CPU is not used for a counter, you can use it via the user program.

### Use of digital outputs by the user program (TM Count and TM PosInput)

You can set the digital outputs with the High_Speed_Counter instruction,

- If the "Use by user program" setting is configured for "Set output".
- If the "After set command from CPU until comparison value" setting is configured for "Set output".
- if you set the corresponding static tag ManualCtrlDQm (temporary overwrite).

The static tags SetDQ0 and SetDQ1 only have an effect in these cases. In the first and third case, DQm follows the value of SetDQm. In the second case, DQm is set with a positive edge of SetDQm. DQm is reset when the counter value corresponds to the comparison value or at a negative edge of SetDQm.

### Use digital outputs by user program (Compact CPU)

You can set the DQ1 digital output with the High_Speed_Counter instruction.

- If the "Use by user program" setting is configured for "Set output".
- If the "After set command from CPU until comparison value" setting is configured for "Set output".
- if you set the corresponding static tag ManualCtrlDQ1 (temporary overwrite).

The static tag SetDQ1 only has an effect in these cases. In the first and third case, DQ1 follows the value of SetDQ1. In the second case, DQ1 is set and reset with a positive edge of SetDQ1 when the counter value corresponds to the comparison value or at a negative edge of SetDQ1.

> **Note**
>
> Before you can set a physical digital output of the Compact CPU with the High_Speed_Counter instruction, you have to assign the DQ1 signal to the desired digital output.

You can set the DQ0 signal using the High_Speed_Counter instruction with the static tag StatusDQ0.

- If the "Use by user program" setting is configured for "Set output".
- If the "After set command from CPU until comparison value" setting is configured for "Set output".
- If you set the static tag ManualCtrlDQ0 (temporary overwrite).

The static tag SetDQ0 only has an effect in these cases. In the first and third case, DQ0 follows the value of SetDQ0. In the second case, StatusDQ0 is set and reset with an edge (positive or negative) by SetDQ0 and is reset when the counter value corresponds to the comparison value.

> **Note**
>
> The digital output DQ0 is not available as a physical output.

### Reaction to error

If an error has occurred during the call of the instruction or in the technology module, the output parameter Error is set. More detailed error information can be read at the output parameter [ErrorID](#error-codes-of-parameter-errorid-s7-1500).

Eliminate the cause of the error and acknowledge the error message by setting the input parameter ErrorAck. When no more errors are pending, the technology object resets the output parameter Error . No new error is signaled until you acknowledge the previous error.

### Changing the count direction

The count direction can only be changed by the user program if "Pulse (A)" is configured as the signal type. In all other cases, the count direction is determined by the input signals of the technology module. The count direction is controlled by the static tag NewDirection:

- +1: Upward count direction
- -1: Downward count direction

To execute the change command, you need to set the static tag SetNewDirection = TRUE.

## High_Speed_Counter input parameters (S7-1500)

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SwGate | INPUT | BOOL | FALSE | Control software gate:  - Positive edge: Software gate opens - Negative edge: Software gate closes   Together with the hardware gate, the SwGate enables the internal gate. |
| CaptureEnable | INPUT | BOOL | FALSE | Enable Capture function  After the enable, a Capture event occurs at the next configured edge at the relevant digital input. A negative edge at CaptureEnable resets the output parameter CaptureStatus. A negative edge at CaptureEnable resets the enable even if no Capture event has occurred.  Irrespective of CaptureEnable the last value is retained at the output parameter CapturedValue until the next Capture event. |
| SyncEnable | INPUT | BOOL | FALSE | Enable synchronization  The direction enabled for synchronization is indicated in the static tags SyncUpDirection and SyncDownDirection. A negative edge at SyncEnable resets the output parameter SyncStatus . |
| ErrorAck | INPUT | BOOL | FALSE | High_Speed_Counter up to V3.0: A positive edge acknowledges the status reported.  High_Speed_Counter as of V3.1: A high level acknowledges the error status reported. |
| EventAck | INPUT | BOOL | FALSE | A positive edge resets the following output parameters:  - CompResult0 - CompResult1 - ZeroStatus - PosOverflow - NegOverflow |
| SetCountValue | INOUT | BOOL | FALSE | A positive edge starts the transfer of the new counter value in the static tag NewCountValue to the technology module. The counter value takes effect immediately after the transfer. |

## High_Speed_Counter output parameters (S7-1500)

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| StatusHW | OUTPUT | BOOL | FALSE | Status bit technology module: The module is configured and ready for operation. The module data is valid. |
| StatusGate | OUTPUT | BOOL | FALSE | Status bit: Internal gate is released if parameter is set |
| StatusUp | OUTPUT | BOOL | FALSE | Status bit: The last count pulse incremented the counter and took place no more than 0.5 s ago |
| StatusDown | OUTPUT | BOOL | FALSE | Status bit: The last count pulse decremented the counter and took place no more than 0.5 s ago |
| CompResult0 | OUTPUT | BOOL | FALSE | Status bit: Compare event for DQ0 occurred (status change) based on the selected comparison condition.  If the counter value is set to the start value in operating mode "Use count value as reference", CompResult0 is not set.  The positive edge of the input parameter EventAck is used to reset CompResult0 . |
| CompResult1 | OUTPUT | BOOL | FALSE | Status bit: Compare event for DQ1 occurred (status change) based on the selected comparison condition.   If the counter value is set to the start value in operating mode "Use count value as reference", CompResult1 is not set.  The positive edge of the input parameter EventAck is used to reset CompResult1 . |
| SyncStatus | OUTPUT | BOOL | FALSE | Status bit: Synchronization event occurred  If the input parameter SyncEnable is set, the configured edge sets the status bit SyncStatus at the respective digital input .  SyncStatus is reset by a negative edge at  - SyncEnable (input parameter) or - SyncUpDirection (static tag) or - SyncDownDirection (static tag) |
| CaptureStatus | OUTPUT | BOOL | FALSE | Status bit: Capture event occurred, the output parameter CapturedValue has a valid Capture value  If the input parameter CaptureEnable is set, the configured edge sets the status bit CaptureStatus. at the respective digital input.  You reset CaptureStatus using the negative edge of the input parameter CaptureEnable . |
| ZeroStatus | OUTPUT | BOOL | FALSE | Status bit: CountValue has reached the value "0" irrespective of the count direction   You reset ZeroStatus using the positive edge of the input parameter EventAck. |
| PosOverflow | OUTPUT | BOOL | FALSE | Status bit: CountValue has violated high counting limit in the positive direction   You reset PosOverflow using the positive edge of the input parameter EventAck. |
| NegOverflow | OUTPUT | BOOL | FALSE | Status bit: CountValue has violated low counting limit in the negative direction   You reset NegOverflow using the positive edge of the input parameter EventAck. |
| Error | OUTPUT | BOOL | FALSE | An error has occurred. Refer to the output parameter ErrorID for the cause of the error. |
| ErrorID | OUTPUT | WORD | 0 | The [ErrorID](#error-codes-of-parameter-errorid-s7-1500) parameter displays the number of the error message.   ErrorID = 0000<sub>H</sub>: There is no error. |
| CountValue | OUTPUT | DINT | 0 | Current counter value |
| CapturedValue | OUTPUT | DINT | 0 | The last acquired Capture value The value is retained until the next Capture event, irrespective of the input parameter CaptureEnable.  If a new Capture event has occurred, CaptureStatus is set and is reset by you using the negative edge of the input parameter CaptureEnable . |
| MeasuredValue | OUTPUT | REAL | 0.0 | Current measured value for frequency, period duration or velocity (depending on configuration) |
| CompareMeasuredValue<sup>1</sup> | OUTPUT | BOOL | FALSE | Status bit:   FALSE: Operating mode "Use count value as reference"; comparison functions work with counter value  TRUE: Operating mode "Use measured value as reference"; comparison functions work with measured value |
| <sup>1</sup> Available for High_Speed_Counter version V3.0 or higher |  |  |  |  |

## High_Speed_Counter static variables (S7-1500)

| Tag |  | Data type | Default | Access | Description |
| --- | --- | --- | --- | --- | --- |
| NewCountValue |  | DINT | L#0 | Write | New counter value |
| NewReferenceValue0 |  | DINT | L#0 | Write | New comparison value 0 in the operating mode "Use count value as reference" |
| NewReferenceValue1 |  | DINT | L#10 | Write | New comparison value 1 in the operating mode "Use count value as reference" |
| NewReferenceValue0_M<sup>1</sup> |  | REAL | L#0.0 | Write | New comparison value 0 in operating mode "Use measured value as reference" |
| NewReferenceValue1_M<sup>1</sup> |  | REAL | L#10.0 | Write | New comparison value 1 in operating mode "Use measured value as reference" |
| NewUpperLimit |  | DINT | L#2147483647 | Write | New high counting limit |
| NewLowerLimit |  | DINT | L#-2147483648 | Write | New low counting limit |
| NewStartValue |  | DINT | L#0 | Write | New start value |
| NewDirection |  | INT | 0 | Write | New count direction:  +1: Upward count direction  -1: Downward count direction |
| CurReferenceValue0 |  | DINT | L#0 | Read | Current comparison value 0 in operating mode "Use count value as reference" |
| CurReferenceValue1 |  | DINT | L#10 | Read | Current comparison value 1 in operating mode "Use count value as reference" |
| CurReferenceValue0_M<sup>1</sup> |  | REAL | L#0.0 | Read | Current comparison value 0 in operating mode "Use measured value as reference" |
| CurReferenceValue1_M<sup>1</sup> |  | REAL | L#10.0 | Read | Current comparison value 1 in operating mode "Use measured value as reference" |
| CurUpperLimit |  | DINT | L#2147483647 | Read | Current high counting limit |
| CurLowerLimit |  | DINT | L#-2147483648 | Read | Current low counting limit |
| CurStartValue |  | DINT | L#0 | Read | Current start value |
| AdditionalErrorID |  | DWORD | W#16#0000 | Read | Error information of an internal instruction, e.g. RDREC |
| OutputByteOffset<sup>2</sup> |  | DINT | L#0 | Read | For internal use |
| InputByteOffset<sup>2</sup> |  | DINT | L#0 | Read | For internal use |
| Initialized<sup>2</sup> |  | BOOL | FALSE | Write | Instruction is initialized and ready for operation.  Resetting to FALSE leads to the re-initialization of the technology object. |
| UserCmdFlags |  | STRUCT | - |  |  |
|  | SetNewDirection | BOOL | FALSE | Write | Set new count direction |
|  | SetUpperLimit | BOOL | FALSE | Write | Set high counting limit |
|  | SetLowerLimit | BOOL | FALSE | Write | Set low counting limit |
|  | SetReferenceValue0 | BOOL | FALSE | Write | Set comparison value 0 |
|  | SetReferenceValue1 | BOOL | FALSE | Write | Set comparison value 1 |
|  | SetStartValue | BOOL | FALSE | Write | Set start value |
|  | SyncDownDirection | BOOL | TRUE | Write | Enable synchronization in downward count direction |
|  | SyncUpDirection | BOOL | TRUE | Write | Enable synchronization in upward count direction |
|  | SetDQ0 | BOOL | FALSE | Write | Set digital output DQ0 |
|  | SetDQ1 | BOOL | FALSE | Write | Set digital output DQ1 |
|  | ManualCtrlDQ0 | BOOL | FALSE | Write | Enable setting of digital output DQ0:  TRUE:   - SetDQ0 sets DQ0 - Control bit TM_CTRL_DQ0 = FALSE   FALSE:   - Setting not enabled - Control bit TM_CTRL_DQ0 = TRUE |
|  | ManualCtrlDQ1 | BOOL | FALSE | Write | Enable setting of digital output DQ1:  TRUE:   - SetDQ1 sets DQ1 - Control bit TM_CTRL_DQ1 = FALSE   FALSE:   - Setting not enabled - Control bit TM_CTRL_DQ1 = TRUE |
| UserStatusFlags |  | STRUCT | - |  |  |
|  | StatusDI0 | BOOL | FALSE | Read | Current status of digital input DI0 |
|  | StatusDI1 | BOOL | FALSE | Read | Current status of digital input DI1 |
|  | StatusDI2 | BOOL | FALSE | Read | Current status of digital input DI2 |
|  | StatusDQ0 | BOOL | FALSE | Read | Current status of digital output DQ0 |
|  | StatusDQ1 | BOOL | FALSE | Read | Current status of digital output DQ1 |
| <sup>1</sup> Available for High_Speed_Counter version V3.0 or higher   <sup>2</sup> Available for High_Speed_Counter version V5.0 or higher |  |  |  |  |  |

## Error codes of parameter ErrorID (S7-1500)

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| **Error messages from technology module** |  |
| 80A1 | POWER_ERROR from feedback interface: Incorrect supply voltage L+ |
| 80A2 | ENC_ERROR from feedback interface: Incorrect encoder signal |
| 80A3 | LD_ERROR from feedback interface: Error when loading via control interface |
| **Error messages of the instruction**  **High_Speed_Counter** |  |
| 80B1 | Invalid count direction |
| 80B4 | For operating mode "Use count value as reference", the following applies:  New low counting limit does not meet the following conditions:  - Low counting limit &lt; high counting limit - Low counting limit &lt;= comparison value/start value     For operating mode "Use measured value as reference", the following applies:  New low counting limit does not meet the following conditions:  - Low counting limit &lt; high counting limit - Low counting limit &lt;= start value |
| 80B5 | For operating mode "Use count value as reference", the following applies:  New high counting limit does not meet the following conditions:  - Low counting limit &lt; high counting limit - High counting limit &gt;= comparison value/start value     For operating mode "Use measured value as reference", the following applies:  New high counting limit does not meet the following conditions:  - Low counting limit &lt; high counting limit - High counting limit &gt;= start value |
| 80B6 | New start value does not meet the following condition:  - Low counting limit &lt;= start value &lt;= high counting limit |
| 80B7 | New counter value does not meet the following condition:  - Low counting limit &lt;= counter value &lt;= high counting limit |
| 80B8 | For operating mode "Use count value as reference", the following applies:  New comparison value 0 does not meet the following conditions:  - Low counting limit &lt;= comparison value 0 &lt;= high counting limit - Comparison value 0 &lt; comparison value 1     For operating mode "Use measured value as reference", the following applies:  New comparison value 0 does not meet the following conditions:  - Comparison value 0 &lt; comparison value 1 |
| 80B9 | For operating mode "Use count value as reference", the following applies:  New comparison value 1 does not meet the following conditions:  - Low counting limit &lt;= comparison value 1 &lt;= high counting limit - Comparison value 0 &lt; comparison value 1     For operating mode "Use measured value as reference", the following applies:  New comparison value 1 does not meet the following conditions:  - Comparison value 0 &lt; comparison value 1 |
| 80C0 | Instruction High_Speed_Counter was called multiple times with the same instance (DB) |
| 80C1 | Communication with technology module failed (read data records): Error information of internal instruction RDREC saved in static tag AdditionalErrorID |
| 80C2 | Communication with technology module failed (write data records): Error information of internal instruction WRREC saved in static tag AdditionalErrorID |
| 80C3 | Access to input data (feedback interface) failed: Error information of internal instruction GETIO_PART saved in static tag AdditionalErrorID |
| 80C4 | Access to output data (control interface) failed: Error information of internal instruction SETIO_PART saved in static tag AdditionalErrorID |
| 80C5 | Reading of the current start information of the OB failed: Error information of internal instruction RD_SINFO saved in static tag AdditionalErrorID |
| 80C6 | Failed to get I/O addresses of the technology module: Error information of internal instruction RD_ADDR saved in static tag AdditionalErrorID |
| 80C7 | Module not inserted or no supply voltage L+ |
| 80C8 | Specified module is not permitted in the static tag Configuration.HWID |
