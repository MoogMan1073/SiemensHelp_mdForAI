---
title: "Using ET 200S 1STEP 5V (S7-300, S7-400)"
package: TFHWC1STEPenUS
topics: 43
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using ET 200S 1STEP 5V (S7-300, S7-400)

This section contains information on the following topics:

- [Terminal assignment of the 1STEP 5V (S7-300, S7-400)](#terminal-assignment-of-the-1step-5v-s7-300-s7-400)
- [Fundamentals of positioning with stepper motor (S7-300, S7-400)](#fundamentals-of-positioning-with-stepper-motor-s7-300-s7-400)
- [Functions of 1STEP 5V (S7-300, S7-400)](#functions-of-1step-5v-s7-300-s7-400)
- [1STEP 5V configuration and parameter assignment (S7-300, S7-400)](#1step-5v-configuration-and-parameter-assignment-s7-300-s7-400)
- [1STEP 5V diagnostics (S7-300, S7-400)](#1step-5v-diagnostics-s7-300-s7-400)

## Terminal assignment of the 1STEP 5V (S7-300, S7-400)

### Wiring rules

The cables (terminals 1 and 5 and terminals 4 and 8) to the power unit must be shielded, twisted-pair cables. The shield must be supported at both ends. To do this, use the shield contact (see the appendix of the [ET 200S Distributed I/O System](http://support.automation.siemens.com/WW/view/en/1144348) operating instructions).

### Terminal Assignment

The following table shows the terminal assignment of 1STEP 5V.

| View | Terminal Assignment | Remarks |
| --- | --- | --- |
| ![Terminal Assignment](images/23328711947_DV_resource.Stream@PNG-en-US.png) |  | 24 V DC: Load voltage  DI0: external enable pulse, external STOP or limit switch in forward/reverse direction   DI1: Reference switch or reference switch and limit switch in forward/reverse direction  P, /P and D, /D are signals to RS 422. |
| ![Terminal Assignment](images/23328745611_DV_resource.Stream@PNG-en-US.png) |  | 24 V DC: Load voltage  DI0: external enable pulse, external STOP or limit switch in forward/reverse direction   DI1: Reference switch or reference switch and limit switch in forward/reverse direction  P, /P and D, /D are signals to RS 422. |

## Fundamentals of positioning with stepper motor (S7-300, S7-400)

This section contains information on the following topics:

- [Interaction of components (S7-300, S7-400)](#interaction-of-components-s7-300-s7-400)
- [Parameters and Settings (S7-300, S7-400)](#parameters-and-settings-s7-300-s7-400)
- [Traversal curve of the 1STEP 5V (S7-300, S7-400)](#traversal-curve-of-the-1step-5v-s7-300-s7-400)
- [Setting the Base Frequency (S7-300, S7-400)](#setting-the-base-frequency-s7-300-s7-400)

### Interaction of components (S7-300, S7-400)

Below is a description of how individual components for positioning with stepping motor affect each other.

#### 1STEP 5V

The 1STEP 5V generates pulses and a directional signal for the power units of stepping motors. The number of pulses emitted determines the distance traversed. The pulse frequency determines the velocity. The change in the pulse frequency per time unit (second) is a measure for the acceleration or deceleration. 1STEP 5V is influenced by its parameters and settings.

#### Power unit for stepping motors

The power unit is the link between the 1STEP 5V and the stepping motor. The 1STEP 5V sends RS 422 differential signals for frequency and direction. These signals are converted in the power unit into motor currents that control the movements of the motor with a very high degree of precision.

#### Stepping motors

Stepping motors are used to position axes. They represent the simple and cost-effective solution for precision positioning jobs in wide performance ranges.

A stepping motor shaft turns by a certain angle with every pulse. During rapid pulse sequences, this stepping movement becomes a continuous turning motion.

### Parameters and Settings (S7-300, S7-400)

#### Required Information

To ensure optimum interplay between the individual components, you must provide the 1STEP 5V with information:

- **One time: during parameter configuration using your configuration software**

  - [Base frequency](#setting-the-base-frequency-s7-300-s7-400) F<sub>b </sub>
  - [Multiplier n](#traversal-curve-of-the-1step-5v-s7-300-s7-400) for setting the start-stop frequency F<sub>ss </sub>
  - [Multiplier i](#traversal-curve-of-the-1step-5v-s7-300-s7-400) for setting the acceleration / delay
  - Function and behavior of the [digital inputs](#behavior-of-the-digital-inputs-s7-300-s7-400)
  - [Traversing range](#axis-type-and-traversing-range-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)
- **In operation: movement of the motor by means of a traversing job in your user program**

  - [Multiplier G](#traversal-curve-of-the-1step-5v-s7-300-s7-400) for the velocity/output frequency F<sub>a </sub>
  - [Reduction factor R](#setting-the-base-frequency-s7-300-s7-400)
  - Distance, position or frequency
  - Operating mode
  - Direction specification (traversing job) to the start
- **In operation: to adjust to different load conditions as a parameter assignment request in your user program**

  - [Base frequency](#setting-the-base-frequency-s7-300-s7-400) F<sub>b </sub>
  - [Multiplier n](#traversal-curve-of-the-1step-5v-s7-300-s7-400) for setting the start-stop frequency F<sub>ss </sub>
  - [Multiplier i](#traversal-curve-of-the-1step-5v-s7-300-s7-400) for setting the acceleration / delay

### Traversal curve of the 1STEP 5V (S7-300, S7-400)

#### Traversal curve

An incremental mode is carried out by the 1STEP 5V in accordance with the following traversal curve. The 1STEP 5V forms the fundamental parameters (start-stop frequency, output frequency, and acceleration/delay) of the traversal curve with a [base frequency](#setting-the-base-frequency-s7-300-s7-400) that you select.

![Traversal curve](images/23363452299_DV_resource.Stream@PNG-en-US.png)

#### Start-Stop Frequency F<sub>ss</sub>

The start-stop frequency F<sub>ss</sub> is the frequency to which the motor can be accelerated under load from a standstill.

The size of F<sub>ss</sub> depends on the load inertia. The best way to work out the load inertia is by trial and error.

The start-stop frequency F<sub>ss</sub> is simultaneously the minimum output frequency F<sub>a</sub> needed to move the stepping motor.

#### Setting the Start-Stop Frequency F<sub>ss</sub>

Through parameter assignment, the 1STEP 5V permits the start-stop frequency F<sub>ss</sub> to be set in steps. To do so, select the multiplier n between 1 and 255, which is multiplied with the base frequency F<sub>b</sub>. You can lower the start-stop frequency F<sub>ss</sub> again with the reduction factor R (1 or 0.1) in the traversing job.

The start-stop frequency is calculated according to equation:

F<sub>ss</sub> = F<sub>b</sub> × n × R

Additional information is available in the following [table](#setting-the-base-frequency-s7-300-s7-400) with the ranges for start-stop frequency, starting frequency and acceleration.

#### Maximum frequency / velocity of the Axis F<sub>max</sub>

When you choose a stepping motor, remember the following:

The maximum frequency/velocity is determined by your application. At this frequency, the motor must reach a torque high enough to move its load.

Note this does not mean the highest possible frequency that the motor or the power unit can tolerate.

You can work out the maximum frequency F<sub>max</sub> with the corresponding characteristic curve. The following figure shows the torque characteristic curve of a stepping motor.

![Maximum frequency / velocity of the Axis Fmax](images/23363507595_DV_resource.Stream@PNG-en-US.png)

#### Output frequency / velocity F<sub>a</sub>

The output frequency can be set differently for each run.

When selecting the output frequency, also observe the minimum pulse duration of your power unit (see [Formula and table](#setting-the-base-frequency-s7-300-s7-400) with the ranges for start-stop frequency, output frequency and acceleration).

If the selected output frequency is lower than the set start-stop frequency F<sub>ss</sub>, the 1STEP 5V output frequency is set to the start-stop frequency F<sub>ss</sub>.

F<sub>a</sub> must always be smaller than F<sub>max</sub>.

#### Setting of the output frequency / Velocity F<sub>a</sub>

The 1STEP 5V permits the output frequency F<sub>a</sub> to be set in steps. To do so, select the multiplier G between 1 and 255, which is multiplied with the base frequency F<sub>b</sub>. You can lower the output frequency F<sub>a</sub> again with the reduction factor R (1 or 0.1) in the traversing job.

The output frequency is calculated according to the equation:

F<sub>a</sub> = F<sub>b</sub> × G × R

Additional information is available in the following [table](#setting-the-base-frequency-s7-300-s7-400) with the ranges for start-stop frequency, starting frequency and acceleration.

#### Acceleration / delay a

The maximum permitted acceleration / delay depends on the load to be moved.

The motor must reach a torque high enough to accelerate or delay the load without loss of step.

Depending on the application, you must also take into account additional criteria for setting the acceleration/delay, such as smooth starting and stopping.

#### Setting the acceleration / delay a

Through parameter assignment, the 1STEP 5V permits the acceleration / delay to be set in steps by means of the multiplier i.

During the acceleration phase, the frequency is increased continuously starting from the start-stop frequency F<sub>ss</sub> until the output frequency F<sub>a</sub> has been reached.

The time interval for the continuous increase in frequency can be set in steps. To do so you select a multiplier i between 1 and 255.

In the delay phase, the output frequency is reduced in the same way.

You can lower the acceleration / delay a again with the reduction factor R (1 or 0.1) in the traversing job.

The acceleration / deceleration is calculated according to the equation:

a = F<sub>b</sub> × R / (i × 0.128 ms)

Additional information is available in the following [table](#setting-the-base-frequency-s7-300-s7-400) with the ranges for start-stop frequency, starting frequency and acceleration.

### Setting the Base Frequency (S7-300, S7-400)

#### Introduction

Through parameter assignment, the 1STEP 5V permits the base frequency to be set in steps.

The base frequency sets the range for the start-stop frequency, the output frequency, and the acceleration.

#### Procedure

1. Depending on the priority of your requirements select a suitable range either of the start-stop frequency F<sub>ss</sub> and of the starting frequency F<sub>a</sub> or of the acceleration a from the following table in accordance with the following criteria:

   - Range for the start-stop frequency F<sub>ss</sub>,  
      for example, for starting and stopping as soon as possible
   - Range for the output frequency F<sub>a</sub>,   
     for example, for a velocity setting that is as precise as possible
   - Range for the acceleration a,   
     for example, for the fastest possible positioning operations
2. Use the table to determine the base frequency F<sub>b</sub>.

   **To optimize the base frequency F**
   <sub>b</sub>
   **, proceed as follows:**
3. Check whether the other corresponding values meet your requirements. If necessary, select another base frequency F<sub>b</sub>, which meets your requirements better.
4. Define the multipliers required to set the output frequency F<sub>a</sub>, the acceleration/delay a, and the start-stop frequency F<sub>ss</sub>.
5. Determine the corresponding reduction factor R from the table.

The following table shows the ranges for the start-stop frequency, output frequency, and acceleration.

| Base frequency F<sub>b:</sub>  in Hz | Reduction factor R | Range  Start-stop frequency F<sub>ss</sub> Starting frequency F<sub>a </sub>in Hz | Range  Acceleration a in Hz/ms |
| --- | --- | --- | --- |
| Equation:  F<sub>ss</sub> = F<sub>b</sub> × n × R F<sub>a</sub> = F<sub>b</sub> × G × R | Equation:  a = F<sub>b</sub> × R / (i × 0.128 ms) |  |  |
| 4 | 0,1 | 0,4 … 102 | 0,01 … 3,13 |
| 8 | 0,1 | 0,8 … 204 | 0,02 … 6,25 |
| 20 | 0,1 | 2 … 510 | 0,06 … 15,6 |
| 4 | 1 | 4 … 1020 | 0,12 … 31,3 |
| 8 | 1 | 8 … 2040 | 0,25 … 62,5 |
| 20 | 1 | 20 … 5100 | 0,61 … 156 |
| 40 | 1 | 40 … 10200 | 1,23 … 313 |
| 80 | 1 | 80 … 20400 | 2,45 … 625 |
| 200 | 1 | 200 … 51000 | 6,13 … 1563 |
| 400 | 1 | 400 … 102000 | 12,25 … 3125 |
| 800 | 1 | 800 … 204000 | 24,51 … 6250 |
| 2000 <sup>1)</sup> | 1 | 2000 … 510000 | 61,27 … 15625 |
| F<sub>b</sub> = Base frequency  F<sub>ss</sub> = Start-Stop frequency  F<sub>a</sub> = Output frequency  a = Acceleration / delay  R = Reduction factor  n = Multiplier for setting the start-stop frequency in steps  G = Multiplier for setting the output frequency in steps  i = Multiplier for setting the acceleration / delay in steps |  |  |  |
| <sup>1)</sup> as of 6ES7138-4DD01-0AB0 |  |  |  |

The minimum pulse duration results from the set starting frequency F<sub>a</sub> and is calculated using the equation T<sub>Pulse</sub> = 1 / (2 × F<sub>a</sub>).

## Functions of 1STEP 5V (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of functions (S7-300, S7-400)](#overview-of-functions-s7-300-s7-400)
- [Starting a traversing job (S7-300, S7-400)](#starting-a-traversing-job-s7-300-s7-400)
- [Search for Reference (S7-300, S7-400)](#search-for-reference-s7-300-s7-400)
- [Sequence of Execution of the Search for Reference (S7-300, S7-400)](#sequence-of-execution-of-the-search-for-reference-s7-300-s7-400)
- [Set reference point (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)](#set-reference-point-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)
- [Relative incremental mode (relative positioning) (S7-300, S7-400)](#relative-incremental-mode-relative-positioning-s7-300-s7-400)
- [Absolute incremental approach (absolute positioning) (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)](#absolute-incremental-approach-absolute-positioning-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)
- [Speed mode (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)](#speed-mode-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)
- [Hold traversing job (S7-300, S7-400)](#hold-traversing-job-s7-300-s7-400)
- [Axis type and traversing range (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)](#axis-type-and-traversing-range-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)
- [Pulse Enable (S7-300, S7-400)](#pulse-enable-s7-300-s7-400)
- [Changing Parameters during Operation (S7-300, S7-400)](#changing-parameters-during-operation-s7-300-s7-400)
- [Behavior of the Digital Inputs (S7-300, S7-400)](#behavior-of-the-digital-inputs-s7-300-s7-400)
- [Reaction to CPU/Master STOP (S7-300, S7-400)](#reaction-to-cpumaster-stop-s7-300-s7-400)
- [Behavior of the digital inputs (-4DC00-) (S7-300, S7-400)](#behavior-of-the-digital-inputs--4dc00--s7-300-s7-400)
- [Pulse enable (-4DC00-) (S7-300, S7-400)](#pulse-enable--4dc00--s7-300-s7-400)

### Overview of functions (S7-300, S7-400)

#### Overview

The job of the 1STEP 5V is to position a drive on certain predefined targets (incremental modes) and to travel continuously with specifiable frequencies (speed-control mode).

The following functions are available to you to this purpose:

- [Reference point approach](#search-for-reference-s7-300-s7-400): The axis is synchronized to a reference point
- [Set reference point](#set-reference-point-as-of-6es7138-4dc01-0ab0-s7-300-s7-400) (as of 6ES7138‑4DC01‑0AB0): A value is assigned to the current position.
- [Relative incremental approach](#relative-incremental-mode-relative-positioning-s7-300-s7-400) (relative positioning): The axis is moved by a predefined distance.
- [Absolute incremental approach](#absolute-incremental-approach-absolute-positioning-as-of-6es7138-4dc01-0ab0-s7-300-s7-400) (absolute positioning) (as of 6ES7138‑4DC01‑0AB0): The axis is traveled to a predefined position.
- [Speed mode](#speed-mode-as-of-6es7138-4dc01-0ab0-s7-300-s7-400) (as of 6ES7138‑4DC01‑0AB0): The drive is moved with a speed that can be specified flexibly (pulse frequency).
- [Hold traversing job](#hold-traversing-job-s7-300-s7-400)
- [Changing Parameters during Operation](#changing-parameters-during-operation-s7-300-s7-400)

The description of the [control interface](#control-interface-of-1step-5v-s7-300-s7-400) provides information about how to control the functions.

### Starting a traversing job (S7-300, S7-400)

#### Starting the traversing job

The figure below shows the process from start request for a traversing job up to the end of the traversing.

![Starting the traversing job](images/23564217867_DV_resource.Stream@PNG-en-US.png)

#### Evaluating the ERR_JOB error bit

As soon as the [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400)STS_JOB is cleared at time stamp 4, evaluate the ERR_JOB error bit. Note that the feedback bit STS_JOB is only cleared if the [control bits](#control-interface-of-1step-5v-s7-300-s7-400)DIR_P, DIR_M and C_PAR are cleared.

### Search for Reference (S7-300, S7-400)

#### Description of the function

The home position marks the point of reference of your drive system (reference cam) for the following traversing jobs. You can determine the home position by, for example, installing an initiator on the reference cam and connecting it to the DI1 digital input.

The 1STEP 5V ensures the reference point can be reproduced accurately in that it is always approached from the same direction. You can specify this direction by always starting the search for reference in the same direction.

#### Traversing job for reference point approach

The traversing job contains the following information:

- Multiplier G for the velocity/output frequency F<sub>a</sub>
- Reduction factor R for the assigned parameters base frequency F<sub>b</sub>
- Reference point position
- Mode = 1 for reference point approach
- [Stop at the reference cam](#hold-traversing-job-s7-300-s7-400)
- [Direction specification as start](#control-interface-of-1step-5v-s7-300-s7-400)

> **Note**
>
> The 1STEP 5V checks the set position for limits (minimum 0 and maximum 16777215). The full-scale value can be configured.

> **Note**
>
> If you have configured the [behavior of the digital input](#behavior-of-the-digital-inputs-s7-300-s7-400) DI1 (7) as a "Reference switch and limit switch", the 1STEP 5V automatically selects the starting direction toward the limit switch, irrespective of the direction specified in the traversing job.

> **Note**
>
> **Status of the limit switch**
>
> When you use limit switches it is possible that these may not supply the correct status at the start of the reference point approach. Such cases can occur, for example, if the limit switches are configured as normally closed contacts (active at 0-level) and the power supply of the limit switches was not yet available before the start of the reference point approach.
>
> This can lead to the reference point approach starting in the wrong direction.
>
> Make sure that each of the limit switches returns the correct status before you start an approach.

#### Status bit SYNC

The [status bit](#feedback-interface-of-1step-5v-s7-300-s7-400) SYNC informs you that the axis has been synchronized, that is, after the correct homing procedure, this status bit is set and deleted during the run.

The SYNC status bit is deleted

- After parameter assignment of your ET 200S station
- After deletion of the pulse enable
- After a CPU/Master STOP

In these cases it is advisable to carry out a search for reference.

#### POS and POS_RCD status bits

While reference point approach is active, it is indicated by the set [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400) POS.

On completion of a reference point approach, the set POS_RCD feedback bit indicates that the position has been reached.

If the reference point approach is interrupted, the POS_RCD feedback bit remains reset.

#### Residual distance, position, frequency

The [residual distance reported](#feedback-interface-of-1step-5v-s7-300-s7-400) is irrelevant during the reference point approach.

> **Note**
>
> In order for the 1STEP 5V to approach the home position with repeated precision, the period duration of the start-stop frequency has to be greater than the runtime of a single step from the 1STEP 5V to the stepping motor and via the reference cam back to 1STEP 5V (input delay of digital inputs: 4 ms).
>
> When stopping at the reference cam or at one of the limit switches during the acceleration phase, the 1STEP 5V continues to send pulses for a maximum of 50 ms at the frequency already reached before it starts braking. This avoids abrupt changes in frequency, which can lead to step losses.

### Sequence of Execution of the Search for Reference (S7-300, S7-400)

#### Steps of the Search for Reference

A search for reference consists of a maximum of three sections.

In the **first section** (1) and **second section** (2), the system ensures that the reference cam is found.

Both these sections are traversed at the defined output frequency F<sub>a</sub>.

In the **third section** (3), the reference cam is approached with start-stop frequency F<sub>ss</sub> in the selected direction up to the reference point ![Steps of the Search for Reference](images/23377807243_DV_resource.Stream@PNG-de-DE.png) with reproducible accuracy.

> **Note**
>
> The maximum number of output pulses of a section is the configured length of the traversing range minus 1.

#### Different Execution Sequences

Depending on the position ![Different Execution Sequences](images/23377823115_DV_resource.Stream@PNG-de-DE.png) at the start of the reference point approach, there are different execution patterns for the run (REF is the reference cam, which is wired to the DI1 digital input). The illustration applies to the forward starting direction (DIR_P).

- **Start before** 
  **REF**
   **or at limit switch LIMIT_M**

The figure below shows a reference point approach with start before the REF.

![Different Execution Sequences](images/23376404491_DV_resource.Stream@PNG-de-DE.png)

- **Start after the** 
  **REF**

The figure below shows a reference point approach with start after the REF.

![Different Execution Sequences](images/23377708939_DV_resource.Stream@PNG-de-DE.png)

- **Start on the** 
  **REF**

The figure below shows a reference point approach with start on the REF.

![Different Execution Sequences](images/23377720587_DV_resource.Stream@PNG-de-DE.png)

- **Start at the limit switch in start direction**

The figure below shows a reference point approach with start on the limit switch in start direction.

![Different Execution Sequences](images/23377732235_DV_resource.Stream@PNG-de-DE.png)

#### Reference switch is simultaneously a limit switch

> **Note**
>
> When the reference switch REF is simultaneously a limit switch, the 1STEP 5V automatically chooses the starting direction toward the limit switch, regardless of the direction specified in the traversing job.

- **Start within the traversing range**

The figure below shows a reference point approach with start within the traversing range, in which REF is simultaneously the limit switch LIMIT_M.

![Reference switch is simultaneously a limit switch](images/89820318091_DV_resource.Stream@PNG-de-DE.png)

- **Start on the limit switch**

The figure below shows a reference point approach with start on the limit switch LIMIT_P, in which REF is simultaneously LIMIT_P.

![Reference switch is simultaneously a limit switch](images/89820321803_DV_resource.Stream@PNG-de-DE.png)

#### Response to defective reference cam with limit switch (interruption of traversing)

The figure below shows a reference point approach with defective reference cam and start before the REF.

![Response to defective reference cam with limit switch (interruption of traversing)](images/23377756683_DV_resource.Stream@PNG-en-US.png)

The figure below shows a reference point approach with defective reference cam and start on the LIMIT_P.

![Response to defective reference cam with limit switch (interruption of traversing)](images/24575858955_DV_resource.Stream@PNG-en-US.png)

#### Behavior in the case of a constantly set reference cam without limit switch

At the end of the first section, after 16777215 pulses have been output, traversing is terminated with cleared SYNC and POS_RCD status bits.

#### Response to failure of the reference cam without limit switch

All three sections of traversing are executed, each with output of 16777215 pulses. Afterwards, the search is interrupted with cleared SYNC and POS_RCD status bits.

### Set reference point (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)

#### Description of functions

The home position marks the reference point of your drive system which the subsequent absolute incremental modes and the position value in the feedback interface reference. You define the home position by specifying the absolute position value for the current position of the stepping motor.

#### Job for setting the home position

A job for setting the home position is a virtual job without traversing movement. It contains the following information:

- Position of the home position
- Mode = 4 for setting home position
- Any [direction specification as start](#control-interface-of-1step-5v-s7-300-s7-400)

> **Note**
>
> The 1STEP 5V checks the set position for limits (minimum 0 and maximum 16777215). The full-scale value can be configured.

> **Note**
>
> Because you can set the reference point within the traversing range to values from 0 to 16777215, situations are possible in which a limit switch is no longer reachable.
>
> Examples:
>
> - If you set the reference point within the traversing range to "0", the limit switch in backward direction is no longer reachable by a traversing job, because you cannot approach negative positions.  
>   Ensure that all positions to be approached are in the positive value range.
> - In non-synchronized state, the axis cannot traverse a distance that is greater than the configured traversing range. If the configured traversing range is less than the distance between the two limit switches and the axis is at the limit switch in the forward direction, the axis cannot transverse to the limit switch in the backward direction with a relative approach.

#### Feedback messages

After correct execution of the job, the [feedback bits](#feedback-interface-of-1step-5v-s7-300-s7-400) SYNC and POS_RCD are set.

If the feedback bit SYNC is already set prior to the execution of the job, it remains set. You can also recognize the correct execution from the change of the position value in the feedback interface.

### Relative incremental mode (relative positioning) (S7-300, S7-400)

#### Description of functions

You can use the relative incremental mode to move the stepping motor a defined distance and thus approach a specified position.

You can determine the direction of traversing and the velocity at the start.

#### Traversing job for relative incremental mode

The traversing job contains the following information:

- Distance (number of pulses to be emitted)
- Multiplier G for the velocity/output frequency F<sub>a</sub>
- Reduction factor R for the assigned parameters base frequency F<sub>b</sub>
- Mode = 0 for incremental mode, relative
- [Stop at the reference cam](#hold-traversing-job-s7-300-s7-400)
- [Direction specification as start](#control-interface-of-1step-5v-s7-300-s7-400)

> **Note**
>
> The 1STEP 5V checks the specified distance for limits (minimum 1 and maximum 16777215 pulses). The distance to the limit switch is not checked by the 1STEP 5V. Traversing is stopped at the latest when the limit switch is reached.

#### Feedback messages

The [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400)POS_RCD is reset at the beginning of incremental mode.

While the incremental mode is active, it is indicated by the set POS feedback bit.

After incremental mode has been correctly executed, the set POS_RCD feedback bit indicates that the position has been reached.

If the incremental mode is interrupted, the POS_RCD feedback bit remains reset. After incremental mode has been stopped, the distance still to be traversed is displayed if the [feedback value](#feedback-interface-of-1step-5v-s7-300-s7-400) is set to "Residual distance".

### Absolute incremental approach (absolute positioning) (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)

#### Description of functions

You can use the absolute mode to move the stepping motor to a defined position and thus approach a specified position.

The velocity is specified at the start. The direction and the distance of traversing are determined automatically by the 1STEP 5V on the basis of the starting position (actual position value). You can also specify the direction for a modulo axis.

> **Note**
>
> If you set Forward start and Backward start (DIR_P and DIR_M) simultaneously at a modulo axis, the 1STEP 5V then automatically selects the [shortest distance to reach](#axis-type-and-traversing-range-as-of-6es7138-4dc01-0ab0-s7-300-s7-400) the target position.

#### Traversing job for absolute incremental mode

The traversing job contains the following information:

- Target position
- Multiplier G for the velocity/output frequency F<sub>a</sub>
- Reduction factor R for the assigned parameters base frequency F<sub>b</sub>
- Mode = 2 for incremental mode
- Any [direction specification as start](#control-interface-of-1step-5v-s7-300-s7-400)

> **Note**
>
> The 1STEP 5V checks the set position for limits (minimum 0 and maximum 16777215). The full-scale value can be configured.
>
> The traversing job is only executed if you have determined or specified the position of the home position beforehand (the SYNC bit has to be set, see "[Reference point approach](#search-for-reference-s7-300-s7-400)" or "[Set reference point](#set-reference-point-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)").
>
> The [control signal](#control-interface-of-1step-5v-s7-300-s7-400) "Stop at reference cam" is not taken into consideration.

#### Feedback messages

The [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400)POS_RCD is reset at the beginning of incremental mode.

While the incremental mode is active, it is indicated by the set POS feedback bit.

After incremental mode has been correctly executed, the set POS_RCD feedback bit indicates that the position has been reached.

If the incremental mode is interrupted, the POS_RCD feedback bit remains reset. After incremental mode has been stopped, the distance still to be traversed is displayed if the [feedback value](#feedback-interface-of-1step-5v-s7-300-s7-400) is set to "Residual distance".

### Speed mode (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)

#### Description of functions

In this operating mode you specify the frequency with which the pulses (steps) are output. When you change the frequency, the pulses are output with the new frequency after an acceleration or deceleration phase. The output is carried out continuously until you stop the traversing job or a traversing range is reached at a linear axis.

The figure below shows the speed-control mode with a modulo axis.

![Description of functions](images/81650477067_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Specification for setpoint frequency |
| ② | Start of the speed-control mode with frequency F<sub>SS</sub>, acceleration ramp up to the setpoint frequency |
| ③ | New setpoint frequency (&lt; F<sub>SS</sub>) |
| ④ | Deceleration ramp up to F<sub>SS</sub>, then stop of pulse output (no stop of speed-control mode) |
| ⑤ | Specification for setpoint frequency: Continuation of speed-control mode with F<sub>SS</sub>, acceleration ramp up to the setpoint frequency |
| ⑥ | Specification for invalid setpoint frequency: Stop of speed-control mode |
| ⑦ | Start of the speed-control mode with frequency F<sub>SS</sub>, acceleration ramp up to the setpoint frequency |
| ⑧ | Specification for setpoint frequency |
| ⑨ | Specification for setpoint frequency: Change from acceleration ramp to deceleration ramp |
| ⑩ | Specification for setpoint frequency: Continuation of the deceleration ramp |
| ⑪ | Specification for setpoint frequency |
| ⑫ | Specification for negative setpoint frequency: Direction change |

#### Traversing job for speed-control mode

The traversing job contains the following information:

- Setpoint frequency as 32-bit value (STEP 7 data type REAL)
- Direction specification by the sign of the setpoint frequency (positive: forward)
- Mode = 3 for speed-control mode
- Any [direction specification as start](#control-interface-of-1step-5v-s7-300-s7-400)

> **Note**
>
> The 1STEP 5V checks the set position for limits (minimum -510,0 kHz and maximum +510,0 kHz).
>
> The specified frequency is approached with the configured acceleration a under consideration of the start-stop frequency F<sub>ss</sub>. No pulse output is emitted at frequencies that are less than F<sub>ss</sub>.
>
> The continuous output of the frequency is terminated at the following events:
>
> - Reaching of the limits of the configured traversing range (0 in the direction backward) unless a modulo axis is configured
> - Other [aborting conditions for traversing jobs](#hold-traversing-job-s7-300-s7-400)

#### Feedback messages

While the traversing job is active, it is indicated by the set [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400) POS.

When a new frequency is specified, the POS_RCD feedback bit is cleared. When the new frequency has been reached after the acceleration or deceleration phase, POS_RCD is set again.

The current frequency is displayed in the feedback interface as a 32-bit value (STEP 7 data type REAL) if the [feedback value](#feedback-interface-of-1step-5v-s7-300-s7-400) is set to "Frequency".

> **Note**
>
> If a traversing job is being executed with a frequency of 0.0 Hz, the job is stopped if a frequency is unequal to 0.0 Hz and the STOP control bit requests the job stop. The status of the feedback bit POS_RCD is then undefined.

### Hold traversing job (S7-300, S7-400)

#### Specific holding of the traversing job

| - Caused by | Displayed by Feedback Bit |
| --- | --- |
| STOP by control bit | - |
| External STOP at digital input | STOP_EXT |
| Limit switch in the forward direction reached (LIMIT_P or digital input) | STOP_LIMIT_P |
| Limit switch in the backward direction reached (LIMIT_M or digital input) | STOP_LIMIT_M |
| STOP at the reference cam | STOP_REF |

> **Note**
>
> Remember that the limit switches are used in the reference point approach mode also to search for the reference cam.
>
> If a traversing job to LIMIT_P was stopped, then you can move the axis away from the limit switch using a new traversing job with DIR_M. When stopping at LIMIT_M, you can move the axis away from the limit switch with DIR_P.

#### Stop at the reference cam

If the "Hold at reference cam" function is selected (the control bit STOP_REF_EN is set) at the start of traversing and the reference cam is detected during traversing, the stepping motor is halted and traversing is terminated.

#### Holding the traversing job in exceptional circumstances

In the following cases the traversing job is halted with loss of the synchronization:

- Incorrect operation in the control interface during an active traversing job
- External error ERR_24V through overload of the encoder supply (e.g. short circuit)
- CPU/Master STOP
- At linear axis: Reaching of the limit of the traversing range

#### Effects

If one of the above reasons for holding the current positioning operation occurs, it is terminated by a deceleration ramp.

The return value continues to be updated even when the traversing job is halted in exceptional cases. This enables you to traverse the residual distance after holding by means of a new traversing job in the "Relative incremental mode".

#### Limit Switches and External STOP

By assigning parameters, you can choose to wire normally open or normally closed contacts for the external STOP and the limit switches.

- **Normally closed contact means:**The external STOP and the effect of the limit switches are triggered by a 0 signal. When the limit switches are reached, delete the associated control bit.
- **Normally open contact means:**The external STOP and the effect of the limit switches are triggered by a 1 signal. When the limit switches are reached, set the associated control bit.

> **Note**
>
> In case of holding during the acceleration phase the 1STEP 5V continues to send pulses for a maximum of 50 ms at the frequency already reached before it starts braking. This avoids abrupt changes in frequency, which can lead to step losses.

### Axis type and traversing range (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)

#### Overview

During configuration you specify the axis type to be controlled by the stepping motor controlled by 1STEP 5V. You have the choice of the following axis types:

- Linear axis
- Modulo axis

#### Description of the function

**Linear axis**

The traversing range of a linear axis can be set. The low limit is always 0, the high limit is configured and has a value range from 1 to 16777215.   
The traversing range can be restricted further using limit switches (operating range).

The following figure shows a linear axis.

![Description of the function](images/23381023755_DV_resource.Stream@PNG-en-US.png)

**Modulo axis**

A modulo axis is a particular form of the rotary axis. The following figure shows a modulo axis.

![Description of the function](images/23381044619_DV_resource.Stream@PNG-de-DE.png)

#### End of the modulo axis

The "Traversing range" parameter is used to specify the end of the modulo axis.

The actual position value cannot reach the traversing range value, because this highest value lies physically at the same position as the start of the modulo axis (0).

Example:

You specify the value 10000 as the traversing range, see figure above.

During a forward movement the position value jumps in the feedback interface from 9999 to 0, during a backward movement from 0 to 9999.

#### Reference point approach

If you have selected the modulo axis during the configuration and have assigned a reference cam to your drive system, you can carry out a [reference point approach](#search-for-reference-s7-300-s7-400).

Traversing is aborted unsuccessfully if the reference cam is not found after the output of a number of pulses that corresponds to the configured traversing range. The [status bits](#feedback-interface-of-1step-5v-s7-300-s7-400)SYNC and POS_RCD will then remain deleted.

#### Set home position

You may only specify values from 0 to the end of the configured end of the traversing range – 1 for the position of the home position.

#### Relative positioning

The end of the traversing range (end of the modulo axis) may be exceeded in both directions.

#### Absolute positioning

If you have selected the modulo axis during the configuration, you may only specify values from 0 to the configured end of the traversing range – 1 for the target position.

In contrast to the linear axis, specify on which path the target position is to be reached by means of the [direction specification](#control-interface-of-1step-5v-s7-300-s7-400) when the traversing job is started:

- Backward start (DIR_M): The 1STEP 5V approaches the target position in the direction of lower actual position values (Option 1 in the following figure).
- Forward start (DIR_P): The 1STEP 5V approaches the target position in the direction of higher actual position values (Option 2 in the following figure).
- Forward start and backward start simultaneously (DIR_P and DIR_M): The 1STEP 5V automatically selects the shortest path for reaching the target position (Option 1 in the following figure).

The figure below shows absolute positioning with a modulo axis.

![Absolute positioning](images/23380990091_DV_resource.Stream@PNG-en-US.png)

### Pulse Enable (S7-300, S7-400)

#### Description of the function

Pulse enable permits the output of pulses from the 1STEP 5V to the power unit. A run is not possible without pulse enable.

#### Activating Pulse Enable

You can activate pulse enable by one of the following methods:

- Through the digital input DI0 when "Function DI0" is configured as an [external enable pulse](#behavior-of-the-digital-inputs-s7-300-s7-400)

or

- Through the control bit DRV_EN when the "Function DI0" is configured as an [external STOP](#behavior-of-the-digital-inputs-s7-300-s7-400) or [limit switch forward or backward](#behavior-of-the-digital-inputs-s7-300-s7-400)

You can recognize the assigned pulse enable through the fact that

- The [LED](#diagnostics-using-the-led-display-s7-300-s7-400)RDY at the 1STEP 5V lights up in the case of correct configuration.
- The [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400)STS_DRV_EN is set.

#### Deleting the Pulse Enable

Deleting the pulse enable during a run terminates the run immediately because no more pulses are emitted to the power unit. The residual distance and actual position value are no longer valid. The synchronization of the axis by means of the reference point is lost. The SYNC feedback bit and the RDY LED are deleted.

Deleting the pulse enable when the motor is at standstill deletes the SYNC feedback bit and the RDY LED.

In this case, it may be necessary to carry out a [reference point approach](#search-for-reference-s7-300-s7-400).

### Changing Parameters during Operation (S7-300, S7-400)

#### Introduction

You can change several of the 1STEP 5V parameters during operation without having to reassign the parameters of the whole ET 200S station.

#### Parameters That Can Be Changed

The following parameters can be changed:

- Base Frequency F<sub>b:</sub>
- Multiplier n for start-stop frequency F<sub>ss</sub>
- Multiplier i for acceleration / delay
- Feedback value in the feedback interface

When you start changing parameters by means of the [control bit](#control-interface-of-1step-5v-s7-300-s7-400)C_PAR, the parameters are checked for permitted values. If you have set invalid values, the [feedback bit](#feedback-interface-of-1step-5v-s7-300-s7-400)ERR_JOB is set.

Only the feedback bits for the ERR_JOB and STS_JOB job processing are affected by the configuration job.

#### Carrying Out a Parameter Change

The following figure shows the process for a parameter change.

![Carrying Out a Parameter Change](images/23561289099_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Only one of the following control bits can be set at a particular time:
>
> DIR_Por DIR_Mor C_PAR.
>
> Otherwise, the ERR_JOB error is reported. The job error message is deleted by the start of the next job.

### Behavior of the Digital Inputs (S7-300, S7-400)

#### Introduction

You can configure the function and the behavior (active level) of the digital inputs DI0 (3) and DI1 (7) . These parameters cannot be changed using the user program.

#### Digital input DI0 (3)

You can configure the function of the digital input DI0 (3) as:

- External enable pulse
- External STOP
- Limit switch in the forward direction
- Limit switch in the backward direction

You can also configure the behavior of the digital input DI0 (3) as:

- Normally closed contact
- Normally open contact

#### Digital input DI0 (3) as an external enable pulse

The input must be [set](#pulse-enable-s7-300-s7-400) (activated) during operation. If the input is set and the configuration correct, the 1STEP 5V is ready for operation.

#### Digital input DI0 (3) as an external STOP

With this input function, you can [halt](#hold-traversing-job-s7-300-s7-400) a current traversing job using an external signal.

#### Digital input DI0 (3) as a limit switch in the forward or backward direction

With these input functions, you can limit the traversing range in the forward or backward direction through an external signal. The signal has the same effect as one of the two control bits LIMIT_P or LIMIT_M in the [control interface](#control-interface-of-1step-5v-s7-300-s7-400).

#### Digital input DI1 (7)

You can configure the function of the digital input DI1 (7) as:

- Reference switch: Reference cam
- Reference switch and limit switch in the forward direction

  This parameter selection is only possible if "Function DI0" is not configured as a "Limit switch in forward direction".
- Reference switch and limit switch in the backward direction

  This parameter selection is only possible if "Function DI0" is not configured as a "Limit switch in backward direction".

You can also configure the behavior of the digital input DI1 (7) as:

- Normally closed contact
- Normally open contact

#### Digital input DI1 (7) as a reference switch

You can wire a switch to this input for the reference cam.

You need a reference cam for the following:

- For a reference point approach
- For an incremental mode with hold on the reference cam.

#### Digital input DI1 (7) as a reference switch and limit switch in the forward or backward direction

With these input functions, you additionally limit the traversing range in the forward or backward direction through the reference cam. The signal also has the same effect as one of the two control bits LIMIT_P or LIMIT_M in the [control interface](#control-interface-of-1step-5v-s7-300-s7-400).

If you have configured the behavior of the digital input DI1 (7) as a "Reference and limit switch", then 1STEP 5V automatically selects the starting direction toward the limit switch, regardless of the direction specified in the traversing job.

### Reaction to CPU/Master STOP (S7-300, S7-400)

#### Introduction

The 1STEP 5V detects the CPU/Master STOP. It responds to it by [stopping the active traversing job](#hold-traversing-job-s7-300-s7-400).

#### Exiting the CPU/Master STOP status

| ET 200S station | 1STEP 5V |
| --- | --- |
| Without reconfiguration of the ET 200S station | - The feedback interface of the 1STEP 5V remains current. - The values changed by means of parameter assignment job are maintained. - If a control bit was set (DIR_P, DIR_M, C_PAR) when the CPU/Master STOP occurred, the bits STS_JOB and ERR_JOB are set when the CPU/Master STOP status is exited. Delete the control bit. Traversing / the parameter assignment job is not executed. You can then start a new traversing by means of the control bit. - After the delay ramp, the pulse enable, the RDY LED, and the SYNC status bit are deleted. |
| With reconfiguration of the ET 200S station | - Information on previous searches and parameter assignment jobs is reset. - If pulse enable was activated by means of the control bit DRV_EN at the time of the CPU/Master STOP, the pulse enable, the RDY LED, and the SYNC status bit are deleted after the delay ramp. |

#### Reconfiguration of the ET 200S station

Reconfiguration of the ET 200S station is carried out by your CPU/ DP master at:

- POWER ON of the CPU / DP master
- POWER ON of the IM 151 / IM 151 FO
- After failure of the DP transmission
- Upon loading changed parameters or configuration of the ET 200S station into the CPU / DP master
- When the 1STEP 5V is plugged
- Upon power on or inserting of the appropriate power module

---

**See also**

[Pulse Enable (S7-300, S7-400)](#pulse-enable-s7-300-s7-400)

### Behavior of the digital inputs (-4DC00-) (S7-300, S7-400)

#### Digital input DI 3

You can configure the function of the digital input DI 3 as:

- External enable pulse
- External STOP

You can also configure the behavior of the digital input DI 3 as:

- Normally closed contact
- Normally open contact

#### Digital input DI 3 as an external enable pulse

The input must be [set](#pulse-enable--4dc00--s7-300-s7-400) (activated) during operation. If the input is set and the configuration correct, the 1STEP 5V/204kHz is ready for operation.

#### Digital input DI 3 as an external STOP

With this input function, you can hold an active traversing job using an external signal.

#### Digital input REF

You can wire a switch to this input for the reference cam.

You need a reference cam for the following:

- For a reference point approach
- For an incremental mode with hold on the reference cam.

### Pulse enable (-4DC00-) (S7-300, S7-400)

#### Description of the function

Pulse enable permits the output of pulses from the 1STEP 5V/204kHz to the power unit. A run is not possible without pulse enable.

#### Activating Pulse Enable

You can activate pulse enable by one of the following methods:

- Through the digital input DI 3 when "Function DI" is configured as an [external enable pulse](#behavior-of-the-digital-inputs--4dc00--s7-300-s7-400)

or

- Through the control bit DRV_EN when the "Function DI" is configured as an [external STOP](#behavior-of-the-digital-inputs--4dc00--s7-300-s7-400)

You can recognize the assigned pulse enable through the fact that

- The [LED](#diagnostics-using-the-led-display-s7-300-s7-400)RDY at the 1STEP 5V/204kHz lights up in the case of correct configuration.
- The STS_DRV_EN feedback bit is set.

#### Deleting the Pulse Enable

Deleting the pulse enable during a run terminates the run immediately because no more pulses are emitted to the power unit. The stepper motor runs without pulse control. This means the residual distance is no longer valid. The synchronization of the axis by means of the reference point is lost. The SYNC feedback bit and the RDY LED are deleted.

Deleting the pulse enable when the motor is at standstill deletes the SYNC feedback bit and the RDY LED.

In this case, it may be necessary to perform a reference point approach.

## 1STEP 5V configuration and parameter assignment (S7-300, S7-400)

This section contains information on the following topics:

- [Parameters (S7-300, S7-400)](#parameters-s7-300-s7-400)
- [1STEP 5V control and feedback interface (S7-300, S7-400)](#1step-5v-control-and-feedback-interface-s7-300-s7-400)

### Parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400)
- [Selecting the base frequency (S7-300, S7-400)](#selecting-the-base-frequency-s7-300-s7-400)
- [Specifying multiplier n (S7-300, S7-400)](#specifying-multiplier-n-s7-300-s7-400)
- [Specifying time interval i (S7-300, S7-400)](#specifying-time-interval-i-s7-300-s7-400)
- [Selecting the feedback value (S7-300, S7-400)](#selecting-the-feedback-value-s7-300-s7-400)
- [Selecting the function DI0 (S7-300, S7-400)](#selecting-the-function-di0-s7-300-s7-400)
- [Selecting the function DI1 (S7-300, S7-400)](#selecting-the-function-di1-s7-300-s7-400)
- [Selecting the behavior of inputs DI0 and DI1 (S7-300, S7-400)](#selecting-the-behavior-of-inputs-di0-and-di1-s7-300-s7-400)
- [Selecting the behavior of the limit switches in the control interface (S7-300, S7-400)](#selecting-the-behavior-of-the-limit-switches-in-the-control-interface-s7-300-s7-400)
- [Enabling the modulo axis (S7-300, S7-400)](#enabling-the-modulo-axis-s7-300-s7-400)
- [Specifying the traversing range (S7-300, S7-400)](#specifying-the-traversing-range-s7-300-s7-400)

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Group diagnostics are enabled in the respective check box.

A "Short circuit encoder supply" ERR_24V or a "Parameter assignment error" ERR_PARA lead to channel-based diagnostics if group diagnostics is enabled.

#### Selecting the base frequency (S7-300, S7-400)

##### Base frequency F<sub>b:</sub>

The base frequency F<sub>b</sub> is the base value for setting the start-stop frequency, output frequency and acceleration/delay.

Select the base frequency suitable for your application.

Detailed information can be found under [Setting the base frequency](#setting-the-base-frequency-s7-300-s7-400).

#### Specifying multiplier n (S7-300, S7-400)

##### Multiplier n

With multiplier n, you can set the start-stop frequency in increments:

F<sub>ss</sub> = F<sub>b</sub> × n

Permitted range of values: 1 … 255

---

**See also**

[Setting the Base Frequency (S7-300, S7-400)](#setting-the-base-frequency-s7-300-s7-400)

#### Specifying time interval i (S7-300, S7-400)

##### Time interval i

With multiplier i, you can set the acceleration/delay in increments:

a = F<sub>b</sub> / (i × 0.128 ms)

Permitted range of values: 1 … 255

---

**See also**

[Setting the Base Frequency (S7-300, S7-400)](#setting-the-base-frequency-s7-300-s7-400)

#### Selecting the feedback value (S7-300, S7-400)

##### Feedback value

Select the feedback value that is supplied in the [feedback interface](#feedback-interface-of-1step-5v-s7-300-s7-400):

- Residual distance
- Position
- Frequency

#### Selecting the function DI0 (S7-300, S7-400)

##### Function DI0

Select which function the [digital input DI0 (3)](#behavior-of-the-digital-inputs-s7-300-s7-400) should have:

- An external enable pulse
- An external STOP
- Limit switch in the forward direction
- Limit switch in the backward direction

#### Selecting the function DI1 (S7-300, S7-400)

##### Function DI1

Select which function the [digital input DI1 (7)](#behavior-of-the-digital-inputs-s7-300-s7-400) should have:

- A reference switch (reference cam)
- Reference switch and limit switch in the forward direction

  This parameter selection is only possible if "Function DI0" is not configured as a "Limit switch forward".
- Reference switch and limit switch in the backward direction

  This parameter selection is only possible if "Function DI0" is not configured as a "Limit switch backward".

#### Selecting the behavior of inputs DI0 and DI1 (S7-300, S7-400)

##### Input DI0, input DI1

Select the behavior of digital inputs DI0 (3) and DI1 (7):

- Normally closed contact
- Normally open contact

---

**See also**

[Behavior of the Digital Inputs (S7-300, S7-400)](#behavior-of-the-digital-inputs-s7-300-s7-400)
  
[Hold traversing job (S7-300, S7-400)](#hold-traversing-job-s7-300-s7-400)

#### Selecting the behavior of the limit switches in the control interface (S7-300, S7-400)

##### Limit switches in the control interface

Select the behavior of the limit switches in the [control interface](#control-interface-of-1step-5v-s7-300-s7-400):

- Normally closed contact
- Normally open contact

---

**See also**

[Hold traversing job (S7-300, S7-400)](#hold-traversing-job-s7-300-s7-400)

#### Enabling the modulo axis (S7-300, S7-400)

##### Modulo axis

The axis type "linear axis" is preconfigured at the 1STEP 5V. If you want to control a "modulo axis", you have to enable the "Modulo axis" check box.

---

**See also**

[Axis type and traversing range (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)](#axis-type-and-traversing-range-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)

#### Specifying the traversing range (S7-300, S7-400)

##### Traversing range

The "Traversing range" parameter is used to specify the end of the modulo axis.

Permitted range of values: 1 … 16777216

---

**See also**

[Axis type and traversing range (as of 6ES7138-4DC01-0AB0) (S7-300, S7-400)](#axis-type-and-traversing-range-as-of-6es7138-4dc01-0ab0-s7-300-s7-400)

### 1STEP 5V control and feedback interface (S7-300, S7-400)

This section contains information on the following topics:

- [Control interface of 1STEP 5V (S7-300, S7-400)](#control-interface-of-1step-5v-s7-300-s7-400)
- [Feedback interface of 1STEP 5V (S7-300, S7-400)](#feedback-interface-of-1step-5v-s7-300-s7-400)

#### Control interface of 1STEP 5V (S7-300, S7-400)

> **Note**
>
> For the 1STEP 5V, the following data of the control interface are consistent:
>
> - Bytes 0 to 3
> - Bytes 4 to 7

##### Assignment of the control interface

The following table shows the assignment of the control interface (outputs) of 1STEP 5V.

| Address | Assignment |  |  |
| --- | --- | --- | --- |
| Bytes 0 to 3 | **Relative incremental mode (Byte 4 Bit 2 to Bit 0 is 0),**    **Absolute incremental mode (Byte 4 Bit 2 to Bit 0 is 2)** |  |  |
| Byte 0 | Multiplier G: F<sub>a</sub>= F<sub>b</sub> × R × G (value range 1 to 255) |  |  |
| Byte 1 | Distance or position bit 23 to bit 16 |  |  |
| Byte 2 | Distance or position bit 15 to bit 8 |  |  |
| Byte 3 | Distance or position bit 7 to bit 0 |  |  |
| **Reference point approach (Byte 4 Bit 2 to Bit 0 is 1)** |  |  |  |
| Byte 0 | Multiplier G: F<sub>a</sub> = F<sub>b</sub> × R × G (value range 1 to 255) |  |  |
| Byte 1 | Position bit 23 to bit 16 |  |  |
| Byte 2 | Position bit 15 to bit 8 |  |  |
| Byte 3 | Position bit 7 to bit 0 |  |  |
| **Set reference point approach (Byte 4 Bit 2 to Bit 0 is 4)** |  |  |  |
| Byte 0 | Reserve = 0 |  |  |
| Byte 1 | Position bit 23 to bit 16 |  |  |
| Byte 2 | Position bit 15 to bit 8 |  |  |
| Byte 3 | Position bit 7 to bit 0 |  |  |
| **Speed-control mode (Byte 4 Bit 2 to Bit 0 is 3)** |  |  |  |
| Bytes 0 to 3 | Frequency as STEP 7 data type REAL |  |  |
| **Parameter assignment request (Byte 5 Bit 6 is 1)** |  |  |  |
| Byte 0 | Reserve = 0 |  |  |
| Byte 1 | Multiplier i: a = F<sub>b</sub> × R / (i × 0.128 ms) (value range 1 to 255) |  |  |
| Byte 2 | Multiplier n: F<sub>ss</sub>=F<sub>b </sub> × n × R (value range 1 to 255) |  |  |
| Byte 3 | Base frequency F<sub>b</sub>:  - 0 = 800 Hz - 1 = 400 Hz - 2 = 200 Hz - 3 = 80 Hz - 4 = 40 Hz - 5 = 20 Hz - 6 = 8 Hz - 7 = 4 Hz - 8 = 2000 Hz |  |  |
| Byte 4 | **Traversing job** |  |  |
| Bit 7 | Reduction factor  - 0 = Factor 1.0 (no reduction) - 1 = Factor 0.1 | R |  |
| Bit 6 | Hold traversing job | STOP |  |
| Bit 5 | Backward start | DIR_M |  |
| Bit 4 | Forward start | DIR_P |  |
| Bit 3 | Firmware Version V1.0.0: Reserve = 0  Firmware-Version V1.0.1 and higher: Release of frequencies below F<sub>SS</sub> in speed-control mode | EN_LF |  |
| Bit 2 to Bit 0 | Operating mode  - 0 = Relative incremental mode (relative positioning) - 1 = Reference point approach - 2 = Absolute incremental mode (absolute positioning) - 3 = Speed-control mode - 4 = Set home position | MODE |  |
| **Parameter assignment request** |  |  |  |
| Bit 7 to Bit 0 | Value is not relevant and is ignored |  |  |
| Byte 5 | **Traversing job** |  |  |
| Bit 7 | Diagnostics error acknowledgment | EXTF_ACK |  |
| Bit 6 | Must be set to 0 | C_PAR |  |
| Bit 5 to Bit 4 | Value is not relevant and is ignored | FEEDBACK |  |
| Bit 3 | Stop at the reference cam | STOP_REF_EN |  |
| Bit 2 | Pulse enable | DRV_EN |  |
| Bit 1 | Limit switch in the forward direction | LIMIT_P |  |
| Bit 0 | Limit switch in the backward direction | LIMIT_M |  |
| **Parameter assignment request** |  |  |  |
| Bit 7 | Diagnostics error acknowledgment | EXTF_ACK |  |
| Bit 6 | Change parameter; must be set to 1 | C_PAR |  |
| Bit 5 to Bit 4 | Feedback value in the feedback interface  - 00 = Residual distance - 01 = Position - 10 = Frequency - 11 = Reserved | FEEDBACK |  |
| Bit 3 | Value is not relevant and is ignored | STOP_REF_EN |  |
| Bit 2 | Pulse enable | DRV_EN |  |
| Bit 1 | Value is not relevant and is ignored | LIMIT_P |  |
| Bit 0 | Value is not relevant and is ignored | LIMIT_M |  |
| Byte 6 | Reserve = 0 |  |  |
| Byte 7 | Reserve = 0 |  |  |

##### Notes on the Control Bits

| Bits | Explanation |
| --- | --- |
| Base frequency F<sub>b:</sub> | Coding for setting the base frequency in steps:  - 0 = 800 Hz - 1 = 400 Hz - 2 = 200 Hz - 3 = 80 Hz - 4 = 40 Hz - 5 = 20 Hz - 6 = 8 Hz - 7 = 4 Hz - 8 = 2000 Hz   You can change this parameter during operation using a [Parameter assignment request](#changing-parameters-during-operation-s7-300-s7-400) with the control bit C_PAR. |
| Operating mode | Coding for operating mode:  - 0 = Relative incremental mode (relative positioning) - 1 = Reference point approach - 2 = Absolute incremental mode (absolute positioning) - 3 = Speed-control mode - 4 = Set home position |
| C_PAR | A parameter change is requested with this bit. |
| DIR_M | This bit requests and starts a traversing job in the backward direction. |
| DIR_P | This bit requests and starts a traversing job in the forward direction. |
| DRV_EN | If you are not using the digital input DI0 (3) as an external pulse enable, this bit is interpreted as a pulse enable. If no external pulse enable is configured and DRV_EN goes to 0, the referencing (SYNC) may be lost. |
| EN_LF | In Firmware Version V1.0.1 and higher, you use this bit in speed-control mode to also permit frequencies that are less, according to amount, than the configured start-stop frequency.  If the specified frequency, according to amount, is below the start-stop frequency, it is output without an acceleration or deceleration ramp. Frequencies above the start-stop frequency are output with acceleration or deceleration ramp.  The lowest frequency, according to amount, that can be output is 0.1 Hz.   The bit is only evaluated when speed-control mode is started. A change of the bit during a traversing job in speed-control mode has no effect. |
| Limit switches LIMIT_M | This limit switch limits the travel range in the backward direction. You set or delete this bit in your user program. |
| Limit switches LIMIT_P | This limit switch limits the travel range in the forward direction. You set or delete this bit in your user program. |
| EXTF_ACK | Acknowledgment bit for diagnostic message |
| FEEDBACK | Coding for the feedback value in the feedback interface:  - 00 = Residual distance - 01 = Position - 10 = Frequency - 11 = Reserved   You can change this parameter during operation using a [Parameter assignment request](#changing-parameters-during-operation-s7-300-s7-400) with the control bit C_PAR. |
| Frequency | A 32-bit value (STEP 7 data type REAL) that contains the pulse frequency to be output. |
| Multiplier G | Factor for setting the velocity / output frequency in steps |
| Multiplier i | Factor for setting the acceleration / deceleration in steps  You can change this parameter during operation using a [Parameter assignment request](#changing-parameters-during-operation-s7-300-s7-400) with the control bit C_PAR. |
| Multiplier n | Factor for setting the start-stop frequency in steps  You can change this parameter during operation using a [Parameter assignment request](#changing-parameters-during-operation-s7-300-s7-400) with the control bit C_PAR. |
| Position | 24-bit value that contains the target position to be approached |
| Reduction factor R | The base frequency F<sub>b</sub> is multiplied by 0.1 if the bit is set. This reduces the output frequency F<sub>a</sub>, the start-stop frequency F<sub>ss</sub>, and the acceleration / deceleration a by the same amount. |
| STOP | With this bit, you can stop a traversing job with a delay ramp at any time (see also "[Stop traversing job](#hold-traversing-job-s7-300-s7-400)"). |
| STOP_REF_EN | When the bit is set, the "Stop at the reference cam" function is active. When the reference cam is recognized, the traversing job is stopped with a delay ramp (see also "[Stop traversing job](#hold-traversing-job-s7-300-s7-400)"). |
| Distance | A 24-bit value that contains (without signs) the number of pulses that have to be traversed. |

#### Feedback interface of 1STEP 5V (S7-300, S7-400)

> **Note**
>
> For the 1STEP 5V, the following data of the feedback interface are consistent:
>
> - Bytes 0 to 3
> - Bytes 4 to 7

##### Assignment of the feedback interface

The following table shows the assignment of the feedback interface (inputs) of 1STEP 5V.

| Address | Assignment |  |  |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Residual distance (bit 23 to bit 0 of 32 bits) /  Position (bit 23 to bit 0 of 32 bits) /  Frequency (32 bits, STEP 7 data type REAL) |  |  |
| Byte 4 | Bit 7 | Short-circuit at encoder supply | ERR_24V |
| Bit 6 | Reserve = 0 |  |  |
| Bit 5 | Programming error | ERR_PARA |  |
| Bit 4 | Determining the home position | SYNC |  |
| Bit 3 | Reserve = 0 |  |  |
| Bit 2 | Position reached | POS_RCD |  |
| Bit 1 | Error during job transfer | ERR_JOB |  |
| Bit 0 | Job transfer running | STS_JOB |  |
| Byte 5 | Bit 7 | Traversing job running | POS |
| Bit 6 | Limit switch forward is cause for stop | STOP_LIMIT_P |  |
| Bit 5 | Limit switch backward is cause for stop | STOP_LIMIT_M |  |
| Bit 4 | External STOP is cause for stop | STOP_EXT |  |
| Bit 3 | Reference cam is cause for stop | STOP_REF |  |
| Bit 2 | Status DI0 | STS_DI0 |  |
| Bit 1 | Status DI1 | STS_DI1 |  |
| Bit 0 | Status pulse enable active | STS_DRV_EN |  |
| Byte 6 | Error number at an error during job transfer |  |  |
| Byte 7 | Reserve = 0 |  |  |

##### Notes on the Feedback Bits

| Bits | Explanation |
| --- | --- |
| Frequency | A 32-bit value (STEP 7 data type REAL) that contains the current pulse frequency. The pulse frequency can take on positive (forward direction) and negative (backward direction) values. |
| ERR_JOB | This bit is set if the job is not clear or not possible.  The error cause is specified in more detail by the returned error number (see the following table "Error number in the feedback interface"). |
| ERR_PARA | Incorrect parameter assignment for the ET 200S station.  The error cause is specified in more detail by the returned error number (see the following table "Error number in the feedback interface").  The parameter error bit is deleted when a correct parameter assignment is transmitted. |
| ERR_24V | The encoder supply has been overloaded (e.g. by a short circuit) and is now switched off. ERR_24V is reset if it has been acknowledged with the EXTF_ACK control bit. After the overload has been eliminated, the encoder supply is switched on again and ERR_24V remains cleared. |
| Error number | Specifies the error cause if ERR_JOB or ERR_PARA is set (see table below "Error numbers in the feedback interface"). |
| POS | Traversing: This bit is set as long as the traversing job is running. |
| POS_RCD | POS_RCD is cleared at the start of an incremental mode or at specification of a new setpoint frequency in speed-control mode. POS_RCD is set after a correctly executed incremental mode or when the setpoint frequency has been reached in speed-control mode.  If traversing was interrupted (if the [traversing job has stopped](#pulse-enable-s7-300-s7-400) or the [pulse enable is deleted](#hold-traversing-job-s7-300-s7-400)), POS_RCD remains cleared. |
| Position | A 24-bit value that contains the current absolute position (without signs).  Byte 0 of the feedback interface is 0. |
| Residual distance | A 24-bit value that contains the number of pulses that still have to be traversed (without signs).  Byte 0 of the feedback interface is 0. |
| STOP_EXT | Cause for stop: This bit is set if the traversing job has been stopped by an external STOP. |
| STOP_LIMIT_M | Cause for stop: This bit is set if the traversing job has been stopped by reaching of the limit switch backward. |
| STOP_LIMIT_P | Cause for stop: This bit is set if the traversing job has been stopped by reaching of the limit switch forward. |
| STOP_REF | Cause for stop: This bit is set if the traversing job has been stopped by reaching of the reference cam. |
| STS_DI0 | The bit displays the status of the DI0 (3) digital input. |
| STS_DI1 | The bit displays the status of the DI1 (7) digital input. |
| STS_DRV_EN | This bit is set when one of the following occurs, depending on the assigned parameter function of the digital input DI0:  - The external enable pulse is set.   or  - The DRV_EN control bit is set for the pulse enable. |
| STS_JOB | This bit is set as feedback when a job request for a traversing or parameter assignment job is detected and then reset when the job has been executed. |
| SYNC | This bit is set after a correct reference point approach or after manual specification of the home position has been set.  The SYNC bit is cleared after parameter assignment with new ET 200S station parameters or after deletion of the pulse enable. |

##### Error number

If an error with the job transfer (ERR_JOB is set) or an error in the basic parameter assignment (ERR_PARA is set) is displayed in the feedback interface, the error cause is specified in more detail by means of an error number.

The table below shows the error numbers of the feedback interface.

| Error number | Meaning |
| --- | --- |
| **General error causes** |  |
| 0<sub>D</sub> | No error (then ERR_JOB or ERR_PARA is also not set) |
| 1<sub>D</sub> | Combination of the control bits (DIR_P, DIR_M, C_PAR) is invalid |
| 2<sub>D</sub> | Another job is still running. |
| **Causes of errors with a traversing job** |  |
| 16<sub>D</sub> | Start forward (DIR_P) at limit switch forward (LIMIT_P) active |
| 17<sub>D</sub> | Start backward (DIR_M) at limit switch backward (LIMIT_M) active |
| 18<sub>D</sub> | Start with set control bit STOP |
| 19<sub>D</sub> | Start at external STOP active |
| 20<sub>D</sub> | Start at a missing pulse enable (internal or external) |
| 21<sub>D</sub> | Start with set STOP_REF_EN with active reference cam |
| 22<sub>D</sub> | Start without reference (at absolute incremental mode) |
| 23<sub>D</sub> | Start with diagnostic error present |
| 24<sub>D</sub> | Start was interrupted by CPU/Master STOP |
| 25<sub>D</sub> | Start with incorrect operating mode (not identical with requirement) |
| 26<sub>D</sub> | Distance or position specification is invalid |
| 27<sub>D</sub> | Multiplier G for the velocity is zero |
| 28<sub>D</sub> | Frequency is invalid at speed-control mode |
| **Error causes at a parameter assignment job or for the basic parameter assignment** |  |
| 32<sub>D</sub> | Specification for the base frequency is invalid |
| 33<sub>D</sub> | Multiplier n for start-stop frequency is zero |
| 34<sub>D</sub> | Multiplier i for acceleration / delay is zero |
| 35<sub>D</sub> | Feedback value for the feedback interface is invalid |
| 36<sub>D</sub> | Combination of the functions of DI0 and DI1 is invalid (limit switches) |
| 37<sub>D</sub> | Specification for the end of the traversing range is invalid |

## 1STEP 5V diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Diagnostics using the LED display (S7-300, S7-400)](#diagnostics-using-the-led-display-s7-300-s7-400)
- [Error types (S7-300, S7-400)](#error-types-s7-300-s7-400)

### Diagnostics using the LED display (S7-300, S7-400)

#### LED display on the 1STEP 5V

![LED display on the 1STEP 5V](images/23329768075_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Group error (red) |
| ② | Ready for traversing job (green) |
| ③ | Positioning underway (green) |
| ④ | Status display for Digital input 0 (green) |
| ⑤ | Status display for Digital input 1 (green) |

#### Status and error displays by means of LEDs on the 1STEP 5V

The table below shows the status and error displays on the 1STEP 5V.

| Event (LED) |  |  |  |  | Cause | Remedy |
| --- | --- | --- | --- | --- | --- | --- |
| SF | RDY | POS | 3 | 7 |  |  |
| On |  |  |  |  | No configuration or incorrect module plugged in. There is a diagnostic message. | Check the parameter assignment. Evaluate the diagnostics data. |
|  | On |  |  |  | If parameters were assigned to the module correctly and pulse enable has been activated |  |
|  |  | On |  |  | When traversing job is running |  |
|  |  |  | On |  | DI 0 is activated. |  |
|  |  |  |  | On | DI 1 is activated. |  |

### Error types (S7-300, S7-400)

For information on the structure of the channel-related diagnostics, refer to the manual on the interface module used in your ET 200S station.

#### 1STEP 5V error types

The following table shows the error types on the 1STEP 5V.

| Error type |  | Meaning | Remedy |
| --- | --- | --- | --- |
| 1<sub>D</sub> | 00001:  Short circuit | Short circuit of the sensor supply. | Check the connection to the switches. Correct the process wiring. |
| 9<sub>D</sub> | 01001:  Error | Internal module error occurred. | Replace the module. |
| 16<sub>D</sub> | 10000:  Parameter assignment error | Parameters have not been assigned to the module. | Correct the parameter assignment. |
