---
title: "PID Self Tuner (S7-300, S7-400)"
package: ProgFBPIDTunenUS
topics: 24
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PID Self Tuner (S7-300, S7-400)

This section contains information on the following topics:

- [TUN_EC (S7-300, S7-400)](#tun_ec-s7-300-s7-400)
- [TUN_ES (S7-300, S7-400)](#tun_es-s7-300-s7-400)

## TUN_EC (S7-300, S7-400)

This section contains information on the following topics:

- [Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
- [Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
- [Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
- [Control zone and structure switchover (S7-300, S7-400)](#control-zone-and-structure-switchover-s7-300-s7-400)
- [Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
- [Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
- [In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
- [Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
- [Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
- [Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
- [Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Description TUN_EC (S7-300, S7-400)

The TUN_EC instruction is used to tune a continuous PID controller. Depending on the controller, you interconnect TUN_EC with one of the following instructions:

- FM 355 C, FM 355 S pulse controller, FM 455 C or FM 455 S pulse controller

  - PID_FM
- PID Basic Functions

  - CONT_C with or without PULSEGEN
- Standard PID Control (PID Professional optional package)

  - PID_CP
- Modular PID Control (PID Professional optional package)

  - PID
  - LMNGEN_C

#### Call

TUN_EC is called in constant intervals of the cycle time of the calling OB (preferably in a cyclic interrupt OB).

When ADAPT1ST = TRUE , the initialization routine of the TUN_EC instruction is run. The following preassignments are made:

- The system switches to PI controller. The parameters of PI_CON are transferred to the controller for this purpose. If the PI_CON.GAIN and PI_CON.TI parameters both have the value 0.0, they are preassigned with PI_CON.GAIN = 1.5 and PI_CON.TI = 3600.0 s.
- PROCESS.GAIN = 999.0
- RATIOFAC = 1.0
- STATUS_H = 0; STATUS_D = 0; STATUS_C = 0

  > **Note**
  >
  > Unless explicitly required, do **not** call TUN_ES during a warm restart of the CPU in its initialization routine as is usual for other instructions. If you do, all process parameters will be lost.

#### CYCLE sampling time

You enter the sampling time in the CYCLE parameter. The sampling time should not exceed 10% of the determined integral action time of the controller. It must agree with the time difference between two calls (cycle time of the cyclic interrupt OB taking into account the reduction ratios).

In order for the process parameters to be identified reliably, the smallest time constant of the process (delay time) should be sampled at least 10 to 20 times.

In connection with the FM355/455 controller modules, the sampling time of TUN_EC must be approximately equal to the resulting cycle time of the controllers on the FM (Parameter setting &gt; Module parameters).

#### Reaction to error

The error message word RET_VAL is not evaluated by the block.

---

**See also**

[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Scope of TUN_EC (S7-300, S7-400)

The Self-Tuner can be used particularly well for:

- Temperature control systems, but also for
- Level control systems and
- Flow control systems

In the case of flow control systems a distinction must be made as to whether only the control valve itself is to be controlled or whether a process with associated delay follows the control valve. In the case of control valve control only, the Self-Tuner cannot be used.

#### Process requirements

The process must meet the following requirements:

- **Stable asymptotic transient response with associated delay**

  The process value must settle to steady state after a manipulated variable jump. This therefore excludes processes that already exhibit an oscillating response in the absence of closed-loop control, as well as controlled systems without inherent regulation (integrator in the controlled system).
- **Delay times not too large**

  The range of application can be specified based on the ratio of the delay time t<sub>u</sub> and response time t<sub>a</sub>. The delay time also encompasses any existing dead time.

  The pretuning or adaptation is designed for the range t<sub>u</sub> &lt; 1/10 t<sub>a</sub>, within which most controlled temperature systems fall.

  For the range of especially long delay times 1/10 t<sub>a</sub> &lt; t<sub>u</sub> &lt; 1/3 t<sub>a</sub>, the design of a utilizable PI controller is generally still also possible.
- **Adequate linear response across a sufficiently large operating range**

  This means that non-linear effects within this operating range can be ignored both during identification and during normal closed-loop control operation. However, it is possible to re-identify the process when there is a change from one operating point to another if the adaptation process is carried out again close to the new operating point and provided that the non-linearity is not passed through during adaptation.

  If certain static non-linearities (e.g., valve characteristic curves) are known, it is always advisable to compensate for them in advance with a polyline in order to linearize the process response.
- **Minimal disturbances in temperature processes**

  Disturbances such as thermal transfer to neighboring zones or heat gains or losses due to changes from one state of matter to another must not influence the overall temperature process to any great extent. If necessary, adaptation at the operating point may be necessary. For example, when zones of an extruder are tuned, all zones must be heated up simultaneously.
- **Quality of the measuring signals**

  The quality of the measured signals has to be sufficient; in other words, the signal-to-disturbance ratio has to be sufficiently high.
- **Process gains not too high**

  The process gains must not be too high. Normalization of the process values is not required. The process gain K can thus include physical units, such as:

  K =∆PV/∆LMN, [K]= °C/%

  The final controller design is based on a calculation of the process gain K and can thus in principle compensate for any values of K. However, K is initially unknown during the learning phase and overshoots cannot be avoided when there are extreme combinations of gain and learning step changes. The overshoot is also reduced by reducing the parameter LHLM_TUN in the heating process or by increasing LLLM_TUN in the cooling process.

#### Requirements for processes with a control valve with integral action

In processes with control valves with an integral action, further requirements must be met in addition to those specified above:

The motor run time of the control valve must be less than the time required to find a point of inflection after a manipulated variable jump (also refer to the process response figure). If this is not the case, the process involved is often a flow rate control system in which only the control valve is effective as the dominating process action. It is not advisable to use the Self-Tuner in this case. You can then set the PI step controller manually in accordance with the following rule of thumb:

GAIN = 1, TI = Motor transition time

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Mode of operation TUN_EC (S7-300, S7-400)

TUN_EC has the following functions for the control and optimization of the controller:

- **Manual mode**

   The Self-Tuner forces the controller into manual mode and transfers its manual parameters to it.
- **Manual/automatic changeover with predictive manipulated-value specification**

   After the controller has been optimized successfully, the Self-Tuner can change over the controller from manual mode to automatic mode by feedforwarding a predictive manipulated value in such a manner that the process settles rapidly into the setpoint. This type of changeover involves a bump. You can also set bumpless changeover at the Self-Tuner.
- **Controller tuning**

   The process is first identified during the optimization of the controller parameters. A controller is designed based on the process characteristics. The new system parameters are calculated on this basis and these are activated for the controller.

  - **First adaption**

     Pretuning can only be carried out for a positive setpoint jump. It is usually used during initial commissioning or in case of a serious change in the controlled system characteristics.
  - **Fine tuning**

     The controller can be fine tuned online during a positive setpoint jump when there is a change from one operating point to another or when there are changes in the process response.
  - **Cooling tuning**

    For control systems that operate with two opposing actuators (for example, in case of temperature control: heating and cooling actuators) the Self-Tuner determines the ratio of the process gains under the influence of a second actuator in the case of a negative manipulated value step (using the same example of a temperature control: under influence of the cooling actuator).

  **Tuning the response to setpoint changes**

  The controller is designed for optimum disturbance response, in principle. The resultant "Stringent" parameters would result in overshoots of 10% to 20 % of the step height at setpoint steps.

  The **control zone** represents an initial remedy. To tune the start-up control response for large setpoint steps, the Self-Tuner calculates a control zone band during optimization. The controller is active within the band. Outside the band the Self-Tuner controls the controller with the maximum or minimum manipulated variable of the controller.

  The **structure segmentation** represents an additional remedy. In this case, the proportional or derivative action is located in the feedback loop. A change in the setpoint thus only acts on the integral action of the controller.

  If structure segmentation is not possible for the controller or if the control zone fails, the following function can be activated to tune the command characteristics:
- **Structure switchover:**

  Temporary disabling of the I-action or predictive manipulated value specification for large positive setpoint steps. This function is not effective when the control zone is activated.
- **Saving the controller parameters**

   If you assess the current controller parameters to be utilizable, you can save these in specially provided parameters in the instance DB of the Self-Tuner, before a manual change in parameters. If you tune the controller, the saved parameters are overwritten by the values that were valid prior to tuning.
- **Reloading saved controller parameters**

  The last controller parameter settings you saved can be activated for the controller again using this function.
- **Changing the controller parameters**

   If you want to set the controller parameters yourself for the controller, you can assign these through special parameters in the instance DB of the Self-Tuner and transfer them to the controller by means of this function.

#### Enabling the functions

| Function | Start bit | Enable bit | Start condition:  PHASE | Start condition:  Setpoint step-change at SP |
| --- | --- | --- | --- | --- |
| Manual mode | — | MAN_ON | 0 to 7 | — |
| Manual/automatic changeover with predictive manipulated-value specification | — | PRED_ON | Transition 7 -&gt; 4 | — |
| First adaption | ADAPT1ST | — | 0, 4 | Pos.: &gt; MIN_STEP |
| First adaption or fine tuning | ADAPT_ON | — | 4 | Pos.: &gt; MIN_STEP |
| Cooling tuning | COOLID_ON | — | 4 | — |
| Control zone | — | CONZ_ON | 4 |  |
| Structure switchover | — | STRUC_ON | 4 | Pos.: &gt; MIN_STEP,  Neg: &gt; MIN_STEP × RATIO_FAC |
| Save controller parameters | SAVE_PAR | — | 2 to 7 | — |
| Reloading controller parameters | UNDO_PAR | — | 4 | — |
| Change controller parameters | LOAD_PAR | — | 4 | — |

> **Note**
>
> Start bits are reset after the function has been started successfully. Enable bits remain set.

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Control zone and structure switchover (S7-300, S7-400)

#### Control zone

The Self-Tuner operates with a control zone. This means that the controller operates based on the following algorithm:

- If the control deviation is greater than CON_ZONE, the system is heated with maximum power.
- If the control deviation is less than (-CON_ZONE) × RATIOFAC, the system is cooled with maximum power.

During pretuning or fine tuning, a CON_ZONE control zone is determined by the Self-Tuner and activated if the process type is suitable: CONZ_ON = TRUE. In closed-loop control, you can change the control zone or deactivate it completely (with CONZ_ON = FALSE).

![Control zone](images/18064332171_DV_resource.Stream@PNG-en-US.png)

When the control zone is activated (CONZ_ON = TRUE), the structure switchover STRUC_ON is not effective.

> **Note**
>
> When there is a separate controller design for controlled systems with long delay time, a control zone is not determined, for example when STATUS_D = 3 after adaptation.
>
> Before you switch on the control zone manually, make sure that the control zone width is not too small. If the control zone width is set too narrow, oscillations occur in the manipulated variable and the process value trends.

#### Structure segmentation

Structure segmentation is a function of the controller. In the case of closed-loop control with structure segmentation, the proportional or derivative action lies within the feedback loop, so that a change in the setpoint only acts on the integral action of the controller. When setpoint jumps occur, the manipulated variable does not undergo a jump change but instead follows a ramp-shaped course. The disturbance response is not changed as a result.

![Closed-loop control with structure segmentation](images/30631088395_DV_resource.Stream@PNG-en-US.png)

Closed-loop control with structure segmentation

In the case of closed-loop control without structure segmentation, the proportional and derivative actions lie within the control deviation, just like the integral action. You can select a structure switchover for this operating mode (STRUC_ON = TRUE).

Closed-loop control with structure segmentation is possible in the following control packages:

- FM 355/455
- Standard PID Control
- Modular PID Control

  > **Note**
  >
  > Only closed-loop control without structure segmentation is possible for the simple controller PID Control of STEP 7 Basic and in the CPU 314 IFM. The structure switchover function should only be selected if there are no other alternatives.

#### Structure switchover when proportional and derivative actions are within the control deviation

The structure switchover is deactivated in the default setting. It should only be selected if no other alternatives such as, for example, control zone or structure segmentation, are available.

When the control zone is activated (CONZ_ON = TRUE), the structure switchover STRUC_ON is not effective.

You can activate the structure switchover with STRUC_ON = TRUE. The block automatically selects between two control measures depending on the total loop gain (product of the process gain and the controller gain):

- Integral action temporarily deactivated, P(D) control:

  In the case of a positive setpoint jump ≥ MIN_STEP, the integral action of the controller is deactivated temporarily and the gain is increased slightly, which means that a pure P(D) controller is used. In the proximity of the setpoint, the integral action is reactivated and the gain is reduced again (PHASE = 5).
- Temporary predictive manipulated variable specification:

  Processes with a high delay time cannot be controlled well with a P(D) control system. After a positive setpoint jump ≥ MIN_STEP, the manipulated variable required constantly for the new setpoint is therefore output constantly. In the proximity of the setpoint, the system is switched back bumplessly to PI or PID closed-loop control. This results in a slow, but overshoot-free response (PHASE = 6).

  > **Note**
  >
  > If you do not achieve good results (transient response is slow) with the structure switchover in the case of positive setpoint jumps (for example, during heating processes), you can deactivate the structure switchover with STRUC_ON = FALSE, on the condition that small overshoots may occur.

| Controller structure modes | CONZ_ON | PFDB_SEL, DFDB_SEL <sup>1)</sup> | STRUC_ON |
| --- | --- | --- | --- |
| Activate control zone | TRUE | Any | Any |
| Activate structure segmentation | Any | TRUE | FALSE |
| Activate structure switchover | FALSE | FALSE | TRUE |

<sup>1)</sup> Controller parameters PFDB_SEL, DFDB_SEL: When CONT_C, these parameters are not available. This corresponds to the PFDB_SEL = DFDB_SEL = FALSE setting (without structure segmentation).

> **Note**
>
> **Notes on selecting the operating modes:**
>
> - The Self-Tuner calculates a control zone and activates it automatically, if the ratio of the two time constants of the process is f = TM_LAG1 / TM_LAG2 &gt; 10.
> - In the case of jumps within the control zone, the structure segmentation that is selected by default acts, if allowed by the controller.
> - If you want to compensate for small setpoint jumps within the control zone as quickly as possible and are willing to accept small overshoots, deactivate the structure segmentation.
>
>   Numerical example: Control zone 20 °C, then overshoots of approx. 10% to 20% of the step size (&lt; 20 °C) occur, i.e. less than 2 to 4 °C.
> - The structure segmentation function prevents overshoots at setpoint jumps of all sizes, even if the process does not permit a control zone or you have deactivated it. However, the rise times are slightly slower than with a control zone.
> - If the process does not allow a control zone and the controller does not allow a structure segmentation, activate the structure switchover. The structure switchover must not be activated at the same time as the structure segmentation.

### Input parameters TUN_EC (S7-300, S7-400)

| Parameter | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP | 0.0 | REAL | 0.0 | Enter the setpoint at the SP input. It is interconnected with the controller via SP_OUT. Note that the setpoint must lie within the setpoint limits of the controller. |
| PV | 4.0 | REAL | 0.0 | PV is interconnected with the process value of the controller. |
| LMN | 8.0 | REAL | 0.0 | LMN is interconnected with the manipulated variable of the controller.  Values from -100 to 100% are permitted. |
| MAN | 12.0 | REAL | 0.0 | Enter the manual value at the MAN input. If MAN_ON = TRUE, the manual value MAN is transferred to the manipulated variable of the controller. If MAN_ON = TRUE and MAN = 0.0, the heating/cooling function is off. If MAN_ON = FALSE, the manipulated variable is specified by the controller.  Values from -100 to 100% are permitted. |
| MIN_STEP | 16.0 | REAL | 10.0 | You can specify the minimum setpoint jump above which pretuning or adaptation can be carried out in the MIN_STEP input.  If structure switchover (STRUC_ON = TRUE) is activated, the setpoint jump must be greater than MIN_STEP in order for the structure switchover activation to take place.  Recommendation: MIN_STEP ≥ 10 % of the required setpoint-process value range |
| LHLM_TUN | 20.0 | REAL | 80.0 | At the LHLM_TUN input, specify the manipulated variable jump for the first setting. The manipulated variable jump is calculated automatically during subsequent fine tuning.  Values from 0 to 100% are permitted. |
| LLLM_TUN | 24.0 | REAL | -20.0 | You specify the manipulated variable jump for cooling tuning at the LLM_TUN input.  Values from -100 to 0% are permitted. |
| NORM_FAC | 28.0 | REAL | 1.0 | A normalization factor is applied for controllers with a normalized controller gain (Standard PID Control). The normalization factor is calculated on the basis of the range limits of the process value of the controller and is interconnected with the NORM_FAC input. |
| MAN_ON | 32.0 | BOOL | TRUE | If MAN_ON = TRUE, the manipulated variable of the controller is specified via the MAN input. If MAN_ON = FALSE, the manipulated variable is specified by the controller. |
| PID_ON | 32.1 | BOOL | TRUE | At the PID_ON input, you can specify whether or not the tuned controller will operate as a PI or PID controller.  PID controller: PID_ON = TRUE   PI controller: PID_ON = FALSE  With certain controlled system types, however, it is possible that only a PI controller will be designed, despite PID_ON = TRUE. |
| STRUC_ON | 32.2 | BOOL | FALSE | If STRUC_ON = TRUE, a structure switchover (from PI(D) to P(D) control) ensures that overshoots are largely avoided at setpoint jumps. The STRUC_ON input must not be set = TRUE if the proportional action or derivative action is fed into the feedback loop of the controller. |
| WRITE_DIS | 32.3 | BOOL | FALSE | In connection with the controller module, the Self-Tuner must know whether the driver block is ready to send data to the FM. This is the case if LOAD_OP = LOAD_PAR = FALSE. The result of the OR operation of LOAD_OP and LOAD_PAR is interconnected with WRITE_DIS. |
| PRED_ON | 32.4 | BOOL | TRUE | When changing over to automatic mode you can specify whether you want to change over bumplessly from the last manual value or with bumps with a manipulated variable calculated by the Self-Tuner. If PRED_ON = TRUE (default setting) the changeover is carried out with bumps. The changeover with bumps is only effective after tuning and ensures rapid settling into the desired setpoint, in particular for a PI control system. |
| CYCLE | 34.0 | TIME | 100 ms | The sampling time must be configured in the CYCLE input. CYCLE must correspond to the sampling time of the controller to be set and the time difference between two calls (cycle time of the cyclic interrupt OB taking into account the reduction ratios).  CYCLE &gt; 1 ms |

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Output parameters TUN_EC (S7-300, S7-400)

| Parameter | Address |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| MAN_OUT | 38.0 |  | REAL | 0.0 | MAN_OUT is connected to the manual input value of the controller. If MAN_ON = TRUE, the Self-Tuner outputs the value specified at the MAN input to the MAN_OUT output. |
| SP_OUT | 42.0 |  | REAL | 0.0 | SP_OUT is connected to the setpoint input of the controller. The Self-Tuner writes the setpoint specified at the SP input to the SP_OUT output. If manual mode MAN_ON = TRUE, the setpoint is tracked to the process value: SP_OUT = PV. |
| GAIN | 46.0 |  | REAL | 1.5 | GAIN is interconnected with the proportional gain (controller gain) of the controller. |
| TI | 50.0 |  | TIME | 1 h | TI is interconnected with the integral action time (reset time) of the controller. |
| TD | 54.0 |  | TIME | 0 ms | TD is interconnected with the derivative action time (rate time) of the controller. |
| TM_LAG | 58.0 |  | TIME | 1 s | TM_LAG is interconnected with the time lag of the controller differentiator. |
| RATIOFAC | 62.0 |  | REAL | 1.0 | RATIOFAC is interconnected with the heating/cooling ratio factor of the controller or of the PULSEGEN instruction. The parameter is only required for cooling. |
| PHASE | 66.0 |  | INT | 0 | [Parameter TUN_EC.PHASE](#parameter-tun_ecphase-s7-300-s7-400) displays the current sequence of the controller tuning. During the tuning of Standard PID Control, the PHASE output is interconnected with the PHASE input of the PID_CP instruction. |
| STATUS_H | 68.0 |  | INT | 0 | [Parameter TUN_EC.STATUS_H](#parameter-tun_ecstatus_h-s7-300-s7-400) displays tuning results regarding the search for the point of inflection during the heating process. |
| STATUS_D | 70.0 |  | INT | 0 | [Parameter TUN_EC.STATUS_D](#parameter-tun_ecstatus_d-s7-300-s7-400) displays tuning results regarding the controller design during the heating process. |
| STATUS_C | 72.0 |  | INT | 0 | [Parameter TUN_EC.STATUS_C](#parameter-tun_ecstatus_c-s7-300-s7-400) displays tuning results regarding the search for the point of inflection during the cooling process. |
| QMAN_ON | 74.0 |  | BOOL | FALSE | QMAN_ON is interconnected with the manual/automatic changeover of the controller. |
| QI_SEL | 74.1 |  | BOOL | TRUE | QI_SEL is interconnected with the on/off switch of the controller integral action I_SEL.  With the FM355/455, TI must be switched to zero depending on QI_SEL: If QI_SEL = FALSE, then TI = 0. |
| QD_SEL | 74.2 |  | BOOL | FALSE | QD_SEL is interconnected with the on/off switch of the controller derivative action D_SEL.  With the FM355/455, TD must be switched to zero depending on QD_SEL: If QD_SEL = FALSE, then TD = 0. |
| QWRITE | 74.3 |  | BOOL | FALSE | QWRITE is interconnected with the LOAD_PAR and LOAD_OP inputs of the PID_FM instruction of FM355/455.  As a result, the data records of the controller channel are downloaded to the FM. |
| PROCESS | 76.0 |  | STRUCT |  | The PROCESS structure contains the parameters of the process. |
| GAIN |  | +0.0 | REAL | 999.0 | The process gain is displayed in the PROCESS.GAIN output. |
| TM_LAG1 |  | +4.0 | REAL | 0.0 | The slow process time constant is displayed at the PROCESS.TM_LAG1 output. |
| TM_LAG2 |  | +8.0 | REAL | 0.0 | The fast process time constant is displayed at the PROCESS.TM_LAG2 output. |
| PV00 |  | +12.0 | REAL | 0.0 | The zero mean value of the process is displayed in the PROCESS.PV00 output.  The zero mean value is the steady-state process value when manipulated variable = zero. This corresponds to the ambient temperature when the system is cold. |
| KIG |  | +16.0 | REAL | 0.0 | The maximum rise ratio of the process value during heating is displayed in the PROCESS.KIG output. |
| KIG_C |  | +20.0 | REAL | 0.0 | The maximum fall ratio of the process value during cooling is displayed in the PROCESS.KIG_C output. |
| PI_CON | 100.0 |  | STRUCT |  | The PI_CON structure contains the parameters of the PI controller. |
| GAIN |  | +0.0 | REAL | 1.5 | PI_CON.GAIN displays the proportional gain of the PI controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| TI |  | +4.0 | REAL | 3600.0 | PI_CON.TI displays the integral action time of the PI controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| PID_CON | 108.0 |  | STRUCT |  | The PID_CON structure contains the parameters of the PID controller. |
| GAIN |  | +0.0 | REAL | 1.5 | PID_CON.GAIN displays the proportional gain of the PID controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| TI |  | +4.0 | REAL | 3600.0 | PID_CON.TI displays the integral action time of the PID controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| TD |  | +8.0 | REAL | 0.0 | PID_CON.TD displays the derivative action time of the PID controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| PI_CON_OLD | 120.0 |  | STRUCT |  | The PI_CON_OLD structure contains the old parameters of the PI controller. |
| GAIN |  | +0.0 | REAL | 1.5 | The old proportional gain of the PI controller is displayed at the PI_CON_OLD.GAIN output. |
| TI |  | +4.0 | REAL | 3600.0 | The old integral action time of the PI controller is displayed at the PI_CON_OLD.TI output. |
| PID_CON_OLD | 128.0 |  | STRUCT |  | The PID_CON_OLD structure contains the old parameters of the PID controller. |
| GAIN |  | +0.0 | REAL | 0.0 | The old proportional gain of the PID controller is displayed at the PID_CON_OLD.GAIN output. |
| TI |  | +4.0 | REAL | 0.0 | The old integral action time of the PID controller is displayed at the PID_CON_OLD.TI output. |
| TD |  | +8.0 | REAL | 0.0 | The old derivative action time of the PID controller is displayed at the PID_CON_OLD.TD output. |
| TU | 140.0 |  | REAL | 0.0 | The determined delay time is displayed at the TU output. |
| TA | 144.0 |  | REAL | 0.0 | The determined recovery time is displayed at the TA output. |

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)

### In/out parameters TUN_EC (S7-300, S7-400)

| Parameter | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| ADAPT1ST | 148.0 | BOOL | FALSE | When you carry out the first optimization of the process or do not wish to use the results of previous optimizations such as manipulated value step size or filter time constants, you must carry out a first adaption. To do this, set ADAPT1ST = TRUE. The Self-Tuner then carries out an initialization routine and in the process sets the default values described in the initialization routine. The Self-Tuner sets ADAPT1ST back to FALSE.  It does not make sense to set ADAPT1ST to TRUE at a restart of the CPU in OB100. |
| ADAPT_ON | 148.1 | BOOL | FALSE | If you want to trigger on-line adaption, set ADAPT_ON = TRUE. If the subsequent setpoint step-change is greater than MIN_STEP, identification is started (PHASE = 2). The Self-Tuner sets ADAPT_ON back to FALSE. |
| STEADY | 148.2 | BOOL | FALSE | When the process value has reached a steady state, you can use STEADY to terminate optimization prematurely, even though the Self-Tuner is still in PHASE 3.  You can also use STEADY to carry out a renewed controller design in steady state, after the Self-Tuner has passed into PHASE 4. |
| COOLID_ON | 148.3 | BOOL | FALSE | If you want to trigger cooling tuning, set COOLID_ON = TRUE. The manipulated value is set to LLLM_TUN and COOLID_ON is reset to FALSE.  If there are multiple heating zones, all pretuning and adaptations should have been completed before cooling tuning is started. |
| UNDO_PAR | 148.4 | BOOL | FALSE | The old controller parameters are transferred to the current controller parameters and are active immediately depending on PID_ON.  PI_CON = PI_CON_OLD  PID_CON = PID_CON_OLD    The function for undoing changes can only be used in automatic mode (PHASE 4). |
| SAVE_PAR | 148.5 | BOOL | FALSE | The current controller parameters are transferred to the old controller parameters.  PI_CON_OLD = PI_CON  PID_CON_OLD = PID_CON |
| LOAD_PAR | 148.6 | BOOL | FALSE | The changed parameters PI_CON and PID_CON are transferred to the controller and are thus active. |
| CONZ_ON | 148.7 | BOOL | FALSE | If CONZ_ON = TRUE, the controller operates with a control zone.  During controller optimization the Self-Tuner decides whether controlling is carried out with or without control zone and determines an optimum control zone. After optimization has been carried out in PHASE 4 you can de-activate the control zone with CONZ_ON = FALSE or re-configure the control zone. |
| CON_ZONE | 150.0 | REAL | 0.0 | CON_ZONE specifies the width of the control zone.  During controller optimization the Self-Tuner decides whether controlling is carried out with or without control zone and determines an optimum control zone. After optimization has been carried out in PHASE 4 you can de-activate the control zone with CONZ_ON = FALSE or re-configure the control zone. |

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Parameter TUN_EC.PHASE (S7-300, S7-400)

| PHASE | Mode | Description |
| --- | --- | --- |
| 0 | Automatic mode: Close-loop control with preset parameters | During the generation of an instance DB for the Self-Tuner, zero is initially assigned to the parameter PHASE. Since TRUE is initially assigned to MAN_ON, the Self-Tuner will change to PHASE 7 (manual mode) after the first run. You can start the first adaption directly from manual mode (ADAPT_ON = TRUE) or change over to automatic mode. When you change over to automatic mode MAN_ON = FALSE for the first time, the parameters are read in from PI_CON. The default values for GAIN and TI are: GAIN = 1.5, TI = 1h. |
| 2 | Controller optimization: Searching for point of inflection with constant manipulated value | As soon as you specify a setpoint step-change ≥ MIN_STEP in the positive direction to the operating point of the warm process state, LHLM_TUN is assigned to MAN_OUT during the first adaption, while a value calculated by Self-Tuner is assigned to MAN_OUT during on-line adaption. QMAN_ON = TRUE is also set. Both values are transferred to the PID controller. The PID controller is controlled with them in manual mode. MIN_STEP should be greater than 10% of the operating range of the setpoint and the process value. |
| 3 | Controller optimization: Closed-loop control with a PI coarse controller | If the point of inflection of the step response is recognized (STATUS_H = 2) or if the process value has reached 70% of the setpoint step height (STATUS_H = 3), a prudently set PI controller is designed. The controller gain GAIN is limited to the range of 0.2 to 20.0. The controller operates immediately as a PI controller and tries to settle the process to a steady state. The Self-Tuner saves the newly determined PI controller parameters in GAIN, TI and PI_CON. The previous values of the PI controller are saved in PI_CON_OLD. If it takes a long time until the steady state is reached (creeping transient response during temperature processes) you can initiate the control design with the current data when the state is almost steady by setting STEADY = TRUE. You can also re-initiate the controller design with the current data at a later stage in Phase 3 or 4 by specifying STEADY = TRUE. This often improves the controller design further.  If an overshoot occurs or if no point of inflection is found, the cause may be that the manipulated value step size LHLM_TUN was selected too large during the first adaption. This does not necessarily produce a bad controller setting. You should select LHLM_TUN approx. 20% smaller at the next first adaption.  If the block has recognized the steady state or if the period 30 × TI (TI: Integral-action time of the PI controller set under PHASE = 3) has passed since the setpoint step-change, an improved controller design is realized and the system changes over to PHASE = 4. The Self-Tuner saves the newly determined PI/PID controller parameters in GAIN, TI, TD and PI_CON or PID_CON. The previous values of the PID controller are saved in PID_CON_OLD. If possible, a PID controller and a PI controller are designed. If PID_ON = TRUE, the PID controller is activated, otherwise the PI controller is activated. In PHASE 4 you can switch over bumplessly at any time between the two controllers. The controller gain GAIN is limited in such a manner that the loop gain of the open loop (product of the process gain and the controller gain) lies under 80.0. |
| 4 | Automatic mode: Normal closed-loop control with/without control zone | In this phase the controller controls with its optimized parameters. From this state, you can start cooling tuning, fine tuning or pretuning. |
| 5 | Automatic mode: Structure switchover at setpoint step-change: I-action deactivated, P(D) control | In the case of a positive setpoint step-change ≥ MIN_STEP the I-action of the controller is de-activated temporarily and the gain is increased slightly, so that a pure P(D) controller is used. In setpoint proximity the I-action is re-activated and the gain is reduced again |
| 6 | Automatic mode: Structure switchover at setpoint step-change: Predictive manipulated value specification | Processes with a high time lag cannot be controlled well with a P(D) control system. After a positive setpoint step-change ≥ MIN_STEP, the steady state manipulated variable required for the new setpoint is therefore output as a constant. In setpoint proximity the system changes back bumplessly to PI or PID controller operating mode. This results in a slow action that is, however, free of overshooting. |
| 7 | Manual mode | If you set the input MAN_ON to TRUE, the output QMAN_ON is set to TRUE and the output MAN_OUT to MAN. This changes the PID controller over to manual mode.  Manual mode takes priority over all other operating modes.  Pretuning, fine tuning and cooling tuning are aborted. When manual operation is disabled (MAN_ON = FALSE), the controller changes over to automatic mode (PHASE = 4 in the operation of the Self-Tuner) and controls with the existing controller parameters. |

#### Heating Optimization Phases during First Adaption

![Heating Optimization Phases during First Adaption](images/26323273227_DV_resource.Stream@PNG-en-US.png)

#### Cooling tuning phases

![Cooling tuning phases](images/26300800907_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Parameter TUN_EC.STATUS_H (S7-300, S7-400)

| STATUS_H | Description | Remedy |
| --- | --- | --- |
| 0 | Initialization |  |
| 1 | Point of inflection too low  In most cases optimization still results in good controller parameters | To get closer the ideal case, increase LHLM_TUN or decrease the setpoint step-change size. |
| 2 | Ideal case:  Point of inflection found |  |
| 3 | Point of inflection too high  A safety factor is included. In most cases optimization leads to controller parameters that can still be used but are prudent. | To get closer the ideal case, decrease LHLM_TUN or increase the setpoint step-change size. |
| 11, 12 | The time lag could not be detected correctly. Operation continues with an estimated value that can lead to controller parameters that are not optimum.  If the process has a pure **VZ1 behavior** (no time lag), the Self-Tuner can often design good controller parameters that are still good. Since calculation is continued with a roughly estimated time lag, it is possible that STATUS_D cannot be determined to 1 (controller for approximating VZ1 behavior) and that the control zone is de-activated, although a control zone makes sense for VZ1 processes. | Repeat optimization and ensure that disturbances do not occur at the process value.  If you are not satisfied with the controller parameters, you can at least use the values from PROCESS.GAIN and PROCESS.TM_LAG1 for a VZ1 model and use your own controller design in accordance with the text book. |
| 13 | The time lag could not be detected correctly. Operation continues with an estimated value that can lead to controller parameters that are not optimum. | Repeat optimization and ensure that disturbances do not occur at the process value. |

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Parameter TUN_EC.STATUS_C (S7-300, S7-400)

| STATUS_C | Description | Remedy |
| --- | --- | --- |
| 0 | Initialization |  |
| 1 | Turning point was not found.  In most cases, optimization still results in good controller parameters. | To get closer to the ideal case, increase LLLM_TUN  (for example from -20.0 to -10.0) |
| 2 | Ideal case:  Cooling point of inflection found |  |
| 11, 12, 13 | Incorrect estimate  The ratio factor is set to the default value: RATIOFAC = 1.0 | Repeat optimization and ensure that disturbances do not occur at the process value. |

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_D (S7-300, S7-400)](#parameter-tun_ecstatus_d-s7-300-s7-400)

### Parameter TUN_EC.STATUS_D (S7-300, S7-400)

| STATUS_D | Description | Remedy |
| --- | --- | --- |
| 0 | Initialization |  |
| 1 | The process has almost PT1 behavior; | you can possibly waive the D-action of the contoller. |
| 2 | PI and PID controllers possible, VZ2 behavior |  |
| 3 | Separate PID controller design for very high delay times, dead times or high process order  In this case the control zone is switched off. |  |
| 4 | Incorrect estimate   No controller design for on-line adaption.  During the first adaption the process is continued with the coarse PI controller from PHASE 3. | Repeat optimization and ensure that disturbances do not occur at the process value. |

---

**See also**

[Description TUN_EC (S7-300, S7-400)](#description-tun_ec-s7-300-s7-400)
  
[Scope of TUN_EC (S7-300, S7-400)](#scope-of-tun_ec-s7-300-s7-400)
  
[Mode of operation TUN_EC (S7-300, S7-400)](#mode-of-operation-tun_ec-s7-300-s7-400)
  
[Input parameters TUN_EC (S7-300, S7-400)](#input-parameters-tun_ec-s7-300-s7-400)
  
[Output parameters TUN_EC (S7-300, S7-400)](#output-parameters-tun_ec-s7-300-s7-400)
  
[In/out parameters TUN_EC (S7-300, S7-400)](#inout-parameters-tun_ec-s7-300-s7-400)
  
[Parameter TUN_EC.PHASE (S7-300, S7-400)](#parameter-tun_ecphase-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_H (S7-300, S7-400)](#parameter-tun_ecstatus_h-s7-300-s7-400)
  
[Parameter TUN_EC.STATUS_C (S7-300, S7-400)](#parameter-tun_ecstatus_c-s7-300-s7-400)

## TUN_ES (S7-300, S7-400)

This section contains information on the following topics:

- [Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
- [Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
- [Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
- [Structure switchover (S7-300, S7-400)](#structure-switchover-s7-300-s7-400)
- [Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
- [Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
- [In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
- [Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
- [Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
- [Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Description TUN_ES (S7-300, S7-400)

The TUN_ES instruction is used to tune a PID step controller. Depending on the controller, you interconnect TUN_ES with one of the following instructions:

- FM 355 S or FM 455 S

  - PID_FM
- PID Basic Functions

  - CONT_S
  - TCONT_S
- Standard PID Control (PID Professional optional package)

  - PID_ES
- Modular PID Control (PID Professional optional package)

  - PID
  - LMNGEN_S

#### Call

TUN_ES is called in the constant time base of the cycle time of the calling OB (preferably in a cyclic interrupt OB).

When ADAPT1ST = TRUE , the initialization routine of the TUN_ES instruction is run. The following preassignments are made:

- The system switches to PI controller. The parameters of PI_CON are transferred to the controller for this purpose. If the PI_CON.GAIN and PI_CON.TI parameters both have the value 0.0, they are preassigned with PI_CON.GAIN = 1.5 and PI_CON.TI = 3600.0 s.
- PROCESS.GAIN = 999.0
- STATUS_H = 0; STATUS_D = 0

  > **Note**
  >
  > Unless explicitly required, do **not** call TUN_ES during a warm restart of the CPU in its initialization routine as is usual for other instructions. If you do, all process parameters will be lost.

#### CYCLE sampling time

You enter the sampling time in the CYCLE parameter. The sampling time should not exceed 10% of the determined integral action time of the controller. In addition, the sampling time should not exceed 1% of the motor transition time so that the position feedback has a resolution of at least 1%. You can set the sampling time in the CYCLE parameter of the TUN_ES instruction and the controller. It must agree with the time difference between two calls (cycle time of the cyclic interrupt OB taking into account the reduction ratios).

In connection with the FM355/455 controller modules, the sampling time of TUN_ES must be approximately equal to the resulting cycle time of the controllers on the FM (Parameter setting &gt; Module parameters).

#### Reaction to error

The error message word RET_VAL is not evaluated by the block.

---

**See also**

[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Scope of TUN_ES (S7-300, S7-400)

The Self-Tuner can be used particularly well for:

- Temperature control systems, but also for
- Level control systems and
- Flow control systems

In the case of flow control systems a distinction must be made as to whether only the control valve itself is to be controlled or whether a process with associated delay follows the control valve. In the case of control valve control only, the Self-Tuner cannot be used.

#### Process requirements

The process must meet the following requirements:

- **Stable asymptotic transient response with associated delay**

  The process value must settle to steady state after a manipulated variable jump. This therefore excludes processes that already exhibit an oscillating response in the absence of closed-loop control, as well as controlled systems without inherent regulation (integrator in the controlled system).
- **Delay times not too large**

  The range of application can be specified based on the ratio of the delay time t<sub>u</sub> and response time t<sub>a</sub>. The delay time also encompasses any existing dead time.

  The pretuning or adaptation is designed for the range t<sub>u</sub> &lt; 1/10 t<sub>a</sub>, within which most controlled temperature systems fall.

  For the range of especially long delay times 1/10 t<sub>a</sub> &lt; t<sub>u</sub> &lt; 1/3 t<sub>a</sub>, the design of a utilizable PI controller is generally still also possible.
- **Adequate linear response across a sufficiently large operating range**

  This means that non-linear effects within this operating range can be ignored both during identification and during normal closed-loop control operation. However, it is possible to re-identify the process when there is a change from one operating point to another if the adaptation process is carried out again close to the new operating point and provided that the non-linearity is not passed through during adaptation.

  If certain static non-linearities (e.g., valve characteristic curves) are known, it is always advisable to compensate for them in advance with a polyline in order to linearize the process response.
- **Minimal disturbances in temperature processes**

  Disturbances such as thermal transfer to neighboring zones or heat gains or losses due to changes from one state of matter to another must not influence the overall temperature process to any great extent. If necessary, adaptation at the operating point may be necessary. For example, when zones of an extruder are tuned, all zones must be heated up simultaneously.
- **Quality of the measuring signals**

  The quality of the measured signals has to be sufficient; in other words, the signal-to-disturbance ratio has to be sufficiently high.
- **Process gains not too high**

  The process gains must not be too high. Normalization of the process values is not required. The process gain K can thus include physical units, such as:

  K =∆PV/∆LMN, [K]= °C/%

  The final controller design is based on a calculation of the process gain K and can thus in principle compensate for any values of K. However, K is initially unknown during the learning phase and overshoots cannot be avoided when there are extreme combinations of gain and learning step changes. The overshoot is also reduced by reducing the parameter LHLM_TUN in the heating process or by increasing LLLM_TUN in the cooling process.

#### Requirements for processes with a control valve with integral action

In processes with control valves with an integral action, further requirements must be met in addition to those specified above:

The motor run time of the control valve must be less than the time required to find a point of inflection after a manipulated variable jump (also refer to the process response figure). If this is not the case, the process involved is often a flow rate control system in which only the control valve is effective as the dominating process action. It is not advisable to use the Self-Tuner in this case. You can then set the PI step controller manually in accordance with the following rule of thumb:

GAIN = 1, TI = Motor transition time

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Mode of operation TUN_ES (S7-300, S7-400)

TUN_ES has the following functions for the control or tuning of the controller:

- **Manual mode**

   The Self-Tuner forces the controller into manual mode and transfers its manual parameters to it. In the case of step controllers with position feedback you can specify the manual value in floating point format and manual value signals such as open/close. In the case of step controllers without position feedback you can only specify the manual value signals.
- **Controller tuning**

  During tuning of the controller parameters, the actuating time of the actuator is measured and then the controlled system is identified. A controller is designed based on the characteristics of the controlled system. The new controller parameters are calculated on this basis and activated for the controller.

  - **First adaption**

    Pretuning can only be carried out for a positive setpoint jump. It is usually used during initial commissioning or in case of a serious change in the controlled system characteristics.
  - **Fine tuning**

     The controller can be fine tuned online during a positive setpoint jump when there is a change from one operating point to another or when there are changes in the process response. Fine tuning is only possible for step controllers with position feedback.
- **Tuning the response to setpoint changes**

  The controller is designed for optimum disturbance response, in principle. The resulting "stringent" parameters would result in overshoots of 10% to 20% of the jump height at setpoint jumps.

  The **structure segmentation** represents an initial remedy. In this case, the proportional or derivative action is located in the feedback loop. A change in the setpoint thus only acts on the integral action of the controller. Structure segmentation may only be used for step controllers with position feedback.

  If structure segmentation is not possible for the controller, the following function can be activated in order to tune the response to setpoint changes:
- **Structure switchover**

  Changeover to a quasi P(D) closed-loop control or predictive manipulated variable specification at large positive setpoint jumps. In the case of step controllers without position feedback, it is only possible to change over to a quasi P(D) closed-loop control.
- **Saving the controller parameters**

   If you assess the current controller parameters to be usable, you can save these before a manual change of the controller parameters in parameters specially provided in the instance data block of the Self-Tuner. If you tune the controller, the saved parameters are overwritten by the values that were valid prior to tuning.
- **Reloading saved controller parameters**

  The last controller parameter settings you saved can be activated for the controller again using this function.
- **Changing the controller parameters**

   If you want to set the controller parameters yourself for the controller, you can assign these through special parameters in the instance DB of the Self-Tuner and transfer them to the controller by means of this function.

No cooling tuning and no control zone mode can be implemented with TUN_ES.

#### Enabling the functions

| Function | Start bit | Enable bit | Start condition:  PHASE | Start condition:  Setpoint jump at SP |
| --- | --- | --- | --- | --- |
| Manual mode | — | MAN_ON  LMNS_ON | 0 to 7 | — |
| Pretuning with measurement of the motor transition time | ADAPT1ST | — | 0, 4 | Pos.: &gt; MIN_STEP |
| Pretuning without measurement of the actuating time of the actuator or fine tuning (only possible for step controller without position feedback) | ADAPT_ON | — | 4 | Pos.: &gt; MIN_STEP |
| Structure switchover | — | STRUC_ON | 4 | Pos.: &gt; MIN_STEP  Neg: &gt; MIN_STEP |
| Save controller parameters | SAVE_PAR | — | 2 to 7 | — |
| Reload controller parameters | UNDO_PAR | — | 4 | — |
| Change controller parameters | LOAD_PAR | — | 4 | — |

> **Note**
>
> Start bits are reset after the function has been started successfully. Enable bits remain set.

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Structure switchover (S7-300, S7-400)

#### Structure segmentation

Structure segmentation is a function of the controller. In the case of closed-loop control with structure segmentation, the proportional or derivative action lies within the feedback loop, so that a change in the setpoint only acts on the integral action of the controller. When setpoint jumps occur, the manipulated variable does not undergo a jump change but instead follows a ramp-shaped course.

The disturbance response is not changed as a result.

![Closed-loop control with structure segmentation](images/30631088395_DV_resource.Stream@PNG-en-US.png)

Closed-loop control with structure segmentation

In the case of closed-loop control without structure segmentation, the proportional and derivative actions lie within the control deviation, just like the integral action. You can select a structure switchover for this operating mode (STRUC_ON = TRUE).

Closed-loop control with structure segmentation is possible in the following control packages:

- FM355/455
- Standard PID Control
- Modular PID Control

  > **Note**
  >
  > - Structure segmentation must not be used if no position feedback of the control valve is available. This means that you must leave the proportional and derivative actions within the control deviation.
  > - In closed-loop control with structure segmentation, the dead band in the control deviation is almost without effect.
  > - With CONT_S and TCONT_S, only closed-loop control without structure segmentation is possible.

#### Structure switchover when proportional and derivative actions are within the control deviation

The structure switchover is deactivated in the default setting. It should only be selected if structure segmentation is not available. You can activate the structure switchover with STRUC_ON = TRUE. The block automatically selects between two control measures depending on the total loop gain (product of the process gain and the controller gain):

- Integral action temporarily increased, quasi P(D) control:

  In the case of a positive setpoint jump ≥ MIN_STEP, the integral action of the controller is increased temporarily by a significant amount and the gain is decreased slightly, which means that a quasi P(D) controller is used. In the proximity of the setpoint, the system is switched back to the original values for the integral action and the gain (PHASE = 5).
- Temporary predictive manipulated variable specification:

  Processes with long delay times cannot be controlled well with a P(D) control system. After a positive setpoint jump ≥ MIN_STEP, the manipulated variable required constantly for the new setpoint is therefore output constantly. In the proximity of the setpoint, the system is switched back bumplessly to PI or PID closed-loop control. This results in a slow, but overshoot-free response (PHASE = 6).

  > **Note**
  >
  > In the case of step control without position feedback, only the first control measure (PHASE = 5) is possible.
  >
  > If you do not achieve good results (transient response is slow) with the structure switchover in the case of positive setpoint jumps (for example, during heating processes), you can deactivate the structure switchover with STRUC_ON = FALSE, on the condition that small overshoots may occur.

| Controller structure modes | PFDB_SEL, DFDB_SEL <sup>1)</sup> | STRUC_ON |
| --- | --- | --- |
| Activate structure segmentation | TRUE | FALSE |
| Activate structure switchover | FALSE | TRUE |

<sup>1)</sup> Controller parameters PFDB_SEL, DFDB_SEL: With CONT_S, these parameters are not available. This corresponds to the PFDB_SEL = DFDB_SEL = FALSE setting (without structure segmentation).

> **Note**
>
> - Structure segmentation prevents overshooting of the controlled variable when setpoint jumps occur. Select structure segmentation if possible.
> - If the controller does not allow structure segmentation, activate structure switchover. The structure switchover must not be activated at the same time as the structure segmentation. You can deactivate structure switchover if rapid tuning is required and small overshoots are permitted at positive setpoint jumps.

### Input parameters TUN_ES (S7-300, S7-400)

| Parameter | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP | 0.0 | REAL | 0.0 | Enter the setpoint at the SP input. It is interconnected with the controller via SP_OUT. Note that the setpoint must lie within the setpoint limits of the controller. |
| PV | 4.0 | REAL | 0.0 | PV is interconnected with the process value of the controller. |
| MAN | 8.0 | REAL | 0.0 | Enter the manual value at the MAN input. If MAN_ON = TRUE, the manual value MAN is transferred to the manipulated variable of the controller. When MAN_ON = TRUE and MAN = 0.0, the heating is off. If MAN_ON = FALSE, the manipulated variable is specified by the controller.  Values from -100 to 100% are permitted. |
| LMNR | 12.0 | REAL | 0.0 | LMNR is interconnected with the position feedback of the controller (if any).  Values from 0.0 to 100% are permitted. |
| MIN_STEP | 16.0 | REAL | 10.0 | You can specify the minimum setpoint jump above which pretuning or adaptation can be carried out in the MIN_STEP input.  If structure switchover (STRUC_ON=TRUE) is activated, the setpoint jump must be greater than MIN_STEP in order for the structure switchover activation to take place.  Recommendation: MIN_STEP ≥ 10 % of the required setpoint/process value range |
| LHLM_TUN | 20.0 | REAL | 80.0 | At the LHLM_TUN input, specify the manipulated variable jump for the first setting. The manipulated variable jump is calculated automatically during subsequent fine tuning.  Values from 0.0 to 100% are permitted. |
| NORM_FAC | 24.0 | REAL | 1.0 | A normalization factor is applied for controllers with a normalized controller gain (Standard PID Control). The normalization factor is calculated on the basis of the range limits of the process value of the controller and is interconnected with the NORM_FAC input. |
| PULSE_TM | 28.0 | TIME | 0 ms | PULSE_TM is interconnected with the minimum pulse duration of the controller.  PULSE_TM ≥ 1 ms |
| C_LMNUP | 32.0 | BOOL | FALSE | C_LMNUP is interconnected with the manipulated variable signal QLMNUP of the controller. |
| C_LMNDN | 32.1 | BOOL | FALSE | C_LMNDN is interconnected with the manipulated variable signal QLMNDN of the controller. |
| MAN_ON | 32.2 | BOOL | FALSE | If MAN_ON = TRUE, the manipulated variable of the controller is specified via the MAN input. If MAN_ON = FALSE, the manipulated variable is specified by the controller. |
| LMNR_HS | 32.3 | BOOL | FALSE | LMNR_HS is interconnected with the endstop signal LMNR_HR of the controller. |
| LMNR_ON | 32.4 | BOOL | FALSE | If LMNR_ON = TRUE, you can use LMNS_ON = TRUE or MAN_ON = TRUE to switch a step controller with position feedback over to manual mode.   If LMNR_ON = FALSE, you can use LMNS_ON = TRUE to switch a step controller without position feedback over to manual mode. |
| LMNS_ON | 32.5 | BOOL | TRUE | If LMNS_ON is set, you can use the LMNUP and LMNDN parameters to manipulate the actuating signals of the controller. |
| LMNUP | 32.6 | BOOL | FALSE | You can use LMNUP to manipulate the actuating signal OPEN of the controller. |
| LMNDN | 32.7 | BOOL | FALSE | You can use LMNDN to manipulate the actuating signal CLOSE of the controller. |
| PID_ON | 33.0 | BOOL | FALSE | You can specify at the PID_ON input whether the tuned controller is to operate as a PI controller or a PID controller.  PID controller: PID_ON = TRUE  PI controller: PID_ON = FALSE  With certain controlled system types, however, it is possible that only a PI controller will be designed, despite PID_ON = TRUE. |
| STRUC_ON | 33.1 | BOOL | FALSE | If STRUC_ON = TRUE, a structure switchover (from PI(D) to P(D) control) ensures that overshoots are largely avoided at setpoint jumps. The STRUC_ON input must not be set = TRUE if the proportional action or derivative action is fed into the feedback loop of the controller. |
| WRITE_DIS | 33.2 | BOOL | FALSE | In connection with the controller module, the Self-Tuner must know whether the driver block is ready to send data to the FM. This is the case if LOAD_OP = LOAD_PAR = FALSE. The result of the OR operation of LOAD_OP and LOAD_PAR is interconnected with WRITE_DIS. |
| CYCLE | 34.0 | TIME | 100 ms | The sampling time must be configured in the CYCLE input. CYCLE must correspond to the sampling time of the controller to be set and the time difference between two calls (cycle time of the cyclic interrupt OB taking into account the reduction ratios).  ≥ 1 ms |

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Output parameters TUN_ES (S7-300, S7-400)

| Parameter | Address |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| MAN_OUT | 38.0 |  | REAL | 0.0 | MAN_OUT is connected to the manual input value of the controller. If MAN_ON = TRUE, the Self-Tuner outputs the value specified at the MAN input to the MAN_OUT output. |
| SP_OUT | 42.0 |  | REAL | 0.0 | SP_OUT is connected to the setpoint input of the controller. The Self-Tuner writes the setpoint specified at the SP input to the SP_OUT output. If manual mode MAN_ON = TRUE, the setpoint is tracked to the process value: SP_OUT = PV. |
| GAIN | 46.0 |  | REAL | 1.5 | GAIN is interconnected with the proportional gain (controller gain) of the controller. |
| TI | 50.0 |  | TIME | 1 h | TI is interconnected with the integral action time (reset time) of the controller. |
| TD | 54.0 |  | TIME | 0 ms | TD is interconnected with the derivative action time (rate time) of the controller. |
| TM_LAG | 58.0 |  | TIME | 1 s | TM_LAG is interconnected with the time lag of the controller differentiator. |
| MTR_TM | 62.0 |  | TIME | 30 s | MTR_TM is interconnected with the motor run time of the controller. |
| DEADB_W | 66.0 |  | REAL | 0.0 | DEADB_W is interconnected with the dead band width of the controller. |
| PHASE | 70.0 |  | INT | 0 | [Parameter TUN_ES.PHASE](#parameter-tun_esphase-s7-300-s7-400) displays the current sequence of the controller tuning. During the tuning of Standard PID Control, the PHASE output is interconnected with the PHASE input of the PID_ES instruction. |
| STATUS_H | 72.0 |  | INT | 0 | [Parameter TUN_ES.STATUS_H](#parameter-tun_esstatus_h-s7-300-s7-400) displays tuning results regarding the search for the point of inflection during the heating process. |
| STATUS_D | 74.0 |  | INT | 0 | [Parameter TUN_ES.STATUS_D](#parameter-tun_esstatus_d-s7-300-s7-400) displays tuning results regarding the controller design during the heating process. |
| QMAN_ON | 76.0 |  | BOOL | FALSE | QMAN_ON is interconnected with the manual/automatic changeover of the controller. |
| QLMNS_ON | 76.1 |  | BOOL |  | QLMNS_ON is interconnected with the "Enable manipulated signals" parameter of the controller |
| QLMNUP | 76.2 |  | BOOL |  | QLMNUP is interconnected with the "Manipulated signal open" parameter of the controller |
| QLMNDN | 76.3 |  | BOOL |  | QLMNDN is interconnected with the "Manipulated signal close" parameter of the controller |
| QI_SEL | 76.4 |  | BOOL | TRUE | QI_SEL is interconnected with the on/off switch of the controller integral action I_SEL.  In the case of FM355/455, TI must be switched to zero depending on QI_SEL: If QI_SEL = FALSE, then TI = 0. |
| QD_SEL | 76.5 |  | BOOL | FALSE | QD_SEL is interconnected with the on/off switch of the controller derivative action D_SEL.  In the case of FM355/455, TD must be switched to zero depending on QD_SEL: If QD_SEL = FALSE, then TD = 0. |
| QWRITE | 76.6 |  | BOOL | FALSE | QWRITE is interconnected with the LOAD_PAR and LOAD_OP inputs of the PID_FM instruction of FM355/455.  As a result, the data records of the controller channel are downloaded to the FM. |
| PROCESS | 78.0 |  | STRUCT |  | The PROCESS structure contains the parameters of the process. |
| GAIN |  | +0.0 | REAL | 999.0 | The process gain is displayed in the PROCESS.GAIN output. |
| TM_LAG1 |  | +4.0 | REAL | 0.0 | The slow process time constant is displayed at the PROCESS.TM_LAG1 output. |
| TM_LAG2 |  | +8.0 | REAL | 0.0 | The fast process time constant is displayed at the PROCESS.TM_LAG2 output. |
| PV00 |  | +12.0 | REAL | 0.0 | The zero mean value of the process is displayed at the PROCESS. PV00 output.  The zero mean value is the steady-state process value when manipulated variable = zero. This corresponds to the ambient temperature when the system is cold. |
| KIG |  | +16.0 | REAL | 0.0 | The maximum rise ratio of the process value during heating is displayed in the PROCESS.KIG output. |
| MTR_TM |  | +20.0 | REAL | 0.0 | The motor run time is displayed at the MTR_TM output. |
| PI_CON | 102.0 |  | STRUCT |  | The PI_CON structure contains the parameters of the PI controller. |
| GAIN |  | +0.0 | REAL | 1.5 | PI_CON.GAIN displays the proportional gain of the PI controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| TI |  | +4.0 | REAL | 3600.0 | PI_CON.TI displays the integral action time of the PI controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| PID_CON | 110.0 |  | STRUCT |  | The PID_CON structure contains the parameters of the PID controller. |
| GAIN |  | +0.0 | REAL | 0.0 | PID_CON.GAIN displays the proportional gain of the PID controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| TI |  | +4.0 | REAL | 0.0 | PID_CON.TI displays the integral action time of the PID controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| TD |  | +8.0 | REAL | 0.0 | PID_CON.TD displays the derivative action time of the PID controller. You can improve the value manually and make it effective by setting LOAD_PAR. |
| PI_CON_OLD | 122.0 |  | STRUCT |  | The PI_CON_OLD structure contains the old parameters of the PI controller. |
| GAIN |  | +0.0 | REAL | 1.5 | The old proportional gain of the PI controller is displayed at the PI_CON_OLD.GAIN output. |
| TI |  | +4.0 | REAL | 3600.0 | The old integral action time of the PI controller is displayed at the PI_CON_OLD.TI output. |
| PID_CON_OLD | 130.0 |  | STRUCT |  | The PID_CON_OLD structure contains the old parameters of the PID controller. |
| GAIN |  | +0.0 | REAL | 1.5 | The old proportional gain of the PID controller is displayed at the PID_CON_OLD.GAIN output. |
| TI |  | +4.0 | REAL | 3600.0 | The old integral action time of the PID controller is displayed at the PID_CON_OLD.TI output. |
| TD |  | +8.0 | REAL | 0.0 | The old derivative action time of the PID controller is displayed at the PID_CON_OLD.TD output. |
| TU | 142.0 |  | REAL | 0.0 | The determined delay time is displayed at the TU output. |
| TA | 146.0 |  | REAL | 0.0 | The determined recovery time is displayed at the TA output. |

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)

### In/out parameters TUN_ES (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| ADAPT1ST | 150.0 | BOOL | FALSE | When you carry out the first optimization of the process or do not wish to use the results of previous optimizations such as manipulated value step size or filter time constants, you must carry out a first adaption. To do this, set ADAPT1ST = TRUE. The Self-Tuner then carries out an initialization routine and, in the process, sets the default values described in the initialization routine. The Self-Tuner sets ADAPT1ST back to FALSE.  It does not make sense to set ADAPT1ST to TRUE at a restart of the CPU in OB100. |
| ADAPT_ON | 150.1 | BOOL | FALSE | If you want to trigger on-line adaption, set ADAPT_ON = TRUE. If the subsequent setpoint step-change is greater than MIN_STEP, identification is started (PHASE = 2). The Self-Tuner sets ADAPT_ON back to FALSE. |
| STEADY | 150.2 | BOOL | FALSE | When the process value has reached a steady state, you can use STEADY to terminate optimization prematurely, even though the Self-Tuner is still in PHASE 3.  After the Self-Tuner has passed into PHASE 4, you can also use STEADY to carry out a renewed controller design in steady state. |
| UNDO_PAR | 150.3 | BOOL | FALSE | The old controller parameters are transferred to the current controller parameters and are active immediately depending on PID_ON.  PI_CON = PI_CON_OLD  PID_CON = PID_CON_OLD   The function for undoing changes can only be used in automatic mode (PHASE 4). |
| SAVE_PAR | 150.4 | BOOL | FALSE | The current controller parameters are transferred to the old controller parameters.  PI_CON_OLD = PI_CON  PID_CON_OLD = PID_CON |
| LOAD_PAR | 150.5 | BOOL | FALSE | The changed parameters PI_CON and PID_CON are transferred to the controller and are thus active. |

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Parameter TUN_ES.PHASE (S7-300, S7-400)

| PHASE | Mode | Description |
| --- | --- | --- |
| 0 | Automatic mode: Close-loop control with preassigned parameters | During the generation of an instance DB for the Self-Tuner, thePHASE parameter is pre-assigned with zero. Since LMNS_ON is pre-assigned with TRUE, the Self-Tuner will switch to PHASE 7 (manual mode) after the first run. You can start the pretuning directly from manual mode (ADAPT_ON = TRUE) or switch to automatic mode. When you switch to automatic mode MAN_ON = FALSE for the first time, the parameters of PI_CON are applied. The default values for GAIN and TI are: GAIN = 1.5, TI = 1h.  Exiting from the phase via MAN_ON, LMNS_ON, or ADAPT1ST |
| 1 | Controller tuning: Heating off and waiting for a setpoint jump | After tuning has been started with ADAPT1ST = TRUE, the Self-Tuner closes the control valve (manipulated variable = 0 or LMNS_ON = LMNDN = TRUE) and waits for a positive setpoint jump ≥ MIN_STEP. |
| 2 | Controller tuning: Motor transition time measurement, moving to a constant control valve setting and searching for point of inflection | As soon as you specify a setpoint jump ≥ MIN_STEP in the positive direction to the operating point of the warm process state, with pretuning MAN_OUT is set to LHLM_TUN and with fine tuning MAN_OUT is set to a value calculated by the self-tuner. MIN_STEP should be greater than 10% of the operating range of the setpoint and the process value.  In the case of step control with position feedback (LMNR_ON = TRUE), the value TRUE is assigned to QMAN_ON. The controller controls the valve to the value of MAN_OUT, and TUN_ES calculates the motor transition time MTR_TM.  In the case of step control without position feedback, QLMNS_ON and QLMNUP are set to TRUE, and the valve is moved to the high endstop position. When the high endstop is reached (LMNR_HS =TRUE), TUN_ES calculates the motor transition time and forwards it to the controller. The valve is then moved toward the closed position until the value of MAN_OUT is reached (QLMNDN = TRUE). |
| 3 | Controller tuning: Closed-loop control with a PI coarse controller | When the point of inflection of the jump response is recognized (STATUS_H = 2) or when the process value has reached 70% of the setpoint jump height (STATUS_H = 3), a PI controller with conservative settings is designed. The controller gain GAIN is limited to the range from 0.2 to 20.0. As of this point, the controller immediately starts working as a PI controller and attempts to bring the controlled system to a steady-state condition. The Self-Tuner stores the newly determined PI controller parameters in GAIN, TI, and PI_CON. The previous values of the PI controller are saved in PI_CON_OLD. If it takes a long time to reach steady-state condition (creeping transient response during temperature processes), you can set STEADY = TRUE to initiate controller design with the current data when steady-state condition is almost reached. You can also set STEADY = TRUE to re-initiate the controller design with the current data at a later stage in Phase 3 or 4. This will often provide some additional improvement to the controller design.  If an overshoot occurs or if no point of inflection is found, the manipulated variable jump size LHLM_TUN selected for pretuning may have been too large. This does not necessarily result in poor controller tuning. For the next pretuning, the value you select for LHLM_TUN should be approximately 20% less.  If the block has recognized steady-state condition or if the period 30 × TI (TI: integral action time of the PI controller set in PHASE = 3) has elapsed since the setpoint jump, the controller design has been improved and the system switches to PHASE = 4. The Self-Tuner stores the newly determined PI/PID controller parameters in GAIN, TI, TD, and PI_CON or PID_CON. The previous values of the PID controller are saved in PID_CON_OLD. If possible, a PID controller and a PI controller are designed. If PID_ON = TRUE, the PID controller is activated, otherwise the PI controller is activated. In PHASE 4, it is possible to switch between the two controllers bumplessly at any time. For difficult processes, the block always designs a PI controller, irrespective of PID_ON. The controller gain GAIN is limited in such a manner that the loop gain of the open loop (product of the process gain and the controller gain) is less than 40.0. |
| 4 | Automatic mode: Normal closed-loop control with/without control zone | In this phase, the controller controls using its tuned parameters. From this state, you can start fine tuning or pretuning. |
| 5 | Automatic mode, structure switchover at setpoint jump: Integral action deactivated, P(D) control | In the case of a positive setpoint jump ≥ MIN_STEP, the integral action of the controller is increased temporarily by a significant amount and the gain is decreased slightly, so that a quasi P(D) controller is used. In the proximity of the setpoint, the system is switched back to the original values for the integral action and the gain (PHASE = 5 in the Self-Tuner sequence). |
| 6 | Automatic mode, structure switchover at setpoint jump: Predictive manipulated variable specification | Only for step controller with position feedback  Processes with long delay times cannot be controlled well with a P(D) control system. After a positive setpoint jump ≥ MIN_STEP, the manipulated variable required constantly for the new setpoint is therefore output continually. In the proximity of the setpoint, the system is switched back bumplessly to PI or PID closed-loop control. This results in a slow, but overshoot-free response |
| 7 | Manual mode | Manual mode takes priority over all other operating modes.  Pretuning or fine tuning is canceled. When manual mode is deactivated (MAN_ON = FALSE and LMNS_ON = FALSE), the controller changes over to automatic mode (PHASE = 4 in the Self-Tuner sequence) and controls using the existing controller parameters.  If you use a step controller with position feedback (LMNR_ON = TRUE), you can use LMNS_ON = TRUE or MAN_ON = TRUE to switch to manual mode. If you use a step controller without position feedback (LMNR_ON = FALSE), you can only use LMNS_ON = TRUE to switch to manual mode. If you set the MAN_ON input to TRUE, the QMAN_ON output is set to TRUE and the MAN_OUT output is set to MAN. If you set the LMNS_ON input to TRUE, the QLMNUP output is set to LMNUP and the QLMNDN output is set to LMNDN. |

#### Heating tuning with step controller without position feedback

The diagram shows the phase steps of pretuning with measurement of the motor run time.

![Heating tuning with step controller without position feedback](images/26297481611_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Parameter TUN_ES.STATUS_H (S7-300, S7-400)

| STATUS_H | Description | Remedy |
| --- | --- | --- |
| 0 | Initialization |  |
| 1 | Point of inflection too low  In most cases optimization still results in good controller parameters. | To get closer the ideal case, increase LHLM_TUN or decrease the setpoint step-change size |
| 2 | Ideal case:  Point of inflection found |  |
| 3 | Point of inflection too high  A safety factor is included. In most cases optimization leads to controller parameters that can still be used but are prudent. | To get closer the ideal case, decrease LHLM_TUN or increase the setpoint step-change size. |
| 11, 12 | The time lag could not be detected correctly. Operation continues with an estimated value that can lead to controller parameters that are not optimum.  If the process has a pure VZ1 behavior (no time lag), the Self-Tuner can often design good controller parameters that are still good. Since calculation is continued with a roughly estimated time lag, it is possible that STATUS_D cannot be determined to 1 (controller for approximating VZ1 behavior) and that the control zone is de-activated, although a control zone makes sense for VZ1 processes. | Repeat optimization and ensure that disturbances do not occur at the process value.  If you are not satisfied with the controller parameters, you can at least use the values from PROCESS.GAIN and PROCESS.TM_LAG1 for a VZ1 model and use your own controller design in accordance with the text book. |
| 13 | The time lag could not be detected correctly. Operation continues with an estimated value that can lead to controller parameters that are not optimum. | Repeat optimization and ensure that disturbances do not occur at the process value. |

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_D (S7-300, S7-400)](#parameter-tun_esstatus_d-s7-300-s7-400)

### Parameter TUN_ES.STATUS_D (S7-300, S7-400)

| STATUS_D | Description |
| --- | --- |
| 0 | Initialization |
| 1 | Only PI controller design, since the process almost has PT1 behavior |
| 2 | Ideal case:  PI and PID controllers possible, VZ2 behavior |
| 3 | Only PI controller design, since there is a very high time lag / dead time or high order |
| 4 | Incorrect estimate   No controller design for on-line adaption.  During the first adaption the process is continued with the coarse PI controller from PHASE = 3.  Repeat optimization and ensure that disturbances do not occur at the process value. |

---

**See also**

[Description TUN_ES (S7-300, S7-400)](#description-tun_es-s7-300-s7-400)
  
[Scope of TUN_ES (S7-300, S7-400)](#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](#mode-of-operation-tun_es-s7-300-s7-400)
  
[Input parameters TUN_ES (S7-300, S7-400)](#input-parameters-tun_es-s7-300-s7-400)
  
[Output parameters TUN_ES (S7-300, S7-400)](#output-parameters-tun_es-s7-300-s7-400)
  
[In/out parameters TUN_ES (S7-300, S7-400)](#inout-parameters-tun_es-s7-300-s7-400)
  
[Parameter TUN_ES.PHASE (S7-300, S7-400)](#parameter-tun_esphase-s7-300-s7-400)
  
[Parameter TUN_ES.STATUS_H (S7-300, S7-400)](#parameter-tun_esstatus_h-s7-300-s7-400)
