---
title: "RampFunction (S7-1200, S7-1500)"
package: ProgFBPIDRampFenUS
topics: 8
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# RampFunction (S7-1200, S7-1500)

This section contains information on the following topics:

- [Compatibility with CPU and FW (S7-1200, S7-1500)](#compatibility-with-cpu-and-fw-s7-1200-s7-1500)
- [RampFunction description (S7-1200, S7-1500)](#rampfunction-description-s7-1200-s7-1500)
- [RampFunction mode of operation (S7-1200, S7-1500)](#rampfunction-mode-of-operation-s7-1200-s7-1500)
- [RampFunction input parameters (S7-1200, S7-1500)](#rampfunction-input-parameters-s7-1200-s7-1500)
- [RampFunction output parameters (S7-1200, S7-1500)](#rampfunction-output-parameters-s7-1200-s7-1500)
- [RampFunction static tags (S7-1200, S7-1500)](#rampfunction-static-tags-s7-1200-s7-1500)
- [ErrorBits parameter (S7-1200, S7-1500)](#errorbits-parameter-s7-1200-s7-1500)

## Compatibility with CPU and FW (S7-1200, S7-1500)

The following table shows which version of RampFunction can be used on which CPU:

| CPU | FW | RampFunction |
| --- | --- | --- |
| S7-1200 | as of V4.2 | V1.0 |
| S7-1500-based CPUs | as of version V2.0 | V1.0 |

## RampFunction description (S7-1200, S7-1500)

### Description

The RampFunction instruction limits the slew rate of a signal. RampFunction outputs a signal jump at the input as ramp function of the output value.

Use the RampFunction to prevent signal jumps, for example, in the following cases:

- Between setpoint source and setpoint input of the controller to achieve a smoother response without influencing the disturbance reaction.
- Between the controller output and the actuator input to preserve the actuator, for example, a motor with gears or the process.

The following limits can be set for the slew rate:

- Increasing slew rate in positive value range
- Decreasing slew rate in positive value range
- Increasing slew rate in negative value range
- Decreasing slew rate in negative value range

In addition, the RampFunction instruction limits the output value to the high and low limit.

When the slew rate limit or the low or high limit are reached, RampFunction sets the associated output bit to TRUE.

### Function chart

The following figure shows the RampFunction instruction and a function chart as an example:

![Function chart](images/166087510795_DV_resource.Stream@PNG-de-DE.png)

### Call

In an OB or FC, RampFunction is called as single-instance DB. In an FB, RampFunction can be called as a single-instance DB, as a multi-instance DB, and as a parameter instance DB.

When the instruction is called, no technology object is created. No parameter assignment interface or commissioning interface is available. You assign the RampFunction parameters directly using the instance DB and commission RampFunction using a watch table of the user program in the CPU or HMI.

### Startup

The tags in the static area of RampFunction are not retentive. These tags are initialized with the start values after each operating state transition of the CPU from STOP to RUN.

If you change the actual values of the limits in online mode and these values are to be retained after the operating state transition of the CPU, back up these values in the start values of the data block.

Specify the initialization value for the Output parameter at the StartMode tag.

During the first call of RampFunction after the

- Operating state transition of the CPU

or

- Execution of "Load start values as actual values" (only with "All values" option, not with "Only setpoints" option)

the initialization value is output at the Output parameter.

For subsequent calls, RampFunction calculates the output value, starting from this initialization value, based on the input value and the slew rate limits.

The following table shows the dependency between the StartMode tag and the Output parameter. The values in the Output column are output at the Output parameter after the operating state transition of the CPU.

| StartMode | Output | Example |
| --- | --- | --- |
| 0 | Value of the Input parameter | ![Startup](images/166087515915_DV_resource.Stream@PNG-de-DE.png) |
| 1 | Value of the SubstituteOutput parameter | ![Startup](images/166087531275_DV_resource.Stream@PNG-de-DE.png) |
| 2 | Remains unchanged. Output parameter is retentive. | ![Startup](images/166087521035_DV_resource.Stream@PNG-de-DE.png) |
| 3 | 0.0 | ![Startup](images/166087526155_DV_resource.Stream@PNG-de-DE.png) |
| 4 | Value of the LowerLimit tag | ![Startup](images/166087536395_DV_resource.Stream@PNG-de-DE.png) |
| 5 | Value of the UpperLimit tag | ![Startup](images/166087541515_DV_resource.Stream@PNG-de-DE.png) |

The following applies in addition for all values of the StartMode tag:

- When the values of the UpperLimit and LowerLimit tags are valid, the initialization value is limited to the value range of these tags. Only then is the initialization value output at the Output parameter.
- If the initialization value is not a valid REAL value, the substitute output value is output at the Output parameter. The substitute output value is configured by the ErrorMode tag. The substitute output value is limited by the value range of the tags UpperLimit and LowerLimit. If the substitute output value is also not a valid REAL value, 0.0 is output at the Output parameter. For subsequent calls, the instruction calculates the output value starting from this substitute output value.
- The StartMode tag is only effective when the Reset = FALSE parameter is set at the first call of the instruction and at the same time no error with error message ErrorBits ≥ 16#0002_0000 is pending. If the Reset = TRUE parameter is set, the value of the SubstituteOutput parameter is output at the Output parameter. If an error with error message ErrorBits ≥ 16#0002_0000 is pending, the substitute output value that is configured at the ErrorMode tag is output at the Output parameter.

### Responses in the event of an error

The RampFunction instruction detects different errors that can occur during the calculation of the output value. The result of this calculation can be output at the output despite a pending error. If an error prevents correct calculation of the output value, a substitute output value is output at the output.

Specify the substitute output value that is output if an error occurs that prevents correct calculation of the output value at the ErrorMode tag.

The following table shows the dependency between the ErrorMode tag and the substitute output value that is output by the RampFunction at the Output parameter:

| ErrorMode | Output |
| --- | --- |
| 0 | Value of the Input parameter |
| 1 | Value of the SubstituteOutput parameter |
| 2 | The last valid output value at the Output parameter |
| 3 | 0.0 |
| 4 | Value of the LowerLimit tag |
| 5 | Value of the UpperLimit tag |

The following applies in addition for all values of the ErrorMode tag:

- If the substitute output value is not a valid REAL value, 0.0 is output as output value.
- When the values of the UpperLimit and LowerLimit tags are valid, the substitute output value is limited to the value range of these tags. Only then is the substitute output value output at the Output parameter.
- The ErrorMode tag is only effective when the Reset = FALSE parameter is set. If the Reset = TRUE parameter is set, the value of the SubstituteOutput parameter is output at the Output parameter.
- If an error is pending that prevents correct calculation of the output value, RampFunction changes at the Output parameter from the calculated output value to the substitute output value. A jump of the output value can occur, depending on the value of the ErrorMode tag.

The Error parameter indicates if an error is pending. When the error is no longer pending, Error is set to FALSE. The ErrorBits parameter shows which errors have occurred. ErrorBits is retentive and is reset only by a positive edge at the Reset or ErrorAck parameter.

## RampFunction mode of operation (S7-1200, S7-1500)

### Limiting the slew rate

You can configure four limits for the slew rate of the input signal. The following factors determine which limit is currently in effect:

- Sign of the output value at the Output parameter
- Change of direction of the absolute value of the output value at the Output parameter

The following table shows the effective tags for the slew rate limit depending on the Output parameter:

| Output | Effective tag |
| --- | --- |
| Output ≥ 0 and |Output| rising | PositiveRisingSlewRate |
| Output ≥ 0 and |Output| falling | PositiveFallingSlewRate |
| Output &lt; 0 and |Output| rising | NegativeRisingSlewRate |
| Output &lt; 0 and |Output| falling | NegativeFallingSlewRate |

The absolute value of the slew rate limits defines the maximum change of the output value per second.

**Example:**

The following scenario applies for the example:

- PositiveRisingSlewRate = 10.0
- Call time of RampFunction = 0.1 s
- Input &gt; Output ≥ 0.0

Result:

The output value Output increases by 1.0 per call (10.0 per second) until the value at the Input parameter has been reached.

To disable the slew rate limit for one or more areas, set the corresponding tag to the value 3.402823e+38.

When the output value Output is currently limited by a slew rate limit, RampFunction sets the associated output bit to TRUE:

- PositiveRisingSlewRate_Active
- PositiveFallingSlewRate_Active
- NegativeRisingSlewRate_Active
- NegativeFallingSlewRate_Active

When the Reset parameter is set to TRUE, the slew rate limits are not in effect. This means jumps at the SubstituteOutput parameter result in jumps at the Output parameter.

RampFunction checks whether the following conditions for the tags PositiveRisingSlewRate, PositiveFallingSlewRate, NegativeRisingSlewRate and NegativeFallingSlewRate are met for each call:

- Values are within the permitted value range greater than 0.0 up to 3.402823e+38
- Values are valid REAL values (≠ NaN e.g. 16#7FFF_FFFF)

If one or more conditions are not met, the substitute output value is output at the Output parameter. A corresponding error message is output at the ErrorBits parameter.

### Limiting the output value

The output value Output is always limited to the value range of the tags UpperLimit and LowerLimit as long as these tags have valid values.

When the output value Output is currently limited by this value range, RampFunction sets the associated output bit to TRUE:

- UpperLimit_Active
- LowerLimit_Active

The limit of the output value has a higher priority than the limit of the slew rate. Changes of the tags UpperLimit and LowerLimit therefore result in jumps of the output value Output, if this is required to observe the limits of the tags UpperLimit and LowerLimit. The limiting of the slew rate is not taken into account in this case.

**Example:**

If the UpperLimit is reduced from 100.0 to 80.0 while the values of the parameters Input and Output are 90.0, the output value Output jumps to 80.0. The output value Output jumps to 80.0 regardless whether or not it violates the configured limit for the slew rate.

RampFunction checks whether the following conditions are met for each call:

- LowerLimit &lt; UpperLimit
- LowerLimit and UpperLimit are within the permitted value range from -3.402823e+38 to 3.402823e+38
- LowerLimit and UpperLimit are valid REAL values (≠ NaN e.g. 16#7FFF_FFFF)

If one or more conditions are not met, the substitute output value is output at the Output parameter. A corresponding error message is output at the ErrorBits parameter.

In addition, RampFunction checks for each call whether the output value Output has the permitted value range of a REAL data type from -3.402823e+38 to 3.402823e+38. If the calculation of the output value yields an invalid REAL value, the substitute output value is output at the Output parameter. You configure the substitute output value at the ErrorMode tag.

### Enable behavior EN/ENO

If one of the following conditions is met, enable output ENO is set to FALSE.

- Enable input EN is set to TRUE and the Output parameter is specified by a substitute output value in case of error messages ErrorBits ≥ 16#0001_0000.
- Enable input EN is set to FALSE.

Otherwise, the enable output ENO is set to TRUE.

### Measuring the cycle time automatically

To calculate the slew rate of the output value RampFunction needs the time that has expired since the last call of RampFunction.

By default, the cycle time is measured automatically and output as of the second call at the CycleTime.Value tag. RampFunction measures the cycle time for each call of the instruction and can therefore be used in non-isochronous call cycles, e.g. in OB1.

Note that conditional calls of the instruction, active breakpoints, or the loading of snapshots as actual values during automatic measurement of the cycle time will extend the cycle time value.

If measurement of the cycle time returns no valid result, RampFunction calculates the current output value with the last valid cycle time. In addition, RampFunction outputs an error message at the ErrorBits parameter.

When you disable automatic measurement of the cycle time by setting the CycleTime.EnableMeasurement tag = FALSE, you must enter the cycle time manually at the CycleTime.Value tag. RampFunction checks the CycleTime.Value tag for validity at each call.

### Automatic measurement of the cycle time with breakpoints

When breakpoints are active between two calls of RampFunction, automatic measurement of the cycle time results in the actual time that has elapsed between two calls. When one breakpoint is active, the CPU is in HOLD operating state.

> **Note**
>
> The active breakpoints extend the time period between two calls of RampFunction.
>
> The longer the time period between two calls, the greater the maximum permitted change of the output value at the Output parameter.

**Example:**

The following scenario applies for the example:

- PositiveRisingSlewRate = 10.0
- Call time of RampFunction = 0.1 s
- Input &gt; Output ≥ 0.0

Result without breakpoints:

The output value Output increases by 1.0 per call until the value at the Input parameter has been reached.

Result with an active breakpoint of ten seconds:

With the next call, the output value Output increases by 100.0.

If you do not need the calculation of the output value based on the actual time with active breakpoints, follow these steps:

- Disable automatic measurement of the cycle time by setting the tag CycleTime.EnableMeasurement = FALSE.
- Enter the cycle time manually at the CycleTime.Value tag.

## RampFunction input parameters (S7-1200, S7-1500)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Input | REAL | 0.0 | Input value |
| SubstituteOutput | REAL | 0.0 | SubstituteOutput is used as the substitute output value when  - Reset = TRUE   or   - An error with error message ErrorBits ≥ 16#0001_0000 prevents correct calculation of the output value, and the configured value of ErrorMode is 1. |
| ErrorAck | BOOL | FALSE | Deletes the error messages  - Edge FALSE -&gt; TRUE   ErrorBits is reset |
| Reset | BOOL | FALSE | Performs a restart of the instruction  - Edge FALSE -&gt; TRUE   ErrorBits is reset. - As long as Reset is set to TRUE, the substitute output value SubstituteOutput is output at the output. - As long as Reset is set to FALSE, the calculation of the output value is performed. |

## RampFunction output parameters (S7-1200, S7-1500)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Output | REAL | 0.0 | Output value |
| PositiveRisingSlewRate_Active | BOOL | FALSE | When PositiveRisingSlewRate_Active = TRUE, the output value is currently limited by PositiveRisingSlewRate . |
| PositiveFallingSlewRate_Active | BOOL | FALSE | When PositiveFallingSlewRate_Active = TRUE, the output value is currently limited by PositiveFallingSlewRate. |
| NegativeRisingSlewRate_Active | BOOL | FALSE | When NegativeRisingSlewRate_Active = TRUE, the output value is currently limited by NegativeRisingSlewRate. |
| NegativeFallingSlewRate_Active | BOOL | FALSE | When NegativeFallingSlewRate_Active = TRUE, the output value is currently limited by NegativeFallingSlewRate. |
| UpperLimit_Active | BOOL | FALSE | When UpperLimit_Active = TRUE, the output value is currently limited by UpperLimit. |
| LowerLimit_Active | BOOL | FALSE | When LowerLimit_Active = TRUE, the output value is currently limited by LowerLimit. |
| ErrorBits | DWORD | DW#16#0 | The [ErrorBits parameter](#errorbits-parameter-s7-1200-s7-1500) shows which error messages are pending. ErrorBits is retentive and is reset at a positive edge at Reset or ErrorAck . |
| Error | BOOL | FALSE | When Error = TRUE, at least one error is currently pending. |

## RampFunction static tags (S7-1200, S7-1500)

| Tag | Data type | Default | Description |
| --- | --- | --- | --- |
| PositiveRisingSlewRate | REAL | 10.0 | Limit for slew rate of the output value per second in positive range with rising absolute value  With PositiveRisingSlewRate = 3.402823e+38, this slew rate limit is disabled.  Permissible value range: &gt; 0.0 |
| PositiveFallingSlewRate | REAL | 10.0 | Limit for slew rate of the output value per second in positive range with falling absolute value  With PositiveFallingSlewRate = 3.402823e+38, this slew rate limit is disabled.  Permissible value range: &gt; 0.0 |
| NegativeRisingSlewRate | REAL | 10.0 | Limit for slew rate of the output value per second in negative range with rising absolute value  With NegativeRisingSlewRate = 3.402823e+38, this slew rate limit is disabled.  Permissible value range: &gt; 0.0 |
| NegativeFallingSlewRate | REAL | 10.0 | Limit for slew rate of the output value per second in negative range with falling absolute value  With NegativeFallingSlewRate = 3.402823e+38, this slew rate limit is disabled.  Permissible value range: &gt; 0.0 |
| UpperLimit | REAL | 100.0 | High limit of output value  Permissible value range: &gt; LowerLimit |
| LowerLimit | REAL | 0.0 | Low limit of output value  Permissible value range: &lt; UpperLimit |
| ErrorMode | INT | 2 | Selection of the substitute output value following an error   - 0 = Input - 1 = SubstituteOutput - 2 = Last valid output value - 3 = 0.0 - 4 = LowerLimit - 5 = UpperLimit   Permissible value range: 0 to 5 |
| StartMode | INT | 2 | Selecting the output value for the first call of the instruction  - 0 = Input - 1 = SubstituteOutput - 2 = Last output value - 3 = 0.0 - 4 = LowerLimit - 5 = UpperLimit   Permissible value range: 0 to 5 |
| CycleTime | AuxFct_CycleTime | - | Cycle time data |
| CycleTime.Value | REAL | 0.1 | Time interval between two calls of the instruction in seconds  Permissible value range: &gt; 0.0 |
| CycleTime.EnableMeasurement | BOOL | TRUE | Automatic measurement of the cycle time  - FALSE = Deactivated - TRUE = Activated |

## ErrorBits parameter (S7-1200, S7-1500)

If several errors are pending simultaneously, the values of the ErrorBits are displayed with binary addition. The display of ErrorBits = 16#0000_0003, for example, indicates that the errors 16#0000_0001 and 16#0000_0002 are pending simultaneously.

For RampFunction, the errors output at the ErrorBits parameter are divided into two categories:

- Errors with error messages ErrorBits &lt; 16#0001_0000
- Errors with error messages ErrorBits ≥ 16#0001_0000

### Errors with error messages ErrorBits &lt; 16#0001_0000

If one or more errors with error messages ErrorBits &lt; 16#0001_0000 are pending, RampFunction reacts as follows:

- The output value is determined as follows despite this error:

  - When Reset = FALSE, output value calculation
  - When Reset = TRUE, output of SubstituteOutput
- The output parameter Error is set.
- The enable output ENO is not changed.

The output parameter Error is deleted as soon as there are no longer any errors.

| ErrorBits  (DW#16#...) | Description |
| --- | --- |
| 0000_0000 | No error is pending. |
| 0000_0002 | **Cause of error:**   The measurement of the cycle time yields in an invalid value while the output value is being calculated (Reset = FALSE).   **Response to error:**   If a valid value of the cycle time has already been measured, RampFunction calculates the output value based on the last value of the CycleTime.Value tag.  If no valid value of the cycle time was previously measured, RampFunction still outputs the output value configured with the StartMode tag at the Output parameter. |

### Errors with error messages ErrorBits ≥ 16#0001_0000

If one or more errors with error messages ErrorBits ≥ 16#0001_0000 are pending, RampFunction reacts as follows:

- The output value cannot be determined as expected. The substitute output value is output instead.
- The output parameter Error is set.
- The enable output ENO is set to FALSE.
- The output value limit remains active as long as the tags LowerLimit and UpperLimit have valid values.
- The slew rate limit is no longer active. Jumps at the output value can occur in one of the following scenarios:

  - When the error is detected, RampFunction switches from the calculated output value to the replacement output value. Whether a jump occurs depends on the value of the tag ErrorMode.
  - The substitute output value is changed while it is active.

As soon as there are no longer errors with error messages ErrorBits ≥ 16#0001_0000, RampFunction reacts as follows:

- The output value is determined as follows:

  - When Reset = FALSE, output value calculation
  - When Reset = TRUE, output of SubstituteOutput
- The enable output ENO is set to TRUE.

The output parameter Error is deleted as soon as there are no longer any errors.

| ErrorBits  (DW#16#...) | Description |  |  |
| --- | --- | --- | --- |
| 0001_0000 | **Cause of error:**   The SubstituteOutput parameter or a different tag that is being used as output value has no valid REAL value.   **Response to error:**   The output is set to 0.0 and limited by the tags LowerLimit and UpperLimit.   **Solution:**   Make sure that the tag used as output value is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF). The tag that is used as output value depends on Reset and ErrorMode: |  |  |
| **Reset** | **ErrorMode** | **Output value** |  |
| FALSE | 0 | Input |  |
| FALSE | 1 | SubstituteOutput |  |
| FALSE | 4 | LowerLimit |  |
| FALSE | 5 | UpperLimit |  |
| TRUE | - | SubstituteOutput |  |
| 0002_0000 | **Cause of error:**   The Input parameter has no valid REAL value while the calculation of the output value is being performed (Reset = FALSE).   **Response to error:**   The substitute output value is output at the Output parameter that is configured at the ErrorMode tag and is limited by the tags UpperLimit and LowerLimit.  When ErrorMode = 0, 0.0 is used as output value.   **Solution:**   Make sure that the parameter Input is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF). |  |  |
| 0004_0000 | **Cause of error:**   The calculation of the output value yields an invalid REAL value for the Output parameter.   **Response to error:**   The substitute output value is output at the Output parameter that is configured at the ErrorMode tag and is limited by the tags UpperLimit and LowerLimit.   **Solution:**   Check all tags involved in the calculation of the output value:  - Input - PositiveRisingSlewRate - PositiveFallingSlewRate - NegativeRisingSlewRate - NegativeFallingSlewRate - CycleTime.Value   These tags have valid values. The calculation of the output value fails in this combination of tags. |  |  |
| 0008_0000 | **Cause of error:**   The LowerLimit or UpperLimit tag has an invalid value.   **Response to error:**   The following value is output at the Output parameter, depending on the Reset parameter:  - Reset = FALSE   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter. - Reset = TRUE   The value of the SubstituteOutput parameter is output at the Output parameter.   In both cases, the Ouput parameter is limited to the value range of the REAL data type from -3.402823e+38 to 3.402823e+38.   **Solution:**   Ensure that the following conditions are met:  1. LowerLimit &lt; UpperLimit 2. LowerLimit and UpperLimit are within the permitted value range from -3.402823e+38 to 3.402823e+38 3. LowerLimit and UpperLimit are valid REAL values (≠ NaN e.g. 16#7FFF_FFFF) |  |  |
| 0010_0000 | **Cause of error:**   At least one of the following tags has invalid values while the calculation of the output value is being performed (Reset = FALSE):  1. PositiveRisingSlewRate 2. PositiveFallingSlewRate 3. NegativeRisingSlewRate 4. NegativeFallingSlewRate    **Response to error:**   The substitute output value is output at the Output parameter that is configured at the ErrorMode tag and is limited by the tags UpperLimit and LowerLimit.   **Solution:**   Ensure that the following conditions are met for all four tags listed above:  - The values are within the permitted value range greater than 0.0 up to 3.402823e+38 - The values are valid REAL values (≠ NaN e.g. 16#7FFF_FFFF) |  |  |
| 0020_0000 | **Cause of error:**   The tag (configured with StartMode) for the initialization of the Output parameter at the first call of the instruction does not have a valid REAL value.    **Response to error:**   The substitute output value is output with the first call of the instruction at the Output parameter that is configured at the ErrorMode tag and is limited by the tags LowerLimit and UpperLimit. For subsequent calls, RampFunction calculates the output value starting from this substitute output value.   **Solution:**   Make sure that the tag for initializing the parameter Output is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF). When Reset = FALSE is set, the initialization takes effect with the first call of the instruction after the operating state transition of the CPU from STOP to RUN. The tag that is used for the initialization of the Output parameter depends on StartMode:  - StartMode = 1: Substitute Output - StartMode = 2: Output |  |  |
| 0040_0000 | **Cause of error:**   The CycleTime.Value tag has an invalid value, while the calculation of the output value is being performed (Reset = FALSE).   **Response to error:**   The substitute output value is output at the Output parameter that is configured at the ErrorMode tag and is limited by the tags UpperLimit and LowerLimit.   **Solution:**   Ensure that the following conditions are met:  - 0.0 &lt; CycleTime.Value ≤ 3.402823e+38 - CycleTime.Value is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF)    **Additional information:**   To automatically calculate the value of the CycleTime.Value tag, set the CycleTime.EnableMeasurement tag to TRUE. |  |  |
