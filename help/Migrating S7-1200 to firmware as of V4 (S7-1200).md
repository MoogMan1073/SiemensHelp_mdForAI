---
title: "Migrating S7-1200 to firmware as of V4 (S7-1200)"
package: ProgFWMigration2MenUS
topics: 4
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Migrating S7-1200 to firmware as of V4 (S7-1200)

This section contains information on the following topics:

- [Basic information on upgrading to V4 (S7-1200)](#basic-information-on-upgrading-to-v4-s7-1200)
- [Migrating to V4 (S7-1200)](#migrating-to-v4-s7-1200)
- [Special considerations after migrating to V4 (S7-1200)](#special-considerations-after-migrating-to-v4-s7-1200)

## Basic information on upgrading to V4 (S7-1200)

### Introduction

If you have used a CPU with firmware version V3 in your project and want to upgrade to a CPU with firmware V4.0 or later, you can easily replace the device.

The TIA Portal offers the "Change device" function for this purpose. The project remains unchanged when the device is replaced. You can continue using the programs that you created with firmware version V3.

### Rules

The following basic rules apply when replacing a device:

- Replacing a device is only possible if the project was created based on a CPU with firmware version V3.0. If your project was created based on firmware version V1.0 or V2.0, create a new CPU with firmware version V3.0 offline in the project, and copy your program to this CPU.
- It is not possible to replace a V4 CPU with a V3 CPU. If you want to continue using the existing V3 CPU, create a copy of this CPU before replacing the device.
- The program cannot be transferred to the new CPU via a memory card. Instead, use the "Change device" function, which is described in the following sections.

### HMI panels

Configured HMI panels are treated differently during device replacement depending on the firmware version of the panel and the communication mode.

The following table shows the HMI connections that are supported with the migration:

| Firmware version of the panel | PUT/GET communication | Migration to V4 |
| --- | --- | --- |
| V11 or later | No | S7-1200 does not support this configuration. Upgrade the firmware of the HMI panel to V12.0. Then compile and load the configuration. |
| V11 or later | Yes | S7-1200 supports this configuration. The connection is established automatically while you compile and load the project after replacing the device. |
| V12 or later | No | S7-1200 supports this configuration. The connection is established automatically while you compile and load the project after replacing the device. |

During compilation of the program, you receive specific information on migrating the HMI panel.

### S7-1200 expansion modules

If you are already using the following centrally plugged S7-1200 modules in your system, you must perform a firmware update for these modules in order to guarantee operation with S7-1200 V4.

- ASi - Master - CM 1243
- DP - Master - CM 1243-5
- WAN CP - CP1243-1

Newly shipped S7-1200 modules have the latest firmware installed ex works.

### Protected blocks

Blocks equipped with know-how protection or copy protection cannot be converted to V4. If the project contains protected blocks, you must remove the protection prior to migration.

If these are supplied blocks and you do not know the password, ask your supplier either for the password or for a V4-compatible block.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Preventing personal injury and material damage**  Changes are made to the program during device replacement in some cases. Therefore, thoroughly check the program in a test environment after replacing the device and before putting it in operation. |  |

> **Note**
>
> **Additional support**
>
> You can find the latest FAQs about migrating to S7-1200 V4 in Siemens Industry Online Support:
>
> <http://support.automation.siemens.com/WW/view/en/82140966>
>
> If you need further assistance with migrating to S7-1200 V4, please contact SIMATIC Customer Support.

---

**See also**

[Migrating to V4 (S7-1200)](#migrating-to-v4-s7-1200)
  
[Special considerations after migrating to V4 (S7-1200)](#special-considerations-after-migrating-to-v4-s7-1200)

## Migrating to V4 (S7-1200)

### Requirement

- A CPU with firmware version V3 is available in the project.
- The project contains no protected blocks.

### Procedure

Proceed as follows to replace a CPU:

1. Select the V3 CPU you want to replace.
2. Select the "Change device" command in the shortcut menu.

   The "Change device" dialog box appears.
3. Under "New device" in the tree structure, select the V4 CPU with which you want to replace your current V3 CPU.
4. Click "OK".

   The existing CPU is replaced by the new one.
5. Select the new CPU and select the "Compile > Hardware and software (only changes)" command in the shortcut menu.

   The device configuration and the user program are compiled again.
6. Optional: If necessary, apply know-how protection or copy protection to individual blocks in the program.
7. Select the new CPU and select the "Download to device > Hardware and software (only changes)" command in the shortcut menu.

   The device configuration and the user program are loaded into the new CPU.

   This completes the device replacement.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Preventing personal injury and material damage**  Changes are made to the program during device replacement in some cases. Therefore, thoroughly check the program in a test environment after replacing the device and before putting it in operation. |  |

> **Note**
>
> **Additional support**
>
> You can find the latest FAQs about migrating to S7-1200 V4 in Siemens Industry Online Support:
>
> <http://support.automation.siemens.com/WW/view/en/82140966>
>
> If you need further assistance with migrating to S7-1200 V4, please contact SIMATIC Customer Support.

---

**See also**

[Basic information on upgrading to V4 (S7-1200)](#basic-information-on-upgrading-to-v4-s7-1200)
  
[Special considerations after migrating to V4 (S7-1200)](#special-considerations-after-migrating-to-v4-s7-1200)

## Special considerations after migrating to V4 (S7-1200)

### Functional changes in V4

S7-1200 V4 offers significantly enhanced functionality. The most important functional changes that you need to consider after migrating from V3 are described briefly below.

You can find more information on S7-1200 in the "SIMATIC S7-1200 Automation System" system manual:

[https://support.industry.siemens.com/cs/ww/en/view/65601780](http://support.automation.siemens.com/WW/view/en/65601780)

### Organization blocks

With S7-1200 V4, you can specifically set the interruptibility of each organization block used. When a device is replaced, all the organization blocks are configured as non-interruptible, to ensure that the executability of your V3 program remains unchanged. The OB priorities from the V3 program also remain unchanged. After migration, you can change the settings for priority and interruptibility as needed.

The behavior of diagnostic interrupts in V4 has changed as follows:

In V3, the start information always contained information on the triggering module, including the channel number. In V4, this information is only generated for a pending diagnostics event. If no diagnostic event is pending, for example, because the fault has already been corrected, only the triggering module is indicated.

### Access levels

S7-1200 V4 offers an extended access level concept. The following table shows how the protection levels of the V3 firmware are indicated in V4:

| V3 protection level | V4 access level | Meaning |
| --- | --- | --- |
| No protection | Full access (no protection) | Unrestricted access without password protection. |
| Read-only | Read access | HMI access and unimpeded communication between CPUs without password protection.  A password is required for changes (write access) in the CPU and for changing the  operating mode of the CPU (RUN/STOP). |
| Write/read protection | HMI access | HMI access and unimpeded communication between CPUs without password protection.  A password is required to read the data in the CPU, for changes (writing) in the CPU, and  for changing the operating mode of the CPU (RUN/STOP). |
| - | No access (complete protection) | No access without password input.  A password is required for HMI access, for reading the data in the CPU, for changing (writing) data in the CPU, and for changing the operating mode of the CPU (RUN/STOP). |

### Instruction libraries

After migration to S7-1200 V4, instructions from the libraries of the firmware version V3 are still available. This ensures that you can continue to use your program unchanged. In addition, S7-1200 V4 offers many new instructions which are also compatible with the instructions of the S7-1500.

You can find more information on the instruction libraries in the "SIMATIC S7-1200 Automation System" system manual:

[https://support.industry.siemens.com/cs/ww/en/view/65601780](http://support.automation.siemens.com/WW/view/en/65601780)

### Motion Control

When a device is replaced, the Motion Control objects from the libraries of the firmware versions V1 and V2 are replaced with the corresponding objects from the V3 libraries. The objects from V3 libraries are compatible so that you can continue to use the programs unchanged.

The libraries of the S7-1200 V4 offer many new Motion Control functions, which are compatible with the functions of the S7-1500. If you want to use V4 libraries, select them on the "Instructions" task card after replacing the device.

You can find more information on the new Motion Control functions in the "SIMATIC S7-1200 Programmable controller" system manual.

[https://support.industry.siemens.com/cs/ww/en/view/65601780](http://support.automation.siemens.com/WW/view/en/65601780)

### Web server

The following settings for operation via a web server are transferred from the V3 CPU to the V4 CPU during device replacement:

- Activate web server on this module
- Permit access only with HTTPS

If you want to operate the V4 CPU via a web server, you need to set up user accounts with assigned user rights in the user management. Only the standard web pages are available to standard users without any additional rights.

> **Note**
>
> **Additional support**
>
> You can find the latest FAQs about migrating to S7-1200 V4 in Siemens Industry Online Support:
>
> <http://support.automation.siemens.com/WW/view/en/82140966>
>
> If you need further assistance with migrating to S7-1200 V4, please contact SIMATIC Customer Support.

### Communication via PUT/GET

Communication via PUT/GET is enabled after the device replacement. Note that the new integrated connection types offer a security standard higher than PUT/GET communication. If you do not use PUT/GET communication, you should disable it.

---

**See also**

[Basic information on upgrading to V4 (S7-1200)](#basic-information-on-upgrading-to-v4-s7-1200)
  
[Migrating to V4 (S7-1200)](#migrating-to-v4-s7-1200)
