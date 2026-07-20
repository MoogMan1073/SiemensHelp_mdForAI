---
title: "S7-1200 Motion Control (S7-1200)"
package: ProgFBBMCenUS
topics: 90
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# S7-1200 Motion Control (S7-1200)

This section contains information on the following topics:

- [S7-1200 Motion Control as of V6 (S7-1200)](#s7-1200-motion-control-as-of-v6-s7-1200)
- [S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
- [S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

## S7-1200 Motion Control as of V6 (S7-1200)

This section contains information on the following topics:

- [MC_Power (S7-1200)](#mc_power-s7-1200)
- [MC_Reset (S7-1200)](#mc_reset-s7-1200)
- [MC_Home (S7-1200)](#mc_home-s7-1200)
- [MC_Halt (S7-1200)](#mc_halt-s7-1200)
- [MC_MoveAbsolute (S7-1200)](#mc_moveabsolute-s7-1200)
- [MC_MoveRelative (S7-1200)](#mc_moverelative-s7-1200)
- [MC_MoveVelocity (S7-1200)](#mc_movevelocity-s7-1200)
- [MC_MoveJog (S7-1200)](#mc_movejog-s7-1200)
- [MC_CommandTable (S7-1200)](#mc_commandtable-s7-1200)
- [MC_ChangeDynamic (S7-1200)](#mc_changedynamic-s7-1200)
- [MC_ReadParam (S7-1200)](#mc_readparam-s7-1200)
- [MC_WriteParam (S7-1200)](#mc_writeparam-s7-1200)

### MC_Power (S7-1200)

This section contains information on the following topics:

- [MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
- [MC_Power: Function chart as of V6 (S7-1200)](#mc_power-function-chart-as-of-v6-s7-1200)

#### MC_Power: Enable, disable axis as of V6 (S7-1200)

##### Description

The Motion Control instruction "MC_Power" enables or disables an axis.

##### Requirements

- The technology object has been configured correctly.
- There is no pending enable-inhibiting error.

For PROFIdrive drive or analog drive connection:

- Cyclic BUS communication is established between controller and encoder ("<Axis name> .StatusSensor[1].CommunicationOK" = TRUE).
- Cyclic BUS communication is established between controller and drive ("<Axis name> .StatusDrive.CommunicationOK" = TRUE).

##### Override response

Execution of "MC_Power" cannot be aborted by a Motion Control command.

Disabling the axis (input parameter "Enable" = FALSE) aborts all Motion Control commands for the associated technology object in accordance with the selected "StopMode".

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis | - | Axis technology object |  |
| Enable | INPUT | BOOL | FALSE | TRUE | The axis is enabled. |
| FALSE | All current jobs are interrupted in accordance with the "StopMode" configured. The axis is stopped and disabled. |  |  |  |  |
| StartMode | INPUT | INT | 1 | 0 | Enable positioning axis not position-controlled *) |
| 1 | Enable positioning axis position-controlled *) |  |  |  |  |
| *) This parameter is ignored when a positioning axis with PTO (Pulse Train Output) drive is used.  The parameter initially takes effect when the positioning axis is enabled (Enable changes from FALSE to TRUE) and when the axis is enabled after successful acknowledgment of an interrupt that caused the axis to be disabled. |  |  |  |  |  |
| StopMode | INPUT | INT | 0 | 0 | Emergency stop  If a request to disable the axis is pending, the axis brakes at the configured emergency deceleration. The axis is disabled after reaching standstill. |
| 1 | Immediate stop  If a request to disable the axis is pending, this setpoint zero is output and the axis is disabled. The axis is braked depending on the configuration in the drive, and is brought to a standstill.  With drive connection via PTO (Pulse Train Output): When you disable the axis, the pulse output is stopped with a frequency-dependent deceleration:  - Output frequency ≥ 100 Hz   Deceleration: max. 30 ms - Output frequency < 100 Hz   Deceleration: 30 ms up to max. 1.5 s at 2 Hz |  |  |  |  |
| 2 | Emergency stop with jerk control  If a request to disable the axis is pending, the axis brakes at the configured emergency deceleration. If the jerk control is activated, the configured jerk is taken into account. The axis is disabled after reaching standstill. |  |  |  |  |
| Status | OUTPUT | BOOL | FALSE | Status of axis enable |  |
| FALSE | The axis is disabled.  The axis does not execute Motion Control commands and does not accept any new commands (exception: MC_Reset command)  For drive connection via PTO (Pulse Train Output):  The axis is not homed.  Upon disabling, the status does not change to FALSE until the axis reaches a standstill. |  |  |  |  |
| TRUE | The axis is enabled.  The axis is ready to execute Motion Control commands.  Upon axis enabling, the status does not change to TRUE until the signal "Drive ready" is pending. If the "Drive ready" drive interface was not configured in the axis configuration, the status changes to TRUE immediately. |  |  |  |  |
| Busy | OUTPUT | BOOL | FALSE | TRUE | MC_Power" is active. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred in Motion Control instruction "MC_Power" or in the associated technology object. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

> **Note**
>
> If the axis is switched off due to an error, it will be enabled again automatically after the error has been eliminated and acknowledged. This requires that the input parameter "Enable" has retained the value TRUE during this process.

##### Enabling an axis with configured drive interface

To enable the axis, follow these steps:

1. Check the requirements indicated above.
2. Initialize input parameters "StartMode" and "StopMode" with the desired value. Set the input parameter "Enable" to TRUE.

   The enable output for "Drive enabled" changes to TRUE to enable the power to the drive. The CPU waits for the "Drive ready" signal of the drive.

   When the "Drive ready" signal is available at the configured ready input of the CPU, the axis is enabled. The output parameter "Status" and the variable of the technology object <axis name>.StatusBits.Enable indicate the value TRUE.

##### Enabling an axis without configured drive interface

To enable the axis, follow these steps:

1. Check the requirements indicated above.
2. Initialize input parameters "StartMode" and "StopMode" with the desired value. Set the input parameter "Enable" to TRUE. The axis is enabled. The output parameter "Status" and the variable of the technology object <axis name>.StatusBits.Enable indicate the value TRUE.

##### Disabling an axis

To disable an axis, you can follow the steps described below:

1. Bring the axis to a standstill.

   You can identify when the axis is at a standstill in the variable of the technology object <axis name>.StatusBits.StandStill.
2. Set input parameter "Enable" to FALSE after standstill is reached.
3. If output parameters "Busy" and "Status" and variable of technology object <axis name>.StatusBits.Enable indicate the value FALSE, disabling of the axis is complete.

---

**See also**

[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)

#### MC_Power: Function chart as of V6 (S7-1200)

##### Function chart

![Function chart](images/103743321355_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Section    ![Function chart](images/103755015307_DV_resource.Stream@PNG-de-DE.png) | An axis is enabled and then disabled again. When the drive has signaled "Drive ready" back to the CPU, the successful enable can be read out via "Status_1". |
| Section    ![Function chart](images/103755736203_DV_resource.Stream@PNG-de-DE.png) | Following an axis enable, an error has occurred that caused the axis to be disabled. The error is eliminated and acknowledged with "MC_Reset". The axis is then enabled again. |
| ① | The exact end of the signals depends on the selected drive and the StopMode. |

### MC_Reset (S7-1200)

This section contains information on the following topics:

- [MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)

#### MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)

##### Description

Motion Control instruction "MC_Reset" can be used to acknowledge "Operating error with axis stop" and "Configuration error". The errors that require acknowledgment can be found in the "List of ErrorIDs and ErrorInfos" under "Remedy".

The axis configuration can be downloaded to the work memory after a download in RUN mode.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The cause of a pending configuration error requiring acknowledgment has been eliminated (for example, acceleration in positioning axis technology object has been changed to a valid value).

##### Override response

The MC_Reset command cannot be aborted by any other Motion Control command.

The new MC_Reset command does not abort any other active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Restart | INPUT | BOOL | FALSE | TRUE | Download the axis configuration from the load memory to the work memory. The command can only be executed when the axis is disabled.  Refer to the notes on Download to the CPU. |
| FALSE | Acknowledges pending errors |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Error has been acknowledged. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

##### Acknowledging an error requiring acknowledgment with MC_Reset

To acknowledge an error, follow these steps:

1. Check the requirements indicated above.
2. Start the acknowledgment of the error with a rising edge at input parameter "Execute". With MC_Reset as of V7.0 or higher you can acknowledge switch-on prevention errors on the configured encoder or drive before the axis is enabled.
3. If output parameter "Done" indicates the value TRUE and tag of technology object <Axis name>.StatusBits.Error the value FALSE, the error has been acknowledged.

> **Note**
>
> **Acknowledge with "Restart" = FALSE**
>
> To acknowledge only the errors, set "Restart" = FALSE. The technology object cannot be used during a restart. All errors at axes and encoders are acknowledged even if they are not enabled or active.

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

### MC_Home (S7-1200)

This section contains information on the following topics:

- [MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)

#### MC_Home: Home axes, set reference point as of V6 (S7-1200)

##### Description

Motion Control instruction "MC_Home" is used to match the axis coordinates to the real, physical drive position. Homing is required for absolute positioning of the axis. The following types of homing can be executed:

- Active homing (Mode = 3)

  The homing procedure is executed automatically.
- Passive homing (Mode = 2)

  During passive homing, the "MC_Home" Motion Control instruction does not carry out any homing motion. The traversing motion required for this must be implemented by the user via other Motion Control instructions. When the homing switch is detected, the axis is homed.
- Direct homing absolute (Mode = 0)

  The current axis position is set to the value of parameter "Position".
- Direct homing relative (Mode = 1)

  The current axis position is offset by the value of parameter "Position".
- Absolute encoder adjustment relative (Mode = 6)

  The current axis position is offset by the value of parameter "Position".
- Absolute encoder adjustment absolute (Mode = 7)

  The current axis position is set to the value of parameter "Position".

Mode 6 and 7 can only be used with drives with an analog interface and PROFIdrive drive.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled. (Not valid for PROFIdrive drive/analog drive connection Mode = 0 or 1)
- No MC_CommandTable command may be active upon start with Mode = 0, 1, or 2.

##### Override response

The override response depends on the selected mode:

**Mode**
**= 0, 1, 6, 7**

The MC_Home command cannot be aborted by any other Motion Control command.

The MC_Home command does not abort any active Motion Control commands. Position-related motion commands are resumed after homing according to the new homing position (value at input parameter: "Position").

**Mode**
**= 2**

The MC_Home command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 2, 3

The new MC_Home command aborts the following active Motion Control command:

- MC_Home command Mode = 2

Position-related motion commands are resumed after homing according to the new homing position (value at input parameter: "Position").

**Mode**
**= 3**

The MC_Home command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_Home command aborts the following active Motion Control commands:

- MC_Home command Mode = 2, 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Position | INPUT | REAL | 0.0 | - Mode = 0, 2, and 3   Absolute position of axis after completion of the homing operation - Mode = 1   Correction value for the current axis position  Limit values:  -1.0E12 ≤ Position ≤ 1.0E12 |  |
| Mode | INPUT | INT | 0 | Homing mode |  |
| 0 | Direct homing (absolute)  New axis position is the position value of parameter "Position". |  |  |  |  |
| 1 | Direct homing (relative)  New axis position is the current axis position + position value of parameter "Position". |  |  |  |  |
| 2 | Passive homing  Homing according to the axis configuration. Following homing, the value of parameter "Position" is set as the new axis position.  With an already referenced axis <axis name>.StatusBits.HomingDone = TRUE this status bit remains set during an additional passive homing. |  |  |  |  |
| 3 | Active homing  Homing procedure in accordance with the axis configuration. Following homing, the value of parameter "Position" is set as the new axis position. |  |  |  |  |
| 6 | Absolute encoder adjustment (relative)  The current axis position is offset by the value of parameter "Position". The calculated absolute value offset is stored retentively in the CPU. (<AxisName>.StatusSensor.AbsEncoderOffset) |  |  |  |  |
| 7 | Absolute encoder adjustment (absolute)  The current axis position is set to the value of parameter "Position". The calculated absolute value offset is stored retentively in the CPU. (<AxisName>.StatusSensor.AbsEncoderOffset) |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Command completed |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |
| ReferenceMarkPosition | OUTPUT | REAL | 0.0 | Display of the position at which the technology object was homed (valid when "Done" = TRUE) |  |

##### Resetting the "Homed" status

The "Homed" status of a technology object (<Axis name>.StatusBits.HomingDone) is reset under the following conditions:

- **Drive connection via** 
  **PTO (Pulse Train Output)**
  **:**

  - Start an "MC_Home" command for active homing

    (After successful completion of the homing operation, the "Homed" status is set again.)
  - Disabling of axis by the "MC_Power" Motion Control instruction
  - Changeover between automatic mode and manual control
  - After POWER OFF → POWER ON of the CPU
  - After restart of CPU (RUN-STOP → STOP-RUN)
- **Technology objects with incremental actual values:**

  - Start an "MC_Home" command for active homing

    (After successful completion of the homing operation, the "Homed" status is set again.)
  - Error in the encoder system, or encoder failure
  - Restart of the technology object
  - After POWER OFF → POWER ON of the CPU
  - Memory reset
  - Modification of the encoder configuration
- **Technology objects with absolute actual values:**

  - Errors in the sensor system/encoder failure
  - Replacement of the CPU
  - Modification of the encoder configuration
  - Restoration of the CPU factory settings
  - Transfer of a different project to the controller

##### Homing an axis

To home the axis, follow these stops:

1. Check the requirements indicated above.
2. Provide the necessary input parameters with values and start the homing operation with a rising edge at input parameter "Execute".
3. If output parameter "Done" and technology object variable <axis name>.StatusBits.HomingDone indicate the value TRUE, homing is complete. The reference position can be taken from the <axis name>.ReferenceMarkPosition variable.

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

### MC_Halt (S7-1200)

This section contains information on the following topics:

- [MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
- [MC_Halt: Function chart as of V6 (S7-1200)](#mc_halt-function-chart-as-of-v6-s7-1200)

#### MC_Halt: Stop axis as of V6 (S7-1200)

##### Description

The "MC_Halt" Motion Control instruction stops all movements and brings the axis to a standstill with the configured deceleration. The standstill position is not defined.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_Halt command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_Halt command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Zero velocity reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

#### MC_Halt: Function chart as of V6 (S7-1200)

##### Function chart

![Function chart](images/103748990731_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 5.0

| Symbol | Meaning |
| --- | --- |
| Section    ![Function chart](images/103755015307_DV_resource.Stream@PNG-de-DE.png) | The axis is braked by an MC_Halt command until it comes to a standstill. The axis standstill is signaled via "Done_2". |
| Section    ![Function chart](images/103755736203_DV_resource.Stream@PNG-de-DE.png) | While an MC_Halt command is braking the axis, this command is aborted by another motion command. The abort is signaled via "Abort_2". |

### MC_MoveAbsolute (S7-1200)

This section contains information on the following topics:

- [MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
- [MC_MoveAbsolute: Function chart as of V6 (S7-1200)](#mc_moveabsolute-function-chart-as-of-v6-s7-1200)

#### MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)

##### Description

The "MC_MoveAbsolute" Motion Control instruction starts an axis positioning motion to move it to an absolute position.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.
- The axis is homed.

##### Override response

The MC_MoveAbsolute command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveAbsolute command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_PositioningAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Position | INPUT | REAL | 0.0 | Absolute target position  Limit values:   -1.0E12 ≤ Position ≤ 1.0E12 |  |
| Velocity | INPUT | REAL | 10.0 | Velocity of axis  This velocity is not always reached on account of the configured acceleration and deceleration and the target position to be approached.  Limit values:  Start/stop velocity ≤ Velocity ≤ maximum velocity |  |
| Direction | INPUT | INT | 1 | Motion direction of the axis  Is only evaluated with "modulo" enabled. "Technology object > Configuration > Extended parameters > Modulo > Enable Modulo"  Parameter is ignored with PTO axes. |  |
| 0 | The sign for the velocity ("Velocity" parameter) determines the motion direction. |  |  |  |  |
| 1 | Positive direction  (Target position is approached in a positive direction) |  |  |  |  |
| 2 | Negative direction  (Target position is approached in a negative direction) |  |  |  |  |
| 3 | Shortest distance (Starting from the current position, the technology selects the shortest distance to the target position) |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Absolute target position reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

#### MC_MoveAbsolute: Function chart as of V6 (S7-1200)

##### Function chart

![Function chart](images/104080647691_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| Section    ![Function chart](images/103755015307_DV_resource.Stream@PNG-de-DE.png) | An axis is moved to absolute position 1000.0 with an MC_MoveAbsolute command. When the axis reaches the target position, this is signaled via "Done_1". When "Done_1" = TRUE, another MC_MoveAbsolute command, with target position 1500.0, is started. Because of the response times (e.g., cycle time of user program, etc.), the axis comes to a standstill briefly (see zoomed-in detail). When the axis reaches the new target position, this is signaled via "Done_2". |
| Section    ![Function chart](images/103755736203_DV_resource.Stream@PNG-de-DE.png) | An active MC_MoveAbsolute command is aborted by another MC_MoveAbsolute command. The abort is signaled via "Abort_1". The axis is then moved at the new velocity to the new target position 1500.0. When the new target position is reached, this is signaled via "Done_2". |

### MC_MoveRelative (S7-1200)

This section contains information on the following topics:

- [MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
- [MC_MoveRelative: Function chart as of V6 (S7-1200)](#mc_moverelative-function-chart-as-of-v6-s7-1200)

#### MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)

##### Description

The "MC_MoveRelative" Motion Control instruction starts a positioning motion relative to the start position.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_MoveRelative command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveRelative command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_PositioningAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Distance | INPUT | REAL | 0.0 | Travel distance for the positioning operation  Limit values:   -1.0E12 ≤ Distance ≤ 1.0E12 |  |
| Velocity | INPUT | REAL | 10.0 | Velocity of axis  This velocity is not always reached on account of the configured acceleration and deceleration and the distance to be traveled.  Limit values:  Start/stop velocity ≤ Velocity ≤ maximum velocity |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Target position reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

#### MC_MoveRelative: Function chart as of V6 (S7-1200)

##### Function chart

![Function chart](images/104081658635_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| Section    ![Function chart](images/103755015307_DV_resource.Stream@PNG-de-DE.png) | The axis is moved by an MC_MoveRelative command by the distance ("Distance") 1000.0. When the axis reaches the target position, this is signaled via "Done_1". When "Done_1" = TRUE, another MC_MoveRelative command, with travel distance 500.0, is started. Because of the response times (e.g., cycle time of user program, etc.), the axis comes to a standstill briefly (see zoomed-in detail). When the axis reaches the new target position, this is signaled via "Done_2". |
| Section    ![Function chart](images/103755736203_DV_resource.Stream@PNG-de-DE.png) | An active MC_MoveRelative command is aborted by another MC_MoveRelative command. The abort is signaled via "Abort_1". The axis is then moved at the new velocity by the new distance ("Distance") 500.0. When the new target position is reached, this is signaled via "Done_2". |

### MC_MoveVelocity (S7-1200)

This section contains information on the following topics:

- [MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
- [MC_MoveVelocity: Function chart as of V6 (S7-1200)](#mc_movevelocity-function-chart-as-of-v6-s7-1200)

#### MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)

##### Description

Motion control instruction "MC_MoveVelocity" moves the axis constantly at the specified velocity.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

MC_MoveVelocity can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveVelocity command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Velocity | INPUT | REAL | 10.0 | Velocity specification for axis motion  Limit values:  Start/stop velocity ≤ |Velocity ≤ maximum velocity  (Velocity = 0.0 is permitted) |  |
| Direction | INPUT | INT | 0 | Direction specification |  |
| 0 | Direction of rotation corresponds to the sign of the value in parameter "Velocity" |  |  |  |  |
| 1 | Positive direction of rotation  (The sign of the value in parameter "Velocity" is ignored) |  |  |  |  |
| 2 | Negative direction of rotation  (The sign of the value in parameter "Velocity" is ignored) |  |  |  |  |
| Current | INPUT | BOOL | FALSE | Maintain current velocity |  |
| FALSE | "Maintain current velocity" is deactivated. The values of parameters "Velocity" and "Direction" are used. |  |  |  |  |
| TRUE | "Maintain current velocity" is activated. The values in parameters "Velocity" and "Direction" are not taken into account.  When the axis resumes motion at the current velocity, the "InVelocity" parameter returns the value TRUE. |  |  |  |  |
| PositionControlled | INPUT | BOOL | TRUE | FALSE | Non position-controlled operation |
| TRUE | Position-controlled operation |  |  |  |  |
| The parameter applies as long as the "MC_MoveVelocity" command is being executed. After this, the setting of MC_Power applies again.  This parameter is ignored when a PTO axis is used. |  |  |  |  |  |
| InVelocity | OUTPUT | BOOL | FALSE | TRUE | - "Current" = FALSE:   The velocity specified in parameter "Velocity" was reached. - "Current" = TRUE:   The axis travels at the current velocity at the start time. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

> **Note**
>
> **PLCopen Version 2.0**
>
> The Motion Control instruction "MC_MoveVelocity" is compatible to PLCopen Version 2.0 as of V4.
>
> The "InVelocity" and "Busy" parameters show their status regardless of the "Execute" parameter until the command is overridden or stopped by an error. For more information, refer to the section " Tracking active commands.

##### Behavior with zero setpoint velocity (Velocity = 0.0)

An MC_MoveVelocity command with "Velocity" = 0.0 (such as an MC_Halt command) aborts active motion commands and stops the axis with the configured deceleration.

When the axis comes to a standstill, output parameter "InVelocity" indicates TRUE for at least one program cycle.

"Busy" indicates the value TRUE during the deceleration process and changes to FALSE together with "InVelocity". If parameter "Execute" = TRUE is set, "InVelocity" and "Busy" are latched.

When the "MC_MoveVelocity" command is started, status bit "SpeedCommand" is set in the technology object. Status bit "ConstantVelocity" is set upon axis standstill. Both bits are adapted to the new situation when a new motion command is started.

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

#### MC_MoveVelocity: Function chart as of V6 (S7-1200)

##### Function chart

![Function chart](images/104084435211_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| Section    ![Function chart](images/103755015307_DV_resource.Stream@PNG-de-DE.png) | An active MC_MoveVelocity command signals via "InVel_1" that its target velocity has been reached. It is then aborted by another MC_MoveVelocity command. The abort is signaled via "Abort_1". When the new target velocity 15.0 is reached, this is signaled via "InVel_2". The axis then continues moving at the new constant velocity. |
| Section    ![Function chart](images/103755736203_DV_resource.Stream@PNG-de-DE.png) | An active MC_MoveVelocity command is aborted by another MC_MoveVelocity command prior to reaching its target velocity. The abort is signaled via "Abort_1". When the new target velocity 15.0 is reached, this is signaled via "InVel_2". The axis then continues moving at the new constant velocity. |

### MC_MoveJog (S7-1200)

This section contains information on the following topics:

- [MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
- [MC_MoveJog: Function chart as of V6 (S7-1200)](#mc_movejog-function-chart-as-of-v6-s7-1200)

#### MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)

##### Description

Motion control instruction "MC_MoveJog" moves the axis constantly at the specified velocity in jog mode. You use this Motion Control instruction, for example, for testing and commissioning purposes.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_MoveJog command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveJog command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| JogForward | INPUT | BOOL | FALSE | As long as the parameter is TRUE, the axis moves in the positive direction at the velocity specified in parameter "Velocity". |  |
| JogBackward | INPUT | BOOL | FALSE | As long as the parameter is TRUE, the axis moves in the negative direction at the velocity specified in parameter "Velocity". |  |
| If both parameters are simultaneously TRUE, the axis stops with the configured deceleration. An error is indicated in parameters "Error", "ErrorID", and "ErrorInfo". |  |  |  |  |  |
| Velocity | INPUT | REAL | 10.0 | Preset velocity for jog mode  Limit values:  Start/stop velocity ≤ velocity ≤ maximum velocity |  |
| PositionControlled | INPUT | BOOL | TRUE | FALSE | Non position-controlled operation |
| TRUE | Position-controlled operation |  |  |  |  |
| The parameter applies as long as the "MC_MoveJog" command is being executed. After this, the setting of MC_Power applies again.  This parameter is ignored when a PTO axis is used. |  |  |  |  |  |
| InVelocity | OUTPUT | BOOL | FALSE | TRUE | The velocity specified in parameter "Velocity" was reached. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

#### MC_MoveJog: Function chart as of V6 (S7-1200)

##### Function chart

![Function chart](images/104088389387_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 5.0

| Symbol | Meaning |
| --- | --- |
| Section    ![Function chart](images/103755015307_DV_resource.Stream@PNG-de-DE.png) | The axis is moved in the positive direction in jog mode via "Jog_F". When the target velocity 50.0 is reached, this is signaled via "InVel_1". After "Jog_F" is reset, the axis is braked to a standstill. |
| Section    ![Function chart](images/103755736203_DV_resource.Stream@PNG-de-DE.png) | The axis is moved in the negative direction in jog mode via "Jog_B". When the target velocity -50.0 is reached, this is signaled via "InVel_1".   When "Jog_B" is set, the value at parameter "Velocity" changes to 25.0. "InVel_1" is reset and the axis is braked. When the new target velocity -25.0 is reached, this is signaled via "InVel_1". After "Jog_B" is reset, the axis is braked to a standstill. |

### MC_CommandTable (S7-1200)

This section contains information on the following topics:

- [MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)

#### MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)

##### Description

The Motion Control instruction "MC_CommandTable" combines multiple individual axis control commands in one movement sequence. "MC_CommandTable" is available for axes with drive connection via PTO (Pulse Train Output).

##### Requirements

- The positioning axis technology object has been inserted and correctly configured.
- The drive is connected via PTO (Pulse Train Output).
- The command table technology object has been inserted and correctly configured.
- The axis is enabled.

##### Override response

The MC_CommandTable command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_CommandTable command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The active Motion Control command is canceled by the start of the first "Positioning Relative", "Positioning Absolute", "Velocity set point" or "Halt" command.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| CommandTable | INPUT | TO_CommandTable | - | Command table technology object |  |
| Execute | INPUT | BOOL | FALSE | Command table start with positive edge |  |
| StartStep | INPUT | INT | 1 | Defines the step at which the execution of the command table should begin  Limit values:  1 ≤ StartStep ≤ EndStep |  |
| EndStep | INPUT | INT | 32 | Defines the step up to which the execution of command table should take place  Limit values:  StartStep ≤ EndStep ≤ 32 |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Command table has been successfully executed |
| Busy | OUTPU | BOOL | FALSE | TRUE | The command table is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | The command table was canceled by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command table. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |
| CurrentStep | OUTPUT | INT | 0 | Step in command table currently being executed |  |
| StepCode | OUTPUT | WORD | 16#0000 | User-defined numerical value / bit pattern of the step currently being executed |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

### MC_ChangeDynamic (S7-1200)

This section contains information on the following topics:

- [MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)

#### MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)

##### Description

Motion Control instruction "MC_ChangeDynamic" allows you to change the following settings of the axis:

- Change the ramp-up time (acceleration) value
- Change the ramp-down time (deceleration) value
- Change the emergency stop ramp-down time (emergency stop deceleration) value
- Change the smoothing time (jerk) value

For the effectiveness of the change, refer to the description of the tag.

##### Requirements

The positioning axis technology object has been configured correctly.

##### Override response

A MC_ChangeDynamic command cannot be aborted by any other Motion Control command.

A new MC_ChangeDynamic command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |  |
| ChangeRampUp | INPUT | BOOL | FALSE | TRUE |  | Change ramp-up time in line with input parameter "RampUpTime" |
| RampUpTime | INPUT | REAL | 5.00 | Time (in seconds) to accelerate axis from standstill to configured maximum velocity without jerk limit.  The change will influence the tag <Axis name>. Config.DynamicDefaults.Acceleration. For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeRampDown | INPUT | BOOL | FALSE | TRUE |  | Change ramp-down time to correspond to input parameter "RampDownTime" |
| RampDownTime | INPUT | REAL | 5.00 | Time (in seconds) to decelerate axis from the configured maximum velocity to standstill without jerk limiter.  The change will influence the tag <Axis name>. Config.DynamicDefaults.Deceleration . For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeEmergency | INPUT | BOOL | FALSE | TRUE |  | Change emergency stop ramp-down time in line with input parameter "EmergencyRampTime" |
| EmergencyRampTime | INPUT | REAL | 2.00 | Time (in seconds) to decelerate the axis from configured maximum velocity to standstill without jerk limiter in emergency stop mode.   The change will influence the tag <Axis name>. Config.DynamicDefaults.EmergencyDeceleration . For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeJerkTime | INPUT | BOOL | FALSE | TRUE |  | Change smoothing time according to the input parameter "JerkTime" |
| JerkTime | INPUT | REAL | 0.25 | Smoothing time (in seconds) used for the axis acceleration and deceleration ramps  The change will influence the tag <Axis name>. Config.DynamicDefaults.Jerk . For the effectiveness of the change, refer to the description of this tag. |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | The changed values have been written to the technology data block. The description of the tags will show when the change becomes effective. |  |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |  |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |  |

> **Note**
>
> At the input parameters "RampUpTime", "RampDownTime", "EmergencyRampTime" and "JerkTime", values can be entered which exceed the admissible limits of the resulting parameters: "Acceleration", "Deceleration", "Emergency stop deceleration" and "Jerk".
>
> Ensure that your inputs are within the valid range, taking into consideration the equations and limits in section "Dynamic".

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

### MC_ReadParam (S7-1200)

This section contains information on the following topics:

- [MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)

#### MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)

##### Description

The Motion Control instruction "MC_ReadParam" enables continuous reading of motion data and status messages of an axis. The current value of the corresponding tags is determined at the start of the command.

The following motion data and status messages can be read:

- As of technology version V4:

  - Setpoint position of the axis
  - Setpoint and actual velocity of the axis
  - Current distance of axis from target position
  - Target position of the axis
- Additional as of technology version V5:

  - Actual position of the axis
  - Actual velocity of the axis
  - Current following error
  - Drive status
  - Encoder status
  - Status bits
  - Error bits

##### Requirements

The positioning axis technology object has been configured correctly.

##### Override response

A MC_ReadParam command cannot be aborted by any other Motion Control command.

A new MC_ReadParam command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Enable | INPUT | BOOL | FALSE | TRUE | Read the tag specified with the "Parameter" and store the value in the destination address specified with "Value". |
| FALSE | Do not update assigned motion data |  |  |  |  |
| Parameter | INPUT | VARIANT (REAL) | - | VARIANT pointer to the value to be read. The following tags are permitted:   - <Axis name>.Position - <Axis name>.Velocity - <Axis name>.ActualPosition - <Axis name>.ActualVelocity - <Axis name>.StatusPositioning.<Tag name> - <Axis name>.StatusDrive.<Tag name> - <Axis name>.StatusSensor.<Tag name> - <Axis name>.StatusBits.<Tag name> - <Axis name>.ErrorBits.<Tag name>   The description of the tags named and the tag structures can be found in the Appendix AUTOHOTSPOT. |  |
| Value | INOUT | VARIANT (REAL) | - | VARIANT pointer to the target tag or destination address to which the read value is to be written. |  |
| Valid | OUTPUT | BOOL | FALSE | TRUE | The read value is valid. |
| FALSE | The read value is invalid. |  |  |  |  |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

### MC_WriteParam (S7-1200)

This section contains information on the following topics:

- [MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-as-of-v6-s7-1200)

#### MC_WriteParam: Write tag of positioning axis as of V6 (S7-1200)

##### Description

Motion Control instruction "MC_WriteParam" enables the writing of tags of the positioning axis technology object in the user program. In contrast to the value assignment of the tags in the user program, "MC_WriteParam" can also change values of read-only tags.

You can learn about the tags, the conditions under which they can be written and the time at which they take effect in the description of the technology object tags.

##### Requirements

- The positioning axis technology object has been configured correctly.
- To write tags that are read-only in the user program, the axis must be disabled.
- Tags whose change requires a restart cannot be written with "MC_WriteParam".

##### Override response

A MC_WriteParam command cannot be aborted by any other Motion Control command.

A new MC_WriteParam command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Parameter | INPUT | VARIANT (BOOL, INT, DINT, UDINT, REAL) | - | VARIANT pointer to the technology object tags positioning axis (destination address) to be written |  |
| Value | INPUT | VARIANT (BOOL, INT, DINT, UDINT, REAL) | - | VARIANT pointer to the value to be written (source address) |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Value was written |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis as of V6 (S7-1200)](#mc_power-enable-disable-axis-as-of-v6-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object as of V6 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-as-of-v6-s7-1200)
  
[MC_Home: Home axes, set reference point as of V6 (S7-1200)](#mc_home-home-axes-set-reference-point-as-of-v6-s7-1200)
  
[MC_Halt: Stop axis as of V6 (S7-1200)](#mc_halt-stop-axis-as-of-v6-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis as of V6 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis as of V6 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-as-of-v6-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity as of V6 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-as-of-v6-s7-1200)
  
[MC_MoveJog: Move axis in jog mode as of V6 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-as-of-v6-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence as of V6 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-as-of-v6-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis as of V6 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-as-of-v6-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis as of V6 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-as-of-v6-s7-1200)

## S7-1200 Motion Control V4...5 (S7-1200)

This section contains information on the following topics:

- [MC_Power (S7-1200)](#mc_power-s7-1200-1)
- [MC_Reset (S7-1200)](#mc_reset-s7-1200-1)
- [MC_Home (S7-1200)](#mc_home-s7-1200-1)
- [MC_Halt (S7-1200)](#mc_halt-s7-1200-1)
- [MC_MoveAbsolute (S7-1200)](#mc_moveabsolute-s7-1200-1)
- [MC_MoveRelative (S7-1200)](#mc_moverelative-s7-1200-1)
- [MC_MoveVelocity (S7-1200)](#mc_movevelocity-s7-1200-1)
- [MC_MoveJog (S7-1200)](#mc_movejog-s7-1200-1)
- [MC_CommandTable (S7-1200)](#mc_commandtable-s7-1200-1)
- [MC_ChangeDynamic (S7-1200)](#mc_changedynamic-s7-1200-1)
- [MC_ReadParam (S7-1200)](#mc_readparam-s7-1200-1)
- [MC_WriteParam (S7-1200)](#mc_writeparam-s7-1200-1)

### MC_Power (S7-1200)

This section contains information on the following topics:

- [MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
- [MC_Power: Function chart V4...5 (S7-1200)](#mc_power-function-chart-v45-s7-1200)

#### MC_Power: Enable, disable axis V4...5 (S7-1200)

##### Description

The Motion Control instruction "MC_Power" enables or disables an axis.

##### Requirements

- The positioning axis technology object has been configured correctly.
- There is no pending enable-inhibiting error.

##### Override response

Execution of "MC_Power" cannot be aborted by a Motion Control command.

Disabling the axis (input parameter "Enable" = FALSE) aborts all Motion Control commands for the associated technology object in accordance with the selected "StopMode".

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis | - | Axis technology object |  |
| Enable | INPUT | BOOL | FALSE | TRUE | The axis is enabled. |
| FALSE | All current jobs are interrupted in accordance with the "StopMode" configured. The axis is stopped and disabled. |  |  |  |  |
| StopMode | INPUT | INT | 0 | 0 | Emergency stop  If a request to disable the axis is pending, the axis brakes at the configured emergency deceleration. The axis is disabled after reaching standstill. |
| 1 | Immediate stop  If a request to disable the axis is pending, this setpoint zero is output and the axis is disabled. The axis is braked depending on the configuration in the drive, and is brought to a standstill.  With drive connection via PTO (Pulse Train Output): When you disable the axis, the pulse output is stopped with a frequency-dependent deceleration:  - Output frequency ≥ 100 Hz   Deceleration: max. 30 ms - Output frequency < 100 Hz   Deceleration: 30 ms up to max. 1.5 s at 2 Hz |  |  |  |  |
| 2 | Emergency stop with jerk control  If a request to disable the axis is pending, the axis brakes at the configured emergency deceleration. If the jerk control is activated, the configured jerk is taken into account. The axis is disabled after reaching standstill. |  |  |  |  |
| Status | OUTPUT | BOOL | FALSE | Status of axis enable |  |
| FALSE | The axis is disabled.  The axis does not execute Motion Control commands and does not accept any new commands (exception: MC_Reset command).  For drive connection via PTO (Pulse Train Output):  The axis is not homed.  Upon disabling, the status does not change to FALSE until the axis reaches a standstill. |  |  |  |  |
| TRUE | The axis is enabled.  The axis is ready to execute Motion Control commands.  Upon axis enabling, the status does not change to TRUE until the signal "Drive ready" is pending. If the "Drive ready" drive interface was not configured in the axis configuration, the status changes to TRUE immediately. |  |  |  |  |
| Busy | OUTPUT | BOOL | FALSE | TRUE | "MC_Power" is active. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred in Motion Control instruction "MC_Power" or in the associated technology object. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

> **Note**
>
> If the axis is switched off due to an error, it will be enabled again automatically after the error has been eliminated and acknowledged. This requires that the input parameter "Enable" has retained the value TRUE during this process.

##### Enabling an axis with configured drive interface

To enable the axis, follow these steps:

1. Check the requirements indicated above.
2. Initialize input parameter "StopMode" with the desired value. Set the input parameter "Enable" to TRUE.

   The enable output for "Drive enabled" changes to TRUE to enable the power to the drive. The CPU waits for the "Drive ready" signal of the drive.

   When the "Drive ready" signal is available at the configured ready input of the CPU, the axis is enabled. The output parameter "Status" and the tag of the technology object <Axis name>.StatusBits.Enable indicate the value TRUE.

##### Enabling an axis without configured drive interface

To enable the axis, follow these steps:

1. Check the requirements indicated above.
2. Initialize input parameter "StopMode" with the desired value. Set the input parameter "Enable" to TRUE. The axis is enabled. The output parameter "Status" and the tag of the technology object <Axis name>.StatusBits.Enable indicate the value TRUE.

##### Disabling an axis

To disable an axis, you can follow the steps described below:

1. Bring the axis to a standstill.

   You can identify when the axis is at a standstill in the tag of the technology object <Axis name>.StatusBits.StandStill.
2. Set input parameter "Enable" to FALSE after standstill is reached.
3. If output parameters "Busy" and "Status" and tag of technology object <Axis name>.StatusBits.Enable indicate the value FALSE, disabling of the axis is complete.

---

**See also**

[MC_Power: Function chart V4...5 (S7-1200)](#mc_power-function-chart-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

#### MC_Power: Function chart V4...5 (S7-1200)

##### Function chart

![Function chart](images/88122167947_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | An axis is enabled and then disabled again. When the drive has signaled "Drive ready" back to the CPU, the successful enable can be read out via "Status_1". |
| ② | Following an axis enable, an error has occurred that caused the axis to be disabled. The error is eliminated and acknowledged with "MC_Reset". The axis is then enabled again. |

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)

### MC_Reset (S7-1200)

This section contains information on the following topics:

- [MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)

#### MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)

##### Description

Motion Control instruction "MC_Reset" can be used to acknowledge "Operating error with axis stop" and "Configuration error". The errors that require acknowledgment can be found in the "List of ErrorIDs and ErrorInfos" under "Remedy".

The axis configuration can be downloaded to the work memory after a download in RUN mode.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The cause of a pending configuration error requiring acknowledgment has been eliminated (for example, acceleration in positioning axis technology object has been changed to a valid value).

##### Override response

The MC_Reset command cannot be aborted by any other Motion Control command.

The new MC_Reset command does not abort any other active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Restart | INPUT | BOOL | FALSE | TRUE | Download the axis configuration from the load memory to the work memory. The command can only be executed when the axis is disabled.  Refer to the notes on Download to the CPU. |
| FALSE | Acknowledges pending errors |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Error has been acknowledged. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

##### Acknowledging an error requiring acknowledgment with MC_Reset

To acknowledge an error, follow these steps:

1. Check the requirements indicated above.
2. Start the acknowledgment of the error with a rising edge at input parameter "Execute".
3. If output parameter "Done" indicates the value TRUE and tag of technology object <Axis name>.StatusBits.Error the value FALSE, the error has been acknowledged.

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

### MC_Home (S7-1200)

This section contains information on the following topics:

- [MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)

#### MC_Home: Home axis, set home position V4...5 (S7-1200)

##### Description

Motion Control instruction "MC_Home" is used to match the axis coordinates to the real, physical drive position. Homing is required for absolute positioning of the axis. The following types of homing can be executed:

- Active homing (Mode = 3)

  The homing procedure is executed automatically.
- Passive homing (Mode = 2)

  During passive homing, the "MC_Home" Motion Control instruction does not carry out any homing motion. The traversing motion required for this must be implemented by the user via other Motion Control instructions. When the homing switch is detected, the axis is homed.
- Direct homing absolute (Mode = 0)

  The current axis position is set to the value of parameter "Position".
- Direct homing relative (Mode = 1)

  The current axis position is offset by the value of parameter "Position".
- Absolute encoder adjustment relative (Mode = 6)

  The current axis position is offset by the value of parameter "Position".
- Absolute encoder adjustment absolute (Mode = 7)

  The current axis position is set to the value of parameter "Position".

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.
- No MC_CommandTable command may be active upon start with Mode = 0, 1, or 2.

##### Override response

The override response depends on the selected mode:

**Mode**
**= 0, 1, 6, 7**

The MC_Home command cannot be aborted by any other Motion Control command.

The MC_Home command does not abort any active Motion Control commands. Position-related motion commands are resumed after homing according to the new homing position (value at input parameter: "Position").

**Mode**
**= 2**

The MC_Home command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 2, 3

The new MC_Home command aborts the following active Motion Control command:

- MC_Home command Mode = 2

Position-related motion commands are resumed after homing according to the new homing position (value at input parameter: "Position").

**Mode**
**= 3**

The MC_Home command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_Home command aborts the following active Motion Control commands:

- MC_Home command Mode = 2, 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Position | INPUT | REAL | 0.0 | - Mode = 0, 2, and 3   Absolute position of axis after completion of the homing operation - Mode = 1   Correction value for the current axis position  Limit values:  -1.0e<sup>12</sup> ≤ Position ≤ 1.0e<sup>12</sup> |  |
| Mode | INPUT | INT | 0 | Homing mode |  |
| 0 | Direct homing (absolute)  New axis position is the position value of parameter "Position". |  |  |  |  |
| 1 | Direct homing (relative)  New axis position is the current axis position + position value of parameter "Position". |  |  |  |  |
| 2 | Passive homing  Homing according to the axis configuration. Following homing, the value of parameter "Position" is set as the new axis position. |  |  |  |  |
| 3 | Active homing  Homing procedure in accordance with the axis configuration. Following homing, the value of parameter "Position" is set as the new axis position. |  |  |  |  |
| 6 | Absolute encoder adjustment (relative)  The current axis position is offset by the value of parameter "Position". The calculated absolute value offset is stored retentively in the CPU. (<AxisName>.StatusSensor.AbsEncoderOffset) |  |  |  |  |
| 7 | Absolute encoder adjustment (absolute)  The current axis position is set to the value of parameter "Position". The calculated absolute value offset is stored retentively in the CPU. (<AxisName>.StatusSensor.AbsEncoderOffset) |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Command completed |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

##### Resetting the "Homed" status

The "Homed" status of a technology object (<Axis name>.StatusBits.HomingDone) is reset under the following conditions:

- **Drive connection via** 
  **PTO (Pulse Train Output)**
  **:**

  - Start an "MC_Home" command for active homing

    (After successful completion of the homing operation, the "Homed" status is set again.)
  - Disabling of axis by the "MC_Power" Motion Control instruction
  - Changeover between automatic mode and manual control
  - After POWER OFF -> POWER ON of the CPU
  - After CPU restart (RUN-STOP -> STOP-RUN)
- **Technology objects with incremental actual values:**

  - Start an "MC_Home" command for active homing

    (After successful completion of the homing operation, the "Homed" status is set again.)
  - Error in the encoder system, or encoder failure
  - Restart of the technology object
  - After POWER OFF → POWER ON of the CPU
  - Memory reset
  - Modification of the encoder configuration
- **Technology objects with absolute actual values:**

  - Errors in the sensor system/encoder failure
  - Replacement of the CPU
  - Modification of the encoder configuration
  - Restoration of the CPU factory settings
  - Transfer of a different project to the controller

##### Homing an axis

To home the axis, follow these stops:

1. Check the requirements indicated above.
2. Provide the necessary input parameters with values and start the homing operation with a rising edge at input parameter "Execute".
3. If output parameter "Done" and technology object tag <Axis name>.StatusBits.HomingDone indicate the value TRUE, homing is complete.

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

### MC_Halt (S7-1200)

This section contains information on the following topics:

- [MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
- [MC_Halt: Function chart V4...5 (S7-1200)](#mc_halt-function-chart-v45-s7-1200)

#### MC_Halt: Stop axis V4...5 (S7-1200)

##### Description

The "MC_Halt" Motion Control instruction stops all movements and brings the axis to a standstill with the configured deceleration. The standstill position is not defined.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_Halt command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_Halt command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Zero velocity reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Halt: Function chart V4...5 (S7-1200)](#mc_halt-function-chart-v45-s7-1200)
  
[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

#### MC_Halt: Function chart V4...5 (S7-1200)

##### Function chart

![Function chart](images/88122172043_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 5.0

| Symbol | Meaning |
| --- | --- |
| ① | The axis is braked by an MC_Halt command until it comes to a standstill. The axis standstill is signaled via "Done_2". |
| ② | While an MC_Halt command is braking the axis, this command is aborted by another motion command. The abort is signaled via "Abort_2". |

---

**See also**

[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)

### MC_MoveAbsolute (S7-1200)

This section contains information on the following topics:

- [MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
- [MC_MoveAbsolute: Function chart V4...5 (S7-1200)](#mc_moveabsolute-function-chart-v45-s7-1200)

#### MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)

##### Description

The "MC_MoveAbsolute" Motion Control instruction starts an axis positioning motion to move it to an absolute position.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.
- The axis is homed.

##### Override response

The MC_MoveAbsolute command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveAbsolute command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_PositioningAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Position | INPUT | REAL | 0.0 | Absolute target position  Limit values:   -1.0e<sup>12</sup> ≤ Position ≤ 1.0e<sup>12</sup> |  |
| Velocity | INPUT | REAL | 10.0 | Velocity of axis  This velocity is not always reached on account of the configured acceleration and deceleration and the target position to be approached.  Limit values:  Start/stop velocity ≤ Velocity ≤ maximum velocity |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Absolute target position reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_MoveAbsolute: Function chart V4...5 (S7-1200)](#mc_moveabsolute-function-chart-v45-s7-1200)
  
[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

#### MC_MoveAbsolute: Function chart V4...5 (S7-1200)

##### Function chart

![Function chart](images/59361187339_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| ① | An axis is moved to absolute position 1000.0 with an MC_MoveAbsolute command. When the axis reaches the target position, this is signaled via "Done_1". When "Done_1" = TRUE, another MC_MoveAbsolute command, with target position 1500.0, is started. Because of the response times (e.g., cycle time of user program, etc.), the axis comes to a standstill briefly (see zoomed-in detail). When the axis reaches the new target position, this is signaled via "Done_2". |
| ② | An active MC_MoveAbsolute command is aborted by another MC_MoveAbsolute command. The abort is signaled via "Abort_1". The axis is then moved at the new velocity to the new target position 1500.0. When the new target position is reached, this is signaled via "Done_2". |

---

**See also**

[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)

### MC_MoveRelative (S7-1200)

This section contains information on the following topics:

- [MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
- [MC_MoveRelative: Function chart V4...5 (S7-1200)](#mc_moverelative-function-chart-v45-s7-1200)

#### MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)

##### Description

The "MC_MoveRelative" Motion Control instruction starts a positioning motion relative to the start position.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_MoveRelative command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveRelative command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_PositioningAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Distance | INPUT | REAL | 0.0 | Travel distance for the positioning operation  Limit values:   -1.0e<sup>12</sup> ≤ Distance  ≤ 1.0e<sup>12</sup> |  |
| Velocity | INPUT | REAL | 10.0 | Velocity of axis  This velocity is not always reached on account of the configured acceleration and deceleration and the distance to be traveled.  Limit values:  Start/stop velocity ≤ Velocity ≤ maximum velocity |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Target position reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_MoveRelative: Function chart V4...5 (S7-1200)](#mc_moverelative-function-chart-v45-s7-1200)
  
[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

#### MC_MoveRelative: Function chart V4...5 (S7-1200)

##### Function chart

![Function chart](images/104081658635_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| ① | The axis is moved by an MC_MoveRelative command by the distance ("Distance") 1000.0. When the axis reaches the target position, this is signaled via "Done_1". When "Done_1" = TRUE, another MC_MoveRelative command, with travel distance 500.0, is started. Because of the response times (e.g., cycle time of user program, etc.), the axis comes to a standstill briefly (see zoomed-in detail). When the axis reaches the new target position, this is signaled via "Done_2". |
| ② | An active MC_MoveRelative command is aborted by another MC_MoveRelative command. The abort is signaled via "Abort_1". The axis is then moved at the new velocity by the new distance ("Distance") 500.0. When the new target position is reached, this is signaled via "Done_2". |

---

**See also**

[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)

### MC_MoveVelocity (S7-1200)

This section contains information on the following topics:

- [MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
- [MC_MoveVelocity: Function chart V4...5 (S7-1200)](#mc_movevelocity-function-chart-v45-s7-1200)

#### MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)

##### Description

Motion control instruction "MC_MoveVelocity" moves the axis constantly at the specified velocity.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

MC_MoveVelocity can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveVelocity command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Velocity | INPUT | REAL | 10.0 | Velocity specification for axis motion  Limit values:  Start/stop velocity ≤ |Velocity ≤ maximum velocity  (Velocity = 0.0 is permitted) |  |
| Direction | INPUT | INT | 0 | Direction specification |  |
| 0 | Direction of rotation corresponds to the sign of the value in parameter "Velocity" |  |  |  |  |
| 1 | Positive direction of rotation  (The sign of the value in parameter "Velocity" is ignored) |  |  |  |  |
| 2 | Negative direction of rotation  (The sign of the value in parameter "Velocity" is ignored) |  |  |  |  |
| Current | INPUT | BOOL | FALSE | Maintain current velocity |  |
| FALSE | "Maintain current velocity" is deactivated. The values of parameters "Velocity" and "Direction" are used. |  |  |  |  |
| TRUE | "Maintain current velocity" is activated. The values in parameters "Velocity" and "Direction" are not taken into account.  When the axis resumes motion at the current velocity, the "InVelocity" parameter returns the value TRUE. |  |  |  |  |
| InVelocity | OUTPUT | BOOL | FALSE | TRUE | - "Current" = FALSE:   The velocity specified in parameter "Velocity" was reached. - "Current" = TRUE:   The axis travels at the current velocity at the start time. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

> **Note**
>
> **PLCopen Version 2.0**
>
> The Motion Control instruction "MC_MoveVelocity" is compatible to PLCopen Version 2.0 as of V4.
>
> The "InVelocity" and "Busy" parameters show their status regardless of the "Execute" parameter until the command is overridden or stopped by an error. For more information, refer to the section " Tracking active commands.

##### Behavior with zero setpoint velocity (Velocity = 0.0)

An MC_MoveVelocity command with "Velocity" = 0.0 (such as an MC_Halt command) aborts active motion commands and stops the axis with the configured deceleration.

When the axis comes to a standstill, output parameter "InVelocity" indicates TRUE for at least one program cycle.

"Busy" indicates the value TRUE during the deceleration process and changes to FALSE together with "InVelocity". If parameter "Execute" = TRUE is set, "InVelocity" and "Busy" are latched.

When the "MC_MoveVelocity" command is started, status bit "SpeedCommand" is set in the technology object. Status bit "ConstantVelocity" is set upon axis standstill. Both bits are adapted to the new situation when a new motion command is started.

---

**See also**

[MC_MoveVelocity: Function chart V4...5 (S7-1200)](#mc_movevelocity-function-chart-v45-s7-1200)
  
[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

#### MC_MoveVelocity: Function chart V4...5 (S7-1200)

##### Function chart

![Function chart](images/59361525515_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| ① | An active MC_MoveVelocity command signals via "InVel_1" that its target velocity has been reached. It is then aborted by another MC_MoveVelocity command. The abort is signaled via "Abort_1". When the new target velocity 15.0 is reached, this is signaled via "InVel_2". The axis then continues moving at the new constant velocity. |
| ② | An active MC_MoveVelocity command is aborted by another MC_MoveVelocity command prior to reaching its target velocity. The abort is signaled via "Abort_1". When the new target velocity 15.0 is reached, this is signaled via "InVel_2". The axis then continues moving at the new constant velocity. |

---

**See also**

[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)

### MC_MoveJog (S7-1200)

This section contains information on the following topics:

- [MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
- [MC_MoveJog: Function chart V4...5 (S7-1200)](#mc_movejog-function-chart-v45-s7-1200)

#### MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)

##### Description

Motion control instruction "MC_MoveJog" moves the axis constantly at the specified velocity in jog mode. You use this Motion Control instruction, for example, for testing and commissioning purposes.

##### Requirements

- The positioning axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_MoveJog command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveJog command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| JogForward | INPUT | BOOL | FALSE | As long as the parameter is TRUE, the axis moves in the positive direction at the velocity specified in parameter "Velocity". |  |
| JogBackward | INPUT | BOOL | FALSE | As long as the parameter is TRUE, the axis moves in the negative direction at the velocity specified in parameter "Velocity". |  |
| If both parameters are simultaneously TRUE, the axis stops with the configured deceleration. An error is indicated in parameters "Error", "ErrorID", and "ErrorInfo". |  |  |  |  |  |
| Velocity | INPUT | REAL | 10.0 | Preset velocity for jog mode  Limit values:  Start/stop velocity ≤ velocity ≤ maximum velocity |  |
| InVelocity | OUTPUT | BOOL | FALSE | TRUE | The velocity specified in parameter "Velocity" was reached. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_MoveJog: Function chart V4...5 (S7-1200)](#mc_movejog-function-chart-v45-s7-1200)
  
[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

#### MC_MoveJog: Function chart V4...5 (S7-1200)

##### Function chart

![Function chart](images/59361745419_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 5.0

| Symbol | Meaning |
| --- | --- |
| ① | The axis is moved in the positive direction in jog mode via "Jog_F". When the target velocity 50.0 is reached, this is signaled via "InVel_1". After "Jog_F" is reset, the axis is braked to a standstill. |
| ② | The axis is moved in the negative direction in jog mode via "Jog_B". When the target velocity -50.0 is reached, this is signaled via "InVel_1".   When "Jog_B" is set, the value at parameter "Velocity" changes to 25.0. "InVel_1" is reset and the axis is braked. When the new target velocity -25.0 is reached, this is signaled via "InVel_1". After "Jog_B" is reset, the axis is braked to a standstill. |

---

**See also**

[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)

### MC_CommandTable (S7-1200)

This section contains information on the following topics:

- [MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)

#### MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)

##### Description

The Motion Control instruction "MC_CommandTable" combines multiple individual axis control commands in one movement sequence. "MC_CommandTable" is available for axes with drive connection via PTO (Pulse Train Output).

##### Requirements

- The positioning axis technology object has been inserted and correctly configured.
- The drive is connected via PTO (Pulse Train Output).
- The command table technology object has been inserted and correctly configured.
- The axis is enabled.

##### Override response

The MC_CommandTable command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_CommandTable command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The active Motion Control command is canceled by the start of the first "Positioning Relative", "Positioning Absolute", "Velocity set point" or "Halt" command.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |
| CommandTable | INPUT | TO_CommandTable | - | Command table technology object |  |
| Execute | INPUT | BOOL | FALSE | Command table start with positive edge |  |
| StartStep | INPUT | INT | 1 | Defines the step at which the execution of the command table should begin  Limit values:  1 ≤ StartStep ≤ EndStep |  |
| EndStep | INPUT | INT | 32 | Defines the step up to which the execution of command table should take place  Limit values:  StartStep ≤ EndStep ≤ 32 |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Command table has been successfully executed |
| Busy | OUTPU | BOOL | FALSE | TRUE | The command table is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | The command table was canceled by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command table. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |
| CurrentStep | OUTPUT | INT | 0 | Step in command table currently being executed |  |
| StepCode | OUTPUT | WORD | 16#0000 | User-defined numerical value / bit pattern of the step currently being executed |  |

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

### MC_ChangeDynamic (S7-1200)

This section contains information on the following topics:

- [MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)

#### MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)

##### Description

Motion Control instruction "MC_ChangeDynamic" allows you to change the following settings of the axis:

- Change the ramp-up time (acceleration) value
- Change the ramp-down time (deceleration) value
- Change the emergency stop ramp-down time (emergency stop deceleration) value
- Change the smoothing time (jerk) value

For the effectiveness of the change, refer to the description of the tag.

##### Requirements

The positioning axis technology object has been configured correctly.

##### Override response

A MC_ChangeDynamic command cannot be aborted by any other Motion Control command.

A new MC_ChangeDynamic command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_SpeedAxis | - | Axis technology object |  |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |  |
| ChangeRampUp | INPUT | BOOL | FALSE | TRUE |  | Change ramp-up time in line with input parameter "RampUpTime" |
| RampUpTime | INPUT | REAL | 5.00 | Time (in seconds) to accelerate axis from standstill to configured maximum velocity without jerk limit.  The change will influence the tag <Axis name>. Config.DynamicDefaults.Acceleration. For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeRampDown | INPUT | BOOL | FALSE | TRUE |  | Change ramp-down time to correspond to input parameter "RampDownTime" |
| RampDownTime | INPUT | REAL | 5.00 | Time (in seconds) to decelerate axis from the configured maximum velocity to standstill without jerk limiter.  The change will influence the tag <Axis name>. Config.DynamicDefaults.Deceleration . For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeEmergency | INPUT | BOOL | FALSE | TRUE |  | Change emergency stop ramp-down time in line with input parameter "EmergencyRampTime" |
| EmergencyRampTime | INPUT | REAL | 2.00 | Time (in seconds) to decelerate the axis from configured maximum velocity to standstill without jerk limiter in emergency stop mode.   The change will influence the tag <Axis name>. Config.DynamicDefaults.EmergencyDeceleration . For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeJerkTime | INPUT | BOOL | FALSE | TRUE |  | Change smoothing time according to the input parameter "JerkTime" |
| JerkTime | INPUT | REAL | 0.25 | Smoothing time (in seconds) used for the axis acceleration and deceleration ramps  The change will influence the tag <Axis name>. Config.DynamicDefaults.Jerk . For the effectiveness of the change, refer to the description of this tag. |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | The changed values have been written to the technology data block. The description of the tags will show when the change becomes effective. |  |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |  |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |  |

> **Note**
>
> At the input parameters "RampUpTime", "RampDownTime", "EmergencyRampTime" and "JerkTime", values can be entered which exceed the admissible limits of the resulting parameters: "Acceleration", "Deceleration", "Emergency stop deceleration" and "Jerk".
>
> Ensure that your inputs are within the valid range, taking into consideration the equations and limits in section "Dynamic".

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

### MC_ReadParam (S7-1200)

This section contains information on the following topics:

- [MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)

#### MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)

##### Description

The Motion Control instruction "MC_ReadParam" enables continuous reading of motion data and status messages of an axis. The current value of the corresponding tags is determined at the start of the command.

The following motion data and status messages can be read:

- As of technology version V4:

  - Setpoint position of the axis
  - Setpoint and actual velocity of the axis
  - Current distance of axis from target position
  - Target position of the axis
- Additional as of technology version V5:

  - Actual position of the axis
  - Actual velocity of the axis
  - Current following error
  - Drive status
  - Encoder status
  - Status bits
  - Error bits

##### Requirements

The positioning axis technology object has been configured correctly.

##### Override response

A MC_ReadParam command cannot be aborted by any other Motion Control command.

A new MC_ReadParam command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Enable | INPUT | BOOL | FALSE | TRUE | Read the tag specified with the "Parameter" and store the value in the destination address specified with "Value". |
| FALSE | Do not update assigned motion data |  |  |  |  |
| Parameter | INPUT | VARIANT (REAL) | - | VARIANT pointer to the value to be read. The following tags are permitted:   - <Axis name>.Position - <Axis name>.Velocity - <Axis name>.ActualPosition - <Axis name>.ActualVelocity - <Axis name>.StatusPositioning.<Tag name> - <Axis name>.StatusDrive.<Tag name> - <Axis name>.StatusSensor.<Tag name> - <Axis name>.StatusBits.<Tag name> - <Axis name>.ErrorBits.<Tag name>   The description of the tags named and the tag structures can be found in the Appendix AUTOHOTSPOT. |  |
| Value | INOUT | VARIANT (REAL) | - | VARIANT pointer to the target tag or destination address to which the read value is to be written. |  |
| Valid | OUTPUT | BOOL | FALSE | TRUE | The read value is valid. |
| FALSE | The read value is invalid. |  |  |  |  |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

### MC_WriteParam (S7-1200)

This section contains information on the following topics:

- [MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)](#mc_writeparam-write-tag-of-positioning-axis-v45-s7-1200)

#### MC_WriteParam: Write tag of positioning axis V4...5 (S7-1200)

##### Description

Motion Control instruction "MC_WriteParam" enables the writing of tags of the positioning axis technology object in the user program. In contrast to the value assignment of the tags in the user program, "MC_WriteParam" can also change values of read-only tags.

You can learn about the tags, the conditions under which they can be written and the time at which they take effect in the description of the technology object tags.

##### Requirements

- The positioning axis technology object has been configured correctly.
- To write tags that are read-only in the user program, the axis must be disabled.

##### Override response

A MC_WriteParam command cannot be aborted by any other Motion Control command.

A new MC_WriteParam command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Parameter | INPUT | VARIANT (BOOL, INT, DINT, UDINT*, REAL)  *) as of V5 | - | VARIANT pointer to the technology object tag positioning axis (destination address) to be written |  |
| Value | INPUT | VARIANT (BOOL, INT, DINT, UDINT*, REAL)  *) as of V5 | - | VARIANT pointer to the value to be written (source address) |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Value was written |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[MC_Power: Enable, disable axis V4...5 (S7-1200)](#mc_power-enable-disable-axis-v45-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V4...5 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v45-s7-1200)
  
[MC_Home: Home axis, set home position V4...5 (S7-1200)](#mc_home-home-axis-set-home-position-v45-s7-1200)
  
[MC_Halt: Stop axis V4...5 (S7-1200)](#mc_halt-stop-axis-v45-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V4...5 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v45-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V4...5 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v45-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V4...5 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v45-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V4...5 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v45-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V4...5 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v45-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V4...5 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v45-s7-1200)
  
[MC_ReadParam: Continuously read motion data of a positioning axis V4...5 (S7-1200)](#mc_readparam-continuously-read-motion-data-of-a-positioning-axis-v45-s7-1200)
  
[S7-1200 Motion Control V1...3 (S7-1200)](#s7-1200-motion-control-v13-s7-1200)

## S7-1200 Motion Control V1...3 (S7-1200)

This section contains information on the following topics:

- [MC_Power (S7-1200)](#mc_power-s7-1200-2)
- [MC_Reset (S7-1200)](#mc_reset-s7-1200-2)
- [MC_Home (S7-1200)](#mc_home-s7-1200-2)
- [MC_Halt (S7-1200)](#mc_halt-s7-1200-2)
- [MC_MoveAbsolute (S7-1200)](#mc_moveabsolute-s7-1200-2)
- [MC_MoveRelative (S7-1200)](#mc_moverelative-s7-1200-2)
- [MC_MoveVelocity (S7-1200)](#mc_movevelocity-s7-1200-2)
- [MC_MoveJog (S7-1200)](#mc_movejog-s7-1200-2)
- [MC_CommandTable (S7-1200)](#mc_commandtable-s7-1200-2)
- [MC_ChangeDynamic (S7-1200)](#mc_changedynamic-s7-1200-2)

### MC_Power (S7-1200)

This section contains information on the following topics:

- [MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
- [MC_Power: Function chart V1...3 (S7-1200)](#mc_power-function-chart-v13-s7-1200)

#### MC_Power: Enable, disable axis V1...3 (S7-1200)

##### Description

The Motion Control instruction "MC_Power" enables or disables an axis.

##### Requirements

- The axis technology object has been configured correctly.
- There is no pending enable-inhibiting error.

##### Override response

Execution of "MC_Power" cannot be aborted by a Motion Control command.

Disabling the axis (input parameter "Enable" = FALSE) aborts all Motion Control commands for the associated technology object in accordance with the selected "StopMode".

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Enable | INPUT | BOOL | FALSE | TRUE | Motion Control attempts to enable the axis. |
| FALSE | All current jobs are interrupted in accordance with the "StopMode" configured. The axis is stopped and disabled. |  |  |  |  |
| StopMode | INPUT | INT | 0 | 0 | Emergency stop  If a request to disable the axis is pending, the axis brakes at the configured emergency stop deceleration. The axis is disabled after reaching standstill. |
| 1 | Immediate stop  If a request to disable the axis is pending, this axis is disabled without deceleration. The pulse output is stopped immediately. |  |  |  |  |
| 2 | Emergency stop with jerk control  If a request to disable the axis is pending, the axis brakes at the configured emergency stop deceleration. If the jerk control is activated, the configured jerk is taken into account. The axis is disabled after reaching standstill. |  |  |  |  |
| Status | OUTPUT | BOOL | FALSE | Status of axis enable |  |
| FALSE | The axis is disabled.  The axis does not execute Motion Control commands and does not accept any new commands (exception: MC_Reset command).  The axis is not homed.  Upon disabling, the status does not change to FALSE until the axis reaches a standstill. |  |  |  |  |
| TRUE | The axis is enabled.  The axis is ready to execute Motion Control commands.  Upon axis enabling, the status does not change to TRUE until the signal "Drive ready" is pending. If the "Drive ready" drive interface was not configured in the axis configuration, the status changes to TRUE immediately. |  |  |  |  |
| Busy | OUTPUT | BOOL | FALSE | TRUE | "MC_Power" is active. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred in Motion Control instruction "MC_Power" or in the associated technology object. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

> **Note**
>
> If the axis is switched off due to an error, it will be enabled again automatically after the error has been eliminated and acknowledged. This requires that the input parameter "Enable" has retained the value TRUE during this process.

##### Enabling an axis with configured drive interface

To enable the axis, follow these steps:

1. Check the requirements indicated above.
2. Initialize input parameter "StopMode" with the desired value. Set the input parameter "Enable" to TRUE.

   The enable output for "Drive enabled" changes to TRUE to enable the power to the drive. The CPU waits for the "Drive ready" signal of the drive.

   When the "Drive ready" signal is available at the configured Ready input of the CPU, the axis is enabled. The output parameter "Status" and the tag of the technology object <Axis name>.StatusBits.Enable indicate the value TRUE.

##### Enabling an axis without configured drive interface

To enable the axis, follow these steps:

1. Check the requirements indicated above.
2. Initialize input parameter "StopMode" with the desired value. Set the input parameter "Enable" to TRUE. The axis is enabled. The output parameter "Status" and the tag of the technology object <Axis name>.StatusBits.Enable indicate the value TRUE.

##### Disabling an axis

To disable an axis, you can follow the steps described below:

1. Bring the axis to a standstill.

   You can identify when the axis is at a standstill in the tag of the technology object <Axis name>.StatusBits.StandStill.
2. Set input parameter "Enable" to FALSE after standstill is reached.
3. If output parameters "Busy" and "Status" and the tag of technology object <Axis name>.StatusBits.Enable indicate the value FALSE, disabling of the axis is complete.

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_Power: Function chart V1...3 (S7-1200)](#mc_power-function-chart-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_Power: Function chart V1...3 (S7-1200)

##### Function chart

![Function chart](images/88122167947_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | An axis is enabled and then disabled again. When the drive has signaled "Drive ready" back to the CPU, the successful enable can be read out via "Status_1". |
| ② | Following an axis enable, an error has occurred that caused the axis to be disabled. The error is eliminated and acknowledged with "MC_Reset". The axis is then enabled again. |

---

**See also**

[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)

### MC_Reset (S7-1200)

This section contains information on the following topics:

- [MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)

#### MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)

##### Description

Motion Control instruction "MC_Reset" can be used to acknowledge "Operating error with axis stop" and "Configuration error". The errors that require acknowledgement can be found in the "List of ErrorIDs and ErrorInfos" under "Remedy".

From version V3.0, the axis configuration can be downloaded to the work memory in RUN operating mode.

##### Requirements

- The axis technology object has been configured correctly.
- The cause of a pending configuration error requiring acknowledgement has been eliminated (for example, acceleration in positioning axis technology object has been changed to a valid value).

##### Override response

The MC_Reset command cannot be aborted by any other Motion Control command.

The new MC_Reset command does not abort any other active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Restart | INPUT | BOOL | FALSE | (From version V3.0) |  |
| TRUE | Download the axis configuration from the load memory to the work memory. The command can only be executed when the axis is disabled.  Refer to the notes on Download to the CPU. |  |  |  |  |
| FALSE | Acknowledges pending errors |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Error has been acknowledged. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

##### Acknowledging an error requiring acknowledgement with MC_Reset

To acknowledge an error, follow these steps:

1. Check the requirements indicated above.
2. Start the acknowledgement of the error with a rising edge at input parameter "Execute".
3. If output parameter "Done" indicates the value TRUE and tag of technology object <Axis name>.StatusBits.Error the value FALSE, the error has been acknowledged.

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

### MC_Home (S7-1200)

This section contains information on the following topics:

- [MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)

#### MC_Home: Home axis, set home position V1...3 (S7-1200)

##### Description

Motion Control instruction "MC_Home" is used to match the axis coordinates to the real, physical drive position. Homing is required for absolute positioning of the axis. The following types of homing can be executed:

- Active homing (Mode = 3)

  The homing procedure is executed automatically.
- Passive homing (Mode = 2)

  During passive homing, the "MC_Home" Motion Control instruction does not carry out any homing motion. The traversing motion required for this must be implemented by the user via other Motion Control instructions. When the homing switch is detected, the axis is homed.
- Direct homing absolute (Mode = 0)

  The current axis position is set to the value of parameter "Position".
- Direct homing relative (Mode = 1)

  The current axis position is offset by the value of parameter "Position".

##### Requirements

- The axis technology object has been configured correctly.
- The axis is enabled.
- No MC_CommandTable command may be active upon start with Mode = 0, 1, or 2.

##### Override response

The override response depends on the selected mode:

**Mode**
**= 0, 1**

The MC_Home command cannot be aborted by any other Motion Control command.

The MC_Home command does not abort any active Motion Control commands. Position-related motion commands are resumed after homing according to the new homing position (value at input parameter: "Position").

**Mode**
**= 2**

The MC_Home command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 2, 3

The new MC_Home command aborts the following active Motion Control command:

- MC_Home command Mode = 2

Position-related motion commands are resumed after homing according to the new homing position (value at input parameter: "Position").

**Mode**
**= 3**

The MC_Home command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_Home command aborts the following active Motion Control commands:

- MC_Home command Mode = 2, 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Position | INPUT | REAL | 0.0 | - Mode = 0, 2, and 3   Absolute position of axis after completion of the homing operation - Mode = 1   Correction value for the current axis position  Limit values:  -1.0E+12 ≤ Position ≤ 1.0E+12 |  |
| Mode | INPUT | INT | 0 | Homing mode |  |
| 0 | Direct homing absolute  New axis position is the position value of parameter "Position". |  |  |  |  |
| 1 | Direct homing relative  New axis position is the current axis position + position value of parameter "Position". |  |  |  |  |
| 2 | Passive homing  Homing according to the axis configuration. Following homing, the value of parameter "Position" is set as the new axis position. |  |  |  |  |
| 3 | Active homing  Homing procedure in accordance with the axis configuration. Following homing, the value of parameter "Position" is set as the new axis position. |  |  |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Command completed |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

> **Note**
>
> Axis homing is lost under the following conditions:
>
> - Disabling of axis by the "MC_Power" Motion Control instruction
> - Changeover between automatic mode and manual control
> - Upon start of active homing. After successful completion of the homing operation, axis homing is again available.
> - After POWER OFF -> POWER ON of the CPU
> - After CPU restart (RUN-STOP -> STOP-RUN)

##### Homing an axis

To home the axis, follow these stops:

1. Check the requirements indicated above.
2. Initialize the necessary input parameters with values, and start the homing operation with a rising edge at input parameter "Execute"
3. If output parameter "Done" and technology object tag <Axis name>.StatusBits.HomingDone indicate the value TRUE, homing is complete.

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

### MC_Halt (S7-1200)

This section contains information on the following topics:

- [MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
- [MC_Halt: Function chart V1...3 (S7-1200)](#mc_halt-function-chart-v13-s7-1200)

#### MC_Halt: Stop axis V1...3 (S7-1200)

##### Description

The "MC_Halt" Motion Control instruction stops all movements and brings the axis to a standstill with the configured deceleration. The standstill position is not defined.

##### Requirements

- The axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_Halt command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_Halt command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Zero velocity reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_Halt: Function chart V1...3 (S7-1200)](#mc_halt-function-chart-v13-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_Halt: Function chart V1...3 (S7-1200)

##### Function chart

![Function chart](images/88122172043_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 5.0

| Symbol | Meaning |
| --- | --- |
| ① | The axis is braked by an MC_Halt command until it comes to a standstill. The axis standstill is signaled via "Done_2". |
| ② | While an MC_Halt command is braking the axis, this command is aborted by another motion command. The abort is signaled via "Abort_2". |

---

**See also**

[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)

### MC_MoveAbsolute (S7-1200)

This section contains information on the following topics:

- [MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
- [MC_MoveAbsolute: Function chart V1...3 (S7-1200)](#mc_moveabsolute-function-chart-v13-s7-1200)

#### MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)

##### Description

The "MC_MoveAbsolute" Motion Control instruction starts an axis positioning motion to move it to an absolute position.

##### Requirements

- The axis technology object has been configured correctly.
- The axis is enabled.
- The axis is homed.

##### Override response

The MC_MoveAbsolute command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveAbsolute command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Position | INPUT | REAL | 0.0 | Absolute target position  Limit values:   -1.0e<sup>12</sup> ≤ Position ≤ 1.0e<sup>12</sup> |  |
| Velocity | INPUT | REAL | 10.0 | Velocity of axis  This velocity is not always reached on account of the configured acceleration and deceleration and the target position to be approached.  Limit values:  Start/stop velocity ≤ Velocity ≤ maximum velocity |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Absolute target position reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_MoveAbsolute: Function chart V1...3 (S7-1200)](#mc_moveabsolute-function-chart-v13-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_MoveAbsolute: Function chart V1...3 (S7-1200)

##### Function chart

![Function chart](images/59361187339_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| ① | An axis is moved to absolute position 1000.0 with an MC_MoveAbsolute command. When the axis reaches the target position, this is signaled via "Done_1". When "Done_1" = TRUE, another MC_MoveAbsolute command, with target position 1500.0, is started. Because of the response times (e.g., cycle time of user program, etc.), the axis comes to a standstill briefly (see zoomed-in detail). When the axis reaches the new target position, this is signaled via "Done_2". |
| ② | An active MC_MoveAbsolute command is aborted by another MC_MoveAbsolute command. The abort is signaled via "Abort_1". The axis is then moved at the new velocity to the new target position 1500.0. When the new target position is reached, this is signaled via "Done_2". |

---

**See also**

[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)

### MC_MoveRelative (S7-1200)

This section contains information on the following topics:

- [MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
- [MC_MoveRelative: Function chart V1...3 (S7-1200)](#mc_moverelative-function-chart-v13-s7-1200)

#### MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)

##### Description

The "MC_MoveRelative" Motion Control instruction starts a positioning motion relative to the start position.

##### Requirements

- The axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_MoveRelative command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveRelative command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Distance | INPUT | REAL | 0.0 | Travel distance for the positioning operation  Limit values:   -1.0e<sup>12</sup> ≤ Distance  ≤ 1.0e<sup>12</sup> |  |
| Velocity | INPUT | REAL | 10.0 | Velocity of axis  This velocity is not always reached on account of the configured acceleration and deceleration and the distance to be traveled.  Limit values:  Start/stop velocity ≤ Velocity ≤ maximum velocity |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Target position reached |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_MoveRelative: Function chart V1...3 (S7-1200)](#mc_moverelative-function-chart-v13-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_MoveRelative: Function chart V1...3 (S7-1200)

##### Function chart

![Function chart](images/104081658635_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| ① | The axis is moved by an MC_MoveRelative command by the distance ("Distance") 1000.0. When the axis reaches the target position, this is signaled via "Done_1". When "Done_1" = TRUE, another MC_MoveRelative command, with travel distance 500.0, is started. Because of the response times (e.g., cycle time of user program, etc.), the axis comes to a standstill briefly (see zoomed-in detail). When the axis reaches the new target position, this is signaled via "Done_2". |
| ② | An active MC_MoveRelative command is aborted by another MC_MoveRelative command. The abort is signaled via "Abort_1". The axis is then moved at the new velocity by the new distance ("Distance") 500.0. When the new target position is reached, this is signaled via "Done_2". |

---

**See also**

[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)

### MC_MoveVelocity (S7-1200)

This section contains information on the following topics:

- [MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
- [MC_MoveVelocity: Function chart V1...3 (S7-1200)](#mc_movevelocity-function-chart-v13-s7-1200)

#### MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)

##### Description

Motion control instruction "MC_MoveVelocity" moves the axis constantly at the specified velocity.

##### Requirements

- The axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

MC_MoveVelocity can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveVelocity command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |
| Velocity | INPUT | REAL | 10.0 | Velocity specification for axis motion  Limit values:  Start/stop velocity ≤ |Velocity ≤ maximum velocity  (Velocity = 0.0 is permitted) |  |
| Direction | INPUT | INT | 0 | Direction specification |  |
| 0 | Direction of rotation corresponds to the sign of the value in parameter "Velocity" |  |  |  |  |
| 1 | Positive direction of rotation  (The sign of the value in parameter "Velocity" is ignored) |  |  |  |  |
| 2 | Negative direction of rotation  (The sign of the value in parameter "Velocity" is ignored) |  |  |  |  |
| Current | INPUT | BOOL | FALSE | Maintain current velocity |  |
| FALSE | "Maintain current velocity" is deactivated. The values of parameters "Velocity" and "Direction" are used. |  |  |  |  |
| TRUE | "Maintain current velocity" is activated. The values in parameters "Velocity" and "Direction" are not taken into account.  When the axis resumes motion at the current velocity, the "InVelocity" parameter returns the value TRUE. |  |  |  |  |
| InVelocity | OUTPUT | BOOL | FALSE | TRUE | - "Current" = FALSE:   The velocity specified in parameter "Velocity" was reached. - "Current" = TRUE:   The axis travels at the current velocity at the start time. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

##### Behavior with zero setpoint velocity (Velocity = 0.0)

An MC_MoveVelocity command with "Velocity" = 0.0 (such as an MC_Halt command) aborts active motion commands and stops the axis with the configured deceleration.

When the axis comes to a standstill, output parameter "InVelocity" indicates TRUE for at least one program cycle.

"Busy" indicates the value TRUE during the deceleration process and changes to FALSE together with "InVelocity". If parameter "Execute" = TRUE is set, "InVelocity" and "Busy" are latched.

When the "MC_MoveVelocity" command is started, status bit "SpeedCommand" is set in the technology object. Status bit "ConstantVelocity" is set upon axis standstill. Both bits are adapted to the new situation when a new motion command is started.

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_MoveVelocity: Function chart V1...3 (S7-1200)](#mc_movevelocity-function-chart-v13-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_MoveVelocity: Function chart V1...3 (S7-1200)

##### Function chart

![Function chart](images/59361837963_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 10.0

| Symbol | Meaning |
| --- | --- |
| ① | An active MC_MoveVelocity command signals via "InVel_1" that its target velocity has been reached. It is then aborted by another MC_MoveVelocity command. The abort is signaled via "Abort_1". When the new target velocity 15.0 is reached, this is signaled via "InVel_2". The axis then continues moving at the new constant velocity. |
| ② | An active MC_MoveVelocity command is aborted by another MC_MoveVelocity command prior to reaching its target velocity. The abort is signaled via "Abort_1". When the new target velocity 15.0 is reached, this is signaled via "InVel_2". The axis then continues moving at the new constant velocity. |

---

**See also**

[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)

### MC_MoveJog (S7-1200)

This section contains information on the following topics:

- [MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
- [MC_MoveJog: Function chart V1...3 (S7-1200)](#mc_movejog-function-chart-v13-s7-1200)

#### MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)

##### Description

Motion control instruction "MC_MoveJog" moves the axis constantly at the specified velocity in jog mode. You use this Motion Control instruction, for example, for testing and commissioning purposes.

##### Requirements

- The axis technology object has been configured correctly.
- The axis is enabled.

##### Override response

The MC_MoveJog command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_MoveJog command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| JogForward | INPUT | BOOL | FALSE | As long as the parameter is TRUE, the axis moves in the positive direction at the velocity specified in parameter "Velocity". |  |
| JogBackward | INPUT | BOOL | FALSE | As long as the parameter is TRUE, the axis moves in the negative direction at the velocity specified in parameter "Velocity". |  |
| If both parameters are simultaneously TRUE, the axis stops with the configured deceleration. An error is indicated in parameters "Error", "ErrorID", and "ErrorInfo". |  |  |  |  |  |
| Velocity | INPUT | REAL | 10.0 | Preset velocity for jog mode |  |
| Limit values, instruction version V1.0:  Start/stop velocity ≤ |Velocity ≤ maximum velocity |  |  |  |  |  |
| Limits, instruction version V2.0:  Start/stop velocity ≤ velocity ≤ maximum velocity |  |  |  |  |  |
| InVelocity | OUTPUT | BOOL | FALSE | TRUE | The velocity specified in parameter "Velocity" was reached. |
| Busy | OUTPUT | BOOL | FALSE | TRUE | The command is being executed |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | During execution, the command was aborted by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_MoveJog: Function chart V1...3 (S7-1200)](#mc_movejog-function-chart-v13-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_MoveJog: Function chart V1...3 (S7-1200)

##### Function chart

![Function chart](images/59361745419_DV_resource.Stream@PNG-de-DE.png)

The following values were configured in the configuration window **Dynamics > General**:

- Acceleration: 10.0
- Deceleration: 5.0

| Symbol | Meaning |
| --- | --- |
| ① | The axis is moved in the positive direction in jog mode via "Jog_F". When the target velocity 50.0 is reached, this is signaled via "InVelo_1". After " Jog_F" is reset, the axis brakes again until it comes to a standstill. |
| ② | The axis is moved in the negative direction in jog mode via "Jog_B". When the target velocity 50.0 is reached, this is signaled via "InVelo_1". After " Jog_B" is reset, the axis brakes again until it comes to a standstill. |

---

**See also**

[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)

### MC_CommandTable (S7-1200)

This section contains information on the following topics:

- [MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)

#### MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)

##### Description

The Motion Control instruction "MC_CommandTable" combines multiple individual axis control commands in one movement sequence.

##### Requirements

- The axis technology object has been inserted in V2 and correctly configured.
- The command table technology object has been inserted and correctly configured.
- The axis is enabled.

##### Override response

The MC_CommandTable command can be aborted by the following Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The new MC_CommandTable command aborts the following active Motion Control commands:

- MC_Home command Mode = 3
- MC_Halt command
- MC_MoveAbsolute command
- MC_MoveRelative command
- MC_MoveVelocity command
- MC_MoveJog command
- MC_CommandTable command

The active Motion Control command is cancelled by the start of the first "Positioning Relative", "Positioning Absolute", "Velocity set point" or "Halt" command.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |
| CommandTable | INPUT | TO_CommandTable_1 | - | Command table technology object |  |
| Execute | INPUT | BOOL | FALSE | Command table start with positive edge |  |
| StartStep | INPUT | INT | 1 | Defines the step at which the execution of the command table should begin  Limit values:  1 ≤ StartStep ≤ EndStep |  |
| EndStep | INPUT | INT | 32 | Defines the step up to which the execution of command table should take place  Limit values:  StartStep ≤ EndStep ≤ 32 |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | Command table has been successfully executed |
| Busy | OUTPU | BOOL | FALSE | TRUE | The command table is being executed. |
| CommandAborted | OUTPUT | BOOL | FALSE | TRUE | The command table was cancelled by another command. |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command table. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |
| CurrentStep | OUTPUT | INT | 0 | Step in command table currently being executed |  |
| StepCode | OUTPUT | WORD | 16#0000 | User-defined numerical value / bit pattern of the step currently being executed |  |

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

### MC_ChangeDynamic (S7-1200)

This section contains information on the following topics:

- [MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)](#mc_changedynamic-change-dynamic-settings-of-axis-v23-s7-1200)

#### MC_ChangeDynamic: Change dynamic settings of axis V2...3 (S7-1200)

##### Description

Motion Control instruction "MC_ChangeDynamic" allows you to change the following settings of the axis:

- Change the ramp-up time (acceleration) value
- Change the ramp-down time (deceleration) value
- Change the emergency stop ramp-down time (emergency stop deceleration) value
- Change the smoothing time (jerk) value

For the effectiveness of the change, refer to the description of the tag.

##### Requirements

- The axis technology object has been inserted in Version V2.
- The axis technology object has been configured correctly.

##### Override response

A MC_ChangeDynamic command cannot be aborted by any other Motion Control command.

A new MC_ChangeDynamic command does not abort any active Motion Control commands.

##### Parameters

| Parameter | Declaration | Data type | Default value | Description |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Axis | INPUT | TO_Axis_1 | - | Axis technology object |  |  |
| Execute | INPUT | BOOL | FALSE | Start of the command with a positive edge |  |  |
| ChangeRampUp | INPUT | BOOL | FALSE | TRUE |  | Change ramp-up time in line with input parameter "RampUpTime" |
| RampUpTime | INPUT | REAL | 5.00 | Time (in seconds) to accelerate axis from standstill to configured maximum velocity without jerk limit.  The change will influence the tag <Axis name>. Config.DynamicDefaults.Acceleration. For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeRampDown | INPUT | BOOL | FALSE | TRUE |  | Change ramp-down time in line with input parameter "RampDownTime" |
| RampDownTime | INPUT | REAL | 5.00 | Time (in seconds) to decelerate axis from the configured maximum velocity to standstill without jerk limiter.  The change will influence the tag <Axis name>. Config.DynamicDefaults.Deceleration . For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeEmergency | INPUT | BOOL | FALSE | TRUE |  | Change emergency stop ramp-down time in line with input parameter "EmergencyRampTime" |
| EmergencyRampTime | INPUT | REAL | 2.00 | Time (in seconds) to decelerate the axis from configured maximum velocity to standstill without jerk limiter in emergency stop mode.   The change will influence the tag <Axis name>. Config.DynamicDefaults.EmergencyDeceleration . For the effectiveness of the change, refer to the description of this tag. |  |  |
| ChangeJerkTime | INPUT | BOOL | FALSE | TRUE |  | Change smoothing time according to the input parameter "JerkTime" |
| JerkTime | INPUT | REAL | 0.25 | Smoothing time (in seconds) used for the axis acceleration and deceleration ramps  The change will influence the tag <Axis name>. Config.DynamicDefaults.Jerk . For the effectiveness of the change, refer to the description of this tag. |  |  |
| Done | OUTPUT | BOOL | FALSE | TRUE | The changed values have been written to the technology data block. The description of the tags will show when the change becomes effective. |  |
| Error | OUTPUT | BOOL | FALSE | TRUE | An error occurred during execution of the command. The cause of the error can be found in parameters "ErrorID" and "ErrorInfo". |  |
| ErrorID | OUTPUT | WORD | 16#0000 | Error ID for parameter "Error" |  |  |
| ErrorInfo | OUTPUT | WORD | 16#0000 | Error info ID for parameter "ErrorID" |  |  |

> **Note**
>
> At the input parameters "RampUpTime", "RampDownTime", "EmergencyRampTime" and "JerkTime", values can be entered which exceed the admissible limits of the resulting parameters: "Acceleration", "Deceleration", "Emergency stop deceleration" and "Jerk".
>
> Please note the equations and limits in "Axis technology object" -> "Configuring the technology object" -> "Dynamics" and ensure that the values you input are within the valid range.

---

**See also**

[S7-1200 Motion Control V4...5 (S7-1200)](#s7-1200-motion-control-v45-s7-1200)
  
[MC_Power: Enable, disable axis V1...3 (S7-1200)](#mc_power-enable-disable-axis-v13-s7-1200)
  
[MC_Reset: Acknowledge fault, restart technology object V1...3 (S7-1200)](#mc_reset-acknowledge-fault-restart-technology-object-v13-s7-1200)
  
[MC_Home: Home axis, set home position V1...3 (S7-1200)](#mc_home-home-axis-set-home-position-v13-s7-1200)
  
[MC_Halt: Stop axis V1...3 (S7-1200)](#mc_halt-stop-axis-v13-s7-1200)
  
[MC_MoveAbsolute: Absolute positioning of axis V1...3 (S7-1200)](#mc_moveabsolute-absolute-positioning-of-axis-v13-s7-1200)
  
[MC_MoveRelative: Relative positioning of axis V1...3 (S7-1200)](#mc_moverelative-relative-positioning-of-axis-v13-s7-1200)
  
[MC_MoveVelocity: Move axis at set velocity V1...3 (S7-1200)](#mc_movevelocity-move-axis-at-set-velocity-v13-s7-1200)
  
[MC_MoveJog: Move axis in jog mode V1...3 (S7-1200)](#mc_movejog-move-axis-in-jog-mode-v13-s7-1200)
  
[MC_CommandTable: Run axis commands as motion sequence V2...3 (S7-1200)](#mc_commandtable-run-axis-commands-as-motion-sequence-v23-s7-1200)
