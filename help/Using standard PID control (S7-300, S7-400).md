---
title: "Using standard PID control (S7-300, S7-400)"
package: TFTOPIDStdenUS
topics: 72
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using standard PID control (S7-300, S7-400)

This section contains information on the following topics:

- [Using PID_CP (S7-300, S7-400)](#using-pid_cp-s7-300-s7-400)
- [Using PID_ES (S7-300, S7-400)](#using-pid_es-s7-300-s7-400)

## Using PID_CP (S7-300, S7-400)

This section contains information on the following topics:

- [Technology object PID_CP (S7-300, S7-400)](#technology-object-pid_cp-s7-300-s7-400)
- [Control deviation generation (S7-300, S7-400)](#control-deviation-generation-s7-300-s7-400)
- [Controller (S7-300, S7-400)](#controller-s7-300-s7-400)
- [Manipulated variable (S7-300, S7-400)](#manipulated-variable-s7-300-s7-400)
- [Commissioning PID_CP (S7-300, S7-400)](#commissioning-pid_cp-s7-300-s7-400)

### Technology object PID_CP (S7-300, S7-400)

The technology object PID_CP provides a continuous PID controller for automatic and manual mode. It corresponds to the instance data block of the instruction PID_CP. You can configure the following controllers:

- Fixed setpoint control with continuous P, PI, PD, PID controllers
- Fixed setpoint control with disturbance variable selection
- Cascade control
- Two-loop ratio control
- Blending control

You configure the following functions of the technology object PID_CP:

- Scaling the process value signal
- Suppression of high-frequency vibrations in the process value branch by smoothing (time delay) of the process value signal.
- Linearization of the quadratic functions of the process value (flow-rate control with differential pressure encoders)
- Calling of "own functions" in the process value branch
- Monitoring the process value for violation of alarm and warning limits
- Monitoring the rate of change of the process value
- Adjustment of the setpoint by ramp/soak
- Scaling an external setpoint signal with ratio controllers
- Calling of "own functions" in the setpoint branch
- Limiting the rate of change of the setpoint
- Limiting the absolute values of the setpoint
- Filtering the control deviation signal with a deadband
- Monitoring the control deviation for violation of alarm and warning limits
- The proportional, integral, and derivative actions can be activated separately.
- Option of proportional and derivative effect in the controller feedback path.
- Selecting a disturbance variable
- Control of the manipulated variable in manual mode from a PG or HMI)
- Calling "own functions" in the manipulated value branch
- Limiting the rate of change of the manipulated variable
- Limiting the absolute values of the manipulated variable
- Scaling the manipulated variable
- Pulse width modulation for pulse generator

### Control deviation generation (S7-300, S7-400)

This section contains information on the following topics:

- [Process value (S7-300, S7-400)](#process-value-s7-300-s7-400)
- [Setpoint (S7-300, S7-400)](#setpoint-s7-300-s7-400)
- [Control deviation (S7-300, S7-400)](#control-deviation-s7-300-s7-400)

#### Process value (S7-300, S7-400)

This section contains information on the following topics:

- [Scaling (PV_NORM) (S7-300, S7-400)](#scaling-pv_norm-s7-300-s7-400)
- [Filter functions (S7-300, S7-400)](#filter-functions-s7-300-s7-400)
- [Alarm (S7-300, S7-400)](#alarm-s7-300-s7-400)

##### Scaling (PV_NORM) (S7-300, S7-400)

The "I/O process value ON" check box is used to specify which analog input variables are scaled to the physical unit of the process value.

- Activated: Input variable is the I/O process value (PV_PER)
- Disabled: Input variable is the internal process value (PV_IN)

In order to uniquely specify the scaling levels, you define the following four parameters:

- High input (NM_PIHR)
- Low input (NM_PILR)
- High output (NM_PVHR)
- Low output (NM_PVLR)

The parameters are preset depending on the sensor type.

The process value is calculated from the respective input value (PV_PER or PV_IN) according to the following formula:

MP4 = (PV_PER - NM_PILR) × (NM_PVHR - NM_PVLR) / (NM_PIHR - NM_PILR) + NM_PVLR

or

MP4 = (PV_IN - NM_PILR) × (NM_PVHR - NM_PVLR) / (NM_PIHR - NM_PILR) + NM_PVLR

![Figure](images/32396288651_DV_resource.Stream@PNG-de-DE.png)

The process value is output in the static variable MP4.

No values are limited and the parameters are not checked. If you enter the same value for input high and input low, a division by zero may occur based on the formulas above. The instruction will not detect this.

##### Filter functions (S7-300, S7-400)

This section contains information on the following topics:

- [Smooth controlled variable (LAG1ST) (S7-300, S7-400)](#smooth-controlled-variable-lag1st-s7-300-s7-400)
- [Square root (SQRT) (S7-300, S7-400)](#square-root-sqrt-s7-300-s7-400)
- [FC call in the process value branch (PVFC) (S7-300, S7-400)](#fc-call-in-the-process-value-branch-pvfc-s7-300-s7-400)

###### Smooth controlled variable (LAG1ST) (S7-300, S7-400)

In order to smooth process signals with superimposed rapid variations (noise), a first-order delay element is applied in the process value branch. This function stabilizes the analog controlled variable to a greater or lesser degree, depending on the time constant (PV_TMLAG). In this way, disturbances are effectively suppressed. As a result of this, however, the time constant of the overall control loop also increases, i.e., the closed-loop control becomes more sluggish.

The stabilizing effect is achieved by a first-order delay algorithm.

The step response within the time range is:

outv(t) = MP4(0) (1 - e<sup> -t/PV_TMLAG</sup>)

![Figure](images/32396371467_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| MP4(0) | The height of the process value step at the input |
| outv(t) | The output variable |
| PV_TMLAG | The time lag constant |
| t | Time |

###### Smoothing of the process value

If smoothing of the process value (LAG1STON = FALSE) is not activated, then the I/O input (PV_PER) or the internal input (PV_IN) is switched through to the process value branch without a delay.

###### Time lag

The PV_TMLAG input parameter specifies the time lag for the process value. Any value within the value range is permitted.

If PV_TMLAG ≤ 0.5 * CYCLE, there is no longer any lag in effect.

A sampling time (CYCLE) of less than one-fifth of the time lag is required in order to achieve a lag response approaching that of the analog response.

###### Square root (SQRT) (S7-300, S7-400)

The "Square root" function (SQRT) is used to linearize the controlled variable. If the process value supplied by an encoder is a physical quantity and there is a quadratic relation between this quantity and the measured process variable, the characteristic of the controlled variable must be linearized prior to any further processing in the controller.

The measured signal must always be linearized by the square-root function if flow measurements are made using metering orifices, venturi tubes, or the like. The measured pressure differential is then proportional to the square of the flow.

The SQRT_ON = TRUE input signal is used to activate the square root function in the process value branch. The square root function algorithm has the following form:

outv = SQRT (MP5) × (SQRT_HR – SQRT_LR) / 10.0 + SQRT_LR

Here, outv is the scaled output value of the square root function (physical flow).

This formula stipulates that the input value of the square root is scaled to the number range 0 to 100. The parameters for the "Measuring range high" and "Measuring range low" must be set to 100.0 and 0.0 in the scaling of the process value. The square root of this value yields a measuring range from 0 to 10. This range of numbers is scaled using the high limit (SQRT_HR) and the low limit of the physical measuring range (SQRT_LR).

![Figure](images/32396416139_DV_resource.Stream@PNG-de-DE.png)

###### Example of scaling

The input value PV_IN of the controller is the differential pressure in mbar:

| Start of measuring range NM_PILR | End of measuring range NM_PIHR | Sample value for PV_IN |
| --- | --- | --- |
| 20.0 mbar | 200.0 mbar | 150.0 mbar |

The scaled differential pressure is calculated with the help of the scaling function PV_NORM, whereby NM_PVHR = 100.0 and NM_PVLR = 0.0 are selected:

|  |  |  |
| --- | --- | --- |
| MP4 | = | (PV_IN - NM_PILR) * (NM_PVHR - NM_PVLR) /    (NM_PIHR - NM_PILR) + NM_PVLR |
|  | = | (PV_IN - 20.0 mbar) * (100.0 - 0.0) /    (200.0 mbar - 20.0 mbar) + 0.0 |
|  | = | (PV_IN - 20.0 mbar) * 100 / 180.0 mbar |

| Initial value of MP4 | End value of MP4 | Sample value for MP4 |
| --- | --- | --- |
| 0.0 | 100.0 | 72.222 |

Since no smoothing is used in this example, the following applies: MP5 = MP4.

For the square root from the scaled differential pressure MP5, the result is:

| Initial value according to the square root | End value according to the square root | Sample value for SQRT(MP5) |
| --- | --- | --- |
| 0.0 | 10.0 | 8.498 |

For the scaled output value outv of the square root function (physical flow-rate) with SQRT_HR = 20000.0 m<sup>3</sup>/h and SQRT_LR = 0.0 m3/h, there follows:

|  |  |  |
| --- | --- | --- |
| outv | = | SQRT(MP5) * (SQRT_HR - SQRT_LR) / 10.0 + SQRT_LR |
|  | = | SQRT(MP5) * (20000.0 m<sup>3</sup>/h - 0.0 m3/h) / 10.0 + 0.0 m3/h |
|  | = | 2000.0 m<sup>3</sup>/h * SQRT(MP5) |

| Start of measuring range outv | End of measuring range outv | Sample value for outv |
| --- | --- | --- |
| 0.0 m<sup>3</sup>/h | 20000.0 m<sup>3</sup>/h | 16996.732 m<sup>3</sup>/h |

###### FC call in the process value branch (PVFC) (S7-300, S7-400)

Insertion of a user-specific function in the process value branch allows the controlled variable to undergo signal processing, e.g., signal delay or linearization, prior to any further processing in the controller.

###### Calling a function

If you want to insert a user-specific function into the process value branch, enable "Enable FC call" (PVFC_ON). The number of the utilized function is entered in the "FC number" input field (PVFC_NBR). The controller calls the function. In so doing, existing input/output parameters of the user function are not supplied. You have to program the data transfer in your function yourself.

You can monitor the output value of the function at the static variable MP6.

> **Note**
>
> No check is made to determine whether a function exists. If the function does not exist, the CPU switches to STOP with an internal system error.

##### Alarm (S7-300, S7-400)

This section contains information on the following topics:

- [Monitor process value for limit values (PV_ALARM) (S7-300, S7-400)](#monitor-process-value-for-limit-values-pv_alarm-s7-300-s7-400)
- [Monitor rate of change of the process value (ROCALARM) (S7-300, S7-400)](#monitor-rate-of-change-of-the-process-value-rocalarm-s7-300-s7-400)

###### Monitor process value for limit values (PV_ALARM) (S7-300, S7-400)

If the values of the process variables (e.g., speed, pressure, filling level, temperature, etc.) exceed or fall below certain values in closed-loop controls, an illegal process status or plant status can occur. In such cases, monitoring of the process value for limit values (PV_ALARM) is used in order to monitor the process value for violation of the permissible operating range. Limit violations are detected and signaled so that an appropriate reaction can be initiated.

> **Note**
>
> The monitoring of the process value for limit values cannot be deactivated. The violation of the configured limits is always signaled.

Monitoring of the process value for limit values (PV_ALARM) monitors the controlled variable PV(t) for four assignable limits in two tolerance bands. If the limits are reached or exceeded, the function signals a “warning” at the first limit and an “alarm” at the second limit.

###### Limit values

The numeric values of the limits are set in the input parameters for “warning” and “alarm”. If the process value (PV) exceeds or falls below these limits, the associated output message bits are set for the high alarm (QPVH_ALM), the high warning (QPVH_WRN), the low warning (QPVL_WRN), and the low alarm (QPVL_ALM).

During a restart, the message bits are reset.

The message bits are set as follows:

| QPVH_ALM | QPVH_WRN | QPVL_WRN | QPVL_ALM | If: | And: |
| --- | --- | --- | --- | --- | --- |
| TRUE | TRUE | FALSE | FALSE | PV ↗  PV ↘ | PV ≥ PVH_ALM  PV ≥ PVH_ALM **-** PV_HYS |
| FALSE | TRUE | FALSE | FALSE | PV ↗  PV ↘ | PV ≥ PVH_WRN  PV ≥ PVH_WRN **-** PV_HYS |
| FALSE | FALSE | TRUE | FALSE | PV ↘  PV ↗ | PV ≤ PVL_WRN  PV ≤ PVL_WRN **+** PV_HYS |
| FALSE | FALSE | TRUE | TRUE | PV ↘  PV ↗ | PV ≤ PVL_ALM  PV ≤ PVL_ALM **+** PV_HYS |

The following has to apply so that the block operates properly:

High alarm &lt; High warning &lt; Low warning &lt; Low alarm

![Limit values](images/32396518539_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | 1. Tolerance band |
| ② | 2. Tolerance band |

###### Hysteresis

In order to prevent "flickering" of the message bits when the input variable undergoes slight changes or in the event of rounding errors, a hysteresis PV_HYS is used. The controlled variable must violate the hysteresis before the message bits are reset.

###### Monitor rate of change of the process value (ROCALARM) (S7-300, S7-400)

If the change in the process variable (e.g., speed, pressure, filling level, temperature, etc.) is too great in closed-loop controls, an illegal process status or plant status can occur. In such cases, monitoring the rate of change of the process value (ROCALARM) is used to monitor the process value for violations of a permissible rate of change. Limit violations are detected and signaled so that an appropriate reaction can be initiated.

> **Note**
>
> Monitoring of the rate of change of the process value (ROCALARM) cannot be deactivated. The violation of the configured limits is always signaled.

The ROCALARM function monitors the controlled variable PV(t) for permissible rate-of-change limits that are assignable according to sign.

The numeric values of the limit slopes are set at the input parameters for "Maximum increase" and "Maximum decrease" in the positive and negative range of the controlled variable. The slopes refer to a rising slope or falling slope in percent per second. If the rate of change of the controlled variable violates these limits, the associated output message bit QPVURLMP ... QPVDRLMN is set.

![Figure](images/32396576011_DV_resource.Stream@PNG-de-DE.png)

The ramp parameters are identified in accordance with the following scheme:

| Parameter | PV change |
| --- | --- |
| Maximum increase in the positive range (PVURLM_P) | PV &gt; 0 and |PV| rising |
| Maximum decrease in the positive range (PVDRLM_P) | PV &gt; 0 and |PV| falling |
| Maximum increase in the negative range (PVURLM_N) | PV &gt; 0 and |PV| rising |
| Maximum decrease in the negative range (PVDRLM_N) | PV &lt; 0 and |PV| falling |

#### Setpoint (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying a setpoint (S7-300, S7-400)](#specifying-a-setpoint-s7-300-s7-400)
- [Setpoint generator (SP_GEN) (S7-300, S7-400)](#setpoint-generator-sp_gen-s7-300-s7-400)
- [Ramp/soak (RMP_SOAK) (S7-300, S7-400)](#rampsoak-rmp_soak-s7-300-s7-400)
- [Scaling (S7-300, S7-400)](#scaling-s7-300-s7-400)
- [Limiting functions (S7-300, S7-400)](#limiting-functions-s7-300-s7-400)

##### Specifying a setpoint (S7-300, S7-400)

Select a source for the setpoint. The following options are available:

- Internal setpoint

  The input parameter SP_INT is used as setpoint
- Setpoint generator

  The input parameter SP_INT is used as setpoint and can be incremented or decremented using the static variables SPUP and SPDN.
- Ramp/soak

  The input parameter SP_INT is used as setpoint and can be changed according to a specified ramp/soak.
- External setpoint

  The input parameter SP_EXT is used as setpoint for blending, ratio and cascade controllers. The external setpoint can be scaled.

The effective setpoint is shown at the output parameter SP.

##### Setpoint generator (SP_GEN) (S7-300, S7-400)

The internal setpoint SP_INT can be incremented or decremented in steps using the SPUP and SPDN switches. The modified value can be monitored at MP1. The configured setpoint limits are taken into account.

###### Effect of the switches SPUP and SPDN

For changes involving small steps, the controller should have a maximum sampling time of 100 ms.

The rate of change of the output variable depends on how long the SPUP or SPDN switch is actuated and on the selected limits. The following relationship applies:

- During the first 3 s after setting SPUP or SPDN:

  doutv/dt = (SP_HLM - SP_LLM) / 100 s
- Afterwards:

  doutv/dt = (SP_HLM - SP_LLM) / 10 s

  ![Effect of the switches SPUP and SPDN](images/32395861771_DV_resource.Stream@PNG-en-US.png)

For a sampling time of 100 ms and a setpoint range of -100.0 to 100.0, the setpoint, for example, changes by 0.2 per cycle during the first 3 seconds. If SPUP is TRUE for more than 3 seconds, the rate of changes increases to ten times the value, in this case therefore to 2 per cycle.

###### Startup and operating principles of the setpoint generator

- During a complete restart, output outv is reset to 0.0.
- If you activate the setpoint generator (SPGEN_ON = TRUE), the signal value SPFC_IN is output initially at output outv. Therefore, the switchover to the setpoint generator from another operating mode is always smooth. Provided the SPUP and SPDN (up/down keys) are not activated, the signal value SPFC_IN is retained at the output.

###### Parameters of the SP_GEN function

Output parameter outv is an implicit parameter. It can be monitored with the configuration tool via measuring point MP1.

| Parameter | Meaning | Permitted value range |
| --- | --- | --- |
| SPFC_IN | FC input setpoint | Engineering value range |
| SP_INT | Internal setpoint | Engineering value range |

![Function scheme and parameters of the setpoint generator](images/37537528331_DV_resource.Stream@PNG-de-DE.png)

Function scheme and parameters of the setpoint generator

##### Ramp/soak (RMP_SOAK) (S7-300, S7-400)

If you want the setpoint SP_INT to change autonomously depending on the time, for example, during the control of processes after a time-controlled temperature program, this is possible by configuring a ramp/soak and activating the ramp/soak function. The setpoint change is formed from the level sections with a maximum of 256 time slices.

> **Note**
>
> The block function does not check whether a global DB with the number 'DB_NBR' exists or whether the parameter 'Number of time slices' NBR_PTS corresponds to the data block length. If the parameter assignment is incorrect, the CPU goes to **STOP** and issues an internal system error.

###### How the ramp/soak works

The ramp/soak supplies the output variable outv according to a function that runs to a defined ramp/soak. The ramp/soak process is defined by specifying a series of time slices in a global data block DB_RMPSK with time values PI[i].TMV and the associated output values PI[i].OUTV.

- PID-CP

  [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400) is not included in the library. You must create this global data block yourself.
- PID-ES

  [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400-1) is not included in the library. You must create this global data block yourself.

The following figure shows a ramp/soak with 6 time slices.

![How the ramp/soak works](images/32395896843_DV_resource.Stream@PNG-de-DE.png)

The time value for the last time slice n is PI[n].TMV = 0 ms. The processing time of a ramp/soak is counted down from the initial value to zero.

PI[i].TMV specifies the intervals between time slices. Between the time slices, interpolation is according to the following function:

![How the ramp/soak works](images/32395933451_DV_resource.Stream@PNG-de-DE.png)

0 ≤ n ≤ (NBR_PTS - 1)

![How the ramp/soak works](images/32395921547_DV_resource.Stream@PNG-en-US.png)

Note

> **Note**
>
> During the interpolation of the ramp/soak between the time slices, pauses can sometimes occur at the initial value if the sampling time CYCLE is very small compared to the time between the time slices PI[n].TMV. Due to the computational accuracy of the CPU, the ramp/soak function cannot linearize all flat ramp/soak profiles. If the ramp/soak profile is too flat, the initial value pauses for a time at the respective time slice and continues, after a certain time, to integrate with the minimum rate of rise to the next time slice.
>
> To correct or avoid error: Shorten the time between the time slices by inserting additional time slices. The output ramp/soak profile thus approximates the desired flat ramp/soak profile.

###### Ramp/soak function ON

The ramp/soak function is activated by changing RMPSK_ON from FALSE to TRUE. The ramp/soak is terminated after the last time slice has been reached. When the function is started again by the operator, RMPSK_ON first has to be set to 'FALSE' and then back to 'TRUE' .

During a **restart**, the output outv is reset to 0.0 and the total time or total remaining time is determined. During the transition to normal operation, the ramp/soak profile is processed immediately from the starting point according to the set operating mode. If this is not desired, the parameter RMPSK_ON must be set to FALSE in the restart OB.

###### Ramp/soak functions

The instruction has the following functions:

- Activate ramp/soak for single execution
- Pre-assign fixed value to the output
- Cyclic repetition on
- Hold ramp/soak
- Continue ramp/soak
- Update the total processing time and remaining total time

The following table applies for the significance of the control inputs when setting a desired operating mode:

| Operating mode | RMPSK_ON | DFOUT_ON | RMP_ HOLD | CONT_ ON | CYC_ ON | TUPDT_ON | Output signal OUTV |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ramp/soak on | TRUE | FALSE | FALSE | **) | FALSE | **) | OUTV(t)  End value is held after the end of processing. |
| Set output | TRUE | TRUE | **) | **) | **) | **) | DF_OUTV |
| Cyclic repetition on | TRUE | FALSE | FALSE | **) | TRUE | **) | OUTV(t)  After end: Automatic start |
| Hold ramp/soak | TRUE | FALSE | TRUE | FALSE | **) | **) | Current value of OUTV(t) is held *) |
| Continue ramp/soak | TRUE | FALSE | TRUE | TRUE | **) | **) | OUTV (old) *) |
| FALSE | Operation is continued with newly defined values. |  |  |  |  |  |  |
| Updating the total time and remaining total time | **) | **) | **) | **) | **) | FALSE | Does not influence OUTV |
|  | TRUE | Does not influence OUTV |  |  |  |  |  |
| *) The ramp/soak profile does not have the form configured by the user until the next time slice.  **) The respective operating mode set is executed irrespective of the significance of the control signals in the fields marked with **) |  |  |  |  |  |  |  |

###### Set output of ramp/soak

If you enable this function (DFRMP_ON = TRUE), the output value of the ramp/soak is set to signal value SP_INT or output value SP_GEN.

> **Note**
>
> Preassignment with the internal setpoint has an effect only if the ramp/soak function is enabled (RMPSK_ON = TRUE).

After the switchover to DFRMP_ON = FALSE, outv moves linearly from the specified setpoint (e.g., SP_INT) to the output value of the current time slice number PI[NBR_ATMS].OUTV.

The internal time processing continues running even when a fixed setpoint (RMPSK_ON = TRUE and DFRMP_ON = TRUE) is switched through.

On the start of the ramp/soak profile (RMPSK_ON = TRUE), the fixed setpoint SP_INT continues to be output until DFRMP_ON changes from TRUE to FALSE after the duration of T*.

![Set output of ramp/soak](images/32395945355_DV_resource.Stream@PNG-en-US.png)

At this moment, the time PI[0].TMV and a part of the time PI[1].TMV has expired. OUTV is moved from SP_INT to PI[2].OUTV, which means to the setpoint at time slice 2.

The configured ramp/soak profile is output only starting from time slice 2. The agreement of the configured and current ramp/soak profile is displayed by setting QR_S_ACT = TRUE. On a rising edge at DFRMP_ON during processing of the ramp/soak profile, the output value OUTV jumps to SP_INT without a delay.

###### Cyclic repetition on

If "Cyclic repetition" operating mode (CYC_ON = TRUE) is activated, the ramp/soak function automatically returns to the starting point after the last time slice value has been output and begins a new run.

There is no interpolation between the last time slice and the starting point. For a smooth transition, the following must be true: PI[NBR_PTS].OUTV = PI[0].OUTV.

###### Hold ramp/soak

When RMP_HOLD = TRUE, the value of the output variable (including the time processing) is frozen. When RMP_HOLD = FALSE is reset, the function resumes at the interruption point PI[x].TMV.

![Hold ramp/soak](images/32395957259_DV_resource.Stream@PNG-en-US.png)

The processing time of the ramp/soak profile is extended by the amount of the time T*. The ramp/soak profile has the configured course from the starting point until the rising edge at RMP_HOLD and from time slice 5* to time slice 6*, i.e., output signal QR_S_ACT has the value TRUE.

If switch CONT_ON is set, the held ramp/soak function continues processing the ramp/soak profile at preassigned point TM_CONT.

###### Continue ramp/soak

With CONT_ON, a held ramp/soak profile is restarted at a defined point. If the ramp/soak function is not held, CONT_ON has no effect.

If the control input for continuing (CONT_ON = TRUE) is set, the held ramp/soak function is continued at time slice TM_SNBR. TM_CONT determines the remaining time that the ramp/soak function requires to reach time slice TM_SNBR.

The following figure shows the effect of RMP_HOLD and CONT_ON when the configuration is as follows:

Continue at time slice 5 (TM_SNBR = 5) and continue in T* s: TM_CONT = T*

![Continue ramp/soak](images/32395969163_DV_resource.Stream@PNG-en-US.png)

Time slices 3 and 4 are omitted in this processing cycle of the ramp/soak function. On a signal change of RMP_HOLD from TRUE to FALSE, the configured curve progression is only reached again starting from time slice 5.

Output QR_S_ACT is only set when the ramp/soak function executes the ramp/soak profile assigned by the user.

###### Updating the total time and remaining total time

The current time slice number NBR_ATMS, the current remaining time until the time slice is reached (RS_TM), the total time T_TM, and the total remaining time until the end of the ramp/soak profile (RT_TM) are updated in every cycle.

In the case of online changes of PI[n].TMV, the total time and the total remaining time of the ramp/soak profile change. Since the calculation of T_TM and RT_TM with many time slices significantly increases the processing time of the function block, the calculation is only carried after a restart or when TUPDT_ON = TRUE. The time intervals PI[0 ... NBR_PTS].TMV between the individual time slices are added up and indicated at the total time T_TM and total remaining time RT_TM outputs.

Please note that determining the total times requires significant CPU runtime.

###### Procedure

To configure the ramp/soak function, proceed as follows:

1. Select "Ramp/soak" from the "Setpoint source" drop-down list.
2. Create a [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400) (PID-CP) or [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400-1) (PID-ES).
3. Define the required parameters for the ramp/soak.
4. Enter the number of the data block DB_RMPSK in the "DB number" input field.
5. Enable or disable the additional functions of the ramp/soak.
6. If you have enabled the Continue ramp/soak function, enter at which time slice and when the ramp/sock is to be continued.

##### Scaling (S7-300, S7-400)

###### Scaling of an external setpoint

If the external setpoint is not expressed in the physical unit of the process value (e.g., expressed as a percent in the case of cascade control), then this value and its setting range must be scaled to the physical unit of the process value. The "Scaling in setpoint branch" function is used for this.

The SP_NORM function scales an analog input variable. The analog external setpoint is transformed to output variable outv using the scaling level. Output value OUTV is accessible in the configuration tool via measuring point MP2.

The output value of the function has an effect when control input SPEXT_ON = TRUE. In order to uniquely specify the scaling levels, you define the following four parameters:

- High input: SP_EXT: NM_SPEHR
- Low input: SP_EXT: NM_SPELR
- High output: NM_PVHR (You specify this value in the scaling function of the process value.)
- Low output: NM_PVLR (You specify this value in the scaling function of the process value.)

  ![Scaling of an external setpoint](images/34001570315_DV_resource.Stream@PNG-de-DE.png)

Output value outv is calculated from the respective input value SP_EXT according to the following formula:

outv = (SP_EXT – NM_SPELR) x (NM_PVHR – NM_PVLR) / (NM_SPEHR – NM_SPELR) + NM_PVLR

For the special case in which a square root function is activated in the process value branch, the scaling values of the square root function (SQRT_HR and SQRT_LR) apply as the high and low limits of output value outv.

In this case, output value outv of the scaling function is calculated from the respective input value SP_EXT according to the following formula:

outv = (SP_EXT – NM_SPELR) x (SQRT_HR – SQRT_LR) / (NM_SPEHR – NM_SPELR) + SQRT_LR

There is no internal value limiting in the function. The parameters are not checked. If you enter the same value for NM_SPEHR and NM_SPELR, a division by zero is possible based on the formulas above. The instruction will not detect this.

###### Combination/ratio factor

With ratio control, the setpoints of the control loop are coordinated with one another in such a way that the set ratio matches the actual ratio of the process values.

With blending control, the desired quantities of the individual components are set. The total of the blending factors FAC must be 1.

###### Procedure

To configure the scaling, proceed as follows:

1. Enter the values for the scaling in the input fields "High input" and "Low input".
2. Enter a blending/ratio factor (FAC).

##### Limiting functions (S7-300, S7-400)

###### FC call in the setpoint branch

Insertion of a user-specific function in the setpoint branch allows an externally specified reference variable to undergo signal processing (e.g., signal delay or linearization) prior to application in the controller.

If you activate the FC call in the setpoint branch, a user-specific function is called. The controller calls the FC. In so doing, existing input/output parameters of the user FC are not initialized. Therefore, you must use S7-STL to program the data transfer in the user FC. You can monitor the prepared setpoint at MP3.

The value of SPFC_ON then determines whether a user-programmed function in the form of a standard FC (e.g., a characteristic curve) will be inserted at this point in the setpoint channel or whether the setpoint will continue to be processed without any influence of this type.

> **Note**
>
> The statement does not check to determine if a function exists. If the function does not exist, the CPU switches to STOP with an internal system error.

###### Procedure

To call a function in the setpoint branch, proceed as follows:

1. Select the "Enable FC call" check box.
2. In the "FC" input field, enter the number of the function to be called.

###### Limiting of the rate of change of the setpoint

Ramp functions are used in the setpoint branch in situations where the process does not tolerate abrupt changes in the actuating signal, since an abrupt setpoint change generally also causes an abrupt change in the manipulated variable of the controller. These abrupt manipulated variable changes must be avoided, for example, when a gearbox is connected in between an adjustable-speed motor and the load to be driven and an excessively rapid increase of the motor speed would result in overloading of the gearbox.

The SP_ROC function limits the rate of change of the setpoints processed in the controller. This is carried out separately for the rising slope and falling slope and separately for the positive and negative range of the reference variable.

The limiting for each slope of the ramp function in the positive range and in the negative range of the reference variable is entered in the four inputs SPURLM_P, SPDRLM_P, SPURLM_N, and SPDRLM_N. The slopes refer to a rising or falling slope per second. Faster setpoint changes are ramped down to these maximum rates.

For example, if SPURLM_P is assigned the value 10.0 [engineering value range/s], the following values are added to the "old value" of outv in each sampling cycle for as long as inv &gt; outv:

|  |  |  |
| --- | --- | --- |
| Sampling time | 1 s | outv<sub>old</sub> + 10 |
|  | 100 ms | outv<sub>old</sub> + 1 |
|  | 10 ms | outv<sub>old</sub> + 0.1 |

The following figure shows an example of how the signal processing functions. The step functions at input inv(t) become ramp functions at output outv(t).

![Limiting of the rate of change of the reference variable SP(t)](images/34001581835_DV_resource.Stream@PNG-en-US.png)

Limiting of the rate of change of the reference variable SP(t)

When slope limits are reached, this is not signaled.

###### Procedure

To limit the rate of change, proceed as follows:

1. Activate the "Limit rate of change" check box.
2. Specify the following values for the positive range as well as for the negative range:

   - Rising slope for setpoint value
   - Falling slope for setpoint value

###### Limiting of the absolute value of the reference variable

The setting range of the reference variable determines the range in which the controlled variable can fluctuate, i.e., the range in which the process varies within the scope of permissible status values.

To avoid a critical or impermissible process status, the setting range of the reference variable is subject to high and low limits (SP_LIMIT) in the setpoint branch of standard PID control.

The SP_LIMIT function limits the setpoint SP at the assignable low and high values (SP_LLM and SP_HLM) as long as input variable INV is outside these limits. Because the function cannot be deactivated, the specification of a low limit and high limit must be taken into consideration in the configuration.

The numeric values of the limits are set in the input parameters for the low and high limits. In the event of violations by input variable inv(t), the associated displays are output via the message outputs.

![Absolute value limiting of reference variable SP(t)](images/34001678219_DV_resource.Stream@PNG-en-US.png)

Absolute value limiting of reference variable SP(t)

During a restart, the message bits are reset.

The message bits are set as follows:

| SP =PVH_ALM | QSP_HLM | QSP_LLM | If: |
| --- | --- | --- | --- |
| SP_HLM | TRUE | FALSE | inv ≥ SP_HLM |
| SP_LLM | FALSE | TRUE | inv ≤ SP_LLM |
| inv | FALSE | FALSE | SP_HLM &lt; inv &lt; SP_LLM |

###### Procedure

To limit the absolute value of the reference variable, proceed as follows:

1. Enter the high limit for the absolute setpoint (SP_HLM) in the "High limit" input field.
2. Enter the low limit for the absolute setpoint (SP_LLM) in the "Low limit" input field.

#### Control deviation (S7-300, S7-400)

This section contains information on the following topics:

- [Deadband (S7-300, S7-400)](#deadband-s7-300-s7-400)
- [Alarm (S7-300, S7-400)](#alarm-s7-300-s7-400-1)

##### Deadband (S7-300, S7-400)

In an optimally tuned controller, when a high-frequency interfering signal is superimposed on the control variable or reference variable, the noise portion will also have an effect on the controller output. This can result in strong fluctuations of the manipulated variable, for example, if the controller gain is high and derivative action is enabled. Due to the increased switching frequency (step controller), this causes increased wear of the actuator.

The function reduces the noise portion in the control deviation signal while the controller is in steady-state and thus reduces undesired oscillating of the controller output.

The deadband can be disabled.

###### Signal filtering through deadband function

The DEADBAND function suppresses small fluctuations of the input variable around a specified zero point within an adjustable range. Outside this fluctuation range, the control deviation ER rises or falls proportional to the input variable. The width of the deadband can be specified with the DEADB_W parameter. Only positive values are permitted for the deadband width.

If the input variable is within the deadband, the value 0 (control deviation = 0) is output at the output. Only when the input variable exits the deadband will the output rise or fall by the same values as input variable inv. This results in corruption of the transmitted signal outside the deadband, too. However, this is accepted in order to avoid step changes at the deadband limits (see figure below). The corruption corresponds to the value DEADB_W and can therefore be controlled easily.

The DEADBAND function operates according to the following functions:

(ER) = inv + DEADB_W for inv &lt; - DEADB_W

(ER) = 0 for -DEADB_W ≤ inv ≤ + DEADB_W

(ER) = inv - DEADB_W for inv &gt; + DEADB_W

![Signal filtering through deadband function](images/34001804299_DV_resource.Stream@PNG-en-US.png)

Effects of the signal filtering can be monitored at the output parameter ER.

##### Alarm (S7-300, S7-400)

Excessive deviations of the controlled variable from the specified setpoint can cause an undesired process status. In such cases, the ER_ALARM function is used to monitor the control deviation for violation of the permissible operating range. ER_ALARM detects and signals any limit violations that occur so that an appropriate reaction can be initiated.

> **Note**
>
> The monitoring of the control deviation for limit values cannot be disabled. The violation of the configured limits is always signaled.

The ER_ALARM function monitors the size of control deviation ER(t) for four assignable limits in two tolerance bands. If the limits are reached or exceeded, the function signals a “warning” at the first limit and an “alarm” at the second limit.

###### Limit values

The numeric values of the limits are set in the input parameters for “warning” and “alarm”. If the control deviation (ER) violates these limits, the associated output message bits QERN_ALM ... QERP_ALM are set.

During a restart, the message bits are reset.

The message bits are set as follows:

| QERP_ALM | QERP_WRN | QERN_WRN | QERN_ALM | If: | And: |
| --- | --- | --- | --- | --- | --- |
| TRUE | TRUE | FALSE | FALSE | ER ↗  ER ↘ | ER ≥ ERP_ALM  ER ≥ ERP_ALM **-** ER_HYS |
| FALSE | TRUE | FALSE | FALSE | ER ↗  ER ↘ | ER ≥ ERP_WRN  ER ≥ ERP_WRN **-** ER_HYS |
| FALSE | FALSE | TRUE | FALSE | ER ↘  ER ↗ | ER ≤ ERP_WRN  ER ≤ ERP_WRN **+** ER_HYS |
| FALSE | FALSE | TRUE | TRUE | ER ↘  ER ↗ | ER ≤ ERP_ALM  ER ≤ ERP_ALM **+** ER_HYS |

The following has to apply so that the block operates properly:

High alarm &lt; High warning &lt; Low warning &lt; Low alarm

![Limit values](images/37711954955_DV_resource.Stream@PNG-en-US.png)

###### Hysteresis

In order to avoid "flickering" of the message bits when the input variable undergoes slight changes or in the event of rounding errors, a hysteresis ER_HYS is used. The control deviation must violate the hysteresis before the message bits are reset.

### Controller (S7-300, S7-400)

This section contains information on the following topics:

- [Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400)
- [Controller structures (S7-300, S7-400)](#controller-structures-s7-300-s7-400)
- [Proportional component (S7-300, S7-400)](#proportional-component-s7-300-s7-400)
- [Integral action (S7-300, S7-400)](#integral-action-s7-300-s7-400)
- [Derivative component (S7-300, S7-400)](#derivative-component-s7-300-s7-400)

#### Control algorithm (S7-300, S7-400)

The manipulated variable of the continuous controller is calculated within the configured sampling time cycle on the basis of the control deviation in the PID position algorithm. The controller is implemented in a purely parallel structure. The proportional, integral, and derivative actions can each be disabled individually.

![Figure](images/35654713995_DV_resource.Stream@PNG-de-DE.png)

##### Feedforward control

A disturbance variable DISV can be added in the output signal of the controller (PID_OUTV). The variable is switched-in or switched-off in the PID window of the configuration tool using the DISV_SEL structure selector or through "Disturbance variable on".

##### Proportional and derivative action in the feedback path

In the parallel structure, each action in the control algorithm receives the control deviation as input signal. Via the proportional action and derivative action, the manipulated variable is influenced directly by setpoint steps. However, a different controller structure in which the formation of the proportional and the derivative actions is moved to the feedback path ensures a smooth response of the manipulated variable to setpoint step changes. In this structure, the integral action processes the control deviation as the input signal. Only the negative controlled variable (factor = - -1) is applied to the proportional action and the derivative action.

![Proportional and derivative action in the feedback path](images/32396718347_DV_resource.Stream@PNG-de-DE.png)

##### Scaling the input variable ER and PV

The input variables ER and PV of the PID controller are scaled to the range 0 to 100 prior to the controller processing according to the following formulas:

- with square-root function disabled (SQRT_ON = FALSE):

  - ER<sub>scaled</sub> = ER * 100.0 / (NM_PVHR – NM_PVLR)
  - PV<sub>scaled</sub> = (PV - NM_PVLR) * 100.0 / (NM_PVHR – NM_PVLR)
- with square-root function enabled (SQRT_ON = TRUE):

  - ER<sub>scaled</sub> = ER * 100.0 / (SQRT_HR – SQRT_LR)
  - PV<sub>scaled</sub> = (PV - SQRT_LR) * 100.0 / (SQRT_HR – SQRT_LR)

This scaling is performed so that the proportional gain GAIN of the PID controller can be entered without dimensions. If the high limit and low limit of the physical measuring range change (for example, from bar to mbar), the gain factor does not then have to be changed.

The scaled input variables ER<sub>scaled</sub> and PV<sub>scaled</sub> cannot be monitored.

---

**See also**

[Controller structures (S7-300, S7-400)](#controller-structures-s7-300-s7-400)
  
[Proportional component (S7-300, S7-400)](#proportional-component-s7-300-s7-400)
  
[Derivative component (S7-300, S7-400)](#derivative-component-s7-300-s7-400)
  
[Integral action (S7-300, S7-400)](#integral-action-s7-300-s7-400)

#### Controller structures (S7-300, S7-400)

##### Use and parameter assignment of the PID controller

The majority of the controlled systems occurring in the process industry can be controlled with the PI controller function/PID controller function of standard PID control. Only in special cases are additional methods and measures needed for a particular closed-loop control.

However, a major problem in the field continues to be how to assign the PI controller/PID controller parameters, i.e., how to determine the "correct" settings for the controller parameters. The quality of this parameter assignment is critical in order for the PID control to meet the requirements of the task at hand. It requires either a lot of practical experience, special expertise, or a great amount of time.

##### P control

The integral and derivative actions are disabled in a proportional-action controller (P-controller). (I_SEL and D_SEL = FALSE). This means that when control deviation ER = 0, output signal OUTV = 0. If an operating point ≠ 0 is intended, i.e., a numeric value will be set for the output signal when the control deviation is zero, the integral branch must be activated (see the following figure).

In the integral action, an operating point ≠ 0 can be specified for the P-controller via a corresponding setting of initialization value I_ITLVAL. Set switches 'I_ITL_ON' and 'I_SEL' = TRUE for this purpose.

![P control](images/35653882507_DV_resource.Stream@PNG-de-DE.png)

The step response of the P-controller within the time range is:  
PID_OUTV (t) = I_ITLVAL + GAIN * ER <sub>scaled </sub>(t)

![P control](images/33472499339_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| I_ITLVAL | Operating point of the P-controller |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(t) | Scaled control deviation |

##### PI control

The derivative action is disabled in the proportional-integraI controller (PI controller). (D_SEL = FALSE). A PI controller adjusts output variable PID_OUTV using the integral action until control deviation ER = 0. However, this only applies if the output variable does not exceed the limits of the control range.

The step response within the time range is:

![PI control](images/34003232779_DV_resource.Stream@PNG-en-US.png)

![PI control](images/33520548875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(0) | Step height of the scaled control deviation |
| TI | Integral-action time constant |

##### PD control

The integral action is disabled in the proportional-derivative controller (PD-controller) (I–SEL = FALSE). This means that when control deviation ER = 0, output signal OUTV = 0. If an operating point ≠ 0 is intended, i.e., a numeric value will be set for the output signal when the control deviation is zero, the integral action branch must be activated (see also the block diagram of the P control).

In the integral action, an operating point ≠ 0 can be specified for the PD-controller via a corresponding setting of initialization value I_ITLVAL. The switches 'I_ITL_ON' and 'I_SEL' must be set to TRUE for this purpose.

The PD-controller maps input variable ER(t) proportionally to the output signal and adds to this the derivative action generated by differentiation of ER(t); the derivative action is calculated with double precision according to the trapezoid rule (Padé approximation). The time response is determined by the derivative time constant TD.

For signal smoothing and suppression of interfering signals, a first-order delay (adjustable time: TM_LAG) is integrated into the algorithm for generating the derivative action. A small value for TM_LAG is usually sufficient to achieve the desired result. If TM_LAG ≤ CYCLE/2 is configured, the time delay is deactivated.

The step response within the time range is:

![PD control](images/33525271435_DV_resource.Stream@PNG-en-US.png)

![PD control](images/34003271947_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(0) | Step height of the scaled control deviation |
| TD | Derivative time |
| TM_LAG | Time delay |

##### PID control

In the proportional-integral-derivative controller (PID-controller), the proportional action, integral action, and derivative action are enabled (P–SEL = TRUE, I–SEL = TRUE, D_SEL = TRUE). A PID controller adjusts output variable PID_OUTV using the integral action until control deviation ER = 0. However, this only applies if the output variable does not exceed the limits of the control range. If manipulated variable limits are exceeded, the integral action maintains the value that was reached at the limit (anti-reset windup).

The PID-controller maps scaled input variable ER<sub>scaled</sub>(t) proportionally to the output signal and adds to this the components generated by differentiation and integration of ER<sub>scaled</sub>(t); these components are calculated with double precision according to the trapezoid rule (Padé approximation). The time response is determined by the derivative-action time TD and integral-action time TI.

For signal smoothing and suppression of interfering signals, a first-order delay (adjustable time constant: TM_LAG) is integrated into the algorithm for generating the derivative action. A small value for TM_LAG is usually sufficient to achieve the desired result. If TM_LAG ≤ CYCLE/2 is configured, the time delay is deactivated.

The step response within the time range is:

![PID control](images/33525435531_DV_resource.Stream@PNG-en-US.png)

![PID control](images/33525447179_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(0) | Step height of the scaled control deviation |
| TI | Integral-action time constant |
| TD | Derivative time |
| TM_LAG | Time delay |

> **Note**
>
> If TD is changed, you should also adjust TM_LAG accordingly.
>
> Recommendation: 5 ≤ (TM / TM_LAG) ≤ 10

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400)
  
[Proportional component (S7-300, S7-400)](#proportional-component-s7-300-s7-400)
  
[Derivative component (S7-300, S7-400)](#derivative-component-s7-300-s7-400)
  
[Integral action (S7-300, S7-400)](#integral-action-s7-300-s7-400)

#### Proportional component (S7-300, S7-400)

##### Proportional gain

The sign of this proportional gain determines the effective direction of the continuous controller.

- Positive proportional gain

  increasing control deviation → rising manipulated variable
- Negative proportional gain

  increasing control deviation → falling manipulated variable

##### Applying proportional action in feedback path

If the proportional action is applied to the feedback path, only the process value has an effect on the proportional action. Therefore, the manipulated variable does not undergo a step change due to the proportional action during a changeover from manual to automatic (also in the case of a setpoint step-change); the changeover is bumpless.

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400)

#### Integral action (S7-300, S7-400)

##### Function of the integral action

The integral action ensures that the control deviation can go to 0 for any manipulated variables by resetting the operating point.

The integral action generates an output signal whose rate of change is proportional to the change in the absolute value of the input variable. The time response is determined by the integral action time TI.

The step response to the input step inv<sub>0</sub> is:

![Function of the integral action](images/32396884491_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| LMN_I(t) | The output variable of the integral action |
| inv<sub>0</sub> | The step height at the input of the integral action |
| TI | Integral action time |

The integral action can be monitored at the static tag LMN_I.

In the deactivated state (I_SEL = FALSE), the integral action, i.e., the internal memory and the static tag LMN_I, is set to zero.

The output and the memory of the integral action are limited by the absolute limits of the manipulated variables LMN_HLM and LMN_LLM (Anti Reset Wind–up).

If the actuating signal is influenced in manual mode, i.e., if MAN_ON, LMNOP_ON, or CAS_ON = TRUE, the internal memory value of the integral action is corrected to the value LMNFC_IN - LMN_P - DISV.

![Function of the integral action](images/32396896395_DV_resource.Stream@PNG-de-DE.png)

##### Smooth changeover from manual to automatic

In manual mode, the integral action of the controller is corrected in such a manner that the controller starts with an appropriate manipulated variable upon switchover to automatic mode.

- Smooth changeover enabled (SMOO_CHG = TRUE)

  The integral action is set in manual mode in such a way that the manipulated variable initially remains unchanged on the switchover from manual to automatic.

  In manual mode, the derivative action is set to zero. The switchover to automatic is performed without manipulated variable step.

  A pending system deviation will be slowly corrected.
- Smooth changeover disabled (SMOO_CHG = FALSE)

  The manipulated variable makes a step from the actual position during the switchover from manual to automatic. The height of this step is determined by the proportional action. The step height of the proportional action corresponds to the manipulated variable change on a setpoint step change from the current process value to the current setpoint.

  In manual mode, the derivative action is set to a value that corresponds to the pending control deviation. The switchover to automatic mode is performed with a manipulated variable step; the control deviation is corrected faster.

  However, if the proportional action is applied to the feedback path, only the process value has an effect on the proportional action. Therefore, the manipulated variable does not undergo a step change due to the proportional action during a switchover from manual to automatic; the changeover is smooth. The same applies to the derivative action, if this was

  moved to the feedback path (DFDB_SEL = TRUE).

  The pending control deviation is corrected faster. This is desirable, for example, for temperature control processes.

##### Permissible ranges for the integral action time TI and CYCLE

The limited accuracy of the REAL numbers calculated in the CPU means that the following can occur during integration: If the selected sampling time CYCLE of the control is too short in comparison with the integral action time TI and the input value inv of the integral action is small compared to its output value OUTV, the integral action does not respond and remains at its current output value.

This effect can be avoided if the following sizing rule is observed during configuration:

CYCLE &gt; 10<sup>–4</sup> × TI

As a result, the integral action still responds to changes in the input values in the range of millionths of one part per thousand of the current output variable:

inv &gt; 10 <sup>–10 </sup>× OUTV

In order for the response characteristic of the integrator algorithm to conform to the analog response, the sampling time should be less than 20% of the specified integral action time or TI should be at least five times the value of the specified sampling time:

CYCLE &lt; 0.2 × TI

The algorithm permits sampling time values up to CYCLE ≤ 0.5 * TI.

##### Initializing the integral action

If initialization of the integral action is enabled, the initialization value is switched through to the static tag LMN_I at a restart of the CPU or COM_RST = TRUE. On the transition to normal operation, the integral action starts the integration of its input variable from the initialization value due to the resetting of the initialization.

##### Hold integral action

The integral action can be blocked in positive or negative direction by the static tags INT_HPOS and INT_HNEG. This can be useful for controller cascades. If, for example, the manipulated variable of the follow-up controller approaches the high limit, a further increase in the manipulated variable of the master controller can be prevented by its integral action. You program this response using the following instructions, for example, in STL:

A "Follow-up controller".QLMN_HLM

= "Master controller".INT_HPOS

A "Follow-up controller".QLMN_ LLM

= "Master controller".INT_HNEG

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400)
  
[Controller structures (S7-300, S7-400)](#controller-structures-s7-300-s7-400)

#### Derivative component (S7-300, S7-400)

##### Function of the derivative action

The derivative action generates an output signal whose size changes proportionally to the rate of change of the input variable. The time response is determined by the derivative time TD and the time delay TM_LAG.

The step response to the input step inv<sub>0</sub> is:

![Function of the derivative action](images/32396928267_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| LMN_D(t) | The output variable of the derivative action |
| inv<sub>0</sub> | The step height at the input of the derivative action |
| TD | Derivative-action time |
| TM_LAG | Time delay |

The derivative action can be monitored at the static tag LMN_D.

In the disabled state (D_SEL = FALSE), the derivative action, i.e., the internal memory and the static tag LMN_D, is set to zero.

##### Apply derivative action in feedback path

If the derivative action is applied to the feedback path, only the process value has an effect on the derivative action. Consequently – as in a setpoint jump – the manipulated variable does not undergo a step change due to the derivative action during a changeover from manual to automatic; the switchover is smooth.

##### Permitted values for derivative time and time delay.

To calculate the derivative action correctly, the following conditions must be satisfied for the derivative time and time delay:

- TD ≥ CYCLE and
- TM_LAG ≥ 0.5 × CYCLE

If TD &lt; CYCLE, the derivative action operates as though the TD has the value CYCLE.

If TM_LAG &lt; 0.5 × CYCLE, the derivative action operates without delay. An input step is then multiplied with the factor TD/CYCLE and this value is applied as "needle pulse" at the output. In other words, LMN_D is reset to zero in the subsequent processing cycle.

##### Coefficient DT1

The coefficient DT1 is calculated as follows:

Coefficient DT1 = TD/TM_LAG

##### Time delay

For signal smoothing and suppression of interfering signals, a first-order delay (adjustable time constant: TM_LAG) is integrated into the algorithm for generating the derivative action.

A small value for the time delay is usually sufficient to achieve the desired result. If the assigned time delay is less than half the controller sampling time, the delay is deactivated.

##### Procedure

To configure the derivative action, proceed as follows:

1. To apply the derivative action to the feedback path, select the corresponding check box.
2. Enter the derivative time in seconds.
3. Enter the time delay in seconds.

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400)

### Manipulated variable (S7-300, S7-400)

This section contains information on the following topics:

- [Manual mode (S7-300, S7-400)](#manual-mode-s7-300-s7-400)
- [Limiting functions (S7-300, S7-400)](#limiting-functions-s7-300-s7-400-1)
- [Scaling (S7-300, S7-400)](#scaling-s7-300-s7-400-1)
- [Pulse generator (S7-300, S7-400)](#pulse-generator-s7-300-s7-400)

#### Manual mode (S7-300, S7-400)

In addition to "automatic" mode, in which the output of the PID algorithm (PID_OUTV) is switched through to the output, there are two other operating modes in which the actuating signal can be influenced manually: "Manual mode without switch operation" and "Manual mode using more/less switch" (MAN_GEN).

The MAN parameter can be used to switch through an external manipulated variable or to specify it from the user program. Input value MAN is limited by the manipulated variable limits (LMN_HLM (high) and LMN_LLM (low)).

The structure of the manual value generation and manual value application emerges from the following figure. When MAN_GEN is activated from another mode, the current manipulated variable in effect is applied at the output of MAN_GEN. The changeover to the manual value generator is thus always bumpless.

![Figure](images/32396996491_DV_resource.Stream@PNG-de-DE.png)

##### Activating automatic mode

If manual mode is disabled (MAN_ON = FALSE), the manipulated variable of the PID algorithm is switched through to the output. In manual mode (MAN_ON = TRUE), the integral action of the controller is corrected such that the controller begins with an appropriate manipulated variable on changeover to automatic mode. The output of the PID algorithm is stored in measuring point MP7.

In automatic mode, the manual value MAN of the manipulated variable (minus the derivative action) is corrected. On changeover to manual mode, the manipulated variable is kept at the last calculated value. It can be changed via operator input.

1. Clear the "Activate manual mode" check box.

##### Activate manual mode with manual value

In this mode (MANGN_ON = FALSE and MAN_ON = TRUE), the manual output value is entered as an absolute value in the MAN input. The manual output value is displayed at measuring point MP8.

1. Select the "Activate manual mode" check box.
2. Choose the "Manual value" option.

##### Activate the manual value generator

The manual value MAN can be incremented or decremented in steps using the MANUP and MANDN switches. The modified value can be monitored at MP8. The configured manipulated variable limits are taken into account.

1. Select the "Activate manual mode" check box.
2. Select the "Manual value generator" option.

##### Effect of the switches MANUP and MANDN

For changes involving small steps, the controller should have a maximum sampling time of 100 ms.

The rate of change of the manipulated variable depends on how long the MANUP or MANDN switch is actuated and on the selected limits. The following relationship applies:

- During the first 3 s after setting MANUP or MANDN:

  doutv/dt = (LMN_HLM - LMN_LLM) / 100 s
- Afterwards:

  doutv/dt = (LMN_HLM - LMN_LLM) / 10 s

  ![Effect of the switches MANUP and MANDN](images/32397029003_DV_resource.Stream@PNG-de-DE.png)

For a sampling time of 100 ms and a manipulated variable range of -100.0 to 100.0, the manipulated variable, for example, changes by 0.2 per cycle during the first 3 seconds. If MANUP is TRUE for more than 3 seconds, the rate of changes increases to ten times the value, in this case therefore to 2 per cycle.

The manual value generator is activated bumpless.

##### Operating modes

The following table shows the possible operating modes of the continuous controller with the required values of the switches.

| Operating mode | MAN_ON | MANGN_ON |
| --- | --- | --- |
| Automatic mode | FALSE | Not relevant |
| Manual mode with manual value | TRUE | FALSE |
| Manual mode with manual value generator | TRUE | TRUE |

#### Limiting functions (S7-300, S7-400)

##### Calling a function

If you insert a user-specific function into the manipulated variable branch, the manipulated variable PID_OUTV generated in the controller can undergo signal processing (e.g., a signal delay) prior to application to the output of the controller.

The controller calls the function. In so doing, existing input/output parameters of the user function are not supplied. You have to program the data transfer in your function yourself.

> **Note**
>
> A check is not performed to determine whether a function exists. If the function does not exist, the CPU switches to STOP with an internal system error.

1. Select the "Enable FC call" check box.
2. Enter the number of the function in the "FC" input field.

##### Limiting the rate of change

Ramp functions will be used in the manipulated variable branch if the process does not tolerate abrupt changes in the controlled system input signal. These abrupt manipulated variable changes must be avoided, for example, when a gearbox is connected in between an adjustable-speed motor and the load to be driven and an excessively rapid increase of the motor speed would result in overloading of the gearbox.

The rate of change of the manipulated variable at the output of the controller is limited separately for the rising and falling slope. Two ramps with rising or falling values can be assigned for the entire value range, when seen from the zero point. The function is enabled if LMNRC_ON = TRUE.

The limiting for each slope of the ramp function in the positive range and in the negative range of the manipulated variable is entered in the two static variables LMN_URLM and LMN_DRLM. The slopes refer to a rising slope or falling slope in percent per second. Faster manipulated variable changes are ramped down to these maximum rates.

For example, if 'LMN_URLM' is assigned the value 10.0 [%/s], the following values are added to the "old value" of outv in each sampling cycle for as long as |inv| &gt; |outv|:

|  |  |  |  |
| --- | --- | --- | --- |
| Sampling time | 1 s | → | outv<sub>old</sub> + 10% |
|  | 100 ms | → | outv<sub>old</sub> + 1% |
|  | 10 ms | → | outv<sub>old</sub> + 0.1 % |

The figure below shows how the signal processing works: The step functions at input inv (t) become ramp functions at output outv (t).

![Limiting the rate of change](images/32397080203_DV_resource.Stream@PNG-de-DE.png)

When slope limits are reached, this is not signaled.

The ramp parameters are identified in accordance with the following scheme:

| Parameter | Ramp |
| --- | --- |
| LMN_URLM | |outv| rising |
| LMN_DRLM | |outv| falling |

1. Activate the "Limit rate of change" check box.
2. Enter the maximum increase of the manipulated variable in the "Maximum increase" field.

   Faster manipulated variable changes will be ramped down to this value.
3. Enter the maximum decrease of the manipulated variable in the "Maximum decrease" field.

   Faster manipulated variable changes will be ramped down to this value.

##### Limiting the absolute value of the manipulated variable

The operating range, i.e., the range in which the actuator can vary within the scope of permissible manipulated variables, is determined by the setting range of the manipulated variable. Since the limits for allowed manipulated variables usually do not coincide with the 0% or 100% limit of the correcting range, depending on the type of actuator, you can configure the high and low limit of the manipulated variable.

To avoid an impermissible status in the particular process, high and low limits for the setting range of the manipulated variable will be set in the manipulated variable branch of the closed-loop control.

The manipulated variable LMN(t) is limited to the assignable high limit (LMN_HLM) and low limit (LMN_LLM). However, the input variable inv must be outside these limits. Because the function cannot be deactivated, the specification of a low limit and high limit must be taken into consideration in the configuration.

In the event of violations by input variable inv(t), the associated displays are output via the message outputs.

![Limiting the absolute value of the manipulated variable](images/32397112075_DV_resource.Stream@PNG-de-DE.png)

##### Startup and operating principles

- During a restart, all message outputs are set to zero.
- The limiting operates according to the following relationships:

| LMN = | QLMN_HLM | QLMN_LLM | If: |
| --- | --- | --- | --- |
| LMN_HLM | TRUE | FALSE | inv ≥ LMN_HLM |
| LMN_LLM | FALSE | TRUE | inv ≤ LMN_LLM |
| inv | FALSE | FALSE | LMN_HLM &lt; inv &lt; LMN_LLM |

The effective manipulated value of the controller is displayed at the output, i.e. at the parameter LMN or at the measuring point MP10.

##### Procedure

To limit the absolute value of the manipulated variable, proceed as follows:

1. In the "High limit" input field, enter the value for the maximum permissible value.
2. In the "Low limit" input field, enter the value for the minimum permissible value.

#### Scaling (S7-300, S7-400)

If a physical quantity is required for the manipulated variable at the controlled process input, the floating-point values in the range from 0 to 100% must be unscaled to the physical range (e.g., 150 to 3000 rpm) of the manipulated variable.

Two parameters are defined for the unique specification of the scaling levels:

- The factor for the slope (LMN_FAC)
- The offset of the scaling level at the zero point (LMN_OFF)

Internal percentage values (in REAL format) ⇒ external physical values

![Figure](images/32397145227_DV_resource.Stream@PNG-de-DE.png)

The scaling value is calculated from the respective input value MP10 according to the following function:

LMN = MP10 * LMN_FAC + LMN_OFF

Example

![Figure](images/32397157131_DV_resource.Stream@PNG-en-US.png)

![Figure](images/32397169035_DV_resource.Stream@PNG-en-US.png)

Values are not limited internally in the function and the parameters are not checked.

##### Performing scaling

1. Enter the slope of the scaling level in the "Factor" input field.
2. Enter the offset of the scaling level with respect to the zero point in the "Offset" input field.

#### Pulse generator (S7-300, S7-400)

##### Application

The pulse generator transforms the input variable “Manipulated variable of PID controller at measuring point MP10" by modulating the pulse width into a pulse train with a constant period. The duration of a pulse per period is proportional to the input variable.

![Application](images/32397277195_DV_resource.Stream@PNG-de-DE.png)

An input variable of 30% and 10 calls of the pulse generator per period therefore means:

- "One" at the QPOS output for the first three calls (30% of 10 calls).
- "Zero" at the QPOS output for seven further calls (70% of 10 calls).

##### Operating modes of controller with pulse output

Depending on the parameter assignment of the pulse generator, PID controllers with a three-step response or with a bipolar or unipolar two-step output can be configured. The following table illustrates the setting of the switch combinations for the possible operating modes.

| Operating mode | Switch |  |  |
| --- | --- | --- | --- |
| MAN_ON | STEP3_ON | ST2BI_ON |  |
| Three-step control | FALSE | TRUE | Any |
| Two-step control with bipolar   Correcting range (-100% to 100%) | FALSE | FALSE | TRUE |
| Two-step control with unipolar   Correcting range (0% to 100%) | FALSE | FALSE | FALSE |
| Manual mode | TRUE | Any | Any |

##### Three-step control

In "Three-step control" mode, three control signal states can be generated, e.g., depending on the actuator and process: More – OFF – Less, Forward – Stop – Backward, Heat – OFF – Cool, etc. The status values of the binary output signals QPOS_P and QNEG_P are assigned to the respective operating states of the actuator, based on the requirements of the process being controlled. The table shows two examples.

|  | Heat  Forward | Off  Stop | Cool  Backward |
| --- | --- | --- | --- |
| QPOS_P | TRUE | FALSE | FALSE |
| QNEG_P | FALSE | FALSE | TRUE |

Selecting sizes for the minimum pulse time or minimum break time P_B_TM_P can prevent very short activation or deactivation times, which reduce the operating life of switch elements and actuating devices considerably. In so doing, a response value for the pulse output is superimposed on the proportional output characteristic curve used to calculate the pulse duration.

> **Note**
>
> Small absolute values of the "Manipulated variable of the PID controller at measuring point MP10" input variable that would generate a pulse duration less than P_B_TM_P are suppressed. For large input values that would generate a pulse duration longer than PER_TM_P – P_B_TM_P, the pulse duration is set to 100% or -100%.

Set values P_B_TM ≤ 0.1 * PER_TM are recommended.

![Three-step control](images/32397301003_DV_resource.Stream@PNG-en-US.png)

The duration of the positive or negative pulses are calculated by multiplying the "Manipulated variable of PID controller at measuring point MP10" input variable (in %) by the period:

![Three-step control](images/32397312907_DV_resource.Stream@PNG-en-US.png)

The suppression of the minimum pulse time or minimum break time causes bend points near the start and end of the conversion characteristic curve.

The above statements also apply to P_B_TM_N and PER_TM_N.

![Three-step control](images/32397324811_DV_resource.Stream@PNG-en-US.png)

##### Three-step control asymmetrical

Using the ratio factor RATIOFAC, the ratio of the duration of positive to negative pulses can be changed. In a thermal process, for example, this would allow different process time constants for heating and cooling to be included.

Assuming the absolute value of the "Manipulated variable of the PID controller at measuring point MP10" is the same, a shorter pulse duration at the negative pulse output than for the positive pulse requires a ratio factor setting less than 1:

![Three-step control asymmetrical](images/32397336715_DV_resource.Stream@PNG-en-US.png)

![Asymmetrical characteristic curve of the three-step controller (ratio factor = 0.5)](images/32397348619_DV_resource.Stream@PNG-en-US.png)

Asymmetrical characteristic curve of the three-step controller (ratio factor = 0.5)

On the other hand, for the same absolute value |MP10|, a shorter pulse duration at the positive pulse output compared to the negative pulse requires a ratio factor setting greater than 1:

![Three-step control asymmetrical](images/32397373323_DV_resource.Stream@PNG-en-US.png)

Mathematically, this means that when RATIOFAC &lt; 1, the response value for negative pulses is multiplied by the ratio factor and when RATIOFAC &gt; 1, the response value for positive pulses is divided by the ratio factor.

> **Note**
>
> For asymmetrical three-step control RATIOFAC ≠ 1, you must adapt the manipulated variable limits according to the following formulas:
>
> **RATIOFAC &lt; 1:**
>
> LMN_HLM = 100
>
> LMN_LLM = –100 * (1 / RATIOFAC)
>
> **RATIOFAC &gt; 1:**
>
> LMN_HLM = 100 * RATIOFAC
>
> LMN_LLM = –100

Examples:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RATIOFAC | = | 1 |  | RATIOFAC | = | 0.5 |  | RATIOFAC | = | 2.0 |
| LMN_HLM | = | 100 |  | LMN_HLM | = | 100 |  | LMN_HLM | = | 200 |
| LMN_LLM | = | –100 |  | LMN_LLM | = | –200 |  | LMN_LLM | = | –100 |

##### Two-step control

In two-step control, only the positive pulse output QPOS_P is connected to the affected on/off actuator. Depending on the correcting range used, MP10 = -100.0% to +100.0% or MP10 = 0.0% to 100.0%, the two-step controller has a bipolar or unipolar correcting range.

In unipolar operating mode, MP10 may assume values between 0.0% and 100.0% only.

![Two-step control](images/32397397131_DV_resource.Stream@PNG-en-US.png)

In bipolar operating mode, MP10 may assume values between -100.0% and 100.0%.

![Two-step control](images/32397385227_DV_resource.Stream@PNG-en-US.png)

The negated output signal is available at QNEG_P in case the interconnection of the two-step controller in the control loop requires a logically inverted binary signal for the actuating pulses.

|  | On | Off |
| --- | --- | --- |
| QPOS_P | TRUE | FALSE |
| QNEG_P | FALSE | TRUE |

##### Controller sampling time CYCLE and pulse pattern width CYCLE_P

If you have activated the pulse generator stage (PULSE_ON = TRUE), you must specify the cycle clock of the calling cyclic interrupt OB in the CYCLE_P input. The duration of the generated pulse is always an integer multiple of this value.

At the CYCLE input, you specify the sampling time for the remaining control functions of the PID_CP. PID_CP determines the time scaling and processes the control functions with the sampling time CYCLE.

CYCLE must be an integer multiple of CYCLE_P. If you do not adhere to this condition, PID_CP rounds up the sampling time for the control functions to an integer multiple of CYCLE_P. The time-dependent functions (e.g., smoothing, integration, differentiation) will then not work correctly to some extent.

The value selected for CYCLE can be less than the period PER_TM_P or PER_TM_N. This is useful if the longest possible period is desired to protect the actuators, but at the same time very short sampling times are required due to a fast process.

The same guideline applies here to the selection of the sampling time CYCLE as for continuous controllers without a pulse generator stage: the value of CYCLE should not be less than approximately 10% of the dominating process time constants of the controlled system.

Example of the effect of the CYCLE_P, CYCLE and PER_TM_P or PER_TM_N parameters:

- PER_TM_P = 10 s, CYCLE = 1 s, CYCLE_P = 100 ms.

A new manipulated variable is calculated every second, and the manipulated variable is compared with the previously output pulse length or break length every 100 ms.

If a pulse is output and calculate manipulated variable is greater than the previous pulse length/PER_TM_P, the pulse is extended. Otherwise, no more pulse signals are output. If no pulse is output and (100% - calculated manipulated variable) is greater than the previous break length/PER_TM_P, the break is extended. Otherwise, a pulse signal is output.

As a result of a special pulse generation procedure, an increase or decrease in the manipulated variable during the period causes the output pulse to be extended or shortened. In this case (CYCLE &lt; PER_TM_P), if the configured period is so long that it would cause the process value to fluctuate, the effective period of PID_CP is automatically reduced to an appropriate value.

##### Accuracy of pulse generation

The period PER_TM is not identical with the processing cycle of the pulse generator. A period is comprised of several processing cycles of the pulse generator. The number of calls of the pulse generator per period is a measure for the accuracy of the pulse width.

The smaller the sampling time CYCLE_P is compared to the period duration PER_TM_P (or PER_TM_N), the more precise the pulse width modulation is. To achieve sufficiently accurate control, the following condition should be met:

![Accuracy of pulse generation](images/32397289099_DV_resource.Stream@PNG-de-DE.png)

##### Realization of very short sampling times

A fast process requires very small sampling times (for example, 10 ms). Due to the program runtime in this case, it is not appropriate to process the control functions in the same cyclic interrupt OB where the pulse output is calculated. You then transfer the processing of the control functions either to the OB 1 or to a slower cyclic interrupt OB. The processing of the control functions in OB 1 is only recommended if the cycle time of OB 1 is significantly less than the sampling time CYCLE of the controller.

Use the SELECT parameter to specify which program section is to be processed. The following table provides a quick overview of the parameter assignment of the SELECT input parameter:

| SELECT | Block functionality used | Underlying method |
| --- | --- | --- |
| 0 | Control functions and pulse output | Control functions and pulse output in one and the same block |
| 1 | Call in OB 1 (control functions) | Control functions in OB 1, pulse output in fast cyclic interrupt OB |
| 2 | Call in cyclic interrupt OB  (pulse output) |  |
| 3 | Call in slow cyclic interrupt OB (control functions) | Control functions in slow cyclic interrupt OB, pulse output in fast cyclic interrupt OB |
| 2 | Call in fast cyclic interrupt OB (pulse output) |  |

The methods for achieving very short pulse pattern widths indicated in the table above are described in more detail below.

- Control functions in OB 1, pulse output in cyclic interrupt OB

  When called with SELECT = 2, the pulse output is calculated and a test is performed to determine whether the sampling time configured in CYCLE has already elapsed since the last time the control functions were processed. If the sampling time has elapsed, PID_CP writes the value TRUE in the QC_ACT variable in the instance DB.

  When called with SELECT = 1, the QC_ACT variable is evaluated in the instance DB: If the value of QC_ACT is FALSE, the block is stopped immediately; thus, only a very brief execution time is required. If the value of QC_ACT is TRUE, the control functions are executed once and the QC_ACT is then reset.

  As a result of this procedure, the exact sampling time for the control functions cannot be adhered to. It fluctuates by the amount of the execution time of OB 1 (including all interruptions). This process is therefore only suitable when the execution time of OB 1 is less than the sampling time CYCLE.
- Control functions in slow cyclic interrupt OB, pulse output in fast cyclic interrupt OB

  When called with SELECT = 2, the pulse output is always calculated.

  When called with SELECT = 3, the control functions are always processed.

  > **Note**
  >
  > To prevent having to program the PID_CP instruction call twice, along with its many formal operands, it is advisable to program this call once in an FC that also has a SELECT parameter as an input parameter. Interconnect this input parameter to PID_CP.SELECT. You then call only this FC in OB 1 or in the cyclic interrupt OB.
  >
  > This procedure is easy to modify and saves program memory.

### Commissioning PID_CP (S7-300, S7-400)

This section contains information on the following topics:

- [Performing tuning manually (S7-300, S7-400)](#performing-tuning-manually-s7-300-s7-400)
- [Commissioning with the PID Self Tuner (S7-300, S7-400)](#commissioning-with-the-pid-self-tuner-s7-300-s7-400)

#### Performing tuning manually (S7-300, S7-400)

##### Requirements

- The instruction and the technology object have been loaded to the CPU.
- MAN_ON = FALSE

##### Procedure

In order to manually determine the optimal PID parameters, proceed as follows:

1. Click the "Measurement on" ![Procedure](images/23498796811_DV_resource.Stream@PNG-de-DE.png) icon.

   An online connection will be established, if one is not already present. The current values for the setpoint, process value and manipulated variable are recorded.
2. Enter new PID parameters in the "P", "I", "D" and "Time delay" fields.
3. Click on the icon ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png)"Send parameter to CPU" in the "Tuning" group.
4. Select the "Change setpoint" check box in the "Current values" group.
5. Enter a new setpoint and click in the "Current Values" group on the icon ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png).

   If the setpoint's rate of change is limited, the changeover to the new setpoint will be bumpless
6. Clear the "Manual mode" check box, if necessary.

   The controller works with the new PID parameters and controls the new setpoint.
7. Check the quality of the PID parameter based on the curve points.
8. Repeat steps 3 to 8 until you are satisfied with the controller results.

#### Commissioning with the PID Self Tuner (S7-300, S7-400)

You can commission the PID_CP instruction and determine the optimum PID parameters with the PID Self Tuner.

##### Procedure

To commission a continuous controller, proceed as follows:

1. Call the instruction PID_CP in a cyclic interrupt OB and interconnect the input and output parameters.
2. Call the instruction TUN_EC in the same cyclic interrupt OB.
3. Interconnect the instruction TUN_EC as follows with PID_CP:

   - TUN_EC.PV with PID_CP.PV
   - TUN_EC.LMN with PID_CP.LMN
   - TUN_EC.SP_OUT with PID_CP.SP_IN or PID_CP.SP_EXT
   - TUN_EC.GAIN with PID_CP.GAIN
   - TUN_EC.TI with PID_CP.TI
   - TUN_EC.TD with PID_CP.TD
   - TUN_EC.TM_LAG with PID_CP.TM_LAG
   - If you are using a three-step controller, TUN_EC.RATIOFAC with PID_CP.RATIOFAC
   - TUN_EC.QMAN_ON with PID_CP.MAN_ON
4. Click the "![Procedure](images/35383750539_DV_resource.Stream@PNG-de-DE.png)" icon on the instruction TUN_EC.

   The commissioning editor for TUN_EC opens. The operation of the commissioning editor is described with the PID Self Tuner.

## Using PID_ES (S7-300, S7-400)

This section contains information on the following topics:

- [Technology object PID_ES (S7-300, S7-400)](#technology-object-pid_es-s7-300-s7-400)
- [Control deviation generation (S7-300, S7-400)](#control-deviation-generation-s7-300-s7-400-1)
- [Controller (S7-300, S7-400)](#controller-s7-300-s7-400-1)
- [Manipulated variable (S7-300, S7-400)](#manipulated-variable-s7-300-s7-400-1)
- [Commissioning PID_ES (S7-300, S7-400)](#commissioning-pid_es-s7-300-s7-400)

### Technology object PID_ES (S7-300, S7-400)

The PID_ES technology object provides a step controller for automatic and manual mode. It corresponds to the instance data block of the instruction PID_ES. You can configure the following controllers:

- Fixed setpoint control with P, PI, PD, PID step controllers
- Step controllers with and without position feedback
- Fixed setpoint control with disturbance variable selection
- Cascade control with step controller in the follow-up circuit
- Two-loop ratio control
- Blending control

You configure the following functions of the technology object PID_ES:

- Scaling the process value signal
- Suppression of high-frequency vibrations in the process value branch by smoothing (time delay) of the process value signal.
- Linearization of the quadratic functions of the process value (flow-rate control with differential pressure encoders)
- Calling of "own functions" in the process value branch
- Monitoring the process value for violation of alarm and warning limits
- Monitoring the rate of change of the process value
- Adjustment of the setpoint by ramp/soak
- Scaling an external setpoint signal with ratio controllers
- Calling of "own functions" in the setpoint branch
- Limiting the rate of change of the setpoint
- Limiting the absolute values of the setpoint
- Filtering the control deviation signal with a deadband
- Monitoring the control deviation for violation of alarm and warning limits
- The proportional, integral, and derivative actions can be activated separately.
- Option of proportional and derivative effect in the controller feedback path.
- Selecting a disturbance variable
- Enabling position feedback
- Control of the manipulated variable in manual mode from a PG or HMI)
- Limiting the absolute values of the manipulated variable
- Taking into account actuator-specific times when generating the pulse

### Control deviation generation (S7-300, S7-400)

This section contains information on the following topics:

- [Process value (S7-300, S7-400)](#process-value-s7-300-s7-400-1)
- [Setpoint (S7-300, S7-400)](#setpoint-s7-300-s7-400-1)
- [Control deviation (S7-300, S7-400)](#control-deviation-s7-300-s7-400-1)

#### Process value (S7-300, S7-400)

This section contains information on the following topics:

- [Scaling (PV_NORM) (S7-300, S7-400)](#scaling-pv_norm-s7-300-s7-400-1)
- [Filter functions (S7-300, S7-400)](#filter-functions-s7-300-s7-400-1)
- [Alarm (S7-300, S7-400)](#alarm-s7-300-s7-400-2)

##### Scaling (PV_NORM) (S7-300, S7-400)

The "I/O process value ON" check box is used to specify which analog input variables are scaled to the physical unit of the process value.

- Activated: Input variable is the I/O process value (PV_PER)
- Disabled: Input variable is the internal process value (PV_IN)

In order to uniquely specify the scaling levels, you define the following four parameters:

- High input (NM_PIHR)
- Low input (NM_PILR)
- High output (NM_PVHR)
- Low output (NM_PVLR)

The parameters are preset depending on the sensor type.

The process value is calculated from the respective input value (PV_PER or PV_IN) according to the following formula:

MP4 = (PV_PER - NM_PILR) × (NM_PVHR - NM_PVLR) / (NM_PIHR - NM_PILR) + NM_PVLR

or

MP4 = (PV_IN - NM_PILR) × (NM_PVHR - NM_PVLR) / (NM_PIHR - NM_PILR) + NM_PVLR

![Figure](images/32396288651_DV_resource.Stream@PNG-de-DE.png)

The process value is output in the static variable MP4.

No values are limited and the parameters are not checked. If you enter the same value for input high and input low, a division by zero may occur based on the formulas above. The instruction will not detect this.

##### Filter functions (S7-300, S7-400)

This section contains information on the following topics:

- [Smooth controlled variable (LAG1ST) (S7-300, S7-400)](#smooth-controlled-variable-lag1st-s7-300-s7-400-1)
- [Square root (SQRT) (S7-300, S7-400)](#square-root-sqrt-s7-300-s7-400-1)
- [FC call in the process value branch (PVFC) (S7-300, S7-400)](#fc-call-in-the-process-value-branch-pvfc-s7-300-s7-400-1)

###### Smooth controlled variable (LAG1ST) (S7-300, S7-400)

In order to smooth process signals with superimposed rapid variations (noise), a first-order delay element is applied in the process value branch. This function stabilizes the analog controlled variable to a greater or lesser degree, depending on the time constant (PV_TMLAG). In this way, disturbances are effectively suppressed. As a result of this, however, the time constant of the overall control loop also increases, i.e., the closed-loop control becomes more sluggish.

The stabilizing effect is achieved by a first-order delay algorithm.

The step response within the time range is:

outv(t) = MP4(0) (1 - e<sup> -t/PV_TMLAG</sup>)

![Figure](images/32396371467_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| MP4(0) | The height of the process value step at the input |
| outv(t) | The output variable |
| PV_TMLAG | The time lag constant |
| t | Time |

###### Smoothing of the process value

If smoothing of the process value (LAG1STON = FALSE) is not activated, then the I/O input (PV_PER) or the internal input (PV_IN) is switched through to the process value branch without a delay.

###### Time lag

The PV_TMLAG input parameter specifies the time lag for the process value. Any value within the value range is permitted.

If PV_TMLAG ≤ 0.5 * CYCLE, there is no longer any lag in effect.

A sampling time (CYCLE) of less than one-fifth of the time lag is required in order to achieve a lag response approaching that of the analog response.

###### Square root (SQRT) (S7-300, S7-400)

The "Square root" function (SQRT) is used to linearize the controlled variable. If the process value supplied by an encoder is a physical quantity and there is a quadratic relation between this quantity and the measured process variable, the characteristic of the controlled variable must be linearized prior to any further processing in the controller.

The measured signal must always be linearized by the square-root function if flow measurements are made using metering orifices, venturi tubes, or the like. The measured pressure differential is then proportional to the square of the flow.

The SQRT_ON = TRUE input signal is used to activate the square root function in the process value branch. The square root function algorithm has the following form:

outv = SQRT (MP5) × (SQRT_HR – SQRT_LR) / 10.0 + SQRT_LR

Here, outv is the scaled output value of the square root function (physical flow).

This formula stipulates that the input value of the square root is scaled to the number range 0 to 100. The parameters for the "Measuring range high" and "Measuring range low" must be set to 100.0 and 0.0 in the scaling of the process value. The square root of this value yields a measuring range from 0 to 10. This range of numbers is scaled using the high limit (SQRT_HR) and the low limit of the physical measuring range (SQRT_LR).

![Figure](images/32396416139_DV_resource.Stream@PNG-de-DE.png)

###### Example of scaling

The input value PV_IN of the controller is the differential pressure in mbar:

| Start of measuring range NM_PILR | End of measuring range NM_PIHR | Sample value for PV_IN |
| --- | --- | --- |
| 20.0 mbar | 200.0 mbar | 150.0 mbar |

The scaled differential pressure is calculated with the help of the scaling function PV_NORM, whereby NM_PVHR = 100.0 and NM_PVLR = 0.0 are selected:

|  |  |  |
| --- | --- | --- |
| MP4 | = | (PV_IN - NM_PILR) * (NM_PVHR - NM_PVLR) /    (NM_PIHR - NM_PILR) + NM_PVLR |
|  | = | (PV_IN - 20.0 mbar) * (100.0 - 0.0) /    (200.0 mbar - 20.0 mbar) + 0.0 |
|  | = | (PV_IN - 20.0 mbar) * 100 / 180.0 mbar |

| Initial value of MP4 | End value of MP4 | Sample value for MP4 |
| --- | --- | --- |
| 0.0 | 100.0 | 72.222 |

Since no smoothing is used in this example, the following applies: MP5 = MP4.

For the square root from the scaled differential pressure MP5, the result is:

| Initial value according to the square root | End value according to the square root | Sample value for SQRT(MP5) |
| --- | --- | --- |
| 0.0 | 10.0 | 8.498 |

For the scaled output value outv of the square root function (physical flow-rate) with SQRT_HR = 20000.0 m<sup>3</sup>/h and SQRT_LR = 0.0 m3/h, there follows:

|  |  |  |
| --- | --- | --- |
| outv | = | SQRT(MP5) * (SQRT_HR - SQRT_LR) / 10.0 + SQRT_LR |
|  | = | SQRT(MP5) * (20000.0 m<sup>3</sup>/h - 0.0 m3/h) / 10.0 + 0.0 m3/h |
|  | = | 2000.0 m<sup>3</sup>/h * SQRT(MP5) |

| Start of measuring range outv | End of measuring range outv | Sample value for outv |
| --- | --- | --- |
| 0.0 m<sup>3</sup>/h | 20000.0 m<sup>3</sup>/h | 16996.732 m<sup>3</sup>/h |

###### FC call in the process value branch (PVFC) (S7-300, S7-400)

Insertion of a user-specific function in the process value branch allows the controlled variable to undergo signal processing, e.g., signal delay or linearization, prior to any further processing in the controller.

###### Calling a function

If you want to insert a user-specific function into the process value branch, enable "Enable FC call" (PVFC_ON). The number of the utilized function is entered in the "FC number" input field (PVFC_NBR). The controller calls the function. In so doing, existing input/output parameters of the user function are not supplied. You have to program the data transfer in your function yourself.

You can monitor the output value of the function at the static variable MP6.

> **Note**
>
> No check is made to determine whether a function exists. If the function does not exist, the CPU switches to STOP with an internal system error.

##### Alarm (S7-300, S7-400)

This section contains information on the following topics:

- [Monitor process value for limit values (PV_ALARM) (S7-300, S7-400)](#monitor-process-value-for-limit-values-pv_alarm-s7-300-s7-400-1)
- [Monitor rate of change of the process value (ROCALARM) (S7-300, S7-400)](#monitor-rate-of-change-of-the-process-value-rocalarm-s7-300-s7-400-1)

###### Monitor process value for limit values (PV_ALARM) (S7-300, S7-400)

If the values of the process variables (e.g., speed, pressure, filling level, temperature, etc.) exceed or fall below certain values in closed-loop controls, an illegal process status or plant status can occur. In such cases, monitoring of the process value for limit values (PV_ALARM) is used in order to monitor the process value for violation of the permissible operating range. Limit violations are detected and signaled so that an appropriate reaction can be initiated.

> **Note**
>
> The monitoring of the process value for limit values cannot be deactivated. The violation of the configured limits is always signaled.

Monitoring of the process value for limit values (PV_ALARM) monitors the controlled variable PV(t) for four assignable limits in two tolerance bands. If the limits are reached or exceeded, the function signals a “warning” at the first limit and an “alarm” at the second limit.

###### Limit values

The numeric values of the limits are set in the input parameters for “warning” and “alarm”. If the process value (PV) exceeds or falls below these limits, the associated output message bits are set for the high alarm (QPVH_ALM), the high warning (QPVH_WRN), the low warning (QPVL_WRN), and the low alarm (QPVL_ALM).

During a restart, the message bits are reset.

The message bits are set as follows:

| QPVH_ALM | QPVH_WRN | QPVL_WRN | QPVL_ALM | If: | And: |
| --- | --- | --- | --- | --- | --- |
| TRUE | TRUE | FALSE | FALSE | PV ↗  PV ↘ | PV ≥ PVH_ALM  PV ≥ PVH_ALM **-** PV_HYS |
| FALSE | TRUE | FALSE | FALSE | PV ↗  PV ↘ | PV ≥ PVH_WRN  PV ≥ PVH_WRN **-** PV_HYS |
| FALSE | FALSE | TRUE | FALSE | PV ↘  PV ↗ | PV ≤ PVL_WRN  PV ≤ PVL_WRN **+** PV_HYS |
| FALSE | FALSE | TRUE | TRUE | PV ↘  PV ↗ | PV ≤ PVL_ALM  PV ≤ PVL_ALM **+** PV_HYS |

The following has to apply so that the block operates properly:

High alarm &lt; High warning &lt; Low warning &lt; Low alarm

![Limit values](images/32396518539_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | 1. Tolerance band |
| ② | 2. Tolerance band |

###### Hysteresis

In order to prevent "flickering" of the message bits when the input variable undergoes slight changes or in the event of rounding errors, a hysteresis PV_HYS is used. The controlled variable must violate the hysteresis before the message bits are reset.

###### Monitor rate of change of the process value (ROCALARM) (S7-300, S7-400)

If the change in the process variable (e.g., speed, pressure, filling level, temperature, etc.) is too great in closed-loop controls, an illegal process status or plant status can occur. In such cases, monitoring the rate of change of the process value (ROCALARM) is used to monitor the process value for violations of a permissible rate of change. Limit violations are detected and signaled so that an appropriate reaction can be initiated.

> **Note**
>
> Monitoring of the rate of change of the process value (ROCALARM) cannot be deactivated. The violation of the configured limits is always signaled.

The ROCALARM function monitors the controlled variable PV(t) for permissible rate-of-change limits that are assignable according to sign.

The numeric values of the limit slopes are set at the input parameters for "Maximum increase" and "Maximum decrease" in the positive and negative range of the controlled variable. The slopes refer to a rising slope or falling slope in percent per second. If the rate of change of the controlled variable violates these limits, the associated output message bit QPVURLMP ... QPVDRLMN is set.

![Figure](images/32396576011_DV_resource.Stream@PNG-de-DE.png)

The ramp parameters are identified in accordance with the following scheme:

| Parameter | PV change |
| --- | --- |
| Maximum increase in the positive range (PVURLM_P) | PV &gt; 0 and |PV| rising |
| Maximum decrease in the positive range (PVDRLM_P) | PV &gt; 0 and |PV| falling |
| Maximum increase in the negative range (PVURLM_N) | PV &gt; 0 and |PV| rising |
| Maximum decrease in the negative range (PVDRLM_N) | PV &lt; 0 and |PV| falling |

#### Setpoint (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying a setpoint (S7-300, S7-400)](#specifying-a-setpoint-s7-300-s7-400-1)
- [Setpoint generator (SP_GEN) (S7-300, S7-400)](#setpoint-generator-sp_gen-s7-300-s7-400-1)
- [Ramp/soak (RMP_SOAK) (S7-300, S7-400)](#rampsoak-rmp_soak-s7-300-s7-400-1)
- [Scaling (S7-300, S7-400)](#scaling-s7-300-s7-400-2)
- [Limiting functions (S7-300, S7-400)](#limiting-functions-s7-300-s7-400-2)

##### Specifying a setpoint (S7-300, S7-400)

Select a source for the setpoint. The following options are available:

- Internal setpoint

  The input parameter SP_INT is used as setpoint
- Setpoint generator

  The input parameter SP_INT is used as setpoint and can be incremented or decremented using the static variables SPUP and SPDN.
- Ramp/soak

  The input parameter SP_INT is used as setpoint and can be changed according to a specified ramp/soak.
- External setpoint

  The input parameter SP_EXT is used as setpoint for blending, ratio and cascade controllers. The external setpoint can be scaled.

The effective setpoint is shown at the output parameter SP.

---

**See also**

[Ramp/soak (RMP_SOAK) (S7-300, S7-400)](#rampsoak-rmp_soak-s7-300-s7-400-1)

##### Setpoint generator (SP_GEN) (S7-300, S7-400)

The internal setpoint SP_INT can be incremented or decremented in steps using the SPUP and SPDN switches. The modified value can be monitored at MP1. The configured setpoint limits are taken into account.

###### Effect of the switches SPUP and SPDN

For changes involving small steps, the controller should have a maximum sampling time of 100 ms.

The rate of change of the output variable depends on how long the SPUP or SPDN switch is actuated and on the selected limits. The following relationship applies:

- During the first 3 s after setting SPUP or SPDN:

  doutv/dt = (SP_HLM - SP_LLM) / 100 s
- Afterwards:

  doutv/dt = (SP_HLM - SP_LLM) / 10 s

  ![Effect of the switches SPUP and SPDN](images/32395861771_DV_resource.Stream@PNG-en-US.png)

For a sampling time of 100 ms and a setpoint range of -100.0 to 100.0, the setpoint, for example, changes by 0.2 per cycle during the first 3 seconds. If SPUP is TRUE for more than 3 seconds, the rate of changes increases to ten times the value, in this case therefore to 2 per cycle.

###### Startup and operating principles of the setpoint generator

- During a complete restart, output outv is reset to 0.0.
- If you activate the setpoint generator (SPGEN_ON = TRUE), the signal value SPFC_IN is output initially at output outv. Therefore, the switchover to the setpoint generator from another operating mode is always smooth. Provided the SPUP and SPDN (up/down keys) are not activated, the signal value SPFC_IN is retained at the output.

###### Parameters of the SP_GEN function

Output parameter outv is an implicit parameter. It can be monitored with the configuration tool via measuring point MP1.

| Parameter | Meaning | Permitted value range |
| --- | --- | --- |
| SPFC_IN | FC input setpoint | Engineering value range |
| SP_INT | Internal setpoint | Engineering value range |

![Function scheme and parameters of the setpoint generator](images/37537528331_DV_resource.Stream@PNG-de-DE.png)

Function scheme and parameters of the setpoint generator

##### Ramp/soak (RMP_SOAK) (S7-300, S7-400)

If you want the setpoint SP_INT to change autonomously depending on the time, for example, during the control of processes after a time-controlled temperature program, this is possible by configuring a ramp/soak and activating the ramp/soak function. The setpoint change is formed from the level sections with a maximum of 256 time slices.

> **Note**
>
> The block function does not check whether a global DB with the number 'DB_NBR' exists or whether the parameter 'Number of time slices' NBR_PTS corresponds to the data block length. If the parameter assignment is incorrect, the CPU goes to **STOP** and issues an internal system error.

###### How the ramp/soak works

The ramp/soak supplies the output variable outv according to a function that runs to a defined ramp/soak. The ramp/soak process is defined by specifying a series of time slices in a global data block DB_RMPSK with time values PI[i].TMV and the associated output values PI[i].OUTV.

- PID-CP

  [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400) is not included in the library. You must create this global data block yourself.
- PID-ES

  [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400-1) is not included in the library. You must create this global data block yourself.

The following figure shows a ramp/soak with 6 time slices.

![How the ramp/soak works](images/32395896843_DV_resource.Stream@PNG-de-DE.png)

The time value for the last time slice n is PI[n].TMV = 0 ms. The processing time of a ramp/soak is counted down from the initial value to zero.

PI[i].TMV specifies the intervals between time slices. Between the time slices, interpolation is according to the following function:

![How the ramp/soak works](images/32395933451_DV_resource.Stream@PNG-de-DE.png)

0 ≤ n ≤ (NBR_PTS - 1)

![How the ramp/soak works](images/32395921547_DV_resource.Stream@PNG-en-US.png)

Note

> **Note**
>
> During the interpolation of the ramp/soak between the time slices, pauses can sometimes occur at the initial value if the sampling time CYCLE is very small compared to the time between the time slices PI[n].TMV. Due to the computational accuracy of the CPU, the ramp/soak function cannot linearize all flat ramp/soak profiles. If the ramp/soak profile is too flat, the initial value pauses for a time at the respective time slice and continues, after a certain time, to integrate with the minimum rate of rise to the next time slice.
>
> To correct or avoid error: Shorten the time between the time slices by inserting additional time slices. The output ramp/soak profile thus approximates the desired flat ramp/soak profile.

###### Ramp/soak function ON

The ramp/soak function is activated by changing RMPSK_ON from FALSE to TRUE. The ramp/soak is terminated after the last time slice has been reached. When the function is started again by the operator, RMPSK_ON first has to be set to 'FALSE' and then back to 'TRUE' .

During a **restart**, the output outv is reset to 0.0 and the total time or total remaining time is determined. During the transition to normal operation, the ramp/soak profile is processed immediately from the starting point according to the set operating mode. If this is not desired, the parameter RMPSK_ON must be set to FALSE in the restart OB.

###### Ramp/soak functions

The instruction has the following functions:

- Activate ramp/soak for single execution
- Pre-assign fixed value to the output
- Cyclic repetition on
- Hold ramp/soak
- Continue ramp/soak
- Update the total processing time and remaining total time

The following table applies for the significance of the control inputs when setting a desired operating mode:

| Operating mode | RMPSK_ON | DFOUT_ON | RMP_ HOLD | CONT_ ON | CYC_ ON | TUPDT_ON | Output signal OUTV |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ramp/soak on | TRUE | FALSE | FALSE | **) | FALSE | **) | OUTV(t)  End value is held after the end of processing. |
| Set output | TRUE | TRUE | **) | **) | **) | **) | DF_OUTV |
| Cyclic repetition on | TRUE | FALSE | FALSE | **) | TRUE | **) | OUTV(t)  After end: Automatic start |
| Hold ramp/soak | TRUE | FALSE | TRUE | FALSE | **) | **) | Current value of OUTV(t) is held *) |
| Continue ramp/soak | TRUE | FALSE | TRUE | TRUE | **) | **) | OUTV (old) *) |
| FALSE | Operation is continued with newly defined values. |  |  |  |  |  |  |
| Updating the total time and remaining total time | **) | **) | **) | **) | **) | FALSE | Does not influence OUTV |
|  | TRUE | Does not influence OUTV |  |  |  |  |  |
| *) The ramp/soak profile does not have the form configured by the user until the next time slice.  **) The respective operating mode set is executed irrespective of the significance of the control signals in the fields marked with **) |  |  |  |  |  |  |  |

###### Set output of ramp/soak

If you enable this function (DFRMP_ON = TRUE), the output value of the ramp/soak is set to signal value SP_INT or output value SP_GEN.

> **Note**
>
> Preassignment with the internal setpoint has an effect only if the ramp/soak function is enabled (RMPSK_ON = TRUE).

After the switchover to DFRMP_ON = FALSE, outv moves linearly from the specified setpoint (e.g., SP_INT) to the output value of the current time slice number PI[NBR_ATMS].OUTV.

The internal time processing continues running even when a fixed setpoint (RMPSK_ON = TRUE and DFRMP_ON = TRUE) is switched through.

On the start of the ramp/soak profile (RMPSK_ON = TRUE), the fixed setpoint SP_INT continues to be output until DFRMP_ON changes from TRUE to FALSE after the duration of T*.

![Set output of ramp/soak](images/32395945355_DV_resource.Stream@PNG-en-US.png)

At this moment, the time PI[0].TMV and a part of the time PI[1].TMV has expired. OUTV is moved from SP_INT to PI[2].OUTV, which means to the setpoint at time slice 2.

The configured ramp/soak profile is output only starting from time slice 2. The agreement of the configured and current ramp/soak profile is displayed by setting QR_S_ACT = TRUE. On a rising edge at DFRMP_ON during processing of the ramp/soak profile, the output value OUTV jumps to SP_INT without a delay.

###### Cyclic repetition on

If "Cyclic repetition" operating mode (CYC_ON = TRUE) is activated, the ramp/soak function automatically returns to the starting point after the last time slice value has been output and begins a new run.

There is no interpolation between the last time slice and the starting point. For a smooth transition, the following must be true: PI[NBR_PTS].OUTV = PI[0].OUTV.

###### Hold ramp/soak

When RMP_HOLD = TRUE, the value of the output variable (including the time processing) is frozen. When RMP_HOLD = FALSE is reset, the function resumes at the interruption point PI[x].TMV.

![Hold ramp/soak](images/32395957259_DV_resource.Stream@PNG-en-US.png)

The processing time of the ramp/soak profile is extended by the amount of the time T*. The ramp/soak profile has the configured course from the starting point until the rising edge at RMP_HOLD and from time slice 5* to time slice 6*, i.e., output signal QR_S_ACT has the value TRUE.

If switch CONT_ON is set, the held ramp/soak function continues processing the ramp/soak profile at preassigned point TM_CONT.

###### Continue ramp/soak

With CONT_ON, a held ramp/soak profile is restarted at a defined point. If the ramp/soak function is not held, CONT_ON has no effect.

If the control input for continuing (CONT_ON = TRUE) is set, the held ramp/soak function is continued at time slice TM_SNBR. TM_CONT determines the remaining time that the ramp/soak function requires to reach time slice TM_SNBR.

The following figure shows the effect of RMP_HOLD and CONT_ON when the configuration is as follows:

Continue at time slice 5 (TM_SNBR = 5) and continue in T* s: TM_CONT = T*

![Continue ramp/soak](images/32395969163_DV_resource.Stream@PNG-en-US.png)

Time slices 3 and 4 are omitted in this processing cycle of the ramp/soak function. On a signal change of RMP_HOLD from TRUE to FALSE, the configured curve progression is only reached again starting from time slice 5.

Output QR_S_ACT is only set when the ramp/soak function executes the ramp/soak profile assigned by the user.

###### Updating the total time and remaining total time

The current time slice number NBR_ATMS, the current remaining time until the time slice is reached (RS_TM), the total time T_TM, and the total remaining time until the end of the ramp/soak profile (RT_TM) are updated in every cycle.

In the case of online changes of PI[n].TMV, the total time and the total remaining time of the ramp/soak profile change. Since the calculation of T_TM and RT_TM with many time slices significantly increases the processing time of the function block, the calculation is only carried after a restart or when TUPDT_ON = TRUE. The time intervals PI[0 ... NBR_PTS].TMV between the individual time slices are added up and indicated at the total time T_TM and total remaining time RT_TM outputs.

Please note that determining the total times requires significant CPU runtime.

###### Procedure

To configure the ramp/soak function, proceed as follows:

1. Select "Ramp/soak" from the "Setpoint source" drop-down list.
2. Create a [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400) (PID-CP) or [Global data block DB_RMPSK](Standard%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_rmpsk-s7-300-s7-400-1) (PID-ES).
3. Define the required parameters for the ramp/soak.
4. Enter the number of the data block DB_RMPSK in the "DB number" input field.
5. Enable or disable the additional functions of the ramp/soak.
6. If you have enabled the Continue ramp/soak function, enter at which time slice and when the ramp/sock is to be continued.

##### Scaling (S7-300, S7-400)

###### Scaling of an external setpoint

If the external setpoint is not expressed in the physical unit of the process value (e.g., expressed as a percent in the case of cascade control), then this value and its setting range must be scaled to the physical unit of the process value. The "Scaling in setpoint branch" function is used for this.

The SP_NORM function scales an analog input variable. The analog external setpoint is transformed to output variable outv using the scaling level. Output value OUTV is accessible in the configuration tool via measuring point MP2.

The output value of the function has an effect when control input SPEXT_ON = TRUE. In order to uniquely specify the scaling levels, you define the following four parameters:

- High input: SP_EXT: NM_SPEHR
- Low input: SP_EXT: NM_SPELR
- High output: NM_PVHR (You specify this value in the scaling function of the process value.)
- Low output: NM_PVLR (You specify this value in the scaling function of the process value.)

  ![Scaling of an external setpoint](images/34001570315_DV_resource.Stream@PNG-de-DE.png)

Output value outv is calculated from the respective input value SP_EXT according to the following formula:

outv = (SP_EXT – NM_SPELR) x (NM_PVHR – NM_PVLR) / (NM_SPEHR – NM_SPELR) + NM_PVLR

For the special case in which a square root function is activated in the process value branch, the scaling values of the square root function (SQRT_HR and SQRT_LR) apply as the high and low limits of output value outv.

In this case, output value outv of the scaling function is calculated from the respective input value SP_EXT according to the following formula:

outv = (SP_EXT – NM_SPELR) x (SQRT_HR – SQRT_LR) / (NM_SPEHR – NM_SPELR) + SQRT_LR

There is no internal value limiting in the function. The parameters are not checked. If you enter the same value for NM_SPEHR and NM_SPELR, a division by zero is possible based on the formulas above. The instruction will not detect this.

###### Combination/ratio factor

With ratio control, the setpoints of the control loop are coordinated with one another in such a way that the set ratio matches the actual ratio of the process values.

With blending control, the desired quantities of the individual components are set. The total of the blending factors FAC must be 1.

###### Procedure

To configure the scaling, proceed as follows:

1. Enter the values for the scaling in the input fields "High input" and "Low input".
2. Enter a blending/ratio factor (FAC).

##### Limiting functions (S7-300, S7-400)

###### FC call in the setpoint branch

Insertion of a user-specific function in the setpoint branch allows an externally specified reference variable to undergo signal processing (e.g., signal delay or linearization) prior to application in the controller.

If you activate the FC call in the setpoint branch, a user-specific function is called. The controller calls the FC. In so doing, existing input/output parameters of the user FC are not initialized. Therefore, you must use S7-STL to program the data transfer in the user FC. You can monitor the prepared setpoint at MP3.

The value of SPFC_ON then determines whether a user-programmed function in the form of a standard FC (e.g., a characteristic curve) will be inserted at this point in the setpoint channel or whether the setpoint will continue to be processed without any influence of this type.

> **Note**
>
> The statement does not check to determine if a function exists. If the function does not exist, the CPU switches to STOP with an internal system error.

###### Procedure

To call a function in the setpoint branch, proceed as follows:

1. Select the "Enable FC call" check box.
2. In the "FC" input field, enter the number of the function to be called.

###### Limiting of the rate of change of the setpoint

Ramp functions are used in the setpoint branch in situations where the process does not tolerate abrupt changes in the actuating signal, since an abrupt setpoint change generally also causes an abrupt change in the manipulated variable of the controller. These abrupt manipulated variable changes must be avoided, for example, when a gearbox is connected in between an adjustable-speed motor and the load to be driven and an excessively rapid increase of the motor speed would result in overloading of the gearbox.

The SP_ROC function limits the rate of change of the setpoints processed in the controller. This is carried out separately for the rising slope and falling slope and separately for the positive and negative range of the reference variable.

The limiting for each slope of the ramp function in the positive range and in the negative range of the reference variable is entered in the four inputs SPURLM_P, SPDRLM_P, SPURLM_N, and SPDRLM_N. The slopes refer to a rising or falling slope per second. Faster setpoint changes are ramped down to these maximum rates.

For example, if SPURLM_P is assigned the value 10.0 [engineering value range/s], the following values are added to the "old value" of outv in each sampling cycle for as long as inv &gt; outv:

|  |  |  |
| --- | --- | --- |
| Sampling time | 1 s | outv<sub>old</sub> + 10 |
|  | 100 ms | outv<sub>old</sub> + 1 |
|  | 10 ms | outv<sub>old</sub> + 0.1 |

The following figure shows an example of how the signal processing functions. The step functions at input inv(t) become ramp functions at output outv(t).

![Limiting of the rate of change of the reference variable SP(t)](images/34001581835_DV_resource.Stream@PNG-en-US.png)

Limiting of the rate of change of the reference variable SP(t)

When slope limits are reached, this is not signaled.

###### Procedure

To limit the rate of change, proceed as follows:

1. Activate the "Limit rate of change" check box.
2. Specify the following values for the positive range as well as for the negative range:

   - Rising slope for setpoint value
   - Falling slope for setpoint value

###### Limiting of the absolute value of the reference variable

The setting range of the reference variable determines the range in which the controlled variable can fluctuate, i.e., the range in which the process varies within the scope of permissible status values.

To avoid a critical or impermissible process status, the setting range of the reference variable is subject to high and low limits (SP_LIMIT) in the setpoint branch of standard PID control.

The SP_LIMIT function limits the setpoint SP at the assignable low and high values (SP_LLM and SP_HLM) as long as input variable INV is outside these limits. Because the function cannot be deactivated, the specification of a low limit and high limit must be taken into consideration in the configuration.

The numeric values of the limits are set in the input parameters for the low and high limits. In the event of violations by input variable inv(t), the associated displays are output via the message outputs.

![Absolute value limiting of reference variable SP(t)](images/34001678219_DV_resource.Stream@PNG-en-US.png)

Absolute value limiting of reference variable SP(t)

During a restart, the message bits are reset.

The message bits are set as follows:

| SP =PVH_ALM | QSP_HLM | QSP_LLM | If: |
| --- | --- | --- | --- |
| SP_HLM | TRUE | FALSE | inv ≥ SP_HLM |
| SP_LLM | FALSE | TRUE | inv ≤ SP_LLM |
| inv | FALSE | FALSE | SP_HLM &lt; inv &lt; SP_LLM |

###### Procedure

To limit the absolute value of the reference variable, proceed as follows:

1. Enter the high limit for the absolute setpoint (SP_HLM) in the "High limit" input field.
2. Enter the low limit for the absolute setpoint (SP_LLM) in the "Low limit" input field.

#### Control deviation (S7-300, S7-400)

This section contains information on the following topics:

- [Deadband (S7-300, S7-400)](#deadband-s7-300-s7-400-1)
- [Alarm (S7-300, S7-400)](#alarm-s7-300-s7-400-3)

##### Deadband (S7-300, S7-400)

In an optimally tuned controller, when a high-frequency interfering signal is superimposed on the control variable or reference variable, the noise portion will also have an effect on the controller output. This can result in strong fluctuations of the manipulated variable, for example, if the controller gain is high and derivative action is enabled. Due to the increased switching frequency (step controller), this causes increased wear of the actuator.

The function reduces the noise portion in the control deviation signal while the controller is in steady-state and thus reduces undesired oscillating of the controller output.

The deadband can be disabled.

###### Signal filtering through deadband function

The DEADBAND function suppresses small fluctuations of the input variable around a specified zero point within an adjustable range. Outside this fluctuation range, the control deviation ER rises or falls proportional to the input variable. The width of the deadband can be specified with the DEADB_W parameter. Only positive values are permitted for the deadband width.

If the input variable is within the deadband, the value 0 (control deviation = 0) is output at the output. Only when the input variable exits the deadband will the output rise or fall by the same values as input variable inv. This results in corruption of the transmitted signal outside the deadband, too. However, this is accepted in order to avoid step changes at the deadband limits (see figure below). The corruption corresponds to the value DEADB_W and can therefore be controlled easily.

The DEADBAND function operates according to the following functions:

(ER) = inv + DEADB_W for inv &lt; - DEADB_W

(ER) = 0 for -DEADB_W ≤ inv ≤ + DEADB_W

(ER) = inv - DEADB_W for inv &gt; + DEADB_W

![Signal filtering through deadband function](images/34001804299_DV_resource.Stream@PNG-en-US.png)

Effects of the signal filtering can be monitored at the output parameter ER.

##### Alarm (S7-300, S7-400)

Excessive deviations of the controlled variable from the specified setpoint can cause an undesired process status. In such cases, the ER_ALARM function is used to monitor the control deviation for violation of the permissible operating range. ER_ALARM detects and signals any limit violations that occur so that an appropriate reaction can be initiated.

> **Note**
>
> The monitoring of the control deviation for limit values cannot be disabled. The violation of the configured limits is always signaled.

The ER_ALARM function monitors the size of control deviation ER(t) for four assignable limits in two tolerance bands. If the limits are reached or exceeded, the function signals a “warning” at the first limit and an “alarm” at the second limit.

###### Limit values

The numeric values of the limits are set in the input parameters for “warning” and “alarm”. If the control deviation (ER) violates these limits, the associated output message bits QERN_ALM ... QERP_ALM are set.

During a restart, the message bits are reset.

The message bits are set as follows:

| QERP_ALM | QERP_WRN | QERN_WRN | QERN_ALM | If: | And: |
| --- | --- | --- | --- | --- | --- |
| TRUE | TRUE | FALSE | FALSE | ER ↗  ER ↘ | ER ≥ ERP_ALM  ER ≥ ERP_ALM **-** ER_HYS |
| FALSE | TRUE | FALSE | FALSE | ER ↗  ER ↘ | ER ≥ ERP_WRN  ER ≥ ERP_WRN **-** ER_HYS |
| FALSE | FALSE | TRUE | FALSE | ER ↘  ER ↗ | ER ≤ ERP_WRN  ER ≤ ERP_WRN **+** ER_HYS |
| FALSE | FALSE | TRUE | TRUE | ER ↘  ER ↗ | ER ≤ ERP_ALM  ER ≤ ERP_ALM **+** ER_HYS |

The following has to apply so that the block operates properly:

High alarm &lt; High warning &lt; Low warning &lt; Low alarm

![Limit values](images/37711954955_DV_resource.Stream@PNG-en-US.png)

###### Hysteresis

In order to avoid "flickering" of the message bits when the input variable undergoes slight changes or in the event of rounding errors, a hysteresis ER_HYS is used. The control deviation must violate the hysteresis before the message bits are reset.

### Controller (S7-300, S7-400)

This section contains information on the following topics:

- [Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400-1)
- [Controller structures (S7-300, S7-400)](#controller-structures-s7-300-s7-400-1)
- [Proportional component (S7-300, S7-400)](#proportional-component-s7-300-s7-400-1)
- [Integral action (S7-300, S7-400)](#integral-action-s7-300-s7-400-1)
- [Derivative component (S7-300, S7-400)](#derivative-component-s7-300-s7-400-1)

#### Control algorithm (S7-300, S7-400)

The manipulated variable of the continuous controller is calculated within the configured sampling time cycle on the basis of the control deviation in the PID position algorithm. The controller is implemented in a purely parallel structure. The proportional, integral, and derivative actions can each be disabled individually.

![Figure](images/35654713995_DV_resource.Stream@PNG-de-DE.png)

##### Feedforward control

A disturbance variable DISV can be added in the output signal of the controller (PID_OUTV). The variable is switched-in or switched-off in the PID window of the configuration tool using the DISV_SEL structure selector or through "Disturbance variable on".

##### Proportional and derivative action in the feedback path

In the parallel structure, each action in the control algorithm receives the control deviation as input signal. Via the proportional action and derivative action, the manipulated variable is influenced directly by setpoint steps. However, a different controller structure in which the formation of the proportional and the derivative actions is moved to the feedback path ensures a smooth response of the manipulated variable to setpoint step changes. In this structure, the integral action processes the control deviation as the input signal. Only the negative controlled variable (factor = - -1) is applied to the proportional action and the derivative action.

![Proportional and derivative action in the feedback path](images/32396718347_DV_resource.Stream@PNG-de-DE.png)

##### Scaling the input variable ER and PV

The input variables ER and PV of the PID controller are scaled to the range 0 to 100 prior to the controller processing according to the following formulas:

- with square-root function disabled (SQRT_ON = FALSE):

  - ER<sub>scaled</sub> = ER * 100.0 / (NM_PVHR – NM_PVLR)
  - PV<sub>scaled</sub> = (PV - NM_PVLR) * 100.0 / (NM_PVHR – NM_PVLR)
- with square-root function enabled (SQRT_ON = TRUE):

  - ER<sub>scaled</sub> = ER * 100.0 / (SQRT_HR – SQRT_LR)
  - PV<sub>scaled</sub> = (PV - SQRT_LR) * 100.0 / (SQRT_HR – SQRT_LR)

This scaling is performed so that the proportional gain GAIN of the PID controller can be entered without dimensions. If the high limit and low limit of the physical measuring range change (for example, from bar to mbar), the gain factor does not then have to be changed.

The scaled input variables ER<sub>scaled</sub> and PV<sub>scaled</sub> cannot be monitored.

---

**See also**

[Controller structures (S7-300, S7-400)](#controller-structures-s7-300-s7-400-1)
  
[Proportional component (S7-300, S7-400)](#proportional-component-s7-300-s7-400-1)
  
[Derivative component (S7-300, S7-400)](#derivative-component-s7-300-s7-400-1)
  
[Integral action (S7-300, S7-400)](#integral-action-s7-300-s7-400-1)

#### Controller structures (S7-300, S7-400)

##### Use and parameter assignment of the PID controller

The majority of the controlled systems occurring in the process industry can be controlled with the PI controller function/PID controller function of standard PID control. Only in special cases are additional methods and measures needed for a particular closed-loop control.

However, a major problem in the field continues to be how to assign the PI controller/PID controller parameters, i.e., how to determine the "correct" settings for the controller parameters. The quality of this parameter assignment is critical in order for the PID control to meet the requirements of the task at hand. It requires either a lot of practical experience, special expertise, or a great amount of time.

##### P control

The integral and derivative actions are disabled in a proportional-action controller (P-controller). (I_SEL and D_SEL = FALSE). This means that when control deviation ER = 0, output signal OUTV = 0. If an operating point ≠ 0 is intended, i.e., a numeric value will be set for the output signal when the control deviation is zero, the integral branch must be activated (see the following figure).

In the integral action, an operating point ≠ 0 can be specified for the P-controller via a corresponding setting of initialization value I_ITLVAL. Set switches 'I_ITL_ON' and 'I_SEL' = TRUE for this purpose.

![P control](images/35653882507_DV_resource.Stream@PNG-de-DE.png)

The step response of the P-controller within the time range is:  
PID_OUTV (t) = I_ITLVAL + GAIN * ER <sub>scaled </sub>(t)

![P control](images/33472499339_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| I_ITLVAL | Operating point of the P-controller |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(t) | Scaled control deviation |

##### PI control

The derivative action is disabled in the proportional-integraI controller (PI controller). (D_SEL = FALSE). A PI controller adjusts output variable PID_OUTV using the integral action until control deviation ER = 0. However, this only applies if the output variable does not exceed the limits of the control range.

The step response within the time range is:

![PI control](images/34003232779_DV_resource.Stream@PNG-en-US.png)

![PI control](images/33520548875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(0) | Step height of the scaled control deviation |
| TI | Integral-action time constant |

##### PD control

The integral action is disabled in the proportional-derivative controller (PD-controller) (I–SEL = FALSE). This means that when control deviation ER = 0, output signal OUTV = 0. If an operating point ≠ 0 is intended, i.e., a numeric value will be set for the output signal when the control deviation is zero, the integral action branch must be activated (see also the block diagram of the P control).

In the integral action, an operating point ≠ 0 can be specified for the PD-controller via a corresponding setting of initialization value I_ITLVAL. The switches 'I_ITL_ON' and 'I_SEL' must be set to TRUE for this purpose.

The PD-controller maps input variable ER(t) proportionally to the output signal and adds to this the derivative action generated by differentiation of ER(t); the derivative action is calculated with double precision according to the trapezoid rule (Padé approximation). The time response is determined by the derivative time constant TD.

For signal smoothing and suppression of interfering signals, a first-order delay (adjustable time: TM_LAG) is integrated into the algorithm for generating the derivative action. A small value for TM_LAG is usually sufficient to achieve the desired result. If TM_LAG ≤ CYCLE/2 is configured, the time delay is deactivated.

The step response within the time range is:

![PD control](images/33525271435_DV_resource.Stream@PNG-en-US.png)

![PD control](images/34003271947_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(0) | Step height of the scaled control deviation |
| TD | Derivative time |
| TM_LAG | Time delay |

##### PID control

In the proportional-integral-derivative controller (PID-controller), the proportional action, integral action, and derivative action are enabled (P–SEL = TRUE, I–SEL = TRUE, D_SEL = TRUE). A PID controller adjusts output variable PID_OUTV using the integral action until control deviation ER = 0. However, this only applies if the output variable does not exceed the limits of the control range. If manipulated variable limits are exceeded, the integral action maintains the value that was reached at the limit (anti-reset windup).

The PID-controller maps scaled input variable ER<sub>scaled</sub>(t) proportionally to the output signal and adds to this the components generated by differentiation and integration of ER<sub>scaled</sub>(t); these components are calculated with double precision according to the trapezoid rule (Padé approximation). The time response is determined by the derivative-action time TD and integral-action time TI.

For signal smoothing and suppression of interfering signals, a first-order delay (adjustable time constant: TM_LAG) is integrated into the algorithm for generating the derivative action. A small value for TM_LAG is usually sufficient to achieve the desired result. If TM_LAG ≤ CYCLE/2 is configured, the time delay is deactivated.

The step response within the time range is:

![PID control](images/33525435531_DV_resource.Stream@PNG-en-US.png)

![PID control](images/33525447179_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| PID_OUTV(t) | Manipulated variable when controller is in automatic mode |
| GAIN | Controller gain |
| ER <sub>scaled </sub>(0) | Step height of the scaled control deviation |
| TI | Integral-action time constant |
| TD | Derivative time |
| TM_LAG | Time delay |

> **Note**
>
> If TD is changed, you should also adjust TM_LAG accordingly.
>
> Recommendation: 5 ≤ (TM / TM_LAG) ≤ 10

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400-1)
  
[Proportional component (S7-300, S7-400)](#proportional-component-s7-300-s7-400-1)
  
[Derivative component (S7-300, S7-400)](#derivative-component-s7-300-s7-400-1)

#### Proportional component (S7-300, S7-400)

##### Proportional gain

The sign of this proportional gain determines the effective direction of the continuous controller.

- Positive proportional gain

  increasing control deviation → rising manipulated variable
- Negative proportional gain

  increasing control deviation → falling manipulated variable

##### Applying proportional action in feedback path

If the proportional action is applied to the feedback path, only the process value has an effect on the proportional action. Therefore, the manipulated variable does not undergo a step change due to the proportional action during a changeover from manual to automatic (also in the case of a setpoint step-change); the changeover is bumpless.

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400-1)

#### Integral action (S7-300, S7-400)

##### Function of the integral action

The integral action ensures that the control deviation can go to 0 for any manipulated variables by resetting the operating point.

The integral action generates an output signal whose rate of change is proportional to the change in the absolute value of the input variable. The time response is determined by the integral action time TI.

The response characteristic in the time range is:

![Function of the integral action](images/32396884491_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| LMN_I(t) | The output variable of the integral action |
| inv<sub>0</sub> | The step height at the input of the integral action |
| TI | Integral action time |

The integral action can be monitored at the static tag LMN_I.

| Parameter | Meaning | Permitted value range |
| --- | --- | --- |
| TI | Integral action time | ≥ 5 * CYCLE |
| I_ITLVAL | Initialization value for I action | -100.0 to +100.0 [%] |

![Function of the integral action](images/37537667595_DV_resource.Stream@PNG-de-DE.png)

*) Default for creation of new technology object

In the deactivated state (I_SEL = FALSE), the integral action, i.e., the internal memory and the static tag LMN_I, is set to zero.

The output and the memory of the integral action are limited by the absolute limits of the manipulated variables LMN_HLM and LMN_LLM (Anti Reset Wind–up).

If the actuating signal is influenced in manual mode, i.e., if MAN_ON, LMNOP_ON or CAS_ON = TRUE, the internal memory value of the integral action is corrected to the value LMN.

![Function of the integral action](images/35681165323_DV_resource.Stream@PNG-de-DE.png)

##### Changeover from manual to automatic mode

The integral action is set in manual mode in such a manner that the manual-to-automatic transition causes the manipulated variable to move from the current position. The height of the step change is determined by the proportional action. The step height of the proportional action corresponds to the manipulated variable change on a setpoint step change from the current process value to the current setpoint.

However, if the proportional action is applied to the feedback path, only the process value has an effect on the proportional action. Therefore, the manipulated variable does not undergo a step change due to the proportional action during a switchover from manual to automatic; the changeover is smooth.

##### Permissible ranges for the integral action time TI and CYCLE

The limited accuracy of the REAL numbers calculated in the CPU means that the following can occur during integration: If the selected sampling time CYCLE of the control is too short in comparison with the integral action time TI and the input value inv of the integral action is small compared to its output value OUTV, the integral action does not respond and remains at its current output value.

This effect can be avoided if the following sizing rule is observed during configuration:

CYCLE &gt; 10<sup>–4</sup> × TI

As a result, the integral action still responds to changes in the input values in the range of millionths of one part per thousand of the current output variable:

inv &gt; 10 <sup>–10 </sup>× OUTV

In order for the response characteristic of the integrator algorithm to conform to the analog response, the sampling time should be less than 20% of the specified integral action time or TI should be at least five times the value of the specified sampling time:

CYCLE &lt; 0.2 × TI

The algorithm permits sampling time values up to CYCLE ≤ 0.5 * TI.

##### Initializing the integral action

If initialization of the integral action is enabled, the initialization value is switched through to the static tag LMN_I at a restart of the CPU or COM_RST = TRUE. On the transition to normal operation, the integral action starts the integration of its input variable from the initialization value due to the resetting of the initialization.

##### Hold integral action

The integral action can be blocked in positive or negative direction by the static tags INT_HPOS and INT_HNEG. This can be useful for controller cascades. If, for example, the manipulated variable of the follow-up controller approaches the high limit, a further increase in the manipulated variable of the master controller can be prevented by its integral action. You program this response using the following instructions, for example, in STL:

A "Follow-up controller".QLMN_HLM

= "Master controller".INT_HPOS

A "Follow-up controller".QLMN_ LLM

= "Master controller".INT_HNEG

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400-1)

#### Derivative component (S7-300, S7-400)

##### Function of the derivative action

The derivative action generates an output signal whose size changes proportionally to the rate of change of the input variable. The time response is determined by the derivative time TD and the time delay TM_LAG.

The step response to the input step inv<sub>0</sub> is:

![Function of the derivative action](images/32396928267_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| LMN_D(t) | The output variable of the derivative action |
| inv<sub>0</sub> | The step height at the input of the derivative action |
| TD | Derivative-action time |
| TM_LAG | Time delay |

The derivative action can be monitored at the static tag LMN_D.

In the disabled state (D_SEL = FALSE), the derivative action, i.e., the internal memory and the static tag LMN_D, is set to zero.

##### Apply derivative action in feedback path

If the derivative action is applied to the feedback path, only the process value has an effect on the derivative action. Consequently – as in a setpoint jump – the manipulated variable does not undergo a step change due to the derivative action during a changeover from manual to automatic; the switchover is smooth.

##### Permitted values for derivative time and time delay.

To calculate the derivative action correctly, the following conditions must be satisfied for the derivative time and time delay:

- TD ≥ CYCLE and
- TM_LAG ≥ 0.5 × CYCLE

If TD &lt; CYCLE, the derivative action operates as though the TD has the value CYCLE.

If TM_LAG &lt; 0.5 × CYCLE, the derivative action operates without delay. An input step is then multiplied with the factor TD/CYCLE and this value is applied as "needle pulse" at the output. In other words, LMN_D is reset to zero in the subsequent processing cycle.

##### Coefficient DT1

The coefficient DT1 is calculated as follows:

Coefficient DT1 = TD/TM_LAG

##### Time delay

For signal smoothing and suppression of interfering signals, a first-order delay (adjustable time constant: TM_LAG) is integrated into the algorithm for generating the derivative action.

A small value for the time delay is usually sufficient to achieve the desired result. If the assigned time delay is less than half the controller sampling time, the delay is deactivated.

##### Procedure

To configure the derivative action, proceed as follows:

1. To apply the derivative action to the feedback path, select the corresponding check box.
2. Enter the derivative time in seconds.
3. Enter the time delay in seconds.

---

**See also**

[Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400-1)

### Manipulated variable (S7-300, S7-400)

This section contains information on the following topics:

- [Step controller with position feedback (S7-300, S7-400)](#step-controller-with-position-feedback-s7-300-s7-400)
- [Step controller without position feedback (S7-300, S7-400)](#step-controller-without-position-feedback-s7-300-s7-400)
- [Manual mode (S7-300, S7-400)](#manual-mode-s7-300-s7-400-1)
- [Limiting functions (S7-300, S7-400)](#limiting-functions-s7-300-s7-400-3)
- [Pulse generator (S7-300, S7-400)](#pulse-generator-s7-300-s7-400-1)

#### Step controller with position feedback (S7-300, S7-400)

##### Function chart of the step controller with position feedback in the control loop

The functional principles of the step controller with position feedback are based on the PID control algorithm and are supplemented by the function elements for generating the binary output signal from the analog actuating signal of the controller.

Depending on the sign, the three-step element hereby converts deviations between manipulated variable and position feedback into positive or negative pulses of the output signal in order, for example, to apply these to a motor-operated valve drive. Basically, this amounts to a cascade control with a lower-level position control loop.

![Function chart of the step controller with position feedback in the control loop](images/32397448075_DV_resource.Stream@PNG-en-US.png)

##### Selecting position feedback

For applying the position feedback to the comparator in the manipulated variable branch of the step controller, inputs with appropriate signal processing are available, depending on the format of the value to be processed. LMNR_PER can be used to apply signals in the SIMATIC I/O format, and LMNR_IN can be used to apply signals in floating-point format.

The associated internal value in the percent range is stored at measuring point MP10.

![Selecting position feedback](images/33692459147_DV_resource.Stream@PNG-de-DE.png)

If the position feedback is provided by an analog input module, the numerical value of the position feedback at LMNR_PER must be converted to a floating-point value scaled to a percentage.

In this process, no check is carried out for positive/negative overflow, reaching of the overrange/underrange, or wire break.

The following table provides an overview of ranges and numerical values before and after processing.

| I/O value LMNR_PER | Output value as a % |
| --- | --- |
| 32767 | 118.515 |
| 27648 | 100.000 |
| 1 | 0.003617 |
| 0 | 0.000 |
| - 1 | - 0.003617 |
| - 27648 | - 100.000 |
| - 32768 | - 118.519 |

##### Procedure

> **Note**
>
> It is not permissible to enable or disable position feedback in online mode. In other words, LMNR_ON may not be changed online.

To activate the position feedback, proceed as follows:

1. Select the "Enable” check box in the "Select position feedback" area.
2. Choose the "Position feedback signal IO" option in order to apply signals in the SIMATIC I/O format.  
   Choose the "Position feedback" option in order to apply signals in floating-point format.

##### Scaling position feedback

If the position feedback is available as a physical variable (e.g. 240 to 800 mm or in the angle from 0° to 60°), the position feedback in floating-point format (%) must be scaled to the physical variable required for the further processing of the required internal floating-point value.

The following parameters must be defined for the unique specification of the scaling levels:

- The factor (for the slope): **LMNR_FAC**
- The offset of the scaling level at the zero point: LMNR_OFF

  ![Scaling position feedback](images/32397639819_DV_resource.Stream@PNG-de-DE.png)

The scaled position feedback is calculated according to the following formula from inv (LMNR_PER) and output at MP10:

MP10 = inv * LMNR_FAC + LMNR_OFF

The scaling is effective if the I/O position feedback is enabled (LMNRP_ON = TRUE). No values are limited internally in the function. There is no parameter check.

##### Procedure

To scale the signal of the position feedback, proceed as follows:

1. Enter the slope of the scaling level in the "Factor" input field.
2. Enter the offset of the scaling level with respect to the zero point in the "Offset" input field.

#### Step controller without position feedback (S7-300, S7-400)

##### Structure and function of the step controller

The step controller without position feedback consists of two parts: The PD controller part, which operates with continuous signals, and a second part in which the binary actuating signals are generated from the difference between the PD action and the feedback.

The integral action of the step controller without position feedback is calculated in the feedback path. The feedback signal compared with the controller output of the PD controller is generated in this process by integrating the following two signal components:

- Signal component for simulated position feedback

  ± 100/MTR_TM
- Signal component for the integral action

  ER<sub>scaled</sub>*GAIN/TI

The feedback signal is thus the difference between simulated position feedback and integral action.

Depending on the sign, the three-step element converts deviations between manipulated variable and feedback signal into positive or negative pulses of the output in order, for example, to apply these to a motor-operated valve drive.

In steady state, the output of the integral action and the PD action go to zero. Because the input of the three-step element also goes to zero, the binary actuating signals QLMNUP and QLMNDN remain at FALSE.

Because the integration take place in the feedback path, the integral action is not calculated in the PID algorithm. However, the integral action in the PID algorithm can be set to a fixed value with I_ITL_ON and I_ITLVAL.

With step controller without position feedback, the freezing of the integral action with INT_HPOS and INT_HNEG is not supported.

In this case, there is no manual mode option using the MAN parameter because of the lack of information regarding the actuator position.

![Structure and function of the step controller](images/32397795979_DV_resource.Stream@PNG-en-US.png)

Addressing the endstop signals of the actuator (LMNR_HS/LMNR_LS) causes the manipulated variable LMNUP or LMNDN to be blocked.

If the actuator returns no endstop signals, the input parameters LMNR_HS and LMNR_LS = FALSE must be set.

> **Note**
>
> If end stop signals are not available, the controller cannot detect whether a mechanical end stop has been reached. For example, it is possible that the controller will output signals for opening the valve even though the valve is already at its upper end stop.

##### Manual mode

The step controller without position feedback has no manual mode via the parameter MAN or the manual output variable generator MAN_GEN because there is no information on the position of the actuator. Manual mode is only possibly by direct switching of the actuating signal (LMNS_ON = TRUE).

##### Simulation of position feedback

If a measurable value for the position feedback is not available, it can also be simulated (LMNRS_ON = TRUE).

The position feedback is simulated by an integrator with motor transition time MTR_TM as the integration time constant. When LMNRS_ON = FALSE, the start value of the LMNRSVAL parameter is output at the output of the LMNR_ SIM integrator. On switchover to LMNRS_ON = TRUE, the simulation starts up with this start value.

If LMNR_HS = TRUE, the integration is held up, and if LMNR_LS = TRUE, it is held down. The simulated position feedback is not adapted to the end positions.

![Simulation of position feedback](images/32397880203_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The position feedback is merely simulated. It does not have to match the actual position of the actuator. If a real position feedback is available, it should always be used.

#### Manual mode (S7-300, S7-400)

##### Manual mode

The structure of the manual value generation and manual value selection is shown in the next figure.

![Manual mode](images/32397530507_DV_resource.Stream@PNG-en-US.png)

With step controllers, there are three operating modes in which the manipulated variable can be influenced:

- Manual value via the input parameter MAN

  The MAN parameter (-100.0% to 100.0%) allows you to activate influencing by an external manipulated variable in the form of an absolute value or to specify it in the user program.

  This is possible only when position feedback is enabled.
- Manual mode via more/less switch of the manual value generator (MANUP, MANDN).

  If MAN_GEN is activated from another operating mode, the manipulated variable MP9 is applied. The changeover to the manual value generator is thus always bumpless. The manual output variable can be increased or decreased within the LMN_HLM and LMN_LLM limits.

  This is possible only when position feedback is enabled.
- Manual mode by means of direct connection of the actuating signals

  Manual mode by direct connection of the actuating signals LMNUP and LMNDN always has priority.

  When LMNS_ON = FALSE is reset, the switch to any other activated operating mode will be "bumpless".

##### Automatic mode

If manual mode is disabled (MAN_ON = FALSE), the manipulated variable of the PID algorithm is connected to the three-step element. The changeover from manual mode to automatic mode causes a step change in the manipulated variable LMN. However, this is not a disadvantage because the integrating actuator means that the process is controlled according to a ramp function. The output of the PID algorithm is stored in measuring point MP7.

##### Manual value follow-up in automatic mode

If the I/O position feedback is enabled (LMNRP_ON = TRUE), the input parameter MAN of the position of the actuator (MP10) is corrected.

If position feedback is enabled (LMNRP_ON = FALSE), the input parameter MAN of the position of the actuator (LMNR_IN) is corrected.

Therefore, on switchover to manual mode, the manipulated variable remains at the value that corresponds to the actuator position. It can now be changed by operator input.

##### Activate manual mode with manual value

In this mode (MANGN_ON = FALSE and MAN_ON = TRUE), the manual output value is entered as an absolute value in the MAN input. The manual output value is displayed at measuring point MP8.

1. Select the "Activate manual mode" check box.
2. Choose the "Manual value" option.

##### Activate the manual value generator

The manual value MAN can be incremented or decremented in steps using the MANUP and MANDN switches. The modified value can be monitored at MP8. The configured manipulated variable limits are taken into account.

1. Select the "Activate manual mode" check box.
2. Select the "Manual value generator" option.

##### Effect of the switches MANUP and MANDN

For changes involving small steps, the controller should have a maximum sampling time of 100 ms.

The rate of change of the manipulated variable depends on how long the MANUP or MANDN switch is actuated and on the selected limits. The following relationship applies:

- During the first 3 s after setting MANUP or MANDN:

  doutv/dt = (LMN_HLM - LMN_LLM) / 100 s
- Afterwards:

  doutv/dt = (LMN_HLM - LMN_LLM) / 10 s

  ![Effect of the switches MANUP and MANDN](images/32397029003_DV_resource.Stream@PNG-de-DE.png)

For a sampling time of 100 ms and a manipulated variable range of -100.0 to 100.0, the manipulated variable, for example, changes by 0.2 per cycle during the first 3 seconds. If MANUP is TRUE for more than 3 seconds, the rate of changes increases to ten times the value, in this case therefore to 2 per cycle.

The manual value generator is activated bumpless.

##### Switching the operating modes

The following table shows the possible operating modes of the step controller with the required values of the structure-defining switches.

Operating modes of step controller

|  | MAN_ON | MNGN_ON | LMNS_ON |
| --- | --- | --- | --- |
| Automatic mode | FALSE | Any | FALSE |
| Manual mode without switch operation | TRUE | FALSE | FALSE |
| Manual mode with manual value generator | TRUE | TRUE | FALSE |
| Manual mode using actuating signals | Any | Any | TRUE |

#### Limiting functions (S7-300, S7-400)

With step controllers with position feedback, you can limit the manipulated variable.

##### Limiting the absolute value of the manipulated variable

The operating range, i.e., the range in which the actuator can vary within the scope of permissible manipulated variables, is determined by the setting range of the manipulated variable. Since the limits for allowed manipulated variables usually do not coincide with the 0% or 100% limit of the correcting range, depending on the type of actuator, you can configure the high and low limit of the manipulated variable.

To avoid an impermissible status in the particular process, high and low limits for the setting range of the manipulated variable will be set in the manipulated variable branch of the closed-loop control.

The LMNLIMIT function limits manipulated variable LMN(t) to the low and high values LMN_HLM and LMN_LLM. These values can be specified. However, input variable inv must be outside these limits. Because the function cannot be deactivated, the specification of a low limit and high limit must always be taken into consideration in the configuration.

The numeric values of the limits (in percent) are set in the input parameters for the low and high limits. In the event of violations by input variable inv(t), the associated displays are output via the message outputs.

![Limiting the absolute value of the manipulated variable](images/33692755723_DV_resource.Stream@PNG-en-US.png)

##### Startup and operating principles

- During a restart, all message outputs are set to zero.
- The limiting operates according to the following relationships:

| LMN = | QLMN_HLM | QLMN_LLM | If: |
| --- | --- | --- | --- |
| LMN_HLM | TRUE | FALSE | inv ≥ LMN_HLM |
| LMN_LLM | FALSE | TRUE | inv ≤ LMN_LLM |
| inv | FALSE | FALSE | LMN_HLM &lt; inv &lt; LMN_LLM |

The effective manipulated value of the controller is displayed at the output, i.e. at the parameter LMN or at the measuring point MP10.

##### Procedure

To limit the absolute value of the manipulated variable, proceed as follows:

1. In the "High limit" input field, enter the value for the maximum permissible value.
2. In the "Low limit" input field, enter the value for the minimum permissible value.

#### Pulse generator (S7-300, S7-400)

The pulse generator ensures that a minimum on and off time is adhered to in order to protect the actuators. Addressing the endstop signals of the actuator (LMNR_HS/LMNR_LS) causes the manipulated variable LMNUP or LMNDN to be blocked. This applies to automatic and manual mode.

If both signal switches are set for manipulated variable signal input (LMNUP = LMNDN = TRUE and LMNUP_OP = LMNDN_OP = TRUE), outputs QLMNUP and QLMNDN always return FALSE.

It is not possible to change directly from "Manipulated variable signal up" (QLMNUP = TRUE, QLMNDN = FALSE) to "Manipulated variable signal down" (QLMNUP = FALSE, QLMNDN = TRUE). The pulse generator inserts a cycle with QLMNUP = QLMNDN = FALSE.

##### Input signal INV with step controllers with position feedback

The difference between manipulated variable LMN and position feedback LMNR is switched-through to the three-step element with hysteresis THREE_ST.

![Input signal INV with step controllers with position feedback](images/32397687051_DV_resource.Stream@PNG-en-US.png)

##### Input signal INV with step controllers without position feedback

The difference between the PD action of the controller and the feedback value (MP11) is switched to the three-step element with hysteresis THREE_ST.

![Input signal INV with step controllers without position feedback](images/33691806603_DV_resource.Stream@PNG-en-US.png)

##### Influence of motor transition time on the three-step element

The three-step element generates two binary signals which are TRUE or FALSE depending on the value and sign of the differential value at the input.

The three-step element THREE_ST responds to the input signal INV according to the following relationships and hereby adopts in each case one of the three possible combinations of its output signals UP/DOWN:

| UP | DOWN | Input combination |
| --- | --- | --- |
| TRUE | FALSE | |INV| ≥ ThrOn or INV &gt; ThrOff and UP<sub>old</sub> = TRUE |
| FALSE | TRUE | |INV| ≤ -ThrOn or INV &lt; -ThrOff and DOWN<sub>old</sub> = TRUE |
| FALSE | FALSE | |INV| ≤ ThrOff |
| ThrOn = Switch-on threshold, ThrOff = Switch-off threshold |  |  |

![Influence of motor transition time on the three-step element](images/32397698955_DV_resource.Stream@PNG-de-DE.png)

The switch-off threshold ThrOff must be greater than the change in the position feedback or the position change after one pulse duration. This value is dependent on the transition time of the motor MTR_TM and is calculated as follows:

![Influence of motor transition time on the three-step element](images/52435455499_DV_resource.Stream@PNG-en-US.png)

MTR_TM must be an integer multiple of CYCLE.

> **Note**
>
> An excessively long motor transition time setting (10% over the actual transition time) will cause the manipulated variable signals QLMNUP and QLMNDN to constantly switch on and off.

##### Adaptation of the switch-on threshold ThrOn

To reduce the switching frequency when larger control deviations are corrected, the switch-on threshold ThrOn is adapted automatically during operation, while ThrOff remains constant. ThrOn is limited to:

![Adaptation of the switch-on threshold ThrOn](images/32397868299_DV_resource.Stream@PNG-de-DE.png)

The adaptation of the switch-on threshold is disabled in pure P, D, and PD controllers. For example:

ThrOn = Min ThrOn

##### Minimum ON time and minimum OFF time.

The pulse generator ensures that a minimum on and off time is adhered to when the output pulses are switched on and off.

Parameters for a minimum ON time PULSE_TM and a minimum OFF time BREAK_TM can therefore be assigned to protect the actuator. The duration of the output pulse QLMNUP or QLMNDN is always greater than the minimum ON time and the break between two pulses always greater than the minimum OFF time. Using the UP signal as an example, the following figure shows how this works.

![Minimum ON time and minimum OFF time.](images/36055648267_DV_resource.Stream@PNG-de-DE.png)

##### Procedure

To configure the pulse generator, proceed as follows:

1. Enter the transition time of the motor in the "Motor transition time" input field.
2. Enter the "Minimum ON time".
3. Enter the "Minimum OFF time".

### Commissioning PID_ES (S7-300, S7-400)

This section contains information on the following topics:

- [Performing tuning manually (S7-300, S7-400)](#performing-tuning-manually-s7-300-s7-400-1)
- [Commissioning with the PID Self Tuner (S7-300, S7-400)](#commissioning-with-the-pid-self-tuner-s7-300-s7-400-1)

#### Performing tuning manually (S7-300, S7-400)

##### Requirements

- The instruction and the technology object have been loaded to the CPU.
- MAN_ON = FALSE

##### Procedure

In order to manually determine the optimal PID parameters, proceed as follows:

1. Click the "Measurement on" ![Procedure](images/23498796811_DV_resource.Stream@PNG-de-DE.png) icon.

   An online connection will be established, if one is not already present. The current values for the setpoint, process value and manipulated variable are recorded.
2. Enter new PID parameters in the "P", "I", "D" and "Time delay" fields.
3. Click on the icon ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png)"Send parameter to CPU" in the "Tuning" group.
4. Select the "Change setpoint" check box in the "Current values" group.
5. Enter a new setpoint and click in the "Current Values" group on the icon ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png).

   If the setpoint's rate of change is limited, the changeover to the new setpoint will be bumpless
6. Clear the "Manual mode" check box, if necessary.

   The controller works with the new PID parameters and controls the new setpoint.
7. Check the quality of the PID parameter based on the curve points.
8. Repeat steps 3 to 8 until you are satisfied with the controller results.

#### Commissioning with the PID Self Tuner (S7-300, S7-400)

You can commission the PID_ES instruction and determine the optimum PID parameters with the PID Self Tuner.

##### Procedure

To commission a step controller, proceed as follows:

1. Call the instruction PID_ES in a cyclic interrupt OB and interconnect the input and output parameters.
2. Call the instruction TUN_ES in the same cyclic interrupt OB.
3. Interconnect the instruction TUN_ES as follows with PID_ES:

   - TUN_ES.PV with PID_ES.PV
   - If you are using a position feedback, TUN_ES.LMNR with PID_ES.LMNR_IN
   - TUN_ES.C_LMNUP and TUN_ES.C_LMNDN with PID_ES.QLMN_UP and PID_ES.QLMNDN
   - TUN_ES.LMNR_HS with PID_ES.LMNR_HS
   - TUN_ES.LMNR_ON with PID_ES.LMNR_ON
   - TUN_ES.LMNS_ON with PID_ES.LMNS_ON
   - TUN_ES.SP_OUT with PID_ES.SP_IN or PID_ES.SP_EXT
   - TUN_ES.GAIN with PID_ES.GAIN
   - TUN_ES.TI with PID_ES.TI
   - TUN_ES.TD with PID_ES.TD
   - TUN_ES.TM_LAG with PID_ES.TM_LAG
   - TUN_ES.MTR_TM with PID_ES.MTR_TM
   - If you are using a deadband, TUN_ES.DEADB_W with PID_ES.DEADB_W
   - TUN_ES.QLMNUP and TUN_ES.QLMNDN with PID_ES.LMNUP and PID_ES.LMNDN
4. Click the "![Procedure](images/35383750539_DV_resource.Stream@PNG-de-DE.png)" icon on the instruction TUN_ES.

   The commissioning editor for TUN_ES opens. The operation of the commissioning editor is described with the PID Self Tuner.
