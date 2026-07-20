---
title: "SINAMICS Motion Control (S7-1200, S7-1500)"
package: TIAPortalSINATOenUS
topics: 9
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Motion Control (S7-1200, S7-1500)

This section contains information on the following topics:

- [BasicPosControl V3.0](#basicposcontrol-v30)
- [BasicPosControl V2.1](#basicposcontrol-v21)
- [BasicPosControl (former TO_BasicPos) V2](#basicposcontrol-former-to_basicpos-v2)
- [TO_BasicPos V1](#to_basicpos-v1)

## BasicPosControl V3.0

This section contains information on the following topics:

- [Description](#description)
- [Telegram enhancements](#telegram-enhancements)
- [Measuring unit selection](#measuring-unit-selection)
- [Adjusting Absolute encoders via BasicPosControl](#adjusting-absolute-encoders-via-basicposcontrol)

### Description

The BasicPosControl technology object V3.0 additionally supports positioning operations with SIEMENS telegram 112. The new telegram is available from firmware version V6.2 onwards (for example, S200 PN V6.2).

### Telegram enhancements

The structures of SIEMENS telegram 111 and SIEMENS telegram 112 are shown below to indicate the differences and enhancements.

#### SIEMENS telegram 111

The following SIEMENS telegram 111 extended functions are supported with all Sinamics S/G drives:

Telegram 111, positiong operation with extended functions

| PZD01 | PZD02 | PZD03 | PZD04 | PZD05 | PZD06 | PZD07 | PZD08 | PZD09 | PZD10 | PZD11 | PZD12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STW1 | POS_STW1 | POS_STW2 | STW2 | OVERRIDE | MDI_TARPOS |  | MDI_VELOCITY |  | MDI_ACC | MDI_DEC | Free |
| ZSW1 | POS_ZSW1 | POS_ZSW2 | ZSW2 | MELDW | XIST_A |  | NIST_B |  | FAULT_CODE | WARN_CODE | Free |

#### SIEMENS telegram 112

The following SIEMENS telegram 112 extended functions are supported with SINAMICS S/G FW V6.2 onwards:

| PZD01 | PZD02 | PZD03 | PZD04 | PZD05 | PZD06 | PZD07 | PZD08 | PZD09 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STW1 | POS_STW1 | POS_STW2 | STW2 | OVERRIDE | MDI_TARPOS_F (Float) |  | MDI_VELOCITY_F (Float) |  |
| ZSW1 | POS_ZSW1 | POS_ZSW2 | ZSW2 | OVERRIDE | XIST_F (Float) |  | VIST_F (Float) |  |

| PZD10 | PZD11 | PZD12 | PZD13 | PZD14 | PZD15 | PZD16 | PZD17 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MDI_ACC_F (Float) |  | MDI_DEC_F (Float) |  | RESERVED |  | REF_COORDINATE |  |
| MELDW | FAULT_CODE | WARN_CODE | - |  |  |  |  |

### Measuring unit selection

SINAMICS S/G FW V6.2 onwards which supports Basic positioner, allows user to select physical measuring units for velocity and position, also the axis type and leadscrew pitch on the drive side. For accurate positioning of the drive axis, this configuration must be synchronized in the technology object.

### Adjusting Absolute encoders via BasicPosControl

TO BasicPosControl V3 used with SIEMENS telegram 112, allows user to perform encoder adjustment for "Absolute encoders" by using a new mode in the BasicPosControl function block. To achieve this, set the function block input “ModePos” value to 9 (Operating mode: 9 = Absolute encoder adjustment).

## BasicPosControl V2.1

### Description

You can use the SINAMICS "BasicPosControl" instruction if the basic positioner function module is used in the connected SINAMICS drive. "BasicPosControl" is used to cyclically control a SINAMICS drive with the SINAMICS S/G/V basic positioner technology.

> **Note**
>
> Because of the various EPos modes, there is a special mode input - the "ModePos" input. The individual operating modes are selected by means of this input. Due to the structure of the EPos, it is not possible to select different operating modes simultaneously. It is possible at any time, however, to switch to different modes within an operating mode such as switching from setup mode to absolute positioning.

> **Note**
>
> To control all additional bits in the setpoint direction without an explicit input, from TIA Portal/Startdrive V14 an additional configuration input is available - the "ConfigEPos" input. Using this input, it is now possible to activate basic device functions such as OFF2/OFF3 - or also EPos functions such as continuous setpoint transfer - WITHOUT having to intervene in the instance data block using a SLICE access.

> **Note**
>
> When configuring the SINAMICS drive, you must ensure that the standard type 111 telegram is selected for communication.

### Parameter

The table below shows the parameters of the BasicPosControl instruction

| Parameter | Declaration | Type | Default […] | Meaning |
| --- | --- | --- | --- | --- |
| ModePos | INPUT | INT | 0 | Operating mode:               1 = relative positioning              2 = absolute positioning              3 = positioning as setup              4 = homing procedure              5 = set home position              6 = traversing block 0 – 15/63 (G120/S120)              7 = jog              8 = jog incremental |
| EnableAxis | INPUT | BOOL | 0 | Switch command: 0 = OFF1, 1 = ON |
| CancelTraversing | INPUT | BOOL | 1 | 0 = reject active traversing job, 1 = do not reject |
| IntermediateStop | INPUT | BOOL | 1 | 0 = active traversing command is interrupted, 1 = no intermediate stop |
| Positive | INPUT | BOOL | 0 | Positive direction |
| Negative | INPUT | BOOL | 0 | Negative direction |
| Jog1 | INPUT | BOOL | 0 | Jog signal source 1 |
| Jog2 | INPUT | BOOL | 0 | Jog signal source 2 |
| FlyRef | INPUT | BOOL | 0 | 0 = deselect flying homing, 1 = select flying homing |
| AckError | INPUT | BOOL | 0 | Acknowledgment of faults |
| ExecuteMode | INPUT | BOOL | 0 | Activate traversing job/setpoint acceptance/activate reference function |
| Position | INPUT | LReal | 0.0 [selected unit] | Position setpoint in [selected unit] for operating mode direct setpoint specification (MDI) or traversing block number for operating mode Traversing block.  The unit can be configured in the BasicPosControl basic parameter settings.  The selected unit is automatically converted to the corresponding value in [LU] by the function block before the data transfer to the drive. |
| Velocity | INPUT | LReal | 0.0 [selected unit] | Velocity setpoint in [selected unit] for MDI operating mode.   The unit can be configured in the BasicPosControl basic parameter settings.   The selected unit is automatically converted to the corresponding value in [1000 LU/min] by the function block before the data transfer to the drive. |
| OverV | INPUT | INT | 100[%] | Velocity override for all operating modes effective: 0-199% |
| OverAcc | INPUT | INT | 100[%] | Acceleration override effective 0-100% |
| OverDec | INPUT | INT | 100[%] | Deceleration override effective 0-100% |
| ConfigEPos | INPUT | DWORD | 3h | With this interface, the following bit functions of telegram 111 can be transmitted: Bit0 = STW1.1 (OFF2: 1 = no pulse inhibit)   Bit1 = STW1.2 (OFF3: 1 = no pulse inhibit)  Bit2 = EPosSTW2.14 (Software limit switch: 1 = active)  Bit3 = EPosSTW2.15 (Stop output cam: 1 = active)  Bit4 = EPosSTW2.11 (reserved)  Bit5 = EPosSTW2.10 (reserved)   Bit6 = EPosSTW2.2 (signal source reference mark)  Bit7 = STW1.13 (External block change)  Bit8 = EPosSTW1.12 (continuous setpoint transfer MDI: 1 = active)  Bit9 = STW2.0 (reserved)  Bit10 = STW2.1 (reserved) Bit11 = STW2.2 (reserved)  Bit12 = STW2.3 (reserved) Bit13 = STW2.4 (reserved)  Bit14 = STW2.7 (reserved) Bit15 = STW1.12 (reserved)  Bit16 = STW1.14 (reserved)  Bit17 = STW1.15 (reserved)  Bit18 = EPosSTW1.6 (reserved)  Bit19 = EPosSTW1.7 (reserved)  Bit20 = EPosSTW1.11 (reserved)  Bit21 = EPosSTW1.13 (reserved)  Bit22 = EPosSTW2.3 (reserved)  Bit23 = EPosSTW2.4 (reserved)  Bit24 = EPosSTW2.6 (reserved)  Bit25 = EPosSTW2.7 (reserved)  Bit26 = EPosSTW2.12 (reserved) Bit27 = EPosSTW2.13 (reserved)  Bit28 = STW2.5 (reserved)  Bit29 = STW2.6 (reserved)  Bit30 = STW2.8 (travel to fixed endstop: 1 = active)  Bit31 = STW2.9 (reserved) |
| UserSetPZD | INPUT | WORD | 0 | Define the PZD12 value. The PZD12 value is sent to drive. |
| AxisEnabled | OUTPUT | BOOL | 0 | Drive is ready and switched on |
| AxisPosOk | OUTPUT | BOOL | 0 | Target position of the axis reached |
| AxisSpFixed | OUTPUT | BOOL | 0 | Fixed setpoint of the axis |
| AxisRef | OUTPUT | BOOL | 0 | Home position set |
| AxisWarn | OUTPUT | BOOL | 0 | Alarm of the drive effective |
| AxisError | OUTPUT | BOOL | 0 | Drive is faulted |
| Lockout | OUTPUT | BOOL | 0 | Switching on inhibited |
| ActVelocity | OUTPUT | LReal | 0.0 [selected unit] | Current actual velocity is displayed in selected unit.  The unit can be configured in the BasicPosControl basic parameter settings.  The function block automatically converts the received drive value from [LU/min] to the selected unit before displaying. |
| ActPosition | OUTPUT | LReal | 0.0 [selected unit] | Current actual position is displayed in selected unit.   The unit can be configured in the BasicPosControl basic parameter settings.  The function block automatically converts the received drive value from [LU] to the selected unit before displaying. |
| ActMode | OUTPUT | INT | 0 | Currently active operating mode |
| EPosZSW1 | OUTPUT | WORD | 0 | Status of the EPos ZSW1 (bit-granular) |
| EPosZSW2 | OUTPUT | WORD | 0 | Status of the EPos ZSW2 (bit-granular) |
| ActWarn | OUTPUT | WORD | 0 | Current alarm number |
| ActFault | OUTPUT | WORD | 0 | Current fault number |
| Error | OUTPUT | BOOL | 0 | 1 = group fault present |
| Status | OUTPUT | INT | 0 | 16#7002: No fault – block is working   16#8401: Drive fault   16#8402: Switching on inhibited   16#8403: Flying homing could not start  16#8600: Error DPRD_DAT   16#8601: Error DPWR_DAT   16#8202: Incorrect operating mode selected   16#8203: Incorrect setpoints parameterized   16#8204: Incorrect traversing block number selected |
| DiagID | OUTPUT | WORD | 0 | Expanded communication error → SFB call error |
| UserReceivePZD | OUTPUT | WORD | 0 | The PZD12 value received from the drive |

For more information, refer "Using technology object" -> "SINAMICS" chapter in TIA Portal online help.

## BasicPosControl (former TO_BasicPos) V2

### Description

You can use the SINAMICS "BasicPosControl" instruction if the basic positioner function module is used in the connected SINAMICS drive. "BasicPosControl" is used to cyclically control a SINAMICS drive with the SINAMICS S/G/V basic positioner technology.

> **Note**
>
> Because of the various EPos modes, there is a special mode input - the "ModePos" input. The individual operating modes are selected by means of this input. Due to the structure of the EPos, it is not possible to select different operating modes simultaneously. It is possible at any time, however, to switch to different modes within an operating mode such as switching from setup mode to absolute positioning.

> **Note**
>
> To control all additional bits in the setpoint direction without an explicit input, from TIA Portal/Startdrive V14 an additional configuration input is available - the "ConfigEPos" input. Using this input, it is now possible to activate basic device functions such as OFF2/OFF3 - or also EPos functions such as continuous setpoint transfer - WITHOUT having to intervene in the instance data block using a SLICE access.

> **Note**
>
> When configuring the SINAMICS drive, you must ensure that the standard type 111 telegram is selected for communication.

### Parameter

The table below shows the parameters of the BasicPosControl instruction.

| Parameter | Declaration | Type | Default[…] | Meaning |
| --- | --- | --- | --- | --- |
| ModePos | INPUT | INT | 0 | Operating mode:               1 = relative positioning              2 = absolute positioning              3 = positioning as setup              4 = homing procedure              5 = set home position              6 = traversing block 0 – 15/63 (G120/S120)              7 = jog              8 = jog incremental |
| EnableAxis | INPUT | BOOL | 0 | Switch command: 0 = OFF1, 1 = ON |
| CancelTraversing | INPUT | BOOL | 1 | 0 = reject active traversing job, 1 = do not reject |
| IntermediateStop | INPUT | BOOL | 1 | 0 = active traversing command is interrupted, 1 = no intermediate stop |
| Positive | INPUT | BOOL | 0 | Positive direction |
| Negative | INPUT | BOOL | 0 | Negative direction |
| Jog1 | INPUT | BOOL | 0 | Jog signal source 1 |
| Jog2 | INPUT | BOOL | 0 | Jog signal source 2 |
| FlyRef | INPUT | BOOL | 0 | 0 = deselect flying homing, 1 = select flying homing |
| AckError | INPUT | BOOL | 0 | Acknowledgement of faults |
| ExecuteMode | INPUT | BOOL | 0 | Activate traversing job/setpoint acceptance/activate reference function |
| Position | INPUT | LReal | 0.0 [selected unit] | Position setpoint in [selected unit] for operating mode direct setpoint specification (MDI) or traversing block number for operating mode Traversing block.  The unit can be configured in the BasicPosControl basic parameter settings.  The selected unit is automatically converted to the corresponding value in [LU] by the function block before the data transfer to the drive. |
| Velocity | INPUT | LReal | 0.0 [selected unit] | Velocity setpoint in [selected unit] for MDI operating mode.   The unit can be configured in the BasicPosControl basic parameter settings.   The selected unit is automatically converted to the corresponding value in [1000 LU/min] by the function block before the data transfer to the drive. |
| OverV | INPUT | INT | 100[%] | Velocity override for all operating modes effective: 0-199% |
| OverAcc | INPUT | INT | 100[%] | Acceleration override effective 0-100% |
| OverDec | INPUT | INT | 100[%] | Deceleration override effective 0-100% |
| ConfigEPos | INPUT | DWORD | 3h | With this interface, the following bit functions of telegram 111 can be transmitted: Bit0 = STW1.1 (OFF2: 1 = no pulse inhibit)   Bit1 = STW1.2 (OFF3: 1 = no pulse inhibit)  Bit2 = EPosSTW2.14 (Software limit switch: 1 = active)  Bit3 = EPosSTW2.15 (Stop output cam: 1 = active)  Bit4 = EPosSTW2.11 (reserved)  Bit5 = EPosSTW2.10 (reserved)   Bit6 = EPosSTW2.2 (signal source reference mark)  Bit7 = STW1.13 (External block change)  Bit8 = EPosSTW1.12 (continuous setpoint transfer MDI: 1 = active)  Bit9 = STW2.0 (reserved)  Bit10 = STW2.1 (reserved) Bit11 = STW2.2 (reserved)  Bit12 = STW2.3 (reserved) Bit13 = STW2.4 (reserved)  Bit14 = STW2.7 (reserved) Bit15 = STW1.12 (reserved)  Bit16 = STW1.14 (reserved)  Bit17 = STW1.15 (reserved)  Bit18 = EPosSTW1.6 (reserved)  Bit19 = EPosSTW1.7 (reserved)  Bit20 = EPosSTW1.11 (reserved)  Bit21 = EPosSTW1.13 (reserved)  Bit22 = EPosSTW2.3 (reserved)  Bit23 = EPosSTW2.4 (reserved)  Bit24 = EPosSTW2.6 (reserved)  Bit25 = EPosSTW2.7 (reserved)  Bit26 = EPosSTW2.12 (reserved) Bit27 = EPosSTW2.13 (reserved)  Bit28 = STW2.5 (reserved)  Bit29 = STW2.6 (reserved)  Bit30 = STW2.8 (travel to fixed endstop: 1 = active)  Bit31 = STW2.9 (reserved) |
| AxisEnabled | OUTPUT | BOOL | 0 | Drive is ready and switched on |
| AxisPosOk | OUTPUT | BOOL | 0 | Target position of the axis reached |
| AxisSpFixed | OUTPUT | BOOL | 0 | Fixed setpoint of the axis |
| AxisRef | OUTPUT | BOOL | 0 | Home position set |
| AxisWarn | OUTPUT | BOOL | 0 | Alarm of the drive effective |
| AxisError | OUTPUT | BOOL | 0 | Drive is faulted |
| Lockout | OUTPUT | BOOL | 0 | Switching on inhibited |
| ActVelocity | OUTPUT | LReal | 0.0 [selected unit] | Current actual velocity is displayed in selected unit.  The unit can be configured in the BasicPosControl basic parameter settings.  The function block automatically converts the received drive value from [LU/min] to the selected unit before displaying. |
| ActPosition | OUTPUT | LReal | 0.0 [selected unit] | Current actual position is displayed in selected unit.   The unit can be configured in the BasicPosControl basic parameter settings.  The function block automatically converts the received drive value from [LU] to the selected unit before displaying. |
| ActMode | OUTPUT | INT | 0 | Currently active operating mode |
| EPosZSW1 | OUTPUT | WORD | 0 | Status of the EPos ZSW1 (bit-granular) |
| EPosZSW2 | OUTPUT | WORD | 0 | Status of the EPos ZSW2 (bit-granular) |
| ActWarn | OUTPUT | WORD | 0 | Current alarm number |
| ActFault | OUTPUT | WORD | 0 | Current fault number |
| Error | OUTPUT | BOOL | 0 | 1 = group fault present |
| Status | OUTPUT | INT | 0 | 16#7002: No fault – block is working   16#8401: Drive fault   16#8402: Switching on inhibited   16#8403: Flying homing could not start  16#8600: Error DPRD_DAT   16#8601: Error DPWR_DAT   16#8202: Incorrect operating mode selected   16#8203: Incorrect setpoints parameterized   16#8204: Incorrect traversing block number selected |
| DiagID | OUTPUT | WORD | 0 | Expanded communication error → SFB call error |

For more information, refer "Using technology object" -> "SINAMICS" chapter in TIA Portal online help.

## TO_BasicPos V1

### Description

You can use the SINAMICS "TO_BasicPos" instruction if the basic positioner function module is used in the connected SINAMICS drive. "TO_BasicPos" is used to cyclically control a SINAMICS drive with the SINAMICS S/G/V basic positioner technology.

> **Note**
>
> Because of the various EPos modes, there is a special mode input - the "ModePos" input. The individual operating modes are selected by means of this input. Due to the structure of the EPos, it is not possible to select different operating modes simultaneously. It is possible at any time, however, to switch to different modes within an operating mode such as switching from setup mode to absolute positioning.

> **Note**
>
> To control all additional bits in the setpoint direction without an explicit input, from TIA Portal/Startdrive V14 an additional configuration input is available - the "ConfigEPos" input. Using this input, it is now possible to activate basic device functions such as OFF2/OFF3 - or also EPos functions such as continuous setpoint transfer - WITHOUT having to intervene in the instance data block using a SLICE access.

> **Note**
>
> When configuring the SINAMICS drive, you must ensure that the standard type 111 telegram is selected for communication.

### Parameter

The table below shows the parameters of the TO_BasicPos instruction.

| Parameter | Declaration | Type | Default[…] | Meaning |
| --- | --- | --- | --- | --- |
| ModePos | INPUT | INT | 0 | Operating mode:               1 = relative positioning              2 = absolute positioning              3 = positioning as setup              4 = homing procedure              5 = set home position              6 = traversing block 0 – 15/63 (G120/S120)              7 = jog              8 = jog incremental |
| EnableAxis | INPUT | BOOL | 0 | Switch command: 0 = OFF1, 1 = ON |
| CancelTraversing | INPUT | BOOL | 1 | 0 = reject active traversing job, 1 = do not reject |
| IntermediateStop | INPUT | BOOL | 1 | 0 = active traversing command is interrupted, 1 = no intermediate stop |
| Positive | INPUT | BOOL | 0 | Positive direction |
| Negative | INPUT | BOOL | 0 | Negative direction |
| Jog1 | INPUT | BOOL | 0 | Jog signal source 1 |
| Jog2 | INPUT | BOOL | 0 | Jog signal source 2 |
| FlyRef | INPUT | BOOL | 0 | 0 = deselect flying homing, 1 = select flying homing |
| AckError | INPUT | BOOL | 0 | Acknowledgement of faults |
| ExecuteMode | INPUT | BOOL | 0 | Activate traversing job/setpoint acceptance/activate reference function |
| Position | INPUT | DINT | 0[LU] | Position setpoint in [LU] for operating mode Direct setpoint specification/MDI OR traversing block number for operating mode traversing block |
| Velocity | INPUT | DINT | 0[LU/min] | Velocity in [LU/min] for MDI operating mode. |
| OverV | INPUT | INT | 100[%] | Velocity override for all operating modes effective: 0-199% |
| OverAcc | INPUT | INT | 100[%] | Acceleration override effective 0-100% |
| OverDec | INPUT | INT | 100[%] | Deceleration override effective 0-100% |
| ConfigEPos | INPUT | DWORD | 3h | With this interface, the following bit functions of telegram 111 can be transmitted: Bit0 = STW1.1 (OFF2: 1 = no pulse inhibit)   Bit1 = STW1.2 (OFF3: 1 = no pulse inhibit)  Bit2 = EPosSTW2.14 (Software limit switch: 1 = active)  Bit3 = EPosSTW2.15 (Stop output cam: 1 = active)  Bit4 = EPosSTW2.11 (reserved)  Bit5 = EPosSTW2.10 (reserved)   Bit6 = EPosSTW2.2 (signal source reference mark)  Bit7 = STW1.13 (External block change)  Bit8 = EPosSTW1.12 (continuous setpoint transfer MDI: 1 = active)  Bit9 = STW2.0 (reserved)  Bit10 = STW2.1 (reserved) Bit11 = STW2.2 (reserved)  Bit12 = STW2.3 (reserved) Bit13 = STW2.4 (reserved)  Bit14 = STW2.7 (reserved) Bit15 = STW1.12 (reserved)  Bit16 = STW1.14 (reserved)  Bit17 = STW1.15 (reserved)  Bit18 = EPosSTW1.6 (reserved)  Bit19 = EPosSTW1.7 (reserved)  Bit20 = EPosSTW1.11 (reserved)  Bit21 = EPosSTW1.13 (reserved)  Bit22 = EPosSTW2.3 (reserved)  Bit23 = EPosSTW2.4 (reserved)  Bit24 = EPosSTW2.6 (reserved)  Bit25 = EPosSTW2.7 (reserved)  Bit26 = EPosSTW2.12 (reserved) Bit27 = EPosSTW2.13 (reserved)  Bit28 = STW2.5 (reserved)  Bit29 = STW2.6 (reserved)  Bit30 = STW2.8 (travel to fixed endstop: 1 = active)  Bit31 = STW2.9 (reserved) |
| AxisEnabled | OUTPUT | BOOL | 0 | Drive is ready and switched on |
| AxisPosOk | OUTPUT | BOOL | 0 | Target position of the axis reached |
| AxisRef | OUTPUT | BOOL | 0 | Home position set |
| AxisWarn | OUTPUT | BOOL | 0 | Alarm of the drive effective |
| AxisError | OUTPUT | BOOL | 0 | Drive is faulted |
| Lockout | OUTPUT | BOOL | 0 | Switching on inhibited |
| ActVelocity | OUTPUT | DINT | 0 | Current velocity (standardized 40000000h = 100% p2000) |
| ActPosition | OUTPUT | DINT | 0[LU] | Current position in LU |
| ActMode | OUTPUT | INT | 0 | Currently active operating mode |
| EPosZSW1 | OUTPUT | WORD | 0 | Status of the EPos ZSW1 (bit-granular) |
| EPosZSW2 | OUTPUT | WORD | 0 | Status of the EPos ZSW2 (bit-granular) |
| ActWarn | OUTPUT | WORD | 0 | Current alarm number |
| ActFault | OUTPUT | WORD | 0 | Current fault number |
| Error | OUTPUT | BOOL | 0 | 1 = group fault present |
| Status | OUTPUT | INT | 0 | 16#7002: No fault – block is working   16#8401: Drive fault   16#8402: Switching on inhibited   16#8403: Flying homing could not start  16#8600: Error DPRD_DAT   16#8601: Error DPWR_DAT   16#8202: Incorrect operating mode selected   16#8203: Incorrect setpoints parameterized   16#8204: Incorrect traversing block number selected |
| DiagID | OUTPUT | WORD | 0 | Expanded communication error → SFB call error |

For more information, refer "Using technology object" -> "SINAMICS" chapter in TIA Portal online help.
