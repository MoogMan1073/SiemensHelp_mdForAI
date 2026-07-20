---
title: "SINAMICS Instructions"
package: TIAPortalSINAenUS
topics: 66
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Instructions

This section contains information on the following topics:

- [Function block SinaPos](#function-block-sinapos)
- [Function block SinaSpeed](#function-block-sinaspeed)
- [Function block SinaPara](#function-block-sinapara)
- [Function block SinaParaS](#function-block-sinaparas)
- [Function block Sinalnfeed](#function-block-sinalnfeed)

## Function block SinaPos

This section contains information on the following topics:

- [Description](#description)
- [Calling OBs](#calling-obs)
- [Called blocks](#called-blocks)
- [Description of functions](#description-of-functions)
- [Input interface of the SinaPos](#input-interface-of-the-sinapos)
- [Description of the configuration input "ConfigEPos"](#description-of-the-configuration-input-configepos)
- [Output interface of the SinaPos](#output-interface-of-the-sinapos)
- [Operating mode selection of EPOS with SinaPos](#operating-mode-selection-of-epos-with-sinapos)
- [Relative positioning](#relative-positioning)
- [Absolute positioning](#absolute-positioning)
- [Setup mode](#setup-mode)
- [Continuous setpoint acceptance](#continuous-setpoint-acceptance)
- [Referencing – reference point approach](#referencing-reference-point-approach)
- [Homing - set home position](#homing---set-home-position)
- [Traversing blocks](#traversing-blocks)
- [Jog](#jog)
- [Jog - incremental](#jog---incremental)
- [Flying homing](#flying-homing)
- [Operating mode change based on the ModePos values](#operating-mode-change-based-on-the-modepos-values)
- [Error handling of the SinaPos function block](#error-handling-of-the-sinapos-function-block)
- [EPOS telegram 111](#epos-telegram-111)

### Description

#### SinaPos block

![Function block SinaPos FB300](images/117879213067_DV_resource.Stream@PNG-en-US.png)

Function block SinaPos FB300

#### Description

The corresponding instance DB is automatically created when the FB300 (SINA_POS) is integrated.

Can be used in the following CPUs: SIMATIC S7-1200/1500

### Calling OBs

#### Calling OBs

The block can be alternatively installed in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

### Called blocks

#### Called blocks

DPRD_DAT/SFC14

DPWR_DAT/SFC15

### Description of functions

#### Function description - general

The function block can be used to cyclically activate a SINAMICS drive with the SINAMICS S/G basic positioner technology.

> **Note**
>
> Because of the various EPos modes, there is a special mode input – the "ModePos" input. The individual operating modes are selected by means of this input. Due to the structure of the EPos, it is not possible to select different operating modes simultaneously. It is possible at any time, however, to switch to different modes within an operating mode such as switching from setup mode to absolute positioning.
>
> For detailed information, see [EPOS telegram 111](#epos-telegram-111).

> **Note**
>
> To control all additional bits in the setpoint direction without an explicit input, from TIA Portal / Startdrive V14 an additional configuration input is available – the "ConfigEPos" input. Using this input, it is now possible to activate basic device functions such as OFF2/OFF3 – or also EPos functions such as continuous setpoint transfer – WITHOUT having to intervene in the instance data block using a SLICE access.

> **Note**
>
> When configuring the SINAMICS drive, you must ensure that the standard type 111 telegram is selected for communication.

### Input interface of the SinaPos

#### Input interface SINA_POS

The input interface comprises 19 inputs in different data formats.

During the initial configuration of the function block, these are set up with initial values. An overview of the input interface is provided below:

| Input signal | Type | Default[…] | Meaning |
| --- | --- | --- | --- |
| ModePos | INT | 0 | Operating mode:               1 = relative positioning              2 = absolute positioning              3 = positioning as setup              4 = homing procedure              5 = set home position              6 = traversing block 0 – 15/63 (G120/S120)              7 = jog              8 = jog incremental |
| EnableAxis | BOOL | 0 | Switch command: 0 = OFF1, 1 = ON |
| CancelTraversing | BOOL | 1 | 0 = reject active traversing job, 1 = do not reject |
| IntermediateStop | BOOL | 1 | 0 = active traversing command is interrupted, 1 = no intermediate stop |
| Positive | BOOL | 0 | Positive direction |
| Negative | BOOL | 0 | Negative direction |
| Jog1 | BOOL | 0 | Jog signal source 1 |
| Jog2 | BOOL | 0 | Jog signal source 2 |
| FlyRef | BOOL | 0 | 0 = deselect flying homing, 1 = select flying homing |
| AckError | BOOL | 0 | Acknowledgement of faults |
| ExecuteMode | BOOL | 0 | Activate traversing job/setpoint acceptance/activate reference function |
| Position | DINT | 0[LU] | Position setpoint in [LU] for operating mode Direct setpoint specification/MDI OR traversing block number for operating mode Traversing block |
| Velocity | DINT | 0[LU/min] | Velocity in [LU/min] for MDI operating mode |
| OverV | INT | 100[%] | Velocity override for all operating modes effective: 0-199% |
| OverAcc | INT | 100[%] | Acceleration override effective 0-100% |
| OverDec | INT | 100[%] | Deceleration override effective 0-100% |
| ConfigEPos | DWORD | 3h | For a detailed description, see [Relative positioning](#relative-positioning) |
| HWIDSTW | HW_IO | 0 | Symbolic name or HW ID on the SIMATIC S7-1200/1500 of the setpoint slot |
| HWIDZSW | HW_IO | 0 | Symbolic name or HW ID on the SIMATIC S7-1200/1500 of the actual value slot |

### Description of the configuration input "ConfigEPos"

#### Configuration input "ConfigEPos"

| ConfigEPos | Meaning | PZD | Interconnection in the drive (telegram 111) | Default |
| --- | --- | --- | --- | --- |
| Bit0 | OFF2 (1 = no pulse disable) | 1 | r2090.1 = p 844[0] | 1 |
| Bit1 | OFF3 (1 = no ramp stop) | 1 | r2090.2 = p 848[0] | 1 |
| Bit2 | Software limit switch (active = 1) | 3 | r2092.14 = p2582 | 0 |
| Bit3 | Stop cams (active = 1) | 3 | r2092.15 = p2568 | 0 |
| Bit4 | Measuring input edge evaluation | 3 | r2092.11 = p2511[0] | 0 |
| Bit5 | Measuring input selection | 3 | r2092.10 = p2510[0] | 0 |
| Bit6 | Signal source reference mark | 3 | r2092.2 = p2612 | 0 |
| Bit7 | External block change (by BUS) | 1 | r2090.13 = p2633 | 0 |
| Bit8 | Continuous setpoint acceptance MDI (active = 1) | 2 | r2091.12 = p2649 | 0 |
| Bit9 | DDS BIT0 | 4 | r2093.0 = 820[0] | 0 |
| Bit10 | DDS BIT1 | 4 | r2093.1 = 821[0] | 0 |
| Bit11 | DDS BIT2 | 4 | r2093.2 = 822[0] | 0 |
| Bit12 | DDS BIT3 | 4 | r2093.3 = 823[0] | 0 |
| Bit13 | DDS BIT4 | 4 | r2093.4 = 824[0] | 0 |
| Bit14 | Parking axis selection | 4 | r2093.7 = p897 | 0 |
| Bit15 |  |  |  |  |
| Bit16 | Reserve - can be used as required | 1 | r2090.14 | 0 |
| Bit17 | Reserve - can be used as required | 1 | r2090.15 | 0 |
| Bit18 | Reserve - can be used as required | 2 | r2091.6 | 0 |
| Bit19 | Reserve - can be used as required | 2 | r2091.7 | 0 |
| Bit20 | Reserve - can be used as required | 2 | r2091.11 | 0 |
| Bit21 | Reserve - can be used as required | 2 | r2091.13 | 0 |
| Bit22 | Reserve - can be used as required | 3 | r2092.3 | 0 |
| Bit23 | Reserve - can be used as required | 3 | r2092.4 | 0 |
| Bit24 | Reserve - can be used as required | 3 | r2092.6 | 0 |
| Bit25 | Reserve - can be used as required | 3 | r2092.7 | 0 |
| Bit26 | Reserve - can be used as required | 3 | r2092.12 | 0 |
| Bit27 | Reserve - can be used as required | 3 | r2092.13 | 0 |
| Bit28 | Reserve - can be used as required | 4 | r2093.5 | 0 |
| Bit29 | Reserve - can be used as required | 4 | r2093.6 | 0 |
| Bit30 | Reserve - can be used as required | 4 | r2093.8 | 0 |
| Bit31 | Reserve - can be used as required | 4 | r2093.9 | 0 |

### Output interface of the SinaPos

#### Output interface SINA_POS

The output interface comprises 16 outputs in different data formats.

During the initial configuration of the block, these are set up with initial values. Below the overview of the output interface:

| Output signal | Type | Default[…] | Meaning |
| --- | --- | --- | --- |
| AxisEnabled | BOOL | 0 | Drive is ready and switched on |
| AxisPosOk | BOOL | 0 | Target position of the axis reached |
| AxisSpFixed | BOOL | 0 | 1 = Setpoint is stationary (Note: Information dependent on SINAMICS firmware: 1. SINAMICS S/G120 FW <4.8/<4.7.9: Transfer of parameter **r2199.0** 2. SINAMICS S/G120 FW ≥ 4.8/≥ 4.7.9: Transfer of parameter **r2683.2** 3. SINAMICS V90 PN: Transfer of parameter **r2683.2** |
| AxisRef | BOOL | 0 | Home position set |
| AxisWarn | BOOL | 0 | Alarm of the drive effective |
| AxisError | BOOL | 0 | Drive is faulted |
| Lockout | BOOL | 0 | Switching on inhibited |
| ActVelocity | DINT | 0 | Current velocity (standardized 40000000h = 100% p2000) |
| ActPosition | DINT | 0[LU] | Current position in LU |
| ActMode | INT | 0 | Currently active operating mode |
| EPosZSW1 | WORD | 0 | Status of the EPos ZSW1 (bit-granular) |
| EPosZSW2 | WORD | 0 | Status of the EPos ZSW2 (bit-granular) |
| ActWarn | WORD | 0 | Current alarm number |
| ActFault | WORD | 0 | Current fault number |
| Error | BOOL | 0 | 1 = group fault present |
| Status | INT | 0 | 16#7002: No fault – block is working   16#8401: Drive fault   16#8402: Switching on inhibited   16#8403: Flying homing could not be started  16#8600: Error DPRD_DAT   16#8601: Error DPWR_DAT   16#8202: Incorrect operating mode selected   16#8203: Incorrect setpoints parameterized   16#8204: Incorrect traversing block number selected |
| DiagID | WORD | 0 | Expanded communication error → SFB call error |

### Operating mode selection of EPOS with SinaPos

#### General operating conditions

The axis is switched on via the input bit "EnableAxis" = 1. 1 is preassigned to OFF2 and OFF3 via the input "ConfigEPos" and do not have to be written for operation.

The axis is ready to be switched on if there is no active error – "AxisError"= "0" – and no switch-on inhibit – "Lockout" = "0". The checkback signal "AxisIEnabled" goes to "1" after switching "EnableAxis".

The "ModePos" input is decisive for the operating mode selection. The desired operating mode is selected by means of this input. It is therefore not possible to select several operating modes at the same time. It is possible, however, to change-over between various lower-level operating modes.

Example: Setup mode (ModePos=3) with on-the-fly change-over to absolute positioning (ModePos=2).

The input signals "CancelTraversing" and "IntermediateStop" are relevant in all operating modes except for jog and must be set to "1" to operate the EPos.

1. Setting the "CancelTraversing" bit to "0" leads to a ramp stop with 100% of the set delay. The job data is rejected and the axis can be assigned with a new job from the standstill. In this state, a mode change is possible.
2. Setting the "IntermediateStop" bit to "0" leads to a ramp stoppage of the axis with the currently applicable acceleration values. The job data is NOT rejected, which means that a setting of "1" allows the axis to continue its motion. It is possible to changes modes in a standstill.
3. The flying homing function can be selected and deselected in any operating mode other than the homing procedure mode at any time via the "FlyRef" input.

### Relative positioning

#### Relative positioning operating mode

The "Relative positioning" operating mode is implemented via the drive function "MDI relative positioning". It permits the position-controlled traversing of traversing paths via the integrated position controller of the SINAMICS drive.

1. Requirements:

   - The operating mode is selected with ModePos=1.
   - Device switched on via "EnableAxis".
   - The axis does not have to be homed or the encoder does not have to be adjusted.
   - The axis is in standstill if a mode higher than 3 is selected. It is possible to make a change within the MDI operating modes (1,2,3) at any time.
2. Sequence:

The traversing path and dynamic response are specified via the inputs "Position“, "Velocity", "OverV" (velocity override), "OverAcc" (acceleration override), "OverDec" (deceleration override).

The velocity override refers to "Velocity".

The operating conditions "CancelTraversing" and "IntermediateStop" must be set to "1". "Jog1" and "Jog2" have no effect and should be set to "0" (false).

In relative positioning, the direction of travel basically results from the sign of the traversing path.

Traversing is started by a positive edge to "ExecuteMode". The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2" (see [EPOS telegram 111](#epos-telegram-111) for details on the assignment of the status words).

The block acknowledges the successful reaching of the end of the traversing path "AxisPosOk". If a fault occurs during the traversing movement, the "Error" output signal is active.

> **Note**
>
> The currently running command can be replaced on-the-fly by a new command via "ExecuteMode". This is only possible for the operating modes of the "ModePos" 1,2,3.

#### Example of relative positioning

![Example of relative positioning](images/117988107915_DV_resource.Stream@PNG-en-US.png)

### Absolute positioning

#### Absolute positioning operating mode

The "Absolute positioning" operating mode is implemented via the drive function "MDI absolute positioning". It permits the position-controlled approach of absolute positions via the integrated position controller of the SINAMICS drive.

1. Requirements:

   - The operating mode is selected with ModePos=2.
   - The device is switched on via "EnableAxis".
   - The axis must be homed or the encoder must be adjusted.
   - The axis is in standstill if a mode higher than 3 is selected. It is possible to make a change within the MDI operating modes (1,2,3) at any time.
2. Sequence:

   - The traversing path and dynamic response are specified via the inputs "Position“, "Velocity", "OverV" (velocity override), "OverAcc" (acceleration override), "OverDec" (deceleration override).
   - The velocity override refers to Velocity.
   - The operating conditions "CancelTraversing" and "IntermediateStop" must be set to "1". Jog1 and Jog2 have no effect and must be set to "0".
   - In absolute positioning, the direction of travel basically results from the shortest path to the target position. The inputs "Positive " and "Negative" are "0".

> **Note**
>
> If a preferred direction to approach the target position is to be specified for a modulo axis, this can be performed with "Positive" or "Negative".
>
> Simultaneous selection of "Positive" and "Negative" immediately stops the axis with further warnings or faults. For a linear axis, the selection is not effective and is ignored.

Traversing is started by a positive edge to "ExecuteMode". The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2", see [EPOS telegram 111](#epos-telegram-111).

The block indicates the current processing of the command with Busy and acknowledges the successful reaching of the target position AxisPosOk and with Done. If a fault occurs during the traversing movement, the Error output signal is active.

> **Note**
>
> The currently running command can be replaced on-the-fly by a new command via "ExecuteMode". This is only possible for the operating modes of the "ModePos" 1,2,3.

#### Example of absolute positioning

![Example of absolute positioning](images/117988143755_DV_resource.Stream@PNG-en-US.png)

### Setup mode

#### Setup mode

The setup mode permits the position-controlled traversing of the axis in a positive or negative travel direction at constant speed without specification of a target position by means of the "MDI setup" drive function.

1. Requirements:

   - The operating mode is selected with ModePos = 3.
   - Switch on device via "EnableAxis".
   - The axis does not have to be homed or the encoder does not have to be adjusted
   - The axis is in standstill if a mode higher than 3 is selected. It is possible to make a change within the MDI operating modes (1,2,3) at any time.
2. Sequence:

   - The traversing path and dynamic response are specified via the inputs "Position“, "Velocity", "OverV" (velocity override), "OverAcc" (acceleration override), "OverDec" (deceleration override).
   - The operating conditions "CancelTraversing" and "IntermediateStop" must be set. "Jog1" and "Jog2" have no effect and must be set to "0".
   - The direction of travel is determined by Pos and Neg. Simultaneous selection is not permitted and will cause a fault.
   - Traversing is started by a positive edge to "ExecuteMode". The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2", see [EPOS telegram 111](#epos-telegram-111)).
   - The output signal "AxisPosOk" is set if the setup mode ends with Reject traverse task and the axis has come to a standstill.
   - If a fault occurs during the traversing movement, the Error output signal is active.

> **Note**
>
> The currently running command can be replaced on-the-fly by a new command via "ExecuteMode". This is only possible for the operating modes of the "ModePos" 1,2,3.

#### Example of setup mode

![Example of setup mode](images/117988205451_DV_resource.Stream@PNG-en-US.png)

### Continuous setpoint acceptance

#### Description

> **Note**
>
> **Continuous setpoint acceptance**
>
> The continuous setpoint acceptance is a special function of the preset positioning mode. By means of the parameter p2649 – which can be found in the standard telegram in the EPos STW1 BIT12 – it is possible to accept these values directly in the EPos WITHOUT edge triggering MDI setting values (position, speed, etc.).
>
> Access takes place via the input "ConfigEPos". Example: ConfigEPos = 3h (standard) -> ConfigEPos = 103h
>
> 259 = (3+(2<sup>8</sup>)) (with direct setpoint acceptance) = 103h.

### Referencing – reference point approach

#### Referencing – reference point approach

The operating mode allows the homing procedure of the axis in a positive or negative direction of travel with pre-configured velocity and homing mode and is activated via the drive function "Active homing".

1. Requirements:

   - The operating mode is selected with ModePos=4.
   - Switch on device via "EnableAxis".
   - The axis is at a standstill
2. Sequence:

   - The specification of the desired velocity is saved as velocity profile in the SINAMICS drive. Furthermore, the preset acceleration and deceleration values act in the traversing profile of the axis. The velocity override "OverV" effects the preconfigured traversing speed.
   - The operating conditions "CancelTraversing" and "IntermediateStop" must be set. Jog1 and Jog2 have no effect and must be set to "0".
   - The direction of travel is determined by Pos and Neg. Simultaneous selection is not permitted and will cause a fault.
   - Homing is started with a positive edge to "ExecuteMode".
   - Traversing is started by a positive edge to "ExecuteMode". The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2", see [EPOS telegram 111](#epos-telegram-111)).
   - The "AxisRef" output signal is set when the homing cam is found and evaluated accordingly.
   - If a fault occurs during the traversing movement, the "Error" output signal is output.

#### Simplified example of a reference point approach

![Simplified example of a reference point approach](images/117988297355_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> A detailed graphic representation of the reference point approach can be found in the Basic Positioner Function Manual, 01/2013, FW V4.6, A5E31759509A AA, and in the SINAMICS S120 Parameter Manual. (/4/)

### Homing - set home position

#### Homing – set home position

The Referencing – set reference point mode enables the referencing of the axis at an arbitrary position and is performed via the "Set reference point" drive function.

1. Requirements:

   - The operating mode is selected with ModePos=5.
   - The axis can be in closed-loop control, but must be at a standstill.
2. Sequence:

   - Axis is at a standstill and the home position is set by means of a positive edge for "ExecuteMode".
   - If a fault occurs while setting the home position, the Error output signal is output.

#### Example of set reference point

![Example of set reference point](images/117988332171_DV_resource.Stream@PNG-en-US.png)

### Traversing blocks

#### Traversing blocks

The Traversing blocks operating mode is implemented via the drive function "Traversing blocks". It permits the creation of automation programs, travel to fixed stop, and setting and resetting of outputs.

1. Requirements:

   - The operating mode is selected with ModePos=6.
   - Device switched on via "EnableAxis"
   - The axis is at a standstill
   - The axis must be homed or the encoder must be adjusted.
2. Sequence:

   > **Note**
   >
   > The selection of the traversing job to be started is set via the "Position" input. The value can only be between 0 and 63 (S120) or 0 and 15 (G120/S110). If the value is outside this range, an alarm is output at the block.

   - The job modes, target positions, and dynamic response are specified via the traversing block parameters in the SINAMICS drive. The "OverV" velocity override refers to the setpoint velocity stored in the traversing block.
   - The operating conditions "CancelTraversing" and "IntermediateStop" must be set to "1". "Jog1" and "Jog2" have no effect and should be set to "0".
   - The direction of travel that results depends on the job mode and the position setpoint that is set. The "Positive" and "Negative" inputs are not relevant in this case and must be set to "0".

> **Note**
>
> If, in the case of a modulo axis, a preferred direction is specified for the approach of the target position, this can be set by selecting "AbsPos" or "AbsNeg" as the job mode.

Traversing is started by a positive edge to "ExecuteMode". The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2", see [EPOS telegram 111](#epos-telegram-111)).

The block indicates the current processing of the command with "AxisEnabled" and acknowledges the successful reaching of the target position or the ending of the last task step with "AxisPosOk". If a fault occurs during the traversing movement, the "Error" output signal is active.

**Example of traversing blocks**

![Traversing blocks](images/117988458251_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The currently running command can be replaced on-the-fly by a new command via "ExecuteMode". This is only possible for the same operating mode.

### Jog

#### Jog

The Jog operating mode is implemented via the drive function "Jog". It permits the position-controlled, velocity-dependent traversing of axes via the integrated position controller of the SINAMICS drive.

1. Requirements:

   - The operating mode is selected with "ModePos" = 7.
   - Device switched on via "EnableAxis".
   - The axis is at a standstill
   - The axis does not have to be homed or adjusted.
2. Sequence:

   - The jog speed is specified via the Startdrive input screen or the acyclic communication for configuring the operating mode in the SINAMICS drive. For the dynamic response of the axis, the SINAMICS drive uses the set acceleration and delay in the SINAMICS drive.
   - The velocity override is also effective in the operating mode and is set via "OverV".
   - The operating conditions "CancelTraversing" and "IntermediateStop" are not relevant for the operating mode can be set to "1" by default.

> **Note**
>
> Jog1 and Jog2 are the signal sources for jog mode in EPOS. The direction of the traversing movement of the respective signal source is configured in the SINAMICS drive and is set by default to Jog1 = negative and Jog2 = positive.

The direction of travel for jogging depends on the velocity setpoint that is set.

The "Positive" and "Negative" inputs are not relevant for the operating mode can be set to "0" by default.

The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2" (see [EPOS telegram 111](#epos-telegram-111) for details on the assignment of the status words).

The block indicates the current processing of the command with Busy and acknowledges the ending of the jog function (Jog1 or Jog2 = 0) when the axis comes to a standstill with "AxisPosOK". If a fault occurs during the traversing movement, the Error output signal is active.

> **Note**
>
> The currently running command can be replaced on-the-fly by a new command via Jog1 or Jog2. This is only possible when you are remaining in one of the jog modes.

**Example of the jog mode**

![Jog](images/117988571531_DV_resource.Stream@PNG-en-US.png)

### Jog - incremental

#### Jog incremental

The Jog incremental operating mode is implemented via the drive function "Jog". It permits the position-controlled, path-dependent traversing of axes via the integrated position controller of the SINAMICS drive.

1. Requirements:

   - The operating mode is selected with ModePos = 8.
   - The device is switched on via "EnableAxis".
   - The axis is at a standstill
   - The axis does not have to be homed or adjusted.
2. Sequence:

   - The path and velocity are specified via the Startdrive input screen or the acyclic communication for configuring the operating mode in the SINAMICS drive. For the dynamic response of the axis, the SINAMICS drive uses the configuration of the acceleration and delay in the SINAMICS drive.
   - The velocity override is also effective in the operating mode and is set via "OverV".
   - The operating conditions "CancelTraversing" and "IntermediateStop" are not relevant for the operating mode can be set to "1" by default.

> **Note**
>
> Jog1 and Jog2 are the signal sources for jog mode in EPOS. The direction of the incremental traversing movement of the respective signal source is configured in the SINAMICS drive and is set to 1000LU (length units) in each case for incremental jogging.

The direction of travel for jogging depends on the path setpoint that is set.

The "Positive" and "Negative" inputs are not relevant for the operating mode can be set to "0" by default.

The current status of the active command can be monitored via "EPosZSW1 / EPosZSW2" (see [EPOS telegram 111](#epos-telegram-111) for details on the assignment of the PosZSW).

The block indicates the current processing of the command with "AxisEnabled" and acknowledges the ending of the jog function ("Jog1" or "Jog2" = 0) when the axis comes to a standstill with the bit AxisPosOk. If a fault occurs during the traversing movement, the "Error" output signal is active.

> **Note**
>
> The currently running command can be replaced on-the-fly by a new command via Jog1 or Jog2. This is only possible when you are remaining in one of the jog modes.

#### Example of incremental jogging

![Example of incremental jogging](images/117988684811_DV_resource.Stream@PNG-en-US.png)

### Flying homing

#### Flying homing

The operating mode Flying homing (passive homing) is implemented via the "Homing" drive function and is subordinate to most modes. It allows the SINAMICS drive to be re-homed during operation.

1. Requirements:

   - The "FlyRef" input is set to "1"
   - No selection of "ModePos" = 4 (homing procedure) and 5 (set home position)
2. Sequence:

The settings/prerequisites of the active operating mode apply. Flying homing can be selected or deselected at any time. When the set homing measuring input is reached, the setpoint and actual value are processed on the fly.

### Operating mode change based on the ModePos values

#### Operating mode change

The following graphic shows the principle possibilities of the operating mode change via ModePos.

![Operating mode change](images/117988801931_DV_resource.Stream@PNG-en-US.png)

### Error handling of the SinaPos function block

#### Function block error

When an error is detected, the "Error" group error is set and the "Status" error ID is set. The following errors that occur are monitored:

| Error number  Status | Cause | Remedy |
| --- | --- | --- |
| 16#7002 | No error |  |
| 16#8600 | Interruption of communication to the SINAMICS drive: Error DPRD_DAT | Check the communication connections/settings (see DiagId) |
| 16#8601 | Interruption of communication to the SINAMICS drive: Error DPWR_DAT | Check the communication connections/settings (see DiagId) |
| 16#8202 | Incorrect operating mode selected | Set "ModePos" from 1 to 8 |
| 16#8203 | Incorrect parameterization of the override inputs | Check the settings of the override inputs |
| 16#8204 | Invalid traversing block number | Enter traversing block number from 0 to 63 |
| 16#8401 | Fault message(s) in the SINAMICS drive | Evaluation of the error code at the "ActFault" output |
| 16#8402 | Switching on of SINAMICS drive inhibited active | Check for parking axis/encoder, active safety functions,  parameter p10 ≠ 0 |
| 16#8403 | Flying homing could not be started | Check for active alarms/errors in the drive |

- The faults of the SINAMICS drive are indicated via the FaultAct output and can be acknowledged (if possible) via the input AcktFlt.
- Active alarms do not have to be acknowledged. They are marked as cleared by the SINAMICS drive once the user has resolved the cause of the alarms.

  > **Note**
  >
  > The meanings of the displayed faults and alarms are described in the List Manual of the respective SINAMICS drive.
- The fault of the SFB call is displayed at the DiagID output and must be checked by the user. Once this fault has been cleared or is withdrawn, the group error "Error" is also withdrawn and the errors ID "Status" is updated.

> **Note**
>
> **If error message 8092(hex) occurs at the DIAGID output, the S7-1x00 firmware used must be checked.The following applies:**
>
> - S7-1200 -> firmware at least 2.x
> - S7-1500 -> firmware at least 1.1

### EPOS telegram 111

#### EPos telegram 111

| PZD | Assignment of the process data |
| --- | --- |
| PZD1 | Control word 1 |
| PZD2 | EPosSTW 1 |
| PZD3 | EPosSTW 2 |
| PZD4 | Control word 2 |
| PZD5 | Velocity override for all operating modes effective (4000HEX = 100%) |
| PZD6 | Position setpoint in [LU] for direct setpoint specification/MDI operating mode |
| PZD7 |  |
| PZD8 | Velocity setpoint in MDI operating mode |
| PZD9 |  |
| PZD10 | Acceleration override for direct setpoint specification/MDI operating mode |
| PZD11 | Deceleration override for direct setpoint specification/MDI operating mode |

#### Assignment of control word 1

| Bit | Abbr. | Designation (description of the HIGH level) | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | Off1 | ON command: 0 = OFF1 active; 1 = ON | p840 | 2501 |
| 1 | Off2 | 0 =: OFF2 active  1 = signal: operating condition   **No** coasting active | p844 | 2501 |
| 2 | Off3 | 0 = OFF3 active  1 = operating condition **no** quick stop active | p848 | 2501 |
| 3 | Enc | Enable of inverter | p852 | 2501 |
| 4 | RejTrvTsk | Traversing blocks and direct setpoint specification/MDI  Reject traversing task  0 = active traversing command is rejected / axis brakes with 100% deceleration override  1 = Do not reject traversing task  (axis can be traversed) | p2640 | 3616 |
| 5 | IntMStop | Intermediate STOP traversing blocks and MDI/direct setpoint specification intermediate stop   0 = active traversing command is interrupted/axis brakes with specified delay override  1 = no intermediate stop (axis can be traversed) | p2640 | 3616 |
| **6** | **TrvStart** | **Activate traversing job**    **Setpoint acceptance edge if MdiTyp = 0** | **p2631**    **p2650** | **3640**    **3620** |
| 7 | AckFault | Acknowledgement of fault | p2103 | 2501 |
| 8 | Jog1 | Jog signal source 1 | p2589 | 3610 |
| 9 | Jog2 | Jog signal source 2 | p2590 | 3610 |
| 10 | LB | Life bit (control request from PLC) | p854 | 2501 |
| 11 | RefStart | Start homing | p2595 | 3612 |
| 12 | Bit12 | Reserved |  |  |
| 13 | Bit13 | External block change (0->1) | <not used>  (p2633) |  |
| 14 | Bit14 | Reserved |  |  |
| 15 | Bit15 | Reserved |  |  |

#### Assignment of EPosSTW 1

| Bit | Abbr. | Name | Drive parameter | Function diagram |
| --- | --- | --- | --- | --- |
|  | TrvBit0 | Block selection bit 0 | p2625 | 3640 |
| 1 | TrvBit1 | Block selection bit 1 | p2626 | 3640 |
| 2 | TrvBit2 | Block selection bit 2 | p2627 | 3640 |
| 3 | TrvBit3 | Block selection bit 3 | p2628 | 3640 |
| 4 | TrvBit4 | Block selection bit 4 | p2629 | 3640 |
| 5 | TrvBit5 | Block selection bit 5 | p2630 | 3640 |
| 6 | Bit6 | Reserved |  |  |
| 7 | Bit7 | Reserved |  |  |
| 8 | MdiTyp | Positioning type   0 = relative positioning  1 = absolute positioning | p2648 | 3620 |
| 9 | MdiPos | Selection of direction for setting up, or absolute positioning of rotary axes, in the positive direction | p2651 | 3620 |
| 10 | MdiNeg | Selection of direction for setting up, or absolute positioning of rotary axes, in the negative direction | p2652 | 3620 |
| 11 | Bit11 | Reserved |  |  |
| 12 | MdiTrTyp | Transfer type  0 = Value acceptance through 0 → 1 edge at MdiEdge   1 signal: continuous setpoint acceptance | P2649 | 3620 |
| 13 | Bit13 | Reserved |  |  |
| 14 | MdiSetup | Direct setpoint input/MDI – setup selection  Selection of MDI setup mode   0 = positioning  1 = set up | p2653 | 3620 |
| 15 | MdiStart | Operating mode MDI/direct setpoint specification | p2647 | 3640 |

#### Assignment of EPosSTW 2

| Bit | Abbr. | Name | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | TrkMode | Start follow-up mode | p2655.0 | 3635 |
| 1 | SetRefPt | Set home position | p2596 | 3612 |
| 2 | ActRefCam | Activate homing cams | p2612 | 3612 |
| 3 | Bit3 | Activate fixed stop | <not used> |  |
| 4 | Bit4 | Reserved |  |  |
| 5 | JogInc | Jog:  0 = continuous traversing  1 = traversing about parameterized path | p2591 | 3610 |
| 6 | Bit6 | Reserved |  |  |
| 7 | Bit7 | Reserved |  |  |
| 8 | RefTyp | Selection of homing type  0 = reference point approach  1 = flying referencing | p2597 | 3612 |
| 9 | RefStDi | Homing procedure start direction  0 = positive start direction  1 = negative start direction | p2604 | 3612 |
| 10 | RefInpS | Setting the signal source for the selection of the measuring input for flying (passive) homing  0 = measuring input 1 is activated  1 = measuring input 2 is activated | p2510 | 4010 |
| 11 | RefEdge | Passive homing: setting of the edge evaluation   0 : Positive edge  1 : Negative edge | p2511 | 4010 |
| 12 | Bit12 | Reserved |  |  |
| 13 | Bit13 | Reserved |  |  |
| 14 | SftLimAct | Activation of the software limit switch | p2582 | 3630 |

#### Assignment of STW2

| Bit | Abbr. | Name | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | DDSBit0 | Drive data set bit 0 | p820.0 | 8565 |
| 1 | DDSBit1 | Drive data set bit 1 | p821.0 | 8565 |
| 2 | DDSBit2 | Drive data set bit 2 | p822.0 | 8565 |
| 3 | DDSBit3 | Drive data set bit 3 | p823.0 | 8565 |
| 4 | DDSBit4 | Drive data set bit 4 | p824.0 | 8565 |
| 5 | GlbStart | Global start | <not used> |  |
| 6 | ResIComp | Reset I-component of speed controller | <not used> |  |
| 7 | ActPrkAxis | Activate parking axis | p897 |  |
| 8 | TrvFixedStp | Travel to fixed stop | <not used>  (p1545.0) | <not used>  (8012) |
| 9 | GlbTrgCom | Global trigger command | <not used> |  |
| 10 | Bit10 | Reserved |  |  |
| 11 | MotSwOver | Motor switchover completed (0->1) | p828.0 | 8575 |
| 12 | MsZykBit0 | Master sign-of-life bit 0 | <not used> |  |
| 13 | MsZykBit1 | Master sign-of-life bit 1 | <not used> |  |
| 14 | MsZykBit2 | Master sign-of-life bit 2 | <not used> |  |
| 15 | MsZykBit3 | Master sign-of-life bit 3 | <not used> |  |

#### Setpoint overview

| PZD | Abbr. | Setpoint | Parameter | Function diagram |
| --- | --- | --- | --- | --- |
| 5 | OverrideV | Velocity override | p2646 | 3630 |
| 6+7 | Position | Position setpoint | p2642 | 3620 |
| 8+9 | Velocity | Velocity setpoint | p2643 | 3618 |
| 10 | OverrideA | Acceleration override | p2644 | 3618 |
| 11 | OverrideD | Deceleration override | p2645 | 3618 |
| 12 | Word12 | Reserved |  |  |

| PZD | Assignment of the process data |
| --- | --- |
| PZD1 | Status word 1 |
| PZD2 | EPosZSW 1 |
| PZD3 | EPosZSW 2 |
| PZD4 | Status word 2 |
| PZD5 | MELDW |
| PZD6 | Actual position value [LU] |
| PZD7 |  |
| PZD8 | Actual velocity value (refers to reference speed p2000)  Note: 40000000HEX = 100% |
| PZD9 |  |
| PZD10 | Fault (sending of the active fault number) |
| PZD11 | Alarm (sending of the active alarm number) |
| PZD12 | Reserve |

#### Assignment of status word 1

| Bit | Abbr. | Name | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | RTS | Ready for power-up | r899.0 | 2503 |
| 1 | RDY | Ready to operate | r899.1 | 2503 |
| 2 | IOp | Drive is switched on (condition for the mode selection of the EPOS) | r899.2 | 2503 |
| 3 | Fault | Fault active | r2139.3 | 2548 |
| 4 | NoOff2Act | OFF2 not activated (partial condition for the switch-on) | r899.4 | 2503 |
| 5 | NoOff3Act | OFF3 not activated (partial condition for the switch-on) | r899.5 | 2503 |
| 6 | PowInhbt | Switching on inhibited active | r899.6 | 2503 |
| 7 | Alarm | Alarm present | r2139.7 | 2548 |
| 8 | NoFlwErr | Following error within tolerance | r2684.8 | 4025 |
| 9 | LbCr | Control request | r899.9 | 2503 |
| 10 | TargPos | Target position reached | r2684.10 | 4020 |
| 11 | RefPSet | Home position set | r2684.11 | 3614 |
| 12 | TrvTskAck | Traversing block activated acknowledgement | r2684.12 | 3646 |
| 13 | StndStill | |n_act| < speed threshold value 3 [p2161]  This bit is used for standstill detection | r2199.0 | 2537 |
| 14 | Accel | Axis accelerates | r2684.4 | 3635 |
| 15 | Decel | Axis decelerates | r2684.5 | 3635 |

#### Assignment of EPosZSW 1

| Bit | Abbr. | Name | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | ActTrvBit0 | Active traversing block bit 0 | r2670.0 | 3650 |
| 1 | ActTrvBit1 | Active traversing block bit 1 | r2670.1 | 3650 |
| 2 | ActTrvBit2 | Active traversing block bit 2 | r2670.2 | 3650 |
| 3 | ActTrvBit3 | Active traversing block bit 3 | r2670.3 | 3650 |
| 4 | ActTrvBit4 | Active traversing block bit 4 | r2670.4 | 3650 |
| 5 | ActTrvBit5 | Active traversing block bit 5 | r2670.5 | 3650 |
| 6 | Bit6 | Reserved |  |  |
| 6 | Bit7 | Reserved |  |  |
| 8 | StpCamMinAct | STOP cam minus active | r2684.13 | 3630 |
| 9 | StpCamPlsAct | STOP cam plus active | r2684.14 | 3630 |
| 10 | JogAct | Jog active operating mode | r2094.0 <sup>1)</sup> | 2460 |
| 11 | RefAct | Homing procedure active operating mode | r2094.1 <sup>1)</sup> | 2460 |
| 12 | FlyRefAct | Flying homing active | r2684.1 | 3630 |
| 13 | TrvBlAct | Traversing blocks active operating mode | r2094.2 <sup>1)</sup> | 2460 |
| 14 | MdiStupAct | In the direct setpoint specification / MDI operating mode,   setup is active | r2094.4 <sup>1)</sup> | 2460 |
| 15 | MdiPosAct | Positioning is active in the direct setpoint specification/MDI operating mode | r2094.3 <sup>1)</sup> | 2460 |

<sup>1)</sup> r2669 (function block diagram 3630) in bit-granular display. For this purpose, p2099[0] = r2699 is connected at the input of the connector-binector converter.

#### Assignment of EPosZSW 2

| Bit | Abbr. | Name | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | TrkModeAct | Follow-up mode active | r2683.0 | 3645 |
| 1 | VeloLimAct | Velocity limitation active | r2683.1 | 3645 |
| 2 | SetPStat | Setpoint stationary | r2683.2 | 3645 |
| 3 | PrntMrkOut | Registration mark outside outer window | r2684.3 | 3614 |
| 4 | FWD | Axis travels forward | r2683.4 | 3635 |
| 5 | BWD | Axis travels backward | r2683.5 | 3635 |
| 6 | SftSwMinAct | Minus software limit switch approached | r2683.6 | 3635 |
| 7 | SftSwPlsAct | Plus software limit switch approached | r2683.7 | 3635 |
| 8 | PosSmCam1 | Actual position value <= cam switching position 1 | r2683.8 | 4025 |
| 9 | PosSmCam2 | Actual position value <= cam switching position 2 | r2683.9 | 4025 |
| 10 | TrvOut1 | Direct output 1 via traversing block | r2683.10 | 3616 |
| 11 | TrvOut2 | Direct output 2 via traversing block | r2683.11 | 3616 |
| 12 | FxStpRd | Fixed stop reached | <not used>  (r2683.12) | 3645 |
| 13 | FxStpTrRd | Fixed stop clamping torque reached | <not used>  (r2683.13) | 3645 |
| 14 | TrvFxStpAct | Travel to fixed stop active | <not used>  (r2683.14) | 3645 |
| 15 | CmdAct | Traversing active | r2683.15 | 3645 |

#### Assignment of status word 2

| Bit | Abbr. | Name | Drive parameters | Function diagram |
| --- | --- | --- | --- | --- |
| 0 | ActDDSBit0 | Drive data set bit 0 | r51.0 | 8565 |
| 1 | ActDDSBit1 | Drive data set bit 1 | r51.1 | 8565 |
| 2 | ActDDSBit2 | Drive data set bit 2 | r51.2 | 8565 |
| 3 | ActDDSBit3 | Drive data set bit 3 | r51.3 | 8565 |
| 4 | ActDDSBit4 | Drive data set bit 4 | r51.4 | 8565 |
| 5 | CmdActRelBrk | Open holding brake active | <not used> |  |
| 6 | TrqContMode | Torque-controlled operation | <not used> |  |
| 7 | ParkAxisAct | Parking axis selected | r896.0 |  |
| 8 | Bit8 | Reserved | r1406.8 |  |
| 9 | GlbTrgReq | Global trigger request | <not used> |  |
| 10 | PulsEn | Pulses enabled | r899.11 | 2503 |
| 11 | MotSwOverAct | Motor data set switchover active | r835.0 | 8575 |
| 12 | SlvZykBit0 | Slave sign-of-life bit 0 | <not used> |  |
| 13 | SlvZykBit1 | Slave sign-of-life bit 1 | <not used> |  |
| 14 | SlvZykBit2 | Slave sign-of-life bit 2 | <not used> |  |
| 15 | SlvZykBit3 | Slave sign-of-life bit 3 | <not used> |  |

#### Actual value overview

| PZD | Abbr. | Actual value | Parameter | Function diagram |
| --- | --- | --- | --- | --- |
| 5 | Word6 | Reserved |  |  |
| 6+7 | Position | Actual position value | r2521 | 4010 |
| 8+9 | Velocity | Actual speed value | r63 | 4715 |
| 10 | ErrNr | Error | r2131 | 8060 |
| 11 | WarnNr | Alarm | r2132 | 8065 |
| 12 | Reserve | Reserved |  |  |

## Function block SinaSpeed

This section contains information on the following topics:

- [Description](#description-1)
- [Calling OBs](#calling-obs-1)
- [Called blocks](#called-blocks-1)
- [Function description - general](#function-description---general)
- [Input interface of the SinaSpeed](#input-interface-of-the-sinaspeed)
- [Pre-assignment of the ConfigAxis input](#pre-assignment-of-the-configaxis-input)
- [Output interface of the SinaSpeed](#output-interface-of-the-sinaspeed)
- [Error handling of the SinaSpeed function block](#error-handling-of-the-sinaspeed-function-block)
- [Standard telegram 1](#standard-telegram-1)

### Description

#### Function block SinaSpeed (FB301)

![Function block SinaSpeed (FB301)](images/117879614603_DV_resource.Stream@PNG-en-US.png)

#### Description

The corresponding instance DB is automatically created when the FB301 (SinaSpeed) is integrated.

Can be used in the following CPUs: SIMATIC S7-1200/1500

### Calling OBs

#### Calling OBs

The block can be alternatively installed in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

### Called blocks

#### Called blocks

DPRD_DAT/SFC14

DPWR_DAT/SFC15

### Function description - general

#### Description of functions

Using the function block, a SINAMICS drive can be cyclically activated with the standard telegram 1.

> **Note**
>
> When configuring the SINAMICS drive, you must ensure that the standard telegram 1 is selected for communication.

> **Note**
>
> The interface for the block is limited to just a few inputs and outputs. All of the signals of the telegram can be reached in the direction of the setpoint at any time via the "ConfigAxis" input. When the block is inserted, the inputs that are not displayed are filled with default values.

The axis is switched on via the input bit "EnableAxis" = 1. "1" is preassigned to OFF2 and OFF3 via the input "ConfigAxis" and they do not have to be written by the user for operation.

The axis is ready to be switched on if there is no active error – "Error"= "0" – and no switch-on inhibit – "Lockout" = "0".

The speed setpoint is specified directly on the block input "SpeedSp" in the REAL format. To undertake the necessary normalization of the setpoint, "RefSpeed" must be entered at the input – this corresponds to the parameter p2000 in the SINAMICS drive. The actual speed value is output at the output "ActVelocity" in the REAL format.

### Input interface of the SinaSpeed

#### Input interface SINA_SPEED

| Input signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| EnableAxis | BOOL | 0 | "EnableAxis" = 1 → switching on the drive |
| AckError | BOOL | 0 | Acknowledgement of axis fault → "AckFlt"=1 |
| SpeedSp | REAL | 0.0[rpm] | Speed setpoint |
| RefSpeed | REAL | 0.0[rpm] | Rated speed of the drive →p2000 |
| ConfigAxis | WORD | 3 | For more information, see [Pre-assignment of the ConfigAxis input](#pre-assignment-of-the-configaxis-input). |
| HWIDSTW | HW_IO | 0 | Symbolic name or HW ID on the SIMATIC S7-1200/1500 of the setpoint slot |
| HWIDZSW | HW_IO | 0 | Symbolic name or HW ID on the SIMATIC S7-1200/1500 of the actual value slot |

### Pre-assignment of the ConfigAxis input

#### Pre-assignment of the ConfigAxis input

| ConfigAxis | Meaning | PZD | Interconnection in the drive | Default |
| --- | --- | --- | --- | --- |
| Bit0 | OFF2 | 1 | r2090.1 = p 844[0] | 1 |
| Bit1 | OFF3 | 1 | r2090.2 = p 848[0] | 1 |
| Bit2 | Inverter enable | 1 | r2090.3 = p 852[0] | 1 |
| Bit3 | Ramp-function generator enable | 1 | r2090.4 = p1140[0] | 1 |
| Bit4 | Continue ramp-function generator | 1 | r2090.5 = p1141[0] | 1 |
| Bit5 | Speed setpoint enable | 1 | r2090.6 = p1142[0] | 1 |
| Bit6 | Holding brake must be opened | 1 | r2090.12 = p855[0] | 0 |
| Bit7 | Direction of rotation | 1 | r2090.11 = p1113[0] | 0 |
| Bit8 | Motorized pot. setpoint higher | 1 | r2090.13 = p1035[0] | 0 |
| Bit9 | Motorized pot. setpoint lower | 1 | r2090.14 = p1036[0] | 0 |
| Bit10 | Reserve - can be used as required (bit 8) | 1 | r2091.0 | 0 |
| Bit11 | Reserve - can be used as required (bit 9) | 1 | r2091.1 | 0 |
| Bit12 | Reserve - can be used as required (bit 15) | 1 | r2091.7 | 0 |
| Bit13 |  |  |  | 0 |
| Bit14 |  |  |  | 0 |
| Bit15 |  |  |  | 0 |

### Output interface of the SinaSpeed

#### Output interface SINA_SPEED

| Output signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| AxisEnabled | BOOL | 0 | Operating mode is executed or enabled |
| Lockout | BOOL | 0 | 1 = switch-on inhibit active |
| ActVelocity | REAL | 0.0[rpm] | Actual speed -> depending on the normalization factor RefSpeed |
| Error | BOOL | 0 | 1 = group fault present |
| Status | INT | 0 | 16#7002: No error – block is being processed   16#8401: Error in drive   16#8402: Switching on inhibited  16#8600: Error DPRD_DAT   16#8601: Error DPWR_DAT |
| DiagID | WORD | 0 | Expanded communication error -> SFB call error |

> **Note**
>
> The complete status data of Telegram 1 can be found in [Standard telegram 1](#standard-telegram-1).

### Error handling of the SinaSpeed function block

#### Troubleshooting the SINA_SPEED function block

The group error "Error" is set if the SINAMICS drive is faulted or the switch-on inhibit of the SINAMICS drive is active or if the call of the SFB reports an error. A corresponding "Status" is also output:

| Error number  Status | Meaning | Remedy |
| --- | --- | --- |
| 16#7002 | No fault active |  |
| 16#8401 | Drive fault active | Evaluate active errors of the SINAMICS per acyclic communication |
| 16#8402 | Switching on of drive inhibited active | Check for parking axis, safety active, parameter p10 ≠ 0 |
| 16#8600   16#8601 | SFB call error active | Clearing the communication fault |

- The faults of the SINAMICS drive can be acknowledged via the input AcktError.
- The fault of the SFB call is displayed at the DiagID output and must be checked by the user. Once this fault has been cleared or goes away, the group error "Error" is rescinded as needed and the errors ID "Status" is updated.

> **Note**
>
> **If error message 8092(hex) occurs at the DIAGID output, the S7-300/400/1x00 firmware must be checked. The following applies:**
>
> • S7-1200  Firmware at least 2.x
>
> • S7-1500  Firmware at least 1.1

### Standard telegram 1

#### Standard telegram 1

| S7 bit representation (drive) | Meaning |
| --- | --- |
| STW1 1.0 (bit 0) | OFF1/ON (pulse enable possible) |
| STW1 1.1 (bit 1) | OFF2/ON (enable possible) |
| STW1 1.2 (bit 2) | OFF3/ON (enable possible) |
| STW1 1.3 (bit 3) | Enable or disable operation |
| STW1 1.4 (bit 4) | Ramp-function generator enable |
| STW1 1.5 (bit 5) | Continue ramp-function generator |
| STW1 1.6 (bit 6) | Speed setpoint enable |
| STW1 1.7 (bit 7) | Acknowledge fault |
| STW1 0.0 (bit 8) | Reserved |
| STW1 0.1 (bit 9) | Reserved |
| STW1 0.2 (bit 10) | Control by PLC |
| STW1 0.3 (bit 11) | Direction of rotation |
| STW1 0.4 (bit 12) | Holding brake must be opened |
| STW1 0.5 (bit 13) | Motorized potentiometer setpoint higher |
| STW1 0.6 (bit 14) | Motorized potentiometer setpoint lower |
| STW1 0.7 (bit 15) | Reserved |
| STW2 (bits 16 to 32) | Speed setpoint |

| S7 bit representation (drive) |  |
| --- | --- |
| ZSW1 1.0 (bit 0) | Ready for switching on |
| ZSW1 1.1 (bit 1) | Ready for operation |
| ZSW1 1.2 (bit 2) | Operation enabled |
| ZSW1 1.3 (bit 3) | Fault present |
| ZSW1 1.4 (bit 4) | No coast down active (OFF2 active) |
| ZSW1 1.5 (bit 5) | No coast down active (OFF3 inactive) |
| ZSW1 1.6 (bit 6) | Switching on inhibited active |
| ZSW1 1.7 (bit 7) | Alarm present |
| ZSW1 0.0 (bit 8) | Speed setpoint - actual value deviation within tolerance t_off |
| ZSW1 0.1 (bit 9) | Control requested |
| ZSW1 0.2 (bit 10) | f or n comparison value reached/exceeded |
| ZSW1 0.3 (bit 11) | I, M, or P limit not reached |
| ZSW1 0.4 (bit 12) | Open the holding brake |
| ZSW1 0.5 (bit 13) | No motor overtemperature alarm |
| ZSW1 0.6 (bit 14) | Direction of rotation |
| ZSW1 0.7 (bit 15) | No alarm, thermal overload, power unit |
| ZSW2 (bits 16 to 32) | Bits 16 – 31 → actual speed value |

## Function block SinaPara

This section contains information on the following topics:

- [Description](#description-2)
- [Calling OBs](#calling-obs-2)
- [Called blocks](#called-blocks-2)
- [Description of functions](#description-of-functions-1)
- [Input interface of the SinaPara](#input-interface-of-the-sinapara)
- [Output interface of the SinaPara](#output-interface-of-the-sinapara)
- [Input/output interface of the SinaPara](#inputoutput-interface-of-the-sinapara)
- [Data structure of the "Parameter" area](#data-structure-of-the-parameter-area)
- [Writing parameters](#writing-parameters)
- [Reading parameters](#reading-parameters)
- [Error handling of the SinaPara function block](#error-handling-of-the-sinapara-function-block)
- [Connection to the LAcycCom library](#connection-to-the-lacyccom-library)

### Description

#### Function block SinaPara (FB302)

![Function block SinaPara (FB302)](images/117879683851_DV_resource.Stream@PNG-en-US.png)

#### Description

The corresponding instance DB is automatically created when the FB302 (SinaPara) is integrated.

Can be used in the following CPUs: S7-1200/1500

### Calling OBs

#### Calling OBs

The block can be alternatively installed in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

### Called blocks

#### Called blocks

RDREC/SFB52

WRRECSFB53

### Description of functions

#### Description of functions

With the aid of the block, any parameters up to a maximum of 16 can be read or written to a SINAMICS S/G drive.

> **Note**
>
> The data is accessed by means of dataset 47 according to the PROFIdrive profile.

At the ReadWrite input it is specified whether the number specified at the ParaNo input is to be written to or read from the SINAMICS drive.

The reading or the writing of the parameters is initiated by the edge-triggered Start input.

The data of the parameters must be entered into a global DB in which an array of 16 entries of the type UDT "SinaParameter" is created. This array must then be interconnected with the INOUT parameter "Parameter".

The data to be written/read is entered or displayed in the REAL or DINT format.

### Input interface of the SinaPara

#### Input interface of SINA_PARA

| Input signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| Start | BOOL | 0 | **Start of the job (0 = no job or cancel job; 1 = start and execute job)** |
| ReadWrite | BOOL | 0 | Job type  0=read, 1=write |
| ParaNo | INT | 1 | Number of parameters → 1to16 |
| AxisNo | BYTE | 1 | Axis number/axis ID/DO number in multi-axis system |
| hardwareId | HW IO | 0 | Hardware ID of the module access points / actual value telegram slot of the axis or drive |

### Output interface of the SinaPara

#### Output interface of SINA_PARA

| Output signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| Ready | BOOL | 0 | Checkback signal for connecting in LAcycCom environment; 1 = job ended or job canceled (one cycle long)  See [Connection to the LAcycCom library](#connection-to-the-lacyccom-library) |
| Busy | BOOL | 0 | Job being processed if "Busy" → 1 |
| Done | BOOL | 0 | Job completed means edge change from 0 → 1 |
| Error | BOOL | 0 | Group error active à "Error" → 1 |
| Status | DWORD | 0 | 1st word → binary-coded as to which parameter access is faulted  2nd word: type of fault |
| DiagId | WORD | 0 | Expanded communication error → SFB call error |

### Input/output interface of the SinaPara

#### Input/output interface of the SinaPara

| **Input/output signal** | **Type** | **Default** | **Meaning** |
| --- | --- | --- | --- |
| Parameter | SinaParameter |  | **List of parameters (max. 16 parameters)** |

### Data structure of the "Parameter" area

#### Data structure of the "Parameter" area

Job fields to be filled in by the user:

- Parameter[x].siParaNo := parameter number (value range 1..65535)
- Parameter[x1].siIndex := parameter index (value range 0..65535)
- Parameter[x].srValue := parameter value (value range 1.175 495e-38..3.402823e+38) – is populated when reading the block.
- Parameter[x].sdValue := parameter value (value range -214748364810 (-2^31) to +214748364710 (2^31)

![Data structure of the "Parameter" area](images/117879759371_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> All of the parameters of the type DWORD or DINT must be written in the Parameter[x].sdValue field. The block logic automatically detects the DWORD / DINT format, and the Parameter[x].sdValue job field is used for writing or reading.
>
> For all other parameters, the Parameter[x].srValue field is used.

> **Note**
>
> Users must know whether the format of the parameter to be read/written involves DWORD/DINT or the remainder (byte, word, real, INT, etc.).
>
> If this is not observed, problems can occur, especially when writing, because the default value of the DINT field ("0") is transferred here instead of the desired value (which was incorrectly entered in the REAL field).
>
> Likewise, the evaluation of read operations for parameters in the DWORD/DINT format must be carried out via the new job field.

> **Note**
>
> With the aid of the new job field, it is now possible to read/write BICO parameter interconnections without problems.

The different formats of the parameter are determined by the block itself. (value range 0x40 = Zero,0x41/0x02/0x05 = Byte, 0x42/0x03/0x06 = Word, 0x43/0x04/0x07/0x08 = DWord, 0x44 = Error)

The following job fields are filled by the block:

- Parameter[x].syFormat := parameter format
- Parameter[x].swErrorNo := parameter error number (value range 0x0000..0x00FF)

![Data structure of the "Parameter" area](images/117879776651_DV_resource.Stream@PNG-en-US.png)

### Writing parameters

#### Writing parameters

The "Write" action results in the parameter value and the format of the set parameter first being read from the SINAMICS drive and then written into the parameter structure. After being read successfully, the parameter value that was set by the user is then sent to the SINAMICS drive.

While this is taking place, the Busy bit is set to "1".

If the parameter to be written is erroneous, the associated parameter error number is also read and entered into the structure. At the same time, the corresponding error bit in the first word of the double word Status is set.

A successful write process is ended with the edge change "10" of the Busy bit and an edge change "01" of the Done bit. The Error bit must NOT be set during this. If this happens, the double word Status is to be evaluated.

Examples for writing parameters can be found at Siemens Industry Online Support under the following ID: 109758413.

### Reading parameters

#### Reading parameters

The "Read" action results in the parameter value and the format of the set parameter being read from the SINAMICS drive and then written into the parameter structure. Then the value to be read is saved in the structure.

While this is taking place, the Busy bit is set to "1".

If the parameter to be read is erroneous, the associated parameter error number is also read and entered into the structure. At the same time, the corresponding error bit in the first word of the double word Status is set.

A successful read process is ended with the edge change "1->0" of the Busy bit and an edge change "0->1" of the Done bit. The Error bit must NOT be set during this. If this happens, the double word Status is to be evaluated.

Examples for reading parameters can be found at Siemens Industry Online Support under the following ID: 109758413.

### Error handling of the SinaPara function block

#### Troubleshooting function block SINA_PARA

The errors that temporarily occurred during the communication with the SINAMICS drive are identified and lead to the required action being repeated.

> **Note**
>
> The siErrorCount (current count) and siMaxErrCount parameters are listed in the instance data block. The siMaxErrCount can be edited by the user and specifies the maximum number of attempts to repeat the job when temporary errors occur (default 12500).
>
> Error is then set = 1 and the status is set.

- During an active SFB fault, group error “Error = 1“ is set, and an output is realized in the first word of the status as well as at output DiagID. Errors due to the SFB calls must not be acknowledged. Once these faults have been eliminated and a new job is started, the outputs DiagID, Error and Status are withdrawn.
- If an incorrect value is entered at the "ParaNo" input, this value is not taken into consideration, the group error "Error" is set, and the parameterization error is displayed at output "Status".
- The group error "Error" is also set if a "Request" error occurs. For this error, the job is carried out, but one or more parameter accesses were not possible. The errors that occurred due to the access are binary coded and displayed in the second word of the double word "Status". The job is also displayed as completed with "Done" = 1.

#### Evaluation of the Status output

| Status |  |
| --- | --- |
| Status[1] | Status[2] |

| ErrorI(1) | Meaning |
| --- | --- |
| 0x000 | No fault active |
| 0x001 | Internal telegram error active |
| 0x002 | Parameterization error active |
| 0x003 | SFB call error active |
| 0x004 | Cancelation of the job during the active data transfer by resetting the Start input to "0" |
| 0x005 | Unknown data type detected; evaluation of the Status[2] shows the parameter with unknown data type in the highest value bit |

| Status | Meaning |
| --- | --- |
| 0x00 | No fault during parameter access |
| 0x01 | 1st parameter access faulty  For evaluation see swParameter[1].ErrorNo |
| 0x02 | 2nd parameter access faulty  For evaluation see swParameter[2].ErrorNo |
| 0x04 | 3rd parameter access faulty  For evaluation see swParameter[3].ErrorNo |
| 0x08 | 4th parameter access faulty  For evaluation see swParameter[4].ErrorNo |
| 0x10 | 5th parameter access faulty  For evaluation see swParameter[5].ErrorNo |
| 0x20 | 6th parameter access faulty  For evaluation see swParameter[6].ErrorNo |
| 0x40 | 7th parameter access faulty  For evaluation see swParameter[7].ErrorNo |
| 0x80 | 8th parameter access faulty  For evaluation see swParameter[8].ErrorNo |
| 0x100 | 9th parameter access faulty  For evaluation see swParameter[9].ErrorNo |
| 0x200 | 10th parameter access faulty  For evaluation see swParameter[10].ErrorNo |
| 0x400 | 11th parameter access faulty  For evaluation see swParameter[11].ErrorNo |
| 0x800 | 12th parameter access faulty  For evaluation see swParameter[12].ErrorNo |
| 0x1000 | 13th parameter access faulty  For evaluation see swParameter[13].ErrorNo |
| 0x2000 | 14th parameter access faulty  For evaluation see swParameter[14].ErrorNo |
| 0x4000 | 15th parameter access faulty  For evaluation see swParameter[15].ErrorNo |
| 0x8000 | 16th parameter access faulty  For evaluation see swParameter[16].ErrorNo |

### Connection to the LAcycCom library

#### Connection to the LAcycCom library

> **Note**
>
> LAcycCom libraries for SIMATIC S7-1200/S7-1500 facilitate collision-free coordination of communication resources in the CPU for acyclic communication using DPV1 services. For this purpose, in the application, instead of the system functions, the corresponding functions in these libraries are used to communicate with external devices.

> **Note**
>
> The LAcycCom library can be accessed at the following SIOS link:
>
> https://support.industry.siemens.com/cs/ww/en/view/109479553

> **Note**
>
> For use within the LAcycCom environment, function block "LAcycCom_ResourceManager", global data block "LAcycCom_RequestBuffer" and the PLC variables and PLC data types available in the library are required.

![Connection to the LAcycCom library](images/117880176779_DV_resource.Stream@PNG-en-US.png)

Connection to the LAcycCom library

Blocks SINA_PARA and SINA_PARA_S are connected in conjunction with the "LAcycCom_HandleResource" block.

The acyclic communication job is transferred to the HandleResource block, and after the release (by the ResourceManager) this controls block SINA_PARA.

After the job has been completed, block SINA_PARA communicates this to the HandleResource block via the Ready output (for one cycle). This can now release the resource again.

To reliably evaluate the start and enable signals, an edge evaluation is used for the start command as well as a memory element (SR flip flop).

> **Note**
>
> Block SINA_PARA_S is connected in the same way.

## Function block SinaParaS

This section contains information on the following topics:

- [Description](#description-3)
- [Calling OBs](#calling-obs-3)
- [Called blocks](#called-blocks-3)
- [Description of functions](#description-of-functions-2)
- [Input interface of the SinaParaS](#input-interface-of-the-sinaparas)
- [Output interface of the FB303](#output-interface-of-the-fb303)
- [Use of the various parameter inputs and outputs](#use-of-the-various-parameter-inputs-and-outputs)
- [Writing parameters](#writing-parameters-1)
- [Reading parameters](#reading-parameters-1)
- [Error handling of the SinaParaS function block](#error-handling-of-the-sinaparas-function-block)

### Description

#### Function block SinaParaS (FB303)

![Function block SinaParaS (FB303)](images/117880309899_DV_resource.Stream@PNG-en-US.png)

#### Description

The corresponding instance DB is automatically created when the SinaParaS (FB303) is integrated.

Can be used in the following CPUs: S7-1200/1500

### Calling OBs

#### Calling OBs

The block can be alternatively installed in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

### Called blocks

#### Called blocks

RDREC/SFB52

WRRECSFB53

### Description of functions

#### Description of functions

With the aid of the block, 1 parameters can be read or written to a SINAMICS S/G drive.

> **Note**
>
> The data is accessed by means of dataset 47 according to the PROFIdrive profile.

At the "ReadWrite" input it is specified whether the parameter is to be written to or read from the SINAMICS drive.

The reading or the writing of the parameters is initiated by the edge-triggered "Start" input.

### Input interface of the SinaParaS

#### Input interface of the SinaParaS (FB303)

| Input signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| Start | BOOL | 0 | **Start of the job (0 = no job or cancel job; 1 = start and execute job)** |
| ReadWrite | BOOL | 0 | Job type  0=read, 1=write |
| Parameter | UINT | 1 | Parameter number |
| Index | UINT | 0 | Index of the parameter |
| ValueWrite1 | REAL | 0.0 | Value of the parameter in REAL format |
| ValueWrite2 | DINT | 0 | Value of the parameter in DINT format |
| AxisNo | BYTE | 1 | Axis number/axis ID/DO number in multi-axis system |
| hardwareId | HW IO | 0 | Hardware ID of the module access points / actual value telegram slot of the axis or drive |

### Output interface of the FB303

#### Output interface of the FB287

| Output signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| Ready | BOOL | 0 | Checkback signal for connecting in LAcycCom environment; 1 = job ended or job canceled (one cycle long) |
| Busy | BOOL | 0 | Job in progress if "Busy"=1 |
| Done | BOOL | 0 | Job ended without errors means edge change from 0->1 |
| ValueRead1 | REAL | 0.0 | Value of the read parameter (REAL format) |
| ValueRead2 | DINT | 0 | Value of the read parameter (DINT format) |
| Format | INT | 0 | Format of the read parameter |
| ErrorNo | INT | 0 | Error number according to PROFIdrive profile |
| Error | BOOL | 0 | Active group error -> "Error" =1 |
| Status | DWORD | 0 | 1st word -> binary-coded indicating which parameter access is faulted  2nd word: type of fault |
| DiagId | WORD | 0 | Expanded communication error -> SFB call error |

### Use of the various parameter inputs and outputs

#### Use of the various parameter inputs and outputs

> **Note**
>
> All of the parameters of the type DWORD or DINT must be written in the ValueRead2 field. The block logic automatically detects the DWORD / DINT format, and the ValueRead2 job field is used for writing or reading.
>
> For all other parameters, the ValueRead1 field is used.

> **Note**
>
> Users must know whether the format of the parameter to be read/written involves DWORD/DINT or the remainder (byte, word, real, INT, etc.).
>
> If this is not observed, problems can occur, especially when writing, because the default value of the DINT field ("0") is transferred here instead of the desired value (which was incorrectly entered in the REAL field).
>
> Likewise, the evaluation of read operations for parameters in the DWORD/DINT format must be carried out via the new job field.

> **Note**
>
> With the aid of the new job field, it is now possible to read/write BICO parameter interconnections without problems.

### Writing parameters

#### Writing parameters

The "Write" action initially means that the parameter value at input ValueWrite1 and ValueWrite2 is accepted. After the parameter format has been successfully read, the appropriate job field is transferred to the SINAMICS drive.

While this is taking place, the "Busy" bit is set to "1".

If the parameter to be written is erroneous, the associated parameter error number is also read and entered at the ErrorNo output. At the same time, the corresponding error bit in the first word of the double word "Status" is set.

A successful write process is ended with the edge change "1→0" of the "Busy" bit and an edge change "0→1" of the "Done" bit. The "Error" bit must NOT be set during this. If this happens, the double word "Status" is to be evaluated.

### Reading parameters

#### Reading parameters

The "Read" action initially means that the parameter at the input parameter is read, and the drive displays the appropriate value at the ValueRead1 or ValueRead2 output.

While this is taking place, the "Busy" bit is set to "1".

If the parameter to be read is erroneous, the associated parameter error number is also output. At the same time, the corresponding error bit in the first word of the double word "Status" is set.

A successful read process is ended with the edge change "1→0" of the "Busy" bit and an edge change "0→1" of the "Done" bit. The "Error" bit must NOT be set during this. If this happens, the double word "Status" is to be evaluated.

### Error handling of the SinaParaS function block

#### Troubleshooting function block SINA_PARA_S

The errors that temporarily occurred during the communication with the SINAMICS drive are identified and lead to the required action being repeated.

> **Note**
>
> **Parameters siErrorCount and siMaxErrCount**
>
> The siErrorCount (current count) and siMaxErrCount parameters are listed in the instance data block. The siMaxErrCount can be edited by the user and specifies the maximum number of attempts to repeat the job when temporary errors occur (default 12500).
>
> Error is then set = 1 and the status is set.

- During an active SFB fault, group error “Error = 1“ is set, and an output is realized in the first word of the status as well as at output DiagID. Errors due to the SFB calls must not be acknowledged. Once these faults have been eliminated and a new job is started, the outputs DiagID, Error and Status are withdrawn.
- If an incorrect value is entered at the "ParaNo" input, this value is not taken into consideration, the group error "Error" is set, and the parameterization error is displayed at output "Status".
- The group error "Error" is also set if a "Request" error occurs. For this error, the job is carried out, but one or more parameter accesses were not possible. The errors that occurred due to the access are binary coded and displayed in the second word of the double word "Status". The job is also displayed as completed with "Done" = 1.

#### Evaluation of the Status output

| Symbol | Meaning |
| --- | --- |
| Status |  |
| Status[1] | Status[2] |

| Status[1] | Meaning |
| --- | --- |
| 0x000 | No fault active |
| 0x001 | Internal telegram error active |
| 0x002 | Parameterization error active |
| 0x003 | SFB call error active |
| 0x004 | Cancelation of the job during the active data transfer by resetting the Start input to "0" |
| 0x005 | Unknown data type detected; evaluation of the Status[2] shows the parameter with unknown data type in the highest value bit |

| Status[2] | Meaning |
| --- | --- |
| 0x00 | No fault during parameter access |
| 0x01 | 1st parameter access faulty  For evaluation see swParameter[1].ErrorNo |

## Function block Sinalnfeed

This section contains information on the following topics:

- [Description](#description-4)
- [Calling OBs](#calling-obs-4)
- [Called blocks/instructions](#called-blocksinstructions)
- [Description of functions](#description-of-functions-3)
- [Input interface of Sinalnfeed](#input-interface-of-sinalnfeed)
- [Pre-assignment of the ConfigAxis input](#pre-assignment-of-the-configaxis-input-1)
- [Output interface of Sinalnfeed](#output-interface-of-sinalnfeed)
- [Error handling of the Sinalnfeed function block](#error-handling-of-the-sinalnfeed-function-block)

### Description

#### Function block Sinalnfeed (FB305)

![Function block Sinalnfeed (FB305)](images/117880467851_DV_resource.Stream@PNG-en-US.png)

#### Description

The block is used to control the infeed unit of a SINAMICS S120. The block is only used for the control word STW1 and evaluates the status word ZSW1 of the infeed (standard telegram 370).

The corresponding instance DB is automatically created when the SinaInfeed (FB305) is integrated.

Can be used in the following CPUs: S7-1200/1500

### Calling OBs

#### Calling OBs

The block can be alternatively installed in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

### Called blocks/instructions

#### Called blocks/instructions

DPRD_DAT  Read consistent data of a DP standard slave

DPWD_DAT         Write consistent data of a standard DP slave

### Description of functions

#### Description of functions

The hardware ID of the setpoint slot is specified via the input "HWIDSTW" and that of the actual value slot is specified via the input "HWIDZSW".

The infeed can be precharged by setting the input "EnablePrecharging" (STW1.0) and enabled via the input "EnableInfeed“ (STW1.3) (by setting the corresponding control bits in STW1).

The functions are only carried out if the infeed is in the status required for this (evaluation of the current ZSW1).

The individual checkback signals (relevant status bits) of the infeed and the complete status word 1 are output via outputs of the block.

Besides the inputs "EnablePrecharging", "EnableInfeed" and "AckFault", the user can also make further specifications in control word 1 via the parameter "ConfigAxis" (standard: 3h). For immediate operation, specific bits are preset in the telegram by means of this input.

The "Control request" bit (STW1.10) is cyclically set within the block.

### Input interface of Sinalnfeed

#### Input interface of Sinalnfeed

| Input signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| EN | BOOL | 1 |  |
| EnablePrecharging | BOOL | 0 | Precharge infeed |
| EnableInfeed | BOOL | 0 | Switch on infeed |
| AckFault | BOOL | 0 | Acknowledgment error infeed |
| ConfigAxis | WORD | 16#0003 | Acknowledgment error infeed |
| HWIDSTW | HW_IO | 0 | Symbolic name or HW ID on the SIMATIC S7-1200/1500 of the setpoint slot |
| HWIDZSW | HW_IO | 0 | Symbolic name or HW ID on the SIMATIC S7-1200/1500 of the actual value slot |

### Pre-assignment of the ConfigAxis input

#### Pre-assignment of the ConfigAxis input

| ConfigAxis | Meaning | PZD | Interconnection in the drive | Default |
| --- | --- | --- | --- | --- |
| Bit0 | OFF2 | 1 | r2090.1 = p 844[0] | 1 |
| Bit1 | Inverter enable | 1 | r2090.3 = p 852[0] | 1 |
| Bit2 | 1 = disable generator operation | 1 | r2090.6 = p 3533 | 0 |
| Bit3 | 1 = disable motor operation | 1 | r2090.5 = p 3532 | 0 |
| Bit4 | Reserve - can be used as required (bit 2) | 1 | r2090.2 | 0 |
| Bit5 | Reserve - can be used as required (bit 4) | 1 | r2090.4 | 0 |
| Bit6 | Reserve - can be used as required (bit 8) | 1 | r2090.8 | 0 |
| Bit7 | Reserve - can be used as required (bit 9) | 1 | r2090.9 | 0 |
| Bit8 | Reserve - can be used as required (bit 11) | 1 | r2090.11 | 0 |
| Bit9 | Reserve - can be used as required (bit 12) | 1 | r2090.12 | 0 |
| Bit10 | Reserve - can be used as required (bit 13) | 1 | r2091.13 | 0 |
| Bit11 | Reserve - can be used as required (bit 14) | 1 | r2091.14 | 0 |
| Bit12 | Reserve - can be used as required (bit 15) | 1 | r2091.5 | 0 |
| Bit13 |  |  |  | 0 |
| Bit14 |  |  |  | 0 |
| Bit15 |  |  |  | 0 |

### Output interface of Sinalnfeed

#### Output interface of Sinalnfeed

| Output signal | Type | Default | Meaning |
| --- | --- | --- | --- |
| ENO | BOOL | 1 |  |
| Ready | BOOL | 1 | Ready for switching on (ZSW1.0) |
| Operation | BOOL | 0 | Ready for operation (ZSW1.1) |
| Run | BOOL | 0 | Running (ZSW1.2) |
| Fault | BOOL | 0 | Error infeed (ZSW1.3) |
| Lockout | BOOL | 0 | Infeed blocked (ZSW1.6) |
| Warning | BOOL | 0 | Warning infeed (ZSW1.7) |
| ZSW1 | WORD | 16#0 | Status word 1 |
| Error | BOOL | 0 | Error |
| DiagID | WORD | 0 | Expanded communication error RET_VAL from the system functions DPRD_DAT or DPWR_DAT (see also "Status" parameter) |
| Status | WORD | 16#0 | 16#7002: No error active  16#7200: Warning infeed  16#8400: Error pre-charging  16#8401: Error infeed  16#8600: Error: DPRD_DAT  16#8601: Error: DPWR_DAT |

### Error handling of the Sinalnfeed function block

#### Error handling of the function block SINA_INFEED

The "Error" output signals a general error, which is specified more precisely via the "Status" output.

If the inputs "EnablePrecharging" and "EnableInfeed" are set and the drive reports a fault, the control bits for the pre-charging and enabling are reset.

If the input "EnableInfeed" is set and "EnablePrecharging" is not set, the output "Error" = 1 and Status = 16#8400 is set. If the "EnablePrecharging" input is then reset to 1, the "Error" output is immediately reset to 0 (no acknowledgment necessary).

Communication between SIMATIC – CPU and infeed takes place via the system blocks "DPRD_DAT" and "DPWR_DAT".

If an error occurs during the processing of the system blocks, the output "Error" is set to 1 and the error message of the system function is output via the output "DiagID".

The "Status" output is set to 16#8600 (DPRD_DAT) or to 16#8601 (DPWR_DAT) depending on which system reports the error.

If an error is active for both system functions, the error message of the DPRD_DAT block is output first and if this is no longer active, the error message of the DPWR_DAT is output, if it is still active after this.

An infeed fault is displayed via the output "Fault" = 1 and "Status" = 16#8401 and can be acknowledged via the input "AckFault".

An infeed warning is displayed via the output "Warning" = 1 and "Status" = 16#7200.

If the block operates error-free, "Status" = 16#7002 is displayed at the output.

> **Note**
>
> **"AckFault" input**
>
> The "AckFault" input must be reset by the user because the error acknowledgment is expecting an edge change (0->1).
