---
title: "Servo drives (highly dynamic)"
package: Stdr011000UIenUS
topics: 285
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Servo drives (highly dynamic)

This section contains information on the following topics:

- [Servo control features](#servo-control-features)
- [Parameterization](#parameterization)
- [Diagnostics](#diagnostics)
- [Rotate &amp; optimize](#rotate-optimize)

## Servo control features

With servo control, the connected motor is emulated in a vector model based on its equivalent circuit diagram data. This means that the servo control is also a vector control. However, the servo control optimizes the vector model according to other factors.

In favor of maximum dynamic response, small losses in the control accuracy and control quality are accepted. Characteristic properties of the servo control are:

- Maximum computing speed
- Very short sampling times
- Maximum dynamic response
- Preferably used with permanent magnet synchronous motors with the appropriate dynamic response

Since a model calculation of the actual values cannot be used with servo control because of the required computing speed, servo control can only be operated with encoders.

## Parameterization

This section contains information on the following topics:

- [Basic parameter assignment](#basic-parameter-assignment)
- [Setpoint channel](#setpoint-channel)
- [Open-loop/closed-loop control](#open-loopclosed-loop-control)
- [Drive functions](#drive-functions)
- [Safety Integrated](#safety-integrated)
- [Technology functions](#technology-functions)
- [Control logic](#control-logic)

### Basic parameter assignment

This section contains information on the following topics:

- [Function modules (servo)](#function-modules-servo)
- [Control type (servo)](#control-type-servo)
- [Limits (servo)](#limits-servo)
- [Reference parameters](#reference-parameters)
- [Sampling times / pulse frequency (servo)](#sampling-times-pulse-frequency-servo)
- [Actual value processing (servo)](#actual-value-processing-servo)
- [Rotor position synchronization (servo)](#rotor-position-synchronization-servo)
- [Mechanical system](#mechanical-system)
- [Enable logic (servo)"](#enable-logic-servo)
- [Data sets](#data-sets)

#### Function modules (servo)

You can connect various function modules for the drive axis used. The function modules that can be activated are listed in the "Function modules" screen form.

> **Note**
>
> The display of the function modules that can be activated is dynamic and depends on the selected drive axis and the configuration of this drive axis.

##### Requirement

- The drive axis is OFFLINE.

  The function modules can only be activated or deactivated offline.

##### Effect of the function modules

The usable function modules are presorted into two areas.

| Function module | Explanation |
| --- | --- |
| **Frequently used function modules** |  |
| [Extended setpoint channel](#setpoint-sources-and-setpoint-preparation-servo) (r0108.8) | Activates the "Setpoint channel" area with seven configuration screen forms. |
| [Extended messages/monitoring](#load-torque-monitoring-servo) (r0108.17) | The "Messages and monitoring" function is complemented in the "Drive function" area by the "Load torque monitoring" function. |
| [Technology controller](#technology-controller) (r0108.16) | Activates the "Technology controller" subarea with four configuration screen forms in the "Technology functions" area. |
| [Extended brake control](#extended-brake-control-servo) (r0108.14) | Extends the "Drive control" function in the "Drive functions" area. |
| [Basic positioner](#basic-positioner) (r0108.4) | Activates the "Basic positioner" and "Position control" functions in the "Technology functions" area. Complements the "Basic parameterization" area with the "Mechanical system" function. |
| **Other function modules** |  |
| Free function blocks ([r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1).18) | In the parameter view, activates the parameters for the F blocks ([p20030](SINAMICS%20Parameter%20CU.md#p2003003-bi-and-0-inputs) … [p20288](SINAMICS%20Parameter%20CU.md#p20288-dif-0-run-sequence)). The free function blocks can only be parameterized in the parameter view. |
| Recorder (r0108.5) | Enables recording of fault events |
| Moment of inertia estimator/OBT (r0108.10) | Activates parameter group [p0530](SINAMICS%20Parameter%20SERVO.md#p05300n-bearing-version-selection)x for configuring the autotuning functions for servo drives in the parameter view. |
| [Position control](#position-control) (r0108.3) | Activates the "Position controller" functions in the "Technology functions" area. Also complements the "Basic parameterization" area with the "Mechanical system" function. |
| [Extended torque control](#extended-torque-control-servo) (r0108.1) | Activates the "Extended torque control" function in the "Technology functions" area. |
| [DSC with spline](#dsc-with-splines-servo) (r0108.6) | Extends the interconnection of the "Speed precontrol" function in the "Open-loop/closed-loop control" area. Adds the "Dynamic Servo Control" secondary screen form. |
| [Advanced Position Control](#active-oscillation-damping-apc) (APC) (r0108.7)  &gt;&gt;Licensed&lt;&lt; | Activates the "Active oscillation damping (APC)" function in the "Technology functions" area. |
| [Extended stop and retract](#extended-stop-and-retract-esr) (r0108.9) | Activates the "Extended stop and retract" function in the "Setpoint channel" area. |
| [Extended current setpoint filter](#current-setpoint-filter-servo) (r0108.21) | Extends the "Current setpoint filter" function in the "Open-loop/closed-loop control" area by six further filters. |
| Detent torque compensation (r0108.22)  &gt;&gt;Licensed&lt;&lt; | Activates all parameters of the "Detent torque compensation" parameter group in the parameter view. The detent torque compensation can be parameterized only via the parameter view.    **Note:**   Activation of this function module results in a substantial increase in the required CPU time per drive axis.  Operation of six SERVO axes on one Control Unit cannot be guaranteed in all constellations and should be reduced to five axes. |

##### Activating a function module

1. Activate the required function module by clicking the option.

   Repeat this for all other function modules that you want to activate.
2. Save the project to save the settings.

##### Additional parameters

---

#### Control type (servo)

##### Control types

Speed control (with and without encoder) and torque control are available for SERVO drives.

- Speed control

  The speed control of a variable-speed drive has the task of following the speed according to a specified setpoint (reference variable) as precisely as possible and without overshoot.
- Torque control

  With torque control, the torque is the reference value and the actual torque value should follow the torque setpoint with as little ripple as possible and without delay.

The control modes can be set ONLINE as well as OFFLINE.

##### Requirements

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.

##### Selecting the control type

1. Select one of the following control types ([p1300](SINAMICS%20Parameter%20SERVO.md#p13000n-open-loopclosed-loop-control-operating-mode-1)) in the drop-down list:

   - Speed control with encoder
   - Speed control without encoder
   - Torque control with encoder

   If you have selected a control type with encoder, this encoder is now shown in the diagram.

##### Additional parameters

---

#### Limits (servo)

The limits can be defined ONLINE as well as OFFLINE.

##### Requirements

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.

##### Description

You define the basic properties of the drive control via the "Important parameters".

| Parameter | Name | Description |
| --- | --- | --- |
| [p1121](SINAMICS%20Parameter%20SERVO.md#p11210n-ramp-function-generator-ramp-down-time-2) | Ramp-down time | Ramp-down time which the drive requires to decelerate from maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)) to standstill. |
| [p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1) | OFF3 ramp-down time | The OFF3 ramp-down time sets the ramp-down time from maximum speed down to standstill for the OFF3 command. |

##### Additional parameters

---

#### Reference parameters

The "Reference parameters" screen form shows the most important reference parameters and their values in a table:

- [p2000](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2000-reference-frequency): Reference speed, reference frequency
- [p2001](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2001-reference-voltage): Reference voltage
- [p2002](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2002-reference-current): Reference currents
- [p2003](SINAMICS%20Parameter%20SERVO.md#p2003-reference-torque-1): Reference torque
- [r2004](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r2004-reference-power): Reference power
- [p2005](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2005-reference-angle): Reference angle
- [p2006](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2006-reference-temperature): Reference temperature
- [p2007](SINAMICS%20Parameter%20SERVO.md#p2007-reference-acceleration-1): Reference acceleration

##### Correct defaults

You can correct the defaults for all p parameters in the table:

1. Click in the "Values" field for the corresponding reference parameter.
2. Enter the desired new value.
3. Repeat steps 1 and 2 for the other reference parameters whose default settings you want to change.
4. Finally, save the project.

##### Additional parameters

---

#### Sampling times / pulse frequency (servo)

As of a pulse frequency of 800 Hz, it is recommended that you enter the sampling times and the pulse frequency for the drive.

##### Requirement

- The drive axis is OFFLINE.

  The entire basic parameter assignment can only be performed offline for the selected drive axis.

##### Setting the defaults

The sampling times are preset via parameter [p0112](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0112-sampling-times-pre-setting-p0115).

1. Select one of the following defaults via the drop-down list (p0112):

   - [0] Expert
   - [1] xLow
   - [2] Low
   - [3] Standard
   - [4] High
   - [5] xHigh

   The designation of the defaults refer to the desired output frequency and control dynamic response. If a particularly high output frequency or control dynamic response is required, "xHigh" would be the correct default. The selected default affects the following control loops:

   - [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)[0]: Current controller
   - p0115[1]: Speed controller
   - p0115[2]: Flux controller
   - p0115[3]: Setpoint channel
   - p0115[4]: Position controller
   - p0115[5]: Positioning
   - p0115[6]: Technology controller

   The display of the parameter values set for p0115 changes depending on the default setting made.

**Note**

If the sampling times of the current controller and speed controller are changed (see also p0115), it is recommended that the controller settings are recalculated via [p0340](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0340-automatic-calculation-control-parameters) = 4 after the commissioning ([p0010](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0010-infeed-commissioning-parameter-filter) = 0).

##### Entering the sampling times manually

If you have set "Expert" in p0112, you can manually configure each of the following sampling times for the following control loops (p0115):

- p0115[0]: Sampling times for internal control loops, current controller
- p0115[1]: Sampling times for internal control loops, speed controller
- p0115[2]: Sampling times for internal control loops, flux controller
- p0115[3]: Sampling times for internal control loops, setpoint channel
- p0115[4]: Sampling times for internal control loops, position controller
- p0115[5]: Sampling times for internal control loops, positioning
- p0115[6]: Sampling times for internal control loops, technology controller

> **Note**
>
> You cannot set the values arbitrarily. The rules when setting the sampling times are listed in item "[Sampling times and number of controllable drives](Configuring%20SINAMICS%20S-G-MV%20drives.md#sampling-times-and-number-of-controllable-drives)".

Enter the sampling times for the internal control loops.

##### Setting the pulse frequency

Set the pulse frequency for the drive via the parameter [p1800](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1800-pulse-frequency). The setting is possible independent of the default user role.

##### Additional parameters

- p1800

---

#### Actual value processing (servo)

The actual value processing can be carried out ONLINE as well as OFFLINE.

##### Requirements

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- An encoder has been configured.

##### Processing actual position values

The actual position values are provided standard in Gn_XIST1 ([r0482](SINAMICS%20Parameter%20SERVO.md#r048202-co-encoder-actual-position-value-gn_xist1)) and Gn_XIST2 ([r0483](SINAMICS%20Parameter%20SERVO.md#r048302-co-encoder-actual-position-value-gn_xist2)) (n = 1 or 2, number of the encoder) in accordance with the PROFIdrive.

- Gn_XIST1: Here, the incremental position change of the encoder is transferred to the controller. This value contains the fine resolution (subdivision of an encoder pulse) set in [p0418](SINAMICS%20Parameter%20SERVO.md#p04180n-fine-resolution-gx_xist1-in-bits).

  For one encoder revolution in the positive direction, Gn_XIST1 is consequently incremented by the value "Pulse number * 2<sup>p0418</sup>". See also parameter help for p0418.
- Gn_XIST2: Here, different positional information can be transmitted in accordance with the PROFIdrive standard. The required values must be requested via the encoder control word ([p0480](SINAMICS%20Parameter%20SERVO.md#p048002-ci-encoder-control-word-gn_stw-signal-source)). For example, this can be the absolute position for absolute value encoders and the zero mark position for incremental encoders with a zero mark. Like with the Gn_XIST1, the position values of the Gn_XIST2 also contain the set fine resolution of parameter [p0419](SINAMICS%20Parameter%20SERVO.md#p04190n-fine-resolution-absolute-value-gx_xist2-in-bits). See also parameter help for p0419.

##### Fine resolution p0418 (XIST_1)

Encoders provide, for example, sinusoidal signals that are multiplied by the encoder evaluation, e.g. 11 bits = 2048 values within one sine period (of an encoder pulse). They can be evaluated by the drive unit and transferred with the fine resolution (p0418) to the controller. You can change the fine resolution as part of the encoder accuracy and the encoder evaluation (see online help for p0418).

**Fine resolution for TTL/HTL encoders**

TTL/HTL pulse encoders operate with signals whose fine resolution is less precise than that for sinusoidal encoders. The TTL/HTL encoders permit only a fine resolution of 2 bits = 4, because only the signal edges can be counted here.

![TTL/HTL encoder](images/147854600075_DV_resource.Stream@PNG-en-US.png)

TTL/HTL encoder

**Fine resolution for SIN/COS encoders**

For SIN/COS encoders, the analog signals of the A and B tracks are evaluated. A position value is determined uniquely via the two analog voltage values in all four quadrants of the encoder pulse. The sinusoidal voltage values permit a greater resolution, e.g. 11 bits per encoder pulse. This resolution of 11 bits and 2048 encoder pulses per revolution (=2<sup>11</sup>) results in a total resolution of 22 bits.

![Incremental encoders](images/147854595211_DV_resource.Stream@PNG-en-US.png)

Incremental encoders

- Enter a value in bits for the fine resolution XIST_1 (p0418) of the deployed encoder. The factory setting of 11 bits suffices for all Siemens motor encoders.

##### Fine resolution position value for XIST_2 (p0419)

Like with Gn_XIST1, the position value of the Gn_XIST2 contains a fine resolution (p0419). Here, too, the position values of the absolute position are multiplied within one sinusoidal period.

- Enter a value in bits for the fine resolution X_IST2 (p0419) of the deployed encoder.

  The fine resolution is already preset to 9 bits for sinusoidal SIEMENS encoders.

##### Relationship between multiturn resolution and fine resolution (p0419 - X_IST2)

The actual encoder values transferred from the drive to the controller are limited to 32 bits. If, for example, a standard multiturn encoder with a multiturn resolution of 12 bits (4096) and number of encoder pulses per revolution of 2048 (=2<sup>11</sup>) is used, only 32-12-11=9 bits (512) remain in the actual encoder value for the fine resolution (p0419). The following graphic shows the relationship between multiturn information and fine resolution. Increasing the fine resolution moves the value of the multiturn information to the left, which decreases the multiturn range of the encoder that can be used.

![Relationship between multiturn resolution and fine resolution (p0419 - X_IST2)](images/147854604939_DV_resource.Stream@PNG-en-US.png)

##### Extrapolating the position value

This parameter is displayed only for pure SSI encoders, i.e. for encoders without additional incremental tracks. Compared with the current controller clock of the SINAMICS, the serial transfer is relatively slow, and therefore the data can already be obsolete on arrival at the Sensor Module.

A dead time of at least one current controller clock occurs.

1. Activate the "Extrapolate position value" option to extrapolate the SSI data for the next current controller clock.

   - Advantage: The dead time decreases and the controller becomes more dynamic.
   - Disadvantage: The extrapolated value can be inaccurate with dynamic position changes.
2. Evaluate the advantages and disadvantages carefully.
3. Also check the deployed baud rate. A higher baud rate may allow a sufficiently fast data transmission.

##### Parameterizing inversion

The parameter is already preset for standard motors. The counting direction of the encoder ([p0410](SINAMICS%20Parameter%20SERVO.md#p04100n-encoder-inversion-actual-value-1) bit 0 = 1 and bit 1 = 1) can be set for third-party or modular motors. The counting direction (speed and position) of the encoder is inverted.

1. Activate the "Actual speed value inverted" (p0410[0].0) option.
2. Activate the "Actual position value inverted" (p0410[0].1) option.

> **Note**
>
> **Inversion when using DSC**
>
> If you have activated the "DSC with spline" function module, you must invert p0410[0].0 and p0410[0].1 to invert the two actual values.

##### Parameterizing the measuring gearbox position tracking

The position tracking serves to reproduce and extend the traverse range of the load position when measuring gearboxes are used. Measuring gearboxes are deployed when the encoder is not mounted on the motor shaft, but rather, for example, driven with a belt or gear wheels with different diameters. The transformation ratio must not be 2<sup>n</sup>. The position tracking can also be used to extend the measuring range of the encoder for a linear axis.

**Virtual multiturn resolution ([p0412](SINAMICS%20Parameter%20SERVO.md#p04120n-measuring-gear-absolute-encoder-rotary-revolutions-virtual))**

For a rotary absolute encoder ([p0404](SINAMICS%20Parameter%20SERVO.md#p04040n-encoder-configuration-effective).1 = 1) with activated position tracking ([p0411](SINAMICS%20Parameter%20SERVO.md#p04110n-measuring-gear-configuration).0 = 1), p0412 specifies a virtual multiturn resolution. This makes it possible to generate a virtual multiturn encoder (r0483) from a singleturn encoder. It must be possible to represent the virtual encoder range in r0483.

When no measuring gearboxes (n = 1) are present, the value in [p0421](SINAMICS%20Parameter%20SERVO.md#p04210n-absolute-encoder-rotary-multiturn-resolution) replaces the actual number of stored revolutions of a rotary absolute encoder. Increasing this value extends the position range (see linear axis). When measuring gearboxes are present, this value sets the resolvable motor revolutions represented in r0483.

**Tolerance window ([p0413](SINAMICS%20Parameter%20SERVO.md#p04130n-measuring-gear-position-tracking-tolerance-window))**

After switch on, the difference between the stored position and the current position is determined and initiated depending on the following:

- Difference within the tolerance window: The position is reproduced based on the current encoder actual value.
- Difference outside the tolerance window: Message F07449 is issued.
- The tolerance window is preassigned to the encoder range quadrant, although it can be changed.

**Making settings**

1. Activate the option for the position tracking for measuring gearboxes.
2. Activate the desired axis type (p0411).

   By default, the "Rotary axis" axis type is active.

   A rotary axis is considered to be a modulo axis (modulo correction can be activated by a higher-level controller or EPOS). For a linear axis, the position tracking is used principally to extend the position range (see "Virtual multiturn resolution").
3. If required, correct the default value for a rotary absolute encoder in the "Virtual multiturn resolution" (p0412) field.

   With a linear axis, this field is deactivated.
4. If required, correct the default value for the tolerance window for the position tracking in the "Tolerance window" (p0413) field.

##### Function diagrams (FD)

Encoder evaluation - Speed actual value and pole position sensing encoder 1 - 4710 -

Encoder evaluation - Encoder interface, receive signals encoder 1 … 3 - 4720 -

Encoder evaluation - Encoder interface, send signals encoder 1 … 3 - 4730 -

##### Additional parameters

---

#### Rotor position synchronization (servo)

This section contains information on the following topics:

- [Rotor position synchronization (servo)](#rotor-position-synchronization-servo-1)
- [Supplementary conditions of the synchronization procedure](#supplementary-conditions-of-the-synchronization-procedure)
- [Important parameters of the synchronization procedures](#important-parameters-of-the-synchronization-procedures)

##### Rotor position synchronization (servo)

###### Description

For synchronous motors, the pole position identification determines the electrical pole position required for the field-oriented closed-loop control. Normally, the electrical pole position is provided with absolute information by a mechanically adjusted encoder.

The content of the "Rotor position synchronization" screen form depends on the encoder used.

No pole position identification is required for the following encoder properties for a mechanically calibrated encoder:

- Absolute encoder (e.g. EnDat, DRIVE-CLiQ encoder)
- Encoder with C/D track and number of pole pairs ≤ 8
- Hall sensor (linear motor)
- Resolver with integer ratio from the number of motor pole pairs to the number of encoder pole pairs (absolute electrical installation)
- Incremental encoder with an integer ratio from the number of motor pole pairs to the number of encoder pulses

The settings can be made ONLINE as well as OFFLINE.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Faulty safety functions of the drive with no pole position identification**  If no pole position identification is carried out, fault-free functioning of the safety functions of the drive cannot be completely guaranteed, which could lead to death or serious injuries.  - Carry out pole position identification. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrolled motor motion as a result of an incorrect control sense of the speed control loop**  If a pole position identification was used to determine the commutation angle, the commutation angle must be determined again each time the control sense changes. An incorrect commutation angle may result in uncontrollable motor movement which can cause death or serious injuries.   - Check the commutation angle offset (F7966) after an actual value inversion and, if necessary, determine the offset again ([p1990](SINAMICS%20Parameter%20SERVO.md#p1990-encoder-adjustment-determine-angular-commutation-offset) = 1). |  |

###### Requirements

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- An encoder has been configured.
- Coarse synchronization was performed successfully.

###### Position identification procedures

The following procedures are available for pole position identification:

- Saturation-based technique  
  "Saturation-based..." is the preferred technique if motor motion is not possible. This procedure may be performed only by experienced qualified personnel because the motor can run away. If you do not master this technique, contact the Siemens Service. The saturation-based technique utilizes the effect that the iron saturation changes the inductance of the motor in various space-vector directions depending on the rotor position. Consequently, this version functions correctly only for motors with an iron core.

  The saturation-based procedure can be used for both braked and non-braked motors.

  - [0] Saturation-based 1st + 2nd harmonics

    This procedure is more precise than procedure [1] if the motor is suitable for it.
  - [1] Saturation-based 1st harmonic

    This procedure is universally suitable (for motors with iron in the magnetic circuit).
  - [4] Saturation-based 2-stage

    This procedure is quieter than the variants [0] and [1] if the motor is suitable for it.
- [10] Motion-based

  The motion-based procedure requires that the motor can move and that no motor brake is installed. You can find more information on the requirements for the motion-based procedure under [Supplementary conditions of the synchronization procedure](#supplementary-conditions-of-the-synchronization-procedure).

  The motion-based pole position identification is the preferred procedure when the motor can move. The motor is moved to the left and right.
- [20] Elasticity-based

  You can find more information on the requirements for the elasticity-based procedure under [Supplementary conditions of the synchronization procedure](#supplementary-conditions-of-the-synchronization-procedure).

  You can find an example of instructions on how to set elasticity-based pole position identification in the SINAMICS S120 Function Manual for Drive Functions in the section "Setting of the elasticity-based pole position identification".
- [99] No technique selected

###### Pole position identification for motors that are not listed

For motors that are not listed in the motor selection, you must configure the pole position identification yourself.

1. Select a suitable procedure for the motor used in the "Technique" ([p1980](SINAMICS%20Parameter%20SERVO.md#p19800n-polid-technique)) drop-down list (see "Position identification procedures").

   See also "[Supplementary conditions of the synchronization procedure](#supplementary-conditions-of-the-synchronization-procedure)".
2. Select the "Pole position identification" option to activate the technique.

**Result**

When was the synchronization **not** successful?

- The motor provides insufficient or no torque.
- The motor becomes hot too fast.
- An appropriate fault message is shown in the message display.

###### Pole position identification for Siemens motors

Use the automatic default setting for the pole position identification when using Siemens standard motors. No further settings are necessary.

###### Fine synchronization

The pole position identification provides a coarse synchronization. If zero marks are present, after traversing the zero mark(s), the pole position is calibrated automatically with the zero mark position (fine synchronization). The zero mark position must be calibrated mechanically or electrically ([p0431](SINAMICS%20Parameter%20SERVO.md#p04310n-angular-commutation-offset)). If the encoder system permits this calibration, a fine synchronization is recommended ([p0404](SINAMICS%20Parameter%20SERVO.md#p04040n-encoder-configuration-effective).15 = 1) because it avoids measurement spreads and permits an additional test of the determined pole position.

Suitable zero marks are:

- A zero mark in the complete traversing range
- Equidistant zero marks

  A prerequisite for determining the pole position using equidistant zero marks is that the zero mark distance of the encoder is a multiple integer of the pole pitch/pole pair width of the motor.
- Distance-coded zero marks
- One zero mark per mechanical revolution.

###### Additional parameters

---

---

**See also**

[Important parameters of the synchronization procedures](#important-parameters-of-the-synchronization-procedures)

##### Supplementary conditions of the synchronization procedure

###### Saturation-based procedure

The following notes and supplementary conditions apply to the saturation-based procedure:

- This procedure can be used for both braked and non-braked motors.
- It can only be used for a speed setpoint = 0 or from standstill.
- The specified current magnitudes ([p0325](SINAMICS%20Parameter%20SERVO.md#p03250n-motor-pole-position-identification-current-1st-phase), [p0329](SINAMICS%20Parameter%20SERVO.md#p03290n-motor-pole-position-identification-current)) must be sufficient to provide a significant measuring result.
- For motors without iron, the pole position cannot be identified using the saturation-based procedure.
- For 1FN3 motors, it is not permissible to traverse with the 2nd harmonic ([p1980](SINAMICS%20Parameter%20SERVO.md#p19800n-polid-technique) = 0, 4).
- With 1FK7 motors, a two-stage procedure must not be used (p1980 = 4). The value in p0329, which is set automatically, must not be reduced.

###### Motion-based procedure

> **Note**
>
> **Inaccuracy when determining the commutation angle**
>
> If several 1FN3 linear motors are coupled with one another, and at the same time saturation-based pole position identification is used for commutation (p1980 ≤ 4 and [p1982](SINAMICS%20Parameter%20SERVO.md#p19820n-polid-selection) = 1), then this can influence the DC link voltage. Fast current changes in the DC link cannot be completely compensated. In this case, the commutation angle is not precisely determined using the pole position identification.
>
> - If a high precision is required, then carry out the pole position identification routines one after the other. This can be achieved, for example, by enabling the individual drives one after the other (with a time offset).

The following notes and supplementary conditions apply to the motion-based procedure:

- The motor must be free to move and it may not be subject to external forces (no hanging/suspended axes).
- It can only be used for a speed setpoint = 0 or from standstill.
- If there is a motor brake, then this must be open ([p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration) = 2).
- The specified current magnitude ([p1993](SINAMICS%20Parameter%20SERVO.md#p19930n-polid-motion-based-current)) must move the motor by a sufficient amount.

###### Elasticity-based procedure

For the elasticity-based technique, the following notes and supplementary conditions apply:

- A brake must be available and must also be activated during the pole position identification. Either the drive controls the brake (p1215 = 1 or 3) or the brake is externally closed well in advance of the start of the pole position ID and is deactivated again after the operation has been completed.
- A position sensor must be available and also activated.
- Drive axis motion corresponds to the deflection (motion in the μm to mm range). Uncontrollable axis motion is completely ruled out **during** the measurement.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Uncontrollable axis motion as a result of incorrect settings**  For incorrect settings during the elasticity-based pole position ID, when enabling the axis after the measuring technique, uncontrollable axis motion can occur that can lead to death or severe injury. - Ensure that the settings in the context of this technique are correct. - Ensure that after exiting the technique, the axis cannot move. |  |
- Parameters [p3090](SINAMICS%20Parameter%20SERVO.md#p30900n-polid-elasticity-based-configuration) to [p3096](SINAMICS%20Parameter%20SERVO.md#p30960n-polid-elasticity-based-current) must be correctly set for a successful pole position ID.

  The following table provides information on how to set parameters p3090 to p3096.

  | Parameter | Name | Information about parameterization |
  | --- | --- | --- |
  | p3090 | Pole ID elasticity-based configuration | The value "0" is preset in the parameter. For motors, where the brake is installed between the motor and encoder, an inversion may be required in order to take into account the relationship between the sign of the deflection and the torque or force. The inversion is set in bit 0 (p3090[0]). |
  | [p3091](SINAMICS%20Parameter%20SERVO.md#p30910n-polid-elasticity-based-ramp-time) | Pole ID elasticity-based ramp time | The ramp time is preset with 250 ms. This value should only be changed if mechanical oscillations are present. Generally, mechanical oscillations occur if the ramp time is too short (&lt; 250 ms). |
  | [p3092](SINAMICS%20Parameter%20SERVO.md#p30920n-polid-elasticity-based-wait-time) | Pole ID elasticity-based wait time | The wait time serves as buffer between the measurement operations. Set a wait time longer than 5 ms in order to make a clear distinction between the individual measuring operations. |
  | [p3093](SINAMICS%20Parameter%20SERVO.md#p30930n-polid-elasticity-based-measurement-number) | Pole ID elasticity-based measurement count | Set 12 measurement steps to achieve a rugged and precise pole position ID. The precision and duration of the measurement increases proportionally with the number of measurement steps. |
  | [p3094](SINAMICS%20Parameter%20SERVO.md#p30940n-polid-elasticity-based-deflection-expected-1) | Pole ID elasticity-based deflection expected | The parameter setting depends heavily on the mechanical design and the drive braking force, and must therefore be set by the customer.  To determine the expected deflection, the technique must be initiated with an already set current (p3096) - and a deflection that has still not been set (p3094). |
  | [p3095](SINAMICS%20Parameter%20SERVO.md#p30950n-polid-elasticity-based-deflection-permissible-1) | Pole ID elasticity-based deflection permitted | The maximum permissible deflection preset in the parameter is 1 degree or 1 mm. This deflection cannot be reached if the current has been correctly set. The maximum permissible deflection is correctly set if the deflection for different current values is approximately the same - or there is no deflection at all. |
  | p3096 | Pole ID elasticity-based current | The parameter setting depends heavily on the mechanical design and the drive braking force, and must therefore be set by the customer.  The value "0" is preset in the parameter. An orientation value is approximately <sup>1</sup>/<sub>3</sub> of the rated motor current. When setting the parameter, a check must be made to ensure that the brake is powerful enough to hold the load for the set current value. The specified current value (p3096) must deflect the motor by a sufficient amount. The current has been correctly set if, after the current has been withdrawn, the deflection returns to its original value. |

###### Additional parameters

---

##### Important parameters of the synchronization procedures

###### Important parameters (depending on the procedure)

The following table provides an overview of the important parameters depending on the procedure selected for the pole position identification:

|  | Saturation-based | Motion-based | Elasticity-based |
| --- | --- | --- | --- |
| [p0325](SINAMICS%20Parameter%20SERVO.md#p03250n-motor-pole-position-identification-current-1st-phase) | + | - | - |
| [p0329](SINAMICS%20Parameter%20SERVO.md#p03290n-motor-pole-position-identification-current) | + | - | - |
| [p1980](SINAMICS%20Parameter%20SERVO.md#p19800n-polid-technique) | Value 0, 1 or 4 | Value 10 | Value 20 |
| [p1981](SINAMICS%20Parameter%20SERVO.md#p19810n-polid-distance-max) | + | + | - |
| [p1982](SINAMICS%20Parameter%20SERVO.md#p19820n-polid-selection) | + | + | + |
| [p1983](SINAMICS%20Parameter%20SERVO.md#p1983-polid-test) | + | + | + |
| [r1984](SINAMICS%20Parameter%20SERVO.md#r1984-polid-angular-difference) | + | + | + |
| [r1985](SINAMICS%20Parameter%20SERVO.md#r1985-polid-saturation-curve) | + | + | + |
| [r1986](SINAMICS%20Parameter%20SERVO.md#r1986-polid-saturation-characteristic-2) | + | + | + |
| [r1987](SINAMICS%20Parameter%20SERVO.md#r1987-polid-trigger-characteristic) | + | + | + |
| [p1990](SINAMICS%20Parameter%20SERVO.md#p1990-encoder-adjustment-determine-angular-commutation-offset) | + | + | + |
| [r1992](SINAMICS%20Parameter%20SERVO.md#r1992015-cobo-polid-diagnostics-1) | + | + | + |
| [p1993](SINAMICS%20Parameter%20SERVO.md#p19930n-polid-motion-based-current) | - | + | - |
| [p1994](SINAMICS%20Parameter%20SERVO.md#p19940n-polid-motion-based-rise-time) | - | + | - |
| [p1995](SINAMICS%20Parameter%20SERVO.md#p19950n-polid-motion-based-gain-1) | - | + | - |
| [p1996](SINAMICS%20Parameter%20SERVO.md#p19960n-polid-motion-based-integral-time) | - | + | - |
| [p1997](SINAMICS%20Parameter%20SERVO.md#p19970n-polid-motion-based-smoothing-time) | - | + | - |
| [p3090](SINAMICS%20Parameter%20SERVO.md#p30900n-polid-elasticity-based-configuration) | - | - | + |
| [p3091](SINAMICS%20Parameter%20SERVO.md#p30910n-polid-elasticity-based-ramp-time) | - | - | + |
| [p3092](SINAMICS%20Parameter%20SERVO.md#p30920n-polid-elasticity-based-wait-time) | - | - | + |
| [p3093](SINAMICS%20Parameter%20SERVO.md#p30930n-polid-elasticity-based-measurement-number) | - | - | + |
| [p3094](SINAMICS%20Parameter%20SERVO.md#p30940n-polid-elasticity-based-deflection-expected-1) | - | - | + |
| [p3095](SINAMICS%20Parameter%20SERVO.md#p30950n-polid-elasticity-based-deflection-permissible-1) | - | - | + |
| [p3096](SINAMICS%20Parameter%20SERVO.md#p30960n-polid-elasticity-based-current) | - | - | + |
| [r3097](SINAMICS%20Parameter%20SERVO.md#r3097031-bo-polid-elasticity-based-status) | - | - | + |
| Marking: + = relevant, - = not relevant |  |  |  |

###### Additional parameters

---

---

**See also**

[Rotor position synchronization (servo)](#rotor-position-synchronization-servo-1)

#### Mechanical system

##### Description

The screen form displays the mechanical system configured in the drive wizard. You can check and, if required, change the settings for the position control. Depending on the encoder type selected for position control and the encoder type selected for the motor encoder, various configurations are displayed for the mechanical system.

The position tracking serves to reproduce the load position when gearboxes are deployed. It can also be used to extend the position range. The position tracking of the load gear however, is only relevant for a motor encoder (encoder 1).

##### Requirements

- The "Basic positioner" and/or "Position control" function module has been activated.
- The drive axis is OFFLINE.

  The entire basic parameter assignment can only be performed offline for the selected drive axis.

##### Parameterizing the position control

An encoder is assigned to the position control during commissioning. This encoder setting is shown in a drop-down list at the top right in the "Mechanical system" screen form. You can change the encoder assignment in this screen form before parameterizing the position control. The following options are available:

1. Select the required encoder in the "Encoder system" ([p2502](SINAMICS%20Parameter%20SERVO.md#p25020n-lr-encoder-assignment)) drop-down list.

   - No encoder
   - Encoder 1
   - Encoder 2
   - Encoder 3
2. Enter the motor revolutions for the gear ratio between the motor shaft and load shaft in the "Number of motor revolutions" ([p2504](SINAMICS%20Parameter%20SERVO.md#p25040n-lr-motorload-motor-distance-1)) field.
3. Enter the load revolutions for the gear ratio between the motor shaft and load shaft in the "Number of load revolutions" ([p2505](SINAMICS%20Parameter%20SERVO.md#p25050n-lr-motorload-load-revolutions)) field.
4. Enter the neutral length unit LU per load revolution in the "LU per load revolution" ([p2506](SINAMICS%20Parameter%20SERVO.md#p25060n-lr-length-unit-lu-per-load-path-1)) field.
5. Interconnect the "Modulo correction activation" ([p2577](SINAMICS%20Parameter%20SERVO.md#p2577-bi-epos-modulo-correction-activation)) signal source for the activation of the modulo correction.
6. Correct the default value for axes with modulo correction in the "Modulo correction modulo range" ([p2576](SINAMICS%20Parameter%20SERVO.md#p2576-epos-modulo-correction-modulo-range)) field.

##### Parameterizing the load gearbox position tracking

If you have parameterized encoder 1 for the position control, you can set the position tracking as follows:

1. Activate the "Activate load gearbox position tracking" (p2729.0) option.
2. Activate the desired axis type ([p2720](SINAMICS%20Parameter%20SERVO.md#p27200n-load-gear-configuration).1).

   By default, the "Rotary axis" axis type is active.
3. If required, correct the number of resolvable revolutions for a rotary absolute encoder in the "Virtual revolutions" ([p2721](SINAMICS%20Parameter%20SERVO.md#p27210n-load-gear-rotary-absolute-encoder-revolutions-virtual)) field.
4. If required, correct the value for the tolerance window for the position tracking in the "Position tracking tolerance window" ([p2722](SINAMICS%20Parameter%20SERVO.md#p27220n-load-gear-position-tracking-tolerance-window)) field. The value is specified in whole encoder pulses.

##### Examples of LU configurations

The unit LU per load revolution is a free dimension, independent of SI units, for the position control of an EPOS axis.

The LU per load revolution upper limit is limited by the encoder resolution (rXXXX). A value above this limit can be selected, but then not all set positions can be approached because they may be between two encoder lines. This could result in an unsmooth axis.

The LU per load revolution should be selected as high as possible. In this way, a better dynamic response can be achieved. If the values for p2506 are too low, this can result in jumps when speed precontrol is activated.

For good repeat accuracy, the LU per load revolution should be selected in the ratio of 1:10 to the encoder resolution, if the encoder resolution can provide this at the required dynamic response.

**Example 1: Linear axis – spindle (encoder on the motor side)**

Leadscrew pitch = 10 mm

Gear ratio i = 1 (p2505/p2504)

Target variable to be controlled: mm

Encoder resolution = 15,000 LU

10 mm distance are travelled per load revolution. According to the encoder resolution, maximum 15,000 LU/10 mm = 1,500 LU per mm can be defined. We will select 1,000 LU per mm (1 LU = 1 µm). 10 mm per revolution results in 10,000 per revolution:

- p2506 = 10,000 LU per load revolution

**Example 2: Rotary axis (encoder on the motor side)**

Gear ratio i = 44.5

- p2504 = 445 motor revolutions
- p2505 = 10 load revolutions

Target variable to be controlled: °

Encoder resolution = 364,544 LU

360° are travelled per load revolution. According to the encoder resolution, maximum 364,544 LU/360° = 1012 LU per ° can be defined. We will select 100 LU per ° (1 LU = 0.01°). 360° per revolution results in 36,000 LU per load revolution.

- p2506 = 36,000 LU per load revolution

**Example 3: Modulo axis – chain drive**

The chain has 250 chain links and a chain link is 0.0338667344 m long. The output wheel has 40 teeth, i.e. 40 chain links are moved per revolution. The target positions are at a distance of 25 chain links to one another.

Gear ratio i = 114.28 (rounded off)

Ratio of the number of teeth of the gearbox = 106,967/936

- p2504 = 106,967 motor revolutions
- p2505 = 936 load revolutions

Encoder resolution = 468,095 LU

The encoder resolution is too low here to convert the chain links to a linear SI unit without rounding-off errors having an effect on the modulo correction. A chain link must therefore be taken as target variable.

Target variable to be controlled: 1 chain link

40 chain links travelled per load revolution. According to the encoder resolution, maximum 468,095 LU/40 chain links = 11,702 LU per chain link can be selected. We will therefore select 1,000 LU per chain link (1 LU = 33.8667344 µm). 40 chain links per revolution results in:

- p2506 = 40,000 LU per load revolution
- p2576 = 250,000 LU modulo range

##### Function diagrams (FD)

- Position control - Position actual value processing (r0108.3 = 1) - 4010 -
- Position control - Position controller (r0108.3 = 1) - 4015 -
- Position control - Standstill monitoring / position monitoring (r0108.3 = 1) - 4020 -
- Position control - Dynamic following error monitoring, cam sequencer (r0108.3 = 1) - 4025 -

##### Additional parameters

---

#### Enable logic (servo)"

If telegrams were interconnected during commissioning, these interconnections are displayed here and an additional specification is not required.

If no telegrams were specified previously, then you must interconnect the required signal sources via the enable logic.

The enable logic can be carried out ONLINE as well as OFFLINE.

##### Interconnecting signal sources

1. Interconnect the signal source for the "Infeed operation" ([p0864](SINAMICS%20Parameter%20SERVO.md#p0864-bi-infeed-operation)) command.
2. Interconnect the signal source for the "OFF1 (low-active)" command ([p0840](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08400n-bi-on-off-off1)).

   This command corresponds to control word 1 bit 1 (STW1.1) in the PROFIdrive profile.
3. Interconnect the 1st signal source for the "OFF2 (low-active) signal source 1" command ([p0844](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1)).

   This command corresponds to control word 1 bit 1 (STW1.1) in the PROFIdrive profile.
4. Interconnect the 2nd signal source for the "OFF2 (low-active) signal source 2" command ([p0845](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)).
5. Interconnect the 1st signal source for the "OFF3 (low-active) signal source 1" command ([p0848](SINAMICS%20Parameter%20SERVO.md#p08480n-bi-no-quick-stop-quick-stop-off3-signal-source-1)).

   This command corresponds to control word 1 bit 2 (STW1.2) in the PROFIdrive profile.
6. Interconnect the 2nd signal source for the "OFF3 (low-active) signal source 2" command ([p0849](SINAMICS%20Parameter%20SERVO.md#p08490n-bi-no-quick-stop-quick-stop-off3-signal-source-2)).

   This command corresponds to control word 1 bit 2 (STW1.2) in the PROFIdrive profile.
7. Interconnect the signal source for the "Release operation" command ([p0852](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08520n-bi-enable-operationinhibit-operation)).

   This command corresponds to control word 1 bit 3 (STW1.3) in the PROFIdrive profile.

##### Additional parameters

---

#### Data sets

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Structure of the data set screen form](#structure-of-the-data-set-screen-form)
- [Managing a command data set (CDS)](#managing-a-command-data-set-cds)
- [Managing a drive data set (DDS)](#managing-a-drive-data-set-dds)
- [Activating or editing data sets](#activating-or-editing-data-sets)
- [Switching data sets](#switching-data-sets)

##### Fundamentals

###### Overview

For many applications it is beneficial if multiple parameters can be changed simultaneously by means of an external signal during operation or when the system is ready for operation. This can be carried out with the aid of indexed parameters. For the purpose of this function, the parameters have been combined in such a way that they form groups or data sets and are indexed. By using the indexing, several different settings can be stored for each parameter and activated by changing the data set (i.e. switching back and forth between the data sets).

Those parameters (connector and binector inputs) that are used to control the converter and enter a setpoint are assigned to the command data set (CDS).

The drive data set (DDS) contains various adjustable parameters that are relevant for the open-loop and closed-loop motor control.

You can configure the data sets for each drive within a project:

- You create the corresponding components in the device configuration.
- You configure the available data sets in Startdrive while creating new data sets or deleting existing data sets.

###### Function diagrams (FD)

- Data sets - Command data sets (CDS) - 8560 -
- Data sets - Drive data sets (DDS) - 8565 -
- Data sets - Encoder data sets (EDS) - 8570 -
- Data sets - Motor data sets (MDS) - 8575 -

###### Parameters

- [p0120](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0120-number-of-power-unit-data-sets-pds)
- [p0130](SINAMICS%20Parameter%20SERVO.md#p0130-number-of-motor-data-sets-mds)
- [p0139](SINAMICS%20Parameter%20SERVO.md#p013902-copy-motor-data-set-mds)
- [p0140](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0140-number-of-vsm-data-sets)
- [p0170](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0170-number-of-command-data-sets-cds)
- [p0180](SINAMICS%20Parameter%20SERVO.md#p0180-number-of-drive-data-sets-dds)
- [p0809](SINAMICS%20Parameter%20SERVO.md#p080902-copy-command-data-set-cds)
- [p0819](SINAMICS%20Parameter%20SERVO.md#p081902-copy-drive-data-set-dds)

---

---

**See also**

[Activating or editing data sets](#activating-or-editing-data-sets)
  
[Data set definitions](Configuring%20SINAMICS%20S-G-MV%20drives.md#data-set-definitions)
  
[Rules for using data sets](Configuring%20SINAMICS%20S-G-MV%20drives.md#rules-for-using-data-sets)

##### Structure of the data set screen form

###### Structure of the data set screen forms

![Example: Screen form for drive data sets](images/147854769291_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icons for editing/activating DDS drive data sets in online mode. Not relevant for CDS. |
| ② | Two buttons in the active data set screen form enable the insertion and deletion of individual data sets of the list. |
| ③ | List of created drive data sets. The created data sets are numbered chronologically. In the list of drive data sets, different (MDS or EDS) data sets are assigned to the drive data sets. |
| ④ | Working area for activating a selected data set via BICO interconnections. |

Example: Screen form for drive data sets

###### Icons for editing data sets in the online mode

The editing mode must be activated first in order to edit data sets in the online mode. The editing mode is not required in the offline mode.

| Icon | Description |
| --- | --- |
| ![Icons for editing data sets in the online mode](images/147854075915_DV_resource.Stream@PNG-en-US.png) | Startdrive is not online.   You can only edit the data sets offline. |
| ![Icons for editing data sets in the online mode](images/147854079883_DV_resource.Stream@PNG-en-US.png) | Startdrive is online.   The editing mode is not activated yet. |
| ![Icons for editing data sets in the online mode](images/147854083851_DV_resource.Stream@PNG-en-US.png) | Startdrive is online.   The editing mode is active. |

##### Managing a command data set (CDS)

###### Overview

You can edit the command data sets of the drive via the "Command data sets (CDS)" screen form. The following CDS can be edited at most:

- 2 CDS for infeeds
- 2 CDS for SERVO drives
- 4 CDS for VECTOR drives

###### Requirements

- At least 1 CDS exists (for Line Module, Power Module, or Motor Module).
- The basic parameterization of an infeed or a drive axis has been opened in the secondary navigation.
- Creating and deleting CDSs: There is no online connection to the drive.

  CDSs can only be created or deleted offline. However, CDSs can be activated online.

###### Creating a new command data set (CDS)

1. Click "Add".

   The "Add new command data set" dialog box opens.

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   Adding a CDS
2. Make sure that the "Create as copy" option is deactivated.
3. Click "OK" in the dialog box.

**Result**

A new command data set is created in the list.

###### Creating a new CDS with contents from other CDSs

1. Click "Add".

   The "Add new command data set" dialog box opens.

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   Adding a CDS
2. Activate the "Create as copy" option.
3. Click "OK" in the dialog box to confirm your selection.

**Note**

**Special case for VECTOR drives**

If more than 2 CDS are available for VECTOR drives, you can select at this point which available CDS should be copied.

**Result**

The new command data set is created from the selected template and also inserted in the last position of the list of command data sets.

###### Deleting a command data set (CDS)

In order for command data sets to be deleted, at least 2 CDS (for servo drives or infeed) or 3 CDS (for vector drives) must be available in the list.

1. Select the CDSs to be deleted in the list of command data sets.

   The CDS is displayed again in detail in a worklist located below the collective list.
2. Click "Delete".

   A confirmation prompt is displayed.

   ![Deleting a CDS](images/147854114827_DV_resource.Stream@PNG-en-US.PNG)

   ![Deleting a CDS](images/147854114827_DV_resource.Stream@PNG-en-US.PNG)

   Deleting a CDS
3. Click "OK" to delete the data set.

**Result**

The CDS is deleted from the list of command data sets. The subsequent CDSs in the list will be renumbered if necessary. The numbering of the CDSs is always chronological. The last available CDS remains and cannot be deleted.

##### Managing a drive data set (DDS)

###### Overview

You can edit the drive data sets of the drive via the "Drive data sets (DDS)" screen form.

###### Requirements

- The drive has at least one drive axis.
- The basic parameterization of a drive axis has been opened in the secondary navigation.

###### Creating a new DDS as a copy of an existing DDS

New drive data sets always can be created via the "Drive data sets (DDS)" screen form only as a copy of an existing data set.

1. Click "Add".

   The "Add new drive data set" dialog box opens.

   ![Adding a DDS](images/147854795531_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a DDS](images/147854795531_DV_resource.Stream@PNG-en-US.PNG)

   Adding a DDS

   The list shows the existing drive data sets which can be used as master copies.
2. Activate the "Copy" option for the existing data set which you want to use as a master copy.
3. Click "OK" in the dialog box to confirm your selection.

**Result**

The new drive data set is created from the selected template and also inserted in the last position of the list of drive data sets.

###### Deleting a drive data set (DDS)

Drive data sets can be deleted only if there are at least two DDSs in the list.

1. Select the DDSs to be deleted in the list of drive data sets.

   The DDS is displayed again in detail in a worklist located below the collective list.
2. Click "Delete".

   A confirmation prompt is displayed.

   ![Example: Deleting a DDS](images/147854799499_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Deleting a DDS](images/147854799499_DV_resource.Stream@PNG-en-US.PNG)

   Example: Deleting a DDS
3. Click "OK" to delete the DDS.

**Result**

The DDS is deleted from the list of drive data sets. The subsequent DDSs in the list will be renumbered if necessary. The numbering of the DDSs is always chronological. The last available DDS remains and cannot be deleted.

###### Online mode: Assign encoder data sets (EDS)

The editing mode must be active in order to edit data sets in the online mode.

1. Click the ![Online mode: Assign encoder data sets (EDS)](images/147854138763_DV_resource.Stream@PNG-en-US.png) icon to start the editing mode.
2. Select a DDS in the list of drive data sets.
3. Click in the EDS cell of the data set row and select the required EDS from the "Motor encoder" drop-down list.

   If you want to assign 2 additional EDSs, repeat this step using the "External encoder 1" and "External encoder 2" drop-down lists.
4. Click the ![Online mode: Assign encoder data sets (EDS)](images/147854142731_DV_resource.Stream@PNG-en-US.png) icon to quit the editing mode on completing the settings.

**Result**

The assigned data sets are displayed for the selected DDS in the list of drive data sets.

###### Offline mode: Assign encoder data sets (EDS)

In the offline mode, the data sets can be configured without an editing mode.

1. Select a DDS in the list of drive data sets.
2. Click in the EDS cell of the data set row and select the required EDS from the "Motor encoder" drop-down list.

   If you want to assign 2 additional EDSs, repeat this step using the "External encoder 1" and "External encoder 2" drop-down lists.

**Result**

The assigned data sets are displayed for the selected DDS in the list of drive data sets. The drive data then has to be downloaded to the drive for use in the drive.

##### Activating or editing data sets

###### Overview

Several data sets of a data set type must be created for a data set switchover.

###### Editing offline

To assign the settings of a drive to a data set, proceed as follows:

1. Open the configuration screen form for the desired data set type (e.g. the screen form for the drive data set).
2. Select the required data set from the list of data sets.
3. Change the signal sources of the BICO interconnections at the bottom of the working area.
4. Save your settings [permanently](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings).

**Result:**

Specific parameterizations are available for each of the various data sets.

###### Editing online

The editing mode must be active in order to edit data sets in the online mode.   
To assign the settings of a drive to a data set, proceed as follows:

1. Click the ![Editing online](images/147854138763_DV_resource.Stream@PNG-en-US.png) icon to start the editing mode.
2. Open the configuration screen form for the desired data set type (e.g. the screen form for the drive data set).
3. Select the required data set from the list of data sets.
4. Change the signal sources of the BICO interconnections at the bottom of the working area.
5. Save your settings [permanently](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings).
6. Click the ![Editing online](images/147854142731_DV_resource.Stream@PNG-en-US.png) icon to quit the editing mode on completing the settings.

**Result:**

Specific parameterizations are available for each of the various data sets.

##### Switching data sets

###### Overview

You can switch between different data sets in the configuration screen form. The switchover is performed via drop-down lists in the toolbar.

![Data set switchover](images/147854824715_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Shows the active drive data set (DDS). Enables switchover to a different data set. |
| ② | Shows the active command data set (CDS). Enables switchover to a different data set. |

Data set switchover

###### Requirement

- Multiple drive data sets or command data sets have been created.

  If only one data set of one data set type has been created, the drop-down list for switchover is deactivated.

###### Procedure

1. Open the required configuration screen form.

   The drop-down lists for the data set switchover show the active data set in each case. The settings and parameter values of this data set are displayed in the screen form below them.
2. Select another data set from the drop-down lists for the data set switchover.
3. Change the signal sources of the BICO interconnections at the bottom of the working area.

###### Result

In the screen form, all data-set-dependent settings are changed to the values of the selected data set (if these values are configured differently). The differences in the drive data sets also may result solely from the MDSs or EDSs used in the selected DDS.

### Setpoint channel

This section contains information on the following topics:

- [Setpoint sources and setpoint preparation (servo)](#setpoint-sources-and-setpoint-preparation-servo)
- [Motorized potentiometer](#motorized-potentiometer)
- [Fixed setpoints](#fixed-setpoints)
- [Speed setpoint](#speed-setpoint)
- [Speed limitation](#speed-limitation)
- [Ramp-function generator](#ramp-function-generator)
- [Extended stop and retract (ESR)](#extended-stop-and-retract-esr)

#### Setpoint sources and setpoint preparation (servo)

##### Overview of the setpoint sources

The setpoint channel forms the connecting element between the external interfaces and the actual motor control. Whereby the input signals are influenced from the point of view of the driven machine, e.g. disabling a direction, hiding certain frequencies, forming acceleration and deceleration ramps through to switchover between different setpoint and command sources.

Generally, different command sources result from the requirements to operate a drive from different locations (local/remote access), in different situations (normal/emergency operation) and/or in different operating modes.

The setpoint source is therefore the interface via which the converter receives its setpoint. The following options are available:

- Motorized potentiometer emulated in the converter
- Analog input of the converter
- Fixed setpoints stored in the converter
- Fieldbus interface of the converter

Depending on the parameter assignment, the setpoint in the converter has one of the following meanings:

- Speed setpoint for the motor
- Torque setpoint for the motor
- Setpoint for a process variable

  The converter receives a setpoint for a process variable, e.g. the level of a liquid container. The converter calculates the speed setpoint internally in the technology controller from this process variable.

##### Overview of the setpoint processing

The setpoint processing modifies the speed setpoint. For example, it limits the setpoint to a maximum and a minimum value and prevents speed jumps of the motor via the ramp-function generator.

- Minimum speed and maximum speed
- Ramp-function generator

##### Requirement

- The "Extended setpoint channel" function module is activated for drive objects of the type "highly dynamic (servo)" (see [Function modules (servo)](#function-modules-servo)).

  For drive objects of the type "universal (vector)", however, the functionality is always active.

##### Function diagrams (FD)

- Setpoint channel - Overview - 3001 -

#### Motorized potentiometer

This section contains information on the following topics:

- [Overview](#overview)
- [Motorized potentiometer](#motorized-potentiometer-1)
- [Ramp-function generator (motorized potentiometer)](#ramp-function-generator-motorized-potentiometer)

##### Overview

###### Description

The drive emulates an electromechanical motorized potentiometer. It is possible to switch over between manual and automatic operation for the setpoint specification. The specified setpoint is supplied to an internal ramp-function generator. Setting values and initial values, as well as braking with OFF1 do not require the ramp-function generator of the motorized potentiometer.

They change the motorized potentiometer (MOP) smoothly via the "Higher" and "Lower" control signals. The control signal can be switched via the digital inputs of the drive or via status words of telegrams. The longer the commands are present, the quicker the setpoint change.

###### Application cases

- Specification of the speed setpoint during the commissioning phase.
- Manual operation of the motor if the higher-level controller fails.
- Specification of the speed setpoint after switchover from automatic to manual mode.
- Applications with mainly constant setpoint without a higher-level controller.
- Interconnection as main or additional setpoint via r1050, see also [Application example: Using the main and additional setpoint](#application-example-using-the-main-and-additional-setpoint).

---

**See also**

[Motorized potentiometer](#motorized-potentiometer-1)

##### Motorized potentiometer

###### Description

The "Motorized potentiometer" function emulates an electromechanical potentiometer for the input of setpoints. The value of the motorized potentiometer is set via the "Setpoint higher" and "Setpoint lower" commands. This value is saved and can be interconnected as main setpoint or as additional setpoint. The "Motorized potentiometer" function can be selected when digital inputs of the operator panel or fieldbusses are used. The behavior of the motorized potentiometer depends on the duration of the "Setpoint higher" and "Setpoint lower" commands: The longer the commands are present, the quicker the setpoint change.

The function is intended for manual control of the drive or for automatic speed specification. The ramp-function generator of the motorized potentiometer can be switched off in automatic operation.

- With manual control, you manually specify the setpoint via a digital input, for example.
- In automatic operation, a higher-level controller specifies the setpoint, for example. You then interconnect the signal source via BICO.

###### Setting automatic operation or manual operation

1. Interconnect the "Manual/automatic" signal source ([p1041](SINAMICS%20Parameter%20SERVO.md#p10410n-bi-motorized-potentiometer-manualautomatic)) for switching from manual to automatic at the motorized potentiometer.

   In manual operation, the setpoint is set higher and lower via two signals.

   In automatic operation, the setpoint must be interconnected via a connector input.

###### Parameterizing the motorized potentiometer for manual operation

1. To specify limit values for the speed setpoint in manual operation, enter a maximum value ([p1037](SINAMICS%20Parameter%20SERVO.md#p10370n-motorized-potentiometer-maximum-velocity-1)) or minimum value ([p1038](SINAMICS%20Parameter%20SERVO.md#p10380n-motorized-potentiometer-minimum-velocity-1)).

   The "Maximum speed" or "Minimum speed" is not overshot or undershot when using the motorized potentiometer.
2. Interconnect the "Setpoint higher" signal source ([p1035](SINAMICS%20Parameter%20SERVO.md#p10350n-bi-motorized-potentiometer-setpoint-raise)) for a continuous increase of the setpoint at the motorized potentiometer.
3. Interconnect the "Setpoint lower" signal source ([p1036](SINAMICS%20Parameter%20SERVO.md#p10360n-bi-motorized-potentiometer-lower-setpoint)) for a continuous decrease of the setpoint at the motorized potentiometer.
4. Interconnect the "Inversion" signal source ([p1039](SINAMICS%20Parameter%20SERVO.md#p10390n-bi-motorized-potentiometer-inversion)) to invert the minimum speed/velocity or the maximum speed/velocity at the motorized potentiometer.
5. To parameterize the ramp-function generator, click the "Ramp-function generator" button.

   Specify the values for the ramp-function generator in the dialog of the same name (see [Ramp-function generator (motorized potentiometer)](#ramp-function-generator-motorized-potentiometer)).

###### Parameterizing the motorized potentiometer for automatic operation

1. Interconnect the "Automatic setpoint" signal source ([p1042](SINAMICS%20Parameter%20SERVO.md#p10420n-ci-motorized-potentiometer-automatic-setpoint)) for the setpoint of the motorized potentiometer during automatic operation.
2. In the "Automatic operation active" drop-down list ([p1030](SINAMICS%20Parameter%20SERVO.md#p10300n-motorized-potentiometer-configuration).1), select whether the ramp-function generator is to be active during Automatic operation.

   - [0] No = In this case, the "Ramp-function generator" button is deactivated.
   - [1] Yes = In this case, the ramp-function generator can be subsequently parameterized.
3. To parameterize the activated ramp-function generator, click the "Ramp-function generator" button.

   Specify the values for the ramp-function generator in the dialog of the same name. (See [Ramp-function generator (motorized potentiometer)](#ramp-function-generator-motorized-potentiometer)).

###### Saving the setpoint

The output of the motorized potentiometer [r1050](SINAMICS%20Parameter%20SERVO.md#r1050-co-motorized-potentiometer-setpoint-after-ramp-function-generator-1) is saved after OFF and the motorized potentiometer is set to the saved value after ON if p1030.0 = 1. The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint. With p1030.0 a decision is made as to whether the ramp-function generator of the motorized potentiometer is based on the motorized potentiometer output that was valid before the OFF command or on a start value specified by [p1040](SINAMICS%20Parameter%20SERVO.md#p10400n-motorized-potentiometer-starting-value-1). Parameter p1030.3 decides whether or not the setpoint is stored in a non-volatile memory.

For saving important data, the converter has an NVRAM (Non-Volatile Random Access Memory). The setpoint of the motorized potentiometer is stored in the non-volatile memory there. The value is re-loaded after POWER ON and specified as the start value after OFF1 enable.

1. Select the "[1] Yes" option in the "Save active" (p1030.0) drop-down list to save the setpoint in the volatile memory (not in the non-volatile memory).
2. Select the "[1] Yes" option in the "Non-volatile saving active" (p1030.3) drop-down list to save the setpoint in the non-volatile memory.

> **Note**
>
> Non-volatile saving is only possible when p1030.0 = 1 and p1030.3 = 1, that is, when the "[1] Yes" option is selected in both drop-down lists.

###### Function diagrams (FD)

Setpoint channel - Motorized potentiometer - 3020 -

Internal control/status words - Control word sequence control - 2501 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1045](SINAMICS%20Parameter%20SERVO.md#r1045-co-mot-potentiom-velocity-setp-in-front-of-ramp-fct-gen-1)
- r1050

---

##### Ramp-function generator (motorized potentiometer)

###### Description

The ramp-function generator (RFG) limits the acceleration at sudden setpoint changes and helps to avoid load surges in the entire drive train. An acceleration ramp and a deceleration ramp can be set independently with the ramp-up time and ramp-down time. This enables a controlled transition at setpoint changes.

In addition to the acceleration limitation, the "Ramp-function generator" screen form also displays the maximum motor speed, and in which speed range the motor operates.

> **Note**
>
> If the ramp-function generator of the motorized potentiometer is used, the actual [Ramp-function generator of the setpoint channel](#application-example-parameterizing-the-ramp-function-generator) is generally not used in addition.

###### Activate initial rounding

An initial rounding results in an S-shaped ramp which provides smooth transitions for acceleration and deceleration.

1. To connect a fixed specified rounding, select the "[1] Yes" entry in the "Initial rounding active" ([p1030](SINAMICS%20Parameter%20SERVO.md#p10300n-motorized-potentiometer-configuration).2) drop-down list.

   The set ramp-up or ramp-down time can be exceeded with the initial rounding.

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down time parameters, whereby these refer to the speed limit n_max.

1. Enter a value for the "Ramp-up time" ([p1047](SINAMICS%20Parameter%20SERVO.md#p10470n-motorized-potentiometer-ramp-up-time)).

   The lower the value, the faster the drive accelerates. The ramp-up time is extended accordingly with activated initial rounding (p1030.2).
2. Enter a value for the "Ramp-down time" ([p1048](SINAMICS%20Parameter%20SERVO.md#p10480n-motorized-potentiometer-ramp-down-time)).

   The lower the value, the faster the drive decelerates. The ramp-down time is extended accordingly with activated initial rounding (p1030.2).

> **Note**
>
> **Direction reversal**
>
> With direction reversal, the two times are added: With direction reversal, the ramp-down time is effective first and then the ramp-up time in the opposite direction.

###### Parameterizing the start value and the setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the motorized potentiometer setting value.

1. Interconnect the "Accept setting value" signal source ([p1043](SINAMICS%20Parameter%20SERVO.md#p10430n-bi-motorized-potentiometer-accept-setting-value)) to accept the setting value at the motorized potentiometer.
2. Interconnect the "Setting value" ([p1044](SINAMICS%20Parameter%20SERVO.md#p10440n-ci-motorized-potentiometer-setting-value)) signal source for the setting value at the motorized potentiometer.

   The setting value influences [r1050](SINAMICS%20Parameter%20SERVO.md#r1050-co-motorized-potentiometer-setpoint-after-ramp-function-generator-1) (motorized potentiometer setpoint after ramp-function generator).
3. Enter a start value for the motorized potentiometer in the "Start value" ([p1040](SINAMICS%20Parameter%20SERVO.md#p10400n-motorized-potentiometer-starting-value-1)) field.

   The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint.

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1))

  Display of the highest possible speed.

###### Function diagrams (FD)

Internal control/status words - Control word sequence control - 2501 -

Setpoint channel - Basic ramp-function generator - 3060 -

Setpoint channel - Extended ramp-function generator - 3070 -

Setpoint channel - Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- [r1045](SINAMICS%20Parameter%20SERVO.md#r1045-co-mot-potentiom-velocity-setp-in-front-of-ramp-fct-gen-1)
- r1050

---

#### Fixed setpoints

This section contains information on the following topics:

- [Fixed setpoints](#fixed-setpoints-1)
- [Fixed setpoint interconnection](#fixed-setpoint-interconnection)
- [Application example: Operating a drive with constant speed](#application-example-operating-a-drive-with-constant-speed)

##### Fixed setpoints

###### Description

This function allows you to specify preset speed/frequency setpoints. The fixed setpoints are defined in parameters and selected via binector inputs. For example, the digital inputs or the appropriate bits in the PROFINET telegrams can be used for the external control. The individual fixed setpoints and the effective fixed setpoint are each available via a connector output for further interconnection. Simple applications in which switchover is only to be between a few dedicated speeds, can be implemented with this function.

###### Procedure

These fixed setpoints are up to 15 freely stored speed setpoints which you can select via a bit pattern. If all the selected bits have low status, then the value 0 is specified as fixed setpoint.

1. Enter fixed speed setpoints 1...15 in the "Fixed value 1...15" ([p1001](SINAMICS%20Parameter%20SERVO.md#p10010n-co-fixed-velocity-setpoint-1-1)...[p1015](SINAMICS%20Parameter%20SERVO.md#p10150n-co-fixed-velocity-setpoint-15-1)) fields.
2. Then interconnect the signal sources for selecting the fixed velocity setpoint for the following bit fields

   - "Bit 0" ([p1020](SINAMICS%20Parameter%20SERVO.md#p10200n-bi-fixed-velocity-setpoint-selection-bit-0-1))
   - "Bit 1" ([p1021](SINAMICS%20Parameter%20SERVO.md#p10210n-bi-fixed-velocity-setpoint-selection-bit-1-1))
   - "Bit 2" ([p1022](SINAMICS%20Parameter%20SERVO.md#p10220n-bi-fixed-velocity-setpoint-selection-bit-2-1))
   - "Bit 3" ([p1023](SINAMICS%20Parameter%20SERVO.md#p10230n-bi-fixed-velocity-setpoint-selection-bit-3-1))

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1024](SINAMICS%20Parameter%20SERVO.md#r1024-co-fixed-velocity-setpoint-effective-1)

---

##### Fixed setpoint interconnection

###### Description

The fixed setpoints are interconnected via BICO technology. Several interconnections can be created for each fixed setpoint.

###### Procedure

1. Click the "Interconnections" button in the "Fixed setpoints" screen form.

   The "Fixed setpoint interconnection" dialog opens.
2. Enter fixed speed setpoints in the "Fixed value 1...15" ([p1001](SINAMICS%20Parameter%20SERVO.md#p10010n-co-fixed-velocity-setpoint-1-1)...[p1015](SINAMICS%20Parameter%20SERVO.md#p10150n-co-fixed-velocity-setpoint-15-1)) fields.
3. To set percentage values for the "Fixed value 1" or "2" ([p2900](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2900-co-fixed-value-1)...[p2901](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2901-co-fixed-value-2)), enter a value at "Fixed value 1" or "Fixed value 2". You can use the percentage fixed values, for example, as signal source for the scaling of the main or additional setpoint in the "Speed setpoint" screen form.
4. To enter a fixed torque value, enter a value at "Fixed value M" ([p2930](SINAMICS%20Parameter%20SERVO.md#p29300n-co-fixed-value-m-nm-1)).

   These values are used as signal source to interconnect the fixed speed to another BICO signal.
5. Interconnect the appropriate connector output to each recorded fixed setpoint (on the right of the associated fixed setpoint field).

   Several connections are also possible for each fixed setpoint.
6. Click "Close" to close the dialog.

###### Function diagrams (FD)

Setpoint channel - Overview - 3001 -

Setpoint channel - Fixed speed setpoints - 3010 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1024](SINAMICS%20Parameter%20SERVO.md#r1024-co-fixed-velocity-setpoint-effective-1)

---

##### Application example: Operating a drive with constant speed

###### Using constant speed (fixed speeds)

Use fixed speeds for simple applications in which the drive only has to turn at constant speed. The drive allows you to predefine up to 15 fixed speeds.

The defined fixed speeds are selected via binector inputs. The various speeds are controlled via digital inputs or via appropriate bits in PROFIdrive telegrams.

If you switch between different fixed speeds, the resulting speed setpoint is accelerated or decelerated via the acceleration ramp of deceleration ramp of the ramp-function generator. Therefore, check the ramp-up times and ramp-down times set in the ramp-function generator. The ramps are set to 10 seconds in the factory setting and can be changed. The OFF3 ramp is set to 0 seconds.

###### Sample applications

Simple applications in which switchover is between a few specified speeds, can be implemented with fixed speeds:

- Mixer with stepped mixing speed
- Conveyor belt with several speed stages
- Fixed setpoint as main or additional setpoint, see also [Speed setpoint](#speed-setpoint-1).

###### Procedure

You want to select fixed setpoint 6 and connect it to a BICO parameter in order to use it as a speed setpoint:

1. Enter a "1" for bit 1.
2. Enter a "2" for bit 1.

   This results in bit pattern "0110" with which you can select fixed value 6.
3. Enter a value for fixed value 6 ([p1006](SINAMICS%20Parameter%20SERVO.md#p10060n-co-fixed-velocity-setpoint-6-1)[6]).
4. Connect the output signal ([r1024](SINAMICS%20Parameter%20SERVO.md#r1024-co-fixed-velocity-setpoint-effective-1)). As default, r1024 is connected to the main setpoint at "Speed setpoint".

![Connecting fixed setpoints](images/147854993419_DV_resource.Stream@PNG-en-US.png)

Connecting fixed setpoints

###### Additional parameters

- [p1020](SINAMICS%20Parameter%20SERVO.md#p10200n-bi-fixed-velocity-setpoint-selection-bit-0-1)
- [p1021](SINAMICS%20Parameter%20SERVO.md#p10210n-bi-fixed-velocity-setpoint-selection-bit-1-1)
- [p1022](SINAMICS%20Parameter%20SERVO.md#p10220n-bi-fixed-velocity-setpoint-selection-bit-2-1)
- [p1023](SINAMICS%20Parameter%20SERVO.md#p10230n-bi-fixed-velocity-setpoint-selection-bit-3-1)
- ---

---

**See also**

[Fixed setpoints](#fixed-setpoints-1)
  
[Fixed setpoint interconnection](#fixed-setpoint-interconnection)

#### Speed setpoint

This section contains information on the following topics:

- [Speed setpoint](#speed-setpoint-1)
- [Application example: Using the main and additional setpoint](#application-example-using-the-main-and-additional-setpoint)

##### Speed setpoint

###### Description

The speed setpoint is the reference variable of the drive to be controlled. You also specify the speed of the drive via the size of the speed setpoint. There are numerous ways to influence the speed setpoint:

- Main setpoint (+ scaling)
- Additional setpoint (+ scaling)
- Jog
- Direction of rotation limitation and direction reversal
- Speed limit in the setpoint channel

###### Setting the main/additional setpoint and setpoint modification

The additional setpoint can be used to incorporate correction values from lower-level controllers. This can be easily carried out using the addition point of the main/additional setpoint in the setpoint channel. Both variables are imported via two separate sources and added in the setpoint channel. In contrast to the setpoint addition, the main and additional setpoints are added before the ramp-function generator. The added speed setpoint is then routed over the acceleration ramp of the ramp-function generator.

1. Connect the "Main setpoint" signal source ([p1070](SINAMICS%20Parameter%20SERVO.md#p10700n-ci-main-setpoint)) of the main setpoint.
2. Connect the "Scaling" signal source ([p1071](SINAMICS%20Parameter%20SERVO.md#p10710n-ci-main-setpoint-scaling)) for scaling the main setpoint.

   Example: Connect "Fixed value 1" at "Fixed setpoint interconnection" as signal source.
3. Connect the "Additional setpoint" signal source ([p1075](SINAMICS%20Parameter%20SERVO.md#p10750n-ci-supplementary-setp)) of the additional setpoint.
4. Connect the "Additional setpoint scaling" signal source ([p1076](SINAMICS%20Parameter%20SERVO.md#p10760n-ci-supplementary-setpoint-scaling)) for scaling the additional setpoint.

   Example: Connect "Fixed value 2" at "Fixed setpoint interconnection" as signal source.

###### Setting jog

"Jog" is oriented towards typical "finger tapping" with which you can traverse a motor through short taps.

When a jog signal is connected, the motor accelerates with the acceleration ramp of the ramp-function generator (in relation to the maximum speed [p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1); see figure) up to the jog setpoint. When the jog signal is deselected, shutdown is performed on the set ramp of the ramp-function generator.

![Jog 1 and Jog 2 flow diagram](images/147855032459_DV_resource.Stream@PNG-en-US.png)

Jog 1 and Jog 2 flow diagram

To traverse a motor via "Jog", e.g. a motor after a program interruption, enter speed setpoints in the following fields:

1. Enter a value for "Jog 1" ([p1058](SINAMICS%20Parameter%20SERVO.md#p10580n-jog-1-velocity-setpoint-1)).

   - and/or -
2. Enter a value for "Jog 2" ([p1059](SINAMICS%20Parameter%20SERVO.md#p10590n-jog-2-velocity-setpoint-1)).
3. Connect the signal sources for Jog 1 or Jog 2, and therefore enable the drive for "Jog":

   - "Jog bit 0" ([p1055](SINAMICS%20Parameter%20SERVO.md#p10550n-bi-jog-bit-0)); signal source for Jog 1
   - "Jog bit 1" ([p1056](SINAMICS%20Parameter%20SERVO.md#p10560n-bi-jog-bit-1)); signal source for Jog 2

   If you have connected both signal sources, the setpoint is maintained.

**Jog properties**

- If both Jog signals are set simultaneously, the momentary speed is maintained (constant speed phase).
- Jog setpoints are approached and left via the ramp-function generator.
- Jog is possible from the "Ready to start" state.
- If ON/OFF1 = "1" and Jog have been selected simultaneously, ON/OFF1 takes priority.  
  For this reason, ON/OFF1 = "1" must not be active for Jog to be activated.
- OFF2 and OFF3 take priority over Jog.
- The ON command is issued via p1055 and p1056.
- The Jog speed is defined via p1058 and p1059.
- The following applies during "Jog mode":

  - The main speed setpoints ([r1078](SINAMICS%20Parameter%20SERVO.md#r1078-co-total-setpoint-effective-1)) are disabled.
  - Additional setpoint 1 ([p1155](SINAMICS%20Parameter%20SERVO.md#p11550n-ci-speed-controller-speed-setpoint-1-1)) is disabled.
  - Additional setpoint 2 ([p1160](SINAMICS%20Parameter%20SERVO.md#p11600n-ci-speed-controller-speed-setpoint-2-1)) is passed on and added to the current speed.
- The skip frequency bands ([p1091](SINAMICS%20Parameter%20SERVO.md#p10910n-skip-velocity-1-1) ... [p1094](SINAMICS%20Parameter%20SERVO.md#p10940n-skip-velocity-4-1)) and the minimum limit ([p1080](SINAMICS%20Parameter%20SERVO.md#p10800n-minimum-velocity-1)) in the setpoint channel are also effective in Jog mode.
- The freezing of the ramp-function generator via [p1141](SINAMICS%20Parameter%20SERVO.md#p11410n-bi-continue-ramp-function-generatorfreeze-ramp-function-generator) is deactivated ([r0046](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0046029-cobo-missing-enable-signal).31 = 1) during Jog mode.

###### Setting the direction of rotation limitation and direction reversal

A direction reversal can be achieved in the setpoint channel by selecting the setpoint inversion ([p1113](SINAMICS%20Parameter%20SERVO.md#p11130n-bi-setpoint-inversion)). However, if the specification of a negative or positive setpoint via the setpoint channel is to be prevented, this can be disabled.

1. Connect the "Setpoint inversion" signal source (p1113) to set the reversal of the direction of rotation.
2. Connect the "Disable negative direction" signal source ([p1110](SINAMICS%20Parameter%20SERVO.md#p11100n-bi-inhibit-negative-direction)) to disable the negative direction of rotation.
3. Connect the "Disable positive direction" signal source ([p1111](SINAMICS%20Parameter%20SERVO.md#p11110n-bi-inhibit-positive-direction)) to disable the positive direction of rotation.

###### Setting the speed limit in the setpoint channel

To limit the speed in the setpoint channel, enter a value for the "Speed limit setpoint channel" ([p1063](SINAMICS%20Parameter%20SERVO.md#p10630n-setpoint-channel-velocity-limit-1)).

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855028235_DV_resource.Stream@PNG-en-US.png) | [Speed limitation](#speed-limitation-1) |

###### Function diagrams (FD)

Setpoint channel - Overview - 3001 -

Setpoint channel - Main setpoint / additional setpoint, setpoint scaling, jog - 3030 -

Setpoint channel - Direction limitation and direction reversal - 3040 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1)
- [r1114](SINAMICS%20Parameter%20SERVO.md#r1114-co-setpoint-after-the-direction-limiting-1)
- [r1073](SINAMICS%20Parameter%20SERVO.md#r1073-co-main-setpoint-effective-1)
- [r1077](SINAMICS%20Parameter%20SERVO.md#r1077-co-supplementary-setpoint-effective-1)
- r1078

---

##### Application example: Using the main and additional setpoint

###### Description

The additional setpoint can be used to incorporate correction values from lower-level controllers. This can be easily carried out using the addition point of the main/additional setpoint in the setpoint channel. Both variables are imported via two separate sources and added in the setpoint channel.

![Main and additional setpoint](images/147855063947_DV_resource.Stream@PNG-en-US.png)

Main and additional setpoint

In contrast to the [setpoint addition](#setpoint-addition-servo), the main and additional setpoints are added before the ramp-function generator. The sum of the main and additional setpoints is then routed through the setpoint channel over the acceleration ramp of the ramp-function generator. The update is performed in the sampling time of the setpoint channel ([p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)[3]) and not in the faster sampling time of the speed controller cycle.

###### Procedure

The resulting fixed speed setpoint [r1024](SINAMICS%20Parameter%20SERVO.md#r1024-co-fixed-velocity-setpoint-effective-1) is connected as default setting:

![Main and additional setpoint](images/147855074443_DV_resource.Stream@PNG-en-US.png)

Main and additional setpoint

1. If required, check and reconnect [p1070](SINAMICS%20Parameter%20SERVO.md#p10700n-ci-main-setpoint) to the signal source for the main setpoint.

   Connect [p1071](SINAMICS%20Parameter%20SERVO.md#p10710n-ci-main-setpoint-scaling) to the signal source for the scaling factor of the main setpoint.
2. Connect [p1075](SINAMICS%20Parameter%20SERVO.md#p10750n-ci-supplementary-setp) to the signal source for the additional setpoint.

   Connect [p1076](SINAMICS%20Parameter%20SERVO.md#p10760n-ci-supplementary-setpoint-scaling) to the signal source for the scaling factor of the additional setpoint.

###### Function diagrams (FD)

Setpoint channel - Overview - 3001 -

Setpoint channel - Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- p1070
- p1071
- [r1073](SINAMICS%20Parameter%20SERVO.md#r1073-co-main-setpoint-effective-1)
- p1075
- p1076
- [r1077](SINAMICS%20Parameter%20SERVO.md#r1077-co-supplementary-setpoint-effective-1)
- [r1078](SINAMICS%20Parameter%20SERVO.md#r1078-co-total-setpoint-effective-1)

---

#### Speed limitation

This section contains information on the following topics:

- [Speed limitation](#speed-limitation-1)
- [Application example: Parameterizing skip frequency bands and minimum limitation](#application-example-parameterizing-skip-frequency-bands-and-minimum-limitation)

##### Speed limitation

###### Description

The speed limitation is used to avoid damage to the connected machine. For example, reversing is not always possible and must be avoided. The speed setpoint limitation can disable the specification of a negative or positive setpoint via the setpoint channel. The maximum speed can also be limited for the connected machine.

In torque control, the sum of the two torque setpoints is limited in the same way as the torque setpoint of the speed control. Above the maximum speed, a speed limitation reduces the torque limits in order to prevent a further acceleration of the drive.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855119499_DV_resource.Stream@PNG-en-US.PNG) | [Speed setpoint](#speed-setpoint-1) |

###### Defining skip frequency bands

If a drive train has interfering points of resonance in the range from 0 rpm to the setpoint speed, you can define skip frequency bands for these points. Skip frequency bands are used, e.g. to prevent mechanical resonance effects. Resonances can cause unwanted mechanical vibrations. The skip frequency bands prevent continuous operation of the drive at these points of resonance. During ramp-up, the speed remains at the lower limit of a skip frequency band, and during ramp-down, the speed remains at the upper limit.

1. To define skip frequency bands, click the "Skip frequency bands" button.

   The "Skip frequency bands" dialog opens.
2. Enter values in the "Skip value 1 to 4" fields ([p1091](SINAMICS%20Parameter%20SERVO.md#p10910n-skip-velocity-1-1) to [p1094](SINAMICS%20Parameter%20SERVO.md#p10940n-skip-velocity-4-1)) in order to define up to four skip frequency bands.
3. Enter a value for the skip frequency band ([p1101](SINAMICS%20Parameter%20SERVO.md#p11010n-skip-velocity-bandwidth-1)) in the "Bandwidth" field. You can only define one identical bandwidth for all four skip frequency bands.

   If you enter "0" as value, no skip frequency bands are taken into account - irrespective of which values you have defined for the "Skip values 1 to 4" (p1091 to p1094).
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

   You have defined valid skip frequency bands when the "Skip frequency bands" button appears as follows:

   ![Defining skip frequency bands](images/147855111563_DV_resource.Stream@PNG-en-US.png)

   ![Defining skip frequency bands](images/147855111563_DV_resource.Stream@PNG-en-US.png)

###### Defining the minimum limitation

A minimum limitation is approached after the pulse enable.

1. To enter a minimum value for the speed setpoint, click the "Minimum limitation" button.

   The "Minimum limitation" dialog opens.
2. Enter a value for the lower limit of the speed setpoint at "Minimum speed" ([p1080](SINAMICS%20Parameter%20SERVO.md#p10800n-minimum-velocity-1)).

   - Or -

   Interconnect the "Minimum speed signal source" signal source ([p1106](SINAMICS%20Parameter%20SERVO.md#p11060n-ci-minimum-velocity-signal-source-1)) for the lowest possible speed of the motor.
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

   You have defined a valid minimum limitation when the "Minimum limitation" button appears as follows:

   ![Defining the minimum limitation](images/147855115531_DV_resource.Stream@PNG-en-US.png)

   ![Defining the minimum limitation](images/147855115531_DV_resource.Stream@PNG-en-US.png)

###### Defining the maximum limitation

1. To enter a maximum value for the speed setpoint, click the "Maximum limitation" button.

   The "Maximum limitation" dialog opens.
2. Interconnect the speed limitations for the following directions of rotation:

   - "Speed limit, positive direction of rotation" ([p1051](SINAMICS%20Parameter%20SERVO.md#p10510n-ci-velocity-limit-rfg-positive-direction-1))

     This speed limitation goes directly into the ramp-function generator.
   - "Speed limit negative direction of rotation" ([p1052](SINAMICS%20Parameter%20SERVO.md#p10520n-ci-velocity-limit-rfg-negative-direction-1))

     This speed limitation goes directly into the ramp-function generator.
3. Make the following settings for the "Speed limit positive effective" ([r1084](SINAMICS%20Parameter%20SERVO.md#r1084-co-speed-limit-positive-effective-1)) here:

   - "pos. variable speed limit" ([p1085](SINAMICS%20Parameter%20SERVO.md#p10850n-ci-velocity-limit-positive-direction-1))

     Interconnect the signal source of a variable speed limitation in the positive direction of rotation.
   - "Positive speed limit" ([p1083](SINAMICS%20Parameter%20SERVO.md#p10830n-co-speed-limit-in-positive-direction-of-rotation-1))

     Enter the maximum speed for the positive direction.
   - "Maximum speed" ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1))

     Enter a value for the highest possible positive speed. The inverted value is used as the lowest possible value.

   The lowest of the three values in p1082, p1083 and p1085 is used as the "Speed limit positive effective" (r1084).
4. Make the following settings for the "Speed limit negative effective" ([p1086](SINAMICS%20Parameter%20SERVO.md#p10860n-co-speed-limit-in-negative-direction-of-rotation-1)) here:

   - "negative speed limit" (p1086)

     Enter the maximum speed for the positive direction.
   - "neg. variable speed limit" (p1052)

     Interconnect the signal source of a variable speed limitation in the negative direction of rotation.

   The lowest of the three values in p1082, p1086 and [p1088](SINAMICS%20Parameter%20SERVO.md#p10880n-ci-velocity-limit-negative-direction-1) is used as the "Speed limit positive effective" ([r1087](SINAMICS%20Parameter%20SERVO.md#r1087-co-speed-limit-negative-effective-1)).

   The setpoint of the ramp-function generator for diagnostic and control purposes is displayed in "CO: ramp-function generator setpoint at the input" ([r1119](SINAMICS%20Parameter%20SERVO.md#r1119-co-ramp-function-generator-setpoint-at-the-input-1)).
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855123723_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator-1) |

###### Function diagrams (FD)

Setpoint channel - Overview - 3001 -

Setpoint channel - Skip frequency bands and speed limits - 3050 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1112](SINAMICS%20Parameter%20SERVO.md#r1112-co-velocity-setpoint-after-minimum-limiting-1)
- [r1114](SINAMICS%20Parameter%20SERVO.md#r1114-co-setpoint-after-the-direction-limiting-1)
- r1119

---

##### Application example: Parameterizing skip frequency bands and minimum limitation

###### Setting up skip frequency bands and minimum limitation

If a drive train has interfering points of resonance in the range from 0 rpm to the setpoint speed, you can define skip frequency bands for these points. The drive crosses the set skip frequency bands on the acceleration/deceleration ramp, but continuous operation in the set skip frequency bands is not possible.

- Reduction of resonant frequencies in mechanical systems, e.g. in pipes and ventilation ducts.

  - Reduced material fatigue
  - Reduced noise levels

###### Determining the points of resonance

You can use the trace technology of the TIA Portal to determine the points of resonance. You may also have noticed a speed range during commissioning in which resonance occurred.

1. Open the trace and select "Configuration &gt; Signals".
2. Select the actual speed value ([r0062](SINAMICS%20Parameter%20SERVO.md#r0062-co-speed-setpoint-after-the-filter-1)) as the signal to be recorded.

   ![Trace with signal r62](images/147855147915_DV_resource.Stream@PNG-en-US.png)

   Trace with signal r62
3. Go online and load the trace configuration to the drive.
4. Specify the speed via the drive control panel.
5. If you find a speed range with resonance, increase or decrease the speed until you have located the resonance point. In this way, you also obtain the speed range in which the resonance occurs.

###### Parameterizing skip frequency bands

To parameterize the skip frequency bands, proceed as follows:

1. Open the "Speed limitation" mask in the secondary navigation and click the "Skip frequency bands" button.

   ![Skip frequency bands](images/147855152011_DV_resource.Stream@PNG-en-US.png)

   Skip frequency bands
2. Enter the determined value for the skip frequency band ([p1091](SINAMICS%20Parameter%20SERVO.md#p10910n-skip-velocity-1-1)).
3. Enter a value for the bandwidth ([p1101](SINAMICS%20Parameter%20SERVO.md#p11010n-skip-velocity-bandwidth-1)), e.g. +/- 15 rpm.
4. In this way, define all additional skip frequency bands and close the dialog with "Close".

###### Minimum limitation

The minimum limitation depends on the requirements of your application or your process. An example of this is a conventional pump application in which a specific delivery rate must be maintained. Accordingly, the motor speed must not fall below the minimum speed.

In addition to the fixed set limit, it is also possible to dynamically influence these limits during operation with the connectors, in order, for example, to be able to adapt the machine for different processing materials.

1. Open the "Speed limitation" mask in the secondary navigation and click the "Minimum limitation" button.

   ![Minimum limitation](images/147855156107_DV_resource.Stream@PNG-en-US.png)

   Minimum limitation
2. Enter a value for the minimum motor speed ([p1080](SINAMICS%20Parameter%20SERVO.md#p10800n-minimum-velocity-1)).

   or
3. Connect a signal for the minimum motor speed ([p1006](SINAMICS%20Parameter%20SERVO.md#p10060n-co-fixed-velocity-setpoint-6-1)).
4. Close the dialog with "Close".

###### Additional parameters

---

---

**See also**

[Speed limitation](#speed-limitation-1)

#### Ramp-function generator

This section contains information on the following topics:

- [Ramp-function generator](#ramp-function-generator-1)
- [Basic ramp-function generator](#basic-ramp-function-generator)
- [Extended ramp-function generator](#extended-ramp-function-generator)
- [Application example: Parameterizing the ramp-function generator](#application-example-parameterizing-the-ramp-function-generator)

##### Ramp-function generator

###### Description

The ramp-function generator is used to limit the acceleration at sudden setpoint changes. The setting of the ramp-function generator parameters depends on your application and the construction of your machine.

- [Basic ramp-function generator](#basic-ramp-function-generator)

  The basic ramp-function generator passes on the input values to the output via linear ramps. The speed setpoint is accelerated or decelerated linearly.
- [Extended ramp-function generator](#extended-ramp-function-generator)

  With the extended ramp-function generator, acceleration and deceleration are not linear. Rounding can be parameterized at the start and end of the range via a selected rounding type.

An acceleration ramp and a deceleration ramp can be set independently with the ramp-up time and ramp-down time. This enables a controlled transition at setpoint changes.

If the drive is in the range of the torque limits or the drive is temporarily not controlled via the ramp-function generator, then the actual speed value moves away from the speed setpoint.

With ramp-function generator tracking, the speed setpoint follows the actual speed value and therefore flattens the ramp. The ramp-function generator tracking can be activated for the basic and the extended ramp-function generator.

> **Note**
>
> If a [Motorized potentiometer with ramp-function generator](#ramp-function-generator-motorized-potentiometer) is used in the setpoint channel, the ramp-function generator described below is usually superfluous.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855028235_DV_resource.Stream@PNG-en-US.png) | [Speed limitation](#speed-limitation-1) |

###### Making the basic settings for the ramp-function generator

1. Select in the "Ramp-function generator selection" drop-down list whether a basic ramp-function generator or an extended ramp-function generator is to be used.

   The ramp-function generator type is shown as subentry in the secondary navigation:
2. Interconnect the signal source for enabling the frequency setpoint in the "Enable setpoint" ([p1142](SINAMICS%20Parameter%20SERVO.md#p11420n-bi-enable-setpointinhibit-setpoint)) field.
3. Interconnect the signal source to start the ramp-function generator in the "Start ramp-function generator" ([p1141](SINAMICS%20Parameter%20SERVO.md#p11410n-bi-continue-ramp-function-generatorfreeze-ramp-function-generator)) field.
4. Click the "Ramp-function generator" button or select the appropriate screen form via the secondary navigation.
5. Make the additional settings for the selected ramp-function generator type.

   - [Basic ramp-function generator](#basic-ramp-function-generator)
   - [Extended ramp-function generator](#extended-ramp-function-generator)
6. Interconnect the signal source in the "Enable ramp-function generator" ([p1140](SINAMICS%20Parameter%20SERVO.md#p11400n-bi-enable-ramp-function-generatorinhibit-ramp-function-generator)) field to enable the ramp-function generator.
7. Save the settings.

###### Required enables

Various enables are required to operate the ramp-function generator.

- "OFF1 enable" and "OFF3 enable" are set via the control word "Sequential control system". Check the individual bits of the control word at "Diagnostics &gt; Control/status words". Check the interconnection at "Diagnostics &gt; Interconnections".

  The control inputs of the ramp-function generator take effect as follows:

  - 1st priority: OFF3
  - 2nd priority: Ramp-function generator enable
  - 3rd priority: Ramp-function generator start
  - 4th priority: Setpoint enable

The following internal enables are required ([r0046](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0046029-cobo-missing-enable-signal)):

- "OFF1 enable internal missing" (r0046[16])

  Shows whether a fault response is present at OFF1. The enable is made only when the fault has been corrected and acknowledged, and the switching on disabled removed with OFF1 = 0.
- "OFF3 enable internal missing" (r0046[18])

  Shows whether an OFF3 has not yet been completed or an OFF3 fault response is present.
- "STOP2 enable internal missing" (r0046[18])

  Shows whether a STOP2 fault response is present.
- "Operation enable missing" (r0046[3])

  Shows that the signal source in [p0852](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08520n-bi-enable-operationinhibit-operation) is a 0 signal.

###### Bypassing the ramp-function generator

If you do not want to use the ramp-function generator for a certain time, you can bypass it.

1. In this case, interconnect the signal source in the "Bypass ramp-function generator" ([p1122](SINAMICS%20Parameter%20SERVO.md#p11220n-bi-bypass-ramp-function-generator)) field.

###### Enabling the ramp-function generator

To enable the ramp-function generator, proceed as follows:

1. Interconnect the signal source in the "Enable ramp-function generator" (p1140) field to enable the ramp-function generator.

###### Ramp-function generator active

The ramp-function generator only becomes active when the settings described above have been made and the enables according to the logical operations are present.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855195787_DV_resource.Stream@PNG-en-US.png) | [Setpoint addition](#setpoint-addition-servo) |

###### Function diagrams (FD)

Setpoint channel - Basic ramp-function generator - 3060 -

Setpoint channel - Extended ramp-function generator - 3070 -

Setpoint channel - Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1119](SINAMICS%20Parameter%20SERVO.md#r1119-co-ramp-function-generator-setpoint-at-the-input-1)
- p1122
- p1140
- [r1150](SINAMICS%20Parameter%20SERVO.md#r1150-co-ramp-function-generator-velocity-setpoint-at-the-output-1)
- [r1198](SINAMICS%20Parameter%20SERVO.md#r1198015-cobo-control-word-setpoint-channel)

---

##### Basic ramp-function generator

###### Description

With the basic ramp-function generator, the input values are passed on to the output via linear ramps, i.e. there is no rounding at the start and end of the range; the drive is accelerated or decelerated linearly.

![Basic ramp-function generator](images/147855220363_DV_resource.Stream@PNG-en-US.png)

Basic ramp-function generator

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855123723_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator-1) |

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down times, whereby these refer to the speed limit n<sub>max</sub>.

1. Correct the specified ramp-up time ([p1047](SINAMICS%20Parameter%20SERVO.md#p10470n-motorized-potentiometer-ramp-up-time)) from standstill to maximum speed.
2. Interconnect the signal source for scaling the ramp-up time of the ramp-function generator in the "Scaling factor" ([p1138](SINAMICS%20Parameter%20SERVO.md#p11380n-ci-ramp-function-generator-ramp-up-time-scaling)) field.
3. Correct the specified ramp-down time ([p1048](SINAMICS%20Parameter%20SERVO.md#p10480n-motorized-potentiometer-ramp-down-time)) from maximum speed to standstill.
4. Interconnect the signal source for scaling the ramp-down time of the ramp-function generator in the "Scaling factor" ([p1139](SINAMICS%20Parameter%20SERVO.md#p11390n-ci-ramp-function-generator-ramp-down-time-scaling)) field.
5. Correct the specified value for the OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)).

   The OFF3 ramp-down time is the ramp-down time that may elapse from maximum speed down to standstill for the OFF3 command.

###### Setting the setting value

Setting values are the values to which the ramp-function generator jumps automatically.

| Symbol | Meaning |
| --- | --- |
| 1. Interconnect the signal source to accept the setting value in the "Accept setting value" ([p1143](SINAMICS%20Parameter%20SERVO.md#p11430n-bi-ramp-function-generator-accept-setting-value)) field.     The ramp-function generator behaves as follows depending on the values of parameter p1143:       | Symbol | Meaning |    | --- | --- |    | 0/1 signal | The output of the ramp-function generator is set to the setting value of the ramp-function generator without delay. |    | 1 signal | The setting value of the ramp-function generator takes effect. |    | 1/0 signal | The input value of the ramp-function generator takes effect. The output of the ramp-function generator is adapted to the input value via the ramp-up time or the ramp-down time. |    | 0 signal | The input value of the ramp-function generator takes effect. | 2. Interconnect the signal source for the setting value on the ramp-function generator in the "Setting value" ([p1144](SINAMICS%20Parameter%20SERVO.md#p11440n-ci-ramp-function-generator-setting-value)) field. |  |

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1))

  Display of the highest possible speed. The value for the maximum speed comes from the speed limitation.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855123723_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator-1) |

###### Function diagrams (FD)

Setpoint channel - Basic ramp-function generator - 3060 -

###### Additional parameters

---

---

**See also**

[Application example: Parameterizing the ramp-function generator](#application-example-parameterizing-the-ramp-function-generator)

##### Extended ramp-function generator

###### Description

With the extended ramp-function generator, acceleration and deceleration are not linear. The acceleration can be described by a ramp for a set rounding. Without rounding, the acceleration jumps to the value specified by the ramp-up or ramp-down time.

![Extended ramp-function generator](images/147855258379_DV_resource.Stream@PNG-en-US.png)

Extended ramp-function generator

The "Effective ramp-up/ramp-down time" is calculated according to the following formula:

- Effective ramp-up time = ramp-up time + initial rounding/2 + final rounding/2
- Effective ramp-down time = ramp-down time + initial rounding/2 + final rounding/2

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855123723_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator-1) |

###### Entering rounding parameters

1. Enter a value for the "Initial rounding 1" or 2 ([p1130](SINAMICS%20Parameter%20SERVO.md#p11300n-ramp-function-generator-initial-rounding-off-time)).

   The value applies for ramp-up and ramp-down.
2. Enter a value for the "Final rounding 1" or 2 ([p1131](SINAMICS%20Parameter%20SERVO.md#p11310n-ramp-function-generator-final-rounding-off-time)).

   The value applies for ramp-up and ramp-down.

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down times, whereby these refer to the speed limit n<sub>max</sub>.

1. Correct the specified ramp-up time ([p1047](SINAMICS%20Parameter%20SERVO.md#p10470n-motorized-potentiometer-ramp-up-time)) from standstill to maximum speed.
2. Interconnect the signal source for scaling the ramp-up time of the ramp-function generator in the "Scaling factor" ([p1138](SINAMICS%20Parameter%20SERVO.md#p11380n-ci-ramp-function-generator-ramp-up-time-scaling)) field.
3. Correct the specified ramp-down time ([p1048](SINAMICS%20Parameter%20SERVO.md#p10480n-motorized-potentiometer-ramp-down-time)) from maximum speed to standstill.
4. Interconnect the signal source for scaling the ramp-down time of the ramp-function generator in the "Scaling factor" ([p1139](SINAMICS%20Parameter%20SERVO.md#p11390n-ci-ramp-function-generator-ramp-down-time-scaling)) field.
5. Select the "[1] Yes" setting in the "Enable rounding at the zero crossover" drop-down list to enable the rounding at the zero crossover.

###### Setting the setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the ramp-function generator setting value.

| Symbol | Meaning |
| --- | --- |
| 1. Interconnect the signal source to accept the setting value in the "Accept setting value" ([p1143](SINAMICS%20Parameter%20SERVO.md#p11430n-bi-ramp-function-generator-accept-setting-value)) field.     The ramp-function generator behaves as follows depending on the values of parameter p1143:       | Symbol | Meaning |    | --- | --- |    | 0/1 signal | The output of the ramp-function generator is set to the setting value of the ramp-function generator without delay. |    | 1 signal | The setting value of the ramp-function generator takes effect. |    | 1/0 signal | The input value of the ramp-function generator takes effect. The output of the ramp-function generator is adapted to the input value via the ramp-up time or the ramp-down time. |    | 0 signal | The input value of the ramp-function generator takes effect. | 2. Interconnect the signal source for the setting value on the ramp-function generator in the "Setting value" ([p1144](SINAMICS%20Parameter%20SERVO.md#p11440n-ci-ramp-function-generator-setting-value)) field. |  |

###### Setting OFF3-relevant parameters

When an OFF3 occurs, the drive is braked along the OFF3 deceleration ramp.

1. To specify a rounding type, select one of the following options from the drop-down list:

   - "Continuous smoothing" ([p1134](SINAMICS%20Parameter%20SERVO.md#p11340n-ramp-function-generator-rounding-off-type) = 0)

     With this setting the rounding is always active, i.e. when setpoint changes occur, they only take effect after the final rounding has been completed. This can result in overshoot.
   - "Discontinuous smoothing" (p1134 = 1)

     A change in the setpoint causes a final rounding to be aborted. This prevents an overshoot. However, this can result in abrupt changes of the velocity/acceleration (jerk).
2. Correct the specified value for the OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)).

   The value describes the ramp-down time from maximum speed to standstill with OFF3.
3. Enter a value for the "OFF3 initial rounding time" ([p1136](SINAMICS%20Parameter%20SERVO.md#p11360n-off3-initial-rounding-off-time)).
4. Enter a value for the "OFF3 final rounding time" ([p1137](SINAMICS%20Parameter%20SERVO.md#p11370n-off3-final-rounding-off-time)).

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1))

  Display of the highest possible speed. The value for the maximum speed comes from the speed limitation.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855123723_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator-1) |

###### Function diagrams (FD)

Setpoint channel - Extended ramp-function generator - 3070 -

###### Additional parameters

- p1143

---

---

**See also**

[Application example: Parameterizing the ramp-function generator](#application-example-parameterizing-the-ramp-function-generator)

##### Application example: Parameterizing the ramp-function generator

###### Basic ramp-function generator or extended ramp-function generator

The ramp-function generator is used to limit the acceleration at sudden setpoint changes. The setting of the ramp-function generator parameters depends on your application and the construction of your machine.

- [Extended ramp-function generator](#extended-ramp-function-generator)

  The extended ramp-function generator limits the acceleration and jerk. This prevents torque jerks at the transitions (constant velocity phase ←→ acceleration/deceleration phase). This is of particular importance for applications (e.g. transport of liquids or lifting gear) that require very "smooth", jerk-free acceleration or deceleration operations.
- [Basic ramp-function generator](#basic-ramp-function-generator)

  The basic ramp-function generator limits the acceleration, but not the change in acceleration (jerk).

If the ramp-up time of the machine is specified via a higher-level controller, the ramp-up time in the drive should be set significantly shorter or maximum the same, in order to avoid delays or overtravel.

If the drive has been dimensioned too small for dynamic ramp-ups, then the ramp-up time should be set so that the drive does not come into overcurrent during acceleration.

###### Parameterizing the ramp-up time and ramp-down time for the extended ramp-function generator

Parameterizing the roundings for the ramp-up time and ramp-down time lengthens the ramp-up time and the ramp-down time; see also [Ramp-function generator](#ramp-function-generator-1). The default setting for the ramp-up time and ramp-down time is 10 s.

![Parameterizing the extended ramp-function generator](images/147855286923_DV_resource.Stream@PNG-en-US.png)

Parameterizing the extended ramp-function generator

1. Enter a value for the ramp-up time ([p1120](SINAMICS%20Parameter%20SERVO.md#p11200n-ramp-function-generator-ramp-up-time-1)).
2. Enter a value for the initial rounding ([p1130](SINAMICS%20Parameter%20SERVO.md#p11300n-ramp-function-generator-initial-rounding-off-time)). The value is also taken for the deceleration ramp.
3. Enter a value for the final rounding ([p1131](SINAMICS%20Parameter%20SERVO.md#p11310n-ramp-function-generator-final-rounding-off-time)). The value is also taken for the deceleration ramp.
4. Enter a value for the ramp-down time ([p1121](SINAMICS%20Parameter%20SERVO.md#p11210n-ramp-function-generator-ramp-down-time-2)). The factory setting of 10 s is more suitable for larger drives. If you use highly dynamic servo drives, you should adapt this value, i.e. set a shorter time.

The effective ramp-up and ramp-down times are calculated from the entered values.

###### Setting the zero point rounding

The zero point rounding is used for a soft change of direction of rotation, whereby the change also takes longer however. If the change of direction of rotation is to be performed as fast as possible, disable the zero point rounding. Note however that this can result in shocks in the mechanical system if the ramp-up time is set greater than the ramp-down time.

![Zero point rounding](images/147855291275_DV_resource.Stream@PNG-en-US.png)

Zero point rounding

- Select "Yes" in the "Disable rounding at the zero crossover" ([p1151](SINAMICS%20Parameter%20SERVO.md#p11510n-ramp-function-generator-configuration)) drop-down list:

###### Parameterizing OFF3

There is a special ramp which can be set via [p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1) for a quick stop (OFF3) (e.g. for a quick controlled shutdown after pressing the emergency stop pushbutton). The OFF3 ramp-down time sets the ramp time from maximum speed down to standstill for the OFF3 command.

1. Enter a value for the OFF3 ramp-down time (p1135). If you do not parameterize a time here, maximum braking is applied on the drive. (??)
2. Enter a value for the "OFF3 initial rounding time" ([p1136](SINAMICS%20Parameter%20SERVO.md#p11360n-off3-initial-rounding-off-time)).
3. Enter a value for the "OFF3 final rounding time" ([p1137](SINAMICS%20Parameter%20SERVO.md#p11370n-off3-final-rounding-off-time)).

###### Setting the rounding type for setpoint reduction and OFF1

You can set how the setpoint change is to be performed for a setpoint change or for an OFF1 command:

- ②
  [p1134](SINAMICS%20Parameter%20SERVO.md#p11340n-ramp-function-generator-rounding-off-type) = "0": Continuous smoothing; rounding is always active. Overshoot can occur. At a setpoint change, the final rounding is performed first and then travel in the direction of the new setpoint.
- ① p1134 = "1": Discontinuous smoothing; at a setpoint change, travel is immediately in the direction of the new setpoint.

  ![Smoothing type](images/147855295371_DV_resource.Stream@PNG-en-US.png)

  Smoothing type

###### Function diagrams (FD)

Setpoint channel - Extended ramp-function generator - 3070 -

###### Additional parameters

- [p1143](SINAMICS%20Parameter%20SERVO.md#p11430n-bi-ramp-function-generator-accept-setting-value)

---

---

**See also**

[Ramp-function generator (motorized potentiometer)](#ramp-function-generator-motorized-potentiometer)

#### Extended stop and retract (ESR)

This section contains information on the following topics:

- [Overview](#overview-1)
- [Setting the ESR responses](#setting-the-esr-responses)
- [Sources for triggering the ESR function](#sources-for-triggering-the-esr-function)
- [PROFIdrive telegram for ESR](#profidrive-telegram-for-esr)

##### Overview

The "Extended stop and retract" (ESR) function allows a workpiece and tool to be separated without causing any damage when a fault situation occurs. The drive axes involved are defined and are retracted and/or stopped in a controlled fashion.

The following drive-autonomous ESR functions are possible:

- [Extended stopping](#extended-stopping) of the drive
- [Extended retraction](#extended-retract) of the drive
- [Generator operation](#regenerative-operation) with monitoring to buffer the DC-link voltage

ESR functions can be initiated from the higher-level controller using a trigger signal, or independently in the drives themselves in the event of a fault (the function is integrated in the drive). The ESR functions integrated in the drive act on an axis-for-axis basis.

- Using an axis-specific trigger, ESR functions are directly initiated for an individual axis.
- Using a local trigger on the device itself, the ESR functions are simultaneously initiated for those axes under the drive line that are activated for ESR.

> **Note**
>
> **ESR functionality under Safety Integrated Functions**
>
> If extended stop and retract are to be activated simultaneously with Safety Integrated Functions, the following conditions must also be satisfied. Further information can be found in the SINAMICS S120 Function Manual Safety Integrated.

###### Requirements

- The "Extended stop and retract" function module has been activated.
- The "highly dynamic (servo)" drive object type is used.

###### Example

For a machine tool, several drives are simultaneously operational, e.g. a workpiece drive and various feed drives for a tool. In the case of a fault, it is not permissible that the tool remains inserted in the workpiece. This could make both unusable. The tool and workpiece must be separated from one another in a controlled fashion before the drives are allowed to come to a standstill.

The "Extended stop and retract" function module allows drive-integrated retraction using the feed drives with subsequent stopping. This means, for example when the line supply fails, a drive can be switched into the generator mode. This then supplies energy for the DC link so that the feed drives can retract the tool from the workpiece and then be subsequently stopped.

###### Restrictions

- Operating several axes in generator mode

  Only use one speed-controlled axis to buffer the DC link. If you have parameterized several axes, faults can occur, which undesirably influence one another and therefore also the drive line-up.
- Unsuitable motors for generator operation

  Linear motors (1FN) and torque motors (1FW) require an adequately high DC-link voltage for braking. They are not suitable to buffer the DC link when operating in generator mode.
- ESR and Safety Integrated

  If the Safety Integrated Extended Functions are controlled via PROFIsafe, in the case of a communication failure, Safety Integrated only permits a response time (p9580/p9380) of maximum 800 ms. After this time expires, Safety Integrated requests pulse suppression.

##### Setting the ESR responses

This section contains information on the following topics:

- [Extended stopping](#extended-stopping)
- [Extended retract](#extended-retract)
- [Regenerative operation](#regenerative-operation)

###### Extended stopping

With the extended stop, the drive is to be stopped in a defined way when an error occurs. The stopping method is used as long as the drive is still capable of functioning. The function is parameterized and operates on an axis-specific basis. Axes are not coupled.

![OFF ramp with timer](images/147855365131_DV_resource.Stream@PNG-en-US.png)

OFF ramp with timer

###### Procedure

1. Select the "Extended stop, n_set" ([p0888](SINAMICS%20Parameter%20SERVO.md#p0888-esr-configuration) = 1) or "Extended stop, n_act" (p0888 = 4) option in the "Configuration" drop-down list.
2. Click the "ESR function" button.

   A setting dialog opens for the option set in step 1.
3. Select the desired OFF ramp in the "OFF ramp" ([p0891](SINAMICS%20Parameter%20SERVO.md#p0891-esr-off-ramp)) drop-down list.

   The display in the dialog is adapted
4. Enter the time in the "Timer" ([p0892](SINAMICS%20Parameter%20SERVO.md#p0892-esr-timer)) field for which the last setpoint from [r1438](SINAMICS%20Parameter%20SERVO.md#r1438-co-speed-controller-speed-setpoint-1) or the last actual value from [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1) is frozen before braking is initiated.
5. Click "Close" to close the dialog.
6. Interconnect the "Response enable" ([p0889](SINAMICS%20Parameter%20SERVO.md#p0889-bi-esr-response-enable)) signal source to enable the response.
7. If required, also interconnect the signal sink for the status word ([r0887](SINAMICS%20Parameter%20SERVO.md#r0887013-bo-esr-status-word)).
8. To correct the interconnection of the ESR trigger, click the "Trigger" button.

   The "ESR trigger" dialog box opens.
9. Change the interconnection of the individual trigger signal sources and click "Close" to close the dialog.
10. Save these settings in the project.
11. Load these ESR settings to your drive units.

###### Function diagrams (FD)

Setpoint channel - Extended Stop and Retract (ESR, r0108.9 = 1) - 3082 -

###### Additional parameters

- [p0890](SINAMICS%20Parameter%20SERVO.md#p089004-bi-esr-trigger)

---

###### Extended retract

With the extended retraction, the drive is to be traversed to a retraction position when an error occurs. The retraction method is used as long as the drive is still capable of functioning. The function is parameterized and operates on an axis-specific basis. Interpolating coupling of the axes is not realized.

![DC-link voltage setpoint](images/147855392139_DV_resource.Stream@PNG-en-US.png)

DC-link voltage setpoint

###### Procedure

1. Select the "Extended retraction" ([p0888](SINAMICS%20Parameter%20SERVO.md#p0888-esr-configuration) = 2) option in the "Configuration" drop-down list.
2. Click the "ESR function" button.

   A setting dialog opens for the option set in step 1.
3. Select the desired OFF ramp in the "OFF ramp" ([p0891](SINAMICS%20Parameter%20SERVO.md#p0891-esr-off-ramp)) drop-down list.

   The display in the dialog is adapted
4. Enter the time in the "Timer" ([p0892](SINAMICS%20Parameter%20SERVO.md#p0892-esr-timer)) field for which the retraction speed should be applied.
5. Enter the retraction speed in the "ESR speed" [p0893](SINAMICS%20Parameter%20SERVO.md#p0893-esr-velocity-1) field.
6. Click "Close" to close the dialog.
7. Interconnect the "Response enable" ([p0889](SINAMICS%20Parameter%20SERVO.md#p0889-bi-esr-response-enable)) signal source to enable the response.
8. If required, also interconnect the signal sink for the status word ([r0887](SINAMICS%20Parameter%20SERVO.md#r0887013-bo-esr-status-word)).
9. To correct the interconnection of the ESR trigger, click the "Trigger" button.

   The "ESR trigger" dialog box opens.
10. Change the interconnection of the individual trigger signal sources and click "Close" to close the dialog.
11. Save these settings in the project.
12. Load these ESR settings to your drive units.

**Result**

The retraction speed is not approached suddenly. It is approached via the OFF3 ramp.

Parameter p0893 supplies the ramp-function generator with the setpoint for the ESR retraction speed which is actuated by an OFF3 ramp in the case of drive-autonomous motions. The safety setpoint velocity limiting [p1051](SINAMICS%20Parameter%20SERVO.md#p10510n-ci-velocity-limit-rfg-positive-direction-1)/[p1052](SINAMICS%20Parameter%20SERVO.md#p10520n-ci-velocity-limit-rfg-negative-direction-1) and the normal velocity limits [r1084](SINAMICS%20Parameter%20SERVO.md#r1084-co-speed-limit-positive-effective-1)/[r1087](SINAMICS%20Parameter%20SERVO.md#r1087-co-speed-limit-negative-effective-1) are active.

![Connecting the setpoint channel to the ramp-function generator](images/147855397259_DV_resource.Stream@PNG-en-US.png)

Connecting the setpoint channel to the ramp-function generator

###### Function diagrams (FD)

Setpoint channel - Extended Stop and Retract (ESR, r0108.9 = 1) - 3082 -

###### Additional parameters

- [p0890](SINAMICS%20Parameter%20SERVO.md#p089004-bi-esr-trigger)

---

###### Regenerative operation

With the ESR response "Generator operation", the DC link is buffered when an error occurs until all of the drives connected to the DC link and enabled by ESR have reached their configured final position. To achieve this, a suitable drive in the drive line-up, for example a spindle drive, is braked in generator operation. The DC-link voltage is then monitored by the V<sub>dc_min</sub> controller.

![DC-link voltage setpoint](images/147855423627_DV_resource.Stream@PNG-en-US.png)

DC-link voltage setpoint

###### Procedure

1. Select the "Generator operation (Vdc controller)" ([p0888](SINAMICS%20Parameter%20SERVO.md#p0888-esr-configuration) = 3) option in the "Configuration" drop-down list.
2. Click the "ESR function" button.

   The "Generator operation (Vdc controller)" dialog box opens.
3. Select the desired option in the "Vdc controller or Vdc monitoring configuration" drop-down list.
4. Click "Close" to close the dialog.
5. Interconnect the "Response enable" ([p0889](SINAMICS%20Parameter%20SERVO.md#p0889-bi-esr-response-enable)) signal source to enable the response.
6. If required, also interconnect the signal sink for the status word ([r0887](SINAMICS%20Parameter%20SERVO.md#r0887013-bo-esr-status-word)).
7. To correct the interconnection of the ESR trigger, click the "Trigger" button.

   The "ESR trigger" dialog box opens.
8. Change the interconnection of the individual trigger signal sources and click "Close" to close the dialog.
9. Save these settings in the project.
10. Load these ESR settings to your drive units.

###### Function diagrams (FD)

Setpoint channel - Extended Stop and Retract (ESR, r0108.9 = 1) - 3082 -

###### Additional parameters

- [p0890](SINAMICS%20Parameter%20SERVO.md#p089004-bi-esr-trigger)

---

##### Sources for triggering the ESR function

###### Invalid sources

The following DRIVE-CLiQ communication failures do not initiate an ESR trigger:

- Pulse suppression of the Motor Modules is present  
  The drive switches to OFF2 and coasts to a standstill.
- Failure of encoder modules as motor measuring system  
  The system is switched to operation without encoder and a parameterized stop response is initiated.
- Failure of encoder modules as a direct application-specific measuring system  
  The application is shut down and a parameterized stop response is initiated.

###### Valid sources: Triggering for all drives of a Control Unit

Conditions for triggering the function:

- ESR function has been configured in the drive, e.g. stopping or retraction.
- ESR function has been enabled in the drive.
- The pulse enable has been set.

**A distinction is made between the following error sources:**

- Communication failure:

  - The Control Unit detects the communication failure and triggers autonomous reactions in all the enabled drives.
  - A status checkback signal is no longer possible.
  - The higher-level control removes the "Master control by PLC" signal (F07220).
  - Interruption of the data transmission via the fieldbus (F01910 or F08501).
- External trigger signal

  - An external trigger signal from the control triggers the ESR function via the telegrams 390, 391 or 392.

###### Valid sources: Axis-related trigger sources

Conditions for triggering the function:

- ESR function has been configured in the drive with p0888, e.g. stopping or retraction.
- ESR function has been enabled in the drive with p0889 = 1.
- The pulse enable has been set.

**A distinction is made between the following error sources:**

- Internal drive fault

  - Faults with response OFF1 or OFF3
  - p0840 (On/OFF1) and p0849 (OFF3) wired to terminal
- Internal trigger signal

  - The source for the ESR trigger signal is set via BICO with p0890.

##### PROFIdrive telegram for ESR

A cyclic bit for CU_STW1 is present in PROFIdrive DO telegrams 390, 391, 392, 393, 394, 395 and 396 to monitor the ESR state.

CU_STW1

| Signal | Meaning | Interconnection parameters |
| --- | --- | --- |
| CU_STW1.2 | ESR trigger | p0890.9 = r2090.2 |

Cyclic bits for STW1 and MELDW are present in the telegrams.

STW1

| Signal | Meaning | Interconnection parameters |
| --- | --- | --- |
| STW1.9 | 1 = Enable ESR response | p0889 = r2090.9 |

MELDW

| Signal | Meaning | Interconnection parameters |
| --- | --- | --- |
| MELDW.2 | 1 = |n_act| &lt; speed threshold value 3 (p2161) | p2082[2] = r2199.0 |
| MELDW.4 | 1 = Vdc_min controller active (V<sub>dc</sub>&lt;p1248) | p2082[4] = r0056.15 |
| MELDW.9 | 1 = ESR response initiated / generator operation active | p2082[9] = r0887.12 |

### Open-loop/closed-loop control

This section contains information on the following topics:

- [Setpoint addition](#setpoint-addition)
- [Speed precontrol](#speed-precontrol)
- [Speed setpoint filter](#speed-setpoint-filter)
- [Speed controller](#speed-controller)
- [U/f control](#uf-control)
- [Torque setpoints](#torque-setpoints)
- [Supplementary torques](#supplementary-torques)
- [Torque limiting](#torque-limiting)
- [Current setpoint filter](#current-setpoint-filter)
- [Current controller](#current-controller)
- [Power unit](#power-unit)
- [Motor encoder](#motor-encoder)

#### Setpoint addition

This section contains information on the following topics:

- [Setpoint addition (servo)](#setpoint-addition-servo)
- [Deceleration ramp (servo)](#deceleration-ramp-servo)
- [Application example: Position controller or controller as setpoint source](#application-example-position-controller-or-controller-as-setpoint-source)

##### Setpoint addition (servo)

###### Description

The setpoint addition allows the use of up to two speed setpoints.

The actual speed values of a higher-level position control system are suitable as source, which can be specified via a PROFIdrive telegram.

You can set the following properties in the Setpoint addition screen form:

- Interconnection of further speed setpoints to the main setpoint.
- Activation of interpolators
- Definition of a deceleration ramp if you have not activated the "Extended setpoint channel".
- Display of the speed controller clock ([p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions).1)

If the speed controller and the source of the output signals run in different time slices (output signal has a slower sampling rate), you can activate interpolators. The activated interpolator causes a finer grading of the speed setpoints coming from the ramp-function generator or a controller by calculating intermediate steps (interpolation).

A detailed description can be found at [Application example: Position controller or controller as setpoint source](#application-example-position-controller-or-controller-as-setpoint-source).

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855123723_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator)   Only when the "Extended setpoint channel" function module is not activated. |

###### Connecting additional speed setpoints

The speed setpoints are added. A higher-level controller, for example, can be used as source for the speed setpoint.

1. Interconnect the signal source for speed setpoint 1 of the speed controller in the "Speed setpoint 1" ([p1155](SINAMICS%20Parameter%20SERVO.md#p11550n-ci-speed-controller-speed-setpoint-1-1)) field.

   If the "Extended setpoint channel" function module is not activated, the setpoint source is interconnected directly to speed setpoint 1 (e.g. from the higher-level controller of from the technology controller).
2. Interconnect the signal source for speed setpoint 2 of the speed controller in the "Speed setpoint 2" ([p1160](SINAMICS%20Parameter%20SERVO.md#p11600n-ci-speed-controller-speed-setpoint-2-1)) field.
3. If the interpolation should be activated, select the "[1] Yes" option ([p1189](SINAMICS%20Parameter%20SERVO.md#p11890n-speed-setpoint-configuration-1)[0].1) in the drop-down list below the "Interpolation" button.

   The interpolator is activated.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147782215179_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#speed-setpoint-filter-servo) |

###### Function diagrams (FD)

Setpoint channel - Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- [r0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1)
- [r1169](SINAMICS%20Parameter%20SERVO.md#r1169-co-speed-controller-speed-setpoints-1-and-2-1)
- [r1170](SINAMICS%20Parameter%20SERVO.md#r1170-co-speed-controller-setpoint-sum-1)

---

---

**See also**

[Deceleration ramp (servo)](#deceleration-ramp-servo)

##### Deceleration ramp (servo)

###### Description

You can parameterize the "Ramp-down time" and the "OFF3 ramp-down time" via the deceleration ramp. You can also parameterize both parameters in the extended setpoint channel in the ramp-function generator screen form.

###### Requirement

- The "Extended setpoint channel" function module is NOT activated.

###### Parameterizing the deceleration ramp

1. Click the "Deceleration ramp" button.

   The dialog with the same name opens.
2. Correct in the "Ramp-down time" ([p1121](SINAMICS%20Parameter%20SERVO.md#p11210n-ramp-function-generator-ramp-down-time-2)) field the specified ramp-down time of the ramp-function generator.

   The ramp-down time for the ramp-function generator always refers to the maximum speed set in [p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1) and specifies the time the drive should require to decelerate from maximum speed down to standstill (setpoint = 0). The ramp-down time is always effective for OFF1.
3. Specify in the "Ramp-down time OFF3" ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)) field the ramp-down time.

   There is a special ramp which can be set via p1135 for a quick stop (OFF3) (e.g. for a quick controlled shutdown after pressing the emergency stop pushbutton). The OFF3 ramp-down time sets the ramp time from maximum speed down to standstill for the OFF3 command.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.
5. If a higher resolution of the speed setpoints is required, select the "[1] Yes" option ([p1189](SINAMICS%20Parameter%20SERVO.md#p11890n-speed-setpoint-configuration-1)[0].0) in the drop-down list below the "Interpolation" button.

   The interpolator is activated.

###### Function diagrams (FD)

Setpoint channel - Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

---

---

**See also**

[Application example: Position controller or controller as setpoint source](#application-example-position-controller-or-controller-as-setpoint-source)

##### Application example: Position controller or controller as setpoint source

###### Setpoint addition

The setpoint addition allows up to two speed setpoints to be combined. Whereas the use of main and additional setpoints in the setpoint channel is affected by speed limitations and ramp-function generators, the speed setpoint acts directly here. This eliminates the ramp-ups and ramp-downs of a ramp-function generator

Through setpoint addition, an additional speed setpoint can minimize disturbances to the speed setpoint coming from the position controller.

![Setpoint addition](images/147855517195_DV_resource.Stream@PNG-en-US.png)

Setpoint addition

###### Speed setpoint 1 from the controller

The speed setpoints of a higher-level position controller are suitable as a source, which can be specified in a PROFIdrive telegram. If you select a telegram for communication between drive and controller, speed setpoint 1 is automatically locked, and used for transferring the speed setpoint from the controller (NSOLL_A or NSOLL_B). The speed setpoint is then updated in the bus cycle, e.g. in the PROFINET cycle. The two enables (ramp-function generator enable and setpoint enable) can be assigned via STW1 in the telegram.

###### Speed setpoint 2 from EPOS, fixed setpoints or technology controller

Further possible connections are available for speed setpoint 2.

- If you activate the EPOS function module, the output of the position controller ([r2562](SINAMICS%20Parameter%20SERVO.md#r2562-co-lr-velocity-setpoint-total-1)) is automatically connected with speed setpoint 2. Further possible connections are:
- Output signal of the technology controller ([r2294](SINAMICS%20Parameter%20SERVO.md#r2294-co-technology-controller-output-signal))
- Fixed setpoints from the setpoint channel.

###### Interpolating speed setpoint values

If a speed setpoint from a higher-level controller is used, the speed setpoints are only updated in the bus cycle. The bus cycle is usually considerably slower than the current controller cycle of the SINAMICS drive, which can lead to steps. When an interpolator is used, the speed setpoint is interpolated linearly between the bus cycles, so that any steps that occur are eliminated from the calculation. Further sources of setpoints may be the setpoint channel, (setpoint channel cycle), EPOS or the technology controller, which also do not run in the fast speed controller cycle.

The interpolator automatically detects the cycle in which the signal is to be interpolated.

The interpolator is active only if the "Basic positioner" function module or isochronous PROFIdrive mode are active.

###### Function diagrams (FD)

Setpoint channel - Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- [r0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1)
- [r1169](SINAMICS%20Parameter%20SERVO.md#r1169-co-speed-controller-speed-setpoints-1-and-2-1)
- [r1170](SINAMICS%20Parameter%20SERVO.md#r1170-co-speed-controller-setpoint-sum-1)

---

---

**See also**

[Setpoint addition (servo)](#setpoint-addition-servo)
  
[Deceleration ramp (servo)](#deceleration-ramp-servo)

#### Speed precontrol

This section contains information on the following topics:

- [Speed precontrol (servo)](#speed-precontrol-servo)
- [Dynamic Servo Control (DSC) (servo)](#dynamic-servo-control-dsc-servo)
- [DSC with splines (servo)](#dsc-with-splines-servo)
- [Application example: Speed precontrol](#application-example-speed-precontrol)

##### Speed precontrol (servo)

###### Description

The precontrol relieves the speed controller during acceleration and prevents overshoot.

The interpolator is used to linearly interpolate the setpoints in the grid of the speed controller clock. This avoids strong excitations caused by large steps in the speed setpoint.

Detailed descriptions can be found at [Application example: Speed precontrol](#application-example-speed-precontrol).

###### Parameterizing the speed precontrol

1. Interconnect the signal source in the "Speed precontrol" ([p1430](SINAMICS%20Parameter%20SERVO.md#p14300n-ci-speed-precontrol-1)) field for the speed precontrol.
2. Select the "[1] Yes" option ([p1400](SINAMICS%20Parameter%20SERVO.md#p14000n-speed-control-configuration-3).7) in the drop-down list below the "Interpolation" button.

   The interpolator is activated and causes a finer grading of the interconnected speed precontrol value by calculating intermediate steps (interpolation).
3. Select via which signal path the precontrol value should be processed in the "Speed precontrol" (p1400) drop-down list:

   - "[1] For balancing";

     With this setting, the value for the speed precontrol is passed on directly to the speed controller via the precontrol balancing (see Parameterizing the precontrol balancing).
   - "[2] For setpoint filter 2";

     With this setting, the value goes directly to the speed setpoint filter.
4. If you have selected the "[1] For balancing" option, you must now parameterize the precontrol balancing so that the speed controller does not counteract the applied torque setpoint.

   Click the "Precontrol balancing" button.

   The dialog with the same name opens.
5. Make the following settings:

   - "Dead time factor" ([p1428](SINAMICS%20Parameter%20SERVO.md#p14280n-speed-precontrol-symmetrizing-dead-time-1))

     Enter the dead time for the precontrol balancing.
   - "Time constant " ([p1429](SINAMICS%20Parameter%20SERVO.md#p14290n-speed-precontrol-symmetrizing-time-constant-1))

     Enter the time constant (PT1) for the balancing of the speed setpoint for active torque precontrol.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

**Note**

Both factors mutually affect the speed precontrol value. Therefore, perform an optimization with a technology trace.

**Note**

The set value for the dead time is calculated with the speed controller clock.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855522443_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#speed-controller-servo) |
| ![Signal processing](images/147782215179_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#speed-setpoint-filter-servo) |
| ![Signal processing](images/147782215179_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#speed-setpoint-filter-servo) |

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

Servo control - Speed controller, torque-speed precontrol with encoder (p1402.4 = 1) - 5042 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1432](SINAMICS%20Parameter%20SERVO.md#r143201-co-speed-precontrol-1)

---

---

**See also**

[Dynamic Servo Control (DSC) (servo)](#dynamic-servo-control-dsc-servo)

##### Dynamic Servo Control (DSC) (servo)

###### Description

The "Dynamic Servo Control" (DSC) function is a closed-loop control structure which is calculated in the fast speed controller clock and supplied with setpoints from the controller in the position controller clock. DSC enables high position controller gains and therefore a low following error and high immunity.

The DSC (Dynamic Servo Control) function significantly improves the dynamic response and the stiffness of the position control loop: DSC minimizes the dead times that normally occur with speed setpoint interfaces by means of an additional, relatively simple feedback network in the drive. The position control loop is closed in the drive which enables very fast position control clocks (e.g. 125 μs for the SINAMICS S120). Dead times are reduced exclusively to the response to setpoint changes.

###### Requirements

The following requirements must be satisfied in order to use the "Dynamic Servo Control" function:

- n-set operating mode
- Isochronous PROFINET IO with IRT
- The position controller gain factor (KPC) and the position deviation (XERR) must be contained in the setpoint telegram (see [p0922](SINAMICS%20Parameter%20CU.md#p0922-if1-profidrive-pzd-telegram-selection-2)).
- The actual position value must be transferred to the master via the encoder interface Gx_XIST1 in the actual value telegram.
- The speed setpoint N_SOLL_B from the PROFIdrive telegram is used as the active speed precontrol value when DSC is active.
- The internal quasi-position controller, DSC position controller (FD-5030), uses the actual position value G1_XIST1 from the motor measuring system or the actual position value from an additional encoder system (telegrams 6, 106, 116, 118, 136 and 138 or free telegrams).

**The following PROFIdrive telegrams support DSC:**

- Standard telegrams 5 and 6
- SIEMENS telegrams 105, 106, 116, 118, 125, 126, 136, 138, 139

Further PZDs can be used via the telegram extension. Note that SERVO supports maximum 20 PZD setpoints and 28 PZD actual values.

> **Note**
>
> Isochronous mode is essential on the controller and on the drive side for the operation of DSC.

A detailed representation of the DSC operating principle can be found in function diagram Setpoint channel - Dynamic Servo Control (DSC) linear and DSC spline (r0108.6 = 1) - 3090 -  
.

###### Parameterizing Dynamic Servo Control

1. Click the "Dynamic Servo Control (DSC)" button in the function view of the "Speed precontrol" screen form.

   The "Dynamic Servo Control (DSC)" dialog opens.
2. Interconnect the signal source from which the position deviation XERR is to be read (position controller output of the higher-level controller) in the "Position deviation XERR" ([p1190](SINAMICS%20Parameter%20SERVO.md#p1190-ci-dsc-position-deviation-xerr)) field.
3. Select in the "Encoder selection" ([p1192](SINAMICS%20Parameter%20SERVO.md#p11920n-dsc-encoder-selection)) drop-down list the encoder (encoder 1 .. encoder 3) that you want to use.
4. Enter a factor for the encoder adaptation when using encoder 2 or 3 in the "Encoder adaptation factor" ([p1193](SINAMICS%20Parameter%20SERVO.md#p11930n-dsc-encoder-adaptation-factor)) field.

   The factor represents the ratio of the pulse difference between the motor encoder and the selected encoder for the same distance moved. The factor takes into account gear ratios, differences in the number of pulses, etc.
5. Interconnect the signal source from which the position gain "KPC" is to be read in the "Position controller gain KPC" ([p1191](SINAMICS%20Parameter%20SERVO.md#p1191-ci-dsc-position-controller-gain-kpc)) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Display parameters

The "Encoder actual position value GX_XIST1...3" ([r0482](SINAMICS%20Parameter%20SERVO.md#r048202-co-encoder-actual-position-value-gn_xist1)) field shows the encoder actual position values of encoders 1...3.

###### Function diagrams (FD)

Setpoint channel - Dynamic Servo Control (DSC) linear and DSC spline (r0108.6 = 1) - 3090 -

###### Additional parameters

- r0482

---

##### DSC with splines (servo)

A splines interpolation achieves the following improvements for the Dynamic Servo Control:

- A finer interpolation of the torque in the speed controller clock and therefore softer motion; torque surges are also avoided.
- Excellent path accuracy for torque speed precontrol (i.e. lower following error in the control behavior).
- High-frequency path motion is possible.

DSC operating modes comparison

| Operating mode for DSC | Meaning |
| --- | --- |
| Speed/torque precontrol with linear interpolation (namely, without splines) | As a result of the step-like torque precontrol in the position control clock, a pulsed torque characteristic is obtained with the excitation clock. |
| Speed precontrol with splines | - The position setpoint is balanced. - The speed precontrol value is not balanced. |
| Speed/torque precontrol with splines | - The position setpoint is balanced. - The speed precontrol value is balanced. - The torque precontrol value is not balanced. |

###### Requirements

- The "DCS with splines" function module is activated (see "[Function modules (servo)](#function-modules-servo)").
- DSC with splines can be used only for drives of type "highly dynamic (servo)".

###### Procedure

1. Click the "Dynamic Servo Control (DSC)" button in the function view of the "Speed precontrol" screen form.

   The "Dynamic Servo Control (DSC)" details screen form opens.
2. Interconnect the signal source for the balancing time constant T_SYMM for DSC with spline in the "Balancing time constant T_SYMM" (p1195) field.
3. Interconnect the signal source for the speed precontrol channel in the "Speed precontrol" (p1430) field.
4. Interconnect the signal source from which the position deviation XERR is to be read (position controller output of the higher-level controller) in the "Position deviation XERR" (p1190) field.
5. Select in the "Encoder selection" (p1192) drop-down list the encoder (encoder 1 .. encoder 3) that you want to use.
6. Enter a factor for the encoder adaptation when using encoder 2 or 3 in the "Encoder adaptation factor" (p1193) field.

   The factor represents the ratio of the pulse difference between the motor encoder and the selected encoder for the same distance moved. The factor takes into account gear ratios, differences in the number of pulses, etc.
7. Interconnect the signal source from which the position gain "KPC" is to be read in the "Position gain KPC" (p1191) field.

##### Application example: Speed precontrol

###### Speed-torque precontrol via the controller or position controller

You use this speed-torque precontrol in conjunction with a higher-level controller or position controller (e.g. EPOS).

With a higher-level controller, such as for a positioning axis, a path profile is generated in which the speed and acceleration are known. In the case of a setpoint step change, the controller can calculate a precontrol value for the speed of the drive corresponding to the setpoint curve. To do this, you must either calculate the values for the load torque in the controller or transfer the values of a rotating measurement ([p1498](SINAMICS%20Parameter%20SERVO.md#p14980n-load-moment-of-inertia-1)) to the controller.

The speed controller in the drive then only has to compensate for the remaining disturbance variable components. The controller transfers the value via fieldbus to the drive in a telegram.

If you use EPOS, you can connect parameter [r2561](SINAMICS%20Parameter%20SERVO.md#r2561-co-lr-velocity-precontrol-value-1) (value of the speed precontrol of the position controller) to the input of the speed precontrol ([p1430](SINAMICS%20Parameter%20SERVO.md#p14300n-ci-speed-precontrol-1)).

The following options are available for configuring the speed precontrol value ([p1400](SINAMICS%20Parameter%20SERVO.md#p14000n-speed-control-configuration-3)).

- "For balancing": Select this setting if you want to enter a dead time for the speed precontrol value.
- "For setpoint filter 2". Select this setting if you do not need a dead time for the speed precontrol value. The value is forwarded to the speed setpoint filter, where you can smooth the signal with filters. This setting is also compatible with the old SIMODRIVE 611U drive.

> **Note**
>
> **First parameterize and optimize the lower-level controllers**
>
> Before you parameterize the speed precontrol, it is recommended to first parameterize the current controller and the speed controller, because parameterizing the speed precontrol can have retroactive effects on other parameters, such as the torque precontrol.

> **Note**
>
> **Torque precontrol in the speed controller active**
>
> If the torque precontrol in the speed controller is active, set the precontrol balancing in the "Precontrol" mask in the speed controller.

###### Interpolating speed precontrol

Precontrol values can be interpolated in a similar way to speed setpoints from the controller, see also [Application example: Position controller or controller as setpoint source](#application-example-position-controller-or-controller-as-setpoint-source).

###### Parameterizing the precontrol balancing

The precontrol balancing serves to prevent unwanted controller motions until the precontrol is activated. The precontrol balancing is implemented as a PT1 element. For this purpose, parameterize the following parameters:

- "Dead time factor" ([p1428](SINAMICS%20Parameter%20SERVO.md#p14280n-speed-precontrol-symmetrizing-dead-time-1)): With active torque precontrol, the speed precontrol must be delayed until the torque precontrol has acted, and the new actual speed value is available. The "new" setpoint should not arrive until the current actual value of the speed controller is known. If torque precontrol is not possible (e.g. the moment of inertia J of the drive is not known), the speed precontrol value does not have to be delayed.

  Set initially the "Dead time factor" to "2" and view the result in the trace (see below).

  The entered value is multiplied by the sampling time of the speed controller ([p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)[1]). If the value "2" does not suffice, the signal can be further delayed via the time constant ([p1429](SINAMICS%20Parameter%20SERVO.md#p14290n-speed-precontrol-symmetrizing-time-constant-1)).
- "Time constant" (p1429): The time constant specifies the course of the rise of the signal. You specify the rate of increase of the speed setpoint with this time constant.

###### Adjusting "Dead time factor" and "Time constant"

Both the "Dead time factor" and the "Time constant" parameter affect the speed precontrol value reciprocally. You therefore have to perform the optimization via the technology trace. A position controller (EPOS) with two encoders (encoder 1 and encoder 2) is used as an example system. Record the signals of the following parameters:

- [r0061](SINAMICS%20Parameter%20SERVO.md#r006101-co-actual-speed-unsmoothed-1)[0] (Actual unsmoothed speed value), encoder 1 (red)
- r0061[1] (Actual unsmoothed speed value), encoder 2 (dark blue)
- r2561; Position controller speed precontrol value (light blue)

The position controller speed precontrol value is adjusted via the precontrol balancing so that, if possible, the actual speed value has no overshoot or following error. Therefore, change the "Dead time factor" and "Time constant" until the result is satisfactory, as the next speed precontrol value does not become available until after approximately 2 speed controller cycles.

![Precontrol balancing](images/147855583115_DV_resource.Stream@PNG-en-US.png)

Precontrol balancing

###### Signal path

The signal of the speed precontrol is fed into the signal path in accordance with the reference model. The signal path is not visible in the mask; look up the characteristic in the FD 5020 function diagram.

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

Servo control - Reference model / precontrol balancing / speed limitation - 5030 -

###### Additional parameters

---

---

**See also**

[Speed precontrol (servo)](#speed-precontrol-servo)
  
[Dynamic Servo Control (DSC) (servo)](#dynamic-servo-control-dsc-servo)

#### Speed setpoint filter

This section contains information on the following topics:

- [Speed setpoint filter (servo)](#speed-setpoint-filter-servo)
- [Application example: Use speed setpoint filter](#application-example-use-speed-setpoint-filter)

##### Speed setpoint filter (servo)

###### Description

The speed setpoint filters are used to skip or weaken certain frequency ranges.

> **Note**
>
> The speed setpoint filters have no effect on the stability of the speed controller because they are in the setpoint channel.
>
> The dynamic response in the response to setpoint changes is reduced by smoothing.

For the speed precontrol, a speed/velocity setpoint is also applied either via setpoint filter 2 or directly at the input of the speed controller. The speed precontrol can improve the response to setpoint changes of a higher-level control loop (e.g. position control).

Up to two identical speed setpoint filters can be set for a servo drive.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855195787_DV_resource.Stream@PNG-en-US.png) | [Setpoint addition](#setpoint-addition-servo) |
| ![Signal source](images/147855627275_DV_resource.Stream@PNG-en-US.png) | [Speed precontrol](#speed-precontrol-servo) |
| ![Signal source](images/147855627275_DV_resource.Stream@PNG-en-US.png) | [Speed precontrol](#speed-precontrol-servo) |

###### Activating and setting speed setpoint filters

1. Click the button of a speed setpoint filter in the screen form.

   The "Speed setpoint filter" setting dialog then opens. Activate here the required speed setpoint filters and make the settings required for each filter.
2. Enter the P gain for the speed setpoint filter in the "P gain" ([p1460](SINAMICS%20Parameter%20SERVO.md#p14600n-speed-controller-p-gain-adaptation-speed-lower-1)) field.
3. Enter the integral time for the speed setpoint filter in the "Integral time" ([p1462](SINAMICS%20Parameter%20SERVO.md#p14620n-speed-controller-integral-time-adaptation-speed-lower-1)) field.
4. At Settings in the "Filter type" ([p1415](SINAMICS%20Parameter%20SERVO.md#p14150n-speed-setpoint-filter-1-type-1)) drop-down list, select one of the following filter types for the 1st speed setpoint filter (see also [Filters](Configuring%20SINAMICS%20S-G-MV%20drives.md#filters)):

   - [Low-pass PT1](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-the-pt1-filter)
   - [Low-pass PT2](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-pt2-filter)
   - [Bandstop](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-bandstop-filter)
   - [Low-pass with reduction](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-low-pass-filter-with-reduction)
   - [General 2nd order filter](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-general-2nd-order-filter)
5. Correct the following default values appropriate for the filter type:

   - Time constant, only for filter type "Low-pass PT1"
   - Numerator frequency, only for filter type "General 2nd order filter"
   - Numerator damping, only for filter type "General 2nd order filter"
   - Denominator frequency, for filter type "Low-pass PT2" and "General 2nd order filter"
   - Denominator damping, for filter type "Low-pass PT2" and "General 2nd order filter"
   - Blocking frequency, only for filter type "Bandstop"
   - Bandwidth, only for filter type "Bandstop"
   - Notch depth, only for filter type "Bandstop"
   - Reduction, only for filter type "Bandstop" and "Low-pass with reduction"
   - Characteristic frequency, only for filter type "Low-pass with reduction"
   - Damping, only for filter type "Low-pass with reduction"
6. Click "Accept" to take your filter settings into the current configuration.

   The filter is displayed in the current configuration.
7. To switch on the parameterized filter, activate the "Filter effective" option.

   The filter is activated in the screen form.
8. If a 2nd speed setpoint filter is to be used, repeat steps 4 ... 7.
9. Once all necessary settings have been made, click "Close".

   The setting dialog closes. The screen form now displays a curve for all speed setpoint filters not activated previously rather than a straight line. This indicates which speed setpoint filters are activated and parameterized.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855522443_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#speed-controller-servo) |

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

###### Additional parameters

- [r0060](SINAMICS%20Parameter%20SERVO.md#r0060-co-speed-setpoint-before-the-setpoint-filter-1)
- [r0062](SINAMICS%20Parameter%20SERVO.md#r0062-co-speed-setpoint-after-the-filter-1)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1170](SINAMICS%20Parameter%20SERVO.md#r1170-co-speed-controller-setpoint-sum-1)
- [r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1)

---

---

**See also**

[Application example: Use speed setpoint filter](#application-example-use-speed-setpoint-filter)

##### Application example: Use speed setpoint filter

###### Speed setpoint filter

The speed setpoint filter processes speed setpoints coming from the position controller (EPOS) or a higher-level controller. The filter is normally used if resonances might still occur in the control loop despite the current setpoint filter. Therefore, first optimize the current controller with current setpoint filters.

Speed setpoint filter 2 is deployed when you are working without precontrol balancing and want to delay the speed setpoint signal or set a low pass filter. For information on filters, see also [Overview](Configuring%20SINAMICS%20S-G-MV%20drives.md#overview-1).

Other filters are bandstop filters and PT2 filters.

The following filters are available for selection:

- Low pass: PT1; for PT1 filters, the phase changes earlier. According to the characteristic frequency, the signal is dampened with -20 dB.

  Consequently, the PT1 filter is better to filter out low frequencies.
- Low pass: PT2; for a PT2 filter, the phase changes later and consequently the characteristic frequency is reached faster. According to the characteristic frequency, the signal is dampened with -40 dB.

  PT2 filters are better to filter out high frequency signals.
- General 2nd order filter The general 2nd order filter allows the implementation of bandstop filters or a low-pass with reduction.

A maximum of two speed setpoint filters can be parameterized and activated ([p1414](SINAMICS%20Parameter%20SERVO.md#p14140n-speed-setpoint-filter-activation-1)).

###### Use PT1 filter

The PT1 filter is deployed when precontrol balancing without time constant should be used, see also [Application example: Speed precontrol](#application-example-speed-precontrol).

1. Enter a value for the time constant ([p1415](SINAMICS%20Parameter%20SERVO.md#p14150n-speed-setpoint-filter-1-type-1)).
2. In the technology trace, trace the relevant signals, such as actual speed value and actual position value.
3. Change the value until the delay time is appropriate for the speed control value.

###### PT2 filter

The "Numerator frequency" and "Numerator attenuation" parameters have no effect on the filter. Set the following parameters for a PT2 filter:

1. Enter a value for the denominator frequency ([p1417](SINAMICS%20Parameter%20SERVO.md#p14170n-speed-setpoint-filter-1-denominator-natural-frequency-1)).
2. Enter a value for the denominator attenuation ([p1418](SINAMICS%20Parameter%20SERVO.md#p14180n-speed-setpoint-filter-1-denominator-damping-1)).

###### General 2nd order filter

Set the following parameters for a general 2nd order filter:

1. Enter a value for the denominator frequency (p1417).
2. Enter a value for the denominator attenuation (p1418).
3. Enter a value for the numerator frequency ([p1419](SINAMICS%20Parameter%20SERVO.md#p14190n-speed-setpoint-filter-1-numerator-natural-frequency-1)).
4. Enter a value for the numerator attenuation ([p1420](SINAMICS%20Parameter%20SERVO.md#p14200n-speed-setpoint-filter-1-numerator-damping-1)).

You can also parameterize band stops and notch filters with the 2nd order filter. For more information about filters, see the [Filter](Configuring%20SINAMICS%20S-G-MV%20drives.md#filters) help page.

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

###### Additional parameters

---

---

**See also**

[Speed setpoint filter (servo)](#speed-setpoint-filter-servo)

#### Speed controller

This section contains information on the following topics:

- [Speed controller (servo)](#speed-controller-servo)
- [Kp/Tn adaptation (servo)](#kptn-adaptation-servo)
- [Integrator control (servo)](#integrator-control-servo)
- [Application example: Optimizing the speed controller](#application-example-optimizing-the-speed-controller)
- [Application example: Setting the reference model](#application-example-setting-the-reference-model)
- [Application example: Speed-torque precontrol in the drive](#application-example-speed-torque-precontrol-in-the-drive)

##### Speed controller (servo)

###### Description

The speed control of a variable-speed drive has the task of following the speed according to a specified setpoint (reference variable) as precisely as possible and without overshoot.

- Basic design of a speed control:

  The speed setpoint from the speed controller is constantly compared with the actual speed value from the motor encoder (the controlled variable). If there are differences due to the effect of disturbance variables (e.g. load changes, fluctuations in the supply voltage), the manipulated variable for the speed (usually the current setpoint for the current control loop) is changed so that the speed returns to the specified value. The individual control loops are cascaded in the converters, i.e. as cascade control.

  ![Speed controller](images/147855664651_DV_resource.Stream@PNG-en-US.png)

  Speed controller
- Design as cascade control

  Cascade control is the distribution of the tasks of a controlling system over various subordinate control loops with the objective of improved optimization of the entire closed-loop control or the control and limitation of intermediate controlled variables.

**PI controller**

The speed controller is designed as PI controller and comprises a P component (proportional effect) and an I component (integrating effect):

- The P component results in an instantaneous response to a control deviation (setpoint change). The P component is responsible for the dynamic response of the controller and is linearly proportional to the control deviation. The P gain is taken into account via [p1460](SINAMICS%20Parameter%20SERVO.md#p14600n-speed-controller-p-gain-adaptation-speed-lower-1).
- The I component corrects faults in the manipulated variable, e.g. of the load torque. If a control deviation occurs after a fault, the deviations are integrated (constantly added or subtracted). In this way, the duration of the control deviation is taken into account in the calculation of the manipulated variable. The following relations apply for the integral time [p1462](SINAMICS%20Parameter%20SERVO.md#p14620n-speed-controller-integral-time-adaptation-speed-lower-1):

Three different control types can be parameterized alternatively in the "Speed controller" screen form. Overshoot can be reduced via a reference model.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147782215179_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#speed-setpoint-filter-servo) |

###### Requirement

- Deactivated V/f control.

###### Making basic settings

1. Select the control type in the "Control type" ([p1300](SINAMICS%20Parameter%20SERVO.md#p13000n-open-loopclosed-loop-control-operating-mode-1)) drop-down list:

   - Speed control (encoderless)

     For simple applications with low control demand
   - Speed control (with encoder)

     For high-speed motors with high control demand
   - Torque control (with encoder)

     For plants with two motors, where the first motor is speed-controlled and there is a strong coupling between the two motors

   Additional configuration parameters are displayed for the "Speed control (encoderless)" control type.
2. Select whether the torque precontrol is to be activated in the "Torque precontrol active" ([p1402](SINAMICS%20Parameter%20SERVO.md#p14020n-closed-loop-current-control-and-motor-model-configuration-1).4) drop-down list:

   - "[1] Yes"
   - "[0] No"

   Additional configuration parameters are displayed with activated torque precontrol. The reference model also cannot be selected and parameterized.
3. Alternatively, select (for the torque precontrol) whether a "Velocity setpoint I component" reference model is to be used in the "Reference model" ([p1400](SINAMICS%20Parameter%20SERVO.md#p14000n-speed-control-configuration-3).3) drop-down list:

   - "[1] On"
   - "[0] Off"

   For an activated reference model, additional configuration parameters are displayed (see "Parameterizing a reference model"). A reference model can only be activated when the torque precontrol has been deactivated.

###### Parameterizing the speed control (with encoder)

1. Enter the P gain before the adaptation speed range in the "P gain" (p1460) field.
2. Enter the integral time before the adaptation speed range in the "Integral time" (p1462) field.
3. Specify the values for the Kp/Tn adaptation (see [Kp/Tn adaptation (servo)](#kptn-adaptation-servo)).
4. Click the "Maximum limitation" button.

   A dialog with the same name opens.
5. Make the following settings in the "Maximum limitation" dialog:

   - Set the maximum speed for the positive direction in the "Positive speed limit ([p1083](SINAMICS%20Parameter%20SERVO.md#p10830n-co-speed-limit-in-positive-direction-of-rotation-1)[0])" field.
   - Set the maximum speed for the negative direction in the "Negative speed limit" ([p1086](SINAMICS%20Parameter%20SERVO.md#p10860n-co-speed-limit-in-negative-direction-of-rotation-1)[0]) field.
   - Set the highest possible speed in the "Maximum speed" ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)[0]) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.
7. Specify the controller parameters for the I component of the PI controller via the "Integrator control" (see [Integrator control (servo)](#integrator-control-servo)).

   If you have activated a reference model (see "Making basic settings"), continue as described in Section "Parameterizing the reference model".

   If you have activated the torque precontrol instead of a reference model (see "Making basic settings"), make the following settings:
8. If you require an actual speed value filter, activate and configure this filter (see section "Configuring actual speed value filters").
9. Interconnect the signal source for the scaling of the motor moment of inertia in the "Moment of inertia scaling" ([p1497](SINAMICS%20Parameter%20SERVO.md#p14970n-ci-moment-of-inertia-scaling-signal-source-1)) field.
10. Enter the load moment of inertia in the "Load moment of inertia" ([p1498](SINAMICS%20Parameter%20SERVO.md#p14980n-load-moment-of-inertia-1)) field.
11. Enter the ratio between the total moment of inertia / mass (load + motor) and the intrinsic moment of inertia / mass (no load) in the "Ratio between the total moment of inertia and motor moment of inertia" ([p0342](SINAMICS%20Parameter%20SERVO.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia-1)) field.
12. Enter the smoothing time constant of the acceleration torque in the "Smoothing" ([p1517](SINAMICS%20Parameter%20SERVO.md#p15170n-accelerating-torque-smoothing-time-constant-1)) field.

###### Parameterizing the speed control (encoderless)

> **Note**
>
> **Encoderless operation active with active ONLINE connection**
>
> If there is an active ONLINE connection to the drive axis, an active encoderless operation is indicated via the "Encoderless operation active" ([r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1).1 = 1) LED. The interconnection screen form switches dynamically and shows the current values of the encoderless operation.

1. Enter the P gain before the adaptation speed range in the "P gain" (p1460) field.
2. Enter the integral time before the adaptation speed range in the "Integral time" (p1462) field.
3. Specify the values for the Kp/Tn adaptation (see [Kp/Tn adaptation (servo)](#kptn-adaptation-servo)).
4. Click the "Maximum limitation" button.

   A dialog with the same name opens.
5. Make the following settings in the "Maximum limitation" dialog:

   - Set the maximum speed for the positive direction in the "Positive speed limit (p1083[0])" field.
   - Set the maximum speed for the negative direction in the "Negative speed limit" (p1086[0]) field.
   - Set the highest possible speed in the "Maximum speed" (p1082[0]) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.
7. Specify the controller parameters for the I component of the PI controller via the "Integrator control" (see [Integrator control (servo)](#integrator-control-servo)).
8. If you require an actual speed value filter, activate and configure this filter (see section "Configuring actual speed value filters").
9. Interconnect the signal source for the scaling of the motor moment of inertia in the "Moment of inertia scaling" (p1497) field.
10. Enter the load moment of inertia in the "Load moment of inertia" (p1498) field.
11. Enter the ratio between the total moment of inertia / mass (load + motor) and the intrinsic moment of inertia / mass (no load) in the "Ratio between the total moment of inertia and motor moment of inertia" (p0342) field.
12. Enter the smoothing time constant of the acceleration torque in the "Smoothing" (p1517) field.

###### Parameterizing the torque control (with encoder)

1. Enter the P gain before the adaptation speed range in the "P gain" (p1460) field.
2. Enter the integral time before the adaptation speed range in the "Integral time" (p1462) field.
3. Specify the values for the Kp/Tn adaptation (see [Kp/Tn adaptation (servo)](#kptn-adaptation-servo)).
4. Click the "Maximum limitation" button.

   A dialog with the same name opens.
5. Make the following settings in the "Maximum limitation" dialog:

   - Set the maximum speed for the positive direction in the "Positive speed limit (p1083[0])" field.
   - Set the maximum speed for the negative direction in the "Negative speed limit" (p1086[0]) field.
   - Set the highest possible speed in the "Maximum speed" (p1082[0]) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.
7. Specify the controller parameters for the I component of the PI controller via the "Integrator control" (see [Integrator control (servo)](#integrator-control-servo)).

   If you have activated a reference model (see "Making basic settings"), continue as described in Section "Parameterizing the reference model".

   If, rather than a reference model, the torque precontrol has been activated (see section "Making basic settings"), then make the following settings:
8. If you require an actual speed value filter, activate and configure this filter (see section "Configuring actual speed value filters").
9. Interconnect the signal source for the scaling of the motor moment of inertia in the "Moment of inertia scaling" (p1497) field.
10. Enter the load moment of inertia in the "Load moment of inertia" (p1498) field.
11. Enter the ratio between the total moment of inertia / mass (load + motor) and the intrinsic moment of inertia / mass (no load) in the "Ratio between the total moment of inertia and motor moment of inertia" (p0342) field.
12. Enter the smoothing time constant of the acceleration torque in the "Smoothing" (p1517) field.

###### Configuring actual speed value filters

An actual speed value filter is required, when, for example, the encoder resolution is relatively poor. An actual speed value filter ([p1441](SINAMICS%20Parameter%20SERVO.md#p14410n-actual-speed-smoothing-time-1)) is calculated based on the encoder resolution and on the motor moment of inertia. The time constant of the actual speed value filter is considered during the calculation of the controller parameters. For information on filters, see also [Overview](Configuring%20SINAMICS%20S-G-MV%20drives.md#overview-1).

1. To open the configuration dialog for the actual speed value filter, click the "Actual value filter" button.

   The "Actual speed value filter" dialog opens.
2. Select the required filter type from the drop-down list with the same name:

   - PT2 low pass
   - General 2nd order filter
3. Enter the numerator natural frequency of the actual speed value filter in the "Numerator frequency" field ([p1449](SINAMICS%20Parameter%20SERVO.md#p14490n-speed-actual-value-filter-numerator-natural-frequency-1)[0]) (not possible for the "PT2 low pass" filter type).
4. Enter the numerator damping of the actual speed value filter in the "Numerator damping" field ([p1450](SINAMICS%20Parameter%20SERVO.md#p14500n-speed-actual-value-filter-numerator-damping-1)[0]) (not possible for the "PT2 low pass" filter type).
5. Enter the denominator natural frequency of the actual speed value filter in the "Denominator frequency" ([p1447](SINAMICS%20Parameter%20SERVO.md#p14470n-speed-actual-value-filter-denominator-natural-frequency-1)[0]) field.
6. Enter the denominator damping of the actual speed value filter in the "Denominator damping" ([p1448](SINAMICS%20Parameter%20SERVO.md#p14480n-speed-actual-value-filter-denominator-damping-1)[0]) field.
7. Activate the "Filter effective" option.
8. Once all necessary settings have been made, click "Close".

   The dialog closes. In the "Speed controller" screen form, the "Actual value filter" button is displayed only with a curve. This is the indicator for a configured actual speed value filter.

###### Parameterizing the reference model

The following configuration parameters are only displayed in the screen form when the "Reference model" option is activated.

Then make the following settings:

1. Click the "Reference model" button.

   A dialog with the same name opens.
2. Enter the "Dead time factor" ([p1435](SINAMICS%20Parameter%20SERVO.md#p14350n-speed-controller-reference-model-dead-time-1)), the broken dead time for the reference model of the velocity controller.
3. Enter the "Natural frequency" ([p1433](SINAMICS%20Parameter%20SERVO.md#p14330n-speed-controller-reference-model-natural-frequency-1)), the natural frequency of a PT2 element, for the reference model of the velocity controller.
4. Enter the "Damping" ([p1434](SINAMICS%20Parameter%20SERVO.md#p14340n-speed-controller-reference-model-damping-1)), the damping of a PT2 element, for the reference model of the velocity controller.
5. Once all necessary settings have been made, click "Close".

   The dialog closes. You have defined a valid reference model when the button shows a curve:

   ![Parameterizing the reference model](images/147855660683_DV_resource.Stream@PNG-en-US.png)

   ![Parameterizing the reference model](images/147855660683_DV_resource.Stream@PNG-en-US.png)
6. Click the "Maximum limitation" button to the right of the "Reference model" button.

   A dialog with the same name opens.
7. Make the following settings in the "Maximum limitation" dialog:

   - Set the maximum speed for the positive direction in the "Positive speed limit (p1083[0])" field.
   - Set the maximum speed for the negative direction in the "Negative speed limit" (p1086[0]) field.
   - Set the highest possible speed in the "Maximum speed" (p1082[0]) field.
8. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Display parameters

The following information is displayed via display parameters:

- Speed setpoint steady-state ([r1444](SINAMICS%20Parameter%20SERVO.md#r1444-speed-controller-speed-setpoint-steady-state-static-1))

  Displays the sum of all speed setpoints that are present.
- Motor moment of inertia ([p0341](SINAMICS%20Parameter%20SERVO.md#p03410n-motor-moment-of-inertia-1))

  Displays the motor moment of inertia (without load). When selecting a catalog motor ([p0301](SINAMICS%20Parameter%20SERVO.md#p03010n-motor-code-number-selection-1)), the parameter is automatically re-assigned and is write-protected. The information in [p0300](SINAMICS%20Parameter%20SERVO.md#p03000n-motor-type-selection-2) should be observed when removing the write protection.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855652235_DV_resource.Stream@PNG-en-US.PNG) | [Torque setpoints](#torque-setpoints-servo) |
| ![Signal processing](images/147855656459_DV_resource.Stream@PNG-en-US.png) | [Motor encoder](#motor-encoder-servo) |
| ![Signal processing](images/147855652235_DV_resource.Stream@PNG-en-US.PNG) | [Torque setpoints](#torque-setpoints-servo)   Only for the "Speed control (encoderless)" control type or for activated torque precontrol. |

###### Function diagrams (FD)

Servo control - Speed controller with encoder - 5040 -

Servo control - Speed controller, torque-speed precontrol with encoder (p1402.4 = 1) - 5042 -

Servo control - Speed controller without encoder - 5210 -

Servo control - Closed-loop speed control configuration - 5490 -

###### Additional parameters

- [r0062](SINAMICS%20Parameter%20SERVO.md#r0062-co-speed-setpoint-after-the-filter-1)
- [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)
- [r0064](SINAMICS%20Parameter%20SERVO.md#r0064-co-speed-controller-system-deviation-1)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- r1407
- [r1436](SINAMICS%20Parameter%20SERVO.md#r1436-co-speed-controller-reference-model-speed-setpoint-output-1)
- [r1438](SINAMICS%20Parameter%20SERVO.md#r1438-co-speed-controller-speed-setpoint-1)
- [r1454](SINAMICS%20Parameter%20SERVO.md#r1454-co-speed-controller-system-deviation-i-component-1)
- [r1468](SINAMICS%20Parameter%20SERVO.md#r1468-speed-controller-p-gain-effective-1)
- [r1469](SINAMICS%20Parameter%20SERVO.md#r1469-speed-controller-integral-time-effective-1)
- [r1480](SINAMICS%20Parameter%20SERVO.md#r1480-co-speed-controller-pi-torque-output-1)
- [r1481](SINAMICS%20Parameter%20SERVO.md#r1481-co-speed-controller-p-torque-output-1)
- [r1482](SINAMICS%20Parameter%20SERVO.md#r1482-co-speed-controller-i-torque-output-1)
- [r1493](SINAMICS%20Parameter%20SERVO.md#r1493-co-moment-of-inertia-total-1)
- [r1518](SINAMICS%20Parameter%20SERVO.md#r151801-co-accelerating-torque-1)

---

##### Kp/Tn adaptation (servo)

###### Description

The Kp/Tn adaptation enables a completely variable proportional gain Kp. The adaptation factor can be interconnected with scaling manually via the parameters of the input screen form or by means of BICO interconnection. A linear adaptation characteristic can be defined by specifying two characteristic interpolation points.

The K<sub>p</sub>/T<sub>n</sub> adaptation is used, for example, for winders where the gain of the tension controller is adapted depending on the diameter.

![Winder](images/147855687819_DV_resource.Stream@PNG-en-US.png)

Winder

###### Defining adaptation parameters

1. Select the "[1] Yes" option ([p1400](SINAMICS%20Parameter%20SERVO.md#p14000n-speed-control-configuration-3).5) in the drop-down list below the "Adaptation" button.

   The K<sub>p</sub>/T<sub>n</sub> adaptation is activated and can be parameterized. No adaptation parameters can be specified without this activation.
2. Click the "K<sub>p</sub>/T<sub>n</sub> adaptation" button next to the input field of the p gain.

   The input screen form "K<sub>p</sub>/T<sub>n</sub> adaptation" is displayed.
3. Interconnect the signal source for scaling the P gain of the velocity controller in the "Scaling" ([p1466](SINAMICS%20Parameter%20SERVO.md#p14660n-ci-speed-controller-p-gain-scaling-1)) field.
4. Interconnect the signal source for the adaptation signal for the additional adaptation of the P gain of the speed controller in the "Adaptation signal" ([p1455](SINAMICS%20Parameter%20SERVO.md#p14550n-ci-speed-controller-p-gain-adaptation-signal-1)) field.
5. Click the "Adaptation" button.

   A dialog with the same name opens.
6. Enter the percentage values for the following adaptation parameters:

   - "Adaptation factor upper" ([p1459](SINAMICS%20Parameter%20SERVO.md#p14590n-adaptation-factor-upper))

     Adaptation range (&gt; [p1457](SINAMICS%20Parameter%20SERVO.md#p14570n-speed-controller-p-gain-adaptation-upper-starting-point-1)) to additionally adapt the P gain of the speed/velocity controller.
   - "Adaptation factor lower" ([p1458](SINAMICS%20Parameter%20SERVO.md#p14580n-adaptation-factor-lower))

     Adaptation range (0% ... [p1456](SINAMICS%20Parameter%20SERVO.md#p14560n-speed-controller-p-gain-adaptation-lower-starting-point-1)) to additionally adapt the P gain of the speed/velocity controller.
   - "Lower application point" (p1456)

     Lower application point of the adaptation range for the additional adaptation of the P gain of the speed controller.
   - "Upper application point" (p1457)

     Upper application point of the adaptation range for the additional adaptation of the P gain of the speed controller.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. Enter the percentage values for the following parameters:

   - "Scaling Kp" ([p1461](SINAMICS%20Parameter%20SERVO.md#p14610n-speed-controller-kp-adaptation-speed-upper-scaling-1))

     P gain of the speed controller for the upper adaptation speed range (&gt; [p1465](SINAMICS%20Parameter%20SERVO.md#p14650n-speed-controller-adaptation-speed-upper-1)).
   - "Scaling Tn" ([p1463](SINAMICS%20Parameter%20SERVO.md#p14630n-speed-controller-tn-adaptation-speed-upper-scaling-1))

     Integral time of the speed controller after the adaptation speed range (&gt; p1465).
9. Enter the desired speed in the "Upper adaptation speed" (p1465) field.
10. Enter the desired speed in the "Lower adaptation speed" ([p1464](SINAMICS%20Parameter%20SERVO.md#p14640n-speed-controller-adaptation-speed-lower-1)) field.

###### Display parameters

The following information is displayed via display parameters:

- "P gain" ([p1460](SINAMICS%20Parameter%20SERVO.md#p14600n-speed-controller-p-gain-adaptation-speed-lower-1))

  Display of the P gain value. Is taken from the "Speed controller" screen form.
- "Actual speed value" ([r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1))

  Display and connector output for the currently smoothed actual speed value.
- "Integral time" ([p1462](SINAMICS%20Parameter%20SERVO.md#p14620n-speed-controller-integral-time-adaptation-speed-lower-1))

  Display of the integral time. Is taken from the "Speed controller" screen form.

###### Function diagrams (FD)

Servo control - Speed controller adaptation (Kp_n/Tn_n adaptation) - 5050 -

###### Additional parameters

- [r1468](SINAMICS%20Parameter%20SERVO.md#r1468-speed-controller-p-gain-effective-1)
- [r1469](SINAMICS%20Parameter%20SERVO.md#r1469-speed-controller-integral-time-effective-1)

---

##### Integrator control (servo)

###### Description

You can specify the controller parameters for the I component of a [PI controller](#speed-controller-servo) in the "Integrator control" dialog.

If you set a value in "Integrator feedback", the integrator of the speed/velocity controller is reparameterized to become a PT1 filter through a feedback element (1st order low-pass filter characteristic). For an application example, see [p1494](SINAMICS%20Parameter%20SERVO.md#p14940n-speed-controller-integrator-feedback-time-constant-1).

For cases where the closed-loop control runs into a saturation, e.g. because a limitation has been exceeded (e.g. hanging load), the I component increases greatly. When the fault dies down again, the I component which is too high must be allowed to decay (windup).

With "Hold integrator", you shut down the integrator when the limitation is exceeded (saturation) and specify a setting value when switching on the final controlling element for the I component, e.g. via "Set integrator value".

###### Specifying the parameters of the I component

1. Click the "Integrator control" button in the "Speed controller" screen form.

   The dialog with the same name opens.
2. Enter the time constant of the PT1 filter for the integrator feedback in the "Integrator feedback" (p1494) field.

   The integrator of the speed/velocity controller is reparameterized to become a PT1 filter through a feedback element (1st order low-pass filter characteristic). Typical application

   - Motion at zero setpoint and dominant stiction can be suppressed but this has a negative effect on the remaining setpoint/actual-value difference. This can be used, for example, to avoid oscillation of a position-controlled axis at standstill (stick-slip effect) or overshoot when traversing in micrometer steps.
   - Also prevents tension/stressing for axes that are mechanically and rigidly coupled with one another (e.g. for synchronous spindles, master-device axes).
3. Interconnect the signal source to hold the integrator (speed control with encoder, torque control with encoder) in the "Hold integrator" ([p1476](SINAMICS%20Parameter%20SERVO.md#p14760n-bi-speed-controller-hold-integrator-1)) field.
4. Interconnect the signal source from which the value for "Set integrator value" is to be read in the "Set integrator value" ([p1477](SINAMICS%20Parameter%20SERVO.md#p14770n-bi-speed-controller-set-integrator-value-1)) field.
5. Interconnect the signal source from which the integrator setting value is to be read in the "Integrator setting value" ([p1478](SINAMICS%20Parameter%20SERVO.md#p14780n-ci-speed-controller-integrator-setting-value-1)) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Display parameters

The following information is displayed via display parameters:

- "P gain" ([r1468](SINAMICS%20Parameter%20SERVO.md#r1468-speed-controller-p-gain-effective-1))

  Displays the effective P gain of the speed controller. Is taken from the "Speed controller" screen form.
- "Integral time" ([r1469](SINAMICS%20Parameter%20SERVO.md#r1469-speed-controller-integral-time-effective-1))

  Displays the effective integral time of the speed controller. Is taken from the "Speed controller" screen form.
- "PI torque output" ([r1480](SINAMICS%20Parameter%20SERVO.md#r1480-co-speed-controller-pi-torque-output-1))

  Display and connector output for the torque setpoint at the output of the PI speed controller.
- "P torque output" ([r1481](SINAMICS%20Parameter%20SERVO.md#r1481-co-speed-controller-p-torque-output-1))

  Display and connector output for the torque setpoint at the output of the P speed controller.
- "I torque output" ([r1482](SINAMICS%20Parameter%20SERVO.md#r1482-co-speed-controller-i-torque-output-1))

  Display and connector output for the torque setpoint at the output of the I speed controller.

###### Function diagrams (FD)

Servo control - Speed controller with encoder - 5040 -

Servo control - Speed controller, torque-speed precontrol with encoder (p1402.4 = 1) - 5042 -

Servo control - Speed controller without encoder - 5210 -

Servo control - Closed-loop speed control configuration - 5490 -

###### Additional parameters

- [r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1)
- p1476
- p1477

---

##### Application example: Optimizing the speed controller

###### Optimization of the speed controller

Before you manually optimize the speed controller, it is better to first perform an Auto Servo Tuning. The Auto Servo Tuning sets the most important parameters of the speed controller over various optimization sequences. See also [One Button Tuning (servo)](#one-button-tuning-servo).

These include the following parameters:

- P gain ([p1460](SINAMICS%20Parameter%20SERVO.md#p14600n-speed-controller-p-gain-adaptation-speed-lower-1))
- Integral time ([p1462](SINAMICS%20Parameter%20SERVO.md#p14620n-speed-controller-integral-time-adaptation-speed-lower-1))

The following figures shown a non-optimized speed controller and an optimized speed controller with the setting "Robust". For this purpose, the smoothed actual speed value ([r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)) was recorded with the technology trace via the drive control panel (trigger on tag, the speed setpoint ([r1438](SINAMICS%20Parameter%20SERVO.md#r1438-co-speed-controller-speed-setpoint-1)) was used as tag, speed setpoint = 1000 rpm).

![Actual speed value not optimized](images/147855732235_DV_resource.Stream@PNG-en-US.png)

Actual speed value not optimized

!["Robust" actual speed value optimized](images/147855736203_DV_resource.Stream@PNG-en-US.png)

"Robust" actual speed value optimized

If after the optimization the speed controller is not sufficiently dynamic or begins to oscillate, the speed controller should be optimized manually. To do this, record the response of the speed controller with the technology trace.

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

Servo control - Reference model / precontrol balancing / speed limitation - 5030 -

###### Additional parameters

---

---

**See also**

[Speed controller (servo)](#speed-controller-servo)

##### Application example: Setting the reference model

###### Adjusting the reference model

The reference model serves for simulating the path of the speed control loop with a P speed controller. The reference model delays the setpoint/actual deviation for the integral component of the speed controller so that the transient elements can be suppressed. The integral component in the controller is mainly responsible for excessive vibrations that are further integrated during the limitation phase, and thus generate an actuating signal that is too large.

> **Note**
>
> **Reference model only for applications with small amplitude**
>
> Use the reference model only for applications for which the signal does not reach the torque limit. Large signals can cause overshooting near the torque limit.

The reference model is designed as a PT2 element. Correspondingly, the following parameters can be set:

- Dead time factor ([p1435](SINAMICS%20Parameter%20SERVO.md#p14350n-speed-controller-reference-model-dead-time-1)); for a description of the dead time, see also [Application example: Speed precontrol](#application-example-speed-precontrol).
- Natural frequency ([p1433](SINAMICS%20Parameter%20SERVO.md#p14330n-speed-controller-reference-model-natural-frequency-1)); the natural frequency is the frequency of the system at which it can vibrate after one excitation. You must determine the natural frequency of your system or adapt it empirically.
- Damping ([p1434](SINAMICS%20Parameter%20SERVO.md#p14340n-speed-controller-reference-model-damping-1)); value for the damping in the PT2 element

You parameterize the reference model after you have optimized the speed controller.

![Optimization without a reference model](images/147855760139_DV_resource.Stream@PNG-en-US.png)

Optimization without a reference model

You can then attempt to eliminate the overshoot with the aid of the reference model.

###### Determining the natural frequency

You can use various methods to determine the natural frequency.

- Determining the natural frequency from the frequency master response
- Determining the natural frequency from the transient response of the speed controller
- Empirically determining the natural frequency

**Determining the natural frequency from the frequency master response**

For these methods of determination, you have to record the frequency master response of the speed control loop with a measuring function, which is not yet available The natural frequency can then be read from the Bode diagram at the point where the phase frequency curve crosses the zero line for the first time.

Then check the setting by using the function generator (not yet available) as a commissioning tool. Also parameterize a trace in order to record the signals.

If the transmission function is still causing an overshoot, you also have to set or increase the damping for the reference model.

**Empirically determining the natural frequency**

The empirical determination of the reference model is based on operating the speed controller as a P controller and trying to set the output of the reference model (speed setpoint I component) so that it matches the actual speed value.

###### Parameterizing the reference model

To parameterize the reference model, record the [r1436](SINAMICS%20Parameter%20SERVO.md#r1436-co-speed-controller-reference-model-speed-setpoint-output-1) and [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1) signals. Set the parameters as follows:

- Set the "Dead time factor" to 2; this value is also recommended for the precontrol.
- The natural frequency shows how fast the value rises. Consequently, compare the r1436 and r0063 signals, and change the natural frequency until the rise is adapted.
- The damping can be set to 0.8. If, however, an overshoot occurs, the value can be increased.

###### Parameterizing the reference model

If the reference model has been correctly parameterized, an overshoot no longer occurs:

![Parameterizing the reference model](images/147855764107_DV_resource.Stream@PNG-en-US.png)

Parameterizing the reference model

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

Servo control - Reference model / precontrol balancing / speed limitation - 5030 -

###### Additional parameters

---

##### Application example: Speed-torque precontrol in the drive

###### Speed-torque precontrol in the speed controller

Only use the torque precontrol if the moment of inertia remains constant and you can calculate it. It you cannot calculate the moment of inertia, a value can be obtained with the aid of the "Inertia estimator" function module.

If the speed setpoint has a ramp-shaped curve, after a short time the P element of the speed controller supplies almost no output signal during the acceleration. After reaching the setpoint speed, the I element of the speed controller ensures that the torque continues to rise, which results in overshooting the speed setpoint (1).

![Speed-torque precontrol in the speed controller](images/147855787403_DV_resource.Stream@PNG-en-US.png)

**Acceleration model**

If you know the moment of inertia of the motor and the connected mechanical system, the speed controller can calculate the setpoint torque required for the acceleration using an acceleration model, and apply the acceleration torque ([p1518](SINAMICS%20Parameter%20SERVO.md#r151801-co-accelerating-torque-1)) at the output of the speed controller. The I element of the speed controller is then practically no longer effective (2). The torque required for the acceleration is then supplied by the torque precontrol. Consequently, the precontrol assumes the command behavior and the speed controller compensates for interferences.

**Speed-torque precontrol in the drive**

The precontrol in the drive offers the following advantages:

- The precontrol in the drive calculates the torque currently required. This value is available even when no controller can provide a precontrol value. This makes the speed controller significantly faster and allows it to be set more dynamic.
- Because the lower-level speed controller is faster, the position control has a better disturbance characteristic and can be set more dynamic (larger p gain).
- Unlike the reference model, the precontrol also functions correctly at the torque limit.

###### Determining the moment of inertia

The total moment of inertia is given by the sum of the moment of inertia of the load and the moment of inertia of the motor.

- The moment of inertia of the motor ([p0341](SINAMICS%20Parameter%20SERVO.md#p03410n-motor-moment-of-inertia-1)) is available or must be entered. The data is on the rating plate of the motor.
- You calculate the moment of inertia of the load and enter it in [p1498](SINAMICS%20Parameter%20SERVO.md#p14980n-load-moment-of-inertia-1). For this purpose, you can make a "rotating measurement" (p1498). If this measurement cannot be made, you can accelerate and brake the drive manually along a ramp, and so determine the moment of inertia of the load manually.
- The "Moment of inertia/motor ratio" factor ([p0342](SINAMICS%20Parameter%20SERVO.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia-1)) between the total moment of inertia J and the moment of inertia of the motor has to be determined manually or by optimizing the speed controller.

###### Parameterizing the speed-torque precontrol in the speed controller

To view or adapt the parameters of the precontrol, proceed as follows:

1. Select "Yes" for "Torque precontrol active" in the "Speed control" mask ([p1402](SINAMICS%20Parameter%20SERVO.md#p14020n-closed-loop-current-control-and-motor-model-configuration-1)).
2. Parameterize the various moments of inertia (see above).
3. Click the "Precontrol" button. The dialog with the same name opens.
4. Parameterize the "Dead time factor" and the "Time constant" (see below).
5. The value for the precontrol torque ([r1518](SINAMICS%20Parameter%20SERVO.md#r151801-co-accelerating-torque-1)) uses a smoothing element ([p1517](SINAMICS%20Parameter%20SERVO.md#p15170n-accelerating-torque-smoothing-time-constant-1)) and is applied after the speed controller (see also "Torque setpoints").

   The factory setting for the "Time constant" (p1517) at 4 ms is relatively high. This setting makes the speed controller too slow under some circumstances.
6. Consequently, check p1517 and, if necessary, set the time constant to 0.5 ms to permit a more dynamic controller. If your system tends to low frequency vibrations, a larger time constant can dampen the vibrations. In this case, an active vibration damping using the "Active Positioning Control" (APC) function module may be better.

   If the smoothing time is set too long, the mechanical system can sometimes fail.

###### Parameterizing the precontrol balancing

The precontrol balancing serves to prevent unwanted controller movements until the precontrol is activated, see also [Application example: Speed precontrol](#application-example-speed-precontrol).

###### Function diagrams (FD)

Servo control - Speed setpoint filter and speed precontrol - 5020 -

Servo control - Reference model / precontrol balancing / speed limitation - 5030 -

###### Additional parameters

---

#### U/f control

This section contains information on the following topics:

- [U/f control (servo)](#uf-control-servo)

##### U/f control (servo)

###### Description

A V/f control is an open control loop. For this reason, the term "open-loop control" is used instead of "closed-loop control". The V/f control is used preferably in the following applications:

- For applications with low to medium demands on the dynamic response, speed setting range and accuracy.
- For group drives (several motors on one converter), also with "Group synchronism" (e.g. with reluctance motors in the textiles industry).
- If simple commissioning and high parameter robustness are required.

With V/f control, the voltage amplitude "V" is specified depending on the current motor frequency "f". A simple motor model is used in which the quotient "V/f" is proportional to the achievable torque. The V/f characteristic can be set (e.g. linear and square-law characteristic).

> **Note**
>
> **Limited area of application for the V/f control**
>
> The V/f control must only be used as a diagnostic function, for example, in order to check the function of the motor encoder.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147782215179_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#speed-setpoint-filter-servo) |

###### Parameterizing V/f control

For the V/f control with linear characteristic to function, it must be activated via the "Diagnostics activation" ([p1317](SINAMICS%20Parameter%20SERVO.md#p13170n-uf-control-activation)[0]) function.

1. Select "[1] Activated" in the drop-down list.

   The other input fields are then displayed.
2. Enter the ramp-up and ramp-down time for the V/f control in the "Ramp-up/ramp-down time" ([p1318](SINAMICS%20Parameter%20SERVO.md#p13180n-uf-control-ramp-upramp-down-time)[0]) field.
3. Enter the top point of a linear voltage characteristic for the V/f control in the "Voltage 4" ([p1327](SINAMICS%20Parameter%20SERVO.md#p13270n-uf-control-characteristic-voltage)[0]) field.
4. Enter the voltage at frequency = 0 Hz in the "Voltage at f = 0 Hz" ([p1319](SINAMICS%20Parameter%20SERVO.md#p13190n-uf-control-voltage-at-zero-frequency)[0]) field.
5. Enter the 4th point of this characteristic in the "Frequency 4" ([p1326](SINAMICS%20Parameter%20SERVO.md#p13260n-uf-control-characteristic-frequency)[0]) field.

   A programmable frequency characteristic for the V/f control is defined by four points.

###### Setting the maximum limitation of the speed setpoint

You can specify the maximum limitation of the speed setpoint via the "Maximum limitation" dialog.

1. Click the "Speed setpoint limited" button.

   The "Maximum limitation" dialog opens.
2. Make the following settings in the "Maximum limitation" dialog:

   - "Positive speed limit" ([p1083](SINAMICS%20Parameter%20SERVO.md#p10830n-co-speed-limit-in-positive-direction-of-rotation-1)[0])

     Maximum speed for the positive direction.
   - "Negative speed limit" ([p1086](SINAMICS%20Parameter%20SERVO.md#p10860n-co-speed-limit-in-negative-direction-of-rotation-1)[0])

     Maximum speed for the negative direction.
   - "Maximum speed" ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)[0])

     Highest possible speed.
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed (p1082)

  Display of the highest possible speed.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855791499_DV_resource.Stream@PNG-en-US.png) | [Power unit](#power-unit-servo) |
| ![Signal processing](images/147855791499_DV_resource.Stream@PNG-en-US.png) | [Power unit](#power-unit-servo) |

###### Function diagrams (FD)

Servo control - U/f control for diagnostics - 5300 -

###### Additional parameters

- [r0024](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0024-co-line-supply-frequency-smoothed)
- [r0062](SINAMICS%20Parameter%20SERVO.md#r0062-co-speed-setpoint-after-the-filter-1)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)

---

#### Torque setpoints

This section contains information on the following topics:

- [Torque setpoints (servo)](#torque-setpoints-servo)

##### Torque setpoints (servo)

###### Description

The torque setpoint of the motor can be set for the following versions:

- Speed controller with encoder

  It is possible to switch between speed-controlled and torque-controlled operation (leading/following switchover) with this option.
- Speed controller without encoder

  Pure torque-controlled operation is not possible around zero speed. However, you can apply a scalable and a fixed supplementary torque.

A predefined switchover speed can be used to specify as of which speed should travel generally be in encoderless operation.

In order to avoid overloads of the machine particularly during acceleration and deceleration phases, the torque of the drive must be limited according to the connected machine.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855522443_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#speed-controller-servo) |
| ![Signal source](images/147855522443_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#speed-controller-servo) |

###### Switchover between speed/torque control

1. Interconnect the "Speed/torque control" ([p1501](SINAMICS%20Parameter%20SERVO.md#p15010n-bi-change-over-between-closed-loop-speedtorque-control-1)) signal source for switching between speed and torque control.

###### Specifying the switchover speed for encoderless operation

1. Check that separate speed controllers have been set for operation with and without encoder.

   This is a requirement for switching from operation with encoder to encoderless operation.
2. Enter the maximum speed (or velocity) as of which there is an automatic switchover to encoderless operation in the "Switchover speed" ([p1404](SINAMICS%20Parameter%20SERVO.md#p14040n-encoderless-operation-changeover-speed-1)[0]) field.

###### Defining torque limiting

1. Click the "Torque limiting" button.

   A dialog with the same name opens.
2. Interconnect the following signal sources:

   - Upper "Scaling" ([p1552](SINAMICS%20Parameter%20SERVO.md#p15520n-ci-torque-limit-upper-scaling-without-offset-1)[0]) field

     Scaling of the upper torque limit for the limitation of the speed controller output without taking the current and power limits into account.
   - Lower "Scaling" ([p1554](SINAMICS%20Parameter%20SERVO.md#p15540n-ci-torque-limit-lower-scaling-without-offset-1)[0]) field

     Scaling of the lower torque limit for the limitation of the speed controller output without taking the current and power limits into account.
   - "Torque limit variable" ([p1551](SINAMICS%20Parameter%20SERVO.md#p15510n-bi-torque-limit-variablefixed-signal-source-1)[0])

     Switch the torque limits between variable and fixed torque limit.
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855828491_DV_resource.Stream@PNG-en-US.PNG) | [Supplementary torques](#supplementary-torques-servo) |

###### Function diagrams (FD)

Servo control - Torque setpoint, control mode switchover - 5060 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [p1402](SINAMICS%20Parameter%20SERVO.md#p14020n-closed-loop-current-control-and-motor-model-configuration-1)
- [r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1)
- [r1480](SINAMICS%20Parameter%20SERVO.md#r1480-co-speed-controller-pi-torque-output-1)
- p1501

---

#### Supplementary torques

This section contains information on the following topics:

- [Supplementary torques (servo)](#supplementary-torques-servo)

##### Supplementary torques (servo)

###### Description

After the speed controller, it is possible to apply three supplementary torques to the torque setpoint. They can be torque setpoints that are known or calculated. Possible supplementary torques are, for example:

- Friction torques of the motor and drive (friction characteristic); the motor uses up part of the torque setpoint through friction. The friction characteristic is interconnected to supplementary setpoint 3 as default.
- Specifying weight torque for the startup of the drive, e.g. for a hanging load.
- Known precontrol torque of the controller

Parameterize up to three supplementary torques in the "Supplementary torques" screen form. These supplementary torques are added to the torque setpoint. In this way, faults can be minimized. Supplementary torque 3 is interconnected, for example, to the signal of the friction characteristic. The supplementary torque compensates the friction torque of the drive.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855627275_DV_resource.Stream@PNG-en-US.png) | [Speed precontrol](#speed-precontrol-servo) |
| ![Signal source](images/147855652235_DV_resource.Stream@PNG-en-US.PNG) | [Torque setpoints](#torque-setpoints-servo) |

###### Requirement

- Deactivated V/f control

###### Setting supplementary torques

You can parameterize up to three supplementary torques.

1. Interconnect the "Supplementary torque 1" ([p1511](SINAMICS%20Parameter%20SERVO.md#p15110n-ci-supplementary-torque-1-1)) signal source of supplementary torque 1.
2. Interconnect the "Scaling" ([p1512](SINAMICS%20Parameter%20SERVO.md#p15120n-ci-supplementary-torque-1-scaling-1)) signal source of the supplementary torque 1 scaling factor.
3. Interconnect the "Supplementary torque 2" ([p1513](SINAMICS%20Parameter%20SERVO.md#p15130n-ci-supplementary-torque-2-1)) signal source of supplementary torque 2.
4. Interconnect the "Supplementary torque 3" ([p1569](SINAMICS%20Parameter%20SERVO.md#p15690n-ci-supplementary-torque-3-1)) signal source of supplementary torque 3.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855865739_DV_resource.Stream@PNG-en-US.png) | [Torque limiting](#torque-limiting-servo) |

###### Function diagrams (FD)

Servo control - Torque setpoint, control mode switchover - 5060 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1509](SINAMICS%20Parameter%20SERVO.md#r1509-co-torque-setpoint-before-torque-limiting-1)
- [r1515](SINAMICS%20Parameter%20SERVO.md#r1515-supplementary-torque-total-1)

---

#### Torque limiting

This section contains information on the following topics:

- [Torque limiting (servo)](#torque-limiting-servo)

##### Torque limiting (servo)

###### Description

A machine sets a counter-torque or load torque against the torque of the drive.

In order to avoid overloads of the machine particularly during acceleration and deceleration phases, the torque of the drive must be limited according to the connected machine.

The limiting of the torque setpoint to a maximum permissible value is possible in all four quadrants. Different limits can be set via parameters for motorized and generator operation.

![Current setpoint limitation](images/147855874187_DV_resource.Stream@PNG-en-US.png)

Current setpoint limitation

The current, torque and power limits of the drive are parameterized in the "Torque limiting" screen form.

The torque limiting is always active with the preset factory settings.

**Torque limiting variants:**

The following torque limiting variants are available:

- No settings are made:

  - No additional restrictions of the torque limits are required by the application.
- Fixed limits are required for the torque:

  - Upper and lower or alternatively motorized and regenerative fixed limit values can be specified independently from separate sources.
- Dynamic limits are required for the torque:

  - Upper and lower or alternatively motorized and regenerative dynamic limit values can be specified independently from separate sources.
  - The source of the current limit values is selected via parameters.
- A torque offset can be set.
- In addition, power limits can be set independently for motorized and regenerative operation.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855828491_DV_resource.Stream@PNG-en-US.PNG) | [Supplementary torques](#supplementary-torques-servo) |

###### Requirement

- Deactivated V/f control.

###### Selecting the type of torque limiting

You can specify the type of torque limiting with which you want to work via the "Motorized/regenerative active" ([p1400](SINAMICS%20Parameter%20SERVO.md#p14000n-speed-control-configuration-3)[0].4) selection.

1. Select the type of torque limiting in the "Motorized/regenerative active" drop-down list.

   - "[1] Yes"

     Motorized/regenerative torque limits are used.
   - "[0] No"

     Upper and lower torque limits are used (default setting).

   The circuit diagram corresponding to this setting is displayed.

###### Configuring the torque limiting

After you have specified the type of torque limiting, you can configure the torque limiting.

1. Click the "Torque limit motorized" or the "Upper torque limit" button.

   A dialog with the same name opens.
2. Make the following settings:

   - Enter the fixed upper or motorized torque limit in the "Upper/motorized torque limit" ([p1520](SINAMICS%20Parameter%20SERVO.md#p15200n-co-torque-limit-uppermotoring-3)[0]) field.
   - Interconnect the signal source for the upper or motorized torque limit in the "Upper/motorized torque limit" ([p1522](SINAMICS%20Parameter%20SERVO.md#p15220n-ci-torque-limit-uppermotoring-3)[0]) field.
   - Interconnect the signal source for the scaling of the upper or motorized torque limit in p1522 in the "Scaling" ([p1528](SINAMICS%20Parameter%20SERVO.md#p15280n-ci-torque-limit-uppermotoring-scaling-1)[0]) field.
   - Interconnect the signal source to switch the torque limits between variable and fixed torque limit in the "Variable/fixed torque limit" ([p1551](SINAMICS%20Parameter%20SERVO.md#p15510n-bi-torque-limit-variablefixed-signal-source-1)[0]) field.
   - Enter the torque offset for the torque limit in the "Torque offset" ([p1532](SINAMICS%20Parameter%20SERVO.md#p15320n-co-torque-limit-offset-1)[0]) field.
3. Once all necessary settings have been made, click "Close".

   The dialog closes.
4. Click the "Regenerative torque limit" or the "Lower torque limit" button.

   A dialog with the same name opens.
5. Make the following settings:

   - Enter the fixed lower or regenerative torque limit in the "Lower/regenerative torque limit" ([p1521](SINAMICS%20Parameter%20SERVO.md#p15210n-co-torque-limit-lowerregenerative-3)[0]) field.
   - Interconnect the signal source for the lower or regenerative torque limit in the "Lower/regenerative torque limit" ([p1523](SINAMICS%20Parameter%20SERVO.md#p15230n-ci-torque-limit-lowerregenerative-3)[0]) field.
   - Interconnect the signal source for the scaling of the lower or regenerative torque limit in p1523 in the "Scaling" ([p1529](SINAMICS%20Parameter%20SERVO.md#p15290n-ci-torque-limit-lowerregenerative-scaling-1)[0]) field.
   - Interconnect the signal source to switch the torque limits between variable and fixed torque limit in the "Variable/fixed torque limit" (p1551[0]) field.
   - Enter the torque offset for the torque limit in the "Torque offset" (p1532[0]) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Configuring the current limit

The current limit can be configured alternatively or in addition to the torque limiting. If only the current limit is configured (without the torque limit), the drive ramps up quickly. However, as only the ramp-function generator is stopped when the current limit is reached, the current can continue to rise. This must be taken into account during the parameterization (if required, through a safety clearance) so that the drive is not switched off with an overcurrent error.

1. Click the "Current limit" button.

   A dialog with the same name opens.
2. Enter the maximum current limit in the "Current limit" ([p0640](SINAMICS%20Parameter%20SERVO.md#p06400n-current-limit)[0]) field.
3. Enter the maximum share of the field-generating current at the permitted maximum current in the "Maximum field-generating current" ([p1603](SINAMICS%20Parameter%20SERVO.md#p16030n-field-generating-current-maximum-1)[0]) field.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Configuring the power limit

The power limit can be configured alternatively or in addition to the torque limiting.

1. Click the "Power limit" button.

   A dialog with the same name opens.
2. Enter the appropriate power limits in the following fields:

   - "Power limit motorized" ([p1530](SINAMICS%20Parameter%20SERVO.md#p15300n-power-limit-motoring-1)[0])

     and/or
   - "Power limit regenerative" ([p1531](SINAMICS%20Parameter%20SERVO.md#p15310n-power-limit-regenerative-1)[0])
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Display of the set torque limiting

The set torque limiting is displayed in the circuit diagram via the following LEDs:

- Torque limit reached ([r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1).7)
- Upper torque limit active (r1407.8)
- Lower torque limit active (r1407.9)

The upper and lower torque limits of all torque limits are displayed via two unlabeled display fields ([r1534](SINAMICS%20Parameter%20SERVO.md#r1534-co-total-upper-torque-limit-1)/[r1535](SINAMICS%20Parameter%20SERVO.md#r1535-co-total-lower-torque-limit-1)). Negative values at r1534 or positive values at r1535 represent a minimum torque for the other torque directions and can result in the drives spinning if there is no counter-torque.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrolled movement of the drive as a result of incorrect parameter assignment**   Incorrect parameter assignment of the torque limits can result in uncontrolled movement of the drives if there is no counter-torque. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Make sure that the parameter assignment is correct. |  |

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855869963_DV_resource.Stream@PNG-en-US.png) | [Current setpoint filter](#current-setpoint-filter-servo) |

###### Function diagrams (FD)

Servo control - Generation of the torque limits, overview - 5609 -

Servo control - Torque limiting/reduction, interpolator - 5610 -

Servo control - Motoring/generating torque limit - 5620 -

Servo control - Upper/lower torque limit - 5630 -

Servo control - Mode switchover, power/current limitation - 5640 -

###### Additional parameters

- [r0067](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r006701-absolute-current-value-permissible)
- [r0079](SINAMICS%20Parameter%20SERVO.md#r007901-co-torque-setpoint-total-1)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1526](SINAMICS%20Parameter%20SERVO.md#r1526-co-torque-limit-uppermotoring-without-offset-1)
- [r1527](SINAMICS%20Parameter%20SERVO.md#r1527-co-torque-limit-lowerregenerative-without-offset-1)
- [r1533](SINAMICS%20Parameter%20SERVO.md#r1533-current-limit-torque-generating-total-1)
- r1534
- r1535
- [r1538](SINAMICS%20Parameter%20SERVO.md#r1538-co-upper-effective-torque-limit-1)
- [r1539](SINAMICS%20Parameter%20SERVO.md#r1539-co-lower-effective-torque-limit-1)

---

#### Current setpoint filter

This section contains information on the following topics:

- [Current setpoint filter (servo)](#current-setpoint-filter-servo)

##### Current setpoint filter (servo)

###### Description

The current setpoint filters are used to skip or weaken certain frequency ranges in order to suppress resonance effects. Bandstop filters and low-pass filters are available to suppress specific interference frequency ranges. You will find a description of the filter at [Overview](Configuring%20SINAMICS%20S-G-MV%20drives.md#overview-1).

Up to four current setpoint filters can be set for a drive of type "Highly dynamic (servo)" as standard.

> **Note**
>
> **Extended current setpoint filter**
>
> Six further current setpoint filters can be connected via the "Extended current setpoint filter" function module (see [Function modules (servo)](#function-modules-servo)). These additional filters can be activated and configured in the same manner as the four base filters.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855865739_DV_resource.Stream@PNG-en-US.png) | [Torque limiting](#torque-limiting-servo) |

###### Requirement

- Deactivated V/f control.

###### Activating and configuring current setpoint filters

1. Click the button of a current setpoint filter in the screen form.

   The "Filter setting" subscreen is then displayed. Activate the required current setpoint filters and make the settings required for each filter.
2. Enter the P gain for the current setpoint filters in the "P gain" ([p1460](SINAMICS%20Parameter%20SERVO.md#p14600n-speed-controller-p-gain-adaptation-speed-lower-1)) field.
3. Enter the integral time for the current setpoint filters in the "Integral time" ([p1462](SINAMICS%20Parameter%20SERVO.md#p14620n-speed-controller-integral-time-adaptation-speed-lower-1)) field.
4. At Settings in the "Filter type" ([p1657](SINAMICS%20Parameter%20SERVO.md#p16570n-current-setpoint-filter-1-type)) drop-down list, select one of the following filter types for the 1st speed setpoint filter (see also [Filters](Configuring%20SINAMICS%20S-G-MV%20drives.md#filters)):

   - Low-pass PT1
   - Low-pass PT2
   - Bandstop
   - Low-pass with reduction
   - General 2nd order filter
5. Correct the following default values appropriate for the filter type:

   - Time constant, only for filter type "Low-pass PT1"
   - Numerator frequency, only for filter type "General 2nd order filter"
   - Numerator damping, only for filter type "General 2nd order filter"
   - Denominator frequency, for filter type "Low-pass PT2" and "General 2nd order filter"
   - Denominator damping, for filter type "Low-pass PT2" and "General 2nd order filter"
   - Blocking frequency, only for filter type "Bandstop"
   - Bandwidth, only for filter type "Bandstop"
   - Notch depth, only for filter type "Bandstop"
   - Reduction, only for filter type "Bandstop" and "Low-pass with reduction"
   - Characteristic frequency, only for filter type "Low-pass with reduction"
   - Damping, only for filter type "Low-pass with reduction"
6. Click "Accept" to take your filter settings into the current configuration.

   The filter is displayed in the current configuration.
7. To switch on the parameterized filter, activate the "Filter effective" option.

   The filter is activated in the screen form.
8. If a 2nd speed setpoint filter is to be used, repeat steps 4 ... 7.
9. Once all necessary settings have been made, click "Close".

   The dialog closes. The screen form now displays a curve for all current setpoint filters not activated previously rather than a straight line. This indicates which current setpoint filters are activated and parameterized.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855922187_DV_resource.Stream@PNG-en-US.png) | [Current controller](#current-controller-current-controller-adaptation-servo) |

###### Function diagrams (FD)

Servo control - Current control, overview - 5700 -

Servo control - Current setpoint filters 1 … 4 - 5710 -

Servo control - Current setpoint filters 5 … 10 (r0108.21 = 1) - 5711 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1650](SINAMICS%20Parameter%20SERVO.md#r1650-current-setpoint-torque-generating-before-filter-1)

---

#### Current controller

This section contains information on the following topics:

- [Current controller / current controller adaptation (servo)](#current-controller-current-controller-adaptation-servo)
- [Application example: Parameterizing the current controller adaptation](#application-example-parameterizing-the-current-controller-adaptation)

##### Current controller / current controller adaptation (servo)

###### Description

The current controller is designed as PI controller that corrects, in general, the "electrical" properties of the control loop, such as cable resistance, leakage inductance or stator resistance of the motor. These parameters are preassigned for Siemens motors. You must perform a motor data identification yourself for non-Siemens motors. The current controller is generally only required for the first commissioning. No further settings are required in normal operation.

After the first commissioning, the P gain ([p1715](SINAMICS%20Parameter%20SERVO.md#p17150n-current-controller-p-gain)) and the integral time ([p1717](SINAMICS%20Parameter%20SERVO.md#p17170n-current-controller-integral-action-time)) are preassigned, and need to be changed only when you change the parameters on the current controller, such as the current controller clock.

The settings of the controller can be further optimized for special application cases.

The following settings can be made to optimize the current controller:

- P gain
- Integral time
- Current limit
- Adaptation of the current controller

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855869963_DV_resource.Stream@PNG-en-US.png) | [Current setpoint filter](#current-setpoint-filter-servo) |
| ![Signal source](images/147855973771_DV_resource.Stream@PNG-en-US.PNG) | [Power unit](#power-unit-servo) |
| ![Signal source](images/147855973771_DV_resource.Stream@PNG-en-US.PNG) | [Power unit](#power-unit-servo) |

###### Requirement

- Deactivated V/f control.

###### Setting P gain and integral time

1. Enter the desired value for the proportional gain of the lower adaptation current range in the "P gain" (p1715[0]) field.
2. Correct the specified value for the integral time of the current controller in the "Integral time" (p1717[0]) field.

###### Configuring the current limit

1. Click the "id_set limitation" button.

   The "Current limit" dialog opens.
2. Correct the default value for the current limit in the "Current limit" ([p0640](SINAMICS%20Parameter%20SERVO.md#p06400n-current-limit)) field.

   The ramp-function generator stops at this current limit. However, the current can continue to rise.
3. Enter the maximum share of the field-generating current at the permitted maximum current in the "Maximum field-generating current" ([p1603](SINAMICS%20Parameter%20SERVO.md#p16030n-field-generating-current-maximum-1)) field.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Setting the adaptation of the current controller

The P gain of the current controller can be reduced via an adaptation depending on the current.

![Current controller adaptation](images/147855959435_DV_resource.Stream@PNG-en-US.png)

Current controller adaptation

The adaptation function must be activated first for the configuration of the adaptation.

1. Select the "[1] Yes" option ([p1402](SINAMICS%20Parameter%20SERVO.md#p14020n-closed-loop-current-control-and-motor-model-configuration-1).2) in the drop-down list below the "Adaptation" button in the "Current controller" screen form.

   The "Adaptation" button now shows a curve and can be used.
2. Click the "Adaptation" button.

   A dialog with the same name opens.
3. Correct the factor for the P gain of the current controller in the adaptation range (current &gt; [p0392](SINAMICS%20Parameter%20SERVO.md#p03920n-current-controller-adaptation-starting-point-kp-adapted)) in the "Scaling" ([p0393](SINAMICS%20Parameter%20SERVO.md#p03930n-current-controller-adaptation-p-gain-adaptation)) field.
4. Enter the application point of the current-dependent current controller adaptation at which the adapted current controller gain takes effect p1715 x p0393 in the "Application point Kp adapted" (p0392) field.
5. Enter the application point of the current-dependent current controller adaptation at which the current controller gain takes effect p1715 in the "Application point Kp" ([p0391](SINAMICS%20Parameter%20SERVO.md#p03910n-current-controller-adaptation-starting-point-kp)) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855791499_DV_resource.Stream@PNG-en-US.png) | [Power unit](#power-unit-servo) |
| ![Signal processing](images/147855791499_DV_resource.Stream@PNG-en-US.png) | [Power unit](#power-unit-servo) |

###### Function diagrams (FD)

Servo control - Current control, overview - 5700 -

Servo control - Iq and Id controllers - 5714 -

###### Additional parameters

- [r0029](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0029-reactive-current-actual-value-smoothed)
- [r0030](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0030-active-current-actual-value-smoothed)
- [r0072](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r007204-co-input-voltage)
- [r0075](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0075-co-reactive-current-setpoint)
- [r0077](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0077-co-active-current-setpoint)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r1408](SINAMICS%20Parameter%20SERVO.md#r140809-cobo-status-word-current-controller)

---

##### Application example: Parameterizing the current controller adaptation

###### Description

In order to obtain an optimum bandwidth of the closed current control loop, its p gain must be in a specific relationship to the total leakage inductance. However, generally the motor leakage inductance is not constant, and decreases with increasing torque-generating current. In order to compensate for the decreasing inductance, the converter can automatically adapt the current controller p gain using a characteristic saved in the system. The characteristic is parameterized in the converter using two interpolation points. The continuous adaptation of the current controller p gain is called "current controller adaptation". The two interpolation points are defined by the following three parameters:

- [p0391](SINAMICS%20Parameter%20SERVO.md#p03910n-current-controller-adaptation-starting-point-kp); "Application point Kp"
- [p0392](SINAMICS%20Parameter%20SERVO.md#p03920n-current-controller-adaptation-starting-point-kp-adapted); "Application point adapted"
- [p0393](SINAMICS%20Parameter%20SERVO.md#p03930n-current-controller-adaptation-p-gain-adaptation); Scaling

![Description](images/147855996939_DV_resource.Stream@PNG-en-US.png)

For Siemens motors whose setting data is called with the motor code number, the values are preassigned.

For third-party motors, the values are frequently not available.

###### Setting data for third-party motors

If the maximum active current (torque) can be applied safely to the locked motor, a procedure for determining the parameter values of the adaptation through measurements is described in the "Requirements of Third-Party Motors System Manual".

If this locked operation is not possible without risk, the determination through measurements can also be performed with current setpoint step changes, when the commissioning tool provides an appropriate functionality.

- The current control loop must first be optimized for low currents (small signal range) for the measurement.
- The adaptation must still be inactive for the measurement, e.g. through p0393 = 100%.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected motion of individual drives caused by torque step**  The current setpoint step change results in a torque step change which accelerates the motor and the coupled machine or plant components. The motor and the coupled machine or plant components must be able to be moved freely if they cannot be locked. In the worst case, the motor accelerates until the speed in the drive reaches the effective switch-off limit. In an extreme situation, death and serious injury can result in the event of an unplanned acceleration.   - To keep the movement as small as possible, current should be applied to the motor only for the short time required for the measurement of a few [ms]. - Make sure that no one is in the vicinity of the motor or machine. |  |

Based on this setting, the step responses for current setpoint step changes are recorded with increasing amplitude. If possible, the amplitude should be increased to the maximum permissible current. Frequently, a graduation in 25% steps is sufficient. 1% - 2%, 25%, 50%, 75%, 100% of the maximum current. If required, a finer graduation can be selected, e.g. 10% steps. In every step, the proportional gain can be reduced compared to the initial value so that an acceptable overshoot of 10%, for example, is produced.

If the values of the proportional gain determined in this way are applied to the active current, the parameter values of the adaptation can be defined from this characteristic as follows:

![Current controller adaptation curve](images/147856007307_DV_resource.Stream@PNG-en-US.png)

Current controller adaptation curve

After completing the measurement, the original non-reduced proportional gain is set again, the determined parameter values of the adaptation parameterized and the adaptation activated when required (e.g. [p1402](SINAMICS%20Parameter%20SERVO.md#p14020n-closed-loop-current-control-and-motor-model-configuration-1).2 = "Yes" = On = 1).

During a check measurement with this setting with current setpoint step changes of different amplitudes, there should be no significant overshoot.

###### Function diagrams (FD)

Servo control - Current control, overview - 5700 -

Servo control - Iq and Id controllers - 5714 -

###### Additional parameters

---

#### Power unit

This section contains information on the following topics:

- [Power unit (servo)](#power-unit-servo)

##### Power unit (servo)

###### Description

The operating values of the power unit are displayed in the "Power unit" screen form.

You can only change the setpoint of the pulse frequency (converter switching frequency) here.

This pulse frequency ([p1800](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1800-pulse-frequency)) must be set to the rated value of the converter at the first commissioning. The maximum possible pulse frequency is therefore determined by the power unit used. If the pulse frequency is set higher, this can result in a reduction of the maximum output current depending on the power unit.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/147855922187_DV_resource.Stream@PNG-en-US.png) | [Current controller](#current-controller-current-controller-adaptation-servo) |
| ![Signal source](images/147855922187_DV_resource.Stream@PNG-en-US.png) | [Current controller](#current-controller-current-controller-adaptation-servo) |

###### Setting the pulse frequency setpoint

1. Click the "PWM" button in the "Power unit" screen form.

   The "Power unit current operating values" dialog opens:
2. Enter the desired converter switching frequency in the "Pulse frequency setpoint" (p1800) field.
3. Check the other values in this dialog.
4. Once all necessary settings have been made, click "Close".

###### Display parameters

The following information is displayed via display parameters:

- U_set ([r0072](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r007204-co-input-voltage))

  Display and connector output for the current output voltage of the power unit (Motor Module).
- Actual current value torque-generating ([r0030](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0030-active-current-actual-value-smoothed))

  Displays the smoothed torque-generating actual current value.
- Actual current value field-generating ([r0029](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0029-reactive-current-actual-value-smoothed))

  Displays the smoothed field-generating actual current value.
- Absolute current ([r0027](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0027-co-absolute-actual-current-smoothed))

  Displays the smoothed absolute actual current value.
- Output frequency smoothed ([r0024](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0024-co-line-supply-frequency-smoothed))

  Displays the smoothed output frequency.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855922187_DV_resource.Stream@PNG-en-US.png) | [Current controller](#current-controller-current-controller-adaptation-servo) |
| ![Signal processing](images/147855922187_DV_resource.Stream@PNG-en-US.png) | [Current controller](#current-controller-current-controller-adaptation-servo) |

###### Additional parameters

- [r0037](SINAMICS%20Parameter%20CU.md#r003701-control-unit-temperature)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)

---

#### Motor encoder

This section contains information on the following topics:

- [Motor encoder (servo)](#motor-encoder-servo)
- [Application example: Parameterizing the motor encoder](#application-example-parameterizing-the-motor-encoder)

##### Motor encoder (servo)

###### Description

The parameters for the actual speed value acquisition of the motor encoder are defined via the "Motor encoder" screen form. If you deploy an encoder that has a lower resolution, it can be necessary to smooth the signal and so also improve the actual position value. The smoothing filters-out the fluctuation peaks.

###### Parameterizing the actual speed value acquisition of the motor encoder

1. If you want to smooth fluctuation peaks in the actual speed value, enter a smoothing time constant in the "Smoothing" ([p1441](SINAMICS%20Parameter%20SERVO.md#p14410n-actual-speed-smoothing-time-1)) field.

   If required, you can use a trace to check whether the controller with the smoothing is still sufficiently dynamic.
2. If you want to change the weighting of the load speed to the motor speed, click the "Encoder mixing" button.

   A dialog with the same name opens.
3. Enter the desired weighting factor in the "Load speed / motor speed" ([p3702](SINAMICS%20Parameter%20SERVO.md#p37020n-apc-load-speedmotor-speed-weighting)) field.
4. Once all necessary settings have been made, click "Close".

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/147855522443_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#speed-controller) |

###### Additional parameters

- [r0061](SINAMICS%20Parameter%20SERVO.md#r006101-co-actual-speed-unsmoothed-1)
- [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)

---

##### Application example: Parameterizing the motor encoder

###### Actual speed value via the motor encoder

If you deploy an encoder that has a lower resolution, such as a resolver with pole pair count "2", it can be necessary to smooth the signal and so also improve the actual position value. The smoothing filters out the fluctuation peaks.

If the actual speed value resolution is too low, faults such as noises in the motor can result.

###### Smoothing the actual speed value

The actual speed value is smoothed using a PT1 filter. Note that a longer smoothing time reduces the dynamic response and so makes the controller softer.

1. Enter the "smoothing time" ([p1441](SINAMICS%20Parameter%20SERVO.md#p14410n-actual-speed-smoothing-time-1)).
2. After changing the smoothing time, check whether the controller is still sufficiently dynamic.
3. If necessary, trace the actual speed value (unsmoothed) [r0061](SINAMICS%20Parameter%20SERVO.md#r006101-co-actual-speed-unsmoothed-1) in the trace and check the quality by fetching the smoothed actual speed value ([r0022](SINAMICS%20Parameter%20SERVO.md#r0022-speed-actual-value-rpm-smoothed-1)).
4. If the controller is no longer sufficiently dynamic, reduce the smoothing time.

   If the actual speed value is still too poor, you can deploy a second encoder with better resolution as actual speed value source.

###### Encoderless operation

When high quality spindles are operating at high speed, it is possible that the encoder evaluation is too slow. The LED display indicates that the controller has been changed to encoderless operation. The changeover frequency is set at "Torque setpoints" ([p1404](SINAMICS%20Parameter%20SERVO.md#p14040n-encoderless-operation-changeover-speed-1)).

###### Function diagrams (FD)

Encoder evaluation - Speed actual value and pole position sensing encoder 1 - 4710 -

###### Additional parameters

- [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)
- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)

---

---

**See also**

[Motor encoder (servo)](#motor-encoder-servo)
  
[Torque setpoints (servo)](#torque-setpoints-servo)

### Drive functions

This section contains information on the following topics:

- [Faults](#faults)
- [Brake control](#brake-control)
- [DC brake](#dc-brake)
- [Messages/monitoring](#messagesmonitoring)
- [Friction characteristic](#friction-characteristic)

#### Faults

##### General information

If a fault occurs, the drive indicates the corresponding fault and/or alarm.

The following options for displaying faults and alarms are available:

- Display via the fault and alarm buffer for PROFINET.
- Display online via the commissioning software.
- Display and operating unit (e.g. BOP, AOP).

##### Differences between faults and alarms

The differences between faults and alarms are as follows:

| Type | Description |
| --- | --- |
| Faults | - What happens when a fault occurs?    - The appropriate fault response is initiated.   - Status signal ZSW1.3 is set.   - The fault is entered in the fault buffer. - How are faults corrected?    - Eliminate the cause of the fault.   - Acknowledge the fault. |
| Alarms | - What happens when an alarm occurs?    - Status signal ZSW1.7 is set.   - The alarm is entered in the alarm buffer. - How are alarms corrected?    - Alarms acknowledge themselves.      When the cause is no longer present, they automatically reset themselves. |

##### Fault responses

The following table contains the fault responses and their meanings for the entire SINAMICS drive family.

| Fault response | PROFIdrive | Response | Description |
| --- | --- | --- | --- |
| NONE | - | None | No response when a fault occurs.   When the "Basic positioner" function module is activated ([r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1).4 = 1), the following applies: When a fault occurs with fault response "NONE", an active motion command is aborted and the system switches to follow-up mode until the fault has been rectified and acknowledged. |
| OFF1 | ON/OFF | Brake along the ramp-function generator deceleration ramp followed by pulse disable | - Speed control ([p1300](SINAMICS%20Parameter%20SERVO.md#p13000n-open-loopclosed-loop-control-operating-mode-1) = 20, 21)    - The immediate specification of n_set = 0 at the ramp generator deceleration ramp ([p1121](SINAMICS%20Parameter%20SERVO.md#p11210n-ramp-function-generator-ramp-down-time-2)) causes the drive to be braked.   - When standstill is detected, the motor holding brake (if parameterized) is closed ([p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration)). The pulses are suppressed after the closing time ([p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time)) has expired.      Standstill is detected when the actual speed value falls below the speed threshold ([p1226](SINAMICS%20Parameter%20SERVO.md#p12260n-threshold-for-zero-speed-detection-1)) or when the monitoring time ([p1227](SINAMICS%20Parameter%20SERVO.md#p1227-zero-speed-detection-monitoring-time)) started when speed setpoint ≤ speed threshold (p1226) has expired. - Torque control (p1300 = 23)   - The following applies for torque control: Response as for OFF2.   - When switching to torque control via [p1501](SINAMICS%20Parameter%20SERVO.md#p15010n-bi-change-over-between-closed-loop-speedtorque-control-1), the following applies:      There is no separate braking response.      If the actual speed value falls below the speed threshold (p1226) or the timer (p1227) has expired, the motor holding brake (if available) is closed. The pulses are suppressed after the closing time (p1217) has expired. |
| OFF1_DELAYED | - | As for OFF1, but delayed | Faults with this fault response only take effect after the delay time in p3136 has expired. The remaining time until OFF1 is displayed in r3137. |
| OFF2 | COAST STOP | Internal/external pulse disable | Speed control and torque control   - Immediate pulse suppression, the drive "coasts" to a standstill. - The motor holding brake (if available) is closed immediately. - The "switching on disabled" is activated. |
| OFF3 | QUICK STOP | Brake along the OFF3 deceleration ramp followed by pulse disable | - Speed control (p1300 = 20, 21)    - The drive is braked along the OFF3 deceleration ramp ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)) by immediately entering n_set = 0.   - When standstill is detected, the motor holding brake (if parameterized) is closed. The pulses are suppressed when the closing time of the holding brake (p1217) expires.      Standstill is detected when the actual speed value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint &lt;= speed threshold (p1226) has expired.   - The "switching on disabled" is activated. - Torque control (p1300 = 23)    - Switchover to speed-controlled operation and other responses as described for speed-controlled operation. |
| STOP2 | - | n_set = 0 | - The drive is braked along the OFF3 deceleration ramp (p1135) by immediately entering n_set = 0. - The drive remains in speed control. |
| IASC/DCBRK | - | - | - For synchronous motors, the following applies:    - If a fault occurs with this fault response, an internal armature short-circuit is triggered.   - The conditions for [p1231](SINAMICS%20Parameter%20SERVO.md#p12310n-armature-short-circuit-dc-braking-configuration) = 4 must be observed. - For induction motors, the following applies:    - If a fault occurs with this fault response, DC braking is triggered.   - DC braking must have been commissioned ([p1232](SINAMICS%20Parameter%20SERVO.md#p12320n-dc-braking-braking-current), [p1233](SINAMICS%20Parameter%20SERVO.md#p12330n-dc-braking-time), [p1234](SINAMICS%20Parameter%20SERVO.md#p12340n-speed-at-the-start-of-dc-braking-1)). |
| ENCODER | - | Internal/external pulse disable ([p0491](SINAMICS%20Parameter%20SERVO.md#p0491-motor-encoder-fault-response-encoder)) | The ENCODER fault response is applied depending on the setting in p0491.   - Factory setting: p0491 = 0 → encoder error results in OFF2     **Notice**    When changing p0491, it is imperative that the information in the description of this parameter is observed. |

##### Acknowledging faults

For each fault, there is a description of how to acknowledge the fault after the cause has been eliminated.

| Acknowledgment | Description |
| --- | --- |
| POWER ON | The fault is acknowledged via a POWER ON (switch drive unit off and on again).    **Note**    If the fault cause has not been eliminated, the fault is displayed again immediately after ramp-up. |
| IMMEDIATELY | Faults can be acknowledged on a single drive object (steps 1 to 3) or on all drive objects (step 4) as follows:   1. Acknowledging via parameter:      [p3981](SINAMICS%20Parameter%20CU.md#p3981-acknowledge-drive-object-faults) = 0 → 1 2. Acknowledging via binector inputs:      [p2103](SINAMICS%20Parameter%20CU.md#p2103-bi-1st-acknowledge-faults) BI: 1. Acknowledge faults     [p2104](SINAMICS%20Parameter%20CU.md#p2104-bi-2nd-acknowledge-faults) BI: 2. Acknowledge faults      [p2105](SINAMICS%20Parameter%20CU.md#p2105-bi-3rd-acknowledge-faults) BI: 3. Acknowledge faults 3. Acknowledging via PROFIBUS control signal:     STW1.7 = 0 → 1 (edge) 4. Acknowledging all faults      [p2102](SINAMICS%20Parameter%20CU.md#p2102-bi-acknowledge-all-faults-1) BI: Acknowledging all faults     All of the faults on all of the drive objects of the drive system can be acknowledged via this binector input.    **Note**   - These faults can also be acknowledged by a POWER ON. - If the fault cause has not been eliminated, the fault is deleted after the acknowledgment. - Safety Integrated faults    The "Safe Torque Off" (STO) function must be deselected before these faults are acknowledged. |
| PULSE DISABLE | The fault can only be acknowledged with a pulse disable ([r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1).11 = 0).   The same options are available for acknowledging as described under acknowledge IMMEDIATELY. |

##### Additional parameters

---

#### Brake control

This section contains information on the following topics:

- [Overview](#overview-2)
- [Simple brake control (servo)](#simple-brake-control-servo)
- [Extended brake control (servo)](#extended-brake-control-servo)

##### Overview

The SINAMICS drives (S120, S150, G150, G130) are equipped with a brake control for motor holding brakes.

The brake control is only used for the control of motor holding brakes. A differentiation is made between mechanically braking and electrically braking a motor:

- Mechanical brakes are generally motor holding brakes that are closed when the motor is at a standstill.
- Mechanical operating brakes that are closed while the motor is rotating are subject to a high wear and are therefore often only used as an emergency brake.
- The motor is electrically braked by the converter. An electrical braking is completely wear-free.

Generally, a motor is switched off at standstill in order to save energy and so that the motor temperature is not unnecessarily increased. Drives that have been switched off, can be secured against unwanted motion by the holding brake.

The converter-internal control of the motor holding brake is suitable typically for horizontal, inclined and vertical conveyors. A motor holding brake can also be useful in several applications for pumps or fans to ensure that the switched-off motor does not rotate in the wrong direction due to a liquid or air flow.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Destruction of the holding brake due to incorrect parameter assignment**  If the drive moves against the closed holding brake, this can destroy the holding brake and cause death or serious injury.   - Do not set the parameter assignment p1215 = 0 when there is a holding brake. - Set all the relevant parameters correctly. |  |

---

**See also**

[Simple brake control (servo)](#simple-brake-control-servo)
  
[Extended brake control (servo)](#extended-brake-control-servo)

##### Simple brake control (servo)

This section contains information on the following topics:

- [Basics](#basics)
- [Parameterizing the brake control](#parameterizing-the-brake-control)
- [Opening the brake](#opening-the-brake)
- [Closing the brake](#closing-the-brake)

###### Basics

The "Simple brake control" is used exclusively for the control of holding brakes. Drives that have been switched off, can be secured against unwanted motion by the holding brake.

The trigger command for releasing and applying the holding brake is transmitted via DRIVE-CLiQ from the Control Unit, which monitors and logically connects the signals to the system-internal processes, directly to the Motor Module.

The Motor Module then performs the action and activates the output for the holding brake. The exact sequence control is shown in function diagrams 2701 and 2704 (see SINAMICS S120/S150 List Manual). The operating principle of the holding brake can be configured via parameter [p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration).

![Sequence diagram, simple brake control](images/147856189195_DV_resource.Stream@PNG-en-US.png)

Sequence diagram, simple brake control

The start of the closing time for the brake depends on the expiration of the shorter of the two times [p1227](SINAMICS%20Parameter%20SERVO.md#p1227-zero-speed-detection-monitoring-time) (standstill detection monitoring time) and [p1228](SINAMICS%20Parameter%20SERVO.md#p1228-pulse-suppression-delay-time) (pulse cancellation delay time).

###### Features

- Automatic activation by means of sequence control
- Standstill monitoring
- Forced brake opening ([p0855](SINAMICS%20Parameter%20SERVO.md#p08550n-bi-unconditionally-release-holding-brake), p1215)
- Closing of brake for a 1 signal "unconditionally close holding brake" ([p0858](SINAMICS%20Parameter%20SERVO.md#p08580n-bi-unconditionally-close-holding-brake-1))
- Closing of brake after the "Enable speed controller" signal has been canceled ([p0856](SINAMICS%20Parameter%20SERVO.md#p08560n-bi-enable-speed-controller-1))

###### Commissioning

Simple brake control is activated automatically (p1215 = 1) when the Motor Module has an internal brake control and a connected brake has been found.

If no internal brake control is available, the control can be activated using a parameter (p1215 = 3).

> **Note**
>
> It is only permissible to activate brake control monitoring for Booksize power units ([p1278](SINAMICS%20Parameter%20SERVO.md#p1278-brake-control-diagnostics-evaluation) = 0).

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

Brake control - Extended brake control, open/close brake (r0108.14 = 1) - 2707 -

Brake control - Extended brake control, signal outputs (r0108.14 = 1) - 2711 -

###### Additional parameters

- [r0056](SINAMICS%20Parameter%20SERVO.md#r0056115-cobo-status-word-closed-loop-control)
- [r0060](SINAMICS%20Parameter%20SERVO.md#r0060-co-speed-setpoint-before-the-setpoint-filter-1)
- [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)
- r0063
- [r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1)
- p0856
- p0858
- [r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1)
- p1215
- [p1216](SINAMICS%20Parameter%20SERVO.md#p1216-motor-holding-brake-opening-time)
- [p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time)
- [p1226](SINAMICS%20Parameter%20SERVO.md#p12260n-threshold-for-zero-speed-detection-1)
- p1227
- p1228

---

###### Parameterizing the brake control

###### Selecting the type of brake control

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Destruction of the holding brake due to incorrect parameter assignment**  If the drive moves against the closed holding brake, this can destroy the holding brake and cause death or serious injury.   - Do **not** set the parameter assignment [p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration) = 0 when there is a holding brake. - Set all the relevant parameters correctly. |  |

To select the type of brake control, proceed as follows:

1. Select one of the following entries from the drop-down list:

   - Motor holding brake like sequence control (p1215 = 1)

     If the configuration is set to "No motor holding brake available" during ramp-up, then an automatic identification of the motor holding brake is performed. If a motor holding brake is detected, the configuration is set to "Motor holding brake the same as sequence control".
   - Motor holding brake always open (p1215 = 2)
   - Motor holding brake like sequence control, connection via BICO (p1215 = 3)

     If a motor holding brake is used via the drive-integrated brake connection of the Motor Module, this option must not be set. If an external motor holding brake is used, p1215 = 3 should be set and [r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1).12 connected as control signal. With activated "Extended brake control" ([r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1).14 = 1) function module, [r1229](SINAMICS%20Parameter%20SERVO.md#r1229111-cobo-motor-holding-brake-status-word).1 should be connected as control signal.

###### Parameterizing the "Motor holding brake like sequence control" option

To parameterize the "Motor holding brake like sequence control" option, proceed as follows:

1. Set the opening time of the brake ([p1216](SINAMICS%20Parameter%20SERVO.md#p1216-motor-holding-brake-opening-time)).

   After activating the holding brake (opening), the speed/velocity setpoint zero is active during this time. The speed/velocity setpoint is then enabled after this time.

   The time should be set greater than the actual opening time of the brake. The drive does not then accelerate when the brake is closed.
2. Set the closing time of the brake ([p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time)).

   The drive still remains in closed-loop control at standstill with speed/velocity setpoint zero after OFF1 or OFF3 and activation of the holding brake (closing). The pulses are suppressed when this time expires.

   The time should be set greater than the actual closing time of the brake. In this way, the pulses are only suppressed when the brake is closed.
3. To open the "[Opening the brake](#opening-the-brake)" dialog, click the "Open brake" button.

   Make the required settings in the dialog.
4. Connect the "Open brake command" ([p0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1).12) signal sink with the required parameters. Several connections are possible.
5. To open the "[Closing the brake](#closing-the-brake)" dialog, click the "Close brake" button.

   Make the required settings in the dialog.
6. Connect the "Close brake command" (p0899.13) signal sink with the required parameters. Several connections are possible.

The "Open brake" and "Close brake" settings are processed logically via the flip-flop. The "Open brake" and "Close brake" signals are then present at the outputs of the flip-flop.

###### The "Motor holding brake always open" option

There are no further setting options for the "Motor holding brake always open" option. The state of the holding brake is displayed in the dialog.

###### Parameterizing the "Motor holding brake like sequence control, connection via BICO" option

To parameterize the "Motor holding brake like sequence control, connection via BICO" option, proceed as follows:

1. Set the opening time of the brake (p1216).

   After activating the holding brake (opening), the speed/velocity setpoint zero is active during this time. The speed/velocity setpoint is then enabled after this time.

   The time should be set greater than the actual opening time of the brake. The drive does not then accelerate when the brake is closed.
2. Set the closing time of the brake (p1217).

   The drive still remains in closed-loop control at standstill with speed/velocity setpoint zero after OFF1 or OFF3 and activation of the holding brake (closing). The pulses are suppressed when this time expires.

   The time should be set greater than the actual closing time of the brake. In this way, the pulses are only suppressed when the brake is closed.
3. To open the "[Opening the brake](#opening-the-brake)" dialog, click the "Open brake" button.

   Make the required settings in the dialog.
4. Connect the "Open brake command" (p0899.12) signal sink with the required parameters. Several connections are possible.
5. To open the "[Closing the brake](#closing-the-brake)" dialog, click the "Close brake" button.

   Make the required settings in the dialog.
6. Connect the "Close brake command" (p0899.13) signal sink with the required parameters. Several connections are possible.

The "Open brake" and "Close brake" settings are processed logically via the flip-flop. The "Open brake" and "Close brake" signals are then present at the outputs of the flip-flop.

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

Brake control - Extended brake control, open/close brake (r0108.14 = 1) - 2707 -

Brake control - Extended brake control, signal outputs (r0108.14 = 1) - 2711 -

###### Additional parameters

- [p0855](SINAMICS%20Parameter%20SERVO.md#p08550n-bi-unconditionally-release-holding-brake)
- p0899

---

###### Opening the brake

To parameterize the command for the forced opening of the brake, proceed as follows:

1. Interconnect the "Unconditionally open holding brake" ([p0855](SINAMICS%20Parameter%20SERVO.md#p08550n-bi-unconditionally-release-holding-brake)) signal source for the command to open the brake unconditionally.

   The brake opens when this signal or the internal signal "Open brake" has the value "1".

> **Note**
>
> The "Unconditionally close holding brake" signal has a higher priority than the "Unconditionally open holding brake" signal.

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

###### Additional parameters

---

###### Closing the brake

To assign the parameters that influence the closing of the brake, proceed as follows:

1. Enter the speed threshold at which "Standstill" is identified when the threshold is undershot in the "Threshold" ([p1226](SINAMICS%20Parameter%20SERVO.md#p12260n-threshold-for-zero-speed-detection-1)) field.

   When this threshold is undershot, the brake control is started and the closing time in [p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time) awaited. The pulses are then suppressed.
2. Enter the delay time for pulse suppression in the "Delay time" ([p1228](SINAMICS%20Parameter%20SERVO.md#p1228-pulse-suppression-delay-time)) field.

   The pulses are suppressed after OFF1 or OFF3 when at least one of the following conditions has been satisfied:

   - The actual speed value falls below the threshold in p1226 and the time started in p1228 has expired.
   - The speed setpoint falls below the threshold in p1226 and the time started in [p1227](SINAMICS%20Parameter%20SERVO.md#p1227-zero-speed-detection-monitoring-time) has expired.
3. Enter the monitoring time for standstill detection in the "Monitoring time" (p1227) field.

   When braking with OFF1 or OFF3, standstill is detected after this time has expired, after the set speed has fallen below p1226. The brake control is then started, the closing time in p1217 awaited and the pulses suppressed.
4. Connect the "Unconditionally close brake" ([p0858](SINAMICS%20Parameter%20SERVO.md#p08580n-bi-unconditionally-close-holding-brake-1)) signal source for the command to unconditionally close the brake.

**Note**

The "Unconditionally close holding brake" signal has a higher priority than the "Unconditionally open holding brake" signal.

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

###### Additional parameters

- p0858
- [p0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1)

---

##### Extended brake control (servo)

This section contains information on the following topics:

- [Basics](#basics-1)
- [Parameterizing extended brake control](#parameterizing-extended-brake-control)
- [Opening the brake](#opening-the-brake-1)
- [Closing the brake](#closing-the-brake-1)

###### Basics

###### Description

The "Extended brake control" allows complex brake controls, such as for motor holding brakes and service brakes. The brake is controlled in the following manner. The order represents the priority:

- Via parameter [p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration)
- Via binectors [p1219](SINAMICS%20Parameter%20SERVO.md#p121903-bi-immediately-close-motor-holding-brake)[0...3] and [p0855](SINAMICS%20Parameter%20SERVO.md#p08550n-bi-unconditionally-release-holding-brake)
- Via standstill detection
- Via the connector connection threshold

###### Requirement

- The "Extended brake control" function module is activated (see [Function modules (servo)](#function-modules-servo)).

###### Features

- Forced brake opening (p0855, p1215)
- Closing of brake for a 1 signal "unconditionally close holding brake" ([p0858](SINAMICS%20Parameter%20SERVO.md#p08580n-bi-unconditionally-close-holding-brake-1))
- Binector inputs for opening or closing the brake ([p1218](SINAMICS%20Parameter%20SERVO.md#p121801-bi-open-motor-holding-brake), p1219)
- Connector input for the threshold for opening and closing the brake ([p1220](SINAMICS%20Parameter%20SERVO.md#p1220-ci-open-motor-holding-brake-signal-source-threshold))
- OR/AND block each with two inputs ([p1279](SINAMICS%20Parameter%20SERVO.md#p127903-bi-motor-holding-brake-orand-logic-operation), [r1229](SINAMICS%20Parameter%20SERVO.md#r1229111-cobo-motor-holding-brake-status-word).10, r1229.11)
- Holding and service brakes can be activated
- Monitoring of the brake feedback signals (r1229.4, r1229.5)
- Configurable responses (A07931, A07932)
- Closing of brake after the "Enable speed controller" signal has been canceled ([p0856](SINAMICS%20Parameter%20SERVO.md#p08560n-bi-enable-speed-controller-1))

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

Brake control - Extended brake control, open/close brake (r0108.14 = 1) - 2707 -

Brake control - Extended brake control, signal outputs (r0108.14 = 1) - 2711 -

###### Additional parameters

- [r0056](SINAMICS%20Parameter%20SERVO.md#r0056115-cobo-status-word-closed-loop-control)
- [r0060](SINAMICS%20Parameter%20SERVO.md#r0060-co-speed-setpoint-before-the-setpoint-filter-1)
- [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)
- r0063
- [r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1)
- p0856
- p0858
- [r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1)
- p1215
- [p1216](SINAMICS%20Parameter%20SERVO.md#p1216-motor-holding-brake-opening-time)
- [p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time)
- [p1226](SINAMICS%20Parameter%20SERVO.md#p12260n-threshold-for-zero-speed-detection-1)
- [p1227](SINAMICS%20Parameter%20SERVO.md#p1227-zero-speed-detection-monitoring-time)
- [p1228](SINAMICS%20Parameter%20SERVO.md#p1228-pulse-suppression-delay-time)

---

---

**See also**

[Parameterizing the brake control](#parameterizing-the-brake-control)

###### Parameterizing extended brake control

When braking with feedback ([p1275](SINAMICS%20Parameter%20SERVO.md#p1275-motor-holding-brake-control-word).5 = 1), the braking control responds to the feedback contacts of the brake. If the period [p1216](SINAMICS%20Parameter%20SERVO.md#p1216-motor-holding-brake-opening-time) is longer than the time until the feedback signal comes, the startup is delayed by the associated time difference.

In order to startup without delay when possible, the set period p1216 must be shorter than the time until the feedback signal comes. If the period is set shorter, the alarm "A07931, brake does not open" appears, however.

###### Selecting the type of brake control

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Destruction of the holding brake due to incorrect parameter assignment**  If the drive moves against the closed holding brake, this can destroy the holding brake and cause death or serious injury.   - Do **not** set the parameter assignment [p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration) = 0 when there is a holding brake. - Set all the relevant parameters correctly. |  |

To select the type of brake control, proceed as follows:

1. Select one of the following entries from the drop-down list:

   - Motor holding brake like sequence control (p1215 = 1)

     If the configuration is set to "No motor holding brake available" during ramp-up, then an automatic identification of the motor holding brake is performed. If a motor holding brake is detected, the configuration is set to "Motor holding brake the same as sequence control".
   - Motor holding brake always open (p1215 = 2)

     No further configuration necessary.
   - Motor holding brake like sequence control, connection via BICO (p1215 = 3)

     If a motor holding brake is used via the drive-integrated brake connection of the Motor Module, this option must not be set. If an external motor holding brake is used, p1215 = 3 should be set and [r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1).12 connected as control signal. With activated "Extended brake control" ([r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1).14 = 1) function module, [r1229](SINAMICS%20Parameter%20SERVO.md#r1229111-cobo-motor-holding-brake-status-word).1 should be connected as control signal.

###### Basic parameterizing selected brake control

1. Set the opening time of the brake (p1216).

   After activating the holding brake (opening), the speed/velocity setpoint zero is active during this time. The speed/velocity setpoint is then enabled after this time.

   The time should be set greater than the actual opening time of the brake. The drive does not then accelerate when the brake is closed.
2. Set the closing time of the brake ([p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time)).

   The drive still remains in closed-loop control at standstill with speed/velocity setpoint zero after OFF1 or OFF3 and activation of the holding brake (closing). The pulses are suppressed when this time expires.

   The time should be set greater than the actual closing time of the brake. In this way, the pulses are only suppressed when the brake is closed.
3. To open the "[Opening the brake](#opening-the-brake-1)" dialog, click the "Open brake" button.

   Make the required settings in the dialog.
4. Interconnect the "Open brake command" (r0899.12) signal sink to the required parameters. Several connections are possible.
5. To open the "[Closing the brake](#closing-the-brake-1)" dialog, click the "Close brake" button.

   Make the required settings in the dialog.
6. Interconnect the "Close brake command" (r0899.13) signal sink to the required parameters. Several connections are possible.

###### Making settings for the brake feedback

1. Select the "[1] Yes" setting in the "Brake with feedback" (p1275.5) drop-down list.

   The screen form then expands downwards with the additional settings.
2. Interconnect the "Brake open feedback" ([p1223](SINAMICS%20Parameter%20SERVO.md#p1223-bi-motor-holding-brake-feedback-signal-brake-open)) signal source for the "Brake open" feedback.
3. Interconnect the "Brake closed feedback" ([p1222](SINAMICS%20Parameter%20SERVO.md#p1222-bi-motor-holding-brake-feedback-signal-brake-closed)) signal source for the "Brake closed" feedback.
4. Click the "Status word" button. A screen form with the same name opens.

   Interconnect the signal sources for the following areas:

   - Status word sequence control (r0899)
   - Motor holding brake status word (r1229)
5. Click the "Logic operations" button in the "Brake control" screen form.

   The "Brake logic operations" dialog opens.

   - Interconnect the signal sources for "OR operation" or for "AND operations".
   - Once all necessary settings have been made, click "Close".

###### Additional parameters

---

###### Opening the brake

###### Parameterizing the "Open brake" command

To parameterize for extended brake control the command for the forced opening of the brake, proceed as follows:

1. Interconnect the "Open threshold signal source" ([p1220](SINAMICS%20Parameter%20SERVO.md#p1220-ci-open-motor-holding-brake-signal-source-threshold)) signal source for the "Open brake" command.
2. Enter the threshold for the "Open brake" command in the "Open threshold" ([p1221](SINAMICS%20Parameter%20SERVO.md#p1221-open-motor-holding-brake-threshold)) field.
3. Enter the monitoring time for standstill detection in the "Monitoring time" ([p1227](SINAMICS%20Parameter%20SERVO.md#p1227-zero-speed-detection-monitoring-time)) field.

   When braking with OFF1 or OFF3, standstill is detected after this time has expired, after the set speed has fallen below [p1226](SINAMICS%20Parameter%20SERVO.md#p12260n-threshold-for-zero-speed-detection-1).
4. Interconnect the "Open motor holding brake" ([p1218](SINAMICS%20Parameter%20SERVO.md#p121801-bi-open-motor-holding-brake)[0]) signal source for conditional opening operation of the motor holding brake and also an AND operation with input 1.

   AND/OR

   Interconnect the "Open motor holding brake" (p1218[1]) signal source for conditional opening operation of the motor holding brake and also an AND operation with input 2.
5. Interconnect the "Unconditionally open holding brake" ([p0855](SINAMICS%20Parameter%20SERVO.md#p08550n-bi-unconditionally-release-holding-brake)) signal source for the command to open the brake unconditionally.

   The brake opens when this signal or the internal signal "Open brake" has the value "1".

> **Note**
>
> The "Unconditionally close holding brake" signal has a higher priority than the "Unconditionally open holding brake" signal.

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

###### Additional parameters

---

###### Closing the brake

###### Parameterizing the "Close brake" command

To assign the parameters that influence the closing of the brake, proceed as follows:

1. Interconnect the signal source for the following options of the "Close motor holding brake at standstill" function:

   - [p1224](SINAMICS%20Parameter%20SERVO.md#p122403-bi-close-motor-holding-brake-at-standstill)[0]: Close brake at standstill signal, inversion via [p1275](SINAMICS%20Parameter%20SERVO.md#p1275-motor-holding-brake-control-word).2
   - p1224[1]: Close brake at standstill signal, inversion via p1275.3
   - p1224[2]: Close brake at standstill signal
   - p1224[3]: Close brake at standstill signal

   These four signals form an OR operation.
2. Interconnect the signal sources for the following options of the "Close motor holding brake immediately" function:

   - [p1219](SINAMICS%20Parameter%20SERVO.md#p121903-bi-immediately-close-motor-holding-brake)[0]: Close brake immediately signal, inversion via p1275.0
   - p1219[1]: Close brake immediately signal, inversion via p1275.1
   - p1219[2]: Close brake immediately signal
   - p1219[3]: Close brake immediately signal according to [r1229](SINAMICS%20Parameter%20SERVO.md#r1229111-cobo-motor-holding-brake-status-word).9

   These four signals form an OR operation.
3. Interconnect the "Unconditionally close brake" ([p0858](SINAMICS%20Parameter%20SERVO.md#p08580n-bi-unconditionally-close-holding-brake-1)[0]) signal source for the "Unconditionally close brake" command.

**Note**

The "Unconditionally close holding brake" signal has a higher priority than the "Unconditionally open holding brake" signal.

###### Configuring standstill detection

The standstill detection is configured in a separate dialog. You can decide for the standstill detection whether a deceleration ramp for the monitoring time is to be used in addition. In the latter case, the brake, however, can close for a turning motor.

1. Click the "Standstill detection" button on the "Close brake" screen form.

   A setting dialog with the same name opens. The "Deceleration ramp monitoring time" option is initialized with the "ON" option.
2. Optional: Select the "OFF" option in the "Deceleration ramp monitoring time" drop-down list. In this case, the input field for the monitoring time is hidden.
3. Interconnect the "Standstill detection threshold" ([p1225](SINAMICS%20Parameter%20SERVO.md#p1225-ci-standstill-detection-threshold-value)) signal source for the standstill detection.
4. Enter the speed threshold for standstill detection in the "Threshold" ([p1226](SINAMICS%20Parameter%20SERVO.md#p12260n-threshold-for-zero-speed-detection-1)[0]) field.
5. Enter the delay time for pulse suppression in the "Delay time" ([p1228](SINAMICS%20Parameter%20SERVO.md#p1228-pulse-suppression-delay-time)) field.
6. Enter the monitoring time for standstill detection in the "Monitoring time" ([p1227](SINAMICS%20Parameter%20SERVO.md#p1227-zero-speed-detection-monitoring-time)) field.

   This step is omitted if the deceleration ramp has been switched off in step 2.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Configuring disable standstill detection

If you want to disable standstill detection, proceed as follows:

1. Select the "ON" entry in the "Disable standstill detection" drop-down list.
2. Enter the deceleration time for closing the brake at standstill in the "Disable standstill detection" ([p1276](SINAMICS%20Parameter%20SERVO.md#p1276-motor-holding-brake-standstill-detection-bypass)) input field below the graphic.

###### Function diagrams (FD)

Brake control - Simple brake control (r0108.14 = 0) - 2701 -

Brake control - Extended brake control, standstill detection (r0108.14 = 1) - 2704 -

###### Additional parameters

- p0858
- [p0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1)

---

#### DC brake

This section contains information on the following topics:

- [Overview](#overview-3)
- [Armature short-circuit brake (servo)](#armature-short-circuit-brake-servo)
- [DC braking for OFF1/OFF3 (servo)](#dc-braking-for-off1off3-servo)
- [DC braking below starting speed (servo)](#dc-braking-below-starting-speed-servo)
- [Fault responses (servo)](#fault-responses-servo)
- [Current controller (servo)](#current-controller-servo)

##### Overview

You can parameterize either "DC braking" or "Armature short-circuit braking" via the "DC brake" screen form irrespective of the motor type.

###### Armature short-circuit

Using this function, you can brake permanent-magnet synchronous motors. The stator windings of synchronous motors are then short-circuited. For a rotating synchronous motor, a current flows that brakes the motor.

Armature short-circuit is preferably used in the following cases:

- If braking is to be performed without feedback
- If braking is to be performed when the power fails
- If an infeed is used that is not capable of feedback
- If with orientation loss (e.g. with encoder errors), the motor should still be braked

You can switch the armature short-circuit internally via the Motor Module or externally using a contactor circuit with braking resistors.

The advantage of armature short-circuit braking over a mechanical brake is the response time of the internal armature short-circuit braking with just a few milliseconds. The response time of a mechanical brake is about 40 ms. For external armature short-circuit braking, the inertia of the switching contactor results in a response time of over 60 ms.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Motor accelerates uncontrollably for pulling loads**  With pulling loads, for an armature short-circuit, the motor can uncontrollably accelerate if a mechanical brake is not additionally used. If the motor accelerates uncontrollably this can result in severe injury or death.  - With pulling loads, only use armature short-circuit braking to support a mechanical brake (a mechanical brake is mandatory). |  |

###### DC braking

Using this function, you can brake induction motors down to standstill. With DC braking, a DC current is injected in the stator windings of the induction motor.

DC braking is preferred in case of danger:

- If it is not possible to ramp-down the drive in a controlled fashion
- If an infeed not capable of feedback is used
- If no braking resistor is used

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Motor accelerates uncontrollably for pulling loads**  With pulling loads, when DC braking is used, during the demagnetization time the motor can accelerate uncontrollably. This can result in severe injury or death. An additional supporting mechanical brake is only closed after the demagnetization time - when the motor is already rotating - and therefore does not prevent the motor from accelerating uncontrollably.  - Do not use DC braking for pulling loads. |  |

###### Function diagrams (FD)

Technology functions - External armature short-circuit (EASC, p0300 = 2xx or 4xx) - 7014 -

Technology functions - Internal armature short-circuit (IASC, p0300 = 2xx or 4xx) - 7016 -

Technology functions - DC braking (p0300 = 1xx) - 7017 -

###### Additional parameters

---

##### Armature short-circuit brake (servo)

With the internal armature short-circuit braking, the motor windings are short-circuited using the Motor Module.

###### Requirements

- Motor Modules of the Booksize or Chassis format
- Short-circuit-proof motors ([p0320](SINAMICS%20Parameter%20SERVO.md#p03200n-motor-rated-magnetizing-currentshort-circuit-current) &lt; [p0323](SINAMICS%20Parameter%20SERVO.md#p03230n-maximum-motor-current))
- One of the following motor types is used:

  - Rotary permanent-magnet synchronous motor ([p0300](SINAMICS%20Parameter%20SERVO.md#p03000n-motor-type-selection-2) = 2xx)
  - Linear permanent-magnet synchronous motor (p0300 = 4xx)
- The maximum current of the Motor Module ([r0209](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r020904-power-unit-maximum-current).0) must be at least 1.8-times the motor short-circuit current ([r0331](SINAMICS%20Parameter%20SERVO.md#r03310n-actual-motor-magnetizing-currentshort-circuit-current)).

  > **Note**
  >
  > **Internal short-circuit braking despite power failure**
  >
  > If armature short-circuit braking should still be maintained despite a power failure, you must buffer the 24 V power supply for the Motor Module. For this purpose, you can use, for example, a dedicated SITOP unit for the Motor Module or a Control Supply Module (CSM).

###### Procedure

1. Select the "[4] Internal armature short-circuit/DC braking" option in the "Braking configuration" drop-down list.
2. Enter the desired braking current value in the "Braking current" ([p1232](SINAMICS%20Parameter%20SERVO.md#p12320n-dc-braking-braking-current)) field.
3. Enter an appropriate time in the "Motor de-excitation time" ([p0347](SINAMICS%20Parameter%20SERVO.md#p03470n-motor-de-excitation-time)) field.
4. If necessary, configure the desired fault reaction of the encoder (see "[Fault responses (servo)](#fault-responses-servo)").
5. If required, configure the values of the current controller (see "[Current controller (servo)](#current-controller-servo)").
6. Interconnect the "Braking activation" ([p1230](SINAMICS%20Parameter%20SERVO.md#p12300n-bi-armature-short-circuit-dc-braking-activation)) signal source for the activation of the armature short-circuit or DC braking.

**Result**

The function is activated and triggered as soon as the signal source of p1230 is set to a "1" signal. The braking can be stopped again via the "0" signal.

###### Additional parameters

---

##### DC braking for OFF1/OFF3 (servo)

With this DC braking, the braking is set as a response to OFF1 or OFF3.

###### Requirements

- Motor Modules of the Booksize or Chassis format
- An induction motor must be used.

With the function "DC braking", after a demagnetization time, a DC current is injected in the stator windings of the induction motor. The DC current brakes the motor.

###### Procedure

1. Select the "[5] DC braking for OFF1/OFF3" option in the "Braking configuration" drop-down list.
2. Correct the specified default value in the "Start speed" ([p1234](SINAMICS%20Parameter%20SERVO.md#p12340n-speed-at-the-start-of-dc-braking-1)) field.
3. Enter the desired braking current value in the "Braking current" ([p1232](SINAMICS%20Parameter%20SERVO.md#p12320n-dc-braking-braking-current)) field.
4. Enter an appropriate time in the "Motor de-excitation time" ([p0347](SINAMICS%20Parameter%20SERVO.md#p03470n-motor-de-excitation-time)) field.
5. Enter an appropriate time in the "Duration" ([p1233](SINAMICS%20Parameter%20SERVO.md#p12330n-dc-braking-time)) field.
6. If necessary, configure the desired fault reaction of the encoder (see "[Fault responses (servo)](#fault-responses-servo)").
7. If required, configure the values of the current controller (see "[Current controller (servo)](#current-controller-servo)").

**Result**

If the motor speed is above the starting speed, the motor speed is reduced until it is below the starting speed. When the speed is below the starting speed, the pulses are disabled and the motor is demagnetized. DC braking is then activated for the specified duration and is then switched off.

###### Additional parameters

---

##### DC braking below starting speed (servo)

With this DC braking, this function is triggered as soon as the actual speed falls below the starting speed of the DC braking ([p1234](SINAMICS%20Parameter%20SERVO.md#p12340n-speed-at-the-start-of-dc-braking-1)).

###### Requirements

- Motor Modules of the Booksize or Chassis format
- An induction motor must be used.

With the function "DC braking", after a demagnetization time, a DC current is injected in the stator windings of the induction motor. The DC current brakes the motor.

###### Procedure

1. Select the "[14] DC braking below starting speed" option in the "Braking configuration" drop-down list.
2. Correct the specified default value in the "Start speed" (p1234) field.
3. Enter the desired braking current value in the "Braking current" ([p1232](SINAMICS%20Parameter%20SERVO.md#p12320n-dc-braking-braking-current)) field.
4. Enter an appropriate time in the "Motor de-excitation time" ([p0347](SINAMICS%20Parameter%20SERVO.md#p03470n-motor-de-excitation-time)) field.
5. Enter an appropriate time in the "Duration" ([p1233](SINAMICS%20Parameter%20SERVO.md#p12330n-dc-braking-time)) field.
6. If necessary, configure the desired fault reaction of the encoder (see "[Fault responses (servo)](#fault-responses-servo)").
7. If required, configure the values of the current controller (see "[Current controller (servo)](#current-controller-servo)").

**Result**

If the actual speed falls below the starting speed, all pulses are disabled. This demagnetizes the motor. DC braking is then initiated for the set duration.

###### Additional parameters

---

##### Fault responses (servo)

You can configure the fault responses for the armature short-circuit braking and the DC braking.

###### Procedure

1. Click the "Fault response" button.

   The configuration dialog with the same name opens. A fault response can be configured for each line in the configuration table.
2. Click in the line of the fault that you want to configure.
3. Enter a number for selected fault in the "Fault number" ([p2100](SINAMICS%20Parameter%20CU.md#p2100019-change-fault-response-fault-number)) field of this line.
4. Select the desired fault response to the fault in this line in the "Fault response" ([p2101](SINAMICS%20Parameter%20CU.md#p2101019-change-fault-response-response)) column.
5. Repeat steps 2 to 4 for further fault that you want to configure.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.
7. The fault reaction for the motor encoders in the "DC brake" screen form is pre-selected. If you want to change this default, open the "ENCODER fault reaction" drop-down list and select the desired fault reaction.

###### Additional parameters

---

##### Current controller (servo)

Configure the respective important parameters of the current controller for armature short-circuit braking and DC braking.

###### Procedure

1. Click the "Current controller" button in the "DC braking" screen form.

   The dialog box with the same name opens.
2. If required, correct the specified values in the following fields:

   - P gain ([p1345](SINAMICS%20Parameter%20SERVO.md#p13450n-dc-braking-proportional-gain))
   - Integral time ([p1346](SINAMICS%20Parameter%20SERVO.md#p13460n-dc-braking-integral-time))
   - DC braking braking current ([p1232](SINAMICS%20Parameter%20SERVO.md#p12320n-dc-braking-braking-current))
3. Once all necessary settings have been made, click "Close".

###### Additional parameters

---

#### Messages/monitoring

This section contains information on the following topics:

- [Actual speed value messages (servo)](#actual-speed-value-messages-servo)
- [Speed messages (servo)](#speed-messages-servo)
- [Setpoint / actual value messages (servo)](#setpoint-actual-value-messages-servo)
- [Blocking message (servo)](#blocking-message-servo)
- [Load torque monitoring (servo)](#load-torque-monitoring-servo)
- [Motor temperature (servo)](#motor-temperature-servo)

##### Actual speed value messages (servo)

###### Description

Comparators are provided for monitoring the actual speed and setpoint thresholds that activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Configuring the monitoring of the actual speed and setpoint thresholds

1. Enter the time constant of the PT1 element for smoothing the actual speed/velocity value in the "Smoothing" ([p2153](SINAMICS%20Parameter%20SERVO.md#p21530n-speed-actual-value-filter-time-constant-1)) field.

   The smoothed actual speed/velocity is compared with the thresholds and is only used for messages.
2. Set the hysteresis speed (bandwidth) for the message "f or n comparison value reached or exceeded" (BO: [r2199](SINAMICS%20Parameter%20SERVO.md#r2199011-cobo-status-word-monitoring-3-1).1) at "Hysteresis speed 1" ([p2142](SINAMICS%20Parameter%20SERVO.md#p21420n-hysteresis-speed-1-1)).
3. Interconnect the "f or n comparison value reached or exceeded" (r2199) signal sink with the required parameters. Several interconnections are possible.

   Interconnect binector output:

   The "f or n comparison value reached/exceeded" signal is generated under consideration of hysteresis speed 1, speed threshold 1 and the ON delay.
4. Enter the speed threshold 1 in the "Speed threshold 1" ([p2141](SINAMICS%20Parameter%20SERVO.md#p21410n-speed-threshold-1-1)) field.
5. Enter the ON delay time for signal |n_act| &gt; speed threshold in the "ON delay" ([p2156](SINAMICS%20Parameter%20SERVO.md#p21560n-on-delay-comparison-value-reached)) field.
6. Enter the bandwidths for the following messages in the "Hysteresis speed 2" ([p2140](SINAMICS%20Parameter%20SERVO.md#p21400n-hysteresis-speed-2-1)) field:

   - |n_act| &lt; speed threshold 2
   - |n_set| &gt; speed threshold 2
7. Interconnect the following signal sinks with the required parameters:

   - |n_act| ≤ speed threshold 2
   - |n_act| &gt; speed threshold 2
8. Enter speed threshold 2 in the "Speed threshold 2" ([p2155](SINAMICS%20Parameter%20SERVO.md#p21550n-speed-threshold-2-1)) field.
9. Enter the bandwidths for the n_act &gt; n_max message in the "Hysteresis speed n_act &gt; n_max" ([p2162](SINAMICS%20Parameter%20SERVO.md#p21620n-hysteresis-speed-n_act-n_max-1)) field.
10. Interconnect the "n_act &gt; n_max" ([r2197](SINAMICS%20Parameter%20SERVO.md#r2197113-cobo-status-word-monitoring-1-1)) signal sink with the required parameters. Several interconnections are possible.

    Interconnect binector output:

    Signal n_act &gt; n_max is generated under consideration of hysteresis speed n_act &gt; n_max.

    For a negative speed limit, the hysteresis is effective below the limit value and for a positive speed limit, above the limit value.

    Note:  
    The limits are set in the setpoint channel; see also [Speed limitation](#speed-limitation-1).

###### Function diagrams (FD)

- Signals and monitoring functions - Speed messages 1 - 8010 -
- Signals and monitoring functions - Speed messages 2 - 8011 -
- Setpoint channel not activated - Generation of the speed limits (r0108.8 = 0) - 3095 -
- Setpoint channel - Skip frequency bands and speed limits - 3050 -

###### Additional parameters

---

##### Speed messages (servo)

###### Description

Comparators are provided for monitoring the speed thresholds used to activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Configuring the monitoring of speed thresholds

1. Correct the specified bandwidths for the following messages in the "Hysteresis speed 3" ([p2150](SINAMICS%20Parameter%20SERVO.md#p21500n-hysteresis-speed-3-1)[0]) field:

   - n_act ≥ 0
   - |n_act| &lt; speed setpoint 3
   - n_set &lt; [p2161](SINAMICS%20Parameter%20SERVO.md#p21610n-speed-threshold-3-1)
   - n_set ≥ 0

   The calculation mode is defined using [p0340](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0340-automatic-calculation-control-parameters).
2. Interconnect the "n_act ≥ 0" ([r2197](SINAMICS%20Parameter%20SERVO.md#r2197113-cobo-status-word-monitoring-1-1).3) signal sink with the required parameters. Several interconnections are possible.

   Signal n_act ≥ 0 is generated considering hysteresis speed 3.
3. Interconnect the "|n_act| &lt; speed threshold 3" ([r2199](SINAMICS%20Parameter%20SERVO.md#r2199011-cobo-status-word-monitoring-3-1).0) signal sink with the required parameters. Several interconnections are possible.

   Signal |n_act| &lt; speed threshold 3 is generated considering hysteresis speed 3 and speed threshold 3.
4. Correct the speed threshold 3 for |n_act| &lt; speed setpoint 3 in the "Speed threshold 3" (p2161) field.
5. Interconnect the "Speed setpoint for messages" ([p2151](SINAMICS%20Parameter%20SERVO.md#p21510n-ci-speed-setpoint-for-messagessignals-1)) signal source for speed setpoint messages.
6. Interconnect the "Speed setpoint 2" ([p2154](SINAMICS%20Parameter%20SERVO.md#p21540n-ci-speed-setpoint-2-1)) signal source for velocity setpoint 2.

###### Function diagrams (FD)

- Signals and monitoring functions - Speed messages 1 - 8010 -
- Signals and monitoring functions - Speed messages 2 - 8011 -

###### Additional parameters

---

##### Setpoint / actual value messages (servo)

###### Description

Comparators are provided for monitoring the actual speed and setpoint thresholds that activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Configuring monitoring

1. Correct the specified bandwidth for the "Speed setp - act val deviation in tolerance t_off" message in the "Hysteresis speed 4" ([p2164](SINAMICS%20Parameter%20SERVO.md#p21640n-hysteresis-speed-4-1)) field.
2. Correct the specified speed threshold in the "Speed threshold 4" ([p2163](SINAMICS%20Parameter%20SERVO.md#p21630n-speed-threshold-4-1)) field.
3. Correct the OFF delay time for the "Speed setpoint - actual value deviation in tolerance t_off" message in the "OFF delay" ([p2166](SINAMICS%20Parameter%20SERVO.md#p21660n-off-delay-n_act-n_set-1)) field.
4. Interconnect the "Setpoint - actual value deviation in tolerance t_off" ([r2197](SINAMICS%20Parameter%20SERVO.md#r2197113-cobo-status-word-monitoring-1-1).7) signal sink for displaying the 1st monitoring status word.
5. Correct the ON delay time for the "Speed setpoint - actual value deviation in tolerance t_off" signal in the "ON delay" ([p2167](SINAMICS%20Parameter%20SERVO.md#p21670n-switch-on-delay-n_act-n_set-1)) field.
6. Interconnect the "Ramp-function generator active" ([p2148](SINAMICS%20Parameter%20SERVO.md#p21480n-bi-rfg-active)) signal source for the "RFG active" signal for the following messages:

   - Speed setp - act val deviation in tolerance t_on
   - Ramp-up/ramp-down completed
7. Interconnect the "Setpoint - actual value deviation in tolerance t_on" ([r2199](SINAMICS%20Parameter%20SERVO.md#r2199011-cobo-status-word-monitoring-3-1).4) signal sink for displaying the monitoring 3 status word.
8. Interconnect the "Ramp-up/ramp-down completed" (r2199.5) signal sink for displaying the monitoring 3 status word.

###### Function diagrams (FD)

- Signals and monitoring functions - Speed messages 1 - 8010 -
- Signals and monitoring functions - Speed messages 2 - 8011 -

###### Additional parameters

---

##### Blocking message (servo)

###### Description

If a motor blocks, when a freely set speed threshold ([p2175](SINAMICS%20Parameter%20SERVO.md#p21750n-motor-blocked-speed-threshold-1)) is undershot, the message "F07900 (N, A) drive: motor blocks" is issued after expiration of a delay time ([p2177](SINAMICS%20Parameter%20SERVO.md#p21770n-motor-blocked-delay-time)). The speed threshold and the delay time for the message can be configured in the "Blocking message" screen form.

###### Requirements

- For drives of the type "Universal (vector)", the speed controller must be located at the limitation.
- For drives with activated V/f control, the current limit must also be attained.

###### Configuring a message

1. Interconnect the "Stall monitoring enable (negated)" ([p2144](SINAMICS%20Parameter%20SERVO.md#p21440n-bi-motor-stall-monitoring-enable-negated)) signal source for the negated enable of the stall monitoring (0 = enable).
2. Correct the specified "Speed threshold" (p2175) value.

   If this speed threshold is overshot, the message "F07900 (N, A) drive: motor blocks" is issued.
3. Correct the specified delay time in the "Delay time" (p2177) field.

   The message "F07900 (N, A) drive: motor blocks" message is issued after expiration of this delay time.
4. Interconnect the "Motor blocked" ([r2198](SINAMICS%20Parameter%20SERVO.md#r2198412-cobo-status-word-monitoring-2-1).6) signal sink for the 2nd status word monitoring.

###### Function diagrams (FD)

- Signals and monitoring functions - Torque messages, motor blocked/stalled - 8012 -

###### Additional parameters

---

##### Load torque monitoring (servo)

###### Description

With the load torque monitoring, you can check the power transmission between a motor and a driven machine. Typical applications are, for example, V belts, flat belts or chains that grip belt pulleys or sprocket wheels of drive and output shafts, and thereby transmit peripheral speeds and forces. Load monitoring can be used here to identify blocking of the driven machine and interruptions to the power transmission.

During load torque monitoring, the current speed/torque curve is compared with the programmed speed/torque curve ([p2182](SINAMICS%20Parameter%20SERVO.md#p21820n-load-monitoring-velocity-threshold-1-1) to [p2190](SINAMICS%20Parameter%20SERVO.md#p21900n-load-monitoring-force-threshold-3-lower-1)). If the actual value is outside the programmed tolerance bandwidth, a fault or alarm is triggered depending on parameter [p2181](SINAMICS%20Parameter%20SERVO.md#p21810n-load-monitoring-response). Faults or alarms can be delayed using parameter [p2192](SINAMICS%20Parameter%20SERVO.md#p21920n-load-monitoring-delay-time). to prevent false messages caused by brief transitional states.

**Extensions through the function module**

The load torque monitoring is a function module that is, by default, deactivated. When this function module is activated, the monitoring functions are extended as follows:

- Speed setpoint monitoring: |n_set| ≤ [p2161](SINAMICS%20Parameter%20SERVO.md#p21610n-speed-threshold-3-1)
- Speed setpoint monitoring: n_set &gt; 0
- Load monitoring (see below)

**Possible responses of the load torque monitoring**

- A07920 for torque/speed too low

  There is a negative difference of the torque to the torque/speed envelope curve (too low).

  - No response
- A07921 for torque/speed too high

  There is a positive difference of the torque to the torque/speed envelope curve (too high).

  - No response
- A07922 for torque/speed out of tolerance

  The torque deviates from the torque/speed envelope curve.

  - No response
- F07923 for torque/speed too low

  There is a negative difference of the torque to the torque/speed envelope curve (too low).

  - OFF1 (OFF2, OFF3, NONE) as response
- F07924 for torque/speed too high

  There is a positive difference of the torque to the torque/speed envelope curve (too high).

  - OFF1 (OFF2, OFF3, NONE) as response
- F07925 for torque/speed outside the tolerance

  The torque deviates from the torque/speed envelope curve.

  - OFF1 (OFF2, OFF3, NONE) as response

###### Requirement

- The function module "Extended messages/monitoring" is activated (see [Function modules (servo)](#function-modules-servo)).

###### Configuring of load torque monitoring

1. In the "Load monitoring response" drop-down list (p2181), select the desired response to the results of the load monitoring (see description above).

   The view of the screen form is adapted to the setting that was made.
2. If the load monitoring is only to be performed in the 1st quadrant, select the option "Yes" in the drop-down list of the same name ([p2149](SINAMICS%20Parameter%20SERVO.md#p21490n-monitoring-configuration)).
3. If required, correct the desired delay time in the "Delay time" field (p2192).
4. Enter the desired values in the fields at the axes of the graphic:

   - Load monitoring speed threshold 1 (p2182)
   - Load monitoring speed threshold 2 ([p2183](SINAMICS%20Parameter%20SERVO.md#p21830n-load-monitoring-velocity-threshold-2-1))
   - Load monitoring speed threshold 3 ([p2184](SINAMICS%20Parameter%20SERVO.md#p21840n-load-monitoring-velocity-threshold-3-1))
   - Load monitoring torque threshold 3, upper ([p2189](SINAMICS%20Parameter%20SERVO.md#p21890n-load-monitoring-force-threshold-3-upper-1))
   - Load monitoring torque threshold 3, lower (p2190)
   - Load monitoring torque threshold 2, upper ([p2187](SINAMICS%20Parameter%20SERVO.md#p21870n-load-monitoring-force-threshold-2-upper-1))
   - Load monitoring torque threshold 2, lower ([p2188](SINAMICS%20Parameter%20SERVO.md#p21880n-load-monitoring-force-threshold-2-lower-1))
   - Load monitoring torque threshold 1, upper ([p2185](SINAMICS%20Parameter%20SERVO.md#p21850n-load-monitoring-force-threshold-1-upper-1))
   - Load monitoring torque threshold 1, lower ([p2186](SINAMICS%20Parameter%20SERVO.md#p21860n-load-monitoring-force-threshold-1-lower-1))
5. Save the project settings.

###### Function diagrams (FD)

Signals and monitoring functions - Load monitoring (r0108.17 = 1) - 8013 -

###### Additional parameters

---

##### Motor temperature (servo)

This section contains information on the following topics:

- [Overview](#overview-4)
- [Motor temperature - Configuration example](#motor-temperature---configuration-example)
- [Configuring temperature models and temperature monitoring](#configuring-temperature-models-and-temperature-monitoring)

###### Overview

The thermal motor protection monitors the motor temperature and responds to overtemperature conditions with alarms or faults. The motor temperature is either measured with sensors in the motor, or is calculated without sensors, with the aid of a temperature model, from the operating data of the motor.

- For thermal motor protection with temperature sensors, the motor temperature is directly measured in the motor windings. The temperature sensors are either connected to the Control Unit, to the Motor Modules and the Power Modules or to supplementary modules. The determined temperature values are sent to the Control Unit, which then responds according to the parameter settings.
- The thermal motor protection without temperature sensors uses different temperature models for the calculation. Depending on the temperature model, the temperatures are calculated from the motor operating data. Whereby, the masses of the motor components and the type of ventilation, and for the I<sup>2</sup>t model (for synchronous motors), the motor current in relation to the operating time is taken into consideration in the calculation. Depending on the temperature model, the temperature rise is either assigned to various motor components (stator, rotor) or is calculated from the motor current and the thermal time constant.

You can also use a combination of temperature models with additional temperature sensors. As soon as critical motor temperatures are determined, measures to protect the motor are automatically initiated.

###### Temperature sensors

**Monitoring sensors**

The motor temperature is measured using temperature sensors integrated in the motor windings. The following settings are possible as monitoring sensor:

- [0] No sensor

  The motor temperature is determined automatically through the motor model of the respective motor type.
- [1] Temperature sensor via encoder 1

  Bimetallic switches and Pt100 temperature sensors are not supported.
- [2] Temperature sensor via encoder 2

  Bimetallic switches and Pt100 temperature sensors are not supported.
- [3] Temperature sensor via encoder 3

  Bimetallic switches and Pt100 temperature sensors are not supported.
- [10] Temperature sensor via BICO interconnection

  The BICO interconnection must be implemented via connector input [p0603](SINAMICS%20Parameter%20SERVO.md#p0603-ci-motor-temperature-signal-source).
- [11] Temperature sensor via Motor Module/CU terminals
- [20] Temperature sensor via BICO interconnection [p0608](SINAMICS%20Parameter%20SERVO.md#p060803-ci-motor-temperature-signal-source-2)

  The BICO interconnection must be implemented via connector input p0608.
- [21] Temperature sensor via BICO interconnection [p0609](SINAMICS%20Parameter%20SERVO.md#p060903-ci-motor-temperature-signal-source-3)

  The BICO interconnection must be implemented via connector input p0609.

**Sensor types**

The sensors used are selected as standard from the following four different sensor types or via temperature channels:

- **PTC**

  The temperature sensor is connected to the Sensor Module at the appropriate terminals (-Temp) and (+Temp). A corresponding alarm is output after exceeding the tripping resistance (1650 Ω) and a corresponding fault after the delay time set in [p0606](SINAMICS%20Parameter%20SERVO.md#p06060n-mot_temp_mod-2-sensor-timer) has expired.
- **KTY84**

  The temperature sensor is connected to the Sensor Module at the appropriate terminals (-Temp) and (+Temp). A KTY84 temperature sensor has an almost linear characteristic and is therefore also suitable for continuously measuring and displaying the motor temperature.
- **Pt100/Pt1000**

  A Pt100 or Pt1000 is in principle a PTC with a very linear characteristic, and is suitable for continuous and exact temperature measurements. Not every sensor input is Pt100/Pt1000-capable.
- **Bimetallic sensor with NC contact** (abbreviated, "bimetal NC contact")

  A bimetallic NC contact actuates a switch at a certain nominal response temperature. The tripping resistance is &lt;100 Ω. Not every sensor input is bimetal NC contact-capable.
- **Evaluation via temperature channels**

  If you use several temperature channels, the sensors are interconnected via BICO.

###### Temperature models

If temperature sensors are not used to protect the motor from overheating, then temperature models (also called "thermal motor models") can be used instead. Temperature models react dynamically faster than temperature sensors and therefore provide better protection against short-term overloads.

> **Note**
>
> During commissioning, the respective temperature model is automatically set after selecting an appropriate motor type. The parameters are automatically set suitable for the motor type.

- **Temperature model 1**

  This temperature model is only used for selected synchronous motors and protects against short-term overloads. It is based on continuous current measurement. The dynamic load of the motor is determined from the motor current and the motor model time constant. The actual value of the motor winding temperature can be measured via a temperature sensor and taken into account.
- **Temperature model 2**

  This temperature model is used for induction motors.
- **Temperature model 3**

  This temperature model is only intended for certain Siemens motors, which do not have their own integrated temperature sensors. Temperature module 3 is a thermal 3-mass model.

###### Additional parameters

---

###### Motor temperature - Configuration example

###### Description

The monitoring of the motor temperature can be performed via a temperature model or a temperature sensor or a combination of both. There are numerous setting variants for the configuration of the motor temperature monitoring that depend on the monitoring sensor used, on the sensor type and on the temperature model used. A detailed description of all these variants would exceed the framework here.

A description of the procedure is shown below for an example with the following configuration:

- Sensor for monitoring: Temperature sensor via encoder 1
- Sensor type: Pt1000
- Motor type: Induction motor
- Alarm message for sensor failure is to be output.

###### Example of a configuration procedure

1. Select the "Temperature sensor via encoder 1" sensor for monitoring the motor temperature in the "Sensor for monitoring" ([p0600](SINAMICS%20Parameter%20SERVO.md#p06000n-motor-temperature-sensor-for-monitoring)) drop-down list.

   The configuration screen form is adapted.

   Since an induction motor is being used, temperature model 2 is activated automatically.

   The "Alarm message for sensor failure" option is generally always activated when this screen form is called and should only be deactivated in exceptional circumstances.
2. In the "Sensor type" ([p0601](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0601-temperature-sensor-sensor-type)) drop-down list select the sensor type "Pt1000" for motor temperature monitoring.
3. In the "Alarm threshold" ([p0604](SINAMICS%20Parameter%20SERVO.md#p06040n-mot_temp_mod-2-sensor-alarm-threshold)) field, correct the proposed alarm threshold for monitoring the motor temperature.
4. In the "Fault threshold" ([p0605](SINAMICS%20Parameter%20SERVO.md#p06050n-mot_temp_mod-12-sensor-threshold-and-temperature-value)) field, correct the threshold or the temperature value for monitoring the motor temperature.
5. In the "Delay" ([p0606](SINAMICS%20Parameter%20SERVO.md#p06060n-mot_temp_mod-2-sensor-timer)) field, enter the timer for monitoring the motor temperature.
6. In the "Timer" ([p0607](SINAMICS%20Parameter%20SERVO.md#p06070n-temperature-sensor-fault-timer)) field, correct the time between the output of an alarm and of a fault.

   This timer is started when a sensor fault is present.
7. If required, you can also optimize the detailed settings of the temperature model.

   To do this, click the "Temperature model" button. The configuration dialog of the temperature model opens.

   Correct the following detailed settings:

   - Overtemperature of the stator iron ([p0626](SINAMICS%20Parameter%20SERVO.md#p06260n-motor-overtemperature-stator-core))
   - Overtemperature of the stator winding ([p0627](SINAMICS%20Parameter%20SERVO.md#p06270n-motor-overtemperature-stator-winding))
   - Overtemperature of the rotor ([p0628](SINAMICS%20Parameter%20SERVO.md#p06280n-motor-overtemperature-rotor))
   - Motor weight ([p0344](SINAMICS%20Parameter%20SERVO.md#p03440n-motor-weight-for-the-thermal-motor-model))

   Once all necessary settings have been made, click "Close".

> **Note**
>
> Depending on the combination of the monitoring sensor, sensor type and temperature model, the values "Alarm threshold", "Fault threshold" and "Delay" in the interconnection screen form may have to be measured separately or corrected for monitoring via a temperature sensor, and for monitoring via a temperature model.

> **Note**
>
> You can view and partly correct further details for the motor and motor data for VECTOR drives. Click the ![Example of a configuration procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon to open the "Motor" screen form.

###### Function diagrams (FD)

Signals and monitoring functions - Thermal monitoring motor - 8016 -

Signals and monitoring functions - Motor temperature model 1 (I2t) - 8017 -

Signals and monitoring functions - Motor temperature model 2 - 8018 -

Signals and monitoring functions - Motor temperature model 3 - 8019 -

###### Additional parameters

- [p0613](SINAMICS%20Parameter%20SERVO.md#p06130n-mot_temp_mod-13-ambient-temperature)
- [p0615](SINAMICS%20Parameter%20SERVO.md#p06150n-mot_temp_mod-1-i2t-fault-threshold)
- [p0625](SINAMICS%20Parameter%20SERVO.md#p06250n-motor-ambient-temperature-during-commissioning)
- [r0631](SINAMICS%20Parameter%20SERVO.md#r06310n-mot_temp_mod-stator-iron-temperature)
- [r0632](SINAMICS%20Parameter%20SERVO.md#r06320n-mot_temp_mod-stator-winding-temperature)
- [r0633](SINAMICS%20Parameter%20SERVO.md#r06330n-mot_temp_mod-rotor-temperature)
- [p5350](SINAMICS%20Parameter%20SERVO.md#p53500n-mot_temp_mod-13-boost-factor-at-standstill-1)
- [p5390](SINAMICS%20Parameter%20SERVO.md#p53900n-mot_temp_mod-13-alarm-threshold)
- [p5391](SINAMICS%20Parameter%20SERVO.md#p53910n-mot_temp_mod-13-fault-threshold)

---

###### Configuring temperature models and temperature monitoring

###### Overview

The three commonly used motor temperature models require different detailed settings. The respective motor temperature models are automatically assigned to the motors used (or motor types). For example, motor temperature model 2 is automatically assigned to induction motors.

Extensions that add further parameters to the models are automatically activated for motor temperature models 1 and 2.

###### Configuring motor temperature model 1

1. Click the "Temperature model" button in the "Motor temperature" screen form.

   The "Motor temperature model 1" dialog opens. All fields are automatically assigned values. You can change these values.
2. If required, correct the values in the following fields:

   - "Motor stall current" ([p0318](SINAMICS%20Parameter%20SERVO.md#p03180n-motor-stall-current)) for synchronous motors
   - "Thermal time constant" ([p0611](SINAMICS%20Parameter%20SERVO.md#p06110n-i2t-motor-model-thermal-time-constant)) for the cold stator winding when loaded with the motor stall current
   - "Boost factor at standstill" ([p5350](SINAMICS%20Parameter%20SERVO.md#p53500n-mot_temp_mod-13-boost-factor-at-standstill-1)) for the copper losses at standstill.
   - "Overtemperature, stator winding" ([p0627](SINAMICS%20Parameter%20SERVO.md#p06270n-motor-overtemperature-stator-winding)) in relation to the ambient temperature
   - "Alarm threshold" ([p5390](SINAMICS%20Parameter%20SERVO.md#p53900n-mot_temp_mod-13-alarm-threshold)) for monitoring the motor temperature
   - "Ambient temperature" ([p0613](SINAMICS%20Parameter%20SERVO.md#p06130n-mot_temp_mod-13-ambient-temperature))
3. Once all necessary settings have been made, click "Close". Then save the setting in the project.

###### Configuring motor temperature model 2

1. Click the "Temperature model" button in the "Motor temperature" screen form.

   The "Motor temperature model 2" dialog opens.
2. If required, correct the values in the following fields:

   - "Overtemperature, stator core" ([p0626](SINAMICS%20Parameter%20SERVO.md#p06260n-motor-overtemperature-stator-core)) in relation to the ambient temperature
   - "Overtemperature, stator winding" (p0627) in relation to the ambient temperature
   - "Overtemperature, rotor" ([p0628](SINAMICS%20Parameter%20SERVO.md#p06280n-motor-overtemperature-rotor)) in relation to the ambient temperature
   - "Motor weight" ([p0344](SINAMICS%20Parameter%20SERVO.md#p03440n-motor-weight-for-the-thermal-motor-model)) that influences the 3-mass model of the induction motor
3. Once all necessary settings have been made, click "Close". Then save the setting in the project.

###### Configuring motor temperature model 3

1. Click the "Temperature model" button in the "Motor temperature" screen form.

   The "Motor temperature model 3" dialog opens.
2. If required, correct the values in the following fields:

   - "Thermal time constant" (p0611) for the cold stator winding when loaded with the motor stall current
   - "Boost factor at standstill" (p5350) for the copper losses at standstill.
   - "Alarm threshold" (p5390) for monitoring the motor temperature
   - "Fault threshold" ([p5391](SINAMICS%20Parameter%20SERVO.md#p53910n-mot_temp_mod-13-fault-threshold)) for monitoring the motor temperature
   - "Ambient temperature" (p0613)
3. Once all necessary settings have been made, click "Close". Then save the setting in the project.

###### Configuring temperature monitoring

The temperature monitoring settings are also automatically preassigned when the corresponding motor type is selected. You can change the following default settings as required:

1. In the "Sensor for monitoring" ([p0600](SINAMICS%20Parameter%20SERVO.md#p06000n-motor-temperature-sensor-for-monitoring)) drop-down list, select another sensor for monitoring the motor temperature.

   The configuration screen form is adapted.
2. In the "Sensor type" ([p0601](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0601-temperature-sensor-sensor-type)) drop-down list, select another sensor type for motor temperature monitoring.

   The configuration screen form is adapted.
3. Via the "Timer" ([p0607](SINAMICS%20Parameter%20SERVO.md#p06070n-temperature-sensor-fault-timer)) you define the timer for an alarm message in case of sensor failure. After this timer has expired, the alarm message is output.

   If necessary, correct the specified timer.
4. Optional: The "Alarm message for sensor failure" option is generally always activated when this screen form is called and should only be deactivated in exceptional circumstances.

   If you nevertheless do not want an alarm message to be output, deactivate this option.
5. Depending on the set sensor and sensor type, further setting values are displayed on the screen form. Correct the default settings there as required.

###### Additional parameters

---

#### Friction characteristic

This section contains information on the following topics:

- [Friction characteristic (servo)](#friction-characteristic-servo)
- [Friction characteristic recording (servo)](#friction-characteristic-recording-servo)

##### Friction characteristic (servo)

###### Description

The friction characteristic is used to compensate the friction torque for the motor and the driven machine. A friction characteristic allows the speed controller to be precontrolled and improves the control response. Use 10 interpolation points for the friction characteristic. You define the coordinates of every interpolation point by a speed parameter ([p3820](SINAMICS%20Parameter%20SERVO.md#p38200n-friction-characteristic-value-n0-1) ... [p3829](SINAMICS%20Parameter%20SERVO.md#p38290n-friction-characteristic-value-n9-1)) and a torque parameter ([p3830](SINAMICS%20Parameter%20SERVO.md#p38300n-friction-characteristic-value-m0-1) ... [p3839](SINAMICS%20Parameter%20SERVO.md#p38390n-friction-characteristic-value-m9-1)). The default coordinates can be changed as required in the "Friction characteristic" screen form.

###### Requirements

- The "Speed/torque control" function module has been activated (see basic parameter assignment).
- The friction characteristic can be used only for non-activated V/f control.

###### Features of the friction characteristic

- 10 interpolation points are available for mapping the friction characteristic.
- An automatic function allows you to record the friction characteristic (record friction characteristic).
- A connector output ([r3841](SINAMICS%20Parameter%20SERVO.md#r3841-co-friction-characteristic-output-1)) can be interconnected as friction torque ([p1569](SINAMICS%20Parameter%20SERVO.md#p15690n-ci-supplementary-torque-3-1)).
- The friction characteristic can be activated and deactivated ([p3842](SINAMICS%20Parameter%20SERVO.md#p3842-friction-characteristic-activation)).
- Online mode is required for using the friction characteristic.

###### Activate friction characteristic

1. Select the "[1] Friction characteristic activated" in the "Friction characteristic activation" drop-down list.

   The LED next to the drop-down list lights up green. The switchover switch is set to 1.
2. Correct the actual speed value signal of the friction characteristic via the "Actual speed value input" signal source ([p3848](SINAMICS%20Parameter%20SERVO.md#p38480n-ci-friction-characteristic-speed-actual-value-signal-source)) if required.
3. Interconnect the signal for the torque of the friction characteristic via the "Friction characteristic output" signal sink (r3841) depending on the speed or velocity.
4. Save the settings in the project.

   The friction characteristic is activated. It uses the specified coordinates of the 10 interpolation points. These coordinates can be configured together with the settings for recording the friction characteristic (see "[Friction characteristic recording (servo)](#friction-characteristic-recording-servo)").

###### Function diagrams (FD)

Servo control - Torque limiting/reduction, interpolator - 5610 -

Vector control - Current setpoint filter - 6710 -

Technology functions - Friction characteristic - 7010 -

###### Additional parameters

- [p3821](SINAMICS%20Parameter%20SERVO.md#p38210n-friction-characteristic-value-n1-1)
- [p3822](SINAMICS%20Parameter%20SERVO.md#p38220n-friction-characteristic-value-n2-1)
- [p3823](SINAMICS%20Parameter%20SERVO.md#p38230n-friction-characteristic-value-n3-1)
- [p3824](SINAMICS%20Parameter%20SERVO.md#p38240n-friction-characteristic-value-n4-1)
- [p3825](SINAMICS%20Parameter%20SERVO.md#p38250n-friction-characteristic-value-n5-1)
- [p3826](SINAMICS%20Parameter%20SERVO.md#p38260n-friction-characteristic-value-n6-1)
- [p3827](SINAMICS%20Parameter%20SERVO.md#p38270n-friction-characteristic-value-n7-1)
- [p3828](SINAMICS%20Parameter%20SERVO.md#p38280n-friction-characteristic-value-n8-1)
- [r3840](SINAMICS%20Parameter%20SERVO.md#r384008-cobo-friction-characteristic-status-word)
- [p3843](SINAMICS%20Parameter%20VECTOR.md#p38430n-friction-characteristic-frictional-torque-diff-smoothing-time)
- [p3844](SINAMICS%20Parameter%20VECTOR.md#p38440n-friction-characteristic-number-changeover-point-upper)
- [p3845](SINAMICS%20Parameter%20SERVO.md#p3845-record-friction-characteristic-activation)
- [p3846](SINAMICS%20Parameter%20SERVO.md#p38460n-record-friction-characteristic-ramp-upramp-down-time)
- [p3847](SINAMICS%20Parameter%20SERVO.md#p38470n-record-friction-characteristic-time-to-warm-up)

---

##### Friction characteristic recording (servo)

###### Description

You can make the following settings in the "Friction characteristic recording" screen form:

- Configuring the recording of the friction characteristic
- Configuring the coordinates of the interpolation points

When the friction characteristic is recorded, the drive can cause the motor to move. As a result, the motor may reach maximum speed.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned motor motion while recording the friction characteristic**  Drive motion caused when recording the friction characteristic can result in death, severe injury or material damage.  - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. |  |

###### Configuring the recording of the friction characteristic

For configuring, proceed as follows:

1. Enter the warm-up time until the maximum speed is to be reached in the "Recording warm-up time" field ([p3847](SINAMICS%20Parameter%20SERVO.md#p38470n-record-friction-characteristic-time-to-warm-up)).

   After the end of the warm-up period, measurement is started.
2. Enter the ramp-up/ramp-down time of the ramp-up/ramp-down generator for automatic recording of the friction characteristic in the "Recording ramp-up/ramp-down time" field ([p3846](SINAMICS%20Parameter%20SERVO.md#p38460n-record-friction-characteristic-ramp-upramp-down-time)).
3. If required, correct the n and M coordinates of the 10 specified interpolation points:

   - In the "Speed" fields, configure the specified speed ([p3820](SINAMICS%20Parameter%20SERVO.md#p38200n-friction-characteristic-value-n0-1)[0] ... [p3829](SINAMICS%20Parameter%20SERVO.md#p38290n-friction-characteristic-value-n9-1)[0]) for each interpolation point.
   - In the "Torque" fields, configure the specified torque ([p3830](SINAMICS%20Parameter%20SERVO.md#p38300n-friction-characteristic-value-m0-1)[0] ... [p3839](SINAMICS%20Parameter%20SERVO.md#p38390n-friction-characteristic-value-m9-1)[0]) for each interpolation point.
4. Establish an online connection to the drive.
5. In the "Recording of the friction characteristic" screen form, select the desired automatic friction characteristic recording in the "Activate recording" drop-down list ([p3845](SINAMICS%20Parameter%20SERVO.md#p3845-record-friction-characteristic-activation)). The following options are available:

   - [0] Record friction characteristic deactivated
   - [1] Record friction characteristic activated all directions

     The friction characteristic is recorded in both directions of rotation. The results of the positive and negative measurement are averaged and entered in p3830 ... p3839.
   - [2] Record friction characteristic activated positive direction
   - [3] Record friction characteristic activated negative direction
6. Save the configuration in the project.

   After the next switch-on command, the friction characteristic will be automatically recorded.

###### Function diagrams (FD)

Servo control - Torque limiting/reduction, interpolator - 5610 -

Vector control - Current setpoint filter - 6710 -

Technology functions - Friction characteristic - 7010 -

###### Additional parameters

---

### Safety Integrated

This section contains information on the following topics:

- [Safety Integrated overview (S/G drives)](#safety-integrated-overview-sg-drives)
- [Specific safety instructions and information](#specific-safety-instructions-and-information)
- [Function descriptions](#function-descriptions)
- [Basic settings](#basic-settings)
- [Basic functions](#basic-functions-1)
- [Extended Functions](#extended-functions-1)
- [Advanced Functions](#advanced-functions-1)
- [Control](#control)
- [Test stop](#test-stop)
- [Function status](#function-status)
- [Acceptance mode](#acceptance-mode)

#### Safety Integrated overview (S/G drives)

##### Overview

In comparison to standard drive functions, safety functions (Safety Integrated) have an especially low error rate. Performance level (PL) and safety integrity level (SIL) of the corresponding standards are a measure of the error rate.

As a consequence, the safety functions are suitable for use in safety-related applications to minimize risk. An application is safety-related if the risk analysis of the machine or the system indicates a special hazard potential in the application.

Safety Integrated ("drive-integrated") means that the safety functions are integrated in the drive and can be executed without additional external components.

##### Conformity

The safety functions conform to

- Safety integrity level (SIL) 2 according to EN 61508
- Category 3 according to EN ISO 13849‑1
- Performance level (PL) d according to EN ISO 13849-1

The safety functions correspond to the functions according to EN 61800‑5‑2.

##### Description

The S/G drives (SINAMICS S120, S150, G150, G130) feature the following drive-integrated safety functions:

Overview of Safety Integrated Functions

| Packages | Functions | Abbr. | Can be used without safety-capable encoder | Brief description |
| --- | --- | --- | --- | --- |
| [Basic Functions](#basic-functions) | Safe Torque Off | STO | x | Safe Torque Off |
| Safe Stop 1 | SS1 | x | Safe stop according to stop category 1 |  |
| Safe Brake Control | SBC | x | Safe Brake Control |  |
| [Extended Functions](#extended-functions) | Safe Torque Off | STO | x<sup>1)</sup> | Safe torque off stop category |
| Safe Stop 1 | SS1 | x<sup>1)</sup> | Safe stop according to stop category 1 |  |
| Safe Brake Control | SBC | x<sup>1)</sup> | Safe Brake Control |  |
| Safe Operating Stop | SOS | ‑ | Safe monitoring of the standstill position |  |
| Safe Stop 2 | SS2 | ‑ | Safe stop according to stop category 2 |  |
| Safe Speed Monitor | SSM | x<sup>1)</sup> | Safe monitoring of the minimum velocity |  |
| Safe Direction | SDI | x<sup>1)</sup> | Safe monitoring of the direction of motion |  |
| **Diagnostic function**   Safe Brake Test<sup>3)</sup> | SBT | ‑ | Safe test of the required holding torque  of a brake |  |
| Safe Acceleration Monitor | SAM | x<sup>1)</sup> | Safe monitoring of drive acceleration |  |
| Safe Brake Ramp | SBR | x<sup>1)</sup> | Safe Brake Ramp |  |
| Safely-Limited Acceleration | SLA | ‑ | Safely-Limited Acceleration |  |
| Safe gear stage switchover<sup>2)</sup> | – | ‑ | – |  |
| [Advanced Functions](#advanced-functions) | Safely-Limited Position | SLP | x<sup>1)</sup> | Safe monitoring of the maximum velocity |
| Transferring safe position values | SP | x<sup>1)</sup> | Transferring safe position values |  |
| Safe Cam | SCA | ‑ | Safe cam |  |
| Safe homing | SR | ‑ | Safe homing |  |
| <sup>1) </sup>The use of this safety function without safety-capable encoder is permitted only for induction motors, reluctance motors or synchronous motors of the "SIMOTICS A-1FU" series.   <sup>2)</sup> The safe gear stage switchover can be parameterized only via the parameter view. Detailed information about these functions can be found in the SINAMICS S120 Safety Integrated Function Manual.   <sup>3)</sup> The Safe Brake Test is purely a **diagnostic function**, but for organizational reasons is included in the list of Safety Integrated Extended Functions. |  |  |  |  |

**Use of encoders**

> **Note**
>
> **Use with and without encoder**
>
> All safety functions of the S/G drives can generally be used "with encoder". But not every encoder is safety-capable. Some encoders are only used for control.
>
> The table below lists the safety functions that can also be used "without safety-capable encoder".

In operation without safety-capable encoder, the actual velocity values are calculated from the measured electrical actual values. In this way, speed monitoring is possible in operation without safety-capable encoder, too.

**Activating the Safety commissioning**

Before the safety functions are edited, the Safety commissioning must be activated and the safety functionality selected:

- [Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)
- [Selecting the safety functionality](#selecting-the-safety-functionality)

**PROFIsafe**

For PROFIsafe you need a telegram extension, which you set under "[Telegram configuration](Communication%20and%20telegrams.md#telegram-configuration-via-profidrive)".

##### Function diagrams (FD)

**Basic Functions**

SI Basic Functions - Parameter manager - 2800 -

SI Basic Functions - Monitoring functions and faults/alarms - 2802 -

SI Basic Functions - SI status CU, MM, CU + MM, group STO - 2804 -

SI Basic Functions - S_STW1/2 safety control word 1/2, S_ZSW1/2 safety status word 1/2 - 2806 -

SI Basic Functions - STO (Safe Torque Off), SS1 (Safe Stop 1) - 2810 -

SI Basic Functions - STO (Safe Torque Off), safe pulse suppression - 2811 -

SI Basic Functions - SBC (Safe Brake Control), SBA (Safe Brake Adapter) - 2814 -

**Extended Functions**

SI Extended Functions - Parameter manager - 2818 -

SI Extended Functions - SS1, SS2, SOS, internal STOP B, C, D, F - 2819 -

SI Extended Functions - SLS (Safely-Limited Speed) - 2820 -

SI Extended Functions - SSM (Safe Speed Monitor) - 2823 -

SI Extended Functions - SDI (Safe Direction) - 2824 -

SI Extended Functions - SAM (Safe Acceleration Monitor), SBR (Safe Brake Ramp) - 2825 -

SI Extended Functions - SBT (Safe Brake Test) - 2836 -

SI Extended Functions - Selection of the active control word - 2837 -

SI Extended Functions - SI Motion drive-integrated control signals / status signals - 2840 -

SI Extended Functions - S_STW1 safety control word 1, S_ZSW1 safety status word 1 - 2842 -

SI Extended Functions - S_STW2 safety control word 2, S_ZSW2 safety status word 2 - 2843 -

SI Advanced Functions - S_ZSW_CAM1 Safety status word Safe Cam 1 - 2844 -

SI Extended Functions - Control via PROFIsafe (p9601.2 = p9601.3 = 1) - 2858 -

SI Extended Functions - CU310-2 (F-DI 0 ... F-DI 2) - 2870 -

SI Extended Functions - CU310-2 failsafe digital output (F-DO 0) - 2873 -

SI Extended Functions - CU310-2 control interface - 2875 -

SI Extended Functions - CU310-2 Safe State selection - 2876 -

SI Extended Functions - CU310-2 assignment (F-DO 0) - 2877 -

**Advanced Functions**

SI Extended Functions - Safe referencing - 2821 -

SI Advanced Functions - SLP (Safely-Limited Position) - 2822 -

SI Advanced Functions - SCA (Safe Cam) - 2826 -

**PROFIsafe**

SI PROFIsafe - Standard telegrams - 2915 -

SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

#### Specific safety instructions and information

This section contains information on the following topics:

- [Safety Integrated safety instructions](#safety-integrated-safety-instructions)
- [Residual risk](#residual-risk)
- [Further information](#further-information)

##### Safety Integrated safety instructions

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Inactive Safety Integrated Functions during ramp-up after switching on**  The Safety Integrated Functions are only activated after the system has completely powered up. System startup is a critical operating state with increased risk. When accidents occur, this can result in death or severe injury.   - Stay completely away from any hazardous areas while the system powers up. - For vertical axes, check that the drives are in a no-torque state. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Undesirable motor movements during automatic restart**  The Emergency Stop function must bring the machine to a standstill according to stop category 0 or 1 (STO or SS1) (EN 60204-1). Persons within the hazardous area are at risk of serious injury or even fatalities whenever an automatic restart is initiated following an emergency stop.   If individual safety functions (Extended Functions) are deactivated, an automatic restart is permitted under certain circumstances depending on the risk analysis (except when Emergency Stop is reset). An automatic start is permitted when a protective door is closed, for example.  - For the cases listed above, ensure that an automatic restart is absolutely not possible. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Undesirable drive movements during power up of the system following modification or replacement of hardware and/or software**  After hardware and/or software components have been modified or replaced, it is only permissible for the system to run up and the drives to be activated with the protective devices closed. Changes to the system that have not been thoroughly tested can initiate undesirable functions. For persons in the hazardous area, this can result in death or severe injury.   - Carry out the following tests after a change or replacement (see [Acceptance test](Safety%20Integrated%20acceptance%20test.md#sinamics-safety-integrated-acceptance-test)):    - A complete acceptance test   - A partial acceptance test   - A simplified function test - Before personnel may re-enter the hazardous area, the drives MUST be tested to ensure that they exhibit stable control behavior by briefly moving them in both the plus and minus directions (+/–). - Ensure that nobody is in the hazardous area during the test. - When switching on, carefully observe that Safety Integrated Functions are only available and can only be selected after the system has completely powered up. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unanticipated movement of the drive**  When the energy supply has been disconnected (STO active), unanticipated movements of the drive may occur (e.g. coasting down) and thus pose a hazard to persons.  - Take suitable measures to prevent undesirable movement, e.g. by using a brake with safe monitoring. |  |

> **Note**
>
> **Risk minimization through Safety Integrated**
>
> Safety Integrated can be used to minimize the level of risk associated with machines and plants.   
> However, safe operation of a system or machine based on Safety Integrated is only possible if the following requirements are fully satisfied:
>
> - The machine builder (OEM) precisely knows and observes this technical user documentation – including the documented limitations, safety information and residual risks.
> - The machine builder (OEM) carefully and professionally designs, constructs and configures the system/machine. This must then be verified through careful and thorough acceptance tests by qualified personnel and the results documented.
> - The machine builder (OEM) implements and validates all the measures required in accordance with the system/machine risk analysis by means of the programmed and configured Safety Integrated Functions or by other means.
>
> The use of Safety Integrated does not replace the machine/plant risk assessment carried out by the machine manufacturer as required by the EC machinery directive.   
> In addition to using Safety Integrated Functions, further risk reduction measures must be implemented.

##### Residual risk

The fault analysis enables machine manufacturers to determine the residual risk at their machine with regard to the drive unit. The following residual risks are known:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Brief limited movements of the motor**  Simultaneous breakdown of 2 power transistors in the power unit can cause a short, limited movement. This can result in accidents leading to death or severe injury.  - If there is a danger of undesirable movement in your application, you must take the appropriate measures to prevent this, e.g. by using a brake with safe monitoring (see "Safe Brake Control") |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Overshooting the speed or position that briefly violates the limit value**  A limit violation may briefly lead to a speed higher than the speed setpoint, depending on the dynamic response of the drive and on parameter settings. The prescribed position can be more or less overtraveled. This can cause damage to the drive.   - Configure the machine to ensure that the prescribed position can be overtraveled as minimally as possible. |  |

**Residual risk for a single-encoder system**

If the encoder signals become static (that is, they no longer follow a movement while still returning a correct level) for a stationary drive (e.g. in SOS), this fault will not be detected. Potential causes for this fault include:

1. A single electrical fault in the encoder
2. An encoder shaft breakage (or the encoder shaft coupling slips) or loosening of the encoder enclosure fastening

Generally, the drive is held by the active closed-loop control. Especially for drives with suspended load, from a closed-loop control perspective, it is conceivable that drives such as these move without this being detected.

The risk of an electrical fault in the encoder as described under 1.) is only present for few encoder types employing a specific principal of operation.

- All of the faults described above must be included in the risk analysis of the machine manufacturer. Additional safety measures have to be taken for drives with suspended/vertical or pulling loads, e.g. in order to exclude faults under 1.):

  - Use of an encoder with analog signal generation
  - Use of a two-encoder system
- The following safety measures are necessary to exclude the fault under 2.):

  - Perform an FMEA regarding encoder shaft breakage (or slip of the encoder shaft coupling) as well as loose encoder housings and use a fault exclusion process according to IEC 61800-5-2, or
  - Implementation of a two-encoder system (the encoders must not be mounted on the same shaft).

##### Further information

As well as the information regarding "Safety Integrated" in this online help, further detailed information may also be obtained in the SINAMICS S120 Safety Integrated Function Manual. In particular, we recommend the following chapters in this Function Manual for additional information:

- System features

  Information regarding certifications, probabilities of failure, and response times.
- Maintenance

  Information regarding component replacement, firmware updates, Safety faults, and Safety message buffer.
- Standards and regulations

  Information on standards and regulations in the EU, USA and Japan, as well as equipment specifications and additional sources of information pertaining to "Safety".

#### Function descriptions

This section contains information on the following topics:

- [Introduction](#introduction)
- [Basic functions](#basic-functions)
- [Extended Functions](#extended-functions)
- [Advanced Functions](#advanced-functions)
- [Difference between Emergency Off and Emergency Stop](#difference-between-emergency-off-and-emergency-stop)

##### Introduction

The following function descriptions are designed to provide you with a quick overview of the operating principle of the Safety Integrated Functions. The description of the functions is simplified, as far as possible to clearly shown essential properties and setting options.

###### Operation of the Safety Integrated Functions

Further information about the parameter assignment of the individual Safety Integrated Functions in Startdrive can be found at:

- [Basic functions](#basic-functions-1)
- [Extended Functions](#extended-functions-1)
- [Advanced Functions](#advanced-functions-1)

##### Basic functions

This section contains information on the following topics:

- [Notes on the basic functions](#notes-on-the-basic-functions)
- [Description of Safe Torque Off (STO, Basic and Extended Functions)](#description-of-safe-torque-off-sto-basic-and-extended-functions)
- [Description of Safe Stop 1 (SS1, Basic Functions)](#description-of-safe-stop-1-ss1-basic-functions)
- [Description of Safe Brake Control (SBC)](#description-of-safe-brake-control-sbc)
- [Safety Integrated faults (Basic Functions)](#safety-integrated-faults-basic-functions)
- [Test stop for Basic Functions](#test-stop-for-basic-functions)

###### Notes on the basic functions

- The Safety Integrated Basic Functions are functions for safely stopping the drive. You do not require an encoder.
- The Basic Functions are available in all control types with and without encoder for synchronous and induction motors without restrictions.

###### Description of Safe Torque Off (STO, Basic and Extended Functions)

Definition according to EN 61800-5-2:

"The STO function prevents energy from being supplied to the motor, which can generate a torque."

![Figure](images/147856991627_DV_resource.Stream@PNG-en-US.png)

###### Examples of how the function can be used

| Example | Possible solution |
| --- | --- |
| It is only permissible to open a protective door if the motor torque has been switched off. | - Select STO in the converter. - The pulses are suppressed and the motor coasts to a standstill. |

###### How does STO function in detail?

|  |  |  |
| --- | --- | --- |
| The converter recognizes the selection of STO via a fail-safe input or via the PROFIsafe safe communication.   The converter then safely switches off the torque of the connected motor. |  | ![How does STO function in detail?](images/147856996235_DV_resource.Stream@PNG-en-US.png) |

###### Description of Safe Stop 1 (SS1, Basic Functions)

Definition according to EN 61800-5-2:

"The SS1 function brakes the motor and trips the STO function after a delay time."

![Figure](images/147857020683_DV_resource.Stream@PNG-en-US.png)

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| After an Emergency Stop button has been pressed, the drive must be braked as quickly as possible and brought into the STO state. | - Wire the Emergency Stop button with a fail-safe input. - Select SS1 via the fail-safe input. |
| A central Emergency Stop button ensures that several drives are braked as quickly as possible and brought into the STO state. | - Evaluate an emergency stop button in a central control. - Select SS1 via PROFIsafe. |

###### How does SS1 function in detail?

|  |  |  |
| --- | --- | --- |
| **Overview**   The drive brakes after the selection of "Safe Stop 1" and goes into the "Safe Torque Off" (STO) state after a delay time. |  | ![How does SS1 function in detail?](images/147857025291_DV_resource.Stream@PNG-en-US.png) |

###### Selecting SS1

As soon as the converter identifies that SS1 has been selected via a terminal or via the PROFIsafe safe communication, the following happens:

- If the motor is already switched off when SS1 is selected, then there is no response until the SS1 delay time has expired. When the time expires, STO takes effect.
- If the motor is switched on when SS1 is selected, the converter brakes the motor with the OFF3 ramp-down time. When the delay time expires, STO automatically takes effect.

###### SS1 with external stop (SS1E)

For drive line-ups (e.g. drives that are mechanically connected via the material), it can be disruptive if drives are braked independently along their respective OFF3 ramp. If the SS1E function is used, the safe delay time (p9562) is started for each drive when selected, but no OFF3 is triggered. The higher-level controller still has setpoint control. The controller is informed that SS1E has been selected via the safety information channel.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned axis movements during Safe Stop 1**  During the delay time (p9652), random axis movements are possible for "Safe Stop 1 (time-controlled) with external stop" which could result in severe injuries or death within the hazardous area.  - Take suitable measures to prevent undesirable axis movements, e.g. by using a brake with safe monitoring.    For more information, see [Description of Safe Brake Control (SBC)](#description-of-safe-brake-control-sbc). |  |

**Differences between "SS1 with OFF3" and "SS1 with external stop"**

There are the following differences between "SS1 with OFF3" and "SS1 with external stop":

- To activate "Safe Stop 1 with external stop", you must **also** set p9653 = 1.
- If SS1E is selected, the drive is **not** braked along the OFF3 ramp, but rather after the delay time (p9652) has expired, only STO/SBC is triggered automatically.

###### Description of Safe Brake Control (SBC)

This section contains information on the following topics:

- [Description of Safe Brake Control (SBC, Basic Functions)](#description-of-safe-brake-control-sbc-basic-functions)
- [Hardware required for SBC](#hardware-required-for-sbc)

###### Description of Safe Brake Control (SBC, Basic Functions)

Definition according to EN 61800-5-2:

"The SBC function supplies a safe output signal to control a holding brake."

![Safe Brake Control (SBC)](images/147857066379_DV_resource.Stream@PNG-en-US.png)

Safe Brake Control (SBC)

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| The safe control of a motor holding brake must be guaranteed in order to guarantee the motor is at a standstill. | SBC (if configured) is triggered together with STO. The Motor Module / Safe Brake Relay / Safe Brake Adapter then carries out the action and safely controls the outputs for the brake. |

###### How does SBC function in detail?

|  |  |  |
| --- | --- | --- |
| The converter recognizes the selection of STO via a fail-safe input or via the PROFIsafe safe communication.   The converter then safely switches off the torque of the connected motor. |  | ![How does SBC function in detail?](images/147857071371_DV_resource.Stream@PNG-en-US.png) |
| SBC (if configured) is triggered together with STO. The Motor Module / Safe Brake Relay / Safe Brake Adapter then performs the action and safely controls the outputs for the brake. |  |  |

###### Hardware required for SBC

###### Hardware required for SBC

- Safe Brake Relay

  The command for releasing or applying the brake is transferred to the Motor Module / Power Module via DRIVE-CLiQ. The Motor Module / Safe Brake Relay then carries out the action and appropriately activates the outputs for the brake.

![Safe Brake Relay interconnection](images/147857098123_DV_resource.Stream@PNG-en-US.png)

Safe Brake Relay interconnection

The brake cannot be directly connected to the Motor Module in the Chassis format. The connection terminals are only designed for 24 VDC with 150 mA; the Safe Brake Adapter is required for higher currents and voltages.

> **Note**
>
> **Additionally required hardware for other formats**
>
> A Safe Brake Adapter is required for the Chassis format (as of an article number with the ending ...xxx3). The Safe Brake Adapter is available for a 230 VAC brake control voltage. For Motor Modules of Booksize format, the brake can be connected directly.

![Interconnecting the Safe Brake Adapter](images/147857108235_DV_resource.Stream@PNG-en-US.png)

Interconnecting the Safe Brake Adapter

###### Safety Integrated faults (Basic Functions)

The alarm messages of the Safety Integrated Basic Functions are stored in the standard alarm buffer and can be read out from there, unlike the alarm messages of the Safety Integrated Extended Functions, which are stored in a separate safety alarm buffer (see "[Alarm buffer](#message-buffer-extended-functionsadvanced-functions)").

When faults associated with Safety Integrated Basic Functions occur, the following stop responses can be initiated:

Stop responses for Safety Integrated Basic Functions

| Stop response | Triggered ... |  | Action |  | Effect |
| --- | --- | --- | --- | --- | --- |
| STOP A cannot be acknowledged | For all Safety Integrated faults with pulse suppression that cannot be acknowledged. |  | Trigger safe pulse suppression via the shutdown path for the relevant monitoring channel. During operation with SBC: Apply motor holding brake. |  | The motor coasts to a standstill or is braked by the holding brake. |
| STOP A | For all acknowledgeable Safety Integrated faults   As a follow-up response of STOP F |  |  |  |  |
| STOP A corresponds to Stop Category 0 in accordance with EN 60204-1.  With STOP A, the motor is switched directly to zero torque via the "Safe Torque Off (STO)" function.  A motor at standstill cannot be started again accidentally.  A moving motor coasts to standstill. This can be prevented by using external braking mechanisms, e.g. holding or operating brake.  When STOP A is present, "Safe Torque Off" (STO) is active. |  |  |  |  |  |
| STOP F | If an error occurs in the data cross-check. | Transition to STOP A. |  | Follow-up response STOP A  with adjustable delay (factory setting without delay) if one of the safety functions is selected |  |
| STOP F is permanently assigned to the data cross-check (DCC). In this way, errors are detected in the monitoring channels.  After STOP F, STOP A is triggered.  When STOP A is present, "Safe Torque Off" (STO) is active. |  |  |  |  |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movement of the axis when a STOP A/F is triggered**  With a vertical axis or a pulling load, there is a danger of uncontrolled movement of the axis when STOP A/F is triggered.   This can cause serious injury or death to persons in the danger zone.   - Used a brake with safe monitoring. For more information, see[Description of Safe Brake Control (SBC)](#description-of-safe-brake-control-sbc). |  |

###### Acknowledgment of the Safety Integrated faults

There are several ways to acknowledge Safety Integrated faults:

- Acknowledgment through deselection of STO or SS1:

  - Remove the cause of the fault.
  - Deselect "Safe Torque Off" (STO) or "Safe Stop 1" (SS1).
  - Acknowledge the fault.

  If the Safety Integrated commissioning mode is exited when the Safety Integrated Functions are switched off (p0010 ≠ 95 when p9601 = 0), all Safety Integrated faults can be acknowledged.

  Once Safety Integrated commissioning mode has been selected again (p0010 = 95), all the faults that were previously present reappear.
- The higher-level controller sets the signal "Internal Event ACK" via the PROFIsafe telegram (STW bit 7). A falling edge in this signal resets the status "Internal Event" and so acknowledges the fault.
- Acknowledgment by switching the drive unit off/on

  Safety Integrated faults can also be acknowledged (as with all other faults) by switching the drive unit off and then on again (POWER ON). If the fault cause has not been eliminated, the fault is displayed again immediately after ramp-up.

###### Description of faults and alarms

Descriptions of the faults and alarms for SINAMICS Safety Integrated functions can be found via the index and the search function of this online help.

###### Test stop for Basic Functions

###### Test of the shutdown paths (test stop) for Safety Integrated Basic Functions

The test of the shutdown paths is used to timely detect errors in the software and hardware of the two monitoring channels and is performed automatically through the selection/deselection of the "Safe Torque Off" (STO) or "Safe Stop 1" (SS1) function.

To fulfill the requirements of ISO 13849-1 regarding timely error detection, the two shutdown paths must be tested at least once within a defined interval to ensure that they are functioning properly. This must be implemented through the manual or process-automated triggering of the test stop.

The timely execution of a test of the shutdown paths (test stop) is monitored by a timer (p9659).

A test of the shutdown paths must be performed at least once within the time set in this parameter.

A corresponding alarm is output after this interval and remains active until the test stop has been performed.

The timer returns to the set value each time the STO/SS1 function is deactivated.

When the appropriate safety devices are implemented (e.g. protective doors), it can be assumed that running machinery will not pose any risk to personnel. The user is therefore only informed that the test of the shutdown paths is pending by an alarm, which requests the user to perform the test stop at the next possible opportunity. This alarm does not affect machine operation.

Users must set the interval for performing the test stop between 0.00 and 9000.00 hours depending on their application (factory setting: 8.00 hours).

Examples for performing the test stop:

- When the drives are at a standstill after the system has been switched on (POWER ON).
- When the protective door is opened.
- At defined intervals (e.g. every eight hours).
- In automatic mode (time and event-dependent).
- The maximum time interval is one year (8760 hours).

Test stops can be automatically executed at POWER ON.

- Even if you have parameterized the test stop for POWER ON, you can still initiate a test stop at any time through the application.
- If the automatically initiated function cannot be correctly completed as a result of a problem (e.g. communication failure), then after the problem has been resolved, the function is automatically restarted.
- After the test stop has been performed successfully, the converter goes into the "Ready" state.
- An automatic test stop resets timer p9559.
- The automatic test stop for POWER ON does not affect the Safety Integrated Functions.

> **Note**
>
> **Reset timer of Basic Functions automatically**
>
> If, when simultaneously using the Extended Functions, the associated test stop is performed, the timer of the Basic Functions is also reset.
>
> While STO is selected by the Extended Functions, the onboard terminals for the selection of the Basic Functions are not checked for discrepancy. This means that the test stop of the Basic Functions must always be performed without the selection of STO or SS1 by the Extended Functions. Otherwise the correct control by the onboard terminals cannot be checked.

##### Extended Functions

This section contains information on the following topics:

- [Description of Safe Torque Off (STO, Basic and Extended Functions)](#description-of-safe-torque-off-sto-basic-and-extended-functions-1)
- [Description of Safe Stop 1 (SS1, Extended Functions)](#description-of-safe-stop-1-ss1-extended-functions)
- [Description of Safe Brake Control (SBC, Extended Functions)](#description-of-safe-brake-control-sbc-extended-functions)
- [Description of Safe Operating Stop (SOS, Extended Functions)](#description-of-safe-operating-stop-sos-extended-functions)
- [Description of Safe Stop 2 (SS2, Extended Functions)](#description-of-safe-stop-2-ss2-extended-functions)
- [Special features of SS2E and SS2ESR](#special-features-of-ss2e-and-ss2esr)
- [Description of Safely-Limited Speed (SLS, Extended Functions)](#description-of-safely-limited-speed-sls-extended-functions)
- [Description of Safe Speed Monitor (SSM, Extended Functions)](#description-of-safe-speed-monitor-ssm-extended-functions)
- [Description of Safe Direction (SDI, Extended Functions)](#description-of-safe-direction-sdi-extended-functions)
- [Description of Safe Brake Test (SBT, diagnostic function)](#description-of-safe-brake-test-sbt-diagnostic-function)
- [Description of Safely Limited Acceleration (SLA, Extended Functions)](#description-of-safely-limited-acceleration-sla-extended-functions)
- [Safety Integrated faults (Extended/Advanced Functions)](#safety-integrated-faults-extendedadvanced-functions)
- [Test stop of Extended/Advanced Functions](#test-stop-of-extendedadvanced-functions)
- [Reliable actual value acquisition with encoder system](#reliable-actual-value-acquisition-with-encoder-system)
- [Safe current actual value acquisition without encoder](#safe-current-actual-value-acquisition-without-encoder)

###### Description of Safe Torque Off (STO, Basic and Extended Functions)

Definition according to EN 61800-5-2:

"The STO function prevents energy from being supplied to the motor, which can generate a torque."

![Figure](images/147856991627_DV_resource.Stream@PNG-en-US.png)

###### Examples of how the function can be used

| Example | Possible solution |
| --- | --- |
| It is only permissible to open a protective door if the motor torque has been switched off. | - Select STO in the converter. - The pulses are suppressed and the motor coasts to a standstill. |

###### How does STO function in detail?

|  |  |  |
| --- | --- | --- |
| The converter recognizes the selection of STO via a fail-safe input or via the PROFIsafe safe communication.   The converter then safely switches off the torque of the connected motor. |  | ![How does STO function in detail?](images/147856996235_DV_resource.Stream@PNG-en-US.png) |

###### Description of Safe Stop 1 (SS1, Extended Functions)

Definition according to EN 61800-5-2:

"The SS1 function brakes the motor, monitors the magnitude of the motor deceleration within specified limits, and after a delay time or violation of a speed threshold, initiates the STO function."

![Figure](images/147857179659_DV_resource.Stream@PNG-en-US.png)

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| After an Emergency Stop button has been pressed, the drive must be braked as quickly as possible and brought into the STO state. | - Wire the Emergency Stop button with a fail-safe input. - Select SS1 via the fail-safe input. - SS1 brakes the drive and then brings it into the STO state. |
| A central Emergency Stop button ensures that several drives are braked as quickly as possible and brought into the STO state. | - Evaluate an emergency stop button in a central control. - Select SS1 via PROFIsafe. - SS1 brakes the drives and then brings them into the STO state. |

###### How does SS1 function in detail?

|  |  |  |
| --- | --- | --- |
| **Overview**    Using the SS1 function, the converter brakes the motor and monitors the absolute speed.  When the motor speed is low enough or the delay time has expired, the converter safely switches off the motor torque with STO. |  | ![How does SS1 function in detail?](images/147857184267_DV_resource.Stream@PNG-en-US.png) |

###### Selecting SS1

As soon as the converter detects that SS1 has been selected via a fail-safe input or via PROFIsafe safe communication, the following happens:

- If the motor has already been switched off when selecting SS1, then the converter safely switches off the motor torque (STO).
- If the motor is switched on when SS1 is selected, the converter brakes the motor with the OFF3 ramp-down time.

**Monitoring modes**

For the Extended Functions **with** or **without** encoder, you have the choice between two different monitoring modes of the SS1 function:

- "Brake ramp monitoring" (Safe Brake Ramp, SBR)
- "Acceleration monitoring" (Safe Acceleration Monitor, SAM)

| Brake ramp monitoring  (with or without encoder) | Acceleration monitoring  (with or without encoder) |
| --- | --- |
| ![Selecting SS1](images/147857195403_DV_resource.Stream@PNG-en-US.png) | ![Selecting SS1](images/147857200011_DV_resource.Stream@PNG-en-US.png) |
| - Using the SBR (Safe Brake Ramp) function, the converter monitors whether the motor speed decreases. - The gradient of the SBR function can be set via the reference velocity and the ramp-down time. The SBR function only starts after the "Delay for brake ramp". - The SBR function starts with the speed setpoint which was present at the time when SS1 was selected. - If the converter detects that the speed has fallen below the speed threshold (standstill monitoring), it safely switches off the motor torque (STO). | - The converter monitors the speed of the motor with the SAM function. - The converter prevents the motor from accelerating again by having the monitoring function continuously track the speed as it decreases. - The converter reduces the monitoring threshold until the "Shutdown speed" has been reached. - The converter safely switches off the motor torque (STO) when one of the following conditions is fulfilled:   - The speed has fallen below the shutdown speed SS1.   - The maximum time until the torque is switched off has expired. |

> **Note**
>
> **SS1 with external stop (SS1E)**
>
> If you use SS1E, neither of the two monitoring functions (SBR, SAM) is active. With SS1E, the drive must be shut down within the delay time, for example, via a CPU user program. STO becomes active after the delay time expires.

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SS1 (Extended Functions)](#ss1-extended-functions)."

---

**See also**

[Description of Safe Brake Control (SBC)](#description-of-safe-brake-control-sbc)

###### Description of Safe Brake Control (SBC, Extended Functions)

Definition according to EN 61800-5-2:

"The SBC function supplies a safe output signal to control a holding brake."

![Safe Brake Control (SBC)](images/147857066379_DV_resource.Stream@PNG-en-US.png)

Safe Brake Control (SBC)

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| The safe control of a motor holding brake must be guaranteed in order to guarantee the motor is at a standstill. | SBC (if configured) is triggered together with STO. The Motor Module / Safe Brake Relay / Safe Brake Adapter then carries out the action and safely controls the outputs for the brake. |

###### How does SBC function in detail?

|  |  |  |
| --- | --- | --- |
| The converter recognizes the selection of STO via a fail-safe input or via the PROFIsafe safe communication.   The converter then safely switches off the torque of the connected motor. |  | ![How does SBC function in detail?](images/147857071371_DV_resource.Stream@PNG-en-US.png) |
| SBC (if configured) is triggered together with STO. The Motor Module / Safe Brake Relay / Safe Brake Adapter then performs the action and safely controls the outputs for the brake. |  |  |

###### Description of Safe Operating Stop (SOS, Extended Functions)

Definition according to EN 61800-5-2:

"The SOS function is used for safe monitoring of the standstill position of a drive."

![Figure](images/147857233675_DV_resource.Stream@PNG-en-US.png)

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| It is only permissible to open a protective door when a motor is at safe standstill. | - Select SOS - A higher-level controller brakes the axis (e.g. position-controlled) down to standstill within the configured time between the selection of SOS and when it becomes active. - Standstill is then safely monitored via the SOS function. |

###### Method of operation

The protected machine areas can be entered without having to shut down the machine as long as SOS is active.

After SOS has been selected, it becomes active after the parameterizable delay time has expired. The drive must be braked to standstill within this delay time, e.g. by the controller.

Drive standstill is monitored via an SOS tolerance window. At the time this function becomes active, the current actual position is stored as the comparison position until SOS is deselected again. After SOS is deselected, there is no delay time and the drive can be immediately traversed.

The drive is stopped with SS1 when the standstill tolerance window is violated.

> **Note**
>
> **Contrary to SS1 and SS2, SOS does not automatically brake the drive**
>
> The controller still has setpoint control.
>
> This means that in the user program of the controller, the system must respond to the "SOS selected" bit so that the controller brings the drive to a standstill within the delay time.

![Standstill tolerance](images/147857238283_DV_resource.Stream@PNG-en-US.png)

Standstill tolerance

###### Description of Safe Stop 2 (SS2, Extended Functions)

Definition according to EN 61800-5-2:

"The SS2 function brakes the motor, monitors the magnitude of the motor deceleration within specified limits, and after a delay time, initiates the SOS function."

![Figure](images/147857281803_DV_resource.Stream@PNG-en-US.png)

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| It is only permissible to open a protective door when a motor is at safe standstill. | - Select SS2 in the converter via a terminal or via PROFIsafe. - After braking, the converter goes into the SOS state. Only then may the protective door be released. |

###### How does SS2 function in detail?

|  |  |  |
| --- | --- | --- |
| The safety function SS2 monitors the load speed and triggers the SOS function when the SS2 delay time has expired.   With SS2, braking is monitored on the OFF3 ramp. A faulty acceleration is detected and the drive is then shut down with STO. |  | ![How does SS2 function in detail?](images/147857286411_DV_resource.Stream@PNG-en-US.png) |

If you are operating the motor with torque control, the converter switches to speed control mode when SS2 is selected.

###### Detailed description

The fail-safe logic (e.g. F‑CPU) selects the SS2 safety function via a fail-safe input or via the PROFIsafe safe communication.

- If the motor is already at a standstill when SS2 is selected, the converter activates the Safe Operating Stop function (SOS) after a delay time.
- If the drive is not at standstill when SS2 is selected, it is braked along the OFF3 ramp. Braking is monitored with one of the following functions, depending on the setting in p9506:

  - "Safe Acceleration Monitor (SAM)"

    A faulty acceleration is detected.
  - "Safe Brake Ramp (SBR)"

    A violation of the brake ramp is detected.

  The converter activates the Safe Operating Stop function (SOS) after a delay time. This function monitors the safe standstill of the drive.

**Braking response**

![Braking response and diagnostics of the safety function SS2 (example of SS2 with SAM)           SS2DiagnosticsSS2Braking responseSS2Time responseSS2EnableSS2Selecting](images/147857297547_DV_resource.Stream@PNG-en-US.png)

Braking response and diagnostics of the safety function SS2 (example of SS2 with SAM)

> **Note**
>
> **SS2 with external stop (SS2E)**
>
> If you use SS2E, neither of the two monitoring functions (SBR, SAM) is active. With SS2E, the drive must be shut down within the delay time, for example, via a CPU user program. SOS becomes active after the delay time expires.

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SS2 (Extended Functions)](#ss2-extended-functions)."

###### Special features of SS2E and SS2ESR

In principle, the Safety Integrated Functions "SS2E" and "SS2ESR" work in a similar way to "SS2". Below are some differences as compared to "SS2 with OFF3":

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis motion**  When function "SS2E" (Safe Stop 2 with external stop) or SS2ESR (Safe Stop 2 with extended stop and retract) is active, the speed follows the setpoint of the higher-level control system during the delay time (p9553 or p9554). As a consequence, unexpected axis movements are possible, which could lead to severe injury or death.  - Prevent persons from entering the danger zone of the machine or system during the delay time (p9553 or p9554), for example, by keeping protective devices closed. |  |

![Selecting function SS2E (left) as compared to SS2ESR (right)](images/147857328907_DV_resource.Stream@PNG-en-US.png)

Selecting function SS2E (left) as compared to SS2ESR (right)

###### Differences to "Safe Stop 2 with OFF3"

| Differences between SS2 and SS2E | Differences between SS2 and SS2ESR |
| --- | --- |
| - If SS2E with external stop is selected, the drive does not brake the motor autonomously, but follows the defined speed setpoint. - During the delay time p9553, the brake ramp (SBR) and the acceleration (SAM) are not monitored and there is no standstill detection. - SOS becomes active after the delay time p9553 has expired.   If the SS2E function is active, the higher-level controller must define the speed setpoint in such a way that the motor is stopped no later than after the delay time p9553 has expired. - To enable SS2E, set p9501.18 = 1. - The PROFIsafe control word S_STW2.28 selects the SS2E function. PROFIsafe S_STW2.28 is contained in telegrams 31, 901, 902 and 903. - The PROFIsafe status word S_ZSW2.28 indicates whether the SS2E function is active. The PROFIsafe status word S_ZSW2.28 is contained in telegrams 31, 901, 902 and 903. The associated diagnostics parameter is r9722.28.   In the "Safety Info Channel," status word S_ZSW3B.11 indicates whether the SS2E function is active. The associated diagnostics parameter is r10234.11.   However, the diagnostic parameters p9722.28 and p10234.11 are also set during an internal STOP D. - Effect on the "Setpoint speed limit effective" (r9733[0...2]):   For SS2E (≙ STOP D), setpoint 0 is specified in r9733[0...2]. | - If SS2ESR with external stop is selected, the drive does not brake the motor autonomously, but follows the defined speed setpoint: This can also result in fast retraction motion. - During the delay time p9554, the brake ramp (SBR) and the acceleration (SAM) are not monitored, and there is no standstill detection. - SOS becomes active after the delay time p9554 has expired.    If function SS2ESR is active, the higher-level control system must define the speed setpoint in such a way that the motor is stopped no later than after the delay time p9554 has expired. - To enable SS2ESR, set p9501.4 = 1. - PROFIsafe control word S_STW2.29 selects function SS2ESR. PROFIsafe S_STW2.29 is contained in telegrams 31, 901, 902 and 903. - PROFIsafe status word S_ZSW2.27 indicates whether function SS2ESR is active. PROFIsafe status word S_ZSW2.27 is contained in telegrams 31, 901, 902 and 903. The associated diagnostics parameter is r9722.27. In the "Safety Info Channel," status word S_ZSW3B.12 indicates whether the SS2ESR function is active. The associated diagnostics parameter is r10234.12. - In addition, in the "Safety Info Channel", status word S_ZSW1B.14 = 1 is set. This bit corresponds to diagnostic parameter r9734.14. - You can use p0890[1] to interconnect to an ESR integrated in the drive. - SS2ESR has no effect on the "Setpoint velocity limit active" (r9733[0...2]). If SS2ESR is enabled in p9501.4, then a STOP E also has no effect on r9733[0...2]. |

###### Deselecting a Safety Integrated Function while it is active

![Deselecting SS2E or SS2ESR while it is active](images/147857333771_DV_resource.Stream@PNG-en-US.png)

Deselecting SS2E or SS2ESR while it is active

After the function has been selected, the delay time starts to elapse - even if the function is deselected during this time. In this case, after the delay time has expired, the SOS function is briefly active. Afterwards, it is permissible that the drive accelerates the motor back to the speed setpoint.

###### Interrupting active SS2E/SS2ESR with SS1 and SS2

![Interrupting the active Safety function with SS1 (left) and SS2 (right)](images/147857338635_DV_resource.Stream@PNG-en-US.png)

Interrupting the active Safety function with SS1 (left) and SS2 (right)

When SS1 is selected, the drive brakes the motor along the OFF3 ramp and monitors the speed using function SAM/SBR. Function STO becomes active when the motor is at a standstill.

When SS2 is selected, the drive also brakes the motor along the OFF3 ramp and monitors the speed using the SAM function. Function SOS becomes active after time p9552.

###### Description of Safely-Limited Speed (SLS, Extended Functions)

Definition according to EN 61800-5-2:

"The SLS function prevents the motor from exceeding the specified speed limit."

![Figure](images/147857367947_DV_resource.Stream@PNG-en-US.png)

###### Examples of how the function can be used

| Example | Possible solution |
| --- | --- |
| The machine operator must be able to enter the machine after the protective door has been opened and slowly move a horizontal conveyor with an acknowledgment button in the danger zone. | - Select SLS in the converter via a fail-safe input or PROFIsafe. - The converter limits and monitors the velocity of the horizontal conveyor. |
| A spindle drive, depending on the selection of the cutting tool, must not exceed a specific maximum velocity. | - Select the SLS and the corresponding SLS level in the converter via PROFIsafe. |

###### How does SLS function in detail?

|  |  |  |  |
| --- | --- | --- | --- |
| **Overview** |  |  |  |
| 1. | The converter recognizes the selection of SLS via a fail-safe input or via the PROFIsafe safe communication. |  | ![How does SLS function in detail?](images/147857379083_DV_resource.Stream@PNG-en-US.png) |
| 2. | SLS allows a motor to reduce its possibly excessively high speed within a defined time.  SLS monitors the absolute value of the actual velocity.  The SLS setpoint limit can be transferred to the higher-level motion controller (e.g. SIMOTION), where the velocity setpoint can be limited. |  |  |
|  | In addition, you can configure the setpoint limit provided by SLS as maximum speed in the ramp-function generator. In this case, SLS limits the speed setpoint. |  |  |
| 3. | SLS monitors the absolute value of the actual velocity.  The SLS setpoint limit can be transferred to the higher-level motion controller (e.g. SIMOTION), where the velocity setpoint can be limited.  In addition, you can configure the setpoint limit provided by SLS as maximum speed in the ramp-function generator. In this case, SLS limits the speed setpoint. |  |  |

> **Note**
>
> **SLS without selection**
>
> As an alternative to control via onboard terminals and/or PROFIsafe, there is also the option of parameterizing the SLS function without selection: In this case, the SLS function is permanently active after POWER ON. Details can be found in: "[SLS (Extended Functions)](#sls-extended-functions)"

###### Selecting SLS when the motor is switched on

As soon as the converter detects the selection of SLS via a fail-safe input or via PROFIsafe safe communication, the following happens:

- To avoid a limit value being violated, the setpoint limit can be transferred to the higher-level motion controller (e.g. SIMOTION). The higher-level motion controller can then limit the velocity setpoint.
- When the velocity setpoint limitation is interconnected to the ramp-function generator, the converter limits the speed to a value below the SLS monitoring.
- For SLS without encoder, you can select whether the converter monitors motor braking with the SBR (Safe Brake Ramp) function or not. For SLS with encoder, the SBR function cannot be selected.

| With brake ramp monitoring<sup>1)</sup> (only without encoder) | Without brake ramp monitoring (with or without encoder) |
| --- | --- |
| ![Selecting SLS when the motor is switched on](images/147857383691_DV_resource.Stream@PNG-en-US.png) | ![Selecting SLS when the motor is switched on](images/147857388299_DV_resource.Stream@PNG-en-US.png) |
| - After the adjustable "Delay time for brake ramp", the converter monitors whether the velocity decreases with the SBR (Safe Brake Ramp) function. - The converter switches from SBR to SLS as soon as one of the following two conditions is fulfilled:   - The SBR monitoring ramp has reached the value of the SLS monitoring. This case is shown in the figure above.   - After the actual velocity has reached the value of the SLS monitoring, the system again waits for the "delay time for brake ramp" until SLS becomes active. | - The converter monitors the load velocity after the "delay time for SLS switchover" has expired. |
| Advantages:  - The converter already detects during braking whether the load velocity is decreasing too slowly. - The "SLS active" feedback signal generally comes earlier than without acceleration monitoring. | Advantage:  - Commissioning is simplified, because instead of the SBR or SAM sub-function of the alternative brake ramp monitoring, you only have to set the delay time. |
| <sup>1)</sup> The automatic reduction of the speed only takes effect when the ramp-function generator is interconnected to the velocity setpoint limitation. |  |

###### Selecting SLS at low velocities

If the motor velocity when selecting SLS is less than the SLS limit, then the drive responds as follows:

![Selecting SLS at low velocities](images/147857392907_DV_resource.Stream@PNG-en-US.png)

**Deselecting SLS**

When the higher-level controller deselects SLS, the converter deactivates limitation and monitoring.

###### Switching over the monitoring limits

When SLS is active, you can switch between four different speed levels. An exception is "SLS without selection": In this case, there is only one limit.

**Switching to a lower speed level**

| With brake ramp monitoring<sup>1)</sup> (only without encoder) | Without brake ramp monitoring (with or without encoder) |
| --- | --- |
| ![Switching over the monitoring limits](images/147857397515_DV_resource.Stream@PNG-en-US.png) | ![Switching over the monitoring limits](images/147857402123_DV_resource.Stream@PNG-en-US.png) |
| - After the "delay time for brake ramp" has expired, the converter monitors the motor velocity with the SBR (Safe Brake Ramp) function. - The converter switches over from SBR monitoring to level 2 of SLS monitoring as soon as one of the following conditions is fulfilled:   - The SBR monitoring ramp has reached the value of the SLS monitoring. This case is shown in the figure above.   - The load velocity has decreased to the SLS monitoring value and the "delay time for brake ramp" has expired. | - The converter monitors the velocity with the lower SLS level after the "delay time for SLS switchover" has expired (this is the same delay time that applies after selecting the SLS function). |
| <sup>1)</sup> The automatic reduction of the speed only takes effect when the ramp-function generator is interconnected to the velocity setpoint limitation. |  |

**Switching to a higher speed level**

If you switch from a lower to a higher velocity level, the converter immediately monitors the actual velocity against the higher velocity.

![Switching over the monitoring limits](images/147857406731_DV_resource.Stream@PNG-en-US.png)

###### Switching the motor off and on (without encoder)

The time response and diagnostic options are as follows in this SLS variant:

![Time response of SLS without selection (example: Switching the motor off and on (without encoder))](images/147857411339_DV_resource.Stream@PNG-en-US.png)

Time response of SLS without selection (example: Switching the motor off and on (without encoder))

"SLS without selection" behaves as follows when switching off and on again:

- After switch-off, the motor behaves in accordance with the canceled signal (OFF1, OFF2 or OFF3).
- The "safe pulse suppression" becomes active after the standstill limit is undershot. If a brake has been parameterized, it is also closed.
- After the ON command, the converter cancels the "safe pulse suppression" state and the start procedure is initiated.
- If the minimum current has not been reached after 5 s, the converter returns into the "safe pulse suppression" state and triggers alarm C01711.

###### Description of Safe Speed Monitor (SSM, Extended Functions)

Definition according to EN 61800-5-2:

"The SSM function supplies a safe output signal to indicate whether the motor speed is below a specified limit value."

![Figure](images/147857415947_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **SSM is a pure signaling function**
>
> Unlike other Safety Integrated Functions, exceeding the SSM limit value does not result in a drive-autonomous stop response.

###### Example of how the function can be used

| Example | Possible solution |
| --- | --- |
| A centrifuge may only be filled below a velocity defined by the user. | - SSM is activated by configuring the Safety Integrated Extended Functions. - The converter safely monitors the centrifuge speed and enables the process to advance to the next step using the "SSM status" status bit. |

###### How does SSM function in detail?

**Requirements**

The SSM safety function cannot be selected or deselected by external control signals. SSM is active when you have set a monitoring speed &gt; 0 for SSM.

**Evaluating the speed**

The converter compares the load speed with the speed limit and signals if the limit value has undershot to the higher-level controller.

**Parameterizable hysteresis**

The parameterizable hysteresis ensures that the SSM output signal does not jump between the values "0" and "1" in the limit range.

![Time response of the SSM safety function (Safe Speed Monitor)SSMTime response](images/147857420555_DV_resource.Stream@PNG-en-US.png)

Time response of the SSM safety function (Safe Speed Monitor)

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SSM (Extended Functions)](#ssm-extended-functions)."

###### Description of Safe Direction (SDI, Extended Functions)

Definition according to EN 61800-5-2:

"The SDI function prevents the motor shaft from moving in the wrong direction."

![Figure](images/147857445771_DV_resource.Stream@PNG-en-US.png)

###### Examples of how the function can be used

| Example | Possible solution |
| --- | --- |
| A protective door must only be opened if a drive moves in the safe direction (away from the operator). | - Select SDI in the converter via a fail-safe input or PROFIsafe. - Enable the locking mechanism of the protective doors via the PROFIsafe status bit of the converter. |
| When replacing the pressure cylinders of the plates, the drive must only move in the safe direction of rotation. | - Select SDI in the converter via a fail-safe input or PROFIsafe. - In the converter, inhibit the direction of rotation that is not permitted. |
| Once the protection against jamming has been triggered, a roller shutter gate must only be able to start moving in one direction. |  |
| At an operational limit switch, the trolley of a crane must only be able to start in the opposite direction. |  |

###### How does SDI function in detail?

|  |  |  |
| --- | --- | --- |
| SDI monitors the current direction of rotation.   The SDI setpoint limit can be transferred to the higher-level motion controller (e.g. SIMOTION) to enable limitation of the velocity setpoint there.  In addition, you can configure the setpoint limit provided by SDI as maximum speed in the ramp-function generator. In this case, SDI limits the speed setpoint to the permissible direction. |  | ![How does SDI function in detail?](images/147857450379_DV_resource.Stream@PNG-en-US.png) |

You can select to block either the positive or the negative direction of rotation via two fail-safe signals (F-DIs or PROFIsafe).

###### Selecting and deselecting SDI

As soon as the converter detects that SDI has been selected via a fail-safe input or via PROFIsafe safe communication, the following happens:

- You can also set a delay time, within which you can ensure that the converter moves in the enabled (safe) direction.
- You can also set a tolerance, within which the converter tolerates movement in the direction that has not been enabled (unsafe). This prevents the triggering of faults during braking (overshoot) as well as in controlled standstill.
- After the delay time has expired, the converter monitors the direction of rotation of the motor.
- If the converter now moves in the blocked direction by more than the configured tolerance, a message is output and the defined stop response is initiated.

  ![Time response of the SDI safety function (Safe Direction)](images/147857454987_DV_resource.Stream@PNG-en-US.png)

  Time response of the SDI safety function (Safe Direction)

  > **Note**
  >
  > **SDI without selection**
  >
  > As an alternative to control via "onboard terminals" and/or "PROFIsafe", there is also the option of parameterizing SDI "without selection". In this case, SDI will be permanently active after POWER ON.

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SDI (Extended Functions)](#sdi-extended-functions)."

###### Description of Safe Brake Test (SBT, diagnostic function)

The diagnostic function "Safe Brake Test" function (SBT) checks the required holding torque of a brake (operating or holding brake).

You can test linear and rotary brakes. The drive purposely generates a force/torque against the applied brake. If the brake is operating correctly, the axis motion remains within a parameterized tolerance. If, however, a larger axis motion is detected, it must be assumed that the braking force/torque has deteriorated and maintenance is required.

![Figure](images/147857481867_DV_resource.Stream@PNG-en-US.png)

The "Safe Brake Test" function allows a safe test of up to two brakes:

- 1 motor holding brake and 1 external brake
- 2 external brakes
- 1 motor holding brake
- 1 external brake

The Safe Brake Test (SBT) diagnostic function meets the requirements for Category 2 according to EN ISO 13849‑1.

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SBT (diagnostic function)](#sbt-diagnostic-function)."

###### Description of Safely Limited Acceleration (SLA, Extended Functions)

Definition according to EN 61800-5-2:

"The SLA function prevents the motor from exceeding the defined acceleration limit."

![Figure](images/147857505291_DV_resource.Stream@PNG-en-US.png)

###### Examples of how the function can be used

| Example | Possible solution |
| --- | --- |
| The drive must not exceed the permissible acceleration in setup mode. | - Select SLA in the converter via PROFIsafe. - The converter limits and monitors the velocity of the machine. |

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SLA (Extended Functions)](#sla-extended-functions)".

###### Safety Integrated faults (Extended/Advanced Functions)

This section contains information on the following topics:

- [Stop responses (Extended/Advanced Functions)](#stop-responses-extendedadvanced-functions)
- [Stop response priorities (Extended Functions/Advanced Functions)](#stop-response-priorities-extended-functionsadvanced-functions)
- [Acknowledgment of the Safety Integrated faults (Extended/Advanced Functions)](#acknowledgment-of-the-safety-integrated-faults-extendedadvanced-functions)
- [Message buffer (Extended Functions/Advanced Functions)](#message-buffer-extended-functionsadvanced-functions)

###### Stop responses (Extended/Advanced Functions)

Faults with Safety Integrated Extended Functions, Safety Integrated Advanced Functions and violation of limits can trigger the following stop response:

Overview of stop responses

| Stop response | Triggered ... | Action | Effect |
| --- | --- | --- | --- |
| STOP A<sup>1) </sup>(corresponds to STO<sup>2)</sup>) | - For all acknowledgeable safety faults with pulse cancellation - Subsequent response of STOP B - Configurable subsequent stop p9563 for SLS - Configurable subsequent stop p9566 for SDI - Configurable subsequent stop p9562 for SLP | Immediate pulse cancellation | Drive coasts down |
| STOP B<sup>1) </sup>(corresponds to SS1<sup>3)</sup>) | Examples:  - Standstill tolerance violated in p9530 (SOS) - Configurable subsequent stop p9563 for SLS - Configurable subsequent stop p9566 for SDI - Configurable subsequent stop p9562 for SLP - Subsequent response of STOP F | Immediate input of speed setpoint = 0 and start of timer t<sub>B  </sub>Once t<sub>B</sub> or n<sub>act</sub> &lt; n<sub>shutdown</sub> has expired, STOP A is triggered. | STOP B with subsequent STOP A.  The drive decelerates along the OFF3 ramp and then switches to STOP A.   **Note:** For "SS1 with external stop" (SS1E), braking is **not** along the OFF3 ramp (see "[Description of Safe Stop 1 (SS1, Extended Functions)](#description-of-safe-stop-1-ss1-extended-functions)") |
| STOP C<sup>1) </sup>(corresponds to SS2<sup>4)</sup>) | - Configurable subsequent stop p9563 for SLS - Configurable subsequent stop p9566 for SDI - Configurable subsequent stop p9562 for SLP | Immediate input of speed setpoint = 0 and start of timer t<sub>C</sub>.  Once t<sub>C</sub> has elapsed, SOS is selected. | The drive decelerates along the OFF3 ramp; SOS is then selected. |
| STOP D<sup>1)</sup> | - Configurable subsequent stop p9563 for SLS - Configurable subsequent stop p9566 for SDI - Configurable subsequent stop p9562 for SLP | Timer t<sub>D</sub> starts.  No drive-integrated response.  SOS is activated on expiration of t<sub>D</sub>. | The drive must be decelerated by the higher-level controller (within the drive group)!  Once t<sub>D</sub> has elapsed, SOS is selected.  An automatic response is only triggered if the standstill tolerance window is violated in SOS. |
| STOP E<sup>1)</sup> | - Configurable subsequent stop p9563 for SLS - Configurable subsequent stop p9566 for SDI - Configurable subsequent stop p9562 for SLP | SOS triggered after the expiry of p9554 | Controlling the drive-integrated ESR functionality |
| STOP F<sup>1)</sup> | If an error occurs in the data cross-check. Follow-up response STOP B or STOP A | Timer t<sub>F1</sub> (Basic Functions) or t<sub>F2</sub> (Extended Functions)  No drive response | If a safety function (SOS, SLS) has been selected or if SSM with hysteresis has been enabled, transition to STOP A after t<sub>F1</sub> (Basic Functions) has elapsed or STOP B after t<sub>F2</sub> (Extended Functions) has elapsed. |
| <sup>1) </sup>See also the following note "delayed pulse cancellation when the bus fails".   <sup>2) </sup>The behavior of the drive after STOP A is triggered corresponds (apart from the safety messages) to the behavior after STO is triggered. Note that the parameterization of STO applies equally for STOP A.   <sup>3)</sup> The behavior of the drive after STOP B is triggered corresponds (apart from the safety messages) to the behavior after SS1 is triggered. Monitoring with the aid of SAM or SBR, for example, works in exactly the same way. Note that the parameterization of SS1 applies equally for STOP B.   <sup>4) </sup>The behavior of the drive after STOP C is triggered corresponds (apart from the safety messages) to the behavior after SS2 is triggered. Monitoring with the aid of SAM or SBR (for safety with encoder), for example, works in exactly the same way. Note that the parameterization of SS2 applies equally for STOP C. |  |  |  |

> **Note**
>
> **Delayed pulse cancellation when the bus fails**
>
> For SLP, SLS and SDI, the stop responses are also available with delayed pulse cancellation when the bus fails (so that the drive does not immediately respond with pulse cancellation when a communication error occurs):
>
> - If p9580 ≠ 0 and SLS is active, in the event of communication failure, the parameterized ESR reaction is only performed if, as the SLS response, a STOP with delayed pulse cancellation when the bus fails has been parameterized (p9563[0...3] ≥ 10).
> - If p9580 ≠ 0 and SDI is active, in the event of communication failure, the parameterized ESR reaction is only performed if, as the SDI response, a STOP with delayed pulse cancellation when the bus fails has been parameterized (p9566[0...3] ≥ 10).
> - If p9580 ≠ 0 and SLP is active, in the event of communication failure, the parameterized ESR reaction is only performed if, as the SLP response, a STOP with delayed pulse cancellation when the bus fails has been parameterized (p9562[0...3] ≥ 10).
>
> The delay time (p9580) must not exceed 800 ms.

> **Note**
>
> **Delay time between STOP F and STOP B**
>
> A delay time between STOP F and STOP B should only be set if an additional response is initiated during this time when the "Internal Event" (r9722.7) message signal is evaluated.
>
> Further, when using the delay time, a monitoring function should always be selected (e.g. SLS with a high limit speed) or the hysteresis of SSM should be configured.
>
> When hysteresis is activated for SSM, then this should be considered to be an activated monitoring function.

###### Switch-on delays at the stop response transitions

| Symbol | Meaning |
| --- | --- |
| t<sub>B</sub> | p9556 |
| t<sub>C</sub> | p9552 |
| t<sub>D</sub> | p9553 |
| t<sub>F1</sub> | p9658 |
| t<sub>F2</sub> | p9555 |
| n<sub>shutdown</sub>: | p9560 |

###### Description of faults and alarms

> **Note**
>
> **References**
>
> The faults and alarms for SINAMICS Safety Integrated are described in the following documentation:
>
> References: SINAMICS S120/S150 List Manual

###### Stop response priorities (Extended Functions/Advanced Functions)

Stop response priorities

| Priority classes | Stop response |
| --- | --- |
| Highest priority | STOP A |
| ..... | STOP B |
| ... | STOP C |
| .. | STOP D |
| .. | STOP E |
| Lowest priority | STOP F |

###### Priorities of stop responses and Extended Functions

Priorities of stop responses and Extended Functions

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Stop response/ Extended Function** |  | Highest priority | ... | ... | ... | ... | Lowest priority |
|  |  | **STOP A** | **STOP B** | **STOP C** | **STOP D** | **STOP E** | **STOP F** |
| Highest priority | **STO** | STOP A / STO | STO | STO | STO | STO | STO |
| ..... | **SS1** | STOP A | STOP B / SS1 | SS1 | SS1 | SS1 | SS1 |
| ... | **SS2** | STOP A | STOP B | STOP C / SS2 | SS2 | SS2 | SS2 / STOP B<sup>2)</sup> |
| .. | **SOS** | STOP A<sup>1)</sup> | STOP B<sup>1)</sup> | SOS | SOS | STOP E/SOS | STOP B<sup>2)</sup> |
| Lowest priority | **SLS** | STOP A<sup>3)</sup> | STOP B<sup>3)</sup> | STOP C<sup>4)</sup> | STOP D<sup>4)</sup> | STOP E<sup>4)</sup> | STOP B<sup>2)</sup> |
| <sup>1)</sup> The SOS monitoring function remains active, although the fault response in the event of a fault can no longer be triggered because it is already present.   <sup>2)</sup> STOP B is the subsequent stop of STOP F, which is activated after a parameterizable time. STOP F alone does not have any effect; the active safety function is still present.   <sup>3)</sup> The SLS monitoring function remains active, although the fault response in the event of a fault can no longer be triggered because it is already present.   <sup>4)</sup> SLS remains active during the braking phase, after which the system switches to SOS. |  |  |  |  |  |  |  |

The table above specifies which stop response / safety function is set if a STOP is triggered when a safety function is active. The STOPs are arranged here from left to right in descending order of priority (STOP A-F).

No overall priority is assigned in the individual safety functions. SOS remains active, for example, even if STO is requested. The safety functions that cause the drive to decelerate (SS1, SS2) are specified from top to bottom in descending order of priority.

If a field contains two entries, the stop responses and safety functions have the same priority. Explanation:

- STOP A corresponds to selecting STO
- STOP B corresponds to selecting SS1
- STOP C corresponds to selecting SS2
- STOP D corresponds to selecting SOS
- STOP E corresponds to selecting SOS (for additional activation of the standard "Extended stop and retract (ESR)" function)
- When the SS2 function is active, STOP F results in follow-up STOP B. SS2 remains active.

**Examples for illustrating the information in the table:**

- Safety function SS1 has just been selected. STOP A remains selected.
- By selecting a STOP with a higher priority, STOPs that are present with a lower priority will be replaced. This means that when SS1 is selected (≙ STOP B), any STOPs C-F that are present will be replaced.
- The SLS safety function is selected. This selection does not modify the function of STOP A-D. A STOP F now triggers a STOP B because a safety function has been activated.
- Stop response STOP C is selected. If the STO or SS1 safety functions are active, this does not have any effect. If SS2 is active, this brake ramp is retained. If SOS is active, SOS remains effective, which is also the end status of STOP C. When SLS is selected, the drive is decelerated with STOP C.

###### Acknowledgment of the Safety Integrated faults (Extended/Advanced Functions)

> **Note**
>
> **Acknowledgment through Power Off/On**
>
> Safety Integrated faults can also be acknowledged (as with all other faults) by switching the drive unit off and then on again (POWER ON).   
> If the fault cause has not been eliminated, the fault is displayed again immediately after ramp-up.

###### Acknowledgment via PROFIsafe

The higher-level controller sets the signal "Internal Event ACK" via the PROFIsafe telegram (STW bit 7) separately for each drive object. A falling edge in this signal resets the status "Internal Event" in the relevant drive, which therefore acknowledges the fault.  
Faults in the drive objects (DOs) cannot be acknowledged by the higher-level controller in the line-up but must instead be acknowledged separately for each individual drive object.

###### Extended acknowledgment

If STO or SS1 is selected/deselected (and p9507.0 = 1 are set), then the Safety messages are canceled automatically.

If, in addition to the "Basic Functions via onboard terminals", the "Extended Functions" are also enabled, then acknowledgment is also possible by selecting/deselecting STO via PROFIsafe.

###### Message buffer (Extended Functions/Advanced Functions)

In addition to the fault buffer for F... faults and the alarm buffer for A... alarms, a special message buffer for C... safety messages is available for Safety Integrated Extended Functions and Safety Integrated Advanced Functions.

The fault messages of the Safety Integrated Basic Functions are stored in the standard fault buffer.   
Detailed information about the standard fault buffers can be found at SINAMICS S120 Commissioning Manual with Startdrive in the "Messages - Faults and alarms" section.

> **Note**
>
> **Messages of the Basic, Extended, and Advanced Functions**
>
> Set parameter [p3117](SINAMICS%20Parameter%20CU.md#p3117-change-safety-message-type-1) = 1 if you need to save both the Basic Functions messages and the Extended Functions and Advanced Functions messages in the standard fault buffer.

The message buffer for Safety Integrated messages is similar to the fault buffer for fault messages. The message buffer comprises the message code, message value, and message time (received, resolved), the component number for identifying the affected SINAMICS component and diagnostic attributes. The following diagram shows how the message buffer is structured:

![Structure of the message bufferAlarm historyAlarmsAlarm historyAlarm valueAlarmsAlarm bufferAlarm buffer](images/147857612043_DV_resource.Stream@PNG-en-US.png)

Structure of the message buffer

When a Safety Integrated message is present, bit [r2139](SINAMICS%20Parameter%20CU.md#r2139015-cobo-status-word-faultsalarms-1).5 is set to 1 ("Safety Integrated message active"). The entry in the message buffer is delayed. For this reason, the message buffer should not be read until a change in the buffer ([r9744](SINAMICS%20Parameter%20SERVO.md#r9744-si-message-buffer-changes-counter)) has been detected after "Safety Integrated message active" is output.

The messages must be acknowledged via PROFIsafe.

**Properties of the Safety Integrated message buffer:**

- The entries appear in the buffer according to the time at which they occurred.
- If a new message case occurs, the message buffer is reorganized accordingly. The history is recorded in the "Acknowledged message case" 1 to 7.
- If the cause of at least one message in "Current message case" is rectified and acknowledged, the message buffer is reorganized accordingly. Messages that have not been rectified remain in "Current message case".
- If "Current message case" contains 8 messages and a new message for the current message case is output, the message in the current message case parameters is overwritten with the new message in index 7.
- r9744 is incremented each time the message buffer changes.
- A message value ([r9749](SINAMICS%20Parameter%20SERVO.md#r9749063-si-message-value), [r9753](SINAMICS%20Parameter%20SERVO.md#r9753063-si-message-value-for-float-values)) can be output for a message. The message value is used to diagnose the message more accurately (refer to the message description for more details).

**Deleting the message buffer:**

The message buffer can be deleted as follows: [p9752](SINAMICS%20Parameter%20SERVO.md#p9752-si-message-cases-counter) = 0. Parameter p9752 (SI message cases, counter) is also reset to 0 at POWER ON. This also clears the fault memory.

###### Additional parameters

- r2139
- r9744
- [r9745](SINAMICS%20Parameter%20SERVO.md#r9745063-si-components)
- [r9747](SINAMICS%20Parameter%20SERVO.md#r9747063-si-message-code)
- [r9748](SINAMICS%20Parameter%20SERVO.md#r9748063-si-message-time-received-in-milliseconds)
- r9749
- [r9750](SINAMICS%20Parameter%20SERVO.md#r9750063-si-diagnostic-attributes)
- p9752
- r9753
- [r9754](SINAMICS%20Parameter%20SERVO.md#r9754063-si-message-time-received-in-days)
- [r9755](SINAMICS%20Parameter%20SERVO.md#r9755063-si-message-time-removed-in-milliseconds)
- [r9756](SINAMICS%20Parameter%20SERVO.md#r9756063-si-message-time-removed-in-days)

---

###### Test stop of Extended/Advanced Functions

###### Requirements

- STO must not be selected before selecting the test stop.

  An STO is triggered when a test stop is performed for the Safety Integrated Functions.

###### Test of the shutdown paths (test stop) and function test

The functions and switch-off signal paths must be tested at least once within a defined period to establish whether they are working properly in order to meet the requirements of EN ISO 13849-1 and IEC 61508 in terms of timely error detection.

The maximum permissible interval for testing the shutdown paths (test stop) for Basic and Extended Functions is 8760 hours. The test of the shutdown paths (test stop) must therefore be performed at least once a year.

This must be implemented by initiating the test cyclically either manually or as part of an automated process.

The test stop cycle is monitored; on expiration of the parameterized timer (also after POWER ON/warm restart), the alarm A01697: "SI Motion: Test of motion monitoring required" is generated and a status bit is set which can be transferred to an output or to a PZD bit via BICO. This alarm does not affect machine operation.

###### Performing the test (test stop)

The test stop can be performed at the following points in time:

- Can be initiated application-specifically at a time suitable for the application:

  This functionality is implemented by means of a single-channel parameter p9705, which can be wired via BICO either to an input terminal on the drive unit (Control Unit) - or to a bit of any arbitrary PZD.

  If the test stop is executed as described, the action does not require a POWER ON. The acknowledgment is set by deselecting the test stop request.
- Automatically at POWER ON:

  - Even if you have parameterized the test stop for POWER ON, you can still initiate a test stop at any time through the application.
  - If the automatically initiated function cannot be correctly completed as a result of a problem (e.g. communication failure), the function will be automatically restarted after the problem has been resolved.
  - After the test stop has been performed successfully, the converter goes into the "Ready" state.
  - An automatic test stop resets timer p9559.
  - The automatic test stop for POWER ON does not affect the Safety Integrated Functions.

###### Safety devices

When the appropriate safety devices are implemented (e.g. protective doors), it can be assumed that running machinery will not pose any risk to personnel. The user is therefore only informed that the test of the shutdown paths is pending by an alarm, which requests the user to perform the test stop at the next possible opportunity.

Examples for the execution of the tests:

- When the drives are at a standstill after the system has been switched on (POWER ON).
- Before the protective door is opened.
- At defined intervals (e.g. every eight hours).
- In automatic mode (time and event-dependent).

###### Reliable actual value acquisition with encoder system

###### Supported encoder systems

The following encoder systems can in principle be used for safety-relevant velocity/position acquisition:

- Single-encoder systems

  ‑ or ‑
- 2-encoder systems

> **Note**
>
> **Rules for connecting an encoder**
>
> An encoder adjustment is essential after connecting an encoder.

###### 1-encoder system

In a single-encoder system, only the motor encoder is used to safely acquire the drive actual values. This motor encoder must be appropriately suitable (see encoder types). The actual values are generated in a safety-relevant fashion either directly in the encoder or in the Sensor Module and are transferred to the Control Unit via DRIVE-CLiQ.

For motors without a DRIVE-CLiQ interface, the connection is made using additional Sensor Modules.

Even if the drive is operating in the closed-loop torque controlled mode, motion monitoring functions may be selected as long as it is guaranteed that the encoder signals can be evaluated.

> **Note**
>
> **No "Safe acceleration monitoring" for encoder faults in a 1-encoder system**
>
> For an encoder fault in a 1-encoder system, the "Safe Acceleration Monitor" function (p9506 = 3) is not active.
>
> A stop response of category 0 or 1 (EN 60204-1) can be set in parameter p9516.4.

**Special feature in the case of linear motors**

The motor encoder (linear scale) of linear motors also acts as load measuring system. Only one measuring system is required for this reason. The system is connected by means of a Sensor Module or directly via DRIVE-CLiQ.

![Example of a single-encoder system](images/147857680395_DV_resource.Stream@PNG-en-US.png)

Example of a single-encoder system

###### 2-encoder system

The fail-safe actual values for a drive are provided by two separate encoders. The actual values are transferred to the Control Unit via DRIVE-CLiQ.

For motors without a DRIVE-CLiQ interface, the connection is made using additional Sensor Modules (see encoder types).

![Example of a 2-encoder system on a linear axis via a ball screw](images/147857660427_DV_resource.Stream@PNG-en-US.png)

Example of a 2-encoder system on a linear axis via a ball screw

![Example of a 2-encoder system on a rotary axis](images/147857670411_DV_resource.Stream@PNG-en-US.png)

Example of a 2-encoder system on a rotary axis

When parameterizing a 2-encoder system with Safety Integrated, you must align parameters p9315 to p9329 with parameters r0401 to r0474.

> **Note**
>
> **Assignment of the encoder parameters**
>
> Parameters p95xx are assigned to the 1st encoder; parameters p93xx to the 2nd encoder.

> **Note**
>
> **Transfer of the values from the encoder commissioning**
>
> To accept the values from the parameters filled during the encoder commissioning to the Safety Integrated parameterization, set parameter p9700 = 46 (2E hex). This copy function is only possible if you are connected online with the drive unit.

Encoder parameters and corresponding Safety parameters for 2-encoder systems

| Safety parameters | Designation | Encoder parameters |
| --- | --- | --- |
| p9315/p9515 SI Motion coarse position value configuration |  |  |
| p9315.0/p9515.0 | Up-counter | r0474[x].0 |
| p9315.1/p9515.1 | Encoder CRC, least significant byte first | r0474[x].1 |
| p9315.2/p9515.2 | Redundant coarse position value, most significant bit left-justified | r0474[x].2 |
| p9315.16/p9515.16 | DRIVE-CLiQ encoder | p0404[x].10 |
| p9316/p9516 SI Motion encoder configuration, safety functions |  |  |
| p9316.0/p9516.0 | Motor encoder, rotary/linear | p0404[x].0 |
| p9316.1/p9516.1 | Actual position value, sign change | p0410[x] |
| p9317/p9517 | SI Motion linear scale grid division | p0407 |
| p9318/p9518 | SI Motion encoder pulses per revolution | p0408 |
| p9319/p9519 | SI Motion fine resolution G1_XIST1 | p0418 |
| p9320/p9520 | SI Motion leadscrew pitch |  |
| p9321/p9521 | SI Motion gearbox encoder |  |
| p9322/p9522 | SI Motion gearbox encoder |  |
| p9323/p9523 | SI Motion redundant coarse position value valid bits | r0470 |
| p9324/p9524 | SI Motion redundant coarse position value fine resolution bits | r0471 |
| p9325/p9525 | SI Motion redundant coarse position value relevant bits | r0472 |
| p9326/p9526 | SI Motion encoder assignment |  |
| p9328/p9528 | SI Motion Sensor Module node identifier |  |
| p9329/p9529 | SI Motion Gx_XIST1 coarse position safety most significant bit | For DRIVE‑CLiQ encoders:  p0415 = r0470 – r0471 |
| For SMx modules: p0415 = 14 |  |  |

###### Encoder types for single and 2-encoder systems

Incremental encoders or absolute encoders can be used for safe acquisition of the position values on a drive.

The absolute position values can be transferred via the serial EnDat interface or an SSI interface to the controller. However, they are not evaluated by the Safety Integrated Functions.

In systems with encoders with SINAMICS Safety Integrated (single and 2-encoder systems), the following encoders are permitted for safe actual value acquisition:

- Encoders with sin/cos 1 Vpp signals

  - Single and 2-encoder systems
  - Connected to the SINAMICS SME20/25, SME120/125 and SMC20 Sensor Modules
  - The encoders must contain purely analog signal processing and creation. This is necessary to be able to prevent the A/B track signals with valid levels from becoming static ("freezing").
- HTL/TTL encoders

  - Can only be used for 2-encoder systems. In this case, one encoder must be an HTL/TTL encoder. The other encoder can be a sin/cos encoder or an HTL/TTL encoder.
  - Note the lowest possible velocity resolution (r9732[1]) for an HTL/TTL encoder system.

> **Note**
>
> **Encoders with integrated DRIVE-CLiQ interface**
>
> These encoders must be certified at least according to IEC 61800‑5‑2 (SIL2) or ISO 13849‑1 (Performance Level d / Category 3).

A fault mode effect analysis (FMEA) for securing the encoder on the motor shaft or on the linear drive must be performed. The result must be that the risk of the encoder mounting loosening is defined as a fault that can be ruled out (see DIN EN 61800‑5‑2, 2008, Table D.16). The encoder would no longer correctly map the motion if its mounting were to become loose.

It should be noted that the machine manufacturer has sole responsibility for the fulfillment of the above-described requirements. Information on the internal realization of the encoder must come from the encoder manufacturer. The FMEA must be created by the machine manufacturer.

Siemens motors with and without DRIVE-CLiQ connection, which can be used for Safety Integrated Functions, are listed at:

[Siemens motors for Safety Integrated](https://support.industry.siemens.com/cs/ww/en/view/33512621)

For these motors, the encoder mounting on the motor shaft can be considered to be safety relevant, and faults associated with an encoder becoming loose ruled out.

> **Note**
>
> **Basic absolute encoders with EnDat interface and additional sin/cos tracks**
>
> Basic absolute encoders (e.g. EQI) that offer an EnDat interface with additional sin/cos tracks, but operate according to an inductive measuring principle internally, are not permitted for SINAMICS Safety Integrated.

###### Actual value synchronization

![Example diagram of actual value synchronization](images/147857694347_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | This deviation cannot be larger than the position difference that can arise at maximum slip (p9549) during a cross-check clock (r9724). |

Example diagram of actual value synchronization

The mean value of the actual values of both channels is calculated cyclically after actual value synchronization (p9501.3 = 1) has been activated, for example, for systems or machines with slip. The maximum slip defined in p9549 is monitored in the cross-check clock (r9724). Whereby, the maximum slip defined in p9549 is monitored once per cross-check clock (r9724).

If "actual value synchronization" is not enabled, the value parameterized in p9542 is used as tolerance value for the crosswise comparison.

###### Safe motion monitoring

The properties of the actual value acquisition determine not only the encoders used, but also the values for safe motion monitoring that can be achieved in the best case:

- Safe maximum speed (r9730)

  The maximum speed (load side) that is permissible due to the acquisition of actual values for safe motion monitoring functions is indicated in r9730. This parameter shows the load velocity up to which the safety-relevant encoder actual values (redundant coarse encoder position) can still be correctly sensed as a result of the particular encoder parameterization.

  The actual value acquisition clock (p9511) determines the frequency at which the actual values are acquired. The longer the clock, the higher the "safe maximum velocity." On the other hand, a longer actual value acquisition clock places a greater load on the Control Unit. You must consider this circumstance when setting the optimum for your application.
- Safe positioning accuracy (r9731)

  This positioning accuracy can be achieved in the best case by acquiring the actual values. If a 2-encoder system is used, the accuracy of the poorer encoder is indicated based on the number of encoder pulses.

###### Safe current actual value acquisition without encoder

Several parameters are available in order to guarantee safe motion monitoring for Safety Extended Functions without encoder depending on the situation in a specific application. In most cases, you can work with the default values.

- If, during the start phase, the actual value acquisition is still not operating correctly, the converter outputs messages; however these still do not represent any Safety problems. In order to avoid this, increase this value of parameter  **Delay time of the evaluation encoderless** (p9586). In this way, you determine the "Evaluation delay time without encoder" (p9586):

  - To determine the minimum delay time of p9586, record the starting behavior of the drive system (with motor and the intended load). The trace function allows the value for p9586 to be determined.
  - In order to avoid fault responses, deselect the "SDI without encoder" and "SLS without encoder" functions.
  - Activate the trace function using the "OFF2 → inactive" trigger, and the following as the signals to be recorded: At least one motor current phase and OFF2. After the ON command, record this motor phase current until I<sub>rated</sub> is reached. Enter the time required to reach I<sub>min</sub> (+ 10% reserve) in p9586.
  - Perform application-specific startup characteristics for the drive. Deduct from the trace recording the time after which the peak current of the induction motor or the pulse pattern of the rotor position identification finishes, and the current of p9588 which exceeds the "Minimum current actual value acquisition without encoder".
  - Enter the measured time + approx. 10 % into p9586.
  - Activate the "SDI without encoder" and "SLS without encoder" functions. Restart the machine, and keep the trace function activated.

    Now it is no longer permissible that messages are output.
  - Alternatively, you can change the value of p9586 in small steps and then monitor the system response. You have found a suitable value if unnecessary messages/signals no longer occur.
- Using parameter **Fault tolerance actual value acquisition encoderless** (p9585), you can set the tolerance of the plausibility monitoring of current and voltage angle.

  - For synchronous motors, p9585 = 4 must be parameterized.
  - Reducing this value can have a negative impact on the actual value acquisition and the plausibility check.
  - Increasing the value results in a longer evaluation delay.
  - For devices in the chassis format, Safety Integrated without encoder can be used with induction motors up to a maximum of 1000 kW: For very large motors, it may be necessary to increase the value in parameter p9585. For chassis format devices, parameter p9585 is preassigned a value of "2".
  - For the factory setting (= -1), for synchronous motors, the calculation automatically uses the value 4, for induction motors, the value 0.
  - The diagnostics parameter r9786[0...2] shows you the values of the plausibility angle, voltage angle and current angle currently measured by the converter. These values allow you to optimize what you enter into p9585.
- The field **Voltage tolerance acceleration** (p9589) is used to suppress acceleration peaks. An increase in this percentage value means that voltage peaks must have a greater amplitude during acceleration operations to avoid influencing actual value acquisition.
- Set the value of **voltage tolerance acceleration** (p9589) as follows:

  - The diagnostics parameter r9784[0...1] shows the parameterized and the actual measured acceleration value. These values allow you to optimize what you enter in p9589.
  - Record the following parameters with the trace function in the current controller clock:

    - r9784[0]: Target acceleration value

    - r9784[1]: Actual acceleration value

    - r9714[0]: load side actual velocity value on the Control Unit

    - r0063: Actual speed value
  - Accelerate the motor , if possible until it reaches the rated speed.
  - Check whether r9714[0] and r0063 match in the range 0 … rated speed.
  - Set p9589 such that r9784[1] touches r9784[0] a maximum of twice per second in the range 0 … rated speed.

    - If the value if the message C01711 with fault value 1043 occurs, you have to increase p9589.

    - The value must be decreased if acceleration has resulted in an excessive Safety actual velocity.
  - Check once again whether r9714[0] and r0063 match in the range 0 … rated speed.

  If you change one of the following parameters, you have to check and set the encoderless actual value acquisition once again:

  - PROFIdrive isochronous mode asynchronous participation:

    p2049 = 1
  - Current controller sampling time for servo control:

    p0115[0] = 187.5 µs, 150 µs, 100 µs, 93.75 µs, 75 µs, 50.0 µs or 37.5 µs
  - Current controller sampling time for vector control:

    p0115[0] = 375 µs, 312.5 µs, 218.75 µs, 200 µs, 187.5 µs, 175 µs, 156.25 µs, 150 µs or 137.5 µs

##### Advanced Functions

This section contains information on the following topics:

- [Description of Safely-Limited Position (SLP, Advanced Functions)](#description-of-safely-limited-position-slp-advanced-functions)
- [Transferring safe position values (SP, Advanced Functions)](#transferring-safe-position-values-sp-advanced-functions)
- [Description of Safe Cam (SCA, Advanced Functions)](#description-of-safe-cam-sca-advanced-functions)
- [Description of "Safe homing" (Advanced Functions)](#description-of-safe-homing-advanced-functions)

###### Description of Safely-Limited Position (SLP, Advanced Functions)

Definition according to EN 61800-5-2:

"The SLP function prevents the motor shaft from exceeding the specified position limit(s)."

![Figure](images/147857770763_DV_resource.Stream@PNG-en-US.png)

The "Safely-Limited Position" function (SLP) is used to safely monitor the limits of two traversing and/or positioning ranges, which are toggled between using a safe signal.

###### Examples of how the function can be used

| Example | Possible solution |
| --- | --- |
| The drive must not exit the specified position ranges. | - Selection of SLP in the converter; inhibiting the range that is not permitted. - After the enabled range has been exited, a parameterizable stop response is initiated. |

###### Function features

- Selection via onboard terminals or PROFIsafe
- Two position ranges, each defined by a limit switch pair
- Safe switchover between the two position ranges
- Adjustable stop response
- To traverse the motor out of the prohibited range, you must perform a special sequence.

###### Requirements

- The function is only available with a suitable encoder.
- The drive must be safely homed (see "[Description of "Safe homing" (Advanced Functions)](#description-of-safe-homing-advanced-functions)").

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SLP (Advanced Functions)](#slp-advanced-functions)."

###### Transferring safe position values (SP, Advanced Functions)

The "Safe Position (SP)" function enables you to transfer safe position values to the higher-level fail-safe controller (F-CPU) via PROFIsafe (telegram 901 or 902).

From the position change over time, the F‑CPU can also calculate the current velocity. In telegram 902, the values are transferred in 32-bit format, in telegram 901, in 16-bit format.

![Figure](images/147857809803_DV_resource.Stream@PNG-en-US.png)

After parameter assignment, release and POWER ON, the function is automatically selected and the values transferred. Please observe the following:

- For use as the safe absolute position, the "Absolute position" must also be enabled and then safely referenced.
- In order that the transferred position can be used, the actual position value must be valid.

Using the time stamp that is also transferred, you can also calculate the velocity from the position values in the higher-level fail-safe controller. If you only want to calculate the velocity, it is sufficient to enable the "Transfer of safe position values" without the "Absolute position."

###### Description of Safe Cam (SCA, Advanced Functions)

Definition according to EN 61800-5-2:

The "Safe Cam" (SCA) function supplies a safe output signal to indicate whether the motor shaft position lies within a defined range.

![Figure](images/147857834635_DV_resource.Stream@PNG-en-US.png)

The "Safe Cam" function outputs a safe signal when the drive is within a specified position range. This function implements the identification of a safe range for each axis.

###### Details and parameterization

For further details and information on how to parameterize this function, see "[SCA (Advanced Functions)](#sca-advanced-functions)."

###### Description of "Safe homing" (Advanced Functions)

###### Details and parameterization

For further details and information on how to parameterize this function, see "[Safe homing (Advanced Functions)](#safe-homing-advanced-functions)."

##### Difference between Emergency Off and Emergency Stop

"Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.

| Symbol | Meaning |
| --- | --- |
| **Emergency Off**   Risk of electric shock.    ![Figure](images/147857881867_DV_resource.Stream@PNG-en-US.png) | **Emergency Stop**   Risk of unexpected motion.    ![Figure](images/147857886091_DV_resource.Stream@PNG-en-US.png) |

Measures and solutions

| Command | Emergency Off | Emergency Stop |
| --- | --- | --- |
| Measure to minimize risk | **Safe switch off**   Switching off the electric power supply for the installation, either completely or partially. | **Safely stop and safely prevent restarting**   Stopping or preventing the dangerous movement |
| Classic solution | Switch off the power supply.    ![Figure](images/147857890315_DV_resource.Stream@PNG-en-US.png) | Switch off the drive power supply.    ![Figure](images/147857894539_DV_resource.Stream@PNG-en-US.png) |
| Solution with the STO safety function integrated in the drive | STO is not suitable for safely switching off a voltage. | Select STO.    ![Figure](images/147857898763_DV_resource.Stream@PNG-en-US.png)   It is permissible that you switch off the converter power supply as well. However, switching off the voltage is not required as a risk-reduction measure. |

#### Basic settings

This section contains information on the following topics:

- [License for Extended/Advanced Functions required](#license-for-extendedadvanced-functions-required)
- [Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)
- [Selecting the safety functionality](#selecting-the-safety-functionality)
- [Distinction: With encoder / without encoder](#distinction-with-encoder-without-encoder)
- [Accepting the safety settings](#accepting-the-safety-settings)
- [Changing the Safety Integrated password](#changing-the-safety-integrated-password)

##### License for Extended/Advanced Functions required

For operation of the Safety Integrated Extended Functions or Safety Integrated Advanced Functions, one license is required for each axis. An insufficient license is indicated via the following fault and LED:

- F13000 → Insufficient license
- LED RDY → flashes red at 2 Hz

  ![Figure](images/147857939211_DV_resource.Stream@PNG-en-US.png)

**License overview**

Startdrive provides a "License overview" page. This shows the most important information about the licenses and the license status of your drive system; see [License overview](Configuring%20SINAMICS%20S-G-MV%20drives.md#overview-of-licenses).

**Trial License Mode**

The drive can only be operated with an insufficient license for an option during commissioning and servicing. For this purpose, the Trial License Mode must be activated explicitly, see [Trial License Mode](Configuring%20SINAMICS%20S-G-MV%20drives.md#activate-trial-license-mode).

**Displaying/acquiring the license key**

The "License overview" page shows the currently entered license key and you can enter a new license key; see [License key](Configuring%20SINAMICS%20S-G-MV%20drives.md#displayingentering-a-license-key).

##### Starting and Ending Safety Integrated commissioning

###### Requirement

For safety reasons, you can only set the Safety Integrated-relevant parameters of the 1st channel offline with the Startdrive commissioning tool. If the drive is online, the data of the 1st channel is automatically duplicated in the 2nd channel. You can protect the settings with a password.

###### Activate/deactivate editing mode

The editing mode must be activated in the online mode in order to configure the safety functions.

| Symbol/button | Description |
| --- | --- |
| ![Activate/deactivate editing mode](images/147854075915_DV_resource.Stream@PNG-en-US.png) | Startdrive is not online. You can only edit the Safety Integrated Functions offline.   - Activate the online mode. |
| ![Activate/deactivate editing mode](images/147854079883_DV_resource.Stream@PNG-en-US.png) | Status: The editing mode is not activated yet.   - Click the ![Activate/deactivate editing mode](images/147857968779_DV_resource.Stream@PNG-en-US.png) icon to activate the editing mode. |
| ![Activate/deactivate editing mode](images/147854083851_DV_resource.Stream@PNG-en-US.png) | Status: The editing mode is active. In addition to the safety marking, a "pencil" ![Activate/deactivate editing mode](images/147857964811_DV_resource.Stream@PNG-en-US.png) is displayed in the secondary navigation.   - Click the ![Activate/deactivate editing mode](images/147857972747_DV_resource.Stream@PNG-en-US.png) icon to exit the editing mode. |

###### Activating the Safety Integrated settings and entering the password​

Proceed as follows to activate the Safety Integrated settings:

1. Click the "Connect online" symbol.
2. Click the ![Activating the Safety Integrated settings and entering the password​](images/147857968779_DV_resource.Stream@PNG-en-US.png) symbol in the toolbar of the parameterization editor.

   The "Password input" screen form is displayed.
3. Enter the password.

   You only have to enter a new password at the first start to replace the "not secure" default password.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

##### Selecting the safety functionality

###### Making basic settings

1. In the secondary navigation, execute "Safety Integrated &gt; Function selection".
2. Select between the following in the first drop-down list:

   - No Safety Integrated Function
   - Basic Functions
   - Extended/Advanced Functions

     A drop-down list for setting the encoder option becomes active:
3. Select the desired encoder option in the second drop-down list for the "Extended/Advanced Functions":

   - with encoder
   - without encoder
4. Select from the "Control type" drop-down list between:

   - via onboard terminals

     (all Safety Integrated Functions with CU310-2; only Basic Functions with CU320-2)

     if you want to use the fail-safe digital I/Os of a drive.
   - via PROFIsafe

     if you want to control the safety functions from a higher-level controller (see [Control](#control)).
   - without selection

     (only for SBC, SBT, SDI and SLS. SBT only for Extended/Advanced Functions with encoder)
5. Activate the "Basic Functions via onboard terminals" option.

   With this setting, you can use the fail-safe digital I/Os of a drive as well as control the safety functions from a higher-level controller (see [Control](#control)).

   The "Basic Functions via onboard terminals" option can be selected for the following settings:

   - "Basic Functions" with "via PROFIsafe" control type
   - "Extended/Advanced Functions" with "via PROFIsafe" control type
   - "Extended/Advanced Functions" with "without selection" control type
6. Then activate the Safety Integrated Functions that you require in the lower part of the dialog.

   Startdrive only displays the functions that belong to the function selection you made. The preselected functions cannot be deselected. The entries for the selected and preselected functions are displayed in the secondary navigation.
7. Click the buttons (or the entry in the secondary navigation) to parameterize the desired Safety function.

###### Result

The basic settings for Safety Integrated have been made. The desired Safety Integrated Functions have been activated and also enabled with the activation. The activated Safety Integrated Functions are active with specified default settings. You can change these default settings in the Details screen forms according to your requirements.

###### Further Safety settings:

- [Basic functions](#basic-functions-1)
- [Extended Functions](#extended-functions-1)
- [Advanced Functions](#advanced-functions-1)
- [Test stop](#test-stop)
- [Control](#control)
- [Acceptance mode](#acceptance-mode)
- [SINAMICS Safety Integrated acceptance test](Safety%20Integrated%20acceptance%20test.md#sinamics-safety-integrated-acceptance-test)

##### Distinction: With encoder / without encoder

This section contains information on the following topics:

- [Differences between Extended Functions "with encoder" and "without encoder"](#differences-between-extended-functions-with-encoder-and-without-encoder)
- [Restrictions for Extended Functions "without encoder"](#restrictions-for-extended-functions-without-encoder)

###### Differences between Extended Functions "with encoder" and "without encoder"

If motors without a (safety-capable) encoder are being used, not all Safety Integrated Functions can be used. You will find general information on this distinction in "[Safety Integrated overview (S/G drives)](#safety-integrated-overview-sg-drives)."

###### Without encoder: Slip of the induction motor

For Safety Integrated without encoder (depending on the drive load), as a result of slip (deviations between electrical and mechanical speed), deviations can occur between the safely determined electrical speed and the mechanical speed at the motor shaft.

> **Note**
>
> **Safety Integrated Functions "without encoder" for group drives**
>
> The Safety Integrated Functions "without encoder" are also permitted for group drives (several motors connected to one power unit).

> **Note**
>
> Sudden changes in the current and voltage curve (e.g. sudden change in the setpoint setting and load) and very small absolute values with a high proportion of noise generally result in faults of the safe encoderless actual value acquisition and must be avoided.

###### With encoder: "Parking" state

> **Note**
>
> **Extended Functions with encoder and "parking"**
>
> When a drive object for which Safety Integrated Extended Functions with encoder are enabled is switched to "Park" mode, the Safety Integrated software responds by selecting STO without generating a separate message. This internal STO selection is displayed in parameter r9772.19.

###### Restrictions for Extended Functions "without encoder"

Extended Functions SS1, SLS, SDI and SSM "without encoder" do not require safety-related actual speed value acquisition. If an encoder is used for the drive control, this has no influence on the encoderless safety functions. They can be used with induction motors in all control types, as well as with "SIMOTICS A-1FU" synchronous motors with V/f control.

###### Illegal operating modes

- Current controller clocks 31.25 µs and 62.5 μs (for Double Motor Modules with two configured Safety Integrated drives).
- For the independent setting of the current controller clock and pulse frequency in conjunction with Safety Integrated "without encoder":

  - Double Motor Module: &lt; 125 μs
  - All other components: &lt; 62.5 μs
  - p9589 must be set = 3300 to allow the current controller clock and pulse frequency to be independently set.
- "Shaft generator" functionality
- Induction motors up to 1000 kW

  On very large machines, it may also be necessary to adjust parameter p9585.
- For devices in "chassis" format, the following also applies:

  - For devices in "chassis" format, operation without encoder is permissible only for induction motors.
  - No operation involving parallel connections
  - Optimized pulse patterns cannot be selected for SIMOTICS FD
  - Only using parameter p1810 = factory setting, this includes:

    - No wobbling

    - No fine setting of the pulse frequency

###### Critical operating modes

In irregular operating states (e.g. "stalled motor"), the converter can fail with Safety faults. However, under no circumstances is an unsafe state reached.

When the safety functions are deactivated, the following technology functions are not negatively influenced.

When using the following operating modes with the Safety Integrated Functions activated without encoder, this can result in errors in the encoderless safe actual value acquisition (see messages C01711, C30711 with fault values 1040 ff.).

Safe, encoderless actual value acquisition is based on the measurement of current and voltage variables, which can influence the following functions. This does not result in unsafe states. However, this fault can be expected to have a negative impact on availability.

- Current limiting of the power unit

  When the current limitation of the power unit responds, a fault of the encoderless safe actual value acquisition and a consequent stop response can be expected.

  > **Note**
  >
  > When engineering the drive and when the parameterizing the current and torque limits, it must be ensured that the power unit current limiting does not respond.
- Operation with pulling loads

  It is not permissible that the converter is forced into regenerative operation as a result of external forces.

  > **Note**
  >
  > Safety functions without encoder can be used when a coupled drive comprises a motorized and regenerative electric drive (e.g. a test stand), and the velocities of both drives are safely monitored. In the case of a fault, the motoring drive recognizes when a limit value is violated.
  >
  > Safety functions without encoder are not permitted for the braking drive when the motoring drive (e.g. an internal combustion engine) is not safely monitored.
  >
  > Winders with a motoring and a braking drive can be assessed in the same way (both drives are monitored).
- Motor data identification

  When using the measuring functions (stationary and rotating measurement) to determine the motor data, then it can be assumed that the encoderless safe actual value acquisition will have an error.

  > **Note**
  >
  > The motor data identification should always be performed before commissioning the Safety Integrated Functions.
- Dataset switchover

  The motor and drive dataset switchover can always be used for safety functions without encoder. It is not possible to switch over between induction and synchronous motors (this is interlocked). For several motor datasets it must be ensured that all motors have the same number of pole pairs. If the number of pole pairs in r0313 is not the same value that was taken into account when configuring the safe actual value acquisition (gearbox), then the calculated, safe actual speed no longer corresponds to the mechanical speed of the shaft.

  When SLS is activated, the shaft can rotate faster than the configured limits.
- Alternating acceleration/deceleration

  For alternating acceleration and deceleration, it must be ensured that the following conditions are maintained.

  - Within 1 s, only one acceleration and one braking ramp are permitted.

    Therefore, for a cycle 0 → +n<sub>set</sub> → -n<sub>set</sub> → 0 – one period of at least 2 s is required.
- This also applies to positioning operation; it may be necessary that the position control settings and traversing profiles must be adapted so that no overshoots occur in the speed characteristic (e.g. reduce the dynamic response, use flatter braking ramps).
- Flying restart

  A flying restart should not be performed in operation with the Safety Integrated Functions active.
- DC brake

  When using this function, DC current is impressed to brake the drive: This can result in a fault of the encoderless safe actual value acquisition and a consequent stop response.

###### Recommendations for stable operation

The following requirements must be fulfilled to avoid fault messages from the safe actual value acquisition without encoder:

- Motor and the power unit must be adequately dimensioned for this application.
- Motor and power unit should fulfill the following condition:   
  The ratio between the rated power unit current (r0207[0]) and rated motor current (p0305) must be less than 5.
- Before commissioning the Safety Integrated Functions, identify the motor data at standstill and perform a rotating measurement.
- For the basic commissioning, i.e. before the Safety Integrated commissioning, the closed-loop control should be optimally set.   
  Avoid the following effects:

  - Speed overshoots
  - Current peaks and discontinuous actual current values over time
  - Voltage peaks and discontinuous actual voltage values over time
  - The lowest possible amount of noise in the current and voltage

##### Accepting the safety settings

After you have parameterized all safety functions, the drive must accept the settings.

1. To accept the settings and deactivate the safety functions, click the symbol in the title bar.

   ![Figure](images/147858070923_DV_resource.Stream@PNG-en-US.png)

   ![Figure](images/147858070923_DV_resource.Stream@PNG-en-US.png)

   The following steps are executed:

   - The parameter settings are copied from CPU 1 to CPU 2.
   - Copy RAM to ROM is offered.
   - Safety mode is deactivated, the symbol now has a yellow border.
2. Terminate the online connection to the drive.

You can now continue with the parameter assignment of the "normal" settings. The dialog are no longer deactivated.

##### Changing the Safety Integrated password

The Safety Integrated password protects Safety Integrated parameters against maloperation. Always assign a strong password, to enable protection. To reset the password to the factory setting, you require the valid password.

> **Note**
>
> The Safety password is write protection specified in the appropriate standards to prevent against maloperation by unauthorized users.
>
> The password must include the following elements to provide better protection against unauthorized access, e.g. by hackers:
>
> - At least 8 characters
> - Upper and lower case letters
> - Numbers and special characters (e.g.: ?!%+ ...)
>
> The Safety password must not be used anywhere else.
>
> **Checking the password**
>
> The drive checks the length of the password. There is no check for special characters or upper and lower case letters.

> **Note**
>
> **Project protection to encrypt passwords**
>
> Using a message ![Figure](images/147853400715_DV_resource.Stream@PNG-en-US.PNG), Startdrive recommends encrypting Safety Integrated passwords using the project protection ("Security settings").
>
> - If you activate project protection for user administration in the TIA Portal, then all parameters and passwords within the project are encrypted.
>
> Detailed information on project protection can be found in the online help under "[Managing users and roles](Managing%20users%20and%20roles.md#managing-users-and-roles)".

###### Requirement

- The drive axis is ONLINE.

  The Safety Integrated password can only be read or changed in online mode.

###### Changing the Safety Integrated password

To change the Safety Integrated password, proceed as follows:

1. Click "Enter password" in the secondary navigation.
2. Enter the current password.
3. Enter the new password.
4. Repeat entry of the new password.
5. Click the "Change password" button to accept the new password.

#### Basic functions

This section contains information on the following topics:

- [STO/SS1/SBC (Basic Functions)](#stoss1sbc-basic-functions)

##### STO/SS1/SBC (Basic Functions)

###### Description

Here you can parameterize the Safe Torque Off (STO), Safe Stop 1 (SS1) and Safe Brake Control (SBC) functions via onboard terminals and PROFIsafe.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858142475_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Torque Off (STO, Basic and Extended Functions)](#description-of-safe-torque-off-sto-basic-and-extended-functions) |
| ![Description](images/147858146443_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Stop 1 (SS1, Basic Functions)](#description-of-safe-stop-1-ss1-basic-functions) |
| ![Description](images/147858150411_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Brake Control (SBC)](#description-of-safe-brake-control-sbc) |

The function is enabled simultaneously with the selection. STO and SS1 cannot be deactivated for the Basic Functions.

###### Configuring Safety Integrated Functions

The Safety Integrated Basic Functions are only partly configured in the "STO/SS1/SBC" screen form. Most of the configuration is performed in other screen forms. Below you will find a procedure if you want to configure all three Safety Integrated Basic Functions.

1. Call the "STO/SS1/SBC" function.

   The screen form of the same name opens.
2. Click the ![Configuring Safety Integrated Functions](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select STO) to configure the "STO" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Basic Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
3. Call the "STO/SS1/SBC" function again.
4. To configure the "SS1" function, set the delay time until the start of "STO" in the "Safe Stop 1 delay time" ([p9652](SINAMICS%20Parameter%20SERVO.md#p9652-si-safe-stop-1-delay-time)) field.
5. Then connect the signal source [r9773](SINAMICS%20Parameter%20SERVO.md#r9773031-cobo-si-status-control-unit-motor-module).1 for the "STO active in drive" signal.
6. Click the ![Configuring Safety Integrated Functions](images/147858158475_DV_resource.Stream@PNG-en-US.png) button (brake control) to configure the "SBC" function.

   The "Brake control" screen form opens.

   Configure the brake control here (see "[Brake control](#brake-control)").
7. Click "Save project" in the toolbar to save the changes in the project.

**Result**

You have configured the Safety Integrated Basic Functions.

###### General function diagrams (FD)

SI Basic Functions - Parameter manager - 2800 -

SI Basic Functions - Monitoring functions and faults/alarms - 2802 -

SI Basic Functions - SI status CU, MM, CU + MM, group STO - 2804 -

###### PROFIsafe function diagrams (FD)

SI Basic Functions - S_STW1/2 safety control word 1/2, S_ZSW1/2 safety status word 1/2 - 2806 -

SI Extended Functions - S_STW1 safety control word 1, S_ZSW1 safety status word 1 - 2842 -

SI Extended Functions - S_STW2 safety control word 2, S_ZSW2 safety status word 2 - 2843 -

###### STO, SS1, SBC function diagrams (FD)

SI Basic Functions - STO (Safe Torque Off), SS1 (Safe Stop 1) - 2810 -

SI Basic Functions - STO (Safe Torque Off), safe pulse suppression - 2811 -

SI Basic Functions - SBC (Safe Brake Control), SBA (Safe Brake Adapter) - 2814 -

###### Additional parameters

---

#### Extended Functions

This section contains information on the following topics:

- [STO/SBC (Extended Functions)](#stosbc-extended-functions)
- [SS1 (Extended Functions)](#ss1-extended-functions)
- [SS2 (Extended Functions)](#ss2-extended-functions)
- [SAM/SBR (Extended Functions)](#samsbr-extended-functions)
- [SOS (Extended Functions)](#sos-extended-functions)
- [SBT (diagnostic function)](#sbt-diagnostic-function)
- [Communication via SIC/SCC](#communication-via-sicscc)
- [SLS (Extended Functions)](#sls-extended-functions)
- [SSM (Extended Functions)](#ssm-extended-functions)
- [SDI (Extended Functions)](#sdi-extended-functions)
- [SLA (Extended Functions)](#sla-extended-functions)
- [Actual value measurement/mechanical system (Extended Functions)](#actual-value-measurementmechanical-system-extended-functions)

##### STO/SBC (Extended Functions)

###### Description

Here you can parameterize the Safe Torque Off (STO) and Safe Brake Control (SBC) functions via onboard terminals and PROFIsafe.

The STO function is used to safely disconnect the torque-generating energy supply to the motor for a machine function or in the event of a fault. A restart is prevented by the two-channel pulse suppression. The switching on inhibited prevents an automatic restart after deselection of STO.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858142475_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Torque Off (STO, Basic and Extended Functions)](#description-of-safe-torque-off-sto-basic-and-extended-functions-1) |
| ![Description](images/147858150411_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Brake Control (SBC, Extended Functions)](#description-of-safe-brake-control-sbc-extended-functions) |

The function is enabled simultaneously with the selection.

**Cable break**

A cable break or short-circuit in the brake winding is only detected at a change of state, i.e. when opening and/or closing the brake.

For devices in Chassis format with Safe Brake Adapter, the connection cable between the Safe Brake Adapter and the motor brake is not monitored for cable break or short-circuit.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unwanted motor movements due to a defective brake**  The "SBC" function does not detect mechanical defects of the brake.   A cable break or short-circuit can cause unwanted movements of the motor, which can lead to bodily injury or death.  - In particular, ensure the brake is not powered from an external source. Information on this can be found in EN 61800‑5‑2, Appendix D. - During commissioning, test the brake with the "Safe Brake Test (SBT)" diagnostic function.  Further information can be found at "Safe Brake Test". |  |

###### Configuring Safety Integrated Functions

The Safety Integrated Extended Functions are only partly configured in the "STO/SBC" screen form. Most of the configuration is performed in other screen forms. Below you will find a procedure if you want to configure all two Safety Integrated Functions.

1. Call the "STO/SBC" Safety Function.

   The screen form of the same name opens.
2. Click the ![Configuring Safety Integrated Functions](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select STO) to configure control of the "STO" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
3. Call the "STO/SBC" function again.
4. Then connect the signal source [r9773](SINAMICS%20Parameter%20SERVO.md#r9773031-cobo-si-status-control-unit-motor-module).1 for the "STO active in drive" signal.
5. Click the ![Configuring Safety Integrated Functions](images/147858158475_DV_resource.Stream@PNG-en-US.png) button (brake control) to configure the "SBC" function.

   The "Brake control" screen form opens.

   Configure the brake control here (see "[Brake control](#brake-control)").
6. Click "Save project" in the toolbar to save the changes in the project.

**Result**

You have configured the Safety Integrated Function "STO/SBC".

###### Function diagrams (FD)

SI Extended Functions - SS1, SS2, SOS, internal STOP B, C, D, F - 2819 -

###### Additional parameters

- [p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)
- [r9720](SINAMICS%20Parameter%20SERVO.md#r9720029-cobo-si-motion-control-signals-integrated-in-the-drive-1)
- [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4)
- [r9772](SINAMICS%20Parameter%20SERVO.md#r9772023-cobo-si-status-control-unit)
- r9773
- [r9774](SINAMICS%20Parameter%20SERVO.md#r9774031-cobo-si-status-group-sto)

---

##### SS1 (Extended Functions)

###### Description

In the "Safe Stop 1" (SS1) screen form you make settings for the motor deceleration. The "SS1" function brakes the motor, monitors the magnitude of the motor deceleration within specified limits, and triggers the STO function after a delay time or violation of a speed threshold.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858210827_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Stop 1 (SS1, Extended Functions)](#description-of-safe-stop-1-ss1-extended-functions) |

###### Comparison of settings for motor deceleration

| Settings | Method of operation |
| --- | --- |
| SS1 with SAM and OFF3 (with/without encoder) | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected ([p9556](SINAMICS%20Parameter%20SERVO.md#p9556-si-motion-stop-a-delay-time-control-unit-1)). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. - Parameters [r9773](SINAMICS%20Parameter%20SERVO.md#r9773031-cobo-si-status-control-unit-motor-module).4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |
| SS1 with SAM and OFF3 (with/without encoder) and STO of the Basic Functions via onboard terminals | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected (p9556). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. - The drive brakes along the OFF3 ramp ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) once the delay time [p9652](SINAMICS%20Parameter%20SERVO.md#p9652-si-safe-stop-1-delay-time) has expired. |
| SS1 with SAM and OFF3 (with/without encoder) and SS1 of the Basic Functions via onboard terminals | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected (p9556). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. - The drive brakes along the OFF3 ramp (p1135) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) once the delay time p9652 has expired. |
| SS1 with SBR and OFF3 (with encoder) | - Braking is monitored with the "Safe Brake Ramp" function. - The drive brakes along the OFF3 ramp (p1135) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) once the delay time has expired (p9556) or when the shutdown velocity is undershot ([p9560](SINAMICS%20Parameter%20SERVO.md#p9560-si-motion-sto-shutdown-velocity-control-unit-3)). - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |
| SS1 with SBR and OFF3 (without encoder) | - In this case, there is no SS1 delay time active. The transition from SS1 to STO depends entirely on the speed falling below the shutdown velocity (p9560). - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |
| SS1 with external stop (with/without encoder) | - With external stop, "Safe Stop 1" functions in principle in just the same way as for "Safe Stop 1 with encoder (time and acceleration-controlled)" and "Safe Stop 1 without encoder (speed-controlled)." However, note the following differences:   - When SS1 with external stop is selected, the drive is not braked along the OFF3 ramp: You are responsible for applying suitable measures to brake the drive. After the delay time has expired (p9556), only STO/SBC are triggered automatically. After the function has been selected, the delay time expires – even if the function is deselected during this time. In this case, after the delay time has expired, the STO/SBC function is selected and then deselected again immediately.   - The brake ramp (SBR) and the acceleration (SAM) are not monitored and there is no standstill detection.   - With this configuration, STO becomes active after the SS1 timer p9556 has expired; this also applies when SBR has been configured. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |

###### Configuring motor deceleration with internal brake response (OFF3)

1. Select the "[0] SS1 with OFF3" setting in the "Brake response" drop-down list.

   The screen form is structured accordingly.
2. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SS1) to configure control of the "SS1" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
3. Call the "SS1" function again.
4. Select the monitoring type in the "Monitoring" drop-down list:

   - with SAM
   - with SBR
5. Click "Monitoring" and parameterize the alternative brake monitoring functions "SAM" and "SBR" in the dialog (see "[SAM/SBR (Extended Functions)](#samsbr-extended-functions)").
6. Enter the required delay time in the "Delay time SS1 -&gt; STO active" (p9556) input field.
7. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select STO via onboard terminals) to configure control of the "STO" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
8. Call the "SS1" function again.
9. Enter the required delay time in the "Safe Stop 1 delay time" (p9652) input field.
10. Connect the signal source "STO active in drive" (r9773.1).
11. If you want to receive an alarm acknowledgment via STO, activate the option of the same name.
12. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/147858158475_DV_resource.Stream@PNG-en-US.png) button (brake control) to configure the brake control.

    The "Brake control" screen form opens.

    Configure the brake control here (see "[Brake control](#brake-control)").
13. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring the motor deceleration with external stop

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned axis movements during Safe Stop 1**  During the delay time (p9652), random axis movements are possible for "Safe Stop 1 (time-controlled) with external stop" which could result in severe injuries or death in extreme cases.  - Take suitable measures to prevent undesirable axis movements, e.g. by using a brake with safe monitoring.    You will find further information in the section "Safe Brake Control." |  |

1. Select the "[1] SS1E external stop" setting in the "Brake response" drop-down list.

   The screen form is structured accordingly.
2. Click the ![Configuring the motor deceleration with external stop](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SS1) to configure control of the "SS1E" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
3. The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   Call the "SS1E" function again.
4. Enter the required delay time in the "Delay time SS1 -&gt; STO active" (p9556) input field.
5. Click the ![Configuring the motor deceleration with external stop](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select STO via onboard terminals) to configure control of the "STO" function.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
6. Call the "SS1" function again.
7. Enter the required delay time in the "Safe Stop 1 delay time" (p9652) input field.
8. Connect the signal sink "STO active in drive" (r9773.1).
9. If you want to receive an alarm acknowledgment via STO, activate the option of the same name.
10. Click the ![Configuring the motor deceleration with external stop](images/147858158475_DV_resource.Stream@PNG-en-US.png) button (brake control) to configure the brake control.

    The "Brake control" screen form opens.

    Configure the brake control here (see "[Brake control](#brake-control)").
11. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SS1, SS2, SOS, internal STOP B, C, D, F - 2819 -

###### Additional parameters

- p1135[0...n]
- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3)
- [p9506](SINAMICS%20Parameter%20SERVO.md#p9506-si-motion-function-specification-control-unit)
- p9560
- [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).0...31
- [p9507](SINAMICS%20Parameter%20SERVO.md#p9507-si-motion-function-specification-control-unit)

---

##### SS2 (Extended Functions)

###### Description

The "Safe Stop 2" ("SS2") safety function is used to brake the motor safely along the OFF3 deceleration ramp ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)) with subsequent transition to the "SOS" state (see "[Safe Operating Stop (SOS)](#sos-extended-functions)") after the delay time expires ([p9552](SINAMICS%20Parameter%20SERVO.md#p9552-si-motion-transition-time-stop-c-to-sos-sbh-control-unit-1)). The delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. The standstill tolerance ([p9530](SINAMICS%20Parameter%20SERVO.md#p9530-si-motion-standstill-tolerance-control-unit-4)) must not be violated after this time. After braking, the drives remain in speed control mode with the speed setpoint n = 0. The full torque is available. The default setpoint (e.g. from the setpoint channel, or from a higher-level controller) remains inhibited as long as "SS2" is selected.

> **Note**
>
> **Interruption of the ramp function with OFF3**
>
> Activating SS2 can mean that the higher-level controller (PLC, motion controller) which specifies the speed setpoint, interrupts the ramp function (e.g. with OFF2). The device behaves in this way as a result of a fault response triggered by OFF3 activation. This fault response must be avoided by appropriate parameterization or configuration.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858238731_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Stop 2 (SS2, Extended Functions)](#description-of-safe-stop-2-ss2-extended-functions) |

###### Differences between "Safe Stop 2 with OFF3" and "SS2 with external stop (SS2E)"

The following differences exist:

- If SS2 with external stop is selected, the drive does not brake the motor autonomously but follows the defined speed setpoint.
- During the delay time [p9553](SINAMICS%20Parameter%20SERVO.md#p9553-si-motion-transition-time-stop-d-to-sos-sbh-control-unit-1), the brake ramp (SBR) and the acceleration (SAM) are not monitored and there is no standstill detection.
- SOS becomes active after the delay time p9553 has expired.

  If the SS2E function is active, the higher-level controller must define the speed setpoint in such a way that the motor is stopped no later than after the delay time p9553 has expired.
- To enable "Safe Stop 2 with external stop", set the "SS2E enable" switch to "Connection".

  > **Note**
  >
  > **SS2E in S120 with CU310-2 PN**
  >
  > The "SS2E enable" setting is not available in SINAMICS S120 drives with CU310-2 PN and Safety Integrated Extended Functions with control via onboard terminals.
- The PROFIsafe control word S_STW2.28 selects the SS2E function. PROFIsafe S_STW2.28 is contained in telegrams 31, 901, 902 and 903.
- The PROFIsafe status word S_ZSW2.28 indicates whether the SS2E function is active. The PROFIsafe status word S_ZSW2.28 is contained in telegrams 31, 901, 902 and 903. The associated diagnostics parameter is [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).28.

  In the "Safety Info Channel," status word S_ZSW3B.11 indicates whether the SS2E function is active. The associated diagnostic parameter is [r10234](SINAMICS%20Parameter%20SERVO.md#r10234015-cobo-si-safety-information-channel-status-word-s_zsw3b-1).11.

  However, the diagnostic parameters [p9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).28 and [p10234](SINAMICS%20Parameter%20SERVO.md#r10234015-cobo-si-safety-information-channel-status-word-s_zsw3b-1).11 are also set during an internal STOP D.

###### Configuring motor deceleration with internal brake response (OFF3)

1. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SS2) to configure control of the "SS2" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SS2" function again.
3. Select the monitoring type in the "Monitoring" drop-down list:

   - with SAM
   - with SBR
4. Click "Monitoring" and parameterize the alternative brake monitoring functions "SAM" and "SBR" in the dialog (see "[SAM/SBR (Extended Functions)](#samsbr-extended-functions)").
5. In the "Delay time SS2 -&gt; SOS active" (p9552) input field select the required delay time.
6. Enter a value for the standstill tolerance in the "Standstill monitoring" (p9530) field.
7. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/147858158475_DV_resource.Stream@PNG-en-US.png) button (brake control) to configure the brake control.

   The "Brake control" screen form opens.

   Configure the brake control here (see "[Brake control](#brake-control)").
8. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring the motor deceleration with external stop

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned axis movements during Safe Stop 2**  During the delay time ([p9652](SINAMICS%20Parameter%20SERVO.md#p9652-si-safe-stop-1-delay-time)), random axis movements are possible for "SS2E" (Safe Stop 2 with external stop) or SS2ESR (Safe Stop 2 with extended stop and retract) which could result in severe injuries or death in extreme cases.  - Take suitable measures to prevent undesirable axis movements, e.g. by using a brake with safe monitoring.    You will find further information in the section "Safe Brake Control." |  |

1. Click the ![Configuring the motor deceleration with external stop](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SS2E) to configure control of the "SS2E" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SS2" function again.
3. Set the "SS2E enable" switch to "Connection".

   > **Note**
   >
   > The "SS2E enable" setting is not available in S120 drives with CU310-2 and Safety Integrated Extended Functions with control via onboard terminals.
4. In the "Delay time SS2E/stop D -&gt; SOS active" (p9553) input field, select the required delay time.

   SBR/SAM is not monitored during this delay time. SOS becomes active after this delay time has elapsed.
5. In the "Delay time Stop E -&gt; SOS active" ([p9554](SINAMICS%20Parameter%20SERVO.md#p9554-si-motion-transition-time-stop-e-to-sos-sbh-control-unit-1)) input field select the required delay time.

   SBR/SAM is not monitored during this delay time. SOS becomes active after this delay time has elapsed.
6. Enter a value for the standstill tolerance in the "Standstill monitoring" (p9530) field.
7. Click the ![Configuring the motor deceleration with external stop](images/147858158475_DV_resource.Stream@PNG-en-US.png) button (brake control) to configure the brake control.

   The "Brake control" screen form opens.

   Configure the brake control here (see "[Brake control](#brake-control)").
8. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SS1, SS2, SOS, internal STOP B, C, D, F - 2819 -

###### Additional parameters

- p1135[0...n]
- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3)
- p9530
- [p9548](SINAMICS%20Parameter%20SERVO.md#p9548-si-motion-sam-actual-speed-tolerance-control-unit-4)
- p9552
- r9722.0...31

---

##### SAM/SBR (Extended Functions)

###### Description

In the following dialogs you parameterize the alternative brake monitoring functions "Safe Acceleration Monitor" ("SAM") and "Safe Brake Ramp" ("SBR"):

###### Safe Acceleration Monitor (SAM)

The "SAM" function is used to safely monitor braking along the OFF3 ramp. The function is active for SS1, SS2 or STOP B and STOP C.

As long as the speed decreases, the converter continuously adds the adjustable tolerance [p9548](SINAMICS%20Parameter%20SERVO.md#p9548-si-motion-sam-actual-speed-tolerance-control-unit-4) to the current speed and thus tracks the monitoring of the speed. If the speed is temporarily higher, the monitoring remains at the last value. The converter reduces the monitoring threshold until the "Shutdown speed" has been reached.

SAM recognizes if the drive accelerates beyond the tolerance defined in p9548 during the ramp-down phase, and triggers a STOP A. The monitoring is performed as follows:

- The monitoring through SAM is activated for SS1 (or STOP B) and SS2 (or STOP C).
- The SAM limit value is frozen when the velocity falls below the velocity limit in [p9568](SINAMICS%20Parameter%20SERVO.md#p9568-si-motion-samsbr-velocity-limit-control-unit-1).
- The SAM monitoring continues until the transition time to SOS/STO expires.

Calculating the SAM tolerance of the actual velocity:

- The following applies when parameterizing the SAM tolerance:

  - The possible velocity increase after SS1 or SS2 is triggered results from the effective acceleration a and the duration of the acceleration phase.
  - The duration of the acceleration phase is equivalent to one monitoring cycle (MC; [p9500](SINAMICS%20Parameter%20SERVO.md#p9500-si-motion-monitoring-clock-cycle-control-unit-1)) (delay from detecting an SS1/SS2 until n<sub>set</sub> = 0)
- Calculating the SAM tolerance:

  Actual velocity for SAM = acceleration x acceleration duration   
  This results in the following setting rule:

  - For a linear axis: SAM tolerance [mm/min] = a [m/s<sup>2</sup>] · MC [s] · 1000 [mm/m] 60 [s/min]
  - For a rotary axis: SAM tolerance [rpm] = a [rev/s<sup>2</sup>] · MC [s] · 60 [s/min]
- Recommendation   
  The SAM tolerance value entered should be approx. 20% higher than the calculated value.
- You set the tolerance so that the "undershoot" which inevitably occurs when standstill is reached after braking along the OFF3 ramp is tolerated. However, the size of this cannot be calculated.

**Configuring SAM**

1. Enter the required values in the "SAM (Safe Acceleration Monitor)" dialog in the following input fields:

   - Velocity tolerance (p9548)
   - SAM velocity limit (p9568)
   - STO shutdown velocity ([p9560](SINAMICS%20Parameter%20SERVO.md#p9560-si-motion-sto-shutdown-velocity-control-unit-3))
   - Ramp-down time (OFF3) ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)[0])
   - Maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)[0])
2. Once all necessary settings have been made, click "Close".

   The dialog closes.
3. Click "Save project" in the toolbar to save the changes in the project.

###### Safe Brake Ramp (SBR)

The "SBR" function safely monitors the brake ramp. The Safe Brake Ramp function is used to monitor braking with the functions "SS1 with/without encoder," "SLS without encoder," SS2 as well as for STOP B / STOP C (for Safety with encoder). For SLS, the setpoint limitation of the Safety Integrated Functions ([r9733](SINAMICS%20Parameter%20SERVO.md#r973302-co-si-motion-setpoint-speed-limit-effective-1)) must be connected to the ramp-function generator ([p1051](SINAMICS%20Parameter%20SERVO.md#p10510n-ci-velocity-limit-rfg-positive-direction-1)/[p1052](SINAMICS%20Parameter%20SERVO.md#p10520n-ci-velocity-limit-rfg-negative-direction-1)).

The motor is braked immediately with the OFF3 ramp when SS1, SS2 or SLS is triggered. Monitoring of the brake ramp is activated once the delay time [p9582](SINAMICS%20Parameter%20SERVO.md#p9582-si-motion-brake-ramp-delay-time-control-unit) has expired. Monitoring ensures that the motor does not exceed the set brake ramp (SBR) when braking.

[p9581](SINAMICS%20Parameter%20SERVO.md#p9581-si-motion-brake-ramp-reference-value-control-unit-1) (SI Motion brake ramp reference value) and [p9583](SINAMICS%20Parameter%20SERVO.md#p9583-si-motion-brake-ramp-monitoring-time-control-unit) (SI Motion brake ramp monitoring time) are used to set the gradient of the brake ramp. Parameter p9581 defines the reference velocity and parameter p9583 defines the ramp-down time. Parameter p9582 sets the time between the triggering of SS1, selection of SLS or SLS level changeover and the start of brake ramp monitoring.

> **Note**
>
> **Limitation of the SBR delay time**
>
> The SBR delay time (p9582) is limited to a minimum value of two SI Motion monitoring cycles (2 · p9500), i.e. even if a value less than 2 · p9500 is parameterized for the delay time (p9582), SBR only takes effect two cycles after an active SS1.
>
> If a value greater than 2 x p9500 is parameterized for the delay time (p9582), SBR takes effect after active SS1 after the time p9582. Ensure that you round off the SBR delay time to an integer multiple of the safety cycle (p9500).

**Configuring SBR**

1. Enter the required values in the "SBR (Safe Brake Ramp)" dialog in the following input fields:

   - Reference velocity (p9581)
   - SAM velocity limit (p9568)
   - STO shutdown velocity (p9560)
   - Delay time (p9582)
   - Brake ramp monitoring time (p9583)
   - Ramp-down time (OFF3) (p1135[0])
   - Maximum speed (p1082[0])
2. Once all necessary settings have been made, click "Close".

   The dialog closes.
3. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SAM (Safe Acceleration Monitor), SBR (Safe Brake Ramp) - 2825 -

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20SERVO.md#p9516-si-motion-encoder-configuration-safety-functions-control-unit-1)
- [p9546](SINAMICS%20Parameter%20SERVO.md#p9546-si-motion-ssm-sga-n-nx-speed-limit-cu-4)
- p9548
- p9560
- p9568
- p9581
- p9582
- p9583

---

##### SOS (Extended Functions)

###### Description

The "Safe Operating Stop" (SOS) function is used for safe monitoring of the standstill position of a drive. The drive interprets positions within a standstill tolerance as "standstill".

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858280971_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Operating Stop (SOS, Extended Functions)](#description-of-safe-operating-stop-sos-extended-functions) |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movement of the drive through mechanical forces**  Mechanical forces greater than the maximum drive torque may force a drive currently operated in position control out of the "Safe Operating Stop" (SOS) position. This unwanted drive movement can lead to serious injury or even death in extreme cases. It then triggers a stop function category 1 according to EN 60204‑1 (fault response function STOP B).  - Note the alarms for SS1 and STO.   Take suitable measures to prevent unwanted movements, e.g. by using a brake with safe monitoring. |  |

**Effectiveness of the SOS function**

The "SOS" function takes effect in the following cases:

- After SOS is selected and the delay time in [p9551](SINAMICS%20Parameter%20SERVO.md#p9551-si-motion-slssg-changeoversos-sbh-delay-time-cu-1) has expired

  The drive must be braked to standstill within this delay time, e.g. by the controller.
- As a consequence of SS2
- As a consequence of STOP C (corresponds to selection of SS2)
- As a consequence of STOP D (corresponds to selection of SOS)
- As a consequence of STOP E (corresponds to selection of SOS with additional activation of the standard "Extended stop and retract (ESR)" function)

**SOS standstill monitoring**

If the standstill tolerance is violated in [p9530](SINAMICS%20Parameter%20SERVO.md#p9530-si-motion-standstill-tolerance-control-unit-4), the drive reacts with:

- STOP B with subsequent STOP A
- Safety message C01707

###### Configuring monitoring

1. Click the ![Configuring monitoring](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SOS) to configure control of the "SOS" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SOS" function again.
3. Correct the default value in the "Delay time SOS -&gt; SOS active" field (p9551).
4. Correct the default value in the "Standstill tolerance" (p9530) field.

   Alternatively, you can also click on the "Standstill tolerance SOS" button. A dialog with a graphic display of the standstill monitoring opens. You can also enter the standstill tolerance here.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SS1, SS2, SOS, internal STOP B, C, D, F - 2819 -

###### Additional parameters

- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3)
- [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).0...31
- [r9731](SINAMICS%20Parameter%20SERVO.md#r9731-si-motion-safe-position-accuracy-1)

---

##### SBT (diagnostic function)

###### Description

The diagnostic function "Safe Brake Test" function (SBT) checks the holding torque of a brake (operating or holding brake). The drive purposely generates a configurable torque against the applied brake. If the brake is operating correctly, the axis movement remains within a parameterized tolerance. However, if a larger axis movement is identified from the encoder actual values, the brake is not in a position to provide the specified holding torque. The brake must now be serviced or replaced.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858305675_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Brake Test (SBT, diagnostic function)](#description-of-safe-brake-test-sbt-diagnostic-function) |

###### Requirements

The following requirements must be satisfied when using the "Safe Brake Test" diagnostic function:

- The Safety Integrated Extended Functions must be enabled; also available for the Safety Integrated Extended Functions without selection.
- Safe Brake Control must be enabled when testing a brake controlled by SINAMICS (motor holding brake).
- The "Safe Brake Test" (SBT) diagnostic function can only be used with an encoder.
- Safety Integrated Extended Functions "with encoder" have been enabled

  You will find information on possible encoder concepts in the "Safety Integrated" Function Manual, Section "Notes on safe actual value acquisition with encoder system".
- Speed control with encoder ([p1300](SINAMICS%20Parameter%20SERVO.md#p13000n-open-loopclosed-loop-control-operating-mode-1) = 21).

  SBT is not possible with encoderless speed control (e.g. vector V/f control) and torque control. In this case, alarm A01784 is output.

###### Functional characteristics

The "SBT" diagnostic function has the following properties:

- The parameters of the SBT diagnostic function are protected by the Safety Integrated password and can only be changed in the Safety Integrated commissioning mode.
- Using this diagnostic function, brakes can be tested that are directly connected to the SINAMICS S120 (integrated brake control), but also externally controlled brakes (e.g. via a PLC).
- A maximum of 2 brakes can be tested:

  - A motor holding brake, controlled by the integrated brake control of the SINAMICS, and in addition, an externally controlled brake.
  - Two externally controlled brakes
  - A motor holding brake, controlled by the integrated brake control of the SINAMICS.
  - One externally controlled brake
- The following options are available to control the SBT diagnostic function:

  - BICO interconnection; digital signals (e.g. DIs) are used to operate the SBT diagnostic function her.
  - Safety Control Channel (SCC) or PROFINET

    Using SCC, the SBT diagnostic function can be controlled directly from a higher-level controller. You can find additional information about SCC and SIC data in "[Communication via SIC/SCC](#communication-via-sicscc)".
  - The brake test can be automatically executed when the forced checking procedure (test stop) is selected. No additional signals are required for the control. However, the test possibilities are restricted.
- The Safe Brake Test (SBT) diagnostic function meets the requirements for Category 2 according to EN ISO 13849‑1.

###### Configuring the brake test via SCC

1. Select the "SBT via SCC" setting in the "Select SBT" drop-down list.

   The interconnection of the parameters for the telegram extension relevant for SCC/SIC can be performed automatically by setting [p60122](SINAMICS%20Parameter%20SERVO.md#p60122-if1-profidrive-sicscc-telegram-selection) = 701. However, the telegram extension must have been previously created. For more detailed information, see "[Communication via SIC/SCC](#communication-via-sicscc)"
2. Select the test settings in the "Brake 1" and "Brake 2" drop-down lists.

   See "Function features/Test configurations".
3. Record the following information in the input fields for Brake 1:

   - Test duration ([p10211](SINAMICS%20Parameter%20SERVO.md#p1021101-si-motion-sbt-test-duration-sequence-1-4)[0])
   - Holding torque ([p10209](SINAMICS%20Parameter%20SERVO.md#p1020901-si-motion-sbt-brake-holding-torque-3)[0])
   - Position tolerance ([p10212](SINAMICS%20Parameter%20SERVO.md#p1021201-si-motion-sbt-position-tolerance-sequence-1-4)[0])
   - Ramp time (p10209[0])
   - Factor ([p10210](SINAMICS%20Parameter%20SERVO.md#p1021001-si-motion-sbt-test-torque-factor-sequence-1-3)[0])
4. If you have set a 2nd brake, record the following information in the input fields for Brake 2:

   - Test duration (p10211[1])
   - Holding torque (p10209[1])
   - Position tolerance (p10212[1])
   - Ramp time (p10209[1])
   - Factor (p10210[1])
5. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring the brake test via BICO interconnection

1. Select the "SBT via BICO" setting in the "Select SBT" drop-down list.
2. Select the test settings in the "Brake 1" and "Brake 2" drop-down lists.

   See "Function features/Test configurations".
3. Record the following information in the input fields for Brake 1:

   - Test duration (p10211[0])
   - Holding torque (p10209[0])
   - Position tolerance (p10212[0])
   - Ramp time (p10209[0])
   - Factor (p10210[0])
4. If you have set a 2nd brake, record the following information in the input fields for Brake 2:

   - Test duration (p10211[1])
   - Holding torque (p10209[1])
   - Position tolerance (p10212[1])
   - Ramp time (p10209[1])
   - Factor (p10210[1])
5. Interconnect the following signal sources for the control word of the Safe Brake Test via BICO for the brake test:

   - Select brake test ([p10230](SINAMICS%20Parameter%20SERVO.md#p1023005-bi-si-motion-sbt-control-word-4)[0])
   - Start brake test (p10230[1])
   - Select brake (p10230[2])
   - Select test torque sign (p10230[3])
   - Select test sequence (p10230[4])
   - Status of external brake (p10230[5])
6. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring the brake test via test stop selection

1. Select the "Test stop selection" setting in the "Select SBT" drop-down list.
2. Select the direction of the test torque for the SBT in the "Test direction" drop-down list.
3. Select the "Test motor holding brake" setting in the "Brake 1" drop-down list.
4. Select the "Disable" setting in the "Brake 2" drop-down list.
5. Record the following information in the input fields for Brake 1:

   - Test duration (p10211[0])
   - Holding torque (p10209[0])
   - Position tolerance (p10212[0])
   - Ramp time (p10209[0])
   - Factor (p10210[0])
6. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SBT (Safe Brake Test) - 2836 -

SI Extended Functions - Selection of the active control word - 2837 -

###### Additional parameters

- [p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration)
- [p1216](SINAMICS%20Parameter%20SERVO.md#p1216-motor-holding-brake-opening-time)
- [p1217](SINAMICS%20Parameter%20SERVO.md#p1217-motor-holding-brake-closing-time)
- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3)
- [p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)
- [p9602](SINAMICS%20Parameter%20SERVO.md#p9602-si-enable-safe-brake-control-control-unit)
- [p10201](SINAMICS%20Parameter%20SERVO.md#p10201-si-motion-sbt-enable-1)
- [p10202](SINAMICS%20Parameter%20SERVO.md#p1020201-si-motion-sbt-brake-selection-1)[0...1]
- [p10203](SINAMICS%20Parameter%20SERVO.md#p10203-si-motion-sbt-control-selection-1)
- [p10204](SINAMICS%20Parameter%20SERVO.md#p10204-si-motion-sbt-motor-type-1)
- [p10208](SINAMICS%20Parameter%20SERVO.md#p1020801-si-motion-sbt-test-torque-ramp-time-3)[0...1]
- [p10218](SINAMICS%20Parameter%20SERVO.md#p10218-si-motion-sbt-test-torque-sign-3)
- [p10220](SINAMICS%20Parameter%20SERVO.md#p1022001-si-motion-sbt-test-torque-factor-sequence-2-3)[0...1]
- [p10221](SINAMICS%20Parameter%20SERVO.md#p1022101-si-motion-sbt-test-duration-sequence-2-4)[0...1]
- [p10222](SINAMICS%20Parameter%20SERVO.md#p1022201-si-motion-sbt-position-tolerance-sequence-2-4)[0...1]
- p10230[0...5]
- [r10231](SINAMICS%20Parameter%20SERVO.md#r10231-si-motion-sbt-control-word-diagnostics-1)
- [r10234](SINAMICS%20Parameter%20SERVO.md#r10234015-cobo-si-safety-information-channel-status-word-s_zsw3b-1).0...15
- [p10235](SINAMICS%20Parameter%20SERVO.md#p10235-ci-si-safety-control-channel-control-word-s_stw3b-1)
- [r10240](SINAMICS%20Parameter%20SERVO.md#r10240-si-motion-sbt-test-torque-diagnostics-1)
- [r10241](SINAMICS%20Parameter%20SERVO.md#r10241-si-motion-sbt-load-torque-diagnostics-1)
- p60122

---

---

**See also**

[Application example](https://support.industry.siemens.com/cs/ww/en/view/69870640)

##### Communication via SIC/SCC

Below you can see the tests of two different types of brakes:

###### Test of a motor holding brake

The following figure shows the communication via SIC and SCC during the test of a motor holding brake:

![Test of a motor holding brake](images/147858346507_DV_resource.Stream@PNG-en-US.png)

###### Test of an external brake

The following figure shows the communication via SIC and SCC during the test of an external brake:

![Test of an external brake](images/147858341515_DV_resource.Stream@PNG-en-US.png)

###### Function diagrams (FD)

SI Extended Functions - SBT (Safe Brake Test) - 2836 -

SI Extended Functions - Selection of the active control word - 2837 -

##### SLS (Extended Functions)

###### Description

The Safely-Limited Speed (SLS) function protects a drive against unintentionally high speeds in both directions of rotation. This is achieved by monitoring the current drive speed up to a velocity limit.

SLS prevents a parameterized velocity limit from being exceeded. Limits must be specified based on results of the risk analysis. Up to four different SLS speed limits can be parameterized using parameter [p9531](SINAMICS%20Parameter%20SERVO.md#p953103-si-motion-sls-sg-limit-values-control-unit-4)[0..3]; it is possible to switch between them even if the SLS is activated.

An override can also be added to SLS limit value 1. In operation, this override can be varied using a PROFIsafe telegram.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858377739_DV_resource.Stream@PNG-en-US.png) | [Description of Safely-Limited Speed (SLS, Extended Functions)](#description-of-safely-limited-speed-sls-extended-functions) |

###### Setting SLS via PROFIsafe with encoder and onboard terminals

**Function features:**

- When SLS is selected, the monitoring only takes effect after the configured delay time has expired ([p9551](SINAMICS%20Parameter%20SERVO.md#p9551-si-motion-slssg-changeoversos-sbh-delay-time-cu-1)). Within this time, the actual velocity must be below the (selected) limit. The delay time is not effective when SLS is deselected.
- After switching to a lower limit value (p9531), the actual velocity of the drive must have dropped below the new limit within the delay time (p9551). The existing limit remains active during the delay time. The lower limit value becomes active after the delay time has expired. This also applies to a reduction of the limit value via PROFIsafe.
- If the actual velocity of the drive is higher than the new Safely-Limited Speed limit value after the delay time has expired, a message is generated with the parameterized stop response.
- The stop response (STOP A, STOP B, STOP C, STOP D, or STOP E) is parameterized with [p9563](SINAMICS%20Parameter%20SERVO.md#p956303-si-motion-sls-sg-specific-stop-response-control-unit-1). Click on the green arrow next to the SLS level.
- On switchover to a higher limit value, the delay time is not active and the higher limit value becomes active immediately. This also applies to increasing the limit value via PROFIsafe.

**Settings**

1. Make the following settings in the function selection:

   - Select the option "with encoder" in the drop-down list.
   - Select the option "via PROFIsafe" in the "Control type" drop-down list.
   - Activate the "Basic Functions via onboard terminals" option.
2. Call the "SLS" function.
3. Click the ![Setting SLS via PROFIsafe with encoder and onboard terminals](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SLS) to configure control of the "SLS" function.

   The "Control" screen form opens. The way the screen form is displayed depends on the basic settings of the Safety Integrated Function SLS.
4. In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
5. Call the "SLS" function again.
6. Correct the prescribed delay time in the "Delay time for selection of SLS -&gt; SLS active" field (p9551).
7. Correct the default value for level 1 of the speed limit (p9531[0]).
8. Select the required stop response for level 1 in the drop-down list (p9563[0]).
9. Click the ![Setting SLS via PROFIsafe with encoder and onboard terminals](images/147858373771_DV_resource.Stream@PNG-en-US.png) icon to open the configuration for level 1.

   The "SS1" screen form opens:

   Set the desired motor deceleration here (see "[SS1 (Extended Functions)](#ss1-extended-functions)")
10. Repeat steps 7 to 9 for the respective level if you also want to configure the speed limit for levels 2, 3 and/or 4.
11. In the "Setpoint velocity limitation SLS level" ([p9533](SINAMICS%20Parameter%20SERVO.md#p9533-si-motion-sls-setpoint-speed-limiting-control-unit)) field, enter a weighting factor for determining the setpoint limit from the selected actual velocity limit as a percentage.
12. If you want to use a PROFIsafe override for level 1 of the speed limit, select the "Enabled" option in the "PROFIsafe override" ([p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3).24) drop-down list.
13. Click "Save project" in the toolbar to save the changes in the project.

**Result**

The velocity limit value of the drive is configured. The current SLS limit value is displayed in the field of the same name ([r9714](SINAMICS%20Parameter%20SERVO.md#r971403-co-si-motion-diagnostics-velocity-1)[2]). The effective setpoint limit is displayed in the field of the same name ([r9733](SINAMICS%20Parameter%20SERVO.md#r973302-co-si-motion-setpoint-speed-limit-effective-1)). It is used, for instance, for transferring values to a higher-level controller, which can then, for example, adjust traversing velocities to the SLS levels or to the setpoint channel ([p1051](SINAMICS%20Parameter%20SERVO.md#p10510n-ci-velocity-limit-rfg-positive-direction-1)). The effective setpoint limit is part of the Safety Info Channel (SIC).

###### Setting SLS without selection

As an alternative to control via onboard terminals and/or PROFIsafe, there is also the option of parameterizing the "SLS without selection" function:

**Settings:**

1. Select the control type "without selection" in the function selection and then call the "SLS" screen form.
2. Click the ![Setting SLS without selection](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SLS) to configure control of the "SLS" function.

   The "Control" screen form opens. The way the screen form is displayed depends on the basic settings of the Safety Integrated Function "SLS".
3. In the "Without selection – Configuration" area, select the settings for the "SLS static", "SDI positive static" and "SDI negative static" options via the corresponding drop-down lists.
4. Call the "SLS" function again.
5. Correct the default value for level 1 of the speed limit (p9531[0]).
6. Select the required stop response for level 1 in the drop-down list (p9563[0]).
7. In the "Setpoint velocity limitation SLS level" (p9533) field, enter a weighting factor for determining the setpoint limit from the selected actual velocity limit as a percentage.
8. Click the ![Setting SLS without selection](images/147858373771_DV_resource.Stream@PNG-en-US.png) icon to configure the motor deceleration.

   The "SS1" screen form is displayed.

   Set the desired motor deceleration here (see "[SS1 (Extended Functions)](#ss1-extended-functions)")
9. Click "Save project" in the toolbar to save the changes in the project.

**Result**

The velocity limit value of the drive is configured. The current SLS limit value is displayed in the field of the same name (r9714[2]). The effective setpoint limit is displayed in the field of the same name (r9733). It is used, for instance, for transferring values to a higher-level controller, which can then, for example, adjust traversing velocities to the SLS levels or to the setpoint channel (p1051). The effective setpoint limit is part of the Safety Info Channel (SIC).

###### Setting SLS without encoder

**Function features:**

- If the velocity setpoint limitation (r9733) was connected to the setpoint channel (p1051/[p1052](SINAMICS%20Parameter%20SERVO.md#p10520n-ci-velocity-limit-rfg-negative-direction-1)) and then SLS was selected – or if you switchover to a lower SLS level – the motor is decelerated from the actual speed to below the value defined with r9733 along the OFF3 ramp. In this case, the drive may no longer follow the setpoint of the higher-level motion controller.
- Parameter [p9582](SINAMICS%20Parameter%20SERVO.md#p9582-si-motion-brake-ramp-delay-time-control-unit) is used to set the delay time for the brake ramp monitoring.
- Monitoring of the brake ramp is activated once the delay time p9582 has expired. If the actual velocity of the drive violates the brake ramp (SBR) during braking, Safety message C01706 is output and the drive is stopped with STOP A.
- The newly selected SLS limit value becomes the new velocity limit in the following cases:

  - When the SBR ramp has reached the new SLS limit value.
  - When the actual velocity of the drive was below the new SLS limit value for at least the time set in p9582.
- The "Safely-Limited Speed without encoder" function then monitors whether the actual velocity remains below the newly selected SLS limit value.
- The parameterized stop response (p9563[x]) is triggered if the SLS limit value is exceeded.
- Only STOP A and STOP B may be configured as stop responses for "Safely-Limited Speed" (SLS) without an encoder.

**Settings**

1. Make the following settings in the function selection:

   - Select the option "without encoder" in the drop-down list.
   - Select the option "via PROFIsafe" in the "Control type" drop-down list.
   - Activate the "Basic Functions via onboard terminals" option.
2. Proceed as described under "Set SLS via PROFIsafe with encoder and onboard terminals". At the same time, note the function features "without encoder".
3. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SLS (Safely-Limited Speed) - 2820 -

###### Additional parameters

- p9501.0
- [p9512](SINAMICS%20Parameter%20SERVO.md#p9512-select-si-motion-safety-functions-without-selection-cu)
- p9531[0...3]
- p9551
- p9563[0...3]
- [p9580](SINAMICS%20Parameter%20SERVO.md#p9580-si-motion-stop-response-delay-bus-failure-control-unit-1)
- [p9581](SINAMICS%20Parameter%20SERVO.md#p9581-si-motion-brake-ramp-reference-value-control-unit-1)
- p9582
- [p9583](SINAMICS%20Parameter%20SERVO.md#p9583-si-motion-brake-ramp-monitoring-time-control-unit)
- [p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)
- [r9707](SINAMICS%20Parameter%20SERVO.md#r970702-co-si-motion-diagnostics-encoder-position-actual-value-gx_xist1-1)[0...2]
- r9714[0...2]
- [r9720](SINAMICS%20Parameter%20SERVO.md#r9720029-cobo-si-motion-control-signals-integrated-in-the-drive-1).0...27
- [r9721](SINAMICS%20Parameter%20SERVO.md#r9721015-cobo-si-motion-status-signals-control-unit).0...15
- [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).0...31

---

##### SSM (Extended Functions)

###### Description

The "Safe Speed Monitor" (SSM) function provides a reliable method for detecting when the velocity falls below the velocity limit ([p9546](SINAMICS%20Parameter%20SERVO.md#p9546-si-motion-ssm-sga-n-nx-speed-limit-cu-4)) in both directions of rotation, e.g. for standstill detection. A fail-safe output signal is available for further processing.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858386315_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Speed Monitor (SSM, Extended Functions)](#description-of-safe-speed-monitor-ssm-extended-functions) |

###### SSM with encoder

A hysteresis can be configured for the "SSM" function via [p9547](SINAMICS%20Parameter%20SERVO.md#p9547-si-motion-ssm-sga-n-nx-velocity-hysteresis-cu-4). In this way, a more stable signal characteristic of SSM can be achieved at speeds close to the monitoring threshold (p9546).

When hysteresis is configured, then the velocity (or speed) determined by the two channels may not differ by more than the difference between p9546 and p9547. Otherwise it would be theoretically possible that one channel returns a HIGH signal and the other a LOW signal for SSM.

The following figure shows the characteristic of the SSM safe output signal when hysteresis is active:

![SSM with encoder](images/147781004171_DV_resource.Stream@PNG-en-US.png)

The output signal for SSM is smoothed by setting a filter time with a PT1 filter ([p9545](SINAMICS%20Parameter%20SERVO.md#p9545-si-motion-ssm-sga-n-nx-filter-time-control-unit-1)).

> **Note**
>
> **Different behavior of the STOP F for SSM with and without hysteresis**
>
> A STOP F is indicated by Safety Integrated message C01711. STOP F only results in the follow-up response STOP B/STOP A when one of the Safety Integrated Functions is active. For the SSM Safety Integrated Function, the behavior depends on whether the hysteresis is enabled or blocked.
>
> - "SSM with hysteresis" option enabled ([p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3).16 = 1):
>
>   STOP F then only results in the follow-up response STOP B / STOP A.
> - "SSM with hysteresis" option blocked (p9501.16 = 0):
>
>   STOP F does not result in a follow-up response.

**Settings for SSM with hysteresis:**

1. Select the setting "Enable" in the "SSM" screen form in the "SSM with hysteresis" (p9501.16) drop-down list.

   The "Velocity hysteresis" input field is displayed together with the "Filter time" field.
2. Correct the specified value in mm/min in the "Velocity hysteresis" (p9547) field.
3. Correct the specified limit value in mm/min in the "Velocity limit" (p9546) field.
4. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.
5. Click "Save project" in the toolbar to save the changes in the project.

**Settings for SSM without hysteresis:**

1. Select the setting "Disable" in the "SSM" screen form in the "SSM with hysteresis" (p9501.16) drop-down list.
2. Correct the specified limit value in mm/min in the "Velocity limit" (p9546) field.
3. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.
4. Click "Save project" in the toolbar to save the changes in the project.

###### SSM without encoder

Without an encoder, the "Safe Speed Monitor" essentially functions exactly the same as "Safe Speed Monitor with encoder".

> **Note**
>
> **Setting of the OFF1 or OFF3 ramp-down time**
>
> If the OFF1 or OFF3 ramp-down time is too short or the difference between the SSM limit speed and the shutdown speed is too small, the "speed below limit value" signal may not change to 1, because no actual speed value could be determined below the SSM limit before pulse suppression occurred. In this case, the OFF1 or OFF3 ramp-down time or the difference between SSM speed limit and shutdown speed should be increased.

**Differences between Safe Speed Monitor with and without encoder**

For Safe Speed Monitor without encoder, the drive is unable to determine the current velocity after the pulse suppression. Two responses can be selected for this operating state with parameter [p9509](SINAMICS%20Parameter%20SERVO.md#p9509-si-motion-behavior-during-pulse-suppression-control-unit).0:

- p9509.0 = 1The status signal (SSM feedback signal) is "0" (factory setting).
- p9509.0 = 0 The status signal (SSM feedback signal) is frozen. "Safe Torque Off" (STO) is selected internally.

  ![SSM without encoder](images/147858381707_DV_resource.Stream@PNG-en-US.png)

  The speed remains below the limits of p9546 throughout the entire monitoring period. Therefore, the SSM feedback signal [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).15 = 1 remains. After the command for pulse suppression, the motor speed drops. The internal STO is set when the speed drops below the zero speed detection level.

  In this case, the SSM feedback signal remains HIGH; it is frozen. The drive cannot accelerate again, due to the internal STO selection.

  To restart the motor safely, STO must be manually selected and deselected again. After STO has been deselected, a 5 second time window is opened. If the pulse enable takes place within this time window, the motor starts. If the pulse enable does not take place within this 5 second time window, the internal STO becomes active again.

  If p9509.0 = 1, the SSM monitoring is terminated after the pulse suppression. The feedback signal r9722.15 drops to 0. The SSM monitoring is only reactivated after a new pulse enable. In this case, STO must not be selected and deselected to start the drive.

Due to the less precise speed detection, "Safe Speed Monitor without encoder" requires a larger hysteresis (p9547) and, where applicable, a filter time (p9545) compared with the function with encoder.

**Settings for SSM with hysteresis:**

1. Select the setting "Enable" in the "SSM" screen form in the "SSM with hysteresis" (p9501.16) drop-down list.

   The "Velocity hysteresis" input field is displayed together with the "Filter time" field.
2. In the "Feedback SSM active for pulse inhibit" (p9509.0) drop-down list, select the possible behavior during pulse suppression:

   - [0] Remains active

     Monitoring continues during pulse suppression. The last feedback signal displayed prior to pulse suppression is retained and the STO state is assumed.
   - [1] Becomes active

     Monitoring is disabled during pulse suppression and the feedback signal shows 0.
3. Correct the specified value in mm/min in the "Velocity hysteresis" (p9547) field.
4. Correct the specified limit value in mm/min in the "Velocity limit" (p9546) field.
5. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.
6. Click "Save project" in the toolbar to save the changes in the project.

**Settings for SSM without hysteresis:**

1. Select the setting "Disable" in the "SSM" screen form in the "SSM with hysteresis" (p9501.16) drop-down list.
2. In the "Feedback SSM active for pulse inhibit" (p9509.0) drop-down list, select the possible behavior during pulse suppression:

   - [0] Remains active
   - [1] Becomes active
3. Correct the specified limit value in mm/min in the "Velocity limit" (p9546) field.
4. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Function diagrams (FD)

SI Extended Functions - SSM (Safe Speed Monitor) - 2823 -

SI Extended Functions - SI Motion drive-integrated control signals / status signals - 2840 -

###### Additional parameters

- p9501
- [p9506](SINAMICS%20Parameter%20SERVO.md#p9506-si-motion-function-specification-control-unit)
- p9509
- p9545
- p9546
- p9547
- r9722.0...31

---

##### SDI (Extended Functions)

###### Description

The "Safe Direction" (SDI) function allows reliable monitoring of the direction of motion of the drive. If this function is activated, the drive can only move in the enabled direction. You can check whether SDI is active in the "[Function status](#function-status)" screen form. When active, at least one of the LEDs is green:

- SDI positive active ([r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).12)
- SDI negative active (r9722.13)

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858432011_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Direction (SDI, Extended Functions)](#description-of-safe-direction-sdi-extended-functions) |

###### Parameterizing SDI (with encoder)

After SDI has been selected via onboard terminals or PROFIsafe (see "[Selecting the safety functionality](#selecting-the-safety-functionality)"), the delay time [p9565](SINAMICS%20Parameter%20SERVO.md#p9565-si-motion-sdi-delay-time-control-unit-1) is started. During this time, you have the option of ensuring that the drive is moving in the enabled direction. After this, the "Safe Direction" function is active and the direction of motion is monitored.

If the drive now moves more than the configured tolerance ([p9564](SINAMICS%20Parameter%20SERVO.md#p9564-si-motion-sdi-tolerance-control-unit-4)) in the blocked direction, message C01716 is output and the stop response defined in [p9566](SINAMICS%20Parameter%20SERVO.md#p9566-si-motion-sdi-stop-response-control-unit-1) is initiated. To acknowledge the messages, you must first deselect SDI, remove the fault cause and then safely acknowledge the messages. Only then can you reselect SDI.

Example:

1. Click the ![Parameterizing SDI (with encoder)](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SDI) to configure control of the "SDI" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SDI" function again.
3. Correct the prescribed delay time in the "Delay time for selection of SDI -&gt; SDI active" field (p9565).
4. In the "Monitoring tolerance" (p9564) field, correct the specified monitoring tolerance in mm.
5. Select the required stop response in the "Selection" drop-down list (p9566).
6. Click the ![Parameterizing SDI (with encoder)](images/147858373771_DV_resource.Stream@PNG-en-US.png) icon to open an additional configuration screen form for the set stop response.

   Make the necessary configuration here.
7. Click "Save project" in the toolbar to save the changes in the project.

**Differences for SDI without encoder**

- For Safe Direction without encoder, after pulse suppression the drive is unable to determine the current speed. For this operating state, the behavior is defined using parameter [p9509](SINAMICS%20Parameter%20SERVO.md#p9509-si-motion-behavior-during-pulse-suppression-control-unit).8:

  - p9509.8 = 1 The status signal displays "inactive".
  - p9509.8 = 0 The status signal displays "active", and the drive takes on the state STO.
- Due to the less precise position recognition, "Safe Direction without encoder" requires a larger tolerance (p9564) compared with the function with encoder.

  > **Note**
  >
  > **No detection of a change in direction by means of [p1820](SINAMICS%20Parameter%20VECTOR.md#p18200n-reverse-the-output-phase-sequence) or [p1821](SINAMICS%20Parameter%20SERVO.md#p18210n-direction-of-rotation-1)**
  >
  > If the direction of rotation is reversed in p1820 or p1821, safe monitoring is still possible: However, in this case, the setpoint limitation [r9733](SINAMICS%20Parameter%20SERVO.md#r973302-co-si-motion-setpoint-speed-limit-effective-1) is calculated with the wrong direction of rotation. Consequently, rotational direction reversal with p1820 or p1821 is not sensible.

**Differences for SDI "without selection"**

As an alternative to control via "onboard terminals" and/or "PROFIsafe", there is also the option of parameterizing SDI "without selection". In this case, SDI will be permanently active after POWER ON (with encoder) or will be active after switch-on (without encoder).

1. Activate the "Function selection" screen form.
2. Select the setting "without selection" from the "Control type" drop-down list.
3. In the "SDI" screen form, select the required stop response in the "Selection" drop-down list (p9566).
4. Click "Save project" in the toolbar to save the changes in the project.

###### Meaning of the display (SDI active)

The "SDI active" icon indicates the following states:

| Symbol | Meaning |
| --- | --- |
| ![Meaning of the display (SDI active)](images/147858416139_DV_resource.Stream@PNG-en-US.png) | SDI not selected |
| ![Meaning of the display (SDI active)](images/147858420107_DV_resource.Stream@PNG-en-US.png) | SDI positive active |
| ![Meaning of the display (SDI active)](images/147858424075_DV_resource.Stream@PNG-en-US.png) | SDI negative active |
| ![Meaning of the display (SDI active)](images/147858428043_DV_resource.Stream@PNG-en-US.png) | SDI positive and SDI negative active |

###### Function diagrams (FD)

SI Extended Functions - SDI (Safe Direction) - 2824 -

SI Extended Functions - SI Motion drive-integrated control signals / status signals - 2840 -

###### Additional parameters

- p1820[0...n]
- p1821[0...n]
- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3).17
- [p9506](SINAMICS%20Parameter%20SERVO.md#p9506-si-motion-function-specification-control-unit)
- p9509
- p9564
- p9565
- p9566
- [p9580](SINAMICS%20Parameter%20SERVO.md#p9580-si-motion-stop-response-delay-bus-failure-control-unit-1)
- [r9720](SINAMICS%20Parameter%20SERVO.md#r9720029-cobo-si-motion-control-signals-integrated-in-the-drive-1).0...27
- r9722.0...31
- r9733.0...2
- [p10017](SINAMICS%20Parameter%20SERVO.md#p10017-si-motion-digital-inputs-debounce-time-processor-1)
- [p10030](SINAMICS%20Parameter%20SERVO.md#p10030-si-motion-sdi-positive-input-terminal-processor-1)[0...3]
- [p10031](SINAMICS%20Parameter%20SERVO.md#p10031-si-motion-sdi-negative-input-terminal-processor-1)[0...3]
- [p10039](SINAMICS%20Parameter%20SERVO.md#p10039-si-motion-safe-state-signal-selection-processor-1)[0...3]
- [p10042](SINAMICS%20Parameter%20SERVO.md#p1004205-si-motion-f-do-signal-sources-processor-1)[0...5]

---

##### SLA (Extended Functions)

###### Description

The function "Safely-Limited Acceleration" (SLA) monitors that the motor does not exceed the defined acceleration limit (e.g. in setup mode). SLA detects an unwanted increase in speed ("runaway") of the drive earlier on and initiates the stop response.

SLA acts during acceleration, but not during braking.

![Safely-Limited Acceleration (SLA): Principle](images/147858458891_DV_resource.Stream@PNG-en-US.png)

Safely-Limited Acceleration (SLA): Principle

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858463755_DV_resource.Stream@PNG-en-US.png) | [Description of Safely Limited Acceleration (SLA, Extended Functions)](#description-of-safely-limited-acceleration-sla-extended-functions) |

###### Requirement

- The "Safely-Limited Acceleration" (SLA) safety function can only be used with encoder and only for 1-encoder systems.

###### Setting Safely-Limited Acceleration

1. Click the ![Setting Safely-Limited Acceleration](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SLA) to configure control of the "SLA" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SLA" function/screen form once again.
3. Enter a value for the acceleration limit of the Safely-Limited Acceleration in the "Acceleration limit" field ([p9578](SINAMICS%20Parameter%20SERVO.md#p9578-si-motion-sla-acceleration-limit-cu-1)).

   This limit value applies to a positive and negative direction of rotation. The drive in [r9790](SINAMICS%20Parameter%20SERVO.md#r979001-si-motion-sla-acceleration-resolution-1) indicates the possible acceleration resolution.
4. In the "Filter time" ([p9576](SINAMICS%20Parameter%20SERVO.md#p9576-si-motion-sla-filter-time-cu)) field, enter a value for the acceleration monitoring filter time.
5. In the "Stop response" ([p9579](SINAMICS%20Parameter%20SERVO.md#p9579-si-motion-sla-stop-response-control-unit)) drop-down list, choose the stop response for Safely-Limited Acceleration.

   If SLA later detects that the acceleration limit has been exceeded, the drive initiates the configured stop response.
6. Click the ![Setting Safely-Limited Acceleration](images/147858373771_DV_resource.Stream@PNG-en-US.png) icon to open the "SS1" screen form.

   Here you correct the settings for the motor deceleration (see "[SS1 (Extended Functions)](#ss1-extended-functions)").
7. Click "Save project" in the toolbar to save the changes in the project.

###### Transmission via PROFIsafe

After SLA has been parameterized and selected, the results of the monitoring are transferred in status words S_ZSW1.8 or S_ZSW2.8.

> **Note**
>
> **Response to bus failure**
>
> If [p9580](SINAMICS%20Parameter%20SERVO.md#p9580-si-motion-stop-response-delay-bus-failure-control-unit-1) ≠ 0 and SLA are active, in the event of communication failure, the parameterized ESR response is only performed if, as the SLA response, a STOP with delayed pulse cancellation when the bus fails has been parameterized (p9579 ≥ 10).

###### Transmission via SIC

After SLA has been parameterized and selected, the results of the monitoring are transferred in the SIC in status word S_ZSW1B.8. You will find this status word in telegrams 700 and 701.

###### Function diagrams (FD)

SI Extended Functions - SLA (Safely-Limited Acceleration) - 2838 -

###### Additional parameters

- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3)
- p9578
- p9579
- [r9714](SINAMICS%20Parameter%20SERVO.md#r971403-co-si-motion-diagnostics-velocity-1)[3]
- r9790

---

##### Actual value measurement/mechanical system (Extended Functions)

###### Requirement

- Extended Functions are selected in the function selection for Safety Integrated.

###### Parameterizing actual value acquisition

For parameterization of the actual value acquisition, only the parameters necessary for your configuration are offered to you.

| Required for configuration:  - Encoder system  - Motor type  - Axis type |  |  |  |  |  |  | Setting | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2-encoder  Rotary  Rotary | 1-encoder  Rotary  Linear | 2-encoder  Rotary  Linear | 1-encoder  Linear  Linear | 2-encoder  Linear  Linear | Without encoder  –  Linear | Without encoder  –  Rotary |  |  |
| x | x | x | x | x | x | x | **Axis type** (p9502) | Select the "Linear axis" or "Rotary axis" axis type. |
| x | x | x | x | x | – | – | **Topology** (p9526) | Select whether you are using a "1-encoder system" or a "2-encoder system". |
| x | x | x | – | – | – | – | **Modulo range** (p9505)  Only for rotary axis / spindle | Set the modulo value in degrees for rotary axes for the "Safe position" function here. This modulo value is taken into account for safe homing and for the transfer of the safe position via PROFIsafe when absolute position is enabled. |
| x | x | x | x | x | x | x | **Monitoring clock** (p9500) | The Safety Integrated Functions are executed in the sampling time indicated in the "Monitoring clock". |
| x | x | x | x | x | x | x | **Actual value acquisition clock** (p9511) | The actual value acquisition clock defines the clock time in which the actual values for Safety Integrated are acquired.  - A slower clock time reduces the maximum permissible velocity, but also reduces the load on the Control Unit for safe actual value acquisition. - The maximum permissible velocity which, if overshot, can trigger faults in the safe actual value acquisition, is indicated in r9730.   Parameterize the actual value acquisition clock identical to the current controller clock (p0115). |
| x | x | x | x | x | x | x | **Accept encoder data** | Click the "Accept encoder data" button to copy the encoder parameters to the associated Safety Integrated parameters.  In a 1-encoder system, the parameter values of the motor encoder "Pulse number" (p9518), "Fine resolution" (p9519) and sign change of the actual position value (p9516.1) are taken from the encoder data and shown in the display fields.   In a 2-encoder system, the parameter values of the external encoder "Pulse number" (p9318), "Fine resolution" (p9319) and sign change of the actual position value (p9316.1) are also taken from the encoder data and shown in the display fields. |
| x | x | x | – | – | – | – | **Rotational direction reversal**  (p9539[0]) | Activate this option if rotational direction reversal is involved for the gear. |
| x | x | x | x | x | – | – | **Number of pulses** (p9518) for motor encoders | Shows the number of pulses of the deployed encoder. |
| x | x | x | x | x | – | – | **Fine resolution** (p9519) for motor encoders | Shows the number of bits of the deployed encoder control word. |
| x | x | x | x | x | – | – | **Sign change** (p9511.1) | Shows whether a sign change has been activated for the actual position value. |
| x | x | x | – | – | x | x | **Load revolutions/**   **encoder revolutions**   (p9521)  (p9522) | The gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft (load revolutions).  Acquire the number of load revolutions and the encoder revolutions for the motor encoder. |
| x | – | – | – | – | – | – | **Load revolutions/**   **encoder revolutions**    (p9321)  (p9322) | A gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft (load revolutions).  Acquire the number of load revolutions and the encoder revolutions for the external encoder. |
| x | – | x | – | x | – | – | **Pulses per revolution** (p9318) for external encoder | Shows the number of pulses of the deployed encoder. |
| x | – | x | – | x | – | – | **Fine resolution** (p9319) for external encoder | Shows the number of bits of the deployed encoder control word. |
| x | – | x | – | x | – | – | **Sign change** (p9316.1) | Shows whether a sign change has been activated for the actual position value. |
| x | – | x | – | x | – | – | **Actual value synchronization**  (p9501.3) | If actual value synchronization has been activated, the actual values of both channels are averaged.  Whereby, the maximum slip defined in p9549 is monitored once per cross-check clock (r9724).  If "actual value synchronization" is locked, the value parameterized in p9542 is used as tolerance for the crosswise comparison. |
| x | – | x | – | x | x | x | **Actual value tolerance** (p9542) | Set the tolerance for the crosswise comparison of the actual position between the two monitoring channels. |
| x | – | x | – | x | – | – | **Velocity tolerance** (p9549) | Set the maximum tolerance for the crosswise comparison of the actual velocity (only if actual value synchronization has been activated). |
| – | – | – | – | – | x | – | **Spindle pitch** (p9520) | Set the transmission ratio between the encoder and load in mm (linear axis with rotary encoder) (available only for linear axis). |
| – | – | – | – | – | x | x | **Pole pair count** (p0313) | The safe actual value acquisition without encoder calculates the electrical speed of the drive. The pole pair count specifies the factor with which the electrical speed must be multiplied in order to obtain the mechanical speed at the motor shaft. |

---

**See also**

[Reliable actual value acquisition with encoder system](#reliable-actual-value-acquisition-with-encoder-system)
  
[Safe current actual value acquisition without encoder](#safe-current-actual-value-acquisition-without-encoder)

#### Advanced Functions

This section contains information on the following topics:

- [SP (Advanced Functions)](#sp-advanced-functions)
- [SLP (Advanced Functions)](#slp-advanced-functions)
- [SCA (Advanced Functions)](#sca-advanced-functions)
- [Safe homing (Advanced Functions)](#safe-homing-advanced-functions)

##### SP (Advanced Functions)

###### Description

The "Safe Position (SP)" function enables you to transfer safe position values to the higher-level fail-safe controller (F‑CPU) via PROFIsafe (telegrams 901, 902 or 903).

From the position change over time, the F‑CPU can also calculate the current velocity. In telegram 902, the values are transferred in 32-bit format, in telegram 901, in 16-bit format.

After parameter assignment, release and POWER ON, the function is automatically selected and the values transferred. Please observe the following:

- Transfer of safe absolute position values

  - If the transfer of the safe relative position has been enabled through [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3).25 = 1 and p9501.2 = 0, the validity of the safe relative position is displayed by the set bit S_ZSW2.22.
  - If the transfer of the safe absolute position has been enabled using p9501.25 = 1 and p9501.2 = 1, S_ZSW2.22 is only set when the drive has also been safely homed.
- Transfer of safe relative position values (e.g. for calculating the velocity)

  - Only S_ZSW2.22 ([r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).22, actual position value valid) must be set to calculate the speed.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858520971_DV_resource.Stream@PNG-en-US.png) | [Transferring safe position values (SP, Advanced Functions)](#transferring-safe-position-values-sp-advanced-functions) |

###### Requirement

- The "via PROFIsafe" control type must be activated (see "[Selecting the safety functionality](#selecting-the-safety-functionality)").

###### Configuring safe absolute position

1. Select the "absolute" setting in the "Safe Position" ([p9502](SINAMICS%20Parameter%20SERVO.md#p9502-si-motion-axis-type-control-unit-1).1) drop-down list.
2. Click the "Safe homing" button and check the actual position values in the dialog of the same name.
3. In the "Tolerance for actual value comparison" ([p9544](SINAMICS%20Parameter%20SERVO.md#p9544-si-motion-actual-value-comparison-tolerance-referencing-cu-4)) field enter a tolerance value for checking the actual values.
4. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring safe relative position

1. Select the "relative" setting in the "Safe Position" (p9502.1) drop-down list.
2. Click the "Safe homing" button and check the actual position values in the dialog of the same name.
3. Click "Save project" in the toolbar to save the changes in the project.

###### Acceptance test

An acceptance test is not required for the "Transfer of Safe Position values" function. However, the function that was implemented with the aid of SP must be accepted in the higher-level controller.

###### Function diagrams (FD)

SI Extended Functions - SI Motion drive-integrated control signals / status signals - 2840 -

###### Additional parameters

- p9501
- [p9505](SINAMICS%20Parameter%20SERVO.md#p9505-si-motion-sp-modulo-value-control-unit)
- [p9542](SINAMICS%20Parameter%20SERVO.md#p9542-si-motion-act-val-comparison-tol-cross-check-control-unit-4)
- [p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)
- [r9708](SINAMICS%20Parameter%20SERVO.md#r970805-si-motion-diagnostics-safe-position-4)[0...5]
- [r9713](SINAMICS%20Parameter%20SERVO.md#r971305-co-si-motion-diagnostics-position-actual-value-load-side-1)[0...5]

---

##### SLP (Advanced Functions)

###### Description

The "Safely-Limited Position" (SLP) function is used to safely monitor the limits of two traversing or positioning ranges which can be switched over by a safe signal.

As soon as "SLP" is active, maintaining the limits of the active positioning range is safely monitored. With a safety signal you can switch between 2 position ranges. Each position range is limited by its previously defined limit switch pair. When passing the position of one of the two limit switches, a parameterizable stop response (STOP A, STOP B, STOP C, STOP D or STOP E) is initiated and the Safety message C01715 output.

To acknowledge this fault, you can either switch over to a range whose limits have not been violated, or you can deselect the "SLP" function. After acknowledgment, the drive can then be traversed again in the permissible range.

You will find a description of safe homing here: [Safe homing (Advanced Functions)](#safe-homing-advanced-functions)

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858550155_DV_resource.Stream@PNG-en-US.png) | [Description of Safely-Limited Position (SLP, Advanced Functions)](#description-of-safely-limited-position-slp-advanced-functions) |

> **Note**
>
> **No actual value synchronization for SLP**
>
> It is not permissible to simultaneously enable the SLP function and the actual value synchronization ([p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3).3 = 1). In this case, the drive outputs fault F01688.

###### Requirements

- Use of one or two suitable encoders for the Safety Integrated Extended Functions with encoder
- Determining the absolute position of the drive by homing during commissioning and after all actions after which a safe absolute reference can no longer be guaranteed (POWER ON, parking)

###### Configuring SLP

Selecting "SLP" and switching over between the position ranges is realized via an F-DI or a PROFIsafe control bit. SLP selection can be checked using parameter [r9720](SINAMICS%20Parameter%20SERVO.md#r9720029-cobo-si-motion-control-signals-integrated-in-the-drive-1).6. The selected position range can be checked using parameter r9720.19. Status bit [r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).6 is set if SLP is active. The active position range is displayed by r9722.19. Maintaining the upper or lower active SLP limit can be checked using r9722.30 and r9722.31.

1. Click the ![Configuring SLP](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SLP) to configure control of the "SLP" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SLP" function again.
3. Specify the limit values of position range 1 in the P<sub>min</sub> ([p9535](SINAMICS%20Parameter%20SERVO.md#p953501-si-motion-slp-se-lower-limit-values-control-unit-4)[0]) and P<sub>max</sub> ([p9534](SINAMICS%20Parameter%20SERVO.md#p953401-si-motion-slp-se-upper-limit-values-control-unit-4)[0]) input fields.
4. Select the stop response for position range 1 in the "Selection" drop-down list ([p9562](SINAMICS%20Parameter%20SERVO.md#p956201-si-motion-slp-se-stop-response-control-unit-1)[0]).
5. Click the ![Configuring SLP](images/147858373771_DV_resource.Stream@PNG-en-US.png) icon to open an additional configuration screen form for position range 1.

   Make the necessary configuration here.
6. Specify the limit values of position range 2 in the input fields P<sub>min</sub> (p9535[1]) and P<sub>max</sub> (p9534[1]).
7. Select the stop response for position range 2 in the "Selection" drop-down list (p9562[1]).
8. Click the ![Configuring SLP](images/147858373771_DV_resource.Stream@PNG-en-US.png) icon to open an additional configuration screen form for position range 2.

   Make the necessary configuration here.
9. Enter a suitable value in mm in the "Tolerance for actual value comparison" ([p9544](SINAMICS%20Parameter%20SERVO.md#p9544-si-motion-actual-value-comparison-tolerance-referencing-cu-4)) field.
10. Click "Save project" in the toolbar to save the changes in the project.

###### Control and status signals from the SLP

Selecting SLP and switching over between the position ranges is realized via an F-DI or a PROFIsafe control bit. SLP selection can be checked using parameter r9720.6. The selected position range can be checked using parameter r9720.19. Status bit r9722.6 is set if SLP is active. The active position range is displayed by r9722.19. Maintaining the upper or lower active SLP limit can be checked using r9722.30 and r9722.31.

> **Note**
>
> **Jumps in the display**
>
> There is no hysteresis available for r9722.30 and r9722.31. Small fluctuations in the area around the range limit can result in the display jumping back and forth.

###### Function diagrams (FD)

SI Advanced Functions - SLP (Safely-Limited Position) - 2822 -

SI Extended Functions - SI Motion drive-integrated control signals / status signals - 2840 -

###### Additional parameters

- p9501.0
- p9534[0...1]
- p9535[0...1]
- p9544
- p9562[0...1]
- [p10032](SINAMICS%20Parameter%20SERVO.md#p10032-si-motion-slp-select-input-terminal-processor-1)[0...3]
- [p10033](SINAMICS%20Parameter%20SERVO.md#p10033-si-motion-slp-position-range-input-terminal-processor-1)[0...3]
- [p10039](SINAMICS%20Parameter%20SERVO.md#p10039-si-motion-safe-state-signal-selection-processor-1)[0...3]
- [p10109](SINAMICS%20Parameter%20SERVO.md#p10109-si-motion-slp-retraction-f-di-processor-2)
- [p10132](SINAMICS%20Parameter%20SERVO.md#p10132-si-motion-slp-input-terminal-processor-2)
- [p10133](SINAMICS%20Parameter%20SERVO.md#p10133-si-motion-slp-position-range-input-terminal-processor-2)
- [p10139](SINAMICS%20Parameter%20SERVO.md#p10139-si-motion-safe-state-signal-selection-processor-2)

---

##### SCA (Advanced Functions)

###### Description

With the "Safe Cam" function ("SCA"), you implement safe electronic cams, safe zone sensing, or a working area limitation/protection zone delimitation for a specific axis, to replace a hardware-based solution. You parameterize up to 30 cams for each axis. You enable each cam individually.

For the function descriptions, see also:

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147858581899_DV_resource.Stream@PNG-en-US.png) | [Description of Safe Cam (SCA, Advanced Functions)](#description-of-safe-cam-sca-advanced-functions) |

###### Requirement

- The "Safe Cam" (SCA) safety function can only be used with an encoder.

###### Configuring SCA

1. Click the ![Configuring SCA](images/147858154379_DV_resource.Stream@PNG-en-US.png) button (Select SCA) to configure control of the "SCA" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SCA" function/screen form again.
3. Owing to variations in the cycle and signal propagation times, the cam signals of the two monitoring channels do not switch simultaneously and not precisely at the same position.

   If necessary, define a tolerance band for all cams in the "Hysteresis" field ([p9540](SINAMICS%20Parameter%20SERVO.md#p9540-si-motion-sca-sn-tolerance-control-unit-4)). Within this tolerance band, the monitoring channels can have different signal states for the same cam:

   ![Parametrize cam and tolerance](images/147858577035_DV_resource.Stream@PNG-en-US.png)

   Parametrize cam and tolerance

   > **Note**
   >
   > The smallest possible tolerance band should be selected for the SCA function (&lt; 5 ... 10 mm). It makes sense to parameterize the cam tolerance to be greater than or equal to the actual value tolerance.
4. Specify the cam positions you wish to monitor in the list at the bottom end of the screen form.

   - Activate the desired cam in the list (= enable).
   - Enter the minus cam position and the plus cam position in the input fields in the same row of the list.

     The defined cams must have a minimum length of: Plus cam position - minus cam position ≥ Hysteresis + tolerance for actual value comparison ([p9542](SINAMICS%20Parameter%20SERVO.md#p9542-si-motion-act-val-comparison-tol-cross-check-control-unit-4)).

     If you violate this rule, the drive will output the message F01686 ("SI Motion: Cam position parameterization not permissible").
5. Home the axis using the "Safe homing" function.

   - Click on the ![Configuring SCA](images/147858585867_DV_resource.Stream@PNG-en-US.png) icon and record the required actual position values in the "Safe homing" dialog (see "[Safe homing (Advanced Functions)](#safe-homing-advanced-functions)").

     | Symbol | Meaning |
     | --- | --- |
     |  | **Warning** |
     | **Safe homing**  The enabled cam signals are output immediately after POWER ON. This output is, however, only safe after safe homing, i.e. the cams are only considered safe after "Safe homing" has been performed. - Home the axis using the "Safe homing" function. |  |
6. Click "Save project" in the toolbar to save the changes in the project.

###### Cam synchronization

For transmission of the cam status word via PROFIsafe to the F host, the cam signals of the two monitoring channels are synchronized. The function also monitors whether a different cam signal from the 2nd channel is plausible. If the drive detects an error, it outputs the message C01711 with the disturbance value 1014.

As the position tolerance for monitoring the cam positions, the tolerance for the crosswise comparison of the actual position between the two monitoring channels in p9542 ("Actual value tolerance") is used.

###### Transmission via PROFIsafe

After SCA has been parameterized and selected, the monitoring results are transmitted in status word S_ZSW_CAM1.

###### Function diagrams (FD)

SI Advanced Functions - SCA (Safe Cam) - 2826 -

SI Advanced Functions - S_ZSW_CAM1 Safety status word Safe Cam 1 - 2844 -

###### Additional parameters

- [p9501](SINAMICS%20Parameter%20SERVO.md#p9501-si-motion-enable-safety-functions-control-unit-3)
- [p9503](SINAMICS%20Parameter%20SERVO.md#p9503-si-motion-sca-sn-enable-control-unit-1)
- [p9505](SINAMICS%20Parameter%20SERVO.md#p9505-si-motion-sp-modulo-value-control-unit)
- [p9536](SINAMICS%20Parameter%20SERVO.md#p9536029-si-motion-sca-sn-plus-cam-position-control-unit-4)[0...29]
- [p9537](SINAMICS%20Parameter%20SERVO.md#p9537029-si-motion-sca-sn-minus-cam-position-control-unit-4)[0...29]
- p9540
- p9542
- [r9703](SINAMICS%20Parameter%20SERVO.md#r9703031-cobo-si-motion-sca-status-signal-control-unit).0...31
- [r9718](SINAMICS%20Parameter%20SERVO.md#r971823-cobo-si-motion-control-signals-1-4)[0...5]
- [r9720](SINAMICS%20Parameter%20SERVO.md#r9720029-cobo-si-motion-control-signals-integrated-in-the-drive-1).0...23
- [r9727](SINAMICS%20Parameter%20SERVO.md#r9727-si-motion-user-agreement-inside-the-drive)
- [r9771](SINAMICS%20Parameter%20SERVO.md#r9771-si-common-functions-control-unit)

---

##### Safe homing (Advanced Functions)

###### Description

![Description](images/147858614283_DV_resource.Stream@PNG-en-US.png)

The "Safe homing" function allows a safe absolute position to be defined. This safe position is used for the following functions:

- [SLP (Advanced Functions)](#slp-advanced-functions)
- [SP (Advanced Functions)](#sp-advanced-functions)
- [SCA (Advanced Functions)](#sca-advanced-functions)

**Perform homing**

In most cases, an external control performs homing to an absolute position. The converter only performs this task in special cases (for example, EPOS).

- Homing using an external control

  Requirement: No movement of the drive

  The home position determined by the control is entered into parameter p9572 and is declared to be valid using p9573 = 89.
- Homing using EPOS

  The SINAMICS EPOS function transfers, when homing, the determined position directly to Safety Integrated. This can also take place during motion.
- User agreement

  The user agreement must be set (p9726 = p9740 = AC hex) within 2 seconds after homing.

Safety Integrated only evaluates the home position if this is required by a function that has been enabled (e.g. SLP). Using diagnostics bit r9723.17, Safety Integrated indicates whether the drive has been homed. Safety Integrated indicates the position of the drive in diagnostic parameters r9708 and r9713. Bit r9722.23 is set when the axis is safely homed.

###### Homing types

SINAMICS distinguishes between 2 types of homing:

- Initial homing

  For initial safe homing, or in the event of a fault during a subsequent homing, the following steps are necessary:

  - The home position determined by the controller is entered in parameter p9572 and is declared to be valid with p9573 = 89. This step is not required for closed-loop position control with EPOS.
  - Homing has been correctly implemented (r9723.17 = 1)
  - Confirm the actual position value by clicking "Confirm the actual position value": Within 2 s, set parameters p9726 = p9740 = AC hex

    If both parameters are not set within the 2 seconds, the converter outputs the messages C01711 (value: 1002).

    After this "user agreement", the drive is "safely homed" (r9722.23 = 1)

    > **Note**
    >
    > **No automatic user agreement permitted**
    >
    > Please note that the operator must be capable of assigning the determined position to the real position of the axis before setting the user agreement. This can be performed, for example, by a visual inspection of the axis position. Under no circumstances must these parameters ever be set fully automatically by a control system without agreement by the user. This would only be permitted if the home position can be safely sensed by means of a safe sensor.
- Subsequent homing

  Subsequent homing involves referencing with a safe history (i.e. with an internally battery-backed user agreement) after a POWER ON or after deselecting "parking axis."

  - The position determined by the controller is entered in parameter p9572 and is declared to be valid with p9573 = 89. This step is not required for closed-loop position control with EPOS and use of an absolute encoder.
  - After the drive has been homed, Safety Integrated automatically performs a plausibility check.
  - If the deviation between the actual absolute position and the previous standstill position saved from Safety Integrated in the NVRAM is within the tolerance p9544, the drive goes into the "safely homed" state (r9722.23 = 1).

###### Value range r9708

The diagnostic information in parameter r9708 is displayed with the following properties:

Value range and resolution (32 bits)

|  | Linear axis | Rotary axis |
| --- | --- | --- |
| Position values | ±737280000 | ±737280000 |
| Unit | 1 μm | 0.001 ° |
| Comment | Monitoring ±737.280 m with an accuracy of 1 μm | ≙ 2048 revolutions |

What is shown in parameter r9713 is identical to the values of r9708; however, in SINAMICS-internal calculation units.

###### Function diagrams (FD)

SI Extended Functions - Safe referencing - 2821 -

#### Control

This section contains information on the following topics:

- [Control via PROFIsafe](#control-via-profisafe)
- [Control via PROFIsafe and via onboard terminals (only CU320-2)](#control-via-profisafe-and-via-onboard-terminals-only-cu320-2)
- [Control via PROFIsafe and via onboard terminals (only CU310-2)](#control-via-profisafe-and-via-onboard-terminals-only-cu310-2)
- [Control via onboard terminals (only CU310-2)](#control-via-onboard-terminals-only-cu310-2)
- [Control without selection](#control-without-selection)

##### Control via PROFIsafe

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrollable responses of the drive when PROFIsafe addresses are not unique**  PROFIsafe addresses can be assigned via an automated mechanism. If these automatically generated PROFIsafe addresses are not unique CPU-wide and network-wide, this can lead to uncontrollable responses of the drive. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that the fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - Make sure that the fail-safe destination address of the fail-safe I/O (drive units in this case) is unique for the entire fail-safe I/O network-wide and CPU-wide (system-wide). The fail-safe I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Please also refer to the corresponding documentation in the online help of the TIA Portal in the section "[SIMATIC Safety - Configuration and programming](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#simatic-safety---configuring-and-programming)". |  |

###### Requirements

- A project has been created.
- In the Safety Integrated [function selection](VECTOR%20drives%20%28universal%29.md#selecting-the-safety-functionality), control "via PROFIsafe" is activated.
- The desired Safety Functions are also activated in the function selection.
- The Safety Integrated Extended Functions with the control type " via PROFIsafe" ([p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)) are selected in the Safety Integrated function selection.

###### Configuring control via PROFIsafe

The PROFIsafe address is required for control of the Safety Integrated Functions via PROFIsafe.

1. Click the "Telegram configuration" icon.

   ![Configuring control via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG)

   ![Configuring control via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG)

   The properties of the PROFINET interface are displayed in the inspector window. The "Cyclic data traffic" adjustment range is active. The telegrams for the drive objects can be specified here.
2. Click in the telegram configuration of the "Drive control telegrams" on the entry &lt;Add telegram&gt;.
3. Select the "Add Safety telegram" option in the drop-down list of the entry.

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. The relevant PROFIsafe telegrams are preassigned.
4. Open the new screen form "Receive Safety Integrated Telegram (setpoint)" in the inspector window.
5. Correct the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" screen form.

   The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20SERVO.md#p9610-si-profisafe-address-control-unit)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Select the desired stop response for a failure of the PROFIsafe communication in the "PROFIsafe failure response" ([p9612](SINAMICS%20Parameter%20SERVO.md#p9612-si-profisafe-failure-response-control-unit)) drop-down list.

###### Additional parameters

- p9610
- [p9650](SINAMICS%20Parameter%20SERVO.md#p9650-si-sge-changeover-discrepancy-time-control-unit)
- [p9651](SINAMICS%20Parameter%20SERVO.md#p9651-si-stosbcss1-debounce-time-control-unit)

---

##### Control via PROFIsafe and via onboard terminals (only CU320-2)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrollable responses of the drive when PROFIsafe addresses are not unique**  PROFIsafe addresses can be assigned via an automated mechanism. If these automatically generated PROFIsafe addresses are not unique CPU-wide and network-wide, this can lead to uncontrollable responses of the drive. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that the fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - Make sure that the fail-safe destination address of the fail-safe I/O (drive units in this case) is unique for the entire fail-safe I/O network-wide and CPU-wide (system-wide). The fail-safe I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Please also refer to the corresponding documentation in the online help of the TIA Portal in the section "[SIMATIC Safety - Configuration and programming](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#simatic-safety---configuring-and-programming)". |  |

###### Requirements

- A project has been created.
- In the Safety Integrated [function selection](VECTOR%20drives%20%28universal%29.md#selecting-the-safety-functionality), control "via PROFIsafe" is activated.
- The desired Safety Functions are also activated in the function selection.
- The Safety Integrated Extended Functions with the control type " via PROFIsafe" ([p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)) are selected in the Safety Integrated function selection.
- The "Basic Functions via onboard terminals" option is additionally activated.

###### Configuring control via PROFIsafe

The PROFIsafe address is required for control of the Safety Integrated Functions via PROFIsafe.

1. Click the "Telegram configuration" icon.

   ![Configuring control via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG)

   ![Configuring control via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG)

   The properties of the PROFINET interface are displayed in the inspector window. The "Cyclic data traffic" adjustment range is active. The telegrams for the drive objects can be specified here.
2. Click in the telegram configuration of the "Drive control telegrams" on the entry &lt;Add telegram&gt;.
3. Select the "Add Safety telegram" option in the drop-down list of the entry.

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. The relevant PROFIsafe telegrams are preassigned.
4. Open the new screen form "Receive Safety Integrated Telegram (setpoint)" in the inspector window.
5. Correct the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" screen form.

   The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20SERVO.md#p9610-si-profisafe-address-control-unit)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Select the desired stop response for a failure of the PROFIsafe communication in the "PROFIsafe failure response" ([p9612](SINAMICS%20Parameter%20SERVO.md#p9612-si-profisafe-failure-response-control-unit)) drop-down list.

###### Configuring the F-DI configuration

The signal states at the two onboard terminals of an F-DI are monitored in order to determine whether these have assumed the same logical state within the discrepancy time.

For example, the unavoidable delay caused by mechanical switching operations can be adapted via parameters. The time within which the selection or deselection must be performed in both monitoring channels in order to qualify as "simultaneous" is specified with [p9650](SINAMICS%20Parameter%20SERVO.md#p9650-si-sge-changeover-discrepancy-time-control-unit).

For internal errors or limit value violations, the drive-internal Safety Integrated Function issues Safety Integrated faults (see [Safety Integrated faults (Basic Functions)](VECTOR%20drives%20%28universal%29.md#safety-integrated-faults-basic-functions)).

1. Interconnect the signal source [p9620](SINAMICS%20Parameter%20SERVO.md#p962007-bi-si-signal-source-for-sto-shsbcss1-control-unit) for STO, SS1 or SBC on the Control Unit.

   Only a fixed zero and the digital inputs DI 0 ... 7, 16, 17, 20, 21 are allowed as signal sources.
2. Enter a discrepancy time [ms] in the "Discrepancy time" (p9650) field.
3. Enter a time [ms] for the input filter (debounce time) in the "F-DI input filter" ([p9651](SINAMICS%20Parameter%20SERVO.md#p9651-si-stosbcss1-debounce-time-control-unit)) field.

   This debounce time applies for the F-DIs and the readback input for the forced checking procedure. The debounce time specifies the maximum time an interference pulse can be present at F-DIs before being interpreted as a switching operation.

###### Additional parameters

- p9610
- p9650
- p9651

---

##### Control via PROFIsafe and via onboard terminals (only CU310-2)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrollable responses of the drive when PROFIsafe addresses are not unique**  PROFIsafe addresses can be assigned via an automated mechanism. If these automatically generated PROFIsafe addresses are not unique CPU-wide and network-wide, this can lead to uncontrollable responses of the drive. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that the fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - Make sure that the fail-safe destination address of the fail-safe I/O (drive units in this case) is unique for the entire fail-safe I/O network-wide and CPU-wide (system-wide). The fail-safe I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Please also refer to the corresponding documentation in the online help of the TIA Portal in the section "[SIMATIC Safety - Configuration and programming](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#simatic-safety---configuring-and-programming)". |  |

###### Requirements

- A project has been created.
- In the Safety Integrated [function selection](VECTOR%20drives%20%28universal%29.md#selecting-the-safety-functionality), control "via PROFIsafe" is activated.
- The desired Safety Functions are also activated in the function selection.
- The Safety Integrated Extended Functions with the control type " via PROFIsafe" ([p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)) are selected in the Safety Integrated function selection.
- The "Basic Functions via onboard terminals" option is additionally activated.

###### Configuring control via PROFIsafe

The PROFIsafe address is required for control of the Safety Integrated Functions via PROFIsafe.

1. Click the "Telegram configuration" icon.

   ![Configuring control via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG)

   ![Configuring control via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG)

   The properties of the PROFINET interface are displayed in the inspector window. The "Cyclic data traffic" adjustment range is active. The telegrams for the drive objects can be specified here.
2. Click in the telegram configuration of the "Drive control telegrams" on the entry &lt;Add telegram&gt;.
3. Select the "Add Safety telegram" option in the drop-down list of the entry.

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. The relevant PROFIsafe telegrams are preassigned.
4. Open the new screen form "Receive Safety Integrated Telegram (setpoint)" in the inspector window.
5. Correct the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" screen form.

   The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20SERVO.md#p9610-si-profisafe-address-control-unit)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Select the desired stop response for a failure of the PROFIsafe communication in the "PROFIsafe failure response" ([p9612](SINAMICS%20Parameter%20SERVO.md#p9612-si-profisafe-failure-response-control-unit)) drop-down list.

###### Configuring the F-DI configuration

The signal states at the two onboard terminals of an F-DI are monitored in order to determine whether these have assumed the same logical state within the discrepancy time.

For example, the unavoidable delay caused by mechanical switching operations can be adapted via parameters. The time within which the selection or deselection must be performed in both monitoring channels in order to qualify as "simultaneous" is specified with [p9650](SINAMICS%20Parameter%20SERVO.md#p9650-si-sge-changeover-discrepancy-time-control-unit).

For internal errors or limit value violations, the drive-internal Safety Integrated Function issues Safety Integrated faults (see [Safety Integrated faults (Basic Functions)](VECTOR%20drives%20%28universal%29.md#safety-integrated-faults-basic-functions)). The signal sources are permanently set and therefore cannot be connected separately on a CU310-2.

1. Enter a discrepancy time [ms] in the "Discrepancy time" (p9650) field.
2. Enter a time [ms] for the input filter (debounce time) in the "F-DI input filter" ([p9651](SINAMICS%20Parameter%20SERVO.md#p9651-si-stosbcss1-debounce-time-control-unit)) field.

   This debounce time applies for the F-DIs and the readback input for the forced checking procedure. The debounce time specifies the maximum time an interference pulse can be present at F-DIs before being interpreted as a switching operation.

###### Additional parameters

- p9610
- p9650
- p9651

---

##### Control via onboard terminals (only CU310-2)

###### Description

When controlling via onboard terminals, the settings differ depending on the respective control unit. The settings for the CU310-2 PN are explained in more detail below.

###### Requirements

- A project has been created.
- A CU310-2 PN Control Unit has been inserted in the device configuration.
- A Power Module of the type AC Power Module or PM240-2 has been inserted in the device configuration.
- In the Safety Integrated [function selection](VECTOR%20drives%20%28universal%29.md#selecting-the-safety-functionality), the Safety Integrated Extended Functions are selected with the control type "via onboard terminals" ([p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2)).

###### Configuring the F-DI configuration

In the "F-DI configuration" field in the "Selection F-DI" area, configure the inputs of the selected Safety Integrated Extended Functions of the drive.

The fail-safe digital inputs (F-DI) can only be configured for the Safety Integrated Functions that were activated in the "Function selection" screen form.

1. In the "Selection F-DI" drop-down list ([p10022](SINAMICS%20Parameter%20SERVO.md#p10022-si-motion-sto-input-terminal-processor-1) to [p10033](SINAMICS%20Parameter%20SERVO.md#p10033-si-motion-slp-position-range-input-terminal-processor-1)), select the desired input terminal for the respective Safety Integrated Function.
2. If you have activated the Safety Integrated Function SLP:  
   Select the F-DI for the SLP retraction logic in the "Selection F-DI" drop-down list ([p10009](SINAMICS%20Parameter%20SERVO.md#p10009-si-motion-slp-retraction-f-di-processor-1)).
3. Select the F-DI for the "Acknowledgment internal event" signal in the "Acknowledgment of Safety Integrated alarms" drop-down list ([p10006](SINAMICS%20Parameter%20SERVO.md#p10006-si-motion-acknowledgment-internal-event-f-di-processor-1)).
4. Select the input mode of the fail-safe digital inputs F-DI 0 to F-DI 1.  
   In the drop-down lists "Connection configuration F-DI 0" to "Connection configuration F-DI 2" ([p10040](SINAMICS%20Parameter%20SERVO.md#p10040-si-motion-f-di-input-mode-processor-1).0 to p10040.2), select whether the F-DI should be NC or NO.
5. Enter a discrepancy time [ms] in the "F-DI discrepancy time" field ([p10002](SINAMICS%20Parameter%20SERVO.md#p10002-si-motion-f-di-changeover-discrepancy-time-processor-1)).
6. Enter a time [ms] for the input filter (debounce time) in the "F-DI input filter" ([p10017](SINAMICS%20Parameter%20SERVO.md#p10017-si-motion-digital-inputs-debounce-time-processor-1)) field.

   This debounce time applies for the F-DIs and the readback input for the forced checking procedure. The debounce time specifies the maximum time an interference pulse can be present at F-DIs before being interpreted as a switching operation.

###### Configuring the F-DO configuration

Configure the F-DO as follows:

1. Click the "Safe State" button.  
   A dialog with the same name opens.
2. Select the individual signals of the individual Safety Integrated Functions to be linked to form a "Safe State".  
   For this purpose, click the connector button in the row of the respective Safety Integrated Function. If the button shows a closed connection between two points, the Safety Integrated Function is linked with "Safe State" ([p10039](SINAMICS%20Parameter%20SERVO.md#p10039-si-motion-safe-state-signal-selection-processor-1).0 to p10039.7).
3. Click "Close" to accept the settings and close the dialog.
4. Select the signal sources for F-DO 0 (X131.5). You can create an AND logic operation for up to six signal sources and output the result at F-DO 0.  
   Click on the six drop-down lists ([p10042](SINAMICS%20Parameter%20SERVO.md#p1004205-si-motion-f-do-signal-sources-processor-1)[0] to 10042[5]) and select a signal source for the AND logic operation.
5. Optional: Set the test mode for F-DO 0.  
   Activate the "Test FD-O" option ([p10046](SINAMICS%20Parameter%20SERVO.md#p10046-si-motion-f-do-feedback-signal-input-activation)) to enable the readback input for F-DO 0.  
   Click on the drop-down list beside it and select the desired test mode ([p10047](SINAMICS%20Parameter%20SERVO.md#p10047-si-motion-f-do-test-stop-mode-processor-1)).
6. In the "Wait time for test" field ([p10001](SINAMICS%20Parameter%20SERVO.md#p10001-si-motion-wait-time-for-test-stop-at-do-processor-1)), enter the wait time for the test of the digital output.  
   Within this time, for a forced checking procedure of the digital output, the signal must have been detected via the corresponding feedback input (p10047).

###### Function diagrams (FD)

SI Basic Functions - S_STW1/2 safety control word 1/2, S_ZSW1/2 safety status word 1/2 - 2806 -

SI Basic Functions - STO (Safe Torque Off), SS1 (Safe Stop 1) - 2810 -

SI Extended Functions - S_STW1 safety control word 1, S_ZSW1 safety status word 1 - 2842 -

SI Extended Functions - S_STW2 safety control word 2, S_ZSW2 safety status word 2 - 2843 -

###### Additional parameters

- [p9610](SINAMICS%20Parameter%20SERVO.md#p9610-si-profisafe-address-control-unit)
- [p9650](SINAMICS%20Parameter%20SERVO.md#p9650-si-sge-changeover-discrepancy-time-control-unit)
- [p9651](SINAMICS%20Parameter%20SERVO.md#p9651-si-stosbcss1-debounce-time-control-unit)

---

##### Control without selection

###### Overview

As an alternative to control via onboard terminals and/or PROFIsafe, it is also possible to assign parameters to the SDI or SLS functions without selection. In this case, the "SDI" function is permanently active after POWER ON (with encoder) or becomes active after switching on (without encoder) (see [SDI (Extended Functions)](VECTOR%20drives%20%28universal%29.md#sdi-extended-functions)). With the "SLS without selection" function, there is no delay time and the function is permanently active after POWER ON (with encoder), or it becomes active when switched on (without encoder) (see [SLS (Extended Functions)](VECTOR%20drives%20%28universal%29.md#sls-extended-functions)).

###### Requirements

- A project has been created.
- In the Safety Integrated [function selection](VECTOR%20drives%20%28universal%29.md#selecting-the-safety-functionality), the Safety Integrated Extended Functions are selected with the control type "without selection" (p9601).

###### Configuring control without selection

1. Select whether SLS should be selected permanently in the "SLS static" (p9512.4) drop-down list.
2. Select whether SDI positive static should be selected permanently in the "SDI positive static" (p9512.12) drop-down list.
3. Select whether SDI negative static should be selected permanently in the "SDI negative static" (p9512.13) drop-down list.

#### Test stop

##### Description

Parameterize the settings for the test of shutdown paths (test stop) in the "Test stop" screen form.

To meet the requirements of the DIN EN ISO 13849‑1 and IEC 61508 standards in terms of timely fault detection, the converter must test its safety-related circuits regularly – at least once a year – for correct functioning. The converter monitors the regular test of its safety-related circuits that monitor the speed of the motor, and to safely interrupt the torque-generating energy supply to the motor through the safe pulse suppression.

You can find detailed theoretical information here:

- [Test stop for Basic Functions](#test-stop-for-basic-functions).
- [Test stop of Extended/Advanced Functions](#test-stop-of-extendedadvanced-functions)

##### Test stop for Basic Functions

1. Enter the interval for performing the forced checking procedure and testing the Safety shutdown paths in the "Timer test stop" ([p9659](SINAMICS%20Parameter%20SERVO.md#p9659-si-forced-checking-procedure-timer)) field.

   Within the parameterized time, the "Safe Stop 1" (SS1) function must be deselected at least once. The monitoring time is reset at every STO deselection.
2. Interconnect the "Test stop required" ([r9773](SINAMICS%20Parameter%20SERVO.md#r9773031-cobo-si-status-control-unit-motor-module).31) signal sink to a digital output or to a bit in the status word of the fieldbus.

**Note**

**Reset timer of Basic Functions automatically**

If, when simultaneously using Extended/Advanced Functions, the associated test stop is performed, the timer of the Basic Functions is also reset.

While STO is selected by the Extended Functions, the onboard terminals for the selection of the Basic Functions are not checked for discrepancy. This means that the test stop of the Basic Functions must always be performed without the selection of STO or SS1 by the Extended/Advanced Functions. Otherwise the correct control by the onboard terminals cannot be checked.

##### Test stop for Extended/Advanced Functions

> **Note**
>
> If the "Basic Functions via onboard terminals" option is active for the Extended Functions, you must make the test stop settings for the Basic Functions as well as for the Extended Functions.

1. Click the "Execute test stop automatically during ramp-up" button to activate the automatic test stop during ramp-up. The automatic test stop during ramp-up is active when the button shows a closed switch.

   - Or -

   If the test stop should not be performed automatically with the ramp-up, select the signal ([p9705](SINAMICS%20Parameter%20SERVO.md#p9705-bi-si-motion-test-stop-signal-source)) that is to trigger the forced checking procedure. Make sure that the connection for "Execute test stop automatically during ramp-up" is interrupted.
2. Under "Extended Functions - Test stop selection" (p9705), select the signal source for the test stop of the safe motion monitoring.
3. Enter the interval for performing the forced checking procedure and testing the Safety shutdown paths in the "Timer test stop" ([p9559](SINAMICS%20Parameter%20SERVO.md#p9559-si-motion-forced-checking-procedure-timer-control-unit)) field.

   The "STO" function must be selected and deselected at least once within the configured time. The monitoring time is reset at every STO deselection.
4. Interconnect the "Test stop required" ([r9723](SINAMICS%20Parameter%20SERVO.md#r9723017-cobo-si-motion-diagnostic-signals-integrated-in-the-drive-1).0) signal sink to a digital output or to a bit in the status word of the fieldbus.

**For S120 with CU310-2 and AC Power Module**

| Symbol | Meaning |
| --- | --- |
| 1. Click the "Execute test stop automatically during ramp-up" button to activate the automatic test stop during ramp-up. The automatic test stop during ramp-up is active when the button shows a closed switch.     - Or -     If the test stop should not be performed automatically with the ramp-up, select the signal (p9705) that is to trigger the forced checking procedure. Make sure that the connection for "Execute test stop automatically during ramp-up" is interrupted. 2. Under "Extended Functions - Test stop selection" (p9705), select the signal source for the test stop of the safe motion monitoring. 3. Enter the interval for performing the forced checking procedure and testing the Safety shutdown paths in the "Timer test stop" (p9559) field.    The "STO" function must be selected and deselected at least once within the configured time. The monitoring time is reset at every STO deselection. 4. Interconnect the "Test stop required" (r9723.0) signal sink to a digital output or to a bit in the status word of the fieldbus. 5. In "Test stop selection for F-DO" ([p10007](SINAMICS%20Parameter%20SERVO.md#p10007-bi-si-motion-forced-checking-procedure-f-do-signal-source)), select the signal source for the start of the test stop for the F-DO. 6. Enter the interval for performing the forced checking procedure and testing the F-DO in the "Timer test stop" ([p10003](SINAMICS%20Parameter%20SERVO.md#p10003-si-motion-forced-checking-procedure-timer)) field. After this interval has elapsed, the alarm A01774 informs you that a test stop needs to be performed for the F‑DI/F‑DO.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Risk of death due to unintended movement with improper use of the feedback DI of the F-DO** The test sequence can cause unwanted movements of the drive if the DI of the F‑DO is used not only for feedback on the test stop/forced checking procedure, but also for other purposes. - Use the DI of the F-DO only for feedback on test stop (forced checking procedure) and not for other purposes. |  | |  |

##### Status display

The following elements show the current status of the forced checking procedure:

- Remaining time:

  Shows the time remaining until the forced checking procedure and the test of the Safety shutdown paths are performed ([r9660](SINAMICS%20Parameter%20SERVO.md#r9660-si-forced-checking-procedure-remaining-time) for the Basic Functions, [r9765](SINAMICS%20Parameter%20SERVO.md#r9765-si-motion-forced-check-procedure-remaining-time-control-unit) for the Extended Functions).
- Test stop required:

  Shows that a test stop must be performed on the drive. Evaluate alarm A01699 in your higher-level controller, for example, by interconnecting r9773.31 or r9723.0 to a digital output or a bit in the fieldbus status word (r9773.31 for the Basic Functions, r9723.0 for the Extended Functions).

##### Function diagrams (FD)

SI Basic Functions - SI status CU, MM, CU + MM, group STO - 2804 -

SI Basic Functions - S_STW1/2 safety control word 1/2, S_ZSW1/2 safety status word 1/2 - 2806 -

SI Basic Functions - STO (Safe Torque Off), SS1 (Safe Stop 1) - 2810 -

##### Additional parameters

- p9559
- p9659
- r9660
- p9705
- r9723
- r9765
- [r9772](SINAMICS%20Parameter%20SERVO.md#r9772023-cobo-si-status-control-unit)
- r9773

---

#### Function status

##### Status messages

The "Function status" screen form shows an overview of the status messages of the parameterized Safety Integrated Functions on the left-hand side ("active" or "not active").

Depending on the function, you see additional information; e.g. for SLS, the "Active level", the "Active SLS limit" and the "Actual speed value" are displayed.

The status information is displayed on the right-hand side of the screen form for:

- "Test stop required" ([r9743](SINAMICS%20Parameter%20SERVO.md#r9743415-cobo-si-safety-information-channel-status-word-s_zsw2b).13)

  Shows that a test of the shutdown paths (test stop) is required (see [Test stop](#test-stop)).

  - "Timer test stop" ([p9659](SINAMICS%20Parameter%20SERVO.md#p9659-si-forced-checking-procedure-timer)): Time interval for performing the forced checking procedure and testing the Safety shutdown paths. Within the parameterized time, the STO must be deselected at least once. The monitoring time is reset at every STO deselection.
  - "Remaining time" ([r9660](SINAMICS%20Parameter%20SERVO.md#r9660-si-forced-checking-procedure-remaining-time) for the Basic Functions, [r9765](SINAMICS%20Parameter%20SERVO.md#r9765-si-motion-forced-check-procedure-remaining-time-control-unit) for the Extended Functions) shows the remaining time until the test of the Safety shutdown paths.
- Internal event ([r9722](SINAMICS%20Parameter%20SERVO.md#r9722031-cobo-si-motion-drive-integrated-status-signals-control-unit-4).7)

  Set when the first Safety message occurs.

##### Additional parameters

- [p9559](SINAMICS%20Parameter%20SERVO.md#p9559-si-motion-forced-checking-procedure-timer-control-unit)
- p9659
- [r9781](SINAMICS%20Parameter%20CU.md#r978101-si-checksum-to-check-changes-control-unit)[0]
- [r9782](SINAMICS%20Parameter%20CU.md#r978201-si-time-stamps-to-check-changes-control-unit)[0]
- r9722.7
- [r9723](SINAMICS%20Parameter%20SERVO.md#r9723017-cobo-si-motion-diagnostic-signals-integrated-in-the-drive-1).2

---

#### Acceptance mode

##### Description

The acceptance mode can be activated ([p9570](SINAMICS%20Parameter%20SERVO.md#p9570-si-motion-acceptance-test-mode-control-unit)) for a parameterized time ([p9558](SINAMICS%20Parameter%20SERVO.md#p9558-si-motion-acceptance-test-mode-time-limit-control-unit-1)), and allows intentional limit violations during the acceptance test. For instance, the setpoint velocity limits are no longer active in acceptance mode. To ensure that this state is not accidentally retained, the acceptance mode is automatically exited after the time set in p9558.

It is only worth activating acceptance mode during the acceptance test of the SS2, SOS, SDI, SLS and SLP functions. It has no effect on other functions.

Normally, SOS can be selected directly or via SS2. To enable triggering of a violation of the SOS standstill limits while acceptance mode is active (also in the "SS2 active" state), the setpoint is enabled again by the acceptance mode after deceleration and transition to SOS, to allow the motor to move. When an SOS violation is acknowledged in active acceptance mode, the current position is adopted as the new standstill position so that an SOS violation is not immediately detected again.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis movement upon activation of the acceptance test**  If a speed setpoint ≠ 0 is present, the active stop function SS2 is set, and the motor is at a standstill (active SOS), the axis starts to move as soon as the acceptance test is activated. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that nobody is in the danger zone during the acceptance test. |  |

##### Activating acceptance mode

1. Correct the specified maximum time for the acceptance mode in the "Acceptance test time limit" (p9558) field.

   If the acceptance mode lasts longer than the set time limit, the mode is exited automatically.
2. Perform a POWER ON to activate the parameters.

   The "Activate acceptance mode" button is then activated.
3. To activate acceptance mode, click the "Activate acceptance mode" button (p9570).

   For activated acceptance mode, you can switch off manually via the "Deactivate acceptance mode" button.

##### Additional parameters

- p9558
- p9570

---

### Technology functions

This section contains information on the following topics:

- [Technology Extensions](#technology-extensions)
- [Basic positioner](#basic-positioner)
- [Position control](#position-control)
- [Active oscillation damping (APC)](#active-oscillation-damping-apc)
- [Extended torque control](#extended-torque-control)
- [Technology controller](#technology-controller)

#### Technology Extensions

This section contains information on the following topics:

- [Adding and activating Technology Extensions](#adding-and-activating-technology-extensions)

##### Adding and activating Technology Extensions

###### "Technology Extensions that can be activated for this drive object" view - Current drive object

This tabular overview shows all installed Technology Extensions that are compatible with the drive object currently selected via the project tree for parameterization.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Usage | Click the "Usage" button to change to the "Current drive object" view of the associated drive object. |
| Selection | Click the "Selection" option to activate or deactivate the Technology Extension for the current Startdrive project. |
| Version | The version of the Technology Extension is displayed here. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

###### "Technology Extensions that cannot be activated" view - Current drive object

The "Technology Extensions that cannot be activated" overview is visible only if you select the "Current drive object" option in the drop-down list just to the right of the "Add further Technology Extensions..." button.

This tabular overview shows all installed Technology Extensions that are incompatible with the drive object currently selected via the project tree for parameterization.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Reason | The reason why the Technology Extension is not compatible with the current drive object is displayed here. Click the button to obtain more information about why the Technology Extension is not compatible with the drive object. |
| Version | The version of the Technology Extension is displayed here. |
| Required FW version | The minimum SINAMICS firmware version required to use the Technology Extension is displayed here. |
| Existing FW version | The SINAMICS firmware version of the current drive object is displayed here. |
| Uninstall | Click the "Remove" button to uninstall the Technology Extension. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

###### "Technology Extensions that can be activated for this drive unit" view - All drive objects

This tabular overview shows all of the installed Technology Extensions which you have added for the currently selected drive.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Usage | Click the "Usage" button to change to the "Current drive object" view of the associated drive object. |
| Selection | Click the "Selection" option to activate or deactivate the Technology Extension for the current Startdrive project. |
| Version | The version of the Technology Extension is displayed here. |
| Parameter number range | The parameters that are relevant for the Technology Extension are displayed here. |
| Uninstall | Click the "Remove" button to uninstall the Technology Extension. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

###### Requirements

- A project has been created, or an existing project is open.
- The device configuration contains one of the following SINAMICS drives:

  - SINAMICS S120 (as of firmware version 5.2)
  - SINAMICS MV (as of firmware version 5.2.1)

###### Changing views

To switch to the display of the "Technology Extensions" function view, proceed as follows:

1. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the option "Current drive object".  
   The "Technology Extensions" function view now contains two overview tables:

   - "Technology Extensions that can be activated for this drive object"
   - "Technology Extensions that cannot be activated"
2. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select "All drive objects".  
   The "Technology Extensions" function view now contains only the overview table "Technology Extensions that can be activated for this drive object".

###### Adding Technology Extensions

Proceed as follows to add a Technology Extension to your Startdrive project:

1. Click the "Add further Technology Extension..." button.  
   A dialog opens.
2. In the file system of your PC, select the desired Technology Extension file (file extension *.tec) and click "Open".  
   The Technology Extension is added to your Startdrive installation.  
   Depending on the currently selected view and the compatibility with the current drive object, the Technology Extension is displayed in one of the tabular overviews.

**Note**

When you add a Technology Extension, it is available to you in your current Startdrive installation across all projects.

###### Activating Technology Extensions

To activate a Technology Extension, proceed as follows:

1. Add a Technology Extension to your project as described in the section "Adding Technology Extensions".
2. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the required "Technology Extensions" function view from the drop-down.
3. Activate the option "Selection" in the corresponding row of the desired drive object located in the column of the tabular overview with the same name.

###### Deactivating Technology Extensions

To deactivate a Technology Extension, proceed as follows:

1. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the required "Technology Extensions" function view from the drop-down.
2. Deactivate the option "Selection" in the corresponding row of the desired drive object located in the column of the tabular overview with the same name.

###### Uninstalling Technology Extensions

You can uninstall Technology Extensions globally via the "All drive objects" view or in the "Technology Extensions that cannot be activated" overview of the respective drive object.

Proceed as follows to remove a Technology Extension from your Startdrive project:

1. Open the "All drive objects" view or the "Technology Extensions that cannot be activated" overview of the desired drive object.
2. Click the "Remove" button in the row of the drive object concerned in the "Uninstall" column.

   The "Remove Technology Extension" dialog opens.
3. Click "Yes" to confirm the uninstallation of the Technology Extension.
4. If the Technology Extension is still activated on drive objects in the project, the "Remove Technology Extension" dialog opens again.  
   All drive objects on which the Technology Extension is still activated are listed.  
   Click "Yes" to uninstall the Technology Extension.

###### Additional information

You can find additional information on the Technology Extensions in the SIOS portal on the Internet.

---

**See also**

[SIOS portal](https://support.industry.siemens.com/cs/ww/en/view/109771648)

#### Basic positioner

This section contains information on the following topics:

- [Overview](#overview-5)
- [EPOS - diagnostics](#epos---diagnostics)
- [Limitation (servo)](#limitation-servo)
- [Jog (servo)](#jog-servo)
- [Homing (servo)](#homing-servo)
- [Traversing blocks (servo)](#traversing-blocks-servo)
- [Direct setpoint specification (MDI) (servo)](#direct-setpoint-specification-mdi-servo)

##### Overview

###### Description

"Position control" means controlling the position of an axis. An "axis" is a machine or system component that comprises the converter with active position control and the driven mechanical system.

The basic positioner (EPOS) calculates the traversing profile for the time-optimized traversing of the axis to the target position.

![Overview: Basic positioner and position control](images/147858894987_DV_resource.Stream@PNG-en-US.png)

Overview: Basic positioner and position control

Extensive positioning tasks can be performed in the SINAMICS S120 without a higher-level controller with the basic positioner (EPOS):

- The actual basic positioner calculates the traversing profile for the time-optimized behavior.
- Subordinate [position control](#overview-6) means controlling the position of an axis.

> **Note**
>
> The basic positioner requires the functions of the position controller. The BICO interconnections that are made automatically by the basic positioner must only be changed by experts.

###### Requirements

- The "Basic positioner" function module is activated (see [Function modules (servo)](#function-modules-servo)).

  With this function module, the "Position control" function module is also automatically activated.
- Startdrive is in online mode.
- The drive control panel is called and the master control is activated.

###### Positioning options of the EPOS

EPOS offers the following positioning options:

- Positioning of linear axes

  A linear axis is an axis whose traversing range is limited in both motor directions of rotation by the mechanical system of the machine.
- Positioning of rotary/modulo axes

  A modulo axis is an axis with an infinite traversing range.
- Absolute positioning

  The converter interprets the position setpoint as an absolute set position relative to the machine zero/home position.
- Relative positioning

  The converter interprets the position setpoint as an absolute set position relative to the current starting position.

###### Operating modes of the EPOS

EPOS can be operated with the following operating modes:

- [Jog](#jog-servo)

  The "Jog" function incrementally traverses the axis (e.g. for setting up).
- [Homing](#homing-servo)

  Homing establishes the reference of the position measurement in the converter to the machine.
- [Traversing block](#traversing-blocks-servo) selection

  Position setpoints are saved in different traversing blocks in the converter. The external controller only selects a saved traversing block. All further operations are performed by the converter independently.
- [Direct setpoint specification (MDI)](#direct-setpoint-specification-mdi-servo)

  The external controller specifies the position setpoint together with the traversing profile for the axis. Saving is not performed in the converter. New target values must be specified by the controller for each new movement.
- [Travel to fixed stop](#programming-traversing-blocks)

  The drive positions the axis with a specified torque against a mechanical fixed stop, e.g. in order to press/clamp an object.

###### Length unit LU

The length unit "LU" is generally used in the basic positioner and position control screen forms.

The length unit "LU" is the shortest length with neutral unit that can be processed by the drive system. Calculation is performed internally in the drive with the length units (e.g. mm, inch or degrees).

##### EPOS - diagnostics

The EPOS diagnostics contain an overview of the most important data of the subordinate EPOS screen forms. The following blocks show the most important information:

- Operating mode
- Status
- Enables
- Setpoints and actual values

###### Further information

| Symbol | Meaning |
| --- | --- |
| ![Further information](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) | [Jog](#jog-servo) mode |
| ![Further information](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) | [Homing](#homing-servo) mode |
| ![Further information](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) | [Traversing block](#traversing-blocks-servo) mode |
| ![Further information](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) | [Direct setpoint specification](#direct-setpoint-specification-mdi-servo) mode |
| ![Further information](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) | [Missing enables](#missing-enables) |

##### Limitation (servo)

This section contains information on the following topics:

- [Traversing range limitation](#traversing-range-limitation)
- [Traversing profile limitation](#traversing-profile-limitation)

###### Traversing range limitation

###### Description

The dynamic limitations, the limits for the software limit switches and the STOP cams for the Basic Positioner function module, are parameterized in the "Traversing range limitation" screen form. The traversing range can be limited using both software and hardware.

![Example: Traversing range limitation](images/147858950539_DV_resource.Stream@PNG-en-US.png)

Example: Traversing range limitation

###### Setting the software limit switches

1. Interconnect the signal source for activating the software limit switch in the "Software limit switch activation" ([p2582](SINAMICS%20Parameter%20SERVO.md#p2582-bi-epos-software-limit-switch-activation)) (static or dynamic) field.

   The software limit switch is defined, for example, by a traversing range limit. The software limit switch is active only when homing has been performed and the modulo correction is not active.
2. Interconnect the signal source for activation of the modulo source in the "Modulo correction activation" ([p2577](SINAMICS%20Parameter%20SERVO.md#p2577-bi-epos-modulo-correction-activation)) field.

   The modulo correction is only required for rotary axes.
3. Enter a negative ([p2580](SINAMICS%20Parameter%20SERVO.md#p2580-co-epos-software-limit-switch-minus)) and a positive end position ([p2581](SINAMICS%20Parameter%20SERVO.md#p2581-co-epos-software-limit-switch-plus)).
4. Interconnect the following signal sources:

   - For the software limit switch minus in the "Negative end position" ([p2578](SINAMICS%20Parameter%20SERVO.md#p2578-ci-epos-software-limit-switch-minus-signal-source)) field.
   - For the software limit switch plus in the "Positive end position" ([p2579](SINAMICS%20Parameter%20SERVO.md#p2579-ci-epos-software-limit-switch-plus-signal-source)) field.

###### Setting the hardware limit switches (stop cams)

1. Interconnect the signal source for activation of the STOP cam in the "Hardware limit switch activation" ([p2568](SINAMICS%20Parameter%20SERVO.md#p2568-bi-epos-stop-cam-activation)) field.

   The STOP cam is specified by a signal from the hardware that you must parameterize, e.g. using a BERO signal.
2. Interconnect the signal source for the STOP cam in the positive travel direction in the "Hardware limit switch plus" ([p2570](SINAMICS%20Parameter%20SERVO.md#p2570-bi-epos-stop-cam-plus)) field.
3. Interconnect the signal source for the STOP cam in the negative travel direction in the "Hardware limit switch minus" ([p2569](SINAMICS%20Parameter%20SERVO.md#p2569-bi-epos-stop-cam-minus)) field.

   When a STOP cam is detected, a stop is performed with the maximum deceleration. When a STOP cam is reached, only movements away from the STOP cam are permitted.

###### Function diagrams (FD)

- EPOS - Traversing range limits (r0108.4 = 1) - 3630 -

###### Additional parameters

---

###### Traversing profile limitation

###### Description

You can specify the limitations of the traversing profile for the basic positioner in the "Traversing profile limitation" screen form. The drive calculates the traversing profile when positioning from specified values for velocity, acceleration and jerk (= acceleration change with respect to time). If the axis must traverse more slowly or must accelerate at a lower rate or "softly", then you must set the relevant limits to lower values. The lower a limit is, the longer the drive requires to position the axis.

![Example: Jerk limitation](images/147858973451_DV_resource.Stream@PNG-en-US.png)

Example: Jerk limitation

###### Specifying the maximum traversing profile limitation

1. Correct the specified value in LU for the maximum velocity in the "Max. velocity" field ([p2571](SINAMICS%20Parameter%20SERVO.md#p2571-epos-maximum-velocity)).

   The maximum velocity defines the maximum travel velocity [1000 LU/min]. A change immediately limits the velocity of a running traversing block.

   The "Corresponds to speed" field displays the converted speed, the "Max. speed" field the maximum speed.

   The limitation acts during positioning (jogging, processing of the traversing blocks, direct setpoint specification, homing procedure).
2. Correct the specified value in LU for the acceleration at "Max. acceleration" ([p2572](SINAMICS%20Parameter%20SERVO.md#p2572-epos-maximum-acceleration)).

   The "Corresponds to acceleration time" field displays the converted acceleration time.
3. Correct the specified value in LU for the deceleration at "Max. deceleration" ([p2573](SINAMICS%20Parameter%20SERVO.md#p2573-epos-maximum-deceleration)).

   The "Corresponds to deceleration time" field displays the converted deceleration time.

   The maximum acceleration/deceleration specify the maximum acceleration for increasing the velocity and the maximum deceleration for reducing the velocity. Both values act during positioning (jogging, processing of the traversing blocks, direct setpoint specification, homing procedure).

###### Specifying the traversing profile limitation in relation to the maximum speed

The velocity, acceleration and deceleration limitation values do not apply for errors or for a safe stop. Instead, the ramp-down times for OFF1 and OFF3 are used. The proposed delay time is displayed in the "Delay time in relation to the max. speed" field.

1. If you want to apply this delay time to OFF1, click the "Accept values" button.

   The delay time is now applied to the "OFF1 ramp-down time" ([p1121](SINAMICS%20Parameter%20SERVO.md#p11210n-ramp-function-generator-ramp-down-time-2)) field.
2. Enter the desired value in s manually in the "Ramp-down time (OFF3)" ([p1135](SINAMICS%20Parameter%20SERVO.md#p11350n-off3-ramp-down-time-1)) field.

###### Specifying the maximum jerk limitation

A jerk limitation delays the acceleration. You can set it as follows.

1. Interconnect the signal source for activation of the EPOS jerk limitation with value 1 in the "Jerk limitation activation" ([p2575](SINAMICS%20Parameter%20SERVO.md#p2575-bi-epos-jerk-limiting-activation)) field.
2. Enter a value in LU for the maximum jerk limitation at "Jerk limitation" ([p2574](SINAMICS%20Parameter%20SERVO.md#p2574-epos-jerk-limiting)).

   The converted values for the minimum acceleration time and minimum deceleration time are displayed in the fields below the graphic.

###### Function diagrams (FD)

- EPOS - Traversing range limits (r0108.4 = 1) - 3630 -

###### Additional parameters

---

##### Jog (servo)

This section contains information on the following topics:

- [Configuring jog](#configuring-jog)
- [Configuring the jog setpoints](#configuring-the-jog-setpoints)

###### Configuring jog

###### Description

Jog is the simplest position-controlled traversing option. For example, you can use "EPOS jogincremental"to traverse the drive either with endless traversing (jog) or over a parameterizable distance. In jogging, acceleration or deceleration is with the parameterized maximum acceleration or maximum deceleration.

**Editing mode**

The editing mode of the "Jog" screen form can be set via a drop-down list. The following selections are available:

- Standard

  Limited configuration scope
- Expert

  Complete configurability

###### Configuring EPOS jog in expert mode

1. Select the "Expert" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the signal sources for the binector and connector inputs on the left in the screen form, beginning with "Jog 1" ([p2589](SINAMICS%20Parameter%20SERVO.md#p2589-bi-epos-jog-1-signal-source)).
3. If required, correct the jog setpoints (see [Configuring the jog setpoints](#configuring-the-jog-setpoints)).
4. Interconnect the signal sinks for the binector and connector outputs on the right side in the screen form, beginning with "Traversal command active" ([r2684](SINAMICS%20Parameter%20SERVO.md#r2684015-cobo-epos-status-word-2).15).

> **Note**
>
> Step 3 can also be performed in standard mode.

###### Function diagrams (FD)

FD_3610 (55)

###### Additional parameters

---

###### Configuring the jog setpoints

###### Description

The following parameters can be set for the EPOS jog:

- Velocity setpoint (either for jog 1 or 2)
- Traversing distances (either for jog 1 or 2)
- Maximum acceleration
- Maximum deceleration

###### Setting the jog setpoints

1. Click the "Configure jog setpoints" button in the "Jog" screen form or click on the entry with the same name in the secondary navigation.

   The "Configure jog setpoints" screen form is displayed.
2. Enter the velocity setpoint for jog 1 in the "Velocity setpoint 1" ([p2585](SINAMICS%20Parameter%20SERVO.md#p2585-epos-jog-1-setpoint-velocity)) field.

   - Or -

   Enter the velocity setpoint for jog 2 in the "Velocity setpoint 2" ([p2586](SINAMICS%20Parameter%20SERVO.md#p2586-epos-jog-2-setpoint-velocity)) field.
3. Enter the traversing distance for incremental jog 1 in the "Traversing distance 1" ([p2587](SINAMICS%20Parameter%20SERVO.md#p2587-epos-jog-1-traversing-distance)) field.

   - Or -

   Enter the traversing distance for incremental jog 2 in the "Traversing distance 2" ([p2588](SINAMICS%20Parameter%20SERVO.md#p2588-epos-jog-2-traversing-distance)) field.

###### Function diagrams (FD)

FD_3610 (55)

###### Additional parameters

---

---

**See also**

[Configuring jog](#configuring-jog)

##### Homing (servo)

This section contains information on the following topics:

- [Basic settings](#basic-settings-1)
- [Active homing](#active-homing)
- [Passive homing](#passive-homing)
- [Absolute encoder adjustment](#absolute-encoder-adjustment)

###### Basic settings

###### Description

After switching on the machine, the absolute dimensional reference for the machine zero must be established for positioning. This procedure is called "Homing". The following homing types are possible:

- Set home position

  The current actual position of the drive is used as the home position. The following positioning jobs are then always performed based on this home position.
- Homing procedure (active homing - incremental)

  With an incremental measuring system, the drive can be traversed to a home position through a homing procedure without a higher-level controller. The drive itself controls and monitors the homing cycle.
- Absolute encoder adjustment (absolute homing)

  Absolute encoders have to be adjusted during commissioning. When the machine is switched off, the position information of the encoder is retained. The absolute encoder is therefore first adjusted to the home position, e.g. by jogging.
- Flying homing (passive homing)

  With flying homing, the homing overlays a traversing task. In this case, the traversing task of the associated mode will be performed and also the evaluation of the measuring input activated. With the recognition of the measuring input, the difference of the home position coordinate and the determined measured value will be corrected on-the-fly (during motion) taking account of the window limits, and the traversing task completed.

**Editing mode**

The editing mode of the "Homing" screen form can be set from a drop-down list. The following selections are available:

- Standard

  Limited configuration scope
- Expert

  Complete configurability

###### Configuring homing in expert mode

1. Select the "Expert" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the signal sources for the binector and connector inputs on the left in the screen form, beginning with "Set home position" ([p2596](SINAMICS%20Parameter%20SERVO.md#p2596-bi-epos-set-reference-point)).
3. Interconnect the signal sinks for the binector outputs (multiple connections are possible) on the left in the screen form, beginning with "Traversal command active" ([r2684](SINAMICS%20Parameter%20SERVO.md#r2684015-cobo-epos-status-word-2).15).
4. Configure one of the following homing types:

   - Active homing (see [Active homing](#active-homing))
   - Passive homing (see [Passive homing](#passive-homing))
5. If you need a "Home position coordinate" for your homing type, specify a corresponding value using the absolute encoder adjustment (see "[Absolute encoder adjustment](#absolute-encoder-adjustment)").

> **Note**
>
> Step 4 can also be performed for servo drive units in standard mode. This is not possible for vector drive units.

###### Function diagrams (FD)

EPOS - Referencing / reference point approach mode (r0108.4 = 1) (p2597 = 0-signal) - 3612 -

EPOS - Flying referencing mode (r0108.4 = 1) (p2597 = 1 signal) - 3614 -

###### Additional parameters

---

###### Active homing

For active homing, the drive with an incremental measuring system can be traversed to a home position by a homing procedure without a higher-level controller. The drive itself controls and monitors the homing cycle.

###### Displaying the "Active homing" screen form

Open the "Active homing" screen form using the secondary navigation or by clicking the "Active" button in the "Homing" screen form.

> **Note**
>
> Active homing can only be configured in the expert mode for VECTOR drives.

###### Selecting homing mode

1. Open the "Active homing" screen form using the secondary navigation or by clicking the "Active" button in the "Homing" screen form.
2. Activate the desired homing mode as an option in the "Select homing mode" field.

   - Encoder zero mark and homing cam
   - Encoder zero mark
   - External zero mark via digital input

###### Configuring "Encoder zero mark and homing cam" homing mode

1. Interconnect the "Negative start direction of the homing procedure" ([p2604](SINAMICS%20Parameter%20SERVO.md#p2604-bi-epos-search-for-reference-start-direction)) for the start direction of the homing procedure.
2. Enter in the "To the zero mark" ([p2608](SINAMICS%20Parameter%20SERVO.md#p2608-epos-search-for-reference-approach-velocity-zero-mark)) field, the approach velocity after detection of the homing cam when searching for the zero mark during the homing procedure.
3. Enter in the "To the homing cam" ([p2605](SINAMICS%20Parameter%20SERVO.md#p2605-epos-search-for-reference-approach-velocity-reference-cam)) field, the approach velocity to the homing cam during the homing procedure.
4. Enter in the "Home position offset" ([p2600](SINAMICS%20Parameter%20SERVO.md#p2600-epos-search-for-reference-reference-point-offset)) field, the desired home position offset during the homing procedure.
5. Enter in the "Home position coordinate" ([p2599](SINAMICS%20Parameter%20SERVO.md#p2599-co-epos-reference-point-coordinate-value)) field, the position value of the home position coordinate.

###### Configuring "Encoder zero mark" homing mode

Once you have activated homing mode, set the approach direction and the approach velocity:

1. Interconnect the "Negative start direction of the homing procedure" (p2604) for the start direction of the homing procedure.
2. Enter in the "To the zero mark" (p2608) field, the approach velocity after detection of the homing cam when searching for the zero mark during the homing procedure.
3. Enter in the "Home position offset" (p2600) field, the desired home position offset during the homing procedure.
4. Enter in the "Home position coordinate" (p2599) field, the position value of the home position coordinate.

###### Configuring "External zero mark via digital input" homing mode

1. Select in the "Digital input of the external zero mark" ([p0494](SINAMICS%20Parameter%20SERVO.md#p04940n-equivalent-zero-mark-input-terminal-1)) drop-down list, the input terminal for connecting a zero mark replacement.

   To prevent incorrect measuring values, this parameter may not be written during an active measurement.
2. Interconnect the "Negative start direction of the homing procedure" (p2604) for the start direction of the homing procedure.
3. Enter in the "To the zero mark" (p2608) field, the approach velocity after detection of the homing cam when searching for the zero mark during the homing procedure.
4. Enter in the "Home position offset" (p2600) field, the desired home position offset during the homing procedure.
5. Enter in the "Home position coordinate" (p2599) field, the position value of the home position coordinate.

###### Additional parameters

---

###### Passive homing

###### Description

With passive (flying) homing, the homing overlays a traversing task. In this case, the traversing task of the associated mode will be performed and also the evaluation of the measuring input activated. With the recognition of the measuring input, the difference of the home position coordinate and the determined measured value will be corrected on-the-fly (during motion) taking account of the window limits, and the traversing task completed.

**Editing mode**

The editing mode of the "Passive homing" screen form can be set from a drop-down list. The following selections are available:

- Standard
- Expert

###### Display the "Passive homing" screen form

Open the "Passive homing" screen form using the secondary navigation or by clicking the "Passive" button in the "Homing" screen form.

> **Note**
>
> Passive homing can only be configured in the expert mode for VECTOR drives.

###### Configuring passive homing in expert mode

1. Select the "Expert" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the "Edge evaluation of the measuring input 1 and 2" ([p2511](SINAMICS%20Parameter%20SERVO.md#p251103-bi-lr-measuring-probe-evaluation-edge)[0]) signal source for the edge evaluation of the measuring input.
3. Interconnect the "Select the measuring inputs" ([p2510](SINAMICS%20Parameter%20SERVO.md#p251003-bi-lr-selecting-measuring-probe-evaluation)[0]) signal source for selecting the measuring input.
4. Select in the "Digital input of measuring input 1 for the zero mark" ([p2517](SINAMICS%20Parameter%20SERVO.md#p251702-lr-direct-measuring-probe-1-1)) drop-down list, the input terminal for the direct measuring input 1.

   The direct measuring input can be parameterized as non-cyclic (value = 1 ... 8) or cyclic (value = 11 ... 18) measuring input.
5. Select in the "Digital input of measuring input 2 for the zero mark" ([p2518](SINAMICS%20Parameter%20SERVO.md#p251802-lr-direct-measuring-probe-2-1)) drop-down list, the input terminal for the direct measuring input 2.

   The direct measuring input can be parameterized as non-cyclic (value = 1 ... 8) or cyclic (value = 11 ... 18) measuring input.
6. Enter in the "Home position coordinate" ([p2599](SINAMICS%20Parameter%20SERVO.md#p2599-co-epos-reference-point-coordinate-value)) field, the position value of the home position coordinate.
7. Click the "Correction window" button.

   A dialog with the same name opens.
8. Enter in the "Inner window" ([p2601](SINAMICS%20Parameter%20SERVO.md#p2601-epos-flying-referencing-inner-window)) field, the size of the inner window during flying homing.

   The inner window must be set smaller than the outer window.
9. Enter in the "Outer window" ([p2602](SINAMICS%20Parameter%20SERVO.md#p2602-epos-flying-referencing-outer-window)) field, the size of the outer window during flying homing.
10. Once all necessary settings have been made, click "Close".

    The dialog closes.

###### Configuring passive homing in standard mode

1. Select the "Standard" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the "Edge evaluation of the measuring input 1 and 2" (p2511[0]) signal source for the edge evaluation of the measuring input.
3. Select in the "Digital input of the measuring input for the zero mark" (p2517) drop-down list, the input terminal for the direct measuring input.

   The direct measuring input can be parameterized as non-cyclic (value = 1 ... 8) or cyclic (value = 11 ... 18) measuring input.
4. Enter in the "Home position coordinate" (p2599) field, the position value of the home position coordinate.

###### Additional parameters

---

###### Absolute encoder adjustment

###### Display the "Absolute encoder adjustment" screen form

Open the "Absolute encoder adjustment" screen form using the secondary navigation or the "Adjustment" button in the "Homing" screen form.

###### Precondition

- Startdrive is in online mode.

###### Parameterizing the home position coordinate

**Set**

1. Correct the home position value in LU in the "Home position coordinate" field.
2. Click the "Set" button.

   Next, the status display for the absolute value adjustment is updated (p2507[0]). With correct adjustment, the "Absolute encoder adjusted" entry is displayed.

**Reset (and correct)**

1. Click the "Reset" button.

   Next, the status display for the absolute value adjustment is updated (p2507[0]). The adjustment is deactivated.
2. Correct the home position value in the "Home position coordinate" field and click "Set".

##### Traversing blocks (servo)

This section contains information on the following topics:

- [Basic settings](#basic-settings-2)
- [Selecting traversing blocks](#selecting-traversing-blocks)
- [Parameterizing the external block change](#parameterizing-the-external-block-change)
- [Programming traversing blocks](#programming-traversing-blocks)

###### Basic settings

###### Description

Up to 64 different traversing tasks can be stored. All parameters that describe a traversing task take effect at a block change when the following conditions are present:

- The corresponding traversing block number is selected in binary code by the binector inputs [p2625](SINAMICS%20Parameter%20SERVO.md#p2625-bi-epos-traversing-block-selection-bit-0) to [p2630](SINAMICS%20Parameter%20SERVO.md#p2630-bi-epos-traversing-block-selection-bit-5) (block selection bit 0...5) and started with the signal on the binector input [p2631](SINAMICS%20Parameter%20SERVO.md#p2631-bi-epos-activate-traversing-task-0---1) (BI: activate EPOS traversing task).
- This results in a block change in a number of traversing blocks.
- An external block change [p2632](SINAMICS%20Parameter%20SERVO.md#p2632-epos-external-block-change-evaluation) "External block change" is triggered.

**Editing mode**

The following editing modes are available for the parameter assignment of the traversing blocks:

- Standard

  Limited configuration scope
- Expert

  Complete configurability

###### Configuring traversing blocks in expert mode

1. Select the "Expert" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the signal sources for the binector and connector inputs on the left in the screen form, beginning with "Activate traversing job" (p2631).
3. Interconnect the signal sinks for the binector outputs (multiple connections are possible) on the left in the screen form, beginning with "Traversal command active" ([r2684](SINAMICS%20Parameter%20SERVO.md#r2684015-cobo-epos-status-word-2).15).
4. Specify the block change via external signals in the "[External block change](#parameterizing-the-external-block-change)" dialog.
5. Interconnect the signals for the individual traversing blocks in the "[Traversing block selection](#selecting-traversing-blocks)" dialog.
6. Specify a maximum of 64 traversing blocks (one table for each traversing block) in the "[Programming traversing blocks](#programming-traversing-blocks)" dialog.

> **Note**
>
> Steps 4 to 6 can also be performed in standard mode.

###### Function diagrams (FD)

EPOS - Traversing blocks mode (r0108.4 = 1) - 3616 -

###### Additional parameters

---

###### Selecting traversing blocks

Connect the signal sources of the traversing blocks via the "Traversing block selection" dialog. You can call the dialog via the "Traversing blocks" mask.

###### Connecting signal sources of the traversing blocks

1. Click the "Select traversing block" button in the "Traversing blocks" mask.

   The "Traversing block selection" dialog opens.
2. Connect the signal sources for the selection of the respective traversing block bits.

   - "Bit 0" ([p2625](SINAMICS%20Parameter%20SERVO.md#p2625-bi-epos-traversing-block-selection-bit-0))
   - "Bit 1" ([p2626](SINAMICS%20Parameter%20SERVO.md#p2626-bi-epos-traversing-block-selection-bit-1))
   - "Bit 2" ([p2627](SINAMICS%20Parameter%20SERVO.md#p2627-bi-epos-traversing-block-selection-bit-2))
   - "Bit 3" ([p2628](SINAMICS%20Parameter%20SERVO.md#p2628-bi-epos-traversing-block-selection-bit-3))
   - "Bit 4" ([p2629](SINAMICS%20Parameter%20SERVO.md#p2629-bi-epos-traversing-block-selection-bit-4))
   - "Bit 5" ([p2630](SINAMICS%20Parameter%20SERVO.md#p2630-bi-epos-traversing-block-selection-bit-5))
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Additional parameters

---

###### Parameterizing the external block change

Configure the parameters for the external block change in the "External block change" dialog. Fundamentally there are two block change variants:

- External block change via measuring input
- External block change via BI: [p2633](SINAMICS%20Parameter%20SERVO.md#p2633-bi-epos-external-block-change-0---1)

You can activate the desired block change variant via a drop-down list.

###### Configuring the external block change via measuring input

1. Click the "External block change" button in the "Traversing blocks" mask.

   The "External block change" dialog opens.
2. Select the "External block change via measuring input" setting in the "External block change" drop-down list.
3. Connect the "Measuring input evaluation edge" ([p2511](SINAMICS%20Parameter%20SERVO.md#p251103-bi-lr-measuring-probe-evaluation-edge)) signal source for the edge evaluation of the measuring input.
4. Select the input terminal for the connection of measuring input 1 in the "Measuring input 1 input terminal" ([p0488](SINAMICS%20Parameter%20SERVO.md#p048802-measuring-probe-1-input-terminal-3)) drop-down list.

   or

   Connect the signal source for the selection of the measuring input (1 or 2) in the "Measuring input evaluation selection" ([p2510](SINAMICS%20Parameter%20SERVO.md#p251003-bi-lr-selecting-measuring-probe-evaluation)) field.
5. Select the input terminal for the connection of measuring input 1 in the "Measuring input 1 input terminal" (p0488) drop-down list.
6. Select the input terminal for the connection of measuring input 2 in the "Measuring input 2 input terminal" ([p0489](SINAMICS%20Parameter%20SERVO.md#p048902-measuring-probe-2-input-terminal-1)) drop-down list.
7. Connect the signal source for the "Measured value valid" feedback signal in the "External block change via measuring input" ([p2661](SINAMICS%20Parameter%20SERVO.md#p2661-bi-epos-measured-value-valid-feedback-signal)) field.
8. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### External block change via BI: configuring p2633

The external block change can be connected simply via p2633 with this setting.

1. Click the "External block change" button in the "Traversing blocks" mask.

   The "External block change" dialog opens.
2. Select the "External block change via BI: p2633" setting in the "External block change" drop-down list.
3. Connect the signal source for the external block change in the "External block change via BICO" (p2633) field.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Additional parameters

---

###### Programming traversing blocks

###### Parameters of the traversing blocks

You can define a maximum of 64 traversing blocks in the "Traversing blocks" dialog. You parameterize each individual traversing block in the table. You can enter the various parameters in the columns. The following parameters can be used to parameterize a traversing block:

**Index**

The Index column shows the index of the corresponding parameters.

**Number [-1, 0, ... 63]**

The number represents the block number ([p2616](SINAMICS%20Parameter%20SERVO.md#p26160n-epos-traversing-block-block-number)). It is used for the unique identification of the task for the selection using the Block selection bit 0 ... 5 signals. The processing sequence for multiple tasks is in ascending order. Traversing tasks with number -1 will be ignored. This allows the task to be removed from the sequence without deleting it. You can specify an arbitrary task number [0 ... 63]. This means, for example, you can define a task 5 after task 2 and reserve numbers 3 and 4 for a subsequent editing.

**Task**

You can select the following tasks in the Task list:

| Symbol | Meaning |
| --- | --- |
| [1] POSITIONING | Initiates a traversing motion until the target position is reached. |
| [2] FIXED STOP | Allows a clamping torque and a clamping force to be entered for the fixed stop.  Activates the "Configuration of fixed stop" button with which you can call a dialog for configuring the fixed stop parameters. |
| [3] ENDLESS_POS | Accelerates to the defined velocity:  - until the software limit switch is reached - until the travel area limit is reached - until the motion is interrupted by BB/intermediate stop - until the motion is aborted by the Discard BB/travel task |
| [4] ENDLESS_NEG | See "ENDLESS_POS". |
| [5] WAIT | Defines a wait time for the next task. |
| [6] GOTO | Allows jumps within a series of traversing tasks. The block number to which the jump is to be made must be specified as task parameter (see below). |
| [7] SET_O | Allows the setting of up to two digital outputs at the same time. |
| [8] RESET_O | Allows the reset of up to two digital outputs at the same time. |
| [9] JERK | Allows a jerk limitation. |

**Task parameter**

The supplementary information for the tasks is queried here:

| Symbol | Meaning |
| --- | --- |
| WAIT | Wait time in [ms] |
| GOTO | Block number (see task) |
| SET_O | Set digital output 1, 2 or both (3). |
| RESET_O | Reset digital output 1, 2 or both (3). |
| Jerk | "1" for activate or "0" for deactivate |
| FIXED STOP | Input of the clamping torque [0.01 Nm] and clamping force in [N] |

**Task mode**

You can specify the positioning mode here:

| Symbol | Meaning |
| --- | --- |
| ABSOLUTE | Travel to the specified position. |
| RELATIVE | Traverse the axis by the specified value. |
| ABS_POS | Travel to the specified position in the direction of increasing actual position values.  (only with activated modulo correction) |
| ABS_NEG | Travel to the specified position in the direction of decreasing actual position values.  (only with activated modulo correction) |

**Transition**

The transition specifies the continuation condition when the next traversing task is to be activated. The following settings are possible:

| Symbol | Meaning |
| --- | --- |
| END | Ends the traversing task; the continuation condition can be used for pure single operation (each task will be started individually) or for the last traversing task of a sequence. |
| CONTINUE_WITH_STOP | Travel is made to exactly the position specified in the traversing block and the axis will be braked to standstill. The following task will be performed without a restart by the "activate traversing task" ([p2631](SINAMICS%20Parameter%20SERVO.md#p2631-bi-epos-activate-traversing-task-0---1)) signal as soon as the actual position lies within the positioning window. |
| CONTINUE_FLYING | The following traversing block is processed immediately when the time to apply the brake is reached. If a direction reversal needs to be made, the behavior corresponds to that for CONTINUE_WITH_STOP, i.e. it will be braked to standstill. |
| CONTINUE_EXTERNAL | Behavior as with CONTINUE_FLYING, but an immediate block change can be triggered via the signal at the binector input [p2632](SINAMICS%20Parameter%20SERVO.md#p2632-epos-external-block-change-evaluation) "External block change" up to the time to apply the brake. If an external block change is not triggered, there is a flying change to the next block at the time to apply the brake. |
| CONTINUE_EXTERNAL_WAIT | A flying change to the next task can be triggered during the entire motion phase via the control signal "External block change". If an "external block change" is not triggered, the axis remains in the parameterized target position until the signal is issued. |
| CONTINUE_EXTERNAL_ALARM | The behavior is as with CONTINUE_EXTERNAL_WAIT, but warning A07463 "External traversing block change in traversing block x not requested" is output if an "external block change" has not been triggered before standstill is reached. The warning can be converted to an alarm with stop response so that block processing can be aborted if the control signal is not issued. |

**Remaining columns**

| Symbol | Meaning |
| --- | --- |
| **Position** | Target position to be approached in the traversing block. |
| **Velocity** | Velocity with which the traversing command is to be performed. The value is influenced by the velocity override. |
| **Acceleration** | Value for the acceleration override which influences the maximum acceleration. |
| **Deceleration** | Value for the deceleration override which influences the maximum deceleration. |
| **Hide** | If you remove the traversing task from the display, it will not be processed. The traversing task then behaves as if it had task number -1. |

###### Programming the traversing block

1. Open the "Program traversing blocks" screen form using the secondary navigation or by clicking the "Program traversing blocks" button in the "Traversing blocks" screen form.
2. In order to be able to edit the "Maximum number of tasks", click the "Edit" button (pin symbol) in the title bar. The input field is activated (online only).
3. Enter the maximum number of traversing blocks. The number of rows in the table then changes accordingly.

   If you reduce the number of traversing blocks, the excess traversing blocks will be lost.
4. Specify the desired parameters for each traversing block (for an explanation, see "Parameters of the traversing block")
5. Click the "Exit editing" button to accept the setting.

###### Configuring the fixed stop

With "Travel to fixed stop", you can, for example, traverse sleeves against the workpiece with a specified torque. You can parameterize the clamping torque in the traversing task. The limit stop monitoring window is parameterized in this dialog. This allows, for example, the drive to traverse beyond the window when the fixed stop breaks away.

1. Click the "Fixed stop configuration" button.

   A dialog with the same name opens.
2. Select which source you want to use for the fixed stop detection from the drop-down list at the top list:

   - "Fixed stop detection via external signal":   
     Enables the fixed stop to be detected, e.g. via BERO.
   - "Fixed stop via maximum following error":   
     Enables a following error that signals the "Fixed stop reached" state to be defined (in LU = Length Unit).
3. Interconnect the "Fixed stop reached" ([p2637](SINAMICS%20Parameter%20SERVO.md#p2637-bi-epos-fixed-stop-reached)) signal source for the "Fixed stop reached" feedback signal.
4. Enter in the "Position tolerance after fixed stop detection" ([p2635](SINAMICS%20Parameter%20SERVO.md#p2635-epos-fixed-stop-monitoring-window)) field, the value for the monitoring window of the actual position after reaching the fixed stop.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Configuring the digital output

1. Click the "Digital output configuration" button.

   A dialog with the same name opens.
2. Interconnect the digital output 1 ([r2683](SINAMICS%20Parameter%20SERVO.md#r2683014-cobo-epos-status-word-1-1).10) and 2 (r2683.11) signal sinks for indicating the status word 1 of the two digital outputs.
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Function diagrams (FD)

- EPOS - Traversing blocks mode external block change (r0108.4 = 1) - 3615 -
- EPOS - Traversing blocks mode (r0108.4 = 1) - 3616 -
- EPOS - Travel to fixed stop (r0108.4 = 1) - 3617 -

###### Additional parameters

---

##### Direct setpoint specification (MDI) (servo)

This section contains information on the following topics:

- [Direct setpoint specification](#direct-setpoint-specification)
- [Configuring the fixed setpoints](#configuring-the-fixed-setpoints)

###### Direct setpoint specification

###### Description

The external controller specifies the position value and also the traversing profile for the axis. Since the converter does not save, new target values must also be specified by the controller for new movements.

> **Note**
>
> Absolute direct setpoint specification is possible only for homed axis.

**Editing mode**

The editing mode of the "Direct setpoint specification (MDI)" screen form can be set via a drop-down list. The following selections are available:

- Standard

  Limited configuration scope
- Expert

  Complete configurability

###### Configuring the direct setpoint specification in expert mode

1. Select the "Expert" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the signal sources for the binector and connector inputs on the left in the screen form, beginning with "Acceptance type selection" ([p2649](SINAMICS%20Parameter%20SERVO.md#p2649-bi-epos-direct-setpoint-inputmdi-transfer-type-selection)).
3. Interconnect the signal sinks for the binector outputs (multiple connections are possible) on the right in the screen form, beginning with "Traversal command active" ([r2684](SINAMICS%20Parameter%20SERVO.md#r2684015-cobo-epos-status-word-2).15).
4. Configure the fixed setpoints (see [Configuring fixed setpoints](#configuring-the-fixed-setpoints)).

> **Note**
>
> Step 4 can also be performed in standard mode.

###### Function diagrams (FD)

EPOS - Direct setpoint input/MDI mode, dynamic values (r0108.4 = 1) - 3618 -

EPOS - Direct setpoint input/MDI mode (r0108.4 = 1) - 3620 -

###### Additional parameters

---

###### Configuring the fixed setpoints

###### Description

Set the fixed setpoints for direct setpoint specification in the "Configure fixed setpoints" dialog. The dialog can also be called via the "Direct setpoint specification" screen form.

###### Configuring fixed setpoints

1. Click the "Configure fixed setpoints" button in the "Direct setpoint specification (MDI)" screen form.

   The "Configure fixed setpoints" dialog opens.
2. Enter a fixed setpoint for the position in the "Position" ([p2690](SINAMICS%20Parameter%20SERVO.md#p2690-co-epos-position-fixed-setpoint)) field.
3. Enter a fixed setpoint for the velocity in the "Velocity" ([p2691](SINAMICS%20Parameter%20SERVO.md#p2691-co-epos-velocity-fixed-setpoint)) field.
4. Enter a fixed setpoint for the acceleration override in the "Acceleration override" ([p2692](SINAMICS%20Parameter%20SERVO.md#p2692-co-epos-acceleration-override-fixed-setpoint)) field.
5. Enter a fixed setpoint for the deceleration override in the "Deceleration override" ([p2693](SINAMICS%20Parameter%20SERVO.md#p2693-co-epos-deceleration-override-fixed-setpoint)) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Additional parameters

---

---

**See also**

[Direct setpoint specification](#direct-setpoint-specification)

#### Position control

This section contains information on the following topics:

- [Overview](#overview-6)
- [Actual position value preparation (servo)](#actual-position-value-preparation-servo)
- [Position controller (servo)](#position-controller-servo)
- [Position controller monitoring (servo)](#position-controller-monitoring-servo)

##### Overview

###### Description

A position controller compensates position deviations during motion and at standstill. To do this, it first compares the current position of an axis with its set position. The position controller is a fundamental requirement for the function of the [Basic positioner](#overview-5).

The position controller essentially consists of the following parts:

- Actual position value processing (including lower-level measuring input evaluation and reference mark search)
- Position controller (including limitations, adaptation and precontrol calculation)
- Monitoring functions (including standstill monitoring, positioning monitoring, dynamic following error monitoring and output cam signals)
- Load gearbox position tracking (motor encoder) when using absolute encoders for rotary axes (modulo) as well as linear axes

###### Requirement

- The "Position control" function module has been activated (see [Function modules (servo)](#function-modules-servo)).

  - OR -
- The "Basic positioner" function module is activated (see [Function modules (servo)](#function-modules-servo)).

  With this function module, the "Position control" function module is also automatically activated.

---

**See also**

[Actual position value preparation (servo)](#actual-position-value-preparation-servo)
  
[Position controller (servo)](#position-controller-servo)
  
[Position controller monitoring (servo)](#position-controller-monitoring-servo)

##### Actual position value preparation (servo)

###### Description

The actual position value processing processes the encoder signals (actual position values) for length units LU used for the position control. Various correction values can be applied for this purpose.

The processing of the actual position value is performed independently of the position controller enable immediately after the system ramp-up, as soon as valid values are received via the encoder interface.

**Editing mode**

The two editing modes (views) are available for the actual position value processing:

- Standard

  Limited configuration scope
- Expert

  Complete configurability

###### Configuring the actual position value processing in expert mode

1. Select the "Expert" editing mode in the "View" drop-down list at the top.

   The display of the screen form corresponds to the selected mode.
2. Interconnect the signal source for the position offset in the "Position offset" field ([p2516](SINAMICS%20Parameter%20SERVO.md#p251603-ci-lr-position-offset)).
3. Click the "Actual position value correction" button.

   The "Actual position value processing" detail screen form opens.
4. If required, enter the size of the modulo range for axes with modulo correction in the "Modulo correction modulo range" field.
5. Interconnect the following signal sources:

   - "Correction value" ([p2513](SINAMICS%20Parameter%20SERVO.md#p251303-ci-lr-position-actual-value-preprocessing-corrective-value)) for the correction value for the actual position value processing
   - "Correction value activation" ([p2512](SINAMICS%20Parameter%20SERVO.md#p251203-bi-lr-pos-actual-value-preprocessing-activate-corr-value-edge)) for the "Activate position actual value preprocessing, corrective value (edge)" function
   - "Negative correction activation" ([p2730](SINAMICS%20Parameter%20SERVO.md#p273003-bi-lr-pos-actual-value-preprocessing-activate-neg-corr-edge)) for the "Activate position actual value preprocessing, negative corrective value (edge)" function
6. Return to the main screen form using the secondary navigation.
7. Click the "Set actual position value" button.

   The "Set actual position value" detail screen form opens.
8. Interconnect the following signal sources:

   - "Position setting value" high ([p2515](SINAMICS%20Parameter%20SERVO.md#p251503-ci-lr-position-actual-setting-setting-value)) for the setting value of the "Set position actual value" function
   - "Position setting value activation" low ([p2514](SINAMICS%20Parameter%20SERVO.md#p251403-bi-lr-activate-position-actual-value-setting)) for activation of the "Set position actual value" function
9. Return to the main screen form using the secondary navigation.
10. Interconnect the "Position actual value" ([p2521](SINAMICS%20Parameter%20SERVO.md#r252103-co-lr-position-actual-value)[0]) signal sink for the position actual value currently determined by the position actual value preprocessing. Multiple connection is possible.
11. Interconnect the "Velocity actual value" ([p2522](SINAMICS%20Parameter%20SERVO.md#r252203-co-lr-velocity-actual-value)[0]) signal sink for the velocity actual value currently determined by the position actual value preprocessing. Multiple connection is possible.

> **Note**
>
> Step 2 can also be performed in standard mode.

###### Function diagrams (FD)

Position control - Position actual value processing (r0108.3 = 1) - 4010 -

###### Additional parameters

- [r2521](SINAMICS%20Parameter%20SERVO.md#r252103-co-lr-position-actual-value)
- [r2522](SINAMICS%20Parameter%20SERVO.md#r252203-co-lr-velocity-actual-value)

---

##### Position controller (servo)

This section contains information on the following topics:

- [Basic settings](#basic-settings-3)
- [Position controller - setpoints](#position-controller---setpoints)
- [Position controller - position controller](#position-controller---position-controller)
- [Position controller - manipulated variable](#position-controller---manipulated-variable)

###### Basic settings

###### Description

The position controller is a PI controller. In this way, it is also possible to compensate even the smallest control deviations. The PI controller is mainly used for the velocity control, because an integrator component in a position controller causes an overshoot of the axis until the integrator component has decayed.

> **Note**
>
> The parameter assignment of the position controller functions without simultaneous use of the basic positioner is only recommended for experts.

**Editing mode**

The following editing modes are available for the actual position value processing:

- Standard

  Limited configuration scope
- Expert

  Complete configurability

###### Making basic settings in expert mode

1. Select the "Expert" editing mode in the drop-down list at the top left.

   The display of the screen form corresponds to the selected mode.
2. Enter a value for the proportional gain of the position controller in the "Proportional gain" field ([p2538](SINAMICS%20Parameter%20SERVO.md#p25380n-lr-proportional-gain)).

   The proportional gain specifies for which traversing velocity which following error occurs.
3. Enter a percentage value for the weighting of the speed precontrol value in the "Speed precontrol factor" ([p2534](SINAMICS%20Parameter%20SERVO.md#p25340n-lr-velocity-precontrol-factor-1)) fied.

   The precontrol is automatically activated with a percentage value &gt; 0%.
4. Interconnect the "Velocity setpoint" ([p2531](SINAMICS%20Parameter%20SERVO.md#p2531-ci-lr-velocity-setpoint)) signal source for the velocity setpoint of the position controller.

   With activated basic positioner, the velocity setpoint is interconnected to [r2666](SINAMICS%20Parameter%20SERVO.md#r2666-co-epos-velocity-setpoint) as standard.
5. Interconnect the "Position setpoint" ([p2530](SINAMICS%20Parameter%20SERVO.md#p2530-ci-lr-position-setpoint)) signal source for the position setpoint of the position controller.
6. Interconnect the "Actual position value" ([p2532](SINAMICS%20Parameter%20SERVO.md#p2532-ci-lr-position-actual-value)) signal source for the actual position value of the position controller.
7. Specify the setpoints of the position controller in the "[Position controller setpoints](#position-controller---setpoints)" dialog.
8. Specify the detailed settings of the position controller in the "[Position controller](#position-controller---position-controller)" dialog.
9. Specify the manipulated variable values of the position controller in the "[Position controller manipulated variable](#position-controller---manipulated-variable)" dialog.
10. Interconnect the "Overall speed setpoint" ([r2562](SINAMICS%20Parameter%20SERVO.md#r2562-co-lr-velocity-setpoint-total-1)) signal sink for the overall speed setpoint.

**Note**

You cannot make the interconnections in steps 4 to 6 in the "Standard" editing mode.

###### Function diagrams (FD)

Position control - Position controller (r0108.3 = 1) - 4015 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)
- [r2557](SINAMICS%20Parameter%20SERVO.md#r2557-co-lr-position-controller-input-system-deviation)
- [r2560](SINAMICS%20Parameter%20SERVO.md#r2560-co-lr-velocity-setpoint-1)
- [r2561](SINAMICS%20Parameter%20SERVO.md#r2561-co-lr-velocity-precontrol-value-1)
- r2562

---

###### Position controller - setpoints

###### Specifying the setpoints

1. Click the "Position controller setpoints" button.

   The "Position controller setpoints" dialog opens.
2. Enter the weighting of the speed precontrol value in % in the "Speed precontrol factor" ([p2534](SINAMICS%20Parameter%20SERVO.md#p25340n-lr-velocity-precontrol-factor-1)) field.

   This setting is optional. If you make this entry, the weighting is automatically active.
3. Enter the time constant for the position setpoint filter PT1 in the "Position setpoint filter" ([p2533](SINAMICS%20Parameter%20SERVO.md#p25330n-lr-position-setpoint-filter-time-constant)) field.
4. Enter the dead time for the emulation of the time response of the closed velocity control loop in the "Dead time factor" ([p2535](SINAMICS%20Parameter%20SERVO.md#p25350n-lr-velocity-precontrol-symmetrizing-filter-dead-time-1)) field.
5. Enter the time value of a PT1 filter for the emulation of the time response of the closed speed control loop in the "Time constant" ([p2536](SINAMICS%20Parameter%20SERVO.md#p25360n-lr-velocity-precontrol-symmetrizing-filter-pt1-1)) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Function diagrams (FD)

Position control - Position controller (r0108.3 = 1) - 4015 -

###### Additional parameters

- [r2556](SINAMICS%20Parameter%20SERVO.md#r2556-co-lr-position-setpoint-after-setpoint-smoothing)
- [r2565](SINAMICS%20Parameter%20SERVO.md#r2565-co-lr-following-error-actual)

---

###### Position controller - position controller

###### Making the detailed settings for the position controller

1. Click the "Position controller" button.

   The "Position controller" dialog opens.
2. Interconnect the "Enable 1" ([p2549](SINAMICS%20Parameter%20SERVO.md#p2549-bi-lr-enable-1)) signal source for the 1st enable of the position controller.

   - AND -

   Interconnect the "Enable 2" ([p2550](SINAMICS%20Parameter%20SERVO.md#p25500n-bi-lr-enable-2)) signal source for the 2nd enable of the position controller.
3. Interconnect the "Position controller adaptation" ([p2537](SINAMICS%20Parameter%20SERVO.md#p2537-ci-lr-position-controller-adaptation)) signal source for the adaptation of the proportional gain of the position controller.
4. Enter the integral time of the position controller in the "Integral time" ([p2539](SINAMICS%20Parameter%20SERVO.md#p25390n-lr-integral-time)) field.

   The I component of the position controller is automatically activated with a percentage value &gt; 0%.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Function diagrams (FD)

Position control - Position controller (r0108.3 = 1) - 4015 -

###### Additional parameters

- [r2558](SINAMICS%20Parameter%20SERVO.md#r2558-co-lr-position-controller-output-p-component-1)
- [r2559](SINAMICS%20Parameter%20SERVO.md#r2559-co-lr-position-controller-output-i-component-1)

---

###### Position controller - manipulated variable

###### Setting the manipulated variables

1. Click the "Position controller manipulated variable" button.

   The "Position controller manipulated variable" dialog opens.
2. Enter the moment of inertia for the torque precontrol in the "Torque precontrol moment of inertia" ([p2567](SINAMICS%20Parameter%20SERVO.md#p25670n-lr-force-precontrol-mass-1)) field.
3. Interconnect the signal source for the limitation of the position controller output in the "Speed limit signal source" ([p2541](SINAMICS%20Parameter%20SERVO.md#p2541-ci-lr-position-controller-output-velocity-limit-signal-source-1)) field.
4. Enter the speed limit of the position controller output in the "Speed limit" ([p2540](SINAMICS%20Parameter%20SERVO.md#p2540-co-lr-position-controller-output-velocity-limit-1)) field.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Function diagrams (FD)

Position control - Position controller (r0108.3 = 1) - 4015 -

###### Additional parameters

- [r2560](SINAMICS%20Parameter%20SERVO.md#r2560-co-lr-velocity-setpoint-1)
- [r2561](SINAMICS%20Parameter%20SERVO.md#r2561-co-lr-velocity-precontrol-value-1)
- [r2562](SINAMICS%20Parameter%20SERVO.md#r2562-co-lr-velocity-setpoint-total-1)
- [r2564](SINAMICS%20Parameter%20SERVO.md#r2564-co-lr-force-precontrol-value-1)

---

##### Position controller monitoring (servo)

This section contains information on the following topics:

- [Positioning and standstill monitoring](#positioning-and-standstill-monitoring)
- [Following error monitoring](#following-error-monitoring)
- [Output cam](#output-cam)

###### Positioning and standstill monitoring

###### Description

As soon as the setpoint for the position within a positioning operation no longer changes, the drive sets the "Setpoint stationary" signal to 1. With this signal, the drive starts to monitor the actual position value:

- As soon as the axis has reached the positioning window, the drive signals that the target has been reached, and maintains the axis in closed-loop control.
- If the axis does not come to a standstill within the standstill monitoring time, the drive signals fault F07450.
- If the axis does not enter the positioning window within the positioning monitoring time, the drive signals fault F07451.

![Standstill monitoring](images/147859435147_DV_resource.Stream@PNG-en-US.png)

Standstill monitoring

###### Parameterizing the position monitoring

On the basis of a positioning window, the entry of the axis into the specified position at the end of a positioning motion is monitored. This requires the specification of a positioning window and a time interval.

1. Enter a value (value = 0, positioning monitoring is deactivated; value &gt;= 1, positioning monitoring is active) in the "Positioning window" ([p2544](SINAMICS%20Parameter%20SERVO.md#p2544-lr-positioning-window)) field.

   The positioning monitoring defines the range around the target position in which the actual position value must lie after the positioning monitoring time has expired.
2. Enter a value in the "Position monitoring time" ([p2545](SINAMICS%20Parameter%20SERVO.md#p2545-lr-positioning-monitoring-time)) field.

   The positioning monitoring time defines the interval in which the following error must lie once within the positioning window, after the time expires.

###### Parameterizing the standstill monitoring

The standstill monitoring monitors the actual position of the axis after a traversing motion has been completed. Two windows are specified for the standstill monitoring.

1. Enter a value (value = 0, standstill monitoring is deactivated; value ≥ 1, standstill monitoring is active) in the "Standstill window" ([p2542](SINAMICS%20Parameter%20SERVO.md#p2542-lr-standstill-window)) field.

   The standstill window defines the range around the target position in which the actual position value must lie after the standstill window monitoring time has expired.
2. Enter a value in the "Standstill monitoring time" ([p2543](SINAMICS%20Parameter%20SERVO.md#p2543-lr-standstill-monitoring-time)) field.

   The standstill monitoring time defines the range which after its expiration the following error must lie within the standstill window. The standstill window is monitored cyclically.

###### Display parameters

The following information is displayed via display parameters:

- Position reached ([r2684](SINAMICS%20Parameter%20SERVO.md#r2684015-cobo-epos-status-word-2))

  Shows whether the set position has been reached (yes/no).

###### Function diagrams (FD)

- Position control - Standstill monitoring / position monitoring (r0108.3 = 1) - 4020 -
- Position control - Dynamic following error monitoring, cam sequencer (r0108.3 = 1) - 4025 -

###### Additional parameters

---

###### Following error monitoring

###### Description

The following error is the difference between a ramp-shaped, variable position setpoint and the associated actual position value. The more dynamic a control loop is, the smaller the resulting following error is. A maximum following error for the actual position value is often specified for the monitoring of position control loops. If this following error is violated, the position control aborts the current positioning operation and generates a fault message.

![Following error](images/147859470859_DV_resource.Stream@PNG-en-US.png)

Following error

###### Defining the maximum possible deviation

1. The interconnection of the "Travel to fixed stop active" ([p2552](SINAMICS%20Parameter%20SERVO.md#p2552-bi-lr-signal-travel-to-fixed-stop-active)) signal source is preset for the corresponding signal.

   If required, correct this interconnection.
2. Enter the maximum deviation between the calculated and the measured actual position value before an error occurs in the "Maximum following error" ([p2546](SINAMICS%20Parameter%20SERVO.md#p25460n-lr-dynamic-following-error-monitoring-tolerance)) field.

   (Value = 0, dyn. following error monitoring is deactivated; value ≥ 1, dyn. following error monitoring is active)
3. Interconnect the signal sink in the "Following error in tolerance" ([r2684](SINAMICS%20Parameter%20SERVO.md#r2684015-cobo-epos-status-word-2).8) field.

   The signal for the following error is generated in the "Position control" function module.

###### Function diagrams (FD)

- Position control - Standstill monitoring / position monitoring (r0108.3 = 1) - 4020 -
- Position control - Dynamic following error monitoring, cam sequencer (r0108.3 = 1) - 4025 -

###### Additional parameters

---

###### Output cam

###### Description

Using the position-dependent switching signals 1 and 2, output cams can be emulated without any mechanical equipment (e.g. at inaccessible positions), depending on the actual position value. The absolute cam switching positions are specified via parameters, and the associated cam switching signals are output as output signals. The reference is guaranteed only for a homed axis.

###### Setting the cam switching positions

1. Enter a value for cam switching position 1 at "Cam switching position 1" ([p2547](SINAMICS%20Parameter%20SERVO.md#p2547-lr-cam-switching-position-1)).
2. Interconnect the "Cam switching signal 1" ([r2683](SINAMICS%20Parameter%20SERVO.md#r2683014-cobo-epos-status-word-1-1).8) signal sink for the signal that the actual position value is less than or equal to cam switching position 1.
3. Enter a value for cam switching position 2 at "Cam switching position 2" ([p2548](SINAMICS%20Parameter%20SERVO.md#p2548-lr-cam-switching-position-2)).
4. Interconnect the "Cam switching signal 2" (r2683.9) signal sink for the signal that the actual position value is less than or equal to cam switching position 2.

> **Note**
>
> For position values less than the cam switching position, the associated status bit supplies a "1 signal", for values greater than the cam switching position a "0 signal".

###### Function diagrams (FD)

- Position control - Standstill monitoring / position monitoring (r0108.3 = 1) - 4020 -
- Position control - Dynamic following error monitoring, cam sequencer (r0108.3 = 1) - 4025 -

###### Additional parameters

---

#### Active oscillation damping (APC)

This section contains information on the following topics:

- [Overview](#overview-7)
- [Configuration](#configuration)
- [Active Vibration Suppression (APC without sensor on the load side)](#active-vibration-suppression-apc-without-sensor-on-the-load-side)
- [APC with encoder mixing and position-difference feedback](#apc-with-encoder-mixing-and-position-difference-feedback)
- [APC with acceleration feedback](#apc-with-acceleration-feedback)
- [APC with load velocity control](#apc-with-load-velocity-control)
- [APC filter settings](#apc-filter-settings)

##### Overview

###### Description

The "Advanced Positioning Control (APC)" function module provides functions for the closed-loop control active damping/influencing of mechanical vibrations. APC is not a filter. The function responds actively with an appropriate manipulated variable to measured vibrations. The motor performs a motion to compensate for the vibration. If the vibration frequency changes, e.g. because of the axis loading or mechanical changes, APC also acts for the changed frequency. The APC function module is calculated in the speed control loop.

Vibrations can be influenced by the motor speed controller (P-gain, integrator). There are two strategies: With a high gain, the controller is set optimally with regard to interferences. This often increases load-side vibrations. For an optimum damping setting, although the vibration is reduced, the controller gain must be reduced which reduces the interference suppression. The APC function module returns additional functions that resolve this conflict. APC allows a vibration to be dampened and simultaneously achieves a good interference suppression with a high speed controller gain.

The mechanical vibrations can be excited in two ways:

- **Excitation by reference values** (planned motion of the axis)

  In this case, the vibration can be reduced by influencing the reference variable (e.g. by changing the acceleration), by limiting the jerk or by deploying a setpoint filter. This function has the disadvantage that it normally increases the processing or cycle times. The deployment of a setpoint filter also frequently results in increased inaccuracy for representing the contours.

  The deployment of APC can reduce the vibration without these disadvantages.
- **Excitation by disturbance variables** (e.g. by periodic process forces)

  In this case, the vibration can be influenced only by an active closed-loop control.

  In both cases, for a successful deployment of APC, it must be possible to measure the vibration at a measuring system/sensor assigned to the axis. For this purpose, the function module offers several versions. APC can be set only by using motor variables (motor encoder, current). If a direct measuring system is available, it can be deployed for APC. It is also possible to integrate an external acceleration sensor in the system and use it for APC.

###### Requirements

- The "Advanced Positioning Control (APC)" function module is activated (see [Function modules](#function-modules-servo)).

- Only drives of type "highly dynamic (servo)" available.
- For some functions integrated in the APC, a 2nd measuring system is required. A more detailed description of the associated requirements is documented in the description of the various subfunctions.
- Based on experience, frequencies of up to 100 Hz can be influenced by APC. Whether an oscillation can be influenced depends on how the mechanical system affects the closed-loop control or how the speed controller loop was set.
- For all functions of the "Advanced Positioning Control" function module, including "Active Vibration Suppression", the license: "Active Vibration Suppression (APC/AVS)" is required.
- The Auto Servo Tuning has been performed previously.

  APC functions must only be performed after an Auto Servo Tuning.

###### Application examples of APC

- The deployment of APC can improve the behavior of a higher-level position control of the speed control. Damping the critical vibration in the speed control loop often allows a higher position controller gain to be set. This is true, in particular, when the position control uses a direct measuring system for the closed-loop control.
- If periodic machining forces (e.g. heavy-duty cutting of steel) in the process cause instability in the process (regenerative rattling), this vibration form can be dampened by APC. The damping ensures that the process is no longer instable. Higher machining feed rates or increased swarf thickness are possible.
- The intended movement of the axes in the process causes vibrations of the mechanical structure. These vibrations have negative effects in the process (e.g. for the finishing of surfaces in mold making). The process must be made slower to avoid these vibrations. APC dampens the vibration and avoids these disadvantages. It is possible to accelerate the process.

> **Note**
>
> The functions integrated in APC are a separate control loop or intervene in the speed control loop. As a consequence, parameterizing the APC is critical from a stability standpoint.
>
> A deep understanding of control technology (e.g. interpretation of frequency responses) is required to tune APC in conjunction with a direct measuring system.
>
> The APC function should be set before tuning the speed control.

> **Note**
>
> Dampening the oscillation is achieved by moving the motor to oppose the oscillation. When correctly parameterized, oscillation is dampened and the amplitude on the load side of the mechanical system reduced. However, the motor itself moves more. This means that the mechanical transmission elements between the motor and load (e.g. gearboxes) are subject to an alternating variable and a high initial amplitude.

> **Note**
>
> Activation of this function module results in a substantial increase in the required CPU time per drive axis.
>
> Operation of 6 servo axes on one Control Unit cannot be guaranteed in all constellations and should be reduced to 5 axes.

###### Overview of the functions included in APC

The APC function module comprises essentially the following subfunctions:

- [Active Vibration Suppression (APC without sensor on the load side)](#active-vibration-suppression-apc-without-sensor-on-the-load-side)

  - Robust function for vibration damping.
  - Does not require a direct measuring system.
  - Can be activated individually/separately as "Active Vibration Suppression (AVS/APC-ECO)" function module.
- [APC with encoder mixing and position-difference feedback](#apc-with-encoder-mixing-and-position-difference-feedback)

  - Influencing the speed controlled system. The speed control behavior can be improved (e.g. increased speed controller gain).
  - Requires a direct measuring system.
  - It involves two functions that preferably should be deployed together.
- [APC with acceleration feedback](#apc-with-acceleration-feedback)

  - Requires a direct measuring system.
  - Uses the measured acceleration at the direct measuring system for damping a vibration.
  - Instead of the acceleration at the direct measuring system, an external acceleration sensor can be used.
- [APC with load velocity control](#apc-with-load-velocity-control)

  - Requires a direct measuring system.
  - P-control of the velocity at the direct measuring system.

##### Configuration

###### Description

Depending on the type of the actual value acquisition, a basic configuration can be made for the APC. The following actual value acquisition types are available:

- Without encoder
- Acceleration sensor
- Measuring system

###### Basic configuration for encoderless actual value acquisition

1. Select "Encoderless" actual value acquisition in the "Actual value acquisition selection" drop-down list.

   No further settings are necessary.

###### Basic configuration for actual value acquisition using acceleration sensors

> **Note**
>
> When using an acceleration sensor, it must be configured at the terminal module.

1. Select "Acceleration sensor" actual value acquisition in the "Actual value acquisition selection" drop-down list.

   The screen form is adapted to this actual value acquisition. The acceleration sensor must be configured and standardized before using this measuring method on the Terminal Module.
2. Interconnect the "APC acceleration sensor input" ([p3750](SINAMICS%20Parameter%20SERVO.md#p37500n-ci-apc-acceleration-sensor-input)[0]) signal source for the actual value of the acceleration sensor for APC.
3. Enter the reference variable for accelerations in the "Reference acceleration" ([p2007](SINAMICS%20Parameter%20SERVO.md#p2007-reference-acceleration-1)) field.

   The reference variable corresponds to 100% (4000 hex (word) or 4000 0000 hex (double word)).
4. If necessary, configure the [Acceleration precontrol](#apc-with-acceleration-feedback).

###### Basic configuration for actual value acquisition using the measuring system

1. Select "Measuring system" actual value acquisition in the "Actual value acquisition selection" drop-down list.

   The screen form is adapted to this actual value acquisition.
2. Select one of the following measuring systems in the "Measuring system selection" drop-down list.

   - BICO
   - Encoder 2
   - Encoder 3

   If you have selected the "BICO" measuring system, you can make additional settings.
3. Interconnect the "APC external actual velocity value input" ([p3749](SINAMICS%20Parameter%20SERVO.md#p37490n-ci-apc-velocity-actual-value-external-input)[0]) signal source for the actual value of the external actual velocity value for APC.
4. Enter in the "APC scaling velocity input" ([p3748](SINAMICS%20Parameter%20SERVO.md#p37480n-apc-velocity-input-scaling)[0]) field, the scaling value for adapting the actual velocity value via connector input p3749.

###### Function diagrams (FD)

- Technology functions - APC differential position gain (APC, r0108.7 = 1) - 7013 -
- Technology functions - External armature short-circuit (EASC, p0300 = 2xx or 4xx) - 7014 -

###### Additional parameters

---

##### Active Vibration Suppression (APC without sensor on the load side)

###### Description

The Active Vibration Suppression (AVS) function is a robust procedure for vibration damping without requiring a direct measuring system. Only the current and actual speed value signals measured on the motor are used. The AVS function can be used, in particular, also for drives with linear or torque motor that often do not use any direct measuring system.

To allow the function to be used successfully, the vibration to be dampened must have adequate feedback on the motor of the axis. This means that the oscillation in the motor current must be measurable.

Before the function can be optimized, the speed control loop must be optimized first, because it forms the lower-level controlled system.

> **Note**
>
> The "AVS" function can also be used when a direct measuring system is available. It is possible that this function has advantages compared with the use of a direct measuring system. The robustness of this function, e.g. for changes to the mechanical system, is normally better.
>
> The closed-loop control without sensor can also be combined with the P-component ([p3760](SINAMICS%20Parameter%20SERVO.md#p37600n-apc-load-velocity-controller-1-p-gain-1)/[p3765](SINAMICS%20Parameter%20SERVO.md#p37650n-apc-load-velocity-controller-2-p-gain-1)) of the direct measuring system provided a direct measuring system is available. This increases the interference suppression and accuracy.

###### Requirement

- The "Active Vibration Suppression" function (APC without sensor on the load side) requires the license with the same name: "Active Vibration Suppression (APC/AVS)".

###### Parameterizing APC without sensor on the load side

1. Select one of the following options in the "Take into account acceleration precontrol" ([p3700](SINAMICS%20Parameter%20SERVO.md#p3700-avsapc-configuration)[3]) drop-down list:

   - Yes. The speed precontrol value in [p1432](SINAMICS%20Parameter%20SERVO.md#r143201-co-speed-precontrol-1)[1] is taken into account when calculating the acceleration.
   - No. The speed precontrol value in p1432[1] is not taken into account when calculating the acceleration.
2. In the "Controller default setting natural vibration frequency" ([p3752](SINAMICS%20Parameter%20SERVO.md#p37520n-avs-controller-preassignment-natural-oscillation-frequency)[D]), enter the natural vibration frequency as default for the AVS controller data.
3. In the "Smoothing time" ([p3709](SINAMICS%20Parameter%20SERVO.md#p37090n-avsapc-velocity-actual-value-smoothing-time-encoder-3-1)[D]) field, enter a value for the smoothing time constant (PT1) for the actual velocity value from encoder 3 for the APC.
4. In the "High pass time constant" ([p3751](SINAMICS%20Parameter%20SERVO.md#p37510n-avsapc-acceleration-sensor-high-pass-time-constant)[D]) field, correct the setpoint value for the time constant of the high pass for the acceleration sensor for AVS and APC.
5. In the "Derivative-action time 1" ([p3761](SINAMICS%20Parameter%20SERVO.md#p37610n-avsapc-load-velocity-controller-1-rate-time-1)[D]) field, enter a value for the derivative-action time of the load velocity control 1 for APC.
6. In the "Derivative-action time 2" ([p3766](SINAMICS%20Parameter%20SERVO.md#p37660n-apc-load-velocity-controller-2-rate-time-1)[D]) field, enter a value for the derivative-action time of the load velocity control 2 for APC.

###### Function diagrams (FD)

- Technology functions - APC differential position gain (APC, r0108.7 = 1) - 7013 -
- Technology functions - External armature short-circuit (EASC, p0300 = 2xx or 4xx) - 7014 -

###### Additional parameters

---

##### APC with encoder mixing and position-difference feedback

###### Description

The controlled system for the speed control can be influenced with these two functions. The encoder mixing acts on the zero points (absorber frequencies) of the system and the position-difference feedback on the poles (resonance frequencies). It is often desirable to use both functions together.

The encoder mixing and the position-difference feedback are always optimized together with the optimization of the speed controller. It is normally better to first parameterize the position-difference feedback and then the encoder mixing.

**Application examples:**

- The ratio of the load inertia to the motor inertia is very large. The vibration frequency is relatively low. In this case, only a very low speed controller gain can often be set.  
  The encoder mixing allows the zero points to be moved to higher frequencies. The effective motor-side inertia increases and so a higher speed controller gain can be set. The combination with the position-difference feedback can increase this effect.
- The effect of a vibration form on the motor is only very small (e.g. because of a large gearbox ratio). The speed controller so does not influence the vibration. The deployment of encoder mixing and position-difference feedback increases the vibration effect apparent on the motor. The speed controller can be set to optimize the damping. This is particularly useful when no other APC functions should be used in addition.

The deployment of encoder mixing and position-difference feedback allows the vibration to be moved to higher frequencies. The speed controller can be set to optimize interference reduction with high gain. To dampen the vibration, an additional APC function is also deployed, e.g. acceleration feedback (see section "[APC with acceleration feedback](#apc-with-acceleration-feedback)").

> **Note**
>
> The encoder mixing and the position-difference feedback move not only the dominant vibration forms in the controlled system, but also all vibration forms that originate in the mechanical system between the two measuring systems. It is possible that a vibration form that should not actually be affected impairs the stability of the speed control. This must be considered for the optimization.

###### Parameterizing the encoder mixing

1. Select in the "Encoder mixing" setting range in the "Configuration" drop-down list, the desired option for encoder mixing:

   - None
   - Encoder mixing
   - Pulse decoupling
2. If the "Encoder mixing" option has been selected, enter in the "Load speed / motor speed weighting" ([p3702](SINAMICS%20Parameter%20SERVO.md#p37020n-apc-load-speedmotor-speed-weighting)[0]) field the weighting factor for forming the actual speed value from the load speed and motor speed.

   The motor encoder must have been parameterized previously for this setting.

###### Parameterizing the position-difference feedback

1. Enter in the "High-pass time constant" ([p3767](SINAMICS%20Parameter%20SERVO.md#p37670n-apc-differential-position-high-pass-time-constant)[0]) field, the time constant of the high pass for the position-difference gain for APC.
2. Enter in the "Gain factor" ([p3768](SINAMICS%20Parameter%20SERVO.md#p37680n-apc-differential-position-gain-factor-1)[0]) field, the Kp gain factor for the position-difference controller for APC.
3. Connect the "Position-difference torque setpoint" ([r3769](SINAMICS%20Parameter%20SERVO.md#r3769-co-apc-differential-position-force-setpoint-1)) signal sink for the torque setpoint from the position-difference controller for APC.

###### Function diagrams (FD)

- Technology functions - APC differential position gain (APC, r0108.7 = 1) - 7013 -
- Technology functions - External armature short-circuit (EASC, p0300 = 2xx or 4xx) - 7014 -

###### Additional parameters

---

##### APC with acceleration feedback

###### Description

For this function, the acceleration signal from a direct measuring system is used to dampen the vibrations.

Only those vibrations that can be measured on the direct measuring system can be dampened. If this is not the case, an external acceleration sensor can be attached at an appropriate location within the machine and used for APC.

The function, for example, is ideal for axes for which the vibration has a limited effect on the motor (e.g. because of a large transmission ratio or a strong gearbox self-locking).

A direct measuring system often causes high-frequency resonances in the range &gt; 100 Hz in the control loop that can cause major problems when setting the APC. In this case, the APC filter must be deployed to ensure the stability of the control loops. The dependency of such resonances, e.g. for axis positions, must also be considered. Such a found parameter assignment must be stable throughout the complete operating range of the machine. Also for this reason, the use of the function without direct measuring system (see Section "[Active Vibration Suppression (APC without sensor on the load side)](#active-vibration-suppression-apc-without-sensor-on-the-load-side)") is often more robust.

Before the function can be optimized, the speed control loop must be optimized first, because it forms the lower-level controlled system.

###### Parameterizing the acceleration feedback

1. Select in the "Consider acceleration precontrol" ([p3700](SINAMICS%20Parameter%20SERVO.md#p3700-avsapc-configuration).3)" drop-down list whether you want to share an acceleration precontrol.

   If you selected the "Yes" option, the mask is extended with a speed precontrol.
2. Connect the "External actual velocity value" ([p3749](SINAMICS%20Parameter%20SERVO.md#p37490n-ci-apc-velocity-actual-value-external-input)[0]) signal source for the actual value of the external actual velocity value for APC.
3. Enter in the "Scaling" ([p3748](SINAMICS%20Parameter%20SERVO.md#p37480n-apc-velocity-input-scaling)[0]) field, the scaling for adapting the actual velocity value via connector input p3749.
4. Enter in the "Derivative-action time 1" ([p3761](SINAMICS%20Parameter%20SERVO.md#p37610n-avsapc-load-velocity-controller-1-rate-time-1)[0]) field, the derivative-action time of load speed controller 1 for APC.
5. Enter in the "Derivative-action time 2" ([p3766](SINAMICS%20Parameter%20SERVO.md#p37660n-apc-load-velocity-controller-2-rate-time-1)[0]) field, the derivative-action time of load speed controller 2 for APC.

###### Function diagrams (FD)

- Technology functions - APC differential position gain (APC, r0108.7 = 1) - 7013 -
- Technology functions - External armature short-circuit (EASC, p0300 = 2xx or 4xx) - 7014 -

###### Additional parameters

---

##### APC with load velocity control

###### Description

This function implements a P-control of the load velocity parallel to the normal speed control. The vibration is moved to higher frequencies and dampened.

The function causes the motor to perform relatively large compensation movements.

The function effect has certain similarity with encoder mixing.

This function is particularly useful together with the "[APC with acceleration feedback](#apc-with-acceleration-feedback)" or "[Active Vibration Suppression](#active-vibration-suppression-apc-without-sensor-on-the-load-side)" functions.

###### Parameterizing the load velocity control

1. Interconnect the "External actual velocity value" ([p3749](SINAMICS%20Parameter%20SERVO.md#p37490n-ci-apc-velocity-actual-value-external-input)[0]) signal source for the actual value of the external actual velocity value for APC.
2. Enter in the "Scaling" ([p3748](SINAMICS%20Parameter%20SERVO.md#p37480n-apc-velocity-input-scaling)[0]) field, the scaling for adapting the actual velocity value via connector input p3749.
3. Enter in the "P-gain 1" ([p3760](SINAMICS%20Parameter%20SERVO.md#p37600n-apc-load-velocity-controller-1-p-gain-1)[0]) field, the proportional gain of load velocity controller 1 for APC.
4. Enter in the "P-gain 2" ([p3765](SINAMICS%20Parameter%20SERVO.md#p37650n-apc-load-velocity-controller-2-p-gain-1)[0]) field, the proportional gain of load velocity controller 2 for APC.

###### Function diagrams (FD)

- Technology functions - APC differential position gain (APC, r0108.7 = 1) - 7013 -
- Technology functions - External armature short-circuit (EASC, p0300 = 2xx or 4xx) - 7014 -

###### Additional parameters

---

##### APC filter settings

###### Making filter settings

1. Click the "Filter 2.x" button in the screen form.

   A dialog with the same name opens. Here you can specify the filter type for filters 2.1 and 2.2, specify the fine adjustment for each filter, and activate each of the filters.
2. Activate the "Filter effective" (p3704[D]) option for the filter you want to activate.
3. In the "Filter settings" (p3705[D]) drop-down list, select one of the following filter types for the filter:

   - [Low-pass PT2](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-pt2-filter)
   - [Bandstop](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-bandstop-filter)
   - [Low-pass with reduction](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-low-pass-filter-with-reduction)
   - [General 2nd order filter](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-a-general-2nd-order-filter)
4. Parameterize the following detailed values:

   - Numerator frequency, only for filter type "General 2nd order filter"
   - Numerator damping, only for filter type "General 2nd order filter"
   - Denominator frequency, for filter type "Low-pass PT2" and "General 2nd order filter"
   - Denominator damping, for filter type "Low-pass PT2" and "General 2nd order filter"
   - Blocking frequency, only for filter type "Bandstop"
   - Bandwidth, only for filter type "Bandstop"
   - Notch depth, only for filter type "Bandstop"
   - Reduction, only for filter type "Bandstop" and "Low-pass with reduction"
   - Characteristic frequency, only for filter type "Low-pass with reduction"
   - Damping, only for filter type "Low-pass with reduction"
5. Repeat steps 2 to 4 for the 2nd filter.
6. Click "Accept" to take your filter settings from "Filter 2.x" into the current configuration.

   The filter is displayed in the current configuration.
7. To switch on the parameterized filter, activate the "Filter effective" option.

   The "Filter 2.x" filter is activated in the screen form.
8. Once all necessary settings have been made, click "Close".  
   The dialog closes.
9. Click the "Filter 3.x" button in the screen form.

   You can now specify the filter type for filters 3.1 and 3.2, specify the fine settings for each filter and activate the associated filter (see steps 2...8).
10. Click the "Filter 1.1" button in the screen form.

    Specify the filter type for filter 1.1, together with the fine settings for the filter and activate the filter.
11. Interconnect the "Filter 1.1 output value" (p3777[1]) signal source for the speeds in filter branch 1.
12. If you want to activate APC, select the "[1] Yes" setting in the "Activate APC" (p3700[0]) drop-down list.

###### Defining the speed limit and maximum limit

1. Correct the specified value in the "Speed limit" (p3778) field.
2. If you want to correct more default values for the speed limit, click the "Maximum limit" button.

   A dialog with the same name opens.
3. If required, correct the default values in the following fields:

   - "Positive speed limit" (p1083)
   - "negative speed limit" (p1086)
   - "Maximum speed" (p1082)
4. Once all necessary settings have been made, click "Close".  
   The dialog closes.

#### Extended torque control

This section contains information on the following topics:

- [Extended torque control (servo)](#extended-torque-control-servo)

##### Extended torque control (servo)

###### Description

The "Extended torque control" function module increases the torque accuracy. It comprises the following individual functions:

- k<sub>T</sub> estimator (only for synchronous motors)
- Compensation of the voltage emulation error of the converter ([p1952](SINAMICS%20Parameter%20SERVO.md#p19520n-voltage-emulation-error-final-value), [p1953](SINAMICS%20Parameter%20SERVO.md#p19530n-voltage-emulation-error-current-offset), [p1954](SINAMICS%20Parameter%20SERVO.md#p19540n-voltage-emulation-error-semiconductor-voltage))
- k<sub>T</sub> characteristic ([p0645](SINAMICS%20Parameter%20SERVO.md#p06450n-motor-kt-characteristic-kt1-1)...[p0648](SINAMICS%20Parameter%20SERVO.md#p06480n-motor-kt-characteristic-kt7)) (only for synchronous motors)

The adaptation of the torque constant for synchronous motors improves the absolute torque accuracy for the closed-loop control of synchronous motors. As result of production tolerances, temperature fluctuations and saturation effects, the magnetization of the permanent magnets varies. The "k<sub>T</sub> estimator" function adapts the torque constant k<sub>T</sub> [Nm/A] in the control to the current magnetization. It only makes sense to use the k<sub>T</sub> estimator in conjunction with the friction characteristic as the k<sub>T</sub> estimator corrects the inner motor torque. The friction losses must be compensated with an additional torque from the friction characteristic.

The k<sub>T</sub> estimator requires the most accurate values for the motor parameters as possible in order to achieve a high torque accuracy. Consequently, before using the k<sub>T</sub> estimator, a motor data identification ([p1909](SINAMICS%20Parameter%20SERVO.md#p19090n-motor-data-identification-control-word-1), [p1910](SINAMICS%20Parameter%20SERVO.md#p1910-motor-data-identification-routine-stationary-standstill)) must be performed. Whereby, the values for stator resistance ([p0350](SINAMICS%20Parameter%20SERVO.md#p03500n-motor-stator-resistance-cold)), leakage inductance ([p0356](SINAMICS%20Parameter%20SERVO.md#p03560n-motor-stator-leakage-inductance)) and voltage emulation errors (p1952, p1953, p1954) are determined. A change of the DC-link voltage and the pulse frequency for the voltage emulation errors is taken into account with p1954 ≠ 0. Before the motor data identification, the line resistance must be entered in [p0352](SINAMICS%20Parameter%20SERVO.md#p03520n-cable-resistance).

The motor should be at room temperature for the identification. The compensation of the voltage conversion fault must be activated ([p1780](SINAMICS%20Parameter%20SERVO.md#p17800n-motor-model-adaptation-configuration-2).8 = 1). The motor temperature ([p0600](SINAMICS%20Parameter%20SERVO.md#p06000n-motor-temperature-sensor-for-monitoring)) should be acquired using a KTY or Pt1000 sensor ([p0601](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0601-temperature-sensor-sensor-type) = 2 or 3).

The k<sub>T</sub> estimator requires the motor temperature in order to track the temperature-dependent variables. If no motor temperature sensor is connected, the estimate is less exact.

The k<sub>T</sub> estimator is only activated above a specific switchover speed ([p1752](SINAMICS%20Parameter%20SERVO.md#p17520n-motor-model-changeover-speed-operation-with-encoder-1)). The terminal voltage of the converter always has small inaccuracies. The lower the output voltage and speed, the less exact the estimate. Consequently, the estimate is deactivated below a specific speed. The estimate value is smoothed with time constant [p1795](SINAMICS%20Parameter%20SERVO.md#p17950n-motor-model-kt-adaptation-smoothing-time). The correction value for the torque constant is indicated in [r1797](SINAMICS%20Parameter%20SERVO.md#r1797-motor-model-kt-adaptation-corrective-value-1).

The torque accuracy can be improved by the k<sub>T</sub> characteristic in the range below the switchover speed (p1752). To do this, the torque constant kT is identified for various currents during the rotating motor data identification and stored in p0645...p0648 as a polynomial. The current dependency of the torque constant can be taken into account. The k<sub>T</sub> characteristic can be combined with the k<sub>T</sub> estimator. The k<sub>T</sub> characteristic is active below the switchover speed (p1752) and the k<sub>T</sub> estimator is active above the speed. In addition to the current dependency, the k<sub>T</sub> estimator also compensates the effect of temperature and the reluctance torque.

The parameters for the voltage emulation errors cannot be determined with the stationary motor data identification for induction motors. At the first commissioning ([p3900](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p3900-completion-of-quick-commissioning) = 3 or [p0340](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0340-automatic-calculation-control-parameters) = 1 or 3), the parameters p1952...p1954 are assigned default values so that the voltage emulation errors for induction motors can also be compensated. However, as the stationary motor data identification returns more precise values, it should always be performed for synchronous motors.

###### Requirements

- The "Extended torque control" function module is activated (see [Function modules (servo)](#function-modules-servo)).

  > **Note**
  >
  > The activation of this function module reduces the maximum number of controllable drives of a Control Unit by at least one drive.
- The motor temperature sensor is configured (see [Motor temperature - Configuration example](#motor-temperature---configuration-example))
- The motor data identification has been performed (see [stationary/turning measurement](#stationaryrotating-measurement))
- A permanently-excited synchronous motor is used (device configuration).

###### Configuring extended torque control

For the extended torque control, individual functions can be activated individually or together:

1. Activate the option for the required individual functions of the extended torque control:

   - "kT adaptation"
   - "Voltage emulation error compensation"
   - "kT(iq) characteristic"
2. Enter the speed for switching the motor model for operation with an encoder in the "Switchover speed" (p1752) field.
3. Enter the smoothing time of the kT adaptation of the motor model in the "Smoothing" (p1795) field.

###### Function diagrams (FD)

Technology functions - kT estimator - 7008 -

###### Additional parameters

- [r0035](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0035-co-temperature-input)
- [r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)
- [r0334](SINAMICS%20Parameter%20SERVO.md#r03340n-actual-motor-torque-constant-1)
- [r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1).1

---

#### Technology controller

This section contains information on the following topics:

- [Overview](#overview-8)
- [Technology motorized potentiometer](#technology-motorized-potentiometer)
- [Technology fixed setpoints](#technology-fixed-setpoints)
- [Technology setpoints / actual values](#technology-setpoints-actual-values)
- [Technology PID controller](#technology-pid-controller)

##### Overview

###### Description

Simple closed-loop control functions can be implemented with the technology controller, e.g.:

- Level control
- Temperature control
- Dancer roll position control
- Pressure control
- Flow control
- Simple closed-loop controls without higher-level controller
- Tension control

The technology controller is designed as a PID controller. Whereby the derivative-action element can be switched to the control deviation channel or the actual value channel (factory setting). The P, I, and D components can be set separately. A value of 0 deactivates the corresponding component. Setpoints can be specified via two connector inputs. Setpoints can be scaled via parameters. A ramp-function generator in the setpoint channel can be used to set the setpoint ramp-up/ramp-down time via parameters. The setpoint and actual value channels each have a smoothing element. The smoothing time can be set via parameters.

###### Requirement

- The "Technology controller" function module is activated (see [Function modules (servo)](#function-modules-servo)).

###### Properties of the technology controller

- Two scalable setpoints
- Scalable output signal
- Integrated fixed values
- Integrated motorized potentiometer
- The output limits are activated and deactivated via the ramp-function generator.
- The D component can be switched to the control deviation or actual value channel.
- The motorized potentiometer of the technology controller is active only when the drive pulses are enabled.

##### Technology motorized potentiometer

This section contains information on the following topics:

- [Technology motorized potentiometer (servo)](#technology-motorized-potentiometer-servo)
- [Motorized potentiometer ramp-function generator (servo)](#motorized-potentiometer-ramp-function-generator-servo)

###### Technology motorized potentiometer (servo)

###### Description

The motorized potentiometer enables a setpoint to be specified for the technology controller. The setpoint is specified via a ramp-function generator.

###### Requirement

- The "Technology controller" function module is active.

###### Parameterizing the technology controller motorized potentiometer

1. Interconnect the "Setpoint higher" signal source ([p2235](SINAMICS%20Parameter%20SERVO.md#p22350n-bi-technology-controller-motorized-potentiometer-raise-setpoint)) to increase the setpoint.
2. Interconnect the "Setpoint lower" signal source ([p2236](SINAMICS%20Parameter%20SERVO.md#p22360n-bi-technology-controller-motorized-potentiometer-lower-setpoint)) to decrease the setpoint.
3. Correct the specified value for the upper limit of the speed setpoint in % in the "Maximum value" field ([p2237](SINAMICS%20Parameter%20SERVO.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)).
4. Correct the specified value for the lower limit of the speed setpoint in % in the "Minimum value" field ([p2238](SINAMICS%20Parameter%20SERVO.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).
5. Configure the ramp-function generator of the motorized potentiometer (see "[Motorized potentiometer ramp-function generator](#motorized-potentiometer-ramp-function-generator-servo)").
6. To save the setpoint after switching the motor off, select "Yes" in the "Saving active" drop-down list.
7. To save the setpoint retentively, select "Yes" in the "Save retentively active" drop-down list.
8. Interconnect the "Setpoint after RFG" ([r2250](SINAMICS%20Parameter%20SERVO.md#r2250-co-technology-controller-motorized-potentiometer-setpoint-after-rfg)) signal sink to display the effective setpoint after the internal ramp-function generator for the motorized potentiometer of the technology controller.

###### Function diagrams (FD)

- Technology controller - Motorized potentiometer (r0108.16 = 1) - 7954 -

###### Additional parameters

---

###### Motorized potentiometer ramp-function generator (servo)

###### Description

The ramp-function generator ramps the setpoint up and down without acceleration jumps. The ramp-function generator is parameterized via the ramp-up time and ramp-down time parameters. The times refer to the time needed to reach the reference setpoint (0% or 100%) in the specified time.

###### Configuring the ramp-function generator

1. Click the "Technology motorized potentiometer" button in the "Ramp-function generator" screen form.

   The "Technology motorized potentiometer ramp-function generator" dialog opens. The initial rounding is active by default.
2. If you do not require an initial rounding, select "No" in the "Initial rounding active" drop-down list.

   The set ramp-up or ramp-down time can be exceeded with the initial rounding.
3. Correct the specified default value in the "Ramp-up time" ([p2247](SINAMICS%20Parameter%20SERVO.md#p22470n-technology-controller-motorized-potentiometer-ramp-up-time)) field.
4. Correct the specified default value in the "Ramp-down time" ([p2248](SINAMICS%20Parameter%20SERVO.md#p22480n-technology-controller-motorized-potentiometer-ramp-down-time)) field.
5. Enter the desired start value for the motorized potentiometer in the "Start value" ([p2240](SINAMICS%20Parameter%20SERVO.md#p22400n-technology-controller-motorized-potentiometer-starting-value)) field.

   This value takes effect when the drive is switched on.
6. Correct the specified maximum value for the motorized potentiometer of the technology controller in the field of the same name ([p2237](SINAMICS%20Parameter%20SERVO.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)).
7. Correct the specified minimum value for the motorized potentiometer of the technology controller in the field of the same name ([p2238](SINAMICS%20Parameter%20SERVO.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).
8. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Function diagrams (FD)

- Technology controller - Motorized potentiometer (r0108.16 = 1) - 7954 -

###### Additional parameters

---

##### Technology fixed setpoints

This section contains information on the following topics:

- [Technology controller fixed setpoints (servo)](#technology-controller-fixed-setpoints-servo)

###### Technology controller fixed setpoints (servo)

###### Description

The fixed setpoints of the technology controller can be selected freely. Fixed setpoints are speed setpoints freely stored by the user.

###### Requirement

- The "Technology controller" function module is active.

###### Selecting fixed setpoints via direct selection

1. Select the "[1] Direct selection" method from the "Fixed value selection method" ([p2216](SINAMICS%20Parameter%20SERVO.md#p22160n-technology-controller-fixed-value-selection-method)) drop-down list:
2. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - Bit 0: [p2220](SINAMICS%20Parameter%20SERVO.md#p22200n-bi-technology-controller-fixed-value-selection-bit-0)
   - Bit 2: [p2221](SINAMICS%20Parameter%20SERVO.md#p22210n-bi-technology-controller-fixed-value-selection-bit-1)
   - Bit 2: [p2222](SINAMICS%20Parameter%20SERVO.md#p22220n-bi-technology-controller-fixed-value-selection-bit-2)
   - Bit 3: [p2223](SINAMICS%20Parameter%20SERVO.md#p22230n-bi-technology-controller-fixed-value-selection-bit-3)
3. Interconnect the "Fixed value selected" ([r2225](SINAMICS%20Parameter%20SERVO.md#r22250-cobo-technology-controller-fixed-value-selection-status-word)) signal sink to display the status of the fixed setpoints (0/1 = off/on).
4. Enter fixed speed setpoints in the "Fixed value 1...4" ([p2201](SINAMICS%20Parameter%20SERVO.md#p22010n-co-technology-controller-fixed-value-1)...[p2204](SINAMICS%20Parameter%20SERVO.md#p22040n-co-technology-controller-fixed-value-4)) fields.

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
5. Click the "Interconnections" button.

   The "Technology fixed setpoint interconnection" dialog opens.
6. Interconnect the "Fixed value 1...15" fixed values (p2201...[p2215](SINAMICS%20Parameter%20SERVO.md#p22150n-co-technology-controller-fixed-value-15)) via the connected signal sources.
7. Once all necessary settings have been made in the dialog, click "Close".

   The dialog closes.
8. Interconnect the "Fixed value active" ([r2224](SINAMICS%20Parameter%20SERVO.md#r2224-co-technology-controller-fixed-value-effective)) signal source to display the active fixed speed setpoint.

###### Selecting fixed setpoints via binary selection

1. Select the "[1] Binary selection" method from the "Fixed value selection method" (p2216) drop-down list:
2. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - Bit 0: p2220
   - Bit 2: p2221
   - Bit 2: p2222
   - Bit 3: p2223
3. Interconnect the "Fixed value selected" (r2225) signal sink to display the status of the fixed setpoints (0/1 = off/on).
4. Enter fixed speed setpoints in the "Fixed value 1...15" (p2201...p2215) fields.

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
5. Click the "Interconnections" button.

   The "Technology fixed setpoint interconnection" dialog opens.
6. Interconnect the "Fixed value 1...15" fixed values (p2201...p2215) via the connected signal sources.
7. Once all necessary settings have been made in the dialog, click "Close".

   The dialog closes.
8. Interconnect the "Fixed value active" (r2224) signal source to display the active fixed speed setpoint.

###### Function diagrams (FD)

- Technology controller - Fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -
- Technology controller - Fixed values, direct selection (r0108.16 = 1 and p2216 = 1) - 7951 -

###### Additional parameters

---

##### Technology setpoints / actual values

This section contains information on the following topics:

- [Technology setpoints / actual values (servo)](#technology-setpoints-actual-values-servo)
- [Technology setpoint ramp-function generator (servo)](#technology-setpoint-ramp-function-generator-servo)

###### Technology setpoints / actual values (servo)

###### Description

SINAMICS contains an integrated technology controller (PID controller) for simple closed-loop control functions such as level control or temperature control. The P, I and D component can each be set and switched off separately. Switching off is performed by entering a "0" in the appropriate parameter ([p2200](SINAMICS%20Parameter%20SERVO.md#p22000n-bi-technology-controller-enable)).

###### Requirement

- The "Technology controller" function module is active.

###### Parameterizing setpoints 1 and 2

1. Interconnect the signal source for setpoint 1 of the technology controller at "Setpoint 1" ([p2253](SINAMICS%20Parameter%20SERVO.md#p22530n-ci-technology-controller-setpoint-1)).

   The PID motorized potentiometer, fixed setpoints, analog inputs or the fieldbus interface can be used as the setpoint source.
2. To scale setpoint 1, enter a value between 0 ... 100% at "Setpoint 1 scaling" ([p2255](SINAMICS%20Parameter%20SERVO.md#p2255-technology-controller-setpoint-1-scaling)).
3. Interconnect the signal source for setpoint 2 of the technology controller at "Setpoint 2" ([p2254](SINAMICS%20Parameter%20SERVO.md#p22540n-ci-technology-controller-setpoint-2)).

   The additional setpoint is added to the main setpoint.
4. To scale setpoint 2, enter a value between 0 ... 100% at "Setpoint 2 scaling" ([p2256](SINAMICS%20Parameter%20SERVO.md#p2256-technology-controller-setpoint-2-scaling)).
5. If required, parameterize the ramp-function generator of the setpoint technology controller (see "[Technology setpoint ramp-function generator (servo)](#technology-setpoint-ramp-function-generator-servo)").
6. Enter a value for the smoothing time in the "Setpoint filter" field ([p2261](SINAMICS%20Parameter%20SERVO.md#p2261-technology-controller-setpoint-filter-time-constant)).

   The setpoint filter is implemented as a PT1 element.

###### Parameterizing the actual value source and the actual value function

1. Interconnect the signal source for actual value of the technology controller at "Actual value" ([p2264](SINAMICS%20Parameter%20SERVO.md#p22640n-ci-technology-controller-actual-value)).
2. In order to apply a smoothing filter to the actual value, enter a value between 0 ... 60 s in the "Actual value filter" field ([p2265](SINAMICS%20Parameter%20SERVO.md#p2265-technology-controller-actual-value-filter-time-constant)).
3. To activate the actual value limit (p2253.3), select the "Yes" option in the "Actual value limit" ([p2252](SINAMICS%20Parameter%20SERVO.md#p2252-technology-controller-configuration).3) drop-down list.
4. To limit the actual value, enter a value for the upper limit in the "Upper limit actual value" ([p2267](SINAMICS%20Parameter%20SERVO.md#p2267-technology-controller-upper-limit-actual-value)) field and a value for the lower limit in the "Lower limit actual value" ([p2268](SINAMICS%20Parameter%20SERVO.md#p2268-technology-controller-lower-limit-actual-value)) field.
5. Select which function is to be used on the actual value in the "Actual value function" ([p2270](SINAMICS%20Parameter%20SERVO.md#p2270-technology-controller-actual-value-function)) drop-down list:

   - Output (y) = input (x)
   - Square root function (square root from x)
   - Square function (x * x)
   - Cubic function (x * x * x)
6. If you want to invert the actual value, select the "Inversion actual value signal" option in the "Actual value inversion (sensor type)" ([p2271](SINAMICS%20Parameter%20SERVO.md#p2271-technology-controller-actual-value-inversion-sensor-type)) drop-down list.
7. Enter a value in [%] for the gain in the "Gain actual value" ([r2269](SINAMICS%20Parameter%20SERVO.md#p2269-technology-controller-gain-actual-value)) field.

###### Function diagrams (FD)

- Technology controller - Closed-loop control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

###### Technology setpoint ramp-function generator (servo)

###### Description

Ramp-up and ramp-down times prevent sudden setpoint jumps and therefore abrupt acceleration. A change at the PID controller input is passed on to the output via a defined ramp.

###### Configuring the ramp-up time and ramp-down time

1. Click the "Ramp-function generator" button in the "Technology setpoints / actual values" screen form.

   The "Technology setpoint ramp-function generator" dialog opens.
2. The "Acceleration/deceleration ramp independent of setpoint sign" option is active by default.

   Deactivate this option if required.
3. Correct the default value in the "Ramp-up time" ([p2257](SINAMICS%20Parameter%20SERVO.md#p2257-technology-controller-ramp-up-time)) field.
4. Correct the default value in the "Ramp-down time" ([p2258](SINAMICS%20Parameter%20SERVO.md#p2258-technology-controller-ramp-down-time)) field.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Function diagrams (FD)

- Technology controller - Closed-loop control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

##### Technology PID controller

This section contains information on the following topics:

- [Technology PID controller (servo)](#technology-pid-controller-servo)
- [Kp/Tn adaptation of the PID controller (servo)](#kptn-adaptation-of-the-pid-controller-servo)
- [Limitation of the PID controller (servo)](#limitation-of-the-pid-controller-servo)

###### Technology PID controller (servo)

###### Description

The technology controller is configured optionally as P, I, PI, or PID controller.

> **Note**
>
> The value 0 deactivates the corresponding controller component.

###### Requirement

- The "Technology controller" function module is active.

###### Configuring the PID controller

To parameterize the PI component of the controller as well as the proportional gain and the integral time, proceed as follows:

1. Enter a value in the "Proportional gain" ([p2280](SINAMICS%20Parameter%20SERVO.md#p2280-technology-controller-proportional-gain)) field.
2. Enter a value in the "Integral time" ([p2285](SINAMICS%20Parameter%20SERVO.md#p2285-technology-controller-integral-time)) field.
3. If you do not require a Kp/Tn adaptation, configure this adaptation vi a downstream dialog (see "[Kp/Tn adaptation of the PID controller (servo)](#kptn-adaptation-of-the-pid-controller-servo)").
4. Click the large button connected to the button for the Kn/Tn adaptation.

   The "PID controller" dialog opens.
5. Interconnect the signal source to hold the integrator for the technology controller at "Hold integrator" ([p2286](SINAMICS%20Parameter%20SERVO.md#p22860n-bi-hold-technology-controller-integrator)).
6. Deactivate the "Integrator independent of Kp" ([p2252](SINAMICS%20Parameter%20SERVO.md#p2252-technology-controller-configuration).1) option to evaluate the integration time of the PID controller with the gain factor Kp (p2280).
7. Enter a value for the "Differentiation" ([p2274](SINAMICS%20Parameter%20SERVO.md#p2274-technology-controller-differentiation-time-constant)).
8. Select one of the following options in the "Technology controller type" ([p2263](SINAMICS%20Parameter%20SERVO.md#p2263-technology-controller-type)) drop-down list:

   - [0] D component in the actual value signal

     The differential component of the controller is used on the actual value signal with this setting. Use the setting, for example, if the actual value signal contains large deflections that have to be cleaned up quickly in the setpoint via the D component in the controller.
   - [1] D component in the control deviation

     The differential component of the controller is used on the setpoint / actual value difference with this setting.
9. Once all necessary settings have been made, click "Close".

   The dialog closes. The settings are accepted on the "Technology PID controller" screen form.
10. Interconnect the signal source for the precontrol at "Precontrol signal" ([p2289](SINAMICS%20Parameter%20SERVO.md#p22890n-ci-technology-controller-precontrol-signal)).
11. Interconnect the signal source for the enabling signal at "Enable" ([p2200](SINAMICS%20Parameter%20SERVO.md#p22000n-bi-technology-controller-enable)).
12. If required, also configure the limits of the PID controller (see "[Limitation of the PID controller (servo)](#limitation-of-the-pid-controller-servo)").
13. If required, correct the interconnection of the "Technology controller output scaling" ([p2296](SINAMICS%20Parameter%20SERVO.md#p22960n-ci-technology-controller-output-scaling)) signal source for scaling the technology controller output.

    Parameter [p2295](SINAMICS%20Parameter%20SERVO.md#p2295-co-technology-controller-output-scaling) is interconnected as default setting. If you want to use a different value for the scaling, change the interconnection.
14. To directly scale the technology controller, enter a value between -100 ... 100% in the "Output scaling" (p2295) field.
15. Interconnect the "Output signal" ([r2294](SINAMICS%20Parameter%20SERVO.md#r2294-co-technology-controller-output-signal)) signal sink to display the output signal of the technology controller.

###### Function diagrams (FD)

- Technology controller - Closed-loop control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

###### Kp/Tn adaptation of the PID controller (servo)

###### Description

You can optionally activate and configure the Kp/Tn adaptation of the PID controller. Whereby, you can specify whether you require only a Kp or only a Tn adaptation or whether you require both adaptations together and have to configure them for your purposes.

###### Configuring the adaptation

The Kp/Tn adaptation is deactivated when calling the "PID controller technology" screen form the first time. If you want to use an adaptation, proceed as follows:

1. Select the "[1] Yes" option in both drop-down lists below the "Kp/Tn adaptation" button. If you only want to use one of the two adaptations, only select the Yes option in the appropriate drop-down list.

   The "Kp/Tn adaptation" button is switched active.
2. Click the "Kp/Tn adaptation" button.

   The configuration dialog with the same name opens. The configuration options in the dialog depend on whether you have activated only one or both adaptation options. The activation of both adaptations is assumed in the following.
3. Interconnect the "Kp scaling" ([p2315](SINAMICS%20Parameter%20SERVO.md#p2315-ci-technology-controller-kp-adaptation-scaling-signal-source)) signal source for scaling the result of the adaptation of the proportional gain Kp for the technology controller.
4. Interconnect the "Kp input value" ([p2310](SINAMICS%20Parameter%20SERVO.md#p2310-ci-technology-controller-kp-adaptation-input-value-signal-source)) signal source for the input value of the adaptation of the proportional gain Kp for the technology controller.
5. Correct the specified values in the fields:

   - "Upper Kp starting point" ([p2314](SINAMICS%20Parameter%20SERVO.md#p2314-technology-controller-kp-adaptation-upper-starting-point))
   - "Upper Kp value" ([p2312](SINAMICS%20Parameter%20SERVO.md#p2312-technology-controller-kp-adaptation-upper-value))
   - "Lower Kp value" ([p2311](SINAMICS%20Parameter%20SERVO.md#p2311-technology-controller-kp-adaptation-lower-value))
   - "Lower Kp starting point" ([p2313](SINAMICS%20Parameter%20SERVO.md#p2313-technology-controller-kp-adaptation-lower-starting-point))
6. Interconnect the "Tn input value" ([p2317](SINAMICS%20Parameter%20SERVO.md#p2317-ci-technology-controller-tn-adaptation-input-value-signal-source)) signal source for the input value of the adaptation of the integral time Tn for the technology controller.
7. Correct the specified values in the fields:

   - "Upper Tn starting point" ([p2321](SINAMICS%20Parameter%20SERVO.md#p2321-technology-controller-tn-adaptation-upper-starting-point))
   - "Lower Tn value" ([p2319](SINAMICS%20Parameter%20SERVO.md#p2319-technology-controller-tn-adaptation-lower-value))
   - "Upper Tn value" ([p2318](SINAMICS%20Parameter%20SERVO.md#p2318-technology-controller-tn-adaptation-upper-value))
   - "Lower Tn starting point" ([p2320](SINAMICS%20Parameter%20SERVO.md#p2320-technology-controller-tn-adaptation-lower-starting-point))
8. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Additional parameters

---

###### Limitation of the PID controller (servo)

###### Description

For some applications, the PID output variable must be limited to defined values. This can be achieved using fixed limits. To prevent large jumps of the PID controller output when the device is switched on, these PID output limits will be ramped-up via the ramp time from 0 to the appropriate values (upper limit for the PID output or lower limit for the PID output). As soon as the limits are reached, the dynamic response of the PID controller is no longer limited by this ramp-up/ramp-down time.

> **Note**
>
> The limits are entered in [%].

###### Configuring the PID controller limits

1. Click the "Controller limited" button.  
   The "Technology PID controller limits" dialog opens.
2. Deactivate the "Output signal without ramp active" ([p2252](SINAMICS%20Parameter%20SERVO.md#p2252-technology-controller-configuration).2) option to reduce the output signal [r2294](SINAMICS%20Parameter%20SERVO.md#r2294-co-technology-controller-output-signal) via the deceleration ramp [p2293](SINAMICS%20Parameter%20SERVO.md#p2293-technology-controller-ramp-upramp-down-time) to zero.
3. Interconnect the "Limit offset" ([p2299](SINAMICS%20Parameter%20SERVO.md#p22990n-ci-technology-controller-limit-offset)) signal source for the offset of the output limiting of the technology controller.
4. Enter a value in the "Maximum limiting" ([p2291](SINAMICS%20Parameter%20SERVO.md#p2291-co-technology-controller-maximum-limiting)) field.
5. Interconnect the "Maximum limiting signal source" ([p2297](SINAMICS%20Parameter%20SERVO.md#p22970n-ci-technology-controller-maximum-limit-signal-source)) for the maximum limiting of the technology controller.
6. Enter a value in the "Minimum limiting" ([p2292](SINAMICS%20Parameter%20SERVO.md#p2292-co-technology-controller-minimum-limiting)) field.
7. Interconnect the "Minimum limiting signal source" ([p2298](SINAMICS%20Parameter%20SERVO.md#p22980n-ci-technology-controller-minimum-limit-signal-source)) for the minimum limiting of the technology controller.
8. Enter a value (in seconds) for the ramp-up and ramp-down time for the output signal of the technology controller in the "Ramp-up/ramp-down time" (p2293) field.
9. Once all necessary settings have been made, click "Close".

   The dialog closes. The settings are accepted on the "Technology PID controller" screen form.

###### Function diagrams (FD)

- Technology controller - Closed-loop control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

### Control logic

#### Definition

The connections for the control and status words are displayed for the drive in the "Control logic" screen form. You can edit these connections:

The connections for the control and status words are arranged in groups. The connections of a group can be displayed in the screen form via two drop-down lists on the left and on the right. Connections can be displayed for the following groups:

- Control word sequence control ([r0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1))
- Control word faults/alarms ([r2138](SINAMICS%20Parameter%20CU.md#r2138715-cobo-control-word-faultsalarms))
- Control word speed controller ([r1406](SINAMICS%20Parameter%20SERVO.md#r1406812-cobo-control-word-speed-controller-1))
- Command Data Set CDS selected ([r0836](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r083603-cobo-command-data-set-cds-selected))
- Status word sequence controls ([r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1))
- Status word faults/alarms 1 ([r2139](SINAMICS%20Parameter%20CU.md#r2139015-cobo-status-word-faultsalarms-1))
- Status word faults/alarms 2 ([r2135](SINAMICS%20Parameter%20CU.md#r2135015-cobo-status-word-faultsalarms-2))
- Status word speed controller ([r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1))
- Status word monitoring 1 ([r2197](SINAMICS%20Parameter%20SERVO.md#r2197113-cobo-status-word-monitoring-1-1))
- Status word monitoring 2 ([r2198](SINAMICS%20Parameter%20SERVO.md#r2198412-cobo-status-word-monitoring-2-1))
- Status word monitoring 3 ([r2199](SINAMICS%20Parameter%20SERVO.md#r2199011-cobo-status-word-monitoring-3-1))
- Encoder control word Gn_STW; Encoder control word Gn_STW ([p0480](SINAMICS%20Parameter%20SERVO.md#p048002-ci-encoder-control-word-gn_stw-signal-source)[0])
- Encoder control word Gn_STW; Encoder control word Gn_STW (p480[1])
- Encoder control word Gn_STW; Encoder control word Gn_STW (p480[2])
- Encoder status word Gn_ZSW; Encoder 1 ([r0481](SINAMICS%20Parameter%20SERVO.md#r048102-co-encoder-status-word-gn_zsw)[0])
- Encoder status word Gn_ZSW, Encoder 2 (r481[1])
- Encoder status word Gn_ZSW, Encoder 3 (r481[2])
- Status word current controller ([r1408](SINAMICS%20Parameter%20SERVO.md#r140809-cobo-status-word-current-controller))
- Missing enables (r46)
- Status word, closed-loop controls (r56)
- SI status (Control Unit) ([r9772](SINAMICS%20Parameter%20SERVO.md#r9772023-cobo-si-status-control-unit))
- SI status (Motor Module) ([r9872](SINAMICS%20Parameter%20SERVO.md#r9872024-cobo-si-status-list-motor-module))
- SI status (Control Unit + Motor Module) ([r9773](SINAMICS%20Parameter%20SERVO.md#r9773031-cobo-si-status-control-unit-motor-module))
- SI status (group STO) ([r9774](SINAMICS%20Parameter%20SERVO.md#r9774031-cobo-si-status-group-sto))
- SI common functions (Control Unit) ([r9771](SINAMICS%20Parameter%20SERVO.md#r9771-si-common-functions-control-unit))
- SI common functions (Motor Module) ([r9871](SINAMICS%20Parameter%20SERVO.md#r9871-si-common-functions-motor-module))

An illuminated LED display means that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical connection of several signal sources, the type of the logical connection is displayed by the associated logic symbol.

#### Selecting and connecting control and status words

1. Select the desired group of control and status words in the drop-down list (on the left or right in the screen form).

   The corresponding display and connection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.
2. Interconnect the signal sources for the displayed parameters (for control words) or the bits (for status words and missing enables).

#### Function diagrams (FD)

Internal control/status words - Control word sequence control - 2501 -

Internal control/status words - Status word sequence control - 2503 -

Internal control/status words - Control word speed controller - 2520 -

Internal control/status words - Status word speed controller - 2522 -

Internal control/status words - Status word current control - 2530 -

Internal control/status words - Control word faults/alarms - 2546 -

#### Additional parameters

- [p0840](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08400n-bi-on-off-off1)
- [p0844](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1)
- [p0845](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)
- [p0852](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08520n-bi-enable-operationinhibit-operation)
- [p3532](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p3532-bi-infeed-inhibit-motoring)
- [p3533](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p3533-bi-infeed-inhibit-generator-mode)
- [p0854](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08540n-bi-control-by-plcno-control-by-plc)
- [p2103](SINAMICS%20Parameter%20CU.md#p2103-bi-1st-acknowledge-faults)
- [p2104](SINAMICS%20Parameter%20CU.md#p2104-bi-2nd-acknowledge-faults)
- [p2105](SINAMICS%20Parameter%20CU.md#p2105-bi-3rd-acknowledge-faults)
- [p2112](SINAMICS%20Parameter%20CU.md#p2112-bi-external-alarm-1)
- [p2116](SINAMICS%20Parameter%20CU.md#p2116-bi-external-alarm-2)
- [p2117](SINAMICS%20Parameter%20CU.md#p2117-bi-external-alarm-3)
- [p2106](SINAMICS%20Parameter%20CU.md#p2106-bi-external-fault-1)
- [p2107](SINAMICS%20Parameter%20CU.md#p2107-bi-external-fault-2)
- [p2108](SINAMICS%20Parameter%20CU.md#p2108-bi-external-fault-3)
- r0899 (various bits)
- r2139 (various bits)
- [r0046](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0046029-cobo-missing-enable-signal) (various bits)

---

## Diagnostics

This section contains information on the following topics:

- [Missing enables](#missing-enables)
- [Control/status words](#controlstatus-words)
- [Status parameters](#status-parameters)
- [Communication](#communication)

### Missing enables

The drive does not change to the "Operation" state until all enables are present. In the "Missing enables" screen form, the LEDs in the function view indicate which enables are still missing. An illuminated LED display indicates that the corresponding enable is missing.

The bits of the missing enables ([r0046](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0046029-cobo-missing-enable-signal)) are displayed in the screen form.

#### Additional parameters

---

### Control/status words

#### Description

The control and status words are displayed in the function view for diagnostic purposes in the "Control/status words" screen form. The screen form is split into two vertical sections each displaying a group of control and status words in a drop-down list.

The following groups can be displayed:

- Control word sequence control ([r0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1))
- Control word faults/alarms ([r2138](SINAMICS%20Parameter%20CU.md#r2138715-cobo-control-word-faultsalarms))
- Control word speed controller ([r1406](SINAMICS%20Parameter%20SERVO.md#r1406812-cobo-control-word-speed-controller-1))
- Status word sequence control ([r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1))
- Status word faults/alarms 1 ([r2139](SINAMICS%20Parameter%20CU.md#r2139015-cobo-status-word-faultsalarms-1))
- Status word faults/alarms 2 ([r2135](SINAMICS%20Parameter%20CU.md#r2135015-cobo-status-word-faultsalarms-2))
- Status word speed controller ([r1407](SINAMICS%20Parameter%20SERVO.md#r1407028-cobo-status-word-speed-controller-1))
- Status word monitoring functions 1 ([r2197](SINAMICS%20Parameter%20SERVO.md#r2197113-cobo-status-word-monitoring-1-1))
- Status word monitoring functions 2 ([r2198](SINAMICS%20Parameter%20SERVO.md#r2198412-cobo-status-word-monitoring-2-1))
- Status word monitoring functions 3 ([r2199](SINAMICS%20Parameter%20SERVO.md#r2199011-cobo-status-word-monitoring-3-1))
- Status word current controller ([r1408](SINAMICS%20Parameter%20SERVO.md#r140809-cobo-status-word-current-controller))
- Status word closed-loop control ([r0056](SINAMICS%20Parameter%20SERVO.md#r0056115-cobo-status-word-closed-loop-control))

#### Selecting a group of control and status words

1. Select the desired group of control and status words in one of the two drop-down lists.

   The corresponding display and connection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.

   A highlighted LED display means that the corresponding bit of the control or status word has been set.
2. If you want to display the values of several groups next to one another, set the other desired groups in the other two drop-down lists.

#### Function diagrams (FD)

- Internal control/status words - Control word setpoint channel - 2505 -
- Internal control/status words - Status word monitoring functions 1 - 2534 -
- Internal control/status words - Status word monitoring functions 3 - 2537 -
- Internal control/status words - Control word faults/alarms - 2546 -
- Internal control/status words - Status word faults/alarms 1 and 2 - 2548 -
- Internal control/status words - Control word sequence control - 2501 -
- Internal control/status words - Status word sequence control - 2503 -
- Internal control/status words - Status word speed controller - 2522 -
- Internal control/status words - Status word closed-loop control - 2526 -
- Internal control/status words - Status word current control - 2530 -
- Internal control/status words - Status word monitoring functions 2 - 2536 -

#### Additional parameters

---

### Status parameters

This dialog displays the values of important parameters, which characterize the operating state of the converter.

The displayed parameters depend on the selected drive object.

More detailed information about the parameters can be found in the following sources:

- Help for the respective parameter
- SINAMICS S120/S150 List Manual

### Communication

This section contains information on the following topics:

- [S120 SERVO drive telegrams receive direction](#s120-servo-drive-telegrams-receive-direction)
- [S120 SERVO drive telegrams send direction](#s120-servo-drive-telegrams-send-direction)
- [Servo PZD Send/Receive Direction Diagnostics](#servo-pzd-sendreceive-direction-diagnostics)

#### S120 SERVO drive telegrams receive direction

##### Description

Here you specify the interconnections of the PROFIdrive telegram in the receive direction for the servo drive object.

Use the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) to change the configuration of the telegrams.  
You can also add Safety Integrated telegrams or telegram extensions. The content of these telegrams is then displayed in the areas "PROFIsafe" and "Telegram extension".

**Telegram structure**

If you use PROFIsafe signals, these are displayed in a separate block.

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the receive direction.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853827083_DV_resource.Stream@PNG-en-US.png) | Click the button next to "Interconnections" to interconnect the signal for the connector output. |
| ![Description](images/147860084491_DV_resource.Stream@PNG-en-US.png) | Click the button to display and interconnect the signal bit by bit. |

The following information of the displayed telegrams is displayed:

| Telegram type | PZD | Display of the value | Format switchover | Control words | Interconnections |
| --- | --- | --- | --- | --- | --- |
|  | The numbering and arrangement of the process data. | Value of the process data (PZD) | Switching the value of the process data to a different display (hex, bin, dec). | List of the control words that are transmitted in the telegram. | Display or interconnection of the parameter with which the signal is to be interconnected. Several interconnections are possible. |
| PROFIsafe  30, 31, 901, 902, 903 | X | X | X | X | ‑ |
| PROFIdrive  7, 9, 110, 111 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### S120 function diagrams (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - Standard telegrams and process data 1 - 2415 -
- PROFIdrive - Standard telegrams and process data 2 - 2416 -
- PROFIdrive - Manufacturer-specific telegrams and process data 1 - 2419 -
- PROFIdrive - Manufacturer-specific telegrams and process data 2 - 2420 -
- PROFIdrive - Manufacturer-specific telegrams and process data 3 - 2421 -
- PROFIdrive - Manufacturer-specific telegrams and process data 4 - 2422 -
- PROFIdrive - Supplementary telegrams/free telegrams and process data - 2423 -
- PROFIdrive - STW1_BM control word metal industry interconnection - 2425 -
- PROFIdrive - STW2_BM control word metal industry interconnection - 2426 -
- PROFIdrive - ZSW1_BM status word metal industry interconnection - 2428 -
- PROFIdrive - ZSW2_BM status word metal industry interconnection - 2429 -
- PROFIdrive - PZD receive signals profile-specific interconnection - 2439 -
- PROFIdrive - PZD receive signals manufacturer-specific interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals profile-specific interconnection - 2449 -
- PROFIdrive - PZD send signals manufacturer-specific interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - IF1 receive telegram free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - IF1 status words free interconnection - 2472 -
- PROFIdrive - IF1 receive telegram free interconnection via BICO (p0922 = 999) - 2481 -
- PROFIdrive - IF2 receive telegram free interconnection - 2485 -
- PROFIdrive - IF2 status words free interconnection - 2489 -
- PROFIdrive - IF2 receive telegram free interconnection - 2491 -
- PROFIdrive - CU_STW1 control word 1 Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - STW1 control word 1 interconnection (r0108.4 = 1) - 2475 -
- PROFIdrive - SATZANW block selection interconnection (r0108.4 = 1) - 2476 -
- PROFIdrive - ZSW1 status word 1 interconnection (r0108.4 = 1) - 2479 -
- PROFIdrive - MDI_MOD MDI mode interconnection (r0108.4 = 1) - 2480 -
- PROFIdrive - POS_STW positioning control word interconnection (r0108.4 = 1) - 2462 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection (r0108.4 = 1) - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection (r0108.4 = 1) - 2464 -
- PROFIdrive - POS_ZSW1 positioning status word 1 interconnection (r0108.4 = 1) - 2466 -
- PROFIdrive - POS_ZSW2 positioning status word 2 interconnection (r0108.4 = 1) - 2467 -
- SI PROFIsafe - Standard telegrams - 2915 -
- SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

#### S120 SERVO drive telegrams send direction

##### Description

Here you specify the parameters of the PROFIdrive telegram in the send direction for the drive.

Use the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) to change the configuration of the telegrams.  
You can also add Safety Integrated telegrams or telegram extensions. The content of these telegrams is then displayed in the areas "PROFIsafe" and "Telegram extension".

**Telegram structure**

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the send direction.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853860363_DV_resource.Stream@PNG-en-US.png) | Click the button next to "Interconnections" on the left to interconnect the signal for the connector input. |

The following information of the displayed telegrams is displayed:

| Telegram type | Interconnections | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- | --- |
|  | Display or interconnection of the parameter with which the signal is to be interconnected or is interconnected. | List of the status words that are transmitted in the telegram. | Value of the process data (PZD) | Switching the value of the process data to a different display (hex, bin, dec). | Numbering and arrangement of the process data. |
| PROFIsafe  30, 31, 901, 902, 903 | ‑ | X | X | X | X |
| PROFIdrive  7, 9, 110, 111 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### S120 function diagrams (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - Standard telegrams and process data 1 - 2415 -
- PROFIdrive - Standard telegrams and process data 2 - 2416 -
- PROFIdrive - Manufacturer-specific telegrams and process data 1 - 2419 -
- PROFIdrive - Manufacturer-specific telegrams and process data 2 - 2420 -
- PROFIdrive - Manufacturer-specific telegrams and process data 3 - 2421 -
- PROFIdrive - Manufacturer-specific telegrams and process data 4 - 2422 -
- PROFIdrive - Supplementary telegrams/free telegrams and process data - 2423 -
- PROFIdrive - STW1_BM control word metal industry interconnection - 2425 -
- PROFIdrive - STW2_BM control word metal industry interconnection - 2426 -
- PROFIdrive - ZSW1_BM status word metal industry interconnection - 2428 -
- PROFIdrive - ZSW2_BM status word metal industry interconnection - 2429 -
- PROFIdrive - PZD receive signals profile-specific interconnection - 2439 -
- PROFIdrive - PZD receive signals manufacturer-specific interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals profile-specific interconnection - 2449 -
- PROFIdrive - PZD send signals manufacturer-specific interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - IF1 send telegram free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - IF1 status words free interconnection - 2472 -
- PROFIdrive - IF1 send telegram free interconnection via BICO (p0922 = 999) - 2483 -
- PROFIdrive - IF2 send telegram free interconnection - 2487 -
- PROFIdrive - IF2 status words free interconnection - 2489 -
- PROFIdrive - IF2 send telegram free interconnection - 2493 -
- PROFIdrive - CU_STW1 control word 1 Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - STW1 control word 1 interconnection (r0108.4 = 1) - 2475 -
- PROFIdrive - SATZANW block selection interconnection (r0108.4 = 1) - 2476 -
- PROFIdrive - ZSW1 status word 1 interconnection (r0108.4 = 1) - 2479 -
- PROFIdrive - MDI_MOD MDI mode interconnection (r0108.4 = 1) - 2480 -
- PROFIdrive - POS_STW positioning control word interconnection (r0108.4 = 1) - 2462 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection (r0108.4 = 1) - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection (r0108.4 = 1) - 2464 -
- PROFIdrive - POS_ZSW1 positioning status word 1 interconnection (r0108.4 = 1) - 2466 -
- PROFIdrive - POS_ZSW2 positioning status word 2 interconnection (r0108.4 = 1) - 2467 -
- SI PROFIsafe - Standard telegrams - 2915 -
- SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

#### Servo PZD Send/Receive Direction Diagnostics

##### Description

You can display a diagnosis of the status or control words of the selected telegram here.

##### Function diagrams (FD)

- PROFIdrive - PZD receive signals profile-specific interconnection - 2439 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 1) - 2443 -
- PROFIdrive - POS_STW positioning control word interconnection (r0108.4 = 1) - 2462 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection (r0108.4 = 1) - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection (r0108.4 = 1) - 2464 -
- PROFIdrive - POS_ZSW1 positioning status word 1 interconnection (r0108.4 = 1) - 2466 -
- PROFIdrive - POS_ZSW2 positioning status word 2 interconnection (r0108.4 = 1) - 2467 -
- SI PROFIsafe - Standard telegrams - 2915 -
- SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

## Rotate & optimize

This section contains information on the following topics:

- [Control panel](#control-panel)
- [One Button Tuning (servo)](#one-button-tuning-servo)
- [Stationary/rotating measurement](#stationaryrotating-measurement)
- [Data set switchover](#data-set-switchover)

### Control panel

#### Overview

You can use the control panel to traverse the drive and therefore test the settings that have been made.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life in the event of non-observance of the safety instructions for the drive control panel**  The safety shutdowns from the higher-level controller have no effect with this function. The **Stop with spacebar** function is not guaranteed in all operating modes. Incorrect operation by untrained personnel and non-observance of the appropriate safety instructions can result in death or serious injury.   - Make sure that this function is only used for commissioning, diagnostic and service purposes. - Make sure that this function is only used by trained and authorized skilled personnel. - Make sure that a hardware device is always available for the EMERGENCY OFF circuit. |  |

> **Note**
>
> **Drive reacts immediately**
>
> Although all enables are removed before returning the master control, the setpoints and commands still come from the original parameterized sources after the control priority is returned.

#### Requirements

- An online connection to the drive has been established.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Activating the master control

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active after you have activated the control panel and set the enables.

> **Note**
>
> **Control panel locked in torque control mode**
>
> The control panel cannot be activated for drives with torque control mode (p1300 = 23).

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> In addition, as a result of inactivity, the automatic project lock is not activated as long as the control panel is active.

When you activate the control panel, you assume master control of the drive. The master control can only be activated for one drive:

| Symbol | Meaning |
| --- | --- |
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

#### Activating the infeed

> **Note**
>
> **No infeed is available.**
>
> If no infeed is available in the device configuration, the switch-on and switch-off icons for the infeed also are not available in the "Control panel" screen form.

If an infeed is available in your drive, then the infeed must also be activated. If it is not activated, no further drive enable can be set.

1. Click the "1" icon at "Infeed" to activate the infeed.

#### Setting the enable

To set the required enable for the control panel, proceed as follows.

1. Click the "Set" button under "Drive enables".

   Further areas of the control panel are activated.
2. Click the "Acknowledge faults" button to acknowledge the currently pending faults.
3. If you no longer require the enables, click the "Reset" button under "Drive enables".

#### Deactivating the master control

When you deactivate the control panel, you return the master control:

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the control panel.
2. Click the "Deactivate" button under "Master control".

   The grayed-out user interface of the control panel indicates that the master control is deactivated.

#### Result

You can now traverse the drive with the control panel. Enables and faults are displayed at "Drive status". In addition to "Active fault", the currently pending fault is displayed.

---

**See also**

[Control panel](Configuring%20SINAMICS%20S-G-MV%20drives.md#control-panel)

### One Button Tuning (servo)

#### Overview

An important part of basic commissioning is performed using One Button Tuning (abbreviated: OBT). With "One Button Tuning", the mechanical drive train is measured with the aid of short test signals. In this way, the controller parameters can be optimally adapted to the existing mechanical system. The optimum controller settings can be determined with a few entries using One Button Tuning.

**Restrictions**

- Only the motor measuring system is taken into account for the optimization of the position controller. If an external measuring system is used for the position control, this can result in an unstable controller setting.
- The "One Button Tuning" function also does not support different sampling times for current controllers and speed/velocity controllers. For this reason, do not use the "One Button Tuning" function for this configuration.

#### Requirements

- There is an online connection to the drive unit.
- A SERVO drive is being used.

  One Button Tuning is not available for modules with vector control (e.g. SINAMICS S150).
- The "Advanced Position Control" (APC) function module is deactivated.   
  APC should generally only be performed after the OBT.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Assuming master control

When an online connection has been established, the bar in the screen form header is highlighted in color. The control elements are grayed-out and deactivated apart from the "Activate" button. The remaining control elements become active after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> In addition, as a result of inactivity, the automatic project lock is not activated as long as the control panel is active.

Proceed as follows to activate the master control:

| Symbol | Meaning |
| --- | --- |
| 1. If the master control is still not active, click on "Activate" under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully and check the value for the monitoring time. Adjust the value as required.     The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury. - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

#### Activating the infeed

> **Note**
>
> **No infeed is available.**
>
> If no infeed is available in the device configuration, the switch-on and switch-off icons for the infeed also are not available in the "Control panel" screen form.

If an infeed is available in your drive, then the infeed must also be activated. If it is not activated then Auto Servo Tuning cannot be performed.

1. Click the "1" icon at "Infeed" to activate the infeed.

#### Performing the settings for the tuning

1. Select the desired dynamic response setting for the One Button Tuning corresponding to the mechanical system of your machine.

   One Button Tuning optimizes the drive based on the selected dynamic response setting.

   - Conservative

     Slow control – low mechanical load.
   - Standard

     Best compromise between fast speed control and low mechanical load.
   - Dynamic

     Fast speed control – high mechanical load.
   - Dynamic response factor

     Fast speed control with manual definition of the dynamic response factor (factory setting: 80%).

     For S120 with CU310-2 PN, setting the dynamic response factor is not listed.
2. Enter the angle in the "Distance limit" field through which the motor and the connected machine are permitted to turn for the required measurements (e.g. 360°) without their mechanical system being damaged.

   The angle should be at least 60° in order to be able to determine useful controller parameters. Generally, longer traversing distances result in better optimization results.
3. Should you wish to perform advanced settings, click on the "Advanced settings" button.

   The "Configuration" dialog opens. The table in the dialog indicates the default settings which you can change for a number of parameters.
4. Correct the defaults in the dialog for each required parameter.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

#### Starting One Button Tuning

Once all necessary default settings have been made, you can initiate One Button Tuning:

1. To read out the drive technical data for One Button Tuning, in the "Optimization" area, click "Start".

   The optimization function determines all actual values of the drive required for the tuning.
2. Click the "1" icon at "Switch on" to start the tuning.

   One Button Tuning is initiated.
3. Save the project when the tuning was successful.

#### Result

The result of the optimization is displayed in the "Status" area. If the optimization was successful, the corresponding LED lights up in green. The "Optimization result" list compares the settings changed by the optimization with the earlier settings prior to tuning.

If the optimization was not successful, repeat the optimization with changed specifications, if applicable.

#### Deactivating the master control

Following conclusion of the optimization, the master control can be returned as follows:

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the master control.
2. Click the "Deactivate" button under "Master control".

   The "Deactivate master control" message window opens.
3. If you really want to deactivate the master control, click on "Yes".

   The grayed-out user interface of the "Deactivate" button indicates that the master control is deactivated.

---

**See also**

[One Button Tuning (SERVO drive)](Configuring%20SINAMICS%20S-G-MV%20drives.md#one-button-tuning-servo-drive)

### Stationary/rotating measurement

This section contains information on the following topics:

- [Motor data identification](#motor-data-identification)
- [Stationary/rotating measurement (servo)](#stationaryrotating-measurement-servo)
- [Stationary measurement (servo)](#stationary-measurement-servo)
- [Rotating measurement (servo)](#rotating-measurement-servo)
- [Encoder adjustment (servo)](#encoder-adjustment-servo)

#### Motor data identification

##### Overview

The motor identification (MotID) helps with determining the motor data, for example, for third-party motors. The MotID should be performed to improve the control properties of the motor. In particular for the encoderless vector control, at least the stator resistance (including the supply cable resistance) and the power unit parameters must be determined for each drive. This is required so that the observer model can operate correctly even for very low speeds.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Damage to the device as a result of incorrectly selected rated current and/or maximum current values**  Incorrect rated current or maximum current data can destroy the motor!  - Check that the entered current values are correct. |  |

> **Note**
>
> If a POWER ON or a warm restart is performed when motor data identification is selected, the motor data identification request is lost. A desired motor data identification must be reselected manually after ramp-up.

> **Note**
>
> While a turning measurement is selected and running, you cannot perform any upload, download, RAM2ROM or reset to the factory settings. This means you cannot load the data into the PG with a second PG or a new project. This is possible only after a power ON/OFF.

**Dependencies and limitations**

- The OFF1, OFF2 and OFF3 enable signals and "Enable operation" are effective.
- Speed limitation ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)) is effective.
- Current limitation ([p0640](SINAMICS%20Parameter%20SERVO.md#p06400n-current-limit)) is effective.
- Observe the rotation direction block ([p1959](SINAMICS%20Parameter%20SERVO.md#p19590n-rotating-measurement-configuration-1).14,15) if it was activated before the start of the measurement. For a stationary measurement, the rotation direction block is used for the "test commutation angle and rotational direction" (p1959.13) partial measurement.
- The rotation direction block is not used for the stationary measurement when the encoder has been incorrectly adjusted and also for encoderless operation. In these two cases, an electrical alignment movement of up to 180 degrees is possible.
- The ramp-up and -down times set in the [p1958](SINAMICS%20Parameter%20SERVO.md#p19580n-rotating-measurement-ramp-upramp-down-time-1) are always considered provided p1958 ≥ 0.
- If p1958 = -1, the maximum of the ramp-up and ramp-down time set for the [p1120](SINAMICS%20Parameter%20SERVO.md#p11200n-ramp-function-generator-ramp-up-time-1) and [p1121](SINAMICS%20Parameter%20SERVO.md#p11210n-ramp-function-generator-ramp-down-time-2) parameters is used provided the extended setpoint channel function module is active.

##### Layout of the dialog

- **Measurement type:** Allows the measurement type to be selected
- **Configuration**: To enter the configuration data and perform the measurement
- **Status**: To follow the progress of the measurement (parameter [r0047](SINAMICS%20Parameter%20SERVO.md#r0047-identification-status))
- **Measurement result**: To view, correct and accept the MotID results

##### Motor data identification procedure

1. Configure the motor data.
2. Enter encoder data.
3. Perform the motor identification for a cold motor.
4. Perform a stationary measurement, see [Servo stationary measurement](#stationary-measurement-servo).
5. Perform a rotating measurement for a motor running without load, see [Servo rotating measurement](#rotating-measurement-servo).

   For the rotating measurement, the motor should be disconnected from the machine in order to prevent serious mechanical damage.
6. Calculate the motor and control parameters using [p0340](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0340-automatic-calculation-control-parameters).

   After calculation of the controller data, p0340 will be initialized correctly (p0340 = 1 or p0340 = 3) and written after the download.

##### Additional parameters

---

---

**See also**

[Encoder adjustment (servo)](#encoder-adjustment-servo)

#### Stationary/rotating measurement (servo)

##### Overview

The "Measurement type" setting range shows the available measurement types. When the screen form is opened, a check is made to determine whether a measurement is already active and, if so, it will be displayed. If no measurement is selected, a check is made as to which measurement has already been performed and then used as a recommendation.

After performing the basic parameter assignment and the subsequent download, the selection in the measuring type is set to "stationary measurement", because the "complete calculation of the motor/control parameters" has already been performed. The selection list is not active, but the measurement is active ("Deactivate" button can be activated). The next step then involves performing the measurement.

##### Requirements

- An online connection to the drive has been established.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

##### Activating the master control

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> In addition, as a result of inactivity, the automatic project lock is not activated as long as the control panel is active.

The master control can only be activated for one drive.

| Symbol | Meaning |
| --- | --- |
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully and check the value for the monitoring time.     The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

##### Configuring and performing the motor data identification

When you open the screen form in online mode, the drive control panel that you require for the measurement is displayed automatically.

1. Click the "1" icon in the "Infeed" area to switch on the infeed.
2. To set the drive enable signals, click "Set" in the "Drive enables" area.
3. Click the "1" icon in the "Switch on" area to switch on the motor.
4. Click the "Activate" button in the "Measurement" area to start the measurement.

   The center of the screen form contains the status display that shows the progress of the measurement (parameter [r0047](SINAMICS%20Parameter%20SERVO.md#r0047-identification-status)).

   The measurement ends independently and a message appears stating that the drive is in the "Switching on inhibited" state.

   After the measurement, the new parameter values are displayed in the results table. You can view and check the new values.
5. Check the values that have been determined to ensure that they are plausible. If the values do not seem appropriate, perform another measurement.
6. If you do not want to perform any more measurements, click the "0" icon in the motor and infeed area. Then click "Deactivate" under "Master control".

##### Selecting measurements yourself (for experts)

> **Note**
>
> **Manually selecting the measurement type**
>
> We only recommend to experienced users that they manually select the measurement type from the list. "Detail values" must be defined in the configuration dialog box for the measurement types "Stationary measurement", "Encoder adjustment", and "Rotating measurement". Precise instructions for making these settings are described further on in this chapter. The results of the respective measurements are displayed in a table in the "Stationary/rotating measurement" screen form.

The specified measurement types depend on the motor.

1. Perform the measurement as described above.

##### NOTES

- For linear motors, [p1959](SINAMICS%20Parameter%20SERVO.md#p19590n-rotating-measurement-configuration-1) is pre-set so that only the q inductance and the high inertia mass are measured (p1959.5 = 1 and p1959.10 = 1), as generally the travel limits do not permit longer traversing distances in one direction.
- If the encoder inversion is changed using MotID, fault F07993 is output, which refers to a possible change in the direction of rotation and can only be acknowledged by [p1910](SINAMICS%20Parameter%20SERVO.md#p1910-motor-data-identification-routine-stationary-standstill) = 2.
- The encoder pulse number ([r1973](SINAMICS%20Parameter%20SERVO.md#r197301-encoder-pulse-number-identified)) is only determined with a very high degree of inaccuracy ([p0407](SINAMICS%20Parameter%20SERVO.md#p04070n-linear-encoder-grid-division)/[p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number)) and is only suitable for making rough checks. The sign is negative if inversion is required ([p0410](SINAMICS%20Parameter%20SERVO.md#p04100n-encoder-inversion-actual-value-1).0).
- If the motor is operated on a load with large moment of inertia compared with the motor, to determine the overall moment of inertia the turning measurement can also be performed with load, however, in this case, only the determination of the moment of inertia (p1959.2) should be activated. The moment of inertia is used for precontrol only in encoderless operation.
- A load gearbox is not considered for the determination of the moment of inertia. The moment of inertia that acts on the motor side is determined. A distribution of the measured moment of inertia to motor and load is not possible, because such a distribution cannot be evaluated.

##### Recommendations

You can make additional settings if the mechanics allow:

- Perform stationary measurement for open brake ([p1215](SINAMICS%20Parameter%20SERVO.md#p1215-motor-holding-brake-configuration) = 2)
- Enable both directions of rotation (p1959.14,15)
- Set ramp-up/ramp-down time to zero ([p1958](SINAMICS%20Parameter%20SERVO.md#p19580n-rotating-measurement-ramp-upramp-down-time-1))
- Activate kT estimator

If the mechanical system does not permit this, the following restrictions apply:

| Restriction | Description |
| --- | --- |
| Brake closed | Commutation angle and encoder sign are not determined |
| Direction of rotation disable active | Reluctance torque constant is not determined |
| Ramp-up/ramp-down time active | Moment of inertia is determined with reduced accuracy. Reluctance torque constant and Lq characteristic are not determined |
| Extended torque control ([r0108](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0108-drive-objects-function-module-1).1) and compensation of the voltage emulation error ([p1780](SINAMICS%20Parameter%20SERVO.md#p17800n-motor-model-adaptation-configuration-2).8) deactivated | Converter emulation errors are not determined |

##### Additional parameters

---

#### Stationary measurement (servo)

##### Description

Here you can enter the data for the stationary measurement for the motor data identification or view the determined data.

The stationary motor data identification can result in slight movement of up to 210 degrees electrical.

For the rotating motor data identification routine, motor motion is initiated, which can reach the maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)) and the motor torque corresponding to the maximum current ([p0640](SINAMICS%20Parameter%20SERVO.md#p06400n-current-limit)).

The rotating measurement should be carried out with a motor running at no load (de-coupled from the mechanical system) in order to prevent damage/destruction to the load or be influenced by the load. If the motor cannot be de-coupled from the mechanical system, then the stress on the mechanical system can be reduced by parameterizing the ramp-up time ([p1958](SINAMICS%20Parameter%20SERVO.md#p19580n-rotating-measurement-ramp-upramp-down-time-1)) and/or using direction limiting ([p1959](SINAMICS%20Parameter%20SERVO.md#p19590n-rotating-measurement-configuration-1).14/p1959.15) or using the current and speed limit.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected motor motion during motor data identification**  Motor motion caused by the motor data identification routine can result in death, severe injury or material damage.  - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. - Do not carry out the rotating measurement if the traversing distance is mechanically limited. |  |

##### Enter configuration data

1. Click "Configuration" to enter the parameter values required for the stationary measurement.
2. Enter the parameter values required for the stationary measurement.

   - [p0352](SINAMICS%20Parameter%20SERVO.md#p03520n-cable-resistance): Cable resistance (important for long motor cables)
   - [p0353](SINAMICS%20Parameter%20SERVO.md#p03530n-motor-series-inductance): Series inductance (important for long motor cables)
   - p0640: Current limit
   - [p1909](SINAMICS%20Parameter%20SERVO.md#p19090n-motor-data-identification-control-word-1): Motor identification control word
   - p1959: Rotating measurement configuration
   - [p1780](SINAMICS%20Parameter%20SERVO.md#p17800n-motor-model-adaptation-configuration-2).8: Compensation of the voltage emulation errors in the converter (only for synchronous motor)

   The p1909 and p1959 parameters can be used to select or deselect individual measurements of the motor identification if not all measurements should or can be performed.

**Perform measurement**

A detailed description of how you can perform the measurement is contained in [Stationary/rotating measurement](#motor-data-identification).

**Determined quantities**

The following quantities are determined for the motor data identification with stationary measurement depending on the used motor:

| Symbol | Meaning |
| --- | --- |
| **Synchronous motor** | **Induction motor** |
| Commutation angle | ‑ |
| Encoder sign | Encoder sign |
| Stator resistance | Stator resistance |
| ‑ | Rotor resistance |
| d-inductance | d-inductance (total leakage inductance) |
| ‑ | Magnetizing inductance Lh |
| q inductance for iq = 0 A | q inductance for iq = 0 A |
| Converter emulation error | ‑ |

The following rules govern the acceptance of the determined parameters:

- The default values are "0".
- For a value to be accepted, it must differ from the default value, i.e. differ from "0".

The following conditions govern the acceptance of the moment of inertia:

|  |  |  |
| --- | --- | --- |
| **p3041 (motor inertia without load - new value determined by MotID)** | **p3042 (load inertia without motor)** | **Acceptance (relevant parameters)** |
| 0 | 0 | -   [p0341](SINAMICS%20Parameter%20SERVO.md#p03410n-motor-moment-of-inertia-1), [p1498](SINAMICS%20Parameter%20SERVO.md#p14980n-load-moment-of-inertia-1), [p0342](SINAMICS%20Parameter%20SERVO.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia-1) = 1 |
| Not equal to 0 | Not equal to 0 |  |
| 0 | Not equal to 0 | p1498, p0342 = 1 |

##### Additional parameters

---

#### Rotating measurement (servo)

##### Description

The rotating measurement is based on the stationary measurement.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected motor movement during motor data identification**  The motor data identification causes motor movements that may reach the maximum speed ([p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)) and the motor torque corresponding to the maximum current ([p0640](SINAMICS%20Parameter%20SERVO.md#p06400n-current-limit)). If persons are in the danger zone, this can result in death, severe injury or material damage.  - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. - Do not carry out the rotating measurement if the traversing distance is mechanically limited. |  |

**Supplementary conditions:**

- The rotating measurement should be carried out with a motor running at no load (de-coupled from the mechanical system).

  This prevents damage/destruction of the load or influencing by the load. If the motor cannot be separated from the mechanical system, the mechanical system can be relieved via the parameterization of the ramp-up time ([p1958](SINAMICS%20Parameter%20SERVO.md#p19580n-rotating-measurement-ramp-upramp-down-time-1)) and/or via a direction of rotation limitation ([p1959](SINAMICS%20Parameter%20SERVO.md#p19590n-rotating-measurement-configuration-1).14,15) or via the current limit (p0640) and speed limit (p1082).
- Do not change default values  
  For the rotating measurement with linear motors, the motor receives different currents up to the maximum current ([p0640](SINAMICS%20Parameter%20SERVO.md#p06400n-current-limit)) and thus the associated maximum force. The motor moves up to three pole-pair widths. Changes to the default values (p1959) may result in damage to the machine.
- The EMERGENCY STOP functions must be operational during the commissioning. Observe the relevant safety rules to preclude danger to the operator and the machine.

> **Note**
>
> The default values of the moving measurement are set for the linear motor so that only the commutation angle is determined, the q-inductance characteristic. The weight is only approximately estimated for the recording of the q-inductance characteristic.

##### Enter configuration data

1. Click "Configuration" to enter the parameter values required for the rotating measurement.
2. Enter the parameter values required for the rotating measurement.

   - [p0352](SINAMICS%20Parameter%20SERVO.md#p03520n-cable-resistance): Cable resistance (important for long motor cables)
   - p0640: Current limit
   - p1082: Maximum rotational speed
   - p1958: Rotating measurement configuration
   - p1959: Rotating measurement configuration

   The [p1909](SINAMICS%20Parameter%20SERVO.md#p19090n-motor-data-identification-control-word-1) and p1959 parameters can be used to select or deselect individual measurements of the motor identification if not all measurements should or can be performed (only for experienced users).

**Perform measurement**

A detailed description of how you can perform the measurement is contained in Stationary/rotating measurement.

**Determined quantities**

The following quantities are determined for the motor data identification with stationary measurement depending on the used motor:

| Synchronous motor | Induction motor |
| --- | --- |
| Commutation angle | ‑ |
| q-inductance characteristic | q-inductance characteristic |
| d-inductance characteristic | ‑ |
| Torque constant k<sub>T</sub> and voltage constant k<sub>E</sub> | ‑ |
| k<sub>T</sub> characteristic | ‑ |
| Moment of inertia | Moment of inertia |
| Reluctance torque constant k<sub>TRel</sub> and optimum load angle | ‑ |
| ‑ | Magnetizing current |
| ‑ | Magnetizing inductance Lh |
| ‑ | Saturation characteristic of the stator inductance |

The following rules govern the acceptance of the determined parameters:

- The default values are "0".
- For a value to be accepted, it must differ from the default value, i.e. differ from "0".

The following conditions govern the acceptance of the moment of inertia:

| [p3041](SINAMICS%20Parameter%20SERVO.md#p3041-motid-moment-of-inertia-identified-1) (motor inertia without load - new value determined by MotID) | [p3042](SINAMICS%20Parameter%20SERVO.md#p3042-motid-load-moment-of-inertia-identified-1) (load inertia without motor) | Acceptance (relevant parameters) |
| --- | --- | --- |
| 0 | 0 | - |
| Not equal to 0 | Not equal to 0 | [p0341](SINAMICS%20Parameter%20SERVO.md#p03410n-motor-moment-of-inertia-1), [p1498](SINAMICS%20Parameter%20SERVO.md#p14980n-load-moment-of-inertia-1), [p0342](SINAMICS%20Parameter%20SERVO.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia-1) = 1 |
| 0 | Not equal to 0 | p1498, p0342 = 1 |

##### Additional parameters

---

---

**See also**

[Motor data identification](#motor-data-identification)

#### Encoder adjustment (servo)

##### Description

For the encoder adjustment for the synchronous motor (linear and rotary), you can enter the following data.

> **Note**
>
> For the encoder adjustment, the motor turns slowly up to 1.5 revolutions or 0.25 pole-pair widths.

**Enter configuration data**

| Parameter | Name |
| --- | --- |
| [p1980](SINAMICS%20Parameter%20SERVO.md#p19800n-polid-technique) | Pole position identification procedure |
| [p1981](SINAMICS%20Parameter%20SERVO.md#p19810n-polid-distance-max) | Pole position identification maximum path |
| [p0325](SINAMICS%20Parameter%20SERVO.md#p03250n-motor-pole-position-identification-current-1st-phase) | Motor pole position identification current 1st phase |
| [p0329](SINAMICS%20Parameter%20SERVO.md#p03290n-motor-pole-position-identification-current) | Motor pole position identification current |
| [p1993](SINAMICS%20Parameter%20SERVO.md#p19930n-polid-motion-based-current) | Pole position identification current motion based |
| [p1994](SINAMICS%20Parameter%20SERVO.md#p19940n-polid-motion-based-rise-time) | Pole position identification rise time motion based |
| [p1995](SINAMICS%20Parameter%20SERVO.md#p19950n-polid-motion-based-gain-1) | Pole position identification gain motion based |
| [p1996](SINAMICS%20Parameter%20SERVO.md#p19960n-polid-motion-based-integral-time) | Pole position identification integral time motion based |
| [p1997](SINAMICS%20Parameter%20SERVO.md#p19970n-polid-motion-based-smoothing-time) | Pole position identification smoothing time motion based |
| [p3090](SINAMICS%20Parameter%20SERVO.md#p30900n-polid-elasticity-based-configuration) | Pole ID elasticity-based configuration |
| [p3091](SINAMICS%20Parameter%20SERVO.md#p30910n-polid-elasticity-based-ramp-time) | Pole ID elasticity-based ramp time |
| [p3092](SINAMICS%20Parameter%20SERVO.md#p30920n-polid-elasticity-based-wait-time) | Pole ID elasticity-based wait time |
| [p3093](SINAMICS%20Parameter%20SERVO.md#p30930n-polid-elasticity-based-measurement-number) | Pole ID elasticity-based measurement count |
| [p3094](SINAMICS%20Parameter%20SERVO.md#p30940n-polid-elasticity-based-deflection-expected-1) | Pole ID elasticity-based deflection expected |
| [p3095](SINAMICS%20Parameter%20SERVO.md#p30950n-polid-elasticity-based-deflection-permissible-1) | Pole ID elasticity-based deflection permitted |
| p3095 | Pole ID elasticity-based current |

**Perform measurement**

A detailed description of how you can perform the measurement is contained in [Stationary/rotating measurement](#motor-data-identification).

**Determined quantities**

The following quantities are determined for the motor data identification with stationary measurement depending on the used motor:

| Name | Parameter |
| --- | --- |
| Commutation angle offset | [p0431](SINAMICS%20Parameter%20SERVO.md#p04310n-angular-commutation-offset) |

Because the commutation angle is always transferred, only the new value is displayed for the encoder adjustment.

##### Messages when activating the measurement

Depending on which method you have selected via p1980 and which motor you are using, different messages are displayed when activating the encoder adjustment.

##### Additional parameters

---

### Data set switchover

#### Overview

Various drive data sets (DDS) and control data sets (CDS) can be used for traversing the drive and for commissioning. As soon as 2 or more data sets of one type have been created for a drive, a drop-down list for selecting the DDS or CDS is activated in the commissioning screen forms of the toolbar. You can use the corresponding drop-down list to select the required data set. Selection of the required data set is, however, possible only if the master control is deactivated.

#### Requirements

- At least 2 drive data sets (DDSs) or control data sets (CDSs) have been created in the drive.
- An online connection to the drive has been established.

#### Procedure

| Symbol | Meaning |
| --- | --- |
| 1. Open the required commissioning screen form (e.g. control panel).     The drop-down list for data set switchover shows the active DDS or the active CDS.                  ![Example: DDS](images/147860348299_DV_resource.Stream@PNG-en-US.png)         ![Example: DDS](images/147860348299_DV_resource.Stream@PNG-en-US.png)      Example: DDS 2. Select the required data set from the drop-down lists. 3. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 4. Read the warning carefully and check the value for the monitoring time.     The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms. 5. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury. - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 6. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

#### Results:

The master control is active. The drop-down lists display the currently set data sets. You can perform additional settings in the commissioning screen form. In addition, the following applies:

- The selection of the data sets can no longer be changed if the master control is active. Selection is blocked via the drop-down lists.
- If another CDS was selected for an infeed, the previously active CDS will nevertheless be used if the master control is active.

---

**See also**

[Rules for using data sets](Configuring%20SINAMICS%20S-G-MV%20drives.md#rules-for-using-data-sets)
