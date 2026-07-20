---
title: "Using S7-1500/S7-1500T Axis functions (S7-1500, S7-1500T)"
package: TFTOSMCAxisenUS
topics: 265
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using S7-1500/S7-1500T Axis functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Overview of functions (S7-1500, S7-1500T)](#overview-of-functions-s7-1500-s7-1500t)
- [Axis functions (S7-1500, S7-1500T)](#axis-functions-s7-1500-s7-1500t)
- [Commissioning (S7-1500, S7-1500T)](#commissioning-s7-1500-s7-1500t)
- [Diagnostics (S7-1500, S7-1500T)](#diagnostics-s7-1500-s7-1500t)
- [Tags of the technology object data blocks (S7-1500, S7-1500T)](#tags-of-the-technology-object-data-blocks-s7-1500-s7-1500t)
- [Appendix (S7-1500, S7-1500T)](#appendix-s7-1500-s7-1500t)

## Overview of functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Speed axis technology object (S7-1500, S7-1500T)](#speed-axis-technology-object-s7-1500-s7-1500t)
- [Positioning axis technology object (S7-1500, S7-1500T)](#positioning-axis-technology-object-s7-1500-s7-1500t)
- [Synchronous axis technology object (S7-1500, S7-1500T)](#synchronous-axis-technology-object-s7-1500-s7-1500t)
- [External encoder technology object (S7-1500, S7-1500T)](#external-encoder-technology-object-s7-1500-s7-1500t)
- [Motion control instructions for axis control (S7-1500, S7-1500T)](#motion-control-instructions-for-axis-control-s7-1500-s7-1500t)
- [Extended functions of the technology CPU (S7-1500T)](#extended-functions-of-the-technology-cpu-s7-1500t)
- [Functions in STEP 7 (S7-1500, S7-1500T)](#functions-in-step-7-s7-1500-s7-1500t)

### Speed axis technology object (S7-1500, S7-1500T)

![Figure](images/165572503051_DV_resource.Stream@PNG-de-DE.png)

The speed axis technology object calculates speed setpoints, taking into account the dynamic settings, and outputs them to the drive. All motions of the speed axis take place as speed-controlled motions. An existing load gear is taken into account on the system side.

You can find an overview of the supported instructions of the speed axis technology object in the section "[Motion Control instructions for axis control](#motion-control-instructions-for-axis-control-s7-1500-s7-1500t)".

A drive is assigned to each speed axis, e.g. via a PROFIdrive telegram.

The speed is specified in revolutions per unit of time.

The following figure shows the basic principle of operation of the speed axis technology object:

![Figure](images/165570748555_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following configurations are available in the speed axis technology object:

- Basic parameters

  - [Units of measure](#units-of-measure-s7-1500-s7-1500t)
  - [Virtual axis](#virtual-axis-s7-1500-s7-1500t)
  - [Axis in simulation](#axis-in-simulation-s7-1500-s7-1500t)
- Hardware interface

  - [Connecting PROFIdrive drives](#connecting-profidrive-drives-s7-1500-s7-1500t)
  - [Transfer drive parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
  - [Connecting stepper motors](#connecting-stepper-motors-s7-1500-s7-1500t)
  - [Connecting drives with analog setpoint interface](#connecting-drives-with-analog-setpoint-interface-s7-1500-s7-1500t)
  - [Connecting force/torque data via SIEMENS additional telegram 750](#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)
- Mechanics

  - [Configuring the mechanics of the speed axis](#configuring-the-mechanics-of-the-speed-axis-s7-1500-s7-1500t)
  - [Configuring the load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
- [Dynamic default values](#velocity-profile-s7-1500-s7-1500t)
- [Emergency stop](#emergency-stop-deceleration-s7-1500-s7-1500t)
- [Configuring the alarm responses](#configuring-remove-enable-alarm-responses-s7-1500-s7-1500t)
- Limits

  - [Dynamic limits](#velocity-profile-s7-1500-s7-1500t)
  - [Torque limits](#forcetorque-limiting-s7-1500-s7-1500t)

### Positioning axis technology object (S7-1500, S7-1500T)

![Figure](images/165572508171_DV_resource.Stream@PNG-de-DE.png)

The positioning axis technology object calculates position setpoints, taking into account the encoder settings, and outputs corresponding speed setpoints to the drive. In position-controlled mode, all movements of the positioning axis take place as position-controlled movements. For absolute positioning, the physical position must be known to the positioning axis technology object.

You can find an overview of the supported instructions of the positioning axis technology object in the section "[Motion Control ‑ Instructions for axis control](#motion-control-instructions-for-axis-control-s7-1500-s7-1500t)".

Each positioning axis is assigned a drive, e.g. via a PROFIdrive telegram, and an encoder, via a PROFIdrive telegram.

The relationship between the encoder values and a defined position is established by the parameter assignment of the mechanical properties and encoder settings and by a homing operation. The technology object can also perform movements without a position relationship, and relative position movements, even without being in a homed status.

Depending on the design of the mechanics, a positioning axis can be configured as a linear or rotary axis.

The following figure shows the basic principle of operation of the positioning axis technology object:

![Figure](images/165751681035_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following configurations are available in the positioning axis technology object:

- Basic parameters

  - [Axis or encoder type](#configure-axis-type-s7-1500-s7-1500t)
  - [Units of measure](#units-of-measure-s7-1500-s7-1500t)
  - [Modulo setting](#modulo-setting-s7-1500-s7-1500t)
  - [Virtual axis](#virtual-axis-s7-1500-s7-1500t)
  - [Axis in simulation](#axis-in-simulation-s7-1500-s7-1500t)
- Hardware interface

  - [Connecting PROFIdrive drives](#connecting-profidrive-drives-s7-1500-s7-1500t)
  - [Connecting encoders via PROFIdrive](#connecting-encoders-via-profidrive-s7-1500-s7-1500t)
  - [Transferring drive and encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
  - [Connecting stepper motors](#connecting-stepper-motors-s7-1500-s7-1500t)
  - [Connecting drives with analog setpoint interface](#connecting-drives-with-analog-setpoint-interface-s7-1500-s7-1500t)
  - [Connecting force/torque data via SIEMENS additional telegram 750](#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)
- Mechanics

  - [Configuring drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
  - [Configuring the load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
  - [Configuring the encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
  - [Configuring the leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
  - [Backlash compensation](#backlash-compensation-s7-1500-s7-1500t)
- [Dynamic default values](#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
- [Emergency stop](#emergency-stop-deceleration-s7-1500-s7-1500t)
- [Configuring the alarm responses](#configuring-remove-enable-alarm-responses-s7-1500-s7-1500t)
- Limits

  - [Position limits](#traversing-range-limitation-s7-1500-s7-1500t)
  - [Dynamic limits](#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
  - [Torque limits](#forcetorque-limiting-s7-1500-s7-1500t)
  - [Fixed stop detection](#fixed-stop-detection-s7-1500-s7-1500t)
- Homing

  - [Active homing](#active-homing-s7-1500-s7-1500t)
  - [Passive homing](#passive-homing-s7-1500-s7-1500t)
- Position monitoring functions

  - [Position monitoring](#positioning-monitoring-s7-1500-s7-1500t)
  - [Following error](#following-error-monitoring-s7-1500-s7-1500t)
  - [Standstill signal](#standstill-signal-s7-1500-s7-1500t)
- Control loop

  - [Configuring position controller in the PLC](#configuring-position-controller-in-the-plc-s7-1500-s7-1500t)
  - [Configuring position controller for drives with DSC](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)
  - Configuring a dynamic filter
  - [Switching the position control off and on](#switching-the-position-control-off-and-on-s7-1500-s7-1500t)

The following configurations of the positioning axis technology object are specific to synchronous operation:

- Leading value settings

  - [Configuring provision of the leading value](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
  - [Configuring the delay time](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#setting-the-delay-times-s7-1500t)
- [Actual value extrapolation](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#actual-value-coupling-and-actual-value-extrapolation-s7-1500t)

You can find a description of the configuration parameters in the "S7-1500/S7-1500T synchronous operation functions" documentation.

### Synchronous axis technology object (S7-1500, S7-1500T)

![Figure](images/165340980363_DV_resource.Stream@PNG-de-DE.png)

The synchronous axis technology object includes all functions of the positioning axis technology object.

A synchronous axis can also follow the motions of a leading axis. The synchronous operation relationship between the leading and following axes is specified by a synchronous operation function.

You can find an overview of the supported instructions of the synchronous axis technology object in the section "[Motion control instructions for axis control](#motion-control-instructions-for-axis-control-s7-1500-s7-1500t)".

The figure below shows the basic principle of operation of the synchronous axis technology object:

![Figure](images/166628918923_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following non-isochronous specific configurations correspond to the positioning axis technology object:

- Basic parameters

  - [Axis or encoder type](#configure-axis-type-s7-1500-s7-1500t)
  - [Units of measure](#units-of-measure-s7-1500-s7-1500t)
  - [Modulo setting](#modulo-setting-s7-1500-s7-1500t)
  - [Virtual axis](#virtual-axis-s7-1500-s7-1500t)
  - [Axis in simulation](#axis-in-simulation-s7-1500-s7-1500t)
- Hardware interface

  - [Connecting PROFIdrive drives](#connecting-profidrive-drives-s7-1500-s7-1500t)
  - [Connecting encoders via PROFIdrive](#connecting-encoders-via-profidrive-s7-1500-s7-1500t)
  - [Transferring drive and encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
  - [Connecting stepper motors](#connecting-stepper-motors-s7-1500-s7-1500t)
  - [Connecting drives with analog setpoint interface](#connecting-drives-with-analog-setpoint-interface-s7-1500-s7-1500t)
  - [Connecting force/torque data via SIEMENS additional telegram 750](#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)
- Mechanics

  - [Configuring drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
  - [Configuring the load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
  - [Configuring the encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
  - [Configuring the leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
  - [Configuring backlash compensation](#backlash-compensation-s7-1500-s7-1500t)
- [Dynamic default values](#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
- [Emergency stop](#emergency-stop-deceleration-s7-1500-s7-1500t)
- [Configuring the alarm responses](#configuring-remove-enable-alarm-responses-s7-1500-s7-1500t)
- Limits

  - [Position limits](#traversing-range-limitation-s7-1500-s7-1500t)
  - [Dynamic limits](#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
  - [Torque limits](#forcetorque-limiting-s7-1500-s7-1500t)
  - [Fixed stop detection](#fixed-stop-detection-s7-1500-s7-1500t)
- Homing

  - [Active homing](#active-homing-s7-1500-s7-1500t)
  - [Passive homing](#passive-homing-s7-1500-s7-1500t)
- Position monitoring functions

  - [Position monitoring](#positioning-monitoring-s7-1500-s7-1500t)
  - [Following error](#following-error-monitoring-s7-1500-s7-1500t)
  - [Standstill signal](#standstill-signal-s7-1500-s7-1500t)
- Control loop

  - [Configuring position controller in the PLC](#configuring-position-controller-in-the-plc-s7-1500-s7-1500t)
  - [Configuring position controller for drives with DSC](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)
  - Configuring a dynamic filter
  - [Switching the position control off and on](#switching-the-position-control-off-and-on-s7-1500-s7-1500t)

You can find a description of the configuration parameters in the "S7-1500/S7-1500T Axis functions" documentation.

The following configurations of the synchronous axis technology object are specific to synchronous operation:

- [Leading value interconnections](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#defining-leading-value-interconnection-s7-1500-s7-1500t)
- Leading value settings

  - [Configuring provision of the leading value](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
  - [Configuring the delay time](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#setting-the-delay-times-s7-1500t)
- [Actual value extrapolation](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#actual-value-coupling-and-actual-value-extrapolation-s7-1500t)

You can find a description of the configuration parameters in the "S7-1500/S7-1500T synchronous operation functions" documentation.

### External encoder technology object (S7-1500, S7-1500T)

![Figure](images/165572705291_DV_resource.Stream@PNG-de-DE.png)

The external encoder technology object detects a position and makes this available to the controller.

The actual position detected by the external encoder can be used for the following functions, for example:

- Measured value acquisition by a measuring input
- Position-dependent generation of switching signals and switching signal sequences by output cam and cam track with actual value reference.
- As a leading value of a synchronous axis (S7-1500T)

The relationship between the encoder values and a defined position is established by the parameter assignment of the mechanical properties and encoder settings and by a homing operation.

You can find an overview of the supported instructions of the positioning axis technology object in the section "[Motion Control ‑ Instructions for axis control](#motion-control-instructions-for-axis-control-s7-1500-s7-1500t)".

The following figure shows the basic principle of operation of the external encoder technology object:

![Figure](images/172718453131_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following configurations are available in the technology object external encoder:

- Basic parameters

  - [Configure the type of an external encoder](#configure-the-type-of-an-external-encoder-s7-1500-s7-1500t)
  - [Units of measure](#units-of-measure-s7-1500-s7-1500t)
  - [Modulo setting](#modulo-setting-s7-1500-s7-1500t)
- Hardware interface

  - [Connecting encoders via PROFIdrive](#connecting-encoders-via-profidrive-s7-1500-s7-1500t)
- Mechanics

  - [Configuring the mechanics of the external encoder](#configuring-the-mechanics-of-the-external-encoder-s7-1500-s7-1500t)
  - [Configuring the load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
  - [Configuring the leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
- Homing

  - [Passive homing](#passive-homing-s7-1500-s7-1500t)
- Standstill

  - [Standstill](#standstill-signal-s7-1500-s7-1500t)

The following configurations of the external encoder technology object are specific to synchronous operation:

- Leading value settings

  - [Configuring provision of the leading value](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
  - [Configuring the delay time](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#setting-the-delay-times-s7-1500t)
- [Actual value extrapolation](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#actual-value-coupling-and-actual-value-extrapolation-s7-1500t)

You can find a description of the configuration parameters in the "S7-1500/S7-1500T synchronous operation functions" documentation.

### Motion control instructions for axis control (S7-1500, S7-1500T)

You can execute the functions of the speed axis, positioning axis, synchronous axis and external encoder technology objects using motion control instructions in your user program or using the TIA Portal (under "Technology object > Commissioning").

The following table shows the motion control instructions that are supported by the technology objects:

| Motion control instruction | Validity |  | Technology object |  |  |
| --- | --- | --- | --- | --- | --- |
| S7-1500 | S7-1500T | [Speed axis](#speed-axis-technology-object-s7-1500-s7-1500t) | [Positioning axis](#positioning-axis-technology-object-s7-1500-s7-1500t)    [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t) | [External encoder](#external-encoder-technology-object-s7-1500-s7-1500t) |  |
| "[MC_Power](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_power-v8-s7-1500-s7-1500t)"  Enable, disable technology object | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_Reset](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_reset-v8-s7-1500-s7-1500t)"  Acknowledge alarms, restart technology object | ✓ | ✓ | ✓ | ✓ | ✓ |
| "[MC_Home](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_home-v8-s7-1500-s7-1500t)"  Home technology object, set home position | ✓ | ✓ | - | ✓ | ✓ |
| "[MC_Halt](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_halt-v8-s7-1500-s7-1500t)"  Pause axis | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_MoveAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_moveabsolute-v8-s7-1500-s7-1500t)"  Position axis absolutely | ✓ | ✓ | - | ✓ | - |
| "[MC_MoveRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_moverelative-v8-s7-1500-s7-1500t)"  Position axis relatively | ✓ | ✓ | - | ✓ | - |
| "[MC_MoveVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movevelocity-v8-s7-1500-s7-1500t)"  Move axes with velocity/speed setpoint | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_MoveJog](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movejog-v8-s7-1500-s7-1500t)"  Move axis in jog mode | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_MoveSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movesuperimposed-v8-s7-1500-s7-1500t)"  Positioning axis overlapping | ✓ | ✓ | - | ✓ | - |
| "[MC_HaltSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_stopsuperimposed-v8-s7-1500-s7-1500t)"  Pause superimposed motions on the axis. | ✓ | ✓ | - | ✓ | - |
| "[MC_SetSensor](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setsensor-v8-s7-1500t)"  Switch alternative encoder to operative encoder | - | ✓ | - | ✓ | - |
| "[MC_Stop](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_stop-v8-s7-1500-s7-1500t)"  Stop axis and prevent new motion jobs | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_SetAxisSTW](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setaxisstw-control-bits-of-control-word-1-and-2-v8-s7-1500-s7-1500t)"  Control bits of control word 1 and control word 2 | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_WriteParameter](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-write-parameter-v8-s7-1500-s7-1500t)"  Write parameter | ✓ | ✓ | ✓ | ✓ | ✓ |
| "[MC_SaveAbsoluteEncoderData](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_saveabsoluteencoderdata-v8-s7-1500-s7-1500t)"   Save absolute adjustment for device replacement | ✓ | ✓ | - | ✓ | ✓ |
| "[MC_MotionInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninvelocity-v8-s7-1500t)"  Specify motion setpoints | - | ✓ | ✓ | ✓ | - |
| "[MC_MotionInPosition](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninposition-v8-s7-1500t)"  Specify motion setpoints | - | ✓ | - | ✓ | - |
| "[MC_MotionInSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninsuperimposed-v8-s7-1500t)"  Specify superimposed motion setpoints | - | ✓ | - | ✓ | - |
| "[MC_TorqueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torqueadditive-v8-s7-1500-s7-1500t)"  Specify additive torque | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_TorqueRange](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torquerange-v8-s7-1500-s7-1500t)"  Set high and low torque limit | ✓ | ✓ | ✓ | ✓ | - |
| "[MC_TorqueLimiting](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torquelimiting-v8-s7-1500-s7-1500t)"  Activate/deactivate force/torque limiting / fixed stop detection | ✓ | ✓ | ✓ | ✓ | - |

---

**See also**

[Introduction (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#introduction-s7-1500-s7-1500t)

### Extended functions of the technology CPU (S7-1500T)

In addition to the functionality of the S7-1500 CPU, the S7-1500T CPU provides additional functions:

| Additional functions | Description |
| --- | --- |
| [Multiple encoders for positioning axis/synchronous axis](#using-multiple-encoders-s7-1500t) | Up to four encoders can be connected to a positioning axis/synchronous axis. The encoders can be switched over during operation. Only one encoder at a time is active for closed loop position control. |
| ["MotionIn" function](#motion-specification-via-motionin-s7-1500t) | With the "MC_MotionInVelocity", "MC_MotionInPosition", and "MC_MotionInSuperimposed" motion control instructions, you can specify cyclically applicable calculated motion setpoints as the basic motion for the axis. No velocity profile is calculated for this, the values are directly active at the technology object. |

### Functions in STEP 7 (S7-1500, S7-1500T)

The following table shows the functions supported by technology objects in STEP 7:

| Functions in the TIA Portal | Technology object |  |  |
| --- | --- | --- | --- |
| [Speed axis](#speed-axis-technology-object-s7-1500-s7-1500t) | [Positioning axis](#positioning-axis-technology-object-s7-1500-s7-1500t)    [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t) | [External encoder](#external-encoder-technology-object-s7-1500-s7-1500t) |  |
| "Axis control panel"  Move and home axes using the TIA Portal | ✓ | ✓ | - |
| "Optimization"  Optimization of closed loop position control | - | ✓ | - |

## Axis functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuring basic parameters (S7-1500, S7-1500T)](#configuring-basic-parameters-s7-1500-s7-1500t)
- [Drive and encoder connection (S7-1500, S7-1500T)](#drive-and-encoder-connection-s7-1500-s7-1500t)
- [Safety functions in the drive (S7-1500, S7-1500T)](#safety-functions-in-the-drive-s7-1500-s7-1500t)
- [Mechanics (S7-1500, S7-1500T)](#mechanics-s7-1500-s7-1500t)
- [Configuring "Remove enable" alarm responses (S7-1500, S7-1500T)](#configuring-remove-enable-alarm-responses-s7-1500-s7-1500t)
- [Motion control and limits for dynamics (S7-1500, S7-1500T)](#motion-control-and-limits-for-dynamics-s7-1500-s7-1500t)
- [Traversing range limitation (S7-1500, S7-1500T)](#traversing-range-limitation-s7-1500-s7-1500t)
- [Homing (S7-1500, S7-1500T)](#homing-s7-1500-s7-1500t)
- [Position monitoring functions (S7-1500, S7-1500T)](#position-monitoring-functions-s7-1500-s7-1500t)
- [Configuring a control loop (S7-1500, S7-1500T)](#configuring-a-control-loop-s7-1500-s7-1500t)

### Configuring basic parameters (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configure axis type (S7-1500, S7-1500T)](#configure-axis-type-s7-1500-s7-1500t)
- [Configure the type of an external encoder (S7-1500, S7-1500T)](#configure-the-type-of-an-external-encoder-s7-1500-s7-1500t)
- [Units of measure (S7-1500, S7-1500T)](#units-of-measure-s7-1500-s7-1500t)
- [Modulo setting (S7-1500, S7-1500T)](#modulo-setting-s7-1500-s7-1500t)
- [Virtual axis (S7-1500, S7-1500T)](#virtual-axis-s7-1500-s7-1500t)
- [Actual value calculation with the virtual axis (S7-1500, S7-1500T)](#actual-value-calculation-with-the-virtual-axis-s7-1500-s7-1500t)
- [Axis in simulation (S7-1500, S7-1500T)](#axis-in-simulation-s7-1500-s7-1500t)
- [Actual value calculation for the axis in simulation (S7-1500, S7-1500T)](#actual-value-calculation-for-the-axis-in-simulation-s7-1500-s7-1500t)

#### Configure axis type (S7-1500, S7-1500T)

Axes can be configured with different axis types:

- Speed axes are always rotary axes.
- You configure positioning axes and synchronous axes either as rotary or linear axes, depending on the mechanics.

##### Configure axis type

In the "Axis type" area, select the type that matches the mechanics for your axis.

- **Linear axis**

  You can configure the linear axis either with a standard motor or with a linear motor.

  For linear axes, the position of the axis is specified as a linear measure, e.g. millimeters (mm).

  - Linear axis with standard motor

    ![Configure axis type](images/165580512779_DV_resource.Stream@PNG-en-US.png)
  - Linear axis with linear motor

    ![Configure axis type](images/165622256523_DV_resource.Stream@PNG-en-US.png)
- **Rotary axis**

  The rotary axis is always configured with a standard motor.

  For rotary axes, the position of the axis is specified as an angular measure, e.g. degrees (°).

  ![Configure axis type](images/165618167307_DV_resource.Stream@PNG-en-US.png)

  Note the following if you apply the drive values automatically from the Startdrive.

  If the drive in the Startdrive is configured as a linear motor, you have to adapt the configuration of the axis type. Change the axis type to "Linear" or attach a standard motor as drive.

  [Connecting PROFIdrive drives](#connecting-profidrive-drives-s7-1500-s7-1500t)

  [Transferring drive and encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)

#### Configure the type of an external encoder (S7-1500, S7-1500T)

For the "External encoder" technology object, you can configure whether the encoder accepts linear or rotary motions.

Select the appropriate type for your encoder in the "External encoder type" area.

- Linear
- Rotary

#### Units of measure (S7-1500, S7-1500T)

Select the units of measure available for the technology object from the drop-down lists.

Setting or changing the measurement units affects the display of the parameter values and the user program:

- Display of parameter values in the technology data block
- Assignment of parameters in the user program
- Input and display of the position and velocity in the TIA Portal
- Setpoint settings by leading axes in synchronous operation

All information and displays correspond to the selected unit of measure.

When measurement units are changed, the values of individual parameters in the technology object may lie outside the minimum value or maximum value due to the LREAL format. Adapt the values or change the measurement units back.

The set units are displayed in the "<TO>.Units" tag structure of the technology object. The tag structure is described under the tags of the respective technology object.

**Speed**

The supported measurement units for speed (revolutions per time unit) are 1/s, 1/min and 1/h.

**Position and velocity**

The table below shows the supported measurement units for position and velocity:

| Position | Velocity |
| --- | --- |
| nm, μm, mm, m, km | mm/s, mm/min, mm/h, m/s, m/min, m/h, km/min, km/h |
| in, ft, mi | in/s, in/min, ft/s, ft/min, mi/h |
| °, rad | °/s, °/min, rad/s, rad/min |

The acceleration is set accordingly as the position/s² measurement unit.

The jerk is set accordingly as the position/s³ measurement unit.

**Force and torque**

The table below shows the supported measurement units for force and torque:

| Force | Torque |
| --- | --- |
| N, kN | Nm, kNm |
| lbf, ozf, pdl | lbf in, lbf ft, ozf in, ozf ft, pdl in, pdl ft |

**Time**

The measurement unit for time is permanently specified for the following technology objects:

| Technology object | Time |
| --- | --- |
| Speed axis, positioning/synchronous axis, external encoder | s |
| Output cam, cam track, measuring input | ms |

**Mass and moment of inertia**

The table below shows the supported measurement units for mass and moment of inertia.

| Mass | Moment of inertia |
| --- | --- |
| mg, g, kg, t | kgm<sup>2</sup> |
| lb | lbft<sup>2</sup> |

##### Position values with higher resolution

If you select the check box "Use position values with higher resolution" in the configuration of the positioning axis, synchronous axis, external encoder and kinematics technology objects, six decimal places are available in the selected unit, instead of the standard three. Due to the LREAL format, the representable position and angle range in [mm] and [°] is limited to +/- 1.0E09.

The following values are reduced by a factor of 1000 for position values with a higher resolution:

- Displayable position range
- Displayable angular range
- Mechanical gear ratio
- Numerical traversing range with regard to long-term stability
- Dynamic values for velocity, acceleration and deceleration

#### Modulo setting (S7-1500, S7-1500T)

For the positioning axis, synchronous axis and external encoder technology objects, the "Modulo" setting can be activated.

When an axis moves in only one direction, the position value continually increases. To limit the position value to a recurring reference system, you can activate the "Modulo" setting. The [long-term accuracy](#long-term-accuracy-s7-1500-s7-1500t) can also be adhered to with modular axes up to the maximum travel time.

When the "Modulo" setting is activated, the position value of the technology object is mapped onto a recurring modulo range. The modulo range is defined by the start value and the length.

For example, to limit the position value of a rotary axis to a full rotation, the modulo range can be defined with start value = 0° and length = 360°. As a result, the position value is mapped onto the modulo range 0° to 359.999°.

The modulo cycle counters for the position setpoint and the actual position on the positioning axis, synchronous axis and external encoder technology objects indicate the number of modulo revolutions.

##### Modulo cycle counter

If the "Modulo" setting is activated, the modulo cycle counter is activated for the positioning axis, synchronous axis and external encoder technology objects. The modulo cycle counter is displayed at the technology object for the position setpoint and the actual position. The modulo cycle counter counts the modulo revolutions and thus the number of modulo runs at the technology object.

The tag <TO>.ModuloCycle indicates the number of modulo cycles of the setpoint.

The tag <TO>.ActualModuloCycle indicates the number of modulo cycles of the actual value.

The counter values of the modulo cycles change during switch on, restart and homing.

The following applies to an incremental encoder:

| Action | Description |
| --- | --- |
| Switching on the CPU | The modulo cycle counter is set to 0. |
| Reset with "Restart" = TRUE | The modulo cycle counter is set to 0. |
| Active and passive homing with "Mode" = 2, 3, 5, 8, 10 | - If the home position is in the range "Modulo start value ≤ Home position ≤ (Modulo Start value + Modulo length / 2)", the modulo cycle counter is set to 0. - If the home position is in the range "(Modulo start value + Modulo length / 2) < Home position < (Modulo start value + Modulo length)" the modulo cycle is set to -1. |
| Direct homing absolute with "Mode" = 0, 11 | The modulo value is the shortest distance between the current and new position. Depending of the distance, the modulo cycle counter can remain the same, increase by 1 or decrease by 1. |
| Direct homing absolute with "Mode"= 1, 12 |  |

The following applies to an absolute encoder:

| Action | Description |
| --- | --- |
| Switching on the CPU | The modulo cycle counter changes according to the determined modulo length from the absolute value of the encoder and the absolute value offset of an absolute value encoder adjustment, if an absolute value encoder adjustment has taken place. |
| Reset with "Restart" = TRUE | The modulo cycle counter remains unchanged. |
| Absolute encoder adjustment with "Mode" = 7 | The modulo cycle counter is set to 0. |
| Absolute encoder adjustment with "Mode" = 6 | The modulo value is the shortest distance between the current and new position. Depending of the distance, the modulo cycle counter can remain the same, increase by 1 or decrease by 1. |
| Direct homing absolute with "Mode" = 0, 11 |  |
| Direct homing absolute with "Mode"= 1, 12 |  |

##### Enable and configure modulo

Select the "Enable modulo" check box if you want to use a recurring system of units for the axis (e.g. 0° to 360° for an axis of the "rotary" axis type).

- **Modulo start value**

  In this field, define the position at which the modulo range should begin (e.g. 0° for an axis of the "rotary" axis type).
- **Modulo length**

  In this field, define the length of the modulo range (e.g. 360° for an axis of the "rotary" axis type).

#### Virtual axis (S7-1500, S7-1500T)

S7‑1500 Motion Control offers the possibility to configure an axis as a virtual axis. The setpoints are only processed within the controller. A real drive is never controlled in this situation. If the axis is later intended to be operated with a real drive and a real encoder, then use the "Axis in simulation" function.

A virtual axis, for example, is often used as a virtual leading axis in order to generate the setpoints for several real following axes in synchronous operation.

The "Virtual axis" configuration can only be changed by a new download to the CPU in STOP mode (<TO>.VirtualAxis.Mode).

If you have configured an absolute encoder at the virtual axis, you must home the virtual axis after switching on the CPU.

> **Note**
>
> The configured alarm response "Remove enable" is not output to the drive.

The following diagram illustrates the differences between a real axis, an axis in simulation, and a virtual axis.

![Figure](images/172754211339_DV_resource.Stream@PNG-en-US.png)

##### Virtual axis technology version ≥ V7.0:

The behavior of a virtual axis is identical to the behavior of an [axis in simulation](#axis-in-simulation-s7-1500-s7-1500t). The actual values are generated via the control loop and a simplified drive model.

##### Virtual axis technology version ≥ V8.0:

The position and velocity setpoints are directly adopted as actual values with an application cycle delay. The feedback loop and the drive model are not simulated. The dynamic filter is effective.

> **Note**
>
> To maintain compatibility with virtual axes of technology versions ≤ V7.0 for an axis:
>
> 1. Interconnect the axis in simulation (<TO>.Simulation.Mode" = 1).
> 2. Disable the virtual axis (<TO>.VirtualAxisMode = 0)

The following table shows the differences in the behavior of tags for the virtual axis up to technology version V7.0:

| Tag | Description |
| --- | --- |
| <TO>.ActualPosition | Apply the position setpoint ("Positon") after one servo clock cycle |
| <TO>.StatusSensor.Position | Apply the position setpoint ("Positon") after one servo clock cycle |
| <TO>.ActualVelocity | Apply the speed setpoint ("Velocity") after one servo clock cycle |
| <TO>.StatusSensor.Velocity | Apply the speed setpoint ("Velocity") after one servo clock cycle |
| <TO>.ActualAcceleration | Apply the acceleration setpoint ("Accelaration") after one servo clock cycle |
| <TO>.ActualSpeed | 0.0 |
| <TO>.VelocitySetpoint | 0.0 |
| <TO>.StatusServo.ControlDifference | 0.0 |
| <TO>.StatusServo.BallancedPosition | 0.0 |
| <TO>.StatusSensor.Adjusted | 1 |

##### Behavior during operation of the virtual axis

A virtual axis does not output setpoints to the drive and does not read any actual values of the encoder.

Hardware limit switches and home position switches have no effect.

The technology objects measuring input (with signal detection via TM Timer DIDQ or SINAMICS measurement sensing input), output cam and cam track can also be used for virtual axes.

The following table shows the Motion Control instructions with adapted behavior with virtual axes:

| Motion Control instruction | Characteristics in simulation mode |
| --- | --- |
| MC_Power | The axis is enabled immediately without waiting for feedback from the drive. |
| MC_Home | Homing jobs are executed immediately without simulated axis motion. |
| MC_TorqueLimiting | The specified torque is not output to the drive. |

##### Possible applications

- As the leading axis for synchronous applications with real following axes.
- Applicable for software tests

#### Actual value calculation with the virtual axis  (S7-1500, S7-1500T)

The position and velocity setpoints are directly adopted as actual values with an application cycle delay. The feedback loop and the drive model are not simulated. The dynamic filter is active.

The configuration of the control loop, including velocity and torque precontrol, is not taking effect.

Note that the trace recording is delayed as follows, depending on the configured time of recording:

| Displayed tag in the trace | Setpoint position "<TO>.Position" |
| --- | --- |
| Encoder position "<TO>.StatusSensor.Position" | Recording point "MC_Servo": 1 servo clock cycle  Recording point "MC_Interpolator": 2 servo clock cycles |
| Actual position "<TO>.ActualPosition" | Recording point "MC_Servo": 2 servo clock cycles  Recording point "MC_Interpolator": 2 servo clock cycles |

##### Actual value calculation after switching on the CPU

For the encoder type "Absolute" or "Cyclic Absolute," the actual position of the axis is calculated from the following values:

- Fixed simulated incremental actual value of the encoder of 240 increments.
- Configured increments per revolution
- Stored encode offset "<TO>.StatusSensor.AbsEncoderOffset"
- Mechanical configuration

**Example of the rotary positioning axis:**

- All gear ratios = 1
- Increments per revolution = 2048
- Encoder offset = 137­.­812­°

  The actual position after power-on = (240/2048)­° + 137­.­812­° = 180­°

#### Axis in simulation (S7-1500, S7-1500T)

S7‑1500 Motion Control offers the option to move real axes in simulation mode. Speed, positioning and synchronous axes can thus be simulated without a connected drive and encoder in the CPU.

When the simulation mode is activated, the drive and encoder connection does not need to be configured in the axis configuration, for example, if the drive configuration is not yet available at this time. The "Simulation" configuration can be changed during runtime of the user program (<TO>.Simulation.Mode). A valid drive and encoder connection is required when exiting the simulation.

To use a technology object in simulation mode or with SIMATIC S7 PLCSIM, you need to use encoder 1 for closed loop position control of the axis.

> **Note**
>
> The configured alarm response "Remove enable" is not output to the drive.

##### Characteristics in simulation mode

An axis in simulation does not output setpoints to the drive and does not read any actual values of the encoder. The actual values are formed with a time delay from the setpoints.

Hardware limit switches and home position switches have no effect.

The technology objects measuring input (with signal detection via TM Timer DIDQ or SINAMICS measuring input), output cam and cam track can also be used for axes in simulation.

The following table shows the Motion Control instructions with adapted behavior in simulation mode:

| Motion Control instruction | Characteristics in simulation mode |
| --- | --- |
| MC_Power | The axis is enabled immediately without waiting for feedback from the drive. |
| MC_Home | Homing jobs are executed immediately without simulated axis motion. |
| MC_TorqueLimiting | The specified torque is not output to the drive. |

##### Possible applications

- For example, an axis is simulated for programming the machine application and assigned to the configured hardware later for commissioning.
- During commissioning, for example, not all hardware components are available.
- No axis motions should take place during commissioning.

#### Actual value calculation for the axis in simulation (S7-1500, S7-1500T)

The actual value of an axis in simulation is formed from the setpoint taking time delays into account.

You calculate the time delay from actual value to the setpoint (T<sub>t</sub>) as follows:

| Calculation |  |
| --- | --- |
| With precontrol | T<sub>t</sub> = T<sub>ipo</sub> + T<sub>servo</sub> + T<sub>vtc</sub>+ T<sub>addPtc</sub> |
| Without precontrol, without DSC | T<sub>t</sub> = T<sub>ipo</sub> + 1/Kv + T<sub>addPtc</sub> |
| Without precontrol, with DSC for one axis in simulation | T<sub>t</sub> = T<sub>ipo</sub> + T<sub>servo</sub> + 1/Kv + T<sub>addPtc</sub> |

| Symbol | Meaning |
| --- | --- |
| T<sub>t</sub> | Time delay from the actual value to the setpoint |
| T<sub>ipo</sub> | Cycle time of the MC_Interpolator |
| T<sub>servo</sub> | Cycle time of the MC_Servo |
| T<sub>vtc</sub> | Speed control loop substitute time (T<sub>vtc</sub> from "<TO>.DynamicAxisModel.VelocityTimeConstant") |
| T<sub>addPtc</sub> | Additive position control loop equivalent time (T<sub>addPtc</sub> from "<TO>.DynamicAxisModel.AdditionalPositionTimeConstant") |
| kV | Gain factor (Kv from "<TO>.PositionControl.Kv") |

##### Actual value calculation after switching on the CPU

For the encoder type "Absolute" or "Cyclic Absolute," the actual position of the axis is calculated from the following values:

- Fixed simulated incremental actual value of the encoder of 240 increments.
- Configured increments per revolution
- Stored encode offset "<TO>.StatusSensor.AbsEncoderOffset"
- Mechanical configuration

**Example of the rotary positioning axis:**

- All gear ratios = 1
- Increments per revolution = 2048
- Encoder offset = 137­.­812­°

  The actual position after power-on = (240/2048)­° + 137­.­812­° = 180­°

### Drive and encoder connection (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of drive and encoder connection (S7-1500, S7-1500T)](#short-description-of-drive-and-encoder-connection-s7-1500-s7-1500t)
- [Adding and configuring drives (S7-1500, S7-1500T)](#adding-and-configuring-drives-s7-1500-s7-1500t)
- [Configuring PROFIdrive telegrams (S7-1500, S7-1500T)](#configuring-profidrive-telegrams-s7-1500-s7-1500t)
- [Connecting PROFIdrive drives (S7-1500, S7-1500T)](#connecting-profidrive-drives-s7-1500-s7-1500t)
- [Connecting encoders via PROFIdrive (S7-1500, S7-1500T)](#connecting-encoders-via-profidrive-s7-1500-s7-1500t)
- [Transferring drive and encoder parameters automatically (S7-1500, S7-1500T)](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
- [Connecting stepper motors (S7-1500, S7-1500T)](#connecting-stepper-motors-s7-1500-s7-1500t)
- [Connecting drives with analog setpoint interface (S7-1500, S7-1500T)](#connecting-drives-with-analog-setpoint-interface-s7-1500-s7-1500t)
- [Connecting force/torque data via SIEMENS additional telegram 750 (S7-1500, S7-1500T)](#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)
- [Encoder signal output via TM41 (S7-1500, S7-1500T)](#encoder-signal-output-via-tm41-s7-1500-s7-1500t)
- [Tags: Drive and encoder connection (S7-1500, S7-1500T)](#tags-drive-and-encoder-connection-s7-1500-s7-1500t)

#### Short description of drive and encoder connection (S7-1500, S7-1500T)

##### Number of drives and encoders per technology object

The following table shows the number of drives and encoders for the various technology objects.

| Technology object | Number of drives (actuators) | Number of encoders (sensors) |
| --- | --- | --- |
| Speed axis | 1 | 0 |
| Positioning axis, synchronous axis | 1 | 1 (S7-1500)  1 to 4 (S7-1500T) |
| External encoder | 0 | 1 |

##### Supported drive types

You can connect the following drives:

- Drive with an analog setpoint interface
- Drives with PROFIdrive telegram (PROFINET IO or PROFIBUS DP), e.g.

  - SINAMICS
  - SIMATIC MICRO-DRIVE
  - Technology modules
  - Drives from other manufacturers

##### Encoder connection options

The following connection options are available for an encoder:

- Connection to the drive
- Encoder on the technology module, e.g. TM Count 1x24V
- PROFIdrive encoder directly on the PROFIBUS DP/PROFINET IO

The actual encoder value is transmitted exclusively via PROFIdrive telegram.

##### Drive configuration process

Complete the following steps to add and configure a drive.

- [Adding a drive unit](#adding-and-configuring-drives-s7-1500-s7-1500t)

  - SINAMICS Startdrive
  - GSD file
  - SIMATIC technology module
- [Configuration of the PROFIdrive telegram for PROFIdrive drives](#configuring-profidrive-telegrams-s7-1500-s7-1500t)
- Configure communication between drive and CPU in the device configuration

  - [Configure PROFINET IO network](#adding-and-configuring-a-profinet-io-drive-s7-1500-s7-1500t)
  - [Configure PROFIBUS DP network](#adding-and-configuring-a-profibus-dp-drive-s7-1500-s7-1500t)
- Configure data exchange between technology object and PROFIdrive drive

  - [Connect PROFIdrive drive directly](#connecting-profidrive-drive-directly-s7-1500-s7-1500t)
  - [Connect PROFIdrive drive via data block](#connecting-a-profidrive-drive-via-data-block-s7-1500-s7-1500t)
  - [Configure drive parameters manually](#configuring-drive-parameters-manually-s7-1500-s7-1500t)
  - [Transfer drive parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
- [Configure data exchange between technology object and drive with analog setpoint interface](#connecting-drives-with-analog-setpoint-interface-s7-1500-s7-1500t)
- [Connect stepper motors](#connecting-stepper-motors-s7-1500-s7-1500t)

If you want to use a torque pre-control, change the torque limits in the drive from the user program, or evaluate the current actual torque value, you have to connect the additional telegram 750 to the technology object.

- [Connecting force/torque data via SIEMENS additional telegram 750](#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)

##### Encoder configuration process

Add the encoder in the device configuration.

- Add encoder in the device configuration

  - PROFINET-IO encoder
  - Profibus-DP encoder
  - Technology module

Configuring the data exchange between technology object and encoder.

- [Connect ProfiDrive encoder directly](#connecting-the-encoder-directly-s7-1500-s7-1500t)
- [Connect ProfiDrive encoder via data block](#connect-encoder-via-data-block-s7-1500-s7-1500t)
- [Transfer encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
- [Configure encoder parameters manually](#configuring-encoder-parameters-manually-s7-1500-s7-1500t)

[Configure the encoder type](#configuring-the-encoder-type-s7-1500-s7-1500t).

#### Adding and configuring drives (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction (S7-1500, S7-1500T)](#introduction-s7-1500-s7-1500t)
- [Adding and configuring a PROFINET IO drive (S7-1500, S7-1500T)](#adding-and-configuring-a-profinet-io-drive-s7-1500-s7-1500t)
- [Adding and configuring a PROFIBUS DP drive (S7-1500, S7-1500T)](#adding-and-configuring-a-profibus-dp-drive-s7-1500-s7-1500t)

##### Introduction (S7-1500, S7-1500T)

Siemens offers numerous drive systems for various applications.

Depending on the drive, the parameter assignment and implementation in the TIA Portal are different. The application examples provide step-by-step descriptions of how to add and configure the drives.

###### Using Startdrive

If you use a SINAMICS drive with Startdrive, you can find additional information in the hardware catalog in the "Drives & Starter" folder. For more information on connecting via Startdrive, refer to:

- Getting Started SINAMICS S120 in Startdrive:

  [Getting Started SINAMICS S120](https://support.industry.siemens.com/cs/ww/en/view/109747452)
- Application example "Configuring an S120 with Startdrive":

  [Application example SINAMICS S120](https://support.industry.siemens.com/cs/ww/en/view/109743270)
- Application example "Configuring an S210 with Startdrive":

  [Application example SINAMICS S210](https://support.industry.siemens.com/cs/ww/en/view/109750431)

###### Using the GSD file

You can add and configure the SINAMICS S210 using a GSD file.

[Application example SINAMICS S210](https://support.industry.siemens.com/cs/ww/en/view/109750431)

###### Using SINAMICS V90 PN

To add and configure a SINAMICS V90 PN drive in the TIA Portal, you need the Hardware Support Package HSP 0185 (SINAMICS V90 PN).

- Getting Started SINAMICS V90 PN on S7-1500 motion control:

  [Getting Started SINAMICS V90 PN](https://support.industry.siemens.com/cs/ww/en/view/109739497)
- Configuring SINAMICS V90 PN with web server:

  [Application example SINAMICS V90 PN](https://support.industry.siemens.com/cs/ww/en/view/109739053)

###### Using SIMATIC MICRO-DRIVE PDC

To add and configure a SIMATIC MICRO‑DRIVE PDC in the TIA Portal, you need the Hardware Support Package HSP 198.

[Application example SIMATIC MICRO-DRIVE PDC](https://support.industry.siemens.com/cs/ww/us/view/109770395)

###### Using ET 200SP F ‑ TM ServoDrive

To add and configure a ET 200SP F‑TM ServoDrive in the TIA Portal, you need the Hardware Support Package HSP 0311.

[Application example ET 200SP F ‑ TM ServoDrive](https://support.industry.siemens.com/cs/ww/en/view/109780201)

###### Drives compatibility list

In the Siemens Industry Online Support you can find an overview of the drives you can connect with a S7-1500 CPU.

[Compatibility list](https://support.industry.siemens.com/cs/ww/en/view/109750431)

##### Adding and configuring a PROFINET IO drive (S7-1500, S7-1500T)

Adding and configuring a PROFINET IO drive is described below with the example of a SINAMICS S120 drive. Adding and configuring other PROFINET IO drives may differ from the description in certain respects.

###### Requirements

- The SIMATIC S7-1500 device is created in the project.
- The desired drive can be selected in the hardware catalog.

If the drive is not available in the hardware catalog, you must install the drive in the "Options" menu as a device description file (GSD).

###### Adding a drive and telegram in the device configuration

1. Open the device configuration and change to the network view.
2. In the hardware catalog, open the folder "Additional field devices > PROFINET IO > Drives > Siemens AG > SINAMICS".
3. Select the desired drive with the desired version, then drag it to the network view.
4. Assign the drive to the PROFINET interface of the CPU.
5. Open the drive in the device view.
6. Drag a drive object (DO) and a telegram from the hardware catalog and drop it onto a slot of the device overview of the drive.
7. Make sure that the order of the telegrams in the device configuration and in the drive parameter assignment are the same.

   Depending on the version of the SINAMICS S120 drive, select "DO with telegram X", or "DO Servo" and a "Telegram X" for the telegram.

   For more information on suitable telegrams, refer to the section "[Configuring PROFIdrive telegrams](#configuring-profidrive-telegrams-s7-1500-s7-1500t)".

   Repeat step 6 if you want to add another drive and another standard telegram.

###### Interconnect the port of the CPU with the port of the drive

1. Select the topology view of the device configuration.
2. Interconnect the port of the drive with the port of the CPU as in the real setup.  
   To plan your PROFINET topology, please note the PROFINET installation guideline of the PROFIBUS user organization.

###### Activating isochronous mode of the drive in the device configuration

PROFINET drives can always be operated in isochronous mode or clock synchronized mode. Isochronous mode, however, increases the quality of the closed loop position control of the drive and is therefore recommended for drives such as SINAMICS S120.

To control the drive in isochronous mode, follow these steps:

1. Open the device view of the drive.
2. In the properties window, select the tab "PROFINET interface [X150] > Advanced options > Isochronous mode".
3. Select the "Isochronous mode" check box in this tab.

   In the detailed overview, the check box for the telegram must also be selected for isochronous mode.

###### Configure the CPU as the sync master and set isochronous mode

1. Select the device view of the CPU.
2. In the Properties window, select the tab "PROFINET interface [X1] > Advanced options > Real-time settings > Synchronization".
3. Select "Sync master" from the "Synchronization role" drop-down list.
4. Click the "Domain settings" button.
5. Open the "Domain Management > Sync Domains" tab and set the desired "Send clock" (isochronous clock).

###### Configure drive as sync device

1. Select the device view of the drive unit.
2. In the properties dialog, select the tab "PROFINET interface [X150] > Advanced options > Real-time settings > Synchronization".
3. Select "IRT" as the RT class.

###### Select drive in the configuration of the technology object

1. Add a new technology object axis, or open the configuration of an existing axis.
2. Open the configuration "Hardware interface > Drive".
3. Select from the "PROFIdrive" entry in the "Drive type" drop-down list.
4. Select the drive object of the PROFINET drive from the "Drive" list.

###### Checking/configuring the properties of the MC_Servo

1. Open the "Program blocks" folder in the project navigator.
2. Select the "MC_Servo" organization block.
3. Select the "Properties" command in the shortcut menu.
4. Select the "Cycle time" entry in the area navigation.
5. The option "Synchronous to the bus" must be selected in the dialog box.
6. An "PROFINET IO system" must be selected in the "Source of the send clock" drop-down list.
7. The application cycle of "MC_Servo" must correspond to the send clock of the bus or be reduced by an integral factor relative to the send clock of the bus.

###### Result

The PROFINET IO drive is configured in such a way that it can be controlled in isochronous mode in the PROFINET IO network.

The properties of the SINAMICS drive must be configured according to the configuration of the axis with the STARTER software or SINAMICS Startdrive.

###### Check the clock synchronization at the drive.

If the configuration sequence described above is not adhered to during configuration of the axis, and drive-specific errors occur when the project is compiled, the setting for isochronous mode on the drive must be checked.

1. Open the device view of the drive.
2. Select standard telegram in the device overview.
3. Select the properties dialog "General > I/O Addresses".
4. The following settings apply for the input and output addresses:

   - "Isochronous mode" is enabled.
   - "MC_Servo" must be selected for the "Organization block".
   - "PIP OB Servo" must be selected for the "Process image".

##### Adding and configuring a PROFIBUS DP drive (S7-1500, S7-1500T)

Adding and configuring a PROFIBUS drive is described below with the example of a SINAMICS S120 drive. Adding and configuring other PROFIBUS drives may differ from the description in certain respects.

###### Requirements

- The SIMATIC S7-1500 device is created in the project.
- The desired drive can be selected in the hardware catalog.

If the drive is not available in the hardware catalog, you must install the drive in the "Options" menu as a device description file (GSD).

###### Adding a drive and telegram in the device configuration

1. Open the device configuration and change to the network view.
2. In the hardware catalog, open the folder "Additional Field Devices > PROFIBUS DP > Drives > Siemens AG > SINAMICS".
3. Select the folder of the desired drive with the desired version, then drag the drive object to the network view.
4. Assign the drive to the PROFIBUS interface of the CPU.
5. Open the drive in the device view.
6. Drag-and-drop a telegram from the hardware catalog onto a slot in the device overview of the drive.

For more information on suitable telegrams, refer to the section "[Configuring PROFIdrive telegrams](#configuring-profidrive-telegrams-s7-1500-s7-1500t)".

If you want to add another drive and another telegram to the device overview, use the "Axis disconnector" in the hardware catalog.

###### Activating isochronous mode of the drive in the device configuration

PROFIBUS drives can be operated in cyclic mode or isochronous mode. Isochronous mode, however, increases the quality of the position control of the drive.

If you want to control the drive in isochronous mode, follow these steps:

1. Open the device view of the drive.
2. In the properties dialog, select the tab "General > Isochronous Mode".
3. Select the "Synchronize DP slave to constant DP bus cycle time" check box.

###### Setting isochronous mode

1. Select the network view.
2. Select the DP master system.
3. In the properties dialog, select the tab "General > Constant bus cycle time".
4. Select the desired "Constant DP bus cycle times".

###### Select drive in the configuration of the technology object

1. Add a new technology object axis, or open the configuration of an existing axis.
2. Open the configuration "Hardware interface > Drive".
3. Select from the "PROFIdrive" entry in the "Drive type" drop-down list.
4. Select the telegram of the PROFIBUS drive from the "Drive" list.

###### Result

The technology object is connected to the drive and the "MC-Servo" organization block can be checked/configured.

The telegram of the configured drive is assigned to the "PIP OB Servo" process image.

###### Checking/configuring the properties of the MC_Servo

1. Open the "Program blocks" folder in the project navigator.
2. Select the "MC_Servo" organization block.
3. Select the "Properties" command in the shortcut menu.

   The "MC_Servo" dialog opens.
4. Select the "Synchronous to the bus" option under "General > Cycle time".
5. In the "Distributed I/O" drop-down list, select a "PROFIBUS DP-System".

   The application cycle of "MC_Servo" must correspond to the send clock of the bus or be reduced by an integral factor relative to the send clock of the bus.

You can select a drive connected to the CPU via a communications processor/communications module (CP/CM) in the configuration of the technology object. You cannot select the DP master system of the CP/CM as the source clock for MC_Servo.

###### Result

The PROFIBUS DP drive is configured in such a way that it can be controlled in isochronous mode in the PROFIBUS network.

The properties of the SINAMICS drive must be configured according to the configuration of the axis with the STARTER software or SINAMICS Startdrive.

###### Checking isochronous mode on the drive

If the configuration sequence described above is not adhered to during configuration of the axis, and drive-specific error occurs when the project is compiled, isochronous mode can be checked on the drive.

1. Open the device view of the drive.
2. Select the entry of the telegram in the device overview.
3. Select the properties dialog "General > I/O Addresses".
4. The following settings apply for the input and output addresses:

   - "MC_Servo" must be selected for the "Organization block".
   - "PIP OB Servo" must be selected for the "Process image".

#### Configuring PROFIdrive telegrams (S7-1500, S7-1500T)

##### PROFIdrive

PROFIdrive is the standardized drive technology profile for connecting drives and encoders via PROFIBUS DP and PROFINET IO. Drives that support the PROFIdrive profile are connected according to the PROFIdrive standard.

The current PROFIdrive specification is available at the page of the PROFIBUS user organization under "Download" > "Profiles":

https://www.profibus.com

Communication between the controller and drive/encoder is performed using various PROFIdrive telegrams. Each of the telegrams has a standardized structure. You can select the appropriate telegram according to the application. Control words and status words as well as setpoints and actual values are transmitted in the PROFIdrive telegrams.

The PROFIdrive profile likewise supports the "Dynamic Servo Control" (DSC) control concept. DSC uses rapid closed loop position control in the drive. This can be used to solve highly dynamic Motion Control tasks.

##### PROFIdrive telegrams

PROFIdrive telegrams are used to transfer setpoints and actual values, control and status words and other parameters between the controller and drive/encoder.

When a PROFIdrive telegram is used for connection, the drives and encoders are handled and switched on in accordance with the PROFIdrive profile.

The following table shows the possible PROFIdrive telegrams for various technology objects.

| Technology object |  |  | Possible PROFIdrive telegrams |
| --- | --- | --- | --- |
| Speed axis |  |  | - 1, 2 - 3, 4, 5, 6, 102, 103, 105, 106 (actual encoder value is not evaluated) |
| Positioning axis/synchronous axis |  |  |  |
|  | Setpoint and actual encoder value in one drive telegram |  | 3, 4, 5, 6, 102, 103, 105, 106 |
| Setpoint and actual encoder value separately |  |  |  |
|  | Setpoint in drive telegram | 1, 2, 3, 4, 5, 6, 102, 103, 105, 106 |  |
| Actual value from telegram | 81, 83 |  |  |
| External encoder |  |  | 81, 83 |
| Measuring input (Measuring via SINAMICS (central probe)) |  |  | 391, 392, 393 |
| Measuring input at axis module |  |  | Corresponds to measuring via PROFIdrive |

##### Telegram types

The following table shows the supported PROFIdrive telegram types for the assignment of drives and encoders:

| Telegram | Brief description |
| --- | --- |
| **Standard telegrams** |  |
| 1<sup>1)</sup> | - Control word STW1<sup>5)</sup>, status word ZSW1 - Speed setpoint 16 bit (NSET), actual speed value 16 bit (NACT) |
| 2 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) |
| 3 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) |
| 4 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) - Actual encoder value 2 (G2_XIST1, G2_XIST2) |
| 5 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) (motor encoder) - Dynamic Servo Control (DSC)<sup>2)</sup>   - Speed precontrol value   - Position difference (XERR)   - Kv factor gain position control (KPC) |
| 6 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) (motor encoder) - Actual encoder value 2 (G2_XIST1, G2_XIST2) - Dynamic Servo Control (DSC)<sup>2)</sup>   - Speed precontrol value   - Position difference (XERR)   - Kv factor gain position control (KPC) |
| **Siemens telegrams (with torque limiting)** |  |
| 102 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) - Torque limiting |
| 103 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) - Actual encoder value 2 (G2_XIST1, G2_XIST2) - Torque limiting |
| 105 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) (motor encoder) - Dynamic Servo Control (DSC)<sup>2)</sup>   - Speed precontrol value   - Position difference (XERR)   - Kv factor gain position control (KPC) - Torque limiting |
| 106 | - Controls word STW1<sup>5)</sup> and STW2<sup>5)</sup>, status words ZSW1 and ZSW2 - Speed setpoint 32 bit (NSET), actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) (motor encoder) - Actual encoder value 2 (G2_XIST1, G2_XIST2) - Dynamic Servo Control (DSC)<sup>2)</sup>   - Speed precontrol value   - Position difference (XERR)   - Kv factor gain position control (KPC) - Torque limiting |
| **SIEMENS additional telegrams (torque data)** |  |
| 750<sup>3)</sup> | - Additive setpoint torque - High and low torque limits - Torque actual values |
| **SIEMENS telegrams (measuring input)** <sup> 4)</sup> |  |
| 391 | - Control word CU_STW1, status word CU_ZSW1 - Measuring input control word (MT_STW), measuring input status word (MT_ZSW) - Measuring input time stamp of negative (MT1…2_ZS_F) or positive edges (MT1…2_ZS_S) - Digital output 16 bit, digital input 16 bit |
| 392 | - Control word CU_STW1, status word CU_ZSW1 - Measuring input control word (MT_STW), measuring input status word (MT_ZSW) - Measuring input time stamp of negative (MT1…6_ZS_F) or positive edges (MT1…6_ZS_S) - Digital output 16 bit, digital input 16 bit |
| 393 | - Control word CU_STW1, status word CU_ZSW1 - Measuring input control word (MT_STW), measuring input status word (MT_ZSW) - Measuring input time stamp of negative (MT1…8_ZS_F) or positive edges (MT1…8_ZS_S) - Digital output 16 bit, digital input 16 bit - Analog input 16 bit |
| **Standard telegrams - encoder** |  |
| 81 | - Control word STW2_ENC, status word ZSW2_ENC - Actual encoder value 1 (G1_XIST1, G1_XIST2) |
| 83 | - Control word STW2_ENC, status word ZSW2_ENC - Actual speed value 32 bit (NACT) - Actual encoder value 1 (G1_XIST1, G1_XIST2) |
| 1) Isochronous mode is not possible.  2) For use of Dynamic Servo Control (DSC), the motor encoder (first encoder in the telegram) of the drive must be used as the first encoder for the technology object.   3) Can also be used for the telegrams 1, 2, 3, 4, 5, 6, 102, 103, 105, 106  4) When using SINAMICS drives (measuring using SINAMICS measuring input)  5) STW1 and STW2: Bits not used by the technology object can be controlled via the user program with the Motion Control instruction "MC_SetAxisSTW". |  |

The following table shows PROFIdrive telegrams that are not supported but are modified by the MC_Servo:

| Telegram | Brief description |
| --- | --- |
| **SIEMENS telegrams** |  |
| 390 | Control word CU_STW1, status word CU_ZSW1 |
| 394 | Control word CU_STW1, status word CU_ZSW1 |
| 395 | Control word CU_STW1, status word CU_ZSW1 |

The exact content of the telegrams can be found in the "[SINAMICS S120/S150](https://support.industry.siemens.com/cs/ww/en/view/109822659)" list manual

#### Connecting PROFIdrive drives (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Connecting PROFIdrive drive directly (S7-1500, S7-1500T)](#connecting-profidrive-drive-directly-s7-1500-s7-1500t)
- [Connecting a PROFIdrive drive via data block (S7-1500, S7-1500T)](#connecting-a-profidrive-drive-via-data-block-s7-1500-s7-1500t)
- [Connect drive/encoder via data block (S7-1500, S7-1500T)](#connect-driveencoder-via-data-block-s7-1500-s7-1500t)
- [Configuring drive parameters manually (S7-1500, S7-1500T)](#configuring-drive-parameters-manually-s7-1500-s7-1500t)

##### Connecting PROFIdrive drive directly (S7-1500, S7-1500T)

In the "Drive" field, select an already configured PROFIdrive drive/slot. A suitable PROFIdrive telegram must be configured so that a drive is displayed.

![Figure](images/165740171659_DV_resource.Stream@PNG-en-US.png)

When you have selected a drive, you can use the "Device configuration" button to navigate directly to the device view of the PROFIdrive, e.g. in Startdrive. Use the "Drive configuration" button to navigate to the parameter assignment of the PROFIdrive drive in Startdrive.

> **Note**
>
> **Option "Show all modules"**
>
> If a PROFIdrive drive that has already been configured is not available for selection, use the option "Show all modules" to display all reachable modules.
>
> When you select the option "Show all modules", only the address range for each of the displayed modules is checked. If the address range of the module is large enough for the selected PROFIdrive telegram, you can select the module. For this reason, make sure that you select a PROFIdrive drive.

##### Connecting a PROFIdrive drive via data block (S7-1500, S7-1500T)

Use the connection via data block if you want to influence or evaluate telegram contents in the user program for process-specific reasons.

![Figure](images/165740665739_DV_resource.Stream@PNG-en-US.png)

###### Principle of data connection via data block

Generally, at the start of closed-loop position control of the axis (by MC_Servo), the input area of the drive or encoder telegram is read.

At the end of closed loop position control, the output area of the drive or encoder telegram is written.

To influence or evaluate process-related telegram contents, a data interface can be connected via a data block before and after the position control.

- The input area of the telegram can be edited using the MC_PreServo organization block. The MC_PreServo is called before the MC_Servo.
- The output area of the telegram can be edited using the MC_PostServo organization block. The MC_PostServo is called after the MC_Servo.

The data block must be created by the user and contain a data structure of data type "PD_TELx" for the data connection. Here, "x" stands for the telegram number of the drive or encoder configured in the device configuration.

The organization blocks MC_PreServo and MC_PostServo can be programmed by the user and must be added with the command "Add new block". The connection to the I/O via telegram must be programmed in this organization block. When you use DSC, you have to edit the signs of life in the telegrams in MC_PreServo and MC_PostServo yourself according to the PROFIdrive standard.

---

**See also**

[Organization blocks for Motion Control (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#organization-blocks-for-motion-control-s7-1500-s7-1500t)

##### Connect drive/encoder via data block (S7-1500, S7-1500T)

###### Creating the data block for data connection

1. Create a new data block of type "Global DB".
2. Select the data block in the project tree and select "Properties" from the shortcut menu.
3. Disable the following attributes under Attributes and accept the change with "OK":

   - "Only store in load memory"
   - "Data block write-protected in the device"
   - "Optimized block access" for technology version < V4.0
4. Open the data block in the block editor.
5. Create a new tag on "Add" in the block editor.
6. For the new tag, enter "PD_TELx" completely in the "Data type" column. The "x" stands for the telegram number. Example: "PD_TEL3" for standard telegram 3   
   You have created a tag structure of the type "PD_TELx". This tag structure contains the "Input" tag structure for the input area of the telegram and the "Output" tag structure for the output area of the telegram.

   > **Note**
   >
   > "Input" and "Output" relate to the view of the technology object. For example, the input area contains the actual values of the drive and the output area contains the setpoints for the drive.
   >
   > For the data connection via a data block, "Input" and "Output" must always be in of the "PD_TELx" tag structure. Do not use standalone tag structures for "Input" and "Output", such as "PD_TEL3_IN".
   >
   > The data block may contain the data structures of multiple axes and encoders and other contents.

###### Configuring data connection via a data block

1. Open the configuration window "Hardware interface > Drive" or "Hardware interface > Encoder".
2. Select the entry "Data block" from the "Data block" drop-down list.
3. In the "Data block" field, select the previously created data block.   
   Open this data block and select the tag name defined for the drive and encoder.

> **Note**
>
> As of TIA Portal V17, you can connect tag structures of the "PD TELx" data type that are defined in arrays (Array [0..x] of "PD_TELx"), PLC data types or structures within a data block.

###### Programming MC_PreServo and MC_PostServo

- Edit the tag structure for the input area "Input" in the MC_PreServo.
- Edit the tag structure for the output area "Output" in the MC_PostServo.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Machine damage**  Improper manipulation of drive and encoder telegrams may result in unwanted drive motions.  Check your user  program for consistency in the drive and encoder connection. |  |

An application example for the use of MC_PreServo and MC_PostServo is available on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109741575).

###### Configuration of the communication times T<sub>i</sub>, T<sub>o,</sub> T<sub>DC</sub>

When calculating the following error, the transmission times of the setpoint to the drive and of the actual position value to the controller are deducted. The transmission times result from the following communication times:

- T<sub>i</sub>: Time to import process values
- T<sub>o</sub>: Time to export process values
- T<sub>DC</sub>: Send clock of the PROFINET interface or PROFIBUS send clock

The following error is calculated from the delayed position setpoint by the communication times T<sub>i</sub> + T<sub>o</sub> + T<sub>DC</sub> and the cycle time of the MC_Servo T<sub>Servo</sub> minus the actual position in the controller.

Unlike with direct drive or encoder connection, the communication times are not automatically adapted by the technology object with the connection via data block; by default, the communication times are preset to 0.0 s. For the correct calculation of the real following error "<TO>.StatusPositioning.FollowingError" and the system deviation at the position controller "<TO>.StatusServo.ControlDifference", you configure the communication times T<sub>i</sub>, T<sub>o</sub>, T<sub>DC</sub> manually.

You can find a description of the communication times in the PROFINET with STEP 7 function manual on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

**Procedure**

1. Read the T<sub>i</sub>, T<sub>o</sub>, and T<sub>DC</sub> (send clock) from the device configuration of the drive or encoder. You can find the values in the menu "PROFINET interface > Advanced settings > Isochronous mode".
2. Define the read times as tags of the data type "LREAL" in a data block.

   > **Note**
   >
   > Enter the time in seconds (s) in the data block. In the device configuration, times are entered in milliseconds (ms). A time Ti of 0.125 ms corresponds to 0.000125 s.
3. Call the "MC_WriteParameter" instruction with the following parameter assignment for "MC_WriteParameter.ParameterNumber". For the input parameter "Value", assign the defined tag for T<sub>i</sub> with the corresponding time.

   | Communication time | MC_WriteParameter.ParameterNumber |
   | --- | --- |
   | T<sub>i</sub> | 1010 |
   | T<sub>o</sub> | 1011 |
   | T<sub>DC</sub> | 1012 |
4. Assign the associated technology object at the "Axis" input parameter.
5. Start the job with a positive edge at the "Execute" input parameter.

   The output parameter "Done" signals that the change has been applied.

   Bit 3 of the tag "<TO>.StatusWord" (OnlineStartValueChanged) indicates that a restart of the technology object is required to effectively apply the values.
6. Repeat steps 3. to 5. for the communication times T<sub>o</sub> and T<sub>DC</sub>.
7. To apply the change of the communication times, restart the technology object with the instruction "MC_Reset" with "Restart" = TRUE.

**Result**

The communication times for T<sub>i</sub>, T<sub>o</sub> and T<sub>DC</sub> are not taken into account by the technology object when calculating the following error.

> **Note**
>
> When you connect the technology object directly to the drive, the technology object automatically adapts the communication times. Do not configure the communication times via the user program in this case.

The communication times are retained with a "RUN → STOP → RUN" transition of the CPU or in case of another restart of the technology object.

Note that the communication times are reset to 0.0 s in the following cases:

- Download of the technology object
- POWER OFF → POWER ON
- Memory reset

In this case, configure the communication times again.

##### Configuring drive parameters manually (S7-1500, S7-1500T)

If the connected drive does not allow the drive parameters to be applied automatically, configure the drive parameters manually. You can find the configured values in the manufacturer's information or in the drive commissioning tool.

[Transferring drive and encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)

###### Standard motor

- **Reference speed**Configure the reference speed of the drive in this field according to the manufacturer's specifications. The specification of the drive speed is a percentage of the reference speed in the range -200% to 200%.
- **Maximum speed**Configure the maximum speed of the drive in this field.
- **Reference torque**In this field, configure the reference torque of the drive according to its configuration.  
  The reference torque is required for the force/torque reduction, which is supported with telegram 10x.

###### Linear motor

- **Reference velocity**Configure the reference velocity of the drive in accordance with the manufacturer's specifications in this field. The specification of the drive velocity is a percentage of the reference velocity in the range -200% to 200%.
- **Maximum velocity**Configure the maximum velocity of the drive in this field.
- **Reference force**In this field, configure the reference force of the drive according to its configuration.  
  The reference force is required for the force/torque reduction, which is supported with telegram 10x.

#### Connecting encoders via PROFIdrive (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction to encoder connection (S7-1500, S7-1500T)](#introduction-to-encoder-connection-s7-1500-s7-1500t)
- [Connecting the encoder directly (S7-1500, S7-1500T)](#connecting-the-encoder-directly-s7-1500-s7-1500t)
- [Connect encoder via data block (S7-1500, S7-1500T)](#connect-encoder-via-data-block-s7-1500-s7-1500t)
- [Configuring the encoder type (S7-1500, S7-1500T)](#configuring-the-encoder-type-s7-1500-s7-1500t)
- [Configuring encoder parameters manually (S7-1500, S7-1500T)](#configuring-encoder-parameters-manually-s7-1500-s7-1500t)
- [Using multiple encoders (S7-1500T)](#using-multiple-encoders-s7-1500t)
- [Calculate actual velocity from actual speed NIST_B from PROFIdrive telegram (S7-1500, S7-1500T)](#calculate-actual-velocity-from-actual-speed-nist_b-from-profidrive-telegram-s7-1500-s7-1500t)

##### Introduction to encoder connection (S7-1500, S7-1500T)

When using a PROFIdrive drive telegram with encoder data for the positioning axis or synchronous axis technology object, e.g. telegram 3, the encoder from the PROFIdrive telegram is automatically connected as the first encoder.

With telegram 6 or 106, the first two encoders are automatically connected (only S7-1500T).

You must connect the encoder separately to the drive in the following applications:

- Drive and encoder data in two separate PROFIdrive telegrams (drive connection via PROFIdrive telegram 1 and encoder connection via PROFIdrive telegram 81/83)
- Connection to the technology object external encoder
- Connection as a second, third or fourth encoder on the positioning axis or synchronous axis technology object (S7-1500T)
- Connection as the first encoder, instead of the automatically connected encoder from the PROFIdrive drive telegram.

##### Connecting the encoder directly (S7-1500, S7-1500T)

In the "Encoder" field, select an already configured encoder or its PROFIdrive telegram.

###### Connection to the drive (not with analog drive connection)

The encoder is configured via the configuration of the PROFIdrive drive. The drive evaluates the encoder signals and sends them to the controller in the PROFIdrive telegram.

###### Encoder on technology module (TM)

Select a previously configured technology module and the channel to be used. Only technology modules set to the "Position input for Motion Control" mode are displayed for selection.

If no technology module is available for selection, change to the device configuration and add a technology module. If you have selected a technology module, you can access the configuration of the technology module using the "Device configuration" button.

You can operate the technology module centrally on an S7-1500 CPU or decentrally on a distributed I/O. During central operation in the CPU isochrone mode is possible as of firmware version 2.8.1.

You can identify the technology modules suitable for position detection for Motion Control in the documentation for the technology module and the catalog data.

With the compact CPUs (e.g. CPU 1512C-1 PN) you can use the high-speed counters (HSC) for position detection.

###### **PROFIdrive** **encoder on** **PROFINET** **/** **PROFIBUS** **(** **PROFIdrive** **)**

In the "PROFIdrive encoder" field, select a configured encoder on PROFINET/PROFIBUS. When you have selected an encoder, you can configure the encoder using the "Device configuration" button.

Switch to the device configuration in the network view, and add an encoder, in the event that no encoder can be selected.

> **Note**
>
> **Option "Show all modules"**
>
> If a PROFIdrive that has already been configured is not available for selection, use the option "Show all modules" to display all reachable modules.
>
> When you select the option "Show all modules", only the address range for each of the displayed modules is checked. If the address range of the module is large enough for the selected PROFIdrive telegram, you can select the module. For this reason, make sure that you select a PROFIdrive encoder.

##### Connect encoder via data block (S7-1500, S7-1500T)

If you have selected "Data block" under the data connection, select in the "Data block" field a previously created data block which contains a tag structure of the data type "PD_TELx" ("x" stands for the telegram number to be used).

The procedure is described in the section "[Connecting a PROFIdrive drive via data block](#connecting-a-profidrive-drive-via-data-block-s7-1500-s7-1500t)".

##### Configuring the encoder type (S7-1500, S7-1500T)

For position-controlled motion and positioning, the controller must know the actual position value.

The actual position value is provided by a PROFIdrive telegram.

The actual values are represented as incremental or absolute values in the PROFIdrive telegram. The actual values are normalized in the controller to the technological unit taking into account the configuration of the mechanics. The reference to a physical position of the axis or external encoder is established by homing.

The controller supports the following types of actual values (encoder types):

- Incremental actual value
- Absolute actual value with the setting absolute (measuring range > traversing range of the axis)
- Absolute actual value with the setting cyclic absolute (measuring range < traversing range of axis)

###### Configuration of the encoder type

Make the setting of the encoder type depending on the encoder used and the measuring range of the encoder. The following table contains the selection criteria.

| Encoder type | Actual value type | Explanation | Selection |
| --- | --- | --- | --- |
| Incremental | The actual value in the PROFIdrive telegram is based on an incremental value. | After POWER ON, position zero is displayed. A transition of the CPU to RUN mode starts the actual value update. The actual value is then also updated in CPU STOP mode. The relationship between the technology object and the mechanical position must be re-established by means of homing. | Select this encoder type when using an incremental encoder. |
| Absolute | The actual value in the PROFIdrive telegram is based on an absolute value. After POWER ON, position zero is displayed. The first transition of the CPU to RUN mode starts the actual value update. The actual value is then also updated in CPU STOP mode. The supplied absolute value is assigned to the associated mechanical axis position by means of the absolute encoder adjustment. The absolute encoder adjustment must be performed once. The absolute value offset is retentively saved beyond the switching on/off of the controller. | The axis position results directly from the current actual encoder value. The traversing range must be within an encoder measuring range. This means that the zero crossing of the encoder must not be located in the traversing range. When the controller is switched on, the axis position is determined from the absolute actual encoder value. | An absolute encoder is used and the measuring range of the encoder is smaller than the traversing range of the axis.  If you cannot ensure that there is no encoder zero crossing in the traversing range, use the "Cyclic absolute" setting. |
| Cyclic absolute | The encoder supplies an absolute value within its measuring range. The controller includes the traversed measuring ranges and thus determines the correct axis position beyond the measuring range. When the controller is switched off, the traversed measuring ranges are saved in the retentive memory area of the controller. At the next power-on, the saved traversed measuring ranges are taken into account in the calculation of the actual position value. | An absolute encoder is used and the measuring range of the encoder is smaller than the traversing range of the axis.  Recommended settings for absolute actual values: The "Cyclic absolute" encoder type is recommended. With this setting, the position of the zero crossing of the encoder is automatically taken into account by the technology object. |  |

The following graphic illustrates three different encoder measurement ranges and the possible configuration of the encoder type.

![Configuration of the encoder type](images/169259343243_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Maximum traversing range |
| ② | Zero crossing |
| ③ | Zero crossing outside the maximum traversing range  Encoder type: "Absolute" or "Cyclically absolute" |
| ④ | Zero crossing within the maximum traversing range  Encoder type: "Cyclic absolute" |
| ⑤ | Zero crossing multiple times within the maximum traversing range  Encoder type: "Cyclic absolute" |

##### Configuring encoder parameters manually (S7-1500, S7-1500T)

If the connected encoder does not allow the encoder parameters to be applied automatically, configure the encoder parameters manually. You can find the configured values in the manufacturer's information or in the drive commissioning tool.

[Transferring drive and encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)

###### Encoder parameters for a rotary measuring system

| Parameters | Drive parameters in SINAMICS | Encoder type |  |  |
| --- | --- | --- | --- | --- |
| Incremental | Absolute | Cyclic absolute |  |  |
| Increments per revolution | p979[2] encoder 1  p979[12] encoder 2 | x | x | x |
| Number of revolutions | p979 [5] encoder 1  p979[15] encoder 2 | - | x | x |
| Bits for fine resolution in the incremental actual value (Gx_XIST1) | p979[3] encoder 1  p979[13] encoder 2 | x | x | x |
| Bits for fine resolution in the absolute actual value (Gx_XIST2) | p979[4] encoder 1  p979[14] encoder 2 | - | x | x |
| Encoder reference speed | p2000 | x | x | x |

###### Encoder parameters for linear measuring system

| Parameters | Drive parameters in SINAMICS | Encoder type |  |  |
| --- | --- | --- | --- | --- |
| Incremental | Absolute | Cyclic absolute |  |  |
| Distance between two increments | p979[2] encoder 1  p979[12] encoder 2 | x | x | x |
| Bits for fine resolution in the incremental actual value (Gx_XIST1) | p979[3] encoder 1  p979[13] encoder 2 | x | x | x |
| Bits for fine resolution in the absolute actual value (Gx_XIST2) | p979[4] encoder 1  p979[14] encoder 2 | - | x | x |
| Encoder reference velocity | p2000 | x | x | x |

###### Evaluation of incremental actual value Gx_XIST1 with absolute encoders

In its default setting "<TO>.Sensor[1..4].Parameter.BehaviorGx_XIST1" = 1, the technology object assumes that the incremental actual value "Gx_XIST1" in the PROFIdrive telegram is supplied as an incremental counter value with a data width of 32 bits by the encoder or by the encoder module. In the "Gx_XIST1", this corresponds to a value between 0 and 4.294.967.295 (32 bits). The technology object expects overflow at these limits.

If "Gx_XIST1" is transmitted in the PROFIdrive telegram with a data width of less than 32 bits, configure "<TO>.Sensor[1..4].Parameter.BehaviorGx_XIST1" with 0. In this configuration, the technology object does not expect an incremental counter value with 32 bits, but evaluates only the data width according to the parameter assignment of the encoder at the technology object in "Gx_XIST1". The overflow in "Gx_XIST1" is also expected based on this parameter assignment. You can diagnose whether the data width of the incremental counter value is less than 32 bits with a trace of "Gx_XIST1" from the PROFIdrive telegram. If "Gx_XIST1" overflows back to 0 before it reaches 4,294,967,295, then the data width is less.

##### Using multiple encoders (S7-1500T)

The S7-1500T technology CPU offers the option of using up to 4 encoder or measuring systems per positioning axis and synchronous axis as the actual position for the closed loop position control

Only one encoder at a time is active for closed loop position control. You can switch between the 4 encoder or measuring systems.

However, the actual values of all configured encoders can be evaluated in the user program.

This opens up the following possible application areas, for example:

- Use of additional machine encoders (besides the motor encoder), e.g. as direct measuring systems for more accurate detection of actual positions of machining processes.
- Use of alternative encoder systems following a tool change in a flexible manufacturing process.

You configure the encoders in the axis configuration. You control the switchover of the encoders in the user program with the Motion Control instruction "MC_SetSensor".

###### Configuring an axis with multiple encoders

Note the following configuration windows when using multiple encoders:

- In the configuration window "Hardware interface > Encoder", configure which alternative encoders are to be used and their corresponding encoder type (incremental, absolute or cyclic absolute).  
  All encoders marked as used supply continually updated actual values to the closed loop position control regardless of their use.
- In the configuration window "Hardware interface > Encoder", configure an encoder as "Encoder at power-up". This is necessary because an encoder must always be assigned to the positioning axis and synchronous axis. To use Dynamic Servo Control (DSC), you must configure the motor encoder of the drive as the first encoder on the axis. The motor encoder is always the first encoder in the telegram.
- In the configuration window "Hardware interface > Data exchange with encoder", configure additional encoder details and the telegram that is to be used to connect the encoders. The configuration must be performed for each encoder used.  
  Each encoder to be used or each measuring system may differ with regard to its encoder mounting type.
- In the configuration window "Extended parameters > Mechanics", configure the encoder mounting type and any gear parameters. The configuration must be performed for each encoder used.
- The axis can be homed with any configured encoder. In the configuration window "Extended parameters > Homing", configure the parameters for active and passive homing. The configuration can be performed for each encoder used.  
  When the axis is homed with an encoder, the axis is homed and retains the "homed" status following encoder switchover.

###### Encoder switchover in the user program

For closed loop position control of the positioning and synchronous axes, an encoder must always be active. Individual encoders may fail as long as they are not involved in closed loop position control.

With the Motion Control instruction "MC_SetSensor", you switch over the encoder for closed loop position control of the axis.

The switchover can occur during an active motion job or at a standstill. The axis does not have to be enabled.

A switchover during an active homing or restart job is not possible.

> **Note**
>
> **Homing**
>
> Homing with the Motion Control instruction "MC_Home" or the axis control panel is always performed with the encoder involved in closed loop position control.
>
> The homing status of the axis is not changed following an encoder switchover.
>
> **Simulation**
>
> When the axis is simulated, all encoders configured as "used" are simulated.

"Mode" = 2 and 3 can be used to prepare a switchover.

###### Position adjustment mode

Following the switchover to an alternative encoder or encoder system, you can select what happens if the actual positions of the encoders are different.

You define how to deal with the difference in the actual positions of the encoders using input parameter "Mode" of the Motion Control instruction "MC_SetSensor".

- **Switch over encoder and transfer actual position to the encoder to be switched ("**
  **Mode**
  **" = 0)**

  With this encoder switchover, step changes in the actual position are prevented. Bumpless switchover of the encoders is possible.
- **Switch over sensor without transferring the actual position ("**
  **Mode**
  **" = 1)**

  Following a switchover to an encoder without adjustment, a step change of the actual position may occur. This can be desirable if the new encoder is intended to compensate for possible mechanical influences (such as slip) in the positioning.

  The position difference is not implemented immediately but rather after a delay using time constant "<TO>.PositionControl.SmoothingTimeByChangeDifference" in order to prevent step changes in the actual position with active closed loop position control.
- **Transfer actual position ("**
  **Mode**
  **" = 2)**

  The actual position of the axis is transferred to the encoder specified in the "Sensor" parameter.
- **Transfer actual position of the reference encoder ("**
  **Mode**
  **" = 3)**

  The actual position of the "Reference encoder" ("ReferenceSensor" parameter) is transferred to the encoder specified in the "Sensor" parameter.

##### Calculate actual velocity from actual speed NIST_B from PROFIdrive telegram (S7-1500, S7-1500T)

If you use an encoder with a low resolution, configure the following calculation methods:

- For positioning axis and synchronous axis technology objects: Calculate actual velocity from actual speed "NIST_B" from telegram
- For technology object external encoder: Calculate actual velocity from actual speed "NIST_B" of encoder telegram 83

For encoders with low resolution, the calculation of the actual velocity from the actual speed "NIST_B" in the PROFIdrive telegram is more precise than the standard calculation from the change in the actual position in the servo cycle.

| Encoder resolution | Recommended configuration | Explanation |
| --- | --- | --- |
| High | <TO>.Sensor[1..4].ActualVelocityMode = 0 | Calculation of the actual velocity from the differentiation of the actual position |
| Low | <TO>.Sensor[1..4].ActualVelocityMode = 1 | Calculation of the actual velocity from the actual speed "NIST_B" from the PROFIdrive telegram |

The calculation of the actual velocity is relevant for the following Motion Control functions:

- Actual value extrapolation for actual value coupling in synchronous operation (S7-1500T)
- Output cam with output cam reference "Actual value"
- Transition from follow-up mode to position-controlled mode
- Calculation of the emergency stop ramp
- Standstill detection

> **Note**
>
> The calculation method of the actual velocity has no influence on the position control and the motion control of the technology object.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Use of drive telegrams with two encoders**  The standard telegrams 4 and 6 and the Siemens telegram 106 support up to two encoders.  Note that the actual speed "NIST_B" is only transferred for encoder 1 in the drive telegram.  If you have connected the second encoder of the telegram for encoder 2 in the technology object and for this encoder "Calculate actual velocity from actual speed NIST_B from PROFIdrive telegram" (<TO>.Sensor.Sensor (2).ActualVelocityMode = PROFIDRIVE_NIST), then the first encoder of the telegram returns the actual speed and the second encoder of the telegram returns the actual position. |  |

If you calculate actual velocity from actual speed "NIST_B" of encoder telegram 83, you must configure the following reference values:

- With rotary measuring system: Encoder reference speed "<TO>.Sensor[1..4].Parameter.ReferenceSpeed"
- With linear measuring system: Encoder reference velocity "<TO>.Sensor[1..4].Parameter.ReferenceVelocity"

When calculating the actual velocity from the actual speed "NIST_B" from drive telegrams, the reference value from the tag "<TO>.Actor.DriveParameter.ReferenceSpeed" or "<TO>.Actor.DriveParameter.ReferenceVelocity" is automatically used. You do not need to configure any additional reference values in "<TO>.Sensor[1..4]".

#### Transferring drive and encoder parameters automatically (S7-1500, S7-1500T)

Identical reference values for the drive and encoder connections must be set in the controller and in the drive and encoder for the operation.

The speed setpoint NSET and the actual speed value NACT are transferred in the PROFIdrive telegram as a percentage of the reference speed. The reference value for the speed must be set identically in the controller and in the drive.

The resolution of the actual value in the PROFIdrive telegram must likewise be set identically in the controller and in the drive and encoder modules

##### Automatic transfer of parameters during runtime (online)

The drive and encoder parameters can be automatically applied in the CPU for the following drives and encoders.

- SINAMICS drives (see "[compatibility list](https://support.industry.siemens.com/cs/ww/en/view/109750431)")
- Certified PROFINET encoder as of encoder profile 4.1

The corresponding parameters are transferred after the (re-)initialization of the technology object or (re)start of the drive and the CPU. Changes in the drive configuration are transferred after restart of the drive or technology object.

Successful transfer of the parameters can be checked in the controller with the value of the tags "<TO>.StatusDrive.AdaptionState" = 2 and "<TO>.StatusSensor[1..4].AdaptionState" = 2 of the technology object.

##### Automatic transfer of parameters during configuration (offline)

If you have completed the drive configuration, e.g. with SINAMICS Startdrive, you can transfer the drive or encoder parameters offline in the technology object. The parameters are automatically transferred to the CPU before the download.

##### Parameters

The settings for automatic transfer can be found in the TIA Portal under "Technology object > Configuration> Hardware interface > Data exchange with the drive/encoder".

The drive and encoder settings are made in the configuration or the respective hardware.

The following table compares the settings in the TIA Portal, in the controller and the corresponding drive/encoder parameters:

| Setting in the TIA Portal | Controller tag in the technology data block |  | Drive parameter | Automatic transfer |
| --- | --- | --- | --- | --- |
| **Drive** |  |  |  |  |
| Telegram number | Telegram input address  <TO>.Actor.Interface.AddressIn |  | Telegram number P922 | - |
| Telegram output address  <TO>.Actor.Interface.AddressOut |  |  |  |  |
| Motor type | <TO>.Actor.MotorType |  | Servo drive with "Linear motor" bit r108.12 | ✓ |
| 0 | Standard motor |  |  |  |
| 1 | Linear motor |  |  |  |
| Reference speed in [rpm] (standard motor) | <TO>.Actor.DriveParameter.ReferenceSpeed |  | (SINAMICS drives: P2000) | ✓ |
| Maximum speed of motor in [1/min] (standard motor) | <TO>.Actor.DriveParameter.MaxSpeed |  | (SINAMICS drives: P1082) | ✓ |
| Reference torque in [NM] (standard motor) | <TO>.Actor.DriveParameter.ReferenceTorque |  | (SINAMICS drives: P2003) | ✓ |
| Reference velocity in [m/min] (linear motor) | <TO>.Actor.LinearMotorDriveParameter.ReferenceVelocity |  | (SINAMICS drives: P2000) | ✓ |
| Maximum velocity in [m/min) (linear motor) | <TO>.Actor.LinearMotorDriveParameter.MaxVelocity |  | (SINAMICS drives: P1082) | ✓ |
| Reference force in [N] (linear motor) | <TO>.Actor.LinearMotorDriveParameter.ReferenceForce |  | (SINAMICS drives: P2003) | ✓ |
| **Encoder** |  |  |  |  |
| Telegram | <TO>.Sensor[1..4].Interface.AddressIn |  | P922 | - |
| <TO>.Sensor[1..4].Interface.AddressOut |  |  |  |  |
| Encoder type | <TO>.Sensor[1..4].Type |  | P979[5] Encoder 1  P979[15] Encoder 2 | - |
| 0 | Incremental |  |  |  |
| 1 | Absolute |  |  |  |
| 2 | Cyclic absolute |  |  |  |
| Measuring system | <TO>.Sensor[1..4].System |  | P979[1] Bit0 Encoder 1  P979[11] Bit0 Encoder 2 | ✓ |
| 0 | Linear |  |  |  |
| 1 | Rotary |  |  |  |
| Resolution (linear encoder)  The grid spacing is specified on the nameplate of the encoder as a separation distance of the marks on the linear measuring system. | <TO>.Sensor[1..4].Parameter.Resolution |  | P979[2] Encoder 1  P979[12] Encoder 2 | ✓ |
| Increments per revolution (rotary encoder) | <TO>.Sensor[1..4].Parameter.StepsPerRevolution |  | P979[2] Encoder 1  P979[12] Encoder 2 | ✓ |
| Number of bits for fine resolution XIST1 (cyclic actual encoder value, linear or rotary encoder) | <TO>.Sensor[1..4].Parameter.FineResolutionXist1 |  | P979[3] Encoder 1  P979[13] Encoder 2 | ✓ |
| Number of bits for fine resolution XIST2 (absolute encoder value, linear or rotary encoder) | <TO>.Sensor[1..4].Parameter.FineResolutionXist2 |  | P979[4] Encoder 1  P979[14] Encoder 2 | ✓ |
| Distinguishable encoder revolutions (rotary absolute encoder) | <TO>.Sensor[1..4].Parameter.DeterminableRevolutions |  | P979[5] Encoder 1  P979[15] Encoder 2 | ✓ |
| Encoder reference speed (rotary measuring system) | <TO>.Sensor[1..4].Parameter.ReferenceSpeed |  | P2000 | ✓ |
| Encoder reference velocity (linear measuring system) | <TO>.Sensor[1..4].Parameter.ReferenceVelocity |  | P2000 | ✓ |

#### Connecting stepper motors (S7-1500, S7-1500T)

Drives with a stepper motor interface are connected using telegram 3 and with the help of PTO (Pulse Train Output) pulse generators.

Use the following modules to control the stepper motors:

- TM PTO 2x24V / TM PTO 4
- SIMATIC MICRO‑Drive F‑TM StepDrive S

For functional support of stepper motor operation, quantization of the control deviation can be set.

Through the specification of a quantization, a range around the target position is defined in which no correction of the actual position is to be made. This prevents a possible oscillation of the stepper motor around the target position. Two types of quantization can be set:

- Quantization of the control deviation corresponding to the encoder resolution

  ("<TO>.PositionControl.­Control­Difference­Quantization.­Mode" = 1)

  This prevents oscillation of the motor in standstill between two increment values, for example. This mode is especially helpful when using multiple encoders. With this setting, the quantization is adapted appropriately at an encoder switchover. This mode is helpful for stepper motors with encoders in which the resolution of the encoder is lower than the step size of the stepper motor.
- Direct specification of a value for quantization of the control deviation.

  ("<TO>.PositionControl.­Control­Difference­Quantization.­Mode" = 2, value setting in "<TO>.PositionControl.­Control­Difference­Quantization.­Value")

  This mode is helpful for stepper motors with encoders in which the resolution of the encoder is greater than the step size of the stepper motor.

#### Connecting drives with analog setpoint interface (S7-1500, S7-1500T)

Drives with analog setpoint interfaces are connected using an analog output and an optional enable signal. The speed setpoint is specified via an analog output signal (e.g. from -10 V to +10 V) from the CPU.

##### Analog output

In the "Analog output" field, select the PLC tag of the analog output via which the drive is to be controlled.

In order to be able to select an output, you first need to add an analog output module in the device configuration and define the PLC tag name for the analog output.

##### Activate enable output

Select the "Activate enable output" check box if the drive supports an enable.

Select the PLC tag of the digital output for the drive enable in the corresponding field. With the enable output, the speed controller in the drive is enabled, or disabled.

In order to be able to select an enable output, a digital output module must be added in the device configuration and the PLC tag name must be defined for the digital output.

> **Note**
>
> If you do not use an enable output, the drive cannot be immediately disabled on the part of the system due to error reactions or monitoring functions. A controlled stop of the drive is not guaranteed.

##### Enable ready input

Select the "Enable ready input" check box if the drive can signal its readiness.

Select the PLC tag of the digital input via which the drive is to signal its operational readiness to the technology object in the corresponding field. The power module is switched on and the analog speed setpoint input is enabled.

In order to be able to select a ready input, you first need to add a digital input module in the device configuration and define the PLC tag name for the digital input.

> **Note**
>
> The enable output and the ready input can be separately enabled.
>
> The following boundary conditions apply to the activated ready input:
>
> - The axis is only enabled ("MC_Power Status" = TRUE) when a signal is present at the ready input.
> - If a signal is not present at the ready input on an enabled axis, the axis is disabled with an error.
> - If the axis is disabled with the instruction "MC_Power" ("Enable" = FALSE), the axis is disabled even when a signal is present at the ready input.

##### Reference speed with analog setpoint interface

The reference speed of the drive is the speed with which the drive spins when there is an output of 100% at the analog output. The reference speed must be configured in the drive, and transferred into the configuration of the technology object.

The analog value that is output at 100% depends on the type of the analog output. For example, for an analog output with +/- 10 V, the value 10 V is output at 100%.

Analog outputs can be overridden by approximately 17%. This means that an analog output can be operated in the range from -117% to 117%, insofar as the drive permits this.

##### Reference velocity with analog setpoint interface

With a linear motor, the reference velocity is the velocity at which the drive moves with an output of 100% at the analog output. The reference velocity must be configured for the drive and transferred to the configuration of the technology object.

The analog value that is output at 100% depends on the type of the analog output. For example, for an analog output with +/- 10 V, the value 10 V is output at 100%.

Analog outputs can be overridden by approximately 17%. This means that an analog output can be operated in the range from -117% to 117%, insofar as the drive permits this.

#### Connecting force/torque data via SIEMENS additional telegram 750 (S7-1500, S7-1500T)

With the connection of the Siemens additional telegram 750 you can use the following functions:

- Specification of an additive setpoint torque (torque precontrol) based on the acceleration of the axis
- Specification of an additive setpoint torque (torque precontrol) with "MC_TorqueAdditive"
- Setting of the upper and lower torque limit with "MC_TorqueRange"
- Readout of the actual torque value with "<DB>.StatusTorqueData.ActualTorque" or "ActualForce"

> **Note**
>
> **Force data for linear motors**
>
> When using a linear motor, force data is transferred via SIEMENS additional telegram 750 instead of torque data.

##### Activation of the additional data in the technology object

If you want to configure the data connection of the torque data, select the "Torque data" check box in "Technology object > Configuration > Hardware interface > Drive data exchange with the drive > Additional data". If you have selected a drive with which the additional telegram 750 has been configured, the "Torque data" check box is preselected.

##### Data connection of the additional telegram in the technology object

If you select the entry "Additional telegram" in the "Data connection" drop-down list, you can edit the "Additional telegram" drop-down list.

- Select an additional telegram configured in the "Additional telegram" field.
- Select the "Show all modules" check box if you want to display all submodules of the connected drive. You can also find self-defined supplemental telegrams with this function.

##### Connect additional telegram via data block

If you select the "Data block" entry in the "Data connection" drop-down list, you can select the previously created data block which contains a tag structure of the "PD_TEL750" data type.

In the "Data block" field, select the data block which you want to use to integrate the torque data.

#### Encoder signal output via TM41 (S7-1500, S7-1500T)

With the TM41 you can emulate the axis position (a leading value) as encoder signal output. The output angle signal behaves like the signal of an incremental encoder. This means that you can, for example, provide a leading value as an encoder signal for an external control.

The TM41 is connected to a TO Axis via standard telegram 3. The TO can be used as an axis at the Motion FBs in the user program.

In the following figure, a real servo axis operated with DSC is controlled by a virtual axis on the SIMATIC S7-1500 and an axis with signal output is controlled via a TM41 module. The position of the servo axis is output via an encoder signal at the TM41 through the synchronous operation coupling of the two following axes. The encoder signals can be evaluated by other controllers.

![Figure](images/172707352587_DV_resource.Stream@PNG-en-US.png)

##### Requirements for the drive

- The TM41 can only be connected to SINAMICS S120 drives.
- The value [0] must be configured in the drive for the "Selection of operating mode" (p4400).

##### Restrictions

Please note the following restrictions for operation of the TM41 at the technology object.

- No active homing
- No measuring via digital drive
- Backlash compensation must be deactivated.
- Following error monitoring must be deactivated.
- Position monitoring must be deactivated.
- Standstill monitoring must be deactivated.
- Hardware limit position monitoring must be deactivated.

##### Necessary position controller setting

- Precontrol = 100%
- Speed control loop substitute time = 0.000

##### Automatic transfer of parameters

Recommendation: For the TM41, the automatic transfer of parameters should always be executed online.

Proceed as follows for automatic transfer offline:

1. Commission the TM41 online.
2. Upload the drive parameters to the TIA Portal project so that the parameters in the Startdrive project are consistent with the online parameters in the drive.

[Transferring drive and encoder parameters automatically](#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)

#### Tags: Drive and encoder connection (S7-1500, S7-1500T)

The following technology object tags are relevant for the drives and encoder connections:

| Drive telegram |  |
| --- | --- |
| Tag | Description |
| <TO>.Actor.Interface.AddressIn | Input address for the PROFIdrive telegram |
| <TO>.Actor.Interface.AddressOut | Output address for the PROFIdrive telegram or the analog setpoint |
| <TO>.Actor.DriveParameter.ReferenceSpeed | Reference value (100%) for the speed setpoint (NSET) of the drive |
| <TO>.Actor.DriveParameter.MaxSpeed | Maximum value for the speed setpoint of the drive (NSET) |
| <TO>.Actor.DriveParameter.ReferenceTorque | Reference torque for the torque transferred as a percentage |
| <TO>.Actor.LinearMotorDriveParameter.ReferenceVelocity | Reference value (100%) for the velocity setpoint of a liner motor |
| <TO>.Actor.LinearMotorDriveParameter.MaxVelocity | Maximum value for the velocity setpoint of a linear motor |
| <TO>.Actor.LinearMotorDriveParameter.ReferenceForce | Reference force for the force of a linear motor, which is transmitted as percentage value |

| Encoder telegram |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].Interface.AddressIn | Input address for the PROFIdrive telegram |
| <TO>.Sensor[1..4].Interface.AddressOut | Output address for the PROFIdrive telegram |
| <TO>.Sensor[1..4].System | Encoder system linear or rotary |
| <TO>.Sensor[1..4].Type | Encoder type, incremental, absolute or cyclic absolute |
| <TO>.Sensor[1..4].Parameter.Resolution | Resolution for linear encoder   Space between two lines |
| <TO>.Sensor[1..4].Parameter.StepsPerRevolution | Steps per revolution for rotary encoder |
| <TO>.Sensor[1..4].Parameter.DeterminableRevolutions | Number of differentiable encoder revolutions for a multi-turn absolute encoder |
| <TO>.Sensor[1..4].Parameter.DistancePerRevolution | For technology objects < V8.0:  Load distance per revolution of an externally mounted encoder  For technology objects ≥ V8.0:  Load travel per measuring wheel revolution of an externally mounted encoder |
| <TO>.Sensor[1..4].Parameter.ReferenceSpeed | Reference speed for the actual speed (NSET_B), which is transmitted as percentage value |
| <TO>.Sensor[1..4].Parameter.ReferenceVelocity | Reference velocity for the actual speed (NSET_B), which is transmitted as percentage value |
| <TO>.Sensor[1..4].MeasuringGear.Numerator | Encoder gear counter |
| <TO>.Sensor[1..4].MeasuringGear.Denominator | Encoder gear denominator |

| Fine resolution |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].Parameter.FineResolutionXist1 | Number of bits for fine resolution XIST1 (cyclic actual encoder value) |
| <TO>.Sensor[1..4].Parameter.FineResolutionXist2 | Number of bits for fine resolution XIST2 (absolute value of encoder) |

| Simulation mode |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.Simulation.Mode | Simulation mode |  |
| 0 | No simulation, normal operation |  |
| 1 | Simulation mode |  |

### Safety functions in the drive (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Brief description of the Safety functions (S7-1500, S7-1500T)](#brief-description-of-the-safety-functions-s7-1500-s7-1500t)
- [Safe stopping process (S7-1500, S7-1500T)](#safe-stopping-process-s7-1500-s7-1500t)
- [Safe brake control (S7-1500, S7-1500T)](#safe-brake-control-s7-1500-s7-1500t)
- [Safe monitoring of motion (S7-1500, S7-1500T)](#safe-monitoring-of-motion-s7-1500-s7-1500t)
- [Safe monitoring of position (S7-1500, S7-1500T)](#safe-monitoring-of-position-s7-1500-s7-1500t)
- [Overview of safety-oriented functions (S7-1500, S7-1500T)](#overview-of-safety-oriented-functions-s7-1500-s7-1500t)

#### Brief description of the Safety functions (S7-1500, S7-1500T)

In addition to programming the motion sequences, you must also reduce the risks of the machine through safety functions to ensure machine safety. The SINAMICS drive system provides integrated safety functions, hereinafter referred to as "Safety Integrated Functions".

The "Safety Integrated Functions" of the SINAMICS drive system available can be subdivided into the following functions:

- Safe stopping process
- Safe brake control
- Safe monitoring of motion
- Safe monitoring of position

More information on the "Safety Integrated Functions" in SINAMICS drives is available in the ["SINAMICS S120 Safety Integrated" function manual](https://support.industry.siemens.com/cs/ww/en/view/109771806).

##### Interaction between the technology object and the SINAMICS "Safety Integrated Functions"

The "Safety Integrated Functions" of the SINAMICS drive system are monitoring functions for fail-safe monitoring of the drive motion. The motion of the drives is controlled via technology objects and the programmed motion control jobs in the user program of the SIMATIC S7‑1500.

When using the "Safety Integrated Functions", you must evaluate the status information of the SINAMICS "Safety Integrated Functions" and program your user program depending on this status information. You can implement an interaction between the SINAMICS "Safety Integrated Functions" and the motion control in the SIMATIC S7‑1500.

The technology object does not contain any information on the states of the SINAMICS "Safety Integrated Functions". Evaluate the current status of the "Safety Integrated Functions" in the drive using one of the following options.

- "Safety Info Channel" (SIC)
- Status words of the PROFIsafe telegram (read access)

If you do not use a PROFIsafe telegram, create a telegram for the SIC.

##### Safety Info Channel

The "Safety Info Channel" is mapped in the telegrams 700 and 701.

| Status word | Status information | Telegram 700 | Telegram 701 |
| --- | --- | --- | --- |
| S_ZSW1B | - Safe stopping process - Safe monitoring of motion | x | x |
| S_ZSW2B | Safe monitoring of position | - | x |
| S_ZSW3B | Status information on the brake test | - | x |
| S_V_LIMIT_B | - Necessary velocity setpoint limiting due to the selected SINAMICS "Safety Integrated Functions". - When selecting a "Safety Integrated Function" for safe shutdown or the "Safety Integrated Function" SDI, the necessary status word S_V_LIMIT_B takes on the value 0. | x | x |

The free "LDrvSafe" library contains function blocks and a description for easy evaluation of the "Safety Info Channel" in your user program.

[LDrvSafe](https://support.industry.siemens.com/cs/ww/en/view/109485794)

##### PROFIsafe telegram

When you control the SINAMICS "Safety Integrated Functions" via PROFIsafe, you have read access from the standard user program to the PROFIsafe status words.

With this information you can react with a Motion Control Instruction suitable for your machine when a "Safety Integrated Function" is triggered in the user program.

#### Safe stopping process (S7-1500, S7-1500T)

##### **SINAMICS "** **Safety Integrated Functions** **" with drive-autonomous stop reaction**

The "Safety Integrated Function" STO triggers a drive-autonomous stop reaction and the drive coasts down (OFF2). The technology object signals the technology alarm 421 (alarm response: remove enable).

The following "Safety Integrated Functions" trigger a drive-autonomous stop reaction and the drive decelerates at the OFF3 ramp.

- SS1
- SS2

The result is that the drive performs a motion that was not specified by the technology object. The technology object signals the technology alarm 550 (alarm response: follow up setpoints). Have the technology object enabled ("MC_Power.Enable" = TRUE) so that the drive-autonomous braking process is not interrupted.

**Example - Pressing an emergency stop control device**

Example:

After pressing the emergency stop button, all drives of the machine must be brought to a standstill as quickly as possible. Standstill drives must not accelerate unintentionally.

Solution:

To this end, the "Safety Integrated Function" SS1 is selected in the SINAMICS drive system and each selected drive is independently braked electrically until it is at standstill.

**Enabling the technology object after a drive-autonomous stop reaction:**

To enable the technology object again after triggering a drive-autonomous stop reaction, follow these steps:

1. Verify in the "Safety Info Channel" SIC, whether STO, SS1 or SS2 was triggered.
2. Eliminate the cause of the triggered "Safety‑Integrated Function", for example, by unlocking the emergency stop button.
3. Safely acknowledge the pending safety messages in the drive.
4. Wait until STO, SS1 and SS2 are no longer active.
5. Acknowledge the technology alarms 421 and 550 with an "MC_Reset" job.

##### **Drive-autonomous stop reaction with coupled axes**

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Machine damage caused by loss of synchronous operation coupling after drive-autonomous stop reaction**  For axes coupled by synchronous operation, a drive-autonomous stop reaction causes each axis to decelerate individually along its own OFF3 ramp. This means that the axes are no longer coupled after SS1 or SS2. This can damage the mechanical components or the workpiece.  If permitted by the risk assessment, use the following "Safety Integrated Functions":  - SS1E instead of SS1 - SS2E or SOS instead of SS2 |  |

When triggering SS1E, no drive-autonomous deceleration is started but a safe delay time is started instead. Motion control still takes place within the safe delay time from the user program of the SIMATIC S7-1500. You must set the axis group to a standstill within the delay time. To do so, stop the leading axis of the synchronous operation, for example, with an "MC_Halt" job to safely stop the entire axis group within the safe delay time. When the safe delay time expires, STO automatically takes effect.

The same behavior applies to SS2E and SOS.

#### Safe brake control (S7-1500, S7-1500T)

The drive-based function "Safe Brake Test" (SBT) is a diagnostic function and checks the required holding torque of a brake (operating or holding brake). After starting the brake test, the drive purposely generates a torque against the applied brake.

The brake test in combination with technology objects is usually controlled via the "Safety Control Channel".

The free "LDrvSafe" library provides you with function blocks and a description for easy control of the "Safety Control Channel" and to use the safe brake test.

[LDrvSafe](https://support.industry.siemens.com/cs/ww/en/view/109485794)

#### Safe monitoring of motion (S7-1500, S7-1500T)

When you select the motion monitoring "Safety Integrated Functions" of the SINAMICS drive system, you must limit the speed and/or the acceleration of the axis to maintain the availability of the machine.

You have the following options to limit the velocity and the acceleration.

- Adapting the dynamic limits at the technology object

  - <TO>.DynamicLimits.Velocity
  - <TO>.DynamicLimits.Acceleration
- Limiting the dynamic parameters at the Motion Control instructions
- Limiting the velocity through the override "<TO>.Velocity.Override"

##### SLS

In SINAMICS, the necessary setpoint speed limiting is configured as follows:

S_V_LIMIT_B (r9733) = Selected SLS limit value (p9531) * evaluation factor (p9533

The setpoint speed limiting "S_V_LIMIT_B" is specified on the motor side in SINAMICS and calculated from the SLS limit value configured on the load side.

| Parameter | Limit value | Unit |
| --- | --- | --- |
| S_V_LIMIT_B (r9733) | Motor-side limit value | - Standard motor: 1/min - Linear motor: m/min |
| SLS limit value (p9531) | Load side limit value taking into account the mechanical parameters in SINAMICS | - Safety rotary axis: 1/min - Safety linear axis: mm/min |

To recognize the necessary setpoint speed limiting after selection of SLS, evaluate the tag "S_V_LIMIT_B" from the "Safety Info Channel". "S_V_LIMIT_B" is transmitted in the SIC normalized via the parameter p2000. The parameter p2000 is saved in the tag "<TO>.Actor.DriveParameter.ReferenceSpeed" of the technology object.

To convert "S_V_LIMIT_B" into the maximum velocity setpoint (v<sub>max</sub>) of the technology object, use the following formula for the following units of measurement.

- Linear axis with standard motor:

  ![SLS](images/165572710411_DV_resource.Stream@PNG-de-DE.png)
- Linear axis with linear motor:

  ![SLS](images/165572715531_DV_resource.Stream@PNG-de-DE.png)
- Rotary axis with standard motor:

  ![SLS](images/165572733451_DV_resource.Stream@PNG-de-DE.png)

Alternatively, especially when using fewer SLS levels, you can define the necessary setpoint speed limiting yourself and save it permanently in a data block. See the procedure for SLA as a reference.

**Example - Opening a protective door in setup mode**

Example:

The machine operator must be able to enter the danger zone of a machine after the protective door has been opened and slowly move a horizontal conveyor in it with an acknowledgment button. The actual velocity of 250 mm/s must not be exceeded in this process.

The horizontal conveyor is implemented using the following technology:

- Technology object Positioning axis as linear axis in the SIMATIC S7-1500
- Safety linear axis axes with standard motor in SINAMICS

Solution:

Select the "Safety Integrated Function" SLS with the limit value 15000 mm/min (is equivalent to 250 mm/s) in SINAMICS. If the actual velocity (intentionally or unintentionally) exceeds the limit value of 250 mm/s, a drive-autonomous, user-defined stop reaction, such as SS1, is triggered.

1. In SINAMICS, you make the following parameter assignment for the drive:

   - SLS limit value Level 1 (p9531) = 15000 mm/min = 250 mm/s
   - Evaluation factor (p9533) = 80%

   Result: The parameter assignment results in the following value for the setpoint speed limiting: 250 mm/s * 0.8 = 200 mm/s

   In this example, this means that the velocity setpoint of the horizontal conveyor is 200 mm/s before the "Safety Integrated Function" SLS Level 1 with the actual speed limit value of 250 mm/s is active.
2. Evaluate the setpoint speed limiting from "S_V_LIMIT_B" in the SIC and convert the standardized value into the velocity value with the configured unit of measurement of the technology object.

   Alternatively, especially when using fewer SLS levels, you can save the setpoint speed limiting of 200 mm/s directly in a data block.
3. Evaluate "S_ZSW1B.Bit6" from SIC (SLS selected) cyclically in the user program. If SLS is selected ("S_ZSW1B.Bit6" = TRUE), execute step 4.
4. Specify the setpoint speed limiting of 200 mm/s as dynamic limitation "<TO>.DynamicLimits.Velocity" at the technology object and limit the setpoint velocity "Velocity" at the Motion Control instructions of the technology object. Alternatively, you can also reduce the setpoint velocity via the override "<TO>.Velocity.Override".

##### SLA

For SLA, the necessary setpoint speed limiting is not calculated by the drive system but must be calculated by the user instead. In this case, you must calculate the necessary setpoint speed limiting yourself and save it in the SIMATIC S7‑1500, for example, in a data block. When selecting SLA, you limit the acceleration to this specific value.

##### SDI

You can recognize a corresponding direction of rotation limitation via the signals SDI negative/SDI positive. If the axis is currently moving in the direction that is no longer permissible after the delay time has expired, you stop or change the motion direction of the axis before the drive performs a drive-autonomous stop reaction.

#### Safe monitoring of position (S7-1500, S7-1500T)

When you select the position monitoring "Safety Integrated Functions" of the SINAMICS drive system, you must limit the position area of the axis to maintain the availability of the machine.

To recognize the permissible position area after selecting SLP, you calculate and save it in the SIMATIC S7-1500, for example, in a data block. When selecting SLP, you limit the setpoint positions of the technology object at the Motion Control instructions to this position area.

#### Overview of safety-oriented functions (S7-1500, S7-1500T)

Below you will find a description of the drive response and which corresponding user reactions you have to program in the SIMATIC user program.

| Function | SIC STW | SIC Bit | Drive response |  | Recommended reaction in the user program |
| --- | --- | --- | --- | --- | --- |
| **Safe stopping process** |  |  |  |  |  |
| STO | S_ZSW1B | 0 | 1 | Drive switches off immediately (OFF2). | "MC_Power" can remain enabled (waiting). |
| 0 | STO not active | None |  |  |  |
| SS1 | S_ZSW1B | 1 | 1 | Drive decelerates autonomously along the OFF3 ramp and then switches off (OFF2). | "MC_Power" remains enabled until STO |
| 0 | SS1 not active | None |  |  |  |
| SS1E | S_ZSW1B | 1 | 1 | Drive switches off after delay time has expired (OFF2). | Stop axis before delay time elapses, e.g. with "MC_Halt", and then switch off the drive with "MC_Power.Enable" = FALSE |
| 0 | SS1E not active | None |  |  |  |
| SS2 | S_ZSW1B | 2 | 1 | Drive decelerates along OFF3 ramp and then monitors the standstill. | "MC_Power" remains enabled |
| 0 | SS2 not active | None |  |  |  |
| SS2E | S_ZSW3B | 11 | 1 | Drive monitors the standstill after delay time has expired. | Stop axis before delay time elapses with "MC_Halt" and hold drive in control with "MC_Power.Enable" = TRUE |
| 0 | SS2E not active | None |  |  |  |
| SOS | S_ZSW1B | 3 | 1 | Drive monitors the standstill after delay time has expired | Stop axis before delay time elapses with "MC_Stop" and hold drive in control with "MC_Power.Enable" = TRUE |
| 0 | SOS not active | None |  |  |  |
| **Safe brake control** |  |  |  |  |  |
| SBC | - | - | Drive switches off immediately (OFF2) and safely controls the outputs for the brake. |  | None |
| SBT | S_ZSW_3 | 0..15 | Drive is brought to a standstill and remains in control. Then, a drive-autonomous torque is generated against the applied brake. |  | Stop axis before selecting SBT, e.g. with "MC_Halt" and hold drive in control with "MC_Power.Enable" = TRUE |
| **Safe monitoring of motion** |  |  |  |  |  |
| SLS | S_ZSW1B | 4 | 1 | Drive monitors a maximum permissible velocity. | Limit the axis velocity |
| 0 | SLS not active | None |  |  |  |
| 6 | 1 | After expiration of a delay time, drive monitors a maximum permissible velocity. | Limit axis velocity within the delay time |  |  |
| 0 | SLS deselected | None |  |  |  |
| SSM | - | - | Drive transfers signal to the F-CPU whether the current velocity is below a defined velocity. |  | Reach positive velocity of the axis within the delay time and maintain or stop axis with "MC_Halt". |
| SDI | S_ZSW1B | 12 | 1 | After expiration of a delay time, drive monitors the positive motion direction. | Reach positive velocity of the axis within the delay time and maintain or stop axis with "MC_Halt" |
| 0 | SDI positive deselected | None |  |  |  |
| 13 | 1 | After expiration of a delay time, drive monitors the negative motion direction. | Reach negative velocity of the axis within the delay time and maintain or stop axis with "MC_Halt" |  |  |
| 0 | SDI negative deselected | None |  |  |  |
| **Safe monitoring of position** |  |  |  |  |  |
| SLP | S_ZSW2B | 4 | 1 | SLP area 2 selected | None |
| 0 | SLP area 2 selected | None |  |  |  |
| 7 | 1 | After expiration of delay time, drive monitors adherence to a defined position area. | Maintain position area of the axis according to the selected SLP area |  |  |
| 0 | SLP not selected or no user approval | None |  |  |  |
| SP | - | - | Drive transfers actual position to the F-CPU. |  | None |
| SCA | - | - | Drive transfers safe cam information to the F-CPU. |  | None |

### Mechanics (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of the mechanics (S7-1500, S7-1500T)](#short-description-of-the-mechanics-s7-1500-s7-1500t)
- [Configuring the mechanics of the speed axis (S7-1500, S7-1500T)](#configuring-the-mechanics-of-the-speed-axis-s7-1500-s7-1500t)
- [Configuring the mechanics of the positioning axis/synchronous axis (S7-1500, S7-1500T)](#configuring-the-mechanics-of-the-positioning-axissynchronous-axis-s7-1500-s7-1500t)
- [Configuring the mechanics of the external encoder (S7-1500, S7-1500T)](#configuring-the-mechanics-of-the-external-encoder-s7-1500-s7-1500t)
- [Configuring drive and encoder direction for positioning axis/synchronous axis (S7-1500, S7-1500T)](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
- [Configuring the load gear (S7-1500, S7-1500T)](#configuring-the-load-gear-s7-1500-s7-1500t)
- [Configuring the encoder gear (S7-1500, S7-1500T)](#configuring-the-encoder-gear-s7-1500-s7-1500t)
- [Configuring the leadscrew pitch (S7-1500, S7-1500T)](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
- [Backlash compensation (S7-1500, S7-1500T)](#backlash-compensation-s7-1500-s7-1500t)
- [Configure inertia values (S7-1500, S7-1500T)](#configure-inertia-values-s7-1500-s7-1500t)
- [Tags: Mechanics (S7-1500, S7-1500T)](#tags-mechanics-s7-1500-s7-1500t)

#### Short description of the mechanics (S7-1500, S7-1500T)

For the display and processing of the technology object's position, the decisive factor is whether the position is represented as a unit of length (linear axis) or a unit of angle (rotary axis).

Examples of units of length: mm, m, km

Examples of units of angle: °, rad

For the determination of the physical position from an actual encoder value, the system must know the various properties and configurations of the mechanics.

#### Configuring the mechanics of the speed axis (S7-1500, S7-1500T)

In the mechanics of the speed axis technology object, you configure how the load side is connected mechanically to the drive.

Configuring the mechanics of a speed axis technology object is necessary for the correct display and processing of the technology object speed.

![Figure](images/165572738571_DV_resource.Stream@PNG-de-DE.png)

Configure the following parameters:

- Invert drive direction
- [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)

##### Inverting the drive direction of the speed axis

By default, the technology object controls the drive with positive speed if the axis is to be moved in the positive direction. Invert the drive direction if the axis travels in positive direction at negative speed due to the mechanical design.

To invert the drive direction of the speed axis, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Mechanics".
2. Select the "Invert drive direction" check box.

#### Configuring the mechanics of the positioning axis/synchronous axis (S7-1500, S7-1500T)

Configuring the mechanics of an axis technology object is necessary for the correct display and processing of the technology object position. The options for configuring the mechanics depend on the following configurations:

- "Axis type" under "Basic parameters"
- "Encoder mounting type" under "Extended parameters > Mechanics > Encoder"
- "Measuring system" under "Hardware interface > Data exchange with encoder > Encoder data"

##### Select encoder (S7-1500T)

With an S7-1500T, you can configure the mechanics of a positioning axis/synchronous axis for up to four encoders.

Select the encoder to be configured from the drop-down list under "Settings for". You can configure the encoders independently of each other.

##### "Linear" axis type with "Standard motor", encoder mounting type "On motor shaft"

The encoder is connected to the motor shaft in a mechanically fixed manner. Motor and encoder form a unit.

!["Linear" axis type with "Standard motor", encoder mounting type "On motor shaft"](images/165572768139_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Linear" and "Standard motor" under Basic parameters.
2. Under "Extended parameters > Mechanics > Encoder", select the "On motor shaft" encoder mounting type.
3. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Backlash compensation](#backlash-compensation-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Linear" axis type with "Standard motor", encoder mounting type "On load side", measuring system "Rotary"

The encoder is mechanically connected to the load side of the gear.

!["Linear" axis type with "Standard motor", encoder mounting type "On load side", measuring system "Rotary"](images/165572772107_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Linear" and "Standard motor" under Basic parameters.
2. Under "Extended parameters > Mechanics > Encoder", select the "On load side" encoder mounting type.
3. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Linear" axis type with "Standard motor", encoder mounting type "On load side", measuring system "Linear"

The encoder is mechanically connected to the load side of the gear.

![Encoder mounting type load side linear axis, measuring system linear](images/165572825483_DV_resource.Stream@PNG-de-DE.png)

Encoder mounting type load side linear axis, measuring system linear

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Linear" and "Standard motor" under Basic parameters.
2. Select the measuring system "Linear" under "Extended parameters >Hardware interface > Data exchange with encoder > Encoder data".
3. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Linear" axis type with "Standard motor", encoder mounting type "External measuring system"

An external measuring system provides the position values of the linear load motion.

!["Linear" axis type with "Standard motor", encoder mounting type "External measuring system"](images/165572776075_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Linear" and "Standard motor" under Basic parameters.
2. Under "Extended parameters > Mechanics > Encoder", select the "External measuring system" encoder mounting type.
3. Configure the linear load travel per encoder revolution under "Distance per encoder revolution".
4. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Linear" axis type with "Linear motor", encoder mounting type "External measuring system", measuring system "Rotary"

An external measuring system provides the position values of the linear load motion.

!["Linear" axis type with "Linear motor", encoder mounting type "External measuring system", measuring system "Rotary"](images/165572780043_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Linear" and "Linear motor" under Basic parameters.

   With this constellation, "External measuring system" is automatically set permanently as encoder mounting type under "Extended parameters > Mechanics > Encoder".
2. Configure the linear load travel per encoder revolution under "Distance per encoder revolution".
3. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Linear" axis type with "Linear motor", encoder mounting type "On motor shaft", measuring system "Linear"

An external measuring system provides the position values of the linear load motion.

!["Linear" axis type with "Linear motor", encoder mounting type "On motor shaft", measuring system "Linear"](images/165572821515_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Linear" and "Linear motor" under Basic parameters.

   With this constellation, "On motor shaft" is automatically set permanently as encoder mounting type under "Extended parameters > Mechanics > Encoder".
2. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Rotary" axis type with "Standard motor", encoder mounting type "On motor shaft"

The encoder is connected to the motor shaft in a mechanically fixed manner. Motor and encoder form a unit.

!["Rotary" axis type with "Standard motor", encoder mounting type "On motor shaft"](images/165572784011_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Rotary" and "Standard motor" under Basic parameters.
2. Under "Extended parameters > Mechanics > Encoder", select the "On motor shaft" encoder mounting type.
3. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Backlash compensation](#backlash-compensation-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Rotary" axis type with "Standard motor", encoder mounting type "On load side"

The encoder is mechanically connected to the load side of the gear.

!["Rotary" axis type with "Standard motor", encoder mounting type "On load side"](images/165572787979_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Rotary" and "Standard motor" under Basic parameters.
2. Under "Extended parameters > Mechanics > Encoder", select the "On load side" encoder mounting type.
3. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### "Rotary" axis type with "Standard motor", encoder mounting type "External measuring system"

An external measuring system provides the position values of the rotary load motion.

!["Rotary" axis type with "Standard motor", encoder mounting type "External measuring system"](images/165572791947_DV_resource.Stream@PNG-de-DE.png)

To configure the mechanics for this constellation of axis type and encoder mounting type, follow these steps:

1. Check that the axis type is configured as "Rotary" and "Standard motor" under Basic parameters.
2. Under "Extended parameters > Mechanics > Encoder", select the "External measuring system" encoder mounting type.
3. Configure the rotary load travel per encoder revolution under "Distance per encoder revolution".
4. Configure the following parameters:

   - [Drive and encoder direction for positioning axis/synchronous axis](#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
   - [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
   - [Encoder gear](#configuring-the-encoder-gear-s7-1500-s7-1500t)
   - [Inertia values](#configure-inertia-values-s7-1500-s7-1500t)

---

**See also**

PosAxis_Config_MechanicDrive_111037 (S7-1500, S7-1500T)
  
PosAxis_Config_MechanicEncoder_111038 (S7-1500, S7-1500T)

#### Configuring the mechanics of the external encoder (S7-1500, S7-1500T)

In the mechanics of the external encoder technology object, you configure how the external encoder is connected mechanically to an axis.

Configuring the mechanics of an external encoder technology object is necessary for the correct display and processing of the technology object position. The options for configuring the mechanics depend on the following configurations:

- "External encoder type" under "Basic parameters"
- "Measuring system" under "Hardware interface > Data exchange with encoder > Encoder data"

##### "Linear" type, measuring system "Rotary"

!["Linear" type, measuring system "Rotary"](images/165572833419_DV_resource.Stream@PNG-de-DE.png)

Configure the following parameters:

- Invert encoder direction
- [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)
- [Leadscrew pitch](#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)

##### "Linear" type, measuring system "Linear"

!["Linear" type, measuring system "Linear"](images/165572841355_DV_resource.Stream@PNG-de-DE.png)

Configure the following parameters:

- Invert encoder direction
- In the "Distance between increments" field, configure the distance between the increments of the linear encoder.

##### "Rotary" type

!["Rotary" type](images/165572829451_DV_resource.Stream@PNG-de-DE.png)

Configure the following parameters:

- Invert encoder direction
- [Load gear](#configuring-the-load-gear-s7-1500-s7-1500t)

##### Inverting the encoder direction for external encoder

To invert the encoder direction for an external encoder, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Mechanics > Encoder".
2. Select the "Invert encoder direction" check box.

##### Example: Inverting the encoder direction for an external encoder

In the following example, an external encoder with two different installation directions is shown. If the encoder rotates in the counter-clockwise direction or counts in the negative direction when the axis travels in the positive direction, you need to invert the encoder direction.

![Example: Inverting the encoder direction for an external encoder](images/165572837387_DV_resource.Stream@PNG-de-DE.png)

To check the direction of rotation, you can monitor the "Gx_XIst1" value from the PROFIdrive telegram in a trace.

Rotate the encoder shaft as it rotates when the axis travels in the positive direction:

- Value "Gx_XIst1" decreases: The encoder counts in the negative direction. Invert the encoder direction.
- Value "Gx_XIst1" increases: The encoder counts in the positive direction, no inversion necessary.

#### Configuring drive and encoder direction for positioning axis/synchronous axis (S7-1500, S7-1500T)

For the speed axis and positioning axis/synchronous axis technology objects, you can invert the drive and encoder direction.

##### Configuring drive and encoder direction on a positioning axis

By default, the technology object controls the drive with positive speed if the axis is to be moved in the positive direction. Invert the drive direction if the axis travels in positive direction at negative speed due to the mechanical design.

By default, an increasing actual encoder value is evaluated as positive direction of movement of the axis. Invert the encoder direction if the actual encoder value decreases when the axis travels in the positive direction.

With SINAMICS drives, the direction of the drive and the direction of the motor encoder are identical by default. If the axis travels in the positive direction at positive speeds, you do not need to invert either the drive direction or the encoder direction.

In the following figure, the drive direction, encoder direction and the real mechanical direction of movement are positive. This arrangement does not require inversion.

![Configuring drive and encoder direction on a positioning axis](images/165572870923_DV_resource.Stream@PNG-de-DE.png)

Invert the drive direction and the encoder direction if the axis travels in the mechanically negative direction with positive motor speed and increasing encoder increments.

An example of this is the linear axis in the following figure, which travels in the negative direction with positive speed.

![Configuring drive and encoder direction on a positioning axis](images/165572874891_DV_resource.Stream@PNG-de-DE.png)

Through the inversion of the drive direction and the encoder direction, the motor travels with negative speed in the case of positively specified velocity, which results in movement in the correct direction. You also need to invert the encoder direction, because the motor encoder direction corresponds to the drive direction.

##### Invert drive direction

To invert the drive direction, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Mechanics > Drive".
2. Select the "Invert drive direction" check box.

##### Invert encoder direction

To invert the encoder direction, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Mechanics > Encoder".
2. Select the "Invert encoder direction" check box.

#### Configuring the load gear (S7-1500, S7-1500T)

If you use a load gear between motor shaft and load side, you need to configure the load gear at the technology object.

The gear ratio of the load gear is specified as the ratio between motor revolutions and load revolutions.

You can configure the load gear for the following technology objects:

- Speed axis
- Positioning axis/synchronous axis
- External encoder

##### Procedure

To configure the load gear, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Mechanics > Drive > Load gear".
2. In the "Number of motor revolutions" configuration field, configure the integer number of motor revolutions.
3. In the "Number of load revolutions" configuration field, configure the integer number of load revolutions.

#### Configuring the encoder gear (S7-1500, S7-1500T)

If you use a measuring gearbox for encoders of axes, you need to configure the encoder gear at the technology object. The gear ratio of the load gear is specified as a ratio.

You can configure the encoder gear for the following technology objects:

- Positioning axis/synchronous axis

You can find the setting in the configuration of the technology object in the section "Extended parameters > Mechanics > Encoder > Encoder gear.

Depending on the mounting type of the encoder, you have to configure the following values:

- External measuring system:

  - In the "Number of measuring wheel revolutions" configuration field, configure the integer number of measuring wheel revolutions.
  - In the "Number of encoder revolutions" configuration field, configure the integer number of encoder revolutions.
  - In the "Distance per measuring wheel revolution" configuration field, configure the distance covered by the measuring wheel in one revolution.
- On load side:

  - In the "Number of load revolutions" configuration field, configure the integer number of load revolutions.
  - In the "Number of encoder revolutions" configuration field, configure the integer number of encoder revolutions.
- On the motor shaft:

  - In the "Number of motor revolutions" configuration field, configure the integer number of motor revolutions.
  - In the "Number of encoder revolutions" configuration field, configure the integer number of encoder revolutions.

#### Configuring the leadscrew pitch (S7-1500, S7-1500T)

The leadscrew pitch indicates the distance by which the load is moved when the leadscrew makes one revolution.

You can configure the leadscrew pitch for the following technology objects:

- Positioning axis/synchronous axis
- External encoder

**Example**

Movement of the load [mm] = Leadscrew pitch * number of motor revolutions * (load gear denominator / load gear numerator)

Load gear denominator = 2

Load gear numerator = 1

Leadscrew pitch = 10 mm / load revolution

Motor revolutions = 50

1000 mm = 10 [mm/rot] * 50 [rot] * 2

##### Procedure

To configure the leadscrew pitch, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Mechanics > Drive > Position parameters".
2. Enter the leadscrew pitch for the technology object in unit of measurement for position of the technology object per revolution in the "Leadscrew pitch" configuration field.

#### Backlash compensation (S7-1500, S7-1500T)

##### What is the backlash?

Backlash (also called play, mechanical play) is the distance or the angle that a motor must travel through when the direction of rotation reverses until the axis actually moves in the other direction.  
The backlash of an axis is made up of the backlash of the gearbox and spindle.

The following figure shows the backlash on the spindle of a linear axis.

![What is the backlash?](images/165572878859_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Load side |
| ② | Drive side |
| ③ | Axis position |
| ④ | Motor position |
| ⑤ | Size of backlashes |

An encoder with mounting type "on motor shaft" records the motor position. The technology object calculates the axis position from the motor position, taking the mechanics (gear unit, leadscrew pitch) into account.

If there is a backlash on the axis, then this backlash is traversed during a reversing motion at the reversal point. While the backlash is being traversed, the real mechanical position of axis does not change, but the motor position changes. Without backlash compensation, the technology object calculates a faulty axis position from the motor position, which means that the axis is not moved to the correct axis position during a reversing motion job.

##### Backlash compensation

If you enable backlash compensation for the motor encoder, the backlash is taken into account when calculating the axis position. The axis is always moved to the correct axis position even with a reversing motion job.

**Setpoint operation**

The setpoint mode is the standard mode of the axis in which motion jobs are accepted and executed.

When the direction of the position setpoint is reversed, the technology object automatically compensates for the backlash. When the motion job starts with a direction reversal, the actual position value of the technology object is adapted. The following settings are relevant for calculating the actual position value:

- Size of backlashes
- Velocity of backlash compensation

The resulting following error is compensated by the position controller and the backlash is traversed. The traversing of the backlash is therefore also dependent on the position controller gain (kv factor).

**Follow-up mode**

In follow-up mode the setpoint is followed up to the actual value. Actual position and actual velocity are updated. This means that it is possible to track when the axis is moved by external influence. Motion jobs are not executed.

Backlash compensation is required in follow-up mode if an axis is moved on the load side with a direction reversal. The same compensation model is used in follow-up mode as in setpoint mode. After the direction reversal of the actual encoder value has been recognized, the actual position value of the technology object is only coupled when the complete size of backlashes has been traversed.

##### Requirements

- Technology objects (V6.0 or higher)

  - Positioning axis
  - Synchronous axis
- Encoder mounting type: On motor shaft

  Backlash compensation is not relevant for a load-side encoder and external measuring systems. A load-side encoder records the axis position directly. After a direction reversal, the backlash on the load-side encoder is traversed using the position control.

> **Note**
>
> **Excessive velocity if the backlash is too large**
>
> Do not set the backlashes larger than as the real existing backlashes. With direction reversal, note that the actual position value is adapted according to the set velocity of backlash compensation and the size of backlashes. A higher velocity of backlash compensation shortens the compensation time. The resulting control difference is output via the position controller.

##### Enable backlash compensation

To activate backlash compensation for an axis, proceed as follows:

1. In the configuration of the Axis technology object, navigate to "Extended parameters"> "Mechanics".
2. Select the "Enable backlash compensation" check box.

In case of axes with multiple encoders, you must activate backlash compensation for each encoder individually.

##### Backlash compensation settings

In the configuration of the technology object, set the following values for backlash compensation:

- Size of backlashes
- Velocity of backlash compensation. At 0.0, the actual value is modified in a servo cycle.
- Absolute homing direction (relevant for absolute encoders)

You have the option of changing the settings for the backlash compensation directly during runtime without restarting the technology object. Change the value of the tags in the technology object "<TO>.Sensor[1..4].Backlash".

After changing the settings for backlash compensation, you have to home the axis again.

You can find more information on the tags of the technology objects in the section "[Appendix](#appendix-s7-1500-s7-1500t)".

##### Backlash compensation function chart

The function chart shows how the backlash compensation affects the movement of an axis when the direction changes.

![Backlash compensation function chart](images/165572883851_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The reversing motion job "MC_MoveRelative" is triggered. The actual motor value is modified by the backlash and the axis traverses the backlash via the position controller. |
| The "<TO>.StatusWord2.PassingBacklash" bit is set. |  |
| ② | The backlash is run through completely. |
| The "<TO>.StatusWord2.PassingBacklash" bit is reset. |  |
| The axis position "<TO>.ActualPosition" is adjusted to the position setpoint "<TO>.Position" via the position control. |  |

##### Homing when backlash compensation is enabled

You can find more information in the section "[Homing when backlash compensation is enabled](#homing-when-backlash-compensation-is-enabled-s7-1500-s7-1500t)".

**Reversal of direction for non-homed axes**

The backlash compensation when the direction is reversed is independent of the "Homed" status. In the first motion of the non-homed axis, the backlash compensation is not active. After the axis has completely passed through the backlash in one direction, the backlash compensation becomes active when the axis travels in the opposite direction.

##### What do you need to note in axes with multiple encoders?

- If the effective encoder is a load-side encoder, then the backlash is implicitly controlled via the position control.
- The position of the motor encoder is followed up accordingly during operation with the load-side encoder as an effective encoder and the backlash is taken into account.
- Switch from a load-side encoder to the motor encoder with "MC_SetSensor" with "Mode" = 0:

  - The backlash must be completely run through once in order that you can set the position of the motor encoder to the same as that of the encoder on the load side.
  - The homing status of the axis is maintained. A new homing is not required on the motor encoder.
- Switch the motor encoder to a load-side encoder with "MC_SetSensor" with "Mode" = 0:

  - The backlash must be completely run through once in order that you can match the position of the load-side encoder to the position of the motor encoder.

##### How large is the backlash?

The following basic options are available to determine the size of backlashes:

- Read the backlash from the data sheet, e.g. for a ball screw
- Measuring backlash

**Example: Measuring the size of backlashes on a linear axis**

Using a linear axis as example, the following section describes how you can determine the size of backlashes by measuring.

Requirement: Backlash compensation is not enabled.

1. Traverse the axis to an axis position A. Mark the axis position and write down the corresponding actual value from the technology object (<TO>.ActualPosition).
2. Continue to move the axis in the same direction at least around the expected size of backlashes.
3. Traverse the axis to the noted actual value from 1. or by the traveled distance from 2. Because of the backlash, the axis is now at of axis position B.
4. Measure the position difference of the axis positions Δ = A - B.

   ![How large is the backlash?](images/165622549771_DV_resource.Stream@PNG-en-US.png)

   You have measured the backlash.
5. Activate backlash compensation and enter the measured size of backlashes.

#### Configure inertia values (S7-1500, S7-1500T)

Configure the inertia values for the axis under "Extended parameters > Mechanics > Inertia values"

The configuration of the inertia values is a requirement for calculating torque precontrol in the "Based on acceleration" mode.

You can find information on torque precontrol in the section "[Configuring the torque precontrol](#configuring-the-torque-precontrol-s7-1500-s7-1500t)".

##### Automatically adopt Inertia values from drive

For drives with DSC, you can transfer the inertia values for the configuration of the position controller with "Automatic transfer from drive".

You can find information on "Automatic transfer from drive" in the section "[Configuring position controller for drives with DSC](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)".

##### Moment of inertia or weight of the load

Configure the moment of inertia or weight of the load depending on the motion.

- For rotary motions Moment of inertia
- For linear motions Mass

You must configure the moment of inertia or weight of the load on the load side.

Follow these steps:

1. Define the p1498 in the drive.

   To determine the value for p1498 once, use "One Button Tuning" for the drive. You can find information on "One Button Tuning" in the function manual of the SINAMICS drive.
2. Convert the value to the load side.
3. Enter the load-side value in the configuration field.

##### Moment of inertia motor

Configure the moment of inertia of the standard motor.

You can adopt the value p0341 from the drive.

##### Mass of motor

Configure the weight of the linear motor.

You can adopt the value p0341 from the drive.

#### Tags: Mechanics (S7-1500, S7-1500T)

The following technology object tags are relevant for the setting of the mechanics:

| Type of motion |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.Properties.MotionType | Indication of linear or rotary motion |  |
| 0 | Linear motion |  |
| 1 | Rotary motion |  |

| Load gear |  |
| --- | --- |
| Tag | Description |
| <TO>.LoadGear.Numerator | Load gear numerator |
| <TO>.LoadGear.Denominator | Load gear denominator |

| Leadscrew pitch |  |
| --- | --- |
| Tag | Description |
| <TO>.Mechanics.LeadScrew | Leadscrew pitch |
| <TO>.Actor.Efficiency | Efficiency of leadscrew pitch |

| Encoder mounting type |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].MountingMode | Encoder mounting type |
| <TO>.Sensor[1..4].Parameter.DistancePerRevolution | Load distance per encoder revolution with an externally mounted encoder |

| Inversion |  |
| --- | --- |
| Tag | Description |
| <TO>.Actor.InverseDirection | Setpoint inversion |
| <TO>.Sensor[1..4].InverseDirection | Actual value inversion |

| Modulo |  |
| --- | --- |
| Tag | Description |
| <TO>.Modulo.Enable | Enable modulo |
| <TO>.Modulo.Length | Modulo length |
| <TO>.Modulo.StartValue | Modulo start value |

| Backlash compensation |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].Backlash.Enable | Enable backlash compensation |
| <TO>.Sensor[1..4].Backlash.Size | Size of backlashes<sup>1)</sup> |
| <TO>.Sensor[1..4].Backlash.Velocity | Velocity for traversing of backlashes  At 0.0, the backlash is traversed in a servo cycle.  (only with positioning axis and synchronous axis) |
| <TO>.Sensor[1..4].Backlash.DirectionAbsoluteHoming | Direction of movement during or before absolute encoder adjustment |
| <sup>1)</sup> If you enable/disable backlash compensation or change the size of backlashes during runtime, you must home the axis again. |  |

| Inertia values |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.Actor.LoadInertia | Depends on the motion |  |
| Rotary motion | Moment of inertia of the load |  |
| Linear motion | Weight of the load |  |
| <TO>.Actor.DriveParameter.MotorInertia | Moment of inertia of the standard motor |  |
| <TO>.Actor.LinearMotorDriveParameter.MotorMass | Mass of linear motor |  |

### Configuring "Remove enable" alarm responses (S7-1500, S7-1500T)

For technology alarms with the reaction "Remove enable," axes with PROFIdrive drives stop based on the configured stop mode and the drive configuration.

The configuration is available for the positioning, speed, and synchronous axis. The configuration is not relevant for the virtual axis and the axis in simulation.

#### Overview of stop modes

- Delay ramp (OFF1) - STW 1 Bit 0 = 0

  ![Overview of stop modes](images/172386415883_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Maximum drive speed |
  | ② | OFF1 ramp-down time |

  - The drive moves to speed "0.0" with the deceleration configured at the drive (parameter "p1121 - Ramp-function generator ramp-down time").
  - The stop process can be interrupted
  - After stopping, a pulse inhibit occurs and the status changes to "Ready to start"
- Coast down (OFF2) - STW 1Bit 1 = 0

  ![Overview of stop modes](images/172386420107_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Current speed |
  | ② | Coasting down |

  - The drive deletes the pulses and the status changes to "closing lockout"
  - The drive is switched off and coasts to a stop.
  - The stop process cannot be interrupted.
- Quick stop (OFF3) - STW 1 Bit 2 = 0

  ![Overview of stop modes](images/172386424331_DV_resource.Stream@JPG-de-DE.jpg)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Maximum drive speed |
  | ② | OFF3 ramp-down time |
  | ③ | Closing lockout (OFF1, OFF2) |

  - The drive moves to the stop with the deceleration configured on the drive speed "0.0" (parameter "p1135 - OFF3 ramp-down time").
  - The stop process cannot be interrupted.
  - After stopping, a pulse inhibit occurs and the status changes to "Closing lockout"

#### Configure stop mode for alarm response "Remove enable"

To set the stop mode, proceed as follows:

- Configure the stop mode in the technology object configuration under "Extended parameters > Alarm responses".
- Alternatively, write the stop mode to the load memory of the technology object in the user program (<TO>.Actor.RemoveEnableReaction) with the "WRIT_DBL" instruction. Apply the change by restarting the technology object.

The following table shows the corresponding alarm response depending on the configuration:

| Configuration |  |  |  |  |
| --- | --- | --- | --- | --- |
| OFF3 | OFF2 | OFF1 | "<TO>.Actor.RemoveEnableReaction" | Stop mode for alarm response "Remove enable" |
| 1 | 1 | 1 | 16#7 | OFF3 – Quick stop (compatible configuration for technology versions up to V7)  Default setting |
| 1 | 0 | 1 | 16#5 | OFF3 – Quick stop |
| 0 | 1 | 1 | 16#3 | OFF2 – Coast down |
| 0 | 0 | 1 | 16#1 | OFF1 – Ramp-down ramp |

#### Procedure for enabling the axis

To enable the axis again after the alarm response, follow these steps:

1. Do not call "MC_Power" while the stop response is active. For this, evaluate "ErrorDetails.Reaction" = 4.

   If the alarm is acknowledged and "MC_Power" is called during the braking ramp, this can lead to undesirable compensating movements.
2. Acknowledge the alarm when the drive is at a standstill.

   You can use, for example, the standstill signal (<TO>.StatusWord.X7(Standstill)) to detect the standstill.
3. To enable the axis again, call "MC_Power" with input "Enable" = TRUE.

Note the following if you set a value other than 16#7 (default setting) as the alarm response in "RemoveEnableReaction":

- Disabling the axis while alarm response "RemoveEnable" is active ("ErrorDetails.Reaction" = 4) with "MC_Power.Enable" = FALSE leads to AUS2 (coast-down) of the axis irrespective of the "StopMode".

Note the following if you set 16#7 (default setting) as the alarm response in "RemoveEnableReaction":

- An active AUS3 ramp cannot be interrupted until the drive reaches a standstill. The axis is disabled after reaching a standstill.

#### More information

You can find more information on PROFIdrive with using state machines as well as control and status words at Siemens Industry Online Support in the FAQ entry [109770665](https://support.industry.siemens.com/cs/ww/en/view/109770665).

---

**See also**

[Standstill signal (S7-1500, S7-1500T)](#standstill-signal-s7-1500-s7-1500t)

### Motion control and limits for dynamics (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of motion control and dynamic limits (S7-1500, S7-1500T)](#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
- [Dynamic defaults for modulo axes (S7-1500, S7-1500T)](#dynamic-defaults-for-modulo-axes-s7-1500-s7-1500t)
- [Velocity profile (S7-1500, S7-1500T)](#velocity-profile-s7-1500-s7-1500t)
- [Override response with and without jerk limitation (S7-1500, S7-1500T)](#override-response-with-and-without-jerk-limitation-s7-1500-s7-1500t)
- [Emergency stop deceleration (S7-1500, S7-1500T)](#emergency-stop-deceleration-s7-1500-s7-1500t)
- [Torque limits (S7-1500, S7-1500T)](#torque-limits-s7-1500-s7-1500t)
- [Superimposed motions (S7-1500, S7-1500T)](#superimposed-motions-s7-1500-s7-1500t)
- [Motion specification via "MotionIn" (S7-1500T)](#motion-specification-via-motionin-s7-1500t)
- [Tags: Motion control and limits for dynamics (S7-1500, S7-1500T)](#tags-motion-control-and-limits-for-dynamics-s7-1500-s7-1500t)

#### Short description of motion control and dynamic limits (S7-1500, S7-1500T)

Motion control of the axis occurs by means of [velocity profiles](#velocity-profile-s7-1500-s7-1500t). The velocity profiles are calculated in accordance with the specifications for dynamics. A velocity profile defines the behavior of the axis during approach, braking and changes in velocity. During positioning a velocity profile is calculated, that moves the axis to the target point.

The configurable [emergency stop deceleration](#emergency-stop-deceleration-s7-1500-s7-1500t) is triggered by the Motion Control instructions "MC_Power" and "MC_Stop" or by a technology alarm.

The jerk limit reduces the mechanical load during a change in acceleration or deceleration. The result is a "smoothed" velocity profile.

##### Configuring dynamic defaults at the technology object

You can configure dynamic defaults for motion jobs for the axis technology object. You define values as dynamic defaults that can be used for motion jobs in most situations.

Configure the following dynamic defaults under "Extended parameters > Dynamic default":

- Velocity (<TO>.DynamicDefaults.Velocity)

  In the "Velocity" field, you configure the default value for the velocity of the axis.
- Acceleration (<TO>.DynamicDefaults.Acceleration)

  You configure the default value for acceleration in the "Ramp-up time" or "Acceleration" fields.

  Relationship between ramp-up time and acceleration:

  ![Configuring dynamic defaults at the technology object](images/165623097611_DV_resource.Stream@PNG-en-US.png)

  > **Note**
  >
  > A change in the velocity influences the acceleration value of the axis. The ramp-up time remains.
- Deceleration (<TO>.DynamicDefaults.Deceleration)

  You configure the default value for deceleration in the "Ramp-down time" or "Deceleration" fields.

  Relationship between ramp-down time and deceleration:

  ![Configuring dynamic defaults at the technology object](images/165623103627_DV_resource.Stream@PNG-en-US.png)

  > **Note**
  >
  > A change in the velocity influences the deceleration value of the axis. The ramp-down time remains.
- Jerk of the axis (<TO>.DynamicDefaults.Jerk)

  - You configure the jerk for the acceleration and deceleration ramp in the "Jerk" box. The value "0" means that jerk limiting is deactivated.
  - You configure the smoothing time for the acceleration ramp in the "Smoothing time" field.

    > **Note**
    >
    > The jerk value is identical for the acceleration and deceleration ramps. The smoothing time in effect for the deceleration ramp results from the following relationships:
    >
    > - **Acceleration > Deceleration**
    >
    >   A shorter smoothing time is used for the deceleration ramp compared with the acceleration ramp.
    > - **Acceleration < Deceleration**
    >
    >   A longer smoothing time is used for the deceleration ramp compared with the acceleration ramp.
    > - **Acceleration = Deceleration**
    >
    >   The smoothing times of the acceleration and deceleration ramp are equal.
    >
    > In case of a fault, the axis decelerates with the configured emergency stop deceleration. A configured jerk limit is not taken into account for this.

    Relationship between the smoothing times and the jerk:

    ![Configuring dynamic defaults at the technology object](images/165622868747_DV_resource.Stream@PNG-en-US.png)

    ![Configuring dynamic defaults at the technology object](images/165622874379_DV_resource.Stream@PNG-en-US.png)

    Motion jobs started in the user program are performed with the selected jerk.

The default values for acceleration and deceleration also act on the traversing motions of active homing.

##### Parameterizing dynamic values in Motion Control instruction

At the Motion Control instructions, you configure the dynamic values for a motion job at the parameters "Velocity", "Acceleration", "Deceleration" or "Jerk". You make the parameter assignment for each parameter individually.

**Using dynamic defaults for a motion job**

To use a dynamic default for a motion job, set a value of less than 0 at the parameter (default: -1.0).

The following table shows which dynamic defaults you can use with which Motion Control instruction.

| Motion Control instruction | <TO>.DynamicDefaults.Velocity | <TO>.DynamicDefaults.Acceleration | <TO>.DynamicDefaults.Deceleration | <TO>.DynamicDefaults.Jerk |
| --- | --- | --- | --- | --- |
| MC_MoveAbsolute | ✓ | ✓ | ✓ | ✓ |
| MC_MoveRelative | ✓ | ✓ | ✓ | ✓ |
| MC_MoveVelocity | - | ✓ | ✓ | ✓ |
| MC_MoveJog | - | ✓ | ✓ | ✓ |
| MC_MoveSuperimposed | ✓<sup>1)</sup> | ✓ | ✓ | ✓ |
| MC_Halt | - | - | ✓ | ✓ |
| MC_HaltSuperimposed | - | - | ✓ | ✓ |
| MC_STOP."Mode" = 3 | - | - | ✓ | ✓ |
| <sup>1)</sup> At the parameter "MC_Superimposed.VelocityDiff" |  |  |  |  |

**Parameterizing individual dynamic values for a motion job**

To use an individual dynamic value for a motion job, set a value that is greater than 0 at the parameter.

##### Limiting the dynamics

Maximum values for velocity, acceleration, deceleration and jerk result from the properties of the drive and the mechanics.

Configure the following dynamic limits under "Extended parameters > Limits > Dynamic limits":

- Maximum velocity (<TO>.DynamicLimits.MaxVelocity)

  Configure the maximum permitted velocity of the axis in the "Maximum velocity" field.
- Maximum acceleration (<TO>.DynamicLimits.MaxAcceleration)

  Configure the maximum permitted acceleration in the "Ramp-up time" or "Maximum acceleration" fields.

  Relationship between ramp-up time and maximum acceleration:

  ![Limiting the dynamics](images/165623109643_DV_resource.Stream@PNG-en-US.png)

  > **Note**
  >
  > A change in the maximum velocity influences the acceleration value of the axis. The ramp-up time remains.
- Maximum deceleration (<TO>.DynamicLimits.MaxDeceleration)

  Configure the maximum permitted deceleration in the "Ramp-down time" or "Maximum deceleration" fields.

  Relationship between ramp-down time and maximum deceleration:

  ![Limiting the dynamics](images/165623243659_DV_resource.Stream@PNG-en-US.png)

  > **Note**
  >
  > The "maximum deceleration" for active homing with change of direction at the hardware limit switch must be set sufficiently high to brake the axis before it reaches the mechanical endstop.
  >
  > A change in the velocity influences the deceleration value of the axis. The ramp-down time remains.
- Jerk (<TO>.DynamicLimits.MaxJerk)

  You configure the jerk for the dynamic limits in the "Smoothing time" and "Jerk" fields. The same rules apply for the configuration as for the dynamic default of the jerk.

The limits for dynamics are in effect as limits for every motion generated by means of the technology object. The dynamic limits have no effect on a following axis in synchronous operation.

##### Interaction of dynamic defaults and dynamic limits

The following overview shows how the dynamic value for a motion job is formed from the dynamic defaults and the dynamic limits.

![Interaction of dynamic defaults and dynamic limits](images/165622555659_DV_resource.Stream@PNG-en-US.png)

**Examples**

The following table shows examples for the formation of the dynamic value for the velocity at a job of the instruction MC_MoveAbsolute.

|  | Configured dynamic default  <TO>.DynamicDefaults.Velocity | Parameterized value at the motion job  MC_MoveAbsolute.Velocity | Dynamic limit  <TO>.DynamicLimits.MaxVelocity | Dynamic value at the motion job |
| --- | --- | --- | --- | --- |
| **Example 1** | 2000.0 | -1.0 | 4000.0 | 2000.0 |
| **Example 2** | 2000.0 | -1.0 | 500.0 | 500.0 |
| **Example 3** | 2000.0 | 3000.0 | 4000.0 | 3000.0 |
| **Example 4** | 2000.0 | 6000.0 | 4000.0 | 4000.0 |

#### Dynamic defaults for modulo axes (S7-1500, S7-1500T)

##### Maximum permissible velocity of the modulo axis

Note the maximum permissible velocity for modulo axes.

- Modulo axis has not been configured as a possible leading value for a synchronous axis technology object:

  ![Maximum permissible velocity of the modulo axis](images/165623249675_DV_resource.Stream@PNG-en-US.png)

  If the maximum permissible velocity is exceeded, alarm 412 is output and the axis is blocked.
- Modulo axis has been configured as a possible leading value for a synchronous axis technology object:

  ![Maximum permissible velocity of the modulo axis](images/165623460363_DV_resource.Stream@PNG-en-US.png)

  When the limit is active, alarm 501 is output.

#### Velocity profile (S7-1500, S7-1500T)

Velocity profiles with or without jerk limitation are supported for motion control of the axis.

The dynamic values for the motion are specified in the Motion Control job. Alternatively, the values of the dynamics defaults can be used. The defaults and the limits for velocity, acceleration, deceleration and jerk are set in the configuration.

To influence velocity, a velocity override can override the current traversing velocity.

##### Velocity profile without jerk limitation

The following figure shows velocity, acceleration and jerk:

![Velocity profile without jerk limitation](images/165572912011_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Velocity profile without jerk limitation](images/165572888971_DV_resource.Stream@PNG-de-DE.png) | Acceleration |
| ![Velocity profile without jerk limitation](images/165572894091_DV_resource.Stream@PNG-de-DE.png) | Deceleration |

##### Velocity profile with jerk limitation

The following figure shows velocity, acceleration and jerk:

![Velocity profile with jerk limitation](images/165572917643_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Velocity profile with jerk limitation](images/165572888971_DV_resource.Stream@PNG-de-DE.png) | Acceleration |
| ![Velocity profile with jerk limitation](images/165572894091_DV_resource.Stream@PNG-de-DE.png) | Deceleration |

A velocity profile with jerk limitation is employed for a continuous acceleration and deceleration sequence. The jerk can be specified.

#### Override response with and without jerk limitation (S7-1500, S7-1500T)

When overriding the active job with a new jerk-limited motion, the current acceleration or deceleration is transferred to the new acceleration/deceleration via the jerk. For overriding motions without jerk limitation, the acceleration/deceleration of the overriding job is effective immediately.

The following figure shows velocity, acceleration and jerk:

![Figure](images/165572961675_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165572888971_DV_resource.Stream@PNG-de-DE.png) | Acceleration |
| ![Figure](images/165572894091_DV_resource.Stream@PNG-de-DE.png) | Deceleration |

**Section A**

An "MC_MoveVelocity" job A1 is active.

In the following sections B, C and D, the job A1 is replaced by an additional "MC_MoveVelocity" job A2, A3 and A4 with "Velocity" = 0 in each case but with different jerk values.

**Section B**

At time ①, the active job A1 is overridden by a job A2 with low jerk. The acceleration is slowly transitioned via the jerk into the deceleration of the overriding job.

**Section C**

At time ②, the active job A1 is overridden by a job A3 with high jerk. The acceleration is quickly transitioned via the jerk into the deceleration of the overriding job.

**Section D**

At time ③, the active job A1 is overridden by a job A4 without jerk limitation. The deceleration of the overriding job is effective immediately.

#### Emergency stop deceleration (S7-1500, S7-1500T)

When stopping with the emergency stop ramp, the axis is braked from the current actual position and actual velocity to a standstill without a jerk limitation, using the configured emergency deceleration.

In the following cases the configured emergency stop deceleration is in effect:

- In case of an emergency stop ramp that has been enabled via the Motion Control instruction "MC_Power" or "MC_Stop".
- For a technology alarm with the local alarm response "Stop with emergency stop ramp".

This emergency stop deceleration can be set greater than the maximum deceleration. If the emergency stop deceleration is set lower than this, it may occur that the axis does not stop until after the limit switch in the case of "Stop at software limit switch" and the occurrence of a technology alarm with the local alarm response "Stop with emergency stop ramp".

##### Configuring emergency stop deceleration

Under "Extended parameters > Emergency stop", you configure the deceleration value for emergency stop in the "Emergency stop deceleration" or "Emergency stop ramp-down time" fields.

The following equation shows the relationship between emergency stop ramp-down time and emergency stop deceleration.

![Configuring emergency stop deceleration](images/165571044747_DV_resource.Stream@PNG-en-US.png)

The configuration of the emergency stop deceleration is related to the configured maximum velocity of the axis. When the maximum velocity of the axis changes, then the value of the emergency stop deceleration also changes. The emergency stop ramp-down time remains unchanged.

#### Torque limits (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Force/torque limiting (S7-1500, S7-1500T)](#forcetorque-limiting-s7-1500-s7-1500t)
- [Fixed stop detection (S7-1500, S7-1500T)](#fixed-stop-detection-s7-1500-s7-1500t)
- [Additive setpoint torque/additive setpoint force (S7-1500, S7-1500T)](#additive-setpoint-torqueadditive-setpoint-force-s7-1500-s7-1500t)
- [Permissible torque range/force range (S7-1500, S7-1500T)](#permissible-torque-rangeforce-range-s7-1500-s7-1500t)

##### Force/torque limiting (S7-1500, S7-1500T)

Adjustable force/torque limiting is available for the speed axis, positioning axis and synchronous axis technology objects. The force/torque limiting can be activated and deactivated before and during a motion job. To use force/torque limiting, the drive and the PROFIdrive telegram must support torque reduction. You can use, for example, a telegram 10x.

The limit value can be configured as a default value during configuration of the axis or it can be defined in the user program using motion control instruction "MC_TorqueLimiting**"**.

You can specify the limiting values in the configured measurement unit for force or torque. The measurement units are defined in the "Basic parameters" configuration window.

The following configuration options are available for force/torque limiting:

- **"Linear" axis type**

  - Torque limiting active on motor side
  - Force limit active on load side
- **"Rotary" axis type**

  - Torque limiting active on load side or motor side

The force/torque limit defined by the user in accordance with the specification in the PROFIdrive telegrams 10x are transferred internally to the drive as a percentage torque reduction. The reference torque set in the "Data exchange with the drive" configuration dialog must match the reference torque set for the drive.

**Linear axis type**

With the rotary motor, a load-side force limit you have defined is converted by the technology into a torque reduction. If the limiting relates to the load side, the gear and leadscrew parameters defined in the "Mechanics" configuration dialog are taken into consideration. If the efficiency of the gear and leadscrew is crucial, you can set them in the "<TO>.Actor.Efficiency" tag.

With the linear motor, you specify the load-side force limit directly. The efficiency is not taken into account.

**Rotary axis type**

The torque is reduced on the load side with the rotary axis type. The gear parameters defined in the "Mechanics" configuration window are taken into consideration. If the efficiency of the gear is crucial, you can set it in the "<TO>.Actor.Efficiency" tag.

The defined limiting values act as an absolute value and thus in the same way for positive and negative forces/torques.

###### Positioning and following error monitoring with active force/torque limiting

As a result of force/torque limiting, a larger setpoint-actual value difference can build up for position-controlled axes, which may cause unwanted activation of the positioning and following error monitoring.

To deactivate the monitoring of the following error and the positioning monitoring during force/torque limiting, select the "Disable position-related monitoring" option. If you want to activate the position-related monitoring, select the option "Leave position-related monitoring enabled".

###### Typical behavior of a positioning or synchronous axis with active force/torque limiting

With active force/torque limiting, a larger setpoint-actual value difference can build up than during motion without force/torque limit.

Given a constant setpoint, the axis makes repeated attempts to reduce the following error.

When the limiting values are increased or limiting is deactivated during active closed loop position control, the axis can accelerate briefly to reduce the following error. If the axis is switched to non-position-controlled operation, e.g. using "MC_MoveVelocity" with "PositionControlled" = FALSE, the following error is no longer in effect.

###### Stopping an axis with active force/torque limiting

When stopping an axis in position-controlled mode with "MC_Halt" or "MC_Stop", the set position and the velocity setpoint are applied. Torque limiting still remains active and any accumulated following error is reduced. The axis is in standstill when the actual velocity "0.0" is reached and the minimum dwell time in the standstill window has expired. The axis remains enabled.

When stopping an axis with "MC_Power" and an emergency stop ramp, the actual position value and the actual velocity are used as a basis. The axis is braked with the configured emergency deceleration without any jerk limitation and brought to a standstill. The axis is then disabled when at a standstill.

###### Configuring force/torque limiting

You can configure the force/torque limit in the configuration of the positioning axis/synchronous axis technology object under "Extended parameters > Limits > Torque limiting".

Follow these steps:

1. In the "Effective" drop-down list, select whether the limit value is to be in effect "on load side" or "on motor side".

   If you have configured a linear motor, this setting has no effect.
2. Enter a default value in the specified measurement unit for "Torque limiting" or "Force limit".

   The default value is in effect when the torque limiting or force limit is specified using the motion control instruction "MC_TorqueLimiting", input parameter "Limit" < 0.

   Torque limiting applies to the following axis configurations:

   - Axis type is "Rotary" and limit value is in effect "On load side" or "On motor side"
   - Axis type is "Linear" and limit value is in effect "On motor side"

   Force limit applies to the following axis configuration:

   - "Standard motor", axis type "linear" and limiting value effective "on load side".

     If the efficiency of the gear and leadscrew is crucial, you can set them in the "<TO>.Actor.Efficiency" tag.
   - "Linear motor"

###### Interconnection in the SINAMICS drive

The following interconnection is required in the SINAMICS drive:

- P1522 to a fixed value of 100%
- P1523 to a fixed value of -100% (e.g. through interconnection to fixed value parameter P2902[i])
- P1544 Torque/force reduction evaluation during travel to fixed stop to 100% (default)
- P2194 Threshold value for the parameter "InLimitation" of < 100% (default 90%)

---

**See also**

[Fixed stop detection (S7-1500, S7-1500T)](#fixed-stop-detection-s7-1500-s7-1500t)

##### Fixed stop detection (S7-1500, S7-1500T)

With the Motion Control instruction "MC_TorqueLimiting", you activate and monitor a fixed stop detection. Together with a position-controlled motion job, a "Travel to fixed stop" can be realized. The operation is also referred to as clamping. "Travel to fixed stop" can be used, for example, to move quills against the workpiece with a specified torque.

The fixed stop detection is only possible in position-controlled operation of the axis. If the drive and telegram support force/torque limiting, this is active during travel to fixed stop and for clamping.

###### Detection of the fixed stop using following error

If the drive is stopped by a mechanical fixed stop during a motion job, the following error is increased. When the following error configured in the configuration window "Extended parameters > Limits > Fixed stop detection" is exceeded, this is regarded as the fixed stop having been reached.

When following error monitoring is activated, the configured following error must be greater than the following error for fixed stop detection.

###### Clamping at the mechanical endstop

When the fixed stop is reached, the active position-controlled motion job is canceled with "CommandAborted". The setpoint is no longer changed and the following error remains constant. The closed loop position control remains active and the monitoring of the configured "Positioning tolerance" is activated The drive is in "Clamping" state.

If the drive and telegram support force/torque limiting, this continues to be active with active fixed stop detection. During clamping, the clamping force or clamping torque can be changed. The value in input parameter "Limit" of the Motion Control instruction "MC_TorqueLimiting" can be changed for this.

###### Monitoring of the clamping

If the actual position changes by a value greater than the configured "Positioning tolerance" during active clamping, this is regarded as the break or push-back of the fixed stop. An alarm is triggered. The axis is disabled and the drive is stopped according to its configuration.

If the position setpoint is within the configured "Positioning tolerance", the breaking away or turning back of the fixed stop cannot be detected.

The configured position tolerance must be less than the configured following error for detection of clamping.

###### Retracting

Retracting from the fixed stop is only possible with a position-controlled motion job in the opposite direction to the fixed stop.

The "Travel to fixed stop" or "Clamping" function is ended when the "Positioning tolerance" is left in the retraction direction.

###### Configuring fixed stop detection

You configure the fixed stop detection in the configuration of the Positioning axis/synchronous axis technology object under "Extended parameters > Limits > Fixed stop detection".

- For "Following error", you configure the value of the following error starting from which the fixed stop detection is to take effect.

  > **Note**
  >
  > If the following error monitoring was activated in the position monitoring configuration, the "Maximum following error" configured there must be greater than the "Following error" of the fixed stop detection.
- For "Positioning tolerance", you configure the positioning tolerance that is regarded as a breaking away or turning back of the fixed stop when exceeded. To detect the breaking away or turning back of the fixed stop, the position setpoint must be located outside the positioning tolerance.

  The configured position tolerance must be less than the configured following error.

---

**See also**

[Force/torque limiting (S7-1500, S7-1500T)](#forcetorque-limiting-s7-1500-s7-1500t)
  
[MC_TorqueLimiting: Activate/deactivate force/torque limit / fixed stop detection V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torquelimiting-activatedeactivate-forcetorque-limit-fixed-stop-detection-v8-s7-1500-s7-1500t)

##### Additive setpoint torque/additive setpoint force (S7-1500, S7-1500T)

The Motion Control instruction "MC_TorqueAdditive" allows you to apply an additional torque/an additional force in the drive.

The additive setpoint torque is used for example in torque feedforward control or the specification of the tensile torque for winding applications.

The following requirements are necessary for setting the additive setpoint torque/additive setpoint force:

- SINAMICS drive (see "[compatibility list](https://support.industry.siemens.com/cs/ww/en/view/109750431)")
- SIEMENS supplementary telegram 750 for transmitting the torque data to the drive

The additive torque/additive setpoint force can be either positive or negative. The value specified in the instruction is a technological value, not a percentage. You set the unit of measure at the axis (default values: Nm, N).

---

**See also**

[MC_TorqueAdditive: Specify additive torque V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torqueadditive-specify-additive-torque-v8-s7-1500-s7-1500t)

##### Permissible torque range/force range (S7-1500, S7-1500T)

The Motion Control instruction "MC_TorqueRange" allows you to set torque limits/force limits for the drive.

The motion control instruction is used, for example, for winding applications in order to prevent the tearing of the material.

The following requirements must be fulfilled to set the torque data:

- SINAMICS drive (see "[compatibility list](https://support.industry.siemens.com/cs/ww/en/view/109750431)")
- SIEMENS supplementary telegram 750 for transmitting the torque data to the drive

The value specified in the instruction is a technological value, not a percentage. You set the unit of measure at the axis (default values torque: Nm/force: N). If you invert the setpoints at the technology object of the axis, the values for the high and low torque limit are output inverted and reversed.

If the torque limitation is activated by specifying the high and low torque limit, the following monitorings and limits are deactivated:

- Following error monitoring
- Time limits for positioning monitoring
- Time limits for standstill monitoring

Monitoring remains in effect if you have selected the option "Leave position-related monitoring enabled" under "Technology object > Configuration > Extended parameters > Limits > Torque limiting".

---

**See also**

[MC_TorqueRange: Set high and low torque limit V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torquerange-set-high-and-low-torque-limit-v8-s7-1500-s7-1500t)

#### Superimposed motions (S7-1500, S7-1500T)

With the motion control instructions "MC_MoveSuperimposed" and "MC_MotionInSuperimposed" you can start motions on the axis that additionally superimpose a position-controlled basic motion.

Use the motion control instruction "MC_HaltSuperimposed" to stop a superimposed motion on the axis independently of the basic motion.

You can superimpose the following motion control instructions with the "MC_MoveSuperimposed", "MC_MotionInSuperimposed", and "MC_HaltSuperimposed" motion control instructions:

- Single axis motion

  - MC_MoveAbsolute
  - MC_MoveRelative
  - MC_MoveVelocity
  - MC_MoveJog
- Synchronous operation

  - MC_GearIn
  - MC_GearInPos
  - MC_GearInVelocity
  - MC_CamIn
- MotionIn motion

  - MC_MotionInVelocity
  - MC_MotionInPosition

A kinematics motion is not permitted as a basic motion. If a kinematics motion is active, then the execution of a "MC_MoveSuperimposed" job or a "MC_MotionInSuperimposed" job is aborted with "Error" and the associated "ErrorID".

##### Superimposing a basic motion with a relative positioning motion

With the motion control instruction "[MC_MoveSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movesuperimposed-position-axis-overlapping-v8-s7-1500-s7-1500t)" you can start a relative positioning motion by the "Distance" distance to superimpose a running basic motion.

The dynamic behavior during superimposed motion is defined with the parameters "VelocityDiff", "Jerk", "Acceleration", and "Deceleration". The basic motion is not affected by the superimposed motion.

The dynamic response of the total axis motion is the sum of the dynamic values of the basic motion and the superimposed motion.

The behavior of the overall motion depends on the type of basic motion:

- If the basic motion is a single-axis motion:

  - The maximum dynamic response of the superimposed motion is the difference between the current dynamic values of the basic motion and the dynamic limits.
  - The entire motion is limited to the configured dynamic limits.
- If the basic motion is a synchronous operation:

  - The synchronous operation of the following axis is not limited to the dynamic limits of the following axis.
  - An "MC_MoveSuperimposed" job on a leading axis in synchronous operation affects the leading axis and thus indirectly the following axis.
  - An "MC_MoveSuperimposed" job on a following axis in synchronous operation only affects the following axis.

    > **Note**
    >
    > **Setting synchronous operation with superimposed motions in simulation**
    >
    > If superimposed movements by the motion control instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed" or "MC_HaltSuperimposed" are or were active on the following axis, do not set a synchronous operation in simulation. This is because after you end the simulation, the following axis follows the leading axis without the position shifted by the superimposed motion. This can cause a setpoint jump of the position on the following axis.
    >
    > If you are using synchronous operation, use the motion control instructions "MC_OffsetAbsolute" or "MC_OffsetRelative" to move the following axis position.
- If the basic motion is a MotionIn motion:

  - The dynamic response of the basic motion is not limited.
  - The maximum dynamic response of the superimposed motion is the difference between the current dynamic values of the basic motion and the dynamic limits.

The dynamic response of the overall motion is always displayed in the technology data block and in the diagnostics of the TIA Portal.

**Starting superimposed positioning motion with "**
**MC_MoveSuperimposed**
**"**

To start a superimposed positioning motion with the Motion Control instruction "MC_MoveSuperimposed", follow these steps:

1. Specify the additional distance to be moved in the "Distance" parameter.
2. Start the "MC_MoveSuperimposed" job with a positive edge at the "Execute" parameter.

   The "MC_MoveSuperimposed" job is executed with the set dynamic responses and superimposed on the basic motion.

   The processing status of the job is displayed at the "Busy", "Done", and "Error" parameters.

##### Superimposing basic motion with MotionIn motion specification

You can specify the cyclic, applicable motion setpoints for additional distance, velocity and acceleration, in addition to the basic motion for the axis with the motion control instruction "[MC_MotionInSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninsuperimposed-specify-superimposed-motion-setpoints-v8-s7-1500t)". In this case no velocity profile is calculated and the values are directly active at the technology object.

The additional distance "Distance" is added to the set position of the basic motion. The summation of the two values corresponds to the set position of the axis.

The summation of the velocity setpoint "VelocityDiff" of the superimposed motion and the velocity setpoint of the basic motion are used as the precontroller value for the velocity precontrol.

The superimposed acceleration "AccelerationDiff" is only required for overriding the superimposed or overall motion.

The behavior of the overall motion depends on the type of basic motion:

- If the basic motion is a single-axis motion:

  - The dynamic responses of the superimposed and overall motions are not limited.
  - Only the basic motion is limited to the configured dynamic limits.
  - When the basic motion is completed, a job with "MC_MotionInSuperimposed" continues to be executed.
- If the basic motion is a synchronous operation:

  - The synchronous operation of the following axis is not limited to the dynamic limits of the following axis.
  - An "MC_MotionInSuperimposed" job on a leading axis in synchronous operation affects the leading axis and thus indirectly the following axis.
  - An "MC_MotionInSuperimposed" job on a following axis in synchronous operation only affects the following axis.

    > **Note**
    >
    > **Setting synchronous operation with superimposed motions in simulation**
    >
    > If superimposed movements by the motion control instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed" or "MC_HaltSuperimposed" are or were active on the following axis, do not set a synchronous operation in simulation. This is because after you end the simulation, the following axis follows the leading axis without the position shifted by the superimposed motion. This can cause a setpoint jump of the position on the following axis.
    >
    > If you are using synchronous operation, use the motion control instructions "MC_OffsetAbsolute" or "MC_OffsetRelative" to move the following axis position.
- If the basic motion is a MotionIn motion:

  - The dynamic response of the superimposed motion and the dynamic response of the overall motion are not limited.
  - The dynamic response of the basic motion is not limited.
- No basic motion is active at the axis:

  - A job with "MC_MotionInSuperimposed" is also possible if no basic motion is active.

The dynamic response of the overall motion is always displayed in the technology data block and in the diagnostics of the TIA Portal.

**Starting superimposed motion with "MC_MotionInSuperimposed"**

To start a superimposed positioning motion with the Motion Control instruction "MC_MotionInSuperimposed", follow these steps:

1. Specify the superimposed motion setpoints at the "Distance", "VelocityDiff", and "AccelerationDiff" parameters.
2. Start the "MC_MotionInSuperimposed" job with a positive edge at the "Enable" parameter.

   The "MC_MotionInSuperimposed" job is executed with the dynamic response specified at the "Distance" and "VelocityDiff" parameters and superimposed on the basic motion.

   The processing status of the job is displayed at the "Busy" and "Error" parameters.

##### Stopping superimposed motion independently of the basic motion

The motion control instruction "[MC_HaltSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_haltsuperimposed-pause-superimposed-motions-on-axis-v8-s7-1500-s7-1500t)" stops a superimposed motion created with the instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed", or "MC_HaltSuperimposed".

With the "Jerk", "Deceleration" and "AbortAcceleration" parameters you can determine the dynamic behavior when stopping the superimposed motion.

The motion control instruction "MC_HaltSuperimposed" has no effect on the basic motion of the axis.

If no superimposed motion with "MC_MoveSuperimposed" or "MC_MotionInSuperimposed" is active, then the "MC_HaltSuperimposed" job is aborted immediately without effect. (MC_HaltSuperimposed.Done = true; MC_HaltSuperimposed.Busy = false)

##### Overriding of superimposed motions

The instructions of the superimposed motions are overridden according to the behavior described in the section "[Override response V8: Homing and motion jobs](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-homing-and-motion-jobs-s7-1500-s7-1500t)". As a rule, the current dynamic responses are approximated to the new motion.

##### Status indicators of superimposed motions

The "<TO>.StatusWord.X23 (MoveSuperimposedCommand)" tag is set when the "MC_MoveSuperimposed" job is active.

The "<TO>.StatusWord2.X6 (MotionInSuperimposedCommand)" tag is set when the "MC_MotionInSuperimposed" job is active.

The "<TO>.StatusWord2.X7 (HaltSuperimposedCommand)" tag is set when the "MC_HaltSuperimposed" job is active.

The "<TO>.StatusPositioning.SuperimposedDistance" tag shows the distance traversed with the "MC_MoveSuperimposed", "MC_MotionInSuperimposed", and "MC_HaltSuperimposed" instructions. The value is reset when the basic motion and superimposed motion are completed or aborted.

#### Motion specification via "MotionIn" (S7-1500T)

In contrast to the motion control instructions such as "MC_MoveAbsolute" and "MC_MoveRelative", no motion profile is calculated by the system when "MC_MotionInVelocity", "MC_MotionInPosition", and "MC_MotionInSuperimposed" are used. Each individual setpoint of the motion profile (motion vector) must be specified with the "MotionIn" instruction in the application cycle. This allows you to calculate your own motion profile. You are responsible for the accuracy or your information.

The setpoints are typically adapted in the processing cycle of the technology object. Call the "MotionIn" instruction in the MC_PreInterpolator. The setpoints take effect directly in the next application cycle when the MC_Servo is called to calculate the position controller.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis motions**  When using the motion specification via the motion control instructions "MC_MotionInVelocity", "MC_MotionInPosition", and "MC_MotionInSuperimposed", the axis can perform unexpected motions.  Consider the current dynamic response of the axis when specifying the new motion vectors. The motion vectors must be consistent with each other.  Before operation with the motion control instructions "MC_MotionInVelocity", "MC_MotionInPosition", and "MC_MotionInSuperimposed", set up the following precautionary measures:  - Ensure that the EMERGENCY OFF switch is within the reach of the operator. - Enable the hardware limit switches. - Enable the software limit switches. - Ensure that following error monitoring is enabled.   Note that a following axis that is coupled to the axis is also moved. |  |

##### "MC_MotionInVelocity"

Use the "[MC_MotionInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninvelocity-specify-motion-setpoints-v8-s7-1500t)" instruction to specify the velocity and acceleration of the motion. The instruction is applicable for speed, positioning and constant axes.

To execute the instruction, you must at least specify the velocity. Acceleration is usually only required for the substituting running motions. By default, the acceleration value is zero.

##### "MC_MotionInPosition"

Use the "[MC_MotionInPosition](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninposition-specify-motion-setpoints-v8-s7-1500t)" instruction to specify the position, velocity and acceleration of the motion. This instruction is used for velocity, positioning and synchronous axes.

To execute the instruction, you must at least specify the position and velocity. The acceleration is needed for the overriding of running motions. By default, the acceleration value is zero. The specified setpoints must be consistent with each other.

The position specification is position-controlled. If you use a velocity precontrol, the velocity specification is processed via the velocity precontrol.

##### "MC_MotionInSuperimposed"

With the "[MC_MotionInSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-homing-and-motion-jobs-s7-1500-s7-1500t)" instruction you can specify the additional distance, and the velocity and the acceleration of a superimposed motion of the axis. This instruction is used for velocity, positioning and synchronous axes.

To execute the instruction, you must at least specify the position and velocity. The acceleration is needed for the overriding of running motions. By default, the acceleration value is zero. The specified setpoints must be consistent with each other.

The position specification is position-controlled. If you use a velocity precontrol, the velocity specification is processed via the velocity precontrol.

##### Overriding with "MotionIn" instructions

If a motion control instruction is overridden by a "MotionIn" instruction, the specified setpoints take immediate effect with the current application cycle. The dynamic response results exclusively through the setpoint value specifications of the user program. It is not limited and no smooth transition takes place from the current motion state. Consider the current dynamic response of the axis when specifying the new motion vectors. Note that dynamic limits set on the technology object are not effective. Only limits set on the drive side are in effect.

##### Stopping the "MotionIn" instructions

The "MotionIn" instructions can be canceled by the following means:

- Overriding them with another motion control instruction

  The "MotionIn" instructions are overridden according to the behavior described in the section[Override response V8: Homing and motion jobs](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-homing-and-motion-jobs-s7-1500-s7-1500t). As a rule, the current dynamic responses are approximated to the new motion.

  > **Note**
  >
  > **Deviating dynamic settings**
  >
  > When overriding the active job with a new jerk-limited motion, the current acceleration or deceleration is transferred to the new acceleration/deceleration via the jerk. Depending on the dynamic settings, this may take several application cycles. When the new acceleration or deceleration deviates significantly from the acceleration/deceleration at the time of the override, the transition profile can result in an unexpected axis motion.
  >
  > If such transitions cannot be excluded during acceleration/deceleration, adjust the dynamic settings of your jobs. For example, add a motion that is not jerk-limited with a direct transition to the new acceleration/deceleration. As an alternative, use high jerk values.
  >
  > For MotionIn jobs, the specification of the acceleration is only relevant for overriding the job. When the currently active acceleration is not to be reduced via the jerk, enter the value "0.0" at the "Acceleration" parameter of the MotionIn job.
- Setting the parameter "Enable" to "FALSE"

  If you set "Enable" parameter to "FALSE", the setpoint is immediately set to zero. Note that the dynamic limits set on the technology object are not effective. Only limits set on the drive side are in effect.

##### MotionIn status indicators

The tag "<TO>.StatusMotionIn.FunctionState" = 1 indicates that an "MC_MotionInVelocity" job is active.

The tag "<TO>.StatusMotionIn.FunctionState" = 2 indicates that an "MC_MotionInPosition" job is active.

The tag "<TO>.StatusWord.X31 (MotionInCommand)" is set when a MotionIn job is active.

The "<TO>.StatusWord2.X6 (MotionInSuperimposedCommand)" tag is set when the "MC_MotionInSuperimposed" job is active.

The "<TO>.StatusMotionIn.StatusWord.X0 (MaxVelocityExcceeded)" tag indicates that the configured maximum velocity has been exceeded during a MotionIn job.

The "<TO>.StatusPositioning.SuperimposedDistance" tag shows the distance traversed with the "MC_MoveSuperimposed", "MC_MotionInSuperimposed", and "MC_HaltSuperimposed" instructions. The value is reset when the basic motion and superimposed motion are completed or aborted.

---

**See also**

[MC_MotionInSuperimposed: Specify superimposed motion setpoints V8 (S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninsuperimposed-specify-superimposed-motion-setpoints-v8-s7-1500t)

#### Tags: Motion control and limits for dynamics (S7-1500, S7-1500T)

The following technology object tags are relevant for motion control:

| Status |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.StatusWord | Status indicator for an active motion |  |
| <TO>.Position | Set position |  |
| <TO>.Velocity | Velocity setpoint/speed setpoint |  |
| <TO>.VelocitySetpoint | Specified velocity setpoint/speed setpoint |  |
| <TO>.ActualPosition | Actual position |  |
| <TO>.ActualVelocity | Actual velocity |  |
| <TO>.ActualSpeed | Actual speed of the motor (only with PROFIdrive drive type) |  |
| <TO>.Acceleration | Setpoint acceleration |  |
| <TO>.ActualAcceleration | Actual acceleration |  |
| <TO>.StatusPositioning.SuperimposedDistance | Distance traveled with the instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed", and "MC_HaltSuperimposed".  The value is reset when the base motion and the superimposed motion are completed. |  |
| <TO>.StatusMotionIn.FunctionState | Status of the "MotionIn" function |  |
| 0 | No "MotionIn" function active |  |
| 1 | "MC_MotionInVelocity" active |  |
| 2 | "MC_MotionInPosition" active |  |
| <TO>.StatusMotionIn.StatusWord.X0 (MaxVelocityExceeded) | The configured maximum velocity is exceeded during a MotionIn movement. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X0 (MaxVelocityExceeded) | The tag is set to the value "TRUE" when the maximum velocity configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X1 (MaxAccelerationExceeded) | The tag is set to the value "TRUE" when the maximum acceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X2 (MaxDecelerationExceeded) | The tag is set to the value "TRUE" when the maximum deceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusWord.X23 (MoveSuperimposedCommand) | An "MC_MoveSuperimposed" job is running. |  |
| <TO>.StatusWord.X31 (MotionInCommand) | A "MotionIn" job is active. |  |
| <TO>.StatusWord2.X6 (MotionInSuperimposedCommand) | An "MC_MotionInSuperimposed" job is running. |  |
| <TO>.StatusWord2.X7 (HaltSuperimposedCommand) | An "MC_HaltSuperimposed" job is running. |  |

| Override |  |
| --- | --- |
| Tag | Description |
| <TO>.Override.Velocity | Velocity or speed override |

| Dynamic limit values |  |
| --- | --- |
| Tag | Description |
| <TO>.DynamicLimits.MaxVelocity | Dynamic limitation for maximum velocity (mechanical) |
| <TO>.DynamicLimits.Velocity | Dynamic limitation for maximum velocity (programmable) |
| <TO>.DynamicLimits.MaxAcceleration | Dynamic limitation for maximum acceleration |
| <TO>.DynamicLimits.MaxDeceleration | Dynamic limitation for maximum deceleration |
| <TO>.DynamicLimits.MaxJerk | Dynamic limitation for maximum jerk |

| Dynamic response defaults |  |
| --- | --- |
| Tag | Description |
| <TO>.DynamicDefaults.Velocity | Default velocity |
| <TO>.DynamicDefaults.Acceleration | Default acceleration |
| <TO>.DynamicDefaults.Deceleration | Default deceleration |
| <TO>.DynamicDefaults.Jerk | Default jerk |
| <TO>.DynamicDefaults.EmergencyDeceleration | Emergency deceleration |

| Torque limiting |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.TorqueLimiting.LimitDefaults.Torque | Limiting torque |  |
| <TO>.TorqueLimiting.LimitDefaults.Force | Limiting force |  |
| <TO>.TorqueLimiting.LimitBase | Torque limiting, motor or load side |  |
| 0 | Motor side |  |
| 1 | Load side |  |
| <TO>.TorqueLimiting.PositionBasedMonitorings | Positioning and following error monitoring |  |
| 0 | Deactivated |  |
| 1 | Enabled |  |
| <TO>.StatusTorqueData.CommandAdditiveTorqueActive | Additive setpoint torque/additive force function |  |
| 0 | Deactivated |  |
| 1 | Enabled |  |
| <TO>.StatusTorqueData.CommandTorqueRangeActive | Torque limits/force limits function |  |
| 0 | Deactivated |  |
| 1 | Enabled |  |
| <TO>.StatusTorqueData.ActualTorque | Actual torque of the axis (for standard motor) |  |
| <TO>.StatusTorqueData.ActualForce | Actual force of axis (for linear motor) |  |

| Fixed stop detection |  |
| --- | --- |
| Tag | Description |
| <TO>.Clamping.FollowingErrorDeviation | Value of the following error starting from which the fixed stop is detected |
| <TO>.Clamping.PositionTolerance | Position tolerance for clamping monitoring |

| Alarm response |  |
| --- | --- |
| Tag | Description |
| <TO>.Actor.RemoveEnableReaction | Stop modes of the drive for the alarm response "Remove enable":  - OFF1 - OFF2 - OFF3 |

### Traversing range limitation (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Options for limiting the traversing range (S7-1500, S7-1500T)](#options-for-limiting-the-traversing-range-s7-1500-s7-1500t)
- [Behavior when approaching and retracting a HW limit switch (S7-1500, S7-1500T)](#behavior-when-approaching-and-retracting-a-hw-limit-switch-s7-1500-s7-1500t)
- [Configuring HW limit switches (S7-1500, S7-1500T)](#configuring-hw-limit-switches-s7-1500-s7-1500t)
- [Behavior when reaching the SW limit switch (S7-1500, S7-1500T)](#behavior-when-reaching-the-sw-limit-switch-s7-1500-s7-1500t)
- [Retracting the SW limit switch (S7-1500, S7-1500T)](#retracting-the-sw-limit-switch-s7-1500-s7-1500t)
- [Configuring SW limit switches (S7-1500, S7-1500T)](#configuring-sw-limit-switches-s7-1500-s7-1500t)
- [Tags: Traversing range limitation (S7-1500, S7-1500T)](#tags-traversing-range-limitation-s7-1500-s7-1500t)
- [Long-term accuracy (S7-1500, S7-1500T)](#long-term-accuracy-s7-1500-s7-1500t)

#### Options for limiting the traversing range (S7-1500, S7-1500T)

Hardware and software limit switches limit the permissible traversing range and operating range of the positioning axis/synchronous axis. Before use, they must be enabled in the configuration or in the user program.

The following figure shows the relationship between the operating range, maximum traversing range and limit switches:

![Figure](images/165572966795_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Mechanical endstop |
| ② | Hardware limit switch (HW limit switch) |
| ③ | Software limit switch (SW limit switch) |
| ④ | Maximum traversing range |
| ⑤ | Operating range |

##### Types of HW limit switches

The positioning axis/synchronous axis technology object supports the following types of HW limit switches.

- Switch traversable: Axis can move beyond HW limit switch. The HW limit switch is enabled when it is approached. When it is overtraveled, the HW limit switch is disabled once again.

  ![Types of HW limit switches](images/165572972427_DV_resource.Stream@PNG-de-DE.png)
- Switch non-traversable: HW limit switch covers the entire range all the way to the mechanical endstop. The HW limit switch is enabled when it is approached and stays enabled up to the mechanical endstop.

  ![Types of HW limit switches](images/165573003147_DV_resource.Stream@PNG-de-DE.png)

#### Behavior when approaching and retracting a HW limit switch (S7-1500, S7-1500T)

Hardware limit switches are limit position switches that limit the maximum permissible traversing range of the axis.

Select the mounting positions of the hardware limit switches so that there is adequate braking distance for the axis when needed. The axis should come to a standstill before a mechanical endstop.

##### Approaching the hardware limit switches

In the monitoring of range limitation, no distinction is made as to whether the switches are reached or crossed.

When a traversable hardware limit switch is approached, technology alarm 531 is output. The axis is disabled and stopped with the configured braking ramp.

When a non-traversable hardware limit switch is approached, technology alarm 531 is output and the configured alarm response is executed.

##### Using the hardware limit switches as reversing output cams during active homing

When hardware limit switches are used as reversing output cams during homing, monitoring of the hardware limit switches has no effect during active homing.

When hardware limit switches are used as reversing output cams, the axis is braked with the deceleration configured in the dynamic defaults.

When planning the distance between hardware limit switch and mechanical endstop during active homing, take into account the dynamic default of the deceleration and the approach velocity.

[Direction reversal at the hardware limit switch (reversing output cam)](#direction-reversal-at-the-hardware-limit-switch-reversing-output-cam-s7-1500-s7-1500t)

##### Retracting the axis with a traversable HW limit switch

In case of a traversable HW limit switch, the position of the axis when the hardware limit switch is detected is stored internally on the CPU. The status of the reached hardware limit switch is reset only after the hardware limit switch is left and the axis is once again in the maximum traversing range.

To retract the axis after it reaches the hardware limit switch and to reset the status of the hardware limit switch, follow the steps below:

1. To enable movements in the retraction direction, acknowledge the technology alarm with "MC_Reset". A restart is not required.
2. Move the axis in the retraction direction until the hardware limit switch is exited.

   - Negative HW limit switch: For retracting, move in the direction of higher position values.
   - Positive HW limit switch: For retracting, move in the direction of lower position values.

   Afterwards, the axis must be within the maximum traversing range.

   If you move the axis opposite the retraction direction before the hardware limit switch is exited, the monitoring is triggered again.

The following diagram shows the behavior of the status word when the hardware limit switch is approached and when the axis is retracted:

![Retracting the axis with a traversable HW limit switch](images/165623466251_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| ① | <TO>.StatusWord.X17 (HWLimitMinActive) |  |
| 0 | Negative hardware limit switch not reached |  |
| 1 | Negative hardware limit switch reached or overtraveled |  |
| ② | <TO>.StatusWord.X18 (HWLimitMaxActive) |  |
| 0 | Positive hardware limit switch not reached |  |
| 1 | Positive hardware limit switch reached or overtraveled |  |
| ③ | The position of the axis when the **positive** hardware limit switch is detected is saved internally in the CPU. To reset the status of the hardware limit switch, the axis position must fall short of this position. |  |
| ④ | The position of the axis when the **negative** hardware limit switch is detected is saved internally in the CPU. To reset the status of the hardware limit switch, the axis position must go past this position. |  |

> **Note**
>
> **Retracting after technology alarm 531 with polarity-reversed HW limit switch or both HW limit switches active**
>
> To enable retraction, you can temporarily disable the hardware limit switches with Motion Control instruction "[MC_WriteParameter](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-write-parameter-v8-s7-1500-s7-1500t)" using parameter "PositionLimits_HW.Active" = FALSE.

##### Retracting the axis with a non-traversable HW limit switch

In case of a non-traversable HW limit switch, the position of the axis when the hardware limit switch is approached is not stored.

To retract the axis after it reaches the hardware limit switch and to reset the status of the hardware limit switch, follow the steps below:

1. To enable movements in the retraction direction, acknowledge the technology alarm with "MC_Reset". A restart is not required.
2. Move the axis in the retraction direction until the hardware limit switch is exited.

   - Negative HW limit switch: For retracting, move in the direction of higher position values.
   - Positive HW limit switch: For retracting, move in the direction of lower position values.

   The status of the approached HW limit switch is reset as soon as the configured level is no longer present at the digital input of the HW limit switch.

   If you move the axis opposite the retraction direction before the hardware limit switch is exited, the monitoring is triggered again.

The following diagram shows the behavior of the status word when the hardware limit switch is approached and when the axis is retracted:

![Retracting the axis with a non-traversable HW limit switch](images/165623766923_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| ① | <TO>.StatusWord.X17 (HWLimitMinActive) |  |
| 0 | Negative hardware limit switch not reached |  |
| 1 | Negative hardware limit switch reached or overtraveled |  |
| ② | <TO>.StatusWord.X18 (HWLimitMaxActive) |  |
| 0 | Positive hardware limit switch not reached |  |
| 1 | Positive hardware limit switch reached or overtraveled |  |
| ③ | When the **positive** hardware limit switch is detected, the status "<TO>.StatusWord.X18 (HWLimitMaxActive)" is set for the positive HW limit switch. The status is reset as soon as the configured level at the digital input of the HW limit switch is no longer present. |  |
| ④ | When the **negative** hardware limit switch is detected, the status "<TO>.StatusWord.X17 (HWLimitMinActive)" is set for the positive HW limit switch. The status is reset as soon as the configured level at the digital input of the HW limit switch is no longer present. |  |

> **Note**
>
> **Retracting after technology alarm 531 with polarity-reversed HW limit switch or both HW limit switches active**
>
> To enable retraction, you can temporarily disable the hardware limit switches with Motion Control instruction "[MC_WriteParameter](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-write-parameter-v8-s7-1500-s7-1500t)" using parameter "PositionLimits_HW.Active" = FALSE.

##### Deactivating the hardware limit switch

For example, to enable homing at the fixed stop, you can temporarily disable the hardware limit switches with Motion Control instruction "[MC_WriteParameter](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-write-parameter-v8-s7-1500-s7-1500t)" using parameter "PositionLimits_HW.Active" = FALSE.

---

**See also**

[MC_WriteParameter: Write parameter V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-write-parameter-v8-s7-1500-s7-1500t)
  
[Direct homing (S7-1500, S7-1500T)](#direct-homing-s7-1500-s7-1500t-1)

#### Configuring HW limit switches (S7-1500, S7-1500T)

##### Configuring HW limit switches

To configure the HW limit switches for the positioning axis/synchronous axis technology object, follow these steps:

1. In the configuration, navigate to "Extended parameters > Limits > Position limits > HW limit switches".
2. Click on the "Enable HW limit switch" check box.

   The function of the negative and positive hardware limit switch is active.
3. Select the type of HW limit switch from the "Type of hardware limit switch" drop-down list:

   - Switch traversable
   - Switch non-traversable
4. If you have selected "Switch non-traversable", configure the alarm response of technology alarm 531 at "Reaction":

   - Keep emergency stop and axis enable: When approaching the HW limit switch, the axis brakes to a standstill with the emergency stop deceleration without jerk limitation. The axis remains enabled.
   - Disable axis: When approaching the HW limit switch, the axis is stopped with the braking ramp configured in the drive.
5. For "Input negative HW limit switch", select the PLC tag of the digital input for the negative hardware limit switch.

   To be able to select an input, a digital input module must have been added in the device configuration, and the PLC tag name for the digital input must be defined.

   > **Note**
   >
   > Only use hardware limit switches that remain permanently switched after the approach. This switching state may only be canceled after the return to the permitted traversing range.
   >
   > The digital inputs of the hardware limit switches are evaluated by default in cyclic data exchange. If the hardware limit switches are to be evaluated in the position control cycle clock of the drive, select the entry "MC_Servo" for "Organization block" and "PIP OB Servo" for "Process image" in the settings of the input module under "I/O addresses".

   | Symbol | Meaning |
   | --- | --- |
   |  | **Caution** |
   | **Filter times of the digital inputs**  Pay attention to the filter times of the digital inputs when placing hardware limit switches.  Based on the time for one position control cycle clock and the filter time of the digital inputs, the resulting delay times must be taken into account.  The filter time is configurable in individual digital input modules in the device configuration.  The digital inputs are set to a filter time of 6.4 ms by default. If these are used as hardware limit switches, undesired decelerations may occur. If this occurs, reduce the filter time for the relevant digital inputs.  The filter time can be set under "Input filter" in the device configuration of the digital inputs. |  |
6. For "Input positive HW limit switch", select the PLC tag of the digital input for the positive hardware limit switch.

   To be able to select an input, a digital input module must have been added in the device configuration, and the PLC tag name for the digital input must be defined.
7. In the "Level selection negative HW limit switch" drop-down list, select the triggering signal level for the negative HW limit switch.

   - High level: Input signal is "TRUE" when the hardware limit switch is approached.
   - Low level: Input signal is "FALSE" when the hardware limit switch is approached.
8. For "Level selection positive HW limit switch", select the triggering signal level for the positive HW limit switch from the drop-down list.

##### Interconnecting inputs for HW limit switches with Boolean tags

Instead of using digital inputs, you can also use Boolean tags to control the HW limit switches. For this, create a data block with the tags without the "Optimized block access" attribute.

Specify the addresses of these Boolean tags in the technology object data block.

**Defining a data block for switching the HW limit switches**

Proceed as follows to define the Boolean tags as HW limit switches:

1. Create a data block without the "Optimized block access" attribute, e.g. "HWLimitSwitches".
2. Define the following tags in the data block:

   | Name | Data type | Offset | Start value | Comment |
   | --- | --- | --- | --- | --- |
   | UserData | DWord | 0.0 | 16#0 | Random data |
   | HwLimitNeg | Bool | 4.0 | 0 | Tag for negative HW limit switch |
   | HwLimitPos | Bool | 4.1 | 0 | Tag for positive HW limit switch |
3. Use the "HwLimitPos" and "HwLimitNeg" tags in the user program to switch the HW limit switches.

**Interconnecting the addresses of the Boolean tags in the technology object**

To connect the HW limit switch to the address, follow these steps:

1. Open the Parameter view of the technology object.
2. Change the navigation structure to data structure.
3. Open the "PositionLimits_HW" structure.
4. Enter the values for the tags:

   | Name | Data type | Start value | Comment |
   | --- | --- | --- | --- |
   | Active | Bool | false | Hardware switches have to be deactivated for download |
   | MinSwitchAddressRid | DWord | 33554433 | RID for data type Boolean |
   | MinSwitchAddressArea | Byte | 132 | DB memory area |
   | MinSwitchAddressDbNumber | UInt | n | n = number of DB "HWLimitSwitches" |
   | MinSwitchAddressOffset | UDint | 32 | Example in DB "HWLimitSwitches":  Offset Boolean tag ("HwLimitNeg") = 4.0  Offset = (4 bytes x 8 bits/byte) + 0 bits = 32 bits |
   | MaxSwitchAddressRid | DWord | 33554433 | RID for data type Boolean |
   | MaxSwitchAddressArea | Byte | 132 | DB memory area |
   | MaxSwitchAddressDbNumber | UInt | n | n = number of DB "HWLimitSwitches" |
   | MaxSwitchAddressOffset | UDint | 33 | Example in DB "HWLimitSwitches"  Offset Boolean tag ("HwLimitPos") = 4.1  Offset = (4 bytes x 8 bits/byte) + 1 bit = 33 bits |

   Result: The addresses of the HW limit switches are configured. The hardware limit switches are deactivated.
5. Download the project to the CPU.
6. Enable the hardware limit switches in the user program using the "MC_WriteParameter" instruction with "parameter" = 1000 and "Value" = true.

   Result: The hardware limit switches with the configured DB variables are now active.

   Note that after restarting the CPU, you need to execute the "MC_WriteParameter" instruction again..

**Writing addresses of the Boolean tags in the user program**

To connect the HW limit switch to the address during runtime, follow these steps:

1. Create a data block with the "Optimized block access" attribute, e.g. "HWPositionLimitsAdress".
2. Define the following tags in the data block:

   | Name | Data type | Start value | Comment |
   | --- | --- | --- | --- |
   | MinSwitchAddressRid | DWord | 16#0200_0001 | RID for data type Boolean |
   | MinSwitchAddressArea | Byte | 16#84 | DB memory area |
   | MinSwitchAddressDbNumber | UInt | n | n = number of DB "HWLimitSwitches" |
   | MinSwitchAddressOffset | UDint | 32 | Example in DB "HWLimitSwitches":  Offset Boolean tag ("HwLimitNeg") = 4.0  Offset = (4 bytes x 8 bits/byte) + 0 bits = 32 bits |
   | MaxSwitchAddressRid | DWord | 16#0200_0001 | RID for data type Boolean |
   | MaxSwitchAddressArea | Byte | 16#84 | DB memory area |
   | MaxSwitchAddressDbNumber | UInt | n | n = number of DB "HWLimitSwitches" |
   | MaxSwitchAddressOffset | UDint | 33 | Example in DB "HWLimitSwitches"  Offset Boolean tag ("HwLimitPos") = 4.1  Offset = (4 bytes x 8 bits/byte) + 1 bit = 33 bits |
3. Write the start values for each variable from the data block to the load memory of the "<TO>.PositionLimits_HW.MaxSwitchAddress" and "<TO>.PositionLimits_HW.MinSwitchAddress" variable with the "WRIT_DBL" instruction.

   You can find more information on changing restart-relevant data in the technology object in section "Changing restart-relevant data" of function manual "S7-1500/S7-1500T Motion Control Overview".

   Example of the tag "<TO>.PositionLimits_HW.MinSwitchAddress.RID":

   `tempRetVal := WRIT_DBL`

   `(REQ := execute,`

   `SRCBLK := "HWPositionLimitsAdress".MinSwitchAddressRid,`

   `BUSY => busy,`

   `DSTBLK =>`

   `<TO>.PositionLimits_HW.MinSwitchAddress.RID);`

   Repeat the call of the "WRIT_DBL" instruction for the remaining 7 variables in the data block.
4. Perform a restart of the technology object.

   Result: The Boolean tag is used as the input for the HW limit switch.
5. Enable the hardware limit switches in the user program using the "MC_WriteParameter" instruction with "parameter" = 1000 and "Value" = true.

   Result: The hardware limit switches with the configured DB variables are now active.

   Note that after restarting the CPU, you need to execute the "MC_WriteParameter" instruction again.

---

**See also**

[MC_WriteParameter: Write parameter V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-write-parameter-v8-s7-1500-s7-1500t)
  
[Change restart-relevant data (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#change-restart-relevant-data-s7-1500-s7-1500t)

#### Behavior when reaching the SW limit switch (S7-1500, S7-1500T)

The operating range of the axis is limited with software limit switches. Relative to the traversing range, always position the software limit switches within the hardware limit switches. Since the positions of the software limit switches can be flexibly configured, the operating range of the axis can be individually adapted in accordance with the current velocity profile.

During motion control, cyclic checks are carried out taking into consideration the current dynamic values to ensure that the software limit switches are not exceeded. If this is the case, the current movement is interrupted and the software limit switch is approached.

When software switches are activated, an active motion comes to a stop at the position of the software limit switch. The technological object signals an error. After acknowledgment of the error, the axis can again be moved in the direction of its operating range.

Software limit switches are only in effect when there is a valid actual value after homing the technology object. The monitoring of the software limit switches is relative to the setpoint.

##### Approaching the software limit switches

When the software limit switch is approached, technology alarm 533 is output.

You can configure the alarm response for approaching the SW limit switches.

The technology object remains enabled.

##### Overrun of the software limit switches

If the software limit switches are overshot, technology alarm 534 is output.

You can configure the alarm response for crossing the SW limit switches.

##### Modulo function is enabled

When the modulo function is enabled, the modulo position is monitored.

The software limit switches are configured and activated in the axis configuration. The software limit switches can be activated or deactivated in the user program using the "<TO>.PositionLimits_SW.Active" tag. If the positions of both software limit switches are outside the modulo range, the monitoring has no effect. No check is made to determine whether the positions of the software limit switches are within the modulo range.

If a software limit switch is active within the valid Modulo range, the system places the second software limit switch at the corresponding Modulo boundary.

#### Retracting the SW limit switch (S7-1500, S7-1500T)

To retract the axis after violation of the software limit switch, follow the steps below:

1. Acknowledge the technology alarm.
2. Move the axis in the retraction direction into the permitted operating range.

   - Negative SW limit switch: For retracting, move in the direction of positive position values.
   - Positive SW limit switch: For retracting, move in the direction of negative position values.

   If the axis is outside the valid traversing range, e.g. due to homing, the current position is the effective SW limit switch. As soon as the axis has been moved back into the valid traversing range, the configured SW limit switch takes effect.

   If you overtravel the effective SW limit switch in the opposite retraction direction, technology alarm 533 or 534 is issued.

#### Configuring SW limit switches (S7-1500, S7-1500T)

To configure the SW limit switches for the positioning axis/synchronous axis technology object, follow these steps:

1. In the configuration, navigate to "Extended parameters > Limits > Position limits > SW limit switches".
2. Click the check box "Enable SW limit switches".  
   The function of the negative and positive SW limit switch is active.

   > **Note**
   >
   > Activated software limit switches act only on a homed axis.
3. For "Position negative SW limit switch", configure the position of the SW limit switch with the smaller position value.
4. For "Position positive SW limit switch", configure the position of the SW limit switch with the higher position value.
5. For "Reaction when a SW limit switch is reached", configure the alarm response of the technology alarm 533.

   - Stop with maximum dynamic values: The axis stops when the SW limit switch is approached with maximum dynamic values.
   - Stop with current dynamic values: The axis stops when the SW limit switch is approached with the programmed dynamic values of the active job.
   > **Note**
   >
   > If the axis approaches the software limit switch as a following axis in synchronous operation or as a kinematics axis during a kinematic movement, the axis is stopped with maximum dynamic values regardless of the selected setting.

   The technology object remains enabled.
6. For "Reaction when a SW limit switch is exceeded", configure the alarm response of the technology alarm 534:

   - Keep emergency stop and axis enable: When the software limit switch is overtraveled, the axis brakes to a standstill with the emergency stop deceleration without jerk limitation. The axis remains enabled.
   - Disable axis: The axis is disabled when the SW limit switch is overtraveled and is braked with the braking ramp configured in the drive.

#### Tags: Traversing range limitation (S7-1500, S7-1500T)

##### Software limit switches

The following technology object tags are relevant for software limit switches:

| Status indicators |  |
| --- | --- |
| Tag | Description |
| <TO>.StatusWord.X15 (SWLimitMinActive) | Negative software limit switch is active. |
| <TO>.StatusWord.X16 (SWLimitMaxActive) | Positive software limit switch is active. |
| <TO>.ErrorWord.X8 (SWLimit) | An alarm is pending, indicating that a software limit switch has been violated. |

| Control bits |  |
| --- | --- |
| Tag | Description |
| <TO>.PositionLimits_SW.Active | Enables/disables the monitoring of the software limit switches. |

| Position values |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.PositionLimits_SW.MinPosition | Position of the negative software limit switch |  |
| <TO>.PositionLimits_SW.MaxPosition | Position of the positive software limit switch |  |
| <TO>.PositionLimits_SW.LimitReachedBehavior | Alarm response when a software limit switch is approached with a single axis job |  |
| 0 | Stop axis with maximum dynamics |  |
| 1 | Stop axis with the programmed dynamic parameters |  |
| <TO>.PositionLimits_SW.LimitExceededBehavior | Alarm response when overrunning a software limit switch |  |
| 0 | Disable axis |  |
| 1 | Brake the axis with the configured emergency stop deceleration without any jerk limitation and bring it to a standstill. |  |

##### Hardware limit switches

The following technology object tags are relevant for hardware limit switches:

| Status indicators |  |
| --- | --- |
| Tag | Description |
| <TO>.StatusWord.X17 (HWLimitMinActive) | Negative hardware limit switch is active. |
| <TO>.StatusWord.X18 (HWLimitMaxActive) | Positive hardware limit switch is active. |
| <TO>.ErrorWord.X9 (HWLimit) | An alarm is pending. A hardware limit switch was reached. |

| Control bits |  |
| --- | --- |
| Tag | Description |
| <TO>.PositionLimits_HW.Active | Enables/disables the monitoring of the hardware limit switches. |

| Parameters |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.PositionLimits_HW.MinSwitchLevel | Level selection for activation of the low hardware limit switch |  |
| FALSE | At low level, the signal is active. |  |
| TRUE | At high level, the signal is active. |  |
| <TO>.PositionLimits_HW.MinSwitchAddress | Address for the negative hardware limit switch |  |
| <TO>.PositionLimits_HW.MaxSwitchLevel | Level selection for activation of the high hardware limit switch |  |
| FALSE | At low level, the signal is active. |  |
| TRUE | At high level, the signal is active. |  |
| <TO>.PositionLimits_HW.MaxSwitchAddress | Address for the positive hardware limit switch |  |
| <TO>.PositionLimits_HW.Mode | Type of HW limit switch |  |
| 0 | The HW limit switches are non-traversable. |  |
| 1 | The HW limit switches are mechanically traversable. |  |
| <TO>.PositionLimits_HW.ApproachBehavior | Alarm response when approaching a HW limit switch |  |
| 0 | Disable axis |  |
| 1 | Keep emergency stop and axis enable |  |

#### Long-term accuracy (S7-1500, S7-1500T)

Long-term accuracy means that the technological set and actual position can always be determined uniquely.

The maximum technological position depends on the selected unit of measure and the maximum display of 9.0E12 mm. At higher resolution the maximum display is reduced to 9.0E9 mm.

The maximum travel time in which the technological position is accurate without rounding error depends on the maximum position and the velocity. The maximum travel time applies likewise to axes with and without modulo setting.

You can use the following equation to estimate when the limit of long-term accuracy is reached:

![Figure](images/165623957899_DV_resource.Stream@PNG-en-US.png)

##### Example of the maximum traversing time

Maximum position = 9.0E12 mm

Velocity = 20.0 m/min = 2.0E4 mm/min

![Example of the maximum traversing time](images/165623772811_DV_resource.Stream@PNG-en-US.png)

| Unit of measure | Maximum travel time |
| --- | --- |
| nm, µm, mm, m, km, in, ft, mi, rad, ° | 4.5E8 min ≙ 856 years |
| mm<sup>1)</sup>, °<sup>1)</sup> | 4.5E5 min ≙ 0.856 years |
| <sup>1)</sup> Position values with higher resolution or six decimal places. The maximum position is reduced to 9.0E9 mm and thus also the travel time. |  |

A change in the velocity has the consequence that the traversing time changes accordingly.

##### Measures to maintain long-term accuracy

To reset the travel time, carry out the following measures before the maximum travel time has expired or before reaching the maximum position:

- Incremental encoder: Home the incremental encoder again.
- Absolute encoder: Perform an absolute encoder adjustment with the default of the currently known position.

---

**See also**

[Units of measure (S7-1500, S7-1500T)](#units-of-measure-s7-1500-s7-1500t)

### Homing (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of homing (S7-1500, S7-1500T)](#short-description-of-homing-s7-1500-s7-1500t)
- [Terms for active and passive homing (S7-1500, S7-1500T)](#terms-for-active-and-passive-homing-s7-1500-s7-1500t)
- [Homing mode for active and passive homing (S7-1500, S7-1500T)](#homing-mode-for-active-and-passive-homing-s7-1500-s7-1500t)
- [Active homing (S7-1500, S7-1500T)](#active-homing-s7-1500-s7-1500t)
- [Passive homing (S7-1500, S7-1500T)](#passive-homing-s7-1500-s7-1500t)
- [Direct homing (S7-1500, S7-1500T)](#direct-homing-s7-1500-s7-1500t)
- [Set setpoint position (S7-1500, S7-1500T)](#set-setpoint-position-s7-1500-s7-1500t)
- [Absolute value adjustment (S7-1500, S7-1500T)](#absolute-value-adjustment-s7-1500-s7-1500t)
- [Save data on the SIMATIC Memory Card (S7-1500, S7-1500T)](#save-data-on-the-simatic-memory-card-s7-1500-s7-1500t)
- [Incremental encoder adjustment (S7-1500, S7-1500T)](#incremental-encoder-adjustment-s7-1500-s7-1500t)
- [Homing SINAMICS drives with external zero marks (S7-1500, S7-1500T)](#homing-sinamics-drives-with-external-zero-marks-s7-1500-s7-1500t)
- [Homing when backlash compensation is enabled (S7-1500, S7-1500T)](#homing-when-backlash-compensation-is-enabled-s7-1500-s7-1500t)
- [Resetting the "Homed" status (S7-1500, S7-1500T)](#resetting-the-homed-status-s7-1500-s7-1500t)
- [Tags: Homing (S7-1500, S7-1500T)](#tags-homing-s7-1500-s7-1500t)

#### Short description of homing (S7-1500, S7-1500T)

With homing, you create the relationship between the position in the technology object and the mechanical position. The actual position value in the technology object is assigned to a homing mark at the same time. This homing mark represents a known mechanical position.

Homing is a requirement for display of the correct position for the technology object and for absolute positioning.

##### Type of homing

Homing can occur by means of an independent homing motion (active homing), the detection of a homing mark during a motion initiated (passive homing) or a direct position assignment.

You select the homing type via the "Mode" parameter of the "[MC_Home](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_home-home-technology-object-set-home-position-v8-s7-1500-s7-1500t)" instruction.

A distinction is made between the following types of homing:

- **Active homing**

  Active homing initiates a homing movement and performs the necessary homing mark approach. When the homing mark is detected, the actual position is set to the value specified in "MC_Home". It is possible to specify a home position offset. Retraction to the home position offset occurs automatically during the home position approach.

  Active homing has an effect on the operative encoder.

  When active homing starts, current traversing movements are aborted.

  If a valid absolute value offset has not yet been saved (<TO>.Sensor[1..4].Adjusted = FALSE), then an absolute value offset is saved during active homing with absolute encoder and retained beyond the switching on/off of the controller. If an absolute value offset has already been saved in the CPU (<TO>.Sensor[1..4].Adjusted = TRUE), it is retained after active homing. To update the absolute encoder offset, perform an absolute encoder adjustment to the current position after the active homing.

  [Active homing](#active-homing-s7-1500-s7-1500t)
- **Passive homing**

  The homing job does not perform its own homing motion. When the homing mark is detected during a motion initiated on the user side, the actual position is set to the value specified in "MC_Home".

  Passive homing has an effect on the operative encoder.

  Passive homing is also called homing on the fly.

  If a valid absolute value offset has not yet been saved (<TO>.Sensor[1..4].Adjusted = FALSE), then an absolute value offset is saved during passive homing with absolute encoder and retained beyond the switching on/off of the controller. If an absolute value offset has already been saved in the CPU (<TO>.Sensor[1..4].Adjusted = TRUE), it is retained after passive homing. To update the absolute encoder offset, perform an absolute encoder adjustment to the current position after the passive homing.

  [Passive homing](#passive-homing-s7-1500-s7-1500t)
- **Direct homing**

  With the homing job, the actual position is set directly to the value specified in "MC_Home" or is offset by this value.

  [Direct homing](#direct-homing-s7-1500-s7-1500t)
- **Set position setpoint**

  The set position of the technology object is set or offset directly to the value specified in "MC_Home". The following error remains.

  [Set setpoint position](#set-setpoint-position-s7-1500-s7-1500t)
- **Absolute encoder adjustment**

  The supplied absolute value is assigned to the associated mechanical axis position by means of the absolute encoder adjustment. You carry out the absolute encoder adjustment once. The absolute value offset is retentively saved beyond the switching on/off of the controller.

  [Absolute value adjustment](#absolute-value-adjustment-s7-1500-s7-1500t)
- **Incremental encoder adjustment**

  With the homing job, the actual position is set directly to the value specified in "MC_Home".

  [Incremental encoder adjustment](#incremental-encoder-adjustment-s7-1500-s7-1500t)

##### Supported encoders and technology objects

The following table shows which homing types are possible with the respective technology objects:

| Type of homing | Positioning axis/synchronous axis with incremental encoder | Positioning axis/synchronous axis with absolute encoder | External encoder incremental | External encoder absolute |
| --- | --- | --- | --- | --- |
| Active homing  ("Mode" = 3, 5) | ✓ | ✓ | - | - |
| Passive homing   ("Mode" = 2, 8, 10) | ✓ | ✓ | ✓ | ✓ |
| Set actual position  ("Mode" = 0)  Relative offset to the actual position  ("Mode" = 1) | ✓ | ✓ | ✓ | ✓ |
| Set position setpoint (direct absolute)  ("Mode" = 11)  Relative offset of the position setpoint  ("Mode" = 12) | ✓ | ✓ | ✓ | ✓ |
| Absolute encoder adjustment  ("Mode" = 6, 7) | - | ✓ | - | ✓ |
| Incremental encoder adjustment  ("Mode" = 13) | ✓ | - | ✓ | - |

##### Start homing job

To start the homing job, activate the Motion Control instruction "MC_Home".

##### Homing status

The "<TO>.StatusWord.X5 (HomingDone)" tag of the technology object indicates whether the technology object axis or external encoder is homed.

The "<TO>.StatusWord.X11 (HomingCommand)" tag of the technology object indicates that a homing job is active.

The "<TO>.ErrorWord.X10 (HomingFault)" tag of the technology object indicates an error during homing.

The "<TO>.StatusSensor[1..4].Adjusted" tag shows whether the encoder is homed with one of the following homing types:

- Active homing
- Passive homing
- Absolute encoder adjustment
- Incremental encoder adjustment

> **Note**
>
> Once the tag "<TO>.StatusSensor[1..4].Adjusted" is set for an absolute encoder, it remains set until you download new settings for the encoder.
>
> Home the axis again when replacing the absolute encoder.

After homing with the homing types Direct homing ("Mode" = 0,1) and Setting of position setpoint ("Mode" = 11,12) is completed, the "<TO>.StatusWord.X5 (HomingDone)" tag of the axis or external encoder technology object is set, but not the "<TO>.StatusSensor[1..4].Adjusted" tag of the encoder.

---

**See also**

[Homing SINAMICS drives with external zero marks (S7-1500, S7-1500T)](#homing-sinamics-drives-with-external-zero-marks-s7-1500-s7-1500t)

#### Terms for active and passive homing (S7-1500, S7-1500T)

##### Homing mark

A homing mark is an input signal, on whose occurrence a known mechanical position can be assigned to the actual values.

A homing mark can be:

- **A zero mark**

  The zero mark of an incremental encoder or an external zero mark is used as a homing mark.

  The zero mark is detected at the drive module or encoder module and transmitted in the PROFIdrive telegram. Perform the setting and evaluation as an encoder zero mark or external zero mark at the drive module and encoder module.
- **An edge at the digital input**

  The negative or positive edge at a digital input is used as a homing mark.

##### Reference output cam

If there are several zero marks in the traversing range, the reference output cam is used to select a specific zero mark before or after the reference output cam.

##### Homing mark position

This is the position assigned to the homing mark.

With active homing, the homing mark position corresponds to the home position minus home position offset.

With passive homing, the homing mark position corresponds to the home position.

##### Home position

At the end of the active homing motion, the axis arrives at the home position.

##### Home position offset

The difference between the home position and the homing mark position is the home position offset.

A home position offset only has an effect with active homing. The offset is traversed after the synchronization of the axis using the Motion Control instruction "MC_Home". For axes with modulo setting, the home position offset is always traversed with the direction setting for the shortest path.

##### Direction reversal at the hardware limit switch (reversing output cam)

Hardware limit switches can be used as reversing output cams in active homing. If the homing mark was not detected or was approached from the wrong side, the motion continues in the opposite direction after the reversing output cam.

##### Approach velocity

With active homing, the technology object approaches the reference output cam/digital input at the approach velocity.

A home position offset is also retracted at the approach velocity.

##### Homing velocity

With active homing, the technology object approaches the homing mark at homing velocity.

#### Homing mode for active and passive homing (S7-1500, S7-1500T)

Three homing modes are available for active and passive homing of absolute encoders and incremental encoders:

- Reference output cam and zero mark via PROFIdrive telegram

  High accuracy
- Zero mark via PROFIdrive telegram

  High accuracy
- Digital input

  Low accuracy

##### Selection criteria

Select the homing mode based on the following criteria:

- Encoder zero mark "N" available on encoder
- Hardware support for a zero mark substitute through use of a fast digital input
- Number of encoder zero marks in the traversing range of the axis

The following figure shows the selection criteria for the homing mode:

![Selection criteria](images/171964563595_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Selection criteria](images/172177645067_DV_resource.Stream@PNG-de-DE.png) | Wiring |
| ![Selection criteria](images/172177320843_DV_resource.Stream@PNG-de-DE.png) | Hardware configuration |
| ![Selection criteria](images/172177869707_DV_resource.Stream@PNG-de-DE.png) | Homing mode |

##### Reference output cam and zero mark via PROFIdrive telegram

If multiple encoder zero marks are in the traversing range and you want to home to one of the zero marks, use this mode

As the reference output cam, you need a digital input at the central or distributed I/O of the CPU or at the compact CPU.

The system checks the reaching of the reference output cam. After the reference output cam has been reached and exited again in the assigned homing direction, zero mark detection is activated via the PROFIdrive telegram.

When the zero mark is reached in the configured direction, the actual position of the technology object is set to the homing mark position.

##### Zero mark via PROFIdrive telegram

You use this homing mode in the following situations:

- The encoder has no zero mark and a zero mark substitute is available.
- The encoder has a zero mark and it is present only once in the entire traversing range of the axis.
- The encoder has multiple zero marks in the traversing range. Instead of the zero marks, a zero mark substitute will be used.

You can use a fast digital input as a zero mark substitute. The signal of this input is transferred via PROFIdrive instead of the encoder zero mark.

The following hardware components have digital inputs that you configure as a zero mark substitute.

- SINAMICS:

  Configure digital input as "[External zero mark](#homing-sinamics-drives-with-external-zero-marks-s7-1500-s7-1500t)"
- Technology modules (e.g. TM Count, TM PosInput):

  Configure operating mode as "Position detection for technology object Motion Control"

  Configure "Signal selection for reference mark 0" as DI0
- Onboard I/O S7-151xC-1 PN

  Activate HSC

  Configure operating mode as "Position detection for technology object Motion Control"

  Configure "Signal selection for reference mark 0" as DI0

  Configure hardware input for HSC DI0 to the wired terminal

##### Digital input

If the encoder has no encoder zero mark in the traversing range and the hardware does not support a zero mark substitute, use this homing mode. You need a digital input at the central or distributed I/O of the CPU or at the compact CPU.

A hardware limit switch can be used as a digital input.

The system checks the state of the digital input as soon as the actual value of the axis or encoder moves in the configured homing direction. When the homing mark is reached (setting of the digital input) in the specified homing direction, the actual position of the technology object is set to the homing mark position.

The digital inputs must be placed into the process image partition "PIP OB Servo". The filter time of the digital inputs must be set smaller than the duration of the input signal at the reference point switch.

A low homing velocity increases the accuracy.

#### Active homing (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Active homing with reference cam and zero mark (S7-1500, S7-1500T)](#active-homing-with-reference-cam-and-zero-mark-s7-1500-s7-1500t)
- [Active homing with zero mark (S7-1500, S7-1500T)](#active-homing-with-zero-mark-s7-1500-s7-1500t)
- [Active homing with digital input (S7-1500, S7-1500T)](#active-homing-with-digital-input-s7-1500-s7-1500t)
- [Direction reversal at the hardware limit switch (reversing output cam) (S7-1500, S7-1500T)](#direction-reversal-at-the-hardware-limit-switch-reversing-output-cam-s7-1500-s7-1500t)
- [Active homing to a hardware limit switch (S7-1500, S7-1500T)](#active-homing-to-a-hardware-limit-switch-s7-1500-s7-1500t)

##### Active homing with reference cam and zero mark (S7-1500, S7-1500T)

The following examples show homing motions in the positive and negative directions.

###### Example of homing in the positive direction

The approach to the homing mark and the home position occurs in the positive direction.

The following figure shows the homing motion with the following settings:

- Active homing with reference output cam and zero mark
- Approach in the positive direction
- Homing in the positive direction
- Positive home position offset

![Example of homing in the positive direction](images/165623963915_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **Motion sequence** |  |
| ① | Start of active homing via the Motion Control instruction "MC_Home" |
| ② | Approach to the reference output cam in approach direction with approach velocity |
| ③ | Detection of reference output cam and activation of homing mark detection |
| ④ | Approach to the homing mark with homing velocity |
| ⑤ | Detection of the homing mark |
| ⑥ | Approach to home position with approach velocity |

> **Note**
>
> If the velocity cannot be reduced to the homing velocity between detection of the reference output cam and the zero mark, homing is performed at the velocity present when the zero mark is crossed.

###### Example of homing in the negative direction

The approach to the homing mark occurs in the negative direction by means of a direction reversal during the homing process. The approach to home position causes another direction reversal and occurs in the positive direction.

The following figure shows the homing motion with the following settings:

- Active homing with reference output cam and zero mark
- Approach in the positive direction
- Homing in the negative direction
- Positive home position offset

![Example of homing in the negative direction](images/165624136331_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **Motion sequence** |  |
| ① | Start of active homing via the Motion Control instruction "MC_Home" |
| ② | Approach to the reference output cam in approach direction with approach velocity |
| ③ | Detection of reference output cam and activation of homing mark detection |
| ④ | Approach to the homing mark with homing velocity |
| ⑤ | Detection of the homing mark |
| ⑥ | Approach to home position with approach velocity |

###### Requirements

- Digital input as PLC tag
- The technology object has been enabled.

###### Procedure

To home the technology object actively with reference output cam and zero mark, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Active homing".
2. In the "Select the homing mode" field, select the "Use reference cam and zero mark via PROFIdrive telegram" option.
3. For "Digital input homing mark/cam", select the PLC tag of the digital input.
4. Select the appropriate signal level for the digital input under "Level selection".
5. In the "Approach direction" field, select the direction in which the reference cam is approached:

   - Positive: Approach direction in direction of positive position values
   - Negative: Approach direction in direction of negative position values
6. In the "Homing direction" field, select the direction in which the zero mark is approached for homing:

   - Positive: Homing direction in the direction of positive position values
   - Negative: Homing direction in the direction of negative position values
7. Under "Approach velocity", set the velocity with which the reference output cam is approached. Any configured home position offset is traversed at the same velocity.
8. Under "Homing velocity", set the velocity with which the zero mark is approached for homing.
9. If the home position is different from the homing mark position, enter a corresponding home position offset under "Home position offset". The axis approaches the home position at approach velocity.
10. Configure the "Home position". The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 5.
11. To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 5.

    - When the homing mark is recognized, the position is set to:

      Position = value in tag "<TO>.Homing.HomePosition" minus "<TO>.Sensor[1..4].ActiveHoming.HomePositionOffset"
    - The "Homed" status of the technology object is set to TRUE.
    - The axis moves to the position that is specified in the "<TO>.Homing.HomePosition" tag.
    - The "Done" parameter in "MC_Home" is set to TRUE after moving to the home position.
12. To home the technology object and specify the home position directly on the homing job, call the "MC_Home" instruction with "Mode" = 3 and "Position" = <Home position>.

    - When the homing mark is recognized, the position is set to:

      Position = value in parameter "Position" minus "<TO>.Sensor[1..4].ActiveHoming.HomePositionOffset"
    - The "Homed" status of the technology object is set to TRUE.
    - The axis moves to the position that is specified in the "Position" parameter.
    - The "Done" parameter in "MC_Home" is set to TRUE after moving to the home position.

---

**See also**

[Homing SINAMICS drives with external zero marks (S7-1500, S7-1500T)](#homing-sinamics-drives-with-external-zero-marks-s7-1500-s7-1500t)

##### Active homing with zero mark (S7-1500, S7-1500T)

###### Example of homing motion

The following figure shows an example of the homing motion with the following settings:

- Active homing with zero mark
- Homing in the positive direction
- Positive home position offset

  ![Example of homing motion](images/165624142731_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | **Motion sequence** |  |
  | ① | Start of active homing via the "MC_Home" Motion Control instruction |
  | ② | Approach to the homing mark in the homing direction with homing velocity |
  | ③ | Detection of the homing mark |
  | ④ | Approach to home position with approach velocity |

###### Requirements

- The technology object has been enabled.

###### Procedure

To home the technology object actively with zero mark, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Active homing".
2. In the "Select the homing mode" field, select the "Use zero mark via PROFIdrive telegram" option.
3. In the "Approach direction" field, select the direction in which the zero mark is approached:

   - Positive: Homing direction in the direction of positive position values
   - Negative: Homing direction in direction of negative position values
4. Under "Approach velocity", set the velocity with which any set home position offset is retracted.
5. Under "Homing velocity", set the velocity with which the homing mark is approached.
6. If the home position is different from the homing mark position, enter a corresponding home position offset under "Home position offset". The axis approaches the home position at approach velocity.
7. For "Home position", configure the absolute home position coordinate of the home position. The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 5.
8. To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 5.

   - When the homing mark is recognized, the position is set to:

     Position = value in tag "<TO>.Homing.HomePosition" minus "<TO>.Sensor[1..4].ActiveHoming.HomePositionOffset"
   - The "Homed" status of the technology object is set to TRUE.
   - The axis moves to the position that is specified in the "<TO>.Homing.HomePosition" tag.
   - The "Done" parameter in "MC_Home" is set to TRUE after moving to the home position.
9. To home the technology object and specify the home position directly on the homing job, call the "MC_Home" instruction with "Mode" = 3 and "Position" = <Home position>.

   - When the homing mark is recognized, the position is set to:

     Position = value in parameter "Position" minus "<TO>.Sensor[1..4].ActiveHoming.HomePositionOffset"
   - The "Homed" status of the technology object is set to TRUE.
   - The axis moves to the position that is specified in the "Position" parameter.
   - The "Done" parameter in "MC_Home" is set to TRUE after moving to the home position.

---

**See also**

[Homing SINAMICS drives with external zero marks (S7-1500, S7-1500T)](#homing-sinamics-drives-with-external-zero-marks-s7-1500-s7-1500t)

##### Active homing with digital input (S7-1500, S7-1500T)

###### Example of homing motion

The following figure shows an example of the homing motion with the following settings:

- Active homing with digital input
- Approach in the positive direction
- Homing mark on the positive side of the digital input
- Positive home position offset

  ![Example of homing motion](images/165624225547_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | **Motion sequence** |  |
  | ① | Start of active homing via the "MC_Home" Motion Control instruction |
  | ② | Move on the positive edge at the digital input in the approach direction with approach velocity |
  | ③ | Detection of the positive edge at the digital input |
  | ④ | Approach to the homing mark in the homing direction with the homing velocity |
  | ⑤ | Detection of the homing mark |
  | ⑥ | Approach to home position with approach velocity |

  > **Note**
  >
  > If the velocity cannot be reduced to the homing velocity between detection of the reference output cam and the zero mark, homing is performed at the velocity present when the zero mark is crossed.

###### Requirements

- Digital input as PLC tag
- The technology object has been enabled.

###### Procedure

To home the technology object actively with a digital input, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Active homing".
2. In the "Select the homing mode" field, select the "Use homing mark via digital input" option.
3. For "Digital input homing mark/cam", select the PLC tag of the digital input.
4. Select the appropriate signal level for the digital input under "Level selection".
5. In the "Approach direction" field, select the direction in which the digital input is approached:

   - Positive: Approach direction in direction of positive position values
   - Negative: Approach direction in direction of negative position values
6. In the "Homing direction" field, select the direction in which the homing mark of the digital input is approached for homing:

   - Positive: Homing direction in the direction of positive position values
   - Negative: Homing direction in the direction of negative position values
7. In the "Homing mark" field, select which side of the digital input is to be used as the homing mark.

   - Positive side
   - Negative side
8. Under "Approach velocity", set the velocity with which the "digital input" is approached. Any configured home position offset is traversed at the same velocity.
9. Under "Homing velocity", set the velocity with which the homing mark is approached.
10. If the home position is different from the homing mark position, enter a corresponding home position offset under "Home position offset". The axis approaches the home position at approach velocity.
11. For "Home position", configure the absolute home position coordinate of the home position. The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 5.
12. To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 5.

    - When the homing mark is recognized, the position is set to:

      Position = value in tag "<TO>.Homing.HomePosition" minus "<TO>.Sensor[1..4].ActiveHoming.HomePositionOffset"
    - The "Homed" status of the technology object is set to TRUE.
    - The axis moves to the position that is specified in the "<TO>.Homing.HomePosition" tag.
    - The "Done" parameter in "MC_Home" is set to TRUE after moving to the home position.
13. To home the technology object and specify the home position directly on the homing job, call the "MC_Home" instruction with "Mode" = 3 and "Position" = <Home position>.

    - When the homing mark is recognized, the position is set to:

      Position = value in parameter "Position" minus "<TO>.Sensor[1..4].ActiveHoming.HomePositionOffset"
    - The "Homed" status of the technology object is set to TRUE.
    - The axis moves to the position that is specified in the "Position" parameter.
    - The "Done" parameter in "MC_Home" is set to TRUE after moving to the home position.

##### Direction reversal at the hardware limit switch (reversing output cam) (S7-1500, S7-1500T)

During active homing, the hardware limit switch can optionally be used as a reversing output cam. If the homing mark is not detected or the motion was not in the homing direction, the motion continues in the opposite direction with the approach velocity after the reversing output cam.

When the hardware limit switch is reached, the default settings for dynamics take effect. Deceleration with the emergency deceleration does not hereby occur.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Avoid moving to a mechanical endstop**  Ensure by one of the following measures, that in a direction reversal the machine does not move to a mechanical endstop.  - Keep the approach velocity low. - Increase the configured default acceleration/deceleration. - Increase the distance between the hardware limit switch and the mechanical endstop. |  |

##### Active homing to a hardware limit switch (S7-1500, S7-1500T)

If only hardware limit switches are available on the axis and no separate digital inputs are available as homing marks, then you can home the axis to the hardware limit switches.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Avoid moving to a mechanical endstop**  Take one of the following measures to ensure that the machine does not hit a mechanical stop when homing is active with the hardware limit switch as the homing mark:  - Keep the approach velocity low. - Increase the configured acceleration/deceleration. - Increase the distance between the hardware limit switch and the mechanical endstop. - Select a home position offset in direction of the traversing range of the axis against the mechanical stop. |  |

###### Procedure

To use the signal of the hardware limit switch as a homing mark, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Active homing".
2. In the "Select the homing mode" field, select the "Use homing mark via digital input" option.
3. For "Digital input homing mark/cam", select the PLC tag of the hardware limit switch, e.g. "HwLimitPos".
4. Select the appropriate signal level for the digital input under "Level selection".
5. In the "Approach direction" field, select the direction in which the digital input is approached:

   - Positive: Approach direction in direction of positive position values
   - Negative: Approach direction in direction of negative position values
6. In the "Homing direction" field, select the direction in which the homing mark of the digital input is approached for homing:

   - Positive: Homing direction in the direction of positive position values
   - Negative: Homing direction in the direction of negative position values
7. In the "Homing mark" field, select which side of the digital input is to be used as the homing mark. The following recommendation applies to hardware limit switches in order not to traverse the axis unnecessarily far in the direction of the mechanical stop.

   - Positive side of the negative hardware limit switch
   - Negative side of the positive hardware limit switch
8. Under "Approach velocity", set the velocity with which the hardware limit switch is approached. Any configured home position offset is traversed at the same velocity.
9. Under "Homing velocity", set the velocity with which the homing mark is approached.
10. If the home position is different from the homing mark position, enter a corresponding home position offset under "Home position offset". The axis approaches the home position at approach velocity. When homing to the hardware limit switch, the following settings are recommended in order to perform the approach to the home position in the direction of the traversing range or opposite the mechanical stop.

    - Negative hardware limit switch: Home position offset ≥ 0
    - Positive hardware limit switch: Home position offset ≤ 0
11. For "Home position", configure the absolute home position coordinate of the home position. The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 5.
12. Disable the existing hardware limit switch with the Motion Control instruction "MC_WriteParameter".
13. To start active homing, call the "MC_Home" instruction in the user program.

    - To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 5.
    - To home the technology object with the home position at the parameter "Position" home position, call the "MC_Home" instruction with "Mode" = 3.
14. Move the axis back to the working area between the hardware limit switches.
15. Activate existing hardware limit switches with the "MC_WriteParameter" Motion Control instruction.

#### Passive homing (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Passive homing with reference cam and zero mark (S7-1500, S7-1500T)](#passive-homing-with-reference-cam-and-zero-mark-s7-1500-s7-1500t)
- [Passive homing with zero mark (S7-1500, S7-1500T)](#passive-homing-with-zero-mark-s7-1500-s7-1500t)
- [Passive homing with digital input (S7-1500, S7-1500T)](#passive-homing-with-digital-input-s7-1500-s7-1500t)
- [Cancel passive homing (S7-1500, S7-1500T)](#cancel-passive-homing-s7-1500-s7-1500t)

##### Passive homing with reference cam and zero mark (S7-1500, S7-1500T)

###### Example of homing motion

The following figure shows an example of the homing motion with the following settings:

- Passive homing with reference output cam and zero mark
- Homing in the positive direction

  ![Example of homing motion](images/165624231563_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | **Motion sequence** |  |
  | ① | Activation of passive homing using the Motion Control instruction "MC_Home" |
  | ② | Motion due to a motion job  The detection of the reference output cam and homing mark is enabled when the actual position value of the axis or encoder moves in the assigned homing direction. |
  | ③ | Detection of the reference output cam |
  | ④ | Exit from the reference output cam  The exit from the reference output cam activates the homing mark detection. |
  | ⑤ | Detection of the homing mark |

  > **Note**
  >
  > If the motion direction changes after the exit from the reference output cam and before detection of the homing mark, the reference output cam must be detected again. The Motion Control instruction "MC_Home" remains enabled.

###### Requirements

- Digital input as PLC tag
- The technology object has been enabled.

###### Procedure

To home the technology object passively with reference output cam and zero mark, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Passive homing".
2. In the "Select the homing mode" field, select the "Use reference cam and zero mark via PROFIdrive telegram" option.
3. For "Digital input homing mark/cam", select the PLC tag of the digital input.
4. Select the appropriate signal level for the digital input under "Level selection".
5. In the "Homing direction" field, select the direction in which the next zero mark is to be approached for homing.

   - Positive: The axis moves in the direction of positive position values.
   - Negative: The axis moves in the direction of negative position values.
   - Current: The currently effective approach direction is used for homing.
6. For "Home position", configure the absolute home position coordinate of the home position. The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 10.
7. To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 10.
8. To home the technology object and specify the home position directly on the homing job, call the "MC_Home" instruction with "Mode" = 8 or "Mode" = 2 (without resetting the "homed" status).
9. Traverse the axis in the configured homing direction.

   - The detection of the zero mark/homing mark is activated after the reference output cam has been traversed.
   - When the homing mark is detected, the position of the axis or encoder is set depending on the mode:

     "Mode" = 10: Position = value in tag "<TO>.Homing.HomePosition"

     "Mode" = 8 or "Mode" = 2: Position = value in parameter "Position"
   - The axis is homed as soon as the zero mark/homing mark is reached or detected.
10. To save the absolute value offset retentively for an absolute encoder, you must perform an [absolute encoder adjustment](#absolute-value-adjustment-s7-1500-s7-1500t).

##### Passive homing with zero mark (S7-1500, S7-1500T)

###### Example of homing motion

The following figure shows an example of the homing motion with the following settings:

- Passive homing with zero mark
- Homing in the positive direction

  ![Example of homing motion](images/165571528075_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | **Motion sequence** |  |
  | ① | Activation of passive homing using the Motion Control instruction "MC_Home" |
  | ② | Motion due to a motion job  The detection of the reference output cam and homing mark is enabled when the actual position value of the axis or encoder moves in the assigned homing direction. |
  | ③ | Detection of the homing mark |

###### Requirements

- Technology object is enabled.

###### Procedure

To home the technology object passively with zero mark, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Passive homing".
2. In the "Select the homing mode" field, select the "Use zero mark via PROFIdrive telegram" option.
3. In the "Homing direction" field, select the direction in which the next zero mark is to be approached for homing.

   - Positive: The axis moves in the direction of positive position values.
   - Negative: The axis moves in the direction of negative position values.
   - Current: The currently effective approach direction is used for homing.
4. For "Home position", configure the absolute home position coordinate of the home position. The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 10.
5. To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 10.
6. To home the technology object and specify the home position directly on the homing job, call the "MC_Home" instruction with "Mode" = 8 or "Mode" = 2 (without resetting the "homed" status).
7. Traverse the axis in the configured homing direction.

   - The detection of the zero mark/homing mark is activated after the reference output cam has been traversed.
   - When the homing mark is detected, the position of the axis or encoder is set depending on the mode:

     "Mode" = 10: Position = value in tag "<TO>.Homing.HomePosition"

     "Mode" = 8 or "Mode" = 2: Position = value in parameter "Position"
   - The axis is homed as soon as the zero mark/homing mark is reached or detected.

##### Passive homing with digital input (S7-1500, S7-1500T)

###### Example of homing motion

The following figure shows an example of the homing motion with the following settings:

- Passive homing with digital input
- Homing in the positive direction
- Homing mark on the positive side of the digital input

  ![Example of homing motion](images/165571538571_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | **Motion sequence** |  |
  | ① | Activation of passive homing using the Motion Control instruction "MC_Home" |
  | ② | Motion due to a motion job  The detection of the reference output cam and homing mark is enabled when the actual position value of the axis or encoder moves in the assigned homing direction. |
  | ③ | Detection of the homing mark  In the example, the negative edge of the switch at the digital input represents the homing mark. |

###### Requirements

- Digital input as PLC tag
- The technology object has been enabled.

###### Procedure

To home the technology object passively with digital input, follow these steps:

1. In the project tree, in the configuration of the technology object, navigate to "Extended parameters > Homing > Passive homing".
2. In the "Select the homing mode" field, select the "Use homing mark via digital input" option.
3. For "Digital input homing mark/cam", select the PLC tag of the digital input.
4. Select the appropriate signal level for the digital input under "Level selection".
5. In the "Homing direction" field, select the direction in which the next zero mark is to be approached for homing.

   - Positive: The axis moves in the direction of positive position values.
   - Negative: The axis moves in the direction of negative position values.
   - Current: The currently effective approach direction is used for homing.
6. In the "Homing mark" field, select which side of the digital input is to be used as the homing mark.

   - Positive side
   - Negative side
7. For "Home position", configure the absolute home position coordinate of the home position. The home position configured here is in effect when the Motion Control instruction "MC_Home" is executed with "Mode" = 10.
8. To home the technology object with the home position configured in the technology object, call the "MC_Home" instruction with "Mode" = 10.
9. To home the technology object and specify the home position directly on the homing job, call the "MC_Home" instruction with "Mode" = 8 or "Mode" = 2 (without resetting the "homed" status).
10. Traverse the axis in the configured homing direction.

    - The detection of the zero mark/homing mark is activated after the reference output cam has been traversed.
    - When the homing mark is detected, the position of the axis or encoder is set depending on the mode:

      "Mode" = 10: Position = value in tag "<TO>.Homing.HomePosition"

      "Mode" = 8 or "Mode" = 2: Position = value in parameter "Position"
    - The axis is homed as soon as the zero mark/homing mark is reached or detected.

##### Cancel passive homing (S7-1500, S7-1500T)

###### Requirements

- A job for passive homing with the instruction "MC_Home" ("Mode" = 2, 8, 10) was started.
- The technology object has not yet been homed.

###### Procedure

To cancel an active job for passive homing, follow these steps:

- Call the "MC_Home" instruction with "Mode" = 9.

  - When the active "MC_Home" job for passive homing ("Mode" = 2, 8, 10) is overridden by another "MC_Home" job with "Mode" = 9, the running job is canceled with the parameter "CommandAborted" = TRUE.
  - The overriding job with "Mode" = 9 signals successful execution with parameter "Done" = TRUE.

#### Direct homing (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Direct homing (S7-1500, S7-1500T)](#direct-homing-s7-1500-s7-1500t-1)

##### Direct homing (S7-1500, S7-1500T)

Depending on the configured mode, the position of the positioning axis/synchronous axis or external encoder technology objects can be absolutely or relatively set with "MC_Home".

###### Requirement

- The technology object is in position-controlled mode.

###### Procedure

**Set actual position absolutely**

To set the actual position absolutely, proceed as follows:

1. In the "MC_Home" Motion Control instruction, enter the absolute actual position in the "Position" parameter.
2. Call the "MC_Home" Motion Control instruction with parameter "Mode" = 0.

The position is set to the value specified in the "Position" parameter.

**Set actual position relatively**

To set the actual position relatively, proceed as follows:

1. In the "MC_Home" Motion Control instruction, enter the relative actual position in the "Position" parameter.
2. Call the "MC_Home" Motion Control instruction with parameter "Mode" = 1.

The position is set to the current position plus the value specified in the "Position" parameter.

###### Direct homing at fixed stop

For direct homing at fixed stop, all motions must be programmed in the user program. Change the configuration data directly in the user program. The fixed stop is used as homing mark.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Too fast manual traversing to the fixed stop**  Too fast a manual traversing of the axis can lead to machine damage.  Move the axis manually with low speed/velocity. Configure a suitable torque limit. |  |

To set the position at the fixed stop absolutely or relatively, proceed as follows:

1. Activate a suitable fixed stop detection with the Motion Control instruction "MC_TorqueLimiting".
2. Deactivate the existing hardware limit switch with the Motion Control instruction "MC_WriteParameter".
3. Move the axis to the fixed stop using a suitable motion job. For example, use the Motion Control instructions "MC_MoveRelative" or "MC_MoveJog".
4. After the axis has reached the fixed stop, execute a direct homing using the Motion Control instruction "MC_Home".
5. Move the axis back to the working area between the hardware limit switches.
6. Activate the hardware limit switch with the Motion Control instruction "MC_WriteParameter".
7. Deactivate the fixed stop detection using the Motion Control instruction "MC_TorqueLimiting".

> **Note**
>
> In the case of an axis with several encoders, the offset of the position at the sensors of all encoders is also applied with a position correction with the parameter "Mode" = 0. This prevents the sensors from diverging.

---

**See also**

[MC_TorqueLimiting V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_torquelimiting-v8-s7-1500-s7-1500t)
  
[MC_WriteParameter V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_writeparameter-v8-s7-1500-s7-1500t)
  
[MC_MoveJog V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movejog-v8-s7-1500-s7-1500t)
  
[MC_MoveRelative V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_moverelative-v8-s7-1500-s7-1500t)
  
[MC_Home V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_home-v8-s7-1500-s7-1500t)

#### Set setpoint position (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Set position setpoint (S7-1500, S7-1500T)](#set-position-setpoint-s7-1500-s7-1500t)

##### Set position setpoint (S7-1500, S7-1500T)

You can set the position setpoint of the axis or the encoder as absolute or relative.

###### Requirement

- Encoder values are valid (<TO>.StatusSensor[1..4].State = 2)

###### Procedure

**Set position setpoint absolutely**

To set the position setpoint absolutely, follow these steps:

1. In the "MC_Home" Motion Control instruction, enter the absolute position setpoint in the "Position" parameter.
2. Call the "MC_Home" Motion Control instruction with parameter "Mode" = 11.

The set position of the technology object is set to the value of the "Position" parameter. The following error remains.

**Set position setpoint relatively**

To set the position setpoint relatively, follow these steps:

1. In the "MC_Home" Motion Control instruction, enter the relative position setpoint in the "Position" parameter.
2. Call the "MC_Home" Motion Control instruction with parameter "Mode" = 12.

The set position of the technology object is shifted by the value of the "Position" parameter. The following error remains.

#### Absolute value adjustment (S7-1500, S7-1500T)

In absolute encoder adjustment, Motion Control determines an absolute value offset that is retentively stored on the CPU.

You can set the actual position of the axis or the encoder as absolute or relative.

##### Requirements

- The technology object is in position-controlled mode.
- The actual encoder values are valid ("<TO>.Statussensor[1..4].State" = 2).

##### Absolute specification of position

To perform absolute encoder adjustment with absolute specification of position, call the Motion Control instruction "MC_Home" with the parameters "Mode" = 7 and "Position" = absolute position setpoint.

To adjust the operative encoder, enter "Sensor" = 0 at the parameter.

To adjust a non-operative encoder, enter the number of the encoder at the "Sensor" parameter. (S7-1500T)

The current position is set to the value of parameter "Position".

The absolute encoder offset is retentively saved in the "<TO>.StatusSensor[1..4].AbsEncoderOffset" tag.

##### Relative specification of position

To perform absolute encoder adjustment with relative specification of position, call the Motion Control instruction "MC_Home" with the parameters "Mode" = 6 and "Position" = value by which the current position is to be shifted.

To adjust the operative encoder, enter "Sensor" = 0 at the parameter.

To adjust a non-operative encoder, enter the number of the encoder at the "Sensor" parameter. (S7-1500T)

The current position is shifted by the value of parameter "Position".

The absolute encoder offset is retentively saved in the "<TO>.StatusSensor[1..4].AbsEncoderOffset" tag.

##### Restoring the position after switching on the CPU

**Absolute actual value with setting absolute (measuring range > traversing range)**

The axis position results directly from the current actual encoder value. The traversing range must be within an encoder measuring range. This means that the zero crossing of the encoder must not be located in the traversing range.

When the controller is switched on, the axis position is determined from the absolute actual encoder value.

**Absolute actual value with setting cyclic absolute (measuring range < traversing range)**

The encoder supplies an absolute value within its measuring range. The controller includes the traversed measuring ranges and thus determines the correct axis position beyond the measuring range.

You can find more information on the encoder type in the section ["Configuring the encoder type"](#configuring-the-encoder-type-s7-1500-s7-1500t).

When the controller is switched off, the traversed measuring ranges are saved in the retentive memory area of the controller.   
At the next power-on, the saved traversed measuring ranges are taken into account in the calculation of the actual position value.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Movements of the axis while the controller is switched off can skew the actual value**  If the axis or the encoder is moved by more than half of the encoder measuring range while the controller is switched off, the actual value in the controller is no longer in accord with the mechanical axis position. |  |

##### Resetting the absolute value offset of an encoder

To reset an absolute value offset stored retentively in the CPU, follow these steps:

1. Change the encoder type to incremental.
2. Load the technology object to the CPU.

   The retentively stored absolute value offset is deleted.
3. Change the encoder type back to absolute encoder.
4. Load the technology object to the CPU.

Specify the position of the axis again.

---

**See also**

[MC_SaveAbsoluteEncoderData V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_saveabsoluteencoderdata-v8-s7-1500-s7-1500t)

#### Save data on the SIMATIC Memory Card (S7-1500, S7-1500T)

With the "MC_SaveAbsoluteEncoderData" Motion Control instruction you can save the absolute encoder adjustment data on the SIMATIC Memory Card for all technology objects with "Absolute" or "Cyclic absolute" encoder type.

The data is saved on the SIMATIC Memory Card in the "UserFiles" folder as "AbsEncoderData.dat".

##### Requirements

You can use the data saved with "MC_SaveAbsoluteEncoderData" when replacing a device if the following requirements are met.

- Identical encoder configuration
- Identical names of technology objects
- Identical numbers of technology object data blocks

The absolute encoder adjustment is therefore saved.

> **Note**
>
> **Invalid values of the absolute encoder adjustment on the CPU**
>
> If your CPU is not in factory-set state, reset it to factory settings without the "Format memory card" option.

##### Transferring data to a new CPU

For transferring the data from the absolute encoder adjustment to the new SIMATIC CPU, you have further steps available.

**Use existing SIMATIC memory card**

1. Insert the SIMATIC Memory Card with values of the absolute encoder adjustment into the new SIMATIC CPU.
2. If your CPU is not in factory-set state, reset it to factory settings without the "Format memory card" option.
3. Check the successful recovery of data in the diagnostic buffer.
4. Switch the CPU to "Run" mode.

**Copy the file "**
**AbsEncoderData.dat**
**" to a new SIMATIC Memory Card with the card reader**

1. Copy the file "AbsEncoderData.dat" to a new SIMATIC Memory Card in the folder "UserFiles".
2. Insert the SIMATIC Memory Card with values of the absolute encoder adjustment into the SIMATIC CPU.
3. If your CPU is not in factory-set state, reset it to factory settings without the "Format memory card" option.
4. Check the successful recovery of data in the diagnostic buffer.
5. Switch the CPU to "Run" mode.

**Transfer the file "**
**AbsEncoderData.dat**
**" to a SIMATIC Memory Card in the web server**

Note that the "UserFiles" folder is write-protected on the "Filebrowser" web page.

To transfer the data to a SIMATIC Memory Card in the web server, follow these steps:

1. Select the file "AbsEncoderData.dat" in the web server under User files .
2. Upload the file. The file is automatically assigned in the folder "UserFiles".
3. If your CPU is not in factory-set state, reset it to factory settings without the "Format memory card" option.
4. Check the successful recovery of data in the diagnostic buffer.
5. Switch the CPU to "Run" mode.

##### Result

The values of the absolute encoder adjustment are restored.

The entry "The data backup for the absolute encoder adjustment was successfully restored" is displayed in the diagnostic buffer.

The backup on the SIMATIC Memory Card is automatically renamed ("AbsEncoderData.bak") and cannot continue to be used.

##### Checking the restore and backing up data again

Check the correct axis positions.

To back up the data of the absolute encoder adjustment again, perform a backup of the absolute encoder data with the Motion Control instruction "MC_SaveAbsoluteEncoderData".

#### Incremental encoder adjustment (S7-1500, S7-1500T)

With the incremental encoder adjustment, you can set the absolute position of an incremental encoder with "Mode" = 13 at "MC_Home".

If the selected encoder is the operative encoder, the setpoint is automatically adjusted to the calibrated actual value during homing. The axis does not perform a compensating motion. After homing, the actual value of the axis is equal to the actual value of the encoder.

In the case of an axis with several encoders: In contrast to "Mode" = 0, when parameter "Mode" = 13 is set, the position offset is not applied at all encoders during a position correction. This means the actual position values can deviate between the encoders. When you switch over the encoder with "MC_SetSensor" with "Mode" = 1 (without synchronization of the actual position) and active position control, an additional difference between the two encoders acts as additional control deviation and can trigger a compensating motion.

During incremental encoder adjustment, the position of the incremental encoder is not saved retentively in the CPU. The values are lost after POWER-OFF.

##### Requirements

- Incremental encoder
- Technology object enabled and position-controlled or technology object disabled
- No active alarms

##### Procedure

To perform the incremental encoder adjustment, call the Motion Control instruction "MC_Home" with the parameters "Mode" = 13 and "Position" = absolute position setpoint.

To adjust the active encoder, set parameter "Sensor" = 0.

To adjust a non-active encoder, enter the number of the encoder at the "Sensor" parameter. (S7-1500T)

The current position is set to the value of parameter "Position".

#### Homing SINAMICS drives with external zero marks (S7-1500, S7-1500T)

For SINAMICS drives with external zero mark, synchronization during homing must always occur on the left side of the external zero mark's signal. That is to say, with a positive direction of travel synchronization is done on a positive edge, and with a negative direction of travel synchronization is done on a negative edge.

By inverting the signal, synchronization can also be done on the right sight of the signal of the external zero mark. The inversion can be set on the drive with SINAMICS parameter p490.

Homing to an encoder zero mark or an external zero mark is set in SINAMICS parameter p495.

#### Homing when backlash compensation is enabled (S7-1500, S7-1500T)

##### Active and passive homing "MC_Home" with "Mode" = 2, 3, 5, 8 or 10

Always move the axis in the same direction to the home position. Select either "positive" or "negative" as homing direction.

> **Note**
>
> Before reaching the homing mark, the backlash must have traversed completely in the homing direction.

##### Direct homing "MC_Home" with "Mode" = 0 or 1

Always move the axis in the same direction before or during direct homing. If you move the axis in another direction during direct homing, then the axis position around the backlash is invalidated.

##### Absolute encoder adjustment "MC_Home" with "Mode" = 6 or 7

In order that the actual encoder value can be clearly assigned to an axis position for an absolute encoder, the position of the backlash must also be taken into account when setting the absolute value offset for the absolute encoder adjustment. The position of the backlash results from the direction of travel of the axis during or before the absolute encoder adjustment. Configure the direction of travel of axis using the "Absolute homing direction" parameter. After the controller is switched on again, the axis traverses the backlash if the first traversing motion is in the opposite direction to the absolute homing direction.

If the absolute encoder adjustment has already been carried out, the axis position will only be displayed correctly after the controller has been switched off and on again if the position of the backlash at the time of switch-on corresponds to the position of the backlash in relation to the axis position when the absolute encoder offset was set. Otherwise the axis position can deviate from the axis position displayed up to a maximum of the size of the backlash. The controller records the actual encoder value at the switch-on time, but cannot infer the position of the backlash without traversing the axis. After the axis has been traversed for the first time by at least the size of backlashes, the technology object again shows the real mechanical position.

##### Incremental encoder adjustment "MC_Home" with "Mode" = 13

Always move the axis and the encoder to be adjusted "MC_Home.Sensor" in the same direction before or during the incremental encoder adjustment. If you move the axis in another direction during incremental encoder adjustment, then the encoder position is incorrect by the amount of the backlash.

---

**See also**

[Backlash compensation (S7-1500, S7-1500T)](#backlash-compensation-s7-1500-s7-1500t)

#### Resetting the "Homed" status (S7-1500, S7-1500T)

##### Incremental encoder

In the following cases, the "Homed" status is reset, and the technology object must be rehomed.

- Error in sensor system/encoder failure
- Starting an "MC_Home" job with "Mode" = 3, 5, 8, 10

  (As soon the homing mark has been approached, the status "Homed" is set to "TRUE".)
- Replacement of the CPU
- Replacement of the SIMATIC Memory Card
- POWER OFF
- Memory reset
- Modification of the encoder configuration
- Restart of the technology object
- Restoration of the CPU factory settings
- Transfer of a different project into the controller

When you use a new incremental encoder you need to home the incremental encoder once again.

##### Absolute encoder

In the following cases, the "Homed" status is reset, and the technology object must be rehomed.

- Replacement of the CPU
- Changing the encoder type to incremental encoder
- Restoration of the CPU factory settings
- Transfer of a different project into the controller

When you use a new absolute value encoder you need to home the absolute encoder once again.

Resetting the memory of the CPU or upgrading a project does not require another absolute encoder adjustment.

#### Tags: Homing (S7-1500, S7-1500T)

The following technology object tags are relevant for homing:

| Status indicators |  |
| --- | --- |
| Tag | Description |
| <TO>.StatusWord.X11 (HomingCommand) | Homing job running |
| <TO>.StatusWord.X5 (HomingDone) | Technology object homed |
| <TO>.ErrorWord.X10 (HomingFault) | Error occurred during homing |
| <TO>.StatusSensor[1..4].Adjusted | Encoder homed |

> **Note**
>
> **Evaluation of the bits in "StatusWord", "ErrorWord" and "WarningWord"**
>
> Note the information in section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

| Approach to reference output cam |  |
| --- | --- |
| Tag | Description |
| <TO>.Homing.ApproachDirection | Start direction or approach direction for the approach to the reference output cam |
| <TO>.Homing.ApproachVelocity | Velocity for the approach to the reference output cam |

| Approach to the homing mark |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].ActiveHoming.Direction | Homing direction |
| <TO>.Homing.ReferencingVelocity | Velocity for the approach to the homing mark |

| Approach to home position |  |
| --- | --- |
| Tag | Description |
| <TO>.Homing.ApproachVelocity | Velocity for the move to homing point |

| Positions |  |
| --- | --- |
| Tag | Description |
| <TO>.Homing.AutoReversal | Reversal at the hardware limit switches |
| <TO>.Homing.HomePosition | Home position |
| <TO>.StatusSensor[1..4].AbsEncoderOffset | Calculated offset after the absolute encoder adjustment |

| Parameters for active homing |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].ActiveHoming.Mode | Homing mode |
| <TO>.Sensor[1..4].ActiveHoming.SideInput | Side of the digital input |
| <TO>.Sensor[1..4].ActiveHoming.Direction | Homing direction or approach direction |
| <TO>.Sensor[1..4].ActiveHoming.DigitalInputAddress | Address of digital input |
| <TO>.Sensor[1..4].ActiveHoming.HomePositionOffset | Offset of the homing mark from the home position |

| Parameters for passive homing |  |
| --- | --- |
| Tag | Description |
| <TO>.Sensor[1..4].PassiveHoming.Mode | Homing mode |
| <TO>.Sensor[1..4].PassiveHoming.SideInput | Side of the digital input |
| <TO>.Sensor[1..4].PassiveHoming.Direction | Homing direction or approach direction |
| <TO>.Sensor[1..4].PassiveHoming.DigitalInputAddress | Address of digital input |

### Position monitoring functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of position monitoring (S7-1500, S7-1500T)](#short-description-of-position-monitoring-s7-1500-s7-1500t)
- [Positioning monitoring (S7-1500, S7-1500T)](#positioning-monitoring-s7-1500-s7-1500t)
- [Following error monitoring (S7-1500, S7-1500T)](#following-error-monitoring-s7-1500-s7-1500t)
- [Standstill signal (S7-1500, S7-1500T)](#standstill-signal-s7-1500-s7-1500t)
- [Tags: Position monitoring functions (S7-1500, S7-1500T)](#tags-position-monitoring-functions-s7-1500-s7-1500t)

#### Short description of position monitoring (S7-1500, S7-1500T)

The following functions are available in the positioning axis/synchronous axis technology object for monitoring positioning and motion:

- [Positioning monitoring](#positioning-monitoring-s7-1500-s7-1500t)

  The actual position value must reach a positioning window within a specified time, and remain in this positioning window for a minimum dwell time.
- [Following error monitoring](#following-error-monitoring-s7-1500-s7-1500t)

  The following error is monitored based on a velocity-dependent following error limit. The permissible maximum following error depends on the velocity setpoint.
- [Standstill signal](#standstill-signal-s7-1500-s7-1500t)

  When the actual velocity reaches the standstill window and remains there for the minimum dwell time, the standstill of the axis is indicated.

If monitored conditions are violated, then technology alarms are output. The technology object responds in accordance with the alarm response.

#### Positioning monitoring (S7-1500, S7-1500T)

Position monitoring monitors the behavior of the actual position at the end of the setpoint calculation.

As soon as the velocity setpoint reaches the value zero, the actual position value must be located in the positioning window within a tolerance time. The actual value must not exit the positioning window during the minimum dwell time.

If the actual position is reached at the end of a positioning motion within the tolerance time and remains in the positioning window for the minimum dwell time, then "<TO>.StatusWord.X6 (Done)" is set in the technology data block. After expiration of the minimum dwell time, the "Done" parameter of the corresponding Motion Control instruction is also set. This completes a motion job.

The following figure shows the chronological sequence and the positioning window:

![Figure](images/165624467979_DV_resource.Stream@PNG-en-US.png)

Positioning monitoring does not make any distinction between how the setpoint interpolation was completed. The end of setpoint interpolation can for example be reached as follows:

- By the setpoint reaching the target position
- By position-controlled stopping during motion by the Motion Control instruction "MC_Halt" or "MC_Stop"

##### Violation of positioning monitoring

In the following cases, technology alarm 541 is output by the positioning monitoring, and the technology object is disabled (alarm reaction: remove enable).

- The actual value does not reach the positioning window during the tolerance time.
- The actual value exits the positioning window during the minimum dwell time.

##### Configure positioning monitoring

You can find the positioning monitoring in the configuration of the positioning axis/synchronous axis under "Extended parameters > Position monitoring > Position monitoring".

Follow these steps:

1. In the "Positioning window" field, configure the size of the positioning window. If the axis is located within this window, the position is considered to be "reached".
2. In the "Tolerance time" field, configure the time within which the position value must reach the positioning window.
3. In the "Minimum dwell time" field, configure the time for which the current position value must be in the positioning window for at least the "minimum dwell time".

   Recommended setting: To avoid longer pauses, set values between 0 ms and 20 ms for dynamic positioning tasks.

#### Following error monitoring (S7-1500, S7-1500T)

The following error is the difference between the setpoint and actual position based on the connection of the axis at the drive. The leading behavior of the axis is contained in the following error. The size of the following error depends on the velocity. The following error also contains a portion that arises from the disturbance variables.

The following error in the positioning axis/synchronous axis technology object is monitored based on a velocity-dependent following error limit. The permissible following error depends on the velocity setpoint.

A constant permissible following error can be specified for velocities lower than an adjustable velocity low limit.

Above this low velocity limit, the permissible following error increases in proportion to the velocity setpoint. The configurable maximum permissible following error is the maximum velocity limit.

##### Calculation of the following error

When calculating the following error, the transmission times of the setpoint to the drive and of the actual position value to the controller are deducted. The transmission times of the setpoints from the controller to the drive and the actual position values from the drive to the controller are therefore not part of the following error. The value of the following error is thus not the same as the difference between the position setpoint available in the controller minus the existing actual position.

The following error is thus calculated from the delayed position setpoint by T<sub>i</sub> + T<sub>o</sub> + T<sub>DC</sub> + T<sub>Servo</sub> minus the actual position in the controller.

The calculation of the following error is valid for the following conditions:

- Position control with and without DSC
- Configuration with and without precontrol of the position control loop
- Configuration of the drive coupling via a PROFIdrive telegram or via an analog output

##### Warning limit

A warning limit can be specified for the following error. The warning limit is input as a percentage value and operates relative to the current permissible following error. If the warning limit of the following error is reached, then technology alarm 522 is output. This is a warning and contains no alarm response.

##### Violation of the permissible following error

If the permissible following error is exceeded, then technology alarm 521 is output, and the technology object is disabled (alarm response: remove enable).

When force/torque limiting is activated, the monitoring of the permissible following error can be deactivated.

##### Enabling and configuring following error monitoring

You can find the following error monitoring in the configuration of the positioning axis/synchronous axis under "Extended parameters > Position monitoring > Following error".

Select the "Enable following error monitoring" check box.

To configure the following error monitoring, follow these steps:

1. In the "Following error" field, configure the permissible following error for low velocities (without dynamic adaptation of the following error) in the unit of measure for position of the axis.
2. In the "Maximum following error" field, enter the maximum permissible following error in the unit of measure for position of the axis.
3. In the "Start of dynamic adjustment" field, enter in the unit of measure for velocity of the axis the velocity from which the following error is to be adjusted dynamically. Starting from this velocity, the following error up to the maximum velocity will be adjusted to the maximum following error.
4. In the "Warning level" field, enter the percentage of the permitted following error as of which a warning is output.

   Example: The current maximum following error is 100 mm. The warning level is configured at 90%. If the current following error exceeds a value of 90 mm, the technology alarm 522 "Warning following error tolerance" is output. This is a warning and contains no alarm response.

##### Parameter assignment of the following error calculation with active dynamic filter

The following error is calculated from the delayed interpolated position setpoint by T<sub>i</sub>, T<sub>o</sub>, T<sub>DC</sub> and T<sub>Servo</sub> minus the current actual position value. The deceleration of the position setpoint by the dynamic filter in the technology object or through additional filters in the drive is not taken into account when calculating the following error. The calculated following error is therefore greater in reference to the position setpoint before the dynamic filter.

For correct calculation of the following error, configure an additional delay time <TO>.FollowingError.AdditionalSetpointDelayTime that delays the position setpoint when calculating the following error.

#### Standstill signal (S7-1500, S7-1500T)

When the actual velocity reaches the standstill window and remains there for the minimum dwell time, the standstill of the axis or the external encoder is indicated.

##### Configuring stationary state detection

You can find the stationary state detection of the positioning axis / synchronous axis in the configuration under "Extended parameters > Position monitoring > Standstill signal".

You can find the stationary state detection of the external encoder in the configuration under "Extended parameters > Standstill signal".

Follow these steps:

1. In the "Standstill window" field, configure the size of the standstill window in the measurement unit for the axis velocity.

   To avoid repeated toggling of the "<TO>.Statusword.X7 (Standstill)" bit, a hysteresis acts internally when the standstill window is exited. To exit the standstill window again, the actual velocity must be slightly higher than what is configured for "Standstill window".
2. In the "Minimum dwell time in standstill window" field, configure the duration in seconds for which the velocity of the axis must remain in the standstill window for stationary state detection.

#### Tags: Position monitoring functions (S7-1500, S7-1500T)

##### Standstill signal

The following technology object tags are relevant for position monitoring and for the standstill signal:

| Status indicators |  |
| --- | --- |
| Tag | Description |
| <TO>.StatusWord.X7 (Standstill) | Set to the value "TRUE" when the actual velocity reaches the standstill window and does not exit it within the minimum dwell time.   The standstill signal is not present at the speed axis. |
| <TO>.StatusWord.X6 (Done) | **Positioning axis/synchronous axis**   Set to the value "TRUE" when the actual velocity value reaches the positioning window within the tolerance time and remains in the window for the minimum dwell time. |
| **Speed axis**   Set to "TRUE" when the motion is complete and the speed setpoint is therefore equal to zero. |  |
| <TO>.ErrorWord.X12 (PositioningFault) | A positioning error has occurred. |

| Positions and times |  |
| --- | --- |
| Tag | Description |
| <TO>.PositioningMonitoring.ToleranceTime | Maximum permissible time until positioning window is reached  The time is started with the end of the setpoint interpolation. |
| <TO>.PositioningMonitoring.MinDwellTime | Minimum dwell time in position window |
| <TO>.PositioningMonitoring.Window | Positioning window |

| Standstill signal |  |
| --- | --- |
| Tag | Description |
| <TO>.StandstillSignal.VelocityThreshold | Velocity threshold for the standstill signal |
| <TO>.StandstillSignal.MinDwellTime | Minimum dwell time below the velocity threshold |

##### Following error monitoring

The following technology object tags are relevant for following error monitoring:

| Status indicators |  |
| --- | --- |
| Tag | Description |
| <TO>.StatusPositioning.FollowingError | Current following error |
| <TO>.ErrorWord.X11 (FollowingErrorFault) | Status indication, that the following error is too large |
| <TO>.WarningWord.X11 (FollowingErrorWarning) | Status indication, that the following error warning limit has been reached |

| Control bits |  |
| --- | --- |
| Tag | Description |
| <TO>.FollowingError.EnableMonitoring | Enable/disable following error monitoring |

| Timers |  |
| --- | --- |
| Tag | Description |
| <TO>.FollowingError.AdditionalSetpointDelayTime | Time constant for additional deceleration of position setpoint to calculate the following error in the time unit of the axis |

| Limits |  |
| --- | --- |
| Tag | Description |
| <TO>.FollowingError.MinVelocity | Lower velocity setpoint for the characteristic curve of the maximum following error |
| <TO>.FollowingError.MinValue | Permissible following error below the "<TO>.FollowingError.MinVelocity" |
| <TO>.FollowingError.MaxValue | Maximum permissible following error at maximum axis velocity |
| <TO>.FollowingError.WarningLevel | Warning limit as a percentage value relative to the maximum permissible following error (velocity-dependent in accordance with the characteristic curve) |

### Configuring a control loop (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of closed-loop control (S7-1500, S7-1500T)](#short-description-of-closed-loop-control-s7-1500-s7-1500t)
- [Position control in the drive with Dynamic Servo Control (DSC) (S7-1500, S7-1500T)](#position-control-in-the-drive-with-dynamic-servo-control-dsc-s7-1500-s7-1500t)
- [Position control in the PLC (S7-1500, S7-1500T)](#position-control-in-the-plc-s7-1500-s7-1500t)
- [Configuring position controller for drives with DSC (S7-1500, S7-1500T)](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)
- [Configuring position controller in the PLC (S7-1500, S7-1500T)](#configuring-position-controller-in-the-plc-s7-1500-s7-1500t)
- [Configuring the torque precontrol (S7-1500, S7-1500T)](#configuring-the-torque-precontrol-s7-1500-s7-1500t)
- [Dynamic filter (S7-1500, S7-1500T)](#dynamic-filter-s7-1500-s7-1500t)
- [Switching the position control off and on (S7-1500, S7-1500T)](#switching-the-position-control-off-and-on-s7-1500-s7-1500t)
- [Tags: Closed-loop control (S7-1500, S7-1500T)](#tags-closed-loop-control-s7-1500-s7-1500t)

#### Short description of closed-loop control (S7-1500, S7-1500T)

Together with the controller in the drive, the technology object forms a cascade control system. The innermost control cascade is the current control, the next cascade is the speed control. Both are located in the drive. The position controller is the outermost cascade and is in the technology object.

The position controller of the positioning axis/synchronous axis is a closed-loop P controller with or without velocity precontrol. Use the servo gain factor to set the gain of the proportional-action controller. Optionally, you can configure a torque precontrol.

When position control is enabled, encoder systems, actual value calculation, controllers and monitors are active.

If position control is inactive, encoder systems, actual value calculation and monitoring are active on the actual value side.

In follow-up mode, the setpoint tracks the actual value. Motion jobs are not executed. Actual position and actual velocity are updated. This means that tracking is possible when the axis is being moved by an external influence.

Follow-up mode is active in the following situations when [position-controlled mode](#switching-the-position-control-off-and-on-s7-1500-s7-1500t) <TO>.StatusWord.%X28 = FALSE:

- For alarms with stop response <TO>.ErrorDetail.Reaction = 4, 5
- Stopping and disabling a technology object with MC_Power.StopMode = 1, 3
- Technology object is disabled <TO>.StatusWord.%X0 = FALSE

##### Position controller configuration

Configure the position controller of the positioning axis/synchronous axis technology object:

- Control methods

  - [Position control in the drive with Dynamic Servo Control (DSC)](#position-control-in-the-drive-with-dynamic-servo-control-dsc-s7-1500-s7-1500t)
  - [Position control in the PLC](#position-control-in-the-plc-s7-1500-s7-1500t)
- Where does the position controller get its values?

  - [Configuring position controller in the PLC](#configuring-position-controller-in-the-plc-s7-1500-s7-1500t)
  - [Configuring position controller for drives with DSC](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)
- Setpoint filter

  - Configuring a dynamic filter

Optionally, configure the torque precontrol.

- [Configuring the torque precontrol](#configuring-the-torque-precontrol-s7-1500-s7-1500t)

Optimize the position controller during commissioning.

- [Optimize position controller](#optimize-position-controller-s7-1500-s7-1500t)

##### More information

For more information about axis control and controller optimization, refer to Siemens Industry Online Support in the FAQ entry [109779884](https://support.industry.siemens.com/cs/ww/en/view/109779884).

#### Position control in the drive with Dynamic Servo Control (DSC) (S7-1500, S7-1500T)

In drives that support Dynamic Servo Control (DSC), you can use the position controller in the drive. If you use telegrams that support DSC, DSC, and thus the position controller in the drive, is automatically activated.

The position controller is usually executed in the drive in the cycle clock of the speed control loop. In this way, you can set higher position controller gain (Kv factor) and increase the dynamic response for reference variable sequence and disturbance variable correction for highly dynamic drives.

When used with a SINAMICS drive, DSC is the standard case, since the faster control cycle in the drive (e.g. 125 μs) leads to even better control quality.

The following figure shows the effective control structure **with** DSC and with precontrol:

![Figure](images/172730363531_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Interpolator with motion control |
| ② | Internal consideration of speed control loop substitute time |
| ③ | Communication between controller and drive |

##### Requirements

The following requirements must be met to use DSC:

- The motor encoder (first encoder in the telegram) of the drive is used as the first encoder for the technology object.
- One of the following PROFIdrive telegrams is configured on the drive:

  - Standard telegram 5 or 6
  - SIEMENS telegram 105 or 106

##### Procedure

To configure position control in the drive with DSC for a positioning axis/synchronous axis, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Control loop > Dynamic Servo Control (DSC)".
2. Select the "Position control in the drive (DSC enabled)" option.
3. Apply the values from the drive.

   [Configuring position controller for drives with DSC](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)

##### Signal flow diagrams

For more information about the control structure in the form of signal flow diagrams for the positioning axis/synchronous axis technology object, refer to the [appendix](#signal-flow-diagrams-position-control-s7-1500-s7-1500t).

#### Position control in the PLC (S7-1500, S7-1500T)

The position controller is executed in the Motion Control application cycle, for example, 4 ms in the MC_Servo.

With position control in the CPU, the drive can be connected either isochronously or non-isochronously. If the drive supports isochronous mode, you can also connect it isochronously. You can find a description on how to connect a drive isochronously in section "[Adding and configuring drives](#adding-and-configuring-drives-s7-1500-s7-1500t)".

The following figure shows the effective control structure in position control in the controller:

![Figure](images/172730368651_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Interpolator with motion control |
| ② | Internal consideration of the signal propagation times and the speed-control loop substitute time |
| ③ | Communication between controller and drive |

##### Procedure

To configure position control in the CPU for a positioning axis/synchronous axis, follow these steps:

1. In the configuration of the technology object, navigate to "Extended parameters > Control loop > Dynamic Servo Control (DSC)".
2. Select the "Position control in the PLC" option.
3. Under "Position control", configure the values for precontrol, speed control loop substitute time and gain (Kv factor).

   [Configuring position controller in the PLC](#configuring-position-controller-in-the-plc-s7-1500-s7-1500t)

##### Signal flow diagrams

For more information about the control structure in the form of signal flow diagrams for the positioning axis/synchronous axis technology object, refer to the [appendix](#signal-flow-diagrams-position-control-s7-1500-s7-1500t).

#### Configuring position controller for drives with DSC (S7-1500, S7-1500T)

You configure automatic adoption of the values for the positioning axis/synchronous axis in the configuration under "Extended parameters > Control loop > Position control".

A description of how to adapt the adopted values for the position controller to your axis is provided in section "[Optimize position controller](#optimize-position-controller-s7-1500-s7-1500t)".

##### Automatic transfer from drive

If you have configured and optimized the assigned drive with SINAMICS Startdrive you can then apply the following values for the in the technology object from the drive.

- Gain (Kv factor): The technology object adopts 50% of the value from the drive.
- Speed control loop substitute time: The technology object adopts the value from the drive.
- Moment of inertia load/weight of the load
- Moment of inertia motor/weight motor
- Current control loop substitute time

Requirements:

- A drive is linked to the technology object.
- Dynamic Servo Control (DSC) is enabled.

**Drive optimized**

The display only applies if you have optimized the assigned drive with One Button Tuning (OBT).

- Display is green: Drive is optimized
- Display is gray: Drive is not optimized

**Optimizing values on the drive**

The green arrow takes you to the configuration of the drive in Startdrive. Optimize the drive there.

**Taking values from the drive**

When you click on this button you transfer the values from the drive to the technology object.

|  | SINAMICS Startdrive offline | SINAMICS Startdrive online |
| --- | --- | --- |
| **Monitoring off** | Offline values of the drive are applied.  The values are transferred as start value to the technology object. | Online values of the drive are applied.  The values are transferred as start value to the technology object. |
| **Monitoring on** | Offline values of the drive are applied.  The values are transferred as actual values to the technology object. | Online values of the drive are applied.  The values are transferred as actual values to the technology object. |

#### Configuring position controller in the PLC (S7-1500, S7-1500T)

You configure the values for the position controller for the positioning axis/synchronous axis in the configuration under "Extended parameters > Control loop > Position control".

The basics on configuration values are explained below.

The configuration of the torque precontrol is described in the section [Configuring torque precontrol](#configuring-the-torque-precontrol-s7-1500-s7-1500t).

A description of how to set the suitable values for the position controller to your axis during commissioning is provided in section "[Optimize position controller](#optimize-position-controller-s7-1500-s7-1500t)".

You need to optimize the speed controller separately on the drive.

##### Velocity precontrol

Configure the percentage velocity precontrol in this field.

The velocity precontrol can be used to minimize the velocity-based following error during position control. As a result, faster positioning may be achieved because the reference variable acts faster.

When using the velocity precontrol, the velocity setpoint is additionally switched to the output of the position controller. You can weight this additional setpoint by a factor.

With digital drive coupling, the velocity precontrol should be at 100%.

##### Speed control loop substitute time

In this field, configure the speed control loop substitute time (T<sub>vtc</sub>).

The speed control loop substitute time is included in the balancing filter.

The balancing filter is a simplified model of the closed speed control loop. The balancing filter is used to prevent the position controller from overriding the speed manipulated variable during the acceleration and deceleration phases. To accomplish this, the position setpoint of the position controller is delayed by the speed control loop substitute time in relation to the speed precontrol.

Note the following regarding the configuration of the speed control loop substitute time:

- If you do not use any speed precontrol (0%), the configuration of the speed control loop substitute time is not relevant.
- If you use speed precontrol (>0%) and set the speed control loop substitute time to 0.0 s (default value), the axis will overshoot. To find the right setting, optimize the position controller.

##### Gain (Kv factor)

In this field, you configure the gain Kv of the position control loop.

The Kv factor affects the following parameters:

- Positioning accuracy and stop control
- Uniformity of motion
- Positioning time

The better the mechanical conditions of the real axis (high stiffness), the higher the Kv factor can be configured. This reduces the following error, and a higher dynamic repsonse is achieved.

#### Configuring the torque precontrol (S7-1500, S7-1500T)

##### Torque precontrol

The torque precontrol, as part of the closed loop position control, allows for faster and more precise movement of the axis while maintaining smoother control settings.

The torque precontrol allows for a reduction of following error during acceleration and deceleration phases.

Note that the torque values of the torque precontrol of the technology object and the torque values specified by an instruction "MC_TorqueAdditive" are added. The resulting value is displayed in "<TO>.StatusTorqueData.TotalTorqueAdditive".

For a linear motor, the torque precontrol outputs force values.

When utilizing torque precontrol, you should configure jerk limitation for all motion jobs.

##### Requirements

- Additional telegram 750 used

  [Connecting force/torque data via SIEMENS additional telegram 750](#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)
- You have configured the inertia values for load and motor, either via "Automatic transfer from drive" or manually.

  [Configuring position controller for drives with DSC](#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)

  [Configure inertia values](#configure-inertia-values-s7-1500-s7-1500t)

##### Constraints

- When utilizing torque precontrol, you should configure jerk limitation for all motion jobs.
- Torque precontrol should not be used for a synchronous axis with actual value coupling.
- For improved control performance, it is recommended to additionally configure the dynamic filter with a moving average and a time constant of, for example, 10 ms. The optimum time constant may be different.
- The inertia load / mass load must be specified on the load side.

##### Torque precontrol mode

Configure the mode for the torque precontrol:

- Off

  No torque precontrol active
- Torque precontrol based on the acceleration of the axis

  The torque precontrol of the S7-1500 CPU provides torque setpoints based on the dynamic response of the axis.

  The value of the torque precontrol M<sub>add</sub> depends on:

  - Acceleration setpoint
  - Inertia value of the load and motor converted to the motor side.
  - Weighting factor as a percentage

##### Current control loop substitute time

Configure the current control loop substitute time <TO>.DynamicAxisModel.CurrentTimeConstant for the torque precontrol.

For drives with DSC, you can automatically take over the current control loop substitute time with "Automatic transfer from drive".

Manual configuration: For SINAMICS drives, a suitable guide value for the current control loop substitute time is the current control loop sampling time of drive T<sub>Current</sub> (p115[0])

T<sub>ctc</sub> = T<sub>Current</sub>

##### Weighting factor

Configure the weighting factor in percent <TO>.TorquePreControl.Scale for the torque precontrol.

##### Settings in the drive

- Activate interpolation for the additional torque between T<sub>DP</sub> and T<sub>current</sub> (p1409.0 = 1).
- Deactivate speed precontrol balancing dead time (p1428 = 0) and speed control balancing time constant (p1429 = 0).
- Configure the speed precontrol to the value "To Symmetrization" p1400.10 = 1.

#### Dynamic filter (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Brief description of dynamic filter (S7-1500, S7-1500T)](#brief-description-of-dynamic-filter-s7-1500-s7-1500t)
- [Dynamic filter as PT1 or PT2 filter (S7-1500, S7-1500T)](#dynamic-filter-as-pt1-or-pt2-filter-s7-1500-s7-1500t)
- [Dynamic response as sliding window demand filter (S7-1500, S7-1500T)](#dynamic-response-as-sliding-window-demand-filter-s7-1500-s7-1500t)

##### Brief description of dynamic filter (S7-1500, S7-1500T)

Axes that act mostly independent of one another are usually optimized independent of one another. Only in specific cases, such as in the highly dynamic interaction of a complete system, can you perform a dynamic adjustment following the actual optimization of individual axes.

The axes involved in a machine often have different mechanics. As a result, speed and position controllers of individual axes cannot be optimized identically. The axes can therefore have different dynamics.

Use the dynamic filter to adapt the dynamic response of axes to one another. The configuration of the dynamic filter is available for positioning and synchronous axes.

The dynamic filter is effective with closed loop position control with and without DSC. The dynamic filter delays the calculated position and velocity setpoints of the interpolator. Smoothing the position and velocity setpoints reduces jerk at the axis and can help minimize the generation of mechanical oscillations on the axis.

For axes in a synchronous operation with different speed control loop substitute time T<sub>vtc</sub> and used precontrol, we recommend a dynamic adjustment using the dynamic filter. Thus, the real traversing movements of the leading axis and the following axes can be more precisely synchronized because the same following error occurs in the axes involved.

To execute path motions with high contour accuracy, for kinematics with different speed control loop substitute times T<sub>vtc </sub> of the kinematics axes, a dynamic adaptation is required.

###### Configure the following error calculation with active dynamic filter

The following error is calculated from the delayed interpolated position setpoint by T<sub>i</sub>, T<sub>o</sub>, T<sub>Pn</sub> and T<sub>Servo</sub> minus the current actual position value. The deceleration of the position setpoint by the dynamic filter in the technology object or through additional filters in the drive is not taken into account when calculating the following error. This calculates a larger following error.

For correct calculation of the following error, set an additional delay time that delays the position setpoint when calculating the following error (<TO>.FollowingError.AdditionalSetpointDelayTime).

###### Dynamic filter - mode

You can specify the dynamic filter with the following modes:

- [PT1 or PT2 filter](#dynamic-filter-as-pt1-or-pt2-filter-s7-1500-s7-1500t) (<TO>.SetPointFilter.DynamicFilter.Mode = 1)

  The dynamic filter can be configured as a parameterizable PT2 setpoint filter with the time constants T<sub>1</sub>, T<sub>2</sub> and an additional parameterizable dead time T<sub>t</sub>. Use this mode for axes in synchronous operation.
- [Sliding window demand filter](#dynamic-response-as-sliding-window-demand-filter-s7-1500-s7-1500t) (<TO>.SetPointFilter.DynamicFilter.Mode = 2)

  The dynamic filter is used with either one or two sliding window demand filters in series. This mode is suitable for achieving high path accuracy in kinematic motions. Use this mode for axes with torque precontrol based on the acceleration of the axis (<TO>.TorquePreControl.Mode = 1)

##### Dynamic filter as PT1 or PT2 filter (S7-1500, S7-1500T)

The dynamic filter can be configured as a parameterizable PT2 setpoint filter with the time constants T<sub>1</sub>, T<sub>2</sub> and an additional parameterizable dead time T<sub>t</sub>. You use the filter to adjust axes with higher dynamic to the axis with the lowest dynamic. The dynamic filter is individually configurable for each positioning axis and synchronous axis.

The dynamic filter is disabled at an axis by default. To activate the dynamic filter with PT1 or PT2 filter on an axis, set the "PT1 or PT2 filter" mode in the configuration of the technology object under "Extended Parameters > Settings of the control loop > Dynamic Filter" ("<TO>.SetPointFilter.DynamicFilter.Mode" = 1) and configure one of the times T<sub>1</sub>, T<sub>2</sub> or T<sub>t</sub> with a value greater than 0.0.

The following table shows the effectiveness of the dynamic filter depending on the configured timers:

| T<sub>1</sub> | T<sub>2</sub> | T<sub>t</sub> | Active dynamic filter |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | Dynamic filter not active (default) |
| > 0.0 | 0.0 | 0.0 | PT1 setpoint filter without additional dead time |
| 0.0 | > 0.0 | 0.0 | PT1 setpoint filter without additional dead time |
| > 0.0 | > 0.0 | 0.0 | PT2 setpoint filter without additional dead time |
| 0.0 | 0.0 | > 0.0 | Exact setpoint delay via dead time |
| > 0.0 | 0.0 | > 0.0 | PT1 setpoint filter with additional dead time |
| 0.0 | > 0.0 | > 0.0 | PT1 setpoint filter with additional dead time |
| > 0.0 | > 0.0 | > 0.0 | PT2 setpoint filter with additional dead time |

The series connection of two PT1 filters creates a PT2 filter. PT1/PT2 filters act as a low pass. This smooths the position and velocity setpoints. For the damping degree D of PT2 filter, D ≥ 1. The PT2 filter cannot vibrate.

The damping degree D is calculated using the following equation.

![Figure](images/169974870411_DV_resource.Stream@PNG-de-DE.png)

The angular frequency ω is calculated using the following equation.

![Figure](images/165573038987_DV_resource.Stream@PNG-de-DE.png)

![Figure](images/172554254859_DV_resource.Stream@PNG-en-US.png)

###### Procedure

To set the dynamic filter, proceed as follows:

1. First, optimize all axes.
2. Determine the speed control loop substitute times T<sub>vtc</sub> of all axes (<TO>.DynamicAxisModel.VelocityTimeConstant)

   Example:

   Axis 1: T<sub>vtc</sub> = 0.004 s

   Axis 2: T<sub>vtc</sub> = 0.006 s

   Axis 1 is the more dynamic axis. The difference is 0.002 s.
3. Enable the dynamic filter in mode PT1or PT2 filter in the configuration of axis 1 under "Extended parameters > Settings of the control loop > Dynamic filter".
4. Configure the effective time constant of the dynamic filter (sum of the time constants T<sub>1</sub>, T<sub>2</sub>, T<sub>t</sub>) at axis 1 to 0.002 s. Depending on the preferred filter behavior, set one of the following variants for parameter assignment of the dynamic filter. In the configuration of the technology object, you can see a graphic representation of the step response.

   - PT1: T<sub>1</sub> = 0.002 s
   - PT2: T<sub>1</sub> = 0.001 s, T<sub>2</sub> = 0.001 s
   - Exact setpoint delay without smoothing: T<sub>t</sub> = 0.002 s
5. For calculating the following error on axis 1, assign the effective time constant of the dynamic filter as additional delay time of the setpoint position ("<TO>.FollowingError.AdditionalSetpointDelayTime" = 0.002 s = T<sub>1</sub> + T<sub>2</sub> + T<sub>t</sub>)<sub>.</sub>

   You can find more information in the section "[Following error monitoring](#following-error-monitoring-s7-1500-s7-1500t)".

##### Dynamic response as sliding window demand filter (S7-1500, S7-1500T)

The dynamic filter can be configured as a moving average with the time constants T<sub>1</sub>, T<sub>2</sub> and an additional parameterizable dead time T<sub>t</sub>. You use the filter to adjust axes with higher dynamic to the axis with the lowest dynamic. The dynamic filter is individually configurable for each positioning axis and synchronous axis.

The dynamic filter is disabled at the axis by default. To activate the dynamic filter with one moving average filter or two moving average filters connected in series, set the "Moving average filter" mode in the configuration of the technology object under "Extended Parameters > Settings of the control loop > Dynamic Filter" ("<TO>.DynamicFilter.Mode" = 2) and configure one of the times T<sub>1</sub>, T<sub>2</sub> or T<sub>t</sub> with a value greater than 0.0. The times T<sub>t</sub>, T<sub>1</sub> and T<sub>2</sub> are limited to 16 times the servo cycle.

The following table shows the effectiveness of the dynamic filter depending on the configured timers:

| T<sub>1</sub> | T<sub>2</sub> | T<sub>t</sub> | Active dynamic filter |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | Dynamic filter not active (default) |
| > 0.0 | 0.0 | 0.0 | One moving average filter without additional dead time |
| 0.0 | > 0.0 | 0.0 | One moving average filter without additional dead time |
| > 0.0 | > 0.0 | 0.0 | Two moving average filters in series without additional dead time |
| 0.0 | 0.0 | > 0.0 | Exact setpoint delay via dead time |
| > 0.0 | 0.0 | > 0.0 | One moving average filter with additional dead time |
| 0.0 | > 0.0 | > 0.0 | One moving average filter with additional dead time |
| > 0.0 | > 0.0 | > 0.0 | Two moving average filters with additional dead time |

The time T<sub>1</sub> defines the time window over which the dynamic filter calculates the average of the position setpoint and the velocity setpoint. With a servo cycle time of 4 ms and T<sub>1</sub> of 12 ms, the dynamic filter calculates the average of the values from the last 3 servo cycles and the current value. The values in the remaining time that do not correspond to a multiple of the servo cycle are weighted in proportion to time. With a servo cycle time of 4 ms and T<sub>1</sub> of 13 ms, the dynamic filter calculates the average of the values from the last 4 servo cycles and the current value. The current value and the values of the last three servo cycles are fully weighted. The value from the time window of the remaining time is weighted at only one-fourth. This corresponds to the remaining time of 1 ms for a servo cycle time of 4 ms.

To reduce mechanical oscillations on an axis and to additionally adapt the dynamic response of this axis to the dynamic response of a less dynamic axis with higher speed control loop substitute time T<sub>vtc</sub>, use two moving average filters in series (T<sub>1</sub> > 0, T<sub>2</sub> > 0).

![Figure](images/172600351627_DV_resource.Stream@PNG-en-US.png)

###### Dynamics of two coupled axes with different dynamic response

To adjust the dynamic response of two coupled axes with different dynamics, follow these steps:

1. Optimize all axes.
2. Determine the speed control loop substitute times T<sub>vtc</sub> of all axes (<TO>.DynamicAxisModel.VelocityTimeConstant)

   Example:

   Axis 1: T<sub>vtc</sub> = 0.004 s

   Axis 2: T<sub>vtc</sub> = 0.006 s

   Axis 1 is the more dynamic axis. The difference is 0.002 s.
3. Activate the dynamic filter in "Moving average" mode in the configuration of axis 1 under "Extended parameters > Settings of the control loop > Dynamic filter" (<TO>.SetpointFilter.DynamicFilter.Mode).
4. Configure the time constant T<sub>1 </sub> of the dynamic filter on axis 1 to 0.004 seconds. This corresponds to twice the time difference of the two speed control loop substitute times. Configure the time constants T<sub>t</sub> and T<sub>2</sub> to 0.0 s.
5. For calculating the following error on axis 1, configure the effective time constant of the dynamic filter as additional delay time of the setpoint position ("<TO>.FollowingError.AdditionalSetpointDelayTime" = 0.002 s‑= 0.5 · T<sub>1</sub> + 0.5 · T<sub>2</sub> +‑T<sub>t</sub> 0.5 · 0.004 s + 0 s + 0 s).

###### Reduce mechanical oscillations on an axis

To reduce mechanical vibrations on an axis, follow these steps:

1. Optimize all axes.
2. Determine the dominant natural frequency of the axis using appropriate measuring methods in the time or frequency domain. For this purpose, use the measurement functions of SINAMICS or position the axis via the control panel or user program and perform a measurement of the actual values.

   Example: The determined natural frequency is 23 Hz.
3. Activate the dynamic filter in "Moving average" mode in the configuration of axis 1 under "Extended parameters > Settings of the control loop > Dynamic filter" (<TO>.SetpointFilter.DynamicFilter.Mode).
4. Configure the time constant T<sub>1 </sub> of the dynamic filter on axis 1 to 1/23 Hz. This corresponds to 0.0435 s. Configure the time constants T<sub>t</sub> and T<sub>2</sub> to 0.0 s.
5. For calculating the following error on axis 1, configure the effective time constant of the dynamic filter as additional delay time of the setpoint position ("<TO>.FollowingError.AdditionalSetpointDelayTime" = 0.02175 s = 0.5 T<sub>1</sub> + 0.5 T<sub>2</sub> + T<sub>t</sub> = 0.5 · 0.0435 s‑+ 0 s + 0 s).

###### Reduce mechanical oscillations on an axis and adjust dynamic response to a coupled axis

To reduce mechanical oscillations on an axis and match the dynamics to a coupled axis, follow these steps:

1. Optimize all axes.
2. Determine the natural frequency of the axis using appropriate measuring methods.

   Example: The determined natural frequency is 23 Hz.
3. Determine the speed control loop substitute times T<sub>vtc</sub> (<TO>.DynamicAxisModel.VelocityTimeConstant).

   Example:

   Axis 1: T<sub>vtc</sub> = 0.004 s

   Axis 2: T<sub>vtc</sub> = 0.036 s

   Axis 1 is the more dynamic axis. The difference is 0.032 s.
4. Activate the dynamic filter in "Moving average" mode in the configuration of axis 1 under "Extended parameters > Settings of the control loop > Dynamic filter" (<TO>.SetpointFilter.DynamicFilter.Mode).
5. Configure the time constant T<sub>1 </sub> of the dynamic filter on axis 1 to 1/23 Hz. This corresponds to 0.0435 s. operating distance. This dampens the mechanical vibration.
6. Calculate the time constant T<sub>2</sub> of the dynamic filter on axis 1. Through use of the additional time constant T<sub>2</sub>, activate the second moving average filter and achieve an effective time constant of the dynamic filter of 0.032 s, which corresponds to the difference between the two axes: T<sub>2</sub> = 2 · 0.032 s – T<sub>1</sub> = 0.0205 s

   A negative time result indicates that axis 1 with the dynamic filter is "slower" than axis 2. The determined value should be set as the filter time on axis 2.
7. For calculating the following error on axis 1, configure the effective time constant of the dynamic filter as additional delay time of the setpoint position ("<TO>.FollowingError.AdditionalSetpointDelayTime" = 0.032 s = 0.5 T<sub>1</sub> + 0.5 T<sub>2</sub> + T<sub>t</sub> = 0.5 · 0.0435 s + 0.5 · 0.0205 s + 0 s).

#### Switching the position control off and on (S7-1500, S7-1500T)

The position control of an axis can be switched off and on again with the following Motion Control instructions in the non-position-controlled mode:

- MC_Power
- MC_MoveVelocity
- MC_MoveJog
- MC_MotionInVelocity

The non-position-controlled mode is indicated in the tag of the technology object "<TO>.StatusWord.X28 (NonPositionControlled)" = TRUE.

##### MC_Power

The axis is enabled without position control with "MC_Power.Enable" = TRUE and the parameter "StartMode" = 0. The position control remains switched off until a different Motion Control instruction changes the status of the position control.

##### MC_MoveVelocity and MC_MoveJog

A "MC_MoveVelocity" or "MC_MoveJog" job with "PositionControlled" = FALSE forces non-position-controlled operation.

A "MC_MoveVelocity" or "MC_MoveJog" job with "PositionControlled" = TRUE forces position-controlled operation.

The selected mode remains in effect after the job is completed.

##### MC_MotionInVelocity and MC_MotionInPosition

A "MC_MotionInVelocity" job with "PositionControlled" = FALSE forces non-position-controlled operation.

A "MC_MotionInVelocity" job with "PositionControlled" = TRUE forces position-controlled operation.

The selected mode remains in effect after the job is completed.

A "MC_MotionInPosition" job forces position-controlled operation.

##### Influence of additional Motion Control instructions

Starting the following Motion Control instructions forces position-controlled operation of the axis:

- MC_Home with "Mode" = 3, 5
- MC_MoveAbsolute
- MC_MoveRelative
- MC_MoveSuperimposed
- MC_MotionInPosition
- MC_GearIn
- MC_GearInPos (S7-1500T)
- MC_CamIn (S7-1500T)

The position control remains active after completing the corresponding jobs.

The Motion Control instructions "MC_Halt" and "MC_Stop" are executed in position-controlled and also in non-position-controlled operation. The status of the position control is not changed by "MC_Halt"/"MC_Stop".

A torque limiting activated with "MC_TorqueLimiting" is in effect even with non-position-controlled operation.

#### Tags: Closed-loop control (S7-1500, S7-1500T)

The following technology object tags are relevant for the control loop:

| Parameters |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.PositionControl.Kv | Proportional gain of the closed loop position control |  |
| <TO>.PositionControl.Kpc | Velocity precontrol of the closed loop position control [%] |  |
| <TO>.PositionControl.EnableDSC | Enable DSC |  |
| <TO>.DynamicAxisModel.VelocityTimeConstant | Speed control loop substitute time [s] |  |
| <TO>.PositionControl.­Control­Difference­Quantization.­Mode | Type of quantification  Configuration of a quantization when a drive with stepper motor interface is connected |  |
| 0 | No quantification |  |
| 1 | Quantization corresponding to encoder resolution |  |
| 2 | Quantization to a direct value (value input in "<TO>.PositionControl.­Control­Difference­Quantization.­Value") |  |
| Configuration is performed using the parameter view (data structure). |  |  |
| <TO>.PositionControl.­Control­Difference­Quantization.­Value | Value of quantification  Configuration of a value for quantization to a direct value ("<TO>.Position­Control.­Control­Difference­Quantization.­Mode" = 2)  The quantization value is specified in the position unit of the axis.   Configuration is performed using the parameter view (data structure). |  |
| <TO>.TorquePreControl.Mode | Mode of torque precontrol (effect only in position-controlled mode) |  |
| 0 | Torque precontrol not in effect |  |
| 1 | Torque precontrol based on the acceleration of the axis |  |
| <TO>.TorquePreControl.Scale | Weighting factor for the value of the torque precontrol [%] |  |
| <TO>.DynamicAxisModel.CurrentTimeConstant | Current control loop substitute time in time unit of the axis |  |

The following technology object tags are relevant for the dynamic filter:

| Parameters |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.SetpointFilter.DynamicFilter.Mode | Dynamic filter mode |  |
| 0 | Dynamic filter not active |  |
| 1 | PT1/PT2 filter + dead time |  |
| 2 | Sliding window demand + dead time |  |
| <TO>.SetpointFilter.DynamicFilter.T1 | First time constant of the sliding window demand The value is internally limited to the 16-fold servo clock. |  |
| <TO>.SetpointFilter.DynamicFilter.T2 | Second time constant of the sliding window demand The value is internally limited to the 16-fold servo clock. |  |
| <TO>.SetpointFilter.DynamicFilter.Tt | Additional dead time of the dynamic filter in the time unit of the axis The value is internally limited to the 16-fold servo clock. |  |
| <TO>.StatusServo.PositionAfterDynamicFilter | Position setpoint after the dynamic filter |  |
| <TO>.FollowingError.AdditionalSetpointDelayTime | Time constant for additional deceleration of position setpoint to calculate the following error in the time unit of the axis |  |

## Commissioning (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction (S7-1500, S7-1500T)](#introduction-s7-1500-s7-1500t-1)
- [Commissioning guidelines (S7-1500, S7-1500T)](#commissioning-guidelines-s7-1500-s7-1500t)
- [Take over master control and enable axis (S7-1500, S7-1500T)](#take-over-master-control-and-enable-axis-s7-1500-s7-1500t)
- [Operator controls for jogging, homing and positioning (S7-1500, S7-1500T)](#operator-controls-for-jogging-homing-and-positioning-s7-1500-s7-1500t)
- [Specify the dynamics in the axis control panel (S7-1500, S7-1500T)](#specify-the-dynamics-in-the-axis-control-panel-s7-1500-s7-1500t)
- [Homing with the axis control panel (S7-1500, S7-1500T)](#homing-with-the-axis-control-panel-s7-1500-s7-1500t)
- [Traversing the axis with the axis control panel (S7-1500, S7-1500T)](#traversing-the-axis-with-the-axis-control-panel-s7-1500-s7-1500t)
- [Optimize position controller (S7-1500, S7-1500T)](#optimize-position-controller-s7-1500-s7-1500t)
- [Disable axis and hand over master control (S7-1500, S7-1500T)](#disable-axis-and-hand-over-master-control-s7-1500-s7-1500t)

### Introduction (S7-1500, S7-1500T)

The following guidelines describe the steps that you should note when commissioning the Motion Control-specific components of your equipment.

The commissioning of other components of your automation system depends on the particular equipment configuration. Commissioning (not Motion Control) is described in the ["Automation System S7-1500"](https://support.industry.siemens.com/cs/ww/en/view/59191792) system manual.

### Commissioning guidelines (S7-1500, S7-1500T)

These guidelines serve as recommendations for commissioning equipment with Motion Control. The procedure is described using the example of a positioning axis technology object.

#### Requirement

- The configuration of the following components is complete:

  - CPU
  - BUS communication
  - Drives
  - Technology objects
- The user program has been created.
- The wiring of the CPU and of the associated I/O is complete.
- The commissioning and optimization of the drive is complete.

#### Procedure

Proceed as follows to commission the Motion Control-specific components of your equipment:

| Step | Action to be performed | Supported by TIA Portal |
| --- | --- | --- |
| Turn on CPU | Turn on the power supply and the CPU. | - |
| "Disable" position controller | Set the gain (Kv factor) of the position control loop to zero.   (This setting avoids unwanted drive movements that may be caused by incorrect parameterization of the position control loop.) | "Technology object > Configuration > Extended parameters > Settings of the control loop > Control loop" |
| Activate precontrol | Set the precontrol to 100 %. | "Technology object > Configuration > Extended parameters > Settings of the control loop > Control loop" |
| Load project into the CPU | Bring the CPU to the STOP mode.  Download your project to the CPU (load hardware and software). | - "Toolbar > Stop CPU" - "Toolbar > Download to device" |
| Create online connection to the CPU | Select the "Receive messages" check box under "Online & Diagnostics > Online Access".   Configure the interface of the TIA Portal and create an online connection with the CPU. | - Device configuration - "Online & Diagnostics > Online Access" |
| Disable Motion Control specific user program | In order to avoid conflicts with the axis control panel, lock the enabling of technology objects in your user program ("MC_Power.Enable" = FALSE). | - PLC programming - Motion Control instructions |
| Evaluating pending messages | Evaluate the message display in the inspector window. Resolve the causes of pending technology alarms. Acknowledge the technology alarms. | "Inspector window > Diagnostics > Message display" |
| Check hardware limit switches | Click the hardware limit switches. Check for correct message display (technology alarm 531). Acknowledge the technology alarm. | "Inspector window > Diagnostics > Message display" |
| Check the connection and configuration of the drive (setpoint) | Bring the CPU into the RUN mode. Open the Axis control panel and take over [master control](#take-over-master-control-and-enable-axis-s7-1500-s7-1500t).   Perform the following steps:  - Enable the technology object.  ⇒ The drive must turn itself on, and where applicable release the brake. The position is held. - Move the axis in [jog mode](#traversing-the-axis-with-the-axis-control-panel-s7-1500-s7-1500t) at low velocity in the positive direction. ⇒ The drive must move. The actual position value must increase (positive direction). - [Disable](#disable-axis-and-hand-over-master-control-s7-1500-s7-1500t) the technology object. ⇒ The drive must turn itself off, and where applicable apply the brake. | "Technology object > Commissioning > Axis control panel" |
| Check the connection and configuration of the encoder (actual value) | - Check the scaling of the actual values (rotation direction, distance evaluation, and resolution of the encoder) ⇒ The change in the actual mechanical position must match the change in the actual values. In case of deviations, correct the parameters assigned for mechanics under "Technology object > Extended parameters > Mechanics". - For absolute encoders, check the absolute encoder adjustment. To do this, move the axis to the start of the traversing range and switch the system off. After the restart, check the actual encoder values for correctness. Repeat this step likewise at the traversing range end. If there are deviations, correct the following:   - Settings for fine resolution under "Technology object > Data exchange with encoder"   - Zero-crossing position of the encoder     The position of the zero crossing can be changed by rotating the encoder in the dismantled state. With programmable encoders, the zero crossing can be adjusted by parameter assignment. The zero crossing must be outside the traversing range. | - "Technology object > Diagnostics > PROFIdrive telegram" - "Technology object > Commissioning > Axis control panel" |
| Specify dynamic parameters | For each traversing motion of the axis, enter the [dynamic parameters](#specify-the-dynamics-in-the-axis-control-panel-s7-1500-s7-1500t) in the axis control panel. |  |
| Checking the reference speed | Traverse the axis in [jog mode](#traversing-the-axis-with-the-axis-control-panel-s7-1500-s7-1500t) at low velocity in the positive direction.  ⇒ The displayed current velocity must match the velocity setpoint.  If the displayed current velocity deviates significantly from the velocity setpoint, adjust the reference speed. | - "Technology object > Hardware interface > Data exchange" - "Technology object > Commissioning > Axis control panel" |
| Homing axis | If necessary, you can [home](#homing-with-the-axis-control-panel-s7-1500-s7-1500t) the axis or set the home position. |  |
| Optimize position controller | Use the [Optimization](#optimize-position-controller-s7-1500-s7-1500t) commissioning function to optimize the gain (Kv) of the position control loop.  For this purpose, adapt following error limits as needed. | "Technology object > Commissioning > Optimization" |
| Transfer the gain Kv to the project. | Enter the gain Kv that you determined by means of the optimization function in your configuration data. Load your project into the CPU. | "Technology object > Configuration > Extended parameters > Control loop" |
| Enable Motion Control specific user program | Unlock the enabling technology objects lock in your user program ("MC_Power.Enable" = TRUE). | - PLC programming - Motion Control instructions |
| Check the functioning of the user program | Check the programmed functions of your user program. | - Watch and force tables - Online and diagnostic functions |
| Commissioning additional technology objects | To commission additional technology objects, perform the corresponding steps again. | See above. |

### Take over master control and enable axis (S7-1500, S7-1500T)

You traverse individual axes during commissioning. A user program is not required.

With the axis control panel, you assume master control for a technology object and control the motions of the axis.

The axis control panel is located in the project tree of the speed axis, positioning axis and synchronous axis technology objects under "Technology object > Commissioning".

With optimization, you take over the master control and optimize the gain and the speed control loop substitute time of the position controller.

You optimize the positioning axis and synchronous axis technology objects under "Technology object > Commissioning".

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis motions**  During commissioning, the axis can execute unexpected motions (e.g. due to erroneous configuration of the drive or the technology object). Any synchronized following axis is moved as well when moving a leading axis with the axis control panel or during optimization.  Therefore, perform the following precautionary measures before operation with the axis control panel or during optimization:  - Ensure that the EMERGENCY OFF switch is within the reach of the operator. - Enable the hardware limit switches. - Enable the software limit switches. - Ensure that following error monitoring is enabled. - Make sure that no following axis is coupled to the axis to be moved. |  |

#### Requirement

- The project has been created and downloaded to the CPU.
- The CPU must be in the RUN mode.
- The technology object is disabled by your user program ("MC_Power.Enable" = FALSE).
- The commissioning for the technology object is not used by another instance of the TIA Portal.

#### Procedure

Follow these steps to control the axis:

1. To assume master control of the technology object and to set up an online connection to the CPU, click "Activate" in the "Master control" area.

   A warning message is displayed.
2. If necessary, adapt the sign of life monitoring and click "OK".
3. To enable the technology object, click the "Enable" button in the "Axis" area.

#### Setting the sign-of-life monitoring time

| Monitoring time | Effect |
| --- | --- |
| Too low | Master control is frequently returned due to violation of the monitoring time and the axis stops with maximum deceleration because the communication time between the TIA Portal and CPU is longer than the configured monitoring time. |
| Appropriate | Monitoring time is not exceeded and the axis is stopped in time when the online connection is lost or sign of life monitoring is exceeded. Recommendation: 1000 ms to 2000 ms |
| Too high | Axis continues moving with the last setpoints of the axis control panel even though the connection between TIA Portal and CPU is interrupted or the communication time between TIA Portal and CPU is too long. The axis is not stopped in time because the monitoring time is still running. |

#### Result

An online connection to the CPU is established, the axis control panel or optimization takes over master control of the technology object, and the technology object is enabled.

#### Behavior while the axis control panel or optimization has the master control

The axis can only be traversed with the axis control panel or the optimization. Access to the axis is blocked by another instance of the TIA Portal.

The user program has no influence on the functions of the technology object. Motion Control jobs from the user program to the technology object are rejected with error ("ErrorID" = 16#8012: Axis control panel enabled).

Changes to the axis configuration will not become effective until the master control is taken over again.

In the following situations, the axis control panel or optimization will retain the master control and the axis keeps moving:

- The axis control panel/optimization is embedded in the TIA Portal, and you switch to a different window, for example, to the trace. Use the Split editor space option to use the axis control panel and the trace at the same time.

In the following situations, the axis control panel or optimization will retain the master control but stops the axis with maximum deceleration.

- The axis control panel or optimization is replaced in the TIA Portal, and you switch to a different window within the TIA Portal, for example, to the project tree. You change to a window outside of the TIA Portal.
- The "Stop" button is hidden by another dialog window or is no longer visible due to scrolling.

In the following situations, the axis is stopped with maximum deceleration and the axis control panel/optimization returns the master control to the user program.

- The online connection to the CPU fails and the time for sign of life monitoring has elapsed. The error message "ErrorID" = 16#8013 is displayed.

  Adapt the time for the sign-of-life monitoring in the warning.
- The online connection to the CPU is impaired by a communication load that is too high. The following message is entered in the alarm display log: "Commissioning error. Sign-of-life failure between controller and TIA Portal". Adapt the time for the sign-of-life monitoring in the warning.
- A dialog box (e.g. Save as) covers the axis control panel or optimization.

### Operator controls for jogging, homing and positioning (S7-1500, S7-1500T)

You can use the slider to execute the following functions of the axis control panel:

- [Homing with the axis control panel](#homing-with-the-axis-control-panel-s7-1500-s7-1500t)
- [Traversing the axis with the axis control panel](#traversing-the-axis-with-the-axis-control-panel-s7-1500-s7-1500t)

#### Jogging and homing velocity

The preset jogging and homing velocity is calculated as follows:

Jogging/homing velocity = configured velocity * slider position * "Adjust velocity" factor

#### Jog forward or backward

![Jog forward or backward](images/160095241227_DV_resource.Stream@PNG-de-DE.png)

**① Backward**

- Click the slider and drag the slider to the left.
- The further you drag the slider to the left, the higher the jogging velocity.
- To jog backward at the maximum, specified jogging velocity, click the ![Jog forward or backward](images/155899111051_DV_resource.Stream@PNG-de-DE.png) symbol.

**② Forward**

- Click the slider and drag the slider to the right.
- The further you drag the slider to the right, the higher the jogging velocity.
- To jog forward at the maximum preset jogging velocity, click the ![Jog forward or backward](images/155899119755_DV_resource.Stream@PNG-de-DE.png) symbol.

**Stop jogging**

- Release the pressed mouse button. The slider automatically jumps to zero and the axis/joint is stopped with the specified deceleration.

#### Active homing

![Active homing](images/160094525451_DV_resource.Stream@PNG-de-DE.png)

- Click the slider and drag the slider to the right. The further you drag the slider to the right, the higher the homing velocity.
- To home at the maximum preset velocity, click the ![Active homing](images/155899119755_DV_resource.Stream@PNG-de-DE.png) symbol.
- The homing stops automatically with the set dynamics.

**Cancel homing**

- To cancel homing, release the pressed mouse button.

#### Positioning

![Positioning](images/160095470603_DV_resource.Stream@PNG-de-DE.png)

- Click the slider and drag the slider to the right. The further you drag the slider to the right, the higher the positioning speed.
- To jog to the target position at the maximum preset jog velocity, click the ![Positioning](images/155899119755_DV_resource.Stream@PNG-de-DE.png) icon.
- Positioning stops automatically at the specified target position with the set dynamics.

**Stop positioning**

To stop positioning, release the pressed mouse button.

### Specify the dynamics in the axis control panel (S7-1500, S7-1500T)

In the operating modes of the axis control panel, you can specify the dynamics for traversing the axis.

Configure the dynamic limits before you use the axis control panel so that the specified dynamic values from the axis control panel are limited and the default setting of the dynamic values takes place accordingly.

During the first commissioning, you should traverse the axis at low dynamics. Reduce the dynamic values to less than the default setting. Increase the dynamic values gradually when traversing of the axis meets your expectations.

Next, adapt the dynamic default and the dynamic limits in the configuration of the technology object. The dynamic values from the axis control panel are not automatically applied to the configuration of the technology object.

#### Default setting of the dynamics values

The default setting of the dynamic values is as follows when calling the axis control panel:

| Dynamic value | Default value |
| --- | --- |
| Velocity/ Velocity setpoint | Velocity or speed at which the axis is traversed when "Homing" operating mode is not selected.  Default setting: 10% of the configured value in "Technology objects > Configuration > Extended parameters > Limits > Dynamics limits". |
| Acceleration | Acceleration with which the axis is traversed.  Default setting: 10% of the configured value in "Technology objects > Configuration > Extended parameters > Limits > Dynamics limits". |
| Deceleration | Deceleration with which the axis is traversed.  Default setting: 100% of the configured value in "Technology objects > Configuration > Extended parameters > Limits > Dynamic limits". |
| Jerk | Jerk with which the axis is traversed.  Default setting: 100% of the configured value in "Technology objects > Configuration > Extended parameters > Limits > Dynamic limits". |

#### Adjusting the velocity

Under "Adjust velocity", you correct the configured velocity using a percentage.

Example:

- Configured velocity in the axis control panel: 100 mm/s
- Adjust velocity: 50%
- Resulting velocity specification: 50 mm/s

You can set a value with the slider or enter a value between 1% and 200% directly in the text box below.

When master control is handed over, the last active position of the slider in the "Control" area is transferred as velocity override to the "<TO>.Override.Velocity" tag of the DriveAxis / positioning axis / synchronous axis technology object. This is not influenced by the "Adjust velocity" set factor.

### Homing with the axis control panel (S7-1500, S7-1500T)

With homing, you create the relationship between the position in the technology object and the mechanical position. The actual position value in the technology object is assigned to a homing mark at the same time. This homing mark represents a known mechanical position.

The "Active homing" operating mode corresponds to active homing with "Mode" = 3. The positioning axis/synchronous axis technology object performs a homing movement according to the configuration of the [active homing](#active-homing-s7-1500-s7-1500t).

The "Set actual position" operating mode in the axis control panel corresponds to direct homing (absolute) with "Mode" = 0.

The operating mode "Absolute encoder adjustment relative" in the axis control panel corresponds to the absolute encoder adjustment (absolute specification of position) with "MODE" = 7.

The operating mode "Absolute encoder adjustment absolute" in the axis control panel corresponds to the absolute encoder adjustment (relative specification of position) with "MODE" = 6.

For more detailed information on homing, refer to the section "[Homing](#homing-s7-1500-s7-1500t)".

#### Actively homing the axis

**Requirements**

- The axis is enabled in the axis control panel.
- The parameters for active [homing](#active-homing-s7-1500-s7-1500t) must be configured.

**Procedure**

1. Under "Operating mode", select "Active homing" from the drop-down list.
2. Enter the home position in the Position text box.
3. Enter the setpoints for acceleration, deceleration and jerk.
4. To start active homing, click the slider and drag the slider to the right.
5. To cancel homing, release the pressed mouse button.

**Result**

The axis executes the homing movement configured under "Active homing".

#### Setting the home position of an axis

**Requirements**

- The axis is enabled in the axis control panel.

**Procedure**

1. Under "Operating mode", select "Set actual position" from the drop-down list.
2. Enter the position to which the axis is to be homed.
3. Click the "Start" button.

**Result**

The entered position is set as the actual position and the axis status is set to "Homed".

#### Adjusting absolute encoder with absolute specification of position

**Requirements**

- The axis is enabled in the axis control panel.

**Procedure**

1. Under "Operating mode", select "Absolute encoder adjustment absolute" from the drop-down list.
2. In the text box "Position setpoint", enter the value by which the position is to be set.
3. Click the "Start" button.

**Result**

The current position is set to the value of the "Position" parameter.

#### Adjusting absolute encoder with relative specification of position

**Requirements**

- The axis is enabled in the axis control panel.

**Procedure**

1. Under "Operating mode", select "Absolute encoder adjustment relative" from the drop-down list.
2. In the "Offset" text box, enter the value by which the position is to be offset.
3. Click the "Start" button.

**Result**

The current position is shifted by the value of the "Offset" parameter.

### Traversing the axis with the axis control panel (S7-1500, S7-1500T)

#### Requirement

- The axis is enabled in the axis control panel.
- The axis is homed (position axis absolutely).

#### Jogging the axis

In "Jog" operating mode in the axis control panel, the motion commands are made by jogging.

1. Under "Operating mode", select "Jog" from the drop-down list.
2. Specify the dynamic parameters for the traversing motion.
3. To move the axis in the positive direction, click on the arrow symbol slider and drag the slider to the right.
4. To move the axis in the negative direction, click on the arrow symbol slider and drag the slider to the left.
5. To stop the traversing motion, release the pressed mouse button.

#### Position axis relatively

The positioning is executed as a controlled, relative traversing motion by the specified distance and the dynamic parameters assigned under "Control".

1. In the "Operating mode" drop-down list, select the entry "Relative positioning".
2. Specify the distance by which the axis is to be moved. A negative distance can be specified; it reverses the traversing direction. If you click on the arrow symbol and drag the slider to the right, the axis travels in negative direction and vice versa.
3. Specify the dynamic parameters for the traversing motion.
4. To move the axis by the specified distance, click on the arrow symbol and drag the slider to the right. To move the axis by the specified distance in the opposite direction, click on the arrow symbol and drag the slider to the left.
5. To stop the traversing motion, release the pressed mouse button.

#### Position axis absolutely

The positioning is executed as a controlled, absolute traversing motion by the specified distance and the dynamic parameters assigned under "Control".

1. In the "Operating mode" drop-down list, select "Absolute positioning".
2. Enter the target position.
3. Specify the dynamic parameters for the traversing motion.
4. Axes without modulo setting: To move the axis to the specified target position, drag the slider to the right.  
   Axes with Modulo setting: To move to the target position in the positive direction, drag the slider to the right. To move to the target position in the negative direction, drag the slider to the left. Position settings outside the modulo range are recalculated to the modulo range accordingly.
5. To stop the traversing motion, release the pressed mouse button.

### Optimize position controller (S7-1500, S7-1500T)

The following section describes how to optimize the position controller of a drive with the axis control panel.

How you proceed depends on the assigned drive:

- SINAMICS drive with DSC configured with Startdrive
- SINAMICS drive with DSC configured without Startdrive
- Drive without DSC

#### Requirements

- The CPU must be in the RUN mode.
- The project has been created and downloaded to the CPU.
- The technology object is disabled by your user program ("MC_Power.Enable" = FALSE).
- The axis control panel for the technology object is not used by another installation of the TIA Portal.
- The axis has been enabled for commissioning.

#### Procedure for SINAMICS drives with DSC configured with Startdrive

To optimize the position controller, follow these steps:

1. Configure values for the distance, duration, and dynamics of a test step in the "Measurement configuration" area.
2. Click the green arrow at "Optimize values in drive".

   You go to the optimization of the drive in Startdrive.
3. Optimize the controller automatically in Startdrive using One Button Tuning (OBT).
4. Navigate back to the optimization of the axis.

   The "Drive optimized" display is green.
5. Click the "Take values from drive" button.

   The following values are taken:

   - Gain (Kv factor): The technology object takes 50% of the value from the drive (r5276).
   - Speed control loop substitute time: The technology object adopts the value from the drive (r5277).

   The online values of the drive are applied when they are connected to the drive online in SINAMICS Startdrive. The offline values of the drive are applied when they are not connected to the drive online in SINAMICS Startdrive.
6. Click the "Forward" or "Backward" button to start a test step for optimization in the positive or negative direction.

   A setpoint is output for the specified duration according to the specified distance. The axis moves by the specified distance. A trace recording of the motion (setpoint and actual values) is created automatically in the "Trace" area.
7. Evaluate the trace recording.
8. If you are not yet satisfied with the optimization result, continue to adjust the gain (KV).
9. Apply the optimized parameters in the project.

#### Procedure for SINAMICS drives with DSC configured without Startdrive

Requirements: You have carried out a One Button Tuning (OBT) controller optimization in the configuration of the drive. If you use an alternative method for controller optimization in drive, then proceed as with the other drives.

To optimize the position controller, follow these steps:

1. If necessary, configure values for the distance, duration, and dynamics of a test step in the "Measurement configuration" area.
2. Configure the following values as actual values in the "Optimize position controller" area:

   - Gain (Kv factor): Apply 50% of the value from the parameter "r5276" of the drive to the technology object.

     Note that: Kv(TO) = 0.5 · 16.66666 · Kv(r5276)
   - Speed control loop substitute time: Apply the value from the parameter "r5277" of the drive to the technology object.

     Note that: vtc(TO) = 0.001 · vtc(r5277)
3. Click the "Forward" or "Backward" button to start a test step for optimization in the positive or negative direction.

   A setpoint is output for the specified duration according to the specified distance. The axis moves by the specified distance. A trace recording of the motion (setpoint and actual values) is created automatically in the "Trace" area.
4. Evaluate the trace recording.
5. If you are not yet satisfied with the optimization result, continue to adjust the gain (KV).
6. Apply the optimized parameters in the project.

#### Procedure for other drives

You use the procedure described here for the following drives:

- SINAMICS drives with DSC that are not optimized with OBT
- SINAMICS drives without DSC
- Third-party drives

To optimize the position controller, follow these steps:

1. In the "Master control" area, click the "Activate" button to activate master control for the technology object, and to establish an online connection to the CPU.

   A warning message is displayed.
2. In the "Axis" area, click the "Enable" button to enable the technology object.
3. Configure values for the distance and dynamics of a test step in the "Measurement configuration" area. Select a sufficiently long measurement duration to record the entire measurement with the trace. If the measurement duration is too short, you will see a warning when entering the value.
4. Configure the following values as actual values in the "Optimize position controller" area:

   - Precontrol: 0.0
   - Speed control loop substitute time: 0.0
   - Gain (Kv factor): 10.0
5. Click the "Forward" or "Backward" button to start a test step for optimization in the positive or negative direction.

   To traverse the specified distance, a trapezoid velocity profile is used. The velocity profile is calculated from the specified dynamic parameters and the distance. A trace recording of the motion (setpoint and actual values) is created automatically in the "Trace" area.
6. Evaluate the trace recording.
7. If required, increase in "measurement configuration" the values you use for "acceleration" and "deceleration".
8. Configure the following values as actual values in the "Optimize position controller" area:

   - Precontrol: 100.0
   - Speed control loop substitute time: 0.0
   - Gain (Kv factor): 90% of the determined value
9. Adjust the speed control loop equivalent time until no more overshoots occur.
10. Apply the optimized parameter values as start values in the project.

**Note**

Check whether the current or torque limitation is active in the drive. To get a meaningful trace recording, both limitations should not be active during optimization. To check this, record the tag "<TO>.StatusTorqueData.ActualTorque" when using telegram 750 or check the limitations directly in the drive.

#### Evaluating trace recordings

The trace recordings are not saved. Note the following properties of the curve:

- The curve shows a brief compensation time.
- The curve does not show any motion reversal of the actual position.
- When approaching the position setpoint, no overshoot occurs.
- The curve shows a stable overall behavior (oscillation-free curve).

The following trace recording shows a curve with a long settling time:

![Evaluating trace recordings](images/165573044107_DV_resource.Stream@PNG-de-DE.png)

The following trace recording shows a curve with overshoot when approaching the setpoint:

![Evaluating trace recordings](images/165573048203_DV_resource.Stream@PNG-de-DE.png)

The following trace recording shows a curve in which the gain is optimal and the overall response is steady:

![Evaluating trace recordings](images/165573077899_DV_resource.Stream@PNG-de-DE.png)

#### Adjust gain (Kv factor)

Proceed as follows to adapt the gain (Kv factor):

1. Increase the value with each test step, e.g. by 5%. If there is no major change in the control behavior, then select larger steps.
2. Click the "Forward" or "Backward" button to start another test step for optimization in the positive or negative direction.
3. Evaluate the trace recording.
4. Repeat steps 1 to 3 until no more overshoots occur in the trace recording.

#### Adjust speed control loop substitute time

With velocity precontrol, a simplified speed control loop model can be generated using the speed control loop substitute time. This prevents the velocity variable being overridden by the position controller during the acceleration and deceleration phases. To accomplish this, the position setpoint of the position controller is delayed by the amount of the speed control loop substitute time in relation to the velocity precontrol. Proceed as follows to adapt the speed control loop equivalent time:

1. Increase the value with each test step, e.g. by 1 ms.
2. On "Forward" or "Backward", perform another test step.
3. Evaluate the trace recording.
4. Repeat steps 1 to 3 until no more overshoots occur in the trace recording.

#### Transferring the optimized parameter values of the position controller to the project

To transfer the optimized parameter values of the position controller to your project, follow these steps:

1. Click the ![Transferring the optimized parameter values of the position controller to the project](images/165573081995_DV_resource.Stream@PNG-de-DE.png) icon next to the field of the respective parameter.

   A list of values is displayed.
2. Enter the determined value in the "Start value project" field of the value list. The value is then transferred to the configuration of the technology object in the project.
3. In the "Axis" area, click the "Disable" button to disable the technology object.
4. In the "Master control" area, click the "Deactivate" button to return master control to your user program.
5. Load your project into the CPU.

#### More information

For more information about axis control and axis optimization, refer to Siemens Industry Online Support in the FAQ entry [109779884](https://support.industry.siemens.com/cs/ww/en/view/109779884).

### Disable axis and hand over master control (S7-1500, S7-1500T)

> **Note**
>
> **No automatic transfer of the parameters to the technology object**
>
> The configured parameter values are discarded after master control is returned.
>
> Transfer the values as needed into your configuration. You can apply the values for the gain, precontrol and speed control loop equivalent time in your configuration using the "Project start value" value.

#### Requirement

- The axis is enabled in the axis control panel/optimization.
- The enabled technology object accepts Motion Control jobs.
- Speed control and position control are active.
- The actual values of the technology object are valid.

#### Procedure

Follow these steps to disable the axis and hand over the master control using the axis control panel or optimization:

1. To disable the technology object, click the "Disable" button in the "Axis" area.
2. To return master control to your user program, click the "Deactivate" button in the "Master control" area.

## Diagnostics (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction to diagnostics (S7-1500, S7-1500T)](#introduction-to-diagnostics-s7-1500-s7-1500t)
- [Speed-controlled axis technology object (S7-1500, S7-1500T)](#speed-controlled-axis-technology-object-s7-1500-s7-1500t)
- [Positioning axis technology object (S7-1500, S7-1500T)](#positioning-axis-technology-object-s7-1500-s7-1500t-1)
- [Technology object external encoder (S7-1500, S7-1500T)](#technology-object-external-encoder-s7-1500-s7-1500t)

### Introduction to diagnostics (S7-1500, S7-1500T)

The description of Motion Control diagnostics is limited to the diagnostics view of the technology objects in TIA Portal, the technology alarms and the error IDs on Motion Control instructions.

The following descriptions can be found in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation:

- [Diagnostics concept](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#diagnostics-concept-s7-1500-s7-1500t-1)
- [Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#technology-alarms-s7-1500-s7-1500t)
- [Error IDs in Motion Control instructions](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#error-ids-in-motion-control-instructions-s7-1500-s7-1500t)

A comprehensive description of the system diagnostics of the S7‑1500 CPU can be found in the ["Diagnostics" function manual](https://support.industry.siemens.com/cs/ww/en/view/59192926).

### Speed-controlled axis technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500, S7-1500T)](#status-and-error-bits-s7-1500-s7-1500t)
- [Motion status (S7-1500, S7-1500T)](#motion-status-s7-1500-s7-1500t)
- [PROFIdrive telegram (S7-1500, S7-1500T)](#profidrive-telegram-s7-1500-s7-1500t)

#### Status and error bits (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Axis status

The following table shows the possible axis status values:

| Status | Description |
| --- | --- |
| Simulation active | The axis is simulated in the CPU or used as the virtual axis. Setpoints are not output to the drive. |
| Enabled | The technology object has been enabled. The axis can be moved with motion jobs.  (<TO>.StatusWord.X0 (Enable)) |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "<TO>.ErrorDetail.Number" and "<TO>.ErrorDetail.Reaction" tags of the technology object.  (<TO>.StatusWord.X1 (Error)) |
| Restart active | The technology object is reinitialized.  (<TO>.StatusWord.X2 (RestartActive)) |
| Axis control panel enabled | The axis control panel is active. The axis control panel has master control over the technology object. The axis cannot be controlled from the user program.  (<TO>.StatusWord.X4 (ControlPanelActive)) |
| Drive ready | Drive is ready to execute setpoints.  (<TO>.StatusDrive.InOperation) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (<TO>.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Motion status

The following table shows the possible axis motion status values:

| Status | Description |
| --- | --- |
| Done (no job running) | There is no active motion job at the technology object.  (<TO>.StatusWord.X6 (Done)) |
| Jog | The axis is being moved with a job for jog mode of Motion Control instruction "MC_MoveJog" or from the axis control panel.  (<TO>.StatusWord.X9 (JogCommand)) |
| Speed setpoint | The axis is traversed with a job with speed setpoint of the Motion Control instruction "MC_MoveVelocity" or using the axis control panel.  (<TO>.StatusWord.X10 (VelocityCommand)) |
| Constant speed | The axis is moved with constant speed or is stationary.  (<TO>.StatusWord.X12 (ConstantVelocity)) |
| Accelerating | Axis is being accelerated.  (<TO>.StatusWord.X13 (Accelerating)) |
| Decelerating | The axis is being decelerated.  (<TO>.StatusWord.X14 (Decelerating)) |
| Torque limit active | At least the threshold value (default 90%) of the preset force/torque limitation acts on the axis.  (<TO>.StatusWord.X27 (InLimitation)) |
| Active stop job | The axis is stopped and disabled by Motion Control instruction "MC_Stop".  (<TO>.StatusWord2.X0 (StopCommand)) |

##### Warnings

The following table shows the possible warnings:

| Warning | Description |
| --- | --- |
| Configuration | One or several configuration parameters are adjusted internally at a certain time.  (<TO>.WarningWord.X1 (ConfigWarning)) |
| Job rejected | A job cannot be executed.  A Motion Control instruction cannot be executed because the necessary conditions have not been met.  (<TO>.WarningWord.X3 (CommandNotAccepted)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (<TO>.WarningWord.X6 (DynamicWarning)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (<TO>.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program with a Motion Control instruction or its use.  (<TO>.ErrorWord.X2 (UserFault)) |
| Drive | An error occurred in the drive.  (<TO>.ErrorWord.X4 (DriveFault)) |
| Data exchange | Communication with a connected device is faulty.  (<TO>.ErrorWord.X7 (CommunicationFault)) |
| I/O | An error occurred accessing a logical address.  (<TO>.ErrorWord.X13 (PeripheralError)) |
| Job rejected | A job cannot be executed.  A Motion Control instruction cannot be executed because necessary requirements have not been met (e.g. technology object not homed).  (<TO>.ErrorWord.X3 (CommandNotAccepted)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (<TO>.ErrorWord.X6 (DynamicError)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

---

**See also**

["StatusWord" tag (speed axis) (S7-1500, S7-1500T)](#statusword-tag-speed-axis-s7-1500-s7-1500t)
  
["ErrorWord" tag (speed axis) (S7-1500, S7-1500T)](#errorword-tag-speed-axis-s7-1500-s7-1500t)
  
["WarningWord" tag (speed axis) (S7-1500, S7-1500T)](#warningword-tag-speed-axis-s7-1500-s7-1500t)

#### Motion status (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Motion status" diagnostic function in the TIA Portal to monitor the motion status of the axis. The Diagnostics function is available in online operation.

##### "Setpoints" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Speed setpoint | Speed setpoint of the axis   (<TO>.Velocity) |
| Speed override | Speed setpoint correction as percentage  The speed setpoint specified in motion control instructions or set by the axis control panel are superimposed with an override signal and corrected as a percentage. Valid speed correction values range from 0.0 % to 200.0 %.  (<TO>.Override.Velocity) |

##### "Current values" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Actual speed | Actual speed of the axis   (<TO>.ActualSpeed) |

##### "Dynamic limits" area

This area displays the limit values for the dynamic parameters.

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Speed | Configured maximum speed  (<TO>.DynamicLimits.MaxVelocity) |
| Acceleration | Configured maximum acceleration  (<TO>.DynamicLimits.MaxAcceleration) |
| Deceleration | Configured maximum deceleration  (<TO>.DynamicLimits.MaxDeceleration) |
| Jerk | Configured maximum jerk  (<TO>.DynamicLimits.MaxJerk) |

#### PROFIdrive telegram (S7-1500, S7-1500T)

The "Technology object > Diagnostics > PROFIdrive telegram" diagnostics function is used in the TIA Portal to monitor the PROFIdrive telegram that the drive returns to the controller. The Diagnostics function is available in online operation.

##### "Drive" area

This area displays the following parameters contained in the PROFIdrive telegram from the drive to the controller:

- Status words "ZSW1" and "ZSW2"
- The speed setpoint (NSET) that was output to the drive
- The actual speed that was signaled from the drive (NACT)

### Positioning axis technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500, S7-1500T)](#status-and-error-bits-s7-1500-s7-1500t-1)
- [Motion status (S7-1500, S7-1500T)](#motion-status-s7-1500-s7-1500t-1)
- [PROFIdrive telegram (S7-1500, S7-1500T)](#profidrive-telegram-s7-1500-s7-1500t-1)

#### Status and error bits (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Axis status

The following table shows the possible axis status values:

| Status | Description |
| --- | --- |
| Simulation active | The axis is simulated in the CPU or used as the virtual axis. Setpoints are not output to the drive.  (<TO>.StatusWord.X25 (AxisSimulation)) |
| Enabled | The technology object has been enabled. You can move the axis with motion jobs.  (<TO>.StatusWord.X0 (Enable)) |
| Position-controlled mode | The axis is in position-controlled mode.  (Inversion of <TO>.StatusWord.X28 (NonPositionControlled)) |
| Homed | The technology object is homed. The relationship between the position in the technology object and the mechanical position was successfully created.  (<TO>.StatusWord.X5 (HomingDone)) |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "<TO>.ErrorDetail.Number" and "<TO>.ErrorDetail.Reaction" tags of the technology object.   (<TO>.StatusWord.X1 (Error)) |
| Restart active | The technology object is reinitialized.  (<TO>.StatusWord.X2 (RestartActive)) |
| Axis control panel enabled | The axis control panel is active. The axis control panel has master control over the technology object. You cannot control the axis from the user program.  (<TO>.StatusWord.X4 (ControlPanelActive)) |
| Drive ready | Drive is ready to execute setpoints.  (<TO>.StatusDrive.InOperation) |
| Encoder values valid | The actual encoder values are valid.  (<TO>.StatusSensor[1].State) |
| Encoder values valid (S7‑1500T) | The actual encoder values of encoder 1, encoder 2, encoder 3 or encoder 4 are valid.  (<TO>.StatusSensor[1..4].State) |
| Active encoder (S7‑1500T) | The encoder in effect operationally is encoder 1, encoder 2, encoder 3 or encoder 4.  (<TO>.OperativeSensor) |
| Encoder values homed | Encoder is homed with one of the following homing types:  - Active homing - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment   (<TO>.StatusSensor[1].Adjusted) |
| Encoder homed (S7-1500T) | Encoder 1, encoder 2, encoder 3 or encoder 4 is homed with one of the following homing types:  - Active homing - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment   (<TO>.StatusSensor[1..4].Adjusted) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (<TO>.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Status limit switch

The following table shows the possibilities for enabling the software and hardware limit switches:

| Status | Description |
| --- | --- |
| Negative SW limit switch approached. | The negative software limit switch has been approached.  (<TO>.StatusWord.X15 (SWLimitMinActive)) |
| Positive SW limit switch approached. | The positive software limit switch has been approached.  (<TO>.StatusWord.X16 (SWLimitMaxActive)) |
| Negative HW limit switch approached | The negative hardware limit switch has been approached or overtraveled.  (<TO>.StatusWord.X17 (HWLimitMinActive)) |
| Positive HW limit switch approached. | The positive hardware limit switch has been approached or overtraveled.  (<TO>.StatusWord.X18 (HWLimitMaxActive)) |

##### Motion status

The following table shows the possible axis motion status values:

| Status | Description |
| --- | --- |
| Done (no job running) | No job active at technology object.  (<TO>.StatusWord.X6 (Done)) |
| Homing job | The technology object executes a homing job of the Motion Control instruction "MC_Home" or from the axis control panel.  (<TO>.StatusWord.X11 (HomingCommand)) |
| Jog | The axis is being moved with a job for jog mode of Motion Control instruction "MC_MoveJog".  (<TO>.StatusWord.X9 (JogCommand)) |
| Velocity specification | The axis is traversed with a job with velocity specification of the Motion Control instruction "MC_MoveVelocity" or from the axis control panel.  (<TO>.StatusWord.X10 (VelocityCommand)) |
| Positioning job | The axis is traversed with a positioning job of Motion Control instruction "MC_MoveAbsolute" or "MC_MoveRelative" or from the axis control panel.  (<TO>.StatusWord.X8 (PositioningCommand)) |
| Constant velocity | The axis is moved with constant velocity or is stationary.  (<TO>.StatusWord.X12 (ConstantVelocity)) |
| Standstill | The axis is at a standstill.  (<TO>.StatusWord.X7 (StandStill)) |
| Accelerating | Axis is being accelerated.  (<TO>.StatusWord.X13 (Accelerating)) |
| Decelerating | The axis is being decelerated.  (<TO>.StatusWord.X14 (Decelerating)) |
| Torque limit active | At least the threshold value (default 90%) of the preset force/torque limitation acts on the axis.  (<TO>.StatusWord.X27 (InLimitation)) |
| Active stop job | The axis is stopped and disabled by Motion Control instruction "MC_Stop".  (<TO>.StatusWord2.X0 (StopCommand)) |
| Superimposed motion | The motion of the axis is superimposed by at least one overlapping Motion Control instruction (OR logic operation).  (<TO>.StatusWord.X23 (MoveSuperimposedCommand);  <TO>.StatusWord2.X6 (MotionInSuperimposedCommand);  <TO>.StatusWord2.X7 (HaltSuperimposedCommand)) |

##### Warnings

The following table shows the possible warnings:

| Warning | Description |
| --- | --- |
| Configuration | One or more configuration parameters are being internally adapted temporarily.  (<TO>.WarningWord.X1 (ConfigWarning)) |
| Job rejected | Job cannot be executed.  You cannot execute a Motion Control instruction because necessary requirements are not fulfilled.  (<TO>.WarningWord.X3 (CommandNotAccepted)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (<TO>.WarningWord.X6 (DynamicWarning)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (<TO>.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program with a Motion Control instruction or its use.  (<TO>.ErrorWord.X2 (UserFault)) |
| Drive | An error occurred in the drive.  (<TO>.ErrorWord.X4 (DriveFault)) |
| Encoder | An error occurred in the encoder system.  (<TO>.StatusSensor[1].Error) |
| Encoder (S7‑1500T) | An error has occurred in the encoder system of encoder 1, encoder 2, encoder 3 or encoder 4.  (<TO>.StatusSensor[1..4].Error) |
| Data exchange | Communication with a connected device is faulty.  (<TO>.ErrorWord.X7 (CommunicationFault)) |
| I/O | An error occurred accessing a logical address.  (<TO>.ErrorWord.X13 (PeripheralError)) |
| Job rejected | A job cannot be executed.  You cannot execute a Motion Control instruction because necessary requirements are not fulfilled (for example, technology object not homed).  (<TO>.ErrorWord.X3 (CommandNotAccepted)) |
| Homing | An error occurred during a homing process.  (<TO>.ErrorWord.X10 (HomingFault)) |
| Positioning | The positioning axis was not positioned correctly at the end of a positioning motion.  (<TO>.ErrorWord.X12 (PositioningFault)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (<TO>.ErrorWord.X6 (DynamicError)) |
| Following error | The maximum permitted following error has been exceeded.  (<TO>.ErrorWord.X11 (FollowingErrorFault)) |
| SW limit switch | A software limit switch has been reached.  (<TO>.ErrorWord.X8 (SwLimit)) |
| HW limit switch | A hardware limit switch has been reached or overtraveled.  (<TO>.ErrorWord.X9 (HWLimit)) |
| Adaptation | An error occurred during data adaption.  (<TO>.ErrorWord.X15 (AdaptionError)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

---

**See also**

["StatusWord" tag (positioning axis) (S7-1500, S7-1500T)](#statusword-tag-positioning-axis-s7-1500-s7-1500t)
  
["ErrorWord" tag (positioning axis) (S7-1500, S7-1500T)](#errorword-tag-positioning-axis-s7-1500-s7-1500t)
  
["WarningWord" tag (positioning axis) (S7-1500, S7-1500T)](#warningword-tag-positioning-axis-s7-1500-s7-1500t)

#### Motion status (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Motion status" diagnostic function in the TIA Portal to monitor the motion status of the axis. The Diagnostics function is available in online operation.

##### "Setpoints" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Target position | Current target position of an active positioning job  The target position value is only valid during execution of a positioning job.  (<TO>.StatusPositioning.TargetPosition) |
| Position setpoint | Setpoint position of the axis  (<TO>.Position) |
| Velocity setpoint | Velocity setpoint of the axis  (<TO>.Velocity) |
| Velocity override | Percentage correction of the velocity specification  The velocity setpoint specified in Motion Control instructions or set by the axis control panel is superimposed with an override signal and corrected as a percentage. Permissible velocity correction values are 0.0% to 200.0%.  (<TO>.Override.Velocity) |

##### "Current values" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Operative encoder | Operative encoder of the axis |
| Actual position | Actual position of the axis  If the technology object is not homed, then the value is displayed relative to the position that existed when the technology object was enabled.   (<TO>.ActualPosition) |
| Actual velocity | Actual velocity of the axis  (<TO>.ActualVelocity) |
| Following error | Following error of the axis  (<TO>.StatusPositioning.FollowingError) |

##### "Dynamic limits" area

This area displays the limit values for the dynamic parameters.

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Velocity | Configured maximum velocity  (<TO>.DynamicLimits.MaxVelocity) |
| Acceleration | Configured maximum acceleration  (<TO>.DynamicLimits.MaxAcceleration) |
| Deceleration | Configured maximum deceleration  (<TO>.DynamicLimits.MaxDeceleration) |
| Jerk | Configured maximum jerk  (<TO>.DynamicLimits.MaxJerk) |

#### PROFIdrive telegram (S7-1500, S7-1500T)

The "Technology object > Diagnostics > PROFIdrive telegram" diagnostics function is used in the TIA Portal to monitor the PROFIdrive telegrams returned by the drive and encoder. The display of the Diagnostics function is available in online operation.

##### "Drive" area

This area displays the following parameters contained in the PROFIdrive telegram from the drive to the controller:

- Status words "ZSW1" and "ZSW2"
- The speed setpoint (NSET) that was output to the drive
- The actual speed that was signaled from the drive (NACT)

##### "Encoder" area

in the areas "Encoder" for CPU S7-1500 or "Encoder 1" to "Encoder 4" for CPU S7-1500T, the following parameters from the PROFIdrive telegram are displayed by the encoder to the controller.

- Status word "Gx_ZSW"
- The actual position value "Gx_XIST1" (cyclic actual encoder value)
- The actual position value "Gx_XIST2" (absolute encoder value)

### Technology object external encoder (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500, S7-1500T)](#status-and-error-bits-s7-1500-s7-1500t-2)
- [Motion status (S7-1500, S7-1500T)](#motion-status-s7-1500-s7-1500t-2)
- [PROFIdrive telegram (S7-1500, S7-1500T)](#profidrive-telegram-s7-1500-s7-1500t-2)

#### Status and error bits (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Encoder status

The following table shows the possible external encoder status values:

| Status | Description |
| --- | --- |
| Encoder enabled | The technology object has been enabled.  (<TO>.StatusWord.X0 (Enable)) |
| Homed | The technology object is homed. The relationship between the position in the technology object and the mechanical position was successfully created.  (<TO>.StatusWord.X5 (HomingDone)) |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "<TO>.ErrorDetail.Number" and "<TO>.ErrorDetail.Reaction" tags of the technology object.  (<TO>.StatusWord.X1 (Error)) |
| Restart active | The technology object is being reinitialized.  (<TO>.StatusWord.X2 (RestartActive)) |
| Encoder values valid | The actual encoder values are valid.  (<TO>.StatusSensor[n].State) |
| Encoder values homed | Encoder is homed with one of the following homing types:  - Active homing - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment   (<TO>.StatusSensor[n].Adjusted) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (<TO>.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Motion status

The following table shows the possible states of the job execution:

| Status | Description |
| --- | --- |
| Done (no job running) | No Motion Control job is active at the technology object (enable by "MC_Power" job excepted).  (<TO>.StatusWord.X6 (Done)) |
| Homing job | The technology object executes a homing job of the Motion Control instruction "MC_Home".  (<TO>.StatusWord.X11 (HomingCommand)) |
| Standstill | The axis is at a standstill.  (<TO>.StatusWord.X7 (StandStill)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (<TO>.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program with a Motion Control instruction or its use.  (<TO>.ErrorWord.X2 UserFault)) |
| Encoder | An error occurred in the encoder system.  (<TO>.ErrorWord.X5 (SensorFault)) |
| Data exchange | Missing or faulty communication.  (<TO>.ErrorWord.X7 (CommunicationFault)) |
| Adaptation | An error occurred during data adaption.  (<TO>.ErrorWord.X15 (AdaptionError)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

---

**See also**

["StatusWord" tag (external encoder) (S7-1500, S7-1500T)](#statusword-tag-external-encoder-s7-1500-s7-1500t)
  
["ErrorWord" tag (external encoder) (S7-1500, S7-1500T)](#errorword-tag-external-encoder-s7-1500-s7-1500t)
  
["WarningWord" tag (external encoder) (S7-1500, S7-1500T)](#warningword-tag-external-encoder-s7-1500-s7-1500t)

#### Motion status (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Motion status" diagnostic function in the TIA Portal to monitor the actual encoder values. The diagnostics function is available in online operation.

##### "Current values" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Actual position | Actual position of the axis   If the technology object is not homed, then the value is displayed relative to the position that existed when the technology object was enabled.   (<TO>.ActualPosition) |
| Actual velocity | Actual velocity of the axis  (<TO>.ActualVelocity) |

#### PROFIdrive telegram (S7-1500, S7-1500T)

The "Technology object > Diagnostics > PROFIdrive telegram" diagnostic function is used in the TIA Portal to monitor the PROFIdrive telegram of the encoder. The display of the diagnostics function is available in technology object online mode.

##### "Encoder" area

This area displays the following parameters contained in the PROFIdrive telegram that the encoder returns to the controller:

- Status word "G1_ZSW"
- The actual position value "G1_XIST1" (cyclic actual encoder value)
- The actual position value "G1_XIST2" (absolute value of the encoder)

## Tags of the technology object data blocks (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Tags of the speed axis technology object (S7-1500, S7-1500T)](#tags-of-the-speed-axis-technology-object-s7-1500-s7-1500t)
- [Tags of the positioning axis technology object (S7-1500, S7-1500T)](#tags-of-the-positioning-axis-technology-object-s7-1500-s7-1500t)
- [Tags of the technology object external encoder (S7-1500, S7-1500T)](#tags-of-the-technology-object-external-encoder-s7-1500-s7-1500t)

### Tags of the speed axis technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t)
- [Actual values and setpoints (speed axis) (S7-1500, S7-1500T)](#actual-values-and-setpoints-speed-axis-s7-1500-s7-1500t)
- ["Simulation" tag (speed axis) (S7-1500, S7-1500T)](#simulation-tag-speed-axis-s7-1500-s7-1500t)
- ["VirtualAxis" tag (speed axis) (S7-1500, S7-1500T)](#virtualaxis-tag-speed-axis-s7-1500-s7-1500t)
- ["Actor" tag (speed axis) (S7-1500, S7-1500T)](#actor-tag-speed-axis-s7-1500-s7-1500t)
- ["TorqueLimiting" tag (speed axis) (S7-1500, S7-1500T)](#torquelimiting-tag-speed-axis-s7-1500-s7-1500t)
- ["LoadGear" tag (speed axis) (S7-1500, S7-1500T)](#loadgear-tag-speed-axis-s7-1500-s7-1500t)
- ["Units" tag (speed axis) (S7-1500, S7-1500T)](#units-tag-speed-axis-s7-1500-s7-1500t)
- ["DynamicLimits" tag (speed axis) (S7-1500, S7-1500T)](#dynamiclimits-tag-speed-axis-s7-1500-s7-1500t)
- ["DynamicDefaults" tag (speed axis) (S7-1500, S7-1500T)](#dynamicdefaults-tag-speed-axis-s7-1500-s7-1500t)
- ["Override" tag (speed axis) (S7-1500, S7-1500T)](#override-tag-speed-axis-s7-1500-s7-1500t)
- ["StatusDrive" tag (speed axis) (S7-1500, S7-1500T)](#statusdrive-tag-speed-axis-s7-1500-s7-1500t)
- ["StatusTorqueData" tag (speed axis) (S7-1500, S7-1500T)](#statustorquedata-tag-speed-axis-s7-1500-s7-1500t)
- ["StatusMotionIn" tag (speed axis) (S7-1500, S7-1500T)](#statusmotionin-tag-speed-axis-s7-1500-s7-1500t)
- ["StatusInterpreterMotion" tag (speed axis) (S7-1500, S7-1500T)](#statusinterpretermotion-tag-speed-axis-s7-1500-s7-1500t)
- ["StatusWord" tag (speed axis) (S7-1500, S7-1500T)](#statusword-tag-speed-axis-s7-1500-s7-1500t)
- ["StatusWord2" tag (speed axis) (S7-1500, S7-1500T)](#statusword2-tag-speed-axis-s7-1500-s7-1500t)
- ["ErrorWord" tag (speed axis) (S7-1500, S7-1500T)](#errorword-tag-speed-axis-s7-1500-s7-1500t)
- ["ErrorDetail" tag (speed axis) (S7-1500, S7-1500T)](#errordetail-tag-speed-axis-s7-1500-s7-1500t)
- ["WarningWord" tag (speed axis) (S7-1500, S7-1500T)](#warningword-tag-speed-axis-s7-1500-s7-1500t)
- ["ControlPanel" tag (speed axis) (S7-1500, S7-1500T)](#controlpanel-tag-speed-axis-s7-1500-s7-1500t)
- ["InternalToTrace" tag (speed axis) (S7-1500, S7-1500T)](#internaltotrace-tag-speed-axis-s7-1500-s7-1500t)

#### Legend (S7-1500, S7-1500T)

|  |  |  |
| --- | --- | --- |
| Tag | Name of the tag |  |
| Data type | Data type of the tag |  |
| Values | Value range of the tag - minimum value to maximum value  If no specific value is shown, the value range limits of the relevant data type apply or the information under "Description". |  |
| W | Effectiveness of changes in the technology data block |  |
| DIR | Direct:  Values are changed via direct assignment and take effect at the start of the next MC_Servo. |  |
| CAL | At call of Motion Control instruction:  Values are changed directly and take effect at the start of the next MC_Servo after the call of the corresponding Motion Control instruction in the user program. |  |
| RES | Restart:  Changes to the start value in the load memory are made using the extended instruction "WRIT_DBL" (write to DB in load memory). Changes will not take effect until after restart of the technology object. |  |
| RON | Read only:  The tag cannot and must not be changed during runtime of the user program. |  |
| Description | Description of the tag |  |

Access to the tags is with "<TO>.<tag name>". The placeholder <TO> represents the name of the technology object.

#### Actual values and setpoints (speed axis) (S7-1500, S7-1500T)

The following tags indicate the setpoint and actual values of the technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag | Data type | Values | W | Description |
| --- | --- | --- | --- | --- |
| Velocity | LREAL | - | RON | Velocity setpoint/speed setpoint |
| ActualSpeed | LREAL | - | RON | With analog setpoint = 0.0:  Actual speed of motor in 1/min |
| Acceleration | LREAL | - | RON | Setpoint acceleration |
| VelocitySetpoint | LREAL | -1.0E12 to 1.0E12 | RON | Output velocity setpoint/speed setpoint |

#### "Simulation" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Simulation.<tag name>" contains the configuration of the simulation mode. In simulation mode, you can simulate axes without a real drive in the CPU.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Simulation. |  | TO_Struct_AxisSimulation |  |  |  |  |
|  | Mode | UDINT | 0, 1 | RES<sup>1)</sup> | Simulation mode |  |
| 0 | No simulation, normal operation |  |  |  |  |  |
| 1 | Simulation mode |  |  |  |  |  |
| <sup>1)</sup> Technology version V2.0: RON |  |  |  |  |  |  |

#### "VirtualAxis" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.VirtualAxis.<tag name>" contains the configuration of the virtual operation of the axis. A virtual axis is often used as a virtual leading axis in order to generate the setpoints for several real following axes in synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| VirtualAxis. |  | TO_Struct_VirtualAxis |  |  |  |  |
|  | Mode | UDINT | 0, 1 | RON | Virtual axis |  |
| 0 | No virtual axis |  |  |  |  |  |
| 1 | Technology version ≥ V7.0:  The behavior of a virtual axis is identical to the behavior of an axis in simulation. The actual values are generated via the control loop and a simplified drive model.  Technology version ≥ V8.0:  In technology version V8.0, the behavior of the virtual axis has been changed. The behavior of a virtual axis is no longer identical to the behavior of an axis in simulation.  The position and velocity setpoints are directly adopted as actual values with an application cycle delay. The feedback loop and the drive model are not simulated. The dynamic filter is effective.  To maintain compatibility with virtual axes of technology versions ≤ V7.0 for an axis:  1. Interconnect the axis in simulation (<TO>.Simulation.Mode" = 1). 2. Disable the virtual axis (<TO>.VirtualAxisMode = 0) |  |  |  |  |  |

#### "Actor" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Actor.<tag name>" contains the controller-side configuration of the drive.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Actor. |  |  | TO_Struct_Actor |  |  |  |  |
|  | Type |  | DINT | 0, 1 | RON | Drive connection |  |
| 0 | Analog output |  |  |  |  |  |  |
| 1 | PROFIdrive telegram |  |  |  |  |  |  |
| InverseDirection |  | BOOL | - | RES | Inversion of the setpoint |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| DataAdaption |  | DINT | 0, 1 | RES | Automatic transfer of the drive values reference speed, maximum speed and reference torque in the device |  |  |
| 0 | No automatic transfer, manual configuration of values |  |  |  |  |  |  |
| 1 | Automatic transfer of values configured in the drive to the configuration of the technology object |  |  |  |  |  |  |
| Efficiency |  | LREAL | 0.0 to 1.0 | RES | Efficiency of gear |  |  |
| RemoveEnableReaction |  | WORD | 16#1 to 16#7 | RES | Stop reaction on "Remove enable" |  |  |
| 16#1 | OFF1 – Ramp stop - Braking with ramp-function generator |  |  |  |  |  |  |
| 16#3 | OFF2 – Coast stop - Coast down |  |  |  |  |  |  |
| 16#5 | OFF3 – Quick stop - Quick stop |  |  |  |  |  |  |
| 16#7 | OFF3 – Quick stop (compatible configuration for technology versions up to V7) |  |  |  |  |  |  |
| 16#2  16#4  16#6 | Invalid |  |  |  |  |  |  |
| Interface. |  | TO_Struct_ActorInterface |  |  |  |  |  |
|  | AddressIn | VREF | 0 to 65535 | RON | Input address for the PROFIdrive telegram |  |  |
| AddressOut | VREF | 0 to 65535 | RON | Output address for the PROFIdrive telegram or the analog setpoint |  |  |  |
| EnableDriveOutput | BOOL | - | RES | "Enable output" for analog drives |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| EnableDriveOutput­Address | VREF | 0 to 65535 | RON | Address for the "Enable output" for analog setpoint |  |  |  |
| DriveReadyInput | BOOL | - | RES | "Ready input" for analog drives   The analog drive signals its readiness to receive speed setpoints. |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| DriveReadyInput­Address | VREF | 0 to 65535 | RON | Address for the "Enable input" for analog setpoint |  |  |  |
| EnableTorqueData | BOOL | - | RES | Torque data |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| TorqueDataAddressIn | VREF | 0 to 65535 | RON | Input Address of the Telegram 750 |  |  |  |
| TorqueDataAddress­Out | VREF | 0 to 65535 | RON | Output address of the telegram 750 |  |  |  |
| DriveParameter. |  | TO_Struct_ActorDriveParameter |  |  |  |  |  |
|  | ReferenceSpeed | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the speed setpoint (N-set) of the drive  The speed setpoint is transferred in the PROFIdrive telegram as a normalized value from -200% to 200% of the "ReferenceSpeed".  For setpoint specification via an analog output, the analog output can be operated in the range from -117% to 117%, provided the drive permits this. |  |  |
| MaxSpeed | LREAL | 0.0 to 1.0E12 | RES | Maximum value for the speed setpoint of the drive (N-set)  (PROFIdrive: MaxSpeed ≤ 2 × ReferenceSpeed  Analog setpoint: MaxSpeed ≤ 1.17 × ReferenceSpeed) |  |  |  |
| ReferenceTorque | LREAL | 0.0 to 1.0E12 | RES | Reference torque of drive (p2003)  Valid for the standard motor setting. |  |  |  |

#### "TorqueLimiting" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.TorqueLimiting.<tag name>" contains the configuration of the torque limiting.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TorqueLimiting. |  |  | TO_Struct_TorqueLimiting |  |  |  |  |
|  | LimitBase |  | DINT | 0, 1 | RES | Torque limiting |  |
| 0 | Motor side |  |  |  |  |  |  |
| 1 | Load side |  |  |  |  |  |  |
| PositionBasedMonitorings |  | DINT | 0, 1 | RES | Positioning and following error monitoring |  |  |
| 0 | Monitoring deactivated |  |  |  |  |  |  |
| 1 | Monitoring activated |  |  |  |  |  |  |
| LimitDefaults. |  | TO_Struct_TorqueLimitingLimitDefaults |  |  |  |  |  |
|  | Torque | LREAL | 0.0 to 1.0E12 | CAL | Limiting torque |  |  |
| Force | LREAL | 0.0 to 1.0E12 | CAL | Limiting force |  |  |  |

#### "LoadGear" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.LoadGear.<tag name>" contains the configuration of the load gear.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| LoadGear. |  | TO_Struct_LoadGear |  |  |  |
|  | Numerator | UDINT | 1 to 4294967295 | RES | Load gear numerator |
| Denominator | UDINT | 1 to 4294967295 | RES | Load gear denominator |  |

#### "Units" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Units.<tag name>" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_Struct_Units / TO_Struct_ExternalEncoder_Units |  |  |  |  |
|  | VelocityUnit | UDINT | - | RON | Unit for velocity |  |
| 1082 | 1/s |  |  |  |  |  |
| 1083 | 1/min |  |  |  |  |  |
| 1528 | 1/h |  |  |  |  |  |
| TimeUnit | UDINT | - | RON | Unit for time |  |  |
| 1054 | s |  |  |  |  |  |
| TorqueUnit | UDINT | - | RON | Unit for torque |  |  |
| 1126 | Nm |  |  |  |  |  |
| 1128 | kNm |  |  |  |  |  |
| 1529 | lbf in (pound-force-inch) |  |  |  |  |  |
| 1530 | lbf ft |  |  |  |  |  |
| 1531 | ozf in (ounce-force-inch) |  |  |  |  |  |
| 1532 | ozf ft |  |  |  |  |  |
| 1533 | pdl in (poundal-inch) |  |  |  |  |  |
| 1534 | pdl ft |  |  |  |  |  |
| ForceUnit | UDINT | - | RON | Unit for force |  |  |
| 1120 | N |  |  |  |  |  |
| 1122 | kN |  |  |  |  |  |
| 1094 | lbf (pound-force) |  |  |  |  |  |
| 1093 | ozf (ounce-force) |  |  |  |  |  |
| 1535 | pdl (poundals) |  |  |  |  |  |
| MassUnit | UDINT | - | RON | Unit for mass |  |  |
| 1088 | kg |  |  |  |  |  |
| 1089 | g |  |  |  |  |  |
| 1090 | mg |  |  |  |  |  |
| 1092 | t |  |  |  |  |  |
| 1540 | lb |  |  |  |  |  |
| IneritaUnit | UDINT | - | RON | Unit for moment of inertia |  |  |
| 1118 | kg·m² |  |  |  |  |  |
| 1541 | lb·ft² |  |  |  |  |  |

#### "DynamicLimits" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicLimits.<tag name>" contains the configuration of the dynamic limits. During Motion Control, no dynamic values greater than the dynamic limits are permitted. If you specify greater values in a Motion Control instruction, then motion is performed using the dynamic limits, and a warning is indicated (alarm 501 to 503 - Dynamic values are limited).

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicLimits. |  | TO_Struct_DynamicLimits |  |  |  |
|  | MaxVelocity | LREAL | 0.0 to 1.0E12 | RES | Maximum permissible velocity of the axis |
| Velocity | LREAL | 0.0 to 1.0E12 | DIR | Current maximum velocity of the axis  The minimum from "MaxVelocity" and "Velocity" is effective for motion control. |  |
| MaxAcceleration | LREAL | 0.0 to 2.77777777777778E8 | DIR | Maximum permissible acceleration of the axis |  |
| MaxDeceleration | LREAL | 0.0 to 2.77777777777778E8 | DIR | Maximum permissible deceleration of the axis |  |
| MaxJerk | LREAL | 0.0 to 4629629.629 | DIR | Maximum permissible jerk on the axis |  |

#### "DynamicDefaults" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicDefaults.<tag name>" contains the configuration of the dynamic defaults. These settings will be used when you specify a dynamic value less than 0.0 in a Motion Control instruction (exceptions: "MC_MoveJog.Velocity", "MC_MoveVelocity.Velocity"). Changes to the default dynamic values will be applied at the next positive edge at the "Execute" parameter of a Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicDefaults. |  | TO_Struct_DynamicDefaults |  |  |  |
|  | Velocity | LREAL | 0.0 to 1.0E12 | CAL | Default velocity |
| Acceleration | LREAL | 0.0 to 2.77777777777778E8 | CAL | Default acceleration |  |
| Deceleration | LREAL | 0.0 to 2.77777777777778E8 | CAL | Default deceleration |  |
| Jerk | LREAL | 0.0 to 4629629.629 | CAL | Default jerk |  |
| EmergencyDeceleration | LREAL | 0.0 to 2.77777777777778E8 | DIR | Emergency stop deceleration |  |

#### "Override" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Override.<tag name>" contains the configuration of override parameters. The override parameters are used to apply a correction percentage to default values. An override change takes effect immediately, and is performed with the dynamic settings in effect in the Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Override. |  | TO_Struct_Override |  |  |  |
|  | Velocity | LREAL | 0.0 to 200.0% | DIR | Velocity or speed override  Percentage correction of the velocity/speed |

#### "StatusDrive" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusDrive.<tag name>" indicates the status of the drive.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusDrive. |  | TO_Struct_StatusDrive |  |  |  |  |
|  | InOperation | BOOL | - | RON | Operation status of the drive |  |
| FALSE | Drive not ready. Setpoints will not be executed. |  |  |  |  |  |
| TRUE | Drive ready. Setpoints can be executed. |  |  |  |  |  |
| CommunicationOK | BOOL | - | RON | Cyclic BUS communication between controller and drive |  |  |
| FALSE | Cyclic communication not established.  Fault ZSW1.X3 (FaultPresent) is present.  Possible causes:  - The CPU is in STOP. - The drive has failed. - The "ControlRequested" bit in the status word of the drive has the value "FALSE". - The drive signals an error using the status word. - For isochronous configuration, the dynamic sign of life in the telegram has failed or is not supplied by the drive. |  |  |  |  |  |
| TRUE | Cyclic communication OK and no fault effective |  |  |  |  |  |
| Error | BOOL | - | RON | FALSE | No drive error |  |
| TRUE | Drive error |  |  |  |  |  |
| AdaptionState | DINT | 0 to 4 | RON | Status of automatic data transfer of drive parameters |  |  |
| 0 | "NOT_ADAPTED"  Data not transferred |  |  |  |  |  |
| 1 | "IN_ADAPTION"  Data transfer in progress |  |  |  |  |  |
| 2 | "ADAPTED"  Data transfer complete |  |  |  |  |  |
| 3 | "NOT_APPLICABLE"  Data transfer not selected, not possible |  |  |  |  |  |
| 4 | "ADAPTION_ERROR"  Error during data transfer |  |  |  |  |  |

#### "StatusTorqueData" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusTorqueData.<tag name>" indicates the status of the torque.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusTorqueData. |  | TO_Struct_StatusTorqueData |  |  |  |  |
|  | Command­Additive­Torque­Active | DINT | - | RON | Additive torque setpoint function |  |
| 0 | Disabled |  |  |  |  |  |
| 1 | Enabled |  |  |  |  |  |
| Command­Torque­Range­Active | DINT | - | RON | Torque range above high and low limit of the torque function |  |  |
| 0 | Disabled |  |  |  |  |  |
| 1 | Enabled |  |  |  |  |  |
| ActualTorque | LREAL | -1.0E12 to 1.0E12 | RON | Actual torque of the axis in the technological unit of the technology object for torque |  |  |

#### "StatusMotionIn" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusMotionIn.<tag name>" indicates the motion status.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusMotionIn. |  | TO_Struct_StatusMotionIn |  |  |  |  |
|  | FunctionState | DINT | 0, 1 | RON | 0 | No "MotionIn" function active |
| 1 | "MotionInVelocity" function active |  |  |  |  |  |

#### "StatusInterpreterMotion" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusInterpreterMotion.<tag name>" contains status information on motion jobs controlled by a technology object Interpreter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusInterpreterMotion. |  |  | TO_Struct_StatusInterpreterMotion |  |  |  |
|  | Interpreter |  | DB_ANY | 0 to 65535 |  | Controlling Interpreter technology object |
| StatusWord. |  | DWORD | - | RON | Status information |  |
|  | Bit 0 | - | - | - | "ControlledByInterpreter"  An MCL job is processed or active or the bit is set via the MCL instruction "[setControlledByInterpreter()](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#setcontrolledbyinterpreter-set-controlledbyinterpreter-bit-for-a-technology-object-s7-1500t)". |  |
| Bit 1 | - | - | - | "MotionByInterpreter"  An MCL motion job is in effect. |  |  |
| Bit 2 to Bit 31 | - | - | - | Reserved |  |  |

#### "StatusWord" tag (speed axis) (S7-1500, S7-1500T)

The "<TO>.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 0 "Enable") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Enable"  Enable status  The technology object has been enabled. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "ControlPanelActive"  The axis control panel is active. |  |
| Bit 5 | - | - | - | Reserved |  |
| Bit 6 | - | - | - | "Done"  No motion job is in progress and the axis control panel is deactivated. |  |
| Bit 7 | - | - | - | Reserved |  |
| Bit 8 | - | - | - | Reserved |  |
| Bit 9 | - | - | - | "JogCommand"  An "MC_MoveJog" job is running. |  |
| Bit 10 | - | - | - | "VelocityCommand"  An "MC_MoveVelocity" job is running. |  |
| Bit 11 | - | - | - | Reserved |  |
| Bit 12 | - | - | - | "ConstantVelocity"  The velocity setpoint is reached. A constant velocity setpoint is output. |  |
| Bit 13 | - | - | - | "Accelerating"  An acceleration operation is active. |  |
| Bit 14 | - | - | - | "Decelerating"  A deceleration operation is active. |  |
| Bit 15... Bit 24 | - | - | - | Reserved |  |
| Bit 25 | - | - | - | "AxisSimulation"  The simulation is active. |  |
| Bit 26 | - | - | - | "TorqueLimitingCommand"  An "MC_TorqueLimiting" job is running. |  |
| Bit 27 | - | - | - | "InLimitation"  The drive operates at least at the threshold value (default 90%) of the torque limit. |  |
| Bit 28... Bit 31 | - | - | - | Reserved |  |
| <sup>1</sup> The bit is correctly displayed only when using SIEMENS telegram 10x. When using Mc_TorqueRange without SIEMENS telegram 10x, compare M_ACT with M_LIMIT_POS or M_LIMIT_NEG of telegram 750. InLimit = M_ACT * 0.9 > M_LIMIT_POS OR M_ACT * 0.9 < M_LIMIT_NEG. Evaluate the variable InLimit instead of StatusWord.%X27. |  |  |  |  |  |

#### "StatusWord2" tag (speed axis) (S7-1500, S7-1500T)

The "<TO>.StatusWord2" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 0 "StopCommand") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord2 |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | BOOL | - | RON | "StopCommand"  An "MC_Stop" job is running. The technology object is disabled. |
| Bit 1 to Bit 31 | BOOL | - | RON | Reserved |  |

#### "ErrorWord" tag (speed axis) (S7-1500, S7-1500T)

The "<TO>.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  System error |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | "DriveFault"  Error in drive |  |
| Bit 5 | - | - | - | Reserved |  |
| Bit 6 | - | - | - | "DynamicError"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 | - | - | - | "CommunicationFault"  Communication error  Missing or faulty communication. |  |
| Bit 8... Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralError"  Error accessing a logical address |  |
| Bit 14 | - | - | - | Reserved |  |
| Bit 15 | - | - | - | "AdaptionError"  Error during data transfer |  |
| Bit 16 ...  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.ErrorDetail.<tag name>" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0 to 5 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 1 | Stop with current dynamic values |  |  |  |  |  |
| 2 | Stop with maximum dynamic values |  |  |  |  |  |
| 3 | Stop with emergency stop ramp |  |  |  |  |  |
| 4 | Remove enable |  |  |  |  |  |
| 5 | Track setpoints |  |  |  |  |  |

#### "WarningWord" tag (speed axis) (S7-1500, S7-1500T)

The "<TO>.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 13 "PeripheralWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | "DriveWarning"  Warning of the drive  When a warning message is pending at the drive that does not result in a TO alarm, this bit is not set. Evaluate the drive warnings directly using the status word of the drive. |  |
| Bit 5 | - | - | - | Reserved |  |
| Bit 6 | - | - | - | "DynamicWarning"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 | - | - | - | "CommunicationWarning"  Communication error  Missing or faulty communication. |  |
| Bit 8... Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14 | - | - | - | Reserved |  |
| Bit 15 | - | - | - | "AdaptionWarning"  Error in automatic data transfer |  |
| Bit 16... Bit 31 | - | - | - | Reserved |  |

#### "ControlPanel" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.ControlPanel.<tag name>" contains no relevant data for you. This tag structure is internally used.

---

**See also**

[Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t)

#### "InternalToTrace" tag (speed axis) (S7-1500, S7-1500T)

The tag structure "<TO>.InternalToTrace.<tag name>" contains no relevant data for you. This tag structure is internally used.

---

**See also**

[Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t)

### Tags of the positioning axis technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t-1)
- [Actual values and setpoints (positioning axis) (S7-1500, S7-1500T)](#actual-values-and-setpoints-positioning-axis-s7-1500-s7-1500t)
- ["Simulation" tag (positioning axis) (S7-1500, S7-1500T)](#simulation-tag-positioning-axis-s7-1500-s7-1500t)
- ["VirtualAxis" tag (positioning axis) (S7-1500, S7-1500T)](#virtualaxis-tag-positioning-axis-s7-1500-s7-1500t)
- ["Actor" tag (positioning axis) (S7-1500, S7-1500T)](#actor-tag-positioning-axis-s7-1500-s7-1500t)
- ["TorqueLimiting" tag (positioning axis) (S7-1500, S7-1500T)](#torquelimiting-tag-positioning-axis-s7-1500-s7-1500t)
- ["Clamping" tag (positioning axis) (S7-1500, S7-1500T)](#clamping-tag-positioning-axis-s7-1500-s7-1500t)
- [Sensor[1..4] tags (positioning axis) (S7-1500, S7-1500T)](#sensor14-tags-positioning-axis-s7-1500-s7-1500t)
- ["CrossPlcSynchronousOperation" tag (positioning axis) (S7-1500, S7-1500T)](#crossplcsynchronousoperation-tag-positioning-axis-s7-1500-s7-1500t)
- ["Extrapolation" tag (positioning axis) (S7-1500, S7-1500T)](#extrapolation-tag-positioning-axis-s7-1500-s7-1500t)
- ["LoadGear" tag (positioning axis) (S7-1500, S7-1500T)](#loadgear-tag-positioning-axis-s7-1500-s7-1500t)
- ["Properties" tag (positioning axis) (S7-1500, S7-1500T)](#properties-tag-positioning-axis-s7-1500-s7-1500t)
- ["Units" tag (positioning axis) (S7-1500, S7-1500T)](#units-tag-positioning-axis-s7-1500-s7-1500t)
- ["Mechanics" tag (positioning axis) (S7-1500, S7-1500T)](#mechanics-tag-positioning-axis-s7-1500-s7-1500t)
- ["Modulo" tag (positioning axis) (S7-1500, S7-1500T)](#modulo-tag-positioning-axis-s7-1500-s7-1500t)
- ["DynamicLimits" tag (positioning axis) (S7-1500, S7-1500T)](#dynamiclimits-tag-positioning-axis-s7-1500-s7-1500t)
- ["DynamicDefaults" tag (positioning axis) (S7-1500, S7-1500T)](#dynamicdefaults-tag-positioning-axis-s7-1500-s7-1500t)
- ["PositionLimits_SW" tag (positioning axis) (S7-1500, S7-1500T)](#positionlimits_sw-tag-positioning-axis-s7-1500-s7-1500t)
- ["PositionLimits_HW" tag (positioning axis) (S7-1500, S7-1500T)](#positionlimits_hw-tag-positioning-axis-s7-1500-s7-1500t)
- ["Homing" tag (positioning axis) (S7-1500, S7-1500T)](#homing-tag-positioning-axis-s7-1500-s7-1500t)
- ["Override" tag (positioning axis) (S7-1500, S7-1500T)](#override-tag-positioning-axis-s7-1500-s7-1500t)
- ["PositionControl" tag (positioning axis) (S7-1500, S7-1500T)](#positioncontrol-tag-positioning-axis-s7-1500-s7-1500t)
- ["TorquePreControl" tag (positioning axis) (S7-1500, S7-1500T)](#torqueprecontrol-tag-positioning-axis-s7-1500-s7-1500t)
- ["SetpointFilter" tag (positioning axis) (S7-1500, S7-1500T)](#setpointfilter-tag-positioning-axis-s7-1500-s7-1500t)
- ["DynamicAxisModel" tag (positioning axis) (S7-1500, S7-1500T)](#dynamicaxismodel-tag-positioning-axis-s7-1500-s7-1500t)
- ["FollowingError" tag (positioning axis) (S7-1500, S7-1500T)](#followingerror-tag-positioning-axis-s7-1500-s7-1500t)
- ["PositioningMonitoring" tag (positioning axis) (S7-1500, S7-1500T)](#positioningmonitoring-tag-positioning-axis-s7-1500-s7-1500t)
- ["StandstillSignal" tag (positioning axis) (S7-1500, S7-1500T)](#standstillsignal-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusPositioning" tag (positioning axis) (S7-1500, S7-1500T)](#statuspositioning-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusDrive" tag (positioning axis) (S7-1500, S7-1500T)](#statusdrive-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusServo" tag (positioning axis) (S7-1500, S7-1500T)](#statusservo-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusProvidedLeadingValue" tag (positioning axis) (S7-1500, S7-1500T)](#statusprovidedleadingvalue-tag-positioning-axis-s7-1500-s7-1500t)
- [StatusSensor[1..4] Tags (positioning axis) (S7-1500, S7-1500T)](#statussensor14-tags-positioning-axis-s7-1500-s7-1500t)
- ["StatusExtrapolation" tag (positioning axis) (S7-1500, S7-1500T)](#statusextrapolation-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusKinematicsMotion" tag (positioning axis) (S7-1500, S7-1500T)](#statuskinematicsmotion-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusTorqueData" tag (positioning axis) (S7-1500, S7-1500T)](#statustorquedata-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusMotionIn" tag (positioning axis) (S7-1500, S7-1500T)](#statusmotionin-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusInterpreterMotion" tag (positioning axis) (S7-1500, S7-1500T)](#statusinterpretermotion-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusWord" tag (positioning axis) (S7-1500, S7-1500T)](#statusword-tag-positioning-axis-s7-1500-s7-1500t)
- ["StatusWord2" tag (positioning axis) (S7-1500, S7-1500T)](#statusword2-tag-positioning-axis-s7-1500-s7-1500t)
- ["ErrorWord" tag (positioning axis) (S7-1500, S7-1500T)](#errorword-tag-positioning-axis-s7-1500-s7-1500t)
- ["ErrorDetail" tag (positioning axis) (S7-1500, S7-1500T)](#errordetail-tag-positioning-axis-s7-1500-s7-1500t)
- ["WarningWord" tag (positioning axis) (S7-1500, S7-1500T)](#warningword-tag-positioning-axis-s7-1500-s7-1500t)
- ["ControlPanel" tag (positioning axis) (S7-1500, S7-1500T)](#controlpanel-tag-positioning-axis-s7-1500-s7-1500t)
- ["InternalToTrace" tag (positioning axis) (S7-1500, S7-1500T)](#internaltotrace-tag-positioning-axis-s7-1500-s7-1500t)

#### Legend (S7-1500, S7-1500T)

|  |  |  |
| --- | --- | --- |
| Tag | Name of the tag |  |
| Data type | Data type of the tag |  |
| Values | Value range of the tag - minimum value to maximum value  (L - linear specification R - rotary specification)  If no specific value is shown, the value range limits of the relevant data type apply or the information under "Description". |  |
| W | Effectiveness of changes in the technology data block |  |
| DIR | Direct:  Values are changed via direct assignment and take effect at the start of the next MC_Servo. |  |
| CAL | At call of Motion Control instruction:  Values are changed directly and take effect at the start of the next MC_Servo after the call of the corresponding Motion Control instruction in the user program. |  |
| RES | Restart:  Changes to the start value in the load memory are made using the extended instruction "WRIT_DBL" (write to DB in load memory). Changes will not take effect until after restart of the technology object. |  |
| RON | Read only:  The tag cannot and must not be changed during runtime of the user program. |  |
| Description | Description of the tag |  |

Access to the tags is with "<TO>.<tag name>". The placeholder <TO> represents the name of the technology object.

#### Actual values and setpoints (positioning axis) (S7-1500, S7-1500T)

The following tags indicate the setpoint and actual values of the technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| Position | LREAL | - | RON | Position setpoint |  |
| Velocity | LREAL | - | RON | Velocity setpoint/speed setpoint |  |
| ActualPosition | LREAL | - | RON | Actual position |  |
| ActualVelocity | LREAL | - | RON | Actual velocity |  |
| ActualSpeed | LREAL | - | RON | For PROFIdrive drives | Actual speed of the motor |
| For drives with analog setpoint interface | 0.0 |  |  |  |  |
| For drives with linear motor | 0.0 |  |  |  |  |
| Acceleration | LREAL | - | RON | Setpoint acceleration |  |
| ActualAcceleration | LREAL | - | RON | Actual acceleration |  |
| OperativeSensor | UDINT | 1 to 4 | RON | Operative encoder |  |
| ModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles of the setpoint |  |
| ActualModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles of the actual value |  |
| VelocitySetpoint | LREAL | -1.0E12 to 1.0E12 | RON | Output velocity setpoint/speed setpoint |  |

#### "Simulation" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Simulation.<tag name>" contains the configuration of the simulation mode. In simulation mode, you can simulate axes without a real drive in the CPU.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Simulation. |  | TO_Struct_AxisSimulation |  |  |  |  |
|  | Mode | UDINT | 0, 1 | RES<sup>1)</sup> | Simulation mode |  |
| 0 | No simulation, normal operation |  |  |  |  |  |
| 1 | Simulation mode |  |  |  |  |  |
| <sup>1)</sup> Technology version V2.0: RON |  |  |  |  |  |  |

#### "VirtualAxis" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.VirtualAxis.<tag name>" contains the configuration of the virtual operation of the axis. A virtual axis is often used as a virtual leading axis in order to generate the setpoints for several real following axes in synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| VirtualAxis. |  | TO_Struct_VirtualAxis |  |  |  |  |
|  | Mode | UDINT | 0, 1 | RON | Virtual axis |  |
| 0 | No virtual axis |  |  |  |  |  |
| 1 | Technology version ≥ V7.0:  The behavior of a virtual axis is identical to the behavior of an axis in simulation. The actual values are generated via the control loop and a simplified drive model.  Technology version ≥ V8.0:  In technology version V8.0, the behavior of the virtual axis has been changed. The behavior of a virtual axis is no longer identical to the behavior of an axis in simulation.  The position and velocity setpoints are directly adopted as actual values with an application cycle delay. The feedback loop and the drive model are not simulated. The dynamic filter is effective.  To maintain compatibility with virtual axes of technology versions ≤ V7.0 for an axis:  1. Interconnect the axis in simulation (<TO>.Simulation.Mode" = 1). 2. Disable the virtual axis (<TO>.VirtualAxisMode = 0) |  |  |  |  |  |

#### "Actor" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Actor.<tag name>" contains the controller-side configuration of the drive.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Actor. |  |  | TO_Struct_Actor |  |  |  |  |
|  | Type |  | DINT | 0, 1 | RON | Drive connection |  |
| 0 | Analog output |  |  |  |  |  |  |
| 1 | PROFIdrive telegram |  |  |  |  |  |  |
| InverseDirection |  | BOOL | - | RES | Inversion of the setpoint |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| DataAdaption |  | DINT | 0, 1 | RES | Automatic transfer of the drive values reference speed, maximum speed and reference torque |  |  |
| 0 | No automatic transfer, manual configuration of values |  |  |  |  |  |  |
| 1 | Automatic transfer of values configured in the drive to the configuration of the technology object |  |  |  |  |  |  |
| Efficiency |  | LREAL | 0.0 to 1.0 | RES | Efficiency of mechanics (gear and leadscrew) |  |  |
| MotorType |  | DINT | 0.1 | DL | Motor type |  |  |
| 0 | Round-frame motor (standard motor) |  |  |  |  |  |  |
| 1 | Linear motor |  |  |  |  |  |  |
| LoadInertia |  | LREAL | 0.0 to 1.0E12 | DIR | Moment of inertia or weight of the load |  |  |
| RemoveEnableReaction |  | WORD | 16#1 to 16#7 | RES | Stop reaction on "Remove enable" |  |  |
| 16#1 | OFF1 – Ramp stop - Braking with ramp-function generator |  |  |  |  |  |  |
| 16#3 | OFF2 – Coast stop - Coast down |  |  |  |  |  |  |
| 16#5 | OFF3 – Quick stop - Quick stop |  |  |  |  |  |  |
| 16#7 | OFF3 – Quick stop (compatible configuration for technology versions up to V7) |  |  |  |  |  |  |
| 16#2  16#4  16#6 | Invalid |  |  |  |  |  |  |
| Interface. |  | TO_Struct_ActorInterface |  |  |  |  |  |
|  | AddressIn | VREF | 0 to 65535 | RON | Input address for the PROFIdrive telegram |  |  |
| AddressOut | VREF | 0 to 65535 | RON | Output address for the PROFIdrive telegram or the analog setpoint |  |  |  |
| EnableDriveOutput | BOOL | - | RES | "Enable output" for analog drives |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| EnableDrive­Output­Address | VREF | 0 to 65535 | RON | Address for the "Enable output" for analog setpoint |  |  |  |
| DriveReadyInput | BOOL | - | RES | "Ready input" for analog drives   The analog drive signals its readiness to receive speed setpoints. |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| DriveReadyInput­Address | VREF | 0 to 65535 | RON | Address for the "Enable input" for analog setpoint |  |  |  |
| EnableTorqueData | BOOL | - | RES | Torque data |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| TorqueDataAddressIn | VREF | 0 to 65535 | RON | Input address of the supplemental telegram |  |  |  |
| TorqueDataAddress­Out | VREF | 0 to 65535 | RON | Output address of additional telegram |  |  |  |
| DriveParameter. |  | TO_Struct_ActorDriveParameter |  |  | Valid when "<TO>.Actor.MotorType" = 0 |  |  |
|  | ReferenceSpeed | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the speed setpoint (N-set) of the drive  The speed setpoint is transferred in the PROFIdrive telegram as a normalized value from -200% to 200% of the "ReferenceSpeed".  For setpoint specification via an analog output, the analog output can be operated in the range from -117% to 117%, provided the drive permits this. |  |  |
| MaxSpeed | LREAL | 0.0 to 1.0E12 | RES | Maximum value for the speed setpoint of the drive (N-set)  (PROFIdrive: MaxSpeed ≤ 2 × ReferenceSpeed  Analog setpoint: MaxSpeed ≤ 1.17 × ReferenceSpeed) |  |  |  |
| ReferenceTorque | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the drive torque |  |  |  |
| MotorInertia | LREAL | 0.0 to 1.0E12 | DIR | Moment of inertia of the motor |  |  |  |
| LinearMotorDrive­Parameter. |  | TO_Struct_LinearMotorActorDriveParameter |  |  | Valid when "<TO>.Actor.MotorType" = 1 |  |  |
|  | ReferenceVelocity | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the velocity setpoint (N-set) of the drive  The speed setpoint is transferred in the PROFIdrive telegram as a normalized value from -200% to 200% of the "ReferenceVelocity".  For setpoint specification via an analog output, the analog output can be operated in the range from -117% to 117%, provided the drive permits this. |  |  |
| MaxVelocity | LREAL | 0.0 to 1.0E12 | RES | Maximum value for the velocity setpoint of the drive (N-set)  (PROFIdrive: MaxVelocity ≤ 2 × ReferenceVelocity  Analog setpoint: MaxVelocity ≤ 1.17 × ReferenceVelocity) |  |  |  |
| ReferenceForce | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the force of the drive |  |  |  |
| MotorMass | LREAL | 0.0 to 1.0E12 | DIR | Mass of linear motor |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "TorqueLimiting" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.TorqueLimiting.<tag name>" contains the configuration of the torque limit/force limit.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TorqueLimiting. |  |  | TO_Struct_TorqueLimiting |  |  |  |  |
|  | LimitBase |  | DINT | 0, 1 | RES | Torque limit/force limit |  |
| 0 | Motor side |  |  |  |  |  |  |
| 1 | Load side |  |  |  |  |  |  |
| Setting is not relevant for linear motors. |  |  |  |  |  |  |  |
| PositionBasedMonitorings |  | DINT | 0, 1 | RES | Positioning and following error monitoring |  |  |
| 0 | Monitoring deactivated |  |  |  |  |  |  |
| 1 | Monitoring activated |  |  |  |  |  |  |
| LimitDefaults. |  | TO_Struct_TorqueLimitingLimitDefaults |  |  |  |  |  |
|  | Torque | LREAL | 0.0 to 1.0E12 | CAL | Limiting torque |  |  |
| Force | LREAL | 0.0 to 1.0E12 | CAL | Limiting force |  |  |  |

#### "Clamping" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Clamping.<tag name>" contains the configuration of the fixed stop detection.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Clamping. |  | TO_Struct_Clamping |  |  |  |
|  | FollowingErrorDeviation | LREAL | 0.001 to 1.0E12 | DIR | Value of the following error starting from which the fixed stop is detected. |
| PositionTolerance | LREAL | 0.001 to 1.0E12 | DIR | Position tolerance for the clamping monitoring |  |

#### Sensor[1..4] tags (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Sensor[1..4].<tag name>" contains the controller-end configuration of the encoder and the configuration of active and passive homing.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sensor[1..4]. |  |  | ARRAY [1..4] OF TO_Struct_Sensor |  |  |  |  |
|  | Existent |  | BOOL | - | RON | Displaying created encoders |  |
| Type |  | DINT | 0 to 2 | RON | Encoder type |  |  |
| 0 | "INCREMENTAL"  Incremental |  |  |  |  |  |  |
| 1 | "ABSOLUTE"  Absolute |  |  |  |  |  |  |
| 2 | "CYCLIC_ABSOLUTE"  Cyclic absolute |  |  |  |  |  |  |
| InverseDirection |  | BOOL | - | RES | Inversion of the actual value |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| System |  | DINT | 0, 1 | RES | Encoder system |  |  |
| 0 | "LINEAR"  Linear encoder |  |  |  |  |  |  |
| 1 | "ROTATORY"  Rotary encoder |  |  |  |  |  |  |
| MountingMode |  | DINT | 0 to 2 | RES | Mounting type of encoder |  |  |
| 0 | On motor shaft |  |  |  |  |  |  |
| 1 | On load side |  |  |  |  |  |  |
| 2 | External measuring system |  |  |  |  |  |  |
| DataAdaption |  | DINT | 0, 1 | RES | Automatic transfer of the drive values reference speed, maximum speed and reference torque in the device |  |  |
| 0 | No automatic transfer, manual configuration of values |  |  |  |  |  |  |
| 1 | Automatic transfer of values configured in the drive to the configuration of the technology object |  |  |  |  |  |  |
| ActualVelocityMode |  | DINT | 0, 1 | RES | Type of calculation for actual speed value or actual velocity value |  |  |
| 0 | Actual value calculation from differentiation of the position change |  |  |  |  |  |  |
| 1 | Actual value calculation with NACT value from the PROFIdrive telegram |  |  |  |  |  |  |
| Interface. |  | TO_Struct_SensorInterface |  |  |  |  |  |
|  | AddressIn | VREF | 0 to 65535 | RON | Input address for the PROFIdrive telegram |  |  |
| AddressOut | VREF | 0 to 65535 | RON | Output address for the PROFIdrive telegram |  |  |  |
| Number | UDINT | 1 to 2 | RON | Number of the encoder in the telegram |  |  |  |
| Parameter. |  | TO_Struct_SensorParameter |  |  |  |  |  |
|  | Resolution | LREAL | 1.0E-12 to 1.0E12 | RES | Resolution of a linear encoder (offset between two encoder pulses) |  |  |
| StepsPerRevolution | UDINT | 1 to 8388608 | RES | Increments per rotary encoder revolution |  |  |  |
| FineResolutionXist1 | UDINT | 0 to 31 | RES | Number of bits for fine resolution "Gx_XIST1" (cyclic actual encoder value) |  |  |  |
| FineResolutionXist2 | UDINT | 0 to 31 | RES | Number of bits for fine resolution "Gx_XIST2" (absolute value of the encoder) |  |  |  |
| DeterminableRevolutions | UDINT | 0 to 8388608 | RES | Number of differentiable encoder revolutions for a multi-turn absolute encoder   (For a single-turn absolute encoder = 1; for an incremental encoder = 0) |  |  |  |
| DistancePerRevolution | LREAL | 0.0 to 1.0E12 | RES | For technology objects < V8.0: Load distance per revolution of an externally mounted encoder  For technology objects >= V8.0: Load travel per measuring wheel revolution of an externally mounted encoder |  |  |  |
| BehaviorGx_XIST1 | DINT | 0, 1 | RES | Evaluation of "Gx_XIST1" bits. |  |  |  |
| 0 | Based on the bits of the encoder resolution.  The incremental actual value "Gx_XIST1" is transmitted with less than 32 bits in the PROFIdrive telegram. For example: At 16 bits, the value ranges from 0 to 65,535. |  |  |  |  |  |  |
| 1 | 32-bit value of the encoder value  The "Gx_XIST1" incremental actual value is transferred with 32 bits of 0 to 4,294,967,295 in the PROFIdrive telegram. |  |  |  |  |  |  |
| ReferenceSpeed | LREAL | 0.0 to 1.0E12 | RES | Reference speed for NACT in PROFIdrive telegram with rotary encoder  Only relevant for "ActualVelocityMode" = 1 |  |  |  |
| ReferenceVelocity | LREAL | 0.0 to 1.0E12 | RES | Reference velocity for NACT in the PROFIdrive telegram with linear encoder  Only relevant for "ActualVelocityMode" = 1 |  |  |  |
| Backlash. |  | TO_Struct_Backlash |  |  |  |  |  |
|  | Enable | BOOL | - | DIR | Enable backlash compensation |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| If you enable/disable backlash compensation during runtime, then you have to home the axis again. |  |  |  |  |  |  |  |
| Size | LREAL | 0.0 to 1.0E12 | DIR | Size of backlashes |  |  |  |
| If you change the size of backlashes during runtime, you have to home the axis again. |  |  |  |  |  |  |  |
| Velocity | LREAL | 0.0 to 1.0E12 | DIR | Velocity for traversing of backlashes |  |  |  |
| 0.0 | Motor traverses backlashes within one servo cycle. |  |  |  |  |  |  |
| > 0.0 | Motor traverses backlash with the specified velocity. |  |  |  |  |  |  |
| DirectionAbsoluteHoming | DINT | 0, 1 | DIR | Direction of movement during or before absolute encoder adjustment |  |  |  |
| 0 | Positive |  |  |  |  |  |  |
| 1 | Negative |  |  |  |  |  |  |
| ActiveHoming. |  | TO_Struct_SensorActiveHoming |  |  |  |  |  |
|  | Mode | DINT | 0 to 2 | RES | Homing mode |  |  |
| 0 | Use zero mark via PROFIdrive telegram |  |  |  |  |  |  |
| 1 | Zero mark via PROFIdrive telegram and reference output cam |  |  |  |  |  |  |
| 2 | Use homing mark via digital input |  |  |  |  |  |  |
| SideInput | BOOL | - | CAL | Side of the digital input for active homing |  |  |  |
| FALSE | Negative side |  |  |  |  |  |  |
| TRUE | Positive side |  |  |  |  |  |  |
| Direction | DINT | 0, 1 | CAL | Homing direction/approach direction to homing mark |  |  |  |
| 0 | Positive homing direction |  |  |  |  |  |  |
| 1 | Negative homing direction |  |  |  |  |  |  |
| DigitalInputAddress | VREF | 0 to 65535 | RON | Address of digital input |  |  |  |
| HomePositionOffset | LREAL | -1.0E12 to 1.0E12 | CAL | Home position offset |  |  |  |
| SwitchLevel | BOOL | - | RES | Signal level that is present at the digital input when homing mark is approached |  |  |  |
| FALSE | Low level |  |  |  |  |  |  |
| TRUE | High level |  |  |  |  |  |  |
| PassiveHoming. |  | TO_Struct_SensorPassiveHoming |  |  |  |  |  |
|  | Mode | DINT | 0 to 2 | RES | Homing mode |  |  |
| 0 | Use zero mark via PROFIdrive telegram |  |  |  |  |  |  |
| 1 | Zero mark via PROFIdrive telegram and reference output cam |  |  |  |  |  |  |
| 2 | Use homing mark via digital input |  |  |  |  |  |  |
| SideInput | BOOL | - | CAL | Side of the digital input for passive homing |  |  |  |
| FALSE | Negative side |  |  |  |  |  |  |
| TRUE | Positive side |  |  |  |  |  |  |
| Direction | DINT | 0 to 2 | CAL | Homing direction/approach direction to homing mark |  |  |  |
| 0 | Positive homing direction |  |  |  |  |  |  |
| 1 | Negative homing direction |  |  |  |  |  |  |
| 2 | Current homing direction |  |  |  |  |  |  |
| DigitalInputAddress | VREF | 0 to 65535 | RON | Address of digital input |  |  |  |
| SwitchLevel | BOOL | - | RES | Signal level that is present at the digital input when homing mark is approached |  |  |  |
| FALSE | Low level |  |  |  |  |  |  |
| TRUE | High level |  |  |  |  |  |  |
| MeasuringGear. |  | TO_Struct_SensorMeasuringGear |  |  |  |  |  |
|  | Numerator | UDINT | 1 to 4294967295 | RES | Default value 1.  For “MountingMode” = Motor side (0):  Specifies the counter of the gear ratio for a measuring wheel for motor-mounted encoders. Number of motor revolutions.  For “MountingMode” = Load side (1):  Specifies the counter of the gear ratio for a measuring gearwheel for load-mounted encoders. Number of load revolutions.  For “MountingMode” = External (2):  Specifies the counter of the gear ratio for a measuring gearwheel for externally mounted encoders. Number of revolutions of the measuring wheel. |  |  |
| Denominator | UDINT | 1 to 4294967295 | RES | Specifies the denominator of the gear wheel for a measuring wheel. It depends on "MountingMode". Number of encoder revolutions. |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "CrossPlcSynchronousOperation" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.CrossPlcSynchronousOperation.<tag name>" contains the configuration of the cross-PLC synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CrossPlcSynchronousOperation. |  |  | TO_Struct_CrossPlcSynchronousOperation |  |  |  |  |
|  | Interface[1..8]. |  | ARRAY [1..8] of TO_Struct_CrossPlcLeadingValueInterface |  |  |  |  |
|  | EnableLeadingValueOutput | BOOL | - | RON | Provide cross-PLC leading value |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| AddressOut | VREF | - | RON | Output address for the leading value telegram |  |  |  |
| LocalLeadingValueDelayTime |  | LREAL | 0.0 to 1.0E9 | RES | Delay time of leading value output on the local following axes |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "Extrapolation" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Extrapolation.<tag name>" contains the configuration of the actual value extrapolation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Extrapolation. |  |  | TO_Struct_Extrapolation |  |  |  |  |
|  | LeadingAxisDependentTime |  | LREAL | - | RON | Extrapolation time component (caused by leading axis)  Results from the following times:  - Time of actual value acquisition for the leading axis - Interpolator cycle clock - Time of position filter of actual value extrapolation (T1 + T2) |  |
| FollowingAxisDependentTime |  | LREAL | 0.0 to 1.0E12 | DIR | Extrapolation time component (caused by following axis)  Results from the following times:  - For a following axis with set velocity precontrol:   - Communication cycle   - Interpolator cycle clock   - Speed control loop substitute time for the following axis   - Output delay time of the setpoint at the following axis - For a following axis without velocity precontrol:   - Communication cycle   - Interpolator cycle clock   - Position control loop equivalent time (1/Kv from "<TO>.PositionControl.Kv")   - Output delay time of the setpoint at the following axis |  |  |
| Settings. |  | TO_Struct_ExtrapolationSettings |  |  |  |  |  |
|  | SystemDefinedExtrapolation | DINT | 0, 1 | RES | Leading axis dependent time |  |  |
| 0 | Not effective |  |  |  |  |  |  |
| 1 | Effective |  |  |  |  |  |  |
| ExtrapolatedVelocityMode | DINT | 0, 1 | RES | Effective velocity value for the synchronization function |  |  |  |
| 0 | "FilteredVelocity"  Leading value velocity from filtered actual velocity |  |  |  |  |  |  |
| 1 | "VelocityByDifferentiation"  The leading value velocity results from the differentiation of the extrapolated leading value position |  |  |  |  |  |  |
| PositionFilter. |  | TO_Struct_ExtrapolationPositionFilter |  |  |  |  |  |
|  | T1 | LREAL | 0.0 to 1.0E12 | DIR | Position filter time constant T1 |  |  |
| T2 | LREAL | 0.0 to 1.0E12 | DIR | Position filter time constant T2 |  |  |  |
| VelocityFilter. |  | TO_Struct_ExtrapolationVelocityFilter |  |  |  |  |  |
|  | T1 | LREAL | 0.0 to 1.0E12 | DIR | Velocity filter time constant T1 |  |  |
| T2 | LREAL | 0.0 to 1.0E12 | DIR | Velocity filter time constant T2 |  |  |  |
| VelocityTolerance. |  | TO_Struct_ExtrapolationVelocityTolerance |  |  |  |  |  |
|  | Range | LREAL | 0.0 to 1.0E12 | DIR | Tolerance band width for velocity |  |  |
| Hysteresis. |  | TO_Struct_ExtrapolationHysteresis |  |  |  |  |  |
|  | Value | LREAL | 0.0 to 1.0E12 | DIR | Hysteresis of the extrapolated actual position value |  |  |

#### "LoadGear" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.LoadGear.<tag name>" contains the configuration of the load gear.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| LoadGear. |  | TO_Struct_LoadGear |  |  |  |
|  | Numerator | UDINT | 1 to 4294967295 | RES | Load gear numerator |
| Denominator | UDINT | 1 to 4294967295 | RES | Load gear denominator |  |

#### "Properties" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Properties.<tag name>" contains the configuration of the type of axis or motion.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Properties. |  | TO_Struct_Properties |  |  |  |  |
|  | MotionType | DINT | 0, 1 | RON | Indication of axis type or motion type |  |
| 0 | Linear axis or motion |  |  |  |  |  |
| 1 | Rotary axis or motion |  |  |  |  |  |

#### "Units" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Units.<tag name>" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_Struct_Units / TO_Struct_ExternalEncoder_Units |  |  |  |  |
|  | LengthUnit | UDINT | - | RON | Unit for position |  |
| 1010 | m |  |  |  |  |  |
| 1013 | mm |  |  |  |  |  |
| 1536 | mm<sup>1)</sup> |  |  |  |  |  |
| 1011 | km |  |  |  |  |  |
| 1014 | µm |  |  |  |  |  |
| 1015 | nm |  |  |  |  |  |
| 1019 | in |  |  |  |  |  |
| 1018 | ft |  |  |  |  |  |
| 1021 | mi |  |  |  |  |  |
| 1004 | rad |  |  |  |  |  |
| 1005 | ° |  |  |  |  |  |
| 1537 | °<sup>1)</sup> |  |  |  |  |  |
| VelocityUnit | UDINT | - | RON | Unit for velocity |  |  |
| 1521 | °/s |  |  |  |  |  |
| 1539 | °/s<sup>1)</sup> |  |  |  |  |  |
| 1522 | °/min |  |  |  |  |  |
| 1086 | rad/s |  |  |  |  |  |
| 1523 | rad/min |  |  |  |  |  |
| 1062 | mm/s |  |  |  |  |  |
| 1538 | mm/s<sup>1)</sup> |  |  |  |  |  |
| 1061 | m/s |  |  |  |  |  |
| 1524 | mm/min |  |  |  |  |  |
| 1525 | m/min |  |  |  |  |  |
| 1526 | mm/h |  |  |  |  |  |
| 1063 | m/h |  |  |  |  |  |
| 1527 | km/min |  |  |  |  |  |
| 1064 | km/h |  |  |  |  |  |
| 1066 | in/s |  |  |  |  |  |
| 1069 | in/min |  |  |  |  |  |
| 1067 | ft/s |  |  |  |  |  |
| 1070 | ft/min |  |  |  |  |  |
| 1075 | mi/h |  |  |  |  |  |
| TimeUnit | UDINT | - | RON | Unit for time |  |  |
| 1054 | s |  |  |  |  |  |
| TorqueUnit | UDINT | - | RON | Unit for torque |  |  |
| 1126 | Nm |  |  |  |  |  |
| 1128 | kNm |  |  |  |  |  |
| 1529 | lbf in (pound-force-inch) |  |  |  |  |  |
| 1530 | lbf ft |  |  |  |  |  |
| 1531 | ozf in (ounce-force-inch) |  |  |  |  |  |
| 1532 | ozf ft |  |  |  |  |  |
| 1533 | pdl in (poundal-inch) |  |  |  |  |  |
| 1534 | pdl ft |  |  |  |  |  |
| ForceUnit | UDINT | - | RON | Unit for force |  |  |
| 1120 | N |  |  |  |  |  |
| 1122 | kN |  |  |  |  |  |
| 1094 | lbf (pound-force) |  |  |  |  |  |
| 1093 | ozf (ounce-force) |  |  |  |  |  |
| 1535 | pdl (poundals) |  |  |  |  |  |
| MassUnit | UDINT | - | RON | Unit for mass |  |  |
| 1088 | kg |  |  |  |  |  |
| 1089 | g |  |  |  |  |  |
| 1090 | mg |  |  |  |  |  |
| 1092 | t |  |  |  |  |  |
| 1540 | lb |  |  |  |  |  |
| IneritaUnit | UDINT | - | RON | Unit for moment of inertia |  |  |
| 1118 | kg·m² |  |  |  |  |  |
| 1541 | lb·ft² |  |  |  |  |  |
| <sup>1)</sup> Position values with higher resolution or six decimal places |  |  |  |  |  |  |

---

**See also**

[Units of measure (S7-1500, S7-1500T)](#units-of-measure-s7-1500-s7-1500t)

#### "Mechanics" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Mechanics.<tag name>" contains the configuration of the mechanics.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| Mechanics. |  | TO_Struct_Mechanics |  |  |  |
|  | LeadScrew | LREAL | 1.0E-12 to 1.0E12 | RES | Leadscrew pitch |

#### "Modulo" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Modulo.<tag name>" contains the configuration of the modulo function.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Modulo. |  | TO_Struct_Modulo |  |  |  |  |
|  | Enable | BOOL | - | RES | FALSE | Modulo conversion disabled |
| TRUE | Modulo conversion enabled |  |  |  |  |  |
| When modulo conversion is enabled, a check is made for modulo length > 0.0 |  |  |  |  |  |  |
| Length | LREAL | 0.001 to 1.0E12 | RES | Modulo length |  |  |
| StartValue | LREAL | -1.0E12 to 1.0E12 | RES | Modulo start value |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "DynamicLimits" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicLimits.<tag name>" contains the configuration of the dynamic limits. During Motion Control, no dynamic values greater than the dynamic limits are permitted. If you specify greater values in a Motion Control instruction, then motion is performed using the dynamic limits, and a warning is indicated (alarm 501 to 503 - Dynamic values are limited).

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicLimits. |  | TO_Struct_DynamicLimits |  |  |  |
|  | MaxVelocity | LREAL | 0.0 to 1.0E12 | RES | Maximum permissible velocity of the axis |
| Velocity | LREAL | 0.0 to 1.0E12 | DIR | Current maximum velocity of the axis  The minimum from "MaxVelocity" and "Velocity" is effective for motion control. |  |
| MaxAcceleration | LREAL | 0.0 to 1.0E12 | DIR | Maximum permissible acceleration of the axis |  |
| MaxDeceleration | LREAL | 0.0 to 1.0E12 | DIR | Maximum permissible deceleration of the axis |  |
| MaxJerk | LREAL | 0.0 to 1.0E12 | DIR | Maximum permissible jerk on the axis |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "DynamicDefaults" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicDefaults.<tag name>" contains the configuration of the dynamic defaults. These settings will be used when you specify a dynamic value less than 0.0 in a Motion Control instruction (exceptions: "MC_MoveJog.Velocity", "MC_MoveVelocity.Velocity"). Changes to the default dynamic values will be applied at the next positive edge at the "Execute" parameter of a Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicDefaults. |  | TO_Struct_DynamicDefaults |  |  |  |
|  | Velocity | LREAL | 0.0 to 1.0E12 | CAL | Default velocity |
| Acceleration | LREAL | 0.0 to 1.0E12 | CAL | Default acceleration |  |
| Deceleration | LREAL | 0.0 to 1.0E12 | CAL | Default deceleration |  |
| Jerk | LREAL | 0.0 to 1.0E12 | CAL | Default jerk |  |
| EmergencyDeceleration | LREAL | 0.0 to 1.0E12 | DIR | Emergency stop deceleration |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "PositionLimits_SW" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositionLimits_SW.<tag name>" contains the configuration of position monitoring with software limit switches. Software limit switches are used to limit the operating range of a positioning axis.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| PositionLimits_SW. |  | TO_Struct_PositionLimitsSW |  |  |  |  |
|  | Active | BOOL | - | DIR | FALSE | Monitoring deactivated |
| TRUE | Monitoring enabled |  |  |  |  |  |
| MinPosition | LREAL | -1.0E12 to 1.0E12 | DIR | Position of negative software limit switches |  |  |
| MaxPosition | LREAL | -1.0E12 to 1.0E12 | DIR | Position of positive software limit switches ("MaxPosition" > "MinPosition") |  |  |
| LimitReachedBehavior | DINT | 0 … 1 | RES | Alarm response when a software limit switch is approached with a single axis job |  |  |
| 0 | Stop with maximum dynamic values |  |  |  |  |  |
| 1 | Stop with current dynamic values |  |  |  |  |  |
| LimitExceededBehavior | DINT | 0 … 1 | RES | Alarm response when overrunning a software limit switch |  |  |
| 0 | Disable axis |  |  |  |  |  |
| 1 | Keep emergency stop and axis enable |  |  |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "PositionLimits_HW" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositionLimits_HW.<tag name>" contains the configuration of position monitoring with hardware limit switches. Hardware limit switches are used to limit the traversing range of a positioning axis.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| PositionLimits_HW. |  | TO_Struct_PositionLimitsHW |  |  |  |  |
|  | Active | BOOL | - | RES | FALSE | Monitoring deactivated |
| TRUE | Monitoring enabled |  |  |  |  |  |
| With "Active", both (negative and positive) hardware limit switches are activated or deactivated. |  |  |  |  |  |  |
| MinSwitchLevel | BOOL | - | RES | Level selection for activation of the negative hardware limit switch |  |  |
| FALSE | Low level (Low active) |  |  |  |  |  |
| TRUE | High level (high-enabled) |  |  |  |  |  |
| MinSwitchAddress | VREF | 0 to 65535 | RES | Address for the negative hardware limit switch |  |  |
| MaxSwitchLevel | BOOL | - | RES | Level selection for activation of the positive hardware limit switch |  |  |
| FALSE | Low level (Low active) |  |  |  |  |  |
| TRUE | High level (high-enabled) |  |  |  |  |  |
| MaxSwitchAddress | VREF | 0 to 65535 | RES | Address for the positive hardware limit switch |  |  |
| Mode | DINT | 0, 1 | RES | Type of HW limit switch |  |  |
| 0 | Switch non-traversable |  |  |  |  |  |
| 1 | Switch traversable |  |  |  |  |  |
| AppoachBehavior | DINT | 0, 1 | RES | Alarm response when approaching a HW limit switch |  |  |
| 0 | Disable axis |  |  |  |  |  |
| 1 | Keep emergency stop and axis enable |  |  |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "Homing" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Homing.<tag name>" contains the configuration for homing the TO.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Homing. |  | TO_Struct_Homing / TO_Struct_ExternalEncoder_Homing |  |  |  |  |
|  | AutoReversal | BOOL | - | RES | Reversal at the hardware limit switches |  |
| FALSE | No |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |
| ApproachDirection | BOOL | - | CAL | Direction of approach to the homing position switch |  |  |
| FALSE | Positive direction |  |  |  |  |  |
| TRUE | Negative direction |  |  |  |  |  |
| ApproachVelocity | LREAL | Linear: 0.0 to 10000.0 mm/s | CAL | Approach velocity  Velocity during active homing at which the reference output cam and home position are approached. |  |  |
| Rotary: 0.0 to 360000.0 °/s |  |  |  |  |  |  |
| ReferencingVelocity | LREAL | Linear: 0.0 to 1000.0 mm/s | CAL | Homing velocity   Velocity during active homing at which the home position is approached. |  |  |
| Rotary: 0.0 to 36000.0 °/s |  |  |  |  |  |  |
| HomePosition | LREAL | -1.0E12 to 1.0E12 | CAL | Home position |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "Override" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Override.<tag name>" contains the configuration of override parameters. The override parameters are used to apply a correction percentage to default values. An override change takes effect immediately, and is performed with the dynamic settings in effect in the Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Override. |  | TO_Struct_Override |  |  |  |
|  | Velocity | LREAL | 0.0 to 200.0% | DIR | Velocity or speed override  Percentage correction of the velocity/speed |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "PositionControl" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositionControl.<tag name>" contains the settings of position control.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PositionControl. |  |  | TO_Struct_PositionControl |  |  |  |  |
|  | Kv |  | LREAL | 0.0 to 2147480.0 | DIR | Proportional gain of the closed loop position control ("Kv" > 0.0) |  |
| Kpc |  | LREAL | 0.0 to 150.0% | DIR | Velocity precontrol of the position control   Recommended setting:  - Isochronous drive connection via PROFIdrive:   100.0% - Non-isochronous drive connection via PROFIdrive:    0.0 to 100.0% - Analog drive connection:    0.0 to 100.0% |  |  |
| EnableDSC |  | BOOL | - | RES | Dynamic Servo Control (DSC) |  |  |
| FALSE | DSC disabled |  |  |  |  |  |  |
| TRUE | DSC activated |  |  |  |  |  |  |
| DSC is only possible with one of the following PROFIdrive telegrams:  - Standard telegram 5 or 6 - SIEMENS telegram 105 or 106 |  |  |  |  |  |  |  |
| SmoothingTimeByChangeDifference |  | LREAL | 0.0 to 1.0E12 s | DIR | Smoothing time for the manipulated variable for switching operations, for example:  - Encoder switchover - Change in P-gain ("Kv") - Switchover to emergency stop ramp |  |  |
| InitialOperativeSensor |  | UDINT | 1 to 4 | RES | Active sensor after initialization of the axis (sensor number 1 to 4)  This encoder is used after startup of the CPU and after a [restart of the technology object](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#restart-of-technology-objects-s7-1500-s7-1500t). At an operating mode transition from STOP → RUN of the CPU (without restart of the technology object), the encoder that was also active before the STOP is still being used. |  |  |
| ControlDifferenceQuantization. |  | TO_Struct_PositionDifferenceQuantification |  |  |  |  |  |
|  | Mode | DINT | - | RES | Type of quantification  Configuration of a quantization when a drive with stepper motor interface is connected |  |  |
| 0 | No quantification |  |  |  |  |  |  |
| 1 | Quantization corresponding to encoder resolution |  |  |  |  |  |  |
| 2 | Quantization to a direct value |  |  |  |  |  |  |
| (configuration is performed using the parameter view (data structure)) |  |  |  |  |  |  |  |
| Value | LREAL | 0.001 to 1.0E12 | RES | Value of quantification  Configuration of a value for quantization to a direct value ("<TO>.PositionControl.ControlDifferenceQuantization.Mode" = 2)  (configuration is performed using the parameter view (data structure)) |  |  |  |
| VelocityModePowerOn |  | DINT | 0 to 1 | RES | Behavior of the velocity setpoint when the axis is enabled |  |  |
| 0 | Velocity is set to "0" with maximum dynamic values of the axis (ramp). |  |  |  |  |  |  |
| 1 | Velocity is immediately set to "0" without ramp. |  |  |  |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "TorquePreControl" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.TorquePreControl.<tag name>" contains the settings of the torque precontrol.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| TorquePreControl. |  | TO_Struct_TorquePreControl |  |  |  |  |
|  | Mode | DINT | 0, 1 | RES | Mode of torque precontrol (effect only in position-controlled mode) |  |
| 0 | Torque precontrol not in effect |  |  |  |  |  |
| 1 | Torque precontrol based on the acceleration of the axis |  |  |  |  |  |
| Scale | LREAL | 0.0 … 150.0 | DIR | Weighting factor for the value of the torque precontrol [%] |  |  |

#### "SetpointFilter" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.SetpointFilter.<tag name>" contains the settings of the setpoint filter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SetpointFilter. |  |  | TO_Struct_SetpointFilter |  |  |  |  |
|  | DynamicFilter. |  | TO_Struct_DynamicFilter |  |  |  |  |
|  | Mode | DINT | 0 to 2 | RES | Dynamic filter mode |  |  |
| 0 | Dynamic filter not active |  |  |  |  |  |  |
| 1 | PT1/PT2 filter + dead time |  |  |  |  |  |  |
| 2 | Sliding window demand + dead time |  |  |  |  |  |  |
| T1 | LREAL | 0.0 to 1.0E12 | DIR | First time constant of the sliding window demand  The value is internally limited to the 16-fold servo clock. |  |  |  |
| T2 | LREAL | 0.0 to 1.0E12 | DIR | Second time constant of the sliding window demand  The value is internally limited to the 16-fold servo clock. |  |  |  |
| Tt | LREAL | 0.0 to 1.0E12<sup>1)</sup> | DIR | Additional dead time of the dynamic filter in time unit of the axis |  |  |  |
| <sup>1)</sup> The dead time T<sub>t</sub> is internally limited to sixteen times the value from the application cycle of the MC_Servo. No alarm is output at higher values. |  |  |  |  |  |  |  |

#### "DynamicAxisModel" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicAxisModel.<tag name>" contains the balancing filter settings.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicAxisModel. |  | TO_Struct_DynamicAxisModel |  |  |  |
|  | VelocityTimeConstant | LREAL | 0.0 to 1.0E12 | DIR | Speed control loop substitute time [s] |
| AdditionalPositionTimeConstant | LREAL | 0.0 to 1.0E12 | DIR | Additive position control loop substitute time [s] |  |
| CurrentTimeConstant | LREAL | 0.0 to 1.0E12 | DIR | Current control loop substitute time in time unit of the axis |  |

#### "FollowingError" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.FollowingError.<tag name>" contains the configuration of the dynamic following error monitoring.

If the permissible following error is exceeded, then technology alarm 521 is output, and the technology object is disabled (alarm reaction: remove enable).

When the warning level is reached, a warning is output (technology alarm 522).

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| FollowingError. |  | TO_Struct_FollowingError |  |  |  |  |
|  | EnableMonitoring | BOOL | - | RES | FALSE | Following error monitoring deactivated |
| TRUE | Following error monitoring enabled |  |  |  |  |  |
| MinValue | LREAL | Linear:  0.0 to 1.0E12 | DIR | Permissible following error at velocities below the value of "MinVelocity" |  |  |
| Rotary:  0.001 to 1.0E12 |  |  |  |  |  |  |
| MaxValue | LREAL | Linear: 0.0 to 1.0E12 | DIR | Maximum permissible following error, which may be reached at the maximum velocity. |  |  |
| Rotary: 0.002 to 1.0E12 |  |  |  |  |  |  |
| MinVelocity | LREAL | 0.0 to 1.0E12 | DIR | "MinValue" is permissible below this velocity and is held constant. |  |  |
| WarningLevel | LREAL | 0.0 to 100.0 | DIR | Warning level  Percentage value relative to the valid maximum following error |  |  |
| AdditionalSetpointDelayTime | LREAL | 0.0 to 1.0E12 | DIR | Time constant for additional deceleration of position setpoint to calculate the following error in the time unit of the axis |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "PositioningMonitoring" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositioningMonitoring.<tag name>" contains the configuration of position monitoring at the end of a positioning motion.

If the actual position value at the end of a positioning motion is reached within the tolerance time and remains in the positioning window for the minimum dwell time, then "<TO>.StatusWord.X6 (Done)" is set in the technology data block. This completes a Motion Control job.

If the tolerance time is exceeded, then technology alarm 541 "Positioning monitoring" with supplemental value 1: "Target range not reached" is displayed.

If the minimum dwell time is not met, then technology alarm 541 "Positioning monitoring" with supplemental value 2: "Exit target range again" is displayed.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| PositioningMonitoring. |  | TO_Struct_PositionMonitoring |  |  |  |
|  | ToleranceTime | LREAL | 0.0 to 1.0E12 | DIR | Tolerance time  Maximum permitted duration from reaching of velocity setpoint zero until entrance into the positioning window |
| MinDwellTime | LREAL | 0.0 to 1.0E12 | DIR | Minimum dwell time in positioning window |  |
| Window | LREAL | 0.001 to 1.0E12 | DIR | Positioning window |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "StandstillSignal" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StandstillSignal.<tag name>" contains the configuration of the standstill signal.

If the actual velocity value is below the velocity threshold, and does not exceed it during the minimum dwell time, then the standstill signal "<TO>.StatusWord.X7 (Standstill)" is set.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StandstillSignal. |  | TO_Struct_StandstillSignal |  |  | Configuration for the standstill signal |
|  | VelocityThreshold | LREAL | 0.0 to 1.0E12 | DIR | Velocity threshold  If velocity is below this threshold, the minimum dwell time begins. |
| MinDwellTime | LREAL | 0.0 to 1.0E12 | DIR | Minimum dwell time |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "StatusPositioning" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusPositioning.<tag name>" indicates the status of a positioning motion.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusPositioning. |  | TO_Struct_StatusPositioning |  |  |  |
|  | Distance | LREAL | -1.0E12 to 1.0E12 | RON | Distance to target position |
| TargetPosition | LREAL | -1.0E12 to 1.0E12 | RON | Target position |  |
| TargetPositionModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles to target position with positioning motions |  |
| FollowingError | LREAL | -1.0E12 to 1.0E12 | RON | Current following error |  |
| SetpointExecutionTime | LREAL | 0 to 1.0E12 | RON | Setpoint execution time of the axis  (Results from T<sub>Ipo</sub>, T<sub>vtc</sub> or 1/kv, T<sub>Send</sub> and T<sub>O</sub> of the axis) |  |
| SuperimposedDistance | LREAL | 0 to 1.0E12 | RON | Distance traveled with the instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed", and "MC_HaltSuperimposed".   The value is reset when the base motion and the superimposed motion are completed. |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "StatusDrive" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusDrive.<tag name>" indicates the status of the drive.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusDrive. |  | TO_Struct_StatusDrive |  |  |  |  |
|  | InOperation | BOOL | - | RON | Operation status of the drive |  |
| FALSE | Drive not ready  Setpoints will not be executed. |  |  |  |  |  |
| TRUE | Drive ready  Setpoints can be executed. |  |  |  |  |  |
| CommunicationOK | BOOL | - | RON | Cyclic BUS communication between controller and drive |  |  |
| FALSE | Cyclic communication not established.  Fault ZSW1.X3 (FaultPresent) is present.  Possible causes:  - The CPU is in STOP. - The drive has failed. - The "ControlRequested" bit in the status word of the drive has the value "FALSE". - The drive signals an error using the status word. - For isochronous configuration, the dynamic sign of life in the telegram has failed or is not supplied by the drive. |  |  |  |  |  |
| TRUE | Cyclic communication OK and no fault effective |  |  |  |  |  |
| Error | BOOL | - | RON | FALSE | No drive error |  |
| TRUE | Drive error |  |  |  |  |  |
| AdaptionState | DINT | 0 to 4 | RON | Status of automatic data transfer of drive parameters |  |  |
| 0 | "NOT_ADAPTED"  Data not transferred |  |  |  |  |  |
| 1 | "IN_ADAPTION"  Data transfer in progress |  |  |  |  |  |
| 2 | "ADAPTED"  Data transfer complete |  |  |  |  |  |
| 3 | "NOT_APPLICABLE"  Data transfer not selected, not possible |  |  |  |  |  |
| 4 | "ADAPTION_ERROR"  Error during data transfer |  |  |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "StatusServo" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusServo.<tag name>" indicates the status for the balancing filter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusServo. |  | TO_Struct_StatusServo |  |  |  |
|  | BalancedPosition | LREAL | - | RON | Position setpoint after the balancing filter |
| ControlDifference | LREAL | - | RON | Control deviation |  |
| PositionAfterDynamicFilter | LREAL | - | RON | Position setpoint after the dynamic filter |  |

#### "StatusProvidedLeadingValue" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusProvidedLeadingValue.<tag name>" contains the provided leading value with leading value delay of the cross-PLC synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusProvidedLeadingValue. |  |  | TO_Struct_StatusProvidedLeadingValue |  |  | Provided leading value |
|  | DelayedLeadingValue |  | TO_Struct_ProvidedLeadingValue |  |  | Leading value with leading value delay |
|  | Position | LREAL | -1.0E12 to 1.0E12 | RON | Position |  |
| Velocity | LREAL | -1.0E12 to 1.0E12 | RON | Velocity |  |  |
| Acceleration | LREAL | -1.0E12 to 1.0E12 | RON | Acceleration |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### StatusSensor[1..4] Tags (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusSensor[1..4].<tag name>" indicates the status of the measuring system.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusSensor[1..4]. |  | Array [1..4] OF TO_Struct_StatusSensor |  |  |  |  |
|  | State | DINT | 0 to 2 | RON | Status of the actual encoder value |  |
| 0 | "NOT_VALID"  Invalid |  |  |  |  |  |
| 1 | "WAITING_FOR_VALID"  Waiting for "Valid" status |  |  |  |  |  |
| 2 | "VALID"  Valid |  |  |  |  |  |
| CommunicationOK | BOOL | - | RON | Cyclic BUS communication between controller and encoder |  |  |
| FALSE | Not established |  |  |  |  |  |
| TRUE | Established |  |  |  |  |  |
| Error | BOOL | - | RON | FALSE | No error in the measuring system |  |
| TRUE | Error in the measuring system. |  |  |  |  |  |
| AbsEncoderOffset | LREAL | - | RON | Home position offset for value of an absolute value encoder.  The value will be retentively stored in the CPU. |  |  |
| Control | BOOL | - | RON | FALSE | Encoder is not active |  |
| TRUE | Encoder is active |  |  |  |  |  |
| Position | LREAL | - | RON | Encoder position |  |  |
| Velocity | LREAL | - | RON | Encoder velocity |  |  |
| AdaptionState | DINT | 0 to 4 | RON | Status of automatic data transfer of encoder parameters |  |  |
| 0 | "NOT_ADAPTED"  Data not transferred |  |  |  |  |  |
| 1 | "IN_ADAPTION"  Data transfer in progress |  |  |  |  |  |
| 2 | "ADAPTED"  Data transfer complete |  |  |  |  |  |
| 3 | "NOT_APPLICABLE"  Data transfer not selected, not possible |  |  |  |  |  |
| 4 | "ADAPTION_ERROR"  Error during data transfer |  |  |  |  |  |
| ModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles |  |  |
| Adjusted | DINT | 0, 1 | RON | Homing status of the encoder |  |  |
| 0 | Encoder not homed |  |  |  |  |  |
| 1 | Encoder homed with one of the following homing types:  - Active homing - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment |  |  |  |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "StatusExtrapolation" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusExtrapolation.<tag name>" indicates the status of the actual value extrapolation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusExtrapolation. |  | TO_Struct_StatusExtrapolation |  |  |  |
|  | FilteredPosition | LREAL | -1.0E12 to 1.0E12 | RON | Position after position filter |
| FilteredVelocity | LREAL | -1.0E12 to 1.0E12 | RON | Velocity after velocity filter and tolerance band |  |
| ExtrapolatedPosition | LREAL | -1.0E12 to 1.0E12 | RON | Extrapolated position |  |
| ExtrapolatedVelocity | LREAL | -1.0E12 to 1.0E12 | RON | Extrapolated velocity |  |

#### "StatusKinematicsMotion" tag (positioning axis) (S7-1500, S7-1500T)

The "<TO>.StatusKinematicsMotion" tag contains status information of the technology object with regard to usage as kinematics axis.

Information on the evaluation of the individual bits (e.g. bit 2 "MaxDecelerationExceeded") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tag

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusKinematicsMotion |  | DWORD | - | RON | Status information of the technology object |  |
|  | Bit 0 | - | - | - | "MaxVelocityExceeded" |  |
| 0 | The kinematics technology object calculated a lower velocity setpoint than the maximum velocity on the axis. |  |  |  |  |  |
| 1 | The kinematics technology object calculated a higher velocity setpoint than the maximum velocity on the axis. |  |  |  |  |  |
| Bit 1 | - | - | - | "MaxAccelerationExceeded" |  |  |
| 0 | The kinematics technology object calculated a lower setpoint acceleration calculated than the maximum acceleration of the axis. |  |  |  |  |  |
| 1 | The kinematics technology object calculated a higher setpoint acceleration than the maximum acceleration of the axis. |  |  |  |  |  |
| Bit 2 | - | - | - | "MaxDecelerationExceeded" |  |  |
| 0 | The kinematics technology object calculated a lower setpoint deceleration than the maximum deceleration of the axis. |  |  |  |  |  |
| 1 | The kinematics technology object calculated a lower setpoint deceleration than the maximum deceleration of the axis. |  |  |  |  |  |

#### "StatusTorqueData" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusTorqueData.<tag name>" indicates the status of the torque data/force data.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusTorqueData. |  | TO_Struct_StatusTorqueData |  |  |  |  |
|  | CommandAdditiveTorqueActive | DINT | 0, 1 | RON | Additive setpoint torque/additive setpoint force |  |
| 0 | Inactive |  |  |  |  |  |
| 1 | Active |  |  |  |  |  |
| CommandTorqueRangeActive | DINT | 0, 1 | RON | Torque limits/force limits B +, B- |  |  |
| 0 | Inactive |  |  |  |  |  |
| 1 | Active |  |  |  |  |  |
| ActualTorque | LREAL | -1.0E12 to 1.0E12 | RON | Actual torque of the axis |  |  |
| ActualForce | LREAL | -1.0E12 to 1.0E12 | RON | Actual force of the axis |  |  |
| TotalTorqueAdditive | LREAL | -1.0E12 to 1.0E12 | RON | Effective additional torque of the axis |  |  |
| TotalForceAdditve | LREAL | -1.0E12 to 1.0E12 | RON | Effective additional force of the axis |  |  |

#### "StatusMotionIn" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusMotionIn.<tag name>" indicates the status of the "MotionIn" function.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusMotionIn. |  |  | TO_Struct_StatusMotionIn |  |  |  |  |
|  | FunctionState |  | DINT | 0 to 2 | RON | 0 | No "MotionIn" function active |
| 1 | "MC_MotionInVelocity" active |  |  |  |  |  |  |
| 2 | "MC_MotionInPosition" active |  |  |  |  |  |  |
| StatusWord. |  | DWORD | - | RON | - |  |  |
|  | Bit 0 | Bool | - | RON | "Max­Velocity­Exceeded"  The configured maximum velocity is exceeded during a MotionIn movement. |  |  |
| Bit 1 …  Bit 31 | Bool | - | RON | Reserved |  |  |  |

#### "StatusInterpreterMotion" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusInterpreterMotion.<tag name>" contains status information on motion jobs controlled by a technology object Interpreter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusInterpreterMotion. |  |  | TO_Struct_StatusInterpreterMotion |  |  |  |
|  | Interpreter |  | DB_ANY | 0 to 65535 |  | Controlling Interpreter technology object |
| StatusWord. |  | DWORD | - | RON | Status information |  |
|  | Bit 0 | - | - | - | "ControlledByInterpreter"  An MCL job is processed or active or the bit is set via the MCL instruction "[setControlledByInterpreter()](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#setcontrolledbyinterpreter-set-controlledbyinterpreter-bit-for-a-technology-object-s7-1500t)". |  |
| Bit 1 | - | - | - | "MotionByInterpreter"  An MCL motion job is in effect. |  |  |
| Bit 2 to Bit 31 | - | - | - | Reserved |  |  |

#### "StatusWord" tag (positioning axis) (S7-1500, S7-1500T)

The "<TO>.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 5 "HomingDone") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Enable"  Enable status  The technology object has been enabled. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object will be reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "ControlPanelActive"  The axis control panel is active. |  |
| Bit 5 | - | - | - | "HomingDone"  Homing status  The technology object is homed. |  |
| Bit 6 | - | - | - | "Done"  No motion job is in progress and the axis control panel is deactivated. |  |
| Bit 7 | - | - | - | "Standstill"  Standstill signal  The axis is at a standstill. |  |
| Bit 8 | - | - | - | "PositioningCommand"  A positioning command is active ("MC_MoveRelative","MC_MoveAbsolute"). |  |
| Bit 9 | - | - | - | "JogCommand"  An "MC_MoveJog" job is running. |  |
| Bit 10 | - | - | - | "VelocityCommand"  An "MC_MoveVelocity" job is running. |  |
| Bit 11 | - | - | - | "HomingCommand"  An "MC_Home" job is being processed. |  |
| Bit 12 | - | - | - | "ConstantVelocity"  The velocity setpoint is reached. A constant velocity setpoint is output. |  |
| Bit 13 | - | - | - | "Accelerating"  An acceleration operation is active. |  |
| Bit 14 | - | - | - | "Decelerating"  A deceleration operation is active. |  |
| Bit 15 | - | - | - | "SWLimitMinActive"  A negative software limit switch has been approached or exceeded. |  |
| Bit 16 | - | - | - | "SWLimitMaxActive"  A positive software limit switch has been approached or exceeded. |  |
| Bit 17 | - | - | - | "HWLimitMinActive"  A negative hardware limit switch has been approached or exceeded. |  |
| Bit 18 | - | - | - | "HWLimitMaxActive"  A positive hardware limit switch has been approached or exceeded. |  |
| Bit 19 …  Bit 22 | - | - | - | Reserved |  |
| Bit 23 | - | - | - | "MoveSuperimposedCommand"  An "MC_MoveSuperimposed" job is running. |  |
| Bit 24 | - | - | - | Reserved |  |
| Bit 25 | - | - | - | "AxisSimulation"  The technology object is in simulation. |  |
| Bit 26 | - | - | - | "TorqueLimitingCommand"  An "MC_TorqueLimiting" job is running. |  |
| Bit 27 | - | - | - | "InLimitation"<sup>1</sup>  The drive operates at least at the threshold value (default 90%) of the torque limit/force limitation. |  |
| Bit 28 | - | - | - | "NonPositionControlled"  The axis is not in position-controlled mode. |  |
| Bit 29 | - | - | - | "KinematicsMotionCommand"  The axis is used for a kinematics job. |  |
| Bit 30 | - | - | - | "InClamping"  The axis is clamped at a fixed stop. |  |
| Bit 31 | - | - | - | "MotionInCommand"  A "MotionIn" job is running. |  |
| <sup>1</sup> The bit is correctly displayed only when using SIEMENS telegram 10x. When using MC_TorqueRange without SIEMENS telegram 10x, compare the values from telegram 750: <InLimit> = ActualTorque (M_ACT) * 0.9 > UpperTorqueLimit (M_LIMIT_POS) OR ActualTorque (M_ACT) * 0.9 < LowerTorqueLimit (M_LIMIT_NEG) |  |  |  |  |  |

#### "StatusWord2" tag (positioning axis) (S7-1500, S7-1500T)

The "<TO>.StatusWord2" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 0 "StopCommand") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord2 |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | BOOL | - | RON | "StopCommand"  An "MC_Stop" job is running. The technology object is disabled. |
| Bit 1 | BOOL | - | RON | Reserved |  |
| Bit 2 | BOOL | - | RON | "PassingBacklash"  The backlash is traversed. "<TO>.ActualPosition" does not hereby change. |  |
| Bit 3 ...  Bit 5 | BOOL | - | RON | Reserved |  |
| Bit 6 | BOOL | - | RON | "MotionInSuperimposedCommand"  An "MC_MotionInSuperimposed" job is running. |  |
| Bit 7 | BOOL | - | RON | "HaltSuperimposedCommand"  An "MC_HaltSuperimposed" job is running. |  |
| Bit 8 ...  Bit 31 | BOOL | - | RON | Reserved |  |

#### "ErrorWord" tag (positioning axis) (S7-1500, S7-1500T)

The "<TO>.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | "DriveFault"  Error in drive |  |
| Bit 5 | - | - | - | "SensorFault"  Error in encoder system |  |
| Bit 6 | - | - | - | "DynamicError"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 | - | - | - | "CommunicationFault"  Communication error  Missing or faulty communication. |  |
| Bit 8 | - | - | - | "SWLimit"  Software limit switch reached or overtraveled. |  |
| Bit 9 | - | - | - | "HWLimit"  Hardware limit switch reached or overtraveled. |  |
| Bit 10 | - | - | - | "HomingError"  Error during homing operation  The homing cannot be completed. |  |
| Bit 11 | - | - | - | "FollowingErrorFault"  Following error limits exceeded |  |
| Bit 12 | - | - | - | "PositioningFault"  Positioning error |  |
| Bit 13 | - | - | - | "PeripheralError"  Error accessing a logical address |  |
| Bit 14 | - | - | - | Reserved |  |
| Bit 15 | - | - | - | "AdaptionError"  Error in automatic data transfer |  |
| Bit 16 ...  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.ErrorDetail.<tag name>" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0 to 5 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 1 | Stop with current dynamic values |  |  |  |  |  |
| 2 | Stop with maximum dynamic values |  |  |  |  |  |
| 3 | Stop with emergency stop ramp |  |  |  |  |  |
| 4 | Remove enable |  |  |  |  |  |
| 5 | Track setpoints |  |  |  |  |  |

#### "WarningWord" tag (positioning axis) (S7-1500, S7-1500T)

The "<TO>.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 13 "PeripheralWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | "DriveWarning"  Warning of the drive  When a warning message is pending at the drive that does not result in a TO alarm, this bit is not set. Evaluate the drive warnings directly using the status word of the drive. |  |
| Bit 5 | - | - | - | "SensorWarning"  Error in encoder system |  |
| Bit 6 | - | - | - | "DynamicWarning"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 | - | - | - | "CommunicationWarning"  Communication error  Missing or faulty communication. |  |
| Bit 8 | - | - | - | "SWLimitMin"  The negative software limit switch has been approached. |  |
| Bit 9 | - | - | - | "SWLimitMax"  The positive software limit switch has been approached. |  |
| Bit 10 | - | - | - | "HomingWarning"  Error during homing operation  The homing cannot be completed. |  |
| Bit 11 | - | - | - | "FollowingErrorWarning"  Warning limit of following error monitoring reached/exceeded |  |
| Bit 12 | - | - | - | "PositioningWarning"  Positioning error |  |
| Bit 13 | - | - | - | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14 | - | - | - | Reserved |  |
| Bit 15 | - | - | - | "AdaptionWarning"  Error in automatic data transfer |  |
| Bit 16... Bit 31 | - | - | - | Reserved |  |

#### "ControlPanel" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.ControlPanel.<tag name>" contains no relevant data for you. This tag structure is internally used.

#### "InternalToTrace" tag (positioning axis) (S7-1500, S7-1500T)

The tag structure "<TO>.InternalToTrace.<tag name>" contains no relevant data for you. This tag structure is internally used.

### Tags of the technology object external encoder (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t-2)
- [Actual values and setpoints (external encoder) (S7-1500, S7-1500T)](#actual-values-and-setpoints-external-encoder-s7-1500-s7-1500t)
- ["Sensor" tag (external encoder) (S7-1500, S7-1500T)](#sensor-tag-external-encoder-s7-1500-s7-1500t)
- ["CrossPlcSynchronousOperation" tag (external encoder) (S7-1500, S7-1500T)](#crossplcsynchronousoperation-tag-external-encoder-s7-1500-s7-1500t)
- ["Extrapolation" tag (external encoder) (S7-1500, S7-1500T)](#extrapolation-tag-external-encoder-s7-1500-s7-1500t)
- ["LoadGear" tag (external encoder) (S7-1500, S7-1500T)](#loadgear-tag-external-encoder-s7-1500-s7-1500t)
- ["Properties" tag (external encoder) (S7-1500, S7-1500T)](#properties-tag-external-encoder-s7-1500-s7-1500t)
- ["Units" tag (external encoder) (S7-1500, S7-1500T)](#units-tag-external-encoder-s7-1500-s7-1500t)
- ["Mechanics" tag (external encoder) (S7-1500, S7-1500T)](#mechanics-tag-external-encoder-s7-1500-s7-1500t)
- ["Modulo" tag (external encoder) (S7-1500, S7-1500T)](#modulo-tag-external-encoder-s7-1500-s7-1500t)
- ["Homing" tag (external encoder) (S7-1500, S7-1500T)](#homing-tag-external-encoder-s7-1500-s7-1500t)
- [Variable "StandstillSignal" (external encoder) (S7-1500, S7-1500T)](#variable-standstillsignal-external-encoder-s7-1500-s7-1500t)
- ["StatusProvidedLeadingValue" tag (external encoder) (S7-1500, S7-1500T)](#statusprovidedleadingvalue-tag-external-encoder-s7-1500-s7-1500t)
- ["StatusSensor" tag (external encoder) (S7-1500, S7-1500T)](#statussensor-tag-external-encoder-s7-1500-s7-1500t)
- ["StatusExtrapolation" tag (external encoder) (S7-1500, S7-1500T)](#statusextrapolation-tag-external-encoder-s7-1500-s7-1500t)
- ["StatusWord" tag (external encoder) (S7-1500, S7-1500T)](#statusword-tag-external-encoder-s7-1500-s7-1500t)
- ["ErrorWord" tag (external encoder) (S7-1500, S7-1500T)](#errorword-tag-external-encoder-s7-1500-s7-1500t)
- ["ErrorDetail" tag (external encoder) (S7-1500, S7-1500T)](#errordetail-tag-external-encoder-s7-1500-s7-1500t)
- ["WarningWord" tag (external encoder) (S7-1500, S7-1500T)](#warningword-tag-external-encoder-s7-1500-s7-1500t)
- ["InternalToTrace" tag (external encoder) (S7-1500, S7-1500T)](#internaltotrace-tag-external-encoder-s7-1500-s7-1500t)

#### Legend (S7-1500, S7-1500T)

|  |  |  |
| --- | --- | --- |
| Tag | Name of the tag |  |
| Data type | Data type of the tag |  |
| Values | Value range of the tag - minimum value to maximum value  If no specific value is shown, the value range limits of the relevant data type apply or the information under "Description". |  |
| W | Effectiveness of changes in the technology data block |  |
| DIR | Direct:  Values are changed via direct assignment and take effect at the start of the next MC_Servo. |  |
| CAL | At call of Motion Control instruction:  Values are changed directly and take effect at the start of the next MC_Servo after the call of the corresponding Motion Control instruction in the user program. |  |
| RES | Restart:  Changes to the start value in the load memory are made using the extended instruction "WRIT_DBL" (write to DB in load memory). Changes will not take effect until after restart of the technology object. |  |
| RON | Read only:  The tag cannot and must not be changed during runtime of the user program. |  |
| Description | Description of the tag |  |

Access to the tags is with "<TO>.<tag name>". The placeholder <TO> represents the name of the technology object.

#### Actual values and setpoints (external encoder) (S7-1500, S7-1500T)

The following tags indicate the setpoint and actual values of the technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag | Data type | Values | W | Description |
| --- | --- | --- | --- | --- |
| ActualPosition | LREAL | - | RON | Actual position |
| ActualVelocity | LREAL | - | RON | Actual velocity |
| ActualAcceleration | LREAL | - | RON | Actual acceleration |
| ActualModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles of the actual value |

#### "Sensor" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Sensor.<tag name>" contains the controller-side configuration for the encoder, and the configuration for passive homing.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sensor. |  |  | TO_Struct_ExternalEncoder_Sensor |  |  |  |  |
|  | Type |  | DINT | 0 to 2 | RON | Encoder type |  |
| 0 | "INCREMENTAL"  Incremental |  |  |  |  |  |  |
| 1 | "ABSOLUTE"  Absolute |  |  |  |  |  |  |
| 2 | "CYCLIC_ABSOLUTE"  Cyclic absolute |  |  |  |  |  |  |
| InverseDirection |  | BOOL | - | RES | Inversion of the actual value |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| System |  | DINT | 0, 1 | RES | Encoder system |  |  |
| 0 | "LINEAR"  Linear encoder |  |  |  |  |  |  |
| 1 | "ROTATORY"  Rotary encoder |  |  |  |  |  |  |
| MountingMode |  | DINT | 0 to 2 | RES | Mounting type of encoder |  |  |
| 0 | On motor shaft |  |  |  |  |  |  |
| 1 | On load side |  |  |  |  |  |  |
| 2 | External measuring system |  |  |  |  |  |  |
| DataAdaption |  | DINT | 0, 1 | RES | Automatic transfer of the drive values reference speed, maximum speed and reference torque in the device |  |  |
| 0 | No automatic transfer, manual configuration of values |  |  |  |  |  |  |
| 1 | Automatic transfer of values configured in the drive to the configuration of the technology object |  |  |  |  |  |  |
| ActualVelocityMode |  | DINT | 0, 1 | RES | Type of calculation for actual speed value or actual velocity value |  |  |
| 0 | Actual value calculation from differentiation of the position change |  |  |  |  |  |  |
| 1 | Actual value calculation with NACT value from the telegram |  |  |  |  |  |  |
| Interface. |  |  |  |  |  |  |  |
|  | AddressIn | VREF | 0 to 65535 | RON | Input address for the PROFIdrive telegram |  |  |
| AddressOut | VREF | 0 to 65535 | RON | Output address for the PROFIdrive telegram |  |  |  |
| Number | UDINT | 1 to 2 | RON | Number of the encoder in the telegram |  |  |  |
| Parameter. |  |  |  |  |  |  |  |
|  | Resolution | LREAL | -1.0E12 to 1.0E12 | RES | Resolution of a linear encoder (offset between two encoder pulses) |  |  |
| StepsPerRevolution | UDINT | 1 to 8388608 | RES | Increments per rotary encoder revolution |  |  |  |
| FineResolutionXist1 | UDINT | 0 to 31 | RES | Number of bits for fine resolution "Gx_XIST1" (cyclic actual encoder value) |  |  |  |
| FineResolutionXist2 | UDINT | 0 to 31 | RES | Number of bits for fine resolution "Gx_XIST2" (absolute value of the encoder) |  |  |  |
| DeterminableRevolutions | UDINT | 0 to 8388608 | RES | Number of differentiable encoder revolutions for a multi-turn absolute encoder   (For a single-turn absolute encoder = 1; for an incremental encoder = 0) |  |  |  |
| DistancePerRevolution | LREAL | 0.0 to 1.0E12 | RES | Load distance per revolution of an externally mounted encoder |  |  |  |
| BehaviorGx_XIST1 | DINT | 0, 1 | RES | Evaluation of "Gx_XIST1" bits. |  |  |  |
| 0 | Based on the bits of the encoder resolution.  The incremental actual value "Gx_XIST1" is transmitted with less than 32 bits in the PROFIdrive telegram. For example: At 16 bits, the value ranges from 0 to 65,535. |  |  |  |  |  |  |
| 1 | 32-bit value of the encoder value  The "Gx_XIST1" incremental actual value is transferred with 32 bits of 0 to 4,294,967,295 in the PROFIdrive telegram. |  |  |  |  |  |  |
| ReferenceSpeed | LREAL | 0.0 to 1.0E12 | RES | Reference speed for NACT in PROFIdrive telegram with rotary encoder  Only relevant for "ActualVelocityMode" = 1 |  |  |  |
| ReferenceVelocity | LREAL | 0.0 to 1.0E12 | RES | Reference velocity for NACT in the PROFIdrive telegram with linear encoder  Only relevant for "ActualVelocityMode" = 1 |  |  |  |
| PassiveHoming. |  | TO_Struct_SensorPassiveHoming |  |  |  |  |  |
|  | Mode | DINT | 0 to 2 | RES | Homing mode |  |  |
| 0 | Use zero mark via PROFIdrive telegram |  |  |  |  |  |  |
| 1 | Zero mark via PROFIdrive telegram and reference output cam |  |  |  |  |  |  |
| 2 | Use homing mark via digital input |  |  |  |  |  |  |
| SideInput | BOOL | - | CAL | Side of the digital input for passive homing |  |  |  |
| FALSE | Negative side |  |  |  |  |  |  |
| TRUE | Positive side |  |  |  |  |  |  |
| Direction | DINT | 0 to 2 | CAL | Homing direction/approach direction to homing mark |  |  |  |
| 0 | Positive homing direction |  |  |  |  |  |  |
| 1 | Negative homing direction |  |  |  |  |  |  |
| 2 | Current homing direction |  |  |  |  |  |  |
| DigitalInputAddress | VREF | 0 to 65535 | RON | Address of the digital input |  |  |  |
| SwitchLevel | BOOL | - | RON | Signal level that is present at the digital input when homing mark is approached |  |  |  |
| FALSE | Low level |  |  |  |  |  |  |
| TRUE | High level |  |  |  |  |  |  |

#### "CrossPlcSynchronousOperation" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.CrossPlcSynchronousOperation.<tag name>" contains the configuration of the cross-PLC synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CrossPlcSynchronousOperation. |  |  | TO_Struct_CrossPlcSynchronousOperation |  |  |  |  |
|  | Interface[1..8]. |  | ARRAY [1..8] of TO_Struct_CrossPlcLeadingValueInterface |  |  |  |  |
|  | EnableLeadingValueOutput | BOOL | - | RON | Provide cross-PLC leading value |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| AddressOut | VREF | - | RON | Output address for the leading value telegram |  |  |  |
| LocalLeadingValueDelayTime |  | LREAL | 0.0 to 1.0E9 | RES | Delay time of leading value output on the local following axes |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "Extrapolation" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Extrapolation.<tag name>" contains the configuration of the actual value extrapolation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Extrapolation. |  |  | TO_Struct_Extrapolation |  |  |  |  |
|  | LeadingAxisDependentTime |  | LREAL | - | RON | Extrapolation time component (caused by leading axis)  Results from the following times:  - Time of actual value acquisition for the leading axis - Interpolator cycle clock - Time of position filter of actual value extrapolation (T1 + T2) |  |
| FollowingAxisDependentTime |  | LREAL | 0.001 to 1.0E12 | DIR | Extrapolation time component (caused by following axis)  Results from the following times:  - For a following axis with set velocity precontrol:   - Communication cycle   - Interpolator cycle clock   - Speed control loop substitute time for the following axis   - Output delay time of the setpoint at the following axis - For a following axis without velocity precontrol:   - Communication cycle   - Interpolator cycle clock   - Position control loop equivalent time (1/Kv from "<TO>.PositionControl.Kv")   - Output delay time of the setpoint at the following axis |  |  |
| Settings. |  | TO_Struct_ExtrapolationSettings |  |  |  |  |  |
|  | SystemDefinedExtrapolation | DINT | 0, 1 | RES | Leading axis dependent time |  |  |
| 0 | Not effective |  |  |  |  |  |  |
| 1 | Effective |  |  |  |  |  |  |
| ExtrapolatedVelocityMode | DINT | 0, 1 | RES | Effective velocity value for the synchronization function |  |  |  |
| 0 | "FilteredVelocity"  Leading value velocity from filtered actual velocity |  |  |  |  |  |  |
| 1 | "VelocityByDifferentiation"  The leading value velocity results from the differentiation of the extrapolated leading value position |  |  |  |  |  |  |
| PositionFilter. |  | TO_Struct_ExtrapolationPositionFilter |  |  |  |  |  |
|  | T1 | LREAL | 0.0 to 1.0E12 | DIR | Position filter time constant T1 |  |  |
| T2 | LREAL | 0.0 to 1.0E12 | DIR | Position filter time constant T2 |  |  |  |
| VelocityFilter. |  | TO_Struct_ExtrapolationVelocityFilter |  |  |  |  |  |
|  | T1 | LREAL | 0.0 to 1.0E12 | DIR | Velocity filter time constant T1 |  |  |
| T2 | LREAL | 0.0 to 1.0E12 | DIR | Velocity filter time constant T2 |  |  |  |
| VelocityTolerance. |  | TO_Struct_ExtrapolationVelocityTolerance |  |  |  |  |  |
|  | Range | LREAL | 0.0 to 1.0E12 | DIR | Tolerance band width for velocity |  |  |
| Hysteresis. |  | TO_Struct_ExtrapolationHysteresis |  |  |  |  |  |
|  | Value | LREAL | 0.0 to 1.0E12 | DIR | Hysteresis of the extrapolated actual position value |  |  |

#### "LoadGear" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.LoadGear.<tag name>" contains the configuration of the load gear.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| LoadGear. |  | TO_Struct_LoadGear |  |  |  |
|  | Numerator | UDINT | 1 to 4294967295 | RES | Load gear counter |
| Denominator | UDINT | 1 to 4294967295 | RES | Load gear denominator |  |

#### "Properties" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Properties.<tag name>" contains the configuration of the type of axis or motion.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Properties. |  | TO_Struct_Properties |  |  |  |  |
|  | MotionType | DINT | 0, 1 | RON | Display of axis type or motion type |  |
| 0 | Linear axis or motion |  |  |  |  |  |
| 1 | Rotary axis or motion |  |  |  |  |  |

#### "Units" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Units.<tag name>" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_Struct_Units / TO_Struct_ExternalEncoder_Units |  |  |  |  |
|  | LengthUnit | UDINT | - | RON | Unit for position |  |
| 1010 | m |  |  |  |  |  |
| 1013 | mm |  |  |  |  |  |
| 1536 | mm<sup>1)</sup> |  |  |  |  |  |
| 1011 | km |  |  |  |  |  |
| 1014 | µm |  |  |  |  |  |
| 1015 | nm |  |  |  |  |  |
| 1019 | in |  |  |  |  |  |
| 1018 | ft |  |  |  |  |  |
| 1021 | mi |  |  |  |  |  |
| 1004 | rad |  |  |  |  |  |
| 1005 | ° |  |  |  |  |  |
| 1537 | °<sup>1)</sup> |  |  |  |  |  |
| VelocityUnit | UDINT | - | RON | Unit for velocity |  |  |
| 1521 | °/s |  |  |  |  |  |
| 1539 | °/s<sup>1)</sup> |  |  |  |  |  |
| 1522 | °/min |  |  |  |  |  |
| 1086 | rad/s |  |  |  |  |  |
| 1523 | rad/min |  |  |  |  |  |
| 1062 | mm/s |  |  |  |  |  |
| 1538 | mm/s<sup>1)</sup> |  |  |  |  |  |
| 1061 | m/s |  |  |  |  |  |
| 1524 | mm/min |  |  |  |  |  |
| 1525 | m/min |  |  |  |  |  |
| 1526 | mm/h |  |  |  |  |  |
| 1063 | m/h |  |  |  |  |  |
| 1527 | km/min |  |  |  |  |  |
| 1064 | km/h |  |  |  |  |  |
| 1066 | in/s |  |  |  |  |  |
| 1069 | in/min |  |  |  |  |  |
| 1067 | ft/s |  |  |  |  |  |
| 1070 | ft/min |  |  |  |  |  |
| 1075 | mi/h |  |  |  |  |  |
| TimeUnit | UDINT | - | RON | Unit for time |  |  |
| 1054 | s |  |  |  |  |  |
| <sup>1)</sup> Position values with higher resolution or six decimal places |  |  |  |  |  |  |

#### "Mechanics" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Mechanics.<tag name>" contains the configuration of the mechanics.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| Mechanics. |  | TO_Struct_Mechanics |  |  |  |
|  | LeadScrew | LREAL | 1.0E-12 to 1.0E12 | RES | Leadscrew pitch |

#### "Modulo" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Modulo.<tag name>" contains the configuration of the modulo function.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Modulo. |  | TO_Struct_Modulo |  |  |  |  |
|  | Enable | BOOL | - | RES | FALSE | Modulo conversion disabled |
| TRUE | Modulo conversion enabled |  |  |  |  |  |
| Length | LREAL | 0.001 to 1.0E12 | RES | Modulo length  When modulo conversion is enabled, a check is made for modulo length > 0.0 |  |  |
| StartValue | LREAL | -1.0E12 to 1.0E12 | RES | Modulo start value |  |  |

#### "Homing" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.Homing.<tag name>" contains the configuration for homing the TO.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Homing. |  | TO_Struct_Homing / TO_Struct_ExternalEncoder_Homing |  |  |  |
|  | HomePosition | LREAL | -1.0E12 to 1.0E12 | CAL | Home position |

#### Variable "StandstillSignal" (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.StandstillSignal.<tag name>" contains the configuration of the standstill signal.

If the actual velocity value is below the velocity threshold, and does not exceed it during the minimum dwell time, then the standstill signal "<TO>.StatusWord.X7 (Standstill)" is set.

##### Variables

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StandstillSignal. |  | TO_Struct_StandstillSignal |  |  | Configuration for the standstill signal |
|  | VelocityThreshold | LREAL | 0.0 to 1.0E12 | DIR | Velocity threshold  If velocity is below this threshold, the minimum dwell time begins. |
| MinDwellTime | LREAL | 0.0 to 1.0E12 | DIR | Minimum dwell time |  |

#### "StatusProvidedLeadingValue" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusProvidedLeadingValue.<tag name>" contains the provided leading value with leading value delay of the cross-PLC synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusProvidedLeadingValue. |  |  | TO_Struct_StatusProvidedLeadingValue |  |  | Provided leading value |
|  | DelayedLeadingValue |  | TO_Struct_ProvidedLeadingValue |  |  | Leading value with leading value delay |
|  | Position | LREAL | -1.0E12 to 1.0E12 | RON | Position |  |
| Velocity | LREAL | -1.0E12 to 1.0E12 | RON | Velocity |  |  |
| Acceleration | LREAL | -1.0E12 to 1.0E12 | RON | Acceleration |  |  |

---

**See also**

[Evaluating the technology data block (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluating-the-technology-data-block-s7-1500-s7-1500t)

#### "StatusSensor" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusSensor.<tag name>" indicates the status of the measuring system.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusSensor. |  | TO_Struct_StatusSensor |  |  |  |  |
|  | State | DINT | 0 to 2 | RON | Status of the actual encoder value |  |
| 0 | "NOT_VALID"  Invalid |  |  |  |  |  |
| 1 | "WAITING_FOR_VALID"  Waiting for "Valid" status |  |  |  |  |  |
| 2 | "VALID"  Valid |  |  |  |  |  |
| CommunicationOK | BOOL | - | RON | Cyclic BUS communication between controller and encoder |  |  |
| FALSE | Not established |  |  |  |  |  |
| TRUE | Established |  |  |  |  |  |
| Error | BOOL | - | RON | FALSE | No error in the measuring system |  |
| TRUE | Error in the measuring system. |  |  |  |  |  |
| AbsEncoderOffset | LREAL | - | RON | Home position offset for value of an absolute value encoder.  The value will be retentively stored in the CPU. |  |  |
| Control | BOOL | - | RON | FALSE | Encoder is not active |  |
| TRUE | Encoder is active |  |  |  |  |  |
| Position | LREAL | - | RON | Encoder position |  |  |
| Velocity | LREAL | - | RON | Encoder velocity |  |  |
| AdaptionState | DINT | - | RON | Status of automatic data transfer of encoder parameters |  |  |
| 0 | "NOT_ADAPTED"  Data not transferred |  |  |  |  |  |
| 1 | "IN_ADAPTION"  Data transfer in progress |  |  |  |  |  |
| 2 | "ADAPTED"  Data transfer complete |  |  |  |  |  |
| 3 | "NOT_APPLICABLE"  Data transfer not selected, not possible |  |  |  |  |  |
| 4 | "ADAPTION_ERROR"  Error during data transfer |  |  |  |  |  |
| ModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles |  |  |
| Adjusted | DINT | 0 to 1 | RON | Homing status of the encoder |  |  |
| 0 | Encoder not homed |  |  |  |  |  |
| 1 | Encoder homed with one of the following homing types:  - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment |  |  |  |  |  |

#### "StatusExtrapolation" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusExtrapolation.<tag name>" indicates the status of the actual value extrapolation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusExtrapolation. |  | TO_Struct_StatusExtrapolation |  |  |  |
|  | FilteredPosition | LREAL | -1.0E12 to 1.0E12 | RON | Position after position filter |
| FilteredVelocity | LREAL | -1.0E12 to 1.0E12 | RON | Velocity after velocity filter and tolerance band |  |
| ExtrapolatedPosition | LREAL | -1.0E12 to 1.0E12 | RON | Extrapolated position |  |
| ExtrapolatedVelocity | LREAL | -1.0E12 to 1.0E12 | RON | Extrapolated velocity |  |

#### "StatusWord" tag (external encoder) (S7-1500, S7-1500T)

The "<TO>.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 5 "HomingDone") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tag

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Enable"  Enable status  The technology object has been enabled. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | Reserved |  |
| Bit 5 | - | - | - | "HomingDone"  Homing status  The technology object is homed. |  |
| Bit 6 | - | - | - | "Done"  No motion job is in progress and the axis control panel is deactivated. |  |
| Bit 7 | - | - | - | "Standstill" standstill signal The external encoder is at a standstill. |  |
| Bit 8 …  Bit 10 | - | - | - | Reserved |  |
| Bit 11 | - | - | - | "HomingCommand"  An "MC_Home" job is being processed. |  |
| Bit 12... Bit 31 | - | - | - | Reserved |  |

#### "ErrorWord" tag (external encoder) (S7-1500, S7-1500T)

The "<TO>.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | Reserved |  |
| Bit 5 | - | - | - | "SensorFault"  Error in encoder system |  |
| Bit 6 | - | - | - | Reserved |  |
| Bit 7 | - | - | - | "CommunicationFault"  Communication error  Missing or faulty communication. |  |
| Bit 8 | - | - | - | Reserved |  |
| Bit 9 | - | - | - | Reserved |  |
| Bit 10 | - | - | - | "HomingError"  Error during homing operation  The homing cannot be completed. |  |
| Bit 11 | - | - | - | Reserved |  |
| Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralError"  Error accessing a logical address |  |
| Bit 14 | - | - | - | Reserved |  |
| Bit 15 | - | - | - | "AdaptionError"  Error in automatic data transfer |  |
| Bit 16 ...  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.ErrorDetail.<tag name>" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 10 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 10 | Remove enable |  |  |  |  |  |

#### "WarningWord" tag (external encoder) (S7-1500, S7-1500T)

The "<TO>.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 13 "PeripheralWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | Reserved |  |
| Bit 5 | - | - | - | "SensorWarning"  Error in encoder system |  |
| Bit 6 | - | - | - | Reserved |  |
| Bit 7 | - | - | - | "CommunicationWarning"  Communication error  Missing or faulty communication. |  |
| Bit 8 | - | - | - | Reserved |  |
| Bit 9 | - | - | - | Reserved |  |
| Bit 10 | - | - | - | "HomingWarning"  Error during homing operation  The homing cannot be completed. |  |
| Bit 11 | - | - | - | Reserved |  |
| Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14 | - | - | - | Reserved |  |
| Bit 15 | - | - | - | "AdaptionWarning"  Error in automatic data transfer |  |
| Bit 16... Bit 31 | - | - | - | Reserved |  |

#### "InternalToTrace" tag (external encoder) (S7-1500, S7-1500T)

The tag structure "<TO>.InternalToTrace.<tag name>" contains no relevant data for you. This tag structure is internally used.

---

**See also**

[Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t-2)

## Appendix (S7-1500, S7-1500T)

This section contains information on the following topics:

- ["MC_Power" function diagrams (S7-1500, S7-1500T)](#mc_power-function-diagrams-s7-1500-s7-1500t)
- [Signal flow diagrams position control (S7-1500, S7-1500T)](#signal-flow-diagrams-position-control-s7-1500-s7-1500t)

### "MC_Power" function diagrams (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Drive connection via PROFIdrive (S7-1500, S7-1500T)](#drive-connection-via-profidrive-s7-1500-s7-1500t)
- [Analog drive connection (S7-1500, S7-1500T)](#analog-drive-connection-s7-1500-s7-1500t)

#### Drive connection via PROFIdrive (S7-1500, S7-1500T)

This section contains information on the following topics:

- [PROFIdrive State Machine (S7-1500, S7-1500T)](#profidrive-state-machine-s7-1500-s7-1500t)
- ["StopMode" = 0, 2 (S7-1500, S7-1500T)](#stopmode-0-2-s7-1500-s7-1500t)
- ["StopMode" = 1 (S7-1500, S7-1500T)](#stopmode-1-s7-1500-s7-1500t)
- ["StopMode" = 3 (S7-1500, S7-1500T)](#stopmode-3-s7-1500-s7-1500t)
- [Alarm reactions with braking ramp via the technology object (S7-1500, S7-1500T)](#alarm-reactions-with-braking-ramp-via-the-technology-object-s7-1500-s7-1500t)
- [Alarm response "Remove enable" (S7-1500, S7-1500T)](#alarm-response-remove-enable-s7-1500-s7-1500t)

##### PROFIdrive State Machine (S7-1500, S7-1500T)

An axis controls the PROFIdrive state machine in the drive through the control word in the PROFIdrive telegram. The PROFIdrive state machine shows the state of the drive.

The following table shows the states of the PROFIdrive state machine:

| Status | Description |
| --- | --- |
| S1 | Switching on inhibited (drive off, brake closed if necessary) |
| S2 | Ready for power-up |
| S3 | Switched on (drive switched on, release brake if necessary) |
| S4 | Operation (drive released, brakes released if necessary) |
| S5 | Switching off (braking with drive-defined ramp) |

###### Additional information

For more information about the PROFIdrive state machine, refer to Siemens Industry Online Support in the FAQ entry [109770665](https://support.industry.siemens.com/cs/ww/en/view/109770665).

##### "StopMode" = 0, 2 (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and disabling with "StopMode" = 0, 2

![Function chart: Enabling a technology object and disabling with "StopMode" = 0, 2](images/165573085963_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | - "StopMode" = 0   The axis is braked with the configured emergency stop deceleration. - "StopMode" = 2   The axis decelerates with the configured maximum deceleration. |

##### "StopMode" = 1 (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and disabling with "StopMode" = 1

![Function chart: Enabling a technology object and disabling with "StopMode" = 1](images/172202209291_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The braking ramp is specified using the parameter "P1135" (OFF3). |
| ② | After stopping, a pulse inhibit occurs and the status changes to "Ready to start". OFF1 and OFF2 are reset. |

##### "StopMode" = 3 (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and disabling with "StopMode" = 3

![Function chart: Enabling a technology object and disabling with "StopMode" = 3](images/165573109259_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The drive coasts down. The behavior depends on the mechanical circumstances. |

##### Alarm reactions with braking ramp via the technology object (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and occurrence of a technology alarm with braking ramp via the technology object

![Function chart: Enabling a technology object and occurrence of a technology alarm with braking ramp via the technology object](images/165573139979_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The axis is braked based on the alarm reaction:  - Stop with current dynamic values (<TO>.ErrorDetail.Reaction = 1)   The axis is braked with the deceleration in the Motion Control instruction. - Stop with maximum dynamic values (<TO>.ErrorDetail.Reaction = 2)   The axis decelerates with the configured maximum deceleration. - Stop with emergency stop ramp (<TO>.ErrorDetail.Reaction = 3)   The axis is braked with the configured emergency stop deceleration. |
| ② | The technology alarm is acknowledged. |

##### Alarm response "Remove enable"  (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and occurrence of a technology alarm with alarm reaction "Remove enable"

![Function chart: Enabling a technology object and occurrence of a technology alarm with alarm reaction "Remove enable"](images/165573145227_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The configured drive stop reaction (OFF1, OFF2, OFF3) determines the braking behavior. Configure the deceleration ramp for OFF1 and OFF3 in the drive: In this example, OFF3 is active as the stop reaction: "<TO>.Actor.RemoveEnableReaction" = 16#7 |
| ② | The technology alarm is acknowledged at time ②. |

#### Analog drive connection (S7-1500, S7-1500T)

This section contains information on the following topics:

- ["StopMode" = 0, 2 (S7-1500, S7-1500T)](#stopmode-0-2-s7-1500-s7-1500t-1)
- ["StopMode" = 1 (S7-1500, S7-1500T)](#stopmode-1-s7-1500-s7-1500t-1)
- ["StopMode" = 3 (S7-1500, S7-1500T)](#stopmode-3-s7-1500-s7-1500t-1)
- [Alarm reactions with braking ramp via the technology object (S7-1500, S7-1500T)](#alarm-reactions-with-braking-ramp-via-the-technology-object-s7-1500-s7-1500t-1)
- [Alarm response "Remove enable" (S7-1500, S7-1500T)](#alarm-response-remove-enable-s7-1500-s7-1500t-1)

##### "StopMode" = 0, 2 (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and disabling with "StopMode" = 0, 2

![Function chart: Enabling a technology object and disabling with "StopMode" = 0, 2](images/165573150475_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | - "StopMode" = 0   The axis is braked with the configured emergency stop deceleration. - "StopMode" = 2   The axis decelerates with the configured maximum deceleration. |

##### "StopMode" = 1 (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and disabling with "StopMode" = 1

![Function chart: Enabling a technology object and disabling with "StopMode" = 1](images/165573168523_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The deceleration ramp depends on the configuration in the drive. |
| ② | The behavior of the ready signal of the drive "DI DriveReadyInput" is manufacturer-specific. |

##### "StopMode" = 3 (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and disabling with "StopMode" = 3

![Function chart: Enabling a technology object and disabling with "StopMode" = 3](images/165573173771_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The drive coasts down. The behavior depends on the mechanical circumstances. |

##### Alarm reactions with braking ramp via the technology object (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and occurrence of a technology alarm with braking ramp via the technology object

![Function chart: Enabling a technology object and occurrence of a technology alarm with braking ramp via the technology object](images/165573204491_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The axis is braked based on the alarm reaction:  - Stop with current dynamic values (<TO>.ErrorDetail.Reaction = 1)   The axis is braked with the deceleration in the Motion Control instruction. - Stop with maximum dynamic values (<TO>.ErrorDetail.Reaction = 2)   The axis decelerates with the configured maximum deceleration. - Stop with emergency stop ramp (<TO>.ErrorDetail.Reaction = 3)   The axis is braked with the configured emergency stop deceleration. |
| ② | The behavior of the ready signal of the drive "DI DriveReadyInput" is manufacturer-specific. |
| ③ | The technology alarm is acknowledged at time ③. |

##### Alarm response "Remove enable"  (S7-1500, S7-1500T)

###### Function chart: Enabling a technology object and occurrence of a technology alarm with alarm reaction "Remove enable"

![Function chart: Enabling a technology object and occurrence of a technology alarm with alarm reaction "Remove enable"](images/165573209739_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The deceleration ramp depends on the configuration in the drive. |
| ② | The behavior of the ready signal of the drive "DI DriveReadyInput" is manufacturer-specific. |
| ③ | The technology alarm is acknowledged at time ③. |

### Signal flow diagrams position control (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Signal flow diagrams position control (S7-1500, S7-1500T)](#signal-flow-diagrams-position-control-s7-1500-s7-1500t-1)

#### Signal flow diagrams position control (S7-1500, S7-1500T)

##### Signal flow diagrams position control

##### Position control in the drive with DSC

![Position control in the drive with DSC](images/172438667147_DV_resource.Stream@PNG-en-US.png)

##### Position control in the CPU

![Position control in the CPU](images/172438673291_DV_resource.Stream@PNG-en-US.png)
