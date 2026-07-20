---
title: "SplitRange (S7-1200, S7-1500)"
package: ProgFBPIDSplitRenUS
topics: 7
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SplitRange (S7-1200, S7-1500)

This section contains information on the following topics:

- [Compatibility with CPU and FW (S7-1200, S7-1500)](#compatibility-with-cpu-and-fw-s7-1200-s7-1500)
- [SplitRange description (S7-1200, S7-1500)](#splitrange-description-s7-1200-s7-1500)
- [SplitRange input parameters (S7-1200, S7-1500)](#splitrange-input-parameters-s7-1200-s7-1500)
- [SplitRange output parameters (S7-1200, S7-1500)](#splitrange-output-parameters-s7-1200-s7-1500)
- [SplitRange static tags (S7-1200, S7-1500)](#splitrange-static-tags-s7-1200-s7-1500)
- [ErrorBits parameter (S7-1200, S7-1500)](#errorbits-parameter-s7-1200-s7-1500)

## Compatibility with CPU and FW (S7-1200, S7-1500)

The following table shows which version of SplitRange can be used on which CPU:

| CPU | FW | SplitRange |
| --- | --- | --- |
| S7-1200 | as of V4.2 | V1.0 |
| S7-1500-based CPUs | as of version V2.0 | V1.0 |

## SplitRange description (S7-1200, S7-1500)

### Description

The SplitRange instruction converts the input value into an output value. The input value is located in the value range that is limited by Points.x1 and Points.x2. The output value is located in the value range that is limited by Points.y1 and Points.y2.

The following figure shows the relevant characteristic of an example configuration of the SplitRange instruction:

![Description](images/166087500555_DV_resource.Stream@PNG-de-DE.png)

Use SplitRange when you need to control a process that is influenced by multiple actuators. SplitRange splits the output value range of the PID controller into multiple subranges. Assign a subrange to each actuator. The user program calls the block once per subrange. The input value of each SplitRange instance is connected to the output value of the PID controller.

The figure below shows an example of a control loop with two SplitRange instances and two actuators:

![Description](images/166087505675_DV_resource.Stream@PNG-de-DE.png)

### Validity of the SplitRange data

The value pairs in the Points structure define the input and output value range of SplitRange. The two value pairs are located in the static area of the block SplitRange.

SplitRange checks whether the following conditions are met for each call so that valid values are available for the calculation of the output value:

- Points.x1 &lt; Points.x2
- Points.x1, Points.y1, Points.x2 and Points.y2 are within the permitted value range from -3.402823e+38 to 3.402823e+38
- Points.x1, Points.y1, Points.x2 and Points.y2 are valid REAL values (≠ NaN e.g. 16#7FFF_FFFF)

If one or more of these conditions are not met, correct calculation of the output value is not possible. A corresponding error message is output at the ErrorBits parameter.

The preassignment of the x and y values with 0.0 does not represent a valid configuration. Change the tags to valid values so that the tags can be used for the calculation of the output value.

### Enable behavior EN/ENO

If one of the following conditions is met, enable output ENO is set to FALSE.

- Enable input EN is set to TRUE and the Output parameter is specified by a substitute output value in case of error messages ErrorBits ≥ 16#0001_0000.
- Enable input EN is set to FALSE.

Otherwise, the enable output ENO is set to TRUE.

### Call

In an OB or FC, SplitRange is called as single-instance DB. In an FB, SplitRange can be called as a single-instance DB, as a multi-instance DB, and as a parameter instance DB.

When the instruction is called, no technology object is created. No parameter assignment interface or commissioning interface is available. You assign the SplitRange parameters directly using the instance DB and commission SplitRange using a watch table of the user program in the CPU or HMI.

### Startup

The tags in the static area of SplitRange are not retentive. These tags are initialized with the start values after each operating state transition of the CPU from STOP to RUN.

If you change the actual values in the Points structure in online mode and these values are to be retained after the operating state transition of the CPU from STOP to RUN, back up these values in the start values of the data block.

### Responses in the event of an error

The SplitRange instruction detects different errors that can occur during the calculation of the output value. The result of the calculation can be output at the output despite a pending error. If an error prevents correct calculation of the output value, a substitute output value is output at the output.

You specify the substitute output value that is output if an error occurs that prevents correct calculation of the output value as follows at the ErrorMode tag:

| ErrorMode | Output |
| --- | --- |
| 0 | Value of the Input parameter |
| 1 | Value of the SubstituteOutput parameter |
| 2 | The last valid result of output value calculation  0.0 if there is no valid result |

The following applies in addition for all values of the ErrorMode tag:

- If the substitute output value is not a valid REAL value, 0.0 is output as output value.
- The substitute output value is limited to the value range of the data type REAL. Only then is the substitute output value output at the Output parameter.
- The ErrorMode tag is only effective when the Reset = FALSE parameter is set. If the Reset = TRUE parameter is set, the value of the SubstituteOutput parameter is output at the Output parameter.

The Error parameter indicates if an error is pending. When the error is no longer pending, Error is set to FALSE. The ErrorBits parameter shows which errors have occurred. ErrorBits is retentive and is reset only by a positive edge at the Reset or ErrorAck parameter.

## SplitRange input parameters (S7-1200, S7-1500)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Input | REAL | 0.0 | Input value |
| SubstituteOutput | REAL | 0.0 | SubstituteOutput is used as the substitute output value when  - Reset = TRUE   or   - An error with error message ErrorBits ≥ 16#0001_0000 prevents correct calculation of the output value, and the configured value of ErrorMode is 1. |
| ErrorAck | BOOL | FALSE | Deletes the error messages  - Edge FALSE -&gt; TRUE   ErrorBits is reset |
| Reset | BOOL | FALSE | Performs a restart of the instruction  - Edge FALSE -&gt; TRUE   ErrorBits is reset. - As long as Reset is set to TRUE, the substitute output value SubstituteOutput is output at the output. - As long as Reset is set to FALSE, the calculation of the output value is performed. |

## SplitRange output parameters (S7-1200, S7-1500)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Output | REAL | 0.0 | Output value |
| ErrorBits | DWORD | DW#16#0 | The [ErrorBits parameter](#errorbits-parameter-s7-1200-s7-1500) shows which error messages are pending. ErrorBits is retentive and is reset at a positive edge at Reset or ErrorAck . |
| Error | BOOL | FALSE | When Error is set to TRUE, at least one error is currently pending. |

## SplitRange static tags (S7-1200, S7-1500)

| Tag | Data type | Default | Description |
| --- | --- | --- | --- |
| Points | AuxFct_SplitRange_Points | - | Points data |
| Points.x1 | REAL | 0.0 | x-value of point 1  Permissible value range: Points.x1 &lt; Points.x2 |
| Points.y1 | REAL | 0.0 | y-value of point 1 |
| Points.x2 | REAL | 0.0 | x-value of point 2  Permissible value range: Points.x1 &lt; Points.x2 |
| Points.y2 | REAL | 0.0 | y-value of point 2 |
| ErrorMode | INT | 0 | Selection of the substitute output value following an error  - 0 = Input - 1 = SubstituteOutput - 2 = Last valid output value   Permissible value range: 0 to 2 |

## ErrorBits parameter (S7-1200, S7-1500)

If several errors are pending simultaneously, the values of the ErrorBits are displayed with binary addition. The display of ErrorBits = 16#0000_0003, for example, indicates that the errors 16#0000_0001 and 16#0000_0002 are pending simultaneously.

For SplitRange, the errors output at the ErrorBits parameter are divided into two categories:

- Errors with error messages ErrorBits &lt; 16#0001_0000
- Errors with error messages ErrorBits ≥ 16#0001_0000

### Errors with error messages ErrorBits &lt; 16#0001_0000

If one or more errors with error messages ErrorBits &lt; 16#0001_0000 are pending, SplitRange reacts as follows:

- The output value is determined as follows despite this error:

  - When Reset = FALSE, output value calculation
  - When Reset = TRUE, output of SubstituteOutput
- The output parameter Error is set.
- The enable output ENO is not changed.

The output parameter Error is deleted as soon as there are no longer any errors.

| ErrorBits  (DW#16#...) | Description |
| --- | --- |
| 0000_0000 | No error is pending. |
| 0000_0001 | **Cause of error and response to error:**   The Output parameter was limited to -3.402823e+38 or +3.402823e+38.   **Solution:**   When ErrorBits ≥ 16#0001_0000 and Reset = FALSE, the substitute output value is limited on its output. In this case, check the following parameters depending on the set value at the ErrorMode tag:  - Input - SubstituteOutput   When Reset = TRUE, check the SubstituteOutput parameter. |

### Errors with error messages ErrorBits ≥ 16#0001_0000

If one or more errors with error messages ErrorBits ≥ 16#0001_0000 are pending, SplitRange reacts as follows:

- The output value cannot be determined as expected. The substitute output value is output instead.
- The output parameter Error is set.
- The enable output ENO is set to FALSE.

As soon as there are no longer errors with error messages ErrorBits ≥ 16#0001_0000, SplitRange reacts as follows:

- The output value is determined as follows:

  - When Reset = FALSE, output value calculation
  - When Reset = TRUE, output of SubstituteOutput
- The enable output ENO is set to TRUE.

The output parameter Error is deleted as soon as there are no longer any errors.

| ErrorBits  (DW#16#...) | Description |  |  |
| --- | --- | --- | --- |
| 0001_0000 | **Cause of error:**   The SubstituteOutput or Input parameter that is being used as the output value has no valid REAL value.    **Response to error:**   The output is set to 0.0.   **Solution:**   Make sure that the parameter used as output value is a valid REAL value (≠ NaN e.g. 16#7FFF_FFFF). The parameter that is used as output value depends on Reset and ErrorMode: |  |  |
| Reset | ErrorMode | Output value |  |
| FALSE | 0 | Input |  |
| FALSE | 1 | SubstituteOutput |  |
| TRUE | - | SubstituteOutput |  |
| 0002_0000 | **Cause of error:**   The Input parameter has no valid REAL value while the calculation of the output value is being performed (Reset = FALSE).   **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.  When ErrorMode = 0, 0.0 is used as output value.   **Solution:**   Make sure that the parameter Input is a valid REAL value (≠NaN e.g. 16#7FFF_FFFF). |  |  |
| 0004_0000 | **Possible causes of error:**   - One or more tags in the Points structure have invalid values. - The calculation of the output value yields an invalid REAL value for the Output parameter.    **Response to error:**   The substitute output value that is configured at the ErrorMode tag is output at the Output parameter.   **Solution:**   Ensure that the following conditions are met:  1. Points.x1 &lt; Points.x2 2. Points.x1, Points.y1, Points.x2 and Points.y2 are within the permitted value range from -3.402823e+38 to 3.402823e+38 3. Points.x1, Points.y1, Points.x2 and Points.y2 are valid REAL values (≠ NaN e.g. 16#7FFF_FFFF)    **Additional information:**   Note that all tags in the Points structure are not retentive. These tags are initialized with the start values after each operating state transition of the CPU from STOP to RUN. |  |  |
