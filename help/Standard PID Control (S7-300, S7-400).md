---
title: "Standard PID Control  (S7-300, S7-400)"
package: ProgFBPIDStdenUS
topics: 31
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Standard PID Control  (S7-300, S7-400)

This section contains information on the following topics:

- [Technical specifications of the instructions (S7-300, S7-400)](#technical-specifications-of-the-instructions-s7-300-s7-400)
- [PID_CP (S7-300, S7-400)](#pid_cp-s7-300-s7-400)
- [PID_ES (S7-300, S7-400)](#pid_es-s7-300-s7-400)
- [LP_SCHED (S7-300, S7-400)](#lp_sched-s7-300-s7-400)

## Technical specifications of the instructions (S7-300, S7-400)

### CPU utilization

The controlling efficiency and therefore processing speed of actual control loops depends exclusively on the performance of the CPU you are using. To estimate the utilization of a particular CPU due to installation of Standard PID Control, the following information applies:

- The user memory only has to contain a single instance of the instruction, regardless of the number of controllers.
- You will need a DB with approximately 0.5 Kbytes for each controller.
- There is no memory requirement for an L-Stack.
- Alarms are not delayed by PID_CP or PID_ES.
- Key data for typical execution times (process times) of blocks when default parameters for control mode are used:

| Instruction | Boundary conditions | Processing time (in ms) CPU 315–2AG10 | Processing time (in ms) CPU 416–2XK02 |
| --- | --- | --- | --- |
| PID_CP | Typical boundary conditions | 1.3 | 0.14 |
| PID_ES | Without position feedback, typical boundary conditions | 1.5 | 0.16 |

### Work memory assignment

Refer to the following tables for the size of the required area in the user memory and, thus, the number of control loops that could theoretically be installed based on the available memory capacity:

| Instruction | Load memory requirement | Work memory requirement | Local data |
| --- | --- | --- | --- |
| PID_CP | 8956 bytes | 7796 bytes | 122 bytes |
| PID_ES | 9104 bytes | 7982 bytes | 152 bytes |
| LP_SCHED | 1064 bytes | 976 bytes | 20 bytes |

| Instance DB or global DB | Load memory requirement | Work memory requirement: |
| --- | --- | --- |
| DB for PID_CP | 1168 bytes | 510 bytes |
| DB for PID_ES | 1124 bytes | 484 bytes |
| DB_LOOP (for 5 control loops) | 184 bytes | 100 bytes |
| DB_RMPSK  (with starting point and 4 interpolation points) | 142 bytes | 78 bytes |

### Sampling time

The minimum selectable sampling time is dependent on the performance class of the CPU used.

> **Note**
>
> The limited computational accuracy limits the achievable sampling time. As the sampling time becomes shorter, the constants in the algorithms take on smaller and smaller values. This can result in incorrect calculation of the manipulated variable.
>
> Recommendation:
>
> - S7-300: Sampling time ≥ 20 ms
> - S7-400: Sampling time ≥ 5 ms

## PID_CP (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID_CP (S7-300, S7-400)](#description-pid_cp-s7-300-s7-400)
- [Generating control deviation PID_CP (S7-300, S7-400)](#generating-control-deviation-pid_cp-s7-300-s7-400)
- [Control algorithm PID_CIP (S7-300, S7-400)](#control-algorithm-pid_cip-s7-300-s7-400)
- [Manipulated variable PID_CP (S7-300, S7-400)](#manipulated-variable-pid_cp-s7-300-s7-400)
- [PID_CP in cascade arrangements (S7-300, S7-400)](#pid_cp-in-cascade-arrangements-s7-300-s7-400)
- [Input parameters for PID_CP (S7-300, S7-400)](#input-parameters-for-pid_cp-s7-300-s7-400)
- [Output parameters PID_CP (S7-300, S7-400)](#output-parameters-pid_cp-s7-300-s7-400)
- [In/out parameters PID_CP (S7-300, S7-400)](#inout-parameters-pid_cp-s7-300-s7-400)
- [Static variables PID_CP (S7-300, S7-400)](#static-variables-pid_cp-s7-300-s7-400)
- [Block diagrams for PID_CP (S7-300, S7-400)](#block-diagrams-for-pid_cp-s7-300-s7-400)
- [Global data block DB_RMPSK (S7-300, S7-400)](#global-data-block-db_rmpsk-s7-300-s7-400)

### Description PID_CP (S7-300, S7-400)

In addition to the functions in the setpoint and process value branches, the instruction implements a complete PID-controller with continuous manipulated variable output and the option of manually influencing the manipulated variable. Subfunctions can be enabled or disabled.

With this instruction you are able to control technical processes and systems with continuous input and output variables on the SIMATIC S7 automation systems. Slow (temperatures, filling levels etc.) as well as fast controlling systems (flow, speed etc.) can be controlled.

The controller can be used individually as a fixed setpoint controller, or in multi-loop control systems as a cascade, blending, or ratio controller.

#### Startup

The PID_CP instruction features an initialization routine that is executed when input parameter COM_RST = TRUE is set.

The integral action is set to the initialization value I_ITLVAL at startup and read out at output LMN_I. When it is called in a cyclic interrupt level, it then continues to work starting at this value.

When ramp/soak is enabled, the time intervals DB_NBR PI[0 ... NBR_PTS].TMV between the time slices are added up and displayed at the total time T_TM and total remaining time RT_TM outputs. In the case of online changes of PI[n].TMV or specification of TM_CONT and TM_SNBR, the total time and the total remaining time of the ramp/soak profile change. Since the calculation of T_TM and RS_TM with many time slices significantly increases the processing time of the RMP_SOAK function, the calculation is only carried out at a restart or when TUPDT_ON = TRUE.

All other outputs are set to their default values.

#### Hot restart

With a hot restart, the operating state that existed at the time of the interruption is assumed. The control continues to operate with the values that were calculated at the moment the interruption occurred.

#### Call

The instruction PID_CP must be called with a constant bus cycle time. To achieve this, use a cyclic interrupt level (e.g. OB35).

### Generating control deviation PID_CP (S7-300, S7-400)

The following functions are always active and cannot be disabled.

- Setpoint limiting SP_LIMIT,
- Process value monitoring for absolute values PV_ALARM,
- Process value monitoring for size of rate of change ROCALARM,
- Control deviation monitoring for absolute values ER_ALARM,
- Limiting of the output signal LMNLIMIT.

The default values are selected in such a manner that operation requires no individual adjustment. To achieve good controller results, you always have to adapt the parameters of these functions to your process.

#### Processing the process value

The process value is scaled to the physical value.

[Scaling (PV_NORM)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#scaling-pv_norm-s7-300-s7-400)

![Processing the process value](images/37537335819_DV_resource.Stream@PNG-de-DE.png)

*) Default for creation of new technology object.

The process value can be smoothed with a first-order delay element.

[Smooth controlled variable (LAG1ST)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#smooth-controlled-variable-lag1st-s7-300-s7-400)

![Processing the process value](images/37537623051_DV_resource.Stream@PNG-de-DE.png)

The process value can be linearized with the square root. The following parameters are required for this:

[Square root (SQRT)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#square-root-sqrt-s7-300-s7-400)

![Processing the process value](images/37537446411_DV_resource.Stream@PNG-de-DE.png)

The process value can be prepared with a user-specific function. The following parameters are required for this: The interconnection must be programmed in the user FC.

[FC call in the process value branch (PVFC)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#fc-call-in-the-process-value-branch-pvfc-s7-300-s7-400)

![Processing the process value](images/37537563659_DV_resource.Stream@PNG-de-DE.png)

The process value is always monitored with the following parameters for warning and alarm limits.

[Monitor process value for limit values (PV_ALARM)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#monitor-process-value-for-limit-values-pv_alarm-s7-300-s7-400)

![Processing the process value](images/37537457675_DV_resource.Stream@PNG-de-DE.png)

The rate of change of the process value is always limited with the following parameters.

[Monitor rate of change of the process value (ROCALARM)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#monitor-rate-of-change-of-the-process-value-rocalarm-s7-300-s7-400)

![Processing the process value](images/37537468939_DV_resource.Stream@PNG-de-DE.png)

#### Processing setpoints

The internal setpoint SP_IN can be incremented or decremented with the following parameters.

[Setpoint generator (SP_GEN)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#setpoint-generator-sp_gen-s7-300-s7-400)

![Processing setpoints](images/37537528331_DV_resource.Stream@PNG-de-DE.png)

The setpoint can be specified with the following parameters via a ramp/soak function.

[Ramp/soak (RMP_SOAK)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#rampsoak-rmp_soak-s7-300-s7-400)

![Processing setpoints](images/37537539595_DV_resource.Stream@PNG-de-DE.png)

The blending/ratio controller can scale the external setpoint SP_EXT using the following parameters.

[Scaling](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#scaling-s7-300-s7-400)

![Processing setpoints](images/37537600523_DV_resource.Stream@PNG-de-DE.png)

The setpoint can be further processed with a user-specific function. The following parameters are required for this: The interconnection must be programmed in the user FC.

The input value SPFC_IN is an implicit parameter. This can be monitored with the configuration tool, either via the measuring point MP1 (SPEXT_ON = FALSE) or via the measuring point MP2 (SPEXT_ON = TRUE). The output value is accessible at the measuring point MP3. The input SPFC_IN is then switched through on the setpoint branch, if SPFC_ON =FALSE.

[Limiting functions](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#limiting-functions-s7-300-s7-400)

![Processing setpoints](images/37537611787_DV_resource.Stream@PNG-de-DE.png)

The rate of change of the setpoint can be limited with the following parameters.

![Processing setpoints](images/37537347083_DV_resource.Stream@PNG-de-DE.png)

The setpoint value is always monitored with the following parameters for an absolute high and low limit.

![Processing setpoints](images/37537409547_DV_resource.Stream@PNG-de-DE.png)

#### Generating control deviation

The following parameters can be used to route the control deviation over a deadband.

[Deadband](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#deadband-s7-300-s7-400)

![Generating control deviation](images/37537505803_DV_resource.Stream@PNG-de-DE.png)

The control deviation is always monitored with the following parameters for warning and alarm limits.

[Alarm](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#alarm-s7-300-s7-400-1)

![Generating control deviation](images/37537517067_DV_resource.Stream@PNG-de-DE.png)

### Control algorithm PID_CIP (S7-300, S7-400)

#### Control algorithm

[Control algorithm](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#control-algorithm-s7-300-s7-400)

A total of five switches are available to specify an effective controller structure.

[Controller structures](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#controller-structures-s7-300-s7-400)

| Controller structure | Switch |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| P_SEL | I_SEL | D_SEL | PFDB_SEL | DFDB_SEL |  |
| P control | TRUE | FALSE | FALSE | FALSE | FALSE |
| P control (P in feedback path) | TRUE | FALSE | FALSE | TRUE | FALSE |
| PI control | TRUE | TRUE | FALSE | FALSE | FALSE |
| PI control (P in feedback path) | TRUE | TRUE | FALSE | TRUE | FALSE |
| PD control | TRUE | FALSE | TRUE | FALSE | FALSE |
| PD control (P in feedback path) | TRUE | FALSE | TRUE | FALSE | TRUE |
| PID control | TRUE | TRUE | TRUE | FALSE | FALSE |
| PID control (P/D in feedback path) | TRUE | TRUE | TRUE | FALSE | TRUE |

The proportional action is determined by the proportional gain GAIN and can be monitored at LMN_P.

[Proportional component](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#proportional-component-s7-300-s7-400)

The integral action is calculated using the following parameters.

[Integral action](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#integral-action-s7-300-s7-400)

![Control algorithm](images/37537667595_DV_resource.Stream@PNG-de-DE.png)

*) Default for creation of new technology object

The derivative action is calculated using the following parameters.

[Derivative component](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#derivative-component-s7-300-s7-400)

![Control algorithm](images/37537691659_DV_resource.Stream@PNG-de-DE.png)

### Manipulated variable PID_CP (S7-300, S7-400)

#### Continuous manipulated variable

The PID control algorithm generates an analog manipulated variable, supplemented if necessary by a pulse generator to generate pulse width modulated output signals for the two-step control or three-step controls with proportional actuators.

![Continuous manipulated variable](images/32396976011_DV_resource.Stream@PNG-en-US.png)

The manipulated variable can be manually influenced using the following parameters.

[Manual mode](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#manual-mode-s7-300-s7-400)

![Continuous manipulated variable](images/37537815051_DV_resource.Stream@PNG-de-DE.png)

The manipulated variable can be further processed with a user-specific function. The following parameters are required for this: The interconnection must be programmed in the user FC.

[Limiting functions](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#limiting-functions-s7-300-s7-400-1)

![Continuous manipulated variable](images/37538131979_DV_resource.Stream@PNG-de-DE.png)

The rate of change of the manipulated variable can be limited using the following parameters.

![Continuous manipulated variable](images/37537715723_DV_resource.Stream@PNG-de-DE.png)

The manipulated variable is always monitored with the following parameters for an absolute high and low limit.

![Continuous manipulated variable](images/37537803787_DV_resource.Stream@PNG-de-DE.png)

The manipulated variable is scaled to a physical value using the following parameters.

[Scaling](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#scaling-s7-300-s7-400-1)

![Continuous manipulated variable](images/37538120715_DV_resource.Stream@PNG-de-DE.png)

The manipulated variable in floating-point format is converted to I/O format. In this process, no check is carried out for positive/negative overflow or for reaching the overrange/underrange. Module types are not taken into account.

The following table provides an overview of ranges and numerical values before and after processing.

| Manipulated value LMN in % | I/O value LMN_PER |
| --- | --- |
| 118.515 | 32767 |
| 100.000 | 27648 |
| 0.003617 | 1 |
| 0.000 | 0 |
| -0.003617 | -1 |
| -100.000 | -27648 |
| -118.519 | -32768 |

![Continuous manipulated variable](images/37538360843_DV_resource.Stream@PNG-de-DE.png)

The continuous manipulated variable can be output as pulse train via a pulse width modulation. The following parameters are required for this:

[Pulse generator](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#pulse-generator-s7-300-s7-400)

![Continuous manipulated variable](images/37538436107_DV_resource.Stream@PNG-de-DE.png)

### PID_CP in cascade arrangements (S7-300, S7-400)

#### Interruption of the controller cascade

In a cascade, several controllers are in direct relationship with each other. Therefore, you must take precautions to ensure problem-free cascade operation following an interruption of the cascade structure at any point.

In cascade controls, for this reason, a QCAS signal is generated in the secondary controllers by applying OR logic from the status signals of the switches in the setpoint and manipulated variable branches. This signal actuates a switch in the higher-level controllers that converts the controllers to follow-up mode. The follow-up value is always the setpoint of the lower-level circuit.

A smooth switchover occurs from follow-up mode to automatic mode, just as the switchover from manual to automatic mode.

PID_CP can be used in higher-level control loops as a master controller and in secondary control loops as a follow-up controller.

![Interruption of the controller cascade](images/32397239563_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The manipulated variable of the master controller LMN must always be interconnected with the external setpoint SP_EXT of the follow-up controller.

#### Block interconnection

The following figure shows the principle of the controller interconnection in multi-loop cascades.

![Block interconnection](images/32397251467_DV_resource.Stream@PNG-en-US.png)

### Input parameters for PID_CP (S7-300, S7-400)

| Parameter | Offset | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| COM_RST | 0.0 | BOOL |  | FALSE | Restart  (Initialization routine of the instruction will be processed) |
| I_SEL | 0.1 | BOOL |  | TRUE | Integral action on |
| D_SEL | 0.2 | BOOL |  | FALSE | Derivative action on |
| MAN_ON | 0.3 | BOOL |  | TRUE | Manual mode on  (control loop interrupted, LMN set manually) |
| CAS_ON | 0.4 | BOOL |  | FALSE | Cascade mode ON  (interconnected to QCAS of the lower-level controller) |
| SELECT | 1.0 | BYTE | 0, 1, 2, 3 | 0 | If PULS_ON = TRUE:  0: PID and pulse generator  1: PID (block call in OB 1)  2: Pulse generator (block call in cyclic interrupt OB)  3: PID (block call in cyclic interrupt OB) |
| CYCLE | 2.0 | TIME | &gt; 20 ms (S7–300) | T#1s | Sampling time  (time between two block calls = constant)  Make sure to assign this parameter with the value of the cyclic interrupt cycle clock of the OB in which the PID_CP instruction runs. Otherwise, the time-dependent functions will not work correctly. (Exception: you are using time scaling, e.g., via the loop scheduler) |
| CYCLE_P | 6.0 | TIME |  | T#10 ms | Sampling time of the pulse generator  Make sure to assign this parameter with the value of the cyclic interrupt cycle clock of the OB in which the PID_CP instruction runs. Otherwise, the time-dependent functions will not work correctly. (Exception: you are using time scaling, e.g., via the loop scheduler) |
| SP_INT | 10.0 | REAL | Engineering value range (physical quantity) | 0.0 | Internal setpoint  SP_INT can be changed via a HMI with SPUP and SPDN |
| SP_EXT | 14.0 | REAL | Engineering value range (physical quantity) | 0.0 | External setpoint  SP_EXT is used for blending, ratio and cascade controllers and can be scaled. |
| PV_IN | 18.0 | REAL | Engineering value range (physical quantity) | 0.0 | Process value input  (PV in floating-point format) |
| PV_PER | 22.0 | INT |  | W#16#0000 | Process value of I/O  (PV in I/O format) |
| GAIN | 24.0 | REAL | Overall value range (dimensionless) | 2.0 | Proportional gain  (= controller gain) |
| TI | 28.0 | TIME | TI ≥ CYCLE | T#20s | Integral action time |
| TD | 32.0 | TIME | TD ≥ CYCLE | T#10s | Derivative action time |
| TM_LAG | 36.0 | TIME | TM_LAG ≥ CYCLE/2 | T#2s | Time delay of derivative action |
| DISV | 40.0 | REAL |  | 0.0 | Disturbance variable  Permissible value range: -100.0 ... 100.0 |
| CAS | 44.0 | REAL | Engineering value range (physical quantity) | 0.0 | Input for cascade mode  (interconnected to SP of the lower-level controller) |
| SP_HLM | 48.0 | REAL | Engineering value range (physical quantity) | 100.0 | Setpoint high limit |
| SP_LLM | 52.0 | REAL | Engineering value range (physical quantity) | 0.0 | Setpoint low limit |
| LMN_HLM | 56.0 | REAL | LMN_LLM ... 100.0 | 100.0 | Manipulated variable: High limit |
| LMN_LLM | 60.0 | REAL | -100.0 ... LMN_HLM | 0.0 | Manipulated variable: Low limit |
| DB_NBR | 64.0 | BLOCK_DB |  | DB 1 | Data block number  (DB with the time slices of the ramp/soak profile) |
| SPFC_NBR | 66.0 | BLOCK_FC |  | FC 0 | Setpoint FC number  (self-defined FC in setpoint branch) |
| PVFC_NBR | 68.0 | BLOCK_FC |  | FC 0 | Process value FC number  (self-defined FC in process value branch) |
| LMNFCNBR | 70.0 | BLOCK_FC |  | FC 0 | Manipulated variable FC number  (self-defined FC in manipulated variable branch) |

### Output parameters PID_CP (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMN | 72.0 | REAL | 0.0 | Manipulated variable  (Manipulated variable in floating-point format) |
| LMN_PER | 76.0 | INT | W#16#0000 | Manipulated variable for I/O  (LMN in I/O format) |
| SP | 78.0 | REAL | 0.0 | Setpoint  (effective setpoint) |
| PV | 82.0 | REAL | 0.0 | Process value  (output of effective process value in cascade mode) |
| QCAS | 86.0 | BOOL | FALSE | Signal for cascade mode  (interconnected to CAS_ON of higher-level controller) |
| QC_ACT | 86.1 | BOOL | TRUE | Indicates whether the control functions will be processed at the next block call (only relevant if SELECT has the value 0 or 1) |
| QPOS_P | 86.2 | BOOL | FALSE | Pulse generator: Positive pulse ON |
| QNEG_P | 86.3 | BOOL | FALSE | Pulse generator: Negative pulse ON |

### In/out parameters PID_CP (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| MAN | 88.0 | REAL | 0.0 | Manual manipulated variable  (for manipulated variable assignment by means of operator control and monitoring functions) |

### Static variables PID_CP (S7-300, S7-400)

| Parameter | Offset | Data type | Range of values | Preassigned value | Description |
| --- | --- | --- | --- | --- | --- |
| PVH_ALM | 92.0 | REAL | PVH_WRN...100.0 | 100.0 | Process value: High limit 'Alarm' |
| PVH_WRN | 96.0 | REAL | PVL_WRN... PVH_ALM | 90.0 | Process value: High limit 'Warning' |
| PVL_WRN | 100.0 | REAL | PVL_ALM... PVH_WRN | -90.0 | Process value: Low limit 'Warning' |
| PVL_ALM | 104.0 | REAL | -100.0...PVL_WRN | -100.0 | Process value: Low limit 'Alarm' |
| SPGEN_ON | 108.0 | BOOL |  | FALSE | Setpoint manipulation ON  (adjusting the setpoint using the up/down switch) |
| SPUP | 108.1 | BOOL |  | FALSE | Setpoint UP |
| SPDN | 108.2 | BOOL |  | FALSE | Setpoint DOWN |
| RMPSK_ON | 108.3 | BOOL |  | FALSE | Ramp/soak function ON  (setpoint is specified as a ramp/soak profile) |
| SPEXT_ON | 108.4 | BOOL |  | FALSE | External setpoint ON  (for interconnection with other controller blocks) |
| MANGN_ON | 108.5 | BOOL |  | FALSE | Manual mode ON  (LMN set via switch) |
| MANUP | 108.6 | BOOL |  | FALSE | Manual output value UP |
| MANDN | 108.7 | BOOL |  | FALSE | Manual output value DOWN |
| DFRMP_ON | 109.0 | BOOL |  | FALSE | Preassign output of ramp/soak function  (output is preassigned with SP_INT) |
| CYC_ON | 109.1 | BOOL |  | FALSE | Cyclic repetition ON  (ramp/soak profile will be repeated automatically) |
| RMP_HOLD | 109.2 | BOOL |  | FALSE | Ramp/soak function HOLD  (output of ramp/soak function is frozen) |
| CONT_ON | 109.3 | BOOL |  | FALSE | Continue (with schedule)  (ramp/soak profile will be continued at the next time slice) |
| TUPDT_ON | 109.4 | BOOL |  | FALSE | Recalculate total time  (total time of ramp/soak profile will be recalculated) |
| SPFC_ON | 109.5 | BOOL |  | FALSE | Call setpoint FC |
| SPROC_ON | 109.6 | BOOL |  | FALSE | Ramp function ON  (rate of change limiting of SP) |
| PVPER_ON | 109.7 | BOOL |  | FALSE | Process value of I/O ON  (interconnection to I/O modules) |
| LAG1STON | 110.0 | BOOL |  | FALSE | First-order delay element ON |
| SQRT_ON | 110.1 | BOOL |  | FALSE | Square root function ON |
| PVFC_ON | 110.2 | BOOL |  | FALSE | Call process value FC |
| DEADB_ON | 110.3 | BOOL |  | FALSE | Deadband ON  (small disturbances and noise will be filtered) |
| P_SEL | 110.4 | BOOL |  | TRUE | P component ON |
| PFDB_SEL | 110.5 | BOOL |  | FALSE | Switch P component to feedback |
| INT_HPOS | 110.6 | BOOL |  | FALSE | Freeze I component in positive direction |
| INT_HNEG | 110.7 | BOOL |  | FALSE | Freeze I component in negative direction |
| I_ITL_ON | 111.0 | BOOL |  | FALSE | Preassign I component |
| DFDB_SEL | 111.1 | BOOL |  | FALSE | Switch D component to feedback |
| DISV_SEL | 111.2 | BOOL |  | FALSE | Apply disturbance variable |
| LMNFC_ON | 111.3 | BOOL |  | FALSE | Call manipulated variable FC |
| LMNRC_ON | 111.4 | BOOL |  | FALSE | Activate manipulated variable ramp function  (rate of change limiting of LMN) |
| SMOO_CHG | 111.5 | BOOL |  | TRUE | Smooth changeover from manual to automatic |
| PULSE_ON | 111.6 | BOOL |  | FALSE | Pulse generator ON |
| STEP3_ON | 111.7 | BOOL |  | TRUE | Pulse generator: Three-step control ON |
| ST2BI_ON | 112.0 | BOOL |  | FALSE | Pulse generator: two-step control for bipolar control range ON  (for unipolar control range, STEP3_ON = FALSE must be set) |
| TM_SNBR | 114.0 | INT | ≥ 0 (dimensionless) | 0 | No. of next time slice for continuation |
| TM_CONT | 116.0 | TIME | Overall value range (dimensionless) | T#0s | Continuation point  (Time after time slice TM_SNBR at which the ramp/soak function continues processing the ramp/soak profile) |
| FAC | 120.0 | REAL | Overall value range (dimensionless) | 1.0 | Factor  (ratio or blending factor) |
| NM_SPEHR | 124.0 | REAL |  | 100.0 | Setpoint scaling: Operating range input high |
| NM_SPELR | 128.0 | REAL |  | -100.0 | Setpoint scaling: Operating range input low |
| SPFC_OUT | 132.0 | REAL | -100.0 ... 100.0 | 0.0 | Setpoint FC output  (interconnected to the output of the FC in the setpoint branch) |
| SPURLM_P | 136.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Setpoint up rate limit in positive range |
| SPDRLM_P | 140.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Setpoint down rate limit in positive range |
| SPURLM_N | 144.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Setpoint up rate limit in negative range |
| SPDRLM_N | 148.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Setpoint down rate limit in negative range |
| NM_PIHR | 152.0 | REAL |  | 100.0 | Process value scaling: Measuring range input high |
| NM_PILR | 156.0 | REAL |  | -100.0 | Process value scaling: Measuring range input low |
| NM_PVHR | 160.0 | REAL |  | 100.0 | Process value scaling: Measuring range output high |
| NM_PVLR | 164.0 | REAL |  | -100.0 | Process value scaling: Measuring range output low |
| PV_TMLAG | 168.0 | TIME | Overall value range | T#5s | Process value time delay  (delay of PT1 element in the PV branch) |
| SQRT_HR | 172.0 | REAL |  | 100.0 | Square root: Working range output high |
| SQRT_LR | 176.0 | REAL |  | 0.0 | Square root: Working range output low |
| PVFC_OUT | 180.0 | REAL | -100.0 ... 100.0 | 0.0 | Process value FC output  (interconnected to the output of the FC in the process value branch) |
| PVURLM_P | 184.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Process value up rate limit in the positive range |
| PVDRLM_P | 188.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Process value down rate limit in the positive range |
| PVURLM_N | 192.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Process value up rate limit in the negative range |
| PVDRLM_N | 196.0 | REAL | ≥ 0 [physical quantity/s] | 10.0 | Process value down rate limit in the negative range |
| PV_HYS | 200.0 | REAL | ≥ 0 | 1.0 | Process value hysteresis  (prevents 'flickering' of monitoring display) |
| DEADB_W | 204.0 | REAL | 0.0 ... 100.0 | 1.0 | Deadband width   (= range from zero to deadband high limit)  (determines the size of the deadband area) |
| ERP_ALM | 208.0 | REAL | 0 ... 200.0 | 100.0 | Control deviation: Positive limit 'Alarm' |
| ERP_WRN | 212.0 | REAL | 0 ... 200.0 | 90.0 | Control deviation: Positive limit 'Warning' |
| ERN_WRN | 216.0 | REAL | -200.0 ... 0 | -90.0 | Control deviation: Negative limit 'Warning' |
| ERN_ALM | 220.0 | REAL | -200.0 ... 0 | -100.0 | Control deviation: Negative limit 'Alarm' |
| ER_HYS | 224.0 | REAL | ≥ 0 [%] | 1.0 | Control deviation hysteresis  (prevents 'flickering' of monitoring display) |
| I_ITLVAL | 228.0 | REAL | -100.0 ... 100.0 [%] | 0.0 | Initialization value for I action |
| LMNFCOUT | 232.0 | REAL | -100.0 ... 100.0 [%] | 0.0 | Manipulated variable FC output  (interconnected to the output of the FC in the manipulated variable branch) |
| LMN_URLM | 236.0 | REAL | ≥ 0 [%/s] | 10.0 | Manipulated variable up rate limit |
| LMN_DRLM | 240.0 | REAL | ≥ 0 [%/s] | 10.0 | Manipulated variable down rate limit |
| LMN_FAC | 244.0 | REAL | Overall value range (dimensionless) | 1.0 | Manipulated variable factor  (factor for adaptation of the manipulated variable range) |
| LMN_OFF | 248.0 | REAL | Overall value range (dimensionless) | 0.0 | Manipulated variable offset  (zero point of manipulated variable scaling) |
| PER_TM_P | 252.0 | TIME |  | T#1s | Pulse generator: Period of positive pulse |
| PER_TM_N | 256.0 | TIME |  | T#1s | Pulse generator: Period of negative pulse |
| P_B_TM_P | 260.0 | TIME |  | T#50ms | Pulse generator: Minimum pulse time or minimum break time of positive pulse |
| P_B_TM_N | 264.0 | TIME |  | T#50ms | Pulse generator: Minimum pulse time or minimum break time of negative pulse |
| RATIOFAC | 268.0 | REAL | 0.1 ... 10.0 (dimensionless) | 1.0 | Pulse generator: Ratio factor (ratio of positive pulse time and negative pulse time) |
| PHASE | 272.0 | INT |  | 0 | Phase of PID self tuner |
| QPVH_ALM | 274.0 | BOOL |  | FALSE | Process value: High limit 'Alarm' triggered |
| QPVH_WRN | 274.1 | BOOL |  | FALSE | Process value: High limit 'Warning' triggered |
| QPVL_WRN | 274.2 | BOOL |  | FALSE | Process value: Low limit 'Warning' triggered |
| QPVL_ALM | 274.3 | BOOL |  | FALSE | Process value: Low limit 'Alarm' triggered |
| QR_S_ACT | 274.4 | BOOL |  | FALSE | Time table for ramp/soak profile will be processed |
| QSP_HLM | 274.5 | BOOL |  | FALSE | Setpoint: High limit triggered |
| QSP_LLM | 274.6 | BOOL |  | FALSE | Setpoint: Low limit triggered |
| QPVURLMP | 274.7 | BOOL |  | FALSE | Process value: Up rate limit in positive range triggered |
| QPVDRLMP | 275.0 | BOOL |  | FALSE | Process value: Down rate limit in positive range triggered |
| QPVURLMN | 275.1 | BOOL |  | FALSE | Process value: Up rate limit in negative range triggered |
| QPVDRLMN | 275.2 | BOOL |  | FALSE | Process value: Down rate limit in negative range triggered |
| QERP_ALM | 275.3 | BOOL |  | FALSE | Control deviation: Positive limit 'Alarm' triggered |
| QERP_WRN | 275.4 | BOOL |  | FALSE | Control deviation: Positive limit 'Warning' triggered |
| QERN_WRN | 275.5 | BOOL |  | FALSE | Control deviation: Negative limit 'Warning' triggered |
| QERN_ALM | 275.6 | BOOL |  | FALSE | Control deviation: Negative limit 'Alarm' triggered |
| QLMN_HLM | 275.7 | BOOL |  | FALSE | Manipulated variable: High limit triggered |
| QLMN_LLM | 276.0 | BOOL |  | FALSE | Manipulated variable: Low limit triggered |
| NBR_ATMS | 278.0 | INT |  | 0 | Number of the time slice currently being approached by the ramp/soak function |
| RS_TM | 280.0 | TIME |  | T#0s | "Current residual time" of ramp/soak profile until the next time slice |
| T_TM | 284.0 | TIME |  | T#0s | "Total time" of ramp/soak profile |
| RT_TM | 288.0 | TIME |  | T#0s | "Total residual time" = time remaining until the end of the ramp/soak profile |
| ER | 292.0 | REAL |  | 0.0 | Control deviation |
| LMN_P | 296.0 | REAL |  | 0.0 | P component |
| LMN_I | 300.0 | REAL |  | 0.0 | I component |
| LMN_D | 304.0 | REAL |  | 0.0 | D component |
| SPFC_IN | 308.0 | REAL |  | 0.0 | Setpoint FC input  (interconnected to input of the self-defined FC) |
| PVFC_IN | 312.0 | REAL |  | 0.0 | Process value FC input  (interconnected to input of the self-defined FC) |
| LMNFC_IN | 316.0 | REAL |  | 0.0 | Manipulated variable FC input  (interconnected to input of the self-defined FC) |
| SP_OP_ON | 320.0 | BOOL |  | FALSE | Setpoint manipulation ON  (value of SP_OP will be applied as the setpoint) |
| PV_OP_ON | 320.1 | BOOL |  | FALSE | Process value manipulation ON  (value of PV_OP will be applied as the setpoint) |
| LMNOP_ON | 320.2 | BOOL |  | FALSE | Manipulated variable manipulation ON  (value of LMN_OP will be applied as the setpoint) |
| SP_OP | 322.0 | REAL |  | 0.0 | Setpoint manipulation during commissioning |
| PV_OP | 326.0 | REAL |  | 0.0 | Process value manipulation during commissioning |
| LMN_OP | 330.0 | REAL |  | 0.0 | Manipulated variable manipulation during commissioning |
| MP1 | 334.0 | REAL |  | 0.0 | Measuring point 1: Internal setpoint |
| MP2 | 338.0 | REAL |  | 0.0 | Measuring point 2: External setpoint |
| MP3 | 342.0 | REAL |  | 0.0 | Measuring point 3: Unlimited setpoint |
| MP4 | 346.0 | REAL |  | 0.0 | Measuring point 4: Process value of the I/O module |
| MP5 | 350.0 | REAL |  | 0.0 | Measuring point 5: Process value after first-order delay element |
| MP6 | 354.0 | REAL |  | 0.0 | Measuring point 6: Effective process value (PV) |
| MP7 | 358.0 | REAL |  | 0.0 | Measuring point 7: Manipulated variable of PID algorithm |
| MP8 | 362.0 | REAL |  | 0.0 | Measuring point 8: Manual output value |
| MP9 | 366.0 | REAL |  | 0.0 | Measuring point 9: Unlimited manipulated variable |
| MP10 | 370.0 | REAL |  | 0.0 | Measuring point 10: Limited manipulated variable |

### Block diagrams for PID_CP (S7-300, S7-400)

#### Signal-flow representations

Analogous to the representation of the switches in the configuration tool, the black dot in each switch symbol indicates that the switching signal has the adjacent Boolean value (0=FALSE or 1=TRUE) and that the signal path is switched through this point in each case. The switching signals (binary signals) are identified by dashed lines.

This means that the setpoint is specified as an absolute setpoint via SP_INT; the same applies to the process value input via PV_IN. The default control function is a standard PI controller with P function in the forward branch. The control loop is open and the percentage range of the manipulated variable is influenced by the MAN input. All other functions are passive or, if they cannot be deactivated, marginal signal characteristic parameters are preassigned within the measuring range or operating range so that the functions have no effect.

#### Symbols and identifiers in the signal flow graphs

The names of the connectable process variables are shown on a shaded background. This allows you to recognize where the controller structure can be connected to the S7 I/O or directly to the measuring and actuators of the process.

Parameter names containing the combination of letters "OP" (for example, SP_OP/SP_OP_ON) indicate that an intervention using the Standard PID Control configuration tool is possible at this point. The configuration tool has its own interface to the controller FB.

Intermediate variables in the signal characteristic can be monitored at the measuring points MP1 to MP12 marked with circles. These intermediate variables are required in order to match values before triggering "smooth" changeovers or to check the current statuses of the relevant control. The measuring point variables in the configuration tool curve recorder can be represented (statically and dynamically).

For reasons of clarity, the parameters for setting and sizing the processing operations (algorithms) are also indicated in the individual function blocks. Please refer to the descriptions in the reference section and to the representation of the individual subfunctions in the following sections.

#### Processing the setpoint

![Processing the setpoint](images/32395484043_DV_resource.Stream@PNG-de-DE.png)

#### Processing the process value

![Processing the process value](images/32395508747_DV_resource.Stream@PNG-de-DE.png)

#### Control algorithm

![Control algorithm](images/35854343563_DV_resource.Stream@PNG-de-DE.png)

#### Processing the analog manipulated variable

![Processing the analog manipulated variable](images/32395532555_DV_resource.Stream@PNG-en-US.png)

Depending on the combination of the switching states, the OR gate generates an enable signal for the cascade coupling.

---

**See also**

[Ramp/soak (RMP_SOAK) (S7-300, S7-400)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#rampsoak-rmp_soak-s7-300-s7-400)

### Global data block DB_RMPSK (S7-300, S7-400)

> **Note**
>
> **Creating a global data block yourself**
>
> The time slices for the ramp/soak function (RMP_SOAK) are specified in a global data block. This global data block is not included in the library. You must create the global data block yourself according to the following schema and adapt it to your application.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| NBR_PTS | INT | 4 | Number of time slices -1  1 - 255 |
| PI | Array [0...NBR_PTS] of Struct |  | Structure for the time slice data. The array must be declared by 0...NBR_PTS. |
| PI[0].OUTV | REAL | 0.0 | Output variable [0] Starting point  Engineering value range |
| PI[0].TMV | TIME | T#1s | Time value [0] Starting point |
| PI[1].OUTV | REAL | 0.0 | Output variable [1] Time slice 1  Engineering value range |
| PI[1].TMV | TIME | T#1s | Time value [1] Time slice 1 |
| PI[2].OUTV | REAL | 0.0 | Output variable [2] Time slice 2  Engineering value range |
| PI[2].TMV | TIME | T#1s | Time value [2] Time slice 2 |
| PI[3].OUTV | REAL | 0.0 | Output variable [3] Time slice 3  Engineering value range |
| PI[3].TMV | TIME | T#1s | Time value [3] Time slice 3 |
| PI[4].OUTV | REAL | 0.0 | Output variable [4] Time slice 4  Engineering value range |
| PI[4].TMV | TIME | T#0s | Time value [4] Time slice 4   0 ms |

#### Generating a data block using an external source file

Alternatively, you can generate the global data block using an external source file.

Proceed as follows:

1. Copy the text below to the clipboard.
2. Open an external text editor.
3. Paste the copied text from the clipboard to the text editor.
4. Save the file with the file name extension "DB":
5. Open the "External sources" folder in the project tree of the TIA Portal.
6. Double-click the command "Add new external file".

   The "Open" dialog is displayed.
7. Navigate to the external source file that you have created and select it.
8. Confirm your selection with "Open".
9. Select the external source file.
10. Select the command "Generate blocks from source" in the shortcut menu.
11. A security prompt informs you that any existing blocks will be overwritten.
12. Click "OK" in response to the security prompt.
13. Adapt the created data block to your application.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| `DATA_BLOCK "DB_RMPSK"` |  |  |  |  |
| `TITLE = data block ramp soak` |  |  |  |  |
| `{ S7_Optimized_Access := 'FALSE' }` |  |  |  |  |
| `NAME : DB_RMPSK` |  |  |  |  |
|  | `STRUCT` |  |  |  |
|  |  | `NBR_PTS : Int;` |  | `// number of points (excluding starting point)` |
|  |  | `PI : Array[0..4] of Struct` |  |  |
|  |  |  | `OUTV : Real;` | `// output variable` |
|  |  |  | `TMV : Time;` | `// output time value` |
|  |  | `END_STRUCT;` |  |  |
|  | `END_STRUCT;` |  |  |  |

|  |  |  |
| --- | --- | --- |
| `BEGIN` |  |  |
|  | `NBR_PTS := 4;` |  |
|  | `PI[0].TMV := T#1s;` |  |
|  | `PI[1].TMV := T#1s;` |  |
|  | `PI[2].TMV := T#1s;` |  |
|  | `PI[3].TMV := T#1s;` |  |
|  | `PI[4].TMV := T#0s;` |  |
| `END_DATA_BLOCK` |  |  |

## PID_ES (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID_ES (S7-300, S7-400)](#description-pid_es-s7-300-s7-400)
- [Control deviation generation for PID_ES (S7-300, S7-400)](#control-deviation-generation-for-pid_es-s7-300-s7-400)
- [Control algorithm for PID_ES (S7-300, S7-400)](#control-algorithm-for-pid_es-s7-300-s7-400)
- [Manipulated variable PID_ES (S7-300, S7-400)](#manipulated-variable-pid_es-s7-300-s7-400)
- [PID_ES in cascade arrangements (S7-300, S7-400)](#pid_es-in-cascade-arrangements-s7-300-s7-400)
- [Input parameters PID_ES (S7-300, S7-400)](#input-parameters-pid_es-s7-300-s7-400)
- [Output parameters PID_ES (S7-300, S7-400)](#output-parameters-pid_es-s7-300-s7-400)
- [In/out parameters PID_ES (S7-300, S7-400)](#inout-parameters-pid_es-s7-300-s7-400)
- [Static variables PID_ES (S7-300, S7-400)](#static-variables-pid_es-s7-300-s7-400)
- [Block diagrams for PID_ES (S7-300, S7-400)](#block-diagrams-for-pid_es-s7-300-s7-400)
- [Global data block DB_RMPSK (S7-300, S7-400)](#global-data-block-db_rmpsk-s7-300-s7-400-1)

### Description PID_ES (S7-300, S7-400)

In addition to the functions in the setpoint and process value branches, the instruction implements a complete PID controller with binary manipulated variable output. It is possible to influence the manipulated variable manually. Subfunctions can be enabled or disabled.

The instruction enables technical processes and systems with integral-action actuators to be controlled on SIMATIC S7 automation systems. Slow (temperatures, filling levels etc.) as well as fast controlling systems (flow, speed etc.) can be controlled.

The controller can be used individually as a fixed setpoint controller, or in secondary control loops in cascade, blending or ratio controls; however it cannot be used as the primary controller.

Signal processing in the setpoint/process value branch as well as handling and monitoring of the control deviation is identical to that of the continuous controller.

#### Startup

The PID_ES instruction features an initialization routine that is executed when input parameter COM_RST = TRUE is set.

The integral action is set to the initialization value I_ITLVAL at startup and read out at output LMN_I. When it is called in a cyclic interrupt level, it then continues to work starting at this value.

When ramp/soak is enabled, the time intervals DB_NBR PI[0 ... NBR_PTS].TMV between the time slices are added up and displayed at the total time T_TM and total remaining time RT_TM outputs. In the case of online changes of PI[n].TMV or specification of TM_CONT and TM_SNBR, the total time and the total remaining time of the ramp/soak profile change. Since the calculation of T_TM and RS_TM with many time slices significantly increases the processing time of the RMP_SOAK function, the calculation is only carried out at a restart or when TUPDT_ON = TRUE.

All other outputs are set to their default values.

#### Hot restart

With a hot restart, the operating state that existed at the time of the interruption is assumed. The control continues to operate with the values that were calculated at the moment the interruption occurred.

#### Call

The instruction PID_ES must be called with a constant bus cycle time. To achieve this, use a cyclic interrupt level (e.g. OB35).

### Control deviation generation for PID_ES (S7-300, S7-400)

The following functions are always active and cannot be disabled.

- Setpoint limiting SP_LIMIT,
- Process value monitoring for absolute values PV_ALARM,
- Process value monitoring for size of rate of change ROCALARM,
- Control deviation monitoring for absolute values ER_ALARM,
- Limiting of the output signal LMNLIMIT.

The default values are selected in such a manner that operation requires no individual adjustment. To achieve good controller results, you always have to adapt the parameters of these functions to your process.

#### Processing the process value

The process value is scaled to the physical value.

[Scaling (PV_NORM)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#scaling-pv_norm-s7-300-s7-400-1)

![Processing the process value](images/37537335819_DV_resource.Stream@PNG-de-DE.png)

*) Default for creation of new technology object.

The process value can be smoothed with a first-order delay element.

[Smooth controlled variable (LAG1ST)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#smooth-controlled-variable-lag1st-s7-300-s7-400-1)

![Processing the process value](images/37537623051_DV_resource.Stream@PNG-de-DE.png)

The process value can be linearized with the square root. The following parameters are required for this:

[Square root (SQRT)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#square-root-sqrt-s7-300-s7-400-1)

![Processing the process value](images/37537446411_DV_resource.Stream@PNG-de-DE.png)

The process value can be prepared with a user-specific function. The following parameters are required for this: The interconnection must be programmed in the user FC.

[FC call in the process value branch (PVFC)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#fc-call-in-the-process-value-branch-pvfc-s7-300-s7-400-1)

![Processing the process value](images/37537563659_DV_resource.Stream@PNG-de-DE.png)

The process value is always monitored with the following parameters for warning and alarm limits.

[Monitor process value for limit values (PV_ALARM)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#monitor-process-value-for-limit-values-pv_alarm-s7-300-s7-400-1)

![Processing the process value](images/37537457675_DV_resource.Stream@PNG-de-DE.png)

The rate of change of the process value is always limited with the following parameters.

[Monitor rate of change of the process value (ROCALARM)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#monitor-rate-of-change-of-the-process-value-rocalarm-s7-300-s7-400-1)

![Processing the process value](images/37537468939_DV_resource.Stream@PNG-de-DE.png)

#### Processing setpoints

The internal setpoint SP_IN can be incremented or decremented with the following parameters.

[Setpoint generator (SP_GEN)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#setpoint-generator-sp_gen-s7-300-s7-400-1)

![Processing setpoints](images/37537528331_DV_resource.Stream@PNG-de-DE.png)

The setpoint can be specified with the following parameters via a ramp/soak function.

[Ramp/soak (RMP_SOAK)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#rampsoak-rmp_soak-s7-300-s7-400-1)

![Processing setpoints](images/37537539595_DV_resource.Stream@PNG-de-DE.png)

The blending/ratio controller can scale the external setpoint SP_EXT using the following parameters.

[Scaling](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#scaling-s7-300-s7-400-2)

![Processing setpoints](images/37537600523_DV_resource.Stream@PNG-de-DE.png)

The setpoint can be further processed with a user-specific function. The following parameters are required for this: The interconnection must be programmed in the user FC.

The input value SPFC_IN is an implicit parameter. This can be monitored with the configuration tool, either via the measuring point MP1 (SPEXT_ON = FALSE) or via the measuring point MP2 (SPEXT_ON = TRUE). The output value is accessible at the measuring point MP3. The input SPFC_IN is then switched through on the setpoint branch, if SPFC_ON =FALSE.

[Limiting functions](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#limiting-functions-s7-300-s7-400-2)

![Processing setpoints](images/37537611787_DV_resource.Stream@PNG-de-DE.png)

The rate of change of the setpoint can be limited with the following parameters.

![Processing setpoints](images/37537347083_DV_resource.Stream@PNG-de-DE.png)

The setpoint value is always monitored with the following parameters for an absolute high and low limit.

![Processing setpoints](images/37537409547_DV_resource.Stream@PNG-de-DE.png)

#### Generating control deviation

The following parameters can be used to route the control deviation over a deadband.

[Deadband](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#deadband-s7-300-s7-400-1)

![Generating control deviation](images/37537505803_DV_resource.Stream@PNG-de-DE.png)

The control deviation is always monitored with the following parameters for warning and alarm limits.

[Alarm](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#alarm-s7-300-s7-400-3)

![Generating control deviation](images/37537517067_DV_resource.Stream@PNG-de-DE.png)

### Control algorithm for PID_ES (S7-300, S7-400)

#### Control algorithm

[Control algorithm](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#control-algorithm-s7-300-s7-400-1)

A total of five switches are available to specify an effective controller structure.

[Controller structures](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#controller-structures-s7-300-s7-400-1)

| Controller structure | Switch |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| P_SEL | I_SEL | D_SEL | PFDB_SEL | DFDB_SEL |  |
| P control | TRUE | FALSE | FALSE | FALSE | FALSE |
| P control (P in feedback path) | TRUE | FALSE | FALSE | TRUE | FALSE |
| PI control | TRUE | TRUE | FALSE | FALSE | FALSE |
| PI control (P in feedback path) | TRUE | TRUE | FALSE | TRUE | FALSE |
| PD control | TRUE | FALSE | TRUE | FALSE | FALSE |
| PD control (P in feedback path) | TRUE | FALSE | TRUE | FALSE | TRUE |
| PID control | TRUE | TRUE | TRUE | FALSE | FALSE |
| PID control (P/D in feedback path) | TRUE | TRUE | TRUE | FALSE | TRUE |

The proportional action is determined by the proportional gain GAIN and can be monitored at LMN_P.

[Proportional component](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#proportional-component-s7-300-s7-400-1)

The integral action is calculated using the following parameters.

[Integral action](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#integral-action-s7-300-s7-400-1)

![Control algorithm](images/37537667595_DV_resource.Stream@PNG-de-DE.png)

*) Default for creation of new technology object

The derivative action is calculated using the following parameters.

[Derivative component](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#derivative-component-s7-300-s7-400-1)

![Control algorithm](images/37537691659_DV_resource.Stream@PNG-de-DE.png)

### Manipulated variable PID_ES (S7-300, S7-400)

#### Scaling the position feedback

The position feedback in I/O format is converted to floating-point format. The position feedback in I/O format can be monitored at MP10.

The following table provides an overview of ranges and numerical values before and after processing.

| I/O value LMNR_PER | LMNR in % |
| --- | --- |
| 32767 | 118.515 |
| 27648 | 100.000 |
| 1 | 0.003617 |
| 0 | 0.000 |
| -1 | -0.003617 |
| -27648 | -100.000 |
| -32768 | -118.519 |

![Scaling the position feedback](images/37539082379_DV_resource.Stream@PNG-de-DE.png)

*) Default for creation of new technology object.

#### Manipulated value limit

The manipulated variable is always monitored with the following parameters for an absolute high and low limit. The implicit parameter can be monitored at MP9.

[Limiting functions](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#limiting-functions-s7-300-s7-400-3)

![Manipulated value limit](images/37539032715_DV_resource.Stream@PNG-de-DE.png)

#### Step controller with position feedback

For step controllers with position feedback, the actuating signals are generated using the following parameters:

[Step controller with position feedback](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#step-controller-with-position-feedback-s7-300-s7-400)

![Step controller with position feedback](images/37539157643_DV_resource.Stream@PNG-de-DE.png)

#### Step controller without position feedback

The position feedback can be simulated. The position feedback is simulated by an integrator with motor transition time MTR_TM as the integral action time constant. When LMNRS_ON = FALSE, the start value of the LMNRSVAL parameter is output at the output of the LMNR_SIM integrator. On switchover to LMNRS_ON = TRUE, the simulation starts up with this start value.

If LMNR_HS = TRUE, the integration is held up, and if LMNR_LS = TRUE, it is held down. The simulated position feedback is not adjusted to the endstop signals.

[Step controller without position feedback](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#step-controller-without-position-feedback-s7-300-s7-400)

![Step controller without position feedback](images/36367318795_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> The position feedback is merely simulated. It does not have to match the actual position of the actuator. If a real position feedback is available, it should always be used.

![Step controller without position feedback](images/37539157643_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Manual mode (S7-300, S7-400)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#manual-mode-s7-300-s7-400-1)
  
[Pulse generator (S7-300, S7-400)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#pulse-generator-s7-300-s7-400-1)

### PID_ES in cascade arrangements (S7-300, S7-400)

#### Interruption of the controller cascade

In a cascade, several controllers are in direct relationship with each other. Therefore, you must take precautions to ensure problem-free cascade operation following an interruption of the cascade structure at any point.

In cascade controls, for this reason, a QCAS signal is generated in the secondary controllers by applying OR logic from the status signals of the switches in the setpoint and manipulated variable branches. This signal actuates a switch in the higher-level controllers that converts the controllers to follow-up mode. The follow-up value is always the setpoint SP of the lower-level circuit.

A smooth switchover occurs from follow-up mode to automatic mode, just as the switchover from manual to automatic mode.

> **Note**
>
> PID_ES can only be used in cascade arrangements as a follow-up controller in lower-level control loops.

![Interruption of the controller cascade](images/32397912075_DV_resource.Stream@PNG-en-US.png)

#### Block interconnection

The following figure shows the principle of the controller interconnection in multi-loop cascades.

![Block interconnection](images/32397923979_DV_resource.Stream@PNG-en-US.png)

### Input parameters PID_ES (S7-300, S7-400)

| Parameter | Offset | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| COM_RST | 0.0 | BOOL |  | FALSE | Restart  (Initialization routine of the instruction will be processed) |
| I_SEL | 0.1 | BOOL |  | TRUE | Integral action on |
| D_SEL | 0.2 | BOOL |  | FALSE | Derivative action on |
| MAN_ON | 0.3 | BOOL |  | TRUE | Manual mode on  (control loop interrupted, LMN set manually) |
| LMNR_HS | 0.4 | BOOL |  | FALSE | High limit signal of position feedback |
| LMNR_LS | 0.5 | BOOL |  | FALSE | Low limit signal of position feedback |
| CYCLE | 2.0 | TIME | &gt; 20 ms (S7–300) | T#1s | Sampling time  (time between block calls = constant)  Make sure to assign this parameter with the value of the cyclic interrupt cycle clock of the OB in which the PID_CP instruction runs. Otherwise, the time-dependent functions will not work correctly. (Exception: You are using time scaling, e.g., via the loop scheduler) |
| SP_INT | 6.0 | REAL | Engineering value range (physical quantity) | 0.0 | Internal setpoint  SP_INT can be changed via a HMI with SPUP and SPDN |
| SP_EXT | 10.0 | REAL | Engineering value range (physical quantity) | 0.0 | External setpoint  SP_EXT is used for blending, ratio and cascade controllers and can be scaled. |
| PV_IN | 14.0 | REAL | Engineering value range (physical quantity) | 0.0 | Process value input  (PV in floating-point format) |
| PV_PER | 18.0 | INT |  | W#16#0000 | Process value of I/O |
| GAIN | 20.0 | REAL | Overall value range (dimensionless) | 2.0 | Proportional gain  (= controller gain) |
| TI | 24.0 | TIME | TI ≥ CYCLE | T#20s | Integral action time |
| TD | 28.0 | TIME | TD ≥ CYCLE | T#10s | Derivative-action time |
| TM_LAG | 32.0 | TIME | TM_LAG ≥ CYCLE/2 | T#2s | Time delay of derivative action |
| DISV | 36.0 | REAL | -100.0 ... 100.0 [%] | 0.0 | Disturbance variable |
| LMNR_IN | 40.0 | REAL | 0.0 ... 100.0 [%] | 0.0 | Position feedback  (LMNR in floating-point format) |
| LMNR_PER | 44.0 | INT |  | W#16#0000 | Position feedback of I/O  (LMNR in I/O format) |
| SP_HLM | 46.0 | REAL | Engineering value range (physical quantity) | 100.0 | Setpoint high limit |
| SP_LLM | 50.0 | REAL | Engineering value range (physical quantity) | 0.0 | Setpoint low limit |
| LMN_HLM | 54.0 | REAL | LMN_LLM ... 100.0 [%] | 100.0 | Manipulated variable: High limit |
| LMN_LLM | 58.0 | REAL | 0.0 ... LMN_HLM [%] | 0.0 | Manipulated variable: Low limit |
| DB_NBR | 62.0 | BLOCK_DB |  | DB 1 | Data block number  (DB with the time slices of the ramp/soak profile) |
| SPFC_NBR | 64.0 | BLOCK_FC |  | FC 0 | Setpoint FC number  (self-defined FC in setpoint branch) |
| PVFC_NBR | 66.0 | BLOCK_FC |  | FC 0 | Process value FC number  (self-defined FC in process value branch) |

### Output parameters PID_ES (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| QLMNUP | 68.0 | BOOL | FALSE | Manipulated variable signal UP |
| QLMNDN | 68.1 | BOOL | FALSE | Manipulated variable signal DOWN |
| QCAS | 68.2 | BOOL | FALSE | Signal for cascade mode  (interconnected to CAS_ON of higher-level controller) |
| LMN | 70.0 | REAL | 0.0 | Manipulated variable signal (according to control algorithm) |
| SP | 74.0 | REAL | 0.0 | Setpoint  (effective setpoint) |
| PV | 78.0 | REAL | 0.0 | Process value  (output of effective process value in cascade mode) |

### In/out parameters PID_ES (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| MAN | 82.0 | REAL | 0.0 | Manual output value  (for manipulated variable assignment by means of operator control and monitoring functions) |

### Static variables PID_ES (S7-300, S7-400)

| Parameter | Offset | Data type | Range of values | Preassigned value | Description |
| --- | --- | --- | --- | --- | --- |
| PVH_ALM | 86.0 | REAL | PVH_WRN...100.0 | 100.0 | Process value: High limit 'Alarm'  Valid value range: |
| PVH_WRN | 90.0 | REAL | PVL_WRN... PVH_ALM | 90.0 | Process value: High limit 'Warning'  Valid value range: |
| PVL_WRN | 94.0 | REAL | PVL_ALM... PVH_WRN | -90.0 | Process value: Low limit 'Warning'  Valid value range: |
| PVL_ALM | 98.0 | REAL | -100.0...PVL_WRN | -100.0 | Process value: Low limit 'Alarm'  Valid value range: |
| SPGEN_ON | 102.0 | BOOL |  | FALSE | Setpoint manipulation ON  (adjusting the setpoint using the up/down switch) |
| SPUP | 102.1 | BOOL |  | FALSE | Setpoint UP |
| SPDN | 102.2 | BOOL |  | FALSE | Setpoint DOWN |
| RMPSK_ON | 102.3 | BOOL |  | FALSE | Ramp/soak function ON  (setpoint is specified as a ramp/soak profile) |
| SPEXT_ON | 102.4 | BOOL |  | FALSE | External setpoint ON  (for interconnection with other controller blocks) |
| MANGN_ON | 102.5 | BOOL |  | FALSE | Manual mode ON  (LMN set via switch) |
| MANUP | 102.6 | BOOL |  | FALSE | Manual output value UP |
| MANDN | 102.7 | BOOL |  | FALSE | Manual output value DOWN |
| LMNS_ON | 103.0 | BOOL |  | FALSE | Manual mode for actuating signals ON |
| LMNUP | 103.1 | BOOL |  | FALSE | Manipulated variable signal UP  (output signal QLMNUP will be manipulated) |
| LMNDN | 103.2 | BOOL |  | FALSE | Manipulated variable signal DOWN  (output signal QLMNDN will be manipulated) |
| DFRMP_ON | 103.3 | BOOL |  | FALSE | Preassign output of ramp/soak function  (output is preassigned with SP_INT) |
| CYC_ON | 103.4 | BOOL |  | FALSE | Cyclic repetition ON  (ramp/soak profile will be repeated automatically) |
| RMP_HOLD | 103.5 | BOOL |  | FALSE | Ramp/soak function HOLD  (output of ramp/soak function is frozen) |
| CONT_ON | 103.6 | BOOL |  | FALSE | Continue (with schedule)  (ramp/soak profile will be continued at the next time slice) |
| TUPDT_ON | 103.7 | BOOL |  | FALSE | Recalculate total time  (total time of ramp/soak profile will be recalculated) |
| SPFC_ON | 104.0 | BOOL |  | FALSE | Call setpoint FC |
| SPROC_ON | 104.1 | BOOL |  | FALSE | Ramp function ON  (rate of change limiting of SP) |
| PVPER_ON | 104.2 | BOOL |  | FALSE | Process value of I/O ON  (interconnection with I/O modules) |
| LAG1STON | 104.3 | BOOL |  | FALSE | First-order delay element ON |
| SQRT_ON | 104.4 | BOOL |  | FALSE | Square root function ON |
| PVFC_ON | 104.5 | BOOL |  | FALSE | Call process value FC |
| DEADB_ON | 104.6 | BOOL |  | FALSE | Deadband ON  (small disturbances and noise will be filtered) |
| P_SEL | 104.7 | BOOL |  | TRUE | P component ON |
| PFDB_SEL | 105.0 | BOOL |  | FALSE | Switch P component to feedback |
| INT_HPOS | 105.1 | BOOL |  | FALSE | Freeze I component in positive direction |
| INT_HNEG | 105.2 | BOOL |  | FALSE | Freeze I component in negative direction |
| I_ITL_ON | 105.3 | BOOL |  | FALSE | Preassign I component |
| DFDB_SEL | 105.4 | BOOL |  | FALSE | Switch D component to feedback |
| DISV_SEL | 105.5 | BOOL |  | FALSE | Apply disturbance variable |
| LMNR_ON | 105.6 | BOOL |  | FALSE | Position feedback ON  (operating modes: step controller with/without position feedback) Do not switch while in control mode! |
| LMNRP_ON | 105.7 | BOOL |  | FALSE | Position feedback of I/O ON |
| TM_SNBR | 106.0 | INT | ≥ 0 (dimensionless) | 0 | No. of next time slice for continuation of the ramp/soak profile |
| TM_CONT | 108.0 | TIME | Overall value range (dimensionless) | T#0s | Time span until continuation of the ramp/soak profile  (time that elapses before the ramp/soak function continues processing the ramp/soak profile at time slice TM_SNBR following an interruption) |
| FAC | 112.0 | REAL | Overall value range (dimensionless) | 1.0 | Factor  (ratio or blending factor) |
| NM_SPEHR | 116.0 | REAL |  | 100.0 | Setpoint scaling: Input high |
| NM_SPELR | 120.0 | REAL |  | -100.0 | Setpoint scaling: Input low |
| SPFC_OUT | 124.0 | REAL | -100.0 ... 100.0 | 0.0 | Setpoint FC output  (interconnected to the output of the FC in the setpoint branch) |
| SPURLM_P | 128.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Setpoint up rate limit in positive range |
| SPDRLM_P | 132.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Setpoint down rate limit in positive range |
| SPURLM_N | 136.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Setpoint up rate limit in negative range |
| SPDRLM_N | 140.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Setpoint down rate limit in negative range |
| NM_PIHR | 144.0 | REAL |  | 100.0 | Process value scaling: Input high |
| NM_PILR | 148.0 | REAL |  | -100.0 | Process value scaling: Input low |
| NM_PVHR | 152.0 | REAL |  | 100.0 | Process value scaling: Output high |
| NM_PVLR | 156.0 | REAL |  | -100.0 | Process value scaling: Output low |
| PV_TMLAG | 160.0 | TIME | Overall value range | T#5s | Process value time delay  (delay of PT1 element in the PV branch) |
| SQRT_HR | 164.0 | REAL |  | 100.0 | Square root: Measuring range output high |
| SQRT_LR | 168.0 | REAL |  | 0.0 | Square root: Measuring range output low |
| PVFC_OUT | 172.0 | REAL | -100.0 ... 100.0 | 0.0 | Process value FC output  (interconnected to the output of the FC in the process value branch) |
| PVURLM_P | 176.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Process value up rate limit in the positive range |
| PVDRLM_P | 180.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Process value down rate limit in the positive range |
| PVURLM_N | 184.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Process value up rate limit in the negative range |
| PVDRLM_N | 188.0 | REAL | ≥ 0   [physical quantity/s] | 10.0 | Process value down rate limit in the negative range |
| PV_HYS | 192.0 | REAL | ≥ 0 | 1.0 | Process value hysteresis  (prevents 'flickering' of monitoring display) |
| DEADB_W | 196.0 | REAL | 0.0 ... 100.0 | 1.0 | Deadband width  (determines the size of the deadband area) |
| ERP_ALM | 200.0 | REAL | 0 ... 200.0 | 100.0 | Control deviation: Positive limit 'Alarm' |
| ERP_WRN | 204.0 | REAL | 0 ... 200.0 | 90.0 | Control deviation: Positive limit 'Warning' |
| ERN_WRN | 208.0 | REAL | -200.0 ... 0 | -90.0 | Control deviation: Negative limit 'Warning' |
| ERN_ALM | 212.0 | REAL | -200.0 ... 0 | -100.0 | Control deviation: Negative limit 'Alarm' |
| ER_HYS | 216.0 | REAL | ≥0 | 1.0 | Control deviation hysteresis  (prevents 'flickering' of monitoring display) |
| I_ITLVAL | 220.0 | REAL | -100.0 ... 100.0 [%] | 0.0 | Initialization value for I action |
| LMNR_FAC | 224.0 | REAL | Overall value range (dimensionless) | 1.0 | Position feedback factor  (factor for adaptation of the feedback range) |
| LMNR_OFF | 228.0 | REAL | -100.0 ... 100.0 [%] | 0.0 | Position feedback offset  (zero point of feedback scaling) |
| PULSE_TM | 232.0 | TIME | = n * CYCLE /n=0,1,2... | T#3s | Minimum pulse time |
| BREAK_TM | 236.0 | TIME | = n * CYCLE /n=0,1,2... | T#3s | Minimum break time |
| MTR_TM | 240.0 | TIME | ≥ CYCLE | T#30s | Motor actuating time |
| PHASE | 244.0 | INT |  | 0 | Phase of PID self tuner |
| QPVH_ALM | 246.0 | BOOL |  | FALSE | Process value: High limit 'Alarm' triggered |
| QPVH_WRN | 246.1 | BOOL |  | FALSE | Process value: High limit 'Warning' triggered |
| QPVL_WRN | 246.2 | BOOL |  | FALSE | Process value: Low limit 'Warning' triggered |
| QPVL_ALM | 246.3 | BOOL |  | FALSE | Process value: Low limit 'Alarm' triggered |
| QR_S_ACT | 246.4 | BOOL |  | FALSE | Time table for ramp/soak profile will be processed |
| QSP_HLM | 246.5 | BOOL |  | FALSE | Setpoint: High limit triggered |
| QSP_LLM | 246.6 | BOOL |  | FALSE | Setpoint: Low limit triggered |
| QPVURLMP | 246.7 | BOOL |  | FALSE | Process value: Up rate limit in positive range triggered |
| QPVDRLMP | 247.0 | BOOL |  | FALSE | Process value: Down rate limit in positive range triggered |
| QPVURLMN | 247.1 | BOOL |  | FALSE | Process value: Up rate limit in negative range triggered |
| QPVDRLMN | 247.2 | BOOL |  | FALSE | Process value: Down rate limit in negative range triggered |
| QERP_ALM | 247.3 | BOOL |  | FALSE | Control deviation: Positive limit 'Alarm' triggered |
| QERP_WRN | 247.4 | BOOL |  | FALSE | Control deviation: Positive limit 'Warning' triggered |
| QERN_WRN | 247.5 | BOOL |  | FALSE | Control deviation: Negative limit 'Warning' triggered |
| QERN_ALM | 247.6 | BOOL |  | FALSE | Control deviation: Negative limit 'Alarm' triggered |
| QLMN_HLM | 247.7 | BOOL |  | FALSE | Manipulated variable: High limit triggered |
| QLMN_LLM | 248.0 | BOOL |  | FALSE | Manipulated variable: Low limit triggered |
| NBR_ATMS | 250.0 | INT |  | 0 | Number of the time slice currently being approached by the ramp/soak function |
| RS_TM | 252.0 | TIME |  | T#0s | "Current residual time" of ramp/soak profile until the next time slice |
| T_TM | 256.0 | TIME |  | T#0s | "Total time" = elapsed time of ramp/soak profile |
| RT_TM | 260.0 | TIME |  | T#0s | "Total residual time" = time remaining until the end of the ramp/soak profile |
| ER | 264.0 | REAL |  | 0.0 | Control deviation |
| LMN_P | 268.0 | REAL |  | 0.0 | P component |
| LMN_I | 272.0 | REAL |  | 0.0 | I component |
| LMN_D | 276.0 | REAL |  | 0.0 | D component |
| SPFC_IN | 280.0 | REAL |  | 0.0 | Setpoint FC input  (interconnected to input of the self-defined FC) |
| PVFC_IN | 284.0 | REAL |  | 0.0 | Process value FC input  (interconnected to input of the self-defined FC) |
| SP_OP_ON | 288.0 | BOOL |  | FALSE | Setpoint manipulation ON  (value of SP_OP will be applied as the setpoint) |
| PV_OP_ON | 288.1 | BOOL |  | FALSE | Process value manipulation ON  (value of PV_OP will be applied as the setpoint) |
| LMNOP_ON | 288.2 | BOOL |  | FALSE | Manipulated variable manipulation ON  (value of LMN_OP will be applied as the setpoint) |
| LMNSOPON | 288.3 | BOOL |  | FALSE | Manipulated variable signal manipulation ON  (LMNUP_OP and LMNDN_OP will be applied as actuating signals) |
| LMNUP_OP | 288.4 | BOOL |  | FALSE | Manipulated variable signal UP |
| LMNDN_OP | 288.5 | BOOL |  | FALSE | Manipulated variable signal DOWN |
| LMNRS_ON | 288.6 | BOOL |  | FALSE | Simulation of the position feedback ON |
| SP_OP | 290.0 | REAL |  | 0.0 | Setpoint manipulation in the configuration tool |
| PV_OP | 294.0 | REAL |  | 0.0 | Process value manipulation in the configuration tool |
| LMN_OP | 298.0 | REAL |  | 0.0 | Manipulated variable manipulation in the configuration tool |
| LMNRSVAL | 302.0 | REAL |  | 0.0 | Start value of the simulated position feedback |
| LMNR_SIM | 306.0 | REAL |  | 0.0 | Current value of the simulated position feedback |
| MP1 | 310.0 | REAL |  | 0.0 | Measuring point 1: Internal setpoint |
| MP2 | 314.0 | REAL |  | 0.0 | Measuring point 2: External setpoint |
| MP3 | 318.0 | REAL |  | 0.0 | Measuring point 3: Unlimited setpoint |
| MP4 | 322.0 | REAL |  | 0.0 | Measuring point 4: Process value of the I/O module |
| MP5 | 326.0 | REAL |  | 0.0 | Measuring point 5: Process value after first-order delay element |
| MP6 | 330.0 | REAL |  | 0.0 | Measuring point 6: Effective process value (PV) |
| MP7 | 334.0 | REAL |  | 0.0 | Measuring point 7: Manipulated variable of PID algorithm |
| MP8 | 338.0 | REAL |  | 0.0 | Measuring point 8: Manual output value |
| MP9 | 342.0 | REAL |  | 0.0 | Measuring point 9: Unlimited manipulated variable |
| MP10 | 346.0 | REAL |  | 0.0 | Measuring point 10: Position feedback I/O |
| MP11 | 350.0 | REAL |  | 0.0 | Measuring point 11: Feedback value (LMNR_ON = FALSE)  Position feedback (LMNR_ON = TRUE) |
| MP12 | 354.0 | REAL |  | 0.0 | Measuring point 12: Three-step element input |

### Block diagrams for PID_ES (S7-300, S7-400)

#### Signal flow diagrams

Analogous to the representation of the switches in the configuration tool, the black dot in each switch symbol indicates that the switching signal has the adjacent Boolean value (0=FALSE or 1=TRUE) and that the signal path is switched through this point in each case. The switching signals (binary signals) are identified by dashed lines.

This means that the setpoint is specified as an absolute setpoint via SP_INT; the same applies to the process value input via PV_IN. The default control function is a standard PI controller with P function in the forward branch. The control loop is open and the percentage range of the manipulated variable is influenced by the MAN input. All other functions are passive or, if they cannot be deactivated, marginal signal characteristic parameters are preassigned within the measuring range or operating range so that the functions have no effect.

#### Symbols and identifiers in the signal flow graphs

The names of the connectable process variables are shown on a shaded background. This allows you to recognize where the controller structure can be connected to the S7 I/O or directly to the measuring elements and actuators of the process.

Parameter names containing the combination of letters "OP" (for example, SP_OP/SP_OP_ON) indicate that an intervention using the Standard PID Control configuration tool is possible at this point. The configuration tool has its own interface to the controller FB.

Intermediate variables in the signal characteristic can be monitored at the measuring points MP1 to MP12 marked with circles. These intermediate variables are required in order to match values before triggering "smooth" changeovers or to check the current statuses of the relevant control. The measuring point variables in the configuration tool curve recorder can be represented (statically and dynamically).

For reasons of clarity, the parameters for setting and sizing the processing operations (algorithms) are also indicated in the individual function blocks. Please refer to the descriptions in the reference section and to the representation of the individual subfunctions in the following sections.

#### Processing the setpoint

![Processing the setpoint](images/32395484043_DV_resource.Stream@PNG-de-DE.png)

#### Processing the process value

![Processing the process value](images/32395508747_DV_resource.Stream@PNG-de-DE.png)

#### Control algorithm

![Control algorithm](images/32395520651_DV_resource.Stream@PNG-de-DE.png)

#### Step controller without position feedback (LMNR_ON = FALSE)

![Step controller without position feedback (LMNR_ON = FALSE)](images/32395556363_DV_resource.Stream@PNG-en-US.png)

#### Step controller with position feedback (LMNR_ON = TRUE)

![Step controller with position feedback (LMNR_ON = TRUE)](images/32395544459_DV_resource.Stream@PNG-en-US.png)

### Global data block DB_RMPSK (S7-300, S7-400)

> **Note**
>
> **Creating a global data block yourself**
>
> The time slices for the ramp/soak function (RMP_SOAK) are specified in a global data block. This global data block is not included in the library. You must create the global data block yourself according to the following schema and adapt it to your application.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| NBR_PTS | INT | 4 | Number of time slices -1  1 - 255 |
| PI | Array [0...NBR_PTS] of Struct |  | Structure for the time slice data. The array must be declared by 0...NBR_PTS. |
| PI[0].OUTV | REAL | 0.0 | Output variable [0] Starting point  Engineering value range |
| PI[0].TMV | TIME | T#1s | Time value [0] Starting point |
| PI[1].OUTV | REAL | 0.0 | Output variable [1] Time slice 1  Engineering value range |
| PI[1].TMV | TIME | T#1s | Time value [1] Time slice 1 |
| PI[2].OUTV | REAL | 0.0 | Output variable [2] Time slice 2  Engineering value range |
| PI[2].TMV | TIME | T#1s | Time value [2] Time slice 2 |
| PI[3].OUTV | REAL | 0.0 | Output variable [3] Time slice 3  Engineering value range |
| PI[3].TMV | TIME | T#1s | Time value [3] Time slice 3 |
| PI[4].OUTV | REAL | 0.0 | Output variable [4] Time slice 4  Engineering value range |
| PI[4].TMV | TIME | T#0s | Time value [4] Time slice 4   0 ms |

#### Generating a data block using an external source file

Alternatively, you can generate the global data block using an external source file.

Proceed as follows:

1. Copy the text below to the clipboard.
2. Open an external text editor.
3. Paste the copied text from the clipboard to the text editor.
4. Save the file with the file name extension "DB":
5. Open the "External sources" folder in the project tree of the TIA Portal.
6. Double-click the command "Add new external file".

   The "Open" dialog is displayed.
7. Navigate to the external source file that you have created and select it.
8. Confirm your selection with "Open".
9. Select the external source file.
10. Select the command "Generate blocks from source" in the shortcut menu.
11. A security prompt informs you that any existing blocks will be overwritten.
12. Click "OK" in response to the security prompt.
13. Adapt the created data block to your application.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| `DATA_BLOCK "DB_RMPSK"` |  |  |  |  |
| `TITLE = data block ramp soak` |  |  |  |  |
| `{ S7_Optimized_Access := 'FALSE' }` |  |  |  |  |
| `NAME : DB_RMPSK` |  |  |  |  |
|  | `STRUCT` |  |  |  |
|  |  | `NBR_PTS : Int;` |  | `// number of points (excluding starting point)` |
|  |  | `PI : Array[0..4] of Struct` |  |  |
|  |  |  | `OUTV : Real;` | `// output variable` |
|  |  |  | `TMV : Time;` | `// output time value` |
|  |  | `END_STRUCT;` |  |  |
|  | `END_STRUCT;` |  |  |  |

|  |  |  |
| --- | --- | --- |
| `BEGIN` |  |  |
|  | `NBR_PTS := 4;` |  |
|  | `PI[0].TMV := T#1s;` |  |
|  | `PI[1].TMV := T#1s;` |  |
|  | `PI[2].TMV := T#1s;` |  |
|  | `PI[3].TMV := T#1s;` |  |
|  | `PI[4].TMV := T#0s;` |  |
| `END_DATA_BLOCK` |  |  |

---

**See also**

[Ramp/soak (RMP_SOAK) (S7-300, S7-400)](Using%20standard%20PID%20control%20%28S7-300%2C%20S7-400%29.md#rampsoak-rmp_soak-s7-300-s7-400-1)

## LP_SCHED (S7-300, S7-400)

This section contains information on the following topics:

- [Description of LP_SCHED (S7-300, S7-400)](#description-of-lp_sched-s7-300-s7-400)
- [Operating principle of LP_SCHED (S7-300, S7-400)](#operating-principle-of-lp_sched-s7-300-s7-400)
- [Input parameters LP_SCHED (S7-300, S7-400)](#input-parameters-lp_sched-s7-300-s7-400)
- [Global data block for DB_LOOP (S7-300, S7-400)](#global-data-block-for-db_loop-s7-300-s7-400)

### Description of LP_SCHED (S7-300, S7-400)

LP_SCHED is used when the number of cyclic interrupts of a CPU is not sufficient to achieve the desired (different) sampling times. It enables up to 256 control loops to be called with sampling times equal to an integer multiple of the cyclic interrupt cycle.

LP_SCHED reads the parameters you assigned from the global data block DB_LOOP, calculates from these parameters the tags necessary for call scheduling, and stores these tags in the DB_LOOP data block again.

[Global data block for DB_LOOP](#global-data-block-for-db_loop-s7-300-s7-400) is not included in the library. You must create this global data block yourself.

> **Note**
>
> The block does not check to determine whether a global DB with the number DB_NBR actually exists or whether the GLP_NBR parameter (maximum control loop number) adapts to the length of the data block. If the parameter assignment is incorrect, the CPU changes to STOP with an "internal system error".

#### Call

You must call LP_SCHED in a cyclic interrupt OB prior to all controllers.

Note the following when assigning values to the input parameters:

- TM_BASE: At this input, specify the cycle clock of the cyclic interrupt OB in which the LP_SCHED instruction is called.
- COM_RST: At CPU startup, you must call LP_SCHED once with COM_RST = TRUE. During cyclic operation (cyclic interrupt), you must call LP_SCHED with COM_RST = FALSE.
- DB_NBR: At this input, you specify the number of the "DB_LOOP" data block that LP_SCHED is to access.

After the LP_SCHED instruction is called, you must call all associated controllers conditionally. You cannot use LP_SCHED to call the controllers PID_CP or PID_ES, as their input and output parameters must be assigned when the instructions are called.

The following is an example of calling the LP_SCHED instruction and of conditionally calling a controller.

| STL |  |
| --- | --- |
| CALL "LP_SCHED" |  |
| TM_BASE:= | Here, the cycle clock of the cyclic interrupt is parameterized. Example: T#100ms or #CYCLE where CYCLE = input parameter of the block in which LP_SCHED instruction is called. |
| COM_RST:= | Here, the LP_SCHED instruction is notified whether or not an initialization pass of the called control loop is to take place. Example: FALSE or #COM_RST where COM_RST = input parameter of the block in which the LP_SCHED instruction is called. |
| DB_NBR:= | Here, the number of the "DB_LOOP" DB that the LP_SCHED instruction is to process is called. Example: "DB_LOOP" where DB_LOOP = name of DB assigned in the symbol table. |
| A "DB_LOOP".LOOP_DAT[1].ENABLE |  |
| SPBN M002 | Control loop call, if ENABLE = TRUE |
| //CALL FBx,DBy |  |
| //COM_RST:= "DB_LOOP".LOOP_DAT[1].COM_RST |  |
| //CYCLE:= "DB_LOOP".LOOP_DAT[1].CYCLE |  |
| CLR |  |
| = "DB_LOOP".LOOP_DAT[1].ENABLE | Reset ENABLE bit |
| M002: | Continuing in the program, e.g., conditional call of the next control loop FB |

#### Startup

When COM_RST = TRUE, the following pre-assignments are set:

| Symbol | Meaning |
| --- | --- |
| Current control loop number: | ALP_NBR = 0 |

The call data of all control loops up to **GLB_NBR** is pre-assigned as follows:

|  |  |  |
| --- | --- | --- |
| Enable: | ENABLE = | NOT MAN_DIS |
| Sampling time: | CYCLE = | GV(MAN_CYC) |
| Restart: | COM_RST = | TRUE |
| Local call number: | ILP_COU = | 0 |
| GV(MAN_CYC) = MAN_CYC is rounded to an integer multiple of TM_BASE*GLP_NBR |  |  |

During CPU startup, you must call LP_SCHED from the associated startup OB and, at the same time, assign the value TRUE to the COM_RST input. Then call PID_CP or PID_ES conditionally to initialize the controllers.

In the cyclic interrupt OB, you must assign the value FALSE to COM_RST again.

### Operating principle of LP_SCHED (S7-300, S7-400)

#### Call processing

A controller should be processed if the respective ENABLE bit in the DB_LOOP data block has the value TRUE. This bit was written previously by LP_SCHED. If the controller was processed, you must assign the value FALSE to the ENABLE bit after processing is complete.

When the controller is called, you must interconnect its input parameters COM_RST and CYCLE with the variables COM_RST[x] and CYCLE[x] of the DB_LOOP data block. CYCLE[x] contains the actual sampling time of the controller x and is written by LP_SCHED during each cycle.

During operation, you can manually disable the call of individual controllers and also reset individual controllers.

![Call processing](images/32398005259_DV_resource.Stream@PNG-en-US.png)

#### Parameter assignment of the DB_LOOP data block

The parameters of the controller call distributor must be assigned in the DB editor.

You must assign parameters to the following variables in the DB_LOOP data block:

- GLP_NBR: Number of controllers whose call is managed by LP_SCHED (max. 256)
- MAN_CYC[x], x = 1 ... GLP_NBR: The desired sampling time for the individual controllers. Note here that the condition indicated below for MAN_CYC[x] applies to each controller. Otherwise, the assigned sampling time cannot be guaranteed.

The following variables can change during operation:

- MAN_DIS[x] is used to disable the call of control loop x during operation.
- MAN_CRST[x] is used to initiate an initialization pass for control loop x during operation.

  The change becomes effective with the next call of the instruction LP_SCHED.

The following variables are written by LP_SCHED:

- LP_SCHED enters the call condition for the controller x in the variable ENABLE[x].
- The ALP_NBR and ILP_COU[x] variables are internal variables of the LP_SCHED instruction. You can use them for monitoring.

The COM_RST[x] and CYCLE[x] variables are interconnected with the input parameters COM_RST and CYCLE of the instructions PID_CP and PID_ES.

#### Sampling time MAN_CYC[x]

LP_SCHED can process a maximum of one controller per call. For this reason, the time

TM_BASE * GLP_NBR, until all controllers have been processed for the first time. Therefore, when you assign parameters for the desired sampling times MAN_CYC[x], you must adhere to the following condition for each controller:

The sampling time of controller x must be an integer multiple of the product obtained from the time base and the number of controllers to be processed.

![Sampling time MAN_CYC[x]](images/32398040971_DV_resource.Stream@PNG-de-DE.png)

The actual sampling time CYCLE[x] of the control loop x is determined as follows by LP_SCHED in each cycle from MAN_CYC[x]:

- If you adhere to this rule, the actual sampling time CYCLE[x] will be identical to the sampling time MAN_CYC[x] you specified previously.
- If you do not adhere to this rule, CYCLE[x] will contain the value that results if MAN_CYC[x] is rounded down to the next integer multiple of TM_BASE * GLP_NBR.

#### Adding additional control loops

If you want to insert one or more control loops into the DB_LOOP data block, increase the start value for GLP_NBR and expand the LOOP_DAT[1...GLP_NBR] array.

Check the desired sampling time MAN_CYC[x] for each controller. At the same time, note the condition for MAN_CYC.

#### Pulse generator in conjunction with LP_SCHED

If you have activated the pulse generator for the continuous controller PID_CP, the pulse pattern width CYCLE_P with the LOOP_DAT[x].CYCLE parameter must be interconnected instead of the CYCLE parameter.

#### Example of a loop schedule

The following example shows the call order of four controllers in a cyclic interrupt OB. A maximum of one controller is processed per unit of the time base TM_BASE. The call order is based on the order of the controllers in the DB_LOOP data block.

![Example of a loop schedule](images/32398017163_DV_resource.Stream@PNG-en-US.png)

#### Call of more than one controller per cycle

If more than one controller is to be processed in a cycle, LP_SCHED may then be called multiple times. All calls of the LP_SCHED instruction must be made before calling the controller. In the input parameter TM_BASE, you must then enter the cycle clock of the cyclic interrupt OB, divided by the number of LP_SCHED calls.

Example: LP_SCHED will be called in OB 35 twice; OB 35 will be processed every 100 ms. The input parameter TM_BASE will be configured with 50 ms.

#### Execution times

The sum of the runtimes of the LP_SCHED instruction and the controller which can be processed in one cycle must not be greater than the cycle clock of the cyclic interrupt OB.

#### Manipulations during operation

The following changes may be made in the "DB_LOOP" data block during operation, provided that only the respective parameter is changed and the complete data block not downloaded to the CPU:

- Disabling individual controllers

  Writing the TRUE value to the MAN_DIS[x] variable disables the processing of controller x during operation. LP_SCHED does not set the ENABLE bit of this controller to TRUE until you write the value FALSE to MAN_DIS[x] again.
- Initializing a control loop

  You can restart an individual controllers by writing the value TRUE to the MAN_CRST[x] variable: In this case, LP_SCHED writes the value TRUE to the COM_RST[x] variable the next time controller x is processed. During the next subsequent processing of this control loop, LP_SCHED writes the value FALSE to the MAN_CRST[x] and COM_RST[x] variables.
- Change in the sampling time of a control loop

  You can change the MAN_CYC[x] parameter during operation:

  > **Note**
  >
  > If the entire DB_LOOP data block is downloaded again to the CPU without requiring a CPU startup, you must pre-assign the internal control loop counters ILP_COU[x], x = 1, ... GLP_NBR and the number of the current control loop ALP_NBR with zero.

#### Monitoring the instruction LP_SCHED

LP_SCHED enters the number of the controller that is to be processed next in the ALP_NBR variable of the DB_LOOP data block. The number of the respective control loop results from the positioning of its call data in the sequence of the entries in the data block.

The ILP_COU[x] variable is the internal counter. It receives the time period until the next call of the corresponding controller. The time unit of ILP_COU is the product obtained from the time base TM_BASE and the number of controllers GLP_NBR. If ILP_COU = 0, LP_SCHED sets the ENABLE bit of the corresponding controller.

#### When control loops are not called contrary to expectation

If LP_SCHED is called but individual control loops are not processed, this can be caused by the following:

- Writing the value TRUE to the MAN_DIS[x] variable disables the processing of control loops during operation.
- The number of controllers to be processed by LP_SCHED specified in the GLP_NBR parameter is too low.
- The sampling times MAN_CYC[x] of the individual control loops that you have specified must not be less than the product obtained from the time base TM_BASE and the number of controllers GLP_NBR. Controllers in which this condition is not met will not be processed.

### Input parameters LP_SCHED (S7-300, S7-400)

| Parameter | Data type | Range of values | Preassigned value | Explanation |
| --- | --- | --- | --- | --- |
| TM_BASE | TIME | ≥ 20 ms (S7-300)  ≥ 5 ms (S7-400) | 100 ms | Time base  (Cycle clock of cyclic interrupt level in which LP_SCHED is called)  Permitted values are |
| COM_RST | BOOL |  | FALSE | Complete restart  (Complete restart routine of LP_SCHED will be processed) |
| DB_NBR | BLOCK_DB |  | DB 1 | Data block number  (DB with the call data of the control loop) |

### Global data block for DB_LOOP (S7-300, S7-400)

The data for the call distribution with LP_SCHED is specified in a global data block. This global data block is not included in the library. You must create the global data block yourself according to the following schema and adapt it to your application.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| GLP_NBR | INT | 2 | Maximum number of controllers 1 - 256 |
| ALP_NBR | INT | 0 | Number of current controllers  0 - 256 |
| LOOP_DAT | Array [1...GLP_NBR] of Struct |  | Structure for the data of the individual controllers. The array must be declared by 1...GLP_NBR. |
| LOOP_DAT[1].MAN_CYC | TIME | T#1s | Data controller 1: Manual sampling time  &gt;= 20 ms (S7-300)  &gt;= 5 ms (S7-400) |
| LOOP_DAT[1].MAN_DIS | BOOL | FALSE | Data controller 1: Disable manual controller call |
| LOOP_DAT[1].MAN_CRST | BOOL | FALSE | Data controller 1: Set manual restart |
| LOOP_DAT[1].ENABLE | BOOL | FALSE | Data controller 1: Controller enable |
| LOOP_DAT[1].COM_RST | BOOL | FALSE | Data controller 1: Restart |
| LOOP_DAT[1].ILP_COU | INT | 0 | Data controller 1: Internal counter |
| LOOP_DAT[1].CYCLE | TIME | T#1s | Data controller 1: Sampling time  &gt;= 20 ms (S7-300)  &gt;= 5 ms (S7-400) |
| LOOP_DAT[2].MAN_CYC |  |  | Data controller 2: Manual sampling time |
| ... |  |  |  |

Alternatively, you can generate the global data block using an external source file. Proceed as follows:

1. Copy the text below to the clipboard.
2. Open an external text editor.
3. Paste the copied text from the clipboard to the text editor.
4. Save the file with the file name extension "DB":
5. Open the "External sources" folder in the project tree of the TIA Portal.
6. Double-click the command "Add new external file".  
   The "Open" dialog is displayed.
7. Navigate to the external source file that you have created and select it.
8. Confirm your selection with "Open".
9. Select the external source file.
10. Select the command "Generate blocks from source" in the shortcut menu.
11. A security prompt informs you that any existing blocks will be overwritten.
12. Click "OK" in response to the security prompt.
13. Adapt the created data block to your application.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DATA_BLOCK "DB_LOOP" |  |  |  |  |
| TITLE = data block loop scheduler |  |  |  |  |
| { S7_Optimized_Access := 'FALSE' } |  |  |  |  |
| NAME : DB_LOOP |  |  |  |  |
|  | STRUCT |  |  |  |
|  |  | GLP_NBR : Int; |  | // greatest loop number |
|  |  | ALP_NBR : Int; |  | // actual loop number |
|  |  | LOOP_DAT : Array[1..2] of Struct |  |  |
|  |  |  | MAN_CYC : Time; | // loop data: manual sample time |
|  |  |  | MAN_DIS : Bool; | // loop data: manual loop disable |
|  |  |  | MAN_CRST : Bool; | // loop data: manual complete restart |
|  |  |  | ENABLE : Bool; | // loop data: enable loop |
|  |  |  | COM_RST : Bool; | // loop data: complete restart |
|  |  |  | ILP_COU : Int; | // loop data: internal loop counter |
|  |  |  | CYCLE : Time; | // loop data: sample time |
|  |  | END_STRUCT; |  |  |
|  | END_STRUCT; |  |  |  |

|  |  |  |
| --- | --- | --- |
| BEGIN |  |  |
|  | GLP_NBR := 2; |  |
|  | LOOP_DAT[1].MAN_CYC := T#1S; |  |
|  | LOOP_DAT[1].CYCLE := T#1S; |  |
|  | LOOP_DAT[2].MAN_CYC := T#200MS; |  |
|  | LOOP_DAT[2].CYCLE := T#200MS; |  |
| END_DATA_BLOCK |  |  |
