---
title: "FM x51 Positioning (S7-300, S7-400)"
package: ProgFBFMx51V1enUS
topics: 20
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# FM x51 Positioning (S7-300, S7-400)

This section contains information on the following topics:

- [ABS_INIT (S7-300, S7-400)](#abs_init-s7-300-s7-400)
- [ABS_CTRL (S7-300, S7-400)](#abs_ctrl-s7-300-s7-400)
- [ABS_DIAG (S7-300, S7-400)](#abs_diag-s7-300-s7-400)
- [ABS_CTRL_451 (S7-300, S7-400)](#abs_ctrl_451-s7-300-s7-400)
- [ABS_DIAG_451 (S7-300, S7-400)](#abs_diag_451-s7-300-s7-400)
- [Additional references for FM x51 ABS V1 (S7-300, S7-400)](#additional-references-for-fm-x51-abs-v1-s7-300-s7-400)

## ABS_INIT (S7-300, S7-400)

### Description

The ABS_INIT instruction initializes the following data in the channel DB:

- The control signals
- The feedback signals
- The trigger bits, done bits and error bits of the jobs
- The function switches and their done bits and error bits
- Job management for the instruction [ABS_CTRL](#abs_ctrl-s7-300-s7-400) or [ABS_CTRL_451](#abs_ctrl_451-s7-300-s7-400)

### Call

The instruction must be executed for each channel after a startup, namely, after power-on of the module or CPU. For this reason, call the instruction in the restart organization block OB 100 and in pulling/plugging OB 83, for example or in the initialization phase of your user program. This ensures that your user program does not access obsolete data after a CPU or module restart.

### Data block used

[Channel DB](#channel-data-block-s7-300-s7-400):

The module address must be entered in the channel DB. You should enter it in the startup OB (OB 100).

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the channel DB |

### Return values

The instruction does not provide a return value.

## ABS_CTRL (S7-300, S7-400)

### Description

Using the ABS_CTRL instruction, you can read the operational data of all module channels, assign the channel parameters and modify them in runtime. To complete such actions, use control signals, feedback signals, function switches as well as write and read commands.

### Operating principle

Each time it is called, the instruction performs the following actions:

- Read feedback signals:

  The ABS_CTRL instruction reads all feedback signals of a channel and enters these in the channel OB. The control signals and commands are not processed unless this step is completed, which means that the feedback signals report the channel status given prior to the instruction call.
- [Command management](#job-management-abs_ctrl-s7-300-s7-400):

  The ABS_CTRL instruction processes the read and write commands and transfers the data between the channel DB, parameter DB and the module.
- Write control signals:

  The control signals that are entered in the channel DB are transferred to the module.

### Call

The ABS_CTRL instruction must be called cyclically for each channel, for example, in OB 1.

Before calling the ABS_CTRL instruction, enter all data necessary to execute the selected functions in the channel DB.

### Data blocks used

- [Channel DB](#channel-data-block-s7-300-s7-400):

  The channel DB is the instance DB of the instruction ABS_CTRL. The module address and the channel number must be entered in the channel DB. Incorrect information could result in I/O access errors or in an access to a different module, which in turn gives rise to data corruption.
- [Parameter DB](#parameter-data-block-s7-300-s7-400):

  If you want to use commands to write or read the machine data, you need a parameter DB, whose number must be entered in the channel DB.

### Return values

The instruction provides the following return values:

| RETVAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | At least 1 command is active |
| 0 | 1 | No active command, no errors |
| -1 | 0 | Errors: Data error (DATA_ERR) or  communication error (JOB_ERR) |

### Control signals

If a STOP signal is set or an operator error is pending or a drive enable is missing, the instruction resets the control signals START, DIR_M and DIR_P.

To enable the restart of a trip, acknowledge the operator error with OT_ERR_A=1. With this acknowledgement you cannot submit any other commands and control signals.

If there is no operator error pending, the instruction sets the acknowledgment status for the operator error OT_ERR_A to 0.

When the channel reports the start of the trip, the instruction sets and resets the start signals START, DIR_P and DIR_M, except in "jog" mode.

If the axis are not configured, the instruction puts all the control signals on hold, except the operator error acknowledgment OT_ERR_A.

### Commands and control signals

You can issue several commands at the same time, also together with the control signals necessary for the positioning. If at least one write command is initiated at the same time as the control signals START, DIR_M or DIR_P, the instruction puts these control signals on hold until the write commands have been executed.

### Startup

Call instruction[ABS_INIT](#abs_init-s7-300-s7-400) at the startup of the module or CPU. This action includes a reset of the function switches. The ABS_CTRL instruction acknowledges the module startup. During this time, RETVAL and JOBBUSY = 1.

### Reaction to error

If incorrect data is found in a write command, the channel returns feedback signal DATA_ERR = 1 in the channel DB. If an error is found in a write or read command during communication with the module, the cause of error is saved to the JOB_ERR parameter in the channel DB.

- Error with a write command:

  The trigger bit is reset and the error bit _ERR and done bit _D are set if the command is corrupt. For all other pending write commands, the trigger bit is also reset and only the error bit _ERR is set. The awaiting write commands will be withdrawn because commands could stack up on top of each other.

  The execution of the pending read commands is continued. JOB_ERR is retriggered accordingly for all commands.
- Error with a read command:

  The trigger bit is reset and the error bit _ERR and done bit _D are set if the command is corrupt.

  The execution of the pending read commands is continued. JOB_ERR is retriggered accordingly for all commands.

## ABS_DIAG (S7-300, S7-400)

### Description

Use the ABS_DIAG instruction to read the data from the diagnostics buffer of the module and make it available for display on the HMI system or for programmed evaluation.

### Operating principle

The instruction reads the data from the diagnostic buffer when a new entry is displayed in the diagnostics buffer by feedback signal DIAG = 1 in the channel DB. After reading the data from the diagnostics buffer, the module sets the DIAG bit in the channel DB to 0.

### Call

The instruction must be called cyclically, for example, in OB 1. Additional calls in an interrupt OB are not allowed. To complete the execution of the instruction, you must call it at least twice (in 2 cycles).

### Data block used

[Diagnostics DB](#diagnostics-data-block-s7-300-s7-400):

The diagnostics DB is the instance DB of the instruction ABS_DIAG. The module address must be entered in the diagnostics DB. The most recent entry in the diagnostics buffer is written to the DIAG[1] structure and the oldest entry to the DIAG[9] structure.

### Return values

The instruction provides the following return values in the RETVAL parameter of the diagnostics DB:

| RETVAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | Command active |
| 0 | 1 | No active command, no errors |
| -1 | 0 | Errors |

### Commands

You can read the diagnostic buffer, independent of any new entry, by setting trigger bit DIAGRD_EN in the diagnostics DB. After the diagnostics buffer has been read, the trigger bit is set to 0.

Execute this command after the startup of a CPU and module is completed. This step ensures consistency between the content of the diagnostics DB and the diagnostics buffer of the module, even if the module has not made a new entry in the diagnostics buffer.

### Startup

The instruction does not run a startup routine.

### Reaction to error

Information about the cause of an execution error is available in the JOB_ERR parameter of the diagnostics DB.

### Diagnostics data

| Errors | Evaluation using OB 82 |
| --- | --- |
| Module fault | OB82_MDL_DEFECT |
| Internal error | OB82_INT_FAULT |
| External error | OB82_EXT_FAULT |
| Channel error | OB82_PNT_INFO |
| External auxiliary voltage is missing | OB82_EXT_VOLTAGE |
| Watchdog timeout | OB82_WTCH_DOG_FLT |
| Failure of the internal internal supply voltage of the module | OB82_INT_PS_FLT |
| Hardware interrupt lost | OB82_HW_INTR_FLT |

### Error classes

The error events are organized in the following error classes:

- [Error class 1: Operational errors](#error-class-1-process-error-s7-300-s7-400)
- [Error class 2: Operator errors](#error-class-2-operator-error-s7-300-s7-400)
- [Error class 4: Data errors](#error-class-4-data-error-s7-300-s7-400)
- [Error class 5: Machine data errors](#error-class-5-machine-data-error-s7-300-s7-400)
- [Error class 6: Incremental dimension table errors](#error-class-6-increment-table-error-s7-300-s7-400)
- [Error class 15: Messages](#error-class-15-messages-s7-300-s7-400)
- [Error class 128: Diagnostics errors](#error-class-128-diagnostics-errors-s7-300-s7-400)

## ABS_CTRL_451 (S7-300, S7-400)

### Description

Using the ABS_CTRL_451 instruction, you can read the operational data of all module channels, assign the channel parameters and change them in runtime. To complete such actions, use control signals, feedback signals, function switches as well as write and read jobs.

### Operating principle

Each time it is called, the instruction performs the following actions:

- Read feedback signals:

  The ABS_CTRL_451 instruction reads all feedback signals of a channel and enters these in the channel OB. The control signals and jobs are not processed unless this step is completed, which means that the feedback signals report the channel status given prior to the instruction call.
- [Job management](#job-management-abs_ctrl_451-s7-300-s7-400):

  The ABS_CTRL_451 instruction processes the read and write jobs and transfers the data between the channel DB, parameter DB and the module.
- Write control signals:

  The control signals that are entered in the channel DB are transferred to the module.

### Call

The ABS_CTRL_451 instruction must be called cyclically for each channel, for example, in OB 1.

Before calling the ABS_CTRL_451 instruction, enter all data necessary to execute the selected functions in the channel DB.

### Data blocks used

- [Channel DB](#channel-data-block-s7-300-s7-400):

  The module address and channel number must be entered in the channel DB. Incorrect information can result in I/O access errors or in an access to a different module, which in turn gives rise to data corruption.
- [Parameter DB](#parameter-data-block-s7-300-s7-400):

  If you want to use jobs to write or read machine data, you need a parameter DB, the number of which must be entered in the channel DB.

### Parameter

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the channel DB |
| RET_VAL | OUTPUT | INT | Return value |

### Return values

The instruction provides the following return values:

| RET_VAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | At least 1 job is active |
| 0 | 1 | No active job, no errors |
| -1 | 0 | Errors: Data error (DATA_ERR) or  communication error (JOB_ERR) |

### Control signals

If a STOP signal is set or an operator error is pending or a drive enable is missing, the instruction resets the control signals START, DIR_M and DIR_P.

To enable the restart of a trip, acknowledge the operator error with OT_ERR_A=1. With this acknowledgment you cannot submit any other jobs and control signals.

If there is no operator error pending, the instruction sets the acknowledgment status for the operator error OT_ERR_A to 0.

When the channel reports the start of the trip, the instruction sets and resets the start signals START, DIR_P and DIR_M, except in "jog" mode..

If the axis are not configured, the instruction puts all the control signals on hold, except the operator error acknowledgment OT_ERR_A.

### Jobs and control signals

You can transfer several jobs simultaneously, also together with the control signals necessary for the positioning. If at least one write job is initiated at the same time as the control signals START, DIR_M or DIR_P, the instruction puts these control signals on hold until the write jobs have been executed.

### Startup

Call the [ABS_INIT](#abs_init-s7-300-s7-400) instruction at the startup of the module or CPU. This action includes a reset the function switches. The ABS_CTRL_451 instruction acknowledges the module startup. During this time, RETVAL and JOBBUSY = 1.

### Reaction to error

If incorrect data is found in a write job, the channel returns feedback signal DATA_ERR = 1 in the channel DB. If an error is found in a write or read job during communication with the module, the cause of error is saved to the JOB_ERR parameter in the channel DB.

- Write job errors:

  The trigger bit is reset and the error bit _ERR and done bit _D are set if the job is corrupt. For all other pending write jobs, the trigger bit is also reset and only the error bit _ERR is set. The other pending write jobs are revoked to prevent jobs from overlapping.

  The execution of the pending read jobs is continued. JOB_ERR is retriggered accordingly for all jobs.
- Read job errors:

  The trigger bit is reset and the error bit _ERR and done bit _D are set if the job is corrupt.

  The execution of the pending read jobs is continued. JOB_ERR is retriggered accordingly for all jobs.

## ABS_DIAG_451 (S7-300, S7-400)

### Description

Use the ABS_DIAG_451 instruction to read the data from the diagnostics buffer of the module and make it available for display on the HMI system or for programmed evaluation.

### Operating principle

The instruction reads the data from the diagnostic buffer when a new entry is displayed in the diagnostics buffer by feedback signal DIAG = 1 in the channel DB. After reading the data from the diagnostics buffer, the module sets the DIAG bit in the channel DB to 0.

### Call

The instruction must be called cyclically, for example, in OB 1. Additional calls in an interrupt OB are not allowed. To complete the execution of the instruction, you must call it at least twice (in 2 cycles).

### Data block used

[Diagnostics DB](#diagnostics-data-block-s7-300-s7-400):

The module address must be entered in the diagnostics DB. The most recent entry in the diagnostics buffer is written to the DIAG[1] structure and the oldest entry to the DIAG[9] structure.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the diagnostics DB |
| RET_VAL | OUTPUT | INT | Return value |

### Return values

The instruction provides the following return values in the RET_VAL parameter of the diagnostics DB:

| RET_VAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | Job active |
| 0 | 1 | No active job, no errors |
| -1 | 0 | Errors |

### Jobs

You can read the diagnostic buffer, independent of any new entry, by setting trigger bit DIAGRD_EN in the diagnostics DB. After the diagnostics buffer has been read, the trigger bit is set to 0.

Execute this job after the startup of a CPU and module is completed. This step ensures consistency between the content of the diagnostics DB and the diagnostics buffer of the module, even if the module has not made a new entry in the diagnostics buffer.

### Startup

The instruction does not run a startup routine.

### Reaction to errors

Information about the cause of an execution error is available in the JOB_ERR parameter of the diagnostics DB.

### Diagnostics data

| Errors | Evaluation using OB 82 |
| --- | --- |
| Module fault | OB82_MDL_DEFECT |
| Internal error | OB82_INT_FAULT |
| External error | OB82_EXT_FAULT |
| Channel error | OB82_PNT_INFO |
| External auxiliary voltage is missing | OB82_EXT_VOLTAGE |
| Front connector missing | OB82_FLD_CONNCTR |
| Watchdog timeout | OB82_WTCH_DOG_FLT |
| Failure of the internal internal supply voltage of the module | OB82_INT_PS_FLT |
| Hardware interrupt lost | OB82_HW_INTR_FLT |

### Error classes

The error events are organized in the following error classes:

- [Error class 1: Operating error](#error-class-1-process-error-s7-300-s7-400)
- [Error class 2: Operator errors](#error-class-2-operator-error-s7-300-s7-400)
- [Error class 4: Data errors](#error-class-4-data-error-s7-300-s7-400)
- [Error class 5: Machine data errors](#error-class-5-machine-data-error-s7-300-s7-400)
- [Error class 6: Incremental dimension table errors](#error-class-6-increment-table-error-s7-300-s7-400)
- [Error class 15: Messages](#error-class-15-messages-s7-300-s7-400)
- [Error class 128: Diagnostics errors](#error-class-128-diagnostics-errors-s7-300-s7-400)

## Additional references for FM x51 ABS V1 (S7-300, S7-400)

This section contains information on the following topics:

- [Channel data block (S7-300, S7-400)](#channel-data-block-s7-300-s7-400)
- [Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400)
- [Diagnostics data block (S7-300, S7-400)](#diagnostics-data-block-s7-300-s7-400)
- [Job management (ABS_CTRL) (S7-300, S7-400)](#job-management-abs_ctrl-s7-300-s7-400)
- [Job management (ABS_CTRL_451) (S7-300, S7-400)](#job-management-abs_ctrl_451-s7-300-s7-400)
- [Error classes (S7-300, S7-400)](#error-classes-s7-300-s7-400)

### Channel data block (S7-300, S7-400)

#### Purpose

The channel DB is the data interface between the user program and FM x51. It contains and stores all data necessary to control and operate a channel.

#### Configuration

The channel DB is divided into different areas:

Channel DB

Addresses *)

Control signals

Feedback signals

Function switches

Trigger bits for write jobs

Trigger bits for read jobs

Done bits

Error bits

Job management for instructions

Data for jobs

*) You can enter the module address in the parameter assignment interface.

#### Content

The table below shows the content of the channel DB.

> **Note**
>
> You may not change any data not listed in this table.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| **Addresses** |  |  |  |  |
| 0.0 | MOD_ADDR | INT | 0 | Module address |
| 2.0 | CH_NO | INT | 1 | Channel number |
| 10.0 | PARADBNO | INT | -1 | Number of the parameter DB |
| **Control signals** |  |  |  |  |
| 14.3 | OT_ERR_A | BOOL | FALSE | 1 = acknowledge operator error |
| 15.0 | START | BOOL | FALSE | 1 = start positioning |
| 15.1 | STOP | BOOL | FALSE | 1 = stop active traversing |
| 15.2 | DIR_M | BOOL | FALSE | 1 = minus direction |
| 15.3 | DIR_P | BOOL | FALSE | 1 = plus direction |
| 15.6 | SPEED252 | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: Start velocity for incremental approach with increment number 252:   - 0 = Creep speed   - 1 = Rapid traverse |
| 15.7 | DRV_EN | BOOL | FALSE | 1 = switch on drive enable |
| 16.0 | MODE_IN | BYTE | B#16#0 | Required mode  - 0 = no mode - 1 = Jog - 3 = reference point approach - 4 = relative incremental approach - 5 = absolute incremental approach |
| 17.0 | MODE_TYPE | BYTE | B#16#0 | - Initial speed for "jog" mode   - 0 = Creep speed   - 1 = Rapid traverse - Increment number for incremental approach mode |
| **Feedback signals** |  |  |  |  |
| 22.2 | DIAG | BOOL | FALSE | 1 = diagnostic buffer modified |
| 22.3 | OT_ERR | BOOL | FALSE | 1 = operator error occurred |
| 22.4 | DATA_ERR | BOOL | FALSE | 1 = data error |
| 22.7 | PARA | BOOL | FALSE | 1 = axis parameters are assigned |
| 23.0 | ST_ENBLD | BOOL | FALSE | 1 = start enabled |
| 23.1 | WORKING | BOOL | FALSE | 1 = positioning is active |
| 23.2 | WAIT_EI | BOOL | FALSE | 1 = axis waiting for external enable |
| 23.4 | SPEED_OUT | BOOL | FALSE | - 0 = Creep speed - 1 = Rapid traverse |
| 23.5 | ZSPEED | BOOL | FALSE | 1 = axis is located in the standstill range |
| 23.6 | CUTOFF | BOOL | FALSE | 1 = axis is located in the switch-off range |
| 23.7 | CHGOVER | BOOL | FALSE | 1 = axis is located in the changeover range |
| 24.0 | MODE_OUT | BYTE | B#16#0 | Active operating mode |
| 25.0 | SYNC | BOOL | FALSE | 1 = axis is synchronized |
| 25.1 | MSR_DONE | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Length measurement / edge detection completed |
| 25.2 | GO_M | BOOL | FALSE | 1 = axis moves in minus direction |
| 25.3 | GO_P | BOOL | FALSE | 1 = axis moves in plus direction |
| 25.5 | FVAL_DONE | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Set actual value on-the-fly completed |
| 25.7 | POS_RCD | BOOL | FALSE | 1 = In position |
| 26.0 | ACT_POS | DINT | L#0 | Current actual value (current position of the axis) |
| **Function switch** |  |  |  |  |
| 34.0 | PLOOP_ON | BOOL | FALSE | 1 = Loop approach in plus direction |
| 34.1 | MLOOP_ON | BOOL | FALSE | 1 = Loop approach in minus direction |
| 34.2 | EI_OFF | BOOL | FALSE | 1 = Do not evaluate enable input |
| 34.3 | EDGE_ON | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Edge detection on |
| 34.4 | MSR_ON | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Length measurement on |
| **Trigger bits for write jobs** |  |  |  |  |
| 35.0 | MDWR_EN | BOOL | FALSE | 1 = write machine data |
| 35.1 | MD_EN | BOOL | FALSE | 1 = Enable machine data |
| 35.2 | DELDIST_EN | BOOL | FALSE | 1 = Delete remaining distance |
| 35.3 | AVALREM_EN | BOOL | FALSE | 1 = Cancel set actual value |
| 35.4 | TRGL1WR_EN | BOOL | FALSE | 1 = Write incremental dimension table 1  (increment number 1 ... 50) |
| 35.5 | TRGL2WR_EN | BOOL | FALSE | 1 = Write incremental dimension table 2  (increment number 51 ... 100) |
| 35.6 | REFPT_EN | BOOL | FALSE | 1 = set reference point |
| 35.7 | AVAL_EN | BOOL | FALSE | 1 = Set actual value |
| 36.0 | FVAL_EN | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Set actual value on-the-fly |
| 36.1 | ZOFF_EN | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Set zero offset |
| 36.2 | TRG252_254_EN | BOOL | FALSE | 1 = Write increment for increment number 252 or 254 |
| 36.3 | TRG255_EN | BOOL | FALSE | 1 = write increment for increment number 255 |
| 36.4 | DELDIAG_EN | BOOL | FALSE | 1 = delete diagnostic buffer |
| **Activation bits for read jobs** |  |  |  |  |
| 36.5 | MDRD_EN | BOOL | FALSE | 1 = Reading machine data |
| 36.6 | TRGL1RD_EN | BOOL | FALSE | 1 = Read incremental dimension table 1  (increment number 1 ... 50) |
| 36.7 | TRGL2RD_EN | BOOL | FALSE | 1 = Read incremental dimension table 2  (increment number 51 ... 100) |
| 37.0 | MSRRD_EN | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Read measured values |
| 37.1 | ACTSPD_EN | BOOL | FALSE | 1 = Read actual speed, remaining distance and current increment |
| 37.2 | ENCVAL_EN | BOOL | FALSE | 1 = read encoder values |
| **Done bits for function switches** |  |  |  |  |
| 38.0 | PLOOP_D | BOOL | FALSE | 1 = "loop approach in plus direction" job completed |
| 38.1 | MLOOP_D | BOOL | FALSE | 1 = "loop approach in minus direction" job completed |
| 38.2 | EI_D | BOOL | FALSE | 1 = "Do not evaluate enable input" job completed |
| 38.3 | EDGE_D | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = "Edge detection ON" job completed |
| 38.4 | MSR_D | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = "Length measurement ON" job completed |
| **Done bits for write jobs** |  |  |  |  |
| 39.0 | MDWR_D | BOOL | FALSE | 1 = "Write machine data" job completed |
| 39.1 | MD_D | BOOL | FALSE | 1 = "Enable machine data" job completed |
| 39.2 | DELDIST_D | BOOL | FALSE | 1 = "Delete remaining distance" job completed |
| 39.3 | AVALREM_D | BOOL | FALSE | 1 = "Cancel set actual value" job completed |
| 39.4 | TRGL1WR_D | BOOL | FALSE | 1 = "Write incremental dimension table 1" job completed |
| 39.5 | TRGL2WR_D | BOOL | FALSE | 1 = "Write incremental dimension table 2" job completed |
| 39.6 | REFPT_D | BOOL | FALSE | 1 = "Set reference point" job completed |
| 39.7 | AVAL_D | BOOL | FALSE | 1 = "Set actual value" job completed |
| 40.0 | FVAL_D | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = "Set actual value on-the-fly" job completed |
| 40.1 | ZOFF_D | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = "Set zero offset" job completed |
| 40.2 | TRG252_254_D | BOOL | FALSE | 1 = "Write increment for increment number 252 or 254" job completed |
| 40.3 | TRG255_D | BOOL | FALSE | 1 = "Write increment for increment number 255" job completed |
| 40.4 | DELDIAG_D | BOOL | FALSE | 1 = "Delete diagnostic buffer" job completed |
| **Done bits for read jobs** |  |  |  |  |
| 40.5 | MDRD_D | BOOL | FALSE | 1 = "Read machine data" job completed |
| 40.6 | TRGL1RD_D | BOOL | FALSE | 1 = "Read incremental dimension table 1" job completed |
| 40.7 | TRGL2RD_D | BOOL | FALSE | 1 = "Read incremental dimension table 2" job completed |
| 41.0 | MSRRD_D | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = "Read measured values" job completed |
| 41.1 | ACTSPD_D | BOOL | FALSE | 1 = "Read actual speed, remaining distance and current increment" job completed |
| 41.2 | ENCVAL_D | BOOL | FALSE | 1 = "Read encoder values" job completed |
| **Error bits for function switches** |  |  |  |  |
| 42.0 | PLOOP_ERR | BOOL | FALSE | 1 = Error with "loop approach in plus direction" job |
| 42.1 | MLOOP_ERR | BOOL | FALSE | 1 = Error with "loop approach in minus direction" job |
| 42.2 | EI_ERR | BOOL | FALSE | 1 = Error with "do not evaluate enable input" job |
| 42.3 | EDGE_ERR | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Error during "Edge detection ON" job |
| 42.4 | MSR_ERR | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Error during "Length measurement ON" job |
| **Error bits for write jobs** |  |  |  |  |
| 43.0 | MDWR_ERR | BOOL | FALSE | 1 = Error with "Write machine data" job |
| 43.1 | MD_ERR | BOOL | FALSE | 1 = Error with "Activate machine data" job |
| 43.2 | DELDIST_ERR | BOOL | FALSE | 1 = Error with "Delete remaining distance" job |
| 43.3 | AVALREM_ERR | BOOL | FALSE | 1 = Error with "Cancel set actual value" job |
| 43.4 | TRGL1WR_ERR | BOOL | FALSE | 1 = Error with "Write incremental dimension table 1" job |
| 43.5 | TRGL2WR_ERR | BOOL | FALSE | 1 = Error with "Write incremental dimension table 2" job |
| 43.6 | REFPT_ERR | BOOL | FALSE | 1 = Error with "set reference point" job |
| 43.7 | AVAL_ERR | BOOL | FALSE | 1 = Error with "set actual value" job |
| 44.0 | FVAL_ERR | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Error in "set actual value on-the-fly" job |
| 44.1 | ZOFF_ERR | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Error in "set zero offset" job |
| 44.2 | TRG252_254_ERR | BOOL | FALSE | 1 = Error with "Write increment for increment number 252 or 254" job |
| 44.3 | TRG255_ERR | BOOL | FALSE | 1 = Error with "Write increment for incremental dimension table 255" job |
| 44.4 | DELDIAG_ERR | BOOL | FALSE | 1 = Error with "Delete diagnostic buffer" |
| **Error bits for read jobs** |  |  |  |  |
| 44.5 | MDRD_ERR | BOOL | FALSE | 1 = Error with "read machine data" job |
| 44.6 | TRGL1RD_ERR | BOOL | FALSE | 1 = Error with "Read incremental dimension table 1" job |
| 44.7 | TRGL2RD_ERR | BOOL | FALSE | 1 = Error with "Read incremental dimension table 2" job |
| 45.0 | MSRRD_ERR | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: 1 = Error with "Read measured values" job |
| 45.1 | ACTSPD_ERR | BOOL | FALSE | 1 = Error with "Read actual speed, remaining distance and current increment" job |
| 45.2 | ENCVAL_ERR | BOOL | FALSE | 1 = Error with "Read current encoder values" job |
| **Job management for the instruction**  **ABS_CTRL**  **or**  **ABS_CTRL_451** |  |  |  |  |
| 48.0 | JOB_ERR | INT | 0 | Error number of the communication error |
| 50.0 | JOBBUSY | BOOL | FALSE | 1 = At least 1 job active |
| 50.1 | JOBRESET | BOOL | FALSE | 1 = Reset all error bits and done bits |
| **Data for "zero offset" job (** **FM 451** **)** |  |  |  |  |
| 80.0 | ZOFF | DINT | L#0 | - FM 351: 0 (not used) - FM 451: Zero offset |
| **Data for "Set actual value" job** |  |  |  |  |
| 84.0 | AVAL | DINT | L#0 | Coordinate for "Set actual value" |
| **Data for "Set actual value on-the-fly" (** **FM 451** **)** |  |  |  |  |
| 88.0 | FVAL | DINT | L#0 | - FM 351: 0 (not used) - FM 451: Coordinate for "Set actual value on-the-fly" |
| **Data for "Set reference point" job** |  |  |  |  |
| 92.0 | REFPT | DINT | L#0 | Coordinate for "Set reference point" |
| **Data for "Write increment for increment number 252 or 254" job** |  |  |  |  |
| 96.0 | TRG252_254 | DINT | L#0 | Write increment for increment number 252 or 254 |
| **Data for "Write increment for increment number 255" job** |  |  |  |  |
| 100.0 | TRG255 | DINT | L#0 | Increment for increment number 255 |
| 104.0 | CHGDIF255 | DINT | L#0 | Changeover difference for increment number 255 |
| 108.0 | CUTDIF255 | DINT | L#0 | Switch-off difference for increment number 255 |
| **Data for "Read position data" job** |  |  |  |  |
| 112.0 | ACTSPD | DINT | L#0 | Current speed |
| 116.0 | DIST_TO_GO | DINT | L#0 | Remaining distance |
| 120.0 | ACT_TRG | DINT | L#0 | Current increment |
| **Data for "Read encoder data" job** |  |  |  |  |
| 124.0 | ENCVAL | DINT | L#0 | Actual encoder value (internal representation) |
| 128.0 | ZEROVAL | DINT | L#0 | Last zero mark value (internal representation) |
| 132.0 | ENC_ADJ | DINT | L#0 | Absolute encoder adjustment |
| **Data for the "Length measurements / edge detection" job (** **FM 451** **)** |  |  |  |  |
| 136.0 | BEG_VAL | DINT | L#0 | - FM 351: 0 (not used) - FM 451: Start value of length measurement / edge detection |
| 140.0 | END_VAL | DINT | L#0 | - FM 351: 0 (not used) - FM 451: End value of length measurement / edge detection |
| 144.0 | LEN_VAL | DINT | L#0 | - FM 351: 0 (not used) - FM 451: Length |

### Parameter data block (S7-300, S7-400)

#### Purpose

In order to change machine data and incremental dimension tables in runtime, you need a parameter DB in which this data is stored. The parameters can be changed from the user program or from an HMI system.

You can export data displayed in the parameter assignment interface to a parameter DB. You can also import a parameter DB into the parameter assignment interface and view it there.

Each module channel can have several sets of parameter assignment data, for example, for different recipes. You can switch among these in your program.

#### Configuration

Parameter DB

Machine data

incremental dimension tables

#### Content

The table below shows the content of the parameter DB.

> **Note**
>
> You may not change any data not listed in this table.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| **Machine data** |  |  |  |  |
| 4.0 | EDGEDIST | DINT | L#0 | - FM 351: 0 (not used) - FM 451: Minimum edge interval |
| 8.0 | UNITS | DINT | L#1 | System of units |
| 12.0 | AXIS_TYPE | DINT | L#0 | 0 = Linear axis, 1 = Rotary axis |
| 16.0 | ENDROTAX | DINT | L#100 000 | End of rotary axis |
| 20.0 | ENC_TYPE | DINT | L#1 | Encoder type, message length |
| 24.0 | DISP_REV | DINT | L#80 000 | Length per encoder revolution |
| 32.0 | INC_REV | DINT | L#500 | Increments per encoder revolution |
| 36.0 | NO_REV | DINT | L#1 | Number of encoder revolutions |
| 40.0 | BAUDRATE | DINT | L#0 | Transmission rate |
| 44.0 | REFPT | DINT | L#0 | Reference point coordinate |
| 48.0 | ENC_ADJ | DINT | L#0 | Absolute encoder adjustment |
| 52.0 | REFPT_TYPE | DINT | L#0 | Type of reference point approach |
| 59.0 | CNT_DIR | BOOL | FALSE | Counting direction:  - 0 = Normal - 1 = Inverted |
| 63.0 | MON_WIRE | BOOL | TRUE | 1 = wire break monitoring |
| 63.1 | MON_FRAME | BOOL | TRUE | 1 = frame error monitoring |
| 63.2 | MON_PULSE | BOOL | TRUE | 1 = missing pulses monitoring |
| 64.0 | SSW_STRT | DINT | L#-100 000 000 | Software limit switch start |
| 68.0 | SSW_END | DINT | L#100 000 000 | Software limit switch end |
| 76.0 | TRG_RANGE | DINT | L#1000 | Target range |
| 80.0 | MON_TIME | DINT | L#2000 | Monitoring time [ms] |
| 84.0 | ZSPEED_R | DINT | L#1000 | Standstill range |
| 88.0 | ZSPEED_L | DINT | L#30 000 | High limit of the standstill speed |
| 92.0 | CTRL_TYPE | DINT | L#1 | Control type (1 - 4) |
| 99.0 | REFPT_SPD | BOOL | TRUE | Start speed in the case of a reference point approach:  - 0 = Rapid traverse - 1 = Creep speed |
| 99.1 | EI_TYPE | BOOL | FALSE | - FM 351: 0 (not used) - FM 451: Enable input:   - 0 = Level-controlled   - 1 = Edge controlled |
| 100.0 | CHGDIF_P | DINT | L#5000 | Changeover difference plus |
| 104.0 | CHGDIF_M | DINT | L#5000 | Changeover difference minus |
| 108.0 | CUTDIF_P | DINT | L#2000 | Switch-off difference plus |
| 112.0 | CUTDIF_M | DINT | L#2000 | Switch-off difference minus |
| **Increment dimension table 1** |  |  |  |  |
| 120.0 | TRGL1.TRG[1] | DINT | L#0 | Increment number 1 |
| .  .  . | .  .  . | .  .  . | .  .  . | .  .  . |
| 316.0 | TRGL1.TRG[50] | DINT | L#0 | Increment number 50 |
| **Increment dimension table 2** |  |  |  |  |
| 320.0 | TRGL2.TRG[51] | DINT | L#0 | Increment number 51 |
| .  .  . | .  .  . | .  .  . | .  .  . | .  .  . |
| 516.0 | TRGL2.TRG[100] | DINT | L#0 | Increment number 100 |

### Diagnostics data block (S7-300, S7-400)

#### Purpose

The diagnostics DB is the storage location for the instruction [ABS_DIAG](#abs_diag-s7-300-s7-400) or [ABS_DIAG_451](#abs_diag_451-s7-300-s7-400). It contains the module's diagnostics buffer which is processed by the instruction.

#### Configuration

Diagnostics DB

Module address

Internal data

Job status

Trigger bit

Processed diagnostics buffer

#### Content

The table below shows the content of the diagnostics DB.

> **Note**
>
> You may not change any data not listed in this table.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 0.0 | MOD_ADDR | INT | 0 | Module address |
| 256.0 | JOB_ERR | INT | 0 | Error number of the communication error |
| 258.0 | JOBBUSY | BOOL | FALSE | 1 = Job active |
| 258.1 | DIAGRD_EN | BOOL | FALSE | 1 = definitely read diagnostics buffer |
| 260.0 | DIAG_CNT | INT | 0 | Number of valid entries in the list |
| 262.0 | DIAG[1] | STRUCT |  | Diagnostics data - latest entry |
| 272.0 | DIAG[2] | STRUCT |  | Diagnostics data - second entry |
| 282.0 | DIAG[3] | STRUCT |  | Diagnostics data - third entry |
| 292.0 | DIAG[4] | STRUCT |  | Diagnostics data - fourth entry |
| 302.0 | DIAG[5] | STRUCT |  | Diagnostics data - fifth entry |
| 312.0 | DIAG[6] | STRUCT |  | Diagnostics data - sixth entry |
| 322.0 | DIAG[7] | STRUCT |  | Diagnostics data - seventh entry |
| 332.0 | DIAG[8] | STRUCT |  | Diagnostics data - eighth entry |
| 342.0 | DIAG[9] | STRUCT |  | Diagnostics data - ninth entry |

#### Structure of the diagnostics entry

The table below shows the structure of a diagnostics entry DIAG[n].

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| +0.0 | STATE | BOOL | FALSE | 0 = incoming event  1 = outgoing event |
| +0.1 | INTF | BOOL | FALSE | 1 = internal error |
| +0.2 | EXTF | BOOL | FALSE | 1 = external error |
| +2.0 | FCL | INT | 0 | Error class:  1: Operating error  2: Operating errors  4: Data error  5: Machine data error  6: Increment dimension table error  15: Messages  128: Diagnostics errors |
| +4.0 | FNO | INT | 0 | Error number |
| +6.0 | CH_NO | INT | 0 | Channel number |
| +8.0 | TRG_NO | INT | 0 | Increment number |

### Job management (ABS_CTRL) (S7-300, S7-400)

#### Jobs

Data communication with the module other than the transfer of control and feedback signals is handled with jobs.

In order to initiate a job, set the corresponding trigger bit in the channel DB, including the specific data for write jobs. To execute the job, call the [ABS_CTRL](#abs_ctrl-s7-300-s7-400) instruction.

If you use the FM 351 centrally, a read job needs precisely one cycle. If you use the FM 351 in a distributed configuration, a read job may need several cycles.

Due to the required acknowledgments of the module, at least 3 calls or OB cycles are required to execute write jobs.

Once a job has been completed, the instruction resets the trigger bit. The next job pending is identified and executed at the next call of the instruction.

In addition to the trigger bit with the _EN extension for "enable", each job is provided a done bit and an error bit. Their names have the extension _D for "done" or _ERR for "error". When the job is completed, the ABS_CTRL instruction updates the done bits and error bits. Following evaluation or prior to the initiation of a job, you should set these bits to 0.

When you set the JOBRESET bit, all done and error bits are reset prior to executing jobs pending. The JOBRESET bit is then reset to 0.

#### Function switches

The function switches toggle the channel states on and off. A job for writing the function switches is only executed when there is a change to a switch setting. The setting of the function switch is retained after the job has been executed.

Function switches and jobs can be used concurrently at the call of the ABS_CTRL instruction.

Similar to jobs, the function switches are provided bits with name extension _ON/_OFF, done bits with name extension _D and error bits with name extension _ERR.

You should set these bits to 0 before you initiate a job to change a function switch, in order to enable the evaluation of the done bits and error bits of the function switches.

#### Order of job execution

You can initiate several jobs in a single operation. If no jobs are active, the job management of the ABS_CTRL instruction performs a scan to detect set trigger bits or changes to function switches, starting with the MDWR_EN job. Any job found are executed. When the job is completed, the job management searches for the next job to be executed. After having scanned the last ENCVAL_EN job, the function restarts the scan at the MDWR_EN job. This scan is repeated until all jobs have been executed.

The jobs are processed in the following technologically appropriate order:

| Order | Address in the channel DB | Parameters | Description | Reset by |
| --- | --- | --- | --- | --- |
| **Write jobs** |  |  |  |  |
| 1 | 35.0 | MDWR_EN | Write machine data | Instruction |
| 2 | 35.1  35.2  35.3  36.4 | MD_EN  DELDIST_EN  AVALREM_EN  DELDIAG_EN | Enable machine data  Delete remaining distance  Cancel set actual value  Delete diagnostics buffer | Instruction |
| 3 | 35.4 | TRGL1WR_EN | Write incremental dimension table 1 | Instruction |
| 4 | 35.5 | TRGL2WR_EN | Write incremental dimension table 2 | Instruction |
| 5 | 35.6 | REFPT_EN | Set reference point | Instruction |
| 6 | 34.0  34.1  34.2 | Function switch:  PLOOP_ON  MLOOP_ON  EI_OFF | Loop approach in plus direction  Loop approach in minus direction  Do not evaluate enable input | User program |
| 7 | 35.7 | AVAL_EN | Set actual value | Instruction |
| 10 | 36.2 | TRG252_254_EN | Write increment for increment number 254 | Instruction |
| 11 | 36.3 | TRG255_EN | Write increment for increment number 255 | Instruction |
| **Read jobs** |  |  |  |  |
| 12 | 36.5 | MDRD_EN | Reading machine data | Instruction |
| 13 | 36.6 | TRGL1RD_EN | Read incremental dimension table 1 | Instruction |
| 14 | 36.7 | TRGL2RD_EN | Read incremental dimension table 2 | Instruction |
| 16 | 37.1 | ACTSPD_EN | Read current velocity, remaining distance and increment | Instruction |
| 17 | 37.2 | ENCVAL_EN | Read encoder data | Instruction |

This order enables you to completely trigger a positioning motion using a set of jobs and control signals. The jobs encompass the writing and activation of the machine data, the setup of the external enable input and the writing of increments for the incremental approaches.

#### Jobs during active positioning

If initiated while a positioning job is active, the write jobs listed in the following table are held until the current positioning job is completed and are then executed at the next instruction call.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 34.0 | PLOOP_ON | BOOL | FALSE | 1 = Loop approach in plus direction |
| 34.1 | MLOOP_ON | BOOL | FALSE | 1 = Loop approach in minus direction |
| 34.2 | EI_OFF | BOOL | FALSE | 1 = Do not evaluate enable input |
| 35.1 | MD_EN | BOOL | FALSE | 1 = Enable machine data |
| 35.2 | DELDIST_EN | BOOL | FALSE | 1 = Delete remaining distance |
| 35.3 | AVALREM_EN | BOOL | FALSE | 1 = Cancel set actual value |
| 35.6 | REFPT_EN | BOOL | FALSE | 1 = Set reference point coordinate |
| 35.7 | AVAL_EN | BOOL | FALSE | 1 = Set actual value |
| 36.4 | DELDIAG_EN | BOOL | FALSE | 1 = Delete diagnostics buffer |

#### Job status

The status of job execution can be read from the return value RETVAL and activity bit JOBBUSY in the channel DB. The status of an individual job can be evaluated based on its trigger bits, done bits and error bits.

|  | RETVAL | JOBBUSY | Trigger bit _EN | Done bit _D | Error bit _ERR |
| --- | --- | --- | --- | --- | --- |
| Job active | 1 | 1 | 1 | 0 | 0 |
| Job completed without errors | 0 | 0 | 0 | 1 | 0 |
| Job completed with errors | -1 | 0 | 0 | 1 | 1 |
| Write job cancelled | -1 | 0 | 0 | 0 | 1 |

### Job management (ABS_CTRL_451) (S7-300, S7-400)

#### Jobs

Data communication with the module other than the control and feedback signals is handled using jobs.

To initiate a job, set the corresponding trigger bit in the channel DB and the corresponding data for write jobs. Then call the [ABS_CTRL_451](#abs_ctrl_451-s7-300-s7-400) instruction to execute the job.

Due to the required acknowledgments of the module, at least 3 calls or OB cycles are required to execute write jobs. A read job is executed immediately.

Once a job has been completed, the instruction resets the trigger bit. The next job pending is identified and executed at the next call of the instruction.

In addition to the trigger bit with the _EN extension for "enable", each job is provided a done bit and an error bit. Their names have the extension _D for "done" or _ERR for "error". When the job is completed, the ABS_CTRL_451 instruction updates the done bits and error bits. After the evaluation or prior to issuing a job, these bits should be set to 0.

When you set the JOBRESET bit, all done and error bits are reset before pending jobs are executed. The JOBRESET bit is then reset to 0.

#### Function switches

The function switches switch the states of the channel on and off. A job for writing the function switches is only executed when there is a change to a switch setting. The setting of the function switch is retained after the job has been executed.

Function switches and jobs can be used concurrently at the call of ABS_CTRL_451.

Similar to jobs, the function switches are provided bits with name extension _ON/_OFF, done bits with name extension _D and error bits with name extension _ERR.

To be able to evaluate the done bits and error bits of the function switches, you should set these bits to 0 before you issue a job to change a function switch.

#### Order of job execution

You can select several jobs simultaneously. If no jobs are active, the job management of the ABS_CTRL_451 instruction performs a scan to detect set trigger bits or changes to function switches, starting with the MDWR_EN job. If a job is found, it is processed. When the job is concluded, the job management searches for the next job to be processed. After having scanned the last ENCVAL_EN job, the function restarts the scan at the MDWR_EN job. This searching process is repeated until all the jobs have been processed.

The jobs are processed in the following technologically appropriate order:

| Order | Address in the channel DB | Parameters | Description | Reset from |
| --- | --- | --- | --- | --- |
| **Write jobs** |  |  |  |  |
| 1 | 35.0 | MDWR_EN | Write machine data | Instruction |
| 2 | 35.1  35.2  35.3  36.4 | MD_EN  DELDIST_EN  AVALREM_EN  DELDIAG_EN | Enable machine data  Delete remaining distance  Cancel set actual value  Delete diagnostic buffer | Instruction |
| 3 | 35.4 | TRGL1WR_EN | Write incremental dimension table 1 | Instruction |
| 4 | 35.5 | TRGL2WR_EN | Write incremental dimension table 2 | Instruction |
| 5 | 35.6 | REFPT_EN | Set reference point | Instruction |
| 6 | 34.0  34.1  34.2  34.3  34.4 | Function switch:  PLOOP_ON  MLOOP_ON  EI_OFF  EDGE_ON  MSR_ON | Loop approach in plus direction  Loop approach in minus direction  Do not evaluate enable input  Edge detection on  Length measurement on | User program |
| 7 | 35.7 | AVAL_EN | Set actual value | Instruction |
| 8 | 36.0 | FVAL_EN | Set actual value on-the-fly | Instruction |
| 9 | 36.1 | ZOFF_EN | Set zero point offset | Instruction |
| 10 | 36.2 | TRG252_254_EN | Write increment for increment number 252/254 | Instruction |
| 11 | 36.3 | TRG255_EN | Write increment for increment number 255 | Instruction |
| **Read jobs** |  |  |  |  |
| 12 | 36.5 | MDRD_EN | Reading machine data | Instruction |
| 13 | 36.6 | TRGL1RD_EN | Read incremental dimension table 1 | Instruction |
| 14 | 36.7 | TRGL2RD_EN | Read incremental dimension table 2 | Instruction |
| 15 | 37.0 | MSRRD_EN | Read measured values | Instruction |
| 16 | 37.1 | ACTSPD_EN | Read current velocity, remaining distance and current increment | Instruction |
| 17 | 37.2 | ENCVAL_EN | Read encoder data | Instruction |

This order enables you to completely trigger a positioning with a set of jobs and control signals. The jobs go from writing and activating the machine data through the setting of the external enable input up to writing the increments for the incremental approaches.

#### Jobs during an ongoing positioning

If initiated while a positioning job is active, the write jobs listed in the following table are held until the current positioning job is completed and are then executed at the next instruction call.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 34.0 | PLOOP_ON | BOOL | FALSE | 1 = loop approach in plus direction |
| 34.1 | MLOOP_ON | BOOL | FALSE | 1 = loop approach in minus direction |
| 34.2 | EI_OFF | BOOL | FALSE | 1 = do not evaluate enable input |
| 34.3 | EDGE_ON | BOOL | FALSE | 1 = Edge detection on |
| 34.4 | MSR_ON | BOOL | FALSE | 1 = Length measurement on |
| 35.1 | MD_EN | BOOL | FALSE | 1 = Enable machine data |
| 35.2 | DELDIST_EN | BOOL | FALSE | 1 = delete remaining distance |
| 35.3 | AVALREM_EN | BOOL | FALSE | 1 = cancel set actual value |
| 35.6 | REFPT_EN | BOOL | FALSE | 1 = set reference point coordinate |
| 35.7 | AVAL_EN | BOOL | FALSE | 1 = Set actual value |
| 36.1 | ZOFF_EN | BOOL | FALSE | 1 = Set zero offset |
| 36.4 | DELDIAG_EN | BOOL | FALSE | 1 = delete diagnostic buffer |

#### Job status

The status of job execution can be read from the return value RET_VAL and activity bit JOBBUSY in the channel DB. The status of an individual job can be evaluated using the trigger bits, done bits, and error bits of this job.

|  | RET_VAL | JOBBUSY | Trigger bit _EN | Done bit _D | Error bit _ERR |
| --- | --- | --- | --- | --- | --- |
| Job active | 1 | 1 | 1 | 0 | 0 |
| Job completed without errors | 0 | 0 | 0 | 1 | 0 |
| Job completed with errors | -1 | 0 | 0 | 1 | 1 |
| Write job cancelled | -1 | 0 | 0 | 0 | 1 |

### Error classes (S7-300, S7-400)

This section contains information on the following topics:

- [Error class 1: Process error (S7-300, S7-400)](#error-class-1-process-error-s7-300-s7-400)
- [Error class 2: Operator error (S7-300, S7-400)](#error-class-2-operator-error-s7-300-s7-400)
- [Error class 4: Data error (S7-300, S7-400)](#error-class-4-data-error-s7-300-s7-400)
- [Error class 5: Machine data error (S7-300, S7-400)](#error-class-5-machine-data-error-s7-300-s7-400)
- [Error class 6: Increment table error (S7-300, S7-400)](#error-class-6-increment-table-error-s7-300-s7-400)
- [Error class 15: Messages (S7-300, S7-400)](#error-class-15-messages-s7-300-s7-400)
- [Error class 128: Diagnostics errors (S7-300, S7-400)](#error-class-128-diagnostics-errors-s7-300-s7-400)

#### Error class 1: Process error (S7-300, S7-400)

##### Description

Operating errors are detected asynchronously to an operation/control. These operating errors cause the positioning to be canceled, except in the case of error number 9, which leads to the shutdown of positioning.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 1 | **Software limit switch start overrun** |  | Yes |
| Cause | The actual value is outside the operating range. |  |  |
| 2 | **Software limit switch end overrun** |  | Yes |
| Cause | The actual value is outside the operating range. |  |  |
| 3 | **Traversing range start overrun** |  | Yes |
| Cause | Traversing range limit overrun (coordinates of the traversing range limits also belong to the traversing range). |  |  |
| 4 | **Traversing range end overrun** |  | Yes |
| Cause | Traversing range limit overrun (coordinates of the traversing range limits also belong to the traversing range). |  |  |
| 5 | **Error on target approach** |  | Yes |
| Cause | Target range has not been reached within the monitoring time. |  |  |
| 6 | **Standstill range exited** |  | Yes |
| Cause | The actual value lies outside of the standstill range. |  |  |
| 7 | **Positive feedback** |  | Yes |
| Cause | Actual value change &gt; ½ standstill range in the wrong direction. |  |  |
| 8 | **Missing or too slight actual value change** |  | Yes |
| Cause | No actual value change or an actual value change against the desired direction within the monitoring time. |  |  |
| 9 | **Target overrun (FM 451)** |  | Yes |
| Cause | The target has been overrun with "set actual value on-the-fly". |  |  |
| 10 | **Target range overrun** |  | Yes |
| Cause | Target range was overrun after target approach. |  |  |
| 11 | **Changeover point switched incorrectly** |  | Yes |
| Cause | Axis swinging in changeover point. |  |  |
| 12 | **Switch-off point switched incorrectly** |  | Yes |
| Cause | Axis swinging between switch-off / return point. |  |  |
| 13 | **Start of target range switched incorrectly** |  | Yes |
| Cause | Axis oscillating in the target range. |  |  |
| 14 | **Change greater than half the rotary axis range** |  | Yes |
| Cause | Velocity/frequency too high or faulty actual value steps. |  |  |
| 15 | **Change greater than the rotary axis range** |  | Yes |
| Cause | Velocity/frequency too high or faulty actual value steps. |  |  |
| 16 | **Increment for increment number 252 cannot be transferred (FM 451)** |  | Yes |
| Cause | The increment cannot be transferred. |  |  |
| 17 | **Increment for increment number 252 cannot be approached (FM 451)** |  | Yes |
| Cause | The distance between the current actual position and the specified increment is less than the changeover difference or switch-off difference. |  |  |
| 18 | **Incorrect increment for increment number 252 (FM 451)** |  | Yes |
| Cause | The increment lies outside of the operating range. |  |  |

#### Error class 2: Operator error (S7-300, S7-400)

##### Description

Operator errors are detected if there is change in the control signals in the user data range. Operator errors lead to the shutdown of positioning.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 1 | **Impermissible operating mode** |  | No |
| Cause | The chosen operating mode is inadmissible. |  |  |
| 3 | **Inadmissible interface job** |  | No |
| Cause | The selected signal is not permitted with this operating mode. |  |  |
| 4 | **Incorrect operating mode parameter** |  | No |
| Cause | - In "jog" mode, the velocity specification is not equal to the rapid traverse or creep speed. - In "incremental approach" mode, the increment is a value other than 1 - 100, 252, 254 or 255 |  |  |
| 5 | **Start enable not available** |  | No |
| Cause | Start enable not available upon start. |  |  |
| 7 | **Target / target range is outside the operating range** |  | No |
| Cause | Default or calculated target is outside the software limit switches. |  |  |
| 8 | **Axis parameters not assigned** |  | No |
| Cause | Incorrect machine data or no machine data has been assigned for the axis. |  |  |
| 9 | **Axis not synchronized** |  | No |
| Cause | The "incremental approach" mode is only possible with an already synchronized axis. |  |  |
| 10 | **Target / distance increment cannot be positioned** |  | No |
| Cause | The distance between the current actual position and the specified target is less than the switch-off difference. |  |  |
| 17 | **Reference point approach not possible** |  | No |
| Cause | An SSI encoder is connected. |  |  |
| 18 | **Relative or absolute incremental approach is not possible** |  | No |
| Cause | The increment is invalid. |  |  |
| 19 | **Switch-off difference is less than ½ the target range with increment number 255** |  | No |
| Cause | The switch-off difference for the increment number 255 is less than half the target range. |  |  |
| 20 | **Inadmissible travel in the specified direction** |  | No |
| Cause | Insufficient distance to the software limit switch. |  |  |

#### Error class 4: Data error (S7-300, S7-400)

##### Meaning

Operating errors are detected synchronously to an operation / control. Data errors do not trigger an error response.

| No. | Meaning |  |  | Diagnostics interrupt |
| --- | --- | --- | --- | --- |
| 6 | **Specified increment too great** |  |  | No |
| Cause |  | The value is outside the range of ±100 m or ±1000 m. The distance increment / target may not be greater than the traversing range.  For a rotary axis, the coordinate must be ≥ 0 and less than the end of the rotary axis. |  |  |
| 10 | **Zero offset error** |  |  | No |
| Cause |  | The zero offset is greater than ±100 m or ±1000 m.   After the zero offset, the software limit switches are positioned outside of the traversing range (-100 m to +100 m or -1000 m to +1000 m).  Rotary axis: The zero offset amount is greater than the end of the rotary axis. |  |  |
| 11 | **Incorrect actual value** |  |  | No |
| Cause |  | Linear axis: The coordinate is outside the current (possibly shifted) software limit switches.  Rotary axis: The coordinate is &lt; 0 or greater than the end of the rotary axis. |  |  |
| 12 | **Incorrect reference point** |  |  | No |
| Cause |  | Linear axis: The coordinate is outside the current (possibly shifted) software limit switches.  Rotary axis: The coordinate is &lt; 0 or greater than the end of the rotary axis. |  |  |
| 20 | **Enable machine data not permitted** |  |  | No |
| Cause | There are no new (error-free) machine data on the module. |  |  |  |
| 27 | **Unauthorized bit-coded setting** |  |  | No |
| Cause | Unused and, in this case, unwritten bits do not equal 0. |  |  |  |
| 29 | **Inadmissible bit coding** |  |  | No |
| Cause | Unused and, in this case, unwritten bits do not equal 0. |  |  |  |
| 34 | **Not possible to cancel set actual value** |  |  | No |
| Cause | With an SSI encoder and a linear axis, the actual position value would lie outside the operating range after making the setting. |  |  |  |
| 36 | **Incorrect changeover difference with the increment number 255** |  |  | No |
| Cause | The value lies outside the permissible range of numbers of ±100 m or ±1000 m.  For a rotary axis, the coordinate must be ≥ 0 and less than the end of the rotary axis. |  |  |  |
| 37 | **Incorrect switch-off difference with the increment number 255** |  |  | No |
| Cause | The value lies outside the permissible range of numbers of ±100 m or ±1000 m.  The switch-off difference must be less than the changeover difference. |  |  |  |
| 107 | **Axis parameters not assigned** |  |  | No |
| Cause | On the axis there is either no machine data or it has not been enabled. |  |  |  |
| 108 | **Axis not synchronized** |  |  | No |
| Cause |  | A "set actual value" or "set actual value on-the-fly" job was initiated although the axis is not synchronized. |  |  |

#### Error class 5: Machine data error (S7-300, S7-400)

##### Meaning

The diagnostic interrupt is only triggered in the event of a faulty system data block (SDB). Machine data errors do not trigger an error response.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 5 | **Error in hardware interrupt setting** |  | Yes |
| Cause | You have attempted to select a hardware interrupt that the module does not support. |  |  |
| 6 | **Incorrect minimum edge distance (FM 451)** |  | Yes |
| Cause | You have entered a value &lt; 0 or &gt; 10<sup>9</sup> µm as the minimum edge distance. |  |  |
| 7 | **Incorrect system of units** |  | Yes |
| Cause | The value for the system of units lies outside of the permissible range of 1 to 4 and 6. |  |  |
| 8 | **Incorrect axis type** |  | Yes |
| Cause | You have entered neither 0 nor 1 as an axis type. |  |  |
| 9 | **Incorrect end of the rotary axis** |  | Yes |
| Cause | The value for the end of the rotary axis is outside the valid range from 1 to 10<sup>9</sup> µm or from 1 to 10<sup>8</sup> µm (depending on the resolution). |  |  |
| 10 | **Incorrect encoder type** |  | Yes |
| Cause | The value for the encoder type lies outside of the permissible range of 1 to 4. |  |  |
| 11 | **Incorrect distance per encoder revolution** |  | Yes |
| Cause | The value for distance / encoder revolution is outside the valid range from 1 to 10<sup>9</sup> µm (regardless of the resolution). |  |  |
| 13 | **Invalid increments per encoder revolution** |  | Yes |
| 14 | **Incorrect number of revolutions** |  | Yes |
| 15 | **Incorrect transmission rate** |  | Yes |
| Cause | You have specified a transmission rate outside the permitted range of 0 to 3. |  |  |
| 16 | **Incorrect reference point coordinate** |  | Yes |
| Cause | The coordinate is outside the range from -100 m to +100 m or from 1000 m to +1000 m (depending on the resolution).  Linear axis: The coordinate lies outside of the operating range.   Rotary axis: The coordinate is &lt; 0 or greater than the end of the rotary axis. |  |  |
| 17 | **Incorrect absolute encoder adjustment** |  | Yes |
| Cause | SSI encoder: The value of the absolute encoder adjustment is not in the encoder range: (increments per encoder revolution x number of revolutions - 1). |  |  |
| 18 | **Incorrect type of reference point approach** |  | Yes |
| Cause | You have specified a value outside the permissible value set of 0, 1, 2 and 3. |  |  |
| 19 | **Incorrect counting direction** |  | Yes |
| Cause | You have specified a value outside of the permissible value quantities of 0 and 1. |  |  |
| 20 | **It is not possible to monitor the hardware** |  | Yes |
| Cause | You have set the monitoring of message frame errors in the parameter DB to "FALSE".  The encoder used does not support error pulse monitoring. Disable the MON_PULSE parameter. |  |  |
| 21 | **Incorrect software limit switch start** |  | Yes |
| Cause | Linear axis: The software limit switch start is outside the traversing range (-100 m to +100 m or -1000 m to +1000 m, depending on the resolution).  Linear axis: The software limit switch start (including any zero offset) is less than -100 m or -1000 m (depending on the resolution). |  |  |
| 22 | **Incorrect software limit switch end** |  | Yes |
| Cause | Linear axis: The software limit switch end is outside the traversing range (-100 m to +100 m or -1000 m to +1000 m, depending on the resolution) or less than the software limit switch start.  Linear axis: The software limit switch end (including any zero offset) is greater than +100 m or +1000 m (depending on the resolution). |  |  |
| 23 | **Incorrect maximum velocity** |  | Yes |
| Cause | The data not listed in the parameter DB must be 0. |  |  |
| 24 | **Incorrect target range** |  | Yes |
| Cause | Linear axis: Range from 0 to 100 m or 1000 m, depending on the resolution.  Rotary axis: Range greater than the end of the rotary axis. |  |  |
| 25 | **Incorrect monitoring time** |  | Yes |
| Cause | The value for the monitoring time lies outside the permissible range from 0 to 100 000 ms. |  |  |
| 26 | **Incorrect standstill range** |  | Yes |
|  | Cause | Linear axis: Range from 0 to 100 m or 1000 m, depending on the resolution.  Rotary axis: Range greater than the end of the rotary axis. |  |
| 127 | **Incorrect standstill velocity** |  | Yes |
| Cause | The value for the standstill velocity lies outside the permissible range from 0 to 100 000 µm/min. |  |  |
| 128 | **Incorrect control mode** |  | Yes |
| Cause | You have specified a value for the control mode that lies outside the permissible range of 1 to 4. |  |  |
| 129 | **Incorrect start velocity for the reference point approach** |  | Yes |
| Cause | You have entered neither 0 nor 1 as a start velocity. |  |  |
| 130 | **Incorrect changeover difference in the direction +** |  | Yes |
| Cause | Linear axis: Range from 0 to 100 m or 1000 m (depending on the resolution).  Rotary axis: Range greater than the end of the rotary axis or less than ½ the target range. |  |  |
| 131 | **Incorrect changeover difference in direction –** |  | Yes |
| Cause | Linear axis: Range from 0 to 100 m or 1000 m (depending on the resolution).  Rotary axis: Range greater than the end of the rotary axis or less than ½ the target range. |  |  |
| 132 | **Incorrect switch-off difference in direction**  + |  | Yes |
| Cause | The switch-off difference is greater than the plus changeover difference, less than ½ the target range or outside the valid range from 0 to 100 m or 0 to 1000 m (depending on resolution). |  |  |
| 133 | **Incorrect switch-off difference in direction**  – |  | Yes |
| Cause | The switch-off difference is greater than the minus changeover difference, less than ½ the target range or outside the valid range from 0 to 100 m or 0 to 1000 m (depending on resolution). |  |  |
| 200 | **Incorrect resolution** |  | Yes |
| Cause | You specified a resolution &lt; 0.1 µm/pulse or &gt; 1000 µm/pulse.  You specified a distance / encoder revolution and a number of pulses/encoder revolution, that results in a resolution of &lt; 0.1 or &gt; 1000. |  |  |
| 201 | **Encoder does not fit the operating range / rotary axis range** |  | Yes |
| Cause | SSI encoders and rotary axes: The encoder does not precisely cover the rotary axis range.  Linear axis: The encoder does not cover at least the operating range (including software limit switches). |  |  |

#### Error class 6: Increment table error (S7-300, S7-400)

##### Meaning

Increment dimension table errors do not trigger an error response.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 6 | **Specified increment in the incremental dimension table too great** |  | No |
| Cause | The value lies outside of ±100 m or ±1000 m.   The increment/target may not be greater than the traversing range.  For a rotary axis, the coordinate must be ≥ 0 and less than the end of the rotary axis. |  |  |

#### Error class 15: Messages (S7-300, S7-400)

##### Meaning

The messages do not trigger an error response.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 1 | **Start of parameter assignment** |  | No |
| Cause | The module has detected a parameter assignment via a system data block. |  |  |
| 2 | **End of parameter assignment** |  | No |
| Cause | The module has processed the parameter assignment via a system data block without errors. |  |  |
| 11 | **Distance to changeover point too short** |  | No |
| Cause | The hardware response times cannot be adhered to because the distance between the switching points is too short. |  |  |
| 12 | **Distance to reversal point too short** |  | No |
| Cause | The hardware response times cannot be adhered to because the distance between the switching points is too short. |  |  |
| 14 | **Distance to switch-off point too short** |  | No |
| Cause | The hardware response times cannot be adhered to because the distance between the switching points is too short. |  |  |
| 15 | **Distance to start of target range too short** |  | No |
| Cause | The hardware response times cannot be adhered to because the distance between the switching points is too short. |  |  |

#### Error class 128: Diagnostics errors (S7-300, S7-400)

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 4 | **External auxiliary voltage missing** |  | Yes |
| Cause | - External 24 V auxiliary voltage is not connected or has failed - The fuse on the module is defective - Undervoltage - Ground wire break - Short-circuit (for example, at the connected encoder) |  |  |
| Effect | - Positioning is cancelled on all channels. - Outputs are switched off - Synchronization is cancelled for incremental encoders when the auxiliary voltage for the encoder supply is missing - Module parameters not assigned. - Start enable is cleared |  |  |
| Remedy | Verify that the 24 V connection is correct (faulty module if 24 V connection is correct). |  |  |
| 5 | **Front connector missing (FM 451)** |  | Yes |
| Cause | Front connector of the positioning module is not connected. |  |  |
| Effect | - Missing external auxiliary 24 V voltage - Module is not ready |  |  |
| Correction | Plug the front connector into the positioning module |  |  |
| 51 | **Timeout monitoring responded (watchdog)** |  | Yes |
| Cause | - Module exposed to severe interference - Module error |  |  |
| Effect | - Module is reset - Turn off all outputs - If, after resetting the module, no module fault is detected, the module is ready for operation again - The module signals the watchdog timeout with "incoming" and "outgoing" |  |  |
| Correction | - Remedying interferences - Contact the relevant sales department who will require details of the circumstances leading to the error. - Replace the module |  |  |
| 144 | **Encoder wire break** |  | Yes |
| Cause | - The encoder cable has sheared off or is not plugged in - Encoders without cross signals - Incorrect pin assignment - Cable length too long - Encoder signals short-circuited - Encoder signal edge fault - Maximum input frequency of the encoder input has been exceeded - Sensor voltage supply failure |  |  |
| Effect | - The positioning is canceled - Turn off all outputs - Delete the synchronization with incremental encoders - Start enable is deleted |  |  |
| Correction | - Check encoder cable - Comply with encoder specification - Monitoring can be temporarily disabled at the responsibility of the operator using the programming interface. - Comply with the technical specifications of the module |  |  |
| 145 | **Absolute encoder message frame error** |  | Yes |
| Cause | Incorrect or interrupted message frame traffic between the module and the absolute encoder (SSI):  - The encoder cable has sheared off or is not plugged in - Incorrect encoder type - The encoder is incorrectly set (programmable encoder) - The message length has been incorrectly specified - The encoder is supplying incorrect values (encoder is faulty) - Interference on the measuring system cable - Chosen transmission rate is too high - Monoflop time of the encoder is greater than 64 µs |  |  |
| Effect | - Positioning is canceled - Shutdown of the outputs - Start enable is cleared |  |  |
| Correction | - Check encoder cable - Check encoder - Check the message frame traffic between the encoder and module |  |  |
| 146 | **Missing pulses of incremental encoder** |  | Yes |
| Cause | - Encoder monitoring has detected missing pulses - Number of increments per encoder revolution is incorrectly entered - Encoder faulty: does not return the defined number of pulses - incorrect or no zero mark - Crosstalk on the encoder cable |  |  |
| Effect | - Positioning is canceled - Shutdown of the outputs - Start enable is cleared |  |  |
| Remedy | - Enter the correct number of increments per encoder revolution (parameter assignment dialog) - Check the encoder and encoder cable - Comply with the shielding and grounding directives - Monitoring can be temporarily disabled at the responsibility of the operator using the programming interface. |  |  |
