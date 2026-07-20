---
title: "Basics on controller modules (S7-300, S7-400)"
package: TFPIDFMenUS
topics: 45
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Basics on controller modules (S7-300, S7-400)

This section contains information on the following topics:

- [Inputs (S7-300, S7-400)](#inputs-s7-300-s7-400)
- [Error signal (S7-300, S7-400)](#error-signal-s7-300-s7-400)
- [Control algorithm (S7-300, S7-400)](#control-algorithm-s7-300-s7-400)
- [Controller output (S7-300, S7-400)](#controller-output-s7-300-s7-400)
- [Shared Device support (S7-300, S7-400)](#shared-device-support-s7-300-s7-400)

## Inputs (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction (S7-300, S7-400)](#introduction-s7-300-s7-400)
- [Analog inputs (S7-300, S7-400)](#analog-inputs-s7-300-s7-400)
- [Digital Inputs (S7-300, S7-400)](#digital-inputs-s7-300-s7-400)
- [Parallel tuning (S7-300, S7-400)](#parallel-tuning-s7-300-s7-400)

### Introduction (S7-300, S7-400)

You can connect different types of sensors to the analog inputs. The sensor input signals are then processed to suit your requirements.

The digital inputs can be used to set different operating modes for the module.

The structure of analog and digital inputs is identical on continuous and step controllers.

#### Number of inputs

| Input | FM 355 | FM 355-2 | FM 455 |
| --- | --- | --- | --- |
| Analog inputs for analog value processing | 4 | 4 | 16 |
| Reference junction input for the compensation of thermocouples | 1 | 1 | 1 |
| Digital inputs | 8 | 8 | 16 |

### Analog inputs (S7-300, S7-400)

#### Function blocks of an analog input

The following figure shows how analog values are prepared:

![Function blocks of an analog input](images/22936353675_DV_resource.Stream@PNG-en-US.png)

#### Adaptation to sensors

You can set up the analog input parameters to suit different sensors. The following settings are available:

- Analog input is not processed (e.g., unused input)

  With this setting, all PID parameters are set to zero, the controller channel is not processed, and a manipulated variable is not calculated.
- Current sensor, 0 mA to 20 mA
- Current sensor, 4 mA to 20 mA
- Voltage sensor, 0 V to 10 V
- Pt 100, –200 °C to +850 °C
- Pt 100, –200 °C to +556 ºC (double resolution)
- Pt 100, –200 °C to +130 ºC (quadruple resolution)
- Thermocouples type B, J, K, R, and S (analog input set to ±80 mV)
- Free thermocouple (analog input set to ±80 mV)

You assign the parameters for analog inputs in the "Analog input" screen form.

#### Toggling between Celsius / Fahrenheit

Temperatures can be measured in °C or °F units.

#### Adaptation to the line frequency

Input signal processing can be adapted to the line frequency in order to suppress interference during the measurement of analog signals. The following settings are available:

- 50 Hz mode
- 60 Hz mode

#### Reference junction

If you set up a thermocouple as sensor on an analog input, you can connect a Pt 100 to the reference junction input of the module in order to compensate for the reference junction temperature at the thermocouple elements. You can also configure a static reference junction temperature.

Alternatively, with the FM 355, you can assign parameters for an internal compensation for thermocouples J, K and E. An internal temperature sensor measures the reference junction temperature directly in the module.

When using the reference junction input, the sampling time of each controller extends by the conversion time for the reference junction input.

#### Analog value processing

The analog value processing offers various assignable options for preparing input signals. The following table offers an overview of these parameters and their assignable values.

| Parameter | Assignable values | Note |
| --- | --- | --- |
| Resolution | - 12 bits  - 14 bits | Conversion time 20 ms (50 Hz)  Conversion time 16<sup>2</sup>/<sub>3</sub> ms (60 Hz)  Conversion time 100 ms |
| Filters | - ON / OFF - Time constant in s | Filter of the first order whose time response is defined by the time constant. |
| Square root | - ON / OFF | For the linearization of sensor signals, where the process value is available as physical quantity with quadratic relation with the measured process variable. |
| Polyline | - ON / OFF - 13 interpolation points can be selected in   - mA with current input   - mV with voltage input | To linearize encoder characteristics |
| Standardization | - High value - Low value | For conversion of the input signal to a different unit of measurement by means of linear interpolation between the start value (low) and end value (high) |

> **Note**
>
> **Standardization/polyline**: The conversion of the unit mA or mV into a unit of measurement takes place either via the polyline or - if this is not enabled - via scaling. The polyline is used for linearization of a free thermocouple, or for any other linearization.

#### Copying parameters

Using the analog input of the FMs, you can transfer the parameters of one input to one or more other inputs. In doing so, all assigned parameters of the output channel are transferred to the destination channels.

### Digital Inputs (S7-300, S7-400)

#### Operating modes

The digital inputs are used to change the operating mode of individual controller channels.

The direction of control action of the digital inputs can be configured. The following settings are available for the digital inputs:

- Active high
- Active low, or open circuit

You can select the following operating modes:

- Changeover to manipulated value setpoint by calling FB PID_FM
- Changeover to following mode (manipulated value setpoint via analog input)
- Changeover to safety manipulated value

For the step controller, you can also define the following signals via digital inputs:

- Feedback: Actuating device at high limit stop
- Feedback: Actuating device at low limit stop

### Parallel tuning (S7-300, S7-400)

The "Parallel tuning" function is only available for FM 355-2.

#### Adjacent zones (heavy thermal coupling)

If using two or several temperature controls of a module to control the temperature, for example, of a plate (e.g. two heaters and two measured process values with heavy thermal coupling), you can tune these in parallel. Proceed as follows:

1. Define the channel group in zone A or zone B.
2. Start tuning in one of these channels. Tuning of the other channels will then be started automatically.

   > **Note**
   >
   > However, for excitation by means of setpoint step, you have to ensure that the setpoint steps are set simultaneously. When using the wizard, you can specify the PID_ON and TUN_DLMN/ TUN_CLMN parameters only for one channel. Specify the parameters for the other channels by means of the corresponding instance DBs of FB FMT_PID before you start tuning.

#### Cancelling tuning

Tuning of all channels is cancelled if an error occurs in one of the channels (phase 0, or end of phase 1).

The user can reset tuning by setting TUN_ON=FALSE at any one of the participating channels.

When a channel goes into safety mode, tuning of all other participating channels is also disabled.

The wizard displays only the status information of the selected channel. For all other channels, the causes of error are found in the corresponding instance DBs.

#### Advantage

Each participating controller will output its tuning manipulated variable until all controllers have exited phase 2. This prevents the controller that completes tuning first from corrupting the tuning results of the other controllers due to the change of its manipulated variable.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| When 75% of the setpoint step is reached at one of the participating channels, tuning is not terminated (risk of overshoot). Automatic mode is not started unless all participating controllers have completed tuning. |  |

#### Adjacent zones (weak thermal coupling)

As a general rule, tuning should be carried out to reflect the way in which the control will later work. When zones are operated in parallel during production so that temperature differences between the zones remain the same, the temperature level of the adjacent zones should also be raised accordingly during tuning.

Temperature differences at the start of testing are irrelevant since they will be compensated for in the initial heating process (initial rise = 0).

## Error signal (S7-300, S7-400)

This section contains information on the following topics:

- [Copying channels (S7-300, S7-400)](#copying-channels-s7-300-s7-400)
- [Controller types (S7-300, S7-400)](#controller-types-s7-300-s7-400)
- [Signal selection for setpoint value, actual value, D-action input and disturbance variable (S7-300, S7-400)](#signal-selection-for-setpoint-value-actual-value-d-action-input-and-disturbance-variable-s7-300-s7-400)
- [Preparation setpoint (S7-300, S7-400)](#preparation-setpoint-s7-300-s7-400)
- [Preparation actual value (S7-300, S7-400)](#preparation-actual-value-s7-300-s7-400)
- [Interrupt (S7-300, S7-400)](#interrupt-s7-300-s7-400)

### Copying channels (S7-300, S7-400)

The FMs support the transfer of a controller channel to one or several other channels. All output channel settings are transferred to the target channels.

### Controller types (S7-300, S7-400)

The error signal is derived from the same structure in all controller modules.

1. The signal for the actual value is conditioned to the effective actual value.
2. The setpoint signal is conditioned to the effective setpoint.
3. The effective setpoint is deducted from the effective actual value.
4. The error signal is transferred to the control algorithm.

You can select the signal sources for the setpoint and actual value and use the controller modules as:

- Fixed setpoint and cascade controllers
- Three-component controllers
- Ratio/blending controllers

#### Fixed setpoint and cascade controllers

The setpoint value of a master controller is set as the manipulated value of a slave controller in a cascade control.

#### Three-component controllers

Three-component controllers have three actual value inputs. For a blending control, the actual values A, B, and C are added to produce the total quantity PV.

- Blending controls

  A blending control is always slave controller. The associated master controller is a three-component controller.

  The manipulated variable of the master controller is interconnectd via the actual value D input. The blending factor is defined by the value at the setpoint input of the controller.

#### Ratio controllers

A ratio controller is always a slave controller. The associated master controller is a fixed-point controller.

The actual value of the master controller is selected as actual value D. The ratio factor is defined by the value at the setpoint input. If a controller output is activated as ratio factor, the setpoint value is converted from "0 .. 100%" to the value range "low threshold ... high threshold" using the high and low thresholds (normalized).

#### Blending controls

A blending control is always slave controller. The associated master controller is a three-component controller.

The manipulated variable of the master controller is activated as process value D. The blending factor is defined by the value at the setpoint input of the controller.

The manipulated variable of the total quantity controller is set to a range of values from 0% and 100%. The slave controller converts this variable to the range of actual value A at actual value input D. The range of actual value A is defined by the "high" and "low" normalization values of the selected analog input.

When the manipulated variable of a slave controller has reached the limiting threshold, or the setpoint gradient of a slave controller is limited by the ramp function in the setpoint value branch, the integral component of the master controller is blocked depending on the direction (anti-reset windup) until the cause of limiting has been eliminated in the slave controller.

### Signal selection for setpoint value, actual value, D-action input and disturbance variable (S7-300, S7-400)

#### Signal selection

You can activate different signal sources for the setpoint, actual value, value at the D input (derivative action input), and disturbance variable at each controller channel. The following table provides an overview of the signal selection options.

Signal selection for setpoints, actual values, D input, and disturbance variables.

| Affected values | Signal sources available |
| --- | --- |
| Setpoint | - A value defined by the function block in the user program - The conditioned analog value of an analog input - The manipulated value (LMN, LMN_A or LMN_B) of another controller channel (when cascading controllers) |
| Actual values A, B, and C | - Zero - The conditioned analog value of an analog input   (the actual values B and C can also be evaluated by factors) |
| Actual value D | - Zero - The conditioned analog value of an analog input - Setpoint of another controller channel |
| Value for D input (only relevant for PD or PID controllers) | - The error signal following the deadband of the internal controller channel - The conditioned analog value of an analog input - The negated effective actual value of the controller channel |
| Disturbance variable | - Zero - The conditioned analog value of an analog input |

### Preparation setpoint  (S7-300, S7-400)

The conditioning of a setpoint to the effective process value can be influenced by the following functions:

#### Setpoint source

The setpoint can be defined by:

- an instruction
- an analog input
- the conditioned output value of another controller channel in the module

  This source for the output value is selected for a blending controller, or slave controller in a cascade control.
- the conditioned output value A of another controller channel in the module (FM 355-2 only)
- the conditioned output value B of another controller channel in the module (FM 355-2 only)

#### Safety setpoint

When the CPU fails or with a CPU stop, the module can set a safety setpoint.

Enter a safety setpoint and set "Setpoint = Safety setpoint" as behavior to CPU stop.

#### Reaction to CPU failure

The controller module can set the following setpoints if the CPU fails or with a CPU stop:

- Setpoint = last valid setpoint

  If the "from instruction" is set as the setpoint selection, the setpoint will remain constant at the last value set after CPU failure or CPU stop.

  If the setpoint is defined by the output value of an FM controller, or by an analog input, the setpoint will change in line with the activated value.
- Setpoint = safety setpoint

  If you entered a safety setpoint, the module corrects the setpoint to this value.

#### Reaction to module start (FM 355 and FM 455 only)

The controller module can correct the values to the following setpoints during the start of module:

- Setpoint = last valid setpoint
- Setpoint = safety setpoint

#### Ramp

You can limit the setpoint rate of change by selecting a ramp up time that covers the physical start to the end value.

#### Setpoint limits

If the setpoint is defined by the function block, or by a conditioned analog value of an analog input, the setpoint is limited to configurable high and low limits.

If the conditioned output value of another controller channel has been activated as setpoint for the ratio controller, this value is used as multiplication factor for process value D. The setpoint, given as a percentage at the input, can in this case be scaled using the high and low limits.

If the output value of another controller channel is used as setpoint for a fixed setpoint or cascade controller, this value can be scaled to a physical value with the help of the normalization constants of the process value channel selected.

#### Multiplication

Process value A is used as controlled variable, while process value D is used as ratio variable for the "ratio controller" type. The setpoint input acts as the ratio factor. It is conditioned to form an effective setpoint by multiplication with process value D and adding an adjustable offset. If process value D is disabled, only the offset is added to the setpoint.

### Preparation actual value  (S7-300, S7-400)

Actual value conditioning to form the effective actual value depends on the controller structure.

#### Effective actual value for fixed setpoint and cascade controllers

The effective actual value is equivalent to actual value A that can be derived from an analog input source. Actual values B, C, and D are ignored.

#### Effective actual value for three-component controllers

The effective actual value is calculated by adding the actual values A, B, and C plus an adjustable offset. The actual values B and C can also be evaluated by factors. Actual value D is ignored.

#### Effective actual value in ratio controllers

Select the following actual values for the ratio controller

- Actual value A: The conditioned signal of an analog input
- Actual value D: Actual value of the master controller.

The ratio factor is defined as setpoint.

If a controller output has been activated as ratio factor FAC, the setpoint is converted from "0 ...100%" to the value range "low threshold ... high threshold" using the low and high thresholds (scaled).

#### Effective actual value in blending controllers

Select the following actual values for the blending controller

- Actual values A, B, and C The conditioned signals of the associated analog inputs.
- Actual value D: Actual value of the master controller.

The ratio factors of the individual controlled systems are defined as setpoint.

The manipulated variable of the total quantity controller is set in the range of values from "0% to 100%". The slave controller converts this variable at input D to the range of values between "low threshold ... high threshold" of actual value A (scaled).

The manipulated variable of the master controller is interconnected via "Actual value D" input of the slave controller. Blending factor FAC is defined by the value set at the controller's setpoint input.

### Interrupt (S7-300, S7-400)

#### Limit monitoring

The controller module contains a limit monitoring function. This enables monitoring of the high and low limits

- of the control deviation
- of the effective process value

for high and low limits warnings and alarms. You can set up a hysteresis for these limits.

The following figure shows the hysteresis for warning and alarm limit:

![Limit monitoring](images/22936471051_DV_resource.Stream@PNG-en-US.png)

## Control algorithm (S7-300, S7-400)

This section contains information on the following topics:

- [FM 355-2 control algorithm (S7-300, S7-400)](#fm-355-2-control-algorithm-s7-300-s7-400)
- [FM 355 and FM 455 control algorithm (S7-300, S7-400)](#fm-355-and-fm-455-control-algorithm-s7-300-s7-400)
- [Selecting the operating mode (S7-300, S7-400)](#selecting-the-operating-mode-s7-300-s7-400)
- [Dead zone (S7-300, S7-400)](#dead-zone-s7-300-s7-400)
- [Proportional control (S7-300, S7-400)](#proportional-control-s7-300-s7-400)
- [PI control (S7-300, S7-400)](#pi-control-s7-300-s7-400)
- [PD control (S7-300, S7-400)](#pd-control-s7-300-s7-400)
- [PID control (S7-300, S7-400)](#pid-control-s7-300-s7-400)
- [I control (S7-300, S7-400)](#i-control-s7-300-s7-400)
- [Proportional action (S7-300, S7-400)](#proportional-action-s7-300-s7-400)
- [Derivative action (S7-300, S7-400)](#derivative-action-s7-300-s7-400)
- [Proportional/Derivative action (S7-300, S7-400)](#proportionalderivative-action-s7-300-s7-400)
- [Fuzzy temperature controller module (S7-300, S7-400)](#fuzzy-temperature-controller-module-s7-300-s7-400)

### FM 355-2 control algorithm (S7-300, S7-400)

#### Components of the control algorithm

Continuous controllers (FM 355-2 C) and pulse controllers (FM 355-2 S) have the same control algorithm structure. The cooling and control zone buttons cannot be selected for the step controller (FM 355-2 S).

The following figure shows the block diagram of the control algorithm for continuous and pulse controllers.

![Components of the control algorithm](images/24633803275_DV_resource.Stream@PNG-en-US.png)

#### Control algorithm: PID in parallel structure

During the cycle of the configured sampling time, the controller’s manipulated variable is calculated based on the control deviation of the PID position algorithm. The controller is implemented in a purely parallel structure. The proportional, integral and derivative actions can each be disabled separately. To disable the integral and derivative actions, set the respective parameter TI or TD to zero.

The following figure shows the control algorithm of the FM 355-2 (parallel structure):

![Control algorithm: PID in parallel structure](images/24633830283_DV_resource.Stream@PNG-en-US.png)

### FM 355 and FM 455 control algorithm (S7-300, S7-400)

#### Components of the control algorithm

You can choose between the following operating modes of the control algorithm:

- Temperature controller (self-tuning fuzzy controller)
- PID controller

C and S controllers have the same control algorithm structure. The following figure shows the block diagram of the control algorithm:

![Components of the control algorithm](images/22937273355_DV_resource.Stream@PNG-en-US.png)

#### Control algorithm and controller structure

The manipulated variable of the continuous controller is calculated within the configured sampling time on the basis of the control deviation in the PID positioning algorithm. The controller is designed with a purely parallel structure (see figure below). The proportional, integral and derivative actions can each be disabled separately. To disable the integral and derivative actions, set the respective parameter TI or TD to zero.

The following figure shows the control algorithm of the FM 355 (parallel structure):

![Control algorithm and controller structure](images/26083747211_DV_resource.Stream@PNG-en-US.png)

### Selecting the operating mode (S7-300, S7-400)

#### Selecting the operating mode

You can choose between different operating modes if the "PID controller" entry has been set as controller type:

- P, for implementing a proportional controller
- PI, for implementing a PI controller
- PD, for implementing a PD controller
- PID, for implementing a PID controller
- I, for implementing an integrating controller
- ID, for implementing an ID controller
- D, for implementing a D controller

#### Bumpless change from manual to automatic mode

If you selected “Bumpless change from manual to automatic mode” (not available for step controllers), the integrator is tracked in manual mode so that the manipulated variable does not take a step through the proportional and derivative actions during the manual to automatic changeover. An error signal is corrected only slowly by means of the integral action. If bumpless manual to automatic changeover is not selected, the manipulated variable performs a step that corresponds with the current error signal during the change from manual to automatic mode. This function allows for the fast correction of active control error.

> **Note**
>
> A step controller is always subject to pulse action at the changeover from manual to automatic mode. The existing error signal and GAIN leads to a jump in the internal manipulated variable. The integral effect of the actuator, however, results in a ramp-shaped excitation of the process.

#### Disturbance variable compensation

An additional disturbance variable DISV can be added to the controller’s output signal. This is activated and deactivated in the “System deviation” window of the configuration tool using the switch “Signal selection, controller disturbance variable”.

### Dead zone (S7-300, S7-400)

#### Purpose of the deadband

A deadband is interconnected upstream of the PID controller. In settled controller state, the deadband suppresses the noise component in the error signal that could be generated by superimposition of a disturbance signal of higher frequency on the control or reference variable. This function prevents unwanted oscillation of the controller output.

#### Deadband width

The deadband width can be configured. If the error signal is within the set dead band width, the value 0 (error signal = 0) is returned at the deadband output. The output value does not follow the input variable until the input variable moves outside the sensitivity range.

This results in corruption of the transferred signal even outside the deadband. However, this is accepted in order to avoid jumps at the limits of the deadband. The corruption corresponds to the value of the deadband width and can therefore be controlled easily.

![Deadband](images/24633862539_DV_resource.Stream@PNG-en-US.png)

Deadband

### Proportional control (S7-300, S7-400)

#### Proportional controller

The following figure shows the step response of a proportional controller:

![Proportional controller](images/22939777035_DV_resource.Stream@PNG-en-US.png)

#### Formula for proportional controllers

The output and input variables are directly proportional, i.e.:

Change to the output variable = proportional coefficient x change to input variable

**LMN = GAIN x ER**

#### Proportional control

The integral and derivative actions are disabled in a proportional controller. This means that the manipulated variable is also "0" when control deviation ER = 0. If an operating point ≠0, in other words, a numeric value is to be set for the manipulated variable when control deviation = 0, the following is possible via the operating point:

- Automatic operating point: The controller automatically sets the operating point to the value of the current (manual) manipulated variable when you switch from manual to automatic mode.
- Operating point not automatic: You can assign the operating point parameters.
- Example: Operating point AP = 5% results in a manipulated variable of 5% when control deviation ER = 0.

The following figure shows a proportional controller with operating point setting by means of an integral element:

![Proportional control](images/22939517707_DV_resource.Stream@PNG-en-US.png)

The following figure shows the step response of the proportional controller:

![Proportional control](images/22939756171_DV_resource.Stream@PNG-en-US.png)

### PI control (S7-300, S7-400)

#### PI controller

The following figure shows the step response of a PI controller:

![PI controller](images/22940543115_DV_resource.Stream@PNG-en-US.png)

Integral control elements have the integral of the input variable as the output variable, i.e. the controller adds up the deviation from the setpoint value over time. This means that the controller continues correction until the deviation from the setpoint is eliminated. In practice, depending on the demands on the controlling, a combination of the different timing elements is ideal. The timing of the individual elements can be described by the controller parameters Proportional band GAIN, Reset time TI (integral action) and Rate time TD (derivative action) .

#### Formula for PI controllers

The following applies for the step response of the PI controller in the time range:

![Formula for PI controllers](images/22940563979_DV_resource.Stream@PNG-en-US.png)

t = time interval since the input variable step

#### PI control

The derivative action is disabled in the PI controller (TD=0.0). A PI controller corrects the output variable by means of integration until control deviation ER = 0. However, this only applies if the output variable does not exceed the limits of the output range. The integral action retains the value reached at the output value limit if these limits are exceeded (anti-reset windup).

![PI control](images/22940253451_DV_resource.Stream@PNG-en-US.png)

### PD control (S7-300, S7-400)

#### PD controller

The following figure shows the step response of a PD controller:

![PD controller](images/22940206219_DV_resource.Stream@PNG-en-US.png)

The derivative control elements are the only ones unsuitable for controlling, because they no longer output actuating commands when the input variable has settled to a static value.

In combination with proportional control elements, the derivative action is used to generate a control pulse based on the rate of change at the controlled variable. If a disturbance variable z is affecting the controlled system, the PD controller sets a different control deviation as a result of the changed degree of correction. Disturbance factors are not fully corrected. Of advantage is the good dynamic response. A well attenuated, non-oscillating transfer is achieved during startup and when changing the reference input variable. However, a controller with derivative action is not appropriate if a control system has oscillating measured variables, e.g. in pressure or flow control systems.

#### Formula for PD controllers

The following applies for the step response of the PD controller in the time range:

![Formula for PD controllers](images/22940239883_DV_resource.Stream@PNG-de-DE.png)

t = time interval since the input variable step

#### PD control

The integral action is disabled in the PD controller (TI=0.0). This means also that output signal = 0 when control deviation ER = 0. If an operating point ≠0, in other words, a numeric value is to be set for the manipulated variable when control deviation = 0, the following is possible via the operating point:

- Automatic operating point: The controller automatically sets the operating point to the value of the current (manual) manipulated variable when you switch from manual to automatic mode.
- Operating point not automatic: You can assign the operating point parameters.

The PD controller maps input variable ER(t) proportionally to the output signal and adds the derivative action formed by the differentiation of ER(t); the derivative action is calculated with double precision according to the trapezoid rule (Padé approximation). The time response (strength of the derivative action or actuating area) is determined by the derivative action time TD (rate time).

For signal smoothing and interference suppression, the derivative action is implemented with a time lag of the first order (adjustable time constant: TM_LAG). A small value for TM_LAG is usually sufficient to achieve the desired result.

The higher the derivative factor D_F,

- the smaller the effective time constant TD/D_F of the delay,
- the higher the maximum initial manipulated variable,
- and the better the control action;
- the higher the noise sensitivity.

D_F is limited to the value range 5.0 through 10.0.

![PD control](images/22939814155_DV_resource.Stream@PNG-en-US.png)

### PID control (S7-300, S7-400)

#### PID controller

The following figure shows the step response of a PID controller:

![PID controller](images/22940767499_DV_resource.Stream@PNG-en-US.png)

Most control systems in process engineering can be managed with a controller with PI component. In the case of slow control systems with long dead times, for example temperature control systems, the control result can be improved with a controller with PID action.

The following figure shows the step response for various proportional controllers:

![PID controller](images/22940788363_DV_resource.Stream@PNG-en-US.png)

Controllers with PI and PID action have the advantage that the process variable does not deviate from the setpoint value after settling. The controlled variable oscillates above the setpoint value upon start-up.

#### Formula for PID controllers

The following applies for the step response of the PI controller in the time range:

![Formula for PID controllers](images/22940822027_DV_resource.Stream@PNG-de-DE.png)

t = time interval since the input variable step

#### PID control

The P, I and D actions are switched on in PID controllers. A PID controller adjusts the output variable via the integral action until the control deviation ER = 0. However, this only applies if the output variable does not exceed the limits of the output range. The integrator maintains the value it has at the point where the limits of the output value are exceeded (Anti-Reset-Windup).

The PID controller proportionally maps the input variable ER(t) to the output signal and then adds the actions generated by the differentiation and integration of ER(t). The time action is determined by the derivative action time TD (rate time) and the integration time TI (reset time).

The derivative action is realized with a delay circuit of the first order for signal smoothing and interference suppression.

The higher the derivative factor D_F,

- the smaller the effective time constant TD/D_F of the delay,
- the higher the maximum initial manipulated variable,
- and the better the control action;
- the higher the noise sensitivity.

D_F is limited to the value range 5.0 through 10.0.

![PID control](images/24633886347_DV_resource.Stream@PNG-en-US.png)

### I control (S7-300, S7-400)

#### Integral controller

You can deactivate the proportional action in order to realize a pure integral-action control. This can also be done using the P_SEL parameter of the PID_FM function block.

### Proportional action (S7-300, S7-400)

#### Attenuation of the proportional action in the event of setpoint changes

You can avoid process value overshoot or excessive manipulated variable amplitude with attenuation of the proportional action using the parameter “Proportional factor at setpoint change” (PFAC_SP). Using PFAC_SP, you can select continuously between 0.0 and 1.0 to decide the effect of the proportional action when the setpoint changes:

- PFAC_SP=1.0: Proportional action for setpoint change is fully effective
- PFAC_SP=0.0: Proportional action for setpoint change is not effective

There are two ways of limiting the rate of setpoint change in the FM355-2:

- Activate ramp (> 0.0s)
- Setpoint change factor < 1.0

Use only one of the two limits. If both limits are activated at the same time, a setpoint jump will produce a change in the manipulated variable in the opposite direction to the setpoint change (step response).

#### Specific features of the step controller

A value of PFAC_SP < 1.0 can reduce overshoot if the motor transition time MTR_TM is small compared to the recovery time TA and if the ratio TU/TA < 0.2. Should MTR_TM reach 20 % of TA, only a slight improvement can be achieved.

#### Inversion of the controller effect

You can enable controller inversion, that is, conversion from

- increasing control deviation = rising manipulated variable

  to
- rising control deviation = falling manipulated variable

by setting a negative proportional gain (GAIN). The sign of this parameter value determines the effective direction of the controller.

### Derivative action (S7-300, S7-400)

#### Derivative action in feedback path

When the setpoint changes, you can avoid pulse-shaped peaks of the derivative action of the manipulated variable by moving the derivative action into the feedback path.

In this structure only the negative control variable (Factor = -1) is fed forward to the derivative action. Changeover for the derivative action is carried out in the feedback in the “Control deviation” window via the “Derivative input controller” switch by selecting the negated effective process value as the input signal.

> **Note**
>
> If you move the derivative action to the feedback path, you should also reduce the value of PFAC_SP, otherwise you would increase overshoot of the process value.

The following figure shows the control algorithm with derivative action in the feedback branch:

![Derivative action in feedback path](images/24633914379_DV_resource.Stream@PNG-de-DE.png)

### Proportional/Derivative action (S7-300, S7-400)

#### P/D action in the feedback

In the parallel structure, each action in the control algorithm receives the control deviation as input signal. In this structure, setpoint steps act directly on the controller. The manipulated variable is influenced directly by the proportional and derivative actions by setpoint steps.

However, a different controller structure, in which the formation of the proportional and derivative action is moved to the feedback, ensures a smooth response of the manipulated variable to setpoint step changes (see figure below).

In this structure, the integral action processes the control deviation as the input signal. Only the **negative** controlled variable (factor = - 1) is applied to the proportional and derivative actions. Changeover for the derivative action is carried out in the feedback in the “Control deviation” window via the “Derivative input controller” switch by selecting the negated effective process value as the input signal.

The following figure shows the control algorithm with proportional and derivative action in the feedback branch:

![P/D action in the feedback](images/26084300683_DV_resource.Stream@PNG-de-DE.png)

### Fuzzy temperature controller module (S7-300, S7-400)

#### Temperature controller

The temperature controller is a self-regulating fuzzy controller, which, after identifying the control section, works using control parameters it has calculated itself.

The following temperature controller settings are possible:

- Cooling controller
- Heating controller
- Aggressivity

  The aggressivity parameter can be used to influence the speed of the transient response.

| Possible aggressivity values: |  |
| --- | --- |
| -1 ≤ Aggressivity < 0 : | Slower transient response than determined by identification |
| Aggressivity = 0 | Transient response as determined via identification |
| 0 < Aggressivity ≤ 1 | Faster transient response than determined by identification |

## Controller output (S7-300, S7-400)

This section contains information on the following topics:

- [Differences between controllers (S7-300, S7-400)](#differences-between-controllers-s7-300-s7-400)
- [Controller analog outputs (S7-300, S7-400)](#controller-analog-outputs-s7-300-s7-400)
- [Digital controller outputs (S7-300, S7-400)](#digital-controller-outputs-s7-300-s7-400)
- [Continuous controller (S7-300, S7-400)](#continuous-controller-s7-300-s7-400)
- [Step controller without position feedback (S7-300, S7-400)](#step-controller-without-position-feedback-s7-300-s7-400)
- [Step controller with position feedback (S7-300, S7-400)](#step-controller-with-position-feedback-s7-300-s7-400)
- [Pulse controller (S7-300, S7-400)](#pulse-controller-s7-300-s7-400)
- [Functions of the controller output (S7-300, S7-400)](#functions-of-the-controller-output-s7-300-s7-400)

### Differences between controllers (S7-300, S7-400)

The FM 355, FM 355-2 and FM 455 controllers are basically divided into two types: step controllers and continuous controllers. Step controllers are identified by an added S, such as FM 355 S, FM 355-2 S and FM 455 S, whereas continuous controllers are identified with a C, such as FM 355 C, FM 355-2 C and FM 455 C. The way the controller modules work do not differ, an FM 355 S and an FM 355 have identical algorithms. The differences lie in the controller output.

#### Step controller

The continuous step controller has digital outputs. Therefore, a control valve can only be addressed by the signals "open" or "closed". If you wish to control a control valve for 50% of the capacity, for example, this can only be realized by setting "open" and "closed" to an equal length.

You can find more detailed information on step controllers at the following locations:

- [Digital controller outputs](#digital-controller-outputs-s7-300-s7-400)
- [Step controller without position feedback](#step-controller-without-position-feedback-s7-300-s7-400)
- [Step controller with position feedback](#step-controller-with-position-feedback-s7-300-s7-400)
- [Pulse controller](#pulse-controller-s7-300-s7-400)

#### Continual controller

The continuous step controller has analog outputs. A control valve can not only be "open" or "closed", it can also be opened by specific percentages. If you wish to control a control valve for 50% of the capacity, for example, the controller module outputs the value "50%" and the door opens halfway.

You can find more detailed information on continuous controllers at the following locations:

- [Controller analog outputs](#controller-analog-outputs-s7-300-s7-400)
- [Continuous controller](#continuous-controller-s7-300-s7-400)

### Controller analog outputs (S7-300, S7-400)

#### Analog outputs

You can assign parameters for the following functions for each analog output:

- Signal source
- Signal type

#### Selection of source for the signal at the analog outputs

Selection of the signal source allows you to define which signal value is to be output at the analog output in question.

The following signal sources can be assigned:

- The value zero
- The conditioned analog value of one of the analog inputs
- Manipulated value A of one of the controller channels
- Manipulated value B of one of the controller channels

The FM 355 and FM 355-2 each have four analog inputs and four controller channels.

The FM 455 has 16 analog inputs and 16 controller channels.

#### Signal Type at the analog outputs

You can determine the signal type for each analog output.

The following signal types can be assigned:

- Current output 0 ... 20 mA
- Current output 4 ... 20 mA
- Voltage output 0 ... 10 V
- Voltage output -10 ... 10 V

### Digital controller outputs (S7-300, S7-400)

#### Digital controller outputs

The digital outputs of the controller are used to control integrating and non-integrating actuators.

You can assign the following functions to each digital output:

- Output type
- Signal selection
- Signal processing

#### Signal output type at the digital output

You can define the signal type for each digital output.

The following signal types are available:

- Step controller w/o position feedback input
- Step controller with position feedback input
- Pulse controller

#### Signal selection

A range of values can be assigned for signal selection depending on the signal type at the output:

- [External manipulated variable](#external-manipulated-variable-s7-300-s7-400)
- [Compensation](#compensation-s7-300-s7-400)
- [Position feedback input](#position-feedback-s7-300-s7-400)
- [Safety manipulated value](#safety-manipulated-value-s7-300-s7-400)

#### Signal processing

A range of values can be assigned for signal processing depending on the signal type at the output:

- [Output signal limit](#manipulated-value-limitation-s7-300-s7-400)
- [Split range](#split-range-s7-300-s7-400)
- [Pulse shaper](#pulse-shaper-of-the-step-controller-s7-300-s7-400)

### Continuous controller (S7-300, S7-400)

#### Signal type at the digital outputs

The following parameters can only be set for an analog module.

#### Available parameters

- Activate[external manipulated variable](#external-manipulated-variable-s7-300-s7-400)
- Activate[compensation](#compensation-s7-300-s7-400)
- Set[safety manipulated value](#safety-manipulated-value-s7-300-s7-400)
- [Limit manipulated value](#manipulated-value-limitation-s7-300-s7-400)
- [Enable two actuators](#split-range-s7-300-s7-400)
- [Select output signal and signal type](#select-output-signal-and-signal-type-s7-300-s7-400)

### Step controller without position feedback (S7-300, S7-400)

#### Signal type at the digital outputs

The following parameters can only be set for a digital module.

#### Available parameters

- Activate[external manipulated variable](#external-manipulated-variable-s7-300-s7-400)
- Set[safety manipulated value](#safety-manipulated-value-s7-300-s7-400)
- [Pulse shaper](#pulse-shaper-of-the-step-controller-s7-300-s7-400)

### Step controller with position feedback (S7-300, S7-400)

#### Signal type at the digital outputs

The following parameters can only be set for a digital module.

#### Available parameters

- Activate[external manipulated variable](#external-manipulated-variable-s7-300-s7-400)
- Activate[compensation](#compensation-s7-300-s7-400)
- Set[safety manipulated value](#safety-manipulated-value-s7-300-s7-400)
- [Limit manipulated value](#manipulated-value-limitation-s7-300-s7-400)
- Set[position feedback](#position-feedback-s7-300-s7-400)
- [Pulse shaper](#pulse-shaper-of-the-step-controller-s7-300-s7-400)

### Pulse controller (S7-300, S7-400)

#### Signal type at the digital outputs

The following parameters can only be set for a digital module.

#### Available parameters

- Activate[external manipulated variable](#external-manipulated-variable-s7-300-s7-400)
- Activate[compensation](#compensation-s7-300-s7-400)
- Set[safety manipulated value](#safety-manipulated-value-s7-300-s7-400)
- [Limit manipulated value](#manipulated-value-limitation-s7-300-s7-400)
- [Conditioning analog signal for conversion to a digital signal](#split-range-s7-300-s7-400)
- [Converting analog signal to digital signal](#analog-inputs-s7-300-s7-400)

### Functions of the controller output (S7-300, S7-400)

This section contains information on the following topics:

- [External manipulated variable (S7-300, S7-400)](#external-manipulated-variable-s7-300-s7-400)
- [Compensation (S7-300, S7-400)](#compensation-s7-300-s7-400)
- [Position feedback (S7-300, S7-400)](#position-feedback-s7-300-s7-400)
- [Safety manipulated value (S7-300, S7-400)](#safety-manipulated-value-s7-300-s7-400)
- [Manipulated value limitation (S7-300, S7-400)](#manipulated-value-limitation-s7-300-s7-400)
- [Split range (S7-300, S7-400)](#split-range-s7-300-s7-400)
- [Pulse shaper of the step controller (S7-300, S7-400)](#pulse-shaper-of-the-step-controller-s7-300-s7-400)
- [Select output signal and signal type (S7-300, S7-400)](#select-output-signal-and-signal-type-s7-300-s7-400)

#### External manipulated variable (S7-300, S7-400)

##### Overview

There are various interconnection possibilities for the manipulated value, the compensation input and the safety manipulated value at the controller output (manipulated value changeover).

A limit ensures that the manipulated value cannot assume invalid values for the process.

##### Switching external manipulated value

The changeover between external manipulated value and effective manipulated value from the controller can alternatively take place using

- A binary value from the function block
- A signal from a logical OR link of a digital value from a function block and a digital input.

#### Compensation (S7-300, S7-400)

##### Overview

Manipulated value compensation prevents a jump in the manipulated value during the changeover from manual to automatic mode.

The manipulated value remains unchanged during the changeover from manual to automatic mode. Manipulated value compensation is not active if a purely proportional controller with a fixed operating point has been implemented (”automatic” is not checked in the PID controller screen).

##### Compensation input

The following alternative settings are available:

- The value at the compensation input = zero
- The compensation input is the conditioned analog value of an analog input

##### Switching to compensation

You can also change from manipulated value to compensation input using

- A binary value from the function block
- A signal from a logical OR link of a digital value from a function block and a digital input.

#### Position feedback (S7-300, S7-400)

##### Overview

A position feedback input is only available for step controllers.

##### Position feedback input

The following alternative settings are available:

- The position feedback input value = zero
- The position feedback input is the conditioned analog value of an analog input

##### Controller output of the step controller

The following figure shows the principle of the S controller output (step controller operating mode with position feedback):

![Controller output of the step controller](images/22941802891_DV_resource.Stream@PNG-en-US.png)

The following figure shows the principle of the S controller output (step controller operating mode without position feedback):

![Controller output of the step controller](images/22941938955_DV_resource.Stream@PNG-en-US.png)

In a step controller without analog position feedback, the external output value and the safety output value act as follows:

If a value between 40.0% and 60.0% is specified, no binary output is set and the actuating device remains unchanged.

If a value > 60.0% is specified, "Actuating signal high" is output until the feedback "Actuating device at high limit" is triggered.

If a value < 40.0% is specified, "Actuating signal low" is output until the feedback "Actuating device at low limit" is triggered.

#### Safety manipulated value (S7-300, S7-400)

##### Overview

There are various interconnection possibilities for the manipulated value, the compensation input and the safety manipulated value at the controller output (manipulated value changeover).

##### Safety manipulated value switching

- Establishing the safety manipulated value
- Alternative reaction of the function module upon start-up:

  - The function module switches to closed-loop operation
  - The safety manipulated value is output as the manipulated value
- Changeover to the safety manipulated value is also possible with

  - A binary value from the function block
  - A signal from a logical OR link of a digital value from a function block and a digital input.
- Reaction to measuring transducer fault of actual value A:

  - The operating mode of the controller remains unchanged when "Closed-loop control operation" is set
  - It changes to the safety manipulated value when "manipulated value = safety manipulated value" is set
- Reaction to analog input measuring transducer fault:

  - The operating mode of the controller remains unchanged when "Closed-loop control operation" is set
  - It changes to the safety manipulated value when "manipulated value = safety manipulated value" is set

#### Manipulated value limitation (S7-300, S7-400)

##### Overview

A limit ensures that the manipulated value cannot assume invalid values for the process.

##### Manipulated value limit

- High and low limit (cannot be switched off)

#### Split range (S7-300, S7-400)

##### Overview

The split range function generates two differently standardized output signals, output value A and output value B, from the output value as input signal. This allows two valves, for example, to be controlled with one output value.

##### Formation of the split range output value

- In / out (C controllers only)
- Initial and final value - input signal
- Initial and final value of the output signal

##### Split range

The splitrange function allows two control valves to be controlled with one manipulated variable. The split range function generates the two output signals output value A and output value B from the output value LMN as input signal.

The following figure shows the effect of the parameters for the output of output value A:

![Split range](images/24633931787_DV_resource.Stream@PNG-en-US.png)

The following figure shows the effect of the parameters for the output of output value B:

![Split range](images/22942413451_DV_resource.Stream@PNG-en-US.png)

The start of the input signal area must be less than the end of the input signal area.

##### Split range / pulse shaper

The split range function is the preparation of the analog signal for conversion to a binary signal.

In the case of a **two-step controller** (e. g. a heating controller), only the output value A is of relevance. The conversion of the output value to the output value A is shown in the following figure. Conversion to a binary output signal is carried out so that the ratio of pulse length to period duration corresponds to the output value A at the assigned digital output.

For example, a output value A of 40% and a period of 60 seconds result in a pulse length of 24 seconds and a pause duration of 36 seconds.

The figure below shows the split range function on a two-step controller:

![Split range / pulse shaper](images/24633948427_DV_resource.Stream@PNG-en-US.png)

The statements above apply for the output value A in the case of a **three-step controller** (for example, a heating and cooling controller). The second signal for controlling the cooling is generated via output value B. The conversion of the output value to the output values A and B is shown in the figure below. The conversion to a binary output signal is carried out so that the ratio of pulse length to period duration corresponds to the output values A and B at the assigned digital outputs.

The figure below shows the split range function on a three-step controller:

![Split range / pulse shaper](images/22942464011_DV_resource.Stream@PNG-en-US.png)

#### Pulse shaper of the step controller (S7-300, S7-400)

##### Overview

The pulse shaper is only available for step controllers (FM 355 S, FM 355‑2 S and FM 455). The followings settings can be configured.

##### Pulse shaper (step controllers only)

- Motor control time
- Minimum duration of pulse
- Minimum pause time

#### Select output signal and signal type (S7-300, S7-400)

##### Analog output

You can select which signal is to be output for each channel at the analog output. This is usually the output value A of a controller. However, you can also select the output value B of a controller or indeed an analog input value. The latter can be used for the linearization of an analog value. This allows, for example, the signal supplied by a thermocouple to be linearized and converted to a range of 0 V to 10 V.

##### Controller output of the pulse controller

The following figure shows the controller output of the step controller (pulse control mode):

![Controller output of the pulse controller](images/24633982347_DV_resource.Stream@PNG-en-US.png)

##### Controller output of the step controller

The following figure shows the controller output of the step controller (step control with position feedback mode):

![Controller output of the step controller](images/22942487179_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the step controller (step control without position feedback mode):

![Controller output of the step controller](images/22942879243_DV_resource.Stream@PNG-en-US.png)

In a step controller without analog position feedback, the external output value and the safety output value act as follows:

If a value between 40.0% and 60.0% is specified, no binary output is set and the actuating device remains unchanged.

If a value > 60.0% is specified, "Actuating signal high" is output until the feedback "Actuating device at high limit" is triggered.

If a value < 40.0% is specified, "Actuating signal low" is output until the feedback "Actuating device at low limit" is triggered.

## Shared Device support (S7-300, S7-400)

The controller modules FM 355 and FM 355-2 support the Shared Device functionality when using an ET 200M interface module.

General information on Shared Device is available at Configuring Shared Device.

### Use of Shared Device with the controller modules

To use Shared Device with the controller modules, the following additional organization blocks must be included in your program:

- **Insert/remove module interrupt OB (OB 83):**

  For configuration as a Shared Device, the OB 83 must be integrated into the block list, because the transition from STOP to RUN will generate so-called "Return of submodule" interrupts. The alarms are intercepted by the OB 83, otherwise the CPU would go into STOP with the event "STOP caused by removing/inserting module".
- **I/O access error OB (OB 122):**

  As long as CPU A is in STOP and CPU B is in RUN, "I/O access errors, writing" will occur in CPU B if instructions from the "FM 355 PID Control" or "FM 355-2 Temp Control" libraries are called in the program or other write access operations to module addresses are carried out. OB 122 intercepts these errors; otherwise, CPU B would switch to STOP with the event "STOP caused by I/O access error".
- **Priority class error OB (OB 85):**

  OB 85 must only be included if the option "No OB85 call" was not configured for the setting "OB85 call if I/O access error occurs" in the CPU properties under "Cycle". For all other options, an OB 85 call is also requested for the I/O access errors that are described above for OB 122. If OB 85 does not exist in this case, the CPU goes to STOP with the event "STOP caused by program sequence error".

Both CPUs must be in "RUN" so that write access to the module addresses and the instructions from the "FM355 PID Control" and "FM355-2 Temp Control" libraries can be executed correctly.

As long as one CPU is in STOP and the other is in RUN, all controller modules of this interface module work in backup mode. This is independent of the "access" that took place in the "Shared Device" settings of the interface module. Only when all CPUs are in RUN do the controller modules work in normal operation.
