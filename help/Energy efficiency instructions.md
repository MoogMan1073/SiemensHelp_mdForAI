---
title: "Energy efficiency instructions"
package: TIAPortalEEmenUS
topics: 28
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Energy efficiency instructions

This section contains information on the following topics:

- [Basic information on energy efficiency instructions](#basic-information-on-energy-efficiency-instructions)
- [EnS_EEm_Calc: Acquire and evaluate machine efficiency uniformly](#ens_eem_calc-acquire-and-evaluate-machine-efficiency-uniformly)
- [EnS_EEm_Report: Create efficiency report as CSV file](#ens_eem_report-create-efficiency-report-as-csv-file)
- [PLC data types (UDTs)](#plc-data-types-udts)
- [Program example](#program-example)

## Basic information on energy efficiency instructions

This section contains information on the following topics:

- [Overview of functions](#overview-of-functions)
- [Areas of application](#areas-of-application)
- [Implementation via TIA Portal instructions / data types](#implementation-via-tia-portal-instructions-data-types)

### Overview of functions

The Energy Efficiency Monitor provides the following three main functions:

- Average power value calculation per operating state
- Distribution of energy to the respective operating state
- Calculation of specific energy consumption per unit produced

#### Average power value calculation per operating state

The average power value calculation per operating state is used to evaluate the machine characteristic. You can start a reference measurement and a current or last measurement. An average power value per operating state is calculated for each configured measuring point. The percentage difference is calculated as a result for each power value.

The following example shows the calculation of the percentage deviation of the power value of a current measurement relative to a reference measurement of an electrical measuring point in the "Standby" operating state:

- Reference measurement: 500 W
- Current measurement: 600 W
- Difference: 20%

The percentage deviation of 20% shows that the machine property has changed.

#### Distribution of energy to the respective operating state

The distribution of the energy to the respective operating state is used to evaluate the operation of the machine. Several status-related counters are mapped for the input value of a measuring point for each status. You can automatically map additional calculations as energy characteristics in SIMATIC Energy Manager PRO.

The following example shows the status-related distribution of the energy of an electrical measuring point:

- Counter in "Off" operating state: 10 kWh
- Counter in "Standby" operating state: 100 kWh
- Counter in "Operational" operating state: 390 kWh
- Counter in "Working" operating state: 2 000 kWh
- Counter value total: 2 500 kWh

The value-adding energy in the "Working" operating state is 80%.

#### Calculation of specific energy consumption per unit produced

With the energy efficiency monitor you can calculate the energy consumption per unit produced in relation to a specific operating state.

The following example shows the energy consumption of an electrical measuring point per unit produced in the "Working" operating state:

- Counter in "Working" operating state: 2 000 kWh
- Counter quantity: 100 units

The energy consumption is 20 kWh per unit. Only the "Working" operating state is taken into account when calculating the energy consumption per unit.

### Areas of application

Each production machine has different energetic states, for example Working, Operational, Standby, Off. The energetic states can be determined from the operating state, for example, Automatic, Manual, Fault and other signals.

The energy efficiency instructions determine the energetic key indicators and provide the energy efficiency report for production machines according to VDMA 34179.

Based on these key indicators, you evaluate the machines with regard to their energy efficiency in a simple and standardized manner. In this way, for example, you can detect creeping efficiency degradation caused by mechanical wear or evaluate potential for energy efficiency measures, for example, the introduction of a pause shutdown.

When needed, you transfer the pre-processed energy data to the SIMATIC Energy Manager PRO for continuous energy data analysis.

The following is an overview of the functions of the energy efficiency instructions and the key indicators.

#### Typical power consumption per operating state

The EnS_EEm_Calc instruction determines the typical power consumption, for example, for validation of the manufacturer's specifications for the machine or recurring inspection.

This results in the following advantages:

- Determination of a reference
- Determination of a deterioration in machine efficiency
- Creation of an energy efficiency report, for example, for auditing

#### Energy and media requirements per operating state

The EnS_EEm_Calc instruction assigns the energy or power counter value to the respective energetic operating state of the machine. Eight energetic operating states and ten measuring points are supported for each instance of the energy efficiency instruction.

This results in the following advantages:

- Possible to distinguish between value-adding and non-value-adding energy consumption
- Batch evaluation

#### Energy indicator per piece produced

The EnS_EEm_Calc instruction determines the amount of energy required for the quantity produced.

This results in the following advantages:

- Evaluation and comparison among the various operating states of a machine. For example, influencing the production speed, differences of individual product versions, evaluation of the energy intensity of products.

#### Creation of the energy efficiency report

The EnS_EEm_Report creates a CSV file on the SIMATIC memory card of the CPU from the data determined from the EnS_EEm_Calc instruction. The CSV file contains the configured machine parameters, for example, name, manufacturer and the measurement data of the current and reference measurement.

#### Example

A machine has the following average power consumption in the respective operating states:

| Operating state | Power consumption |
| --- | --- |
| Working | 15 kW |
| Operational | 8 kW |
| Standby | 1 kW |
| Off | 0.3 kW |

The following conditions also apply to this process:

- The machine produces 10 units in the process.
- One batch contains 100 units.
- The machine switches between the "Working" and "Operational" operating states during production.
- The machine changes to the "Standby" operating state between the batches.
- When a batch is finished, the production counter value returns to the value 0.0.

The following requirements apply to the machine:

- The machine provides a power value in LREAL format.
- The machine provides a production counter value.
- The machine provides the energetic operating state of the machine in USINT format.

For the acquisition and calculation of the energy data, you first need to create a global data block in your project. The names of the data block and the tags can be changed individually.

The following table shows the required configuration of the data block:

| Global data block | Tag | Configuration |
| --- | --- | --- |
| db_OEM_EEm_Machine | MachineConfiguration | EnS_EEm_typeConfig |
| MachineOperation | EnS_EEm_typeOperation |  |
| MeasurementsConfiguration | ARRAY[0..X] of "EnS_EEm_typeMeasConfig" |  |
| MeasurementsOperation | ARRAY[0..X] of "EnS_EEm_typeMeasOperation" |  |
| Error | BOOL |  |
| Status | WORD |  |

> **Note**
>
> To define the size of the arrays at the MeasurementsConfiguration and MeasurementsOperation tags with the same size, you need to create a user constant in the PLC tags with the corresponding value.

The following table shows how to configure the parameters:

| Energy efficiency component | Parameter | Configuration |
| --- | --- | --- |
| **Functions** |  |  |
| EnS_EEm_Calc | machineConfig | db_OEM_EEm_Machine.Machine1Configuration |
| machineOperation | db_OEM_EEm_Machine.Machine1Operation |  |
| measConfiguration | db_OEM_EEm_Machine.MeasurementsConfiguration |  |
| measOperation | db_OEM_EEm_Machine.MeasurementsOperation |  |
| error | db_OEM_EEm_Machine.Error |  |
| status | db_OEM_EEm_Machine.Status |  |
| **PLC data type** |  |  |
| EnS_EEm_typeConfig | licenseKey | "Valid license number" from the license certificate (Certificate of License "CoL") |
| pieceCounterOverlfow | 100.0  When the value exceeds 100.0, the production counter value jumps to 1.0. |  |
| EnS_EEm_typeOperation | pieceCounter | Assignment of the production counter value of the machine |
| eState | Assignment of the energetic operating state of the machine |  |
| triggerRecalcOutput | FALSE  If you set triggerRecalcOutput = TRUE, edge-triggered updating of the energy counter values at the output is initiated. You must then reset triggerRecalcOutput = FALSE. |  |
| startAvgCalcPeriod | Assignment of an HMI or PLC tag  If you want to start the calculation of the typical power consumption for each energetic state of the machine, set startAvgCalcPeriod = TRUE. |  |
| stopAvgCalcPeriod | Assignment of an HMI or PLC tag  If you want to stop the calculation of the typical power consumption for each energetic state of the machine, set stopAvgCalcPeriod = TRUE. |  |
| EnS_EEm_typeMeasConfig | unitActValueNumber | 1190  You can find additional information in the TIA Portal Information System under the keyword "Enumeration for units". |
| inputType | 2  The machine provides a power value; you therefore set inputType = 2. |  |

#### Output of the efficiency report on the Web server

The efficiency report is stored as a CSV file on the SIMATIC memory card by setting the request parameter of the EnS_EEm_Report instruction.

The name of the CSV file is unique and consists of the machine name and the time stamp in the following format: "&lt;Machine name&gt;_yyyymmdd_NN.csv". "NN" is a sequential number. The maximum number of files created per day is 100 (NN = 99).

You can find additional information in the section [EnS_EEm_Report description](#ens_eem_report-description).

### Implementation via TIA Portal instructions / data types

#### Overview of components, data flows

The following table shows the components of the "Energy Suite Extensions" folder in the "Options" palette of the "Instructions" task card:

| Component | Description |
| --- | --- |
| **Functions** |  |
| [EnS_EEm_Calc](#ens_eem_calc-description) | Calculation of the following energy data:  - Energy counter values - Average power consumption - Energy consumption per piece |
| **Blocks** |  |
| [EnS_EEm_Report](#ens_eem_report-description) | Creating the energy data as a data log (CSV file) on the S7-1200 and S7-1500 CPU on the SIMATIC memory card |
| **PLC data type** |  |
| [EnS_EEm_typeConfig](#ens_eem_typeconfig-configuration-data-for-a-machine) | Configuration data of a machine |
| [EnS_EEm_typeOperation](#ens_eem_typeoperation-operating-data-for-a-machine) | Operating data of a machine |
| [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) | Configuration data of a measuring point |
| [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) | Operating data of a measuring point |
| [EnS_EEm_type1Counter](#ens_eem_type1counter-parameters-for-energy-counter-value-input-signal) | Acquisition of the energy counter value |
| [EnS_EEm_type2ActualValue](#ens_eem_type2actualvalue-parameters-for-power-value-input-signal) | Acquisition of the power value |
| [EnS_EEm_typeInMeasOperation](#ens_eem_typeinmeasoperation-input-parameters-for-a-measuring-point) | Input parameters of the measuring point |
| [EnS_EEm_typeOutMeasOperation](#ens_eem_typeoutmeasoperation-output-parameters-for-a-measuring-point) | Output parameter of the measuring point |
| [EnS_EEm_typeReportData](#ens_eem_typereportdata-data-for-efficiency-report) | Interface for data exchange |

#### Compatibility with CPU and FW

The following table shows CPUs on which the respective versions of the energy efficiency components can be used:

| CPU | FW | Energy efficiency components |
| --- | --- | --- |
| S7-1200 | V4.2 and higher | V1.0 and higher |
| S7-1500 | V2.1 and higher | V1.0 and higher |
| S7-1500S | V2.1 and higher | V1.0 and higher |

#### Scale for calculation

Ten measuring points and eight energetic operating states are supported for each machine. One medium (e.g. gas, water) is supported for each measuring point.

All measuring points of a machine have the same energetic operating state.

The following table shows the maximum number of measuring points per CPU:

| CPU | Number of measuring points |
| --- | --- |
| S7-1200 | 250 |
| S7-1500 | 250 |

#### Licensing of the machine instances

An "S7 EE Monitor for Machines S7-1500/1200" license is required for each machine.

The license is verified by entering the 20-digit license number, which you can find on the license certificate (Certificate of License "CoL"):

![Licensing of the machine instances](images/111296818699_DV_resource.Stream@PNG-de-DE.png)

Enter the 20-digit license number at the licenseKey parameter of the EnS_EEm_typeConfig PLC data type.

## EnS_EEm_Calc: Acquire and evaluate machine efficiency uniformly

This section contains information on the following topics:

- [EnS_EEm_Calc description](#ens_eem_calc-description)
- [EnS_EEm_Calc operating principle](#ens_eem_calc-operating-principle)
- [EnS_EEm_Calc parameter](#ens_eem_calc-parameter)
- [Parameter status](#parameter-status)

### EnS_EEm_Calc description

#### Description

The EnS_EEm_Calc instruction is used for the uniform acquisition and calculation of the efficiency of machines.

EnS_EEm_Calc normalizes the input data to a power value or counter value. Then EnS_EEm_Calc links this value to an energetic operating state of the machine and outputs the state-related energy counter value and power consumption.

An efficiency report cannot be generated while the efficiency is being calculated.

#### Call

EnS_EEm_Calc is called in a cyclic interrupt OB.

You configure EnS_EEm_Calc using the [EnS_EEm_typeConfig](#ens_eem_typeconfig-configuration-data-for-a-machine) and [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) PLC data types.

#### Startup

The parameters of the following PLC data types are retentive:

- [EnS_EEm_typeConfig](#ens_eem_typeconfig-configuration-data-for-a-machine)
- [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point)
- [EnS_EEm_typeOperation](#ens_eem_typeoperation-operating-data-for-a-machine)
- [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point)

The values of the parameters are retained after a power failure and after each change of the operating mode of the CPU from STOP to RUN.

#### Behavior in case of error

When an error occurs, the output parameter error = TRUE is set. The [status](#parameter-status) parameter contains additional error information.

### EnS_EEm_Calc operating principle

#### Normalization of the input data

The EnS_EEm_Calc instruction calculates the input data from an energy counter value or a power value to a normalized energy counter value.

The input data is normalized for all measuring points simultaneously each time the instruction is called.

EnS_EEm_Calc reads the input data from the following data areas of the CPU:

- I/O area
- DB area
- PLC tags

The following modes for normalizing the input data are available:

**Normalization of the energy counter value**

EnS_EEm_Calc uses the overflowCntValue parameter to check whether a counter value overflow has occurred. Then EnS_EEm_Calc multiplies the input value with the value of the normFactor parameter of the [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) PLC data type.

Example:

A measuring instrument supplies the effective energy counter value of the LREAL data type with the counter overflow of 10<sup>12 </sup> set in the hardware configuration with the Wh unit. The counter runs from 0.0 to 999999999999.9. The value at the normFactor parameter is 0.001. EnS_EEm_Calc provides the effective energy value in kWh units.

**Normalization of the power value**

EnS_EEm_Calc normalizes the input value with the values of the following parameters of the [EnS_EEm_type2ActualValue](#ens_eem_type2actualvalue-parameters-for-power-value-input-signal) PLC data type:

- rawLow
- rawHigh
- outLow
- outHigh

Then EnS_EEm_Calc calculates the input value to a consumption value.

Example:

A measuring instrument provides an analog value between 1 V and 10 V. Whereby "1 V" corresponds to 0.0 l/h and "10 V" to 100.0 l/min.

The parameters have the following values:

- rawLow: 1.0
- rawHigh: 10.0
- outLow: 0.0
- outHigh: 100.0

  ![Normalization of the input data](images/102342577675_DV_resource.Stream@PNG-de-DE.png)

EnS_EEm_Calc calculates the Input input value to a normalized Output value with the l/h unit according to the formula:

![Normalization of the input data](images/105039197579_DV_resource.Stream@PNG-de-DE.png)

Depending on the cycle time in which EnS_EEm_Calc is called, EnS_EEm_Calc calculates the normalized energy counter value from the power value.

For a cycle time of 100 ms, EnS_EEm_Calc calculates the energy counter value according to the following formula:

![Normalization of the input data](images/102343386891_DV_resource.Stream@PNG-de-DE.png)

You can find additional information about analog value processing in the [Siemens Industry Online Support](https://support.industry.siemens.com/cs/ww/en/view/67989094).

#### Determining the energy efficiency

The EnS_EEm_Calc instruction calculates the average value of the power for each operating state of the machine. Up to eight operating states of the machine can be configured.

In addition, EnS_EEm_Calc calculates the energy consumption per unit for the configured operating states of the machine.

#### Configuration of the operating states

The following table shows the assignment of the respective bits of the value at the maskEnPI parameter of the [EnS_EEm_typeOperation](#ens_eem_typeoperation-operating-data-for-a-machine) PLC data type to the operating states of the machine:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| **Operating state** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | - | - | - | - | - | - | - |

If you want to display the resource consumption per unit, it is possible to use bit 0 but not useful. You can use the eStateName[0] parameter, for example, for conversion processes, evaluations and repairs. The eStateName[0] parameter is a collector of all operating states except 1 to 8. 16#01FE is required for acquiring the operating states 1 to 8. A .maskEnPI from 00C4 (bit 7, 6, 2 to 1), for example, means that the energy values of states of eStateName[2], eStateName[6] and eStateName[7] are included in the calculation of .out.energyPerItem.

### EnS_EEm_Calc parameter

The following table shows the parameters of the "EnS_EEm_Calc" block:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| error | BOOL | FALSE | TRUE = An error is pending |
| status | WORD | - | [Error status information](#parameter-status) |
| machineConfiguration | EnS_EEm_typeMachineConfig | - | Configuration data of a machine |
| machineOperation | EnS_EEm_typeMachineOperation | - | Operating data of a machine |
| measValueConfiguration | ARRAY[*] of [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) | - | Configuration data of a measuring point |
| measValueOperation | ARRAY[*] of [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) | - | Operating data of a measuring point |

### Parameter status

The following table shows the error codes that are generated at the status output parameter when errors occur:

| Error code (W#16#...) | Description |
| --- | --- |
| 740A | After switching to the "Run" operating state, the device runs for 4 hours in a trial version. When the trial version expires, you must purchase a valid license. |
| 8401 | Invalid license number at the licenseKey parameter of the [EnS_EEm_typeConfig](#ens_eem_typeconfig-configuration-data-for-a-machine) PLC data type. |
| 8402 | The array sizes and limits of the [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) and [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) PLC data types do not match. |
| 8403 | Error in internal system function. |
| 8404 | The function is not called in a cyclic interrupt OB. Call the function in a cyclic interrupt OB (e.g. OB30). |
| 8410 | Invalid value at the inputType parameter of the [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) PLC data type. |
| 8411 | Invalid normalization factor at the normFactor parameter of the [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) PLC data type. (Valid value range: 0.0 ... 9999.0) |
| 8412 | Invalid overflow value at the overflowCntValue parameter of the EnS_EEm_typeMeasConfig PLC data type. (Valid value range: 0.0 ... 1.0e<sup>12</sup>) |
| 8413 | Invalid value on at least one of the following parameters of the EnS_EEm_typeMeasConfig PLC data type:  - type2ActualValue.rawLow - type2ActualValue.rawHigh - type2ActualValue.OutLow - type2ActualValue.OutLow |
| 8414 | Maximum duration of seven days for the calculation of the mean values has been exceeded. |

## EnS_EEm_Report: Create efficiency report as CSV file

This section contains information on the following topics:

- [EnS_EEm_Report description](#ens_eem_report-description)
- [EnS_EEm_Report operating principle](#ens_eem_report-operating-principle)
- [EnS_EEm_Report parameter](#ens_eem_report-parameter)
- [Parameter status](#parameter-status-1)

### EnS_EEm_Report description

#### Description

The EnS_EEm_Report instruction writes the data for the efficiency report to the data log on the SIMATIC memory card.

The data log is a CSV file with the following layout:

| Column | Name | Description |
| --- | --- | --- |
| 1 | seqNo | Sequential number assigned by EnS_EEm_Report |
| 2 | name | Name of the stored value |
| 3 | value | Stored value |

An efficiency report cannot be generated while the efficiency is being calculated.

#### Example

The following example shows the information provided by the "Machinexyz_20161117_01" data log:

- Machine information

  - Name
  - Type
  - License key
  - Manufacturer
  - Operating state 1 to 8
- Measuring point information

  - Start date and time of reference test in UTC format
  - Duration of the reference test
  - Time zone of the reference test
  - Start date and time of acceptance test in UTC format
  - Duration of the acceptance test
  - Time zone of the acceptance test
- Measured value information for each measuring point

  - Name
  - Unit
  - Medium
  - Power value for reference value of operating states 1 to 8
  - Power value for the current value of the operating states 1 to 8

#### Call

EnS_EEm_Report is called as a single instance in a cyclic interrupt OB.

You can start up EnS_EEm_Report via a watch table of the user program in the CPU or HMI.

#### Startup

EnS_EEm_Report has no special startup characteristics.

#### Behavior in case of error

When an error occurs, the output parameter error = TRUE is set. The [status](#parameter-status-1) parameter contains additional error information.

### EnS_EEm_Report operating principle

#### Write data log

EnS_EEm_Report reads the data sequentially, converts the data into the STRING data type and writes the data to the data log. Data conversion in the STRING data type and writing data to the data log is edge-triggered.

EnS_EEm_Report starts writing the data to the data log if the following conditions are fulfilled:

- Rising edge at the request input parameter of the EnS_EEm_Report block
- The parameter outputValuesRelease = TRUE of the [EnS_EEm_typeStatOperation](#ens_eem_typestatoperation-static-parameters-for-a-machine) PLC data type

The writing speed of the data varies depending on the following factors:

- The employed PLC and SIMATIC memory card
- Storage location of the data on the SIMATIC memory card
- Size and number of the data log (CSV file) on the SIMATIC memory card
- Parallel access of the Web server to a data log

### EnS_EEm_Report parameter

The following table shows the parameters of the "EnS_EEm_Report" block:

| Parameter | Data type | Default | Description | HMI<sup>1)</sup> |
| --- | --- | --- | --- | --- |
| request | BOOL | FALSE | TRUE = Request for acceptance test report | x |
| busy | BOOL | - | TRUE = Data log is created | x |
| done | BOOL | - | TRUE = Data successfully written to the data log | x |
| error | BOOL | - | TRUE = An error is pending | x |
| status | WORD | - | [Error status information](#parameter-status-1) | x |
| dataLogNameAct | STRING[35] | - | Name of the currently active data log | x |
| machineConfiguration | [EnS_EEm_typeConfig](#ens_eem_typeconfig-configuration-data-for-a-machine) | - | Configuration data of the machine | - |
| machineOperation | [EnS_EEm_typeOperation](#ens_eem_typeoperation-operating-data-for-a-machine) | - | Operating data of the machine | - |
| measValueConfiguration | ARRAY[*] of [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) | - | Configuration data of the measuring point | - |
| measValueOperation | ARRAY[*] of [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) | - | Operating data of the measuring point | - |

<sup>1)</sup> The selected parameters are assigned the system attribute "Available for HMI" and "Visible in HMI". These parameters are used to exchange data with a SCADA system.

### Parameter status

The following table shows the error codes that are generated at the status output parameter when errors occur:

| Error code (W#16#...) | Description |
| --- | --- |
| 8001 | Error creating data log  If the statStatusDataLogCreate parameter = 0, the maximum number of data logs created per day has been reached. |
| 8002 | Error opening data log |
| 8003 | Error writing data to the data log |
| 8004 | Error closing data log |
| 8011 | Invalid values in:  - Configuration data at the measValueConfiguration parameter   or   - Operating data at the measValueOperation parameter |
| 8012 | Invalid value at the machineConfiguration.name parameter |

## PLC data types (UDTs)

This section contains information on the following topics:

- [EnS_EEm_typeConfig: Configuration data for a machine](#ens_eem_typeconfig-configuration-data-for-a-machine)
- [EnS_EEm_typeOperation: Operating data for a machine](#ens_eem_typeoperation-operating-data-for-a-machine)
- [EnS_EEm_typeMeasConfig: Configuration data for a measuring point](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point)
- [EnS_EEm_typeMeasOperation: Operating data for a measuring point](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point)
- [EnS_EEm_type1Counter: Parameters for energy counter value input signal](#ens_eem_type1counter-parameters-for-energy-counter-value-input-signal)
- [EnS_EEm_type2ActualValue: Parameters for power value input signal](#ens_eem_type2actualvalue-parameters-for-power-value-input-signal)
- [EnS_EEm_typeStatOperation: Static parameters for a machine](#ens_eem_typestatoperation-static-parameters-for-a-machine)
- [EnS_EEm_typeInMeasOperation: Input parameters for a measuring point](#ens_eem_typeinmeasoperation-input-parameters-for-a-measuring-point)
- [EnS_EEm_typeOutMeasOperation: Output parameters for a measuring point](#ens_eem_typeoutmeasoperation-output-parameters-for-a-measuring-point)
- [EnS_EEm_typeStatMeasOperation: Static parameters for a measuring point](#ens_eem_typestatmeasoperation-static-parameters-for-a-measuring-point)
- [EnS_EEm_typeReportData: Data for efficiency report](#ens_eem_typereportdata-data-for-efficiency-report)

### EnS_EEm_typeConfig: Configuration data for a machine

#### Description

Data and information of the machine can be configured in the EnS_EEm_typeConfig PLC data type.

> **Note**
>
> The values can only be changed in the start values of the data block in offline mode.

#### Configuration

The following table shows the parameters of the EnS_EEm_typeConfig PLC data type:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| name | STRING[30] | Default_Machine | Unique name of the machine |
| type | STRING[30] | Default_Type | Type of machine |
| serialNumber | STRING[30] | Default_Serial_Number | Serial number of the machine |
| manufacturer | STRING[30] | Default_Manufacturer | Name of manufacturer of machine |
| licenseKey | STRING[20] | EnterValidLicense | 20-digit license number of the energy object certificate |
| pieceOverflowCntValue | LREAL | 0.0 | Overflow value of the production counter value |
| eStateName | ARRAY[0..8] of STRING[14] | - | Operating states of the machine  Permissible value range: 0 ... 8 |
| eStateName[0] | STRING[14] | Undefined | Collectors of all operating states except 1 ... 8 |
| eStateName[1] | STRING[14] | Off | Name of operating state 1 of the machine |
| eStateName[2] | STRING[14] | Standby | Name of operating state 2 of the machine |
| eStateName[3] | STRING[14] | Operational | Name of operating state 3 of the machine |
| eStateName[4] | STRING[14] | Working | Name of operating state 4 of the machine |
| eStateName[5] | STRING[14] | Powering Up | Name of operating state 5 of the machine |
| eStateName[6] | STRING[14] | Powering Down | Name of operating state 6 of the machine |
| eStateName[7] | STRING[14] | UserDefined1 | Name of operating state 7 of the machine |
| eStateName[8] | STRING[14] | UserDefined2 | Name of operating state 8 of the machine |
| additionalInfoDescription | ARRAY[0..3] of STRING[18] | - | Additional information (e.g. name, type, serial number) |
| additionalInfoDescription[0] | STRING[18] | additional Info1 | Additional information (e.g. name, type, serial number) |
| additionalInfoDescription[1] | STRING[18] | additional Info2 | Additional information (e.g. name, type, serial number) |
| additionalInfoDescription[2] | STRING[18] | additional Info3 | Additional information (e.g. name, type, serial number) |
| additionalInfoDescription[3] | STRING[18] | additional Info4 | Additional information (e.g. name, type, serial number) |

### EnS_EEm_typeOperation: Operating data for a machine

#### Description

The EnE_EEm_typeOperation PLC data type contains dynamic information on the machine and is used to exchange data between the energy efficiency blocks.

#### Configuration

The following table shows the parameters of the EnS_EEm_typeOperation PLC data type:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| pieceCounter | LREAL | 0.0 | Production counter value |
| additionalInformation | ARRAY[0..3] of STRING[30] | - | Additional information |
| additionalInformation[0] | ARRAY[0..3] of STRING[30] | Product | Additional information |
| additionalInformation[1] | ARRAY[0..3] of STRING[30] | Product Variant | Additional information |
| additionalInformation[2] | ARRAY[0..3] of STRING[30] | Material | Additional information |
| additionalInformation[3] | ARRAY[0..3] of STRING[30] | Batch No. | Additional information |
| eState | USINT | 0 | Index of the operating state of the machine currently in effect |
| maskEnPI | WORD | 16#0 | Mask for calculation of the energy consumption per piece |
| triggerRecalcOutput | BOOL | FALSE | A rising edge updates the energy counter values at the output |
| resetMeasErrors | BOOL | FALSE | A rising edge resets the error codes of measuring points |
| globalResetEnergyCounter | BOOL | FALSE | A rising edge resets the energy counter value |
| globalResetAvgValues | BOOL | FALSE | A rising edge resets the average values |
| globalResetEnergyPerItem | BOOL | FALSE | A rising edge reduces the energy consumption per unit |
| startAvgCalcPeriod | BOOL | FALSE | A rising edge starts the calculation of the average values |
| stopAvgCalcPeriod | BOOL | FALSE | A rising edge stops the calculation of the average values |
| setAvgCalcRef | BOOL | FALSE | TRUE = Set the calculated average value as a reference |
| stat | [EnS_EEm_typeStatOperation](#ens_eem_typestatoperation-static-parameters-for-a-machine) | - | System-internal |

### EnS_EEm_typeMeasConfig: Configuration data for a measuring point

#### Configuration data for a measuring point

The EnS_EEm_typeMeasConfig PLC data type contains values and information of a measuring point.

The size of the array of the EnS_EEm_typeMeasConfig data type defines the number of measuring points in a machine.

> **Note**
>
> The values can only be changed in the start values of the data block in offline mode.

#### Configuration

The following table shows the parameters of the EnS_EEm_typeMeasConfig PLC data type:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| name | STRING[30] | Electrical Infeed | Name of the measuring point |
| nameShort | STRING[4] | EL01 | Abbreviation for the name of the measuring point |
| media | STRING[30] | - | Name of the medium |
| unitCounterNumber | INT | 0 | Enumeration of the counter value unit |
| unitCounterText | STRING[6] | - | Name of the counter value unit |
| unitActValueNumber | INT | 0 | Enumeration of the power value unit |
| unitActValueText | STRING[6] | - | Name of the power value unit |
| inputType | INT | 0 | Type of input signal  - inputType = 1: Energy counter value    If inputType = 1, you only have to edit the type1Counter parameter. - inputType = 2: Power value    If inputType = 2, you only have to edit the type2ActValue parameter. |
| type1Counter | [EnS_EEm_type1Counter](#ens_eem_type1counter-parameters-for-energy-counter-value-input-signal) | - | Parameters for the energy counter value input signal |
| type2ActValue | [EnS_EEm_type2ActualValue](#ens_eem_type2actualvalue-parameters-for-power-value-input-signal) | - | Parameters for the power value input signal |

### EnS_EEm_typeMeasOperation: Operating data for a measuring point

#### Operating data for a measuring point

The EnS_EEm_typeMeasOperation PLC data type contains the operating data of the measuring point and has the following purposes:

- Provision of the operational state-related values at the output
- Data exchange between the energy efficiency blocks

The size of the array of the EnS_EEm_typeMeasOperation data type defines the number of measuring points in a machine.

#### Configuration

The following table shows the parameters of the EnS_EEm_typeMeasOperation PLC data type:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| in | [EnS_EEm_typeInMeasOperation](#ens_eem_typeinmeasoperation-input-parameters-for-a-measuring-point) | - | Input parameters for a measuring point |
| out | [EnS_EEm_typeOutMeasOperation](#ens_eem_typeoutmeasoperation-output-parameters-for-a-measuring-point) | - | Output parameters for a measuring point |
| stat | [EnS_EEm_typeStatMeasOperation](#ens_eem_typestatmeasoperation-static-parameters-for-a-measuring-point) | - | System-internal |

### EnS_EEm_type1Counter: Parameters for energy counter value input signal

#### Description

You use the EnS_EEm_type1Counter PLC data type to configure the acquisition of the energy counter value in the [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) PLC data type.

#### Configuration

The following table shows the parameters of the EnS_EEm_type1Counter PLC data type:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| overflowCntValue | LREAL | 0.0 | Overflow value of the energy counter value |
| normFactor | LREAL | 0.0 | Normalization factor of the energy counter value |

### EnS_EEm_type2ActualValue: Parameters for power value input signal

#### Description

You use the EnS_EEm_type2ActualValue PLC data type to configure the acquisition of the power value in the [EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point) PLC data type.

#### Configuration

The following table shows the parameters of the EnS_EEm_type2ActualValue PLC data type:

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| rawLow | REAL | 0.0 | Low limit for the input value |
| rawHigh | REAL | 100.0 | High limit for the input value |
| outLow | REAL | 0.0 | Low limit for the output value |
| outHigh | REAL | 100.0 | High limit for the output value |

### EnS_EEm_typeStatOperation: Static parameters for a machine

#### Description

The EnS_EEm_typeStatOperation PLC data type of the [EnS_EEm_typeOperation](#ens_eem_typeoperation-operating-data-for-a-machine) PLC data type is used for system-internal operation of the EnS_EEm_Calc block.

The EnS_EEm_typeStatOperation PLC data type cannot be changed and is not relevant for the user.

---

**See also**

[EnS_EEm_typeMeasConfig: Configuration data for a measuring point](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point)
  
[EnS_EEm_typeMeasOperation: Operating data for a measuring point](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point)

### EnS_EEm_typeInMeasOperation: Input parameters for a measuring point

#### Input parameters for a measuring point

The EnS_EEm_typeInMeasOperation PLC data type provides the input parameter for a measuring point in the [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) PLC data type.

#### Configuration

The following table shows the parameters of the EnS_EEm_typeInMeasOperation PLC data type:

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| counterValue | LREAL | 0.0 | Energy counter value |
| actValue | REAL | 0.0 | Power value |

### EnS_EEm_typeOutMeasOperation: Output parameters for a measuring point

#### Output parameters for a measuring point

The EnS_EEm_typeOutMeasOperation PLC data type provides the output parameter for a measuring point in the [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) PLC data type.

#### Configuration

The following table shows the parameters of the EnS_EEm_typeOutMeasOperation PLC data type:

| Parameters | Data type | Default | Description |
| --- | --- | --- | --- |
| avgValue | ARRAY[0..8] of REAL | - | Average values of the power during the calculation period |
| refValue | ARRAY[0..8] of REAL | - | Reference values |
| differencePercent | ARRAY[0..8] of REAL | - | Difference of the average values to reference values in percent |
| energyCounter | ARRAY[0..8] of LREAL | - | Energy counter values |
| energyCounterTotal | LREAL | 0.0 | Energy counter value of all energy counter values |
| error | BOOL | FALSE | TRUE = An error is pending in the settings of the measuring point |
| energyPerItem | REAL | 0.0 | Energy consumption per piece |

### EnS_EEm_typeStatMeasOperation: Static parameters for a measuring point

#### Description

The EnS_EEm_typeStatMeasOperation PLC data type of the [EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point) PLC data type is used for system-internal operation of the EnS_EEm_Calc block.

The EnS_EEm_typeStatMeasOperation PLC data type cannot be changed and is not relevant for the user.

### EnS_EEm_typeReportData: Data for efficiency report

#### Description

The EnS_EEm_typeReportData PLC data type in the EnS_EEm_Report is used as a system-internal interface for data exchange.

#### Configuration

The table below shows the parameters of the EnS_EEm_typeReportData PLC data type:

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| name | STRING[14] | - | Parameter name |
| value | STRING[30] | - | Parameter value |

## Program example

### Introduction

In the following example you configure the FC "EnS_EEm_Calc" and the FB "EnS_EEm_Report" in a CPU S7-1500.

### Requirements

- CPU SIMATIC S7-1500 has been created.
- Cyclic interrupt OB (OB30) has been created.
- Global data block or function block for creating the PLC data types/tags has been created.

### Calling FB "EnS_EEm_Calc" and FC "EnS_EEm_Report"

You can call the FB "EnS_EEm_Calc" and the FC "EnS_EEm_Report" in a cyclic interrupt OB. Drag the FC "EnS_EEm_Calc" and the FB "EnS_EEm_Report" from the option packages of the Energy Suite extension into the network.

![Calling FB "EnS_EEm_Calc" and FC "EnS_EEm_Report"](images/114328542731_DV_resource.Stream@PNG-en-US.png)

### Creating PLC data types

The FC "EnS_EEm_Calc" and the FB "EnS_EEm_Report" are configured via the following PLC data types/tags:

- EnS_EEm_typeConfig
- EnS_EEm_typeOperation
- EnS_EEm_tpyeMeasConfig
- EnS_EEm_typeMeasOperation

For FC "EnS_EEm_Calc" you must also create and interconnect the following tags:

- Error (Bool)
- Status (Word)

In this example, the PLC data types/tags are created in a global data block.

![Creating PLC data types](images/114309768075_DV_resource.Stream@PNG-en-US.png)

### Assigning parameters for the "EnS_EEm_typeConfig" tag

The "EnS_EEm_typeMeasConfig" tag is used for general machine configuration. The following figure shows the parameter assignment of the data type "[EnS_EEm_typeConfig](#ens_eem_typeconfig-configuration-data-for-a-machine)":

![Assigning parameters for the "EnS_EEm_typeConfig" tag](images/114301512075_DV_resource.Stream@PNG-en-US.png)

Enter your license key in the "licenseKey" tag. Without a valid license, the block only runs for 4 hours in a trial version. A valid license for the energy efficiency monitor is available from the[Siemens Industry Mall](https://mall.industry.siemens.com/mall/de/WW/Catalog/Search?searchTerm=6AV2108-1CF00-0BB0&tab=Product
// XmlEditor.InternalXmlClipboard:b2232a42-4ccc-7ee8-2958-f6d799fce7af).

Enter the name of the operating state of the machine "eStateName" tag array. For example, if the tag has the value 1, the machine is in the "Off" operating state. Production status 0 is not used.

For more information on the "EnS_EEm_typeConfig" data type, refer to the section [PLC Data Types (UDTs)](#ens_eem_typeconfig-configuration-data-for-a-machine).

### "EnS_EEm_typeOperation" tag

The "EnS_EEm_typeOperation" tag is used for general machine control. The following figure shows the view of the data type "[EnS_EEm_typeOperation](#ens_eem_typeoperation-operating-data-for-a-machine)" data type:

!["EnS_EEm_typeOperation" tag](images/114309329163_DV_resource.Stream@PNG-en-US.png)

The following PLC tags are used to control the reference and current measurements:

- "startAvgCalcPeriod"
- "stopAvgCalcPeriod"
- "setAvgCalcRef"

To start a reference or current measurement, set the tags as follows:

- For a reference measurement: "setAvgCalcRef" = TRUE, "startAvgCalcPeriod" = TRUE (positive edge)
- For a current measurement: "setAvgCalcRef" = FALSE, "startAvgCalcPeriod" = TRUE (positive edge)
- To stop a measurement: "stopAvgCalcPeriod" = TRUE (positive edge)

For more information on the "EnS_EEm_typeOperation" data type, refer to the section [PLC Data Types (UDTs)](#ens_eem_typeoperation-operating-data-for-a-machine).

### Assigning parameters for the "EnS_EEm_typeMeasConfig" tag

The "EnS_EEm_typeMeasConfig" tag is used for general measuring point configuration. The following figure shows the parameter assignment of the data type "[EnS_EEm_typeMeasConfig](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point)":

![Assigning parameters for the "EnS_EEm_typeMeasConfig" tag](images/114309632139_DV_resource.Stream@PNG-en-US.png)

You can interconnect up to 10 measuring points to the efficiency monitor. Each array element from "Array[0...3] of EnS_EEm_typeMeasConfig" represents a measuring point.

> **Note**
>
> **Array size EnS_EEm_typeMeasConfig and EnS_EEm_typeMeasOperation**
>
> The size of the two array elements "EnS_EEm_typeMeasConfig" and "EnS_EEm_typeMeasOperation" must be the same.

In the "inputType" tag you can specify whether a count value or a current value is recorded from the measuring point. For example, when you enter a count value, enter "1" as the start value for the "inputType" parameter. Then, under "type1Counter", enter the overflow value of the energy count in the "overflowCntValue" parameter and the normalization factor of the energy count in the "normFactor" parameter. For example, when you enter a current value, enter "2" as the start value for the "inputType" parameter. Enter the values for the respective parameters under "type2ActValue" accordingly.

For more information on the "EnS_EEm_typeMeasConfig" data type, refer to the section [PLC Data Types (UDTs)](#ens_eem_typemeasconfig-configuration-data-for-a-measuring-point).

### Assigning parameters for the "EnS_EEm_typeMeasOperation" tag

The "EnS_EEm_typeMeasOperation" tag provides the result of the energy efficiency monitor. The following figure shows the parameter assignment of the data type "[EnS_EEm_typeMeasOperation](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point)":

![Assigning parameters for the "EnS_EEm_typeMeasOperation" tag](images/114309640715_DV_resource.Stream@PNG-en-US.png)

Depending on the "inputType", the counter value or actual value is read in from the energy program under the "in" tags. The measurement evaluation is displayed under the "out" tags. The following evaluations are calculated:

- "avgValue": Result of the current measurement per operating state
- "refValue": Result of the reference measurement per operating state
- "differencePercent": Percentage difference between reference and current value per operating state
- "energyCounter": Result of count values per status
- "energyCounterTotal": Result of the total counter

  > **Note**
  >
  > **Updating the counter value**
  >
  > The counter value of the total counter is only updated after a status change.
- "energyPerItem": Result of the energy consumption per unit produced

  > **Note**
  >
  > **Updating the value**
  >
  > The value of the energy consumption per piece produced is only updated after a change in the workpiece counter.

For more information on the "EnS_EEm_typeMeasOperation" data type, refer to the section [PLC Data Types (UDTs)](#ens_eem_typemeasoperation-operating-data-for-a-measuring-point).

### Interconnecting PLC data types/tags with the blocks

After you have created and parameterized the data types, connect the data types to the corresponding inputs and outputs at the blocks. To do this, click in the navigation on the global data block with the PLC data types contained there. In the details view you can see a list of the existing PLC data types:

![Interconnecting PLC data types/tags with the blocks](images/114316931851_DV_resource.Stream@PNG-en-US.png)

Drag the blue icon of the data type to the corresponding position of the block. If you move the cursor over the corresponding position, the position is highlighted in green:

![Interconnecting PLC data types/tags with the blocks](images/114318182027_DV_resource.Stream@PNG-de-DE.png)

Insert the data type in the appropriate position:

![Interconnecting PLC data types/tags with the blocks](images/114318190603_DV_resource.Stream@PNG-de-DE.png)

Use the same procedure to insert the remaining data types in the correct position, both for FC "EnS_EEm_Calc" and for FB "EnS_EEm_Report". If a data type has been incorrectly created or the parameter assignment of the data types is incomplete or incorrect, the corresponding data type is highlighted in red.

The following figure shows the correct configuration of the FC "EnS_EEm_Calc":

![Interconnecting PLC data types/tags with the blocks](images/114318480779_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the correct configuration of the FB "EnS_EEm_Report":

![Interconnecting PLC data types/tags with the blocks](images/114319026955_DV_resource.Stream@PNG-de-DE.png)

You can create a report using the "request" tag. You can check the status of the FB via the tags "busy", "done" and "error".

### Result

The blocks are fully configured. You can then use the blocks in your energy program and operate them via a user program watch table in the CPU or HMI.
