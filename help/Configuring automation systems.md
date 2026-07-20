---
title: "Configuring automation systems"
package: HWCConf34enUS
topics: 209
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring automation systems

This section contains information on the following topics:

- [Functional description of S7-300/400 CPUs (S7-300, S7-400)](Functional%20description%20of%20S7-300-400%20CPUs%20%28S7-300%2C%20S7-400%29.md#functional-description-of-s7-300400-cpus-s7-300-s7-400)
- [Functional description of S7-1200 CPUs (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#functional-description-of-s7-1200-cpus-s7-1200)
- [Functional description of S7-1500 CPUs (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#functional-description-of-s7-1500-cpus-s7-1500)
- [Principle of operation for S7-1500R/H CPUs (S7-1500)](Principle%20of%20operation%20for%20S7-1500R-H%20CPUs%20%28S7-1500%29.md#principle-of-operation-for-s7-1500rh-cpus-s7-1500)
- [Principle of operation of virtual CPUs](#principle-of-operation-of-virtual-cpus)
- [Principle of operation for SIMATIC Drive controllers](Principle%20of%20operation%20of%20SIMATIC%20Drive%20Controllers.md#principle-of-operation-of-simatic-drive-controllers)
- [Addressing modules](#addressing-modules)
- [Configuring the Web server (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#configuring-the-web-server-s7-300-s7-400-s7-1500)
- [Configuring the Web server (S7-1200)](#configuring-the-web-server-s7-1200)
- [Configuring central racks (S7-300, S7-400, S7-1500)](#configuring-central-racks-s7-300-s7-400-s7-1500)
- [Rules for modules (S7-300)](#rules-for-modules-s7-300)
- [Rules for modules (S7-400)](#rules-for-modules-s7-400)
- [Rules for modules (S7-1500)](#rules-for-modules-s7-1500)
- [Selecting modules (S7-300, S7-400, S7-1500)](#selecting-modules-s7-300-s7-400-s7-1500)
- [Selecting fail-safe modules (S7-300, S7-400, S7-1500)](#selecting-fail-safe-modules-s7-300-s7-400-s7-1500)
- [Changing the properties of CPUs (S7-300, S7-400, S7-1500)](#changing-the-properties-of-cpus-s7-300-s7-400-s7-1500)
- [Linking racks (S7-300)](#linking-racks-s7-300)
- [Linking racks (S7-400)](#linking-racks-s7-400)
- [Flexible automation concepts (S7-1200, S7-1500, S7-1500T)](#flexible-automation-concepts-s7-1200-s7-1500-s7-1500t)
- [Using OPC UA communication (S7-1200, S7-1500, S7-1500T)](#using-opc-ua-communication-s7-1200-s7-1500-s7-1500t)
- [Additional configurations (S7-1200)](#additional-configurations-s7-1200)

## Principle of operation of virtual CPUs

This section contains information on the following topics:

- [Useful information about virtual CPUs](#useful-information-about-virtual-cpus)
- [Rules for programming a virtual CPU](#rules-for-programming-a-virtual-cpu)

### Useful information about virtual CPUs

#### Virtual CPUs for Edge-based automation applications

As of TIA Portal V19, you can insert virtual CPUs, e.g. a CPU S7-1587V, into a project and configure them. Functionally, these CPUs are not different from standard CPUs. Virtual CPUs have the advantage, however, that they can be easily integrated in an Industrial Edge Computing platform since they are not hardware-dependent.

The special considerations regarding the compilation and use of programs for virtual CPUs are outlined below.

#### Requirements

- The Industrial Edge Management system is available.
- An Industrial Edge device is registered and configured through the Industrial Edge Management System.
- The application "CPU 1587V (F)" is available on your Industrial Edge Hub Tenant.

You can operate the CPU 1587V(F) on the Industrial Edge Virtual Device Platform (IEVD). You install the IEVD as a virtual machine on the VMWare ESXi. You need to adjust some settings of the virtual machine for the "CPU 1587V(F)" application.

#### More information

For information on the provision and installation of the CPU S7-1587V(F), refer to the documentation "S7-1500 Virtual Controller CPU 1587V(F)".

### Rules for programming a virtual CPU

On compilation of a program that is located in the project tree under a CPU, the TIA Portal automatically ensures that the appropriate executable code is generated.

However, when creating programs for a library, you must follow a few rules to ensure that the blocks are universally applicable. These rules are explained below.

#### Compiling programs below a CPU

- If a program is located below a standard CPU (S7-151x CPU) then, by default, the blocks are only executable on standard CPUs for a project. The generated code is not executable on virtual CPUs (S7-158x CPUs).
- If a program is located below a virtual CPU, then the blocks are executable on both virtual CPUs and standard CPUs. This also applies to know-how-protected blocks.

#### Rules for creating blocks for standard and virtual CPUs

- If you want to use blocks created below a standard CPU for virtual CPUs as well, you need to adjust the default project settings: In the settings for the project, "Protection" tab, activate the setting "Enable usage of S7-1500 blocks in virtual PLCs".

  If the blocks need to be know-how protected, you must enable the option mentioned above **before** you generate the block.

  ![Rules for creating blocks for standard and virtual CPUs](images/170541266443_DV_resource.Stream@PNG-en-US.png)
- If you want to create library types that are not know-how-protected, it is not necessary to activate the option "Enable usage of S7-1500 blocks in virtual PLCs". When instantiating the library type in a CPU, the TIA Portal automatically generates the correct code.
- If you want to upload blocks from an S7-1500 CPU into your TIA project and maintain support for virtual CPUs, make sure that in the project settings, under the "Protection" tab, the option "Enable usage of S7-1500 blocks in virtual PLCs" is activated.

  If the blocks are know-how-protected or if the blocks are instances of released versions of library types, support for virtual CPUs will not be removed from the TIA Portal. In this case, you don't need to worry about the appropriate project settings.

## Addressing modules

This section contains information on the following topics:

- [Addressing modules (S7-300, S7-400)](#addressing-modules-s7-300-s7-400)
- [Addressing modules (S7-1200)](#addressing-modules-s7-1200)
- [Addressing modules (S7-1500)](#addressing-modules-s7-1500)
- [Specifying input and output addresses (S7-300, S7-400, S7-1500)](#specifying-input-and-output-addresses-s7-300-s7-400-s7-1500)
- [Specifying input and output addresses (S7-1200)](#specifying-input-and-output-addresses-s7-1200)
- [Information about diagnostic addresses (S7-300, S7-400)](#information-about-diagnostic-addresses-s7-300-s7-400)
- [What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
- [Example for the use of hardware identifiers (S7-1200, S7-1500, S7-1500T)](#example-for-the-use-of-hardware-identifiers-s7-1200-s7-1500-s7-1500t)
- [Input and output addresses in the address overview (S7-300, S7-400, S7-1500)](#input-and-output-addresses-in-the-address-overview-s7-300-s7-400-s7-1500)
- [Assign process image/process image partition (S7-300, S7-400)](#assign-process-imageprocess-image-partition-s7-300-s7-400)
- [Assign process image/process image partition (S7-1500)](#assign-process-imageprocess-image-partition-s7-1500)
- [Using process image partitions in instructions (S7-1500)](#using-process-image-partitions-in-instructions-s7-1500)
- [Assigning addresses to a location in the program (S7-300, S7-400, S7-1500)](#assigning-addresses-to-a-location-in-the-program-s7-300-s7-400-s7-1500)
- [Assigning addresses to a location in the program (S7-1200)](#assigning-addresses-to-a-location-in-the-program-s7-1200)

### Addressing modules (S7-300, S7-400)

#### Introduction

In the device overview, you see the addresses or address ranges of the modules in the I address and Q address columns.

Input and output addresses are assigned automatically when modules are inserted in the rack. The address of the first channel is the start address of a module. The addresses of the other channels are derived from this start address. The end address is derived from the module-specific address length.

#### Special feature: Input addresses with asterisk (*)

In the device view certain addresses from the input address range are marked with an asterisk (*). In this case these are diagnostics addresses, e.g. interface modules that do not address user data, but rather that are used for system diagnostics.

#### Difference between device addresses and I/O addresses

When assigning addresses a distinction is made between device addresses and I/O addresses (input/output addresses):

- Device addresses are addresses of programmable modules (MPI addresses, PROFIBUS addresses, Industrial Ethernet addresses). They are required to address the different stations of a subnet, for example, to download a user program to a CPU.
- I/O addresses are used to read inputs or set outputs in the user program.

#### Special feature: MPI addresses of FMs and CPs (S7-300)

For CPs and FMs with own MPI address, the default MPI address is set by STEP 7.

The MPI address can be changed subsequently (in the inspector window via "Properties > MPI interface").

For CPs and FMs without own MPI address, the CPU addresses these modules via the K bus using the module rack and slot number.

---

**See also**

[Specifying input and output addresses (S7-300, S7-400, S7-1500)](#specifying-input-and-output-addresses-s7-300-s7-400-s7-1500)
  
[Assigning addresses to a location in the program (S7-300, S7-400, S7-1500)](#assigning-addresses-to-a-location-in-the-program-s7-300-s7-400-s7-1500)

### Addressing modules (S7-1200)

#### Introduction

In the device overview, you see the addresses or address ranges of the modules in the I address and Q address columns. There are other addresses as well, which are explained below.

#### I/O address

I/O addresses (input/output addresses) are required to read inputs and set outputs in the user program.

Input and output addresses are assigned automatically when modules are inserted in the rack. The address of the first channel is the start address of a module. The addresses of the other channels are derived from this start address. The address end is obtained from the module-specific address length.

#### Device address (e.g., Ethernet address)

Device addresses are addresses of programmable modules (Industrial Ethernet addresses). They are required to address the different stations of a subnet, for example, to download a user program to a CPU.

#### Hardware identifier for identifying modules and submodules

In addition to the I addresses and Q addresses, a hardware identifier (HW ID) is assigned automatically and is used to address and identify the module. Submodules (units of a module), such as an integrated counter, also receive such a hardware identifier.

The hardware identifier consists of an integer and is output by the system with diagnostics alarms to allow the faulty module or the faulty submodule to be localized.

In addition, the hardware identifier is used for a number of instructions to address the corresponding module.

The hardware identifier cannot be changed.

Example: Identifying high-speed counters of the S7-1200 CPU

![Hardware identifier for identifying modules and submodules](images/25944137227_DV_resource.Stream@PNG-de-DE.png)

The hardware identifier is assigned automatically when components are inserted in the device or network view and in the PLC tags. A name is also assigned automatically for the hardware identifier. The system constants of the PLC tags cannot be changed either.

---

**See also**

[Specifying input and output addresses (S7-1200)](#specifying-input-and-output-addresses-s7-1200)
  
[Assigning addresses to a location in the program (S7-1200)](#assigning-addresses-to-a-location-in-the-program-s7-1200)
  
[Introduction to loading a configuration](Configuring%20devices%20and%20networks.md#introduction-to-loading-a-configuration)
  
[Inspector window](Configuring%20devices%20and%20networks.md#inspector-window)

### Addressing modules (S7-1500)

#### Introduction

In the device overview, you see the addresses or address ranges of the modules in the I address and Q address columns. There are other addresses as well, which are explained below.

#### I/O address

I/O addresses (input/output addresses) are required to read inputs and set outputs in the user program.

Input and output addresses are assigned automatically when modules are inserted in the rack. The address of the first channel is the start address of a module. The addresses of the other channels are derived from this start address. The address end is obtained from the module-specific address length.

#### Device address (e.g., Ethernet address)

Device addresses are addresses of programmable modules (Industrial Ethernet addresses). They are required to address the different stations of a subnet, for example, to download a user program to a CPU.

#### Hardware identifier for identifying modules and submodules

In addition to the I addresses and Q addresses, a hardware identifier (HW ID) is assigned automatically and is used to address and identify the module. Submodules (units of a module), such as integrated counters, also receive a hardware identifier. The hardware identifier consists of an integer and is output by the system with diagnostics alarms to allow the faulty module or the faulty submodule to be localized. In addition, the hardware identifier is used for a number of instructions to address the corresponding module. The hardware identifier cannot be changed.

---

**See also**

[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[Inspector window](Configuring%20devices%20and%20networks.md#inspector-window)

### Specifying input and output addresses (S7-300, S7-400, S7-1500)

The input and output addresses are indeed preset automatically, however you can change the addressing retroactively.

#### Requirement

- You are in the device view.
- The device is a compact DP slave, for example, or the addressable module is inserted in one of the following objects:

  - Central rack
  - Expansion rack
  - DP slave/IO device
- The CPU allows free address assignment.

#### Procedure

To change the preset address range proceed as follows:

1. In the device view, click on the module for which you want to set the start address.
2. Click on "I/O Addresses" under "Properties" in the Inspector window.
3. Under "Start address" enter the required start address.
4. Press <Return> or click on any object to accept a modified value.

If you have entered an invalid address a message will be shown in which you can accept a suggested address or enter a different address.

> **Note**
>
> You can also change the addresses directly in the device overview. If address specification is not enabled by the CPU, the address will be disabled in the display.
>
> For modules within a local bus segment, formed by an FM (S7-300) or for special FMs (S7-400), additionally assign another start address. In addition to the start address for the CPU, the module will then also have a start address for the FM. In the device overview in this case the start address is always displayed from the perspective of the FM.

---

**See also**

[Editing properties and parameters](Configuring%20devices%20and%20networks.md#editing-properties-and-parameters)

### Specifying input and output addresses (S7-1200)

Default input and output addresses are set automatically. You can, however, change the address assignment later.

All addresses of modules are located in the process image area. The process image is automatically updated cyclically.

#### Requirement

You are in the device view.

#### Procedure

To change the preset address range proceed as follows:

1. In the device view, click on the module for which you want to set the start address.
2. Go to "I/O addresses" in "Properties" in the inspector window.
3. Under "Start address" enter the required start address.
4. Press <Return> or click on any object to accept a modified value.

If you have entered an invalid address, a message indicating the next available address is displayed.

> **Note**
>
> You can also change the addresses directly in the device overview.

---

**See also**

[Editing properties and parameters](Configuring%20devices%20and%20networks.md#editing-properties-and-parameters)
  
[Input and output addresses in the address overview](Configuring%20devices%20and%20networks.md#input-and-output-addresses-in-the-address-overview)

### Information about diagnostic addresses (S7-300, S7-400)

#### Introduction

Diagnostic addresses are used to address components that do not have user data, for example interface modules or ports.

#### Input addresses as diagnostic addresses

Use diagnostic addresses to address components that do not have user data. STEP 7 assigns an e-address automatically to the components "from the top", i.e. from the highest e-address downward. This e-address is named diagnostic address.

This input address is not used to read in input values (process values). The diagnostic address is used, for example, to address components in the instructions "DPNRM_DG" or "RDREC".

#### Examples

To read the diagnostic data record of an DP slave, use the diagnostic address of the interface module of this DP slave with the instruction "DPNRM_DG" ("LADDR" parameter).

To read the data record containing the neighborhood relationships of a port, use the diagnostic address of this port for the instruction "RDREC" ("ID" parameter).

#### Addressing with input and output groups

To address the input module, use the start address with the instructions "RDREC" or "WRREC". If the addresses 5 and 6 are assigned to an input module, 5 is the start address. Set the value "DW#16#0005" for the "ID" parameter.

To address the output module, use the start address also with the instructions "RDREC" or "WRREC". Set the "ID" parameter to the value "DW#16#8005" for the start address 5. For an output module, bit 15 (value "1") must be set. Therefore, with the start address 5, the value of DW#16#8005 results for the "ID" parameter.

To address a hybrid module (input and output module), enter the smaller of the two start addresses in the "ID" parameter. If the input and output area have the same start address, then use the identifier for an input address (bit 15 of the address is not set, "0").

---

**See also**

[DPNRM_DG: Read diagnostics data from a DP slave (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)
  
[Reading out topology data of a PROFINET system](http://support.automation.siemens.com/WW/view/en/38566021)

### What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)

#### Introduction

Every hardware object, e.g., a module, interface or port of a module, or even transfer areas of I-devices, has a HW identifier that STEP 7 assigns automatically when a hardware component is configured.

In S7-1500 and S7-1200 systems, these hardware identifiers have a similar function to the diagnostic addresses of HW components without user data, or the start addresses of HW objects with user data in S7-300/400 systems. The hardware identifiers of the modules are insensitive to changes to the I/O addresses and are therefore retained. When I/O addresses are changed, the instructions that use a hardware identifier do not have to be adapted.

#### HW identifiers in the "System constants" tab in the Inspector window

When you select a hardware object in the device view and select the "System constants" tab in the Inspector window, all HW identifiers of the hardware object are displayed as system constants with name and type.

The names of the HW identifiers are structured hierarchically. They consist of a maximum of four hierarchical level, each of which is separated by a tilde "~". Based on the name, you can therefore recognize the "path" to the relevant hardware module.

The display of the hardware identifiers depends on the object that you have selected in the graphic view. If you select an entire device in the network view or device view, all hardware identifiers of all objects in the corresponding device are displayed in the system constants (modules, interfaces, ports, etc.). If you only select an individual module or port, only the hardware identifier of the selected object is displayed in the system constants.

#### Example

The system constant with the name "Local~DI_16x24VDC_HF_1" identify the HW identifier for the digital input module with the name "DI_16x24VDC_HF_1" in the local ("Local") CPU. The name of the digital module matches the editable name in the properties of the component (inspector window). If you only select this module, only the hardware identifier for this module is displayed.

![Example](images/69428073611_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> To facilitate identification of HW objects, assign the most descriptive names possible for HW objects when configuring the hardware. The names should include the association of the HW object to a plant unit or device.

#### HW identifiers in the system constants of the PLC tag table

STEP 7 adds entries to the PLC tags ("System constants" tab) for each configured hardware component. These entries are read-only. In addition to the integer value, a name and a HW data type are also specified.

Example:

![HW identifiers in the system constants of the PLC tag table](images/69428590091_DV_resource.Stream@PNG-en-US.png)

#### Hardware identifiers in programming

If you address a HW component in an instruction with the "ID" or "LADDR" input parameter, for example, you can double-click this input parameter to display a list of all relevant HW components for selection.

In the start information of a hardware interrupt OB, for example, you can identify the interrupt-triggering module through the hardware identifier.

![Hardware identifiers in programming](images/69431676427_DV_resource.Stream@PNG-de-DE.png)

#### Additional information

You can find information on converting address information (IO addresses, slot, HW identifier) [here](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#instructions-for-address-conversion-s7-1200-s7-1500).

---

**See also**

[Hardware interrupt OBs (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#hardware-interrupt-obs-s7-1500)
  
[Inspector window](Configuring%20devices%20and%20networks.md#inspector-window)
  
[Example of a hardware interrupt event (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#example-of-a-hardware-interrupt-event-s7-1500)
  
[Example for the use of hardware identifiers (S7-1200, S7-1500, S7-1500T)](#example-for-the-use-of-hardware-identifiers-s7-1200-s7-1500-s7-1500t)

### Example for the use of hardware identifiers (S7-1200, S7-1500, S7-1500T)

You use hardware identifiers to address hardware objects such as modules, submodules or devices. The hardware identifiers have different hardware data types, depending on the instruction. The permitted hardware data type is listed for all configured components in the default tag table, "System constants" tab.

Below, you will find an explanation of the hardware identifiers that have to be used for selected instructions.

> **Note**
>
> **Information on the respective hardware identifier**
>
> For each extended instruction that addresses hardware objects, the hardware object that has to be used is documented in the help. You access the help for the selected instruction with the <F1> key.

#### Recommendation

You can enter the name of the hardware object or the numerical hardware identifier of the hardware object in the Program editor.

Recommendation: Assign the most descriptive names possible for hardware objects, for example, for the modules. Read out the name and HW identifier from the "System constants" tab in the device view and enter it in the Program editor at the corresponding instruction. If you have assigned a descriptive name, you will find the name more easily in the drop-down list for selecting the HW identifier at the block parameter "ID".

#### Additional options for input of the HW identifier

You can drag the HW identifier from the tag table to the block parameter "ID" with drag-and-drop.

Advantage: The hardware data type is checked by the Program editor and may be rejected if an invalid hardware object was selected.

No check is possible with a numerical input.

If the permitted hardware object is an IO device, for example, select the entire IO device in the network view and read out the hardware identifier under "Properties" ("General" tab) in the inspector window. If you do not select the IO device in this case but rather the interface module in the IO device, the hardware identifier visible in the inspector window would be invalid for this instruction. You will not notice this error during programming with numerical input of the HW identifier.

#### Example of entering a hardware identifier

The following name of a module may be listed in the default tag table, "System constants" tab, for example:

myModule[AI]

1. Open the program editor
2. Open the default tag table ("PLC tags" folder)
3. Place the editor window of the programming editor and the default tag table next to each other.

   To do so, click the "Split editor space vertically" button in the toolbar.

   ![Example of entering a hardware identifier](images/60591971083_DV_resource.Stream@PNG-de-DE.png)

   ![Example of entering a hardware identifier](images/60591971083_DV_resource.Stream@PNG-de-DE.png)
4. Drag the "myModule[AI]" from the "System constants" tab and drop it in the "ID" or "LADDR" box of the respective instruction with drag-and-drop as seen in the figure below.

![Example of entering a hardware identifier](images/105175509003_DV_resource.Stream@PNG-de-DE.png)

#### Example for addressing with hardware identifier

Extended instruction D_ACT_DP: Deactivate/activate the DP slave or PROFINET IO device.

The hardware data type is Hw_DpSlave or Hw_Device. DP slaves or IO devices are permitted hardware objects for the input parameter "LADDR".

![Example for addressing with hardware identifier](images/52411180683_DV_resource.Stream@PNG-de-DE.png)

Extended instruction DPSYC_FR: Synchronize/freeze DP slaves.

The hardware data type is Hw_Interface. The DP master interface is the permitted hardware object for the input parameter "LADDR".

![Example for addressing with hardware identifier](images/60595327243_DV_resource.Stream@PNG-de-DE.png)

Extended instruction RDREC: Read data record.

The hardware data type is Hw_SubModule. Modules or submodules from which the data record is to be read are permitted hardware objects for the input parameter "ID".

You also use this HW data type for the extended instruction DPRD_DAT.

![Example for addressing with hardware identifier](images/52411783179_DV_resource.Stream@PNG-de-DE.png)

Extended instruction WRREC: Write data record. The instruction is used, for example, to write data records to a module or submodule.

The hardware data type is also Hw_SubModule. Permitted hardware objects for the input parameter "ID" are modules or submodules to which the data record is to be transferred.

You also use this HW data type for the extended instruction DPWR_DAT.

Notes:

- When dividing an I/O module into several submodules (e.g., 1 x 8 AI => 8 x 1AI), use the hardware identifier of a submodule. Do not use the hardware identifier of the module in this case.
- Use the hardware identifier of the head for interface modules of a distributed I/O system to which a data record is to be transferred for configuration control (option handling), see figure.

![Example for addressing with hardware identifier](images/60073690891_DV_resource.Stream@PNG-en-US.png)

Extended instruction Station_Info: Reading information of an IO device.

The hardware data type is Hw_Device. An IO device is the permitted hardware object for the input parameter "ID".

![Example for addressing with hardware identifier](images/60924522379_DV_resource.Stream@PNG-de-DE.png)

#### Additional information

You can find additional information on converting address information (IO addresses, slot, HW identifier) [here](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#instructions-for-address-conversion-s7-1200-s7-1500).

---

**See also**

[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)

### Input and output addresses in the address overview (S7-300, S7-400, S7-1500)

#### Introduction

The currently used input and output addresses can be displayed in the address overview in a table form. The address overview can be found in the inspector window under "Properties" of the CPU.

#### Design of the address overview

With the different check boxes, you can set which objects should be displayed in the address overview:

- Inputs: Display of the input addresses
- Outputs: Display of the output addresses
- Address gaps: Display of open address spaces
- Slot: Display of the slot number

The following information is typically shown in the address overview:

| Table header | Meaning |
| --- | --- |
| Type | Indicates whether the area is an input address area or an output address area. |
| Address from | Start address in the address range. |
| Address to | End address in the address range. |
| Module | Modules using the address area. |
| PIP | Number of the process image partition. Shows if the cyclical OB in the process image partition. |
| OB | Assigned organization block |
| DP | Number of the master system. You can use the number to determine which slaves are assigned to a master. The value in brackets specifies the PROFIBUS address of the hardware component. |
| PN | Number of the IO system. The value in brackets stands for the device number of the hardware component. |
| Racks | Rack number on which the hardware component is inserted. |
| Slot | Slot number on the rack in which the hardware component is inserted. |

### Assign process image/process image partition (S7-300, S7-400)

#### Introduction

For S7-300/400, if input addresses and output addresses are contained in a process image, they can either be in the OB1 process image (OB1-PI) or in a process image partition (PIP).

A process image offers the advantage that you can access a consistent image of process signals during cyclic program execution. For S7-300/400, you can choose between "OB1-PI" and "PIP 1" to max. "PIP 15".

Each input/output address that you have assigned to a process image partition with STEP 7 no longer belongs to the OB 1 process image input/output! Input/output addresses can be assigned only once across the OB 1 process image and all process image partitions.

You define the process image partition during address assignment (which input/output addresses of modules are managed in which process image partition). The process image partition is updated either by the user with the help of instructions or automatically by the system by connection to an OB. Exception: process image partitions of isochronous mode interrupt OBs are not updated by the system, even though they are connected to an OB (OB 61 to OB 64).

You can update each process image partition in the user program with special instructions. Use "[UPDAT_PI](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#updat_pi-update-the-process-image-inputs-s7-300-s7-400)" (SFC 26) for the process image partition of inputs and "[UPDAT_PO](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#updat_po-update-the-process-image-outputs-s7-300-s7-400)" (SFC 27) for the process image partition of outputs.

You assign the connection of a process image partition to an OB in the properties of the CPU ("Interrupts" area).

> **Note**
>
> The option can only be selected for modules with inputs or outputs. In addition, the CPU must support process image partitions. The number of available process image partitions also depends on the CPU.

#### Requirement

- You are in the device view.
- The module is a compact DP slave or is inserted in one of the following objects:

  - Central rack
  - Expansion rack
  - DP slave
- The CPU allows free address assignment.

#### Procedure

To change the preset process image range, proceed as follows:

1. In the device view, select the module whose start address you want to set.
2. Click on "I/O Addresses" under "Properties" in the Inspector window.
3. Under "Process image," select the desired process image.

> **Note**
>
> If the entry "- - -" is visible in the "Process image" field (not changeable), this means that a process image is not available for the specified address range.
>
> - For digital input or output modules, select a lower start address.
> - If an analog module is to be addressed in a process image, then also select a lower start address. Shifting of the start address to the area of the address range for process images must be supported by the CPU.
> - If the size of the process image can be specified for a CPU (via parameter assignment), then you can enlarge the process image (cycle properties of the CPU), so that the entered address is again in the process image. The parameter is called "Size of the process image...".

### Assign process image/process image partition (S7-1500)

#### Introduction

A process image offers the advantage that you can access a consistent image of process signals during cyclic program execution. For S7-1500, you can choose between "Update automatically" and "PIP 1" to max. "PIP 31".

#### Assigning addresses to the automatically updating process image area

You define the process image during address assignment (inspector window, "I/O addresses" area). The following setting should be selected if the addresses of a module are to lie in the process image area that is updated automatically by the system in each program cycle:

![Assigning addresses to the automatically updating process image area](images/47920220683_DV_resource.Stream@PNG-en-US.png)

For comparison: For S7-300/400 modules, this setting is called "OB1 process image".

If the addresses should not lie in the process image area, select "None" as the process image.

#### Assigning an address to a process image partition

You define the process image partition during address assignment (inspector window, "I/O addresses" area). The process image partition is updated either by the user with the help of instructions or automatically by the system by connection to an OB.

#### Connecting a process image partition to an OB

You also connect a process image partition to an OB in the I/O addresses area ("Organization block" parameter).

For OBs of the type "Cyclic Interrupt", for example, the next free process image partition is assigned automatically; this can be changed, however. After the OB has been started, the assigned process image partition of inputs is updated by the system. At the end of the OB, the outputs of the assigned process image partition are written to the I/O outputs by the system. The process image partitions are excluded from the automatic update.

Example for the coupling of the process image partition 2 (PIP 2) to a cyclic interrupt:

![Connecting a process image partition to an OB](images/47944097419_DV_resource.Stream@PNG-en-US.png)

**Exception**: process image partitions of isochronous mode interrupt OBs are not updated by the system, even though they are connected to an OB (OB 61 to OB 64).

The assigned process image or process image partition is displayed in the properties of the assigned OB (cannot be changed).

#### Updating a process image partition in the user program

You can update each process image partition in the user program with special instructions. Use "UPDAT_PI" for the process image partition input and "UPDAT_PO" for the process image partition output.

#### Requirement

- You are in the device view.
- The module or submodule has an I/O address.

#### Procedure

To change the preset process image range, proceed as follows:

1. In the device view, select the module whose start address you want to set.
2. In the inspector window, click on the "I/O Addresses" area under "Properties".
3. Under "Process image," select the desired process image.

### Using process image partitions in instructions (S7-1500)

#### Introduction

Instructions such as "UPDAT_PI" for updating process image partition inputs and "UPDAT_PO" for outputting process image partition outputs to I/O outputs use the "PART" input parameter for inputting the process image partition.

In the following section we show you how to define a user constant for a process image partition and how to use it for inputting the process image partition in the user program. If you use different process image partitions for your I/O configuration, the symbols makes programming easier.

#### Requirement

You have configured the I/O, assigned addresses and process image partitions, and created the required blocks.

The programming language is set to LAD for this example.

#### Procedure

Follow these steps:

1. Open the tag table and enter constants of data type "Pip" (process image partition) in the "User constants" tab. For each process image partition used, assign a name and, if necessary, a comment.

   ![Procedure](images/48042610187_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/48042610187_DV_resource.Stream@PNG-en-US.png)
2. Open the program editor (e.g., by double-clicking an OB in the project tree).
3. Use a drag-and-drop operation to move the UPDAT_PI instruction to the network.
4. Double-click the PART input parameter to open the tag selection.

   Only process image partition constants will be listed in the tag selection.
5. Select the desired process image partition.

   ![Procedure](images/47898384139_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/47898384139_DV_resource.Stream@PNG-de-DE.png)

### Assigning addresses to a location in the program (S7-300, S7-400, S7-1500)

You can assign addresses of the I/O channels of modules directly to the points of use in the program or to a tag table.

#### Requirement

- The device view of the hardware and network editor is open.
- The zoom level in the device view must be set to at least 200% to allow you to see the individual I/O channels.
- The instruction window of the programming editor or a tag table is open.

#### Procedure

To assign I/O channels of modules to the points of use in the program or to a tag table, follow these steps:

1. In the device view, navigate to the module with the desired I/O channel.
2. Click and hold down the mouse button to drag the desired I/O address to the corresponding point of use of the block or to the tag table.

The address of the module is assigned to the point of use in the program or entered as a tag in the tag table.

> **Note**
>
> The tag for an input or output of a block can also be dragged to the input or output of a module in order to link the tag to the I/O channel of the module.

![Procedure](images/25664478219_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The location of a block was dragged to an I/O channel. |
| ② | The name of an I/O channel was dragged to a point of use in the program. |
| ③ | Hold down the mouse button and drag from the name of an I/O channel to the input of a block. |

---

**See also**

[Overview of PLC tag tables](Declaring%20PLC%20tags.md#overview-of-plc-tag-tables)

### Assigning addresses to a location in the program (S7-1200)

You can assign addresses of the I/O channels of modules directly to the points of use in the program or to a tag table.

#### Requirement

- The device view of the hardware and network editor is open.
- The zoom level in the device view must be set to at least 200% to allow you to see the individual I/O channels.
- The instruction window of the programming editor or a tag table is open.

#### Procedure

To assign I/O channels of modules to the points of use in the program or to a tag table, follow these steps:

1. In the device view, navigate to the module with the desired I/O channel.
2. Click and hold down the mouse button to drag the desired I/O address to the corresponding point of use of the block or to the tag table.

   ![Procedure](images/13010265995_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/13010265995_DV_resource.Stream@PNG-en-US.png)

The address of the module is assigned to the point of use in the program or entered as a tag in the tag table.

> **Note**
>
> The tag for an input or output of a block can also be dragged to the input or output of a module in order to link the tag to the I/O channel of the module.

---

**See also**

[Overview of PLC tag tables](Declaring%20PLC%20tags.md#overview-of-plc-tag-tables)

## Configuring the Web server (S7-1200)

This section contains information on the following topics:

- [Information about the web server (S7-1200)](#information-about-the-web-server-s7-1200)
- [Standard web pages (S7-1200)](#standard-web-pages-s7-1200)
- [Creating and loading user pages (S7-1200)](#creating-and-loading-user-pages-s7-1200)

### Information about the web server (S7-1200)

#### Introduction

The Web server allows you to monitor the CPU via the Internet or the intranet of your company. This permits evaluation and diagnostics over long distances.

Alarms and status information are visualized on HTML pages.

#### Web browser

You need a web browser to access the HTML pages of the CPU.

The information with which Web browsers and Web browser versions the Web server was tested is available in the corresponding [manual](http://support.automation.siemens.com/WW/view/en/36932465).

#### Reading information via the Web server

The following information can be read from the CPU. The availability of the respective web pages depends on the CPU and its firmware version.

As of firmware version 4 the web pages are available in several languages.

| Page/information | Description |
| --- | --- |
| Introduction | Entry page for the standard web pages |
| Start page with general CPU information | The start page provides an overview of general information on the CPU, the name of the CPU, the type of CPU and basic information on the current operating state. |
| Diagnostics | Display of the detailed information about the CPU including the serial number, article number and version numbers.  Displays the content of the diagnostics buffer with the most recent entries first. |
| Module information | Display of the identification information whether the centrally inserted components of a station are OK, whether there are maintenance requirements or components cannot be reached, for example.  As of firmware version 4 a firmware update is possible via this Web page. |
| Communication | Displays the communication connections during open communication (OUC); displays resources and address parameters. |
| Diagnostic buffer | Display of the diagnostic buffer content |
| Tags | Displays the status of operands of the user program to monitor and change the values. |
| File browser   (as of firmware version 4) | Data logs in CSV format to transfer to the hard disk of the programming device. The data logs are created with data log instructions in the user program and filled with data.   As of firmware version 4 you have access to files of the internal load memory and of the external load memory (Memory Card) via this web page, for example, to the content of the directories "DataLogs" and "Recipes". |
| Login | Login as a user or logoff. |
| User pages (if user-defined web pages have been configured and loaded) | The user web pages deliver a list of web pages with customer-specific web applications. |
|  |  |

#### Web access to the CPU via PG/PC

Proceed as follows to access the Web server:

1. Connect the client (PG/PC) to the CPU via the PROFINET interface.
2. Open the web browser.

   Enter the IP address of the CPU in the "Address" field of the Web browser in the format http://ww.xx.yy.zz (example: http://192.168.3.141).  
   The start page of the CPU is opened. From the start page, you can navigate to further information.

### Standard web pages (S7-1200)

This section contains information on the following topics:

- [Requirements for web access (S7-1200)](#requirements-for-web-access-s7-1200)
- [Settings for operation (S7-1200)](#settings-for-operation-s7-1200)
- [Access for HTTPS (S7-1200)](#access-for-https-s7-1200)
- [Web server security (S7-1200)](#web-server-security-s7-1200)
- [Accessing data of the CPU memory (S7-1200)](#accessing-data-of-the-cpu-memory-s7-1200)

#### Requirements for web access (S7-1200)

The requirements for access to standard CPU web pages are explained in the following, as well as the effects of missing or existing configuration information.

##### Requirement

The web server must be started.

The web server only starts when it has been activated in the properties of the CPU in the "Web server" section.

Note the following:

The web pages are normally transmitted via an non-secure connection and are not secured against hacker attacks. If you want to transfer the web pages in encrypted form to the browser, use the URL https://, followed by the IP address of the CPU.

##### Logon

No logon is required to access the standard web pages read-only. A user must be logged on to execute certain actions like changing the operating mode of the CPU or for write access.

**For S7-1200 CPUs up to FW version V3**:

You must be logged on as "admin" for the actions listed above. The logon input boxes are on the top left of each standard web page.

![Logon](images/23550810123_DV_resource.Stream@PNG-de-DE.png)

If you log on as "admin", you must enter the user name and password there.

Name: admin.

Password: configured CPU password (for password-protected CPU).

**For S7-1200 CPUs as of FW version 4**:

You can freely select the names of users and the passwords (CPU parameter "Web server", area "User management").

You assign rights to the users, for example the right to query diagnostics or to update the firmware.

##### JavaScript and cookies

The standard web pages use JavaScript and cookies. You must enable both in your web browser.

If JavaScript is not enabled, the following limitations apply:

- Data from standard web pages is not automatically updated.
- You cannot log on as user.
- Fields cannot be sorted (module information)

If cookies are not enabled, you cannot log on.

---

**See also**

[Access for HTTPS (S7-1200)](#access-for-https-s7-1200)

#### Settings for operation (S7-1200)

##### Settings for operation

To be able to use the web server of an S7-1200-CPU, you must select the CPU in the network view or the device view and make the following settings in the inspector window under "Properties > General > Web server":

- Enable the web server
- Restricting access to the CPU to HTTPS transmission protocol (encrypted transmission)

  Access via port 80 is then blocked. Communication is only possible via port 443.
- Enabling automatic update of web pages

  The update interval is set by default and cannot be changed. The CPU updates web pages with changing content ( (for example, status information or diagnostics information) at regular intervals.
- Creating and managing users

  Users are exclusively entitled to options that are assigned to the access rights.  
  Depending on the CPU and firmware used, you can assign different user rights. Rights that your CPU does not support cannot be activated. A user called "Everybody" with minimal access rights, that you can, however, extend, is set by default in the user list. A user who uses the Web server without entering a password has "Everybody" user rights.

  You have the possibility of configuring further users with different access rights. These users have to log on with the configured user name and password.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Unauthorized access to the CPU by means of the Web server**  Unauthorized access to the CPU or the changing of PLC variables to invalid values can result in interruptions of the processes controlled by the CPU and cause death, serious bodily harm or material damage!  Since the activation of the Web server allows authorized persons for example to change operating modes, to write-access CPU data or to update the firmware, we recommend that the following security measures be taken: - If possible limit access to the HTTPS protocol. - Create users with secure passwords. An example of a secure password is one which is only used for a single application, is more than 8 characters long, and consists of lower- and upper-case letters as well as symbols and numbers (?!+%$1234...). In addition, passwords based on common keyboard sequences or words from the dictionary should be avoided. Change the password at regular intervals. - Do not extend the rights of the "Everybody" user. - Check the PLC variables in the user program and limit the range of values to permissible ranges since users can set invalid values via the Web server. |  |

#### Access for HTTPS (S7-1200)

##### Access via HTTPS

HTTPS is used for encrypting and authentication of communication between the browser and web server.

To transfer data between the browser and the CPU using the HTTPS protocol, enter the URL as https://ww.xx.yy.zz in the address line of your browser, whereby ww.xx.yy.zz stands for the IP address of the CPU.

You require a valid, installed certificate for error-free HTTPS access to the CPU.

If no certificate is installed a warning is displayed with a recommendation not to use this page. To view the page you must explicitly "Add exception".

You can receive a valid certificate (Certification Authority) "SIMATIC CONTROLLER" as a download from the "Intro" web page under "Download certificate". The help function for your respective web browser provides information on how to install a certificate.

---

**See also**

[Web server security (S7-1200)](#web-server-security-s7-1200)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

#### Web server security (S7-1200)

##### Web server security settings

As of TIA Portal version V17 (and from firmware version V4.5 of the S7-1200 CPUs), you have additional options for setting the type and how you purchase certificates for the CPU.

If the web server of the CPU is enabled (HTTPS protocol is default), you have to specify in the properties of the CPU which type of certificate the web server should use (CPU properties, "Web server > Security" area):

- Hardware generated  
  This is a self-signed certificate generated by the CPU. This option corresponds to the certificate that was automatically generated and used by the CPU prior to the introduction of certificate management. Use a hardware-generated certificate only in a secure environment.
- Software downloaded  
  This is a manually generated certificate. In the expanded "Server certificate" field, you can select an existing certificate in the TIA Portal or create a new certificate.   
  When you create a new certificate, you can create a self-signed certificate or a certificate signed by a Certificate Authority (CA). To do this, click the "Add" button in the expanded "Server certificate" field.

  - Create self-signed certificate  
    Self-signed certificates can be created without having to protect the project and without the global security settings. Unprotected projects only allow for the creation of self-signed certificates. However, many clients do not trust self-signed certificates because they are not embedded in a PKI infrastructure and do not provide secure authentication of the Web server. Therefore, only use self-signed certificates in a secure environment, such as when only internal and authorized employees can access the Web server of the CPU.
  - CA certificate  
    To be able to create CA certificates in the TIA Portal, you need to activate project protection:

    To do this, select "Security settings > Settings" in the project tree and protect the project with a password. The global security settings for the certificate manager must be activated in the "Protection & Security > Certificate manager" area of the CPU properties.

    When creating the certificate, select the "Signed by certification authority" option.

    This certificate option provides the most comprehensive protection.

  "Software downloaded" certificates are downloaded to the CPU with the project. If you connect to the Web server of the CPU using a Web browser (client), the start page of the Web server provides a link to download the certificate. Follow the instructions for your browser to import and install certificates.

##### Configuration limits of certificates

The S7-1200 CPU supports up to 64 certificates.

- All types of certificates count towards the maximum possible number of certificates. Counting is independent of the application that uses the certificates (Web server, Secure Open User Communication, OPC UA).
- If you are using a CA certificate, the CPU also requires the certificate of the certification authority that signed the CA certificate. Include these additional certificates when counting; the maximum number of possible certificates may be reached more quickly this way.

##### Certificate parameter restrictions

The following settings are **not** supported for a certificate from the S7-1200 CPU even though they can be set:

- EC encryption method with encryption parameter secp384r1
- RSA encryption method with encryption parameter 4096 (cryptographic key length) or greater

It is possible that the web server cannot be reached with these settings after loading the hardware configuration.

---

**See also**

[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

#### Accessing data of the CPU memory (S7-1200)

You can access data in the internal or external CPU load memory by means of a standard web page.

- Use the web page "Data logs" for S7-1200 CPUs up to and including FW version 3. From this web page, you transfer the data logs from the CPU to a drive on your PC.
- Use the web page "File Browser" for S7-1200 CPUs as of FW version 4. From this web page, you transfer data from the folders "Data logs" or "Recipes", for example, to a drive on your PC.

Depending on the file type and the access permissions you have configured for the web server user, you can download, delete, rename or upload the files. The actual directories can only be created, deleted or renamed.

##### Example: Data logs

To open a data log, click on the link of the desired data log. You can then open the file (.csv), for example, in Microsoft Excel or in another program you choose or you can save the file.

Special note: Data logs are saved in U.S. American CSV format. You can only open the file directly using the U.S. version of Microsoft Excel. If you are using another national version of Microsoft Excel, you must import the file, selecting "comma" in the import assistant as the delimiter.

##### Downloading a data log

To download a data log, click on the download icon of the desired data log. You can then open the file (.csv), for example, in Microsoft Excel or in another program you choose or you can save the file.

##### Downloading and clearing or deleting a data log

For a CPU with FW version up to V3.0:

To download and delete the current entries of the data log, you must be logged on. To do this, click on the "Download and delete" icon of the required data log. You can then open the file (.csv), for example, in Microsoft Excel or in another program you choose or you can save the file.

For a CPU as of FW version V4.0:

To reset the data log, follow these steps:

1. Open the CSV file, for example with Excel.
2. Delete the rows between the headline and the row with the entry "//END", if this row exists.
3. Save the file to a drive on your PC.
4. On the web page "File Browser", delete the data log (which means the CSV file) and load the prepared CSV file to the CPU with the "Upload file" button of the "File Browser" web page.

Additional information is available in the S7-1500 CPU system manual.

---

**See also**

[Data logging - Overview (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#data-logging---overview-s7-1200-s7-1500)

### Creating and loading user pages (S7-1200)

This section contains information on the following topics:

- [What you need to know about user pages (S7-1200)](#what-you-need-to-know-about-user-pages-s7-1200)
- [Procedural overview (S7-1200)](#procedural-overview-s7-1200)
- [Creating web pages (S7-1200)](#creating-web-pages-s7-1200)
- [AWP commands for controlling Web pages (S7-1200)](#awp-commands-for-controlling-web-pages-s7-1200)
- [Creating and loading a data block (S7-1200)](#creating-and-loading-a-data-block-s7-1200-1)
- [Structure of the PLC program (S7-1200)](#structure-of-the-plc-program-s7-1200)
- [Web Control DB (S7-1200)](#web-control-db-s7-1200)
- [Interaction with the user program (S7-1200)](#interaction-with-the-user-program-s7-1200)
- [Displaying custom web pages in the browser (S7-1200)](#displaying-custom-web-pages-in-the-browser-s7-1200)
- [Creating custom web pages in several languages (S7-1200)](#creating-custom-web-pages-in-several-languages-s7-1200)
- [Selecting an entry page (S7-1200)](#selecting-an-entry-page-s7-1200)
- [Language switching for custom web pages (S7-1200)](#language-switching-for-custom-web-pages-s7-1200)
- [Example of language switching (S7-1200)](#example-of-language-switching-s7-1200)
- [Additional examples (S7-1200)](#additional-examples-s7-1200)

#### What you need to know about user pages (S7-1200)

##### Concept

The concept of user pages or of user-defined web pages allows you to access freely-designed web pages of the CPU with a web browser. The Web server of the CPU provides this function.

You are not dependent on special tools for the design and functionality of the user-defined web pages. You can adapt the pages in the layout with CSS, provide dynamic content with JavaScript or use any framework to produce web pages. The totality of files processed by the Web server is also referred to as the "web application".

##### Web application and user program

Using HTML code in user-defined web pages (AWP commands), you can also transmit data via a web browser to the user program of the CPU for further processing and can display data from the operand area of the CPU in the web browser.

You can use script instructions (such as Javascript) to optimize your web pages, for example to dynamically change contents or validate user entries.

To synchronize between the user program and the Web server, but also to initialize, you must call the WWW (SFC 99) instruction in the user program.

- If no interaction is required between the web application and the user program, for example, if a web page only provides static information, only initialization in the user program is required.
- If a simple data exchange is necessary between PLC tags and tags in web applications, to display the contents of PLC tags or write a value in a PLC tag for example, the syntax for reading and writing tags has to be observed. In this case only an initialization is required in the user program, for example in the startup OB.
- If a further interaction is required between the web application and the user program, you must handle status and control information from the Web Control DB in addition to the synchronization between Web server and user program. This is the case, for example, when user entries are transmitted via the web browser to the Web server for evaluation by the CPU. Unlike simple data exchange, the user program directly influences the time at which the requested web page is relayed back to the web browser. In this case, you must be acquainted with the concept of manual fragments and the structure of the Web Control DB.

##### Integration of the HTML sources via the TIA Portal

The parameters for an integration of the HTML sources in the TIA Portal are located in the properties of the respective CPU with Web server:

| Parameter | Meaning |
| --- | --- |
| HTML directory | Directory of the HTML sources for the web applications. You can input the path directly or navigate to the directory by using the button next to the entry field.   It is advantageous if you integrate your Web pages with relative paths. To do this you have to insert the directory in which you store the HTML sources for the Web application in the STEP 7 project directory, for example, in a new directory "Webpages". You then specify the relative path name as the HTML directory; in the example ".\Webpages".   Advantages of using relative paths:   - The user-defined Web pages are archived together with the STEP 7 project. - The Web pages are copied to the new path with the menu command "Project > Save as...". - When copying the project to another path using the Windows Explorer, it is no longer necessary to adapt the HTML directory path to generate new Web DBs. - Several control systems in a project that use the same HTML pages also have the same HTML directory path information. |
| Start HTML page | Path to the Start HTML page. You can input the path directly or navigate to the HTML page with the button next to the entry field. The start HTML page is the HTML page to be opened at the start of the web application. |
| Application name | Optional name for the application. This name is used to further divide or group the web pages. When an application name already exists, the URL is displayed in the following format:"http://a.b.c.d/awp/<Application name>/<Page name>.html" |

##### Initialization

User-defined web pages are "packaged" in data blocks for processing by the CPU. You must generate appropriate data blocks from the source data (HTML files, images, JavaScript files, etc.) during configuration to be able to download the web application into the CPU. The Web Control DB takes on a special role (default: DB 333). It contains status and control information as well as links to additional data blocks with coded web pages. Data blocks that contain coded web pages are termed "Fragment DBs".

When the data block is downloaded into the CPU, the CPU does not "know" that user-defined web pages are coded inside it. The "WWW" (SFC 99) instruction, for example, in the Startup OB informs the CPU which DB is the Web Control DB. The user-defined web pages can be accessed via a web browser after this initialization.

##### Synchronization

If the user program is to exchange data with the user-defined web pages, the WWW (SFC 99) instruction must be used in the cyclic program section.

Examples of interaction between user program and web page:

- Check received data
- Assemble and send back data to the web browser making the request

In this case, the status information must be able to be evaluated and control information must be transmitted to the Web server, for example, to release a requested web page.

#### Procedural overview (S7-1200)

##### Basic information

This section provides a step-by-step explanation of the basic procedure used to create and download custom web pages and to use them in the operating phase.

The following graphic provides a simplified representation of the process used in creating and displaying custom web pages:

![Basic information](images/23546333323_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Programming a web application (using suitable tools when required and AWP commands for dynamic pages when applicable). |
| ② | The web application is comprised of single source files, for example, *.html, *.gif, *.js, etc. |
| ③ | Using STEP 7:  - Generate the data blocks (Web Control DB and fragment DBs) from source files. The DBs contain meta information and the complete web application, including the images and the dynamic and static parts of the web application. The DBs are stored under "System blocks" in the project tree. - Call the "WWW" instruction in the user program. This instruction initializes the web server of the CPU for a web application. - If required, complete final programming for interaction between the web server and user program |
| ④ | Downloading the blocks to the CPU. |
| ⑤ | Call the web page in the browser. The web pages of the CPU are called by entering the IP address of the CPU. |

##### Additional information

You can find additional information and examples relating to the S7-1200 web server on the [Internet](http://support.automation.siemens.com/WW/view/en/36932465).

#### Creating web pages (S7-1200)

Web design tools from various companies can be used to create user-defined web pages. As a rule, the web pages should be programmed and designed compliant to the conventions of the W3C (World Wide Web Consortium). No check is made for compliance to W3C criteria in the web server of the CPU.

##### Rules

- The tool must be able to directly edit the HTML code so that the AWP command can be inserted into the HTML page.

  Only the AWP commands are parsed in the CPU and, for example, replaced by values from the user program/process image of the CPU.
- Files containing AWP commands must be coded in UTF-8. In the metadata of the HTML page, therefore, set the attribute charset to UTF-8 and save the file UTF-8 coded.
- Files containing AWP commands must not contain the following sequence: ]]
- Files containing AWP commands must not contain the following sequence outside of the "Tag read ranges" (:=<Tag name>:): :=

  Tip: Replace the first character of a prohibited sequence with its character coding; for the colon, for example, &#58;.

A small example for a custom web page should make clear the basic design.

##### Requirement

- The CPU must have a web server and the web server of the CPU must be activated.
- To be able to access PLC tags with write access as a user, you must be logged on as "admin".
- For the example below, PLC tags must be defined for those PLC tags that are to be shown on the web page. This is shown here for the first tab used, "Tank_below_max".

  ![Requirement](images/21252750603_DV_resource.Stream@PNG-en-US.png)

##### Creating user-defined web pages

The following code for an example web page reads values from the process image and provides them in a table.

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">  
<html>  
 <head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<title>Mix</title>

</head>

<body>

<h1>Mix</h1>

<h2> Actual State </h2>

<table border="1">

<tr>

<th>Variable</th>

<th>State</th>

</tr>

<tr>

<td>Tank below max</td>

<td>:="Tank_below_max":</td>

</tr>

<tr>

<td>Tank above min</td>

<td>:="Tank_above_min":</td>

</tr>

</table>

</body>

</html>

#### AWP commands for controlling Web pages (S7-1200)

This section contains information on the following topics:

- [Using AWP commands in Web pages (S7-1200)](#using-awp-commands-in-web-pages-s7-1200)
- [Reading tags (S7-1200)](#reading-tags-s7-1200)
- [Writing tags (S7-1200)](#writing-tags-s7-1200)
- [Special tags (S7-1200)](#special-tags-s7-1200)
- [Enumeration types (S7-1200)](#enumeration-types-s7-1200)
- [Simplified use of enumeration types (S7-1200)](#simplified-use-of-enumeration-types-s7-1200)
- [Definition of fragments (S7-1200)](#definition-of-fragments-s7-1200)
- [Importing fragments (S7-1200)](#importing-fragments-s7-1200)
- [Creating and loading a data block (S7-1200)](#creating-and-loading-a-data-block-s7-1200)

##### Using AWP commands in Web pages (S7-1200)

With AWP (Automation Web Programming) commands, you declare the interface between your user pages (Web application, e.g. a simple HTML page) and the CPU data.

To develop user pages or Web applications, you need only observe the restrictions of the Web browser. In one of the programming languages of STEP 7, control with the user program in the CPU which CPU data is displayed at what time in the Web browser of the viewer.

Use AWP commands, which you comment within the HTML page, to declare data to be used for intentional interaction between the Web application and the user program.

You insert AWP commands as HTML comments with a special syntax into HTML pages. Using AWP commands, the following features can be implemented:

- Read PLC tags
- Write PLC tag
- Read special tags
- Write special tags
- Define enum types
- Assign tags to enum types
- Defining fragments
- Import fragments

###### Syntax of AWP commands

An AWP command begins with "`<!-- AWP_`" and ends with " `-->`". In JavaScript files, the commands should also be enclosed by JavaScript comments ("`/*...*/`").

###### Notation rules for PLC tag names within an AWP command

The AWP commands "AWP_In_Variable" and "AWP_Out_Variable" contain a name attribute and optionally a use attribute. A PLC tag name is assigned to these attributes, by means of which the PLC tags in the browser are written or read. The following rules apply to handling PLC tag names in HTML code:

- PLC tags must be enclosed in quotation marks (" ... ").
- PLC tags used in AWP commands must also be enclosed by single quotation marks ('" ... "') or with quotation marks masked by a backslash ("\" ... \"").
- If the PLC tag name contains the character \ (backslash) or * (star), this character must be designated with the escape sequence \\ as standard character of the PLC tag name. See below for examples.
- If the PLC tag name in the AWP command is also enclosed by single quotation marks and the single quotation mark (') occurs within the name, it must also be designed as normal character by the escape sequence \'.
- If an absolute address (input, output, bit memory) is used in AWP command, it is enclosed by single quotation marks.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "Velocity" | <!-- AWP_In_Variable Name='"Velocity"' -->  <!-- AWP_In_Variable Name="\"Velocity\"" --> |
| "abc\de" | <!-- AWP_In_Variable Name='"abc\\de"' --> |
| "abc'de" | <!-- AWP_In_Variable Name='"abc\'de"' --> |
| "abc'de" | <!-- AWP_In_Variable Name="abcde" Use'"abc\'de"' --> |
| "DB name".tag | <!-- AWP_In_Variable Name='"DB name".tag' --> |
| "Plc1".Data[1].typeDataStruct.value | <!-- AWP_In_Variable Name='"Plc1".Data[1].typeDataStruct.value' --> |
| - | <!-- AWP_Out_Variable Name=’flag1’ Use='M0.0' --> |

---

**See also**

[Reading tags (S7-1200)](#reading-tags-s7-1200)
  
[Writing tags (S7-1200)](#writing-tags-s7-1200)
  
[Special tags (S7-1200)](#special-tags-s7-1200)

##### Reading tags (S7-1200)

User-defined web pages can read PLC tags.

The PLC tag must be specified by a PLC tag name.

These OUT variables (direction of output as viewed from the controller) are inserted at any location within the HTML text with the syntax described in the following.

###### Syntax

:=<varname>:

These references are replaced when the Web server is in operation by the current values of the PLC tag in each case.

`<varname>` can be a simple, global PLC tag but also a complete tag path to a structural element.

###### Notation rules for PLC tag names

- PLC tags in HTML code are enclosed by quotation marks ("), if they are defined in the tag table. In the case of data block tags, the name of the data block is enclosed by quotation marks. If special characters are used in the structure elements of the data block, for example the dot (.) or blank, this part must also be enclosed by quotation marks.
- Quotation marks are not used for absolute addresses of inputs, outputs or bit memories.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "DB_name".var_name | :="DB_name".var_name: |
| "DB_name"."var.name" | :="DB_name"."var.name": |
| "memory" | :="memory": |
| - | :=I0.0:  :=Q0.0:  :=MW100:  :=%MW100: |
| "My_Data_Block".flag1 | <!-- AWP_Out_Variable Name='flag1' Use='"My_Data_Block".flag1' -->  ...  :=flag1: |

- If the PLC tag name contains the character : (colon) or \ (backslash), this character must be designated with the escape sequence \: or \\ as standard character of the PLC tag name.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "abc:de" | :="abc\:de": |
| "abc\de" | :="abc\\de": |

- Special characters "<, &, >"

  Display problems can occur if these characters are contained in the tag name (for example, "a<b").

  Avoid expressions such as :="a<b": in the HTML page.

  To prevent display problems from occurring, use e.g. an AWP command with a use expression according to the pattern depicted below. The use attribute defines the PLC tag with the problematic character, the name attribute defines the name without problematic character, as it is used in the HTML page.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "a<b" | <!-- AWP_Out_Variable Name='simplename' Use='"a<b"' -->  ...  :=simplename: |

---

**See also**

[Using AWP commands in Web pages (S7-1200)](#using-awp-commands-in-web-pages-s7-1200)

##### Writing tags (S7-1200)

Custom web pages can write data into the CPU.

This requires an AWP command that identifies the PLC tag to be written.

The PLC tag must also be specified by a PLC tag name.

The IN tags (direction of input as viewed from the controller) are placed on the browser page. This can be done, for example, in a form.

The tags are either set in the HTTP header (by cookie or POST method) or in the URL (GET method) by the browser and are then written by the Web server into the respective PLC tag.

###### Syntax

To allow the IN tags to be written to the CPU, the tags must first be defined by an explicit AWP instruction:

<!-- AWP_In_Variable Name='<PLC_Varname1>' Name='<PLC_Varname2>' Name='<PLC_Varname3>' -->

Several tags can be defined in an instruction - such as that shown above.

The specific PLC tag name is hereby written in double quotation marks; for example <PLC_Varname1> = "myVar".

In cases where the name of the tag that you use for the web application is not identical to the name of the PLC tag, the "Use" parameter can be used to assign to a PLC tag:

<!-- AWP_In_Variable Name=’<Webapp_Varname>’ Use=’<PLC_Varname>’

###### Example

The "AWP_In_Variable" AWP command is indispensable when handling forms.

<form method='post' action='/awp/appl/x.html'>

<p>

<input name='"var1"' type='text'>

<input value='set' name='Button1' type='submit'>

</p>

</form>

In the form defined above, the HTTP request method "post" is used to transfer the tag "var1" to the Web server. The user places the "var1" tag in the form field. The tag 'Button1' has the value 'set', but is not required for the CPU. To allow the "var1" tag to be written to the CPU, the following instruction must be included in the same fragment:

<!-- AWP_In_Variable Name='"var1"' -->

Since PLC tags are enclosed in double quotation marks ("), the name in the AWP command must be enclosed in single quotation marks (') or in masked quotation marks (\"). To avoid the numerous escape sequences, we recommend the use of single quotation marks.

<!-- AWP_In_Variable Name=’"Info".par1’ -->

<!-- AWP_In_Variable Name="\"Info".par1\"" -->

###### Conditions for write access during operation

The following requirement has to be met in order for a user to be able to write to PLC tags from a user-defined web page:

The user must have rights to change tags. The Web server ignores the commands if the user has no change rights.

This rules applies to all writing access to web pages on a CPU.

---

**See also**

[Requirements for web access (S7-1200)](#requirements-for-web-access-s7-1200)
  
[Using AWP commands in Web pages (S7-1200)](#using-awp-commands-in-web-pages-s7-1200)

##### Special tags (S7-1200)

Special tags are mainly HTTP tags set in the definition of the World Wide Web Consortium (W3C) . Special tags are also used for cookies and server tags.

The AWP command to read and write special tags differ only in that they have additional parameters than the AWP command used to read and write normal tags.

###### Reading a special tag

The Web server can read PLC tags and transfer these to special tags in the HTTP Response Header. You can, for example, read a URL for a diversion to another web page and transfer to the special tag HEADER:Location using the special tag HEADER:Location.

The following special tags can be read:

| Name | Description |
| --- | --- |
| COOKIE_VALUE:name | Value of cookie with name: "name" |
| COOKIE_EXPIRES:name | Execution time of cookie with name: "name" in seconds (must be set beforehand). |
| HEADER:Status | HTTP status code (if no other value has been set, status code 302 is returned). |
| HEADER:Location | Path for forwarding to another page. Status code 302 must be set. |
| HEADER:Retry-After | Anticipated time in which the service is not available. Status code 503 must be set. |
| HEADER: … | All other header tags can also be forwarded in this way. |

Use the AWP command "AWP_Out_Variable" to specify which PLC tags are to be transferred in the HTTP header to the web browser.

Basic structure:

<!-- AWP_Out_Variable Name="<Typ>:<Name>" [Use="<Varname>"] -->

###### Parameter description

- Name: Type and name of special tag
- Use (optional parameter): In cases where the name of the special tag is not identical to the name of the PLC tag, parameter "Use" can be used to assign to a PLC tag.

Example:

<!-- AWP_Out_Variable Name="COOKIE_VALUE:siemens" Use='"info".language' -->

###### Writing a special tag

In principle, all HTTP tags written in the HTTP header by the web browser can be evaluated by the user program of the CPU. Examples of tag types:

| Name | Description |
| --- | --- |
| HEADER:Accept-Language | Accepted or preferred language |
| HEADER:Authorization | Proof of authorization for a requested resource |
| HEADER:Host | Host and port of the requested resource |
| HEADER:User-Agent | Information on the browser |
| HEADER: … | All other header tags can also be forwarded in this way |
|  |  |
| SERVER:current_user_id | Indicates whether a user is logged on (current_user_id=0: no user logged on) |
| SERVER:current_user_name | User name of the user logged on |
| SERVER:GET | Request method is GET |
| SERVER:POST | Request method is POST |
|  |  |
| COOKIE_VALUE:name | Value of cookie with name: "name" |

The AWP command "AWP_In_Variable" is used to define which special tags are to be evaluated in the user program of the CPU.

Basic structure:

<!-- AWP_In_Variable Name="<Typ>:<Name>" [Use="<Varname>"] -->

Parameter description:

Name: Type and name of special tag

Use (optional parameter): In cases where the name of the special tag is not identical to the name of the PLC tag, the parameter Use can be used to assign to a PLC tag.

###### Examples:

<!-- AWP_In_Variable Name="COOKIE_VALUE:siemens" Use='"info".language' -->

The tag name in the HTTP header is replaced by the PLC tag name specified by Use . The cookie is written to the PLC tag "info".language .

<!-- AWP_In_Variable Name='COOKIE_VALUE:siemens' Use='"info".language' -->

The tag name in the HTTP header is replaced by the PLC tag name specified by Use. The cookie is written to the PLC tag "info".language .

<!-- AWP_In_Variable Name='"COOKIE_VALUE:siemens"' -->

The HTTP-header variable is written in the same-name PLC variable.

---

**See also**

[Using AWP commands in Web pages (S7-1200)](#using-awp-commands-in-web-pages-s7-1200)

##### Enumeration types (S7-1200)

###### Enumeration types (enums)

Numerical values from the PLC program can be converted into text and vice versa using enums. The numerical values can also be assigned for several languages.

###### Creating enums

Enter an AWP command using the following syntax at the start of the HTML file:

<!-- AWP_Enum_Def Name="<Name of the enum type>" Values='0:"<Text_1>", 1:"<Text_2>", ... , x:"<Text_x>"' -->

For example, for German values to be saved as an HTML file in the "de" folder of the HTML directory:

<!-- AWP_Enum_Def Name="Enum1" Values='0:"an", 1:"aus", 2:"Störung"' -->

For example, for English values, to be saved as an HTML file in the "en" folder of the HTML directory:

<!-- AWP_Enum_Def Name="Enum1" Values='0:"on", 1:"off", 2:"error"' -->

###### Assigning enums

Tags are assigned from the user program to the individual enum texts using a special AWP command:

<!-- AWP_Enum_Ref Name="<VarName>" Enum="<EnumTypeName>" -->

<VarName> is thereby the symbolic name from the user program and <EnumTypeName> is the previously set name of the enum type.

> **Note**
>
> In each fragment in which enum texts are referenced by a PLC tag, this PLC tag must be assigned by the appropriate AWP command of the enum type name.
>
> Ensure that no AWP command for importing fragments is positioned between an enum assignment and enum usage because this import can result in the enum assignment lying in a different fragment than the enum usage.

###### Example

Enum type "state" is defined with values "0" and "1". "0" means "off", "1" means "on":

<!-- AWP_Enum_Def Name="state" Values='0:"off", 1:"on"' -->

The following code is contained in the HTML code of the web page to be output:

<!-- AWP_Enum_Ref Name="operating state" Enum="state" -->

:=operating state:

Depending on the value of the "operating state" tag, the ´result displayed is no longer "0" or "1", but "off" or "on".

##### Simplified use of enumeration types (S7-1200)

At S7-1200 CPUs as of firmware version 4 it is possible to use enumerations directly in AWP commands to read and write PLC variables.

You create enums as described in the previous section, and you can then utilize the values with user program read and write commands.

###### Creating enums

<!-- AWP_Enum_Def Name="<Name des Enum Typs>" Values='0:"<Text_1>", 1:"<Text_2>", ... , x:"<Text_x>"' -->

###### Utilizing enums in the user program read and write commands

<!-- AWP_In_Variable Name='<Varname>' Enum="<EnumType>" -->

<!-- AWP_Out_Variable Name='<Varname>' Enum="<EnumType>" -->

###### Example of reading PLC tags

**<!-- AWP_Enum_Def Name='AlarmEnum' Values='0:"No alarms", 1:"Tank is full", 2:"Tank is empty"' --><!-- AWP_Out_Variable Name='"Alarm"' Enum="AlarmEnum" -->...<p>The current value of "Alarm" is :="Alarm":</p>**

If the value of "Alarm" in the CPU is "2", the following text will be displayed on the HTML page:

'The current value of "Alarm" is Tank is empty' because the enum definition assigns the string "Tank is empty" to the numerical value 2.

###### Example of writing PLC tags

**<!-- AWP_Enum_Def Name='AlarmEnum' Values='0:"No alarms", 1:"Tank is full", 2:"Tank is empty"' --><!-- AWP_In_Variable Name='"Alarm"' Enum='AlarmEnum' -->...**

**<form method="POST">**

**<p><input type="hidden" name='"Alarm"' value="Tank is full" /></p>**

**<p><input type="submit" value='Set Tank is full' /></p>**

**</form>**

Because the enum definition assigns the string "Tank is full" to the numerical value "1", the value "1" is written to the PLC tag "Alarm".

##### Definition of fragments (S7-1200)

###### Fragments

Fragments are "logical sections" of a web page to be processed by the CPU individually.

Fragments are usually complete pages but can also be individual elements such as files (for example, images) or complete documents.

###### Defining fragments

<!-- AWP_Start_Fragment Name="<Name>" [Type="<Type>"] [ID="<Id>"] [Mode=<Mode>]-->

The start of a fragment is specified by this command. A fragment runs to the start of the next fragment or to the end of the file.

- <Name> Indicates the name of the fragment.

  The name must start with a letter [a-zA-Z] or an underscore ( _ ). Letters, underscores or numbers [0-9] can follow after this first character.
- <Type> Indicates the type of the fragment.

  - "manual" The user program is informed of the request for a fragment; the web page to be returned can be changed by the user program.
  - "automatic" The page is automatically processed (default).
- <id> A numeric ID can be stipulated for the fragment. If no ID is assigned, the fragment is automatically assigned an ID. For manual pages (<Type>=manual) , the fragment can be addressed in the user program of the CPU by this ID.

  > **Note**
  >
  > Keep the ID low because the highest ID influences the size of the Web Control DB.
- <Mode> Fragments support the visible and hidden modes.

  - "visible" The fragment is a part of the web page. This mode is preset and can also be omitted.
  - "hidden" The fragment is not part of the web page. However, the fragment will be saved in the Web DB and is available to the user program for inserting in a requested web page. You use an exchange of the fragment ID (Web-Control-DB.fragment_index tag) to insert a "hidden" fragment in the requested web page.

The input document is completely divided into fragments by the "AWP_Start_Fragment" command. "AWP_End_Fragment" is therefore unnecessary.

Without a start fragment command, a file is mapped as a fragment; the fragment name is derived from the file name. If a file is divided into several fragments (by "AWP_Start_Fragment"), the file must begin with the "AWP_Start_Fragment" command.

##### Importing fragments (S7-1200)

You can declare a fragment in an HTML page and import this fragment into other web pages.

###### Example

A company logo is to be displayed on all web pages of a web application.

There is only one instance of the HTML code for the fragment that displays the company logo. You can import the fragment as often and into as many HTML files as required.

###### Syntax

<!-- AWP_Import_Fragment Name = "<name>"-->

- <name> is the name of the fragment to be imported.

###### Example

HTML code within a web page that declares a fragment:

<!-- AWP_Start_Fragment Name = "My_Company_Logo" -->

<p><img src = "compay_logo.jpg"></p>

###### Example

HTML code within another web page that imports the declared fragment:

<!-- AWP_Import_Fragment Name = "My_Company_Logo" -->

##### Creating and loading a data block (S7-1200)

###### Requirement

- All source files required for the web application (*.html, *.js, *.png, ...) have been created.
- The source files are located in one folder, but only those source files that are required for the web application. No other files may be located in this folder.

###### Procedure

To create data blocks from the source files for user-defined web pages in STEP 7, proceed as follows:

1. Select the CPU, for example, in the device configuration.
2. Select the properties for user-defined web pages in the inspector window under "Properties > General > Web server".
3. As "HTML source", select the folder that contains the source files for the web application.
4. Enter the HTMP page to be opened on starting the web application as the start HTML page.
5. Enter a name for the application if required.
6. You can supplement a range of file name extensions as "Files with dynamic content" if necessary. Only enter those file name extensions that also contain AWP commands.
7. The number for the Web Control DB and for the fragment DB start number can be kept as long as they are not already being used by your user program.
8. Click on the "Generate" button to create DBs from the source files.

   The generated data blocks are saved in the project navigation in the "System block" folder (in the "Web server" subfolder).
9. In the CPU, select the network view to be loaded and then select the "Download to device" command in the "Online" menu to download the blocks. Compilation of the blocks is implicitly initiated before downloading.

   If errors are reported during this process, you must correct these errors before you can download the configuration.

###### Tips for generating the web data blocks

When you click on the "Generate blocks" button in the area "Web server > User-defined pages", STEP 7 checks whether the corresponding web data blocks can be generated.

The following causes prevent the generation of web data blocks:

- Length of file names and tag names is too long

  If you have a comprehensive web application with many files and directories, the generation of the web data blocks may possibly fail. If this happens, the generation is aborted with the message "Text list overflow...". The cause is system-internal size limitations for management information saved in the web data block.

  Solution: Use short file names and short tag names.
- Files with dynamic content (file with AWP commands) are too large

  When the files with dynamic content (e.g. *.htm, *.html) are too large (for S7-1500 CPUs, e.g., larger than ca. 64 kB), you will see the following message "WebInt: Unable to read files for web application ..." with information on the file size and the path to the file that causes the error.

  Solution: Use the following AWP command to fragment the file:

  `<!-- AWP_Start_Fragment Name='<Fragmentname>' -->`

  The command divides the file internally into multiple segments that can be processed individually by the CPU.

#### Creating and loading a data block (S7-1200)

##### Requirement

- All source files required for the web application (*.html, *.js, *.png, ...) have been created.
- The source files are located in one folder, but only those source files that are required for the web application. No other files may be located in this folder.

##### Procedure

To create data blocks from the source files for user-defined web pages in STEP 7, proceed as follows:

1. Select the CPU, for example, in the device configuration.
2. Select the properties for user-defined web pages in the inspector window under "Properties > General > Web server".
3. As "HTML source", select the folder that contains the source files for the web application.
4. Enter the HTMP page to be opened on starting the web application as the start HTML page.
5. Enter a name for the application if required.
6. You can supplement a range of file name extensions as "Files with dynamic content" if necessary. Only enter those file name extensions that also contain AWP commands.
7. The number for the Web Control DB and for the fragment DB start number can be kept as long as they are not already being used by your user program.
8. Click on the "Generate" button to create DBs from the source files.

   The generated data blocks are saved in the project navigation in the "System block" folder (in the "Web server" subfolder).
9. In the CPU, select the network view to be loaded and then select the "Download to device" command in the "Online" menu to download the blocks. Compilation of the blocks is implicitly initiated before downloading.

   If errors are reported during this process, you must correct these errors before you can download the configuration.

##### Tips for generating the web data blocks

When you click on the "Generate blocks" button in the area "Web server > User-defined pages", STEP 7 checks whether the corresponding web data blocks can be generated.

The following causes prevent the generation of web data blocks:

- Length of file names and tag names is too long

  If you have a comprehensive web application with many files and directories, the generation of the web data blocks may possibly fail. If this happens, the generation is aborted with the message "Text list overflow...". The cause is system-internal size limitations for management information saved in the web data block.

  Solution: Use short file names and short tag names.
- Files with dynamic content (file with AWP commands) are too large

  When the files with dynamic content (e.g. *.htm, *.html) are too large (for S7-1500 CPUs, e.g., larger than ca. 64 kB), you will see the following message "WebInt: Unable to read files for web application ..." with information on the file size and the path to the file that causes the error.

  Solution: Use the following AWP command to fragment the file:

  `<!-- AWP_Start_Fragment Name='<Fragmentname>' -->`

  The command divides the file internally into multiple segments that can be processed individually by the CPU.

#### Structure of the PLC program (S7-1200)

Your user program must call the " WWW" instruction to even allow the web application, for example, the user-defined web pages, to be available to the CPU on the standard web pages and to allow them to be called up there.

The Web Control DB you have created from the source files is the input parameter (CTRL_DB) for the "WWW" instruction. The Web Control DB references the content of the user-defined web pages coded in the fragment DB and then receives status and control information.

##### Calling the "WWW" instruction in the startup program

If you do not want the user program to influence requested web pages, it is sufficient to only call the "WWW" instruction once in a startup OB. This instruction initializes communication between the web server and the CPU.

##### Calling the "WWW" instruction in the cyclic program

The "WWW" instruction can also be called in an OB processed in cycles (for example, OB 1). This has the advantage of being able to respond to web server requests from within the user program. Manual fragments must be used for this.

In this case, you must evaluate information from the Web Control DB in order to identify the requested web page or the requested fragment. On the other hand, you must set a bit in the user program in order to explicitly release the web page to be returned by the web server after processing the web page request.

The structure of the Web Control DB is described in the following section.

#### Web Control DB (S7-1200)

The Web Control DB (DB 333 by default) is created by STEP 7 and contains information on the structure of user pages, the status of communication and any errors that occur.

Additional fragment DBs are also created as well as the Web Control DB. These fragment DBs (there may also only be one fragment DB) are referenced in the Web Control DB. The fragment DBs contain the web pages and media data coded in fragments, for example, images. The content of the fragment DB cannot be changed by the user program. It is created automatically and is only for data management.

The status and control tags of the Web Control DB are accessed via symbols.

The following lists the tags of the Web Control DB required for status evaluation and to control interaction.

The Web Control DB provides two types of information:

- Global status information: Not bound to a concrete web page request.
- Request status and control information: Information about queued requests.

##### Global status information

| Symbol | Meaning |
| --- | --- |
| "WEB-Control_DB".commandstate.init | Activates and initializes the web application. |
| "WEB-Control_DB".commandstate.deactivate | Deactivates the web application. |
| "WEB-Control_DB".commandstate.inititializing | The web application is initialized (read Web Control DB, etc.). |
| "WEB-Control_DB".commandstate.error | Web application could not be initialized. The reason is coded in "WEB-Control_DB".commandstate.last_error . |
| "WEB-Control_DB".commandstate.deactivating | The web application is closed. |
| "WEB-Control_DB".commandstate.initialized | The web application has been initialized and is ready. |
| "WEB-Control_DB".commandstate.last_error | Refer to the next table for a value table of possible errors. |

| Last_error | Description |
| --- | --- |
| 1 | Fragment DB is inconsistent (does not match the Web Control DB). |
| 2 | A web application already exists with this name. |
| 3 | Memory problem initializing in the web server. |
| 4 | Inconsistent data in the Web Control DB. |
| 5 | A fragment DB is not available (not loaded). |
| 6 | No AWP ID for a fragment DB. |
| 7 | The enum fragment is not available (contains the texts and information on the enum types). |
| 8 | An action requested via the command flag in the Web Control DB is prohibited in the current state. |
| 9 | Web application is not initialized (if there is no reinitializing after disabling). |
| 10 | Web server is disabled. |
| ... | Last_error is reset once the web application has been successfully initialized. |

##### Request status information

Request status information is bound to one of four possible requests, x = [1 … 4].

| Symbol | Meaning |
| --- | --- |
| "WEB-Control_DB".requesttab[x].idle | Nothing need be done. |
| "WEB-Control_DB".requesttab[x].waiting | The user program must react to a request from a manual fragment and explicitly initiate further processing in the web browser. |
| "WEB-Control_DB".requesttab[x].sending | The web server is occupied with processing the request/fragment. |
| "WEB-Control_DB".requesttab[x].aborting | The TCP connection is closed by the web server. |

##### Request control information

Request control information is bound to one of four possible requests, x = [1 … 4].

| Symbol | Meaning |
| --- | --- |
| "WEB-Control_DB".requesttab[x].continue | Releases the fragment being processed for transmission. Processing of the next fragment is initiated. |
| "WEB-Control_DB".requesttab[x].repeat | Releases the fragment being processed for transmission. The fragment is then processed again. |
| "WEB-Control_DB".requesttab[x].abort | Closes the TCP connection. |
| "WEB-Control_DB".requesttab[x].finish | Releases the fragment being processed for transmission. Stops further processing of requests (terminates the request). |

##### Example:

The tag for the DB is: "WEB-Control_DB". Whether errors have occurred during initialization of the web application can be determined by requesting bit "WEB-Control_DB".commandstate.error in the user program.

If an error has occurred you can analyze it using the "WEB-Control_DB".commandstate.last_error value.

#### Interaction with the user program (S7-1200)

With the help of manual fragments, you can make sure that the user program reacts synchronously to browser entries so that the returned website can be prepared by the user program.

##### Fragment type

To react to the received data in the user program the "manual" fragment type must be used for the fragment writing the data (for "manual pages"):

<!-- AWP_Start_Fragment Name="testfrag" ID="1" Type="manual" -->

The values are always transferred to the Web server of the CPU for automatic and manual pages in the same way:

Example:

<form method="POST" action="">

<p>

<input type="submit" value="Set new value">

<input type="text" name='"Velocity"' size="20">

</p>

</form>

##### User program for manual fragments

When using manual pages, the "WWW" instruction must be called in cycles in the user program of the CPU.

To react to values entered in the browser, the request - which is made by the manual page to the Web server - must first be evaluated in the user program. The web-control-DB (for example, DB 333) must investigate pending requests to do this. The array that manages four requests is contained in the "requesttab" section of the Web Control DB. Each element of the array contains information about the respective request in a structure.

A simple programming example shows how queued requests are checked based on the tags of the Web Control DB.

![User program for manual fragments](images/22130956555_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22130966539_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22131793931_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22132006923_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22132015115_DV_resource.Stream@PNG-de-DE.png)

In cases where a request has been made, this program section writes the fragment ID in the #frag_index tag and the request no. (value range 1-4) in the #req_index tag.

Using the information from this, the information transferred in the request can now be processed separately for each fragment ID in the program (for example, plausibility check).

Once processing of the request has been completed by the program, the request must be answered and the appropriate entry is once more reset under"requesttab" of the Web Control DB (for example, DB 333).

A simple programming example for replying to requests:

![User program for manual fragments](images/22132061707_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22132108299_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22132116491_DV_resource.Stream@PNG-de-DE.png)

![User program for manual fragments](images/22132188683_DV_resource.Stream@PNG-de-DE.png)

##### Principle sequence of a browser request with interaction from the user program

The following figure shows the simplified, principle sequence of the web browser request on the effects of Web Control DB content and the actions required from the user program until the processed web page is returned (response).

![Principle sequence of a browser request with interaction from the user program](images/21252715659_DV_resource.Stream@PNG-en-US.png)

#### Displaying custom web pages in the browser (S7-1200)

##### Display web pages in browser

Web pages are called from the standard web pages of the web browser.

In addition to the other links in the navigation bar, the standard web pages also have a link to "user pages".

Click on the "user pages" link to open the web browser you have configured as the default HTML page.

#### Creating custom web pages in several languages (S7-1200)

You can make each of your custom web pages available in various languages.

##### Requirements

The language-dependent HTML; pages must be stored in a folder structure containing folders with the respective language abbreviations:

![Requirements](images/24165365771_DV_resource.Stream@PNG-de-DE.png)

##### Specified language abbreviations

Language abbreviations "de", "en", "fr", "es", "it" and "zh" are fixed. Additional language folders or other designated language folders are not supported.

Additional folders within the same folder hierarchy for other files can be created as required; for example, an "img" folder for images and a "script" folder for JavaScript files.

#### Selecting an entry page (S7-1200)

##### Defining the user page as the start page

In addition to the default intro page, you can also define the start page of your user pages as the start page of the Web server.

Follow these steps to define the user pages in STEP 7 as the start page of the Web server:

1. Select the CPU in the device configuration.
2. Open the settings in the Inspector window of the CPU under "Properties > General > Web server".
3. Select the entry "AWP1" in the area "Entry page" under "Select entry page".

If you now enter the IP address of the CPU in the browser, a connection to your user pages is automatically established.

If you want to access the Web pages of your CPU again, link the Web pages from your user pages, e.g. via the URL "http://a.b.c.d./Portal/Portal.mwsl?PriNav=Start" or "https://a.b.c.d/Portal/Portal.mwsl?PriNav=Start". In this case, the information "a.b.c.d" represents, as an example, the IP address of the configured CPU.

Example of the link in HTML:

<a href="/Portal/Portal.mwsl?PriNav=Start">SIMATIC Web pages</a>

> **Note**
>
> If you define your user page as start page of the Web server, all direct access to the Web pages of the CPU is blocked. This applies also to the bookmarks you saved for the Web pages of the CPU as well as the page for reading out the service data.

**Reading out service data**

If you define your user page as the start page of the Web server, all direct access to the Web pages for reading out the service data is also blocked.   
If you want to continue to read out service data via the Web server in a service situation, here is how you can link the service data page directly to your user page.  
Just as for the web pages of the CPU, link the service data page e.g. via the URL "http://a.b.c.d/save_service_data" or "https://a.b.c.d/save_service_data"; the "a.b.c.d" here is an example of the IP address of the configured CPU.

Example of the link in HTML:

<a href="/save_service_data">Service data</a>

#### Language switching for custom web pages (S7-1200)

##### Requirements

The HTML pages are contained in the predefined language folders, for example, HTML pages with German text are in the "de" folder, HTML pages with English text are in the "en" folder.

##### Language switching concept

Language switching is based on a predefined cookie named "siemens_automation_language". If the cookie is set to value "de", at the next web page request or web page update, the web server switches to the web page from the "de" folder.

Similarly, the web server switches to the web page from the "en" folder when the cookie is set to "en".

#### Example of language switching (S7-1200)

The example is structured as follows:

- The language-dependent HTML files with the same name, for example, "langswitch.html" are located in both language folders "de" and "en". The text to be displayed within the two files are German or English, corresponding to the name of the folder.
- There is an additional "script" folder in the folder structure containing the JavaScript file "lang.js". Functions required for language switching are stored in this file .

##### Structure of the "langswitch.html" file ("de" folder)

Meta data "content language", charset and path to JavaScript file are set in the file header.

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>

<head>

<meta http-equiv="Content-Language" content="de">

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<title>Switch language to German page</title>

<script type="text/javascript" src="script/lang.js" ></script>

<head>

Language selection is implemented in the body of the file by the "select" HTML element. The select element initiates a list box and contains the "de" option, labeled as "German" and "en", labeled as "English"; "de" is the default.

The "DoLocalLanguageChange(this)" function is called using the "onchange" event handler. The "this" parameter transmits the select object with the selected option to this function. "onchange" calls the function each time the option is changed.

<!-- Language Selection -->

<table>

<tr>

<td align="right" valign="top" nowrap>

<!-- change language immediately on change of the selection -->

<select name="Language" onchange="DoLocalLanguageChange(this)" size="1">

<option value="de" selected >Deutsch</option>

<option value="en" >English</option>

</select>

</td>

</tr>

</table>

<!-- Language Selection End-->

##### Structure of the "langswitch.html" file ("en" folder)

The header of the HTML file with English text is structured similarly to the HTML file with German text.

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>

<head>

<meta http-equiv="Content-Language" content="en">

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<title>Language switching english page</title>

<script type="text/javascript" src="script/lang.js" ></script>

Language selection is also implemented in the body of the file by the "select" HTML element. In contrast to the German HTML file, the English option is already selected as a default and the test or the labels are in English.

<!-- Language Selection -->

<table>

<tr>

<td align="right" valign="top" nowrap>

<!-- change language immediately on change of the selection -->

<select name="Language" onchange="DoLocalLanguageChange(this)" size="1">

<option value="de" >German</option>

<option value="en" selected >English</option>

</select>

</td>

</tr>

</table>

<!-- Language Selection End-->

##### Structure of "lang.js" file (in the "script" folder)

The " DoLocalLanguageChange" function is defined in the Java script file and calls the "SetLangCookie" function with the language selection value. SetLangCookie combines the cookie name and cookie value and then sets the cookie by means of the corresponding document.cookie property. The web page must then be reloaded (top.window.location.reload) to allow the web server to react to the setting of the cookie by displaying the required language.

function DoLocalLanguageChange(oSelect) {

SetLangCookie(oSelect.value);

top.window.location.reload();

}

function SetLangCookie(value) {

var strval = "siemens_automation_language=";

// this is the cookie by which the web server

// detects the desired language

// this name is required by the web server

strval = strval + value;

strval = strval + "; path=/ ;";

// set path to the application, since otherwise

// path would be set to the requesting page

// would not get the cookie.

// The path for user defined applications follows this sample:

// path=/awp/<application name>/<pagename>

// example: path=/awp/myapp/myappstartpage.htm

//(where myapp is the name of the web application

// entered in the web server properties of the cpu)

/*

use expiration if this cookie should live longer

than the current browser session

var now = new Date();

var endttime = new Date(now.getTime() + expiration);

strval = strval + "; expires=" + endttime.toGMTString() + ";";

*/

document.cookie = strval;

}

#### Additional examples (S7-1200)

**Filling bottles with different drinks**

This example describes a [bottling plant](http://support.automation.siemens.com/WW/view/en/94681612) that can be monitored and controlled via a user-defined Web page.

It is possible to decide the type of drinks to be bottled using a recipe.

For the control and visualization of the plant, no panel (HMI) is necessary.

A Web browser serves to display the Web page.

The Web page is regularly supplied with current process values.

This is done with an invisible inline frame (iframe) that is re-sent regularly by the Web server. Current process values reach the browser with the inline frame. Using JavaScript, the process values are read from the inline frame and inserted in the main page.

In addition to this, users can call functions on the CPU via the Web page, for example starting or stopping bottling or importing or exporting recipes (refer to the link [Bottling plant application](http://support.automation.siemens.com/WW/view/en/94681612)).

**Filling and emptying a tank**

This example describes a [tank for liquids](http://support.automation.siemens.com/WW/view/en/58862931) that can be monitored and controlled via a user-defined Web page. Using buttons, the user controls the inflow into the tank and the outflow from the tank.

The current fill level is displayed along with the last ten fill levels with time information

The pages "Overview" and "Data" read in the current process values at fixed intervals whereby the Web server sends the pages completely new to the browser.

The "DataOpti" page, on the other hand, uses an inline frame simply to receive the current fill levels of the tank from the Web server (see [Tank simulation application](http://support.automation.siemens.com/WW/view/en/58862931)).

## Configuring central racks (S7-300, S7-400, S7-1500)

In the chapters below you will learn how to configure central racks. For this you will also find information on addressing modules.

### Overview for configuring modules

| Step | Description |
| --- | --- |
| 1 | [Select a central module](#selecting-modules-s7-300-s7-400-s7-1500). |
| 2 | [Specify the properties of the modules](#changing-the-properties-of-cpus-s7-300-s7-400-s7-1500). |
| 3 | [Specify the input and output addresses](#specifying-input-and-output-addresses-s7-300-s7-400-s7-1500). |

---

**See also**

[Addressing modules (S7-1500)](#addressing-modules-s7-1500)
  
[Addressing modules (S7-300, S7-400)](#addressing-modules-s7-300-s7-400)
  
[Rules for modules (S7-300)](#rules-for-modules-s7-300)
  
[Rules for modules (S7-400)](#rules-for-modules-s7-400)
  
[Rules for modules (S7-1500)](#rules-for-modules-s7-1500)
  
[Introduction to configuring hardware](Configuring%20devices%20and%20networks.md#introduction-to-configuring-hardware)

## Rules for modules (S7-300)

### Introduction

Specific slot rules apply for S7-300 modules.

When you select a module in the device view of the hardware catalog, all possible slots for the selected module are marked in the rack. You can only drag modules to marked slots.

If you insert, move or swap a module, the slot rules are also applied.

### Slot rules for S7-300

In addition to the general slot rules, the following rules also apply for S7-300:

- You can use up to 4 racks.

  Rack 0:

  - Slot 1: Only power supply (e.g. 6ES7 307-...) or empty
  - Slot 2: Only central rack (e.g. 6ES7 314-...)
  - Slot 3: Interface module (e.g. 6ES7 360-.../365-...) or empty
  - Slot 4 to 11: Signal modules or function modules, communication processors, or empty

  Racks 1 to 3:

  - Slot 1: Only power supply module (e.g. 6ES7 307-...) or empty
  - Slot 2: Empty
  - Slot 3: Interface module (e.g. 6ES7 361-.../365-...)
  - Slot 4 to 11: Signal module or function module, communication processors, (depending on the interface module used) or empty
- In rack 3 when using a CPU with integrated I/O you cannot use slot 11.
- You must mount modules side-by-side without gaps.

  > **Note**
  >
  > Slot 3 in S7-300 is reserved for the interface module. If you use a single rack, this slot will not be assigned because you do not have to plug an interface module. You do not have a gap in the real structure because otherwise the backplane bus would be interrupted!
  >
  > An ET200m with active backplane bus can have gaps in the allocation.

### Special rules for DM 370 dummy module

You can insert the DM 370 dummy module (6ES7 370-0AA01-0AA0) in place of a module that will be used later.

The DM 370 dummy module reserves address space of 1 byte for a module in the modular DP slave (e.g. for a digital I/O module).

---

**See also**

[Rack: General slot rules](Configuring%20devices%20and%20networks.md#rack-general-slot-rules)

## Rules for modules (S7-400)

### Introduction

Specific slot rules apply for S7-400 modules. The rules for the assignment of components in an S7-400 rack depend on the type of rack used.

When you select a module in the device view of the hardware catalog, all possible slots for the selected module are marked in the rack. You can only drag modules to marked slots.

If you insert, move or swap a module, the slot rules are also applied.

### Slot rules of the S7-400 for central racks

In addition to the general slot rules, the following rules for components on a central rack apply for S7-400:

- Only insert power supply modules in slot 1 (exception: redundant power supply modules)
- insert a max. of 6 interface modules (transmission IMs); max of 2 with power transmission
- connect a max. of 21 expansion racks to the central racks through interface modules
- connect a max. of 1 expansion rack **with power transmission** to an interface of the transmission IM (IM 460-1 with IM 461-1)
- max. of 4 expansion racks **without power transmission** (IM 460-0 with IM 461-0 or IM 460-3 with 461-3)

### Slot rules of the S7-400 for expansion racks

In addition to the general slot rules, the following rules apply for components on extension racks for S7-400:

- Only insert power supply modules in slot 1 (exception: redundant power supply modules)
- insert the interface module (recipient IM) only on the outer right slot (slot 9 and slot 18)
- Insert K-bus modules only in expansion racks with a number no larger than 6 (otherwise it cannot be accessed)

### Special rules for redundant power supply modules

Redundant power supply modules can be inserted into a rack twice. You can find out if the power transmission module is redundant by looking in the "Information" palette on the "Hardware Catalog" task card.

The following rules must be observed:

- You can only insert redundant power supply modules into the designated racks (recognizable from the informational text in the "Hardware Catalog" task card).
- The redundant power transmission modules must be inserted into slot 1 and the connecting slot (no gaps allowed!).
- Redundant and non-redundant power transmission modules may not be inserted in the same rack (this means that no "mixed operation" is possible).

---

**See also**

[Rack: General slot rules](Configuring%20devices%20and%20networks.md#rack-general-slot-rules)

## Rules for modules (S7-1500)

This section contains information on the following topics:

- [Use of S7-1500 modules (S7-1500)](#use-of-s7-1500-modules-s7-1500)
- [Slot rules for S7-1500 modules (S7-1500)](#slot-rules-for-s7-1500-modules-s7-1500)
- [Configuration of an S7-1500 station (S7-1500)](#configuration-of-an-s7-1500-station-s7-1500)
- [Power budget calculation (S7-1500)](#power-budget-calculation-s7-1500)
- [Checking the power budget (S7-1500)](#checking-the-power-budget-s7-1500)
- [Using extended retentive data area with PS 60W 24/48/60VDC HF (S7-1500)](#using-extended-retentive-data-area-with-ps-60w-244860vdc-hf-s7-1500)

### Use of S7-1500 modules (S7-1500)

#### Introduction

The CPUs of the S7‑1500 automation system are modular controllers for medium- and high-performance automation system solutions for discrete and continuous processes.

#### Application area

The S7‑1500 automation system is designed for system solutions in process and manufacturing automation. As a universal automation system, the S7‑1500 automation system represents the optimal solution for centralized and decentralized design applications.

The scalable structure allows you to align your control system's design exactly to the specific needs of your location.

The S7‑1500 automation system complies with IP 20 degree of protection and is intended for installation in a control cabinet.

#### Structure

The S7‑1500 automation system is installed on a mounting rail and can comprise up to 32 modules. Bus connectors are used to interconnect the modules. Power is supplied via the backplane bus; the CPU itself can also supply power to several modules. If the power consumed by the modules exceeds the amount supplied by the CPU, you can insert up to three additional power supply modules.

#### Compact design

The S7-1500 automation system is also available in a compact design. The CPU is then already equipped with integrated inputs and outputs.

The compact CPUs can be expanded with all modules of the S7-1500 automation system. The entire expansion is a total of 32 modules with the CPU and the modules integrated in the CPU (refer to the manuals [CPU 1511C-1 PN](http://support.automation.siemens.com/WW/view/en/109478675) and [CPU 1512C-1 PN](http://support.automation.siemens.com/WW/view/en/109478676)).

---

**See also**

[Slot rules for S7-1500 modules (S7-1500)](#slot-rules-for-s7-1500-modules-s7-1500)
  
[Configuration of an S7-1500 station (S7-1500)](#configuration-of-an-s7-1500-station-s7-1500)
  
[Power budget calculation (S7-1500)](#power-budget-calculation-s7-1500)
  
[Checking the power budget (S7-1500)](#checking-the-power-budget-s7-1500)

### Slot rules for S7-1500 modules (S7-1500)

Specific slot rules apply to S7-1500 modules. When you select a module in the device view of the hardware catalog, all possible slots for the selected module are marked in the rack. You can only drag modules to marked slots. The slot rules apply whenever you insert, move or replace a module.

#### Slot rules for S7-1500

The following slot rules apply to S7-1500:

- In addition to the CPU, you can also insert up to 31 modules on one rack.
- You can insert a maximum of three power supply modules. Together with the CPU, these modules supply power to all downstream devices on the rack. The power consumption of the individual modules determines how many power supply modules are required, at a minimum.

  - One load current supply module PM or one system power supply module PS can be inserted to the left of the CPU (slot 0).
  - Up to two additional standard system power supply modules (PS) can be inserted to the right of the CPU (slots 2 to 31).

> **Note**
>
> **Power segments**
>
> A power supply module and modules supplied by it form a power segment. A power supply module always supplies power to the modules installed on its right. The power segment ends at the next power supply module and a new power segment begins for the next power supply module and the modules installed on its right. The modules located on the left of the power supply module are either supplied from the upstream power supply module or the CPU.

---

**See also**

[Power budget calculation (S7-1500)](#power-budget-calculation-s7-1500)
  
[Configuration of an S7-1500 station (S7-1500)](#configuration-of-an-s7-1500-station-s7-1500)
  
[Using extended retentive data area with PS 60W 24/48/60VDC HF (S7-1500)](#using-extended-retentive-data-area-with-ps-60w-244860vdc-hf-s7-1500)

### Configuration of an S7-1500 station (S7-1500)

The individual S7-1500 CPUs can be expanded with a variety of I/O modules. Besides analog and digital input and output modules, you can use technology modules, communication modules and special modules. In spite of their high performance, S7-1500 CPUs are subject to limits on the number of I/O modules and configured IO systems in situations where the hardware configuration is very large. These limits vary according to the CPU used. When you configure your hardware you should therefore observe the limits described in the technical specifications sheet for the respective CPU.

#### Maximum configuration of a station

When the hardware configuration is compiled, a check is made to determine whether the station configuration exceeds maximum limits. However, you are advised to make sure that any quantity limitations are met when you are configuring the S7-1500 station. In particular, when creating your hardware configuration you should check the technical specifications for your devices for the following criteria:

- Maximum number of communication modules for PROFINET, PROFIBUS and Industrial ETHERNET as well as communication processors

  In the case of an S7-1513 (6ES7 513-1AL00-0AB0), for example, the maximum number allowed is six.
- Maximum number of distributed PROFINET IO systems and distributed PROFIBUS DP systems.

  IO systems that are connected via an I-device do not have to be counted toward the maximum number. In this case, the rules for the maximum configuration of the I-device apply.
- Maximum number of distributed I/O devices (IO devices and DP slaves)

  The number includes all distributed I/O devices that are assigned to the CPU, regardless of the interface to which they are connected (integrated interface or CP/CM interface). The CPU is only included in the IO devices if it is configured as an I-device.

  If I-devices are connected to the PROFINET IO system, the IO devices on an I-device's lower-level PROFINET IO system are not counted.
- Maximum number of modules/submodules

  The maximum number of pluggable modules is very large and is only rarely reached in conventional hardware configurations of an S7-1500 automation system.  
  If modules with submodules are used in very large installations, the CPU's available resources for modules/submodules can be exceeded.  
  Simple I/O modules, which have no submodules, require a single resource.  
  Complex modules can have multiple submodules and require one resource for each submodule. A module with submodules also requires an additional resource (which represents the whole module).   
  **Example**:  
  An IM 155-5PNHF interface module requires five resources based on the following method of counting:   
  Two resources for the PROFINET interface's two ports, one resource for the interface of the PROFINET interface, one resource for the submodule for the interface module's parameters. As explained above, an additional resource is added because the module has submodules.

#### Example

The following figures show an example of a hardware configuration and illustrate the counting method described above:

![In this figure, PLC_1 is configured as the IO controller. IO-Device_1 and PLC_2 are devices on the IO system of PLC_1. Although IO-Device_2 is connected to the same network, it is not a part of the IO system. The IO system of PLC_1 therefore has two devices.](images/39197388555_DV_resource.Stream@PNG-de-DE.png)

In this figure, PLC_1 is configured as the IO controller. IO-Device_1 and PLC_2 are devices on the IO system of PLC_1. Although IO-Device_2 is connected to the same network, it is not a part of the IO system. The IO system of PLC_1 therefore has two devices.

![The second figure shows that while PLC_2 is an I-device in the IO system of PLC_1, it is simultaneously also an IO controller. A lower-level IO system is spanned via the communication module and this IO system is connected to IO device_2. In total, two devices are counted for PLC_2.](images/39205935499_DV_resource.Stream@PNG-de-DE.png)

The second figure shows that while PLC_2 is an I-device in the IO system of PLC_1, it is simultaneously also an IO controller. A lower-level IO system is spanned via the communication module and this IO system is connected to IO device_2. In total, two devices are counted for PLC_2.

![In the third figure, an additional IO system is assigned to PLC_2. PLC_2 now has two IO systems, one connected to the internal interface and one connected to the communication module. Another device must be counted for the new IO system. In total, three devices are counted for this hardware configuration for PLC_2 - one I-device (PLC_2 is assigned to PLC_1) and two I/O devices (assigned to PLC_2).](images/39205944459_DV_resource.Stream@PNG-de-DE.png)

In the third figure, an additional IO system is assigned to PLC_2. PLC_2 now has two IO systems, one connected to the internal interface and one connected to the communication module. Another device must be counted for the new IO system. In total, three devices are counted for this hardware configuration for PLC_2 - one I-device (PLC_2 is assigned to PLC_1) and two I/O devices (assigned to PLC_2).

---

**See also**

[Slot rules for S7-1500 modules (S7-1500)](#slot-rules-for-s7-1500-modules-s7-1500)
  
[Power budget calculation (S7-1500)](#power-budget-calculation-s7-1500)

### Power budget calculation (S7-1500)

#### Introduction

All I/O modules draw the power needed to control the electronics from the backplane bus. This power is fed from the CPU and, if required, also by additional system power supplies to the backplane bus.

#### Power supply/consumption ratio check while configuring

STEP 7 helps you to check the power supply/consumption ratio. All the inserted I/O modules and their maximum power consumption are listed in a table. The power consumption is offset by the plugged system power supply modules. Thus, you see at a glance whether sufficient power is available for all modules.

You can find the table in the "System power supply" section of the Inspector window after you have selected the CPU and then selected the "Properties" tab.

In addition, a check is made during the configuration to determine if sufficient power is available. If the I/O modules consume more power from the backplane bus than is supplied, the corresponding table cells are colored red and you receive a corresponding warning after the hardware configuration is compiled.

#### Power supply/consumption ratio check by the CPU

During operation, the CPU monitors compliance with the power supply/consumption ratio:

- At every Power ON
- At every change of the installed hardware

If the CPU identifies a backplane bus overload, it switches off all I/O modules that are supplied by the CPU or the system power supply and enters an alarm in the diagnostic buffer. The CPU does not start up while the supply/consumption ratio is negative.

#### Causes of overload

An overload may be caused by a mismatch between the installed and configured hardware. For example, the system power supply units required for operation are not inserted or are not switched on or there are more modules inserted than configured.

---

**See also**

[Checking the power budget (S7-1500)](#checking-the-power-budget-s7-1500)
  
[Slot rules for S7-1500 modules (S7-1500)](#slot-rules-for-s7-1500-modules-s7-1500)
  
[Configuration of an S7-1500 station (S7-1500)](#configuration-of-an-s7-1500-station-s7-1500)

### Checking the power budget (S7-1500)

You can see whether sufficient power is available for all I/O modules as you are configuring a station. To do so, you must first specify whether or not the CPU is supplied with voltage.

#### Procedure

To activate the power supply of the CPU and evaluate the power supply/consumption ratio, follow these steps:

1. Select the S7-1500 CPU, for example, in the network view.
2. Open the "Properties" tab in the inspector window.

   The properties of the CPU are displayed.
3. Select the "System power supply" item in the area navigation.
4. Select the "Connection to supply voltage L+" option if the CPU is supplied with voltage. The option is activated by default. As a result, the power consumption of the CPU is included in the power supply/consumption ratio.
5. Check the "Power segment overview" table to find out if the power budget is positive. If the power supply/consumption ratio is negative, the underpowered modules is marked in red.

---

**See also**

[Power budget calculation (S7-1500)](#power-budget-calculation-s7-1500)

### Using extended retentive data area with PS 60W 24/48/60VDC HF (S7-1500)

If you are using the system power supply PS 60W 24/48/60VDC HF, you can use the extended retentive data area for an S7-1500 CPU.

You use the system power supply PS 60W 24/48/60VDC HF for processes that require a large amount of retentive data for a seamless transition after a power failure.

The values for the extended retentivity depend on the CPU you use. The values can be found in the technical specifications of the CPU manuals or in the corresponding Product Information.

Link to the Product Information:

<https://support.industry.siemens.com/cs/ww/en/view/68052815>

#### Requirement

Requirements for use of the system power supply PS 60W 24/48/60VDC HF to use the extended retentive data area:

- CPU S7-1500 firmware version V2.1 and higher
- Compatible hardware function level of the CPU S7-1500

  With the following CPUs you can only use the extended retentive data area **as of hardware function level FS03**:

  - CPU 1517-3 PN/DP, CPU 1517F-3 PN/DP
  - CPU 1518-4 PN/DP, CPU 1518F-4 PN/DP

  With the following CPU you can only use the extended retentive data area **as of hardware function level FS02**:

  - CPU 1518F-4 PN/DP ODK

  The listed CPUs do not permit download of the user program (software) when you use the extended retentive data area.

  Remedy: Use a CPU with the matching HW function level.
- STEP 7 as of V14 Service Pack 1

#### Rules for configuration of an S7-1500 with PS 60W 24/48/60VDC HF

- The system power supply PS 60W 24/48/60VDC HF must be inserted to the left of the CPU (slot 0).

  For the distributed configuration of an ET 200MP the system power supply may only be inserted to the left of the interface module. The power supply does not extend the retentive data area of the CPU in case of distributed use.

  STEP 7 shows the permissible slots for placement of modules with a blue frame so that an incorrect configuration is not possible.

  The figure shows slot 100 for a system power supply module (PM) to the left of slot 0. This slot is only visible when a CPU as of firmware version 2.1 and higher is inserted.

  ![Rules for configuration of an S7-1500 with PS 60W 24/48/60VDC HF](images/96242987915_DV_resource.Stream@PNG-de-DE.png)
- A system power supply PS 60W 24/48/60VDC HF cannot be inserted to the right next to the CPU or to the right of an interface module (ET 200MP). If you need additional system power supplies to increase the capacity for the backplane bus, use a standard system power supply as of slot 2.
- If you are using the PS 60W 24/48/60VDC HF, the 24 V supply of the CPU is not taken into account in the power balance calculation. This means you should not connect the 24 V DC to the CPU. The CPU parameter "System power supply" therefore must be set to the option "No connection to supply voltage L+".

  ![Rules for configuration of an S7-1500 with PS 60W 24/48/60VDC HF](images/94897840523_DV_resource.Stream@PNG-en-US.png)
- The parameter "Comparison preset to actual module" must be set to the value "Startup CPU only if compatible".

  Reason: The retentivity of the entire CPU work memory (data) is only guaranteed when a PS 60W 24/48/60VDC HF is inserted.

  When you insert the PS 60W 24/48/60VDC HF, STEP 7 automatically sets this value for the slot.

  ![Rules for configuration of an S7-1500 with PS 60W 24/48/60VDC HF](images/94897810955_DV_resource.Stream@PNG-en-US.png)

STEP 7 checks the rules listed above during compilation or loading of the user program to the CPU.

#### Replacement parts scenario

You can use the PS 60W 24/48/60VDC HF system power supply as replacement for a configured PS 60W 24/48/60VDC (standard PS) in slot 0. In this case you do not benefit from the extended retentive data area.

However, you can **not** use the standard PS as replacement for a configured PS 60W 24/48/60VDC HF.

#### Missing diagnostics of the PS 60W 24/48/60VDC HF system power supply

In case of POWER OFF, saving the extended retentive data is most important. The CPU as of FW V2.1 and higher does **no longer** output the following diagnostics of the PS 60W 24/48/60VDC HF:

- Supply voltage fault
- Switch position Off

---

**See also**

[Retentive memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#retentive-memory-areas-s7-1500)
  
[Slot rules for S7-1500 modules (S7-1500)](#slot-rules-for-s7-1500-modules-s7-1500)

## Selecting modules (S7-300, S7-400, S7-1500)

### Introduction

Select a CPU from the hardware catalog and place it, together with a rack, in the network view. On this device drag the desired modules from the hardware catalog; they are arranged automatically on the rack.

### Selecting the components in the hardware catalog

Each hardware component is displayed as a folder in the hardware catalog. When you open this folder, you see the different versions of the selected hardware component with its respective article numbers.

There will be an example of how to set up a CPU with a rack in network view.

### Requirement

- The hardware catalog is open.
- You must be in the network view.

### Procedure

To select a CPU from the hardware catalog, proceed as follows:

1. In the hardware catalog navigate to the folder with the desired CPUs.
2. Open the folder with the desired CPU type; you will see all article numbers for the selected CPU type.
3. Click on a CPU article number to get information about the selected CPU in the "Information" pane.

   ![Procedure](images/76391748235_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76391748235_DV_resource.Stream@PNG-en-US.png)
4. Set the matching firmware version of your CPU in the drop-down list box "Version".
5. Set up the CPU and a rack. You have the following options:

   - Use drag-and-drop to drag the CPU from the hardware catalog into network view.
   - Double-click the CPU entry in the hardware catalog.

---

**See also**

[Adding a device to the hardware configuration](Configuring%20devices%20and%20networks.md#adding-a-device-to-the-hardware-configuration)
  
[Rack: Inserting a module](Configuring%20devices%20and%20networks.md#rack-inserting-a-module)
  
[Rack: Basics](Configuring%20devices%20and%20networks.md#rack-basics)
  
[Browsing the hardware catalog](Configuring%20devices%20and%20networks.md#browsing-the-hardware-catalog)

## Selecting fail-safe modules (S7-300, S7-400, S7-1500)

### Introduction

Fail-safe automation systems (F systems) are used to control processes with a safe state that can be achieved immediately on shutdown. F systems control processes that can be shut down immediately without endangering human beings or the environment.

### Selecting the F components in the hardware catalog

Each hardware component is displayed as a folder in the hardware catalog. Fail-safe hardware components are displayed with yellow symbols in the hardware catalog in contrast to the blue hardware components that are not fail-safe.

The following figure shows excerpts from the hardware catalog with two CPUs and two digital output modules, normal in blue and F in yellow:

![Selecting the F components in the hardware catalog](images/25540860299_DV_resource.Stream@PNG-de-DE.png)

Based on this color coding, you can identify F components in the hardware catalog simply and quickly.

### Display of the F components in the hardware and network editor

If you use fail-safe devices and "normal" devices in the graphic views of the hardware and network editor, you can recognize them simply by the yellow color-coding of the devices.

The following figure shows two CPUs. The F CPU is shown in yellow:

![Display of the F components in the hardware and network editor](images/25541546891_DV_resource.Stream@PNG-de-DE.png)

Fail-safe modules in racks or devices can also be recognized in the device view due to their yellow color coding. Since modules that are not capable of networking are not displayed in the network or topology view, devices with F components without networking capability are represented by a special symbol in the network and topology view.

The following figure shows a "normal" CPU and an F-CPU in the network view that both contain F components:

![Display of the F components in the hardware and network editor](images/25541555083_DV_resource.Stream@PNG-de-DE.png)

Based on the color coding of the fail-safe devices and modules, you can also identify the F components quickly in the graphic views of the hardware and network editor.

## Changing the properties of CPUs (S7-300, S7-400, S7-1500)

Each hardware component (module, interface, or interface module) has pre-selected properties, e.g. for analog entry modules pre-selected measurement types and measurement ranges.

### Properties of CPUs

The properties of the CPUs have special significance for system behavior. For example for a CPU you can set:

- Startup characteristics
- Local data storage areas
- Priorities for interrupts
- Memory areas
- Magnetic latching
- Clock memory
- Protection level
- Password

The entry possibilities specify what is adjustable and in which value ranges. Fields that cannot be edited are disabled or are not shown in the properties window.

You can assign parameters for an integrated MPI interface or PROFIBUS DP interface in the properties of an interface, for example, and connect them with an existing subnet.

### Requirement

You have already arranged the hardware components for which you want to change properties, on a rack.

### Procedure

To change the properties and parameters of the hardware components, proceed as follows:

1. In the device or network view, select the hardware components that you want to edit.

   You can also select individual parts of a hardware component, e.g.:

   - Interface
   - Input
   - Output
2. Edit the settings for the selected object:

   - For example in the device view you can edit addresses and names.
   - In the Inspector window additional setting possibilities are available.

You do not need to confirm your entries, the changed values will be applied immediately.

### Additional possibilities for parameter assignment

For the S7-300/400 automation systems, for example, you have the possibility of setting parameters for analog modules in the user program. To do this, open the system functions [WR_PARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_parm-write-module-data-record-s7-300-s7-400) (SFC 55), [DP_DPARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_dparm-read-data-record-from-configured-system-data-s7-400) (SFC 56) and [PARM_MOD](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#parm_mod-transfer-module-data-records-s7-300-s7-400) (SFC 57) in the user program. However these settings will be lost at start-up or restart (warm restart).

### Additional information

For additional information about system functions and standard functions for S7-300/400, refer to the system software reference manual for S7-300/400.

---

**See also**

[Editing properties and parameters](Configuring%20devices%20and%20networks.md#editing-properties-and-parameters)

## Linking racks (S7-300)

### Introduction

Depending on the device used, the option exists to link racks using interface modules for some S7-300 CPUs.

### Linking racks

To link racks through an interface module, another rack must be moved from the hardware catalog into the device view. Then a sender module is plugged into the central rack and a receiver module into the new rack. A link is automatically established between sender and receiver modules.

![Linking racks](images/9778932363_DV_resource.Stream@PNG-de-DE.png)

With S7-300, for example, you can link up to four racks. The interface modules are always plugged in slot 3.

> **Note**
>
> If your configuration does not include an expansion, slot 3 will always be identified as empty even if the module in slot 4 is actually connected directly to the CPU and there is no gap.

Use the following interface modules:

- To expand by one rack precisely:

  Racks 0 and 1: IM 365
- To expand by up to 3 racks:

  Rack 0: IM 360

  Racks 1 to 3: IM 361

If you prefer a manual link, first delete the connection line representing the link. Then press and hold down the mouse button and draw a new connection line between the interfaces of the sender and receiver modules.

### Expandable racks

Depending on the device used, several CPUs (e.g. IM 151-1) have expandable racks whose groups of slots can be expanded and collapsed using the arrow symbols above the expandable slot. When the groups of slots are collapsed, the first and last of the group's slot numbers are displayed.

The following diagram shows a section of an expanded rack:

![Expandable racks](images/9778926219_DV_resource.Stream@PNG-de-DE.png)

Groups of slots into which modules have already been plugged cannot be collapsed. The first group of slots and device cannot be collapsed. You can tell from the grayed out arrow symbol if a group of slots cannot be collapsed.

---

**See also**

[Rack: Basics](Configuring%20devices%20and%20networks.md#rack-basics)

## Linking racks (S7-400)

This section contains information on the following topics:

- [Expanding a central rack by adding an expansion rack (S7-400)](#expanding-a-central-rack-by-adding-an-expansion-rack-s7-400)
- [Rules for linking expansion racks (S7-400)](#rules-for-linking-expansion-racks-s7-400)
- [Arrangement of the expansion rack (S7-400)](#arrangement-of-the-expansion-rack-s7-400)

### Expanding a central rack by adding an expansion rack (S7-400)

#### Configuring expansion racks in SIMATIC 400

In SIMATIC 400, the expansion options are more complex due to be various racks and interface modules.

All expansion racks connected to an interface of the IM send module of the central rack form a chain.

The following figure shows two groups of three expansion racks, with each group connected to an interface of the IM send module.

![Configuring expansion racks in SIMATIC 400](images/25429051147_DV_resource.Stream@PNG-de-DE.png)

### Rules for linking expansion racks (S7-400)

#### Linking expansion racks

If you link expansion racks (SIMATIC 400) to an interface of the interface module (IM send module) of the central rack, the following properties of the IM send module and IM receive module must match:

- Power transfer (with/without)
- Type of link (central/distributed)
- K bus transfer (with/without interrupt transfer)

#### Slot rules of the S7-400 for expansion racks

In addition to the general slot rules, the following rules apply for components on extension racks for S7-400:

- Insert power supply modules in slot 1
- Insert the interface module (receive IM) only in the outer right-hand slot (slot 9 or slot 18)
- Insert K-bus modules only in expansion racks with a number no larger than 6 (otherwise it cannot be accessed)

### Arrangement of the expansion rack (S7-400)

#### Basic procedure

To arrange expansion racks and drag connections between the interface modules in the racks, follow these steps:

1. Select a CPU rack (for example CPU 417) from the "hardware catalog".
2. Drag the controller to the device view.
3. Assign the controller modules (for example, power supply and IM 460) to the rack.
4. Select suitable expansion racks (for example ER1) from the "hardware catalog".
5. Drag the expansion racks one after the other to the device view.
6. Assign modules (for example, power supply or IM 461) to each rack.

   Important: The interface modules must be inserted in all racks to allow you to link racks together.
7. Connect the interface of the IM send module with the iterface of the IM receive module of the required rack.

   Connection lines then show the assignment of the racks among themselves.

The following figure shows groups of two expansion racks, with each group connected via a receive IM to an interface of the send IM.

![Basic procedure](images/26379678091_DV_resource.Stream@PNG-de-DE.png)

## Flexible automation concepts (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Overview of flexible automation concepts (S7-1200, S7-1500, S7-1500T)](#overview-of-flexible-automation-concepts-s7-1200-s7-1500-s7-1500t)
- [Configuration control (option handling) for devices (S7-1500, S7-1500T)](#configuration-control-option-handling-for-devices-s7-1500-s7-1500t)
- [Configuration control (option handling) for IO systems (S7-1500)](#configuration-control-option-handling-for-io-systems-s7-1500)
- [Configuration control (option handling) for devices (S7-1200)](#configuration-control-option-handling-for-devices-s7-1200)

### Overview of flexible automation concepts (S7-1200, S7-1500, S7-1500T)

#### Flexibility in configuration

Flexible automation concepts are based on the idea that different configurations can be operated with a single program. Under certain conditions, a new project does not have to be set up and completely re-tested for each configuration and each stage of expansion. Depending on the application, it is often sufficient to temporarily or permanently disable the components that are momentarily not required by the program.

For example, modules may be needed in one machine but not in another. Otherwise, the automation task is the same.

Or IO devices may be needed in one plant but not in another. The maximum expansion is configured; the program manages the various stages of expansion.

It is also possible for a CPU to work as a lower-level I-device in one constellation, but does not require a higher-level IO controller in another constellation.

---

**See also**

[Configuration control (option handling) for IO systems (S7-1500)](#configuration-control-option-handling-for-io-systems-s7-1500)
  
[Disabling I-device in the user program of the I-device CPU](Special%20PROFINET%20configurations.md#disabling-i-device-in-the-user-program-of-the-i-device-cpu)
  
[Configuration control (option handling) for devices (S7-1500, S7-1500T)](#configuration-control-option-handling-for-devices-s7-1500-s7-1500t)
  
[Configuration control (option handling) for devices (S7-1200)](#configuration-control-option-handling-for-devices-s7-1200)

### Configuration control (option handling) for devices (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Configuration control (option handling) for central S7-1500 (S7-1500, S7-1500T)](#configuration-control-option-handling-for-central-s7-1500-s7-1500-s7-1500t)

#### Configuration control (option handling) for central S7-1500 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Important information regarding configuration control (option handling) (S7-1500)](#important-information-regarding-configuration-control-option-handling-s7-1500)
- [Example of a configuration control](#example-of-a-configuration-control)
- [Control data record for an ET 200SP CPU (S7-1500, S7-1500T)](#control-data-record-for-an-et-200sp-cpu-s7-1500-s7-1500t)

##### Important information regarding configuration control (option handling) (S7-1500)

###### Operating principle

You can use the configuration control to configure the structure of a control system (here: central configuration of an S7-1500) and to work with variants (options) that differ from this configuration.

- All modules that are needed in a set of similar plant units or machines are configured in a master project with a maximum configuration (station master).
- Provision is made in the user program of the master project for various station options for various plant units or machines as well as the selection of a station option. A station option uses, for example, only some of the configured modules and these modules are inserted in varying order.
- An operator selects a station option for a specific plant on-site. The operator does not have to modify the project and thus also does not have to download a modified configuration for this.

![Operating principle](images/69475312651_DV_resource.Stream@PNG-en-US.png)

A control data record you have programmed in the startup program notifies the CPU as to which modules are missing or located in different slots as compared to the preset configuration. The configuration control has no effect on the parameter assignment of the modules.

Configuration control gives you the flexibility to vary the central installation as long as the real configuration can be derived from a preset maximum configuration.

Below you will find a description of how to activate configuration control (CPU parameter assignment) and how to structure the required data record.

###### Requirements

- STEP 7 Professional Version V13 or higher
- CPU S7-15XX Firmware Version 1.5 or higher Modules that support the "Configuration control" function also have the "Configuration control" entry in the description (info text) of the hardware catalog.
- Recommendation: Before you load a new program with a modified control data record, perform a reset to factory settings. This action will prevent inconsistent states that may result from the presence of incompatible control data records.
- The startup parameter "Compare preset to actual configuration" is set to "Startup CPU even if mismatch" (default setting).

###### Required steps

1. Enable the "Allow to reconfigure the device via the user program" parameter when configuring the CPU ("Configuration control" area).

   ![Required steps](images/69749576587_DV_resource.Stream@PNG-en-US.png)
2. Create a control data record (e.g., in a data block) according to the current configuration based on the sample described below for the control data record. The control data record has the number 196. Note that you must first create a PLC data type containing the structure of the control data record and base the data block on this PLC data type.

   ![Required steps](images/69957311499_DV_resource.Stream@PNG-en-US.png)
3. Transfer the control data record to the CPU in the startup program.

   The configuration control for the centrally inserted modules takes effect only after an operating mode change of the CPU from STOP to RUN. For this reason, call the extended WRREC (Write data record) instruction in the startup OB, and transfer the created control data record to the CPU; see next section.

   If a valid control data record is not transferred in the startup OB, the control is not ready for operation. The CPU returns from startup to STOP in this case.

###### Transferring a control data record in the startup program

The CPU processes the WRREC instruction for asynchronous transfer of the control data record. For this reason, you must call WRREC in the startup OB repeatedly in a loop until the output parameter "BUSY" or "DONE" indicate that the data record has been transferred.

Tip: Use the [SCL programming language](Creating%20SCL%20programs.md#programming-language-scl) with the REPEAT ... UNTIL instruction for programming the loop.

`REPEAT`

`"WRREC_DB"(REQ := "start_config_control",`

`ID := 33,`

`INDEX := 196,`

`LEN := "conf_LEN",`

`DONE => "conf_DONE",`

`BUSY => "conf_BUSY",`

`ERROR => "conf_ERROR",`

`RECORD := "ConfDB".ConfigControl,`

`STATUS => "conf_STATUS");`

`UNTIL NOT "conf_BUSY"`

`END_REPEAT;`

Below, you will find explanations for individual block parameters that you must supply with specific values in the configuration control context. For the remaining block parameters, see also [WRREC](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#wrrec-write-data-record-s7-1200-s7-1500-1):

| Parameter | Explanation |
| --- | --- |
| ID | HW identifier; is always 33 (decimal) for configuration control for centrally arranged modules. |
| INDEX | Data record number; is always 196 (decimal) for configuration control for centrally arranged modules. |
| RECORD | Control data record to be transferred.   See the section "Control data record" for the structure of the control data record.  Tip: The "RECORD" block parameter of the WRREC instruction (V1.1 and higher) is of the "VARIANT" data type and therefore requires a tag with data type. If you store the control data record in a data block, this data block must thus have a data type. The data block created must not be of the "Global-DB" type. Rather, it must be derived from a user data type.  Proceed as follows:  1. First, create a new PLC data type (user data type) with the structure of the control data record and name it, for example, "ConfDB". 2. Create a new data block. Select the newly created user data type, for example, "ConfDB", as type for this data block. |

In graphical programming languages, you realize the loop using instructions for program control.

Example in FBD: Use the LABEL (jump label) and JMP (jump at RLO=1) instructions to program a loop.

![Transferring a control data record in the startup program](images/89565973643_DV_resource.Stream@PNG-en-US.png)

###### Arrangement of the modules

The following table shows the slot number assignment:

| Slot | Modules | Note |
| --- | --- | --- |
| 0 | Power supply module (optional) | Slot to the left of the CPU |
| 1 | CPU | Slot 1 is always the CPU |
| 2 - 31 | I/O modules/system power supply modules, depending on the configuration variant | Slots to the right of the CPU |

###### Control data record

A control data record 196 containing a slot assignment is defined for configuration control.

| Byte | Element | Code | Explanation |
| --- | --- | --- | --- |
| 0 | Block length | 4 + number of slots | Header |
| 1 | Block ID | 196 |  |
| 2 | Version | 4 (for central I/O) |  |
| 3 | Subversion | 0 |  |
| 4 | Assignment of configured slot 0 | Real slot 0 | Control element  Describes in each element which real slot in the device is assigned to the configured slot. The structure of a control element is described in the following section. |
| 5 | Assignment of configured slot 1 | Real slot 1   (always 1, because the CPU is always in slot 1) |  |
| 6 | Assignment of configured slot 2 | Real slot or 16#FF |  |
| 7 | Assignment of configured slot 3 | Real slot or 16#FF |  |
| ... | ... | ... |  |
| 4 + (max. slot number) | Assignment of configured maximum slot | Real slot or 16#FF |  |

###### Structure of a control element

A control element contains the information on which module is inserted in which slot.

The byte numbers represent the configured slots in ascending order (see above):

- Byte 4 stands for the configured slot 0
- Byte 5 stands for the configured slot 1
- Byte 6 stands for the configured slot 2
- etc.

The value that you need to enter in the corresponding byte depends on the following rule:

- If the module is present in the real configuration, enter the real slot number of the module.

  - Example 1: The module configured in slot 2 is located in slot 2.

    Enter value 2 (= actual slot) in byte 6 (= configured slot 2).
  - Example 2: The module configured in slot 3 is located in slot 2.

    Enter value 2 (= actual slot) in byte 7 (= configured slot 3).
- If the module does not exist in the real structure, enter 16#FF (255) in the byte for the configured slot.

###### Rules

Observe the following rules:

- If you have enabled configuration control, the CPU is not ready for operation without a control data record. The CPU returns from startup to STOP if a valid control data record is not transferred in the startup OB. The central I/O is not initialized in this case. The cause for the STOP mode is entered in the diagnostics buffer.
- For addressing the WRREC instruction, use the HW identifier 33 (decimal, for the ID block parameter) to write the control data record.
- The control data record is saved retentively in the CPU, which means that it is not necessary to write the control data record 196 again at a restart if the configuration is unchanged. Prior to commissioning, we recommend that a memory reset be performed for the CPU in order to delete any control data record that is present.
- Slot entries in the control data record outside the configured preset configuration are ignored by the CPU.
- You can shorten the control data record. It must contain the entries up to the last slot of the current preset configuration.
- Each real slot may only be present once in the control data record.
- A real slot may only be assigned to one configured slot.
- Using CPs/CMs:

  - As regards the configuration control, point-to-point CPs/CMs behave like digital and analog modules (no restrictions).
  - CPUs with firmware version V1.7 or higher:   
    If the central configuration includes CPs/CMs, for example a CM 1542-5 (DP master or DP slave), these CMs/CPs are not affected by the configuration control. Therefore, these modules must remain in their configured slots and their configured slot numbers entered in the control data record ("real slot = configured slot") Maximum flexibility is achieved by inserting CMs/CPs to the immediate right of the CPU.
  - CPUs with firmware version V1.6 or higher:   
    As a matter of principal, CMs and CPs cannot be used for configuration control.
- System power supply modules (PS) can also be subject to configuration control. Note the information on this topic in the [S7-1500 system manual](http://support.automation.siemens.com/WW/view/en/59191792). In particular for a system power supply module (PS) on slot 0, we recommended that you avoid reconfiguration.

  > **Note**
  >
  > **Modified configuration**
  >
  > The writing of a control data record with a modified configuration leads automatically to a restart with this modified configuration.
  >
  > As a result of this reaction, the retentively saved original data record 196 is deleted and the new data record 196 is saved retentively.

###### Behavior during operation

Effect of the discrepancy between the configured configuration and real configuration:

- For the online display and for the display in the diagnostics buffer (module OK or module faulty), the hardware configuration is always used and not the differing real configuration.

  Example: A module supplies diagnostic information. This module is configured in slot 4, but is really inserted in slot 3 (missing module; see example in the next section). In the online view, a configured slot 4 is indicated as faulty. In the real configuration, the module in slot 3 indicates an error via an LED display.

If modules are entered as missing in the control data record, the automation system behaves as follows:

- Modules designated as not present in the control data record do not supply diagnostics and their status is always OK. The value status is OK
- Direct write access to the outputs or write access to the process image of outputs that are not present: Remains without effect; no access error is signaled.
- Direct read access to the inputs or read access to the process image of inputs that are not present: Value "0" is supplied; no access error is signaled.
- Write data record to module that is not present: Remains without effect; no error is signaled.
- Read data record from module that is not present: An error is signaled because a valid data record cannot be returned.

###### Error messages

The following error messages are returned if an error occurs during writing of the control data record:

Error messages

| Error code | Meaning |
| --- | --- |
| 16#80B1 | Invalid length; the length information in data record 196 is not correct. |
| 16#80B5 | Configuration control parameters not assigned. |
| 16#80E2 | Data record was transferred in the wrong OB context. The data record must be transferred in the startup program. |
| 16#80B8 | Parameter error; module signals invalid parameters. |

###### Additional information and examples

You will find a library of the data records and application examples here: [Templates for the data records](http://support.automation.siemens.com/WW/view/en/29430270)

---

**See also**

[Basic information on VARIANT (S7-1200, S7-1500)](Data%20types.md#basic-information-on-variant-s7-1200-s7-1500)
  
[Important information regarding configuration control (option handling) (S7-1200)](#important-information-regarding-configuration-control-option-handling-s7-1200)
  
[S7-1500 system manual](http://support.automation.siemens.com/WW/view/en/59191792)
  
[Use the program example of the control data record with WRREC & RDREC (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#use-the-program-example-of-the-control-data-record-with-wrrec-rdrec-s7-1200-s7-1500)

##### Example of a configuration control

A configuration consisting of a system power supply, CPU, and 3 I/O modules is configured in the following section.

The module at slot 3 is not present in the first configuration expansion and is "hidden" by the configuration control.

In the second configuration expansion, the module that was initially hidden is located in the last slot. The added slot is made known to the CPU by a modified control data record.

###### Actual configuration with missing module

The specified configuration contains all modules that can be present in a final expansion stage.

The module that is inserted in slot 3 in the specified configuration is missing in the real expanded configuration. For this reason, slot 3 must be coded in the control data record accordingly with "FF <sub>H</sub>" (= not present).

![Actual configuration with missing module](images/69785359243_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Module is missing in the real configuration |

###### Actual configuration with subsequently added module

The module present in slot 3 in the specified configuration is added to the back of the real configuration by inserting it as the last module in slot 4.

The control data record is adapted accordingly.

![Actual configuration with subsequently added module](images/69478314507_DV_resource.Stream@PNG-en-US.png)

##### Control data record for an ET 200SP CPU (S7-1500, S7-1500T)

###### Slot assignment

The following table shows the possible slots for the various modules for an ET 200SP CPU:

Slot assignment

| Modules | Possible slots | Note |
| --- | --- | --- |
| CPU | 1 | Slot 1 is always the CPU |
| I/O modules | 2 - 65 | Downstream of CPU |
| Server module | 2 - 66 | The server module completes the configuration of the ET 200SP station after the CPU/the last I/O module. |
|  |  |  |

###### Control data record

For the configuration control of an ET 200SP CPU, you define a control data record 196 V2.0, which includes a slot assignment. The maximum slot corresponds to the slot of the server module.

The table below shows the structure of a control data record with explanations of the individual elements.

Configuration control: Structure of control data record 196

| Byte | Element | Code | Explanation |
| --- | --- | --- | --- |
| 0 | Block length | 4 + (number of slots × 2) | Header |
| 1 | Block ID | 196 |  |
| 2 | Version | 2 |  |
| 3 | Version | 0 |  |
| 4 | Slot 1 of the station master | Slot assignment 1 in the station option   (always 1, because the CPU is always in slot 1) | **Control element**   Contains the information on which module is inserted in which slot.  The value that you need to enter in the corresponding byte depends on the following rule:  - If the module exists in the station option, enter the slot number of the module. - If the module exists as empty slot (with BU cover), enter the slot number of the module + 128. (Example: module as empty slot on slot 3: Enter 131 in the control element) - If the module does not exist in the station option, enter 0.    **Additional function**   Contains information on whether a new potential group will be opened in the station option - by replacing a dark-colored BaseUnit with a light-colored BaseUnit.  - If you replace a dark-colored BaseUnit with a light-colored BaseUnit, enter 1 as additional function. - If you accept the BaseUnit from the station master, enter 0 as additional function. |
| 5 | Additional function for slot 1 |  |  |
| 6 | Slot 2 of the station master | Slot assignment in the station option |  |
| 7 | Additional function for slot 2 |  |  |
| 8 | Slot 3 of the station master | Slot assignment in the station option |  |
| 9 | Additional function for slot 3 |  |  |
| : | : | : |  |
| 4 + ((max. slot - 1) × 2) | Server module slot | Server module slot assignment in the station option* |  |
| 4 + ((max. slot - 1)× 2) + 1 | Additional function for server module slot |  |  |
| * The server module must be present in the station option and must not be marked as empty slot (BU cover). |  |  |  |

###### Block library "OH_S71x00_Library"

The block library [OH_S71x00_Library](https://support.industry.siemens.com/cs/#document/29430270?lc=en-WW) is available for download from the Internet. The block library contains data types with the structure of the control data records for the ET 200SP distributed I/O system. You can implement your flexible automation solution economically with the help of these data types.

---

**See also**

[ET 200SP system manual](https://support.industry.siemens.com/cs/ww/en/view/58649293)

### Configuration control (option handling) for IO systems (S7-1500)

#### Using standard machine projects

Standard machine projects can be a useful solution, for example, when:

- The automation solution (machine) is used multiple times by a customer.
- The machine is used in different plants by various customers.

#### Variability in the configuration through configuration control of IO devices

You obtain additional flexibility for a system or machine by configuring optional IO devices and by configuring ports that are prepared for interconnection by the user program.

Optional IO devices can be added to the configuration via the user program without having to download the project again. In addition, the interconnection of the ports of IO devices and thus the order of the IO devices can be adapted via the user program, enabling control of the configuration required in each case - without an engineering system!

#### Advantages of standard machine projects

- A centrally maintained project (configuration and program) can be loaded to various machines of the same type without changes.
- Only a few easy adaptations are needed locally to integrate the machine into an existing network infrastructure.
- Modular machines can be easily adapted for various applications by using the configuration control to notify the PROFINET IO system of the current real configuration of the IO system.

#### Additional information

For detailed information on standard machine projects, refer to the [PROFINET with STEP 7](http://support.automation.siemens.com/WW/view/en/49948856) manual [here](Special%20PROFINET%20configurations.md#what-you-should-know-about-multiple-use-io-systems).

### Configuration control (option handling) for devices (S7-1200)

This section contains information on the following topics:

- [Important information regarding configuration control (option handling) (S7-1200)](#important-information-regarding-configuration-control-option-handling-s7-1200)
- [Example of a configuration control (S7-1200)](#example-of-a-configuration-control-s7-1200)

#### Important information regarding configuration control (option handling) (S7-1200)

##### Operating principle

With S7-1200 Firmware Version 4.1 or higher, the configuration control enables you to configure the structure of a control system and to work with variants (options) that differ from this configuration.

- All modules that are needed in a set of similar plant units or machines are configured in a master project with a maximum configuration (station master).
- Provision is made in the user program of the master project for various station options for various plant units or machines as well as the selection of a station option. A station option uses, for example, only some of the configured modules and these modules are inserted in varying order.
- An operator selects a station option for a specific plant on-site. The operator does not have to modify the project and thus also does not have to download a modified configuration for this.

![Operating principle](images/82516823179_DV_resource.Stream@PNG-en-US.png)

A control data record you have programmed in the startup program notifies the CPU as to which modules are missing or located in different slots as compared to the preset configuration. The configuration control has no effect on the parameter assignment of the modules.

Configuration control gives you the flexibility to vary the central installation as long as the real configuration can be derived from a preset maximum configuration.

Below you will find a description of how to activate configuration control (CPU parameter assignment) and how to structure the required data record.

##### Requirements

- STEP 7 Version V13 SP1 or higher
- CPU S7-12XX Firmware Version V4.1 or higher Modules that support the "Configuration control" function also have the "Configuration control" entry in the description (info text) of the hardware catalog.
- Recommendation: Before you load a new program with a modified control data record, perform a memory reset. This action will prevent inconsistent states that may result from the presence of incompatible control data records.
- The startup parameter "Compare preset to actual configuration" is set to "Startup CPU even if mismatch" (default setting).

##### Required steps

1. Enable the "Allow to reconfigure the device via the user program" parameter when configuring the CPU ("Configuration control" area).

   ![Required steps](images/69749427211_DV_resource.Stream@PNG-en-US.png)
2. Create a control data record (e.g., in a data block) according to the current configuration based on the sample described below for the control data record. The control data record has the number 196. If you want to transfer the control data record as a whole block to the WRREC instruction (input parameter RECORD), note that you must first create a PLC data type containing the structure of the control data record and base the data block on this PLC data type.

   ![Required steps](images/69972458379_DV_resource.Stream@PNG-en-US.png)
3. Transfer the control data record to the CPU in the startup program.

   The configuration control for the centrally inserted modules takes effect only after an operating mode change of the CPU from STOP to RUN. For this reason, call the extended WRREC (Write data record) instruction in the startup OB, and transfer the created control data record to the CPU; see next section.

   If a valid control data record is not transferred in the startup OB, the control is not ready for operation. The CPU returns from startup to STOP in this case.

##### Transferring a control data record in the startup program

The CPU processes the WRREC instruction for asynchronous transfer of the control data record. For this reason, you must call WRREC in the startup OB repeatedly in a loop until the output parameter "BUSY" or "DONE" indicate that the data record has been transferred.

Tip: Use the [SCL programming language](Creating%20SCL%20programs.md#programming-language-scl) with the REPEAT ... UNTIL instruction for programming the loop.

`REPEAT`

`"WRREC_DB"(REQ := "start_config_control",`

`ID := 33,`

`INDEX := 196,`

`LEN := "conf_LEN",`

`DONE => "conf_DONE",`

`BUSY => "conf_BUSY",`

`ERROR => "conf_ERROR",`

`RECORD := "ConfDB".ConfigControl,`

`STATUS => "conf_STATUS");`

`UNTIL NOT "conf_BUSY"`

`END_REPEAT;`

Below, you will find explanations for individual block parameters that you must supply with specific values in the configuration control context. For the remaining block parameters, see also [WRREC](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#wrrec-write-data-record-s7-1200-s7-1500-1):

| Parameter | Explanation |
| --- | --- |
| ID | HW identifier; is always 33 (decimal) for configuration control for centrally arranged modules. |
| INDEX | Data record number; is always 196 (decimal) for configuration control for centrally arranged modules. |
| RECORD | Control data record to be transferred.   See the section "Control data record" for the structure of the control data record.  Tip: The "RECORD" block parameter of the WRREC instruction (V1.1 and higher) is of the "VARIANT" data type and therefore requires a tag with data type. If you store the control data record in a data block, this data block must thus have a data type. The data block created must not be of the "Global-DB" type. Rather, it must be derived from a user data type.  Proceed as follows:  1. First, create a new PLC data type (user data type) with the structure of the control data record and name it, for example, "ConfDB". 2. Create a new data block. Select the newly created user data type, for example, "ConfDB", as type for this data block. |

In graphical programming languages, you realize the loop using instructions for program control.

Example in FBD: Use the LABEL (jump label) and JMP (jump at RLO=1) instructions to program a loop.

![Transferring a control data record in the startup program](images/89565877643_DV_resource.Stream@PNG-en-US.png)

##### Arrangement of the modules

The following table shows the slot number assignment:

| Slot | Modules | Note |
| --- | --- | --- |
| 1 | Signal board, communication board, battery board | Slot on front of the CPU |
| 2 - 9 | Signal modules | Slots to the right of the CPU |
| 101 - 103 | Communications modules | Slots to the left of the CPU |

##### Control data record

A control data record 196 containing a slot assignment is defined for configuration control.

The following codes apply:

| Symbol | Meaning |
| --- | --- |
| 0 | Module is included in the hardware configuration but is not used in the current configuration. |
| 1 to 9, 101 to 103 | Current slot of the module |
| 16#FF (255) | A module is not located in this slot in the hardware configuration. |

| Byte | Element | Code | Explanation |
| --- | --- | --- | --- |
| 0 | Block length | 4 + number of slots | Header |
| 1 | Block ID | 196 |  |
| 2 | Version | 5 (for central I/O) |  |
| 3 | Subversion | 0 |  |
| 4 | Assignment of the CPU expansion board | Expansion board, 0 or 16#FF | Control element  Describes in each element which real slot in the device is assigned to the configured slot. The structure of a control element is described in the following section. |
| 5 | Assignment of configured slot 2 | Real slot, 0 or 16#FF |  |
| ... | ... | ... |  |
| 12 | Assignment of configured slot 9 | Real slot, 0 or 16#FF |  |
| 13 | Assignment of configured slot 101 | Real slot or 16#FF | In contrast to signal modules, the real slot of the communications modules must correspond to the configured slot. |
| 14 | Assignment of configured slot 102 | Real slot or 16#FF |  |
| 15 | Assignment of configured slot 103 | Real slot or 16#FF |  |

##### Structure of a control element

A control element contains the information on which module is inserted in which slot.

The byte numbers represent the configured slots in ascending order (see above):

- Byte 4 stands for the configured slot of the expansion board
- Byte 5 to byte 9 stand for the configured slots 2 to 9
- Byte 13 to byte 15 stand for the configured slots 101 to 103

The value that you need to enter in the corresponding byte depends on the following rule:

- If the module is present in the real configuration, enter the real slot number of the module.

  - Example 1: The module configured in slot 2 is located in slot 2.

    Enter value 2 (= actual slot) in byte 5 (= configured slot 2).
  - Example 2: The module configured in slot 3 is located in slot 2.

    Enter value 2 (= actual slot) in byte 6 (= configured slot 3).
- If the module is configured but is missing in the real structure, enter 0 in the byte for the configured slot.
- If a module is not located in this slot in the hardware configuration, enter 16#FF (255) in the byte for the configured slot.

##### Rules

Observe the following rules:

- The configuration control does not support the repositioning of communications modules. The slot entries in the control data record for slots 101 to 103 must correspond to the real positions of the modules or be defined as not present in the hardware configuration by entering 16#FF (255).
- Slot gaps in the configuration are not allowed. For example, if a signal module is inserted in slot 4 in the real configuration, slots 2 and 3 of the real configuration must also be occupied. The same applies to the slots 101 to 103. If a communications module is inserted in slot 102 in the real configuration, slot 101 must also have a communications module inserted in the real configuration.
- If you have enabled configuration control, the CPU is not ready for operation without a control data record. The CPU returns from startup to STOP if a valid control data record is not transferred in the startup OB. The central I/O is not initialized in this case. The cause for the STOP mode is entered in the diagnostics buffer.
- For addressing the WRREC instruction, use the HW identifier 33 (decimal, for the ID block parameter) to write the control data record.
- The control data record is saved retentively in the CPU, which means that it is not necessary to write the control data record 196 again at a restart if the configuration is unchanged. Prior to commissioning, we recommend that a memory reset be performed for the CPU in order to delete any control data record that is present.
- Slot entries in the control data record outside the configured preset configuration are ignored by the CPU.
- Each real slot may only be present once in the control data record.
- A real slot may only be assigned to one configured slot.

> **Note**
>
> **Modified configuration**
>
> The writing of a control data record with a modified configuration triggers the following automatic reaction by the CPU:
>
> Memory reset with subsequent startup with this modified configuration.
>
> As a result of this reaction, the retentively saved original data record 196 is deleted and the new data record 196 is saved retentively.

##### Behavior during operation

Effect of the discrepancy between the configured configuration and real configuration:

- For the online display and for the display in the diagnostics buffer (module OK or module faulty), the hardware configuration is always used and not the differing real configuration.

  Example: A module supplies diagnostic information. This module is configured in slot 4, but is really inserted in slot 3 (missing module; see example in the next section). In the online view, a configured slot 4 is indicated as faulty. In the real configuration, the module in slot 3 indicates an error via an LED display.

If modules are entered as missing in the control data record, the automation system behaves as follows:

- Modules designated as not present in the control data record do not supply diagnostics and their status is always OK. The value status is OK
- Direct write access to the outputs or write access to the process image of outputs that are not present: Remains without effect; no access error is signaled.
- Direct read access to the inputs or read access to the process image of inputs that are not present: Value "0" is supplied; no access error is signaled.
- Write data record to module that is not present: Remains without effect; no error is signaled.
- Read data record from module that is not present: An error is signaled because a valid data record cannot be returned.

##### Error messages

The following error messages are returned if an error occurs during writing of the control data record:

Error messages

| Error code | Meaning |
| --- | --- |
| 16#80B1 | Invalid length; the length information in data record 196 is not correct. |
| 16#80B5 | Configuration control parameters not assigned. |
| 16#80E2 | Data record was transferred in the wrong OB context. The data record must be transferred in the startup program. |
| 16#80B8 | Parameter error; module signals invalid parameters. |

---

**See also**

[Basic information on VARIANT (S7-1200, S7-1500)](Data%20types.md#basic-information-on-variant-s7-1200-s7-1500)
  
[Important information regarding configuration control (option handling) (S7-1500)](#important-information-regarding-configuration-control-option-handling-s7-1500)
  
[S7-1200 System Manual](http://support.automation.siemens.com/WW/view/en/89851659)

#### Example of a configuration control (S7-1200)

A configuration consisting of a CPU and 3 signal modules is configured in the following.

The module at slot 3 is not present in the first configuration expansion and is "hidden" by the configuration control.

In the second configuration expansion, the module that was initially hidden is located in the last slot. The added slot is made known to the CPU by a modified control data record.

##### Actual configuration with missing module

The specified configuration contains all modules that can be present in a final expansion stage.

The module that is inserted in slot 3 in the specified configuration is missing in the real expanded configuration. For this reason, slot 3 must be coded in the control data record accordingly with "FF <sub>H</sub>" (= not present).

![Actual configuration with missing module](images/79263855115_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Module is missing in the real configuration |

##### Actual configuration with subsequently added module

The module present in slot 3 in the specified configuration is added to the back of the real configuration by inserting it as the last module in slot 4.

The control data record is adapted accordingly.

![Actual configuration with subsequently added module](images/79263872907_DV_resource.Stream@PNG-de-DE.png)

## Using OPC UA communication (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [What you need to know about OPC UA (S7-1200, S7-1500, S7-1500T)](#what-you-need-to-know-about-opc-ua-s7-1200-s7-1500-s7-1500t)
- [Security at OPC UA (S7-1200, S7-1500, S7-1500T)](#security-at-opc-ua-s7-1200-s7-1500-s7-1500t)
- [Using diagnostics options (S7-1200, S7-1500, S7-1500T)](#using-diagnostics-options-s7-1200-s7-1500-s7-1500t)
- [Using the S7-1200 CPU as an OPC UA server (S7-1200)](#using-the-s7-1200-cpu-as-an-opc-ua-server-s7-1200)
- [Using the S7-1500 as an OPC UA server (S7-1500, S7-1500T)](#using-the-s7-1500-as-an-opc-ua-server-s7-1500-s7-1500t)
- [Using the S7-1500 CPU as an OPC UA client (S7-1500, S7-1500T)](#using-the-s7-1500-cpu-as-an-opc-ua-client-s7-1500-s7-1500t)
- [Tips and recommendations (S7-1200, S7-1500, S7-1500T)](#tips-and-recommendations-s7-1200-s7-1500-s7-1500t)

### What you need to know about OPC UA (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [OPC UA and Industrie 4.0 (S7-1200, S7-1500, S7-1500T)](#opc-ua-and-industrie-40-s7-1200-s7-1500-s7-1500t)
- [General features of OPC UA (S7-1200, S7-1500, S7-1500T)](#general-features-of-opc-ua-s7-1200-s7-1500-s7-1500t)
- [OPC UA for S7-1200/S7-1500 CPUs (S7-1200, S7-1500, S7-1500T)](#opc-ua-for-s7-1200s7-1500-cpus-s7-1200-s7-1500-s7-1500t)
- [Supported OPC UA profiles and Conformance Classes (S7-1200, S7-1500, S7-1500T)](#supported-opc-ua-profiles-and-conformance-classes-s7-1200-s7-1500-s7-1500t)
- [Access to OPC UA applications (S7-1200, S7-1500, S7-1500T)](#access-to-opc-ua-applications-s7-1200-s7-1500-s7-1500t)
- [Addressing nodes (S7-1200, S7-1500, S7-1500T)](#addressing-nodes-s7-1200-s7-1500-s7-1500t)
- [Namespace overview for the OPC UA server of the S7-1200/1500 CPUs (S7-1200, S7-1500, S7-1500T)](#namespace-overview-for-the-opc-ua-server-of-the-s7-12001500-cpus-s7-1200-s7-1500-s7-1500t)
- [What you need to know about OPC UA clients (S7-1500, S7-1500T)](#what-you-need-to-know-about-opc-ua-clients-s7-1500-s7-1500t)

#### OPC UA and Industrie 4.0 (S7-1200, S7-1500, S7-1500T)

##### Uniform standard for information and data exchange

Industry 4.0 stands for the intensive utilization, evaluation and analysis of the large volumes of data from production in IT systems at the enterprise level. With Industry 4.0, data exchange between the production and enterprise levels is rapidly increasing. However, a prerequisite for success is a uniform standard for the information and data exchange.

Classic OPC only runs on Windows operating systems. To get around this restriction, the OPC Foundation developed the OPC UA (OPC Unified Architecture) standard.

The OPC UA standard is particularly suitable for data exchange across different levels thanks to its independence from specific operating systems, its secure transfer procedures and the semantic description of data. Machine data (controlled variables, measured values or parameters) can also be transferred in this way.

An important component of this concept is that OPC UA communication can take place in parallel with real-time communication for time-critical, machine-level data transfer.

OPC UA is highly scalable so that a consistent information exchange between sensors, controllers and MES or ERP systems is possible.

OPC UA makes available not only data but also information about the data (data types), at the same time making possible machine-interpretable access to the data.

#### General features of OPC UA (S7-1200, S7-1500, S7-1500T)

##### OPC UA and PROFINET

OPC UA and PROFINET can be used together. The two protocols use the same network infrastructure.

##### Independence from the operating system

The OPC UA standard is platform-independent and uses an optimized TCP-based binary protocol for high-performance applications.

OPC UA can be used, for example, under Windows, Linux, Mac OS X, a realtime operating system or a mobile operating system (Android or iOS).

##### Independence of a specific transport layer

OPC UA currently supports the following transport mechanisms and protocols:

- The transfer of messages as a binary stream directly via TCP/IP
- The transfer of messages with XML via TCP/IP and HTTP. This transport mechanism allows only a slow transfer and is therefore almost never used. S7-1500 CPUs do not support this transport mechanism.

Binary data exchange is supported by all OPC UA applications (required in OPC UA specification).

##### Simple client-server principle

An OPC UA server provides a great deal of information within a network, e.g. relating to the CPU, the OPC UA server itself, the data and the data types. An OPC UA client accesses this information.

##### Implementation in different programming languages

The OPC Foundation has implemented the OPC UA standard in several programming languages: Stacks for .NET, ANSI C and Java are available, although maintenance has been discontinued for the stacks for ANSI C and Java.

The OPC Foundation offers the .NET stack as well as example programs as open source software. See [Github](https://github.com/opcfoundation).

A number of companies offer Software Development Kits (SDK). These development packages contain the stacks of the OPC Foundation and other functionalities that facilitate the development of solutions.

Advantages of using SDKs:

- Support from the supplier
- Tested software
- Detailed documentation
- Clear license conditions (important for selling of solutions)

##### Scalability

OPC UA can be used for devices of different performance classes:

- Sensors
- Embedded systems
- Controllers
- PC systems
- Smartphones
- Servers running MES or ERP applications.

The performance class of the devices is differentiated by profiles. Different OPC UA profiles offer the possibility to scale OPC UA for very small and simple devices as well as for very high-performance devices.

An OPC UA profile describes functions and services that must be supported by the server and client. In addition, other functionalities/services that are not required by the profile can be optionally provided.

OPC UA profiles differ from PROFINET profiles; the latter define additional cross-vendor properties and behavior for installations and systems in the sense of a vendor-neutral software interface.

**Nano Embedded Device 2017 Server Profile**

For the smallest devices with severely limited functionality, there is the "Nano Embedded Device 2017 Server Profile" of the OPC Foundation. This profile is functionally equivalent to the core server facet and defines the OPC UA TCP binary protocol as the required transport profile. The profile allows for connections without UA Security and does not allow subscriptions or method calls. Support for diagnostic objects and variables is optional for this profile.

Additional profiles build on the "Nano Embedded Device 2017 Server Profile", requiring more resources and offering more functionality.

**Micro Embedded Device 2017 Server Profile**

This profile provides limited functionality; it requires at least two parallel connections. Additionally, it allows subscriptions/data monitoring, but no UA Security and no method calls.

- S7-1200 Basic Controllers support the "Micro Embedded Device 2017 Server Profile". The S7-1200 additionally supports UA Security.

**Embedded 2017 UA Server Profile**

This profile has been developed for devices with more than 50 MB RAM and a more high-performance processor. It is based on the Micro Embedded Device Server profile. In addition, it requires UA security and method calls.

In addition, the servers must make their used type model (data types, reference types, variable types, etc.) available.

- S7-1500 Advanced Controllers support the "Embedded 2017 UA Server Profile".

**Standard and global discovery profiles**

The "OPC UA Specification Part 7" defines additional profiles:

- The "Standard 2017 UA Server Profile", which is suitable for PC-based OPC UA servers
- 2 global profiles, "Global Discovery Server 2017 Profile" and "Global Discovery and Certificate Management 2017 Server Profile", that cover the required service and information models of a Global Discovery Server

##### Type-instance concept

OPC UA offers a fully networked (full-meshed network), object-oriented information model for namespaces, including metadata for the object description. Any object structures can be generated via referencing of the instances among each other and their types. Because servers disclose their instance and type systems, clients can navigate through this network and obtain all the information they need. Both instances and their type definitions are available in runtime.

Procedures or concepts on how to handle references to types are optimized over time. These optimizations lead to new versions of the OPC UA Specification (e.g. V1.03 => V1.04).

##### PLC tag mapping

The information of the OPC UA server (for example the PLC tags) is modeled as nodes connected to one another via references. The semantics are displayed by the server in the address space and can be acquired by clients (while navigating). This makes it possible to browse from node to node with an OPC UA client and find out what content can be read, monitored or written.

##### Integrated security mechanisms

OPC UA uses security mechanisms at various levels:

- A secure connection can only be established between an OPC UA server and an OPC UA client if the client and server can register with X.509-v3 certificates and accept each other's certificates (security at the application level). Various security policies are possible, including an unsecured connection between server and client (Security Policy: "No security").
- A server can always request the following information from the user for authorized access (authentication):

  - A user certificate (not configurable in STEP 7)

  - User name and password

  - No user authorization

The security mechanisms are optional and configurable.

---

**See also**

[OPC Foundation](https://opcfoundation.org)

#### OPC UA for S7-1200/S7-1500 CPUs (S7-1200, S7-1500, S7-1500T)

In OPC UA, one system operates as a server and provides data the existing information to other systems (clients).

OPC UA clients, for example, have read and write access to data on an OPC UA server. OPC UA clients call methods on the OPC UA server.

You can access this data online with a client, including e.g. information on performance and diagnostics. In OPC UA terminology, this function is called "Browsen". The "Subscription" function eliminates regular reading of a tag; with this function, the server informs a client about value changes.

A system can be both a client and a server at the same time.

##### OPC UA server of the S7-1500 CPU

As of firmware version 2.0, an S7-1500 CPU is equipped with an OPC UA server.

The following sections describe how you configure the OPC UA server of the S7-1500 CPU to make data and methods available for OPC UA clients so that clients have read or write access to PLC tags on the CPU and can call server methods.

The following sections also set out how to integrate companion specifications into the address space of the OPC UA server.

##### OPC UA server of the S7-1200 CPU

As of firmware V4.4, an S7-1200 CPU is equipped with an OPC UA server.

The OPC UA server is generally configured as it is for an S7-1500 CPU; the scope of functions and the quantity limits are limited according to the supported "Micro Embedded Device 2017 Server Profile". Unlike for an S7-1500 CPU, the functions "Registered Read" and "Registered Write" are **not** available.

As of firmware V4.5, S7-1200 CPUs support server methods as well as structured data types (structures and arrays).

Additional information is available [here](#using-the-s7-1200-cpu-as-an-opc-ua-server-s7-1200).

##### OPC UA client of the S7-1500 CPU

As of firmware version V2.6, an S7-1500 CPU is additionally equipped with an OPC UA client.

The following sections show how to use standardized instructions (PLCopen function blocks) to create a user program that, as an OPC UA client, provides the following functions:

- Reading data from an OPC UA server
- Writing data to an OPC UA server
- Calling methods of an OPC UA server

STEP 7 (TIA Portal) assists you in creating user programs by providing an editor for client interfaces and a parameter assignment for OPC UA connections.

The OPC UA instructions for an S7-1500 CPU as client are described in detail in the help to the instructions (Instructions > Communication > OPC UA).

##### OPC UA client for test purposes

The following description uses various different OPC UA clients to illustrate the use of OPC UA clients:

- "UaExpert" of Unified Automation. An extensive client that can be used free of charge:  
  [Link for downloading UaExpert](https://www.unified-automation.com/downloads/opc-ua-clients.html)
- "UA Sample Client" of the OPC Foundation. This client is available free of charge for users who are registered with the OPC Foundation :  
  [Link for downloading the example client of the OPC Foundation](https://opcfoundation.org)

##### Application example in Industry online support

Siemens Industry Online Support provides a free application example with a client API for various applications. You use the functions of this interface to create your own OPC UA clients that match your application. To simplify handling the API, we offer a higher-level .NET helper class.

The client API is based on the .NET OPC UA stack of the OPC Foundation.

The application example shows how to establish connections between servers and clients, for example. It also demonstrates the reading and writing of PLC tags.

Link to download: [OPC UA .NET client for the SIMATIC S7-1500 OPC UA Server](http://support.automation.siemens.com/WW/view/en/109737901)

#### Supported OPC UA profiles and Conformance Classes (S7-1200, S7-1500, S7-1500T)

As a rule an OPC UA application or an OPC UA device does not support the entire functional scope of OPC UA. An OPC UA server on an embedded system can, for example, not support any Subscriptions or track changes in the own address space.

Differences in functional scope also apply for clients.

In order to be able to manage differences and be able to make them transparent, profiles were introduced for OPC UA.

In simple terms, profiles define the functionality of an OPC UA application.

Additional details and descriptions on the profiles and facets are available under [https://profiles.opcfoundation.org/v104/reporting/.](https://profiles.opcfoundation.org/v104/reporting/)

##### Structuring of the OPC UA functionality

The smallest functional unit is called a "Conformance Unit" at OPC UA. Conformance Units define a manageable set of functions which are used together and which are therefore are tested as a unit with a compliance test tool.

Several Conformance Units can be summarized into one facet. A facet is a named grouping of related Conformance Units to make the lists of supported Conformance Classes more manageable. Facets define specific facets of a server, e.g. the support of event subscriptions.   
Conformance Units and Facets together form a "Full-featured" profile. An OPC UA server must support at least one full featured profile. This profile must be implemented with all contained Conformance Units in order for it to be certified.

An OPC UA application can also support several profiles and a profile can, in turn, include other profiles.

The following figure shows the interaction of profiles, facets and Conformance Units.

![Structuring of the OPC UA functionality](images/172062958475_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Full-featured profile (standalone), e. g. "Embedded 2017 UA Server Profile". Fully supported by an OPC UA application / by a device. |
| ② | Facet = Profile (not standalone), e. g. "Standard DataChange Subscription 2017 Server Facet". Summarized as the "Profiles" ConformanceGroup of OPC UA Standard. |

##### Checking the profiles for runtime

During the connection establishment OPC UA clients and OPC UA servers exchange their list of supported and used profiles. This mechanism allow the applications to check whether the required features are provided by the communication partner.

##### Supported OPC UA profiles: S7-1500 server

The OPC UA server of the S7-1500 CPUs supports the "Embedded 2017 UA Server Profiles" with additional facets as shown in the following table.

The table is based on the table "Profile tables" of the OPC UA specification Part 7 (OPC 10000-7: UA Part 7: Profiles).

The "Group" column names the Conformance Group to which the Conformance Unit belongs. If "Profile" is entered, it is not a Conformance Unit, but rather an included profile.

The column "Conformance Unit / Profile title" offers a short description of the Conformance Unit or the included profile.

Some of the entries in the "Conformance Unit / Profile Title" column are provided with links to the corresponding descriptions (all available at https://profiles.opcfoundation.org/).

| Specification | Group | Conformance Unit / Profile title |
| --- | --- | --- |
| OPC 10000-7 - "CORE" | Profile | Embedded 2017 UA Server Profile   <http://opcfoundation.org/UA-Profile/Server/EmbeddedUA2017> |
| OPC 10000-7 - "CORE" | Session Services | Session Change User |
| OPC 10000-7 - "CORE" | Security General | Security – No Application Authentication |
| OPC 10000-7 - "CORE" | Alarms and Conditions | A & C Comment |
| OPC 10000-7 - "CORE" | Base Information | Base Info Diagnostics |
| OPC 10000-7 - "CORE" | Base Information | Base Info Placeholder Modelling Rules |
| OPC 10000-7 - "CORE" | Attribute Services | Attribute Write Values |
| OPC 10000-7 - "CORE" | Attribute Services | Attribute Write Index |
| OPC 10000-7 - "CORE" | Security General | Security Administration |
| OPC 10000-7 - "CORE" | Base Information | Base Info Custom Type System |
| OPC 10000-7 - "CORE" | Base Information | Base Info Server Capabilities |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – None |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Basic128Rsa15 |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Basic256 |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Basic256Sha256 |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Aes128-Sha256-RsaOaep |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Aes256-Sha256-RsaPss |
| OPC 10000-7 - "CORE" | Profile | Method Server Facet |
| OPC 10000-7 - "CORE" | Profile | User Token – Anonymous Facet |
| OPC 10000-7 - "CORE" | Profile | User Token – User Name Password Server Facet |
| OPC 10000-7 - "CORE" | Profile | ComplexType 2017 Server Facet |
| OPC 10000-7 - "CORE" | Profile | A & C Base Condition Server Facet |
| OPC 10000-7 - "CORE" | Profile | A & C Acknowledgeable Alarm Server Facet |
| OPC 10000-7 - "CORE" | Profile | Standard DataChange Subscription 2017 Server Facet   <http://opcfoundation.org/UA-Profile/Server/StandardDataChangeSubscription2017> |
| OPC 10000-7 - "CORE" | Profile | Global Certificate Management Server Facet   <http://opcfoundation.org/UA-Profile/Server/GlobalCertificateManagement> |
| OPC 10000-100 "DI" | Profile | DI BaseDevice Server Facet   <http://opcfoundation.org/UA-Profile/DI/Server/BaseDevice> |
| OPC 10000-100 "DI" | DI | DI DeviceType |

##### Supported OPC UA profiles: S7-1500 client

The OPC UA client of the S7-1500 CPUs supports the "Minimum UA Client Profiles".

| Specification | Group | Conformance Unit / Profile title |
| --- | --- | --- |
| OPC 10000-7 - "CORE" | Profile | Minimum UA Client Profile   <http://opcfoundation.org/UA-Profile/Client/Minimum> |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – None |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Basic128Rsa15 |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Basic256 |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Basic256Sha256 |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Aes128-Sha256-RsaOaep |
| OPC 10000-7 - "CORE" | Profile | SecurityPolicy – Aes256-Sha256-RsaPss |
| OPC 10000-7 - "CORE" | Profile | User Token – Anonymous Facet |
| OPC 10000-7 - "CORE" | Profile | User Token – User Name Password Server Facet |

##### Supported OPC UA profiles: S7-1200 server

The OPC UA server of the S7-1200 CPUs supports the "Micro-Embedded Device 2017 Server Profile" with additional facets as specified in the following table.

| Specification | Group | Conformance Unit / Profile title |
| --- | --- | --- |
| OPC 10000-7 - "CORE" | Profile | Micro Embedded 2017 UA Server Profile   <http://opcfoundation.org/UA-Profile/Server/MicroEmbeddedDevice2017> |
| OPC 10000-7 - "CORE" | Attribute Services | Attribute Write Values |
| OPC 10000-7 - "CORE" | Attribute Services | Attribute Write Index |
| OPC 10000-7 - "CORE" | Base Information | Base Info Custom Type System |
| OPC 10000-7 - "CORE" | Base Information | Base Info Server Capabilities |
| OPC 10000-7 - "CORE" | Profile | Method Server Facet |
| OPC 10000-7 - "CORE" | Profile | Embedded DataChange Subscription Server Facet   <http://opcfoundation.org/UA-Profile/Server/EmbeddedDataChangeSubscription> |
| OPC 10000-100 "DI" | Profile | DI BaseDevice Server Facet  Profile URI siehe oben. |
| OPC 10000-100 "DI" | Profile | DI DeviceType |

#### Access to OPC UA applications (S7-1200, S7-1500, S7-1500T)

The access possibilities that an S7-1500 CPU with an OPC UA application (client or server) has via a CP in the same station are described below. In addition, an approach for combining these access possibilities with the "IP Forwarding" function to allow access to devices of another IP subnet via an S7-1500 station is presented.

All the settings for this can be found in the CPU properties, "Advanced configuration" area in the Inspector window.

The possibility of accessing the OPC UA application in the CPU via CP interface is subject to the following requirements:

- S7-1500 CPU (except S7-1500 R/H) as of firmware version V2.8
- CP 1543-1 firmware version V2.2 or higher

##### Principle: Interface for access via communication module

For a CPU application, such as OPC UA, to be accessed via CP interface, you must configure a virtual interface (W1). IP-based applications can then be accessed via the IP address parameters of this virtual interface.

The schematic is shown in the following figure.

![Principle: Interface for access via communication module](images/132291883531_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | CPU S7-1500 FW V2.8 or higher (e.g. CPU 1515-2 PN) |
| ② | CP 1543-1 (FW V2.2 or higher) |
| ③ | Virtual interface (W1) |
| ④ | Protocol conversion PROFINET / Industrial Ethernet on backplane bus or backplane bus on PROFINET / Industrial Ethernet |
| ⑤ | Backplane bus |

##### Example: Access of OPC UA clients to the OPC UA server of the CPU

For access of an OPC UA client to the OPC UA server of the CPU, the following interfaces of the S7-1500 station are available:

- The local PROFINET interfaces of the S7-1500 CPU
- The Ethernet interface of a CP 1543-1 (firmware version V2.2 and higher)

The following figure shows an example of a possible configuration: The CPU could also have the role OPC UA client and the device on the subnet of the CP could have the role OPC UA server.

![Example: Access of OPC UA clients to the OPC UA server of the CPU](images/132291895051_DV_resource.Stream@PNG-de-DE.png)

##### Example: Access of OPC UA clients to OPC UA servers via S7-1500 CPU with activated IP Forwarding

OPC UA client and OPC UA server can also be connected to one another via an S7-1500 CPU, in which case the S7-1500 CPU operates as an IP Forwarder. This configuration option allows for flexible expansion of existing systems.

![Example: Access of OPC UA clients to OPC UA servers via S7-1500 CPU with activated IP Forwarding](images/132297948683_DV_resource.Stream@PNG-de-DE.png)

##### Additional information

Additional information on access options via the virtual interface and via IP forwarding can be found in the following sections:

- [Virtual interface for IP-based applications](Configuring%20devices%20and%20networks.md#virtual-interface-for-ip-based-applications)
- [IP forwarding](Configuring%20devices%20and%20networks.md#ip-forwarding)

#### Addressing nodes (S7-1200, S7-1500, S7-1500T)

Nodes are the basic elements of OPC UA, they are comparable with objects from object-oriented programming. Nodes are used, for example, for user data (tags) or other metadata. Nodes are used to model an OPC UA address space that also contains a type model with type definitions.

##### Node ID (NodeId)

Nodes in the OPC UA address space are uniquely identified by a NodeId (Node Identifier).

The NodeId consists of an identifier, identifier type and a namespace index. Namespaces are used to avoid naming conflicts.

The OPC Foundation has defined a wide range of nodes that provide information about the given OPC UA server. These nodes can be found in the namespace of the OPC Foundation and have the index 0.

The OPC Foundation also defines data types and tag types.

##### Namespace (Namespace)

In addition to the above-described namespace of the OPC Foundation, the namespace for accessing CPU data is of interest: All the tags or methods of an S7‑1500 OPC UA server are contained in the namespace (Namespace) of the standard server interface "http://www.siemens.com/simatic-s7-opcua".

By default this namespace has the Index 3. The index may change later if additional namespaces are inserted into the server or if existing ones are deleted. It is therefore necessary for an OPC UA client to request the current index of the namespace (e.g. "http://www.siemens.com/simatic-s7-opcua") from the server before reading or writing its values.

The following figure shows an example of the result of such a request.

![Namespace (Namespace)](images/105750620939_DV_resource.Stream@PNG-de-DE.png)

##### Identifier

The Identifier corresponds to the name of the PLC tag in quotation marks. The quotation mark is the only sign that is not permitted as part of a name in STEP 7. Quotation marks avoid naming conflicts.

The following example reads the value of the "StartTimer" tag:

![Identifier](images/105750629643_DV_resource.Stream@PNG-de-DE.png)

The Identifier can consist of several components. The individual components are then separated by a dot.

The following example reads the "MyDB" array data block completely. This data block contains an array with ten integer values. All ten values should be read in one pass. Therefore, "0:9" is entered at the array range.

![Identifier](images/105750638347_DV_resource.Stream@PNG-de-DE.png)

##### Example of NodeIds, identifiers and namespaces

The following figure illustrates the relation between NodeIds, identifiers and namespaces: It is no problem if two nodes have the same identifiers but belong to different namespaces.

STEP 7 (TIA Portal) allows you to easily import namespaces via a server interface.

![Example of NodeIds, identifiers and namespaces](images/125648436491_DV_resource.Stream@PNG-en-US.png)

##### PLC tags in the address space of the OPC UA server

The figure below shows where the PLC tags in the example are located in the address space of the OPC UA server (S7-1500) (excerpt from UA client):

The "MyDB" data block is a global data block. The data block is therefore located below the node "DataBlocksGlobal". "StartTimer" is a memory tag and is therefore stored below the "Memory" node.

![PLC tags in the address space of the OPC UA server](images/105750647051_DV_resource.Stream@PNG-de-DE.png)

##### Methods in the address space of the OPC UA server

If you implement a method via your user program, it takes the following form in the address space of the OPC UA Server (S7-1500)

(see [Providing methods on the OPC UA server](#providing-methods-on-the-opc-ua-server-s7-1500-s7-1500t)):

![Methods in the address space of the OPC UA server](images/106316140555_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Using the S7-1200 CPU as an OPC UA server (S7-1200)](#using-the-s7-1200-cpu-as-an-opc-ua-server-s7-1200)

#### Namespace overview for the OPC UA server of the S7-1200/1500 CPUs (S7-1200, S7-1500, S7-1500T)

As already written for the topic "Addressing of nodes", the namespace index is part of the node ID. To ensure that a node ID is always unique in the address space, namespaces are used in OPC UA; the BrowseName as the sole means of identifying a node can be ambiguous.

Namespaces are specified at OPC UA through different "Naming Authorities" which develop the OPC UA information models, for example by a working group, the OPC Foundation or organizations that develop standard information models.

Namespaces are identified through a namespace URI; the namespace URI identifies the Naming Authority.

A namespace index is used to optimize accesses to the nodes of the server instead of the namespace URI. The namespace index is a pointer to a namespace array that the server manages. A client reads the namespace index once from the server to be able to access the nodes of the server afterwards with a simple integer instead of a URI string.

The following table contains the assignment between namespace URIs and namespace indexes of S7-1500 and S7-1200 CPUs.

##### Assignment between namespace URI and namespace index

The namespace indexes are fixed at S7-1200 and S7-1500 CPUs for the namespace indexes 0 to 3. Further namespace indexes are currently not specified.

| Namespace URI | Namespace index | Description |
| --- | --- | --- |
| http://opcfoundation.org/UA/ | 0 | Namespace for the node IDs and BrowseNames of the OPC UA specification (OPC 10000-3).   **Example**   0:EngineeringUnits |
| Local Server URI  ("urn:" + application name as configured in TIA Portal (area "OPC UA > General" in the CPU properties)) | 1 | Namespace for nodes that are defined in the local server (OPC 10000-5).   **Example**   urn:SIMATIC.S7-1500.OPC-UA.Application:PLC_1 |
| http://opcfoundation.org/UA/DI/ | 2 | Namespace for node IDs and BrowseNames of the OPC UA specification for devices (OPC 10000-100).   **Example**   2:DeviceRevision |
| http://www.siemens.com/simatic-s7-opcua | 3 | Namespace for node IDs and BrowseNames that are defined product-specifically for an S7-1200/S7-1500 CPU. In this namespace instances (CPU, tags, DBs, etc.) as well as their types (UDTs, LDTs, FBs, etc.) are defined.    **Example**   3:DataBlocksGlobal |
| URIs of additional namespaces for further instances and types   **Examples**   http://machinesupplier.org/implementedPackML  http://opcfoundation.org/UA/PackML | > 3 | Not specified. Can, for example, be defined with SiOME.   **Examples**   4:MyPackMLMachineInstance  5:PackMLBaseObjectType |

---

**See also**

[OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500)

#### What you need to know about OPC UA clients (S7-1500, S7-1500T)

##### Basics of OPC UA clients

OPC UA clients are programs that do the following:

- Access the information from an OPC UA server (for example an S7-1500 CPU): read/browse access, write access, subscriptions
- Execute methods through the OPC UA server

However, OPC US clients can only access data that is enabled for this purpose (see "[Managing write and read rights](#managing-write-and-read-rights-s7-1500-s7-1500t)").

You need the endpoint of the server to establish a connection to an OPC UA server (see "[Endpoints of the OPC UA servers](#end-points-of-the-opc-ua-server-s7-1500-s7-1500t)").

##### Reading out information from the OPC UA server

When a connection to an end point of the server exists, you can use the navigation function of the client: You navigate starting from a defined starting point (from the "root" node) through the address space of the server.

The following information is provided in the process:

- Enabled PLC tags, data blocks and data block components
- Namespace index and identifiers of these PLC tags, data blocks and DB components
- Data types of the PLC tags and DB components
- Number of components in arrays (required for reading and writing arrays)

In addition, you receive information about the OPC UA server itself as well as information about the S7-1500 based on the "OPC UA for Devices" standard of the OPC Foundation (for example, serial number, firmware version).

##### Reading data from the server and writing to the server

You now know the namespace, identifier and data type of PLC tags. This means that you can now specifically read individual PLC tags and DB components as well as complete arrays and structures.

You can find examples of the reading of Boolean tags and array data blocks in [Addressing nodes](#addressing-nodes-s7-1200-s7-1500-s7-1500t).

Rules for access to structures are available [here](#rules-for-the-access-to-structures-s7-1500-s7-1500t).

With the information that you obtain while navigating through the address space of the server (index, identifier and data type), you can also transfer values to the S7-1500 with the OPC UA client. The following example overwrites the first three values in the array data block "MyDB".

![Reading data from the server and writing to the server](images/105750673163_DV_resource.Stream@PNG-de-DE.png)

For "Array Range" you specify which components of the array you want to overwrite. The "Good" status code indicates that the values were transferred successfully. However, you can only write the values to the S7-1500 but not the time stamps of these values. The time stamps can only be read.

##### Faster access through registration

Registered Read/Write lends itself to repeated, optimized access to data – with maximum performance. When tag nodes are registered, the OPC UA server creates a numerical Identifier (numerical NodeId) that directly references the registered node. For read or write jobs of the client to this numerical Identifier, the server does not have to resolve any strings as Identifier and can access the requested tag in an optimized manner.

This Identifier applies solely to the current session and has to be queried again when the session connection is terminated/lost.

In the following example, the "StartTimer" tag is first registered on the server. Afterwards, the rapid function "RegisteredWrite" is used for setting the value.

![Faster access through registration](images/105750720779_DV_resource.Stream@PNG-de-DE.png)

In accordance with the same scheme, the "RegisteredRead" function can also be used, which is particularly useful for recurring data readouts. Take into account, however, that depending on the application it may be advisable to use a Subscription instead.

Recommendation: It is best to place registrations in the startup program of the OPC UA client, since the registration takes up time.

Please note that you can set the maximum number of registered nodes in the properties of the S7-1500 CPU and that the Clients have to respect this number, see [General settings of the OPC UA server](#general-settings-of-the-opc-ua-server-s7-1500-s7-1500t).

##### Subscription

The term "Subscription" is used for a function in which only those tags for which an OPC UA client has registered at the OPC UA server are transferred. The OPC UA server only sends a message to the OPC UA client for these registered tags (monitored Items) when a value has changed. The monitoring of these tags makes constant sampling by the OPC UA client (Polling)superfluous, which reduces the network load.

You have to create a Subscription to use this function. For this purpose, you specify the "Publishing Interval" at the UA client and click the "Create" button. The publishing interval is the time interval in which the server sends new values to the client in a notification (data change notification).

In the following example a subscription has been created: The client receives a message with the new values (publishing interval 50 ms) every 50 milliseconds here.

![Subscription](images/105750703371_DV_resource.Stream@PNG-de-DE.png)

**Preventing server overload**

You can set the OPC UA server of the S7-1500 CPU by means of the "Minimum publishing interval" so that it does not serve extremely short send intervals requested by the client, see [Settings of the server for subscriptions](#settings-of-the-server-for-subscriptions-s7-1500-s7-1500t).

**Example**: A client wants to be operated at a publishing interval of 50 ms as detailed above. Such a short publishing interval would, however, result in a high network and server load. You should therefore set 1000 ms as the "Minimum publishing interval" for the server. Clients whose subscription requires shorter publishing intervals are "slowed" to 1000 ms and the server is protected from overload.

Sampling and transmission (Sampling & Publishing) within the scope of a subscription are communication processes which, like other communication processes (TCP/UDP/Web server communication...), are processed by the CPU with priority 15. OBs with higher priority interrupt the communication. If you set the sampling and transmission intervals too short, this setting causes a high communication load. Therefore, select intervals as large as possible, which are still sufficient for the application.

For information about the consistency of tags, refer to [Consistency of tags](#consistency-of-tags-s7-1500-s7-1500t).

##### Monitoring of PLC tags

When the Subscription has been created, you inform the server which tags are to be monitored with it. In the following example, the "Voltage" tag was added to the subscription.

![Monitoring of PLC tags](images/105750712075_DV_resource.Stream@PNG-de-DE.png)

The "Voltage" tag contains the value of a voltage that is detected by an S7-1500 CPU.

The sampling interval ("Sampling Interval") contains a negative value (-1). This determines that the default setting of the OPC UA server is used for the sampling interval. The default setting is defined by the transmission interval ("Publishing Interval") of the subscription. If you want to set the smallest possible sampling interval, select the value "0".

In this example, the length of the queue is set to "1": Only one value is read from the CPU at an interval of 50 milliseconds and subsequently sent to the OPC UA client when the value has changed.

The "Deadband" parameter in this example is "0.1": Changes in value have to amount to 0.1 Volt; only then does the sender send the new value to the client. The server does not send smaller changes in value. You can use this parameter, for example, to disable signal noise: Slight changes in a process variable which do not have a real meaning.

---

**See also**

[Interesting information about the OPC UA server of the S7-1200 CPUs (S7-1200)](#interesting-information-about-the-opc-ua-server-of-the-s7-1200-cpus-s7-1200)

### Security at OPC UA (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Security settings (S7-1200, S7-1500, S7-1500T)](#security-settings-s7-1200-s7-1500-s7-1500t)
- [Certificates pursuant to ITU X.509 (S7-1200, S7-1500, S7-1500T)](#certificates-pursuant-to-itu-x509-s7-1200-s7-1500-s7-1500t)
- [Certificates with OPC UA (S7-1200, S7-1500, S7-1500T)](#certificates-with-opc-ua-s7-1200-s7-1500-s7-1500t)
- [Creating self-signed certificates (S7-1200, S7-1500, S7-1500T)](#creating-self-signed-certificates-s7-1200-s7-1500-s7-1500t)
- [Generating PKI key pairs and certificates yourself (S7-1200, S7-1500, S7-1500T)](#generating-pki-key-pairs-and-certificates-yourself-s7-1200-s7-1500-s7-1500t)
- [Secure transfer of messages (S7-1200, S7-1500, S7-1500T)](#secure-transfer-of-messages-s7-1200-s7-1500-s7-1500t)
- [Certificate management via Global Discovery Server (GDS) (S7-1500, S7-1500T)](#certificate-management-via-global-discovery-server-gds-s7-1500-s7-1500t)

#### Security settings (S7-1200, S7-1500, S7-1500T)

##### Addressing risks

OPC UA allows the exchange of data between different systems, both within the process and production levels and to systems at the control and enterprise level.

This possibility also entails security risks. That is why OPC UA provides a range of security mechanisms:

- Verification of the identity of OPC UA server and clients.
- Checking of the identity of the users.
- Signed/encrypted data exchange between OPC UA server and clients.

These security policies should only be bypassed in cases where it is absolutely necessary:

- During commissioning
- In stand-alone projects without external Ethernet connection

If you have selected the endpoint "None" for "UA Sample Client" of the OPC Foundation, for example, the program issues a clear warning:

![Addressing risks](images/105750903179_DV_resource.Stream@PNG-de-DE.png)

When STEP 7 compiles your project it also checks whether you have considered the setting options for the protection and warns you of possible risks. This also includes an OPC UA security policy with the setting "no security", which corresponds to the end point "None".

> **Note**
>
> **Disabling security policies you do not want**
>
> If you have enabled all security policies in the secure channel settings of the S7-1500 OPC UA server – thus, also the end point "None" (no security) – unsecured data traffic (neither signed nor encrypted) between the server and client is also possible. The OPC UA server of the S7-1500 CPU also sends its public certificate to the client at "None" (No security). And some clients check this certificate. However, the client is not forced to send a certificate to the server. The identity of the client may possibly remain unknown. Each OPC UA client can then connect to the server irrespective of any subsequent security settings.
>
> When configuring the OPC UA server, make sure that only security policies that are compatible with the security concept of your machine or plant are selected. All other security policies should be disabled.
>
> Recommendation: Use the setting "Basic256Sha256 - Sign and Encrypt", which means that the server only accepts Sha256 certificates. The security policies "Basic128Rsa15" and "Basic256" are deactivated by default and should not be used as an end point. Select end points with a higher security policy.

##### Additional security rules

- Only use the end point "None" in exceptional cases.
- Only use the "guest authentication" of the user in exceptional cases.
- Only allow access to PLC tags and DB components via OPC UA if it is genuinely necessary.
- Use the list of trusted clients in the settings of the S7-1500 OPC UA client to allow access to certain clients only.

---

**See also**

[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)
  
[Secure Channel - Select Security Policies (S7-1500, S7-1500T)](#secure-channel---select-security-policies-s7-1500-s7-1500t)

#### Certificates pursuant to ITU X.509 (S7-1200, S7-1500, S7-1500T)

Security mechanisms are integrated in several layers in OPC UA. Digital certificates have an important role here. An OPC UA client can only establish a secure connection to an OPC UA server when the server accepts the digital certificate of the client and classifies it as trusted.

See section [Handling client and server certificates](#handling-client-and-server-certificates-s7-1500-s7-1500t).

The client must also check and trust the certificate of the server. The server and client must show their identities and prove that they are what they claim to be: They must prove their identity. Mutual authentication of client and server, for example, prevents man-in-the-middle attacks.

##### Man-in-the-middle attacks

A "man-in-the-middle" could have positioned itself between server and client. A man-in-the-middle is a program that intercepts communication between server and client and claims to be a client or server, and is thus able to obtain information about the S7 program or to set values in the CPU and attack a machine or plant.

OPC UA uses digital certificates that meet standard X.509 of the International Telecommunication Union (ITU).

This allows the identity of a program, a computer or an organization to be proven (authenticated).

##### X.509 certificates

An X.509 certificate includes the following information:

- Version number of the certificate
- Serial number of the certificate
- Information on the algorithm used by the certificate authority to sign the certificate.
- Name of the certificate authority
- Start and end of the validity period of the certificate
- Name of the program, person or organization for which/whom the certificate has been signed by the certificate authority.
- The public key of the program, person or organization.

An X509 certificate thus links an identity (name of a program, person or an organization) to the public key of the program, person or organization.

**Check during connection establishment**

When a connection is being established between the client and server, the devices check all information from the certificate that is required to determine its integrity, such as signature, period of validity, application name (URN) and, in case of firmware version V2.5 only, also the IP address of the client in the client certificate.

> **Note**
>
> The validity period stored in the certificate is also checked. The CPU clock must therefore be set and date/time must be within the validity period, otherwise no communication takes place.

##### Signing and encryption

To allow you to check whether a certificate has been manipulated, certificates are signed.

There are various possible procedures here**:**

- Within the TIA Portal you have the possibility to generate and sign certificates. If you have protected your project and are logged in as a user with the function right to make security settings, you can use the global security settings. The global security settings allow access to the certificate manager and therefore to the certificate authority (CA) of the TIA Portal.
- Additional options are available for creating and signing certificates. In the TIA Portal, you can import certificates into the global certificate manager.

  - You contact a certificate authority (CA) and have your certificate signed.

    In this case, the certificate authority checks your identity and signs your certificate with the private key of the certificate authority. For this purpose you send a CSR (Certificate Signing Request) to the certificate authority.
  - You yourself create a certificate and sign it.

    To this purpose you use, for example, the "Opc.Ua.CertificateGenerator" program of the OPC Foundation. Alternatively, you use OpenSSL.   
    You can find additional information in [Generating PKI key pairs and certificates yourself](#generating-pki-key-pairs-and-certificates-yourself-s7-1200-s7-1500-s7-1500t).

##### Useful information: Certificate types

- Self-signed certificate:

  Each device generates and signs its own certificate. Application examples: Static configuration with limited number of communication nodes.

  No new certificates can be derived from a self-signed certificate. However, you need to load all self-signed certificates from partner devices to the CPU (STOP required).
- CA certificate:

  All certificates are generated and signed by a certificate authority. Application examples: Dynamically growing plants.

  You only need to download the certificate from the certificate authority to the CPU. The certificate authority can generate new certificates (partner devices can be added without CPU STOP).

##### Signing

The signature makes it possible to prove the integrity and source of a message as detailed below.

Signing starts with the sender creating a hash value from the plain text (plain text message). The sender then encrypts the hash value with its private key and subsequently transfers the plain text together with the encrypted hash value to the recipient. To verify the signature, the recipient needs the public key of the sender (this is contained in the X509 certificate of the sender). The recipient uses the sender's public key to decrypt the hash value received. The recipient then forms the hash value themselves from the plain text received (the hash process is contained in the sender's certificate). The recipient compares the two hash values:

- If the two hash values are identical, the plain text message has reached the receiver unchanged and has not been manipulated.
- If the two hash values do not match, the plain text message has not reached the receiver unchanged. The plain text message has been manipulated or has been distorted during transfer.

##### Encryption

Encrypting data prevents unauthorized parties from reading the content. X509 certificates are not encrypted; they are public and can be viewed by anyone.

Encryption involves the sender encrypting the plain text message with the public key of the recipient. To do so, the sender requires the recipient's X509 certificate, as it contains the public key of the recipient. The recipient decrypts the message with their private key. Only the recipient can decrypt the message: They alone hold the private key. The private key must therefore never be disclosed.

##### Secure channel

OPC UA uses the private and public key of client and server to establish a secure connection, the secure channel. Once the secure connection has been established, the client and server generate an internal key only known to them which they both use for signing and encrypting messages. This symmetric process (a shared key) is much faster than asymmetric processes (private and public key).

---

**See also**

[Creating self-signed certificates (S7-1200, S7-1500, S7-1500T)](#creating-self-signed-certificates-s7-1200-s7-1500-s7-1500t)
  
[Certificates with OPC UA (S7-1200, S7-1500, S7-1500T)](#certificates-with-opc-ua-s7-1200-s7-1500-s7-1500t)
  
[Using certificates with TIA Portal](https://support.industry.siemens.com/cs/ww/en/view/109769068)
  
Secure Communication

#### Certificates with OPC UA (S7-1200, S7-1500, S7-1500T)

##### Usage of X509 certificates with OPC UA

OPC UA uses various types of X.509 certificates for establishing a connection from client to server:

- OPC UA application certificates

  Such X.509 certificates identify the software instance, the installation of client or server software. For the "Organization name" attribute, you enter the name of the company that uses the software.

  > **Note**
  >
  > The OPC UA server of the S7-1500 uses application certificates even for the security setting "None" (no security). This ensures compatibility to OPC UA V1.1 and earlier versions.
- OPC UA software certificates

  This X-509 certificate identifies a specific version of the client or server software. These certificates contain attributes that describe which tests this version of the software has passed during certification by the OPC Foundation (or recognized test laboratories). For the "Organization name" attribute, you enter the name of the company that has developed or markets the software.

  > **Note**
  >
  > Software certificates are not supported in STEP 7.
- OPC UA user certificates

  This X.509 certificate identifies the specific user who, for example, retrieves process data from the OPC UA server. This certificate is not required if the user can authenticate itself with a password, or if anonymous access is configured.

  > **Note**
  >
  > User certificates are not supported in STEP 7.

The described certificates are end-entity certificates: They identify, for example, a person, an organization, a company or an instance (installation) of a software.

#### Creating self-signed certificates (S7-1200, S7-1500, S7-1500T)

##### Using the client's certificate generator

Many OPC UA client applications or SDKs are integrated in a sample application that allows you to generate certificates for the client from this application.

The description for certificate generation can generally be found in the context for describing the OPC UA client application.

**Example client from the online support**

The [OPC UA .NET client for the SIMATIC S7-1500 OPC UA server](https://support.industry.siemens.com/cs/ww/en/view/109737901) creates a self-signed software certificate of the client application in the Windows Certificate Store during the first program start. The documentation for this example describes the procedure for handling these certificates.

##### Using the certificate generator of the TIA Portal

If you use an OPC UA client that does not generate a client certificate, you can create self-signed certificates with STEP 7.

To do this, follow these steps:

1. In the properties of the CPU, double-click "<Add new>" under "Protection & Security > Certificate manager > Device certificates".
2. Click "Add".
3. In the "Create a new certificate" dialog, select the "OPC UA client" option for "Usage".
4. Click "OK".

In the field "Subject Alternative Name" STEP 7 automatically enters the URI for the generated certificate. In the program-specific certificate generation by means of the .NET stack of the OPC Foundation, the field is called, for example, "ApplicationUri" - it can have a different name in other tools for certificate generation.

---

**See also**

[Handling of the client certificates of the S7-1500 CPU (S7-1500, S7-1500T)](#handling-of-the-client-certificates-of-the-s7-1500-cpu-s7-1500-s7-1500t)

#### Generating PKI key pairs and certificates yourself (S7-1200, S7-1500, S7-1500T)

This section is only relevant if you want to use an OPC UA client that cannot itself create a PKI key pair and a client certificate. In this case, you generate a private and a public key using OpenSSL, generate an X.509 certificate, and sign the certificate yourself.

##### Using OpenSSL

OpenSSL is a tool for Transport Layer Security that you can use to create certificates. You can also use other tools, for example XCA, a type of key management software with a graphical user interface for an improved overview of certificates issued.

To work with OpenSSL under Windows, follow these steps:

1. Install OpenSSL under Windows. If you are using a 64-bit version of the operating system, install OpenSSL in the "C:\OpenSSL-Win64" directory, for example. You can obtain OpenSSL-Win64 as a download from various providers for open source software.
2. Create a directory, for example "C:\demo".
3. Open the command prompt. To do so, click "Start" and enter "cmd" or "command prompt" in the search field. Right-click "cmd.exe" in the results list and run the program as an administrator. Windows opens the command prompt.
4. Change to the "C:\demo" directory. To do this, enter the following command: "cd C:\demo".
5. Set the following network variables:

   - set RANDFILE=c:\demo\.rnd
   - set OPENSSL_CONF=C:\OpenSSL-Win64\bin\openssl.cfg

   The figure below shows the command line with the following commands:

   ![Using OpenSSL](images/105750850955_DV_resource.Stream@PNG-de-DE.png)
6. Now start OpenSSL. If OpenSSL has been installed in the C:\OpenSSL-Win64 directory, enter the following: C:\OpenSSL-Win64\bin\openssl.exe The figure below shows the command line with the following command:

   ![Using OpenSSL](images/105750859659_DV_resource.Stream@PNG-de-DE.png)
7. Generate a private key. Save the key to the "myKey.key" file. The key in this example is 1024 bits long; for greater RSA security, use 2048 bits in practice. Enter the following command: "genrsa -out myKey.key 2048" ("genrsa -out myKey.key 1024" in the example). The figure below shows the command line with the command and the output of OpenSSL:

   ![Using OpenSSL](images/105750868363_DV_resource.Stream@PNG-de-DE.png)
8. Generate a CSR (Certificate Signing Request). To do this, enter the following command: "req -new -key myKey.key -out myRequest.csr". During execution of this command, OpenSSL queries information about your certificate:

   - Country name: for example "DE" for Germany, "FR" for France
   - State or province name: for example "Bavaria".
   - Location Name: for example "Augsburg".
   - Organization Name: Enter the name of your company.
   - Organizational Unit Name: for example "IT"
   - Common Name: for example "OPC UA client of machine A"
   - Email Address:

> **Note**
>
> **Note for S7-1500 CPU as server with firmware version V2.5**
>
> The IP address of the client program has to be stored in the "Subject Alternative Name" field of the created certificate for S7-1500 CPUs version V2.5 (only for this version); otherwise, the CPU will not accept the certificate.

The information you enter is added to the certificate. The figure below shows the command line with the command and the output of OpenSSL:

![Using OpenSSL](images/105750877067_DV_resource.Stream@PNG-de-DE.png)

The command creates a file in the C:\demo directory containing the Certificate Signing Request (CSR); in the example, this is "myRequest.csr".

##### Using the CSR

There are two ways to use a CSR:

- You send the CSR to a certificate authority (CA): Read the information of the respective certification authority. The certificate authority (CA) checks your information and identity (authentication) and signs the certificate with the private key of the certificate authority. You receive the signed X.509 certificate and use this certificate for OPC UA, HTTPS or Secure OUC (secure open user communication), for example. Your communication partners use the public key of the certificate authority to check whether your certificate was really issued and signed by that CA (i.e. that the certificate authority has confirmed your information).
- You sign the CSR yourself: Using your private key. This option is shown in the next step.

##### Signing the certificate yourself

Enter the following command so that you can generate and sign your certificate (self-signed certificate) yourself: "x509 -req -days 365 -in myRequest.csr -signkey myKey.key -out myCertificate.crt".

The figure below shows the command line with the command and OpenSSL:

![Signing the certificate yourself](images/105750885771_DV_resource.Stream@PNG-de-DE.png)

The command generates an X.509 certificate with the attributes that you transfer with the CSR (in the example "myRequest.csr"), for example with a validity of one year (-days 365). The command also signs the certificate with your private key ("myKey.key" in the example). Your communication partners can use your public key (contained in your certificate) to check that you are in possession of the private key that belongs to this public key. This also prevents your public key from being misused by an attacker.

With self-signed certificates, you yourself confirm that the information in your certificate is correct. There is no independent body that checks your information.

---

**See also**

[Handling of the client certificates of the S7-1500 CPU (S7-1500, S7-1500T)](#handling-of-the-client-certificates-of-the-s7-1500-cpu-s7-1500-s7-1500t)

#### Secure transfer of messages (S7-1200, S7-1500, S7-1500T)

##### Establishing secure connections with OPC UA

OPC UA uses secure connections between client and server. OPC UA checks the identity of the communication partners. OPC UA uses certificates in accordance with X.509-V3 from the ITU (International Telecommunication Union) for client and server authentication. Exception: A secure connection is not established with the "No security" security policy.

##### Message security mode

OPC UA uses the following security policies to protect messages:

- No security

  All messages are unsecured. In order to use this security policy, establish a connection to a None end point of a server.
- Signing

  All message are signed. This allows the integrity of the messages received to be checked. Manipulations are detected. In order to use this security policy, establish a connection to a Sign end point of a server.
- Sign & Encrypt

  All messages are signed and encrypted. This allows the integrity of the messages received to be checked. Manipulations are detected. What is more, no attacker can read the content of the message (protection of confidentiality). In order to use this security policy, establish a connection to a "SignAndEncrypt" end point of a server.

The security policies are also named according to the algorithms used. Example: "Basic256Sha256 - Sign & Encrypt" means: Secure endpoint, supports a series of algorithms for 256-bit hashing and 256-bit encryption.

##### Layers required

The figure below shows the three layers that are always required for establishing a connection: the transport layer, the secure channel and the session.

![Necessary layers: transport layer, secure channel and session](images/133961923083_DV_resource.Stream@PNG-en-US.png)

Necessary layers: transport layer, secure channel and session

- Transport layer:

  This layer sends and receives messages. OPC UA uses an optimized TCP-based binary protocol here. The transport layer is the basis for the subsequent secure channel.
- Secure channel

  The secure channel receives the data received from the transport layer, and forwards that data to the session. The secure channel forwards data of the session that is to be sent to the transport layer.

  In "Sign" security mode, the secure channel signs the data (messages) that is sent. When a message is received, the secure channel checks the signature to detect any manipulations.

  With a "SignAndEncrypt" security policy, the secure channel signs and encrypts the send data. Data received is decrypted by the secure channel, and the secure channel then checks the signature.

  With the "No security" security policy, the message packages pass the secure channel unchanged (the messages are received and sent in plain text).
- Session

  The session forwards the messages from the secure channel to the application, or receives from the application the messages that are to be sent. The application uses the process values or provides the values.

##### Establishing the secure channel

The secure channel is established as follows:

1. The server starts establishing the secure channel when it receives a request to this effect from the client. This request is signed or signed and encrypted, or the message is sent in plain text (security mode of the selected server end point). With "Sign" and "Sign & Encrypt", the client sends a "secret" (random number) with the request.
2. The server validates the client certificate (contained in the request, unencrypted) and checks the identity of the client. If the server trusts the client certificate,

   - it decrypts the message and checks the signature ("Sign & Encrypt"),
   - checks the signature only ("Sign"),
   - or leaves the message unchanged ("No security")
3. The server then sends a response to the client (same level of security as the request). The server secret is contained in the response. The client and server calculate a symmetric key from the client and server secret. The secure channel is now established.

The symmetric key (instead of the private and public key of client and server) is now used for signing and encrypting messages.

##### Establishment of the session

The session is executed as follows:

1. The client starts establishing the session by sending a CreateSessionRequest to the server. This message contains a Nonce, a random number that is only used once. The server must sign this random number (Nonce) to prove that it is the owner of the private key. The private key belongs to the certificate that the server uses to establish the secure channel. This message (and all subsequent messages) is secured in line with the security policies of the selected server endpoint (selected security policies).
2. The server responds with the CreateSession Response. This message contains the public key of the server and the signed Nonce. The client checks the signed Nonce.
3. If the server passes the test, the client sends a SessionActivateRequest to the server. This message contains the information that is required for user authentication:

   - User name and password, or
   - X.509 certificate of the user (not supported in STEP 7), or
   - No data (if anonymous access is configured).

   In OPC UA, the data required to authenticate the user is transferred with a separate security policy. This security policy is  
   referred to as the "UserTokenPolicy". Regardless of the configured security policies for the secure channel, the client selects an appropriate "UserTokenPolicy" for its needs. This UserTokenPolicy ensures that a UserIdentityToken (e.g. user name and password) is always transferred with adequate security settings.

   The OPC UA client is then able to transfer the user name and password with encryption if there is "No security" for the secure channel based on the configured security policy.
4. If the user has the necessary rights, the server returns a message to the client (ActivateSessionResponse). This activates the session.

The secure connection between the OPC UA client and server has been established.

##### Establishing a connection to PLCopen function block

The PLCopen specification defines a range of IEC 61131 function blocks for OPC UA clients. The instruction UA_Connect initiates both a secure channel and a session following the pattern described above.

---

**See also**

[User authentication (S7-1500, S7-1500T)](#user-authentication-s7-1500-s7-1500t)

#### Certificate management via Global Discovery Server (GDS) (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Automated certificate management with GDS (S7-1500, S7-1500T)](#automated-certificate-management-with-gds-s7-1500-s7-1500t)
- [Configuration limits for GDS push function (S7-1500, S7-1500T)](#configuration-limits-for-gds-push-function-s7-1500-s7-1500t)
- [Setting and loading GDS parameters (S7-1500, S7-1500T)](#setting-and-loading-gds-parameters-s7-1500-s7-1500t)
- [GDS commissioning (S7-1500, S7-1500T)](#gds-commissioning-s7-1500-s7-1500t)
- [Address model for the push certificate management (S7-1500, S7-1500T)](#address-model-for-the-push-certificate-management-s7-1500-s7-1500t)
- [CertificateGroups in the address model (S7-1500, S7-1500T)](#certificategroups-in-the-address-model-s7-1500-s7-1500t)

##### Automated certificate management with GDS (S7-1500, S7-1500T)

**As of TIA Portal V17 and S7-1500 CPU firmware version V2.9**, you can use the certificate management services of the OPC UA server for transferring OPC UA server certificates at runtime.

OPC UA certificates, trust lists and certificate revocation lists (CRLs) for the OPC UA server of the S7-1500 CPU can be updated automatically using GDS push management functions. The automation of the certificate management eliminates any manual work required for reconfiguring the CPU, for example, after a certificate has expired, and a fresh download of the CPU. You can also use the GDS push management functions to transfer updated certificates and lists in the STOP and RUN operating states of the CPU.

The certificate management information model is specified in OPC UA Part 12 (OPC 10000-12: OPC Unified Architecture, Part 12: Discovery and Global Services).

**From TIA Portal version V18 onwards and S7-1500 CPU firmware version V3.0** onwards, you can also use the GDS push management function for web server certificates. The sequence of, for example, certificate updates via GDS push-management functions is identical here in principle to the certificate update of OPC UA server certificates. Instead of OPC UA server certificates, you transfer web server certificates to the CPU at runtime or during operation. The differences or restrictions are explained in the following description at the corresponding places.

The following sections provide a general overview of Global Discovery Services and the function of an automated certificate update supported as of TIA Portal V17 / CPU firmware version V2.9.

###### Discovery server

To connect to an OPC UA server, an OPC UA client requires information about its endpoint such as the endpoint URL and the security policy. When a large number of possible servers are available in the network, a discovery server can take over the search and management of this server information.

- OPC UA servers register with the discovery server.
- OPC UA clients request a list of accessible servers from the discovery server and then connect to the desired OPC UA server.

###### Global Discovery Server (GDS)

The OPC UA GDS concept allows the configuration of cross-subnet discovery services on the one hand and provides interfaces for central certificate management on the other hand.

A Global Discovery Server (GDS) makes mechanisms available for the central management of the following components:

- CA-signed certificates and self-signed certificates
- Trusted Lists and Certificate Revocation Lists (CRL)

A GDS thus provides an access point to central certificate management and takes over the task of a security server within an OPC UA network.

The main application of GDS is the management of CA-signed certificates with the corresponding CRLs:

- Initial creation of an application certificate, for example, for the OPC UA server or for the web server.
- Regular update of the trust list and the CRLs
- Renovation of an application certificate

###### Certificate management

Certificate management has the task of automating the administration and distribution of certificates and trust lists for different services or applications.

In this context, a distinction is made between the following roles:

- Certificate manager - an OPC UA application that provides certificate management functions
- Certificate recipient – an OPC UA application that receives certificates, trust lists and CRLs from the certificate manager.

There are two models for certificate management: Pull and push management.

- With pull management, the OPC UA application acts as a client of the GDS server and uses certificate management methods to request certificate updates and trust list updates.
- With push management, the OPC UA application acts as a server and provides methods for an OPC UA GDS as OPC UA client. The GDS in the role of certificate manager uses these methods to transfer ("push") certificates and trusted list updates, see explanation of the concept for automated certificate update below.

As of firmware version V2.9, the S7-1500 CPU initially only supports push management for the OPC UA server of the CPU.

###### System configuration with GDS

The figure below shows an example of the tasks of the devices involved in combination with a GDS that provides certificate management functions.

![System configuration with GDS](images/137075539979_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Root CA - device that issues certificates for the system (these certificates can also be transmitted in other ways, for example, by email) |
| ② | OPC UA GDS with certificate manager creates or signs device certificates, manages trust lists and certificate revocation lists (CRLs), and writes certificates and lists to the devices (push function). This device requires OPC UA client functionality for the push function. |
| ③ | Device with OPC UA application receives "pushed" certificates and lists |

###### Concept for automated certificate update for STEP 7 version V17 and higher

GDS and certificate manager are usually combined into one application; however, in the figure below, they are two separate components.

Devices such as "normal" OPC UA clients are also suitable as certificate managers, but they need to support the Bytestring data type that is required to transfer certificates, for example, an S7-1500 CPU firmware V2.9 and higher as OPC UA client or the UA Expert tool (Unified Automation) with GDS plugin.

The OPC UA server of the S7-1500 CPU as certificate receiver provides the standardized methods and attributes that the OPC UA client certificates need to read and write trust lists and CRLs.

The focus in the context of the OPC UA server of the S7-1500 CPU is the description of the push function in contrast to the usual manner in which certificates are provided to the CPU: By loading the hardware configuration.

The figure below shows how to transfer certificates and lists for OPC UA in an S7-1500 CPU FW V2.9 or higher:

- Either by loading the hardware configuration in STOP of the CPU; the certificates are part of the hardware configuration.
- Or via GDS push methods in RUN or in STOP mode of the CPU.

It is not possible to use both transmission paths in parallel. If, for example, you have opted for transfer of OPC UA server certificates with GDS push functions at runtime, you must also transmit all the other certificate types to the CPU via this route.

![Concept for automated certificate update for STEP 7 version V17 and higher](images/139489297931_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Certificates with OPC UA (S7-1200, S7-1500, S7-1500T)](#certificates-with-opc-ua-s7-1200-s7-1500-s7-1500t)
  
[What you should know about the certificate management (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#what-you-should-know-about-the-certificate-management-s7-1200-s7-1500-s7-1500t)

##### Configuration limits for GDS push function (S7-1500, S7-1500T)

###### Number of certificates for Push function

For the OPC UA Push function, an S7-1500 CPU, regardless of the type, has a configuration limit of 62 trust list entries as of firmware version V2.9.

- Each activated certificate-based service (CPU application) "consumes" one entry each for a certificate and an entry for the private key.
- A Certificate Revocation List entry (CRL) counts just as an entry in the list of trusted certificates.
- A certificate that is used by different services (CPU applications) counts as a single trust list entry.

###### Size of elements for Push function (e.g. certificates)

Max. 4096 bytes

###### Example

You want to grant access to the OPC UA server for up to 62 OPC UA clients and fill the trusted list accordingly.

When you add a Certificate Revocation List entry in the trusted list, you can only trust up to 61 client certificates.

Additional OPC UA certificates can **not** be transferred by loading the hardware configuration to the CPU.

###### Tip

To keep the number of required certificates low, we recommend having the OPC UA client certificates signed by the same CA.

In this case, the CPU as OPC UA server only needs the corresponding CA certificate and CRLs. With these elements, the OPC UA server can then verify all client certificates signed by the CA. This means you do not have to add the individual client certificates to the trusted list.

---

**See also**

[Automated certificate management with GDS (S7-1500, S7-1500T)](#automated-certificate-management-with-gds-s7-1500-s7-1500t)
  
[What you should know about the certificate management (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#what-you-should-know-about-the-certificate-management-s7-1200-s7-1500-s7-1500t)

##### Setting and loading GDS parameters (S7-1500, S7-1500T)

The following describes the settings required for the certificate update.

###### Requirement

- Depending on the application certificate, the corresponding STEP 7/TIA Portal version and S7-1500 CPU firmware version is required.   
  Also see here: [What you should know about the certificate management](Configuring%20devices%20and%20networks.md#what-you-should-know-about-the-certificate-management-s7-1200-s7-1500-s7-1500t)

  - For OPC UA server certificates, for example, TIA Portal from V17 onwards, CPU firmware version V2.9
  - For web server certificates, for example. from TIA Portal V18, CPU firmware version V3.0
- Time/date of the CPU is set (generally applies to certificate-based communication).
- The OPC UA server is enabled.
- The service that the GDS push management uses must be enabled. For example, the web server must be enabled for the transfer of web server certificates.
- At least one endpoint with the "Sign & Encrypt" security policy must be configured for the OPC UA server. The partner must use this endpoint.
- An authenticated user with sufficient function rights is configured  
  The user must have a role that has the function right "Manage certificates".

  This function right, in turn, has the following requirements:

  - **Project protection** must be enabled in the project tree: Project tree: "Security settings > Settings > Project protection".
  - In the "OPC UA > General" area of the CPU settings, the following general user management setting must be enabled: "Enable additional user management via project security settings"

You can find a description of how to set the function rights [here](#users-and-roles-with-opc-ua-function-rights-s7-1500-s7-1500t).

###### Enabling GDS push

When the requirements listed above are met, GDS Push still has to be activated:

1. In the Inspector window (CPU parameters), go to the "OPC UA > Server > General" area.
2. Enable the "Enable Global Discovery Services (Push)" option.

###### Determining the certificate store used

Certificates that are managed using GDS push certificate management are in a different memory area than the certificates that are downloaded via the TIA Portal (STEP 7). When GDS push certificate management is enabled, the services (applications) of the CPU also use certificates from the certificate store whose certificates are managed at runtime.

1. In the CPU settings, navigate to the area "Protection & Security > Certificate management".
2. Select the "Use certificates provided by the certificate management at runtime" option.

   The other option (use certificates configured and downloaded using TIA Portal) uses the certificates that are downloaded to the CPU from the TIA Portal with the configuration in CPU STOP. Certificates or trust lists cannot be updated in this certificate store during runtime.

###### Enabling the diagnostics for the lapsing of certificates

If you wish to be informed in advance about the lapsing of a certificate, select the "Enable system diagnostics event for the certificate lapsing" option in the area "Protection & Security > Certificate management".

In the entry field "Display event when the remaining life of the certificate is ..." enter a percent value.

Effect of these settings:

- At the instant when this value is reached by a certificate, a corresponding system diagnostics message appears till the certificate lapses or is refreshed.
- If the end of the validity period of a certificate has been reached, the CPU generates a corresponding system diagnostics message as well as an entry in the diagnostics buffer and the maintenance LED lights up.

**Example**:  
The certificate transferred via GDS on June 01, 2022 has a validity from June 01, 2022 to June 30, 2022 (30 days). You have input a percent value of 10 for the diagnostics event. On June 27, 2022, when 90% of the period of validity lapses, a corresponding message will appear stating that the certificate that had been transferred will lapse on June 30, 2022.  
Regardless of the configured percentage value, upon lapsing of the period of validity of a certificate, a corresponding message is displayed in any case, an entry is made in the diagnostic buffer, and the maintenance LED lights up.

###### Download to CPU

When downloading the configuration to the CPU, you can delete the certificates that are managed via GDS before the download. When you confirm the deletion, the download is followed by a provisioning phase (see section on commissioning).

When you download the memory card outside of the CPU (card reader), this certificate store is always deleted.

When Global Discovery Services (Push) is activated and no pushed certificates are available, then no separate certificate, trust list or CRL is available for the OPC UA server.

---

**See also**

[GDS commissioning (S7-1500, S7-1500T)](#gds-commissioning-s7-1500-s7-1500t)

##### GDS commissioning (S7-1500, S7-1500T)

Part 12 of the OPC UA specification distinguishes between a provisioning phase and a run time phase during certificate management.

In the provisioning phase, a GDS or OPC UA client provides initial trust lists and CRLs for clients of the OPC UA server. In this phase, the OPC UA server of the CPU accepts all client certificates and lists it is offered – similar to the "Trusted clients" setting for the OPC UA server that all client certificates are accepted during runtime. This is the only way in which a connection to clients not known to the server is possible. For example, clients that the server cannot authenticate using existing certificates or trust lists until it has received the corresponding client certificate or the corresponding trust list.

The provisioning phase is characterized by lower security; therefore, the provisioning phase is indicated by a lit Maintenance LED and a corresponding diagnostics buffer entry (Maintenance demanded).

During the runtime phase, the existing CRLs are updated, for example, and the certificates and trust lists are renewed. Communication is secure in this phase.

###### Requirement

Only authorized users with sufficient function rights can set up a connection in the provisioning phase. The users must have a role with the function right "Manage certificates".

See also [Setting and loading GDS parameters](#setting-and-loading-gds-parameters-s7-1500-s7-1500t).

###### Rules for the provisioning phase

In the provisioning phase, the OPC UA server of the CPU cannot authenticate the OPC UA clients that initiate connection establishment. Therefore, the following rules must be observed:

- Provide a secure environment, for example, access to the CPU is limited to commissioning personnel. Check that the right devices are communicating with one another.
- Limit the time for this phase.

The CPU signals that it is in the provisioning phase by the lit Maintenance LED as well as a corresponding diagnostic buffer entry (Maintenance demanded).

###### Sequence of the provisioning phase

The following provides an outline of the process of the provisioning phase for OPC UA server certificates and trust lists.

The process of the provisioning phase for web server certificates is comparable. In contrast to OPC UA, the GDS client only pushes web server certificates but not trust lists into the corresponding certificate store.

![Sequence of the provisioning phase](images/159085469323_DV_resource.Stream@PNG-en-US.png)

###### Entering the provisioning phase

After startup of the OPC UA server, the CPU automatically enters the provisioning phase when one of the following conditions is met:

- The OPC UA server certificate is the initial self-signed certificate generated by the CPU and has not yet been replaced by a valid server certificate.
- The trust list (list of trustworthy clients) is empty.

The OPC UA server certificate generated by the CPU contains the most important parameters of the OPC UA server and is re-generated, including the private key, after each startup of the OPC UA server following POWER ON - until the valid server certificate is present. For this reason, the OPC UA server may take longer to start up after a POWER ON.

After the hardware configuration is downloaded, the certificate store for certificates that can be updated during runtime is deleted on download or the certificates are retained, depending on the setting. In other words, if GDS is activated and the certificate store has been deleted, the CPU is in the provisioning phase after loading the hardware configuration.

###### Provisioning phase diagnostics

In addition to the lit Maintenance LED, the GDS address model has two nodes that provide information on whether the OPC UA server of the CPU is in the provisioning phase:

![Provisioning phase diagnostics](images/139408788491_DV_resource.Stream@PNG-de-DE.png)

You can only use the two nodes as marked in the figure for diagnostics if the requirements for GDS are met (endpoint security signed & encrypted plus administrator function rights available).

ProvisioningModeEnabled: Indicates that a provisioning phase is supported

ProvisioningModeActive: Indicates that the OPC UA server of the CPU is in the provisioning phase.

###### End of the provisioning phase

The CPU ends the provisioning phase automatically when the following conditions are met:

- The certificate generated and self-signed by the CPU for the provisioning phase has been overwritten by a valid server certificate. This valid server certificate can be a self-signed certificate or a CA-signed certificate.
- The trust list in the CPU is not empty, i.e. client certificates of the OPC UA clients to be trusted or CA certificates for checking the client certificates are available.

If the OPC UA client transfers a CA-signed certificate and also adds the CA certificate to the trust list, the OPC UA server of the CPU can automatically accept all other certificates from OPC UA clients that were signed by the same CA.

###### Request for a valid certificate

From TIA Portal version V18 / S7-1500 CPU version V3.0 onwards, apart from OPC UA server certificates, certificates for other services can also be transferred into the CPU, for example, for the web server.

The corresponding service, for example, the OPC UA server of the CPU, receives a valid certificate in the following steps:

1. A GDS client (OPC UA client) calls the method "CreateSigningRequest" to request a certificate with a Certificate Signing Request (CSR).
2. This CSR must be signed by a Certificate Authority (CA).
3. The signed CSR must then be transferred back to the OPC UA server of the CPU as a certificate.

The OPC UA server of the CPU makes this method available if the client has the required function right "Manage certificates".

The "CreateSigningRequest" method allows for the following variants:

- Certificate update without creating a new key pair (internal CPU keys that are already available are used)
- Certificate update with creation of a new key pair (CPU-internal)

There is also the possibility to generate certificates with externally created key pairs.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Recommended procedure to generate certificates**  Transport of private keys should be avoided; a private key should not leave a device.  We, therefore, recommend the generation of a certificate without creating a new key pair or with the creation of a key pair inside the CPU. |  |

**Create certificate without key pair**

- The "CreateSigningRequest" method returns a Certificate Signing Request (CSR), that is, a file (*.csr) with specific information on the server or on the service, for example, application name and URL.
- Outside of the CPU, this CSR must be validated and signed by a Certificate Authority (CA) and the certificate must be returned.
- The certificate must then be transferred to the CPU ("pushed") using the "UpdateCertificate" method.

The key does not leave the CPU in this scenario.

**Create certificate with internally created key pair**

The procedure is similar to the method explained in the previous section; the only difference is that a key pair is generated in addition to the CSR. You specify in the parameter of the "CreateSigningRequest" method that it is to generate a key pair.

The private key does not leave the CPU in this procedure either.

The generation of a new key pair creates a very heavy load on the CPU. The CPU processes this request over a longer period of time with lower priority in the reserved area for the communication load. The duration of this time period depends on the performance of the CPU.

Because the share of the set communication load is fully utilized during key generation over a longer period of time, set the "Scan cycle load due to communication" share so that the maximum cycle time is not exceeded and sufficient reserves are available. For this, use the web server page "Diagnostics > Runtime information" of the CPU. This page shows information about the current program/communication load and cycle time of your user program. Via a controller, you can get help on the effects of a changed communication load on the cycle time.

**Create certificate with externally created key pair**

The certificate is generated with the help of tools, for example, that can generate additional keys.

Certificate and keys are transferred to the CPU using the "UpdateCertificate" method.

Due to low security, this procedure is not recommended.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Different keys for different target systems**  Always use newly generated keys for a production system. If you simulate and test your project, e.g. with PLCSIM Advanced on your PC, do not under any circumstances use the keys used for the simulation also for a productive system.   Restrict the access to PC-based controllers by setting up appropriate permissions. |  |

##### Address model for the push certificate management (S7-1500, S7-1500T)

The OPC UA specification Part 12 (OPC 10000-12: Discovery, Global Services) defines methods and attributes for OPC UA servers, for example, that enable GDS or OPC UA clients to update certificates and trust lists on the server ("Push certificate management"). These methods and attributes are also included in the address model of the OPC UA server.

The relevant section in the address model of the OPC UA server of the S7-1500 CPU is explained below.

###### Requirement

The following requirements must be met for the relevant methods and attributes to become visible for the GDS push functionality:

- GDS is activated.
- The set security policy supports the integrity and confidentiality of the data through signature and encryption (Sign & Encrypt)
- Access with runtime function right "Manage certificates"

###### Address model for the GDS push functionality

The address model for the GDS push functionality corresponds to the "Information Model for Push Certificate Management" of the OPC UA specification OPC 10000-12: Discovery, Global Services.

You will find the following structure below the "ServerConfiguration" node:

![Address model for the GDS push functionality](images/141533564427_DV_resource.Stream@PNG-de-DE.png)

###### Methods and attributes for access to the address model

The methods and attributes are briefly described below with special features and restrictions of the specific address model of the S7-1500 CPU. The OPC UA specification listed above contains the general description.

You can find a detailed description of the individual methods below this overview table.

| Method / Attribute (Variable) | Description |
| --- | --- |
| CreateSigningRequest | Method for generating a PKCS#10-encoded certificate request signed with the private key of the service (for example, OPC UA server). |
| UpdateCertificate | Method for updating the server certificate for the OPC UA server. |
| ApplyChanges | Method for applying a security-relevant change if the "ApplyChangesRequired" attribute was set when executing a previously executed method.   **Note**   If, as a result of "ApplyChanges", a certificate is changed, the CPU interrupts the connections/sessions that are secured via this certificate.   Background: The basis for the secured connections - the certificate - is no longer valid. |
| GetRejectedList | Method that returns a list of certificates that were rejected by the OPC UA server.  Maximum of 4 entries, retentive. |
| ServerCapabilities | Variable is not supported by the OPC UA server of the S7-1500 CPU. |
| SupportedPrivateKeyFormats | Variable that specifies permitted formats of the private key. For S7-1500 CPUs only "PEM" (String Array) |
| MaxTrustListSize | Variable that specifies the maximum size of the trust list. |
| MulticastDnsEnabled | Variable that specifies whether multicast DNS is supported. For S7-1500 CPUs, the value is "False". |
| CertificateGroups | Object (folder) that organizes all certificate groups supported by the OPC UA server. The certificate groups contain the objects that can be updated dynamically during runtime: For example, one trust list each and one or multiple certificates that are assigned to a service (for example, OPC UA application).   Details on the structure of the CertificateGroups object and the methods and attributes that are available in the object are described in the next section. |

###### CreateSigningRequest

The method has the following parameters:

| Parameter | Data type | Description |
| --- | --- | --- |
| [in] certificateGroupId | NodeId | NodeId of the CertificateGroup object. |
| [in] certificateTypeId | NodeId | Requested certificate type.   List of permitted certificate types is specified by the "CertificateTypes" variable of the certificate group.  For the OPC UA server for example, certificate type "RsaSha256ApplicationCertificateType", for the web server the certificate type "HttpsCertificateType" |
| [in] subjectName | String | Subject Name that is requested in the Certificate Request. If not specified, the current Subject Name of the certificate is used. |
| [in] regeneratePrivateKey | Boolean | True: Server generates a new private key. This key is saves until the UpdateCertificate methods with the matching signed certificate is called.   False: Server uses the available private key. |
| [in] nonce | ByteString | Additional nonce for generating the new private key (see regeneratePrivateKey). Must be at least 32 bytes long. |
| [out] certificateRequest | ByteString | PKCS #10 - DER coded Certificate Request. |

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Bad_InvalidArgument | certificateTypeId, certificateGroupId or subjectName is invalid. |
| Bad_UserAccessDenied | The current user does not have the required function rights. |

###### UpdateCertificate

Applications:

- Generation of certificate with CreateSigningRequest. No private key is available.
- New private key and new certificate were generated outside of the server. Both are updated with UpdateCertificate.
- Certificate generated and signed with the private key of the existing certificate. No private key is available.

| Parameter | Data type | Description |
| --- | --- | --- |
| [in] certificateGroupId | NodeId | NodeId of the CertificateGroup object. |
| [in] certificateTypeId | NodeId | Requested certificate type.   List of permitted certificate types is specified by the "CertificateTypes" variable of the certificate group. |
| [in] certificate | ByteString | DER-coded certificate that replaces the existing certificate. |
| [in] issuerCertificates | ByteString | Issuer certificates |
| [in] privateKeyFormat | String | Format of the private key. Currently only PEM is supported. If the privateKey is not specified: zero or empty string. |
| [in] privateKey | ByteString | Privater key coded as specified in privateKeyFormat. |
| [out] applyChangesRequired | Boolean | Indicates that the "ApplyChanges" method must be called before you use the new certificate. |

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Bad_InvalidArgument | certificateTypeId or certificateGroupId is invalid. |
| Bad_CertificateInvalid | The certificate is invalid or the format is not supported. |
| Bad_NotSupported | The private key is invalid or the format is not supported. |
| Bad_UserAccessDenied | The current user does not have the required function rights. |
| Bad_SecurityChecksFailed | Error occurred when verifying the integrity of the certificate. |

###### Apply Changes

The method has no parameters.

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Bad_UserAccessDenied | The current user does not have the required function rights. |

###### GetRejectedList

The method has the following parameters:

| Parameter | Data type | Description |
| --- | --- | --- |
| [out] certificates | ByteStrings | DER-coded list of rejected certificates. |

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Bad_UserAccessDenied | The current user does not have the required function rights. |

##### CertificateGroups in the address model  (S7-1500, S7-1500T)

Certificates and trust lists for services or applications of the CPU (for example, OPC UA servers) that can be updated during runtime are located in the address model in the "CertificateGroups" object - there is one certificate group each for the various services of the S7-1500 CPU. For the OPC UA server certificate, the certificate group has the name "OPC UA server".

###### CertificateGroup in the address model

The following figure shows the structure of the "CertificateGroups" object below the "ServerConfiguration" node.

![CertificateGroup in the address model](images/158874544011_DV_resource.Stream@PNG-de-DE.png)

You can change the Display Name of the CertificateGroups (for example, of the "OPC UA server" group) in STEP 7 (TIA Portal):

1. In the Inspector window (CPU properties), navigate to the area "Protection & Security > Certificate management".
2. Enable the option "Use certificates provided by the certificate management during runtime" option.
3. Change the group name (DisplayName) of the certificate group in the table below that, the column "Folder for certificate store ...". 1-64 characters in 7-bit ASCII format are permitted. The first column contains the activated service for which certificates can be transferred at runtime and the "ID" column contains a fixed numeric identifier that is used CPU-internally for referencing the certificate.

Here is an example for the display in the area "Certificate management":

![CertificateGroup in the address model](images/159242365963_DV_resource.Stream@PNG-en-US.png)

###### "CertificateTypes" node

The "CertificateTypes" variable specifies the NodeIds of the certificate types that are assigned to the server application.

For the OPC UA server service, for example, the "RsaSha256ApplicationCertificateType" CertificateType is supported, for the web server, it is the "HttpsCertificateTypeCertificateType".

###### "TrustList" node

The node for the trust list object (TrustList file) defines an OPC UA file type (Binary encoded stream) that contains information on the certificates and CRLs that can be read and updated in the "pki store\trusted/issuer" directory of the Memory Card. This node provides methods and attributes that make reading and updating possible.

The node is an instance of the OPC UA data type "TrustListDataType" with the following structure:

| Parameter | Data type | Description |
| --- | --- | --- |
| specifiedLists | TrustListsMasks | Bit mask that shows which lists contain information. |
| trustedCertificates | ByteStrings | List of the trusted application certificates and CA certificates. |
| trustedCrls | ByteStrings | CRLs for the certificates in the "trustedCertificates" list. |
| issuerCertificates | ByteStrings | List of the CA certificates that are necessary for validating the CA-signed certificates. |
| issuerCrls | ByteStrings | CRLs of the CA certificates in the "issuerCertificates" list. |

###### Structure of the "TrustList" node

The "TrustList" node has the following structure:

![Structure of the "TrustList" node](images/141533615883_DV_resource.Stream@PNG-de-DE.png)

###### Methods and attributes for the "TrustList" node

Below is a description of the nodes under "TrustList" that supplement the methods of the Object Type "FileType". The TrustList Type is derived from FileType (see OPC 10000-5: OPC Unified Architecture, Part 5: Information Model).

| Method / Attribute (Variable) | Description |
| --- | --- |
| LastUpdateTime | Variable that shows the time of the last update. |
| OpenWithMasks | Method that permits a client to only read a part of the TrustList. |
| CloseAndUpdate | Method for closing the TrustList file and applying the changes. |
| AddCertificate | Method for adding a single certificate to the TrustList. |
| RemoveCertificate | Method for removing a single certificate from the TrustList. |

###### Description of the methods

The description of the methods with their result codes, attributes and types of the TrustList object is available in the OPC UA specification Part 12, Discovery and Global Services.

---

**See also**

[Setting and loading GDS parameters (S7-1500, S7-1500T)](#setting-and-loading-gds-parameters-s7-1500-s7-1500t)

### Using diagnostics options (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Diagnostics of the OPC UA server (S7-1500, S7-1500T)](#diagnostics-of-the-opc-ua-server-s7-1500-s7-1500t)
- [Running diagnostics for OPC UA servers in the program (S7-1200, S7-1500, S7-1500T)](#running-diagnostics-for-opc-ua-servers-in-the-program-s7-1200-s7-1500-s7-1500t)
- [Server state transition diagnostics (S7-1500, S7-1500T)](#server-state-transition-diagnostics-s7-1500-s7-1500t)
- [Session state transition diagnostics (S7-1500, S7-1500T)](#session-state-transition-diagnostics-s7-1500-s7-1500t)
- [Check of security policy failed (S7-1500, S7-1500T)](#check-of-security-policy-failed-s7-1500-s7-1500t)
- [Requests of a remote OPC UA client failed (S7-1500, S7-1500T)](#requests-of-a-remote-opc-ua-client-failed-s7-1500-s7-1500t)
- [Subscription diagnostics (S7-1500, S7-1500T)](#subscription-diagnostics-s7-1500-s7-1500t)
- [Summarizing diagnostics (S7-1500, S7-1500T)](#summarizing-diagnostics-s7-1500-s7-1500t)

#### Diagnostics of the OPC UA server (S7-1500, S7-1500T)

##### Online diagnostics of the OPC UA server

The CPU OPC UA server can be diagnosed online with standard OPC UA clients, such as UaExpert.

The diagnostic information is subdivided into the following areas:

- Server Diagnostics
- Sessions Diagnostics
- Subscriptions Diagnostics

In the address space of the server, for example, the following nodes are available with diagnostic information:

- **ServerDiagnosticsSummary**: Server diagnostics summary

  - CurrentSessionCount: Number of active sessions
  - SecurityRejectedSessionCount: Number of sessions rejected due to mismatching end point security settings between client and server
- **SessionsDiagnosticsSummary**: Session diagnostics summary

  - ActualSessionTimeout: Set time that a session lasts, e.g. in the event of disconnection
- **SubscriptionsDiagnosticsArray**: ARRAY with one element per subscription for each session

![Online diagnostics of the OPC UA server](images/114678874635_DV_resource.Stream@PNG-de-DE.png)

The SessionsDiagnosticsSummary node also shows the properties of the client application accessing the server within the session.

![Online diagnostics of the OPC UA server](images/114678882955_DV_resource.Stream@PNG-de-DE.png)

##### Diagnostics of the connection between client and server (S7-1500)

To diagnose the status of the connection during program runtime in the client, use the following instruction:

OPC_UA_ConnectionGetStatus: Read connection status.

---

**See also**

[Diagnosing the OPC UA server with OPC_UA_ReadList (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#diagnosing-the-opc-ua-server-with-opc_ua_readlist-s7-1500)

#### Running diagnostics for OPC UA servers in the program (S7-1200, S7-1500, S7-1500T)

From STEP 7 (TIA Portal) V18 onwards, you can access nodes in the OPC UA address space of an S7-1500 CPU (firmware version V3.0 onwards) to evaluate the contents for diagnostic purposes in the program.

##### Functional principle

In the local address space of the CPU, there are numerous nodes where the OPC UA server of the CPU stores data and states. The "OPC_UA_ReadList" instruction enables you to access this information and evaluate it in the user program.

Example: "ServerState" is a node in the address space of the CPU that contains values for the server state or for state transitions (Running, Shutdown, Failed, etc.).

You do not use the instruction as a client instruction, but instead as an instruction for reading nodes of the own local OPC UA address space. In this regard, special rules and requirements apply to this application case.

Note that the instruction "OPC_UA_ReadList" also generates communication load when accessing the local address space of the OPC UA server. If necessary, lower the frequency of the queries to reduce the communication load.

##### Additional information

You can find additional information on calling the "OPC_UA_Readlist" instruction for diagnostic purposes here: [Diagnosing the OPC UA server with OPC_UA_ReadList](Communication%20%28S7-1200%2C%20S7-1500%29.md#diagnosing-the-opc-ua-server-with-opc_ua_readlist-s7-1500)

#### Server state transition diagnostics (S7-1500, S7-1500T)

##### Information on the server state

S7-1500 CPUs as of firmware version V2.8 and S7-1200 CPUs as of firmware version V4.5 are able to create an entry in the diagnostics buffer upon state changes of the OPC UA server.

The diagnostic buffer displays the new state.

The cause of the state change is also displayed, such as download to the CPU, POWER OFF - POWER ON transition, user program instruction or service request from a partner (client).

##### Requirement

The "Change of OPC UA server status" option is selected (OPC UA > Server > Diagnostics) in the OPC UA properties of the CPU.

> **Note**
>
> If this option is selected, the CPU also automatically enters the lowest set security policy into the diagnostic buffer after startup.

##### Examples

If the OPC UA server of the CPU shuts down due to a download process and then starts with a valid new configuration, the diagnostic buffer shows new server state, e.g. Shutdown => Starting => Running.

If the OPC UA server shuts down due to a download process and the server cannot start because the type dictionary is too large, the diagnostic buffer finally shows the state "Failed" (Shutdown => Starting => Failed).

##### Server states and state transitions

![Server states and state transitions](images/123862578187_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ①, ④ | POWER ON or Load in RUN, if OPC UA relevant data could be affected. |
| ② | Loading the hardware configuration with deactivated OPC UA server. The server remains shut down.  Loading the hardware configuration with activated OPC UA server and faulty OPC UA data (for example, too many structures with the result that the type dictionary becomes too large). In this case, the server cannot start (see ③). |
| ③ | OPC UA server cannot start due, for example, to faulty configuration. |

##### Description of the server states

The individual states that the OPC UA server can assume are explained below.

| Server states | Explanation |
| --- | --- |
| Shutdown | Initial status   - After POWER ON - After loading the hardware configuration with activated or deactivated OPC UA server. - After loading OPC UA relevant data |
| Starting | OPC UA address space in server is initialized. |
| Running | OPC UA server running (normal productive state for OPC UA server). |
| Failed | Error state. OPC UA server cannot start due, for example, to faulty configuration. |

#### Session state transition diagnostics (S7-1500, S7-1500T)

##### Information on the session state

CPUs are able to create an entry in the diagnostics buffer for state changes of an OPC UA session.

The diagnostic buffer displays the new state. The corresponding session ID is also displayed.

##### Requirement

The "Change of session states" option (OPC UA > Server > Diagnostics) is selected in the OPC UA properties of the CPU.

##### Example

A client transmits incorrect authentication data (for example, incorrect password) when a connection is established. The new state of the "ActivationFailed" session is entered with the corresponding session ID in the diagnostic buffer.

##### Session states and state transitions

![Session states and state transitions](images/126635795595_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Client connects to server, login with correct authentication data (correct credentials). |
| ② | Client closes connection correctly. |
| ③ | Client no longer sends messages; session ends with timeout. |
| ④ | Client connects to server, login with incorrect authentication data. |

#### Check of security policy failed (S7-1500, S7-1500T)

If the CPU diagnostics detects a security event during the OPC UA communication, it can enter it in the diagnostic buffer.

##### Requirements

- S7-1200 CPUs as of FW version V4.5 or S7-1500 CPUs as of FW version 2.8
- The option "Check of security policy failed" is activated (properties of the CPU > OPC UA > Server > Diagnostics)

##### Security events detected in diagnostics

CPUs perform diagnostics on the following OPC UA-relevant security events:

- Client-certificate is invalid (for example, syntactically or semantically incorrect, incorrect signature, current date is not in the validity period)
- User name/password login failed (deactivated or incorrect data)
- Client wants to use a specific security policy or a specific message security mode; the server does not support the security policy or the requested security mode.
- Client does not establish connection according to specification (OPC UA Spec) (for example, unexpected SecureChannelID/SessionID/client Nonce)

##### Example

If an attempt is made to compromise communications (for example, by session hijacking, man-in-the-middle attacks etc.), the server detects this via analysis.

#### Requests of a remote OPC UA client failed (S7-1500, S7-1500T)

CPUs are able to create an entry in the diagnostics buffer for the following events:

- Bad client requests (incorrect use)
- CPU-specific limits of the OPC UA server were exceeded
- Insufficient memory
- Service error occurred

##### Requirements

- S7-1200 CPUs as of FW version V4.5 or S7-1500 CPUs as of FW version 2.8
- The option "Requests of a remote OPC UA client failed" is activated (properties of the CPU > OPC UA > Server > Diagnostics)

##### Example of a faulty client request

For example, there is an incorrect request when a client addresses a node (tag) that does not exist or if a resource is requested that does not exist.

In this case, the corresponding service that caused the fault is entered in the diagnostic buffer and the corresponding session ID is also entered.

##### Example of limit violations

If a service request exceeds a CPU-specific limit, for example, number of sessions, number of monitored items, number of subscriptions, etc., this diagnostics is entered in the diagnostics buffer. Together with the message, it is indicated which limit has been violated.

Exception: If you summarize diagnostics and the message occurs frequently, the limit causing the error is not entered. You receive general information that the supported configuration limit has been violated.

"Out-of-memory" situations (insufficient memory) are a special case of exceeded limits. This diagnostic is also only entered in the diagnostics buffer when you have activated the "Requests of a remote OPC UA client failed" option.

##### Also activate the option "Summarize diagnostics in case of high message volume"

When you activate the "Requests of a remote OPC UA client failed" option, you should also activate the "Summarize diagnostics in case of high message volume" option. This prevents the numerous identical diagnostic alarms from "flooding" the diagnostics buffer.

##### Service fault

If a service itself fails, the server returns a ServiceFault. In this case, the status code (Bad...) and the according session ID are entered in the diagnostics buffer.

##### Possible entries for the service that is causing the error

Depending on the client application used, requests to the server can be triggered differently from the user's viewpoint, for example, by an online tool with a graphical user interface or by instructions in a client's program.

With its service-oriented architecture, OPC UA follows a request-response paradigm, therefore the respective client application converts the requests into the service requests defined in OPC UA.

The names of these services are defined and grouped according to their use, see also opcfoundation.org.

In the case of an incorrect use, you can find precisely these names of the services, together with the corresponding session ID, in the diagnostic buffer as the service that caused the error.

The services available with OPC UA are listed below.

**Discovery Service Set**

FindServers

GetEndpoints

**Session Service Set**

CreateSession

ActivateSession

CloseSession

Cancel

**View Service Set**

Browse

BrowseNext

TranslateBrowsePathsToNodeIds

RegisterNodes

UnregisterNodes

**Attribute Service Set**

Write

Read

**Method Service Set**

Call

**Monitored Item Service Set**

CreateMonitoredItems

ModifyMonitoredItems

DeleteMonitoredItems

SetMonitoringMode

SetTriggering

**Subscription Service Set**

CreateSubscription

ModifySubscription

DeleteSubscriptions

Publish

Republish

SetPublishingMode

#### Subscription diagnostics (S7-1500, S7-1500T)

##### Information about a subscription

CPUs are able to create an entry in the diagnostics buffer for state changes of a subscription.

The diagnostic buffer displays the new state; exception: "KeepAlive".

##### Requirement

In the OPC UA properties of the CPU, the option "Subscriptions: Change of status" (OPC UA > Server > Diagnostics) is selected.

##### Example

An OPC UA client is connected to an S7-1200/1500 CPU as OPC UA server and generates a subscription in the server.

The diagnostic options for subscriptions are selected in the OPC UA properties of the CPU.

The "Creating" and "Normal" states are entered one after the other with the corresponding subscription ID in the diagnostic buffer.

##### Subscription states and state transitions

![Subscription states and state transitions](images/123912475275_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Subscription is generated and is then active. |
| ② | Status change is not entered in the diagnostic buffer because too many entries may be made in the diagnostic buffer depending on the amount of data. |
| ③ | See explanation in table for "Late"; for example, no requests to send from client. |
| ④ | Maximum KeepAlive value reached. |
| ⑤ | See explanation in table for "TimedOut". |
| ⑥ | Maximum lifetime of subscription reached. |
| ⑦ | Client has deleted subscription. |

##### Description of the subscription states

A subscription in the OPC UA server can have the following states:

| Status | Meaning |
| --- | --- |
| Creating | Client has requested a subscription in the server; the server creates the subscription. |
| Normal | Subscription is created in the server and active. |
| Closed | Client has deleted the subscription. |
| KeepAlive | Status if the monitored items do not change over a long period of time. These state transitions are not entered in the diagnostic buffer. |
| Late | Client has generated a subscription with minimal sampling and publishing intervals. The amount of monitored items is not transmitted to the client during this time.   Client no longer transmits requests to send (for example, due to failure). |
| TimedOut | The client has requested a subscription.   The server can only honor the subscription (send Publish Response) when there is a sufficient number of send requests (Publish Requests) from the client.   When the client stops sending subscription requests, the subscription enters the "TimedOut" state after a certain time. |

##### Subscription: Error in the sampling times

As of firmware V2.5 of the SIMATIC S7-1500 CPU, the OPC UA server can transmit the status code "GoodOverload" when using subscriptions, if an overload of the CPU occurs when sampling the items.

The OPC UA server can also enter this event into the diagnostics buffer.

##### Requirement

In the OPC UA properties of the CPU, the option "Subscriptions: Sampling time errors" (OPC UA > Server > Diagnostics) is selected.

##### Error-free subscription

In the case of an OPC UA subscription to various items (such as tags), the OPC UA server must check the items for value changes at specified intervals (sampling interval). This check, referred to as "sampling", requires some time, which depends on the number and the data type of the items. After the sampling is completed and a publishing request has been received, the server sends the elements to the client.

![Error-free subscription](images/123912450059_DV_resource.Stream@PNG-en-US.png)

##### Subscription with error

If there are too many elements in the queue, there may be an overload of the communication stack. The CPU cannot check all elements in the given sampling interval and must therefore skip the next sampling job.

In this case, the CPU sends the status code "GoodOverload" (0x002F0000) per element, even though the elements were not checked. The meaning of the status code according to IEC 61131-3 is as follows: "Sampling has slowed down due to resource limitations".

![Subscription with error](images/123912424843_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Sampling job is skipped |

See also [FAQ 109763090](https://support.industry.siemens.com/cs/ww/en/view/109763090).

---

**See also**

[Settings of the server for subscriptions (S7-1500, S7-1500T)](#settings-of-the-server-for-subscriptions-s7-1500-s7-1500t)

#### Summarizing diagnostics (S7-1500, S7-1500T)

To prevent the diagnostic buffer being "swamped" by large numbers of identical OPC UA diagnostics, as of STEP 7 V16 you can set parameters so that these diagnostics are entered in the diagnostics buffer as group alarm. Per interval (monitoring time), the CPU then only generates one group alarm per OPC UA diagnostics.

The following sections describe which diagnostics the CPU groups together and how the process runs with a high message volume.

##### Requirement

The "Summarize diagnostics in case of high message volume" option is activated in the OPC UA properties of the CPU (OPC UA > Server > Diagnostics, "Summarize diagnostics" area).

##### Example

An OPC UA client repeatedly "overstrains" an S7-1200/1500 CPU as OPC UA server with a sampling rate that the server cannot handle (overload).

The "Summarize diagnostics in case of high message volume" setting is activated.

A message appears in the diagnostics buffer for this diagnostic option. It states that the sampling rate cannot be reached; followed by the number of these events within the configured interval.

##### OPC UA diagnostics that can be summarized

The diagnostics listed below each form their own groups (type). Diagnostic events from the same group are combined using the setting "Summarize diagnostics in case of high message volume":

- Incorrect use of an OPC UA service
- OPC UA Service error
- Subscription status has changed
- Sampling rate could not be achieved (subscriptions, overload)
- OPC UA security check failed
- Configuration limit of the OPC UA server violated

##### Principle of operation

The CPU enters the first three events of an event type in the diagnostics buffer. It then ignores all subsequent diagnostics of this group.

At the end of the monitoring time (interval), the CPU generates a group alarm in which it enters the diagnostics and the frequency of this diagnostics during the elapsed interval. If these diagnostics also occur in the intervals that follow, the CPU only generates one group alarm per subsequent interval.

A diagnostic surge leaves the following pattern in the diagnostics buffer: Three individual messages followed by a series of group alarms. This series can consist of two, three or more group alarms depending on the selected monitoring time and duration of the diagnostic surge.

![Principle of operation](images/125113859467_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Diagnostic results of a group (of a type), for example "Sampling rate could not be reached". |
| ② | Interval (monitoring time): When a diagnostic event occurs the first time (or reoccurs), the monitoring time is started (or restarted). |
| ③ | Single alarms: The first three diagnostic events from the same group are entered in the diagnostics buffer immediately. Starting with the fourth diagnostic event, the CPU generates only group alarms. If a diagnostic event of this group occurs after a pause of at least one interval, the CPU enters a single alarm in the diagnostics buffer and restarts the monitoring time. |
| ④ | Group alarms: After three diagnostic events, the CPU only generates a group alarm as a summary of all additional diagnostic events in this interval. If these diagnostic events also occur in the intervals that follow, the CPU only generates one group alarm per subsequent interval. |

### Using the S7-1200 CPU as an OPC UA server (S7-1200)

This section contains information on the following topics:

- [Interesting information about the OPC UA server of the S7-1200 CPUs (S7-1200)](#interesting-information-about-the-opc-ua-server-of-the-s7-1200-cpus-s7-1200)
- [Configuring access to PLC tags (S7-1200)](#configuring-access-to-plc-tags-s7-1200)
- [Configuring the OPC UA server (S7-1200)](#configuring-the-opc-ua-server-s7-1200)
- [OPC UA server interface configuration (S7-1200)](#opc-ua-server-interface-configuration-s7-1200)
- [Providing methods on the OPC UA server (S7-1200)](#providing-methods-on-the-opc-ua-server-s7-1200)

#### Interesting information about the OPC UA server of the S7-1200 CPUs (S7-1200)

This section contains information on the following topics:

- [The OPC UA server of the S7-1200 CPUs (S7-1200)](#the-opc-ua-server-of-the-s7-1200-cpus-s7-1200)
- [End points of the OPC UA servers (S7-1200)](#end-points-of-the-opc-ua-servers-s7-1200)
- [Mapping of CPU data types to OPC UA data types (S7-1200)](#mapping-of-cpu-data-types-to-opc-ua-data-types-s7-1200)
- [Behavior of the OPC UA server in operation (S7-1200)](#behavior-of-the-opc-ua-server-in-operation-s7-1200)

##### The OPC UA server of the S7-1200 CPUs (S7-1200)

The S7-1200 CPUs as of firmware V4.4 are equipped with an OPC UA server. This also includes the versions S7-1200FC in addition to the standard S7-1200C CPUs.

Convention: "S7-1200 CPU" also includes the above-mentioned CPU variants.

###### Basics on the OPC UA server of the S7-1200 CPU

Access to the OPC UA server of the CPU is possible over the PROFINET interfaces of the S7-1200 CPU.

For access by clients, the server saves the enabled PLC tags and other information in the form of nodes (see [Configuring access to PLC tags](#configuring-access-to-plc-tags-s7-1200)). These nodes are interconnected and form a network. OPC UA defines access points to this network (well-known nodes) that enable navigation to subordinate nodes.

###### Node classes and address space

OPC UA servers provide information in the form of nodes. A node can be, for example, an object, a tag, or a property.

A network of nodes is also called an address space. Starting from the root, all nodes can be reached in the address space.

The nodes are linked over references, for example, the reference "HasComponent", which represents a hierarchical relationship between a node and its subordinate nodes. With their references, the nodes form a network that can, for example, take the form of a tree.

If you want to publish PLC tags in the address space of the OPC UA server of the S7-1200 CPU, use either a Companion Specification with mapping to the corresponding tags or create a server interface and assign the PLC tags to the OPC UA nodes using drag-and-drop operation.

The example below shows the address space of the OPC UA server of an S7-1200 CPU (extract from the "UaExpert" from Unified Automation).

![Example of the address space of the OPC UA server of an S7-1200 CPU](images/131659661963_DV_resource.Stream@PNG-de-DE.png)

Example of the address space of the OPC UA server of an S7-1200 CPU

The "MyValue" tag is selected in the figure above.

This tag is located below the "Memory" server interface node.

---

**See also**

[Access to OPC UA applications (S7-1200, S7-1500, S7-1500T)](#access-to-opc-ua-applications-s7-1200-s7-1500-s7-1500t)
  
[Documentation for S7-1200 automation system](https://support.industry.siemens.com/cs/ww/en/view/109772940)
  
[What you need to know about OPC UA (S7-1200, S7-1500, S7-1500T)](#what-you-need-to-know-about-opc-ua-s7-1200-s7-1500-s7-1500t)

##### End points of the OPC UA servers (S7-1200)

The end points of the OPC UA servers define the security level for a connection. Depending on the application or desired security level, you must configure the connection accordingly at the end point.

###### Different security settings

Before establishing a secure connection, OPC UA clients ask the server with which security settings connections are possible. The server returns a list with all the security settings (end points) that the server allows.

###### Structure of end points

End points consist of the following components:

- Identifier for OPC: "opc.tcp"
- IP address: 192.168.178.151 (in the example)
- Port number for OPC UA: 4840 (standard port)

  The port number can be configured.
- Security setting for messages (Message Security Mode): None, Sign, SignAndEncrypt.
- Encryption and hash procedures (Security Policy): None, Basic128Rsa15, Basic256, Basic256Sha256 (in the example).

The following figure shows the "UA Sample Client" of the OPC Foundation.

The client has established a secure connection to the OPC UA server to the end point "opc.tcp://192.168.178.151:4840 - [SignAndEncrypt: Basic256Sha256:Binary]". The security settings "SignAndEncrypt:Basic256Sha256" are contained in the end point.

> **Note**
>
> **Select an end point with a security policy that is as strict as possible**
>
> - For the end points at the OPC UA server, activate only the most secure ones which a client still supports.
> - Disable the less strict security policy at the OPC UA server.
>
> **Establishing a connection to the server (client side)**
>
> - To establish a connection to the server, select the appropriate security policy for the application.
> - Use a Sha256 certificate for the most secure end points (Basic256Sha256) of the S7-1200 CPU OPC UA server.

![Structure of end points](images/128184168203_DV_resource.Stream@PNG-de-DE.png)

A connection to a server end point is only established if the OPC UA client complies with the security policies of that end point.

The "Handling client and server certificates" section describes how to configure the security policy in the TIA Portal.

###### Information provided by the OPC UA server

OPC UA servers provide a wide range of information:

- The values of PLC tags and DB components which clients may access.
- The data types of these PLC tags and DB components.  
  You can find the data types supported by the OPC UA server of the S7-1200 under [Mapping of CPU data types to OPC UA data types](#mapping-of-cpu-data-types-to-opc-ua-data-types-s7-1200).
- Information on the OPC UA server itself and on the CPU.

This gives clients an overview and allows them to read out specific information. Previous knowledge of the PLC program and the CPU data is not required. You do not need to ask the developer of the PLC program when PLC tags are to be read. All necessary information is stored on the server itself (for example, the data types of the PLC tags).

###### Display of the information of the OPC UA server

You have the following options:

- Online: You have all the available information displayed during the runtime of the OPC UA server. To do so, navigate (browse) the address space of the server.
- Offline: You export your configured server interfaces as XML files that are based on the XML schemes of the OPC Foundation.
- Offline with the Openness API: In your program, you use the API (Application Programming Interface) of the TIA Portal to access the function for exporting all PLC tags that can be read by OPC UA. This requires .NET Framework 4.0; see TIA Portal Openness, [Automating SIMATIC projects with scripts](https://support.industry.siemens.com/cs/ww/en/view/109477163).
- If you already know the syntax and the PLC program, you can access the OPC UA server without first researching the information.

---

**See also**

[Documentation for S7-1200 automation system](https://support.industry.siemens.com/cs/ww/en/ps/13685/man)

##### Mapping of CPU data types to OPC UA data types (S7-1200)

S7-1200 CPUs as of firmware version V4.4 have an OPC UA server. You can configure OPC UA server interfaces for this server.

The following mapping of the S7-1200 data types to OPC UA data types applies:

| SIMATIC data type | OPC UA data type |
| --- | --- |
| BOOL | Boolean |
| SINT | SByte |
| USINT | Byte |
| INT | Int16 |
| UINT | UInt16 |
| DINT | Int32 |
| UDINT | UInt32 |
| REAL | Float |
| LREAL | Double |
| WSTRING  (UCS-2; Universal Coded Character Set) | String |
| DWORD | StatusCode |

The OPC UA server of the S7-1200 supports reading and writing of the listed simple data types.

As of firmware V4.5, S7-1200 CPUs support server methods as well as structured data types (structures and arrays).

Unions are not supported by S7-1200 CPUs.

##### Behavior of the OPC UA server in operation (S7-1200)

###### OPC UA server in operation

The OPC UA server of the S7-1200 CPU starts when you activate the server and download the project to the CPU.

**Behavior in stop mode of CPU**

An activated OPC UA server remains in operation even if the CPU switches to "STOP". The OPC UA server continues to respond to requests from OPC UA clients.

Server response in detail:

- If you request the values of PLC tags, you will get the values that were current before the CPU switched to or was set to "STOP".
- If you write values to the OPC UA server, the OPC UA server will accept those values.

  However, the CPU will not process the values because the user program is not executed in "STOP" mode.

  An OPC UA client can nonetheless read the values written at STOP from the OPC UA server of the CPU.

###### Loading of the CPU with running OPC UA server

If you load a CPU with running OPC UA server, you may need to stop and restart the server depending on the loaded objects. In this case, active connections are interrupted and must be re-established once the server restarts.

The duration of the restart depends mainly on the following parameters:

- The scope of the data structure
- The number of variables visible in the OPC UA address space
- The setting for downward compatible data type definition according to OPC UA specification to V1.03 (TypeDictionary enabled)
- The settings for the communication load and minimum cycle time

With CPU FW versions older than V4.5, the OPC UA server was stopped at each download to the CPU and then restarted.

As of FW version V4.5, the behavior of the OPC UA server has been optimized as follows:

- When objects are downloaded in STOP operating state of the CPU, the OPC UA server still always stops and then restarts. STEP 7 does not show a warning in this case.
- When objects are downloaded in RUN operating state of the CPU, the OPC UA server only stops if the downloaded objects are, or could be, OPC UA-relevant. The OPC UA server restarts after re-initialization due to the modified OPC UA data.

  Before OPC-UA-relevant objects are loaded into the CPU and stop the OPC UA server, STEP 7 displays a warning in the preview dialog for loading. You can then decide whether a server restart is compatible for the running process or whether you want to cancel the download. These warnings are only displayed when the OPC UA server is running. If the OPC UA server is not enabled, modified OPC UA data have no influence on the download process.

**Examples**

- You only want to add another code block to the program.   
  Neither data blocks nor inputs, outputs, flags, times or counters are affected.  
  Reaction during loading: A running OPC UA server is not interrupted.
- You want to load a new data module and you have flagged the data module as non-OPC-UA-relevant:  
  Reaction during loading: A running OPC UA server is not interrupted.
- You want to overwrite a data module.  
  Reaction during loading: A warning appears that the server will be restarted.  
  Background: STEP 7 cannot determine whether the changes refer to OPC-UA-relevant data or not.

###### Reading out the CPU operating mode over OPC UA server

The OPC UA server allows you to read out the CPU mode, see figure below:

![Reading out the CPU operating mode over OPC UA server](images/132239653003_DV_resource.Stream@PNG-de-DE.png)

In addition to the operating mode of the CPU you can, for example, read out information in the manual (DeviceManual) or firmware version (HardwareRevision).

#### Configuring access to PLC tags (S7-1200)

This section contains information on the following topics:

- [Managing write and read rights (S7-1200)](#managing-write-and-read-rights-s7-1200)
- [Coordinating write and read rights for CPU tags (S7-1200)](#coordinating-write-and-read-rights-for-cpu-tags-s7-1200)
- [MinimumSamplingInterval attribute for tags (S7-1200)](#minimumsamplinginterval-attribute-for-tags-s7-1200)

##### Managing write and read rights (S7-1200)

###### Enabling PLC tags and DB tags for OPC UA

OPC UA clients can have read and write access to PLC tags and DB tags if the tags are enabled for OPC UA (default setting).

For enabled tags, the check boxes "Accessible from HMI/OPC UA", "Writable from HMI/OPC UA" and "Visible in HMI engineering" are activated.

![Enabling PLC tags and DB tags for OPC UA](images/127069022475_DV_resource.Stream@PNG-en-US.png)

You can change the default setting in the settings of the TIA Portal: Command "Settings > PLC programming > General" in "Options" menu. You will find the corresponding options in the "Block interface/data block elements" area.

In addition, with S7-1200 CPUs you must make the PLC tags known as OPC UA nodes for OPC UA clients via a server interface ("OPC UA communication" area in the project tree). Alternatively, you can use a Companion Specification with mapping to PLC tags.

###### Removing write rights

If you want to write-protect a tag, deselect the "Writable from HMI/OPC UA" option for that tag. This removes the write right for the OPC UA clients and HMI devices.

Result: Only read access by OPC UA clients and HMI devices is possible. OPC UA clients cannot assign values to this tag and therefore cannot influence execution of the S7 program.

For S7-1200 CPUs it is sufficient to remove the mapping of the corresponding PLC tags from the server interface.

###### Removing write and read rights

To write-protect and read-protect a tag, disable the "Accessible from HMI/OPC UA" option for that tag (checkbox not selected). This makes the OPC UA server remove the tag from its address space. OPC UA clients can no longer see this CPU tag.

Result: OPC UA clients and HMI devices can neither read nor write the tag.

###### Visible in HMI engineering

The option "Visible in HMI Engineering" applies to Siemens engineering tools. If you disable the option "Visible in HMI Engineering" (check mark not set), you can no longer configure the tag in WinCC (TIA Portal).

The option does not have any effect on OPC UA.

###### Rules

- Only allow read access to PLC tags and tags of data blocks in STEP 7 if this is necessary for communication with other systems (controllers, embedded systems or MES).

  You should not enable other PLC tags.
- Only allow write access over OPC UA if write rights are genuinely necessary for specific PLC tags and tags of data blocks.
- If you have reset the "Accessible from HMI/OPC UA" option for all elements of a data block, the data block for an OPC UA client is no longer visible in the address space of the OPC UA server of the S7-1200 CPU.
- You can also prevent access to an entire data block centrally, as with S7-1500 CPUs (see [Managing write and read rights for a complete DB](#managing-write-and-read-rights-for-a-complete-db-s7-1500-s7-1500t)). This setting "overrules" the settings for the components in the DB editor.

##### Coordinating write and read rights for CPU tags (S7-1200)

###### Definition of write and read rights in the information model (OPC UA XML)

In the OPC UA information model, the attribute "AccessLevel" regulates access to tags.

AccessLevel is defined bit by bit:

Bit 0 = CurrentRead and Bit 1 = CurrentWrite. The meaning of the bit combinations is as follows:

- AccessLevel = 0: no access
- AccessLevel = 1: read only
- AccessLevel = 2: write only
- AccessLevel = 3: read+write

**Example of the assignment of write and read rights (read+write)**

![Definition of write and read rights in the information model (OPC UA XML)](images/105751164043_DV_resource.Stream@PNG-de-DE.png)

###### Definition of write and read rights in STEP 7

When you define tags, you specify the access rights using the properties "Accessible from HMI/OPC UA" and "Writable from HMI/OPC UA".

You can find a description of the interaction between write and read rights [here](#read-and-write-access-rights-for-cpu-variables-and-opc-ua-tags-s7-1500-s7-1500t).

##### MinimumSamplingInterval attribute for tags (S7-1200)

###### Sampling of tags

In addition to "Value", "DataType" and "AccessLevel", you can also set the "MinimumSamplingInterval" attribute for a tag in the XML file that represents the server address space.

The attribute specifies how fast the server can sample the tag value.

The value can be set in a range from 100 ms to 10 s. The default value is 1000 ms.

The sampling frequency is limited to the sampling interval defined by the OPC UA client.

The OPC UA server of the S7-1200 CPU handles the values for MinimumSamplingInterval as follows:

- Negative values and values greater than 4294967 are set to -1. This means: The minimum sampling rate is indeterminate. The server does not specify how fast the tag value is sampled.
- Decimal numbers are rounded to three decimal places.

#### Configuring the OPC UA server (S7-1200)

This section contains information on the following topics:

- [Enabling the OPC UA server (S7-1200)](#enabling-the-opc-ua-server-s7-1200)
- [Access to the OPC UA server (S7-1200)](#access-to-the-opc-ua-server-s7-1200)
- [Additional OPC UA server settings (S7-1200)](#additional-opc-ua-server-settings-s7-1200)
- [License for OPC UA (S7-1200)](#license-for-opc-ua-s7-1200)

##### Enabling the OPC UA server (S7-1200)

###### Requirement

- If you use **certificates** for secured communication, e.g. HTTPS, Secure OUC, OPC UA, make sure that the modules involved have the **current time of day and the current date**. Otherwise, the modules evaluate the used certificates as invalid and secure communication does not work.
- You have acquired a runtime license for the operation of the OPC UA functions.

###### Commissioning an OPC UA server

By default, the OPC UA server of the CPU is not enabled for reasons of security: OPC UA clients have neither write nor read access to the S7-1200 CPU.

Follow these steps to activate the OPC UA server of the CPU:

1. Select the CPU. Click on the CPU symbol (for example in the network view).
2. Click "OPC UA > Server" in the properties of the CPU.
3. Activate the OPC UA server of the CPU.
4. Confirm the security notes.
5. Go to the CPU properties, select "Runtime licenses" and set the runtime license acquired for the OPC UA server.
6. Compile the project.
7. Download the project to the CPU.

   The OPC UA server of CPU now starts.

###### Settings remain stored

If you have already enabled the server and assigned the parameters, those parameter assignments are not lost if the server is then disabled. The settings are saved as before and are available when you enable the server again.

###### Application name

The application name is the name of the OPC UA application and applies in principle to the server and the client of a CPU. S7-1200 CPUs currently have only one OPC UA server. The name is displayed under "OPC UA > General":

- The default for the application name is: "SIMATIC.S7-1200.OPC-UA.Application:PLC_1".
- The default consists of "SIMATIC.S7-1200.OPC-UA.Application:" and the name of the CPU selected under "General > Product information > Name", in this case "PLC_1".
- The OPC UA server uses this application name to identify itself to a communication partner (OPC UA client), for example, when an OPC UA client uses the discovery service to detect accessible servers.
- The displayed application name uses the OPC UA client of the CPU when connecting to an OPC UA Server. This means that the CPU enters this application name automatically as "ApplicationName" for the instruction "OPC_UA_Connect" (tag of type "OPC_UA_SessionConnectInfo" at the parameter "SessionConnectInfo" of the instruction "OPC_UA_Connect").

  When you program the instruction "OPC_UA_Connect" you must therefore assign an empty string to the "ApplicationName". You can use the application name, for example, to identify the client and its sessions (SessionNames) for diagnostic purposes.

If you have activated the server, you can also use a different name that is meaningful in your project and that fulfills the requirements of your project, e.g. for worldwide uniqueness.

###### Changing the application name

To change the application name, follow these steps:

1. Select the CPU. Click on the CPU symbol (for example in the network view).
2. Click "OPC UA > General" in the properties of the CPU.
3. Enter a meaningful name.

Please note that the application name is also entered on the certificate (Subject Alternative Name) and you may have to generate an existing certificate again after changing the application name.

---

**See also**

[License for OPC UA (S7-1200)](#license-for-opc-ua-s7-1200)

##### Access to the OPC UA server (S7-1200)

###### Server addresses

The OPC UA server of the S7-1200 CPU can be reached over the integrated PROFINET interface of the CPU (firmware V4.4 and higher).

The server address is available in the area "OPC UA > Server > General" of the CPU parameters and shows the IP address of the PROFINET interface in form of a URL in the following format:

Example of a URL (Uniform Resource Locator) that can be used to set up connections to the OPC UA server of the CPU:

"opc.tcp://192.168.178.151:4840 "

The URL is structured as follows:

- Protocol identifier **"**opc.tcp://"
- IP address

  - 192.168.178.151

    The IP address at which the OPC UA server can be accessed from the Ethernet subnet 192.168.178.
- TCP Port number

  - Default: 4840 (standard port)

    The port number can be changed under "OPC > UA > Server > Port".

###### Dynamic IP addresses

If the IP address of the PROFINET interface has not been specified yet, the placeholder "<dynamically>" is displayed in the "Server addresses" area.

In this case, the IP address of this PROFINET interface must be set later on the device.

###### Standard SIMATIC server interface not for S7-1200

The option "Activate standard SIMATIC server interface" is not available for the OPC UA server of the S7-1200 CPU.

You must add server interfaces using the "OPC UA communication" entry in the project tree. These server interfaces make the PLC tags enabled for OPC UA visible for OPC UA clients.

---

**See also**

[OPC UA server interface configuration (S7-1200)](#opc-ua-server-interface-configuration-s7-1200)

##### Additional OPC UA server settings (S7-1200)

###### OPC UA server settings

In principle, the OPC UA server of the S7-1200 CPU offers the same settings as a S7-1500 CPU; only some options are not available with the OPC UA server of the S7-1200 CPU. Value ranges are restricted.

You can find additional information on the OPC UA server settings here:

[General settings of the OPC UA server](#general-settings-of-the-opc-ua-server-s7-1500-s7-1500t)

[Settings of the server for subscriptions](#settings-of-the-server-for-subscriptions-s7-1500-s7-1500t)

[Handling client and server certificates](#handling-client-and-server-certificates-s7-1500-s7-1500t)

[Generating server certificates with STEP 7](#generating-server-certificates-with-step-7-s7-1500-s7-1500t)

[User authentication](#user-authentication-s7-1500-s7-1500t)

##### License for OPC UA (S7-1200)

###### Runtime licenses

A "Basic" type license is required to run the OPC UA server of the S7-1200 CPU.

The required license type is displayed under "Properties > General > Runtime licenses > OPC-UA > Type of required license":

![Runtime licenses](images/127586509451_DV_resource.Stream@PNG-en-US.png)

To confirm purchase of the license, follow these steps:

1. Click "Runtime licenses > OPC UA" in the properties of the CPU.
2. Select the license from the "Type of purchased license" drop-down list.

#### OPC UA server interface configuration (S7-1200)

This section contains information on the following topics:

- [What is a server interface? (S7-1200)](#what-is-a-server-interface-s7-1200)
- [Using OPC UA companion specifications (S7-1200)](#using-opc-ua-companion-specifications-s7-1200)
- [Creating a user-defined server interface (S7-1200)](#creating-a-user-defined-server-interface-s7-1200)
- [Creating a server interface for reference namespace (S7-1200)](#creating-a-server-interface-for-reference-namespace-s7-1200)
- [Generating OPC UA nodes based on local data mappings of FB types and UDTs (S7-1200)](#generating-opc-ua-nodes-based-on-local-data-mappings-of-fb-types-and-udts-s7-1200)

##### What is a server interface? (S7-1200)

###### Definition

A server interface combines nodes of an OPC UA address space of a CPU into a unit, so that a specific view on this CPU is provided for OPC UA clients.

Each server interface defines one or more namespaces in the OPC UA server of the CPU.

STEP 7 (TIA Portal) differentiates between the following types of server interfaces:

- Companion specification

  For this type of server interface, you use a Companion Specification created by a workgroup, for example.

  The workgroup is typically composed of members of the OPC Foundation and another industry organization who have jointly specified an OPC UA information model for a specific purpose (for example, for data exchange with RFID devices or with injection molding machines).

  This information model is realized in the form of OPC UA nodes in the address space of an OPC UA server. OPC UA clients can access these OPC UA nodes.

  You can also use the server interface type "Companion specification", for example, to download company-internal information models, e.g. in SiOME.

  If you implement a certain companion specification in your project, you apply the specifications of this companion specification into your project as server interface.

  For "Companion specification"-type server interfaces, you can import multiple namespaces which the Companion specification uses.

  Additional information on companion specifications: Creating a server interface for companion specificationhere.

  Additional information on SiOME: [SiOME](https://support.industry.siemens.com/cs/ww/en/view/109755133)

  - When companion specifications refer to type definitions in dependent specifications, use the reference namespaces for this. You import reference namespaces as you would the actual companion specifications.

    See [Creating a server interface for reference namespace](#creating-a-server-interface-for-reference-namespace-s7-1200).
  - If you want to make instance data from FBs or UDTs of the CPU accessible to OPC UA clients, you can have these instance data assignments automatically made as of TIA Portal version V17. You only need to map the FB types or the UDTs to suitable OPC UA data types of an imported reference namespace. For this mapping to be possible, enable the option "Generate OPC UA nodes based on the local data mapping" in the dialog for creating an OPC UA server interface of the type companion specification/reference namespace.

    See [Generating OPC UA nodes based on local data mappings of FB types and UDTs](#generating-opc-ua-nodes-based-on-local-data-mappings-of-fb-types-and-udts-s7-1200)
- User-defined server interface:

  For this type of server interface you combine OPC UA nodes of an OPC UA server into a unit.

  To do this, use the specifications for your project or the requirements for your machine or your plant as a basis.

  Additional information on the user-defined server interface is available [here](#creating-a-user-defined-server-interface-s7-1200).

###### Injection molding machine as an example for companion specification

A server interface of the type "Companion specification", for example, contains the following elements:

- OPC UA nodes which you can write with an OPC UA client to receive information about this injection molding machine (in readable PLC tags)
- OPC UA nodes which you can write with an OPC UA client to transfer values to the injection molding machine (in writable PLC tags)

This server interface enables a default view of a CPU, which can be used to control an injection molding machine.

For injection molding machines, the companion specification "Euromap" defines a whole series of OPC UA nodes which you can combine in a server interface.

Other OPC UA nodes of the CPU are not included in this server interface. This provides a better overview.

###### Additional Information on handling server interfaces

Creation, export and loading of server interfaces is exactly the same as for the S7-1500 CPUs.

As of firmware V4.5, S7-1200 CPUs support server methods and structured data types (structures and arrays).

**Copying server interfaces of an S7-1500 CPU**

If you have created server interfaces for an S7-1500 CPU, you can copy these server interfaces to the "OPC UA communication" area of an S7-1200 CPU.

If the server interface contains elements that are not supported, as described above, a compilation of the configuration or the consistency check is canceled with errors.

##### Using OPC UA companion specifications (S7-1200)

###### Introduction

OPC UA is universally applicable: The standard itself does not, for example, specify how PLC tags are to be named. It is also up to the individual user (application developer) to program and name server methods that can be called over OPC UA.

**Information modeling and standardization for devices and sectors**

For applications of the same kind, it is worth standardizing your device or machine interfaces with the "OPC UA toolkit".

Many different bodies and working groups have driven forward standardization and developed a range of companion specifications.

These specifications define:

- The objects, methods and tags with which a typical device or machine is to be described.
- The namespace intended for the specified objects.

Machines are typically structured in functional or technological units, and these units are then standardized.

Companion specifications offer machine and plant operators the benefits of a standardized interface. For example, all RFID readers that comply with the AutoID specifications can be integrated in the same way. This means that all RFID readers that comply with the AutoID specifications can be addressed by OPC UA clients in the same way irrespective of manufacturer.

Another example of a companion specification from the injection molding machinery sector is the EUROMAP specification.

The EUROMAP information models and the corresponding OPC companion specifications standardize the data exchange between injection molding machines and the higher-level MES (Manufacturing Execution System). This allows the MES to connect all lower-level injection molding machines in the same way.

> **Note**
>
> **EUROMAP and the OPC Foundation have established the Joint Working Group "OPC UA Plastics and Rubber Machinery".**
>
> The existing EUROMAP recommendations EUROMAP 77 (data exchange between injection moulding machines and MES), 82.1 (temperature control devices) and 83 (general definitions) were published under the neutral umbrella of the OPC Foundation as OPC 40077, 40082-1 and 40083. Future publications will be published both as EUROMAP recommendations and as OPC companion specifications.
>
> A major change it the change of the namespace, for example, for EUROMAP 77: Currently "http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/".

###### Useful information on EUROMAP

**Euromap 77, Euromap 83 and OPC UA for Devices (DI)**

With Release Candidate 2, some of the EUROMAP definitions have been transferred from EUROMAP 77 to EUROMAP 83 (currently OPC 40083). EUROMAP 83 defines general types that are used in specific information models. You will therefore also need to import the OPC UA server interface of EUROMAP 83.

"OPC UA for Devices" is a generally applicable information model for the configuration of hardware and software components. The information model also serves as the basis for other companion standards and is therefore also imported.

The OPC UA XML files are available here:

[Euromap77](http://www.euromap.org/euromap77)

[Euromap83](http://www.euromap.org/euromap83)

[OPC UA for Devices](https://opcfoundation.org/UA/schemas/DI/)

###### Using EUROMAP companion specification: Overview

To use the EUROMAP companion specification, follow these steps:

1. Generate an XML file by creating an instance of the type "IMM_MES_InterfaceType" using the SiOME program.

   How to proceed is described below in "Step 1: Create instances in SiOME".
2. In STEP 7 (TIA Portal), create PLC tags and server methods that correspond to the instance of the type "IMM_MES_InterfaceType" (created in Step 1).

   See below for information on how to proceed in "Step 2: Create PLC tags in STEP 7".

   An example of OPC UA nodes and the corresponding PLC tags can be found in section "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)".
3. In STEP 7 (TIA Portal), add a new server interface of companion specification type and import the XML file you created in step 1.

   The "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)" section describes how to proceed.
4. Assign the OPC UA nodes of the new server interface to the corresponding PLC tags, which you created in step 2.

   The "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)" section describes how to proceed.

###### Step 1: Create instances in SiOME

The following section describes how to use the free program "SiOME", the "Siemens OPC UA Modeling Editor".

With SiOME, you can create an OPC UA XML file, which describes the server interface (an information model).

Download link and explanations about SiOME are available [here](https://support.industry.siemens.com/cs/ww/en/view/109755133).

**Procedure in STEP 7**

To use the new server interface, import the server interface into the STEP 7 project, see section "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)".

When the project is loaded into the CPU, the new server interface is available for OPC UA clients.

**Procedure in SiOME 1.7.3**

> **Note**
>
> The following description shows the work steps in SiOME 1.7.3.
>
> Follow-up versions of SiOME make it easier for you, for example, to create corresponding DBs, structures, variables or methods in the user program. Using a drag-and-drop operation, you can transfer data, for example, from SiOME to the TIA Portal (user program). In this case, the variables, etc. are already mapped correctly or, for methods, the corresponding FB elements are also generated correctly in the user program.
>
> Download the current SiOME version using the download link listed above, and follow the instructions in the documentation included in the download.

To use Euromap 77, create an XML file with an instance of "IMM_MES_InterfaceType".

The object type must be instantiated in order for the information model of the specific machine to appear in the address space of the OPC UA server.

The object type "IMM_MES_InterfaceType" is the root object type of Euromap 77. "IMM" stands for "Injection Moulding Machine".

Follow these steps:

1. Download the files "Opc_Ua.EUROMAP77.NodeSet2.xml" and "Opc_Ua_EUROMAP83_NodeSet2.xml" from the Euromap website (see above).
2. Download the file "Opc.Ua.Di.NodeSet2**.**xml" from the OPC Foundation website.

   The "Opc.Ua.Di.NodeSet2**.**xml" file contains type definitions which Euromap 77 uses.
3. Start SiOME.
4. First, import the namespace "http://opcfoundation.org/UA/DI/".

   To do so, click the ""Import XML" button in the "Information model" area.

   ![Step 1: Create instances in SiOME](images/111206704779_DV_resource.Stream@PNG-de-DE.png)

   SiOME displays the dialog for the opening files.
5. To import the file, select the "Opc.Ua.Di.NodeSet2.xml" file and click "Open".  
   Result: SiOME imports the XML file and shows the namespace "http://opcfoundation.org/UA/DI/" in the "Namespaces" area.

   The standard namespace "http://opfoundation.org/UA/" is always available in SiOME and does not have to be imported.
6. Now import the namespace "http://www.euromap.org/euromap83/"

   To do so, click the "Import XML" button again in the "Information model" area.

   Select the file "Opc_Ua.EUROMAP83.NodeSet2.xml".

   Result: SiOME imports the XML file and shows the namespace "http://www.euromap.org/euromap83/" in the "Namespaces" area.
7. Now import the namespace "http://www.euromap.org/euromap77/"

   To do so, click the "Import XML" button again in the "Information model" area.

   Select the file "Opc_Ua.EUROMAP77.NodeSet2.xml".
8. Create your own namespace for your project.

   To do this, right-click in the "Namespaces" area on "OPC UA Modelling Editor Project" or on "Namespaces" and select "Add Namespace".

   SiOME opens the "Add Namespace" dialog.
9. Enter the name of a new namespace.

   The "YourCompany.org" namespace is used in the example.

   SiOME now also displays the new namespace:

   ![Step 1: Create instances in SiOME](images/111206922763_DV_resource.Stream@PNG-de-DE.png)
10. Create an instance from the root object type IMM_MES_InterfaceType of the Companion specification Euromap 77.   
    To do so, in the "Information model" area, right-click the "DeviceSet" directory and select "Add Instance".

    SiOME displays the "Add Instance" dialog.
11. For "Name", enter a meaningful name for your instance.

    In the example, enter "IMM_Manufacturer_01234".

    For "TypeDefinition", select "IMM_MES_InterfaceType".

    This object type is the root object type of Euromap 77: If you generate an instance of this object type, then use the Euromap 77 once in the address space of your OPC UA server.
12. Click "OK".

    SiOME shows the new instance "IMM_Manufacturer_01234" in the "Information model" area under "DeviceSet":

    ![Step 1: Create instances in SiOME](images/124448410251_DV_resource.Stream@PNG-de-DE.png)
13. Create an instance of the data type "InjectionUnitType".

    To do this, right-click on the "InjectionUnits" directory in the "Information model" area and select "Add Instance".

    SiOME displays the "Add Instance" dialog.

    For "Name", enter a meaningful name for the instance.

    In the example, enter "InjectionUnit_1".

    For "TypeDefinition", select "InjectionUnitType".

    Click "OK".
14. Create a new "Mould_1" instance of the "MouldType" object type in the "Moulds" directory.
15. Create a new instance "PowerUnit_1" of the "PowerUnitType" object type in the "PowerUnits" directory.
16. Save the XML file.

    To do so, click the "Quick save" button in the "Information model" area:

    ![Step 1: Create instances in SiOME](images/124448418443_DV_resource.Stream@PNG-de-DE.png)
17. Export the XML file.

    To do so, click the ""Export XML" button in the "Information model" area.

    ![Step 1: Create instances in SiOME](images/111206713611_DV_resource.Stream@PNG-de-DE.png)

    SiOME shows the "Export XML" dialog.
18. Leave all namespaces activated and click "OK".

    SiOME displays the "Save as" dialog.
19. Select a meaningful name and save the exported file.

    In the example, name the XML file "IMM_Manufacturer_01234".

**Result**:

You have now created an XML file which uses the companion specification "Euromap 77" once (with one instance).

###### Step 2: Creating PLC tags for the Euromap 77 instance in STEP 7.

For Euromap 77, you must provide PLC tags and server methods in your user program and assign the instance of the "IMM_MES_InterfaceType" type.

To create PLC tags for the instance of the "IMM_MES_InterfaceType" type, proceed as follows.

1. Create a user-defined data type (UDT).

   The figure below shows the beginning of the user-defined data type "InjectionUnit" as example.

   This data type has the same structure as "InjectionUnit" in the type "IMM_MES_InterfaceType".

   Make sure that you use SIMATIC data types that are compatible with the OPC UA data types (see "Mapping of data types" below).

   ![Step 2:  Creating PLC tags for the Euromap 77 instance in STEP 7.](images/125157130635_DV_resource.Stream@PNG-en-US.png)
2. Add a new global data block to your STEP 7 project.

   In the example, name the data block "IMM_Manufacturer_01234", so that there is a reference to the injection molding machine of the respective manufacturer and the serial number.
3. Create a new element in this data block.

   In the example, name this element "InjectionUnit_1"
4. Assign the new user-defined data type "InjectionUnit" to this element.

###### Result

In your STEP 7 project, you have created a tag for the Euromap 77 in the "IMM_Manufacturer_01234" data block.

##### Creating a user-defined server interface (S7-1200)

###### Procedure

To create an Server interface, follow these steps:

1. Select the CPU that you have used and configured as OPC UA server.
2. Click "OPC UA communication > Server interfaces".
3. Double-click "Add new server interface".

   STEP 7 displays the following dialog.

   ![Procedure](images/134348165259_DV_resource.Stream@PNG-en-US.png)
4. Change the name of the new server interface so that it is descriptive in your project.

   In the example, change the name "Server-interface_1" suggested by STEP 7 to "Cell_1".
5. Click "Server interface" and then "OK".
6. Click on the triangle in front of "Program blocks" in the area "OPC UA elements" to open the "Program blocks" folder.

   STEP 7 displays a table for editing:

   The editor is divided into two areas.

   - **OPC UA server interface**

     On the left is the root node of the server interface "Cell_1".

     This interface is currently still empty: No OPC UA elements have been added to the server interface yet.
   - **OPC UA elements**

     On the right are the OPC UA elements.

     OPC UA elements are objects that have been created so far in the STEP 7 project and have the property "Accessible from HMI/OPC UA".

     You can add the OPC UA elements to the new server interface "Cell_1".
7. Drag the OPC UA elements into the "<Add new>" line of the new server interface.

   ![Procedure](images/134348192011_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > The following applies in general: If you store data blocks or technology objects in the left area of the table, STEP 7 (TIA Portal) creates an object in the server interface. The elements of the data blocks are arranged as separate nodes below this.
   >
   > If you store structures in the left area of the table, STEP 7 does not create a node for the structure as a whole, but only nodes for each element of the structure.
   >
   > The same applies to arrays: Again, STEP 7 does not create a node for the array as a whole, but nodes for each element of the array.

**Limiting the view to OPC UA servers**

By selecting the OPC UA elements, you limit the view to the OPC UA server and the options of the OPC UA clients.

You have the option to disable the visibility of each configured server interface in the properties of the server interface and thus prevent this server interface being used by clients during operation.

- To do this, select the server interface and right-click on the "Properties" command.

This option lets you define multiple server interfaces, for example, and enable and download only the server interface required for a CPU in each case.

Once a server interface has been defined, you can drag it to another CPU in the project tree.

![Procedure](images/134348207755_DV_resource.Stream@PNG-en-US.png)

###### Information on the server interface

The "OPC UA Server Interface" dialog is structured as a table and provides the following information:

Note that not all columns are displayed initially. You determine what is displayed by right-clicking on the header line of the table.

When a row is selected, you can display the OPC UA attributes of the node in the Inspector window ("OPC UA attributes" area), such as node ID, node class, node type, and description.

- **BrowseName**

  The language neutral name of the user-defined server interface is at the top (BrowseName). This name can be freely selected.

  The names (BrowseNames) of the individual OPC UA nodes that have been added to the server interface are under the name of the interface.

  You cannot change the name of an OPC UA node in this dialog. The names come from the STEP 7 project.

  You can delete an OPC UA node from the table. This means that it no longer belongs to the server interface and is no longer visible to OPC UA clients.
- **DisplayName**

  Similar to BrowseName. However, the name can be translated and is displayed, if available, in the corresponding language.
- **Node ID**

  NodeId of the OPC UA node, e.g. http://Server-Node_1; i=1
- **Node type**

  Type of the OPC UA node, for example BOOL, BYTE, INT.

  These node types were defined by Siemens, not by the OPC Foundation. For example, the OPC Foundation uses the Boolean node type for BOOL. BOOL is directly derived from Boolean.

  The specified node type cannot be changed in this dialog: If you want to use a different node type, you must change the type of the respective PLC tags in the STEP 7 project.
- **Access level**

  - If an OPC UA node is a tag (UAVariable type), the node can be only readable (RD) or readable and writable (RD/WR).
- **Description**
    
  The description at the node corresponds to the comment at the CPU tag (e.g. the comment for a data block element). STEP 7 adds the comment to the description of the node during mapping.
- **Data type**

  The SIMATIC data type used in the STEP 7 project is specified, for example, Bool, Byte, Int. etc.
- **Local data**

  The SIMATIC data type of the data block in the CPU, from which the value of an OPC UA node (UAVariable type) is read, or to which a value is written.

###### Generate local data

You have the option of generating local data for all or for selected nodes of the server interface that are not already assigned ("mapped") to local data of the CPU. The newly created local data are mapped automatically.

You trigger the automatic generation of local data by clicking the "Generate local data" button (all nodes that are not already mapped) or by selecting individual nodes and then clicking the "Generate local data" shortcut menu.

"Generate local data" button:

![Generate local data](images/142323385099_DV_resource.Stream@PNG-en-US.png)

You can only generate nodes that can be mapped to local data, which means no objects, no folders, no methods or input/output arguments of methods.

After you have clicked the button or selected the shortcut menu, you must select in the follow-up dialog box whether the local data should be created in a new DB or in an existing DB.

###### Consistency check

You have the option to check the server interface.

During the consistency check, STEP 7 checks whether the OPC UA nodes of the server interface are each assigned to a suitable OPC UA element (identical data type) or whether the used element still exists in the CPU.

In methods, STEP 7 checks the quantity, name and data type of the arguments.

To check the consistency of the server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Consistency check](images/134363766923_DV_resource.Stream@PNG-en-US.png)

###### Export interface

You have the option of exporting the OPC UA server interface as an XML file. This XML file contains all data type definitions referenced by the server interface.

To export the OPC UA server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Export interface](images/134363752971_DV_resource.Stream@PNG-en-US.png)

##### Creating a server interface for reference namespace (S7-1200)

###### Companion specifications and referenced namespaces

A series of OPC UA object types (as well as additional definitions) are defined in a companion specification. These object types are each defined in namespaces so that the names of the object types (type definitions) are unique.

To use a companion specification in your project, create instances of object types of this companion specification.

To do this the object definitions must be available in your STEP 7 project. If this is not the case, you must import the object definitions. To import all definitions of a namespace, create a server interface of type "Reference namespace" for each namespace in STEP 7.

###### Example Euromap 77

You have added a server interface for the companion specification Euromap 77 .

The server interface uses object types defined in OPC UA DI as well as in Euromap 83 and Euromap 77 in their corresponding namespaces.

Therefore, in addition to the server interface Euromap 77 of the "Companion Specification" type, create additional server interfaces of "Reference namespace" type in STEP 7, in each case for the following namespaces:

- http://opcfoundation.org/UA/DI/
- http://www.euromap.org/euromap83/
- http://www.euromap.org/euromap77/

The following description shows you how to proceed.

###### Creating a server interface for a reference namespace

To create a server interface for a namespace, proceed as follows:

1. Select the CPU that you want to use as an OPC UA server.
2. Click "OPC UA communication > Server interfaces".
3. Double-click "Add new server interface".

   STEP 7 (TIA Portal) now displays the dialog "Add new server interface".

   A general name for the new server interface is entered in the dialog, for example "Server_Interface_1".
4. Assign a descriptive name for the new server interface.

   In the example, select the name "OPC.Ua.Di" or a similar name that clearly references the namespace "http://opcfoundation.org/UA/DI/".

   This namespace must be imported first. It contains basic definitions (for example, the UAObjectType "DeviceType").
5. For "Import XML file", select an XML file that contains the definitions of the namespace "http://opcfoundation.org/UA/DI/".

   Select the file "Opc.Ua.Di.NodeSet2.xml" in the example. You can download this file here:  
   [Opc.Ua.Di.NodeSet2.xml](https://opcfoundation.org/UA/schemas/DI/)

   The figure below shows the dialog with the entries:

   ![Creating a server interface for a reference namespace](images/134447361803_DV_resource.Stream@PNG-en-US.png)
6. Click "OK".

   STEP 7 (TIA) now generates the new server interface.

You can find the server interface in the project navigation of STEP 7 (TIA Portal), under "OPC UA Communication > Server interfaces > Namespace references".

If a companion specification uses additional namespaces, add a new server interface for each namespace.

**Add additional server interfaces for Euromap77**

For Euromap 77, you still need the following namespaces:

- http://www.euromap.org/euromap83/
- http://www.euromap.org/euromap77/

First, add a server interface for the namespace "http://www.euromap.org/euromap83/".

This namespace contains basic definitions for Euromap 77, therefore it is required here first. All definitions of this namespace are included in the XML file "Opc_Ua.EUROMAP83NodeSet2.xml", which you can download from the [Euromap website](http://www.euromap.org/en/euromap83).

Then add a server interface for the namespace "http://www.euromap.org/euromap77". All definitions of this namespace are included in the XML file "Opc_Ua.EUROMAP77.NodeSet2.xml", which you can also download from the [Euromap website](http://www.euromap.org/en/euromap77).

###### Consistency check

You have the option to check the server interface.

STEP 7 (TIA Portal) checks whether the OPC UA node of the server interface PLC tags (data blocks) has been assigned compatible SIMATIC data types.

To check the consistency of the server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Consistency check](images/134411473803_DV_resource.Stream@PNG-en-US.png)

###### Export interface

You have the option of exporting the OPC UA server interface as an XML file. This XML file contains all data type definitions referenced by the server interface.

To export the OPC UA server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Export interface](images/134411459851_DV_resource.Stream@PNG-en-US.png)

##### Generating OPC UA nodes based on local data mappings of FB types and UDTs (S7-1200)

If you want to make instance data from FBs or UDTs of the CPU accessible to OPC UA clients, you can have these instance data assignments automatically made as of TIA Portal version V17.

You only have to map the FB types or the UDTs to suitable OPC UA data types of imported reference namespaces. Based on these mappings created in STEP 7 (TIA Portal), generate the required nodes in the server interface for each FB instance or for each UDT usage during the compile.

If you extend your program and add more FB instances or UDT usages, or if you add existing instances delete, you do not need to worry about adapting the server interface: STEP 7 automatically adjusts the server interface when compiling the program.

###### Example

- You create a function block (FB) in the user program of the CPU and define in the "Static" area of the interface of the FB the parameters that form the "memory" of the FB. The instances (values) of this parameter are to be accessible for OPC UA clients.
- You create an OPC UA data type (e.g. with SiOME) with elements that correspond to the data type the parameters in the static area of interface of the FB. The order of the elements does not matter. Then import the reference nodeset file (reference namespace) as a reference name space.

The following figure shows the assignment of elements as comparison of the reference namespace view (server interface) and the OPC UA elements view (program).

![Example](images/143156317579_DV_resource.Stream@PNG-de-DE.png)

**Mapping of data types (FB interface - OPC UA interface): Principle**

The following figure shows the assignment of the elements from the user program of the CPU to the elements of the OPC UA server interface. Names and the order of the elements do not have to match.

![Example](images/141229107467_DV_resource.Stream@PNG-de-DE.png)

**Automatic generation of the OPC UA server instances in the server interface: Principle**

The figure below shows the compilation of the project. The instances of the user program are also generated in the server interface.

![Example](images/143157002635_DV_resource.Stream@PNG-de-DE.png)

By mapping between FB type information / UDT type information and OPC UA type information, STEP 7 is able to create all instances present in the program as nodes in the server interface. You have the option to generate these nodes together with a new server interface or to generate these nodes in an existing server interface.

![Example](images/141310135179_DV_resource.Stream@PNG-en-US.png)

###### Rules

- Only the FB elements in the "Static" area of an FB interface can be mapped to OPC UA type descriptions.
- When mapping the data types, OPC UA elements from the same FB interface or from the same UDT must always be selected for an object. Mapping from different FBs or UDTs to an object is not permitted.

###### Requirement

- The FB types used, defined in the "Static" area of an FB, must be configured as "Accessible for OPC UA".
- The UDTs used must be configured as "Accessible for OPC UA".
- A nodeset file (XML file) is available with OPC UA data type definitions that match the FB types or UDTs defined in user program (can be mapped).
- The user program with the FB instances and UDT usages is available.

###### Procedure

To map a data type from a reference namespace to an FB type or UDT data type, follow these steps:

1. Select the CPU that you want to use as an OPC UA server.
2. Import the prepared nodeset file (XML file) with the type definitions as a reference namespace

   (see [Creating a server interface for reference namespace](#creating-a-server-interface-for-reference-namespace-s7-1500-s7-1500t)).

   - In the "Add new server interface" dialog, enable the option "Generate OPC UA nodes based on the local data mapping".

     Only when this option is enabled can you map FB types or UDTs by dragging them to the OPC UA type descriptions.
3. Double-click the icon for the server interface of the "Reference namespace" type that you just generated.

   The editor for mapping between OPC UA server interface and OPC UA elements opens. In the properties area of the editor, in the "Mapping of local data", the option "Generate OPC UA nodes based on the local data mapping" is enabled. If not, enable the option now.

   Edit the "Interface name" field; to do this, click on the three dots on the right edge of the field.

   Select an existing server interface or create a new server interface ("Add" button).

   When adding, a new server-interface is created. If you select an existing server interface, you can edit the properties ("Edit" button).
4. Assign the existing FB types or UDTs to the nodes of the server interface (reference namespace) by dragging the OPC UA element (right side of the editor) to the corresponding node of the server interface (reference namespace, "Local data" column).

   ![Procedure](images/142427612939_DV_resource.Stream@PNG-en-US.png)
5. Compile the project.

   After the compile, the newly generated nodes of the instances are located in the server interface. STEP 7 creates an object for each instance DB. The generated elements are located under each of these objects.

   Similarly, STEP 7 also creates an object for each global DB that is created when a UDT is instantiated.

###### Create user program with FB types or UDT

How to create FBs and UDTs is not explained in detail here; for this purpose use the description for creating a user program, e.g. declare block interface and declare PLC data types (UDT).

###### Consistency check

The consistency check ("Consistency check" button of the editor) also checks the mapping of the data types and updates the display of the data types in the corresponding column of the editor.

#### Providing methods on the OPC UA server (S7-1200)

This section contains information on the following topics:

- [Useful information about server methods (S7-1200)](#useful-information-about-server-methods-s7-1200)
- [Boundary conditions for using server methods (S7-1200)](#boundary-conditions-for-using-server-methods-s7-1200)

##### Useful information about server methods (S7-1200)

###### Providing user programs for server methods

You can provide OPC UA methods by the user program in the OPC UA server of an S7-1200 CPU.

With OPC UA methods, you can trigger specific actions on the controller and transfer data consistently.

OPC UA methods can use an OPC UA client, for example, to start a production order via the method call of the S7-1200.

OPC UA methods, an implementation of "Remote Procedure Calls", provide an efficient mechanism for interactions between different communication nodes. The mechanism provides both job confirmation and feedback values, therefore you no longer need to program handshake mechanisms.

###### How does an OPC UA method work?

In principle, an OPC UA method works like a know-how-protected function block that is called during runtime.

The OPC UA client "sees" only the defined inputs and outputs. The content of the function block, the method or the algorithm, remains hidden from the external OPC UA client. The OPC UA client receives feedback upon successful execution, and values returned by the function block (method) or an error message if execution was not successful.

As a programmer, you have full control over and responsibility for the program context in which the OPC UA method is executed.

###### Rules for programming a method and runtime behavior

- Ensure that the values returned by the OPC UA method are consistent with the input values provided by the OPC UA client.
- Follow the rules for assigning the name and structure of parameters and the permitted data types (see description of OPC UA server instructions).
- Behavior during runtime: The OPC UA server accepts one call per instance. The method instance is not available for other OPC UA clients until the call is completed or the time for it has expired. The instance time expires when the maximum time allowed to connect to the server is reached.

###### Implementing a server method

The implementation of a server method includes the following tasks:

- Specifying optional input and output parameters for the server method
- Querying the call of the server method with OPC_UA_ServerMethodPre
- Writing the server method
- Answering the server method with OPC_UA_ServerMethodPost

###### Specifying optional input and output parameters for the server method

An OPC UA method can optionally specify input or output parameters. No parameter type is mandatory. The OPC UA client provides input parameters for the OPC UA method during runtime. The OPC UA method returns output parameters for the OPC UA client during runtime when the method is completed.

Follow these steps to specify input parameters for the OPC UA method:

1. Specify a Struct named UAMethod_InParameters in the static part of the FB interface. Mark this Struct data type as "Accessible from HMI/OPC UA/Web API" and "Writable from HMI/OPC UA/Web API".
2. Set the input parameters of the OPC UA method in this Struct. The input parameters can have any valid name. The data types of the input parameters for an OPC UA method can be scalar (Int, Real etc.), structured data types or arrays.

Proceed as follows to specify output parameters for the OPC UA method:

1. Specify a Struct named UAMethod_OutParameters in the static part of the FB interface. Select this Struct data type as "Accessible from HMI/OPC UA/Web API".
2. Set the output parameters of the OPC UA method in this Struct. The output parameters can have any valid name. The data types of the output parameters for an OPC UA method can be scalar (Int, Real etc.), structured data types or arrays.

The following example shows user-defined input and output parameters for an OPC UA method:

![Specifying optional input and output parameters for the server method](images/155001277067_DV_resource.Stream@PNG-en-US.png)

###### Querying the call of the server method with OPC_UA_ServerMethodPre

Call the "OPC_UA_ServerMethodPre" instruction in your user program from your server method.

The instruction asks the OPC UA server of the S7-1200 CPU whether the server method was called by an OPC UA client.

When an OPC UA client calls the server method, the server method receives all input parameters from the OPC UA client.

###### Writing the server method

You make the actual user program available in the server method section between the calls of OPC_UA_ServerMethodPre and OPC_UA_ServerMethodPost. You have the same options as with any other user program (for example, access to other function blocks or global data blocks). If the server method works with input parameters, these parameters are available to you. The server method may only execute this section if an OPC UA client has called the server method and the server method in turn has called OPC_UA_ServerMethodPre.

After successful execution of the method, set the output parameters of the server method (if the method has such output parameters).

###### Responding to the server method with OPC_UA_ServerMethodPost

Call the "OPC_UA_ServerMethodPost" instruction to complete the server method.   
Use the parameters to inform the "OPC_UA_ServerMethodPost" instruction about the processing state of the user program.   
As soon as the user program has been executed successfully, the OPC UA server is informed by the relevant parameters. The OPC UA server then sends the output parameters of the server method to the OPC UA client.

###### Information about server methods

Always use "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" in pairs when writing an OPC UA method. OPC UA methods only work if both methods are added.

A detailed description of "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" can be found in the TIA Portal Information System.

###### Integrate server method

The figure below shows how an OPC UA client (A) calls the "Cool" server method:

![Integrate server method](images/154994013067_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| O | The OPC UA client calls the OPC UA server method and manages its "Done" state. |
| ① | The OPC UA method calls between the OPC UA client and the OPC UA server method are asynchronous. |
| B | The firmware of the OPC UA server waits for calls from the OPC UA client, manages calls in the queue and forwards the "Done" information from the cyclic user program to the OPC UA client. |
| ② | This call transfers data from the OPC UA server to the instance of the user program, "Cool" method FB. |
| C | The OPC_UA_ServerMethodPre instruction is used to ask the OPC UA server of the CPU whether the OPC UA server method was called by an OPC UA client. As soon as an OPC UA client calls the OPC UA server method, the OPC_UA_ServerMethodPre instruction sets a flag indicating that the OPC UA server method is currently being called by the OPC UA client. If input parameters from the OPC UA client are available, the OPC_UA_ServerMethodPre instruction makes them available to the "Cool" method FB. The user program, "Cool" method FB, must call the OPC_UA_ServerMethodPre instruction first. |
| ③ | The "Cool" method FB executes a synchronous call of the instruction OPC_UA_ServerMethodPre. The OPC_UA_ServerMethodPre instruction is a static multi-instance tag that stores input data from the OPC UA client. The return value from the synchronous call indicates whether or not a client has called the OPC UA server method. |
| ④ | The cyclic user program calls the "Cool" method FB asynchronously with the required instance parameters. |
| ⑤ | This synchronous call checks the status - completed or "running" - of the OPC UA server method. |
| D | The OPC_UA_ServerMethodPost instruction forwards the output data of the method instance to the OPC UA server after completion of the OPC UA server method. In addition, the OPC_UA_ServerMethodPost instruction notifies the method instance and the OPC UA server that the method is complete. |
| ⑥ | This call transfers data from the instance of the user program, "Cool" method FB, to the OPC UA server. |
| ⑦ | The firmware of the OPC UA server sends the information back to the OPC UA client. |

###### How it works in this example

The CPU executes the "Cool1" instance of the "Cool" server method FB in the cyclic user program ④.

The "Cool1" instance calls the "OPC_UA_ServerMethodPre" instruction to query ③ whether an OPC UA client has called the "Cool" server method FB ①.

- If the OPC_UA_ServerMethodPre server method FB has not called the "Cool" instruction, program execution is returned directly to the cyclic user program via ③ and ④. The CPU resumes the cyclic user program after "Cool1".
- If the "Cool" server method FB has already called OPC_UA_ServerMethodPre, OPC_UA_ServerMethodPre returns information directly to the "Cool" server method FB via ③. The "Cool" method FB is now executed and accesses data from the plant machines.

As soon as the OPC UA server method is completed, the "Cool" server method FB calls the "OPC_UA_ServerMethodPost" instruction ⑤ to inform the firmware (B) that the instruction ⑥ has been executed. The firmware returns this information via ⑦ to the calling OPC UA client (A). The CPU resumes the cyclic user program after "Cool1".

###### Information about server instructions

The "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" are described in detail in the help to the Instructions > Communication > OPC UA > OPC UA server.

##### Boundary conditions for using server methods (S7-1200)

###### Permitted data types

If you provide server methods, observe the following rule:

- Assign the data types as shown below (SIMATIC data type - OPC UA data type). Other assignments are not permitted.

STEP 7 does not check the observance of this rule and does not prevent an incorrect assignment. You are responsible for the rule-compliant selection and assignment of the data types.

You can also use the listed data types, for example, as elements of structures/arrays/UDTs for input and output parameters of self-created server methods (UAMethod_InParameters and UAMethod_OutParameters).

| SIMATIC data type | OPC UA data type |
| --- | --- |
| BOOL | Boolean |
| SINT | SByte |
| INT | Int16 |
| DINT | Int32 |
|  |  |
| USINT | Byte |
| UINT | UInt16 |
| UDINT | UInt32 |
|  |  |
| REAL | Float |
| LREAL | Double |
| LDT | DateTime |
| WSTRING | String |
| DINT | Enumeration (Encoding Int32) and all derived data types |

###### Number of implementable server methods and number of arguments

If you implement server methods via your user program, the number of usable methods is limited depending on the CPU type, see the following table (up-to-date technical data of the CPUs can be found in the [Internet](https://support.industry.siemens.com/cs/ww/en/ps/td)).

| Technical specification value | CPU 121x |
| --- | --- |
| Maximum number of usable server methods or max. number of server method instances (OPC_UA_ServerMethodPre, OPC_UA_ServerMethodPost instructions) | 20 |
| Maximum number of arguments per method  (More than the specified number of arguments can be configured and loaded into the CPU, but an OPC UA client cannot call the method). | 20 |

**Error message when exceeded**

If the maximum number of server methods is exceeded, the OPC_UA_ServerMethodPre or OPC_UA_ServerMethodPost instructions report the error code 0xB080_B000 (TooManyMethods).

###### Supply of structured data types with nested arrays

If a structured data type (Struct/UDT) contains an array, the OPC UA server does not provide information about the length of this array.

If you use such a structure as the input or output parameter of a server method, for example, you must ensure that the nested array is supplied with the correct length when the method is called.

If you do not adhere to this rule, the method fails with the error code "BadInvalidArgument".

### Using the S7-1500 as an OPC UA server (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Interesting information about the OPC UA server of the S7-1500 CPUs (S7-1500, S7-1500T)](#interesting-information-about-the-opc-ua-server-of-the-s7-1500-cpus-s7-1500-s7-1500t)
- [Accessing OPC UA server data (S7-1500, S7-1500T)](#accessing-opc-ua-server-data-s7-1500-s7-1500t)
- [Configuring the OPC UA server (S7-1500, S7-1500T)](#configuring-the-opc-ua-server-s7-1500-s7-1500t)
- [OPC UA server interface configuration (S7-1500, S7-1500T)](#opc-ua-server-interface-configuration-s7-1500-s7-1500t)
- [Providing methods on the OPC UA server (S7-1500, S7-1500T)](#providing-methods-on-the-opc-ua-server-s7-1500-s7-1500t)
- [Providing alarms on the OPC UA server (S7-1500, S7-1500T)](#providing-alarms-on-the-opc-ua-server-s7-1500-s7-1500t)

#### Interesting information about the OPC UA server of the S7-1500 CPUs (S7-1500, S7-1500T)

This section contains information on the following topics:

- [The OPC UA server of the S7-1500 CPUs (S7-1500, S7-1500T)](#the-opc-ua-server-of-the-s7-1500-cpus-s7-1500-s7-1500t)
- [End points of the OPC UA server (S7-1500, S7-1500T)](#end-points-of-the-opc-ua-server-s7-1500-s7-1500t)
- [Mapping SIMATIC data types to OPC UA data types (S7-1500, S7-1500T)](#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t)
- [Runtime behavior of the OPC UA server (S7-1500, S7-1500T)](#runtime-behavior-of-the-opc-ua-server-s7-1500-s7-1500t)

##### The OPC UA server of the S7-1500 CPUs (S7-1500, S7-1500T)

The S7-1500 CPUs as of firmware V2.0 are equipped with an OPC UA server. Apart from the Standard-S7-1500 CPUs this applies to the variants S7-1500F, S7-1500T, S7-1500C, S7-1500pro CPUs, ET 200SP CPUs, SIMATIC S7-1500 SW controllers and PLCSIM Advanced.

Convention: "S7-1500 CPUs" also includes the above-mentioned CPU variants.

###### S7-1500 CPU OPC UA server basics

Access to the OPC UA server of the CPU is possible via all integrated PROFINET interfaces of the S7-1500 CPU.

Direct access to the OPC UA server of the CPU over the backplane bus of the automation system is not possible via CPs under the following conditions:

- Configuration with TIA Portal Version V16 or higher
- S7-1500 CPU firmware version 2.8 or higher and CP 1543-1 firmware version V2.2 or higher

For configuration, see [Access to OPC UA applications](#access-to-opc-ua-applications-s7-1200-s7-1500-s7-1500t).

Direct access to the OPC UA server of the CPU over the backplane bus of the automation system is not possible via CMs.

For access by clients, the server saves the enabled PLC variables and other information in the form of nodes (see [Accessing OPC UA server data](#accessing-opc-ua-server-data-s7-1500-s7-1500t)). These nodes are interconnected and form a network. OPC UA defines access points to this network (well-known nodes) that enable navigation to subordinate nodes.

With an OPC UA client you can read, observe or write values of variables of the PLC program as well as call methods that are available to the server. As of firmware version 2.5 you can implement methods, see [Useful information about server methods](#useful-information-about-server-methods-s7-1500-s7-1500t).

###### Node classes

OPC UA servers provide information in the form of nodes. A node can be, for example, an object, a tag, a method or a property.

The example below shows the address space of the OPC UA server of an S7-1500 CPU (extract from the OPC UA client "UaExpert" from Unified Automation).

![Example of the address space of the OPC UA server of an S7-1500 CPU](images/131659661963_DV_resource.Stream@PNG-de-DE.png)

Example of the address space of the OPC UA server of an S7-1500 CPU

The "MyValue" tag is selected in the figure above.

This tag is located below the "Memory" server interface node.

###### Address space

The nodes are linked over references, for example, the reference "HasComponent, which represents a hierarchical relationship between a node and its subordinate nodes. With their references, the nodes form a network that can, for example, take the form of a tree.

A network of nodes is also called an address space. Starting from the root, all nodes can be reached in the address space.

##### End points of the OPC UA server (S7-1500, S7-1500T)

The end points of the OPC UA server define the security level for a connection. Depending on the purpose of use or desired security level, you have to carry out the corresponding settings for the connection at the end point.

###### Different security settings

Before establishing a secure connection, OPC UA clients ask the server with which security settings connections are possible. The server returns a list with all the security settings (endpoints) that the server offers.

###### Structure of end points

End points consist of the following components:

- Identifier for OPC: "opc.tcp"
- IP address: 192.168.178.151 (in the example)
- Port number for OPC UA: 4840 (standard port)

  The port number can be configured.
- Security setting for messages (Message Security Mode): None, Sign, SignAndEncrypt.
- Encryption and hash procedures (Security Policy): None, Basic128Rsa15, Basic256, Basic256Sha256 (in the example).

The following figure shows the "UA Sample Client" of the OPC Foundation.

The client has established a secure connection to the OPC UA server of an S7-1500 CPU to the end point "opc.tcp://192.168.178.151:4840 - [SignAndEncrypt: Basic256Sha256:Binary]". The security settings "SignAndEncrypt:Basic256Sha256" are contained in the end point.

> **Note**
>
> **Select an endpoint with as strict as possible a security policy**
>
> Select an application-appropriate security policy for the end point and disable the less strict security policy at the OPC UA server.
>
> A Sha256 certificate is required for the most secure end points (Basic256Sha256) of the S7-1500 CPU OPC UA server.

![Structure of end points](images/128184168203_DV_resource.Stream@PNG-de-DE.png)

A connection to a server end point is only established if the OPC UA client complies with the security policies of that end point.

###### Through the information provided by the OPC UA server

OPC UA servers provide a wide range of information:

- The values of PLC tabs and DB components which clients may access.
- The data types of these PLC tags and DB components.
- Information on the OPC UA server itself and on the CPU.

This gives clients an overview and allows them to read out specific information. Previous knowledge of the PLC program and the CPU data is not required. You do not need to ask the developer of the PLC program when PLC tags are to be read. All necessary information is stored on the server itself (for example, the data types of the PLC tags).

###### Display of the information of the OPC UA server

You have the following options:

- Online: You have all the available information displayed during the runtime of the OPC UA server. To do so, navigate (browse) the address space of the server.
- Offline: You export an XML file that is based on the XML schemes of the OPC Foundation.

  Server methods created by the user (FB instance that can be called by an OPC UA client) are not exported as of STEP 7 V15.1), see [Providing methods on the OPC UA server](#providing-methods-on-the-opc-ua-server-s7-1500-s7-1500t).
- Offline with the Openness API: In your program, you use the API (Application Programming Interface) of the TIA Portal to access the function for exporting all PLC tags that can be read by OPC UA. This requires .NET Framework 4.0; see TIA Portal Openness, [Automating SIMATIC projects with scripts](https://support.industry.siemens.com/cs/ww/en/view/109477163).
- If you already know the syntax and the PLC program, you can access the OPC UA server without first researching the information.

##### Mapping SIMATIC data types to OPC UA data types (S7-1500, S7-1500T)

###### SIMATIC and OPC UA data types

SIMATIC data types do not always correspond with OPC UA data types.

S7-1500 CPUs provide SIMATIC tags (with SIMATIC data types) to their own OPC UA server as OPC UA tags (with OPC UA data types). OPC UA clients can then access these tags with OPC UA data types via the server interface.

A client can read the attribute "DataType" from such a tag and reconstruct the original data type in SIMATIC.

**Example**

A tag has the SIMATIC data type "COUNTER". You read COUNTER → UInt16 in the table. You now know that you do not need to convert; the COUNTER value is sent over the line as a UInt16 data type.

The client detects from the attribute "DataType" that the tag is actually the SIMATIC data type "COUNTER". With this knowledge, the client reconstructs the data type.

SIMATIC and OPC UA data types

| SIMATIC data type | OPC UA data type |
| --- | --- |
| BOOL | Boolean |
| BYTE | BYTE  → Byte |
| WORD | WORD  → UInt16 |
| DWORD | DWORD  → UInt32 |
| LWORD | LWORD  → UInt64 |
| SINT | SByte |
| INT | Int16 |
| DINT | Int32 |
| LINT | Int64 |
| USINT | Byte |
| UINT | UInt16 |
| UDINT | UInt32 |
| ULINT | UInt64 |
| REAL | Float |
| LREAL | Double |
| S5TIME | S5TIME  → UInt16 |
| TIME | TIME  → Int32 |
| LTIME | LTIME  → Int64 |
| DATE | DATE  → UInt16 |
| TIME_OF_DAY (TOD) | TOD  → UInt32 |
| LTIME_OF_DAY (LTOD) | LTOD  → UInt64 |
| DATE_AND_TIME (DT) | DT  → Byte[8] |
| LDT | DateTime |
| DTL  Special note: You can only describe the structure completely with an OPC UA client. You have read-only access individual elements of this structure (e.g. "YEAR") | mapped as structure |
| CHAR | CHAR  → Byte |
| WCHAR | WCHAR  → UInt16 |
| STRING  (Code page 1252 or Windows-1252) | STRING  → String |
| WSTRING  (UCS-2; Universal Coded Character Set) | String |
| TIMER | TIMER  → UInt16 |
| COUNTER | COUNTER  → UInt16 |

###### Arrays

A read or write job with OPC UA is always an array access, which means that it always has an index and length. A single tag is a special case of an array (index 0 and length 1). The data type is simply sent repeatedly on the line. For the tags, the "DataType" attribute indicates the basic data type. The attributes "ValueRank" and "ArrayDimensions" show whether or not you are dealing with an array and how large the array is.

###### Data types based on arrays

There are SIMATIC data types for which an OPC UA value is mapped to an array of bytes. An array of these data types is then mapped to a two-dimensional array.

Example: The SIMATIC data type DATE_AND_TIME (DT) is mapped on the OPC UA side to an 8-byte array (Byte[8]), see table above. When you define an array of the SIMATIC data type DATE_AND_TIME (DT), then it is considered as two-dimensional array.

This fact affects the use of system data types such as OPC_UA_NodeAdditionalInfo and OPC_UA_NodeAdditionalInfoExt, for example:

For the data types described above, you must use the system data type OPC_UA_NodeAdditionalInfoExt for multidimensional arrays instead of OPC_UA_NodeAdditionalInfo.

###### Structures

Structures are transferred as ExtensionObject. The S7-1500 server uses binary representation for transmission of the ExtensionObjects over the line; the individual structure elements come one after the other. At the front is the NodeId of the data type; this is used by the client to establish the structure.

For OPC UA Specification <= V1.03, a client has to read, decode and interpret the complete DataTypeDictionary for this (unless it has already learned this library offline through an XML import).

Starting in OPC UA V1.04, the DataTypeDefinition attribute is available for this, which can be read and interpreted more quickly and easily. A client only determines the setup of the structure once, before or during the first access, and then uses this information for the duration of the session.

###### Special SIMATIC data types

SIMATIC data types that are not in the table above and cannot be defined as elements of a structure or PLC data type are not supported by the OPC UA client.

These are, for example, "ANY" or "POINTER" pointers, function block "Block_FB", function "Block_FC" or hardware data type "REMOTE".

The selection of an unsupported data type leads to an error message.

###### Additional information

More details on mapping of basic data types, arrays and structures can be found in the OPC UA Specification Part 6, "Mappings" (see OPC UA BINARY there).

##### Runtime behavior of the OPC UA server (S7-1500, S7-1500T)

###### OPC UA server in operation

The OPC UA server of the S7-1500 CPU starts when you activate the server and download the project to the CPU.

**Behavior in the operating state STOP of the CPU**

An activated OPC UA server remains in operation even if the CPU switches to "STOP". The OPC UA server continues to respond to requests from OPC UA clients.

Server response in detail:

- If you request the values of PLC tags, you will get what were the latest values before the CPU switched to or was set to "STOP".
- If you write values to the OPC UA server, the OPC UA server will accept those values.

  However, the CPU will not process the values because the user program is not executed in "STOP" mode.

  An OPC UA client can nonetheless read the values written at STOP from the OPC UA server of the CPU.

  During restart, the CPU overwrites the values written at STOP with the start of the PLC tags.
- If you call a server method, the error message 16#00AF_0000 (BadInvalidState) is output because the server method (user program) is not running.
- Connections to the OPC UA server remain active during an operating mode transition (STOP > RUN or RUN > STOP). Exception: OPC UA-relevant data is loaded, see next section.

###### Download to the CPU may affect OPC UA server

If you load a CPU with running OPC UA server, you may need to stop and restart the server depending on the loaded objects. In this case, active connections are interrupted and must be re-established once the server restarts.

The duration of the restart depends mainly on the following parameters:

- The scope of the data structure
- The number of variables visible in the OPC UA address space
- The setting for downward compatible data type definition according to OPC UA specification to V1.03 (TypeDictionary enabled)
- The settings for the communication load and minimum cycle time.

  For more information, refer to the following section: [Tips and recommendations](#tips-and-recommendations-s7-1200-s7-1500-s7-1500t)

With CPU FW versions older than V2.8, the OPC UA server was stopped at each download to the CPU and then restarted.

As of FW version V2.8, the behavior of the OPC UA server has been optimized as follows:

- When objects are downloaded in STOP operating state of the CPU, the OPC UA server still always stops and then restarts. STEP 7 does not show a warning in this case.
- When objects are downloaded in RUN operating state of the CPU, the OPC UA server only stops if the downloaded objects are, or could be, OPC UA-relevant. The OPC UA server restarts after re-initialization due to the modified OPC UA data.

  Before OPC-UA-relevant objects are loaded into the CPU and stop the OPC UA server, STEP 7 displays a warning in the preview dialog for loading. You can then decide whether a server restart is compatible for the running process or whether you want to cancel the download. These warnings are only displayed when the OPC UA server is running. If the OPC UA server is not enabled, modified OPC UA data have no influence on the download process.

**Examples**

- You only want to add another code module to the program.   
  Neither data blocks nor inputs, outputs, flags, times or counters are affected.  
  Reaction during loading: A running OPC UA server is not interrupted.
- You want to load a new data module and you have flagged the data module as non-OPC-UA-relevant:  
  Reaction during loading: A running OPC UA server is not interrupted.
- You want to overwrite a data module.  
  Reaction during loading: A warning appears that the server will be restarted.  
  Background: STEP 7 cannot determine whether the changes refer to OPC-UA-relevant data or not.

###### Reading CPU operating mode over OPC UA server

The OPC UA server allows you to read out the CPU mode, see figure below:

![Reading CPU operating mode over OPC UA server](images/132239653003_DV_resource.Stream@PNG-de-DE.png)

In addition to the operating mode of the CPU you can, for example, read out information in the manual (DeviceManual) or firmware version (HardwareRevision).

#### Accessing OPC UA server data (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Client accesses and local accesses to the OPC UA server (S7-1500, S7-1500T)](#client-accesses-and-local-accesses-to-the-opc-ua-server-s7-1500-s7-1500t)
- [Managing write and read rights (S7-1500, S7-1500T)](#managing-write-and-read-rights-s7-1500-s7-1500t)
- [Managing write and read rights for a complete DB (S7-1500, S7-1500T)](#managing-write-and-read-rights-for-a-complete-db-s7-1500-s7-1500t)
- [Read and write access rights for CPU variables and OPC UA tags (S7-1500, S7-1500T)](#read-and-write-access-rights-for-cpu-variables-and-opc-ua-tags-s7-1500-s7-1500t)
- [Consistency of tags (S7-1500, S7-1500T)](#consistency-of-tags-s7-1500-s7-1500t)
- [Write accesses to OPC UA variables from S7-1500 Motion Control. (S7-1500, S7-1500T)](#write-accesses-to-opc-ua-variables-from-s7-1500-motion-control-s7-1500-s7-1500t)
- [MinimumSamplingInterval attribute for tags (S7-1500, S7-1500T)](#minimumsamplinginterval-attribute-for-tags-s7-1500-s7-1500t)
- [Recommendations for client access to the OPC UA server (S7-1500, S7-1500T)](#recommendations-for-client-access-to-the-opc-ua-server-s7-1500-s7-1500t)
- [Export OPC UA XML file (S7-1500, S7-1500T)](#export-opc-ua-xml-file-s7-1500-s7-1500t)

##### Client accesses and local accesses to the OPC UA server (S7-1500, S7-1500T)

An OPC UA server provides a lot of information for OPC UA clients within a network. The following section describes the options for making CPU variables (PLC variables and DB elements) available in the address space of your own OPC UA server.

###### Provide CPU variables via server interfaces in the OPC UA address space

The easiest way to transfer CPU variables automatically into the address space of the OPC UA server:

- Activate the standard SIMATIC server interface in the OPC UA properties of the CPU.

  All CPU variables released for OPC UA are then automatically also available in the OPC UA address space under the name of the CPU.

![Provide CPU variables via server interfaces in the OPC UA address space](images/153913602955_DV_resource.Stream@PNG-en-US.png)

The use of OPC UA server interfaces is more flexible and clearer; you configure the server interfaces in the project tree (below the CPU, "OPC UA Communication folder"). User-defined OPC UA server interfaces allow you to easily map OPC UA tags and CPU variables (local data).

![Provide CPU variables via server interfaces in the OPC UA address space](images/153901095947_DV_resource.Stream@PNG-en-US.png)

The data exchange between OPC UA client and OPC UA server is clearly illustrated in the following example of two S7-1500 CPUs.

Here, an S7-1500 CPU as client writes values to an OPC UA tag of the OPC UA server. The mapping between CPU variable and OPC UA tag makes it look as though the OPC UA client writes a value directly into the CPU variable. For an S7-1500 client CPU, use the "OPC_UA_WriteList" instruction in connection with additionally required instructions for the data exchange.

![Provide CPU variables via server interfaces in the OPC UA address space](images/154670903307_DV_resource.Stream@PNG-en-US.png)

###### Writing CPU tag values directly to an OPC UA tag (setting OPC UA DataValue attributes)

As of firmware version V3.0, S7-1500 CPUs offer, in addition to mapping tags, the possibility to write values directly into local OPC UA tag nodes of the server via the "OPC_UA_WriteList" instruction. Normally, the "OPC_UA_WriteList" instruction in the client program of the CPU is used to write values into OPC UA tags of a remote OPC UA server.

Advantage of using "OPC_UA_WriteList" in the server: In addition to the value, you can provide the OPC UA tag node with the following additional information:

- SourceTimestamp
- StatusCode

OPC UA provides a built-in "DataValue" data type. DataValue is a structure that holds the value (Value) as well as SourceTimestamp and StatusCode as additional information for the value. The DataValue structure is only used by OPC UA services and you cannot write directly in the program of the CPU to the elements of this structure. Write access is only possible via a special use of the "OPC_UA_WriteList" instruction.

**Application options**

CPU variables cannot record a time stamp indicating when a value was last written to the CPU variable. Thus, if you map CPU tags and OPC UA tags via server interfaces, the OPC UA server does not set the SourceTimestamp to the time at which the CPU tag changed but to the time at which the value was "collected" in the server; e.g. by a read service or by sampling in the context of a subscription.

If you write DataValue directly with "OPC_UA_WriteList" into an OPC UA tag node, for example, you can provide a time stamp determined in the program as SourceTimestamp for the value.

**How the OPC_UA_WriteList instruction works in principle for setting DataValues**

The DataValue structure is, for example, modeled as UDT and a tag of this data type is transferred to the "OPC_UA_WriteList" instruction. The instruction then consistently transfers the elements of the tag to the OPC UA tag node.

The value of the "ConnectionHdl" instruction parameter defines the how the "OPC_UA_WriteList" works: "Normal" client instruction or instruction to write to local OPC UA tag nodes. OPC UA clients can read the value with additional information in the latter case and evaluate it accordingly.

The principle is shown in the following figures, once with any client and once with an S7-1500 CPU as OPC UA client. In the case of the S7-1500 CPU client, the assignment of the DataValue elements to the corresponding instruction parameters of the OPC_UA_ReadList instruction is shown. You have full access to all elements of the DataValue structure.

The value of "ConnectionHdl" (-42) of the "OPC_UA_WriteList" instruction causes the server to write to local OPC UA tag nodes.

![Writing CPU tag values directly to an OPC UA tag (setting OPC UA DataValue attributes)](images/154680954123_DV_resource.Stream@PNG-en-US.png)

![Writing CPU tag values directly to an OPC UA tag (setting OPC UA DataValue attributes)](images/154681840139_DV_resource.Stream@PNG-en-US.png)

**Other application options**

If OPC UA clients register with an S7-1500 CPU for value changes (monitored items) in the context of a subscription and you supply the corresponding DataValue with both the value and the additional information mentioned above, then changes to the additional information can also trigger a notification.

**Example**: A binary value changes so fast that it falls back to its original value in the sampling interval (fast change TRUE > FALSE > TRUE). A change of the value is not detected. But the change of the time stamp is detected. Similarly, a notification can be triggered when the StatusCode changes - even without the value changing.

**Constraints**

- OPC UA clients are only allowed to read the OPC UA tag; the "AccessLevel" attribute for read/write permissions must be set accordingly for the OPC UA tag.
- Only OPC UA tags of the user-defined server interfaces can be set locally.
- In the user-defined server interface, there must be no mapping to CPU variables for the directly written OPC UA tags.

  ![Writing CPU tag values directly to an OPC UA tag (setting OPC UA DataValue attributes)](images/153915578507_DV_resource.Stream@PNG-en-US.png)

Details about the usage of the "OPC_UA_WriteList" instruction in the "Set OPC UA-DataValue" context can be found in the corresponding section of the communication instruction help.

###### Setting OPC UA DataValue attributes for arrays and structures

When OPC UA tags of type Structure or Array are set using "OPC_UA_WriteList" for setting OPC UA DataValue attributes, all elements of this array or structure are filled.

You should not model individual elements of structures or arrays additionally as lower-level OPC UA tags. Reason: If you model individual elements of arrays or structures additionally as separate lower-level nodes in the address area of the server, these nodes are **not** automatically filled. For the OPC UA server, these separate nodes are independent of the higher-level OPC UA tag of type Structure or Array, because they are not mapped to CPU tags.

To fill these separately modeled nodes, you must create each individual element as its own DataValue structure in the program.

**Tip**: In order for OPC UA clients to simultaneously learn about changes to relevant nodes in this case, set the values of all OPC UA tags involved in the same OPC_UA_WriteList call.

###### More information

An [application example](https://support.industry.siemens.com/cs/us/en/view/109820694) is provided to assist you on the topic of "setting OPC UA DataValue attributes".

---

**See also**

[Set OPC UA-DataValue with OPC_UA_WriteList (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#set-opc-ua-datavalue-with-opc_ua_writelist-s7-1500)
  
[Read and write access rights for CPU variables and OPC UA tags (S7-1500, S7-1500T)](#read-and-write-access-rights-for-cpu-variables-and-opc-ua-tags-s7-1500-s7-1500t)
  
[Creating a user-defined server interface (S7-1500, S7-1500T)](#creating-a-user-defined-server-interface-s7-1500-s7-1500t)

##### Managing write and read rights (S7-1500, S7-1500T)

###### Enabling PLC tags and DB tags for OPC UA

OPC UA clients can have read and write access to PLC tags and DB tags if the tags are enabled for OPC UA (default setting). For an enabled tag the check box "Accessible from HMI/OPC UA" is activated.

You can change the default setting in the settings of the TIA Portal: Command "Settings > PLC programming > General" in "Options" menu. You will find the corresponding options in the "Block interface/data block elements" area.

The following example shows an array data block:

![Enabling PLC tags and DB tags for OPC UA](images/105751001227_DV_resource.Stream@PNG-en-US.png)

This array can be read completely in one pass by OPC UA clients (see [Addressing nodes](#addressing-nodes-s7-1200-s7-1500-s7-1500t)). The check boxes at "Accessible from HMI/OPC UA" and "Writable from HMI/OPC UA" are activated for all the components of the array.

Result: OPC UA clients can both read and write these components.

###### Removing write rights

If you want to write-protect a tag, deselect the "Writable from HMI/OPC UA" option for that tag. This removes the write right for the OPC UA clients and HMI devices.

Result: Only read access by OPC UA clients and HMI devices is possible. OPC UA clients cannot assign values to this tag and therefore cannot influence execution of the S7 program.

###### Removing write and read rights

To write-protect and read-protect a tag, disable the "Accessible from HMI/OPC UA" option for that tag (checkbox not selected). This makes the OPC UA server remove the tag from its address space. OPC UA clients can no longer see that CPU tag.

Result: OPC UA clients and HMI devices can neither read nor write the tag.

###### Write and read rights of structures

If you remove the read or write right for the component of a structure, the structure or the data block cannot be written or read as a whole.

If you remove read and write rights for individual components of a PLC data type (UDT), the rights will also be removed from any data block based on that data type!

###### Visible in HMI engineering

The option "Visible in HMI Engineering" applies to Siemens engineering tools. If you disable the option "Visible in HMI Engineering" (check mark not set), you can no longer configure the tag in WinCC (TIA Portal).

The option does not have any effect on OPC UA.

###### Rules

- Only allow read access to PLC tags and tags of data blocks in STEP 7 if this is necessary for communication with other systems (controllers, embedded systems or MES).

  You should not enable other PLC tags.
- Only allow write access over OPC UA if write rights are genuinely necessary for specific PLC tags and tags of data blocks.
- If you have reset the "Accessible from HMI/OPC UA" option for all elements of a data block, the data block for an OPC UA client is no longer visible in the address space of the OPC UA server of the S7-1500 CPU.
- You can also prevent access to an entire data block centrally (see [Managing write and read rights for a complete DB](#managing-write-and-read-rights-for-a-complete-db-s7-1500-s7-1500t)). This setting "overrules" the settings for the components in the DB editor.

---

**See also**

What you need to know about OPC UA clients
  
[Read and write access rights for CPU variables and OPC UA tags (S7-1500, S7-1500T)](#read-and-write-access-rights-for-cpu-variables-and-opc-ua-tags-s7-1500-s7-1500t)

##### Managing write and read rights for a complete DB (S7-1500, S7-1500T)

###### Hiding DBs or DB contents for OPC UA clients

You can easily prevent access to a complete data block by an OPC UA client.

With this option, the data of the corresponding DB, including instance DBs of function blocks, remains hidden for OPC UA clients.

In the default setting, data blocks can be read and written from OPC UA clients. You can change this default setting in the settings of the TIA Portal: Command "Settings > PLC programming > General" in "Options" menu. You will find the corresponding option in the "Default settings for new blocks" area.

###### Procedure

Proceed as follows to completely hide a data block for OPC UA clients or to protect a data block from write access from OPC UA clients:

1. Select the data block to be protected in the project tree.
2. Select the "Properties" shortcut menu.
3. Select the "Attributes" area.
4. Select/clear the "DB accessible from OPC UA" checkbox as required.

   ![Procedure](images/105751019147_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Effect on settings in the DB editor**
>
> If you hide a DB using the DB attribute described here, the settings for the components in the DB editor are no longer relevant; individual components can no longer be accessed or written.

###### Tip: Using the overview of all program blocks

If you are using multiple data blocks, it is appropriate to use the detailed overview of the "Program blocks" folder for selective activation or deactivation of the OPC UA accessibility.

Follow these steps:

1. Select the "Program blocks" folder in the project tree.
2. Select the "Overview" command in the "View" menu.
3. Select the "Details" tab.

   An overview of the blocks with their attributes is displayed.
4. Ensure that the "Data block accessible via OPC UA" column is selected.
5. Select only the data blocks that are to be accessible via OPC UA.

   ![Tip: Using the overview of all program blocks](images/126567331467_DV_resource.Stream@PNG-en-US.png)

##### Read and write access rights for CPU variables and OPC UA tags (S7-1500, S7-1500T)

###### Definition of read and write permissions for OPC UA tags (OPC UA-XML)

In the OPC UA information model, the attribute "AccessLevel" regulates access to tags.

AccessLevel is defined bit by bit:

Bit 0 = CurrentRead and Bit 1 = CurrentWrite. The meaning of the bit combinations is as follows:

- AccessLevel = 0: no access
- AccessLevel = 1: read only
- AccessLevel = 2: write only
- AccessLevel = 3: read+write

**Example of the assignment of write and read rights (read+write)**

![Definition of read and write permissions for OPC UA tags (OPC UA-XML)](images/105751164043_DV_resource.Stream@PNG-de-DE.png)

###### Definition of read and write permissions for CPU variables

When you define tags, you specify the access rights using the properties "Accessible from HMI/OPC UA" and "Writable from HMI/OPC UA".

**Example of the assignment of write and read rights**

![Definition of read and write permissions for CPU variables](images/105751172747_DV_resource.Stream@PNG-de-DE.png)

###### Interaction of read and write permissions for imported OPC UA server interfaces

If you have imported an OPC UA server interface and AccessLevel attributes are set in this OPC UA XML file, the write and read rights are defined by the following rule: The least extensive access rights for each setting apply.

**Example**

- AccessLevel = 1 (read only) in the OPC UA server interface
- Both "Accessible from HMI/OPC UA" and "Writable from HMI/OPC UA" are selected in the PLC variable table

Result: This tag can only be read.

###### Rules

If write rights are required:

- AccessLevel = 2 or 3
- "Writable from HMI/OPC UA" enabled

If read rights are required:

- AccessLevel = 1 (AccessLevel 3 is also possible, but misleading. The settings suggests that an OPC UA client has write and read rights)
- "Accessible from HMI/OPC UA" enabled, "Writable from HMI/OPC UA" disabled

If neither read nor write rights are to be granted (no access):

- AccessLevel = 0
- "Accessible from HMI/OPC UA" disabled

  Only one of the two conditions needs to be met to block all access. In this case, review whether the tag in the OPC UA server interface is actually necessary at all.

###### Access table

"Accessible from HMI/OPC UA" must be set if access over OPC UA is to be possible at all. "Writable from HMI/OPC UA" must be set to allow an OPC UA client to write a tag / DB element.

Please see the table for the resulting access right.

Access table

| OPC UA XML | STEP 7 (TIA Portal), for example variable table |  |  |
| --- | --- | --- | --- |
| AccessLevel | Accessible from HMI/OPC UA | Writable from HMI/OPC UA | Resulting access right |
| 0 | x | x | No access |
| x | 0 | x | No access |
| 1 | Enabled | x | Read only |
| 2 | Enabled | Disabled | No access |
| 3 | Enabled | Disabled | Read only |
| 2 | Enabled | Enabled | Write only |
| 3 | Enabled | Enabled | Read+write |

(x = don't care)

---

**See also**

[Consistency of tags (S7-1500, S7-1500T)](#consistency-of-tags-s7-1500-s7-1500t)
  
[Managing write and read rights (S7-1500, S7-1500T)](#managing-write-and-read-rights-s7-1500-s7-1500t)

##### Consistency of tags (S7-1500, S7-1500T)

###### "AccessLevelEx" attribute extends access properties

As of firmware version V2.6, the OPC UA server of the S7-1500 CPU supports not only the attribute "AccessLevel" (see [Read and write access rights for CPU variables and OPC UA tags](#read-and-write-access-rights-for-cpu-variables-and-opc-ua-tags-s7-1500-s7-1500t)) but also the attribute "AccessLevelEx" which, in addition to the already explained bits for read access and write access, provides information on the consistency of a OPC UA tag. The new attribute was introduced with version V1.04 of the OPC UA specification (Part 3, Address Space Model).

###### Reading consistency properties

In the OPC UA information model of the OPC UA server, the attribute "AccessLevel" defines the access.

AccessLevelEx is defined bit by bit; in this case the relevant bits are:

- Bit 0 = CurrentRead
- Bit 1 = CurrentWrite
- Bits 2 to 7 are not relevant for the OPC UA server of an S7-1500 CPU

The meaning of the bit combinations is explained in the section on read and write rights.

The following bits for consistency are also added:

- Bit 8 = NonatomicRead; the bit is set if the tag cannot be read consistently. For read consistency of tags, bit 8=0.
- Bit 9 = NonatomicWrite; is set if the tag cannot be written consistently. For write consistency of tags, or if no write access is granted, bit 9=0.

**Examples**

An OPC UA tag (structure) is readable and writable; but inconsistent for reading and writing access.

Consequently: Bits 0, 1, 8 and 9 are set: AccessLevelEx = "771" (1+2+256+512).

Another structure is read-only.

Consequently: Bits 0 and 8 are set, bit 1 and bit 9 are not set: AccessLevelEx = "257" (1+0+256+0).

###### Handling of the attribute in the server

The "AccessLevelEx" attribute is only available in the OPC UA server. The attribute is not present in a node set file (XML export file).

However, the attribute "AccessLevel", which is exported, includes the information from "AccessLevelEx", see next section.

**Export**

During XML export of the standard SIMATIC server interface, the server sets the "AccessLevel" attribute, which was expanded to 32 bits in V1.04 compared to V1.03, to the value of the "AccessLevelEx" attribute.

**Import**

When importing a node set file (e.g. from an export of a server interface), the S7-1500 CPU sets the attribute "AccessLevelEx" according to its own estimate of the consistency of the imported data type, see next section. The imported value is ignored.

###### Consistency of data types at the server interface

The consistency of tags ("atomicity" in the language usage of OPC UA) within a program cycle of an S7-1500 CPU is ensured at the nodes of the server interface for the following data types:

- BOOL, BYTE, WORD, DWORD, LWORD
- SINT, INT, LINT, DINT, USINT, UINT, ULINT, UDINT
- REAL, LREAL
- DATE, LDT, TIME, LTIME, TIME_OF_DAY, LTIME_OF_DAY, S5TIME
- CHAR, WCHAR
- System data types and hardware data types that are based on the above-mentioned data types are also consistent.

  Example: HW_ANY, derived from UINT (UInt16).

**Tip**: If you browse in the address space of the S7-1500 CPU (e.g. with the OPC UA Client UaExpert), you can find the consistent data types under Types > BaseDataType > Enumeration/Number/String.

Tags of the following data types are **not** consistent ("nonatomic" in the language usage of OPC UA):

- SIMATIC structures are generally not consistent. This means that all tags which, for example, have unknown structures or a UDT data type are not consistent.
- System data types such as DTL, IEC_Counter, IEC_TIMER, etc. are data types that are derived from structures.

**Tip**: If you browse in the address space of the S7-1500 CPU (e.g. with the OPC UA Client UaExpert), you can find data types based on structures under Types > BaseDataType > Structure.

##### Write accesses to OPC UA variables from S7-1500 Motion Control. (S7-1500, S7-1500T)

In addition to the consistency of the data types, the CPU examines the variables of the technology objects for plausibility and validity.

If an OPC UA client writes an invalid or implausible value to a variable, the original value is retained in the variable of the technology object.

Despite an unsuccessful write access, the status "Good" is output.

**Example 1**

Interpolation type of the cyclic cam

The variable "Cam_1".InterpolationSettings.InterpolationMode is of type INT, but may only assume the values 1...2.

If you want to change the variable using OPC UA to an invalid value, for example, 3, then the status code "Good" is output, but the variable is not changed.

**Example 2**

Position the software limit switch at a positioning axis

The position of the positive HW limit switch must be more positive than the position of the negative SW limit switch.

"PosAxis_1".PositionLimits_SW.MaxPosition > "PosAxis_1".PositionLimits_SW.MinPosition

If you want to change the variable using OPC UA to a value that does not meet this condition, then the status code "Good" is output, but the variable is not changed.

Which values are valid for variables of the technology objects can be looked up in the documentation of the technology objects.

##### MinimumSamplingInterval attribute for tags (S7-1500, S7-1500T)

###### MinimumSamplingInterval attribute of tags

In addition to "Value", "DataType" and "AccessLevel", you can also set the "MinimumSamplingInterval" attribute for a tag in the XML file that represents the server address space.

The attribute specifies how fast the server can sample the tag value.

The OPC UA server of the S7-1500 CPU handles the values for MinimumSamplingInterval as follows:

- Negative values and values greater than 4294967 are set to -1; this means: The minimum sampling rate is indeterminate. The server does not specify how fast the tag value can be sampled.
- Decimal numbers are rounded to three decimal places.

##### Recommendations for client access to the OPC UA server (S7-1500, S7-1500T)

###### High performance in line with application

OPC UA is designed for the transfer of a high volume of data within a short period of time. You can increase the performance significantly if you do not access individual PLC tags, but rather read and write arrays and structures as a whole.

It is fastest to access arrays. Therefore, you should combine the data for OPC UA clients into arrays.

**Recommendations for access to the OPC UA server by the OPC UA client**

- For one-off or infrequent data access, use standard read/write access.
- For cyclic access to small amounts of data (up to ca. every 5 seconds), use subscriptions.

  Optimize the settings for the smallest publishing interval and the smallest sampling interval at the OPC UA server.
- If you access specific tags regularly (recurring access), you should use the functions "RegisteredRead" and "RegisteredWrite".

Allow a greater communication load for the PLC by increasing the value for "Cycle load due to communication". Make sure that your application still works properly with the changed settings.

###### Procedure for creating an array DB

You can create arrays for example in global data blocks, in the instance data block of a function block or as an array DB . The following sections describe how to create an Array-DB.

To create a data block with an array (array data block), follow these steps:

1. Select the CPU with the OPC UA server in the project tree.
2. Double-click "Program blocks".
3. Double-click "Add new block".
4. Click "Data block".
5. Select a unique name for the data block and accept the name that is already entered.
6. Select the "Array DB" entry from the drop-down list for "Type".
7. Select the data type for the individual components of the array from the drop-down list for "Array data type".
8. Enter the high limit of the array for "Array limit".
9. Click "OK".

##### Export OPC UA XML file (S7-1500, S7-1500T)

###### Generating an OPC UA export file

The OPC Foundation has specified a standard XML-based format for describing information models. It allows the information model of an OPC UA server to be provided to a client in advance, or information models can be downloaded to an OPC UA server. A file in this format is called a nodeset file because it describes an information model as a set of nodes.

With STEP 7 (TIA Portal), you can easily export the standard SIMATIC information model of the S7-1500 CPU as a server to an OPC UA XML file (node set file); including the following elements that you have enabled for OPC UA:

- CPU variables (PLC variables and DB elements)
- Function blocks with their inputs/outputs

Elements that exist in the CPU but are not used in the program do not appear in the OPC UA XML file after the export. Examples of such unused elements are:

- UDTs that are not mapped to a data block
- Function blocks with inputs/outputs without assigning inputs/outputs to CPU variables

You use the OPC UA XML file for the offline configuration of an OPC UA client. The OPC UA XML file is structured according to the OPC UA specification and acts as a standard SIMATIC server interface.

To create and export the OPC UA XML file, follow these steps:

1. Select the CPU. Click on the CPU symbol (for example in the network view).
2. Click "General > OPC UA > Server > Export" in the properties of the CPU.
3. Click "Export OPC UA XML file".
4. Select the directory in which you want to save the export file.
5. Choose a new name for the file or keep the name that is already entered.
6. Click "Save".

> **Note**
>
> As of STEP 7 (TIA Portal) V15.1, server methods are contained in the OPC UA export file (node set) together with their input and output parameters.

###### Exporting all array elements separately

If the "Export all array elements as separate nodes" option is selected in the CPU properties under "OPC UA > Server > Export", the OPC UA XML file contains all elements of arrays as individual XML elements. In addition, the arrays themselves are each described in an XML element in the XML file.

If an array contains many array elements, the XML file can be very large.

###### Tip

The following FAQ contains a converter with which you can convert the export file into CSV format. You then obtain a list of the variables of the CPU that can be accessed by OPC UA.

You can find the FAQ on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109742903).

#### Configuring the OPC UA server (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Enabling the OPC UA server (S7-1500, S7-1500T)](#enabling-the-opc-ua-server-s7-1500-s7-1500t)
- [License for OPC UA (S7-1500, S7-1500T)](#license-for-opc-ua-s7-1500-s7-1500t)
- [Access to the OPC UA server (S7-1500, S7-1500T)](#access-to-the-opc-ua-server-s7-1500-s7-1500t)
- [General settings of the OPC UA server (S7-1500, S7-1500T)](#general-settings-of-the-opc-ua-server-s7-1500-s7-1500t)
- [Settings of the server for subscriptions (S7-1500, S7-1500T)](#settings-of-the-server-for-subscriptions-s7-1500-s7-1500t)
- [Handling client and server certificates (S7-1500, S7-1500T)](#handling-client-and-server-certificates-s7-1500-s7-1500t)
- [Secure Channel - Select Security Policies (S7-1500, S7-1500T)](#secure-channel---select-security-policies-s7-1500-s7-1500t)
- [Generating server certificates with STEP 7 (S7-1500, S7-1500T)](#generating-server-certificates-with-step-7-s7-1500-s7-1500t)
- [User authentication (S7-1500, S7-1500T)](#user-authentication-s7-1500-s7-1500t)
- [Users and roles with OPC UA function rights (S7-1500, S7-1500T)](#users-and-roles-with-opc-ua-function-rights-s7-1500-s7-1500t)
- [Diagnostic settings of the server (S7-1500, S7-1500T)](#diagnostic-settings-of-the-server-s7-1500-s7-1500t)

##### Enabling the OPC UA server (S7-1500, S7-1500T)

###### Requirement

- If you use **certificates** for secured communication, e.g. HTTPS, Secure OUC, OPC UA, make sure that the modules involved have the **current time of day and the current date**. Otherwise, the modules evaluate the used certificates as invalid and secure communication does not work.
- You have acquired a runtime license for the operation of the OPC UA functions, see [License for OPC UA](#license-for-opc-ua-s7-1500-s7-1500t).

###### Commissioning an OPC UA server

By default, the OPC UA server of the CPU is not enabled for reasons of security: OPC UA clients have neither write nor read access to the S7-1500 CPU.

Follow these steps to activate the OPC UA server of the CPU:

1. Select the CPU. Click on the CPU symbol (for example in the network view).
2. Click "OPC UA > Server" in the properties of the CPU.
3. Activate the OPC UA server of the CPU.
4. Confirm the security notes.
5. Go to the CPU properties, select "Runtime licenses" and set the runtime license acquired for the OPC UA server.
6. Compile the project.
7. Download the project to the CPU.

   The OPC UA server of CPU now starts.

###### Settings remain stored

If you have already enabled the server and made settings, those settings are not lost if the server is disabled. The settings are saved as before and are available when you enable the server again.

###### Application name

The application name is the name of the OPC UA application and applies to the server and the client. The name is displayed under "OPC UA > General":

- The default for the application name is: "SIMATIC.S7-1500.OPC-UA.Application:PLC_1".
- The default consists of "SIMATIC.S7-1500.OPC-UA.Application:" and the name of the CPU selected under "General > Product information > Name", in this case "PLC_1".
- The OPC UA server uses this application name to identify itself to a communication partner (OPC UA client), for example, when an OPC UA client uses the discovery service to detect accessible servers.
- The displayed application name uses the OPC UA client of the CPU when connecting to an OPC UA Server. This means that the CPU enters this application name automatically as "ApplicationName" for the instruction "OPC_UA_Connect" (tag of type "OPC_UA_SessionConnectInfo" at the parameter "SessionConnectInfo" of the instruction "OPC_UA_Connect").

  When you program the instruction "OPC_UA_Connect" you must therefore assign an empty string to the "ApplicationName". You can use the application name, for example, to identify the client and its sessions (SessionNames) for diagnostic purposes.

If you have activated the server, you can also use a different name that is meaningful in your project and that fulfills the requirements of your project, e.g. for worldwide uniqueness.

The example below originates from UaExpert:

![Application name](images/105751492235_DV_resource.Stream@PNG-de-DE.png)

###### Changing the application name

To change the application name, follow these steps:

1. Select the CPU. Click on the CPU symbol (for example in the network view).
2. Click "OPC UA > General" in the properties of the CPU.
3. Enter a meaningful name.

Please note that the application name is also entered on the certificate (Subject Alternative Name) and you may have to generate an existing certificate again after changing the application name.

##### License for OPC UA (S7-1500, S7-1500T)

###### Runtime licenses

A license is required to run the OPC UA server of the S7-1500 CPU. The type of license required depends on the performance of the respective CPU. The following license types are differentiated:

- SIMATIC OPC UA S7-1500 small (required for CPU 1511, CPU 1512, CPU 1513, ET 200SP CPUs, CPU 1515SP PC)
- SIMATIC OPC UA S7-1500 medium (required for CPU 1515, CPU 1516, Software Controller CPU 1507, CPU 1516pro-2PN)
- SIMATIC OPC UA S7-1500 large (required for CPU 1517, CPU 1518)

The required license type is displayed under "Properties > General > Runtime licenses > OPC-UA > Type of required license":

![Runtime licenses](images/127586505483_DV_resource.Stream@PNG-en-US.png)

To confirm purchase of the required license, follow these steps:

1. Click "Runtime licenses > OPC UA" in the properties of the CPU.
2. Select the required license from the "Type of purchased license" drop-down list.

##### Access to the OPC UA server (S7-1500, S7-1500T)

###### Server addresses

The OPC UA server of the S7-1500 CPU can be reached over all integrated PROFINET interfaces of the CPU (firmware V2.0 and higher).

Direct access to the OPC UA server of the CPU over the backplane bus of the automation system is not possible via CPs under the following conditions:

- Configuration with TIA Portal Version V16 or higher, S7-1500 CPU firmware version 2.8 or higher and CP 1543-1 firmware version V2.2 or higher.

  For configuration, see [Access to OPC UA applications](#access-to-opc-ua-applications-s7-1200-s7-1500-s7-1500t).

Direct access to the OPC UA server of the CPU over the backplane bus of the automation system is not possible via CMs.

With SIMATIC S7-1500 SW controllers, access to the OPC UA server is possible via PROFINET interfaces that are assigned to the software PLC.

Additional access options of SW controllers are described in the following application example: [Internal and external OPC UA connection via the virtual Ethernet interface of the software controller V2.5 or higher](https://support.industry.siemens.com/cs/ww/en/view/109760541).

Example for URLs (Uniform Resource Locator) that can be used to set up connections to the OPC UA server of the CPU:

![Server addresses](images/105751402507_DV_resource.Stream@PNG-en-US.png)

The URLs are structured as follows:

- Protocol identifier **"**opc.tcp://"
- IP address

  - 192.168.178.151

    The IP address at which the OPC UA server can be accessed from the Ethernet subnet 192.168.178.
  - 192.168.1.1

    The IP address at which the OPC UA server can be accessed from the Ethernet subnet 192.168.1.
- TCP Port number

  - Default: 4840 (standard port)

    The port number can be changed under "OPC > UA > Server > Port".

###### Dynamic IP addresses

In the example below, the IP address for the PROFINET interface [X2] has not yet been specified.

![Dynamic IP addresses](images/105751325835_DV_resource.Stream@PNG-en-US.png)

The placeholder "<dynamically>" appears in the table.

The IP address of this PROFINET interface is set later on the device, e.g. via the display of the CPU.

###### Activating the standard SIMATIC Server interface

If the "Enable standard SIMATIC server interface" option is selected, the OPC UA server of the CPU provides the enabled PLC tags and server methods to the clients, as was specified by SIEMENS in the self-defined namespace.

This option is selected in the default setting.

Leave the option selected so that OPC UA clients can automatically connect to the OPC UA server of the CPU and exchange data.

If you do not select this option, you must add the server interface by entering the "OPC UA communication" entry in the project tree. This interface is then used as OPC UA server interface, see [OPC UA server interface configuration](#opc-ua-server-interface-configuration-s7-1500-s7-1500t).

> **Note**
>
> **General device information is readable even with deactivated standard SIMATIC server interface**
>
> Even if you disable the standard SIMATIC server interface, OPC UA clients can read general device information about the OPC UA server of the CPU.
>
> Examples of such device information: DeviceManual, DeviceRevision, OrderNumber. In this case, however, all objects of the application program remain invisible to clients.
>
> If you want to prevent that this device information is not visible, you have to disable the OPC UA server of the CPU.

##### General settings of the OPC UA server (S7-1500, S7-1500T)

###### TCP port for OPC UA

By default, OPC UA uses TCP port 4840. You can, however, select a different port. Entries from 1024 to 49151 are possible. You must, however, make sure that there are no conflicts with other applications. OPC UA clients must use the selected port when establishing a connection.

In the example below, port 48400 is selected:

![TCP port for OPC UA](images/105751416971_DV_resource.Stream@PNG-en-US.png)

###### Settings for sessions

- Maximum timeout for sessions

  In this field, you specify the maximum time period before the OPC UA server closes a session without data exchange.

  Possible values between 1 and 600000 seconds.
- Maximum number of OPC UA sessions

  In this field, you specify the maximum number of sessions the OPC UA server starts and simultaneously operates.

  The maximum number of sessions is dependent on the performance capability of the CPU. Each session ties up resources.

###### Maximum number of registered nodes

In this field, you specify the maximum number of nodes the OPC UA server registers.

The maximum number of registered nodes depends on the capacity of the CPU and is displayed when you configure the field content (place cursor in field). Each registration ties up resources.

> **Note**
>
> **No error message following attempt to register more than the configured maximum number of registrable nodes**
>
> If a client tries to register more nodes during runtime than the configured maximum number, the server of the S7-1500 CPU only registers the configured maximum number. Starting from the configured maximum number of registrable nodes, the server returns the regular string node IDs unchanged to the client so that the speed advantage gained by registration for these nodes is lost. The client does not receive an error message.
>
> When configuring, make sure you have a sufficient reserve by taking into account the maximum number of nodes that can be registered (for example, using the technical data of the CPU).

###### Additional information

Details on which ports are used by the various services for data transfer via TCP and UDP, and what are the points to note when using routers and firewalls can be found in the [FAQ](https://support.industry.siemens.com/cs/ww/en/view/8970169).

###### Backward compatible data type definitions according to OPC UA specification ≤ V1.03

The OPC UA specification (<= V1.03) defines mechanisms in order to read out data type definitions, for example for user-defined structures (UDTs), from a server by means of the TypeDictionaries.

In the OPC UA server properties of the CPU, you can set whether the CPU generates these backward compatible data type definitions according to the OPC UA specification ≤ V1.03 for the standard SIMATIC server interface or not.

Because TypeDictionaries are complex and result in large OPC UA XML files which the client has to interpret, a simpler solution was introduced with OPC UA Specification V1.04 (attribute "DataTypeDefinition" at the data type node). If your client supports the OPC UA specification V1.04 or higher, then disable the option "Backward compatible data type definitions according to OPC UA specification ≤ V1.03".

Advantages of the data type definitions according to OPC UA specification as of V1.04:

- The server starts faster
- The memory is used more efficiently
- The "Browse" function is faster

##### Settings of the server for subscriptions (S7-1500, S7-1500T)

###### Subscription instead of cyclic queries

An alternative to cyclic queries for a PLC tag (polling) is to monitor this value. Use a Subscription: The server informs the client if the value of PLC tags changes. See "The OPC UA client".

One server usually monitors a large number of PLC values. For this reason, the server sends notifications to the client at regular intervals containing the new values of the PLC tags.

Advantages of subscriptions:

- The server starts faster
- The memory is used efficiently

**How frequently does the server send notifications?**

When a Subscription is set up, the OPC UA client specifies the intervals at which it wants to be sent the new values in the event of changes. To limit the communication load through OPC UA, set a minimum interval for the messages. For this purpose, use the parameters for the minimum publishing interval and the minimum sampling interval.

![Subscription instead of cyclic queries](images/114399870091_DV_resource.Stream@PNG-en-US.png)

###### Minimum publishing interval

With "Minimum publishing interval", you set the time intervals at which the server sends a message to the client with the new values in the event of changes.

250 ms is used as the "Minimum sampling interval" in the figure below. The value 200 ms is entered as the "Minimum publishing interval".

![Minimum publishing interval](images/105751541515_DV_resource.Stream@PNG-en-US.png)

In the example, following a value change the OPC UA server will send a new message every 200 ms if the OPC UA client requests an update.

If the OPC UA client requests an update every 1000 ms, the OPC UA server will only send a message with the new values once every 1000 ms (one second).

If the OPC UA client requests an update every 100 ms, the server will still only send a message every 200 ms (minimum publishing interval).

###### Minimum sampling interval

With "Minimum sampling interval", you set the time intervals at which the OPC UA server records the value of a CPU tag and compares it with the previous value to detect any changes.

If the sampling interval is selected smaller than the publishing interval and an OPC UA client requests a high sampling rate for certain PLC tags, two or more values may be measured during each publishing interval.

In this case, the OPC UA server writes the value changes into the queue and sends all value changes to the client after the completion of the publishing interval. If more value changes occur in the publishing interval than fit in the queue, the OPC UA server overwrites the oldest values (depending on the set "Discard Policy" of the client subscribing to the data, the option "Discard Oldest" has to be activated in this case). The most recent values are sent to the client.

###### Maximum number of monitored elements (monitored items)

In this field, you specify the maximum number of elements that the OPC UA server of the CPU simultaneously monitors for a value change.

The monitoring ties up resources. The maximum number of monitored elements is dependent on the utilized CPU.

###### Additional information

Information about the system limits of the OPC UA server of the S7-1500 CPUs (firmware V2.0 and V2.1) regarding subscriptions, sampling intervals and publishing intervals can be found in the following [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109755846).

When using subscriptions, certain status codes of errors provide information on the error that occurred. For information on causes and remedies for status codes of OPC UA client that appear, see the list of error codes in the online help of Step 7 (TIA Portal) or in the following [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109755860).

---

**See also**

[Rules for subscriptions (S7-1200, S7-1500, S7-1500T)](#rules-for-subscriptions-s7-1200-s7-1500-s7-1500t)
  
[Subscription diagnostics (S7-1500, S7-1500T)](#subscription-diagnostics-s7-1500-s7-1500t)

##### Handling client and server certificates (S7-1500, S7-1500T)

A secure connection between the OPC UA server and an OPC UA client is only established when the server can prove its identity to the client. This is done with the server certificate.

###### Certificate of the OPC UA server

When you have activated the OPC UA server and have confirmed the security prompts, STEP 7 automatically generates the certificate for the server and saves it in the local certificate directory of the CPU. You can view and manage this directory with the local certificate manager of the CPU (exporting or deleting certificates).

The figure below shows the local certificate manager of the CPU with the automatically generated certificate for the OPC UA server:

![Certificate of the OPC UA server](images/105751445899_DV_resource.Stream@PNG-en-US.png)

Alternatively, you can also generate a server certificate yourself.

The certificate of the server is transferred from the server to the client during establishment of a connection. The client checks the certificate.

###### The client user decides whether the server certificate is to be trusted.

The user at the client side now has to decide whether the server certificate is to be trusted. If the user trusts the server certificate, the client stores the server certificate in its directory containing the trusted server certificates.

The following example shows a dialog of the client "UA Sample Client". When the user clicks the "Yes" button, the client trusts the server certificate:

![The client user decides whether the server certificate is to be trusted.](images/105751509643_DV_resource.Stream@PNG-de-DE.png)

###### Where does a client certificate come from?

**Client of the S7-1500**

If you are using the OPC UA client of an S7-1500 CPU (OPC UA client enabled), you can create certificates for these clients with STEP 7 V15 and higher.

1. In the project tree, select the CPU you want to use as a client.
2. Double-click "Device configuration".
3. In the properties of the CPU, click "Protection & Security > Certificate manager".
4. Double-click "<Add new>" in the "Device certificates" table.

   STEP 7 opens a dialog.
5. Click the "Add" button.
6. Select the "OPC UA client" entry from the "Usage" list.

   Note:

   The IP addresses under which the CPU can be accessed in your system must be entered under "Subject Alternative Name (SAN)".

   You must therefore configure the IP interfaces of the CPU before you generate a client certificate.
7. Click "OK".

   STEP 7 now shows the client certificate in the "Device certificates" table.
8. Right-click this line and select the "Export certificate" entry from the shortcut menu.
9. Select a directory where you will store the client certificate.

**Clients of other manufacturers**

When you use UA clients from manufacturers or the OPC Foundation, a client certificate is generated automatically during installation or upon the first program call. You have to import these certificates via the global certificate manager in STEP 7 and use them for the corresponding CPU (as shown above).

When you program an OPC UA client yourself, you can have the certificates generated by the program; see the section "Instance certificate for the client". Alternatively, you can generate certificates with tools, for example with OpenSSL or the certificate generator of the OPC Foundation:

- The procedure for OpenSSL is described here: "Generating PKI key pairs and certificates yourself".
- Working with the certificate generator of the OPC Foundation is described here: "Creating self-signed certificates".

###### Announcing client certificates to the server

You need to send client certificates to the server to allow a secure connection to be established.

To do this, follow these steps:

1. Select the "Use global security settings for certificate manager" option in the local certificate manager of the server. This makes the global certificate manager available.

   You will find this option under "Protection & Security > Certificate manager" in the properties of the CPU that is acting as server.

   If the project is not yet protected, select "Security settings > Settings" in the STEP 7 project tree, click the "Protect this project" button and log on.

   The "Global security settings" item is now displayed under "Security settings" in the STEP 7 project tree.
2. Double click "Global security settings".
3. Double click "Certificate manager".

   STEP 7 opens the global certificate manager.
4. Click on the "Trusted certificates" tab.
5. Right-click in the tab on a free area (not on a certificate).
6. Select the "Import" command from the shortcut menu.

   The dialog for importing certificates is displayed.
7. Select the client certificate that the server is to trust.
8. Click "Open" to import the certificate.

   The certificate of the client is now contained in the global certificate manager.

   Note the ID of the client certificate just imported.
9. Click the "General" tab in the properties of the CPU that is acting as server.
10. Click "OPC UA > Server > Security > Secure Channel".
11. Scroll down in the "Secure Channel" dialog to the section "Trusted clients".
12. Double-click in the table on the empty row with "<add new>". A browse button is displayed in the row.
13. Click this button.
14. Select the client certificate that you have imported.
15. Click the button with the green check mark.
16. Compile the project.
17. Load the configuration onto the S7-1500 CPU.

**Result**:

The server now trusts the client. If the server certificate is also considered trusted, the server and client can establish a secure connection.

###### Accepting client certificates automatically

When you select the option "Automatically accept all client certificates during runtime" (below the "Trusted clients" list), the server automatically accepts all client certificates.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Setting after commissioning**  In order to avoid security risks, deactivate the "Automatically accept client certificates during runtime" option again after commissioning. |  |

---

**See also**

Secure transfer of messages
  
[Generating server certificates with STEP 7 (S7-1500, S7-1500T)](#generating-server-certificates-with-step-7-s7-1500-s7-1500t)

##### Secure Channel - Select Security Policies (S7-1500, S7-1500T)

While data exchange between the OPC UA client and OPC UA server takes place on the application layer via OPC UA sessions, the communication layer with its "Secure channel" provides integrity and confidentiality protection.

Security policies in the sense of OPC UA summarize all security settings of an endpoint. Security policies specify, under an appropriate name, a set of security algorithms and key lengths that are used for a secure channel. A connection can only be established if the OPC UA client and OPC UA server support the same security policy.

Example: "Basic256Sha256 - Sign & Encrypt" means: Secure endpoint, supports a series of algorithms for 256-bit hashing and 256-bit encryption.

Security policies are derived from security profiles, see OPC UA Specification Part 7 (Profiles).

###### Configuring security settings of the server

The figure below shows the available server security settings for signing and encrypting messages.

![Configuring security settings of the server](images/159334936331_DV_resource.Stream@PNG-en-US.png)

By default, a server certificate is created that uses SHA256 signing. The following security policies are possible:

- None  
  Unsecured end point

  > **Note**
  >
  > **Disabling security policies you do not want**
  >
  > If you have enabled all security policies in the secure channel settings of the S7-1500 OPC UA server (default setting) – thus, also the end point "None" (no security) – unsecured data traffic (neither signed nor encrypted) between the server and client is also possible. The identity of the client remains unknown with "No security". Each OPC UA client can then connect to the server irrespective of any subsequent security settings.
  >
  > When configuring the OPC UA server, make sure that only security policies that are compatible with the security concept of your machine or plant are selected. All other security policies should be disabled.
  >
  > Recommendation: If possible, use the setting "Basic256Sha256".
- Basic128Rsa15 - Sign (deprecated)   
  Secure endpoint supports a number of algorithms that use the hash algorithm RSA15 and 128-bit encryption.  
  This endpoint protects the integrity of the data by signing it.
- Basic128Rsa15 - Sign & Encrypt (deprecated)   
  Secure endpoint, supports a range of algorithms that use the RSA15 hash algorithm and 128-bit encryption.  
  This endpoint protects the integrity and confidentiality of data by signing and encrypting it.
- Basic256Rsa15 - Sign (deprecated)   
  Secure endpoint, supports a series of algorithms that use the hash algorithm RSA15 and 256-bit encryption.  
  This endpoint protects the integrity of the data through signing.
- Basic256Rsa15 - Sign & Encrypt (deprecated)  
  Secure endpoint, supports a series of algorithms that use the hash algorithm RSA15 and 256-bit encryption.  
  This endpoint protects the integrity and confidentiality of the data through signing and encrypting.
- Basic256Sha256 - Sign  
  Secure endpoint, supports a series of algorithms for 256-bit hashing and 256-bit encryption.   
  This endpoint protects the integrity of the data through signing.
- Basic256Sha256 - Sign & Encrypt  
  Secure endpoint, supports a series of algorithms for 256-bit hashing and 256-bit encryption.  
  This endpoint protects the integrity and confidentiality of the data through signing and encryption.
- Aes128_Sha256_RsaOaep - Sign

  Secure endpoint, supports a range of algorithms for 128-bit encryption and 256-bit hashing. All certificates must use at least Sha256 signatures. This endpoint protects the integrity of the data through signing.

  For average security requirements. PKI infrastructure required.
- Aes128_Sha256_RsaOaep - Sign & Encrypt  
  Secure endpoint, supports a range of algorithms for 128-bit encryption and 256-bit hashing. All certificates must use at least Sha256 signatures. This endpoint protects the integrity and confidentiality of data by signing and encrypting it.
- Aes256_Sha256_RsaPss - Sign

  Secure endpoint, supports a range of algorithms for 256-bit encryption and 256-bit hashing. All certificates must use at least Sha256 signatures. This endpoint protects the integrity of the data by signing it.  
  For high security requirements. PKI infrastructure required.
- Aes256_Sha256_RsaPss - Sign & Encrypt

  Secure endpoint, supports a range of algorithms for 256-bit encryption and 256-bit hashing. All certificates must use at least Sha256 signatures. This endpoint protects the integrity and confidentiality of data by signing and encrypting it.  
  For high security requirements. PKI infrastructure required.

To enable the security setting, click the check box in the relevant line.

> **Note**
>
> If you use the settings "Basic256Sha256 -Sign" and "Basic256Sha256 -Sign & Encrypt", the OPC UA server and OPC UA clients must use "SHA256"-signed certificates.
>
> For the settings "Basic256Sha256 -Sign" and "Basic256Sha256 -Sign & Encrypt", the certificate authority of STEP 7 automatically signs the certificates with "SHA256".

###### "No Security" security policy and authentication via user name and password

You can set the following combination:

Security policy = "No Security" and authentication via user name and password.

- The OPC UA server of the S7-1500 supports this combination. OPC UA clients can connect and encrypt the authentication data or not.
- OPC UA client of the S7-1500 CPU also supports this combination: However, in runtime it only connects if it can send the authentication data encrypted via cable!

##### Generating server certificates with STEP 7 (S7-1500, S7-1500T)

The description below shows the procedure for generating new certificates with STEP 7 and applies in principle to various uses of the certificates. STEP 7 sets the appropriate purpose - in this case "OPC UA Client & Server" - depending on which area of the CPU properties is used to start the following dialog.

Recommendation: To use the full functionality for the security of the OPC UA server, use the global security settings.

The global security settings are enabled in the CPU properties under "Protection & Security > Certificate manager".

###### Customizing server certificates

STEP 7 automatically generates a certificate for the OPC UA server of the S7-1500 when you activate the server (see "[Activating the OPC UA server](#enabling-the-opc-ua-server-s7-1500-s7-1500t)"). In the process STEP 7 uses the default values for the parameters of the certificate. If you want to change the parameters, follow these steps:

1. Click the Browse button under "General > OPC UA > Server > Security > Secure channel > Server certificate" in the properties of the CPU. A dialog is displayed that shows the certificates available locally.
2. Click the "Add" button.
3. The dialog for generating new certificates is displayed (figure below). The values for an example are already entered:

   ![Customizing server certificates](images/105751518347_DV_resource.Stream@PNG-en-US.png)
4. Use other parameters if this is necessary in accordance with the security specifications in your company or your customer.

###### Explanation of fields for certificate generation

- CA

  Select whether the certificate is to be self-signed or signed by one of the CA certificates of the TIA Portal. The certificates are described under "Certificates with OPC UA". If you want to generate a certificate that is to be signed by one of the CA certificates of the TIA-Portal, the project must be protected and you must be logged in as a user with all the required function rights. Further information can be found under "Basics of user administration in the TIA Portal".
- Certificate holder

  The default setting always consists of the name of the project and "\OPCUA-1". In the example, the project name is "PLC1". In the properties of the CPU set the project name under "General > Project information" > Name". Keep the default or enter a different name that is more meaningful for the OPC-UA server under "Certificate holder".
- Signature

  Here you select the hash and encryption process that is to be used when signing the server certificate. The following entries are available:

  - "sha1RSA",
  - "sha256RSA".
- Valid from

  Here you enter the date and time for the beginning of the validity of the server certificate.
- Valid until

  Here you enter the date and time for the end of the validity of the server certificate. Ensure that the certificate is valid not only for one year or a few years. In the example the certificate is valid for 30 years. However, for reasons of security you should renew the certificate at much shorter intervals. The long period of validity gives you the opportunity to decide when a suitable moment would be, for example, when the system is being serviced.
- Usage

  The default is "OPC UA client & server". Keep this default for the OPC UA server. The "Create a new certificate" dialog can be called from several points in STEP 7. If, for example, you call this dialog for the Web server of the CPU, "Web server" is entered under "Usage". The following entries are available in the Usage drop-down list:

  - "OPC UA client"
  - "OPC UA client & server"
  - "OPC UA server"
  - "TLS"
  - "Web server"
- Subject Alternative Name (SAN)

  The following is entered in the example above: "URI:urn:SIMATIC.S7-1500.OPC-UAServer:PLC1,IP:192.168.178.151,IP:192.168.1.1". This URI must be correctly entered because it is checked against the communicated application description.

  The following entry would also be valid: "IP: 192.168.178.151, IP: 192.168.1.1". The important thing here is that the IP addresses via which the OPC UA server of the CPU can be accessed are entered here.

  See "[Access to the OPC UA server](#access-to-the-opc-ua-server-s7-1500-s7-1500t)".

  This allows OPC UA clients to verify whether a connection to the OPC UA server of the S7-1500 is really to be established or whether in fact an attacker is trying to send manipulated values from another PC to the OPC UA client.

##### User authentication (S7-1500, S7-1500T)

###### Types of user authentication

For the OPC UA server of the S7-1500, you can set what authentication is required for a user of the OPC UA client wishing to access the server.

You have the following options:

- **Guest authentication**

  The user does not have to prove their authorization (anonymous access). The OPC UA server does not check the authorization of the client user

  For CPUs up to firmware version V3.0: If you want to use this type of user authentication, select the "Enable guest authentication" option under "OPC UA > Server > Security > User authentication".

  For CPUs as of firmware version V3.1: Use the local user administration to realize the guest authentication via the "Anonymous" user.   
  See: [Settings for users and roles](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#settings-for-users-and-roles-s7-1500)

  > **Note**
  >
  > To increase security, you should only allow access to the OPC UA server with user authentication.
- **User name and password authentication**

  The user has to prove their authorization (no anonymous access). The OPC UA server checks whether the client user is authorized to access the server. Authorization is given by the user name and the correct password.

  For CPUs up to firmware version V3.0: If you want to use this type of user authentication, proceed as follows:

  - Select the "Enable user name and password authentication" option under "OPC UA > Server > Security > User authentication".
  - Deactivate the guest authentication.
  - Enter the user in the "User management" table.

    To do so, click the "<Add new user>" entry. A new user is created with an automatically assigned name. You can edit the user name and enter the password for the user name. You can add a maximum of 21 users.

  For CPUs as of firmware version V3.1: Use the local user administration.
- **Additional user administration via the security settings of the project**

  For CPUs up to firmware version V3.0, there is the "Enable additional user management via project security settings" option. You can find this setting under the general OPC UA settings (CPU properties: OPC UA > General). If you select this option, the user management for the open project will also be used for user authentication for the OPC UA server: The same user names and passwords are then valid in OPC UA as in the current project.

  Proceed as follows to activate user management for the project:

  - Click "Security settings > Settings" in the project tree.
  - Click the "Protect this project" button.
  - Enter your user name and your password.
  - Enter additional users under "Security settings > Users and roles".

  If you configure an additional OPC UA server in your project and the same users must access it, also select the option "Activate additional user administration via the security settings of the project". Repeated or local input of user names and passwords is then unnecessary.

###### Transfer of user authentication via the secure channel

In OPC UA, identification data for user authentication, such as user name and password, is transferred with a separate security policy. This security policy is referred to as the "UserTokenPolicy".

Regardless of the configured security policies for the secure channel, an OPC UA client selects an appropriate "UserTokenPolicy" during connection establishment when user authentication is required. This UserTokenPolicy ensures that a UserIdentityToken (e.g. user name and password) is always transferred with adequate security settings.

The OPC UA client is then able to transfer the user name and password with encryption if there is "No security" for the secure channel based on the configured security policy. For information on the process of establishing a secure connection in OPC UA, see [Secure transfer of messages](#secure-transfer-of-messages-s7-1200-s7-1500-s7-1500t).

---

**See also**

Editing the security settings of the OPC UA server.
  
[User authentication (S7-1500, S7-1500T)](#user-authentication-s7-1500-s7-1500t-1)
  
[Users and roles with OPC UA function rights (S7-1500, S7-1500T)](#users-and-roles-with-opc-ua-function-rights-s7-1500-s7-1500t)

##### Users and roles with OPC UA function rights (S7-1500, S7-1500T)

The following options for user authentication use central project settings for project users:

- For the server:

  For configuration of CPU properties (OPC UA > Server > Security > User authentication). Option: "Enable additional user administration via the security settings of the project"
- For the client:

  For configuration of client interface ("Configuration" tab, "Security"). Option: "User (TIA Portal - security settings)"

###### Requirement

Before you can edit the security settings, the project must be protected and you must be logged on with sufficient rights, for example as administrator.

###### Settings in the project tree > "Security settings"

You access the central user settings and roles in the protected project in the project tree under "Security settings". Here, you centrally define users with their user name, password and assigned roles. In turn, the roles are assigned, in turn, to the corresponding function rights. You can simply use these settings elsewhere.

![Settings in the project tree > "Security settings"](images/142261176459_DV_resource.Stream@PNG-en-US.png)

###### Reusing central security settings

Examples for reusing elsewhere:

- User selection for user authentication for OPC UA server

  With this setting, you tell the server which client (user) with which user name and which password is allowed to access the server.
- User selection for OPC UA client authentication

  With this setting, you tell the client the user name and password that it is to use for client authentication for the server.

The settings for the client and server must correspond: The user name and password used by the client to log on must have been set up on the server and assigned the required authorizations.

###### Function rights for server and client

The corresponding function rights for the client or the server must also be enabled for users of the client function and users of the server function on an S7-1500 CPU. It is not enough simply to save the user name and password centrally.

Here is an example to illustrate this type of rights use.

1. Under "Security settings > Users and roles", you define a new role in the "Roles" tab with the name "PLC-opcua-role-all-inclusive", for example.  
   **Tip**: **The tab might be covered by an information window** ("The current status has not yet been checked..."). In this case, first close the information window.
2. In the "Function rights categories" area, you navigate to the runtime rights, then to the CPU function rights and below that you mark the CPU with the function rights you want to assign to a role.
3. You will find the following function rights in the "Function rights" section:

   - **OPC UA server access**

     This function right has an effect on the OPC UA server of the S7-1500 CPU. Only when this option is enabled, can the user with the role "PLC-opcua-role-all-inclusive" set up a session with the OPC UA server of the CPU. The user (client) authenticates itself with one of the user names and corresponding passwords that have been centrally defined (and loaded to the CPU).
   - **Managing certificates**

     This function right has an effect on the OPC UA server of the S7-1500 CPU. Only when this option is enabled, can the user with the role "PLC-opcua-role-all-inclusive" transfer certificates, CRLs or trusted lists to the CPU at runtime (push function). This functional right is required for automated certificate handling, e.g. in the context of GDS (Global Discovery Service).
   - **User authentication of the OPC UA client**

     This function right apples on the OPC UA client of the S7-1500 CPU (with client instructions). Only when this option is enabled can the user with the role "PLC-opcua-role-all-inclusive" use the user name and password for authentication to establish a session with a server.

     ![Function rights for server and client](images/142257986955_DV_resource.Stream@PNG-en-US.png)
4. The role "PLC-opcua-role-all-inclusive" still needs to be assigned to the relevant users ("Users" tab under "Security settings" in the project tree).

   > **Note**
   >
   > **"Runtime timeout" for users with OPC UA function rights**
   >
   > The value in the column "Runtime timeout" (max. session duration) in the table for user configuration does not evaluate the CPU for OPC UA runtime rights.
   >
   > Therefore, a user is not automatically logged out after a certain period of time. For this purpose use OPC UA specific mechanisms such as e.g. the parameter "Max. session timeout" (area OPC UA > Server > Settings).

---

**See also**

[User authentication (S7-1500, S7-1500T)](#user-authentication-s7-1500-s7-1500t)
  
[User authentication (S7-1500, S7-1500T)](#user-authentication-s7-1500-s7-1500t-1)
  
[Basics of user management in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)
  
[Overview of function rights](Managing%20users%20and%20roles.md#overview-of-function-rights)

##### Diagnostic settings of the server (S7-1500, S7-1500T)

###### Diagnostics

You can specify the scope of the diagnostics of the OPC UA server in the CPU settings.

To change the diagnostics scope, navigate to the "OPC UA > Server > Diagnostics" area.

![Diagnostics](images/125639623307_DV_resource.Stream@PNG-en-US.png)

###### Default setting

The default setting is a diagnostics behavior that supports the most important diagnostics without appreciably increasing the communication load.

You enable diagnostics for subscriptions when the OPC UA server also uses subscriptions, i.e. if necessary during the commissioning phase only.

Reason: A large volume of diagnostic activity generates a high communication load in the CPU and may suppress other important messages. Or, the high volume of diagnostics may result in important messages disappearing in the mass of messages and being ignored.

###### Additional information

You will find additional information on the meaning and effect of the settings shown above [here](#using-diagnostics-options-s7-1200-s7-1500-s7-1500t).

#### OPC UA server interface configuration (S7-1500, S7-1500T)

This section contains information on the following topics:

- [What is a server interface? (S7-1500, S7-1500T)](#what-is-a-server-interface-s7-1500-s7-1500t)
- [Using OPC UA companion specifications (S7-1500, S7-1500T)](#using-opc-ua-companion-specifications-s7-1500-s7-1500t)
- [Creating a server interface for companion specification (S7-1500, S7-1500T)](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)
- [Creating a user-defined server interface (S7-1500, S7-1500T)](#creating-a-user-defined-server-interface-s7-1500-s7-1500t)
- [Data types for companion specifications (S7-1500, S7-1500T)](#data-types-for-companion-specifications-s7-1500-s7-1500t)
- [Using additional OPC UA data types for companion specifications (S7-1500, S7-1500T)](#using-additional-opc-ua-data-types-for-companion-specifications-s7-1500-s7-1500t)
- [LocalizedText and ByteString data types (S7-1500, S7-1500T)](#localizedtext-and-bytestring-data-types-s7-1500-s7-1500t)
- [Rules for OPC UA XML files (S7-1500, S7-1500T)](#rules-for-opc-ua-xml-files-s7-1500-s7-1500t)
- [Creating a server interface for reference namespace (S7-1500, S7-1500T)](#creating-a-server-interface-for-reference-namespace-s7-1500-s7-1500t)
- [Generating OPC UA nodes based on local data mappings of FB types and UDTs (S7-1500, S7-1500T)](#generating-opc-ua-nodes-based-on-local-data-mappings-of-fb-types-and-udts-s7-1500-s7-1500t)
- [Notes on configuration limits when using server interfaces (S7-1500, S7-1500T)](#notes-on-configuration-limits-when-using-server-interfaces-s7-1500-s7-1500t)

##### What is a server interface? (S7-1500, S7-1500T)

###### Definition

A server interface combines nodes of an OPC UA address space of a CPU into a unit, so that a specific view on this CPU is provided for OPC UA clients.

Each server interface defines one or more namespaces in the OPC UA server of the CPU.

STEP 7 (TIA Portal) differentiates between the following types of server interfaces:

- Companion specification

  For this type of server interface, you use a Companion Specification created by a workgroup, for example.

  The workgroup is typically composed of members of the OPC Foundation and another industry organization who have jointly specified an OPC UA information model for a specific purpose (for example, for data exchange with RFID devices or with injection molding machines).

  This information model is realized in the form of OPC UA nodes in the address space of an OPC UA server. OPC UA clients can access these OPC UA nodes.

  You can also use the server interface type "Companion specification", for example, to download company-internal information models, e.g. in SiOME.

  If you implement a certain companion specification in your project, you apply the specifications of this companion specification into your project as server interface.

  For "Companion specification"-type server interfaces, you can import multiple namespaces which the Companion specification uses.

  Additional information on companion specifications is available [here](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t).

  Additional information on SiOME is available [here](https://support.industry.siemens.com/cs/ww/en/view/109755133).

  - When companion specifications refer to type definitions in dependent specifications, use the reference namespaces for this. You import reference namespaces as you would the actual companion specifications.

    See [Creating a server interface for reference namespace](#creating-a-server-interface-for-reference-namespace-s7-1500-s7-1500t).
  - If you want to make instance data from FBs or UDTs of the CPU accessible to OPC UA clients, you can have these instance data assignments automatically made as of TIA Portal version V17. You only need to map the FB types or the UDTs to suitable OPC UA data types of an imported reference namespace. For this mapping to be possible, enable the option "Generate OPC UA nodes based on the local data mapping" in the dialog for creating an OPC UA server interface of the type companion specification/reference namespace.

    See [Generating OPC UA nodes based on local data mappings of FB types and UDTs](#generating-opc-ua-nodes-based-on-local-data-mappings-of-fb-types-and-udts-s7-1500-s7-1500t)
- User-defined server interface:

  For this type of server interface you combine OPC UA nodes of an OPC UA server into a unit.

  To do this, use the specifications for your project or the requirements for your machine or your plant as a basis.

  Additional information on the user-defined server interface is available [here](#creating-a-user-defined-server-interface-s7-1500-s7-1500t).

###### Injection molding machine as an example for companion specification

In this example, a server interface contains the following elements:

- OPC UA nodes which you can write with an OPC UA client to receive information about this injection molding machine (in readable PLC tags)
- OPC UA nodes which you can write with an OPC UA client to transfer values to the injection molding machine (in writable PLC tags)
- OPC UA nodes which you can call with an OPC UA client to start functions of the injection molding machine (via server methods)

This server interface enables a default view of a CPU, which can be used to control an injection molding machine.

For injection molding machines, the companion specifications "OPC UA specifications for plastics and rubber machines" (previously "Euromap") define a whole series of OPC UA nodes which you can combine in a server interface.

Other OPC UA nodes of the CPU are not included in this server interface. This provides a better overview.

###### Example of user-defined server interface

A CPU should control the production of workpieces. Production begins when a production job arrives from the higher-level control system.

The production jobs are transferred via a server method: A control system transmits information on a workpiece by calling the server method in the CPU. This server method also starts production.

The control system, i.e. the connected OPC UA client, should only see this one server method. Therefore, you create a user-defined server interface in the CPU and assign the server method to this server interface. You enable only this server interface for OPC UA clients and thus limit the view of the CPU to this one function.

---

**See also**

[Using OPC UA companion specifications (S7-1500, S7-1500T)](#using-opc-ua-companion-specifications-s7-1500-s7-1500t)

##### Using OPC UA companion specifications (S7-1500, S7-1500T)

###### Introduction

OPC UA is universally applicable: The standard itself does not, for example, specify how PLC tags are to be named. It is also up to the individual user (application developer) to program and name server methods that can be called over OPC UA.

**Information modeling and standardization for devices and sectors**

For applications of the same kind, it is worth standardizing your device or machine interfaces with the "OPC UA toolkit".

Many different bodies and working groups have driven forward standardization and developed a range of companion specifications.

These specifications define:

- The objects, methods and tags with which a typical device or machine is to be described.
- The namespace intended for the specified objects.

Machines are typically structured in functional or technological units, and these units are then standardized.

Companion specifications offer machine and plant operators the benefits of a standardized interface. For example, all RFID readers that comply with the AutoID specifications can be integrated in the same way. This means that all RFID readers that comply with the AutoID specifications can be addressed by OPC UA clients in the same way irrespective of manufacturer.

Another example of a companion specification from the injection molding machinery sector is the EUROMAP specification.

The EUROMAP information models and the corresponding OPC companion specifications standardize the data exchange between injection molding machines and the higher-level MES (Manufacturing Execution System). This allows the MES to connect all lower-level injection molding machines in the same way.

> **Note**
>
> **EUROMAP and the OPC Foundation have established the Joint Working Group "OPC UA Plastics and Rubber Machinery".**
>
> The existing EUROMAP recommendations EUROMAP 77 (data exchange between injection moulding machines and MES), 82.1 (temperature control devices) and 83 (general definitions) were published under the neutral umbrella of the OPC Foundation as OPC 40077, 40082-1 and 40083. Future publications will be published both as EUROMAP recommendations and as OPC companion specifications.
>
> A major change it the change of the namespace, for example, for EUROMAP 77: Currently "http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/".

###### Useful information on EUROMAP

**Euromap 77, Euromap 83 and OPC UA for Devices (DI)**

With Release Candidate 2, some of the EUROMAP definitions have been transferred from EUROMAP 77 to EUROMAP 83 (currently OPC 40083). EUROMAP 83 defines general types that are used in specific information models. You will therefore also need to import the OPC UA server interface of EUROMAP 83.

"OPC UA for Devices" is a generally applicable information model for the configuration of hardware and software components. The information model also serves as the basis for other companion standards and is therefore also imported.

The OPC UA XML files are available here:

[Euromap77](http://www.euromap.org/euromap77)

[Euromap83](http://www.euromap.org/euromap83)

[OPC UA for Devices](https://opcfoundation.org/UA/schemas/DI/)

###### Using EUROMAP companion specification: Overview

To use the EUROMAP companion specification, follow these steps:

1. Generate an XML file by creating an instance of the type "IMM_MES_InterfaceType" using the SiOME program.

   How to proceed is described below in "Step 1: Create instances in SiOME".
2. In STEP 7 (TIA Portal), create PLC tags and server methods that correspond to the instance of the type "IMM_MES_InterfaceType" (created in Step 1).

   See below for information on how to proceed in "Step 2: Create PLC tags in STEP 7".

   An example of OPC UA nodes and the corresponding PLC tags can be found in section "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)".
3. In STEP 7 (TIA Portal), add a new server interface of companion specification type and import the XML file you created in step 1.

   The "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)" section describes how to proceed.
4. Assign the OPC UA nodes of the new server interface to the corresponding PLC tags, which you created in step 2.

   The "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)" section describes how to proceed.

###### Step 1: Create instances in SiOME

The following section describes how to use the free program "SiOME", the "Siemens OPC UA Modeling Editor".

With SiOME, you can create an OPC UA XML file, which describes the server interface (an information model).

Download link and explanations about SiOME are available [here](https://support.industry.siemens.com/cs/ww/en/view/109755133).

**Procedure in STEP 7**

To use the new server interface, import the server interface into the STEP 7 project, see section "[Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t)".

When the project is loaded into the CPU, the new server interface is available for OPC UA clients.

**Procedure in SiOME 1.7.3**

> **Note**
>
> The following description shows the work steps in SiOME 1.7.3.
>
> Follow-up versions of SiOME make it easier for you, for example, to create corresponding DBs, structures, variables or methods in the user program. Using a drag-and-drop operation, you can transfer data, for example, from SiOME to the TIA Portal (user program). In this case, the variables, etc. are already mapped correctly or, for methods, the corresponding FB elements are also generated correctly in the user program.
>
> Download the current SiOME version using the download link listed above, and follow the instructions in the documentation included in the download.

To use Euromap 77, create an XML file with an instance of "IMM_MES_InterfaceType".

The object type must be instantiated in order for the information model of the specific machine to appear in the address space of the OPC UA server.

The object type "IMM_MES_InterfaceType" is the root object type of Euromap 77. "IMM" stands for "Injection Moulding Machine".

Follow these steps:

1. Download the files "Opc_Ua.EUROMAP77.NodeSet2.xml" and "Opc_Ua_EUROMAP83_NodeSet2.xml" from the Euromap website (see above).
2. Download the file "Opc.Ua.Di.NodeSet2**.**xml" from the OPC Foundation website.

   The "Opc.Ua.Di.NodeSet2**.**xml" file contains type definitions which Euromap 77 uses.
3. Start SiOME.
4. First, import the namespace "http://opcfoundation.org/UA/DI/".

   To do so, click the ""Import XML" button in the "Information model" area.

   ![Step 1: Create instances in SiOME](images/111206704779_DV_resource.Stream@PNG-de-DE.png)

   SiOME displays the dialog for the opening files.
5. To import the file, select the "Opc.Ua.Di.NodeSet2.xml" file and click "Open".  
   Result: SiOME imports the XML file and shows the namespace "http://opcfoundation.org/UA/DI/" in the "Namespaces" area.

   The standard namespace "http://opfoundation.org/UA/" is always available in SiOME and does not have to be imported.
6. Now import the namespace "http://www.euromap.org/euromap83/"

   To do so, click the "Import XML" button again in the "Information model" area.

   Select the file "Opc_Ua.EUROMAP83.NodeSet2.xml".

   Result: SiOME imports the XML file and shows the namespace "http://www.euromap.org/euromap83/" in the "Namespaces" area.
7. Now import the namespace "http://www.euromap.org/euromap77/"

   To do so, click the "Import XML" button again in the "Information model" area.

   Select the file "Opc_Ua.EUROMAP77.NodeSet2.xml".
8. Create your own namespace for your project.

   To do this, right-click in the "Namespaces" area on "OPC UA Modelling Editor Project" or on "Namespaces" and select "Add Namespace".

   SiOME opens the "Add Namespace" dialog.
9. Enter the name of a new namespace.

   The "YourCompany.org" namespace is used in the example.

   SiOME now also displays the new namespace:

   ![Step 1: Create instances in SiOME](images/111206922763_DV_resource.Stream@PNG-de-DE.png)
10. Create an instance from the root object type IMM_MES_InterfaceType of the Companion specification Euromap 77.   
    To do so, in the "Information model" area, right-click the "DeviceSet" directory and select "Add Instance".

    SiOME displays the "Add Instance" dialog.
11. For "Name", enter a meaningful name for your instance.

    In the example, enter "IMM_Manufacturer_01234".

    For "TypeDefinition", select "IMM_MES_InterfaceType".

    This object type is the root object type of Euromap 77: If you generate an instance of this object type, then use the Euromap 77 once in the address space of your OPC UA server.
12. Click "OK".

    SiOME shows the new instance "IMM_Manufacturer_01234" in the "Information model" area under "DeviceSet":

    ![Step 1: Create instances in SiOME](images/124448410251_DV_resource.Stream@PNG-de-DE.png)
13. Create an instance of the data type "InjectionUnitType".

    To do this, right-click on the "InjectionUnits" directory in the "Information model" area and select "Add Instance".

    SiOME displays the "Add Instance" dialog.

    For "Name", enter a meaningful name for the instance.

    In the example, enter "InjectionUnit_1".

    For "TypeDefinition", select "InjectionUnitType".

    Click "OK".
14. Create a new "Mould_1" instance of the "MouldType" object type in the "Moulds" directory.
15. Create a new instance "PowerUnit_1" of the "PowerUnitType" object type in the "PowerUnits" directory.
16. Save the XML file.

    To do so, click the "Quick save" button in the "Information model" area:

    ![Step 1: Create instances in SiOME](images/124448418443_DV_resource.Stream@PNG-de-DE.png)
17. Export the XML file.

    To do so, click the ""Export XML" button in the "Information model" area.

    ![Step 1: Create instances in SiOME](images/111206713611_DV_resource.Stream@PNG-de-DE.png)

    SiOME shows the "Export XML" dialog.
18. Leave all namespaces activated and click "OK".

    SiOME displays the "Save as" dialog.
19. Select a meaningful name and save the exported file.

    In the example, name the XML file "IMM_Manufacturer_01234".

**Result**:

You have now created an XML file which uses the companion specification "Euromap 77" once (with one instance).

###### Step 2: Creating PLC tags for the Euromap 77 instance in STEP 7.

For Euromap 77, you must provide PLC tags and server methods in your user program and assign the instance of the "IMM_MES_InterfaceType" type.

To create PLC tags for the instance of the "IMM_MES_InterfaceType" type, proceed as follows.

1. Create a user-defined data type (UDT).

   The figure below shows the beginning of the user-defined data type "InjectionUnit" as example.

   This data type has the same structure as "InjectionUnit" in the type "IMM_MES_InterfaceType".

   Make sure that you use SIMATIC data types that are compatible with the OPC UA data types (see "Mapping of data types" below).

   ![Step 2:  Creating PLC tags for the Euromap 77 instance in STEP 7.](images/125157130635_DV_resource.Stream@PNG-en-US.png)
2. Add a new global data block to your STEP 7 project.

   In the example, name the data block "IMM_Manufacturer_01234", so that there is a reference to the injection molding machine of the respective manufacturer and the serial number.
3. Create a new element in this data block.

   In the example, name this element "InjectionUnit_1"
4. Assign the new user-defined data type "InjectionUnit" to this element.

###### Result

In your STEP 7 project, you have created a tag for the Euromap 77 in the "IMM_Manufacturer_01234" data block.

##### Creating a server interface for companion specification (S7-1500, S7-1500T)

For basic information on companion specifications, refer to the section "[Using OPC UA companion specifications](#using-opc-ua-companion-specifications-s7-1500-s7-1500t)". The benefits of the Euromap 77 companion specification, which provides a model for injection molding machines, is also discussed in detail there.

Using this companion standard, the S7-1500 CPU can control an injection molding machine, for example, and provide an OPC UA client, such as a higher-level MES system, with an interface for accessing the functions and tags of injection molding machine.

An OPC UA server interface of the type "Companion Standard" limits the access of clients to exactly those functions and tags that are required, for example, for higher-level systems (MES systems).

The following description shows how to create a server interface in STEP 7 (TIA Portal) which contains only the Euromap 77 companion specification.

If you want to make OPC UA clients accessible to other tags or methods than those required for the management of an injection molding machine, simply create another OPC UA server interface. In this way, you can clearly arrange the functionality of the CPU as OPC UA server.

###### Creating a server interface for a companion specification

To create a server interface for a companion specification with STEP 7 (TIA Portal), proceed as follows:

1. Select the CPU that you want to use as an OPC UA server.
2. In the project tree, click "OPC UA communication > Server interfaces".
3. Double-click "Add new server interface".
4. To select this type of server interface, click "Companion specification".

   A general name for the new server interface is entered in the dialog, for example "Server_Interface_1".
5. Change the name of the new server interface so that it is descriptive in your project.

   The name should have the following structure, according to Euromap 77 for example: "IMM_<Manufacturer>_<Serial number>".

   The example uses the name "IMM_Manufacturer_01234".

   ![Creating a server interface for a companion specification](images/127894043019_DV_resource.Stream@PNG-en-US.png)
6. In the "Import XML file" field, select an XML file that describes an information model.

   The "[Using OPC UA companion specifications](#using-opc-ua-companion-specifications-s7-1500-s7-1500t)" section describes how to create such an XML file with the SiOME tool.

   The figure below shows a section from the information model: "IMM_MANUFACTURER_0123456" an instance (use) of the type "IMM_MES_InterfaceType" which was defined by Euromap 77 . "InjectionUnit_1" is an instance of the "InjectionUnitType" type of Euromap 77.

   ![Creating a server interface for a companion specification](images/124375817227_DV_resource.Stream@PNG-de-DE.png)
7. Click "OK".

   STEP 7 (TIA Portal) imports the information model described in the selected XML file.

   An error occurs when type definitions are used in the imported XML file that are not yet present in STEP 7 (TIA Portal) and that are also not contained in the imported XML file.

   In the example, an XML file is imported that uses type definitions defined in the following namespaces (Namespaces):

   - http://opcfoundation.org/UA/DI/
   - http://www.euromap.org/euromap83/
   - http://www.euromap.org/euromap77/

   **Tip**: STEP 7 displays missing namespaces in the lower area of the OPC UA interface editor ("Properties" tab).

   To do this, select the server interface in the project tree (here: IMM_Manufacturer_01234) and select the "Namespaces" area in the inspector window. Missing namespaces are selected.

   If one or more namespaces are missing in your STEP 7 project, create a new server interface of the "Reference namespace" type for each namespace.

   The "[Creating a server interface for reference namespace](#creating-a-server-interface-for-reference-namespace-s7-1500-s7-1500t)" section describes the procedure.

   If all reference namespaces are available, STEP 7 displays the table without errors:

   ![Creating a server interface for a companion specification](images/124377400459_DV_resource.Stream@PNG-de-DE.png)
8. Drag the OPC UA elements from the right area of the table (OPC UA elements) to the left part of the table (OPC UA server interface) so that the respective OPC UA elements (the local PLC tags) are assigned to the respective OPC UA nodes of Euromap 77.

   The figure below shows a section from the assignment of the local data (PLC tags) to the OPC UA nodes of the Euromap 77.

   ![Creating a server interface for a companion specification](images/125091075467_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Checking the mapping of CPU local data on nodes of the OPC UA server interface**  When invalid assignments (mappings) exist in the server interface, they can result in incorrect read and write operations. Check the assignments and run a consistency check. |  |

###### Information on the server interface

The editor for configuring the OPC UA server interface is structured as a table and provides the following information:

- **Name**

  The top node (root node) is named "IMM_Manufacturer_01234" in the example. If a client browses in the address space of the server, this node is the container for all lower-level nodes. BrowseName and the DisplayName of this node depend on the name you have assigned for the server interface.

  In this case, for example, this name stands for the injection molding machine as a whole. It is the name of the instance of the companion specification Euromap 77 that is used here. According to the companion specification, the instance name should begin with "IMM", followed by the name of the manufacturer of the injection molding machine; the serial number of the machine is added to the end. This allows a unique identification of the machine.

  The names of all other lower-level nodes are defined by the specification (in the example above by Euromap 77). These node names must not be changed. This ensures a uniform view of all injection molding machines, which complies with the specification.
- **Node type**

  Type of the OPC UA node. The type is specified by the companion specification that is used.

  In the following cases, STEP 7 marks a node type in the table in color:

  - No type definition is included for this in the imported XML file.
  - The namespace in which the type was defined is not available in STEP 7.

  In this case, create a server interface of the "Reference namespace" type for the missing namespace or for each of the missing namespaces.

  The missing namespaces can be found under "Namespaces" in the properties of the server interface.
- **Local data**

  STEP 7 displays the data block which is assigned to the OPC UA node: The CPU reads the value of the OPC UA nodes from this data block.

  If a data block is highlighted in color (e.g. after a consistency check), the specified data block is not available in the CPU.

  In this case, you have to create the missing data block in the CPU (of user program) and supply it with values.
- **Data type**

  The SIMATIC data type of the PLC tag (e.g. element of a data block) in the CPU, from which the value of an OPC UA node (UAVariable type) is read, or to which a value is assigned.

###### Update interface

You have the possibility to update the server interface for companion specifications.

Example: After importing companion specifications and then importing reference namespaces on which the companion specifications depend, the type definitions of the reference namespaces do not take effect immediately.

When you click on the "Update interface" button, it resolves the missing type definitions of the companion specifications.

"Update interface" button:

![Update interface](images/170529175691_DV_resource.Stream@PNG-en-US.png)

###### Generate local data

You have the option of generating local data for all or for selected nodes of the server interface that are not already assigned ("mapped") to local data of the CPU. The newly created local data are mapped automatically.

You trigger the automatic generation of local data by clicking the "Generate local data" button (all nodes that are not already mapped) or by selecting individual nodes and then clicking the "Generate local data" shortcut menu.

"Generate local data" button:

![Generate local data](images/142323385099_DV_resource.Stream@PNG-en-US.png)

You can only generate nodes that can be mapped to local data, which means no objects, no folders, no methods or input/output arguments of methods.

After you have clicked the button or selected the shortcut menu, you must select in the follow-up dialog box whether the local data should be created in a new DB or in an existing DB.

###### Consistency check

You have the option to check the server interface.

STEP 7 (TIA Portal) checks whether the OPC UA node of the server interface PLC tags (data blocks) has been assigned compatible SIMATIC data types.

In methods, STEP 7 checks the quantity, name and data type of the arguments.

To check the consistency of the server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Consistency check](images/126635249035_DV_resource.Stream@PNG-en-US.png)

###### Export interface

You have the option of exporting the OPC UA server interface as an XML file. This XML file contains all data type definitions referenced by the server interface.

To export the OPC UA server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Export interface](images/125342533259_DV_resource.Stream@PNG-en-US.png)

###### Import companion specification

Click this button to import a new companion specification:

![Import companion specification](images/170533964299_DV_resource.Stream@PNG-en-US.png)

##### Creating a user-defined server interface (S7-1500, S7-1500T)

###### Introduction

The description is based on the following example:

A protective fence surrounds the production cell "Cell_1". The fence is equipped with the gate "Gate_1".

An S7-1500 CPU controls the entire production cell and also controls access through Gate_1.

A robot packs drugs into boxes in the production cell and then stacks the boxes on pallets.

Self-driving vehicles for automated material transport move the pallets to the central warehouse, thereby passing through Gate_1.

The CPU publishes a server interface via which the driverless transport systems arrange for Gate_1 to open.

The server interface contains the server method "smOpenGate" for opening the gate and the tag "Gate_1_State" which indicates the status of the gate (open or closed).

###### Creating a user-defined server interface

To create an Server interface, follow these steps:

1. Select the CPU that you have used and configured as OPC UA server.
2. Click "OPC UA communication > Server interfaces".
3. Double-click "Add new server interface".

   STEP 7 displays the following dialog.

   ![Creating a user-defined server interface](images/126768339083_DV_resource.Stream@PNG-en-US.png)
4. Change the name of the new server interface so that it is descriptive in your project.

   In the example, change the name "Server-interface_1" suggested by STEP 7 to "Cell_1".
5. Click "Server interface" and then "OK".
6. Click on the triangle in front of "Program blocks" in the area "OPC UA elements" to open the "Program blocks" folder.

   STEP 7 displays the following table for editing:

   ![Creating a user-defined server interface](images/127737143947_DV_resource.Stream@PNG-en-US.png)

   The editor is divided into two areas.

   - **OPC UA server interface**

     On the left is the root node of the server interface "Cell_1".

     This interface is currently still empty: No OPC UA elements have been added to the server interface yet.
   - **OPC UA elements**

     On the right are the OPC UA elements.

     OPC UA elements are objects that have been created in the STEP 7 project and have the property "Accessible from HMI/OPC UA".
7. Drag the OPC UA elements into the "<Add new>" line of the new OPC UA server interface.

   > **Note**
   >
   > The following applies in general: If you store data blocks or technology objects in the left area of the table, STEP 7 (TIA Portal) creates an object in the server interface. The elements of the data blocks are arranged as separate nodes below this.
   >
   > If you store structures in the left area of the table, STEP 7 creates a node for the structure as a whole and nodes for each element of the structure.
   >
   > The same applies to arrays: Again, STEP 7 creates a node for the array as a whole and nodes for each element of the array.
   >
   > When you place a method in the left area of the table, STEP 7 creates a single node; the arguments of the inserted method are displayed for information purposes.

   In the example, you drag the "Gate_1_State" tag from the right area to the left area to "<Add new>".

   Then, drag the server method into the left area.

   This server method is located within the "smOpenGate_DB [DB3]" data block in the right area.

   STEP 7 (TIA Portal) displays the dialog as follows:

   ![Creating a user-defined server interface](images/126583055371_DV_resource.Stream@PNG-en-US.png)

   | Symbol | Meaning |
   | --- | --- |
   |  | **Notice** |
   | **Checking the mapping of CPU local data on nodes of the OPC UA server interface**  When invalid assignments (mappings) exist in the server interface, they can result in incorrect read and write operations. Check the assignments and run a consistency check.  Since TIA Portal generates only warnings and not errors for invalid assignments, you can proceed step-by-step as follows:  For example, in the first step, you can modify the program/local data so that the program runs without errors. In the next step, you modify the OPC UA server interface and eliminate the inconsistencies.   At the points at which the TIA Portal generates warnings, the OPC UA server interface does not function during runtime. The OPC UA server generates runtime errors. |  |

**Limiting the view to OPC UA servers**

By selecting the OPC UA elements, you limit the view to the OPC UA server and the options of the OPC UA clients.

In the server interface of the example, the "Robot_1" data block is missing because industrial trucks do not need access to the server methods and tags of the robot.

In this case, it is best to disable the standard server interface (SIMATIC namespace) in the OPC UA properties of the S7-1500 CPU so that the filtered nodes cannot be accessed any other way, see the figure below.

![Creating a user-defined server interface](images/126768840331_DV_resource.Stream@PNG-en-US.png)

You can also disable the visibility of each configured OPC UA server interface in the properties of the server interface and thus prevent that this server interface can be used by clients during operation.

- To do this, select the server interface and right-click on the "Properties" command.

This option lets you define multiple server interfaces centrally, for example, and enable and download only the required server interface.

Once a server interface has been defined, you can drag it to another CPU in the project tree.

![Creating a user-defined server interface](images/126768343947_DV_resource.Stream@PNG-en-US.png)

###### Information on the server interface

The "OPC UA Server Interface" dialog is structured as a table and provides the following information:

Note that not all columns are displayed initially. You determine what is displayed by right-clicking on the header line of the table.

When a row is selected, you can display the OPC UA attributes of the node in the Inspector window ("OPC UA attributes" area), such as node ID, node class, node type, and description.

- **BrowseName**

  The language neutral name of the user-defined server interface is at the top (BrowseName). This name can be freely selected.

  The names (BrowseNames) of the individual OPC UA nodes that have been added to the server interface are under the name of the interface.

  You cannot change the name of an OPC UA node in this dialog. The names come from the STEP 7 project.

  You can delete an OPC UA node from the table. This means that it no longer belongs to the server interface and is no longer visible to OPC UA clients.
- **DisplayName**

  Similar to BrowseName. However, the name can be translated and is displayed, if available, in the corresponding language.
- **Node ID**

  NodeId of the OPC UA node, e.g. http://Server-Node_1; i=1
- **Node type**

  Type of the OPC UA node, for example BOOL, BYTE, INT.

  These node types were defined by Siemens, not by the OPC Foundation. For example, the OPC Foundation uses the Boolean node type for BOOL. BOOL is directly derived from Boolean.

  The specified node type cannot be changed in this dialog: If you want to use a different node type, you must change the type of the respective PLC tags in the STEP 7 project.
- **Access level**

  - If an OPC UA node is a tag (UAVariable type), the node can be only readable (RD) or readable and writable (RD/WR).
  - If an OPC UA node is a method (UAMethod type), this node can always be called.
- **Description**
    
  The description at the node corresponds to the comment at the CPU tag (e.g. the comment for a data block element). STEP 7 adds the comment to the description of the node during mapping.
- **Data type**

  The SIMATIC data type used in the STEP 7 project is specified, for example, Bool, Byte, Int. etc.
- **Local data**

  The SIMATIC data type of the data block in the CPU, from which the value of an OPC UA node (UAVariable type) is read, or to which a value is written.

###### Generate local data

You have the option of generating local data for all or for selected nodes of the server interface that are not already assigned ("mapped") to local data of the CPU. The newly created local data are mapped automatically.

You trigger the automatic generation of local data by clicking the "Generate local data" button (all nodes that are not already mapped) or by selecting individual nodes and then clicking the "Generate local data" shortcut menu.

"Generate local data" button:

![Generate local data](images/142323385099_DV_resource.Stream@PNG-en-US.png)

You can only generate nodes that can be mapped to local data, which means no objects, no folders, no methods or input/output arguments of methods.

After you have clicked the button or selected the shortcut menu, you must select in the follow-up dialog box whether the local data should be created in a new DB or in an existing DB.

###### Consistency check

You have the option to check the server interface.

During the consistency check, STEP 7 checks whether the OPC UA nodes of the server interface are each assigned to a suitable OPC UA element (identical data type) or whether the used element still exists in the CPU.

In methods, STEP 7 checks the quantity, name and data type of the arguments.

To check the consistency of the server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Consistency check](images/126635249035_DV_resource.Stream@PNG-en-US.png)

###### Export interface

You have the option of exporting the OPC UA server interface as an XML file. This XML file contains all data type definitions referenced by the server interface.

To export the OPC UA server interface, click on the following icon in the toolbar of the OPC UA server interface editor:

![Export interface](images/125342533259_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Master copies for OPC UA communication (S7-1200, S7-1500, S7-1500T)](#master-copies-for-opc-ua-communication-s7-1200-s7-1500-s7-1500t)

##### Data types for companion specifications (S7-1500, S7-1500T)

###### Mapping of data types

The table below shows the compatible SIMATIC data type for each OPC UA data type.

Assign the data types as shown below (SIMATIC data type - OPC UA data type). Other assignments are not permitted. STEP 7 does not check the observance of this rule and does not prevent an incorrect assignment. You are responsible for the rule-compliant selection and assignment of the data types.

You can also use the listed data types, for example, as elements of structures/UDTs for input and output parameters of self-created server methods (UAMethod_InParameters and UAMethod_OutParameters).

Mapping of data types

| SIMATIC data type | OPC UA data type |
| --- | --- |
| BOOL | Boolean |
| SINT | SByte |
| INT | Int16 |
| DINT | Int32 |
| LINT | Int64 |
| USINT | Byte |
| UINT | UInt16 |
| UDINT | UInt32 |
| ULINT | UInt64 |
| REAL | Float |
| LREAL | Double |
| LDT | DateTime |
| WSTRING | String |
| DINT | Enumeration (Encoding Int32) and all derived data types |
| User-defined data type required (UDT, user-defined data type)  The user-defined data type must be created with the prefix "Union_", for example "Union_MyDatatype". See example below the table.  The first element (Selector) in this UDT must have the data type "UDINT". | UNION and all derived data types |
| see [LocalizedText and ByteString data types](#localizedtext-and-bytestring-data-types-s7-1500-s7-1500t) | LocalizedText  ByteString |

**User-defined data type for UNION required**

The figure below shows the tag "MyVariable", which has the "Union_MyDatatype" data type.

This SIMATIC data type corresponds to an OPC UA tag with the data type UNION.

The figure shows an example of the declaration: When Selector = 1, Union takes a ByteArray; when Selector = 2, Union takes a WString.

![Mapping of data types](images/115303896331_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Using additional OPC UA data types for companion specifications (S7-1500, S7-1500T)](#using-additional-opc-ua-data-types-for-companion-specifications-s7-1500-s7-1500t)

##### Using additional OPC UA data types for companion specifications (S7-1500, S7-1500T)

Apart from the OPC UA data types listed in the section "Mapping of data types" and their correspondences on the SIMATIC side, there are the following OPC UA basic data types (built-in data types) which you can also use:

- OpcUa_NodeId
- OpcUa_QualifiedName
- OpcUa_Guid
- OpcUa_XmlElement
- [OpcUa_ByteString](#localizedtext-and-bytestring-data-types-s7-1500-s7-1500t)
- [OpcUa_LocalizedText](#localizedtext-and-bytestring-data-types-s7-1500-s7-1500t)

Requirement for the use of the basic data types listed above as variables in the application program: The basic data types have to exist as complex data types that are structured exactly like the corresponding OPC UA basic data types.

- OpcUa_NodeId, OpcUa_QualifiedName and OpcUa_Guid exist as system data types; that's why you can use these data types not only for single variables but also as elements of a structure.
- For the built-in data type XmlElement, you need to create a PLC data type according to the OPC UA specification and then use it as an element in a structure so that the data types of the elements can be resolved.
- For OpcUa_ByteString and OpcUa_LocalizedText, the requirements have been created in TIA Portal V17 to simply use these data types in the server interface of the "Companion Specification" type:

  - You create the corresponding node type in the server interface (for example, OpcUa_LocalizedText)
  - You click on "Generate local data"

  STEP 7 then automatically generates the appropriate data structures in a DB.
- These requirements were created in TIA Portal V19 for OpcUa_Guid. Proceed as described in the previous section.

###### System data type "OPC_UA_NodeId"

For the OPC UA basic data type "OpcUa_NodeId", refer to the structure of the system data type and the meaning of the individual elements. OPC_UA_NodeId is used to identify a node in the OPC UA server.

| Name | S7 data type | Meaning |
| --- | --- | --- |
| NamespaceIndex | UINT | Namespace index of the node in the OPC UA server.  A node can, for example, be a tag. |
| Identifier | WSTRING[254] | The designation of the node (object or tag) depends on the identifier type:  - Numeric identifier: The node is labeled with a number, for example "12345678". - String identifier: The node is labeled with a name, for example "MyTag". No distinction is made between upper and lower case. |
| IdentifierType | UDINT | Type of identifier  - 0: Numeric identifier - 1: String identifier - 2: GUID - 3: Opaque |

###### System data type "OPC_UA_QualifiedName"

See the following table for the structure of the system data type "OPC_UA_QualifiedName":

| Name | S7 data type | Meaning |
| --- | --- | --- |
| NamespaceIndex | UINT | The namespace index of the name. |
| Name | WSTRING[64] | Name of the node or tag. |

###### System data type "GUID"

The "Guid" data type is available as a node type from TIA Portal V19. For the definition of these OPC UA data types, see also OPC 10000-6 mappings.

The figure shows the assignment of the "Guid" data type for a tag node in a server interface.

![System data type "GUID"](images/172402039819_DV_resource.Stream@PNG-de-DE.png)

The next figure shows the automatically created data block "Generate local data" with the GUID elements.

![System data type "GUID"](images/172402031627_DV_resource.Stream@PNG-de-DE.png)

###### UDT for XmlElement

An XmlElement is a serialized XML fragment (UTF-8 string).

For the basic data type "XmlElement", create the following PLC data type:

![UDT for XmlElement](images/106476397067_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Data types for companion specifications (S7-1500, S7-1500T)](#data-types-for-companion-specifications-s7-1500-s7-1500t)

##### LocalizedText and ByteString data types (S7-1500, S7-1500T)

As of TIA Portal version V17 and S7-1500 CPU firmware version V2.9, the two OPC UA Built-in data types "LocalizedText" and "ByteString" are available for mapping to corresponding SIMATIC data structures. For the definition of these OPC UA data types, see also OPC 10000-3 DataType definitions.

These data types are used in companion specifications, for example, and can be easily handled by the user program with the OPC UA interface editor.

**LocalizedText**

A structure containing a string with locale identifier (e.g. 'en-US').

The structure has three elements with a defined order and the following structure in SIMATIC:

- **Encoding** (data type OPC_UA_LocalizedTextEncodingMask): Indicates in bit 0 whether the "Locale" field has a content and in bit 1 whether the "Text" field has a content. Both fields should have a content. We therefore recommend setting the "Encoding" value for SIMATIC to 2#00000011.
- **Local** (WString data type): Locale, for example, 'en-US'.
- **Text** (WString data type): Text box, for example, 'Text'.

**ByteString**

A sequence of octets.

The structure is built up as follows:

- **ActualLength** (data type "OPC_UA_ByteStringActualLength"): Length of the ByteString array that is filled
- **ByteString** ("Array of Byte" data type): Byte array

###### Requirement

An OPC UA server interface has been created.

###### Application

You can import a companion specification or a reference namespace that contains definitions of the "LocalizedText" or "ByteString" type.

Likewise, you can create a server interface and define an address model yourself with the data types "LocalizedText" or "ByteString". The procedure is described in the next section.

###### Procedure

You will learn how to create a node of the type "LocalizedText" or "ByteString" with the interface editor and then have a SIMATIC data structure created automatically for this node in the paragraphs below.

To define OPC UA nodes of the type "Localized Text"/"ByteString" in a server interface, follow these steps:

1. Create nodes of the type "LocalizedText" or "ByteString" in the "OPC UA server interface" area. These node types are included in the list of selectable node types.

   ![Procedure](images/143591852427_DV_resource.Stream@PNG-de-DE.png)
2. Select the "Generate local data" command from the shortcut menu. To generate the local data, select a data block, for example, a new DB with the name "MyServerInterface_Data".

   ![Procedure](images/143591860875_DV_resource.Stream@PNG-de-DE.png)

   **Result**: STEP 7 generates the corresponding structure for the mapping in which you still need to adjust the required text length (Text) and the required locale (Locale) for "LocalizedText".

   The same is true for "ByteString"; in this case, you must adjust the length and the array.

   The consistency check generates a warning to indicate the required adjustments.

   ![Procedure](images/143570396427_DV_resource.Stream@PNG-de-DE.png)

###### Rules

- You can also create UDTs with the structure as shown above for the node types "LocalizedText" or "ByteString" and use them for DB elements.
- You can use the node types "LocalizedText" or "ByteString" in other structures (nests).
- The SIMATIC structures for "LocalizedText" or "ByteString" may only be used completely; an isolated data type, such as "OPC_UA_LocalizedTextEncodingMask" for other purposes, is not provided.
- Input and output parameters of methods can also be of the data type/node type "LocalizedText" or "ByteString".

---

**See also**

[Data types for companion specifications (S7-1500, S7-1500T)](#data-types-for-companion-specifications-s7-1500-s7-1500t)

##### Rules for OPC UA XML files (S7-1500, S7-1500T)

###### Importing exported OPC UA XML files to an S7-1500 CPU

Please note the following information when importing server interfaces that come from the OPC UA XML export of an S7-1500.

> **Note**
>
> **Import blocked for namespace "http://www.siemens.com/simatic-s7-opcua"**
>
> You cannot import server interfaces with the namespace "http://www.siemens.com/simatic-s7-opcua" to an S7-1500 CPU because this namespace is reserved for S7-1500 CPUs (standard SIMATIC server interface) and is not available for imports.
>
> If you want to import a server interface with the namespace "http://www.siemens.com/simatic-s7-opcua", open the server interface to be imported (OPC UA XML file) and change the namespace in the relevant places. The file thus changed can then be imported.

###### Integrity of the OPC UA XML files

OPC UA XML files represent the server address space. These files are, for example, imported by you in the context of OPC UA Companion specifications as a server interface after adaptation to the application, loaded into the S7-1500 CPU and tested.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **No checking of imported OPC UA XML files**  Protect these OPC UA XML files against unauthorized manipulation since STEP 7 does not check the integrity of these files. |  |

**Recommendation**

To minimize risks in the case of an extension or adaptation of the server address space, follow these steps:

1. Protect the project (project navigation: Security settings > Settings).
2. Export the corresponding server interface before the extension or adaptation.
3. Revise this OPC UA XML file.
4. Import the file again as a server interface.

##### Creating a server interface for reference namespace (S7-1500, S7-1500T)

###### Companion specifications and referenced namespaces

A series of OPC UA object types (as well as additional definitions) are defined in a companion specification. These object types are each defined in namespaces so that the names of the object types (type definitions) are unique.

To use a companion specification in your project, create instances of object types of this companion specification.

To do this the object definitions must be available in your STEP 7 project. If this is not the case, you must import the object definitions. To import all definitions of a namespace, create a server interface of type "Reference namespace" for each namespace in STEP 7.

> **Note**
>
> **EUROMAP and the OPC Foundation have established the Joint Working Group "OPC UA Plastics and Rubber Machinery".**
>
> The existing EUROMAP recommendations EUROMAP 77 (data exchange between injection moulding machines and MES), 82.1 (temperature control devices) and 83 (general definitions) were published under the neutral umbrella of the OPC Foundation as OPC 40077, 40082-1 and 40083. However, the examples listed below use the previously valid designations and references.

###### Example Euromap 77 (currently OPC 40077)

You have added a server interface for the companion specification Euromap 77 (currently OPC 40077).

The server interface uses object types defined in OPC UA DI as well as in Euromap 83 and Euromap 77 in their corresponding namespaces.

Therefore, in addition to the server interface Euromap 77 of the "Companion Specification" type, create additional server interfaces of "Reference namespace" type in STEP 7, in each case for the following namespaces:

- http://opcfoundation.org/UA/DI/
- http://www.euromap.org/euromap83/
- http://www.euromap.org/euromap77/

The following description shows you how to proceed.

###### Creating a server interface for a reference namespace

To create a server interface for a namespace, proceed as follows:

1. Select the CPU that you want to use as an OPC UA server.
2. Click "OPC UA communication > Server interfaces".
3. Double-click "Add new server interface".

   STEP 7 (TIA Portal) now displays the dialog "Add new server interface".

   A general name for the new server interface is entered in the dialog, for example "Server_Interface_1".
4. Assign a descriptive name for the new server interface.

   In the example, select the name "OPC.Ua.Di" or a similar name that clearly references the namespace "http://opcfoundation.org/UA/DI/".

   This namespace must be imported first. It contains basic definitions (for example, the UAObjectType "DeviceType").
5. Click on the "Companion specification" button and select the "Reference namespace" type.
6. Click on the three dots next to the "Import XML file" field.
7. Select an XML file that contains the definitions of the namespace "http://opcfoundation.org/UA/DI/".

   Select the file "Opc.Ua.Di.NodeSet2.xml" in the example. You can download this file here:  
   [Opc.Ua.Di.NodeSet2.xml](https://opcfoundation.org/UA/schemas/DI/)

   **Note**: If the file cannot be imported, this may be because the OPC UA ("CORE") model version available in TIA Portal does not match the OPC UA for Devices ("DI") model version. In this case, select a different version of the DI model (e.g. a previous version).

   The figure below shows the dialog with the entries:

   ![Creating a server interface for a reference namespace](images/172496960779_DV_resource.Stream@PNG-en-US.png)
8. Click "OK".

   STEP 7 (TIA) now generates the new server interface.

You can find the server interface in the project tree of STEP 7 (TIA Portal), under "OPC UA Communication > Server interfaces > Reference namespace".

If a companion specification uses additional namespaces, add a new server interface for each namespace.

**Add additional server interfaces for Euromap77**

For Euromap 77, you still need the following namespaces:

- http://www.euromap.org/euromap83/
- http://www.euromap.org/euromap77/

First, add a server interface for the namespace "http://www.euromap.org/euromap83/".

This namespace contains basic definitions for Euromap 77, therefore it is required here first. All definitions of this namespace are included in the XML file "Opc_Ua.EUROMAP83NodeSet2.xml", which you can download from the [Euromap website](http://www.euromap.org/en/euromap83).

Then add a server interface for the namespace "http://www.euromap.org/euromap77". All definitions of this namespace are included in the XML file "Opc_Ua.EUROMAP77.NodeSet2.xml", which you can also download from the [Euromap website](http://www.euromap.org/en/euromap77).

##### Generating OPC UA nodes based on local data mappings of FB types and UDTs (S7-1500, S7-1500T)

If you want to make instance data from FBs or UDTs of the CPU accessible to OPC UA clients, you can have these instance data assignments automatically made as of TIA Portal version V17.

You only have to map the FB types or the UDTs to suitable OPC UA data types of imported reference namespaces. Based on these mappings created in STEP 7 (TIA Portal), generate the required nodes in the server interface for each FB instance or for each UDT usage during the compile.

If you extend your program and add more FB instances or UDT usages, or if you add existing instances delete, you do not need to worry about adapting the server interface: STEP 7 automatically adjusts the server interface when compiling the program.

###### Example

- You create a function block (FB) in the user program of the CPU and define in the "Static" area of the interface of the FB the parameters that form the "memory" of the FB. The instances (values) of this parameter are to be accessible for OPC UA clients.
- You create an OPC UA data type (e.g. with SiOME) with elements that correspond to the data type the parameters in the static area of interface of the FB. The order of the elements does not matter. Then import the reference nodeset file as a reference namespace.

The following figure shows the assignment of elements as comparison of the reference namespace view (server interface) and the OPC UA elements view (program).

![Example](images/143156317579_DV_resource.Stream@PNG-de-DE.png)

**Mapping of data types (FB interface - OPC UA interface): Principle**

The following figure shows the assignment of the elements from the user program of the CPU to the elements of the OPC UA server interface. Names and the order of the elements do not have to match.

![Example](images/141229107467_DV_resource.Stream@PNG-de-DE.png)

**Automatic generation of the OPC UA server instances in the server interface: Principle**

The figure below shows the compilation of the project. The instances of the user program are also generated in the server interface.

![Example](images/143157002635_DV_resource.Stream@PNG-de-DE.png)

By mapping between FB type information / UDT type information and OPC UA type information, STEP 7 is able to create all instances present in the program as nodes in the server interface. You have the option to generate these nodes together with a new server interface or to generate these nodes in an existing server interface.

![Example](images/141310135179_DV_resource.Stream@PNG-en-US.png)

###### Rules

- Only the FB elements in the "Static" area of an FB interface can be mapped to OPC UA type descriptions.
- When mapping the data types, OPC UA elements from the same FB interface or from the same UDT must always be selected for an object. Mapping from different FBs or UDTs to an object is not permitted.

###### Requirement

- The FB types used, defined in the "Static" area of an FB, must be configured as "Accessible for OPC UA".
- The UDTs used must be configured as "Accessible for OPC UA".
- A nodeset file (XML file) is available with OPC UA data type definitions that match the FB types or UDTs defined in user program (can be mapped).
- The user program with the FB instances and UDT usages is available.

###### Procedure

To map a data type from a reference namespace to an FB type or UDT data type, follow these steps:

1. Select the CPU that you want to use as an OPC UA server.
2. Import the prepared nodeset file (XML file) with the type definitions as a reference namespace

   (see [Creating a server interface for reference namespace](#creating-a-server-interface-for-reference-namespace-s7-1500-s7-1500t)).

   - In the "Add new server interface" dialog, enable the option "Generate OPC UA nodes based on the local data mapping".

     Only when this option is enabled can you map FB types or UDTs by dragging them to the OPC UA type descriptions.
3. Double-click the icon for the server interface of the "Reference namespace" type that you just generated.

   The editor for mapping between OPC UA server interface and OPC UA elements opens. In the properties area of the editor, in the "Mapping of local data", the option "Generate OPC UA nodes based on the local data mapping" is enabled. If not, enable the option now.
4. Assign the existing FB types or UDTs to the nodes of the server interface (reference namespace) by dragging the OPC UA element (right side of the editor) to the corresponding node of the server interface (reference namespace, "Local data" column).

   ![Procedure](images/142427612939_DV_resource.Stream@PNG-en-US.png)
5. Compile the project.

   After the compile, the newly generated nodes of the instances are located in the generated server interface of the "Companion specification" type. STEP 7 creates an object for each instance DB. The generated elements are located under each of these objects.

   Similarly, STEP 7 also creates an object for each global DB that is created when a UDT is instantiated.

   The generated companion specification interface cannot be changed (no longer possible: generating local data, importing companion specification). This measure provides protection against data loss in the event that the server interface was manually expanded and thus overwritten during a recompilation. Only the name of the generated companion specification interface can be modified.

   Furthermore, group folders that you have created to structure your data in the project tree of your TIA project are applied as "Folder" (node type) in the generated companion specification interface.

###### Create user program with FB types or UDT

How to create FBs and UDTs is not explained in detail here; for this purpose use the description for creating a user program, e.g. declare block interface and declare PLC data types (UDT).

###### Consistency check

The consistency check ("Consistency check" button of the editor) also checks the mapping of the data types and updates the display of the data types in the corresponding column of the editor.

##### Notes on configuration limits when using server interfaces (S7-1500, S7-1500T)

When you use OPC UA server interfaces, you must comply with limits for the following objects in line with the S7-1500 CPU performance class:

- Number of server interfaces
- Number of OPC UA nodes
- Load object data volume
- If you have implemented methods: Number of server methods or server method instances

###### Configuration limits for OPC UA server interfaces and methods

The table below sets out the configuration limits for S7-1500 CPUs; these must also be taken into account when you compile and load a configuration (up-to-date technical data of the CPUs can be found in the [Internet](https://support.industry.siemens.com/cs/ww/en/ps/td)).

A violation of configuration limits results in an error message.

Configuration limits for OPC UA server interfaces

| Technical specification value | CPU 1510SP (F)   CPU 1511 (C/F/T/TF)  CPU 1512C  CPU 1512SP (F)  CPU 1513 (F) | CPU 1505 (S/SP/SP F/SP T/SP TF)  CPU 1515 (F/T/TF)  CPU 1515 SP PC (F/T/TF)  CPU 1516 (F/T/TF) | CPU 1507S (F)  CPU 1517 (F/T/TF)  CPU 1518 (F) |
| --- | --- | --- | --- |
| Use of imported companion specifications (information models) |  |  |  |
| Maximum number of OPC UA server interfaces:  - "Companion specification" type - "Reference namespace" type - "Server interface" type | 10  20  10 | 10  20  10 | 10  20  10 |
| - Maximum number of OPC UA nodes in user-defined server interfaces | 1000 | 5000 | 30000 |
| - Maximum size of loadable OPC UA server interfaces | 1024 KB | 5120 KB | 8192 KB |
| Provision of methods |  |  |  |
| Maximum number of usable server methods or max. number of server method instances (instructions OPC_UA_ServerMethodPre, OPC_UA_ServerMethodPost) | 20 | 50 | 100 |

#### Providing methods on the OPC UA server (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Useful information about server methods (S7-1500, S7-1500T)](#useful-information-about-server-methods-s7-1500-s7-1500t)
- [Boundary conditions for using server methods (S7-1500, S7-1500T)](#boundary-conditions-for-using-server-methods-s7-1500-s7-1500t)

##### Useful information about server methods (S7-1500, S7-1500T)

###### Providing user program for server methods

On the OPC UA server of an S7-1500 CPU (as of firmware V2.5), you have the option of providing methods via your user program. These methods can be used by OPC UA clients, for example to start a manufacturing job using the method call of the S7-1500 CPU.

OPC UA methods, an implementation of "Remote Procedure Calls", provide an efficient mechanism for interactions between different communication nodes. The mechanism provides both job confirmation and feedback values so you no longer have to program handshaking mechanisms.

Using OPC UA methods, you can transfer data consistently without trigger bits/handshaking, for example, or trigger specific actions on the controller.

**How does an OPC UA method work?**

An OPC UA method in principle operates like a know-how protected function block that is called by an external OPC UA client in runtime.

The OPC UA client only "sees" the defined inputs and outputs. The content of the function block, the method or algorithm, remains hidden to the external OPC UA client. The OPC UA client receives feedback on successful execution and values returned by the function block (method), or an error message if execution has not been successful.

As the programmer, you have full control over and responsibility for the program context in which the OPC UA method runs.

**Rules for programming a method and runtime behavior**

- Make sure that the values returned by the OPC UA method are consistent with the input values provided by the OPC UA client.
- Follow the rules on assigning name and the structure of parameters, and the permitted data types (see description of the OPC UA server instructions).
- Behavior during runtime: The OPC UA server accepts **one** call per instance. The method instance is not available for other OPC UA clients until the call has been processed by the user program or has timed out.

The basic procedure for implementing a user program as a server method is set out below.

**Implementing a server method**

A program (function block) for implementing a server method is structured as follows:

1. **Querying the server method call with OPC_UA_ServerMethodPre**

   You first call the "OPC_UA_ServerMethodPre" instruction in your user program (i.e. in your server method).

   This instruction has the following tasks:

   - With this instruction you ask the OPC UA server of the CPU whether your server method was called from an OPC UA client.
   - If the method was called and the server method has input parameters, your server method now receives the input parameters.

     The input parameters of the server method come from the calling OPC UA client.
2. **Editing the server method**

   In this section of the server method, you provide the actual user program.

   You have the same options as in any other user program (for example, access to other function blocks or global data blocks).

   If the server method uses input parameters, these parameters are available to you.

   This section of the server method should only be executed if an OPC UA client has called the server method.

   After successful execution of the method, you set the output parameters of the server method if the method has output parameters.
3. **Responding to server method with OPC_UA_ServerMethodPost**

   To complete the server method, call the "OPC_UA_ServerMethodPost" instruction.

   Use the parameters to notify the "OPC_UA_ServerMethodPost" instruction whether or not the user program has been processed.

   If the user program has been successfully executed, the OPC UA server is notified via the relevant parameters. The OPC UA server then sends the output parameters of the server method to the OPC UA client.

Always call the instructions "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" as a pair irrespective of whether the user program is processed by both instructions or continued in the next cycle.

You will find an example of a server method implementation in the STEP 7 online help.

###### Integrating the server method

The diagram below shows how an OPC UA client (A) calls the server method "Cool":

The CPU executes the instance "Cool1" of the server method "Cool" in the cyclic user program ⑥.

The CPU first uses the instruction "OPC_UA_ServerMethodPre" to query ④ whether an OPC UA client has called the server method "Cool" ①.

- If the server method has not been called, program execution returns directly to the cyclic user program over ④ and ⑥. The CPU resumes the cyclic user program after "Cool1".
- If the server method has been called, this information is returned to the server method "Cool" over ④. The actual functionality is now executed in the Cool server method, see"<Method Functionality>" in the graphic.

  The server method then uses the instruction "OPC_UA_ServerMethodPost" ⑤ to notify the firmware (B) that the instruction has been executed ③.

  The firmware returns this information over ② to the calling OPC UA client (A).

  The CPU resumes the cyclic user program after "Cool1".

![Integrating the server method](images/136909377419_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **A** | Call of the server method and management of the "Done" information (method complete) |
| ① | Asynchronous call of the server method |
| ② | Asynchronous "Done" information for the method called (method complete) |
| **B** | Wait for OPC UA client calls, management of calls in the queue, forwarding of "Done" information from the cyclic user program to the OPC UA client |
| ③ | Data transfer from the OPC UA server to the method instances of the user program and vice versa |
| **C** | Check whether method has been called.   If it has, forwarding of input data from the OPC UA server to the method instance of the user program and feedback to the method instance that the method has been called ("called") |
| ④ | Synchronous call of the instruction OPC_UA_ServerMethodPre as a multi-instance stating the storage area for the input data from the OPC UA server.  The return value indicates whether or not the method has been called by the OPC UA client. |
| ⑤ | Check whether the method has been completed or is still active ("busy"). |
| **D** | Check whether the method has been completed.   If it has, the output data of the method instance is forwarded to the OPC UA server and the method instance is notified that the method has been completed. The OPC UA server is notified. |
| ⑥ | Call of the method FB (in this case: FB Cool) with the required instance and the process parameters |

###### Information about server instructions

The "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" are described in detail in the help to the Instructions > Communication > OPC UA > OPC UA server.

---

**See also**

Example program for providing a method for OPC UA clients
  
[Boundary conditions for using server methods (S7-1500, S7-1500T)](#boundary-conditions-for-using-server-methods-s7-1500-s7-1500t)
  
[Server instructions (S7-1200, S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#server-instructions-s7-1200-s7-1500)

##### Boundary conditions for using server methods (S7-1500, S7-1500T)

###### Permitted data types

If you provide server methods, observe the following rule:

- Assign the data types as shown below (SIMATIC data type - OPC UA data type). Other assignments are not permitted.

STEP 7 does not check the observance of this rule and does not prevent an incorrect assignment. You are responsible for the rule-compliant selection and assignment of the data types.

You can also use the listed data types, for example, as elements of structures/arrays/UDTs for input and output parameters of self-created server methods (UAMethod_InParameters and UAMethod_OutParameters).

| SIMATIC data type | OPC UA data type |
| --- | --- |
| BOOL | Boolean |
| SINT | SByte |
| INT | Int16 |
| DINT | Int32 |
| LINT | Int64 |
| USINT | Byte |
| UINT | UInt16 |
| UDINT | UInt32 |
| ULINT | UInt64 |
| REAL | Float |
| LREAL | Double |
| LDT | DateTime |
| WSTRING | String |
| DINT | Enumeration (Encoding Int32) and all derived data types |
| User-defined data type required (UDT, user-defined data type)  The user-defined data type must be created with the prefix "Union_", for example "Union_MyDatatype".  The first element (Selector) in this UDT must have the data type "UDINT". | UNION and all derived data types |

###### Number of implementable server methods and number of arguments

If you implement server methods via your user program, the number of usable methods is limited depending on the CPU type, see the following table (up-to-date technical data of the CPUs can be found in the [Internet](https://support.industry.siemens.com/cs/ww/en/ps/td)).

| Technical specification value | CPU 1510SP (F)   CPU 1511 (C/F/T/TF)  CPU 1512C  CPU 1512SP (F)  CPU 1513 (F) | CPU 1505 (S/SP/SP F/SP T/SP TF)  CPU 1515 (F/T/TF)  CPU 1515 SP PC (F/T/TF)  CPU 1516 (F/T/TF) | CPU 1507S (F)  CPU 1517 (F/T/TF)  CPU 1518 (F) |
| --- | --- | --- | --- |
| Maximum number of usable server methods or max. number of server method instances (OPC_UA_ServerMethodPre, OPC_UA_ServerMethodPost instructions) | 20 | 50 | 100 |
| Maximum number of arguments per method  (More than the specified number of arguments can be configured and loaded into the CPU, but an OPC UA client cannot call the method). | 20 | 20 | 20 |

**Error message when exceeded**

If the maximum number of server methods is exceeded, the OPC_UA_ServerMethodPre or OPC_UA_ServerMethodPost instructions report the error code 0xB080_B000 (TooManyMethods).

###### Supply of structured data types with nested arrays

If a structured data type (Struct/UDT) contains an array, the OPC UA server does not provide information about the length of this array.

If you use such a structure as the input or output parameter of a server method, for example, you must ensure that the nested array is supplied with the correct length when the method is called.

If you do not adhere to this rule, the method fails with the error code "BadInvalidArgument".

#### Providing alarms on the OPC UA server (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Useful information on alarms (S7-1500, S7-1500T)](#useful-information-on-alarms-s7-1500-s7-1500t)
- [OPC UA Events (S7-1500, S7-1500T)](#opc-ua-events-s7-1500-s7-1500t)
- [OPC UA conditions and OPC UA alarms (S7-1500, S7-1500T)](#opc-ua-conditions-and-opc-ua-alarms-s7-1500-s7-1500t)
- [Activating Alarms and Conditions (S7-1500, S7-1500T)](#activating-alarms-and-conditions-s7-1500-s7-1500t)
- [Subscribing to events of an OPC UA server (S7-1500, S7-1500T)](#subscribing-to-events-of-an-opc-ua-server-s7-1500-s7-1500t)
- [Processing associated values of alarms (S7-1500, S7-1500T)](#processing-associated-values-of-alarms-s7-1500-s7-1500t)
- [Methods for OPC UA Alarms and Conditions (S7-1500, S7-1500T)](#methods-for-opc-ua-alarms-and-conditions-s7-1500-s7-1500t)
- [Handling memory limits for OPC UA Alarms and Conditions (S7-1500, S7-1500T)](#handling-memory-limits-for-opc-ua-alarms-and-conditions-s7-1500-s7-1500t)

##### Useful information on alarms (S7-1500, S7-1500T)

Alarms allow you to detect errors in process control in the automation system quickly, to localize them precisely, and to eliminate them. This leads to a significant reduction in downtimes in a plant. The OPC UA information model "Alarms & Conditions" provides a standardized and platform-independent way of message processing.

As of firmware version V2.9, the OPC UA server of an S7-1500 CPU supports the OPC UA information model "Alarms and Conditions". In this way, the OPC UA server provides access to controller alarms.

The following sections describe which alarm types available in SIMATIC are supported at the OPC UA interface of the OPC UA server.

The following sections also describe how you configure the OPC UA server of the S7-1500 CPU for Alarms & Conditions, the main points of how the Alarms & Conditions model is structured with OPC UA, and which special points must be taken into consideration when using alarms from the address space of the OPC UA server as compared to the SIMATIC controller alarms of the CPU alarm system.

###### Basis for the converting alarms to OPC UA Alarms & Conditions

The Alarms and Conditions information model is specified in the "OPC 10000-9: OPC Unified Architecture Part 9: Alarms & Conditions" specification.

###### Controller alarms in SIMATIC

The OPC UA server of the S7-1500 CPUs supports the controller alarms listed below, which are available to S7-1500 CPUs. You configure or program these alarms in the usual way; for the placeholders that are possible in the alarms for SIMATIC, you need to consider the rules for use of these alarms by OPC UA clients.

The added benefit of OPC UA Alarms and Conditions is that these alarm types can be displayed not only by HMI devices, web browsers, the CPU display or the TIA Portal, but also by all OPC UA clients that support OPC UA Alarms and Conditions.

- PLC supervision alarms with ProDiag  
  You can integrate simple supervisions in your program with just a few configuring steps and without having to change the program code. The configuration of the supervisions is independent of the programming languages of the TIA Portal because only individual operands are supervised, and you do not need any additional programming sections.
- System diagnostics alarms  
  Configuration-dependent module events are known by the hardware configuration of the CPU and can be evaluated by connected display devices. They can only be viewed in the alarm editor and cannot be edited.
- Program alarms (Program_Alarm instruction)  
  For reporting program synchronous events, program alarms are assigned to one block at a time. They are created in the program editor and edited in the alarm editor (TIA Portal).
- GRAPH alarms  
  For GRAPH function blocks, you can also enable alarms; e.g. for interlocks, supervisions and GRAPH warnings (step time monitoring).

###### Important information on the alarm types

The following characteristics are significant to the differences in the behavior of alarms:

- Do alarms have a state (e.g. are they incoming, outgoing - with the corresponding time stamps)?
- Do alarms require acknowledgment?

If none of these characteristics apply, which means the alarms have no state and do not require acknowledgment, alarms simply provide information about an event that has occurred ("Fire and Forget"). It is up to the device receiving the alarm to buffer the alarm for further use or only for display.

###### Alarm class determines acknowledgment behavior

This section covers the setting options for program alarms. You can also set the behavior of the alarms for system diagnostics alarms and PLC supervision alarms (e.g. ProDiag supervision settings) - refer to the linked additional information for details.

You can find the setting options for program alarms in the alarm editor (double-click on "PLC supervisions and alarms" in the project tree, select the "Alarms" tab).

For the S7-1500 CPU, you set here via the alarm class whether an alarm needs to be acknowledged or not. In addition to the acknowledgment behavior, when creating a new alarm class, you define the default priority of alarms of this alarm class.

You set whether an alarm has a state or not by means of the "Information only" option, for example, at the alarm type; this results in "Fire-and-Forget" behavior of the alarm.

Here is an example with settings in the alarm editor with different alarm classes ("PLC supervisions and alarms" in the project tree):

- First line "Program_Alarm": Does not require acknowledgment, information only ("Fire and Forget").
- Second line "Program_Alarm_1": Requires acknowledgment and has a state, which means the alarm includes information on whether it is incoming or outgoing.
- Third line "Program_Alarm_2": Does not require acknowledgment and has a state, which means the alarm includes information on whether it is incoming or outgoing.

![Alarm class determines acknowledgment behavior](images/138660596363_DV_resource.Stream@PNG-en-US.png)

###### Display of alarms in the TIA Portal

During runtime, you have the option of viewing the alarms in the TIA Portal: The alarm display is located directly under the alarm editor ("Diagnostics" tab > "Alarm display" tab).

The following applies to the state and acknowledgment behavior:

- When you click on the "Current alarms" button, alarms that have been recently incoming, outgoing or acknowledged are displayed. Only alarms with a state and alarms requiring acknowledgment are displayed here. You can also acknowledge an alarm requiring acknowledgment (blue font) in this view via the shortcut menu or using the "Acknowledge" button.
- If you want to observe the chronological development (e.g. alarm came in, was acknowledged and went out), you need to click the "Alarm archive" button. The three events that belong to this alarm are listed one after another only in this view. You can only find the current state in the "Current alarms" view.
- Info reports (alarms with the "Information only" property) are only displayed in the "Alarm archive" view. Because these alarms are only triggered once and not buffered, they do not appear in the "Current alarms" view.
- PLC supervisions are also shown in the alarm display.
- System alarms usually belong to the "No Acknowledgement" alarm class with the "Information only" option. These alarms are logged in the diagnostics buffer in the CPU and thus allow the sequence of system alarms to be analyzed over a limited period. In contrast, operating state changes that are also logged in the diagnostics buffer have a state, which means it is indicated that or when a CPU went into STOP state and if or when it exited this state again, for example, entered RUN state. This information is displayed with the states "incoming/outgoing".

![Display of alarms in the TIA Portal](images/138678476683_DV_resource.Stream@PNG-en-US.png)

###### Provision of controller alarms by the OPC UA server

When an OPC UA client wants to receive alarms of the S7-1500 CPU, it needs to subscribe to OPC UA events (MonitoredEventItems).

For this purpose, the address space of the OPC UA server of the S7-1500 CPU contains corresponding nodes that are "Event-Notifiers" and create a subscription for the OPC UA clients to receive the alarms.

For completeness, we also mention that further type definitions are contained in the server address space for this purpose as nodes under "Types". Type definitions under "BaseEventType" and "ConditionType" ensure that the fields used by SIMATIC alarms are also provided in the OPC UA server.

After the activation of OPC UA Alarms and Conditions (CPU properties in the hardware configuration), the OPC UA address space of the S7-1500 CPU thus reflects the various alarm types (controller alarms) as described above:

- ProcessDiagnostics  
  Corresponds to the PLC supervision alarms with ProDiag
- SystemDiagnostics  
  Corresponds to the system diagnostics alarms
- UserProgram  
  Corresponds to the program alarms
- Graph  
  Corresponds to GRAPH alarms

By selecting the node for a subscription, you determine which alarm types are received by the OPC UA client. For example, the "Server" node enables receipt of all alarms, the "UserProgram" node only the receipt of program alarms.

Details about the OPC UA model for Alarms and Conditions are given in the next selection, especially for the "Overloads" node, you can find more information here: [Handling memory limits for OPC UA Alarms and Conditions](#handling-memory-limits-for-opc-ua-alarms-and-conditions-s7-1500-s7-1500t).

![Provision of controller alarms by the OPC UA server](images/140027850635_DV_resource.Stream@PNG-de-DE.PNG)

###### Preselection of the language for the OPC UA server

Alarms are transmitted from the OPC UA server to the OPC UA client in the default or reference language. For instructions for changing the language in the "Multilingual support" section of the CPU parameters, see [Multilingual](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#multilingual-s7-1500).

###### Additional information on the alarm types

The concepts and configuration options for controller alarms are not described further here. You can get to the corresponding descriptions via the following links.

---

**See also**

[Overview of the alarm display](Displaying%20alarms.md#overview-of-the-alarm-display)
  
[Introduction to alarm configuration (S7-300, S7-400, S7-1500)](Configuring%20alarms.md#introduction-to-alarm-configuration-s7-300-s7-400-s7-1500)
  
[Program_Alarm: Generate program alarm with associated values (S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#program_alarm-generate-program-alarm-with-associated-values-s7-1500)
  
[Get_AlarmState: Output alarm status (S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#get_alarmstate-output-alarm-status-s7-1500)

##### OPC UA Events (S7-1500, S7-1500T)

The basic concepts for alarm processing in OPC UA are expanded on here - the basic concept of "Events" is covered here. The terms used in the various parts of the OPC UA specification have been retained here.

###### Properties of events

In the address model of the OPC UA server, as of CPU firmware version V2.9, you not only have the option to access PLC tags (read, write) via nodes and to use methods - you can also receive events or alarms via nodes. In OPC UA terminology, these are called "events".

An event includes an event text (Message), time stamp (Time) and event source (SourceNode).

The information supplied with an event from the server depends on the event type. OPC UA defines a BaseEventType in part 5 of the specification (Information Model).

Other event types that provide different alarm behavior are derived from the BaseEventType. This type information of the different event types is visible in the address space of an OPC UA server ("Types" folder). This also applies, for example, to the event types of "Conditions" and "Alarms", which are discussed in the next section.

The OPC UA specification defines for the BaseEventType and for derived EventTypes which properties (fields) of an event are mandatory and which are optional.

The following sections show how specialized EventTypes are derived from the root of the derivation hierarchy, the BaseEventType. The SIMATIC-specific derivations ensure that the information supplied in SIMATIC with an alarm and displayed on an HMI device, for example, can also be subscribed to by an OPC UA client in the address space of the OPC UA server.

An event itself is not available as a node in the address space. Events are only triggered by nodes or objects that have the "Event-Notifier" property. These nodes are often also referred to as event signaling objects. Only nodes with this property can be specified as EventMonitoredItem in a subscription to receive corresponding events in the client.

Nodes that can trigger events with an S7-1500 CPU are objects such as "Server", the "SimaticAlarmsAndConditions" object below it, and the three objects below that, ProcessDiagnostics, SystemDiagnostics and UserProgram. The "EventNotifier" attribute is set for these objects in the address space of the OPC UA server of the CPU.

###### Definition of SimaticEventType

The figure below shows that the type "SimaticEventType" is derived directly from BaseEventType.

BaseEventType is the basic type definition for events with OPC UA.

All event types for OPC UA can be defined, directly or indirectly, based on BaseEventType.

![Definition of SimaticEventType](images/139624625035_DV_resource.Stream@PNG-de-DE.png)

The "SimaticEventType" type is defined in the SIMATIC namespace (http://www.siemens.com/simatic-s7-opcua).

SimaticEventType has all properties of BaseEventType as well as the special properties which are an image of the field structure of SIMATIC alarms.

###### Description of the event fields for SimaticEventType

The following table contains information on the fields of SimaticEventType for alarms of the type "Information only". Fields that are optional according to OPC UA and are not used by the OPC UA server of the CPU are omitted. You can also find a general description of the fields in the specification OPC 10000-5: OPC Unified Architecture, Part 5: Information Model, Release 1.04.

| BrowsePath | DataType | Explanations |
| --- | --- | --- |
| EventId | ByteString | Unique Event ID of the event |
| EventType | NodeId | Node ID of the event type |
| Time | UtcTime | Time stamp of the event (Event occurrence) |
| ReceiveTime | UtcTime | Current time stamp at which the OPC UA event was generated. |
| Message | LocalizedText | Event text |
| Severity | UInt16 | Priority of the alarm from SIMATIC (0..16), spread into a range from 1..1000 with OPC UA, see following table.   The priority indicates the urgency with which the event needs a response. |
| 3:AdditionalText_01 | LocalizedText | Optional additional text 1 |
| ... | ... | ... |
| 3:AdditionalText_09 | LocalizedText | Optional additional text 9 |
| 3:AssociatedValue_01 | 3:SimaticAssociatedAlarmValue | Optional associated value 1 (not for system diagnostics) |
| ... | ... | ... |
| 3:AssociatedValue_10 | 3:SimaticAssociatedAlarmValue | Optional associated value 10 (not for system diagnostics) |
| 3:InfoText | LocalizedText | Info text |
| 3:ID | UInt16 | Alarm number - A number (ID) assigned by the system that is unique within the CPU and identifies an alarm. |
| 3:DisplayClass | UInt16 | Display class (used by HMI devices. Determines the events displayed on specific HMI devices. |
| 3:GroupID | UInt8 | Acknowledgment group for alarms that are acknowledged together. |

###### Assignment of Priority (SIMATIC) - Severity (OPC UA)

The following table shows how the 17 priorities that you can assign to alarms in the SIMATIC environment are mapped to the 1000-level Severity with the OPC UA server of the S7-1500 CPU.

This assignment depends on the manufacturer. Different assignments may apply to other devices.

| OPC Range | Priority 0..16 (SIMATIC) | Severity 1..1000 (OPC UA) |
| --- | --- | --- |
| HIGH (667 – 1 000) | 16 | 1000 |
|  | 15 | 930 |
|  | 14 | 860 |
|  | 13 | 790 |
|  | 12 | 720 |
| MEDIUM (334 – 666) | 11 | 650 |
|  | 10 | 600 |
|  | 9 | 550 |
|  | 8 | 500 |
|  | 7 | 450 |
|  | 6 | 400 |
|  | 5 | 350 |
| LOW (1 – 333) | 4 | 300 |
|  | 3 | 225 |
|  | 2 | 150 |
|  | 1 | 75 |
|  | 0 | 1 |

##### OPC UA conditions and OPC UA alarms (S7-1500, S7-1500T)

The following goes further in depth about the basic concepts for OPC UA Conditions and OPC UA Alarms based on the explanations of events in the previous sections. Again, the terms used in the various parts of the OPC UA specification have been retained here.

###### Properties of Conditions

A prerequisite for understanding is the concept of "Events" in OPC UA.

In OPC UA, if an event alarm object provides status information in addition to its ability to fire Events, we speak of Conditions. Conditions represent a state of a system or one of its components. Basic states are "enabled" and "disabled", other state definitions are also possible.

In turn, interested OPC UA clients are notified of state changes by means of events (Condition Events).

An example of a Condition is state information, for example, that a device requires maintenance.

###### Properties of Alarms

However, the properties of ConditionType are not sufficient to completely map the characteristics of SIMATIC alarms in the OPC UA server.

From the ConditionType, which is derived from the BaseEventType, OPC UA defines further derived event types such as AcknowledgeableConditionType and AlarmConditionType.

AcknowledgeableConditionType supplements the properties of ConditionType with the "Acknowledgeable" characteristic (AckedState).

AlarmConditionType thus adds the "ActiveState" characteristic to the properties of ConditionType and the AcknowledgeableConditionType. In SIMATIC terminology, this is an incoming alarm. The ActiveState signals that the situation, which the Condition represents, is currently present or has occurred.

Example: A temperature has exceeded a limit. If "ActiveState" is not set, the situation that represents the condition no longer exists - this is usually referred to as a "normal state". In SIMATIC terminology, this corresponds to an outgoing alarm.

In OPC UA, other statuses such as SilenceState and ShelvingState are defined, but these are not relevant to mapping to the SIMATIC alarm system and will therefore not be described further here.

The SimaticAlarmConditionType is derived from the AlarmConditionType and contains all event fields to map the state and acknowledgment information of SIMATIC messages.

###### Definition of SimaticAlarmConditionType

The following figure shows how events of the type "SimaticAlarmConditionType" are defined by a series of expansions to the OPC UA "BaseEventType".

![Definition of SimaticAlarmConditionType](images/139624636939_DV_resource.Stream@PNG-de-DE.png)

###### Description of the event fields for SimaticAlarmConditionType

The following table contains information about the fields of SimaticAlarmConditionType for stateful and acknowledgeable alarms, which are added to the event fields such as SimaticEventType. Fields that are optional according to OPC UA and are not used by the OPC UA server of the CPU are omitted. You can also find a description of the fields in the specification OPC 10000-9: OPC Unified Architecture, Part 9: Alarms & Conditions, Release 1.04.

| BrowsePath | DataType | Explanations |
| --- | --- | --- |
| ConditionClassId | NodeId | Node IDs for SystemConditionClassType, ProcessConditionClassType or BaseConditionClassType are possible |
| ConditionClassName | LocalizedText | Display name of the ConditionClassId |
| Retain | Boolean | Indicates that the alarm is still relevant for OPC UA clients (set if alarm is still pending and not acknowledged). |
| Comment | LocalizedText | - Most recent comment entered using the "AddComment" or "Acknowledge" method. - ZERO after a server restart and if no comment was entered. |
| Comment.SourceTimestamp | UtcTime | Time stamp for the last change of the comment field |
| AckedState | LocalizedText | "Acknowledged" or "Unacknowledged" |
| AckedState.Id | Boolean | Set, if acknowledged |
| AckedState.TransitionTime | UtcTime | Time at which the alarm was acknowledged.   ZERO if not acknowledged or not acknowledgeable. |
| ActiveState | LocalizedText | "Active" or "Inactive" |
| ActiveState.Id | Boolean | Set when "active" |

##### Activating Alarms and Conditions (S7-1500, S7-1500T)

###### Requirements

- S7-1500 CPU as of firmware version 2.9
- Runtime license for OPC UA were purchased according to the license specifications and set in the CPU properties
- Parameter "Central alarm management in the PLC" is enabled (area "PLC alarms" in the CPU properties).

###### Procedure

To activate alarms through OPC UA Alarms and Conditions, proceed as follows:

1. In the CPU properties, go to the "OPC UA > Server > General" area.
2. Select the "Enable Alarms and Conditions on the OPC UA server" option.   
   The corresponding types and objects that can trigger events only become visible in the address space when the option is activated.
3. If required, also activate the option "Allow message acknowledgment by OPC UA client".  
   In this case, every connected OPC UA client can acknowledge a message requiring acknowledgment with the "Acknowledge" method.

![Procedure](images/149943619083_DV_resource.Stream@PNG-en-US.png)

###### Recommendation: Activate diagnostics "Requests of a remote OPC UA client failed"

When the OPC UA server cannot allocate sufficient memory, it is not possible to generate OPC UA alarms in this state. A message loss for OPC UA clients is possible.

Therefore, you should activate the diagnostics "Requests of a remote OPC UA client failed" to diagnose this state (Properties of the CPU > OPC UA > Server > Diagnostics).

In addition, you should also activate the option "Summarize diagnostics in case of high message volume".

As soon as sufficient memory is available again, OPC UA clients should call the ConditionRefresh method to receive the current state of the alarm system.

---

**See also**

[Requests of a remote OPC UA client failed (S7-1500, S7-1500T)](#requests-of-a-remote-opc-ua-client-failed-s7-1500-s7-1500t)
  
[Methods for OPC UA Alarms and Conditions (S7-1500, S7-1500T)](#methods-for-opc-ua-alarms-and-conditions-s7-1500-s7-1500t)

##### Subscribing to events of an OPC UA server (S7-1500, S7-1500T)

###### Subscribing to all events via the "Server" node

OPC UA servers provide events via the "Server" node and lower-level nodes. When OPC UA clients subscribe to the "Server" node, they receive all events and alarms of the OPC UA server.

The "Server" node is located in the "Objects" folder below "Root".

OPC UA servers inform OPC UA clients which event types they use (under "Root > Types > EventTypes" in the address space).

###### Filter options for events

OPC UA clients can choose and only subscribe to specific nodes under the "Server" node and thus to specific event types, for example, only the "UserProgram" node. This reduces the number of events from the OPC UA server to program alarms.

Another way of filtering is to select the event fields, known as "Select Clause" in OPC UA terminology.

This means that in the subscription, the OPC UA client makes a selection of the event fields in addition to the event alarm object (e.g. the "UserProgram" node). You select the event fields via the browse name of the corresponding field.

OPC UA also defines so-called "Where Clauses". A Where Clause in the event filter is used to further limit the number of events that are supplied by the OPC UA server for the selected object, for example, by filtering to a severity range.

###### Example client UaExpert

The example of the UaExpert OPC UA client shows how events of an OPC UA server can be received via a subscription. Here is the most important information on the displayed events/alarms:

- Event View is a separate view of events in addition to the Data Access View.
- The "Configuration" area contains the selected event signaling object with the fields for the Select Clause. A configuration of Where clauses is currently not possible in UaExpert.
- In the "Events" area, "Events" tab: Corresponds to the TIA alarm view with activated "Alarm archive" button; events of the "Information only" category and outgoing alarms are also visible there, because UaExpert buffers them in the background for display. These events are not visible in the "Alarms" tab.
- In the "Events" field, "Alarms" tab: Corresponds to the TIA alarm display with activated "Current alarms" button; alarms are visible here with their status, e.g. "active" (corresponds to "incoming") and these alarms can also be acknowledged using the shortcut menu. Outgoing alarms are no longer visible in this view.

In the columns of the Event area, a selection of event fields is offered, for example, the event text (Message) and whether the alarm was acknowledged (A=Acknowledged).

![Example client UaExpert](images/138927756683_DV_resource.Stream@PNG-de-DE.png)

###### Special features of the display of alarms via the OPC UA server of the CPU

The following once again summarizes the special features of the alarm display via OPC UA Alarms and Conditions for the current status.

| Topic | Explanation |
| --- | --- |
| Comment | Via OPC UA, you can add a comment to a alarm using the "AddComment" method or the "Acknowledge" method. This comment is no longer available after a server restart. |
| Pending alarms are not lost after a server restart | The OPC UA server supports the "ConditionRefresh" method with which it makes the current state of the system available to the OPC UA client, for example, after download of a new data block (requires server restart and connection re-establishment). |

##### Processing associated values of alarms (S7-1500, S7-1500T)

You can specify placeholders for SIMATIC alarms. With placeholders you can integrate up to 10 associated values (SD_1 to SD_10) into the alarm text. Placeholders can also be specific text list entries.

When you are using alarms with placeholder, you must observe the following rules:

- Placeholders that represent values in the alarm are only inserted automatically for system diagnostic alarms or security event alarms. For other categories of alarms (e.g. program alarms), the placeholders for values are not resolved. The OPC UA clients must resolve these alarms.
- Placeholders that reference text lists are resolved by the CPU (format, e.g.: %t#<name of the text list>).

###### Example of how values and placeholders are assigned through UaExpert

1. Make sure that you have selected all fields that you need in the UaExpert configuration.

   Note that each field that is not needed causes a communication load. Therefore, you should avoid a complete selection as shown in the example below.

   ![Example of how values and placeholders are assigned through UaExpert](images/149958283019_DV_resource.Stream@PNG-de-DE.png)
2. In the "Events" tab of UaExpert, you select the alarm with the integrated associated values.  
   In the "Details" area of the alarm, you will find the value that is to be integrated into the alarm.   
   Example: "AssociatedValue_01" is assigned to SD_1 (format @1% ...@).   
   You will find explanations on the formats for associated values in the TIA Portal information system (e.g. by searching for "Example of associated values".

###### Support of simple data types as associated values

The field type from "AssociatedValue_01 to ..._10 is of the Union type and is limited to some simple types. The OPC UA data type is SimaticAssociatedAlarmValue. The following simple data types are supported:

![Support of simple data types as associated values](images/149959228683_DV_resource.Stream@PNG-de-DE.png)

###### Mapping to SIMATIC data types

The following assignment SIMATIC data type => OPC UA data type applies:

| Supported data types for SD_1 to SD_10 | Mapping to OPC UA |
| --- | --- |
| BOOL | Boolean |
| BBOOL | Boolean |
| BYTE | Byte |
| CHAR | Byte |
| SINT | SByte |
| USINT | Byte |
| WORD | UInt16 |
| WChar | UInt16 |
| INT | Int16 |
| UINT | UInt16 |
| DWORD | Uint32 |
| DINT | Int32 |
| UDINT | Uint32 |
| REAL | Float |
| LREAL | Double |
| String | String |
| WString | String |

##### Methods for OPC UA Alarms and Conditions (S7-1500, S7-1500T)

The OPC UA specification Part 9 (OPC 10000-9: Alarms & Conditions) defines methods for OPC UA servers to enable OPC UA clients to react to state changes, for example.

In the following, the methods are described that are supported by the OPC UA server of the S7-1500 CPU with their special features.

###### Requirement

Using the relevant methods for the Alarms and Conditions functionality requires the following:

- Alarms and Conditions is activated
- For the "Acknowledge" method, the acknowledgment of alarms by OPC UA clients must be allowed on the server side.

###### Methods for OPC UA Alarms and Conditions

In the following, the methods are briefly explained with the special features and restrictions caused by the implementation for the OPC UA server of the S7-1500 CPU.

The methods are visible in the type space.

The OPC UA specification listed above contains the general description.

You can find a detailed description of the individual methods below this overview table.

| Method | Description |
| --- | --- |
| Acknowledge | Method for acknowledging an alarm object that is uniquely identified by a EventId. |
| ConditionRefresh | Method for requesting an update of all alarm objects (in SIMATIC language: updating of all pending alarms). All monitored items of the subscription are updated.  Synchronization of pending alarm objects from the OPC UA server of the CPU is indicated e.g. in the following situations:   - Connecting for the first time or resuming the connection (after interrupting the communication) - Screen change on an operator screen of an HMI device |
| AddComment | Method for adding comments to alarm objects. |

###### Calling the "Acknowledge" and "AddComment" methods

Method calls in OPC UA use MethodId and ObjectId.

In the case of an alarm object, ObjectId is the node ID for the instance of the alarm object.

Since the address model of Simatic Alarms and Conditions does not provide instances for alarm objects, the OPC UA specification provides in this case that the OPC UA client uses the ConditionId as ObjectId.

You can find information on how to determine the ConditionId using a SimpleAttributeOperands in the SelectClause of the event filter, see also the OPC UA specification Part 9 (OPC 10000-9: Alarms & Conditions):

![Calling the "Acknowledge" and "AddComment" methods](images/139795978891_DV_resource.Stream@PNG-de-DE.png)

###### Acknowledge

The Acknowledge method (MethodId: i=9111) has the following parameters:

| Parameter | Data type | Description |
| --- | --- | --- |
| [in] EventId | ByteString | EventId identifies a specific event notification.   Only events whose AckedState.Id field has the value "False", can be acknowledged with the "Acknowledge" method. |
| [in] comment | LocalizedText | Text for commenting the acknowledgment, e.g. by an operator.  See also supplementary description of the "AddComment" method. |

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Good | Method was successfully executed. |
| BadNotSupported | Method cannot be called because the option for acknowledging for Alarms and Conditions by OPC UA clients is deactivated in the CPU properties for OPC UA. |
| BadConditionBranchAlreadyAcked | Acknowledgment has already been made. |
| BadNodeIdUnknown | Method was called with the wrong ConditionId (see notes on ObjectId). |
| BadEventIdUnknown | Method was called with the wrong EventId. |

###### ConditionRefresh

The ConditionRefresh method (MethodId: i=3875) has the following parameters:

| Parameter | Data type | Description |
| --- | --- | --- |
| [in] SubscriptionId | Uint32 | SubscriptionId of the subscription to be updated. |

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Bad_SubscriptionIdInvalid | The SubscriptinId is not valid. |
| Bad_RefreshInProgress | The "ConditionRefresh" is currently running. |
| Bad_UserAccessDenied | The method "ConditionRefresh" runs in the context of a wrong session. This means that the subscription belongs to a different session. |

> **Note**
>
> **ConditionRefresh2 method**
>
> The OPC UA server of the S7-1500 CPU does not support the ConditionRefresh2 method which can specifically synchronize a monitored item (MonitoredItem) in a subscription. In this case, the OPC UA Server returns the result code "Bad_MethodInvalid". Use the method "ConditionRefresh" instead.

###### AddComment

You have the possibility to add comments to Alarms- objects of the SimaticAlarmConditionType type because the support of comments is mandatory for OPC UA Alarms and Conditions .

A comment was save in the "Comment" event field.

The following time stamp event fields belong to the comment:

- "Comment.SourceTimestamp" for the time when the comment is transferred to the CPU
- "Time" for the time when the Alarms object was modified

When the "AddComment" method is called, "Time" and "Comment.SourceTimestamp" are identical.

**Special features of Alarms and Conditions comments for the OPC UA server of the CPU**

The AddComment method (MethodId: i=9029) has the following parameters:

| Parameter | Data type | Description |
| --- | --- | --- |
| [in] EventId | ByteString | EventId identifies the event notification for which a state was reported. |
| [in] comment | LocalizedText | Text for commenting the specified Alarms object. |

**Method Result Codes**

| Result Code | Description |
| --- | --- |
| Good | Method was successfully executed. |
| BadNodeIdUnknown | Method was called with the wrong ConditionId (see notes on calling the methods "Acknowlege" and "AddComment"). |
| BadEventIdUnknown | Method was called with the wrong EventId. |

###### Special features of Alarms and Conditions comments for the OPC UA server of the CPU

You have the possibility to add comments to alarm objects of the "SimaticAlarmConditionType" type with the AddComment method. A comment is also set when the Acknowledge method is called. The "AddComment" method can be called several times.

- A comment was save in the "Comment" event field. The "Comment.SourceTimestamp" indicates the last time at which a **comment** was set.
- The "Time" time stamp marks the **last modification time of the alarm object**.

When the "AddComment" method is called, "Time" and "Comment.SourceTimestamp" are identical.

When the "Acknowledge" method is called, the two time stamps may differ, since the acknowledgment is asynchronous.

The support of comments for OPC UA Alarms and Conditions is mandatory. The SIMATIC alarm system does not know corresponding comments for alarms. Therefore, some special features have to be considered:

- There is only one comment:  
  There is only one comment for an alarm object, so that an existing comment is always overwritten when several method calls are made in succession.
- Lifetime and time stamp:  
  Comments are only stored at the current alarm object. If the alarm object no longer exists, e.g. after a server restart, the comment no longer exists either. The corresponding "Comment" and "Comment.SourceTimestamp" event fields are then reset (zero).   
  The "Time" event field is then set as if the method call "AddComment" did not exist. Example: If you comment on an unacknowledged Alarms object, the "Time" event field receives the time of this comment change. After a server restart, the "Time" event field does not show the time when the comment was set, but the time when the corresponding Event arrived.

##### Handling memory limits for OPC UA Alarms and Conditions (S7-1500, S7-1500T)

The OPC UA server of the S7-1500 CPU has product-specific limited memory capacity for the "Alarms and Conditions" function (see CPU specifications).

Two memory pools for different categories of alarms are available:

- Pool only for ProgramAlarms (corresponds to program-related alarm originators (producers) such as program alarms via Program_Alarm, ProDiag, Graph)
- Pool only for SystemDiagnostics (corresponds to system diagnostic alarms)

Under unfavorable conditions (e.g. alarm burst) the CPU cannot make all pending alarms (ProgramAlarms or SystemDiagnostics) from the SIMATIC alarm area available to the OPC UA Alarms and Conditions system. However, alarms are not lost in this case.

You have the possibility to react to this overload event in the user program. According to your application you can use the "ConditionRefresh" method to make alarms that "did not make it into the OPC UA Alarms and Conditions system" available to the OPC UA Alarms and Conditions system again.

###### Requirement

- Alarms and Conditions is activated
- Event subscriptions are set up in the OPC UA client

###### Principle

The following figure shows a simplified process for temporarily storing ProgramAlarms to make them available again at another time for the OPC UA Alarms and Condition System. The nodes mentioned in the caption are visible in the following image of the address model.

![Principle](images/140096877579_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Number of active alarms is too high to make all alarms accessible via OPC UA Alarms and Conditions |
| ② | Overloads alarm (overload alarm) is triggered. This overload alarm is active until the following situation occurs:  - No more alarms are pending for the OPC UA Alarms and Conditions system (OutstandingProgramAlarms = 0) and - Number of alarms in the OPC UA Alarms and Conditions system < Hysteresis-cleaned maximum value for OPC UA alarms (= MaxAlarmsInQueue - OverloadHysteresis)   Alarms that are not available in the OPC UA Alarms and Conditions system due to the overload situation are buffered by the CPU as "OutstandingAlarms". |
| ③ | When an OPC UA client executes the ConditionRefresh method, not only are all alarm objects of the relevant subscription synchronized, but also the alarms outstanding for OPC UA Alarms and Conditions (OutstandingAlarms) are transferred to the Alarms and Conditions memory area - until the maximum number of alarms is reached. "Oldest" alarms are transferred first. After that every subscription to these alarms receives the transferred alarms - not only the OPC UA client that called the ConditionRefresh method. |
| ④ | The OPC UA client controls the handling of pending alarms via the information of the Overloads nodes. |

###### Address model for Alarms and Conditions

The following figure shows the nodes of the OPC UA Alarms and Conditions address model.

![Address model for Alarms and Conditions](images/139974762379_DV_resource.Stream@PNG-de-DE.PNG)

###### Special features

- When pending alarms go out or are acknowledged, they no longer enter the OCP UA Alarms and Conditions system area via the ConditionRefresh method. They are then "invisible" to OPC UA Alarms and Conditions and thus to the connected OPC UA clients. This fact influences e.g. statistical evaluations of alarm progressions.
- To avoid a high alarm frequency for the Overloads Alarm if the number of alarms oscillates around the maximum value, the limit for triggering the alarm is higher than the limit for canceling this alarm: The value for this difference is displayed in the "OverloadHysteresis" node.   
  Example: Maximum number of alarms: 200, OverloadHysteresis: 3.  
  Overloads alarm is triggered starting with 200 alarms and is only canceled if there are fewer than 197 alarms. If the number of alarms increases again, it will be triggered again when 200 alarms are exceeded.

### Using the S7-1500 CPU as an OPC UA client (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Overview and requirements (S7-1500, S7-1500T)](#overview-and-requirements-s7-1500-s7-1500t)
- [Useful information about the client instructions (S7-1500, S7-1500T)](#useful-information-about-the-client-instructions-s7-1500-s7-1500t)
- [Number of client instructions that can be used simultaneously (S7-1500, S7-1500T)](#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t)
- [Example configuration for OPC UA (S7-1500, S7-1500T)](#example-configuration-for-opc-ua-s7-1500-s7-1500t)
- [Creating client interfaces (S7-1500, S7-1500T)](#creating-client-interfaces-s7-1500-s7-1500t)
- [Determine server interface online (S7-1500, S7-1500T)](#determine-server-interface-online-s7-1500-s7-1500t)
- [Using multilingual texts (S7-1500, S7-1500T)](#using-multilingual-texts-s7-1500-s7-1500t)
- [Rules for the access to structures (S7-1500, S7-1500T)](#rules-for-the-access-to-structures-s7-1500-s7-1500t)
- [Using connection parameter assignment (S7-1500, S7-1500T)](#using-connection-parameter-assignment-s7-1500-s7-1500t)

#### Overview and requirements (S7-1500, S7-1500T)

With STEP 7 (TIA Portal) Version V15.1 and higher, you can assign parameters and program an OPC UA client that can read PLC tags in an OPC UA server. Furthermore it is possible to transfer new values for PLC tags to an OPC UA server. In addition, you can call methods that an OPC UA server provides in your user program. You use the instructions for OPC UA clients in your user program for this.

The instructions of the OPC UA client are based on the standard "PLCopen OPC UA Client for IEC61131-3".

##### PLCopen specification

With these standardized instructions, you can develop an OPC UA client functions in your user program that can be executed in an S7-1500 CPU.

In addition, it is possible with just a few adaptations to run this user program in controllers of other manufacturers if these manufacturers have also implemented the OPC UA Specification "PLCopen OPC UA client for IEC61131-3".

##### Convenient editors in STEP 7

For the parameter assignment of the instructions for OPC UA clients, a convenient editor is available in the TIA Portal – the [connection parameter assignment](#enabling-the-opc-ua-server-s7-1500-s7-1500t).

As of Version 15.1, STEP 7 also features an [editor for client interfaces](#creating-client-interfaces-s7-1500-s7-1500t).

This section describes how you work with these editors.

First, you will be shown how to create and configure a new interface with the interface editor, because you need this type of interface for the subsequent connection parameter assignment.

The description uses an example for better comprehensibility, see [Description of the example](#example-configuration-for-opc-ua-s7-1500-s7-1500t).

##### Requirements

- You have the required runtime license for OPC UA and have configured the license in STEP 7 (CPU Properties > Runtime Licenses).
- The client of the S7-1500 CPU is activated.
- If the CPU as OPC UA client is to read and write **structures** in the OPC UA server: The OPC UA server must support version V1.04 of the OPC UA specification.

##### Enabling the OPC UA client of the CPU

To use the client of the S7-1500 CPU, you must enable it:

1. Select the area "OPC UA > Client" in the properties of the CPU.
2. Select the "Enable OPC UA client" option.

If you do not enable the client, the connection is not established. You receive a corresponding error message at the instructions, for example "OPC_UA_Connect".

For information about the application name, which also applies to the server and the client, see [here](#enabling-the-opc-ua-server-s7-1500-s7-1500t).

##### Overview

To use the editor and the connection parameter assignment, follow these steps:

1. First, specify a client interface. Add to this the PLC tags and PLC methods interface that you want to access ("[First step](#creating-client-interfaces-s7-1500-s7-1500t)").
2. Next, configure the connection to the OPC UA server ([Second step](#creating-and-configuring-connections-s7-1500-s7-1500t)).
3. Finally, use the configured connection for the OPC UA client instructions ([Third step](#using-a-configured-connection-s7-1500-s7-1500t)).

#### Useful information about the client instructions (S7-1500, S7-1500T)

With the standardized OPC UA client instructions you are able to control communication for the following tasks with the S7-1500 CPU as an OPC UA client:

- Read/write tags of the OPC UA server
- Call methods in the OPC UA server

Optional instructions can be used to determine the following information:

- The status of the connection between the OPC UA client and OPC UA server
- Node IDs of nodes with known hierarchy of the address space

> **Note**
>
> **Compact instructions as of STEP 7 version V17**
>
> Similar to the compact instructions for Open User Communication, as of STEP 7 version V17 compact instructions are also available for OPC UA, which bundle connection establishment and data exchange/method call in one instruction. For more information, see the reference part of the Help, see [Compact instructions](Communication%20%28S7-1200%2C%20S7-1500%29.md#compact-instructions-s7-1500).

##### Standardized sequence of OPC UA communication

The sequence of the communication, and thus the order of the instructions, follows a pattern that is illustrated in the following.

Run sequence for a read or write operation

![Standardized sequence of OPC UA communication](images/109275317515_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for "clean-up" after a completed read or write operation |

**Run sequence for a method call in the OPC UA server**

![Standardized sequence of OPC UA communication](images/125984626955_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of method calls |
| ② | Method calls |
| ③ | Instructions for "clean-up" after completed method calls |

**Optional instructions (reading out the status of a connection / reading out node IDs of nodes with known hierarchy of the address space)**

- OPC_UA_ConnectionGetStatus
- OPC_UA_TranslatePathList

![Standardized sequence of OPC UA communication](images/104430498187_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations with inserted instruction for requesting, for example, the NodeIDs of nodes of the OPC UA server. |
| ② | You can determine the connection status between the establishment and termination of the connection in parallel with other instructions. |
| ③ | Instructions for "clean-up" |

##### Convenient editors in STEP 7

The OPC UA client instructions are described in detail in the reference part (STEP 7 information system). For parameter assignment of the instructions, a convenient editor is available in the TIA Portal – the [connection parameter assignment](#creating-and-configuring-connections-s7-1500-s7-1500t).

We recommend starting with the connection parameter assignment for the first program draft and using additional instructions and manually optimizing the program as required.

##### Information about the client instructions

The client instructions are described in detail in the help to the Instructions > Communication > OPC UA > OPC UA client.

##### Application example in Online Support

This [application example](https://support.industry.siemens.com/cs/ww/en/view/109762770) provides you with an S7 user block "OpcUaClient" that summarizes the most important functions of the OPC UA instructions, accelerates the implementation for you and simplifies the programming. The OPC UA server in the example is an S7-1500 controller with a simple simulation program for process values.

The S7 user block performs the following:

- Establishment and termination of the connection to the server
- Diagnostics of the connection and automatic reconnection after connection terminations
- Registered Read
- Registered Write
- Registered Method Call

#### Number of client instructions that can be used simultaneously (S7-1500, S7-1500T)

##### SIMATIC error codes for OPC UA client instructions

The following limits apply to the simultaneous use of OPC UA client instructions. You can find the technical specifications of the S7-1500 CPU variants, updated daily, here:

- [Advanced Controller (Std. S7-1500 CPUs)](https://support.industry.siemens.com/cs/ww/en/ps/13717/td)
- [Distributed Controller](https://support.industry.siemens.com/cs/ww/en/ps/13888/td)
- [SW Controller](https://support.industry.siemens.com/cs/ww/en/ps/13912/td)
- [Drive Controller](https://support.industry.siemens.com/cs/ww/en/ps/25714/td)

Quantity structures for OPC UA client instructions

| OPC UA instruction | Maximum number for   CPU 1510SP (F)   CPU 1511 (C/F/T/TF)  CPU 1512C  CPU 1512SP (F)  CPU 1513 (F) | Maximum number for   CPU 1505 (S/SP/SP F/SP T/SP TF)  CPU 1515 (F/T/TF)  CPU 1515 SP PC (F/T/TF)  CPU 1516 (F/T/TF) | Maximum number for   CPU 1507S (F)  CPU 1517 (F/T/TF)  CPU 1518 (F) |
| --- | --- | --- | --- |
| OPC_UA_Connect | 4 | 10 | 40 |
| OPC_UA_NamespaceGetIndexList | 4* | 10* | 40* |
| OPC_UA_NodeGetHandleList | 4* | 10* | 40* |
| OPC_UA_MethodGetHandleList | 4* | 10* | 40* |
| OPC_UA_TranslatePathList | 4* | 10* | 40* |
| OPC_UA_ReadList | 20 in total (max. 5 per connection, see OPC_UA_Connect) | 50 in total (max. 5 per connection, see OPC_UA_Connect) | 200 in total (max. 5 per connection, see OPC_UA_Connect) |
| OPC_UA_WriteList | 20 in total (max. 5 per connection, see OPC_UA_Connect) | 50 in total (max. 5 per connection, see OPC_UA_Connect) | 200 in total (max. 5 per connection, see OPC_UA_Connect) |
| OPC_UA_MethodCall | 20 in total (max. 5 per connection, see OPC_UA_Connect) | 50 in total (max. 5 per connection, see OPC_UA_Connect) | 200 in total (max. 5 per connection, see OPC_UA_Connect) |
| OPC_UA_NodeReleaseHandleList | 4* | 10* | 40* |
| OPC_UA_MethodReleaseHandleList | 4* | 10* | 40* |
| OPC_UA_Disconnect | 4* | 10* | 40* |
| OPC_UA_ConnectionGetStatus | 4* | 10* | 40* |
| * maximum 1 per connection |  |  |  |

##### Maximum number of usable OPC UA client interfaces

If you create OPC UA client interfaces using the connection parameter assignment, the number of client interfaces is limited to max. 40.

Create the OPC UA client interfaces by double-clicking the "Add new client interface" symbol in the project tree of the "OPC UA communication" area.

The maximum number of OPC UA client interfaces is independent of whether you also use the CPU as OPC UA server.

#### Example configuration for OPC UA (S7-1500, S7-1500T)

The following sections describe how you can use the client interfaces editor and the connection parameter assignment.

The description is based on a specific example: Two S7-1500 CPUs operate in the system: One CPU serves as the OPC UA client and the other as the OPC UA server.

You can, of course, also use controllers, sensors and IT systems of other manufacturers as OPC UA clients or servers. In particular, the data exchange between different systems (interoperability) is a major advantage of OPC UA.

##### Connection parameter assignment using an example:

The plant produces blanks in a production line.

The following controllers are used:

1. An S7-1511 CPU serves as the controller of the production line.

   The controller is named "**Productionline**" in the example.

   The OPC UA server of the controller is enabled.

   The CPU has the IP address 192.168.1.1 in the example.

   This CPU publishes the values of following tags via the OPC UA server:

   - **NewProduct**

     The tag has the data type "BOOL".

     When this PLC tag has the value TRUE, the production line has processed a blank.

     The blank is ready for pick-up.
   - **ProductNumber**

     This tag contains the identification number of the blank.

     The tag has the data type "Int".
   - **Temperature**

     This tag contains temperature values recorded during the production of the blank.

     The tag is an array with elements of the "Real" data type.

   In addition, this CPU provides the following writable tag:

   - **ProductionEnabled**

     The tag is set by the OPC UA client.

     The tag has the data type "BOOL".

     If the value is set to TRUE, the production line is released and may produce blanks.

   In addition, this CPU provides the following method via the OPC UA server:

   - **OpenDoor**.

     OPC UA clients can hereby arrange for an access door to be opened to the production line.
2. An S7-1516 CPU controls the interaction with other production lines.

   This CPU is named "**Supervisor**" in the example.

   The OPC UA client of this CPU is enabled.

   Using OPC UA, this CPU can read the NewProduct and ProductNumber tags, set the ProductionEnabled tag and call the OpenDoor method.

   The CPU has the IP address 192.168.1.2 in the example.

The following figure shows the example in the network view of the TIA Portal:

![Connection parameter assignment using an example:](images/109116001035_DV_resource.Stream@PNG-de-DE.png)

#### Creating client interfaces (S7-1500, S7-1500T)

As of Version 15.1, the TIA Portal has an editor for client interfaces.

You group all PLC tags that you want to read or write from an OPC UA server in a client interface.

In addition, the client interface contains all methods that the OPC UA server provides and that you want to call with your user program (that acts as an OPC UA client).

If you create a client interface, STEP 7 creates data blocks for the parameter assignment of the connection to the OPC UA server from which you want to read data or to which you want to write data.

**Maximum number of client interfaces**

You can create a maximum of 40 client interfaces.

##### Requirement for access to structures on the server

The following requirement must be met to be able to read and write **structures** on the OPC UA server:

- The OPC UA server must support version V1.04 of the OPC UA specification.

If it does not, the node cannot be added to a read or write list and the CPU as OPC UA client generates an error message.

Background: The OPC UA specification Part 3 (Address Space Model) V1.04 requires the DataTypeDefinition attribute for structured data types. If the attribute is missing in the OPC UA server, as is the case with servers with version V1.03, for example, the CPU as OPC UA client cannot access structures in the OPC UA server.

##### Editor for client interfaces

To create a client interface, follow these steps:

1. Select the project view in the TIA Portal.
2. In the "Devices" area, select the CPU you want to use as an OPC UA client.
3. Click "OPC UA communication > Client interfaces".
4. Double-click "Add new client interface".

   STEP 7 creates a new client interface and display in the editor.

   ![Editor for client interfaces](images/109865884171_DV_resource.Stream@PNG-en-US.png)

   ![Editor for client interfaces](images/109865884171_DV_resource.Stream@PNG-en-US.png)

   STEP 7 names the new interface "Client interface_1". If a "Client interface_1" already exists, the new interface receives the designation "Client interface_2" etc.

   In addition, STEP 7 creates the following data blocks:

   - Client_Interface_1_Configuration

     The data block already contains all system data types that are needed for the instructions of the OPC UA client.

     This data block is filled when you configure the connection to the OPC UA server.

     You configure a connection in the properties of the client interface, see: [Example configuration for OPC UA](#example-configuration-for-opc-ua-s7-1500-s7-1500t).
   - Client_Interface_1_Data

     A data block for the PLC tags that you want to read or write from an OPC UA server as well as for methods that you want to call in the OPC UA server.

     You use this data block in your user program.

     This data block is currently still empty.
5. Select a descriptive name for the new client interface.

   Select "Productionline" in the example.

   This also changes the names of the associated data blocks to:

   - Productionline_Data
   - Productionline_Configuration
6. To import an OPC UA server interface, click the "Import interface" button in the top right of the editor.

   This allows you to import an XML file which describes the server interface of an OPC UA server.

   Alternative: To determine online the server interface of a connected OPC UA server, see: [Determine server interface online](#determine-server-interface-online-s7-1500-s7-1500t).
7. STEP 7 displays a dialog with which you can select an XML file.

   This XML file describes a address space of an OPC UA server.

   The address space of an OPC UA server contains all PLC tags and server methods published by an OPC UA server.

   OPC UA clients can access this address space:

   - Read PLC tags

   - Write PLC tags

   - Calling Server Methods

   The address space of an OPC UA server can be divided into one or more server interfaces.

   For creating server interfaces, see: [Creating a server interface for companion specification](#creating-a-server-interface-for-companion-specification-s7-1500-s7-1500t).
8. Create a **read list** in this client interface.

   To do this, follow these steps:

   - Click "Add new read list" in the left section of the editor.

     STEP 7 adds a new list named "ReadList_1".

     For the example, change the name to "ReadListProduct"
   - Now add the new read list of the PLC tags that you want to read from the OPC UA server.

     In the example the "NewProduct" and "ProductNumber" tags are added to the "ReadListProduct" read list.

     Select the "NewProduct" tag in the right-hand field of the editor ("OPC UA Server interface"). Drag the "NewProduct" tag to the "ReadProduct" read list in the middle field of the editor. Follow the same procedure with the "ProductNumber" tag.

   The figure below shows the right field of the editor.

   ![Editor for client interfaces](images/109168534667_DV_resource.Stream@PNG-en-US.png)

   ![Editor for client interfaces](images/109168534667_DV_resource.Stream@PNG-en-US.png)

   **Alternative:**

   You can also select a new read list by dragging the right field of the editor ("OPC UA Server interface") to a node of the type Object or Folder and then dragging it to "Add new read list" in the left field of the editor. The new read list then contains all PLC tags of the node that has been moved.

   In the example, select the object "Data_for_OPC_UA_Clients", which contains the tags "NewProduct" and "ProductNumber". STEP 7 generates the new read list "Data_for_OPC_UA_Clients". In addition, the object contains the tag "Temperature". Delete the "Temperature" tag from the read list. Since they should not be read in the example.

   Change the name of the read list in "ReadListProduct".

   The following figure shows the content of the read list:

   ![Editor for client interfaces](images/122487816843_DV_resource.Stream@PNG-en-US.png)

   ![Editor for client interfaces](images/122487816843_DV_resource.Stream@PNG-en-US.png)
9. If you want assign new values to PLC tags, create a **write list** in this client interface.

   To do this, follow these steps:

   - Click "Add new write list" in the left section of the editor.

     STEP 7 adds a new list with the name "ReadList_1".

     For the example, change the name to "WriteListStatus".
   - Now add the new write list of all OPC UA server tags to which you want to assign new values.

     In the example, add the "WriteListStatus" tag to the write list "ProductionEnabled".

     Select the Tag of right field of the editor ("OPC UA Server interface"). Drag the tag to the write list in the middle field of the editor.

   **Alternative:**

   You can also create a new write list by selecting a node of the type Object or Folder in the right field of the editor ("OPC UA server interface") and then dragging to "Add new write list" in the left field of the editor.

   The new write list then contains all tags of the relevant node.

   In the example, select the object "Data_from_OPC_UA_Clients", which contains the tag "ProductionEnabled". STEP 7 generates the new write list "Data_from_OPC_UA_Clients". Change the name in "WriteListStatus".

   The following figure shows the content of the write list:

   ![Editor for client interfaces](images/122489725451_DV_resource.Stream@PNG-en-US.png)

   ![Editor for client interfaces](images/122489725451_DV_resource.Stream@PNG-en-US.png)
10. If you want to call a method of this OPC UA server, generate a new method list.

    To do this, follow these steps:

    - In the left section of the editor, click "Add new method list".

      STEP 7 adds a new list with the name "Method list_1".

      For the example, change the name to "MethodListOpenDoor".
    - Now add a method of the OPC UA server to the new method list.

      In this example, add the method "OpenDoor" to the method list "MethodListOpenDoor".

      Select the method of right field of the editor ("OPC UA Server interface"). Drag the method to the method list in the middle field of the editor.

    **Alternative:**

    You can also generate a new method list by selecting a method (node of the type Object) in the right field of the editor (OPC UA Server interface) and then dragging it to "Add new method list" in the left field of the editor. The new method list then contains the method of the relevant node.

    The following figure shows the content of the method list:

    ![Editor for client interfaces](images/122496036491_DV_resource.Stream@PNG-en-US.png)

    ![Editor for client interfaces](images/122496036491_DV_resource.Stream@PNG-en-US.png)

    If you want to call another method of the OPC UA server, you must create a new method list. Each method list contains only one method.

    See also [Useful information about server methods](#useful-information-about-server-methods-s7-1500-s7-1500t).
11. Compile the project.

    To do so, select the project and click the following button in the toolbar:

    ![Editor for client interfaces](images/109262545163_DV_resource.Stream@PNG-de-DE.png)

    ![Editor for client interfaces](images/109262545163_DV_resource.Stream@PNG-de-DE.png)

**Note**

**Read and write lists do not support all node types.**

The OPC UA client of the S7-1500 CPU does not support all OPC UA data types (node types) that can be made available via an OPC UA server interface. If you place an unsupported node type, for example, in a read list or write list a corresponding error signal appears. In this case, you cannot include the corresponding node in the read or write list.

Which types are supported is described here: [Mapping SIMATIC data types to OPC UA data types](#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t)

STEP 7 compiles the project and updates the data blocks that belong to the "Productionline" client interface.

> **Note**
>
> During compilation, STEP 7 overwrites all data in the data blocks belonging to the client interface. For this reason, you should neither add to nor correct these data blocks manually.

> **Note**
>
> **Renaming nod names (DisplayNames)**
>
> In read lists, write lists and method lists you can rename the name of a node by means of the shortcut menu. This is the "DisplayName" in the OPC UA language usage.
>
> If you rename the name of a method list node and the node is already used in a programmed block for the method call "OPC_UA_MethodCall", the compilation of the project leads to consistency errors: During the compilation the UDTs of the method are generated with the changed name. The references to the method used in the program are then no longer correct.
>
> To correct the consistency errors, you can either undo the name change of the method in the client interface or navigate to the method call and assign the relevant parameters again there under "Properties > Block parameters" ("Configuration" tab).

##### Data blocks of client interface

The following data blocks belong to the "Productionline" client interface:

- **Productionline_Configuration**

  A data block for the configuration.

  In the example, this data block is called "Productionline_Configuration".

  The data block already contains all system data types that are needed for the instructions of the OPC UA client.

  In addition, the data block contains general default values for parameter assignment of the connection to an OPC UA server.

  If you are working with connection parameter assignment, this data block will be filled.
- **ProductionLine_Data**

  A data block for the PLC tags that you have entered in the client interface editor.

  In the example, this data block is called "Productionline_Data".

  The figure below shows the data block.

  ![Data blocks of client interface](images/122496920331_DV_resource.Stream@PNG-de-DE.png)

  Use the "Productionline_Data" data block in your user program and access the read values of the "NewProduct" and "ProductNumber" PLC tags. This is explained in the following section using an example.

##### Reading and writing PLC tags of the client interface

**Example: Reading the "ProductNumber" value**

For example, you write in an SCL program:

#MyLocalVariable := "Productionline_Data".ReadListProduct.Variable.ProductNumber;

You use this, for example, to assign the number of the blank that was just produced in the production line to the local tag "#MyLocalVariable".

Requirements:

- A connection exists to the OPC UA server of the CPU, which controls the production line.
- The OPC UA client has read the current values.

For this reason you check whether a read value is valid:

- Check whether the value in "Productionline_Data".ReadListProduct.NodeStatusList[1] is equal to 0.
- Optional: Check when this value was sent from the OPC UA server. This value is in "Productionline_Data".Product.TimeStamps[1]. If no time stamp is requested, the communication load is reduced.

**Example: Writing the "ProductEnabled" value**

Transfer the new values for PLC tags, in the example for the "ProductionEnabled" tag, to the OPC UA server using the data block.

With the following assignment, you enable the production line in the example plant:

"Productionline_Data".WriteListStatus.Variable.ProductionEnabled := TRUE;

This is only successful, however, if the following requirements are met:

- A connection exists to the OPC UA server of the CPU, which controls the production line.
- Current values are being written via the OPC UA client

##### Consistency check

Finally, check the consistency of the read/write list or method list.

1. Select the list that you want to check.
2. Click the "Consistency check" button above the "OPC UA client interface" area.

A green check mark indicates an error-free assignment of the tags or methods to the corresponding elements of the server interface.

![Consistency check](images/112174249099_DV_resource.Stream@PNG-en-US.png)

You can assume that the data exchange between client and server and method calls operate without problem in runtime.

In the event of an error a list appears in the Inspector window. From this list you can jump to the respective error.

During the consistency check, STEP 7 checks:

- Whether all elements that you use in the respective list are also present in the server.
- Do the data types used match?
- For methods: Do the number, name, order, and data types of method arguments match?

---

**See also**

[OPC_UA_MethodCall: Call method (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#opc_ua_methodcall-call-method-s7-1500)
  
[OPC_UA_Connect: Create connection](Communication%20%28S7-1200%2C%20S7-1500%29.md#opc_ua_connect-create-connection)
  
[Program example for reading PLC tags (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#program-example-for-reading-plc-tags-s7-1500)

#### Determine server interface online (S7-1500, S7-1500T)

With STEP 7 (TIA Portal) you can determine the interface of an OPC UA server online. This provides information on which tags of a connected OPC UA server you can read or set (write) with OPC UA clients. It also provides information on which server methods of the OPC UA server are available for OPC UA clients.

If you are work offline you can create the interface of the OPC UA server by means of an OPC UA XML file. The address space of the server is described in the OPC UA XML file, see: [Export OPC UA XML file](#export-opc-ua-xml-file-s7-1500-s7-1500t).

##### Determine online server interfaces

To determine a server interface online, follow these steps:

1. In the STEP 7 project tree, select the CPU which is configured as OPC UA client (Supervisor in the example).
2. Select the client interface (in the example, OPC UA Communication > Client interfaces > Productionline).

   If no client interface has been created, double-click "Add new client interface".
3. Double-click the selected client interface.

   The editor for client interfaces is displayed.

   ![Determine online server interfaces](images/109865884171_DV_resource.Stream@PNG-en-US.png)
4. In the left section of the editor, click "Add new read list", "Add new write list", or "Add new method list".
5. In the right field of the editor, select "Online[]" as data source for "Source of server data":

   ![Determine online server interfaces](images/114488163467_DV_resource.Stream@PNG-en-US.png)
6. Click the "Online Access" button.

   STEP 7 displays the "Connect to OPC UA server" dialog.

   ![Determine online server interfaces](images/114476632075_DV_resource.Stream@PNG-en-US.png)

   **Tip:** When establishing an online connection to an OPC UA server for the first time, use the "Online access" button. When reconnecting after a disconnection, select the "Connect to Online Server" button next to the "Online" selection field.

   In the top right, enter the IP address of the OPC UA server whose server interface you want to determine online.
7. Click "Find selected server".

   STEP 7 establishes a connection to the OPC UA server and determines all security settings (server endpoints) that the server holds in readiness.

   STEP 7 displays the end points as list:

   ![Determine online server interfaces](images/109873244171_DV_resource.Stream@PNG-de-DE.png)
8. Click on the end point you want to use for a connection of step 7 to the OPC UA server.
9. Do you want to use a secure connection?

   - If you have selected a secure end point, then select the entry "TIA Portal" for the "Certificate location".

     And under "Certificate (Client)", select a client certificate for your PC on which STEP 7 (TIA Portal) is currently running.

     If a client certificate does not yet exist for your PC, you can generate a client certificate here in the TIA Portal.

     Proceed as follows to generate a certificate for your PC:

     - Click on the button in the "Certificate (Client)" input field.

     - Click "Add".

     - For "Certificate owners" enter "STEP 7 (TIA Portal)".

     - Select the "OPC UA client" entry at "Usage".

     - For "Subject Alternative Name (SAN)", enter the IP address of your PC, on which you are currently running STEP 7 (TIA Portal), under "Value". Overwrite the already entered IP address.

     - If your PC uses a second IP address, enter this address as well. If your PC does not use a second IP address, delete the second IP address already entered.

     - Click "OK".
   - If you have not selected a secure end point, then keep the default ("None").
10. How do you want log on?

    - If you want to log onto the OPC UA server as guest, then apply the default with "User authentication".
    - If you want to log on with user name and password, select "User name and password".

      Use the user name and password which was stored during the configuration of the OPC UA server in the properties of the CPU under "General > OPC UA > Server > Security > User authentication > User management".
11. Click on the "Go online" button.

    When a secure connection is established, a message appears that you must accept the server certificate for the secure connection to be established. In the message window, you can display further details about the server certificate via a link.

    This standard Windows window only provides information about the server certificate. If you click on the button to install the server certificate, the server certificate is not saved to the certificate memory of the TIA Portal, i.e. at the next connection attempt you will be prompted again to accept the server certificate.

    STEP 7 then establishes a connection to the OPC UA server and again displays the editor for client interfaces.

    In the right field of the editor, STEP 7 displays the uppermost level of the address space of the OPC UA server:

    ![Determine online server interfaces](images/109873252747_DV_resource.Stream@PNG-de-DE.png)
12. Click on the small black triangle next to "Objects".

    STEP 7 now also displays the level below Objects.
13. Click on the small black triangle next to "Productionline".

    STEP 7 now also displays the level below Productionline.
14. Now open additional lower-level folders:

    ![Determine online server interfaces](images/109172749323_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Mapping SIMATIC data types to OPC UA data types (S7-1500, S7-1500T)](#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t)
  
[Creating client interfaces (S7-1500, S7-1500T)](#creating-client-interfaces-s7-1500-s7-1500t)

#### Using multilingual texts (S7-1500, S7-1500T)

In the client interface editor, you are also importing texts that can be displayed in different languages with the OPC UA XML files (information models). Multilingualism is optional, and each node can be defined differently regarding the languages it offers.

In the XML file, these are the following fields that can be prepared for different languages:

- Display name
- Description

**Example for multilingual texts in an OPC UA XML file**

In the XML file below, the display name and the description, for example, are entered with a "default" text and multiple localizable texts.

- Default text is the first entry without localization information.
- Localized text is the text after "Locale=" followed by a language code, e.g. "it-IT" for Italian

![Figure](images/109276021771_DV_resource.Stream@PNG-de-DE.png)

##### Display of multilingual texts

When importing a server interface, the available multilingual texts are saved internally and downloaded to a CPU together with the project.

The client editor displays the text from the OPC UA XML file in the columns "Name of the node" (corresponds to "DisplayName") and "Description" (corresponds to "Description").

The following cascading rules determine which language is shown for a node:

- When the node contains text in the currently used editing language, the text is also displayed in the editing language.

  (Setting the editing language: In the project tree, select the area "Languages & resources > Project languages")
- When the node does not contain text in the editing language but a default text is defined there (without language code), the default text is displayed.
- "Name of the node" column: If no default text is defined either but a text in any other language exists, the DisplayName text is displayed in the first available language. This rule does not apply to description texts.
- If none of the conditions listed above is met, no text is displayed.

![Display of multilingual texts](images/127910341771_DV_resource.Stream@PNG-en-US.png)

When you change the editing language, the multilingual text in the imported interface will also change according to the rules explained above.

You can then apply the nodes in the corresponding lists (read list, write list, method list) with drag and drop.

You cannot change the language in the lists (read list, write list, method list).

##### Applying the displayed description texts as comment in PLC data types

When you compile the program, STEP 7 automatically creates PLC data types (UDTs) for each read list, for each write list and for inputs or outputs of each method. These UDTs each have one element for each node.

The UDTs apply the description text as comment according to the rules stated above. STEP 7 creates the comment in only one language, just like the texts in the OPC UA server interface can only be displayed in one language.

#### Rules for the access to structures (S7-1500, S7-1500T)

The rules for the access to structures are explained below. Note these rules when reading and writing values of complete structures provided by an OPC UA server.

##### How the client of the S7-1500 CPU accesses structures

To add structures as nodes to a read or write list, the following requirement must be met:

- The OPC UA server must support version V1.04 of the OPC UA specification.

The OPC UA client of the S7-1500 CPU uses neither TypeDictionaries nor DataTypeDefinition attributes, which a server offers for the resolution of these structures.

These options of the OPC UA client for checking structural elements in runtime are limited in the client.

##### Rules for the access to structures

If you use the client interfaces to configure the read and write lists (connection parameterization) and assign the PLC data types to the imported or online determined address model of the server, the read and write accesses to structures operate trouble-free in runtime.

The configuration by means of client interface automatically ensures that the sequence and the data type of the structural elements are coordinated on client and server side.

Recommendation: Update an S7-1500 CPU (as server) to the current firmware version (e.g. V2.0 > V2.5.2 or higher).

In runtime the OPC UA client only checks the total length of the transmitted value; more detailed checks are not possible.

Strings (WSTRING, STRING and OPC UA ByteString) are also permitted in structures. Strings do have a variable length, but OPC UA surmounts this variability: At the time of transfer, a length field in which the length of the string is encoded is prefixed to each string. Therefore, a S7-1500 CPU as a OPC UA client can check the length of a string and determine whether the string "fits into" the assigned CPU variable. In this manner, the CPU can also check the total length of the structure.

Mapping rules apply to the assignment of OPC UA structures to PLC tags or DB tags (see [Mapping SIMATIC data types to OPC UA data types](#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t)).

**Example of an error-free assignment of the structure elements**

In the imported node set file (XML export), the structure is defined as follows:

![Rules for the access to structures](images/112127165835_DV_resource.Stream@PNG-de-DE.png)

The structure mapped in the read list matches, both in the order and in the assigned data types, the corresponding nodes of the node set file.

![Rules for the access to structures](images/112128078091_DV_resource.Stream@PNG-de-DE.png)

If the structure now changes on the server, for example tagA and tagB are swapped, and the read list remains the same in the client, the assignment is no longer correct:

- The total length of the data remains the same (only the order has changed)
- The configuration of the structure is different for client and server!

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **No error message in the case of different structure configuration between client and server**  If the structures of client and server do not match, this rule violation will possibly not generate any error during compilation and also not in runtime.  Make sure not to change the configured assignments for structures in runtime. If required, reconfigure the assignment in the read and write lists! |  |

#### Using connection parameter assignment (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Creating and configuring connections (S7-1500, S7-1500T)](#creating-and-configuring-connections-s7-1500-s7-1500t)
- [Handling of the client certificates of the S7-1500 CPU (S7-1500, S7-1500T)](#handling-of-the-client-certificates-of-the-s7-1500-cpu-s7-1500-s7-1500t)
- [User authentication (S7-1500, S7-1500T)](#user-authentication-s7-1500-s7-1500t-1)
- [Using a configured connection (S7-1500, S7-1500T)](#using-a-configured-connection-s7-1500-s7-1500t)

##### Creating and configuring connections (S7-1500, S7-1500T)

With the instructions for OPC UA clients, you create a user program that exchanges data with an OPC UA server. A series of system data types are required for this.

To simplify your work with these system data types, a connection parameter assignment for OPC UA clients is available starting in STEP 7 (TIA Portal) Version 15.1.

Use of the connection parameter assignment is optional and not mandatory. You can also manually create the required system data types.

We use an example to make the description easier to follow, see [description of the example](#example-configuration-for-opc-ua-s7-1500-s7-1500t).

###### Opening the connection parameter assignment

To configure the connection to an OPC UA server, follow these steps:

1. In the "OPC UA communication" area, double-click the client interface whose parameters you want to assign in the project tree.

   For the example configuration: Double-click the "ProductionLine" client interface.

   ![Opening the connection parameter assignment](images/115212886667_DV_resource.Stream@PNG-de-DE.png)

   ![Opening the connection parameter assignment](images/115212886667_DV_resource.Stream@PNG-de-DE.png)

   The section "[Create client interface](#creating-client-interfaces-s7-1500-s7-1500t)" describes how to create a client interface.
2. Click the "Properties" tab (Inspector window) if the tab is not already displayed.

   STEP 7 now displays the connection parameter assignment for the instructions of the OPC UA client.

   The "General" tab is open.
3. Click on the "Configuration" tab and set the connection to the OPC UA server.

###### Setting the connection parameters

1. Select a descriptive name for the session. For the example, select the name "OPC UA Connection to ProductionLine".
2. In the "Address" field, enter the IP address of the OPC UA server to which your user program (that operates as an OPC UA client) is to establish a connection. In the example configuration, the CPU that controls the production line has the IP address "192.168.1.1". A connection to the OPC UA server of this CPU is to be established. For this reason, you enter this IP address in the "Address" field. In this case, the OPC UA server uses the default port 4840.  
     
   Alternatively, you can enter a valid DNS name in the "Address" field. The length of the DNS name is limited to 242 characters.   
   If the address is not valid, the error message is shown: "Enter a valid address".  
   If the string of the "Address", "Port" and "Path" fields contains more than 254 characters, an error message is also displayed.
3. Enter a path within the OPC UA server to restrict access to this path. The information is optional. However, some servers only establish a connection if a server path is specified.

   When you specify a path, it is automatically entered at the "ServerEndpointUrl" entry in the configuration DB for the client interface. The entry then consists of the components "OPC Schematic Prefix", "IP address", "Port number" and "Server path", for example: "opc.tcp://192.168.0.10:4840/example/path".

   The following figure shows the entry of the IP address for the OPC UA server:

   ![Setting the connection parameters](images/115212894347_DV_resource.Stream@PNG-en-US.png)

   ![Setting the connection parameters](images/115212894347_DV_resource.Stream@PNG-en-US.png)
4. If the OPC UA server is not using the standard port 4840, you must insert the port number here.

   For example, enter the number 65535 in the field, if the OPC UA server to which you want to establish a connection uses this port number.
5. In addition, you accept the default settings for session timeout (30 seconds) and monitoring time (5 seconds).

###### Setting the security parameters

1. Click the "Security" area in the "Configuration" tab.

   This area contains all security settings for the connection to the OPC UA server.

The following settings are possible:

**"General" area**

**Security mode:**

Select the security mode that the connection to the OPC UA server must meet from the drop-down list.

If the server does not meet the selected mode, a session is not established.

The following settings are available:

- No security: No secure connection!
- Sign: OPC UA server and OPC UA client sign the data transmission (all messages): Manipulations can thus be detected.
- Sign & Encrypt: OPC UA server and OPC UA client sign and encrypt the data transmission (all messages):

**Security policy:**

Set the encryption techniques for the signing and encryption of messages.

The following settings are possible:

- No security
- Basic128Rsa15
- Basic256
- Basic256Sha256

To configure a secure connection, you must observe the following items:

- A certificate is required for the client for a secure connection.
- You have to make the client certificate known to the server.

To find out how to proceed, see the section "[Handling client and server certificates](#handling-client-and-server-certificates-s7-1500-s7-1500t)" under "Certificate of the OPC UA client".

**"Certificates" area**

**Client certificate:**

The certificate confirms the authenticity of the OPC UA client.

To select a certificate, click the following symbol:

![Setting the security parameters](images/109263762059_DV_resource.Stream@PNG-de-DE.png)

STEP 7 displays a list of certificates.

Select the certificate that you have made known to the server.

Click the symbol with the green check mark:

![Setting the security parameters](images/109263769739_DV_resource.Stream@PNG-de-DE.png)

Or, create a new certificate. To do so, click the "Add" symbol.

If you create a new certificate, you must make this certificate known to the server.

**"User authentication" area**

The following settings are possible for user authentication:

- Guest
- User name and password
- Users (TIA Portal - Security Settings)

For more information, see [Users and roles with OPC UA function rights](#users-and-roles-with-opc-ua-function-rights-s7-1500-s7-1500t).

###### Setting languages

UA tags of the String type can be localized with OPC UA, that is, texts (values for the UA tag) can be available in different languages for the server. For example, localized texts can be available for DisplayName (Name of the node) and Description (Description).

In the "Languages" area of the "Configuration" tab you can, for example, influence the language of the texts returned by the server as follows:

In the "Languages" area, enter a number of languages that the server transfers to the client during connection setup.

The language or the local ID ("language code") associated with it that you enter in the first line is the language preferred by the client.

- If the server can provide the UA tag in the requested language, it is transferred to the client.
- If the server cannot provide the UA tag in the requested language, it checks whether it can provide the UA tag in the language you have entered in the second line (first substitute language).
- The server works its way down the list, and when it can provide neither the requested language nor a substitute language, it will provide the default language.

---

**See also**

[Handling of the client certificates of the S7-1500 CPU (S7-1500, S7-1500T)](#handling-of-the-client-certificates-of-the-s7-1500-cpu-s7-1500-s7-1500t)
  
[Program example for reading PLC tags (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#program-example-for-reading-plc-tags-s7-1500)

##### Handling of the client certificates of the S7-1500 CPU (S7-1500, S7-1500T)

###### Where does the client certificate come from?

If you are using the OPC UA client of an S7-1500 CPU (OPC UA client enabled), you can create certificates for these clients with STEP 7 V15.1 and higher as described in the following sections.

When you use UA clients from manufacturers or the OPC Foundation, a client certificate is generated automatically during installation or upon the first program call. You have to import these certificates with the global certificate manager in STEP 7 and use them for the respective CPU.

If you program an OPC UA client yourself, you can generate certificates through the program. Alternatively, you can generate certificates with tools, for example with OpenSSL or the certificate generator of the OPC Foundation:

- The procedure for OpenSSL is described here: "[Generating PKI key pairs and certificates yourself](#generating-pki-key-pairs-and-certificates-yourself-s7-1200-s7-1500-s7-1500t)".
- Working with the certificate generator of the OPC Foundation is described here: "[Creating self-signed certificates](#creating-self-signed-certificates-s7-1200-s7-1500-s7-1500t)".

###### Certificate of the OPC UA client of the S7-1500 CPU

A secure connection between the OPC UA server and an OPC UA client is only established if the server classifies the certificate of the client as trusted.

Therefore you have to make the client certificate known to the server.

The following sections describe how you can initially generate a certificate for the OPC UA client of the S7-1500 CPU and then make it available to the server.

###### 1. Generate and export a certificate for the client

For a secure connection you have to generate a client certificate and - if the server and client are located in different projects - export the certificate.

If client and server are in the same project, exporting the client certificate and subsequent import are not necessary.

**Requirements**

The IP interface of the CPU is configured, an IP address is available.

Background: The IP address under which the CPU can be accessed in your system is entered under "Subject Alternative Name (SAN)".

**Creating an OPC UA Client certificate**

The easiest way to generate a client certificate for an S7-1500 CPU is to configure a client interface.

The configuration of the client interface provides for the selection or generation of a client certificate, see [Creating and configuring connections](#creating-and-configuring-connections-s7-1500-s7-1500t).

Alternatively, you can generate the client certificate as follows:

1. In the project tree, select the CPU you want to use as a client.
2. Double-click "Device configuration".
3. In the properties of the CPU, click "Protection & Security > Certificate manager".
4. Double-click "<Add new>" in the "Device certificates" table.

   STEP 7 opens a dialog.
5. Click the "Add" button.
6. Select the "OPC UA client" entry from the "Usage" list.
7. Click "OK".

   STEP 7 now shows the client certificate in the "Device certificates" table.
8. If the server is in another project: Right-click this line and select "Export certificate" from the shortcut menu.
9. Select a directory where you will store the client certificate.

###### 2. Announcing the client certificate to the server

You have to make the client certificate available to the server to allow a secure connection to be established.

To do this, follow these steps:

1. If the client was configured in another project and you created and exported the client certificate there:

   - Select the "Use global security settings for certificate manager" option in the local certificate manager of the server. This makes the global certificate manager available.

     You will find this option under "Protection & Security > Certificate manager" in the properties of the CPU that is acting as server.
   - If the project is not yet protected, select "Security settings > Settings" in the STEP 7 project tree, click the "Protect this project" button and log on.

     The "Global security settings" item is now displayed under "Security settings" in the STEP 7 project tree.
   - Double click "Global security settings".
   - Double click "Certificate manager".

     STEP 7 opens the global certificate manager.
   - Click the "Device certificates" tab.
   - Right-click in the tab on a free area (not on a certificate).
   - Select the "Import" shortcut menu.

     The dialog for importing certificates is displayed.
   - Select the client certificate that the server is to trust.
   - Click "Open" to import the certificate.

     The certificate of the client is now contained in the global certificate manager. Note the ID of the client certificate just imported.
2. Click the "General" tab in the properties of the CPU that is acting as server.
3. Click "OPC UA > Server > Security > Secure Channel".
4. Scroll down in the "Secure Channel" dialog to the section "Trusted clients".
5. Double-click in the table on the empty row with "<add new>". A browse button is displayed in the row.
6. Click this button.
7. Select the prepared client certificate.
8. Click the button with the green check mark.
9. Compile the project.
10. Load the configuration onto the S7-1500 CPU (server).

###### Result

The server now trusts the client. If the server certificate is also considered trusted, the server and client can establish a secure connection.

---

**See also**

[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

##### User authentication (S7-1500, S7-1500T)

In the OPC UA client interface of the S7-1500, you can set what authentication is required for a user of the OPC UA client wishing to access the server. To do so, you must select the corresponding client interface in the project tree of the requested S7-1500 CPU under "OPC UA communication > Client interfaces" and select the type of user authentication in the Inspector window under "Properties > Configuration > Security".

###### Types of user authentication

The following options are available for user authentication:

- **Guest**

  The user does not need to verify authorization (anonymous access). The CPU creates an anonymous session for the user, and the OPC UA server does not check the authorization of the client user.
- **User name and password**

  The user must prove authorization (no anonymous access). The OPC UA server checks whether the client user is authorized to access the server. Authorization is given by the user name and the correct password. These inputs cannot be checked by the client interface, which means all values are accepted as being valid.

  > **Note**
  >
  > STEP 7 stores user name and password unencrypted in the data block/instance data block. Recommendation: Use the user authentication "User (TIA Portal - Security Settings)".
- **Users (TIA Portal - Security Settings)**

  You can enter a user name from the list of users entered in the project for authentication. The names of the registered users for the current project are available in the user administration in the project tree under "Security Settings > Users and roles". There you can also enter additional users.

  You can also enter a name that is not listed in the user administration of the project or leave the field blank. This is necessary when the corresponding user name is only provided by a different source during runtime, for example, via HMI or from a different OPC UA client.

###### "No Security" security policy and authentication via user name and password

You can set the following combination:

Security policy = "No Security" and authentication via user name and password.

- The OPC UA server of the S7-1500 supports this combination. OPC UA clients can connect and encrypt the authentication data or not.
- OPC UA client of the S7-1500 CPU also supports this combination: However, in runtime it only connects if it can send the authentication data encrypted via cable!

Result: With the following configuration, not connection can be established in runtime.

- S7-1500 as OPC UA client
- OPC UA server which supports no encryption of authentication data when "No Security" (="none") is set as security policy.

---

**See also**

[Users and roles with OPC UA function rights (S7-1500, S7-1500T)](#users-and-roles-with-opc-ua-function-rights-s7-1500-s7-1500t)
  
[OPC_UA_SessionConnectInfo (S7-1500)](Communication%20%28S7-1200%2C%20S7-1500%29.md#opc_ua_sessionconnectinfo-s7-1500)

##### Using a configured connection (S7-1500, S7-1500T)

###### Introduction

This section shows you how to use a configured connection for OPC UA instructions (third step).

###### Requirements

- You have created a client interface and added PLC tags and PLC methods to this interface, see ("[First step](#creating-client-interfaces-s7-1500-s7-1500t)").
- You have configured a connection to an OPC UA server ([Second step](#creating-and-configuring-connections-s7-1500-s7-1500t)).

###### Overview

To read data from an OPC UA server or write data to an OPC UA server, use the following instructions:

- OPC_UA_Connect
- OPC_UA_NamespaceGetIndexList
- OPC_UA_NodeGetHandleList
- OPC_UA_ReadList or OPC_UA_WriteList
- OPC_UA_NodeReleaseHandleList
- OPC_UA_Disconnect

###### Order of the OPC UA instructions

The following figure shows the order in which the OPC UA instructions are called in a user program in order to use these instructions to read or write PLC tags:

![Order of the OPC UA instructions](images/109275317515_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for "clean-up" after a completed read or write operation  The "OPC_UA_NodeReleaseHandleList" instruction can be omitted if "OPC_UA_Disconnect" is called immediately afterwards. |

STEP 7 (TIA Portal) automatically supplies the parameters of these instructions if you are using a client interface and a configured connection to an OPC UA server.

###### Using a client interface and configured connection

To use a configured OPC UA connection, follow these steps:

1. Open your user program in the TIA Portal.
2. Using drag-and-drop, move the "**OPC_UA_Connect**" instruction into the program editor.

   You will find the instruction under "Instructions > Communication > OPC UA" in the TIA Portal.
3. Select a call option for the instruction

   The example uses a multi-instance.

   STEP 7 displays the instruction in the program editor.

   The editor for the Function Block Diagram (FBD) programming language uses the following display:

   ![Using a client interface and configured connection](images/109274203659_DV_resource.Stream@PNG-de-DE.png)

   ![Using a client interface and configured connection](images/109274203659_DV_resource.Stream@PNG-de-DE.png)
4. Click the toolbox symbol in the editor for FBD or LAD.

   The symbol is located in the heading of the instruction:

   ![Using a client interface and configured connection](images/109274262539_DV_resource.Stream@PNG-de-DE.png)

   ![Using a client interface and configured connection](images/109274262539_DV_resource.Stream@PNG-de-DE.png)

   If you are using the editor for STL or SCL: Click the small green rectangle below the first character of the instance name:

   ![Using a client interface and configured connection](images/109274418699_DV_resource.Stream@PNG-de-DE.png)

   ![Using a client interface and configured connection](images/109274418699_DV_resource.Stream@PNG-de-DE.png)

   The [example](#example-configuration-for-opc-ua-s7-1500-s7-1500t) uses "#OPC_UA_Connect_Instance" as the instance name.

   STEP 7 displays the properties of the instruction in a separate dialog.
5. For "Client interface", select the client interface that you want to use for the instruction.

   In the example, the "ProductionLine" client interface is selected.

   STEP 7 now interconnects the "ProductionLine" client interface with the parameters of the OPC_UA_Connect instruction:

   ![Using a client interface and configured connection](images/114375385739_DV_resource.Stream@PNG-de-DE.png)

   ![Using a client interface and configured connection](images/114375385739_DV_resource.Stream@PNG-de-DE.png)

   "ProductionLine" is the interface that the OPC UA client of the [example](#example-configuration-for-opc-ua-s7-1500-s7-1500t) uses for data exchange with the OPC UA server "ProductionLine".
6. Using drag-and-drop, move the "**OPC_UA_NamespaceGetIndexList**" instruction into the program editor.

   You will find the instruction under "Instructions > Communication > OPC UA" in the TIA Portal.

   - Select the "Multi-instance" call option.
   - Click the toolbox symbol (LAD and FBD) or the small green box below the instance name (STL and SCL) if the editor is not already open.
   - Select the client interface that you want to use (in the example, "ProductionLine").

   STEP 7 now automatically interconnects all parameters of the "OPC_UA_NamespaceGetIndexList" instruction:
7. Using drag-and-drop, move the "**OPC_UA_NodeGetHandleList**" instruction into the program editor.

   - Select the "Multi-instance" call option.
   - Click the toolbox symbol (LAD and FBD) or the small green box below the instance name (STL and SCL) if the editor is not already open.
   - Select the client interface that you want to use. The example uses the "ProductionLine" client interface.
   - Under "Data access > Read/write list", select the read list that you want to use (in the example, the "Product" read list).

   STEP 7 now automatically interconnects all parameters of the "OPC_UA_NodeGetHandleList" instruction:

   ![Using a client interface and configured connection](images/109274528779_DV_resource.Stream@PNG-de-DE.png)

   ![Using a client interface and configured connection](images/109274528779_DV_resource.Stream@PNG-de-DE.png)

   If you want to write data to an OPC UA server, select the write list you want to use under "Data access > Read/write list" (in the example, the "ProductionStatus" write list).
8. Using drag-and-drop, move the "**OPC_UA_ReadList**" instruction into the program editor.

   - Select the "Multi-instance" call option.
   - Click the toolbox symbol (LAD and FBD) or the small green box below the instance name (STL and SCL) if the editor is not already open.
   - Select the client interface that you want to use. The example uses the "ProductionLine" client interface.
   - Under "Data access > Read list", select the read list that you want to use (in the example, the "Product" read list).

   STEP 7 now automatically interconnects all parameters of the "OPC_UA_ReadList" instruction.

   If you want to write data to an OPC UA server, use the "**OPC_UA_Write**" instruction and select the list of tags you want to send to the server under "Data access > Write list" (in the example, the "ProductionStatus" write list).
9. If you want to use different read lists or write lists as program-controlled lists in your user program, move the "**OPC_UA_NodeReleaseHandleList**" instruction into the program editor using drag-and-drop.

   - Select the client interface that you want to use.
   - Now select a read list or write list that you want to release: Release only read or write lists that you rarely use, since re-registering is time-consuming.
   - Then, repeat the steps starting with step 7 with the "UA_NodeGetHandleList" instruction.
10. Using drag-and-drop, move the "**OPC_UA_Disconnect**" instruction into the program editor.

    - Select the "Multi-instance" call option.
    - Click the toolbox symbol (LAD and FBD) or the small green box below the instance name (STL and SCL) if the editor is not already open.
    - Select the client interface that you want to use. The example uses the "ProductionLine" client interface.

    STEP 7 now automatically interconnects all parameters of the "OPC_UA_Disconnect" instruction.

###### Supported instructions

For the following instructions, STEP 7 automatically supplies the parameters if you are using a client interface and a configured connection to an OPC UA server:

- OPC_UA_Connect
- OPC_UA_NamespaceGetIndexList
- OPC_UA_NodeGetHandleList
- OPC_UA_MethodGetHandleList
- OPC_UA_MethodReleaseHandleList
- OPC_UA_ReadList
- OPC_UA_WriteList

- OPC_UA_MethodCall
- OPC_UA_NodeReleaseHandleList
- OPC_UA_Disconnect

### Tips and recommendations (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Rules for subscriptions (S7-1200, S7-1500, S7-1500T)](#rules-for-subscriptions-s7-1200-s7-1500-s7-1500t)
- [Rules for the user program (S7-1200, S7-1500, S7-1500T)](#rules-for-the-user-program-s7-1200-s7-1500-s7-1500t)
- [Master copies for OPC UA communication (S7-1200, S7-1500, S7-1500T)](#master-copies-for-opc-ua-communication-s7-1200-s7-1500-s7-1500t)
- [OPC UA client-server connection via NAT router (S7-1200, S7-1500, S7-1500T)](#opc-ua-client-server-connection-via-nat-router-s7-1200-s7-1500-s7-1500t)

#### Rules for subscriptions (S7-1200, S7-1500, S7-1500T)

The following rules apply to subscriptions:

- Group subscriptions in the client according to different sampling and publishing intervals and distribute the monitored elements (variables) to these groups.

  Example: Create a subscription for longer publishing intervals (e.g. 5 seconds) and a subscription for shorter publishing intervals (e.g. 0.1 second).
- Disable unneeded subscriptions.

  Reason: The "Deactivated" subscription mode reduces resource consumption.
- To further optimize resource consumption, reduce the subscription timeout for the client. The subscription timeout cannot be fixed directly, this time results from the subscription settings "PublishingInterval" and "LifetimeCount" confirmed by the server.   
  Background: When a client has created subscriptions and the session is terminated, the subscriptions initially remain in the server and occupy memory resources. The OPC UA server only releases the required resources when the subscription timeout ends the lifetime of the subscriptions.

- Consider the maximum number of monitored items of subscriptions for the corresponding S7-1500 CPU.

  The information can be found in the technical specification of the respective CPU. The information is based on a sampling / publishing interval of 1 second.

  You can find additional information in the [FAQ 109755846](https://support.industry.siemens.com/cs/us/en/view/109755846).
- Select the same sampling and publishing intervals for the OPC UA client and for the OPC UA server.
- Avoid arrays and structures as elements of subscriptions – if the process allows.

  Reason: If even one value of an array/structure changes, the entire structure is transferred, creating an unnecessary communication load.
- Occasional non-compliance with the required sampling rate is acknowledged by the OPC UA server of the S7-1500 CPU according to OPC UA specification with a "GoodOverload" error code, see also TIA Portal Help. Different OPC UA clients handle "Good" error codes unequal to "0" differently. Consider this behavior and, if needed, reduce the communication load according to the measures described above.

---

**See also**

[Settings of the server for subscriptions (S7-1500, S7-1500T)](#settings-of-the-server-for-subscriptions-s7-1500-s7-1500t)

#### Rules for the user program (S7-1200, S7-1500, S7-1500T)

##### User programs for OPC UA

The following rules apply to user programs:

- If your application allows it and the communication load is high, you should set a minimum time for cycle OBs.

  Advantages:

  - The cycle time remains constant for the most part
  - The CPU has more time for communication tasks throughout

  Tip: To analyze the CPU utilization (e.g. communication), use the instruction "RT_INFO": Read runtime statistics"; mode 21 or mode 25 (see TIA Portal help).
- Reduce the number of variables or data blocks that can be reached from OPC UA/HMI. By default, all variables from OPC UA/HMI are accessible when creating variables/DBs/IDBs. This measure leads to improved performance when loading in RUN.

  Tip: Using the detailed object display in the TIA Portal, you can easily mark the non-OPC-UA-relevant data blocks as "not accessible from OPC UA".
- Consistent transfer of data beyond the limits of simple data types is only possible with OPC UA methods. If you use other OPC UA functions (Subscriptions, Read/Write), you must ensure data consistency in the application.
- OPC UA offers the "RegisterNodes" service for repeated read and write accesses to the same variables. Servers can use this service to prepare for optimized access to variables. The instruction "OPC_UA_NodeGetHandleList" of the S7-1500 as OPC UA client implicitly calls this service to prepare the server for optimized accesses (in OPC UA usage "Registered Read/Write").

##### Calling detailed object display in the TIA Portal

To call up the detailed object display, proceed as follows:

1. Switch to the "PLC Programming" portal in the portal view.
2. Select "Show all objects".
3. Switch to the "Details" tab in the selection window.
4. In the "DB accessible from OPC UA" column, disable the accessibility from OPC UA for individual objects.

   ![Calling detailed object display in the TIA Portal](images/122236395787_DV_resource.Stream@PNG-en-US.png)

   ![Calling detailed object display in the TIA Portal](images/122236395787_DV_resource.Stream@PNG-en-US.png)

#### Master copies for OPC UA communication (S7-1200, S7-1500, S7-1500T)

##### Master copies for the OPC UA interfaces

Interfaces of OPC UA servers and OPC UA clients that you want to use multiple times can be stored either in the project library or in a global library. Master copies in the project library can only be used within the project. When you create the master copy in a global library, it can be used in different projects.

The OPC UA capable CPUs differentiate between 3 interface types of the OPC UA server:

- Standard OPC UA server interface
- Companion specification interface
- Namespace reference

When adding the OPC UA interface in the project tree under "OPC UA Communication" each interface type gets its own symbol. The same symbol is used by the master copy.

Create either single master copies or a master copy with multiple interfaces.

##### Creating multiple master copies from selection

You select one or more elements and create individual master copies from them

1. Open the library in the "Libraries" task card.
2. Select the desired elements.
3. Using a drag-and-drop operation, move the elements to the "Master copies" folder or any subfolder of "Master copies".

##### Creating a master copy from selection

You select multiple elements and create a single master copy from them that contains all selected elements.

1. Copy to the clipboard the elements that you want to create as master copies.
2. Right-click on the "Master copies" folder or any of its subfolders in the library.
3. In the shortcut menu, select "Paste as a single master copy" command.

If multiple interfaces are added to a master copy from the OPC UA server or OPC UA client, the label and the symbol in the library are changed accordingly.

A symbol with "+" is displayed instead of the simple symbol.

![Creating a master copy from selection](images/123922109835_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Creating a user-defined server interface (S7-1500, S7-1500T)](#creating-a-user-defined-server-interface-s7-1500-s7-1500t)

#### OPC UA client-server connection via NAT router (S7-1200, S7-1500, S7-1500T)

If client and server are connected via NAT routers, this attempt to make a connection fails with the error message "BadCommunicationError" or "BadNotConnected".

Background: The IPv4 packets are manipulated by the router in NAT systems. As a result, either the source IP ("Source NAT") or the destination IP ("Destination NAT") of a packet is replaced by an IP address configured in the router (depending on the destination port). This process is transparent for client and server, i.e. these devices are not informed about this process.

The problem: The NAT router also has no way to replace the endpoint description returned by the server (this is the EndpointUrl), since this address information is located in the user data of "GetEndpointsResponse".

You can find a detailed description of the procedure in the following [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109766709).

##### CPU Firmware Version V2.6

No OPC UA client-server connection via NAT router possible.

##### Remedy as of CPU firmware version V2.8

Use the "ServerUri" attribute of the connection information ("SessionConnectInfo" parameter of the "OPC_UA_Connect" instruction).

Enter the complete ServerEndpointUrl with the IP address of the NAT router as "ServerUri". This ServerEndpointUrl is then used to establish the connection instead of the EndpointUrl returned in GetEndpointsResponse.   
If you leave the attribute empty, the behavior will be the same as in CPU firmware version V2.6.

When you use the connection parameter assignment for the OPC UA connection setup (create client interface), then you must open the client interfaces DB (*_Configuration[DBx]) after the parameter assignment and change the string in the "ServerUri" parameter. The entry is retained after compiling the OPC UA configuration.

##### Example of connection setup (address from ServerUri replaces address from GetEndpointsResponse)

**Procedure**

In the "ServerUri" parameter, enter the complete server address (ServerEndpointUrl), consisting of IP address, port and optional path. The IP address is the client-side IP address of the NAT router:

1. Open configuration DB

   ![Example of connection setup (address from ServerUri replaces address from GetEndpointsResponse)](images/131229545995_DV_resource.Stream@PNG-de-DE.png)
2. Change "ServerUri" parameter

   ![Example of connection setup (address from ServerUri replaces address from GetEndpointsResponse)](images/131229537803_DV_resource.Stream@PNG-de-DE.png)

   The connection is then established with the following steps:

   - GetEndpointsRequest: The S7-1500 OPC UA client addresses the server via the destination address of the NAT router in the subnet of the client (10.10.0.1).  
      The NAT router converts the destination address into the IP address of the server (192.168.0.1) in the subnet of the server.
   - GetEndpointsResponse: The server returns its EndpointUrl in "GetEndpointsResponse":   
     "opc.tcp://192.168.0.1:4840/UA/DemoServer".   
     This address cannot be reached directly by the client because it is located behind a NAT router.
   - OpenSecureChannel:   
     The client does not take the EndpointUrl from the GetEndpointsResponse to open the secure channel. Instead, it takes the EndpointUrl from the "ServerUri" parameter:  
     "opc.tcp://10.10.0.1:4840/UA/DemoServer".  
     This IP address can be reached by the client; the data is routed from the NAT router to the IP address of the server.

     ![Example of connection setup (address from ServerUri replaces address from GetEndpointsResponse)](images/131229925387_DV_resource.Stream@PNG-de-DE.png)

## Additional configurations (S7-1200)

### Configuring additional functions

The S7-1200 automation system has numerous additional functions that are useful as integrated CPU functions or available via plug-in modules (for example, communication modules). You can find the description via the following links.

---

**See also**

[Overview of point-to-point communication (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#overview-of-point-to-point-communication-s7-1200)
  
[General information on high-speed counters (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#general-information-on-high-speed-counters-s7-1200)
  
[Motion functionality of the CPU S7-1200 (S7-1200)](Using%20S7-1200%20Motion%20Control%20%28S7-1200%29.md#motion-functionality-of-the-cpu-s7-1200-s7-1200)
  
Configuring PID Compact (S7-1200)
  
Configuring PID_3Step (S7-1200)
  
[Using the S7-1200 CPU as an OPC UA server (S7-1200)](#using-the-s7-1200-cpu-as-an-opc-ua-server-s7-1200)
