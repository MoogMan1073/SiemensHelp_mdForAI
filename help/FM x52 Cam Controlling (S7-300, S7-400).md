---
title: "FM x52 Cam Controlling (S7-300, S7-400)"
package: ProgFBFMx52V2enUS
topics: 20
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# FM x52 Cam Controlling (S7-300, S7-400)

This section contains information on the following topics:

- [CAM_INIT (S7-300, S7-400)](#cam_init-s7-300-s7-400)
- [CAM_CTRL (S7-300, S7-400)](#cam_ctrl-s7-300-s7-400)
- [CAM_DIAG (S7-300, S7-400)](#cam_diag-s7-300-s7-400)
- [CAM_CTRL_452 (S7-300, S7-400)](#cam_ctrl_452-s7-300-s7-400)
- [CAM_DIAG_452 (S7-300, S7-400)](#cam_diag_452-s7-300-s7-400)
- [CAM_MSRM_452 (S7-300, S7-400)](#cam_msrm_452-s7-300-s7-400)
- [Additional references for FM x52 CAM V2 (S7-300, S7-400)](#additional-references-for-fm-x52-cam-v2-s7-300-s7-400)

## CAM_INIT (S7-300, S7-400)

### Description

The CAM_INIT instruction initializes the following data in the channel DB:

- The control signals
- The feedback signals
- The trigger, done and error bits of the jobs
- The function switches and their done and error bits
- Job management and the internal buffers for the [CAM_CTRL](#cam_ctrl-s7-300-s7-400) or [CAM_CTRL_452](#cam_ctrl_452-s7-300-s7-400) instruction
- Job management and the internal buffers for the [CAM_MSRM_452](#cam_msrm_452-s7-300-s7-400) instruction (FM 452 only)

### Call

The instruction must be executed after a startup, in other words, after the power supply to the module or CPU is switched on. Therefore, you should integrate the instruction in the restart organization block OB 100, for example, and plug/pull organization block OB 83 or call it in the initialization phase of your user program. Before you do that, enter the module address in the DB of OB 100. This ensures that your user program does not access obsolete data after a CPU or module restart.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the channel DB |

### Return values

The instruction does not provide a return value.

## CAM_CTRL (S7-300, S7-400)

### Description

You can call CAM_CTRL instruction to read operating data from the module, initialize the module and control the module in runtime. To complete such actions, use control signals, feedback signals, function switches as well as write and read commands.

### Operating principle

Each time it is called, the instruction performs the following actions:

- Read feedback signals:

  The CAM_CTRL instruction reads all feedback signals from the module and enters them in the channel DB. The control signals and commands are not processed unless this step is completed, which means that the feedback signals report the module status given prior to the instruction call.
- Write control signals:

  The control signals that are entered in the channel DB are transferred to the module. Enabling of cam processing, however, is delayed as long as the trigger for a "Set reference point" or "Write cam data" command is set. Activation (reactivation) of cam processing is delayed by this time period.
- [Command management](#job-management-cam_ctrl-s7-300-s7-400):

  The next command is executed based on the command trigger bits entered in the channel DB.

### Call

This instruction must be called at cyclic intervals.

Before calling the instruction, enter all the data necessary to execute the selected functions in the channel DB.

### Data blocks used

- [Channel DB](#channel-data-block-s7-300-s7-400):

  The channel DB is the instance DB of the instruction CAM_CTRL. The module address must be entered in the channel DB. .
- [Parameter DB](#parameter-data-block-s7-300-s7-400):

  To write or read machine or cam data using commands, you need a parameter DB whose number is entered in the channel DB. The parameter DB must be of sufficient length to handle the existing number of cams.

### Return values

The instruction provides the following return values in the RETVAL parameter of the channel DB:

| RETVAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | At least 1 command is active |
| 0 | 1 | No active command, no errors |
| -1 | 0 | Errors:  Data error (DAT_ERR) or   Communication error (JOB_ERR) has occurred |

### Startup

Call the [CAM_INIT](#cam_init-s7-300-s7-400) instruction at the startup of the module or CPU. This action includes a reset of the function switches.

The CAM_CTRL instruction acknowledges the module startup. During this time, RETVAL and JOBBUSY = 1.

### Reaction to error

If corrupt data was written by a write command, the module returns the feedback signal DATA_ERR = 1. If an error occurs during communication with the module for a write or read command, the cause of the error is written to the JOB_ERR parameter of the channel DB.

- Error with a write command:

  For the corrupt command, the trigger bit is reset, and error bit _ERR and done bit _D are set. The trigger bit is canceled and error bit _ERR is set for all pending write commands.

  The execution of the pending read commands is continued. JOB_ERR is retriggered accordingly for all commands.
- Error with a read command:

  For the corrupt command, the trigger bit is reset, and error bit _ERR and done bit _D are set.

  The execution of the pending read commands is continued. JOB_ERR is retriggered accordingly for all commands.

## CAM_DIAG (S7-300, S7-400)

### Description

Use the CAM_DIAG instruction to read the data from the diagnostics buffer of the module and make it available for display on the HMI system or for programmed evaluation.

### Operating principle

The instruction reads the diagnostics buffer if a new entry is displayed in the diagnostics buffer by feedback signal DIAG = 1. After the diagnostics buffer has been read, the module sets DIAG to 0.

### Call

This instruction must be called at cyclic intervals. Additional calls in an event-driven interrupt program are not allowed. To complete the execution of the instruction, you must call it at least twice (in 2 cycles).

### Data block used

[Diagnostics DB](#diagnostics-data-block-s7-300-s7-400):

The diagnostics DB is the instance DB of the instruction CAM_DIAG. The module address must be entered in the diagnostics DB. The address should entered in the startup OB (OB 100) or prior to its initial use. The most recent entry in the diagnostics buffer is written to the DIAG[1] structure and the oldest entry to the DIAG[4] structure.

### Return values

The instruction provides the following return values in the RETVAL parameter of the diagnostics DB:

| RETVAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | Command active |
| 0 | 1 | No active command, no errors |
| -1 | 0 | Errors |

### Commands

You can read the diagnostics buffer regardless of any new entry by setting the DIAGRD_EN trigger bit. After the diagnostics buffer has been read, the trigger bit is set to 0.

### Startup

The instruction does not run a startup routine.

### Reaction to error

The cause of a command error can be read from the JOB_ERR parameter of the diagnostics DB.

### Error classes

The error events are organized in the following error classes:

- [Error class 1: Operational errors](#error-class-1-operating-errors-s7-300-s7-400)
- [Error class 4: Data errors](#error-class-4-data-error-s7-300-s7-400)
- [Error class 5: Machine data errors](#error-class-5-machine-data-error-s7-300-s7-400)
- [Error class 7: Cam data errors](#error-class-7-cam-data-errors-s7-300-s7-400)
- [Error class 15: Messages](#error-class-15-messages-s7-300-s7-400)
- [Error class 128: Diagnostics errors](#error-class-128-diagnostics-errors-s7-300-s7-400)

## CAM_CTRL_452 (S7-300, S7-400)

### Description

You can call CAM_CTRL_452 instruction to read operating data from the module, initialize the module and control the module in runtime. To complete such actions, use control signals, feedback signals, function switches as well as write and read jobs.

### Operating principle

Each time it is called, the instruction performs the following actions:

- Read feedback signals:

  The CAM_CTRL_452 instruction reads all feedback signals from the module and enters them in the channel DB. The control signals and jobs are not processed unless this step is completed, which means that the feedback signals report the module status given prior to the instruction call.
- Write control signals:

  The control signals that are entered in the channel DB are transferred to the module. Enabling of cam processing, however, is delayed as long as the trigger for a "Set reference point" or "Write cam data" job is set. Activation (reactivation) of cam processing is delayed by this time period.
- [Job management](#job-management-cam_ctrl_452-s7-300-s7-400):

  The next job is executed based on the job trigger bits entered in the channel DB.

### Call

This instruction must be called at cyclic intervals.

Before calling the instruction, enter all the data necessary to execute the selected functions in the channel DB.

### Data blocks used

- [Channel DB](#channel-data-block-s7-300-s7-400):

  The module address must be entered in the channel DB.
- [Parameter DB](#parameter-data-block-s7-300-s7-400):

  To write or read machine or cam data using jobs, you need a parameter DB whose number is entered in the channel DB. The parameter DB must be of sufficient length to handle the existing number of cams.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the channel DB |
| RET_VAL | OUTPUT | INT | Return value |

### Return values

The instruction provides the following return values in the RET_VAL parameter of the channel DB:

| RET_VAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | At least 1 job is active |
| 0 | 1 | No active job, no errors |
| -1 | 0 | Errors:  Data error (DAT_ERR) or   Communication error (JOB_ERR) has occurred |

### Startup

Call the [CAM_INIT](#cam_init-s7-300-s7-400) instruction at the startup of the module or CPU. This action includes a reset the function switches.

The CAM_CTRL_452 instruction acknowledges the module startup. During this time, RET_VAL and JOBBUSY = 1.

### Reaction to errors

If corrupt data was written by a write job, the module returns the feedback signal DATA_ERR = 1. If an error occurs during communication with the module for a write or read job, the cause of the error is written to the JOB_ERR parameter of the channel DB.

- Write job errors:

  For the corrupt job, the trigger bit is reset, and error bit _ERR and done bit _D are set. The trigger bit is canceled and error bit _ERR is set for all pending write jobs.

  The execution of the pending read jobs is continued. JOB_ERR is retriggered accordingly for all jobs.
- Read job errors:

  For the corrupt job, the trigger bit is reset, and error bit _ERR and done bit _D are set.

  The execution of the pending read jobs is continued. JOB_ERR is retriggered accordingly for all jobs.

## CAM_DIAG_452 (S7-300, S7-400)

### Description

Use the CAM_DIAG_452 instruction to read the data from the diagnostics buffer of the module and make it available for display on the HMI system or for programmed evaluation.

### Operating principle

The instruction reads the diagnostics buffer if a new entry is displayed in the diagnostics buffer by feedback signal DIAG = 1. After the diagnostics buffer has been read, the module sets DIAG to 0.

### Call

This instruction must be called at cyclic intervals. Additional calls in an interrupt OB are not allowed. To complete the execution of the instruction, you must call it at least twice (in 2 cycles).

### Data block used

[Diagnostics DB](#diagnostics-data-block-s7-300-s7-400):

The module address must be entered in the diagnostics DB. The most recent entry in the diagnostics buffer is written to the DIAG[1] structure and the oldest entry to the DIAG[4] structure.

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

You can read the diagnostics buffer regardless of any new entry by setting the DIAGRD_EN trigger bit. After the diagnostics buffer has been read, the trigger bit is set to 0.

### Startup

The instruction does not run a startup routine.

### Reaction to errors

The cause of a job error can be read from the JOB_ERR parameter of the diagnostics DB.

### Error classes

The error events are organized in the following error classes:

- [Error class 1: Operating error](#error-class-1-operating-errors-s7-300-s7-400)
- [Error class 4: Data errors](#error-class-4-data-error-s7-300-s7-400)
- [Error class 5: Machine data errors](#error-class-5-machine-data-error-s7-300-s7-400)
- [Error class 7: Cam data errors](#error-class-7-cam-data-errors-s7-300-s7-400)
- [Error class 15: Messages](#error-class-15-messages-s7-300-s7-400)
- [Error class 128: Diagnostics errors](#error-class-128-diagnostics-errors-s7-300-s7-400)

## CAM_MSRM_452 (S7-300, S7-400)

### Description

Call the CAM_MSRM_452 instruction to immediately evaluate the length measurement or edge detection data of an FM 452 in the hardware interrupt OB.

### Call

The instruction is called in a hardware interrupt OB (for example, OB 40).

### Data block used

[Channel DB](#channel-data-block-s7-300-s7-400):

The module address must be entered in the channel DB. You should enter it in the startup OB (OB 100).

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the channel DB |
| RET_VAL | OUTPUT | INT | Return value |

### Return values

The instruction provides the following return values in the RET_VAL parameter of the channel DB:

| RET_VAL | BR | Description |
| --- | --- | --- |
| 1 | 1 | Job active |
| 0 | 1 | No active job, no errors |
| -1 | 0 | Errors |

### Measurement results and status information

The measurement results and status information are available in the channel DB:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 112.0 | BEG_VAL | DINT | L#0 | Initial value |
| 116.0 | END_VAL | DINT | L#0 | End value |
| 120.0 | LEN_VAL | DINT | L#0 | Length |
| 56.0 | JOB_ERR_M | INT | 0 | Communication errors |
| 58.0 | JOBBUSY_M | BOOL | FALSE | Job active |

### Startup

The instruction does not run a startup routine.

### Reaction to errors

The cause of a job error can be read from the JOB_ERR_M parameter of the channel DB.

## Additional references for FM x52 CAM V2 (S7-300, S7-400)

This section contains information on the following topics:

- [Channel data block (S7-300, S7-400)](#channel-data-block-s7-300-s7-400)
- [Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400)
- [Diagnostics data block (S7-300, S7-400)](#diagnostics-data-block-s7-300-s7-400)
- [Job management (CAM_CTRL) (S7-300, S7-400)](#job-management-cam_ctrl-s7-300-s7-400)
- [Job management (CAM_CTRL_452) (S7-300, S7-400)](#job-management-cam_ctrl_452-s7-300-s7-400)
- [Error classes (S7-300, S7-400)](#error-classes-s7-300-s7-400)

### Channel data block (S7-300, S7-400)

#### Purpose

The channel DB is the data interface between the user program and the electronic cam controller FM x52. It contains and saves all data necessary to control and operate the module.

#### Configuration

The channel DB is divided into different areas:

Channel DB

Addresses* / version switch

Control signals

Feedback signals

Function switches

Trigger bits for write jobs

Trigger bits for read jobs

Done bits

Error bits

Job management for instructions

Data for jobs

* You can enter the module address in the parameter assignment interface.

#### Content

The table below shows the content of the channel DB.

> **Note**
>
> Do not modify any data not listed in this table.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| **Addresses / version switch** |  |  |  |  |
| 0.0 | MOD_ADDR **(Enter!)** | INT | 0 | Module address |
| 2.0 | CH_NO | INT | 1 | Channel number (always 1) |
| 10.0 | PARADBNO | INT | -1 | Number of the parameter DB -1 = DB not available |
| 12.0 | FM_TYPE | BOOL | FALSE | 0 = FM 352 up to V4.0 1 = FM 452 or FM 352 V5.0 and higher |
| **Control signals** |  |  |  |  |
| 15.2 | DIR_M | BOOL | FALSE | 1 = simulation in negative direction |
| 15.3 | DIR_P | BOOL | FALSE | 1 = simulation in positive direction |
| 15.4 | CAM_EN | BOOL | FALSE | 1 = enable cam processing |
| 15.5 | CNTC0_EN | BOOL | FALSE | 1 = enable count function of counter cam track 0 |
| 15.6 | CNTC1_EN | BOOL | FALSE | 1 = enable count function of counter cam track 1 |
| 16.0 | TRACK_EN | WORD | W#16#0 | Enable cam tracks 0 to 15  Bit 0 = track 0 |
| **Feedback signals** |  |  |  |  |
| 22.2 | DIAG | BOOL | FALSE | 1 = diagnostic buffer modified |
| 22.4 | DATA_ERR | BOOL | FALSE | 1 = data error |
| 22.7 | PARA | BOOL | FALSE | 1 = module has parameters assigned |
| 23.4 | CAM_ACT | BOOL | FALSE | 1 = cam processing busy |
| 25.0 | SYNC | BOOL | FALSE | 1 = axis is synchronized |
| 25.1 | MSR_DONE | BOOL | FALSE | 1 = length measurement or edge detection completed |
| 25.2 | GO_M | BOOL | FALSE | 1 = axis moving in negative direction |
| 25.3 | GO_P | BOOL | FALSE | 1 = axis moving in positive direction |
| 25.4 | HYS | BOOL | FALSE | 1 = axis within the hysteresis range |
| 25.5 | FVAL_DONE | BOOL | FALSE | 1 = set actual value on-the-fly executed |
| 26.0 | ACT_POS | DINT | L#0 | Current position of axis |
| 30.0 | TRACK_OUT | DWORD | DW#16#0 | Current signals of tracks 0 to 31  Bit 0 = track 0 |
| **Function switches** |  |  |  |  |
| 34.0 | EDGE_ON | BOOL | FALSE | 1 = Edge detection on |
| 34.1 | SIM_ON | BOOL | FALSE | 1 = simulation on |
| 34.2 | MSR_ON | BOOL | FALSE | 1 = Length measurement on |
| 34.3 | REFTR_ON | BOOL | FALSE | 1 = retrigger reference point |
| 34.4 | SSW_OFF | BOOL | FALSE | 1 = Software limit switches disabled |
| **Trigger bits for write jobs** |  |  |  |  |
| 35.0 | MDWR_EN | BOOL | FALSE | 1 = write machine data |
| 35.1 | MD_EN | BOOL | FALSE | 1 = Enable machine data |
| 35.2 | AVALREM_EN | BOOL | FALSE | 1 = set actual value, cancel set actual value on-the-fly |
| 35.3 | CAM1WR_EN | BOOL | FALSE | 1 = write cam data 1   (cams 0 to 15) |
| 35.4 | CAM2WR_EN | BOOL | FALSE | 1 = write cam data 2   (cams 16 to 31) |
| 35.5 | CAM3WR_EN | BOOL | FALSE | 1 = write cam data 3   (cams 32 to 47) |
| 35.6 | CAM4WR_EN | BOOL | FALSE | 1 = write cam data 4   (cams 48 to 63) |
| 35.7 | CAM5WR_EN | BOOL | FALSE | 1 = write cam data 5   (cams 64 to 79) |
| 36.0 | CAM6WR_EN | BOOL | FALSE | 1 = write cam data 6   (cams 80 to 95) |
| 36.1 | CAM7WR_EN | BOOL | FALSE | 1 = write cam data 7   (cams 96 to 111) |
| 36.2 | CAM8WR_EN | BOOL | FALSE | 1 = write cam data 8   (cams 112 to 127) |
| 36.3 | REFPT_EN | BOOL | FALSE | 1 = set reference point coordinates |
| 36.4 | AVAL_EN | BOOL | FALSE | 1 = Set actual value |
| 36.5 | FVAL_EN | BOOL | FALSE | 1 = set actual value on-the-fly |
| 36.6 | ZOFF_EN | BOOL | FALSE | 1 = Set zero offset |
| 36.7 | CH01CAM_EN | BOOL | FALSE | 1 = write cam edge setting (1 cam) |
| 37.0 | CH16CAM_EN | BOOL | FALSE | 1 = Write setting for fast cam change (16 cams) |
| **Trigger bits for read jobs** |  |  |  |  |
| 37.1 | MDRD_EN | BOOL | FALSE | 1 = read machine data |
| 37.2 | CAM1RD_EN | BOOL | FALSE | 1 = read cam data 1   (cams 0 to 15) |
| 37.3 | CAM2RD_EN | BOOL | FALSE | 1 = read cam data 2   (cams 16 to 31) |
| 37.4 | CAM3RD_EN | BOOL | FALSE | 1 = read cam data 3   (cams 32 to 47) |
| 37.5 | CAM4RD_EN | BOOL | FALSE | 1 = read cam data 4   (cams 48 to 63) |
| 37.6 | CAM5RD_EN | BOOL | FALSE | 1 = read cam data 5   (cams 64 to 79) |
| 37.7 | CAM6RD_EN | BOOL | FALSE | 1 = read cam data 6   (cams 80 to 95) |
| 38.0 | CAM7RD_EN | BOOL | FALSE | 1 = read cam data 7   (cams 96 to 111) |
| 38.1 | CAM8RD_EN | BOOL | FALSE | 1 = read cam data 8   (cams 112 to 127) |
| 38.2 | MSRRD_EN | BOOL | FALSE | 1 = read measured values |
| 38.3 | CNTTRC_EN | BOOL | FALSE | 1 = read count values of counter cam tracks |
| 38.4 | ACTPOS_EN | BOOL | FALSE | 1 = read position and track data |
| 38.5 | ENCVAL_EN | BOOL | FALSE | 1 = read encoder values |
| 38.6 | CAMOUT_EN | BOOL | FALSE | 1 = read cam and track data |
| **Done bits for function switches** |  |  |  |  |
| 40.0 | EDGE_D | BOOL | FALSE | 1 = "activate edge detection" or "deactivate edge detection" completed |
| 40.1 | SIM_D | BOOL | FALSE | 1 = "activate simulation" or "deactivate simulation" completed |
| 40.2 | MSR_D | BOOL | FALSE | 1 = "activate length measurement" or "deactivate length measurement" completed |
| 40.3 | REFTR_D | BOOL | FALSE | 1 = "activate retrigger reference point" or "deactivate retrigger reference point" completed |
| 40.4 | SSW_D | BOOL | FALSE | 1 = "Enable software limit switches" or "Disable software limit switches" completed |
| **Done bits for write jobs** |  |  |  |  |
| 41.0 | MDWR_D | BOOL | FALSE | 1 = "write machine data" job completed |
| 41.1 | MD_D | BOOL | FALSE | 1 = "enable machine data" job completed |
| 41.2 | AVALREM_D | BOOL | FALSE | 1 = "cancel set actual value" or "cancel set actual value on-the-fly" completed |
| 41.3 | CAM1WR_D | BOOL | FALSE | 1 = "write cam data 1" job completed |
| 41.4 | CAM2WR_D | BOOL | FALSE | 1 = "write cam data 2" job completed |
| 41.5 | CAM3WR_D | BOOL | FALSE | 1 = "write cam data 3" job completed |
| 41.6 | CAM4WR_D | BOOL | FALSE | 1 = "write cam data 4" job completed |
| 41.7 | CAM5WR_D | BOOL | FALSE | 1 = "write cam data 5" job completed |
| 42.0 | CAM6WR_D | BOOL | FALSE | 1 = "write cam data 6" job completed |
| 42.1 | CAM7WR_D | BOOL | FALSE | 1 = "write cam data 7" job completed |
| 42.2 | CAM8WR_D | BOOL | FALSE | 1 = "write cam data 8" job completed |
| 42.3 | REFPT_D | BOOL | FALSE | 1 = "set reference point" job completed |
| 42.4 | AVAL_D | BOOL | FALSE | 1 = "set actual value" job completed |
| 42.5 | FVAL_D | BOOL | FALSE | 1 = "Set actual value on-the-fly" job completed |
| 42.6 | ZOFF_D | BOOL | FALSE | 1 = "set zero offset" job completed |
| 42.7 | CH01CAM_D | BOOL | FALSE | 1 = "change 1 cam" job completed |
| 43.0 | CH16CAM_D | BOOL | FALSE | 1 = "change 16 cams" completed (fast cam parameter change) |
| **Done bits for read jobs** |  |  |  |  |
| 43.1 | MDRD_D | BOOL | FALSE | 1 = "read machine data" job completed |
| 43.2 | CAM1RD_D | BOOL | FALSE | 1 = "read cam data 1" job completed |
| 43.3 | CAM2RD_D | BOOL | FALSE | 1 = "read cam data 2" job completed |
| 43.4 | CAM3RD_D | BOOL | FALSE | 1 = "read cam data 3" job completed |
| 43.5 | CAM4RD_D | BOOL | FALSE | 1 = "read cam data 4" job completed |
| 43.6 | CAM5RD_D | BOOL | FALSE | 1 = "read cam data 5" job completed |
| 43.7 | CAM6RD_D | BOOL | FALSE | 1 = "read cam data 6" job completed |
| 44.0 | CAM7RD_D | BOOL | FALSE | 1 = "read cam data 7" job completed |
| 44.1 | CAM8RD_D | BOOL | FALSE | 1 = "read cam data 8" job completed |
| 44.2 | MSRRD_D | BOOL | FALSE | 1 = "read measured values" job completed |
| 44.3 | CNTTRC_D | BOOL | FALSE | 1 = "read count values of counter cam tracks" job completed |
| 44.4 | ACTPOS_D | BOOL | FALSE | 1 = "read position and track data" job completed |
| 44.5 | ENCVAL_D | BOOL | FALSE | 1 = "read actual encoder value" job completed |
| 44.6 | CAMOUT_D | BOOL | FALSE | 1 = "read position and track data" job completed |
| **Error bits for function switches** |  |  |  |  |
| 46.0 | EDGE_ERR | BOOL | FALSE | 1 = error in "activate edge detection" or "deactivate edge detection" |
| 46.1 | SIM_ERR | BOOL | FALSE | 1 = error in "activate simulation" or "deactivate simulation" |
| 46.2 | MSR_ERR | BOOL | FALSE | 1 = error in "activate length measurement" or "deactivate length measurement" |
| 46.3 | REFTR_ERR | BOOL | FALSE | 1 = Error in "Enable retrigger reference point" or "Disable retrigger reference point" |
| 46.4 | SSW_ERR | BOOL | FALSE | 1 = Error in "Enable software limit switches" or "Disable software limit switches" |
| **Error bits for write jobs** |  |  |  |  |
| 47.0 | MDWR_ERR | BOOL | FALSE | 1 = error in "write machine data" job |
| 47.1 | MD_ERR | BOOL | FALSE | 1 = error in "activate machine data" job |
| 47.2 | AVALREM_ERR | BOOL | FALSE | 1 = error in "cancel set actual value" or "cancel set actual value on-the-fly" |
| 47.3 | CAM1WR_ERR | BOOL | FALSE | 1 = error in "write cam data 1" job |
| 47.4 | CAM2WR_ERR | BOOL | FALSE | 1 = error in "write cam data 2" job |
| 47.5 | CAM3WR_ERR | BOOL | FALSE | 1 = error in "write cam data 3" job |
| 47.6 | CAM4WR_ERR | BOOL | FALSE | 1 = error in "write cam data 4" job |
| 47.7 | CAM5WR_ERR | BOOL | FALSE | 1 = error in "write cam data 5" job |
| 48.0 | CAM6WR_ERR | BOOL | FALSE | 1 = error in "write cam data 6" job |
| 48.1 | CAM7WR_ERR | BOOL | FALSE | 1 = error in "write cam data 7" job |
| 48.2 | CAM8WR_ERR | BOOL | FALSE | 1 = error in "write cam data 8" job |
| 48.3 | REFPT_ERR | BOOL | FALSE | 1 = error in "set reference point" job |
| 48.4 | AVAL_ERR | BOOL | FALSE | 1 = error in "set actual value" job |
| 48.5 | FVAL_ERR | BOOL | FALSE | 1 = error in "set actual value on-the-fly" job |
| 48.6 | ZOFF_ERR | BOOL | FALSE | 1 = error in "set zero offset" job |
| 48.7 | CH01CAM_ERR | BOOL | FALSE | 1 = error in "change 1 cam" job |
| 49.0 | CH16CAM_ERR | BOOL | FALSE | 1 = error in "change 16 cams" (fast cam parameter change) |
| **Error bits for read jobs** |  |  |  |  |
| 49.1 | MDRD_ERR | BOOL | FALSE | 1 = error in "read machine data" job |
| 49.2 | CAM1RD_ERR | BOOL | FALSE | 1 = error in "read cam data 1" job |
| 49.3 | CAM2RD_ERR | BOOL | FALSE | 1 = error in "read cam data 2" job |
| 49.4 | CAM3RD_ERR | BOOL | FALSE | 1 = error in "read cam data 3" job |
| 49.5 | CAM4RD_ERR | BOOL | FALSE | 1 = error in "read cam data 4" job |
| 49.6 | CAM5RD_ERR | BOOL | FALSE | 1 = error in "read cam data 5" job |
| 49.7 | CAM6RD_ERR | BOOL | FALSE | 1 = error in "read cam data 6" job |
| 50.0 | CAM7RD_ERR | BOOL | FALSE | 1 = error in "read cam data 7" job |
| 50.1 | CAM8RD_ERR | BOOL | FALSE | 1 = error in "read cam data 8" job |
| 50.2 | MSRRD_ERR | BOOL | FALSE | 1 = error in "read measured values" job |
| 50.3 | CNTTRC_ERR | BOOL | FALSE | 1 = error in "read count values of counter cam tracks" job |
| 50.4 | ACTPOS_ERR | BOOL | FALSE | 1 = error in "read position and track data" job |
| 50.5 | ENCVAL_ERR | BOOL | FALSE | 1 = error in "read current encoder value" job |
| 50.6 | CAMOUT_ERR | BOOL | FALSE | 1 = Error in "Read cam and track data" job |
| **Job management for the instruction** **CAM_CTRL**  **or**  **CAM_CTRL_452** |  |  |  |  |
| 52.0 | JOB_ERR | INT | 0 | Communication errors |
| 54.0 | JOBBUSY | BOOL | FALSE | 1 = At least 1 job active |
| 54.1 | JOBRESET | BOOL | FALSE | 1 = Reset all error bits and done bits |
| **Job management for the instruction**  **CAM_MSRM_452** |  |  |  |  |
| 56.0 | JOB_ERR_M | INT | 0 | Communication errors |
| 58.0 | JOBBUSY_M | BOOL | FALSE | 1 = Job active |
| **Data for "Zero offset" job** |  |  |  |  |
| 86.0 | ZOFF | DINT | L#0 | Zero offset |
| **Data for "Set actual value" job** |  |  |  |  |
| 90.0 | AVAL | DINT | L#0 | Coordinate for "Set actual value" |
| **Data for "Set actual value on-the-fly" job** |  |  |  |  |
| 94.0 | FVAL | DINT | L#0 | Coordinate for "Set actual value on-the-fly" |
| **Data for "Set reference point" job** |  |  |  |  |
| 98.0 | REFPT | DINT | L#0 | Coordinate for "Set reference point" |
| **Data for "change cam edges" job** |  |  |  |  |
| 102.0 | CAM_NO | INT | 0 | Cam number |
| 104.0 | CAM_START | DINT | L#0 | Cam start |
| 108.0 | CAM_END | DINT | L#0 | Cam end |
| **Data for the "Length measurement / edge detection" job** |  |  |  |  |
| 112.0 | BEG_VAL | DINT | L#0 | Initial value |
| 116.0 | END_VAL | DINT | L#0 | End value |
| 120.0 | LEN_VAL | DINT | L#0 | Length |
| **Data for the "read count values" job** |  |  |  |  |
| 124.0 | CNT_TRC0 | INT | 0 | Current count value of counter cam track 0 |
| 126.0 | CNT_TRC1 | INT | 0 | Current count value of counter cam track 1 |
| **Data for the "read position and track data" job** |  |  |  |  |
| 128.0 | ACTPOS | DINT | L#0 | Current position |
| 132.0 | ACTSPD | DINT | L#0 | Actual velocity |
| 136.0 | TRACK_ID | DWORD | DW#16#0 | Track identifier bits of tracks 0 to 31 |
| **Data for the "read encoder data" job** |  |  |  |  |
| 140.0 | ENCVAL | DINT | L#0 | Encoder value |
| 144.0 | ZEROVAL | DINT | L#0 | Count value at the last zero mark |
| 148.0 | ENC_ADJ | DINT | L#0 | Absolute encoder adjustment |
| **Data for the "read cam and track data" job** |  |  |  |  |
| 152.0 | CAM_00_31 | DWORD | DW#16#0 | Cam identifier bits for cams 0 to 31 |
| 156.0 | CAM_32_63 | DWORD | DW#16#0 | Cam identifier bits for cams 32 to 63 |
| 160.0 | CAM_64_95 | DWORD | DW#16#0 | Cam identifier bits for cams 64 to 95 |
| 164.0 | CAM_96_127 | DWORD | DW#16#0 | Cam identifier bits for cams 96 to 127 |
| 168.0 | TRACK_ID1 | DWORD | DW#16#0 | Track identifier bits of tracks 0 to 31 |
| 172.0 | ACTPOS1 | DINT | L#0 | Current position |
| **Data for the "fast cam parameter change" job** |  |  |  |  |
| 176.0 | C_QTY | BYTE | B#16#0 | Number of cams to modify |
| 177.0 | DIS_CHECK | BOOL | FALSE | 1 = disable data check |
| 180.0 | CAM | ARRAY [0...15]  STRUCT |  | Note:  The following structure must be completed for each cam to be modified |
| **Relative address** |  |  |  |  |
| +0.0 | CAM_NO | BYTE | B#16#0 | Number of the cam to modify |
| +1.0 | C_EFFDIR | BOOL | FALSE | 1 = change the activation direction |
| +1.1 | C_CBEGIN | BOOL | FALSE | 1 = change the cam start to the value CBEGIN (new cam start) |
| +1.2 | C_CEND | BOOL | FALSE | 1 = change the cam end / activation time to the value CEND (new cam end) |
| +1.3 | C_LTIME | BOOL | FALSE | 1 = change the lead time to the LTIME value (new lead time) |
| +1.4 | CAM_OFF | BOOL | FALSE | 1 = deactivate the cam during the cam change |
| +1.5 | EFFDIR_P | BOOL | FALSE | 1 = new effective direction positive (plus) |
| +1.6 | EFFDIR_M | BOOL | FALSE | 1 = new effective direction negative (minus) |
| +2.0 | CBEGIN | DINT | L#0 | New cam start |
| +6.0 | CEND | DINT | L#0 | New cam end / new activation time |
| +10.0 | LTIME | INT | 0 | New lead time |

### Parameter data block (S7-300, S7-400)

#### Purpose

The machine and cam data is stored in the parameter DB. The parameters can be changed from the user program or from an HMI system. The modified data can be imported to the parameter assignment interface and displayed there. You can export data displayed in the parameter assignment interface to a parameter DB.

A module can contain several parameter data sets (for example, for different recipes) that can be selected from the program.

#### Configuration

| Symbol | Meaning |
| --- | --- |
| **Parameter DB** |  |
| CAM_P016TYPE (UDT3)  Machine data  Data of cams 0 to 15 |  |
| CAM_P032TYPE (UDT4)  Machine data  Data of cams 0 to 31 |  |
| CAM_P064TYPE (UDT5)  Machine data  Data of cams 0 to 63 |  |
| CAM_P0128TYPE (UDT6)  Machine data  Data of cams 0 to 127 |  |

#### Content

The table below shows the content of the parameter DB.

> **Note**
>
> You may not change any data not listed in this table.

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| **Machine data** |  |  |  |  |
| 3.1 | PI_MEND | BOOL | FALSE | - FM 352: 0 - FM 452: 1: Enable hardware interrupt: Full scale value |
| 3.2 | PI_CAM | BOOL | FALSE | 1: Enable hardware interrupt: Cam on/off |
| 3.5 | PI_MSTRT | BOOL | FALSE | - FM 352: 0 - FM 452: 1: Enable hardware interrupt: Start of measurement |
| 4.0 | EDGEDIST | DINT | L#0 | Minimum edge distance for edge detection |
| 8.0 | UNITS | DINT | L#1 | Physical units system |
| 12.0 | AXIS_TYPE | DINT | L#0 | 0: Linear axis, 1: Rotary axis |
| 16.0 | ENDROTAX | DINT | L#100 000 | End of rotary axis |
| 20.0 | ENC_TYPE | DINT | L#1 | Encoder type, frame length |
| 24.0 | DISP_REV | DINT | L#80 000 | Distance per encoder revolution |
| 32.0 | INC_REV | DINT | L#500 | Increments per encoder revolution |
| 36.0 | NO_REV | DINT | L#1024 | Number of encoder revolutions |
| 40.0 | BAUDRATE | DINT | L#0 | Transmission rate |
| 44.0 | REFPT | DINT | L#0 | Reference point coordinate |
| 48.0 | ENC_ADJ | DINT | L#0 | Absolute encoder adjustment |
| 52.0 | RETR_TYPE | DINT | L#0 | Mode for "Retrigger reference point" |
| 59.0 | CNT_DIR | DINT | L#0 | Count direction:  0: normal, 1: inverted |
| 63.0 | MON_WIRE | BOOL | TRUE | 1: Wire-break monitoring |
| 63.1 | MON_FRAME | BOOL | TRUE | 1: Message frame error monitoring |
| 63.2 | MON_PULSE | BOOL | TRUE | 1: Missing pulse monitoring |
| 64.0 | SSW_STRT | DINT | L#-100 000 000 | Software limit switch start |
| 68.0 | SSW_END | DINT | L#100 000 000 | Software limit switch end |
| 76.0 | C_QTY | DINT | L#0 | Number of cams: 0, 1, 2, 3 = max. 16, 32, 64, 128 cams |
| 80.0 | HYS | DINT | L#0 | Hysteresis |
| 84.0 | SIM_SPD | DINT | L#0 | Simulation velocity |
| 90.0 | TRACK_OUT | WORD | W#16#0 | Control of track outputs:   0 = cam controller, 1 = CPU;   Bit number = track number |
| 95.0 | EN_IN_I3 | BOOL | FALSE | Enable input I3 |
| 95.1 | EN_IN_I4 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I4 |
| 95.2 | EN_IN_I5 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I5 |
| 95.3 | EN_IN_I6 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I6 |
| 95.4 | EN_IN_I7 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I7 |
| 95.5 | EN_IN_I8 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I8 |
| 95.6 | EN_IN_I9 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I9 |
| 95.7 | EN_IN_I10 | BOOL | FALSE | - FM 352: 0 - FM 452: Enable input I10 |
| 99.0 | SPEC_TRC0 | BOOL | FALSE | 1 = track 0 is counter cam track |
| 99.1 | SPEC_TRC1 | BOOL | FALSE | 1 = track 1 is counter cam track |
| 99.2 | SPEC_TRC2 | BOOL | FALSE | 1 = track 2 is brake cam track |
| 100.0 | CNT_LIM0 | DINT | L#2 | High count value for counter cam track 0 |
| 104.0 | CNT_LIM1 | DINT | L#2 | High count value for counter cam track 1 |
| **Data for cams 0 to 15 / 0 to 31 / 0 to 63 / 0 to 127** |  |  |  |  |
| 108.0 |  | STRUCT |  | (12 bytes length per element) |
| **Relative address** |  |  |  |  |
| +0.0 | CAMVALID | BOOL | FALSE | 1: Cam valid |
| +0.1 | EFFDIR_P | BOOL | TRUE | 1: Positive effective direction (plus) |
| +0.2 | EFFDIR_M | BOOL | TRUE | 1: Negative effective direction (minus) |
| +0.3 | CAM_TYPE | BOOL | FALSE | 0: Distance cam, 1: Time-based cam |
| +0.4 | PI_SW_ON | BOOL | FALSE | 1: Hardware interrupt on activation |
| +0.5 | PI_SW_OFF | BOOL | FALSE | 1: Hardware interrupt on deactivation |
| +1.0 | TRACK_NO | BYTE | B#16#0 | Track number |
| +2.0 | CBEGIN | DINT | L#-100 000 000 | Cam start |
| +6.0 | CEND | DINT | L#100 000 000 | End of output cam / activation time |
| +10.0 | LTIME | INT | 0 | Lead time |

### Diagnostics data block (S7-300, S7-400)

#### Purpose

The diagnostics DB is the storage location for the [CAM_DIAG](#cam_diag-s7-300-s7-400) or [CAM_DIAG_452](#cam_diag_452-s7-300-s7-400) instruction. It contains the module's diagnostics buffer which is processed by the instruction.

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
| 0.0 | MOD_ADDR **(Enter!)** | INT | 0 | Module address |
| 256.0 | JOB_ERR | INT | 0 | Communication errors |
| 258.0 | JOBBUSY | BOOL | FALSE | 1 = job active |
| 258.1 | DIAGRD_EN | BOOL | FALSE | 1 = read diagnostic buffer unconditional |
| 260.0 | DIAG_CNT | INT | 0 | Number of valid entries in the list |
| 262.0 | DIAG[1] | STRUCT |  | Diagnostic data latest entry |
| 272.0 | DIAG[2] | STRUCT |  | Diagnostic data second entry |
| 282.0 | DIAG[3] | STRUCT |  | Diagnostic data third entry |
| 292.0 | DIAG[4] | STRUCT |  | Diagnostic data oldest entry |

#### Structure of the Diagnostic Entry

The table below shows the structure of a diagnostics entry DIAG[n].

| Address | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| +0.0 | STATE | BOOL | FALSE | 0 = outgoing event 1 = incoming event |
| +0.1 | INTF | BOOL | FALSE | 1 = Internal error |
| +0.2 | EXTF | BOOL | FALSE | 1 = external error |
| +2.0 | FCL | INT | 0 | Error class: 1: Operating error 4: Data error 5: Machine data error 7: Cam data error 15: Messages 128: Diagnostics errors |
| +4.0 | FNO | INT | 0 | Error number 0 ... 255 |
| +6.0 | CH_NO | INT | 0 | Channel number (always 1) |
| +8.0 | CAMNO | INT | 0 | Cam numbers 0 to 127 with error class = cam data error |

### Job management (CAM_CTRL) (S7-300, S7-400)

#### Jobs

Data communication with the module other than the transfer of control and feedback signals is handled by means of jobs.

To initiate a job, set the corresponding trigger bit in the channel DB, including the corresponding data for write jobs. To execute the job, call the [CAM_CTRL](#cam_ctrl-s7-300-s7-400) instruction.

If operating the module centrally, read jobs are executed immediately. If you use the FM 352 in a distributed configuration, a read job may need several cycles.

Due to the required confirmations from the module, a write job requires at least 3 calls (or OB cycles). If you use the FM 352 in a distributed system, a write job may take more than 3 calls.

You can send several jobs at the same time, if necessary, along with control signals. With the exception of the job for writing the function switches, the jobs are executed in the order of the trigger bits specified in the channel DB. When a job is completed, the trigger bit is reset. The next job pending is identified and executed at the next call of the instruction.

In addition to a trigger bit, all jobs are provided a done bit and an error bit. These are distinguished by their name extension:

| Bit | Extension |
| --- | --- |
| Trigger bit | _EN ("enable") |
| Done bit | _D ("done") |
| Error bit | _ERR ("error") |

Done and error bits of the job should be set to 0 after they are evaluated or before this job is initiated.

When you set the JOBRESET bit, all done and error bits are reset before pending jobs are executed. The JOBRESET bit is then reset to 0.

#### Function switches

The function switches enable and disable module states. A job for writing the function switches is only executed when there is a change to a switch setting. The setting of the function switch is retained after the job has been executed.

Length measurements and edge detection cannot be activated concurrently. For this reason, the CAM_CTRL instruction makes sure that when one of the function switches is enabled, the other is disabled. However, if you enable both function switches (0 → 1), the length measurement is enabled.

Function switches and jobs can be used concurrently at the call of CAM_CTRL.

As with the jobs, the function switches are provided done bits with the name extension _D and error bits with the name extension _ERR.

To be able to evaluate the done and error bits, you should set these bits to 0 when changing a function switch.

#### Job status

The status of job execution can be read from the return value RETVAL and activity bit JOBBUSY in the channel DB. You can evaluate the status of a single job based on its trigger, done and error bits.

|  | RETVAL | JOBBUSY | Trigger bit _EN | Done bit _D | Error bit _ERR |
| --- | --- | --- | --- | --- | --- |
| Job active | 1 | 1 | 1 | 0 | 0 |
| Job completed without errors | 0 | 0 | 0 | 1 | 0 |
| Job completed with errors | -1 | 0 | 0 | 1 | 1 |
| Write job cancelled | -1 | 0 | 0 | 0 | 1 |

### Job management (CAM_CTRL_452) (S7-300, S7-400)

#### Jobs

Data communication with the module other than the transfer of control and feedback signals is handled by means of jobs.

To initiate a command, set the corresponding trigger bit in the channel DB, including the corresponding data for write jobs. To execute the command, call the [CAM_CTRL_452](#cam_ctrl_452-s7-300-s7-400) instruction.

A read command is executed immediately. Due to the required confirmations from the module, a write command requires at least 3 calls (or OB cycles).

You can send several jobs at the same time, if necessary, along with control signals. With the exception of the command for writing the function switches, the jobs are executed in the order of the trigger bits specified in the channel DB. When a command is completed, the trigger bit is reset. The next command pending is identified and executed at the next call of the instruction.

In addition to a trigger bit, all jobs are provided a done bit and an error bit. These are distinguished by their name extension:

| Bit | Extension |
| --- | --- |
| Trigger bit | _EN ("enable") |
| Done bit | _D ("done") |
| Error bit | _ERR ("error") |

Done and error bits of the command should be set to 0 after they are evaluated or before this command is initiated.

When you set the JOBRESET bit, all done and error bits are reset before pending jobs are executed. The JOBRESET bit is then reset to 0.

#### Function switches

The function switches enable and disable module states. A command for writing the function switches is only executed when there is a change to a switch setting. The setting of the function switch is retained after the command has been executed.

Length measurements and edge detection cannot be activated concurrently. For this reason, the CAM_CTRL_452 instruction makes sure that when one of the function switches is enabled, the other is disabled. However, if you enable both function switches (0 → 1), the length measurement is enabled.

Function switches and jobs can be used concurrently at the call of CAM_CTRL_452.

As with the jobs, the function switches are provided done bits with the name extension _D and error bits with the name extension _ERR.

To be able to evaluate the done and error bits, you should set these bits to 0 when changing a function switch.

#### Command status

The status of command execution can be read from the return value RET_VAL and activity bit JOBBUSY in the channel DB. You can evaluate the status of a single command based on its trigger, done and error bits.

|  | RET_VAL | JOBBUSY | Trigger bit _EN | Done bit _D | Error bit _ERR |
| --- | --- | --- | --- | --- | --- |
| Command active | 1 | 1 | 1 | 0 | 0 |
| Command completed without errors | 0 | 0 | 0 | 1 | 0 |
| Command completed with errors | -1 | 0 | 0 | 1 | 1 |
| Write command cancelled | -1 | 0 | 0 | 0 | 1 |

### Error classes (S7-300, S7-400)

This section contains information on the following topics:

- [Error class 1: Operating errors (S7-300, S7-400)](#error-class-1-operating-errors-s7-300-s7-400)
- [Error class 4: Data error (S7-300, S7-400)](#error-class-4-data-error-s7-300-s7-400)
- [Error class 5: Machine data error (S7-300, S7-400)](#error-class-5-machine-data-error-s7-300-s7-400)
- [Error class 7: Cam data errors (S7-300, S7-400)](#error-class-7-cam-data-errors-s7-300-s7-400)
- [Error class 15: Messages (S7-300, S7-400)](#error-class-15-messages-s7-300-s7-400)
- [Error class 128: Diagnostics errors (S7-300, S7-400)](#error-class-128-diagnostics-errors-s7-300-s7-400)

#### Error class 1: Operating errors (S7-300, S7-400)

##### Description

Operating errors are detected asynchronously to an operator input/control.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 1 | **Software limit switch start overrun** |  | Yes |
| 2 | **Software limit switch end overrun** |  | Yes |
| 3 | **Traversing range start overrun** |  | Yes |
| 4 | **Traversing range end overrun** |  | Yes |
| 13 | **Set actual value on-the-fly cannot be executed** |  | Yes |
| Cause | After you set the actual value on-the-fly, the software limit switches are outside the traversing range  (-100 m to +100 m or -1000 m to +1000 m).   The offset derived from the set actual value/set actual value on-the-fly operation is greater than ± 100 m or ± 1000 m. |  |  |
| Effect | Axis not synchronized. |  |  |

#### Error class 4: Data error (S7-300, S7-400)

##### Description

Data errors are detected synchronously to an operator input/control.

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 10 | **Incorrect zero offset** |  | No |
| Cause | The zero offset is greater than ±100 m or ±1000 m.   After the zero offset, the software limit switches are outside the traversing range (-100 m to +100 m or -1000 m to +1000 m).   Rotary axis: The zero offset amount is greater than the end of the rotary axis. |  |  |
| 11 | **Incorrect actual value specification** |  | No |
| Cause | Linear axis: The coordinate is outside the current (possibly shifted) software limit switches.  Rotary axis: The coordinate is < 0 or greater than the end of the rotary axis. |  |  |
| 12 | **Incorrect reference position** |  | No |
| Cause | Linear axis: The coordinate is outside the current (possibly shifted) software limit switches.  Rotary axis: The coordinate is < 0 or greater than the end of the rotary axis. |  |  |
| 20 | **Enable machine data not permitted** |  | No |
| Cause | There is no new (error-free) machine data on the module |  |  |
| 21 | **Set actual value on-the-fly not permitted** |  | No |
| Cause | An attempt was made to execute "Set actual value on-the-fly" while "Retrigger reference point" was enabled. |  |  |
| 27 | **Invalid bit-coded setting** |  | No |
| Cause | Unused and, in this case, unwritten bits do not equal 0.  An attempt was made to select "length measurement" and "edge detection" at the same time. |  |  |
| 28 | **Retrigger reference point is not permitted** |  | No |
| Cause | An attempt was made to execute "Retrigger reference point" while "Set actual value on-the-fly" was active.  An attempt was made to execute "Retrigger reference point" with an SSI encoder. |  |  |
| 29 | **Invalid bit-coded command** |  | No |
| Cause | Unused and, in this case, unwritten bits do not equal 0. |  |  |
| 30 | **Incorrect lead time** |  | No |
| 31 | **Incorrect cam number** |  | No |
| Cause | Cam is invalid  The cam number is not in the range from 0 to 127. |  |  |
| 32 | **Incorrect cam start** |  | No |
| Cause | The cam start is outside the traversing range  (-100 m to +100 m or -1000 m to +1000 m).  Rotary axis: Cam start is < 0 or greater than the end of the rotary axis. |  |  |
| 33 | **Incorrect cam end / cam activation time** |  | No |
| Cause | The cam end is outside the traversing range  (-100 m to +100 m or -1000 m to +1000 m).  Rotary axis: The cam end is < 0 or greater than the end of the rotary axis.   The cam is not activated at least for the duration of one pulse.  With an inverse cam, there are not at least 4 pulses between the cam start and cam end. |  |  |
| 34 | **Cancel set actual value not possible** |  | No |
| Cause | The actual position value would be outside the working range with an SSI encoder and linear axis after making the setting. |  |  |
| 35 | **Incorrect actual value specified by "Set actual value" / "Set actual value on-the-fly"** |  | No |
| Cause | The specified actual value is outside the valid number range of ±100 m or ±1000 m.   If this setting is made, the software limit switches would be outside the traversing range (-100 m to +100 m or -1000 m to +1000 m).   The offset derived from set actual value / set actual value on-the-fly would be greater than ±100 m or ±1000 m. |  |  |
| 107 | **Axis parameters not assigned** |  | No |
| Cause | No machine data on the axis.  No machine data activated on the axis. |  |  |
| 108 | **Axis not synchronized** |  | No |
| Cause | One of the settings "Set actual value" or "Set actual value on-the-fly" was initiated although the axis is not synchronized. |  |  |
| 109 | **Cam processing active.** |  | No |
| 110 | **Incorrect number of cams to be modified** |  | No |

#### Error class 5: Machine data error (S7-300, S7-400)

##### Description

A diagnostics interrupt is only triggered if an error is detected in the system data block (SDB).

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 5 | **Error in hardware interrupt setting** |  | Yes |
| Cause | You have attempted to select a hardware interrupt that the module does not support. |  |  |
| 6 | **Incorrect minimum edge distance** |  | Yes |
| Cause | You have entered a value <0 or >10<sup>9</sup> µm as the minimum edge distance |  |  |
| 8 | **Incorrect axis type** |  | Yes |
| Cause | You have specified neither 0, nor 1 as the axis type |  |  |
| 9 | **Incorrect end of the rotary axis** |  | Yes |
| Cause | The value for the end of the rotary axis is outside the valid range from 1 to 10<sup>9</sup> µm or from 1 to 10<sup>8</sup> µm (depending on the resolution). |  |  |
| 10 | **Incorrect encoder type** |  | Yes |
| Cause | The value for the encoder type is outside the valid range from 1 to 10 |  |  |
| 11 | **Incorrect distance / encoder revolution** |  | Yes |
| Cause | The value for distance / encoder revolution is outside the valid range from 1 to 10<sup>9</sup> µm (regardless of the resolution). |  |  |
| 13 | **Incorrect number of increments / encoder revolution** |  | Yes |
| 14 | **Incorrect number of revolutions** |  | Yes |
| 15 | **Incorrect transmission rate** |  | Yes |
| Cause | You specified a transmission rate outside the valid range from 0 to 3. |  |  |
| 16 | **Incorrect reference point coordinate** |  | Yes |
| Cause | The coordinate is outside the range from -100 m to +100 m or -1000 m to +1000 m, depending on the resolution.  Linear axis: The coordinate is outside the operating range.   Rotary axis: The coordinate is < 0 or greater than the end of the rotary axis. |  |  |
| 17 | **Incorrect absolute encoder adjustment** |  | Yes |
| Cause | SSI encoder: The value of the absolute encoder adjustment is not in the encoder range: (increments per encoder revolution x number of revolutions - 1). |  |  |
| 18 | **Incorrect mode for "Retrigger reference point"** |  | Yes |
| Cause | You specified a value outside the valid quantity of 0, 1, 6 and 7. |  |  |
| 19 | **Incorrect direction adaptation** |  | Yes |
| Cause | You have specified a value other than the valid 0 and 1. |  |  |
| 20 | **Hardware monitoring not possible** |  | Yes |
| Cause | You set message frame error monitoring = FALSE at the parameter DB.  Encoder does not support error pulse monitoring (disable MON_PULSE) |  |  |
| 21 | **Incorrect software limit switch start** |  | Yes |
| Cause | Linear axis: The software limit switch start is outside the traversing range (-100 m to +100 m or -1000 m to +1000 m, depending on the resolution).  Linear axis: The software limit switch start (including any zero offset) is less than -100 m or -1000 m (depending on the resolution). |  |  |
| 22 | **Incorrect software limit switch end** |  | Yes |
| Cause | Linear axis: The software limit switch end is outside the traversing range (-100 m to +100 m or 1000 m to +1000 m, depending on the resolution) or less than the software limit switch start.  Linear axis: The software limit switch end (including any zero offset) is greater than +100 m or +1000 m (depending on the resolution). |  |  |
| 144 | **Incorrect quantity structure** |  | Yes |
| Cause | You have specified a quantity structure other than 0 to 3. |  |  |
| 145 | **Incorrect hysteresis** |  | Yes |
| Cause | The hysteresis is outside the range 0 to 65535 × resolution.   The hysteresis is greater than ¼ × the working range or ¼ × the rotary axis range. |  |  |
| 146 | **Incorrect simulation velocity** |  | Yes |
| Cause | The simulation velocity is outside the range 1000 × RES to 3 × 10<sup>7</sup> × RES or is greater than 5 × 10<sup>8 </sup>µm/min.  The simulation velocity cannot be set internally. |  |  |
| 147 | **Incorrect track** |  | Yes |
| Cause | Activation of a track outside 0 to 15 (bits 0 to 15) was selected. |  |  |
| 148 | **Incorrect selection of enable inputs** |  | Yes |
| Cause | You wanted to enable a track outside 3 to 10 (bits 0 to 7) using an external signal. |  |  |
| 149 | **Incorrect selection of special tracks** |  | Yes |
| Cause | You wanted to define a track outside 0, 1 and 2 (bits 0, 1 and 2) as a special track |  |  |
| 150 | **Incorrect high count value track 0** |  | Yes |
| Cause | You have specified a count value < 2 or > 65535 as the high count value. |  |  |
| 151 | **Incorrect high count value track 1** |  | Yes |
| Cause | You have specified a count value < 2 or > 65535 as the high count value. |  |  |
| 200 | **Incorrect resolution** |  | Yes |
| Cause | You have specified a resolution < 0.1 µm/pulse or >1000 µm/pulse.  You specified a distance / encoder revolution and a number of pulses / encoder revolutions, that results in a resolution of < 0.1 or > 1000. |  |  |
| 201 | **Encoder does not match the operating range / rotary axis range** |  | Yes |
| Cause | SSI encoder and rotary axis: The encoder does not precisely cover the rotary axis range.  Linear axis: The encoder does not cover at least the operating range (including software limit switches). |  |  |

#### Error class 7: Cam data errors (S7-300, S7-400)

##### Description

A diagnostics interrupt is only triggered if an error is detected in the system data block (SDB).

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 1 | **Invalid hardware interrupt** |  | Yes |
| Cause | You attempted to define a hardware interrupt for a cam with a cam number > 7. |  |  |
| 2 | **Incorrect track number** |  | Yes |
| Cause | The track number is outside the range from 0 to 31 |  |  |
| 3 | **Incorrect cam start** |  | Yes |
| Cause | The cam start is outside the traversing range  (-100 m to +100 m or -1000 m to +1000 m).  Rotary axis: Cam start is < 0 or greater than the end of the rotary axis. |  |  |
| 4 | **Incorrect cam end** |  | Yes |
| Cause | The cam end is outside the traversing range  (-100 m to +100 m or -1000 m to +1000 m).  The cam length is not at least 1 pulse.   Rotary axis: The cam end is < 0 or greater than the end of the rotary axis.   With an inverse cam, there are not at least 4 pulses between the cam start and cam end. |  |  |
| 5 | **Incorrect activation time** |  | Yes |
| Cause | The activation time is < 0 µs. The maximum value depends on the quantity structure. |  |  |
| 6 | **Incorrect lead time**  <sup>1)</sup> |  | Yes |
| Cause | The derivative time is < 0 µs. The maximum value depends on the quantity structure. |  |  |
| 50 | **Too many cam records** |  | Yes |
| Cause | You wanted to enter more cam records than is possible with this quantity structure. |  |  |
| 51 | **Axis in operation** |  | Yes |
| Cause | You attempted to enter cam records while the cam controller was active. |  |  |
| 52 | **Axis parameters not assigned** |  | Yes |
| Cause | You want to enter cam data although no machine parameters have been activated yet. |  |  |
| <sup>1)</sup> The error message can also be generated if you have assigned the parameter "inverted" as the count direction in connection with an absolute encoder (SSI). |  |  |  |

#### Error class 15: Messages (S7-300, S7-400)

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 1 | **Start of parameter assignment** |  | No |
| Cause | The module has detected a parameter assignment via a system data block. |  |  |
| 2 | **End of parameter assignment** |  | No |
| Cause | The module has completed processing of the parameter assignment via system data block without errors. |  |  |

#### Error class 128: Diagnostics errors (S7-300, S7-400)

| No. | Meaning |  | Diagnostics interrupt |
| --- | --- | --- | --- |
| 4 | **External auxiliary voltage missing** |  | Yes |
| Cause | - External 24 V auxiliary voltage is not connected or has failed - Front connector missing - Short-circuit (for example, at the connected encoder) |  |  |
| Effect | - Cam processing is disabled - Track outputs is disabled - With incremental encoders, synchronization is canceled - Module parameters not assigned (feedback signal PARA = 0). |  |  |
| Remedy | Verify that the 24 V connection is correct (faulty module if 24 V connection is correct). |  |  |
| 5 | **Front connector missing (** **FM 452** **)** |  | Yes |
| Cause | Front connector not inserted |  |  |
| Effect | - Missing external auxiliary 24 V voltage - Module not ready |  |  |
| Remedy | Insert the front connector |  |  |
| 51 | **Timeout monitoring responded (watchdog)** |  | Yes |
| Cause | - Module exposed to severe interference - Module error |  |  |
| Effect | - Module is reset - Provided that no module error response is detected after the module reset, the module is ready for operation again. - The module signals the watchdog timeout with "incoming" and "outgoing" |  |  |
| Remedy | - Eliminate the interference - Contact the relevant sales department, which will require exact details about the circumstances leading to the error. - Replace the module |  |  |
| 52 | **Internal power supply of the module failed** |  | Yes |
| Cause | Module error |  |  |
| Effect | - Module is reset - Provided that no module error response is detected after the module reset, the module is ready for operation again. |  |  |
| Remedy | Replace the module |  |  |
| 70 | **Hardware interrupt lost** |  | Yes |
| Cause | The module detected a hardware interrupt event that cannot be reported, because the same event has not yet been processed by the user program/ CPU. |  |  |
| Effect | - Cam processing is disabled - Track outputs is disabled - With incremental encoders, synchronization is canceled |  |  |
| Remedy | - Integrate the hardware interrupt OB in the user program - Check the module's bus connection - Disable the hardware interrupt - Adapt your hardware and software to suit your process requirements (for example, faster CPU, optimize user program). |  |  |
| 144 | **Encoder wire break** |  | Yes |
| Cause | - Encoder cable not inserted or sheared off - Encoder has no transverse signals - Incorrect pin assignment - Cable length too long - Short-circuit of the encoder signals |  |  |
| Effect | - Cam processing is disabled - Track outputs is disabled - With incremental encoders, synchronization is canceled |  |  |
| Remedy | - Check the encoder cable - Comply with the encoder specifications - Monitoring can be temporarily disabled at the responsibility of the operator using the programming interface. - Comply with the technical specifications of the module |  |  |
| 145 | **Absolute encoder message frame error** |  | Yes |
| Cause | Incorrect or interrupted message frame traffic between the module and the absolute encoder (SSI):  - Encoder cable not inserted or sheared off - Incorrect encoder type - Incorrect encoder setting (programmable encoders) - Invalid message frame length - Encoder returns incorrect values (faulty encoder) - Interference on the measuring system cable - Selected transmission rate too high |  |  |
| Effect | - Cam processing is disabled - Track outputs is disabled - The last valid actual value remains unchanged until the end of the next correct SSI transfer |  |  |
| Remedy | - Check the encoder cable - Check the encoder - Check the message frame traffic between the encoder and module |  |  |
| 146 | **Incremental encoder missing pulses** |  | Yes |
| Cause | - Encoder monitoring has detected missing pulses - Incorrect entry of the number of increments per encoder revolution - Encoder failure: does not return the specified number of pulses - Incorrect or missing zero mark - Interference on the encoder cable |  |  |
| Effect | - Cam processing is disabled - Track outputs is disabled - Cancelation of synchronization |  |  |
| Remedy | - Enter the correct number of increments / encoder revolutions - Check the encoder and its cable - Comply with shielding and grounding rules - Monitoring can be temporarily disabled at the responsibility of the operator using the programming interface. |  |  |
