---
title: "Using PID basic functions (S7-300, S7-400, S7-1500)"
package: TFTOPIDBasenUS
topics: 39
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using PID basic functions (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [CONT_C (S7-300, S7-400, S7-1500)](#cont_c-s7-300-s7-400-s7-1500)
- [CONT_S (S7-300, S7-400, S7-1500)](#cont_s-s7-300-s7-400-s7-1500)
- [TCONT_CP (S7-300, S7-400, S7-1500)](#tcont_cp-s7-300-s7-400-s7-1500)
- [TCONT_S (S7-300, S7-400, S7-1500)](#tcont_s-s7-300-s7-400-s7-1500)

## CONT_C (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Technology object CONT_C (S7-300, S7-400, S7-1500)](#technology-object-cont_c-s7-300-s7-400-s7-1500)
- [Configure controller difference CONT_C (S7-300, S7-400, S7-1500)](#configure-controller-difference-cont_c-s7-300-s7-400-s7-1500)
- [Configure the controller algorithm CONT_C (S7-300, S7-400, S7-1500)](#configure-the-controller-algorithm-cont_c-s7-300-s7-400-s7-1500)
- [Configure the output value CONT_C (S7-300, S7-400, S7-1500)](#configure-the-output-value-cont_c-s7-300-s7-400-s7-1500)
- [Programming a pulse controller (S7-300, S7-400, S7-1500)](#programming-a-pulse-controller-s7-300-s7-400-s7-1500)
- [Commissioning CONT_C (S7-300, S7-400, S7-1500)](#commissioning-cont_c-s7-300-s7-400-s7-1500)

### Technology object CONT_C (S7-300, S7-400, S7-1500)

The technology object CONT_C provides a continual PID-controller for automatic and manual mode. It corresponds to the instance data block of the instruction CONT_C. You can configure a pulse controller using the PULSEGEN instruction.

The proportional, integral (INT) and differential components (DIF) are switched parallel to each other and can be turned on and off individually. With this, P-, I, PI-, PD- and PID-controller can be set.

S7-1500  
All parameters and tags of the technology object are retentive and can only be changed during download to the device if you completely download CONT_C.

---

**See also**

[Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
  
[Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
  
[Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
  
[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)
  
[CONT_C (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#cont_c-s7-300-s7-400)

### Configure controller difference CONT_C (S7-300, S7-400, S7-1500)

#### Use process value periphery

To use the process value in the periphery format at the PV_PER input parameter, follow these steps:

1. Select the "Enable I/O" check box.
2. If the process value is available as a physical size, enter the factor and offset for the scaling in percent.  
   The process value is then determined according to the following formula:  
   PV = PV_PER × PV_FAC + PV_OFF

#### Use internal process values

To use the process value in the floating-point format at the PV_IN input parameter, follow these steps:

1. Clear the "Enable I/O" check box.

#### Control deviation

Set a dead zone range under the following requirement:

- The process value signal is noisy.
- The controller gain is high.
- The derivative action is activated.

The noise component of the process value causes strong deviations of the output value in this case. The dead zone suppresses the noise component in the steady controller state. The dead zone range specifies the size of the dead zone. With a dead zone range of 0.0, the dead zone is turned off.

---

**See also**

[How CONT_C works (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#how-cont_c-works-s7-300-s7-400)

### Configure the controller algorithm CONT_C (S7-300, S7-400, S7-1500)

#### General

To determine which components of the control algorithm are activated, proceed as follows:

1. Select an entry from the "Controller structure" list.  
    You can only specify required parameters for the selected controller structure.

#### Proportional action

1. If the controller structure contains a proportional action, enter the "proportional gain".

#### Integral action

1. If the controller structure contains an integral action, enter the integral action time.
2. To give the integral action an initialization value, select the check box "Initialize integral action" and enter the initialization value.
3. In order to permanently set the integral action to this initialization value, select the "Integral action hold" check box.

#### Derivative action

1. If the controller structure contains a derivative action, enter the derivative action time, the derivative action weighting and the delay time.

---

**See also**

[How CONT_C works (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#how-cont_c-works-s7-300-s7-400)

### Configure the output value CONT_C (S7-300, S7-400, S7-1500)

#### General

You can set CONT_C in the manual or automatic mode.

1. To set a manual manipulated value, activate the option "Activate manual mode" option check box.  
   You can specify a manual manipulated value on the input parameter MAN.

#### Manipulated value limits

The manipulated value is limited at the top and bottom so that it can only accept valid values. You cannot turn off the limitation. Exceeding the limits is displayed through the output parameters QLMN_HLM and QLMN_LLM.

1. Enter a value for the high and low manipulated value limits.   
   If the manipulated value is a physical size, the units for the high and low manipulated value limits must match.

#### Scaling

The manipulated value can be scaled for output as a floating point and periphery value through a factor and an offset according to the following formula.

Scaled manipulated value = manipulated value x factor + offset

Default is a factor of 1.0 and an offset of 0.0.

1. Enter a value for the factor and offset.

---

**See also**

[How CONT_C works (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#how-cont_c-works-s7-300-s7-400)

### Programming a pulse controller (S7-300, S7-400, S7-1500)

With the continuous controller CONT_C and the pulse shaper PULSEGEN, you can implement a fixed setpoint controller with a switching output for proportional actuators. The following figure shows the signal flow of the control loop.

![Figure](images/166014573067_DV_resource.Stream@PNG-en-US.png)

The continuous controller CONT_C forms the output value LMN that is converted by the pulse shaper PULSEGEN into pulse/break signals QPOS_P or QNEG_P.

---

**See also**

[PULSEGEN (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#pulsegen-s7-300-s7-400)

### Commissioning CONT_C (S7-300, S7-400, S7-1500)

#### Requirements

- The instruction and the technology object have been loaded to the CPU.

#### Procedure

To manually determine the optimal PID parameters, proceed as follows:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value and output value are recorded.
2. Enter new PID parameters in the "P", "I", "D" and "Delay time" fields.
3. Click on the icon ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png)"Send parameter to CPU" in the "Tuning" group.
4. Select the "Change setpoint" check box in the "Current values" group.
5. Enter a new setpoint and click the ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png) icon in the "Current values" group.
6. Clear the "Manual mode" check box.

   The controller works with the new PID parameters and controls the new setpoint.
7. Check the quality of the PID parameter to check the curve points.
8. Repeat steps 2 to 6 until you are satisfied with the controller results.

## CONT_S (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Technology object CONT_S (S7-300, S7-400, S7-1500)](#technology-object-cont_s-s7-300-s7-400-s7-1500)
- [Configure controller difference CONT_S (S7-300, S7-400, S7-1500)](#configure-controller-difference-cont_s-s7-300-s7-400-s7-1500)
- [Configuring control algorithm CONT_S (S7-300, S7-400, S7-1500)](#configuring-control-algorithm-cont_s-s7-300-s7-400-s7-1500)
- [Configure manipulated value CONT_S (S7-300, S7-400, S7-1500)](#configure-manipulated-value-cont_s-s7-300-s7-400-s7-1500)
- [Commissioning CONT_S (S7-300, S7-400, S7-1500)](#commissioning-cont_s-s7-300-s7-400-s7-1500)

### Technology object CONT_S (S7-300, S7-400, S7-1500)

The technology object CONT_S provides a step controller for actuators with integrating behavior and is used to control technical temperature processes with binary output value output signals. The technology object corresponds to the instance data block of the CONT_S instruction. The operating principle is based on the PI control algorithm of the sampling controller. The step controller operates without a position feedback signal. Both manual and automatic mode are possible.

S7-1500  
All parameters and tags of the technology object are retentive and can only be changed during download to the device if you completely download CONT_S.

---

**See also**

[Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
  
[Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
  
[Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
  
[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)
  
[CONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#cont_s-s7-300-s7-400)

### Configure controller difference CONT_S (S7-300, S7-400, S7-1500)

#### Use process value periphery

To use the process value in the periphery format at the PV_PER input parameter, follow these steps:

1. Select the "Enable I/O" check box.
2. If the process value is available as a physical quantity, enter the factor and offset for the scaling in percent.  
   The process value is then determined according to the following formula:  
   PV = PV_PER × PV_FAC + PV_OFF

#### Use internal process values

To use the process value in the floating-point format at the PV_IN input parameter, follow these steps:

1. Clear the "Enable I/O" check box.

#### Control deviation

Set a deadband range under the following requirement:

- The process value signal is noisy.
- The controller gain is high.
- The derivative action is activated.

The noise component of the process value causes strong deviations of the manipulated variable in this case. The deadband suppresses the noise component in the steady controller state. The deadband range specifies the size of the deadband. With a deadband range of 0.0, the deadband is turned off.

---

**See also**

[Mode of operation CONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-cont_s-s7-300-s7-400)

### Configuring control algorithm CONT_S (S7-300, S7-400, S7-1500)

#### PID algorithm

1. Enter the "proportional amplification" for the P-component.
2. Enter the integration time for the time behavior of the I-component.   
   With an integration time of 0.0, the I-component is switched off.

---

**See also**

[Mode of operation CONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-cont_s-s7-300-s7-400)

### Configure manipulated value CONT_S (S7-300, S7-400, S7-1500)

#### General

You can set CONT_S in the manual or automatic mode.

1. To set a manual manipulated value, activate the "Activate manual mode" option check box.   
   Enter a manual manipulated value for the input parameters LMNUP and LMNDN.

#### Pulse generator

1. Enter the minimum impulse duration and minimum pause duration.  
   The values must be greater than or equal to the cycle time for the input parameter CYCLE. The frequency of operation is reduced through this.
2. Enter the motor setting time.   
   The value must be greater than or equal to the cycle time of the input parameter CYCLE.

---

**See also**

[Mode of operation CONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-cont_s-s7-300-s7-400)

### Commissioning CONT_S (S7-300, S7-400, S7-1500)

#### Requirements

- The instruction and the technology object have been loaded to the CPU.

#### Procedure

To manually determine the optimal PID parameters, proceed as follows:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value and output value are recorded.
2. In the fields "P" and "I", enter a new proportional value and a new integration time.
3. Click on the icon ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png)"Send parameter to CPU" in the "Tuning" group.
4. Select the "Change setpoint" check box in the "Current values" group.
5. Enter a new setpoint and click the ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png) icon in the "Current values" group.
6. Clear the "Manual mode" check box.

   The controller works with the new parameters and controls the new setpoint.
7. Check the quality of the PID parameter to check the curve points.
8. Repeat steps 2 to 6 until you are satisfied with the controller results.

## TCONT_CP (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Technology object TCONT_CP (S7-300, S7-400, S7-1500)](#technology-object-tcont_cp-s7-300-s7-400-s7-1500)
- [Configure TCONT_CP (S7-300, S7-400, S7-1500)](#configure-tcont_cp-s7-300-s7-400-s7-1500)
- [Commissioning TCONT_CP (S7-300, S7-400, S7-1500)](#commissioning-tcont_cp-s7-300-s7-400-s7-1500)

### Technology object TCONT_CP (S7-300, S7-400, S7-1500)

The technology object TCONT_CP provides a continual temperature controller with pulse generator. It corresponds to the instance data block of the instruction TCONT_CP. The operation is based on the PID control algorithm of the sampling controller. Both manual and automatic mode are possible.

The instruction TCONT_CP calculates the proportional, integral and derivative parameters for your controlled system during pretuning. "Fine tuning" can be used to tune the parameters further. You can also enter the PID parameters manually.

S7-1500  
All parameters and tags of the technology object are retentive and can only be changed during download to the device if you completely download TCONT_CP.

---

**See also**

[Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
  
[Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
  
[Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
  
[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)
  
[TCONT_CP (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#tcont_cp-s7-300-s7-400)

### Configure TCONT_CP (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Controller difference (S7-300, S7-400, S7-1500)](#controller-difference-s7-300-s7-400-s7-1500)
- [Controlling algorithm (S7-300, S7-400, S7-1500)](#controlling-algorithm-s7-300-s7-400-s7-1500)
- [Manipulated value continual controller (S7-300, S7-400, S7-1500)](#manipulated-value-continual-controller-s7-300-s7-400-s7-1500)
- [Manipulated value pulse controller (S7-300, S7-400, S7-1500)](#manipulated-value-pulse-controller-s7-300-s7-400-s7-1500)

#### Controller difference (S7-300, S7-400, S7-1500)

##### Use process value periphery

To use the input parameter PV_PER, proceed as follows:

1. Select the entry "Periphery" from the "Source" list.
2. Select the "sensor type".  
   Depending on the sensor type, the process value is scaled according to different formulas.

   - Standard  
     Thermoelements; PT100/NI100

     PV = 0.1 × PV_PER × PV_FAC + PV_OFFS
   - Cooling;  
     PT100/NI100

     PV = 0.01 × PV_PER × PV_FAC + PV_OFFS
   - Current/voltage

     PV = 100/27648 × PV_PER × PV_FAC + PV_OFFS
3. Enter the factor and offset for the scaling of the process value periphery.

##### Use internal process values

To use the input parameter PV_IN, proceed as follows:

1. Select the entry "Internal" from the "Source" list.

##### Control deviation

Set a deadband range under the following requirement:

- The process value signal is noisy.
- The controller gain is high.
- The derivative action is activated.

The noise component of the process value causes strong deviations of the manipulated variable in this case. The deadband suppresses the noise component in the steady controller state. The deadband range specifies the size of the deadband. With a deadband range of 0.0, the deadband is turned off.

---

**See also**

[Mode of operation TCONT_CP (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_cp-s7-300-s7-400)

#### Controlling algorithm (S7-300, S7-400, S7-1500)

##### General

1. Enter the "Sampling time PID algorithm".  
   A controller sampling time should not exceed 10 % of the determined integratl action time of the controller (TI).
2. If the controller structure contains a proportional action, enter the "proportional gain".   
   A negative proportional gain inverts the rule meaning.

##### Proportional action

For changes of the setpoint, it may lead to overshooting of the proportional action. Through the weighting of the proportional action, you can select how strongly the proportional action should react when setpoint changes are made. The weakening of the proportional action is reached through a compensation of the integral action.

1. To weaken the proportional action for setpoint changes, enter a "Proportional action weighting".

   - 1.0: Proportional action for setpoint change is fully effective
   - 0.0: Proportional action for setpoint change is not effective

##### Integral action

With a limitation of the manipulated value, the integral action is stopped. With a control deviation that moves the integral action in the direction of an internal setting range, the integral action is released again.

1. If the controller structure contains an integral action, enter the "integral action time".   
   With an integral action time of 0.0, the integral action is switched off.
2. To give the integral action an initialization value, select the "Initialize integral action" check box and enter the "Initialization value".  
   Upon restart or COM_RST = TRUE, the integral action is set to this value.

##### Derivative action

1. If the controller structure contains a derivative action, enter the derivative action time (TD) and the coefficients DT1 (D_F).  
   With switched derivative action, the following equation should be maintained:  
   TD = 0.5 × CYCLE× D_F.  
   The delay time is calculated from this according to the formula:  
   delay time = TD/D_F

##### Set PD-controller with operating point

1. Enter the integral action time 0.0.
2. Activate the "Initialize integral action" check box.
3. Enter the operating point as the initialization value.

##### Set P-controller with operating point

1. Set a PD-controller with an operating point.
2. Enter the derivative action time 0.0.  
   The derivative action is disabled.

##### Control zone

The control zone limits the value range of the control deviation. If the control deviation is outside of this value range, the manipulated value limits are used.

With an occurrence in the control zone, the derivative action leads to a very quick reduction of the manipulated variable. Thus, the control zone only makes sense for switched on derivative actions. Without control zone, only the reducing proportional action would reduce the manipulated value. The control zone leads to a quick oscillation without over/under shooting if the emitted minimum or maximum manipulated values are removed from the manipulated value required for the new operating point.

1. Activate the "Activate" check box in the "control zone" group.
2. Enter a setpoint value in the "Width" input field from which the process value may deviate above or below.

---

**See also**

[Mode of operation TCONT_CP (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_cp-s7-300-s7-400)

#### Manipulated value continual controller (S7-300, S7-400, S7-1500)

##### Manipulated value limits

The manipulated value is limited at the top and bottom so that it can only accept valid values. You cannot turn off the limitation. Exceeding the limits is displayed through the output parameters QLMN_HLM and QLMN_LLM.

1. Enter a value for the high and low manipulated value limits.

##### Scaling

The manipulated value can be scaled for output as a floating point and periphery value through a factor and an offset according to the following formula.

Scaled manipulated value = manipulated value x factor + offset

Default is a factor of 1.0 and an offset of 0.0.

1. Enter a value for the factor and offset.

##### Pulse generator

The pulse generator must be turned on for a continual controller.

1. Disable the "Activate" option check box in the "Pulse generator" group.

---

**See also**

[Mode of operation TCONT_CP (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_cp-s7-300-s7-400)

#### Manipulated value pulse controller (S7-300, S7-400, S7-1500)

##### Pulse generator

The analog manipulated value (LmnN) can be emitted through pulse-duration modulation on the output parameter QPULSE as an impulse sequence.

To use the pulse generator, proceed as follows:

1. Activate the "Activate" option check box in the "pulse generator" group.
2. Enter the "sampling time pulse generator", the "minimum impulse/break duration" and the "period duration".

The following graphics clarify the connection between the "sampling pulse generator" (CYCLE_P), the "minimum impulse/break duration" (P_B_TM) and the "period duration" (PER_TM):

![Pulse generator](images/166014578571_DV_resource.Stream@PNG-de-DE.png)

![Pulse generator](images/166014584075_DV_resource.Stream@PNG-de-DE.png)

##### Sampling time pulse generator

The sampling time pulse generator must agree with the time tact of the cyclic interrupt OB being called. The duration of the created impulse is always a whole number factor of this value. For an adequately precise manipulated value resolution, the following relationship should apply:  
CYCLE_P ≤ PER_TM/50

##### Minimum impulse/break duration

Through the minimum impulse/break duration, short on or off times on the actuator are avoided. An impulse smaller than P_B_TM is suppressed.

Recommended are values P_B_TM ≤ 0.1 × PER_TM.

##### Period duration

The period duration should not exceed 20% of the determined integration time of the controller (TI):  
PER_TM ≤ TI/5

##### Example for the effect of the parameter CYCLE_P, CYCLE and PER_TM:

Period duration PER_TM = 10 s

Sampling time PID-algorithm CYCLE = 1 s

Sampling time pulse generator CYCLE_P = 100 ms.

Every second, a new manipulated value, every 100 ms the comparison of the manipulated value occurs with the previously emitted impulse length and break length.

- If an impulse is emitted, there are 2 possibilities:

  - The calculated manipulated value is larger than the previous impulse length/PER_TM. Then the impulse is extended.
  - The calculated manipulated value is less than or equal to the previous impulse length/PER_TM. Then no impulse signal will be emitted.
- If no impulse is emitted, there are also 2 possibilities:

  - The value (100 % - calculated manipulated value) is greater than the previous break length / PER_TM. Then the break is extended.
  - The value (100 % - calculated manipulated value) is less than or equal to the previous break length / PER_TM. Then an impulse signal will be emitted.

---

**See also**

[Mode of operation TCONT_CP (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_cp-s7-300-s7-400)
  
[Operating principle of the pulse generator (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#operating-principle-of-the-pulse-generator-s7-300-s7-400)

### Commissioning TCONT_CP (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Optimization of TCONT_CP (S7-300, S7-400, S7-1500)](#optimization-of-tcont_cp-s7-300-s7-400-s7-1500)
- [Requirements for an optimization (S7-300, S7-400, S7-1500)](#requirements-for-an-optimization-s7-300-s7-400-s7-1500)
- [Possibilities for optimization (S7-300, S7-400, S7-1500)](#possibilities-for-optimization-s7-300-s7-400-s7-1500)
- [Tuning result (S7-300, S7-400, S7-1500)](#tuning-result-s7-300-s7-400-s7-1500)
- [Parallel tuning of controller channels (S7-300, S7-400, S7-1500)](#parallel-tuning-of-controller-channels-s7-300-s7-400-s7-1500)
- [Fault descriptions and corrective measures (S7-300, S7-400, S7-1500)](#fault-descriptions-and-corrective-measures-s7-300-s7-400-s7-1500)
- [Performing pretuning (S7-300, S7-400, S7-1500)](#performing-pretuning-s7-300-s7-400-s7-1500)
- [Performing fine tuning (S7-300, S7-400, S7-1500)](#performing-fine-tuning-s7-300-s7-400-s7-1500)
- [Cancelling pretuning or fine tuning (S7-300, S7-400, S7-1500)](#cancelling-pretuning-or-fine-tuning-s7-300-s7-400-s7-1500)
- [Manual fine-tuning in control mode (S7-300, S7-400, S7-1500)](#manual-fine-tuning-in-control-mode-s7-300-s7-400-s7-1500)
- [Performing fine tuning manually (S7-300, S7-400, S7-1500)](#performing-fine-tuning-manually-s7-300-s7-400-s7-1500)

#### Optimization of TCONT_CP (S7-300, S7-400, S7-1500)

##### Application possibilities

The controller optimization for heating or cooling processes from process type I is applicable. But you can use the block for processes with higher levels like process type II or III.

The PI/PID parameters are automatically determined and set. The controller draft is designed for an optimal disruption behavior The "precise" parameters resulting from this lead to overshooting of 10% to 40% of the jump height for setpoint jump heights.

##### Phases of controller optimization

For the controller optimization, individual phases are run through, which you can read on the parameter PHASE .

##### PHASE = 0

No tuning is running. TCONT_CP works in automatic or manual mode.

During PHASE = 0, you can make sure that the controlled system fulfills the requirements for an optimization.

At the end of the optimization, TCONT_CP changes back into PHASE = 0.

##### PHASE = 1

TCONT_CP is prepared for optimization. PHASE = 1 may only be started if the requirements for an optimization are fulfilled.

During PHASE = 1, the following values are determined:

- Process value noise NOISE_PV
- Initial slope PVDT0
- Average of the manipulated variable
- Sampling time PID algorithm CYCLE
- Sampling time pulse generator CYCLE_P

##### PHASE = 2

In phase 2, the process value attempts to detect the point of inflection with a constant manipulated variable. This method prevents the point of inflection from being found too early as a result of process variable noise.

With the pulse controller, the process variable is averaged over N pulse cycles and then made available to the controller stage. There is a further averaging of the process variable in the controller stage: Initially, this averaging is inactive; in other words, averaging always takes place over 1 cycle. As long as the noise exceeds a certain level, the number of cycles is doubled.

The period and amplitude of the noise are calculated. The search for the point of inflection is canceled and phase 2 is exited only when the gradient is always smaller than the maximum rise during the estimated period. TU and T_P_INF are, however, calculated at the actual point of inflection.

Tuning, however, is only ended when the following two conditions are met:

1. The process value is more than 2*NOISE_PV away from the point of inflection.
2. The process value has exceeded the point of inflection by 20%.

   > **Note**
   >
   > When exciting the process using a setpoint step change, tuning is ended at the latest when the process value exceeds 75% of the setpoint step change (SP_INT-PV0) (see below).

##### PHASE = 3, 4, 5

The phases 3, 4 and 5 last 1 cycle each.

In Phase 3, the valid PI/PID parameters are saved before the optimization and the process parameter is calculated.

In Phase 4, the new PI/PID parameters are calculated.

In Phase 5, the new manipulated variable is calculated and the controlled system is given.

##### PHASE = 7

The process type is inspected in Phase 7, because TCONT_CP always changes to automatic mode after optimization. The automatic mode starts with LMN = LMN0 + 0.75*TUN_DLMN as a manipulated variable. The testing of the process type occurs **in the automatic mode** with the recently recalculated controller parameters and ends at the latest 0.35*TA (equilibrium time) after the point of inflection. If the process order deviates strongly from the estimated value, the controller parameters are newly calculated and STATUS_D is counted up by 1, otherwise, the controller parameters remain unchanged.

Then the optimization mode is complete and TCONT_CP is back in PHASE = 0. At the STATUS_H parameter, you can identify whether the tuning was successfully completed.

##### Premature cancellation of the optimization

In Phase 1, 2 or 3, you can cancel the optimization by resetting TUN_ON = FALSE without calculating new parameters. The controller starts in the automatic mode with LMN = LMN0 + TUN_DLMN. If the controller was in manual mode before the tuning, the old manual manipulated variable is output.

If the tuning is canceled in Phase 4, 5 or 7 with TUN_ON = FALSE, the determined controlled parameters are contained until then.

#### Requirements for an optimization (S7-300, S7-400, S7-1500)

##### Transient response

The process must have a stable, asymptotic transient response with time lag.

The process value must settle to steady state after a step change of the manipulated variable. This therefore excludes processes that already show an oscillating response without control, as well as processes with no recovery (integrator in the control system).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| This may result in death, severe injury or considerable property damage.   During an tuning, the parameter MAN_ON is ineffective. Through this, the output value or process value may take on undesired - even extreme - values.  The output value is defined through the tuning. To cancel the tuning, you first have to set TUN_ON = FALSE. This makes MAN_ON effective again. |  |

##### Guaranteeing a stationary initial state (phase 0)

With lower-frequency oscillations of the process value, for example, due to incorrect controller parameters, the controller must be put in manual mode before the tuning is started and wait for the oscillation to stop. Alternatively, you could switch to a "soft" set PI controller (small loop gain large integration time).

Now you have to wait until the stationary state is reached, this means, until the process value and output value have a steady state. It is also permissible to have an asymptotic transient oscillation or slow drifting of the process value (stationary state, see the following image). The output value must be constant or fluctuate by a constant average.

> **Note**
>
> Avoid changing the manipulated variable shortly before starting the tuning. A change of the manipulated variable can occur in an unintended manner through the establishment of the test conditions (for example, closing an oven door)! If this does happen, you have to at least wait until the process value has an asymptotic transient oscillation in a stationary state again. Better controller parameters can be reached if you wait until the transient effect has completely subsided.

In the following image, the transient oscillation is illustrated in the stationary state:

![Guaranteeing a stationary initial state (phase 0)](images/166014602379_DV_resource.Stream@PNG-en-US.png)

##### Linearity and operating range

The process response must be linear across the operating range. Non-linear response occurs, for example, when an aggregation state changes. Tuning must take place in a linear part of the operating range.

This means, during tuning and normal control operation non-linear effects within the operating range must be insignificant. It is, however possible to retune the process when the operating point changes, providing tuning is repeated in the close vicinity of the new operating point and non-linearity does not occur during tuning.

If a specific static non-linearity (e.g., valve characteristics) is known, it is always advisable to compensate this with a polyline to linearize the process response.

##### Disturbance in temperature processes

Disturbances such as thermal transfer to neighboring zones must not influence the overall temperature process to any great extent. For example, when zones of an extruder are tuned, all zones must be heated up simultaneously.

#### Possibilities for optimization (S7-300, S7-400, S7-1500)

The following possibilities for tuning exist:

- Pretuning
- Fine tuning
- Manual fine-tuning in control mode

##### Pretuning

During this tuning, the working point is approached from the cold state through a setpoint jump.

With TUN_ON = TRUE, you can establish the tuning readiness. The controller switches from PHASE = 0 to PHASE = 1.

![Pretuning](images/166014607883_DV_resource.Stream@PNG-en-US.png)

The tuning manipulated variable (LMN0 + TUN_DLMN) is activated by a setpoint change (transition phase 1 -> 2). The setpoint is not effective until the inflection point has been reached (automatic mode is not enabled until this point is reached).

The user is responsible for defining the output excitation delta (TUN_DLMN) according to the permitted process value change. The sign of TUN_DLMN must be set depending on the intended process value change (take into account the direction in which the control is operating).

The setpoint step change and TUN_DLMN must be suitably matched. If the value of TUN_DLMN is too high, there is a risk that the point of inflection will not be found before 75% of the setpoint step change is reached.

TUN_DLMN must nonetheless be high enough to ensure that the process value reaches at least 22 % of the setpoint step change. Otherwise, the process will remain in tuning mode (phase 2).

Remedy: Reduce the setpoint value during the inflection point search.

> **Note**
>
> If processes are extremely sluggish, it is advisable during tuning to specify a target setpoint that is somewhat lower than the desired operating point and to monitor the status bits and PV closely (risk of overshooting).
>
> **Tuning only in the linear range:**
>
> The signals of certain processes (e.g., zinc or magnesium smelters) will pass a non-linear area at the approach of the operating range (change in the state of aggregation).
>
> By selecting a suitable setpoint step change, tuning can be limited to the linear range. When the process value has passed 75% of the setpoint step change (SP_INT-PV0), tuning is ended.
>
> At the same time, TUN_DLMN should be reduced to the extent that the point of inflection is guaranteed to be found before 75% of the setpoint step change is reached.

##### Fine tuning

During this tuning, the process with a constant setpoint is activated through a output value jump.

![Fine tuning](images/166014626187_DV_resource.Stream@PNG-en-US.png)

The tuning manipulated variable (LMN0 + TUN_DLMN) is activated by setting the start bit TUN_ST (transition from phase 1 -> 2). When you modify the setpoint value, the new value will not take effect until the point of inflection has been reached (automatic mode will not be enabled until this point has been reached).

The user is responsible for defining the output excitation delta (TUN_DLMN) according to the permitted process value change. The sign of TUN_DLMN must be set depending on the intended process value change (take into account the direction in which the control is operating).

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| Safety off at 75% is not available when you excite the process via TUN_ST. Tuning is ended when the point of inflection is reached. However, in noisy processes the point of inflection may be significantly exceeded. |  |

##### Manual fine-tuning in control mode

The following measures can be employed to achieve an overshoot-free setpoint response:

- Adapting the control zone
- Optimize command action
- Attenuation of control parameters
- Modifying control parameters

#### Tuning result (S7-300, S7-400, S7-1500)

The left digit of STATUS_H displays the tuning status

| STATUS_H | Result |
| --- | --- |
| 0 | Default or new controller parameters have not yet been found. |
| 10000 | Suitable control parameters found. |
| 2xxxx | Control parameters have been found via estimated values; check the control response or check the STATUS_H diagnostic message and repeat controller tuning. |
| 3xxxx | An operator error has occurred; check the STATUS_H diagnostic message and repeat controller tuning. |

The CYCLE and CYCLE_P sampling times were already checked in phase 1.

The following controller parameters are updated on TCONT_CP:

- P (proportional GAIN)
- I (integration time TI)
- D (derivative time TD)
- Weighting of the proportional action PFAC_SP
- Coefficient DT1 (D_F)
- Control zone on/off CONZ_ON
- Control zone width CON_ZONE

The control zone is only activated if the process type is suitable (process type I and II) and a PID controller is used (CONZ_ON = TRUE).

Depending on PID_ON, control is implemented either with a PI or a PID controller. The old controller parameters are saved and can be retrieved with UNDO_PAR. A PI parameter record and a PID parameter record are saved additionally in the PI_CON and PID_CON structures. Using LOAD_PID and making a suitable setting for PID_ON, it is also possible to switch later between the tuned PI or PID parameters.

#### Parallel tuning of controller channels (S7-300, S7-400, S7-1500)

##### Adjacent zones (strong heat coupling)

If two or more controllers are controlling the temperature, on a plate, for example (in other words, there are two heaters and two measured process values with strong heat coupling), proceed as follows:

1. OR the two outputs QTUN_RUN.
2. Interconnect each TUN_KEEP input with the output of the OR element.
3. Start both controllers by specifying a setpoint step change at the same time or by setting TUN_ST at the same time.

The following schematic illustrates the parallel tuning of controller channels.

![Adjacent zones (strong heat coupling)](images/166014631691_DV_resource.Stream@PNG-de-DE.png)

**Advantage:**

Both controllers output LMN0 + TUN_DLMN until both controllers have left phase 2. This prevents the controller that completes tuning first from falsifying the tuning result of the other controller due to the change in its manipulated variable.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| Reaching 75% of the setpoint step change causes an exiting of phase 2 and resetting of output QTUN_RUN. However, automatic mode does not start until TUN_KEEP is also 0. |  |

##### Adjacent zones (weak heat coupling)

In general terms, tuning should be carried out to reflect the way in which the controller will operate subsequently. If zones are operated together during production such that the temperature differences between the zones remain the same, the temperature of the adjacent zones ought to be increased accordingly during tuning.

Differences in temperature at the beginning of the tuning are irrelevant since they will be compensated by the initial heating (-> initial rise = 0).

#### Fault descriptions and corrective measures (S7-300, S7-400, S7-1500)

##### Compensating operator errors

| Operator error | STATUS and action | Comment |
| --- | --- | --- |
| TUN_ON and setpoint step change or TUN_ST are set simultaneously | Transition to phase 1; however, tuning is not started.  - SP_INT = SP<sub>old </sub>or - TUN_ST = FALSE | The setpoint change is canceled. This prevents the controller from settling to the new setpoint value and from leaving the stationary operating point unnecessarily. |
| Effective TUN_DLMN < 5% (end of phase 1) | STATUS_H = 30002  - Transition to phase 0 - TUN_ON = FALSE - SP = SP<sub>old</sub> | Tuning is canceled.  The setpoint change is canceled. This prevents the controller from settling to the new setpoint value and from leaving the stationary operating point unnecessarily. |

##### Point of inflection not reached (only if excited by setpoint step change)

At the latest, tuning is ended when the process value has passed 75% of the setpoint step change (SP_INT-PV0). This is signaled by "inflection point not reached" in STATUS_H (2xx2x).

The currently valid setpoint always applies. By reducing the setpoint, it is possible to achieve an earlier end of the tuning function.

In typical temperature processes, cancelation of tuning at 75% of the setpoint step change is normally adequate to prevent overshoot. However, **caution** is advised, particularly in processes with a greater delay (TU/TA > 0.1, process type III). If manipulated variable excitation is too strong compared to the setpoint step change, the process value can overshoot heavily (up to a factor of 3).

In higher-order processes, if the point of inflection is still a long way off after reaching 75% of the setpoint step change, there will be significant overshoot. In addition, the controller parameters are too stringent. In this case, you should reduce the controller parameters or repeat the attempt.

The following schematic illustrates the overshoot of the process variable when the excitation is too strong (process type III):

![Point of inflection not reached (only if excited by setpoint step change)](images/166014649995_DV_resource.Stream@PNG-en-US.png)

In typical temperature processes, cancelation shortly before reaching the point of inflection is not critical in terms of the controller parameters.

If you repeat the attempt, reduce TUN_DLMN or increase the setpoint step change.

Principle: The value of the manipulated variable used for tuning must be suitable for the setpoint step change.

##### Error estimating the delay time or order

The delay time (STATUS_H = 2x1xx or 2x3xx) or order (STATUS_H = 21xxx or 22xxx) were not acquired correctly. Operation continues with an estimate that can lead to non-optimum controller parameters.

Repeat the tuning procedure and ensure that disturbances do not occur at the process value.

> **Note**
>
> The special case of a PT1-only process is also indicated by STATUS_H = 2x1xx (TU <= 3*CYCLE). In this case, it is not necessary to repeat the attempt. Reduce the controller parameters if the control oscillates.

##### Quality of measuring signals (measurement noise, low-frequency interference)

The results of tuning can be distorted by measurement noise or by low-frequency interference. Note the following:

- If you encounter measurement noise, set the sampling frequency higher rather than lower. During one noise period, the process value should be sampled at least twice. In pulse mode, integrated mean value filtering can be helpful. This assumes, however, that the process variable PV is transferred to the instruction in the fast pulse cycle. The degree of noise should not exceed 5% of the useful signal change.
- High-frequency interference cannot be filtered out by TCONT_CP. This should be filtered earlier in the measuring sensor to prevent the aliasing effect.

  The following schematic illustrates the aliasing effect when the sampling time is too long:

  ![Quality of measuring signals (measurement noise, low-frequency interference)](images/166014655499_DV_resource.Stream@PNG-de-DE.png)
- With low-frequency interference, it is relatively easy to ensure an adequately high sampling rate. However, the TCONT_CP must then generate a uniform measuring signal by having a large interval in the mean value filtering. Mean value filtering must extend over at least two noise periods. Internally in the block, this soon results in higher sampling times such that the accuracy of the tuning is adversely affected. Adequate accuracy is guaranteed with at least 40 noise periods up to the point of inflection.

  Possible remedy when repeating the attempt:

  Increase TUN_DLMN.

##### Overshoot

Overshoot can occur in the following situations:

| Situation | Cause | Remedy |
| --- | --- | --- |
| End of tuning | - Excitation by a too high manipulated value change compared with the setpoint step change (see above). - PI controller activated by PID_ON = FALSE. | - Increase the setpoint step change or reduce the manipulated value step change. - If the process permits a PID controller, start tuning with PID_ON = TRUE. |
| Tuning in phase 7 | Initially, less aggressive controller parameters were determined (process type III); these can lead to an overshoot in phase 7. | - |
| Control mode | PI controller with PFAC_SP = 1.0 for process type I. | If the process permits a PID controller, start tuning with PID_ON = TRUE. |

#### Performing pretuning (S7-300, S7-400, S7-1500)

##### Requirements

- The instruction and the technology object have been loaded to the CPU.

##### Procedure

To manually determine the optimum PID parameters for initial commissioning, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value and output value are recorded.
2. Select "Pretuning" from the "Mode" drop-down list.

   TCONT_CP is ready for tuning.
3. In the "Output value jump" field, specify how much the output value should be increased.
4. Enter a setpoint in the "Setpoint" field. The output value jump only takes effect when another setpoint is entered.
5. Click the ![Procedure](images/166014283659_DV_resource.Stream@PNG-de-DE.png) "Start tuning" icon.

   The pretuning starts. The status of the tuning is displayed.

#### Performing fine tuning (S7-300, S7-400, S7-1500)

##### Requirements

- The instruction and the technology object have been loaded to the CPU.

##### Procedure

To determine the optimal PID parameters at the operating point, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value and output value are recorded.
2. Select "Fine tuning" from the "Mode" drop-down list.

   TCONT_CP is ready for tuning.
3. In the "Output value jump" field, specify how much the output value should be increased.
4. Click the ![Procedure](images/166014283659_DV_resource.Stream@PNG-de-DE.png) "Start tuning" icon.

   Fine tuning starts. The status of the tuning is displayed.

#### Cancelling pretuning or fine tuning (S7-300, S7-400, S7-1500)

To cancel pretuning or fine tuning, click on the ![Figure](images/166014661003_DV_resource.Stream@PNG-de-DE.png) icon, "Stop tuning".

If the PID parameters have not yet been calculated and stored, TCONT_CP starts in automatic mode LMN = LMN0 + TUN_DLMN. If the controller was in manual mode before the tuning, the old manual manipulated variable is output.

If the calculated PID parameters have already been saved, TCONT_CP starts in automatic mode and works with the previously determined PID parameters.

#### Manual fine-tuning in control mode (S7-300, S7-400, S7-1500)

The following measures can be employed to achieve an overshoot-free setpoint response:

##### Adapting the control zone

During tuning, "TCONT_CP" determines a control zone CON_ZONE and activated if the process type is suitable (process type I and II) and a PID controller is used (CONZ_ON = TRUE). In control mode, you can modify the control zone or switch it off completely (with CONZ_ON = FALSE).

> **Note**
>
> Activating the control zone with higher-order processes (process type III) does not normally provide any benefit since the control zone is then larger than the control range that can be achieved with a 100% manipulated variable. There is also no advantage in activating the control zone for PI controllers.
>
> Before you switch on the control zone manually, make sure that the control zone is not too narrow. If the control zone is set too narrow, oscillations occur in the manipulated variable and the process value.

##### Continuous attenuation of the control response with PFAC_SP

The control response can be attenuated with the PFAC_SP parameter. This parameter specifies the percentage of proportional component that is effective for setpoint step changes.

Regardless of the process type, PFAC_SP is set to a default value of 0.8 by the tuning function; you can later modify this value if required. To limit overshoot during setpoint step changes (with otherwise correct controller parameters) to approximately 2%, the following values are adequate for PFAC_SP:

|  | Process type I | Process type II | Process type III |
| --- | --- | --- | --- |
|  | Typical temperature process | Intermediate range | Higher-order temperature process |
| PI | 0.8 | 0.82 | 0.8 |
| PID | 0.6 | 0.75 | 0.96 |

Adjust the default factor (0.8) in the following situations, in particular:

- Process type I with PID (0.8 →0.6): Setpoint step changes within the control zone still lead to approximately 18% overshoot with PFAC_SP = 0.8.
- Process type III with PID (0.8 →0.96): Setpoint step changes with PFAC_SP = 0.8 are attenuated too strongly. This leads to a significantly slower response time.

##### Attenuation of control parameters

When a closed-loop control circuit oscillates or if overshoot occurs after setpoint step changes, you can reduce the controller GAIN (e.g., to 80% of the original value) and increase integral time TI (e.g., to 150% of the original value). If the analog output value of the continuous controller is converted to binary actuating signals by a pulse shaper, quantization noise may cause minor permanent oscillation. You can eliminate this by increasing the controller deadband DEADB_W.

##### Modifying control parameters

Proceed as follows to modify control parameters:

1. Save the current parameters with SAVE_PAR.
2. Modify the parameters.
3. Test the control response.

If the new parameter settings are worse than the old ones, retrieve the old parameters with UNDO_PAR.

#### Performing fine tuning manually (S7-300, S7-400, S7-1500)

##### Requirements

- The instruction and the technology object have been loaded to the CPU.

##### Procedure

To manually determine the optimal PID parameters, proceed as follows:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value and output value are recorded.
2. Select "Manual" from the "Mode" drop-down list.
3. Enter the new PID parameters.
4. Click on the icon ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png)"Send parameter to CPU" in the "Tuning" group.
5. Select the "Change setpoint" check box in the "Current values" group.
6. Enter a new setpoint and click the ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png) icon in the "Current values" group.
7. Clear the "Manual mode" check box.

   The controller works with the new PID parameters and controls the new setpoint.
8. Check the quality of the PID parameter to check the curve points.
9. Repeat steps 3 to 8 until you are satisfied with the controller results.

## TCONT_S (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Technology object TCONT_S (S7-300, S7-400, S7-1500)](#technology-object-tcont_s-s7-300-s7-400-s7-1500)
- [Configure controller difference TCONT_S (S7-300, S7-400, S7-1500)](#configure-controller-difference-tcont_s-s7-300-s7-400-s7-1500)
- [Configure controller algorithm TCONT_S (S7-300, S7-400, S7-1500)](#configure-controller-algorithm-tcont_s-s7-300-s7-400-s7-1500)
- [Configure manipulated value TCONT_S (S7-300, S7-400, S7-1500)](#configure-manipulated-value-tcont_s-s7-300-s7-400-s7-1500)
- [Commissioning TCONT_S (S7-300, S7-400, S7-1500)](#commissioning-tcont_s-s7-300-s7-400-s7-1500)

### Technology object TCONT_S (S7-300, S7-400, S7-1500)

The technology object TCONT_S provides a step controller for actuators with integrating behavior and is used to control technical temperature processes with binary output value output signals. The technology object corresponds to the instance data block of the TCONT_S instruction. The operating principle is based on the PI control algorithm of the sampling controller. The step controller operates without a position feedback signal. Both manual and automatic mode are possible.

S7-1500  
All parameters and tags of the technology object are retentive and can only be changed during download to the device if you completely download TCONT_S.

---

**See also**

[Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
  
[Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
  
[Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
  
[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)
  
[TCONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#tcont_s-s7-300-s7-400)

### Configure controller difference TCONT_S (S7-300, S7-400, S7-1500)

#### Use process value periphery

To use the input parameter PV_PER, proceed as follows:

1. Select the entry "Periphery" from the "Source" list.
2. Select the "sensor type".  
   Depending on the sensor type, the process value is scaled according to different formulas.

   - Standard  
     Thermoelements; PT100/NI100

     PV = 0.1 × PV_PER × PV_FAC + PV_OFFS
   - Cooling;  
     PT100/NI100

     PV = 0.01 × PV_PER × PV_FAC + PV_OFFS
   - Current/voltage

     PV = 100/27648 × PV_PER × PV_FAC + PV_OFFS
3. Enter the factor and offset for the scaling of the process value periphery.

#### Use internal process values

To use the input parameter PV_IN, proceed as follows:

1. Select the entry "Internal" from the "Source" list.

#### Control deviation

Set a dead zone range under the following requirement:

- The process value signal is noisy.
- The controller gain is high.
- The derivative action is activated.

The noise component of the process value causes strong deviations of the output value in this case. The dead zone suppresses the noise component in the steady controller state. The dead zone range specifies the size of the dead zone. With a dead zone range of 0.0, the dead zone is turned off.

---

**See also**

[Mode of operation TCONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_s-s7-300-s7-400)

### Configure controller algorithm TCONT_S (S7-300, S7-400, S7-1500)

#### General

1. Enter the "Sampling time PID algorithm".  
   A controller sampling time should not exceed 10 % of the determined integral action time of the controller (TI).
2. If the controller structure contains a proportional action, enter the "proportional gain".   
   A negative proportional gain inverts the rule meaning.

#### Proportional action

For changes of the setpoint, it may lead to overshooting of the proportional action. Through the weighting of the proportional action, you can select how strongly the proportional action should react when setpoint changes are made. The weakening of the proportional action is reached through a compensation of the integral action.

1. To weaken the proportional action for setpoint changes, enter a "Proportional action weighting".

   - 1.0: Proportional action for setpoint change is fully effective
   - 0.0: Proportional action for setpoint change is not effective

#### Integral action

1. If the controller structure contains an integral action, enter the "integral action time".   
   With an integral action time of 0.0, the integral action is switched off.

---

**See also**

[Mode of operation TCONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_s-s7-300-s7-400)

### Configure manipulated value TCONT_S (S7-300, S7-400, S7-1500)

#### Pulse generator

1. Enter the minimum impulse duration and minimum pause duration.  
   The values must be greater than or equal to the cycle time for the input parameter CYCLE. The frequency of operation is reduced through this.
2. Enter the motor setting time.   
   The value must be greater than or equal to the cycle time of the input parameter CYCLE.

---

**See also**

[Mode of operation TCONT_S (S7-300, S7-400)](PID%20Basic%20Functions%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tcont_s-s7-300-s7-400)

### Commissioning TCONT_S (S7-300, S7-400, S7-1500)

#### Requirements

- The instruction and the technology object have been loaded to the CPU.

#### Procedure

To manually determine the optimal PID parameters, proceed as follows:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value and output value are recorded.
2. Enter new PID parameters in the "P", "I" and weighting proportional action fields.
3. Click on the icon ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png)"Send parameter to CPU" in the "Tuning" group.
4. Select the "Change setpoint" check box in the "Current values" group.
5. Enter a new setpoint and click the ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png) icon in the "Current values" group.
6. Clear the "Manual mode" check box.

   The controller works with the new parameters and controls the new setpoint.
7. Check the quality of the PID parameter to check the curve points.
8. Repeat steps 2 to 6 until you are satisfied with the controller results.
