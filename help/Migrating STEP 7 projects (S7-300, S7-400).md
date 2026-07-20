---
title: "Migrating STEP 7 projects (S7-300, S7-400)"
package: MigrationSTEP734enUS
topics: 20
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Migrating STEP 7 projects (S7-300, S7-400)

This section contains information on the following topics:

- [Migration of STEP 7 projects (S7-300, S7-400)](#migration-of-step-7-projects-s7-300-s7-400)
- [Requirements for the migration of STEP 7 projects (S7-300, S7-400)](#requirements-for-the-migration-of-step-7-projects-s7-300-s7-400)
- [Checking whether STEP 7 projects can be migrated (S7-300, S7-400)](#checking-whether-step-7-projects-can-be-migrated-s7-300-s7-400)
- [Consistency check in the initial project (S7-300, S7-400)](#consistency-check-in-the-initial-project-s7-300-s7-400)
- [Removing unsupported hardware components (S7-300, S7-400)](#removing-unsupported-hardware-components-s7-300-s7-400)
- [Special points to observe during migration (S7-300, S7-400)](#special-points-to-observe-during-migration-s7-300-s7-400)

## Migration of STEP 7 projects (S7-300, S7-400)

### Introduction

You can migrate a project from SIMATIC STEP 7 V5.4 SP5. You can then continue to use this project in the TIA Portal. If you want to migrate projects from older STEP 7 versions, you must open, compile and save these projects first in STEP 7 V5.4 SP5. It is also possible to migrate integrated projects with devices from other software products.

### Scope of migration

Generally, you can migrate all configurations and objects from SIMATIC STEP 7 V5.4 SP5 that the installed version of the TIA Portal supports. This includes, for example, the following devices and configurations:

- Devices of the S7-300 and S7-400 family.
- PROFIBUS configurations with connected distributed I/O. These include GSD-based slaves, I-slaves as well as direct data exchange.
- PROFINET configurations with distributed I/O. These include GSD-based devices and I-devices.
- Network configurations
- Connections
- Blocks created in the programming languages LAD, FBD or STL, S7-SCL, S7-GRAPH
- PLC tags
- User-defined data types (UDT)
- Alarms and alarm classes
- Interrupts
- User-defined attributes (UDA)
- User text libraries

### Including the hardware configuration in the migration

By default, only the software parts of the project are included in the migration. An unspecified device is generated in the migrated project for each of the devices contained in the initial project. The hardware and network configurations and the connection are not migrated. You can convert the unspecified devices into suitable devices after the migration and create any network configurations and connections manually.

If you are certain that the hardware used in the initial project has a corresponding equivalent in the TIA Portal, you can include the hardware configuration in the migration. In this case, both the hardware configuration and the software are migrated.

> **Note**
>
> **Additional support for migration**
>
> You can find the latest information about migration in the Siemens Industry Online Support:
>
> [Migration of controllers](http://support.automation.siemens.com/WW/view/en/83557459)
>
> If you need further support, contact SIMATIC Customer Support.

---

**See also**

[Migrating projects with the migration tool](Migrating%20projects%20and%20programs.md#migrating-projects-with-the-migration-tool)
  
[Migration of projects with the TIA Portal](Migrating%20projects%20and%20programs.md#migration-of-projects-with-the-tia-portal)
  
[Reporting system errors (S7-300, S7-400)](#reporting-system-errors-s7-300-s7-400)
  
[Migrating program blocks (S7-300, S7-400)](#migrating-program-blocks-s7-300-s7-400)
  
[Migrating an integrated project (S7-300, S7-400)](Migrating%20projects%20and%20programs.md#migrating-an-integrated-project-s7-300-s7-400)

## Requirements for the migration of STEP 7 projects (S7-300, S7-400)

Various requirements for the software installed on the original PG/PC and for the initial project apply to the migration.

### Requirements for the original PG/PC

The following requirements apply to the PG/PC:

- A licensed version of STEP 7 V5.4 SP5 or higher (we recommend V5.5 SP4) must be installed. For projects that only contain PC stations, it is sufficient if the SIMATIC NET PC software is installed.
- For all of the configurations used in the project, the corresponding additional software must be installed with a valid license, for example, optional packages
- All HSPs for modules not included in the hardware catalog must be installed.
- All GSD files used in the project must comply with the specifications.
- You must be logged on to the operating system with administrative rights.
- One of the following software products must be installed:

  - The TIA Portal with STEP 7 Professional V13 SP1 or higher

    If you do not migrate with the most recent version of the TIA Portal on the original programming device/PC, the functional scope of the project in more recent versions of the TIA Portal is initially limited. You first have to upgrade the project before you can use the full functional scope of more recent versions.
  - The migration tool

### Requirements for the initial project

- The initial project must not be configured with access protection.
- The hardware and software must be consistent.
- The alarm number assignment must be set to CPU-oriented.
- The project cannot contain any protected blocks with time stamp conflict.
- It must be possible to compile all programs and their sources without errors.
- All called blocks must be available in the block folder.
- The block folder must contain no blocks that are not called, in particular no instance data blocks.
- We recommend that you migrate blocks unencrypted, because blocks encrypted with S7-Block Privacy cannot be read or modified in the TIA Portal.

### Requirements for the PG/PC with STEP 7 Professional

- One of the following software products must be installed:

  - STEP 7 Professional V13 SP1 or later
  - STEP 7 Professional V13 SP1 or later (without license) when the project to be migrated only contains components that have been configured with the SIMATIC NET PC software.
- For all of the configurations used in the project, the corresponding additional software must be installed with a valid license, for example, optional packages.
- All HSPs for modules that are not contained in the hardware catalog and all GSD files used in the project must be installed.

## Checking whether STEP 7 projects can be migrated (S7-300, S7-400)

Before you start the migration, check to determine whether all necessary requirements for migration have been met in the initial project.

> **Note**
>
> Note that the actual values are reset in the initial project when the following steps are carried out. Also note that running the block consistency check resets the start values in the instance DBs to the default values. If you are using technology functions, this behavior is not desired.

### Procedure

To check whether a project can be migrated, follow these steps:

1. Open the initial project in SIMATIC STEP 7 V5.4 SP5. For correct matching, only the optional packages and hardware components available in the TIA Portal, including HSPs and GSD files, may be installed.
2. Open the individual stations. If no alarms indicating missing components are displayed when the stations are opened, all the components necessary for migration are available.
3. Perform a block consistency check for each block container contained in the project.

   For more information on the consistency check, refer to Chapter "[Consistency check in the initial project](#consistency-check-in-the-initial-project-s7-300-s7-400)".
4. Compile the entire project. If no errors are displayed during the compilation, the programs can be migrated.
5. Check whether all modules with an identical MLFB and the same firmware version are contained in the TIA Portal hardware catalog.
6. Check whether the CPU-oriented alarm number assignment is activated for each CPU.
7. Compile the project in NetPro. The compilation in NetPro must also be error-free.

---

**See also**

[Consistency check in the initial project (S7-300, S7-400)](#consistency-check-in-the-initial-project-s7-300-s7-400)
  
[Check migration readiness of hardware components](Migrating%20projects%20and%20programs.md#check-migration-readiness-of-hardware-components)
  
[FAQ entry on consistency check](http://support.automation.siemens.com/WW/view/en/5416540)

## Consistency check in the initial project (S7-300, S7-400)

### Consistent initial project

A consistent initial project is a requirement for the successful migration of a project to the TIA Portal. It is therefore advisable to perform a consistency check on the initial project before migration. You can find a guide to the consistency check in SIMATIC STEP 7 in an [FAQ entry](http://support.automation.siemens.com/WW/view/en/5416540) on the Siemens Industry Online Support page or in the SIMATIC STEP 7 help.

### Migrate start values in instance DBs for technology blocks

The compilation in the block consistency check causes the tags in instance DBs to be reset to the default values. The set start values are lost in the process.

To migrate the start values anyway, we recommend one of the following procedures:

- For smaller projects: Backup the instance DBs outside the block folder

  Backup the instance DBs before you start the consistency check. After the consistency check has been completed, copy the instance DBs back to the block folder.
- For larger projects: Create a copy of the project

  Make a copy of the project and then carry out the check on the copy of the project. Correct any errors found during the consistency check in the initial project.

You can then migrate the project with the configured values. In this way, the configuration of the technology functions is also retained.

---

**See also**

[Basic information on start values](Programming%20data%20blocks.md#basic-information-on-start-values)

## Removing unsupported hardware components (S7-300, S7-400)

If you have created configurations in the initial project for which not all of the right software is installed, then you can still migrate the project by manually deleting the unsupported configurations from the project. Alternatively, you can use the "Reorganize" function.

### Procedure

To clean the original project, follow these steps:

1. Use an installation of SIMATIC STEP 7 V5.4 SP5 that contains only the optional packages contained in the TIA Portal and all required modules.
2. Save the project again and select the "With reorganization" option when saving. Any unsupported configurations will be removed from the project.

For modules that are only available in a new version or with a new firmware version in the TIA Portal, use the "Exchange object" function in the station to exchange an older module for one that can be migrated.

## Special points to observe during migration (S7-300, S7-400)

This section contains information on the following topics:

- [Device names (S7-300, S7-400)](#device-names-s7-300-s7-400)
- [PROFINET IO configurations (S7-300, S7-400)](#profinet-io-configurations-s7-300-s7-400)
- [PROFIBUS configurations (S7-300, S7-400)](#profibus-configurations-s7-300-s7-400)
- [GSD and GSDML devices (S7-300, S7-400)](#gsd-and-gsdml-devices-s7-300-s7-400)
- [Connections (S7-300, S7-400)](#connections-s7-300-s7-400)
- [Multiprojects (S7-300, S7-400)](#multiprojects-s7-300-s7-400)
- [Migrating program blocks (S7-300, S7-400)](#migrating-program-blocks-s7-300-s7-400)
- [Migration of LAD/FBD/STL programs (S7-300, S7-400)](#migration-of-ladfbdstl-programs-s7-300-s7-400)
- [Migrating GRAPH programs (S7-300, S7-400)](#migrating-graph-programs-s7-300-s7-400)
- [Migrating SCL programs (S7-300, S7-400)](#migrating-scl-programs-s7-300-s7-400)
- [Messages (S7-300, S7-400)](#messages-s7-300-s7-400)
- [Reporting system errors (S7-300, S7-400)](#reporting-system-errors-s7-300-s7-400)
- [Migration of project texts (S7-300, S7-400)](#migration-of-project-texts-s7-300-s7-400)

### Device names (S7-300, S7-400)

#### Device names of PROFINET IO devices

In STEP 7 V5.5 the device name of a PROFINET IO device is used as the name of the IO devices. After the migration to a TIA Portal project, the device name of the PROFINET IO device from the initial project is used as follows:

- As the PROFINET device name
- As the name for the interface module
- As the name of the station

  A maximum of 24 characters is permitted for the name of the station in the TIA Portal. The name of the station is therefore truncated to a maximum of 24 characters where required. If truncating of the station name would result in several stations with the same name, the last characters of the station name are used to number the stations consecutively.

#### Names of modules and racks

In SIMATIC STEP 7 V5.5, the names of modules and racks do not have to be unique. In the TIA Portal, however, unique names are required. Therefore, the names of the modules and racks are incremented during the migration to make sure that unique names are assigned. This does not apply to PROFINET IO devices and PROFINET CPs. You must provide unique names for these yourself.

### PROFINET IO configurations (S7-300, S7-400)

#### Unique name assignment required

The names of PROFINET IO devices must be unique within the subnet. The same applies to the names of PROFINET CPs. For this reason, ensure that the name assignment is unique before the migration into the initial project or provide unique names after migration and before the first compilation.

#### Media redundancy with sync domains

If a sync domain with activated media redundancy is found in the initial project, the sync domain configuration is imported during migration. If, however, several sync domains with activated media redundancy are found in the initial project, they are removed and the project is migrated without the sync domains. In any case, you will receive a message which sync domains were imported.

In any case, use SIMATIC STEP 7 V5.5 to configure the media redundancy in the initial project.

#### Isochronous mode with PROFINET IO

Note the following for PROFINET IO configurations in isochronous mode:

- IRT with high performance

  If you have configured IRT with high performance when planning the topology in the initial project, the option is changed to "RT" during migration. You will receive a message informing you of the change.
- Use of OB 61

  If the isochronous mode for PROFINET IO with OB 61 is activated in the original configuration in the STEP 7 project, it will be deactivated by the migration. The devices will still be imported. PROFINET IRT configurations with the option "high flexibility" without the use of OB 61 can be migrated.

#### CBA for IO controllers

If you have used the cyclical service CBA (Component Based Automation) in the initial project, it is deactivated during migration. You will receive a message informing you of the change.

#### Use of Shared Devices

If Shared Devices are configured in the initial project, they are removal during migration. You will receive a message informing you of their removal.

#### Transfer areas

If transfer areas for data exchange between the IO controller and I-device are configured in the initial project, they are removed during migration. You will receive a message informing you when a transfer area is removed during migration.

#### Update groups for PROFINET IO

If necessary, also remove update groups from the STEP 7 project before you start the migration. If any update groups are still configured, then the migration can not be carried out.

#### I slaves and I-devices

Only connected and consistent I slave and I-device configurations can be migrated. If the configuration is inconsistent, then the configurations in question will be excluded from the migration.

#### PROFINET IO systems that are not connected

Devices with PROFINET IO systems that are not connected can be migrated. The IO devices and the PROFINET IO systems are located in the network view without connection after migration. Connect these IO devices after migration with an IO controller or delete any unnecessary IO devices.

### PROFIBUS configurations (S7-300, S7-400)

#### Isochronous PROFIBUS

It is possible to migrate isochronous PROFIBUS configurations. You should compile the project again after the migration, however, to rule out any possible inconsistencies. Also pay attention to slightly changed SDBs.

#### Orphaned master systems

Devices with orphaned DP master systems can be migrated. The DP slaves of the abandoned DP master system are located in the network view without connection after migration. Connect these DP slaves after migration with a DP master or delete any unnecessary DP slaves.

### GSD and GSDML devices (S7-300, S7-400)

For devices that were configured with PROFIBUS GSD or PROFINET GSD files, the corresponding GSD files must also be installed in the TIA Portal. If GSD files are not yet installed in the TIA Portal, they will be installed automatically during the migration. The GSD files must comply with the specifications (e.g., GSDML Specification for PROFINET IO, see [www.profinet.com](http://www.profinet.com)), in order for the project to be migrated successfully. If GSD files of a device manufacturer do not comply with the specification, the project cannot be migrated. In the migration log, you receive alarms notifying you of non-compliant GSD files.

If the GSD files do not comply with specifications, check whether a newer version of the GSD file is available from the manufacturer. Install the current version. If a version of the GSD file that complies with the specification is not available, contact the device manufacturer.

### Connections (S7-300, S7-400)

Connections from SIMATIC STEP 7 projects can generally be migrated if they are also supported by the installed version of the TIA Portal.

#### Migratable types of connection

The following connection types can be migrated:

- S7 connection one-way
- S7 connection two-way
- Failsafe S7 connection
- TCP connection
- ISO-on-TCP connection
- ISO connection
- UDP connection
- E-mail connection
- FDL connection
- Point-to-point connection

FMS connections on the PROFIBUS are not accepted during the migration. Adapt the connections or modify the user program.

### Multiprojects (S7-300, S7-400)

#### Multiprojects in SIMATIC STEP 7

In SIMATIC STEP 7, you can organize projects into a multiproject if, for example, a project is very large or if several people are working on it. The subprojects may contain cross-project references, for example connections. All subprojects of a multiproject and the associated libraries are stored in the same directory.

#### Migration of parts of a multiproject

You can migrate the subprojects of a multiproject. To do this, select one of the subprojects during the migration. All of the devices and configurations contained in the respective subproject will be imported during the migration.

Observe the following when migrating a subproject:

- Cross-project connections

  Cross-project connections between subprojects are created as unspecified connections.
- Cross-project networking

  Information on networking of devices across project boundaries will be lost during the migration. Links between devices in the same subproject will be retained however.

#### Grouping a multiproject for the migration.

It is only possible to migrate an entire multiproject with all of its associated subprojects if you manually regroup the different subprojects prior to the migration. To regroup a multiproject, copy all devices, for example, and paste the devices into a single project.

### Migrating program blocks (S7-300, S7-400)

You can generally migrate all blocks created in LAD, FBD, SCL, STL, and GRAPH. Please note the following:

#### Programs with absolute addressing

In the TIA Portal, symbolic operands are automatically declared for all absolute addresses. If absolute addressing is used in the STEP 7 program to be migrated, symbolic operands are declared for the absolute addresses during the migration. This automatic declaration can lead to data type conflicts, particularly if the IEC check is activated in the TIA Portal. A data type conflict could occur, for example, when a 32-bit data word is interpreted as a tag with the type DWORD by the automatic declaration, but the program expects a tag with the data type REAL.

In this case, it is not enough to deactivate the IEC check. Instead, you must correct the declaration in the PLC tag table.

Data type conflicts can also occur if you access the same absolute address multiple times in the program, but use different data types for the different access operations. The following figure shows an example of such multiple access:

![Programs with absolute addressing](images/90011084043_DV_resource.Stream@PNG-de-DE.png)

In these cases, a separate tag is declared automatically for each data type during the migration. Since all tags reference the same absolute address, warnings are output in the PLC tag table. You need to manually correct these address overlaps in the PLC tag table.

#### Migration of communication blocks

During the migration of communication instructions from STEP 7 V5.x, pointers of the data type ANY are replaced by PLC tags within the own S7 station.

- After the migration a warning is displayed at the affected parameters.
- Replace the PLC tags with a pointer at the affected parameters.

  For absolute addressing of a data block with data type ANY, the data block must have been created with standard access, since symbolic addressing with data type ANY is not possible.

  Example: To input values, use the appropriate parameters of instruction P#M10.0 BYTE 4 instead of %MD10.

#### Symbolic names for blocks and user-defined data types (UDT)

In the TIA Portal, each block or UDT has a number and a name. It is therefore no longer necessary to declare symbolic names. If the migrated program contains symbol declarations for blocks or UDTs, they will be used as names after the migration.

#### Blocks from STEP 7 libraries

In the TIA Portal, standard functions and function blocks are not provided in libraries. Instead, they are available as instructions in the "Instructions" task card. The instructions are sorted by function and can be found under their symbolic name.

If calls of standard functions or function blocks are contained in the migrated program, they are replaced during the migration by the instructions that correspond to the original standard function or the original standard function block.

If the library block is no longer supported in the TIA Portal, you have the following options:

- The library block is replaced by a compatible instruction. In this case, you will receive an alarm informing you that you have to compile the program after migration. Note that the calling block may not carry any know-how protection, as the block call has to be adapted during compilation.

- If there is no compatible instruction, the block is migrated as user block. It is then available as a know-how protected block in the folder "Program blocks" with the extension "_LF" (legacy function).

#### User-defined block libraries

User-defined block libraries are no longer available in the familiar form in the TIA Portal. However, you can migrate user-defined libraries by integrating these into a project prior to migration and then migrating the project. After this, you can copy these from this project in the TIA Portal and use them.

#### Instructions in a modified display

The display of some of the LAD, FBD, STL, SCL and GRAPH commands in the TIA Portal differs from the display in earlier versions of STEP 7. So, for example, the mathematical functions and the comparators are no longer specific for data types. Instead, there is a central instruction, which can be used for all types of data. The "ADD_I" command is no longer permitted, for example; the instruction "ADD" is used instead.

Some other commands also have a new display in the TIA Portal, e.g., edge commands, word logic operations, conversions, IEC timers, IEC counters, etc.

The commands will be converted for the new display during the migration.

#### Stricter IEC check

Stricter rules for checking data type compatibility will be used in the TIA Portal. In addition, errors that can lead to runtime errors are already detected during the syntax check. It is no longer permitted to write your own input parameters or to read your own output parameters in functions (FC). Observe the following rules to avoid syntax errors:

- Only use tags with compatible data types when transferring the parameters.
- In comparison instructions or arithmetic instructions, only use tags with compatible data types.
- You may not write to input parameters or read from output parameters.

For more information on the block interface and on data type conversion with IEC check, refer to the Help on data types:

[Data types](Data%20types.md#overview-of-the-valid-data-types)

#### Stricter data type check with the "MOVE" and "FILL" instructions

With the "MOVE" and "FILL" instructions, the compatibility of the source and destination areas is checked according to stricter rules. It is no longer possible, for example, to move a tag of the data type "Integer" to a destination area of the data type "WORD" using "MOVE". Instead of this, use the "CONVERT", "T_CONV" or "S_CONV" instructions in the TIA Portal.

You will find more detailed information on the data types compatible with "MOVE" and "FILL" in the help on the instructions:

[MOVE: Move value](LAD%20%28S7-1200%2C%20S7-1500%29.md#move-move-value-s7-1200-s7-1500)

[FILL: Fill block](LAD%20%28S7-1200%2C%20S7-1500%29.md#fill-fill-block-s7-1500)

Programs that were created in LAD or in FBD and use invalid data types at the "MOVE" or "FILL" instruction are shown in STL after the migration. However, the language is still set as LAD or FBD in the block properties.

In the block properties, change the program again to STL. Then reset the language to LAD or FBD.

#### Suffix for I/O access ":P"

In the TIA Portal, the access ID ":P" is used for direct addressing of the I/O. The following notation is not permitted, for example:

%PIW3

The following notation is used instead:

%IW3:P //absolute display

MyTag:P //symbolic display

The accesses are converted into the new notation during the migration. However, symbolic names, which were declared to be I/O tags in the original program, cannot be accepted. New declarations will be created instead. For more information on the I/O access refer to the Help on addressing the I/O:

[Address I/O](Programming%20basics.md#accessing-io-devices)

#### No distinction is made between upper and lower case for jump labels

No distinction is made between upper and lower case for jump labels in the TIA Portal. If the source program contains jump labels that differ only through upper/lower case, these will be converted into unique jump labels. The log file provides information on the modified jump labels.

#### German special character "ß" is not distinguished from "ss"

In tag names, the German special character "ß" is not distinguished from "ss" in the TIA Portal. If, for example, the source program contains tag names that differ only in these two characters, they will be converted into unique tag names.

#### Migration of REAL and STRING values

In the TIA Portal it is checked whether the start values of REAL and STRING tags are in the permitted and/or declared range. The following rules apply:

- REAL tags must have a value in the range from +1.175494E-38 to +3.402823E+38.
- The maximum length of the STRING value must not exceed the declared length of the STRING.

If these rules are not satisfied, the program will be successfully migrated but it will not then be possible to compile it.

As remedy, you can open the corresponding data block in STEP 7 (TIA Portal) and change the start values. Then compile the program with the menu command "Software (rebuild all blocks)".

#### Migration of global data blocks

The display and handling of data values in data blocks is different in the TIA Portal compared with SIMATIC STEP 7. In global data blocks which are not derived from a higher-level object, for example a UDT, the tags are always assigned the default value of the data type as the default value, for example FALSE for the data type BOOL. This default value is not editable. If offline initial values were assigned in the declaration view, they are not imported during the migration. If you require user-specific default values in the program, use a global data block based on a PLC data type. You can assign user-specific default values for tag values in a PLC data type.

For more information on data values in data blocks refer to the Help on data blocks:

[Programming data blocks](Programming%20data%20blocks.md#defining-start-values)

#### Tag tables

The tag tables from the original program are not migrated to the TIA Portal. To monitor tags online in the TIA Portal, you create so-called "watch tables". These have the same function as the tag tables in SIMATIC STEP7.

> **Note**
>
> **Additional support for migration**
>
> You can find the latest information about migration in the Siemens Industry Online Support:
>
> [Migration of controllers](http://support.automation.siemens.com/WW/view/en/83557459)
>
> If you need further support, please contact SIMATIC Customer Support.

#### **"Ret_val" as tag name in the Block interface**

If the keyword "Ret_val" is used as tag name in the reference program in a block interface, the block is not migrated correctly. In this case, correct the reference program and re-migrate it.

### Migration of LAD/FBD/STL programs (S7-300, S7-400)

LAD, FBD and STL blocks can run after the migration without being recompiled or reloaded.

#### STL sources

STL sources cannot be migrated to the TIA Portal. Create STL blocks from your sources prior to migration. You can then migrate these once again as sources to the TIA Portal. To do so, use the "Generate source from blocks" shortcut menu command in the project tree.

See also: [Using external source files](Creating%20and%20managing%20blocks.md#using-external-source-files)

#### Know-how protection

Blocks that were know-how protected before the migration remain know-how protected after the migration. Because the sources are not migrated, the know-how protection cannot be canceled. The blocks can thus not be opened or edited. It is possible, however, to load the blocks into the CPU and to run them.

The following options are available for disabling a block's know-how protection:

- Prior to the migration, remove the KNOW_HOW_PROTECT attribute from the source and create a block without know-how protection from this. Then migrate this block.
- Import the source into the TIA Portal and create a block without know-how protection from this. Then use the "Edit &gt; Know-how protection" menu command to provide the block with a password.

#### Switch-over from LAD/FBD to STL

More precise syntax checks are performed in some areas in the TIA Portal than in older versions of STEP 7. However, the migration ensures where possible that your program can still be compiled: If a LAD/FBD block contains operations that would result in a syntax error in the TIA Portal, the affected networks are shown in STL after the migration. The semantics of the source program remain unchanged.

A message in the migration log informs you of the conversion of the programming language of individual networks.

### Migrating GRAPH programs (S7-300, S7-400)

#### Requirement

The prerequisite for migrating GRAPH blocks is to have the "S7-GRAPH" optional package, version 5.3 SP6 or later, installed on the original device.

#### GRAPH-specific block settings

The GRAPH-specific block settings have been significantly reduced in the TIA Portal. The following table gives an overview of how the original block settings are transferred to the TIA Portal.

| Setting in the initial project |  | Setting in the TIA Portal |
| --- | --- | --- |
| FB parameter | Minimum | Existing parameters will be migrated |
| Standard |  |  |
| Maximum |  |  |
| Definable |  |  |
| Interface description | Minimized memory space | Create minimized DB |
| Structure fields | Individual structures are always created |  |
| Individual structures |  |  |
| Run capability | FC70/71 | FC 73 if the option "Create minimized DB" is active; otherwise FC 72 |
| FC72 |  |  |
| FC73 |  |  |
| Criteria analysis in the DB |  | Setting not relevant in the TIA Portal |
| Skip steps |  | Skip steps |
| Acknowledge errors |  | Acknowledge supervision errors |
| Synchronization |  | Always activated in the TIA Portal |
| Permanent processing of all interlocks in manual operation |  | Permanent processing of all interlocks in manual operation |
| Lock operating mode selection |  | Lock operating mode selection |
| Safe activation mode |  | Always activated in the TIA Portal |
| Warnings | None | Always activated in the TIA Portal |
| Any |  |  |
| Activate alarms |  | Activate alarms |
| Alarms with WR_USMSG |  | Alarms in the TIA Portal always with ALARM_SQ/ALARM_S |

#### Step name extension

Step name extensions are not supported in the TIA Portal. They are converted to step-specific text during the migration.

#### Compiling the migrated block

GRAPH blocks must be recompiled and reloaded after the migration.

The following errors may occur when compiling:

- Data type conflicts may occur due to the stricter IEC check. In this case, change the declaration.
- Since the "structure fields" setting for the interface is no longer available in the TIA Portal, interface elements can no longer be addressed with G7S[1].X, for example. Access to the element must therefore be corrected, e.g. to STEP1.X.

#### Changing the interface of the GRAPH block

The changed settings can lead to interface changes of the block. Therefore, it may be necessary to regenerate the instance DB or to update block calls.

### Migrating SCL programs (S7-300, S7-400)

The prerequisite for migrating SCL blocks is to have the "S7-SCL" option package, version 5.3 SP5 or later, installed on the original device.

SCL blocks must be recompiled and reloaded after the migration.

#### Basic procedure for the migration

A complete migration of SCL blocks is only carried out if the associated sources exist in the initial project.

The table below gives you an overview of the basic procedure:

| Existing in the initial project | Existing after migration |
| --- | --- |
| SCL blocks with source | Editable SCL blocks |
| Know-how protected SCL blocks with source | Editable SCL blocks. After the migration, the blocks no longer have know-how protection but can be re-protected, if necessary. |
| SCL blocks without source | Know-how protected SCL blocks |
| Know-how protected SCL blocks without source | Know-how protected SCL blocks |

#### SCL-specific compiler options

Only the compiler options that are defined directly in an SCL source are adopted as block properties in the TIA Portal during migration. If no compiler options are defined in the original SCL source, the options in the properties of the migrated block are deactivated.

Compiler options defined as settings in the SCL Editor or in an SCL compile control file are not migrated.

The following table gives an overview of the compiler options that are transferred as block property to the TIA Portal.

| Compiler option in the SCL source | Block property in the TIA Portal |
| --- | --- |
| scl_monitorarraylimits | Check ARRAY limits |
| scl_createdebuginfo | Create extended status information |
| scl_setokflag | Set ENO automatically |

#### Calling function blocks

A block call with indication of the function block, for example "DBX"."FBX()", is no longer permitted in the TIA Portal. The call syntax is converted to the notation "DBX()" during the migration.

#### New EN/ENO mechanism

SCL uses the EN/ENO mechanism of the TIA Portal. For this reason, all usages of the OK flag are replaced by ENO during the migration. The points where ENO was used in the original program are highlighted. You must check these points after the migration and adapt them to the new mechanism.

See also:

[EN/ENO mechanism](Programming%20basics.md#eneno-mechanism)

#### Operator "DIV"

The "DIV" operator is no longer available in the TIA Portal. All usages of "DIV" will be converted to the standard notation "/" during the migration.

#### Local constants

Local, symbolic constants are declared in the "CONST" section of the block interface in the TIA Portal. They always have a data type. If symbolic constants are declared without data type in the source program, an appropriate data type will be assigned to them during the migration.

In classic SCL programs it was possible to use local constants as ARRAY limits. These declarations are retained during migration.

Example for the declaration of ARRAY limits with local constants in a classic SCL program:

VAR_INPUT

MyArray : Array[MyConst1 .. MyConst2] of Int;

END_VAR

This declaration looks as follows after the migration:

![Local constants](images/94980845579_DV_resource.Stream@PNG-de-DE.png)

However, it is not possible to form expressions with local constants in the block interface of the TIA Portal and use them for the declaration of ARRAY limits or initialization of values. Instead the event of the expression is formed during migration and entered as value in the declaration. The expression from the source program is stored as comment.

Example for the declaration of ARRAY limits with the help of expressions in a classic SCL program:

CONST

MyConst1Value10 := int#10;

MyConst2Value10 := int#10;

MyConst20 := MyConst1Value10 + MyConst2Value10 ;

MyConst0 := MyConst1Value10 - MyConst2Value10 ;

MyConst100 := MyConst1Value10 * MyConst2Value10 ;

END_CONST

This declaration looks as follows after the migration:

![Local constants](images/94980854411_DV_resource.Stream@PNG-de-DE.png)

See also:

[Basics of constants](Programming%20basics.md#basics-of-constants)

[Declaring local tags and constants in the block interface](Declaring%20the%20block%20interface.md#declaring-local-tags-and-constants-in-the-block-interface)

#### Nested ARRAYs

It is not possible to nest ARRAYs in the TIA Portal. The following declaration is not permitted, for example:

ARRAY[1..5] OF ARRAY[0..3] OF INT

Nested ARRAYs are converted into multi-dimensional ARRAYs during migration. The example would look as follows after the migration:

ARRAY[1..5, 0..3] OF INT

#### Violation of ARRAY limits

During compilation in older versions of STEP 7, it was not checked whether the program contained invalid accesses to ARRAYs. Accesses to ARRAY elements which lay outside the declared ARRAY limits, were therefore not reported as syntax errors. If the program was loaded with errors, runtime errors could occur.

In TIA Portal the violation of the ARRAY limits is checked by a more precise syntax check. If the program contains access errors, these will now be reported during compilation. In this case, correct the access and recompile the program. You have the option to use a tag as an ARRAY index.

See also:

[Addressing ARRAY components](Data%20types.md#addressing-array-components)

#### Declaration of jump labels (LABEL)

The declaration of jump labels is not possible in the TIA Portal. The following declaration would not be accepted from the initial project, for example:

LABEL

MARKE1, MARKE2, MARKE3 ;

END_LABEL

Set jump labels, however, will be retained in the program code and can be used for GOTO operations.

#### Indexed I/O access

In the TIA Portal, the syntax with rounded parentheses is used for indexed I/O access. The following notation is not permitted, for example:

PEB[1]

The following notation is used instead:

EB(1):P

The accesses are converted into the new notation during the migration.

See also:

[Accessing I/O devices](Programming%20basics.md#accessing-io-devices)

#### Indexed memory accesses

In the TIA Portal, the syntax with rounded parentheses is used for indexed memory accesses. The following notation is not permitted, for example:

EB[2]

The following notation is used instead:

EB(2)

The accesses are converted into the new notation during the migration. For additional information on addressing, refer to "See also".

#### Indexed access to data blocks

In the TIA Portal, the syntax with rounded parentheses is used for indexed data block accesses. The following notation is not permitted, for example:

%DB100.DW[5]

The following notation is used instead:

%DB100.DW(5)

The accesses are converted into the new notation during the migration. For additional information on addressing, refer to "See also".

#### Absolute access to data blocks

For absolute access, the absolute designator of the data block must be used. Access using the symbolic designator is not permitted in the TIA Portal.

The following notation is not permitted, for example:

DB100.DW3

The following notation is used instead:

%DB100.DW3

During the migration, the marker "%" will be added for a detected absolute data block access. For additional information on addressing, refer to "See also".

#### Logarithmic functions "EXPD" and "LOG"

Logarithmic functions "EXPD" and "LOG" are no longer available in the TIA Portal. All usages of "EXPD" are converted to the standard notation "10**(&lt;expression&gt;)" during the migration. All usages of "LOG" are converted to the standard notation "LN(&lt;expression&gt;)" during the migration.

#### Mathematical instruction "MAX"

The "MAX" instruction cannot process any time data types in the TIA Portal. However, you can use comparators instead.

The following example shows how you can find the "larger" of two time data types using comparators:

| SCL |  |
| --- | --- |
| #xs_tod := #xi_tod + #xi_time;   // statt #xstod1 := MAX(IN1:=#xtod1, IN2:=#xstod1);   IF #xs_tod &lt; #xi_tod THEN   #xs_tod := #xi_tod;     END_IF;     // statt #xsd1 := MAX(IN1:=#xd1, IN2:=#xsd1);   IF #xi_date &lt;#xs_date THEN   #xs_date := #xi_date;     END_IF;  #xs_date_time := #xi_date_time + #xi_time;   // statt #xs_date_time := MAX(IN1:=#xi_date_time, IN2:=#xs_date_time);   IF #xi_date_time &lt;#xs_date_time THEN   #xs_date_time := #xi_date_time;     END_IF; |  |
|  |  |

#### Floating point numbers - exponential display

The exponential notation of floating point numbers without a decimal point is no longer permitted in the TIA Portal. The following notation is not permitted, for example:

3E10

The following notation is used instead:

3.0E10

During the migration, all usages of "3E10" will be converted to the standard notation "3.0E10".

See also:

[Floating-point numbers](Data%20types.md#floating-point-numbers)

#### Blocks from STEP 7 libraries

The functions FC 1 to FC 40 from the STEP 7 classic library "IEC standard functions" are no longer available in the TIA Portal. Calls to the standard functions are converted to calls to the corresponding extended instructions during the migration. If there is no clear conversion possibility, a system error is issued.

In this case, change the SCL block after the migration and use SCL instructions or operators instead of IEC standard functions.

Examples:

Use S5TIME_TO_TIME instead of S5TI_TIM (FC 33)

"TAG_TIME" := S5TIME_TO_TIME ("TAG_S5TIME");

Use the comparator operator &lt;&gt; instead of NE_DT (FC 9):

IF #D1 &lt;&gt; #D2 THEN "MyOutput" : = 10;

END_IF;

Use the comparator operator = instead of EQ_STRING (FC 10):

IF #My_String1 = #MyString2 THEN "MyOutput" : = 10;

END_IF;

#### Interruption of strings with "$"

In STEP 7 Classic, strings in SCL could be interrupted by special characters, e.g., control characters or non-printable characters. These characters were identified by the interruption sequences "$&gt;" and "$&lt;".

Example:

#myString := 'Test1$&gt; $&lt;Test1';

This option no longer exists in the TIA Portal. String interruptions will be deleted during the migration.

#### NULL pointer

Null pointers are no longer specified in the TIA Portal with "NIL" but instead with "NULL". The notation is replaced automatically during the migration.

#### Comments

Comments from the migrated source are transferred when possible. The following rules apply:

- Comments in the output block directly after the block definition are converted as block comments.
- Comments that appear as line comments after a tag declaration are transferred to the "Comment" column in the block interface.
- All other comments are not transferred.

Example:

// Comment that is not transferred.

FUNCTION_BLOCK FB57

// Comment that is transferred to the block properties.

(*Comment that is transferred to the block properties. *)

VAR_TEMP

    myVar1 : INT;// Comment that is transferred to the interface.

    myVar2 : INT;(* Comment that is not transferred because it is a comment section *)

END_VAR

// Comment that is not transferred.

BEGIN

    ;

END_FUNCTION_BLOCK

#### **Block calls in S7-SCL sources**

In the S7-SCL sources with STEP 7 V5.x, you can set the block parameters before or after the actual call of the block. This means that the block can be called with incomplete parameters and the input/output parameters of the block can be suppled with tags or values at a different position with the S7-SCL source. This type of programming is not possible in STEP 7 (TIA Portal) due to the system and will also not be supported in future. Although you can migrate and compile the STEP 7 V5.x project without errors in TIA portal, the function of this block call is no longer possible within the S7-SCL program.

Before you compiled your S7-SCL source in STEP 7 V5.x and migrate the project to the TIA Portal, note the following points:

- All parameters of the called block must be supplied within the call instruction.
- No parameters of the called block may be deleted and inserted or set at a different position of the S7-SCL source.

---

**See also**

[Declaring global constants](Declaring%20PLC%20tags.md#declaring-global-constants)
  
[Addressing operands](Programming%20basics.md#addressing-operands)

### Messages (S7-300, S7-400)

PLC alarms are migrated with all parameters and including all alarm classes. Alarm types and alarm instances are also migrated and stored under the PLC alarms in the TIA Portal.

#### Requirement

A requirement is that the CPU-wide assignment of alarm numbers is selected in the initial project. Before the migration, select the "Always assign CPU-oriented unique message numbers" option in the initial project, if necessary, and perform "Save as &gt; With reorganization".

#### Restrictions

- Symbol-based alarms cannot be migrated.
- The keywords "$$AKZ$$", "$$BlockComment$$", and "$$Area$$" are transferred but no replacement takes place during runtime.

### Reporting system errors (S7-300, S7-400)

In principle, you can migrate system error messages that you have configured using SIMATIC STEP 7.

#### Restrictions

When migrating the "Report system errors" application, only the settings that were set by the user in the SIMATIC STEP 7 project will be migrated (e.g. basic settings, block numbers, block names).

The following elements are not migrated:

- SFM blocks
- SFM messages and the settings that were made to configure the message texts
- System text libraries

After migration, the settings can be manually adjusted once again. The missing elements will be recreated during the first compilation of the hardware configuration.

### Migration of project texts (S7-300, S7-400)

When you migrate an initial project, project texts such as block titles and block comments are adopted in the TIA Portal. However, only project texts in the set editing language of the initial project are migrated. Project texts in other languages are not migrated.

---

**See also**

[Migration of STEP 7 projects (S7-300, S7-400)](#migration-of-step-7-projects-s7-300-s7-400)
  
[Project text basics](Editing%20project%20data.md#project-text-basics)
