---
title: "SINAMICS S200 parameters"
package: StdrInfSysOptParaSinaS200enUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS S200 parameters

This section contains information on the following topics:

- [Explanation of the parameter information](#explanation-of-the-parameter-information)
- [SINAMICS S200 Basic PN parameters](SINAMICS%20Parameter%20S200%20Basic%20PN.md#sinamics-parameter-s200-basic-pn)
- [SINAMICS S200 PN parameters](SINAMICS%20Parameter%20S200%20PN.md#sinamics-parameter-s200-pn)

## Explanation of the parameter information

Parameters are displayed according to the following example. As a maximum, the description of a parameter includes the information listed below. Depending on the specific parameter, some of the listed information is not applicable.

### Example

![Example](images/163074956939_DV_resource.Stream@PNG-en-US.png)

### Parameter number (rxxxx)

The parameter number is composed of a preceding "p", "r" or "c", several digits, and optionally the index and optionally the bit array.

The parameter number has the following syntax: pxxxx[0...n], rxxxx[0...n], cxxxx[0...n], pxxxx.0...15 or rxxxx.0...15, cxxxx.0...15, pxxxx[0...n].0...15 or rxxxx[0...n].0...15, cxxxx[0...n].0...15.

Examples for representation in the parameter list:

| Symbol | Meaning |
| --- | --- |
| - p... | Adjustable parameters (read and write parameters) |
| - r... | Display parameters (read-only) |
| - c... | Display parameters (read-only) |
| - p0972 | Adjustable parameter 972 |
| - p0489[0...2] | Adjustable parameter 489 index 0 to 2 |
| - r0945 | Display parameter 945 |
| - r0196[0...255].4...15 | Display parameter with index 0 to 255 and bit array bit 0 to bit 15 |
| - r5613.0...1 | Display parameter 5613 with bit array from bit 0 to bit 1 |
| - c8997[0...2] | Display parameter 8997 index 0 to 2 |
| Other examples of the notation in the documentation: |  |
| - p9563[1] | Adjustable parameter 9563 index 1 |
| - r0196[1].5 | Display parameter 196 index 1 bit 5 |
| - r0964[2] | Display parameter 964 index 2 |
| - p5611.1 | Adjustable parameter 5611 bit 1 |

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

You can change the quantity of displayed parameters in the commissioning tools via:

- Standard display  
  Only the basic parameters are displayed.
- Extended display  
  The full range of parameters is displayed.

### Rights

User management and access control (UMAC) regulates access to the parameters.

Function rights regulate access to individual areas in the commissioning tool used. The following function rights can be distinguished:

- Engineering function rights

  Are required for offline configuration in the Startdrive project. However, in addition to the runtime function rights, they are also checked when accessing the protected drive online.
- Runtime function rights

  Are required for online access from Startdrive to a protected drive.

Function rights are bundled into roles. These roles can then be assigned to individual user accounts.

For space reasons, only runtime function rights are listed in the parameter description.

Detailed information about user administration and access control and especially about function rights can be found on the following help page: Access control

### Changeable in operating state

A parameter can only be changed in this operating state. The change becomes effective only after exiting the state.  
The following states exist:

- Operation  
  The pulses are enabled.
- Ready  
  The pulses are not enabled and the "Device commissioning" or "Drive object commissioning" state is not active.
- Device commissioning  
  Device commissioning is performed.  
  The pulses cannot be enabled.
- Drive object commissioning  
  Drive object commissioning is performed.  
  The pulses cannot be enabled.

### Parameter group

A parameter group contains parameters that are functionally associated with one another.

### Unit

Shows the default unit of the parameter. For adjustable parameters, the unit is additionally specified according to the values (min, max, factory setting) in square brackets.

### Min, Max, Factory setting

The parameter value when shipped is specified under "Factory setting" with the relevant unit in square parentheses.

The value can be changed within the range defined by "Min" and "Max".

This information is not applicable for display parameters.

| Symbol | Meaning |
| --- | --- |
| Min | Minimum value of the parameter [unit] |
| Max | Maximum value of the parameter [unit] |
| Factory setting | Value when delivered [unit] |

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

  The adjustment range and unit apply to all indices.
- Factory setting:

  When all indices have the same factory setting, index 0 is specified with the unit to represent all indices.

  When the indices have different factory settings, they are all listed individually with the unit.

### Bit array

For parameters with bit arrays, the following information is provided for each bit:

- Bit number and signal name
- Meaning when signal state is 1 and 0

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
