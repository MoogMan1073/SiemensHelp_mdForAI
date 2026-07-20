---
title: "Configuring AS-i devices"
package: HWCASienUS
topics: 12
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring AS-i devices

This section contains information on the following topics:

- [Digital addresses](#digital-addresses)
- [Network configuration of AS interface](#network-configuration-of-as-interface)
- [Scope of AS-i configuration](#scope-of-as-i-configuration)
- [AS-i motor starter parameters](#as-i-motor-starter-parameters)
- [AS-i master operating state](#as-i-master-operating-state)
- [AS-i master system default](#as-i-master-system-default)
- [I/O range](#io-range)
- [Reset CM 1243-2 AS-i master module to factory settings](#reset-cm-1243-2-as-i-master-module-to-factory-settings)

## Digital addresses

### Bit assignment

The bit assignment is determined from the IO code (I/O configuration) of the configured AS-i slave. The following table shows the bit assignment.

| IO code | Offset of the input bits |  |  |  | Offset of the output bits |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0.0 | 0.1 | 0.2 | 0.3 | 0.0 | 0.1 | 0.2 | 0.3 |
| 0 (EEEE) | IN1 | IN2 | IN3 | IN4 | - | - | - | - |
| 1 (EEE-) | IN1 | IN2 | IN3 | - | - | - | - | - |
| 2 (EEEE) | IN1 | IN2 | IN3 | IN4 | - | - | - | - |
| 3 (EEA-) | IN1 | IN2 | - | - | - | - | OUT1 | - |
| 4 (EEBE) | IN1 | IN2 | IN3 | IN4 | - | - | OUT1 | - |
| 5 (EAAA) | IN1 | - | - | - | - | OUT1 | OUT2 | OUT3 |
| 6 (BBBB) | IN1 | IN2 | IN3 | IN4 | OUT1 | OUT2 | OUT3 | OUT4 |
| 7 (BBBB) | IN1 | IN2 | IN3 | IN4 | OUT1 | OUT2 | OUT3 | OUT4 |
| 8 (AAAA) | - | - | - | - | OUT1 | OUT2 | OUT3 | OUT4 |
| 9 (AAAE) | - | - | - | IN1 | OUT1 | OUT2 | OUT3 | - |
| A (AAAB) | - | - | - | IN1 | OUT1 | OUT2 | OUT3 | OUT4 |
| B (AAEE) | - | - | IN1 | IN2 | OUT1 | OUT2 | - | - |
| C (AABB) | - | - | IN1 | IN2 | OUT1 | OUT2 | OUT3 | OUT4 |
| D (AEEE) | - | IN1 | IN2 | IN3 | OUT1 | - | - | - |
| E (ABBB) | - | IN1 | IN2 | IN3 | OUT1 | OUT2 | OUT3 | OUT4 |
| IN1 = first input of the AS-i slave, IN2 = second input of the AS-i slave, etc.  OUT1 = first output of the AS-i slave, OUT2 = second output of the AS-i slave, etc. |  |  |  |  |  |  |  |  |

> **Note**
>
> The labeling of the inputs and outputs on the AS-i slaves may differ from this illustration.
>
> For A/B slaves (with ID code = A), output bit offset 0.3 is not occupied. Exception: An A/B slave with 4 inputs and 4 outputs (IO code = 7, ID code = A) occupies all output bits.
>
> The actual address of the bit is calculated from the input and/or output address plus that of the offset given in this table.

### Example

Input address 100.0 and output address 200.4 have been set. The IO code of the slave has been set to "3 (EEA-)". The AS-i slave data then lies in the process image on input and/or output bits E100.0, E100.1 and A200.6.

## Network configuration of AS interface

AS-Interface consists of an AS-i master and AS-i slaves connected to each other over an AS-i subnet.

### Rules for AS interface network configuration

All the nodes in an AS-i subnet must have a different AS-i node address.

You should only load the settings over the network when all the modules in a subnet have different addresses and when the actual structure matches that of the network configuration you have created.

One AS-i master and up to 62 AS-i slaves can be operated on an AS-i subnet.

For more information on configuring an AS-Interface with an AS-i master and AS-i slaves, refer to the section on AS-Interface and the documentation of the AS-i master modules.

## Scope of AS-i configuration

The scope of AS-i configuration shows how the AS-i slaves are configured for the AS-i network of the master.

The selected scope of AS-i configuration switches over automatically if you connect one or more AS-i slaves from the hardware catalog to the AS-i master or delete all slaves.

When the scope of AS-i configuration is changed, the I/O addresses of the AS-i slaves can change.

The following options are available. (The functional scope can depend on the AS-i master.)

### **Scope of AS-i configuration: Basic configuration**

The "Basic configuration" option is selected if you configure the AS-i master in the hardware configuration, but do not connect any AS-i slaves to the AS-i master module in the project.

In this case, the AS-i master manages the AS-i slaves that are really present through the device memory of the master.

The digital I/O addresses of the slaves are distributed according to a fixed scheme in the process image.

Analog I/O addresses do not exist in the process image. If they are required, analog I/O data can be read/written via acyclic data set communication.

You can use the online functions in the TIA Portal or an (optional) button on the device to apply the real existing actual configuration of the AS-i slaves as the planned configuration in the device memory of the master and switch the master to "Protected mode". In protected mode, the master only activates the slaves configured in the device memory and generates a diagnostic interrupt in case of faulty slaves.

A graphical view is not possible in the network view of the TIA Portal because the slaves are not stored in the project.

Alternatively, you can switch the master to "Configuration mode" (CM) whereby all existing slaves are activated - without target-actual comparison - and no interrupts are generated in case of a slave failure.

### Scope of AS-i configuration: Configuration with AS-i network

The "Configuration with AS-i network" option is selected if you configure the AS-i master in the hardware configuration and connect one or more AS-i slaves in the project to the AS-i master module.

In this case, the AS-i master takes over the target specifications for expansion of the AS-i network from the TIA project.

The digital and analog I/O addresses of the slaves are individually defined in the TIA project. If they are required, analog I/O data can also be read/written via acyclic data set communication.

The TIA project contains the AS-i network and all AS-i slaves with their parameterization and documentation.

By using the hardware identification menu command, you can apply an existing actual configuration of the AS-i slaves to the hardware configuration of the project. After the download, the master automatically switches to "Protected mode" and activates only the configured slaves. Faulty slaves generate a diagnostics interrupt.

The status of the slaves can be displayed as a graphic in the TIA Portal.

Switchover to the operating mode "Configuration mode" (CM) is disabled because the TIA project specifies an unequivocal hardware configuration.

## AS-i motor starter parameters

### Process image extension

With this parameter, you specify whether the extended cyclic process image (analog data) should be used.

The extended PII (4 bytes) contains the motor current and selected diagnostic bits. The extended cyclic process image input can be read out even if this parameter is deactivated.

The motor starter can be parameterized with the extended PIQ (4 bytes). It is a reduced parameter range.

The parameters in the extended cyclic process image can only be used if this parameter is activated.

### Waiting for data set parameters

With this parameter, you specify whether the parameters are transferred from within the user program.

The motor starter then detects whether a data set is to be transmitted. The motor starter waits for 3 minutes for the start-up data set "Parameter". If the transmission is not completed within this time, the starter reports the error "Invalid parameter value". This error is automatically acknowledged when the start-up parameters have been transferred without errors.

## AS-i master operating state

### **Protected mode**

- The AS-i master only exchanges data with the configured AS-i slaves.
- In case of changes to the actual bus configuration, error messages are automatically generated, for example, in case of a slave failure.
- The CM LED is off.
- When specifying the AS-i slave configuration in the TIA project, the master automatically starts in "Protected mode".

### **Configuration mode**

- The AS-i master only exchanges data with all recognized AS-i slaves.
- A configuration of the slaves is not evaluated.
- No error message is generated in case of a slave failure.
- The CM LED lights up ("Configuration Mode").

## AS-i master system default

### **System default is activated**

The I/O addresses of the AS-i slaves are automatically assigned. The I/O address of an individual slave is calculated depending on the AS-i address. By entering the start address of the AS-i master, you determine the address range of the digital I/O addresses of the slaves.

Further information and properties:

- Analog slaves are not located in the cyclic process image.
- For Safety input slaves, bit 0 = F-IN1 and bit 2 = F-IN2 applies (only for diagnostics purposes, never evaluate safety-related!).
- The system default is automatically activated when no slaves are configured in the TIA project (basic configuration).

For AS-i master CM 1243-2, the following applies:

The I/O addresses of the AS-i slaves are automatically assigned. The I/O address of an individual slave is calculated depending on the AS-i address. By entering the start address of the AS-i master, you determine the address range of the digital I/O addresses of the slaves.

One I/O byte is reserved for each AS-i slave. To determine the byte address, add the AS-i address of the slave and the start address of the master. For slaves with B address, you also add the offset value 32. The I/O byte contains right-justified the 4-bit I/O data of the AS-i slave. The slave profile of the slave determines which positions of the 4-bit I/O data are actually busy with I/O signals.

### **System default is deactivated**

You specify the I/O addresses of an individual slave by configuring the slave.

Further information and properties:

- Digital and analog slaves are located in the cyclic process image.
- For Safety input slaves, bit 0 = F-IN1 and bit 2 = F-IN2 applies (only for diagnostics purposes, never evaluate safety-related!).
- The system default is automatically deactivated when at least one slave is configured in the TIA project (configuration with AS-i network).

For AS-i master CM 1243-2, the following applies:

You specify the I/O addresses of an individual slave by configuring the slave.

Each configured AS-i slave uses at least one input byte and/or output byte. The slave profile of the slave determines which bits of the I/O data are actually busy with I/O signals. The first bit position used is automatically displayed in the properties of the configuration.

## I/O range

This section contains information on the following topics:

- [Input and output ranges](#input-and-output-ranges)
- [I/O configuration for AS-i slaves](#io-configuration-for-as-i-slaves)
- [Operating principle of the safe AS-i outputs](#operating-principle-of-the-safe-as-i-outputs)

### Input and output ranges

The CM AS-i Master ST module has an I/O range (process image for inputs and outputs) for transferring the AS-i slave input and output data to the CPU of the PLC.

The permissible length of the I/O range, as well as the assignment of I/O addresses to AS-i slaves, is dependent on the configuration used. The input and output ranges have the same length.

The length of data configured is always transferred, although data not used by slaves is filled with substitute values.

If a configured slave is not present (e.g. in the event of slave failure), the allocated input range is populated with substitute values.

In the event of a slave failure, no I/O area access error is generated because the entire I/O range is transferred, filled with either process values or substitute values.

In order to achieve the best possible performance, select the length of the I/O range based on the volume of data used by the slaves.

If the length is set to > 32 bytes, the module in the ET 200SP slot uses time division multiplexing to internally transfer data with a block size of 32 bytes.

#### **Properties of the I/O range for different configurations**

**CM AS-i Master ST, FW version V1.0**

Length of I/O range: 32 bytes

The digital inputs and outputs of the AS-i slaves are assigned to the addresses in the I/O range according to a defined format. See the table below for more details.

The analog inputs and outputs of the AS-i slaves can be transferred via data record communication.

The following table shows the assignment of the digital I/O address to the AS-i slave address:

|  |  |  |
| --- | --- | --- |
| Byte | Bit 7 … 4 | Bit 3 … 0 |
| n+0 | Reserved | Slave 1 or 1A |
| n+1 | Slave 2 or 2A | Slave 3 or 3A |
| n+2 | Slave 4 or 4A | Slave 5 or 5A |
| n+3 | Slave 6 or 6A | Slave 7 or 7A |
| n+4 | Slave 8 or 8A | Slave 9 or 9A |
| n+5 | Slave 10 or 10A | Slave 11 or 11A |
| n+6 | Slave 12 or 12A | Slave 13 or 13A |
| n+7 | Slave 14 or 14A | Slave 15 or 15A |
| n+8 | Slave 16 or 16A | Slave 17 or 17A |
| n+9 | Slave 18 or 18A | Slave 19 or 19A |
| n+10 | Slave 20 or 20A | Slave 21 or 21A |
| n+11 | Slave 22 or 22A | Slave 23 or 23A |
| n+12 | Slave 24 or 24A | Slave 25 or 25A |
| n+13 | Slave 26 or 26A | Slave 27 or 27A |
| n+14 | Slave 28 or 28A | Slave 29 or 29A |
| n+15 | Slave 30 or 30A | Slave 31 or 31A |
| n+16 | Status data | Slave 1B |
| n+17 | Slave 2B | Slave 3B |
| n+18 | Slave 4B | Slave 5B |
| n+19 | Slave 6B | Slave 7B |
| n+20 | Slave 8B | Slave 9B |
| n+21 | Slave 10B | Slave 11B |
| n+22 | Slave 12B | Slave 13B |
| n+23 | Slave 14B | Slave 15B |
| n+24 | Slave 16B | Slave 17B |
| n+25 | Slave 18B | Slave 19B |
| n+26 | Slave 20B | Slave 21B |
| n+27 | Slave 22B | Slave 23B |
| n+28 | Slave 24B | Slave 25B |
| n+29 | Slave 26B | Slave 27B |
| n+30 | Slave 28B | Slave 29B |
| n+31 | Slave 30B | Slave 31B |

n = Start address

Status data only possible with CM AS-i Master ST from FW version V1.1 onwards, otherwise these 4 bits are not used (reserved).

#### **CM AS-i Master ST, from FW version V1.1 with configuration via acceptance of ACTUAL configuration, e.g. via SET button**

> **Note**
>
> **No configuration of AS-i slaves in STEP 7 and/or configuration via GSD**

Switchable I/O range length: 16 bytes or 32 bytes

The digital inputs and outputs of the AS-i slaves are assigned to the addresses in the I/O range according to a defined format. See above table.

The analog inputs and outputs of the AS-i slaves can be transferred via data record communication.

When the length is set to 16 bytes, the digital I/Os of the AS-i slaves with B addresses are not transferred.

When the length is set to 32 bytes, 4 bits of status data can be additionally transferred.

#### **CM AS-i Master ST, from FW version V1.1 with configuration of AS-i slaves in STEP 7 (i.e. selection of AS-i slaves from hardware catalog)**

Settable I/O range length: 4 ... 288 bytes

Possible settings: 4, 8, 12, 16, 20, 24, 28, 32, 64, 96, 128, 160, 192, 224, 256, 288 bytes

The digital and analog inputs and outputs of the AS-i slaves can be freely assigned within the I/O range.

The digital and analog inputs and outputs of the AS-i slaves can also be transferred via data record communication.

Further factors affecting the length of the I/O range:

Length of I/O range: 4 ... 256 bytes for configurations with IM 155-6 PN ST from FW V3.1 onwards  
Length of I/O range: 4 ... 32 bytes for configurations with IM 155-6 PN ST < FW V3.1   
Restriction when operating under CPU S7-300 FW version < V3 - length of I/O range: max. 224 bytes

Length of I/O range: 4 ... 32 bytes for configurations with IM 155-6 DP HF

### I/O configuration for AS-i slaves

#### I/O configuration

The I/O configuration is assigned as follows on the basis of the I/O code standard:

AS-i standard slave

| I/O code | I/O configuration |  |  |  |
| --- | --- | --- | --- | --- |
|  | D0 | D1 | D2 | D3 |
| 0 | I | I | I | I |
| 1 | I | I | I | O |
| 2 | I | I | I | B |
| 3 | I | I | O | O |
| 4 | I | I | B | B |
| 5 | I | O | O | O |
| 6 | B | B | B | B |
| 7 | B | B | B | B |
| 8 | O | O | O | O |
| 9 | O | O | O | I |
| A | O | O | O | B |
| B | O | O | I | I |
| C | O | O | B | B |
| D | O | I | I | I |
| E | O | B | B | B |
| F | F | F | F | F |
| Key: I=Input; O=Output; B=Bidirectional (input/output); F=TriState |  |  |  |  |

AS-i A/B slave

| I/O code | I/O configuration |  |  |  |
| --- | --- | --- | --- | --- |
|  | D0 | D1 | D2 | D3 |
| 0 | I | I | I | I |
| 1 | I | I | I | - |
| 2 | I | I | I | I |
| 3 | I | I | O | - |
| 4 | I | I | B | I |
| 5 | I | O | O | - |
| 6 | B | B | B | I |
| 7 | B | B | B | I |
| 8 | O | O | O | - |
| 9 | O | O | O | I |
| A | O | O | O | I |
| B | O | O | I | I |
| C | O | O | B | I |
| D | O | I | I | I |
| E | O | B | B | I |
| F | F | F | F | F |
| Key: I=Input; O=Output; B=Bidirectional (input/output); F=TriState |  |  |  |  |

### Operating principle of the safe AS-i outputs

Safety-related communication for safe AS-i outputs also uses code sequences. However, they have a different data structure compared to the code sequences of safe AS‑i input slaves. The code sequences for safe AS-i outputs do not have to be taught and transferred.

For the function of a safe AS‑i output, you need the following components:

- A control unit
- An evaluation unit

#### Control unit

The control unit outputs safety-related IN or OUT control commands to the AS-i bus. The control unit is integrated in the F‑CM AS‑i Safety ST module. The control unit assumes an active position in the communication. It acts like an AS-i slave and has an AS-i address that must be called by the AS‑i master. The values in the output data of the AS-i master are not relevant in this case. The F‑CM AS‑i Safety ST module inserts the safety-related control data into the communication data.

Besides controlling the OFF state according to specification, a control unit can control up to four different output switching states: F‑OUT 1, F‑OUT 2, F‑OUT 3, and F‑OUT 4. The F‑CM AS‑i Safety ST module, however, makes available only the output switching state F‑OUT 1, i.e., The OFF and ON states are controlled.

In addition to the switching states, a control unit can send out two different auxiliary signals: AUX1 and AUX2. You can use these auxiliary signals for error acknowledgement in the evaluation unit. For technical reasons, the AUX1 and AUX2 signals are mapped in the safe process image output. The auxiliary signals are not safety-related signals, however. During control by the safety program, the F‑CM AS‑i Safety ST module sends a sequence from each auxiliary signal one after the other on the AS-i bus. Up to 16 different control units can be activated in the F‑CM AS‑i Safety ST module. The control units are managed in the F‑CM AS‑i Safety ST module as switching group 0 to switching group 15.

If you want to use more than 16 different control units, you can plug two F‑CM AS‑i Safety ST modules into the ET 200SP station.

Observe the information on the bus configuration in Section AS-i bus configuration with multiple F-CM AS-i Safety ST modules.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Uniqueness of the AS‑i address on the AS-i bus**  Carefully check the AS‑i addresses for the control of the safe AS‑i outputs. Ensure that the assigned AS-i address exists only once on the AS-i bus. This is particularly important when you are using multiple devices that can control safe AS-i outputs on the same AS-i bus. If this is not observed, reliable shutdown of a safe output module is not guaranteed. |  |

#### Evaluation unit

The evaluation unit reads the safety-related control commands ON or OFF on the AS-i bus and passes corresponding switching commands, e.g., to switching contacts. In case of error, e.g., communication error on the AS-i bus, the evaluation unit switches off. The evaluation unit is integrated in the safe AS-i output module to which, for example, drive contactor coils are connected. The evaluation unit behaves as a passive unit in the AS-i communication. The master does not detect the evaluation unit and does not call it. The evaluation unit monitors the communication of the AS-i address of the control unit and reacts to its safety-related control signals.

You set the AS-i address (see Section "Control unit") the evaluation unit is to monitor.

You can set multiple evaluation units to the same address so that a control unit can control multiple safe output modules simultaneously.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Bus cycle time for safe AS-i outputs**  An evaluation unit requires a minimum AS-i bus cycle time. Ensure that at least 5 AS-i addresses are present on the AS-i bus. Otherwise, the control unit goes to error state. When A/B slaves are used, at least 5 different numerical AS-i addresses must be present. That is, a combination of slave addresses 1A and 1B count as 1 numerical address.  The F‑CM AS‑i Safety ST module does not have a monitoring function for this configuration rule. |  |

## Reset CM 1243-2 AS-i master module to factory settings

### Automatic restart

When you reset the CM 1243-2 AS-i master module to factory settings, the module executes a restart on the AS-i bus. This means:

- The slave configuration contained in the non-volatile memory of the AS-i master is deleted: AS-i addresses, slave profiles (IO, ID, ID2 codes), ID1 codes and AS-i slave parameters.   
  The terms IO code and I/O configuration used for the slave profile are equivalent.
- The AS-i master switches to "Configuration Mode (CM)" when no slaves are configured in the TIA project (basic configuration without configured slaves / specifying the AS-i slave configuration: Device memory of the AS-i master).  
  In configuration mode, all connected permissible AS-i slaves are recognized by the master immediately, activated, and integrated into the cyclic data exchange.
- The connection to the AS-i slaves is interrupted (AS-i offline) and established again (AS-i online). This means the AS-i LED on the CM 1243-2 will turn off briefly.

### Notes on configuration

- The slave configuration in the non-volatile memory of the master is only applied when no slaves are configured in the TIA project.  
  Using the online function control panel - "Apply AS-i slave configuration (ACTUAL->TARGET)", the AS-i master can apply the slave configuration connected at the terminals ASI+ / ASI- to the non-volatile memory. You can switch from "Configuration Mode" to "Protected Mode" using the online function control panel.
- If slaves are configured in the TIA project, the non-volatile memory of the master is not used (specification of the AS-i slave configuration: TIA project). The slave configuration of the TIA project is also valid after a reset to factory settings and the master remains in "Protected Mode".
- In "Protected Mode", the master only activates the slaves that are contained in the configuration. Slaves that are included in the configuration but do not exist, are signaled as faulty.
