---
title: "Running through the wizard"
package: StdrWizardenUS
topics: 34
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Running through the wizard

This section contains information on the following topics:

- [Commissioning wizard](#commissioning-wizard)

## Commissioning wizard

This section contains information on the following topics:

- [Application class](#application-class)
- [Options for cabinet unts](#options-for-cabinet-unts)
- [Setpoint specification](#setpoint-specification)
- [Open-loop/closed-loop control type](#open-loopclosed-loop-control-type)
- [Default settings of the setpoints / command sources](#default-settings-of-the-setpoints-command-sources)
- [Profile setting of AS-i device (G110M and G115D)](#profile-setting-of-as-i-device-g110m-and-g115d)
- [Drive setting](#drive-setting)
- [Drive options](#drive-options)
- [Motor](#motor)
- [Motor holding brake](#motor-holding-brake)
- [Drive functions](#drive-functions)
- [Important parameters](#important-parameters)
- [Configuring the encoder](#configuring-the-encoder)
- [Dimension system](#dimension-system)
- [Mechanical system (G120D only)](#mechanical-system-g120d-only)
- [Summary](#summary)

### Application class

#### Description

You can set the application class in the wizard function in the configuration. Select one of the following classes:

- Standard Drive Control
- Dynamic Drive Control
- Expert

The Expert functions include the Standard Drive Control and Dynamic Drive Control functions.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Standard Drive Control** | **Dynamic Drive Control** | **Expert** |
| Typical applications | - Pumps, fans and compressors with flow characteristic - Blasting technology (wet and dry blasting) - Mills, mixers, kneaders, crushers, agitators - Horizontal conveyor technology (conveyor belts, roller conveyors, chain conveyors) - Basic spindles | - Demanding applications with high utilization of the motor and converter - Pumps and compressors with displacement machines - Rotary kilns - Extruders - Centrifuges - Vertical conveyor technology (conveyor belts, roller conveyors, chain conveyors) with encoder - Escalators, lifting/lowering gear, elevators, overhead cranes with encoder - Cable railways with encoder - Stacker cranes with encoder - Encoderless synchronous motors - Reluctance motors | All setting options are available. |
| Typical characteristics | - Robust vector control for simple handling - Drive commissioning only via rated motor current/speed - Motor power up to 45 kW - Ramp times greater than 5 - 10 s - Continuous motion with constant load - Static torque limitation (500 ms) - Stationary speed accuracy (transient recovery time 100 - 200 ms) | - Precise vector control: Efficient utilization of power unit, motor and mechanical system - Particularly recommended for motor powers greater than 45 kW - Required for ramp times less than 2 s - Continuous motion with dynamic load - High speed control accuracy during setpoint response and transient response - Dynamically controlled transient response (fast, high load surges) - Dynamic torque limitation (20 ms) - Heavy starting (with up to 90% breakdown torque) | All setting options are available. |

> **Note**
>
> For SINAMICS G120, the application class can only be set for CU230P, CU240x-2, CU250S-2, G120C with PM240, PM240-2, PM340, PM330 and PM330L.

**Standard Drive Control**

The same performance such as U/f with FCC and slip compensation / speed accuracy is only restricted. There is therefore no speed controller and no torque accuracy.

Two rating plate parameters are required for the motor commissioning: Rated current and rated speed. The synchronous rated speed is accepted.

The motor data identification is preset. A short measurement is performed once (only stator resistance, dead time compensation) to improve the start-up. This is followed by a direct switchover to operation.

The optimization of the speed controller is not relevant.

> **Note**
>
> Note that the Standard Drive Control functions only apply to induction motors (Siemens and third-party motors).

**Dynamic Drive Control**

Compared to Standard Drive Control, the performance such as sensorless vector control / speed accuracy is significantly improved.

The robustness is improved with higher model change limits, but takes effect at slow reversing.

Three rating plate parameters are required for the motor commissioning: Rated current, rated power and rated speed.

The motor data identification is preset and serves to simplify and shorten the measurement compared with the existing standstill measurement. This is followed by a direct switchover to operation.

In the speed controller optimization, there is a shorter measurement of the moment of inertia / magnetizing current with direct transition to operation and the setpoint speed defined by the user.

****p0502****

A stationary starting torque and, if required, break loose torques must be parameterized for the control of the drive during sensorless vector control from standstill. The technological application that you can set in p0502 is suitable in the basic commissioning.

| Technological application (p0096 = dynamic) |  |  |  |  |  | Cross references |
| --- | --- | --- | --- | --- | --- | --- |
| Setting of the technological application for dynamic applications    0 = Operation without encoder (e.g. pumps, fans, compressors)  5 = Operation without encoder with high break loose torque (e.g. extruders) |  |  |  |  | Relevant to:  Induction motors | Protection level  Access level:  2 |
| **Mode** | **Unit** | **Default value** | **Min. value** | **Max value** | **Data type** | **FBD** |
|  | - | - | - | - | INT16 |  |
| **Index** |  |  | **Effectiveness** | **Display** | **HideStarter** | **HideDocu** |
|  |  |  |  | True | False | False |
| p0502: Technological application |  |  |  |  |  |  |

**Expert**

The selection of the control mode is retained with the "Extended wizard" selection. The selection for the motor data identification (p1900) is taken over by the Dynamic Drive Control. The selection of the complete calculation (p0340) is retained.

### Options for cabinet unts

#### Requirement

This mask is only visible for converter cabinet units with a PM330 or PM330L as power unit.

#### Options for the PM330/PM330L power modules

The following options are available after selecting a PM330/PM330L. Select the options that your drive / power module has:

| Option | Description |
| --- | --- |
| L00 | Line filter; the converters / power modules are equipped by default with a radio interference filter for limiting emitted interference as per the limit values defined in Category C3. Optional filters are available for use in the first environment (Category C2). |
| L01 | Line harmonic filter for reducing line harmonic distortions. The harmonics generated by the converter are filtered out by a low-pass filter between the converter and the line |
| L07 | dv/dt filter compact voltage peak limiters; limit the voltage peaks at the output of frequency converters as well as the rate of voltage rise. |
| L08 | Motor reactor; motor reactors reduce the voltage load of the motor windings by reducing the voltage rise rates at the motor terminals caused by operating the converter. |
| L10 | dv/dt filter plus voltage peak limiter; if you select this option, the parameter p0230 (dv/dt filter) is automatically set to 2 (p0230=2). |
| L22 | Without line reactor; if the converter is supplied via a separate transformer or if the ratio of the line short-circuit output at the connection point to the converter's rated output is low, then the standard line reactors can be omitted for converters < 500 kW (see configuration information). If a line filter (option L00) is used, however, this line reactor is required. |
| L45 | Emergency off pushbutton |
| L57 | Emergency stop category 0; EMERGENCY OFF category 0 for uncontrolled shutdown according to EN 60 204. |
| L59 | Emergency stop category 1; EMERGENCY OFF category 1 for controlled shutdown according to EN 60 204. |
| L60 | Emergency stop category 1 24V; EMERGENCY OFF category 1 for controlled shutdown according to EN 60 204. |
| L61 | Braking module (25 kW); for drives which allow generator modes, the use of braking choppers may be required. |
| L62 | Braking module (50 kW) |

### Setpoint specification

#### Description

Here you can specify whether the drive is connected to a PLC and whether the ramp-function generator setpoint specification is performed in the PLC or in the drive.

#### Selecting the setpoint specification

Depending on the configured drive, up to three selectable options are displayed.

Activate one of the following options:

- Drive is connected to a PLC. Ramp-function generator is in the PLC.

  With this option, the drive is connected via PROFIBUS or PROFINET to a PLC which specifies the ramp-function generator setpoint.  
  The drive follows the speed setpoint of the PLC.
- Drive is connected to a PLC. Ramp-function generator is in the drive.

  With this option, the drive is connected via PROFIBUS or PROFINET to a PLC.   
  The ramp-function generator is in the drive.
- Drive is not connected to any PLC. Ramp-function generator is in the drive.

  With this option, a PLC is not available.

  The ramp-function generator is in the drive.

> **Note**
>
> For G115D PN, the setpoint specification page is not available and the selection by default is "Drive is connected to a PLC".

Depending on which option you select, you must make different settings for the ramp-function generator in the "Important parameters" mask shown later in the commissioning wizard.

Further settings for the ramp-function generator setpoint specification can be made after completing the commissioning wizard in the "Ramp-function generator" mask. Further information on the "Ramp-function generator" mask can be found via the 'See also' links to the appropriate drive units at the end of this Help page.

---

**See also**

[G110M ramp-function generator](G110M.md#g110m-ramp-function-generator)
  
[G120C ramp-function generator](G120C.md#g120c-ramp-function-generator)
  
[G120D-2 ramp-function generator](G120D-2.md#g120d-2-ramp-function-generator)
  
[G120P ramp-function generator](G120P.md#g120p-ramp-function-generator)
  
[G120 CU240-2 ramp-function generator](G120%20CU240-2.md#g120-cu240-2-ramp-function-generator)
  
[G120 CU250S-2 V ramp-function generator](G120%20CU250S-2%20vector.md#g120-cu250s-2-v-ramp-function-generator)

### Open-loop/closed-loop control type

#### Description

The closed-loop control structure is used to specify the control type and the control. At "Control", you can specify the control depending on the control type for your drive device.

#### Activating function modules

Various drives, such as the G120 CU250S-2, provide additional functions via function modules. Activate the required function modules:

- [PID Technology controller](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#pid-technology-controller)
- [Basic positioner](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#basic-positioner-and-position-control)
- [Extended messages/monitors](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#protective-functions)
- [Free function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#free-function-blocks)

The same functionality exists in various drives as a standard feature and does not have to be individually activated.

#### Selecting the control type

- Select the control type ([p1300](SINAMICS%20Parameter%20G120.md#p13000n-open-loopclosed-loop-control-operating-mode-13)) you wish to use.

You can select the following control types:

- "V/f control with linear characteristic"

  Standard characteristic curve (voltage or frequency control) for simple constant torque single or multi-motor drives without high demands on the dynamic response.
- "V/f control with linear characteristic and FCC (flux current control)"

  Characteristic that compensates for voltage losses in the stator resistance for static/dynamic loads (flux current control FCC).
- "V/f control with parabolic characteristic"

  Characteristic curve for variable torque loads such as fans and pumps.

  Significant energy savings can be made by using this characteristic curve in the fans and pumps application.
- "V/f control with parameterizable characteristic"

  This control type permits the parameterization of an individually adjusted characteristic curve. Three additional frequency and three additional voltage coordinates are provided for this.
- "V/f control with linear characteristic and ECO"
- "V/f control for parabolic characteristic and ECO"

  The ECO mode is suitable for applications with a low dynamic response and allows energy savings of up to 40%.

  > **Note**
  >
  > Sudden load variations can cause the motor to stall.
- "V/f control for drives requiring a precise frequency (textile sector)"

  The V/f characteristic curve for textile applications:

  - Is suitable for single and group drives with SIEMOSYN and reluctance motors with high speed accuracy, e.g. in the textiles industry.
  - Is the same as the linear V/f characteristic curve, however without the control influencing the frequency. This means the Imax controller refers to the converter output voltage instead of the converter output frequency.
- "V/f control for drives requiring a precise frequency and FCC"
- "V/f control with independent voltage setpoint"

  The voltage setpoint can be specified using [p1330](SINAMICS%20Parameter%20G120.md#p13300n-ci-uf-control-independent-voltage-setpoint) independently of the output frequency of the ramp-function generator (RFG). This means, based on the V/f characteristic curve, it is possible to specify a voltage independently of the frequency. The control of an electromagnet is an application example.
- "Speed control (encoderless)"

  SLVC (Sensorless Vector Control) is the control type for applications with high dynamic response demands without feedback and torque limits such as compressors, punching presses, simple lifting gear, etc.

  > **Note**
  >
  > Switchover from vector control to torque control ([p1501](SINAMICS%20Parameter%20G120.md#p15010n-bi-change-over-between-closed-loop-speedtorque-control)) is possible.
  >
  > For a proper functioning of the SLVC, it is essential to introduce the correct motor data ([p0300](SINAMICS%20Parameter%20G120.md#p03000n-motor-type-selection-19) through [p0320](SINAMICS%20Parameter%20G120.md#p03200n-motor-rated-magnetizing-currentshort-circuit-current)) and to perform a motor identification ([p1900](SINAMICS%20Parameter%20G120.md#p1900-motor-data-identification-and-rotating-measurement-9)) and a controller optimization ([p1960](SINAMICS%20Parameter%20G120.md#p1960-rotating-measurement-selection-3)).
- "Speed control with encoder" (only for drives with encoder)

  The only difference between vector control with encoder and encoderless vector control, is that the converter measures the speed, instead of calculating it.
- "Torque control (encoderless)"

  This control type allows the converter to control or limit the torque of a motor. This means the converters can be used in applications which require a constant torque or a torque limitation (e.g. simple tension control).

  The output current (and therefore the required torque) of the converter (motor) can be varied (specified) by specifying a torque setpoint.

  > **Note**
  >
  > For an optimum quality of the open-loop or closed-loop control, it is always necessary to carry out a commissioning with motor identification and controller optimization.

#### Additional parameters

---

### Default settings of the setpoints / command sources

This section contains information on the following topics:

- [Telegram overview for G120/G115D/G110M drives](#telegram-overview-for-g120g115dg110m-drives)
- [Default settings of the setpoints / command sources](#default-settings-of-the-setpoints-command-sources-1)
- [Default settings for G120P](#default-settings-for-g120p)
- [Default settings for G120 CU240-2](#default-settings-for-g120-cu240-2)
- [Default settings for G120C](#default-settings-for-g120c)
- [Default settings for G120 CU240D-2/CU250D-2](#default-settings-for-g120-cu240d-2cu250d-2)
- [G120 CU250S-2 vector default settings](#g120-cu250s-2-vector-default-settings)
- [G110M default settings](#g110m-default-settings)
- [G115D default settings](#g115d-default-settings)

#### Telegram overview for G120/G115D/G110M drives

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

G120, G115D and G110M telegrams

| Symbol | Meaning |
| --- | --- |
| **Telegram** | **Description** |
| 1 | Speed setpoint, 16-bit |
| 2 | Speed setpoint, 32-bit |
| 3 | Speed setpoint, 32-bit with 1 position encoder |
| 4 | Speed setpoint, 32-bit with 2 position encoders |
| 7 | Basic positioner with selection of the traversing block |
| 9 | Basic positioner with direct setpoint specification (MDI) |
| 20 | 16-bit speed setpoint for VIK-NAMUR |
| 110 | Basic positioner with direct setpoint specification (MDI), override, and actual position value |
| 111 | Basic positioner with direct setpoint specification (MDI), override, actual position value, and actual speed value |
| 350 | Speed setpoint, 16-bit with torque limitation |
| 352 | 16-bit speed setpoint for PCS7 |
| 353 | 16-bit speed setpoint to read and write parameters |
| 354 | 16-bit speed setpoint for PCS7 to read and write parameters |
| 999 | Unassigned interconnection and length |

#### Default settings of the setpoints / command sources

##### Description

The command source is the interface via which the converter receives its control commands. The setpoint source is the interface via which the converter receives its setpoint. See [SINAMICS G120 interface assignments - CU240B-2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#sinamics-g120-interface-assignments---cu240b-2) for a description of the interface assignment.

In order to avoid a time-consuming configuration of the interfaces, predefined I/O configurations are provided for a large number of tasks. You can define the I/O configuration either here or set it via [p0015](SINAMICS%20Parameter%20G120.md#p0015-macro-drive-unit-10) in the parameter list. This is only possible when there is an online connection to the drive. The settings required for this I/O configuration are preassigned via macros so that no further settings have to be made. Safety functions are the exception, they still have to be parameterized manually.

The available default settings depend on the drive that is used.

- [Default settings for G120P](#default-settings-for-g120p)
- [Default settings for G120 CU240-2](#default-settings-for-g120-cu240-2)
- [Default settings for G120C](#default-settings-for-g120c)
- [Default settings for G120 CU240D-2/CU250D-2](#default-settings-for-g120-cu240d-2cu250d-2)
- [G120 CU250S-2 vector default settings](#g120-cu250s-2-vector-default-settings)
- [G110M default settings](#g110m-default-settings)

##### Current I/O configuration

This field displays the currently selected I/O configuration.

##### Default setting of the I/O configuration

The following settings can be made for the various drives:

- 1.) Conveyor technology with two fixed frequencies
- 2.) Conveyor technology with the Basic Safety (safety functions)
- 3.) Conveyor technology with four fixed frequencies
- 4.) Conveyor technology with fieldbus
- 5.) Conveyor technology with fieldbus and Basic Safety (safety functions)
- 6.) Fieldbus with Extended Safety
- 7.) Fieldbus with data set switchover
- 8.) MOP with Basic Safety
- 9.) Standard I/O with MOP
- 12.) Standard I/O with analog setpoint
- 13.) Standard I/O with analog setpoint and Safety
- 14.) Process industry with fieldbus
- 15.) Process industry
- 17.) 2-wire (forward/backward 1)
- 18.) 2-wire (forward/backward 2)
- 19.) 2-wire (enable/forward/backward)
- 20.) 3-wire (enable/forward/backward)
- 24.) Distributed conveyor technology with PROFIBUS or PROFINET fieldbus
- 25.) Distributed conveyor technology with PROFIBUS or PROFINET fieldbus and safety functions
- 26.) Basic positioner without fieldbus
- 27.) Basic positioner with fieldbus
- 28.) Conveyor technology with two fixed speeds
- 29.) Conveyor technology with two fixed velocities
- 30.) ASi single device with fixed setpoints
- 31.) ASi dual device with fixed setpoints
- 32.) ASi single device with analog setpoint
- 34.) ASi dual device with speed setpoint

Detailed information about the default settings is contained in the operating instructions of the relevant converter.

##### Accept settings

- Click "Accept" to accept the default setting of the I/O configuration. It is then displayed in the "Current I/O configuration" field.

##### Current interconnections of the I/O terminals

This field displays the current interconnections of the inputs/outputs corresponding to the selected I/O configuration.

##### Current telegram configuration

This field displays the current telegram configuration.

##### Additional parameters

---

#### Default settings for G120P

##### Possible settings for G120P

The following table shows the setting options for the G120P

| Macro | Designation | CU230P HVAC | CU230P DP/PN | CU230P CAN |
| --- | --- | --- | --- | --- |
| 1 | Conveyor systems with two fixed frequencies | - | - | - |
| 2 | Conveyor systems with the Basic Safety | - | - | - |
| 3 | Conveyor systems with four fixed frequencies | - | - | - |
| 4 | Conveyor systems with fieldbus | - | - | - |
| 5 | Conveyor systems with fieldbus and Basic Safety | - | - | - |
| 6 | Fieldbus with Extended Safety | - | - | - |
| 7 | Fieldbus with data set switchover | - | D | - |
| 8 | MOP with Basic Safety | - | - | - |
| 9 | Standard I/O with MOP | X | X | X |
| 10 | Currently with no function | - | - | - |
| 11 | Currently with no function | - | - | - |
| 12 | Standard I/O with analog setpoint | D | X | D |
| 13 | Standard I/O with analog setpoint and safety | - | - | - |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | - | X | - |
| 15 | Process industry | X | X | X |
| 16 | Currently with no function | - | - | - |
| 17 | 2-wire (forward/backward 1) | X | X | X |
| 18 | 2-wire (forward/backward 2) | X | X | X |
| 19 | 3-wire (enable/forward/backward) | X | X | X |
| 20 | 3-wire (enable/on/reverse) | X | X | X |
| 21 | USS fieldbus | X | - | - |
| 22 | CAN fieldbus | - | - | X |
| 23 | Fieldbus with data set switchover | - | - | - |
| 24 | Distributed conveyor systems with fieldbus | - | - | - |
| 25 | Distributed conveyor systems with fieldbus, safety | - | - | - |
| 26 | EPOS without fieldbus | - | - | - |
| 27 | EPOS with fieldbus | - | - | - |
| X = is supported |  |  |  |  |
| D = default setting |  |  |  |  |

---

**See also**

[Default settings of the setpoints / command sources](#default-settings-of-the-setpoints-command-sources-1)

#### Default settings for G120 CU240-2

##### Possible settings for G120 CU240-2

The following table shows the setting options for the G120 CU240-2

| Macro | Designation | CU240B-2 | CU240B-2 DP/PN | CU240E-2 | CU240E DP/PN | CU240E F | CU240E DP/PN F |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Conveyor systems with two fixed frequencies | - | - | - | X | X | X |
| 2 | Conveyor systems with the Basic Safety | - | - | - | X | X | X |
| 3 | Conveyor systems with four fixed frequencies | - | - | - | X | X | X |
| 4 | Conveyor systems with fieldbus | - | - | - | X | - | X |
| 5 | Conveyor systems with fieldbus and Basic Safety | - | - | - | X | - | X |
| 6 | Fieldbus with Extended Safety | - | - | - | - | - | X |
| 7 | Fieldbus with data set switchover | - | D | - | D | - | D |
| 8 | MOP with Basic Safety | - | - | X | X | X | X |
| 9 | Standard I/O with MOP | X | X | X | X | X | X |
| 10 | Currently with no function | - | - | - | - | - | - |
| 11 | Currently with no function | - | - | - | - | - | - |
| 12 | Standard I/O with analog setpoint | D | X | D | X | D | X |
| 13 | Standard I/O with analog setpoint and safety | - | - | X | X | X | X |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | - | - | - | X | - | - |
| 15 | Process industry | - | - | X | X | X | X |
| 16 | Currently with no function | - | - | - | - | - | - |
| 17 | 2-wire (forward/backward 1) | X | X | X | X | X | X |
| 18 | 2-wire (forward/backward 2) | X | X | X | X | X | X |
| 19 | 3-wire (enable/forward/backward) | X | X | X | X | X | X |
| 20 | 3-wire (enable/on/reverse) | X | X | X | X | X | X |
| 21 | USS fieldbus | X | - | X | - | X | X |
| 22 | CAN fieldbus | - | - | - | - | - | - |
| 23 | Fieldbus with data set switchover | - | - | - | - | - | - |
| 24 | Distributed conveyor systems with fieldbus | - | - | - | - | - | - |
| 25 | Distributed conveyor systems with fieldbus, safety | - | - | - | - | - | - |
| 26 | EPOS without fieldbus | - | - | - | - | - | - |
| 27 | EPOS with fieldbus | - | - | - | - | - | - |
| X = is supported |  |  |  |  |  |  |  |
| D = default setting |  |  |  |  |  |  |  |

---

**See also**

[Default settings of the setpoints / command sources](#default-settings-of-the-setpoints-command-sources-1)

#### Default settings for G120C

##### Possible settings for G120C

The following table shows the setting options for the G120C

| Macro | Designation | G120C | G120C DP/PN | G120C CAN |
| --- | --- | --- | --- | --- |
| 1 | Conveyor systems with two fixed frequencies | X | X | X |
| 2 | Conveyor systems with the Basic Safety | X | X | X |
| 3 | Conveyor systems with four fixed frequencies | X | X | X |
| 4 | Conveyor systems with fieldbus | - | X | - |
| 5 | Conveyor systems with fieldbus and Basic Safety | - | X | - |
| 6 | Fieldbus with Extended Safety | - | - | - |
| 7 | Fieldbus with data set switchover | - | D | - |
| 8 | MOP with Basic Safety | X | X | X |
| 9 | Standard I/O with MOP | X | X | X |
| 10 | Currently with no function | - | - | - |
| 11 | Currently with no function | - | - | - |
| 12 | Standard I/O with analog setpoint | D | X | D |
| 13 | Standard I/O with analog setpoint and safety | - | X | - |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | - | X | - |
| 15 | Process industry | X | X | X |
| 16 | Currently with no function | - | - | - |
| 17 | 2-wire (forward/backward 1) | X | X | X |
| 18 | 2-wire (forward/backward 2) | X | X | X |
| 19 | 3-wire (enable/forward/backward) | X | X | X |
| 20 | 3-wire (enable/on/reverse) | X | X | X |
| 21 | USS fieldbus | X | - | - |
| 22 | CAN fieldbus | - | - | X |
| 23 | Fieldbus with data set switchover | - | - | - |
| 24 | Distributed conveyor systems with fieldbus | - | - | - |
| 25 | Distributed conveyor systems with fieldbus, safety | - | - | - |
| 26 | EPOS without fieldbus | - | - | - |
| 27 | EPOS with fieldbus | - | - | - |
| X = is supported |  |  |  |  |
| D = default setting |  |  |  |  |

---

**See also**

[Default settings of the setpoints / command sources](#default-settings-of-the-setpoints-command-sources-1)

#### Default settings for G120 CU240D-2/CU250D-2

##### Possible settings for G120 CU240D-2/CU250D-2

The following table shows the setting options for the G120 CU240D-2/CU250D-2

| Macro | Designation | CU240D-2  DP/PN | CU240D-2 DP/PN F | CU250D-2  DP/PN F |
| --- | --- | --- | --- | --- |
| 1 | Conveyor systems with two fixed frequencies | X | X | - |
| 2 | Conveyor systems with the Basic Safety | X | X | - |
| 3 | Conveyor systems with four fixed frequencies | X | X | - |
| 4 | Conveyor systems with fieldbus | X | X | - |
| 5 | Conveyor systems with fieldbus and Basic Safety | X | X | - |
| 6 | Fieldbus with Extended Safety | - | X | - |
| 7 | Fieldbus with data set switchover | D | D | - |
| 8 | MOP with Basic Safety | X | X | - |
| 9 | Standard I/O with MOP | X | X | - |
| 10 | Currently with no function | - | - | - |
| 11 | Currently with no function | - | - | - |
| 12 | Standard I/O with analog setpoint | X | X | - |
| 13 | Standard I/O with analog setpoint and safety | X | X | - |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | X | X | - |
| 15 | Process industry | - | - | - |
| 16 | Currently with no function | - | - | - |
| 17 | 2-wire (forward/backward 1) | - | - | - |
| 18 | 2-wire (forward/backward 2) | - | - | - |
| 19 | 3-wire (enable/forward/backward) | - | - | - |
| 20 | 3-wire (enable/on/reverse) | - | - | - |
| 21 | USS fieldbus | - | - | - |
| 22 | CAN fieldbus | - | - | - |
| 23 | Fieldbus with data set switchover | - | - | - |
| 24 | Distributed conveyor systems with fieldbus | X | X | - |
| 25 | Distributed conveyor systems with fieldbus, safety | X | X | - |
| 26 | EPOS without fieldbus | - | - | D |
| 27 | EPOS with fieldbus | - | - | X |
| X = is supported |  |  |  |  |
| D = default setting |  |  |  |  |

---

**See also**

[Default settings of the setpoints / command sources](#default-settings-of-the-setpoints-command-sources-1)

#### G120 CU250S-2 vector default settings

##### Possible settings for the G120 CU250S-2

The following table shows the setting options for the G120 CU250S-2.

| Macro | Designation | CU250S-2 | CU250S-2 CAN | CU250S-2 DP | CU250S-2 PN |
| --- | --- | --- | --- | --- | --- |
| 1 | Conveyor technology with two fixed frequencies | X | X | X | X |
| 2 | Conveyor technology with the Basic Safety | X | X | X | X |
| 3 | Conveyor technology with four fixed frequencies | X | X | X | X |
| 4 | Conveyor technology with fieldbus | X | X | X | X |
| 5 | Conveyor technology with fieldbus and Basic Safety | X | X | X | X |
| 6 | Fieldbus with Extended Safety | - | - | - | - |
| 7 | Fieldbus with data set switchover | X | X | D | D |
| 8 | MOP with Basic Safety | X | X | X | X |
| 9 | Standard I/O with MOP | X | X | X | X |
| 10 | Currently with no function | - | - | - | - |
| 11 | Currently with no function | - | - | - | - |
| 12 | Standard I/O with analog setpoint | D | D | X | X |
| 13 | Standard I/O with analog setpoint and safety | X | X | X | X |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | X | X | X | X |
| 15 | Process industry | X | X | X | X |
| 16 | Currently with no function | - | - | - | - |
| 17 | 2-wire (forward/backward 1) | X | X | X | X |
| 18 | 2-wire (forward/backward 2) | X | X | X | X |
| 19 | 3-wire (enable/forward/backward) | X | X | X | X |
| 20 | 3-wire (enable/on/reverse) | X | X | X | X |
| 21 | USS fieldbus | X | X | X | X |
| 22 | CAN fieldbus | - | X | - | - |
| 23 | Fieldbus with data set switchover | - | - | - | - |
| 24 | Distributed conveyor technology with fieldbus | - | - | - | - |
| 25 | Distributed conveyor technology with fieldbus, safety | - | - | - | - |
| 26 | EPOS without fieldbus | - | - | - | - |
| 27 | EPOS with fieldbus | - | - | - | - |
| X = is supported |  |  |  |  |  |
| D = default setting |  |  |  |  |  |

#### G110M default settings

##### Possible settings for the G110M

The following table shows the setting options for the G110M

| Macro | Designation | CU240M USS | CU240M DP | CU240M PN | CU240M AS-i |
| --- | --- | --- | --- | --- | --- |
| 1 | Conveyor technology with two fixed speeds | - | - | - | - |
| 2 | Conveyor technology with the Basic Safety | - | - | - | - |
| 3 | Conveyor technology with four fixed speeds | - | - | - | - |
| 4 | Conveyor technology with fieldbus | - | - | - | - |
| 5 | Conveyor technology with fieldbus and Basic Safety | - | - | - | - |
| 6 | Fieldbus with Extended Safety | - | - | - | - |
| 7 | Fieldbus with data set switchover | X | X | X | - |
| 8 | MOP with Basic Safety | - | - | - | - |
| 9 | Standard I/O with MOP | X | X | X | - |
| 10 | Currently with no function | - | - | - | - |
| 11 | Currently with no function | - | - | - | - |
| 12 | Standard I/O with analog setpoint | X | X | X | - |
| 13 | Standard I/O with analog setpoint and safety | - | - | - | - |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | - | - | - | - |
| 15 | Process industry | - | - | - | - |
| 16 | Currently with no function | - | - | - | - |
| 17 | 2-wire (forward/backward 1) | X | X | X | - |
| 18 | 2-wire (forward/backward 2) | X | X | X | - |
| 19 | 3-wire (enable/forward/backward) | X | X | X | - |
| 20 | 3-wire (enable/on/reverse) | X | X | X | - |
| 21 | USS fieldbus | X | X | X | - |
| 22 | CAN fieldbus | - | - | - | - |
| 23 | Fieldbus with data set switchover | - | - | - | - |
| 24 | Distributed conveyor technology with fieldbus | - | - | - | - |
| 25 | Distributed conveyor technology with fieldbus, safety | - | - | - | - |
| 26 | EPOS without fieldbus | - | - | - | - |
| 27 | EPOS with fieldbus | - | - | - | - |
| 28 | Conveyor technology with fixed speed | X | X | X | - |
| 29 | Conveyor technology poti/fixed setpoint | X | X | X | - |
| 30 | ASi single device with fixed setpoints | - | - | - | D |
| 31 | ASi dual device with fixed setpoints | - | - | - | D |
| 32 | ASi single device with analog setpoint | - | - | - | X |
| 34 | ASi dual device with speed setpoint | - | - | - | X |
| X = is supported  D = default setting  - = not supported |  |  |  |  |  |

> **Note**
>
> For more information on default settings refer "[Interface assignments - G110M](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#interface-assignments---g110m)".

#### G115D default settings

##### Possible settings for the G115D

.

The following table shows the setting options for the G115D

| Macro | Designation | G115D I/O | G115D PN | G115D AS-i |
| --- | --- | --- | --- | --- |
| 1 | Conveyor technology with two fixed speeds | - | - | - |
| 2 | Conveyor technology with the Basic Safety | - | - | - |
| 3 | Conveyor technology with four fixed speeds | - | - | - |
| 4 | Conveyor technology with fieldbus | - | - | - |
| 5 | Conveyor technology with fieldbus and Basic Safety | - | - | - |
| 6 | Fieldbus with Extended Safety | - | - | - |
| 7 | Fieldbus with data set switchover | - | - | - |
| 8 | MOP with Basic Safety | - | - | - |
| 9 | Standard I/O with MOP | X | - | - |
| 10 | Currently with no function | - | - | - |
| 11 | Currently with no function | - | - | - |
| 12 | Standard I/O with analog setpoint | - | - | - |
| 13 | Standard I/O with analog setpoint and safety | - | - | - |
| 14 | Standard I/O assignments 14.) Process industry, with fieldbus | - | - | - |
| 15 | Process industry | - | - | - |
| 16 | Currently with no function | - | - | - |
| 17 | 2-wire (forward/backward 1) | - | - | - |
| 18 | 2-wire (forward/backward 2) | - | - | - |
| 19 | 3-wire (enable/forward/backward) | - | - | - |
| 20 | 3-wire (enable/on/reverse) | - | - | - |
| 21 | USS fieldbus | - | - | - |
| 22 | CAN fieldbus | - | - | - |
| 23 | Fieldbus with data set switchover | - | - | - |
| 24 | Distributed conveyor technology with fieldbus | - | - | - |
| 25 | Distributed conveyor technology with fieldbus, safety | - | - | - |
| 26 | EPOS without fieldbus | - | - | - |
| 27 | EPOS with fieldbus | - | - | - |
| 28 | Conveyor technology with 2 fixed speed | X | - | - |
| 29 | Conveyor technology with MOP and fixed speed | - | - | - |
| 30 | AS-i single device with fixed setpoints | - | - | D |
| 31 | AS-i dual device with fixed setpoints | - | - | X |
| 32 | AS-i single device with analog setpoint | - | - | X |
| 60 | Standard I/O with port 1 setpoint | X | - | - |
| 61 | 2-wire (for/rev 1) with port 1 setpoint | X | - | - |
| 62 | 2-wire (for/rev 2) with port 1 or port 2 setpoint | X | - | - |
| 63 | 3-wire (enable/for/rev) with port 1 setpoint | X | - | - |
| 64 | 3-wire (enable/start/dir) with port 1 setpoint | X | - | - |
| 65 | Conveyor technology with port 1 or port 2 setpoint | D | - | - |
| 66 | AS-i dual device with port 1 or port 2 setpoint | - | - | X |
| 67 | 4DI distributed conveyor technology with fieldbus. | - | D | - |
| X = is supported  D = default setting  - = not supported |  |  |  |  |

> **Note**
>
> When the DIP switch is activated, the selection of macro is disabled in the commissioning wizard, as shown in the below image.

![Possible settings for the G115D](images/134767862283_DV_resource.Stream@PNG-en-US.png)

### Profile setting of AS-i device (G110M and G115D)

#### Description

In this mask you can configure AS-i address and profile ID for AS-i device.

The AS-i interface related parameters, p2012 and p2014 are not part of download. Hence, commission them online with the drive.

#### AS-i profile

The "AS-i Profile" (p2013) is read-only. It reflects the information from p15.

#### AS-i address

You can select the device "AS-i address" (p2012) from the drop-down list in online mode. In offline mode this field is read-only. The address range for different AS-i mode is as indicated in the following table.

| AS-i mode | AS-i address range |
| --- | --- |
| Single device | 0 to 31 |
| Dual device | 33 to 63 |

#### Profile ID1

You can select the device "Profile ID1" (p2014) from the drop-down list in online mode. This value ranges from 0 to F.

![Profile setting of single device.](images/137829843979_DV_resource.Stream@PNG-en-US.png)

Profile setting of single device.

![Profile setting of dual device.](images/137829852555_DV_resource.Stream@PNG-en-US.png)

Profile setting of dual device.

### Drive setting

#### Selection of motor standard and load cycle

The motor standard appears on the rating plate of the motor.

#### Motor standard

- In the "Standard" drop-down list ([p0100](SINAMICS%20Parameter%20G120.md#p0100-iecnema-standards)), select the standard for your motor:

  - IEC motor 50 Hz, SI units
  - NEMA motor 60 Hz, SI units
- Enter a value for the device supply voltage at "Device supply voltage" ([p0210](SINAMICS%20Parameter%20G120.md#p0210-drive-unit-line-supply-voltage-1)) or check the entered value.

#### Power unit application

- To set the "Power unit application" ([p0205](SINAMICS%20Parameter%20G120.md#p0205-power-unit-application)), select one of the following options:

  - Load cycle with high overload for vector drives.  
    Select high overload for dynamic applications, such as conveyor systems.
  - Load cycle with low overload for vector drives.  
    Select low overload for less dynamic applications, such as pumps.

  The parameter value is not reset with "Restore factory setting".

  If the parameter is changed, all motor parameters, the technological application and the control type are preset in accordance with the selected application.

#### Pulse frequency (only for G115D)

Enter a value for the pulse frequency at "Pulse frequency" ([p1800](SINAMICS%20Parameter%20G120.md#p18000n-pulse-frequency-setpoint-2)) or select from the list of values (4, 6, 8, 10, 12, 14, or 16).

The default value is 4 kHz.

> **Note**
>
> - Increase of pulse frequency above default (4 kHz) will result in current / power derating of the converter.
> - When the pulse frequency is activated via DIP switch, the "Pulse Frequency" field is disabled in the commissioning wizard.

#### Additional parameters

---

### Drive options

#### Description

Configure an optional brake resistor or a filter at the motor end of your drive.

#### Brake resistance

Depending on the configured drive, the option "Brake resistance" appears so that you can add a brake resistor to your drive.

If you activate the "Brake resistor" button, the "Maximum braking power" (p219) input field is displayed.

Enter a value for the maximum braking power in the "Maximum brake power" field.

#### Filter type

In the "Drive filter type motor end" drop-down list, select the filter type (p230).

The following options are available:

- [0] No filter
- [1] Motor reactor
- [2] dv/dt filter
- [3] Siemens sine filter
- [4] Third-party sine-wave filter

**Sine-wave filter**

Depending on the selected filter type, the input fields "Sine filter inductivity" (p233) and "Sine filter capacitance" (p234) are displayed.

For the filter types [1] and [3], the values for the Sine-wave filter inductivity and the Sine-wave filter capacity are default values and inputs are disabled.

Enter a value for the Sine-wave filter inductivity and the Sine-wave filter capacity if you have selected filter type [4].

### Motor

#### Description

Parameterize the motor type and whether you want to retain the motor data or enter the motor data:

- In the "Select motor type" drop-down list ([p0300](SINAMICS%20Parameter%20G120.md#p03000n-motor-type-selection-19)), select the motor type that you are using:

  - Induction motor (rotary)
  - Synchronous motor (rotary, permanently excited)
  - 1LE1 induction motor
  - 1LG6 induction motor
  - 1LA7 induction motor
  - 1LA9 synchronous motor

#### Motor data

1. Select "Enter motor data" if you want to enter the data of the motor yourself.
2. Select "Enter from Order no. list" to display a motor list. You can select the motor there using the MLFB. The values of the selected motor are then taken as default motor data.

#### Connection type (p133[0])

Depending on your application, you must operate the motor in a star or delta connection.

Examples for operating the converter and motor on a 400 V line

Assumption: The rating plate of the motor specifies 230/400 V Δ/Y.

- Case 1: Normally, a motor is operated in the range from standstill to its rated speed (i.e. the speed that corresponds to the line frequency). If this is the case, you must connect the motor in Y. Operating the motor above its rated speed is only possible in this case with field weakening, i.e. the available torque of the motor is reduced above the rated speed.
- Case 2: If you want to operate the motor with the "87 Hz characteristic", you must connect  
  the motor in Δ.  
  With the 87 Hz characteristic, the power output of the motor increases. The 87 Hz  
  characteristic is primarily used for geared motors.

Before you connect the motor, check to see whether the motor is connected according to your application.

#### Parallel motor connection (only induction motors)

1. To use several induction motors in parallel, activate the "Parallel motor connection" option.
2. Enter the number of motors.

   If you subsequently select a synchronous motor, the option is reset to 1.

#### Temperature sensor

Select the temperature sensor you want to use in the "Temperature sensor" drop-down list.

#### 87 Hz calculation ([p0133](SINAMICS%20Parameter%20G120.md#p01330n-motor-configuration)[1])

The 87 Hz characteristic is used in gearbox construction so that the motor has the root 3 higher power and the torque is fully available over a larger range. A 230/400 V motor is switched to the delta connection at this operating point and then operated with 400 V, 87 Hz. Only then does the motor go into the field weakening.

> **Note**
>
> The 87 Hz calculation can be selected only when a rated frequency of 50 Hz is set.

#### **Motor selection for G115D**

- **Wall Mount**

  The SIMOGEAR order number can be selected using the combo boxes, and after clicking on the accept button, the motor and gear information is displayed.

  ![Motor selection for G115D](images/135194152203_DV_resource.Stream@PNG-en-US.png)
- **Motor mount**

  The already configured SIMOGEAR motor and gear information is displayed as read-only.

  - **Reverse the output phase sequence**

    The "Reverse the output phase sequence" option can be enabled from commissioning wizard in case of G115D.

    ![Motor selection for G115D](images/135197506571_DV_resource.Stream@PNG-en-US.png)
  > **Note**
  >
  > When the DIP switch is activated, the "Motor type", "Motor connection type", "Temperature sensor", and the "Reverse the output phase sequence" fields are disabled in the commissioning wizard.

Temperature sensor is defined from the selected SIMOGEAR order number.

#### Additional parameters

---

### Motor holding brake

#### Selection of the motor holding brake

Select one of the following options (p1215) from the drop-down list:

- No motor holding brake available
- Motor holding brake like sequential control system
- Motor holding brake always open
- Motor holding brake like sequential control system, connection via BICO

#### Brake closing time

Enter the application time of the holding brake at "Motor holding brake closing time" (p1217). Along with the speed threshold it is a criterion for closing the holding brake. If the closing time has elapsed after removing the controller enable, the "Open holding brake" signal is removed. Alternatively, the brake can already be closed having reached the speed threshold. After the closing delay time has elapsed, the pulse enable will be blocked.

#### Brake opening time

Enter the opening time of the holding brake at "Motor holding brake opening time" (p1216). The setpoint acceptance after the controller enable is delayed by this time. With n set = 0 rpm, the speed control has already been activated with the controller enable in order to prevent a sagging of the axis.

#### **Motor holding brake for G115D with Simogear**

The brake configuration is pre-selected for the SIMOGAER motor according to the brake option ordered with it.

> **Note**
>
> When the motor holding brake configuration is activated via DIP switch, the user cannot change the configuration in the commissioning wizard.

### Drive functions

#### Description

A motor identification is recommended for the first commissioning. The drive uses the preselected type of motor identification to perform this when it is connected for the first time.

#### Technological application

Based on the preselected technological application, the motoring and generating torque and power limits are calculated in the drive after the download to the target device.

From the "Technological application" ([p0500](SINAMICS%20Parameter%20G120.md#p0500-technology-application-16)) drop-down list, select one of the following options:

- Standard drive (e.g. pumps and fans)
- Dynamic starting or reversing
- Pumps and fans
- Sensorless control up to f = 0 (passive loads)
- Pumps and fans, efficiency optimization
- Constant load (linear characteristic)
- Speed-dependent load (parabolic characteristic)
- Heavy starting (e.g. extruders, compressors)

#### Motor identification

- From the "Motor identification" drop-down list ([p1900](SINAMICS%20Parameter%20G120.md#p1900-motor-data-identification-and-rotating-measurement-9)), select one of the following options:

  - Disabled  
    No motor data identification
  - Identify motor data and optimize speed controller  
    Motor data identification at standstill and for rotating motor  
    Recommended if you have set "Speed control" as the control type. The converter then optimizes the speed controller.
  - Identify motor data (at standstill)  
    Motor data identification at standstill  
    Recommended if you have set "Speed control" as the control type, but the motor cannot rotate freely, e.g. with mechanically restricted traversing paths.  
    Also recommended if you have set "V/f control" as the control type.
  - Optimize speed controller  
    Motor data identification for rotating motor

#### Calculation of the motor data in online mode

Select how the motor data for the commissioning in online mode is to be calculated:

- "Restore factory setting and calculate motor data"; only those parameter settings changed via "online commissioning" are retained here. All other parameters, including the I/O settings, will be reset to the factory setting.

  The motor data will be calculated after the factory setting has been completed.
- "Calculate motor data only"; only the motor and controller calculations are performed here.

  Time can be saved if the online commissioning is completed with this setting (for example, when only the motor rating plate data has been changed).

#### Calculation of the motor data in offline mode

Select how the motor data for commissioning is to be calculated or not in offline mode.

- "No calculation"; the motor data will not be calculated. The motor data does not have to be calculated, for example, when it has already been calculated in the offline project.
- "Complete calculation"; the motor data will be calculated completely. The data to be calculated is listed in parameter [p0340](SINAMICS%20Parameter%20G120.md#p03400n-automatic-calculation-motorcontrol-parameters-2).

#### Additional parameters

---

### Important parameters

#### Description

Set the values of the most important parameters.

Depending on which option you have activated in the Setpoint specification mask, different settings must be parameterized.

The following settings must be parameterized in the "Setpoint specification" mask if you have activated the option "Drive is connected to a PLC. Ramp-function generator is in the PLC".

1. Enter a value for the "Reference speed" ([p2000](SINAMICS%20Parameter%20G120.md#p2000-reference-speed-reference-frequency)), which is the reference variable for the speed and frequency. All of the speeds or frequencies specified as relative values refer to this reference variable.
2. At "Maximum speed" ([p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3)), enter a value for the maximum possible speed.

   > **Note**
   >
   > **For G115D drive**
   >
   > - The maximum speed (p1082) is set to 120% of nominally calculated value using a check box.
   > - When the ramp function is activated via DIP switch, the "OFF1 ramp-down time" field is disabled in the commissioning wizard.
3. Enter a value for the ramp-function generator ramp-down time at "OFF1 ramp-down time" ([p1121](SINAMICS%20Parameter%20G120.md#p11210n-ramp-function-generator-ramp-down-time-5)).
4. Enter a value for the ramp-function generator ramp-down time at "OFF3·(quick·stop)·ramp-down·time" ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)).
5. Enter a value for the current limit at "Current limit" ([p0640](SINAMICS%20Parameter%20G120.md#p06400n-current-limit-1)).

The following settings must be parameterized in the "Setpoint specification" mask if you have activated the option "Drive is connected to a PLC. Ramp-function generator is in the drive".

1. Enter a value for the "Reference speed" (p2000), which is the reference variable for the speed and frequency. All of the speeds or frequencies specified as relative value refer to this reference variable.
2. At "Maximum speed" (p1082), enter a value for the maximum possible speed.
3. Enter a value for the ramp-function generator ramp-up time at "Ramp-up time" ([p1120](SINAMICS%20Parameter%20G120.md#p11200n-ramp-function-generator-ramp-up-time-3)).
4. Enter a value for the ramp-function generator ramp-down time at "OFF1 ramp-down time" (p1121).
5. Enter a value for the ramp-function generator ramp-down time at "OFF3·(quick·stop)·ramp-down·time" (p1135).
6. Enter a value for the current limit at "Current limit" (p0640).

The following settings must be parameterized in the "Setpoint specification" mask if you have activated the option "Drive is not connected to any PLC. Ramp-function generator is in the drive".

1. Enter a value for the "Current limit" that defines the limit value of the maximum output current ([p0305](SINAMICS%20Parameter%20G120.md#p03050n-rated-motor-current)), ([p0640](SINAMICS%20Parameter%20G120.md#p06400n-current-limit-1)).
2. At "Min. speed" ([p1080](SINAMICS%20Parameter%20G120.md#p10800n-minimum-speed)) or "Max. speed" (p1082), enter a value for the minimum/maximum motor speed with which the motor can operate or is limited irrespective of the speed setpoint. The set value is valid for both directions of rotation.
3. Enter a value for the ramp-function generator ramp-up time at "Ramp-up time" (p1120).
4. Enter a value for the ramp-function generator ramp-down time at "Ramp-down time" (p1121).

   The ramp-up/ramp-down time always refers to the time interval from motor standstill to the set maximum speed (without using roundings).
5. Enter a value for the ramp-down time at "OFF3 ramp-down time" (p1135).

   The OFF3 ramp-down time is effective from the maximum speed down to motor standstill.

#### Additional parameters

---

### Configuring the encoder

This section contains information on the following topics:

- [Encoder](#encoder)
- [Encoder data](#encoder-data)
- [ENDAT + SIN/COS encoder](#endat-sincos-encoder)
- [TTL/HTL incremental encoder](#ttlhtl-incremental-encoder)
- [SIN/COS incremental encoders](#sincos-incremental-encoders)
- [Resolver](#resolver)
- [SSI encoder](#ssi-encoder)

#### Encoder

##### Description

Specify the encoder here:

- Encoder 1: Motor encoder (HTL encoder)
- Encoder 2: External measuring system (SSI encoder)

You can select the interface to which your encoder is connected for the G120 CU250S-2:

- Select one of the following interfaces in the "Encoder interface" drop-down list:

  - Terminal interface
  - Sub-D interface
  - DRIVE-CLiQ interface; the encoder is connected directly. The encoder data is known after the upload.

The configuration of the measuring systems is carried out by either selecting a standard encoder from the list or by entering the encoder data:

**Select standard encoder from the list**

- Select the encoder type from the drop-down list.

  - For the motor encoder (Encoder 1), the measuring systems that can be configured together with the previously selected motor type are offered in the list.
  - For external measuring systems, the measuring systems that are supported by the drive are offered. The code numbers (values) are displayed here additionally; these can be used in the parameter p400 to select the encoder via the expert list.

**Enter encoder data**

1. In order to be able to enter user-defined encoder data, select the "Encoder data" option in the "Encoder configuration" drop-down list.
2. Click the "[Encoder data](#encoder-data)" button to open the dialog box.

#### Encoder data

##### Description

In this dialog you specify the user-defined encoder data for external encoders. The encoders that can be used depend on the converter used.

##### General

Enter the general encoder data for external encoders in this tab.

The technical data of the external encoder is on the encoder. Note the data and enter it or activate the appropriate options.

**Encoder type**

- Select whether you use a linear or a rotary encoder.

The following encoder measuring systems can be configured via the selection list:

> **Note**
>
> The setting options are dependent on the encoder type. Detailed descriptions of the setting options can be found in the online help for the encoder types.

- [TTL/HTL incremental encoder](#ttlhtl-incremental-encoder)
- [SSI encoder](#ssi-encoder)

> **Note**
>
> The actual position values are normalized to encoder lines in the PROFIdrive profile. With the SSI encoder without incremental tracks, the singleturn resolution is taken over as the number of pulses per revolution as a substitute.

##### Details

You can specify further parameters for the selected encoders (motor and load encoders) (encoder 1 to 3) in this tab.

The data for the selected encoders will be transferred automatically

**Gear ratio**

The gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft.

> **Note**
>
> Parameters [p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions) and [p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions) are also used for indirect measuring systems and therefore have no relation to the motor.
>
> For example, the encoder for the indirect measuring system can be mounted for the position determination behind the load gearbox and also above a measuring gearbox.

**Inversion**

Because the installation direction of the encoder (at the right- or left-hand side) cannot be defined, but rather depends on the conditions of the machine (linear motor, torque motor, etc.), you can invert the position and the speed and thus perform a direction reversal.

1. Activate the "Invert actual speed value" option to invert the actual speed value.
2. Activate the "Invert actual position value" option to invert the actual position value.

**Fine resolution**

- Specify the fine resolution of the incremental actual position values [bits]:

  - G1_XIST1 / G2_XIST1
  - G1_XIST2 / G2_XIST2 (only for absolute encoder)

##### **Encoder selection with synchronous motors (G115D only)**

For G115D, when you select the synchronous motors, the encoder 1 is enabled in "Encoder" page of the commissioning wizard.

##### **Encoder data for G115D**

A user selectable high speed input can be configured for G115D converters using the onboard digital inputs DI0 and DI1.

> **Note**
>
> The existing BICO interconnections for these DI0 and DI1 must be deselectecd while using the encoder function.

##### Additional parameters

---

---

**See also**

[ENDAT + SIN/COS encoder](#endat-sincos-encoder)
  
[SIN/COS incremental encoders](#sincos-incremental-encoders)
  
[Resolver](#resolver)

#### ENDAT + SIN/COS encoder

##### Description

Absolute encoders (absolute shaft encoders) are designed on the same scanning principle as incremental encoders, but have a greater number of tracks. For example, if there are 13 tracks, then 2<sup>13</sup> = 8192 steps are coded for singleturn encoders. The code used is a one-step code (Gray code) which prevents any scanning errors from occurring. After switching on the machine, the position value is transferred immediately to the evaluation module. Data is transferred between the encoder and the evaluation module via EnDat.

Two protocols are supported:

- EnDat01; the encoders generally have a sin/cos track and are connected to SMx20, SME25 or SME125.
- Endat22; the encoders generally have no incremental tracks and are connected to SMC40.

> **Note**
>
> **EnDat encoder functional scope**
>
> SIEMENS does not support the full functional scope of EnDat encoder

A reference point approach is omitted, but an absolute encoder adjustment must be performed during the first commissioning with a higher-level controller or EPOS.

![EnDat absolute encoder](images/103277844619_DV_resource.Stream@PNG-en-US.png)

EnDat absolute encoder

**Identify encoder**

- Select the option if you want to fetch the encoder configuration from the encoder (only online).

**Incremental tracks**

The parameters for the number of pulses/revolution are transferred over the course of the encoder identification (for EnDat22, that corresponds to a virtual number of pulses).

##### Gear ratio / measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

#### TTL/HTL incremental encoder

##### Description

These encoders operate analogously to the SIN/COS incremental encoders, although they supply a different output level. They are also referred to as pulse or square-wave encoders. The signals are quadrupled by an edge evaluation.

- HTL (High Voltage Transistor Logic); in unipolar design can be connected to the SMC30.
- RS 422 difference signals (TTL = Transistor Transistor Logic); in bipolar design can be connected to the SMC30.
- The resolution can be improved by a factor of four for TTL and HTL encoders through edge evaluation.
- TTL/HTL encoders are offered in the Startdrive with and without SSI protocol.

> **Note**
>
> **Using the SSI protocol**
>
> You can find information about the SSI protocol at [SSI encoder](#ssi-encoder).

**TTL/HTL encoder mode of operation.**

![TTL pulse encoder](images/103174101515_DV_resource.Stream@PNG-en-US.png)

TTL pulse encoder

After the signal edges of tracks A and B have been evaluated, direction-dependent speed and position information is available.

**Absolute position**

After a machine is switched on, a reference point approach must be carried out to determine the absolute position.

**HTL/TTL encoder type**

The following general parameters can be selected for the HTL/TTL encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": Select this option when a rotary encoder is available.
- "Linear": Select this option when a linear scale is available.

**Power supply ([p0404](SINAMICS%20Parameter%20G120.md#p04040n-encoder-configuration-effective-2))**

- Select the appropriate voltage supply for your encoder:

  - 5 V
  - 24 V (HTL encoder)
  - "Remote sense"; activate this option if you want to use remote sensing to ensure that a possible voltage drop along the cable is compensated.

**Incremental tracks**

The resolution of the encoder is determined by its "number of pulses". This value is located on the encoder type plate and in the associated data sheet.

- "Number of pulses per revolution": Enter the pulse number for the encoder.
- "Level": Select whether you use an HTL (High Threshold Logic) or a TTL (Transistor-Transistor Logic) encoder.
- "Signal": Select whether the encoder transfers a unipolar (ground-based) or a bipolar (differential) signal. Unipolar signals lie in the range von 0 ... 5 V. Bipolar signals lie in the range von -5 ... 5 V.
- "Track monitoring": Activate this option if you want to monitor the incremental track. Note that TTL signals can only be evaluated bipolarly.

**Zero marks (p0404)**

Zero marks serve as reference signal for incremental encoders. Select the appropriate zero signal for your encoder:

- No zero mark
- No zero mark monitoring
- One zero mark per revolution
- Several zero marks per revolution (equidistant zero marks):

  - The number of pulses between the two equidistant zero marks are parameterized at "Zero mark distance".
  - "Number of zero marks": Enter the number of zero marks here. Enter a number ≥ 2.
- Irregular zero marks: Select this option if the zero marks are not equidistant and thus no gap monitoring of the zero marks is possible.
- [Distance-coded zero marks](Configuring%20SINAMICS%20S-G-MV%20drives.md#distance-coded-zero-marks)

##### Gear ratio / measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

---

**See also**

[SSI encoder](#ssi-encoder)

#### SIN/COS incremental encoders

##### Description

Incremental encoders operate on the principle of optoelectronic scanning of dividing discs with the transmitted-light method. The light source is a light emitting diode (LED). The light-dark modulation generated as the encoder shaft rotates is picked up by photoelectronic elements. With an appropriate arrangement of the line pattern on the dividing disk connected to the shaft and the fixed aperture, the photoelectronic elements provide two trace signals A and B at 90° to one another, as well as a reference signal R. The encoder electronics amplify these signals and convert them to sin/cos 1 Vpp.

**Absolute position**

After a machine is switched on, a reference point approach must be carried out to determine the absolute position.

**SIN/COS encoder operation**

![Sine/cosine incremental encoder](images/103277890955_DV_resource.Stream@PNG-en-US.png)

Sine/cosine incremental encoder

**SIN/COS encoder type**

The following general parameters can be selected for the SIN/COS encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": Select this option when a rotatory encoder is available.
- "Linear": Select this option when a linear scale is available.

**Power supply ([p0404](SINAMICS%20Parameter%20G120.md#p04040n-encoder-configuration-effective-2))**

- Select the appropriate voltage supply for your encoder:

  - 5 V
  - "Remote sense"; remote sensing ensures that a possible voltage drop along the cable is compensated.

**Incremental tracks ([p0408](SINAMICS%20Parameter%20G120.md#p04080n-rotary-encoder-pulse-number-1))**

- Enter the number of pulses per revolution for your encoder. The number of pulses per revolution can also be specified in bits in the encoder data sheets. Encoder pulse number = 2<sup>resolution in bit</sup>.

**Coarse synchronization (p0404)**

- Select how coarse synchronization is to be carried out. You thereby define how the pole position identification is to be carried out.

  - Track C/D; the flux position can be determined using the C/D track and the zero mark, which is adjusted to the magnetic position of the rotor. As the C/D track only has one encoder pulse per mechanical revolution, the accuracy of this determination method is only adequate for starting. Therefore, you must carry out fine synchronization, see also [Rotor position synchronization (servo)](Servo%20drives%20%28highly%20dynamic%29.md#rotor-position-synchronization-servo-1).
  - Hall sensor (only for linear motors); Hall sensors are used that measure the magnetic flux. Two sensors are used, which supply information equivalent to a C/D track for each pole pair.
  - None

**Zero marks (p0404)**

Zero marks serve as reference signal for incremental encoders. Select the appropriate zero signal for your encoder:

- No zero mark
- Equidistant zero marks (evaluate several zero marks):

  - The number of pulses between the two equidistant zero marks are parameterized at "Zero mark distance".
- Irregular zero marks: Select this option if the zero marks are not equidistant and thus no gap monitoring of the zero marks is possible.
- [Distance-coded zero marks](Configuring%20SINAMICS%20S-G-MV%20drives.md#distance-coded-zero-marks)

##### Gear ratio / measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

#### Resolver

##### Description

Resolvers are rotary encoders that supply an absolute signal within a pole pitch. Therefore, resolvers do not have to be homed.

In principle, a resolver is made up of two components:

- Two stator windings offset by 90°
- One rotor

With the aid of an excitation voltage (typically 8 kHz), two tracks offset by 90° are generated according to the transformer principle, with an amplitude that depends upon the rotor position. The evaluation of the signals that are still modulated with the excitation frequency is done in the SMx10, which means that the speed, actual position value, rotor position and reference point are available.

![Resolver](images/103277924491_DV_resource.Stream@PNG-en-US.png)

Resolver

> **Note**
>
> When a multi-pole resolver is used, the number of resolver poles matches the number of motor poles.

**Encoder type Resolver**

The following general parameters can be selected for the resolver encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": This option is preselected for resolvers.

**Enter the number of pole pairs ([p0408](SINAMICS%20Parameter%20G120.md#p04080n-rotary-encoder-pulse-number-1))**

- Enter the number of pole pairs that the associated encoder provides.

##### Gear ratio / measuring gearbox

Gearboxes or measuring gearboxes are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

#### SSI encoder

##### SSI encoder

SSI encoders use the SSI protocol for the data transfer. The SSI protocol is a serial data transfer between an encoder and an evaluation module.

> **Note**
>
> **Data sheet of the encoder being used**
>
> To parameterize the SSI protocol, it is absolutely necessary that you have the encoder data sheet at hand. Use the information in the data sheet to set the protocol parameters. Not all encoders support the parameterizable functions.

**Encoder type SSI**

The following general parameters can be selected for the SSI encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": Select this option when a rotatory encoder is available.
- "Linear": Select this option when a linear scale is available.

**Power supply ([p0404](SINAMICS%20Parameter%20G120.md#p04040n-encoder-configuration-effective-2))**

- Select the appropriate voltage supply for your encoder:

  - 5 V
  - 24 V
  - "Remote sense"; remote sensing ensures that a possible voltage drop along the cable is compensated.

##### Absolute SSI protocol

**Multiturn**

- Select in the drop-down list whether your encoder is multiturn-conform:

**Singleturn resolution ([p0423](SINAMICS%20Parameter%20G120.md#p04230n-absolute-encoder-rotary-singleturn-resolution-1))**

Singleturn encoders divide one rotation (360 degrees mechanical) into a specific number of encoder pulses, e.g. 8192. A unique code word is assigned to each position. After 360° the position values are repeated.

- Enter the singleturn resolution based on your encoder data sheet.

**Multiturn resolution ([p0421](SINAMICS%20Parameter%20G120.md#p04210n-absolute-encoder-rotary-multiturn-resolution-1))**

Multiturn encoders also record the number of revolutions, in addition to the absolute position within one revolution. To do this, further code disks which are coupled via gear steps with the encoder shaft are scanned. When evaluating 12 additional tracks, this means that an additional 4096 revolutions can be coded.

- Enter the multiturn resolution based on your encoder data sheet.

##### SSI protocol structure

The SSI connection between the encoder and the encoder module is established using four wires. This is a serial transmission.

The data transmission with the SSI protocol is performed in just one direction, i.e. the data is transferred from the encoder to the evaluation module. The data is a position value for a rotary or linear measuring system and, possibly, further bits that describe the position value.

The structure of the telegram differs depending on the encoder manufacturer and the measuring system. Consequently, you must use the information provided by the manufacturer that describes the protocol structure in detail. Manufacturers frequently extend the position value and leading and trailing zero bits to produce a telegram length of 13, 21 or 25 bits. Whereby this information is extended to 9 bits for a telegram of 21 bits or to 12 bits for a telegram of 25 bits. In the meantime, however, any telegram length is common. In the following example, 29-bit position data is transferred and extended with 3 bits before and after the position.

| Bits before the position |  |  | Position bits |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Bits after the position |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x | x | x | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | x | x | x |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
| P indicates the position bits; x indicates the possible position of fault, alarm and parity bits. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### Parameters that can be set for the SSI protocol

**Code ([p0429](SINAMICS%20Parameter%20G120.md#p04290n-encoder-ssi-configuration-1))**

- Here, select which code versions your encoder supports:

  - Gray code; special coding of transfer signals; when transitioning from one position to another, only one bit is always changed.
  - Binary code; binary-coded transfer signals

**Baud rate ([p0427](SINAMICS%20Parameter%20G120.md#p04270n-encoder-ssi-baud-rate-1))**

- Here, enter the baud rate for the SSI encoder.

  When setting the baud rate, also take into account the update rate of the speed or actual position value. All bits must be transferred within the cycle, as otherwise the data transfer is too slow and only performed every xth cycle. If you are using an SSI encoder with incremental track, the incremental track is used for the speed control.

  **Example**: For a baud rate of 100 kHz and an SSI length of 35 bits, 10x35 µs = 350 µs + 30 µs monoflop time = 380 µs are required to transfer the SSI value. If the current controller cycle is faster, you must set a higher baud rate.

  The possible baud rate depends on the cable length (see the diagram).

  ![Parameters that can be set for the SSI protocol](images/103174189067_DV_resource.Stream@PNG-en-US.png)

**Parameterizing the protocol**

For the protocol, define the "Position length", "Bit before position" and "Bit after position" parameters:

1. Enter a value for the "Position length in bits" ([p0447](SINAMICS%20Parameter%20G120.md#p04470n-encoder-ssi-number-of-bits-absolute-value-1)). Refer to the encoder data sheet to identify which value is suitable for your encoder. For a singleturn encoder, for example, 13 bits are used for the position information, and 25 bits for a multiturn encoder (this contains 13 bits of singleturn information).

   Also observe the count direction for the position bit. For the examples shown here, the protocols start with "0" (ascending from left to right). However, there are also manufacturers who have defined a different way of counting, starting from the MSB, counting downward from left to right. Therefore, compare the setting with the data in the encoder data sheet.
2. Enter a value for the "Bits before the position" ([p0446](SINAMICS%20Parameter%20G120.md#p04460n-encoder-ssi-number-of-bits-before-the-absolute-value-1)); see the diagram above.
3. Enter a value for the "Bits after the position" ([p0448](SINAMICS%20Parameter%20G120.md#p04480n-encoder-ssi-number-of-bits-after-the-absolute-value-1)); see the diagram above.

##### Bit functions in the SSI protocol

If alarm bits, error bits or parity bits signal errors when transferring data, in Startdrive, alarms or faults are output in the inspector window.

**Alarm bit ([p0435](SINAMICS%20Parameter%20G120.md#p04350n-encoder-ssi-alarm-bit-1)) – only if the encoder supports it**

If the encoder manufacturer has added alarm bits to the position value, you should certainly evaluate these because they provide the only possibility to output alarms regarding the position value. For example, the encoder may be soiled.

The alarm bit triggers an alarm on the SINAMICS device (A3x412, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).

1. At "Bit activation", activate the alarm bit.
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. At "Logical state", select at which level (high active or low active) the alarm bit should be output. High active means that the corresponding alarm is displayed on the SINAMICS when the bit is set.

**Error bits ([p0434](SINAMICS%20Parameter%20G120.md#p04340n-encoder-ssi-error-bit-1)) – only if the encoder supports it**

If the encoder manufacturer has added error bits to the position value, you must also evaluate them because they allow you to determine the validity of the position value.

Error bits trigger a fault on the SINAMICS device (F3x112, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).

1. At "Bit activation", select the bit number for the error bit. You can parameterize several error bits (see online help for parameters)
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. At "Logical state", select at which level (high active or low active) the error bit should be output. High active means that the corresponding fault is displayed on the SINAMICS when the bit is set.

**Parity bits ([p0436](SINAMICS%20Parameter%20G120.md#p04360n-encoder-ssi-parity-bit-1)) – only if the encoder supports it**

Another possibility to validate the transmission is to transfer a parity bit in the telegram. This is a parity check for all of the bits of the telegram content. The following settings apply for the parity: even (= low level) and odd (= high level). Refer to the data sheet to see whether the encoder uses "even" or "odd" as checking criterion for the parity bit.

Example for "even" parity:

The number of bits filled with 1 in the telegram must always be even. An odd number of set bits is compensated by the parity bit. If an uneven number of set bits is nevertheless determined in the evaluation module, a fault is output on the SINAMICS side (F3x110 Bit 11, with x=1,2,3 for encoder 1, 2, 3).

For "uneven" parity, the inverse logic applies accordingly.

1. At "Bit activation", select the bit number for the parity bit.
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. Under "Logic state", select whether the parity bit has even or odd logic.

**Example telegram**

![SSI encoder example telegram](images/103174138891_DV_resource.Stream@PNG-en-US.png)

SSI encoder example telegram

**Monoflop time ([p0428](SINAMICS%20Parameter%20G120.md#p04280n-encoder-ssi-monoflop-time-1))**

The monoflop time describes the minimum wait time between two transfers of the absolute value for the SSI encoder. The set value must be greater than or equal to the value specified in the data sheet for the encoder.

- Enter the monoflop time.

**Transfer the position value twice (p0429) – only if the encoder supports it**

Some manufacturers allow a position value to be transferred twice; this is called "ring shift" or "fetch doubled". It detects transmission errors, although it extends the time taken to transfer the position value. At least one fill bit is necessary between reading out the first time and second time. You can also refer to the encoder data sheet for the number of fill bits. The following example shows the use of fill bits:

- Select "Double transfer" and enter a value for the fill bits ([p0449](SINAMICS%20Parameter%20G120.md#p04490n-encoder-ssi-number-of-bits-filler-bits-1)).

![SSI encoder position value](images/103174151179_DV_resource.Stream@PNG-en-US.png)

SSI encoder position value

##### Gear ratio / measuring gearbox

Gearboxes or measuring gearboxes are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

### Dimension system

#### Description

Specify here the encoder system for the actual position value preparation.

**Select the encoder system**

The selection list shows all encoders that have been configured in the various drive data sets. If, for example, encoder 1 and 3 were configured in data set 1, and encoder 2 and 3 were configured in data set 2, then all three encoders will be offered for selection.

- Select an encoder system from this list.

### Mechanical system (G120D only)

#### Description

You can configure here the position resolution and the associated mechanical system. Depending on the encoder type selected for the position control, the selected encoder type for the motor encoder and the dimension system, various constellations can occur for the mechanical system.

**Encoder**

The display box shows the encoder system selected in the dimension system.

**LU per load revolution (encoder resolution)**

The field shows the maximum possible LU per load revolution that result for rotary encoders because of the configured mechanical system and the encoder data.

The maximum value per load revolution is calculated as follows:

Maximum value per load revolution = absolute value of the product of "Encoder pulse number per revolution" and "Fine resolution"multiplied by the quotient from "Motor revolutions" divided by "Load revolutions".

**Load revolutions**

Load revolutions can be used to specify the gear ratio numerator. The gear ratio provides the ratio of the motor shaft to the load shaft.

**Motor revolutions**

Motor revolutions can be used to specify the gear ratio denominator. The gear ratio acts directly on the maximum possible LU per load revolution. The more motor revolutions possible per load revolution, the higher is the resolution.

**Fine resolution**

The fine resolution is a multiplication factor for the encoder resolution.

**LU per load revolution (position setpoint / actual value resolution) (only rotary encoder)**

LU per load revolution is used to provide the relationship between the physical conditions and the drive-internal neutral LU. This requires that you know the mechanical data for your system (mm/revolution) and the resolution that you want to attain. If, for example, you use a ball screw with 10 mm/revolution, then you can enter an LU per load revolution of 10000 when you want to achieve a resolution of 1 µm.

**Encoder system**

The resolution possible for the encoder system is displayed here. The graphic changes depending on whether you use a motor encoder or some other encoder.

**Modulo correction (basic positioner)**

- Select this option if you want to enter a modulo correction (modulo length).

### Summary

#### Description

This is a summary of all the configuration settings.

#### Continue to use the summary

- Click "Copy text to the clipboard" if you want to copy a summary of the drive configuration to a different application, e.g. to print it there.
