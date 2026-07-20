---
title: "Using S7-1500/S7-1500T Measuring input and output cam functions (S7-1500, S7-1500T)"
package: TFTOSMCSignalenUS
topics: 90
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using S7-1500/S7-1500T Measuring input and output cam functions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Basics (S7-1500, S7-1500T)](#basics-s7-1500-s7-1500t)
- [Configuring (S7-1500, S7-1500T)](#configuring-s7-1500-s7-1500t)
- [Diagnostics (S7-1500, S7-1500T)](#diagnostics-s7-1500-s7-1500t)
- [Tags of the technology object data blocks (S7-1500, S7-1500T)](#tags-of-the-technology-object-data-blocks-s7-1500-s7-1500t)

## Basics (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Functions (S7-1500, S7-1500T)](#functions-s7-1500-s7-1500t)
- [Measuring input technology object (S7-1500, S7-1500T)](#measuring-input-technology-object-s7-1500-s7-1500t)
- [Output cam technology object (S7-1500, S7-1500T)](#output-cam-technology-object-s7-1500-s7-1500t)
- [Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)

### Functions (S7-1500, S7-1500T)

You execute the functions of the measuring input, output cam and cam track technology objects via the Motion Control instructions in your user program.

The following table shows the Motion Control instructions that are supported by the technology objects:

| Motion Control instruction | Validity |  | Technology object |  |  |
| --- | --- | --- | --- | --- | --- |
| S7-1500 | S7-1500T | [Measuring input](#short-description-of-the-measuring-input-technology-object-s7-1500-s7-1500t) | [Output cam](#short-description-of-the-output-cam-technology-object-s7-1500-s7-1500t) | [Cam track](#short-description-of-the-cam-track-technology-object-s7-1500-s7-1500t) |  |
| "[MC_Reset](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_reset-v8-s7-1500-s7-1500t)"  Acknowledge alarms, restart technology objects | ✓ | ✓ | ✓ | ✓ | ✓ |
| "[MC_MeasuringInput](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_measuringinput-v8-s7-1500-s7-1500t)"  Start measuring once | ✓ | ✓ | ✓ | - | - |
| "[MC_MeasuringInputCyclic](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_measuringinputcyclic-v8-s7-1500-s7-1500t)"  Start cyclic measuring | ✓ | ✓ | ✓ | - | - |
| "[MC_AbortMeasuringInput](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_abortmeasuringinput-v8-s7-1500-s7-1500t)"  Cancel active measuring job | ✓ | ✓ | ✓ | - | - |
| "[MC_OutputCam](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_outputcam-v8-s7-1500-s7-1500t)"  Activate/deactivate output cam | ✓ | ✓ | - | ✓ | - |
| "[MC_CamTrack](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_camtrack-v8-s7-1500-s7-1500t)"  Activate/deactivate cam track | ✓ | ✓ | - | - | ✓ |

### Measuring input technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of the measuring input technology object (S7-1500, S7-1500T)](#short-description-of-the-measuring-input-technology-object-s7-1500-s7-1500t)
- [Measuring (S7-1500, S7-1500T)](#measuring-s7-1500-s7-1500t)
- [Measuring with measuring range (S7-1500, S7-1500T)](#measuring-with-measuring-range-s7-1500-s7-1500t)
- [Use a measurement input for several axes (S7-1500, S7-1500T)](#use-a-measurement-input-for-several-axes-s7-1500-s7-1500t)
- [Time-related boundary conditions (S7-1500, S7-1500T)](#time-related-boundary-conditions-s7-1500-s7-1500t)
- [Tags: Measuring input technology object (S7-1500, S7-1500T)](#tags-measuring-input-technology-object-s7-1500-s7-1500t)

#### Short description of the measuring input technology object (S7-1500, S7-1500T)

![Figure](images/169054025867_DV_resource.Stream@PNG-de-DE.png)

The measuring input technology object acquires the actual position of an axis or external encoder at a signal change at the measuring input.

You can find an overview of the functions of the measuring input technology object in the "[Functions](#functions-s7-1500-s7-1500t)" section.

The following figure shows the basic principle of operation of the measuring input technology object:

![Figure](images/169054132491_DV_resource.Stream@PNG-en-US.png)

##### Measurement types

The following types of measurement can be performed:

- [One-time measurement](#one-time-measurement-s7-1500-s7-1500t)

  Up to two measured values are acquired with edge accuracy with one measuring job. A one-time measuring job is started with "MC_MeasuringInput".
- [Cyclic measuring](#cyclic-measuring-s7-1500-s7-1500t)

  With cyclic measuring, up to two measured values are acquired with edge accuracy in each position control cycle.

  A cyclic measuring job is started with "MC_MeasuringInputCyclic". The measurements are continued cyclically until they are ended per command.

The edges to be detected are selected when starting the measurement using Motion Control instruction "MC_MeasuringInput" or "MC_MeasuringInputCyclic".

##### Assignment

The measuring input technology object must always be assigned to another technology object whose position will be evaluated by the measuring input.

The measuring input technology object can be assigned to the following technology objects:

- Synchronous axis
- Positioning axis
- External encoder

![Assignment](images/169054137483_DV_resource.Stream@PNG-en-US.png)

Exactly one axis or one external encoder can be assigned to a measuring input technology object.

An axis or external encoder can be assigned multiple measuring input technology objects.

##### Measured value determination

The position can be detected using support from the hardware in one of the following ways:

- **Measurement using Timer DI**

  With measured value acquisition via time value, the time points of the signal changes are recorded precisely. The time stamps are then transferred to the controller and the associated actual positions are determined in the technology object.

  Measurement using Timer DI requires isochronous mode.
- **Measurement using** 
  **SINAMICS**
   **(central probe)**

  With central measuring inputs, the time points of the signal changes are recorded precisely. The time stamps are then transferred to the controller via telegram 39x and the associated actual positions are determined in the technology object.

  Measurements via a central measuring input are only possible for SINAMICS drives, see "[Compatibility list](https://support.industry.siemens.com/cs/ww/en/view/109750431)". The maximum usable cycle time on the bus is limited, see "[Time-related boundary conditions](#time-related-boundary-conditions-s7-1500-s7-1500t)".

  Measurement using SINAMICS (central probe) requires isochronous mode.

  You can find more information on the telegrams in the "[PROFIdrive telegrams configuration](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#configuring-profidrive-telegrams-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Axis functions" documentation.
- **Measurement using** 
  **PROFIdrive**
   **telegram (drive or external encoder)**

  With measurement using PROFIdrive telegram, the measurement input is connected to the drive device and measurement takes place directly in the drive. The position value is determined on a signal change at the measurement input. The drive or encoder module communicates the determined position value to the technology object via the PROFIdrive telegram.

  With measurement using PROFIdrive telegram, only one measurement input at a time can be active on an actual value or encoder in the PROFIdrive telegram. A maximum of two measuring inputs can be configured on an actual value or encoder in the PROFIdrive telegram via PROFIdrive; see section "[Automatic transfer of drive and encoder parameters in the device](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Axis functions" documentation.
- **Measuring via monitoring**

  During measuring via monitoring. the measuring event of a measurement input is captured by multiple measuring probes. The monitoring probes are assigned to the measuring probes with measurement input.

  No measured signal on the hardware is assigned to the monitoring probes.

  Position detection with the monitoring probes is only possible when the measuring type "measuring via timer DI" or "Measuring via SINAMICS" is enabled for the measuring probe with measurement input.

**Measuring job**

A measuring job is started using the Motion Control instruction "MC_MeasuringInput" (one-time measuring) or "MC_MeasuringInputCyclic" (cyclic measuring). Cyclic measuring is only available at selected measurement inputs. You can find an overview in the "[Configuration - Hardware interface](#configuration---hardware-interface-s7-1500-s7-1500t)" section. One-time measuring is always possible.

The resulting measured value is indicated at the respective output of the Motion Control instruction "MC_MeasuringInput" or "MC_MeasuringInputCyclic".

**Use with** 
**SIMATIC S7-PLCSIM**

The measuring input technology object cannot be used with SIMATIC S7-PLCSIM. The measuring input technology object and the measuring input jobs used in the user program can be loaded into SIMATIC S7-PLCSIM, but have no function. Measured values are not shown.

##### Correction time

The time of the measurement can be corrected by setting a correction time (&lt;TO&gt;.Parameter.CorrectionTime) for the measuring input technology object.

Corrections may be required for the following examples:

- Times for mechanical displacement of the measuring input
- Times for the generation of the measured signal before the measurement input
- Filter times at measurement input

The correction time is included in the calculation for all measuring input types of the measuring input technology object.

Also note the time delay when measuring on a virtual axis, see section "Virtual axis" of the ["S7-1500/S7-1500T Axis functions" documentation](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#virtual-axis-s7-1500-s7-1500t).

#### Measuring (S7-1500, S7-1500T)

This section contains information on the following topics:

- [One-time measurement (S7-1500, S7-1500T)](#one-time-measurement-s7-1500-s7-1500t)
- [Cyclic measuring (S7-1500, S7-1500T)](#cyclic-measuring-s7-1500-s7-1500t)

##### One-time measurement (S7-1500, S7-1500T)

With one-time measurement, up to two edges can be detected with one measuring job. The associated actual positions are signaled back in the function block and in the technology data block and can be further processed in the user program.

###### Measuring job

A measuring job is started using the Motion Control instruction "MC_MeasuringInput". The "&lt;TO&gt;.Status" tag in the technology data block changes to "WAITING_FOR_TRIGGER". The technology object activates the measurement when the selected edge is detected.

- The measurement occurs at the measurement input in the form of up to two system times. Based on the times, the associated position is determined and output, taking into consideration a correction time, if present.
- With direct position detection, the detected position value is supplied directly from the drive or encoder module to the technology object via the PROFIdrive telegram.

The measurement is then finished. An additional measurement must be restarted using Motion Control instruction "MC_MeasuringInput".

| Configured "Mode" parameter in Motion Control instruction "MC_MeasuringInput" | Output of Motion Control instruction "MC_MeasuringInput" |  |
| --- | --- | --- |
| "MeasuredValue1" | "MeasuredValue2" |  |
| Measure positive edge only | Actual position at the time of the edge | – |
| Measure negative edge only |  |  |
| Measure the next two edges | Actual position at the time of the first edge | Actual position at the time of the second edge |
| Measure the next two edges starting with the positive edge | Actual position at the time of the positive edge | Actual position at the time of the negative edge |
| Measure the next two edges starting with the negative edge | Actual position at the time of the negative edge | Actual position at the time of the positive edge |

The last detected values are set in the technology data block. If a new job is initiated with the function block, the outputs of the function block are initialized. The technology data block is not initialized. After detecting the first valid measuring cycle, the values in the technology data block and function block are consistent with one another.

The finished measuring job is indicated in the function block in "MC_MeasuringInput.DONE" = TRUE or in the technology data block in "&lt;TO&gt;.Status" = "TRIGGER_OCCURRED".

###### Temporal requirements for measuring jobs via "MC_MeasuringInput"

The hardware-related restrictions to measuring via the PROFIdrive telegram (drive or encoder) or measuring via SINAMICS (central probe) result in time requirements for the period until the measuring event can be recorded.

When measuring once via "MC_MeasuringInput" with "Mode" = 3 (measurement at both edges, beginning with the rising edge) or "Mode" = 4 (measurement at both edges, beginning with the falling edge), a minimum interval of several servo cycles is therefore required between the first edge to be measured and the previous edge, so that the first edge to be measured can be recorded.

You can find information on the temporal boundary conditions in the section [Time-related boundary conditions](#time-related-boundary-conditions-s7-1500-s7-1500t).

---

**See also**

[Time-related boundary conditions (S7-1500, S7-1500T)](#time-related-boundary-conditions-s7-1500-s7-1500t)
  
[MC_MeasuringInput: Start measuring once V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_measuringinput-start-measuring-once-v8-s7-1500-s7-1500t)

##### Cyclic measuring (S7-1500, S7-1500T)

With cyclic measuring, up to two measuring events can be acquired by the system in each position control cycle of the technology object and the associated measuring positions can be displayed. The measurements are continued cyclically until they are ended per command.

The determined measured values are displayed and can be read by the user program.

Cyclic measuring requires the measured value to be determined using hardware support of the type "Measurement using Timer DI" or "Measurement using SINAMICS".

Measuring edges at which a measured value could not be determined are indicated in a lost edge counter in the technology data block as well as in function block "MC_MeasuringInputCyclic".

###### Measuring job

A cyclic measuring job is started with Motion Control instruction "MC_MeasuringInputCyclic" and the measuring job is issued to the corresponding measuring hardware. Depending on the functionality of the hardware, up to two measuring events and thus measuring times can be recorded with edge reference per position control cycle and then forwarded to the technology object. The technology object determines the measuring positions for the measuring times taking into consideration any specified correction times.

The technology data block tag "&lt;TO&gt;.Status" changes from "INACTIVE" to "WAITING_FOR_TRIGGER" and remains in this status as long as additional events are awaited.

The mode set in the Motion Control instruction specifies the edges for which the measured values are to be acquired. At most, the following edges can be detected in each position control cycle:

- Two positive edges when detecting positive edges
- Two negative edges when detecting negative edges
- One positive edge and one negative edge when detecting positive and negative edges

###### Measured values and counters

With a positive edge at the input "MC_Measuring­Input­Cyclic.­Execute", outputs "MeasuredValue1Counter" and "MeasuredValue2Counter" are reset to "0". As a result, new events can be tracked immediately and new measured value entries can be detected.

All measuring event occurrences of the measuring job are incremented by "1" in the corresponding event counters "&lt;TO&gt;.MeasuredValues.MeasuredValue1Counter" and "&lt;TO&gt;.MeasuredValues.MeasuredValue2Counter" of the technology data block.

The acquired measured values are continuously captured in the technology data block irrespective of individual jobs and the values are only reset to "0" at power-up or restart of the technology object.

After a completed measurement, the measured values are output in the function block. The counters of the function block are set to "0" at a new measuring job. The measured value output in the technology data block always indicates the last acquired measured value.

###### Lost edge counter (LEC) for Timer DI

If more than two edges to be detected occur within one position control cycle, a measured value cannot be evaluated for the other edges to be detected. The number of lost edges is recorded in the LEC.

The lost edges that are recorded in the LEC depend on the mode set in the Motion Control instruction. For example, if only positive edges are to be measured, the LEC records only the non-measured positive edges.

A maximum of seven lost edges can be counted and displayed in the LEC.

The number of lost edges is indicated in the function block and in the technology data block in:

- "LostEdgeCounter1"

  Lost cleared edges from the position control cycle in which "MeasuredValue1" was acquired.

  ⇒ The displayed value in "LostEdgeCounter1" is updated when counter "MeasuredValueCounter1" is incremented.
- "LostEdgeCounter2"

  Lost cleared edges from the position control cycle in which "MeasuredValue2" was acquired.

  ⇒ The displayed value in "LostEdgeCounter2" is updated when counter "MeasuredValueCounter2" is incremented.

###### Lost Edge Counter for central measuring input

During cyclic measuring using the central probe, the LEC is always 0.

###### Display of measurement results when using cyclic measuring

| Edges selected in the command | Display per position control cycle |  |  |  |
| --- | --- | --- | --- | --- |
| "MeasuredValue1" | "MeasuredValue2" | "LostEdgeCounter1"<sup>1</sup> | "LostEdgeCounter2"<sup>1</sup> |  |
| Detect positive edges only  "MC_Measuring­Input­Cyclic.­Mode" = 0 | Actual position at the time of the first positive edge | Actual position at the time of the second positive edge | Number of positive or negative edges in excess of two in the position control cycle of acquisition of "MeasuredValue1" and "MeasuredValue2".  The following applies here:  - If a "MeasuredValue1" and a "MeasuredValue2" are acquired, the number of acquired and lost edges indicated in "LostEdgeCounter1" and "LostEdgeCounter2" are the same. - If only one "MeasuredValue1" is acquired, the "LostEdgeCounter1" is reset to "0". The value in "LostEdgeCounter2" remains changed. |  |
| Detect negative edges only  "MC_Measuring­Input­Cyclic.­Mode" = 1 | Actual position at the time of the first negative edge | Actual position at the time of the second negative edge |  |  |
| Detect positive and negative edges  "MC_Measuring­Input­Cyclic.­Mode" = 2 | Actual position at the time of the first positive edge in the position control cycle | Actual position at the time of the first negative edge in the position control cycle | Number of edges in excess of two in the position control cycle of acquisition of "MeasuredValue1" and "MeasuredValue2".  The following applies here:  - If a "MeasuredValue1" and a "MeasuredValue2" are acquired, the number of acquired and lost edges indicated in "LostEdgeCounter1" and "LostEdgeCounter2" are the same. - If only one "MeasuredValue1" is acquired, the "LostEdgeCounter1" is reset to "0". The value in "LostEdgeCounter2" remains changed. - If only one "MeasuredValue2" is acquired, the "LostEdgeCounter2" is reset to "0". The value in "LostEdgeCounter1" remains changed. |  |
| <sup>1)</sup> Applies only to cyclic measuring via Timer DI. |  |  |  |  |

###### Examples

The following figures show examples of divergence of "MeasuredValue1Counter" and "MeasuredValue2Counter" as a result of lost edges.

**Example: Measurement at positive edges (Mode = 0)**

![Examples](images/169055532427_DV_resource.Stream@PNG-en-US.png)

**Example: Measurement at negative edges (Mode = 1)**

![Examples](images/169056241547_DV_resource.Stream@PNG-en-US.png)

**Example: Measurement at positive and negative edges (Mode = 2)**

![Examples](images/169056246667_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[MC_MeasuringInputCyclic: Start cyclic measuring V8 (S7-1500, S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_measuringinputcyclic-start-cyclic-measuring-v8-s7-1500-s7-1500t)

#### Measuring with measuring range (S7-1500, S7-1500T)

A measuring job can be activated directly or restricted to a defined measuring range.

The following graphic shows an example of measuring with measuring range in "Mode" = 0 (measurement of next positive edge):

![Figure](images/169071744011_DV_resource.Stream@PNG-en-US.png)

Only measured values within the measuring range are displayed for the technology object.

- If no measuring edge within the measuring range is detected during a one-time measurement, the measuring job is canceled and an alarm is triggered.
- Cyclic measuring remains active even if no measuring edge within the measuring range was detected.

For axes without modulo function, it is immaterial in which order the start and end positions are specified. If the start position is greater than the end position, the two values are interchanged in the application. If the start position for an axis with modulo function is greater than the end position, the measuring range is extended from the start position past the modulo transition of the axis to the end position.

![Figure](images/169071749131_DV_resource.Stream@PNG-en-US.png)

The measuring range positions are specified in the Motion Control instruction "MC_MeasuringInput" or "MC_MeasuringInputCyclic".

##### Activation time for the measuring range

The measuring function must be active at the measurement input when the start of the measuring range is reached. To compensate for the communication time for activation in the Timer DI or drive, for example, the activation of the measurement in the technology object begins earlier then the measuring range start by the amount of the activation time.

The activation time for measuring with measuring range is divided up as follows:

- The activation time allocation defined and active on the system side is indicated in the "&lt;TO&gt;.Parameter.MeasuringRangeActivationTime" tag.
- An additional activation time can also be set by the user with the "&lt;TO&gt;.Parameter.MeasuringRangeAdditionalActivationTime" tag.

#### Use a measurement input for several axes (S7-1500, S7-1500T)

##### Description

The measurement event of a measurement input can be captured simultaneously by multiple measuring probes (referred to below as monitoring probes).

Therefore, the actual positions of multiple axes or external encoders can be captured using a measurement input. The measuring probes do not require assignment to a measurement input and therefore do not need additional wiring. Assign the monitoring probes to the measuring probe with the measurement input..

The following figure shows the interconnection of multiple measuring probes to a common measured signal:

![Description](images/170748054411_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Measuring an event on multiple axes/external encoders simultaneously is only possible when measuring via Timer DI or via SINAMICS (central probe) is configured for the measuring probe with the measurement input.

##### Programming

Start the jobs for one-time or cyclic measuring with the instructions "MC_MeasuringInput" and "MC_MeasuringInputCyclic" on the measuring probe with measurement input. The configured measuring range only applies for the measuring probe with measurement input.   
When the measuring job is completed, all monitoring probes automatically output the captured measured values of the actual positions (&lt;TO&gt;.Status" = "TRIGGER_OCCURRED).  
Measuring job at monitoring probes are rejected.

The measuring values of the monitoring probes are output in the technology object data block.(&lt;TO&gt;.MeasuredValues.MeasuredValue1 / &lt;TO&gt;.MeasuredValues.MeasuredValue2).

---

**See also**

[Configuration - Hardware interface (S7-1500, S7-1500T)](#configuration---hardware-interface-s7-1500-s7-1500t)

#### Time-related boundary conditions (S7-1500, S7-1500T)

Depending on the hardware configuration and selection of edges to be detected, different system-inherent requirements apply to the time allowed after calling the Motion Control instruction "MC_MeasuringInput" or "MC_MeasuringInputCyclic" until a measurement occurs and the results are displayed.

The following times must be distinguished here:

- Time until the measuring event can be captured
- Time until the measurement result is displayed or the measurement is finished.

The times calculated taking into account the current settings are indicated in configuration window "Extended parameters" of a measuring input.

##### Measurement using Timer DI

| Description | Measuring once | Cyclic measuring |
| --- | --- | --- |
| Time from output of a measuring job until measuring event detection becomes effective ("MeasuringRangeActivationTime") | 2 × T<sub>servo</sub> |  |
| Activation time for a measurement with measuring range | "MeasuringRangeActivationTime" + "Measuring­Range­Additional­Activation­Time" |  |
| Minimum time after measuring event until measured value is available in the controller | 2 × T<sub>servo</sub> + T<sub>Send</sub> | T<sub>servo</sub> + T<sub>Send</sub> |
| Minimum time between two measuring events | 4 × T<sub>servo</sub> + T<sub>Send</sub> | T<sub>servo</sub> |

##### Measuring via SINAMICS (central probe)

| Description | Measuring once | Cyclic measuring |
| --- | --- | --- |
| Time from output of a measuring job until measuring event detection becomes effective ("MeasuringRangeActivationTime") | 2 × T<sub>servo</sub> |  |
| Activation time for a measurement with measuring range | "MeasuringRangeActivationTime" + "Measuring­Range­Additional­Activation­Time" |  |
| Minimum time after measuring event until measured value is available in the controller | 2 × T<sub>servo</sub> | T<sub>servo</sub> + T<sub>Send</sub> |
| Minimum time between two measuring events | 4 × T<sub>servo</sub> | 3 × T<sub>servo</sub> |

##### Measurement using PROFIdrive telegram (drive or external encoder)

- Time from output of a measuring job until measuring event detection becomes effective ("MeasuringRangeActivationTime"):

  - T<sub>Send</sub> and T<sub>servo</sub> equal to: 3 × T<sub>servo</sub>
  - T<sub>Send</sub> and T<sub>servo</sub> not equal to: 2 × T<sub>servo</sub>
- Activation time for a measurement with measuring range:

  - Measuring a positive/negative edge or two edges:

    "MeasuringRangeActivationTime" + "MeasuringRangeAdditionalActivationTime" + 2 × T<sub>servo</sub>
  - Measuring two dedicated edges:

    "MeasuringRangeActivationTime" + "MeasuringRangeAdditionalActivationTime" + 3 × T<sub>servo</sub>
- Time from output of an "MC_MeasuringInput" job until measuring event detection becomes effective:

  - Measuring a positive/negative edge or two edges:

    "MeasuringRangeActivationTime" + 2 × T<sub>servo</sub>
  - Measuring two dedicated edges:

    "MeasuringRangeActivationTime" + 3 × T<sub>servo</sub>
- Time after measuring event until measured value is available in the controller:

  - Measuring an edge: 7 × <sub>servo</sub>
  - Measuring two edges: 13 × T<sub>servo</sub>

##### Definition of tags

- T<sub>servo</sub> = Call interval of the technology object in the servo cycle clock [ms]
- T<sub>Send</sub> = Send clock [ms]
- "MeasuringRangeActivationTime" = See section "[Measuring with measuring range](#measuring-with-measuring-range-s7-1500-s7-1500t)"

> **Note**
>
> **Maximum bus clock cycle**
>
> With the use of SINAMICS measuring inputs, the maximum bus clock cycle T<sub>Send</sub> can be up to 8 ms.

To prevent asynchronous processing from overwriting a measured value that was just determined, a new one-time measuring job cannot be started until the active measurement has concluded. The sum of the activation time and the time until display or conclusion must be taken into account for this.

In the case of cyclic measuring, evaluation or temporary storage of the measurement results in the synchronous MC_PreInterpolator is recommended from the user perspective.

#### Tags: Measuring input technology object (S7-1500, S7-1500T)

The following technology object tags are relevant for measuring:

| Status indicator |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.Status | Status of the measuring input function |  |
| 0 | Measurement is not active ("INACTIVE") |  |
| 1 | The measuring input is waiting for a measuring event ("WAITING_FOR_TRIGGER") |  |
| 2 | The measuring input has acquired one or more measured values ("TRIGGER_OCCURRED"). |  |
| 3 | Error during the measurement ("MEASURING_ERROR") |  |
| &lt;TO&gt;.InputState | Status of the measurement input |  |

| Parameters |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.Parameter.Measuring­Input­Type | Measuring input type |
| &lt;TO&gt;.Parameter.PROFIdriveProbeNumber | Number of the measuring input to be used for a measurement via PROFIdrive telegram |
| &lt;TO&gt;.Parameter.Measuring­Range­Activation­Time | System-defined activation time allocation [ms] |
| &lt;TO&gt;.Parameter.Measuring­Range­Additional­Activation­Time | Additional user-defined activation time allocation [ms] |
| &lt;TO&gt;.Parameter.Correction­Time | User-defined correction time for the measurement result [ms] |

| Interface |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.Interface.Address | I/O address for the digital measuring input |

| Units |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.Units.LengthUnit | Unit of the length data |
| &lt;TO&gt;.Units.TimeUnit | Unit of the time data |

| MeasuredValues |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.MeasuredValues.Measured­Value1 | First measured value |
| &lt;TO&gt;.MeasuredValues.Measured­Value2 | Second measured value (when measuring two or more edges in one position control cycle) |
| &lt;TO&gt;.MeasuredValues.Measured­Value1­Counter | Count value for the first measured value |
| &lt;TO&gt;.MeasuredValues.Measured­Value2­Counter | Count value for the second measured value |
| &lt;TO&gt;.MeasuredValues.Lost­Edge­Counter1 | Lost edges in the cycle clock of the first measured value acquisition  Zero in the case of one-time measurement  During cyclic measurement via SINAMICS equal to zero |
| &lt;TO&gt;.MeasuredValues.Lost­Edge­Counter2 | Lost edges in the cycle clock of the second measured value acquisition  Zero in the case of one-time measurement  During cyclic measurement via SINAMICS equal to zero |

| StatusWord |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.StatusWord.X0 (Control) | The technology object is in operation. |
| &lt;TO&gt;.StatusWord.X1 (Error) | An error occurred at the technology object. |
| &lt;TO&gt;.StatusWord.X2 (RestartActive) | The technology object will be reinitialized. The tags of the technology data block are not updated with active restart. |
| &lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged) | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object. |
| &lt;TO&gt;.StatusWord.X5 (CommunicationOk) | The measuring input is synchronized with the measurement input and can be used.  With the monitoring probe, this bit always has the value "FALSE". |

| ErrorWord |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.ErrorWord.X0 (SystemFault) | A system-internal error has occurred. |
| &lt;TO&gt;.ErrorWord.X1 (ConfigFault) | Configuration error  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program. |
| &lt;TO&gt;.ErrorWord.X2 (UserFault) | Error in user program at a Motion Control instruction or its use |
| &lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted) | Command cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |
| &lt;TO&gt;.ErrorWord.X13 (PeripheralError) | Error accessing a logical address |

| ErrorDetail |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.ErrorDetail.Number | Alarm number  You can find a list of the technology alarms and alarm responses in the "[Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation. |  |
| &lt;TO&gt;.ErrorDetail.Reaction | Effective alarm response |  |
| 0 | No reaction |  |
| 6 | End measuring input processing |  |

### Output cam technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of the output cam technology object (S7-1500, S7-1500T)](#short-description-of-the-output-cam-technology-object-s7-1500-s7-1500t)
- [Distance output cam (S7-1500, S7-1500T)](#distance-output-cam-s7-1500-s7-1500t)
- [Time-based output cam (S7-1500, S7-1500T)](#time-based-output-cam-s7-1500-s7-1500t)
- [Activation direction of output cams (S7-1500, S7-1500T)](#activation-direction-of-output-cams-s7-1500-s7-1500t)
- [Hysteresis (S7-1500, S7-1500T)](#hysteresis-s7-1500-s7-1500t)
- [Compensation of actuator switching times (S7-1500, S7-1500T)](#compensation-of-actuator-switching-times-s7-1500-s7-1500t)
- [Tags: Output cam technology object (S7-1500, S7-1500T)](#tags-output-cam-technology-object-s7-1500-s7-1500t)

#### Short description of the output cam technology object (S7-1500, S7-1500T)

![Figure](images/169102262923_DV_resource.Stream@PNG-de-DE.png)

The output cam technology object generates switching signals depending on the position of an axis or external encoder. The switching states can be evaluated in the user program and fed to digital outputs.

You can find an overview of the functions of the output cam technology object in the "[Functions](#functions-s7-1500-s7-1500t)" section.

The following figure shows the basic operating principle of the output cam technology object:

![Figure](images/169102267147_DV_resource.Stream@PNG-en-US.png)

##### Output cam types

The following output cam types can be used:

- [Distance output cam](#distance-output-cam-s7-1500-s7-1500t)

  Distance output cams switch on between the start position and end position. Outside this range, the distance output cam is switched off.
- [Time-based output cam](#time-based-output-cam-s7-1500-s7-1500t)

  Time-based output cams switch on for a defined time period when the start position is reached.

##### Assignment

The output cam technology object must always be assigned to another technology object whose position will be evaluated.

The output cam technology object can be assigned to the following technology objects:

- Synchronous axis
- Positioning axis
- External encoder

![Assignment](images/169102257803_DV_resource.Stream@PNG-en-US.png)

Exactly one axis or one external encoder can be assigned to an output cam.

Multiple output cams can be assigned to one axis or external encoder.

##### Output cam calculation and output cam output

The output cam technology object calculates the exact switching time, thereby ensuring exact adherence to the switching positions. The switching time is calculated two position control cycles before the output.

The following output options are available for the digital output cam output:

- Timer DQ

  Digital output with high degree of accuracy and reproducibility in the microsecond range on time-based IO modules basis. In the case of signal output via time value, the times of the signal changes are determined by the technology object. The time stamps are then transferred to the hardware of the digital output and the edges are output with high precision.

  Output via Timer DQ requires isochronous mode.
- Digital output module

  Digital output with switching accuracy depending on the output cycle of the I/O used

When output is deactivated, the output cam status is not output at the hardware output. The output cam status can be used internally in the user program by evaluating the relevant "&lt;TO&gt;.CamOutput" tag.

**Inverted output**

In the case of inverted output, the range in which the output cam output is switched on and the range in which it is switched off are swapped.

The inverted output is set in Motion Control instruction "MC_OutputCam" and is active when the instruction is enabled.

The inverted output can be used for both distance output cams and time-based output cams.

**Output of multiple output cams to one output**

The output of multiple output cams to one output is performed with either an AND or OR logic operation of the output cam signals to the output.

![Output cam calculation and output cam output](images/169102412939_DV_resource.Stream@PNG-en-US.png)

**Display of the switching state**

The switching state of the output cam is displayed in the associated technology data block in "&lt;TO&gt;.CamOutput".

##### Position reference

The switching points of the output cams can be referenced to the following positions, depending on the interconnected technology object.

- Actual position of a synchronous axis/positioning axis
- Position setpoint of a synchronous axis/positioning axis
- Position of an external encoder

**Homing the interconnected technology object**

A change to the position of an axis or external encoder using Motion Control instruction "MC_Home" is regarded as a sudden position change.

- Distance output cams are either skipped or correspondingly output.
- Time-based output cams are skipped. A time-based output cam is switched on only when the start position is overtraveled and remains switched on for the switch-on duration.
- Switched time-based output cams are not canceled by a homing operation.

**Trace recording of output cam with reference to setpoint position**

The CPU calculates the output time of the output cam in such a way that the output cam is switched when the position setpoint has been transferred from the PLC to the drive.

The communication time is not considered in the trace.

#### Distance output cam (S7-1500, S7-1500T)

##### Switch-on range

The switch-on range of distance output cams is basically defined by the start position and end position.

**Start position smaller than end position**

When the start position is less than the end position, the switch-on range begins with the start position and ends with the end position.

![Switch-on range](images/169102418059_DV_resource.Stream@PNG-en-US.png)

**Start position greater than end position**

When the start position is greater than the end position, there are two switch-on ranges as follows:

- Switch-on range beginning with the start position and ending with the positive range end (e.g. positive software limit switch, end of modulo range)
- Switch-on range beginning with the negative range end (e.g. negative software limit switch, start of modulo range) and ending with the end position

![Switch-on range](images/169102423179_DV_resource.Stream@PNG-en-US.png)

##### Mapping to an axis with modulo function

With active modulo function of the interconnected technology object, the start and end positions of the output cam are automatically mapped to values within the modulo range.

**Example**

- Modulo range = 0° to 50°
- Output cam start position = 80°
- Output cam end position = 220°

⇒ The specified start and end position of the output cam are outside the modulo range. The values are therefore mapped onto the modulo range. The start position is at 30° (80° mod 50° = 30°) and the end position is at 20° (220° mod 50° = 20°). The output cam remains switched on over two consecutive modulo lengths and switches off at 20° in every second modulo length.

![Mapping to an axis with modulo function](images/169102595851_DV_resource.Stream@PNG-en-US.png)

##### Switching characteristics

After activation, a distance output cam switches on in the following cases:

- The position of the interconnected technology object reaches the start or end position in the activation direction configured in Motion Control instruction "MC_OutputCam".
- The position of the interconnected technology object is moved into the switch-on range of the output cam (e.g. during homing) in the activation direction configured in Motion Control instruction "MC_OutputCam". If both activation directions are enabled in Motion Control instruction "MC_OutputCam", the output cam switches on even when the interconnected technology object is at a standstill.
- The output cam is switched on permanently using Motion Control instruction "MC_OutputCam" with "Mode" = 3.

An active distance output cam switches off in the following cases:

- The position is outside the switch-on range of the output cam.
- The position value is moved outside the switch-on range of the output cam.
- Motion Control instruction "MC_OutputCam" is set to "Enable" = FALSE.
- The motion direction of the interconnected technology object is reversed and no longer agrees with the enabled activation direction.

#### Time-based output cam (S7-1500, S7-1500T)

A time-based output cam switches on at the start position and remains set for the on-load factor.

![Figure](images/169102600971_DV_resource.Stream@PNG-en-US.png)

**Mapping to an axis with modulo function**

In the case of active modulo function of the interconnected technology object, the start position of the output cam is automatically mapped to the value within the modulo range.

**Example**

- Modulo range = 0° to 50°
- Output cam start positions:

  - Output cam 1 = 20°
  - Output cam 2 = 30°
  - Output cam 3 = 80°

⇒ The time-based output cam 1 switches on at 20°, the time-based output cam 2 switches on at 30°. The specified start position of time-based output cam 3 is outside the modulo range. The value for the start position is therefore mapped onto the modulo range so that the time-based output cam 3 switches on at 30°. All three output cams remain active the set on-load factor in each case.

![Figure](images/169102721291_DV_resource.Stream@PNG-en-US.png)

##### Switching characteristics

A time-based output cam switches on in the following cases:

- The start position has been reached and the motion direction of the interconnected technology object corresponds to the effective direction enabled by the instruction.

  > **Note**
  >
  > - If the start position is reached again while an output cam is switched on, the on-load factor is not re-triggered.
  > - If due to the Motion Control instruction "MC_Home", the position value of the interconnected technology object is placed directly on or behind the start position of the output cam during the motion, the output cam does not switch on.

A time-based output cam switches off in the following cases:

- The configured on-load factor has expired.
- Motion Control instruction "MC_OutputCam" is set to "Enable" = FALSE.

#### Activation direction of output cams (S7-1500, S7-1500T)

An output cam can be switched depending on the motion direction of the interconnected technology object. An output of the output cam in positive or negative motion direction or independent of direction is possible.

The effective direction is set in "MC_OutputCam.Direction".

The following examples show the behavior of the output cam as a function of the effective direction setting.

##### Example of "positive" effective direction ("Direction" = 1)

![Example of "positive" effective direction ("Direction" = 1)](images/169102757131_DV_resource.Stream@PNG-en-US.png)

**Distance output cam**

The output cam switches on when the switch-on range is reached in the **positive** direction. At a direction reversal ②, the output cam switches off.

If the position value is moved into the switch-on range of the output cam, the output cam switches on when there is positive motion direction of the interconnected technology object. The output cam remains switched off when the interconnected technology object is at a standstill.

**Time-based output cam**

The output cam switches on when the start position is reached in the **positive** direction. At a direction reversal, the output cam remains switched on for the specified on-load factor ①.

If during the homing motion, the position value of the interconnected technology object is directly on or behind the start position of the output cam, the output cam does not switch on.

##### Example of "negative" effective direction ("Direction" = 2)

![Example of "negative" effective direction ("Direction" = 2)](images/169102726411_DV_resource.Stream@PNG-en-US.png)

**Distance output cam**

The output cam switches on when the switch-on range is reached in the **negative** direction. At a direction reversal ②, the output cam switches off.

If the position value is moved into the switch-on range of the output cam, the output cam switches on when there is negative motion direction of the interconnected technology object. The output cam remains switched off when the interconnected technology object is at a standstill.

**Time-based output cam**

The output cam switches on when the start position is reached in the **negative** direction. At a direction reversal, the output cam remains switched on for the specified on-load factor ①.

If during the homing motion, the position value of the interconnected technology object is directly on or behind the start position of the output cam, the output cam does not switch on.

##### Example of "both directions" effective direction ("Direction" = 3)

![Example of "both directions" effective direction ("Direction" = 3)](images/169102762251_DV_resource.Stream@PNG-en-US.png)

**Distance output cam**

The output cam switches on when the position of the interconnected technology object is within the switch-on range.

If the position value of the interconnected technology object is moved into the switch-on range of the output cam, the output cam switches on even when the interconnected technology object is at a standstill.

**Time-based output cam**

The output cam switches on when the start position is reached. At a direction reversal, the output cam remains switched on for the specified on-load factor ①.

If during the homing motion, the position value of the interconnected technology object is directly on or behind the start position of the output cam, the output cam does not switch on.

#### Hysteresis (S7-1500, S7-1500T)

Possible variations in the actual position/position setpoint can result in unwanted switch-on and switch-off of output cams.

Minimal changes of the actual value of an axis in standstill can result in the switching on or off of an actual value output cam with preset positive or negative effective direction. Even minimal changes of the setpoints of a switched-off axis in follow-up mode can result in switch-on or switch-off of an actual value output cam with specified positive or negative effective direction. Such unwanted switching states can be prevented by configuring a hysteresis (&gt; 0.0). The configuration of a hysteresis value (&gt; 0.0) is recommended in particular with reference to the actual position.

The hysteresis is a position tolerance within which the position values may vary without changing the switching state of the output cam. Changes of direction detected within the hysteresis are ignored.

The hysteresis is set for the technology object in "&lt;TO&gt;.Parameter.Hysteresis".

##### Behavior

- The hysteresis is activated at a direction reversal.
- The following applies within the hysteresis:

  - The switching state of distance output cams is not changed.
  - The motion direction is not determined again.
  - If the start position of a time-based output cam is within the hysteresis, the time-based output cam is switched on when leaving the hysteresis with the corresponding effective direction.
  - The on-load factor of time-based output cams remains unchanged.
- After the hysteresis range is exited, distance output cams are set according to the output cam settings.

![Behavior](images/169102823691_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Actual position |
| ② | Effective position |
| ③ | Hysteresis range |

The following examples show the effects of the hysteresis on the switching behavior of output cams with positive activation direction.

![Behavior](images/169102767371_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Direction reversal without hysteresis effect |
| ② | Hysteresis in effect |
| ③ | The switch-on position of the distance output cam is influenced according to the direction reversal and hysteresis. |
| ④ | The start position of the time-based output cam is located within the hysteresis. The time-based output cam is switched on when leaving the hysteresis with the corresponding effective direction. |
| ⑤ | Switch-on duration |

##### Hysteresis range

The maximum size of the hysteresis range in the system is as follows: for an axis with modulo function, one quarter of the modulo range; for an axis without modulo function, one quarter of the operating range.

#### Compensation of actuator switching times (S7-1500, S7-1500T)

You can compensate for communication times, switching times of the output and the connected actuator using the activation time or deactivation time of the output cam technology object.

The activation time is specified as the lead time for the switch-on edge, and the deactivation time as the lead time for the switch-off edge.

For the timers, the following must apply:

Switch on duration &gt; deactivation time - activation time

The activation time is set in the technology object via the "&lt;TO&gt;.Parameter.OnCompensation" tag, the deactivation time via "&lt;TO&gt;.Parameter.OffCompensation".

If the output cam has been switched with consideration of the derivative-action times and the current velocity changes afterwards, the output cam will not be switched again.

**Influence of the digital outputs used**

- When the output cam is output via timer DQ, the communication times are automatically taken into account.

  When the output cam is output via digital output, the communication times are not automatically taken into account.

**Time-based output cam**

For time-based output cams, you indicate the switch-on duration at the "Duration" parameter of the "MC_OutputCam" instruction.

![Figure](images/169102828811_DV_resource.Stream@PNG-en-US.png)

The derivative-action time dynamically shifts the switch-on and switch-off times of the time-based output cam depending on the velocity of the axis.

**Example**

An actuator (e.g. valve) should open at position 200° and the derivative-action time is 0.5s.

- With a velocity of 10°/s, the switch-on time is already at 195°.
- With a velocity of 20°/s, the switch-on time is already at 190°.

The switch-off time shifts accordingly.

**Distance output cam**

The switch-on duration for distance output cams is determined by the switching positions and the current velocity.

#### Tags: Output cam technology object (S7-1500, S7-1500T)

The following technology object tags are relevant:

| Status indicator |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.CamOutput | The output cam is switched. |

| Parameters |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.Parameter.OutputCamType | Output cam type |  |
| 0 | Distance output cam |  |
| 1 | Time-based output cam |  |
| &lt;TO&gt;.Parameter.PositionType | Position reference |  |
| 0 | Position setpoint |  |
| 1 | Actual position |  |
| &lt;TO&gt;.ParameterOnCompensation | Activation time (lead time for the switch-on edge) |  |
| &lt;TO&gt;.Parameter.OffCompensation | Deactivation time (lead time for the switch-off edge) |  |
| &lt;TO&gt;.Parameter.Hysteresis | Hysteresis value |  |

| Interface |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.Interface.EnableOutput | Activation of the output cam output |  |
| FALSE | No output |  |
| TRUE | Output |  |
| &lt;TO&gt;.Interface.Address | I/O address of the output cam |  |
| &lt;TO&gt;.Interface.LogicOperation | Logical operation of the output cam signals at the output |  |
| 0 | OR logic operation |  |
| 1 | AND logic operation |  |

| Units |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.Units.LengthUnit | Unit of the length data |
| &lt;TO&gt;.Units.TimeUnit | Unit of the time data |

| StatusWord |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.StatusWord.X0 (Control) | The technology object is in operation. |
| &lt;TO&gt;.StatusWord.X1 (Error) | An error occurred at the technology object. |
| &lt;TO&gt;.StatusWord.X2 (RestartActive) | The technology object is being reinitialized. The tags of the technology data block are not updated with active restart. |
| &lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged) | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object. |
| &lt;TO&gt;.StatusWord.X4 (OutputInverted) | The output cam output is inverted. |
| &lt;TO&gt;.StatusWord.X5 (CommunicationOk) | The output cam is synchronized with the output module and available for use. |

| ErrorWord |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.ErrorWord.X0 (SystemFault) | A system-internal error has occurred. |
| &lt;TO&gt;.ErrorWord.X1 (ConfigFault) | Configuration error  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program. |
| &lt;TO&gt;.ErrorWord.X2 (UserFault) | Error in user program at a Motion Control instruction or its use |
| &lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted) | Command cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |
| &lt;TO&gt;.ErrorWord.X13 (PeripheralError) | Error accessing a logical address |

| ErrorDetail |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.ErrorDetail.Number | Alarm number  You can find a list of the technology alarms and alarm responses in the "[Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation. |  |
| &lt;TO&gt;.ErrorDetail.Reaction | Effective alarm response |  |
| 0 | No reaction |  |
| 6 | Output cam processing is complete. |  |

### Cam track technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of the cam track technology object (S7-1500, S7-1500T)](#short-description-of-the-cam-track-technology-object-s7-1500-s7-1500t)
- [Modulo function (S7-1500, S7-1500T)](#modulo-function-s7-1500-s7-1500t)
- [Effective direction (S7-1500, S7-1500T)](#effective-direction-s7-1500-s7-1500t)
- [Changing the cam track data during operation (S7-1500, S7-1500T)](#changing-the-cam-track-data-during-operation-s7-1500-s7-1500t)
- [Activation behavior (S7-1500, S7-1500T)](#activation-behavior-s7-1500-s7-1500t)
- [Hysteresis (S7-1500, S7-1500T)](#hysteresis-s7-1500-s7-1500t-1)
- [Time offset of output cam switching points (S7-1500, S7-1500T)](#time-offset-of-output-cam-switching-points-s7-1500-s7-1500t)
- [Tags: Cam track technology object (S7-1500, S7-1500T)](#tags-cam-track-technology-object-s7-1500-s7-1500t)

#### Short description of the cam track technology object (S7-1500, S7-1500T)

![Figure](images/169108619147_DV_resource.Stream@PNG-de-DE.png)

The cam track technology object generates a switching signal sequence dependent on the position of an axis or external encoder. A cam track can consist of up to 32 individual output cams and be output to one output. The switching states can be evaluated in the user program or fed to digital outputs.

You can find an overview of the functions of the cam track technology object in the "[Functions](#functions-s7-1500-s7-1500t)" section.

The following figure shows the basic principle of operation of the cam track technology object:

![Figure](images/169108623371_DV_resource.Stream@PNG-en-US.png)

##### Definition of cam track

A cam track consists of up to 32 individual output cams that are specified within an adjustable track length.

![Definition of cam track](images/169108404107_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Start position |
| ② | End position |
| ③ | Cam track length |

The output cam positions are defined relative to the cam track. The start of the cam track is always 0.0. The output cam positions on the cam track are thus always positive.

When the cam track is processed, the output cams with start position within the track length are taken into consideration.

The output cams of the cam track can be set as distance output cams or time-based output cams, whereby only one of the two output cam types can be used in a cam track.

If the end of a cam track is crossed, connected output cams behave as follows within the cam track:

- Time-based output cams remain switched on for the set on-load factor.
- Distance output cams whose end position lies outside the cam track are switched off when the cam track is left.

Output cams whose start and end positions lie outside the cam track length are ignored. They become active only if the cam track length is increased so that at least the respective start position of an output cam is within the new track length.

##### Assignment

The cam track technology object must always be assigned to another technology object whose position is evaluated.

The cam track technology object can be assigned to the following technology objects:

- Synchronous axis
- Positioning axis
- External encoder

![Assignment](images/169108628363_DV_resource.Stream@PNG-en-US.png)

Exactly one axis or one external encoder can be assigned to a cam track.

Multiple cam tracks can be assigned to one axis or external encoder.

##### Position reference

The switching points of the output cams of a cam track can be referenced to the following positions, depending on the interconnected technology object.

- Actual position of a synchronous axis/positioning axis
- Position setpoint of a synchronous axis/positioning axis
- Position of an external encoder

##### Mapping of the cam track to the position of the technology object

The start of the cam track is placed at the specified reference position of the interconnected technology object. Thus, the switching positions result from the cam track positions mapped onto the interconnected technology object starting from the reference position. The cam track is continued in both directions of the interconnected technology object.

The setting for the reference position can be either positive or negative.

**Example**

- Axis range = -1000 mm to +1000 mm
- Desired switching points of the output cam with reference to axis position:

  - Start position = -200 mm
  - End position = -100 mm
- Cam track length = 2000 mm
- Definition of output cam on the track:

  - Start position = 800 mm
  - End position = 900 mm

![Mapping of the cam track to the position of the technology object](images/170231501579_DV_resource.Stream@PNG-en-US.png)

##### Processing of a cam track

The processing of a cam track occurs cyclically.

![Processing of a cam track](images/169108710283_DV_resource.Stream@PNG-en-US.png)

The cam track is mapped onto the position of the interconnected technology object starting from the reference position and is continued cyclically in both directions.

##### Output of a cam track

The following output options are available for the digital cam track output:

- Timer DQ

  Digital output with high degree of accuracy and reproducibility in the microsecond range on time-based IO modules basis. In the case of signal output via time value, the times of the signal changes are determined by the technology object. The time stamps are then transferred to the hardware of the digital output and the edges are output with high precision.

  Output via Timer DQ requires isochronous mode.
- Digital output module

  Digital output with switching accuracy depending on the output cycle of the I/O used

A maximum of two edges (via Timer DQ, positive and negative) or one edge (via digital output module, positive or negative) can be output per position control cycle. If multiple switch-on edges or switch-off edges are transmitted in one position control cycle clock, the last written values in each case are valid.

**Masking of individual output cams of a cam track**

In order for output cams to be processed, they must be configured as valid in the technology data block with "&lt;TO&gt;.Parameter.Cam[1..32].Existent" = TRUE. In addition, output cams of a cam track configured as valid can be defined as valid in the user program using bit masking ("&lt;TO&gt;.Parameter.CamMasking"). In the default setting, all valid output cams are enabled ("&lt;TO&gt;.Parameter.CamMasking" = 0xFFFFFFFF). The cam track itself is activated/deactivated using the Motion Control instruction "MC_CamTrack".

#### Modulo function (S7-1500, S7-1500T)

##### Track length and mapping to an axis or encoder with modulo function

When a cam track is mapped onto an axis with modulo function, a reference position specified outside the modulo range is mapped within the modulo range.

The track length can be less than or greater than the modulo length of the axis. In order for the cam track to be mapped without offset in the modulo range and to prevent unwanted overrides, an integer ratio of modulo length to track length, and vice versa, is required.

|  |  |  |  |
| --- | --- | --- | --- |
| **Example** Mapping without offset |  | **Example** Mapping with offset |  |
| ![Track length and mapping to an axis or encoder with modulo function](images/169108715403_DV_resource.Stream@PNG-de-DE.png) |  | ![Track length and mapping to an axis or encoder with modulo function](images/169108719627_DV_resource.Stream@PNG-de-DE.png) |  |
| ① | Axis with modulo length 360° | ① | Axis with modulo length 360° |
| ② | Cam track with track length 120° | ② | Cam track with track length 160° |
| ⇒ | Ratio = 360° / 120° = **3**  The cam track is output 3 times on a modulo length. | ⇒ | Ratio = 360° / 160° = **2.25**  The cam track is output 2.25 times on the first modulo length and continued correspondingly in the other modulo lengths. |

During cyclic processing of the cam track, the continued reference position of the current cam track is displayed in the "&lt;TO&gt;.MatchPosition" tag. The continued reference position is independent of direction and always the position of the left boundary of the cam track. The unique detection and output of the position is only possible when the assigned technology object is in motion. The distance to the current reference position of the current cam track (&lt;TO&gt;.MatchPosition) is displayed in the "&lt;TO&gt;.TrackPosition" tag.

When the cam track is enabled by a "MC_CamTrack" job, the position of the cam track (&lt;TO_CamTrack&gt;.MatchPosition) is set as if the current position had been reached by a motion in the positive direction starting from the reference position (&lt;TO_CamTrack&gt;.ReferencePosition).

##### Homing of an axis or an encoder without modulo function

A change to the position of an axis or external encoder using Motion Control instruction "MC_Home" is regarded as a sudden position change. An enabled cam track is referenced to the changed position and processed further from there.

- Homing also has an effect on the current position of the cam track (&lt;TO&gt;.TrackPosition). The position is formed again as quickly as possible due to the offset.
- Distance output cams are either skipped or correspondingly output.
- Time-based output cams are skipped. A time-based output cam is switched on only when the start position is overtraveled and remains switched on for the switch-on duration.
- Switched time-based output cams are not canceled by a homing operation.

Recommendation:

Disable the cam track before or during homing.

##### Homing of an axis or an encoder with modulo function

- Homing also has an effect on the current position of the cam track (&lt;TO&gt;.TrackPosition).

  The homing of the assigned technology object influences the position of the subsequently active cam track on a direction-dependent basis. This is dependent on the position difference, the difference between the new position minus the original position. If the position difference is negative, you add the modulo length (&lt;TO_Axis/TO_ExternalEncoder&gt;.Modulo.Length).

  If this position difference is less than or equal to half the modulo length, the new position of the cam track (&lt;TO_CamTrack&gt;.MatchPosition) is set as if the new position had been reached by a motion in the positive direction starting from the original position.

  If this position difference is greater than half the modulo length, the new position of the cam track (&lt;TO_CamTrack&gt;.MatchPosition) is set as if the new position had been reached by a motion in the negative direction starting from the original position.
- Distance output cams are either skipped or correspondingly output.
- Time-based output cams are skipped. A time-based output cam is switched on only when the start position is overtraveled and remains switched on for the switch-on duration.
- Switched time-based output cams are not canceled by a homing operation.

Recommendation:

Disable the cam track before or during homing.

#### Effective direction (S7-1500, S7-1500T)

The cam track is always active for both directions of the position of the interconnected technology object.

##### Output of a cam track with distance output cams

Distance output cams are switched when the switch-on range is overtraveled.

The following graphic shows the execution of a cam track with distance output cam depending on the motion direction of the axis.

![Output of a cam track with distance output cams](images/169108839051_DV_resource.Stream@PNG-en-US.png)

With positive motion direction, the output cams of the cam track are output in the order Output Cam N1, Output Cam N2, Output Cam N3. In the case of negative motion direction, the output cams of the cam track are output in the order Output Cam N3, Output Cam N2, Output Cam N1. The distance output cams switch on at ① and switch off at ②.

##### Output of a cam track with time-based output cams

The time-based output cams are switched when the start position is crossed.

The following graphic shows the execution of a cam track with time-based output cam depending on the motion direction of the axis.

![Output of a cam track with time-based output cams](images/169108844171_DV_resource.Stream@PNG-en-US.png)

With positive motion direction, the output cams of the cam track are output in the order Output Cam N1, Output Cam N2, Output Cam N3. In the case of negative motion direction, the output cams of the cam track are output in the order Output Cam N3, Output Cam N2, Output Cam N1. The time-based output cams switch on at ① and remain switched on for the set switch-on duration ②.

#### Changing the cam track data during operation (S7-1500, S7-1500T)

The data of a cam track and the parameters of the associated Motion Control instruction "MC_CamTrack" can be changed while track processing is enabled. The active Motion Control instruction "MC_CamTrack" is not aborted. The modified parameters, however, only take effect at the next call of the Motion Control instruction "MC_CamTrack".

The following parameters can be changed during operation and are in effect after another call of Motion Control instruction "MC_CamTrack".

- Cam track data in technology data block

  - Reference position (&lt;TO&gt;.Parameter.ReferencePosition)
  - Track length (&lt;TO&gt;.Parameter.CamTrackLength)
  - Bit masking of individual output cams (&lt;TO&gt;.Parameter.CamMasking)
  - Activation time (&lt;TO&gt;.Parameter.OnCompensation)
  - Deactivation time (&lt;TO&gt;.Parameter.OffCompensation)
  - Hysteresis value (&lt;TO&gt;.Parameter.Hysteresis)
  - Output cam data (&lt;TO&gt;.Parameter.Cam[1..32])
- Parameters in the function block

  - Enable (MC_CamTrack.Enable)
  - Mode (MC_CamTrack.Mode)
  - Inverted output (MC_CamTrack.InvertOutput)

Note the different [activation behavior](#activation-behavior-s7-1500-s7-1500t) when changing the cam track data.

#### Activation behavior (S7-1500, S7-1500T)

A cam track is activated by the call of Motion Control instruction "MC_CamTrack" with "Enable" = TRUE. A distinction must be made here between:

- First-time activation of the cam track
- Call after a change of the cam track data during active cam track processing

The difference relates to how the cam track data is applied. Depending on the set mode ("MC_CamTrack.Mode"), the configuration (cam track data, data in the function block) is applied at different times.

- **First-time switch-on of a cam track**

  Calling the Motion Control instruction "MC_CamTrack" with "Enable" = TRUE activates the cam track immediately ("&lt;TO&gt;.Status" changes to 1) and configured cam track data takes effect immediately. This behavior is the same when "MC_CamTrack.Mode" = 0 and "MC_CamTrack.Mode" = 1.
- **Change of cam track data of an already activated cam track** ("&lt;TO&gt;.Status" = 1)

  - With the call of Motion Control instruction "MC_CamTrack" with "Enable" = TRUE and "Mode" = 0, the modified cam track data takes effect immediately.

    Previously activated distance output cams are aborted if their track signals are not still set due to the changed cam track data. Previously activated time-based output cams are always aborted.
  - With the call of Motion Control instruction "MC_CamTrack" with "Enable" = TRUE and "Mode" = 1, the cam track continues to be output with the prior configuration up to the cam track end. Modified cam track data takes effect at the end of the current track cycle.

    If you change a cam track with "MC_CamTrack.Mode" = 1 during runtime of the user program, keep in mind the lead time of the cam track as reserve for the first output cam. Define the first output cam position in the cam track only after the following position:

    Position of first output cam &gt; velocity of axis x lead time of the cam track (&lt;TO&gt;.Parameter.OnCompensation)

    Also keep in mind the internal system time for output cam calculation, even if you set the lead time 0.0.

**Changing cam track data when modulo length is not a multiple of the track length**

For the switching times to be set correctly, we recommend the following procedure for changes:

- Enter changes as soon as possible after start of a new cam track
- Enter a new reference position (&lt;TO&gt;.Parameter.ReferencePosition) for the changed cam track. The new reference position is composed as follows depending on the direction:

  - Positive effective direction: Current reference position (&lt;TO&gt;.MatchPosition) + cam track length (&lt;TO&gt;.Parameter.CamTrackLength)
  - Negative effective direction: Current reference position (&lt;TO&gt;.MatchPosition) - cam track length (&lt;TO&gt;.Parameter.CamTrackLength)
- Output the changes of the cam track when calling the Motion Control instruction "MC_CamTrack" and "Mode" = 1.

##### Example

The following figure shows an example of the differences in the activation behavior.

![Example](images/169108938891_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| A1 | A | The cam track is activated the first time with "MC_CamTrack.Enable" = TRUE and the output cams are output immediately with set "MC_CamTrack.Mode" = 0. |
| B | After cam track data were changed (①), the cam track is activated by calling Motion Control instruction "MC_CamTrack" with "Enable" = TRUE and the modified data takes effect immediately (①) with set "MC_CamTrack.Mode" = 0. |  |
| A2 | A | The cam track is activated the first time with "MC_CamTrack.Enable" = TRUE and the output cams are output immediately with set "MC_CamTrack.Mode" = 1. |
| B | After cam track data were changed (①), the cam track is activated by calling Motion Control instruction "MC_CamTrack" with "Enable" = TRUE and the modified data takes effect at the end of the current track cycle (②) with set "MC_CamTrack.Mode" = 1. |  |

#### Hysteresis (S7-1500, S7-1500T)

The hysteresis is set in the cam track technology object. The behavior and effect of the hysteresis setting corresponds to the [hysteresis](#hysteresis-s7-1500-s7-1500t) for the output cam technology object.

#### Time offset of output cam switching points (S7-1500, S7-1500T)

Switching times of the output and the connected actuator (e.g. valve) can be compensated for using the activation time or deactivation time of the cam track technology object.

The time offset of output cam switching points corresponds to the [activation time or deactivation time](#compensation-of-actuator-switching-times-s7-1500-s7-1500t) for the output cam technology object.

#### Tags: Cam track technology object (S7-1500, S7-1500T)

The following technology object tags are relevant:

| Status indicator |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.Status | Status of the cam track function |  |
| 0 | Inactive |  |
| 1 | Active |  |
| 2 | Active and waiting for next track |  |
| &lt;TO&gt;.TrackOutput | An output cam of cam track is switched. |  |
| &lt;TO&gt;.SingleCamState | Switched on output cam (bit-masked) |  |
| &lt;TO&gt;.TrackPosition | Display of the current position within the cam track  The distance to the current reference position of the current cam track (&lt;TO&gt;.MatchPosition) is displayed. |  |
| &lt;TO&gt;.MatchPosition | Reference position of the current cam track  During cyclic processing of the cam track, the continued reference position of the current cam track is displayed. The unique detection and output of the position is only possible when the assigned technology object is in motion. |  |

| Parameters |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.Parameter.CamTrackType | Output cam type |  |
| 0 | Distance output cam |  |
| 1 | Time-based output cam |  |
| &lt;TO&gt;.Parameter.PositionType | Position reference |  |
| 0 | Position setpoint |  |
| 1 | Actual position |  |
| &lt;TO&gt;.Parameter.ReferencePosition | Reference position |  |
| &lt;TO&gt;.Parameter.CamTrackLength | Track length |  |
| &lt;TO&gt;.Parameter.CamMasking | Bit masking of individual output cams |  |
| &lt;TO&gt;.Parameter.OnCompensation | Activation time (lead time for the switch-on edge) |  |
| &lt;TO&gt;.Parameter.OffCompensation | Deactivation time (lead time for the switch-off edge) |  |
| &lt;TO&gt;.Parameter.Hysteresis | Hysteresis value |  |
| &lt;TO&gt;.Parameter.Cam[1..32].OnPosition | Start position (distance output cams and time-based output cams) |  |
| &lt;TO&gt;.Parameter.Cam[1..32].OffPosition | End position (distance output cam) |  |
| &lt;TO&gt;.Parameter.Cam[1..32].Duration | Switch-on duration (time-based output cam) |  |
| &lt;TO&gt;.Parameter.Cam[1..32].Existent | Validity of an output cam |  |
| FALSE | Output cam is not used. |  |
| TRUE | Output cam is used. |  |

| Interface |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.Interface.EnableOutput | Output cam output at the bit specified under "Address" |  |
| FALSE | No output |  |
| TRUE | Output |  |
| &lt;TO&gt;.Interface.Address | I/O address for digital output cam output |  |

| Units |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.Units.LengthUnit | Unit of the length data |
| &lt;TO&gt;.Units.TimeUnit | Unit of the time data |

| StatusWord |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.StatusWord.X0 (Control) | The technology object is in operation. |
| &lt;TO&gt;.StatusWord.X1 (Error) | An error occurred at the technology object. |
| &lt;TO&gt;.StatusWord.X2 (RestartActive) | The technology object is being reinitialized. The tags of the technology data block are not updated with active restart. |
| &lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged) | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object. |
| &lt;TO&gt;.StatusWord.X4 (OutputInverted) | The output cam output is inverted. |
| &lt;TO&gt;.StatusWord.X5 (CommunicationOk) | The cam track is synchronized with the output module and available for use. |
| &lt;TO&gt;.StatusWord.X6 (CamDataChanged) | The data of individual output cams has been changed but not yet taken effect with Motion Control instruction "MC_CamTrack". |

| ErrorWord |  |
| --- | --- |
| Tag | Description |
| &lt;TO&gt;.ErrorWord.X0 (SystemFault) | A system-internal error has occurred. |
| &lt;TO&gt;.ErrorWord.X1 (ConfigFault) | Configuration error  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program. |
| &lt;TO&gt;.ErrorWord.X2 (UserFault) | Error in user program at a Motion Control instruction or its use. |
| &lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted) | Command cannot be executed   A Motion Control instruction cannot be executed because the necessary conditions have not been met. |
| &lt;TO&gt;.ErrorWord.X13 (PeripheralError) | Error accessing a logical address. |

| ErrorDetail |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.ErrorDetail.Number | Alarm number  You can find a list of the technology alarms and alarm responses in the "[Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation. |  |
| &lt;TO&gt;.ErrorDetail.Reaction | Effective alarm response |  |
| 0 | No reaction |  |
| 5 | Cam track processing is complete. |  |

## Configuring (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuring the technology object measuring input (S7-1500, S7-1500T)](#configuring-the-technology-object-measuring-input-s7-1500-s7-1500t)
- [Configuring the output cam technology object (S7-1500, S7-1500T)](#configuring-the-output-cam-technology-object-s7-1500-s7-1500t)
- [Configuring the cam track technology object (S7-1500, S7-1500T)](#configuring-the-cam-track-technology-object-s7-1500-s7-1500t)

### Configuring the technology object measuring input (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuration - Basic parameters (S7-1500, S7-1500T)](#configuration---basic-parameters-s7-1500-s7-1500t)
- [Configuration - Hardware interface (S7-1500, S7-1500T)](#configuration---hardware-interface-s7-1500-s7-1500t)
- [Configuration - Extended parameters (S7-1500, S7-1500T)](#configuration---extended-parameters-s7-1500-s7-1500t)

#### Configuration - Basic parameters (S7-1500, S7-1500T)

Configure the basic properties of the technology object in the "Basic parameters" configuration window.

##### Name

Define the name of the measuring input in this field. The technology object is listed under this name in the project tree. The tags of the measuring input can be used in the user program under this name.

##### Assigned axis or external encoder

The axis or external encoder assigned to the measuring input is displayed. You can use the button ![Assigned axis or external encoder](images/134670054155_DV_resource.Stream@PNG-de-DE.png) to directly access the configuration of the basic parameters of the higher-level technology object.

##### Unit of measure

The indicated unit of measure for the position of the measuring input corresponds to the unit of measure of the higher-level technology object.

To use six decimal places in the selected unit, select the check box "Use position values with higher resolution" in the higher-level technology object.

---

**See also**

[Units of measure (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#units-of-measure-s7-1500-s7-1500t)
  
[Measuring input technology object (S7-1500, S7-1500T)](#measuring-input-technology-object-s7-1500-s7-1500t)

#### Configuration - Hardware interface (S7-1500, S7-1500T)

##### Measuring input type

Select the measuring input type.

- Measurement using Timer DI
- Measurement using SINAMICS (central probe)
- Measurement using PROFIdrive telegram (drive or external encoder)
- Measuring via monitoring

You can only operate a measuring input with a technology object measuring input.

**Overview of possible measurement inputs and measuring types**

| Measuring input type | Possible measurement inputs | Possible measuring types |
| --- | --- | --- |
| **Measurement using Timer DI**   ("STANDARD") | With Timer DI  - ET 200SP or ET 200MP TM Timer DIDQ - SIMATIC Drive Controller (X142) | - "MC_MeasuringInput" (One-time measuring) - "MC_MeasuringInputCyclic" (Cyclic measuring) |
| **Measurement using SINAMICS  (central probe)**   ("STANDARD") | Using telegram 39x of the drive control:  - SINAMICS S120 CU320-2 (X122/X132) - SINAMICS S120 CU310-2 (X121/X131) - SIMATIC Drive Controller (X122/X132) |  |
| **Measurement using PROFIdrive telegrams**   ("PROFIDRIVE") | Using PROFIdrive telegram of the drive axis:  - SINAMICS S210 (X130) - SINAMICS S120 CU320-2 (X122/X132) - SINAMICS S120 CU310-2 (X121/X131) - SIMATIC Drive Controller (X122/X132) | "MC_MeasuringInput" (One-time measuring) |
| **Measuring via monitoring**   ("MONITORING") | - No assignment to measurement input necessary - Assignment to another measuring probe with measurement input | Measuring jobs are rejected with an error on monitoring probes. The measurement tasks are initiated at the assigned monitoring probe with measurement input.  Monitoring probes support the measuring types of the assigned measuring probe with measurement input. • "MC_MeasuringInput" (one-time measurement) • "MC_MeasuringInputCyclic" (cyclic measurement) |

##### Measurement using Timer DI

Select a measurement input for a measurement using a Timer DI. The selection box shows all channels that are configured correctly. For this purpose, you need to have configured the I/O channels as Timer DI beforehand.

##### Measurement using SINAMICS (central probe)

Select a measuring input for a measurement via SINAMICS measurement sensing input. The selection box shows all compatible telegram types. You are shown all terminals that can potentially be used as measuring inputs. For this purpose, you need to have configured the necessary central measuring inputs on the drive side beforehand.

For SINAMICS drives that are not configured via Startdrive, you need to assign the inputs to the measuring inputs (p680) in the telegram without gaps and in ascending order.

With p728.8 to p728.15, you configure as input all DI/DQs used as measurement input on the control unit. Use p680 of the control unit to specify the terminals for the global measuring inputs.

You need to configure telegram 391, 392 or 393 on the control unit. Telegrams 394 and 395 must be configured as free telegrams.

##### Measurement using PROFIdrive telegram (drive or external encoder)

For a measurement via PROFIdrive telegram, select the number of the measuring input in the telegram in the "Number of the measuring input" drop-down list. The input field is preset with the value "1".

Two communication channels are available for the transmission of measured values in the PROFIdrive telegram. These communication channels are assigned to one measurement input/digital input each in the drive. Use the PROFIdrive parameters to configure the digital input on the drive that is to be used for the configured communication channel.

- Measurement input for the first communication channel

  ("&lt;TO&gt;.Parameter.PROFIdriveProbeNumber" = 1)

  If you use two encoders, you must select the associated DI in the SINAMICS for each encoder. Various results are then transferred to the technology object depending on the selected encoder. The encoders are configured using the parameters p488[0] and p488[1].
- Measurement input for the second communication channel

  ("&lt;TO&gt;.Parameter.PROFIdriveProbeNumber" = 2)

  If you use two encoders, you must select the associated DI in the SINAMICS for each encoder. Various results are then transferred to the technology object depending on the selected encoder. The encoders are configured using the parameters p489[0] and p489[1].

##### Measuring via monitoring

To set the measuring input as "monitoring", proceed as follows:

- Create the new measuring input below the respective axis.
- In the functional view of the measuring probe configuration, select the "Measuring via monitoring " mode under the "Hardware Interface."
- In the "Probe with measurement input" selection field, select the axis or external encoder with the measurement input.

##### Correction time for the measuring signal

Specify a correction time if possible delay times in the measurement signal are to be compensated.

---

**See also**

[Transferring drive and encoder parameters automatically (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#transferring-drive-and-encoder-parameters-automatically-s7-1500-s7-1500t)
  
[Use a measurement input for several axes (S7-1500, S7-1500T)](#use-a-measurement-input-for-several-axes-s7-1500-s7-1500t)
  
[Measuring input technology object (S7-1500, S7-1500T)](#measuring-input-technology-object-s7-1500-s7-1500t)
  
[Configuring technological modules and onboard I/O for Motion Control (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#configuring-technological-modules-and-onboard-io-for-motion-control-s7-1500-s7-1500t)

#### Configuration - Extended parameters (S7-1500, S7-1500T)

##### Adjustment for activation time of the measuring range

To adjust the activation time defined on the system side, enter an additional activation time here.

The configuration window also displays the following times calculated on the system side:

- Time after output of the measuring job until the measuring event can be detected
- Time after the measuring event until the measurement result is displayed (for measuring of one or two edges)

---

**See also**

[Measuring with measuring range (S7-1500, S7-1500T)](#measuring-with-measuring-range-s7-1500-s7-1500t)
  
[Time-related boundary conditions (S7-1500, S7-1500T)](#time-related-boundary-conditions-s7-1500-s7-1500t)
  
[Measuring input technology object (S7-1500, S7-1500T)](#measuring-input-technology-object-s7-1500-s7-1500t)

### Configuring the output cam technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuration - Basic parameters (S7-1500, S7-1500T)](#configuration---basic-parameters-s7-1500-s7-1500t-1)
- [Configuration - Hardware interface (S7-1500, S7-1500T)](#configuration---hardware-interface-s7-1500-s7-1500t-1)
- [Extended parameters (S7-1500, S7-1500T)](#extended-parameters-s7-1500-s7-1500t)

#### Configuration - Basic parameters (S7-1500, S7-1500T)

Configure the basic properties of the technology object in the "Basic parameters" configuration window.

##### Name

Define the name of the output cam in this field. The technology object is listed under this name in the project tree. The tags of the output cam can be used in the user program under this name.

##### Assigned axis or external encoder

The axis or external encoder assigned to the output cam is displayed. You can use the button ![Assigned axis or external encoder](images/134670054155_DV_resource.Stream@PNG-de-DE.png) to directly access the configuration of the basic parameters of the higher-level technology object.

##### Output cam type

Select based on the desired switching behavior of an output cam type:

- Distance output cam (position-dependent switch-on/switch-off)
- Time-based output cam (position-dependent switch-on and position-independent or time-dependent switch-off)

##### Output cam reference

Configure in this selection whether the switching points of the output cam are to reference the actual position or the position setpoint.

##### Unit of measure

The indicated unit of measure for the position of the output cam corresponds to the unit of measure of the higher-level technology object.

To use six decimal places in the selected unit, select the check box "Use position values with higher resolution" in the higher-level technology object.

When a time-based output cam is selected as the output cam type, the unit of measure for the switch-on duration and other times is also indicated. For output cams, this is always ms.

---

**See also**

[Units of measure (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#units-of-measure-s7-1500-s7-1500t)
  
[Output cam technology object (S7-1500, S7-1500T)](#output-cam-technology-object-s7-1500-s7-1500t)

#### Configuration - Hardware interface (S7-1500, S7-1500T)

##### Output cam output

Select whether the generated switching signals are to be output at the digital output.

- **Activate output**

  Select one of the following two output options for the output cam output:

  - **Output via Timer DQ**

    With output via a Timer DQ, you select a suitable channel in the "Output" field. The selection box shows all channels that are configured as Timer DQ. For this purpose, you need to have configured the I/O channels as Timer DQ beforehand.

    Timer DQs are supported by:

    - ET 200MP TM Timer DIDQ 16x24V

    - ET 200SP TM Timer DIDQ 10x24V

    - SIMATIC Drive Controller (X142)
  - **Output by digital output module**

    For output by a digital output module, select this in the "Output cam output" field. Only the digital outputs with previously defined PLC tags are displayed for selection.

  Select the logical operation of the output cam signal at the output. The logic operation relates to the last signal to be output after the set inversion, if any.

  All output cams that use the selected output are shown graphically.
- **Output deactivated**

  When the output is deactivated, the output cam is evaluated only in the software.

---

**See also**

[Output cam technology object (S7-1500, S7-1500T)](#output-cam-technology-object-s7-1500-s7-1500t)
  
[Configuring technological modules and onboard I/O for Motion Control (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#configuring-technological-modules-and-onboard-io-for-motion-control-s7-1500-s7-1500t)

#### Extended parameters (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuration - Activation time (S7-1500, S7-1500T)](#configuration---activation-time-s7-1500-s7-1500t)
- [Configuration - Hysteresis (S7-1500, S7-1500T)](#configuration---hysteresis-s7-1500-s7-1500t)

##### Configuration - Activation time (S7-1500, S7-1500T)

The specified output cam type is indicated in the upper area of the "Activation time" configuration window.

###### Activation time and deactivation time

For a time shift of the switch-on and switch-off times of an output cam, enter an activation time and a deactivation time.

---

**See also**

[Compensation of actuator switching times (S7-1500, S7-1500T)](#compensation-of-actuator-switching-times-s7-1500-s7-1500t)
  
[Output cam technology object (S7-1500, S7-1500T)](#output-cam-technology-object-s7-1500-s7-1500t)

##### Configuration - Hysteresis (S7-1500, S7-1500T)

To prevent unwanted changes in the switching state of the output cams of a cam track, enter a hysteresis value.

When using an output cam with reference to actual position, always enter a hysteresis value (&gt; 0.0).

---

**See also**

[Hysteresis (S7-1500, S7-1500T)](#hysteresis-s7-1500-s7-1500t)
  
[Output cam technology object (S7-1500, S7-1500T)](#output-cam-technology-object-s7-1500-s7-1500t)

### Configuring the cam track technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuration - Basic parameters (S7-1500, S7-1500T)](#configuration---basic-parameters-s7-1500-s7-1500t-2)
- [Configuration - Hardware interface (S7-1500, S7-1500T)](#configuration---hardware-interface-s7-1500-s7-1500t-2)
- [Extended parameters (S7-1500, S7-1500T)](#extended-parameters-s7-1500-s7-1500t-1)

#### Configuration - Basic parameters (S7-1500, S7-1500T)

Configure the basic properties of the technology object in the "Basic parameters" configuration window.

##### Name

Define the name of the cam track in this field. The technology object is listed under this name in the project tree. The tags of the cam track can be used in the user program under this name.

##### Assigned axis or external encoder

The axis or external encoder assigned to the cam track is displayed. You can use the button ![Assigned axis or external encoder](images/134670054155_DV_resource.Stream@PNG-de-DE.png) to directly access the configuration of the basic parameters of the higher-level technology object.

##### Output cam type

Select based on the desired switching behavior of an output cam type for the cam track:

- Distance output cam (position-dependent switch-on/switch-off)
- Time-based output cam (position-dependent switch-on and position-independent or time-dependent switch-off)

##### Output cam reference

In this selection, configure whether the switching points of the cam track are to reference the actual position or the position setpoint.

##### Unit of measure

The indicated unit of measure for the position of the cam track corresponds to the unit of measure of the higher-level technology object.

To use six decimal places in the selected unit, select the check box "Use position values with higher resolution" in the higher-level technology object.

When a time-based output cam is selected as the output cam type, the unit of measure for the switch-on duration and other times is also indicated. For output cams, this is always ms.

---

**See also**

[Units of measure (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#units-of-measure-s7-1500-s7-1500t)
  
[Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)

#### Configuration - Hardware interface (S7-1500, S7-1500T)

##### Output cam track

Select whether the generated switching signals are to be output at the digital output.

- **Activate output**

  Select one of the following two output options for the output track:

  - Output via Timer DQ

    With output via a Timer DQ, you select a suitable channel in the "Output" field. The selection box shows all channels that are configured as Timer DQ. For this purpose, you need to have configured the I/O channels as Timer DQ beforehand.

    Timer DQs are supported by:

    - ET 200MP TM Timer DIDQ 16x24V

    - ET 200SP TM Timer DIDQ 10x24V

    - SIMATIC Drive Controller (X142)
  - Output by digital output module

    For output by a digital output module, select this in the "Output cam output" field. Only the digital outputs with previously defined PLC tags are displayed for selection.
- **Deactivate output**

  When the output is deactivated, the cam track is evaluated only in the software.

---

**See also**

[Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)
  
[Configuring technological modules and onboard I/O for Motion Control (S7-1500, S7-1500T)](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#configuring-technological-modules-and-onboard-io-for-motion-control-s7-1500-s7-1500t)

#### Extended parameters (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Track data (S7-1500, S7-1500T)](#track-data-s7-1500-s7-1500t)
- [Configuration - Output cam data (S7-1500, S7-1500T)](#configuration---output-cam-data-s7-1500-s7-1500t)

##### Track data (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuration - Activation time (S7-1500, S7-1500T)](#configuration---activation-time-s7-1500-s7-1500t-1)
- [Configuration - Hysteresis (S7-1500, S7-1500T)](#configuration---hysteresis-s7-1500-s7-1500t-1)
- [Configuration - Track dimensions (S7-1500, S7-1500T)](#configuration---track-dimensions-s7-1500-s7-1500t)

###### Configuration - Activation time (S7-1500, S7-1500T)

The set output cam type is displayed.

###### Activation time and deactivation time

Enter the activation time and the deactivation time.

For a time shift of the switch-on and switch-off times of the output cam of a cam track, enter an activation time and a deactivation time.

---

**See also**

[Time offset of output cam switching points (S7-1500, S7-1500T)](#time-offset-of-output-cam-switching-points-s7-1500-s7-1500t)
  
[Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)

###### Configuration - Hysteresis (S7-1500, S7-1500T)

To prevent unwanted changes in the switching state of the output cams of a cam track, enter a hysteresis value.

When using an output cam with reference to actual position, always enter a hysteresis value (&gt; 0.0).

---

**See also**

[Hysteresis (S7-1500, S7-1500T)](#hysteresis-s7-1500-s7-1500t-1)
  
[Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)

###### Configuration - Track dimensions (S7-1500, S7-1500T)

###### Track length

Enter the corresponding track length.

Also take into account the output cam data of the individual output cams when defining the track length. Output cams whose start position lies outside the cam track length are not included. They become active only if the cam track length is increased so that at least the respective start position of an output cam is within the new track length.

###### Axis reference position

Enter the position of an axis or external encoder starting from which the output of the cam track is to occur. The start of the cam track is placed at the entered position.

You can enter a negative or positive value for the reference position.

###### Modulo length of the axis

When an axis with modulo function is used, the modulo length of the axis is displayed.

---

**See also**

[Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)

##### Configuration - Output cam data (S7-1500, S7-1500T)

The set output cam type is displayed.

Enter the properties for the output cams of the cam track that are to be output. You can set up to 32 individual output cams on a cam track.

Also take into account any previously defined track length when defining the output cam data. Output cams whose start position lies outside the cam track length are not included. They become active only if the cam track length is increased so that at least the respective start position of an output cam is within the new track length.

The input options described below are displayed in the Output cam data configuration window according to the configured output cam type.

- **Valid**

  Only output cams set as "valid" are output and have a status display.
- **Start position**

  - The start position may not be greater than the end position for distance output cams.
  - If the start position is equal to the end position, the distance output cam does not switch.
  - The switching ranges of individual output cams are permitted to overlap.
- **End position**

  - The "End position" column is only displayed when distance output cam is set for the output cam type.
  - The end position must not be less than the start position.
- **Switch-on duration**

  The "Switch-on duration" column is only displayed when time-based output cam is set for the output cam type.

---

**See also**

[Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t)

## Diagnostics (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction to diagnostics (S7-1500, S7-1500T)](#introduction-to-diagnostics-s7-1500-s7-1500t)
- [Measuring input technology object (S7-1500, S7-1500T)](#measuring-input-technology-object-s7-1500-s7-1500t-1)
- [Output cam technology object (S7-1500, S7-1500T)](#output-cam-technology-object-s7-1500-s7-1500t-1)
- [Cam track technology object (S7-1500, S7-1500T)](#cam-track-technology-object-s7-1500-s7-1500t-1)

### Introduction to diagnostics (S7-1500, S7-1500T)

The description of Motion Control diagnostics is limited to the diagnostics view of the technology objects in TIA Portal, the technology alarms and the error IDs on Motion Control instructions.

The following descriptions can be found in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation:

- [Diagnostics concept](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#diagnostics-concept-s7-1500-s7-1500t-1)
- [Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#technology-alarms-s7-1500-s7-1500t)
- [Error IDs in Motion Control instructions](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#error-ids-in-motion-control-instructions-s7-1500-s7-1500t)

A comprehensive description of the system diagnostics of the S7‑1500 CPU can be found in the ["Diagnostics" function manual](https://support.industry.siemens.com/cs/ww/en/view/59192926).

### Measuring input technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500, S7-1500T)](#status-and-error-bits-s7-1500-s7-1500t)

#### Status and error bits (S7-1500, S7-1500T)

You use the "Technology object &gt; Diagnostics &gt; Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Measuring input status

The following table shows the possible states of the measuring input:

| Status | Description |
| --- | --- |
| Active | The technology object is in operation.   (&lt;TO&gt;.StatusWord.X0 (Control)) |
| Waiting for measuring event | The measuring input is waiting for a measuring event.  The technology data block tag "&lt;TO&gt;.Status" has the value "1" ("WAITING_FOR_TRIGGER"). |
| Measured value present | The measuring input has acquired one or more measured values.  The technology data block tag "&lt;TO&gt;.Status" has the value "2" ("TRIGGER_OCCURRED"). |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "&lt;TO&gt;.ErrorDetail.Number" and "&lt;TO&gt;.ErrorDetail.Reaction" tags of the technology object.  (&lt;TO&gt;.StatusWord.X1 (Error)) |
| Restart active | The technology object is reinitialized. The tags of the technology data block are not updated with active restart.  (&lt;TO&gt;.StatusWord.X2 (RestartActive)) |
| Measuring input ready | The measuring input is synchronized with the measurement input and can be used.  With the monitoring probe, the bit always has the value "FALSE".  (&lt;TO&gt;.StatusWord.X5 (CommunicationOK)) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (&lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (&lt;TO&gt;.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (&lt;TO&gt;.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program with a Motion Control instruction or its use.  (&lt;TO&gt;.ErrorWord.X2 (UserFault)) |
| Job rejected | A job cannot be executed.  A Motion Control instruction cannot be executed because the necessary conditions have not been met (e.g. axis assigned to the measuring input is not homed).  (&lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted)) |
| I/O | An error occurred accessing a logical address.  (&lt;TO&gt;.ErrorWord.X13 (PeripheralError)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

---

**See also**

["StatusWord" tag (measuring input) (S7-1500, S7-1500T)](#statusword-tag-measuring-input-s7-1500-s7-1500t)
  
["ErrorWord" tag (measuring input) (S7-1500, S7-1500T)](#errorword-tag-measuring-input-s7-1500-s7-1500t)
  
["WarningWord" tag (measuring input) (S7-1500, S7-1500T)](#warningword-tag-measuring-input-s7-1500-s7-1500t)

### Output cam technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500, S7-1500T)](#status-and-error-bits-s7-1500-s7-1500t-1)

#### Status and error bits (S7-1500, S7-1500T)

You use the "Technology object &gt; Diagnostics &gt; Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Output cam status

The following table shows the possible states of the output cam:

| Status | Description |
| --- | --- |
| Active | The technology object is in operation.  (&lt;TO&gt;.StatusWord.X0 (Control)) |
| Switched | The output cam is switched.  (&lt;TO&gt;.CamOutput) |
| Inverted output for output cam | The output cam output is inverted.  (&lt;TO&gt;.StatusWord.X4 (OutputInverted)) |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "&lt;TO&gt;.ErrorDetail.Number" and "&lt;TO&gt;.ErrorDetail.Reaction" tags of the technology object.  (&lt;TO&gt;.StatusWord.X1 (Error)) |
| Restart active | The technology object is being reinitialized. The tags of the technology data block are not updated with active restart.  (&lt;TO&gt;.StatusWord.X2 (RestartActive)) |
| Output cam output ready | The output cam is synchronized with the output module and available for use.  (&lt;TO&gt;.StatusWord.X5 (CommunicationOk)) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (&lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (&lt;TO&gt;.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (&lt;TO&gt;.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program with a Motion Control instruction or its use.  (&lt;TO&gt;.ErrorWord.X2 (UserFault)) |
| Job rejected | A job cannot be executed.   A Motion Control instruction cannot be executed because the necessary conditions have not been met (e.g. axis assigned to the output cam is not homed).  (&lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted)) |
| I/O | An error occurred accessing a logical address.  (&lt;TO&gt;.ErrorWord.X13 (PeripheralError)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

---

**See also**

["StatusWord" tag (output cam) (S7-1500, S7-1500T)](#statusword-tag-output-cam-s7-1500-s7-1500t)
  
["ErrorWord" tag (output cam) (S7-1500, S7-1500T)](#errorword-tag-output-cam-s7-1500-s7-1500t)
  
["WarningWord" tag (output cam) (S7-1500, S7-1500T)](#warningword-tag-output-cam-s7-1500-s7-1500t)

### Cam track technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Status and error bits (S7-1500, S7-1500T)](#status-and-error-bits-s7-1500-s7-1500t-2)
- [Cam track status (S7-1500, S7-1500T)](#cam-track-status-s7-1500-s7-1500t)

#### Status and error bits (S7-1500, S7-1500T)

You use the "Technology object &gt; Diagnostics &gt; Status and error bits" diagnostic function in the TIA Portal to monitor the status and error messages for the technology object. The diagnostics function is available in online operation.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### Cam track status

The following table shows the possible states of the cam track:

| Status | Description |
| --- | --- |
| Active | The technology object is in operation.  (&lt;TO&gt;.StatusWord.X0 (Control)) |
| Switched | An output cam of cam track is switched.  (&lt;TO&gt;.TrackOutput) |
| Inverted output for output cam | The output cam output is inverted.  (&lt;TO&gt;.StatusWord.X4 (OutputInverted)) |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "&lt;TO&gt;.ErrorDetail.Number" and "&lt;TO&gt;.ErrorDetail.Reaction" tags of the technology object.  (&lt;TO&gt;.StatusWord.X1 (Error)) |
| Restart active | The technology object is being reinitialized. The tags of the technology data block are not updated with active restart.  (&lt;TO&gt;.StatusWord.X2 (RestartActive)) |
| Cam track output ready | The cam track is synchronized with the output module and available for use.  (&lt;TO&gt;.StatusWord.X5 (CommunicationOk)) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (&lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged)) |

##### Error

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (&lt;TO&gt;.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (&lt;TO&gt;.ErrorWord.X1 (ConfigFault)) |
| User program | An error occurred in the user program with a Motion Control instruction or its use.  (&lt;TO&gt;.ErrorWord.X2 (UserFault)) |
| Job rejected | A job cannot be executed.  A Motion Control instruction cannot be executed because the necessary conditions have not been met (e.g. axis assigned to the cam track is not homed).  (&lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted)) |
| I/O | An error occurred accessing a logical address.  (&lt;TO&gt;.ErrorWord.X13 (PeripheralError)) |

##### Alarm display

For more information and to acknowledge the error, go to the Inspector window by clicking on the "Alarm display" link.

##### More information

An option for evaluating the individual status bits can be found in the section "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Motion Control overview" documentation.

---

**See also**

["StatusWord" tag (cam track) (S7-1500, S7-1500T)](#statusword-tag-cam-track-s7-1500-s7-1500t)
  
["ErrorWord" tag (cam track) (S7-1500, S7-1500T)](#errorword-tag-cam-track-s7-1500-s7-1500t)
  
["WarningWord" tag (cam track) (S7-1500, S7-1500T)](#warningword-tag-cam-track-s7-1500-s7-1500t)

#### Cam track status (S7-1500, S7-1500T)

You use the "Technology object &gt; Diagnostics &gt; Cam track status" diagnostics function in the TIA Portal to monitor the status of the cam track. The Diagnostics function is available in online operation.

##### "Validity and masking of the output cams" area

The individual output cams of a cam track are shown in this area along with the status for the following properties:

| Status | Description |
| --- | --- |
| Valid | Validity of the individual output cams of the cam track  (&lt;TO&gt;.Parameter.Cam[1..32].Existent) |
| Masked | Bit masking of the individual cams of the cam track  (&lt;TO&gt;.Parameter.CamMasking) |
| Effective | Switched on output cam (bit-masked)  (&lt;TO&gt;.SingleCamState) |

##### "Positions" area

The following status values are displayed in this area:

| Status | Description |
| --- | --- |
| Current position in the cam track | Position during cam track processing within a cam track cycle  The distance to the current reference position of the current cam track (&lt;TO&gt;.MatchPosition) is displayed.  (&lt;TO&gt;.TrackPosition) |
| Current cam track start | Reference position of the current cam track  During cyclic processing of the cam track, the continued reference position of the current cam track is displayed. The unique detection and output of the position is only possible when the assigned technology object is in motion.  (&lt;TO&gt;.MatchPosition) |

## Tags of the technology object data blocks (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Tags of the measuring input technology object (S7-1500, S7-1500T)](#tags-of-the-measuring-input-technology-object-s7-1500-s7-1500t)
- [Tags of the output cam technology object (S7-1500, S7-1500T)](#tags-of-the-output-cam-technology-object-s7-1500-s7-1500t)
- [Tags of the cam track technology object (S7-1500, S7-1500T)](#tags-of-the-cam-track-technology-object-s7-1500-s7-1500t)

### Tags of the measuring input technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t)
- [Display data (measuring input) (S7-1500, S7-1500T)](#display-data-measuring-input-s7-1500-s7-1500t)
- ["Parameter" tag (measuring input) (S7-1500, S7-1500T)](#parameter-tag-measuring-input-s7-1500-s7-1500t)
- ["Interface" tag (measuring input) (S7-1500, S7-1500T)](#interface-tag-measuring-input-s7-1500-s7-1500t)
- ["Units" tag (measuring input) (S7-1500, S7-1500T)](#units-tag-measuring-input-s7-1500-s7-1500t)
- ["MeasuredValues" tag (measuring input) (S7-1500, S7-1500T)](#measuredvalues-tag-measuring-input-s7-1500-s7-1500t)
- ["StatusWord" tag (measuring input) (S7-1500, S7-1500T)](#statusword-tag-measuring-input-s7-1500-s7-1500t)
- ["ErrorWord" tag (measuring input) (S7-1500, S7-1500T)](#errorword-tag-measuring-input-s7-1500-s7-1500t)
- ["ErrorDetail" tag (measuring input) (S7-1500, S7-1500T)](#errordetail-tag-measuring-input-s7-1500-s7-1500t)
- ["WarningWord" tag (measuring input) (S7-1500, S7-1500T)](#warningword-tag-measuring-input-s7-1500-s7-1500t)

#### Legend (S7-1500, S7-1500T)

|  |  |  |
| --- | --- | --- |
| Tag | Name of the tag |  |
| Data type | Data type of the tag |  |
| Values | Value range of the tag - minimum value to maximum value  If no specific value is shown, the value range limits of the relevant data type apply or the information under "Description". |  |
| W | Effectiveness of changes in the technology data block |  |
| DIR | Direct:  Values are changed via direct assignment and take effect at the start of the next MC_Servo. |  |
| CAL | At call of Motion Control instruction:  Values are changed directly and take effect at the start of the next MC_Servo  after the call of the corresponding Motion Control instruction in the user program. |  |
| RES | Restart:  Changes to the start value in the load memory are made using the extended instruction "WRIT_DBL" (write to DB in load memory). Changes will not take effect until after restart of the technology object. |  |
| RON | Read only:  The tag cannot and must not be changed during runtime of the user program. |  |
| Description | Description of the tag |  |

Access to the tags is with "&lt;TO&gt;.&lt;tag name&gt;". The placeholder &lt;TO&gt; represents the name of the technology object.

#### Display data (measuring input) (S7-1500, S7-1500T)

The "&lt;TO&gt;.Status" and "&lt;TO&gt;.InputState" tags show the status of the measuring input function and the measurement input.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| Status | DINT | - | RON | Status of the measuring input function |  |
| 0 | "INACTIVE"  No measurement is active. |  |  |  |  |
| 1 | "WAITING_FOR_TRIGGER"  The measuring input is waiting for the measuring event. |  |  |  |  |
| 2 | "TRIGGER_OCCURRED"  One or more measured values have been captured. |  |  |  |  |
| 3 | "MEASURING_ERROR"  Error during the measurement |  |  |  |  |
| InputState | BOOL | - | RON | Status of the measurement input |  |
| FALSE | Measurement input inactive |  |  |  |  |
| TRUE | Measurement input active |  |  |  |  |

#### "Parameter" tag (measuring input) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Parameter.&lt;tag name&gt;" contains the configuration of the basic parameters of the measuring input technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Parameter. |  | TO_MeasuringInput_Struct_Parameter |  |  |  |  |
|  | MeasuringInputType | DINT | 0…2 | RON | Measuring input type |  |
| 0 | "STANDARD"  Measurement using time stamp |  |  |  |  |  |
| 1 | "PROFIDRIVE"  Measuring event using PROFIdrive telegram |  |  |  |  |  |
| 2 | "MONITORING"  "Measuring via monitoring" Capture a measuring event of another measuring input technology object |  |  |  |  |  |
| PROFIdriveProbeNumber | UDINT | 1, 2 | RES | Number of the measuring input to be used for a measurement via PROFIdrive telegram |  |  |
| MeasuringRangeActivationTime | LREAL | 0.0 … 1.0E12 | RON | System share for activation time of measuring range |  |  |
| MeasuringRangeAdditionalActivationTime | LREAL | 0.0 … 1.0E12 | RES | Additional activation time when using measuring range limits [ms] |  |  |
| CorrectionTime | LREAL | 0.0 … 1.0E12 | RES | Correction time for the measurement result [ms] |  |  |

#### "Interface" tag (measuring input) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Interface.&lt;tag name&gt;" contains the configuration of the input properties for the measuring input technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Interface. |  | TO_MeasuringInput_Struct_Interface |  |  |  |
|  | Address | VREF | - | RON | I/O address for the digital measurement input  Not relevant for measuring via monitoring ("MeasuringInputType" = 2) |

#### "Units" tag (measuring input) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Units.&lt;tag name&gt;" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_MeasuringInput_Struct_Units |  |  |  |  |
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
| TimeUnit | UDINT | - | RON | Unit for time |  |  |
| 1056 | ms |  |  |  |  |  |
| <sup>1)</sup> Position values with higher resolution or six decimal places. |  |  |  |  |  |  |

#### "MeasuredValues" tag (measuring input) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.MeasuredValues.&lt;tag name&gt;" displays the measurement results.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| MeasuredValues. |  | TO_MeasuringInput_Struct_MeasuringValues |  |  |  |
|  | MeasuredValue1 | LREAL | -1.0E12 … 1.0E12 | RON | First measured value |
| MeasuredValue2 | LREAL | -1.0E12 … 1.0E12 | RON | Second measured value |  |
| MeasuredValue1Counter | UDINT | 0 … 2147483647 | RON | Count value for the first measured value |  |
| MeasuredValue2Counter | UDINT | 0 … 2147483647 | RON | Count value for the second measured value |  |
| LostEdgeCounter1 | UDINT | 0 … 7 | RON | LEC for measured value 1  (Zero in the case of one-time measurement) |  |
| LostEdgeCounter2 | UDINT | 0 … 7 | RON | LEC for measured value 2  (Zero in the case of one-time measurement) |  |

#### "StatusWord" tag (measuring input) (S7-1500, S7-1500T)

The "&lt;TO&gt;.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 2 "RestartActive") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Control"  The technology object is in operation. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | Reserved |  |
| Bit 5 | - | - | - | "CommunicationOK"  The communication between the measuring probe and measurement input is established.  With the monitoring probe, this bit always has the value "FALSE". |  |
| Bit 6... Bit 31 | - | - | - | Reserved |  |

#### "ErrorWord" tag (measuring input) (S7-1500, S7-1500T)

The "&lt;TO&gt;.ErrorWord" tag indicates technology object errors (technology alarms).

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
| Bit 4... Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralError"  Error accessing a logical address |  |
| Bit 14... Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (measuring input) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.ErrorDetail.&lt;tag name&gt;" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 6 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 6 | End measuring input processing |  |  |  |  |  |

#### "WarningWord" tag (measuring input) (S7-1500, S7-1500T)

The "&lt;TO&gt;.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 1 "ConfigWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4... Bit 12 | - | - | - | Reserved |  |
| Bit 13 |  |  |  | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14... Bit 31 | - | - | - | Reserved |  |

### Tags of the output cam technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t-1)
- [Display data (output cam) (S7-1500, S7-1500T)](#display-data-output-cam-s7-1500-s7-1500t)
- ["Parameter" tag (output cam) (S7-1500, S7-1500T)](#parameter-tag-output-cam-s7-1500-s7-1500t)
- ["Interface" tag (output cam) (S7-1500, S7-1500T)](#interface-tag-output-cam-s7-1500-s7-1500t)
- ["Units" tag (output cam) (S7-1500, S7-1500T)](#units-tag-output-cam-s7-1500-s7-1500t)
- ["StatusWord" tag (output cam) (S7-1500, S7-1500T)](#statusword-tag-output-cam-s7-1500-s7-1500t)
- ["ErrorWord" tag (output cam) (S7-1500, S7-1500T)](#errorword-tag-output-cam-s7-1500-s7-1500t)
- ["ErrorDetail" tag (output cam) (S7-1500, S7-1500T)](#errordetail-tag-output-cam-s7-1500-s7-1500t)
- ["WarningWord" tag (output cam) (S7-1500, S7-1500T)](#warningword-tag-output-cam-s7-1500-s7-1500t)

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

Access to the tags is with "&lt;TO&gt;.&lt;tag name&gt;". The placeholder &lt;TO&gt; represents the name of the technology object.

#### Display data (output cam) (S7-1500, S7-1500T)

The "&lt;TO&gt;.CamOutput" tag indicates the switching state of the output cam.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| CamOutput | BOOL | - | RON | Switching state of output cam |  |
| FALSE | Not switched |  |  |  |  |
| TRUE | Switched |  |  |  |  |

#### "Parameter" tag (output cam) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Parameter.&lt;tag name&gt;" contains the configuration of the basic parameters of the output cam technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Parameter. |  | TO_OutputCam_Struct_Parameter |  |  |  |  |
|  | OutputCamType | DINT | 0 … 2 | RES | Output cam type |  |
| 0 | Distance output cam |  |  |  |  |  |
| 1 | Time-based output cam |  |  |  |  |  |
| 2 | Switching output cam |  |  |  |  |  |
| PositionType | DINT | 0, 1 | RES | Position reference |  |  |
| 0 | Position setpoint |  |  |  |  |  |
| 1 | Actual position |  |  |  |  |  |
| OnCompensation | LREAL | 0.0 … 1.0E12 | DIR | Activation time  Lead time for the switch-on edge |  |  |
| OffCompensation | LREAL | 0.0 … 1.0E12 | DIR | Deactivation time  Lead time for the switch-off edge |  |  |
| Hysteresis | LREAL | 0.0 … 1.0E12 | DIR | Hysteresis value  For output cams with reference to actual position, always enter a hysteresis value (&gt; 0.0). |  |  |

#### "Interface" tag (output cam) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Interface.&lt;tag name&gt;" contains the configuration of the output properties for the output cam technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Interface. |  | TO_OutputCam_Struct_Interface |  |  |  |  |
|  | EnableOutput | BOOL | - | RES | Activation of the output cam output |  |
| FALSE | Output is deactivated |  |  |  |  |  |
| TRUE | Output is activated |  |  |  |  |  |
| Address | VREF | - | RON | I/O address of the output cam |  |  |
| LogicOperation | DINT | 0, 1 | RON | Logical operation of the output cam signals at the output |  |  |
| 0 | OR logic operation |  |  |  |  |  |
| 1 | AND logic operation |  |  |  |  |  |

#### "Units" tag (output cam) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Units.&lt;tag name&gt;" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_OutputCam_Struct_Units |  |  |  |  |
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
| TimeUnit | UDINT | - | RON | Unit for time |  |  |
| 1056 | ms |  |  |  |  |  |
| <sup>1)</sup> Position values with higher resolution or six decimal places. |  |  |  |  |  |  |

#### "StatusWord" tag (output cam) (S7-1500, S7-1500T)

The "&lt;TO&gt;.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 2 "RestartActive") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Control"  The technology object is in operation. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is being reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "OutputInverted"  The output cam output is inverted. |  |
| Bit 5 | - | - | - | "CommunicationOK"  The communication between output cam and output module is established. |  |
| Bit 6... Bit 31 | - | - | - | Reserved |  |

#### "ErrorWord" tag (output cam) (S7-1500, S7-1500T)

The "&lt;TO&gt;.ErrorWord" tag indicates technology object errors (technology alarms).

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
| Bit 4... Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralError"  Error accessing a logical address |  |
| Bit 14... Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (output cam) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.ErrorDetail.&lt;tag name&gt;" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 6 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 6 | Output cam processing is complete. |  |  |  |  |  |

#### "WarningWord" tag (output cam) (S7-1500, S7-1500T)

The "&lt;TO&gt;.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 1 "ConfigWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-1)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4... Bit 12 | - | - | - | Reserved |  |
| Bit 13 |  |  |  | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14... Bit 31 | - | - | - | Reserved |  |

### Tags of the cam track technology object (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500, S7-1500T)](#legend-s7-1500-s7-1500t-2)
- [Display data (cam track) (S7-1500, S7-1500T)](#display-data-cam-track-s7-1500-s7-1500t)
- ["Parameter" tag (cam track) (S7-1500, S7-1500T)](#parameter-tag-cam-track-s7-1500-s7-1500t)
- ["Interface" tag (cam track) (S7-1500, S7-1500T)](#interface-tag-cam-track-s7-1500-s7-1500t)
- ["Units" tag (cam track) (S7-1500, S7-1500T)](#units-tag-cam-track-s7-1500-s7-1500t)
- ["StatusWord" tag (cam track) (S7-1500, S7-1500T)](#statusword-tag-cam-track-s7-1500-s7-1500t)
- ["ErrorWord" tag (cam track) (S7-1500, S7-1500T)](#errorword-tag-cam-track-s7-1500-s7-1500t)
- ["ErrorDetail" tag (cam track) (S7-1500, S7-1500T)](#errordetail-tag-cam-track-s7-1500-s7-1500t)
- ["WarningWord" tag (cam track) (S7-1500, S7-1500T)](#warningword-tag-cam-track-s7-1500-s7-1500t)

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

Access to the tags is with "&lt;TO&gt;.&lt;tag name&gt;". The placeholder &lt;TO&gt; represents the name of the technology object.

#### Display data (cam track) (S7-1500, S7-1500T)

The following tags indicate the status of the cam track:

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- |
| Status | DINT | 0 … 2 | RON | 0 | "INACTIVE"  Inactive |
| 1 | "ACTIVE"  Active |  |  |  |  |
| 2 | "ACTIVE_WAITING_FOR_NEXT_CYCLE"  Active and waiting for next track |  |  |  |  |
| TrackOutput | BOOL | - | RON | FALSE | Cam track is not output. |
| TRUE | Cam track is output. |  |  |  |  |
| SingleCamState | DWORD | 16#0 … 16#FFFF_FFFF | RON | Switched on output cam (bit-masked) |  |
| 0 | Output cam is not switched on |  |  |  |  |
| 1 | Output cam is switched on |  |  |  |  |
| TrackPosition | LREAL | -1.0E12 … 1.0E12 | RON | Display of the current position within the cam track |  |
| MatchPosition | LREAL | -1.0E12 … 1.0E12 | RON | Reference position of the current cam track  During cyclic processing of the cam track, the continued reference position of the current cam track is displayed. The unique detection and output of the position is only possible when the assigned technology object is in motion. |  |

#### "Parameter" tag (cam track) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Parameter.&lt;tag name&gt;" contains the configuration of the basic parameters of the cam track technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Parameter. |  |  | TO_CamTrack_Struct_Parameter |  |  |  |  |
|  | CamTrackType |  | DINT | 0, 1 | RES | Output cam type |  |
| 0 | Distance output cam |  |  |  |  |  |  |
| 1 | Time-based output cam |  |  |  |  |  |  |
| PositionType |  | DINT | 0, 1 | RES | Position reference |  |  |
| 0 | Position setpoint |  |  |  |  |  |  |
| 1 | Actual position |  |  |  |  |  |  |
| ReferencePosition |  | LREAL | -1.0E12 … 1.0E12 | DIR | Reference position |  |  |
| CamTrackLength |  | LREAL | 0.001 … 1.0E12 | DIR | Track length |  |  |
| CamMasking |  | DWORD | 16#0 … 16#FFFF_FFFF | DIR | Bit masking of individual output cams |  |  |
| OnCompensation |  | LREAL | 0.0 … 1.0E12 | DIR | Activation time  Lead time for the switch-on edge |  |  |
| OffCompensation |  | LREAL | 0.0 … 1.0E12 | DIR | Deactivation time  Lead time for the switch-off edge |  |  |
| Hysteresis |  | LREAL | 0.0 … 1.0E12 | DIR | Hysteresis value  For output cams with reference to actual position, always enter a hysteresis value (&gt; 0.0). |  |  |
| Cam[1..32]. |  | ARRAY[1..32] OF TO_CamTrack_Struct_CamData |  |  |  |  |  |
|  | OnPosition | LREAL | 0.0 … 1.0E12 | CAL | With distance output cams and time-based output cams:  Start position |  |  |
| Offposition | LREAL | 0.0 … 1.0E12 | CAL | With distance output cams:  End position |  |  |  |
| Duration | LREAL | 0.001 … 1.0E12 | CAL | With time-based output cams:  Switch-on duration |  |  |  |
| Existent | BOOL | - | CAL | FALSE | Output cam is not used. |  |  |
| TRUE | Output cam is used. |  |  |  |  |  |  |

#### "Interface" tag (cam track) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Interface.&lt;tag name&gt;" contains the configuration of the output properties for the cam track technology object.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Interface. |  | TO_CamTrack_Struct_Interface |  |  |  |  |
|  | EnableOutput | BOOL | - | RES | Output cam output at the bit specified under "&lt;TO&gt;.Interface.Address" |  |
| FALSE | No output |  |  |  |  |  |
| TRUE | Output |  |  |  |  |  |
| Address | VREF | - | RON | I/O address for digital output cam output |  |  |

#### "Units" tag (cam track) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.Units.&lt;tag name&gt;" shows the set technological units.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_CamTrack_Struct_Units |  |  |  |  |
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
| TimeUnit | UDINT | - | RON | Unit for time |  |  |
| 1056 | ms |  |  |  |  |  |
| <sup>1)</sup> Position values with higher resolution or six decimal places. |  |  |  |  |  |  |

---

**See also**

[Units of measure (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#units-of-measure-s7-1500-s7-1500t)

#### "StatusWord" tag (cam track) (S7-1500, S7-1500T)

The "&lt;TO&gt;.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 2 "RestartActive") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | "Control"  The technology object is in operation. |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is being reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "OutputInverted"  The output cam output is inverted. |  |
| Bit 5 | - | - | - | "CommunicationOK"  The communication between cam track and output module is established. |  |
| Bit 6... Bit 31 | - | - | - | Reserved |  |

#### "ErrorWord" tag (cam track) (S7-1500, S7-1500T)

The "&lt;TO&gt;.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Command cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4... Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralError"  Error accessing a logical address |  |
| Bit 14... Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (cam track) (S7-1500, S7-1500T)

The tag structure "&lt;TO&gt;.ErrorDetail.&lt;tag name&gt;" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t-2)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 6 | RON | Effective alarm response |  |  |
| 0 | No reaction |  |  |  |  |  |
| 6 | Cam track processing is complete. |  |  |  |  |  |

#### "WarningWord" tag (cam track) (S7-1500, S7-1500T)

The "&lt;TO&gt;.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 1 "ConfigWarning") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemWarning"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigWarning"  Configuration error  One or several configuration parameters are adjusted internally. |  |
| Bit 2 | - | - | - | "UserWarning"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Command cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4... Bit 12 | - | - | - | Reserved |  |
| Bit 13 | - | - | - | "PeripheralWarning"  Error accessing a logical address |  |
| Bit 14... Bit 31 | - | - | - | Reserved |  |
