---
title: "Using S7-1500/S7-1500T Synchronous operation functions (S7-1500, S7-1500T)"
package: TFTOSMCSyncenUS
topics: 252
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using S7-1500/S7-1500T Synchronous operation functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Overview of functions (S7-1500, S7-1500T)](#overview-of-functions-s7-1500-s7-1500t)
- [Preparing synchronous operation (S7-1500, S7-1500T)](#preparing-synchronous-operation-s7-1500-s7-1500t)
- [Gearing (S7-1500, S7-1500T)](#gearing-s7-1500-s7-1500t)
- [Velocity synchronous operation (S7-1500T)](#velocity-synchronous-operation-s7-1500t)
- [Camming (S7-1500T)](#camming-s7-1500t)
- [Other synchronous operation functions (S7-1500T)](#other-synchronous-operation-functions-s7-1500t)
- [Cross-PLC synchronous operation (S7-1500T)](#cross-plc-synchronous-operation-s7-1500t)
- [Diagnostics (S7-1500, S7-1500T)](#diagnostics-s7-1500-s7-1500t)
- [Tags of the technology object data blocks (S7-1500, S7-1500T)](#tags-of-the-technology-object-data-blocks-s7-1500-s7-1500t)

## Overview of functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Function overview of synchronous operation (S7-1500, S7-1500T)](#function-overview-of-synchronous-operation-s7-1500-s7-1500t)
- [Synchronous axis technology object (S7-1500, S7-1500T)](#synchronous-axis-technology-object-s7-1500-s7-1500t)
- [Cam technology object (S7-1500T)](#cam-technology-object-s7-1500t)
- [Leading axis proxy technology object (S7-1500T)](#leading-axis-proxy-technology-object-s7-1500t)
- [Motion Control instructions for synchronous operation (S7-1500, S7-1500T)](#motion-control-instructions-for-synchronous-operation-s7-1500-s7-1500t)
- [Mode of operation of the instructions in synchronous operation (S7-1500, S7-1500T)](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)

### Function overview of synchronous operation (S7-1500, S7-1500T)

Synchronous operation enables a following axis to be linked to a leading axis and move synchronously with it. The synchronous operation relationship between the leading and following axes is specified by a synchronous operation function.

#### Gearing

During [gearing](#gearing-s7-1500-s7-1500t), the position of the following axis results from the position of the leading axis multiplied by the gear ratio. You specify the gear ratio as a ratio of two integers. The result is a linear synchronous operation function.

#### Gearing (S7-1500T)

The following axis can be pre-synchronized or post-synchronized via the leading value path or dynamic parameters. For this purpose, you can specify corresponding reference positions of leading and following axis that define the relation of the axes to each other.

As an alternative to the setpoint, the extrapolated actual value can be interconnected as a leading value for synchronous operation. As a result, you can use an external encoder technology object as the leading value.

In addition, the following axis can be desynchronized to a presettable stop position via the leading value path or dynamic parameters.

#### Velocity synchronous operation (S7-1500T)

During [velocity synchronous operation](#velocity-synchronous-operation-s7-1500t), the velocity of the following axis results from the velocity of the leading axis multiplied by the gear ratio, regardless of the position. You specify the gear ratio as a ratio of two integers either once or variably during synchronization.

#### Camming (S7-1500T)

During [camming](#camming-s7-1500t), the leading axis and following axis are coupled by a synchronous operation function, which you specify using a cam technology object. The cam technology object (TO_Cam, TO_Cam_10k) defines a function f(x) by means of interpolation points and/or segments. Gaps between the defined interpolation points and segments of the cam are closed by interpolation during runtime of the user program. The transmission behavior during camming is expressed by the cam curve.

#### Synchronous operation phases

A synchronous operation runs in the following phases:

- Pending synchronous operation (S7-1500T)

  The following axis waits for the starting conditions of the synchronizing motion to be fulfilled.
- Synchronization

  The following axis is synchronized to the leading value.
- Synchronous motion

  The following axis follows the position of the leading axis according to the synchronous operation function.
- Synchronous operation override

  An active synchronous operation is overridden by motion jobs, e.g. "MC_Halt" on the following axis.
- Waiting synchronization job (S7-1500T)

  The following axis waits for the starting conditions of the desynchronization motion to be fulfilled.
- Desynchronize synchronous operation (S7‑1500T)

  The following axis is desynchronized from the leading value. The following axis stops at a defined position and synchronous operation is ended.

#### Cross-PLC synchronous operation (S7-1500T)

[Cross-PLC synchronous operation](#cross-plc-synchronous-operation-s7-1500t) enables synchronous operation over multiple controllers. You can configure leading and following axes on different controllers.

The synchronous operation function, e.g. a gearing, is executed on the CPU of the following axis. The leading axis proxy technology object (TO_LeadingAxisProxy) represents the leading axis for the local synchronous operation within a CPU. The leading axis proxy evaluates the leading value telegram and provides the external leading value for the local following axes.

### Synchronous axis technology object (S7-1500, S7-1500T)

![Figure](images/165340980363_DV_resource.Stream@PNG-de-DE.png)

The synchronous axis technology object includes all functions of the positioning axis technology object.

A synchronous axis can also follow the motions of a leading axis. The synchronous operation relationship between the leading and following axes is specified by a synchronous operation function.

You can find an overview of the supported instructions of the synchronous axis technology object in the section "[Motion Control instructions for synchronous operation](#motion-control-instructions-for-synchronous-operation-s7-1500-s7-1500t)".

The figure below shows the basic principle of operation of the synchronous axis technology object:

![Figure](images/166628918923_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following non-isochronous specific configurations correspond to the positioning axis technology object:

- Basic parameters

  - [Axis or encoder type](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configure-axis-type-s7-1500-s7-1500t)
  - [Units of measure](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#units-of-measure-s7-1500-s7-1500t)
  - [Modulo setting](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#modulo-setting-s7-1500-s7-1500t)
  - [Virtual axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#virtual-axis-s7-1500-s7-1500t)
  - [Axis in simulation](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#axis-in-simulation-s7-1500-s7-1500t)
- Hardware interface

  - [Connecting PROFIdrive drives](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#connecting-profidrive-drives-s7-1500-s7-1500t)
  - [Connecting encoders via PROFIdrive](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#connecting-encoders-via-profidrive-s7-1500-s7-1500t)
  - [Transferring drive and encoder parameters automatically](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
  - [Connecting stepper motors](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#connecting-stepper-motors-s7-1500-s7-1500t)
  - [Connecting drives with analog setpoint interface](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#connecting-drives-with-analog-setpoint-interface-s7-1500-s7-1500t)
  - [Connecting force/torque data via SIEMENS additional telegram 750](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#connecting-forcetorque-data-via-siemens-additional-telegram-750-s7-1500-s7-1500t)
- Mechanics

  - [Configuring drive and encoder direction for positioning axis/synchronous axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-drive-and-encoder-direction-for-positioning-axissynchronous-axis-s7-1500-s7-1500t)
  - [Configuring the load gear](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-the-load-gear-s7-1500-s7-1500t)
  - Configuring the encoder gear
  - [Configuring the leadscrew pitch](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-the-leadscrew-pitch-s7-1500-s7-1500t)
  - [Configuring backlash compensation](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#backlash-compensation-s7-1500-s7-1500t)
- [Dynamic default values](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
- [Emergency stop](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#emergency-stop-deceleration-s7-1500-s7-1500t)
- Configuring the alarm responses
- Limits

  - [Position limits](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#traversing-range-limitation-s7-1500-s7-1500t)
  - [Dynamic limits](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#short-description-of-motion-control-and-dynamic-limits-s7-1500-s7-1500t)
  - [Torque limits](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#forcetorque-limiting-s7-1500-s7-1500t)
  - [Fixed stop detection](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#fixed-stop-detection-s7-1500-s7-1500t)
- Homing

  - [Active homing](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#active-homing-s7-1500-s7-1500t)
  - [Passive homing](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#passive-homing-s7-1500-s7-1500t)
- Position monitoring functions

  - [Position monitoring](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#positioning-monitoring-s7-1500-s7-1500t)
  - [Following error](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#following-error-monitoring-s7-1500-s7-1500t)
  - [Standstill signal](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#standstill-signal-s7-1500-s7-1500t)
- Control loop

  - [Configuring position controller in the PLC](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-position-controller-in-the-plc-s7-1500-s7-1500t)
  - [Configuring position controller for drives with DSC](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-position-controller-for-drives-with-dsc-s7-1500-s7-1500t)
  - Configuring a dynamic filter
  - [Switching the position control off and on](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#switching-the-position-control-off-and-on-s7-1500-s7-1500t)

You can find a description of the configuration parameters in the "S7-1500/S7-1500T Axis functions" documentation.

The following configurations of the synchronous axis technology object are specific to synchronous operation:

- [Leading value interconnections](#defining-leading-value-interconnection-s7-1500-s7-1500t)
- Leading value settings

  - [Configuring provision of the leading value](#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
  - [Configuring the delay time](#setting-the-delay-times-s7-1500t)
- [Actual value extrapolation](#actual-value-coupling-and-actual-value-extrapolation-s7-1500t)

You can find a description of the configuration parameters in the "S7-1500/S7-1500T synchronous operation functions" documentation.

### Cam technology object (S7-1500T)

#### Term definition

The following section discusses the "Cam technology object" in general. This refers to both the cam technology object of type "TO_Cam" and of type "TO_Cam_10k". If a specific cam technology object is meant, the type is explicitly mentioned.

#### Cam technology object

![Cam technology object](images/165342051979_DV_resource.Stream@PNG-de-DE.png)

![Cam technology object](images/165342057099_DV_resource.Stream@PNG-de-DE.png)

The cam technology object defines a transfer function y = f(x). The dependency of an output value on an input value is described in this transfer function in a unit-neutral manner. A cam technology object can be used multiple times.

You can find an overview of the supported instructions of the cam technology object in the section "[Motion Control instructions for synchronous operation](#motion-control-instructions-for-synchronous-operation-s7-1500-s7-1500t)".

You define the function y = f(x) in the [configuration of the technology object](#configuring-the-synchronous-operation-function-of-the-cam-s7-1500t) using interpolation points and/or segments. The cam technology object of the type "TO_Cam" can contain up to 1000 points. The cam technology object of the type "TO_Cam_10k" can contain up to 10 000 points. Both technology objects can contain up to 50 segments.

Ranges between interpolation points and segments are interpolated using the Motion Control instruction "[MC_InterpolateCam](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_interpolatecam-interpolate-cam-v8-s7-1500t)". During runtime of the user program, the settings can be changed/redefined via the technology data block as described in the section "[Changing the synchronous operation function of the cam online](#changing-the-synchronous-operation-function-of-the-cam-online-s7-1500t)".

![Cam technology object](images/165341823371_DV_resource.Stream@PNG-de-DE.png)

An interpolated cam can be applied as a synchronous operation function for [camming](#camming-with-mc_camin-s7-1500t).

The figure below shows the basic operating principle of the cam technology object:

![Cam technology object](images/166631468939_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following configurations are available in the cam technology object:

- [Configuring the synchronous operation function of the cam](#configuring-the-synchronous-operation-function-of-the-cam-s7-1500t)

### Leading axis proxy technology object (S7-1500T)

![Figure](images/165342170635_DV_resource.Stream@PNG-de-DE.png)

With cross-PLC synchronous operation, the leading axis proxy technology object represents the leading axis for local synchronous operation within a CPU. The leading axis proxy adjust the time of the leading value so that the following axes on the different CPUs are synchronous, and it provides the leading value for the local following axes.

You can find an overview of the supported instructions of the leading axis proxy technology object in the section "[Motion Control instructions for synchronous operation](#motion-control-instructions-for-synchronous-operation-s7-1500-s7-1500t)".

The figure below shows the basic principle of operation of the leading axis proxy technology object:

![Figure](images/166632802443_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following configurations are available in the leading axis proxy technology object:

- Basic parameters
- Leading value settings

  - [Configuring provision of the leading value](#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
  - [Configuring the tolerance time](#configuring-the-tolerance-time-s7-1500t)
  - [Configuring the delay time](#setting-the-delay-times-s7-1500t)

### Motion Control instructions for synchronous operation (S7-1500, S7-1500T)

You execute the functions of the synchronous axis, cam and leading axis proxy technology objects using Motion Control instructions in your user program or using the TIA Portal (under "Technology object > Commissioning").

The following table shows the additional Motion Control instructions for synchronous operation that are supported by the technology objects in addition to the axis functions:

| Motion Control instruction | Validity |  | Technology object |  |  |
| --- | --- | --- | --- | --- | --- |
| S7-1500 | S7-1500T | [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t) | [Cam](#cam-technology-object-s7-1500t) <sup>1)</sup> | [Leading axis proxy](#leading-axis-proxy-technology-object-s7-1500t) |  |
| "[MC_Reset](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_reset-acknowledge-alarms-restart-technology-object-v8-s7-1500-s7-1500t)"  Acknowledge alarms, restart technology objects | ✓ | ✓ | ✓ | ✓ | ✓ |
| "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)"  Start gearing | ✓ | ✓ | ✓ | - | ✓ |
| "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)"  Start gearing with specified synchronous positions | - | ✓ | ✓ | - | ✓ |
| "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)"  Start velocity synchronous operation | - | ✓ | ✓ | - | ✓ |
| "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)"  Relative shift of leading value on the following axis | - | ✓ | ✓ | - | ✓ |
| "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)"  Absolute shift of leading value on the following axis | - | ✓ | ✓ | - | ✓ |
| "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)"  Relative shift of following value on the following axis. | - | ✓ | ✓ | - | - |
| "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)"  Absolute shift of following value on the following axis. | - | ✓ | ✓ | - | - |
| "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)"  Start camming | - | ✓ | ✓ | ✓ | ✓ |
| "[MC_SynchronizedMotionSimulation](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_synchronizedmotionsimulation-simulate-synchronous-operation-v8-s7-1500t)"  Simulate synchronous operation | - | ✓ | ✓ | - | - |
| "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)"  Specify additive leading value | - | ✓ | ✓ | - | - |
| "[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)"  Desynchronize gearing | - | ✓ | ✓ | - | - |
| "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)"  Desynchronize camming | - | ✓ | ✓ | - | - |
| "[MC_InterpolateCam](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_interpolatecam-interpolate-cam-v8-s7-1500t)"  Interpolate cam | - | ✓ | - | ✓ | - |
| "[MC_GetCamLeadingValue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamleadingvalue-read-out-leading-value-of-a-cam-v8-s7-1500t)"  Read out leading value of a cam | - | ✓ | - | ✓ | - |
| "[MC_GetCamFollowingValue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamfollowingvalue-read-out-following-value-of-a-cam-v8-s7-1500t)"  Read out following value of a cam | - | ✓ | - | ✓ | - |
| "[MC_GetCamFollowingValueCyclic](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamfollowingvaluecyclic-cyclically-read-the-following-value-of-a-cam-v8-s7-1500t)"  Cyclically read out following value of a cam | - | ✓ | - | ✓ | - |
| "[MC_CopyCamData](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_copycamdata-copy-calculated-cam-elements-v8-s7-1500t)"  Copy calculated cam elements | - | ✓ | - | ✓ | - |
| <sup>1)</sup> Applies to both the cam technology object of the type "TO_Cam" and to the type "TO_Cam_10k". |  |  |  |  |  |

### Mode of operation of the instructions in synchronous operation (S7-1500, S7-1500T)

The following graphic shows the general influence of the Motion Control instructions on the following axis in synchronous operation:

![Figure](images/165342175755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Effective leading value  (<TO>.StatusSynchronizedMotion.EffectiveLeadingValue) |
| ② | Leading value of the synchronous operation function  (<TO>.StatusSynchronizedMotion.FunctionLeadingValue) |
| ③ | Following value of the synchronous operation function  (<TO>.StatusSynchronizedMotion.FunctionFollowingValue) |
| ④ | Following value after following value offset  (<TO>.StatusSynchronizedMotion.FunctionFollowingValue.Position + <TO>.StatusSynchronizedMotion.Offset) |

#### Additive leading value

With an "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)" job, you specify an [additive leading value](#brief-description-of-specifying-the-additive-leading-value-s7-1500t) cyclically in addition to the active leading value of a following axis.

#### Leading value offset

With a "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" job you shift the effective leading value on a following axis in [gearing](#leading-value-offset-during-gearing-s7-1500t) or in [camming](#leading-value-offset-during-camming-s7-1500t).

A simultaneous following value offset is not permitted. You can only start a new job for leading value offset once a previous job for following value offset has been completed.

#### Synchronous operation function

With an "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)" job, you start a [gearing](#gearing-s7-1500-s7-1500t) between a leading axis and a following axis.

With an "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)" job, you start a [camming](#camming-s7-1500t) between a leading axis and a following axis.

With an "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)" job, you start [velocity synchronous operation](#velocity-synchronous-operation-s7-1500t) between a leading axis and a following axis.

#### Following value offset

With an "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" job, you move the following value on a following axis [in gearing](#following-value-offset-on-the-following-axis-during-gearing-using-leading-value-distance-as-of-current-leading-value-position-s7-1500t) or [in camming](#following-value-offset-during-camming-s7-1500t).

A simultaneous leading value offset is not permitted. You can only start a new job for following value offset once a previous job for leading value offset has been completed.

#### Superimposed motion

With a "[MC_MoveSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movesuperimposed-position-axis-overlapping-v8-s7-1500-s7-1500t)" job, you superimpose the following value with a relative positioning motion independent of the motion of the leading axis.

With a "[MC_MotionInSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_motioninsuperimposed-specify-superimposed-motion-setpoints-v8-s7-1500t)" job, you superimpose the subsequent value by specifying values for position, velocity and acceleration for each application cycle. The superimposed motion is independent of the motion of the leading axis.

In velocity synchronous operation with "MC_GearInVelocity", a superimposed motion is only possible if the following axis is in position-controlled mode.

With a "[MC_HaltSuperimposed](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_haltsuperimposed-pause-superimposed-motions-on-axis-v8-s7-1500-s7-1500t)" job, you stop a superimposed motion independently of the base motion.

## Preparing synchronous operation (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Creating technology objects (S7-1500, S7-1500T)](#creating-technology-objects-s7-1500-s7-1500t)
- [Defining leading value interconnection (S7-1500, S7-1500T)](#defining-leading-value-interconnection-s7-1500-s7-1500t)
- [Position control in synchronous operation (S7-1500, S7-1500T)](#position-control-in-synchronous-operation-s7-1500-s7-1500t)

### Creating technology objects (S7-1500, S7-1500T)

For synchronous operation, you need technology objects for the leading and following axes. You can also create multiple following axes for one leading axis. For a camming, you also need a cam technology object (S7-1500T).

#### Requirement

- You have created an S7-1500 CPU for gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)".

  Note that an actual value coupling is only possible with an S7-1500T CPU.
- You have created an S7-1500T CPU for one of the following synchronous operation types:

  - Gearing with specified synchronous position with "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)"
  - Velocity synchronous operation with "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)"
  - Camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)"

#### Procedure

To create technology objects for synchronous operation, follow these steps:

1. As leading axis, create one of the technology objects:

   - [Positioning axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#positioning-axis-technology-object-s7-1500-s7-1500t)
   - [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t)
   - [External encoder](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#external-encoder-technology-object-s7-1500-s7-1500t) (S7‑1500T)
2. As following axis, create a synchronous axis technology object.
3. Configure the configuration parameters of the leading and following axes that are not specific for synchronous operation. You can find a description of the [configuration parameters](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#synchronous-axis-technology-object-s7-1500-s7-1500t) in the "S7-1500/S7-1500T Axis functions" documentation.
4. For a camming, create a cam technology object (S7-1500T).

### Defining leading value interconnection (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Interconnecting the leading value (S7-1500, S7-1500T)](#interconnecting-the-leading-value-s7-1500-s7-1500t)
- [Setpoint coupling (S7-1500, S7-1500T)](#setpoint-coupling-s7-1500-s7-1500t)
- [Actual value coupling and actual value extrapolation (S7-1500T)](#actual-value-coupling-and-actual-value-extrapolation-s7-1500t)
- [Tags: Actual value extrapolation (S7-1500T)](#tags-actual-value-extrapolation-s7-1500t)

#### Interconnecting the leading value (S7-1500, S7-1500T)

A leading value for a synchronous operation is provided by a leading axis or an external encoder (S7‑1500T). The leading value is specified and coupled in the user program with the call of the corresponding Motion Control instruction for synchronous operation. The leading value is switched when you call the Motion Control instruction again, specifying a different leading axis.

The following rules apply to the master value coupling:

- A leading axis or an external encoder (S7-1500T) can output the leading value for multiple following axes.
- You can interconnect a following axis with multiple leading value-capable technology objects. The following technology objects are leading value-capable:

  - [Positioning axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#positioning-axis-technology-object-s7-1500-s7-1500t)
  - [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t)
  - [External encoder](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#external-encoder-technology-object-s7-1500-s7-1500t) (S7-1500T)

  The [Leading axis proxy](#leading-axis-proxy-technology-object-s7-1500t) technology object is only relevant for a [cross-PLC synchronous operation](#cross-plc-synchronous-operation-s7-1500t) (S7-1500T).

  All interconnections required during operation must be set up during the configuration of the synchronous axis technology object.
- You can select only one leading value at a time to be coupled and evaluated during the runtime of your user program.
- The leading values and following values are coupled without conversion in the respective configured unit of measure. If, for example, a linear leading axis moves by 10 mm, a rotary following axis moves by 10° with a gear ratio of 1:1.

##### Procedure

To interconnect the required leading values of a following axis, follow these steps:

1. Open the "Technology object > Configuration > Leading value interconnections" configuration window of the synchronous axis.
2. In the "Possible leading values" table column, add all leading value-capable technology objects that you need during operation as leading values for the following axis.

   You can use the technology objects added to the table with the corresponding Motion Control instruction as leading values for the following axis. All configured leading value interconnections for the technology object are displayed in the cross-reference list of the technology object.
3. Select the coupling type of the leading value in the "Type of coupling" table column:

   - [Setpoint coupling](#setpoint-coupling-s7-1500-s7-1500t)
   - [Actual value coupling](#actual-value-coupling-and-actual-value-extrapolation-s7-1500t) (S7-1500T)

   The "Delayed" selection is only relevant for a [cross-PLC synchronous operation](#cross-plc-synchronous-operation-s7-1500t) (S7-1500T).

#### Setpoint coupling (S7-1500, S7-1500T)

With a setpoint coupling, the setpoints of the leading axis are used as the leading value for the synchronous operation.

The setpoints of the following technology objects can be connected as leading value for the synchronous operation:

- [Positioning axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#positioning-axis-technology-object-s7-1500-s7-1500t)
- [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t)
- [Leading axis proxy (S7-1500T)](#leading-axis-proxy-technology-object-s7-1500t)

---

**See also**

[Switching the position control off and on (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#switching-the-position-control-off-and-on-s7-1500-s7-1500t)

#### Actual value coupling and actual value extrapolation (S7-1500T)

For applications in which setpoint coupling is not possible, e.g. when using an external encoder, or does not make sense from a technical perspective, the S7-1500T CPU also offers actual value coupling for synchronous operation. In actual value coupling, the extrapolated actual values of a technology object are used as the leading value.

The actual values of the following technology objects can be used as a leading value for the synchronous operation:

- [Positioning axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#positioning-axis-technology-object-s7-1500-s7-1500t)
- [Synchronous axis](#synchronous-axis-technology-object-s7-1500-s7-1500t)
- [External encoder](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#external-encoder-technology-object-s7-1500-s7-1500t)

##### Actual value extrapolation of the leading value

With an actual value coupling, delay times result from the processing of the actual values. To compensate for these delay times, the actual value is extrapolated on the leading value side. This means that the leading value is extrapolated based on previously known values.

Delay times at constant velocity or at constant acceleration or deceleration can be compensated for with the extrapolation. For technical reasons, changes of acceleration or deceleration (jerk) during extrapolation always cause a displacement of the following axis relative to the leading value.

The effective extrapolation time consists of a leading axis-dependent part, a configured following axis-dependent part and, optionally, the time from the cross-PLC synchronous operation:

- **Leading axis-dependent part**

  The leading axis-dependent part is calculated automatically and displayed at the leading axis in the "<TO>.Extrapolation.LeadingAxisDependentTime" tag of the technology object. You can disable the leading axis-dependent part using the tag "<TO>.Extrapolation.Settings.SystemDefinedExtrapolation" = 0.
- **Following axis-dependent part**

  The following axis-dependent part is calculated automatically and displayed at the following axis in the "<TO>.StatusPositioning.SetpointExecutionTime" tag of the technology object. You configure the value under "Technology object > Configuration > Extended parameters > Actual value extrapolation" (<TO>.Extrapolation.FollowingAxisDependentTime).
- **Time from the cross-PLC synchronous operation**

  For cross-PLC synchronous operation, the output delay of the leading value at the locally coupled following axes is automatically taken into account. The displayed value is equal to the leading value delay and corresponds to the delay time entered at the leading axis or at the external encoder. You configure the delay time under "Technology object > Configuration > Leading value settings" (<TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime).

The extrapolated actual value is evaluated with a configurable hysteresis before it is output as the leading value. The hysteresis evaluation prevents an inversion of the leading value, which may result from extrapolation of a noisy value.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Machine damage**  If you change the extrapolation time during user program runtime in increments that are too large, damage to the machine may occur.   Change the extrapolation time only by a small amount. |  |

The following diagram shows the sequence of the actual value extrapolation.

![Actual value extrapolation of the leading value](images/165342348043_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Actual position value |
| ② | Actual velocity value |
| ③ | Position filter T1 (<TO>.Extrapolation.PositionFilter.T1) and T2 (<TO>.Extrapolation.PositionFilter.T2) |
| ④ | Velocity filters T1 (<TO>.Extrapolation.VelocityFilter.T1) and T2 (<TO>.Extrapolation.VelocityFilter.T2) |
| ⑤ | Tolerance band width for velocity (<TO>.Extrapolation.VelocityTolerance.Range) |
| ⑥ | Hysteresis value in the configured unit of length (<TO>.Extrapolation.Hysteresis.Value) |
| ⑦ | Extrapolation time component caused by the leading axis (<TO>.Extrapolation.LeadingAxisDependentTime) |
| ⑧ | Extrapolation time component caused by the following axis (<TO>.Extrapolation.FollowingAxisDependentTime) |
| ⑨ | Portion of the extrapolation time from the cross-PLC synchronous operation (<TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime) |
| ⑩ | Extrapolated leading value position |
| ⑪ | Extrapolated leading value velocity, depending on the switch position:  - Leading value velocity from the extrapolation with hysteresis ("<TO>.Extrapolation.Settings.ExtrapolatedVelocityMode" = 1) - Leading value velocity from the filtered actual velocity value ("<TO>.Extrapolation.Settings.ExtrapolatedVelocityMode" = 0) |

##### Filtering the actual values

Noisy encoder signals lead to high velocity step changes, which also affect the extrapolation. These step changes can be reduced or compensated for by using suitable filter settings. The position filter is a PT2 filter. The velocity filter is a PT2 filter with configurable tolerance bandwidth.

The actual position value is blended by the actual position filter. The actual velocity value is blended by the velocity filter and further "stabilized" by the tolerance band. The filtered position value is then extrapolated taking into account the filtered velocity value.

The leading value velocity results from the extrapolated leading value position or from the filtered velocity value without extrapolation ("<TO>.Extrapolation.Settings.ExtrapolatedVelocityMode" = 0).

Recommended settings.

Set the total of the time constants T1 and T2 of the position filter significantly smaller than the time constants T1 and T2 of the velocity filter.

##### Tolerance band

The tolerance band acts on the filtered velocity value in the interpolation cycle. The position of the tolerance band is automatically shifted in the direction of the velocity value as soon as it changes in one direction by more than half of the tolerance band from the last output value.

A new output value is simultaneously formed with the shift of the tolerance band. This corresponds to the filtered velocity value minus half the tolerance band. As long as the velocity value remains within the tolerance band, no new output value is formed.

![Tolerance band](images/165342354059_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Tolerance band |
| ![Tolerance band](images/165342858379_DV_resource.Stream@PNG-de-DE.png) | Filtered velocity before tolerance band |
| ![Tolerance band](images/165342863499_DV_resource.Stream@PNG-de-DE.png) | Filtered velocity according to tolerance band |

##### Hysteresis

The hysteresis acts on the filtered extrapolated position value in the interpolation cycle. A change of direction only takes effect when the position value changes in the direction opposite at least by the hysteresis value. The hysteresis/reversal tolerance prevents undesired reversing of the leading value on a position reversal within the tolerance band.

![Hysteresis](images/165342919819_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Hysteresis/reversal tolerance |
| ![Hysteresis](images/165342858379_DV_resource.Stream@PNG-de-DE.png) | Extrapolated position before hysteresis/reversal tolerance |
| ![Hysteresis](images/165342863499_DV_resource.Stream@PNG-de-DE.png) | Extrapolated position after hysteresis/reversal tolerance |

##### Configuring actual value extrapolation

To configure the actual value extrapolation of the leading value, follow these steps:

1. Open the "Technology object > Configuration > Extended parameters > Actual value extrapolation" configuration window of the leading axis.
2. In the "Position filter T1" and "Position filter T2" input fields, enter the time constants of the PT2 filter for smoothing the position. To activate the position filter, select the "Consider leading axis" check box.
3. In the "Hysteresis value" input field, enter a value for applying the hysteresis function to the extrapolated actual value of the position. The specification is made in the configured length unit.
4. In the "Velocity filter T1" and "Velocity filter T2" input fields, enter the time constants of the PT2 filter for smoothing the actual velocity.
5. In the "Tolerance band width" input field, enter the tolerance band width of the smoothed actual velocity. For optimized application of the tolerance band, enter the same bandwidth for the tolerance band as the width of the noise signal.
6. In the "Following axis" input field, specify the following axis proportion for the extrapolation of the leading value. The value (unchanged or offset against user-specific runtimes) from the "<TO>.StatusPositioning.SetpointExecutionTime" tag of the following axis is used as the basis.

   The leading axis-dependent extrapolation is displayed in the "Leading axis" field. The leading axis-dependent extrapolation time is calculated from the sum of the actual value acquisition time at the leading axis, (T<sub>i</sub>), the interpolator time (T<sub>Ipo</sub>) and the sum of position filters T1 and T2:

   Leading axis-dependent extrapolation time = T<sub>i</sub> + T<sub>Ipo</sub> + T1 + T2

   The time from a cross-PLC synchronous operation is displayed in the "cross-PLC" field. The time from the cross-PLC synchronous operation corresponds to the set delay time in the configuration window "Technology object > Configuration > Leading value settings".
7. To apply the leading value velocity from the differentiation of the extrapolated leading value position, select the "Activate differentiation" check box. Otherwise, the filtered actual value velocity is applied.
8. To take the leading axis-dependent extrapolation into account when calculating the effective extrapolation time, select the "Consider leading axis" check box. Otherwise, the leading axis-dependent extrapolation is not taken into account when calculating the effective extrapolation time and the position filters are deactivated.

   In the "Effective extrapolation time" field, the sum of the leading-axis time, the following axis- dependent time and the delay time of the cross-PLC synchronization is displayed.

A guideline to configuring the actual value extrapolation can be found in Siemens Industry Online Support in FAQ entry [109763337](https://support.industry.siemens.com/cs/ww/en/view/109763337).

#### Tags: Actual value extrapolation (S7-1500T)

The following technology object tags are relevant for the actual value extrapolation:

| Configuration |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime | For cross-PLC synchronous operation:  The delay time of leading value output to the local following axes |  |
| <TO>.Extrapolation.LeadingAxisDependentTime | On the leading axis:  Leading axis-dependent portion of the extrapolation time, which results from T<sub>i</sub>, T<sub>Ipo</sub>, and T<sub>Filter</sub>. |  |
| <TO>.Extrapolation.FollowingAxisDependentTime | On the leading axis:  Following-axis dependent portion of the extrapolation time  Enter the value from the "<TO>.StatusPositioning.SetpointExecutionTime" tag of the following axis (unchanged or compensated with user-specific times). |  |
| <TO>.Extrapolation.Settings.SystemDefinedExtrapolation | Effectiveness of the leading axis-dependent portion of the extrapolation time (<TO>.Extrapolation.LeadingAxisDependentTime) |  |
| 0 | Not effective |  |
| 1 | Effective |  |
| <TO>.Extrapolation.Settings.ExtrapolatedVelocityMode | 0 | "FilteredVelocity"  Leading value velocity from filtered actual velocity |
| 1 | "VelocityByDifferentiation"  Leading value velocity from differentiation of the extrapolated leading value position |  |
| <TO>.Extrapolation.PositionFilter.T1 | Position filter time constant T1 |  |
| <TO>.Extrapolation.PositionFilter.T2 | Position filter time constant T2 |  |
| <TO>.Extrapolation.VelocityFilter.T1 | Velocity filter time constant T1 |  |
| <TO>.Extrapolation.VelocityFilter.T2 | Velocity filter time constant T2 |  |
| <TO>.Extrapolation.VelocityTolerance.Range | Tolerance band width for velocity |  |
| <TO>.Extrapolation.Hysteresis.Value | Hysteresis value (in the configured unit of length) |  |

| Status indicators |  |
| --- | --- |
| Tag | Description |
| <TO>.StatusPositioning.SetpointExecutionTime | Setpoint execution time of the axis  Results from T<sub>Ipo</sub>, T<sub>vtc</sub> or 1/kv, T<sub>Send</sub> and T<sub>O</sub> of the axis. |

### Position control in synchronous operation (S7-1500, S7-1500T)

#### Gearing/camming with setpoint coupling

A following axis is set into position-controlled operation with the start of a synchronous operation job. If the leading axis is in non-position-controlled operation at the start of the synchronous operation job, the technology alarm 603 is output and the technology object is disabled (alarm response: remove enable). Synchronization is started only after the [position control has been activated](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#switching-the-position-control-off-and-on-s7-1500-s7-1500t) and the start position of the synchronization has been reached.

> **Note**
>
> **Switching the operating mode of the leading axis**
>
> If the leading axis is set to non-position-controlled operation during active synchronous operation, the setpoint of the leading axis is set to zero.
>
> The coupling gives the setpoint of the following axis a setpoint step-change. The setpoint step-change is compensated according to the constant function. The only limiting factor is the maximum speed of the drive. A following error may occur on the following axis.

#### Gearing/camming with actual value coupling (S7-1500T)

A following axis is set into position-controlled operation with the start of a synchronous operation job. If the leading axis is in non-position-controlled operation at the start of the synchronous operation and the actual values are valid, the following axis is synchronized.

If the leading axis is set to the non-position-controlled mode during active synchronization, the synchronization remains active.

#### Velocity synchronous operation (S7-1500T)

[A following axis can be operated in position-controlled or non-position-controlled mode during active synchronous operation](#defining-position-control-of-the-following-axis-s7-1500t). You specify the operating mode of the following axis at the "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)" job.

The operating mode of the leading axis is irrelevant during an active synchronous operation.

## Gearing (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Gearing with "MC_GearIn" (S7-1500, S7-1500T)](#gearing-with-mc_gearin-s7-1500-s7-1500t)
- [Gearing with "MC_GearInPos" (S7-1500T)](#gearing-with-mc_gearinpos-s7-1500t)
- [Desynchronizing gearing (S7-1500T)](#desynchronizing-gearing-s7-1500t)
- [Tags: Gearing (S7-1500, S7-1500T)](#tags-gearing-s7-1500-s7-1500t)

### Gearing with "MC_GearIn" (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Brief description of gearing (S7-1500, S7-1500T)](#brief-description-of-gearing-s7-1500-s7-1500t)
- [Defining gear ratio (S7-1500, S7-1500T)](#defining-gear-ratio-s7-1500-s7-1500t)
- [Dynamic limits of the following axis in gearing with "MC_GearIn" (S7-1500, S7-1500T)](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearin-s7-1500-s7-1500t)
- [Synchronizing following axis using dynamic parameters with "MC_GearIn" (S7-1500, S7-1500T)](#synchronizing-following-axis-using-dynamic-parameters-with-mc_gearin-s7-1500-s7-1500t)
- [Synchronous travel in gearing with "MC_GearIn" (S7-1500, S7-1500T)](#synchronous-travel-in-gearing-with-mc_gearin-s7-1500-s7-1500t)

#### Brief description of gearing (S7-1500, S7-1500T)

With the Motion Control instruction "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)", you start gearing between a leading axis and a following axis. During gearing, the position of the following axis results from the position of the leading axis multiplied by the gear ratio. You specify the gear ratio as a ratio of two integers. The result is a linear synchronous operation function.

You can start synchronous operation when the leading axis is at a standstill or when it is in motion. Synchronous travel begins after synchronization when the following axis has reached the velocity and acceleration of the leading axis, taking into account the gear ratio.

![Figure](images/165342924939_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165342858379_DV_resource.Stream@PNG-de-DE.png) | Slope of line/transmission ratio  Gear ratio = "MC_GearIn.RatioNumerator"/"MC_GearIn.RatioDenominator" |
| ![Figure](images/165342930955_DV_resource.Stream@PNG-de-DE.png) | Synchronization |
| ① | Synchronous position of leading axis starting at which the leading and following axes move synchronously |
| ② | Synchronous position of following axis starting at which the leading and following axes move synchronously |

You have the following options for gearing with "MC_GearIn":

- [Defining gear ratio](#defining-gear-ratio-s7-1500-s7-1500t)
- [Synchronizing following axis using dynamic parameters](#synchronizing-following-axis-using-dynamic-parameters-with-mc_gearin-s7-1500-s7-1500t)
- [Synchronous travel in gearing](#synchronous-travel-in-gearing-with-mc_gearin-s7-1500-s7-1500t)
- [Specify additive leading value with "MC_LeadingValueAdditive"](#specify-additive-leading-value-s7-1500t) (S7-1500T)
- [Set gearing to simulation mode with "MC_SynchronizedMotionSimulation"](#simulate-synchronous-operation-s7-1500t) (S7-1500T)
- [Desynchronize following axis with "MC_GearOut"](#desynchronizing-gearing-s7-1500t) (S7‑1500T)

Also note the [dynamic limits of the following axis in gearing with "MC_GearIn"](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearin-s7-1500-s7-1500t).

#### Defining gear ratio (S7-1500, S7-1500T)

During gearing, the position of the following axis results from the position of the leading axis multiplied by the gear ratio. You specify the gear ratio at the Motion Control instruction "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" as the relationship between two integers (numerator/denominator). The result is a linear synchronous operation function.

##### Numerator of the gear ratio

With the "RatioNumerator" parameter, you define the numerator of the gear ratio. You can define the numerator of the gear ratio as positive or negative. This yields the following behavior:

- Positive gear ratio:

  The leading and following axes move in the same direction.
- Negative gear ratio:

  The following axis moves in the opposite direction of the leading axis.

The value "0" is not permitted for the numerator of the gear ratio.

##### Denominator of the gear ratio

With the "RatioDenominator" parameter, you define the denominator of the gear ratio. Only positive values are permitted for the denominator of the gear ratio.

##### Example 1: Positive gear ratio

Leading axis and following axis are rotary axes and each has a traversing range from 0 ° to 360 ° with enabled "[Modulo](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#modulo-setting-s7-1500-s7-1500t)" setting.

Parameter inputs:

- "RatioNumerator" = 5
- "RatioDenominator" = 1

When the leading axis moves by 10 °, the following axis moves by 50 ° in the "Synchronous" status of the gearing.

##### Example 2: Negative gear ratio

Leading axis and following axis are rotary axes and each has a traversing range from 0 ° to 360 ° with enabled "Modulo" setting.

Parameter inputs:

- "RatioNumerator" = -3
- "RatioDenominator" = 1

When the leading axis moves by 10 °, the following axis moves by -30 ° in the "Synchronous" status of the gearing.

#### Dynamic limits of the following axis in gearing with "MC_GearIn" (S7-1500, S7-1500T)

If a synchronous axis is operated as a following axis in the gearing with the Motion Control instruction "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)", the following dynamic limits apply, depending on the phase of the synchronous operation:

##### Synchronization

During the synchronizing phase, dynamic limits configured for the technology object apply to the following axis.

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The SW limit switches also continue to be monitored with the configured dynamic limits of the following axis.

If the programmed dynamics of the synchronization function are greater than the maximum dynamics of the following axis, the synchronization process is only completed when the resulting final velocity is lower than the maximum velocity of the following axis.

##### Synchronous travel

During synchronous travel, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The dynamics of the following axis results from the synchronous operation function.

If the dynamic limits configured for the following axis are exceeded, this is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The SW limit switches continue to be monitored with the configured dynamic limits of the following axis.

If the following axis cannot follow the leading value, this results in a following error, which is monitored by the following error monitoring.

##### Synchronous operation override

As soon as synchronous operation [has been overridden](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-synchronous-operation-jobs-s7-1500-s7-1500t), the dynamic limits configured for the technology object apply to the following axis again. With the start of the overriding job, the active dynamics are transitioned (smoothed) to the configured dynamic limits and the specifications for the Motion Control instruction.

##### Desynchronization (S7-1500T)

You can find more information on dynamic limits during desynchronization in the section "[Dynamic limits of the following axis during desynchronization with "MC_GearOut"](#dynamic-limits-of-the-following-axis-during-desynchronization-with-mc_gearout-s7-1500t).

##### More information

You can find more information on dynamic limits in synchronous operation at Siemens Industry Online Support in the FAQ entry [109822283](https://support.industry.siemens.com/cs/ww/en/view/109822283).

#### Synchronizing following axis using dynamic parameters with "MC_GearIn" (S7-1500, S7-1500T)

During [gearing](#brief-description-of-gearing-s7-1500-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. Synchronization begins immediately after the "MC_GearIn" job starts.

##### Parameter inputs

You define the dynamic behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)":

- With the "Acceleration" parameter, you specify the acceleration of the following axis.
- With the "Deceleration" parameter, you specify the deceleration of the following axis.
- With the "Jerk" parameter, you specify the jerk of the following axis.

Observe the [dynamic limits](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearin-s7-1500-s7-1500t) of the following axis during synchronization.

##### During synchronization

Synchronization begins after the "MC_GearIn" job starts. Active motion jobs are overridden.

The synchronization duration and distance are dependent on the following parameters:

- Dynamics of the following axis at the start time of the "MC_GearIn" job
- Dynamic settings for synchronization
- Dynamics of the leading axis

The synchronization is indicated in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165343153675_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |

If the programmed dynamic response of the synchronous operation function is greater than the maximum dynamic response of the following axis, the corresponding technology alarms 502 or 503 are output at the following axis. The speed of the following axis is also limited; however, no Technology Alarm 501 is generated. The synchronization process is only completed when the resulting final velocity is lower than the maximum velocity of the following axis (<TO>.DynamicLimits.MaxVelocity).

##### After synchronization

If the following axis has reached the velocity and the acceleration of the leading axis, taking into account the gear ratio, the following axis is synchronized. [The following axis travels synchronously with the leading axis](#synchronous-travel-in-gearing-with-mc_gearin-s7-1500-s7-1500t).

#### Synchronous travel in gearing with "MC_GearIn" (S7-1500, S7-1500T)

As soon as the following axis is synchronized to a leading value, the following axis follows the dynamics of the leading axis according to the gear ratio. The transmission behavior during gearing is expressed by a linear relationship between the leading value and the following value.

The following value is calculated as follows:

Position of following axis (following value) = Synchronous position of following axis + gear ratio × (Position of leading axis - Synchronous position of leading axis)

The "Synchronous" status is indicated in the Motion Control instruction "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" with the parameter "InGear" = TRUE and in the "<TO>.StatusWord.X22 (Synchronous)" tag of the technology object.

> **Note**
>
> **Avoid homing the leading axis in synchronous operation**
>
> Avoid homing the leading axis during an active synchronous operation. Homing the leading axis during synchronous operation corresponds to a setpoint step-change on the following axis. The following axis compensates for the jump according to the synchronous operation function and limited only to the maximum speed of the drive.

### Gearing with "MC_GearInPos" (S7-1500T)

This section contains information on the following topics:

- [Brief description of gearing with specified synchronous position (S7-1500T)](#brief-description-of-gearing-with-specified-synchronous-position-s7-1500t)
- [Defining gear ratio (S7-1500T)](#defining-gear-ratio-s7-1500t)
- [Dynamic limits of the following axis in gearing with "MC_GearInPos" (S7-1500T)](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearinpos-s7-1500t)
- [Synchronizing gearing (S7-1500T)](#synchronizing-gearing-s7-1500t)
- [Synchronous travel in gearing with "MC_GearInPos" (S7-1500T)](#synchronous-travel-in-gearing-with-mc_gearinpos-s7-1500t)
- [Leading value offset during gearing (S7-1500T)](#leading-value-offset-during-gearing-s7-1500t)
- [Following value offset during gearing (S7-1500T)](#following-value-offset-during-gearing-s7-1500t)

#### Brief description of gearing with specified synchronous position (S7-1500T)

With the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)", you start gearing between a leading axis and a following axis. During gearing, the position of the following axis results from the position of the leading axis multiplied by the gear ratio depending on the synchronous positions. You specify the gear ratio as a ratio of two integers. The result is a linear synchronous operation function.

In contrast to the [gearing with "MC_GearIn"](#brief-description-of-gearing-s7-1500-s7-1500t), for gearing with "MC_GearInPos" you also specify the synchronous positions of the leading and following axes, which define the reference of the axes to one another.

You can start synchronous operation when the leading axis is at a standstill or when it is in motion. Synchronous travel begins after synchronization when the following axis has reached the velocity and acceleration of the leading axis, taking into account the gear ratio.

![Figure](images/166606051979_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165342858379_DV_resource.Stream@PNG-de-DE.png) | Slope of line/transmission ratio  Gear ratio = "MC_GearInPos.RatioNumerator"/"MC_GearInPos.RatioDenominator" |
| ![Figure](images/165342930955_DV_resource.Stream@PNG-de-DE.png) | Synchronization in advance |
| ![Figure](images/165343320331_DV_resource.Stream@PNG-de-DE.png) | Subsequent synchronization |
| ① | Leading value distance with synchronization in advance |
| ② | Leading value distance with subsequent synchronization |

You have the following options for gearing with "MC_GearInPos":

- [Defining gear ratio](#defining-gear-ratio-s7-1500t)
- [Defining direction of synchronization](#defining-direction-of-synchronization-with-mc_gearinpos-s7-1500t)
- Defining synchronous positions and type of synchronization:

  - [Synchronizing following axis in advance using dynamic parameters](#synchronizing-following-axis-in-advance-using-dynamic-parameters-with-mc_gearinpos-s7-1500t)
  - [Synchronizing following axis in advance using leading value distance](#synchronizing-following-axis-in-advance-using-leading-value-distance-with-mc_gearinpos-s7-1500t)
  - [Subsequent synchronizing of following axis using leading value distance](#subsequent-synchronizing-of-following-axis-using-leading-value-distance-with-mc_gearinpos-s7-1500t)
- [Synchronous travel in gearing](#synchronous-travel-in-gearing-with-mc_gearinpos-s7-1500t)
- [Specify additive leading value with "MC_LeadingValueAdditive"](#specify-additive-leading-value-s7-1500t)
- [Offset leading value absolute or relative with "MC_PhasingAbsolute" or "MC_PhasingRelative"](#leading-value-offset-on-the-following-axis-during-gearing-using-dynamic-parameters-s7-1500t)
- [Absolute or relative following value offset with "MC_OffsetAbsolute" or "MC_OffsetRelative"](#following-value-offset-on-the-following-axis-during-gearing-using-leading-value-distance-as-of-current-leading-value-position-s7-1500t)
- [Set gearing to simulation mode with "MC_SynchronizedMotionSimulation"](#simulate-synchronous-operation-s7-1500t)
- [Desynchronize following axis with "MC_GearOut"](#desynchronizing-gearing-s7-1500t)
- [Cancel a pending gearing with "MC_GearOut"](#only-cancel-a-pending-gearing-with-mc_gearout-s7-1500t)

Also note the [dynamic limits of the following axis in gearing with "MC_GearInPos"](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearinpos-s7-1500t).

#### Defining gear ratio (S7-1500T)

During gearing, the position of the following axis results from the position of the leading axis multiplied by the gear ratio depending on the synchronous positions. You specify the gear ratio at the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)" as the relationship between two integers (numerator/denominator). The result is a linear synchronous operation function.

##### Numerator of the gear ratio

With the "RatioNumerator" parameter, you define the numerator of the gear ratio. You can define the numerator of the gear ratio as positive or negative. This yields the following behavior:

- Positive gear ratio:

  The leading and following axes move in the same direction.
- Negative gear ratio:

  The following axis moves in the opposite direction of the leading axis.

The value "0" is not permitted for the numerator of the gear ratio.

##### Denominator of the gear ratio

With the "RatioDenominator" parameter, you define the denominator of the gear ratio. Only positive values are permitted for the denominator of the gear ratio.

##### Example 1: Positive gear ratio

Leading axis and following axis are rotary axes and each has a traversing range from 0 ° to 360 ° with enabled "[Modulo](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#modulo-setting-s7-1500-s7-1500t)" setting.

Parameter inputs:

- "RatioNumerator" = 5
- "RatioDenominator" = 1

When the leading axis moves by 10 °, the following axis moves by 50 ° in the "Synchronous" status of the gearing.

##### Example 2: Negative gear ratio

Leading axis and following axis are rotary axes and each has a traversing range from 0 ° to 360 ° with enabled "Modulo" setting.

Parameter inputs:

- "RatioNumerator" = -3
- "RatioDenominator" = 1

When the leading axis moves by 10 °, the following axis moves by -30 ° in the "Synchronous" status of the gearing.

#### Dynamic limits of the following axis in gearing with "MC_GearInPos" (S7-1500T)

If a synchronous axis is operated as a following axis in the gearing with the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)", the following dynamic limits apply, depending on the phase of the synchronous operation:

##### Pending synchronous operation

If synchronous operation is not active, the configured dynamic limits of the following axis apply. If there is already a synchronous operation active, the descriptions in the following sections apply.

##### Synchronization using dynamic parameters

During synchronization using dynamic parameters, the dynamic limits configured at the technology object apply to the following axis:

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The SW limit switches also continue to be monitored with the configured dynamic limits of the following axis.

##### Synchronization using leading value distance/synchronous travel

During synchronization via the leading value distance and during synchronous travel, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The dynamics of the following axis results from the synchronous operation function.

If the dynamic limits configured for the following axis are exceeded, this is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The SW limit switches continue to be monitored with the configured dynamic limits of the following axis.

If the following axis cannot follow the leading value, this results in a following error, which is monitored by the following error monitoring.

##### Synchronous operation override

As soon as synchronous operation [has been overridden](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-synchronous-operation-jobs-s7-1500-s7-1500t), the dynamic limits configured for the technology object apply to the following axis again. With the start of the overriding job, the active dynamics are transitioned (smoothed) to the configured dynamic limits and the specifications for the Motion Control instruction.

##### Desynchronization

You can find more information on dynamic limits during desynchronization in the section "[Dynamic limits of the following axis during desynchronization with "MC_GearOut"](#dynamic-limits-of-the-following-axis-during-desynchronization-with-mc_gearout-s7-1500t).

##### More information

You can find more information on dynamic limits in synchronous operation at Siemens Industry Online Support in the FAQ entry [109822283](https://support.industry.siemens.com/cs/ww/en/view/109822283).

#### Synchronizing gearing (S7-1500T)

This section contains information on the following topics:

- [Parameter overview for synchronizing with "MC_GearInPos" (S7-1500T)](#parameter-overview-for-synchronizing-with-mc_gearinpos-s7-1500t)
- [Defining direction of synchronization with "MC_GearInPos" (S7-1500T)](#defining-direction-of-synchronization-with-mc_gearinpos-s7-1500t)
- [Synchronizing following axis in advance using dynamic parameters with "MC_GearInPos" (S7-1500T)](#synchronizing-following-axis-in-advance-using-dynamic-parameters-with-mc_gearinpos-s7-1500t)
- [Synchronizing following axis in advance using leading value distance with "MC_GearInPos" (S7-1500T)](#synchronizing-following-axis-in-advance-using-leading-value-distance-with-mc_gearinpos-s7-1500t)
- [Subsequent synchronizing of following axis using leading value distance with "MC_GearInPos" (S7-1500T)](#subsequent-synchronizing-of-following-axis-using-leading-value-distance-with-mc_gearinpos-s7-1500t)

##### Parameter overview for synchronizing with "MC_GearInPos" (S7-1500T)

During [gearing](#brief-description-of-gearing-with-specified-synchronous-position-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With the parameter "SyncProfileReference" you define the type of synchronization:

| SyncProfileReference | Synchronization profile |
| --- | --- |
| 0 | [Synchronization in advance using dynamic parameters](#synchronizing-following-axis-in-advance-using-dynamic-parameters-with-mc_gearinpos-s7-1500t) |
| 1 | [Synchronization in advance using leading value distance](#synchronizing-following-axis-in-advance-using-leading-value-distance-with-mc_gearinpos-s7-1500t) |
| 3 | [Subsequent synchronization using leading value distance](#subsequent-synchronizing-of-following-axis-using-leading-value-distance-with-mc_gearinpos-s7-1500t) |

Depending on the synchronization profile, different parameters of the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)" are relevant:

| Parameters | SyncProfileReference |  |  |
| --- | --- | --- | --- |
| 0 | 1 | 3 |  |
| RatioNumerator | ✓ | ✓ | ✓ |
| RatioDenominator | ✓ | ✓ | ✓ |
| MasterSyncPosition | ✓ | ✓ | ✓ |
| SlaveSyncPosition | ✓ | ✓ | ✓ |
| MasterStartDistance | - | ✓ | ✓ |
| Velocity | ✓ | - | - |
| Acceleration | ✓ | - | - |
| Deceleration | ✓ | - | - |
| Jerk | ✓ | - | - |
| SyncDirection | ✓ | ✓ | ✓ |

##### Defining direction of synchronization with "MC_GearInPos" (S7-1500T)

During [gearing](#brief-description-of-gearing-with-specified-synchronous-position-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. If you have activated the "[Modulo](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#modulo-setting-s7-1500-s7-1500t)" setting for the following axis, you can define the direction of the synchronization with the "SyncDirection" parameter of the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)".

In the examples below, the transformation ratio is 1:1.

###### Positive direction

With "SyncDirection" = 1, the following axis may only travel in positive direction during synchronization. In this example, the synchronous position is 360.0.

![Positive direction](images/165343325451_DV_resource.Stream@PNG-de-DE.png)

###### Negative direction

With "SyncDirection" = 2, the following axis may only travel in negative direction during synchronization. In this example, the synchronous position is 0.0.

![Negative direction](images/165343381771_DV_resource.Stream@PNG-de-DE.png)

###### Shortest distance

With "SyncDirection" = 3, changes in direction of the following axis are permitted during synchronization. In this example, the synchronous position is 0.0.

![Shortest distance](images/165343386891_DV_resource.Stream@PNG-de-DE.png)

##### Synchronizing following axis in advance using dynamic parameters with "MC_GearInPos" (S7-1500T)

During [gearing](#brief-description-of-gearing-with-specified-synchronous-position-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. During synchronization in advance using dynamic parameters, synchronization begins in such a way that the leading and following axis are synchronous when the synchronous positions are reached.

###### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 0, you define the type of synchronization as synchronization in advance using dynamic parameters.
- With the parameters "MasterSyncPosition" and "SlaveSyncPosition", you define the synchronous positions of the leading and following axis which determine the relationship of the axes to each other. For synchronization in advance, the synchronous position is the position starting from which the leading axis and following axis travel synchronously.
- With the parameters "Velocity", "Acceleration", "Deceleration" and "Jerk" you define the dynamics for the synchronization of the following axis.

###### Until synchronization

After the start of the "MC_GearInPos" job, a motion profile for the following axis is calculated continuously. The motion profile is calculated based on the following parameters:

- Specified synchronous positions of the leading and following axis at the Motion Control instruction
- Specified dynamics of the Motion Control instruction
- Current position and dynamics of the leading and following axes
- Synchronous operation function

The calculation determines the synchronization length and thus the start position of the leading axis for the synchronization.

The start position of the leading axis is derived in the following way:

Start position = Synchronous position of leading axis - Synchronization length

The status "Waiting" is displayed at the following axis until the leading value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 2).

If the leading axis is already in its synchronous position before synchronization, the following axis must also be moved to its synchronous position, for example, with a "MC_MoveAbsolute" job. If the leading and following axes are already at their synchronous positions when the "MC_GearInPos" job is started, synchronous operation immediately has "Synchronous" status.

###### During synchronization

The following axis begins to synchronize as soon as the leading value has reached the start position. The synchronization is indicated in the Motion Control instruction "MC_GearInPos" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165343494411_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function.

If the programmed dynamic response of the synchronous operation function is greater than the maximum dynamic response of the following axis, the corresponding technology alarms 501, 502, or 503 are output at the following axis. The synchronization process is only completed when the resulting final velocity is lower than the maximum velocity of the following axis (<TO>.DynamicLimits.MaxVelocity).

###### After synchronization

The following axis is synchronized as soon as the leading axis has reached the synchronous position. [The following axis travels synchronously with the leading axis](#synchronous-travel-in-gearing-with-mc_gearinpos-s7-1500t).

##### Synchronizing following axis in advance using leading value distance with "MC_GearInPos" (S7-1500T)

During [gearing](#brief-description-of-gearing-with-specified-synchronous-position-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. During synchronization in advance using the leading value distance, synchronization begins in such a way that the leading and following axis are synchronous when the synchronous positions are reached.

###### Parameter inputs

You can define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 1, you define the type of synchronization as synchronization in advance using the leading value distance.
- With the parameters "MasterSyncPosition" and "SlaveSyncPosition", you define the synchronous positions of the leading and following axis which determine the relationship of the axes to each other. For synchronization in advance, the synchronous position is the position starting from which the leading axis and following axis travel synchronously.
- With the "MasterStartDistance" parameter, you specify the leading value distance (synchronization length).

###### Until synchronization

After the start of the "MC_GearInPos" job, a motion profile is calculated for the following axis depending on the specified leading value distance. The calculation determines the required dynamic response and thus the start position of the leading axis for the synchronization.

The start position of the leading axis is derived in the following way:

Start position = Synchronous position of leading axis - Synchronization length

The leading axis must be at least the leading value distance away from the synchronous position. The status "Waiting" is displayed at the following axis until the leading value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 2).

> **Note**
>
> **Dynamic jumps**
>
> If the following axis is in motion and the leading value is at standstill when the "MC_GearInPos" job is started, dynamic jumps can occur at the following axis as soon as the leading axis is set in motion and the following axis starts synchronizing.

If the leading and following axes are already at their synchronous positions when the "MC_GearInPos" job is started, synchronous operation immediately has "Synchronous" status.

###### During synchronization

The following axis begins to synchronize as soon as the leading value has reached the start position. The synchronization is indicated in the Motion Control instruction "MC_GearInPos" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165343500299_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" variables of the technology object. The dynamic response of the following axis is limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

###### After synchronization

The following axis is synchronized as soon as the leading axis has reached the synchronous position. [The following axis travels synchronously with the leading axis](#synchronous-travel-in-gearing-with-mc_gearinpos-s7-1500t).

##### Subsequent synchronizing of following axis using leading value distance with "MC_GearInPos" (S7-1500T)

During [gearing](#brief-description-of-gearing-with-specified-synchronous-position-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With subsequent synchronization using the leading value distance, synchronization begins as soon as the leading value has reached the synchronous position of the leading axis.

###### Parameter inputs

You can define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 3, you define the type of synchronization as subsequent synchronization using the leading value distance.
- With the parameters "MasterSyncPosition" and "SlaveSyncPosition", you define the synchronous positions of the leading and following axis which determine the relationship of the axes to each other. For subsequent synchronization, the synchronous position of the leading axis is the start position for synchronization. The synchronous position of the following axis is a theoretical position which is assigned to the synchronous position of the leading axis.
- With the "MasterStartDistance" parameter, you specify the leading value distance (synchronization length).

###### Until synchronization

After starting the "MC_GearInPos" job, a motion profile for the slave axis is calculated depending on the start position and the synchronous position of the following axis as well as on the specified leading value distance. The calculation determines the required dynamic response and the position of the leading axis as of which the leading axis and the following axis travel synchronously.

The status "Waiting" is displayed at the following axis until the leading value has reached the synchronous position of the leading axis (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 2).

> **Note**
>
> **Dynamic jumps**
>
> If the following axis is in motion and the leading value is at standstill when the "MC_GearInPos" job is started, dynamic jumps can occur at the following axis as soon as the leading axis is set in motion and the following axis starts synchronizing.

If the leading and following axes are already at their synchronous positions when the "MC_GearInPos" job is started, synchronous operation immediately has "Synchronous" status.

###### During synchronization

The following axis begins to synchronize as soon as the leading value has reached the synchronous position. The synchronization is indicated in the Motion Control instruction "MC_GearInPos" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165343506187_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" variables of the technology object. The dynamic response of the following axis is limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

###### After synchronization

The position of the leading axis from which the leading axis and following axis travel synchronously is derived in the following way:

Position axes synchronous = Synchronous position of leading axis + Synchronization length

As soon as the leading axis has reached this position, the following axis is synchronized. [The following axis travels synchronously with the leading axis](#synchronous-travel-in-gearing-with-mc_gearinpos-s7-1500t).

#### Synchronous travel in gearing with "MC_GearInPos" (S7-1500T)

As soon as the following axis is synchronized to a leading value, the following axis follows the position of the leading axis according to the synchronous positions and the gear ratio. The transmission behavior during gearing is expressed by a linear relationship between the leading value and the following value.

The following value is calculated as follows:

Position of following axis (following value) = Synchronous position of following axis + gear ratio × (Position of leading axis - Synchronous position of leading axis)

The "Synchronous" status is indicated in the Motion Control instruction "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)" with the parameter "InSync" = TRUE and in the "<TO>.StatusWord.X22 (Synchronous)" tag of the technology object.

> **Note**
>
> **Avoid homing the leading axis in synchronous operation**
>
> Avoid homing the leading axis during an active synchronous operation. Homing the leading axis during synchronous operation corresponds to a setpoint step-change on the following axis. The following axis compensates for the jump according to the synchronous operation function and limited only to the maximum speed of the drive.

#### Leading value offset during gearing (S7-1500T)

This section contains information on the following topics:

- [Leading value offset on the following axis during gearing using dynamic parameters (S7-1500T)](#leading-value-offset-on-the-following-axis-during-gearing-using-dynamic-parameters-s7-1500t)
- [Leading value offset on the following axis during gearing using leading value distance as of current leading value position (S7-1500T)](#leading-value-offset-on-the-following-axis-during-gearing-using-leading-value-distance-as-of-current-leading-value-position-s7-1500t)
- [Leading value offset on the following axis during gearing using leading value distance as of specific leading value position (S7-1500T)](#leading-value-offset-on-the-following-axis-during-gearing-using-leading-value-distance-as-of-specific-leading-value-position-s7-1500t)
- [Defining the direction of the leading value distance of a leading value offset on the following axis during gearing (S7-1500T)](#defining-the-direction-of-the-leading-value-distance-of-a-leading-value-offset-on-the-following-axis-during-gearing-s7-1500t)
- [Only cancel a pending leading value offset in the gearing (S7-1500T)](#only-cancel-a-pending-leading-value-offset-in-the-gearing-s7-1500t)

##### Leading value offset on the following axis during gearing using dynamic parameters (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". You can move the effective leading value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the leading value offset.

The leading value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

###### Parameter inputs

You define the behavior of the following axis during leading value offset with the following parameters of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 0, you specify the type of leading value offset as offset using dynamic parameters.
- With the "PhaseShift" parameter, you specify the leading value offset on the following axis.
- With the "Velocity" parameter, you specify the additive velocity of the following axis during the leading value offset.
- With the "Acceleration" parameter, you specify the additive acceleration of the following axis during the leading value offset.
- With the "Deceleration" parameter, you specify the additive deceleration of the following axis during the leading value offset.
- With the "Jerk" parameter, you specify the additive jerk of the following axis during the leading value offset.

###### During the leading value offset

The leading value offset via dynamic parameters is effective immediately, regardless of the leading value position. The leading value is offset on the following axis. The dynamic values are added to the values of the synchronous operation motion. The required travel distance of the following axis to offset the leading value is calculated by the system.

During leading value offset, the speed of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The configured velocity limit may be exceeded (<TO>.DynamicLimits.MaxVelocity).

Acceleration, deceleration, and jerk of the following axis are limited to the dynamic limits configured on the technology object:

- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The leading value offset is indicated in the Motion Control instruction with the parameter "StartPhasing" = TRUE and in the "<TO>.StatusWort.X24 (PhasingCommand)" tag of the technology object. The "AbsolutePhaseShift" or "CoveredPhaseShift" parameter shows the absolute leading value portion already shifted.

###### After the leading value offset

As soon as the following axis has offset the leading value, the leading value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.PhaseShift" tag of the technology object.

The leading value offset only has an effect in the "Synchronous" status of the gearing. When the gearing is overridden, the leading value offset is reset to zero.

##### Leading value offset on the following axis during gearing using leading value distance as of current leading value position (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". You can move the effective leading value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the leading value offset.

The leading value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

###### Parameter inputs

You define the behavior of the following axis during leading value offset with the following parameters of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 1, you specify the type of leading value offset as offset using leading value distance as of the current leading value position.
- With the "PhaseShift" parameter, you specify the leading value offset on the following axis.
- With the "PhasingDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the leading value offset.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-leading-value-offset-on-the-following-axis-during-gearing-s7-1500t).

###### During the leading value offset

After starting the jobs, the following axis begins with the leading value offset starting from the current position. Within the traversing distance of the leading axis, the following axis offsets the leading value at continuous velocity and acceleration. The required dynamics of the following axis to offset the leading value is calculated by the system. During leading value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The leading value offset is indicated in the Motion Control instruction with the parameter "StartPhasing" = TRUE and in the "<TO>.StatusWort.X24 (PhasingCommand)" tag of the technology object. The "AbsolutePhaseShift" or "CoveredPhaseShift" parameter shows the absolute leading value portion already shifted.

The leading value must not reverse during the leading value offset on the following axis. When the leading value reverses, the "MC_PhasingAbsolute" job or "MC_PhasingRelative" job is canceled with "ErrorID" = 16#808C.

###### After the leading value offset

As soon as the following axis has offset the leading value, the leading value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.PhaseShift" tag of the technology object.

The leading value offset only has an effect in the "Synchronous" status of the gearing. When the gearing is overridden, the leading value offset is reset to zero.

##### Leading value offset on the following axis during gearing using leading value distance as of specific leading value position (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". You can move the effective leading value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the leading value offset.

The leading value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

###### Parameter inputs

You define the behavior of the following axis during leading value offset with the following parameters of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 2, you specify the type of leading value offset as offset using leading value distance as of a specific leading value position.
- With the "PhaseShift" parameter, you specify the leading value offset on the following axis.
- With the "PhasingDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the leading value offset.
- With the "StartPosition" parameter, you specify the leading value position from which the leading value offset starts.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-leading-value-offset-on-the-following-axis-during-gearing-s7-1500t).

###### Until the leading value offset

After starting the job, the status "Waiting" is displayed at the following axis when the leading value is at standstill and until the leading value has reached the leading value position (<TO>.StatusWord2.X3 = TRUE (PhasingCommandWaiting)).

###### During the leading value offset

As soon as the leading value has reached the leading value position, the following axis begins to offset the leading value. Within the traversing distance of the leading axis, the following axis offsets the leading value at continuous velocity and acceleration. The required dynamics of the following axis to offset the leading value is calculated by the system. During leading value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The leading value offset is indicated in the Motion Control instruction with the parameter "StartPhasing" = TRUE and in the "<TO>.StatusWort.X24 (PhasingCommand)" tag of the technology object. The "AbsolutePhaseShift" or "CoveredPhaseShift" parameter shows the absolute leading value portion already shifted.

The leading value must not reverse during the leading value offset on the following axis. When the leading value reverses, the "MC_PhasingAbsolute" job or "MC_PhasingRelative" job is canceled with "ErrorID" = 16#808C. The waiting job is not canceled.

###### After the leading value offset

As soon as the following axis has offset the leading value, the leading value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.PhaseShift" tag of the technology object.

The leading value offset only has an effect in the "Synchronous" status of the gearing. When the gearing is overridden, the leading value offset is reset to zero.

##### Defining the direction of the leading value distance of a leading value offset on the following axis during gearing (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". With the "Direction" parameter of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)", you specify the direction of the leading value distance in relation to the direction of motion of the effective leading value.

###### Defining leading value distance in the positive direction of motion of the effective leading value

With "Direction" = 1, the following axis only offsets the leading value when the leading axis travels in the positive direction.

![Defining leading value distance in the positive direction of motion of the effective leading value](images/165343844875_DV_resource.Stream@PNG-de-DE.png)

###### Defining leading value distance in the negative direction of motion of the effective leading value

With "Direction" = 2, the following axis only offsets the leading value when the leading axis travels in the negative direction.

![Defining leading value distance in the negative direction of motion of the effective leading value](images/165343849995_DV_resource.Stream@PNG-de-DE.png)

###### Defining leading value distance in the current direction of motion of the effective leading value

With "Direction" = 3, the following axis offsets the leading value regardless of the direction in which the leading axis is currently traveling.

##### Only cancel a pending leading value offset in the gearing (S7-1500T)

With an "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" job with "ProfileReference" = 5, you cancel a pending "MC_PhasingAbsolute" or "MC_PhasingRelative" job. Canceling a waiting job has no effect on an active leading value offset.

#### Following value offset during gearing (S7-1500T)

This section contains information on the following topics:

- [Following value offset on the following axis during gearing using leading value distance as of current leading value position (S7-1500T)](#following-value-offset-on-the-following-axis-during-gearing-using-leading-value-distance-as-of-current-leading-value-position-s7-1500t)
- [Following value offset on the following axis during gearing using leading value distance as of specific leading value position (S7-1500T)](#following-value-offset-on-the-following-axis-during-gearing-using-leading-value-distance-as-of-specific-leading-value-position-s7-1500t)
- [Defining the direction of the leading value distance of a following value offset on the following axis during gearing (S7-1500T)](#defining-the-direction-of-the-leading-value-distance-of-a-following-value-offset-on-the-following-axis-during-gearing-s7-1500t)
- [Only cancel a pending following value offset in the gearing (S7-1500T)](#only-cancel-a-pending-following-value-offset-in-the-gearing-s7-1500t)

##### Following value offset on the following axis during gearing using leading value distance as of current leading value position (S7-1500T)

With a following value offset, you offset the following value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". You can move the following value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the following value offset.

The following value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

###### Parameter inputs

You define the behavior of the following axis during following value offset with the following parameters of the Motion Control instruction "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 1, you specify the type of following value offset as offset using leading value distance as of the current leading value position.
- With the "Offset" parameter, you specify the following value offset on the following axis.
- With the "OffsetDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the following value offset.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-following-value-offset-on-the-following-axis-during-gearing-s7-1500t).

###### During the following value offset

After starting the job, the following axis begins with the following value offset starting from the current position. Within the traversing distance of the leading axis, the following axis offsets the following value at continuous velocity and acceleration. The required dynamics of the following axis for the following value offset is calculated by the system. During following value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The following value offset is indicated in the Motion Control instruction with the parameter "StartOffset" = TRUE and in the "<TO>.StatusWort2.X4 (OffsetCommand)" tag of the technology object. The "AbsoluteOffset" or "CoveredOffset" parameter shows the absolute following value portion already shifted.

The leading value must not reverse during the following value offset on the following axis. When the leading value reverses, the "MC_OffsetAbsolute" job or "MC_OffsetRelative" job is canceled with "ErrorID" = 16#808C.

###### After the following value offset

As soon as the following axis has offset the following value, the following value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.Offset" tag of the technology object.

The following value offset only has an effect in the "Synchronous" status of the gearing. When the gearing is overridden, the following value offset is reset to zero.

##### Following value offset on the following axis during gearing using leading value distance as of specific leading value position (S7-1500T)

With a following value offset, you offset the following value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". You can move the following value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the following value offset.

The following value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

###### Parameter inputs

You define the behavior of the following axis during following value offset with the following parameters of the Motion Control instruction "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 2, you specify the type of following value offset as offset using leading value distance as of a specific leading value position.
- With the "Offset" parameter, you specify the following value offset on the following axis.
- With the "OffsetDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the following value offset.
- With the "StartPosition" parameter, you specify the leading value position from which the following value offset starts.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-following-value-offset-on-the-following-axis-during-gearing-s7-1500t).

###### Until the following value offset

After starting the job, the status "Waiting" is displayed at the following axis when the leading value is at standstill and until the leading value has reached the leading value position (<TO>.StatusWord2.X5 = TRUE (OffsetCommandWaiting)).

###### During the following value offset

As soon as the leading value has reached the leading value position, the following axis begins to offset the following value. Within the traversing distance of the leading axis, the following axis offsets the following value at continuous velocity and acceleration. The required dynamics of the following axis for the following value offset is calculated by the system. During following value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The following value offset is indicated in the Motion Control instruction with the parameter "StartOffset" = TRUE and in the "<TO>.StatusWort2.X4 (OffsetCommand)" tag of the technology object. The "AbsoluteOffset" or "CoveredOffset" parameter shows the absolute following value portion already shifted.

The leading value must not reverse during the following value offset on the following axis. When the leading value reverses, the "MC_OffsetAbsolute" job or "MC_OffsetRelative" job is canceled with "ErrorID" = 16#808C. The waiting job is not canceled.

###### After the following value offset

As soon as the following axis has offset the following value, the following value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.Offset" tag of the technology object.

The following value offset only has an effect in the "Synchronous" status of the gearing. When the gearing is overridden, the following value offset is reset to zero.

##### Defining the direction of the leading value distance of a following value offset on the following axis during gearing (S7-1500T)

With a following value offset, you offset the following value on the following axis during gearing with "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" or "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)". With the "Direction" parameter of the Motion Control instruction "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)", you specify the direction of the leading value distance in relation to the direction of motion of the effective leading value.

###### Defining leading value distance in the positive direction of motion of the effective leading value

With "Direction" = 1, the following axis only offsets the following value when the leading axis travels in the positive direction.

![Defining leading value distance in the positive direction of motion of the effective leading value](images/165344021515_DV_resource.Stream@PNG-de-DE.png)

###### Defining leading value distance in the negative direction of motion of the effective leading value

With "Direction" = 2, the following axis only offsets the following value when the leading axis travels in the negative direction.

![Defining leading value distance in the negative direction of motion of the effective leading value](images/165344026635_DV_resource.Stream@PNG-de-DE.png)

###### Defining leading value distance in the current direction of motion of the effective leading value

With "Direction" = 3, the following axis offsets the following value regardless of the direction in which the leading axis is currently traveling.

##### Only cancel a pending following value offset in the gearing (S7-1500T)

With an "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" job with "ProfileReference" = 5, you cancel a pending "MC_OffsetAbsolute" or "MC_OffsetRelative" job. Canceling a pending job has no effect on an active following value offset.

### Desynchronizing gearing (S7-1500T)

This section contains information on the following topics:

- [Desynchronizing following axis using dynamic parameters with "MC_GearOut" (S7-1500T)](#desynchronizing-following-axis-using-dynamic-parameters-with-mc_gearout-s7-1500t)
- [Desynchronizing following axis using leading value distance with "MC_GearOut" (S7-1500T)](#desynchronizing-following-axis-using-leading-value-distance-with-mc_gearout-s7-1500t)
- [Defining direction of desynchronization with "MC_GearOut" (S7-1500T)](#defining-direction-of-desynchronization-with-mc_gearout-s7-1500t)
- [Dynamic limits of the following axis during desynchronization with "MC_GearOut" (S7-1500T)](#dynamic-limits-of-the-following-axis-during-desynchronization-with-mc_gearout-s7-1500t)
- [Only cancel a pending gearing with "MC_GearOut" (S7-1500T)](#only-cancel-a-pending-gearing-with-mc_gearout-s7-1500t)

#### Desynchronizing following axis using dynamic parameters with "MC_GearOut" (S7-1500T)

Desynchronization ends the synchronous operation relationship between the leading and following axis and gearing is ended. For desynchronization using dynamic parameters, desynchronization begins in such a way that the following axis comes to a standstill when the stop position is reached.

With the Motion Control instruction "MC_GearOut" you can desynchronize a gearing which you have started either with a "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" job or with a "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)" job.

##### Parameter inputs

You define the behavior of the following axis for desynchronization with the following parameters of the Motion Control instruction "[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 0, you specify the type of desynchronization as desynchronization using dynamic parameters.
- With the parameter "SlavePosition", you specify the stop positions of the following axis. The stop position of the following axis is the position at which the following axis comes to a standstill and the desynchronization is completed.
- With the "Deceleration" parameter, you specify the deceleration of the following axis.
- With the "Jerk" parameter, you specify the jerk of the following axis.
- With the "SyncOutDirection" parameter, you specify the [direction of the desynchronization](#defining-direction-of-desynchronization-with-mc_gearout-s7-1500t).

##### Until desynchronization

After the start of the "MC_GearOut" job, a motion profile for the following axis is calculated continuously. The motion profile is calculated based on the following parameters:

- Specified stop position of the following axis in the Motion Control instruction
- Specified dynamics of the Motion Control instruction
- Current position and dynamics of the leading and following axes
- Synchronous operation function
- Superimposed motion of the following axis
- Additive leading value of the following axis

The distance of the following axis and thus the starting position of the following axis for desynchronization results from the calculation.

The start position of the following axis is derived in the following way:

Start position = stop position of the following axis - travel distance of the following axis

The status "Waiting" is displayed at the following axis until the following value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 4).

##### During desynchronization

The following axis begins to desynchronize as soon as the following value has reached the start position. Desynchronization is indicated in the Motion Control instruction "MC_GearOut" with the parameter "StartSyncOut" = TRUE and in the "<TO>.StatusWord2.X1 (DesynchronizingCommand)" tag of the technology object. The synchronous operation is no longer in the "Synchronous" status. Superimposed jobs of the following axis are canceled.

The following axis moves to the stop position with the specified dynamics, independent of the leading value. The dynamic response of the following axis is limited to the dynamic limits configured on the technology object.

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

During desynchronization, several modulo revolutions of both axes are generally possible.

##### After desynchronization

As soon as the following axis reaches the stop position, the following axis is desynchronized. The following axis is at a standstill. The status is indicated in the Motion Control instruction "MC_GearOut" with the parameter "Done" = TRUE and in the "<TO>.StatusWord.X7 (Standstill)" tag of the technology object.

#### Desynchronizing following axis using leading value distance with "MC_GearOut" (S7-1500T)

Desynchronization ends the synchronous operation relationship between the leading and following axis and gearing is ended. For desynchronization using the leading value distance, desynchronization begins in such a way that the following axis comes to a standstill when the stop position is reached.

With the Motion Control instruction "MC_GearOut" you can desynchronize a gearing which you have started either with a "[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)" job or with a "[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)" job.

##### Parameter inputs

You define the behavior of the following axis for desynchronization with the following parameters of the Motion Control instruction "[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 1, you specify the type of desynchronization as desynchronization using the leading value distance.
- With the parameter "SlavePosition", you specify the stop positions of the following axis. The stop position of the following axis is the position at which the following axis comes to a standstill and the desynchronization is completed.
- With the "MasterStopDistance" parameter, you define the leading value distance (desynchronization length).
- With the "SyncOutDirection" parameter, you specify the [direction of the desynchronization](#defining-direction-of-desynchronization-with-mc_gearout-s7-1500t).

##### Until desynchronization

After the start of the "MC_GearOut" job, a motion profile is calculated depending on the specified leading value distance. The calculation determines the required dynamics and thus the start position of the leading axis for the desynchronization.

The start position of the leading axis is derived in the following way:

Start position = leading value position when the stop position of the following axis is reached - leading value distance

The status "Waiting" is displayed at the following axis until the leading value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 4).

##### During desynchronization

The following axis begins to desynchronize as soon as the leading value has reached the start position. Desynchronization is indicated in the Motion Control instruction "MC_GearOut" with the parameter "StartSyncOut" = TRUE and in the "<TO>.StatusWord2.X1 (DesynchronizingCommand)" tag of the technology object. The synchronous operation is no longer in the "Synchronous" status. Superimposed jobs of the following axis are canceled.

The following axis travels to the stop position depending on the leading value distance The dynamics of the following axis during desynchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. The dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

Changes in the dynamics of the leading axis during desynchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object.

The leading value must not reverse during desynchronization. During desynchronization, several modulo revolutions of both axes are generally possible.

![During desynchronization](images/165344031755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when desynchronization starts |
| ② | Time when desynchronization is complete |

If the leading axis stops during desynchronization, high dynamic values can occur at the following axis as soon as the leading axis starts moving again and the following axis continues moving to the specified stop position. To avoid these high dynamic values at the following axis, use desynchronization via dynamic parameters ("SyncProfileReference" = 0).

##### After desynchronization

As soon as the following axis reaches the stop position, the following axis is desynchronized. The following axis is at a standstill. The status is indicated in the Motion Control instruction "MC_GearOut" with the parameter "Done" = TRUE and in the "<TO>.StatusWord.X7 (Standstill)" tag of the technology object.

#### Defining direction of desynchronization with "MC_GearOut" (S7-1500T)

Desynchronization ends the synchronous operation relationship between the leading and following axis and gearing is ended. You can specify the desynchronization direction with the "SyncOutDirection" parameter of the Motion Control instruction "[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)".

##### Desynchronizing the following axis in positive traversing direction

With "SyncOutDirection" = 1, the following axis is only desynchronized when the following axis moves in the positive direction.

![Desynchronizing the following axis in positive traversing direction](images/165344050443_DV_resource.Stream@PNG-de-DE.png)

##### Desynchronizing the following axis in negative traversing direction

With "SyncOutDirection" = 2, the following axis is only desynchronized when the following axis moves in the negative direction.

![Desynchronizing the following axis in negative traversing direction](images/165344055563_DV_resource.Stream@PNG-de-DE.png)

##### Desynchronizing the following axis in the current traversing direction

With "SyncOutDirection" = 3, the following axis is desynchronized in the direction in which the following axis is currently moving.

#### Dynamic limits of the following axis during desynchronization with "MC_GearOut" (S7-1500T)

If a synchronous axis is desynchronized as a following axis in the gearing with the Motion Control instruction "[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)", the following dynamic limits apply, depending on the type of the synchronous operation:

##### Desynchronization via dynamic parameters

During synchronization using dynamic parameters, the dynamic limits configured at the technology object apply to the following axis.

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The SW limit switches also continue to be monitored with the configured dynamic limits of the following axis.

##### Desynchronization using leading value distance

When desynchronizing via the leading value distance, the dynamic response of the following axis are only limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The dynamics of the following axis results from the synchronous operation function.

If the dynamic limits configured for the following axis are exceeded, this is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The SW limit switches continue to be monitored with the configured dynamic limits of the following axis.

If the following axis cannot follow the leading value, this results in a following error, which is monitored by the following error monitoring.

---

**See also**

[Dynamic limits of the following axis in gearing with "MC_GearIn" (S7-1500, S7-1500T)](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearin-s7-1500-s7-1500t)
  
[Dynamic limits of the following axis in gearing with "MC_GearInPos" (S7-1500T)](#dynamic-limits-of-the-following-axis-in-gearing-with-mc_gearinpos-s7-1500t)

#### Only cancel a pending gearing with "MC_GearOut" (S7-1500T)

With a "[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)" job with "SyncProfileReference" = 5, you cancel a pending gearing. Canceling a pending gearing has no influence on an active gearing.

### Tags: Gearing (S7-1500, S7-1500T)

The following technology object tags are relevant for gearing:

| Status indicators |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.StatusSynchronizedMotion.FunctionState | Indication of which synchronous operation function is active |  |
| 0 | No synchronous operation active |  |
| 1 | Gearing ("[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)") |  |
| 2 | Gearing with specified synchronous positions ("[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)") |  |
| 3 | Camming ("[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)") |  |
| 4 | Desynchronization of gearing ("[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)") |  |
| 5 | Desynchronization of camming ("[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)") |  |
| 6 | Velocity gearing ("[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)") |  |
| <TO>.StatusSynchronizedMotion.WaitingFunctionState | Indication of which synchronous operation function is waiting |  |
| 0 | No synchronous operation waiting |  |
| 1 | Reserved |  |
| 2 | Gearing with specified synchronous positions waiting ("MC_GearInPos") |  |
| 3 | Camming waiting ("MC_CamIn") |  |
| 4 | Desynchronization of gearing waiting ("MC_GearOut") |  |
| 5 | Desynchronization of camming waiting ("MC_CamOut") |  |
| <TO>.StatusSynchronizedMotion.ActualMaster | When a synchronous operation job is started, the number of the technology data block of the currently used leading axis is displayed. |  |
| 0 | Synchronous operation inactive |  |
| <TO>.Position | Setpoints of the axis |  |
| <TO>.Velocity |  |  |
| <TO>.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Position | Effective leading value including an additive leading value with an "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Velocity |  |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.PhaseShift | Current absolute leading value offset with an "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.FunctionLeadingValue.Position | Leading value of the synchronous operation function after a leading value offset with an "MC_PhasingAbsolute" job or "MC_PhasingRelative" job including an additive leading value with a "MC_LeadingValueAdditive" job |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Position | Following value of the synchronous operation function before a following value offset with an "MC_OffsetAbsolute" job or "MC_OffsetRelative" job |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Velocity |  |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.Offset | Current absolute following value offset with an "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X0 (MaxVelocityExceeded) | Set to the value "TRUE" when the maximum velocity configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X1 (MaxAccelerationExceeded) | Set to the value "TRUE" when the maximum acceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X2 (MaxDecelerationExceeded) | Set to the value "TRUE" when the maximum deceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusWord.X21 (Synchronizing) | Set to the value "TRUE" when the synchronous axis synchronizes to a leading value. |  |
| <TO>.StatusWord.X22 (Synchronous) | Set to the value "TRUE" when the synchronous axis is synchronized and moves synchronously to the leading axis. |  |
| <TO>.StatusWord2.X1 (DesynchronizingCommand) | Set to the value "TRUE" when the synchronous axis desynchronizes. |  |
| <TO>.StatusWord.X24 (PhasingCommand) | Is set to the value "TRUE" if a job for leading value offset is active ("MC_PhasingAbsolute", "MC_PhasingRelative"). |  |
| <TO>.StatusWord2.X3 (PhasingCommandWaiting) | Is set to the value "TRUE" if a job for leading value offset is pending ("MC_PhasingAbsolute", "MC_PhasingRelative"). |  |
| <TO>.StatusWord2.X4 (OffsetCommand) | Is set to the value "TRUE" if a job for following value offset is active ("MC_OffsetAbsolute", "MC_OffsetRelative"). |  |
| <TO>.StatusWord2.X5 (OffsetCommandWaiting) | Is set to the value "TRUE" if a job for following value offset is waiting ("MC_OffsetAbsolute", "MC_OffsetRelative"). |  |
| <TO>.ErrorWord.X14 (SynchronousError) | Error during synchronous operation  The leading axis specified in the motion control instruction was not configured as a possible leading axis. |  |

## Velocity synchronous operation (S7-1500T)

This section contains information on the following topics:

- [Brief description velocity synchronous operation (S7-1500T)](#brief-description-velocity-synchronous-operation-s7-1500t)
- [Defining gear ratio (S7-1500T)](#defining-gear-ratio-s7-1500t-1)
- [Specify gear ratio once or dynamically (S7-1500T)](#specify-gear-ratio-once-or-dynamically-s7-1500t)
- [Defining position control of the following axis (S7-1500T)](#defining-position-control-of-the-following-axis-s7-1500t)
- [Dynamic limits of the following axis in velocity synchronous operation (S7-1500T)](#dynamic-limits-of-the-following-axis-in-velocity-synchronous-operation-s7-1500t)
- [Synchronizing following axis using dynamic parameters with "MC_GearInVelocity" (S7-1500T)](#synchronizing-following-axis-using-dynamic-parameters-with-mc_gearinvelocity-s7-1500t)
- [Synchronous travel in velocity synchronous operation with "MC_GearInVelocity" (S7-1500T)](#synchronous-travel-in-velocity-synchronous-operation-with-mc_gearinvelocity-s7-1500t)
- [Tags: Velocity synchronous operation (S7-1500T)](#tags-velocity-synchronous-operation-s7-1500t)

### Brief description velocity synchronous operation (S7-1500T)

With the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)" you start a velocity synchronous operation between a leading axis and a following axis. During velocity synchronous operation , the velocity of the following axis results from the velocity of the leading axis multiplied by the gear ratio, regardless of the position. You specify the gear ratio as a ratio of two integers either once or variably during synchronization. This results in a linear transformation ratio.

You can start synchronous operation when the leading axis is at a standstill or when it is in motion. Synchronous travel begins after synchronization when the following axis has reached the velocity and acceleration of the leading axis, taking into account the gear ratio.

![Figure](images/165344316683_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165342858379_DV_resource.Stream@PNG-de-DE.png) | Slope of line/transmission ratio  Gear ratio = "MC_GearInVelocity.RatioNumerator"/"MC_GearInVelocity.RatioDenominator" |

For velocity synchronous operation with "MC_GearInVelocity", you have the following options:

- [Defining gear ratio](#defining-gear-ratio-s7-1500t-1)
- [Specify gear ratio once or dynamically](#specify-gear-ratio-once-or-dynamically-s7-1500t)
- [Defining position control of the following axis](#defining-position-control-of-the-following-axis-s7-1500t)
- [Synchronize following axis using dynamic parameters](#synchronizing-following-axis-using-dynamic-parameters-with-mc_gearinvelocity-s7-1500t)
- [Synchronous travel in velocity synchronous operation](#synchronous-travel-in-velocity-synchronous-operation-with-mc_gearinvelocity-s7-1500t)
- [Specify additive leading value with "MC_LeadingValueAdditive"](#specify-additive-leading-value-s7-1500t)
- [Set velocity synchronous operation with "MC_SynchronizedMotionSimulation" in simulation](#simulate-synchronous-operation-s7-1500t)

Also note the [Dynamic limits of the following axis in velocity synchronous operation](#dynamic-limits-of-the-following-axis-in-velocity-synchronous-operation-s7-1500t).

### Defining gear ratio (S7-1500T)

During velocity synchronous operation , the velocity of the following axis results from the velocity of the leading axis multiplied by the gear ratio, regardless of the position. You specify the gear ratio at the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)" as the relationship between two integers (numerator/denominator).

#### Numerator of the gear ratio

With the "RatioNumerator" parameter, you define the numerator of the gear ratio. You can define the numerator of the gear ratio as positive or negative. This yields the following behavior:

- Positive gear ratio:

  The leading and following axes move in the same direction.
- Negative gear ratio:

  The following axis moves in the opposite direction of the leading axis.

The value "0" is not permitted for the numerator of the gear ratio.

#### Denominator of the gear ratio

With the "RatioDenominator" parameter, you define the denominator of the gear ratio. Only positive values are permitted for the denominator of the gear ratio.

#### Example 1: Positive gear ratio

Leading axis and following axis are rotary axes.

Parameter inputs:

- "RatioNumerator" = 5
- "RatioDenominator" = 1

If the leading axis moves at 100 °/s, the following axis moves at 500 °/s in the "Synchronous" status of the velocity synchronous operation .

#### Example 2: Negative gear ratio

The leading axis is a linear axis. The following axis is a rotary axis.

Parameter inputs:

- "RatioNumerator" = -3
- "RatioDenominator" = 1

If the leading axis moves at 100 mm/s, the following axis moves at -300 °/s in the "Synchronous" status of the velocity synchronous operation .

### Specify gear ratio once or dynamically (S7-1500T)

For a velocity synchronous operation , you can either preset the gear ratio once at the start of the job or change it continuously during an active synchronous operation.

Make sure that the [dynamic limits of the following axis](#dynamic-limits-of-the-following-axis-in-velocity-synchronous-operation-s7-1500t) are not exceeded by the changed gear ratios.

#### Parameter inputs

You define the behavior with the following parameters of the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)":

- You define the mode for presetting the [gear ratio](#defining-gear-ratio-s7-1500t-1) with the parameter "ContinuousUpdate" .

#### Specify gear ratio once

With "ContinuousUpdate" = FALSE, the gear ratio specified at the start time of the "MC_GearInVelocity" job is used as long as the job is active.

To change the gear ratio if necessary, you must start the job again with a rising edge of the parameter "Execute" = TRUE. The following axis then synchronizes again.

#### Specify gear ratio dynamically

With "ContinuousUpdate" = TRUE you can change the gear ratio dynamically while the "MC_GearInVelocity" job is active. Changes of the parameter values "RatioNumerator" and "RatioDenominator" are effective immediately.

That the mode for dynamic presetting of the gear ratio is active is indicated at the motion control instruction "MC_GearInVelocity" with the parameter "ContinuousUpdateActive" = TRUE.

**Recommendation**

You can specify only integer values as numerator ("RatioNumerator") and denominator ("RatioDenominator") of the gear ratio.

To achieve as continuous a change as possible in the gear ratio, multiply the numerator and denominator by a high factor. This increases the resolution of the gear ratio and reduces the quantization error.

**Example**

The gear ratio should change gradually from 1.0 to 1.1.

Parameter assignment 1:

"RatioNumerator" = 100 … 110

"RatioDenominator" = 100 … 100

Increasing the counter in steps of 1 increases the gear ratio by 0.01 each time.

Parameter assignment 2:

"RatioNumerator" = 1 000 000 … 1 100 000

"RatioDenominator" = 1 000 000 … 1 000 000

Increasing the counter in steps of 1 increases the gear ratio by 0.000001 each time.

With parameter assignment 2 you get a higher resolution and can change the gear ratio in smaller steps than with parameter assignment 1.

### Defining position control of the following axis (S7-1500T)

During a velocity synchronous operation, the following axis can be operated in position-controlled or non-position-controlled mode. You specify the operating mode of the following axis independently of the operating mode of the leading axis at the motion control instruction "MC_GearInVelocity".

#### Parameter inputs

You define the behavior of the following axis with the following parameters of the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)":

- You define the operating mode of the following axis with the parameter "PositionControlled".

#### Position-controlled mode

As soon as the "MC_GearInVelocity" job with "PositionControlled" = TRUE becomes effective, the following axis is switched to position-controlled operation. The configured position monitorings of the following axis are active.

Superimposed motion, e.g. with a "MC_MoveSuperimposed" job, and travel to a fixed stop is only possible in position-controlled operation.

#### Non-position-controlled mode

As soon as the "MC_GearInVelocity" job with "PositionControlled" = FALSE becomes effective, the following axis is switched to non-position-controlled operation. The configured position monitorings of the following axis are deactivated.

The position setpoint of the following axis is irrelevant in non-position-controlled operation. The zero position setpoint is displayed in "<TO>.Position" tag of the technology object.

### Dynamic limits of the following axis in velocity synchronous operation (S7-1500T)

If a synchronous axis is operated as a following axis in velocity synchronous operation with the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)", the following dynamic limits apply depending on the phase of the synchronous operation:

#### Synchronization

During synchronization, the velocity of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The configured velocity limit may be exceeded (<TO>.DynamicLimits.MaxVelocity).

For acceleration, deceleration, and jerk of the following axis, the dynamic limits configured on the technology object apply:

- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The SW limit switches also continue to be monitored with the configured dynamic limits of the following axis.

#### Synchronous travel

During synchronous travel, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The dynamics of the following axis results from the synchronous operation function.

If the dynamic limits configured for the following axis are exceeded, this is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The SW limit switches continue to be monitored with the configured dynamic limits of the following axis.

#### Synchronous operation override

As soon as synchronous operation [has been overridden](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-synchronous-operation-jobs-s7-1500-s7-1500t), the dynamic limits configured for the technology object apply to the following axis again. With the start of the overriding job, the active dynamics are transitioned (smoothed) to the configured dynamic limits and the specifications for the Motion Control instruction.

#### More information

You can find more information on dynamic limits in synchronous operation at Siemens Industry Online Support in the FAQ entry [109822283](https://support.industry.siemens.com/cs/ww/en/view/109822283).

### Synchronizing following axis using dynamic parameters with "MC_GearInVelocity" (S7-1500T)

During velocity synchronous operation , the synchronization establishes the relationship between the leading and following axes. Synchronization begins immediately after the "MC_GearInVelocity" job starts.

#### Parameter inputs

You define the dynamic behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)":

- With the "Acceleration" parameter, you specify the acceleration of the following axis.
- With the "Deceleration" parameter, you specify the deceleration of the following axis.
- With the "Jerk" parameter, you specify the jerk of the following axis.

Observe the [dynamic limits](#dynamic-limits-of-the-following-axis-in-velocity-synchronous-operation-s7-1500t) of the following axis during synchronization.

#### During synchronization

Synchronization begins after the "MC_GearInVelocity" job starts. Active motion jobs are overridden.

The synchronization duration and distance are dependent on the following parameters:

- Dynamics of the following axis at the start time of the "MC_GearInVelocity" job
- Dynamic settings for synchronization
- Preset gear ratio at the start time of the "MC_GearInVelocity" job
- Dynamics of the leading axis

The synchronization is indicated in the Motion Control instruction "MC_GearInVelocity" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis.

![During synchronization](images/165344322571_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |
| ② | Time when synchronization is complete |

The specified gear ratio at the start time of the "MC_GearInVelocity" job is used for the synchronization. If you use a variable gear ratio with "ContinuousUpdate" = TRUE, changes to the gear ratio are only taken into account after synchronization.

#### After synchronization

The following axis is synchronized when the following axis has reached the velocity of the leading axis, taking into account the gear ratio. [The following axis travels synchronously with the leading axis](#synchronous-travel-in-velocity-synchronous-operation-with-mc_gearinvelocity-s7-1500t).

### Synchronous travel in velocity synchronous operation  with "MC_GearInVelocity" (S7-1500T)

As soon as the following axis is synchronized, it follows the velocity of the leading axis depending on the specified gear ratio.

The following value velocity is obtained as follows:

Following value velocity = leading value velocity × gear ratio

The "Synchronous" status is indicated in the Motion Control instruction "[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)" with the parameter "InSync" = TRUE and in the "<TO>.StatusWord.X22 (Synchronous)" tag of the technology object.

If the gear ratio changes when "ContinuousUpdateActive" = TRUE, the "Synchronous" status is retained.

### Tags: Velocity synchronous operation (S7-1500T)

The following tags of the technology object are relevant for the velocity synchronous operation :

| Status indicators |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.StatusSynchronizedMotion.FunctionState | Indication of which synchronous operation function is active |  |
| 0 | No synchronous operation active |  |
| 1 | Gearing ("[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)") |  |
| 2 | Gearing with specified synchronous positions ("[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)") |  |
| 3 | Camming ("[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)") |  |
| 4 | Desynchronization of gearing ("[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)") |  |
| 5 | Desynchronization of camming ("[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)") |  |
| 6 | Velocity synchronous operation ("[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)") |  |
| <TO>.StatusSynchronizedMotion.ActualMaster | When a synchronous operation job is started, the number of the technology data block of the currently used leading axis is displayed. |  |
| 0 | Synchronous operation inactive |  |
| <TO>.Position | Setpoints of the axis |  |
| <TO>.Velocity |  |  |
| <TO>.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Position | Effective leading value including an additive leading value with an "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Velocity |  |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Position | Following value of the synchronous operation function |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Velocity |  |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X0 (MaxVelocityExceeded) | Set to the value "TRUE" when the maximum velocity configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X1 (MaxAccelerationExceeded) | Set to the value "TRUE" when the maximum acceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X2 (MaxDecelerationExceeded) | Set to the value "TRUE" when the maximum deceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusWord.X21 (Synchronizing) | Set to the value "TRUE" when the synchronous axis synchronizes to a leading value. |  |
| <TO>.StatusWord.X22 (Synchronous) | Set to the value "TRUE" when the synchronous axis is synchronized and moves synchronously to the leading axis. |  |
| <TO>.ErrorWord.X14 (SynchronousError) | Error during synchronous operation  The leading axis specified in the Motion Control instruction was not configured as a possible leading axis. |  |

## Camming (S7-1500T)

This section contains information on the following topics:

- [Camming with "MC_CamIn" (S7-1500T)](#camming-with-mc_camin-s7-1500t)
- [Configuring the synchronous operation function of the cam (S7-1500T)](#configuring-the-synchronous-operation-function-of-the-cam-s7-1500t)
- [Changing the synchronous operation function of the cam online (S7-1500T)](#changing-the-synchronous-operation-function-of-the-cam-online-s7-1500t)
- [Interpolating a cam (S7-1500T)](#interpolating-a-cam-s7-1500t)
- [Scaling and shifting cam (S7-1500T)](#scaling-and-shifting-cam-s7-1500t)
- [Defining application mode of the cam (S7-1500T)](#defining-application-mode-of-the-cam-s7-1500t)
- [Dynamic limits of the following axis in camming (S7-1500T)](#dynamic-limits-of-the-following-axis-in-camming-s7-1500t)
- [Synchronizing camming (S7-1500T)](#synchronizing-camming-s7-1500t)
- [Synchronous travel in camming with "MC_CamIn" (S7-1500T)](#synchronous-travel-in-camming-with-mc_camin-s7-1500t)
- [Reading out leading and following values during camming (S7-1500T)](#reading-out-leading-and-following-values-during-camming-s7-1500t)
- [Leading value offset during camming (S7-1500T)](#leading-value-offset-during-camming-s7-1500t)
- [Following value offset during camming (S7-1500T)](#following-value-offset-during-camming-s7-1500t)
- [Desynchronize camming (S7-1500T)](#desynchronize-camming-s7-1500t)
- [Tags: Camming (S7-1500T)](#tags-camming-s7-1500t)

### Camming with "MC_CamIn" (S7-1500T)

With the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)", you start a camming operation between a leading axis and a following axis. You specify the synchronous operation function with a [cam](#cam-technology-object-s7-1500t). To use a cam for camming, the cam must be interpolated. The utilized cam can be scaled on a job-related basis and applied shifted.

You can start synchronous operation when the leading axis is at a standstill or when it is in motion. Synchronous travel begins after synchronization of the following axis.

![Figure](images/165344558859_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165342858379_DV_resource.Stream@PNG-de-DE.png) | Transfer function:  Following value = f(leading value) |
| ![Figure](images/165342930955_DV_resource.Stream@PNG-de-DE.png) | Synchronization in advance |
| ![Figure](images/165343320331_DV_resource.Stream@PNG-de-DE.png) | Subsequent synchronization |
| ① | Leading value distance with synchronization in advance |
| ② | Leading value distance with subsequent synchronization |

You have the following options for camming with "MC_CamIn":

- [Defining the synchronous operation function](#configuring-the-synchronous-operation-function-of-the-cam-s7-1500t)
- [Interpolate cam with "MC_InterpolateCam"](#interpolating-a-cam-s7-1500t)
- [Scaling and shifting cam](#scaling-and-shifting-cam-s7-1500t)
- [Defining application mode of the cam](#defining-application-mode-of-the-cam-s7-1500t)
- [Defining direction of synchronization](#defining-direction-of-synchronization-with-mc_camin-s7-1500t)
- Define synchronous position and type of synchronization:

  - [Synchronizing following axis in advance using dynamic parameters](#synchronizing-following-axis-in-advance-using-dynamic-parameters-with-mc_camin-s7-1500t)
  - [Synchronizing following axis in advance using leading value distance](#synchronizing-following-axis-in-advance-using-leading-value-distance-with-mc_camin-s7-1500t)
  - [Synchronize the following axis in advance via the leading value path from the current leading value position](#synchronizing-following-axis-in-advance-via-the-leading-value-path-from-the-current-leading-value-position-with-mc_camin-s7-1500t)
  - [Subsequent synchronizing of following axis using leading value distance](#subsequent-synchronizing-of-following-axis-using-leading-value-distance-with-mc_camin-s7-1500t)
  - [Subsequent synchronizing of following axis using leading axis value starting at current leading value position](#subsequent-synchronizing-of-following-axis-using-leading-axis-value-starting-from-the-current-leading-value-position-with-mc_camin-s7-1500t)
  - [Directly set the following axis synchronously](#directly-set-following-axis-synchronously-with-mc_camin-s7-1500t)
  - [Directly set following axis synchronously at end of the cam](#directly-set-following-axis-synchronously-at-end-of-the-cam-with-mc_camin-s7-1500t)
- [Synchronous travel in camming](#synchronous-travel-in-camming-with-mc_camin-s7-1500t)
- [Reading a leading value with "MC_GetCamLeadingValue"](#reading-the-leading-value-in-camming-s7-1500t)
- [Reading a following value with "MC_GetCamFollowingValue"](#reading-the-following-value-in-camming-s7-1500t)
- [Reading a following value cyclically with "MC_GetCamFollowingValueCyclic"](#reading-out-the-following-value-cyclically-during-camming-s7-1500t)
- [Specify additive leading value with "MC_LeadingValueAdditive"](#specify-additive-leading-value-s7-1500t)
- [Offset leading value absolute or relative with "MC_PhasingAbsolute" or "MC_PhasingRelative"](#leading-value-offset-during-camming-s7-1500t)
- [Absolute or relative following value offset with "MC_OffsetAbsolute" or "MC_OffsetRelative"](#following-value-offset-during-camming-s7-1500t)
- [Changing synchronous operation function during Runtime](#changing-the-synchronous-operation-function-of-the-cam-online-s7-1500t)
- [Set camming to simulation mode with "MC_SynchronizedMotionSimulation"](#simulate-synchronous-operation-s7-1500t)
- [Desynchronize following axis with "MC_CamOut"](#desynchronize-camming-s7-1500t)
- [Cancel a pending camming with "MC_CamOut"](#only-cancel-a-pending-camming-with-mc_camout-s7-1500t)

Also note the [dynamic limits of the following axis in camming with "MC_CamIn"](#dynamic-limits-of-the-following-axis-in-camming-s7-1500t).

> **Note**
>
> **Using "DB_ANY" data type with the cam technology object**
>
> In Motion Control instructions with technology version ≥ V6.0, direct assignment of the "DB_ANY" data type at the "Cam" parameter leads to an access error. Due to this access error, the CPU changes to the "STOP" state.
>
> Use a data type conversion function for the cam technology object of the type "TO_Cam" or "TO_Cam_10k". A description of the procedure can be found in the section "[Parameter transfer for function blocks](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#parameter-transfer-for-function-blocks-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control Overview documentation".

### Configuring the synchronous operation function of the cam (S7-1500T)

This section contains information on the following topics:

- [Structure and operation of the cam editor (S7-1500T)](#structure-and-operation-of-the-cam-editor-s7-1500t)
- [Configure the profile and display of the cam (S7-1500T)](#configure-the-profile-and-display-of-the-cam-s7-1500t)
- [Inserting and configuring cam elements (S7-1500T)](#inserting-and-configuring-cam-elements-s7-1500t)
- [Transferring the synchronous operation function of the cam to the technology object data block (S7-1500T)](#transferring-the-synchronous-operation-function-of-the-cam-to-the-technology-object-data-block-s7-1500t)
- [Importing/exporting cam (S7-1500T)](#importingexporting-cam-s7-1500t)

#### Structure and operation of the cam editor (S7-1500T)

This section contains information on the following topics:

- [Structure and operation of the cam editor (S7-1500T)](#structure-and-operation-of-the-cam-editor-s7-1500t-1)
- [Structure of the graphical editor (S7-1500T)](#structure-of-the-graphical-editor-s7-1500t)
- [Shortcut menu in the graphical editor (S7-1500T)](#shortcut-menu-in-the-graphical-editor-s7-1500t)
- [Structure of the tabular editor (S7-1500T)](#structure-of-the-tabular-editor-s7-1500t)
- [Shortcut menu in the tabular editor (S7-1500T)](#shortcut-menu-in-the-tabular-editor-s7-1500t)
- [Operating the cam editor (S7-1500T)](#operating-the-cam-editor-s7-1500t)

##### Structure and operation of the cam editor (S7-1500T)

You configure a [cam technology object](#cam-technology-object-s7-1500t) using the cam editor.

You create the cam function using a chart a table containing the elements of the curve and the properties of the elements. Transitions are calculated between the individual elements of the curve (e.g. points, lines, polynomials). The curve reflects the path-related dependency between the leading axis (leading values, abscissa in the chart) and following axis (following values, ordinate in the chart).

The cam editor offers you the following support when creating a cam:

- Optimization of the curve form
- Generation of continuous and jerk-free transitions between curve elements
- Velocity-optimized design of the cam

The following figure shows the layout of the editor:

![Figure](images/165339094155_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar |
| ② | Curve diagram  The leading value range (definition range) is displayed on the abscissa (x axis).  The following value range (value range) is displayed on the ordinate (y axis). |
| ①+② | Graphical editor |
| ③ | Tabular editor |
| ④ | Inspector window (properties and display) |

###### Toolbar

You use the toolbar to operate the graphical editor and to import/export cams.

###### Graphical editor

In the graphical editor, you edit the elements of the curve graphically. The elements can be added, edited and deleted. Up to four charts can be created one above the other with synchronized abscissa. The setpoint curve as well as the curves for the effective position, velocity, acceleration and the jerk can be displayed in the charts.

The definition of the cam starts with the first defined interpolation point or the first segment and ends with the last interpolation point or the last segment. In contrast, the configurable display range of the leading value and the following value is used in the properties of the cam editor (Inspector window) only for display in the graphical editor.

###### Tabular editor

All elements of the curve are listed in the tabular editor. Existing elements can be edited. New elements can be added.

###### Inspector window

In the Inspector window, you configure the properties of the curve and of the selected element in the "Properties" tab. You configure the graphic view in the "Display" tab:

- Profile (e.g. leading and following value range, optimization and interpolation of the profile, number of elements used)
- Element (e.g. derivatives, polynomial coefficients, optimization of the element)
- Graphical view (e.g. line type, line color, scaling of the view)

###### Elements of the curve

The following table shows the elements that can be used to define the curve:

| Element | Description |
| --- | --- |
| Point | A point assigns a following value to a leading value. Depending on the [interpolation type](#interpolating-a-cam-s7-1500t), the curve runs through the point with these coordinates or only uses the point for orientation.  The velocity, acceleration and jerk can be defined in this point using the first, second and third derivative. |
| Point group | A point group combines two or more points into an commonly interpolated element and allows precise interpolation between these points. |
| Line | A line describes a motion with constant velocity from the start point of the line to the end point. The incline of the line specifies the constant velocity. |
| Sine | A sine element describes a motion according to the sine function. The sine function can be adjusted with the phase angle in the start point and end point, the period length, the amplitude as well as the oscillation zero point (offset). |
| Polynomial | A polynomial describes a motion according to a polynomial function of the 7th degree maximum. Polynomials can be defined by entering the boundary conditions or the polynomial coefficients. Optionally, you can configure a trigonometric polynomial component. |
| Inverse sine (approximated) | An inverse sine describes a motion according to the arcsine function. An inverse sine is approximated using interpolation points of the arcsine function. |
| Transition | Transitions interpolate the range between two elements. The ranges are automatically interpolated by the controller or using a configurable optimization according to VDI Guideline 2143.   Transitions are added automatically. |

###### Additional information

You can find more information about working with the cam editor in FAQ entry [109749820](https://support.industry.siemens.com/cs/ww/en/view/109749820) in the Siemens Industry Online Support.

##### Structure of the graphical editor (S7-1500T)

The graphical editor is divided into the following areas:

- Toolbar
- Curve diagram

###### Toolbar

The toolbar at the top of the graphical editor provides you with icons for the following functions:

| Symbol | Function | Description |
| --- | --- | --- |
| ![Toolbar](images/165344866187_DV_resource.Stream@PNG-de-DE.png) | Importing cam from file | See section "[Importing/exporting cam](#importingexporting-cam-s7-1500t)" |
| ![Toolbar](images/165344870155_DV_resource.Stream@PNG-de-DE.png) | Exporting cam to file | See section "[Importing/exporting cam](#importingexporting-cam-s7-1500t)" |
| ![Toolbar](images/165344566027_DV_resource.Stream@PNG-de-DE.png) | Edit elements/Move view | - Selecting and moving of individual elements - Moving the view using the drag-and-drop feature  To switch from any tool to the "Edit elements/Move view" tool, press the <Esc> key. |
| ![Toolbar](images/165344684811_DV_resource.Stream@PNG-de-DE.png) | Activate zoom selection | Zoom into selected area |
| ![Toolbar](images/165344688395_DV_resource.Stream@PNG-de-DE.png) | Activate vertical zoom | Vertical zoom into selected area without horizontal scaling  Alternative: <Ctrl> +drag to ordinate keeping mouse button pressed |
| ![Toolbar](images/165344691979_DV_resource.Stream@PNG-de-DE.png) | Activate horizontal zoom | Horizontal zoom into selected area without vertical scaling  Alternative: <Ctrl> +drag to abscissa keeping mouse button pressed |
| ![Toolbar](images/165344699147_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlargement of the display  Alternative: <Ctrl> + mouse wheel up in curve diagram |
| ![Toolbar](images/165344703115_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduction of the display  Alternative: <Ctrl> + mouse wheel down in curve diagram |
| ![Toolbar](images/165344695563_DV_resource.Stream@PNG-de-DE.png) | Show all | Display of entire definition and value range |
| ![Toolbar](images/165345196299_DV_resource.Stream@PNG-de-DE.png) | Zoom into curve | Zoom to the following value range of the curve that you selected in the legend of the chart |
| ![Toolbar](images/165345188363_DV_resource.Stream@PNG-de-DE.png) | Activate snap grid | Alignment of inputs and element end points to the configurable snap grid and to other element end points |
| ![Toolbar](images/165344874123_DV_resource.Stream@PNG-de-DE.png) | Inserting a point | Adding a point to the chart |
| ![Toolbar](images/165344929291_DV_resource.Stream@PNG-de-DE.png) | Inserting a line | Adding a line to the chart |
| ![Toolbar](images/165344933259_DV_resource.Stream@PNG-de-DE.png) | Inserting a sine | Adding a sine element to the chart |
| ![Toolbar](images/165344937227_DV_resource.Stream@PNG-de-DE.png) | Inserting a polynomial | Adding a polynomial to the chart |
| ![Toolbar](images/165345184395_DV_resource.Stream@PNG-de-DE.png) | Inserting an inverse sine | Adding an inverse sine to the chart |
| ![Toolbar](images/165345280267_DV_resource.Stream@PNG-de-DE.png) | Insert point group | Add a point group to the chart |
| ![Toolbar](images/165345276683_DV_resource.Stream@PNG-de-DE.png) | View: A chart with positions | Display of one chart with the following curves of the cam opened in the editor:  - Preset curve - Effective position |
| ![Toolbar](images/165344795019_DV_resource.Stream@PNG-de-DE.png) | View: A chart with all curves | Display of one chart with the following curves of the cam opened in the editor:  - Preset curve - Effective position - Effective velocity - Effective acceleration - Effective jerk |
| ![Toolbar](images/165344798603_DV_resource.Stream@PNG-de-DE.png) | View: Four charts with all curves | Display of four charts with the following curves of the cam opened in the editor:  - Chart with setpoint curve and effective position - Chart with effective velocity - Chart with effective acceleration - Chart with effective jerk |
| ![Toolbar](images/165344707083_DV_resource.Stream@PNG-de-DE.png) | Vertical measuring lines | Displaying and moving of vertical measuring lines  Hold down the left mouse button and drag to draw a measuring range. The vertical position of the measuring lines can be moved.  The function values for the measuring line positions are displayed in the chart. The difference of the measuring lines is displayed between the measuring lines. |
| ![Toolbar](images/165344787467_DV_resource.Stream@PNG-de-DE.png) | Horizontal measuring lines | Displaying and moving of horizontal measuring lines  Hold down the left mouse button and drag to draw a measuring range. The horizontal position of the measuring lines can be moved.   The function values for the measuring line positions are displayed in the chart. The difference of the measuring lines is displayed between the measuring lines. |
| ![Toolbar](images/165344791051_DV_resource.Stream@PNG-de-DE.png) | Show legend | Showing or hiding of the legend in the curve diagram.  To display values for a specific curve on the ordinate, click on the name of the corresponding curve in the legend. |
| ![Toolbar](images/163741876875_DV_resource.Stream@PNG-de-DE.png) | Read out and display online curve one time | Display of the position values of the cam read back from the CPU (orange)  The cam editor reads out the cam that was already loaded into the CPU. The read out "Online curve" is displayed in the graphical editor. |

###### Curve diagram

In the curve diagram, you enter the elements of the curve and adjust the curve by selecting and moving elements.

Chart areas outside of the leading value/following value range configured in "[Profile > General](#configuration-of-profile---general-s7-1500t)" are grayed out. Elements outside the leading value/following value range are displayed with a warning ("Element is outside the definition range").

You can display various curves (position, velocity, acceleration and jerk) one above the other in up to four charts by configuring the graphical view accordingly. When multiple charts are displayed, you can adapt the graphs to match the separator lines.

The view can be zoomed in the manual mode by pressing <Ctrl > + Mouse wheel and <Ctrl > + while pressing the mouse button on the abscissa/ordinate.

The editor shows messages for checking the entered curve via warning triangles ![Curve diagram](images/165345192331_DV_resource.Stream@PNG-de-DE.png). The tooltip of the waring triangle shows the message text. Configure the checking of the curve in the "[Check](#configuration-of-profile---check-s7-1500t)" configuration window.

###### Display of the online curve

When you click the ![Display of the online curve](images/163741876875_DV_resource.Stream@PNG-de-DE.png) icon, the cam editor reads the data from the technology object data block and displays the curve in the graphical editor:

| Cam status | Interpolation status | Description |
| --- | --- | --- |
| Data not modified  (CamDataChanged = 0) | Not interpolated  (Interpolated = 0) | Only the points and segments of the cam are displayed. |
| Interpolated  (Interpolated = 1) | The interpolated cam is displayed. |  |
| Data modified  (CamDataChanged = 1) | Not interpolated  (Interpolated = 0) | Only the points and segments of the cam are displayed. |
| Interpolated  (Interpolated = 1) | The interpolated cam as well as changed points and segments are displayed. |  |

##### Shortcut menu in the graphical editor (S7-1500T)

Use the shortcut menu in the graphical editor to call up the following functions:

| Function | Description |
| --- | --- |
| Show all | Displaying the entire definition range and value range |
| Zoom into curve | Displaying the curve selected in the legend of the chart |
| Zoom in | Enlargement of the display |
| Zoom out | Reduction of the display |
| Open charts and curves | Opening of the "[Charts and curves](#configuration-charts---charts-and-curves-s7-1500t)" dialog |
| Cut | Removing the selected elements and copying them to the clipboard |
| Copy | Copying of the selected elements to the clipboard |
| Insert | Pasting of the elements from the clipboard to the last element |
| Delete | Deletion of the selected elements  Transitions to existing elements are also deleted. |
| Insert special | Open the "[Insert elements](#inserting-elements-from-the-clipboard-s7-1500t)" dialog |
| Group points | Combine the selected points into a group of points  The entry is displayed under the following conditions:  - Only points are selected in the graphic/tabular editor. - There are no other elements between the selected points. |
| Dissolve point group | Ungrouping the selected point group into individual points |
| Show/hide measuring point labels | Showing or hiding the measuring points  The entry is displayed under the following conditions:  - Measuring lines are displayed. - Measuring points are hidden/shown. |
| Move | Open the "[Move elements](#move-elements-s7-1500t)" dialog |
| Scale | Open the "[Scale elements](#scale-elements-s7-1500t)" dialog |

##### Structure of the tabular editor (S7-1500T)

The tabular editor shows all elements of the curve, sorted by their leading values. The elements can be adjusted. New elements can be added.

The following properties are displayed in the corresponding column for each element of the curve:

| Column/Property |  | Description |
| --- | --- | --- |
| First column |  | Sequential number of the element |
| Second column |  | Display of calculation problems that might occur with warning triangle ![Figure](images/165345192331_DV_resource.Stream@PNG-de-DE.png)  The alarm text is displayed in the tooltip of the warning triangle. |
| Element type |  | - Display/change of element type - Adding elements  Possible element types:  - Point - Point group - Line - Sine - Polynomial - Inverse sine - Transition |
| Start |  | Parameter values at start point of the element |
|  | Leading value | Leading values at start point of the element |
| Following value | Following values at start point of the element |  |
| Position<sup>1)</sup> | Calculated effective position at start point of the element |  |
| Velocity<sup>1)</sup> | Calculated effective velocity at start point of the element |  |
| Acceleration<sup>1)</sup> | Calculated effective acceleration at start point of the element |  |
| Jerk<sup>1)</sup> | Calculated effective jerk at start point of the element |  |
| End |  | Parameter values at end point of the element |
|  | Leading value | Leading values at end point of the element |
| Following value | Following values at end point of the element |  |
| Position<sup>1)</sup> | Calculated effective position at end point of the element |  |
| Velocity<sup>1)</sup> | Calculated effective velocity at end point of the element |  |
| Acceleration<sup>1)</sup> | Calculated effective acceleration at end point of the element |  |
| Jerk<sup>1)</sup> | Calculated effective jerk at end point of the element |  |
| Comment |  | Optional comment for element. |
| <sup>1)</sup> Displayed according to the configuration in "Properties (Inspector window) > Graphical view > Charts and curves". |  |  |

##### Shortcut menu in the tabular editor (S7-1500T)

Use the shortcut menu in the tabular editor to call up the following functions:

| Function | Description |
| --- | --- |
| Insert row above | Insert a table row/element before the selected row/element  If no transition exists before the element, the selected element and the adjoining elements are changed. |
| Insert row below | Insert a table row/element after the selected row/element  If no transition exists after the element, the selected element and the adjoining elements are changed. |
| Cut | Removing the selected elements and copying them to the clipboard |
| Copy | Copying of the selected elements to the clipboard |
| Insert | Pasting of the elements from the clipboard to the last element |
| Delete | Deletion of the selected elements  Transitions to existing elements are also deleted. |
| Insert special | Open the "[Insert elements](#inserting-elements-from-the-clipboard-s7-1500t)" dialog |
| Group points | Combine the selected points into a group of points  The entry is displayed under the following conditions:  - Only points are selected in the graphic/tabular editor. - There are no other elements between the selected points. |
| Dissolve point group | Ungroups the selected point group into individual points |
| Move | Open the "[Move elements](#move-elements-s7-1500t)" dialog |
| Scale | Open the "[Scale elements](#scale-elements-s7-1500t)" dialog |

##### Operating the cam editor (S7-1500T)

The procedure described here shows the basic operation of the cam editor. This procedure serves as a recommendation.

The basic operation can include the follow tasks:

- Adapting defaults
- Creating and adapting the curve
- [Interpolation/optimization of the transitions](#interpolation-according-to-vdi-guideline-2143-s7-1500t)

###### Adapting defaults

To adjust the leading and following value range of the cam profile as well as the graphical view, follow these steps:

1. In the properties (Inspector window), open the "[Profile > General](#configuration-of-profile---general-s7-1500t)" configuration window.
2. Configure the leading value range and the following value range of the curve definition.

   The graphical view is automatically adapted to the inputs.
3. In the area navigation of the Inspector window, open the "[Display](#configure-the-profile-and-display-of-the-cam-s7-1500t)" tab.
4. Configure the following configuration windows:

   - The display of the charts and curves
   - The grid spacing for aligning inputs in the graphical editor
   - The decimal places displayed in the cam editor.

###### Creating and adapting the curve

To create and adapt the curve, follow these steps:

1. Use the graphical editor and/or the tabular editor to add the elements of the cam:

   - On the toolbar, click the icon for inserting the corresponding element. Place the element at the required position in the graphical editor.
   - Use <Add> to insert the corresponding elements in the "Element type" column of the tabular editor. Adjust the position of the elements using the start and end values.

   Transitions between the elements are added automatically.
2. To edit an element, select it in the graphical or tabular editor.

   The element is highlighted in the graphical and in the tabular editor. The "Element > Parameter" configuration window is displayed in the properties (Inspector window), or in case of a transition, "Element > Characteristic".
3. The elements can be adjusted as follows:

   - Move the element or the drag handles of the element in the graphical editor.
   - Adjust the start and end values in the tabular editor.
   - Configure additional element-specific parameters in the properties (Inspector window) in the "Element > Parameter" configuration window.
   - Set the interpolation of the transitions with the properties (Inspector window).

The number of elements used is displayed in the properties (Inspector window) in the "[Profile > Statistics](#show-elements-used-s7-1500t)" properties window.

---

**See also**

[System interpolation (S7-1500T)](#system-interpolation-s7-1500t)
  
[Configuring transitions (S7-1500T)](#configuring-transitions-s7-1500t)
  
[Configuration charts - Charts and curves (S7-1500T)](#configuration-charts---charts-and-curves-s7-1500t)
  
[Interpolate cam with "MC_InterpolateCam" (S7-1500T)](#interpolate-cam-with-mc_interpolatecam-s7-1500t)

#### Configure the profile and display of the cam (S7-1500T)

This section contains information on the following topics:

- [Properties and display in the inspector window (S7-1500T)](#properties-and-display-in-the-inspector-window-s7-1500t)
- [Configuration of profile - General (S7-1500T)](#configuration-of-profile---general-s7-1500t)
- [Configuration of profile - Effective runtime curves (S7-1500T)](#configuration-of-profile---effective-runtime-curves-s7-1500t)
- [Configuration of profile - Check (S7-1500T)](#configuration-of-profile---check-s7-1500t)
- [Configuration charts - Charts and curves (S7-1500T)](#configuration-charts---charts-and-curves-s7-1500t)
- [Configuration charts - Snap grid (S7-1500T)](#configuration-charts---snap-grid-s7-1500t)
- [Configuration - Decimal places (S7-1500T)](#configuration---decimal-places-s7-1500t)

##### Properties and display in the inspector window (S7-1500T)

You configure further element-specific parameters in the inspector window in the following tabs:

- The parameters for the profile of the cam as well as for the elements are displayed in the "properties" tab. The corresponding parameters are displayed depending on the selected element:

  - If no element of the curve is selected, only the settings for the profile of the cam are displayed.
  - If an element of the curve is selected, the parameters of the element are additionally displayed.
- In the "Display" tab you can configure the graphic view of the charts and curves.

##### Configuration of profile - General (S7-1500T)

Configure the display range of the graphical editor in the "General" configuration window.

The inputs of the leading value range and following value range only effect the display in the graphical editor. The cam is interpolated in the definition range between the following values:

- First defined interpolation point/start of the first segment of the cam (<TO>.StatusCam.StartLeadingValue)
- Last defined interpolation point/end of the last segment of the cam (<TO>.StatusCam.EndLeadingValue)

###### Leading value display range

In this area, configure the leading value display range in the graphical editor:

| Parameters | Description |
| --- | --- |
| Start | In this field you configure the initial value of the display range of the leading value. |
| End | In this field you configure the full-scale value of the display range of the leading value. |

###### Following value display range

In this area, you can configure the limitation of the following value range in the graphical editor:

| Parameters | Description |
| --- | --- |
| Minimum | In this field you configure the lowest permissible value for the following value display range. |
| Maximum | In this field you configure the greatest permissible value for the following value display range. |

##### Configuration of profile - Effective runtime curves (S7-1500T)

Configure the values for the leading axis and following axis that are applied to the effective curve In the "Effective runtime curves" configuration window. The runtime emulation calculates the effective curve with these applied values and displays the curve in the graphical editor with the applied limits.

The inputs are not downloaded into the CPU. This means the cam is interpolated without these inputs. You can use these applied values to test and visualize how the cam behaves during operation, for example, when entering a scaling at an "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)" job.

###### Settings of the leading axis

Configure the calculation and display of the curve on the leading value end in this area:

| Parameters | Description |
| --- | --- |
| Copy from axis | Using the button and the "Copy leading value settings of axis" dialog, select an axis whose maximum velocity is applied as the velocity for the leading axis. |
| Scaling factor | Configure a leading value-side scaling factor in this field. This visualizes a scaled curve. You enter a scaling during runtime with an "MC_CamIn" job. |
| Unit of measure | In the selection list, select the unit of measure for the leading value. |
| Unit of measure for the first derivative | In the selection list, select the unit of measure for the first derivative of the leading value. |
| Velocity | Configure the velocity of the leading axis applied for the runtime emulation of the curve in this field. |

###### Settings of the following axis

Configure the calculation and display of the curve on the following value side in this area:

| Parameters | Description |
| --- | --- |
| Copy from axis | Using the button and the "Copy following value settings of axis" dialog, select an axis whose maximum dynamic values are applied as the limits to be checked during calculation and display of the curve. |
| Scaling factor | Configure a following value-side scaling factor in this field. This visualizes a scaled curve. You enter a scaling during runtime with an "MC_CamIn" job. |
| Unit of measure | In the selection list, select the unit of measure for the following value. |
| Unit of measure for the first derivative | In the selection list, select the unit of measure for the first derivative of the following value. |
| Maximum velocity | Configure the maximum velocity for the following axis in this field. |
| Maximum acceleration | Configure the maximum acceleration for the following axis in this field. |
| Maximum jerk | Configure the maximum jerk for the following axis in this field. |

##### Configuration of profile - Check (S7-1500T)

In the "Check" configuration window, you configure which criteria the cam editor checks when entering the curve. When you activate a check, the graphical and the tabular editor display corresponding messages via a warning triangle on the element. Use the tooltip at the warning triangle to display the message text.

> **Note**
>
> Use the checking options for the final check of the cam and enable all checks before completing the cam. Make any required adjustments to the cam profile.

###### Checking of limit violations

Configure the checks for compliance with the configured limits in this area:

| Check/Element | Description |
| --- | --- |
| Check curve definition of the leading and following value ranges | Select this check box to have the cam editor check the curve accordingly. |
| Check adherence to the maximum values of the derivatives of the effective runtime curve | Select this check box to have the cam editor check the curve accordingly. |

###### Verification of VDI suitability

Select the "Check the suitability of transitions in accordance with VDI" check box to have the cam editor check the VDI suitability of the curve.

The cam editor checks the following with this:

- Support of the transition classification of the currently selected VDI transition
- Boundary value adjustment according to VDI

###### Verification of continuity

In the "Required continuity" list, select which parameter the cam editor checks for continuity:

- Position
- Velocity
- Acceleration
- Jerk

If a function or a derivative is discontinuous, all higher derivatives are also discontinuous.

##### Configuration charts - Charts and curves (S7-1500T)

In the "Charts and curves" configuration window, configure the display of the graphical editor.

###### "Reset to defaults" button

Use this button to reset all settings of the view of charts and curves to the default settings.

###### Configuration table

Configure the display of the graphical editor in the table:

| Column | Description |
| --- | --- |
| Show | Displaying/hiding of charts 1 to 4 |
| Visible | Displaying/hiding of curves in the chart  You can show or hide online curves already offline.   The curve becomes visible when you have shown the curve, established an online connection and read out the online curve. |
| Name | Name of chart or curve  New curves can be added. Existing curves can be removed.  Curves of other cams can also be displayed. The name of the other cam is also displayed in the table and in the legend of the chart.  A curve can be inserted multiple times in a chart, e.g. in order to display it with different scalings. |
| Color | Line color of the curve |
| Line type | Line type of the curve |
| Offset of the leading values<sup>1)</sup> | Movement of the curve on the abscissa |
| Multiplier for leading values<sup>1)</sup> | Scaling of abscissa |
| Offset of the following values<sup>1)</sup> | Movement of the curve on the ordinate |
| Multiplier for following values<sup>1)</sup> | Scaling of ordinate |
| <sup>1)</sup> Only affects the display of the curve in the chart. You specify the scaling and shifting of the cam during camming in the Motion Control instruction "MC_CamIn". |  |

##### Configuration charts - Snap grid (S7-1500T)

In the "Snap grid" configuration window, you configure the grid spacing for aligning inputs to the grid in the graphical editor. When "Snap" is activated, inputs and element end points are aligned to this grid and to other element end points.

###### Snap grid spacing

In this area, configure the grid spacing of the snap grid:

| Parameter | Description |
| --- | --- |
| Grid spacing leading value | Configure the grid spacing on the abscissa (leading values) in this field. |
| Grid spacing following value | Configure the grid spacing on the ordinate (following values) in this field. |

##### Configuration - Decimal places (S7-1500T)

In the "Decimal places" configuration window, you configure how many decimal places are used to represent the values in the graphical and tabular editor as well as in the configuration windows. The values are rounded in the displays. The settings do not affect the calculation of the curves. The curves are calculated with higher accuracy regardless of the settings.

###### Displayed decimal places

In this area, configure the displayed decimal places:

| Parameter | Description |
| --- | --- |
| Tabular editor and configuration window | In this field, configure the number of decimal places for displaying values in the tabular editor and in the configuration windows. |
| Graphical editor | In this field, configure the number of decimal places for displaying values in the graphical editor. |

#### Inserting and configuring cam elements (S7-1500T)

This section contains information on the following topics:

- [Inserting and configuring a point (S7-1500T)](#inserting-and-configuring-a-point-s7-1500t)
- [Inserting and configuring a point group (S7-1500T)](#inserting-and-configuring-a-point-group-s7-1500t)
- [Inserting and configuring the line (S7-1500T)](#inserting-and-configuring-the-line-s7-1500t)
- [Inserting and configuring a sine (S7-1500T)](#inserting-and-configuring-a-sine-s7-1500t)
- [Inserting and configuring a polynomial (S7-1500T)](#inserting-and-configuring-a-polynomial-s7-1500t)
- [Inserting and configuring an inverse sine (S7-1500T)](#inserting-and-configuring-an-inverse-sine-s7-1500t)
- [Inserting elements from the clipboard (S7-1500T)](#inserting-elements-from-the-clipboard-s7-1500t)
- [Move elements (S7-1500T)](#move-elements-s7-1500t)
- [Scale elements (S7-1500T)](#scale-elements-s7-1500t)
- [Deleting elements (S7-1500T)](#deleting-elements-s7-1500t)
- [Show elements used (S7-1500T)](#show-elements-used-s7-1500t)

##### Inserting and configuring a point (S7-1500T)

A point assigns a following value to a leading value. The curve runs through the point with these coordinates.

By means of the first, second and third derivatives, the velocity, acceleration and jerk can be defined in this point. The derivative are only taken into consideration during VDI-based optimization of transitions of the point to other elements.

###### Inserting a point

To add a point to the curve, follow these steps:

1. On the toolbar, click the ![Inserting a point](images/165344874123_DV_resource.Stream@PNG-de-DE.png) "Insert point" icon.
2. In Chart 1, click on the desired position.  
   The point is inserted. The coordinates are displayed for the point. The tabular editor and the view of the properties (Inspector window) are updated. A transition to any element is inserted automatically.

###### Moving a point

To move a point in the graphical editor, follow these steps:

1. On the toolbar, click the icon ![Moving a point](images/165344566027_DV_resource.Stream@PNG-de-DE.png) "Edit elements/Move view".
2. Select the point in chart 1.
3. Use the drag-and-drop feature to move the point to the desired position.

###### Adapting parameters

The parameters of the point can be adjusted in the tabular editor as well as in the inspector window under "Properties > Element > Parameter".

Configure the parameters of the selected point in this area:

| Parameter/Option |  | Description |
| --- | --- | --- |
| Leading value of the point |  |  |
|  | Leading value | In this field, configure the leading value of the point (value in the definition area). |
| Following values of the point |  |  |
|  | Following value | Configure the following value of the point (value in the range of the function) in this field. |
| Use first derivative | By selecting the check box, you can specify the first derivative at the selected point and include it in the interpolation of the cam. |  |
| First derivative | Configure the value of the first derivative in the selected point in this field. |  |
| Use second derivative | By selecting the check box, you can specify the second derivative at the selected point and include it in the interpolation of the cam. |  |
| Second derivative | Configure the value of the second derivative in the selected point in this field. |  |
| Use third derivative | By selecting the check box, you can specify the third derivative at the selected point and include it in the interpolation of the cam. |  |
| Third derivative | Configure the value of the third derivative in the selected point in this field. |  |

The derivative are only taken into consideration during VDI-based optimization of transitions of the point to other elements.

##### Inserting and configuring a point group (S7-1500T)

A point group combines two or more points into a commonly interpolated element and allows precise interpolation between the points.

###### Insert point group

To add a point group to the curve, proceed as follows:

1. On the toolbar, click the ![Insert point group](images/165345280267_DV_resource.Stream@PNG-de-DE.png) "Insert point group" icon.
2. In Chart 1, click on the desired position at which you want to insert the point group.  
   The point group is inserted. The coordinates of the start point and the end point are displayed at the point group. The tabular editor and the view of the properties (Inspector window) are updated. If a different element already exists, a transition to the existing element is automatically inserted.

###### Adapt point group

To adapt a point group in the graphical editor, proceed as follows:

1. On the toolbar, click the icon ![Adapt point group](images/165344566027_DV_resource.Stream@PNG-de-DE.png) "Edit elements/Move view".
2. Select the point group in chart 1.

   The point group is highlighted graphically with drag handles. The following drag handles are displayed:

   - Start point of the point group
   - End point of the point group
3. Use the drag-and-drop feature to move the handles or the whole point group to the desired position.

   If further interpolation points are configured between the start point and the end point in the point group, the cam editor handles the interpolation points as follows:

   - Definition type of the leading value "Relative to segment"

     The interpolation points are shifted relative to the start and end points.
   - Definition type of the leading value "Absolute in the profile"

     The interpolation points are not moved.

###### Adapting parameters

You can adjust the parameters of the point group in the graphical editor, in the tabular editor as well as in the inspector window under "Properties > Element > Parameter".

Configure the parameters of the selected point group in this area:

| Parameter/Option |  |  | Description |
| --- | --- | --- | --- |
| Leading values of the point group |  |  |  |
|  | Start |  | In this field, configure the start point of the point group in the leading value range (definition area). |
| End |  | In this field, configure the end point of the point group in the leading value area (definition area). |  |
| Interpolation points |  |  |  |
|  | Definition type of the leading values |  | In the drop-down list, select how the leading values of the interpolation points are specified:  - Relative to segment   You specify the leading values of the interpolation points relative to the group of points from 0.0 to 1.0. The value 0.0 corresponds to the beginning of the point group. The value 1.0 corresponds to the end of the point group. - Absolute in the profile   You specify the leading values of the interpolation points as absolute values. |
| Definition type of the following values |  | In the drop-down list, select how the following values of the interpolation points are specified:  - Relative to segment   You specify the following values of the interpolation points relative to the following value range of the point group from 0.0 to 1.0. The value 0.0 corresponds to the configured minimum following value of the point group. The value 1.0 corresponds to the configured maximum following value of the point group. - Absolute in the profile   You specify the following values of the interpolation points as absolute values. |  |
| Minimum following value |  | In this field, configure the minimum following value for the point group in the following value range. |  |
| Maximum following value |  | In this field, configure the maximum following value of the point group in the following value range (value range). |  |
| ![Adapting parameters](images/165345284235_DV_resource.Stream@PNG-de-DE.png) |  | Use this "Insert interpolation point" icon to add an interpolation point to the point group. |  |
| Interpolation points |  | This table shows the configured interpolation points sorted by increasing leading value.   Add interpolation points using the ![Adapting parameters](images/165345284235_DV_resource.Stream@PNG-de-DE.png) icon. Delete interpolation points by marking a row and pressing the <Delete> key. If you delete all points except one, the element type is changed from "Point group" to "Point". |  |
|  | Leading value | In this field, configure the leading value of the interpolation point (value in the definition area). |  |
| Following value | In this field, configure the following value of the interpolation point (value in the value range). |  |  |
| Interpolation |  |  |  |
|  | Interpolation type |  | In the drop-down list, select the interpolation type to be used for interpolating the point group:   - Interpolation with cubic splines - Interpolation with Bézier splines |
| Approximation |  |  |  |
|  | Mapping method |  | Select the mapping method in the drop-down list:  - Point approximation - Segment approximation |
| Number of interpolation points |  | Configure the number of interpolation points for the point approximation in this field. |  |
| Maximum following value tolerance |  | In this field, enter the maximum permissible deviation (absolute) of the approximation from the interpolation points.  If the configured value is exceeded, a warning is displayed in the graphical editor at the point group. |  |

##### Inserting and configuring the line (S7-1500T)

A line describes a motion with constant velocity from the start point to the end point of the line. The incline of the line specifies the constant velocity.

###### Inserting a line

To add a line to the curve, follow these steps:

1. On the toolbar, click the ![Inserting a line](images/165344929291_DV_resource.Stream@PNG-de-DE.png) "Insert line" icon.
2. Use the drag-and-drop feature in chart 1 to draw the line from the start position to the end position.  
   The straight line is inserted. The coordinates of the start point and end point are displayed for the line. The tabular editor and the view of the properties (Inspector window) are updated. A transition to any element is inserted automatically.

###### Moving a line

To move a line in the graphical editor, follow these steps:

1. On the toolbar, click the icon ![Moving a line](images/165344566027_DV_resource.Stream@PNG-de-DE.png) "Edit elements/Move view".
2. Select the line in chart 1.

   The line is graphically highlighted with drag handles. The following drag handles are displayed:

   - Start point of the line
   - End point of the line
3. Use the drag-and-drop feature to move the handles or the entire line to the desired position.

###### Adapting parameters

The parameters of the line can be adjusted in the graphical editor, in the tabular editor as well as in the inspector window under "Properties > Element > Parameter".

Configure the parameters of the selected line in this area:

| Parameters |  | Description |
| --- | --- | --- |
| Leading values of the line |  |  |
|  | Start | Configure the start point of the line in the leading value range (definition range) in this field. |
| End | Configure the end point of the line in the leading value range (definition range) in this field. |  |
| Following values of the line |  |  |
|  | Definition by | In the selection list, select the parameters to be used to define the line:  - Following values at start and end - Following value at the start and incline - Incline and following value at end   The corresponding parameters are displayed based on the selection. |
| Start | Configure the start point of the line in the following value range (value range) in this field. |  |
| End | Configure the end point of the line in the following value range (value range) in this field. |  |
| Incline | Configure the incline of the line in this field. |  |

##### Inserting and configuring a sine (S7-1500T)

A sine element describes a motion according to the sine function. The sine function can be adjusted with the phase angle in the start point and end point, the period length, the amplitude as well as the oscillation zero point (offset).

###### Inserting a sine

To add a sine to the curve, follow these steps:

1. On the toolbar, click the "Insert sine" icon ![Inserting a sine](images/165344933259_DV_resource.Stream@PNG-de-DE.png).
2. In Chart 1, click on the position desired position. The mouse pointer points to the start position of the sine here.

   The sine is inserted. The coordinates of the start point and end point are displayed for the sine. The tabular editor and the view of the properties (Inspector window) are updated. A transition to any element is inserted automatically.

###### Adjusting a sine

To adjust a sine in the graphical editor, follow these steps:

1. On the toolbar, click the icon ![Adjusting a sine](images/165344566027_DV_resource.Stream@PNG-de-DE.png) "Edit elements/Move view".
2. Select the sine in chart 1.

   The sine is graphically highlighted with drag handles and guide lines for the zero line and the amplitude. The following drag handles are displayed:

   - Leading value/shift at left/right boundary

     These drag handles can also be used to adjust the inclination of an inclined sine.
   - Leading value at left/right boundary
   - Phase at left/right boundary
   - Amplitude
3. Use the drag-and-drop feature to move the handles or the entire sine to the desired position.

###### Adapting parameters

The parameters of the sine can be adjusted in the graphical editor, in the tabular editor as well as in the inspector window under "Properties > Element > Parameter".

Configure the parameters of the selected sine element in this area:

| Parameters |  | Description |
| --- | --- | --- |
| Leading values of the sine |  |  |
|  | Start | Configure the start point of the sine element in the leading value range (definition range) in this field. |
| End | Configure the end point of the sine element in the leading value range (definition range) in this field. |  |
| Trigonometric parameters |  |  |
|  | Amplitude | Configure the amplitude of the sine element in this field. |
| Definition by | In the drop-down list, select how the sine element is defined:  - Phase at start and at end - Phase at start and period length - Phase at start and frequency - Period length and phase at end - Frequency and phase at end   The corresponding parameters are displayed based on the selection. |  |
| Phase angle at start | Configure the phase angle at the start of the sine element in this field. |  |
| Phase angle at end | Configure the phase angle at the end of the sine element in this field. |  |
| Period length | Configure the period length of the sine element in this field. |  |
| Frequency | Configure the frequency of the sine element in this field. |  |
| Extended parameters |  |  |
|  | Segment type | Select the variant of the sine element in the drop-down list.  - Sine - Inclined sine   If you have configured an inclined sine, additional orientation lines are displayed in the graphical editor for the amplitude and center position.   The corresponding parameters are displayed based on the selection. |
| Offset | Configure the oscillation midpoint of the sine element in this field. |  |
| Definition of inclination as a function of: | In the drop-down list, select how the inclined sine element is defined:  - Offset at start and end - Offset at start and inclination - Inclination and offset at end   The corresponding parameters are displayed based on the selection. |  |
| Offset at start | Configure the center of oscillation at the start of the sine element in this field. |  |
| Offset at end | Configure the center of oscillation at the end of the sine element in this field. |  |
| Inclination | Configure the inclination of the sine element in this field. |  |

##### Inserting and configuring a polynomial (S7-1500T)

A polynomial describes a motion according to a polynomial function of the 7th degree maximum. Polynomials can be defined by entering the boundary conditions or the polynomial coefficients. Optionally, you can configure a trigonometric polynomial component.

###### Inserting a polynomial

To add a polynomial to the curve, follow these steps:

1. On the toolbar, click the ![Inserting a polynomial](images/165344937227_DV_resource.Stream@PNG-de-DE.png) "Insert polynomial" icon.
2. In Chart 1, click on the position desired position. In so doing, the mouse pointer points to the start position of the polynomial.

   The polynomial is inserted. The coordinates of the start point and end point are displayed for the polynomial. The tabular editor and the view of the properties (Inspector window) are updated. If a different element already exists, a transition to the existing element is automatically inserted.

###### Adjusting a polynomial

To adjust a polynomial in the graphical editor, follow these steps:

1. On the toolbar, click the icon ![Adjusting a polynomial](images/165344566027_DV_resource.Stream@PNG-de-DE.png) "Edit elements/Move view".
2. Select the polynomial in chart 1.

   The polynomial is graphically highlighted with drag handles. The following drag handles are displayed:

   - Leading value/following value at left/right boundary
   - Position of point of inflection (lambda: relative to the element or absolute in the profile)
3. Use the drag-and-drop feature to moves sizing handles or the entire polynomial to the required position.

###### Adapting parameters

You can adjust the parameters of the polynomial in the graphical editor, in the tabular editor as well as in the inspector window under "Properties > Element > Parameter".

Configure the parameters of the selected polynomial in this area:

| Parameters |  | Description |
| --- | --- | --- |
| Leading values of the polynomial |  |  |
|  | Start | Configure the start point of the polynomial in the leading value range (definition range) in this field. |
| End | Configure the end point of the polynomial in the leading value range (definition range) in this field. |  |
| Polynomial parameters |  |  |
|  | Definition by | In the selection list, select how the polynomial is defined:  - Coefficients - Boundary values   The corresponding parameters are displayed based on the selection. |
| Coefficients | Configure the coefficients of the 6th degree polynomial function in these fields:  P(x) = a<sub>6</sub>x<sup>6</sup> + a<sub>5</sub>x<sup>5</sup> + a<sub>4</sub>x<sup>4</sup> + a<sub>3</sub>x<sup>3</sup> + a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>  The coefficients are shown in scientific notation, e.g. "9.6450617283e-11". |  |
| Following value - Left boundary value | Configure the following value at the start of the polynomial in this field. |  |
| Following value - Right boundary value | Configure the following value at the end of the polynomial in this field. |  |
| Use first derivative | Select the check box to specify the first derivative (velocity) in the left/right boundary value of the polynomial and to include it in the interpolation of the cam. |  |
| First derivative - left boundary value | Configure the first derivative (velocity) for the following value at the start of the polynomial in this field. |  |
| First derivative - right boundary value | Configure the first derivative (velocity) for the following value at the end of the polynomial in this field. |  |
| Use second derivative | Select the check box to specify the second derivative (acceleration) in the left/right boundary value of the polynomial and to include it in the interpolation of the cam. |  |
| Second derivative - left boundary value | Configure the second derivative (acceleration) for the following value at the start of the polynomial in this field. |  |
| Second derivative - right boundary value | Configure the second derivative (acceleration) for the following value at the end of the polynomial in this field. |  |
| Use third derivative | Select the check box to specify the third derivative (jerk) in the left/right boundary value of the polynomial and to include it in the interpolation of the cam. |  |
| Third derivative - left boundary value | Configure the third derivative (jerk) for the following value at the start of the polynomial in this field. |  |
| Third derivative - right boundary value | Configure the third derivative (jerk) for the following value at the end of the polynomial in this field. |  |
| Lambda | In the selection list, select how the turning point of the polynomial is specified in the "Lambda position" field:  - No lambda   Do not enter any value. The position of the point of inflection is calculated automatically. - Relative to the element   You specify the leading value of the turning point relative to the polynomial from 0.0 to 1.0. The value 0.0 corresponds to the beginning of the polynomial. The value 1.0 corresponds to the end of the polynomial. - Absolute in the profile   You specify the leading value of the point of inflection as an absolute value. |  |
| In this field, configure the leading value of the point of inflection for the polynomial according to the selection in the selection list. |  |  |
| Extended parameters |  |  |
|  | Segment type | In the selection list, select whether or not the polynomial is to have a trigonometric component.  When "Polynomial with trigonometric portion" is selected, the corresponding trigonometric parameters are displayed, as they are with sine. When a sine element is converted to a polynomial, the sine element is configured as a polynomial with trigonometric portion. The shape of the element is retained.  You have the option to define the trigonometric portion of the polynomial using the following formula:  Y(x) = a<sub>6</sub>x<sup>6</sup> + a<sub>5</sub>x<sup>5</sup> + a<sub>4</sub>x<sup>4</sup> + a<sub>3</sub>x<sup>3</sup> + a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub> + b<sub>0</sub>sin((b<sub>1</sub>x) + b<sub>2</sub>)  a<sub>0…6</sub>: Coefficient of order 0 to 6 of the polynomial  b<sub>0</sub>: Amplitude of the trigonometric portion  b<sub>1</sub>: Period of the trigonometric portion  b<sub>2</sub>: Phase offset of the trigonometric portion |
| Amplitude | Configure the amplitude of the trigonometric component in this field. |  |
| Definition by | In the selection list, select how the trigonometric component is defined:  - Phase at start and at end - Phase at start and period length - Phase at start and frequency - Period length and phase at end - Frequency and phase at end   The corresponding parameters are displayed based on the selection. |  |
| Phase angle at start | Configure the phase angle at the start of the trigonometric component in this field. |  |
| Phase angle at end | Configure the phase angle at the end of the trigonometric component in this field. |  |
| Period length | Configure the period length of the trigonometric component in this field. |  |
| Frequency | Configure the frequency of the trigonometric component in this field. |  |

##### Inserting and configuring an inverse sine (S7-1500T)

An inverse sine describes a motion according to the arcsine function. The arcsine function is the inverse function of the sine function. An inverse sine is approximated using interpolation points of the arcsine function.

The inverse sine is defined within the definition range [-1, 1]. The inverse sine can be calculated for the entire definition range or a restricted definition range of the arcsine function.

###### Inserting an inverse sine

To add an inverse sine to the curve, follow these steps:

1. On the toolbar, click the ![Inserting an inverse sine](images/165345184395_DV_resource.Stream@PNG-de-DE.png) "Insert inverse sine" icon.
2. In Chart 1, click on the position desired position. In so doing, the mouse pointer points to the start position of the inverse sine.

   The sine is inserted. The coordinates are displayed for the point. The tabular editor and the view of the properties (Inspector window) are updated. A transition to any element is inserted automatically.

###### Adjusting an inverse sine

To adjust an inverse sine in the graphical editor, follow these steps:

1. On the toolbar, click the icon ![Adjusting an inverse sine](images/165344566027_DV_resource.Stream@PNG-de-DE.png) "Edit elements/Move view".
2. Select the inverse sine in chart 1.

   The inverse sine is graphically highlighted with drag handles. The following drag handles are displayed:

   - Start point of the inverse sine
   - End point of the inverse sine
3. Use the drag-and-drop feature to move the handles or the entire inverse sine to the desired position.

###### Adapting parameters

The parameters of the inverse sine can be adjusted in the graphical editor, in the tabular editor as well as in the inspector window under "Properties > Element > Parameter".

Configure the parameters of the selected inverse sine in this area:

| Parameters |  | Description |
| --- | --- | --- |
| Leading values of the inverse sine |  |  |
|  | Start | Configure the start point of the inverse sine in the leading value range (definition range) in this field. |
| End | Configure the end point of the inverse sine in the leading value range (definition range) in this field. |  |
| Following values of the inverse sine |  |  |
|  | Minimum | Configure the minimum value of the inverse sine in the following value range (value range) in this field. |
| Maximum | Configure the maximum value of the inverse sine in the following value range (value range) in this field. |  |
| Definition range |  |  |
|  | Not mirrored/mirrored | Select whether or not the inverse sine is to be mirrored about the abscissa. |
| Start | Configure the start point in the definition range of the arcsine function that is to be used in this field. |  |
| End | Configure the end point in the definition range of the arcsine function that is to be used in this field. |  |
| Approximation |  |  |
|  | Number of interpolation points | Configure the number of interpolation points for the approximation in this field. |
| Maximum following value tolerance | In this field, specify the maximum permitted deviation (absolute) of the approximation from the arcsine function.  If the configured value is exceeded, a warning is displayed in the graphical editor for the arcsine element. |  |

##### Inserting elements from the clipboard (S7-1500T)

###### Insert element after the last element

To insert an element from the clipboard after the last element, follow these steps:

1. Open the shortcut menu in graphic or tabular editor.
2. Select "Insert" from the shortcut menu entry.

   The element from the clipboard is inserted after the last element.

###### Insert element using insert mode

To insert an element from the clipboard using a selected insert mode, follow these steps:

1. If necessary, select the elements to be overwritten.
2. Open the shortcut menu in graphic or tabular editor.
3. Select the "Insert special" entry from the shortcut menu.

   The "Insert elements" dialog opens.
4. In the "Insert mode" selection list, select the desired insert mode:

   | Insert mode | Description |
   | --- | --- |
   | Overwrite from the end to the left | You overwrite the selected elements with the elements from the clipboard starting from the end in the direction of smaller leading values. The end of the inserted elements then lies at the end of the selected elements.  Elements that are located in the leading value range of the elements in the clipboard are overwritten or truncated. |
   | Overwrite from the start to the right | You overwrite the selected elements with the elements from the clipboard starting from the start in the direction of bigger leading values. The start of the inserted elements then lies at the start of the selected elements.  Elements that are located in the leading value range of the elements in the clipboard are overwritten or truncated. |
   | Overwrite from the middle | Starting from the center, you overwrite the selected elements with the elements from the clipboard. The center of the inserted elements then lies at the center of the selected elements.  Elements that are located in the leading value range of the elements in the clipboard are overwritten or truncated. |
   | Scale selection to the leading value range | The elements in the clipboard are scaled to the leading value range of selected elements. The start and end of the inserted elements then lie at the start and end of the selected elements. |
   | Apply leading values from the clipboard | The elements in the clipboard are inserted with the leading values at the start and end.  Elements that are located in the leading value range of the elements in the clipboard are overwritten or truncated. |
5. Click "OK".

   The element from the clipboard is inserted using the selected insert mode.

##### Move elements (S7-1500T)

To move an element, follow these steps:

1. In the graphical or tabular editor, open the shortcut menu of the element that is to be moved.
2. Select the "Move" shortcut menu entry.

   The "Move elements" dialog opens.
3. In the "Horizontal distance" field, enter the shift of the selection on the abscissa (x-axis).
4. In the "Vertical distance" field, enter the shift of the selection on the ordinate (y-axis).
5. Click "OK".

   The element is moved the entered distance.

##### Scale elements (S7-1500T)

To scale an element, follow these steps:

1. In the graphical or tabular editor, open the shortcut menu of the element that is to be scaled.
2. Select the "Scale" shortcut menu entry.

   The "Scale elements" dialog opens.
3. In the "Leading value range" field, enter the scaling length (leading value side) to which you want to scale the selection.
4. Select the direction of scaling in the "Anchor point" selection list:

   | Direction | Description |
   | --- | --- |
   | Links | The selection is adjusted by the left boundary point to the scaling length. |
   | Center | The selection is adjusted by the center point to the scaling length. |
   | Right | The selection is adjusted by the right boundary point to the scaling length. |
5. Click "OK".

   The element is scaled using the selected parameter values.

##### Deleting elements (S7-1500T)

To delete an element in the graphical editor, follow these steps:

1. Select the element that is to be deleted.
2. Press the <Del> key.

   The element is deleted. The graphical editor and the view of the properties (Inspector window) are updated. A transition to any element present is also deleted.

##### Show elements used (S7-1500T)

The "Statistics" properties window shows an overview of the number of elements of the cam, as well as the minimum and maximum values of the effective curves for the slave value and the derivatives.

###### Used elements

In the statistics, a distinction is made between points and segments:

- Point  
  A following value/leading value coordinate on the cam through which the curve runs
- Segments  
  All elements and transitions that are calculated by a 6th degree polynomial with a trigonometric component

The "Elements used" area shows the number of curve elements used:

| Parameters | Description |
| --- | --- |
| Points | This field shows the number of used points of the cam.  A cam of the type "TO_Cam" consists of a maximum of 1000 points.  A cam of the type "TO_Cam_10k" consists of a maximum of 10 000 points. |
| Segments | This field shows the number of used segments of the cam.  A cam consists of a maximum of 50 segments. |

The use of points and segments depends on the compilation and configuration of the elements.

If an element or a transition is defined via a point or several interpolation points, the number of specified interpolation points determines the number of points used. The following elements or transitions are calculated using interpolation points:

- "Point" element
- "Inverse sine" element
- "Point group" element with "Point approximation" mapping option
- "Double-harmonic transition" motion rule according to VDI Guideline

All other elements and transitions according to the VDI guideline are defined using 6th degree polynomials with a trigonometric component and thus count as segments in the statistics.

The following table shows the use of points and segments per element:

| Element |  |  |  |  | Number of used points | Number of used segments |
| --- | --- | --- | --- | --- | --- | --- |
| Point |  |  |  |  | 1 | 0 |
| Point at a transition with VDI-based optimization |  |  |  |  | 0 | 0 |
| Point group with point approximation mapping method |  |  |  |  | Number of interpolation points configured.  ("Properties (Inspector window) > Element > Parameter > Approximation > Number of interpolation points")  Default setting: 32 | 0 |
| Point group with segment approximation mapping method |  |  |  |  | 0 | Number of interpolation points configured - 1 |
| Line |  |  |  |  | 0 | 1 |
| Sine |  |  |  |  | 0 | 1 |
| Polynomial |  |  |  |  |  |  |
|  | < of the 7th degree |  |  |  | 0 | 1 |
| of the 7th degree |  |  |  | 0 | 2 |  |
| Inverse sine |  |  |  |  | Number of interpolation points configured.  ("Properties (Inspector window) > Element > Parameter > Approximation > Number of interpolation points")  Default setting: 32 | 0 |
| Inverse sine to the right of a transition with VDI-based optimization |  |  |  |  | Number of interpolation points configured - 1 | 0 |
| Transition with system interpolation |  |  |  |  | 0 | 0 |
| Transition with VDI-based optimization |  |  |  |  |  |  |
|  | Motion rule |  |  |  |  |  |
|  | Sine |  |  | 0 | 1 |  |
| Sine with relative Lambda ≠ 0.5 |  |  | 0 | 2 |  |  |
| Inclined sine |  |  | 0 | 1 |  |  |
| Inclined sine with relative Lambda ≠ 0.5 |  |  | 0 | 2 |  |  |
| Polynomial |  |  | 0 | 1 |  |  |
| Sinus with relative Lambda ≠ 0.5 |  |  | 0 | 2 |  |  |
| Modified acceleration trapezoid |  |  |  |  |  |  |
|  | Motion task |  |  |  |  |  |
|  | Dwell-in-reverse | 0 | 5 |  |  |  |
| Reverse-in-dwell | 0 | 5 |  |  |  |  |
| Dwell-in-dwell | 0 | 6 |  |  |  |  |
| Modified sine |  |  |  |  |  |  |
|  | Motion task |  |  |  |  |  |
|  | Dwell-in-dwell | 0 | 3 |  |  |  |
| Constant velocity-in-constant velocity | 0 | 4 |  |  |  |  |
| Constant-velocity-in-dwell | 0 | 4 |  |  |  |  |
| Dwell-in-constant velocity | 0 | 4 |  |  |  |  |
| Sine line combination |  |  | 0 | 3 |  |  |
| Harmonic combination |  |  | 0 | 3 |  |  |
| Double-harmonic transition |  |  | Number of interpolation points configured.  ("Properties (Inspector window) > Element > Parameter > Approximation > Number of interpolation points")  Default setting: 32 | 0 |  |  |
| Quadratic parabola |  |  | 0 | 2 |  |  |
| Lambda = turning point of the curve |  |  |  |  |  |  |

###### Value ranges

This area shows the minimum and maximum values of the effective curves for the following value and the derivatives.

###### Boundary conditions

The following boundary conditions apply to the input and use of points and segments:

- **Points**

  With points with the same leading values, the point that you have entered last or which is listed in the tabular editor is active.
- **Segments**

  - Gaps between segments are filled with a transition segment.
  - For gaps in the leading value range of less than 1.0E-4, segment end points and segment start points are pulled together.
  - For gaps in the leading value range greater than 1.0E-4, a new transition segment is inserted.
  - For overlaps, the new segment is inserted from the start point and used completely. When the previous segment is defined in excess of the new segment, the previous segment continues to be used after the end point of the new segment.
- **Interpolation points and segments** (mixed cams)

  The segment is used when points are defined in the same range.

#### Transferring the synchronous operation function of the cam to the technology object data block (S7-1500T)

After you have configured the synchronous operation function of the cam in the cam editor, compile the cam technology object. By compiling, the configuration is transferred from the cam editor to the technology object data block of the cam. All existing values are overwritten.

##### Requirement

- You have defined the synchronous operation function of the cam in the cam editor or imported it.

##### Procedure

To transfer the synchronous operation function of the cam to the technology object data block, follow the steps below:

1. Select the can technology object in the project tree.
2. Select the "Compile > Software (only changes)" entry in the shortcut menu.

##### Result

The configuration of the synchronous operation function is transferred from the cam editor to the technology object data block of the cam. All existing values are overwritten.

#### Importing/exporting cam (S7-1500T)

Use the toolbar to export cams from the cam editor and import cams into the cam editor.

In the cam diagnostics you export and import snapshots of cams.

You can do the following jobs via export and import:

- Archive cams
- Generate cam in the cam editor from an exported snapshot of a cam generated during runtime
- Exchange cams between TIA Portal and external software tools

##### Importing cam

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Machine damage**  Importing corrupt files (*.txt, *.csv) can result in unwanted behavior of the axes.  Each time you import a cam from a file, check the integrity of the imported data. |  |

**Import formats**

The following table shows the supported file formats for importing a cam:

| File format | Comment |
| --- | --- |
| SIMOTION SCOUT CamTool format<sup>1)</sup>/MCD *.txt | MCD exchange format is automatically detected, imported data:  - Interpolated points - Lines - Sine elements - Inverse sine elements - Polynomials - Transitions |
| SIMOTION SCOUT CamTool format<sup>1)</sup>/MCD *.csv |  |
| Binary format  *.bin | The binary format is used for exchanging cams between multiple TIA Portal installations. |
| <sup>1) </sup>Export the geometry "as polynomials" in SIMOTION SCOUT. |  |

**Procedure**

To import a cam, follow these steps:

1. On the toolbar, click the ![Importing cam](images/165344866187_DV_resource.Stream@PNG-de-DE.png) "Import cam from file" icon.

   The "Cam import" dialog opens.
2. Select the file type of the file to be imported.
3. From the file directory, select the file to be imported.
4. Click the "Open" button.

   The cam is imported into the cam editor and opened. All previous entries in the editor are discarded.
5. [Compile the cam technology object](#transferring-the-synchronous-operation-function-of-the-cam-to-the-technology-object-data-block-s7-1500t).

   The configuration from the cam editor is transferred to the technology object data block. All existing values are overwritten.

##### Exporting cam

**Export formats**

The table below shows the supported export formats, their use and special features:

| Format | Comment |
| --- | --- |
| MCD exchange format | Exchange of cams between the TIA Portal and the NX Mechatronics Concept Designer  The following elements are exported in a different form, while maintaining the profile of the cam:  - Polynomial of the 7th degree   The format does not support 7th degree polynomials. You can define polynomials of the 7th degree using boundary values in the cam editor. If you configure all three derivatives at the right and left boundary values, which corresponds to a 7th degree polynomial. A 7th degree polynomial is mapped into two 6th degree polynomials during export. - Point group   With the "Point group" element, the export depends on the mapping method. With the "Point approximation" mapping method, the interpolation points are exported and the transitions between the points are interpolated with the system interpolation. With the "Segment approximation" mapping method, the point group is exported in segments. - Inverted sine   The "Inverted sine" element is exported using interpolation points. |
| SIMOTION SCOUT CamTool format | Exchange of cams between the TIA Portal and the SIMOTION SCOUT CamTool  The same special features apply to this format as to the MCD Exchange format. |
| Point list | Export cams as x and y values for processing in, for example, spreadsheet or word processing programs  With the point list, you export points at isochronous distances from the leading value. In addition to the following values, you also have the option to export velocity, acceleration and jerk. Select as many points as possible in order to export the cam with a high degree of accuracy. |
| Binary format | Exchange of cams between multiple TIA Portal projects.  With the binary format you export all configuration data of the cam without restrictions. In addition, your settings for the displaying the charts, such as colors of the curves, are exported. |

**Procedure**

To export a cam, follow these steps:

1. On the toolbar, click the ![Exporting cam](images/165344870155_DV_resource.Stream@PNG-de-DE.png) "Cam file exporting" icon.

   The "Export cam" dialog opens.
2. Select the desired export format from the "Export as" drop-down list.
3. Select the desired delimiter:

   - When you select the "Comma" delimiter, a CSV file is created.
   - When you select the "Tabulator" delimiter, a TXT file is created.
   - This selection is not possible for the binary format.
4. If you export the cam as a point list, enter the number of points and optionally activate the curves to be exported for velocity, acceleration and jerk.

   The more points you export, the more accurately the point list maps the configured cam.
5. Enter a file name in the "File name" box.
6. Select the directory to which the file is written.
7. Click the "Export" button.

### Changing the synchronous operation function of the cam online (S7-1500T)

This section contains information on the following topics:

- [Changing the synchronous operation function of the cam online - short description (S7-1500T)](#changing-the-synchronous-operation-function-of-the-cam-online---short-description-s7-1500t)
- [Changing the synchronous operation function of the cam manually (S7-1500T)](#changing-the-synchronous-operation-function-of-the-cam-manually-s7-1500t)
- [Copy calculated cam elements (S7-1500T)](#copy-calculated-cam-elements-s7-1500t)
- [Creating the synchronous operation function of the cam with the "LCamHdl" library (S7-1500T)](#creating-the-synchronous-operation-function-of-the-cam-with-the-lcamhdl-library-s7-1500t)
- [Transferring the synchronous operation function of the cam defined online to the offline project (S7-1500T)](#transferring-the-synchronous-operation-function-of-the-cam-defined-online-to-the-offline-project-s7-1500t)

#### Changing the synchronous operation function of the cam online - short description (S7-1500T)

You can configure the y = f(x) function of the cam using the cam editor in the [configuration of the technology object](#configuring-the-synchronous-operation-function-of-the-cam-s7-1500t). Alternatively, for dynamic cam plate calculations, you can define or change the synchronous operation function of the cam during the runtime of the user program. The cam technology object must already be created for this.

To change the synchronous operation function of a cam online, you have the following options:

- [Changing the synchronous operation function of the cam manually](#changing-the-synchronous-operation-function-of-the-cam-manually-s7-1500t)
- [Copy calculated cam elements](#copy-calculated-cam-elements-s7-1500t)
- [Creating the synchronous operation function of the cam with the "LCamHdl" library](#creating-the-synchronous-operation-function-of-the-cam-with-the-lcamhdl-library-s7-1500t)

Then, you can transfer the [synchronous operation function of the cam defined online to the offline project](#transferring-the-synchronous-operation-function-of-the-cam-defined-online-to-the-offline-project-s7-1500t).

#### Changing the synchronous operation function of the cam manually (S7-1500T)

The following [tags of the technology object data block](#tags-of-the-cam-technology-object-s7-1500t) of the cam are relevant for defining the synchronous operation function of a cam manually in runtime:

- <TO>.Point[i]
- <TO>.ValidPoint[i]
- <TO>.Segment[i]
- <TO>.ValidSegment[i]
- <TO>.InterpolationSettings

You can adapt the tags in runtime via the user program. You can use the "<TO>.ValidPoint[i]" and "<TO>.ValidSegment[i]" tags to determine which cam elements included for the interpolation. If the value is "TRUE", the element "<TO>.Point[i]" or "<TO>.Segment[i]" with the corresponding index "i" is included in the interpolation. You can determine the [interpolation type](#interpolate-cam-with-mc_interpolatecam-s7-1500t) using the "<TO>.InterpolationSettings" tag.

##### Requirement

- The cam technology object has been created. Configuration via the cam editor is not required.
- The project is downloaded to the CPU.
- The cam elements to be adapted should not be edited by an active copy operation of an "[MC_CopyCamData](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_copycamdata-copy-calculated-cam-elements-v8-s7-1500t)" job.

##### Procedure

To manually change the synchronous operation function of a cam in runtime, follow these steps:

1. Calculate the points and segments of the cam depending on your application.
2. Define the calculated points in the technology object data block of the cam.

   `<TO>.Point[i] := Point; // data type TO_Cam_Struct_PointData`
3. Set the defined points to valid.

   `<TO>.ValidPoint[i] := TRUE;`
4. Set all undefined points to invalid.

   `<TO>.ValidPoint[i] := FALSE;`
5. Define the calculated segments in the technology object data block of the cam.

   `<TO>.Segment[i] := Segment; // data type TO_Cam_Struct_SegmentData`
6. Set the defined segments to valid.

   `<TO>.ValidSegment[i] := TRUE;`
7. Set all undefined segments to invalid.

   `<TO>.ValidSegment[i] := FALSE;`
8. Make the interpolation settings of the cam.

   `<TO>.InterpolationSettings.InterpolationMode := 1;`

   `<TO>.InterpolationSettings.BoundaryConditions := 0;`

   The values "1" and "0" are only used as examples. Adapt them as needed.
9. Interpolate the cam with a "[MC_InterpolateCam](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_interpolatecam-interpolate-cam-v8-s7-1500t)" job.

##### Check the synchronous operation function of the cam

Use the [cam diagnostics](#cam-technology-object-s7-1500t-1) to analyze and check the generated cam. This provides you with a graphical view of the cam, a list of all valid cam elements and the interpolation type.

#### Copy calculated cam elements (S7-1500T)

You use an "[MC_CopyCamData](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_copycamdata-copy-calculated-cam-elements-v8-s7-1500t)" job to copy calculated cam elements to a cam. You can use the same job to copy points and segments to the technology object data block of the cam.

##### Cam elements to be copied

Save or calculate the cam elements in a data block. Create an array for points of the "TO_Cam­_Struct­_Point­Data" type and an array for segments of the "TO_Cam­_Struct­_Segment­Data" type. The size of the arrays depends on the use case and is variable.

The consistency of the cam elements in the data block is your responsibility. The cam elements must not change during an active copy operation of an "MC_CopyCamData" job.

Specify the arrays for points and segments at the "ArrayOfPoints" and "ArrayOfSegments" parameters of the "MC_CopyCamData" job. Define the number of elements to be copied at the "NumberOfPoints" and "NumberOfSegments" parameters.

Use the "StartPointArray" and "StartSegmentArray" parameters to define the index of the first element to be copied in the array, respectively. Use the "StartPointCam" and "StartSegmentCam" parameters to define the respective index in the cam starting at which the elements to be copied are to be inserted.

##### Copy mode

Following the copy operation, the inserted cam elements are set as valid ("ValidPoint" = TRUE, "ValidSegment" = TRUE).

With copy mode "Mode" = 0, you specify that all defined elements already present in the cam are set as invalid before the copy operation ("ValidPoint" = FALSE, "ValidSegment" = FALSE). This results in only the inserted elements being valid after the copy operation. Use this copy mode to completely regenerate the cam and overwrite its previous synchronous operation function.

Use copy mode "Mode" = 1 to specify that all defined elements already present in the cam remain valid ("ValidPoint" = TRUE, "ValidSegment" = TRUE). This results in both the inserted elements and the still existing elements not overwritten being valid after the copy operation. Use this copy mode to append cam elements to the previous synchronous operation function of the cam, or to partially overwrite the synchronous operation function of cam.

##### Copy operation

Copying of cam elements is possible during active cam synchronization.

An active copy operation is indicated by the "MC_CopyCamData.Busy" = TRUE parameter, in the "<TO>.StatusWord.X7 (CopyCamDataActive)" tag as well as in the status and error bits of the diagnostics of the technology object. Only one active "MC_CopyCamData" job is possible at a given time on a cam.

As soon as the cam elements have been copied and set to valid, the copy operation is complete. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE. The "<TO>.StatusWord.X4 (CamDataChanged)" tag of the technology object is set to "TRUE".

Before you can use the cam with the inserted elements, the cam must be interpolated. To do this, start an "MC_InterpolateCam" job.

#### Creating the synchronous operation function of the cam with the "LCamHdl" library (S7-1500T)

The "LCamHdl" library provides function blocks that support you in creating jerkless cams in accordance with VDI guideline 2143. The function blocks perform the required calculations of the segments for different profile types, e.g. the polynomial coefficients.

In addition, you can use the optimized "Basic" function block with a simplified user interface to define the synchronous operation function of the cam in terms of points and associated dynamic values. From this, the function block calculates the corresponding segments according to a 5th degree polynomial function.

##### More information

You can find additional information about the "LCamHdl" library in the Siemens Industry Online Support under entry ID [105644659](https://support.industry.siemens.com/cs/ww/en/view/105644659).

An application example shows the creation of cams with the "LCamHdl" library and switching of two cams using the example of a press. The application example can be found in the Siemens Industry Online Support under entry ID [109749460](https://support.industry.siemens.com/cs/ww/en/view/109749460).

#### Transferring the synchronous operation function of the cam defined online to the offline project (S7-1500T)

After you have defined or changed the synchronous operation function of the cam at runtime of the user program, you can transfer the synchronous operation function to the offline project. To do this, use the cam diagnostics.

##### Requirement

- You have adapted the synchronous operation function of a cam online.
- The current cam data is contained in the technology object data block.

##### Procedure

To transfer the adapted synchronous operation function of the cam to the offline project, follow the steps below:

1. Open the cam diagnostics.
2. [Save a snapshot of the online configuration of the cam](#managing-snapshots-s7-1500t).
3. [Export the saved snapshot in binary format](#exporting-and-importing-snapshots-s7-1500t).
4. Open the cam configuration.
5. [Import the exported snapshot of the cam](#importingexporting-cam-s7-1500t).
6. [Compile the cam technology object](#transferring-the-synchronous-operation-function-of-the-cam-to-the-technology-object-data-block-s7-1500t).

   The configuration from the cam editor is transferred to the technology object data block of the cam. All existing values are overwritten.

   An online/offline inconsistency is displayed for the Cam technology object because the start values differ.
7. Load the Cam technology object to the CPU again.

##### Result

You have transferred the synchronous operation function of the cam defined online to the offline project.

### Interpolating a cam (S7-1500T)

This section contains information on the following topics:

- [Configuring transitions (S7-1500T)](#configuring-transitions-s7-1500t)
- [System interpolation (S7-1500T)](#system-interpolation-s7-1500t)
- [Interpolation according to VDI Guideline 2143 (S7-1500T)](#interpolation-according-to-vdi-guideline-2143-s7-1500t)
- [Interpolate cam with "MC_InterpolateCam" (S7-1500T)](#interpolate-cam-with-mc_interpolatecam-s7-1500t)

#### Configuring transitions (S7-1500T)

To use a cam in the user program, you must interpolate the cam after downloading to the CPU or after adapting the technology object data block. The interpolation closes the gaps between the defined interpolation points and segments of the cam. These missing ranges are called transitions. The interpolation type defines how the transitions are interpolated.

##### Configuring interpolation

You specify the interpolation type in the configuration of the technology object. You can set the interpolation separately for each transition in the cam. The following methods are possible:

- [System interpolation](#system-interpolation-s7-1500t):

  The system interpolation is the default for interpolation of the transitions. You configure the system interpolation for all transitions in the properties (Inspector window) in the "Profile > System interpolation" configuration window.
- [Interpolation according to VDI Guideline 2143](#interpolation-according-to-vdi-guideline-2143-s7-1500t):

  You can adapt each transition separately according to the VDI Guideline 2143. The settings in the properties (Inspector window) in the "Profile > Default optimization settings" configuration window are hereby taken into consideration.

##### "Characteristic" configuration window

In the "Characteristic" configuration window, you configure the parameters for optimizing the selected transition in the properties (Inspector window):

| Parameters |  |  | Description |
| --- | --- | --- | --- |
| Interpolation settings of the transition |  |  |  |
|  | Optimization method |  | Select the optimization method in the drop-down list:  - [System interpolation](#system-interpolation-s7-1500t)    The CPU defines the optimization parameters automatically according to the settings of the system interpolation. - [VDI-based optimization](#interpolation-according-to-vdi-guideline-2143-s7-1500t)    Adjust the optimization manually. The inputs are applied automatically according to the VDI Guideline 2143. |
| Motion task |  | The transition type is determined from the properties of the adjacent elements of the transition and displayed in this field. |  |
| Continuity at start/end |  | In the drop-down lists, select which parameter is continuous in the boundary points and is to be included for optimization:  - Default optimization setting (setting under "Profile > Default optimization settings") - Position - Velocity (bumpless) - Acceleration (jerkless) - Jerk (jerk continuity permitted on one side only) |  |
| Optimization target |  | In the drop-down list, select the optimization target:  - Default optimization setting (setting under "Profile > Default optimization settings") - Not specified - Velocity (Cv) - Acceleration (Ca) - Jerk (Cj) - Dynamic torque (Cmdyn) |  |
| Selection of motion rule |  |  |  |
|  | Motion rule |  | In the drop-down list, select the motion rule according to which optimization is to occur:  - Line - Quadratic parabola - Sine - Polynomial - Inclined sine - Modified acceleration trapezoid - Modified sine - Harmonic combination - Double-harmonic transition - Sine line combination   The selection is automatically limited to the motion rules that can be applied according to the motion task and the selected boundary conditions. Additional parameters are displayed depending on the selected motion rule.  If you have changed the motion task in such a way that the motion rule can no longer be applied, a notice is displayed. In this case, you need to select a motion rule that can be applied. |
| Parameter used |  | In the drop-down list, select the parameters to be included in the optimization:  - Lambda - Maximum acceleration (Ca) - Maximum deceleration (Ca*)   The selection is automatically limited to the parameters that can be applied according to the motion rule. |  |
| Lambda |  | In the drop-down list, select the transition point in the "Lambda position" field:  - No lambda   Do not enter any value. The position of the point of inflection is calculated automatically. - Relative to segment   Specify the leading value of the point of inflection relative to the transition from 0.0 to 1.0. The value 0.0 corresponds to the beginning of the transition. The value 1.0 corresponds to the end of the transition. - Absolute in the profile   You specify the leading value of the point of inflection as an absolute value. |  |
| Lambda position |  | In this field, configure the leading value of the point of inflection for the transition according to the selection in the "Lambda" drop-down list. |  |
| Maximum acceleration (Ca) |  | Configure the maximum acceleration (Ca) for the transition in this field. |  |
| Maximum deceleration (Ca*) |  | Configure the maximum deceleration (Ca*) for the transition in this field. |  |
| Approximation |  |  |  |
|  | Number of interpolation points | In this field, configure the number of interpolation points for the transition. |  |
| Maximum following value tolerance | In this field, enter the maximum permitted deviation (absolute) of the approximation from the motion rule.  If the configured value is exceeded, a warning is displayed in the graphical editor at the transition. |  |  |
| Characteristic values of the transition |  |  | The characteristic values of the transition that are relevant according to VDI 2143 are displayed in this area. The maximum value and the standardized value are displayed for the following characteristic values:  - Velocity (Cv) - Acceleration (Ca) - Deceleration (Ca*) - Jerk (Cj) - Dynamic torque (Cmdyn) |

#### System interpolation (S7-1500T)

With system interpolation, the transitions are interpolated according to the interpolation type and the response in the boundary points of the transition segment. The following interpolation methods are possible:

- **Linear interpolation**

  Gaps in the curve are closed with a straight line.

  ![Figure](images/165345313803_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ![Figure](images/165345317771_DV_resource.Stream@PNG-de-DE.png) | Specified position (point) |
  | ![Figure](images/165345321739_DV_resource.Stream@PNG-de-DE.png) | Interpolated position |
  | ![Figure](images/165345325707_DV_resource.Stream@PNG-de-DE.png) | Resulting velocity (scaled) |
  | ![Figure](images/165345329675_DV_resource.Stream@PNG-de-DE.png) | Resulting acceleration |
  | ![Figure](images/165345333643_DV_resource.Stream@PNG-de-DE.png) | Resulting jerk |
- **Interpolation with cubic splines**

  The interpolated curve runs through the interpolation points and the segments of the curve.

  After interpolation has been completed, the value range of the following value of the cam can be greater than before interpolation.

  ![Figure](images/165345350411_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ![Figure](images/165345317771_DV_resource.Stream@PNG-de-DE.png) | Specified position (point) |
  | ![Figure](images/165345321739_DV_resource.Stream@PNG-de-DE.png) | Interpolated position |
  | ![Figure](images/165345325707_DV_resource.Stream@PNG-de-DE.png) | Resulting velocity (scaled) |
  | ![Figure](images/165345329675_DV_resource.Stream@PNG-de-DE.png) | Resulting acceleration (scaled) |
  | ![Figure](images/165345333643_DV_resource.Stream@PNG-de-DE.png) | Resulting jerk (scaled) |
- **Interpolation with Bézier splines**

  The interpolated curve runs along the interpolation points and through the segments of the curve.

  The range of the cam is not changed by interpolation.

  ![Figure](images/165345354379_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ![Figure](images/165345317771_DV_resource.Stream@PNG-de-DE.png) | Specified position (point) |
  | ![Figure](images/165345321739_DV_resource.Stream@PNG-de-DE.png) | Interpolated position |
  | ![Figure](images/165345325707_DV_resource.Stream@PNG-de-DE.png) | Resulting velocity (scaled) |
  | ![Figure](images/165345329675_DV_resource.Stream@PNG-de-DE.png) | Resulting acceleration (scaled) |
  | ![Figure](images/165345333643_DV_resource.Stream@PNG-de-DE.png) | Resulting jerk (scaled) |

> **Note**
>
> **Differences in the interpolation types**
>
> Depending on the definition of the cam, high dynamic responses can result when interpolating with cubic splines, as the interpolated curve always runs through the specified points. The course of the curve for interpolation via cubic splines runs through all specified points, while the course of the curve for interpolation via Bézier splines is only based on the points and thus results in lower dynamic values.
>
> If required, select an interpolation using Bézier splines in order to obtain a smooth, slower interpolated curve.

##### "System interpolation" configuration window

In the "System interpolation" configuration window, configure the interpolation of transitions according to the system specifications in the properties (Inspector window). These settings are used when the "System interpolation" optimization method is used for a [transition](#configuring-transitions-s7-1500t) (default setting).

Configure the interpolation type and the behavior of the boundary points in this area:

| Parameter | Description |
| --- | --- |
| Interpolation type | In the drop-down list, select the interpolation type by which the transitions in the curve are interpolated:  - Linear interpolation In linear interpolation, the transitions (magenta) between the cam elements (blue) are defined by a straight line. - Interpolation with cubic splines In the interpolation with cubic splines, the transitions (magenta) between the cam elements (blue) are defined so that the interpolated curve runs through all the cam elements. The acceleration (green) in the transition is linear. - Interpolation with Bézier splines In the interpolation with Bézier splines, the transitions (magenta) between the cam elements (blue) are defined so that the interpolated curve is based on specified points and the curve runs through other cam element types. |
| Behavior at boundary | In the drop-down list, select which behavior of the interpolation applies to a cyclic use of the cam in the boundary points:  - No restrictions The areas between the elements are closed. - First derivative continuous (velocity continuous)   The cam is interpolated in such a way that the first derivative (velocity) is equal at the start and end of the cam. |

---

**See also**

[MC_InterpolateCam: Interpolate cam V8 (S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_interpolatecam-interpolate-cam-v8-s7-1500t)

#### Interpolation according to VDI Guideline 2143 (S7-1500T)

The VDI Guideline 2143 deals with motion rules for cam gears. The aim of these motion rules is to achieve high running quality and to avoid jolts and jerks.

The VDI Guideline 2143 distinguishes between areas of usage and motion transitions:

- Areas of usage correspond to the sequences in a process, which means the inserted elements of the cam.
- Motion transitions are transitions between areas of usage that are not directly relevant to the process but must meet specific boundary conditions, for example, velocity consistency.

The following motion tasks are defined based on VDI Guideline 2143:

| Motion task | Designation | Properties |
| --- | --- | --- |
| Dwell | R | Velocity = 0  Acceleration = 0 |
| Constant velocity | G | Velocity ≠ 0  Acceleration = 0 |
| Reverse | U | Velocity = 0  Acceleration ≠ 0 |
| Motion | B | Velocity ≠ 0  Acceleration ≠ 0 |

The graphic below shows an example of the motion jobs:

![Figure](images/165345358347_DV_resource.Stream@PNG-de-DE.png)

The following graphic shows the possible combinations of motion jobs:

![Figure](images/165345388939_DV_resource.Stream@PNG-de-DE.png)

##### Adjust the optimization of a transition

To adapt the optimization of a transition according to the VDI Guideline 2143, follow these steps:

1. Select the transition in the graphical or tabular editor.
2. In the properties (Inspector window), open the "[Element > Characteristic](#configuring-transitions-s7-1500t)" configuration window.
3. Select the optimization method "VDI-based optimization" in the "Optimization method" drop-down list.
4. If necessary, change the default settings.

   The selection of the parameters is automatically limited to the settings that can be applied according to VDI Guideline 2143.

You interpolate the cam with the Motion Control instruction "[MC_InterpolateCam](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_interpolatecam-interpolate-cam-v8-s7-1500t)" according to the settings for the VDI optimization. Note that, in contrast to system interpolation, the optimization of transitions according to VDI Guideline 2143 directly occupies segments in the technology object data block. This optimization type is thus not possible via "MC_InterpolateCam" during runtime.

##### "Default optimization settings" configuration window

You configure the default values for optimization of transitions according to VDI Guideline 2143 in the "Profile > Default optimization settings" configuration window in the properties (Inspector window). The default values are used when the "VDI-based optimization" optimization method is selected for a [transition](#configuring-transitions-s7-1500t) and when the setting "Default optimization setting" is selected for the continuity or the optimization target.

Configure the default settings for continuity requirement and optimization target in this area:

| Parameter | Description |
| --- | --- |
| Continuity | In the drop-down list, select which parameter is continuous in the boundary points and is to be taken into consideration for optimization:  - Position - Velocity - Acceleration - Jerk |
| Optimization target | In the drop-down list, select the optimization target according to the VDI Guideline:  - Not specified - Velocity (Cv) - Acceleration (Ca) - Jerk (Cj) - Dynamic torque (Cmdyn) |

#### Interpolate cam with "MC_InterpolateCam" (S7-1500T)

To use a cam in the user program, you must interpolate the cam after downloading to the CPU or after adapting the technology object data block. The interpolation closes the gaps between the defined interpolation points and segments of the cam. The interpolation type defines how missing ranges are interpolated.

> **Note**
>
> **Improving system performance**
>
> To improve the system performance for interpolating the cam technology object, select the "Improve system performance" check box in the properties of MC_Interpolator under "General > Multi-core processor".

After you have configured the [interpolation type](#configuring-transitions-s7-1500t), you interpolate a cam in the user program with the Motion Control instruction "[MC_InterpolateCam](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_interpolatecam-interpolate-cam-v8-s7-1500t)". After starting the "MC_InterpolateCam" job, the cam is interpolated in the definition range from the minimum to the maximum value in the leading value range:

- The minimum value in the leading value range is the first defined interpolation point or start of the first segment of the cam (<TO>.StatusCam.StartLeadingValue).
- The maximum value in the leading value range is the last defined interpolation point or end of the last segment of the cam (<TO>.StatusCam.EndLeadingValue).

As soon as the cam has been interpolated, this is indicated on Motion Control instruction "MC_InterpolateCam" with parameter "Done" = TRUE and in tag "<TO>.StatusWord.X5 (Interpolated)" = 1 of the technology object. After interpolation, an explicit value in the value range is assigned to each value in the definition range.

### Scaling and shifting cam (S7-1500T)

You can scale and shift the utilized cam for [camming](#camming-with-mc_camin-s7-1500t) at the Motion Control instruction "MC_CamIn" in the leading and following value range. The configured cam is not changed by this. In contrast, the specification for leading and following value range in the [configuration of the technology object](#configuration-of-profile---general-s7-1500t) only effect the display in the graphical editor.

The following diagram shows the general sequence of scaling and shifting the cam:

![Figure](images/165345394187_DV_resource.Stream@PNG-en-US.png)

Position following axis = f[(Position leading axis - Leading value shift) / Leading value scaling] × Following value scaling + Following value shift

#### Parameter inputs

You define the use of the cam with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the "MasterScaling" parameter, you specify the scaling of the cam in the leading value range. The value "0.0" is invalid.
- With the "SlaveScaling" parameter, you specify the scaling of the cam in the following value range.
- You define the offset of the cam in the leading value range with the parameter "MasterOffset".
- You define the offset of the cam in the following value range with the parameter "SlaveOffset".

#### Scaling of the cam

The figure below shows the basic effect of scaling the cam with the parameters "MasterScaling" and "SlaveScaling":

![Scaling of the cam](images/165345400203_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Scaling of the cam](images/165345558923_DV_resource.Stream@PNG-de-DE.png) | Leading value |
| ![Scaling of the cam](images/165345564043_DV_resource.Stream@PNG-de-DE.png) | Following value |

#### Shifting of the cam

The following figure shows the basic effect of the leading value and following value offset as well as the position of the cam with the following parameter values:

- "MasterOffset" > 0
- "SlaveOffset" > 0
- Start position of the cam > 0
- "MasterSyncPosition" > 0

![Shifting of the cam](images/165345658763_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Start position of the cam  First defined interpolation point/start of the first segment of the cam (<TO>.StatusCam.StartLeadingValue) |
| ② | Leading value distance with synchronization in advance ("MasterStartDistance") |
| ③ | Synchronous position of the leading axis relative to the starting position of the cam ("MasterSyncPosition") |
| ④ | Leading value distance with subsequent synchronization ("MasterStartDistance") |
| ⑤ | End position of the cam   Last defined interpolation point/end of the last segment of the cam (<TO>.StatusCam.EndLeadingValue) |

### Defining application mode of the cam (S7-1500T)

For [camming](#camming-with-mc_camin-s7-1500t), you can define the application mode of the cam. The following modes are available:

- Not cyclic
- Cyclical
- Cyclic appending

A cam is defined between the start position (<TO>.StatusCam.StartLeadingValue) and end position (<TO>.StatusCam.EndLeadingValue) after the [interpolation](#interpolating-a-cam-s7-1500t).

#### Parameter inputs

You define the use of the cam with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the "ApplicationMode" parameter, you define the application mode of the cam.

#### Not cyclic

With the "ApplicationMode" = 0 parameter, you define the application mode of the cam as "Not cyclic".

The cam is run exactly once. When the cam is run through in the positive direction, synchronous operation is ended when the end position of the cam is reached. When the cam is run through in the negative direction, synchronous operation is ended when the start position of the cam is reached.

To prevent step changes in the dynamic values, the velocity of the following axis must be zero at the start and end position of the cam.

![Not cyclic](images/165345664651_DV_resource.Stream@PNG-en-US.png)

#### Cyclical

With the "ApplicationMode" = 1 parameter, you define the application mode of the cam as "Cyclical".

The cam is run cyclically. When the cam is run through in the positive direction, the cam is repeated from the start position when the end position of the cam is reached. When the cam is run through in the negative direction, the cam is repeated from the end position when the start position of the cam is reached.

To prevent step changes in the dynamic values, the start and end positions of the cam must be match, and the velocity at the start and end position must be identical. For a velocity continuous transition, use the setting "First derivative continuous (velocity continuous)" under "Properties (Inspector window) > System interpolation > Behavior at boundary" (<TO>.InterpolationSettings.BoundaryConditions = 1) for interpolation of the cam.

![Cyclical](images/165346157067_DV_resource.Stream@PNG-en-US.png)

#### Cyclic appending

With the "ApplicationMode" = 2 parameter, you define the application mode of the cam as "Cyclic appending".

The cam is run cyclically. When the cam is run through in the positive direction, the end position of the cam is used as the start position for the next run. When the cam is run through in the negative direction, the start position of the cam is used as the start position for the next run. The position difference between the start and end position on the following value side is added up.

To prevent step changes in the dynamic values, the velocity at the start and end position must be identical. For a velocity continuous transition, use the setting "First derivative continuous (velocity continuous)" under "Properties (Inspector window) > System interpolation > Behavior at boundary" (<TO>.InterpolationSettings.BoundaryConditions = 1) for interpolation of the cam.

![Cyclic appending](images/165346163083_DV_resource.Stream@PNG-en-US.png)

### Dynamic limits of the following axis in camming (S7-1500T)

If a synchronous axis is operated as a following axis in camming with the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)", the following dynamic limits apply depending on the phase of the synchronous operation:

#### Pending synchronous operation

If synchronous operation is not active, the configured dynamic limits of the following axis apply. If there is already a synchronous operation active, the descriptions in the following sections apply.

#### Synchronization/desynchronization using dynamic parameters

During synchronization and desynchronization using dynamic parameters with "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)", the dynamic limits configured at the technology object apply to the following axis.

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The SW limit switches also continue to be monitored with the configured dynamic limits of the following axis.

#### Synchronization/desynchronization using leading value distance/synchronous travel

During synchronization and desynchronization using leading value distance with "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)" and during synchronous travel, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The dynamics of the following axis results from the synchronous operation function.

If the dynamic limits configured for the following axis are exceeded, this is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The SW limit switches continue to be monitored with the configured dynamic limits of the following axis.

If the following axis cannot follow the leading value, this results in a following error, which is monitored by the following error monitoring.

#### Synchronous operation override

As soon as synchronous operation [has been overridden](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#override-response-v8-synchronous-operation-jobs-s7-1500-s7-1500t), the dynamic limits configured for the technology object apply to the following axis again. With the start of the overriding job, the active dynamics are transitioned (smoothed) to the configured dynamic limits and the specifications for the Motion Control instruction.

#### More information

You can find more information on dynamic limits in synchronous operation at Siemens Industry Online Support in the FAQ entry [109822283](https://support.industry.siemens.com/cs/ww/en/view/109822283).

### Synchronizing camming (S7-1500T)

This section contains information on the following topics:

- [Parameter overview for synchronizing with "MC_CamIn" (S7-1500T)](#parameter-overview-for-synchronizing-with-mc_camin-s7-1500t)
- [Defining direction of synchronization with "MC_CamIn" (S7-1500T)](#defining-direction-of-synchronization-with-mc_camin-s7-1500t)
- [Synchronizing following axis in advance using dynamic parameters with "MC_CamIn" (S7-1500T)](#synchronizing-following-axis-in-advance-using-dynamic-parameters-with-mc_camin-s7-1500t)
- [Synchronizing following axis in advance using leading value distance with "MC_CamIn" (S7-1500T)](#synchronizing-following-axis-in-advance-using-leading-value-distance-with-mc_camin-s7-1500t)
- [Synchronizing following axis in advance via the leading value path from the current leading value position with "MC_CamIn" (S7-1500T)](#synchronizing-following-axis-in-advance-via-the-leading-value-path-from-the-current-leading-value-position-with-mc_camin-s7-1500t)
- [Subsequent synchronizing of following axis using leading value distance with "MC_CamIn" (S7-1500T)](#subsequent-synchronizing-of-following-axis-using-leading-value-distance-with-mc_camin-s7-1500t)
- [Subsequent synchronizing of following axis using leading axis value starting from the current leading value position with "MC_CamIn" (S7-1500T)](#subsequent-synchronizing-of-following-axis-using-leading-axis-value-starting-from-the-current-leading-value-position-with-mc_camin-s7-1500t)
- [Directly set following axis synchronously with "MC_CamIn" (S7-1500T)](#directly-set-following-axis-synchronously-with-mc_camin-s7-1500t)
- [Directly set following axis synchronously at end of the cam with "MC_CamIn" (S7-1500T)](#directly-set-following-axis-synchronously-at-end-of-the-cam-with-mc_camin-s7-1500t)

#### Parameter overview for synchronizing with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With the parameter "SyncProfileReference" you define the type of synchronization:

| SyncProfileReference | Synchronization profile |
| --- | --- |
| 0 | [Synchronization in advance using dynamic parameters](#synchronizing-following-axis-in-advance-using-dynamic-parameters-with-mc_camin-s7-1500t) |
| 1 | [Synchronization in advance using leading value distance](#synchronizing-following-axis-in-advance-using-leading-value-distance-with-mc_camin-s7-1500t) |
| 2 | [Direct synchronous setting](#directly-set-following-axis-synchronously-with-mc_camin-s7-1500t) |
| 3 | [Subsequent synchronization using leading value distance](#subsequent-synchronizing-of-following-axis-using-leading-value-distance-with-mc_camin-s7-1500t) |
| 4 | [Subsequent synchronization using leading value distance starting from current leading value position](#subsequent-synchronizing-of-following-axis-using-leading-axis-value-starting-from-the-current-leading-value-position-with-mc_camin-s7-1500t) |
| 5 | [Direct synchronous setting at the end of the cam](#directly-set-following-axis-synchronously-at-end-of-the-cam-with-mc_camin-s7-1500t) |
| 6 | [Synchronization in advance using leading value distance starting from current leading value position](#synchronizing-following-axis-in-advance-via-the-leading-value-path-from-the-current-leading-value-position-with-mc_camin-s7-1500t) |

Depending on the synchronization profile, different parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)" are relevant:

| Parameters | SyncProfileReference |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |  |
| MasterOffset | ✓ | ✓ | - | ✓ | ✓ | - | - |
| SlaveOffset | ✓ | ✓ | - | ✓ | ✓ | - | ✓ |
| MasterScaling | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| SlaveScaling | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| MasterSyncPosition | ✓ | ✓ | ✓ | ✓ | - | ✓ | ✓ |
| MasterStartDistance | - | ✓ | - | ✓ | ✓ | - | ✓ |
| Velocity | ✓ | - | - | - | - | - | - |
| Acceleration | ✓ | - | - | - | - | - | - |
| Deceleration | ✓ | - | - | - | - | - | - |
| Jerk | ✓ | - | - | - | - | - | - |
| ApplicationMode | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| SyncDirection | ✓ | ✓ | - | ✓ | ✓ | - | ✓ |

#### Defining direction of synchronization with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. If you have activated the "[Modulo](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#modulo-setting-s7-1500-s7-1500t)" setting for the following axis, you can define the direction of the synchronization with the "SyncDirection" parameter of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)".

![Figure](images/165346632459_DV_resource.Stream@PNG-en-US.png)

##### Positive direction

With "SyncDirection" = 1, the following axis may only travel in positive direction during synchronization. In this example, the synchronous position is 0.0.

![Positive direction](images/165346169099_DV_resource.Stream@PNG-de-DE.png)

##### Negative direction

With "SyncDirection" = 2, the following axis may only travel in negative direction during synchronization. In this example, the synchronous position is 0.0.

![Negative direction](images/165346430219_DV_resource.Stream@PNG-de-DE.png)

##### Shortest distance

With "SyncDirection" = 3, changes in direction of the following axis are permitted during synchronization. In this example, the synchronous position is 90.0.

![Shortest distance](images/165346435339_DV_resource.Stream@PNG-de-DE.png)

#### Synchronizing following axis in advance using dynamic parameters with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. During synchronization in advance using dynamic parameters, synchronization begins in such a way that the leading and following axis are synchronous when the synchronous position is reached.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 0, you define the type of synchronization as synchronization in advance using dynamic parameters.
- With the parameter "MasterSyncPosition", you define the synchronous position of the leading axis relative to the start position of the cam. The synchronous position establishes the relationship between leading value and following value. The synchronous position must be within the definition of the cam. With "MasterSyncPosition" ≠ 0.0, you move the synchronous position within the cam without changing the position of the cam. For synchronization in advance, the synchronous position is the position starting from which the leading and following axes are synchronous.
- With the parameters "Velocity", "Acceleration", "Deceleration" and "Jerk" you define the dynamics for the synchronization of the following axis.

##### Until synchronization

After the start of the "MC_CamIn" job, a motion profile for the following axis is calculated continuously. The motion profile is calculated based on the following parameters:

- Specified synchronous position of the Motion Control instruction
- Specified dynamics of the Motion Control instruction
- Current position and dynamics of the leading and following axes
- Synchronous operation specified via cam

The calculation determines the synchronization length and thus the start position of the leading axis for the synchronization.

The start position of the leading axis is derived in the following way:

Start position = Synchronous position of leading axis - Synchronization length

The status "Waiting" is displayed at the following axis until the leading value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 3).

If the leading axis is already in its synchronous position when the "MC_CamIn" job is started, the leading axis must first cross the start position to start synchronization. If the leading and following axes are already at their synchronous positions when the "MC_CamIn" job is started, synchronous operation immediately has "Synchronous" status.

##### During synchronization

The following axis begins to synchronize as soon as the leading value has reached the start position. The synchronization is indicated in the Motion Control instruction "MC_CamIn" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function.

If the programmed dynamic response of the synchronous operation function is greater than the maximum dynamic response of the following axis, the corresponding technology alarms 501, 502, or 503 are output at the following axis. The synchronization process is only completed when the resulting final velocity is lower than the maximum velocity of the following axis (<TO>.DynamicLimits.MaxVelocity).

##### After synchronization

The following axis is synchronized as soon as the leading axis has reached the synchronous position. [The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

#### Synchronizing following axis in advance using leading value distance with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. During synchronization in advance using the leading value distance, synchronization begins in such a way that the leading and following axis are synchronous when the synchronous position is reached.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 1, you define the type of synchronization as synchronization in advance using the leading value distance.
- With the parameter "MasterSyncPosition", you define the synchronous position of the leading axis relative to the start position of the cam. The synchronous position establishes the relationship between leading value and following value. The synchronous position must be within the definition of the cam. With "MasterSyncPosition" ≠ 0.0, you move the synchronous position within the cam without changing the position of the cam. For synchronization in advance, the synchronous position is the position starting from which the leading and following axes are synchronous.
- With the "MasterStartDistance" parameter, you specify the leading value distance (synchronization length).

##### Until synchronization

After the start of the "MC_CamIn" job, a motion profile is calculated for the following axis depending on the specified leading value distance. The calculation determines the required dynamic response and thus the start position of the leading axis for the synchronization.

The start position of the leading axis is derived in the following way:

Start position = Synchronous position of leading axis - Synchronization length

The leading axis must be at least the leading value distance away from the synchronous position. The status "Waiting" is displayed at the following axis until the leading value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 3).

> **Note**
>
> **Dynamic jumps**
>
> If the following axis is in motion and the leading value is at standstill when the "MC_CamIn" job is started, dynamic jumps can occur at the following axis as soon as the leading axis is set in motion and the following axis starts synchronizing.

If the leading and following axes are already at their synchronous positions when the "MC_CamIn" job is started, synchronous operation immediately has "Synchronous" status.

##### During synchronization

The following axis begins to synchronize as soon as the leading value has reached the start position. The synchronization is indicated in the Motion Control instruction "MC_CamIn" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165346638347_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The dynamic response of the following axis is limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

##### After synchronization

The following axis is synchronized as soon as the leading axis has reached the synchronous position. [The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

#### Synchronizing following axis in advance via the leading value path from the current leading value position with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. For synchronization in advance, the leading value path from the current leading value position begins as soon as the "MC_CamIn" job becomes effective and the leading axis is in motion.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 6, you define the type of synchronization as synchronization in advance via the leading value path from the current leading value position.
- With the parameter "MasterSyncPosition", you define the synchronous position of the leading axis relative to the start position of the cam. The synchronous position establishes the relationship between leading value and following value. The synchronous position must be within the definition of the cam. With "MasterSyncPosition" ≠ 0.0, you move the synchronous position within the cam without changing the position of the cam. For synchronization in advance, the synchronous position is the position starting from which the leading and following axes are synchronous.
- With the "MasterStartDistance" parameter, you specify the leading value distance (synchronization length).
- With the parameter "SlaveOffset" you define the [offset of the cam in the following value range](#scaling-and-shifting-cam-s7-1500t). The offset of the cam in the leading value range is calculated automatically.

##### Until synchronization

After the start of the "MC_CamIn" job, a motion profile is calculated for the following axis depending on the specified leading value distance. The calculation results in the required dynamics and the offset of the cam in the leading value range.

If the leading axis is at a standstill when the job starts, the status "Waiting" is displayed on the following axis (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 3) until the leading axis is set in motion.

> **Note**
>
> **Dynamic jumps**
>
> If the following axis is in motion and the leading value is at standstill when the "MC_CamIn" job is started, dynamic jumps can occur at the following axis as soon as the leading axis is set in motion and the following axis starts synchronizing.

If the leading and following axes are already at their synchronous positions when the "MC_CamIn" job is started, synchronous operation immediately has "Synchronous" status.

##### During synchronization

The following axis begins to synchronize as soon as the "MC_CamIn" job takes effect and the leading axis is moving. The synchronization is indicated in the Motion Control instruction "MC_CamIn" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165346638347_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time at which the job becomes effective and the synchronization begins. |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The dynamic response of the following axis is limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

##### After synchronization

The cam is offset accordingly in the master value range. The offset results from the current leading value position and the default values of the parameters "MasterSyncPosition", "MasterStartDistance" and "SlaveOffset". The offset in the leading value range is displayed in the "<TO>.StatusSynchronizedMotion.MasterOffset" tag of the technology object.

![After synchronization](images/165347309835_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Current leading value position |
| ② | Current following value position |

The following axis is synchronized as soon as the leading axis has reached the synchronous position. [The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

#### Subsequent synchronizing of following axis using leading value distance with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With subsequent synchronization using the leading value distance, synchronization begins as soon as the leading value has reached the synchronous position of the leading axis.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 3, you define the type of synchronization as subsequent synchronization using the leading value distance.
- With the parameter "MasterSyncPosition", you define the synchronous position of the leading axis relative to the start position of the cam. The synchronous position establishes the relationship between leading value and following value. The synchronous position must be within the definition of the cam. With "MasterSyncPosition" ≠ 0.0, you move the synchronous position within the cam without changing the position of the cam. For subsequent synchronization, the synchronous position of the leading axis is the start position from which synchronization starts.
- With the "MasterStartDistance" parameter, you specify the leading value distance (synchronization length).

##### Until synchronization

After the start of the "MC_CamIn" job, a motion profile is calculated for the following axis depending on the specified leading value distance. The calculation determines the required dynamic response and the position of the leading axis as of which the leading axis and the following axis travel synchronously.

The status "Waiting" is displayed at the following axis until the leading value has reached the synchronous position of the leading axis (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 3).

> **Note**
>
> **Dynamic jumps**
>
> If the following axis is in motion and the leading value is at standstill when the "MC_CamIn" job is started, dynamic jumps can occur at the following axis as soon as the leading axis is set in motion and the following axis starts synchronizing.

If the leading and following axes are already at their synchronous positions when the "MC_CamIn" job is started, synchronous operation immediately has "Synchronous" status.

##### During synchronization

The following axis begins to synchronize as soon as the leading value has reached the synchronous position. The synchronization is indicated in the Motion Control instruction "MC_CamIn" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165347315723_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when synchronization starts |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The dynamic response of the following axis is limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

##### After synchronization

The position of the leading axis from which the leading axis and following axis travel synchronously is derived in the following way:

Position axes synchronous = Synchronous position of leading axis + Synchronization length

As soon as the leading axis has reached this position, the following axis is synchronized. [The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

#### Subsequent synchronizing of following axis using leading axis value starting from the current leading value position with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With subsequent synchronization using the leading value distance from the current leading value position, synchronization begins as soon as the "MC_CamIn" job takes effect and the leading axis is set in motion.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 4, you define the type of synchronization as subsequent synchronization using the leading value distance from the current leading value position. The position of the leading axis must be within the definition of the cam, which may be scaled or shifted.
- With the "MasterStartDistance" parameter, you specify the leading value distance (synchronization length).

##### Until synchronization

After the start of the "MC_CamIn" job, a motion profile is calculated for the following axis depending on the specified leading value distance. The calculation determines the required dynamic response and the position of the leading axis as of which the leading axis and the following axis travel synchronously.

If the leading axis is at a standstill when the job starts, the status "Waiting" is displayed on the following axis (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 3) until the leading axis is set in motion.

> **Note**
>
> **Dynamic jumps**
>
> If the following axis is in motion and the leading value is at standstill when the "MC_CamIn" job is started, dynamic jumps can occur at the following axis as soon as the leading axis is set in motion and the following axis starts synchronizing.

If the leading and following axes are already at their synchronous positions when the "MC_CamIn" job is started, synchronous operation immediately has "Synchronous" status.

##### During synchronization

The following axis begins to synchronize as soon as the "MC_CamIn" job takes effect and the leading axis is moving. The synchronization is indicated in the Motion Control instruction "MC_CamIn" with the parameter "StartSync" = TRUE and in the "<TO>.StatusWord.X21 (Synchronizing)" tag of the following axis. The leading value must not reverse during synchronization.

![During synchronization](images/165348320011_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time at which the job becomes effective and the synchronization begins. |
| ② | Time when synchronization is complete |

The dynamics of the following axis during synchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. Changes in the dynamics of the leading axis during synchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The dynamic response of the following axis is limited to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

##### After synchronization

The position of the leading axis from which the leading axis and following axis travel synchronously is derived in the following way:

Position axes synchronous = Current leading value position at job start + synchronization length

As soon as the leading axis has reached this position, the following axis is synchronized. [The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

#### Directly set following axis synchronously with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With directly set synchronously, the leading and following axes move synchronously immediately without synchronization motion.

This type of synchronization is mainly suitable for synchronizing at a standstill.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 2, you specify the type of synchronization as directly set synchronously.
- With the parameter "MasterSyncPosition", you define the synchronous position of the leading axis relative to the start position of the cam. The synchronous position must be within the definition of the cam. With directly set synchronously, the synchronous position is the position in the cam via which the relation between leading axis and following axis is established.

##### After the "MC_CamIn" job has started

After the "MC_CamIn" job has started, the status "Synchronous" is set directly at the current leading value position and at the current following value position.

The synchronous position specified in the cam is assigned to the position setpoint of the leading axis in the leading value range and to the position setpoint of the following axis in the following value range. The cam is offset accordingly. The current offset results from the cam and is displayed at the "<TO>.StatusSynchronizedMotion.MasterOffset" and "<TO>.StatusSynchronizedMotion.SlaveOffset" tags of the technology object.

[The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

##### Additional information

For more information on direct synchronous setting, refer to the FAQ entry [109758886](https://support.industry.siemens.com/cs/ww/en/view/109758886) in the Siemens Industry Online Support.

#### Directly set following axis synchronously at end of the cam with "MC_CamIn" (S7-1500T)

During [camming](#camming-with-mc_camin-s7-1500t), synchronization establishes the relationship between the leading axis and following axis. With directly set synchronously at the end of the cam, you change another cam or the current cam with a new scaling at the end of the active cam. Camming must already be active for this ("MC_CamIn.InSync" = TRUE). The synchronous operation remains in "synchronous" status without a synchronous operation of the following axis.

##### Parameter inputs

You define the behavior of the following axis for synchronization with the following parameters of the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 5, you specify the type of synchronization as directly set synchronously.
- With the "MasterSyncPosition" parameter, you define the synchronous position relative to the start position of the cam. The synchronous position must be within the definition of the cam. With directly set synchronously at the end of the cam, the specified synchronous position of the cam to be changed is automatically moved to the end position of the active cam. To do this, the cam to be inserted is moved in the leading value range and in the following value range. This means that there is no setpoint jump in the following value.

  > **Note**
  >
  > **Dynamic jumps**
  >
  > Note that dynamic jumps on the following axis can occur in the transition between the two cams if the velocity and acceleration are discontinuous.

##### Dynamic jumps on the following axis

To determine dynamic jumps on the following axis, use the "[MC_GetCamFollowingValue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamfollowingvalue-read-out-following-value-of-a-cam-v8-s7-1500t)" instruction, for example, to check the following values for velocity and acceleration in the following positions:

- End position of the active cam (<TO>.StatusCam.EndLeadingValue)
- Synchronous position of the ("MasterSyncPosition") cam to be changed

If the parameter values "MC_GetCamFollowingValue.FirstDerivative" of both jobs match, the transition between the cams is constant in velocity. If the parameter values "MC_GetCamFollowingValue.SecondDerivative" of both jobs match, the transition between the cams is constant in acceleration.

To avoid dynamic jumps on the following axis when changing the active cam with new scaling with the start position as synchronous position, use the setting "<TO>.InterpolationSettings.BoundaryConditions" = 1 for the[interpolation of the cam](#interpolating-a-cam-s7-1500t). This gives you a steady velocity transition.

##### After the "MC_CamIn" job has started

The status "Waiting" is displayed at the following axis until the leading value has reached the end of the active cam or the active cam cycle ("<TO>.StatusSynchronizedMotion.WaitingFunctionState" = 3).

##### When reaching the end of the cam

When the end of the cam is reached ("EndOfProfile" = TRUE), the replaced cam becomes active directly at the current leading value position and at the current following value position starting from the specified synchronous position. The cam is offset accordingly. The offset is displayed in the "<TO>.StatusSynchronizedMotion.MasterOffset" and "<TO>.StatusSynchronizedMotion.SlaveOffset" tags of the technology object.

The synchronous operation remains in "synchronous" status. [The following axis travels synchronously with the leading axis in accordance with the cam profile](#synchronous-travel-in-camming-with-mc_camin-s7-1500t).

### Synchronous travel in camming with "MC_CamIn" (S7-1500T)

As soon as the following axis is synchronized to a leading value, the following axis follows the position of the leading axis according to the cam profile. The transmission behavior during camming is expressed by the cam curve.

The "Synchronous" status is indicated in the Motion Control instruction "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)" with the parameter "InSync" = TRUE and in the "<TO>.StatusWord.X22 (Synchronous)" tag of the technology object.

> **Note**
>
> **Avoid homing the leading axis in synchronous operation**
>
> Avoid homing the leading axis during an active synchronous operation. Homing the leading axis during synchronous operation corresponds to a setpoint step-change on the following axis. The following axis compensates for the jump according to the synchronous operation function and limited only to the maximum speed of the drive.

### Reading out leading and following values during camming (S7-1500T)

This section contains information on the following topics:

- [Reading the leading value in camming (S7-1500T)](#reading-the-leading-value-in-camming-s7-1500t)
- [Reading the following value in camming (S7-1500T)](#reading-the-following-value-in-camming-s7-1500t)
- [Reading out the following value cyclically during camming (S7-1500T)](#reading-out-the-following-value-cyclically-during-camming-s7-1500t)

#### Reading the leading value in camming (S7-1500T)

With the Motion Control instruction "MC_GetCamLeadingValue", you read the leading value that is defined for a following value from a cam.

##### Parameter inputs

You use the following parameters of the motion control instruction "[MC_GetCamLeadingValue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamleadingvalue-read-out-leading-value-of-a-cam-v8-s7-1500t)" to define the settings:

- With the parameter "FollowingValue", you define the following value for which the leading value is to be read.
- You define an approach value for the sought leading value with the parameter "ApproachLeadingValue".
- You define the approach direction for the sought leading value with the parameter "ApproachDirection".
- You define the offset of the cam in the leading value range with the parameter "MasterOffset".
- You define the offset of the cam in the following value range with the parameter "SlaveOffset".
- You define the scaling of the cam in the leading value range with the "MasterScaling" parameter.
- You define the scaling of the cam in the following value range with the "SlaveScaling" parameter.

The cam technology object is not changed with the specification of offset and scaling of the cam. For more information on offset and scaling of the cam, refer to the section "[Scaling and shifting cam](#scaling-and-shifting-cam-s7-1500t)".

##### Approach value and approach direction

Since the same following values can be defined for different leading values, specify an approach value for the sought leading value in the "ApproachLeadingValue" parameter. If the following value is used multiple times in the cam, it can be used to limit the searched leading value. The approach value refers to the – if applicable, offset and scaled – leading values of the cam. The approach value can lie inside or outside the definition range of the cam.

In addition, you can define a search direction with the "ApproachDirection" parameter. With "ApproachDirection" = 1, the search is carried out in the positive direction from the specified approach value. With "ApproachDirection" = 2, the search is carried out in the negative direction. With "ApproachDirection" = 3, the nearest value is searched for independent of direction.

If the specified approach value "ApproachLeadingValue" already corresponds to the sought leading value, this leading value is only found with "ApproachDirection" = 3. With "ApproachDirection" = 1 or 2, the closest value in the specified search direction is found in each case.

**Example**

In the following example, the following value for which the leading value is to be read is defined as "FollowingValue" = 0.5. For the approach value for the sought leading value ①, "ApproachLeadingValue" = 225.0 is specified.

![Approach value and approach direction](images/169290006667_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Approach value for the sought leading value ("ApproachLeadingValue") |

With "ApproachDirection" = 1, the search is carried out in the positive direction from the approach value. The read leading value is "Value" = 270.0.

With "ApproachDirection" = 2, the search is carried out in the negative direction from the approach value. The read leading value is "Value" = 90.0.

With "ApproachDirection" = 3, the nearest value is searched for from the approach value independent of direction. The read leading value is "Value" = 270.0.

##### After the "MC_GetCamLeadingValue" job has started

The leading value is read after the "MC_GetCamLeadingValue" job has started. As soon as the job is completed with "Done" = TRUE, the parameter "Value" contains the read leading value.

#### Reading the following value in camming (S7-1500T)

With the Motion Control instruction "MC_GetCamFollowingValue", you read the following value that is defined for a leading value from a cam.

##### Parameter inputs

You use the following parameters of the motion control instruction "[MC_GetCamFollowingValue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamfollowingvalue-read-out-following-value-of-a-cam-v8-s7-1500t)" to define the settings:

- With the parameter "LeadingValue", you define the leading value for which the following value is to be read.
- You define the offset of the cam in the leading value range with the parameter "MasterOffset".
- You define the offset of the cam in the following value range with the parameter "SlaveOffset".
- You define the scaling of the cam in the leading value range with the "MasterScaling" parameter.
- You define the scaling of the cam in the following value range with the "SlaveScaling" parameter.

The cam technology object is not changed with the specification of offset and scaling of the cam. You can find more information on offset and scaling of the cam in the section "[Scaling and shifting cam](#scaling-and-shifting-cam-s7-1500t)".

##### After the "MC_GetCamFollowingValue" job has started

The following value is read after the "MC_GetCamFollowingValue" job has started. As soon as the job is completed with "Done" = TRUE, the following parameters contain the read following value:

- The "Value" parameter contains the position.
- The "FirstDerivative" parameter contains the velocity.
- The "SecondDerivative" parameter contains the acceleration.

#### Reading out the following value cyclically during camming (S7-1500T)

You read the following value that has been defined for a leading value from a cam cyclically with the motion control instruction "MC_GetCamFollowingValueCyclic". Several "MC_GetCamFollowingValueCyclic" jobs related to the same cam are possible simultaneously.

##### Parameter inputs

You use the following parameters of the motion control instruction "[MC_GetCamFollowingValueCyclic](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_getcamfollowingvaluecyclic-cyclically-read-the-following-value-of-a-cam-v8-s7-1500t)" to define the settings:

- With the parameter "LeadingValue", you define the leading value for which the following value is to be read.
- You define the offset of the cam in the leading value range with the parameter "MasterOffset".
- You define the offset of the cam in the following value range with the parameter "SlaveOffset".
- You define the scaling of the cam in the leading value range with the "MasterScaling" parameter.
- You define the scaling of the cam in the following value range with the "SlaveScaling" parameter.

The cam technology object is not changed with the specification of offset and scaling of the cam. You can find more information on offset and scaling of the cam in the section "[Scaling and shifting cam](#scaling-and-shifting-cam-s7-1500t)".

##### During the active "MC_GetCamFollowingValueCyclic" job

The following value is read cyclically as long as the parameter "Enable" = TRUE. Job processing is done synchronously so that the result is output directly. If the parameter "Valid" = TRUE, the following parameters contain the read-out valid following value for the leading value of the same application cycle:

- The "Value" parameter contains the position.
- The "FirstDerivative" parameter contains the velocity.
- The "SecondDerivative" parameter contains the acceleration.

### Leading value offset during camming (S7-1500T)

This section contains information on the following topics:

- [Leading value offset on the following axis during camming using leading value distance as of current leading value position (S7-1500T)](#leading-value-offset-on-the-following-axis-during-camming-using-leading-value-distance-as-of-current-leading-value-position-s7-1500t)
- [Leading value offset on the following axis during camming using leading value distance as of specific leading value position (S7-1500T)](#leading-value-offset-on-the-following-axis-during-camming-using-leading-value-distance-as-of-specific-leading-value-position-s7-1500t)
- [Defining the direction of the leading value distance of a leading value offset on the following axis during camming (S7-1500T)](#defining-the-direction-of-the-leading-value-distance-of-a-leading-value-offset-on-the-following-axis-during-camming-s7-1500t)
- [Only cancel a pending leading value offset in the camming (S7-1500T)](#only-cancel-a-pending-leading-value-offset-in-the-camming-s7-1500t)

#### Leading value offset on the following axis during camming using leading value distance as of current leading value position (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)". You can move the effective leading value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the leading value offset.

The leading value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

##### Parameter inputs

You define the behavior of the following axis during leading value offset with the following parameters of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 1, you specify the type of leading value offset as offset using leading value distance as of the current leading value position.
- With the "PhaseShift" parameter, you specify the leading value offset on the following axis.
- With the "PhasingDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the leading value offset.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-leading-value-offset-on-the-following-axis-during-camming-s7-1500t).

##### During the leading value offset

After starting the jobs, the following axis begins with the leading value offset starting from the current position. Within the traversing distance of the leading axis, the following axis offsets the leading value at continuous velocity and acceleration. The required dynamics of the following axis to offset the leading value is calculated by the system. During leading value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The leading value offset is indicated in the Motion Control instruction with the parameter "StartPhasing" = TRUE and in the "<TO>.StatusWort.X24 (PhasingCommand)" tag of the technology object. The "AbsolutePhaseShift" or "CoveredPhaseShift" parameter shows the absolute leading value portion already shifted.

The leading value must not reverse during the leading value offset on the following axis. When the leading value reverses, the "MC_PhasingAbsolute" job or "MC_PhasingRelative" job is canceled with "ErrorID" = 16#808C.

##### After the leading value offset

As soon as the following axis has offset the leading value, the leading value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.PhaseShift" tag of the technology object.

The leading value offset only has an effect in the "Synchronous" status of the camming. When the camming is overridden, the leading value offset is reset to zero.

#### Leading value offset on the following axis during camming using leading value distance as of specific leading value position (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)". You can move the effective leading value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the leading value offset.

The leading value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

##### Parameter inputs

You define the behavior of the following axis during leading value offset with the following parameters of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 2, you specify the type of leading value offset as offset using leading value distance as of a specific leading value position.
- With the "PhaseShift" parameter, you specify the leading value offset on the following axis.
- With the "PhasingDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the leading value offset.
- With the "StartPosition" parameter, you specify the leading value position from which the leading value offset starts.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-leading-value-offset-on-the-following-axis-during-camming-s7-1500t).

##### Until the leading value offset

After starting the job, the status "Waiting" is displayed at the following axis when the leading value is at standstill and until the leading value has reached the leading value position (<TO>.StatusWord2.X3 = TRUE (PhasingCommandWaiting)).

##### During the leading value offset

As soon as the leading value has reached the leading value position, the following axis begins to offset the leading value. Within the traversing distance of the leading axis, the following axis offsets the leading value at continuous velocity and acceleration. The required dynamics of the following axis to offset the leading value is calculated by the system. During leading value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The leading value offset is indicated in the Motion Control instruction with the parameter "StartPhasing" = TRUE and in the "<TO>.StatusWort.X24 (PhasingCommand)" tag of the technology object. The "AbsolutePhaseShift" or "CoveredPhaseShift" parameter shows the absolute leading value portion already shifted.

The leading value must not reverse during the leading value offset on the following axis. When the leading value reverses, the "MC_PhasingAbsolute" job or "MC_PhasingRelative" job is canceled with "ErrorID" = 16#808C. The waiting job is not canceled.

##### After the leading value offset

As soon as the following axis has offset the leading value, the leading value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.PhaseShift" tag of the technology object.

The leading value offset only has an effect in the "Synchronous" status of the camming. When the camming is overridden, the leading value offset is reset to zero.

#### Defining the direction of the leading value distance of a leading value offset on the following axis during camming (S7-1500T)

With a leading value offset, you offset the effective leading value on the following axis during camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)". With the "Direction" parameter of the Motion Control instruction "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)", you specify the direction of the leading value distance in relation to the direction of motion of the effective leading value.

![Figure](images/165346632459_DV_resource.Stream@PNG-en-US.png)

##### Defining leading value distance in the positive direction of motion of the effective leading value

With "Direction" = 1, the following axis only offsets the leading value when the leading axis travels in the positive direction.

![Defining leading value distance in the positive direction of motion of the effective leading value](images/165348325899_DV_resource.Stream@PNG-de-DE.png)

##### Defining leading value distance in the negative direction of motion of the effective leading value

With "Direction" = 2, the following axis only offsets the leading value when the leading axis travels in the negative direction.

![Defining leading value distance in the negative direction of motion of the effective leading value](images/165348331019_DV_resource.Stream@PNG-de-DE.png)

##### Defining leading value distance in the current direction of motion of the effective leading value

With "Direction" = 3, the following axis offsets the leading value regardless of the direction in which the leading axis is currently traveling.

#### Only cancel a pending leading value offset in the camming (S7-1500T)

With an "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" job with "ProfileReference" = 5, you cancel a pending "MC_PhasingAbsolute" or "MC_PhasingRelative" job. Canceling a waiting job has no effect on an active leading value offset.

### Following value offset during camming (S7-1500T)

This section contains information on the following topics:

- [Following value offset on the following axis during camming using leading value distance as of current leading value position (S7-1500T)](#following-value-offset-on-the-following-axis-during-camming-using-leading-value-distance-as-of-current-leading-value-position-s7-1500t)
- [Following value offset on the following axis during camming using leading value distance as of specific leading value position (S7-1500T)](#following-value-offset-on-the-following-axis-during-camming-using-leading-value-distance-as-of-specific-leading-value-position-s7-1500t)
- [Defining the direction of the leading value distance of a following value offset on the following axis during camming (S7-1500T)](#defining-the-direction-of-the-leading-value-distance-of-a-following-value-offset-on-the-following-axis-during-camming-s7-1500t)
- [Only cancel a pending following value offset in the camming (S7-1500T)](#only-cancel-a-pending-following-value-offset-in-the-camming-s7-1500t)

#### Following value offset on the following axis during camming using leading value distance as of current leading value position (S7-1500T)

With a following value offset, you offset the following value on the following axis during camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)". You can move the following value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the following value offset.

The following value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

For camming, the offset of the following value with an "MC_OffsetAbsolute" or "MC_OffsetRelative" job (<TO>.StatusSynchronizedMotion.Offset) starts at the start value "<TO>.StatusSynchronizedMotion.SlaveOffset".

##### Parameter inputs

You define the behavior of the following axis during following value offset with the following parameters of the Motion Control instruction "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 1, you specify the type of following value offset as offset using leading value distance as of the current leading value position.
- With the "Offset" parameter, you specify the following value offset on the following axis.
- With the "OffsetDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the following value offset.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-following-value-offset-on-the-following-axis-during-camming-s7-1500t).

##### During the following value offset

After starting the job, the following axis begins with the following value offset starting from the current position. Within the traversing distance of the leading axis, the following axis offsets the following value at continuous velocity and acceleration. The required dynamics of the following axis for the following value offset is calculated by the system. During following value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The following value offset is indicated in the Motion Control instruction with the parameter "StartOffset" = TRUE and in the "<TO>.StatusWort2.X4 (OffsetCommand)" tag of the technology object. The "AbsoluteOffset" or "CoveredOffset" parameter shows the absolute following value portion already shifted.

The leading value must not reverse during the following value offset on the following axis. When the leading value reverses, the "MC_OffsetAbsolute" job or "MC_OffsetRelative" job is canceled with "ErrorID" = 16#808C.

##### After the following value offset

As soon as the following axis has offset the following value, the following value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.Offset" tag of the technology object.

The following value offset only has an effect in the "Synchronous" status of the camming. When the camming is overridden, the following value offset is reset to zero.

#### Following value offset on the following axis during camming using leading value distance as of specific leading value position (S7-1500T)

With a following value offset, you offset the following value on the following axis during camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)". You can move the following value absolutely or relatively. The leading value of the leading value source and the position of the leading axis are not influenced by the following value offset.

The following value offset always refers to the effective leading value. The effective leading value is made up of the leading value of the leading value source and the additive leading value. If you do not use an additive leading value via "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)", the effective leading value corresponds to the leading value of the leading value source. You can find an overview in the "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)" section. In the following, "leading value" refers to the effective leading value.

For camming, the offset of the following value with an "MC_OffsetAbsolute" or "MC_OffsetRelative" job (<TO>.StatusSynchronizedMotion.Offset) starts at the start value "<TO>.StatusSynchronizedMotion.SlaveOffset".

##### Parameter inputs

You define the behavior of the following axis during following value offset with the following parameters of the Motion Control instruction "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)":

- With the parameter "ProfileReference" = 2, you specify the type of following value offset as offset using leading value distance as of a specific leading value position.
- With the "Offset" parameter, you specify the following value offset on the following axis.
- With the "OffsetDistance" parameter, you specify the leading value distance (traversing distance of the leading axis) during the following value offset.
- With the "StartPosition" parameter, you specify the leading value position from which the following value offset starts.
- With the "Direction" parameter, you specify the [direction of the leading value distance in relation to the direction of motion of the leading value](#defining-the-direction-of-the-leading-value-distance-of-a-following-value-offset-on-the-following-axis-during-camming-s7-1500t).

##### Until the following value offset

After starting the job, the status "Waiting" is displayed at the following axis when the leading value is at standstill and until the leading value has reached the leading value position (<TO>.StatusWord2.X5 = TRUE (OffsetCommandWaiting)).

##### During the following value offset

As soon as the leading value has reached the leading value position, the following axis begins to offset the following value. Within the traversing distance of the leading axis, the following axis offsets the following value at continuous velocity and acceleration. The required dynamics of the following axis for the following value offset is calculated by the system. During following value offset, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

The following value offset is indicated in the Motion Control instruction with the parameter "StartOffset" = TRUE and in the "<TO>.StatusWort2.X4 (OffsetCommand)" tag of the technology object. The "AbsoluteOffset" or "CoveredOffset" parameter shows the absolute following value portion already shifted.

The leading value must not reverse during the following value offset on the following axis. When the leading value reverses, the "MC_OffsetAbsolute" job or "MC_OffsetRelative" job is canceled with "ErrorID" = 16#808C. The waiting job is not canceled.

##### After the following value offset

As soon as the following axis has offset the following value, the following value offset is active on the following axis. The status is indicated in the Motion Control instruction with the parameter "Done" = TRUE and in the "<TO>.StatusSynchronizedMotion.Offset" tag of the technology object.

The following value offset only has an effect in the "Synchronous" status of the camming. When the camming is overridden, the following value offset is reset to zero.

#### Defining the direction of the leading value distance of a following value offset on the following axis during camming (S7-1500T)

With a following value offset, you offset the following value on the following axis during camming with "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)". With the "Direction" parameter of the Motion Control instruction "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)", you specify the direction of the leading value distance in relation to the direction of motion of the effective leading value.

![Figure](images/165346632459_DV_resource.Stream@PNG-en-US.png)

##### Defining leading value distance in the positive direction of motion of the effective leading value

With "Direction" = 1, the following axis only offsets the following value when the leading axis travels in the positive direction.

![Defining leading value distance in the positive direction of motion of the effective leading value](images/165348707339_DV_resource.Stream@PNG-de-DE.png)

##### Defining leading value distance in the negative direction of motion of the effective leading value

With "Direction" = 2, the following axis only offsets the following value when the leading axis travels in the negative direction.

![Defining leading value distance in the negative direction of motion of the effective leading value](images/165348712459_DV_resource.Stream@PNG-de-DE.png)

##### Defining leading value distance in the current direction of motion of the effective leading value

With "Direction" = 3, the following axis offsets the following value regardless of the direction in which the leading axis is currently traveling.

#### Only cancel a pending following value offset in the camming (S7-1500T)

With an "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" job with "ProfileReference" = 5, you cancel a pending "MC_OffsetAbsolute" or "MC_OffsetRelative" job. Canceling a pending job has no effect on an active following value offset.

### Desynchronize camming (S7-1500T)

This section contains information on the following topics:

- [Desynchronizing following axis using dynamic parameters with "MC_CamOut" (S7-1500T)](#desynchronizing-following-axis-using-dynamic-parameters-with-mc_camout-s7-1500t)
- [Desynchronizing following axis using leading value distance with "MC_CamOut" (S7-1500T)](#desynchronizing-following-axis-using-leading-value-distance-with-mc_camout-s7-1500t)
- [Defining direction of desynchronization with "MC_CamOut" (S7-1500T)](#defining-direction-of-desynchronization-with-mc_camout-s7-1500t)
- [Dynamic limits of the following axis during desynchronization with "MC_CamOut" (S7-1500T)](#dynamic-limits-of-the-following-axis-during-desynchronization-with-mc_camout-s7-1500t)
- [Only cancel a pending camming with "MC_CamOut" (S7-1500T)](#only-cancel-a-pending-camming-with-mc_camout-s7-1500t)

#### Desynchronizing following axis using dynamic parameters with "MC_CamOut" (S7-1500T)

Desynchronization ends the synchronous operation relationship between the leading and following axis and camming is ended. For desynchronization using dynamic parameters, desynchronization begins in such a way that the following axis comes to a standstill when the stop position is reached.

With the Motion Control instruction "MC_CamOut" you can desynchronize a camming which you have started either with a "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)" job.

##### Parameter inputs

You define the behavior of the following axis for desynchronization with the following parameters of the Motion Control instruction "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 0, you specify the type of desynchronization as desynchronization using dynamic parameters.
- With the parameter "SlavePosition", you specify the stop positions of the following axis. The stop position of the following axis is the position at which the following axis comes to a standstill and the desynchronization is completed.
- With the "Deceleration" parameter, you specify the deceleration of the following axis.
- With the "Jerk" parameter, you specify the jerk of the following axis.
- With the "SyncOutDirection" parameter, you specify the [direction of the desynchronization](#defining-direction-of-desynchronization-with-mc_camout-s7-1500t).

##### Until desynchronization

After the start of the "MC_CamOut" job, a motion profile for the following axis is calculated continuously. The motion profile is calculated based on the following parameters:

- Specified stop position of the following axis in the Motion Control instruction
- Specified dynamics of the Motion Control instruction
- Current position and dynamics of the leading and following axes
- Synchronous operation function
- Superimposed motion of the following axis
- Additive leading value of the following axis

The distance of the following axis and thus the starting position of the following axis for desynchronization results from the calculation.

The start position of the following axis is derived in the following way:

Start position = stop position of the following axis - travel distance of the following axis

The status "Waiting" is displayed at the following axis until the following value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 5).

##### During desynchronization

The following axis begins to desynchronize as soon as the following value has reached the start position. Desynchronization is indicated in the Motion Control instruction "MC_CamOut" with the parameter "StartSyncOut" = TRUE and in the "<TO>.StatusWord2.X1 (DesynchronizingCommand)" tag of the technology object. The synchronous operation is no longer in the "Synchronous" status. Superimposed jobs of the following axis are canceled.

The following axis moves to the stop position with the specified dynamics, independent of the leading value. The dynamic response of the following axis is limited to the dynamic limits configured on the technology object.

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

During desynchronization, several modulo revolutions of both axes are generally possible.

##### After desynchronization

As soon as the following axis reaches the stop position, the following axis is desynchronized. The following axis is at a standstill. The status is indicated in the Motion Control instruction "MC_CamOut" with the parameter "Done" = TRUE and in the "<TO>.StatusWord.X7 (Standstill)" tag of the technology object.

#### Desynchronizing following axis using leading value distance with "MC_CamOut" (S7-1500T)

Desynchronization ends the synchronous operation relationship between the leading and following axis and camming is ended. For desynchronization using the leading value distance, desynchronization begins in such a way that the following axis comes to a standstill when the stop position is reached.

With the Motion Control instruction "MC_CamOut" you can desynchronize a camming which you have started either with a "[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)" job.

##### Parameter inputs

You define the behavior of the following axis for desynchronization with the following parameters of the Motion Control instruction "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)":

- With the parameter "SyncProfileReference" = 1, you specify the type of desynchronization as desynchronization using the leading value distance.
- With the parameter "SlavePosition", you specify the stop positions of the following axis. The stop position of the following axis is the position at which the following axis comes to a standstill and the desynchronization is completed.
- With the "MasterStopDistance" parameter, you define the leading value distance (desynchronization length).
- With the "SyncOutDirection" parameter, you specify the [direction of the desynchronization](#defining-direction-of-desynchronization-with-mc_camout-s7-1500t).

##### Until desynchronization

After the start of the "MC_CamOut" job, a motion profile is calculated depending on the specified leading value distance. The calculation determines the required dynamics and thus the start position of the leading axis for the desynchronization.

The start position of the leading axis is derived in the following way:

Start position = leading value position when the stop position of the following axis is reached - leading value distance

The status "Waiting" is displayed at the following axis until the leading value has reached the start position (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 5).

##### During desynchronization

The following axis begins to desynchronize as soon as the leading value has reached the start position. Desynchronization is indicated in the Motion Control instruction "MC_CamOut" with the parameter "StartSyncOut" = TRUE and in the "<TO>.StatusWord2.X1 (DesynchronizingCommand)" tag of the technology object. The synchronous operation is no longer in the "Synchronous" status. Superimposed jobs of the following axis are canceled.

The following axis travels to the stop position depending on the leading value distance. The dynamics of the following axis during desynchronization is obtained from the calculated motion profile and the current dynamics of the leading axis. The dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed).

Changes in the dynamics of the leading axis during desynchronization are superimposed with the calculated motion profile in accordance with the synchronous operation function. This can have the result that the configured dynamic limits at the following axis are violated. This scenario is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object.

The leading value must not reverse during desynchronization. During desynchronization, several modulo revolutions of both axes are generally possible.

![During desynchronization](images/165348768779_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time when desynchronization starts |
| ② | Time when desynchronization is complete |

If the leading axis stops during desynchronization, high dynamic values can occur at the following axis as soon as the leading axis starts moving again and the following axis continues moving to the specified stop position. To avoid these high dynamic values at the following axis, use desynchronization via dynamic parameters ("SyncProfileReference" = 0).

##### After desynchronization

As soon as the following axis reaches the stop position, the following axis is desynchronized. The following axis is at a standstill. The status is indicated in the Motion Control instruction "MC_CamOut" with the parameter "Done" = TRUE and in the "<TO>.StatusWord.X7 (Standstill)" tag of the technology object.

#### Defining direction of desynchronization with "MC_CamOut" (S7-1500T)

Desynchronization ends the synchronous operation relationship between the leading and following axis and camming is ended. You can specify the desynchronization direction with the "SyncOutDirection" parameter of the Motion Control instruction "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)".

![Figure](images/165346632459_DV_resource.Stream@PNG-en-US.png)

##### Desynchronizing the following axis in positive traversing direction

With "SyncOutDirection" = 1, the following axis is only desynchronized when the following axis moves in the positive direction.

![Desynchronizing the following axis in positive traversing direction](images/165348774667_DV_resource.Stream@PNG-de-DE.png)

##### Desynchronizing the following axis in negative traversing direction

With "SyncOutDirection" = 2, the following axis is only desynchronized when the following axis moves in the negative direction.

![Desynchronizing the following axis in negative traversing direction](images/165348779787_DV_resource.Stream@PNG-de-DE.png)

##### Desynchronizing the following axis in the current traversing direction

With "SyncOutDirection" = 3, the following axis is desynchronized in the direction in which the following axis is currently moving.

#### Dynamic limits of the following axis during desynchronization with "MC_CamOut" (S7-1500T)

If a synchronous axis is desynchronized as a following axis in the camming with the Motion Control instruction "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)", the following dynamic limits apply, depending on the type of desynchronization:

##### Desynchronization via dynamic parameters

During synchronization using dynamic parameters, the dynamic limits configured at the technology object apply to the following axis.

- <TO>.DynamicLimits.MaxVelocity
- <TO>.DynamicLimits.MaxAcceleration
- <TO>.DynamicLimits.MaxDeceleration
- <TO>.DynamicLimits.MaxJerk

The SW limit switches also continue to be monitored with the configured dynamic limits of the following axis.

##### Desynchronization using leading value distance

During desynchronization via the leading value distance and during synchronous travel, the dynamics of the following axis is limited only to the maximum speed of the drive (<TO>.Actor.DriveParameter.MaxSpeed). The dynamics of the following axis results from the synchronous operation function.

If the dynamic limits configured for the following axis are exceeded, this is indicated in the "<TO>.StatusSynchronizedMotion.StatusWord.X0 … X2" tags of the technology object. The SW limit switches continue to be monitored with the configured dynamic limits of the following axis.

If the following axis cannot follow the leading value, this results in a following error, which is monitored by the following error monitoring.

---

**See also**

[Dynamic limits of the following axis in camming (S7-1500T)](#dynamic-limits-of-the-following-axis-in-camming-s7-1500t)

#### Only cancel a pending camming with "MC_CamOut" (S7-1500T)

With a "[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)" job with "SyncProfileReference" = 5 you cancel a pending camming. Canceling a pending camming has no effect on an active cam camming.

### Tags: Camming (S7-1500T)

The following technology object tags are relevant for camming:

| Status indicators |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.StatusSynchronizedMotion.FunctionState | Indication of which synchronous operation function is active |  |
| 0 | No synchronous operation active |  |
| 1 | Gearing ("[MC_GearIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearin-start-gearing-v8-s7-1500-s7-1500t)") |  |
| 2 | Gearing with specified synchronous positions ("[MC_GearInPos](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinpos-start-gearing-with-specified-synchronous-positions-v8-s7-1500t)") |  |
| 3 | Camming ("[MC_CamIn](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camin-start-camming-v8-s7-1500t)") |  |
| 4 | Desynchronization of gearing ("[MC_GearOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearout-desynchronize-gearing-v8-s7-1500t)") |  |
| 5 | Desynchronization of camming ("[MC_CamOut](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camout-desynchronize-camming-v8-s7-1500t)") |  |
| 6 | Velocity gearing ("[MC_GearInVelocity](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_gearinvelocity-start-velocity-synchronous-operation-v8-s7-1500t)") |  |
| <TO>.StatusSynchronizedMotion.WaitingFunctionState | Indication of which synchronous operation function is waiting |  |
| 0 | No synchronous operation waiting |  |
| 1 | Reserved |  |
| 2 | Gearing with specified synchronous positions waiting ("MC_GearInPos") |  |
| 3 | Camming waiting ("MC_CamIn") |  |
| 4 | Desynchronization of gearing waiting ("MC_GearOut") |  |
| 5 | Desynchronization of camming waiting ("MC_CamOut") |  |
| <TO>.StatusSynchronizedMotion.ActualMaster | When a synchronous operation job is started, the number of the technology data block of the currently used leading axis is displayed. |  |
| 0 | Synchronous operation inactive |  |
| <TO>.StatusSynchronizedMotion.ActualCam | Currently used for cyclic cam for camming |  |
| <TO>.StatusSynchronizedMotion.MasterOffset | Current offset of the leading value range of the cyclic cam |  |
| <TO>.StatusSynchronizedMotion.MasterScaling | Current scaling of the leading value range of the cyclic cam |  |
| <TO>.StatusSynchronizedMotion.SlaveOffset | Current offset of the following value range of the cyclic cam |  |
| <TO>.StatusSynchronizedMotion.SlaveScaling | Current scaling of the following value range of the cyclic cam |  |
| <TO>.Position | Setpoints of the axis |  |
| <TO>.Velocity |  |  |
| <TO>.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Position | Effective leading value including an additive leading value with an "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Velocity |  |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.PhaseShift | Current absolute leading value offset with an "[MC_PhasingAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingabsolute-absolute-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" or "[MC_PhasingRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_phasingrelative-relative-shift-of-leading-value-on-the-following-axis-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.FunctionLeadingValue.Position | Leading value of the synchronous operation function after a leading value offset with an "MC_PhasingAbsolute" job or "MC_PhasingRelative" job including an additive leading value with a "MC_LeadingValueAdditive" job |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Position | Following value of the synchronous operation function before a following value offset with an "MC_OffsetAbsolute" job or "MC_OffsetRelative" job |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Velocity |  |  |
| <TO>.StatusSynchronizedMotion.FunctionFollowingValue.Acceleration |  |  |
| <TO>.StatusSynchronizedMotion.Offset | Current absolute following value offset with an "[MC_OffsetAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetabsolute-absolute-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" or "[MC_OffsetRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_offsetrelative-relative-shift-of-following-value-on-the-following-axis-v8-s7-1500t)" job |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X0 (MaxVelocityExceeded) | Set to the value "TRUE" when the maximum velocity configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X1 (MaxAccelerationExceeded) | Set to the value "TRUE" when the maximum acceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X2 (MaxDecelerationExceeded) | Set to the value "TRUE" when the maximum deceleration configured for the following axis is exceeded during synchronous operation. |  |
| <TO>.StatusWord.X21 (Synchronizing) | Set to the value "TRUE" when the synchronous axis synchronizes to a leading value. |  |
| <TO>.StatusWord.X22 (Synchronous) | Set to the value "TRUE" when the synchronous axis is synchronized and moves synchronously to the leading axis. |  |
| <TO>.StatusWord2.X1 (DesynchronizingCommand) | Set to the value "TRUE" when the synchronous axis desynchronizes. |  |
| <TO>.StatusWord.X24 (PhasingCommand) | Is set to the value "TRUE" if a job for leading value offset is active ("MC_PhasingAbsolute", "MC_PhasingRelative"). |  |
| <TO>.StatusWord2.X3 (PhasingCommandWaiting) | Is set to the value "TRUE" if a job for leading value offset is pending ("MC_PhasingAbsolute", "MC_PhasingRelative"). |  |
| <TO>.StatusWord2.X4 (OffsetCommand) | Is set to the value "TRUE" if a job for following value offset is active ("MC_OffsetAbsolute", "MC_OffsetRelative"). |  |
| <TO>.StatusWord2.X5 (OffsetCommandWaiting) | Is set to the value "TRUE" if a job for following value offset is waiting ("MC_OffsetAbsolute", "MC_OffsetRelative"). |  |
| <TO>.ErrorWord.X14 (SynchronousError) | Error during synchronous operation  The leading axis specified in the motion control instruction was not configured as a possible leading axis. |  |

## Other synchronous operation functions (S7-1500T)

This section contains information on the following topics:

- [Simulate synchronous operation (S7-1500T)](#simulate-synchronous-operation-s7-1500t)
- [Specify additive leading value (S7-1500T)](#specify-additive-leading-value-s7-1500t)

### Simulate synchronous operation (S7-1500T)

This section contains information on the following topics:

- [Brief description of simulating synchronous operation (S7-1500T)](#brief-description-of-simulating-synchronous-operation-s7-1500t)
- [Tags: Synchronous operation is being simulated (S7-1500T)](#tags-synchronous-operation-is-being-simulated-s7-1500t)

#### Brief description of simulating synchronous operation (S7-1500T)

An active synchronous operation connection is disconnected when axis enables are removed or for motion jobs on a following axis. By simulating synchronous operation, you can keep the synchronous operation active without canceling the synchronous operation relationship. You can set an active synchronous operation with the motion control instruction "[MC_SynchronizedMotionSimulation](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_synchronizedmotionsimulation-simulate-synchronous-operation-v8-s7-1500t)" in simulation.

The synchronous operation only acts on the following axis. Setpoint changes from the synchronous operation are no longer taken into consideration at the axis and no longer forwarded to the drive. The setpoints output to the drive continue to come from any active superimposed motions of the following axis. This also applies to single-axis jobs on the following axis, while synchronous operation is in simulation mode.

> **Note**
>
> **Setting synchronous operation with superimposed motions in simulation**
>
> If superimposed movements by the motion control instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed" or "MC_HaltSuperimposed" are or were active on the following axis, do not set a synchronous operation in simulation. This is because after you end the simulation, the following axis follows the leading axis without the position shifted by the superimposed motion. This can cause a setpoint jump of the position on the following axis.
>
> If you are using synchronous operation, use the motion control instructions "MC_OffsetAbsolute" or "MC_OffsetRelative" to move the following axis position.

##### Starting the simulation

**Requirement**

- The technology object has been configured correctly.
- The following axis is a synchronous axis.
- Synchronous operation is active on the technology object in status "Synchronous" (<TO>.StatusWord.X22 = TRUE).

**Procedure**

To set a synchronous operation on a following axis in simulation mode, follow these steps:

1. At the "Slave" parameter of the "MC_SynchronizedMotionSimulation" job, specify the following axis on which the synchronous operation is active.
2. Bring the leading axis to a standstill, e.g. with an "MC_Halt" job.
3. Start the simulation of the synchronous operation on the following axis with "Enable" = TRUE parameter. The leading axis must be stopped at this time.

   As soon as the synchronous operation is active, this is indicated in the motion control instruction by the parameter "InSimulation" = TRUE and in the "<TO>.StatusSynchronizedMotion.StatusWord.X3 (In­Simulation)" tag of the technology object.

   The synchronous operation remains active during the simulation, including the motions through single axis jobs or with disabling the leading axis and/or following axis with "MC_Power.Enable" = FALSE or a "MC_Stop" job, for example by opening a protective door. The synchronous operation in "synchronous" status ("MC_GearIn.InGear" = TRUE, "MC_GearInPos.InSync" = TRUE or "MC_CamIn.InSync" = TRUE, but "<TO>.StatusWord.X22" = FALSE).

##### End simulation

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Machine damage**  If the position of the following axis at the end of the simulation differs from the position at the start of the simulation, this triggers a setpoint step-change which can lead to machine damage.  Therefore, make sure that the setpoints of the following axis correspond to the setpoints from the synchronous operation relationship when simulation is ended. |  |

**Requirement**

- The set position of the following axis coincides with the setpoint from the synchronous relationship.
- The technology object has been enabled ("MC_Power.Enable" = TRUE).

**Procedure**

To end a synchronous operation on a following axis, follow these steps:

1. End the synchronous operation with the parameter "Enable" = FALSE of the "MC_SynchronizedMotionSimulation" job.

   The setpoints of the synchronous operation are directly effective on the following axis. The following axis does not have to be synchronized again after the synchronous operation has been completed.

#### Tags: Synchronous operation is being simulated (S7-1500T)

The following tags of the technology object are relevant for simulation:

| Status indicators |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X3 (In­Simulation) | [Simulation of synchronous operation on a following axis with a "MC_SynchronizedMotionSimulation" job](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_synchronizedmotionsimulation-simulate-synchronous-operation-v8-s7-1500t) |  |
| FALSE | Not simulated |  |
| TRUE | Simulated |  |

### Specify additive leading value (S7-1500T)

This section contains information on the following topics:

- [Brief description of specifying the additive leading value (S7-1500T)](#brief-description-of-specifying-the-additive-leading-value-s7-1500t)
- [Tags: Additive leading value (S7-1500T)](#tags-additive-leading-value-s7-1500t)

#### Brief description of specifying the additive leading value (S7-1500T)

To superimpose the leading value of a synchronous operation from the application, use the Motion Control instruction "MC_LeadingValueAdditive" in addition to the active leading value to cyclically specify an additive leading value on the following axis. The additive leading value consists of position, velocity and acceleration.

You can find an overview in the section "[Mode of operation of the instructions in synchronous operation](#mode-of-operation-of-the-instructions-in-synchronous-operation-s7-1500-s7-1500t)".

##### Parameter inputs

With the following parameters of the Motion Control instruction "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)" you can determine the additive leading value:

- At the "Axis" parameter, specify the following axis on which the additive leading value acts.
- With the "Position" parameter, you can define the additive position value.
- With the "Velocity" parameter, you can define the additive velocity value.
- With the "Acceleration" parameter, you can define the additive acceleration value.

##### Start additive leading value specification

With the "Enable" parameter = TRUE of the "MC_LeadingValueAdditive" job, set the additive leading value to effective. The additive leading value becomes effective directly and without dynamic limitation on the following axis.

You can start an "MC_LeadingValueAdditive" job independently of the synchronous operation job. Only one "MC_LeadingValueAdditive" job can be active on a following axis at any time.

##### During the additive leading value specification

The default values for position, velocity and acceleration are valid as long as the "Busy" parameter = TRUE. Changes in the specified values are directly effective without consideration of the dynamic limits. The active additive leading value specification is displayed in of the "<TO>.StatusSynchronizedMotion.StatusWord.X4 (LeadingValueAdditiveCommand)" tag of the technology object.

The effect of a "MC_LeadingValueAdditive" job depends on the status of the synchronous operation:

| Status of synchronous operation | Effect on: |
| --- | --- |
| Not active or pending | - Start position of synchronization - Following axis dynamic response |
| Synchronization | - Synchronous position - Phase position - Following axis dynamic response |
| Synchronous motion | - Phase position - Following axis dynamic response |
| Desynchronization | - Stop position of following axis - Phase position - Following axis dynamic response |

With a leading value switchover, the additive leading value still remains effective.

##### Ending the additive leading value specification

As soon as you end the leading value specification with the parameter "Enable" = FALSE of the "MC_LeadingValueAdditive" job, the additive leading value directly becomes ineffective.

#### Tags: Additive leading value (S7-1500T)

The following technology object tags are relevant for the additive leading value:

| Status indicators |  |  |
| --- | --- | --- |
| Tag | Description |  |
| <TO>.StatusSynchronizedMotion.StatusWord.X4 (LeadingValueAdditiveCommand) | Additive leading value with a "[MC_LeadingValueAdditive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_leadingvalueadditive-specify-additive-leading-value-v8-s7-1500t)" job |  |
| FALSE | Additive leading value not active |  |
| TRUE | Additive leading value active |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Position | Effective leading value position of the synchronous operation function |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Velocity | Effective leading value velocity of the synchronous operation function |  |
| <TO>.StatusSynchronizedMotion.EffectiveLeadingValue.Acceleration | Effective leading value acceleration of the synchronous operation function |  |

## Cross-PLC synchronous operation (S7-1500T)

This section contains information on the following topics:

- [Brief description of cross-PLC synchronous operation (S7-1500T)](#brief-description-of-cross-plc-synchronous-operation-s7-1500t)
- [Interconnection possibilities (S7-1500T)](#interconnection-possibilities-s7-1500t)
- [Preparing cross-PLC synchronous operation (S7-1500T)](#preparing-cross-plc-synchronous-operation-s7-1500t)
- [Setting up communication via direct data exchange (S7-1500T)](#setting-up-communication-via-direct-data-exchange-s7-1500t)
- [Configuring the provision of leading value and interconnecting axes (S7-1500T)](#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
- [Configuring the tolerance time (S7-1500T)](#configuring-the-tolerance-time-s7-1500t)
- [Working with the interconnection overview table (S7-1500T)](#working-with-the-interconnection-overview-table-s7-1500t)
- [Tags: Cross-PLC synchronous operation (S7-1500T)](#tags-cross-plc-synchronous-operation-s7-1500t)

### Brief description of cross-PLC synchronous operation (S7-1500T)

With cross-PLC synchronous operation, you realize synchronous operations (gearing or camming) between axes that are on different CPUs. All following axes of a leading value are hereby synchronous to one another with consideration of the respective synchronous operation function. All following axes receive the same leading value at the same time. You can configure and operate the following axes on different CPUs within a project. You can also configure the leading axis on any CPU of the same project.

The figure below shows the operating principle based on an example with two following axes on two CPUs:

![Figure](images/166648033803_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165348938507_DV_resource.Stream@PNG-de-DE.png) | Leading value |

The leading axis and a local following axis 1 are located on CPU 1. The leading axis and the following axis 1 are interconnected to a synchronous operation.

The leading axis makes the leading value available for cross-PLC synchronous operation. The leading value is transferred to CPU 2 by means of a leading value telegram via PROFINET IO with IRT.

On CPU 2, a leading axis proxy reads the leading value. A following axis 2 is interconnected locally with the leading axis proxy as leading axis.

The following axes 1 and 2 are synchronous and follow the same leading value.

The S7-1500 and S7-1500T CPUs can make the leading value available for a cross-PLC synchronous operation. You need to use an S7-1500T CPU as the CPU that receives the leading value via a leading value proxy. A cross-PLC synchronous operation between technology objects with different technology versions ≥ V5.0 on CPUs with different firmware versions ≥ V2.8 is possible.

#### More information

For more information on the setup and diagnostics of a cross-PLC synchronous operation including sample projects, refer to the Siemens Industry Online Support FAQ entry [109770938](https://support.industry.siemens.com/cs/ww/en/view/109770938).

### Interconnection possibilities (S7-1500T)

The figure below shows the schematic structure of synchronous following axes with different synchronous operation functions that are distributed over multiple CPUs:

![Figure](images/165349323275_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/165349039115_DV_resource.Stream@PNG-de-DE.png) | Leading value delay that can be configured at the leading axis (delay time) |
| ![Figure](images/165349049355_DV_resource.Stream@PNG-de-DE.png) | Delay time caused by the processing and transfer of the leading value |
| ![Figure](images/165349044235_DV_resource.Stream@PNG-de-DE.png) | Gearing (example) |

You can interconnect a positioning axis, external encoder or synchronous axis technology object as the leading axis on CPU 1.

#### Cascaded interconnection

With a cascaded interconnection, a following axis makes a cross-PLC leading value available to a leading axis proxy again. Use a virtual axis for this purpose.

The figure above shows two cascades: The interconnection between the leading axis and the following axes 2 and 4 is the first cascade. The interconnection between the virtual following axis and the following axes 3 is the second cascade.

#### Communication and time response

In the processing and transfer of the leading value, a delay time occurs between the generation of the leading value on the leading axis one on CPU and the provision of the leading value for the following axes at the leading axis proxy on the other CPUs. The following axes of the other CPUs receive the leading value with a time delay.

In principle, the delay time per cascade is:

Delay time = 2 x application cycle of the CPU of the leading axis proxy

To achieve synchronicity between the local following axes of the CPU of the leading axis and the following axes of other CPUs without extrapolating the leading value at the leading axis proxy, the leading value can be delayed at the leading axis for the local following axes. The delay time can be compensated for with these configurable delay times.

Therefore, in the figure above, a delay time is set at the leading axis on CPU 1, which delays the leading value output to the local following axis 1. In addition, a delay time at the virtual following axis on CPU 2 is set, because CPU 3 is present in a cascade. All following axes thus receive the same leading value at the same time.

During configuration of the following axis under "Leading value interconnections", you select the entry "Delayed" as type of coupling so that the leading value is delayed for local synchronous operation.

Recommendation: Use a virtual axis as leading axis.

#### Delay time

You can calculate and view the delay times in the [interconnection overview](#interconnection-overview-s7-1500t). The application cycles of the leading axis proxy and any cascading present are included in the calculation of the delay times.

Alternatively, you can manually configure the delay times on the leading axis and on the virtual following axis. In this way, you can consider additional requirements from your specific application, for example.

Depending on the set delay time, the leading value at the leading axis proxy is automatically interpolated or extrapolated. The automatic interpolation and extrapolation guarantees the synchronicity of all following axes. In the interconnection overview, an indication of whether the leading value is interpolated or extrapolated is provided for each [route of a leading value](#showing-routes-s7-1500t).

> **Note**
>
> **Deviations in the following values**
>
> With an extrapolation, deviations in the following values can occur in the event of velocity changes. With an interpolation, no deviations of the following values occur in the event of velocity changes.

If you increase the delay time of the leading axis in the leading value settings, this leads to a lower extrapolation time at the leading axis proxy or to a higher interpolation time of the leading value at the leading axis proxy. This reduces the deviations in the following values that arise during extrapolation in the acceleration and deceleration phases.

If the delay time at the leading axis proxy is increased, this results in a higher extrapolation time or to a lower interpolation time.

#### Recursive interconnection

When all axes are active, the leading axis becomes the following axis of its own leading value with a recursive interconnection. During the configuration, recursive interconnections are displayed in the interconnection overview. No delay times can be calculated for recursive interconnections.

Even if different synchronized groups are active at different times, recursive interconnections may still occur during interconnection. Recursive interconnections over multiple CPUs are not detected during runtime.

A recursive interconnection that is in effect during runtime is not permitted.

### Preparing cross-PLC synchronous operation (S7-1500T)

For a cross-PLC synchronous operation, a leading axis proxy technology object on each additional CPU is required in addition to the technology objects for leading and following axes.

When you create a technology object, an "MC_Servo" organization block is automatically created. This is required when you set up communication via direct data exchange on each CPU.

#### Requirement

- You have created a CPU S7-1500 or S7-1500T for the leading axis.
- You have created one or more CPUs S7-1500T for additional following axes.

#### Procedure

To prepare the cross-PLC synchronous operation, follow these steps:

1. On the first CPU, create one of the following technology objects as the leading axis.

   - [Positioning axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#positioning-axis-technology-object-s7-1500-s7-1500t)
   - [Synchronous axis](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#synchronous-axis-technology-object-s7-1500-s7-1500t)
   - [External encoder](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#external-encoder-technology-object-s7-1500-s7-1500t) (S7‑1500T)
2. If necessary, create one or more synchronous axis technology objects as local following axes on the first CPU.
3. Create a leading axis proxy technology object on each additional CPU.
4. Create one or more synchronous axis technology objects as following axes on each additional CPU.
5. For each additional cascade, create a synchronous axis technology object as a virtual following axis that will serve as the leading axis for the next cascade.
6. Configure the configuration parameters of the leading and following axes that are not specific for synchronous operation. You can find a description of the [configuration parameters](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#synchronous-axis-technology-object-s7-1500-s7-1500t) in the "S7-1500/S7-1500T Axis functions" documentation.
7. [Set up the communication via the direct data exchange](#setting-up-communication-via-direct-data-exchange-s7-1500t).
8. [Configure the provision of leading value.](#configuring-the-provision-of-leading-value-and-interconnecting-axes-s7-1500t)
9. [Configure the tolerance time](#configuring-the-tolerance-time-s7-1500t).
10. [Set the delay times](#setting-the-delay-times-s7-1500t).

### Setting up communication via direct data exchange (S7-1500T)

In a cross-PLC synchronous operation, the leading value is transferred via PROFINET IO with IRT. Direct data exchange is used for the communication between the CPUs within a project. With communication by means of direct data exchange, the leading value is made available once within a project and can then by received by multiple CPUs on the same bus. Leading axis proxies that are interconnected with the same leading value can be configured on different CPUs. In addition, it is possible to make multiple leading values of different leading axes available on different CPUs via the same bus. The CPUs must be on a bus and belong to the same sync domain.

For the required communication directions between the connected CPUs, you must first set up transfer areas. A leading value can be provided over up to eight different transfer areas. You then create input and output tags for the CPUs which reference the relevant transfer areas. You can then select these tags for the transfer area when configuring the leading axis and the leading axis proxy.

Hereafter, the sender CPU is the CPU on which a leading axis provides a leading value. The receiver CPU is the CPU on which a leading axis proxy reads the leading value.

#### Requirement

- You have set up a network via PROFINET IO with IRT.
- You have connected the IRT ports of the CPUs in the network view and in the topology view.
- You have assigned the same sync domain to all CPUs.
- You have configured a CPU as sync master.
- You have configured all other CPUs as sync device.
- You have created at least one technology object on all CPUs.

  > **Note**
  >
  > **"MC_Servo" organization block**
  >
  > When you create a technology object, an MC_Servo OB is created automatically.
- You have configured the property "Synchronous to the bus" with "PROFINET IO-System (100)" as the source of the send clock on all CPUs for the "MC_Servo" under "General > Cycle time".

#### Adding communication directions

To add the communication directions, proceed as follows:

1. Open the "I/O communication" tab in the network view.
2. To create a communication direction from the sender CPU to the receiver CPU, select the sender CPU.
3. Drag-and-drop the receiver CPU into the "Drop or select the device here" field of the "Partner 2" table column of the corresponding PROFINET interface.

   The communication direction from sender CPU to receiver CPU is created.
4. Repeat steps 2 and 3 for all communication directions required between the interconnected CPUs.

**Note**

**Communication direction from the receiver CPU to the sender CPU**

If necessary, also set up a communication direction from the receiver CPU to the sender CPU, e.g. to transfer application-specific status information.

#### Configuring transfer areas

To configure the transfer areas, follow these steps:

1. In the "I/O communication" tab in the network view, select a communication direction of a selected CPU.
2. Add a transfer area in the Inspector window under "Properties > General > Direct data exchange" by entering a name.
3. Repeat steps 1 and 2 for all created configuration directions.
4. Configure the created transfer area in the Inspector window "Properties > General > Direct data exchange > <Name of transfer area>":

   - In the "Start address" fields, define the start address of the assigned logical address area of the sender and of the receiver.
   - In the "Organization block" fields, select the MC_Servo OB of the respective CPU.
   - Define a data length of 48 bytes in the "Data length [byte]" field.
5. Repeat step 4 for all created transfer areas.
6. If you use a SIMATIC Drive Controller, set the clock system of the SINAMICS Integrated:

   - Select PROFIdrive Integrated in the network view.
   - In the Inspector window, select the entry "Send clock of the PROFINET interface [X150]" under "Properties > General > Constant bus cycle time" in the "Cycle time" drop-down list.

**Note**

**Multiple receiver CPUs in the same cascade (1:n relationship)**

If multiple receiver CPUs receive the same leading value of the sender CPU, select in each case for the receiver CPU the same address area for the transfer area between the sender CPU and the receiver CPU n that you defined between the sender CPU and the receiver CPU 1 under "Properties > General > Direct data exchange" in the "Partner address" table column.

#### Creating tags

To create the output tag of a sender CPU and the input tag of a receiver CPU, proceed as follows:

1. Open the PLC tags of a CPU via the project tree "<Name of CPU> > PLC tags > Show all tags".

   The "PLC tags" table opens.
2. Enter the name of the new tag in the "Name" column.
3. In the "Data type" column, manually enter the "DX_TEL_SyncOp" data type.
4. Enter the configured start address of the transfer area in the "Address" column with the following prefix:

   - "%Q" for an output tag on the sender CPU
   - "%I" for an input tag on the receiver CPU
5. Repeat steps 1 to 4 for the respective sender and receiver CPUs of all configured transfer areas.

**Note**

**Data type "DX_TEL_SyncOp"**

If the data type "DX_TEL_SyncOp" is not available, it was deleted with the last compilation.

To restore the "DX_TEL_SyncOp" data type, add a ≥ V5.0 technology object. After you have used the data type in the "PLC tags" table, you can delete the technology object again.

#### Result

You have set up communication via direct data exchange. During the configuration of the leading axis and the leading axis proxy, you can now select the configured tags for the transfer areas in the table column or in the "Transfer area" drop-down list under "Technology object > Configuration > Leading value settings".

If no technology object is created on a CPU, the MC_Servo OB is deleted when the software is compiled. To be able to check the set communication in this case, compile the hardware only.

#### More information

For more information on the subject of "Direct data exchange" refer to the ["SIMATIC PROFINET with STEP 7" function manual](https://support.industry.siemens.com/cs/ww/en/view/49948856).

### Configuring the provision of leading value and interconnecting axes (S7-1500T)

The following describes how to connect the leading value and the axes involved for a cross-PLC synchronous operation via one or more cascades.

#### Requirement

- [You have set up the direct data exchange between the CPUs.](#setting-up-communication-via-direct-data-exchange-s7-1500t)
- You have created one of the following technology objects as the leading axis on the first CPU (S7-1500, S7-1500T):

  - Positioning axis
  - Synchronous axis
  - External encoder

  Recommendation: You have configured the leading axis as virtual axis.
- You may have created one or more synchronous axis technology objects as local following axes on the first CPU.
- You have created a leading axis proxy technology object on each additional CPU (S7-1500T).
- You have created one or more synchronous axis technology objects as following axes on each additional CPU.
- For each additional cascade you have created a technology object synchronous axis as a virtual following axis that is used as the leading axis for the next cascade.
- The technology objects are configured correctly.

#### Provide cross-PLC leading value

To make the leading value of the leading axis available cross-PLC, proceed as follows:

1. Open the configuration window "Technology object > Configuration > Leading value settings" of the leading axis.
2. To show rows 2 to 8 in the table in the "Provision of leading value" area, select the "Show all transfer areas" check box.
3. In the "Provide leading value" table column, select the check box of the corresponding transfer area.
4. In the "Transfer area" table column, select in the drop-down list the CPU output tag created for the direct data exchange.

#### Interconnect local following axes

To interconnect the local following axes on the CPU of the leading axis, follow these steps:

1. Open the configuration window "Technology object > Configuration > Leading value interconnections" of a local following axis.
2. In the "Possible leading values" table column, select the leading axis.
3. In the "Type of coupling" table column, select the entry "Delayed".
4. Repeat steps 1 to 3 for all local following axes.

#### Interconnecting leading axis proxies

To interconnect the leading axis proxies to other CPUs, follow these steps:

1. Open the configuration window "Technology object > Configuration > Leading value settings" of a leading axis proxy.
2. In the "Provision of leading value" area in the "Transfer area" drop-down list, select the input tag of the CPU created for the direct data exchange.
3. Repeat steps 1 and 2 for all leading axis proxies of the same cascade.

#### Interconnecting following axes of the other CPUs

To interconnect the following axes that are not configured on the CPU of the leading axis, proceed as follows:

1. Open the configuration window "Technology object > Configuration > Leading value interconnections" of a following axis.
2. In the "Possible leading values" table column, select the alternate leading axis of the CPU.

   In the table column "Leading value source", the leading axis is displayed which provides the leading value (<Name of the CPU>.<Name of the technology object>). The "Setpoint" entry is preset in the "Type of coupling" table column.
3. In the table column with the icon ![Interconnecting following axes of the other CPUs](images/165349329163_DV_resource.Stream@PNG-de-DE.png), select whether this leading value interconnection should be taken into consideration when calculating the delay time in the [interconnection overview](#working-with-the-interconnection-overview-table-s7-1500t).
4. Repeat steps 1 to 3 for all following axes of the same cascade.

#### Interconnecting virtual following axis as leading axis for the next cascade

To interconnect a virtual following axis that is used as leading axis for the next cascade, proceed as follows:

1. Open the configuration window "Technology object > Configuration > Leading value interconnections" of the virtual following axis.
2. In the "Possible leading values" table column, select the alternate leading axis of the CPU.

   In the table column "Leading value source", the leading axis is displayed which provides the leading value (<Name of the CPU>.<Name of the technology object>). The "Setpoint" entry is preset in the "Type of coupling" table column.
3. In the table column with the icon ![Interconnecting virtual following axis as leading axis for the next cascade](images/165349329163_DV_resource.Stream@PNG-de-DE.png), select whether this leading value interconnection should be taken into consideration when calculating the delay time in the interconnection overview.
4. Switch to the configuration window "Technology object > Configuration > Leading value settings" of the virtual following axis.
5. To show rows 2 to 8 in the table in the "Provision of leading value" area, select the "Show all transfer areas" check box.
6. In the "Provide leading value" table column, select the check box of the corresponding transfer area.
7. In the "Transfer area" table column, select in the drop-down list the CPU output tag created for the direct data exchange.
8. Repeat the steps in the section "Interconnecting leading axis proxies" for all leading axis proxy of the next cascade.
9. Repeat the steps "Interconnecting following axes of the other CPUs" for all following axes of the next cascade.
10. Repeat steps 1 to 9 for all other cascades.

### Configuring the tolerance time (S7-1500T)

If an external leading value becomes invalid during a cross-PLC synchronous operation or a communication error occurs, technology alarm 900 ("Leading values invalid") is output after a tolerance time. You can configure this tolerance time on the leading axis proxy technology object.

#### Procedure

To configure the tolerance time, follow these steps:

1. Open the configuration window "Technology object > Configuration > Leading value settings" of a leading axis proxy.
2. In the "Leading value monitoring" area, enter the tolerance time within which a valid leading value is expected in the "Tolerance time invalid leading value" input field.

   > **Note**
   >
   > **Extrapolation of the leading value**
   >
   > Note that the leading value is still being extrapolated during the tolerance time and that the following axis continues to move.
   >
   > Therefore, set the tolerance time as brief as possible.
3. Repeat steps 1 and 2 for all other leading axis proxies.

### Working with the interconnection overview table (S7-1500T)

This section contains information on the following topics:

- [Opening the interconnection overview (S7-1500T)](#opening-the-interconnection-overview-s7-1500t)
- [Interconnection overview (S7-1500T)](#interconnection-overview-s7-1500t)
- [Showing routes (S7-1500T)](#showing-routes-s7-1500t)
- [Setting the delay times (S7-1500T)](#setting-the-delay-times-s7-1500t)

#### Opening the interconnection overview (S7-1500T)

The interconnection overview contains an overview of the interconnected leading and following axes and their CPU assignment. In the interconnection overview, you also trigger the system calculation of the delay time.

##### Requirement

- You have created technology objects in the project for:

  - Leading axis
  - Following axis
  - Leading axis proxy
- You have interconnected the CPUs and technology objects with one another.

##### Procedure

To open the interconnection overview, follow these steps:

1. Select one of the following technology objects in the project navigation:

   - Positioning axis
   - Synchronous axis
   - External encoder
   - Leading axis proxy
2. Select the "Interconnection overview" command from the shortcut menu.

##### Result

The interconnection overview opens.

#### Interconnection overview (S7-1500T)

The interconnection overview contains an overview of the interconnected leading and following axes and their CPU assignment in tabular form.

##### Toolbar

The toolbar at the top of the interconnection overview provides the following functions via buttons:

| Button | Description |
| --- | --- |
| ![Toolbar](images/165349461131_DV_resource.Stream@PNG-de-DE.png) | You update the view of the interconnection overview with this icon. |
| Calculate delay times | You trigger calculation of delay times with this button.  The delay time is only calculated if the check box "Allow system calculation" is selected under "Leading value settings" during configuration of the technology objects.  You can only trigger the calculation of the delay times if the values are not current and the technology objects are not recursively connected. |

##### Filtering the view

You have the following options above the table to filter the view of the interconnection overview:

| Field | Description |
| --- | --- |
| Enter text filter | In this field, enter a term by which the view should be filtered. |
| Show delay times | Select this check box to show the "Delay time" columns which contain the delay times. |
| Show local synchronous operations | Select this check box to display the local leading value interconnections in addition to the cross-PLC leading value interconnections. |

##### Interconnection overview table

The interconnection overview table contains the following information and functions:

| Column |  | Description |  |
| --- | --- | --- | --- |
| Leading value source |  |  |  |
|  | PLC | This column displays the CPU of the leading axis. |  |
| Leading axis | This column displays the name of the leading axis.  You open the configuration of the technology object via the link. |  |  |
| ![Interconnection overview table](images/165349506571_DV_resource.Stream@PNG-de-DE.png) | If this icon is displayed in the "Leading axis" column, the interconnection is excluded from the system calculation of the delay time.  In the configuration of the leading axis, the check box "Allow system calculation" is not selected under "Leading value settings". |  |  |
| DT | This column displays the delay time in ms.  This column is only displayed when the "Show delay times" check box is selected. |  |  |
| Leading value output | This column displays the type of the leading value output and the number of the transfer area. |  |  |
| Recipient |  |  |  |
|  | PLC | This column displays the CPU of the following axis. |  |
| Following axis | This column displays the name of the following axis.  You open the configuration of the technology object via the link. |  |  |
| Routes | When you select a row, the icon ![Interconnection overview table](images/165349465099_DV_resource.Stream@PNG-de-DE.png) is displayed in this column. You open the "Routes" area with this icon. |  |  |
| Leading axis proxy | The name of the leading axis proxy is displayed in this column.  You open the configuration of the technology object via the link. |  |  |
| ![Interconnection overview table](images/165349506571_DV_resource.Stream@PNG-de-DE.png) | If this icon is displayed in the "Leading axis proxy" column, the interconnection is excluded from the system calculation of the delay time.  In the configuration of the leading axis proxy, the check box "Allow system calculation" is not selected under "Leading value settings". |  |  |
| DT | This column displays the delay time in ms.  This column is only displayed when the "Show delay times" check box is selected. |  |  |
| Interconnection |  | ![Interconnection overview table](images/165349502603_DV_resource.Stream@PNG-de-DE.png) | If this icon is displayed in the "Interconnection" column, the interconnection is affected by a recursion. |
| ![Interconnection overview table](images/165349578507_DV_resource.Stream@PNG-de-DE.png) | If this icon is displayed in the "Interconnection" column, the interconnection is affected by a recursion, but at least one interconnection is excluded from the calculation of the delay time. |  |  |
| ![Interconnection overview table](images/165349506571_DV_resource.Stream@PNG-de-DE.png) | If this icon is displayed in the "Interconnection" column, the interconnection is excluded from the system calculation of the delay time. |  |  |
| ![Interconnection overview table](images/165349574539_DV_resource.Stream@PNG-de-DE.png) | With this icon, you open the configuration of the following axis. |  |  |
| ![Interconnection overview table](images/165349469067_DV_resource.Stream@PNG-de-DE.png) |  | If the configured delay time corresponds to the calculated delay time, the icon ![Interconnection overview table](images/165349498635_DV_resource.Stream@PNG-de-DE.png) is displayed in this column. |  |

In the "Leading value source cannot be clearly determined" area, interconnections are displayed where, for example, several leading axes are connected for a leading axis proxy and the leading value source is therefore not unique. The range is only displayed if there are interconnections without a unique leading value source.

#### Showing routes (S7-1500T)

The routes of the leading value of a selected following axis are shown in the interconnection overview in the area underneath the table. The leading value is tracked back from the following axis to the leading axis source. If there are multiple routes, they are displayed next to one another.

##### Procedure

To display the existing routes of a following axis, follow these steps:

1. Select the row of the corresponding following axis in the table.
2. To show the routes, click the icon ![Procedure](images/165349465099_DV_resource.Stream@PNG-de-DE.png) in the "Routes" column.

##### Result

All routes are displayed in the area below the table for the selected following axis. Routes affected by a recursion are not displayed.

It is indicated underneath a route whether the leading value is interpolated or extrapolated:

- If all cascades interpolate, "Interpolated" is displayed.
- If at least one cascade extrapolates, "Extrapolated" is displayed.

#### Setting the delay times (S7-1500T)

You can calculate and view the delay times in the interconnection overview. Alternatively, you can manually configure the delay times on the leading axis and on the virtual following axes. Depending on the set delay time, the leading value at the leading axis proxy is automatically interpolated or extrapolated.

##### Requirement

- You have interconnected the CPUs and technology objects with one another.
- Except for the delay time, the technology objects are fully configured.

##### Calculating delay times

To calculate the delay times, follow these steps:

1. Open the configuration window "Technology object > Configuration > Leading value settings" of the leading axis.
2. In the "Delay time of local leading value" area, select the "Allow system calculation" check box.
3. Repeat steps 1 and 2 for all leading axis proxies and for all virtual following axes that are used as leading axis for additional cascades.
4. Open the configuration window "Technology object > Configuration > Leading value interconnections" of a non-local following axis.
5. For a leading axis proxy technology object of the table column with the symbol ![Calculating delay times](images/165349329163_DV_resource.Stream@PNG-de-DE.png), select whether this leading value interconnection should be taken into account when calculating the delay time.
6. Repeat steps 4 and 5 for all other non-local following axes.
7. To open the interconnection overview, click on the link "Interconnection overview".
8. To calculate the delay times, click the "Calculate delay times" button in the interconnection overview.
9. Check the calculated delay times in the columns "DT" of the interconnection overview.
10. In the [routes](#showing-routes-s7-1500t), check whether a leading value is interpolated or extrapolated at the leading axis proxy (<TO>.StatusExternalLeadingValue.AdjustmentTime).

##### Configuring delay times

To adjust the delay time and, for example, take into account additional requirements from your special application, follow these steps:

1. Open the configuration window "Technology object > Configuration > Leading value settings" of the leading axis.
2. Clear the "Allow system calculation" check box in the "Delay time of local leading value" area.
3. Enter the corresponding value in the "Delay time" input field.

   The entered delay time determines the output delay of the leading value for the local following axes (<TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime).
4. Repeat steps 1 to 3 for all virtual following axes that are used as the leading axis for additional cascades.
5. Open the configuration window "Technology object > Configuration > Leading value settings" of a leading axis proxy.
6. Clear the "Allow system calculation" check box in the "Delay time of local leading value" area.
7. In the "Delay time" (<TO>.Parameter.LocalLeadingValueDelayTime) input field, enter the same delay time that is set on the local virtual following axis that is used as the leading axis for an additional cascade.

   The entered delay time determines the output delay of the leading value for the local following axes (<TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime).
8. To open the interconnection overview, click on the link "Interconnection overview".
9. Check the delay times in the "DT" columns of the interconnection overview.
10. In the [routes](#showing-routes-s7-1500t), check whether a leading value is interpolated or extrapolated at the leading axis proxy (<TO>.StatusExternalLeadingValue.AdjustmentTime).

### Tags: Cross-PLC synchronous operation (S7-1500T)

#### Positioning axis/synchronous axis/external encoder

The following tags of the positioning axis, synchronous axis and external encoder are relevant for cross-PLC synchronous operation:

| Tag | Description |  |
| --- | --- | --- |
| <TO>.CrossPlcSynchronousOperation.Interface[1..8].EnableLeadingValueOutput | Provide cross-PLC leading value |  |
| FALSE | No |  |
| TRUE | Yes |  |
| <TO>.CrossPlcSynchronousOperation.Interface[1..8].AddressOut | Output address for the telegram of cross-PLC synchronous operation |  |
| <TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime | Delay time for setpoint coupling with delayed leading value |  |
| <TO>.StatusProvidedLeadingValue.DelayedLeadingValue.Position | Position of the provided leading value |  |
| <TO>.StatusProvidedLeadingValue.DelayedLeadingValue.Velocity | Velocity of the provided leading value |  |
| <TO>.StatusProvidedLeadingValue.DelayedLeadingValue.Acceleration | Acceleration of the provided leading value |  |

#### Leading axis proxy

The following leading axis proxy technology object tags are relevant for cross-PLC synchronous operation:

| Tag | Description |  |
| --- | --- | --- |
| <TO>.Position | Position of the leading value for local synchronous operation |  |
| <TO>.Velocity | Velocity of the leading value for local synchronous operation |  |
| <TO>.Acceleration | Acceleration of the leading value for local synchronous operation |  |
| <TO>.Interface.AddressIn | Input address for the telegram of the external leading value |  |
| <TO>.Parameter.LocalLeadingValueDelayTime | Delay time of leading value output on the local following axis which, in turn, provides a leading value |  |
| <TO>.Parameter.ToleranceTimeExternalLeadingValueInvalid | Tolerance time until a technology alarm is triggered when the external leading value becomes invalid |  |
| <TO>.StatusExternalLeadingValue.ModuloLength | Modulo length of the external leading value |  |
| <TO>.StatusExternalLeadingValue.ModuloStartValue | Modulo start value of the external leading value |  |
| <TO>.StatusExternalLeadingValue.AdjustmentTime | Time by which the external leading value is adjusted |  |
| < 0 | The external leading value is interpolated by this time. |  |
| > 0 | The external leading value is extrapolated by this time. |  |
| <TO>.StatusWord.X4 (LeadingValueValid) | Validity of the external leading value |  |
| 0 | Leading value does not exist or is not valid |  |
| 1 | Leading value exists and is valid |  |
| <TO>.StatusWord.X5 (LeadingValueModulo) | Modulo functionality |  |
| 0 | Leading value without modulo functionality |  |
| 1 | Leading value with modulo functionality |  |
| <TO>.StatusWord.X6 (LeadingAxisControl) | Follow-up mode |  |
| 0 | Leading axis in follow-up mode |  |
| 1 | Leading axis not in follow-up mode |  |

## Diagnostics (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction to diagnostics (S7-1500, S7-1500T)](#introduction-to-diagnostics-s7-1500-s7-1500t)
- [Synchronous axis technology object (S7-1500, S7-1500T)](#synchronous-axis-technology-object-s7-1500-s7-1500t-1)
- [Cam technology object (S7-1500T)](#cam-technology-object-s7-1500t-1)
- [Leading axis proxy technology object (S7-1500T)](#leading-axis-proxy-technology-object-s7-1500t-1)

### Introduction to diagnostics (S7-1500, S7-1500T)

The description of Motion Control diagnostics is limited to the diagnostics view of the technology objects in TIA Portal, the technology alarms and the error IDs on Motion Control instructions.

The following descriptions can be found in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation:

- [Diagnostics concept](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#diagnostics-concept-s7-1500-s7-1500t-1)
- [Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#technology-alarms-s7-1500-s7-1500t)
- [Error IDs in Motion Control instructions](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#error-ids-in-motion-control-instructions-s7-1500-s7-1500t)

A comprehensive description of the system diagnostics of the S7‑1500 CPU can be found in the ["Diagnostics" function manual](https://support.industry.siemens.com/cs/ww/en/view/59192926).

### Synchronous axis technology object (S7-1500, S7-1500T)

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
| Encoder homed (S7-1500T) | Encoder 1, encoder 2, encoder 3 or encoder 4 is homed with one of the following homing types:  - Active homing - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment   (<TO>.StatusSensor[1..4].Adjusted) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (<TO>.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Status limit switch

The following table shows the possibilities for enabling the software and hardware limit switches:

| Status | Description |
| --- | --- |
| Negative SW limit switch approached | The negative software limit switch has been approached.  (<TO>.StatusWord.X15 (SWLimitMinActive)) |
| Positive SW limit switch approached | The positive software limit switch has been approached.  (<TO>.StatusWord.X16 (SWLimitMaxActive)) |
| Negative HW limit switch approached | The negative hardware limit switch has been approached or overtraveled.  (<TO>.StatusWord.X17 (HWLimitMinActive)) |
| Positive HW limit switch approached | The positive hardware limit switch has been approached or overtraveled.  (<TO>.StatusWord.X18 (HWLimitMaxActive)) |

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
| Stop job active | The axis is stopped and disabled by Motion Control instruction "MC_Stop".  (<TO>.StatusWord2.X0 (StopCommand)) |
| Superimposed motion | The motion of the axis is superimposed by at least one overlapping Motion Control instruction (OR logic operation).  (<TO>.StatusWord.X23 (MoveSuperimposedCommand);  <TO>.StatusWord2.X6 (MotionInSuperimposedCommand);  <TO>.StatusWord2.X7 (HaltSuperimposedCommand)) |

##### Synchronous operation status

| Status | Description |
| --- | --- |
| Synchronization | The axis is synchronized to the leading value of a leading axis.  (<TO>.StatusWord.X21 (Synchronizing)) |
| Synchronous | The axis is synchronized and moves synchronously to the leading axis.  (<TO>.StatusWord.X22 (Synchronous)) |
| Desynchronization (S7‑1500T) | The axis is desynchronized from the leading value of a leading axis.  (<TO>.StatusWord2.X1 (DesynchronizingCommand)) |
| Synchronization pending (S7‑1500T) | A synchronous operation is pending until the leading value reaches the start position for synchronization.  (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 2 or 3) |
| Desynchronization pending (S7‑1500T) | A desynchronization job is pending until the leading value reaches the start position for desynchronization.  (<TO>.StatusSynchronizedMotion.WaitingFunctionState = 4 or 5) |
| Additive leading value active (S7‑1500T) | The axis receives an additive leading value with the Motion Control instruction "MC_LeadingValueAdditive".  (<TO>.StatusSynchronizedMotion.StatusWord.X4 (LeadingValueAdditiveCommand)) |
| Leading value offset (S7-1500T) | The leading value is shifted with the Motion Control instruction "MC_PhasingAbsolute" or "MC_PhasingRelative".  (<TO>.StatusWord.X24 (PhasingCommand)) |
| Leading value offset pending (S7‑1500T) | A job for leading value offset is waiting.  (<TO>.StatusWord2.X3 (PhasingCommandWaiting)) |
| Following value offset (S7-1500T) | The following value is shifted with the Motion Control instruction "MC_OffsetAbsolute" or "MC_OffsetRelative".  (<TO>.StatusWord2.X4 (OffsetCommand)) |
| Following value offset is pending (S7‑1500T) | A job for following value offset is waiting.  (<TO>.StatusWord2.X5 (OffsetCommandWaiting)) |

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
| SW limit switch | A software limit switch has been reached.  (<TO>.ErrorWord.X8 (SWLimit)) |
| HW limit switch | A hardware limit switch has been reached or overtraveled.  (<TO>.ErrorWord.X9 (HWLimit)) |
| Adapt | An error occurred during data adaption.  (<TO>.ErrorWord.X15 (AdaptionError)) |
| Synchronization | An error occurred during synchronization. The leading axis specified for the corresponding Motion Control instruction was not configured as a possible leading axis.  (<TO>.ErrorWord.X14 (SynchronousError)) |

##### Warnings

The following table shows the possible warnings:

| Warning | Description |
| --- | --- |
| Configuration | One or several configuration parameters are adjusted internally at a certain time.  (<TO>.WarningWord.X1 (ConfigWarning)) |
| Job rejected | Job cannot be executed.  You cannot execute a Motion Control instruction because necessary requirements are not fulfilled.  (<TO>.WarningWord.X3 (CommandNotAccepted)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (<TO>.WarningWord.X6 (DynamicWarning)) |
| Synchronization | An error occurred during synchronization. The leading axis specified for the corresponding Motion Control instruction was not configured as a possible leading axis.  (<TO>.WarningWord.X14 (SynchronousWarning)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

#### Motion status (S7-1500, S7-1500T)

You use the "Technology object > Diagnostics > Motion status" diagnostic function in the TIA Portal to monitor the motion status of the axis. The diagnostics function is available in online operation.

##### "Setpoints" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Target position | Current target position of an active positioning job  The target position value is only valid during execution of a positioning job.  (<TO>.StatusPositioning.TargetPosition) |
| Position setpoint | Setpoint position of the axis  (<TO>.Position) |
| Velocity setpoint | Velocity setpoint of the axis  (<TO>.Velocity) |
| Velocity override | Percentage correction of the velocity specification  The velocity setpoint specified in Motion Control instructions or set by the axis control panel is superimposed with an override signal and corrected as a percentage. Valid velocity correction values range from 0.0 % to 200.0 %.  (<TO>.Override.Velocity) |

##### "Current values" area

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Operative encoder | Operative encoder of the axis  (<TO>.OperativeSensor) |
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

This area displays the following parameters contained in the PROFIdrive telegram from the encoder to the controller:

- Status word "Gx_ZSW"
- The actual position value "Gx_XIST1" (cyclic actual encoder value)
- The actual position value "Gx_XIST2" (absolute encoder value)

##### Areas "Encoder 1" to "Encoder 4" (S7-1500T)

The "Encoder 1" to "Encoder 4" areas display the following parameters from the PROFIdrive telegram of the corresponding encoder to the controller:

- Status word "Gx_ZSW"
- The actual position value "Gx_XIST1" (cyclic actual encoder value)
- The actual position value "Gx_XIST2" (absolute encoder value)

### Cam technology object (S7-1500T)

This section contains information on the following topics:

- [Applications of the cam diagnostics (S7-1500T)](#applications-of-the-cam-diagnostics-s7-1500t)
- [Structure of the diagnostics (S7-1500T)](#structure-of-the-diagnostics-s7-1500t)
- [Online view (S7-1500T)](#online-view-s7-1500t)
- [Status and error bits (S7-1500T)](#status-and-error-bits-s7-1500t)
- ["Definition changed" and "Interpolated" status bits (S7-1500T)](#definition-changed-and-interpolated-status-bits-s7-1500t)
- [Filter by segments and points (S7-1500T)](#filter-by-segments-and-points-s7-1500t)
- [Comparing elements (S7-1500T)](#comparing-elements-s7-1500t)
- [Managing snapshots (S7-1500T)](#managing-snapshots-s7-1500t)
- [Exporting and importing snapshots (S7-1500T)](#exporting-and-importing-snapshots-s7-1500t)
- [Printing curve diagram (S7-1500T)](#printing-curve-diagram-s7-1500t)

#### Applications of the cam diagnostics (S7-1500T)

In the cam diagnostics you can monitor and analyze valid points and segments of a cam from the offline and online technology object data block. The values are shown in tables and graphics and correspond to the interpolated offline or online parameters of the technology object data block.

The cam diagnostics in TIA Portal interpolates the current technology object data block parameters independently. In contrast to the cam editor, the diagnostics does not depend on the interpolation in the SIMATIC S7-1500T. The interpolation always refers to the current values in the technology object data block, the so-called snapshot.

The following parameters are taken into account during interpolation.

- <TO>.Point[i]
- <TO>.Segment[i]
- <TO>.VaildPoint[i]
- <TO>.ValidSegment[i]
- <TO>.InterpolationSettings

> **Note**
>
> The term "cam" used in this chapter applies to the technology objects of the "TO_Cam" and "TO_Cam_10k" types.

##### Calling the diagnostics

You can call the diagnostics as follows:

- Project tree > Project> Technology objects > Cam > Diagnostics

##### Possible offline applications

Valid start values of the cam in the project are displayed in a list and represented graphically.

> **Note**
>
> After you have changed values in the cam editor, you must compile the cam. The cam is automatically interpolated, even without a controller or PLCSIM.

Offline, you can:

- Check the interpolation of cams
- Identify points and segments for the same leading value
- Check the calculated velocity, acceleration and jerk
- View and compare saved snapshots
- Check transitions between cams, such as the continuity when changing cams

##### Possible online applications

Valid start values of the cam from the project and the actual values are displayed in a list and graphically represented online.

Online you can also:

- Check the algorithms for calculating the cams in the user program, e.g. the calculation of the coefficients for segments
- Compare a curve generated during runtime with the expected curve
- Monitor status bits and error bits
- Sort points and segments according to the leading value range, even if they are not defined in ascending order according to index in the technology object data block.
- Take, save and compare snapshots. You can use the snapshots later for documentation and additional diagnostics, when you close the TIA Portal project or change the elements of the cam.

#### Structure of the diagnostics (S7-1500T)

The cam diagnostics consists of four areas:

![Figure](images/165349643915_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | List of valid points and segments with toolbar |
| ② | Curve diagram with toolbar |
| ③ | Element comparison |
| ④ | Inspector window |

##### List of valid points and segments

In the list you can find all valid points and segments from the offline and online DB and the saved snapshots. Since you can display the values of the offline configuration and several snapshots, they are provided with expandable headers.

The list consists of the following columns:

| Table column | Description |
| --- | --- |
| Type | In this column, the type of symbol is displayed with a symbol that corresponds to the symbol in the cam editor.  The following element types are recognized:  - Point - Line - Sine - Polynomial |
| Element | points or segments are shown in this column. |
| Start value | The x values for points and the x min. values for segments are shown in this column. |
| Value | The y values for points are shown in this column. When you expand the segments, the following details are shown:  - x min. - x max. - a0 - a1 - a2 - a3 - a4 - a5 - a6 - sineAmplitude - sinePeriod - sinePhase |
| ![List of valid points and segments](images/165349582475_DV_resource.Stream@PNG-de-DE.png) | In this column you can select points/segments for [comparison](#comparing-elements-s7-1500t). |

**Sorting**

You can sort the points and segments in ascending or descending order using the "Element" and "Start value" columns.

**Toolbar**

The toolbar at the top of the list of valid points and segments provides the following functions via buttons:

| Symbol | Function | Description |
| --- | --- | --- |
| ![List of valid points and segments](images/165349713163_DV_resource.Stream@PNG-de-DE.png) | Monitoring On/Off | Monitoring of the cam is started/completed. |
| ![List of valid points and segments](images/165349648907_DV_resource.Stream@PNG-de-DE.png) | Update online curve | The online snapshot is updated. |
| ![List of valid points and segments](images/165349704075_DV_resource.Stream@PNG-de-DE.png) | Print | The "[Print](#printing-curve-diagram-s7-1500t)" dialog will open. |
| ![List of valid points and segments](images/163741864971_DV_resource.Stream@PNG-de-DE.png) | Link list and graphic display for the selected objects | If coupling is enabled and an element is selected in the curve diagram, this element is automatically scrolled to in the list of valid points and segments.  Note: This is only relevant if the list has so many entries that they are not all visible. |
| ![List of valid points and segments](images/165339961611_DV_resource.Stream@PNG-en-US.png) | Select filter | You can select a defined filter. |
| ![List of valid points and segments](images/165349708043_DV_resource.Stream@PNG-de-DE.png) | Defining filter | The "[Define filter](#filter-by-segments-and-points-s7-1500t)" dialog opens. |

##### Curve diagram

Offline, online and saved snapshots are displayed in the curve diagram.  
All valid data from the technology object data block are graphically displayed as a curve. In the curve diagram you can display curves that reflect the position specification, position, velocity, acceleration and jerk. You set the parameters of the displayed curves in the inspector window. You can show or hide the legend using the ![Curve diagram](images/165344791051_DV_resource.Stream@PNG-de-DE.png) icon on the toolbar.

> **Note**
>
> **Refresh the curve displayed in the offline view**
>
> If you change the values in the offline technology object data block, the offline snapshot is automatically reloaded. After you have changed parameters in the cam editor, you must compile the cam. The parameters are then automatically transferred to the technology object data block.

**Toolbar**

The toolbar at the top of the curve diagram provides the following functions via buttons:

| Symbol | Function | Description |
| --- | --- | --- |
| ![Curve diagram](images/165344566027_DV_resource.Stream@PNG-de-DE.png) | Move view | Moving the view using the drag-and-drop feature   To switch from any tool to the "Move view" tool, press the <Esc> key. |
| ![Curve diagram](images/165344684811_DV_resource.Stream@PNG-de-DE.png) | Activate zoom selection | Zoom into selected area |
| ![Curve diagram](images/165344688395_DV_resource.Stream@PNG-de-DE.png) | Activate vertical zoom | Vertical zoom into selected area without horizontal scaling  Alternative: <Ctrl> +drag to ordinate keeping mouse button pressed |
| ![Curve diagram](images/165344691979_DV_resource.Stream@PNG-de-DE.png) | Activate horizontal zoom | Horizontal zoom into selected area without vertical scaling  Alternative: <Ctrl> +drag to abscissa keeping mouse button pressed |
| ![Curve diagram](images/165344699147_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlargement of the display  Alternative: <Ctrl> + mouse wheel up in curve diagram |
| ![Curve diagram](images/165344703115_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduction of the display  Alternative: <Ctrl> + mouse wheel down in curve diagram |
| ![Curve diagram](images/165344695563_DV_resource.Stream@PNG-de-DE.png) | Show all | Display of entire definition and value range |
| ![Curve diagram](images/165345196299_DV_resource.Stream@PNG-de-DE.png) | Zoom into curve | Zoom to the following value range of the curve that you selected in the legend of the chart |
| ![Curve diagram](images/165345276683_DV_resource.Stream@PNG-de-DE.png) | View: A chart with positions | Display of one chart with the following curves of the cam opened in the diagnostics:   - Position specification - Effective position |
| ![Curve diagram](images/165344795019_DV_resource.Stream@PNG-de-DE.png) | View: A chart with all curves | Display of one chart with the following curves of the cam opened in the diagnostics:   - Position specification - Effective position - Effective velocity - Effective acceleration - Effective jerk |
| ![Curve diagram](images/165344798603_DV_resource.Stream@PNG-de-DE.png) | View: Four charts with all curves | Display of four charts with the following curves of the cam opened in the diagnostics:  - Chart with position specification and effective position - Chart with effective velocity - Chart with effective acceleration - Chart with effective jerk |
| ![Curve diagram](images/165344707083_DV_resource.Stream@PNG-de-DE.png) | Vertical measuring lines | Displaying and moving of vertical measuring lines  Hold down the left mouse button and drag to draw a measuring range. The vertical position of the measuring lines can be moved.   The function values for the positions of the measuring lines are displayed in the chart. The difference is displayed between the measuring lines. |
| ![Curve diagram](images/165344787467_DV_resource.Stream@PNG-de-DE.png) | Horizontal measuring lines | Displaying and moving of horizontal measuring lines  Hold down the left mouse button and drag to draw a measuring range. The horizontal position of the measuring lines can be moved.  The function values for the positions of the measuring lines are displayed in the chart. The difference is displayed between the measuring lines. |
| ![Curve diagram](images/165344791051_DV_resource.Stream@PNG-de-DE.png) | Show legend | Showing or hiding of the legend in the curve diagram.  To display values for a specific curve on the ordinate, click on the name of the corresponding curve in the legend. |
| ![Curve diagram](images/165349755275_DV_resource.Stream@PNG-de-DE.png) | Show status and error bits | Show and hide the diagnostics window "[Status and error bits](#status-and-error-bits-s7-1500t)"  You monitor the status of the technology object using the "Status and error bits" diagnostics window. |
| ![Curve diagram](images/165349638795_DV_resource.Stream@PNG-de-DE.png) | Save window settings | Saves of the display settings. |

##### Element comparison

The element comparison is located below the curve diagram. You can select individual points and segments and thus [Analyze and compare elements](#comparing-elements-s7-1500t):

##### Inspector window

In the inspector window you can manage the [Manage snapshots](#managing-snapshots-s7-1500t) in the "General" tab. You can set the decimal places separately in the list of valid points and segments and in the curve diagram.

#### Online view (S7-1500T)

Use the "Monitoring on/off" icon ![Figure](images/165349713163_DV_resource.Stream@PNG-de-DE.png) on the toolbar of the cam diagnostics to switch to the online view.

##### Online view of the list with valid points and segments

In the list with valid points and segments you can find the current online values under "Online snapshot". The start values and values of the elements are highlighted in orange.

##### Online view of the curve diagram

In the curve diagram you can monitor changes to the status of the online cam in the "[Status and error bits](#status-and-error-bits-s7-1500t)" diagnostics window. You can show and hide the window using the ![Online view of the curve diagram](images/165349755275_DV_resource.Stream@PNG-de-DE.png) icon.

##### Online view of the Inspector window

In the list of the current snapshots you can see the online snapshot, whose display you can [manage and save under "Saved snapshots"](#managing-snapshots-s7-1500t).

#### Status and error bits (S7-1500T)

You monitor the status of the technology object using the "Status and error bits" diagnostics window. The diagnostics function is available in online operation.

You can show and hide the diagnostics window using the ![Figure](images/165349755275_DV_resource.Stream@PNG-de-DE.png) icon on the toolbar. You can move the window to a desired position within the curve diagram using drag-and-drop.

The meaning of the status and error bits is described in the following tables.

##### Cam status

The following table shows the possible statuses of the cam:

| Status | Description |
| --- | --- |
| In use | The cam is used.  (<TO>.StatusWord.X0 (Control)) |
| Error | An error occurred at the technology object.  Detailed information about the error is available in the "Error" area and in the "<TO>.ErrorDetail.Number" and "<TO>.ErrorDetail.Reaction" tags of the technology object.  (<TO>.StatusWord.X1 (Error)) |
| Restart active | The technology object is being reinitialized.  (<TO>.StatusWord.X2 (RestartActive)) |
| Copy operation active | A copy operation of an "MC_CopyCamData" job is active.  (<TO>.StatusWord.X7 (CopyCamDataActive)) |
| Definition changed | The definition range of the cam has changed in the technology data block.  (<TO>.StatusWord.X4 (CamDataChanged)) |
| Interpolated | The cam is interpolated.  (<TO>.StatusWord.X5 (Interpolated)) |
| In interpolation | The cam is interpolated.  (<TO>.StatusWord.X6 (InInterpolation)) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (<TO>.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred. One or more configuration parameters are inconsistent or invalid. The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (<TO>.ErrorWord.X1 (ConfigFault)) |
| User program | An error in a Motion Control instruction or during its use has occurred in the user program.  (<TO>.ErrorWord.X2 (UserFault)) |
| Job rejected | A job cannot be executed. You cannot execute a Motion Control instruction because necessary requirements are not fulfilled.  (<TO>.ErrorWord.X3 (CommandNotAccepted)) |

You can access the alarm display via the ![Error](images/165349574539_DV_resource.Stream@PNG-de-DE.png) icon.

##### Warnings

The following table shows the possible warnings:

| Warning | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.WarningWord.X0 (SystemWarning)) |
| Configuration | One or more configuration parameters will be temporarily adjusted internally.  (<TO>.WarningWord.X1 (ConfigWarning)) |
| User program | An error in a Motion Control instruction or during its use has occurred in the user program.  (<TO>.WarningWord.X2 (UserWarning)) |
| Job rejected | Job cannot be executed. You cannot execute a Motion Control instruction because necessary requirements are not fulfilled.  (<TO>.WarningWord.X3 (CommandNotAccepted)) |

You can access the alarm display via the ![Warnings](images/165349574539_DV_resource.Stream@PNG-de-DE.png) icon.

#### "Definition changed" and "Interpolated" status bits (S7-1500T)

Depending on the change in the online technology object data block, the associated status bits are displayed in green.

If you change values in the online technology object data block and they do not match the interpolated values displayed in the curve diagram, the "Definition changed" status bit is displayed in green.

The following message is displayed in the upper part of the cam diagnostics:

"The online values do not correspond to the active interpolated curve. Interpolate the cam and then reload the curve in the graphic display."

**Refresh graphic display**

To display the current values, follow these steps:

1. Interpolate the curve.

   After the interpolation, the "Definition changed" bit is no longer set.

   The "Interpolated" bit is set.

   The note in the banner changes:

   "The curve shown is not current. Update."
2. Click on the "Refresh" icon ![Figure](images/165349648907_DV_resource.Stream@PNG-de-DE.png) on the toolbar or, alternatively, on the "Refresh" link in the message.

   The online snapshot is updated. You can save the online snapshots under "[Saved snapshots](#managing-snapshots-s7-1500t)".

> **Note**
>
> You can also update the diagnostics without re-interpolating the cam after making changes in the technology object data block. The last interpolated cam then remains active in the controller and during camming. The "Interpolated" bit remains set. Before interpolation, you can then analyze the interpolated cam with the new technology object data block parameters in the controller. The "Definition changed" bit then remains TRUE.

#### Filter by segments and points (S7-1500T)

To analyze the relevant elements in extensive cams, you can filter them according to the following criteria:

- Filter segments by index in the technology data block
- Filter segments by segment type
- Filter points by index in the technology data block
- Filter the displayed leading value range

Elements that do not meet the filter criteria are hidden in the list of points and segments and displayed in a lighter shade in the curve diagram than elements that meet the criteria. The filter criteria are applied to all displayed snapshots.

##### Defining and saving filters

To define and save a filter, follow these steps:

1. Click on the ![Defining and saving filters](images/165349708043_DV_resource.Stream@PNG-de-DE.png) icon in the cam diagnostics toolbar.

   The "Define filter" dialog opens.
2. Set the desired filter criteria.
3. Name the filter in the drop-down list.
4. Click "OK".

   The filter is saved and applied.

##### Adding other filters

To add additional filters, proceed as follows:

1. Click on the ![Adding other filters](images/165349708043_DV_resource.Stream@PNG-de-DE.png) icon in the cam diagnostics toolbar.

   The "Define filter" dialog opens.
2. Click the symbol ![Adding other filters](images/165349759243_DV_resource.Stream@PNG-de-DE.png).
3. Set the desired filter criteria.
4. Name the filter in the drop-down list.
5. Click "OK".

   The additional filter is saved, applied and displayed with existing filters in the drop-down list of the toolbar.

##### Adapting existing filters

To adjust existing filters, follow these steps:

1. Click on the ![Adapting existing filters](images/165349708043_DV_resource.Stream@PNG-de-DE.png) icon in the cam diagnostics toolbar.

   The "Define filter" dialog opens.
2. Select the filter to be adjusted from the drop-down list.
3. Adjust the filter criteria.
4. Click "OK".

   The changes are saved and applied.

##### Delete filter

Proceed as follows to delete filter:

1. Click on the ![Delete filter](images/165349708043_DV_resource.Stream@PNG-de-DE.png) icon in the cam diagnostics toolbar.

   The "Define filter" dialog opens.
2. In the drop-down list, select the filter to deleted.
3. Click the symbol ![Delete filter](images/165349764235_DV_resource.Stream@PNG-de-DE.png).
4. Click "OK".

   The filter is deleted.

##### Cancel filter

To cancel a filter, select the "No filter" entry in the drop-down list in the toolbar.

The filter settings are terminated.

#### Comparing elements (S7-1500T)

You can select individual points and segments from various snapshots and compare them in detail.

##### Select elements to compare

You can select items to compare in the following two ways:

- In the "![Select elements to compare](images/165349582475_DV_resource.Stream@PNG-de-DE.png)" column, select valid points or segments.
- In the curve diagram in the shortcut menu, select the element "Show in element comparison".

##### Parameters in the element comparison

For each selected element, the parameters are displayed in a separate window.

> **Note**
>
> You can change the order of the window using the drag-and-drop feature.

Each window contains three expandable areas:

- Element type with mapping in the upper part

  You can expand and collapse the image of the element with the arrow next to the element type.
- Basic parameters

  The basic parameters are read out directly from the technology object data block of the cam.

  For points, the x and y values are displayed.

  The following values are displayed for segments:

  - x min.
  - x max.
  - a0
  - a1
  - a2
  - a3
  - a4
  - a5
  - a6
  - sineAmplitude
  - sinePeriod
  - sinePhase
- Extended parameters

  The extended parameters are not saved directly in the technology object data block. They are calculated by the diagnostics in the TIA Portal.

  For points, the values are displayed depending on the interpolation:

  - With linear interpolation, the velocity in the points is discontinuous. The velocity is displayed to the left (v left) and right (v right) of the point. Acceleration and jerk are not displayed.
  - With cubic interpolation, the jerk in the points is discontinuous. The jerk is displayed to the left (j left) and right (j right) of the point.
  - When interpolating with Bézier splines, the values "y", "v", "a" and "j" from the interpolation result are displayed.

  The following values are displayed for segments:

  - x start
  - x end
  - y min.
  - y max.
  - v start
  - v end
  - v min.
  - v max.
  - a start
  - a end
  - a min.
  - a max.
  - j start
  - j end
  - j min.
  - j max.

> **Note**
>
> The expanding and collapsing of the individual areas and the scrolling are synchronized for all segments and points.

#### Managing snapshots (S7-1500T)

You can manage the displayed curves and snapshots in the inspector window under "Properties > General> Snapshots and curves". In the "Current snapshot" area you can see snapshots that contain valid points and segments from the technology object data block in the following order:

1. Offline configuration
2. Online configuration
3. Saved snapshot

##### Settings of the snapshots

You can expand the snapshots and make the following settings:

| Control element/display element | Meaning |
| --- | --- |
| ![Settings of the snapshots](images/165349846027_DV_resource.Stream@PNG-de-DE.png) | Show and hide the respective snapshot in the curve diagram and in the list of valid points and segments |
| ![Settings of the snapshots](images/165349851147_DV_resource.Stream@PNG-de-DE.png) |  |
| ![Settings of the snapshots](images/165350163723_DV_resource.Stream@PNG-de-DE.png) | Save the snapshot under "Saved snapshot" |
| ![Settings of the snapshots](images/165350099467_DV_resource.Stream@PNG-de-DE.png) | [Export the snapshot](#exporting-and-importing-snapshots-s7-1500t) |
| ![Settings of the snapshots](images/165350104587_DV_resource.Stream@PNG-de-DE.png) | Delete the saved snapshot |
| ![Settings of the snapshots](images/165350108555_DV_resource.Stream@PNG-de-DE.png) | Show and hide individual curves in the curve diagram and in the legend  You can select the color and line shape for each curve. |

The date and time of the recording, the number of segments and points and the type of interpolation are displayed for each snapshot.

You can change the name of saved snapshots.

#### Exporting and importing snapshots (S7-1500T)

You can export and import snapshots.

A list with all snapshots and the "Import snapshot" button can be found in the Inspector window > General tab > Snapshots and curves.

The following formats are supported:

- MCD exchange format
- SIMOTION SCOUT CamTool format
- Binary format

A description of the individual formats can be found in the "[Import/export cam](#importingexporting-cam-s7-1500t)" section.

##### Export snapshot

To export snapshots, follow these steps:

1. For the snapshot you want to export, click the ![Export snapshot](images/165350099467_DV_resource.Stream@PNG-de-DE.png) icon.

   The "Export snapshot" dialog opens.
2. Select the export format and the delimiter.

   - When you select the "Comma" delimiter, the snapshot is exported as CSV file.
   - When you select the "Tabulator" delimiter, the snapshot is exported as TXT file.
3. Enter a file name.
4. Select the target directory.
5. Click the "Export" button.

> **Note**
>
> You can import into the cam configuration a snapshot exported in binary format.

##### Import snapshot

To import snapshots, follow these steps:

1. Click "Import snapshot".

   The "Cam import" dialog opens.
2. Select the format.
3. Select the file.
4. Click the "Open" button.

   The snapshot is displayed in the "Saved snapshots" area.
5. To display the snapshot in the list of valid points and segments and in the curve diagram, select the check box.
6. For the display in the curve diagram, select the color and line shape for the curves.

> **Note**
>
> Exports from the cam configuration can contain elements that are not supported in the cam diagnostics (see "[Structure of the diagnostics](#structure-of-the-diagnostics-s7-1500t)" section). These elements are then displayed as a group of points.

#### Printing curve diagram (S7-1500T)

You have the possibility to print the displayed curves.

##### Procedure

To print the curves displayed in the curve diagram, follow these steps:

1. Show all curves to be printed out.
2. On the toolbar, click the icon ![Procedure](images/165349704075_DV_resource.Stream@PNG-de-DE.png).
3. Select the printer and the document layout.

   To preview the resulting document, click the "Preview" button.
4. Click "Press".

### Leading axis proxy technology object (S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500T)](#status-and-error-bits-s7-1500t-1)
- [Motion status (S7-1500T)](#motion-status-s7-1500t)

#### Status and error bits (S7-1500T)

You use the "Technology object > Diagnostics > Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Leading axis proxy status

The following table shows the possible states of the leading axis proxy:

| Status | Description |
| --- | --- |
| In operation | The technology object is in operation.  (<TO>.StatusWord.X0 (Control)) |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "<TO>.ErrorDetail.Number" and "<TO>.ErrorDetail.Reaction" tags of the technology object.  (<TO>.StatusWord.X1 (Error)) |
| Restart active | The technology object is being reinitialized.  (<TO>.StatusWord.X2 (RestartActive)) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (<TO.>StatusWord.X3 (OnlineStartValuesChanged)) |
| External leading value valid | The external leading value exists and is valid.  (<TO>.StatusWord.X4 (LeadingValueValid)) |
| External leading value with modulo | The external leading value has modulo functionality.  (<TO>.StatusWord.X5 (LeadingValueModulo)) |
| Leading axis in setpoint operation | The leading axis is in setpoint operation.  (<TO>.StatusWord.X6 (LeadingAxisControl)) |

##### Warnings

The following table shows the possible warnings:

| Warning | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.WarningWord.X0 (SystemWarning)) |
| Configuration | One or more configuration parameters are being internally adapted temporarily.  (<TO>.WarningWord.X1 (ConfigWarning)) |
| User program | An error has occurred in the user program.  (<TO>.WarningWord.X2 (UserWarning)) |
| Job rejected | Job cannot be executed.  You cannot execute a Motion Control instruction because necessary requirements are not fulfilled.  (<TO>.WarningWord.X3 (CommandNotAccepted)) |
| Data exchange | An error in the communication has occurred.  (<TO>.WarningWord.X7 (CommunicationWarning)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (<TO>.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (<TO>.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program at a Motion Control instruction or its use.  (<TO>.ErrorWord.X2 (UserFault)) |
| Job rejected | A job cannot be executed.  You cannot execute a Motion Control instruction because necessary requirements are not fulfilled (for example, technology object not homed).  (<TO>.ErrorWord.X3 (CommandNotAccepted)) |
| Data exchange | Communication with a connected device is faulty.   (<TO>.ErrorWord.X7 (CommunicationFault)) |

##### Alarm display

For additional information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

#### Motion status (S7-1500T)

You use the "Technology object > Diagnostics > Motion status" diagnostic function in the TIA Portal to monitor the leading value of the leading axis proxy. The diagnostics function is available in online operation.

##### Leading value for local synchronous operation

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Position | Adapted leading value for local synchronous operation  (<TO>.Position) |
| Velocity | Leading value velocity for local synchronous operation  (<TO>.Velocity) |
| Acceleration | Leading value acceleration for local synchronous operation  (<TO>.Acceleration) |

##### External leading value

The following table shows the meaning of the status data:

| Status | Description |
| --- | --- |
| Modulo length | Modulo length of the external leading value  (<TO>.StatusExternalLeadingValue.ModuloLength) |
| Modulo start value | Modulo start value of the external leading value  (<TO>.StatusExternalLeadingValue.ModuloStartValue) |
| Adjustment time | Time by which the external leading value is adapted  (<TO>.StatusExternalLeadingValue.AdjustmentTime) |

## Tags of the technology object data blocks (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Tags of the synchronous axis technology object (S7-1500, S7-1500T)](#tags-of-the-synchronous-axis-technology-object-s7-1500-s7-1500t)
- [Tags of the cam technology object (S7-1500T)](#tags-of-the-cam-technology-object-s7-1500t)
- [Tags of the leading axis proxy technology object (S7-1500T)](#tags-of-the-leading-axis-proxy-technology-object-s7-1500t)

### Tags of the synchronous axis technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t)
- [Actual values and setpoints (synchronous axis) (S7-1500, S7-1500T)](#actual-values-and-setpoints-synchronous-axis-s7-1500-s7-1500t)
- ["Simulation" tag (synchronous axis) (S7-1500, S7-1500T)](#simulation-tag-synchronous-axis-s7-1500-s7-1500t)
- ["VirtualAxis" tag (synchronous axis) (S7-1500, S7-1500T)](#virtualaxis-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Actor" tag (synchronous axis) (S7-1500, S7-1500T)](#actor-tag-synchronous-axis-s7-1500-s7-1500t)
- ["TorqueLimiting" tag (synchronous axis) (S7-1500, S7-1500T)](#torquelimiting-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Clamping" tag (synchronous axis) (S7-1500, S7-1500T)](#clamping-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Sensor[1..4]" tags (synchronous axis) (S7-1500, S7-1500T)](#sensor14-tags-synchronous-axis-s7-1500-s7-1500t)
- ["CrossPlcSynchronousOperation" tag (synchronous axis) (S7-1500, S7-1500T)](#crossplcsynchronousoperation-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Extrapolation" tag (synchronous axis) (S7-1500, S7-1500T)](#extrapolation-tag-synchronous-axis-s7-1500-s7-1500t)
- ["LoadGear" tag (synchronous axis) (S7-1500, S7-1500T)](#loadgear-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Properties" tag (synchronous axis) (S7-1500, S7-1500T)](#properties-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Units" tag (synchronous axis) (S7-1500, S7-1500T)](#units-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Mechanics" tag (synchronous axis) (S7-1500, S7-1500T)](#mechanics-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Modulo" tag (synchronous axis) (S7-1500, S7-1500T)](#modulo-tag-synchronous-axis-s7-1500-s7-1500t)
- ["DynamicLimits" tag (synchronous axis) (S7-1500, S7-1500T)](#dynamiclimits-tag-synchronous-axis-s7-1500-s7-1500t)
- ["DynamicDefaults" tag (synchronous axis) (S7-1500, S7-1500T)](#dynamicdefaults-tag-synchronous-axis-s7-1500-s7-1500t)
- ["PositionLimits_SW" tag (synchronous axis) (S7-1500, S7-1500T)](#positionlimits_sw-tag-synchronous-axis-s7-1500-s7-1500t)
- ["PositionLimits_HW" tag (synchronous axis) (S7-1500, S7-1500T)](#positionlimits_hw-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Homing" tag (synchronous axis) (S7-1500, S7-1500T)](#homing-tag-synchronous-axis-s7-1500-s7-1500t)
- ["Override" tag (synchronous axis) (S7-1500, S7-1500T)](#override-tag-synchronous-axis-s7-1500-s7-1500t)
- ["PositionControl" tag (synchronous axis) (S7-1500, S7-1500T)](#positioncontrol-tag-synchronous-axis-s7-1500-s7-1500t)
- ["TorquePreControl" tag (synchronous axis) (S7-1500, S7-1500T)](#torqueprecontrol-tag-synchronous-axis-s7-1500-s7-1500t)
- ["SetpointFilter" tag (synchronous axis) (S7-1500, S7-1500T)](#setpointfilter-tag-synchronous-axis-s7-1500-s7-1500t)
- ["DynamicAxisModel" tag (synchronous axis) (S7-1500, S7-1500T)](#dynamicaxismodel-tag-synchronous-axis-s7-1500-s7-1500t)
- ["FollowingError" tag (synchronous axis) (S7-1500, S7-1500T)](#followingerror-tag-synchronous-axis-s7-1500-s7-1500t)
- ["PositioningMonitoring" tag (synchronous axis) (S7-1500, S7-1500T)](#positioningmonitoring-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StandstillSignal" tag (synchronous axis) (S7-1500, S7-1500T)](#standstillsignal-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusPositioning" tag (synchronous axis) (S7-1500, S7-1500T)](#statuspositioning-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusDrive" tag (synchronous axis) (S7-1500, S7-1500T)](#statusdrive-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusServo" tag (synchronous axis) (S7-1500, S7-1500T)](#statusservo-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusProvidedLeadingValue" tag (synchronous axis) (S7-1500, S7-1500T)](#statusprovidedleadingvalue-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusSensor[1..4]" tags (synchronous axis) (S7-1500, S7-1500T)](#statussensor14-tags-synchronous-axis-s7-1500-s7-1500t)
- ["StatusExtrapolation" tag (synchronous axis) (S7-1500, S7-1500T)](#statusextrapolation-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusSynchronizedMotion" tag (synchronous axis) (S7-1500, S7-1500T)](#statussynchronizedmotion-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusKinematicsMotion" tag (synchronous axis) (S7-1500, S7-1500T)](#statuskinematicsmotion-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusTorqueData" tag (synchronous axis) (S7-1500, S7-1500T)](#statustorquedata-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusMotionIn" tag (synchronous axis) (S7-1500, S7-1500T)](#statusmotionin-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusInterpreterMotion" tag (synchronous axis) (S7-1500, S7-1500T)](#statusinterpretermotion-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusWord" tag (synchronous axis) (S7-1500, S7-1500T)](#statusword-tag-synchronous-axis-s7-1500-s7-1500t)
- ["StatusWord2" tag (synchronous axis) (S7-1500, S7-1500T)](#statusword2-tag-synchronous-axis-s7-1500-s7-1500t)
- ["ErrorWord" tag (synchronous axis) (S7-1500, S7-1500T)](#errorword-tag-synchronous-axis-s7-1500-s7-1500t)
- ["ErrorDetail" tag (synchronous axis) (S7-1500, S7-1500T)](#errordetail-tag-synchronous-axis-s7-1500-s7-1500t)
- ["WarningWord" tag (synchronous axis) (S7-1500, S7-1500T)](#warningword-tag-synchronous-axis-s7-1500-s7-1500t)
- ["ControlPanel" tag (synchronous axis) (S7-1500, S7-1500T)](#controlpanel-tag-synchronous-axis-s7-1500-s7-1500t)
- ["InternalToTrace" tag (synchronous axis) (S7-1500, S7-1500T)](#internaltotrace-tag-synchronous-axis-s7-1500-s7-1500t)

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

#### Actual values and setpoints (synchronous axis) (S7-1500, S7-1500T)

The following tags indicate the setpoint and actual values of the technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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
| OperativeSensor | UDINT | 1 … 4 | RON | Operative encoder |  |
| ModuloCycle | DINT | -2147483648 … 2147483647 | RON | Number of modulo cycles of the setpoint |  |
| ActualModuloCycle | DINT | -2147483648 … 2147483647 | RON | Number of modulo cycles of the actual value |  |
| VelocitySetpoint | LREAL | -1.0E12 … 1.0E12 | RON | Output velocity setpoint/speed setpoint |  |

#### "Simulation" tag (synchronous axis) (S7-1500, S7-1500T)

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

#### "VirtualAxis" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.VirtualAxis.<tag name>" contains the configuration of the virtual operation of the axis. A virtual axis is often used as a virtual leading axis in order to generate the setpoints for several real following axes in synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| VirtualAxis. |  | TO_Struct_VirtualAxis |  |  |  |  |
|  | Mode | UDINT | 0, 1 | RON | Virtual axis |  |
| 0 | No virtual axis |  |  |  |  |  |
| 1 | Technology version ≥ V7.0:  The behavior of a virtual axis is identical to the behavior of an axis in simulation. The actual values are generated via the control loop and a simplified drive model.  Technology version ≥ V8.0:  In technology version V8.0, the behavior of the virtual axis has been changed. The behavior of a virtual axis is no longer identical to the behavior of an axis in simulation.  The position and velocity setpoints are directly adopted as actual values with an application cycle delay. The feedback loop and the drive model are not simulated. The dynamic filter is effective.  To maintain compatibility with virtual axes of technology versions ≤ V7.0 for an axis:  1. Interconnect the axis in simulation (<TO>.Simulation.Mode" = 1). 2. Disable the virtual axis (<TO>.VirtualAxisMode = 0) |  |  |  |  |  |

#### "Actor" tag (synchronous axis) (S7-1500, S7-1500T)

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
| EnableDriveOutputAddress | VREF | 0 to 65535 | RON | Address for the "Enable output" for analog setpoint |  |  |  |
| DriveReadyInput | BOOL | - | RES | "Ready input" for analog drives   The analog drive signals its readiness to receive speed setpoints. |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| DriveReadyInputAddress | VREF | 0 to 65535 | RON | Address for the "Enable input" for analog setpoint |  |  |  |
| EnableTorqueData | BOOL | - | RES | Torque data |  |  |  |
| FALSE | Disabled |  |  |  |  |  |  |
| TRUE | Enabled |  |  |  |  |  |  |
| TorqueDataAddressIn | VREF | 0 to 65535 | RON | Input address of the supplemental telegram |  |  |  |
| TorqueDataAddressOut | VREF | 0 to 65535 | RON | Output address of additional telegram |  |  |  |
| DriveParameter. |  | TO_Struct_ActorDriveParameter |  |  | Valid when "<TO>.Actor.MotorType" = 0 |  |  |
|  | ReferenceSpeed | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the speed setpoint (N-set) of the drive  The speed setpoint is transferred in the PROFIdrive telegram as a normalized value from -200% to 200% of the "ReferenceSpeed".  For setpoint specification via an analog output, the analog output can be operated in the range from -117% to 117%, provided the drive permits this. |  |  |
| MaxSpeed | LREAL | 0.0 to 1.0E12 | RES | Maximum value for the speed setpoint of the drive (N-set)  (PROFIdrive: MaxSpeed ≤ 2 × ReferenceSpeed  Analog setpoint: MaxSpeed ≤ 1.17 × ReferenceSpeed) |  |  |  |
| ReferenceTorque | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the drive torque |  |  |  |
| MotorInertia | LREAL | 0.0 to 1.0E12 | DIR | Moment of inertia of the motor |  |  |  |
| LinearMotorDriveParameter. |  | TO_Struct_LinearMotorActorDriveParameter |  |  | Valid when "<TO>.Actor.MotorType" = 1 |  |  |
|  | ReferenceVelocity | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the velocity setpoint (N-set) of the drive  The speed setpoint is transferred in the PROFIdrive telegram as a normalized value from -200% to 200% of the "ReferenceVelocity".  For setpoint specification via an analog value, the analog output can be operated in the range from -117% to 117%, provided the drive permits this. |  |  |
| MaxVelocity | LREAL | 0.0 to 1.0E12 | RES | Maximum value for the velocity setpoint of the drive (N-set)  (PROFIdrive: MaxVelocity ≤ 2 × ReferenceVelocity  Analog setpoint: MaxVelocity ≤ 1.17 × ReferenceVelocity) |  |  |  |
| ReferenceForce | LREAL | 0.0 to 1.0E12 | RES | Reference value (100%) for the force of the drive |  |  |  |
| MotorMass | LREAL | 0.0 to 1.0E12 | DIR | Mass of linear motor |  |  |  |

#### "TorqueLimiting" tag (synchronous axis) (S7-1500, S7-1500T)

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
|  | Torque | LREAL | 0.0 … 1.0E12 | CAL | Limiting torque |  |  |
| Force | LREAL | 0.0 … 1.0E12 | CAL | Limiting force |  |  |  |

#### "Clamping" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Clamping.<tag name>" contains the configuration of the fixed stop detection.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Clamping. |  | TO_Struct_Clamping |  |  |  |
|  | FollowingErrorDeviation | LREAL | 0.001 … 1.0E12 | DIR | Value of the following error starting from which the fixed stop is detected. |
| PositionTolerance | LREAL | 0.001 … 1.0E12 | DIR | Position tolerance for the clamping monitoring |  |

#### "Sensor[1..4]" tags (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Sensor[1..4].<tag name>" contains the controller-end configuration of the encoder and the configuration of active and passive homing.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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
|  | Resolution | LREAL | 1.0E‑12 to 1.0E12 | RES | Resolution of a linear encoder (offset between two encoder pulses) |  |  |
| StepsPerRevolution | UDINT | 1 to 8388608 | RES | Increments per rotary encoder revolution |  |  |  |
| FineResolutionXist1 | UDINT | 0 to 31 | RES | Number of bits for fine resolution "Gx_XIST1" (cyclic actual encoder value) |  |  |  |
| FineResolutionXist2 | UDINT | 0 to 31 | RES | Number of bits for fine resolution "Gx_XIST2" (absolute value of the encoder) |  |  |  |
| DeterminableRevolutions | UDINT | 0 to 8388608 | RES | Number of differentiable encoder revolutions for a multi-turn absolute encoder   (For a single-turn absolute encoder = 1; for an incremental encoder = 0) |  |  |  |
| DistancePerRevolution | LREAL | 0.0 to 1.0E12 | RES | For technology objects < V8.0:  Load distance per revolution of an externally mounted encoder  For technology objects ≥ V8.0:  Load travel per measuring wheel revolution of an externally mounted encoder |  |  |  |
| BehaviorGx_XIST1 | DINT | - | RES | Evaluation of "Gx_XIST1" bits. |  |  |  |
| 0 | Based on the bits of the encoder resolution.  The incremental actual value "Gx_XIST1" is transmitted with less than 32 bits in the PROFIdrive telegram. For example: At 16 bits, the value ranges from 0 to 65,535. |  |  |  |  |  |  |
| 1 | 32-bit value of the encoder value  The "Gx_XIST1" incremental actual value is transferred with 32 bits of 0 to 4,294,967,295 in the PROFIdrive telegram. |  |  |  |  |  |  |
| ReferenceSpeed | LREAL | 0.0 to 1.0E12 | RES | Reference speed for NACT in PROFIdrive telegram with rotary encoder  Only relevant for "ActualVelocityMode" = 1 |  |  |  |
| ReferenceVelocity | LREAL | 0.0 to 1.0E12 | RES | Reference velocity for NACT in the PROFIdrive telegram with linear encoder  Only relevant for "ActualVelocityMode" = 1 |  |  |  |
| Backlash. |  | TO_Struct_Backlash |  |  | u |  |  |
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

#### "CrossPlcSynchronousOperation" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.CrossPlcSynchronousOperation.<tag name>" contains the configuration of the cross-PLC synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CrossPlcSynchronousOperation. |  |  | TO_Struct_CrossPlcSynchronousOperation |  |  |  |  |
|  | Interface[1..8]. |  | ARRAY [1..8] of TO_Struct_CrossPlcLeadingValueInterface |  |  |  |  |
|  | EnableLeadingValueOutput | BOOL | - | RON | Provide cross-PLC leading value |  |  |
| FALSE | No |  |  |  |  |  |  |
| TRUE | Yes |  |  |  |  |  |  |
| AddressOut | VREF | - | RON | Output address for the leading value telegram |  |  |  |
| LocalLeadingValueDelayTime |  | LREAL | 0.0 … 1.0E9 | RES | Delay time of leading value output at the local following axes |  |  |

#### "Extrapolation" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Extrapolation.<tag name>" contains the configuration of the actual value extrapolation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Extrapolation. |  |  | TO_Struct_Extrapolation |  |  |  |  |
|  | LeadingAxisDependentTime |  | LREAL | - | RON | Extrapolation time component (caused by leading axis)  Results from the following times:  - Time of actual value acquisition for the leading axis - Interpolator cycle clock - Time of position filter of actual value extrapolation (T1 + T2) |  |
| FollowingAxisDependentTime |  | LREAL | 0.0 … 1.0E12 | DIR | Extrapolation time component (caused by following axis)  Results from the following times:  - For a following axis with set velocity precontrol:   - Communication cycle   - Interpolator cycle clock   - Speed control loop substitute time for the following axis   - Output delay time of the setpoint at the following axis - For a following axis without velocity precontrol:   - Communication cycle   - Interpolator cycle clock   - Position control loop equivalent time (1/Kv from "<TO>.PositionControl.Kv")   - Output delay time of the setpoint at the following axis |  |  |
| Settings. |  | TO_Struct_ExtrapolationSettings |  |  |  |  |  |
|  | SystemDefinedExtrapolation | DINT | 0, 1 | RES | Leading axis dependent time |  |  |
| 0 | Not effective |  |  |  |  |  |  |
| 1 | Effective |  |  |  |  |  |  |
| ExtrapolatedVelocityMode | DINT | 0, 1 | RES | Effective velocity value for the synchronization function |  |  |  |
| 0 | "FilteredVelocity"  Leading value velocity from filtered actual velocity |  |  |  |  |  |  |
| 1 | "VelocityByDifferentiation"  The leading value velocity results from the differentiation of the extrapolated leading value position |  |  |  |  |  |  |
| PositionFilter. |  | TO_Struct_ExtrapolationPositionFilter |  |  |  |  |  |
|  | T1 | LREAL | 0.0 … 1.0E12 | DIR | Position filter time constant T1 |  |  |
| T2 | LREAL | 0.0 … 1.0E12 | DIR | Position filter time constant T2 |  |  |  |
| VelocityFilter. |  | TO_Struct_ExtrapolationVelocityFilter |  |  |  |  |  |
|  | T1 | LREAL | 0.0 … 1.0E12 | DIR | Velocity filter time constant T1 |  |  |
| T2 | LREAL | 0.0 … 1.0E12 | DIR | Velocity filter time constant T2 |  |  |  |
| VelocityTolerance. |  | TO_Struct_ExtrapolationVelocityTolerance |  |  |  |  |  |
|  | Range | LREAL | 0.0 … 1.0E12 | DIR | Tolerance band width for velocity |  |  |
| Hysteresis. |  | TO_Struct_ExtrapolationHysteresis |  |  |  |  |  |
|  | Value | LREAL | 0.0 … 1.0E12 | DIR | Hysteresis of the extrapolated actual position value |  |  |

#### "LoadGear" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.LoadGear.<tag name>" contains the configuration of the load gear.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| LoadGear. |  | TO_Struct_LoadGear |  |  |  |
|  | Numerator | UDINT | 1 … 4294967295 | RES | Load gear counter |
| Denominator | UDINT | 1 … 4294967295 | RES | Load gear denominator |  |

#### "Properties" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Properties.<tag name>" contains the configuration of the type of axis or motion.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Properties. |  | TO_Struct_Properties |  |  |  |  |
|  | MotionType | DINT | 0, 1 | RON | Indication of axis type or motion type |  |
| 0 | Linear axis or motion |  |  |  |  |  |
| 1 | Rotary axis or motion |  |  |  |  |  |

#### "Units" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Units.<tag name>" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_Struct_Units/TO_Struct_ExternalEncoder_Units |  |  |  |  |
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

#### "Mechanics" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Mechanics.<tag name>" contains the configuration of the mechanics.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| Mechanics. |  | TO_Struct_Mechanics |  |  |  |
|  | LeadScrew | LREAL | 1.0E-12 … 1.0E12 | RES | Leadscrew pitch |

#### "Modulo" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Modulo.<tag name>" contains the configuration of the modulo function.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Modulo. |  | TO_Struct_Modulo |  |  |  |  |
|  | Enable | BOOL | - | RES | FALSE | Modulo conversion disabled |
| TRUE | Modulo conversion enabled |  |  |  |  |  |
| When modulo conversion is enabled, a check is made for modulo length > 0.0 |  |  |  |  |  |  |
| Length | LREAL | 0.001 … 1.0E12 | RES | Modulo length |  |  |
| StartValue | LREAL | -1.0E12 … 1.0E12 | RES | Modulo start value |  |  |

#### "DynamicLimits" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicLimits.<tag name>" contains the configuration of the dynamic limits. During Motion Control, no dynamic values greater than the dynamic limits are permitted. If you specify greater values in a Motion Control instruction, then motion is performed using the dynamic limits, and a warning is indicated (alarms 501 to 503 - dynamic values are limited).

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicLimits. |  | TO_Struct_DynamicLimits |  |  |  |
|  | MaxVelocity | LREAL | 0.0 … 1.0E12 | RES | Maximum permissible velocity of the axis |
| Velocity | LREAL | 0.0 … 1.0E12 | DIR | Current maximum velocity of the axis  The minimum from "MaxVelocity" and "Velocity" is effective for motion control. |  |
| MaxAcceleration | LREAL | 0.0 … 1.0E12 | DIR | Maximum permissible acceleration of the axis |  |
| MaxDeceleration | LREAL | 0.0 … 1.0E12 | DIR | Maximum permissible deceleration of the axis |  |
| MaxJerk | LREAL | 0.0 … 1.0E12 | DIR | Maximum permissible jerk on the axis |  |

#### "DynamicDefaults" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicDefaults.<tag name>" contains the configuration of the dynamic defaults. These settings will be used when you specify a dynamic value less than 0.0 in a Motion Control instruction (exceptions: "MC_MoveJog.Velocity", "MC_MoveVelocity.Velocity"). Changes to the default dynamic values will be applied at the next positive edge at the "Execute" parameter of a Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicDefaults. |  | TO_Struct_DynamicDefaults |  |  |  |
|  | Velocity | LREAL | 0.0 … 1.0E12 | CAL | Default velocity |
| Acceleration | LREAL | 0.0 … 1.0E12 | CAL | Default acceleration |  |
| Deceleration | LREAL | 0.0 … 1.0E12 | CAL | Default deceleration |  |
| Jerk | LREAL | 0.0 … 1.0E12 | CAL | Default jerk |  |
| EmergencyDeceleration | LREAL | 0.0 … 1.0E12 | DIR | Emergency stop deceleration |  |

#### "PositionLimits_SW" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositionLimits_SW.<tag name>" contains the configuration of position monitoring with software limit switches. Software limit switches are used to limit the operating range of a synchronous axis.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| PositionLimits_SW. |  | TO_Struct_PositionLimitsSW |  |  |  |  |
|  | Active | BOOL | - | DIR | FALSE | Monitoring deactivated |
| TRUE | Monitoring activated |  |  |  |  |  |
| MinPosition | LREAL | -1.0E12 … 1.0E12 | DIR | Position of negative software limit switches |  |  |
| MaxPosition | LREAL | -1.0E12 … 1.0E12 | DIR | Position of positive software limit switches ("MaxPosition" > "MinPosition") |  |  |
| LimitReachedBehavior | DINT | 0 … 1 | RES | Alarm response when a software limit switch is approached with a single axis job |  |  |
| 0 | Stop with maximum dynamic values |  |  |  |  |  |
| 1 | Stop with current dynamic values |  |  |  |  |  |
| LimitExceededBehavior | DINT | 0 … 1 | RES | Alarm response when overrunning a software limit switch |  |  |
| 0 | Lock axis |  |  |  |  |  |
| 1 | Keep emergency stop and axis enable |  |  |  |  |  |

#### "PositionLimits_HW" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositionLimits_HW.<tag name>" contains the configuration of position monitoring with hardware limit switches. Hardware limit switches are used to limit the traversing range of a synchronous axis.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| PositionLimits_HW. |  | TO_Struct_PositionLimitsHW |  |  |  |  |
|  | Active | BOOL | - | RES | FALSE | Monitoring deactivated |
| TRUE | Monitoring activated |  |  |  |  |  |
| With "Active", both (negative and positive) hardware limit switches are activated or deactivated. |  |  |  |  |  |  |
| MinSwitchLevel | BOOL | - | RES | Level selection for activation of the negative hardware limit switch |  |  |
| FALSE | Low level (Low active) |  |  |  |  |  |
| TRUE | High level (High active) |  |  |  |  |  |
| MinSwitchAddress | VREF | 0 … 65535 | RES | Address for the negative hardware limit switch |  |  |
| MaxSwitchLevel | BOOL | - | RES | Level selection for activation of the positive hardware limit switch |  |  |
| FALSE | Low level (Low active) |  |  |  |  |  |
| TRUE | High level (High active) |  |  |  |  |  |
| MaxSwitchAddress | VREF | 0 … 65535 | RES | Address for the positive hardware limit switch |  |  |
| Mode | DINT | 0 … 1 | RES | Type of HW limit switch |  |  |
| 0 | Switch non-traversable |  |  |  |  |  |
| 1 | Switch traversable |  |  |  |  |  |
| AppoachBehavior | DINT | 0 … 1 | RES | Alarm response when approaching a HW limit switch |  |  |
| 0 | Disable axis |  |  |  |  |  |
| 1 | Keep emergency stop and axis enable |  |  |  |  |  |

#### "Homing" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Homing.<tag name>" contains the configuration for homing the TO.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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

#### "Override" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.Override.<tag name>" contains the configuration of override parameters. The override parameters are used to apply a correction percentage to default values. An override change takes effect immediately, and is performed with the dynamic settings in effect in the Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Override. |  | TO_Struct_Override |  |  |  |
|  | Velocity | LREAL | 0.0 … 200.0% | DIR | Velocity or speed override  Percentage correction of the velocity/speed |

#### "PositionControl" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositionControl.<tag name>" contains the settings of position control.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PositionControl. |  |  | TO_Struct_PositionControl |  |  |  |  |
|  | Kv |  | LREAL | 0.0 … 2147480.0 | DIR | Proportional gain of the closed loop position control ("Kv" > 0.0) |  |
| Kpc |  | LREAL | 0.0 … 150.0% | DIR | Velocity precontrol of the position control   Recommended setting:  - Isochronous drive connection via PROFIdrive:   100.0% - Non-isochronous drive connection via PROFIdrive:    0.0 to 100.0% - Analog drive connection:    0.0 to 100.0% |  |  |
| EnableDSC |  | BOOL | - | RES | Dynamic Servo Control (DSC) |  |  |
| FALSE | DSC disabled |  |  |  |  |  |  |
| TRUE | DSC activated |  |  |  |  |  |  |
| DSC is only possible with one of the following PROFIdrive telegrams:  - Standard telegram 5 or 6 - SIEMENS telegram 105 or 106 |  |  |  |  |  |  |  |
| SmoothingTimeByChangeDifference |  | LREAL | 0.0 … 1.0E12 s | DIR | Smoothing time for the manipulated variable for switching operations, for example:  - Encoder switchover - Change in P-gain ("Kv") - Switchover to emergency stop ramp |  |  |
| InitialOperativeSensor |  | UDINT | 1 … 4 | RES | Active sensor after initialization of the axis (sensor number 1 to 4)  This encoder is used after startup of the CPU and after a [restart of the technology object](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#restart-of-technology-objects-s7-1500-s7-1500t). At an operating mode transition from STOP → RUN of the CPU (without restart of the technology object), the encoder that was also active before the STOP is still being used. |  |  |
| ControlDifferenceQuantization. |  | TO_Struct_PositionDifferenceQuantification |  |  |  |  |  |
|  | Mode | DINT | - | RES | Type of quantification  Configuration of a quantization when a drive with stepper motor interface is connected |  |  |
| 0 | No quantification |  |  |  |  |  |  |
| 1 | Quantization corresponding to encoder resolution |  |  |  |  |  |  |
| 2 | Quantization to a direct value |  |  |  |  |  |  |
| (configuration is performed using the parameter view (data structure)) |  |  |  |  |  |  |  |
| Value | LREAL | 0.001 … 1.0E12 | RES | Value of quantification  Configuration of a value for quantization to a direct value ("<TO>.PositionControl.ControlDifferenceQuantization.Mode" = 2)  (configuration is performed using the parameter view (data structure)) |  |  |  |
| VelocityModePowerOn |  | DINT | 0 ... 1 | RES | Behavior of the velocity setpoint when the axis is enabled |  |  |
| 0 | Velocity is set to "0" with maximum dynamic values of the axis (ramp). |  |  |  |  |  |  |
| 1 | Velocity is immediately set to "0" without ramp. |  |  |  |  |  |  |

#### "TorquePreControl" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.TorquePreControl.<tag name>" contains the settings of the torque precontrol.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| TorquePreControl. |  | TO_Struct_TorquePreControl |  |  |  |  |
|  | Mode | DINT | 0 … 1 | RES | Mode of torque precontrol (effect only in position-controlled mode) |  |
| 0 | Torque precontrol not in effect |  |  |  |  |  |
| 1 | Torque precontrol based on the acceleration of the axis |  |  |  |  |  |
| Scale | LREAL | 0.0 … 150.0 | DIR | Weighting factor for the value of the torque precontrol [%] |  |  |

#### "SetpointFilter" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.SetpointFilter.<tag name>" contains the settings of the setpoint filter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SetpointFilter. |  |  | TO_Struct_SetpointFilter |  |  |  |  |
|  | DynamicFilter. |  | TO_Struct_DynamicFilter |  |  |  |  |
|  | Mode | DINT | 0 … 2 | RES | Dynamic filter mode |  |  |
| 0 | Dynamic filter not effective |  |  |  |  |  |  |
| 1 | PT1/PT2 filter + dead time |  |  |  |  |  |  |
| 2 | Sliding window demand + dead time |  |  |  |  |  |  |
| T1 | LREAL | 0.0 … 1.0E12 | DIR | First time constant of the sliding window demand  The value is internally limited to the 16-fold servo clock. |  |  |  |
| T2 | LREAL | 0.0 … 1.0E12 | DIR | Second time constant of the sliding window demand  The value is internally limited to the 16-fold servo clock. |  |  |  |
| Tt | LREAL | 0.0 … 1.0E12<sup>1)</sup> | DIR | Additional dead time of the dynamic filter in time unit of the axis |  |  |  |
| <sup>1)</sup> The dead time T<sub>t</sub> is internally limited to sixteen times the value from the application cycle of the MC_Servo. No alarm is output at higher values. |  |  |  |  |  |  |  |

#### "DynamicAxisModel" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.DynamicAxisModel.<tag name>" contains the balancing filter settings.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| DynamicAxisModel. |  | TO_Struct_DynamicAxisModel |  |  | Time constants for braking ramp generation with alarm response "Brake with emergency stop ramp" |
|  | VelocityTimeConstant | LREAL | 0.0 … 1.0E12 | DIR | Speed control loop substitute time [s] |
| AdditionalPositionTimeConstant | LREAL | 0.0 … 1.0E12 | DIR | Additive position control loop substitute time [s] |  |
| CurrentTimeConstant | LREAL | 0.0 … 1.0E12 | DIR | Current control loop substitute time in time unit of the axis |  |

#### "FollowingError" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.FollowingError.<tag name>" contains the configuration of the dynamic following error monitoring.

If the permissible following error is exceeded, then technology alarm 521 is output, and the technology object is disabled (alarm reaction: remove enable).

When the warning level is reached, a warning is output (technology alarm 522).

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| FollowingError. |  | TO_Struct_FollowingError |  |  |  |  |
|  | EnableMonitoring | BOOL | - | RES | FALSE | Following error monitoring deactivated |
| TRUE | Following error monitoring enabled |  |  |  |  |  |
| MinValue | LREAL | Linear:  0.0 … 1.0E12 | DIR | Permissible following error at velocities below the value of "MinVelocity" |  |  |
| Rotary:  0.001 … 1.0E12 |  |  |  |  |  |  |
| MaxValue | LREAL | Linear: 0.0 … 1.0E12 | DIR | Maximum permissible following error, which may be reached at the maximum velocity. |  |  |
| Rotary: 0.002 ... 1.0E12 |  |  |  |  |  |  |
| MinVelocity | LREAL | 0.0 … 1.0E12 | DIR | "MinValue" is permissible below this velocity and is held constant. |  |  |
| WarningLevel | LREAL | 0.0 … 100.0 | DIR | Warning level  Percentage value relative to the valid maximum following error |  |  |
| AdditionalSetpointDelayTime | LREAL | 0.0 … 1.0E12 | DIR | Time constant for additional deceleration of position setpoint to calculate the following error [s] |  |  |

#### "PositioningMonitoring" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.PositioningMonitoring.<tag name>" contains the configuration of position monitoring at the end of a positioning motion.

If the actual position value at the end of a positioning motion is reached within the tolerance time and remains in the positioning window for the minimum dwell time, then "<TO>.StatusWord.X6 (Done)" is set in the technology data block. This completes a Motion Control job.

If the tolerance time is exceeded, then technology alarm 541 "Positioning monitoring" with supplemental value 1: "Target range not reached" is displayed.

If the minimum dwell time is not met, then technology alarm 541 "Positioning monitoring" with supplemental value 2: "Exit target range again" is displayed.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| PositioningMonitoring. |  | TO_Struct_PositionMonitoring |  |  |  |
|  | ToleranceTime | LREAL | 0.0 to 1.0E12 | DIR | Tolerance time  Maximum permitted duration from reaching of velocity setpoint zero until entrance into the positioning window |
| MinDwellTime | LREAL | 0.0 to 1.0E12 | DIR | Minimum dwell time in positioning window |  |
| Window | LREAL | 0.001 to 1.0E12 | DIR | Positioning window |  |

#### "StandstillSignal" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StandstillSignal.<tag name>" contains the configuration of the standstill signal.

If the actual velocity value is below the velocity threshold, and does not exceed it during the minimum dwell time, then the standstill signal "<TO>.StatusWord.X7 (Standstill)" is set.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StandstillSignal. |  | TO_Struct_StandstillSignal |  |  | Configuration for the standstill signal |
|  | VelocityThreshold | LREAL | 0.0 … 1.0E12 | DIR | Velocity threshold  If velocity is below this threshold, the minimum dwell time begins. |
| MinDwellTime | LREAL | 0.0 … 1.0E12 | DIR | Minimum dwell time |  |

#### "StatusPositioning" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusPositioning.<tag name>" indicates the status of a positioning motion.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusPositioning. |  | TO_Struct_StatusPositioning |  |  |  |
|  | Distance | LREAL | -1.0E12 to 1.0E12 | RON | Distance to target position |
| TargetPosition | LREAL | -1.0E12 to 1.0E12 | RON | Target position |  |
| TargetPositionModuloCycle | DINT | -2147483648 to 2147483647 | RON | Number of modulo cycles to target position with positioning motions |  |
| FollowingError | LREAL | -1.0E12 to 1.0E12 | RON | Current following error |  |
| SetpointExecutionTime | LREAL | 0 to 1.0E12 | RON | Setpoint execution time of the axis  (Results from T<sub>Ipo</sub>, T<sub>vtc</sub> or 1/kv, T<sub>Send</sub> and T<sub>O</sub> of the axis) |  |
| SuperimposedDistance | LREAL | 0 to 1.0E12 | RON | Distance traveled with the instructions "MC_MoveSuperimposed", "MC_MotionInSuperimposed", and "MC_HaltSuperimposed".   The value is reset when the base motion and the superimposed motion are completed. |  |

#### "StatusDrive" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusDrive.<tag name>" indicates the status of the drive.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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
| AdaptionState | DINT | 0 … 4 | RON | Status of automatic data transfer of drive parameters |  |  |
| 0 | "NOT_ADAPTED"  Data not transferred |  |  |  |  |  |
| 1 | "IN_ADAPTION"  Data transfer in progress |  |  |  |  |  |
| 2 | "ADAPTED"  Data transfer complete |  |  |  |  |  |
| 3 | "NOT_APPLICABLE"  Data transfer not selected, not possible |  |  |  |  |  |
| 4 | "ADAPTION_ERROR"  Error during data transfer |  |  |  |  |  |

#### "StatusServo" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusServo.<tag name>" indicates the status for the balancing filter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusServo. |  | TO_Struct_StatusServo |  |  |  |
|  | BalancedPosition | LREAL | - | RON | Position setpoint after the balancing filter |
| ControlDifference | LREAL | - | RON | Control deviation |  |
| PositionAfterDynamicFilter | LREAL | - | RON | Position setpoint after the dynamic filter |  |

#### "StatusProvidedLeadingValue" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusProvidedLeadingValue.<tag name>" contains the provided leading value with leading value delay of the cross-PLC synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusProvidedLeadingValue. |  |  | TO_Struct_StatusProvidedLeadingValue |  |  | Provided leading value |
|  | DelayedLeadingValue |  | TO_Struct_ProvidedLeadingValue |  |  | Leading value with leading value delay |
|  | Position | LREAL | -1.0E12 … 1.0E12 | RON | Position |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity |  |  |
| Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration |  |  |

#### "StatusSensor[1..4]" tags (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusSensor[1..4].<tag name>" indicates the status of the measuring system.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusSensor[1..4]. |  | Array [1..4] OF TO_Struct_StatusSensor |  |  |  |  |
|  | State | DINT | 0 … 2 | RON | Status of the actual encoder value |  |
| 0 | "NOT_VALID"  Invalid |  |  |  |  |  |
| 1 | "WAITING_FOR_VALID"  Waiting for "Valid" status |  |  |  |  |  |
| 2 | "VALID"  Valid |  |  |  |  |  |
| CommunicationOK | BOOL | - | RON | Cyclic BUS communication between controller and encoder |  |  |
| FALSE | Not established |  |  |  |  |  |
| TRUE | Established |  |  |  |  |  |
| Error | BOOL | - | RON | FALSE | No error in the measuring system |  |
| TRUE | Error in the measuring system. |  |  |  |  |  |
| AbsEncoderOffset | LREAL | - | RON | Home point offset to the value of an absolute value encoder.  The value will be retentively stored in the CPU. |  |  |
| Control | BOOL | - | RON | FALSE | Encoder is not active |  |
| TRUE | Encoder is active |  |  |  |  |  |
| Position | LREAL | - | RON | Encoder position |  |  |
| Velocity | LREAL | - | RON | Encoder velocity |  |  |
| AdaptionState | DINT | 0 … 4 | RON | Status of automatic data transfer of encoder parameters |  |  |
| 0 | "NOT_ADAPTED"  Data not transferred |  |  |  |  |  |
| 1 | "IN_ADAPTION"  Data transfer in progress |  |  |  |  |  |
| 2 | "ADAPTED"  Data transfer complete |  |  |  |  |  |
| 3 | "NOT_APPLICABLE"  Data transfer not selected, not possible |  |  |  |  |  |
| 4 | "ADAPTION_ERROR"  Error during data transfer |  |  |  |  |  |
| ModuloCycle | DINT | -2147483648 … 2147483647 | RON | Number of modulo cycles |  |  |
| Adjusted | DINT | 0 ... 1 | RON | Status of the encoder adjustment |  |  |
| 0 | Encoder not homed |  |  |  |  |  |
| 1 | Encoder adjusted with one of the following homing types:  - Active homing - Passive homing - Absolute encoder adjustment - Incremental encoder adjustment |  |  |  |  |  |

#### "StatusExtrapolation" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusExtrapolation.<tag name>" indicates the actual value extrapolation status.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusExtrapolation. |  | TO_Struct_StatusExtrapolation |  |  |  |
|  | FilteredPosition | LREAL | -1.0E12 … 1.0E12 | RON | Position after position filter |
| FilteredVelocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity after velocity filter and tolerance band |  |
| ExtrapolatedPosition | LREAL | -1.0E12 … 1.0E12 | RON | Extrapolated position |  |
| ExtrapolatedVelocity | LREAL | -1.0E12 … 1.0E12 | RON | Extrapolated velocity |  |

#### "StatusSynchronizedMotion" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusSynchronizedMotion.<tag name>" indicates the status of synchronous operation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusSynchronizedMotion. |  |  | TO_Struct_StatusSynchronizedMotion |  |  |  |  |
|  | FunctionState |  | DINT | 0 … 6 | RON | Indication of which synchronous operation function is active |  |
| 0 | No synchronous operation active |  |  |  |  |  |  |
| 1 | Gearing ("MC_GearIn") |  |  |  |  |  |  |
| 2 | Gearing with specified synchronous positions ("MC_GearInPos") |  |  |  |  |  |  |
| 3 | Camming ("MC_CamIn") |  |  |  |  |  |  |
| 4 | Desynchronization of gearing ("MC_GearOut") |  |  |  |  |  |  |
| 5 | Desynchronization of camming ("MC_CamOut") |  |  |  |  |  |  |
| 6 | Velocity gearing ("MC_GearInVelocity") |  |  |  |  |  |  |
| WaitingFunctionState |  | DINT | 0 … 5 | RON | Indication of which synchronous operation function is waiting |  |  |
| 0 | No synchronous operation waiting |  |  |  |  |  |  |
| 1 | Reserved |  |  |  |  |  |  |
| 2 | Gearing with specified synchronous positions waiting ("MC_GearInPos") |  |  |  |  |  |  |
| 3 | Camming waiting ("MC_CamIn") |  |  |  |  |  |  |
| 4 | Desynchronization of gearing waiting ("MC_GearOut") |  |  |  |  |  |  |
| 5 | Desynchronization of camming waiting ("MC_CamOut") |  |  |  |  |  |  |
| PhaseShift |  | LREAL | -1.0E12 … 1.0E12 | RON | Current absolute leading value offset with an "MC_PhasingAbsolute" or "MC_PhasingRelative" job. |  |  |
| ActualMaster |  | DB_ANY | 0 … 65535 | RON | When a synchronous operation job is started, the number of the technology data block of the currently used leading axis is displayed. |  |  |
| 0 | Synchronous operation inactive |  |  |  |  |  |  |
| ActualCam |  | DB_ANY | 0 … 65535 | RON | Cyclic cam currently used for camming |  |  |
| MasterOffset |  | LREAL | -1.0E12 … 1.0E12 | RON | Current offset of the leading value range of the cam with an "MC_CamIn" job |  |  |
| MasterScaling |  | LREAL | -1.0E12 … 1.0E12 | RON | Current scaling of the leading value range of the cam with an "MC_CamIn" job |  |  |
| SlaveOffset |  | LREAL | -1.0E12 … 1.0E12 | RON | Current offset of the following value range of the cam with an "MC_CamIn" job |  |  |
| SlaveScaling |  | LREAL | -1.0E12 … 1.0E12 | RON | Current scaling of the following value range of the cam with an "MC_CamIn" job |  |  |
| Offset |  | LREAL | -1.0E12 … 1.0E12 | RON | Current absolute following value offset with an "MC_OffsetAbsolute" or "MC_OffsetRelative" job, including the following value offset of an "MC_CamIn" job (<TO>.StatusSynchronizedMotion.SlaveOffset) |  |  |
| EffectiveLeadingValue. |  | TO_Struct_EffectiveLeadingValue |  |  | Effective leading value of the synchronous operation function |  |  |
|  | Position | LREAL | -1.0E12 … 1.0E12 | RON | Position |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity |  |  |  |
| Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration |  |  |  |
| FunctionLeadingValue. |  | TO_Struct_FunctionLeadingValue |  |  | Leading value of the synchronous operation function after a leading value offset with a "MC_PhasingAbsolute" or "MC_PhasingRelative" job |  |  |
|  | Position | LREAL | -1.0E12 … 1.0E12 | RON | Position |  |  |
| FunctionFollowingValue. |  | TO_Struct_FunctionFollowingValue |  |  | Following value of the synchronous operation function before a following value offset with an "MC_OffsetAbsolute" job or "MC_OffsetRelative" job |  |  |
|  | Position | LREAL | -1.0E12 … 1.0E12 | RON | Position |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity |  |  |  |
| Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration |  |  |  |
| StatusWord. |  | DWORD | - | RON | Status information of synchronous operation |  |  |
|  | Bit 0 | BOOL | - | RON | "Max­Velocity­Exceeded"  Configured maximum velocity is exceeded during synchronous operation. |  |  |
| Bit 1 | BOOL | - | RON | "Max­Acceleration­Exceeded"  Configured maximum acceleration is exceeded during synchronous operation. |  |  |  |
| Bit 2 | BOOL | - | RON | "Max­Deceleration­Exceeded"  Configured maximum deceleration is exceeded during synchronous operation. |  |  |  |
| Bit 3 | BOOL | - | RON | "In­Simulation"  Simulation of synchronous operation |  |  |  |
| FALSE | Not simulated |  |  |  |  |  |  |
| TRUE | Simulated |  |  |  |  |  |  |
| Bit 4 | BOOL | - | RON | "LeadingValueAdditiveCommand"  Additive leading value via "MC_LeadingValueAdditive" |  |  |  |
| FALSE | No additive leading value active |  |  |  |  |  |  |
| TRUE | Additive leading value active |  |  |  |  |  |  |
| Bit 5 …  Bit 31 | BOOL | - | RON | Reserved |  |  |  |

#### "StatusKinematicsMotion" tag (synchronous axis) (S7-1500, S7-1500T)

The "<TO>.StatusKinematicsMotion" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 2 "MaxDecelerationExceeded") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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

#### "StatusTorqueData" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusTorqueData.<tag name>" indicates the status of the torque data.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusTorqueData. |  | TO_Struct_StatusTorqueData |  |  |  |  |
|  | CommandAdditiveTorqueActive | DINT | 0, 1 | RON | Additive setpoint torque |  |
| 0 | Inactive |  |  |  |  |  |
| 1 | Active |  |  |  |  |  |
| CommandTorqueRangeActive | DINT | 0, 1 | RON | Torque limits B +, B- |  |  |
| 0 | Inactive |  |  |  |  |  |
| 1 | Active |  |  |  |  |  |
| ActualTorque | LREAL | -1.0E12 … 1.0E12 | RON | Actual torque of the axis |  |  |
| ActualForce | LREAL | -1.0E12 … 1.0E12 | RON | Actual force of the axis |  |  |
| TotalTorqueAdditive | LREAL | -1.0E12 … 1.0E12 | RON | Effective additional torque of the axis |  |  |
| TotalForceAdditve | LREAL | -1.0E12 … 1.0E12 | RON | Effective additional force of the axis |  |  |

#### "StatusMotionIn" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusMotionIn.<tag name>" indicates the status of the "MotionIn" function.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusMotionIn. |  |  | TO_Struct_StatusMotionIn |  |  |  |  |
|  | FunctionState |  | DINT | 0 … 2 | RON | 0 | No "MotionIn" function active |
| 1 | "MC_MotionInVelocity" active |  |  |  |  |  |  |
| 2 | "MC_MotionInPosition" active |  |  |  |  |  |  |
| StatusWord. |  | DWORD | - | RON | - |  |  |
|  | Bit 0 | Bool | - | RON | "Max­Velocity­Exceeded"  The configured maximum velocity is exceeded during a MotionIn movement. |  |  |
| Bit 1 …  Bit 31 | Bool | - | RON | Reserved |  |  |  |

#### "StatusInterpreterMotion" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.StatusInterpreterMotion.<tag name>" contains status information on motion jobs controlled by a technology object Interpreter.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusInterpreterMotion. |  |  | TO_Struct_StatusInterpreterMotion |  |  |  |
|  | Interpreter |  | DB_ANY | 0 … 65535 |  | Controlling Interpreter technology object |
| StatusWord. |  | DWORD | - | RON | Status information |  |
|  | Bit 0 | - | - | - | "ControlledByInterpreter"  An MCL job is processed or active or the bit is set via the MCL instruction "[setControlledByInterpreter()](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#setcontrolledbyinterpreter-set-controlledbyinterpreter-bit-for-a-technology-object-s7-1500t)". |  |
| Bit 1 | - | - | - | "MotionByInterpreter"  An MCL motion job is in effect. |  |  |
| Bit 2 to Bit 31 | - | - | - | Reserved |  |  |

#### "StatusWord" tag (synchronous axis) (S7-1500, S7-1500T)

The "<TO>.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 5 "HomingDone") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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
| Bit 19 | - | - | - | Reserved |  |
| Bit 20 | - | - | - | Reserved |  |
| Bit 21 | - | - | - | "Synchronizing"  The axis synchronizes to a leading value. |  |
| Bit 22 | - | - | - | "Synchronous"  The axis moves synchronously to a leading value. |  |
| Bit 23 | - | - | - | "MoveSuperimposedCommand"  An "MC_MoveSuperimposed" job is running. |  |
| Bit 24 | - | - | - | "PhasingCommand"  An "MC_PhasingAbsolute" or "MC_PhasingRelative" job for the leading value offset is active. |  |
| Bit 25 | - | - | - | "AxisSimulation"  The technology object is in simulation. |  |
| Bit 26 | - | - | - | "TorqueLimitingCommand"  An "MC_TorqueLimiting" job is running. |  |
| Bit 27 | - | - | - | "InLimitation"<sup>1</sup>  The drive operates at least at the threshold value (default 90%) of the torque limit/force limitation. |  |
| Bit 28 | - | - | - | "NonPositionControlled"  The axis is not in position-controlled mode. |  |
| Bit 29 | - | - | - | "KinematicsMotionCommand"  The axis is used for a kinematics job. |  |
| Bit 30 | - | - | - | "InClamping"  The axis is clamped at a fixed stop. |  |
| Bit 31 | - | - | - | "MotionInCommand"  A "MotionIn" job is running. |  |
| <sup>1</sup> The bit is correctly displayed only when using SIEMENS telegram 10x. When using MC_TorqueRange without SIEMENS telegram 10x, compare the values from telegram 750: <InLimit> = ActualTorque (M_ACT) * 0.9 > UpperTorqueLimit (M_LIMIT_POS) OR ActualTorque (M_ACT) * 0.9 < LowerTorqueLimit (M_LIMIT_NEG) |  |  |  |  |  |

#### "StatusWord2" tag (synchronous axis) (S7-1500, S7-1500T)

The "<TO>.StatusWord2" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 0 "StopCommand") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord2 |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | BOOL | - | RON | "StopCommand"  An "MC_Stop" job is running. The technology object is disabled. |
| Bit 1 | BOOL | - | RON | "DesynchronizingCommand"  An "MC_GearOut" job or "MC_CamOut" job is active. The following axis is desynchronized. |  |
| Bit 2 | BOOL | - | RON | "PassingBacklash"  The backlash is traversed. "<TO>.ActualPosition" does not hereby change. |  |
| Bit 3 | BOOL | - | RON | "PhasingCommandWaiting"  An "MC_PhasingAbsolute" or "MC_PhasingRelative" job for leading value offset is waiting. |  |
| Bit 4 | BOOL | - | RON | "OffsetCommand"  An "MC_OffsetAbsolute" or "MC_OffsetRelative" job for following value offset is active. |  |
| Bit 5 | BOOL | - | RON | "OffsetCommandWaiting"  An "MC_OffsetAbsolute" or "MC_OffsetRelative" job for following value offset is waiting. |  |
| Bit 6 | BOOL | - | RON | "MotionInSuperimposedCommand"  An "MC_MotionInSuperimposed" job is running. |  |
| Bit 7 | BOOL | - | RON | "HaltSuperimposedCommand"  An "MC_HaltSuperimposed" job is running. |  |
| Bit 8 ...  Bit 31 | BOOL | - | RON | Reserved |  |

#### "ErrorWord" tag (synchronous axis) (S7-1500, S7-1500T)

The "<TO>.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

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
| Bit 14 | - | - | - | "SynchronousError"  Error during synchronous operation  The leading axis specified in the Motion Control instruction was not configured as a possible leading axis. |  |
| Bit 15 | - | - | - | "AdaptionError"  Error in automatic data transfer |  |
| Bit 16 ...  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.ErrorDetail.<tag name>" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0 … 5 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 1 | Stop with current dynamic values |  |  |  |  |  |
| 2 | Stop with maximum dynamic values |  |  |  |  |  |
| 3 | Stop with emergency stop ramp |  |  |  |  |  |
| 4 | Remove enable |  |  |  |  |  |
| 5 | Track setpoints |  |  |  |  |  |

#### "WarningWord" tag (synchronous axis) (S7-1500, S7-1500T)

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
| Bit 5 | - | - | - | "SensorWarning"  Error in encoder system |  |
| Bit 6 | - | - | - | "DynamicWarning"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 | - | - | - | "CommunicationWarning"  Communication error  Missing or faulty communication. |  |
| Bit 8 | - | - | - | "SWLimitMin"  The negative software limit switch has been approached. |  |
| Bit 9 | - | - | - | "SWLimitMax"  The positive software limit switch has been approached. |  |
| Bit 10 | - | - | - | "HomingWarning"  Error during homing operation  The homing cannot be completed. |  |
| Bit 11 | - | - | - | "FollowingErrorWarning"  Warning limit of following error monitoring reached/exceeded |  |
| Bit 12 | - | - | - | "PositioningWarning"  Positioning error |  |
| Bit 13 | - | - | - | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14 | - | - | - | "SynchronousWarning"  Error during synchronous operation  The leading axis specified in the Motion Control instruction was not configured as a possible leading axis. |  |
| Bit 15 | - | - | - | "AdaptionWarning"  Error in automatic data transfer |  |
| Bit 16... Bit 31 | - | - | - | Reserved |  |

#### "ControlPanel" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.ControlPanel.<tag name>" contains no relevant data for you. This tag structure is internally used.

#### "InternalToTrace" tag (synchronous axis) (S7-1500, S7-1500T)

The tag structure "<TO>.InternalToTrace.<tag name>" contains no relevant data for you. This tag structure is internally used.

### Tags of the cam technology object (S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500T)](#legend-s7-1500t)
- ["Point[1..1000]" tag (cam of type "TO_Cam") (S7-1500T)](#point11000-tag-cam-of-type-to_cam-s7-1500t)
- ["Point[1..10000]" tag (cam of type "TO_Cam_10k") (S7-1500T)](#point110000-tag-cam-of-type-to_cam_10k-s7-1500t)
- ["ValidPoint[1..1000]" tag (cam of the "TO_Cam" type) (S7-1500T)](#validpoint11000-tag-cam-of-the-to_cam-type-s7-1500t)
- ["ValidPoint[1..10000]" tag (cam of the "TO_Cam_10k" type) (S7-1500T)](#validpoint110000-tag-cam-of-the-to_cam_10k-type-s7-1500t)
- ["Segment[1..50]" tag (cam) (S7-1500T)](#segment150-tag-cam-s7-1500t)
- ["ValidSegment[1..50]" tag (cam) (S7-1500T)](#validsegment150-tag-cam-s7-1500t)
- ["InterpolationSettings" tag (cam) (S7-1500T)](#interpolationsettings-tag-cam-s7-1500t)
- ["StatusCam" tag (cam of the "TO_Cam" type) (S7-1500T)](#statuscam-tag-cam-of-the-to_cam-type-s7-1500t)
- ["StatusCam" tag (cam of the "TO_Cam_10k" type) (S7-1500T)](#statuscam-tag-cam-of-the-to_cam_10k-type-s7-1500t)
- ["StatusWord" tag (cam) (S7-1500T)](#statusword-tag-cam-s7-1500t)
- ["ErrorWord" tag (cam) (S7-1500T)](#errorword-tag-cam-s7-1500t)
- ["ErrorDetail" tag (cam) (S7-1500T)](#errordetail-tag-cam-s7-1500t)
- ["WarningWord" tag (cam) (S7-1500T)](#warningword-tag-cam-s7-1500t)

#### Legend (S7-1500T)

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

#### "Point[1..1000]" tag (cam of type "TO_Cam") (S7-1500T)

The tag structure "<TO>.Point[1..1000].<tag name>" contains the defined points of the cam of type "TO_Cam".

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Point[1..1000]. |  | ARRAY [1..1000] OF TO_Cam_Struct_PointData |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | CAL | Value of the point in the definition range |
| y | LREAL | -1.0E12 … 1.0E12 | CAL | Value of the point in the range of the function |  |

#### "Point[1..10000]" tag (cam of type "TO_Cam_10k") (S7-1500T)

The tag structure "<TO>.Point[1..10000].<tag name>" contains the defined points of the cam of type "TO_Cam_10k".

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Point[1..10000]. |  | ARRAY [1..10000] OF TO_Cam_Struct_PointData |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | CAL | Value of the point in the definition range |
| y | LREAL | -1.0E12 … 1.0E12 | CAL | Value of the point in the range of the function |  |

#### "ValidPoint[1..1000]" tag (cam of the "TO_Cam" type) (S7-1500T)

The tag structure "<TO>.ValidPoint[1..1000]" shows the validity of the defined points of the cam of type "TO_Cam".

##### Tags

[Legend](#legend-s7-1500t)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| ValidPoint[1..1000] | ARRAY [1..1000] OF BOOL | - | CAL | Indicates whether the defined point is valid. |  |
| FALSE | Invalid |  |  |  |  |
| TRUE | Valid |  |  |  |  |

#### "ValidPoint[1..10000]" tag (cam of the "TO_Cam_10k" type) (S7-1500T)

The tag structure "<TO>.ValidPoint[1..10000]" shows the validity of the defined points of the cam of type "TO_Cam_10k".

##### Tags

[Legend](#legend-s7-1500t)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| ValidPoint[1..10000] | ARRAY [1..10000] OF BOOL | - | CAL | Indicates whether the defined point is valid. |  |
| FALSE | Invalid |  |  |  |  |
| TRUE | Valid |  |  |  |  |

#### "Segment[1..50]" tag (cam) (S7-1500T)

The tag structure "<TO>.Segment[1..50].<tag name>" contains the defined segments of the cam.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Segment[1..50]. |  | ARRAY [1..50] OF TO_Cam_Struct_SegmentData |  |  |  |
|  | xmin | LREAL | -1.0E12 … 1.0E12 | CAL | Start coordinates of the segment |
| xmax | LREAL | -1.0E12 … 1.0E12 | CAL | End coordinates of the segment |  |
| a0 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A0 for x<sup>0</sup> of the polynomial for the segment |  |
| a1 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A1 for x<sup>1</sup> of the polynomial for the segment |  |
| a2 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A2 for x<sup>2</sup> of the polynomial for the segment |  |
| a3 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A3 for x<sup>3</sup> of the polynomial for the segment |  |
| a4 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A4 for x<sup>4</sup> of the polynomial for the segment |  |
| a5 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A5 for x<sup>5</sup> of the polynomial for the segment |  |
| a6 | LREAL | -1.0E12 … 1.0E12 | CAL | Coefficient A6 for x<sup>6</sup> of the polynomial for the segment |  |
| sineAmplitude | LREAL | -1.0E12 … 1.0E12 | CAL | Amplitude of the sine element |  |
| sinePeriod | LREAL | -1.0E12 … 1.0E12 | CAL | Period length of the sine element [rad] |  |
| sinePhase | LREAL | -1.0E12 … 1.0E12 | CAL | Phase offset of the sine element [rad] |  |

#### "ValidSegment[1..50]" tag (cam) (S7-1500T)

The "<TO>.ValidSegment[1..50]" tag structure indicates the validity of the defined segments of the cam.

##### Tags

[Legend](#legend-s7-1500t)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| ValidSegment[1..50] | ARRAY [1..50] OF BOOL | - | CAL | Indicates whether the defined segment is valid. |  |
| FALSE | Invalid |  |  |  |  |
| TRUE | Valid |  |  |  |  |

#### "InterpolationSettings" tag (cam) (S7-1500T)

The tag structure "<TO>.InterpolationSettings.<tag name>" contains the configuration for the interpolation of the cam.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| InterpolationSettings. |  | TO_Cam_Struct_InterpolationSettings |  |  |  |  |
|  | InterpolationMode | DINT | 0 … 2 | CAL | Interpolation type |  |
| 0 | Linear |  |  |  |  |  |
| 1 | C splines |  |  |  |  |  |
| 2 | B splines |  |  |  |  |  |
| BoundaryConditions | DINT | 0, 1 | CAL | Characteristics of the boundary points |  |  |
| 0 | No profile start or profile end conditions |  |  |  |  |  |
| 1 | First derivative equal at profile start and end |  |  |  |  |  |

#### "StatusCam" tag (cam of the "TO_Cam" type) (S7-1500T)

The tag structure "<TO>.StatusCam.<tag name>" indicates the status of the cam.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusCam. |  | TO_Cam_Struct_StatusCam |  |  |  |
|  | StartLeadingValue | LREAL | -1.0E12 … 1.0E12 | RON | First defined interpolation point/start of the first segment of the cam  (Start value of the definition range of the cam) |
| EndLeadingValue | LREAL | -1.0E12 … 1.0E12 | RON | Last defined interpolation point/end of the last segment of the cam  (End value of the definition range of the cam) |  |
| NumberOfValidPoints | DINT | 0 … 1 000 | RON | Number of valid points  ("ValidPoint" = TRUE) |  |
| NumberOfValidSegments | DINT | 0 … 50 | RON | Number of valid segments  ("ValidSegment" = TRUE) |  |

#### "StatusCam" tag (cam of the "TO_Cam_10k" type) (S7-1500T)

The tag structure "<TO>.StatusCam.<tag name>" indicates the status of the cam.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusCam. |  | TO_Cam_Struct_StatusCam |  |  |  |
|  | StartLeadingValue | LREAL | -1.0E12 … 1.0E12 | RON | First defined interpolation point/start of the first segment of the cam  (Start value of the definition range of the cam) |
| EndLeadingValue | LREAL | -1.0E12 … 1.0E12 | RON | Last defined interpolation point/end of the last segment of the cam  (End value of the definition range of the cam) |  |
| NumberOfValidPoints | DINT | 0 … 10 000 | RON | Number of valid points  ("ValidPoint" = TRUE) |  |
| NumberOfValidSegments | DINT | 0 … 50 | RON | Number of valid segments  ("ValidSegment" = TRUE) |  |

#### "StatusWord" tag (cam) (S7-1500T)

The "<TO>.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 4 "CamDataChanged") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Control"  Use status  The cam is in use. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is being reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "CamDataChanged"  The definition range of the cam has changed in the technology data block. |  |
| Bit 5 | - | - | - | "Interpolated"  The cam is interpolated. |  |
| Bit 6 | - | - | - | "InInterpolation"   The cam is in interpolation. |  |
| Bit 7 | - | - | - | "CopyCamDataActive"  A copy operation of an "MC_CopyCamData" job is active. |  |
| Bit 8 … Bit 31 | - | - | - | Reserved |  |

#### "ErrorWord" tag (cam) (S7-1500T)

The "<TO>.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 …  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (cam) (S7-1500T)

The tag structure "<TO>.ErrorDetail.<tag name>" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 9 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 9 | Terminate processing of the technology object |  |  |  |  |  |

#### "WarningWord" tag (cam) (S7-1500T)

The "<TO>.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 …  Bit 31 | - | - | - | Reserved |  |

### Tags of the leading axis proxy technology object (S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500T)](#legend-s7-1500t-1)
- [Leading value (leading axis proxy) (S7-1500T)](#leading-value-leading-axis-proxy-s7-1500t)
- ["Interface" tag (leading axis proxy) (S7-1500T)](#interface-tag-leading-axis-proxy-s7-1500t)
- ["Parameter" tag (leading axis proxy) (S7-1500T)](#parameter-tag-leading-axis-proxy-s7-1500t)
- ["StatusExternalLeadingValue" tag (leading axis proxy) (S7-1500T)](#statusexternalleadingvalue-tag-leading-axis-proxy-s7-1500t)
- ["StatusWord" tag (leading axis proxy) (S7-1500T)](#statusword-tag-leading-axis-proxy-s7-1500t)
- ["'ErrorWord" tag (leading axis proxy) (S7-1500T)](#errorword-tag-leading-axis-proxy-s7-1500t)
- ["ErrorDetail" tag (leading axis proxy) (S7-1500T)](#errordetail-tag-leading-axis-proxy-s7-1500t)
- ["WarningWord" tag (leading axis proxy) (S7-1500T)](#warningword-tag-leading-axis-proxy-s7-1500t)

#### Legend (S7-1500T)

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

#### Leading value (leading axis proxy) (S7-1500T)

The following tags indicate the leading value parameters of the technology object for local synchronous operation.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag | Data type | Values | W | Description |
| --- | --- | --- | --- | --- |
| Position | LREAL | - | RON | Adapted leading value for local synchronous operation |
| Velocity | LREAL | - | RON | Leading value velocity for local synchronous operation |
| Acceleration | LREAL | - | RON | Leading value velocity for local synchronous operation |

#### "Interface" tag (leading axis proxy) (S7-1500T)

The tag structure "<TO>.Interface.<Tag name>" contains the input address of the telegram.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Interface. |  | TO_Struct_LeadingAxisProxy_Interface |  |  |  |
|  | AddressIn | VRef | - | RON | Input address for the telegram of the external leading value |

#### "Parameter" tag (leading axis proxy) (S7-1500T)

The tag structure "<TO>.Parameter.<tag name>" contains parameters for leading value adaptation.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Parameter. |  | TO_Struct_LeadingAxisProxy_Parameter |  |  |  |
|  | LocalLeadingValueDelayTime | LREAL | 0.0 … 1.0E9 | DIR | Delay time of virtual local following axis which, in turn, provides a cross-PLC leading value with a cascade (<TO>.CrossPlcSynchronousOperation.LocalLeadingValueDelayTime) |
| ToleranceTimeExternalLeadingValueInvalid | LREAL | 0.0 … 1.0E12 | DIR | Tolerance time until a technology alarm is triggered when the external leading value becomes invalid |  |

#### "StatusExternalLeadingValue" tag (leading axis proxy) (S7-1500T)

The tag structure "<TO>.StatusExternalLeadingValue.<Tag name>" contains the parameter values of the external leading value.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusExternalLeadingValue. |  | TO_Struct_LeadingAxisProxy_StatusData |  |  |  |  |
|  | ModuloLength | LREAL | 0.0 … 1.0E12 | RON | Modulo length of the external leading value |  |
| ModuloStartValue | LREAL | -1.0E12 … 1.0E12 | RON | Modulo start value of the external leading value |  |  |
| AdjustmentTime | LREAL | -1.0E12 … 1.0E12 | RON | Time by which the external leading value is adjusted |  |  |
| < 0 | The external leading value is interpolated by this time. |  |  |  |  |  |
| > 0 | The external leading value is extrapolated by this time. |  |  |  |  |  |

#### "StatusWord" tag (leading axis proxy) (S7-1500T)

The "<TO>.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 4 "LeadingValueValid") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Control"  Use status  The leading axis proxy is in operation. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is being reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "LeadingValueValid"  The leading value exists and is valid. |  |
| Bit 5 | - | - | - | "LeadingValueModulo"  The leading value is with modulo functionality. |  |
| Bit 6 | - | - | - | "LeadingAxisControl"  The leading axis is in setpoint operation. |  |
| Bit 7 …  Bit 31 | - | - | - | Reserved |  |

#### "'ErrorWord" tag (leading axis proxy) (S7-1500T)

The "<TO>.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  System error |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 …  Bit 7 | - | - | - | Reserved |  |
| Bit 7 | - | - | - | "CommunicationFault"  Communication error  Missing or faulty communication. |  |
| Bit 8 …  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (leading axis proxy) (S7-1500T)

The tag structure "<TO>.ErrorDetail.<tag name>" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 13 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 13 | Invalid leading value |  |  |  |  |  |

#### "WarningWord" tag (leading axis proxy) (S7-1500T)

The "<TO>.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 1 "ConfigWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 …  Bit 6 | - | - | - | Reserved |  |
| Bit 7 | - | - | - | "CommunicationWarning"  Communication error  Missing or faulty communication. |  |
| Bit 8 …  Bit 31 | - | - | - | Reserved |  |
