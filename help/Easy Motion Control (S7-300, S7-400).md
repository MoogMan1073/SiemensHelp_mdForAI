---
title: "Easy Motion Control (S7-300, S7-400)"
package: ProgFBEMCenUS
topics: 36
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [MC_Init (S7-300, S7-400)](#mc_init-s7-300-s7-400)
- [MC_MoveAbsolute (S7-300, S7-400)](#mc_moveabsolute-s7-300-s7-400)
- [MC_MoveRelative (S7-300, S7-400)](#mc_moverelative-s7-300-s7-400)
- [MC_MoveJog (S7-300, S7-400)](#mc_movejog-s7-300-s7-400)
- [MC_Home (S7-300, S7-400)](#mc_home-s7-300-s7-400)
- [MC_StopMotion (S7-300, S7-400)](#mc_stopmotion-s7-300-s7-400)
- [MC_Control (S7-300, S7-400)](#mc_control-s7-300-s7-400)
- [MC_Simulation (S7-300, S7-400)](#mc_simulation-s7-300-s7-400)
- [MC_GearIn (S7-300, S7-400)](#mc_gearin-s7-300-s7-400)
- [Input driver (S7-300, S7-400)](#input-driver-s7-300-s7-400)
- [Output driver (S7-300, S7-400)](#output-driver-s7-300-s7-400)
- [Additional references for Easy Motion Control (S7-300, S7-400)](#additional-references-for-easy-motion-control-s7-300-s7-400)

## MC_Init (S7-300, S7-400)

### Description

The MC_Init prepares the initialization of all axis blocks by setting all bits in the "Init.Ix" bit array of the axis DB (see "[Initialization and parameter changes](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#initialization-and-parameter-changes-s7-300-s7-400)").

### Operating principle

instruction MC_Init **prevents the unintentional start of the axis** by setting the error displays "Error" = TRUE and "Err.StoppedMotion" = TRUE in the axis DB. If you want to move the axis after instruction MC_Init has been called, you must first cancel the error displays by acknowledging them (see [Error displays and error acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)).

instruction MC_Init checks the parameters in the axis DB. If a parameter error is detected, the "Error" and "Err.ConfigErr" bits are set in the Axis Db for the (group) error display, as well as one of the bits in the "ConfigErr" structure for a more detailed error display.

Parameter errors **cannot be acknowledged**. You must call instruction MC_Init again after correcting the error.

For more information on the error concept, refer to "[Error displays and error acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)" and "[Parameter errors](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#parameter-errors-s7-300-s7-400)".

### Call

> **Note**
>
> instruction MC_Init may only be called when the axis is at a standstill.

Call instruction MC_Init conditionally in the same program block in which you also call the other instructions of this axis. You must call instruction MC_Init in the following situations:

- After every startup of the CPU (OB 100 and OB 101)
- If you change a parameter that is identified by the following symbol in [Configuring the Axis TO](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#configuring-the-axis-to-s7-300-s7-400) without using the configuration software:

  ![Call](images/29245571339_DV_resource.Stream@PNG-de-DE.png)

  > **Note**
  >
  > Reset the condition used for calling instruction MC_Init once the call has been completed. Otherwise the Easy Motion Control blocks will always repeat only their initialization because the initialization bits in the axis DB are set again.

## MC_MoveAbsolute (S7-300, S7-400)

### Description

instruction MC_MoveAbsolute can be used to approach a synchronized axis to the absolute target specified in "Position".

### Operating principle

On detecting a positive edge at the "Execute" input, instruction MC_MoveAbsolute determines the direction of travel and accelerates the axis in this direction. On reaching the point of deceleration, the axis is slowed down. The specified velocity does not have to be reached during the movement.

**Special feature with a linear axis:**

- The direction of travel is determined from the setpoint position at the start and the target.

**Special features with a rotary axis:**

- instruction MC_MoveAbsolute limits the distance by which you can move the axis from a standstill to less than one rotary axis revolution. Use instruction [MC_MoveRelative](#mc_moverelative-s7-300-s7-400) to position the rotary axis with several revolutions.
- Polarity selection when starting from axis standstill:

  - Positive direction: target approached in a positive direction
  - Negative direction: target approached in a negative direction
  - Shortest distance: The target is approached in the direction in which the distance between start position and target is equivalent to ≤ ½ rev of the rotary axis.
- Polarity selection when overriding a motion

  - Positive direction: target approached in the positive direction. If the previous motion was in the negative direction, the axis is slowed down and the target is approached in the positive direction. If the target is reached exactly when slowing down with a negative travel direction, the axis then travels one revolution in the positive direction.
  - Negative direction: target approached in the negative direction. If the previous motion was in the positive direction, the axis is slowed down and the target is approached in the negative direction. If the target is reached exactly when slowing down with a positive travel direction, the axis then travels one revolution in the negative direction.
  - Shortest distance: The target is approached in the direction in which the distance between start position and target is equivalent to ≤ ½ rev of the rotary axis. If the braking distance is greater, the axis travels to the target in the original direction.
  - If you have selected travel parameters in such a ways that the braking distance of the previous movement is greater than one rotary axis revolution, the target is approached directly after direction reversal.
  - The entire distance between the start position and target may be greater than one rotary axis revolution.

**Signal flow diagram for** 
**MC_MoveAbsolute**

![Operating principle](images/29330561419_DV_resource.Stream@PNG-en-US.png)

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Execute | INPUT | BOOL | Start of positioning at a positive edge. |
| Position | INPUT | REAL | Absolute target position in [length unit]  Rotary axis: Start of rotary axis ≤ position < end of rotary axis |
| Velocity | INPUT | REAL | Axis velocity in [length unit/s] |
| Acceleration | INPUT | REAL | Axis acceleration in [length unit/s<sup>2</sup>] |
| Deceleration | INPUT | REAL | Axis deceleration in [length unit/s<sup>2</sup>] |
| Direction | INPUT | INT | Polarity selection for travel with rotary axis  -1 = Negative direction  0 = Shortest distance  1 = Positive direction |
| Busy | OUTPUT | BOOL | 1 = Job in progress. |
| Done | OUTPUT | BOOL | 1 = Job completed without error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| CommandAborted | OUTPUT | BOOL | 1 = Job was canceled by another job.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| Error | OUTPUT | BOOL | 1 = Job was canceled due to an axis error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |

### UDT2

A UDT2 data type is listed and reserved in the block properties of MC_MoveAbsolute. This means that no separate UDT2 data type may be used in the same project. This would result in error messages and inconsistencies within the project. If you want to use a UDT2 data type, this UDT must be renamed, for example, to UDT3.

## MC_MoveRelative (S7-300, S7-400)

### Description

instruction MC_MoveRelative can be used to traverse an axis by the distance that is specified in the "Distance" parameter and that is relative to the setpoint at the start of axis movement. The sign of the "Distance" parameter determines the direction.

### Operating principle

On detecting a positive edge at input "Execute", instruction MC_MoveRelative accelerates the axis in the direction that is specified in the "Distance" parameter. On reaching the point of deceleration, the axis is slowed down. The specified velocity does not have to be reached during the movement. The target is determined from the setpoint position at the start of travel and the distance to be traveled.

**Special feature of rotary axes:**

- You can realize travel over multiple revolutions by setting values in "Distance" that are greater than one revolution of the of the round axis.

**Signal flow diagram for** 
**MC_MoveRelative**

![Operating principle](images/29330561419_DV_resource.Stream@PNG-en-US.png)

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Execute | INPUT | BOOL | Start of positioning at a positive edge. |
| Distance | INPUT | REAL | Distance to be traversed in [length unit], relative to the last position setpoint.  The sign determines the direction of travel. |
| Velocity | INPUT | REAL | Axis velocity in [length unit/s] |
| Acceleration | INPUT | REAL | Axis acceleration in [length unit/s<sup>2</sup>] |
| Deceleration | INPUT | REAL | Axis deceleration in [length unit/s<sup>2</sup>] |
| Busy | OUTPUT | BOOL | 1 = Job in progress. |
| Done | OUTPUT | BOOL | 1 = Job completed without error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| CommandAborted | OUTPUT | BOOL | 1 = Job was canceled by another job.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| Error | OUTPUT | BOOL | 1 = Job was canceled due to an axis error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |

### UDT2

A UDT2 data type is listed and reserved in the block properties of MC_MoveRelative. This means that no separate UDT2 data type may be used in the same project. This would result in error messages and inconsistencies within the project. If you want to use a UDT2 data type, this UDT must be renamed, for example, to UDT3.

## MC_MoveJog (S7-300, S7-400)

### Description

instruction MC_MoveJog can be used to move an axis using two level-controlled directional inputs "JogPos" and "JogNeg" (jogging).

### Operating principle

Once you have set a directional input, MC_MoveJog accelerates the axis to the specified velocity. The axis moves in this direction as long as the directional input remains set. If you reset the directional input again, the axis slows down.

The two directional inputs are evaluated with the following dependencies:

- As long as one direction is selected, setting the opposite direction has no effect. No error is produced.
- To change direction during travel, set the other directional input to TRUE and at the same time set the originally selected directional input to FALSE.
- A start error will be generated if both inputs are set at the start of a movement ("Err.StartErr"; refer to [Errors with soft stop](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-with-soft-stop-s7-300-s7-400)).

**Special features of linear axes:**

- If the maximum travel distance during travel with a linear axis is exceeded, the MC_MoveJog instruction ramps down the axis to a standstill and the acknowledgeable error message "Err.DistanceErr" is output (refer to [Sequence of Travel Movements](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#sequence-of-travel-movements-s7-300-s7-400)). Then the axis can be moved again after the error has been acknowledged.
- A **non-synchronized** linear axis is not monitored and can therefore travel right to the physical end of the axis without slowing down. You must therefore complete the motion in time.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Non-synchronized linear axis**  Injury to persons and property may occur.  instruction MC_MoveJog can be used to traverse a non-synchronized linear axis to its mechanical end.  To avoid injury to persons and damage to objects, take the following precautions: - Install an EMERGENCY STOP switch in the vicinity of the computer. This is the only way to ensure that the system is reliably switched off in the event of a computer or software failure. - Install safety limit switches for direct control of the power units of all drives. - Ensure that nobody has access to the area of the system where there are moving parts. |  |
- A **synchronized** linear axis is decelerated when approaching the end of the working range and stops at the software limit switch. The acknowledgeable error message "Err.DistanceErr", as well as the "Err.SWLimitMinExceeded" or "Err.SWLimitMaxExceeded" error messages will be output. After the error has been acknowledged, it is only possible to travel in the opposite direction.

**Special features of rotary axes:**

- instruction MC_MoveJog does not limit the traversing distance of a rotary axis (infinite rotation).

**Signal flow diagram for** 
**MC_MoveJog**

![Operating principle](images/32957255819_DV_resource.Stream@PNG-en-US.png)

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| JogPos | INPUT | BOOL | 1 = Movement in positive direction as long as "JogPos" is set. |
| JogNeg | INPUT | BOOL | 1 = Movement in negative direction as long as "JogNeg" is set. |
| Velocity | INPUT | REAL | Axis velocity in [length unit/s] |
| Acceleration | INPUT | REAL | Axis acceleration in [length unit/s<sup>2</sup>] |
| Deceleration | INPUT | REAL | Axis deceleration in [length unit/s<sup>2</sup>] |
| Busy | OUTPUT | BOOL | 1 = Job in progress. |
| Done | OUTPUT | BOOL | 1 = Job completed without error.  After the axis has reached a standstill, the bit is set for exactly for the duration of one call of the instruction. |
| CommandAborted | OUTPUT | BOOL | 1 = Job was canceled by another job.  The bit remains active until the reset of "JogPos" or "JogNeg". |
| Error | OUTPUT | BOOL | 1 = Job was canceled due to an axis error.  The bit remains active until the reset of "JogPos" or "JogNeg". |

### UDT2

A UDT2 data type is listed and reserved in the block properties of MC_MoveJog. This means that no separate UDT2 data type may be used in the same project. This would result in error messages and inconsistencies within the project. If you want to use a UDT2 data type, this UDT must be renamed, for example, to UDT3.

## MC_Home (S7-300, S7-400)

### Description

instruction MC_Home is used for the following tasks:

- Reference point approach with incremental encoder ("Velocity" > 0)
- Set reference point with incremental and absolute encoder ("Velocity" = 0)   
  The set reference point function for absolute encoders is also known as absolute encoder adjustment.

### Operating principle

**Reference point approach ("**
**Velocity**
**" > 0)**

Once "Execute" has been set, the axis travels at the selected velocity and in the selected direction until the position decoder module distance and the input driver detect that the axis has reached the reference point. Once the reference point has been reached, the actual position value is set to the value specified in the"Position" parameter, and the axis is slowed down. The axis is now synchronized ("Sync" = TRUE), but is not positioned on the reference point.

If the [maximum travel distance](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#sequence-of-travel-movements-s7-300-s7-400) is exceeded in the reference point approach, instruction MC_Home slows down the axis to a standstill (refer to [Sequence of travel movements](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#sequence-of-travel-movements-s7-300-s7-400)) and the "Error" and "Err.DistanceErr" displays is set (refer to [Errors with soft stop](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-with-soft-stop-s7-300-s7-400)).

The axis will not be synchronized ("Sync" = FALSE) if the reference point approach is stopped before the reference point has been reached.

instruction MC_Home does not stop at the end of the axis, or automatically reverse the direction of movement.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| If no reference point is found, you must take suitable measures to ensure that the axis will come to a standstill before it reaches the mechanical end position (for example, EMERGENCY STOP switch, safety limit switch). |  |

**Set reference point ("**
**Velocity**
**" = 0)**

Set "Velocity" to 0. Once "Execute" has been set, the actual position value is set to the value specified in "Position" and the status bit in the axis DB is set simultaneously to "Sync" = TRUE.

Following a replacement of the absolute encoder or mechanical alterations, you must repeat the set reference point task, even if the axis is still synchronized.

> **Note**
>
> Rule for absolute encoders:
>
> The encoder value at the reference point is saved in the axis DB. For this reason, after setting the reference point, you should add the online axis DB to your offline database. Otherwise, the axis is no longer synchronized after you download the DB to the CPU.
>
> Read the information on [Loading the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#saving-and-loading-the-axis-data-block-s7-300-s7-400).

**Signal flow diagram for reference point approach**

![Operating principle](images/29338381579_DV_resource.Stream@PNG-en-US.png)

**Signal flow diagram for reference point setting**

![Operating principle](images/29340048651_DV_resource.Stream@PNG-en-US.png)

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

The reference point approach or reference setting can only be started when the axis is at a standstill.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Execute | INPUT | BOOL | Start of reference point approach or reference setting with a positive edge. |
| Position | INPUT | REAL | **Incremental encoder** Reference point coordinate for reference point approach or reference setting.   **Absolute encoder** Reference point coordinate for reference setting.  The value must be within the working range:  - **Linear axis** Within the software limit switch - **Rotary axis:**    Rotary axis start ≤ position < Rotary axis end |
| Velocity | INPUT | REAL | Axis velocity in [length unit/s]  Velocity > 0: Reference point approach  Velocity = 0: Set reference point |
| Acceleration | INPUT | REAL | Axis acceleration in [length unit/s<sup>2</sup>] |
| Deceleration | INPUT | REAL | Axis deceleration in [length unit/s<sup>2</sup>] |
| Direction | INPUT | INT | Start direction for reference point approach  1 = Reference point approach in positive direction  -1 = Reference point approach in negative direction |
| Busy | OUTPUT | BOOL | 1 = Job in progress. |
| Done | OUTPUT | BOOL | 1 = Job completed without error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| CommandAborted | OUTPUT | BOOL | 1 = Job was canceled by another job.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| Error | OUTPUT | BOOL | 1 = Job was canceled due to an axis error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |

## MC_StopMotion (S7-300, S7-400)

### Description

instruction MC_StopMotion allows you to interrupt any travel instruction so that the axis comes to a standstill with the set deceleration.

Typical application: A positioning job can by interrupted at any time due to an external event (for example, opening of a safety door).

### Operating principle

On detecting the positive edge at input "Execute", the MC_StopMotion instruction takes control of the axis and slows it down to a standstill. The MC_StopMotion instruction can only be interrupted by [hard faults](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-with-hard-stop-s7-300-s7-400) and not by a travel instruction. After the axis has reached a standstill, a new travel movement can be started.

You can set a deceleration value at the MC_StopMotion instruction to suit your application. If this deceleration value is less than the one set in the interrupted instruction, the axis is slowed down with this deceleration value. This ensures that the axis does not overshoot the target set in the interrupted block.

If you interrupt a movement with target (MC_MoveAbsolute, MC_MoveRelative) by calling instruction MC_StopMotion, the instruction continues to calculate the remaining distance. On termination of instruction MC_StopMotion, the remaining distance indicates the distance of the current position setpoint to the target of the interrupted block. You can assign this value to an MC_MoveRelative instruction in order to approach the axis to the original target after interruption.

**Signal flow diagram for** 
**MC_StopMotion**

![Operating principle](images/29343754123_DV_resource.Stream@PNG-en-US.png)

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Execute | INPUT | BOOL | Start of braking with a positive edge |
| Deceleration | INPUT | REAL | Axis deceleration for deceleration ramp in [length unit/s<sup>2</sup>]  If you enter values <= 0.0, the maximum deceleration value from the axis DB will be used. |
| Busy | OUTPUT | BOOL | 1 = Job in progress. |
| Done | OUTPUT | BOOL | 1 = Job completed without error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |
| CommandAborted | OUTPUT | BOOL | 1 = Job was cancelled due to manual intervention at the controller. |
| Error | OUTPUT | BOOL | 1 = Job was canceled due to an axis error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |

## MC_Control (S7-300, S7-400)

### Description

instruction MC_Control allows you to implement the position control in combination with the I/O drivers.

instruction MC_Control may assume the following controller states:

- Control mode
- Follow-up mode
- Manual mode

### Control mode

The MC_Control instruction

- Calculates the velocity setpoint for the output driver as a function of the position setpoint of a travel instruction and actual position value of the input driver.
- Monitors

  - Standstill
  - Target approach
  - Following error
- Processes error acknowledgment (see [Error displays and error acknowledgment](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400))

### Follow-up mode

In this state, the setpoint position is corrected according to the actual position. The follow-up mode is activated if "EnableDrive" = FALSE, or after an axis fault with hard stop (refer to [Error displays and error acknowledgment](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)). Output "DriveEnabled" = FALSE in follow-up mode.

### Manual mode

In this mode, the manual setpoint "[ManVelocity](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#specifying-the-velocity-setpoint-in-manual-mode-s7-300-s7-400)" is output as the velocity setpoint. This setpoint is limited to "[MaxVelocity](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#specifying-the-maximum-axis-velocity-s7-300-s7-400)". The position setpoint is tracked to the actual position value.

This state is switched on or off using ["ManEnable"](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#specifying-the-velocity-setpoint-in-manual-mode-s7-300-s7-400).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Manual control is possible at any time, even if the axis is in error status. |  |

### Operating principle

The proportional element of the control algorithm of instruction MC_Control is configured at the "[controller gain](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#specifying-controller-gain-s7-300-s7-400)" parameter ("FactorP").

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

Call instruction MC_Control once per axis unconditionally in the selected OB.

### Parameter

| Parameter | Declaration | Data type | Meaning |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 0 = Disable drive, tracking control is active.  1 = Enable drive, position control is active.  If no error is pending, "DriveEnabled" is set. |
| DriveEnabled | OUTPUT | BOOL | Drive enable, position control is active.  If "EnableDrive" is set and no error is pending, "DriveEnabled" is set. If "DriveEnabled" is not set, the axis is in follow-up mode and standstill monitoring is not active for the axis.  This signal should be used in order to control the enable input on the power unit. |

## MC_Simulation (S7-300, S7-400)

### Description

instruction MC_Simulation allows you to test your traversing program and driver blocks. You do not require any I/O and your axis is not moved.

### Operating principle

instruction MC_Simulation feeds back the controller output value to the input driver by simulating an encoder value corresponding to the encoder type selected in the axis DB.

To activate simulation mode, set the bit "Sim" = TRUE in the axis DB.

When simulation is enabled, a reference point approach is not possible. When in simulation mode, configure the "Velocity" input of instruction MC_Home with the value 0.0. This means that a reference setting will be performed instead of a reference point approach.

If you set a reference point in simulation mode, the reference point of your real axis is also altered. It is therefore necessary to resynchronize your axis after exiting simulation mode.

Whenever you activate and deactivate simulation mode, the axis is set to the stop status that requires acknowledgment (refer to [Faults with hard stop](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-with-hard-stop-s7-300-s7-400)) and all bits of the "Init.Ix" bit array is set in the axis DB.

If simulation mode is enabled, the following occurs:

- The output driver does not output values to the I/O.
- The input driver does not read in any encoder values from the I/O.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| The axis must be at a standstill when simulation mode is enabled. |  |

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

## MC_GearIn (S7-300, S7-400)

### Description

instruction MC_GearIn allows you to link the velocity setpoint of a following axis to the velocity setpoint of a leading axis by means of gear ratio (setpoint coupling).

### Operating principle

As soon as a positive edge is detected at the "Execute" input, instruction MC_GearIn couples a following axis (parameter "Slave") to the velocity or position setpoint of a leading axis (parameter "Master") by means of the set gear ratio. The instruction therefore represents a travel instruction of the following axis.

The values in each cycle of a coupled motion are as follows:

- The distance traversed by the following axis, starting at the coupling position =   
  the distance traversed by the leading axis, starting at the coupling position x gear ratio
- Velocity of the following axis = gear velocity =   
  velocity of the leading axis x gear ratio
- Acceleration of the following axis =   
   acceleration of the leading axis x gear ratio
- Deceleration of the following axis =   
  deceleration of the leading axis x gear ratio

To allow the following axis to follow the leading axis without restriction, set the following values (with a reserve factor of 1.1) for the following axis. These values must be valid and attainable:

- Velocity(following axis) =   
  Velocity(leading axis) × ABS(gear ratio) × 1.1
- Acceleration(following axis) =   
  Acceleration(leading axis) × ABS(gear ratio) × 1.1
- Deceleration(following axis) =   
  Deceleration(leading axis) × ABS(gear ratio) × 1.1

To cancel the coupling, call the stop instruction, or any other travel instruction for the following axis.

As with all other travel instructions, the MC_GearIn instruction can override a movement and be overridden itself.

The following axis can be coupled to a moving leading axis, whereby the following axis automatically accelerates or decelerates using the ramps configured at the gear instruction until it has reached the gear velocity.

The "InGear" output is set when the gear velocity has been reached for the first time after the start of the motion. If "Execute" is not set at this point, "InGear" remains active for one call of the instruction. "InGear" is reset at the high to low transition at Execute, when an error has occurred, and when a movement is overridden.

Provided the gear velocity can be reached, the following axis travels in speed and position synchronism. The "Coupled" output of the instruction is set.

If the following axis cannot reach the gear velocity, it moves according to the motion parameters set at the gear instruction. The "Coupled" output of the instruction is then reset. As soon as the gear velocity can be reached again, the following axis moves at this velocity. The "Coupled" output of the instruction is set.

As long as instruction MC_GearIn is active at the following axis, you can call any travel instruction for the leading axis, and also override a movement.   
**Exception:** During referencing of the leading axis, the coupling is released with an error ("Err.MasterErr").

The "Override" axis parameter is useless for the following axis and is therefore not evaluated.

**Special features when operating a following axis as linear axis:**

- If the maximum traversing distance is exceeded during a gear movement, instruction MC_GearIn slows down the following axis to a standstill with the error message (see [Sequence of travel movements](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#sequence-of-travel-movements-s7-300-s7-400)). The coupling is released.
- A **non-synchronized** linear axis is not monitored and can therefore travel right to the physical end of the axis without slowing down. You must therefore complete the motion in time.
- A **synchronized** linear axis is decelerated when approaching the end of the working range and stops at the software limit switch. The error message "DistanceErr" is output along with "Err.SWLimitMinExceeded", or "Err.SWLimitMaxExceeded". The coupling is released.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Injury to persons and property may occur.  instruction MC_GearIn can be used to traverse a non-synchronized linear axis to its mechanical end.  To avoid injury to persons and objects, take the following precautions:  - Install an EMERGENCY STOP switch in the vicinity of the computer. This is the only way to ensure that the system is reliably switched off in the event of a computer or software failure. - Install safety limit switches for direct control of the power units of all drives. - Ensure that nobody has access to the area of the system where there are moving parts. |  |

**Special feature when operating a following axis as rotary axis:**

- The traversing distance of instruction MC_GearIn is not limited (infinite rotation).

### Error handling

**Master axis errors:**

- The leading axis decelerates when it detects errors that result in a soft stop. The coupled following axis follows this motion and does not release the coupling. If the leading axis error is acknowledged, and the leading axis continues its motion, the following axis also resumes the motion.
- If the leading axis detects errors that result in a hard stop, or if it is operated in manual mode, the gear instruction decelerates the following axis and resolves the coupling. The instruction outputs the "Err.MasterErr" error message.

**Slave axis errors:**

- If the following axis detects errors that result in a soft stop, the gear instruction decelerates the following axis and resolves the coupling.
- If the following axis detects errors that result in a hard stop, the following axis is brought to a stop, and the coupling is released.
- The maximum traversing distance of the coupling movement of a linear axis is limited to 2<sup>24</sup> increments or 2<sup>24</sup> [length unit]. If this limit is exceeded, instruction MC_GearIn decelerates the following axis, outputs a "DistanceErr" error message that you can acknowledge, and resolves the coupling.

**Coupling errors:**

- The following axis travels according to the motion parameters set at the instruction if it cannot reach the gear velocity in the current cycle. This applies particularly when the axis is coupled to a moving leading axis and during a braking operation triggered by an error.

  The "Coupled" parameter is reset, but the coupling is not released. As soon as the following axis is capable of reaching the necessary values again, it travels according to these values and "Coupled" is set again.

### Interaction of instructions for the gear

When using a gear instruction, you should also note the following aspects (refer to "[Structure of a user program](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#user-program-setup-s7-300-s7-400)"):

- The leading and following axes must be called in the **same** execution level.
- In each processing cycle, the following axis adapts itself again to the default values of the leading axis. The following axis instructions should therefore be called after instructions of the leading axis. In particular, the gear instruction of the leading axis should be called **after** the controller of the leading axis.  
  Other call sequences, in particular nested calls of the instructions of the leading and following axes, may lead to greater following errors.
- In isochronous applications, the I/O data of the leading axis **and** the following axis must be located in the same process image partition.

This results in one of the following figures, depending on the selected structure:

![Interaction of instructions for the gear](images/29344361995_DV_resource.Stream@PNG-en-US.png)

### Signal Flow Chart

The chart below shows how the gear instruction takes control of the axis movement and couples to a moving leading axis. In this example, the gear ratio is 0.8. The following axis cannot reach the velocity required to maintain this ratio.

The leading axis is stopped between t = 0.5 and t = 0.72. The coupling is maintained.

![Signal Flow Chart](images/29348256267_DV_resource.Stream@PNG-en-US.png)

### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Execute | INPUT | BOOL | Start of the gear motion on a positive edge |
| Rationumerator | INPUT | REAL | Gear ratio numerator  Gear ratio = "RatioNumerator" / "RatioDenominator"  If "RatioNumerator" < 0, the direction of movement of the leading axis is opposite to that of the following axis.  "RatioNumerator" = 0 is rejected with "DataErr" = 1.   You can modify the effective gear ratio of the following axis by overriding the active gear instruction with another instance that contains a modified gear ratio. |
| RatioDenominator | INPUT | INT | The gear ratio denominator; must be an integer ≥ 1  You can modify the effective gear ratio of the following axis by overriding the active gear instruction with another instance that contains a modified gear ratio. |
| Velocity | INPUT | REAL | Axis velocity in [length unit/s]  The maximum geared velocity of the following axis is limited to this value. |
| Acceleration | INPUT | REAL | Axis acceleration in [length unit/s<sup>2</sup>]  The maximum geared acceleration of the following axis is limited to this value.  This parameter is used if:  - The following axis is coupled to a faster leading axis. - The acceleration of the leading axis exceeds the capability of the following axis. |
| Deceleration | INPUT | REAL | Axis deceleration in [length unit/s<sup>2</sup>]  The maximum geared deceleration of the following axis is limited to this value.  This parameter is used if:  - A following axis that is already in motion is coupled to a slower leading axis. - The following axis is brought to a stop due to an error. - The deceleration of the leading axis exceeds the capability of the following axis. |
| Master | IN-OUT | AXIS_REF | Reference to the leading axis data |
| Slave | IN-OUT | AXIS_REF | Reference to the following axis data |
| Init | IN-OUT | BOOL | If Init = TRUE, the instruction completes its initialization and then resets the bit. |
| Busy | OUTPUT | BOOL | 1 = Job in progress. |
| InGear | OUTPUT | BOOL | 1 = Gear speed reached  Set the first time the gear velocity has been reached. If "Execute" is already reset at this point, "InGear" still remains active for one call of the instruction.  It is reset at the high to low transition at Execute, when an error has occurred, and when the movement is overridden. |
| Coupled | OUTPUT | BOOL | 1 = Axis is currently coupled to the leading axis.  Reports in each processing cycle whether the gear speed was reached. |
| CommandAborted | OUTPUT | BOOL | 1 = Job was canceled by another job. |
| Error | OUTPUT | BOOL | 1 = Job was canceled due to an axis error.  The bit remains active at least for one call of the instruction until "Execute" is reset. |

## Input driver (S7-300, S7-400)

This section contains information on the following topics:

- [Task of the input driver (S7-300, S7-400)](#task-of-the-input-driver-s7-300-s7-400)
- [EncoderIM178 (S7-300, S7-400)](#encoderim178-s7-300-s7-400)
- [EncoderFM450 (S7-300, S7-400)](#encoderfm450-s7-300-s7-400)
- [EncoderET200S1SSI (S7-300, S7-400)](#encoderet200s1ssi-s7-300-s7-400)
- [EncoderAbsSensorDP (S7-300, S7-400)](#encoderabssensordp-s7-300-s7-400)
- [EncoderSM338 (S7-300, S7-400)](#encodersm338-s7-300-s7-400)
- [EncoderET200S1Count (S7-300, S7-400)](#encoderet200s1count-s7-300-s7-400)
- [EncoderFM350 (S7-300, S7-400)](#encoderfm350-s7-300-s7-400)
- [EncoderCPU314C (S7-300, S7-400)](#encodercpu314c-s7-300-s7-400)
- [EncoderIM174 (S7-300, S7-400)](#encoderim174-s7-300-s7-400)
- [EncoderSINAMICS (S7-300, S7-400)](#encodersinamics-s7-300-s7-400)
- [EncoderUniversal (S7-300, S7-400)](#encoderuniversal-s7-300-s7-400)

### Task of the input driver (S7-300, S7-400)

#### Function

This input driver is used to detect the actual positions of an axis. It reads the non-standardized axis position and converts this to the selected unit of length.

Suitable input drivers are available for a number of position decoder modules. These drivers are described individually in the following sections. Adaptation to configurations that are not directly supported is possible by means of instruction [EncoderUniversal](#encoderuniversal-s7-300-s7-400).

#### Initialization

- [Synchronization](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#synchronization-s7-300-s7-400) of an **incremental encoder** with the axis is reset (parameter "Sync" = FALSE in the axis data). A new reference point approach or reference setting is then necessary.
- Synchronization of an **absolute encoder** with the axis is retained.

#### Call

The input driver of an axis must be called unconditionally.

#### Isochronous mode

The input drivers support the isochronous mode of all suitable I/O modules. The driver automatically recognizes isochronous mode by the fact that it is called in an isochronous OB.

#### Error handling

Errors can be detected by means of the following mechanisms:

- An error detected by the user program (for example, module removed, or station failure) can be signaled to the input driver at input "EncErr". The input driver will not access the position decoder module as long as input "EncErr" is TRUE.
- Some position decoder modules provide error information that is evaluated automatically by the input driver.
- Other position decoder modules only return their error information by means of diagnostic interrupt and data set 1 (DS1). You must therefore perform the following steps:

  - Enable the diagnostics interrupt for the module in the hardware configuration.
  - In OB 82, compare the address returned in the local data element "OB82_MDL_ADDR" with your module address. If these agree, set the "ReadDiagErr" parameter of the input driver to TRUE (for the incoming and outgoing alarm).  
    If "ReadDiagErr" = TRUE, the input driver reads DS 1 of the module by calling instruction RD_REC, saves this record to the static "DiagStatus" parameter  
     and then sets "ReadDiagErr" = FALSE. The return value of instruction RD_REC is written to the static "JobErr" parameter.

#### Error Response

- In the event of an error, the"Error" and "Err.EncoderErr" displays is set in the axis DB.
- With **incremental encoder**, status bit "Sync" is always reset in the axis DB.
- With **absolute encoder**, status bit "Sync" is never reset in the axis DB.

Please also note specific error handling in the following sections on individual drivers.

For detailed information on error response, error display, and error acknowledgment, see "[Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)".

#### Simulation mode

The input driver will not access the position decoder module as long as input "[Sim](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#activating-simulation-mode-s7-300-s7-400)" is set in the axis DB. The encoder values are simulated by means of instruction [MC_Simulation](#mc_simulation-s7-300-s7-400).

### EncoderIM178 (S7-300, S7-400)

#### Description

instruction EncoderIM178 is included for reasons of compatibility with STEP7  V5.x. Siemens is no longer actively marketing the IM 178‑4 . You can use IM 174 as an alternative.

IM 178‑4 must be used with the same channel number and axis both at the input **and** output drivers, as specific address settings refer to both drivers. A combination with other drivers is not possible.

#### Configuration of IM 178‑4 (hardware configuration)

Select the IM 178‑4 from the "Distributed I/O devices" section in the hardware catalog. Configure slot 4 of IM 178‑4 as "4Word QQ/12Word QI/cons. 1Word".

| Parameter | Setting |
| --- | --- |
| Synchronization | Software |
| Edge selection | Rising, falling, or both edges |

Configure the other settings depending on the connected encoder.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| RefMode | INPUT | BOOL | Referencing type:  0 = With digital input I0  1 = With digital input I1 and zero mark |
| DI_0 | OUTPUT | BOOL | Digital input 0 of the corresponding channel of IM 178‑4 |
| DI_1 | OUTPUT | BOOL | Digital input 1 of the corresponding channel of IM 178‑4 |
| DI_2 | OUTPUT | BOOL | Digital input 2 of the corresponding channel of IM 178‑4 |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| Status.PARA | STAT | BOOL | PARA = TRUE: IM 178‑4 was correctly configured by means of the hardware configuration.   PARA = FALSE: see [SIMATIC IM 178‑4 Drive Interface Manual](http://support.automation.siemens.com/WW/view/en/1117389) |
| Status.EXTF0 | STAT | BOOL | 1 = Encoder signal line fault |
| Status.EXTF1 | STAT | BOOL | 1 = Encoder error |
| Status.EXTF2 | STAT | BOOL | 1 = Zero mark fault |

#### Synchronization

Synchronization can be performed by:

- Reference point approach (with incremental encoder)
- Reference point setting (with incremental and absolute encoder)

Depending on the setting, connect the reference point switch to digital input I0 or I1.

During a reference point approach, IM 178‑4 can detect the reference point in either of the following cases:

- At a negative edge, positive edge, or at both edges at digital input I0 (RefMode = 0).
- At the positive edge of the first zero mark after detecting the negative edge of digital input I1 (RefMode = 1).

If the axis is already positioned on the reference point switch at the time the reference point approach is started, it is referenced to the current position, as is the case with reference point setting.

#### Digital Inputs

The digital inputs I0 to I2 of the selected channel of IM 178‑4 are indicated at the output parameters "DI_0" to "DI_2" of the input driver.

#### Error handling

In response to a detected error, the input driver sets the "Error" and "Err.EncoderErr" error codes in the axis DB. The input driver resets the "Sync" status bit in the axis DB if you are using an incremental encoder. For more information, refer to the [SIMATIC IM 178‑4 Drive Interface Manual](http://support.automation.siemens.com/WW/view/en/1117389).

For detailed information on error response, error display, and error acknowledgment, see "[Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)".

#### Error acknowledgment

If you set error acknowledgment in the axis DB of Easy Motion Control, errors pending in the module are also acknowledged.

### EncoderFM450 (S7-300, S7-400)

#### Description

instruction EncoderFM450 is used to employ a channel of the FM 450‑1 as position decoder module for incremental encoders. The channel number is configured at the axis DB.

#### Configuration of the module (hardware configuration)

The FM 450‑1 module should be configured in accordance with the settings listed in the following table.

| Dialog | Setting |
| --- | --- |
| Interrupt selection | Enable diagnostic interrupt |
| Operating modes | - Count range: -31 to +31 bits - Operating mode: Continuous counting - Gate control: None |
| Inputs | If you want to perform a reference point approach, you must select the following setting:  - Synchronization: once - The setting "Evaluate zero mark for setting" may be selected or cleared as a reference point criterion. |

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| ReadDiagErr | IN-OUT | BOOL | Set this bit in OB 82 if the module has triggered a diagnostic interrupt (see below under Error handling). |
| DI_0 | OUTPUT | BOOL | Digital input 0 of the selected channel |
| DI_1 | OUTPUT | BOOL | Digital input 1 of the selected channel |
| DI_2 | OUTPUT | BOOL | Digital input 2 of the selected channel |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| JobErr | STAT | INT | Return value of instruction RD_REC, if "ReadDiagErr" = TRUE was set. |
| DiagStatus.EXT_VOLTAGE | STAT | STRUCT | External auxiliary voltage faulty |
| DiagStatus.CONFIG_ERR | STAT | STRUCT | Incorrect configuration |
| DiagStatus.WTCH_DOG_FLT | STAT | STRUCT | Watchdog timeout |
| DiagStatus.RAM_FLT | STAT | STRUCT | RAM failure |
| DiagStatus.CH1_SIGA | STAT | STRUCT | Channel 1 signal A defective |
| DiagStatus.CH1_SIGB | STAT | STRUCT | Channel 1 signal B defective |
| DiagStatus.CH1_SIGZ | STAT | STRUCT | Channel 1 signal N defective |
| DiagStatus.CH1_BETW | STAT | STRUCT | Channel 1 fault between channels |
| DiagStatus.CH1_5V2 | STAT | STRUCT | Channel 1 encoder supply 5.2 V fault |
| DiagStatus.CH2_SIGA | STAT | STRUCT | Channel 2 signal A defective |
| DiagStatus.CH2_SIGB | STAT | STRUCT | Channel 2 signal B defective |
| DiagStatus.CH2_SIGZ | STAT | STRUCT | Channel 2 signal N defective |
| DiagStatus.CH2_BETW | STAT | STRUCT | Channel 2 fault between channels |
| DiagStatus.CH2_5V2 | STAT | STRUCT | Channel 2 encoder supply 5.2 V fault |

#### Synchronization

Synchronization can be performed by:

- Reference point approach or
- Set reference point

Connect the reference point switch to digital input I2.

During a reference point approach, the module can detect the reference point in either of the following cases:

- On a rising edge at digital input I2
- On the rising edge of the zero mark, if digital input I2 is set

If the axis is already positioned on the reference point switch at the time the reference point approach is started, it is referenced to the current position, as is the case with reference point setting.

#### Digital inputs

Digital inputs I0 to I2 of the selected channel are indicated at the output parameters "DI_0" to "DI_2" of the input driver.

#### Error handling

The module returns its error information by means of dataset 1 (DS1). In the following situations, the input driver reads DS1 from the module by calling instruction RD_REC and saves it to the static "DiagStatus" parameter:

- The input driver is initialized.
- The module reports an error.
- The driver input parameter "ReadDiagErr" is TRUE.

It then sets "ReadDiagErr" = FALSE. The return value of instruction RD_REC is written to the static "JobErr" parameter (see [JOB_Err alarms](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#job_err-interrupts-s7-300-s7-400)).

If an error display is registered in dataset 1, the input driver sets the error codes "Error" and "Err.EncoderErr" to TRUE in the axis DB. Status bit "Sync" is set to FALSE.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

> **Note**
>
> If you are using an FM 450‑1 in single-channel mode only, you must configure the second channel with "24 V channel A+B phase offset", as it will otherwise transmit cyclic diagnostic interrupts (for example, due to missing circuitry).

### EncoderET200S1SSI (S7-300, S7-400)

#### Description

instruction EncoderET200S1SSI is used to employ the ET 200S 1SSI Fast Mode as position decoder module for absolute encoders.

The driver can also be used for the isochronous variant of this module.

#### Configuration the ET 200S 1SSI Fast Mode module (hardware configuration)

The input driver is only suitable for the 1SSI module with "**Fast Mode**" parameter setting as operating mode. In the TIA Portal, the "**Fast Mode**" is no longer selected based on the module, but is now set as operating mode.

Select the module from the "Distributed I/O devices" > ET 200S > FM > Position detection" section in the hardware catalog.

| Parameter | Setting |
| --- | --- |
| Group diagnostics | You can activate this function if you want to evaluate the data in your program. |
| Detection | Freewheeling |
| Reversal of the direction of rotation | Deactivated  You can reverse the direction of rotation using the instructions of Easy Motion Control (parameter "[Set encoder polarity](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#selecting-the-encoder-polarity-s7-300-s7-400)"). |
| Operating mode | Fast mode |

Configure the other settings depending on the connected encoder.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| Status.STS_UP | STAT | BOOL | Forward direction: encoder values increase |
| Status.STS_DN | STAT | BOOL | Reverse direction: encoder values decrease |
| Status.STS_DI | STAT | BOOL | Status of digital input |
| Status.EXTF | STAT | BOOL | Group error or short circuit in encoder supply |
| Status.ERR_PARA | STAT | BOOL | Parameter errors |
| Status.RDY | STAT | BOOL | Module is ready for operation |

#### Synchronization

The ET 200S 1SSI Fast Mode module only supports synchronization by means of reference point setting.

#### Error handling

If the input driver detects an error report of the module, it sets the error codes "Error" and "Err.EncoderErr" in the axis DB.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

### EncoderAbsSensorDP (S7-300, S7-400)

#### Description

instruction EncoderAbsSensorDP is used to employ the absolute encoder SIMODRIVE sensor in combination with PROFIBUS DP for position detection.

#### Configuration of the absolute encoder SIMODRIVE sensor (hardware configuration)

Select the "PROFIBUS DP > ENCODER > SIMODRIVE sensor > Version 2.2 Single-turn or Version 2.2 Multiturn" encoder from the hardware catalog. If the SIMODRIVE sensor is not yet available, implement the device using the corresponding GSD file. The encoder will then be available in the "Additional field devices > PROFIBUS DP > Encoder > Siemens AG > SIMODRIVE sensor" folder.

| Parameter | Setting |  |
| --- | --- | --- |
| Code sequence | Increasing clockwise  You can reverse the direction of rotation using the instructions of Easy Motion Control (parameter "[Set encoder polarity](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#selecting-the-encoder-polarity-s7-300-s7-400)"). |  |
|  | **Multiturn** | **Single-turn** |
| Scaling function | Enable | Enable |
| Measuring steps (high) | 0 | - |
| Measuring steps (low) | 4096 | 4096 |
| Physical impulses (high) | 0 | - |
| Physical impulses (low) | 4096 | 4096 |
| Desired measuring units per | Revolution | Revolution |
| Total measuring range (high) | 256 | - |
| Total measuring range (low) | 0 | 4096 |
| Commissioning mode | Switched off | Switched off |
| Shorter diagnostics | No | No |
| Lower limit switch | Switched off | Switched off |
| Lower limit switch (high) | 0 | - |
| Lower limit switch (low) | 0 | 0 |
| Upper limit switch | Switched off | Switched off |
| Upper limit switch (high) | 0 | - |
| Upper limit switch (low) | 32767 | 4096 |
| Velocity output unit | Steps/1000 ms | Steps/1000 ms |

Adapt the setting to your selected length unit using the instructions of Easy Motion Control. Fixed parameters can therefore be assigned to the encoder - as indicated above. It is not necessary to perform a "teach-in" of the encoder (refer to the [SIMODRIVE sensor absolute encoder with PROFIBUS DP Operating Manual](http://support.automation.siemens.com/WW/view/en/28813901)).

At the parameter "steps per encoder revolution" of Easy Motion Control, enter 4096 ("[StepsPerRev](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#specifying-the-steps-per-encoder-revolution-s7-300-s7-400)").

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| Status.Ready | STAT | BOOL | 1 = Encoder is ready for operation |
| Status.Mode | STAT | BOOL | Operating mode: 0 = Startup mode, 1 = Normal mode |
| Status.SWLimitExceeded | STAT | BOOL | 1 = Software limit switch MIN or MAX has responded |
| Status.Dir | STAT | BOOL | Direction of rotation: 0 = Clockwise, 1 = Counter-clockwise |

#### Synchronization

Synchronization with the absolute encoder SIMODRIVE sensor is only possible by means of reference point setting.

#### Error handling

If the input driver detects that an encoder error alarm is pending, it sets the"Error" and "Err.EncoderErr" error codes in the axis DB. For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

### EncoderSM338 (S7-300, S7-400)

#### Description

instruction EncoderSM338 is used to employ SM 338 POS_INPUT as position decoder module for absolute encoders.

The driver can also be used for the isochronous variant of this module.

#### Configuration of SM 338 (hardware configuration)

The FREEZE function must be deactivated.

If the input driver detects a FREEZE status at the encoder input, it sets the "Error" and "Err.EncoderErr" error codes in the axis DB.

Configure the other settings depending on the connected encoder.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| ReadDiagErr | IN-OUT | BOOL | Set this bit in OB 82 if the module has triggered a diagnostic interrupt (see Error handling). |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| Freeze | STAT | BOOL | FREEZE status of the encoder input |
| JobErr | STAT | INT | Return value of instruction RD_REC, if "ReadDiagErr" = TRUE was set. |
| DiagStatus.EXT_VOLTAGE | STAT | STRUCT | External auxiliary voltage faulty |
| DiagStatus.CONFIG_ERR | STAT | STRUCT | Incorrect configuration |
| DiagStatus.WTCH_DOG_FLT | STAT | STRUCT | Watchdog timeout |
| DiagStatus.RAM_FLT | STAT | STRUCT | RAM failure |
| DiagStatus.CH0_INTF | STAT | STRUCT | Configuration or parameter assignment error (internal channel error) |
| DiagStatus.CH0_EXTF | STAT | STRUCT | Encoder error (external channel error) |

#### Synchronization

Synchronization with SM 338 is only possible by means of reference point setting.

#### Error handling

This module only provides its error information via diagnostic interrupt and data record 1 (DS1). You must therefore perform the following steps:

- Enable the diagnostics interrupt for the module in the hardware configuration.
- In OB 82, compare the address returned in the local data element "OB82_MDL_ADDR" with your module address. If these agree, set the ReadDiagErr parameter of the input driver to TRUE (for the incoming and outgoing interrupt).

  If "ReadDiagErr" = TRUE, the input driver reads dataset 1 of the module by means of instruction RD_REC and saves it to the static "DiagStatus" parameter.

  It then sets "ReadDiagErr" = FALSE. The return value of instruction RD_REC is written to the static "JobErr" parameter (see [JOB_Err alarms](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#job_err-interrupts-s7-300-s7-400)).

If an error display is registered in dataset 1, the input driver sets the error codes "Error" and "Err.EncoderErr" to TRUE in the axis DB.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

### EncoderET200S1Count (S7-300, S7-400)

#### Description

instruction EncoderET200S1Count is used to employ the ET 200S 1Count5V or 1Count24V module as position decoder module for incremental encoders.

The driver can also be used for the isochronous variant of this module.

#### Configuration of the ET 200S 1Count module (hardware configuration)

The input driver is only suitable for the "1 Count 5V" or "1 Count 24V" from the hardware catalog. The count mode is now set as the operating mode instead of be selecting via the module.

Select the module from the "Distributed I/O devices" > ET 200S > FM > Counting" section in the hardware catalog.

| Parameter | Setting |
| --- | --- |
| Group diagnostics | You can activate this function if you want to evaluate the data in your program. |
| Type of counting mode | Continuous counting |
| DI function,  Synchronization | - If you wish to perform a reference point approach, select:   - DI function = Synchronization at positive edge   - Synchronization = One-time - Otherwise select:   - DI function = input |
| Gate function | Arbitrary |
| Operating mode | Count |

Configure the other settings depending on the connected encoder.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| DOut_1 | INPUT | BOOL | Digital output 1 |
| DOut_2 | INPUT | BOOL | Digital output 2 (only available with 1Count5V) |
| DIn | OUTPUT | BOOL | Digital input of module |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| Status.ERR_ENCODER | STAT | BOOL | Short circuit / wire break at encoder signal (only with 1Count5V) |
| Status.ERR_DO2 |  | BOOL | Short circuit / wire break / overheating DO2  (only with 1Count5V) |
| Status.ERR_PARA |  | BOOL | Parameter errors |
| Status.ERR_DO1 |  | BOOL | Short circuit / wire break / overheating DO1 |
| Status.ERR_24V |  | BOOL | Short circuit encoder supply |

#### Synchronization

Synchronization can be performed by:

- Reference point approach or
- Reference setting

Connect the reference point switch to digital input DI.

During a reference point approach, ET 200S 1Count is capable of detecting the reference point based a rising edge at digital input DI.

If the axis is already positioned on the reference point switch at the time the reference point approach is started, it is referenced to the current position, as is the case with reference point setting.

#### Digital Input

The digital input of the module is displayed in output parameter "DIn" of the input driver.

#### Digital outputs

The digital outputs can be controlled by means of the "DOut_1" and "DOut_2" input parameters of the input driver.

#### Error handling

On detecting an error report of the module, the input driver sets the "Error" and "Err.EncoderErr" error codes and resets the "Sync" status bit in the axis DB.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

### EncoderFM350 (S7-300, S7-400)

#### Description

instruction EncoderFM350 is used to employ the FM 350‑1 as position decoder module for incremental encoders.

The driver can also be used for the isochronous variant of this module.

#### Configuration of the module (hardware configuration)

| Dialog | Setting |
| --- | --- |
| Interrupt selection | Enable diagnostic interrupts |
| Operating modes | - Count range: -31 to +31 bits - Operating mode: Continuous counting - Gate control: None |
| Inputs | If you want to perform a reference point approach, you must select the following setting:  - Set counter (DI set): once - The setting "Evaluate zero mark for setting" may be selected or cleared as a reference point criterion. |

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program (for example, module removed or station failure). |
| ReadDiagErr | IN-OUT | BOOL | Set this bit in OB 82 if the module has triggered a diagnostic interrupt (see Error handling). |
| DI_0 | OUTPUT | BOOL | Digital input 0 |
| DI_1 | OUTPUT | BOOL | Digital input 1 |
| DI_2 | OUTPUT | BOOL | Digital input 2 |
| The following static parameters of the instruction are only used for diagnostic purposes in the event of an error. |  |  |  |
| JobErr | STAT | INT | Return value of instruction RD_REC, if "ReadDiagErr" = TRUE was set. |
| DiagStatus.EXT_VOLTAGE | STAT | STRUCT | External auxiliary voltage faulty |
| DiagStatus.NO_CONFIG | STAT | STRUCT | Configuration missing |
| DiagStatus.CONFIG_ERR | STAT | STRUCT | Incorrect configuration |
| DiagStatus.WTCH_DOG_FLT | STAT | STRUCT | Watchdog timeout |
| DiagStatus.RAM_FLT | STAT | STRUCT | RAM failure |
| DiagStatus.CH1_SIGA | STAT | STRUCT | Signal A faulty |
| DiagStatus.CH1_SIGB | STAT | STRUCT | Signal B faulty |
| DiagStatus.CH1_SIGZ | STAT | STRUCT | Signal N faulty |
| DiagStatus.CH1_BETW | STAT | STRUCT | Error between channels |
| DiagStatus.CH1_5V2 | STAT | STRUCT | Error at the 5.2 V encoder supply |

#### Synchronization

Synchronization can be performed by:

- Reference point approach or
- Reference setting

Connect the reference point switch to digital input I2.

During a reference point approach, the module can detect the reference point in either of the following cases:

- Rising edge at digital input I2
- Rising edge of the zero mark, if digital input I2 is set

If the axis is already positioned on the reference point switch at the time the reference point approach is started, it is referenced to the current position, as is the case with reference point setting.

#### Digital inputs

The digital inputs I0 to I2 are displayed in the "DI_0" to "DI_2" output parameters of the input driver.

#### Error handling

The module returns its error information by means of dataset 1 (DS1). In the following situations, the input driver reads DS1 from the module by calling instruction RD_REC and saves it to the static "DiagStatus" parameter:

- The input driver is initialized.
- The module reports an error.
- The driver input parameter "ReadDiagErr" is TRUE.

It then sets "ReadDiagErr" = FALSE. The return value of instruction RD_REC is written to the static "JobErr" parameter (see [JOB_Err alarms](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#job_err-interrupts-s7-300-s7-400)).

If an error display is registered in dataset 1, the input driver sets the error codes "Error" and "Err.EncoderErr" to TRUE in the axis DB. Status bit "Sync" is set to FALSE.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

### EncoderCPU314C (S7-300, S7-400)

#### Description

The instruction EncoderCPU314C is used to integrate a counter channel of CPU 314C for position feedback from 24 V incremental encoders.

Up to 4 counter channels are available.

#### Configuration of the counter function of CPU 314C (hardware configuration)

This input driver is only supports CPU 314C with firmware V2.0 and higher.

For each counter channel you want to use, set the following parameters in the Properties dialog of the module in slot 2.7 (count):

| Parameter | Setting |
| --- | --- |
| Operating mode | Continuous counting |
| Hardware gate | No HW gate (check box cleared) |

Customize the other settings according to the encoder used and to the requirements for your application.

Enter the address you have assigned in the hardware configuration to the inputs at slot 2.7 (count) in the axis data of the "Start address of inputs of the position decoder module" parameter ("InputModuleInAddress"). Set the address of the counter outputs at the "Start address of outputs of the position decoder module" parameter ("InputModuleOutAddress") .

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  Here, you inform the input driver of an error detected by the user program. |

#### Synchronization

Synchronization can be performed by:

- Reference point approach or
- Reference setting

Connect the reference point switch to the latch digital input of the corresponding channel (DI1.4 for channel 0 to DI1.7 for channel 3).

During a reference point approach, CPU 314C is capable of detecting the reference point at a rising edge at digital input DI.

If the axis is already positioned on the reference point switch at the time the reference point approach is started, it is referenced to the current position, as is the case with reference point setting.

Among other things, the driver polls the status of the reference point switch during a reference point approach. The access actions that are necessary for reading the data considerably increase the instruction runtime.

#### Maximum count frequency

> **Note**
>
> The counter of CPU 314C does not output any values if its maximum counting frequency is exceeded (refer to the [SIMATIC S7‑300 CPU 31xC Technological Functions Manual](http://support.automation.siemens.com/WW/view/en/12429336)). The axis is halted and the error message "[Following error exceeded](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-with-hard-stop-s7-300-s7-400)" is output.

When specifying the maximum velocity ("MaxVelocity") in the axis data, you should therefore account for the limit frequency of the counter.

#### Error handling

The CPU 314C does not return encoder error information.

### EncoderIM174 (S7-300, S7-400)

#### Description

instruction EncoderIM174 is used to employ IM 174 as position decoder module for incremental and absolute encoders.

IM 174 provides up to 4 axes. You need a driver instruction EncoderIM174 for each axis.

#### Configuration of IM 174 (hardware configuration)

Insert an IM 174 at an isochronous PROFIBUS DP in your project. Ensure the I/O addresses are in the process image of the CPU. Adjust the addresses manually if necessary. Assign the I/O addresses to a process image partition. An isochronous OB must be assigned to the process image partition in the configuration of the S7 CPU.

| Parameter | Setting |
| --- | --- |
| I/O address | Specify the first input address for the axis to be used in Easy Motion Control in the axis DB. (Example for slot 4: input address 256 to 273; enter input address 256) |
| frame selection | You can select PROFIBUS frame 3 or frame 81 in the hardware configuration. Enter this information at input TelNumber of instruction EncoderIM174 as well. |
| 611U compliance mode | When using an external reference mark, activate the 611U compliance mode. |

> **Note**
>
> If frame 81 is used, IM 174 only transfers the encoder information to the CPU. Frame 81 is employed if you want to use IM 174 only to read encoder data.  
> In this case, it is not necessary to provide an output driver for IM 174 (OutputIM174).

> **Note**
>
> The hardware configuration implements IM 174 by default as an isochronous module. Isochronous processing is based on the condition that the I/O addresses of IM 174 are in the process image of the CPU.
>
> For more information on the isochronous mode in SIMATIC S7, refer to the [Isochronous Mode Function Manual](http://support.automation.siemens.com/WW/view/en/15218045).
>
> The EncoderIM174 driver instruction demands isochronous processing. If you ignore this rule, the instruction is prevented from accessing the hardware addresses.

#### Configuration of IM 174 in the axis DB

Specify the input address set for this axis in the hardware configuration in the "Module address inputs" field.

The EncoderIM174 input driver calculates the axis number for IM 174 at runtime. This address can be read from the local data of the corresponding DB.

Input driver EncoderIM174 determines the cycle time that was set in the isochronous PROFIBUS DP at runtime and enters it in the axis DB. You are therefore strongly advised to read back the modified axis DB from the controller in order to apply all changes that may have been made.

#### Call

The instruction is called in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| RefMode | INPUT | INT | Referencing type:  - 0 = Encoder zero mark - 1 = Positive edge at external zero mark (demands 611U compliant mode). - 4 = Positive edge at sensor 1 - 5 = Negative edge at sensor 1 - 6 = Positive edge at sensor 2 - 7 = Negative edge at sensor 2 |
| TelNumber | INPUT | INT | Number of the PROFIBUS frame used:  - 3 = PROFIBUS frame 3 - 81 = PROFIBUS frame 81 |
| Err_ID | OUTPUT | WORD | Error code of the instruction:  - W#16#0001 = Incorrect OB; instruction may only be installed in OB 6x - W#16#0002 = Incorrect frame number; IM 174 only supports PROFIBUS frames 3 and 81 - W#16#0004 = Incorrect axis number; IM 174 supports up to 4 axes. The hardware address you entered in the axis DB could not be assigned to an axis of IM 174. - W#16#0008 = Incorrect referencing mode setting. Check the parameter at input RefMode. |

#### Synchronization

Synchronization can be performed by:

- Reference point approach (with incremental encoder)
- Reference point setting (with incremental and absolute encoder)

You can use two types of reference point switches for reference point approach:

- If operating with an encoder with zero mark that you want to use for referencing, set the parameter at input "RefMode" = 0. The 611U compliance mode may not be selected in this scenario.
- Configure input "RefMode" = 1 if you want to use an external reference mark (BERO) for referencing. Connect the external reference point switch to digital input B1 to B4, depending on the axis used in your application. For this setup, it is mandatory to select the 611U compliance mode in the hardware configuration.

The digital inputs M1 or M2 must be used for both adjustable sensors.

For more information, refer to the [Distributed I/O PROFIBUS Module IM 174 manual](http://support.automation.siemens.com/WW/view/en/35014863).

If the axis is already positioned on the reference point switch at the time the reference point approach is started, it is referenced to the current position, as is the case with reference point setting.

#### Error handling

In response to a detected error, the input driver sets the "Error" and "Err.EncoderErr" error codes in the axis DB. The input driver resets the "Sync" status bit in the axis DB if you are using an incremental encoder.

For more information on error response, error display, and error acknowledgment, see [Error displays and error acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

#### Error acknowledgment

If you set error acknowledgment in the axis DB of Easy Motion Control, errors pending in the module are also acknowledged.

### EncoderSINAMICS (S7-300, S7-400)

#### Description

instruction EncoderSINAMICS is used to integrate a SINAMICS drive in Easy Motion Control. The drive may be integrated using PROFIBUS DP or PROFINET IO. You need an EncoderSINAMICS driver instruction for each SINAMICS axis.

#### Tools required

You need the following tools when using a SINAMICS in Easy Motion Control and to configure a SINAMICS:

- The drive configuration tool STARTER or S7 Technology, including the current SINAMICS Support Package (SSP)

#### Configuration of SINAMICS (hardware configuration)

Insert a SINAMICS into an isochronous PROFIBUS DP or PROFINET IO segment in your project. The EncoderSINAMICS driver instruction supports the standard frames 3, 5, 102, and 105 for PROFIBUS DP, as well as the standard frames 3 and 102 for PROFINET IO.

You need a suitable frame (5, 105) and an isochronous connection if you are going to use the Dynamic Servo Control (DSC) control method for your application. This DSC functionality is currently not supported for PROFINET IO.

For isochronous processing, make sure that the I/O addresses are in the process image of the CPU. Adjust the addresses manually if necessary. Assign the I/O addresses to a process image partition. An isochronous OB must be assigned to the process image partition in the configuration of the S7 CPU. For more information on the isochronous mode in SIMATIC S7, refer to the [Isochronous Mode Function Manual](http://support.automation.siemens.com/WW/view/en/15218045).

| Parameter | Setting |
| --- | --- |
| I/O address | Specify the first input address for the axis to be used in Easy Motion Control in the axis DB. (Example for slot 4: input address 256 to 273; enter input address 256) |
| frame selection | A frame number is selected for communication from the SINAMICS configuration wizard and transferred to the hardware configuration. Enter this information at input TelNumber of instruction EncoderSINAMICS as well. |

> **Note**
>
> The standard installation of TIA Portal does not support integration of the SINAMICS in a SIMATIC S7 CPU. Check the availability. Install the corresponding GSD file for SINAMICS. The necessary data is not integrated until you completed this additional installation.

#### Configuration of SINAMICS in the axis DB

Specify the input address set for this axis in the hardware configuration in the "Module address inputs" field.

Input driver EncoderSINAMICS determines the configured cycle time if a constant bus cycle time or an isochronous mode was detected and enters it in the axis DB. You are therefore strongly advised to read back the modified axis DB from the controller in order to apply all changes that may have been made.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |  |
| --- | --- | --- | --- | --- |
| RefMode | INPUT | INT | Referencing type: |  |
| 0 = Function 1 Reference mark 1 | Referencing to encoder zero mark or external zero mark (p495[0] in SINAMICS) |  |  |  |
| 1 = Function 2 Reference mark 2 | Second encoder zero mark |  |  |  |
| 2 = Function 3 Reference mark 3 | Third encoder zero mark |  |  |  |
| 3 = Function 4 Reference mark 4 | Fourth encoder zero mark |  |  |  |
| TelNumber | INPUT | INT | Frame number: |  |
| The following standard frames are supported:  3, 5, 102, and 105 | Only the frames 3 and 102 have been approved for PROFINET IO. |  |  |  |
| EncoderValid | OUTPUT | BOOL | 1= actual position values are valid | SINAMICS reports that the position encoder of the relevant axis returns valid values. This input may be used as activation condition at MC_Control. |
| Err_ID | OUTPUT | WORD | Error code of the instruction: |  |
| W#16#0001 = Incorrect OB | The instruction may only be called in OB 6x, OB 3x, or OB 1. |  |  |  |
| W#16#0002 = Incorrect frame number | The driver does not support the specified number. |  |  |  |
| W#16#0004 = Incorrect referencing mode setting | Check the parameter at input RefMode. Valid values are 0, 1, 2, or 3. |  |  |  |
|  |  |  |  |  |

> **Note**
>
> The frame number at the input driver must agree with the frame number configured for SINAMICS. Otherwise, correct operation cannot be guaranteed. No error code is output if you make incorrect entries.

#### Synchronization

Synchronization can be performed by:

- Reference point approach (with incremental encoder)
- Reference point setting (with incremental and absolute encoder)

The referencing type can be specified using input parameter "RefMode" at the input driver. The following table lists the options available for Easy Motion Control.

| RefMode | "Velocity" on MC_Home | Encoder zero mark | External zero mark p495[0] | Description |
| --- | --- | --- | --- | --- |
| 0 | > 0 | First encoder zero mark | 0 | Referencing to first encoder zero mark |
| 1 | > 0 | Second encoder zero mark | 0 | Referencing to second encoder zero mark |
| 2 | > 0 | Third encoder zero mark | 0 | Referencing to third encoder zero mark |
| 3 | > 0 | Fourth encoder zero mark | 0 | Referencing to fourth encoder zero mark |
|  |  |  |  |  |

The entry at RefMode controls the corresponding encoder control word for the drive so that the required functionality is realized in the SINAMICS. Input driver EncoderSINAMICS enables only the reference point approach to one or several encoder zero marks and to an external zero mark (alternative zero mark). Referencing on-the-fly is not possible. In order to reference to an external zero mark, set the p495[0] parameter of the axis concerned to a value between 1 and 6 value in the SINAMICS. To enable activation of a reference point approach, a traversing velocity greater than zero must be entered at instruction MC_HOME.

If traversing velocity zero has been entered, the contents of the "RefMode" input and the parameter p495[0] will be ignored.

#### Error handling

In response to a detected error, the input driver sets the "Error" and "Err.EncoderErr" error codes in the axis DB. The input driver resets the "Sync" status bit in the axis DB if you are using an incremental encoder.

For more information on error response, error display, and error acknowledgment, see [Error displays and error acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

#### Error acknowledgment

If you set error acknowledgment in the axis DB of Easy Motion Control, errors pending in the module are also acknowledged.

### EncoderUniversal (S7-300, S7-400)

#### Description

instruction EncoderUniversal is used to integrate position decoder modules for which Easy Motion Control does not provide any special input driver.

#### Operating principle

instruction EncoderUniversal expects a value at its "EncoderValue" input that corresponds to the actual position of your axis. It does not access the I/O itself. You can interconnect the value provided by your position decoder module directly with the driver, or convert it beforehand.

If your distance measurement module offers special functions you wish to use, you should integrate these into your user program.

#### Configuration of the module (hardware configuration)

Select parameters according to your hardware and the encoder used.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EncErr | INPUT | BOOL | 1 = Encoder error  With this parameter, you inform the input driver of an error detected by the position decoder module or user program (for example, module removed, or station failure). |
| EncoderValue | INPUT | DINT | Encoder value |

#### Synchronization

Synchronization with instruction EncoderUniversal is only possible by means of reference point setting.

#### Error handling

Any errors detected by your distance measurement module should be recorded and processed further in your user program.

If such an error impairs the functions you are performing with Easy Motion Control instructions, you should implement this error into Easy Motion Control error handling by means of "EncErr" input.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

## Output driver (S7-300, S7-400)

This section contains information on the following topics:

- [Task of the output driver (S7-300, S7-400)](#task-of-the-output-driver-s7-300-s7-400)
- [OutputIM178 (S7-300, S7-400)](#outputim178-s7-300-s7-400)
- [OutputSM432 (S7-300, S7-400)](#outputsm432-s7-300-s7-400)
- [OutputET200S2AO (S7-300, S7-400)](#outputet200s2ao-s7-300-s7-400)
- [OutputCPU314C (S7-300, S7-400)](#outputcpu314c-s7-300-s7-400)
- [OutputSM332 (S7-300, S7-400)](#outputsm332-s7-300-s7-400)
- [OutputUniversal (S7-300, S7-400)](#outputuniversal-s7-300-s7-400)
- [OutputMM4_DP (S7-300, S7-400)](#outputmm4_dp-s7-300-s7-400)
- [OutputIM174 (S7-300, S7-400)](#outputim174-s7-300-s7-400)
- [OutputSINAMICS (S7-300, S7-400)](#outputsinamics-s7-300-s7-400)

### Task of the output driver (S7-300, S7-400)

#### Function

The output driver is used to output the velocity setpoint of an axis which has been calculated by the controller to the connected output module. The instruction converts the velocity from [length unit/s] to the corresponding range of values of the output module and outputs this value.

If input "EnableDrive" = FALSE, the output driver outputs zero to the output module.

#### Initialization

The output value is set to zero.

#### Call

The output driver of an axis must be called unconditionally.

#### Isochronous Mode

The output drivers support the isochronous mode of all suitable I/O modules. The driver automatically recognizes isochronous mode by the fact that it is called in an isochronous OB.

#### Error handling

An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver at input "OutErr" . The output driver does not access the output module as long as input "OutErr" = TRUE.

If input"OutErr" = TRUE, the output driver sets the "Error" and "Err.OutputErr" error codes in the axis DB.

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

#### Simulation mode

As long as the "Sim" bit is in the axis DB, the output driver does not access the output module (see instruction [MC_Simulation](#mc_simulation-s7-300-s7-400)).

### OutputIM178 (S7-300, S7-400)

#### Description

instruction OutputIM178 is used to employ a channel of the IM 178‑4 as output module. instruction OutputIM178 is included for reasons of compatibility with STEP7 V5.x. Siemens is no longer actively marketing the IM 178‑4. You can use IM 174 as an alternative.

IM 178‑4 must be used with the same channel number and axis both at the input **and** output drivers, as specific address settings refer to both drivers. A combination with other drivers is not possible.

#### Call

The instruction is called in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  If "EnableDrive" = FALSE, a zero value is transferred to the output module.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| Q0 | INPUT | BOOL | Digital output 0 of selected channel |
| Q1 | INPUT | BOOL | Digital output 1 of selected channel |
| Q2 | INPUT | BOOL | Digital output 2 of selected channel |
| OutErr | INPUT | BOOL | 1 = Error at output module  An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver here. |

#### Digital outputs

The digital outputs "Q0" to "Q2"of the selected channel of IM 178‑4 can be controlled using the input parameters "Q0" to "Q2" of the output driver.

### OutputSM432 (S7-300, S7-400)

#### Description

instruction OutputSM432 is used to employ a channel of the SM 432 as output module.

#### Configuration of SM 432 (hardware configuration)

Set the output voltage of the corresponding SM 432 channel to ±10 V.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  If "EnableDrive" = FALSE, a zero value is transferred to the output module.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| OutErr | INPUT | BOOL | 1 = Error at output module  An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver here. |

### OutputET200S2AO (S7-300, S7-400)

#### Description

instruction OutputET200S2AO is used to employ a channel of the ET 200S analog output module 2AO U as output module.

The driver can also be used for the isochronous variant of this module.

#### Configuration of the ET 200S analog output module 2AO U (hardware configuration)

Set the output voltage of the corresponding channel of the module to ±10 V.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  If "EnableDrive" = FALSE, a zero value is transferred to the output module.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| OutErr | INPUT | BOOL | 1 = Error at output module  An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver here. |

### OutputCPU314C (S7-300, S7-400)

#### Description

instruction OutputCPU314C is used to employ an analog output channel of CPU 314C for ±10 V output voltage.

#### Configuration of the analog outputs of CPU 314C (hardware configuration)

Set the corresponding channel (analog output) of CPU 314C to an output voltage of ±10 V.

Set the address that you have assigned in the hardware configuration to the outputs at slot 2.6 (AI5/AO2) in the axis data parameter "Start address of the outputs of output module" ("OutputModuleOutAddress"). It is not necessary to configure the " Start address of the inputs of the output module" parameter for the output module ("OutputModuleInAddress").

Up to 2 analog output channels are available that allow you to operate the 2 axes entirely by means of CPU 314C.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  If "EnableDrive" = FALSE, the zero value is transferred to the analog output.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| OutErr | INPUT | BOOL | 1 = Analog output error  Errors detected by the user program can be reported to the output driver here. |

### OutputSM332 (S7-300, S7-400)

#### Description

instruction OutputSM332 is used to employ a channel of the SM 332 as output module.

The driver can also be used for the isochronous variant of this module.

#### Configuration of SM 332 (hardware configuration)

Set the output voltage of the corresponding SM 332 channel to ±10 V.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  If "EnableDrive" = FALSE, a zero value is transferred to the output module.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| OutErr | INPUT | BOOL | 1 = Error at output module  An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver here. |

### OutputUniversal (S7-300, S7-400)

#### Description

instruction OutputUniversal allows you to use any analog output module in combination with the instructions of Easy Motion Control.

#### Operating principle

instruction OutputUniversal calculates a speed setpoint based on the velocity value output by the controller and proportionality ratio "IntAtMaxVelocity" and provides the result at its outputs.

The driver itself does not access the I/O.

"You must use the value of "IntAtMaxVelocity" to control your analog output module so that it outputs a voltage that will move the axis at "MaxVelocity" (you have already declared the value of this voltage in the "DriveInputAtMaxVel" parameter).

The driver curve always passes through zero and follows a linear course.

The speed setpoint is output both as signed integer value and as an amount with a separate sign.

If these output values already correspond to your application, you can output them directly to the I/O via the user program. If the values are not yet suitable, you can also make an additional adjustment via the user program and output the value that is generated.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  A zero value is returned at the outputs as soon as "EnableDrive" = FALSE.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| IntAtMaxVelocity | INPUT | INT | Integer value for converting the speed setpoint (see below). |
| OutErr | INPUT | BOOL | 1 = Error at output module  An error detected on the output module by the user program (for example, module removed or station failure) can be signaled to the output driver here. |
| OutputValue | OUTPUT | INT | Calculated speed setpoint |
| OutValAbs | OUTPUT | INT | Absolute speed setpoint value |
| OutValSign | OUTPUT | BOOL | Sign of speed setpoint (TRUE = Negative value) |

### OutputMM4_DP (S7-300, S7-400)

#### Description

instruction OutputMM4_DP is used to implement of a MICROMASTER 4 with optional DP add-on module.

#### Configuration of MM4 (hardware configuration)

For information on MICROMASTER 4, refer to the hardware catalog at:

"Additional field devices > PROFIBUS DP > Drives > Siemens AG > SIMOVERT > MICROMASTER 4".

You may first have to install the corresponding GSD file.

Position the MICROMASTER in your DP master system and assign it a DP address. Insert a "0 PKW, 2 PZD (PPO3)" module into slots 0 and 1. Either accept the default I/O addresses or select your own values.

Transfer these addresses to "Start address of the outputs of the output module" or "Start address of the inputs of the output module" in the axis DB for your axis.

#### Configuring the MM4

Configure the MICROMASTER (motor data, DP address, operation as DP slave, etc.) using the MICROMASTER documentation according to your requirements.

Transfer the "reference frequency" specified in the P2000 parameter as "reference value for 100 % speed" ("DriveInputAt100") to the axis DB for your axis.

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  The zero speed value is output to the MICROMASTER as soon as "EnableDrive" = FALSE.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| OutErr | INPUT | BOOL | 1 = Output error  An error detected on the output module by the user program (for example, station failure) can be signaled to the output driver here. |
| ON | INPUT | BOOL | 1 = Drive switched on  "ON" in entered in bit 0 in the controller word. |
| DriveReady | OUTPUT | BOOL | 1 = Drive ready  If "DriveReady" = FALSE, starting the travel generates a "DriveError". |

### OutputIM174 (S7-300, S7-400)

#### Description

instruction OutputIM174 is used to employ a channel of the IM 174 as output module. IM 174 provides up to 4 axes. You need a driver instruction OutputIM174 for each axis for which PROFIBUS frame 3 is set.

#### Configuration of IM 174 (hardware configuration)

You only need output driver OutputIM174 if you configure an axis with PROFIBUS frame 3. You do not need an output driver for an axis with PROFIBUS frame 81.

Insert an IM 174 at an isochronous PROFIBUS DP in your project. Ensure the I/O addresses are in the process image of the CPU. Adjust the addresses manually if necessary. Assign the I/O addresses to a process image partition. An isochronous OB must be assigned to the process image partition in the configuration of the S7 CPU.

| Parameter | Setting |
| --- | --- |
| I/O address | Specify the first output address for the axis to be used in Easy Motion Control in the axis DB. (Example for slot 5: For start address 256 to 265, you must enter output address 256) |

> **Note**
>
> The hardware configuration implements IM 174 by default as an isochronous module. Isochronous processing is based on the condition that the I/O addresses of IM 174 are in the process image of the CPU.
>
> For more information on the isochronous mode in SIMATIC S7, refer to the [Isochronous Mode Function Manual](http://support.automation.siemens.com/WW/view/en/15218045).
>
> The OutputIM174 driver instruction demands isochronous processing. If you ignore this rule, the instruction is prevented from accessing the hardware addresses.

#### Configuration of IM 174 in the axis DB

Specify the output address set for this axis in the hardware configuration in the "Module address outputs" field.

#### Call

The instruction is called in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EnableDrive | INPUT | BOOL | 1 = Analog output enable  The zero speed value is output to the drive as soon as "EnableDrive" = FALSE. The drive enable is locked.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| OutErr | INPUT | BOOL | 1 = Error at output module  An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver here. |
| Err_ID | OUTPUT | WORD | Error code of the instruction  W#16#0001 = Incorrect OB; instruction may only be installed in OB 6x |

### OutputSINAMICS (S7-300, S7-400)

#### Description

instruction OutputSINAMICS is used to integrate a SINAMICS drive in Easy Motion Control. The drive may be integrated using PROFIBUS DP or PROFINET IO. You need an OutputSINAMICS driver instruction for each SINAMICS axis.

#### Configuration of SINAMICS (hardware configuration)

Insert a SINAMICS into an isochronous PROFIBUS DP or PROFINET IO segment in your project. The OutputSINAMICS driver instruction supports the standard frames 3, 5, 102, and 105 for PROFIBUS DP, as well as the standard frames 3 and 102 for PROFINET IO.

You need a suitable frame (5, 105) and an isochronous connection if you are going to use the Dynamic Servo Control (DSC) control method for your application. This DSC functionality is currently not supported for PROFINET IO.

For isochronous processing, make sure that the I/O addresses are in the process image of the CPU. Adjust the addresses manually if necessary. Assign the I/O addresses to a process image partition. An isochronous OB must be assigned to the process image partition in the configuration of the S7 CPU. For more information on the isochronous mode in SIMATIC S7, refer to the [Isochronous Mode Function Manual](http://support.automation.siemens.com/WW/view/en/15218045).

| Parameter | Setting |
| --- | --- |
| I/O address | Specify the first output address for the axis to be used in Easy Motion Control in the axis DB. (Example for slot 5: For start address 256 to 265, you must enter output address 256) |
|  |  |

> **Note**
>
> The standard installation of TIA Portal does not support integration of the SINAMICS in a SIMATIC S7 CPU. Check the availability. Install the corresponding GSD file for SINAMICS. The necessary data is not integrated until you completed this additional installation.

#### Configuration of SINAMICS in the axis DB

Specify the output address set for this axis in the hardware configuration in the "Module address outputs" field. Specify the frame number once again to enable stand-alone operation of the output driver. The program checks if the frame number agrees with that of the corresponding EncoderSINAMICS input driver (if that exists).

#### Activating the axis

Each SINAMICS motor module inevitably assigned a central power supply (line module) for the DC link. Always ensure that the central power supply is switched on before you activate the axis by setting input "EnableDrive" of instruction MC_Control. The line module returns corresponding information on its operating status. Evaluate the necessary feedback signals from the line module and link these as power-on conditions.

For more information, refer to the [SINAMICS Drives documentation](http://www.automation.siemens.com/doconweb).

An example of the application for switching on an active line module is available on the [Internet](http://support.automation.siemens.com/WW/view/en/21971603).

#### Switching off the axis - Configuration of the StopMode

**Coasting (coast stop) (**
**AUS2**
**) – StopMode = 3:**

In this case, the power enable signal is immediately cleared and the drive coasts to a standstill in the power-off state. The mechanical brake control is enabled immediately and simultaneously. This engages the brake for active deceleration of the drive. Mechanical stress on the brake increases in the process depending on its inertia load.

![Switching off the axis - Configuration of the StopMode](images/30418635019_DV_resource.Stream@PNG-en-US.png)

**Ramp-down stop (**
**AUS1**
**) – StopMode = 5:**

In this mode, the drive is decelerated with its ramp-up function. Once the speed threshold has been reached, the holding brake is engaged and pulse enable is deactivated on expiration of the brake closing time.

![Switching off the axis - Configuration of the StopMode](images/30418623371_DV_resource.Stream@PNG-en-US.png)

**Fast stop (**
**AUS3**
**) – StopMode = 6:**

In this mode, the drive is decelerated and brought to a stop with the fast stop ramp (emergency stop). Once the speed threshold has been reached, the holding brake is engaged and pulse enable is deactivated on expiration of the brake closing time.

![Switching off the axis - Configuration of the StopMode](images/30418697867_DV_resource.Stream@PNG-en-US.png)

For more information, refer to the [SINAMICS S120 product information](http://support.automation.siemens.com/WW/view/en/30119684).

#### Call

The instruction is called in a cyclic interrupt OB (for example, OB 35), or in a synchronous cycle interrupt OB (for example, OB 61). You must call all EMC instructions of an axis in the same program block.

#### Parameter

| Parameter | Declaration | Data type | Description |  |
| --- | --- | --- | --- | --- |
| TelNumber | INPUT | INT | Frame number: |  |
| The following standard frames are supported:  3, 5, 102,105 | Only the frames 3 and 102 have been approved for PROFINET IO.  If you are using EncoderSINAMICS as input driver, the number of the frame used must always remain the same. |  |  |  |
| EnableDrive | INPUT | BOOL | 1 = Drive enable | The zero speed value is output to the drive as soon as "EnableDrive" = FALSE. The drive enable is locked.  This input can be interconnected with the "DriveEnabled" output of instruction MC_Control. |
| StopMode | INPUT | INT | Stop mode: |  |
| 3 = Coast to stop (AUS2) | The drive coasts to a stop in power-off state |  |  |  |
| 5 = Ramp stop (AUS1) | Stops the axis by using a ramp function generator |  |  |  |
| 6 = Quick stop (AUS3) | Stops the axis along a quick stop ramp |  |  |  |
| OutErr | INPUT | BOOL | 1 = Error at output module | An error detected by the user program (for example, module removed or station failure) can be signaled to the output driver here. |
| Operation_Enabled | OUTPUT | BOOL | 1 = SINAMICS reports "Operation enabled" | All axis enable signals are set in the drive and the axis reports that it is ready for movement. The starting current is applied to the axis. |
| Err_ID | OUTPUT | WORD | Error code of the instruction: |  |
| W#16#0001 = Incorrect OB | The instruction may only be installed in OB 6x, OB 3x, or OB 1. |  |  |  |
| W#16#0002 = Incorrect frame number | The specified number is not supported by the driver, or differs from the frame number that has been configured in the SINAMICS. |  |  |  |
|  |  |  |  |  |

OutErr: The drive (SINAMICS) is deactivated on the positive edge of this variable. To reactivate the drive, OutErr = FALSE must be set and the error message must be acknowledged.

Operation_Enabled: This variable reports the current axis status in the SINAMICS. You should not activate a travel instruction while Operation_Enabled = FALSE.

For more information on integration of the SINAMICS, refer to the [Internet](http://support.automation.siemens.com/WW/view/en/30119684).

## Additional references for Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Axis data block (axis DB) (S7-300, S7-400)](#axis-data-block-axis-db-s7-300-s7-400)

### Axis data block (axis DB) (S7-300, S7-400)

#### Function

The axis DB is the central database of Easy Motion Control. It contains:

- Parameters that provide basic information about the axis (for example, I/O addresses)
- Position control parameters that are calculated from these basic parameters during initialization of the EMC instructions
- Actual values of the position control (for example, position, error states, etc.)
- Initialization bits for coordinating the start of the instructions

#### Contents

The following table shows the content of the axis DB.

> **Note**
>
> You may not change any data not listed in this table.

| Address | Parameter | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 0.0 | Sample_T | REAL | 0.01 | Scan time of the axis instructions [s] |
| 4.0 | AxisType | BOOL | FALSE | Axis type  - FALSE = Linear axis - TRUE = Rotary axis |
| 4.1 | EncoderType | BOOL | FALSE | Encoder type  - FALSE = Incremental encoder - TRUE = Absolute encoder |
| 4.2 | Sim | BOOL | FALSE | TRUE = Simulation mode is active |
| 6.0 | AxisLimitMax | REAL | 1.0e<sup>+6</sup> | Software limit switch end [length unit] |
| 10.0 | AxisLimitMin | REAL | -1.0e<sup>+6</sup> | Software limit switch start [length unit] |
| 14.0 | MaxVelocity | REAL | 0.1 | Maximum axis velocity [unit of length/s] |
| 18.0 | MaxAcceleration | REAL | 0.1 | Max. axis acceleration in [unit of length/s<sup>2</sup>] |
| 22.0 | MaxDeceleration | REAL | 0.1 | Max. axis deceleration in [unit of length/s<sup>2</sup>] |
| 26.0 | MonTimeTargetAppr | REAL | 1.0 | Monitoring time for target approach [s] |
| 30.0 | TargetRange | REAL | 1.0 | Target range on positioning [unit of length] |
| 34.0 | StandstillRange | REAL | 1.5 | Standstill range without travel order [unit of length] |
| 38.0 | MaxFollowingDist | REAL | 5.0 | Maximum admissible. following error [unit of length] |
| 42.0 | MonitorTargetAppr | BOOL | TRUE | TRUE = Enable monitoring of target range |
| 42.1 | SWLimitEnable | BOOL | TRUE | TRUE = Enable software limit switch monitoring |
| 44.0 | FactorP | REAL | 1.0 | Proportionality factor [1/s] |
| 48.0 | ManVelocity | REAL | 0.0 | Setpoint velocity in manual mode [unit of length/s] |
| 52.0 | ManEnable | BOOL | FALSE | TRUE = Enable manual mode |
| 54.0 | EmergencyDec | REAL | 1000.0 | Axis deceleration for emergency stop [length unit/s<sup>2</sup>] |
| 58.0 | InputModuleInAddr | INT | 0 | Start address for the position detection module inputs |
| 60.0 | InputModuleOutAddr | INT | 0 | Start address for the position detection module outputs |
| 62.0 | InputChannelNo | INT | 0 | Channel number of position input module |
| 64.0 | StepsPerRev | DINT | L#1 | Steps per encoder revolution  [steps/encoder revolution] |
| 68.0 | DisplacementPerRev | REAL | 1.0 | Distance per encoder revolution  [unit of length/encoder revolution] |
| 72.0 | NumberRevs | INT | 1 | Number of revolutions of an absolute encoder |
| 74.0 | PolarityEncoder | INT | 1 | Set encoder polarity |
| 76.0 | PositionOffset | DINT | L#0 | Position offset / absolute encoder adjustment [step] |
| 80.0 | OutputModuleOutAddr | INT | 0 | Start address for the output module outputs |
| 82.0 | OutputModuleInAddr | INT | 0 | Start address of the output module inputs |
| 84.0 | OutputChannelNo | INT | 0 | Channel number of the output module |
| 86.0 | PolarityDrive | INT | 1 | Set drive polarity |
| 88.0 | DriveInputAtMaxVel | REAL | 9.0 | Reference value for max. axis velocity [V] |
| 92.0 | OffsetCompensation | REAL | 0.0 | Offset compensation [V] |
| 96.0 | DriveInputAt100 | REAL | 10.0 | Reference value for 100% speed [V] |
| 100.0 | Override | REAL | 100.0 | Velocity override [%] |
| 104.0 | ActPosition | REAL | 0.0 | Current actual position [unit of length] |
| 108.0 | FollowingDistance | REAL | 0.0 | Current following error [unit of length] |
| 112.0 | RemainingDistance | REAL | 0.0 | Current residual distance to target [unit of length] |
| 116.0 | NomVelocity | REAL | 0.0 | Setpoint velocity of axis [unit of length/s] |
| 120.0 | ActVelocity | REAL | 0.0 | Actual speed of axis [unit of length/s] |
| 124.0 | Sync | BOOL | FALSE | - FALSE = Axis not synchronized - TRUE = Axis synchronized |
| 124.1 | Error | BOOL | TRUE | - FALSE = No error - TRUE = Group error |
| 124.2 | ErrorAck | BOOL | FALSE | - FALSE = No acknowledgment - TRUE = Acknowledge error |
| 128.0 | Err.SWLimitMinExceeded | BOOL | FALSE | TRUE = Software limit switch start exceeded |
| 128.1 | Err.SWLimitMaxExceeded | BOOL | FALSE | TRUE = Software limit switch end exceeded |
| 128.2 | Err.TargetErr | BOOL | FALSE | TRUE = Target outside travel range |
| 128.3 | Err.NoSync | BOOL | FALSE | TRUE = Axis not synchronized |
| 128.4 | Err.DirectionErr | BOOL | FALSE | TRUE = Travel in specified direction inadmissible |
| 128.5 | Err.DataErr | BOOL | FALSE | TRUE = Invalid parameter in travel instruction |
| 128.6 | Err.StartErr | BOOL | FALSE | TRUE = Start not possible in current axis status |
| 128.7 | Err.DistanceErr | BOOL | FALSE | TRUE = Overtravel |
| 129.0 | Err.MasterErr | BOOL | FALSE | TRUE = Master axis in error state |
| 130.0 | Err.StoppedMotion | BOOL | TRUE | TRUE = Axis in stop status requiring acknowledgment |
| 130.1 | Err.EnableDriveErr | BOOL | FALSE | TRUE = Drive enable missing |
| 130.2 | Err.FollowingDistErr | BOOL | FALSE | TRUE = Max. following error exceeded |
| 130.3 | Err.StandstillErr | BOOL | FALSE | TRUE = Standstill range exceeded |
| 130.4 | Err.TargetApproachErr | BOOL | FALSE | TRUE = Error on target approach |
| 130.5 | Err.EncoderErr | BOOL | FALSE | TRUE = Encoder error |
| 130.6 | Err.OutputErr | BOOL | FALSE | TRUE = Error at output driver |
| 130.7 | Err.ConfigErr | BOOL | FALSE | TRUE = Axis data incorrectly configured |
| 131.0 | Err.DriveErr | BOOL | FALSE | TRUE = Drive error |
| 132.0 | Config.Err_AxisLimit | BOOL | FALSE | TRUE = Axis limits incorrect |
| 132.1 | Config.Err_MaxVelocity | BOOL | FALSE | TRUE = Max. velocity incorrect |
| 132.2 | Config.Err_MaxAcceleration | BOOL | FALSE | TRUE = Max. acceleration incorrect |
| 132.3 | Config.Err_MaxDeceleration | BOOL | FALSE | TRUE = Max. deceleration incorrect |
| 132.4 | Config.Err_MonTimeTargetAppr | BOOL | FALSE | TRUE = Monitoring time for target approach incorrect |
| 132.5 | Config.Err_TargetRange | BOOL | FALSE | TRUE = Target range incorrect |
| 132.6 | Config.Err_StandstillRange | BOOL | FALSE | TRUE = Standstill range incorrect |
| 132.7 | Config.Err_MaxFollowingDist | BOOL | FALSE | TRUE = Max. following error incorrect |
| 133.0 | Config.Err_EmergencyDec | BOOL | FALSE | TRUE = Deceleration for hard stop incorrect |
| 133.1 | Config.Err_StepsPerRev | BOOL | FALSE | TRUE = Steps per encoder revolution incorrect |
| 133.2 | Config.Err_DisplacementPerRev | BOOL | FALSE | TRUE = Axis distance per encoder revolution incorrect |
| 133.3 | Config.Err_NumberRevs | BOOL | FALSE | TRUE = Incorrect number of encoder revolutions |
| 133.4 | Config.Err_PolarityEncoder | BOOL | FALSE | TRUE = Set encoder polarity incorrect |
| 133.5 | Config.Err_PolarityDrive | BOOL | FALSE | TRUE = Set drive polarity incorrect |
| 133.6 | Config.Err_DriveInputAtMaxVel | BOOL | FALSE | TRUE =reference value for maximum velocity incorrect |
| 133.7 | Config.Err_AxisLength | BOOL | FALSE | TRUE = Length of axis incorrect |
| 134.0 | Config.Err_EncoderRange | BOOL | FALSE | TRUE = Encoder range is not suitable for axis length |
| 134.1 | Config.Err_MaxVelRotaryAxis | BOOL | FALSE | TRUE = Max. velocity and scan time do not match rotary axis module |
| 134.2 | Config.Err_DriveInputAt100 | BOOL | FALSE | TRUE = Reference value for 100 % speed ≤ 0 |
| 136.0 | EncoderValue | DINT | L#0 | Current encoder value |
| 278.0 | Init | STRUCT | TRUE | Bit array for initializing 32 instructions |
