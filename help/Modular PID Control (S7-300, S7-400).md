---
title: "Modular PID Control (S7-300, S7-400)"
package: ProgFBPIDModenUS
topics: 125
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Modular PID Control (S7-300, S7-400)

This section contains information on the following topics:

- [General (S7-300, S7-400)](#general-s7-300-s7-400)
- [A_DEAD_B (S7-300, S7-400)](#a_dead_b-s7-300-s7-400)
- [CRP_IN (S7-300, S7-400)](#crp_in-s7-300-s7-400)
- [CPR_OUT (S7-300, S7-400)](#cpr_out-s7-300-s7-400)
- [DEAD_T (S7-300, S7-400)](#dead_t-s7-300-s7-400)
- [DEADBAND (S7-300, S7-400)](#deadband-s7-300-s7-400)
- [DIF (S7-300, S7-400)](#dif-s7-300-s7-400)
- [ERR_MON (S7-300, S7-400)](#err_mon-s7-300-s7-400)
- [INTEG (S7-300, S7-400)](#integ-s7-300-s7-400)
- [LAG1ST (S7-300, S7-400)](#lag1st-s7-300-s7-400)
- [LAG2ND (S7-300, S7-400)](#lag2nd-s7-300-s7-400)
- [LIMALARM (S7-300, S7-400)](#limalarm-s7-300-s7-400)
- [LIMITER (S7-300, S7-400)](#limiter-s7-300-s7-400)
- [LMNGEN_C (S7-300, S7-400)](#lmngen_c-s7-300-s7-400)
- [LMNGEN_S (S7-300, S7-400)](#lmngen_s-s7-300-s7-400)
- [NONLIN (S7-300, S7-400)](#nonlin-s7-300-s7-400)
- [NORM (S7-300, S7-400)](#norm-s7-300-s7-400)
- [OVERRIDE (S7-300, S7-400)](#override-s7-300-s7-400)
- [PARA_CTL (S7-300, S7-400)](#para_ctl-s7-300-s7-400)
- [PID (S7-300, S7-400)](#pid-s7-300-s7-400)
- [PULSEGEN_M (S7-300, S7-400)](#pulsegen_m-s7-300-s7-400)
- [RMP_SOAK (S7-300, S7-400)](#rmp_soak-s7-300-s7-400)
- [ROC_LIM (S7-300, S7-400)](#roc_lim-s7-300-s7-400)
- [SCALE_M (S7-300, S7-400)](#scale_m-s7-300-s7-400)
- [SP_GEN (S7-300, S7-400)](#sp_gen-s7-300-s7-400)
- [SPLT_RAN (S7-300, S7-400)](#splt_ran-s7-300-s7-400)
- [SWITCH (S7-300, S7-400)](#switch-s7-300-s7-400)
- [LP_SCHED_M (S7-300, S7-400)](#lp_sched_m-s7-300-s7-400)

## General (S7-300, S7-400)

### Conventions for parameter and block names in the block diagram

Not more than 8 characters were selected for the parameter designations.

The following conventions apply for the designation of the parameters:

| Initial character: |  |
| --- | --- |
| Q | General output of the BOOL type (Boolean variable) |
| SP | Reference variable |
| PV | Measured value or controlled variable |
| LMN | Manipulated variable or analog output signal to be output |
| DISV | Disturbance variable |
| **Subsequent characters**: |  |
| MAN | Manual value |
| INT | Internal |
| EXT | External |
| _ON | Boolean variable for activating a function |

### Call data

Most Modular PID Control instructions require control-loop-specific call data such as the restart bit and sampling time. These values are transferred to the inputs COM_RST and CYCLE.

**Remarks on the block parameter bars (input, output, and in/out parameters)**

- **Preassigned value:** The preassigned values for the creation of an instance are displayed here.
- **Range of values**: The values at the input parameter should not exceed the permitted range of values. The range is **not** checked in the course of the block execution. If a range of engineering values is specified, a physical variable whose value should lie between approx. ±10 <sup>6</sup> is meant.

## A_DEAD_B (S7-300, S7-400)

This section contains information on the following topics:

- [Description A_DEAD_B (S7-300, S7-400)](#description-a_dead_b-s7-300-s7-400)
- [Input parameters A_DEAD_B (S7-300, S7-400)](#input-parameters-a_dead_b-s7-300-s7-400)
- [Output parameters A_DEAD_B (S7-300, S7-400)](#output-parameters-a_dead_b-s7-300-s7-400)

### Description A_DEAD_B (S7-300, S7-400)

If the process value is affected by noise and the controller is optimally set, the noise also affects the controller output. This results in increased wear of the actuator through a high frequency of operation (step controllers). Oscillation of the controller output is avoided by suppression of the noise component.

#### Operating principle

The instruction filters high-frequency interfering signals from the control deviation and produces a deadband around the zero point. If the input variable lies within this range, zero is output at the output. The range width is adapted automatically to the amplitude of the interfering signal.

The instruction operates in accordance with the function:

|  |  |  |
| --- | --- | --- |
| OUTV = INV + DB_WIDTH | for | INV < -DB_WIDTH |
| OUTV = 0.0 | for | -DB_WIDTH ≤ INV ≤ +DB_WIDTH |
| OUTV = INV - DB_WIDTH | for | INV > +DB_WIDTH |

![Operating principle](images/18026471947_DV_resource.Stream@PNG-de-DE.png)

#### Adaptation of the deadband

The adaptation of the deadband can be activated and deactivated.

- Adaptation off

  If the adaptation is deactivated (ADAPT_ON = FALSE), the last DB_WIDTH value is frozen as the effective deadband width DB_WIDTH.
- Adaptation on

  With ADAPT_ON = TRUE, an adaptation algorithm that calculates the effective deadband width can be activated. The effect is that the deadband width is adapted to the amplitude of the noise signal that is superimposed on the input variable, so that the noise component is also suppressed at a fluctuating noise amplitude.

  In the case of an acyclic block call, the adaptation has to be deactivated (ADAP_ON = FALSE).

If adaptation is activated during commissioning and a stable deadband width is set after a certain time, the adaptation can be deactivated. The deadband width set through the adaptation remains in force as long as a complete restart is not carried out.

#### Adaptation on

To ensure stability, the effective deadband width DB_WIDTH is subject to a low limit, which is represented by the DB_WL_LM value that can be specified at the input bar. If input signal INV superimposed by the measurement noise exceeds the currently specified deadband width in the negative (1), positive (2), and again negative direction (3) within the period 1/CRIT_FRQ, the effective deadband width is increased by the amount 0.1.

![Adaptation on](images/18026494731_DV_resource.Stream@PNG-de-DE.png)

The procedure is started if the limit is exceeded positively or negatively. Whenever the opposing deadband width is exceeded again (3 -> 4) within half the cycle duration, it is increased again by 0.1. This procedure is repeated until the deadband width agrees with the amplitude of the measurement noise. In order not to indiscriminately suppress input signals of any size, the effective deadband width is subject to a high limit, which is represented by input DB_WH_LM. If, on the other hand, the deadband width is not exceeded within time RET_FAC * 1/CRIT_FRQ, it is reduced by the amount 0.1.

CRIT_FRQ specifies the limit frequency from which a signal component is regarded as a disturbance. It is subject to a high limit and low limit as follows:

0.01 ≤ CRIT_FRQ ≤ 1/(3*CYCLE) where CYCLE: Sampling time in sec

The RET_FAC parameter specifies the multiple of 1/CRIT_FRQ based on which the deadband width is reduced again.

The adaptation logic only functions if the input variable without disturbance component lies near zero.

![Adaptation on](images/18026483339_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

At a complete restart, OUTV=0.0 is set, and the effective deadband width DB_WIDTH = DB_WL_LM is set

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Generating and processing the control deviation (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#generating-and-processing-the-control-deviation-s7-300-s7-400)

### Input parameters A_DEAD_B (S7-300, S7-400)

| Parameter | Data type | Preassigned value | Description |
| --- | --- | --- | --- |
| INV | REAL | 0.0 | Input variable  Engineering value range |
| DB_WH_LM | REAL | 5.0 | High limit of the deadband width  Engineering value range  DB_WH_LM > DB_WL_LM |
| DB_WL_LM | REAL | 1.0 | Low limit of the deadband width   Engineering value range  DB_WL_LM < DB_WH_LM |
| CRIT_FRQ | REAL | 0.1 | Limit frequency  CRIT_FRQ ≥ 0.01 and  CRIT_FRQ ≤ 1/(3 * CYCLE) |
| RET_FAC | INT | 1 | Return factor  RET_FAC ≥ 1 |
| ADAPT_ON | BOOL | FALSE | Activate adaptation algorithm |
| COM_RST | BOOL | FALSE | Restart |
| CYCLE | TIME | T#1s | Sampling time  CYCLE ≥ 1ms |

### Output parameters A_DEAD_B (S7-300, S7-400)

| Parameter | Data type | Preassigned value | Description |
| --- | --- | --- | --- |
| OUTV | REAL | 0.0 | Output variable |
| DB_WIDTH | REAL | 0.0 | Effective deadband width |

## CRP_IN (S7-300, S7-400)

This section contains information on the following topics:

- [Description CRP_IN (S7-300, S7-400)](#description-crp_in-s7-300-s7-400)
- [Input parameters CRP_IN (S7-300, S7-400)](#input-parameters-crp_in-s7-300-s7-400)
- [Output parameters CRP_IN (S7-300, S7-400)](#output-parameters-crp_in-s7-300-s7-400)

### Description CRP_IN (S7-300, S7-400)

This instruction adapts the range of values of the analog I/O to the internal representation of the modular control. The instruction can be called in the process value branch, for example.

#### Operating principle

CRP_IN converts an input value in I/O format into a scaled floating-point value of the modular control.

| I/O value | Output value as a % |
| --- | --- |
| 32767 | 118.515 |
| 27648 | 100.000 |
| 1 | 0.003617 |
| 0 | 0.000 |
| -1 | -0.003617 |
| -27648 | -100.000 |
| -32768 | -118.519 |

The floating-point value can be adapted by means of a scaling factor and an offset. The output results from:

OUTV = INV_PER * 100/27648 * FACTOR + OFFSET

> **Note**
>
> A check for positive/negative overflow is not performed.

#### Using a commissioning value

It is possible to switch over to a commissioning value for purposes of commissioning or testing or in case of I/O faults. If START_ON = TRUE, the value in STARTVAL is output at output OUTV.

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#applying-the-disturbance-variable-s7-300-s7-400)
  
[Processing position feedback (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-position-feedback-s7-300-s7-400)

### Input parameters CRP_IN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV_PER | 0.0 | WORD | 0 | Input variable for I/O  Engineering value range |
| FACTOR | 2.0 | REAL | 1.0 | Scaling factor |
| OFFSET | 6.0 | REAL | 0.0 | Offset  Engineering value range |
| START_ON | 10.0 | BOOL | TRUE | Activate commissioning value |
| STARTVAL | 12.0 | REAL | 0.0 | Commissioning value  Engineering value range |

### Output parameters CRP_IN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 16.0 | REAL | 0.0 | Output variable |

## CPR_OUT (S7-300, S7-400)

This section contains information on the following topics:

- [Description CRP_OUT (S7-300, S7-400)](#description-crp_out-s7-300-s7-400)
- [Input parameters CRP_OUT (S7-300, S7-400)](#input-parameters-crp_out-s7-300-s7-400)
- [Output parameters CRP_OUT (S7-300, S7-400)](#output-parameters-crp_out-s7-300-s7-400)

### Description CRP_OUT (S7-300, S7-400)

This instruction adapts a floating-point value of the modular control to the I/O format.

#### Operating principle

CRP_OUT converts an input value (scaled floating-point value of the modular control) into the I/O format of the analog I/O.

| Input value in % | I/O value |
| --- | --- |
| 118.515 | 32767 |
| 100.000 | 27648 |
| 0.003617 | 1 |
| 0.000 | 0 |
| -0.003617 | -1 |
| -100.000 | -27648 |
| -118.519 | -32768 |

The floating-point value can be adapted by means of a scaling factor and an offset. The output results from:

OUTV_PER = (INV * FACTOR + OFFSET) * 27648/100

> **Note**
>
> A check for positive/negative overflow is not performed.

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Creating a continual controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-continual-controller-s7-300-s7-400)

### Input parameters CRP_OUT (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| FACTOR | 4.0 | REAL | 1.0 | Scaling factor |
| OFFSET | 8.0 | REAL | 0.0 | Offset  Engineering value range |

### Output parameters CRP_OUT (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV_PER | 12.0 | WORD | 0 | Output variable for I/O |

## DEAD_T (S7-300, S7-400)

This section contains information on the following topics:

- [Description DEAD_T (S7-300, S7-400)](#description-dead_t-s7-300-s7-400)
- [Input parameters DEAD_T (S7-300, S7-400)](#input-parameters-dead_t-s7-300-s7-400)
- [Output parameters DEAD_T (S7-300, S7-400)](#output-parameters-dead_t-s7-300-s7-400)
- [Global data block DB_DEADT (S7-300, S7-400)](#global-data-block-db_deadt-s7-300-s7-400)

### Description DEAD_T (S7-300, S7-400)

This instruction is used in ratio control systems in which the individual components on transport routes of different lengths are brought together.

#### Operating principle

The instruction delays the output of an input value by an assignable time (dead time). In the case of online changes in the dead time steps can occur at the output value,

The input values are stored temporarily in a global data block.

[Global data block DB_DEADT](#global-data-block-db_deadt-s7-300-s7-400) is not included in the library. You must create this global data block yourself.

The global data block must contain an Array [0..n<sub>max</sub>] of real.

n<sub>max</sub> is determined by the dead time DEAD_TM and sampling time CYCLE of the DEAD_T. instruction. The following applies:

- DEAD_TM must be an integer multiple of CYCLE.
- n<sub>max</sub>=DEAD_TM/CYCLE

In cycle n, the saved input value INV[n] is read from the global data block and output to OUTV. INV[n] is overwritten with the current input value. Counter n is increased by 1. When n = n<sub>max</sub>, the counter is reset to 0. You specify the number of the global block in input parameter DB_NBR.

#### Example

At a sampling time of CYCLE=1s and a dead time of DEAD_TM=5s, 5 input values must be buffered. The data area must have a length of 20 bytes.

The data in the global data block are processed like in a ring buffer.

| Cycle no. | Counter n | INV of instruction | Tag in global data block | Value of INVI[n] at start of cycle | OUTV of instruction | Value of  INVI [n] at end of cycle |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 80.0 | INVI[0] | 0.0 | 0.0 | 80.0 |
| 1 | 1 | 100.0 | INVI[1] | 0.0 | 0.0 | 100.0 |
| 2 | 2 | 100.0 | INVI[2] | 0.0 | 0.0 | 100.0 |
| 3 | 3 | 80.0 | INVI[3] | 0.0 | 0.0 | 80.0 |
| 4 | 4 | 0.0 | INVI[4] | 0.0 | 0.0 | 0.0 |
| 5 | 0 | 0.0 | INVI[0] | 80.0 | 80.0 | 0.0 |
| 6 | 1 | 0.0 | INVI[1] | 100.0 | 100.0 | 0.0 |
| 7 | 2 | 0.0 | INVI[2] | 100.0 | 100.0 | 0.0 |
| 8 | 3 | 10.0 | INVI[3] | 80.0 | 80.0 | 10.0 |
| 9 | 4 | 100.0 | INVI[4] | 0.0 | 0.0 | 100.0 |

The value of INV in cycle 0 is not output at OUTVuntil cycle 5. With a sampling time of 1 s, the output is thus delayed by the dead time of 5 s.

#### Tracking

When TRACK=TRUE, the input value is output at OUTV without a delay. Buffering of the input values is not interrupted so that, after tracking has been deactivated, the input values can continue to be output after the set dead time. On a falling edge at TRACK, OUTV jumps to INV[DEAD_TM]!

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

> **Note**
>
> The instruction does not check whether a global DB with the number DB_NBR actually exists or whether the parameters DEAD_TM (dead time) and CYCLE (sampling time) are suitable for the data block length. If the parameter assignment is incorrect, the CPU changes to the STOP operating mode with the message "Internal system error".

#### Restart

During a restart, all saved input values are deleted and OUTV=0.0 is output.

### Input parameters DEAD_T (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| DB_NBR | 4.0 | BLOCK_DB | DB 1 | Data block number |
| DEAD_TM | 6.0 | TIME | 10s | Dead time  DEAD_TM ≥ CYCLE |
| TRACK | 10.0 | BOOL | FALSE | Tracking OUTV = INV |
| COM_RST | 10.1 | BOOL | FALSE | Complete restart |
| CYCLE | 12.0 | TIME | 1s | Sampling time  CYCLE ≥ 1ms |

### Output parameters DEAD_T (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 16.0 | REAL | 0.0 | Output variable |

### Global data block DB_DEADT (S7-300, S7-400)

The input values for the dead time element DEAD_T are stored temporarily in a global data block. This global data block is not included in the library. You must create the global data block yourself according to the following schema and adapt it to your application.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| INVI | Array[0..n<sub>max</sub>] of real | 0.0 | Input value [n]   Engineering value range |

Alternatively, you can generate the global data block using an external source file. Proceed as follows:

1. Copy the text below to the clipboard.
2. Open an external text editor.
3. Paste the copied text from the clipboard to the text editor.
4. Save the file with the file name extension "DB":
5. Open the "External sources" folder in the project tree of the TIA Portal.
6. Double-click the command "Add new external file". The "Open" dialog is displayed.
7. Navigate to the external source file that you have created and select it.
8. Confirm your selection with "Open".
9. Select the external source file.
10. Select the command "Generate blocks from source" in the shortcut menu.
11. A security prompt informs you that any existing blocks will be overwritten.
12. Click "OK" in response to the security prompt.
13. Adapt the created data block to your application.

|  |  |  |
| --- | --- | --- |
| DATA_BLOCK "DB_DEADT" |  |  |
| TITLE = data block dead time |  |  |
| { S7_Optimized_Access := 'FALSE' } |  |  |
| NAME : DB_DEADT |  |  |
|  | STRUCT |  |
|  |  | INVI : Array[0..4] of Real; |
|  | END_STRUCT; |  |
| BEGIN |  |  |
| END_DATA_BLOCK |  |  |

## DEADBAND (S7-300, S7-400)

This section contains information on the following topics:

- [Description DEADBAND (S7-300, S7-400)](#description-deadband-s7-300-s7-400)
- [Input parameters DEADBAND (S7-300, S7-400)](#input-parameters-deadband-s7-300-s7-400)
- [Output parameters DEADBAND (S7-300, S7-400)](#output-parameters-deadband-s7-300-s7-400)

### Description DEADBAND (S7-300, S7-400)

If the process value is affected by noise and the controller is optimally set, the noise also affects the controller output. This results in increased wear of the actuator through a high frequency of operation (step controllers). Oscillation of the controller output is avoided by suppression of the noise component.

#### Operating principle

The DEADBAND instruction suppresses minor fluctuations of input variable INV around a defined zero point. Outside these fluctuations, output variable OUTV rises proportionally to the input variable. It operates in accordance with the function:

|  |  |  |
| --- | --- | --- |
| OUTV = INV + DEADB_W - DEADB_O | for | INV < DEADB_O - DEADB_W |
| OUTV = 0.0 | for | DEADB_O - DEADB_W ≤ INV |
| and | INV ≤ DEADB_O + DEADB_W |  |
| OUTV = INV - DEADB_W - DEADB_O | for | INV > DEADB_O + DEADB_W |

The signal corruption corresponds to the value DEADB_W. The center of the deadband is defined with DEADB_O.

![Operating principle](images/18026570123_DV_resource.Stream@PNG-de-DE.png)

Deadband width DEADB_W and deadband offset DEADB_O can be assigned. When used for generating the control deviation, offset DEADB_O=0.0 must be set.

The following figure shows the bypassing of a noise component with offset

![Operating principle](images/18026581515_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check. Only positive values are permitted for the deadband width.

---

**See also**

[Generating and processing the control deviation (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#generating-and-processing-the-control-deviation-s7-300-s7-400)

### Input parameters DEADBAND (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| DEADB_W | 4.0 | REAL | 1.0 | Deadband width  Engineering value range and ≥ 0.0 |
| DEADB_O | 8.0 | REAL | 0.0 | Deadband offset  Engineering value range |

### Output parameters DEADBAND (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 12.0 | REAL | 0.0 | Output variable |

## DIF (S7-300, S7-400)

This section contains information on the following topics:

- [Description DIF (S7-300, S7-400)](#description-dif-s7-300-s7-400)
- [Input parameters DIF (S7-300, S7-400)](#input-parameters-dif-s7-300-s7-400)
- [Output parameters DIF (S7-300, S7-400)](#output-parameters-dif-s7-300-s7-400)

### Description DIF (S7-300, S7-400)

Process variables are differentiated dynamically. Thus, for example, the velocity can be calculated from the distance traversed. The differentiator can be used for disturbance variable compensation, for feedforward control, and to structure a controller.

#### Operating principle

This instruction differentiates the input variable with respect to time and smoothes the signal with a first-order delay element. It operates in the Laplace domain according the following transfer function:

- OUTV(s) / INV(s) = TD / (1+TM_LAG*s)

The time response is defined by the derivative-action time TD and the time delay TM_LAG. The following figures show the step response of DIF.

![Operating principle](images/18026608907_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| TD | Derivative-action time |
| TM_LAG | Time delay |
| INV0 | Input step height |
| INV | Input variable |
| OUTV | Output variable |

If TM_LAG ≤CYCLE/2 is assigned, DIF works without a delay. An input step-change is applied to the output with the factor TD**/**CYCLE. After one cycle the output returns to 0.0.

![Operating principle](images/18026624907_DV_resource.Stream@PNG-de-DE.png)

#### Block-internal limits

The derivative-action time is subject to a low limit equal to the sampling time. The time delay is subject to a low limit equal to half the sampling time.

|  |  |  |
| --- | --- | --- |
| TD<sub>intern</sub> = CYCLE | for | TD < CYCLE |
| TM_LAG<sub>intern</sub> = CYCLE/2 | for | TM_LAG < CYCLE/2 |

The other values of the input parameters are not limited in the instruction. There is no parameter check.

#### Complete restart

During a complete restart, all the signal outputs are set to 0. The differentiator is preassigned internally with the current input value INV. The transition to normal operation is thus smooth at a constant input variable.

---

**See also**

[Applying the disturbance variable (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#applying-the-disturbance-variable-s7-300-s7-400)

### Input parameters DIF (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| TD | 4.0 | TIME | T#25s | Derivative-action time  ≥ CYCLE |
| TM_LAG | 8.0 | TIME | T#5s | Time delay |
| COM_RST | 12.0 | BOOL | FALSE | Complete restart |
| CYCLE | 14.0 | TIME | T#1s | Sampling time  ≥ 1ms |

### Output parameters DIF (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 18.0 | REAL | 0.0 | Output variable |

## ERR_MON (S7-300, S7-400)

This section contains information on the following topics:

- [Description ERR_MON (S7-300, S7-400)](#description-err_mon-s7-300-s7-400)
- [Input parameters ERR_MON (S7-300, S7-400)](#input-parameters-err_mon-s7-300-s7-400)
- [Output parameters ERR_MON (S7-300, S7-400)](#output-parameters-err_mon-s7-300-s7-400)

### Description ERR_MON (S7-300, S7-400)

This instruction is used for control deviation generation and monitoring.

#### Operating principle

The instruction calculates control deviation ER = SP - PV and monitors it for assignable limits. As a result of a setpoint change |ΔSP| > SP_DIFF, the response of limit value signal ER_LM is suppressed for an assignable delay time (TM_DELAY+TM_RAMP). During this time, ER is monitored for the higher limit value ER_LMTD. If ER_LMTD is exceeded, QER_LMTD=TRUE is output. After the delay time has expired, ER_LMTD is transformed into ER_LM along a ramp. The slope of the ramp can be assigned in the TM_RAMP parameter.

![Operating principle](images/18026652299_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |  |
| --- | --- | --- | --- |
| PV: | Process value | TM_DELAY: | On delay of the monitoring signal |
| SP: | Setpoint |  |  |
| ER: | Control deviation | TM_RAMP: | Ramp time constant |
| ER_LM: | Limit value of the control deviation | QER_LM: | Limit value of the control deviation triggered |
| ER_LMTD: | Limit value of the control deviation during On delay | QER_LMTD: | Limit value of the control deviation during On delay and ramp triggered |
| ① | Suppression of the limit value signal | ② | Ramp function |

#### Complete restart

During a complete restart, alarm signals QER_LM and QER_LMTD and control deviation output ER are reset.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Generating and processing the control deviation (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#generating-and-processing-the-control-deviation-s7-300-s7-400)

### Input parameters ERR_MON (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| ER_LM | 0.0 | REAL | 10.0 | Limit value of the control deviation  Engineering value range and > 0.0 and < ER_LMTD |
| ER_LMTD | 4.0 | REAL | 100.0 | Limit value of the control deviation during On delay  Engineering value range and > ER_LM |
| SP | 8.0 | REAL | 0.0 | Setpoint  Engineering value range |
| PV | 12.0 | REAL | 0.0 | Controlled variable  Engineering value range |
| SP_DIFF | 16.0 | REAL | 10.0 | Setpoint change  Engineering value range and > 0.0 |
| TM_DELAY | 20.0 | TIME | T#60s | On delay of the monitoring signal |
| TM_RAMP | 24.0 | TIME | T#60s | Ramp time constant |
| COM_RST | 28.0 | BOOL | FALSE | Complete restart |
| CYCLE | 30.0 | TIME | T#1s | Sampling time  ≥ 1ms |

### Output parameters ERR_MON (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| QER_LM | 34.0 | BOOL | FALSE | Limit value of the control deviation triggered |
| QER_LMTD | 34.1 | BOOL | FALSE | Limit value of the control deviation during On delay and the ramp triggered |
| ER | 36.0 | REAL | 0.0 | Control deviation |

## INTEG (S7-300, S7-400)

This section contains information on the following topics:

- [Description INTEG (S7-300, S7-400)](#description-integ-s7-300-s7-400)
- [Input parameters INTEG (S7-300, S7-400)](#input-parameters-integ-s7-300-s7-400)
- [Output parameters INTEG (S7-300, S7-400)](#output-parameters-integ-s7-300-s7-400)

### Description INTEG (S7-300, S7-400)

Process variables are integrated dynamically. Thus, for example, the distance traversed is calculated from the velocity. This instruction can be used to set up a controller with integral component.

#### Operating principle

The instruction integrates the input variable with respect to time and limits the integral to a definable preassigned high and low limit. Limiting of the output variable is indicated by means of message bits.

The instruction contains the following functions:

| Functions | DFOUT_ON | HOLD |
| --- | --- | --- |
| Integrate | FALSE | FALSE |
| Freeze integral component | FALSE | TRUE |
| Preassign output | TRUE | Any |

- **Integrate**

  During integration, the instruction works in accordance with the following transfer function:

  In the Laplace domain:

  OUTV(s) / INV(s) = 1 / (TI*s)

  The time response of the integral component is determined by the integral-action time TI. The associated step response is shown in the figure below.

  ![Operating principle](images/18026684299_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | T1: | Integral-action time |
  | INV0: | Input step height |
  | t: | Time |
  | INV: | Input variable |
  | OUTV: | Output variable |

The output as well as the memory of the integral component are limited based on the H_LM and L_LM parameters. If the output is outside the range L_LM...H_LM the message bits QH_LM or QL_LM are set to TRUE.

- **Freeze integrator**

  With HOLD = TRUE, the integral component remains at its current output value OUTV. On reset (HOLD = FALSE), integration is continued starting from the current output value OUTV.
- **Preassign output**

  If DFOUT_ON = TRUE is set, DF_OUTV is output at the output. Limit is effective. On reset (DF_OUTV_ON = FALSE), INTEG starts integrating from value DF_OUTV.

The following figure shows an example with DFOUT_ON, HOLD, and limiting

![Operating principle](images/18026700299_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

During a complete restart, output OUTV is reset to 0.0. If DFOUT_ON = TRUE is set, DF_OUTV is output. Limiting of the output and its display are also in effect when a complete restart occurs. On transition to normal operation, the instruction continues to integrate from OUTV.

If the integral component is to be started from a specific operating point on a complete restart, the operating point must be entered in input DF_OUTV. When the instruction is called in the complete restart routine, DFOUT_ON= TRUE must be set and reset back to DFOUT_ON= FALSE in the cyclic interrupt level.

#### Block-internal limits

The integral-action time is subject to a low limit equal to the sampling time.

|  |  |  |
| --- | --- | --- |
| TI<sub>intern</sub> = CYCLE | for | TI < CYCLE |

The other values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters INTEG (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| H_LM | 4.0 | REAL | 100.0 | High limit  Engineering value range  H_LM > L_LM |
| L_LM | 8.0 | REAL | 0.0 | Low limit  Engineering value range  L_HM < H_LM |
| TI | 12.0 | TIME | T#25s | Integral-action time  TI ≥ CYCLE |
| DF_OUTV | 16.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| HOLD | 20.0 | BOOL | FALSE | Freeze integral component |
| DFOUT_ON | 20.1 | BOOL | FALSE | Default setting of output variable On |
| COM_RST | 20.2 | BOOL | FALSE | Complete restart |
| CYCLE | 22.0 | TIME | T#1s | Sampling time  CYCLE ≥ 1ms |

### Output parameters INTEG (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 26.0 | REAL | 0.0 | Output variable |
| QH_LM | 30.0 | BOOL | FALSE | High limit triggered |
| QL_LM | 30.1 | BOOL | FALSE | Low limit triggered |

## LAG1ST (S7-300, S7-400)

This section contains information on the following topics:

- [Description LAG1ST (S7-300, S7-400)](#description-lag1st-s7-300-s7-400)
- [Input parameters LAG1ST (S7-300, S7-400)](#input-parameters-lag1st-s7-300-s7-400)
- [Output parameters LAG1ST (S7-300, S7-400)](#output-parameters-lag1st-s7-300-s7-400)

### Description LAG1ST (S7-300, S7-400)

This instruction can be used as a first-order delay and smoothing element. The time delay is parameterizable.

#### Operating principle

The instruction smoothes the input variable according to the first-order delay and contains the following functions:

| Functions | DFOUT_ON | TRACK |
| --- | --- | --- |
| Smoothing | FALSE | FALSE |
| Tracking | FALSE | TRUE |
| Preassign output | TRUE | Any |

- **Smoothing**

  With smoothing, the instruction operates in the Laplace domain in accordance with the following transfer function:

  OUTV(s) / INV(s) = 1 / (1+TM_LAG*s)

  The time response of the delay element is determined by the time delay TM_LAG. The associated step response is shown in the figure below.

  ![Operating principle](images/18026732299_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | INV | Input variable |
  | OUTV | Output variable |
  | INV0 | Input step height |
  | TM_LAG | Time delay |
- **Tracking**

  With TRACK = TRUE, input value INV is switched through to output OUTV.
- **Preassign output**

  If DFOUT_ON = TRUE is set, DF_OUTV is output at the output. On reset (DF_OUTV_ON = FALSE), the delay element smoothes starting from value DF_OUTV**.**

  The following diagram shows the effect of DFOUT_ON and TRACK.

  ![Operating principle](images/18026748299_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

During a complete restart, output OUTV is reset to 0.0. If DFOUT_ON = TRUE is set, DF_OUTV is output. On transition to smoothing, the instruction continues to operate from OUTV.

#### Block-internal limits

The time delay is subject to a low limit equal to half the sampling time.

|  |  |  |
| --- | --- | --- |
| TM_LAG<sub>intern </sub>= CYCLE/**2** | for | TM_LAG < CYCLE/**2** |

The other values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)
  
[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#applying-the-disturbance-variable-s7-300-s7-400)

### Input parameters LAG1ST (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| TM_LAG | 4.0 | TIME | T#25s | Time delay |
| DF_OUTV | 8.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| TRACK | 12.0 | BOOL | FALSE | Tracking OUTV=INV |
| DFOUT_ON | 12.1 | BOOL | FALSE | Default setting of output variable On |
| COM_RST | 12.2 | BOOL | FALSE | Complete restart |
| CYCLE | 14.0 | TIME | T#1s | Sampling time  ≥1ms |

### Output parameters LAG1ST (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 18.0 | REAL | 0.0 | Output variable |

## LAG2ND (S7-300, S7-400)

This section contains information on the following topics:

- [Description LAG2ND (S7-300, S7-400)](#description-lag2nd-s7-300-s7-400)
- [Input parameters LAG2ND (S7-300, S7-400)](#input-parameters-lag2nd-s7-300-s7-400)
- [Output parameters LAG2ND (S7-300, S7-400)](#output-parameters-lag2nd-s7-300-s7-400)

### Description LAG2ND (S7-300, S7-400)

This instruction is used to simulate controlled system components for feedforward controls and two-circuit control systems.

#### Operating principle

The instruction implements an oscillating second-order delay element and contains the following functions:

| Functions | DFOUT_ON | TRACK |
| --- | --- | --- |
| Transferring | FALSE | FALSE |
| Tracking | FALSE | TRUE |
| Preassign output | TRUE | Any |

- **Transferring**

  The transfer function in the Laplace domain is:

  OUTV(s) / INV(s) = TRANCOEF / (1 + 2*DAM_COEF*TM_CONST*s + TM_CONST<sup>2</sup>*s2)

  If DAM_COEF >= 1 (aperiodic case), the transfer element can be represented in a series connection of two first-order delay elements.

  OUTV(s) / INV(s) = TRANCOEF / (1 + T1*s) * 1 / (1 + T2 * s)

  The time constants are converted as follows:

  ![Operating principle](images/18027894923_DV_resource.Stream@PNG-de-DE.png)

  The figure below shows the block diagram.

  ![Operating principle](images/18026780299_DV_resource.Stream@PNG-de-DE.png)

  The following figure shows the step response of the oscillating LAG2ND element.

  ![Operating principle](images/18026791691_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | INV | Input variable |
  | OUTV | Output variable |
  | TRANCOEF | Transfer constant |
  | DAM_COEF | Damping constant |
  | phi | Supplement angle |
- **Tracking**

  If TRACK =TRUE, OUTV = INV; the internal historical values are set to INV.
- **Preassign output**

  If DFOUT_ON =TRUE, DF_OUTV is output; the internal historical values are set to DF_OUTV. DFOUT_ON has higher priority than TRACK.

#### Complete restart

During a complete restart, output OUTV is reset to 0.0. If DFOUT_ON = TRUE, DF_OUTV is output.

#### Block-internal limits

The time constant TM_CONST is subject to a low limit equal to half the sampling time.

|  |  |  |
| --- | --- | --- |
| TM_CONST<sub>intern</sub>= CYCLE/2 | for | TM_CONST < CYCLE/2 |

The other values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters LAG2ND (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| TM_CONST | 4.0 | TIME | T#10s | Time constant |
| DAM_COEF | 8.0 | REAL | 1.0 | Damping constant |
| TRANCOEF | 12.0 | REAL | 1.0 | Transfer constant |
| DF_OUTV | 16.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| DFOUT_ON | 20.0 | BOOL | FALSE | Default setting of output variable On |
| TRACK | 20.1 | BOOL | FALSE | Tracking OUTV=INV |
| COM_RST | 20.2 | BOOL | FALSE | Complete restart |
| CYCLE | 22.0 | TIME | T#1s | Sampling time  ≥ 1ms |

### Output parameters LAG2ND (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 26.0 | REAL | 0.0 | Output variable |

## LIMALARM (S7-300, S7-400)

This section contains information on the following topics:

- [Description LIMALARM (S7-300, S7-400)](#description-limalarm-s7-300-s7-400)
- [Input parameters LIMALARM (S7-300, S7-400)](#input-parameters-limalarm-s7-300-s7-400)
- [Output parameters LIMALARM (S7-300, S7-400)](#output-parameters-limalarm-s7-300-s7-400)

### Description LIMALARM (S7-300, S7-400)

Illegal or dangerous states can occur in a system if process variables (for example, motor speed, temperature or pressure) exceed or fall below critical values. Such limit violations must be detected and signaled to allow an appropriate reaction.

The instruction checks input variable INV for 4 assignable limits. If one of these limits is reached and exceeded, a limit signal is output. A hysteresis can be set for the off threshold.

#### Operating principle

The limits are set at inputs H_LM_ALM, H_LM_WRN, L_LM_WRN, and L_LM_ALM. If input variable INV exceeds the limits, the message bits QH_LMALM, QH_LMWRN, QL_LMWRN, and QL_LMALM are set. In order to avoid rapid activating and deactivating of the message bits, the input value must also violate a hysteresis HYS before the outputs are reset.

The figure below shows how the LIMALARM instruction functions:

![Operating principle](images/18026823691_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| QH_LMALM = TRUE | If | INV rises | and | INV >= H_LM_ALM |
| or | INV falls | and | INV >= H_LM_ALM - HYS |  |
| QH_LMWRN = TRUE | If | INV rises | and | INV >= H_LM_WRN |
| or | INV falls | and | INV >= H_LM_WRN - HYS |  |
| QL_LMWRN = TRUE | If | INV falls | and | INV <= L_LM_WRN |
| or | INV rises | and | INV <= L_LM_WRN + HYS |  |
| QL_LMALM = TRUE | If | INV falls | and | INV <= L_LM_ALM |
| or | INV rises | and | INV <= L_LM_ALM + HYS |  |

In order for the instruction to function in a useful way, the following must apply:

L_LM_ALM < L_LM_WRN < H_LM_WRN < H_LM_ALM

#### Complete restart

During a complete restart, all the signal outputs are set to FALSE.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)

### Input parameters LIMALARM (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| H_LM_ALM | 0.0 | REAL | 100.0 | High limit alarm  Engineering value range  > H_LM_WRN |
| H_LM_WRN | 4.0 | REAL | 90.0 | High limit warning  Engineering value range  > L_LM_WRN |
| L_LM_WRN | 8.0 | REAL | 10.0 | Low limit warning  Engineering value range  > L_LM_ALM |
| L_LM_ALM | 12.0 | REAL | 0.0 | Low limit alarm  Engineering value range  < L_LM_WRN |
| INV | 16.0 | REAL | 0.0 | Input variable  Engineering value range |
| HYS | 20.0 | REAL | 1.0 | Hysteresis  Engineering value range |
| COM_RST | 24.0 | BOOL | FALSE | Complete restart |

### Output parameters LIMALARM (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| QH_LMALM | 26.0 | BOOL | FALSE | High limit alarm triggered |
| QH_LMWRN | 26.1 | BOOL | FALSE | High limit warning triggered |
| QL_LMWRN | 26.2 | BOOL | FALSE | Low limit warning triggered |
| QL_LMALM | 26.3 | BOOL | FALSE | Low limit alarm triggered |

## LIMITER (S7-300, S7-400)

This section contains information on the following topics:

- [Description LIMITER (S7-300, S7-400)](#description-limiter-s7-300-s7-400)
- [Input parameters LIMITER (S7-300, S7-400)](#input-parameters-limiter-s7-300-s7-400)
- [Output parameters LIMITER (S7-300, S7-400)](#output-parameters-limiter-s7-300-s7-400)

### Description LIMITER (S7-300, S7-400)

If parameters are defined dynamically (for example calculation of setpoints from process variables), these can assume values that are invalid for the process. The LIMITER instruction can be used to keep parameters within a valid range.

#### Operating principle

The instruction limits output variable OUTV to a definable high and low limit H_LM and L_LM when input variable INV lies outside these limits. Limiting of OUTV is signaled by outputs QH_LM and QL_LM.

The figure below shows how the LIMITER instruction functions:

![Operating principle](images/18026851083_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |  |
| --- | --- | --- | --- |
| **INV** | **OUTV** | **QH_LM** | **QL_LM** |
| ≥ H_LM | H_LM, | TRUE | FALSE |
| ≤ L_LM | L_LM, | FALSE | TRUE |
| ≤ L_LM   and   ≤H_LM | INV | FALSE | FALSE |

In order for the instruction to function in a useful way, the following must apply:

L_LM < H_LM

#### Complete restart

During a complete restart, all signal outputs are set to FALSE; 0.0 is output at output OUTV.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)
  
[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)

### Input parameters LIMITER (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| H_LM | 4.0 | REAL | 100.0 | High limit  Engineering value range  > L_LM |
| L_LM | 8.0 | REAL | 0.0 | Low limit  Engineering value range  < H_LM |
| COM_RST | 12.0 | BOOL | FALSE | Complete restart |

### Output parameters LIMITER (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 14.0 | REAL | 0.0 | Output variable |
| QH_LM | 18.0 | BOOL | FALSE | High limit triggered |
| QL_LM | 18.1 | BOOL | FALSE | Low limit triggered |

## LMNGEN_C (S7-300, S7-400)

This section contains information on the following topics:

- [Description LMNGEN_C (S7-300, S7-400)](#description-lmngen_c-s7-300-s7-400)
- [Operating principle LMNGEN_C (S7-300, S7-400)](#operating-principle-lmngen_c-s7-300-s7-400)
- [Input parameters LMNGEN_C (S7-300, S7-400)](#input-parameters-lmngen_c-s7-300-s7-400)
- [Output parameters LMNGEN_C (S7-300, S7-400)](#output-parameters-lmngen_c-s7-300-s7-400)
- [In/out parameters LMNGEN_C (S7-300, S7-400)](#inout-parameters-lmngen_c-s7-300-s7-400)
- [LMNGEN_C static variables (S7-300, S7-400)](#lmngen_c-static-variables-s7-300-s7-400)

### Description LMNGEN_C (S7-300, S7-400)

This instruction is used to set up a continuous PID controller and determines the manipulated variable or the controller. The manipulated variable can be determined in automatic mode or specified in manual mode. The manual value can be assigned as an absolute value or increased/decreased via a switch. The manipulated variable and the increase in the manipulated variable can be limited to definable values.

#### Restart

During a complete restart the default value DF_OUTV is switched through to the output LMN irrespective of the default bit DFOUT_ON. Limiting of the output and its display also remains effective during a complete restart. On transition to normal operation, the instruction continues to operate from DF_OUTV.

The output parameters QLMN_HLM and QLMN_LLM are set to FALSE.

#### Call

While the PID instruction is called in a cyclic interrupt level whose cycle time is adapted to the dominating system time constant, the LMNGEN_C instruction for manual interventions can be called in a faster cyclic interrupt level. Interconnection is carried out with the structured input-output parameters PID_LMNG and LMNG_PID.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

#### Operating principle

The LMNGEN_C instruction is always used in conjunction with the PID instruction.

The following figure shows the interconnection of the continuous PID controller.

![Operating principle](images/18026878475_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Creating a continual controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-continual-controller-s7-300-s7-400)
  
[Creating a pulse controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-pulse-controller-s7-300-s7-400)

### Operating principle LMNGEN_C (S7-300, S7-400)

#### Limiting the manipulated variable

The manipulated variable is limited in all operating modes. You enter the high limit of the manipulated variable at input LMN_HLM and the low limit at input LMN_LLM. If the calculated manipulated variable exceeds or falls below these values, the high limit or low limit, respectively, is output at LMN. The limiting of the manipulated variable to the high limit is indicated at output QLMN_HLM, and the limiting to the limit limit at output QLMN_LLM.

#### Manipulated variable ramp

You use the manipulated variable ramp to limit the rate of change of the manipulated variable. You activate the manipulated variable with LMNRC_ON=TRUE. At input parameter LMN_URLM, you specify the maximum rate of change for the rising slope of the manipulated variable, and at input parameter LMN_DRLM the maximum rate of change for the falling slope of the manipulated variable.

#### Operating modes

The operating modes are activated and deactivated using the DFOUT_ON, MAN_ON, and MANGN_ON parameters.

| Operating modes | DFOUT_ON | MAN_ON | MANGN_ON |
| --- | --- | --- | --- |
| Automatic mode | FALSE | FALSE | FALSE |
| Manual mode | FALSE | TRUE | FALSE |
| Manual value generator | FALSE | TRUE | TRUE |
| Preassign manipulated variable | TRUE | Not relevant | Not relevant |

![Operating modes](images/18026894475_DV_resource.Stream@PNG-de-DE.png)

- **Automatic mode**

  The value determined by the PID algorithm is used to determine manipulated variable LMN. The changeover to automatic mode is bumpless if the manipulated variable ramp (LMNRC_ON = TRUE) is activated.
- **Manual mode**

  With MAN_ON = TRUE, you switch to manual mode and thus interrupt the control loop. Manual value MAN is output directly as manipulated variable LMN. MAN must lie within the limits LMN_HLM and LMN_LLM.
- **Manual value generator**

  If MANGN_ON = TRUE as well, the manipulated variable can be increased and decreased using the MANUP and MANDN switches, respectively. The rate of change of the manipulated variable depends on the limits as follows:

  - During the first 3 s after setting of MANUP or MANDN

    dLMN/dt = (LMN_HLM - LMN_LLM) / 100 s
  - Afterwards:

    dLMN/dt = (LMN_HLM - LMN_LLM) / 10 s
- **Preassign manipulated variable**

  When DFOUT_ON = TRUE, the preassigned value DF_OUTV is applied at output LMN. The changeover from or to "Preassign manipulated variable" is only bumpless if the manipulated variable ramp is activated. (LMNRC_ON= TRUE).

#### Operator control via HMI

You can use static variables to influence the manipulated variable via the HMI (see figure below). The static variables LMN_OP, LMNOP_ON, and MP1 may be operated and monitored via an HMI, for example.

![Operator control via HMI](images/18026913547_DV_resource.Stream@PNG-de-DE.png)

If LMNOP_ON is set to TRUE, LMN_OP is switched through to manipulated variable LMN. MP1 contains the manipulated variable that is being processed by the LMNGEN_C instruction.

If the manipulated variable ramp is activated, bumpless changeover between the values MP1 and LMN_OP is possible. LMN is fed back to the value MP1 in conformance with the specified ramp.

When a static variable is changed, the change takes effect in the process only after the variable has been transferred to the CPU.

### Input parameters LMNGEN_C (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMN_HLM | 0.0 | REAL | 100.0 | High limit of manipulated variable  Engineering value range  > LMN_LLM |
| LMN_LLM | 4.0 | REAL | 0.0 | Low limit of manipulated variable  Engineering value range  < LMN_HLM |
| LMN_URLM | 8.0 | REAL | 10.0 | Manipulated variable up rate limit [1/s]  > 0.0 |
| LMN_DRLM | 12.0 | REAL | 10.0 | Manipulated variable down rate limit [1/s]  > 0.0 |
| DF_OUTV | 16.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| MAN_ON | 20.0 | BOOL | TRUE | Manual mode ON |
| MANGN_ON | 20.1 | BOOL | FALSE | Activate manual value operation |
| MANUP | 20.2 | BOOL | FALSE | Manual value up |
| MANDN | 20.3 | BOOL | FALSE | Manual value down |
| LMNRC_ON | 20.4 | BOOL | FALSE | Manipulated variable rate of change on |
| DFOUT_ON | 20.5 | BOOL | FALSE | Default setting of output variable On |
| COM_RST | 20.6 | BOOL | FALSE | Complete restart |
| CYCLE | 22.0 | TIME | T#1s | Sampling time  ≥ 1ms |
| PID_LMNG | 26.0 | STRUC |  | PID-LMNGEN interface |

### Output parameters LMNGEN_C (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMN | 44.0 | REAL | 0.0 | Manipulated variable |
| QLMN_HLM | 48.0 | BOOL | FALSE | High limit of manipulated variable triggered |
| QLMN_LLM | 48.1 | BOOL | FALSE | Low limit of manipulated variable triggered |
| LMNG_PID | 50.0 | STRUC |  | PID-LMNGEN interface |

### In/out parameters LMNGEN_C (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| MAN | 68.0 | REAL | 0.0 | Manual value  Engineering value range |

### LMNGEN_C static variables (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| MP1 | 72.0 | REAL | 0.0 | Manipulated variable processed by LMNGEN_C. |
| LMM_OP | 76.0 | REAL | 0.0 | Operator control via HMI   Manual value |
| LMNOP_ON | 80.0 | BOOL | FALSE | Operator control via HMI   Manual mode ON |

## LMNGEN_S (S7-300, S7-400)

This section contains information on the following topics:

- [Description LMNGEN_S (S7-300, S7-400)](#description-lmngen_s-s7-300-s7-400)
- [Operating principle LMNGEN_S (S7-300, S7-400)](#operating-principle-lmngen_s-s7-300-s7-400)
- [Input parameters LMNGEN_S (S7-300, S7-400)](#input-parameters-lmngen_s-s7-300-s7-400)
- [Output parameters LMNGEN_S (S7-300, S7-400)](#output-parameters-lmngen_s-s7-300-s7-400)
- [In/out parameters LMNGEN_S (S7-300, S7-400)](#inout-parameters-lmngen_s-s7-300-s7-400)
- [LMNGEN_S static variables (S7-300, S7-400)](#lmngen_s-static-variables-s7-300-s7-400)

### Description LMNGEN_S (S7-300, S7-400)

This instruction is used to set up a PID step controller for actuators with integral-action response (e.g., motor-driven valves) and determines the manipulated variable of the controller. The manipulated variable can be determined in automatic mode or specified in manual mode. The manual value can be assigned as an absolute value or increased/decreased via a switch. The manipulated variable can be limited to assignable values. The step controller can operate with or without position feedback.

#### Complete restart

During a complete restart, all the signal outputs are set to 0.

#### Call

While the PID instruction is called in a cyclic interrupt level whose cycle time is adapted to the dominating system time constant, the LMNGEN_S instruction for manual interventions can be called in a faster cyclic interrupt level. Interconnection is carried out with the structured input-output parameters PID_LMNG and LMNG_PID.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

#### Operating principle

The LMNGEN_S instruction is always used in conjunction with the PID instruction.

The following figure shows the interconnection of a step controller.

![Operating principle](images/18026945547_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Creating a step controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-step-controller-s7-300-s7-400)

### Operating principle LMNGEN_S (S7-300, S7-400)

#### Limiting the manipulated variable

The manipulated variable is limited in all operating modes. You enter the high limit of the manipulated variable at input LMN_HLM and the low limit at input LMN_LLM. If the calculated manipulated variable exceeds or falls below these values, the high limit or low limit, respectively, is output at LMN. The limiting of the manipulated variable to the high limit is indicated at output QLMN_HLM, and the limiting to the limit limit at output QLMN_LLM.

#### Limit signals

You interconnect the signals for the upper and lower actuator stop with input parameters LMNR_HS and LMNR_LS. If LMNR_HS= TRUE, the actuator will not open further. If LMNR_LS= TRUE, the actuator will not close further. Output signals QLMNUP and QLMNDN are blocked. The end stops are taken into consideration in all operating modes.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If limit signals are not available, the controller cannot recognize a valve stop, and the possibility exists, for example, that the controller will output signals to open the valve even though the valve is at its upper stop. If limit signals are not available, inputs LMNR_HS and LMNR_LS must be assigned the value FALSE. |  |

#### Step controller with position feedback

If position feedback is available, the instruction uses a three-step element and pulse generator to generate the pulses for controlling the control valve based on the difference between the manipulated variable and the position feedback. You can adapt the response threshold of the three-step element to reduce the switching frequency of the controller.

You activate the position feedback with LMNR_ON = TRUE.

![Step controller with position feedback](images/18026956939_DV_resource.Stream@PNG-de-DE.png)

#### Step controller without position feedback

If position feedback is not available, the instruction adds up the difference between the integral component of the PID algorithm and a simulated position feedback in an integrator and then compares this, as a feedback value, with the remaining proportional-derivative component. The difference is applied in turn to the three-step element and the pulse generator that generates the pulses for the control valve. You can adapt the response threshold of the three-step element to reduce the switching frequency of the controller.

You deactivate the position feedback with LMNR_ON = FALSE.

![Step controller without position feedback](images/18026976011_DV_resource.Stream@PNG-de-DE.png)

#### Operating modes

The operating modes are activated and deactivated using the LMN_ON, MAN_ON, and MANGN_ON parameters.

| Operating modes | LMN_ON | MAN_ON | MANGN_ON |
| --- | --- | --- | --- |
| Automatic mode | FALSE | FALSE | FALSE |
| Specify manual value | FALSE | TRUE | FALSE |
| Manual value generator | FALSE | TRUE | TRUE |
| Manual mode of the manipulated variable output signals | TRUE | Not relevant | Not relevant |

The Specify manual value and Manual value generator modes are only possible for step controllers with position feedback. Because information on the valve position is not available in a step controller without position feedback, the actuator cannot be moved to a fixed manual value.

- **Specify manual value**

  With MAN_ON = TRUE, you switch to manual mode and thus interrupt the conrol loop. Manual value MAN is switched through directly as the manipulated variable. MAN must lie within the limits LMN_HLM and LMN_LLM.
- **Manual value generator**

  If MANGN_ON = TRUE as well, the manipulated variable can be increased and decreased using the MANUP and MANDN switches, respectively. The rate of change of the manipulated variable depends on the limits as follows:

  - During the first 3 s after setting of MANUP or MANDN

    dLMN/dt = (LMN_HLM - LMN_LLM) / 100 s
  - Afterwards:

    dLMN/dt = (LMN_HLM - LMN_LLM) / 10 s
- **Manual mode of the manipulated variable output signals**

  If LMNS_ON = TRUE, the binary output signals can be influenced directly. The actuating signal outputs QLMNUP and QLMNDN are set by switches LMNUP and LMNDN. The minimum pulse time PULSE_TM and minimum break time BREAK_TM are also taken into consideration.
- **Automatic operation with position feedback**

  The value PID_LMNG.PID_OUTV sent by the PID algorithm is limited to assignable values LMN_HLM and LMN_LLM. The difference between the manipulated variable and the position feedback is switched to a three-step element with hysteresis. The trip threshold is calculated from the motor actuating time. In order to reduce the switching frequency, the response threshold is adapted. The pulse generator PULSEOUT ensures that the minimum pulse time and minimum break time are observed.
- **Automatic mode without position feedback**

  The difference between the integral component of the PID algorithm and a simulated position feedback is summed in integrator INT. The input of the integrator is the difference of 100.0/0.0/-100.0 (depending on the state of output signals QLMNUP and QLMNDN), referenced to motor actuating time MTR_TM, and the control deviation multiplied times the controller gain, referenced to integral-action time TI of the PID algorithm (PID_LMNG.PID_SCTR). The output of the integrator forms the feedback value that is compared with the remaining proportional-derivative component of the PID algorithm (PID_LMNG.PID_OUTV). The difference is switched to a three-step element with hysteresis. The trip threshold is calculated from the motor actuating time.

  In order to reduce the switching frequency, the response threshold is adapted. The pulse generator PULSEOUT ensures that the minimum pulse time and minimum break time are observed.

#### Simulation of the position feedback

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The position feedback is only simulated. It does not have to agree with the real position feedback of the control valve.  If a real position feedback exists, it should also be used. |  |

The simulation of the position feedback is carried out by an integrator with motor actuating time MTR_TM as the integral-action time constant. A rising edge at LMNRS_ON starts the simulation with start value LMNRSVAL. If the value of LMNRS_ON is FALSE, the start value LMNRSVAL is output in parameter LMNR_SIM.

The limit signals LMNR_HS = TRUE and LMNR_LS = TRUE block the integration at high and low limits.

#### Operator input via HMI

You can use an HMI and static variables to interrupt the manipulated variable branch and specify your own manipulated variables (see figure below).

![Operator input via HMI](images/18026995083_DV_resource.Stream@PNG-de-DE.png)

If LMNOP_ON is set to TRUE, LMN_OP is switched through to manipulated variable LMN. MP1 contains the manipulated variable that is being processed by the LMNGEN_S instruction.

If the manipulated variable ramp is activated, bumpless changeover between the values MP1 and LMN_OP is possible. LMN is fed back to the value MP1 in conformance with the specified ramp.

If LMNSOPON is set to TRUE, you can increase the manipulated variable with LMNUP_OP or decrease it with LMNDN_OP. This applies to step controllers with and without position feedback.

The static variables LMNOP_ON, LMN_OP, MP1, LMNSOPON, LMNUP_OP, and LMNDN_OP must not be interconnected and are only manipulated and monitored via an HMI.

When a static variable is changed, the change takes effect in the process only after the variable has been transferred to the CPU.

### Input parameters LMNGEN_S (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMN_HLM | 0.0 | REAL | 100.0 | High limit of manipulated variable  Engineering value range  > LMN_LLM |
| LMN_LLM | 4.0 | REAL | 0.0 | Low limit of manipulated variable  Engineering value range  < LMN_HLM |
| LMNR_IN | 8.0 | REAL | 0.0 | Position feedback  Engineering value range |
| MTR_TM | 12.0 | TIME | T#30s | Motor actuating time  ≥ CYCLE |
| PULSE_TM | 16.0 | TIME | T#3s | Minimum pulse time  ≥ CYCLE |
| BREAK_TM | 20.0 | TIME | T#3s | Minimum break time  ≥ CYCLE |
| MAN_ON | 24.0 | BOOL | TRUE | Manual mode ON |
| MANGN_ON | 24.1 | BOOL | FALSE | Activate manual value operation |
| MANUP | 24.2 | BOOL | FALSE | Manual value up |
| MANDN | 24.3 | BOOL | FALSE | Manual value down |
| LMNR_ON | 24.4 | BOOL | FALSE | Position feedback on |
| LMNR_HS | 24.5 | BOOL | FALSE | High limit signal of position feedback |
| LMNR_LS | 24.6 | BOOL | FALSE | Low limit signal of position feedback |
| LMNS_ON | 24.7 | BOOL | FALSE | Activate manual mode for manipulated variable signals |
| LMNUP | 25.0 | BOOL | FALSE | Manipulated variable signal UP |
| LMNDN | 25.1 | BOOL | FALSE | Manipulated variable signal DOWN |
| COM_RST | 25.2 | BOOL | FALSE | Complete restart |
| CYCLE | 26.0 | TIME | T#1s | Sampling time  ≥ 1ms |
| PID_LMNG | 30.0 | STRUC |  | PID-LMNGEN interface |

### Output parameters LMNGEN_S (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMN | 48.0 | REAL | 0.0 | Manipulated variable |
| QLMNUP | 52.0 | BOOL | FALSE | Manipulated value signal up |
| QLMNDN | 52.1 | BOOL | FALSE | Manipulated variable signal DOWN |
| QLMN_HLM | 52.2 | BOOL | FALSE | High limit of manipulated variable triggered |
| QLMN_LLM | 52.3 | BOOL | FALSE | Low limit of manipulated variable triggered |
| LMNG_PID | 54.0 | STRUC |  | PID-LMNGEN interface |

### In/out parameters LMNGEN_S (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| MAN | 72.0 | REAL | 0.0 | Manual value  Engineering value range |

### LMNGEN_S static variables (S7-300, S7-400)

You must not modify variables that are not listed. These are used for internal purposes only.

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMNSOPON | 76.0 | BOOL | FALSE | Operator control via HMI   Manual mode of the manipulated variable output signals ON |
| LMNUP_OP | 76.1 | BOOL | FALSE | Operator control via HMI   Manipulated variable UP |
| LMNDN_OP | 76.2 | BOOL | FALSE | Operator control via HMI   Manipulated variable DOWN |
| LMNOP_ON | 76.3 | BOOL | FALSE | Operator control via HMI   Manual mode ON |
| LMNRS_ON | 76.4 | BOOL | FALSE | Simulated position feedback ON |
| MP1 | 78.0 | REAL | 0.0 | Operator control via HMI   Manipulated variable processed by LMNGEN_C. |
| LMM_OP | 82.0 | REAL | 0.0 | Operator control via HMI   Manual value |
| LMNRSVAL | 86.0 | REAL | 0.0 | Initial value for simulate position feedback |
| LMNR_SIM | 9.0 | REAL | 0.0 | Simulated position feedback |

## NONLIN (S7-300, S7-400)

This section contains information on the following topics:

- [Description NONLIN (S7-300, S7-400)](#description-nonlin-s7-300-s7-400)
- [Input parameters NONLIN (S7-300, S7-400)](#input-parameters-nonlin-s7-300-s7-400)
- [Output parameters NONLIN (S7-300, S7-400)](#output-parameters-nonlin-s7-300-s7-400)
- [Global data block DB_NONLIN (S7-300, S7-400)](#global-data-block-db_nonlin-s7-300-s7-400)

### Description NONLIN (S7-300, S7-400)

The NONLIN instruction can be used to adapt an input value, such as a measured value of a thermocouple, as a function of a definable characteristic (polyline).

#### Operating principle

NONLIN interpolates the corresponding output variable OUTV for the current input variable INV using time slices on a polyline. The time slices of the polyline are stored in a global data block.

[Global data block DB_NONLIN](#global-data-block-db_nonlin-s7-300-s7-400) is not included in the library. You must create this global data block yourself.

> **Note**
>
> The instruction does not check whether a global DB with the number DB_NBR actually exists or whether the DB_NBR. NBR_PTS parameter (number of time slices) is suited to the length of the data block. If the parameter assignment is incorrect, the CPU changes to the STOP operating mode with the message "Internal system error".

NONLIN has the following functions:

| Functions | DFOUT_ON | TRACK | OUTV |
| --- | --- | --- | --- |
| Interpolation | FALSE | FALSE | OUTV = f(INV) |
| Preassign output | TRUE | Any | DF_OUTV |
| Tracking | FALSE | TRUE | OUTV = INV |

- **Interpolation**

  The following figure shows how output variable OUTV is determined from input variable INV.

  OUTV = f(INV)

  ![Operating principle](images/18027086475_DV_resource.Stream@PNG-de-DE.png)

  If the input value lies below time slice 0, extrapolation is carried out with the rise of the time slice pair 0/1. It it lies above the last time slice, extrapolation is carried out with the rise of the last time slice pair. In order for the instruction to produce a useful result, the values of the time slices must exhibit a monotonic rise in ascending order.
- **Preassign output**

  If DFOUT_ON = TRUE is set, DF_OUTV is output at the output; the change of OUTV is a step change. On changeover to DFOUT_ON = FALSE the change of OUTV is also a step change.
- **Tracking**

  When TRACK=TRUE, the input value is output directly (OUTV=INV). The change is a step change, as in the case of DFOUT_ON. TRACK has lower priority than DFOUT_ON.

#### Restart

On a complete restart, OUTV = 0.0 is output. If DFOUT_ON=TRUE, DF_OUTV is output.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)
  
[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#applying-the-disturbance-variable-s7-300-s7-400)
  
[Processing position feedback (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-position-feedback-s7-300-s7-400)

### Input parameters NONLIN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| DF_OUTV | 4.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| DB_NBR | 8.0 | BLOCK_DB | DB 1 | Data block number |
| DFOUT_ON | 10.0 | BOOL | FALSE | Default setting of output variable On |
| TRACK | 10.1 | BOOL | FALSE | Tracking OUTV=INV |
| COM_RST | 10.2 | BOOL | FALSE | Complete restart |

### Output parameters NONLIN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 12.0 | REAL | 0.0 | Output variable |

### Global data block DB_NONLIN (S7-300, S7-400)

The time slices of the polyline for the instruction NONLIN are stored in a global data block. This global data block is not included in the library. You must create the global data block yourself according to the following schema and adapt it to your application.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| DB_NBR.NBR_PTS | INT | 4 | Highest time slice number  Range of values 1 - 255 |
| DB_NBR.PI[0].OUTV | REAL | 0.0 | Output variable [0] Starting point 0  Engineering value range |
| DB_NBR.PI[0].INV | REAL | 0.0 | Input variable [0] Starting point 0   Engineering value range |
| DB_NBR.PI[1].OUTV | REAL | 0.0 | Output variable [1] Time slice 1   Engineering value range |
| DB_NBR.PI[1].INV | REAL | 0.0 | Input variable [1] Time slice 1   Engineering value range |
| DB_NBR.PI[2].OUTV | REAL | 0.0 | Output variable [2] Time slice 2   Engineering value range |
| DB_NBR.PI[2].INV | REAL | 0.0 | Input variable [2] Time slice 2   Engineering value range |
| DB_NBR.PI[3].OUTV | REAL | 0.0 | Output variable [3] Time slice 3   Engineering value range |
| DB_NBR.PI[3].INV | REAL | 0.0 | Input variable [3] Time slice 3   Engineering value range |
| DB_NBR.PI[4].OUTV | REAL | 0.0 | Output variable [4] Time slice 4   Engineering value range |
| DB_NBR.PI[4].INV | REAL | 0.0 | Input variable [4] Time slice 4   Engineering value range |

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
| DATA_BLOCK "DB_NONLIN" |  |  |  |  |
| TITLE = data block nonlinear static function |  |  |  |  |
| { S7_Optimized_Access := 'FALSE' } |  |  |  |  |
| NAME : DB_NONLI |  |  |  |  |
|  | STRUCT |  |  |  |
|  |  | NBR_PTS : Int; |  | // number of points (excluding starting point) |
|  |  | PI : Array[0..4] of Struct |  |  |
|  |  |  | OUTV : Real; | // output variable |
|  |  |  | INV : Real; | // input variable |
|  |  | END_STRUCT; |  |  |
|  | END_STRUCT; |  |  |  |

| Symbol | Meaning |
| --- | --- |
| BEGIN |  |
|  | NBR_PTS := 4; |
|  | PI[0].OUTV := 1.0; |
|  | PI[0].INV := 2.0; |
|  | PI[1].OUTV := 2.0; |
|  | PI[1].INV := 3.0; |
|  | PI[2].OUTV := 4.0; |
|  | PI[2].INV := 4.0; |
|  | PI[3].OUTV := 5.0; |
|  | PI[3].INV := 5.0; |
|  | PI[4].OUTV := 6.0; |
|  | PI[4].INV := 7.0; |
| END_DATA_BLOCK |  |

## NORM (S7-300, S7-400)

This section contains information on the following topics:

- [Description NORM (S7-300, S7-400)](#description-norm-s7-300-s7-400)
- [Input parameters NORM (S7-300, S7-400)](#input-parameters-norm-s7-300-s7-400)
- [Output parameters NORM (S7-300, S7-400)](#output-parameters-norm-s7-300-s7-400)

### Description NORM (S7-300, S7-400)

In the case of process values the value supplied by the encoder often lies in a range that is unfavorable for the user (for example 0 to 10 V correspond to 0 to 1200 ºC or 0 to 10 V correspond to 0 to 3000 rpm). By scaling the setpoint or the process value, both process variables lie in the same range of values.

#### Operating principle

The instruction scales the input variable into an output variable with a different range of values. Input variable INV is transformed to output variable OUTV based on the scaling line. The scaling line is defined by the two value pairs IN_LVAL, OUT_LVAL and IN_HVAL, OUT_HVAL.

![Operating principle](images/18027113867_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)
  
[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#applying-the-disturbance-variable-s7-300-s7-400)

### Input parameters NORM (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| IN_HVAL | 4.0 | REAL | 100.0 | Physical input value below   Engineering value range  > IN_LVAL |
| OUT_HVAL | 8.0 | REAL | 100.0 | Physical output value below  Engineering value range  > OUT_LVAL |
| IN_LVAL | 12.0 | REAL | 0.0 | Physical input value above   Engineering value range  < IN_HVAL |
| OUT_LVAL | 16.0 | REAL | 0.0 | Physical output value above  Engineering value range  < OUT_HVAL |

### Output parameters NORM (S7-300, S7-400)

| Parameter | Offset | Data type | Description |
| --- | --- | --- | --- |
| OUTV | 20.0 | REAL | Output variable |

## OVERRIDE (S7-300, S7-400)

This section contains information on the following topics:

- [Description OVERRIDE (S7-300, S7-400)](#description-override-s7-300-s7-400)
- [Input parameters OVERRIDE (S7-300, S7-400)](#input-parameters-override-s7-300-s7-400)
- [Output parameters OVERRIDE (S7-300, S7-400)](#output-parameters-override-s7-300-s7-400)

### Description OVERRIDE (S7-300, S7-400)

This instruction is required to implement an override control.

#### Operating principle

Two PID controllers are connected to one actuator. For this purpose, two PID instructions are interconnected by means of instruction OVERRIDE with instruction LMNGEN_C or LMNGEN_S. If you use LMNGEN_S, position feedback must be activated (LMNR_ON=TRUE).

![Operating principle](images/18027141259_DV_resource.Stream@PNG-de-DE.png)

The instruction compares the values PID1_OVR and PID2_OVR and connects either the larger or the smaller value.

The instruction transfers the value in PID1_OVR or in PID2_OVR to LMN_GEN_C or LMN_GEN_S.

If the PID1_ON and PID2_ON switches are unequal, the one value is always transferred. If the PID1_ON and PID2_ON switches are equal, the larger (OVR_MODE=FALSE) or smaller (OVR_MODE=TRUE) of the two values is transferred.

| PID1_ON | PID2_ON | OVR_MOD | Function |
| --- | --- | --- | --- |
| TRUE | FALSE | Not relevant | PID1_OVR is transferred. |
| FALSE | TRUE | PID2_OVR is transferred. |  |
| FALSE | FALSE | FALSE | The larger value of PID1_OVR and PID2_OVR is transferred. |
| TRUE | TRUE | FALSE |  |
| FALSE | FALSE | TRUE | The smaller value of PID1_OVR and PID2_OVR is transferred. |
| TRUE | TRUE | TRUE |  |

If PID1_OVR is transferred, QPID1=TRUE; if PID2_OVR is transferred, QPID2=TRUE.

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters OVERRIDE (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| PID1_ON | 0.0 | BOOL | FALSE | PID controller 1 on |
| PID2_ON | 0.1 | BOOL | FALSE | PID controller 2 on |
| OVR_MODE | 0.2 | BOOL | FALSE | Override mode FALSE=maximum, TRUE=minimum |
| PID1_OVR | 2.0 | STRUC |  | PID-LMNGEN interface |
| PID2_OVR | 20.0 | STRUC |  | PID-LMNGEN interface |

### Output parameters OVERRIDE (S7-300, S7-400)

| Parameter | Offset | Data type | Description |
| --- | --- | --- | --- |
| QPID1 | 38.0 | BOOL | PID controller 1 active |
| QPID2 | 38.1 | BOOL | PID controller 2 active |
| OVR_LMNG | 40.0 | STRUC | PID-LMNGEN interface |

## PARA_CTL (S7-300, S7-400)

This section contains information on the following topics:

- [Description PARA_CTL (S7-300, S7-400)](#description-para_ctl-s7-300-s7-400)
- [Input parameters PARA_CTL (S7-300, S7-400)](#input-parameters-para_ctl-s7-300-s7-400)
- [Output parameters PARA_CTL (S7-300, S7-400)](#output-parameters-para_ctl-s7-300-s7-400)

### Description PARA_CTL (S7-300, S7-400)

The instruction is used in controller structures with parameter changeovers if optimum controller parameters are required for different operating ranges.

#### Operating principle

Several controller parameter sets (GAIN, TI, TD, and TM_LAG) can be transferred to a PID controller.

The PSET1_ON...PSET4_ON switches can be used to switch through one of the 4 parameter sets to outputs GAIN, TI, TD, and TM_LAG.

| Symbol | Meaning |
| --- | --- |
| If... | Then... |
| PSET1_ON = TRUE | GAIN = PARASET1.GAIN |
| TI = PARASET1.TR |  |
| TD = PARASET1.TD |  |
| TM_LAG = PARASET1.TM_LAG |  |
| PSET2_ON = TRUE | GAIN = PARASET2.GAIN |
| TI = PARASET2.TR |  |
| TD = PARASET2.TD |  |
| TM_LAG = PARASET2.TM_LAG |  |
| PSET3_ON = TRUE | GAIN = PARASET3.GAIN |
| TI = PARASET3.TR |  |
| TD = PARASET3.TD |  |
| TM_LAG = PARASET3.TM_LAG |  |
| PSET4_ON = TRUE | GAIN = PARASET4.GAIN |
| TI = PARASET4.TR |  |
| TD = PARASET4.TD |  |
| TM_LAG = PARASET4.TM_LAG |  |

If 2 or more switches are set to TRUE, the switch with the lowest number always has the highest priority. If no switch is set to TRUE, the first parameter set is transferred.

In order to achieve a bumpless changeover between the parameter sets, a rate of change limiter (ROC_LIM) must be connected between the PID and PARA_CTL instructions for the GAIN parameter.

![Operating principle](images/18027173259_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters PARA_CTL (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| PSET1_ON | 0.0 | BOOL | FALSE | Transfer Parameter set number 1 |
| PSET2_ON | 0.1 | BOOL | FALSE | Transfer Parameter set number 2 |
| PSET3_ON | 0.2 | BOOL | FALSE | Transfer Parameter set number 3 |
| PSET4_ON | 0.3 | BOOL | FALSE | Transfer Parameter set number 4 |
| PARASET1.GAIN | 2.0 | REAL |  | Proportional gain 1 |
| PARASET1.TI | 6.0 | TIME | 5 s | Integral-action time 1 |
| PARASET1.TD | 10.0 | TIME | 10 s | Derivative-action time 1 |
| PARASET1.TM_LAG | 14.0 | TIME | 2 s | Time delay 1 |
| PARASET2.GAIN | 18.0 | REAL |  | Proportional gain 2 |
| PARASET2.TI | 22.0 | TIME | 5 s | Integral-action time 2 |
| PARASET2.TD | 26.0 | TIME | 10 s | Derivative-action time 2 |
| PARASET2.TM_LAG | 30.0 | TIME | 2 s | Time delay 2 |
| PARASET3.GAIN | 34.0 | REAL |  | Proportional gain 3 |
| PARASET3.TI | 38.0 | TIME | 5 s | Integral-action time 3 |
| PARASET3.TD | 42.0 | TIME | 10 s | Derivative-action time 3 |
| PARASET3.TM_LAG | 46.0 | TIME | 2 s | Time delay 3 |
| PARASET4.GAIN | 500 | REAL |  | Proportional gain 4 |
| PARASET4.TI | 54.0 | TIME | 5 s | Integral-action time 4 |
| PARASET4.TD | 58.0 | TIME | 10 s | Derivative-action time 4 |
| PARASET4.TM_LAG | 62.0 | TIME | 2 s | Time delay 4 |

### Output parameters PARA_CTL (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| GAIN | 66.0 | REAL | 1.0 | Proportional gain |
| TI | 70.0 | TIME | 10s | Integral action time |
| TD | 74.0 | TIME | 5s | Derivative-action time |
| TM_LAG | 78.0 | TIME | 2s | Time delay |

## PID (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID (S7-300, S7-400)](#description-pid-s7-300-s7-400)
- [Operating principle PID (S7-300, S7-400)](#operating-principle-pid-s7-300-s7-400)
- [Input parameters PID (S7-300, S7-400)](#input-parameters-pid-s7-300-s7-400)
- [Output parameters PID (S7-300, S7-400)](#output-parameters-pid-s7-300-s7-400)

### Description PID (S7-300, S7-400)

This instruction contains the PID algorithm for setting up the following controller types:

| Symbol | Meaning |
| --- | --- |
| Continuous PID controller: | PID + LMNGEN_C |
| PID step controller for proportional actuators: | PID + LMNGEN_C + PULSEGEN |
| PID step controller for integrating actuators: | PID + LMNGEN_S |

The instruction implements the PID algorithm. It is realized as a pure parallel structure and acts solely as a position algorithm. You can activate and deactivate the proportional, integral and derivative components individually. This allows P, PI, PD, and PID controllers to be configured.

The calculation of the proportional and derivative components can be laid into the feedback. Laying the proportional and derivative components into the feedback loop makes the response to setpoint changes "smooth" while retaining the same speed in settling disturbance variables. It is usually possible to dispense with the common application of a setpoint integrator in order to avoid setpoint steps.

While the PID instruction is placed in a cyclic interrupt level whose cycle time is adapted to the dominating system time constant, the instructions that run the actuators (LMNGEN_C or LMNGEN_S) can be placed in a faster cyclic interrupt level.

#### Complete restart

During a complete restart zero is pre-assigned to all the output and in/out parameters.

#### Block-internal limits

The integral-action time is subject to a limit equal to half the sampling time.

The derivative-action time is subject to a low limit equal to the sampling time.

The time lag is subject to a low limit equal to half the sampling time.

|  |  |  |
| --- | --- | --- |
| TI<sub>intern</sub> = CYCLE/2 | for | TI < CYCLE/2 |
| TD<sub>intern</sub> = CYCLE | for | TD < CYCLE |
| TM_LAG<sub>intern</sub> = CYCLE/2 | for | TM_LAG < CYCLE/2 |

The other values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Creating a continual controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-continual-controller-s7-300-s7-400)
  
[Creating a pulse controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-pulse-controller-s7-300-s7-400)
  
[Creating a step controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-step-controller-s7-300-s7-400)

### Operating principle PID (S7-300, S7-400)

#### Controller structure

The following controller structures are possible with switches P_SEL, I_SEL and D_SEL:

| Controller structure | P_SEL | I_SEL | D_SEL |
| --- | --- | --- | --- |
| P control | TRUE | TRUE bzw. FALSE | FALSE |
| PI control | TRUE | TRUE | FALSE |
| PD control | TRUE | FALSE | TRUE |
| PID control | TRUE | TRUE | TRUE |

#### Block diagram of the PID algorithm

![Block diagram of the PID algorithm](images/52435855243_DV_resource.Stream@PNG-en-US.png)

#### Proportional component

The proportional action can optionally be activated or deactivated using the P_SEL switch. The proportional action is the product of the control deviation ER and the proportional gain GAIN. It can be laid into the feedback path using the PFDB_SEL switch. If the proportional action has been laid into the feedback path, the proportional action is the product of the the process value PV and the proportional gain.

#### Integral action

The integral action can optionally be activated or deactivated with the I_SEL switch. The time response is determined by the integral action time TI. When deactivated, the integral action and the internal memory of the integral action are set to zero. The integral action can be held using INT_HOLD. You can assign the integral action the value at input I_ITLVAL with the I_ITL_ON switch. In the case manipulated variable limiting the Integral action time remains at the old value (anti reset wind-up).

The following applies to a step controller without position feedback: LMN_I = 0.0

#### Derivative component

The derivative action can be activated or deactivated with the D_SEL switch. It can be laid into the feedback path by using the DFDB_SEL switch. The input variable of the derivative action is now the controlled variable PV. The time response is determined by the derivative action time TD.

Oscillation in manipulated variable signals may occur, particularly with rapid processes and an activated derivative action. In this case, the control response can be improved by using the first-order delay integrated in the derivative action. Usually a small TM_LAG time delay is sufficient in order to achieve the desired success.

#### Feedforward control

A disturbance variable DISV can be fed forward additively to the manipulated variable. It can optionally be activated or deactivated by using the DISV_SEL switch.

---

**See also**

[Control Response at Different Feedback Structures](PID%20control.md#control-response-at-different-feedback-structures)
  
[Selection of the controller structure for specified controlled systems](PID%20control.md#selection-of-the-controller-structure-for-specified-controlled-systems)

### Input parameters PID (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| ER | 0.0 | REAL | 0.0 | Control deviation  Engineering value range |
| PV | 4.0 | REAL | 0.0 | Controlled variable (proportional or derivative component in the feedback)  Engineering value range |
| GAIN | 8.0 | REAL | 1.0 | Proportional gain |
| TI | 12.0 | TIME | T#20s | Integral action time |
| I_ITLVAL | 16.0 | REAL | 0.0 | Initialization value for the integral component  Engineering value range |
| TD | 20.0 | TIME | T#10s | Derivative-action time |
| TM_LAG | 24.0 | TIME | T#2s | Time delay of the derivative component |
| DISV | 28.0 | REAL | 0.0 | Disturbance variable  Engineering value range |
| P_SEL | 32.0 | BOOL | TRUE | Activate proportional component |
| PFDB_SEL | 32.1 | BOOL | FALSE | Switch proportional component into feedback |
| DFDB_SEL | 32.2 | BOOL | FALSE | Switch derivative component into feedback |
| I_SEL | 32.3 | BOOL | TRUE | Activate integral component |
| INT_HPOS | 32.4 | BOOL | FALSE | Hold integral component in positive direction |
| INT_HNEG | 32.5 | BOOL | FALSE | Hold integral component in negative direction |
| I_ITL_ON | 32.6 | BOOL | FALSE | Set integral component |
| D_SEL | 32.7 | BOOL | FALSE | Activate derivative component |
| DISV_SEL | 33.0 | BOOL | TRUE | Apply disturbance variable |
| SMOO_CHG | 33.1 | BOOL | TRUE | Smooth changeover from manual mode to automatic mode |
| COM_RST | 33.2 | BOOL | FALSE | Complete restart |
| CYCLE | 34.0 | TIME | T#1s | Sampling time  ≥ 1ms |
| LMNG_PID | 38.0 | STRUC |  | PID-LMNGEN interface |

### Output parameters PID (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| LMN_P | 56.0 | REAL | 0.0 | Proportional component |
| LMN_I | 60.0 | REAL | 0.0 | Integral component |
| LMN_D | 64.0 | REAL | 0.0 | Derivative component |
| PID_LMNG | 68.0 | STRUC |  | PID-LMNGEN interface |

## PULSEGEN_M (S7-300, S7-400)

This section contains information on the following topics:

- [Description PULSEGEN_M (S7-300, S7-400)](#description-pulsegen_m-s7-300-s7-400)
- [Operating principle PULSEGEN_M (S7-300, S7-400)](#operating-principle-pulsegen_m-s7-300-s7-400)
- [PULSEGEN_M modes (S7-300, S7-400)](#pulsegen_m-modes-s7-300-s7-400)
- [PULSEGEN_M three-step control (S7-300, S7-400)](#pulsegen_m-three-step-control-s7-300-s7-400)
- [PULSEGEN_M two-step control (S7-300, S7-400)](#pulsegen_m-two-step-control-s7-300-s7-400)
- [Input parameters PULSEGEN_M (S7-300, S7-400)](#input-parameters-pulsegen_m-s7-300-s7-400)
- [Output parameters PULSEGEN_M (S7-300, S7-400)](#output-parameters-pulsegen_m-s7-300-s7-400)

### Description PULSEGEN_M (S7-300, S7-400)

The instruction PULSEGEN_M is used to set up a PID controller with pulse output for proportional actuators. You can use the PULSEGEN_M instruction to configure two- or three-step PID controllers with pulse width modulation. The instruction is usually used in conjunction with the continuous controller PID + LMNGEN_C.

The diagram below shows how the instructions are connected.

![Figure](images/18027306507_DV_resource.Stream@PNG-de-DE.png)

#### Restart

During a restart, all the signal outputs are set to 0.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Creating a pulse controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-pulse-controller-s7-300-s7-400)

### Operating principle PULSEGEN_M (S7-300, S7-400)

#### Pulse width modulation

PULSEGEN_M transforms the input variable INV (= LMN of the PID controller) by modulating the pulse width into a pulse train with a constant period PER_TM. The period corresponds to the cycle time with which the input variable is updated. The duration of a pulse per period is proportional to the input variable. The cycle assigned via PER_TM is not identical to the processing cycle of the PULSEGEN_M instruction. Rather, a PER_TM cycle is made up of several processing cycles of the PULSEGEN_M instruction, whereby the number of PULSEGEN_M calls per PER_TM cycle measures the accuracy of the pulse width.

![Pulse width modulation](images/18027295115_DV_resource.Stream@PNG-de-DE.png)

An input variable of 30% and 10 PULSEGEN calls per PER_TM mean the following:

- "One" at the QPOS_P output for the first three calls of PULSEGEN_M (30% of 10 calls)
- "Zero" at the QPOS_P output for seven further calls of PULSEGEN_M (70% of 10 calls)

**Minimum pulse time or minimum break time**

A correctly configured minimum pulse time or minimum break time P_B_TM can prevent short on/off times, which reduce the working life of actuators. Small absolute values at the input variable LMN that would otherwise generate a pulse duration shorter than P_B_TM are suppressed. Large input values that would generate a pulse duration longer than PER_TM - P_B_TM are set to 100 % or -100 %.

The following formula applies: P_B_TM ≤ 0.1 × PER_TM

![Pulse width modulation](images/18027336971_DV_resource.Stream@PNG-en-US.png)

Duration of positive or negative pulses is calculated from the input variable (in %) multiplied by the period duration:

Pulse duration = INV / 100 * PER_TM

#### Accuracy of pulse width modulation

While the continual controller PID+LMGEN_C is placed in a slow cyclic interrupt level whose cycle time is adapted to the dominating system time constant, the PULSEGEN_M block must be placed in a faster cyclic interrupt level.

With a "Sampling ratio" of 1:10 (controller calls to PULSEGEN_M calls), the accuracy of the manipulated variable is restricted to 10%, in other words, set input values INV can only be simulated by a pulse duration at the QPOS_P output with an accuracy of 10%.

The accuracy is increased as the number of PULSEGEN_M calls per controller call is increased.

The faster the cyclic interrupt level is, the greater the precision with which the manipulated variable can be output. At a cyclic interrupt level that is 100 times faster, a resolution of 1% of the manipulated variable range is achieved.

#### Automatic synchronization

It is possible to synchronize the pulse output with the controller instruction automatically. This ensures that a modified value of the manipulated variable LMN(t) is output as fast as possible as a proportionally modified pulse duration of the binary signal.

The pulse generator evaluates the input variable INV within the interval of the period PER_TM in each case. Since, however, INV is calculated in a slower cyclic interrupt class, the pulse generator should start the conversion of the discrete value into a pulse signal as soon as possible after the updating of INV. To allow this, the instruction can synchronize the start of the period using the following procedure. If INV changes and if the block call is not in the first or last two call cycles of a period, synchronization is performed. The pulse duration is recalculated and, in the next cycle, is output with a new period.

The period PER_TM must correspond to the sampling time CYCLE of the controller.

![Automatic synchronization](images/18027317899_DV_resource.Stream@PNG-en-US.png)

The automatic synchronization is switched off if SYN_ON = FALSE.

> **Note**
>
> The start of a new period and subsequent synchronization usually leads to a certain imprecision when the old value of INV (i.e. of LMN) is mapped to the pulse signal.

### PULSEGEN_M modes (S7-300, S7-400)

#### Operating modes

Depending on the parameters assigned to the pulse shaper, PID controllers with a three-step output or with a bipolar or unipolar two-step output can be configured. The following table illustrates the setting of the switch combinations for the possible modes.

| Mode | MAN_ON | STEP3_ON | ST2BI_ON |
| --- | --- | --- | --- |
| Three-step control | FALSE | TRUE | Any |
| Two-step control with bi-polar   Manipulating range (-100 % to 100 %) | FALSE | FALSE | TRUE |
| Two-step control with unipolar   Manipulating range (0 % to 100 %) | FALSE | FALSE | FALSE |
| Manual mode | TRUE | Any | Any |

#### Manual mode in two/three-step control

In the manual mode (MAN_ON = TRUE), the binary outputs of the three-step or two-step controller can be set using the signals POS_P_ON and NEG_P_ON regardless of INV.

![Manual mode in two/three-step control](images/34422260875_DV_resource.Stream@PNG-de-DE.png)

| Control | POS_P_ON | NEG_P_ON | QPOS_P | QNEG_P |
| --- | --- | --- | --- | --- |
| Three-step control | FALSE | FALSE | FALSE | FALSE |
| TRUE | FALSE | TRUE | FALSE |  |
| FALSE | TRUE | FALSE | TRUE |  |
| TRUE | TRUE | FALSE | FALSE |  |
| Two-step control | FALSE | Any | FALSE | TRUE |
| TRUE | Any | TRUE | FALSE |  |

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-pulsegen-s7-300-s7-400)
  
[PULSEGEN_M three-step control (S7-300, S7-400)](#pulsegen_m-three-step-control-s7-300-s7-400)
  
[PULSEGEN_M two-step control (S7-300, S7-400)](#pulsegen_m-two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#output-parameter-pulsegen-s7-300-s7-400)

### PULSEGEN_M three-step control (S7-300, S7-400)

#### Three-step control

Three actuating signal states can be generated in "three-step control" mode, e.g. more - off - less, forward - stop - backward, heat - off - cool. The values of the binary output signals QPOS_P and QNEG_P are assigned to the specific states of the actuator. The table shows the example of a temperature control:

| Output signals | Heat | off | Cool |
| --- | --- | --- | --- |
| QPOS_P | TRUE | FALSE | FALSE |
| QNEG_P | FALSE | FALSE | TRUE |

Based on the input variable, a characteristic curve is used to calculate pulse duration. The form of the characteristic curve is defined by the minimum pulse time or minimum break time and the ratio factor. The normal value for the ratio factor is 1. The bend points in the characteristic curves are caused by the minimum pulse or minimum break times P_B_TM.

The following figure shows a symmetrical curve of the three-step controller (ratio factor = 1).

![Three-step control](images/34398418827_DV_resource.Stream@PNG-en-US.png)

#### Three-step control asymmetrical

Using the ratio factor RATIOFAC, the ratio of the duration of positive to negative pulses can be changed. In a thermal process, for example, this would allow different system time constants for heating and cooling.

**Ratio factor < 1**

The pulse duration at the negative pulse output calculated from the input variable multiplied by the period duration is reduced by the ratio factor.

Positive pulse duration = INV /100 * PER_TM

Negative pulse duration = INV / 100 * PER_TM * RATIOFAC

The negative pulse duration is multiplied with the ratio factor.

The following figure shows the asymmetric curve of the three-step controller (ratio factor = 0.5):

![Three-step control asymmetrical](images/52356449035_DV_resource.Stream@PNG-en-US.png)

The ratio factor RATIOFAC also influences the minimum pulse or minimum break time. The threshold value for negative pulses is multiplied by the ratio factor.

**Ratio factor > 1**

The pulse duration at the positive pulse output calculated from the input variable multiplied by the period duration is reduced by the ratio factor.

Positive pulse duration = INV / 100 * PER_TM / RATIOFAC

Negative pulse duration = INV / 100 * PER_TM

The ratio factor RATIOFAC also influences the minimum pulse or minimum break time. The threshold value for positive pulses is divided by the ratio factor.

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-pulsegen-s7-300-s7-400)
  
[PULSEGEN_M modes (S7-300, S7-400)](#pulsegen_m-modes-s7-300-s7-400)
  
[PULSEGEN_M two-step control (S7-300, S7-400)](#pulsegen_m-two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#output-parameter-pulsegen-s7-300-s7-400)

### PULSEGEN_M two-step control (S7-300, S7-400)

In two-step control, only the positive pulse output QPOS_P of PULSEGEN_M is connected to the on/off actuator in question. Depending on the manipulated value range used, the two-step controller has a bipolar or a unipolar manipulated value range.

**Two-step control with bipolar manipulated variable range  (-100% to 100%)**

![Figure](images/52359819531_DV_resource.Stream@PNG-en-US.png)

**Two-step control with unipolar manipulated variable range  (0% to 100%)**

![Figure](images/52359823499_DV_resource.Stream@PNG-en-US.png)

The negated output signal is available at QNEG_P if the connection of the two-step controller in the control loop requires a logically inverted binary signal for the actuating pulses.

| Pulse | Actuator On | Actuator Off |
| --- | --- | --- |
| QPOS_P | TRUE | FALSE |
| QNEG_P | FALSE | TRUE |

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-pulsegen-s7-300-s7-400)
  
[PULSEGEN_M modes (S7-300, S7-400)](#pulsegen_m-modes-s7-300-s7-400)
  
[PULSEGEN_M three-step control (S7-300, S7-400)](#pulsegen_m-three-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#output-parameter-pulsegen-s7-300-s7-400)

### Input parameters PULSEGEN_M (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  -100.0..100.0 (%) |
| PER_TM | 4.0 | TIME | T#1s | Period  PER_TM >= 20*CYCLE |
| P_B_TM | 8.0 | TIME | T#50ms | Minimum pulse or minimum break time  P_B_TM >= CYCLE |
| RATIOFAC | 12.0 | REAL | 1.0 | Ratio factor  0.1..10.0  (dimensionless) |
| STEP3_ON | 16.0 | BOOL | TRUE | Three-step control ON |
| ST2BI_ON | 16.1 | BOOL | FALSE | Activate two-step control for bipolar manipulated variable range |
| MAN_ON | 16.2 | BOOL | FALSE | Manual mode ON |
| POS_P_ON | 16.3 | BOOL | FALSE | Activate positive pulse |
| NEG_P_ON | 16.4 | BOOL | FALSE | Activate negative pulse |
| SYN_ON | 16.5 | BOOL | TRUE | Activate synchronization |
| COM_RST | 16.6 | BOOL | FALSE | Complete restart |
| CYCLE | 18.0 | TIME | T#10ms | Sampling time  CYCLE >= 1ms |

### Output parameters PULSEGEN_M (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| QPOS_P | 22.0 | BOOL | FALSE | Output signal positive pulse |
| QNEG_P | 22.1 | BOOL | FALSE | Output signal negative pulse |

## RMP_SOAK (S7-300, S7-400)

This section contains information on the following topics:

- [Description RMP_SOAK (S7-300, S7-400)](#description-rmp_soak-s7-300-s7-400)
- [Input parameters RMP_SOAK (S7-300, S7-400)](#input-parameters-rmp_soak-s7-300-s7-400)
- [Output parameters RMP_SOAK (S7-300, S7-400)](#output-parameters-rmp_soak-s7-300-s7-400)
- [Global data block DB_RMPSK (S7-300, S7-400)](#global-data-block-db_rmpsk-s7-300-s7-400)

### Description RMP_SOAK (S7-300, S7-400)

You use the RMP_SOAK instruction to specify different setpoints, primarily as a function of the process time.

#### Operating principle

You specify the time slice of the ramp/soak profile in a global data block. On each call of the instruction, the setpoint valid for this time is output.

The [Global data block DB_RMPSK](#global-data-block-db_rmpsk-s7-300-s7-400) Is not included in the library. You must create this global data block yourself.

You enter the number of time slices in the global data block in the NBR_PTS tag. You specify the number of the shared block in input parameter DB_NBR.

For each time slice, you enter the setpoint in PI[i].OUTV and the time in PI[i].TMV.

Example of a ramp/soak profile with starting point and time slices.

![Operating principle](images/18027528331_DV_resource.Stream@PNG-de-DE.png)

With n time slices, the time value for time slice n = 0 ms.

The method of counting of the time slice values and times is illustrated in the following figure:

![Operating principle](images/18027539723_DV_resource.Stream@PNG-en-US.png)

Between the time slices, the ramp/soak function interpolates with 0 ≤ n < (NBR_PTS - 1) according to the following function:

![Operating principle](images/18027558795_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The instruction does not check whether a global DB with the number DB_NBR actually exists or whether the DB_NBR.NBR_PTS parameter (number of time slices) is suitable for the data block length. If the parameter assignment is incorrect, the CPU changes to the STOP operating mode with the message "Internal system error".

#### Ramp/soak functions

The instruction has the following functions:

- Activate ramp/soak for single execution
- Pre-assign fixed value to the ramp/soak output
- Activate cyclic operation of the ramp/soak
- Hold processing of the ramp/soak
- Define the processing step and time (the residual time RS_TM and the time slice number TM_SNBR are redefined)
- Update the total processing time and remaining total time

The following table applies for the significance of the control inputs when setting a desired operating mode:

| Operating mode | RMPSK_ON | DFOUT_ON | RMP_ HOLD | CONT_ ON | CYC_ ON | TUPDT_ON | Output signal OUTV |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ramp/soak on | TRUE | FALSE | FALSE | **) | FALSE | **) | OUTV(t)  End value is held after the end of processing. |
| Pre-assign output | TRUE | TRUE | **) | **) | **) | **) | DF_OUTV |
| Cyclic operation on | TRUE | FALSE | FALSE | **) | TRUE | **) | OUTV(t)  After end: Automatic start |
| Hold ramp/soak | TRUE | FALSE | TRUE | FALSE | **) | **) | Current value of OUTV(t) is held *) |
| Pre-assign processing step and processing time | TRUE | FALSE | TRUE | TRUE | **) | **) | OUTV (old) *) |
| FALSE | Operation is continued with newly defined values. |  |  |  |  |  |  |
| Update total time | **) | **) | **) | **) | **) | FALSE | Does not influence OUTV |
|  | TRUE | Does not influence OUTV |  |  |  |  |  |
| *) The ramp/soak profile does not have the form configured by the user until the next time slice.  **) The respective operating mode set is executed irrespective of the significance of the control signals in the fields marked with **) |  |  |  |  |  |  |  |

#### Restart

During a complete restart, output OUTV is reset to 0.0. When DFOUT_ON=TRUE, DF_OUTV is output. The time intervals (0 to NBRPTS-1) between the time slices 0 to NBRPTS are totaled and made available under T_TM. The output QR_S_ACT is reset. The outputs NBR_ATMS and RS_TM are pre-assigned with 0.

#### Activating the ramp/soak

On a positive edge at RMPSK_ON, the ramp/soak function is activated. The ramp/soak profile is terminated after the last time slice has been reached. In order to restart the ramp/soak function, you must first set RMPSK_ON = FALSE and then RMPSK_ON = TRUE.

#### Pre-assigning the output, starting the ramp/soak profile

If the ramp/soak profile is to start with a particular output value, DFOUT_ON = TRUE must be set. In this case, signal value DF_OUTV is applied at the output of the ramp/soak.

> **Note**
>
> The signal for the output of constant setpoint DFOUT_ON has a higher priority than the start signal for ramp/soak RMPSK_ON.

On changeover (DFOUT_ON = FALSE), OUTV moves linearly from the specified setpoint (DF_OUTV) to the output value of the current time slice number PI[NBR_ATMS].OUTV.

The internal time processing continues running even when a fixed setpoint (RMPSK_ON = TRUE and DFOUT_ON = TRUE) is switched through.

On the start of the ramp/soak profile (RMPSK_ON = TRUE), the fixed setpoint DF_OUTV continues to be output until DFOUT_ON changes from TRUE to FALSE after the duration of T*.

![Pre-assigning the output, starting the ramp/soak profile](images/18027574795_DV_resource.Stream@PNG-en-US.png)

At this moment, the time PI[0].TMV and a part of the time PI[1].TMV has expired. OUTV is moved from DF_OUTV to PI[2].OUTV, which means to the setpoint at time slice 2.

The configured ramp/soak profile is output only starting from time slice 2. The agreement of the configured and current ramp/soak profile is displayed by setting QR_S_ACT = TRUE. On a positive edge at DFOUT_ON during processing of the ramp/soak profile, the output value OUTV jumps to DF_OUTV without a delay.

#### Cyclic operation activated

If "Cyclic repetition" operating mode (CYC_ON = TRUE) is activated, the ramp/soak function automatically returns to the starting point after the last time slice value has been output and begins a new run.

There is no interpolation between the last time slice and the starting point. For a smooth transition, the following must be true: PI[NBR_PTS].OUTV = PI[0].OUTV.

#### Hold ramp/soak

With RMP_HOLD = TRUE, the value of the output variable (including the time processing) is frozen. When RMP_HOLD = FALSE is reset, the function resumes at the interruption point PI[x].TMV.

The processing time of the ramp/soak profile is extended by the amount of the time T*. The ramp/soak profile has the configured characteristic from the starting point until the positive edge at RMP_HOLD and from time slice 5* to time slice 6*, i.e. output signal QR_S_ACT has the value TRUE.

![Hold ramp/soak](images/18027593867_DV_resource.Stream@PNG-en-US.png)

#### Pre-assigning the processing step and processing time

With CONT_ON, a held ramp/soak profile is restarted at a defined point. If the ramp/soak function is not held, CONT_ON has no effect.

If the control input for continuing (CONT_ON = TRUE) is set, the held ramp/soak function is continued at time slice TM_SNBR. TM_CONT determines the remaining time that the ramp/soak function requires to reach time slice TM_SNBR.

The following figure shows the effect of RMP_HOLD and CONT_ON.

TM_SNBR = 5 and TM_CONT = T*

![Pre-assigning the processing step and processing time](images/18027612939_DV_resource.Stream@PNG-en-US.png)

Time slices 3 and 4 are omitted in this cycle of the ramp/soak function.

On a signal change of RMP_HOLD from TRUE to FALSE, the configured characteristic curve is only reached again starting from time slice 5.

#### Updating the total time and remaining total time

The current time slice number NBR_ATMS, the current remaining time until the time slice is reached (RS_TM), the total time T_TM, and the total remaining time until the end of the ramp/soak profile (RT_TM) are updated in every cycle.

In the case of online changes of PI[n].TMV, the total time and the total remaining time of the ramp/soak profile change. Since the calculation of T_TM and RT_TM with many time slices significantly increases the processing time of the function block, the calculation is only carried after a restart or when TUPDT_ON = TRUE. The time intervals PI[0 ... NBR_PTS].TMV between the individual time slices are added up and indicated at the total time T_TM and total remaining time RT_TM outputs.

Please note that determining the total times requires significant CPU runtime.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)

### Input parameters RMP_SOAK (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| DF_OUTV | 0.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| DB_NBR | 4.0 | BLOCK_DB | DB 1 | Data block number, shared (time slice values)  CPU-dependent |
| TM_SNBR | 6.0 | INT | 0 | No. of next time slice for continuation  0 - 255 |
| TM_CONT | 8.0 | TIME | T#0s | Remaining time for continuing until time slice TM_SNBR  Engineering value range |
| DFOUT_ON | 12.0 | BOOL | FALSE | Default setting of output variable On |
| RMPSK_ON | 12.1 | BOOL | FALSE | Ramp/soak function ON |
| HOLD | 12.2 | BOOL | FALSE | Hold the output variable |
| CONT_ON | 12.3 | BOOL | FALSE | Continue |
| CYC_ON | 12.4 | BOOL | FALSE | Cyclic repetition ON |
| TUPDT_ON | 12.5 | BOOL | FALSE | Update total time after change in times (extended block run time!) |
| COM_RST | 12.6 | BOOL | FALSE | Complete restart |
| CYCLE | 14.0 | TIME | T#1s | Sampling time  Engineering value range ≥ 1 ms |

### Output parameters RMP_SOAK (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 18.0 | REAL | 0.0 | Output variable |
| QR_S_ACT | 22.0 | BOOL | FALSE | ramp/soak is being executed |
| NBR_ATMS | 24.0 | INT | 0 | Current time slice number (time slice that is being approached) |
| RS_TM | 26.0 | TIME | T#0s | Residual slice time |
| T_TM | 30.0 | TIME | T#0s | Shared data: Total time ΣTMVI |
| RT_TM | 34.0 | TIME | T#0s | Shared data: Residual total time ΣTMVI |

The time slices as well as the number of time slices NBRPTS are stored in a shared data block DB_NBR. Output begins with time slice 0 and ends with the time slice NBR_PTS.

### Global data block DB_RMPSK (S7-300, S7-400)

The time slices for the ramp/soak function (RMP_SOAK) are specified in a global data block. This global data block is not included in the library. You must create this global data block yourself according to the following scheme and adapt it to your application.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| NBR_PTS | INT | 4 | Number of time slices -1  1 - 255 |
| PI | Array [0...NBR_PTS] of Struct |  | Time slice data structure. The array must be declared by 0...NBR_PTS. |
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

Alternatively, you can generate the global data block using an external source file. To do so, proceed as follows:

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

`DATA_BLOCK "DB_RMPSK"`

`TITLE = data block ramp soak`

`{ S7_Optimized_Access := 'FALSE' }`

`NAME : DB_RMPSK`

`STRUCT`

`NBR_PTS : Int; // number of points (excluding starting point)`

`PI : Array[0..4] of Struct`

`OUTV : Real; // output variable`

`TMV : Time; // output time value`

`END_STRUCT;`

`END_STRUCT;`

`BEGIN`

`NBR_PTS := 4;`

`PI[0].TMV := T#1s;`

`PI[1].TMV := T#1s;`

`PI[2].TMV := T#1s;`

`PI[3].TMV := T#1s;`

`PI[4].TMV := T#0s;`

`END_DATA_BLOCK`

## ROC_LIM (S7-300, S7-400)

This section contains information on the following topics:

- [Description ROC_LIM (S7-300, S7-400)](#description-roc_lim-s7-300-s7-400)
- [Input parameters ROC_LIM (S7-300, S7-400)](#input-parameters-roc_lim-s7-300-s7-400)
- [Output parameters ROC_LIM (S7-300, S7-400)](#output-parameters-roc_lim-s7-300-s7-400)

### Description ROC_LIM (S7-300, S7-400)

Ramp functions are used when the process does not tolerate an input step. This is for example the case when a gearbox is inserted between a motor and the load to be driven and an excessively rapid increase of the motor speed would result in overloading of the gearbox. The instruction limits the rate of change of an output value. Step jump functions become ramp functions.

#### Operating principle

A total of four ramps can be assigned for the positive and negative value range of input variable INV for use in determining the output variable:

- UPRLM_P: Rising values in the positive range

  OUTV > 0 and |OUTV| rising
- DNRLM_P: Falling values in the positive range

  OUTV > 0 and |OUTV| falling
- UPRLM_N: Rising values in the negative range

  OUTV < 0 and |OUTV| rising
- DNRLM_N: Falling values in the negative range

  OUTV < 0 and |OUTV| falling

  ![Operating principle](images/18027648011_DV_resource.Stream@PNG-de-DE.png)

The assigned values of the ramps refer to a rising or falling slope of the output variable per second.

If UPRLM_P = 10.0 and |INV| are rising, OUTV may increase by a maximum of 10.0 in 1 s.

If the input variable rises at a higher rate, OUTV is increased as follows, according to the sampling time CYCLE per call:

| CYCLE [s] | Increase of OUTV |
| --- | --- |
| 1 | 10.0 |
| 0.1 | 1.0 |
| 0.01 | 0.1 |

The limiting of the rate of change is indicated in the QUPRLM_P, QDNRLM_P, QUPRLM_N, and QDNRLM_N parameters.

The output variable can be limited by H_LM and L_LM. This is indicated in the QH_LM and QL_LM parameters.

#### Functions of the instruction

You can use the DFOUT_ON, TRACK, and MAN_ON parameters to influence how the instruction works.

- DFOUT_ON = TRUE

  If DFOUT_ON = TRUE is set, DF_OUTV is output at output OUTV; on a falling edge, OUTV moves from DF_OUTV to INV, and on a rising edge, OUTV moves from INV to DF_OUTV.
- TRACK = TRUE

  Bit TRACK = TRUE is set in order to track OUTV = INV. Since the input variable is switched through directly to the output variable, step changes in the input variable are also output.
- MAN_ON = TRUE

  With MAN_ON = TRUE, you can perform a bumpless changeover between manual and automatic mode. For this purpose, the ROC_LIM instruction is inserted in the setpoint branch directly upstream of the control deviation. The process value is interconnected with input PV and the manual-automatic bit, e.g., LMNGEN_C.MAN_ON is interconnected with input MAN_ON.

  ![Functions of the instruction](images/18027682187_DV_resource.Stream@PNG-de-DE.png)

  On changeover to manual mode (MAN_ON = TRUE), the value applied to input PV is switched through immediately to output OUTV. Since the setpoint and the process value are equal, the control deviation becomes zero and the controller is in a steady-state idle condition. On reset to automatic mode (MAN_ON = FALSE), output OUTV moves from the current value PV to input value INV along a ramp. This causes a bumpless changeover of the controller structure from manual to automatic mode.

  When MAN_ON = TRUE, the H_LM and L_LM limits have no effect; DFOUT_ON is not taken into consideration.

#### Example 1

When MAN_ON, TRACK, DFOUT_ON equal FALSE , the signal outputs exhibit the following characteristics:

![Example 1](images/18027659403_DV_resource.Stream@PNG-de-DE.png)

#### Example 2

Smooth manual-automatic changeover

![Example 2](images/18027670795_DV_resource.Stream@PNG-de-DE.png)

#### Example 3

Ramp that is only used in the positive range of values.

![Example 3](images/52435620747_DV_resource.Stream@PNG-en-US.png)

#### Complete restart

During a complete restart, the output OUTV is reset to 0.0. If DFOUT_ON = TRUE is set, DF_OUTV is output. All the signal outputs are set to FALSE.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)

### Input parameters ROC_LIM (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| UPRLM_P | 4.0 | REAL | 10.0 | Rise limiter in the positive range  Increment per second [1/s]  > 0.0 |
| DNRLM_P | 8.0 | REAL | 10.0 | Fall limiter in the positive range  Increment per second [1/s]  > 0.0 |
| UPRLM_N | 12.0 | REAL | 10.0 | Rise limiter in the negative range  Increment per second [1/s]  > 0.0 |
| DNRLM_N | 16.0 | REAL | 10.0 | Fall limiter in the negative range  Increment per second [1/s]  > 0.0 |
| H_LM | 20.0 | REAL | 100.0 | High limit  Engineering value range  > L_LM |
| L_LM | 24.0 | REAL | 0.0 | Low limit  Engineering value range  < H_LM |
| PV | 28.0 | REAL | 0.0 | Controlled variable  Engineering value range |
| DF_OUTV | 32.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| DFOUT_ON | 36.0 | BOOL | FALSE | Default setting of output variable On |
| TRACK | 36.1 | BOOL | FALSE | Tracking OUTV=INV |
| MAN_ON | 36.2 | BOOL | FALSE | Manual mode ON |
| COM_RST | 36.3 | BOOL | FALSE | Complete restart |
| CYCLE | 38.0 | TIME | T#1s | Sampling time |

### Output parameters ROC_LIM (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 42.0 | REAL | 0.0 | Output variable |
| QUPRLM_P | 46.0 | BOOL | FALSE | Rise limiter in the positive range triggered |
| QDNRLM_P | 46.1 | BOOL | FALSE | Fall limiter in the positive range triggered |
| QUPRLM_N | 46.2 | BOOL | FALSE | Rise limiter in the negative range triggered |
| QDNRLM_N | 46.3 | BOOL | FALSE | Fall limiter in the negative range triggered |
| QH_LM | 46.4 | BOOL | FALSE | High limit triggered |
| QL_LM | 46.5 | BOOL | FALSE | Low limit triggered |

## SCALE_M (S7-300, S7-400)

This section contains information on the following topics:

- [Description SCALE_M (S7-300, S7-400)](#description-scale_m-s7-300-s7-400)
- [Input parameters SCALE_M (S7-300, S7-400)](#input-parameters-scale_m-s7-300-s7-400)
- [Output parameters SCALE_M (S7-300, S7-400)](#output-parameters-scale_m-s7-300-s7-400)

### Description SCALE_M (S7-300, S7-400)

In the case of process values, the value supplied by the encoder often lies in a range that is unfavorable for the user (for example, 0 to 10 V corresponds to 0 to 1200 ºC or 0 to 10 V corresponds to 0 to 3000 rpm). By adapting the setpoint or the process value, both process variables lie in the same range of values.

#### Operating principle

The instruction scales an analog input variable. Analog input variable INV is transformed to output variable OUTV based on the scaling line. The scaling line is defined by the slope (FACTOR) and the distance (OFFSET) between OUTV when INV=0 and coordinate axis OUTV=0 is defined.

Formula:

OUTV = INV * FACTOR + OFFSET

![Operating principle](images/18027728651_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)
  
[Processing the process value (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-the-process-value-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#applying-the-disturbance-variable-s7-300-s7-400)

### Input parameters SCALE_M (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| FACTOR | 4.0 | REAL | 1.0 | Scaling factor |
| OFFSET | 8.0 | REAL | 0.0 | Offset  Engineering value range |

### Output parameters SCALE_M (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV | 12.0 | REAL | 0.0 | Output variable |

## SP_GEN (S7-300, S7-400)

This section contains information on the following topics:

- [Description SP_GEN (S7-300, S7-400)](#description-sp_gen-s7-300-s7-400)
- [Input parameters SP_GEN (S7-300, S7-400)](#input-parameters-sp_gen-s7-300-s7-400)
- [Output parameters SP_GEN (S7-300, S7-400)](#output-parameters-sp_gen-s7-300-s7-400)

### Description SP_GEN (S7-300, S7-400)

An output value can be changed using the SP_GEN instruction and two inputs in order to specify the setpoint manually. To carry out a change in small steps, the instruction should have a sampling time of ≤100 ms.

#### Operating principle

DFOUT_ON, OUTVUP, and OUTVDN have the following effect on OUTV:

| DFOUT_ON | OUTVDN | OUTVUP | OUTV |
| --- | --- | --- | --- |
| TRUE | Any | Any | DF_OUTV |
| FALSE | TRUE | TRUE | OUTV unchanged |
| FALSE | OUTV rising |  |  |
| TRUE | FALSE | OUTV falling |  |
| FALSE | OUTV unchanged |  |  |

If DFOUT_ON = TRUE is set, DF_OUTV is output at the output. The change in OUTV is a step change. The changeover to DFOUT_ON = FALSE is bumpless.

The OUTVUP input can be used to continuously increase output variable OUTV within the limits H_LM and L_LM; accordingly, the OUTVDN output is used for reducing. The rate of change of OUTV depends on the limits.

- During the first 3 s after setting of OUTVUP or OUTVDN:

  dLMN/dt = (LMN_HLM - LMN_LLM) / 100 s
- Afterwards:

  dLMN/dt = (LMN_HLM - LMN_LLM) / 10 s

The figure shows the change in the output value when OUTVUP is set.

![Operating principle](images/18027756043_DV_resource.Stream@PNG-de-DE.png)

OUTVUP and OUTVDN are executed only if DFOUT_ON = FALSE.

Output variable OUTV is limited by H_LM and L_LM. This is indicated in the QH_LM and QL_LM parameters.

The figure shows how OUTVUP, OUTVDN, and DFOUTV_ON. affect OUTV.

![Operating principle](images/18027794827_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

During a complete restart, the output OUTV is set to 0.0. If DFOUT_ON = TRUE, DF_OUTV is output. The limits remain valid at a compete restart.

#### Block-internal limits

No values are limited block-internally. The parameters are not checked.

---

**See also**

[Processing setpoints (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#processing-setpoints-s7-300-s7-400)

### Input parameters SP_GEN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| DF_OUTV | 0.0 | REAL | 0.0 | Default setting of output variable  Engineering value range |
| H_LM | 4.0 | REAL | 100.0 | High limit  Engineering value range   > L_LM |
| L_LM | 8.0 | REAL | 0.0 | Low limit  Engineering value range   < H_LM |
| OUTVUP | 12.0 | BOOL | FALSE | OUTV up |
| OUTVDN | 12.1 | BOOL | FALSE | OUTV down |
| DFOUT_ON | 12.2 | BOOL | FALSE | Default setting of output variable On |
| COM_RST | 12.3 | BOOL | FALSE | Complete restart |
| CYCLE | 14.0 | TIME | T#100ms | Sampling time |

### Output parameters SP_GEN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value   (on complete restart) | Description |
| --- | --- | --- | --- | --- |
| OUTV | 18.0 | REAL | 0.0 | Output variable |
| QH_LM | 22.0 | BOOL | FALSE | High limit triggered |
| QL_LM | 22.1 | BOOL | FALSE | Low limit triggered |

## SPLT_RAN (S7-300, S7-400)

This section contains information on the following topics:

- [Description SPLT_RAN (S7-300, S7-400)](#description-splt_ran-s7-300-s7-400)
- [Input parameters SPLT_RAN (S7-300, S7-400)](#input-parameters-splt_ran-s7-300-s7-400)
- [Output parameters SPLT_RAN (S7-300, S7-400)](#output-parameters-splt_ran-s7-300-s7-400)

### Description SPLT_RAN (S7-300, S7-400)

The instruction is required, for example to split a temperature control loop into an actuator for cooling and an actuator for heating.

#### Operating principle

The manipulated variable of a PID controller is spilt into several ranges. The instruction must be called once per range and be interconnected with manipulated variable processing block LMNGEN_C or LMNGEN_S. If you interconnect LMNGEN_S, position feedback must be activated (LMNR_ON = TRUE).

![Operating principle](images/35190495115_DV_resource.Stream@PNG-de-DE.png)

If input value INV is within the range STR_INV and EDR_INV, output value SPL_LMNG.PID_OUTV is output within the range STR_OUTV and EDR_OUTV. If INV < STR_INV,, then STR_OUTV is output. If INV > STR_INV,, then EDR_OUTV is output.

![Operating principle](images/18027822219_DV_resource.Stream@PNG-de-DE.png)

#### Complete restart

The block does not have a complete restart routine.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters SPLT_RAN (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV | 0.0 | REAL | 0.0 | Input variable  Engineering value range |
| STR_INV | 4.0 | REAL | 0.0 | Start of range INV  Engineering value range |
| EDR_INV | 8.0 | REAL | 50.0 | End of range INV  Engineering value range |
| STR_OUTV | 12.0 | REAL | 0.0 | Start of range OUTV  Engineering value range |
| EDR_OUTV | 16.0 | REAL | 100.0 | End of range OUTV  Engineering value range |

### Output parameters SPLT_RAN (S7-300, S7-400)

| Parameter | Offset | Data type | Description |
| --- | --- | --- | --- |
| SPL_LMNG | 20.0 | STRUC | PID-LMNGEN interface |

## SWITCH (S7-300, S7-400)

This section contains information on the following topics:

- [Description SWITCH (S7-300, S7-400)](#description-switch-s7-300-s7-400)
- [Input parameters SWITCH (S7-300, S7-400)](#input-parameters-switch-s7-300-s7-400)
- [Output parameters SWITCH (S7-300, S7-400)](#output-parameters-switch-s7-300-s7-400)

### Description SWITCH (S7-300, S7-400)

The instruction is used as an input and/or output multiplexer of 2 input/output variables.

#### Operating principle

The instruction connects one of two analog input values to one of two output values. The INV1_ON and OUTV1_ON switches determine how the instruction operates.

|  |  |  |  |
| --- | --- | --- | --- |
| INV1_ON | OUTV1_ON | OUTV1 | OUTV2 |
| FALSE | FALSE | Unchanged | INV2 |
| TRUE | FALSE | Unchanged | INV1 |
| FALSE | TRUE | INV2 | Unchanged |
| TRUE | TRUE | INV1 | Unchanged |

Unchanged means that the value from the last cycle is retained in the output parameter.

#### Complete restart

On a complete restart, OUTV1 = 0.0 and OUTV2 = 0.0 are set.

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters SWITCH (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| INV1 | 0.0 | REAL | 0.0 | Input variable 1  Engineering value range |
| INV2 | 4.0 | REAL | 0.0 | Input variable 2  Engineering value range |
| INV1_ON | 8.0 | BOOL | FALSE | Input variable INV1 is switched through |
| OUTV1_ON | 8.1 | BOOL | FALSE | Output variable OUTV1 is switched through |
| COM_RST | 8.2 | BOOL | FALSE | Complete restart |

### Output parameters SWITCH (S7-300, S7-400)

| Parameter | Offset | Data type | Preassigned value | Description |
| --- | --- | --- | --- | --- |
| OUTV1 | 10.0 | REAL | 0.0 | Output variable 1 |
| OUTV2 | 14.0 | REAL | 0.0 | Output variable 2 |

## LP_SCHED_M (S7-300, S7-400)

This section contains information on the following topics:

- [Description LP_SCHED_M (S7-300, S7-400)](#description-lp_sched_m-s7-300-s7-400)
- [Operating principle LP_SCHED_M (S7-300, S7-400)](#operating-principle-lp_sched_m-s7-300-s7-400)
- [Input parameters LP_SCHED_M (S7-300, S7-400)](#input-parameters-lp_sched_m-s7-300-s7-400)
- [Global data block for DB_LOOP (S7-300, S7-400)](#global-data-block-for-db_loop-s7-300-s7-400)

### Description LP_SCHED_M (S7-300, S7-400)

If many controllers with different sampling times, in particular slow control systems with high sampling times, have to be called, the scope of the priority class model with regard to usable cyclic interrupt levels is insufficient. The controller call distribution function (LP_SCHED) now makes it possible to integrate several controllers with different sampling times in a cyclic interrupt level. The individual controllers can then called up cyclically with their sampling times.

Use of the controller call distribution function is not mandatory. The controller instructions can also be called directly from the OB without the distribution function.

The call distribution of several controllers on a cyclic interrupt level is implemented in the LP_SCHED instruction. The instruction must be called up **before** all control loops. The data for the individual controller calls is stored in a global data block (DB_LOOP).

![Figure](images/18027022475_DV_resource.Stream@PNG-en-US.png)

[Global data block for DB_LOOP](#global-data-block-for-db_loop-s7-300-s7-400) is not included in the library. You must create this global data block yourself.

The call distributor processes the global data block and sets the ENABLE bits depending on the sequence and the parameterized sampling times of the controllers. The time cycle of the cyclic interrupt level is subordinated by this. The individual control loops on this cyclic interrupt level are called up and processed according to their set sampling time. The ENABLE bit has to be reset again after the block call. The block calls and the reset of the ENABLE bits have to be programmed.

The call of individual control loops can be manually blocked. Individual control loops can also be reset (restart).

> **Note**
>
> The instruction does not check whether a global DB with the number DB_NBR actually exists or whether the GLP_NBR parameter (largest control loop number) is suitable for the data block length. If the parameter assignment is incorrect, the CPU changes to STOP with an "internal system error".

---

**See also**

[Creating a pulse controller (S7-300, S7-400)](Using%20modular%20PID%20control%20%28S7-300%2C%20S7-400%29.md#creating-a-pulse-controller-s7-300-s7-400)

### Operating principle LP_SCHED_M (S7-300, S7-400)

#### Restart

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

#### Control loop call via LP_SCHED_M

The LP_SCHED instruction is included by means of three input parameters in the call scheme of the CPU. The time cycle of the cyclic interrupt level is specified at the TM_BASE input. The execution call of the assigned control loops is carried out via a conditional block call from one cyclic interrupt level (for example OB 35). In the course the ENABLE bits in the global data block are sampled.

If the call is carried out from the restart level, input COM_RST = TRUE is set. This call has to be reset again to FALSE in the cyclic interrupt level. The global data block (see previous table) with the time-relevant data of the control loops in the respective cyclic interrupt level is assigned via the input parameter DB_NBR.

#### Parameter assignment of the control loop call (global DB)

The parameter assignment of the controller call distribution function has to be carried out **without** support by the configuration software.

The data block (DB_LOOP) contains both a parameter that determines the total number of control loops that have to be processed on the respective cyclic interrupt level (max. 256) and a parameter that displays the control loop that is currently being processed:

| Symbol | Meaning |
| --- | --- |
| GLP_NBR | Largest control loop number |
| ALP_NBR | Number of the control loop processed in the cycle |

The number of the respective control loop results from the positioning of its call data in the sequence of the entries in the DB.

The call data of the individual control loops resides structured in the LOOP_DAT field. If control loops are to be added, the field length of LOOP_DAT has to be adapted. To this purpose the ARRAY data type has to be adapted in the declaration view. For example, with 10 control loops, you must enter ARRAY[1..10]. In addition the GLP_NBR parameter has to be adapted in the data view. It may never be larger than the field length.

The parameters COM_RST and CYCLE in the call data must be interconnected to the corresponding input parameters at the FB of the calling control loop. This interconnection is to be programmed by the user. If the ENABLE parameter is set, the corresponding control loop is to be called. The ENABLE bit has to be reset after the controller call. The conditional controller call and the reset of the ENABLE bit have to be programmed by the user.

With the aid of the manually adjustable parameters MAN_CYC/MAN_DIS/MAN_CRST, one can control whether a control loop can or cannot be called. These call data can be modified online - during operation - so long as only the parameters are overwritten and the entire DB is not regenerated. The following meanings apply:

| Symbol | Meaning |
| --- | --- |
| MAN_CYC | The sampling time of the respective controller (is rounded to an integer multiple of TM_BASE * GLP_NBR in CYCLE). |
| MAN_DIS | Disabling of the controller call |
| MAN_CRST | Restart for this controller |

#### Call processing

The corresponding control loop is processed in accordance with the previous DB parameter assignment, depending on the value of the ENABLE signal of the controller call data.

The data block is processed from top to bottom. Per cycle the call distribution function moves one control loop number (ALP_NBR) further in the sequence of the DB. The internal counter ILP_COU is counted down by 1 at the same time. If ILP_COU = 0, the call distribution function sets the ENABLE bit of the corresponding control loop. Resetting of the ENABLE bits has to be programmed by the user after the controller call.

The parameter MAN_CYC is transferred to CYCLE during processing:

CYCLE = GV (MAN_CYC), GV = integer multiple

![Principle of the controller call using the call distribution function LP_SCHED](images/18027038475_DV_resource.Stream@PNG-en-US.png)

Principle of the controller call using the call distribution function LP_SCHED

- Blocking individual control loops:

  If you set the bit "MAN_DIS" by parameter assignment in the DB data block, the "ENABLE" bit is reset to FALSE and the respective control loop is excluded from processing in the call distribution function.
- Resetting individual control loops (restart):

  If you set the "MAN_CRST" bit by parameter assignment in the DB, COM_RST = TRUE and MAN_CRST is subsequently reset. The respective control loop is processed with its restart routine. In the next call cycle, COM_RST = FALSE is also reset automatically.

  > **Note**
  >
  > If a control loop is inserted or deleted, meaning that the whole DB is regenerated, without the call distribution function having to be processed in the restart, the internal control loop counter (ILP_COU[n]) and the parameter for the current control loop number ALP_NBR have to have zero pre-assigned.

#### Conditions for control loop call via LP_SCHED

In order to ensure that the intervals between the calls of a specific controller remain constant and to utilize the CPU evenly, the cyclic interrupt level may only process one control loop per cycle. The following conditions must therefore be observed during the parameter assignment of the sampling times MAN_CYC in relation to the cycle (TM_BASE):

- The processing times of the individual control loops have to be smaller than the cycle (TM_BASE) of the cyclic interrupt level.
- The sampling time of a control loop (MAN_CYC) has to be an integer multiple (GV) of the product of the time base and number of the controllers to be processed (GLP_NBR):

  MAN_CYC = GV (TM_BASE * GLP_NBR)

#### Example for call distribution function

The following example shows the call sequence of four control loops in a cyclic interrupt level (see following figure). Only one control loop is always processed per unit of the time base. The call sequence and thus the displacement times (TD1 ... TD5) result from the sequence of the call data within the global DB.

![Call sequence of four control loops that are processed at varying intervals](images/18027054475_DV_resource.Stream@PNG-en-US.png)

Call sequence of four control loops that are processed at varying intervals

#### Block-internal limits

The values of the input parameters are not limited in the instruction. There is no parameter check.

### Input parameters LP_SCHED_M (S7-300, S7-400)

| Parameter | Data type | Description |
| --- | --- | --- |
| TM_BASE | TIME | Time base  >= 1ms |
| COM_RST | BOOL | Complete restart |
| DB_NBR | BLOCK_DB | Data block number |

### Global data block for DB_LOOP (S7-300, S7-400)

The data for the call distribution with LP_SCHED is specified in a global data block. This global data block is not included in the library. You must create this global data block yourself according to the following scheme and adapt it to your application.

| Parameter | Data type | Preassigned value | Description |
| --- | --- | --- | --- |
| GLP_NBR | INT | 2 | Maximum number of controllers  1 - 256 |
| ALP_NBR | INT | 0 | Number of the current controller  0 - 256 |
| LOOP_DAT | Array [1...GLP_NBR] of Struct |  | Individual controller data structure. The array must be declared by 1...GLP_NBR. |
| LOOP_DAT[1].MAN_CYC | TIME | T#1s | Controller 1 data: Manual sampling time  >= 1ms |
| LOOP_DAT[1].MAN_DIS | BOOL | FALSE | Controller 1 data: Disable manual controller call |
| LOOP_DAT[1].MAN_CRST | BOOL | FALSE | Controller 1 data: Set manual restart |
| LOOP_DAT[1].ENABLE | BOOL | FALSE | Controller 1 data: Controller enable |
| LOOP_DAT[1].COM_RST | BOOL | FALSE | Controller 1 data: Restart |
| LOOP_DAT[1].ILP_COU | INT | 0 | Controller 1 data: Internal counter |
| LOOP_DAT[1].CYCLE | TIME | T#1s | Controller 1 data: Sampling time  >= 1ms |
| LOOP_DAT[2].MAN_CYC |  |  | Controller 2 data: Manual sampling time |
| ... |  |  |  |

Alternatively, you can generate the global data block using an external source file. To do so, proceed as follows:

1. Copy the text below to the clipboard.
2. Open an external text editor.
3. Paste the copied text from the clipboard to the text editor.
4. Save the file with the file name extension " .DB":
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

`DATA_BLOCK "DB_LOOP"`

`TITLE = data block loop scheduler`

`{ S7_Optimized_Access := 'FALSE' }`

`NAME : DB_LOOP`

`STRUCT`

`GLP_NBR : Int; // greatest loop number`

`ALP_NBR : Int; // actual loop number`

`LOOP_DAT : Array[1..2] of Struct`

`MAN_CYC : Time; // loop data: manual sample time`

`MAN_DIS : Bool; // loop data: manual loop disable`

`MAN_CRST : Bool; // loop data: manual complete restart`

`ENABLE : Bool; // loop data: enable loop`

`COM_RST : Bool; // loop data: complete restart`

`ILP_COU : Int; // loop data: internal loop counter`

`CYCLE : Time; // loop data: sample time`

`END_STRUCT;`

`END_STRUCT;`

`BEGIN`

`GLP_NBR := 2;`

`LOOP_DAT[1].MAN_CYC := T#1S;`

`LOOP_DAT[1].CYCLE := T#1S;`

`LOOP_DAT[2].MAN_CYC := T#200MS;`

`LOOP_DAT[2].CYCLE := T#200MS;`

`END_DATA_BLOCK`
