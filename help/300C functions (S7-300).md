---
title: "300C functions (S7-300)"
package: ProgTech300C34enUS
topics: 6
devices: [S7-300]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# 300C functions (S7-300)

This section contains information on the following topics:

- [ANALOG: Position with analog output (S7-300)](#analog-position-with-analog-output-s7-300)
- [DIGITAL: Position with digital output (S7-300)](#digital-position-with-digital-output-s7-300)
- [COUNT: Control counter (S7-300)](#count-control-counter-s7-300)
- [FREQUENC: Control frequency measurement (S7-300)](#frequenc-control-frequency-measurement-s7-300)
- [PULSE: Control pulse width modulation (S7-300)](#pulse-control-pulse-width-modulation-s7-300)

## ANALOG: Position with analog output (S7-300)

### Description

You use the ANALOG instruction to control the positioning functions of the user program.

A fixed assigned analog output controls the power section with a voltage (voltage signal) of ±10 V or with a current (current signal) of ±20 mA.

- After the acceleration phase (RAM_UP), the drive approaches the destination at the speed (V<sub>setpoint</sub>).
- At the braking point that is calculated by the CPU, the deceleration (RAMP_DN) to the changeover point is initialized.
- Once the changeover point has been reached, the run will continue at creep speed (V<sub>creep</sub>).
- The drive is switched off at the cut-off point.
- The changeover point and the cut-off point are determined for every target that will be approached in the values you have specified for the changeover difference and cut-off difference parameters. The changeover difference and cut-off difference can be determined differently for forward motion (in plus direction) and for reverse motion (in minus direction).
- Traverse is complete (WORKING = FALSE) when the cut-off point is reached. A new traverse can then be started after this time.
- The specified target has been reached (POS_RCD = TRUE) when the actual position value has reached the target area. If the actual position value again deviates from the target area without a new traverse having been started, the signal "position reached" is not reset.

If the change-over difference is less than the cut-off difference, the drive is slowed linearly to speed setpoint 0 starting at the braking point.

### Basic parameters

The parameters of the instruction that are identical for all modes are described here. The parameters specific to the operating mode are described for the individual operating modes.

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameter

The following table shows the parameters of the instruction ANALOG:

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| LADDR | Input | WORD | 0 | CPU-specific | W#16#0310 | The submodule I/O address, which you have specified during hardware configuration.  If the I and O addresses are not equal, the lesser of the two addresses must be specified. |
| CHANNEL | Input | INT | 2 | 0 | 0 | Channel number |
| STOP | Input | BOOL | 4.4 | TRUE/FALSE | FALSE | Stop traverse  Use STOP = TRUE to stop/interrupt the traverse prematurely. |
| ERR_A | Input | BOOL | 4.5 | TRUE/FALSE | FALSE | Group acknowledgement of external error  External errors are acknowledged with ERR_A = TRUE. |
| SPEED | Input | DINT | 12 | Creep speed to  1 000 000 pulses/s  No higher than the maximum speed that will be assigned in the parameter | 1000 | The axis will be accelerated to the speed "V<sub>setpoint</sub>".  It is not possible to change the speed during traverse. |
| WORKING | Output | BOOL | 16.0 | TRUE/FALSE | FALSE | Traverse in process |
| ACT_POS | Output | DINT | 18 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 22 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |
| ERR | Output | WORD | 24 | Each bit  0 or 1 | 0 | External error:  Bit 2: Zero mark monitoring  Bit 11: Traverse range monitoring (always 1)  Bit 12: Work range monitoring  Bit 13: Process value monitoring  Bit 14: Destination run-up monitoring  Bit 15: Destination area monitoring  Remaining bits reserved |
| ST_ENBLD | Output | BOOL | 26.0 | TRUE/FALSE | TRUE | The CPU sets start enable if all the following conditions apply:  - STOP is not active (STOP = FALSE) - No external error pending (ERR = 0) - Drive enable is set (DRV_EN = TRUE) - Positioning not in process (WORKING = FALSE) |
| ERROR | Output | BOOL | 26.1 | TRUE/FALSE | FALSE | Error when starting /resuming a traverse |
| STATUS | Output | WORD | 28.0 | W#16#0000 to W#16#FFFF | W#16#0000 | Error number |

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| ACCEL | STATIC | DINT | 30 | 1 to 100 000 pulses/s<sup>2</sup> | 100 | Acceleration  Change during traverse not possible. |
| DECEL | STATIC | DINT | 34 | 1 to 100 000 pulses/s<sup>2</sup> | 100 | Deceleration  Change during traverse not possible. |
| CHGDIFF_P | STATIC | DINT | 38 | 0 to +10<sup>8 </sup>pulses | 1000 | Changeover difference plus:  "Changeover difference plus" defines the changeover point from which the drive continues forward traverse in creep speed. |
| CUTOFF- DIFF_P | STATIC | DINT | 42 | 0 to +10<sup>8 </sup>pulses | 100 | Cut-off difference plus:  "Cut-off difference plus" defines the cut-off point at which the drive is shut off from creep speed in the forward direction. |
| CHGDIFF_M | STATIC | DINT | 46 | 0 to +10<sup>8 </sup>pulses | 1000 | Changeover difference minus:  "Changeover difference minus" defines the changeover point from which the drive continues in reverse motion at creep speed. |
| CUTOFF- DIFF_M | STATIC | DINT | 50 | 0 to +10<sup>8 </sup>pulses | 100 | Cut-off difference minus:  "Cut-off difference minus" defines the point at which the drive is switched out of creep speed in the reverse direction. |
| PARA | STATIC | BOOL | 54.0 | TRUE/FALSE | FALSE | Parameters have been assigned to the axis |
| DIR | STATIC | BOOL | 54.1 | TRUE/FALSE | FALSE | Actual/last direction of movement  FALSE = forward (in plus direction)  TRUE = reverse (in minus direction) |
| CUTOFF | STATIC | BOOL | 54.2 | TRUE/FALSE | FALSE | Drive in cut-off area (from the cut-off point to the start of the next run) |
| CHGOVER | STATIC | BOOL | 54.3 | TRUE/FALSE | FALSE | Drive in changeover range (from reaching creep speed to start of next traverse) |
| RAMP_DN | STATIC | BOOL | 54.4 | TRUE/FALSE | FALSE | The drive is decelerated (from braking point to changeover point) |
| RAMP_UP | STATIC | BOOL | 54.5 | TRUE/FALSE | FALSE | The drive is accelerated (from start until it reaches the speed SPEED (V<sub>setpoint</sub>)) |
| DIST_TO_  GO | STATIC | DINT | 56 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual residual distance |
| LAST_TRG | STATIC | DINT | 60 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Last/current target  - Absolute incremental mode:   At start of traverse LST_TRG = current absolute target (TARGET). - Relative incremental mode:   At start of traverse LST_TRG = LAST_TRG is the specified +/- distance of the previous traverse (TARGET). |

### Parameters for "jog" mode

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Jog in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Jog in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 1 = jog |
| WORKING | Output | BOOL | 16.0 | TRUE/FALSE | FALSE | Traverse in process |
| ACT_POS | Output | DINT | 18 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 22 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for "search for reference" mode

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Search for reference in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Search for reference in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 3 = "search for reference" |
| WORKING | Output | BOOL | 16.0 | TRUE/FALSE | FALSE | Traverse in process |
| SYNC | Output | BOOL | 16.3 | TRUE/FALSE | FALSE | SYNC = TRUE: Axis is synchronized |
| ACT_POS | Output | DINT | 18 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 22 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for "relative incremental mode"

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Traverse in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Traverse in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 4 = relative incremental mode |
| TARGET | Input | DINT | 8 | 0 to 10<sup>9</sup> pulses | 1000 | Distance in pulses (only positive values allowed) |
| WORKING | Output | BOOL | 16.0 | TRUE/FALSE | FALSE | Traverse in process |
| POS_RCD | Output | BOOL | 16.1 | TRUE/FALSE | FALSE | Position reached |
| ACT_POS | Output | DINT | 18 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 22 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for "absolute incremental mode"

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| START | Input | BOOL | 4.1 | TRUE/FALSE | FALSE | Start traverse (positive edge) |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Traverse in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Traverse in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 5 = absolute incremental mode |
| TARGET | Input | DINT | 8 | Linear axis :  -5x10<sup>8</sup> to +5x10<sup>8</sup>  Rotary axis:  0 to rotary axis end -1 | 1000 | Target in pulses |
| WORKING | Output | BOOL | 16.0 | TRUE/FALSE | FALSE | Traverse in process |
| POS_RCD | Output | BOOL | 16.1 | TRUE/FALSE | FALSE | Position reached |
| ACT_POS | Output | DINT | 18 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 22 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for the job "set reference point"

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| SYNC | Output | BOOL | 16.3 | TRUE/FALSE | FALSE | Axis is synchronized |

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| JOB_REQ | STATIC | BOOL | 76.0 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_DONE | STATIC | BOOL | 76.1 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | STATIC | BOOL | 76.2 | TRUE/FALSE | FALSE | Faulty job |
| JOB_ID | STATIC | INT | 78 | 1, 2 | 0 | Job, 1 = "set reference point" |
| JOB_STAT | STATIC | WORD | 80 | W#16#0000 to W#16#FFFF | W#16#0000 | Job error number |
| JOB_VAL | STATIC | DINT | 82 | 5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Job parameter for reference point coordinates |

### Parameters for the job "delete residual distance"

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| JOB_REQ | STATIC | BOOL | 76.0 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_DONE | STATIC | BOOL | 76.1 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | STATIC | BOOL | 76.2 | TRUE/FALSE | FALSE | Faulty job |
| JOB_ID | STATIC | INT | 78 | 1, 2 | 0 | Job, 2 = "delete residual distance" |
| JOB_STAT | STATIC | WORD | 80 | W#16#0000 to W#16#FFFF | W#16#0000 | Job error number |
| JOB_VAL | STATIC | DINT | 82 | - | 0 | Any setting |

### Parameters for the "length measurement" function

This operation is started at the positive edge on the digital input. There are no specific input parameters.

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| MSR_DONE | OUT | BOOL | 16.2 | TRUE/FALSE | FALSE | Length measurement complete |

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| BEG_VAL | STATIC | DINT | 64 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value start of length measurement |
| END_VAL | STATIC | DINT | 68 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value  length measurement end |
| LEN_VAL | STATIC | DINT | 72 | 0 to 10<sup>9</sup> pulses | 0 | Measured length |

### Parameter ERROR and STATUS

**Operating mode error (**
**ERROR**
 **=** 
**TRUE**
**)**

The output parameter ERROR is set to TRUE if an error is detected. The parameter STATUS shows the cause of the error.

| Event class error code | Description |
| --- | --- |
| W#16#2002 | Incorrect instruction, use ANALOG |
| W#16#2004 | Incorrect channel number (CHANNEL). Set channel number "0". |
| W#16#3001 | Traverse job rejected because of job error in the same call. Correct the respective JOB parameters. |
| W#16#3002 | A change of Output _IN is not permitted while the drive is still running. Wait for the end of the current positioning. |
| W#16#3003 | Unknown operating mode (MODE_IN). Permitted are 1 (jog), 3 (search for reference), 4 (relative incremental mode) and 5 (absolute incremental mode). |
| W#16#3004 | Only one start request is allowed at a time. Valid start requests are DIR_P, DIR_M or START. |
| W#16#3005 | START is only permitted in operating mode "absolute incremental mode”. Start the traverse with DIR_P or DIR_M. |
| W#16#3006 | DIR_P and DIR_M are not permitted for linear axis and "absolute incremental mode". Start the traverse with START. |
| W#16#3007 | Axis not synchronized. "Absolute incremental mode" is only possible with a synchronized axis. |
| W#16#3008 | Leave work area. Return traverse to work area is only allowed in jog mode. |
| W#16#3101 | Start is not enabled because parameters have not been assigned for the axis. Assign parameters for the "positioning" submodule via HW Config. |
| W#16#3102 | Start not enabled because drive enable is not set Set the "drive enable" on the instruction (DRV_EN=TRUE). |
| W#16#3103 | Start not enabled because STOP is set. Delete STOP on the instruction (STOP=FALSE) |
| W#16#3104 | Start is not enabled because the axis is currently positioning (WORKING=TRUE). Wait for the end of the current positioning. |
| W#16#3105 | Start not enabled because at least one error that is pending has not been acknowledged. First, eliminate and clear all external errors and then restart traverse. |
| W#16#3202 | Wrong SPEED default. The speed default is out of the permitted creep speed range of up to 1000000 pulses/s, though not higher than the parameter-assigned maximum speed. |
| W#16#3203 | The acceleration default in ACCEL is outside the permitted range of 1 to 100,000 pulses/s<sup>2</sup>. |
| W#16#3204 | The deceleration default in DECEL is outside the permitted range of 1 to 100,000 pulses/s<sup>2</sup>. |
| W#16#3206 | The speed default in SPEED must be greater than or equal to the assigned referencing frequency parameter. |
| W#16#3301 | Changeover/cut-off difference is too high. Set a maximum changeover/cut-off difference of 10<sup>8</sup>. |
| W#16#3304 | Cut-off difference too low. The cut-off difference must be at least half the value of the target range. |
| W#16#3305 | Changeover difference too low. The changeover difference must be at least half the value of the target range. |
| W#16#3401 | Target default outside of work range. For a linear axis and absolute incremental mode the target default must be within the range of the software limit switches (inclusive). |
| W#16#3402 | Wrong target default. For a rotary axis the target default must be greater than 0 and less than the rotary axis end value. |
| W#16#3403 | Wrong distance specification. The traverse distance for relative incremental mode must be positive. |
| W#16#3404 | Wrong distance specification. The resulting absolute target coordinate must be greater than -5x10<sup>8</sup>. |
| W#16#3405 | Wrong distance specification. The resulting absolute target coordinate must be greater than -5x10<sup>8</sup>. |
| W#16#3406 | Wrong distance specification. The resulting absolute target coordinate must be within the work range (+/‑ half of the target range). |
| W#16#3501 | Travel range too great. Target coordinate + actual residual distance must be greater than or equal to -5x10<sup>8</sup>. |
| W#16#3502 | Travel range too great. Target coordinate + actual residual distance must be less than or equal to 5x10<sup>8</sup>. |
| W#16#3503 | Traverse distance insufficient. Traverse distance in plus direction must be greater than the specified cut-off difference for direction plus. |
| W#16#3504 | Traverse distance insufficient. The traverse distance in minus direction must be greater than the specified cut-off difference for the minus direction |
| W#16#3505 | Traverse distance insufficient or the limit switch is already overtraveled in plus direction. The last approachable target in plus direction (work range or traverse range limit) is too close to the current position. |
| W#16#3506 | Traverse distance insufficient, or the limit switch is already overtraveled in the minus direction. The last approachable target in the minus direction (work range or traverse range limit) is too close to the current position. |

### Job error (JOB_ERR = TRUE)

The output parameter JOB_ERR is set to TRUE if an error is detected. The parameter JOB_STAT shows the cause of the error.

| Event class error code | Description |
| --- | --- |
| W#16#4001 | Parameters not assigned for axis. Assign parameters for the "positioning" submodule via HW Config. |
| W#16#4002 | Job not possible because positioning is in progress. Wait until WORKING = FALSE, then repeat the job. |
| W#16#4004 | Unknown job. Check the job ID and then repeat the job. |
| W#16#4101 | For a linear axis the reference point coordinate should not be outside of the work area limits. |
| W#16#4102 | For a linear axis the specified reference point coordinate + actual residual distance must be greater than or equal to -5x10<sup>8</sup>. |
| W#16#4103 | For a linear axis the specified reference point coordinate + actual residual distance must be greater than or equal to 5x10<sup>8</sup>. |
| W#16#4104 | For a linear axis the specified reference point coordinate + actual difference to the starting point of traverse must be greater than or equal to -5x10<sup>8</sup>. |
| W#16#4105 | For a linear axis the specified reference point coordinate + actual difference to the starting point of traverse must be less than or equal to 5x10<sup>8</sup>. |
| W#16#4106 | For a rotary axis the reference point coordinate should not be lower than 0 and greater than or equal to the rotary axis end. |

### External error (ERR)

The technology monitors traverse, traverse range, and the connected peripheral devices. The prerequisite is that you have switched on monitoring in the "Drive", "Axis" and "Encoder" parameter screen forms beforehand.

An external fault is reported when the monitoring unit is tripped. External errors can occur at anytime regardless of the started functions. You must always acknowledge external errors with ERR_A = TRUE.

External errors are indicated by a set bit in parameter ERR (WORD).

| Monitoring | Error code | Bit in ERR-WORD |
| --- | --- | --- |
| Missing pulse (zero mark) | W#16#0004 | 2 |
| Traverse range | W#16#0800 | 11 |
| Work range | W#16#1000 | 12 |
| Process value | W#16#2000 | 13 |
| Destination run-up | W#16#4000 | 14 |
| Target range | W#16#8000 | 15 |

### System error

A system error is indicated with BIE (binary result) = FALSE. A system error is triggered by errors while reading/writing the instance DB or by multiple calls of the instruction.

## DIGITAL: Position with digital output (S7-300)

### Description

You use the DIGITAL instruction to control the positioning functions of the user program.

Four 24 V digital outputs are permanently assigned to the drive and control the power stage (you can find additional information in the documentation for the hardware used). Depending on the trigger mode, the digital outputs control the direction and speed levels (rapid/creep speed).

The distance is measured via an asymmetrical 24 V incremental transducer with two out-of-phase signals at 90 degrees.

- First, the target is approached with the speed (V<sub>rapid</sub>).
- At the changeover point, the system switches to creep speed (V<sub>creep</sub>).
- The drive is switched off at the cut-off point.
- You can set the changeover point and cut-off point with the parameter values CHGDIFF_P/M and CUTOFFDIFF_P/M. The changeover difference and cut-off difference can be defined differently for forward motion (in plus direction) and for reverse motion (in minus direction).
- Traverse is complete (WORKING = FALSE) when the cut-off point is reached. A new traverse can then be started after this time.
- The specified target has been reached (POS_RCD = TRUE) when the actual position value has reached the target area. If the actual position value again deviates from the target area without a new traverse having been started, the signal "position reached" is not reset.

### Basic parameters:

The parameters of the instruction that are identical for all modes are described here. The parameters specific to the operating mode are described for the individual operating modes.

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| LADDR | Input | WORD | 0 | CPU-specific | W#16#0310 | The submodule I/O address, which you have specified during hardware configuration.  If the I and O addresses are not equal, the lesser of the two addresses must be specified. |
| CHANNEL | Input | INT | 2 | 0 | 0 | Channel number |
| STOP | Input | BOOL | 4.4 | TRUE/FALSE | FALSE | Stop traverse  Use STOP = TRUE to stop/interrupt the traverse prematurely. |
| ERR_A | Input | BOOL | 4.5 | TRUE/FALSE | FALSE | Group acknowledgement of external error  External errors are acknowledged with ERR_A = TRUE. |
| SPEED | Input | BOOL | 12.0 | TRUE/FALSE | FALSE | Two speed stages for rapid traverse/creep speed  TRUE = rapid traverse FALSE= creep speed |
| WORKING | Output | BOOL | 14.0 | TRUE/FALSE | FALSE | Traverse in process |
| ACT_POS | Output | DINT | 16 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 20 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |
| ERR | Output | WORD | 22 | Each bit  0 or 1 | 0 | External error  - Bit2: Zero mark monitoring - Bit11: Traverse range monitoring (always 1) - Bit12: Work range monitoring - Bit13: Process value monitoring - Bit14: Target area monitoring - Bit15: Target area monitoring Remaining bits reserved |
| ST_ENBLD | Output | BOOL | 24.0 | TRUE/FALSE | TRUE | The CPU sets start enable if all the following conditions apply:  - STOP is not active (STOP = FALSE) - No external error pending (ERR = 0) - Drive enable is set (DRV_EN = TRUE) - Positioning not in process (WORKING = FALSE) |
| ERROR | Output | BOOL | 24.1 | TRUE/FALSE | FALSE | Error when starting /resuming a traverse |
| STATUS | Output | WORD | 26.0 | W#16#0000 to W#16#FFFF | W#16#0000 | Error number |

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| CHGDIFF_P | STATIC | DINT | 28 | 0 to +10<sup>8</sup>pulses | 1000 | Changeover difference plus:  "Changeover difference plus" defines the point at which the drive continues its forward traverse with creep speed. |
| CUTOFF- DIFF_P | STATIC | DINT | 32 | 0 to +10<sup>8</sup> pulses | 100 | Cut-off difference plus:  "Cut-off difference plus" defines the cut-off point at which the drive is shut off from creep speed in the forward direction. |
| CHGDIFF_M | STATIC | DINT | 36 | 0 to +10<sup>8</sup> pulses | 1000 | Changeover difference minus:  "Changeover difference minus" defines the point at which the drive changes over from rapid traverse to creep speed in the reverse direction. |
| CUTOFF- DIFF_M | STATIC | DINT | 40 | 0 to +10<sup>8</sup> pulses | 100 | Cut-off difference minus:  "Cut-off difference minus" defines the point at which the drive is switched out of creep speed in the reverse direction. |
| PARA | STATIC | BOOL | 44.0 | TRUE/FALSE | FALSE | Parameters have been assigned to the axis |
| DIR | STATIC | BOOL | 44.1 | TRUE/FALSE | FALSE | Actual/last direction of movement  FALSE = forward (in plus direction)  TRUE = reverse (in minus direction) |
| CUTOFF | STATIC | BOOL | 44.2 | TRUE/FALSE | FALSE | Drive in cut-off area (from the cut-off point to the start of the next run) |
| CHGOVER | STATIC | BOOL | 44.3 | TRUE/FALSE | FALSE | Drive in changeover range (from reaching creep speed to start of the next traverse) |
| DIST_TO_GO | STATIC | DINT | 46 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual residual distance |
| LAST_TRG | STATIC | DINT | 50 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Last/current target  - Absolute incremental mode: At start of traverse LST_TRG = current absolute target (TARGET). - Relative incremental mode: At start of traverse LST_TRG = LAST_TRG is the specified +/- distance of the previous traverse (TARGET). |

### Parameters for "jog" mode

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Jog in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Jog in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 1 = jog |
| WORKING | Output | BOOL | 14.0 | TRUE/FALSE | FALSE | Traverse in process |
| ACT_POS | Output | DINT | 16 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 20 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for "search for reference" mode

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Search for reference in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Search for reference in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 3 = "search for reference" |
| WORKING | Output | BOOL | 14.0 | TRUE/FALSE | FALSE | Traverse in process |
| SYNC | Output | BOOL | 14.3 | TRUE/FALSE | FALSE | SYNC = TRUE: Axis is synchronized |
| ACT_POS | Output | DINT | 16 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 20 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for "relative incremental mode"

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Traverse in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Traverse in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 4 = relative incremental mode |
| TARGET | Input | DINT | 8 | 0 to 10<sup>9</sup>  Pulse | 1000 | Distance in pulses (only positive values allowed) |
| WORKING | Output | BOOL | 14.0 | TRUE/FALSE | FALSE | Traverse in process |
| POS_RCD | Output | BOOL | 14.1 | TRUE/FALSE | FALSE | Position reached |
| ACT_POS | Output | DINT | 16 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 20 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for "absolute incremental mode"

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DRV_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Drive enable |
| START | Input | BOOL | 4.1 | TRUE/FALSE | FALSE | Start traverse (positive edge) |
| DIR_P | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Traverse in plus direction (positive edge) |
| DIR_M | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Traverse in minus direction (positive edge) |
| MODE_IN | Input | INT | 6 | 0, 1, 3, 4, 5 | 1 | Operating mode, 5 = absolute incremental mode |
| TARGET | Input | DINT | 8 | Linear axis :  -5x10<sup>8</sup> to +5x10<sup>8</sup>  Rotary axis:  0 to rotary axis end -1 | 1000 | Target in pulses |
| WORKING | Output | BOOL | 14.0 | TRUE/FALSE | FALSE | Traverse in process |
| POS_RCD | Output | BOOL | 14.1 | TRUE/FALSE | FALSE | Position reached |
| ACT_POS | Output | DINT | 16 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value |
| MODE_OUT | Output | INT | 20 | 0, 1, 3, 4, 5 | 0 | Active/set operating mode |

### Parameters for the job "set reference point"

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| SYNC | Output | BOOL | 14.3 | TRUE/FALSE | FALSE | Axis is synchronized |

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| JOB_REQ | STATIC | BOOL | 66.0 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_DONE | STATIC | BOOL | 66.1 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | STATIC | BOOL | 66.2 | TRUE/FALSE | FALSE | Faulty job |
| JOB_ID | STATIC | INT | 68 | 1, 2 | 0 | Job, 1 = "set reference point" |
| JOB_STAT | STATIC | WORD | 70 | W#16#0000 to W#16#FFFF | W#16#0000 | Job error number |
| JOB_VAL | STATIC | DINT | 72 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Job parameter for reference point coordinates |

### Parameters for the job "delete residual distance"

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| JOB_REQ | STATIC | BOOL | 66.0 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_DONE | STATIC | BOOL | 66.1 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | STATIC | BOOL | 66.2 | TRUE/FALSE | FALSE | Faulty job |
| JOB_ID | STATIC | INT | 68 | 1, 2 | 0 | Job, 2 = "delete residual distance" |
| JOB_STAT | STATIC | WORD | 70 | 0 to FFFF hex | 0 | Job error number |
| JOB_VAL | STATIC | DINT | 72 | - | 0 | None |

### Parameters for the "length measurement" function

This operation is started at the positive edge on the digital input. There are no specific input parameters.

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| MSR_DONE | Output | BOOL | 14.2 | TRUE/FALSE | FALSE | Length measurement complete |

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| BEG_VAL | STATIC | DINT | 54 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value start of length measurement |
| END_VAL | STATIC | DINT | 58 | -5x10<sup>8</sup> to +5x10<sup>8</sup> pulses | 0 | Actual position value  length measurement end |
| LEN_VAL | STATIC | DINT | 62 | 0 to 10<sup>9</sup>pulses | 0 | Measured length |

### Parameter ERROR and STATUS

The output parameter ERROR is set to TRUE if an error is detected. The parameter STATUS shows the cause of the error.

| STATUS Error code | Description |
| --- | --- |
| W#16#2001 | Incorrect instruction, use DIGITAL instruction. |
| W#16#2004 | Incorrect channel number (CHANNEL). Set channel number "0". |
| W#16#3001 | Traverse job rejected because of job error in the same call. Correct the respective JOB parameters. |
| W#16#3002 | A change of MODE_IN is not permitted while the drive is still running. Wait for the end of the current positioning. |
| W#16#3003 | Unknown operating mode (MODE_IN). Permitted are 1 (jog), 3 (search for reference), 4 (relative incremental mode) and 5 (absolute incremental mode). |
| W#16#3004 | Only one start request is allowed at a time. Valid start requests are DIR_P, DIR_M or START. |
| W#16#3005 | START is only permitted in operating mode "absolute incremental mode”. Start the traverse with DIR_P or DIR_M. |
| W#16#3006 | DIR_P and DIR_M are not permitted for linear axis and "absolute incremental mode". Start the traverse with START. |
| W#16#3007 | Axis not synchronized. "Absolute incremental mode" is only possible with a synchronized axis. |
| W#16#3008 | Leave work area. Return traverse to work area is only allowed in jog mode. |
| W#16#3101 | Start is not enabled because parameters have not been assigned for the axis. Assign parameters for the "positioning" submodule via the hardware configuration. |
| W#16#3102 | Start not enabled because drive enable is not set Set the "drive enable" on the instruction (DRV_EN=TRUE). |
| W#16#3103 | Start not enabled because STOP is set. Delete STOP on the instruction (STOP = FALSE). |
| W#16#3104 | Start is not enabled because the axis is currently positioning (WORKING=TRUE). Wait for the end of the current positioning. |
| W#16#3105 | Start not enabled because at least one error that is pending has not been acknowledged. First, eliminate and clear all external errors and then restart traverse. |
| W#16#3201 | Wrong SPEED default. For positioning with digital outputs only "creep speed" (0) and "rapid traverse" (1) are allowed. |
| W#16#3301 | Changeover/cut-off difference is too high. Set a maximum changeover/cut-off difference of 10<sup>8</sup>. |
| W#16#3303 | Changeover difference too low. The changeover difference must be greater than or equal to the cut-off difference. |
| W#16#3304 | Cut-off difference too low. The cut-off difference must be at least half the value of the target range. |
| W#16#3401 | Target default outside of work range. For a linear axis and absolute incremental mode the target default must be within the range of the software limit switches (inclusive). |
| W#16#3402 | Wrong target default. For a rotary axis the target default must be greater than "0" and less than the rotary axis end value. |
| W#16#3403 | Wrong distance specification. The traverse distance for relative incremental mode must be positive. |
| W#16#3404 | Wrong distance specification. The resulting absolute target coordinate must be greater than -5x10<sup>8</sup>. |
| W#16#3405 | Wrong distance specification. The resulting absolute target coordinate must be greater than -5x10<sup>8</sup>. |
| W#16#3406 | Wrong distance specification. The resulting absolute target coordinate must be within the work range (+/‑ half of the target range). |
| W#16#3501 | Traverse distance too great. Target coordinate + actual residual distance must be greater than or equal to -5x10<sup>8</sup>. |
| W#16#3502 | Traverse distance too great. Target coordinate + actual residual distance must be less than or equal to 5x10<sup>8</sup>. |
| W#16#3503 | Traverse distance insufficient. Traverse distance in plus direction must be greater than the specified cut-off difference for plus direction. |
| W#16#3504 | Traverse distance insufficient. The traverse distance in minus direction must be greater than the specified cut-off difference for the minus direction. |
| W#16#3505 | Traverse distance insufficient or the limit switch is already overtraveled in plus direction. The last approachable target in plus direction (work range or traverse distance limit) is too close to the current position. |
| W#16#3506 | Traverse distance insufficient, or the limit switch is already overtraveled in the minus direction. The last approachable target in minus direction (work range or traverse distance limit) is too close to the current position. |

### Job error (JOB_ERR = TRUE)

The parameter JOB_ERR is set to TRUE if an error is detected. The parameter JOB_STAT shows the cause of the error.

| Event class error code | Description |
| --- | --- |
| W#16#4001 | Parameters not assigned for axis. Assign parameters for the "positioning" submodule via the hardware configuration. |
| W#16#4002 | Job not possible because positioning is in progress. Jobs can only be carried out if positioning is not in progress. Wait until WORKING = FALSE, then repeat the job. |
| W#16#4004 | Unknown job. Check the job ID and then repeat the job. |
| W#16#4101 | For a linear axis the reference point coordinate should not be outside of the work area limits. |
| W#16#4102 | For a linear axis the specified reference point coordinate + actual residual distance must be greater than or equal to -5x10<sup>8</sup>. |
| W#16#4103 | For a linear axis the specified reference point coordinate + actual residual distance must be greater than or equal to 5x10<sup>8</sup>. |
| W#16#4104 | For a linear axis the specified reference point coordinate + actual difference to the starting point of traverse must be greater than or equal to -5x10<sup>8</sup>. |
| W#16#4105 | For a linear axis the specified reference point coordinate + actual difference to the starting point of traverse must be less than or equal to 5x10<sup>8</sup>. |
| W#16#4106 | For a rotary axis the reference point coordinate should not be lower than 0 and greater than or equal to the rotary axis end. |

### External error (ERR)

The technology monitors traverse, traverse range, and the connected peripheral devices. The prerequisite is that you have switched on monitoring in the "Drive", "Axis" and "Encoder" parameter screen forms beforehand.

An external fault is reported when the monitoring unit is tripped. External errors can occur at anytime regardless of the started functions. You must always acknowledge external errors with ERR_A = TRUE.

External errors are indicated by a set bit in parameter ERR (WORD).

| Monitoring | Error code | Bit in ERR-WORD |
| --- | --- | --- |
| **Missing pulse (zero mark)** | W#16#0004 | 2 |
| **Traverse range** | W#16#0800 | 11 |
| **Work range** | W#16#1000 | 12 |
| **Process value** | W#16#2000 | 13 |
| **Destination run-up** | W#16#4000 | 14 |
| **Target range** | W#16#8000 | 15 |

### System error

A system error is indicated with BIE (binary result) = FALSE. A system error is triggered by errors while reading/writing the instance DB or by multiple calls of the instruction.

## COUNT: Control counter (S7-300)

### Description

You use the "COUNT" instruction to control the counter from the user program.

The following functionality is available:

- Starting/stopping the counter via the software gate SW_GATE
- Enabling/controlling the output DO
- Retrieving status bits STS_CMP, STS_OFLW, STS_UFLW and STS_ZP
- Retrieving the current counter value COUNTVAL
- Jobs for reading/writing the internal counter registers
- Retrieving the current period duration TIMEVAL

### Parameter

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| LADDR | Input | WORD | 0 | CPU-specific | W#16#0300 | The submodule I/O address, which you have specified during hardware configuration.  If the I and O addresses are not equal, the lesser of the two addresses must be specified. |
| CHANNEL | Input | INT | 2 | CPU 312C: 0 to 1  CPU 313C: 0 to 2  CPU 314C: 0 to 3 | 0 | Channel number |
| SW_GATE | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Software gate for starting/stopping the counter |
| CTRL_DO | Input | BOOL | 4.1 | TRUE/FALSE | FALSE | Enable output |
| SET_DO | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Control output |
| JOB_REQ | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_ID | Input | WORD | 6 | W#16#0000  Job without function  W#16#0001  Write count value  W#16#0002  Write load value  W#16#0004  Write comparison value  W#16#0008  Write hysteresis  W#16#0010  Write pulse duration  W#16#0082  Read load value  W#16#0084  Read comparison value  W#16#0088  Read hysteresis   W#16#0090 Read pulse duration | W#16#0000 | Job number |
| JOB_VAL | Input | DINT | 8 | -2<sup>31</sup> to  +2<sup>31</sup> -1 | 0 | Value for write jobs. |
| STS_GATE | Output | BOOL | 12.0 | TRUE/FALSE | FALSE | Status of the internal gate |
| STS_STRT | Output | BOOL | 12.1 | TRUE/FALSE | FALSE | Status of the hardware gate (start input) |
| STS_LTCH | Output | BOOL | 12.2 | TRUE/FALSE | FALSE | Status of the latch input |
| STS_DO | Output | BOOL | 12.3 | TRUE/FALSE | FALSE | Output status |
| STS_C_DN | Output | BOOL | 12.4 | TRUE/FALSE | FALSE | Status reverse direction.   The last count direction is always displayed. The value of STS_C_DN is FALSE after the first call of the instruction. |
| STS_C_UP | Output | BOOL | 12.5 | TRUE/FALSE | FALSE | Status forward direction  The last count direction is always displayed. The value of STS_C_UP is TRUE after the first call of the instruction. |
| COUNTVAL | Output | DINT | 14 | -2<sup>31</sup> to  +2<sup>31</sup> -1 | 0 | Actual count value |
| LATCHVAL | Output | DINT | 18 | -2<sup>31</sup> to  +2<sup>31</sup> -1 | 0 | Actual latch value |
| JOB_DONE | Output | BOOL | 22.0 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | Output | BOOL | 22.1 | TRUE/FALSE | FALSE | Faulty job |
| JOB_STAT | Output | WORD | 24 | 0 to W#16#FFFF | 0 | Job error number |
|  |  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> If you have set the parameter "response of the output" to "no comparison" via the configuration interface, the following is valid:
>
> - The output will be switched in the same manner that a normal output is switched.
> - The input parameters CTRL_DO and SET_DO are not active.
> - The status bits STS_DO and STS_CMP (status comparator in the IDB) remain reset.

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| STS_CMP | STATIC | BOOL | 26.3 | TRUE/FALSE | FALSE | Status comparator.   Reset with RES_STS.  The status bit STS_CMP indicates that the conditions for comparison of the comparator are satisfied or have been satisfied.  STS_CMP also indicates that the output was set (STS_DO = TRUE). |
| STS_OFLW | STATIC | BOOL | 26.5 | TRUE/FALSE | FALSE | Status overflow  Reset with RES_STS. |
| STS_UFLW | STATIC | BOOL | 26.6 | TRUE/FALSE | FALSE | Status underflow  Reset with RES_STS. |
| STS_ZP | STATIC | BOOL | 26.7 | TRUE/FALSE | FALSE | Status zero-crossing  Reset with RES_STS.  Only set for counters without main count direction.   Indicates the zero crossing. Is also set when the counter is set to 0 or if the counter starts counting as of load value=0. |
| JOB_OVAL | STATIC | DINT | 28 | -2<sup>31</sup> to  +2<sup>31</sup> -1 | 0 | Output value for read jobs. |
| RES_STS | STATIC | BOOL | 32.2 | TRUE/FALSE | FALSE | Reset status bits.  Resets the status bits STS_CMP, STS_OFLW, STS_UFLW and STS_ZP. Two calls of the instruction are required to reset the status bits. |

### Parameter JOB_ERR and JOB_STAT

JOB_ERR = TRUE if a job error occurs. The precise error cause is displayed in JOB_STAT.

| Event class error code | Description |
| --- | --- |
| W#16#0121 | Compare value too low. |
| W#16#0122 | Compare value too great. |
| W#16#0131 | Hysteresis too small. |
| W#16#0132 | Hysteresis too great. |
| W#16#0141 | Pulse duration too low. |
| W#16#0142 | Pulse duration too great. |
| W#16#0151 | Load value too low. |
| W#16#0152 | Load value too high. |
| W#16#0161 | Counter value too low. |
| W#16#0162 | Counter value too high. |
| W#16#01FF | Invalid job number. |

### System error

If a system error occurs, BIE (binary result) = FALSE.

| Event class error code | Description |
| --- | --- |
| W#16#8001 | Wrong operating mode or faulty parameters. Set the correct operating mode during hardware configuration or use the instruction that matches the set operating mode. |
| W#16#8009 | Invalid channel number. Set a channel number ≤ 3 (CPU-specific value). |

## FREQUENC: Control frequency measurement (S7-300)

### Description

You use the "FREQUENC" instruction to operate the frequency meter of the user program.

The following functionality is available:

- Starting/stopping via the software gate SW_GATE
- Enabling/controlling the output DO
- Retrieving the status bits STS_CMP, STS_OFLW and STS_UFLW
- Retrieving the current frequency value MEAS_VAL
- Jobs for reading/writing the internal frequency counter registers

### Parameter

| Parameter | Declaration | Data type | Address (instance  DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| LADDR | Input | WORD | 0 | CPU-specific | W#16#0300 | The submodule I/O address, which you have specified during hardware configuration.  If the I and O addresses are not equal, the lesser of the two addresses must be specified. |
| CHANNEL | Input | INT | 2 | CPU 312C:  0 to 1 CPU 313C: 0 to 2 CPU 314C: 0 to 3 | 0 | Channel number |
| SW_GATE | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Software gate for starting/stopping the frequency measurement |
| MAN_DO | Input | BOOL | 4.1 | TRUE/FALSE | FALSE | Enable manual output control |
| SET_DO | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Control output |
| JOB_REQ | Input | BOOL | 4.3 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_ID | Input | WORD | 6 | W#16#0000  =  Job without function  W#16#0001 = Write low limit  W#16#0002 = Write high limit  W#16#0004 = Write integration time  W#16#0081 = Read integration time  W#16#0082 = Read high limit  W#16#0084 = Read integration time | 0 | Job number |
| JOB_VAL | Input | DINT | 8 | -2<sup>31</sup> to  +2<sup>31</sup> -1 | 0 | Value for write jobs. |
| STS_GATE | Output | BOOL | 12.0 | TRUE/FALSE | FALSE | Status of the internal gate |
| STS_STRT | Output | BOOL | 12.1 | TRUE/FALSE | FALSE | Status of the hardware gate (start input) |
| STS_DO | Output | BOOL | 12.2 | TRUE/FALSE | FALSE | Output status |
| STS_C_DN | Output | BOOL | 12.3 | TRUE/FALSE | FALSE | Status reverse direction.   The last count direction is always displayed. The value of STS_C_DN is FALSE after the first call of the instruction. |
| STS_C_UP | Output | BOOL | 12.4 | TRUE/FALSE | FALSE | Status forward direction   The last count direction is always displayed. The value of STS_C_UP is TRUE after the first call of the instruction. |
| MEAS_VAL | Output | DINT | 14 | 0 to +2<sup>31</sup> -1 | 0 | Actual frequency value |
| COUNTVAL | Output | DINT | 18 | -2<sup>31</sup> to  +2<sup>31</sup> -1 | 0 | Actual count value (starts every time the gate opens at 0) |
| JOB_DONE | Output | BOOL | 22.0 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | Output | BOOL | 22.1 | TRUE/FALSE | FALSE | Faulty job |
| JOB_STAT | Output | WORD | 24 | W#16#0000 to W#16#FFFF | W#16#0000 | Job error number |
|  |  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> If you have set the parameter "response of the output" to "no comparison" via the configuration interface, the following is valid:
>
> - The output will be switched in the same manner that a normal output is switched.
> - The input parameters MAN_DO and SET_DO are not active.
> - The status bit STS_DO remains reset.

**Parameters not interconnected to the block (static local data without the reserved parameter** 
**RESxx**
**):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| STS_CMP | STATIC | BOOL | 26.3 | TRUE/FALSE | FALSE | End of measurement status   Reset with RES_STS .  The measured value is updated after every expired time interval. Here, the end of measurement is reported by the status bit STS_CMP. |
| STS_OFLW | STATIC | BOOL | 26.5 | TRUE/FALSE | FALSE | Status overflow Reset with RES_STS. |
| STS_UFLW | STATIC | BOOL | 26.6 | TRUE/FALSE | FALSE | Status underflow   Reset with RES_STS. |
| JOB_OVAL | STATIC | DINT | 28 | -2<sup>31</sup> to 2<sup>31</sup> -1 | 0 | Output value for read jobs. |
| RES_STS | STATIC | BOOL | 32.2 | TRUE/FALSE | FALSE | Reset status bits.  Resets the status bits STS_CMP, STS_OFLW and STS_UFLW.   Two calls of the instruction are required to reset the status bits. |

### Parameter JOB_ERR and JOB_STAT

JOB_ERR = TRUE if a job error occurs. The precise error cause is displayed in JOB_STAT.

| Event class error code | Description |
| --- | --- |
| W#16#0221 | Integration time too low. |
| W#16#0222 | Integration time too great. |
| W#16#0231 | Low limit of the frequency is too low. |
| W#16#0232 | High limit of the frequency is too high. |
| W#16#0241 | High limit of the frequency is too low. |
| W#16#0242 | High limit of the frequency is too high. |
| W#16#02FF | Invalid job number. |

### System error

If a system error occurs, BIE (binary result) = FALSE.

| Event class error code | Description |
| --- | --- |
| W#16#8001 | Wrong operating mode or faulty parameters. Set the correct operating mode during hardware configuration or use the instruction that matches the set operating mode. |
| W#16#8009 | Invalid channel number. Set a channel number ≤ 3 (CPU-specific value). |

## PULSE: Control pulse width modulation (S7-300)

### Description

You use the "PULSE" instruction to control the pulse width modulation of the user program.

The following functionality is available:

- Starting/stopping via the software gate SW_EN
- Enabling/controlling the output DO
- Retrieving the status bits STS_EN, STS_STRT and STS_DO
- Input of the output value
- Jobs for reading/writing the registers

### Parameter

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Meaning |
| --- | --- | --- | --- | --- | --- | --- |
| LADDR | Input | WORD | 0 | CPU-specific | W#16#0300 | The submodule I/O address, which you have specified during hardware configuration.  If the I and O addresses are not equal, the lesser of the two addresses must be specified. |
| CHANNEL | Input | INT | 2 | CPU 312C: 0 to 1 CPU 313C: 0 to 2 CPU 314C: 0 to 3 | 0 | Channel number |
| SW_EN | Input | BOOL | 4.0 | TRUE/FALSE | FALSE | Software gate for starting/stopping the output |
| MAN_DO | Input | BOOL | 4.1 | TRUE/FALSE | FALSE | Enable manual output control |
| SET_DO | Input | BOOL | 4.2 | TRUE/FALSE | FALSE | Control output |
| OUTP_VAL | Input | INT | 6.0 | in ppm:  0 to 1000  as S7 analog value: 0 to 27648 | 0 | Default output value   if you enter an output value > 1 000 or 27648, the CPU will limit it to 1 000 or 27648 |
| JOB_REQ | Input | BOOL | 8.0 | TRUE/FALSE | FALSE | Job trigger (positive edge) |
| JOB_ID | Input | WORD | 10 | W#16#0000  = Job without function  W#16#0001 = Write period time  W#16#0002 = Write switch-on delay  W#16#0004 = Write minimum pulse duration  W#16#0081 = Read period time  W#16#0082 = Read switch-on delay  W#16#0084 = Read minimum pulse duration | W#16#0000 | Job number |
| JOB_VAL | Input | DINT | 12 | -2<sup>31</sup> to+2<sup>31</sup> -1 | 0 | Value for write jobs. |
| STS_EN | Output | BOOL | 16.0 | TRUE/FALSE | FALSE | Enable status |
| STS_STRT | Output | BOOL | 16.1 | TRUE/FALSE | FALSE | Status of the hardware gate (start input) |
| STS_DO | Output | BOOL | 16.2 | TRUE/FALSE | FALSE | Output status |
| JOB_DONE | Output | BOOL | 16.3 | TRUE/FALSE | TRUE | New job can be started |
| JOB_ERR | Output | BOOL | 16.4 | TRUE/FALSE | FALSE | Faulty job |
| JOB_STAT | Output | WORD | 18 | W#16#0000 to W#16#FFFF | W#16#0000 | Job error number |
|  |  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

**Parameters not assigned to the block (static local data):**

| Parameter | Declaration | Data type | Address (instance DB) | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- | --- |
| JOB_OVAL | Output | DINT | 20 | -2<sup>31</sup> to 2<sup>31</sup> -1 | 0 | Output value for read jobs. |

### Parameter JOB_ERR and JOB_STAT

JOB_ERR = TRUE if a job error occurs. The precise error cause is displayed in JOB_STAT.

| Event class error code | Description |
| --- | --- |
| W#16#0411 | Period too low. |
| W#16#0412 | Compare value too great. |
| W#16#0421 | On delay too short. |
| W#16#0422 | On delay too long. |
| W#16#0431 | Minimum pulse duration too low. |
| W#16#0432 | Minimum pulse duration too great. |
| W#16#04FF | Invalid job number. |

### System error

If a system error occurs, BIE (binary result) = FALSE.

| Event class error code | Description |
| --- | --- |
| W#16#8001 | Wrong operating mode or faulty parameters. Set the correct operating mode during hardware configuration or use the instruction that matches the set operating mode. |
| W#16#8009 | Invalid channel number. Set a channel number ≤ 3 (CPU-specific value). |
