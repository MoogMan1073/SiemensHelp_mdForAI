---
title: "SINAMICS G220 parameters"
package: StdrInfSysOptParaSinaG220enUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS G220 parameters

This section contains information on the following topics:

- [Explanation of the parameter information](#explanation-of-the-parameter-information)
- [SINAMICS G220 parameters](SINAMICS%20Parameter%20G220.md#sinamics-parameter-g220)
- [SINAMICS G220 Clean Power parameters](SINAMICS%20Parameter%20G220%20Clean%20Power.md#sinamics-parameter-g220-clean-power)

## Explanation of the parameter information

Parameters are displayed according to the following example. As a maximum, the description of a parameter includes the information listed below. Depending on the specific parameter, some of the listed information is not applicable.

### Example

![Example](images/155972802571_DV_resource.Stream@PNG-en-US.png)

### Parameter number (rxxxx)

The parameter number is made up of a "p", "r" or "c", followed by several digits and optionally the index or bit array. A parameter number has the following syntax: pxxxx[0...n], rxxxx[0...n], pxxxx.0...15 or rxxxx.0...15.

For parameters with index and bit array, only the index field is added to the parameter number.

Examples for representation in the parameter list:

| Symbol | Meaning |
| --- | --- |
| - p... | Adjustable parameters (read and write parameters) |
| - r... | Display parameters (read-only) |
| - c... | Interconnection parameters (can be interconnected)  Allows an interconnection to be established between a signal source and a signal sink. Possible signal sinks are marked with the prefix "c". |
| - p0972 | Adjustable parameter 972 |
| - p0089[0...2] | Adjustable parameter 89 indices 0 to 2 |
| - p1001[0...n] | Adjustable parameter 1001, indices 0 to n (n = configurable) |
| - r0944 | Display parameter 944 |
| - r2139.0...15 | Display parameter 2139 with bit array from bit 0 to bit 15 |
| Other examples of the notation in the documentation: |  |
| - p1213[1] | Adjustable parameter 1213 index 1 |
| - p1151[1].2 | Adjustable parameter 1151, index 1 bit 2 |
| - r0945[2] | Display parameter 945, index 2 |
| - c0771[0] | Interconnection parameter 771, index 0 |
| - p0795.4 | Adjustable parameter 795, bit 4 |

### Parameter name / Short parameter name

Shows the parameter name in the long form and separated by a slash, in the short form.

### Variant

Specifies the product variant for which the parameter is valid. This information is not applicable if a parameter is the same for all product variants used in the parameter list.

### Data type

Each parameter is assigned one of the following data types:

|  |  |  |
| --- | --- | --- |
| - Integer8 | I8 | 8-bit integer |
| - Integer16 | I16 | 16-bit integer number |
| - Integer32 | I32 | 32-bit integer number |
| - Unsigned8 | U8 | 8 bit without sign |
| - Unsigned16 | U16 | 16 bit without sign |
| - Unsigned32 | U32 | 32 bit without sign |
| - FloatingPoint32 | Float | 32-bit floating-point number |

### Visible in

You change the number of parameters displayed in the parameter view via:

- Standard display  
  Only the basis parameters are displayed.
- Extended display  
  The full scope of parameters is displayed.

### Parameter group

A parameter group contains parameters that are functionally associated with one another.

### Not for motor type

This parameter has no significance for the specified motor types.

### Dynamic index

For parameters with a dynamic index [0 to n], the following information is specified:

- Data set
- Parameter specifying the number of indices (n = number - 1).

Example: **Dyn. Index [0…n]:** MDS n defined by: p0130

**Data set types**

- CDS (command data set)
- DDS (drive data set)
- EDS (encoder data set)
- MDS (motor data set)
- PDS (power data set)

You create and delete data sets in the commissioning tool.

### Calculated

Parameters, which are influenced by automatic calculations, are marked "automatic".

### Unit

Shows the default unit of the parameter. For adjustable parameters, the unit is additionally specified according to the values (min, max, factory setting) in square brackets.

### Unit group and unit selection

Depending on the selection of the standard, a different unit is shown for the power data of the converter and motor. As a consequence, the unit is switched over for some parameters.

The "Unit selection" shows for which parameter the unit is changed.

The units for the different standards are stored in unit groups.

Example:

Unit group: 14_6, unit selection: p0100

The parameter belongs to unit group 14_6, and the unit is switched over using p0100.

All available unit groups and possible unit selections are listed below.

Unit groups (p0100)

| Unit group | Unit selection for p0100 = |  | Reference value for % |
| --- | --- | --- | --- |
| 0, 2 | 1 |  |  |
| 7_4 | Nm | lbf ft | - |
| 8_4 | N | lbf | - |
| 14_2 | W | W | - |
| 14_6 | kW | HP | - |
| 14_13 | W/A | HP/A | - |
| 14_14 | W min/1000 | HP min/1000 | - |
| 14_15 | W/A<sup>2</sup> | HP/A<sup>2</sup> | - |
| 14_16 | W min<sup>2</sup>/1000<sup>2</sup> | HP min<sup>2</sup>/1000<sup>2</sup> | - |
| 25_1 | kgm<sup>2</sup> | lb ft<sup>2</sup> | - |
| 27_1 | kg | lb | - |
| 28_1 | Nm/A | lbf ft/A | - |
| 29_1 | N/Arms | lbf/Arms | - |
| 30_1 | m | ft | - |
| 47_1 | kW s/K | HP s/K | - |
| 48_1 | W/K | HP/K | - |
| 48_2 | W min/1000 K | HP min/1000 K | - |
| 48_3 | W min<sup>2</sup>/1000<sup>2</sup> K | HP min<sup>2</sup>/1000<sup>2</sup> K | - |
| 50_1 | K/W | K/HP | - |

### Min, max, factory setting

The parameter value when shipped is specified under "Factory setting" with the relevant unit in square parentheses.

The value can be changed within the range defined by "Min" and "Max".

This information is not applicable for display parameters.

| Symbol | Meaning |
| --- | --- |
| Min | Minimum value of the parameter [unit] |
| Max | Maximum value of the parameter [unit] |
| Factory setting | Value when delivered [unit] |

### Signal interconnection

Interconnectable parameter types:

- Numerical signal source
- Binary signal source
- Numerical signal sink
- Binary signal sink

For parameters, type "Signal sink", the factory interconnection is also specified.

Interconnection possibilities for signal sinks:

- Fixed value
- Substitute value
- Parameter

When commissioned for the first time, or when restoring factory settings, it is possible that a value other than the factory interconnection is visible.

Only certain combinations are permitted when creating signal interconnections:

Possible combinations of signal interconnections

| Signal source parameter | Signal sink parameter |  |  |  |
| --- | --- | --- | --- | --- |
| Numerical sink |  |  | Binary sink |  |
| Integer16 | Integer32 | FloatingPoint32 | Binary |  |
| numerical: Unsigned8 | x | x | - | - |
| numerical: Unsigned16 | x | x | - | - |
| numerical: Integer16 | x | x | r2050 | - |
| numerical: Unsigned32 | x | x | - | - |
| numerical: Integer32 | x | x | r2060 | - |
| numerical: FloatingPoint32 | x | x | x | - |
| binary: Unsigned8 | . | . | - | x |
| binary: Unsigned16 | . | . | - | x |
| binary: Integer16 | . | . | - | x |
| binary: Unsigned32 | . | . | - | x |
| binary: Integer32 | . | . | - | x |
| x: Signal interconnection permitted  –: Signal interconnection not permitted  rxxxx: Signal interconnection only permitted for the specified source parameters |  |  |  |  |

### Scaling

Specifies the reference quantity, with which a signal value is automatically converted for a signal interconnection.

The following reference variables exist:

- p2000 … p2007: Reference speed, reference voltage, etc.
- PERCENT: 1.0 = 100 %
- 4000H: 4000 hex = 100 % (word) or 4000 0000 hex = 100 % (double word)

### Description

Explanation of the function of a parameter.

### Values

List of the possible values of a parameter.

### Recommendation

Information about recommended settings.

### Index

For each individual index, indexed parameters represent the name and its significance.

For the parameter values (min, max, factory setting), for the indexed adjustable parameters, the following applies:

- Min, Max:

  The setting range and unit apply to all indices.
- Factory setting:

  When all indices have the same factory setting, index 0 is specified with the unit to represent all indices.

  When the indices have different factory settings, they are all listed individually with the unit.

### Bit array

For parameters with bit arrays, the following information is provided for each bit:

- Bit number and signal name
- Meaning when signal state is 1 and 0
- Function diagram (optional)  
  The signal is shown in this function diagram.

### Dependency

Specification of interactions that this parameter can potentially have:

- Effects on other parameters
- Dependent on the parameter settings (dependent on the selected functions)
- List of other parameters to be considered
- List of faults and alarms to be considered

### Danger / Caution / Alarm / Notice

The relevant notes correspond to the warning note concept and contain the following information:

- Important information that must be observed to avoid the risk of physical injury or material damage.
- Information that must be observed to avoid any problems.
- Information that the user may find useful.

### Note

Additional explanations about parameters
