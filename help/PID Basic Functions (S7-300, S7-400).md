---
title: "PID Basic Functions (S7-300, S7-400)"
package: ProgFBPIDBasenUS
topics: 44
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PID Basic Functions (S7-300, S7-400)

This section contains information on the following topics:

- [CONT_C (S7-300, S7-400)](#cont_c-s7-300-s7-400)
- [CONT_S (S7-300, S7-400)](#cont_s-s7-300-s7-400)
- [PULSEGEN (S7-300, S7-400)](#pulsegen-s7-300-s7-400)
- [TCONT_CP (S7-300, S7-400)](#tcont_cp-s7-300-s7-400)
- [TCONT_S (S7-300, S7-400)](#tcont_s-s7-300-s7-400)
- [Integrated system functions (S7-300, S7-400)](#integrated-system-functions-s7-300-s7-400)

## CONT_C (S7-300, S7-400)

This section contains information on the following topics:

- [Description CONT_C (S7-300, S7-400)](#description-cont_c-s7-300-s7-400)
- [How CONT_C works (S7-300, S7-400)](#how-cont_c-works-s7-300-s7-400)
- [CONT_C block diagram (S7-300, S7-400)](#cont_c-block-diagram-s7-300-s7-400)
- [Input parameter CONT_C (S7-300, S7-400)](#input-parameter-cont_c-s7-300-s7-400)
- [Output parameters CONT_C (S7-300, S7-400)](#output-parameters-cont_c-s7-300-s7-400)

### Description CONT_C (S7-300, S7-400)

The CONT_C instruction is used on SIMATIC S7 automation systems to control technical processes with continuous input and output variables. You can assign parameters to enable or disable sub-functions of the PID controller and adapt it to the process. In addition to the functions in the setpoint and process value branches, the instruction implements a complete PID controller with continuous output value output and the option of manually influencing the value of the output value.

#### Application

You can use the controller as a PID fixed setpoint controller, or in multi-loop control systems, also as a cascade, blending or ratio controller. The functions of the controller are based on the PID control algorithm of the sampling controller with an analog signal, if necessary extended by including a pulse shaper stage to generate pulse-width modulated output signals for two or three step controllers with proportional actuators.

#### Call

The CONT_C instruction has an initialization routine that is run through when input parameter COM_RST = TRUE is set. During initialization, the integral action is set to the initialization value I_ITVAL. All the signal outputs are set to zero. COM_RST = FALSE has to be set after the initialization routine has been completed.

The calculation of the values in the control blocks is only correct if the block is called at regular intervals. You should therefore call the control blocks in a cyclic interrupt OB (OB 30 to OB 38). Enter the sampling time in the CYCLE parameter.

#### Error information

The error message word RET_VAL is not evaluated by the block.

---

**See also**

[How CONT_C works (S7-300, S7-400)](#how-cont_c-works-s7-300-s7-400)
  
[CONT_C block diagram (S7-300, S7-400)](#cont_c-block-diagram-s7-300-s7-400)
  
[Input parameter CONT_C (S7-300, S7-400)](#input-parameter-cont_c-s7-300-s7-400)
  
[Output parameters CONT_C (S7-300, S7-400)](#output-parameters-cont_c-s7-300-s7-400)
  
[Differences compared to CONT_C S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_c-s7-300400-s7-1500)

### How CONT_C works (S7-300, S7-400)

#### Setpoint branch

The setpoint is entered in floating-point format at the SP_INT input.

#### Process value branch

The process value can be input in I/O or floating-point format. The function CRP_IN converts the I/O value PV_PER to a floating-point format -100 to +100 % in accordance with the following rule:

Output of CRP_IN = PV_PER * 100 / 27648

The PV_NORM function scales the output of CRP_IN according to the following rule:

Output of PV_NORM = (output of CRP_IN) *PV_FAC + PV_OFF

PV_FAC has a default of 1 and PV_OFF a default of 0.

#### Forming the error signal

The difference between the setpoint and process value is the error signal. To suppress a minor sustained oscillation due to manipulated variable quantization (e.g. with a pulse width modulation with PULSEGEN), the error signal is applied to a dead band (DEADBAND). With DEADB_W = 0, the dead band is switched off.

#### PID Algorithm

The PID algorithm operates as a position algorithm. The proportional, integral (INT), and differential (DIF) actions are connected in parallel and can be activated or deactivated individually. This allows P, PI, PD, and PID controllers to be configured. Pure I controllers are also possible.

#### Manual value processing

It is possible to switch over between manual and automatic mode. In manual mode, the manipulated variable is corrected to a manually selected value.

The integral action (INT) is set internally to LMN - LMN_P - DISV and the derivative action (DIF) is set to 0 and synchronized internally. Changeover to automatic mode is therefore bumpless.

#### Manipulated value processing

You can use the LMNLIMIT function to limit the manipulated value to selected values. Alarm bits indicate when a limit is exceeded by the input variable.

The LMN_NORM function normalizes the output of LMNLIMIT according to the following rule:

LMN = (output of LMNLIMIT) * LMN_FAC + LMN_OFF

LMN_FAC has a default of 1 and LMN_OFF a default of 0.

The manipulated value is also available in I/O format. The CRP_OUT function converts the LMN floating-point value to a I/O value according to the following rule:

LMN_PER = LMN * 27648 / 100

#### Feedforward control

A disturbance variable can be added at the DISV input.

---

**See also**

[Description CONT_C (S7-300, S7-400)](#description-cont_c-s7-300-s7-400)
  
[CONT_C block diagram (S7-300, S7-400)](#cont_c-block-diagram-s7-300-s7-400)
  
[Input parameter CONT_C (S7-300, S7-400)](#input-parameter-cont_c-s7-300-s7-400)
  
[Output parameters CONT_C (S7-300, S7-400)](#output-parameters-cont_c-s7-300-s7-400)
  
[Differences compared to CONT_C S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_c-s7-300400-s7-1500)

### CONT_C block diagram (S7-300, S7-400)

![Figure](images/166087191819_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Description CONT_C (S7-300, S7-400)](#description-cont_c-s7-300-s7-400)
  
[How CONT_C works (S7-300, S7-400)](#how-cont_c-works-s7-300-s7-400)
  
[Input parameter CONT_C (S7-300, S7-400)](#input-parameter-cont_c-s7-300-s7-400)
  
[Output parameters CONT_C (S7-300, S7-400)](#output-parameters-cont_c-s7-300-s7-400)
  
[Differences compared to CONT_C S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_c-s7-300400-s7-1500)

### Input parameter CONT_C (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| COM_RST | BOOL | FALSE | The instruction has an initialization routine that is  processed when the "Restart" input is set. |
| MAN_ON | BOOL | TRUE | If the input "Enable manual mode" is set then the control loop is interrupted. A manual value  is set as the manipulated value. |
| PVPER_ON | BOOL | FALSE | If the process value is to be read in from the I/Os, the PV_PER input must be interconnected with the I/Os and the "Enable process value I/Os" input must be set. |
| P_SEL | BOOL | TRUE | The PID actions can be switched on and off individually in the PID algorithm. P-action is on when the "Enable P-action" input is set. |
| I_SEL | BOOL | TRUE | The PID actions can be switched on and off individually in the PID algorithm. I action is on when the input  "I-action on" is set. |
| INT_HOLD | BOOL | FALSE | The output of the integral action can be frozen. For this the input "I-action hold" must be set. |
| I_ITL_ON | BOOL | FALSE | The output of the integral action can be set at the I_ITLVAL input. For this the input "Set I-action" must be set. |
| D_SEL | BOOL | FALSE | The PID actions can be switched on and off individually in the PID algorithm. D-action is on when the  input "Enable D-action" is set. |
| CYCLE | TIME | T#1s | The time between block calls must be constant. The "Sampling time" input specifies the  time between block calls.  CYCLE &gt;= 1ms |
| SP_INT | REAL | 0.0 | The input "Internal setpoint" is used to specify a setpoint.  Permissible are values from -100 to 100 % or a physical variable 1). |
| PV_IN | REAL | 0.0 | At the "Process value input" you can assign parameters to a commissioning value or you can interconnect an external process value in floating-point format.   Permissible are values from -100 to 100 % or a physical variable 1). |
| PV_PER | WORD | W#16#0000 | The process value in I/O format is interconnected with the controller at the "Process value I/0" input. |
| MAN | REAL | 0.0 | The "Manual value" input is used to set a  manual value using the operator interface  functions.  Permissible are values from -100 to 100 % or a physical variable 2). |
| GAIN | REAL | 2.0 | The "Proportional gain" input specifies controller amplification. |
| TI | TIME | T#20s | The "Integration time" input determines the time  response of the integral action.  TI &gt;= CYCLE |
| TD | TIME | T#10s | The "Derivative action time" input determines the time  response of the derivative action.  TD &gt;= CYCLE |
| TM_LAG | TIME | T#2s | Time lag of the D-action  The algorithm of the D-action contains a delay for which parameters can be assigned at the input "Time lag of the D-action".  TM_LAG &gt;= CYCLE/2 |
| DEADB_W | REAL | 0.0 | A dead band is applied to the system deviation. The "Dead band width" input determines the size of the dead band.  DEADB_W &gt;= 0.0 (%) or a physical variable 1) |
| LMN_HLM | REAL | 100.0 | The manipulated value is always restricted to a high limit and low limit. The "High limit of manipulated value" input specifies the high limit.   Permissible are real values starting at LMN_LLM (%) or a physical variable 2). |
| LMN_LLM | REAL | 0.0 | The manipulated value is always restricted to a high limit and low limit. The "Low limit of manipulated value" input specifies the low limit.  Permissible are real values up to LMN_HLM (%) or a physical variable 2). |
| PV_FAC | REAL | 1.0 | The "Process value factor" input is multiplied by the process value. The input is used to scale the process value range. |
| PV_OFF | REAL | 0.0 | The input "Process value offset" is added to the process value. The input is used to scale the process value range. |
| LMN_FAC | REAL | 1.0 | The "Manipulated value factor" input is multiplied with the manipulated value. The input is used to scale the manipulated value range. |
| LMN_OFF | REAL | 0.0 | The input "Manipulated value offset" is added to the process value. The input is used to scale the manipulated value range. |
| I_ITLVAL | REAL | 0.0 | The output of the integral action can be set at the I_ITL_ON input. The initialization value is indicated at the input "Initialization value of the integral-action."  Permissible are values of -100.0 to 100.0 (%) or a physical variable 2). |
| DISV | REAL | 0.0 | For feedforward control, the disturbance variable is interconnected to the "Disturbance variable" input.  Permissible are values of -100.0 to 100.0 (%) or a physical variable 2). |

1) Parameters in the setpoint and process value branches with the same unit

2) Parameters in the manipulated value branch with the same unit

---

**See also**

[Description CONT_C (S7-300, S7-400)](#description-cont_c-s7-300-s7-400)
  
[How CONT_C works (S7-300, S7-400)](#how-cont_c-works-s7-300-s7-400)
  
[CONT_C block diagram (S7-300, S7-400)](#cont_c-block-diagram-s7-300-s7-400)
  
[Output parameters CONT_C (S7-300, S7-400)](#output-parameters-cont_c-s7-300-s7-400)
  
[Differences compared to CONT_C S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_c-s7-300400-s7-1500)

### Output parameters CONT_C (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| LMN | REAL | 0.0 | The effective "Manipulated value" is output in  floating point format at the "Manipulated  value" output. |
| LMN_PER | WORD | W#16#0000 | The manipulated value in I/O format is interconnected on the input "Manipulated value I/O" with the controller. |
| QLMN_HLM | BOOL | FALSE | The manipulated value is always restricted to a high limit and low limit. The output "High  limit of manipulated value reached"  indicates that the high limit has been  reached. |
| QLMN_LLM | BOOL | FALSE | The manipulated value is always restricted to a high limit and low limit. The output "Low  limit of manipulated value reached"  indicates that the low limit has been  reached. |
| LMN_P | REAL | 0.0 | The "P-action" output contains the proportional action of the manipulated variable. |
| LMN_I | REAL | 0.0 | The "I-action" output contains the integral action of the manipulated variable. |
| LMN_D | REAL | 0.0 | The "D-action" output contains the derivative action of the manipulated variable. |
| PV | REAL | 0.0 | The effective process value is output at the "Process value" output. |
| ER | REAL | 0.0 | The effective system deviation is output at the "Error signal" output. |

---

**See also**

[Description CONT_C (S7-300, S7-400)](#description-cont_c-s7-300-s7-400)
  
[How CONT_C works (S7-300, S7-400)](#how-cont_c-works-s7-300-s7-400)
  
[CONT_C block diagram (S7-300, S7-400)](#cont_c-block-diagram-s7-300-s7-400)
  
[Input parameter CONT_C (S7-300, S7-400)](#input-parameter-cont_c-s7-300-s7-400)
  
[Differences compared to CONT_C S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_c-s7-300400-s7-1500)

## CONT_S (S7-300, S7-400)

This section contains information on the following topics:

- [Description CONT_S (S7-300, S7-400)](#description-cont_s-s7-300-s7-400)
- [Mode of operation CONT_S (S7-300, S7-400)](#mode-of-operation-cont_s-s7-300-s7-400)
- [Block diagram CONT_S (S7-300, S7-400)](#block-diagram-cont_s-s7-300-s7-400)
- [Input parameters CONT_S (S7-300, S7-400)](#input-parameters-cont_s-s7-300-s7-400)
- [Output parameters CONT_S (S7-300, S7-400)](#output-parameters-cont_s-s7-300-s7-400)

### Description CONT_S (S7-300, S7-400)

The CONT_S instruction is used on SIMATIC S7 automation systems to control technical processes with binary output value output signals for actuators with integrating behavior. During parameter assignment, you can activate or deactivate sub-functions of the PI step controller to adapt the controller to the controlled system. In addition to the functions in the process value branch, the instruction implements a complete proportional-plus-integral-action controller with binary output value output and the option of manually influencing the value of the output value. The step controller operates without a position feedback signal.

#### Application

You can use the controller as a PI fixed setpoint controller or in secondary control loops in cascade, blending or ratio controllers, however you cannot use it as the primary controller. The functions of the controller are based on the PI control algorithm of the sampling controller supplemented by the functions for generating the binary output signal from the analog actuating signal.

#### Call

The CONT_S instruction has an initialization routine that is run through when input parameter COM_RST = TRUE is set. All the signal outputs are set to zero. COM_RST = FALSE has to be set after the initialization routine has been completed.

The calculation of the values in the control blocks is only correct if the block is called at regular intervals. You should therefore call the control blocks in a cyclic interrupt OB (OB 30 to OB 38). Enter the sampling time in the CYCLE parameter.

#### Error information

The error message word RET_VAL is not evaluated by the block.

---

**See also**

[Mode of operation CONT_S (S7-300, S7-400)](#mode-of-operation-cont_s-s7-300-s7-400)
  
[Input parameters CONT_S (S7-300, S7-400)](#input-parameters-cont_s-s7-300-s7-400)
  
[Output parameters CONT_S (S7-300, S7-400)](#output-parameters-cont_s-s7-300-s7-400)
  
[Block diagram CONT_S (S7-300, S7-400)](#block-diagram-cont_s-s7-300-s7-400)
  
[Differences compared to CONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_s-s7-300400-s7-1500)

### Mode of operation CONT_S (S7-300, S7-400)

#### Setpoint branch

The setpoint is entered in floating-point format at the SP_INT input.

#### Process value branch

The process value can be input in I/O or floating-point format. The function CRP_IN converts the I/O value PV_PER to a floating-point format -100 to +100 % in accordance with the following rule:

Output of CRP_IN = PV_PER * 100 / 27648

The PV_NORM function normalizes the output of CRP_IN according to the following rule:

Output of PV_NORM = (output of CRP_IN) * PV_FAC + PV_OFF

PV_FAC has a default of 1 and PV_OFF a default of 0.

#### Forming the error signal

The difference between the setpoint and process value is the error signal. To suppress a small constant oscillation due to the manipulated variable quantization (for example, due to a limited resolution of the manipulated value by the control valve), a dead band is applied to the error signal (DEADBAND). With DEADB_W = 0, the dead band is switched off.

#### PI step algorithm

The instruction operates without position feedback. The I-action of the PI algorithm and the assumed position feedback signal are calculated in **one** integral action (INT) and compared with the remaining P-action as a feedback value. The difference is applied to a three-step element (THREE_ST) and a pulse shaper (PULSEOUT) that generates the pulses for the control valve. The switching frequency of the controller can be reduced by adapting the response threshold of the three-step element.

#### Feedforward control

A disturbance variable can be added at the DISV input.

---

**See also**

[Description CONT_S (S7-300, S7-400)](#description-cont_s-s7-300-s7-400)
  
[Input parameters CONT_S (S7-300, S7-400)](#input-parameters-cont_s-s7-300-s7-400)
  
[Output parameters CONT_S (S7-300, S7-400)](#output-parameters-cont_s-s7-300-s7-400)
  
[Block diagram CONT_S (S7-300, S7-400)](#block-diagram-cont_s-s7-300-s7-400)
  
[Differences compared to CONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_s-s7-300400-s7-1500)

### Block diagram CONT_S (S7-300, S7-400)

![Figure](images/166087197451_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Description CONT_S (S7-300, S7-400)](#description-cont_s-s7-300-s7-400)
  
[Mode of operation CONT_S (S7-300, S7-400)](#mode-of-operation-cont_s-s7-300-s7-400)
  
[Input parameters CONT_S (S7-300, S7-400)](#input-parameters-cont_s-s7-300-s7-400)
  
[Output parameters CONT_S (S7-300, S7-400)](#output-parameters-cont_s-s7-300-s7-400)
  
[Differences compared to CONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_s-s7-300400-s7-1500)

### Input parameters CONT_S (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| COM_RST | BOOL | FALSE | The block has an initialization routine that is  processed when the "Restart" input is set. |
| LMNR_HS | BOOL | FALSE | The signal "Control valve at high endstop" is interconnected at the input "High endstop signal of position feedback". LMNR_HS=TRUE means: The  control valve is at high endstop. |
| LMNR_LS | BOOL | FALSE | The signal "Control valve at low endstop" is interconnected on the input "Low endstop signal of position feedback". LMNR_LS=TRUE means The  control valve is at low endstop. |
| LMNS_ON | BOOL | FALSE | Manipulated value signal processing is switched to manual mode at the "Enable manual mode of manipulated signal". |
| LMNUP | BOOL | FALSE | The output signal QLMNUP is operated in manual mode of the manipulated value signals at the input "Manipulated value signal up". |
| LMNDN | BOOL | FALSE | The output signal QLMNDN is operated in manual mode of the manipulated value signals at the input "Manipulated value signal down" |
| PVPER_ON | BOOL | FALSE | If the process value is to be read from the I/O then the input PV_PER must be interconnected with the I/O and the input "Enable process value I/O" must be set. |
| CYCLE | TIME | T#1s | The time between block calls must be constant. The "Sampling time" input specifies the  time between block calls.   CYCLE &gt;= 1ms |
| SP_INT | REAL | 0.0 | The input "Internal setpoint" is used to specify a setpoint.  Permissible are values from -100 to 100 % or a physical variable <sup>1)</sup>. |
| PV_IN | REAL | 0.0 | At the "Process value input" you can assign parameters to a commissioning value or you can interconnect an external process value in floating-point format.   Permissible are values from -100 to 100 % or a physical variable <sup>1)</sup>. |
| PV_PER | WORD | W#16#0000 | The process value in I/O format is interconnected with the controller at the "Process value I/O" input. |
| GAIN | REAL | 2.0 | The "Proportional gain" input specifies controller amplification. |
| TI | TIME | T#20s | The "Integration time" input determines the time  response of the integral action.  TI &gt;= CYCLE |
| DEADB_W | REAL | 1.0 | A dead band is applied to the system deviation. The "Dead band width" input determines the size of the dead band.   Permissible are values from 0 to 100 % or a physical variable <sup>1)</sup>. |
| PV_FAC | REAL | 1.0 | The "Process value factor" input is multiplied by the process value. The input is used to scale the process value range. |
| PV_OFF | REAL | 0.0 | The input "Process value offset" is added to the process value. The input is used to scale the process value range. |
| PULSE_TM | TIME | T#3s | You can assign a minimum pulse time at the parameter "Minimum pulse time".  PULSE_TM &gt;= CYCLE |
| BREAK_TM | TIME | T#3s | You can assign a minimum break time at the parameter "Minimum break time".  BREAK_TM &gt;= CYCLE |
| MTR_TM | TIME | T#30s | The time required by the actuator to move from  limit stop to limit stop is entered at the "Motor  actuating time" parameter.  MTR_TM &gt;= CYCLE |
| DISV | REAL | 0.0 | For feedforward control, the disturbance variable is interconnected to the "Disturbance variable" input.  Permissible are values from -100 to 100 % or a physical variable <sup>2)</sup>. |

<sup>1)</sup> Parameters in setpoint and process value branches with identical unit

<sup>2)</sup> Parameters in the manipulated value branch with same unit

---

**See also**

[Description CONT_S (S7-300, S7-400)](#description-cont_s-s7-300-s7-400)
  
[Mode of operation CONT_S (S7-300, S7-400)](#mode-of-operation-cont_s-s7-300-s7-400)
  
[Output parameters CONT_S (S7-300, S7-400)](#output-parameters-cont_s-s7-300-s7-400)
  
[Block diagram CONT_S (S7-300, S7-400)](#block-diagram-cont_s-s7-300-s7-400)
  
[Differences compared to CONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_s-s7-300400-s7-1500)

### Output parameters CONT_S (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| QLMNUP | BOOL | FALSE | If the output "Manipulated value signal up" is set then the control valve should be open. |
| QLMNDN | BOOL | FALSE | If the output "Manipulated value signal down" is set then the control valve should be closed. |
| PV | REAL | 0.0 | The effective process value is output at the "Process value" output. |
| ER | REAL | 0.0 | The effective system deviation is output at the "Error signal" output. |

---

**See also**

[Description CONT_S (S7-300, S7-400)](#description-cont_s-s7-300-s7-400)
  
[Mode of operation CONT_S (S7-300, S7-400)](#mode-of-operation-cont_s-s7-300-s7-400)
  
[Input parameters CONT_S (S7-300, S7-400)](#input-parameters-cont_s-s7-300-s7-400)
  
[Block diagram CONT_S (S7-300, S7-400)](#block-diagram-cont_s-s7-300-s7-400)
  
[Differences compared to CONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-cont_s-s7-300400-s7-1500)

## PULSEGEN (S7-300, S7-400)

This section contains information on the following topics:

- [Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
- [Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
- [Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
- [Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
- [Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
- [Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
- [Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)

### Description PULSEGEN (S7-300, S7-400)

The instruction PULSEGEN serves as the structure of a PID controller with impulse output for proportional actuators. PULSEGEN transforms the input value INV (= LMN of the PID controller) through modulation of the impulse width in an impulse sequence with a constant period duration, which corresponds with the cycle time with which the input value is updated.

#### Application

You can use the PULSEGEN instruction to configure two- or three-step PID controllers with pulse width modulation. The function is normally used in conjunction with the continuous controller CONT_C.

![Application](images/166087203083_DV_resource.Stream@PNG-de-DE.png)

#### Call

The PULSEGEN instruction has an initialization routine that is run through when input parameter COM_RST = TRUE is set. All the signal outputs are set to zero. COM_RST = FALSE has to be set after the initialization routine has been completed.

The calculation of the values in the control blocks is only correct if the block is called at regular intervals. You should therefore call the control blocks in a cyclic interrupt OB (OB 30 to OB 38). Enter the sampling time in the CYCLE parameter.

#### Responses in the event of an error

The error message word RET_VAL is not evaluated by the block.

---

**See also**

[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

### Mode of operation PULSEGEN (S7-300, S7-400)

#### Impulse width modulation

The duration of a pulse per period duration is proportional to the input variable. The cycle assigned via PER_TM is not identical to the processing cycle of the PULSEGEN instruction. Rather, a PER_TM cycle is made up of several processing cycles of the PULSEGEN instruction, whereby the number of PULSEGEN calls per PER_TM cycle determines the accuracy of the pulse width.

![Impulse width modulation](images/166087208715_DV_resource.Stream@PNG-en-US.png)

An input variable of 30% and 10 PULSEGEN calls per PER_TM mean the following:

- "One" at the QPOS_P output for the first three calls of PULSEGEN (30% of 10 calls)
- "Zero" at the QPOS_P output for seven further calls of PULSEGEN (70% of 10 calls)

#### Block diagram

![Block diagram](images/166087214219_DV_resource.Stream@PNG-de-DE.png)

#### Accuracy of the manipulated value

With a "Sampling ratio" of 1:10 (CONT_C calls to PULSEGEN calls) the accuracy of the manipulated value in this example is restricted to 10%, in other words, set input values INV can only be simulated by a pulse duration at the QPOS_P output in steps of 10 %.

The accuracy is increased as the number of PULSEGEN calls per CONT_C call is increased.

If PULSEGEN is called, for example, 100 times more often than CONT_C, a resolution of 1 % of the manipulated value range is achieved.

> **Note**
>
> The reduction ratio of the call frequency must be programmed by the user.

#### Automatic synchronization

It is possible to automatically synchronize the pulse output with the instruction that updates the input variable INV (e.g. CONT_C). This ensures that a change in the input variable is output as quickly as possible as a pulse.

The pulse shaper evaluates the input value INV at intervals corresponding to the period duration PER_TM and converts the value into a pulse signal of corresponding length.

Since, however, INV is usually calculated in a slower cyclic interrupt class, the pulse shaper should start the conversion of the discrete value into a pulse signal as soon as possible after the updating of INV.

To allow this, the block can synchronize the start of the period using the following procedure:

If INV changes and if the block call is not in the first or last two call cycles of a period, a synchronization is performed. The pulse duration is recalculated and in the next cycle is output with a new period.

![Automatic synchronization](images/166087219723_DV_resource.Stream@PNG-en-US.png)

The automatic synchronization is switched off, if SYN_ON = FALSE.

> **Note**
>
> The start of a new period and subsequent synchronization usually leads to a certain imprecision when the old value of INV (i.e. of LMN) is mapped to the pulse signal.

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

### Mode of operation PULSEGEN (S7-300, S7-400)

#### Modes

Depending on the parameters assigned to the pulse shaper, PID controllers with a three-step output or with a bipolar or unipolar two-step output can be configured. The following table illustrates the setting of the switch combinations for the possible modes.

| Mode | MAN_ON | STEP3_ON | ST2BI_ON |
| --- | --- | --- | --- |
| Three-step control | FALSE | TRUE | Any |
| Two-step control with bi-polar   Manipulating range (-100 % to 100 %) | FALSE | FALSE | TRUE |
| Two-step control with unipolar   Manipulating range (0 % to 100 %) | FALSE | FALSE | FALSE |
| Manual mode | TRUE | Any | Any |

#### Manual mode in two/three-step control

In the manual mode (MAN_ON = TRUE), the binary outputs of the three-step or two-step controller can be set using the signals POS_P_ON and NEG_P_ON regardless of INV.

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

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

### Three-step control (S7-300, S7-400)

#### Three-step control

In "Three-step control" mode, it is possible to generate three statuses of the actuating signal. For this, the status values of the binary output signals QPOS_P and QNEG_P are assigned to the respective operating statuses of the actuator. The table shows the example of a temperature control:

| Output signals | Heat | Off | Cool |
| --- | --- | --- | --- |
| QPOS_P | TRUE | FALSE | FALSE |
| QNEG_P | FALSE | FALSE | TRUE |

The pulse duration is calculated from the input variable via a characteristic curve. The form of the characteristic curve is defined by the minimum pulse duration or minimum interval and the ratio factor. The normal value for the ratio factor is 1.

The "doglegs" in the curves are caused by the minimum pulse duration or minimum interval.

**Minimum pulse duration or minimum interval**

A correctly assigned minimum pulse duration or minimum interval P_B_TM can prevent short on/off times, which reduce the working life of switching elements and actuators. Small absolute values of input variable LMN that could otherwise generate a pulse duration shorter than P_B_TM are suppressed. Large input values that would generate a pulse duration longer than PER_TM - P_B_TM are set to 100% or -100%.

The duration of positive or negative pulses is calculated by multiplying the input variable (in %) by the period duration:

Pulse duration = INV / 100 * PER_TM

The following figure shows a symmetrical characteristic curve of the three-step controller (ratio factor = 1).

![Three-step control](images/166087225227_DV_resource.Stream@PNG-en-US.png)

#### Asymmetrical three-step control

Using the ratio factor RATIOFAC, the ratio of the duration of positive to negative pulses can be changed. In a thermal process, for example, this would allow different system time constants for heating and cooling.

**Ratio factor &lt; 1**

The pulse duration at the negative pulse output, calculated by multiplying the input variable by the period duration, is multiplied by the ratio factor.

Positive pulse duration = INV /100 * PER_TM

Negative pulse duration = INV / 100 * PER_TM * RATIOFAC

The following figure shows the asymmetrical characteristic curve of the three-step controller (ratio factor = 0.5):

![Asymmetrical three-step control](images/166087230731_DV_resource.Stream@PNG-en-US.png)

**Ratio factor &gt; 1**

The pulse duration at the positive pulse output, calculated by multiplying the input variable by the period duration, is divided by the ratio factor.

Positive pulse duration = INV / 100 * PER_TM / RATIOFAC

Negative pulse duration = INV / 100 * PER_TM

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

### Two-step control (S7-300, S7-400)

In two-step control, only the positive pulse output QPOS_P of PULSEGEN is connected to the on/off actuator. Depending on the manipulated value range used, the two-step controller has a bipolar or a unipolar manipulated value range.

**Two-step control with bipolar manipulated variable range  (-100% to 100%)**

![Figure](images/166087236235_DV_resource.Stream@PNG-en-US.png)

**Two-step control with unipolar manipulated variable range  (0% to 100%)**

![Figure](images/166087292939_DV_resource.Stream@PNG-en-US.png)

The negated output signal is available at QNEG_P if the connection of the two-step controller in the control loop requires a logically inverted binary signal for the actuating pulses.

| Pulse | Actuator On | Actuator Off |
| --- | --- | --- |
| QPOS_P | TRUE | FALSE |
| QNEG_P | FALSE | TRUE |

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

### Input parameters PULSEGEN (S7-300, S7-400)

The values of the input parameters are not limited in the block. There is no parameter check.

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| INV | REAL | 0.0 | At the input parameter "Input variable" an analog manipulated variable is connected.  Values from -100 to 100 % are permitted. |
| PER_TM | TIME | T#1s | At the parameter "Period duration" the constant period duration of the pulse width modulation is entered. This corresponds to the  sampling time of the controller. The ratio  between the sampling time of the pulse  shaper and the sampling time of the  controller determines the accuracy of the  pulse width modulation.  PER_TM &gt;=20*CYCLE |
| P_B_TM | TIME | T#50 ms | You can assign a minimum pulse/break time at the parameter "Minimum pulse/break time".  P_B_TM &gt;= CYCLE |
| RATIOFAC | REAL | 1.0 | Using the "Ratio factor" input parameter the ratio of the duration of positive to negative pulses can be changed. In a thermal  process, this would, for example, allow  different time constants for heating and  cooling to be compensated (for example, in  a process with electrical heating and water  cooling).  Values from 0.1 to 10.0 are permitted. |
| STEP3_ON | BOOL | TRUE | At the input parameter "Enable three-step control" the appropriate mode is activated. In three-step control  both output signals are active. |
| ST2BI_ON | BOOL | FALSE | At the input parameter "Enable two-step control for bipolar manipulated value range" you can select from the modes "Two-step control for bipolar manipulated value range" and "Two-step control for unipolar manipulated value range". STEP3_ON = FALSE is required. |
| MAN_ON | BOOL | FALSE | Setting the input parameter "Enable manual mode" allows the output signals to be set manually. |
| POS_P_ON | BOOL | FALSE | For manual mode three-step control, the output signal QPOS_P can be operated on the input parameter "Positive pulse on". In  manual mode with two-step control, QNEG_P is always set inversely to  QPOS_P. |
| NEG_P_ON | BOOL | FALSE | For manual mode three-step control, the output signal QNEG_P can be operated on the input parameter "Negative pulse on". In  manual mode with two-step control, QNEG_P is always set inversely to  QPOS_P. |
| SYN_ON | BOOL | TRUE | By setting the input parameter  "Enable synchronization", it is possible to  synchronize the pulse output automatically with the block  that updates the input variable INV. This ensures that a change in the input variable is output as quickly as possible as a pulse. |
| COM_RST | BOOL | FALSE | The block has an initialization routine that is  processed when the input "Restart" is set. |
| CYCLE | TIME | T#10ms | The time between block calls must be constant. The "Sampling time" input specifies the  time between block calls.  CYCLE &gt;= 1ms |

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

### Output parameter PULSEGEN (S7-300, S7-400)

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| QPOS_P | BOOL | FALSE | The output parameter "Output signal positive pulse" is set if a pulse will be output. In three-step control, this is  always the positive pulse. In two-step control, the QNEG_P  is always set inversely to QPOS_P. |
| QNEG_P | BOOL | FALSE | The output parameter "Output signal negative pulse" is set if a pulse will be output. In three-step control, this is  always the negative pulse. In two-step control, QNEG_P  is always set inversely to QPOS_P. |

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Differences compared to PULSEGEN S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-pulsegen-s7-300400-s7-1500)

## TCONT_CP (S7-300, S7-400)

This section contains information on the following topics:

- [Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
- [Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
- [Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
- [Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
- [Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
- [Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
- [In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
- [Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
- [Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
- [Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Description TCONT_CP (S7-300, S7-400)

The instruction TCONT_CP is used to control temperature processes with continuous or pulsed control signals. The controller functionality is based on the PID control algorithm with additional functions for temperature processes. To improve the control response with temperature processes, the block includes a control zone and reduction of the proportional component if there is a setpoint step change.

The instruction can set the PI/PID parameters itself using the controller optimization function.

#### Application

The controller controls one actuator; in other words, with one controller you can either heat or cool but not both. If you use the block for cooling, GAIN must be assigned a negative value. This inversion of the controller means that if the temperature rises, for example, the manipulated variable LMN and with it the cooling action is increased.

#### Call

The instruction TCONT_CP must be called with a constant bus cycle time. To achieve this, use a cyclic interrupt priority class (for example, OB35 for an S7-300).

The TCONT_CP instruction has an initialization routine that is run through when input parameter COM_RST = TRUE is set. During initialization, the integral action is set to the initialization value I_ITVAL. All the signal outputs are set to zero. Following execution of the initialization routine, the block sets COM_RST back to FALSE. If you require initialization when the CPU restarts, call the block in OB100 with COM_RST = TRUE.

---

**See also**

[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Mode of operation TCONT_CP (S7-300, S7-400)

#### Setpoint branch

The setpoint is entered at input SP_INT in floating-point format as a physical value or percentage. The setpoint and process value used to form the control deviation must have the same unit.

#### Process value options (PVPER_ON)

Depending on PVPER_ON, the process value can be read in, in the I/O or floating-point format.

| PVPER_ON | Process Value Input |
| --- | --- |
| TRUE | The process value is read in via the analog I/Os (PIW xxx) at input PV_PER. |
| FALSE | The process value is acquired in floating-point format at input PV_IN. |

#### Process value format conversion CRP_IN (PER_MODE)

The CRP_IN function converts the I/O value PV_PER to floating-point format depending on the PER_MODE switch according to the following rules:

| PER_MODE | Output of CRP_IN | Analog Input Type | Unit |
| --- | --- | --- | --- |
| 0 | PV_PER * 0.1 | Thermoelements; PT100/NI100; standard | °C;°F |
| 1 | PV_PER * 0.01 | PT100/NI100; climate; | °C;°F |
| 2 | PV_PER * 100/27648 | Voltage/current | % |

#### Process value scaling PV_NORM (PF_FAC, PV_OFFS)

The PV_NORM function calculates the output of CRP_IN according to the following rule:

"Output of PV_NORM" = "Output of CRP_IN" * PV_FAC + PV_OFFS

It can be used for the following purposes:

- Process value adjustment with PV_FAC as process value factor and PV_OFFS as process value offset.
- Scaling of temperature to percentage

  You want to enter the setpoint as a percentage and must now convert the measured temperature value to a percentage.
- Scaling of percentage to temperature

  You want to enter the setpoint in the physical temperature unit and must now convert the measured voltage/current value to a temperature.

Calculation of the parameters:

- PV_FAC = range of PV_NORM/range of CRP_IN;
- PV_OFFS = LL (PV_NORM) - PV_FAC * LL(CRP_IN);

  where LL: Low limit

The scaling is switched off with the default values (PV_FAC = 1.0 and PV_OFFS = 0.0). The effective process value is output at the PV output.

> **Note**
>
> With pulse control, the process value must be transferred to the block in the fast pulse call (reason: mean value filtering). Otherwise, the control quality can deteriorate.

#### Example of Process Value Scaling

If you want to enter the setpoint as a percentage, and you have a temperature range of -20 to 85 °C applied to , CRP_IN you must normalize the temperature range as a percentage.

The diagram below shows an example of adapting the temperature range -20 to 85 °C to an internal scale of 0 to 100 %:

![Example of Process Value Scaling](images/166087298443_DV_resource.Stream@PNG-de-DE.png)

#### Forming the control deviation

The difference between the setpoint and process value is the control deviation before the dead zone.

The setpoint and process value must exist in the same unit.

#### Dead zone (DEADB_W)

To suppress a minor sustained oscillation due to the manipulated variable quantization (for example, in pulse width modulation with PULSEGEN) a dead zone is applied to the (DEADBAND) control deviation. With DEADB_W = 0.0, the dead zone is disabled. The effective control deviation is indicated by the ER parameter.

![Dead zone (DEADB_W)](images/166087355147_DV_resource.Stream@PNG-de-DE.png)

#### PID algorithm

The following figure shows the block diagram of the PID algorithm.

![PID algorithm](images/166087360779_DV_resource.Stream@PNG-de-DE.png)

![PID algorithm](images/166087401611_DV_resource.Stream@PNG-de-DE.png) Parameter configuration interface

![PID algorithm](images/166087456395_DV_resource.Stream@PNG-de-DE.png) Instruction call interface

#### PID algorithm (GAIN, TI, TD, D_F)

The PID algorithm operates as a position algorithm. The proportional, integral (INT), and derivative (DIF) actions are connected in parallel and can be activated or deactivated individually. This allows P, PI, PD, and PID controllers to be configured.

Controller tuning supports PI and PID controllers. Controller inversion is implemented using a negative GAIN (cooling controller).

If you set TI and TD to 0.0, you obtain a pure P controller at the operating point.

The step response in the time range is:

![PID algorithm (GAIN, TI, TD, D_F)](images/166087366283_DV_resource.Stream@PNG-de-DE.png)

Where:

LMN_Sum(t) the manipulated variable in the controller's automatic mode

ER (0) is the step height of the normalized control deviation

GAIN is the controller gain

TI is the integration time

TD is the derivative action time

D_F is the derivative factor

![PID algorithm (GAIN, TI, TD, D_F)](images/166087384715_DV_resource.Stream@PNG-de-DE.png)

#### Integral action (TI, I_ITL_ON, I_ITLVAL)

In manual mode, it is corrected as follows: LMN_I = LMN - LMN_P - DISV.

If the output value is limited, the integral action is halted. If the control deviation moves the integral action back in the direction of the output range, the integral action is enabled again.

The integral action is also modified by the following measures:

- The integral action of the controller is deactivated by TI = 0.0
- Weakening of the proportional action when setpoint changes occur
- Control zone
- The output value limits can be modified online

#### Weakening of the proportional action when setpoint changes occur (PFAC_SP)

To prevent overshoot, you can weaken the proportional action using the "Proportional factor for setpoint changes" parameter (PFAC_SP). Using PFAC_SP, you can select continuously between 0.0 and 1.0 to decide the effect of the proportional action when the setpoint changes:

- PFAC_SP = 1.0: Proportional action for setpoint change is fully effective
- PFAC_SP = 0.0: Proportional action for setpoint change is not effective

The weakening of the proportional action is achieved by compensating the integral action.

#### Derivative action (TD, D_F)

- The derivative action of the controller is deactivated by TD = 0.0
- If the derivative action is active, the following relationship should apply:

  TD = 0.5 * CYCLE * D_F

#### Parameter Settings of a P or PD Controller with Operating Point

In the user interface, deactivate the integral action (TI = 0.0) and possibly also the derivative action (TD = 0.0). Then make the following parameter settings:

- I_ITL_ON = TRUE
- I_ITLVAL = operating point;

#### Feedforward control (DISV)

A disturbance variable can be added at the DISV input.

#### Calculating the output value

The diagram below is the block diagram of the output value calculation:

![Calculating the output value](images/166087390219_DV_resource.Stream@PNG-de-DE.png)

![Calculating the output value](images/166087401611_DV_resource.Stream@PNG-de-DE.png) Parameter configuration interface

![Calculating the output value](images/166087456395_DV_resource.Stream@PNG-de-DE.png) Instruction call interface

![Calculating the output value](images/166087459979_DV_resource.Stream@PNG-de-DE.png) Parameter configuration interface, call interface

#### Control zone (CONZ_ON, CON_ZONE)

If CONZ_ON = TRUE, the controller operates with a control zone. This means that the controller operates according to the following algorithm:

- If process value PV exceeds the setpoint SP_INT by more than CON_ZONE, the value LMN_LLM is output as the manipulated variable.
- If the process value PV falls below setpoint SP_INT by more than CON_ZONE, LMN_HLM is output.
- If the process value PV is within the control zone (CON_ZONE), the output value takes its value from the PID algorithm LMN_Sum.

  > **Note**
  >
  > Changing the manipulated variable from LMN_LLM or LMN_HLM to LMN_Sum occurs under compliance of a hysteresis of 20% of the control zone.

  ![Control zone (CONZ_ON, CON_ZONE)](images/166087395723_DV_resource.Stream@PNG-en-US.png)

  > **Note**
  >
  > Before enabling the control zone manually, make sure that the control zone band is not too narrow. If the control zone band is too small, oscillations will occur in the manipulated variable and process value.

#### Advantage of the Control Zone

When the process value enters the control zone, the D-action causes an extremely fast reduction of the manipulated variable. This means that the control zone is only useful when the D-action is activated. Without a control zone, only the reducing proportional action would essentially reduce the manipulated variable. The control zone leads to faster settling without overshoot or undershoot if the output minimum or maximum manipulated variable is a long way from the manipulated variable required for the new operating point.

#### Manual value processing (MAN_ON, MAN)

You can change over between manual and automatic mode. In manual mode, the manipulated variable is corrected to a manually selected value.

The integral action (INT) is set internally to LMN - LMN_P - DISV and the derivative action (DIF) is set to 0 and synchronized internally. Changeover to automatic mode is therefore bumpless.

> **Note**
>
> The MAN_ON parameter has no effect during tuning.

#### Output value limit LMNLIMIT (LMN_HLM, LMN_LLM)

The LMNLIMIT function is used to limit the output value to the limits LMN_HLM and LMN_LLM. If these limits are reached, this is indicated by the message bits QLMN_HLM and QLMN_LLM.

If the output value is limited, the integral action is halted. If the control deviation moves the integral action back in the direction of the output range, the integral action is enabled again.

#### Changing the Manipulated Value Limits Online

If the range of the output value is reduced and the new unlimited value of the output value is outside the limits, the integral action and therefore the output value shifts.

The output value is reduced by the same amount as the output value limit changed. If the output value was unlimited prior to the change, it is set exactly to the new limit (described here for the high output value limit).

#### Scaling of output value LMN_NORM (LMN_FAC, LMN_OFFS)

The LMN_NORM function normalizes the output value according to the following rule:

LMN = LmnN * LMN_FAC + LMN_OFFS

It can be used for the following purposes:

- Output value scaling with LMN_FAC as output value factor and LMN_OFFS as output value offset.

The output value is also available in I/O format. The CRP_OUT function converts the LMN floating-point value to an I/O value according to the following rule:

LMN_PER = LMN * 27648/100

The scaling is switched off with the default values (LMN_FAC = 1.0 and LMN_OFFS = 0.0). The effective output value is sent to output LMN.

#### Save controller parameters SAVE_PAR

 If you classify the current controller parameters as utilizable, you can save these before a manual change in structure parameters provided specifically for this in the instance DB of the instruction TCONT_CP. If you optimize the controller, the saved parameters are overwritten by the values that were valid prior to tuning.

PFAC_SP, GAIN, TI, TD, D_F, CONZ_ON and CONZONE are written to the structure PAR_SAVE.

#### Reloading Saved Controller Parameters UNDO_PAR

The last controller parameter settings you saved can be activated for the controller again using this function (in manual mode only).

#### Change between PI and PID parameters LOAD_PID (PID_ON)

Following tuning, the PI and PID parameters are stored in the PI_CON and PID_CON structures. Depending on PID_ON, you can use LOAD_PID in manual mode to write the PI or PID parameters to the effective controller parameters.

| PID parameters PID_ON = TRUE | PI parameters PID_ON = FALSE |
| --- | --- |
| - GAIN = PID_CON.GAIN - TI = PID_CON.TI - TD = PID_CON.TD | - GAIN = PI_CON.GAIN - TI = PI_CON.TI |

> **Note**
>
> The controller parameters are only written back to the controller with UNDO_PAR or LOAD_PID, if the controller gain is not equal to 0:
>
> With LOAD_PID, the parameters are only copied if the corresponding GAIN &lt;&gt; 0 is (either the PI or PID parameters). This strategy takes into account the situation that no tuning has yet been made or that PID parameters are missing. If PID_ON = TRUE and PID.GAIN = FALSE, PID_ON is set to FALSE and the PI parameter is copied.
>
> - D_F, PFAC_SP are preset by the tuning. These can then be modified by the user. LOAD_PID does not change these parameters.
> - With LOAD_PID, the control zone is always recalculated
>
>   (CON_ZONE = 250/GAIN), even if CONZ_ON = FALSE.

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Operating principle of the pulse generator (S7-300, S7-400)

The function PULSEGEN transforms the analog manipulated value LmnN through pulse width module into an impulse sequence with the period duration PER_TM. PULSEGEN is switched on with PULSE_ON = TRUE and is processed in the cycle CYCLE_P.

![Figure](images/166014578571_DV_resource.Stream@PNG-de-DE.png)

A manipulated value of LmnN = 30% and 10 PULSEGEN calls per PER_TM therefore means:

- TRUE at output QPULSE for the first three PULSEGEN calls   
  (30% of 10 calls)
- FALSE at output QPULSE for seven further PULSEGEN calls   
  (70% of 10 calls)

The duration of a pulse per pulse repetition period is proportional to the manipulated variable and is calculated as follows:

Pulse duration = PER_TM * LmnN /100

By suppressing the minimum pulse or break time, the characteristic curve of the conversion develops "knees" in the start and end regions.

The following diagram illustrates two-step control with a unipolar manipulated variable range   
(0% to 100%):

![Figure](images/166087463563_DV_resource.Stream@PNG-en-US.png)

#### Minimum pulse or minimum break time (P_B_TM)

Short on or off times hinder the lifespan of actuators and fine controlling units. These can be avoided by setting a minimum pulse duration or minimum break time P_B_TM.

Small absolute values of input variable LmnN that could otherwise generate a pulse duration shorter than P_B_TM are suppressed.

Large input values that would generate a pulse duration greater than   
PER_TM - P_B_TM are set to 100%. This reduces the dynamic response of pulse generation.

Set values of P_B_TM ≤ 0,1 * PER_TM are recommended for the minimum pulse duration and the minimum break duration.

The "knees" in the curves in the diagram above are caused by the minimum pulse or minimum break times.

The following schematic illustrates the switching response of the pulse output:

![Minimum pulse or minimum break time (P_B_TM)](images/166014584075_DV_resource.Stream@PNG-de-DE.png)

#### Accuracy of pulse generation

The smaller the pulse generator CYCLE_P is compared to the period duration PER_TM, the more precise the pulse width modulation is. To achieve sufficiently accurate control, the following relationship should apply:

CYCLE_P ≤ PER_TM/50

The manipulated value is transformed with a resolution of ≤ 2 % into an impulse.

> **Note**
>
> When calling the controller in the pulse shaper cycle, you must note the following:
>
> Calling the controller in the pulse shaper cycle will cause the process value to be averaged. As a result, at output PV, different values may be at input PV_IN and PV_PER. If you want to track the setpoint value, you must save the process value at input parameter PV_IN at the call times for complete controller processing (QC_ACT = TRUE). For pulse shaper calls occurring between these times, you must supply the input parameters PV_IN and SP_INT with the saved process value.

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Block diagram TCONT_CP (S7-300, S7-400)

![Figure](images/166087469067_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Input parameters TCONT_CP (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| PV_IN | 0.0 | REAL | 0.0 | At the "Process value input" you can assign parameters to a commissioning value or you can interconnect an external process value in floating-point format. The valid values depend on the sensors used. |
| PV_PER | 4.0 | INT | 0 | The process value in I/O format is interconnected with the controller at the "Process value I/O" input. |
| DISV | 6.0 | REAL | 0.0 | For feedforward control, the disturbance variable is interconnected to the "Disturbance variable" input. |
| INT_HPOS | 10.0 | BOOL | FALSE | The output of the integral action can be held in the positive direction. For this, the input INT_HPOS must be set to TRUE. In a cascade control, INT_HPOS of the primary controller is connected to QLMN_HLM of the secondary controller. |
| INT_HNEG | 10.1 | BOOL | FALSE | The output of the integral action can be held in the negative direction. For this, the input INT_HNEG must be set to TRUE. In a cascade control, INT_HNEG of the primary controller is connected to QLMN_LLM of the secondary controller. |
| SELECT | 12.0 | INT | 0 | If the pulse shaper is on, there are several ways of calling the PID algorithm and pulse shaper:  - SELECT = 0: The controller is called in a fast cyclic interrupt priority class and the PID algorithm and pulse shaper are processed. - SELECT = 1: The controller is called in OB1 and only the PID algorithm is processed. - SELECT = 2: The controller is called in a fast cyclic interrupt priority class and only the pulse shaper is processed. - SELECT = 3: The controller is called a slow cyclic interrupt priority class and only the PID algorithm is processed. |

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Output parameters TCONT_CP (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameter | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| PV | 14.0 | REAL | 0.0 | The effective process value is output at the "Process value" output.  The valid values depend on the sensors used. |
| LMN | 18.0 | REAL | 0.0 | The effective "Manipulated value" is output in  floating point format at the "Manipulated  value" output. |
| LMN_PER | 22.0 | INT | 0 | The manipulated value in I/O format is interconnected with the controller on the output "Manipulated value I/O". |
| QPULSE | 24.0 | BOOL | FALSE | The manipulated value is pulse-width-modulated at the QPULSE output. |
| QLMN_HLM | 24.1 | BOOL | FALSE | The manipulated value is always restricted to a high limit and low limit. The output QLMN_HLM signals that the high limit has been reached. |
| QLMN_LLM | 24.2 | BOOL | FALSE | The manipulated value is always restricted to a high limit and low limit. The output QLMN_LLM signals that the low limit has been reached. |
| QC_ACT | 24.3 | BOOL | TRUE | This parameter indicates whether continuous control component will be processed the next time the block is called (relevant only when SELECT has the value 0 or 1). |

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### In/out parameters TCONT_CP (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| CYCLE | 26.0 | REAL | 0.1 s | Sets the sampling time for the PID algorithm. In phase 1, the tuner calculates  the sampling time and enters it in CYCLE.  CYCLE &gt; 0.001 s |
| CYCLE_P | 30.0 | REAL | 0.02 s | At this input, you set the sampling time for the pulse shaper action. In phase 1, the TCONT_CP instruction calculates the sampling time and enters it in CYCLE_P.   CYCLE_P &gt; 0.001 s |
| SP_INT | 34.0 | REAL | 0.0 | The input "Internal setpoint" is used to specify a setpoint.  The valid values depend on the sensors used. |
| MAN | 38.0 | REAL | 0.0 | The "Manual value" input is used to set a manual value. In automatic mode, it tracks the manipulated value. |
| COM_RST | 42.0 | BOOL | FALSE | The block has an initialization routine that is processed when the COM_RST input is set. |
| MAN_ON | 42.1 | BOOL | TRUE | If the input "Enable manual mode" is set then the control loop is interrupted. The manual value MAN is set as manipulated value. |

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Static variables TCONT_CP (S7-300, S7-400)

The names of the following variables apply both to the data block and to access via the Openness API.

| Parameters | Address |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| DEADB_W | 44.0 |  | REAL | 0.0 | A deadband is applied to the control deviation. The "Deadband width" input determines the size of the deadband.  The valid values depend on the sensors used. |
| I_ITLVAL | 48.0 |  | REAL | 0.0 | The output of the integrator can be set at the I_ITL_ON input. The initialization value is applied to the "Initialization value of the I-action" input. During a restart COM_RST = TRUE, the I-action is set to the initialization value.  Values from -100 to 100 % are permitted. |
| LMN_HLM | 52.0 |  | REAL | 100.0 | The output value is always restricted to a high limit and low limit. The "Manipulated value high limit" input specifies the high limit.  LMN_HLM &gt; LMN_LLM |
| LMN_LLM | 56.0 |  | REAL | 0.0 | The output value is always restricted to a high limit and low limit. The "Manipulated value low limit" input specifies the low limit.  LMN_LLM &lt; LMN_HLM |
| PV_FAC | 60.0 |  | REAL | 1.0 | The "Process value factor" input is multiplied by the "Process value I/O". The input is used to scale the process value range. |
| PV_OFFS | 64.0 |  | REAL | 0.0 | The "Process value offset" input is added to the "Process value I/O". The input is used to scale the process value range. |
| LMN_FAC | 68.0 |  | REAL | 1.0 | The "Output value factor" input is multiplied with the output value. The input is used to scale the output value range. |
| LMN_OFFS | 72.0 |  | REAL | 0.0 | The "Output value offset" input is added to the output value. The input is used to scale the output value range. |
| PER_TM | 76.0 |  | REAL | 1.0 s | The period duration of the pulse width modulation is entered at the PER_TM parameter. The relationship of the period duration to the sampling time of the pulse shaper determines the accuracy of the pulse width modulation.   PER_TM ≥ CYCLE |
| P_B_TM | 80.0 |  | REAL | 0.02 s | You can assign a minimum pulse or break time at the parameter "Minimum pulse/break time". P_B_TM is internally limited to &gt; CYCLE_P. |
| TUN_DLMN | 84.0 |  | REAL | 20.0 | Process excitation for controller tuning results from a output value step change at TUN_DLMN.  Values from -100 to 100 % are permitted. |
| PER_MODE | 88.0 |  | INT | 0 | You can use this switch to enter the type of I/O module. The process value at input PV_PER is then scaled as follows at the PV output.  - PER_MODE = 0: Thermocouples; PT100/NI100; standard   PV_PER * 0.1   Unit: C, °F - PER_MODE = 1: PT100/NI100; climate   PV_PER * 0.01   Unit: C, °F - PER_MODE = 2: Current/voltage    PV_PER * 100/27648   Unit: % |
| PVPER_ON | 90.0 |  | BOOL | FALSE | If the process value is to be read in from the I/Os, the PV_PER input must be interconnected with the I/Os and the "Enable process value I/Os" input must be set. |
| I_ITL_ON | 90.1 |  | BOOL | FALSE | The output of the integrator can be set at the I_ITLVAL input. The "Set I-action" input must be set for this. |
| PULSE_ON | 90.2 |  | BOOL | FALSE | If PULSE_ON = TRUE is set, the pulse shaper is activated. |
| TUN_KEEP | 90.3 |  | BOOL | FALSE | The mode changes to automatic only when TUN_KEEP changes to FALSE. |
| ER | 92.0 |  | REAL | 0.0 | The effective control deviation is output at the "Control deviation" output.  The valid values depend on the sensors used. |
| LMN_P | 96.0 |  | REAL | 0.0 | The "P-action" output contains the proportional action of the manipulated tag. |
| LMN_I | 100.0 |  | REAL | 0.0 | The "integral action" output contains the integral action of the manipulated tag. |
| LMN_D | 104.0 |  | REAL | 0.0 | The "D-action" output contains the derivative action of the manipulated tag. |
| PHASE | 108.0 |  | INT | 0 | The current phase of controller tuning is indicated at the PHASE output.  - PHASE = 0: No optimization mode; automatic or manual mode - PHASE = 1: Ready to start tuning; check parameters, wait for excitation, measure the sampling times - PHASE = 2: Actual tuning: Searching for point of inflection with constant output value. Entering the sampling time in instance DB. - PHASE = 3: Calculating the process parameters. Saving valid controller parameters prior to tuning. - PHASE = 4: Controller design - PHASE = 5: Following up the controller to the new manipulated variable - PHASE = 7: Validating the process type |
| STATUS_H | 110.0 |  | INT | 0 | [STATUS_H](#parameter-status_h-s7-300-s7-400) indicates the diagnostic value via the search for the point of inflection during the heating process. |
| STATUS_D | 112.0 |  | INT | 0 | [STATUS_D](#parameters-status_d-s7-300-s7-400) indicates the diagnostic value via the controller design during the heating process. |
| QTUN_RUN | 114.0 |  | BOOL | 0 | The tuning manipulated tag has been applied, tuning has started and is still in phase 2 (searching for point of inflection). |
| PI_CON | 116.0 |  | STRUCT |  | PI controller parameters |
| GAIN |  | +0.0 | REAL | 0.0 | PI controller gain  %/phys. Unit |
| TI |  | +4.0 | REAL | 0.0 s | PI integration time [s] |
| PID_CON | 124.0 |  | STRUCT |  | PID controller parameters |
| GAIN |  | +0.0 | REAL | 0.0 | PID controller gain |
| TI |  | +4.0 | REAL | 0.0s | PID integration time [s] |
| TD |  | +8.0 | REAL | 0.0s | PID derivative action time [s] |
| PAR_SAVE | 136.0 |  | STRUCT |  | The PID parameters are saved in this structure. |
| PFAC_SP |  | +0.0 | REAL | 1.0 | Proportional factor for setpoint changes  Values from 0.0 to 1.0 are permitted. |
| GAIN |  | +4.0 | REAL | 0.0 | Controller gain  %/phys. Unit |
| TI |  | +8.0 | REAL | 40.0 s | Integration time [s] |
| TD |  | +12.0 | REAL | 10.0 s | Derivative action time (s) |
| D_F |  | +16.0 | REAL | 5.0 | Derivative factor  Values from 5.0 to 10.0 are permitted. |
| CON_ZONE |  | +20.0 | REAL | 100.0 | Control zone band   If the control deviation is greater than the control zone band, the high output value limit is output as output value. If the control deviation is less than the negative control zone band, the low output value limit is output as the output value.  CON_ZONE ≥ 0.0 |
| CONZ_ON |  | +24.0 | BOOL | FALSE | Enable control zone |
| PFAC_SP | 162.0 |  | REAL | 1.0 | PFAC_SP specifies the effective P-action when there is a setpoint change. This is set between 0 and 1.  - 1: P-action has full effect if the setpoint changes. - 0: P-action has no effect if the setpoint changes.   Values from 0.0 to 1.0 are permitted. |
| GAIN | 166.0 |  | REAL | 2.0 | The "Proportional gain" input specifies controller amplification. The direction of control can be reversed by giving GAIN a negative sign.  %/phys. Unit |
| TI | 170.0 |  | REAL | 40.0 s | The "Integration time" (integral-action time) input defines the integrator's time response. |
| TD | 174.0 |  | REAL | 10.0 s | The "Derivative-action time" (rate time) input decides the time response of the differentiator. |
| D_F | 178.0 |  | REAL | 5.0 | The derivative factor decides the lag of the D-action.   D_F = derivative-action time/"Lag of the D-action"  Values from 5.0 to 10.0 are permitted. |
| CON_ZONE | 182.0 |  | REAL | 100.0 | If the control deviation is greater than the control zone band, the high output value limit is output as output value.  If the control deviation is less than the negative control zone band, the low output value limit is output as the output value.  The valid values depend on the sensors used. |
| CONZ_ON | 186.0 |  | BOOL | FALSE | You can use CONZ_ON =TRUE to enable the control zone. |
| TUN_ON | 186.1 |  | BOOL | FALSE | If TUN_ON=TRUE, the output value is averaged until the output value excitation TUN_DLMN is enabled either by a setpoint step-change or by TUN_ST=TRUE. |
| TUN_ST | 186.2 |  | BOOL | FALSE | If the setpoint is to remain constant during controller tuning at the operating point, a output value step-change by the amount of TUN_DLMN is activated by TUN_ST=1. |
| UNDO_PAR | 186.3 |  | BOOL | FALSE | Loads the controller parametersPFAC_SP, GAIN, TI, TD, D_FCONZ_ON and CON_ZONE from the data structure PAR_SAVE (only in manual mode). |
| SAVE_PAR | 186.4 |  | BOOL | FALSE | Saves the controller parameters PFAC_SP, GAIN, TI, TD, D_F, CONZ_ON and CON_ZONE in the data structure PAR_SAVE. |
| LOAD_PID | 186.5 |  | BOOL | FALSE | Loads the controller parametersGAIN, TI,TD depending on PID_ON from the data structure PI_CON or PID_CON (only in manual mode) |
| PID_ON | 186.6 |  | BOOL | TRUE | At the PID_ON input, you can specify whether or not the tuned controller will operate as a PI or PID controller.  - PID controller: PID_ON = TRUE - PI controller: PID_ON = FALSE   With certain process types it is nevertheless possible that only a PI controller will be designed despite PID_ON = TRUE. |
| GAIN_P | 188.0 |  | REAL | 0.0 | Identified process gain. In the case of process type I, GAIN_P tends to be estimated too low. |
| TU | 192.0 |  | REAL | 0.0 | Identified time lag of the process.  TU ≥ 3*CYCLE |
| TA | 196.0 |  | REAL | 0.0 | Identified recovery time of the process. In the case of process type I, TA tends to be estimated too low. |
| KIG | 200.0 |  | REAL | 0.0 | Maximum process value rise at manipulated tag excitation from 0 to 100 % [1/s]  GAIN_P = 0.01 * KIG * TA |
| N_PTN | 204.0 |  | REAL | 0.0 | The parameter specifies the order of the process. "Non-integer values" are also possible.  Values from 1.01 to 10.0 are permitted. |
| TM_LAG_P | 208.0 |  | REAL | 0.0 | Time constants of a PTN model (practical values only for N_PTN &gt;= 2). |
| T_P_INF | 212.0 |  | REAL | 0.0 | Time from process excitation until the point of inflection. |
| P_INF | 216.0 |  | REAL | 0.0 | Process value change from process excitation until the point of inflection.  The valid values depend on the sensors used. |
| LMN0 | 220.0 |  | REAL | 0.0 | Output value at the start of tuning  Detected in phase 1 (mean value).  Values from 0 to 100 % are permitted. |
| PV0 | 224.0 |  | REAL | 0.0 | Process value at the start of tuning |
| PVDT0 | 228.0 |  | REAL | 0.0 | Process value slew rate at start of tuning [1/s]  Sign adapted. |
| PVDT | 232.0 |  | REAL | 0.0 | Current process value slew rate [1/s]  Sign adapted. |
| PVDT_MAX | 236.0 |  | REAL | 0.0 | Max. change in the process value per second [1/s]  Maximum derivative of the process value at the point of inflection (sign adapted, always &gt; 0); is used to calculate TU and KIG. |
| NOI_PVDT | 240.0 |  | REAL | 0.0 | Noise action in PVDT_MAX in %  The higher the noise action, the less accurate (less aggressive) the control parameters. |
| NOISE_PV | 244.0 |  | REAL | 0.0 | Absolute noise in process value  Difference between maximum and minimum process value in phase 1. |
| FIL_CYC | 248.0 |  | INT | 1 | Number of cycles of the mean value filter  The process value is determined through FIL_CYC cycles. FIL_CYC is increased from 1 to a max. of 1024 if needed. |
| POI_CMAX | 250.0 |  | INT | 2 | Maximum number of cycles after point of inflection  This time is used to find another (i.e. better) inflection point for measuring noise. The tuning is completed only after this time. |
| POI_CYCL | 252.0 |  | INT | 0 | Number of cycles after inflection point |

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Parameter STATUS_H (S7-300, S7-400)

| STATUS_H | Description | Remedy |
| --- | --- | --- |
| 0 | Default, or no/no new controller parameters |  |
| 10000 | Tuning completed + suitable controller parameters found |  |
| 2xxxx | Tuning completed + controller parameters uncertain |  |
| 2xx2x | Point of inflection not reached (only if excited via setpoint step-change) | If the controller oscillates, weaken the controller parameters, or repeat the test with a smaller manipulated value difference TUN_DLMN. |
| 2x1xx | Estimation error (TU &lt; 3*CYCLE) | Reduce CYCLE and repeat attempt. Special case for PT1-only process: Do not repeat test, if necessary reduce controller parameters. |
| 2x3xx | Estimation error TU too high | Repeat test under better conditions. |
| 21xxx | Estimation error N_PTN &lt; 1 | Repeat test under better conditions. |
| 22xxx | Estimation error N_PTN &gt; 10 | Repeat test under better conditions. |
| 3xxxx | Tuning canceled in phase 1 owing to faulty parameter assignment: |  |
| 30002 | Effective manipulated value differential &lt; 5% | Correct manipulated value differential TUN_DLMN. |
| 30005 | The sampling times CYCLE and CYCLE_P differ by more than 5% of the measured values. | Compare CYCLE and CYCLE_P with the cycle time of the cyclic interrupt priority class and note any loop scheduler.  Check CPU load. An excessively loaded CPU can result in prolonged sampling times that are inconsistent with CYCLE or CYCLE_P. |

> **Note**
>
> If you cancel tuning in phase 1 or 2, STATUS_H = 0 is set. However, STATUS_D still displays the status of the last controller calculation.
>
> The higher the value of STATUS_D, the higher the order of the control process, the greater the TU/TA ratio and the gentler the controller parameters will be.

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

### Parameters STATUS_D (S7-300, S7-400)

| STATUS_D | Description |
| --- | --- |
| 0 | No controller parameters were calculated. |
| 110 | N_PTN &lt;= 1.5 Process type I fast |
| 121 | N_PTN &gt; 1.5 Process type I |
| 200 | N_PTN &gt; 1.9 Process type II (transition range) |
| 310 | N_PTN &gt;= 2.1 Process type III fast |
| 320 | N_PTN &gt; 2.6 Process type III |
| 111, 122, 201, 311, 321 | Parameters have been corrected from phase 7. |

> **Note**
>
> The higher the value of STATUS_D, the higher the order of the control process, the greater the TU/TA ratio and the gentler the controller parameters will be.

---

**See also**

[Description TCONT_CP (S7-300, S7-400)](#description-tcont_cp-s7-300-s7-400)
  
[Mode of operation TCONT_CP (S7-300, S7-400)](#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](#operating-principle-of-the-pulse-generator-s7-300-s7-400)
  
[Block diagram TCONT_CP (S7-300, S7-400)](#block-diagram-tcont_cp-s7-300-s7-400)
  
[Input parameters TCONT_CP (S7-300, S7-400)](#input-parameters-tcont_cp-s7-300-s7-400)
  
[Output parameters TCONT_CP (S7-300, S7-400)](#output-parameters-tcont_cp-s7-300-s7-400)
  
[In/out parameters TCONT_CP (S7-300, S7-400)](#inout-parameters-tcont_cp-s7-300-s7-400)
  
[Static variables TCONT_CP (S7-300, S7-400)](#static-variables-tcont_cp-s7-300-s7-400)
  
[Parameter STATUS_H (S7-300, S7-400)](#parameter-status_h-s7-300-s7-400)
  
[Differences compared to TCONT_CP S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_cp-s7-300400-s7-1500)

## TCONT_S (S7-300, S7-400)

This section contains information on the following topics:

- [Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
- [Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
- [Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
- [Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
- [Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
- [In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
- [Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)

### Description TCONT_S (S7-300, S7-400)

The TCONT_S instruction is used on SIMATIC S7 automation systems to control technical temperature processes with binary manipulated value output signals for actuators with integrating behavior. The functionality is based on the PI control algorithm of the sampling controller. The step controller operates without a position feedback signal.

#### Application

You can also use the controller in a cascade control as a secondary position controller. You specify the actuator position via the setpoint input SP_INT. In this case, you must set the process value input and the parameter TI (integration time) to zero. An application might be, for example, temperature control with heating power control using pulse-break activation and cooling control using a butterfly valve. To close the valve completely, the manipulated variable (ER*GAIN) should be negative.

#### Call

The instruction TCONT_S must be called with a constant bus cycle time. To achieve this, use a cyclic interrupt level (e.g. OB35 with S7-300). The sampling time is specified at the CYCLE parameter.

#### CYCLE sampling time

The CYCLE sampling time match the time difference between two calls (cycle time of the cyclic interrupt OB taking into account the reduction ratios).

The controller sampling time should not exceed 10% of the calculated integration time of the controller (TI). Generally, you must set the sampling time to a much lower value to achieve the required accuracy of the step controller.

| Required accuracy G | MTR_TM | CYCLE = MTR_TM*G | Comment |
| --- | --- | --- | --- |
| 0.5% | 10 s | 0.05 s | The sampling time is determined by the required accuracy of the step controller. |

#### Start-up

The TCONT_S instruction has an initialization routine that is run through when input parameter COM_RST = TRUE is set. Following execution of the initialization routine, the block sets COM_RST back to FALSE. All outputs are set to their initial values. If you require initialization when the CPU restarts, call the block in OB100 with COM_RST = TRUE.

---

**See also**

[Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
  
[Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
  
[Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
  
[Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
  
[In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
  
[Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)
  
[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)

### Mode of operation TCONT_S (S7-300, S7-400)

#### Setpoint branch

The setpoint is entered at input SP_INT in floating-point format as a physical value or percentage. The setpoint and process value used to form the control deviation must have the same unit.

#### Process value options (PVPER_ON)

Depending on PVPER_ON, the process value can be read in, in the I/O or floating-point format.

| PVPER_ON | Process Value Input |
| --- | --- |
| TRUE | The process value is read in via the analog I/Os (PIW xxx) at input PV_PER. |
| FALSE | The process value is acquired in floating-point format at input PV_IN. |

#### Process value format conversion CRP_IN (PER_MODE)

The CRP_IN function converts the I/O value PV_PER to floating-point format depending on the PER_MODE switch according to the following rules:

| PER_MODE | Output of CRP_IN | Analog Input Type | Unit |
| --- | --- | --- | --- |
| 0 | PV_PER * 0.1 | Thermoelements; PT100/NI100; standard | °C;°F |
| 1 | PV_PER * 0.01 | PT100/NI100; climate; | °C;°F |
| 2 | PV_PER * 100/27648 | Voltage/current | % |

#### Process value scaling PV_NORM (PF_FAC, PV_OFFS)

The PV_NORM function calculates the output of CRP_IN according to the following rule:

"Output of PV_NORM" = "Output of CRP_IN" * PV_FAC + PV_OFFS

It can be used for the following purposes:

- Process value adjustment with PV_FAC as process value factor and PV_OFFS as process value offset.
- Scaling of temperature to percentage

  You want to enter the setpoint as a percentage and must now convert the measured temperature value to a percentage.
- Scaling of percentage to temperature

  You want to enter the setpoint in the physical temperature unit and must now convert the measured voltage/current value to a temperature.

Calculation of the parameters:

- PV_FAC = range of PV_NORM/range of CRP_IN;
- PV_OFFS = LL (PV_NORM) - PV_FAC * LL(CRP_IN);

  where LL: low limit

The scaling is switched off with the default values (PV_FAC = 1.0 and PV_OFFS = 0.0). The effective process value is output at the PV output.

#### Example of Process Value Scaling

If you want to enter the setpoint as a percentage, and you have a temperature range of -20 to 85 °C applied to , CRP_IN you must normalize the temperature range as a percentage.

The diagram below shows an example of adapting the temperature range -20 to 85 °C to an internal scale of 0 to 100 %:

![Example of Process Value Scaling](images/166087298443_DV_resource.Stream@PNG-de-DE.png)

#### Forming the control deviation

The difference between the setpoint and process value is the control deviation before the dead zone.

The setpoint and process value must exist in the same unit.

#### Dead zone (DEADB_W)

To suppress a minor sustained oscillation due to the manipulated variable quantization (for example, in pulse width modulation with PULSEGEN) a dead zone is applied to the (DEADBAND) control deviation. With DEADB_W = 0.0, the dead zone is disabled.

![Dead zone (DEADB_W)](images/166087355147_DV_resource.Stream@PNG-de-DE.png)

#### PI step controller algorithm

The instruction TCONT_S operates without position feedback. The I-action of the PI algorithm and the assumed position feedback signal are calculated in an integrator (INT) and compared as a feedback value with the remaining proportional action. The difference is applied to a three-step element (THREE_ST) and a pulse shaper (PULSEOUT) that generates the pulses for the control valve. Adapting the response threshold of the three-step element reduces the switching frequency of the controller.

#### Weakening of the proportional action when setpoint changes occur

To prevent overshoot, you can weaken the proportional action using the "Proportional factor for setpoint changes" parameter (PFAC_SP). Using PFAC_SP, you can now select continuously between 0.0 and 1.0 to decide the effect of the proportional action when the setpoint changes:

- PFAC_SP = 1.0: Proportional action for setpoint change is fully effective
- PFAC_SP = 0.0: Proportional action has no effect in the setpoint change

As in the case of the continuous controller, a value of PFAC_SP &lt; 1.0 can reduce the overshoot if the motor run time MTR_TM is small compared with the recovery time TA and the ratio is TU/TA &lt; 0.2. If MTR_TM reaches 20% of TA, only a slight improvement can still be achieved.

#### Feedforward control

A disturbance variable can be added at the DISV input.

#### Manual value processing (LMNS_ON, LMNUP, LMNDN)

With LMNS_ON, you can change between manual and automatic mode. In manual mode, the actuator is halted and the integral action (INT) is set to 0 internally. Using LMNUP and LMNDN, the actuator can be adjusted to OPEN and CLOSED. Switching over to automatic mode therefore involves a bump. As a result of the GAIN, the existing control deviation leads to a step change in the internal manipulated variable. The integral component of the actuator, however, results in a ramp-shaped excitation of the process.

---

**See also**

[Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
  
[Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
  
[Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
  
[Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
  
[In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
  
[Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)
  
[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)

### Block diagram TCONT_S (S7-300, S7-400)

![Figure](images/166087474571_DV_resource.Stream@PNG-de-DE.png)

![Figure](images/166087401611_DV_resource.Stream@PNG-de-DE.png) Parameter configuration interface

![Figure](images/166087456395_DV_resource.Stream@PNG-de-DE.png) Instruction call interface

![Figure](images/166087459979_DV_resource.Stream@PNG-de-DE.png) Parameter configuration interface, call interface

---

**See also**

[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)
  
[Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
  
[Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
  
[Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
  
[Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
  
[In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
  
[Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)

### Input paramters TCONT_S (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| CYCLE | 0.0 | REAL | 0.1 s | At this input, you enter the sampling time for the controller.  CYCLE ≥ 0.001 |
| SP_INT | 4.0 | REAL | 0.0 | The input "Internal setpoint" is used to specify a setpoint.  The valid values depend on the sensors used. |
| PV_IN | 8.0 | REAL | 0.0 | At the "Process variable input" you can assign parameters to a commissioning value or you can interconnect an external process value in floating-point format.   The valid values depend on the sensors used. |
| PV_PER | 12.0 | INT | 0 | The process value in I/O format is interconnected with the controller at the "Process value I/O" input. |
| DISV | 14.0 | REAL | 0.0 | For feedforward control, the disturbance variable is interconnected to the "Disturbance variable" input. |
| LMNR_HS | 18.0 | BOOL | FALSE | The signal "Control valve at high endstop" is interconnected on the input "High endstop signal of position feedback".   - LMNR_HS=TRUE: The control valve is located at the high endstop. |
| LMNR_LS | 18.1 | BOOL | FALSE | The signal "Control valve at low endstop" is interconnected on the input "Low endstop signal of position feedback".  - LMNR_LS=TRUE:  The control valve is located at the low endstop. |
| LMNS_ON | 18.2 | BOOL | TRUE | Manipulated value signal processing is switched to manual mode at the "Enable manual mode of manipulated signal". |
| LMNUP | 18.3 | BOOL | FALSE | In manual mode of manipulated signals, the output parameter QLMNUP is operated at the input parameter "Manipulated signal up". |
| LMNDN | 18.4 | BOOL | FALSE | In manual mode of the manipulated signals, the output parameter QLMNDN is operated at the input parameter "Manipulated signal down". |

---

**See also**

[Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
  
[Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
  
[Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
  
[Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
  
[In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
  
[Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)
  
[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)

### Output parameters TCONT_S (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| QLMNUP | 20.0 | BOOL | FALSE | If the output "Manipulated value signal up" is set then the control valve should be open. |
| QLMNDN | 20.1 | BOOL | FALSE | If the output "Manipulated value signal down" is set then the control valve should be closed. |
| PV | 22.0 | REAL | 0.0 | The effective process value is output at the "Process value" output. |
| ER | 26.0 | REAL | 0.0 | The effective system deviation is output at the "Error signal" output. |

---

**See also**

[Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
  
[Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
  
[Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
  
[Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
  
[In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
  
[Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)
  
[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)

### In/out parameters TCONT_S (S7-300, S7-400)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 30.0 | BOOL | FALSE | The block has an initialization routine that is processed when the COM_RST input is set. |

---

**See also**

[Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
  
[Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
  
[Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
  
[Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
  
[Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
  
[Static variables TCONT_S (S7-300, S7-400)](#static-variables-tcont_s-s7-300-s7-400)
  
[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)

### Static variables TCONT_S (S7-300, S7-400)

The names of the following variables apply both to the data block and to access via the Openness API.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| PV_FAC | 32.0 | REAL | 1.0 | The "Process value factor" input is multiplied by the process value. The input is used to scale the process value range. |
| PV_OFFS | 36.0 | REAL | 0.0 | The input "Process value offset" is added to the process value. The input is used to scale the process value range.  The valid values depend on the sensors used. |
| DEADB_W | 40.0 | REAL | 0.0 | A deadband is applied to the control deviation. The "Deadband width" input determines the size of the deadband.  DEADB_W ≥ 0.0 |
| PFAC_SP | 44.4 | REAL | 1.0 | PFAC_SP specifies the effective P-action when there is a setpoint change.  - 1: P-action has full effect if the setpoint changes. - 0: P-action has no effect if the setpoint changes.   Values from 0.0 to 1.0 are permitted. |
| GAIN | 48.0 | REAL | 2.0 | The "Proportional gain" input specifies controller amplification. The direction of control can be reversed by giving GAIN a negative sign.  %/phys. Unit |
| TI | 52.0 | REAL | 40.0 s | The "Integration time" (integral-action time) input defines the integrator's time response. |
| MTR_TM | 56.0 | REAL | 30 s | The runtime from endstop to endstop of the control valve is entered at the "Motor actuating time" parameter.  MTR_TM ≥ CYCLE |
| PULSE_TM | 60.0 | REAL | 0.0 s | A minimum pulse time can be configured at the "Minimum pulse time" parameter. |
| BREAK_TM | 64.0 | REAL | 0.0 s | You can assign a minimum break time at the parameter "Minimum break time". |
| PER_MODE | 68.0 | INT | 0 | You can use this switch to enter the type of I/O module. The process value at input PV_PER is then scaled as follows at the PV output.  - PER_MODE = 0: Thermocouples; PT100/NI100; standard   PV_PER * 0.1   Unit: C, °F - PER_MODE = 1: PT100/NI100; climate   PV_PER * 0.01   Unit: C, °F - PER_MODE = 2: Current/voltage    PV_PER * 100/27648   Unit: % |
| PVPER_ON | 70.0 | BOOL | FALSE | If the process value is to be read in from the I/Os, the PV_PER input must be interconnected with the I/Os and the "Enable process value I/Os" input must be set. |

---

**See also**

[Description TCONT_S (S7-300, S7-400)](#description-tcont_s-s7-300-s7-400)
  
[Mode of operation TCONT_S (S7-300, S7-400)](#mode-of-operation-tcont_s-s7-300-s7-400)
  
[Block diagram TCONT_S (S7-300, S7-400)](#block-diagram-tcont_s-s7-300-s7-400)
  
[Input paramters TCONT_S (S7-300, S7-400)](#input-paramters-tcont_s-s7-300-s7-400)
  
[Output parameters TCONT_S (S7-300, S7-400)](#output-parameters-tcont_s-s7-300-s7-400)
  
[In/out parameters TCONT_S (S7-300, S7-400)](#inout-parameters-tcont_s-s7-300-s7-400)
  
[Differences compared to TCONT_S S7-300/400 (S7-1500)](PID%20basic%20functions%20%28S7-1500%29.md#differences-compared-to-tcont_s-s7-300400-s7-1500)

## Integrated system functions (S7-300, S7-400)

This section contains information on the following topics:

- [CONT_C_SF (S7-300, S7-400)](#cont_c_sf-s7-300-s7-400)
- [CONT_S_SF (S7-300, S7-400)](#cont_s_sf-s7-300-s7-400)
- [PULSEGEN_SF (S7-300, S7-400)](#pulsegen_sf-s7-300-s7-400)

### CONT_C_SF (S7-300, S7-400)

#### CONT_C_SF

The instruction CONT_C_SF is integrated in the S7-300 compact CPUs. The instruction must not be transmitted to the S7-300 CPU during loading. The scope of function corresponds with the instruction CONT_C.

---

**See also**

[Description CONT_C (S7-300, S7-400)](#description-cont_c-s7-300-s7-400)
  
[How CONT_C works (S7-300, S7-400)](#how-cont_c-works-s7-300-s7-400)
  
[CONT_C block diagram (S7-300, S7-400)](#cont_c-block-diagram-s7-300-s7-400)
  
[Input parameter CONT_C (S7-300, S7-400)](#input-parameter-cont_c-s7-300-s7-400)
  
[Output parameters CONT_C (S7-300, S7-400)](#output-parameters-cont_c-s7-300-s7-400)

### CONT_S_SF (S7-300, S7-400)

#### CONT_S_SF

The instruction CONT_S_SF is integrated in the S7-300 compact CPUs. The instruction must not be transmitted to the S7-300 CPU during loading. The scope of function corresponds with the instruction CONT_S.

---

**See also**

[Description CONT_S (S7-300, S7-400)](#description-cont_s-s7-300-s7-400)
  
[Mode of operation CONT_S (S7-300, S7-400)](#mode-of-operation-cont_s-s7-300-s7-400)
  
[Block diagram CONT_S (S7-300, S7-400)](#block-diagram-cont_s-s7-300-s7-400)
  
[Input parameters CONT_S (S7-300, S7-400)](#input-parameters-cont_s-s7-300-s7-400)
  
[Output parameters CONT_S (S7-300, S7-400)](#output-parameters-cont_s-s7-300-s7-400)

### PULSEGEN_SF (S7-300, S7-400)

#### PULSEGEN_SF

The instruction PULSEGEN_SF is integrated in the S7-300 compact CPUs. The instruction must not be transmitted to the S7-300 CPU during loading. The scope of function corresponds with the instruction PULSEGEN.

---

**See also**

[Description PULSEGEN (S7-300, S7-400)](#description-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400)
  
[Mode of operation PULSEGEN (S7-300, S7-400)](#mode-of-operation-pulsegen-s7-300-s7-400-1)
  
[Three-step control (S7-300, S7-400)](#three-step-control-s7-300-s7-400)
  
[Two-step control (S7-300, S7-400)](#two-step-control-s7-300-s7-400)
  
[Input parameters PULSEGEN (S7-300, S7-400)](#input-parameters-pulsegen-s7-300-s7-400)
  
[Output parameter PULSEGEN (S7-300, S7-400)](#output-parameter-pulsegen-s7-300-s7-400)
