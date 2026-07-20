---
title: "SSI_Absolute_Encoder (S7-1500)"
package: ProgFBSSIenUS
topics: 6
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SSI_Absolute_Encoder (S7-1500)

This section contains information on the following topics:

- [Description SSI_Absolute_Encoder (S7-1500)](#description-ssi_absolute_encoder-s7-1500)
- [Input parameter SSI_Absolute_Encoder (S7-1500)](#input-parameter-ssi_absolute_encoder-s7-1500)
- [Output parameter SSI_Absolute_Encoder (S7-1500)](#output-parameter-ssi_absolute_encoder-s7-1500)
- [Static tags SSI_Absolute_Encoder (S7-1500)](#static-tags-ssi_absolute_encoder-s7-1500)
- [Error codes of parameter ErrorID (S7-1500)](#error-codes-of-parameter-errorid-s7-1500)

## Description SSI_Absolute_Encoder  (S7-1500)

### Description

The SSI_Absolute_Encoder instruction is used to control the position input and measuring functions of the technology module TM PosInput via the user program.

### Call

The instruction must be called once per channel, either cyclically or in a time-controlled program. The call is not permitted in an event-controlled interrupt program.

### Operating principle

**Position value**: The position value is available at the output parameter PositionValue. The position value is updated every time the instruction is called.

**Measured value**: The technology module updates the measured value asynchronously to the instruction call based on the configured update time. The measured value last determined by the technology module is updated at the output parameter MeasuredValue each time the instruction is called.

Measured value and position value are available in parallel as output parameters.

Instead of a measured value, the complete SSI frame can be returned at the output parameter CompleteSSIFrame. Either MeasuredValue or CompleteSSIFrame is valid, depending on the parameter assignment.

**Capture**: The output parameter CaptureStatus = TRUE indicates a valid Capture value at the output parameter CapturedValue.

- A Capture value is captured under the following conditions:

  - A digital input has the parameter assignment "Capture"
  - CaptureEnable = TRUE
  - Edge at digital input with the Capture function
- The output parameter CaptureStatus is reset by a negative edge at the input parameter CaptureEnable.

**Parameter changes via the user program**

Proceed as follows to modify parameters using the user program:

1. Check the relevant Set tag to establish whether the technology object is ready for the parameter change (Set tag = FALSE) or whether a change job is still running (Set tag = TRUE).   
   The following Set tags in UserCmdFlags are available for this in the static tags of the technology object instance DB:

   - SetReferenceValue0
   - SetReferenceValue1
2. If the technology object is ready for the parameter change, modify the relevant static tag.  
   The following static tags of the technology object instance DB are available for this:

   - NewReferenceValue0 / NewReferenceValue0_M (for SetReferenceValue0)
   - NewReferenceValue1 / NewReferenceValue1_M (for SetReferenceValue1)
3. Set the relevant Set tag for execution of the change job.
4. Use the output parameter Error to check whether an error has occurred.  
   If no errors have occurred and the Set tag has been automatically reset by the technology object, the parameter change was successful.

### Operating mode

Configure the operating mode in the technology object under "Behavior of DQ0".

The operating mode is indicated by the output parameters CompareMeasuredValue:

| State | Description |
| --- | --- |
| FALSE | Operating mode "Use position value (SSI absolute value) as reference":  The comparison functions work with the position value. The following static variables are specifically used in this operating mode:  - NewReferenceValue0 - NewReferenceValue1 - CurReferenceValue0 - CurReferenceValue1   The four specific static variables of operating mode "Use measured value as reference" are ignored. |
| TRUE | Operating mode "Use measured value as reference":  The comparison functions work with the measured value. The following static variables are specifically used in this operating mode:  - NewReferenceValue0_M - NewReferenceValue1_M - CurReferenceValue0_M - CurReferenceValue1_M   The four specific static tags of operating mode "Use position value (SSI absolute value) as reference" are ignored. |

### Acknowledgment of events

You acknowledge signaled events using the positive edge of the input parameter EventAck . EventAck must stay set until the technology object has reset the status bits of the following events of the count channel:

- CompResult0
- CompResult1
- ZeroStatus
- PosOverflow
- NegOverflow

### Status of the digital inputs

You obtain the status of the digital inputs via the static tags StatusDI0 and StatusDI1.

### Using digital outputs with user program

In the following cases you can set the digital outputs via the instruction:

| Case | Description |
| --- | --- |
| The setting "Use by user program" is configured for "Set output". | The respective digital output DQM follows the value of SetDQm. |
| The setting "After set command from CPU until comp. value" is configured for "Set output". | The respective digital output DQm is set with a negative edge of SetDQm. DQm is reset when the position value corresponds to the comparison value or at a negative edge of SetDQm. |
| Set the respective static variable ManualCtrlDQm (temporary overwrite). | The respective digital output DQM follows the value of SetDQm. |

### Reaction to error

If an error has occurred during the call of the instruction or in the technology module, the output parameter Error is set. More detailed error information can be read at the output parameter [ErrorID](#error-codes-of-parameter-errorid-s7-1500).

Eliminate the cause of the error and acknowledge the error message by setting the input parameter ErrorAck. When no more errors are pending, the technology object resets the output parameter Error . No new error is signaled until you acknowledge the previous error.

## Input parameter SSI_Absolute_Encoder (S7-1500)

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| CaptureEnable | INPUT | BOOL | FALSE | Enable Capture function  After the enable, a Capture event occurs at the next configured edge at the relevant digital input. A negative edge at CaptureEnable resets the output parameter CaptureStatus. A negative edge at CaptureEnable resets the enable even if no Capture event has occurred.  Irrespective of CaptureEnable the last value is retained at the output parameter CapturedValue until the next Capture event. |
| ErrorAck | INPUT | BOOL | FALSE | SSI_Absolute_Encoder V1.0: A positive edge acknowledges the error status reported.  SSI_Absolute_Encoder as of V2.0: A high level acknowledges the error status reported. |
| EventAck | INPUT | BOOL | FALSE | A positive edge resets the following output parameters:  - CompResult0 - CompResult1 - ZeroStatus - PosOverflow - NegOverflow |

## Output parameter SSI_Absolute_Encoder (S7-1500)

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| StatusHW | OUTPUT | BOOL | FALSE | Status bit technology module: The module is configured and ready for operation. The module data is valid. |
| StatusUp | OUTPUT | BOOL | FALSE | Status bit: Last position value has changed in the positive direction and took place no more than 0.5 s ago. |
| StatusDown | OUTPUT | BOOL | FALSE | Status bit: Last position value has changed in the negative direction and took place no more than 0.5 s ago. |
| CompResult0 | OUTPUT | BOOL | FALSE | Status bit: Comparison event for DQ0 (change of state) occurs as a result of the selected comparison condition.  The positive edge of the input parameter EventAck is used to reset CompResult0 . |
| CompResult1 | OUTPUT | BOOL | FALSE | Status bit: Comparison event for DQ1 (change of state) occurs as a result of the selected comparison condition.   The positive edge of the input parameter EventAck is used to reset CompResult1 . |
| CaptureStatus | OUTPUT | BOOL | FALSE | Status bit: Capture event occurred, the output parameter CapturedValue has a valid Capture value  If the input parameter CaptureEnable is set, the configured edge sets the status bit CaptureStatus. at the respective digital input.  You reset CaptureStatus using the negative edge of the input parameter CaptureEnable . |
| CapturedValue | OUTPUT | DINT | 0 | The last acquired Capture value The value is retained until the next Capture event, irrespective of the input parameter CaptureEnable.  If a new Capture event has occurred, CaptureStatus is set and is reset by you using the negative edge of the input parameter CaptureEnable . |
| ZeroStatus | OUTPUT | BOOL | FALSE | Status bit: PositionValue has reached or exceeded the value "0" irrespective of the count direction.  You reset ZeroStatus using the positive edge of the input parameter EventAck. |
| PosOverflow | OUTPUT | BOOL | FALSE | Status bit: PositionValue has exceeded the high limit of the position value range of the encoder in the positive direction.  You reset PosOverflow using the positive edge of the input parameter EventAck. |
| NegOverflow | OUTPUT | BOOL | FALSE | Status bit: PositionValue has exceeded the low limit of the position value range of the encoder in the negative direction.  You reset NegOverflow using the positive edge of the input parameter EventAck. |
| Error | OUTPUT | BOOL | FALSE | An error has occurred. Refer to the output parameter ErrorID for the cause of the error. |
| ErrorID | OUTPUT | WORD | 0 | The [ErrorID](#error-codes-of-parameter-errorid-s7-1500) parameter displays the number of the error message.   ErrorID = 0000<sub>H</sub>: There is no error. |
| PositionValue | OUTPUT | DINT | 0 | Current position value |
| MeasuredValue | OUTPUT | REAL | 0.0 | Current measured value for frequency, period duration or velocity (depending on configuration)  Either MeasuredValue or CompleteSSIFrame is valid, depending on the parameter assignment in the technology object under "Measured value". |
| CompleteSSIFrame | OUTPUT | DWORD | 0 | Last received complete SSI frame (least significant 32 bits)  Either MeasuredValue or CompleteSSIFrame is valid, depending on the parameter assignment in the technology object under "Measured value". |
| CompareMeasuredValue | OUTPUT | BOOL | FALSE | Status bit:   FALSE: Operating mode "Use position value (SSI absolute value) as reference"; position value is used as reference  TRUE: Operating mode "Use measured value as reference"; measured value is used as reference |

## Static tags SSI_Absolute_Encoder (S7-1500)

| Tag |  | Data type | Default | Access | Description |
| --- | --- | --- | --- | --- | --- |
| NewReferenceValue0 |  | DINT | L#0 | Write | New comparison value 0 in operating mode "Use position value (SSI absolute value) as reference" |
| NewReferenceValue1 |  | DINT | L#10 | Write | New comparison value 1 in operating mode "Use position value (SSI absolute value) as reference" |
| NewReferenceValue0_M |  | REAL | L#0.0 | Write | New comparison value 0 in operating mode "Use measured value as reference" |
| NewReferenceValue1_M |  | REAL | L#10.0 | Write | New comparison value 1 in operating mode "Use measured value as reference" |
| CurReferenceValue0 |  | DINT | L#0 | Read | Current comparison value 0 in operating mode "Use position value (SSI absolute value) as reference" |
| CurReferenceValue1 |  | DINT | L#10 | Read | Current comparison value 1 in operating mode "Use position value (SSI absolute value) as reference" |
| CurReferenceValue0_M |  | REAL | L#0.0 | Read | Current comparison value 0 in operating mode "Use measured value as reference" |
| CurReferenceValue1_M |  | REAL | L#10.0 | Read | Current comparison value 1 in operating mode "Use measured value as reference" |
| AdditionalErrorID |  | DWORD | W#16#0000 | Read | Error information of an internal instruction, e.g.,RDREC |
| UserCmdFlags |  | STRUCT | - |  |  |
|  | SetReferenceValue0 | BOOL | FALSE | Write | Set comparison value 0 |
|  | SetReferenceValue1 | BOOL | FALSE | Write | Set comparison value 1 |
|  | SetDQ0 | BOOL | FALSE | Write | Set digital output DQ0 |
|  | SetDQ1 | BOOL | FALSE | Write | Set digital output DQ1 |
|  | ManualCtrlDQ0 | BOOL | FALSE | Write | Enable setting of digital output DQ0.  TRUE: SetDQ0 sets DQ0<sup>1</sup>  FALSE: Setting not enabled |
|  | ManualCtrlDQ1 | BOOL | FALSE | Write | Enable setting of digital output DQ1:  TRUE: SetDQ1 sets DQ1<sup>1</sup>  FALSE: Setting not enabled |
| UserStatusFlags |  | STRUCT | - |  |  |
|  | StatusDI0 | BOOL | FALSE | Read | Current status of digital input DI0 |
|  | StatusDI1 | BOOL | FALSE | Read | Current status of digital input DI1 |
|  | StatusDQ0 | BOOL | FALSE | Read | Current status of digital output DQ0 |
|  | StatusDQ1 | BOOL | FALSE | Read | Current status of digital output DQ1 |
| <sup>1 </sup> The instruction sets the TM_CTRL_DQm bit to FALSE. in the control interface of the module. The static tag SetDQm acts on the control bit SET_DQm. |  |  |  |  |  |

## Error codes of parameter ErrorID (S7-1500)

| Error code  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| **Error messages from technology module** |  |
| 80A1 | POWER_ERROR from feedback interface: Incorrect supply voltage L+ |
| 80A2 | ENC_ERROR from feedback interface: Incorrect encoder signal |
| 80A3 | LD_ERROR from feedback interface: Error when loading via control interface |
| **Error messages of the instruction** SSI_Absolute_Encoder |  |
| 80B8 | New comparison value 0 does not meet the following conditions:  - Low counting limit &lt;= comparison value 0 &lt;= high counting limit - Comparison value 0 &lt; comparison value 1 |
| 80B9 | New comparison value 1 does not meet the following conditions:  - Low counting limit &lt;= comparison value 1 &lt;= high counting limit - Comparison value 0 &lt; comparison value 1 |
| 80C0 | Instruction was called multiple times with the same instance (DB) |
| 80C1 | Communication with technology module failed (read data records): Error information of internal instruction RDREC saved in static tag AdditionalErrorID |
| 80C2 | Communication with technology module failed (write data records): Error information of internal instruction WRREC saved in static tag AdditionalErrorID |
| 80C5 | Reading of the current start information of the OB failed: Error information of internal instruction RD_SINFO saved in static tag AdditionalErrorID |
| 80C6 | Failed to get I/O addresses of the technology module: Error information of internal instruction RD_ADDR saved in static tag AdditionalErrorID |
| 80C7 | Module not inserted or no supply voltage L+ |
| 80C8 | Specified module is not permitted in the static tag Configuration.HWID |
