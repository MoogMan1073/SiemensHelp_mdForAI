---
title: "Migrating PLC programs to a S7-1500 CPU / ET 200SP"
package: ProgPLCMigration15enUS
topics: 57
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Migrating PLC programs to a S7-1500 CPU / ET 200SP

This section contains information on the following topics:

- [Basic information on migrating PLC programs (S7-1500)](#basic-information-on-migrating-plc-programs-s7-1500)
- [Performing migration (S7-1500)](#performing-migration-s7-1500)
- [Displaying a log file (S7-1500)](#displaying-a-log-file-s7-1500)
- [Special considerations for migrating PLC programs (S7-1500)](#special-considerations-for-migrating-plc-programs-s7-1500)

## Basic information on migrating PLC programs (S7-1500)

### Introduction

You can migrate PLC programs within the TIA Portal. Migration within the TIA Portal is called "PLC migration". With this migration, the new module will be created in the project and the existing PLC program copied to the new module. The old module remains available unchanged in the project.

The advantage of migration compared to copying is that the program is automatically adapted to the new CPU family as much as possible. Program structures that are no longer permitted are updated. Instructions that are not available on the new module are replaced with corresponding S7-1500 instructions.

The table below gives you an overview of the modules that can be migrated:

| Original block | Target block |
| --- | --- |
| S7-300/400 CPU | S7-1500 CPU |
| ET 200S CPU | ET200SP CPU |
| ET 200S CPU | S7-1500 CPU |
| ET 200S CPU | ET 200pro CPU |
| IM 154-8 CPU | CPU 1516-2 PN |

The migration to S7-1500 and the migration to ET 200SP follow the same rules. The PLC programs are treated identical in both migration operations.

### Scope of migration

During PLC migration, all components of the PLC program are copied to the newly created module. The following objects are included, for example:

- Program blocks, whose programming language is supported by S7-1500 and that have no know-how protection.
- PLC tag tables
- Watch and force tables
- PLC data types
- Technological objects
- User-defined groups in the project navigation

The hardware configuration of the output module is not transferred automatically.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Preventing personal injury and material damage**  Changes are made to the program during PLC migration in some cases. It is therefore very important that you thoroughly review the program in a test environment after migration before putting it in operation. |  |

> **Note**
>
> **Additional support for PLC migration**
>
> You can find the latest information about PLC migration in the Siemens Industry Online Support:
>
> Migration of complete systems:
>
> <http://support.automation.siemens.com/WW/view/en/83558085>
>
> Migration of controllers:
>
> <http://support.automation.siemens.com/WW/view/en/83557459>
>
> Migration of visualization:
>
> <http://support.automation.siemens.com/WW/view/en/76878921>
>
> Migration of communication:
>
> <http://support.automation.siemens.com/WW/view/en/83558087>
>
> FAQs on migration:
>
> <http://support.automation.siemens.com/WW/view/en/67858106>
>
> If you need further support, please contact SIMATIC Customer Support.

> **Note**
>
> **Additional information on the TIA Portal**
>
> Additional information on all aspects of the TIA Portal can be found in the TIA Portal in the Siemens Industry Online Support.
>
> <http://support.automation.siemens.com/WW/view/en/65601780>
>
> There you will find information on our training offers. For experienced users of the classic SIMATIC S7 system who want to upgrade efficiently to SIMATIC S7-1500 with the TIA Portal, we recommend "TIA-SYSUP - SIMATIC TIA Portal system retraining course for SIMATIC S7-1500".

## Performing migration (S7-1500)

### Requirement

- A consistent reference program is available.
- All blocks are compiled up-to-date. This also applies to blocks that are included in the project, but will not be called during program execution.
- The program was created with TIA Portal V12 or later or upgraded to this version.

> **Note**
>
> **Instruction profiles**
>
> No instruction profile should be activated during PLC migration.
>
> Deactivate your instruction profile before you perform the PLC migration. You can then reactivate the profile again.

### Preparing for migration

Proceed as follows to prepare the program for migration:

1. Open the device that contains the reference program in the project navigation.
2. Open the folder "Program blocks" and check whether it contains know-how protected blocks.
3. Remove the know-how protection from the blocks.
4. Open the folder "Program blocks > System blocks" and check whether the block contained therein include the extension "_LF" (legacy functions).

   These are library blocks from STEP 7 that are no longer supported in the TIA Portal. These blocks are not transferred to the new device during PLC migration because they are know-how protected.
5. If possible, replace the blocks with an instruction from the "Instructions" task card.
6. If the program contains instructions on alarm configuration, follow the instructions for migrating alarms with associated values.

   See also: [Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)

### Procedure

To migrate a PLC program within the TIA Portal, follow these steps:

1. Open the device that contains the reference program in the project navigation.
2. Open the device configuration.
3. Select the module that contains the reference program in the device view or network view.
4. Select the "Migrate to S7-1500" command in the shortcut menu.

   The "Migrate to S7-1500" dialog opens.
5. In the "New device" area, select the device to which you want to migrate your program and confirm with "OK".

   A security message appears informing you that the program will be changed during the migration.
6. Confirm the security prompt.

   A dialog opens in which you can specify which instructions you want to use for point-to-point communication in the migrated program.
7. Select the required set of instructions.

   - Select the option "Use new PtP instructions for the integrated communication modules of the S7-1500" to use the new PtP instructions of the S7-1500.
   - Select the option "Continue to use PtP instructions for S7-300/400 communications processors" to continue using the PtP instructions of the CP 300/400 or ET200.

   You must select one of the two options even if you do not use point-to-point communication. The selection does not have an effect on the program in this case.

   The PLC program is migrated. An alarm then appears notifying you whether errors occurred during the migration. The alarm also contains a link to the migration log.
8. Open the migration log. It contains details on the migration and informs you about program changes which you must perform to make your program executable on the new device.
9. Process all the information contained in the migration log.
10. Compile the migrated project.

    See also: [Migrating point-to-point program blocks](#migrating-point-to-point-program-blocks-s7-1500)

### Result

A new device is created next to the original device in the project navigation. It contains the migrated PLC program.

To access the full functionality of the S7-1500, we recommend that you enable optimized block access for the migrated blocks. You can find additional information in the Help under Blocks with optimized access:

[Blocks with optimized access](Programming%20basics.md#blocks-with-optimized-access)

> **Note**
>
> Note that only the PLC program is converted by the PLC migration. The hardware configuration of the original device is not automatically transferred to the new device. Perform the hardware configuration of the new device manually after the migration.

---

**See also**

[Using logs](Editing%20projects.md#using-logs)

## Displaying a log file (S7-1500)

A log file is created for each migration. The log file contains the following information:

- Modifications to objects made during migration.
- Information on necessary adaptations you need to make to the program.

### Procedure

To display the log file of the migration, follow these steps:

1. Open the "Common data > Logs" folder in the project tree. It contains the logs of all previously performed migrations.
2. Double-click the required migration log.

   The log opens.
3. Messages that relate to a certain position in the program are marked with an arrow in the "Go to" column. Double-click on the arrow to jump to the relevant position in the program.
4. Messages for which additional information is available are marked with a question mark in the "?" column. To obtain additional information on the message, click the question mark.

---

**See also**

[Using logs](Editing%20projects.md#using-logs)

## Special considerations for migrating PLC programs (S7-1500)

This section contains information on the following topics:

- [Information on migrating PLC programs (S7-1500)](#information-on-migrating-plc-programs-s7-1500)
- [Migration of instructions to S7-1500 (S7-1500)](#migration-of-instructions-to-s7-1500-s7-1500)
- [Migration of LAD/FBD programs to S7-1500 (S7-1500)](#migration-of-ladfbd-programs-to-s7-1500-s7-1500)
- [Migration of STL programs to S7-1500 (S7-1500)](#migration-of-stl-programs-to-s7-1500-s7-1500)
- [Migration of SCL programs to S7-1500 (S7-1500)](#migration-of-scl-programs-to-s7-1500-s7-1500)
- [Migration of GRAPH programs to S7-1500 (S7-1500)](#migration-of-graph-programs-to-s7-1500-s7-1500)

### Information on migrating PLC programs (S7-1500)

This section contains information on the following topics:

- [Migrating organization blocks (S7-1500)](#migrating-organization-blocks-s7-1500)
- [Migrating hardware IDs (S7-1500)](#migrating-hardware-ids-s7-1500)
- [Migrating IEC timers and IEC counters (S7-1500)](#migrating-iec-timers-and-iec-counters-s7-1500)
- [Migrating CPU data blocks (S7-1500)](#migrating-cpu-data-blocks-s7-1500)
- [Migrating diagnostics functions (S7-1500)](#migrating-diagnostics-functions-s7-1500)
- [Migrating absolute access to local data (S7-1500)](#migrating-absolute-access-to-local-data-s7-1500)
- [Block parameters in S7-1500 (S7-1500)](#block-parameters-in-s7-1500-s7-1500)
- [Multi-instance capability in S7-1500 (S7-1500)](#multi-instance-capability-in-s7-1500-s7-1500)
- [Floating-point numbers in S7-1500 (S7-1500)](#floating-point-numbers-in-s7-1500-s7-1500)
- [Writing individual characters of a STRING to S7-1500 (S7-1500)](#writing-individual-characters-of-a-string-to-s7-1500-s7-1500)
- [Access to the status word in S7-1500 (S7-1500)](#access-to-the-status-word-in-s7-1500-s7-1500)
- [Loading software changes to S7-1500 (S7-1500)](#loading-software-changes-to-s7-1500-s7-1500)

#### Migrating organization blocks (S7-1500)

##### Organization blocks

The following rules apply to migration of organization blocks:

- Block names and numbers are transferred unchanged.
- The block interface is also accepted unchanged.
- The OB is assigned to the event corresponding to the OB type.
- The OB parameters, such as the priority, remain unchanged. If additional parameters can be assigned in the new CPU, they will be assigned default values.

Some organization blocks (OBs) are not supported by S7-1500 and therefore cannot be migrated. The following table provides an overview of these organization blocks and contains information on how you can reproduce the functionality in your program.

| Non-migratable OB | Notes |
| --- | --- |
| OB60 (multicomputing interrupt) | The OB cannot be replaced. Multicomputing is not available on S7-1500. |
| OB65 (technology synchronization interrupt) | Check whether the OB in your program can be replaced by the MC servo OB or the MC interpolator OB. |
| OB7x (redundancy error) | The OB cannot be replaced. Redundancy is not available on S7-1500. |
| OB81 (power supply error) | Check whether the OB in your program can be replaced by the diagnostic interrupt OB. |
| OB84 (CPU hardware fault) | Check whether the OB in your program can be replaced by the diagnostic interrupt OB. |
| OB85 (program execution error) | Check whether the OB in your program can be replaced by the pull/plug OB or the rack error OB. |
| OB87 (communications error) | Check whether the OB in your program can be replaced by the diagnostic interrupt OB. |
| OB88 (processing interrupt) | Check whether the OB in your program can be replaced by the programming error OB. |
| OB90 (background cycle) | The OB cannot be replaced. Background processing is not available on S7-1500. |
| OB101 (hot restart) | The OB cannot be replaced. Hot restart is not available on S7-1500. |
| OB102 (cold restart) | Check whether the OB in your program can be replaced by the startup OB. |

---

**See also**

[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)
  
[Organization blocks (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#organization-blocks-s7-1500)
  
[Description of all types of organization blocks (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#description-of-all-types-of-organization-blocks-s7-1500)
  
[Setting parameters of organization blocks (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#setting-parameters-of-organization-blocks-s7-1500)
  
[FAQs on migration](http://support.automation.siemens.com/WW/view/en/67858106)

#### Migrating hardware IDs (S7-1500)

##### Addressing modules by means of hardware IDs

If your program addresses hardware modules, for example, at the "LADDR" or "ID" parameter, these addresses are no longer valid after migration to the new hardware. The addresses must be replaced. The hardware modules of the S7-1500 are addressed by hardware IDs. This means you have to enter the hardware identifier of the new module at the "LADDR" or "ID" parameter after migration.

To do this, follow these steps:

1. Open the device configuration.
2. Select the module that you want to address.
3. Select the "Properties > System constants" tab in the Inspector window.

   The table contains constants for all modules used and the required HW identifiers.
4. Select the constants for the module to be addressed and select the "Copy" command from the shortcut menu.
5. Insert the constants at the "LADDR" or "ID" parameter of the migrated instruction.

![Addressing modules by means of hardware IDs](images/69370276491_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[Instructions for address conversion (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#instructions-for-address-conversion-s7-1200-s7-1500)
  
[Example for the use of hardware identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#example-for-the-use-of-hardware-identifiers-s7-1200-s7-1500-s7-1500t)

#### Migrating IEC timers and IEC counters (S7-1500)

##### **Updating IEC timers**

The "Q" and "ET" outputs of the IEC timers TP, TON and TOF are determined in S7-300/400 at the point in time at which the program runs the IEC timer. After this, the status of "Q" and "ET" remains unchanged. If you access these outputs multiple times in the program, you therefore always receive the same value.

This behavior has changed in S7-1500: Here, the program checks the current timer value at each access and determines the "Q" and "ET" outputs again.

Thus, after the migration, the behavior of your program may change if you access "Q" or "ET" multiple times.

For the program to demonstrate the same behavior as in S7-300/400, you can assign the value of "Q" or "ET" to a tag. In the program, you then reference this tag instead of the output.

##### IEC timers and IEC counters with EN/ENO interconnection

The instructions have been adapted to the IEC 1131-3 standard for S7-1500. They are now connected to the current path via the "IN" parameter and therefore no longer have the "EN" and "ENO" parameters. The migration reports an error if the reference program includes an IEC timer or IEC counter with preceding logic that is evaluated using the "EN" input parameter.

Insert a jump instruction between the preceding logic and the IEC timer or IEC counter to call the IEC timer or IEC counter based on the RLO. The following jump instructions are available:

- ---( JMP ): Jump if RLO = 1
- ---( JMPN ): Jump if RLO = 0

##### IEC counters: New parameters for the counter status in the block interface

After the migration, the block interface contains the "QU" and "QD" parameters instead of the "Q" output parameter for the counter status of an IEC counter. Only one of the two parameters is read out, depending on the IEC counter type. The other parameter in each case is not used.

If you have accessed the "Q" parameter in the program code, you need to manually adjust the access after the migration. Use "QU" if you are counting up and "QD" if you are counting down.

---

**See also**

[Using IEC timers and counters (S7-1200, S7-1500)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#using-iec-timers-and-counters-s7-1200-s7-1500)

#### Migrating CPU data blocks (S7-1500)

##### CPU data blocks

Blocks that were created in the CPU by the CREAT_DB or CREATE_DB instruction and are only available online are not migrated.

---

**See also**

[Migration of data block instructions (S7-1500)](#migration-of-data-block-instructions-s7-1500)
  
[CPU data blocks](Programming%20basics.md#cpu-data-blocks)
  
[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

#### Migrating diagnostics functions (S7-1500)

##### System status lists

CPUs of the S7-1500 series do not provide system status lists. However, you can read some of the information using the "GET_DIAG", "Geo2Log", "DeviceStates", or "ModuleStates" instruction.  
Additional information on migration of system status lists is available under: [Migrating the RDSYSST instruction](#migration-of-the-instruction-rdsysst-s7-1500)

##### System diagnostics with "Report System Errors"

The CPUs of the S7-1500 series have integrated system diagnostics. "Report System Errors" is therefore no longer supported. If the program contains blocks for "Report System Errors", disable system diagnostics in the reference program prior to migration and recompile the program. The blocks in question are deleted during this process.

System diagnostics for the S7-1500 CPUs is enabled by default. You do not have to make any additional settings.  
To change the settings for the system diagnostics, select the CPU in the device configuration. The settings for the system diagnostics are then shown in the Inspector window under "Properties > System diagnostics". The alarms of the system diagnostics are enabled and can be deselected if they are not needed.

##### PROFINET/PROFIBUS diagnostics

The following rules apply to migration of PROFINET/PROFIBUS diagnostics:

- "Report system errors" is replaced by the integrated system diagnostics.
- FB 126 is not supported and can therefore not be migrated.
- Use the "DeviceStates" and "ModuleStates" instructions for application-specific evaluation.

#### Migrating absolute access to local data (S7-1500)

##### Absolute access to local data

Absolute access to the local data of a block was possible in S7-300/400 without declaring a symbol for the address.

Because pure absolute access in S7-1500 is no longer supported, migration deals with this as follows:

- If a temporary tag is declared in the block interface for an area within the local data, the absolute address is converted to a symbolic address.
- If there is no suitable temporary tag, the absolute address is retained. Because additional local tags may be created in some circumstances during migration, addresses may shift within the local data. Therefore, check to see if the absolute address you are using is still correct and if the correct data is being addressed. If possible, create a tag in the "Temp" section and use it for addressing. To specifically address areas within declared tags, you can overlay existing tags with AT or address individual areas with the syntax .X, .B, .W or .D.

##### Examples

The following examples show migration of absolute access to local data.

In the first table, you can see a program section prior to migration:

| STL |  |
| --- | --- |
| L %LW20  L %LW3  +I  T %LW5 |  |

In the second table, you can see a program section after migration:

| STL |  |
| --- | --- |
| L "MyTempVar1"  L "MyTempVar2"  +I  T %LW5 |  |

- Temporary tags were already declared for "LW20" and "LW3". These are used in the program after migration.
- No tag was declared for "LW5". You need to check if access is still correct after the migration.

---

**See also**

[Addressing areas of a tag with slice access (S7-1200, S7-1500)](Programming%20basics.md#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)
  
[Overlaying tags with AT](Programming%20basics.md#overlaying-tags-with-at)

#### Block parameters in S7-1500 (S7-1500)

##### Using block parameters

The following rules apply to the use of block parameters within the block in S7-1500:

- Input parameters may only be read.
- Output parameters may only be written.
- In/out parameters may be read and written.
- Function values (Ret_Val) may only be written.

If your program does not conform to these rules, a warning is output during compilation. In this case, convert the relevant input or output parameter to an in/out parameter.

Additional rules apply to the parameter assignment of functions (FC).

See also:

[Parameter assignment of functions](Programming%20basics.md#parameter-assignment-to-functions)

##### Block parameter as edge memory bit in functions (FC)

The above-mentioned rules for parameter assignment must also be observed when edge evaluations are programmed in functions (FC):

As edge memory bit, you require a data value that may be both read and written and that is retained for several cycles. Since input parameters (input) may only be read and output parameters (output) may only be written, these cannot be used as edge memory bits. Temporary local data (Temp) can also not be used as edge memory bits, because it is only available for one cycle.

Therefore, use only in/out parameters (InOut) as edge memory bits in functions (FC). You can also use a single bit of an in/out parameter as edge memory bit, if you address this via a slice access.

The following example shows you how to use an in/out parameter as edge memory bit.

| STL |  |
| --- | --- |
| FP #InOutFlagStore.x0 |  |

"InOutFlagStore" is an in/out parameter of the BYTE data type. The address "#InOutFlagStore.x0" addresses the bit address 0, which is used as edge memory bit.

##### Automatic initialization of block parameters in functions (FC)

In S7-300/400, temporary local data (Temp) of a function must be pre-assigned with a value. Otherwise, it may happen that the program operates with undefined values.

In S7-1500, the risk of continuing to process undefined values is considerably reduced because the parameters below are automatically initialized when the block is called:

- Temporary local data of the STRING and WSTRING data types are always pre-assigned with the maximum length 254 and actual length 0.
- Temporary local data with the elementary data type is automatically initialized in functions (FC) with optimized access. It is then assigned the value that has been predefined for the specified data type. For example, the value "false" is predefined for BOOL. Elements of the PLC data types are pre-assigned with the default value that is specified in the declaration of the PLC data type (UDT). Elements of the data type ARRAY, STRING or WSTRING are pre-assigned with the value "0", even if they are used within a PLC data type.

In S7-300/400, output parameters (Output) in functions had to be assigned a value, because unwanted reactions could otherwise have occurred in the program. When jump instructions or RLO instructions were used, each supported program path then had to be checked.

In S7-1500, the risk of undefined output parameters is considerably reduced because the output parameters of the elementary data type are automatically initialized when blocks are called. They are then pre-assigned the value that was predefined for the specified data type. For example, the value "false" is predefined for BOOL. However, structured output parameters are not pre-assigned with a value. They are transferred as pointer when a block is called and therefore cannot be undefined.

---

**See also**

[Transfer parameter as copy or as pointer](Programming%20basics.md#transfer-parameter-as-copy-or-as-pointer)
  
[Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)

#### Multi-instance capability in S7-1500 (S7-1500)

##### Multiple instance capability

All function blocks in the CPUs of the S7-1500 series have multiple instance capability. This means FBs that were labeled as not having multiple instance capability in the reference program are converted to blocks with multiple instance capability by the migration. A note is output in the migration log for each converted FB. If you continue to use the FB as a single instance after migration, your program runs unchanged.

---

**See also**

[Instances](Programming%20basics.md#instances)

#### Floating-point numbers in S7-1500 (S7-1500)

##### Invalid floating-point numbers

The handling of invalid floating-point numbers in S7-1500 differs from S7-300/400. Example:

- S7-300/400: The result of the expression "Invalid floating-point number <> 1.0" is FALSE.
- S7-1500: The result of the expression "Invalid floating-point number <> 1.0" is TRUE.

Note that the instructions in your program can produce other results due to this difference.

---

**See also**

[Floating-point numbers](Data%20types.md#floating-point-numbers)

#### Writing individual characters of a STRING to S7-1500 (S7-1500)

##### Writing individual characters of a STRING

If a character or a byte within a STRING is to be written, an S7-1500 CPU checks whether the target address lies within the actual length of the STRING. If not, the character or byte is not written. The only exception is when the character is written directly after the actual length of the STRING.

The following example shows the string 'hello' with the actual length of 5. The 27th character of the STRING lies outside the actual length and can therefore not be written. The STRING remains unchanged; the result of the assignment is 'hello'.

| SCL |  |
| --- | --- |
| MyDB.mystring := 'hello'; |  |
| MyDB.mystring[27] := CHAR_TO_BYTE('!'); |  |

The following example shows the specified exception: The character is written directly behind the STRING to the 6th character. The result of the assignment is 'hello!'.

| SCL |  |
| --- | --- |
| MyDB.mystring := 'hello'; |  |
| MyDB.mystring[6] := CHAR_TO_BYTE('!'); |  |

Where possible, use instructions from the "Extended instructions > String + Char" pane to handle STRINGs.

| SCL |  |
| --- | --- |
| CONCAT(IN1 := 'hello', IN2 := '!'); |  |
|  |  |

---

**See also**

[Addressing individual characters of a STRING or WSTRING (S7-1200, S7-1500)](Data%20types.md#addressing-individual-characters-of-a-string-or-wstring-s7-1200-s7-1500)
  
[String + Char (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#string-char-s7-1200-s7-1500)

#### Access to the status word in S7-1500 (S7-1500)

##### Status word

The status word is no longer fully supported in S7-1500. It contains less information and can now be evaluated only in STL. LAD and FBD no longer support the evaluation of the status word. The chapters below provide information on the migration of status word access in the individual programming languages.

---

**See also**

[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Migration of LAD/FBD programs to S7-1500 (S7-1500)](#migration-of-ladfbd-programs-to-s7-1500-s7-1500)
  
[Migration of STL programs to S7-1500 (S7-1500)](#migration-of-stl-programs-to-s7-1500-s7-1500)

#### Loading software changes to S7-1500 (S7-1500)

##### Downloading software changes

CPUs of the S7-1500 series behave differently than CPUs of the S7-300/400 series with regard to the downloading of software changes. For example, they allow changes to be downloaded in STOP and RUN without affecting the actual values of previously loaded tags.

### Migration of instructions to S7-1500 (S7-1500)

This section contains information on the following topics:

- [Information on migrating instructions (S7-1500)](#information-on-migrating-instructions-s7-1500)
- [Overview of non-migratable instructions (S7-1500)](#overview-of-non-migratable-instructions-s7-1500)
- [Migration of data block instructions (S7-1500)](#migration-of-data-block-instructions-s7-1500)
- [Migration of the instruction RDSYSST (S7-1500)](#migration-of-the-instruction-rdsysst-s7-1500)
- [Migration of the T_CONV instruction (S7-1500)](#migration-of-the-t_conv-instruction-s7-1500)
- [Migrating alarms with associated values (S7-1500)](#migrating-alarms-with-associated-values-s7-1500)
- [Migration of table instructions (S7-1500)](#migration-of-table-instructions-s7-1500)
- [Migration of communication instructions (S7-1500)](#migration-of-communication-instructions-s7-1500)

#### Information on migrating instructions (S7-1500)

##### Automatic migration of instructions

During migration, the instructions used in the initial program are carried over to the new program as much as possible. In the process, necessary adaptations are made automatically whenever possible without altering the semantics of the initial program. If multiple versions of an instruction exist, the migration always uses the newest instruction version.

Instructions that are not available in S7-1500 are replaced automatically whenever possible by a compatible or similar instruction.

##### Migration scenarios

The following table shows the possible scenarios for migrating instructions:

| Class | Scenario | System reaction | Manual adaptation of the program |
| --- | --- | --- | --- |
| 1 | The instruction is identical in both CPU families. | The instruction is migrated. | No adaptation is required. The semantics of the migrated program is unchanged and can be compiled. |
| 2 | The instruction is no longer available in S7-1500, but there is a compatible, new instruction. | The instruction is replaced by the new instruction. Additional instructions that are necessary to preserve the semantics of the initial program may be inserted. The migration log reports the replacement. | No adaptation is required. The semantics of the migrated program is unchanged and can be compiled. |
| 3 | The instruction is no longer available in S7-1500, but there is a similar instruction. | The instruction is replaced by the similar instruction. The migration log reports the replacement. Locations to be checked are marked in the program. You receive information regarding necessary adaptations in the form of a comment at the appropriate location in the program or when compiling. | You must check the program and possibly adapt it. |
| 4 | The instruction is no longer available in S7-1500 and there is no similar instruction. | The instruction is highlighted in red. The program cannot be compiled. | You must check the program and possibly adapt it. |

##### Information regarding instructions of migration class 3

Some instructions that were available in S7-300/400 are no longer offered in S7-1500 because there are now easier or more efficient methods available for solving certain tasks. The PLC migration supports you during the migration by replacing these instructions with appropriate new instructions. However, the instructions from scenario 3 cannot be completely migrated automatically. For example, new formal parameters may need to be added. The locations that cannot be migrated automatically are marked in the program. You receive information regarding necessary adaptations in the form of a comment directly at the appropriate location in the program, in the migration log, or when compiling.

The following manual adaptations may be necessary:

- If the new instruction has additional formal parameters, assign these parameters with suitable actual parameters.
- If the new instruction has modified parameter names, change the parameter assignment.
- If the migration cannot unequivocally ensure that the parameter assignment is semantically identical to the reference program, the actual parameters to be checked are marked. Check the semantics at these locations in the program after migration and correct it if necessary.
- If the reference program contains hardware identifiers, for example at the "LADDR" parameter, these are also marked. Enter the new HW identifier at the "LADDR" parameter.
- If the new instruction has modified error codes, adapt the error handling in the program.

Some examples of instructions of migration class 3 can be found in the chapter "[Migration of data block instructions](#migration-of-data-block-instructions-s7-1500)".

##### Information regarding instructions of migration class 4

Some instructions are no longer offered in S7-1500 because the functionality has fundamentally changed. These instructions are not replaced by the migration. They are shown in red in the program and prevent the program from being compiled. You receive information regarding necessary adaptations in the form of a comment directly at the appropriate location in the program, in the migration log, or when compiling.

In the following chapters, you can find an overview of the non-migratable instructions of migration class 4 as well as information on alternative solutions.

> **Note**
>
> **Further support**
>
> You can find the latest information about PLC migration in the Siemens Industry Online Support:
>
> Migration of controllers:
>
> <http://support.automation.siemens.com/WW/view/en/83557459>
>
> If you need further assistance for PLC migration, please contact SIMATIC Customer Support.

---

**See also**

[FAQs on migration](http://support.automation.siemens.com/WW/view/en/67858106)

#### Overview of non-migratable instructions (S7-1500)

##### Introduction

Some instructions from S7-300/400 cannot be migrated to S7-1500. This is the case, for example, when the instructions can be used only in connection with certain modules or when the functionality of the instruction in S7-1500 needs to be implemented differently.

##### Information on replacing non-migratable instruction (Class 4)

The following are examples of instructions that cannot be migrated and information on their replacement:

| Instruction group | Instruction which cannot be migrated | Notes |
| --- | --- | --- |
| Other instructions | SETP | Check whether the instruction in your program can be replaced by the "SET_BF" instruction. |
| RESETP | Check whether the instruction in your program can be replaced by the "RESET_BF" instruction. |  |
| DRUM_X | Check whether the instruction in your program can be replaced by the "DRUM" instruction. |  |
| TONR_X | Check whether the instruction in your program can be replaced by the "TONR" instruction. |  |
| RESET | Check whether the instruction in your program can be replaced by the "RESET_BF" instruction. |  |
| SET | Check whether the instruction in your program can be replaced by the "SET_BF" instruction. |  |
| WSR | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| SHRB | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| RESETI | Check whether the instruction in your program can be replaced by the "RESET_BF" instruction. |  |
| SETI | Check whether the instruction in your program can be replaced by the "SET_BF" instruction. |  |
| Runtime control | COMPRESS | Delete the instruction. In S7-1500, it is no longer necessary to compress the work memory of the CPU or the load memory. |
| PROTECT | Configure the protection level and password via the front panel of the S7-1500 CPU or in the module properties of the CPU. |  |
| CIR | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| Date and time | SET_CLKS | Check whether the instruction in your program can be replaced by the "WR_SYS_T" instruction. |
| LOC_TIME | Check whether the instruction in your program can be replaced by the "RD_SYS_T" instruction. |  |
| BT_LT | Check whether the instruction in your program can be replaced by the "RD_SYS_T" instruction. |  |
| LT_BT | Check whether the instruction in your program can be replaced by the "RD_SYS_T" instruction. |  |
| S_LTINT | Check whether the instruction in your program can be replaced by the "SET_TINTL" instruction. |  |
| SET_SW | Check whether the instruction in your program can be replaced by the "WR_SYS_T" or "RD_SYS_T" instruction. |  |
| SET_SW_S | Check whether the instruction in your program can be replaced by the "WR_SYS_T" or "RD_SYS_T" instruction. |  |
| TIMESTMP | Check whether the instruction in your program can be replaced by the "WR_SYS_T" or "RD_SYS_T" instruction. |  |
| WS_RULES | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| Distributed I/O | D_PRAL | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |
| ASi_3422 | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| SALRM | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| Module parameter assignment | PARM_MOD | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |
| Interrupts | MP_ALM | Multicomputing is not available on S7-1500. |
| REPL_VAL | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| Alarms | EN_MSG | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |
| DIS_MSG | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| ALARM_SQ | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| ALARM_S | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| ALARM_SC | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| WR_USMSG | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| READ_SI | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| DEL_SI | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |  |
| ALARM_DQ | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| ALARM_D | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| NOTIFY_8P | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| ALARM | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| ALARM_8 | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| ALARM_8P | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| NOTIFY | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| AR_SEND | Check whether the instruction in your program can be replaced by the "Program_Alarm" instruction.  You can find additional information in the chapter "[Migrating alarms with associated values](#migrating-alarms-with-associated-values-s7-1500)" and from SIMATIC Customer Support. |  |
| Diagnostics | RDSYSST | The instruction "RDSYSST: Read system status list" is no longer available in S7-1500 as the CPUs of this product series do not provide system status lists. However, you can read some of the information using the "GET_DIAG", "Geo2Log", "DeviceStates", or "ModuleStates" instruction. You can find additional information in the chapter "[Migration of the instruction RDSYSST](#migration-of-the-instruction-rdsysst-s7-1500)" and from SIMATIC Customer Support. |
| OB_RT | Check whether the instruction in your program can be replaced by the "RD_SYS_T" instruction. |  |
| Table functions | ATT | The instructions cannot be replaced. If you need the instructions in your program, you have to implement them yourself. For additional support, refer to the chapter "[Migration of table instructions](#migration-of-table-instructions-s7-1500)" and to SIMATIC Customer Support. |
| FIFO |  |  |
| TBL_FIND |  |  |
| LIFO |  |  |
| TBL |  |  |
| TBL_WRD |  |  |
| WRD_TBL |  |  |
| DEV |  |  |
| CDT |  |  |
| TBL_TBL |  |  |
| PACK |  |  |
| Addressing | LGC_GADR | The instructions cannot be used for the modules behind gateways (for example, IE/PB link). Instead, use the instructions "GEO2LOG" and "LOG2GEO".  The "LGC_GADR" and "GADR_LGC" instructions continue to work for modules that are not connected through gateways (for example, IE/PB link) to the CPU. |
| GADR_LGC |  |  |
| iSlave | SET_ADDR | The instruction cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |
| PID Control | TUN_EC | Check whether the instructions in your program can be replaced by the "PID_Compact" or "PID_3Step" technology objects. |
| TUN_ES |  |  |
| Function modules | CNT_CTRL | Check whether the instructions in your program can be replaced by the "High_Speed_Counter" technology object in conjunction with the "S7-1500 TM Count 2x24V" or "TM PosInput 2" counter module.  Alternatively, check whether the required functionality can be implemented with the "ET 200S 1Count24V" or "1Count5V" module. |
| DIAG_INF |  |  |
| CNT_CTL1 |  |  |
| CNT_CTL2 |  |  |
| CNT2WRPN |  |  |
| CNT2RDPN |  |  |
| CNT2_CTR |  |  |
| DIAG_RD |  |  |
| ABS_INIT | Check whether the functions can be implemented by "S7-1500 Motion" or "ET 200S 1PosU".  Check whether the functions can be implemented using the "TM Count 2x24V" or "TM PosInput 2" modules. |  |
| ABS_CTRL |  |  |
| ABS_DIAG |  |  |
| CAM_INIT | Check whether the encoder acquisition is possible via the modules "S7-1500 TM Count 2x24V" or "TM PosInput 2" and the use of the two DQs for faster reactions. Additional DQs of standard DQs can be switched depending on the encoder value from the application program. |  |
| CAM_CTRL |  |  |
| CAM_DIAG |  |  |
| PID_FM | Check whether the instructions in your program can be replaced by the technology objects "PID_Compact", "PID_3Step" or PID basic functions. |  |
| FUZ_355 |  |  |
| FORCE355 |  |  |
| READ_355 |  |  |
| CH_DIAG |  |  |
| PID_PAR |  |  |
| CJ_T_PAR |  |  |
| FMT_PID |  |  |
| FMT_PAR |  |  |
| FMT_CJ_T |  |  |
| FMT_DS1 |  |  |
| FMT_TUN |  |  |
| FMT_PV |  |  |
| 300C functions | ANALOG_300C | Check whether the instructions in your program can be replaced by the instructions from the "Motion Control" group. |
| DIGITAL_300C |  |  |
| COUNT_300C | Check whether the instructions in your program can be replaced by the "High_Speed_Counter" technology object in connection with counter modules. |  |
| FREQUENC_300C |  |  |
| PULSE_300C | Check whether the instruction in your program can be replaced by the "CTRL_PWM" instruction. |  |
| SEND_RK_300C | The communication instructions of the S7-1500 do not support RK 512. If you need RK functionality, you must implement it yourself. |  |
| FETCH_RK_300C |  |  |
| SERVE_RK_300C |  |  |
| Communication with iSlave/iDevice | I_GET | The instructions cannot be replaced. For more assistance, please contact SIMATIC Customer Support. |
| I_PUT |  |  |
| I_ABORT |  |  |
| S7 communication | PRINT | Check whether the instructions in your program can be replaced by the instructions of S7 communication for S7-1500. The "CONTROL" and "C_CNTRL" instructions, for example, can be replaced by the "T_DIAG" instruction. |
| START |  |  |
| STOP |  |  |
| RESUME |  |  |
| STATUS |  |  |
| USTATUS |  |  |
| CONTROL |  |  |
| C_CNTRL |  |  |
| Open user communication | TCON_PAR | These instructions are not required for the Open User Communication in S7-1500. The connection parameters are set in the block properties. |
| TADDR_PAR |  |  |
| TCP_conn_active |  |  |
| TCP_conn_passive |  |  |
| ISOonTCP_conn_active |  |  |
| SOonTCP_conn_passive |  |  |
| ISOonTCP_conn_CP_active |  |  |
| ISOonTCP_conn_CP_passive |  |  |
| UDP_local_open |  |  |
| UDP_rem_address_and_port |  |  |
| Communications processor | Instructions of the SIMATIC NET CPs group  Instructions of the PTP CP 340, PTP CP341, PTP CP 440, PTP CP 441 groups | You can find more detailed information on these instructions in the chapter "[Migration of communication instructions](#migration-of-communication-instructions-s7-1500)". |
| PROFINET / CBA | PN_IN | PROFINET/CBA communication is not supported by S7-1500. Use S7 communication or open user communication. |
| PN_OUT |  |  |
| PN_DP |  |  |
| MPI communication | X_SEND | MPI communication is not supported by S7-1500.   Use S7 communication or open user communication. |
| X_RCV |  |  |
| X_GET |  |  |
| X_PUT |  |  |
| X_ABORT |  |  |
| Global data communications | GD_SND | Global data communications is not supported by S7-1500.   Use S7 communication or open user communication. |
| GD_RCV |  |  |
| Point-to-point communication | P_PRINT | The print function is not supported by the point-to-point communication modules. |
| P_PRINT341 | The print function is not supported by the point-to-point communication modules. |  |
| MODB_341 | These blocks for CP 341/CP 441 are not supported by S7-1500. Use the instructions for Modbus (RTU) instead.  - Modbus_Comm_Load - Modbus_Master - Modbus_Slave   In connection with the S7-1500 point-to-point modules   - CM PtP RS232 HF - CM PtP RS422/485 HF   You can find more detailed information on these instructions in the chapter "[Migrating point-to-point program blocks](#migrating-point-to-point-program-blocks-s7-1500)". |  |
| MODB_441 |  |  |
| S_MODB | These instructions for ET 200S 1SI are not supported by S7-1500. Instead, use the instructions for Modbus (RTU) or for USS in connection with the point-to-point module "ET 200SP CM PtP".  You can find more detailed information on these instructions in the chapter "[Migrating point-to-point program blocks](#migrating-point-to-point-program-blocks-s7-1500)". |  |
| S_USST |  |  |
| S_USSR |  |  |
| S_USSI |  |  |
| Teleservice | PG_DIAL | The MPI interface is not supported by S7-1500 as the default interface. The instruction is no longer available. |
| AS_DIAL | The MPI interface is not supported by S7-1500 as the default interface. The instruction is no longer available. |  |
| SMS_SEND | The MPI interface is not supported by S7-1500 as the default interface. Check whether the instruction in your program can be replaced by the "TMAIL_C" instruction. |  |
| AS_MAIL | The MPI interface is not supported by S7-1500 as the default interface. Check whether the instruction in your program can be replaced by the "TMAIL_C" instruction. |  |
| User library | PNIO_DIAG | The "PNIO_DIAG" instruction could be downloaded to a user library for S7-300/400 and used for diagnostic purposes. "PNIO_DIAG" has been replaced in S7-1500 by integrated diagnostics and is thus no longer needed.   In S7-1500, the system diagnostics is enabled by default. You can use the system diagnostics without making any additional settings. If required, you can edit the settings for the system diagnostics in the device configuration of the S7-1500 on the "Properties > Diagnostics" tab. You can also configure the interrupts of the system diagnostics there. The interrupts are enabled by default.  Following the migration, you can delete the diagnostic screens used in conjunction with "PNIO_DIAG" and the associated tags in the HMI Panel. Use the "System diagnostics display" control in your diagnostic screens instead. |

> **Note**
>
> **Support for instructions that cannot be migrated**
>
> If you need further assistance for instructions that cannot be migrated, please contact SIMATIC Customer Support.
>
> You can find the latest information about PLC migration in the Siemens Industry Online Support:
>
> Migration of controllers:
>
> <http://support.automation.siemens.com/WW/view/en/83557459>

---

**See also**

[FAQs on migration](http://support.automation.siemens.com/WW/view/en/67858106)

#### Migration of data block instructions (S7-1500)

##### Procedure for migration of data block instructions (migration class 3)

S7-1500 provides a revised set of instructions of the "Data blocks" category. These instructions are replaced automatically during the migration. Afterwards you still have to make manual adaptations.

The table below provides an overview of the migration of data block instructions:

| Instruction in S7-300/400 | Instruction in S7-1500 | Migration class |
| --- | --- | --- |
| CREA_DBL | CREATE_DB | 3 |
| CREAT_DB | CREATE_DB | 3 |
| CREA_DB | CREATE_DB | 3 |
| DEL_DB | DELETE_DB | 3 |
| TEST_DB | ATTR_DB | 3 |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Asynchronous processing**  The new instructions work asynchronously in S7-1500, which means their execution is spread across several programming cycles. |  |

##### Manual adaptations after migration

The instructions have additional formal parameters in S7-1500 which are required for asynchronous execution, for example . You need to provide these additional parameters with appropriate actual parameters following migration.

The block number of the created DB must be between 60000 and 60999 in S7-1500. Therefore, adapt the "LOW_LIMIT" and "UP_LIMIT" parameters to the new number range.

You can find a detailed description of the parameters in the reference help for S7-1500.

See also:

[Data block functions](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#data-block-functions-s7-1200-s7-1500)

[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

##### Example

The following example shows the migration of the "CREAT_DB" instruction to the "CREATE_DB" instruction.

In the first figure, you can see the call for "CREAT_DB" before migration:

![Example](images/42478108171_DV_resource.Stream@PNG-de-DE.png)

In the second figure, you can see the call for "CREATE_DB" after migration:

![Example](images/46882311307_DV_resource.Stream@PNG-de-DE.png)

- The "REQ" parameter was not available for "CREAT_DB" and was amended by the migration. It gets the default value "TRUE".
- The "LOW_LIMIT" and "UP_LIMIT" parameters were outside the permitted number range of 60000 to 60999. The values "12" and "34" were therefore marked as invalid during the migration. The permitted values "60000" and "60100" were then entered manually.
- The "ATTRIB" parameter was not available for "CREAT_DB" and was amended by the migration. It gets the default value "0". You can specify the properties of the DB to be created at this parameter.
- The "SRCBLK" parameter was not available for "CREAT_DB" and was amended by the migration. Here you can specify the data area whose contents are to be written to the DB to be generated.
- The "BUSY" parameter was not available for "CREAT_DB" and was amended by the migration. The parameter retains the signal "1" until the process for generating the data block is complete. To evaluate the signal, you need to interconnect the output parameter with an operand.

#### Migration of the instruction RDSYSST (S7-1500)

##### Procedure for migration of RDSYSST (migration class 4)

The instruction "RDSYSST: Read system status list" is no longer available in S7-1500 as the CPUs of this product series do not provide system status lists. However, the option exists to use one of the following instructions to read out some of the information you received previously via the system status list:

- "[RDREC](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rdrec-read-data-record-s7-1200-s7-1500-1)" (Extended instructions > Distributed I/O)
- "[GET_DIAG](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#get_diag-read-diagnostic-information-s7-1200-s7-1500)" (Extended instructions > Diagnostics)
- "[GEO2LOG](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#geo2log-determine-hardware-identifier-from-slot-s7-1200-s7-1500)" (Extended instructions > Diagnostics)
- "[DeviceStates](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#devicestates-read-module-status-information-in-an-io-system-s7-1200-s7-1500)" (Extended instructions > Diagnostics)
- "[ModuleStates](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#modulestates-read-module-status-information-of-a-module-s7-1200-s7-1500)" (Extended instructions > Diagnostics)
- "[RALRM](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#description-ralrm-s7-1200-s7-1500)" (Extended instructions > Distributed I/O)
- "[LED](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#led-read-led-status-s7-1200-s7-1500)" (Extended instructions > Diagnostics)

##### Reading system status information in S7-1500

The following table shows which information about the system status can be read in S7-1500.

You will find the IDs that you have previously read with the RDSYSST instruction in the "SSL-ID" column. The two final digits are relevant. The "xy" placeholder varies depending on the module used.

The "Migration" column indicates whether the information is still available in S7-1500 and how you can read it out.

| Partial list | SZL-ID | Migration |
| --- | --- | --- |
| Module ID | W#16#xy11 | This information can be read with the "RDREC" instruction.   Read data record 16#AFF0 in the "INDEX" parameter. |
| CPU characteristics | W#16#xy12 | This information is not currently available in S7-1500. |
| User memory areas | W#16#xy13 | This information is not currently available in S7-1500. |
| System areas | W#16#xy14 | This information is not currently available in S7-1500. |
| Block types | W#16#xy15 | This information is not currently available in S7-1500. |
| Identification of one component | W#16#xy1C | This information can be read with the "RDREC" instruction for central modules and PROFINET IO.   Read data record 16#AFF0 in the "INDEX" parameter. |
| Interrupt status | W#16#xy22 | This information is not available in S7-1500. |
| Assignment of partial process images and OBs | W#16#xy25 | This information is not available in S7-1500. |
| Communication: Status data | W#16#xy32 | This information is not available in S7-1500. |
| H-CPU group information | W#16#xy71 | Not relevant |
| Status of the module LEDs | W#16#xy74 | This information can be read with the "LED" instruction.  Read data record W#16#xy74 in the "LED" parameter. |
| Switched DP slaves in the H-system | W#16#xy75 | Not relevant |
| DP master system information | W#16#xy90 | This information is not available in S7-1500. |
| Module status information | W#16#xy91 | This information can be read with the "GET_DIAG" or "ModuleStates" instruction. |
| Rack/station status information | W#16#xy92 | This information can be read with the "GET_DIAG" or "DeviceStates" instruction. |
| Rack/station status information | W#16#xy94 | This information can be read with the "GET_DIAG" or "DeviceStates" instruction. |
| Extended DP master system information | W#16#xy95 | This information is not available in S7-1500. |
| Module status information PROFINET IO and PROFIBUS DP | W#16#xy96 | This information can be read with the "GET_DIAG", "ModuleStates" or "DeviceStates" instruction. |
| Tool changer information (PROFINET IO) | W#16#xy9C | This information is not available in S7-1500. |
| Diagnostics buffer | W#16#xyA0 | This information is not available in S7-1500. |
| Module diagnostics information (data record 0) | W#16#00B1 | This information can be read with the "GET_DIAG" or "RDREC" instruction. Within the interrupt OB, you also get the diagnostics information using "RALRM". |
| Module diagnostics information (data record 1), physical address | W#16#00B2 | This information can be read with the "RDREC" or "GEO2LOG" instruction. Within the interrupt OB, you also get the diagnostics information using "RALRM". |
| Module diagnostics information (data record 1), logical address | W#16#00B3 | This information can be read with the "GET_DIAG" or "RDREC" instruction. Within the interrupt OB, you also get the diagnostics information using "RALRM". |
| Diagnostics data of a DP slave | W#16#00B4 | This information can partially be read with the "ModuleStates" or "GET_DIAG" instruction.  Within the interrupt OB, you also get the diagnostics information using "RALRM".  Some of the information is not available in S7-1500. |
|  |  |  |

> **Note**
>
> **Support on information that cannot be read**
>
> If you need further assistance on information that cannot be read, please contact SIMATIC Customer Support.
>
> You can find the latest information about PLC migration in the Siemens Industry Online Support:
>
> Migration of controllers:
>
> <http://support.automation.siemens.com/WW/view/en/83557459>

---

**See also**

[FAQs on migration](http://support.automation.siemens.com/WW/view/en/67858106)

#### Migration of the T_CONV instruction (S7-1500)

##### Extracting weekdays from DATE_AND_TIME with T_CONV

The "T_CONV" instruction is available both in S7-300/400 and in S7-1500. The instruction is migrated automatically in most cases. However, if you have used "T_CONV" to extract the weekday from the DATE_AND_TIME (DT) data type, you need to note the following in S7-1500:

In S7-300/400, an output parameter "OUT" of the data type INT was expected for the extraction of the weekday. In S7-1500, the output parameter must be of the data type DTL instead when you are expecting a weekday as a result.

If the output parameter "OUT" has a different data type, an error is output in the migration log during the PLC migration. In this case, convert the data type of the output parameter to DTL and use the component "Weekday".

For additional information, refer to "See also".

---

**See also**

[T_CONV: Convert times and extract (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#t_conv-convert-times-and-extract-s7-300-s7-400)
  
[DTL (S7-1200, S7-1500)](Data%20types.md#dtl-s7-1200-s7-1500)

#### Migrating alarms with associated values (S7-1500)

##### Alarm configuration with S7-1500

In S7-1500, you can carry out all functions for alarm configuration centrally with the instruction "Program_Alarm".

 "Program_Alarm" replaces the following instructions of S7-300/400:

| Instruction for alarm configuration (S7-300/400) | Instruction for alarm configuration (S7-1500) |
| --- | --- |
| ALARM_SQ | Program_Alarm (migration class 4) |
| ALARM_S |  |
| ALARM_SC |  |
| ALARM_DQ |  |
| ALARM_D |  |
| NOTIFY_8P |  |
| ALARM |  |
| ALARM_8 |  |
| ALARM_8P |  |
| NOTIFY |  |
| AR_SEND |  |

##### Procedure for the migration of alarms

Alarms are not migrated automatically. You need to manually reconfigure the alarms after migration.

Below, you will learn how to prepare your program in such a way that alarm texts are retained after migration and manual follow-up work is minimal.

The procedure only applies for alarm instructions that use the data types "C_Alarm_8", "C_Alarm_8p", "C_Alarm_t"; "C_Notify_8p" or "C_Ar_send".

To migrate alarms, follow these steps:

1. Open the block containing the alarm.

   The interface of the block contains a parameter that has an alarm data type (e.g. the data types "C_Alarm_s", " C_Notify", etc.). This parameter defines the alarm number input.
2. Move the parameter for the alarm number input to the "Static" section.

   ![Procedure for the migration of alarms](images/66231029003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for the migration of alarms](images/66231029003_DV_resource.Stream@PNG-en-US.png)
3. Save and compile the block.
4. You then perform the PLC migration.

   See also: [Performing migration](#performing-migration-s7-1500)
5. In the newly created CPU, open the block that contains the alarm again.

   The instruction for alarm configuration could not be migrated and is shown in red.
6. Replace the alarm data type (e.g., "C_Alarm_s") in the block interface with the new data type "Program_Alarm". If the data type "Program_Alarm" is not offered in the selection list, enter the name using the keyboard.
7. Open the "Instructions" task card and navigate to the "Alarms" folder in the "Extended instructions" pane.
8. Drag the "Program_Alarm" instruction to your network.
9. In the "Call options" dialog, select the previously re-configured alarm tag in the "Name in the interface" input field.
10. Open the tag properties and change to the "Alarm" tab.

    The alarm text from the output program is entered.
11. Delete the character for the element type from the associated values (e.g., Y, W, X, I, etc.). Associated values do not include information on the element type in S7-1500.

    See also: [Structure of associated values](Configuring%20alarms.md#structure-of-associated-values-s7-300-s7-400)
12. Delete the old alarm block from the network.

    The alarm configuration was migrated. The alarm text has been taken from the output program.

    ![Procedure for the migration of alarms](images/67086914571_DV_resource.Stream@PNG-en-US.png)

    ![Procedure for the migration of alarms](images/67086914571_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Program_Alarm: Generate program alarm with associated values (S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#program_alarm-generate-program-alarm-with-associated-values-s7-1500)

#### Migration of table instructions (S7-1500)

This section contains information on the following topics:

- [Example for migration of "ATT: Add value to table" (S7-1500)](#example-for-migration-of-att-add-value-to-table-s7-1500)
- [Example for migration of "FIFO: Output first value of the table" (S7-1500)](#example-for-migration-of-fifo-output-first-value-of-the-table-s7-1500)
- [Example for migration of "LIFO: Output last value in the table" (S7-1500)](#example-for-migration-of-lifo-output-last-value-in-the-table-s7-1500)

##### Example for migration of "ATT: Add value to table" (S7-1500)

###### Procedure for migration of table instructions (migration class 4)

The instructions from the "Table instructions" group are no longer available in S7-1500 and cannot be replaced during the migration because they are based on pure absolute addressing. However, S7-1500 provides convenient functions that allow you to implement the instructions yourself. Below is an example for the implementation of the instruction "ATT": Add value to table".

###### Implementation

The following SCL program shows how to implement the "ATT" instruction. The function in this example has been implemented as an FC in SCL.

The following table shows the declaration of the tags used:

| Operand |  | Declaration | Data type | Description |
| --- | --- | --- | --- | --- |
| val |  | Input | INT | Entered value |
| tab |  | InOut | PLC data type "Table10" | Table with 10 rows |
|  | x | InOut | ARRAY[0..9] of INT | Each ARRAY element represents a row. An ARRAY of INT is used in the example. However, you can create ARRAYs with any data type. An ARRAY of STRUCT or an ARRAY of a PLC data type is also possible. |
|  | lng | InOut | INT | Length of the buffer. The value depends on the number of ARRAY elements of "tab.x". |
|  | first | InOut | INT | First written value |
|  | last | InOut | INT | Last written value |
| h |  | Temp | INT | Auxiliary tag |
| Ret_Val |  |  | BOOL | Function value |

The following table shows the FC "Attend":

The function writes the value of the input parameter "#val" to the last row of the table.

| SCL |  |
| --- | --- |
| #h:=(#tab.last+1) MOD #tab.lng; // increment index  IF #h <> #tab.first THEN ​ // Scan to see if indices are overtaking each other   #tab.x[#tab.last] := #val; //  Write value   #tab.last := #h; ​ // Save index of the next free element   #Attend:= false;  ELSE   #Attend:= true; // Error >> The table is full; the value cannot be entered  END_IF; |  |

##### Example for migration of "FIFO: Output first value of the table" (S7-1500)

###### Procedure for migration of table instructions (migration class 4)

The instructions from the "Table instructions" group are no longer available in S7-1500 and cannot be replaced during the migration because they are based on pure absolute addressing. However, S7-1500 provides convenient functions that allow you to implement the instructions yourself. Below is an example for the implementation of the instruction "FIFO": Output first value of the table".

###### Implementation

The following SCL program shows how to implement the "FIFO" table function. The function in this example has been implemented as an FC in SCL.

The following table shows the declaration of the tags used:

| Operand |  | Declaration | Data type | Description |
| --- | --- | --- | --- | --- |
| val |  | Output | INT | Value returned |
| tab |  | InOut | PLC data type "Table10" | Table with 10 rows |
|  | x | InOut | ARRAY of INT [0..9] | Each ARRAY element represents a row. An ARRAY of INT is used in the example. However, you can create ARRAYs with any data type. An ARRAY of STRUCT or an ARRAY of a PLC data type is also possible. |
|  | lng | InOut | INT | Length of the buffer. The value depends on the number of ARRAY elements of "tab.x". |
|  | first | InOut | INT | First written value |
|  | last | InOut | INT | Last written value |
| h |  | Temp | INT | Auxiliary tag |
| Ret_Val |  |  | BOOL | Function value |

The following table shows the FC "Fifo":

The function returns the first value written to the table (first in, first out). The function value "true" indicates that the table is empty.

| SCL |  |
| --- | --- |
| #h:=(#tab.first+1) MOD #tab.lng; // increment index   IF #h <> #tab.last THEN ​ // Scan to see if indices are overtaking each other   #tab.first := #h; ·​ // Save index of the next value   #val := #tab.x[#h]; //  Output desired value   #Fifo:= false;   ELSE   #Fifo:= true; // Error >> The table is empty; no value is output   #val := #tab.x[#tab.first]; //  Output last valid value   END_IF; |  |

##### Example for migration of "LIFO: Output last value in the table" (S7-1500)

###### Procedure for migration of table instructions (migration class 4)

The instructions from the "Table instructions" group are no longer available in S7-1500 and cannot be replaced during the migration because they are based on pure absolute addressing. However, S7-1500 provides convenient functions that allow you to implement the instructions yourself. Below is an example for the implementation of the instruction "LIFO": Output last value in the table".

###### Implementation

The following SCL program shows how to implement the "LIFO" table function. The function in this example has been implemented as an FC in SCL.

The following table shows the declaration of the tags used:

| Operand |  | Declaration | Data type | Description |
| --- | --- | --- | --- | --- |
| val |  | Output | INT | Value returned |
| tab |  | InOut | PLC data type "Table10" | Table with 10 rows |
|  | x | InOut | ARRAY of INT [0..9] | Each ARRAY element represents a row. An ARRAY of INT is used in the example. However, you can create ARRAYs with any data type. An ARRAY of STRUCT or an ARRAY of a PLC data type is also possible. |
|  | lng | InOut | INT | Length of the buffer. The value depends on the number of ARRAY elements of "tab.x". |
|  | first | InOut | INT | First written value |
|  | last | InOut | INT | Last written value |
| h |  | Temp | INT | Auxiliary tag |
| Ret_Val |  |  | BOOL | Function value |

The following table shows the FC "Lifo":

The function returns the last value written in the table (last in, first out). The function value "true" indicates that the table is empty.

| SCL |  |
| --- | --- |
| #h:=(#tab.last-1) MOD #tab.lng; // decrement index   IF #h<0 THEN #h:=#h + #tab.lng; END_IF; // allow only positive indices   IF #h <> #tab.first THEN ​ // Scan to see if indices are overtaking each other   #tab.last := #h; ​ // Save index of the next value   #val := #tab.x[#h]; //  Output desired value   #Lifo:= false;   ELSE   #Lifo:= true; // Error >> The table is empty; no value is output   #val := #tab.x[#tab.last]; //  Output last valid value   END_IF; |  |

#### Migration of communication instructions (S7-1500)

This section contains information on the following topics:

- [SIMATIC NET CP/CM (S7-1500)](#simatic-net-cpcm-s7-1500)
- [Point-to-point CP/CM (S7-1500)](#point-to-point-cpcm-s7-1500)

##### SIMATIC NET CP/CM (S7-1500)

This section contains information on the following topics:

- [Migrating program blocks (S7-1500)](#migrating-program-blocks-s7-1500)
- [Migration AG_SEND/AG_LSEND (S7-1500)](#migration-ag_sendag_lsend-s7-1500)
- [Migration AG_RECV/AG_LRECV (S7-1500)](#migration-ag_recvag_lrecv-s7-1500)

###### Migrating program blocks (S7-1500)

###### Introduction

S7-300/400 uses specific program blocks for communication functions via SIMATIC NET CPs. S7-1500 provides a revised set of instructions for these communication functions.

The following tables provide an overview of the migration of the program blocks used in S7-300/400.

You can find more detailed information about the specification in the "Class" column in chapter [Information on migrating instructions](#information-on-migrating-instructions-s7-1500).

###### Program blocks for industrial Ethernet / PROFINET

| Communication service / functional area | Type of instruction | Library |  | Instruction in S7‑1500 | Class |
| --- | --- | --- | --- | --- | --- |
| CP 300 | CP 400 |  |  |  |  |
| SEND / RECEIVE   (Open communication services) | AG_SEND   [Migration AG_SEND/AG_LSEND](#migration-ag_sendag_lsend-s7-1500) | x | x | T_SEND | 3 |
| AG_LSEND    [Migration AG_SEND/AG_LSEND](#migration-ag_sendag_lsend-s7-1500) | x | x | T_SEND | 3 |  |
| AG_SEND (via UDP)   [Migration AG_SEND/AG_LSEND](#migration-ag_sendag_lsend-s7-1500) | x | x | TUSEND | 3 |  |
| AG_SEND (e-mail)   [Migration AG_SEND/AG_LSEND](#migration-ag_sendag_lsend-s7-1500) | x | x | TMAIL_C | 3 |  |
| AG_RECV   [Migration AG_RECV/AG_LRECV](#migration-ag_recvag_lrecv-s7-1500) | x | x | T_RCV | 3 |  |
| AG_LRECV   [Migration AG_RECV/AG_LRECV](#migration-ag_recvag_lrecv-s7-1500) | x | x | T_RCV | 3 |  |
| AG_LOCK | x | x | - | 4 |  |
| AG_UNLOCK | x | x | - | 4 |  |
| AG_CNTRL | x | x | T_DIAG, T_RESET, TCON, TDISCON | 3 |  |
| Programmed communication connections | IP_CONFIG | x | x | T_CONFIG | 3 |
| FTP | FTP_CMD | x | x | FTP_CMD | 3 |
| PROFINET IO | PNIO_SEND | x | - | - | 4 <sup>*)</sup> |
| PNIO_RECV | x | - | - | 4 <sup>*)</sup> |  |
| PNIO_RW_REC | x | - | - | 4 <sup>*)</sup> |  |
| PNIO_ALARM | x | - | - | 4 <sup>*)</sup> |  |
| <sup>*) </sup>Other access mechanisms should be used. |  |  |  |  |  |

###### Program blocks for PROFIBUS

| Communication service / functional area | Type of instruction | Library |  | Instruction in S7-1500 | Case |
| --- | --- | --- | --- | --- | --- |
| CP 300 | CP 400 |  |  |  |  |
| SEND / RECEIVE   (Open communication services) | AG_SEND   [Migration AG_SEND/AG_LSEND](#migration-ag_sendag_lsend-s7-1500) | x | x | T_SEND | 3 |
| AG_LSEND   [Migration AG_SEND/AG_LSEND](#migration-ag_sendag_lsend-s7-1500) | - | x | T_SEND | 3 |  |
| AG_RECV   [Migration AG_RECV/AG_LRECV](#migration-ag_recvag_lrecv-s7-1500) | x | x | T_RCV | 3 |  |
| AG_LRECV   [Migration AG_RECV/AG_LRECV](#migration-ag_recvag_lrecv-s7-1500) | - | x | T_RCV | 3 |  |
| PROFIBUS DP | DP_SEND | x | - | - | 4 <sup>*)</sup> |
| DP_RECV | x | - | - | 4 <sup>*)</sup> |  |
| DP_DIAG | x | - | - | 4 <sup>*)</sup> |  |
| DP_CTRL | x | - | - | 4 <sup>*)</sup> |  |
| <sup>*) </sup>Other access mechanisms should be used. |  |  |  |  |  |

###### Additional formal parameters

The instructions have additional formal parameters in S7-1500 which are required for asynchronous execution, for example . You need to provide these additional parameters with appropriate actual parameters following migration.

You can find a detailed description of the parameters in the reference help for S7-1500.

See also:

[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

###### Example

You can find a basic example of the representation of a migrated instruction in the chapter [Migration of data block instructions](#migration-of-data-block-instructions-s7-1500)

###### Migration AG_SEND/AG_LSEND (S7-1500)

###### Migration of the call parameters - communication via ISO Transport, ISO-on-TCP, TCP

Migration AG_SEND/AG_LSEND

| AG_SEND / AG_LSEND |  | T_SEND |  | Description / notes |
| --- | --- | --- | --- | --- |
| Parameter | Type | Parameter | Type |  |
| ACT | BOOL | REQ | BOOL |  |
| ID | INT | ID | CONN_OUC (WORD) |  |
| LADDR | WORD | -- | -- |  |
| SEND | ANY | DATA | VARIANT |  |
| -- | -- | ADDR | VARIANT |  |
| LEN | INT | LEN | UINT |  |
| DONE | BOOL | DONE | BOOL |  |
| -- | -- | BUSY | BOOL |  |
| ERROR | BOOL | ERROR | BOOL |  |
| STATUS | WORD | STATUS | WORD |  |
|  |  |  |  |  |

###### Additional steps

- Configure the corresponding connection type with the relevant address parameters.

###### Migration of the call parameters - communication via UDP

Migration AG_SEND/AG_LSEND

| AG_SEND / AG_LSEND |  | TUSEND |  | Description / notes |
| --- | --- | --- | --- | --- |
| Parameter | Type | Parameter | Type |  |
| ACT | BOOL | REQ | BOOL |  |
| ID | INT | ID | CONN_OUC (WORD) |  |
| LADDR | WORD | -- | -- |  |
| SEND | ANY | DATA | VARIANT |  |
| -- | -- | ADDR | VARIANT |  |
| LEN | INT | LEN | UINT |  |
| DONE | BOOL | DONE | BOOL |  |
| -- | -- | BUSY | BOOL |  |
| ERROR | BOOL | ERROR | BOOL |  |
| STATUS | WORD | STATUS | WORD |  |
|  |  |  |  |  |

###### Additional steps

- Configure the corresponding connection type with the relevant address parameters.

###### Migration of the call parameters - communication via E-MAIL

Migration AG_SEND/AG_LSEND

| AG_SEND / AG_LSEND |  | TMAIL_C |  | Description / notes |
| --- | --- | --- | --- | --- |
| Parameter | Type | Parameter | Type |  |
| ACT | BOOL | REQ | BOOL |  |
| ID | INT | -- | -- |  |
| LADDR | WORD | -- | -- |  |
| SEND | ANY | TO_S | STRING |  |
| SEND | ANY | CC | STRING |  |
| SEND | ANY | SUBJECT | STRING |  |
| SEND | ANY | TEXT | STRING |  |
| SEND | ANY | ATTACHMENT | VARIANT |  |
| -- | -- | ATTACHMENT _NAME | STRING |  |
| -- | -- | MAIL_ADDR_PARAM | VARIANT |  |
| LEN | INT | -- | -- |  |
| DONE | BOOL | DONE | BOOL |  |
| -- | -- | BUSY | BOOL |  |
| ERROR | BOOL | ERROR | BOOL |  |
| STATUS | WORD | STATUS | WORD |  |
|  |  |  |  |  |

###### Additional steps

- Configure the corresponding connection type with the relevant address parameters.

###### Migration AG_RECV/AG_LRECV (S7-1500)

###### Migration of call parameters

Migration AG_RECV/AG_LRECV

| AG_RECV / AG_LRECV |  | TRCV / TURCV |  | Description / notes |
| --- | --- | --- | --- | --- |
| Parameter | Type | Parameter | Type |  |
|  |  | EN_R | BOOL |  |
| ID | INT | ID | CONN_OUC (WORD) |  |
| LADDR | WORD | -- | -- |  |
| -- | -- | LEN | UDINT |  |
| RECV | ANY | DATA | VARIANT |  |
| -- | -- | ADDR | VARIANT |  |
| LEN | INT | LEN | UINT |  |
| NDR | BOOL | NDR | BOOL |  |
| -- | -- | BUSY | BOOL |  |
| ERROR | BOOL | ERROR | BOOL |  |
| STATUS | WORD | STATUS | WORD |  |
|  |  |  |  |  |

###### Additional steps

- Configure the corresponding connection type with the relevant address parameters.

##### Point-to-point CP/CM (S7-1500)

This section contains information on the following topics:

- [Migrating point-to-point program blocks (S7-1500)](#migrating-point-to-point-program-blocks-s7-1500)

###### Migrating point-to-point program blocks (S7-1500)

###### Introduction

S7-300/400 uses specific program blocks for communication functions via point-to-point CPs.

S7-1500 provides a revised set of instructions for these communication functions.

During migration, you are asked whether you want to use the revised set of instructions for the communication modules of the S7‑1500 or the program blocks for the communication processors of the S7‑300/400.

The table below provides an overview of the migration of the program blocks used in S7-300/400 on instructions of the S7-1500.

You can find more detailed information about the specification in the "Class" column in chapter [Information on migrating instructions](#information-on-migrating-instructions-s7-1500).

###### Program blocks for point-to-point communication

| Communication service / functional area | Block | Library |  |  | Instruction in  S7‑1500 | Class |
| --- | --- | --- | --- | --- | --- | --- |
| CP 300 | CP 400 | ET 200S |  |  |  |  |
| Blocks for CP 340 | P_RCV | x | - | - | Receive_P2P | 3 <sup>1)</sup> |
| P_SEND | x | - | - | Send_P2P | 3 <sup>1)</sup> |  |
| P_RESET | x | - | - | Receive_Reset | 3 <sup>1)</sup> |  |
| V24_STAT_340 | x | - | - | Signal_Get | 3 <sup>1)</sup> |  |
| V24_SET_340 | x | - | - | Signal_Set | 3 <sup>1)</sup> |  |
| P_PRINT | x | - | - | - | 4 |  |
| Blocks for CP 341 | P_RCV_RK | x | - | - | Receive_P2P | 3 <sup>1)</sup> |
| P_SND_RK | x | - | - | Send_P2P | 3 <sup>1)</sup> |  |
| V24_STAT | x | - | - | Signal_Get | 3 <sup>1)</sup> |  |
| V24_SET | x | - | - | Signal_Set | 3 <sup>1)</sup> |  |
| P-PRT341 | x | - | - | - | 4 |  |
| Blocks for CP 440 | RECV_440 | - | x | - | Receive_P2P | 3 <sup>1)</sup> |
| SEND_440 | - | x | - | Send_P2P | 3 <sup>1)</sup> |  |
| RES_RECV | - | x | - | Receive_Reset | 3 <sup>1)</sup> |  |
| Blocks for CP 441 | V24_STAT_441 | - | x | - | Signal_Get | 3 <sup>1)</sup> |
| V24_SET_441 | - | x | - | Signal_Set | 3 <sup>1)</sup> |  |
| Blocks for Modbus | MODB_341 | x | - | - | - | 4 <sup>2)</sup> |
| MODB_441 | - | x | - | - | 4 <sup>2)</sup> |  |
| Blocks for ET 200S 1SI | S_RCV | - | - | x | Receive_P2P | 3 <sup>1)</sup> |
| S_SEND | - | - | x | Send_P2P | 3 <sup>1)</sup> |  |
| S_VSTAT | - | - | x | Signal_Get | 3 <sup>1)</sup> |  |
| S_VSET | - | - | x | Signal_Set | 3 <sup>1)</sup> |  |
| S_XON | - | - | x | Port_Config | 3 <sup>1)</sup> |  |
| S_RTS | - | - | x | Port_Config | 3 <sup>1)</sup> |  |
| S_V24 | - | - | x | Send_Config | 3 <sup>1)</sup> |  |
| S_MODB | - | - | x | - | 4 <sup>2)</sup> |  |
| S_USST | - | - | x | - | 4 <sup>2)</sup> |  |
| S_USSR | - | - | x | - | 4 <sup>2)</sup> |  |
| S_USSI | - | - | x | - | 4 <sup>2)</sup> |  |
| Blocks for compact CPUs S7-300 | SEND_PTP | x | - | - | Send_P2P | 3 <sup>1)</sup> |
| RCV_PTP | x | - | - | Receive_P2P | 3 <sup>1)</sup> |  |
| RES_RCVB | x | - | - | Receive_Reset | 3 <sup>1)</sup> |  |

<sup>1)</sup> You can find information on migrating this instruction at this [link](#information-on-migrating-instructions-s7-1500).

<sup>2)</sup> These instructions for ET 200S 1SI are not supported by S7-1500. Instead, use the instructions for Modbus (RTU) or for USS in connection with the point-to-point module "ET 200SP CM PtP".

###### Additional formal parameters

The instructions have additional formal parameters in S7-1500. You need to provide these additional parameters with appropriate actual parameters following migration.

> **Note**
>
> **Additional support for migration of communication instructions**
>
> You can find the latest information about migrating communication instructions in the Siemens Industry Online Support.
>
> Migration of communication:
>
> <http://support.automation.siemens.com/WW/view/en/83558087>
>
> Migration of controllers:
>
> <http://support.automation.siemens.com/WW/view/en/83557459>
>
> If you need further support, please contact SIMATIC Customer Support.

---

**See also**

[FAQs on migration](http://support.automation.siemens.com/WW/view/en/67858106)

### Migration of LAD/FBD programs to S7-1500 (S7-1500)

This section contains information on the following topics:

- [Information on migrating LAD/FBD programs (S7-1500)](#information-on-migrating-ladfbd-programs-s7-1500)
- [Partially qualified addresses in LAD/FBD (S7-1500)](#partially-qualified-addresses-in-ladfbd-s7-1500)
- [Access to status bits in LAD/FBD (S7-1500)](#access-to-status-bits-in-ladfbd-s7-1500)

#### Information on migrating LAD/FBD programs (S7-1500)

##### ---(SAVE): Save RLO to BR memory

The instruction is not available in S7-1500. Migration handles the instruction as follows:

- If the "---(SAVE)" instruction was used in the last network of a block, it is replaced by the "---(RET)" instruction with the parameter "RLO".
- If the "---(SAVE)" instruction was used in a network that is not the last network of the block, it cannot be replaced. Change the program manually. For example, save the RLO in a PLC tag, a DB tag or a local tag and return it to the calling block at the end of the block with the --(RET) instruction.

##### ---(CALL) Call block without parameters

The instruction is not available in S7-1500. Migration adapts the program so that the call is implemented via a box.

##### Master control relay

The master control relay is not available on S7-1500. Migration reports an error. Change the program manually. Use temporary tags, for example, to conditionally execute instructions or networks.

##### Language change within a block

The contents of the registers, accumulators and the status word are only available within STL networks. When an LAD or FBD network follows an STL network, you cannot access the register contents that were previously set in STL from the LAD or FBD network. However, the register contents are again available in a downstream STL network. The result of logic operation is an exception: It is set to "undefined" at a language change and is no longer available in downstream networks.

See also: [Passing values using registers in case of language change](#passing-values-using-registers-in-case-of-language-change-s7-1500)

---

**See also**

[--(RET): Return (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#ret-return-s7-1200-s7-1500)
  
[RET: Return (S7-1200, S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#ret-return-s7-1200-s7-1500)
  
[EN/ENO mechanism](Programming%20basics.md#eneno-mechanism)

#### Partially qualified addresses in LAD/FBD (S7-1500)

##### Introduction

The addressing of DB tags without specification of the DB name is referred to as partially qualified addressing. Partially qualified addressing is not supported in S7-1500 for LAD/FBD. The "---(OPN)" and "---(OPNI)" instructions, which were often used in conjunction with partially qualified addressing, are not supported in S7-1500 either.

##### Migration of partially qualified addresses

Migration handles partially qualified addresses as follows, if possible:

- If the data block can be uniquely determined, migration replaces partially qualified addresses with full addresses and specifies the DB.
- If the DB is specified indirectly by the data block register, the data block cannot be clearly determined. In this case, migration adds a parameter of the data type "DB_Any" to the block interface. The data block name is passed to this parameter. The migration then replaces all partially qualified addresses with addresses having the following syntax: `#<parameter name>.%<absolute address>.`

##### Example

The following example shows migration of partially qualified addresses. In the first figure, you can see the program before migration:

**Network 1**: Tags are addressed partially qualified.

![Example](images/38097438219_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the program after migration:

**Network 1**: The DB containing the tags could be determined unambiguously. The program was migrated automatically. The tags in "DB1" are addressed fully qualified.

![Example](images/38096052619_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Migration of partially qualified block parameters**
>
> The migration also converts partially qualified DB parameters into fully qualified parameters. Note that the type of parameter transfer to the called block can change because of this: The called block may possibly no longer access the actual parameter directly using the fully qualified address but rather work with a copy that is transferred during the block call.  
> You should therefore check whether the semantics of the migrated program match that of the reference program.  
> Additional information is available under: [Access to block parameters during program execution](Programming%20basics.md#transfer-parameter-as-copy-or-as-pointer)  
>   
> If this adaptation is not desired, you can, for example, use a parameter with structured data type rather than an elementary block parameter.   
> Define PLC data type (UDT) as formal parameter and transfer a tag of this type or a DB that was derived from the PLC data type (UDT).

---

**See also**

[Addressing operands](Programming%20basics.md#addressing-operands)

#### Access to status bits in LAD/FBD (S7-1500)

##### Introduction

To achieve the highest possible program execution performance on CPUs of the S7-1500 series, values are only passed between blocks by means of the block interface, by using global data blocks or PLC tags. It is not possible to pass values by using the status word in LAD and FBD.

##### Migration of the instructions "--| |--: Get status bit" / "--|/|--: Get negated status bit"

The instructions are not available in S7-1500. The migration distinguishes between the following cases:

- If a status bit query is placed directly after a mathematical instruction in the same network, a comparator is used instead.
- In all other cases the program is faulty after migration. You have to change your program in this case. For example, use a query of the ENO output instead of a query of the OV status bit. If you link the negation of several ENO queries with OR, you can replace the query of the OS status bit.

##### Example

The following example shows the migration of a status bit query. In the first figure, you can see the program before migration.

**Network 1**: The "<=0" instruction queries the status bit "A1". It indicates whether the result of multiplication is less than or equal to zero.

![Example](images/38099133451_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the program after migration.

**Network 1**: The program was able to be migrated automatically. The "<=0" instruction was removed. Instead, the result of the multiplication is queried by using a comparator with the "myTag3" tag.

![Example](images/38099268619_DV_resource.Stream@PNG-de-DE.png)

### Migration of STL programs to S7-1500 (S7-1500)

This section contains information on the following topics:

- [Information on migrating STL programs (S7-1500)](#information-on-migrating-stl-programs-s7-1500)
- [Logic operation sequences and jumps (S7-1500)](#logic-operation-sequences-and-jumps-s7-1500)
- [Passing values using registers in case of language change (S7-1500)](#passing-values-using-registers-in-case-of-language-change-s7-1500)
- [Passing values using registers or the status word with a block call (S7-1500)](#passing-values-using-registers-or-the-status-word-with-a-block-call-s7-1500)
- [Passing values using registers with the CC and UC instructions (S7-1500)](#passing-values-using-registers-with-the-cc-and-uc-instructions-s7-1500)
- [Fully qualified addresses in STL (S7-1500)](#fully-qualified-addresses-in-stl-s7-1500)
- [Partially qualified addresses in STL (S7-1500)](#partially-qualified-addresses-in-stl-s7-1500)
- [Access to the instance DB in STL (S7-1500)](#access-to-the-instance-db-in-stl-s7-1500)

#### Information on migrating STL programs (S7-1500)

##### Passing values using registers and status words

To achieve the highest possible program execution performance on CPUs of the S7-1500 series, values are only passed between blocks by means of the block interface, by using global data blocks or PLC tags.

There is no way to pass values using registers (for example, accumulators, AR1, AR2, DB, DI) or the status word in LAD and FBD. In STL, values can be passed with some restrictions. Keep in mind that program execution slows down when you use these areas to pass values between various blocks.

The following rules apply for STL:

- The contents of the registers, accumulators and the status word are only available within STL networks. When an LAD or FBD network follows an STL network, you cannot access the register contents that were previously set in STL from the LAD or FBD network. However, the register contents are available again in a downstream STL network.

  The RLO bit is an exception: It is set to "undefined" at a language change and is no longer available in downstream networks.
- The values from the registers, accumulators and the status word are never transferred to called blocks. The instructions "CC" and "UC" are the only exceptions. If you use "UC" or "CC" and want to pass parameters to the called block by using registers, the status word or accumulators, you have to enable the "Parameter passing via registers" option in the properties of the called block. Note that this option is only available for STL blocks with standard access and the block can have no formal parameters. When the option is enabled, you can transfer register contents between blocks. The RLO bit is an exception here as well: It is set to "undefined" when the block is exited and is no longer available after a block call.
- To pass an error message to the calling block, you can use the BR bit. You first need to store the error message in the calling block with the instruction "SAVE" in BR bit. You can then read the BR bit in the calling block.
- The data block register DB is set to "0" after each access to a data block with specification of a fully qualified address (for example, `%DB10.DBW10`). Subsequent partially qualified access leads to an error during compilation.
- If you symbolically address a local formal parameter (e.g. with the instruction L #myIn) from the block interface of an FB in S7-1500, you always access the data block that you specified as an instance in the block call. Although the OPN DI, L AR2, +AR2, TDB, TAR instructions change the contents of the DI or address register, the registers are not evaluated when addressing local formal parameters.

You can find programming examples in the sections below.

##### Master control relay

The master control relay is not available on S7-1500. Migration reports an error. Change the program manually. Formulate conditions, for example, in the form of block parameters to conditionally execute instructions or networks.

##### LEAVE and ENT

The "LEAVE" and "ENT" instructions are not available in S7-1500 because only two accumulators are available. Migration reports an error. Change the program manually. Use temporary tags, for example, to store intermediate results.

##### Block parameters of the "Block_DB" parameter type

The "Block_DB" parameter type is not available in S7-1500. Migration changes this parameter and assigns it the "DB_Any" data type instead.

It is not possible to match library instructions with the call of an instance in the form of a parameter of the "DB_Any" type in S7-1500.

The following example shows the call of a library block with a variable instance in an S7-300/400 CPU. This sequence cannot be migrated to S7-1500.

| STL | Explanation |
| --- | --- |
| CALL GET, #myBlock_DB | / / The library block "GET" is called with the instance data block that is currently applied at the "myBlock_DB" block parameter. |
| REQ := #Start |  |
| ID := W#16#100 |  |
| NDR := #Done |  |
| ERROR := #Error |  |
| STATUS := #Status |  |
| ADDR_1 := P#DB10.DBX5.0 BYTE 10 |  |
| ADDR_2 := |  |
| ADDR_3 := |  |
| ADDR_4 := |  |
| RD_1 := P#DB10.DBX6.0 BYTE 10 |  |
| RD_2 := |  |
| RD_3 := |  |
| RD_4 := |  |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)

#### Logic operation sequences and jumps (S7-1500)

##### Introduction

In S7-300/400, it is possible to place jump labels in STL at any instruction to enable a program-controlled jump to the labeled position. However, if you define the jump destination within a logical program unit in which the RLO does not have a defined state, unexpected results can occur during program execution. The CPU may switch to STOP state.

You must therefore take steps during program creation to ensure that jump labels are only set at the start of a logic operation sequence. You should also avoid jumps from the middle of a logic operation sequence.

The CPU families behave differently when a jump occurs in a logic operation sequence:

- With the S7-300, the first input bit scan behavior of an instruction after a jump label is determined by the instructions executed linearly beforehand. It does not matter here whether the instruction after the jump label was reached linearly or by means of a jump.
- With the S7-400, the first input bit scan behavior of an instruction after a jump label is determined by the actually executed program flow. The first input bit scan behavior can therefore depend on whether the jump label was reached linearly or by means of a jump.
- In S7-1500, a compilation error was output when programs contained jumps out of or into logic operation sequences which could lead to different runtime behavior when executed on an S7-300 or S7-400. The program must be adapted at this point in order to determine the intentional behavior of the program.

##### Example

The following example shows a jump to a logic operation sequence. The instruction in line 6 at the jump label n_OK does not have clearly defined first input bit scan behavior. It is thus not possible to form an RLO. This program sequence would lead to a compilation error on an S7-1500.

![Example](images/96124104075_DV_resource.Stream@PNG-de-DE.png)

##### Migration of jumps to logic operation sequences

The migration does not change the jump labels of your STL program. However, an error is reported when compiling if jump label conflicts are detected. Check the program logic of your block at the reported points of conflict. Use the SET or CLR instructions to label the start of a new "logical unit" and to force a first input bit scan.

##### Recommendation

Avoid jumps in logic operation sequences, for example, to optimize the program code. This makes the code too confusing and hard to maintain.

#### Passing values using registers in case of language change (S7-1500)

##### Introduction

The contents of the registers, accumulators and the status word are only available within STL networks. When an LAD or FBD network follows an STL network, you cannot access the register contents that were previously set in STL from the LAD or FBD network. However, the register contents are available again in a downstream STL network.

The RLO bit is an exception: It is set to "undefined" at a language change and is no longer available in downstream networks.

##### Migration of value passing using registers in case of language change

When a register is accessed in a migrated LAD or FBD network, an error is reported during compilation. Change the program in such a way that registers are only set and read in STL networks.

##### Example

The following example shows the migration of an accumulator access. In the first two figures, you can see the program before migration:

**Network 1:** The "myIN1" operand is downloaded to accumulator 1. Then "myIN2" is downloaded to accumulator 1, which transfers "myIN1" to accumulator 2. Now both values are added together. The result is stored in accumulator 1 and from there it is assigned to the "myOUT" operand.

![Example](images/40115599627_DV_resource.Stream@PNG-de-DE.png)

**Network 2:**The "myIN3" operand is downloaded to accumulator 1. The existing "myOUT" operand is thereby transferred to accumulator 2 and can be immediately added to the "myIN3" operand. The "myOUT" operand does not need to be explicitly downloaded again.

![Example](images/40118615947_DV_resource.Stream@PNG-de-DE.png)

After the migration, network 2 is faulty because values are no longer written to the accumulators by the LAD network. The program must be adapted manually so that both values are explicitly loaded to the accumulators in STL.

The following figure shows network 2 after correction of the error.

**Network 2:** The two values are explicitly loaded to the accumulator in STL before they are added together.

![Example](images/40683121547_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)

#### Passing values using registers or the status word with a block call (S7-1500)

##### Migration of passing values using registers or the status word with a block call

The values from registers, accumulators and the status word are set to "0" or given the status "undefined" at a block change. This means they cannot be passed to called blocks.

The instructions "CC" and "UC" are the only exceptions. If you use "UC" or "CC" and want to pass parameters to the called block by using registers, the status word or accumulators, you have to enable the "Parameter passing via registers" option in the properties of the called block. Note that this option is only available for STL blocks with standard access and the block can have no formal parameters. When the option is enabled, you can transfer register contents between blocks. The RLO bit is an exception: It is always set to "undefined" at a block transition and is no longer available after a block call.

To pass an error message to the calling block, you can use the BR bit. You first need to store the error message in the calling block BR bit. To do this, use the instructions "SAVE" or "JNB", for example. You can then read the BR bit in the calling block.

An error is reported if you access register contents that were set in the called block after a block call. In this case, change your program. Use the tags in data blocks or PLC tags, for example, to return values to the calling block.

##### Examples

The following example shows the changes you need to make to your program in order to pass values to a calling block via registers.

In the first table, you can see the program prior to migration:

| STL | Explanation |
| --- | --- |
| CALL "MyFB", "MyFB_DB" | The RLO of the "MyFB" block is assigned to the "MyBit" operand after execution. |
| = #MyBit |  |
|  |  |

The second table shows you which changes you need to make to the program

| STL | Explanation |
| --- | --- |
| CALL "MyFB", "MyFB_DB" | In the called "MyFB" block, write the currently pending RLO to the BR bit with the instruction "SAVE" at any location. |
| A BR | The BR bit is read in the calling block. |
| = #MyBit | The value of the BR bit is assigned to the "MyBit" operand. |

---

**See also**

[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)
  
[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Protecting blocks](Protecting%20blocks.md#protecting-blocks-1)
  
[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)

#### Passing values using registers with the CC and UC instructions (S7-1500)

##### Introduction

In S7-300/400, block calls can be programmed using the instructions UC and CC. The parameters are not passed to the calling block via the interface, but rather via registers, for example, the AR1, AR2, DB, DI, accumulators or the status word.

These calls slow down program execution and can therefore no longer be set as the default in S7-1500. The CALL instruction is used instead in S7-1500. But the CALL instruction cannot be used to implement indirect block calls. If you wish to use UC or CC for indirect block calls, you need to select the "Parameter passing via registers" option in the properties of the called block. It is then possible for you to transfer register contents between different blocks. The RLO bit is an exception: It is set to "undefined" at a block transition and is no longer available after a block call.

Note that this option is only available for STL blocks with standard access and the block can have no formal parameters. When the option is enabled, you can transfer register contents between blocks. The RLO bit is an exception here as well: It is set to "undefined" at a block transition and is no longer available after a block call.

It is no longer necessary to use indirect block calls for the creation of know-how protected library elements. The TIA Portal supports you here automatically: Any number conflicts that occur with blocks that are already in the user program are automatically resolved when a block is inserted from a library.

##### Migration of block calls via "UC" or "CC"

The migration handles block calls via "UC" or "CC" as follows:

- The "UC FC" instruction with specification of a block number is replaced by the "CALL" instruction.
- The "CC FC" instruction with specification of a block number is replaced by the "CALL" instruction. A jump instruction is also added that implements the conditional call.
- The "UC FC" and "CC FC" instructions with indirect specification of the block number remain unchanged.
- The "UC FB" and "CC FB" instructions with indirect specification of a block number remain unchanged.

##### Example

The following example shows migration of block calls via "UC".

In the first table, you can see the program prior to migration:

| STL |  |
| --- | --- |
| UC FC 10 |  |
| UC FC[#temp0] |  |
| UC FB 10 |  |
| UC FB [#temp0] |  |

In the following table, you can see the program after migration:

| STL | Description |
| --- | --- |
| CALL FC 10 |  |
| UC FC[#temp0] | The "Parameter passing via registers" option must be set at the called block. |
| UC FB 10 | The "Parameter passing via registers" option must be set at the called block. |
| UC FB [#temp0] | The "Parameter passing via registers" option must be set at the called block. |

---

**See also**

[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)
  
[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)

#### Fully qualified addresses in STL (S7-1500)

##### Introduction

The addressing of DB tags with specification of the DB name or DB number is referred to as fully qualified addressing. The data block register is set to "0" after each access to the data block with specification of a fully qualified address. If you want to access the DB register again after fully qualified access, you must first re-assign a value using the OPEN DB command.

##### Migration of fully qualified addresses

Migration inserts the "OPN" instruction after fully qualified access, if needed, to reload the current data block into the data block register.

##### Example

The following example shows migration of a fully qualified address.

In the first table, you can see the program prior to migration:

| STL | Explanation |
| --- | --- |
| AUF "MyDB" | "MyDB" is loaded to the data block register. |
| L %DBW1 | Data elements from "MyDB" are addressed partially qualified. |
| L "Global_DB".Data1 | The elements from a global DB are then addressed fully qualified. "Global_DB" is loaded implicitly to the data block register by this step. |
| L "Global_DB".DBW2 |  |
| T DBW[AR1, P#0.0] | A subsequent access addresses the "Global_DB", because it is in the DB register. |

In the following table, you can see the program after migration:

| STL | Explanation |
| --- | --- |
| AUF "MyDB" |  |
| L "MyDB".DBW1 | The partially qualified access is converted into a fully qualified access. |
| L "Global_DB".Data1 |  |
| L "Global_DB".DBW2 | The DB register is reset after fully qualified access. |
| OPN "Global_DB" | The "Global_DB" must be loaded to the DB register again with OPN. |
| T DBW[AR1, P#0.0] |  |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)

#### Partially qualified addresses in STL (S7-1500)

##### Introduction

The addressing of DB tags without specification of the DB name or DB number is referred to as partially qualified addressing. Partially qualified addressing accesses a defined value in the data block that is currently stored in the DB register.

The following restrictions apply to partially qualified addresses in S7-1500:

- In S7-1500, partially qualified addresses are only allowed if the DB register has been set explicitly in the current block. You set the DB register with the instruction "OPN", for example. In data blocks with standard access, you can only address tags partially qualified.
- The data block register is set to "0" with the block call in S7-1500. This means it is not possible to open a data block in a block and to address data elements from the data block in a subordinate block partially qualified. Set the DB register in the current block before you address a DB tag partially qualified.
- The DB data block register is also to "0" with each fully qualified access (for example, %DB10.DBW10). Set the DB register again after fully qualified access before you address a DB tag partially qualified.
- The use of partly qualified addresses slows down the processing of the program during runtime.

##### Migration of partially qualified addresses

Migration handles partially qualified addresses in STL as follows:

- The partially qualified address is converted into a fully qualified address, if possible.
- If the data block is opened in the calling code block and the DB cannot be clearly identified, migration inserts a parameter of the "DB_Any" data type in the interface of the called block. The data block name is passed to this parameter. Migration inserts the "OPN" instruction in the called block to open the data block.

##### Example

The following example shows the migration of partially qualified addresses.

In the first table, you can see the program prior to migration:

| STL | Explanation |
| --- | --- |
| L DBW10  L DBW12  +I  T DBW14 | A data block is opened in the calling block and transferred to the DB register. In the current block, the values "DBW10", "DBW12" and "DBW14" are adopted from the data block that is currently open in the DB register. |

In the following table, you can see the program after migration:

| STL | Explanation |
| --- | --- |
| OPN "PlcmigTempBlockDB"  L DBW10  L DBW12  +I  T DBW14 | Migration inserts a parameter of the data type "DB_Any" in the interface of the called block. The data block name is passed to this parameter. Migration inserts the "OPN" instruction in the called block to open the data block passed in the interface. |

> **Note**
>
> **Migration of partially qualified block parameters**
>
> The migration also converts partially qualified DB parameters into fully qualified parameters. Note that the type of parameter transfer to the called block can change because of this: The called block may no longer access the actual parameter directly using the fully qualified address but works with a copy that was transferred during the block call instead.  
> Make sure that the semantics of the migrated program matches that of the reference program.  
> Additional information is available under: [Access to block parameters during program execution](Programming%20basics.md#transfer-parameter-as-copy-or-as-pointer)  
>   
> If this adaptation is not desired, you can, for example, use a parameter with structured data type rather than an elementary block parameter.   
> Define PLC data type (UDT) as formal parameter and transfer a tag of this type or a DB that was derived from the PLC data type (UDT).
>
> Examples:
>
> CALL "MyFC"  
>  InStruct :="DBofUDT"  
>   
> or  
>   
>  CALL "MyFC"  
>  InStruct := "DBArrayOfUDT".a[#i]

---

**See also**

[Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)
  
[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)

#### Access to the instance DB in STL (S7-1500)

##### Introduction

The "OPN DI" or "CDB" instructions place a data block in the DI register. In S7-300/400, the block opened there is considered an instance data block. The subsequent symbolic addressing of a local formal parameter from the block interface of an FB (IN, OUT, InOut, Static) no longer addresses the data block that was specified as an instance in the block call, but rather the data block that is located in the DI register. To subsequently symbolically address a local formal parameter from the block interface, the instance DB must be loaded to the DI register.

Even after the instructions "L AR2", "+ AR" and "TAR", it is not possible in S7-300/400 to symbolically address a formal parameter from the block interface, because the basis for the parameter access has been destroyed by the instructions.

This behavior has been corrected in S7-1500: If you symbolically address a local formal parameter (e.g. with the instruction L #myIn) from the block interface in S7-1500, you always access the data block that you specified as an instance in the block call. Although the OPN DI, L AR2, +AR2, TDB, TAR instructions change the contents of the DI or address register, the registers are not evaluated when addressing local formal parameters.

##### Migration of accesses to local tags in the instance DB

Migration does not change the programmed accesses. However, if you have changed the instructions OPN DI, L AR2, +AR2, TDB, TAR, etc. in the reference program, the semantics of the program may have changed.   
In order to achieve the original semantics again, you must change the program manually. It is often no longer necessary to address data via registers. Instead, avail of the possibility to use ARRAYs within the instance DB and index the ARRAY elements indirectly.

##### Example 1

The following example shows the modified semantics of the instruction "OPN DI":

| STL | Explanation |
| --- | --- |
| L #MyIn1  L #MyIn2  +I  T #MyOut3 | The "L" and "T" instructions address local tags that were declared in the block interface. The values of the tags are located in the instance DB that was specified in the block call. |
| OPNDI "MyDB"  L #MyIn1  L #MyIn2  +I  T #MyOut3 | The global data block "MyDB" is written to the DI register.   The "L" and "T" instructions address tags that were declared in "MyDB" prior to migration.  After migration, the "L" and "T" instructions address tags that were declared in the block interface. The DI register is not evaluated for access in S7-1500. |

##### Example 2

The following example shows the modified semantics of the instruction "LAR2":

| STL | Explanation |
| --- | --- |
| L P#M23.0 |  |
| LAR2 | Prior to migration, the basis for parameter access is destroyed with the assignment to AR2. |
| L #MyIn1 | Prior to migration, access to "MyIn1" is not possible or results in an error.  After migration, access to the formal parameter "MyIn1" is correctly executed. |
| L IW [AR2, P#1.0] | Access to %IW24.0 |
| A [AR2, P#0.4] | Access to %M23.4 |

##### Example 3

The following example shows how a DB tag can be addressed indirectly in S7-1500 without using the address register:

| STL | Explanation |
| --- | --- |
| OPN "MyDB"  L #index  LAR1  L DBW [AR1 , P#10.0] | Prior to migration, area-internal indirect register addressing is used. A variable value (#index) is hereby loaded to the address register 1. Depending on this value, a data word from "MyDB" is loaded to accumulator 1. |
| L "MyDB".MyArray1[#index] | After migration, you can store the data values in "MyDB" in an ARRAY.   The individual ARRAY elements can be variably indexed using the input parameter "#index". |

### Migration of SCL programs to S7-1500 (S7-1500)

This section contains information on the following topics:

- [Information on migrating SCL programs (S7-1500)](#information-on-migrating-scl-programs-s7-1500)
- [Indirect addressing in SCL (S7-1500)](#indirect-addressing-in-scl-s7-1500)
- [Instructions in SCL (S7-1500)](#instructions-in-scl-s7-1500)

#### Information on migrating SCL programs (S7-1500)

##### Representation of SCL blocks after migration

SCL blocks that were created with S7-300/400 are automatically migrated to S7-1500, if their semantics are clearly interpretable. The program positions that are not clearly interpretable are marked with a question mark after the migration, which results in syntax errors. Check the semantics at these positions in the program after migration and correct them if necessary.

In some cases, the program code is changed by the migration. The corresponding section of code from the original program is then transferred to the migrated block as a comment section. This makes it easy for you to track the changes that were made by the migration.

---

**See also**

[Basic information on migrating PLC programs (S7-1500)](#basic-information-on-migrating-plc-programs-s7-1500)
  
[Information on migrating PLC programs (S7-1500)](#information-on-migrating-plc-programs-s7-1500)

#### Indirect addressing in SCL (S7-1500)

##### Introduction

The options for indirect addressing were standardized for all programming languages in S7-1500. Indirect addressing that was possible in S7-300/400 is therefore partially converted during the migration.

The following table provides an overview of the conversion options. The migration of individual language constructs is explained below in more detail.

| Indirect addressing | S7-300/400 | S7-1500 |
| --- | --- | --- |
| Indirect addressing of a DB | Data type "BLOCK_DB" | "DB_ANY" data type |
| Indirect addressing of DB tags | #block.%DBW3 | "PEEK"/"POKE" instructions |
| WORD_TO_BLOCK_DB(#myWord).%DBW3 | "PEEK"/"POKE" instructions |  |
| #block.DW(IDX := #myInt) | "PEEK"/"POKE" instructions |  |
| WORD_TO_BLOCK_DB(#myWord).DW(IDX:=#myInt) | "PEEK"/"POKE" instructions |  |
| %DB1.DW(IDX :=#myInt) | "PEEK"/"POKE" instructions |  |
| Indirect addressing of I/O | QB(IDX :=#myInt):P | "PEEK"/"POKE" instructions |
| Indirect addressing of PLC tags | IX(IDX :=#myInt1,Bit:=#myInt2) | "PEEK"/"POKE" instructions |
| QB(IDX :=#myInt) | "PEEK"/"POKE" instructions |  |
| MW(IDX :=#myInt) | "PEEK"/"POKE" instructions |  |

##### Migration of the "BLOCK_DB" data type to "DB_ANY"

The "BLOCK_DB" data type is no longer available in S7-1500. Tags of this data type are converted to the "DB_ANY" data type by the migration. The "BLOCK_DB_TO_WORD" and "WORD_TO_BLOCK_DB" conversion functions are migrated to "UINT_TO_WORD(DB_ANY_TO_UINT)" and "UINT_TO_DB_ANY(WORD_TO_UINT)".

The following examples show the migration of the "BLOCK_DB" data type.

In the first table, you can see three program sections prior to migration:

| SCL |  |
| --- | --- |
| #myBlock //Data type BLOCK_DB;  //... |  |
| #myWord :=BLOCK_DB_TO_WORD(#myBlock);  //... |  |
| #myBlockDB := WORD_TO_BLOCK_DB(#myWord); |  |

In the second table, you can see three program sections after migration:

| SCL |  |
| --- | --- |
| #myBlock //Datentyp DB_Any;  //... |  |
| #myWord := UINT_TO_WORD(DB_ANY_TO_UINT(#myBlock));  //... |  |
| #myDBANY:= UINT_TO_DB_ANY(WORD_TO_UINT(#myWord)); |  |

##### Migration of indirect addressing of DB tags

Indirect specification of data blocks or DB tags is implemented with the "PEEK"/"POKE" instructions in S7-1500. The migration automatically converts them to indirect addressing.

The following examples show the migration of indirect addressing of DB tags.

In the first table, you can see some program sections prior to migration:

| SCL |  |
| --- | --- |
| #myWord := %DB1.DW(IDX :=#myInt);  //... |  |
| #myBool := %DB1.DX(IDX :=#myByteOffset,Bit:=#myBitOffset);  //... |  |
| %DB1.DW(IDX := #myInt) := 12;  //... |  |

In the second table, you can see the program sections after migration:

| SCL |  |
| --- | --- |
| #myWord := PEEK_WORD(area:=16#84, dbNumber:=1, byteOffset:=#myInt);  //... |  |
| #myBool:=PEEK_BOOL(area:=16#84, dbNumber:=1, byteOffset:=#myByteOffset, bitOffset:=#myBitOffset);  //... |  |
| POKE(area:=16#84,dbNumber:=1,byteOffset:=#myInt,value:=12);  //... |  |

##### Migration of indirect addressing of PLC tags

Indirect specification of PLC tags is implemented with the "PEEK"/"POKE" instructions in S7-1500. The migration automatically converts them to indirect addressing.

The following examples show the migration of indirect addressing of DB tags.

In the first table, you can see a program section prior to migration:

| SCL |  |
| --- | --- |
| #myWord := MW(IDX := #myInt); |  |

In the second table, you can see the program sections after migration:

| SCL |  |
| --- | --- |
| #myWord := PEEK(area:=16#83,dbNumber:=0,byteOffset:=#myInt); |  |

---

**See also**

[POKE: Write memory address (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#poke-write-memory-address-s7-1200-s7-1500)
  
[POKE_BOOL: Write memory bit (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#poke_bool-write-memory-bit-s7-1200-s7-1500)
  
[PEEK: Read memory address (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#peek-read-memory-address-s7-1200-s7-1500)
  
[PEEK_BOOL: Read memory bit (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#peek_bool-read-memory-bit-s7-1200-s7-1500)
  
[POKE_BLK: Write memory area (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#poke_blk-write-memory-area-s7-1200-s7-1500)
  
[Addressing operands indirectly](Programming%20basics.md#addressing-operands-indirectly)

#### Instructions in SCL (S7-1500)

##### Migration of instructions

S7-1500 has a slightly different set of instructions. Some instructions have been innovated or replaced by new instructions.

During migration, the instructions used in the program are retained as much as possible. If an instruction is not available in S7-1500, an attempt is made to replace it with a compatible or similar instruction. You then have to check the migrated program again and adapt it if necessary.

The following changes may occur, for example:

- The new instruction has additional formal parameters. Configure the additional parameters.
- A formal parameter of the new instruction has a different data type. In this case, the migration automatically adds an instruction to convert the data types.

If the migration cannot unequivocally ensure that the parameter assignment is semantically identical to the initial program, the relevant parameters are commented out. Check the semantics at these locations in the program after migration and correct it if necessary.

The following examples show the migration of the "AG_SEND" instruction to the "TSEND" instruction.

In the first table, you can see a call of "AG_SEND" prior to migration:

| SCL |  |
| --- | --- |
| AG_SEND (ACT:=#myBool,   ID:=#myInt1,   LADDR:=#myWord,   SEND:=#myAny,   LEN:=#myInt2,   DONE=>#myBool,   ERROR=>#myBool,   STATUS=>#myWord); |  |

In the first table, you can see the call of "TSEND" after migration:

| SCL |  |
| --- | --- |
| "TSEND_DB"((* ToReplace: REQ:=#myBool *)    (* ToReplace: ID:=#myInt1 *)    LEN:=INT_TO_UDINT(#myInt2),   DONE=>#myBool,   ERROR:=#myBool,   STATUS:=#myWord,   DATA:=#myAny; |  |

The actual parameter of "REQ" was applied from the "ACT" parameter of the "AG_SEND" instruction. It is commented out because the program must be checked at this location.

The actual parameter of "ID" was applied from "AG_SEND" and also needs to be tested.

The "LEN" parameter has another data type with "AG_SEND". The migration automatically adds a conversion.

##### Migration of instructions in expressions

In some cases, migration generates several instructions from a single instruction, for example, when an output parameter has another data type after migration and the formal parameter must be converted. The conversion instruction is inserted after the migrated instruction. This means, however, that the original instruction can no longer be used as an expression. In this case, the migration adds a temporary tag in the interface of the migrated block and assigns it the result of the instruction. This temporary tag can then be used as an expression. Automatic migration cannot always be performed for complex expressions. Expressions that are not clearly interpretable are marked with a question mark after the migration, which results in syntax errors. Check the semantics at these locations in the program after migration and correct it if necessary.

The following examples shows the migration of the "READ_RTM" instruction to the "RTM" instruction.

In the first table, you can see a call of "READ_RTM" prior to migration:

| SCL |  |
| --- | --- |
| IF READ_RTM(NR:=#myByte, CQ=>#myBool, CV=>#myOutInt)= 1 THEN   ...; END_IF; |  |

In the second table, you can see a call of "RTM" after migration.

| SCL |  |
| --- | --- |
| (* classic code: IF READ_RTM(NR:=#myByte, CQ=>#myBool, CV=>#myOutInt)= 1 THEN*)  #SCL_MIGRA_TEMP_INT_1:=RTM(NR:=#myByte,   MODE:=0,   PV:=#Migra_PV,   CQ:=#myBool,   CV:=#Migra_CV);  #myOutInt:=DINT_TO_INT(#Migra_CV);     IF #SCL_MIGRA_TEMP_INT_1= 1 THEN;  ...  END_IF; |  |

The instruction from the original program is transferred as a comment section to the migrated block. This makes it easy for you to track the changes that were made by the migration.

Because CV has the DINT data type for "RTM", a conversion instruction is inserted that converts the actual parameter from INT to DINT. This means the result of RTM can no longer be used as an expression within the IF instruction.

The temporary tag "SCL_MIGRA_TEMP_INT_1" is inserted in the interface of the migrated block. The result of the RTM instruction is assigned to the temporary tag.

The temporary tag is used as the expression in the IF instruction instead of the "RTM" instruction.

### Migration of GRAPH programs to S7-1500 (S7-1500)

This section contains information on the following topics:

- [Information on migration of GRAPH programs (S7-1500)](#information-on-migration-of-graph-programs-s7-1500)
- [Changes in the GRAPH program (S7-1500)](#changes-in-the-graph-program-s7-1500)
- [Adaptation of the interface of GRAPH blocks (S7-1500)](#adaptation-of-the-interface-of-graph-blocks-s7-1500)

#### Information on migration of GRAPH programs (S7-1500)

##### Introduction

GRAPH programs that were created with S7-300/400 can be migrated automatically to S7-1500. The PLC migration optimizes the programs for running on a CPU of the S7-1500 series. The migration log reports all automatic program changes made during the migration and informs you of any necessary manual changes you still have to perform.

##### Adaptation of the GRAPH program by the PLC migration

The following list shows some examples of automatic adaptations that are made during the PLC migration. All adaptations are described in detail in the sections belows.

- Adaptation of the block interface

  The interface of the GRAPH blocks is changed slightly. This enables use of the optimized block access of the S7-1500 for GRAPH blocks.
- Integrated symbolic addressing

  SIMATIC S7-1500 is characterized by its integrated symbolic programming. This makes the program more efficient and reduces the risk of access errors.   
  For this reason, if the initial program uses addresses for which a symbolic name is not declared, the migration assigns a symbolic name for the address whenever possible.
- Memory model of the GRAPH DB

  Based on the performance data of the S7-1500, it is no longer necessary to use GRAPH DBs with minimized memory space requirements. For this reason, GRAPH no longer offers different memory space models. You have access to the full parameter set and thus the complete functionality in all GRAPH DBs.

  During migration, DBs with minimized memory space requirements are expanded to include the full parameter set.

##### New functions of the S7-1500

Following migration of a GRAPH program, you can make full use of the functionality of the S7-1500. The following list shows some examples of the new functions:

- Optimized block access

  With optimized block access, the declared data elements are arranged automatically in the available memory area of the block in such a way as to make optimal use of its capacity. The data is structured and saved in a manner that is optimal for the CPU used. This allows you to increase the performance of the CPU. Access errors, from the HMI, for example, are not possible.

  The "Optimized block access" attribute is always enabled for GRAPH blocks in S7-1500 and cannot be deselected.

  See also: [Blocks with optimized access](Programming%20basics.md#blocks-with-optimized-access)
- New instructions

  The "Instructions" task card contains the complete set of instructions of the S7-1500. Numerous instructions have been newly developed or innovated. For example, the "Program control" folder in the "Basic instructions" pane contains the "GET_ERROR" instruction for programming local troubleshooting.

  See also: [GET_ERROR: Get error locally](GRAPH%20%28S7-1500%29.md#get_error-get-error-locally-s7-1500)
- LAD/FBD functions

  For S7-300/400, GRAPH only supported the programming of a preceding logic operation at the first Boolean input of a box. In S7-1500, preceding logic operations can be programmed for all Boolean inputs.

  The enable output (ENO) can be enabled or disabled selectively for individual instructions.

  See also: [Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
- New data types

  S7-1500 provides an expanded set of data types and new data type conversion options.

  See also: [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
- Constants

  S7-1500 provides additional options for constant notation. Thus you can also assign data types to constants.

  See also: [Constants](Programming%20basics.md#constants)

#### Changes in the GRAPH program (S7-1500)

##### Introduction

The PLC migration automatically adapts the GRAPH program to the new CPU family as much as possible. In so doing, both the actions as well as the LAD or FBD networks that you used for programming of conditions are analyzed. Program structures that are no longer permitted are updated. Instructions that are not available on the new CPU are replaced with appropriate S7-1500 instructions.

##### Symbolic addressing

SIMATIC S7-1500 is characterized by its integrated symbolic programming. This makes the program more efficient and reduces the risk of access errors.

If the initial program uses absolute addresses for which a symbolic name is not declared, the absolute address is marked as invalid. You must then declare a symbolic name before you can compile the migrated program.

If the initial program uses absolute addresses for which a symbolic name is declared, the migration uses the symbolic name instead of the absolute address. Accesses to individual bits within a declared symbolic operand are replaced by slice accesses.

The following example shows an absolute access before the migration:

| Symbol | Meaning |
| --- | --- |
| %DB1.DBx1.1 |  |

The following shows you how the migration replaces the absolute access. Since the "FirstDataByte" tag was declared for the first data byte in "DataBlock1", the access to the first bit within this tag can be replaced by a slice access.

| Symbol | Meaning |
| --- | --- |
| "DataBlock1".FirstDataByte.x1 |  |

##### Fully qualified addressing

S7-300/400 programs frequently use partially qualified addresses to access addresses indirectly. In this case only the address of a DB tag within a data block is specified. The DB name or DB number is not specified in the address (e.g., `%DBX0.2`). At runtime, the program accesses the data block that is currently stored in the DB register. Partially qualified addressing is not supported in S7-1500. In order to address DB tags indirectly, use block parameters of data type "DB_ANY".

If you have used partly qualified addresses in GRAPH programs, these are reported as errors after the migration. The block cannot be compiled. Then replace the partly qualified address with a fully qualified address.

##### LAD/FBD elements in conditions

The LAD or FBD networks in Transition, Interlock, Supervision, and Permanent instructions are migrated according to the same rules as the networks in pure LAD or FBD blocks.

See also: [Migration of LAD/FBD programs to S7-1500](#migration-of-ladfbd-programs-to-s7-1500-s7-1500)

##### GRAPH actions

SIMATIC S7-1500 provides a slightly modified set of instructions. Some instructions have been innovated or replaced by new instructions.

If you have used instructions in GRAPH actions, the migration checks whether these are still supported on S7-1500. The instructions are carried over as much possible. If an instruction is not available in S7-1500, an attempt is made to replace it with a compatible or similar instruction.

Examples of this are the "RLDA: Rotate left by status bit CC 1" and "RRDA: Rotate right by status bit CC 1" instructions. These are replaced by the "ROR: Rotate right" and "ROL: Rotate left" instructions.

If instructions are replaced during the migration, this is noted in the migration log. You then have to check the migrated program again and adapt it if necessary.

See also: [Migration of instructions to S7-1500](#migration-of-instructions-to-s7-1500-s7-1500)

#### Adaptation of the interface of GRAPH blocks (S7-1500)

##### Modification of the block interface during migration

The interface of the GRAPH blocks is adapted during the migration. The adaptations enable you to use the optimized memory concept of the S7-1500 with GRAPH. Optimized block access is always active for GRAPH blocks on the S7-1500 and cannot be deselected. Changes are made in the following areas:

- Static parameters: "STATIC"
- Output parameters: "OUTPUT"
- Retentivity setting for all internal parameters

See also: [Blocks with optimized access](Programming%20basics.md#blocks-with-optimized-access)

If you have used parameter names in the initial program that are reserved in S7-1500, these are renamed during the migration.

##### Static parameters

Static parameters are adapted as follows during the migration:

- The interface contains a structure in the "Static" section for each step and transition of the GRAPH FB. In S7-300/400, the "GraphStep", "GraphStepMin", "GraphTransition", and "GraphTransitionMin" data types were used. In S7-1500, the new "G7_StepPlus" and "G7_TransitionPlus" data types are introduced for reproducing the step and transition structures.

  The migration proceeds as follows here:

  - The "SNO" and "TNO" parameters are transferred together with their default values from the old structures; all other default values are not transferred. GRAPH programs with a DB with minimized memory space requirements do not contain the "SNO" and "TNO" parameters. If you migrate a DB with minimized memory space requirements, the migration assigns default values for these parameters starting with "1".
  - The locations of use of the modified parameters in the GRAPH program are not adapted automatically but rather are marked as errors. You must manually adapt the locations of use after the migration.
- All other static parameters are transferred to the "RT_DATA" structure. The default values are thus carried over as much as possible and the locations of use in the program are adapted automatically.

##### Output parameters

Because the output parameter "S_CRITSUP" is no longer supported during criteria analysis on S7-1500, it is removed during migration.

The locations of use in the GRAPH program are not adapted automatically but rather are marked as errors. You must manually adapt the locations of use after the migration.

##### Retentivity setting for all internal parameters

The retentivity setting of the internal GRAPH parameters affects the behavior of the sequential control system after a power loss:

- A GRAPH block whose parameters are retentive continues with the last active step after a power loss.
- A GRAPH block whose parameters are not retentive starts again with the initial step after a power loss.

GRAPH blocks that were created with S7-300/400 have retentive interface parameters by default.

The retentiveness of the internal parameters is not kept when you migrate the GRAPH FB from an S7-300/S7-400 CPU to an S7-1500 CPU. The internal parameters are declared as non-retentive after the migration.

Proceed as follows after the migration to declare the internal parameters of a GRAPH FB as retentive again:

1. Open the GRAPH FB after the migration.
2. Select the "Retentive internal parameters" command in the "Edit" menu.

   The settings for the internal parameters in the "Retain" column change from "Retain" to "Non-retain" in the block interface of the GRAPH FB.
3. Save and compile your project.

   The settings for the parameters are then applied to all instance DBs.

---

**See also**

[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
