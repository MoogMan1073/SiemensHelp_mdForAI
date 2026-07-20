---
title: "Filter_Universal (S7-1500)"
package: ProgFBPIDFUNIenUS
topics: 15
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Filter_Universal (S7-1500)

This section contains information on the following topics:

- [Compatibility with CPU and FW (S7-1500)](#compatibility-with-cpu-and-fw-s7-1500)
- [Description Filter_Universal (S7-1500)](#description-filter_universal-s7-1500)
- [Operating principle Filter_Universal (S7-1500)](#operating-principle-filter_universal-s7-1500)
- [Input parameter Filter_Universal (S7-1500)](#input-parameter-filter_universal-s7-1500)
- [Output parameter Filter_Universal (S7-1500)](#output-parameter-filter_universal-s7-1500)
- [Static tags Filter_Universal (S7-1500)](#static-tags-filter_universal-s7-1500)
- [ErrorBits parameter (S7-1500)](#errorbits-parameter-s7-1500)

## Compatibility with CPU and FW (S7-1500)

The following table shows which version of Filter_Universal can be used on which CPU:

| CPU | FW | Filter_Universal |
| --- | --- | --- |
| S7-1500-based CPUs | as of version V2.0 | V1.0 |

## Description Filter_Universal (S7-1500)

### Description

The Filter_Universal instruction is a configurable filter of the order 1 to 10.

It is used to manipulate a signal in such a way that specific frequency components of this signal are either allowed through or attenuated.

Filter_Universal can be used for the following purposes:

- High-pass filter
- Low-pass filter
- Bandpass filter
- Bandstop filter

The following filter parameters can be specified based on the corresponding tags in order to achieve the desired filter behavior:

- Type ( Type tag)
- Frequency (Frequency tag)
- Bandwidth (Bandwidth tag)
- Order (Order tag)
- Characteristic (Characteristic tag)

An extended description of the filter parameters and corresponding tags can be found in section [Filter parameters](#filter-parameters-s7-1500).

### Call

Filter_Universal requires a constant cycle time and therefore needs to be called in a cyclic interrupt OB.

In an OB or FC, Filter_Universal is called as a single-instance DB. In a function block, Filter_Universal can be called as a single-instance DB, as a multi-instance DB, and as a parameter instance DB.

When the instruction is called, no technology object is created. No parameter assignment interface or commissioning interface is available. You assign the Filter_Universal parameters directly using the instance DB and commission Filter_Universal using a watch table of the user program in the CPU or HMI.

### Startup

The tags in the static area of Filter_Universal are not retentive. These tags are initialized with the start values after each operating state transition of the CPU from STOP to RUN. If you change the actual values in online mode and these values are to be retained after the operating state transition of the CPU from STOP to RUN, back up these values in the start values of the data block.

With the tag [StartMode](#initializing-output-values-s7-1500), you can define the start behavior of the Filter_Universal instruction at the first call after the operating state transition of the CPU from STOP to RUN.

### Responses in the event of an error

If the output value cannot be correctly calculated, the Filter_Universalinstruction instead outputs a substitute output value and an error with an error message ErrorBits &gt;= 16#0002_0000. You can use the [tag ErrorMode](#errorbits-parameter-s7-1500) to define the substitute output value as follows:

| ErrorMode | Output |
| --- | --- |
| 0 | Value of the Input parameter |
| 1 | Value of the SubstituteOutput parameter |
| 2 | Last valid filter output value  0.0, if no valid filter output value exists. |
| 3 | 0.0 |

The following applies in addition for all values of the ErrorMode tag:

- If the substitute output value is not a valid REAL value, 0.0 is output as output value.
- The substitute output value is limited to the value range -3.402823e+38 .. +3.402823e+38 of the data type REAL. Only then is the substitute output value output at the Output parameter.
- The ErrorMode tag is only effective when the Reset = FALSE parameter is set. If the Reset = TRUE parameter is set, the value of the SubstituteOutput parameter or 0.0 is output at the Output parameter.

The Error parameter indicates if an error is pending. When the error is no longer pending, Error is set to FALSE. The ErrorBits parameter shows which errors have occurred. ErrorBits is retentive and is reset only by a positive edge at the Reset or ErrorAck parameter.

Filter_Universal returns to output value calculation through the filter algorithm as soon as there are no more pending errors with error messages ErrorBits ≥ 16 0002_0000. Switchover depends on the filter type:

- For high-pass and bandpass filters (Type = 1 or 2), the filter algorithm is set up as if it were in a steady state with Output = 0.0. If the Input parameter remains constant, the output value will jump to Output = 0.0. If the Input parameter changes, the output value jumps to an appropriate value.
- For low-pass and bandstop filters (Type = 0 or 3), the filter algorithm is set up as if it were in a steady state with Output = SubstituteOutput. Switchover is bumpless.

## Operating principle Filter_Universal (S7-1500)

This section contains information on the following topics:

- [Filter parameters (S7-1500)](#filter-parameters-s7-1500)
- [Initializing output values (S7-1500)](#initializing-output-values-s7-1500)
- [Final value in steady state (S7-1500)](#final-value-in-steady-state-s7-1500)
- [Use in time-critical applications (S7-1500)](#use-in-time-critical-applications-s7-1500)
- [Call environment and automatic detection of the cycle time (S7-1500)](#call-environment-and-automatic-detection-of-the-cycle-time-s7-1500)
- [Reset response (S7-1500)](#reset-response-s7-1500)
- [Enable behavior EN/ENO (S7-1500)](#enable-behavior-eneno-s7-1500)

### Filter parameters (S7-1500)

The filter parameters Type, Frequency, Bandwidth, Characteristic and Order can be specified based on the corresponding tags in order to achieve the desired filter behavior.

#### Filter type

The filter type determines the general transfer behavior for the different frequency components of the input signal. It is defined by the Type tag.

The following table shows the different filter types:

| Type | Description | Application example |
| --- | --- | --- |
| 0 | Low-pass filter:  The filter allows frequency components below the cutoff frequency through, and attenuates frequency components above the cutoff frequency. | Noise reduction at a measured input value to obtain smoother signal characteristics |
| 1 | High-pass filter: The filter allows frequency components above the cutoff frequency through, and attenuates frequency components below the cutoff frequency. | Suppression of DC or low frequency components, e.g. DC component in signal |
| 2 | Bandpass filter: The filter allows frequency components within a specific range around the center frequency through, and attenuates frequency components outside of this range. | Determination of the wanted signal with a specific frequency range from a signal that contains additional frequency components |
| 3 | Bandstop filter: The filter attenuates frequency components within a specific range around the center frequency, and allows frequency components outside of this range through. | Attenuation of interferences in a specific frequency range, e.g. interruptions due to the line frequency |

#### Frequency and bandwidth

For low-pass and high-pass filters, the cutoff frequency is determined by the Frequency tag. The cutoff frequency is the frequency at which the gain is reduced to 1/√2≈0.707≈−3dB. A sinusoidal input signal with amplitude 1.0 and a frequency equal to the cutoff frequency will result in a sinusoidal output signal with amplitude 0.707.

The ratio of output value to input value (gain) depending on the frequency can be shown in the amplitude response. The value 0 dB corresponds to a gain = 1.0.

The following figure shows the amplitude response of a low-pass filter with Frequency = 100 Hz (Order = 10, Characteristic = 2):

![Frequency and bandwidth](images/167556270987_DV_resource.Stream@PNG-de-DE.png)

Bandpass and bandstop filters have a low and a high cutoff frequency whose position is defined by the center frequency and bandwidth. The following table shows the corresponding tags that are configured for such filters:

| Tag | Description |
| --- | --- |
| Frequency | Determines the center frequency that is the geometrical mean of the low and high cutoff frequency. In logarithmic frequency scaling, the center frequency is midway between the low and high cutoff frequency. |
| Bandwidth | The bandwidth determines the difference between the low and high cutoff frequency. It defines the width of the frequency range that is attenuated or allowed through. |

The following figure shows the amplitude response of a bandpass filter with Frequency = 100 Hz and different values for the tag Bandwidth (Order = 10, Characteristic = 2):

![Frequency and bandwidth](images/167556885003_DV_resource.Stream@PNG-de-DE.png)

The maximum cutoff or center frequency that can be used depends on the cycle time. The permitted range of values is Frequency &lt; 0.5 / CycleTime.Value.

The maximum bandwidth that can be used depends on the cycle time and the center frequency. The permitted range of values is Bandwidth &lt; 0.5 / CycleTime.Value - Frequency.

> **Note**
>
> To avoid aliasing, the sampling rate for the Filter_Universal (= 1 / cycle time) must be at least double the maximum frequency of the processed signals or signal components. The recommendation is to set a cycle time that is lower than this limit.
>
> **Example**: A signal with frequency components up to 100 Hz requires a sampling rate greater than 200 Hz. This corresponds to a maximum cycle time of 5 ms, but the recommendation is to set a lower value.

#### Order

The filter order determines how quickly attenuation increases beyond the cutoff frequency. This corresponds to the slope of the amplitude response beyond the cutoff frequency. The filter order is defined by the Order tag.

With a higher-order filter:

- The same frequency is attenuated more strongly beyond the cutoff frequency. The amplitude response shows a higher slope.
- Increases the execution time of Filter_Universal.
- The overshoot of the step response increases after an input jump for Butterworth and Chebyshev filter characteristic ( Characteristic tag = 1 or 2).

For bandpass and bandstop filters, the recommendation is to use only higher order filters; otherwise, the desired filter effect in the frequency range around the center frequency may not be reached.

Values from 0 to 10 can be configured at the Order tag for the filter order.

With the setting Order = 0, the filter has no effect and Output = Input.

#### Characteristic

The filter characteristic is defined by the Characteristic tag.

This affects:

- The ripple of the amplitude response in the passband
- The slope of the amplitude response beyond the cutoff frequency (how fast attenuation increases)
- The overshoot in the step response after an input jump

Three characteristics can be configured for Filter_Universal based on the Characteristic tag:

| Characteristic | Description |
| --- | --- |
| 0 | Bessel:  This filter has a flat amplitude response in the passband. The slope of the amplitude response beyond the cutoff frequency is smaller as compared to the Butterworth filter and Chebyshev filter. The step response only shows a small overshoot. |
| 1 | Butterworth:  This filter has a flat amplitude response in the passband. The slope of the amplitude response beyond the cutoff frequency is greater as compared to the Bessel filter and smaller as compared to the Chebyshev filter. The overshoot of the step response is greater as compared to the Bessel filter and smaller as compared to the Chebyshev filter. |
| 2 | Chebyshev Type I:  This filter has a 0.5 dB ripple of the amplitude response in the passband. The slope of the amplitude response beyond the cutoff frequency is greater as compared to the Bessel filter and to the Butterworth filter. The step response shows a greater overshoot as compared to the Bessel filter and the Butterworth filter. |

The following figure shows the effect of different order and characteristic values on the amplitude response of the low-pass filter:

![Characteristic](images/167556893579_DV_resource.Stream@PNG-de-DE.png)

#### Changing filter parameters

Before the filter algorithm calculates the output value, Filter_Universal needs to determine the filter coefficients once based on the filter parameters. This is triggered in the following situations:

- On the first execution after the change of operating state of the CPU from STOP to RUN
- Every time the filter parameters are changed
- When "Load start values as actual values" is executed

The following conditions for the filter parameters are checked in this process:

- 0.0 &lt; Frequency &lt; 0.5 / CycleTime.Value
- 0.0 ≤ Bandwidth &lt; 0.5 / CycleTime.Value - Frequency
- 0 ≤ Type ≤ 3
- 0 ≤ Characteristic ≤ 2
- 0 ≤ Order ≤ 10

If one of these conditions is not met and Reset = FALSE at the same time, correct calculation of the output value by the filter algorithm is not possible. In this case, an error message is output and a substitute output value is output at the Output parameter until all filter parameters have a valid value.

When all values are valid, the filter coefficients are determined once and saved internally for the filter algorithm calculation.

The reaction of the output value to valid changes to the filter parameters depends on the filter type:

- For high-pass and bandpass filters (Type = 1 or 2), the filter algorithm is set up as if it were in a steady state with Output = 0.0. If the Input parameter remains constant, the output value will jump to Output = 0.0. If the Input parameter changes, the output value jumps to an appropriate value.
- For low-pass and bandstop filters (Type = 0 or 3), the filter algorithm is set up as if it were in a steady state with Output = SubstituteOutput. Switchover is bumpless.

For time-critical applications, it should be taken into account that determining the filter coefficient requires a multiple of the execution time for calculating the filter algorithm.

### Initializing output values (S7-1500)

The first value of the Output parameter is initialized after the following actions for the first execution:

- Operating state change of the CPU from STOP to RUN
- Execution of "Load start values as actual values" with the option "All values"

The first value of the Output parameter depends on the filter type:

- For high-pass and bandpass filters (Type = 1 or 2), the first value of the parameter Output = 0.0.
- For low-pass and bandstop filters (Type = 0 or 3), the first value of the Output parameter can be configured via the StartMode tag.

For subsequent calls, Filter_Universal calculates the output value, starting from this initialization value, with consideration of the input value and the filter parameters.

The following settings of the StartMode tag are possible for low-pass and bandstop filters:

- StartMode = 0

  The Output parameter assumes the value of the Input parameter.

  ![Figure](images/170196259723_DV_resource.Stream@PNG-de-DE.png)
- StartMode = 1

  The Output parameter assumes the value of the SubstituteOutput parameter.

  ![Figure](images/170208607627_DV_resource.Stream@PNG-de-DE.png)
- StartMode = 2

  The Output parameter remains unchanged.

  ![Figure](images/170208701963_DV_resource.Stream@PNG-de-DE.png)
- StartMode = 3

  The Output parameter adopts the value 0.0.

  ![Figure](images/170208834187_DV_resource.Stream@PNG-de-DE.png)

The following applies in addition for all values of the StartMode tag:

- The StartMode tag and the filter parameters are not retentive. These tags are initialized with the start values after each operating state transition of the CPU from STOP to RUN. Make sure that at the first call of the Filter_Universal instruction, after the operating state transition of the CPU from STOP to RUN, these tags have suitable values to achieve the desired behavior.
- The value selected through StartMode is limited to the value range of the REAL data type. Only then is it output at the Output parameter.
- If the value selected through StartMode is not a valid REAL value, the substitute output value is output at the Output parameter. The substitute output value is configured by means of the ErrorMode tag and is limited to the value range of the REAL data type. If the substitute output value is also not a valid REAL value, 0.0 is output at the Output parameter. For subsequent calls, the instruction calculates the output value starting from this substitute output value.
- Only if the parameter Reset = FALSE has been set and, at the same time, there is no error pending with an error message ErrorBits ≥ 16#0002_0000, does the StartMode tag act on the Output parameter. If the Reset = TRUE parameter is set, the value of the SubstituteOutput parameter is output at the Output parameter. If an error with error message ErrorBits ≥ 16#0002_0000 is pending, the substitute output value that is configured at the ErrorMode tag is output at the Output parameter.

### Final value in steady state (S7-1500)

If the input value is constant, the output value of the Filter_Universal should also reach a constant final value after some time:

- Output = 0.0 for high-pass and bandpass filters (Type = 1 or 2)
- Output = Input for low-pass and bandstop filters (Type = 0 or 3)

The limited accuracy of the floating point arithmetic can have the result that this final value is not reached exactly.

This is more common with odd ordered filters (tag Order = 1, 3, 5, 7, or 9) than with even ordered filters.

In addition to choosing a even filter order, setting the tag FinalValueMode = 1 can help to achieve the final value. If the absolute value of the output value does not change for several cycles, this setting converts the output value to the final value. This option is only effective with a constant input value.

Using the FinalValueMode = 1 option can almost double the calculation time of the filter algorithm. The effect on the execution time depends on the filter parameters, input value and cycle time. For time-critical applications, you can check whether use of the FinalValueMode = 1 tag is necessary or whether the behavior with FinalValueMode = 0 is adequate.

Depending on the filter parameters, input value and cycle time, it is possible that the final value is already reached exactly with the FinalValueMode = 0 option and the FinalValueMode = 1 option is not necessary.

**Example:**

The following table shows the effect of the FinalValueMode tag on the output value of a low-pass filter with Frequency = 120.0, Order = 1, Characteristic = 2 and CycleTime.Value = 0.001, on an input jump from 1.0 to 0.0:

| Time in seconds | Input | Output with FinalValueMode = 0 | Output with FinalValueMode = 1 |
| --- | --- | --- | --- |
| -0.001 | 1.0 | 1.0000000 | 1.0000000 |
| 0.000 | 0.0 | 0.7163693 | 0.7163693 |
| 0.001 | 0.0 | 0.3100007 | 0.3100007 |
| … | 0.0 | ... | ... |
| 0.075 | 0.0 | -4.597156E-17 | -4.597156E-17 |
| 0.076 | 0.0 | 4.597156E-17 | 4.597156E-17 |
| 0.077 | 0.0 | -4.597156E-17 | -4.597156E-17 |
| 0.078 | 0.0 | 4.597156E-17 | 0.0000000 |
| 0.079 | 0.0 | -4.597156E-17 | 0.0000000 |
| ... | 0.0 | +/-4.597156E-17 | 0.0000000 |

### Use in time-critical applications (S7-1500)

The execution time of Filter_Universal depends to a significant effect on its configuration. With a standard configuration (CycleTime.EnableDetection = TRUE, FinalValueMode = 1), it is not possible for all CPU types to execute a higher order filter in the fastest possible cycle time. When Filter_Universal is used for high signal frequencies, such fast cycle times can be necessary. For example, signal frequencies of up to 2 kHz require a cycle time of at most 250 µsec.

The following adjustments to the configuration can help to reduce the execution time of Filter_Universal in a time-critical application:

- Reduction of the filter order (Order tag) if the desired filter behavior can still be achieved in this way.
- Setting of FinalValueMode to 0 if this does not cause a relevant difference in the filter behavior for constant input values as compared to FinalValueMode = 1.
- Setting of CycleTime.EnableDetection to FALSE and manual specification of the CycleTime.Value tag. This only has an effect on the execution time of the first call, or after the filter parameters have been changed.

The current operating state of Filter_Universal has an effect on the execution time. Determining the filter coefficients during the first execution or after a change to the filter parameters requires a multiple of the execution time required to calculate the filter algorithm with constant parameters.

### Call environment and automatic detection of the cycle time (S7-1500)

To calculate the output value, Filter_Universal requires a constant cycle time and therefore needs to be called in a cyclic interrupt OB. With the default configuration, Filter_Universal detects the cycle time of the OB automatically and saves it in the CycleTime.Value tag. This happens in the following situations:

- On the first execution after the change of operating state of the CPU from STOP to RUN
- Every time the filter parameters are changed
- When "Load start values as actual values" is executed

If the automatic detection of the cycle time does not return a valid result or Filter_Universal is not called in a cyclic interrupt OB, correct calculation of the Output parameter is not possible. In this case, an error message is output and a substitute output value is output at the parameter until until a valid cycle time of a cyclic interrupt OB is detected.

Please note that changes to the call rate due to conditional calls of Filter_Universal lead to deviations between the detected and actual cycle time, which influences the filter behavior. Therefore, avoid conditional calls of Filter_Universal.

Active breakpoints or the loading of snapshots as actual values have no effect on the automatic detection of the cycle time.

When you disable automatic detection of the cycle time by setting the CycleTime.EnableDetection = FALSE tag, you must enter the cycle time manually at the CycleTime.Value tag. Filter_Universal checks the Variable CycleTime.Value tag for validity at each call.

Deactivating the automatic detection of the cycle time reduces the execution time of the Filter_Universal, which can be helpful for time-critical applications. Calls outside of a cyclic interrupt OB can have a negative effect on the filter behavior, because the actual cycle time is not constant in this case.

### Reset response (S7-1500)

The Filter_Universal instruction behaves as follows depending on the Reset parameter:

- If the parameter Reset = TRUE is set, the value of the SubstituteOutput parameter is output at the Output parameter.
- If the parameter Reset = FALSE, the value that is output at the Output parameter is calculated by the filter algorithm.
- When the Reset parameter is set from FALSE to TRUE, the value at the Output parameter changes directly to the value of the SubstituteOutput parameter. An output jump can occur during this transition. In addition, the ErrorBits parameter is reset.
- If the Reset parameter is set from TRUE to FALSE, the behavior depends on the filter type:

  - For high-pass and bandpass filters (Type = 1 or 2), the filter algorithm is set up as if it were in a steady state with Output = 0.0. If the Input parameter remains constant, the output value will jump to Output = 0.0. If the Input parameter changes, the output value jumps to an appropriate value.
  - For low-pass and bandstop filters (Type = 0 or 3), the filter algorithm is set up as if it were in a steady state with Output = SubstituteOutput. Switchover is bumpless.

### Enable behavior EN/ENO (S7-1500)

If one of the following conditions is met, enable output ENO is set to FALSE:

- Enable input EN is set to TRUE and the Output parameter is specified by a substitute output value in case of error messages ErrorBits ≥ 16#0001_0000.
- Enable input EN is set to FALSE.

Otherwise, the enable output ENO is set to TRUE.

## Input parameter Filter_Universal (S7-1500)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Input | REAL | 0.0 | Input value |
| SubstituteOutput | REAL | 0.0 | SubstituteOutput is used as a substitute output value when Reset = TRUE or one of the following modes is currently in effect:  - ErrorMode = 1 - StartMode = 1 |
| ErrorAck | BOOL | FALSE | Deletes the error messages.  - Edge FALSE -&gt; TRUE ErrorBits is reset. |
| Reset | BOOL | FALSE | Resets the instruction  - Edge FALSE -&gt; TRUE   ErrorBits is reset. - As long as Reset is set to TRUE, the substitute output value SubstituteOutput is output. - As long as Reset is set to FALSE, the calculation of the output value is performed. - Edge TRUE -&gt; FALSE   - For high-pass and bandpass filters (Type 1 or 2), the filter algorithm is set up as if it were in a steady state with Output = 0.0.   - For low-pass and bandstop filters (Type 0 or 3), the filter algorithm is set up as if it were in a steady state with Output = SubstituteOutput. |

## Output parameter Filter_Universal (S7-1500)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Output | REAL | 0.0 | Output value  The output value is retentive. |
| ErrorBits | DWORD | 16#0 | The [ErrorBits parameter](#errorbits-parameter-s7-1500) shows which error messages are pending. ErrorBits is retentive and is reset upon a rising edge at Reset or ErrorAck. |
| Error | BOOL | FALSE | When Error is set to TRUE, at least one error is currently pending. |

## Static tags Filter_Universal (S7-1500)

| Tag | Data type | Default | Description |
| --- | --- | --- | --- |
| Frequency | REAL | 50.0 | Cutoff frequency of low-pass and high-pass or center frequency of bandpass and bandstop in Hz  Permissible value range: 0.5/CycleTime.Value &gt; Frequency &gt; 0.0 |
| Bandwidth | REAL | 0.0 | Bandwidth of bandpass and bandstop in Hz  Permissible value range: 0.5/CycleTime.Value - Frequency &gt; Bandwidth ≥ 0.0 |
| Type | INT | 0 | Filter type  - 0 = Low-pass filter - 1 = High-pass filter - 2 = Bandpass filter - 3 = Bandstop filter   Permissible value range: 0 to 3 |
| Characteristic | INT | 0 | Filter characteristic   - 0 = Bessel - 1 = Butterworth - 2 = Chebyshev with 0.5 dB ripple in the passband   Permissible value range: 0 to 2 |
| Order | INT | 2 | Filter order (at Order = 0, Output = Input)  Permissible value range: 0 to 10 |
| ErrorMode | INT | 2 | Selection of the substitute output value following an error   - 0 = Input - 1 = SubstituteOutput - 2 = Last valid filter output value - 3 = 0.0   Permissible value range: 0 to 3  If the value of ErrorMode does not correspond to the permissible range of values, then ErrorMode = 2. |
| StartMode | INT | 2 | Selection of the first output value for low-pass and bandstop filter   - 0 = Input - 1 = SubstituteOutput - 2 = Last output value - 3 = 0.0   Permissible value range: 0 to 3  If the value of StartMode does not correspond to the permissible range of values, then StartMode = 2. |
| FinalValueMode | INT | 1 | Selection of the behavior in steady state   - 0 = Deviations between output value and final value possible - 1 = Output value reaches final value exactly   Permissible value range: 0 to 1  If the value of FinalValueMode does not correspond to the permissible range of values, then FinalValueMode = 1. |
| CycleTime | AuxFct_CycleTimeDetection | - | Cycle time data |
| CycleTime.Value | REAL | 0.001 | Cycle time in seconds (interval between two calls)  Permissible value range: CycleTime.Value &gt; 0.0 |
| CycleTime.EnableDetection | BOOL | TRUE | Automatic detection of the cycle time  - FALSE = Deactivated - TRUE = Activated |

## ErrorBits parameter (S7-1500)

If several errors are pending simultaneously, the values of the ErrorBits are displayed with binary addition. The display of ErrorBits = 16#0000_0003, for example, indicates that the errors 16#0000_0001 and 16#0000_0002 are pending simultaneously.

With Filter_Universal, the errors output at the ErrorBits parameter are divided into two categories:

- Errors with error messages ErrorBits &lt; 16#0001_0000  
  The output value can be calculated despite the error.
- Errors with error messages ErrorBits ≥ 16#0001_0000  
  The error prevents calculation of the output value. A substitute output value is output.

### Errors with error messages ErrorBits &lt; 16#0001_0000

If one or more errors with error messages ErrorBits &lt; 16#0001_0000 is/are pending, Filter_Universal reacts as follows:

- The output value is determined as follows despite this error:

  - When Reset = FALSE, output value calculation by the filter algorithm
  - When Reset = TRUE, output of SubstituteOutput
- The output parameter Error is set.
- The enable output ENO is not changed.

The output parameter Error is deleted as soon as there are no longer any errors.

| ErrorBits  (DW#16#...) | Description |
| --- | --- |
| 0000_0000 | No error is pending. |
| 0000_0001 | **Cause of error and response to error:**   The Output parameter was limited to -3.402823e+38 or +3.402823e+38.   **Solution:**   If the value determined by the filter function is output at the output (Reset = FALSE and ErrorBits &lt; 16#0001_0000), check the Input parameter.  When ErrorBits ≥ 16#0001_0000 and Reset = FALSE, the substitute output value is limited on its output. In this case, check the following parameters depending on the set value at the tag ErrorMode:  - Input - SubstituteOutput   When Reset = TRUE, check the SubstituteOutput parameter. |

### Errors with error messages ErrorBits ≥ 16#0001_0000

If one or more errors with error messages ErrorBits ≥ 16#0001_0000 is/are pending, Filter_Universal reacts as follows:

- The output value cannot be determined as expected. The substitute output value is output instead.
- The output parameter Error is set.
- The enable output ENO is set to FALSE.

As soon as there are no longer errors with error messages ErrorBits ≥ 16#0001_0000, Filter_Universal reacts as follows:

- The output value is determined as follows:

  - When Reset = FALSE, output value calculation by the filter algorithm
  - When Reset = TRUE, output of SubstituteOutput
- The enable output ENO is set to TRUE.

The output parameter Error is deleted as soon as there are no longer any errors.

| ErrorBits  (DW#16#...) | Description |  |  |
| --- | --- | --- | --- |
| 0001_0000 | **Cause of error:**   The SubstituteOutput parameter or a different tag that is being used as output value has no valid REAL value.    **Response to error:**   The output is set to 0.0.   **Solution:**   Make sure that the tag used as output value is a valid REAL value (≠NaN e.g. 16#7FFF_FFFF). The tag that is used as output value depends on Reset and ErrorMode: |  |  |
| **Reset** | **ErrorMode** | **Output value** |  |
| FALSE | 0 | Input |  |
| FALSE | 1 | SubstituteOutput |  |
| TRUE | - | SubstituteOutput |  |
| 0002_0000 | **Cause of error:**   The Input parameter has no valid REAL value while the calculation of the output value is being performed (Reset = FALSE).   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.  When ErrorMode = 0, 0.0 is used as output value.   **Solution:**   Make sure that the parameter Input is a valid REAL value (≠NaN e.g. 16#7FFF_FFFF). |  |  |
| 0004_0000 | **Cause of error:**   The calculation of the output value yields an invalid REAL value for the Output parameter.   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.   **Solution:**   Check all tags involved in the calculation of the output value:  - Input - Frequency - Bandwidth - Type - Characteristic - Order - CycleTime.Value   These tags have valid values. The calculation of the output value fails in this combination of tags. |  |  |
| 0008_0000 | **Cause of error:**   One or more filter parameters have an invalid value while the calculation of the output value is being performed (Reset = FALSE).   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.   **Solution:**   Ensure that the following conditions for the values of the filter parameters are met:  - 0.0 &lt; Frequency &lt; 0.5 / CycleTime.Value - 0.0 ≤ Bandwidth &lt; 0.5 / CycleTime.Value - Frequency - 0 ≤ Type ≤ 3 - 0 ≤ Characteristic ≤ 2 - 0 ≤ Order ≤ 10 |  |  |
| 0010_0000 | **Cause of error:**   Automatic detection of the cycle time failed because Filter_Universal is not called in a cyclic interrupt OB.   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.   **Solution:**   Make sure that Filter_Universal is called in a cyclic interrupt OB.   **Additional information:**   Automatic detection of the cycle time can be disabled by setting the tag CycleTime.EnableDetection = FALSE. You then need to specify the cycle time manually at the Variable CycleTime.Value. Calling of Filter_Universal outside of a cyclic interrupt OB can have a negative effect on the filter behavior, because the actual cycle time fluctuates in this case. |  |  |
| 0020_0000 | **Cause of error:**   The tag (configured with StartMode) for the initialization of the Output parameter at the first call of the instruction does not have a valid REAL value.   **Response to error:**   The substitute output value is output with the first call of the instruction at the Output parameter that is configured at the ErrorMode tag. For subsequent calls, Filter_Universal calculates the output value starting from this substitute output value.   **Solution:**   Make sure that the tag for initializing the parameter Output is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF). When Reset = FALSE is set, the initialization takes effect with the first call of the instruction after the operating state transition of the CPU from STOP to RUN. The tag that is used for the initialization of the Output parameter depends on StartMode:  - StartMode = 1: SubstituteOutput - StartMode = 2: Output |  |  |
| 0040_0000 | **Cause of error:**   The CycleTime.Value tag has an invalid value, while the calculation of the output value is being performed (Reset = FALSE).   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.   **Solution:**   Ensure that the following conditions are met:  - 0.0 &lt; CycleTime.Value ≤ 3.402823e+38 - CycleTime.Value is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF)    **Additional information:**   To automatically calculate the value of the CycleTime.Value tag, set the CycleTime.EnableDetection tag to TRUE. |  |  |
| 0080_0000 | **Cause of error:**   An internal error occurred during automatic detection of the cycle time.   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.   **Solution:**   Make sure that Filter_Universal is called in a cyclic interrupt OB. If the error continues to occur, contact SIMATIC Customer Support.   **Additional information:**   Automatic detection of the cycle time can be disabled by setting the tag CycleTime.EnableDetection = FALSE. You then need to specify the cycle time manually at the CycleTime.Value tag. |  |  |
