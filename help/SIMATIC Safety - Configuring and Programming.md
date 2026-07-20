---
title: "SIMATIC Safety - Configuring and Programming"
package: ProgFAILenUS
topics: 292
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SIMATIC Safety - Configuring and Programming

This section contains information on the following topics:

- [Important notes](#important-notes)
- [Product Overview](#product-overview)
- [Configuring](#configuring)
- [Safety Administration Editor](#safety-administration-editor)
- [Access protection](#access-protection)
- [Programming](#programming)
- [F-I/O access](#f-io-access)
- [Implementation of user acknowledgment](#implementation-of-user-acknowledgment)
- [Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program)
- [Safety-related communication](#safety-related-communication)
- [Compiling and commissioning a safety program](#compiling-and-commissioning-a-safety-program)
- [System acceptance](#system-acceptance)
- [Operation and maintenance](#operation-and-maintenance)
- [STEP 7 Safety V19 instructions](STEP%207%20Safety%20V19%20instructions.md#step-7-safety-v19-instructions)
- [Monitoring and response times](#monitoring-and-response-times)
- [Checklist](#checklist)
- [Glossary](#glossary)

## Important notes

This section contains information on the following topics:

- [Important notes](#important-notes-1)
- [Cybersecurity information](#cybersecurity-information)
- [Siemens Industry Online Support](#siemens-industry-online-support)
- [Industry Mall](#industry-mall)

### Important notes

#### Purpose of this documentation

The information in this documentation enables you to [configure](#configuring) and [program](#programming) SIMATIC Safety fail-safe systems. In addition, you will obtain information on [acceptance](#system-acceptance) of a SIMATIC Safety F-system.

> **Note**
>
> The Programming and Operating Manual "SIMATIC Safety - Configuring and Programming" in its latest version (possibly including product information for the manual) is the relevant source of all information on functional safety regarding configuring and programming. This also applies in the event of discrepancies between this manual and other documentation on functional safety regarding configuring and programming of SIMATIC Safety.
>
> You must heed all warnings in the Programming and Operating Manual "SIMATIC Safety - Configuring and Programming".

#### Basic knowledge requirements

General basic knowledge of automation engineering is needed to understand this documentation. Basic knowledge of the following is also necessary:

- Fail-safe automation systems
- Automation systems

  - S7-300
  - S7-400
  - S7-1200
  - S7-1500
  - S7-1500H
  - S7-1500 Software Controller
  - SIMATIC Drive Controller
- Distributed I/O systems on

  - PROFIBUS DP
  - PROFINET IO
- Totally Integrated Automation Portal, including:

  - Hardware configuration with the hardware and network editor
  - Programming in the LAD and FBD programming languages using the program editor.
  - Communication between CPUs

#### Scope of this documentation

This documentation is valid for STEP 7 Safety Advanced V19 and STEP 7 Safety Basic V19.

STEP 7 Safety Advanced V19 and STEP 7 Safety Basic V19 are used for the configuration and programming of the fail-safe SIMATIC Safety system.

In this context, integration of the F-I/O listed below in SIMATIC Safety is also addressed:

- S7-1500/ET 200MP fail-safe modules
- ET 200SP fail-safe modules
- ET 200S fail-safe modules
- ET 200eco fail-safe I/O modules
- ET 200eco PN fail-safe I/O modules
- ET 200AL fail-safe I/O modules
- ET 200pro fail-safe modules
- ET 200iSP fail-safe modules
- S7-300 fail-safe signal modules
- S7-1200 fail-safe modules
- Fail-safe GSD based DP slaves
- Fail-safe GSD based I/O devices

#### Approvals

The SIMATIC Safety F-system is certified for use in safety mode up to:

- Safety Integrity Level SIL3 in accordance with IEC 61508:2010
- Performance Level (PL) e and category 4 in accordance with ISO 13849-1:2015 or EN ISO 13849-1:2015

#### Incorporation in the information landscape

Depending on your application, you will need the following supplementary documentation when working with STEP 7 Safety.

This documentation includes references to the supplementary documentation where appropriate.

| Documentation | Brief description of relevant content |
| --- | --- |
| For the SIMATIC Safety F-system | Depending on which F-CPU you are using, you will need the following documentation:  - For the F-CPUs S7-1200/1500, a [Product Information](http://support.automation.siemens.com/WW/view/en/109478599) describes all deviations from the respective standard CPUs. - Each F-CPU S7-300/400 that can be used has its own product information. The product information describes the deviations from the respective standard CPUs. - The [Device manuals](http://support.automation.siemens.com/WW/view/en/67295862/133300) describe the S7-1500 CPUs. - The ["S7-300, CPU 31xC and CPU 31x: Installation"](http://support.automation.siemens.com/WW/view/en/13008499) operating instructions describe the installation and wiring of S7-300 systems. - The ["CPU 31xC and CPU 31x, Technical Data"](http://support.automation.siemens.com/WW/view/en/12996906) device manual describes the CPUs 315-2 DP and PN/DP, the CPU 317-2 DP and PN/DP, and the CPU 319-3 PN/DP. - The ["S7-400 Automation System, Installation](http://support.automation.siemens.com/WW/view/en/1117849) installation manual describes the installation and wiring of S7-400 systems. - The ["S7-400 Automation System, CPU Data"](http://support.automation.siemens.com/WW/view/en/23904550) reference manual describes the CPUs 414-3 PN/DP, the CPU 416-2, and the CPU 416-3 PN/DP. - The ["ET 200S Interface Module IM 151-7 CPU"](http://support.automation.siemens.com/WW/view/en/12714722) manual describes the IM 151-7 CPU. - The ["ET 200S, Interface Module IM 151-8 PN/DP CPU"](http://support.automation.siemens.com/WW/view/en/47409312) manual describes the IM 151-8 PN/DP CPU. - The ["ET 200S, Interface Module IM 154-8 CPU"](http://support.automation.siemens.com/WW/view/de/24363739/0/en) manual describes the IM 154-8 CPU. - The "[SIMATIC S7-1500 Software Controller CPU 1505SP (F), CPU 1507S (F) and CPU 1508S (F) SIMATIC Industrial OS Version 30.0](https://support.industry.siemens.com/cs/ww/en/view/109808199)" manual describes the SIMATIC S7-1500 Software Controllers CPU 1505SP (F), CPU 1507S (F) and CPU 1508S (F). |
| "[S7-1200 Functional Safety manual](http://support.automation.siemens.com/WW/view/en/104547552)" system manual | Describes the F-CPUs S7-1200 and the fail-safe modules S7-1200 (including installation, wiring, and technical specifications) |
| "[S7-1500/ET200MP system manual](http://support.automation.siemens.com/WW/view/en/59191792)" system manual and the [product manuals](https://support.industry.siemens.com/cs/ww/en/ps/14141/man) for the corresponding S7-1500/ET 200MP fail-safe modules | Describes the hardware of the S7-1500 systems and the S7-1500/ET 200MP fail-safe modules (including installation, wiring, and technical specifications) |
| System manual "[Redundant System S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/109754833)" | Describes the hardware of S7-1500R/H systems (including design, wiring and technical specifications) |
| "[SIMATIC Drive Controller](https://support.industry.siemens.com/cs/ww/en/view/109766665)" system manual and "[SIMATIC Drive Controller](https://support.industry.siemens.com/cs/ww/en/view/109766666)" equipment manual | Describes the hardware of the SIMATIC Drive Controller (including design, wiring and technical specifications) |
| "[SIMATIC S7-1500 S7-PLCSIM Advanced](https://support.industry.siemens.com/cs/ww/en/view/109798879)" function manual | Describes the operation of S7-PLCSIM Advanced |
| "[ET 200SP distributed I/O system](http://support.automation.siemens.com/WW/view/en/58649293)" system manual and the [product manuals](https://support.industry.siemens.com/cs/ww/en/ps/14059/man) for the corresponding ET 200SP fail-safe modules | Describes the hardware of the ET 200SP fail-safe modules (including installation, wiring, and technical specifications) |
| "[ET 200eco Distributed I/O Station Fail-safe I/O Block](http://support.automation.siemens.com/WW/view/en/19033850)" manual | Describes the hardware of the ET 200eco fail-safe I/O module (including installation, wiring, and technical specifications) |
| Manual "[ET 200eco PN F-DI 8 x 24 VDC, 4xM12 / F-DQ 3 x 24 VDC/2.0A PM, 3xM12](https://support.industry.siemens.com/cs/ww/en/view/109765611)" | Describes the hardware of the ET 200eco PN fail-safe I/O module (including installation, wiring, and technical specifications) |
| System manual "[ET 200AL system manual](https://support.industry.siemens.com/cs/ww/en/view/89254965)" and equipment manual "Digital I/O Module F-DI 4+F-DQ 2x24VDC/2A, 4xM12" | Describes the hardware of the ET 200AL fail-safe I/O module (including installation, wiring, and technical specifications) |
| "[Distributed I/O System ET 200S, Fail-Safe Modules](http://support.automation.siemens.com/WW/view/en/27235629)" operating instructions | Describes the hardware of the ET 200S fail-safe modules (including installation, wiring, and technical specifications) |
| "[S7-300 Automation System, ET 200M Distributed I/O System, Fail-safe Signal Modules](http://support.automation.siemens.com/WW/view/en/19026151)" manual | Describes the hardware of the S7-300 fail-safe signal modules (including installation, wiring, and technical specifications) |
| "[Distributed I/O system ET 200pro, fail-safe I/O modules](http://support.automation.siemens.com/WW/view/en/22098524)" operating instructions | Describes the hardware of the ET 200pro fail-safe modules (including installation, wiring, and technical specifications) |
| "[ET 200iSP distributed I/O device - Fail-safe modules](http://support.automation.siemens.com/WW/view/en/47357221)" operating instructions | Describes the hardware of the ET 200iSP fail-safe modules (including installation, wiring, and technical specifications) |
| Help on STEP 7 | - Describes the operation of the standard tools in STEP 7 - Contains information regarding configuration and parameter assignment of hardware - Contains a description of the programming languages FBD and LAD |

#### Fail-safe modules Manual Collection

The Manual Collection contains all the documentation for the SIMATIC fail-safe modules collected into one file.

You can find the Manual Collection on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109806400).

#### Guide

This documentation describes how to work with STEP 7 Safety. It includes instructions and reference sections (description of the instructions for the safety program).

The following topics are addressed:

- Configuration of SIMATIC Safety
- Access protection for SIMATIC Safety
- Programming of the safety program (safety-related user program)
- Safety-related communication
- Instructions for the safety program
- Support for the system acceptance
- Operation and maintenance of SIMATIC Safety
- Monitoring and response times

#### Conventions

The following conventions apply:

- In this documentation, the terms "safety engineering" and "fail-safe engineering" are used synonymously. The same applies to the terms "fail-safe" and "F-".
- "F-systems" include redundant S7-1500HF systems. Special features and restrictions of H systems are described in the system manual "[Redundant S7-1500R/H system](https://support.industry.siemens.com/cs/ww/en/view/109754833)" and also apply to the redundant S7-1500HF systems.
- "STEP 7 Safety V19" stands for "STEP 7 Safety Advanced V19" and "STEP 7 Safety Basic V19".
- "(S7-300)" indicates that the section **only** applies to S7-300 F-CPUs. S7-300 F-CPUs also includes the F-CPUs ET 200S and ET 200pro (IM F-CPUs).
- "(S7-400)" indicates that the section **only** applies to S7-400 F-CPUs.
- "(S7-1200)" indicates that the section **only** applies to S7-1200 F-CPUs.
- "(S7-1500)" indicates that the section **only** applies to S7-1500 F-CPUs. S7-1500 F-CPUs also includes S7-1500 HF-CPUs, ET 200SP F-CPUs, the CPU 151xpro F-2 PN, the S7-1500 F Software Controller and the SIMATIC Drive Controller. In the case of exceptions, these are indicated.

The scopes can be combined.

The term **Safety program** refers to the fail-safe portion of the user program and is used instead of "fail-safe user program", "F‑program", etc. For purposes of contrast, the non-safety-related part of the user program is referred to as the "standard user program".

The **hardware configuration** includes the configuration of standard CPUs and standard I/Os as well as the configuration of F-CPUs and F-I/Os.

The **safety-related hardware configuration** includes the safety-related parameters of the F-CPUs and F-I/Os.

The **safety-related project data** includes the safety-related hardware configuration as well as the safety program.

> **Note**
>
> Each warning is marked with a unique number at the end of the text. This enables you to easily reference other documents, for example, to obtain an overview of the safety requirements for the system.

#### Additional support

If you have further questions about the use of products presented in this manual, contact your local Siemens representative.

You can find information on whom to contact on the [Web](http://www.siemens.com/automation/partner).

A guide to the technical documentation for the various SIMATIC products and systems is available on the [Web](http://www.siemens.com/simatic-tech-doku-portal).

You can find the online catalog and online ordering system on the [Web](http://www.siemens.com/industrymall).

#### Training center

We offer courses to help you get started with the S7 automation system. To do this, contact your regional training center or the central training center in Nuremberg, Germany.

You can find more information on the [Internet](http://www.sitrain.com).

#### Technical Support

To contact Technical Support for all Industry Automation products, use the Support Request [Web form](http://www.siemens.com/automation/support-request).

You can find more information about our Technical Support on the [Web](http://www.siemens.com/automation/service).

#### Important note for maintaining the operational safety of your system

> **Note**
>
> The operators of systems with safety-related characteristics must adhere to operational safety requirements. The supplier is also obliged to comply with special product monitoring measures. Siemens informs system operators in the form of personal notifications about product developments and properties which could be or become important issues in terms of operational safety.
>
> You should subscribe to the corresponding notifications in order to obtain the latest information and to allow you to make any necessary modifications to your system.
>
> Log in to the Industry Online Support. Follow the links below and click on "Email on update" on the right-hand side in each case:
>
> - [SIMATIC S7-300/S7-300F](https://support.industry.siemens.com/cs/products?pnid=13751&lc=en-WW)
> - [SIMATIC S7-400/S7-400H/S7-400F/FH](https://support.industry.siemens.com/cs/products?pnid=13828&lc=en-WW)
> - [SIMATIC S7-1500/SIMATIC S7-1500F/SIMATIC S7-1500HF](https://support.industry.siemens.com/cs/products?pnid=13716&lc=en-WW)
> - [SIMATIC S7-1200/SIMATIC S7-1200F](https://support.industry.siemens.com/cs/products?pnid=13683&lc=en-WW)
> - [Software Controller](https://support.industry.siemens.com/cs/products?pnid=13911&lc=en-WW)
> - [Distributed I/O](https://support.industry.siemens.com/cs/products?pnid=14029&lc=en-WW)
> - [STEP 7 (TIA Portal)](https://support.industry.siemens.com/cs/products?pnid=14340&lc=en-WW)

### Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines, and networks.

In order to protect plants, systems, machines, and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens’ products and solutions constitute one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For more information on protective industrial cybersecurity measures for implementation, please [visit](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Siemens' products and solutions undergo continuous development to make them more secure. Siemens strongly recommends that product updates are applied as soon as they are available and that the latest product versions are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase customers' exposure to cyber threats.

To stay informed about product updates at all times, subscribe to the Siemens Industrial Cybersecurity RSS Feed [under](https://new.siemens.com/global/en/products/services/cert.html).

### Siemens Industry Online Support

You can find current information on the following topics quickly and easily here:

- **Product support**

  All the information and extensive know-how on your product, technical specifications, FAQs, certificates, downloads, and manuals.
- **Application examples**

  Tools and examples to solve your automation tasks – as well as function blocks, performance information and videos.
- **Services**

  Information about Industry Services, Field Services, Technical Support, spare parts and training offers.
- **Forums**

  For answers and solutions concerning automation technology.
- **mySupport**

  Your personal working area in Industry Online Support for messages, support queries, and configurable documents.

This information is provided by the Siemens Industry Online Support in the [Internet](http://www.siemens.com/automation/service&support).

### Industry Mall

The Industry Mall is the catalog and order system of Siemens AG for automation and drive solutions on the basis of Totally Integrated Automation (TIA) and Totally Integrated Power (TIP).

Catalogs for all the products in automation and drives are available on the [Internet](https://mall.industry.siemens.com).

## Product Overview

This section contains information on the following topics:

- [Overview](#overview)
- [Hardware and Software Components](#hardware-and-software-components)
- [Installing/uninstalling the STEP 7 Safety Basic V19 license](#installinguninstalling-the-step-7-safety-basic-v19-license)
- [Installing/uninstalling the STEP 7 Safety Advanced V19 license](#installinguninstalling-the-step-7-safety-advanced-v19-license)
- [Installing/uninstalling STEP 7 Safety PowerPack](#installinguninstalling-step-7-safety-powerpack)
- [Migrating projects from S7 Distributed Safety V5.4 SP5 to STEP 7 Safety Advanced](#migrating-projects-from-s7-distributed-safety-v54-sp5-to-step-7-safety-advanced)
- [Migrating PLC programs to a n F-CPU S7-1500](#migrating-plc-programs-to-a-n-f-cpu-s7-1500)
- [Upgrading projects to STEP 7 Safety V19](#upgrading-projects-to-step-7-safety-v19)
- [First steps](#first-steps)

### Overview

#### SIMATIC Safety fail-safe system

The SIMATIC Safety fail-safe system is available to implement safety concepts in the area of machine and personnel protection (for example, for emergency STOP devices for machining and processing equipment) and in the process industry (for example, for implementation of protection functions for safety devices of instrumentation and controls and of burners).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The SIMATIC Safety F-system is used to control processes that reach their safe state immediately through shutdown. This also applies in particular to redundant S7-1500HF systems.  SIMATIC Safety may only be used for controlling processes in which a shutdown does not pose a danger to humans or the environment.  When realizing safety applications including the creation of the safety-related project data you have to take into consideration the standards, directives and guidelines relevant for your application. In particular include standards in which the software creation process is described (for example IEC 61508-3 or ISO 13849-1). (S062) |  |

#### Achievable safety requirements

SIMATIC Safety F-systems can satisfy the following safety requirements:

- Safety Integrity Level SIL3 in accordance with IEC 61508:2010
- Performance Level (PL) e and category 4 in accordance with ISO 13849-1:2015 or EN ISO 13849-1:2015

#### Functional safety in SIMATIC Safety

Functional safety is implemented primarily in the software. The SIMATIC Safety F-System brings the plant into a safe state in the event of a hazardous event and maintains this state. Safety mechanisms are contained mainly in the following components:

- In the safety-related user program (safety program) in the F-CPU
- In the fail-safe inputs and outputs (F-I/O)

The F‑I/O ensure the safe processing of field information (sensors: e.g. emergency STOP pushbutton, light barriers; actuators, e.g. for motor control). They have all of the required hardware and software components for safe processing, in accordance with the required Safety Integrity Level. The user only has to program the user safety function. Functional safety for the process can be provided by a user safety function or a fault reaction function. The F-system cyclically checks the integrity of the safety program and the safety-related data. This check is generally always performed when safety-related data leaves an F-runtime group via safety-related communication or F-I/O access. If this check detects a fault, the F-system executes the fault reaction function, which switches off the associated outputs and, if necessary, sets the F-CPU to STOP.

> **Note**
>
> If the F-CPU switches to STOP mode due to a fault reaction function, with a redundant S7-1500HF system, it leads to the STOP of the primary CPU **and** the backup CPU.

#### Example of user safety function and fault reaction function

In the event of overpressure, the F-system will open a valve (user safety function). In the event of a hazardous fault in the F‑CPU, all outputs are deactivated (fault reaction function), whereby the valve is opened, and the other actuators also attain a safe state. For a non-faulty F-system, only the valve would be opened.

### Hardware and Software Components

#### Hardware and software components of SIMATIC Safety

The following schematic diagram provides an overview of the hardware and software components required to configure and operate a SIMATIC Safety F-system.

![Hardware and software components of SIMATIC Safety](images/166654088203_DV_resource.Stream@PNG-en-US.png)

#### Hardware components for PROFIBUS DP

You can use the following fail-safe components in SIMATIC Safety F-systems on PROFIBUS DP:

- F-CPUs with DP interface, such as CPU 1516F‑3 PN/DP
- SIMATIC Drive Controller, for example, CPU 1504D TF
- Fail-safe inputs and outputs (F‑I/O), such as:

  - S7‑300 fail-safe signal modules in ET 200M
  - S7-1500/ET 200MP fail-safe modules
  - ET 200SP fail-safe modules
  - ET 200S fail-safe modules
  - ET 200pro fail-safe modules
  - ET 200iSP fail-safe modules
  - Fail-safe I/O modules ET 200eco (S7-300, S7-400)
  - Fail-safe GSD based DP slaves (light array, laser scanner, etc.)

You have the option to expand the configuration with standard I/O.

The following CPs/CMs can be used in a SIMATIC Safety F-system on PROFIBUS DP for connection to distributed F-I/O:

- CP 443‑5 Extended
- CM 1243-5
- CM 1542-5
- CP 1542-5
- SP CM DP

#### Hardware components for PROFINET IO

You can use the following fail-safe components in SIMATIC Safety F-systems on PROFINET IO:

- F‑CPUs with PN interface, e.g. CPU 1214FC DC/DC/DC
- SIMATIC Drive Controller, for example, CPU 1504D TF
- Fail-safe inputs and outputs (F‑I/O), such as:

  - S7‑300 fail-safe signal modules in ET 200M
  - S7-1500/ET 200MP fail-safe modules
  - ET 200SP fail-safe modules
  - ET 200S fail-safe modules
  - ET 200pro fail-safe modules
  - ET 200eco PN fail-safe I/O modules
  - ET 200AL fail-safe I/O modules
  - Fail-safe GSD based I/O devices (light array, laser scanner, etc.)

You have the option to expand the configuration with standard I/O.

The following CPs/CMs can be used in a SIMATIC Safety F-system on PROFINET IO for connection to distributed F-I/O:

- CP 443‑1
- CP 443‑1 Advanced‑IT
- CM 1542-1

#### Hardware components for central configuration

You can use the following fail-safe components in SIMATIC Safety F-systems centrally on an F-CPU (not HF-CPU):

- S7‑300 fail-safe signal modules
- S7-1200 fail-safe modules
- S7-1500 fail-safe modules
- ET 200SP fail-safe modules
- ET 200S fail-safe modules
- ET 200pro fail-safe modules (can also be used with CPU 1516proF-2)

You have the option to expand the configuration with standard I/O.

#### STEP 7 Safety

This documentation describes STEP 7 Safety Advanced V19 and STEP 7 Safety Basic V19. STEP 7 Safety is the configuration and programming software for the SIMATIC Safety F-system. With STEP 7 Safety, you receive the following:

- The support for configuring the F‑I/O in the hardware and network editor of TIA Portal
- The support for creating the safety program using LAD and FBD and integrating error detection functions into the safety program
- Instructions for programming your safety program in LAD and FBD, which you are familiar with from the standard user programs
- Instructions for programming your safety program in LAD and FBD with special safety functions

Moreover, STEP 7 Safety offers functions for comparing safety programs and for assisting you with the system acceptance.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The configuration of F-CPUs and F-I/Os as well as the programming of F-blocks must be carried out in TIA Portal as described in this documentation.You must observe all aspects described in the section [System acceptance](#system-acceptance) to ensure safe operation with the SIMATIC Safety F-system. Any other procedures are not permitted. (S056) |  |

#### Optional packages

In addition to the STEP 7 Safety, you can use optional packages with F-I/O and F-CPUs and use instructions for programming your safety program with special safety functions within the SIMATIC Safety F-system. For example, SINUMERIK or Failsafe HMI Mobile Panels.

The installation, parameter assignment and programming as well as what is important to note during system acceptance, is described in the documentation for the specific optional packages.

Also read the notes in "[Configurations supported by the SIMATIC Safety F-system](#configurations-supported-by-the-simatic-safety-f-system)".

#### TIA Portal Cloud Connector

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Use of the TIA Portal Cloud Connector is only intended for engineering work with TIA Portal. This means online access in productive operation (e.g. SCADA) is not permitted. This is particularly true for safety programs. (S068) |  |

#### Openness

[Openness](https://support.industry.siemens.com/cs/ww/en/view/109798533) as part of STEP 7 Safety is supported with the functions listed below. The use of Openness in productive operation is not permitted.

As part of STEP 7 Safety the following is supported:

- Inserting / removing F-CPUs and F-I/Os
- Copying / deleting F-CPUs and F-I/Os from templates
- Compiling hardware
- Compiling software (incl. safety program)
- Handling access protection for the safety-related project data (for TIA projects not protected by project protection)
- Reading/configuring F-parameters of the F-CPU (for S7-1500 F-CPUs)
- Reading/configuring F-parameters of F-I/O
- Reading/configuring i-parameters of F-I/O (for ET 200SP, ET 200AL, ET 200MP, ET 200eco PN, ET 200pro)
- Downloading safety-related project data to a SIMATIC Memory Card or storing it in a file folder
- Reading, declaring or deleting fail-safe tags in the PLC tag table
- Updating projects to the latest type versions of F-blocks
- Consistent station upload
- Export and import of F-blocks and F-compliant PLC data types (UDT)
- Comparison of hardware and software
- Version control interface (VCI) support
- Reading out PLC online fingerprint for the safety program
- Storing safety-related project data as a PC System Configuration file

The following are not supported.

- Downloading to device

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using Openness or other tools for operating the TIA Portal in combination with safety-related project data, integrity of the data must be ensured (for example, as part of the save or transfer functions of "Source Code Management" applications). If there is a connection of external tools, the requirements for offline support tools according to IEC 61508-3 must be observed. A violation of the integrity of the safety-related project data either offline or online cannot be detected by STEP 7 Safety. A final verification of the correctness of the safety-related project data has to be carried out as described in the section [System acceptance](#system-acceptance). (S070) |  |

Openness programs can also be integrated into TIA Portal as an add-in. It is also possible to include so-called workflow add-ins, which are automatically called before a safety program is compiled. See "Extending workflows" in the standard help.  
If you have integrated such a workflow add-in, this is output in the safety summary.

#### Openness service

The Openness interface (Siemens.Engineering.dll) has been expanded to include the following services:

- `GlobalSettings` (see name area **Siemens.Engineering.Safety**) which provides the following actions:

  - `SafetyModificationsPossible(bool safetyModificationsPossible)`
  - `UsernameForFChangeHistory(string userName)`
  - `bool SafetyModificationsPossible()`
  - `string UsernameForFChangeHistory()`
- `SafetySignatureProvider` which provides the following actions and properties:

  - `SafetySignatureComposition Signatures`
  - `UInt64 SafetySignature.Value`
  - `SafetySignatureType SafetySignature.Type`
- `SafetyAdministration` with the following actions and properties in the name area **Siemens.Engineering.Safety**.

  - `bool IsSafetyOfflineProgramPasswordSet`
  - `void SetSafetyOfflineProgramPassword(SecureString newPassword)`
  - `void RevokeSafetyOfflineProgramPassword(SecureString currentPassword)`
  - `bool IsLoggedOnToSafetyOfflineProgram`
  - `void LoginToSafetyOfflineProgram(SecureString currentPassword)`
  - `void LogoffFromSafetyOfflineProgram()`
- `Safety Administration`, which can be accessed from the `PLc-DeviceItem`.

  The `SafetyAdministration` service offers the following properties in the **Siemens.Engineering.Safety** namespace. These two properties include additional properties that are listed in the description.

  - `RuntimegroupComposition RuntimeGroups { get; }`
  - `SafetySettings Settings { get; }`
- `SafetyPrintout` with the following action in the name area **Siemens.Engineering.Safety**:

  - `bool Print(SafetyPrintoutFilePrinter filePrinter, FileInfo fullOutputPath, SafetyPrintoutOption documentationOption, string documentLayout);`

You can find more information in the System Manual "[SIMATIC TIA Portal Openness: Automating creation of projects](https://support.industry.siemens.com/cs/ww/en/view/109798533)" in the section "F-specific openness".

#### Virtual environments

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Use of virtual environments in the engineering system**  Note that a hypervisor or a client software of a hypervisor is not permitted to perform any function that reproduces recorded message frame sequences with correct time response in a network with real F-CPUs and F-I/Os.  Make sure that this condition is met, for example, when using the following functions:  - Reset of captured statuses (snapshots) of the virtual machines (VMs) - Suspending and resuming the VMs - Replay of recorded sequences in the VMs - Moving VMs between hosts in productive operation (e.g. Fault Tolerance (FT)) - Digital twins of VMs in the virtual environment   If in doubt, disable these functions in the settings (Hypervisor administration console). (S067) |  |

#### Operating system installations with S7-150xS(P) F

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using a PC with multiple Windows or Linux operating system installations (e.g. via boot manager), only one S7-150xS(P) may be installed on this PC. (S095) |  |

#### Safety program

You can create a safety program using the program editor. You can program fail-safe FBs and FCs in the FBD or LAD programming languages using the instructions from STEP 7 Safety and create fail-safe DBs.

Safety checks are automatically performed and additional fail-safe blocks for error detection and fault reaction are inserted when the safety program is compiled. This ensures that failures and errors are detected and appropriate reactions are triggered to maintain the F-system in the safe state or bring it to a safe state.

In addition to the safety program, a standard user program can be run on the F-CPU. A standard program can coexist with a safety program in an F‑CPU because unintentional influencing of the safety-related data of the safety program is uncovered by the standard user program.

Data can be exchanged between the safety program and the standard user program in the F-CPU by means of bit memory or data of a standard DB or by accessing the process image input and output.

Note possible restrictions/particularities when using Software Units or a [Safety Unit](#safety-program-in-software-unit-safety-unit-s7-1500).

---

**See also**

[Data Transfer from the Safety Program to the Standard User Program](#data-transfer-from-the-safety-program-to-the-standard-user-program)

### Installing/uninstalling the STEP 7 Safety Basic V19 license

After the installation of the STEP 7 Safety Basic V19 license, the functional scope of STEP 7 Safety Basic V19 is available to you.

#### Software requirements for STEP 7 Safety Basic V19

At a minimum, the following software package must be installed on the programming device or PC:

- SIMATIC STEP 7 Basic V19

#### Installing the STEP 7 Safety Basic V19 license

1. Start the Automation License Manager on the programming device/PC on which the "SIMATIC STEP 7 Basic V19" or "SIMATIC STEP 7 Advanced V19" software package is installed.
2. Install the STEP 7 Safety Basic V19 license as described in the Automation License Manager help.

#### Uninstalling the STEP 7 Safety Basic V19 license

To uninstall the STEP 7 Safety Basic V19 license, proceed as described in the Automation License Manager help.

### Installing/uninstalling the STEP 7 Safety Advanced V19 license

After the installation of the STEP 7 Safety Advanced V19 license, the functional scope of STEP 7 Safety Advanced V19 is available to you.

#### Software requirements for STEP 7 Safety Advanced V19

At a minimum, the following software package must be installed on the programming device or PC:

- SIMATIC STEP 7 Professional V19

#### Installing the STEP 7 Safety Advanced V19 license

1. Start the Automation License Manager on the programming device/PC on which the "SIMATIC STEP 7 Professional V19" software package is installed.
2. Install the STEP 7 Safety Advanced V19 license as described in the Automation License Manager help.

#### Uninstalling the STEP 7 Safety Advanced V19 license

To uninstall the STEP 7 Safety Advanced V19 license, proceed as described in the Automation License Manager help.

### Installing/uninstalling STEP 7 Safety PowerPack

After the installation of the STEP 7 Safety PowerPack the functional scope of STEP 7 Safety Advanced V19 is available to you.

#### Software requirements for STEP 7 Safety PowerPack

At a minimum, the following software package must be installed on the programming device or PC:

- SIMATIC STEP 7 Professional V19

#### Installing STEP 7 Safety PowerPack

1. Start the Automation License Manager on the programming device/PC on which the "SIMATIC STEP 7 Professional V19" software package is installed.
2. Install the license included in the STEP 7 Safety PowerPack as described in the Automation License Manager help.

#### Uninstalling STEP 7 Safety PowerPack

To uninstall the license included in the STEP 7 Safety PowerPack, proceed as described in the Automation License Manager help.

### Migrating projects from S7 Distributed Safety V5.4 SP5 to STEP 7 Safety Advanced

#### Introduction

In STEP 7 Safety Advanced, you can continue to use projects with safety programs that you created with S7 Distributed Safety V5.4 SP5.

#### Requirement

STEP 7 Safety Advanced, S7 Distributed Safety V5.4 SP5, and the F-Configuration Pack used to create the project must all be installed on the computer you are using for migration. The F-Configuration PackV5.4 SP5 to V5.5 SP13 is supported.

**To that end, the projects must have been compiled in** 
S7 Distributed Safety V5.4 SP5
 **and with the** 
F-Configuration Pack
**.**

#### Prior to migration

Delete all F-blocks not required by the safety program in your S7 Distributed Safety V5.4 SP5 project prior to migration.

#### Procedure as in STEP 7 Professional

Proceed just as you would for standard projects to migrate projects from S7 Distributed Safety V5.4 SP5 to STEP 7 Safety Advanced. Once the migration is complete, you should verify using the Collective F-Signature whether the project was migrated unchanged.

> **Note**
>
> If you use the safety program to migrate F-blocks with know-how protection, remove the know-how protection prior to migration.
>
> You can assign the F-blocks know-how protection again once the migration is completed.

This migration approach is described in the "Migration" section of the STEP 7 Professional Help. Special considerations about STEP 7 Safety Advanced are described below.

> **Note**
>
> We recommend that you enable the "Include hardware configuration" option in the "Migrating project" window.

#### Older hardware versions

Older versions of F-hardware may not be supported by STEP 7 Safety Advanced .

If you have used and configured versions of F‑CPUs and F‑I/O in S7 Distributed Safety projects that are not approved for STEP 7 Safety Advanced, you will need to upgrade this hardware to the new version in S7 Distributed Safety V5.4 SP5 and the corresponding F-Configuration Pack. Once the upgrade is completed, migration to STEP 7 Safety Advanced is feasible. A Product Information with a list of approved hardware is available on the [Internet](https://support.industry.siemens.com/cs/ww/de/view/109481784):

#### Particularities for safety-related CPU-CPU communication via S7 connections

You can find information about the special considerations for migrated projects with safety-related CPU-CPU communication via S7 connections in [Safety-related communication via S7 connections](#safety-related-communication-via-s7-connections). Also note [Communication with S7 Distributed Safety via S7 connections](#communication-with-s7-distributed-safety-via-s7-connections).

#### Particularities for ESTOP1 or FDBACK instructions

Information on the special considerations when using the ESTOP1 and FDBACK instructions can be found in the "Instruction versions" section in [ESTOP1: Emergency STOP/OFF up to stop category 1 (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#estop1-emergency-stopoff-up-to-stop-category-1-step-7-safety-v19) and [FDBACK: Feedback circuit monitoring (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#fdback-feedback-circuit-monitoring-step-7-safety-v19).

#### Post-migration procedures

Once migration is complete, you have a complete project with a safety program which has retained the program structure of S7 Distributed Safety and the Collective F-Signature. F-blocks from the S7 Distributed Safety F-library (V1) are converted into instructions that are provided by STEP 7 Safety Advanced.

The migrated project therefore does not need to be re-accepted; it can be loaded as is to the F-CPU as long as it has not been modified or compiled since migration.

> **Note**
>
> **Safety summary**
>
> You cannot create a safety summary for a migrated project in STEP 7 Safety Advanced. The printout of the project created with S7 Distributed Safety V5.4 SP5 and the corresponding acceptance documents are still valid, because the Collective F-Signature has been retained.

#### Compiling of the migrated hardware configuration

If you receive an error message after migration and subsequent compilation of the hardware configuration stating that the F-source address does not match the "Central F-source address" parameter of the F-CPU, change the "Central F-source address" parameter.   
The F-source addresses of all F-I/Os assigned to the F-CPU are reassigned in the process.

If after migration of an SM 326; DI 24 x DC 24V (6ES7 326-1BK01-0AB0 and 6ES7 326-1BK02-0AB0) and subsequent compilation of the hardware configuration, the error message "F_IParam_ID_1: Value outside the permitted range" is displayed, delete the F-SM and reinsert it.

In both cases, subsequent compilation of the safety program is required.

#### Compiling the migrated safety programs

As a result of compilation of the migrated project with STEP 7 Safety Advanced, the existing program structure (with F-CALL) is converted to the new program structure of STEP 7 Safety Advanced (with main safety block). This changes the Collective F-Signature and the safety program has to be validated and acceptance may have to be carried out again.

(S7-300, S7-400) You must call up the main safety block according to the F-CALL from an arbitrary block of the standard user program. We recommend a call from an OB 3x.

> **Note**
>
> During the first-time compiling of the migrated safety program the call of the F-CALL is replaced automatically by a call of the main safety block, if the calling block of the F-CALL was created using the programming language LAD, FBD or STL.

> **Note**
>
> **Changing the Safety system version**
>
> Before compiling with STEP 7 Safety Advanced for the first time, you must change the safety system version to a version which is not equal to 1.0 in the "Settings" area of the Safety Administration Editor. We recommend that you use the highest available version.

> **Note**
>
> **Using the latest version of instructions**
>
> If you want to expand the migrated safety program, we recommend that you update to the latest version of the instructions used before compiling with STEP 7 Safety Advanced for the first time. Read the information on instruction versions for each instruction.

> **Note**
>
> Note that compiling the migrated safety program extends the runtime of the F-runtime group(s) and increases the memory requirements of the safety program (see also [Excel file for calculating response time](https://support.industry.siemens.com/cs/ww/en/view/109783831)).

---

**See also**

[Application example "Migration of a safety program to TIA Portal"](https://support.industry.siemens.com/cs/ww/en/view/109475826)

### Migrating PLC programs to a n F-CPU S7-1500

To migrate an F-CPU S7-300/400 onto an F-CPU S7-1500, proceed as with the migration of a standard CPU S7-300/400 onto a CPU S7-1500.

Points to note after migration:

- Non-automatable actions

  - Creating an F-runtime group and assigning it to the main safety block.
  - The hardware configuration including the I/O of the initial F-CPU is not automatically transferred to an S7-1500 F-CPU. Implement the hardware configuration of the new CPU manually after migration.

    Please also read the sections "Specify F-destination address for F-I/O of PROFIsafe address type 1" and "Specify F-destination address for F-I/O of PROFIsafe address type 2“ in chapter "[Configuring an F-CPU](#configuring-an-f-cpu)“. Otherwise, this can lead to a reassignment of the F-destination addresses in the configuration.
  - When using F-I/Os with PROFIsafe Protocol Version = Expanded Protocol (XP) (for example S7-1500/ET 200MP F-modules) keep in mind that you need one byte more in the address area of S7-1200/1500 F-CPUs than in S7-300/400 F-CPUs.
  - Replacement of the OV instruction by the connection of the ENO output for [mathematical functions](STEP%207%20Safety%20V19%20instructions.md#math-functions).
  - Replacement of the RD_FDB instruction by the instructions [RD_ARRAY_I](STEP%207%20Safety%20V19%20instructions.md#rd_array_i-read-value-from-int-f-array-step-7-safety-v19-s7-1500) and [RD_ARRAY_DI](STEP%207%20Safety%20V19%20instructions.md#rd_array_di-read-value-from-dint-f-array-step-7-safety-v19-s7-1500).
  - Replacement of the F-runtime group communication through [Communication via Flexible F-Link](#f-runtime-group-communication-s7-1200-s7-1500).
- Instructions not supported:

  - MUTING
  - TWO_HAND
  - WR_FDB
  - OPN
  - SENDS7
  - RCVS7
- Data types not supported

  - DWORD
- Changes to safety program programming

  - F_GLOBDB.VKE0/1 replaced by [FALSE/TRUE](#restrictions-in-the-programming-languages-fbdlad).
  - Readable values from the F_GLOBDB replaced by the F-runtime group information DB. Additional information is available under [F-shared DB (S7-300, S7-400)](#f-shared-db-s7-300-s7-400) and [F-runtime group information DB (S7-1200, S7-1500)](#f-runtime-group-information-db-s7-1200-s7-1500).
  - Replacement of the QBAD_I_xx or QBAD_O_xx tag by the value status. Additional information is available under [Value status (S7-1200, S7-1500)](#value-status-s7-1200-s7-1500) and [F‑I/O DB](#f-io-db).
- New naming convention when naming the F-I/O DBs
- Modified behavior of [QBAD and PASS_OUT](#qbadpass_outdisabledqbad_i_xxqbad_o_xx-and-value-status) tags for F-I/O with "RIOforFA safety" profile.

Compile the safety program and eliminate any compilation errors displayed.

> **Note**
>
> A new acceptance must be carried out following F-CPU migration.

---

**See also**

[Programming](#programming)

### Upgrading projects to STEP 7 Safety V19

This section contains information on the following topics:

- [Upgrading projects from STEP 7 Safety V18 SP1 to V19](#upgrading-projects-from-step-7-safety-v18-sp1-to-v19)
- [Upgrading projects from STEP 7 Safety as of V14 SP1 to V19](#upgrading-projects-from-step-7-safety-as-of-v14-sp1-to-v19)
- [Upgrading projects from STEP 7 Safety V13 SP1/SP2 to V19](#upgrading-projects-from-step-7-safety-v13-sp1sp2-to-v19)
- [Upgrading projects from STEP 7 Safety prior to V13 SP1](#upgrading-projects-from-step-7-safety-prior-to-v13-sp1)

#### Upgrading projects from STEP 7 Safety V18 SP1 to V19

If you have created your project with STEP 7 Safety V18 SP1 and have stored the safety program in a Safety Unit in this project, you must upgrade the project and then re-create the safety summary, which replaces the safety summary created with STEP 7 Safety V18 SP1. This is required for the SENDDP and RCVDP instructions in the "System library elements used in safety program" section to be displayed correctly.

#### Upgrading projects from STEP 7 Safety as of V14 SP1 to V19

If you want to continue working with a project from STEP 7 Safety as of V14 SP1, you must first upgrade the project to STEP 7 Safety V19.

Perform the upgrade following the usual procedure for STEP 7. After upgrading to V19, you must compile your safety program.

If you have upgraded and compiled a project <= V17 to V19, the collective F-signature remains the same, but the version comparison between the online and offline programs shows a change. Here, follow the procedure described in section "[Identity of online and offline program](#identity-of-online-and-offline-program)".

Keep in mind that existing change histories are not upgraded. All previous entries are deleted after the upgrade. If required, print out the change log before you upgrade.

#### Upgrading projects from STEP 7 Safety V13 SP1/SP2 to V19

If you want to continue to work with a project from STEP 7 Safety V13 SP1, you must first upgrade the project to STEP 7 Safety V19.

Perform the upgrade following the usual procedure for STEP 7. After upgrading to V19, you must compile your safety program.

(S7-300, S7-400): After compilation, the safety program is consistent and the Collective F-Signature of the upgraded safety program corresponds to the Collective F-Signature of the safety program from V13 SP1. Acceptance of changes is not required

(S7-1200, S7-1500): After compiling, your safety program is consistent and the Collective F-Signature of the upgraded safety program has changed for system reasons. The new collective F-signature of the safety program with STEP 7 Safety V19 replaces the former collective F-signature of the safety program with STEP 7 Safety V13 SP1.

You can find an overview of all system-related changes under "Common data/Protocols/F-Convert Log+CPU name+time stamp". One of the system-related changes is that STEP 7 Safety V19 automatically replaces versions of instructions no longer supported with new, functionally identical versions. The overview contains a comparison of the previous signatures with STEP 7 Safety V13 SP1 to the new signatures with STEP 7 Safety V19 and displays the automatically changed instruction versions. Print out the overview and store this printout with your acceptance documents or your machine documentation. Change acceptance is not required, since the "Collective F-Signature with STEP 7 Safety V13 SP1" contained in the overview matches the Collective F-Signature in your current acceptance documents.

Keep in mind that existing change histories are not upgraded. All previous entries are deleted after the upgrade. If required, print out the change log before you upgrade.

##### Special features for user acknowledgment and reintegration of F-I/O after F-I/O or channel faults and PASS_ON = 1 (S7-1200, S7-1500)

The following applies to F-I/Os:

- S7-300 fail-safe signal modules
- ET 200SP fail-safe modules
- ET 200S fail-safe modules
- ET 200pro fail-safe modules
- ET 200iSP fail-safe modules

You must take into account the changed behavior for user acknowledgment and reintegration if you have configured "Behavior after channel fault" = "Passivate channel" for the F-parameter and set the ACK_NEC tag in the F-I/O DB to 1. The behavior was adapted to the behavior when configuring "Behavior after channel fault" = "Passivate the entire module":

As of STEP 7 Safety V14 or higher, user acknowledgment of a corrected F-I/O or channel fault is **possible** even when the tag PASS_ON (F-I/O DB) = 1. A reintegration (provision of process values) takes place **as soon as the tag PASS_ON = 0**.

Until STEP 7 Safety V13 SP1, user acknowledgment of a corrected F-I/O or channel fault was **not possible** as long as the tag PASS_ON (F-I/O DB) = 1. A user acknowledgment was only possible once the tag PASS_ON = 0. The reintegration (provision of process values) took place immediately after the user acknowledgment.

##### Special features when using instruction profiles

If you want to use an instruction profile in your project from STEP 7 Safety V13 SP1, delete the instruction profile before you upgrade to STEP 7 Safety V19. Before deleting, make a note of your settings. After upgrading create a new instruction profile, if required, and enter the noted settings there, if applicable. Note that some instruction versions are no longer supported under STEP 7 Safety V19. You will find more information about the supported instruction versions in the description of the respective instruction.

#### Upgrading projects from STEP 7 Safety prior to V13 SP1

If you want to upgrade from a project **prior to**STEP 7 Safety V13 SP1 to STEP 7 Safety V19, you must upgrade the project as in Standard to STEP 7 Safety V13 SP1 via an intermediate step.

The safety program signature does not change after upgrading the safety program to STEP 7 Safety V13 SP1. Acceptance of changes is therefore not required.

Perform the upgrade following the usual procedure for STEP 7 Professional.

When upgrading a project that was created with STEP 7 Safety Advanced V11 . note the following information:

> **Note**
>
> Adjustments are required before you can continue working on a project upgraded from STEP 7 Safety Advanced V11:
>
> There was a product warning for STEP 7 Safety Advanced V11 regarding setting the parameters "Discrepancy behavior" and "Reintegration after discrepancy error" for the fail-safe digital input and output modules 4F-DI/3F-DO DC24V/2A (6ES7138-4FC01-0AB0, 6ES7138-4FC00-0AB0). These parameters could be displayed incorrectly in certain combinations.
>
> Based on the instructions in this product warning, you used a conversion table to set the affected parameters in such a way that they were displayed incorrectly in the safety summary and hardware configuration in order for them to have the correct effect in the F-module. You also corrected the safety summary to document the actual behavior of F-modules.
>
> To reverse these changes, follow these steps:
>
>
>
> 1. Compile the upgraded project with STEP 7 Safety Advanced V13 SP1. An error message is displayed for each F-module in STEP 7 Safety Advanced V11 the parameters of which you have corrected: "The CRC (F_Par_CRC) of the module (xxx) does not match the calculated value (yyy)."
> 2. Adapt the parameter assignment for each F-module for which this error message is displayed based on your corrections in the safety summary.
> 3. Do this for each F-CPU and then compile the safety program.
> 4. If, after compilation, the Collective F-signature matches the Collective F-signature in the safety summary, you have made all the necessary corrections.

##### Use of CPs

F-I/Os operated downstream from a CP443-5 Extended, CP443-1 or CP 443-1 Advanced-IT were not automatically assigned a unique F-destination address.

As soon as you compile the hardware in a project with such F-I/Os in STEP 7 Safety V13 SP1, you are notified for the affected F-I/Os. You have to assign new, unique F-destination addresses for the reported F-I/Os. More information is available under [PROFIsafe addresses for F-I/O of PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1), [PROFIsafe addresses for F-I/O of PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2) and [Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices](#peculiarities-when-configuring-fail-safe-gsd-based-dp-slaves-and-fail-safe-gsd-based-io-devices).

This changes the Collective F-Signature of the safety program. Because the Collective F-SW-Signature is unchanged, it is documented that the safety program has remained unchanged. The changed Collective F-HW-Signature indicates that the safety-related hardware configuration has changed. You can now verify that solely the changed F-destination addresses have caused this change:

- The F-parameter signature (without address) for each changed F-I/O remains the same.
- Only the affected F-I/O DBs are listed in the comparison editor of the safety program with the filter set to "Compare only F-blocks relevant for certification".

##### Changed names of F-I/O DBs

Prior to STEP 7 Safety V13 SP1 it was possible to change the name of an F-I/O DB. This change results in a changed Collective F-Signature during upgrading.

If a changed Collective F-Signature is unwanted during upgrading, follow these steps:

1. Under STEP 7 Safety V13, rename the changed names of the F-I/O DBs back to the original names.
2. Compile the safety program.

   The Collective F-Signature does not change as a result.
3. Perform an offline-offline comparison between the upgraded program and the program compiled in step 2.
4. Create a [comparison printout](#comparing-safety-programs) (electronic/paper form).

   Use the comparison printout to ensure that you have only changed the names of the F-F-I/O DBs.
5. Upgrading the safety program to STEP 7 Safety V13 SP1. After upgrading, the safety program has the Collective F-Signature from step 2.

### First steps

#### Getting Started in SIMATIC Safety

Three Getting Started documents are available to help you begin using SIMATIC Safety.

The Getting Started documentation is an instruction manual that provides a step-by-step description of how to create a project with SIMATIC Safety. It gives you the opportunity to quickly become familiar with the scope of features of SIMATIC Safety.

#### Contents

The Getting Started documentation describes the creation of a single, continuous project that is extended with each section. Based on the configuration, you program a fail-safe shutdown, make changes to the programming, and accept the system.

In addition to the step-by-step instructions, the Getting Started documentation also gives you background information for every new topic, which explains the functions used in more detail and how they interrelate.

#### Target audience

The Getting Started documentation is intended for beginners but is also suitable for users who are switching from S7 Distributed Safety.

#### Download

Three Getting Started documents are available as PDF files for free download in the Industry Online Support:

- [STEP 7 Safety Advanced V11 with S7-300/400 F-CPUs](http://support.automation.siemens.com/WW/view/en/49972838)
- [STEP 7 Safety Basic V13 SP1 with S7-1200 F-CPUs](http://support.automation.siemens.com/WW/view/en/34612486/133300) (part of the manual "S7-1200 Functional Safety manual")
- [STEP 7 Safety Advanced V13 with S7-1500 F-CPUs](http://support.automation.siemens.com/WW/view/en/101177693)

## Configuring

This section contains information on the following topics:

- [Overview of Configuration](#overview-of-configuration)
- [Particularities for configuring the F-System](#particularities-for-configuring-the-f-system)
- [Configuring an F-CPU](#configuring-an-f-cpu)
- [Configuring F-I/O](#configuring-f-io)
- [Configuration control (option handling) for F-I/Os](#configuration-control-option-handling-for-f-ios)
- [Configuring shared device](#configuring-shared-device)
- [Configuring isochronous mode (S7-1500)](#configuring-isochronous-mode-s7-1500)
- [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment)
- [Configurations supported by the SIMATIC Safety F-system](#configurations-supported-by-the-simatic-safety-f-system)
- [PROFIsafe addresses for F-I/O of PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1)
- [PROFIsafe addresses for F-I/O of PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2)
- [Setting the F-destination address for F-I/O with DIP switches](#setting-the-f-destination-address-for-f-io-with-dip-switches)
- [Assigning a PROFIsafe address of the F-I/Os with SIMATIC Safety](#assigning-a-profisafe-address-of-the-f-ios-with-simatic-safety)
- [Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices](#peculiarities-when-configuring-fail-safe-gsd-based-dp-slaves-and-fail-safe-gsd-based-io-devices)

### Overview of Configuration

#### Introduction

You basically configure a SIMATIC Safety F‑system in the same way as a standard S7‑300, S7‑400, S7-1200, S7‑1500 or ET 200MP, ET 200SP, ET 200AL, ET 200S, ET 200iSP, ET 200eco, ET 200eco PN or ET 200pro automation system in STEP 7.

This section presents only the essential differences compared to standard configuration you encounter when configuring a SIMATIC Safety F-system.

This documentation distinguishes between two groups of F-I/O:

#### F-I/Os of PROFIsafe address type 1

F-I/Os which ensure the uniqueness of the PROFIsafe address solely with the F-destination address, for example, ET 200S F-modules. The PROFIsafe address is usually assigned by DIP switches.

#### F-I/Os of PROFIsafe address type 2

F-I/Os which can ensure the uniqueness of the PROFIsafe address with a combination of F-source address and F-destination address, for example, S7-1500/ET 200MP F-modules. The PROFIsafe address is usually assigned with STEP 7 Safety.

#### Which F‑components can you configure with the STEP 7 Safety ?

The table below shows you which F-CPUs you can configure with STEP 7 Safety Basic and which with STEP 7 Safety Advanced:

| F-CPUs | STEP 7 Safety Basic | STEP 7 Safety Advanced |
| --- | --- | --- |
| S7-300 | — | x |
| S7-400 | — | x |
| S7-1200 | x | x |
| S7-1500(H) | — | x |
| SIMATIC Drive Controller | — | x |
| S7-1500 F Software Controller | — | x |

The table below shows you which F-I/Os you can configure with STEP 7 Safety Basic and which with STEP 7 Safety Advanced as well as which PROFIsafe address type they support:

| F-I/O | STEP 7 Safety Basic | STEP 7 Safety Advanced | PROFIsafe address type |
| --- | --- | --- | --- |
| S7‑300 F-SMs | x** | x** | 1 |
| ET 200S F-modules | x | x | 1 |
| ET 200pro F-modules | x | x | 1 |
| ET 200iSP F-modules | x | x | 1 |
| ET 200eco DP F-I/Os | — | With S7-300/400 F-CPUs (only PROFIsafe V1 mode) | 1 |
| ET 200eco PN F-I/Os | x | x | 2 |
| S7-1200 F-modules  (centrally on S7-1200 F-CPUs) | x | x | 2 |
| ET 200SP F-modules | x | x | 2 |
| S7-1500/ET 200MP F-modules | x | x | 2 |
| ET 200AL F-modules | x | x | 2 |
| fail-safe GSD based DP slaves | x | x | * |
| fail-safe GSD based I/O devices | x | x | * |
| * Consult the respective documentation to determine the PROFIsafe address type of a GSD based DP slave/GSD based I/O device. If in doubt, assume that the PROFIsafe address is type 1.  *** F-SMs that only support PROFIsafe V1 mode can only be used on F-CPUs S7-300/400. |  |  |  |

#### Example: Configured F-system in STEP 7 Professional

The following figure presents a configured F-system. You choose the fail-safe components in the "Hardware catalog" task card as you would do with standard components and place them in the work area of the network or device view. F-components are shown in yellow.

![Example: Configured F-system inSTEP 7 Professional](images/113865169419_DV_resource.Stream@PNG-en-US.png)

#### More information

For detailed information on F-I/O, refer to the manuals for the relevant F-I/O.

#### Which safety-related communication options can you configure?

You need to use the hardware and network editor to configure the following safety-related communication options (see [Configuring and programming communication (S7-300, S7-400)](#configuring-and-programming-communication-s7-300-s7-400) or [Configuring and programming communication (S7-1200, S7-1500)](#configuring-and-programming-communication-s7-1200-s7-1500)):

- [Communication with Flexible F-Link](#configuring-and-programming-communication-with-flexible-f-link-s7-1200-s7-1500)
- Safety-related master-master communication
- Safety-related master-master communication for S7 Distributed Safety
- Safety-related master-I-slave communication
- Safety-related I-slave-I-slave communication
- Safety-related I-slave-slave communication
- Safety-related IO controller-IO controller communication
- Safety-related IO controller-IO controller communication for S7 Distributed Safety
- Safety-related IO controller-I-device communication
- Safety-related IO controller-I-slave communication
- Safety-related communication via S7 connections
- Safety-related communication via S7 connections for S7 Distributed Safety or S7 F Systems

### Particularities for configuring the F-System

#### Configuring is the same as for standard components

You configure a SIMATIC Safety F-system in the same way as a standard S7 system. This means that you configure and assign parameters for the hardware in the hardware and network editor as a centralized system (F‑CPU and if required F‑IO for example CPU 1516F-3 PN/DP and F‑modules S7-1500/ET 200MP) and/or as a distributed system (F‑CPU, F‑SMs in ET 200M, F‑modules ET 200MP, ET 200SP, ET 200AL, ET 200S, ET 200pro, ET 200iSP, ET 200eco, ET 200eco PN, fail-safe GSD-based DP slaves and/or fail-safe GSD-based I/O devices).

#### Special F-parameters

For the F-functionality there are special F-parameters that you can review and set in the "Properties" of the fail-safe components (F-CPU and F-I/O). F‑parameters are marked in yellow.

F‑parameters are explained in "[Configuring an F-CPU](#configuring-an-f-cpu)" and "[Configuring F-I/O](#configuring-f-io)".

#### Compiling the hardware configuration

You must compile the hardware configuration of the SIMATIC Safety F-system (shortcut menu "Compile > Hardware configuration"). A configured F-CPU with enabled F-capability is the only prerequisite for programming the safety program.

> **Note**
>
> Inconsistencies are possible when configuring the hardware and can also be saved. A full consistency check of the hardware configuration and possible connection data is performed only during compilation. Therefore, perform "Edit > Compile" regularly.

#### Changing safety-related parameters

> **Note**
>
> If you change a safety-related parameter (marked in yellow) for an F-I/O or an F-CPU, you must then compile the modified hardware configuration and the [Compiling the safety program](#compiling-the-safety-program) (shortcut menu "Compile > Hardware and software (only changes)") and download. This also applies for changes to the F-I/O which are not used in the safety program. F-I/O in standard operation is not affected by this.

### Configuring an F-CPU

#### Introduction

You configure the F-CPU basically in the same way as a standard automation system.

F‑CPUs are always configurable in STEP 7, regardless of whether or not the STEP 7 Safety license is installed. Without an installed STEP 7 Safety license, the F‑CPU can only be used as a standard CPU.

With installed STEP 7 Safety license, you can enable or disable the F‑capability for the F‑CPU.

If you want to use the F-I/O in safety mode or in safety-related communication, the F-capability of the F-CPU must be enabled.

F‑capability is activated by default when STEP 7 Safety license is installed.

#### Enabling F-capability

If you want to enable the F-capability, proceed as follows:

1. Select the F‑CPU in the device or network view, and select the "Properties" tab in the Inspector window.
2. Select "Fail-safe" in the area navigation.
3. Enable the F-capability with the "Enable F-activation" button.

#### Disabling F-capability

If you want to disable the F‑capability for an F‑CPU because you intend to use the F‑CPU as a standard CPU, note the following:

- You need F-access permission for the safety program, if assigned.
- The [Safety Administration Editor](#safety-administration-editor-1) is deleted from the project tree.
- The F-OBs are deleted. (S7-1200, S7-1500)
- All F-blocks are deleted.
- From now on you cannot use F-I/O in safety mode with this F-CPU.

If you want to disable the F-capability, proceed as follows:

1. Select the F‑CPU in the device or network view, and select the "Properties" tab in the Inspector window.
2. Select "Fail-safe" in the area navigation.
3. Disable the F-capability with the "Disable F-activation" button.
4. Confirm the "Disable F-activation" dialog with "Yes".

Although you can enable the F-capability of the F-CPU without F-access permission, this permission is required to disable it.   
If you do not have F-access permission and have enabled the F-capability accidentally, you can only disable it using "Undo".

#### Configuring the F-parameters of the F-CPU

In the "Properties" tab of the F-CPU, you can change or apply the default settings for the following parameters:

- The F-destination address range

  - Low limit for F-destination addresses
  - High limit for F-destination addresses
- The default F-monitoring time for central or distributed F-I/O at the F-CPU

  (For HF-CPUs, only the default F-monitoring time for distributed F-I/O.)

  > **Note**
  >
  > A change of the F-monitoring time for central or distributed F-I/O at the F-CPU results in modifications to the safety program when it is recompiled. A new acceptance may therefore be required.

#### Specify F-destination address for F-I/O of PROFIsafe address type 1

With the parameters "Low limit for F-destination addresses" and "High limit for F-destination addresses" you specify a range for this F-CPU in which the F-destination address of newly inserted F-I/Os of [PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1) is assigned automatically. The F-destination address of an F-I/O is automatically moved to the destination address range of an F-CPU as soon as it is newly assigned to it.

The F-destination address is assigned in ascending order starting at the "Low limit for F-destination addresses". When no free F-destination address is available in the F-destination address range, the next available free F-destination address outside the F-destination address range is assigned and a warning is output during compilation.

The maximum possible F-destination address for ET 200S, ET 200eco, ET 200pro, ET 200iSP F-modules and S7-300 F-SMs is 1022.

The F-destination addresses for F-I/O of PROFIsafe address type 1 must be unique network-wide and CPU-wide.

By selecting different F-destination address ranges for different F-CPUs, you can define different ranges for the automatic assignment of the F-destination address. This is useful when you are operating multiple F-CPUs in one network. Subsequent manual address changes are possible. (see also [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment))

**Example:**

You have configured the F-destination address range as follows:

- Low limit for F-destination addresses = 100
- High limit for F-destination addresses = 199

When inserting the first F-I/O of PROFIsafe address type 1, the F-destination address 100 is assigned. When inserting an additional F-I/O of PROFIsafe address type 1, the F-destination address 101 is assigned.

> **Note**
>
> The parameters "Low limit for F-destination addresses" and "High limit for F-destination addresses" have no effect on the following F-I/Os:
>
> - SM 326; DI 8 x NAMUR (as of article number 6ES7326-1RF00-0AB0)
> - SM 326; DO 10 x DC 24V/2A (article number 6ES7326-2BF01-0AB0)
> - SM 336; AI 6 x 13 bit (article number 6ES7336-1HE00-0AB0)

#### Specify F-destination address for F-I/O of PROFIsafe address type 2

The F-destination address of F-I/O of [PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2) is assigned automatically for each F-CPU in descending order starting with 65534. The low limit is the value configured with the parameter "Low limit for F-destination addresses" (for F-I/O of PROFIsafe address type 1) + 1.

When the value configured with the "High limit for F-destination addresses" parameter is reached, a warning is output during compilation. (See also [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment))

#### Specify F-source address for F-I/O of PROFIsafe address type 2

You specify the F-source address for F-I/O of [PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2) assigned to this F-CPU with the "Central F-source address" parameter. The F-source address must be unique throughout the network. (see also [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment))

> **Note**
>
> A change to the "Central F-source address" parameter results in modifications to the safety program when it is recompiled. A new acceptance may therefore be required because the F-source addresses of all F-I/Os of address type 2 are changed centrally by this step.

#### "Default F-monitoring time" parameter

Configure the "Default F-monitoring time" for monitoring the communication between the F-CPU and F-I/O.

You can adjust the F-monitoring time via the following parameters:

- "Default F‑monitoring time for central F‑I/O"
- "Default F‑monitoring time for F‑I/O of this interface"

The **default F‑monitoring time for the central F‑I/O** acts on the F‑I/O that is arranged centrally, i.e. near the F‑CPU. You set this parameter in the properties of the F‑CPU (select F‑CPU, then select "Properties > Fail-safe > F‑parameters").

The **default F‑monitoring time for the F‑I/O of this interface** acts on the F-I/O that is assigned to this interface of the F-CPU (PROFIBUS or PROFINET). You change this parameter in the properties of the relevant interface (selection of the interface in the "Device view" tab, then "F-parameters").

The various settings available allow you to flexibly adapt the F‑monitoring time to the conditions of your F‑system, for example to take account of different bus cycles.

You can also change the F-monitoring time individually for each F-I/O in the F-I/O properties (see [Configuring F-I/O](#configuring-f-io) or [Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices](#peculiarities-when-configuring-fail-safe-gsd-based-dp-slaves-and-fail-safe-gsd-based-io-devices)).

> **Note**
>
> A change of the F-monitoring time for central or distributed F-I/O at the F-CPU results in modifications to the safety program when it is recompiled. A new acceptance may therefore be required.

> **Note**
>
> The default value for the "Default F-monitoring time for the F-I/O" for an HF-system is 2300 ms and is designed for an MRP ring. For line topology, you can set the "Default F-monitoring time for the F-I/O" smaller by a factor of approx. 2. You can determine the exact value as described in section "[Monitoring and response times](#monitoring-and-response-times)". You can set this value in the properties of the F-CPU (selection of the F-CPU, then "Properties > Fail-safe > F-parameters > PROFINET interface [X1]").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time.(S018) |  |

You can find more information in [Monitoring and response times](#monitoring-and-response-times).

#### Automatic generation of the safety program

The safety program of an F-CPU consists of one or two F-runtime groups that contain the F-blocks (see also [Defining F-Runtime Groups](#defining-f-runtime-groups)). When the F-CPU (with activated F-capability) is inserted into the work area of the device view or network view, a safety program with an F-runtime group is generated automatically.

You can define in STEP 7 Safety  that no F-runtime group is generated while inserting the F-CPU (with activated F-capability).

Proceed as follows:

1. Select the "Options > Settings" menu command.
2. Select the "STEP 7 Safety" area.
3. If it is not already disabled, disable automatic generation of an F-runtime group by deselecting the "Generate default fail-safe program" option.

This change has no influence on any existing safety programs; it only defines whether an F-runtime group is automatically generated for each one of the subsequently inserted F-CPUs.

#### Configuring the protection level of the F-CPU

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) In productive operation, it must be prevented that changes to the standard user program are unintentionally made in the safety program as well. For this purpose, you must configure the protection level "Write protection for fail-safe blocks" and configure a password for the F‑CPU.   With the "Write protection" or "Write/read protection" protection level, the password would apply to the standard and the safety program. (S001) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) In productive operation, the safety-related project data must be protected against unintentional changes.  If you use local user management, the Runtime rights "F-Admin" and "Full access with fail-safe access" and the engineering right for user management may only be granted to authorized users. You must also limit the assignment of user rights to trained personnel.  If you are not using local user management or if legacy mode is enabled, then, at a minimum, configure protection level "Full access (no protection)" and assign a password under "Full access with fail-safe (no protection)". This protection level allows full access only to the standard user program and not the safety program.  If you select a higher protection level, for example to protect the standard user program, you must assign an additional password for "Full access (no protection)".   Assign different passwords for the individual access levels. (S041) |  |

You configure the protection level following the same procedure as for standard CPUs.

For information on the password for the F‑CPU, refer to [Access protection](#introduction-to-access-protection). Pay special attention to the warnings in [Access protection for the F-CPU](#access-protection-for-the-f-cpu-1).

### Configuring F-I/O

#### Introduction

You configure the S7-1500/ET 200MP, ET 200SP, ET 200AL, ET 200S, ET 200eco (S7-300, S7-400), ET 200eco PN, ET 200pro and ET 200iSP, the S7‑300 F‑SMs and the S7-1200 F-modules as usual in STEP 7.

After you have inserted the F‑I/O in the work area of the device or network view, you access the configuration dialogs by selecting the relevant F‑I/O and the "Properties" tab.

> **Note**
>
> Changes to the parameter assignment result in modifications to the safety program when it is recompiled. A new acceptance may therefore be required.

The ET 200SP F-modules can be used in distributed system with:

- IM 155-6 PN ST as of firmware V1.1
- IM 155-6 PN HF
- IM 155-6 PN/2 HF as of firmware V4.2
- IM 155-6 PN/3 HF as of firmware V4.2
- IM 155-6 MF HF
- IM 155-6 PN HS
- IM 155-6 DP HF
- IM 155-6 PN R1

  You can find information on whether operation with R1 is supported for an ET 200SP F-module on the [Internet.](https://support.industry.siemens.com/cs/ww/en/view/73021864)

The distributed use of S7-1500/ET 200MP F-modules is possible with:

- IM 155-5 PN BA as of firmware V4.3
- IM 155-5 PN ST as of firmware V3.0
- IM 155-5 PN HF as of firmware V2.0
- IM 155-5 DP ST as of firmware V3.0

The central use of S7-1500/ET 200MP F-modules is possible with S7-1500 F-CPUs as of firmware V1.7, distributed use as of firmware V1.5.

(S7-1200) We recommend you limit the total number of F-I/Os that are used centrally or distributed in an S7-1200 F-CPU to 12. Depending on the volume of project data, the maximum number of F-I/Os can be smaller.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When you make changes in which the assignment of input/output addresses and wiring can change, then you must perform a [wiring test](#testing-the-safety-program-1).  Examples for such changes are:  - Adding F-I/O - Changing the start address of F-I/O - Changing the slot position of F-I/O - Changing   - the rack   - the slave/device address   - the PROFIBUS DP/PROFINET IO subnet   - the IP address   - the device name    (S071) |  |

#### Channel-granular passivation after channel faults

You can configure how the F-I/O will respond to channel faults, such as a short-circuit, overload, discrepancy error, or wire break, provided the F-I/O supports this parameter (e.g. for ET 200S or ET 200pro F-modules). You configure this response in the properties for the relevant F-I/O ("Behavior after channel fault" parameter). This parameter is used to specify whether the entire F-I/O or just the faulty channel(s) are passivated in the event of channel faults.

> **Note**
>
> (S7-300, S7-400) Note that channel-granular passivation increases the runtime of the F-runtime group(s) compared to passivation of the entire F-I/O (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).

#### "Channel failure acknowledge" parameter (S7-1200, S7-1500)

In the case of F-I/Os that support the "Channel failure acknowledge" channel parameter (for example S7-1500/ET 200MP F-modules, S7-1200 F-modules or ET 200AL F-modules), this function replaces the ACK_NEC tag of the F-I/O DB.

If an F-I/O fault is detected by the F-I/O, passivation of all channels of the relevant F-I/O occurs. If channel faults are detected, the relevant channels are passivated if "Passivate channel" is configured. If "Passivate the entire module" is configured, all channels of the relevant F-I/O are passivated. Once the F-I/O fault or channel fault has been eliminated, reintegration of the relevant F-I/O/the relevant channel occurs in line with the "Channel failure acknowledge" parameter.

- Automatically
- Manually

The parameter "Channel failure acknowledge" can be set individually for each channel with channel-granular passivation if "Adjustable" has been parameterized at the "Reintegration after channel fault" parameter.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The parameter assignment "Channel failure acknowledge = Automatic" is only allowed if automatic reintegration is permitted for the relevant process from a safety standpoint.(S045) |  |

> **Note**
>
> The default assignment for the "Channel failure acknowledge" parameter when the F-module is created is "Manually".

#### Organization block/Process image (S7-1200, S7-1500)

If you use F-I/O in standard mode, you can select the organization block/process image as you do for standard I/O.

If you use F-I/O in safety mode, no selection is possible. The process image is always updated automatically at the beginning or end of the F-runtime group (see section [Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)).

Contrary to F-I/O operated in non-isochronous mode, you need to selected a process image partition, such as PIP 1 for F-I/O that is operated in isochronous mode (see "[Configuring isochronous mode (S7-1500)](#configuring-isochronous-mode-s7-1500)").

#### Changing the name and number of the F‑I/O DB

For more information, refer to the section "[Fail-safe I/O data block](#f-io-db)".

#### Customizing the F‑monitoring time for F-I/O

You can customize the F-monitoring time in the properties of the F-I/O under "F‑parameters". This may be necessary to prevent a timeout being triggered when no error occurs and the F-I/O requires a longer F-monitoring time or assignment with a default F-monitoring time is not possible. For this purpose, activate the corresponding check box and assign an F-monitoring time.

> **Note**
>
> A change of the F-monitoring time for central or distributed F-I/O at the F-CPU results in modifications to the safety program when it is recompiled. A new acceptance may therefore be required.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time.(S018) |  |

You can find more information in [Monitoring and response times](#monitoring-and-response-times).

#### Group diagnostics for fail-safe S7-300 signal modules

By disabling a channel of the fail-safe signal module in the module properties, you also disable the group diagnostics for this channel.

**Exception for S7-300/400 F-CPUs:**

For the following S7-300 fail-safe signal modules, the monitoring of channel-specific diagnostic messages (for example, wire break, short-circuit) from the F-SM to the F-CPU is enabled and disabled with the "Group diagnostics" parameter.

- SM 326; DI 8 x NAMUR (as of article number 6ES7326‑1RF00‑0AB0)
- SM 326; DO 10 x DC 24V/2A (article number 6ES7326‑2BF01‑0AB0)
- SM 336; AI 6 x 13Bit (article number 6ES7336‑1HE00‑0AB0)

You should disable group diagnostics for **unused** input or output channels.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) For the following S7‑300 fail-safe signal modules (F‑SMs) with activated safety mode, "Group diagnostics" must be enabled on all used channels:  - SM 326; DI 8 x NAMUR (article numbers 6ES7326‑1RF00‑0AB0 and 6ES7326-1RF01-0AB0) - SM 326; DO 10 x DC 24V/2A (article number 6ES7326‑2BF01‑0AB0) - SM 336; AI 6 x 13 Bit (article number 6ES7336‑1HE00‑0AB0)    (S003) |  |

Diagnostic interrupts can be enabled optionally.

#### More information

For detailed description of the **parameters**, refer to the help on the properties of the respective F-I/O and in the respective manual for the F-I/O.

### Configuration control (option handling) for F-I/Os

This section contains information on the following topics:

- [Configuration control (option handling) for F-I/Os](#configuration-control-option-handling-for-f-ios-1)
- [Example](#example)

#### Configuration control (option handling) for F-I/Os

For configuration control (option handling) with F-I/Os proceed as with the standard I/O devices. Detailed information can be obtained by searching for "Configuration control (option handling)" in the help of STEP 7.

The following section describes what you have to observe additionally for F-I/Os.

##### Requirements

- The requirements that are specified under "Configuration control (option handling)" in the help of STEP 7 are fulfilled.
- The requirements that are specified under "Configuration control (option handling)" in the help of STEP 7 are fulfilled. Handle the F-I/O as standard I/O.
- V2.1 or higher is set as the safety system version.
- The F-I/Os for which you use the configuration control (option handling) are located

  - Distributed at an F-CPU S7-300/400/1200/1500
  - Centrally at an F-CPU S7-1500

  The PROFIsafe address of the F-I/Os are set or assigned.

  > **Note**
  >
  > Only if the maximum configuration actually exists is [assigning the PROFIsafe addresses](#assigning-a-profisafe-address-of-the-f-ios-with-simatic-safety) possible.

##### Procedure

(S7-1200, S7-1500) Disable the F-I/Os not existing in the respective variant (option) by setting the [DISABLE](#disable) variable in the associated [F-I/O DB](#f-io-db-1) to "1". This prevents the flashing of the error LED of the F-CPU and diagnostic entries of the safety program that reference these F-I/Os. With the [DISABLED](#qbadpass_outdisabledqbad_i_xxqbad_o_xx-and-value-status) variable of the associated F-IO data block, you can evaluate whether an F-module is deactivated.

(S7-300, S7-400) To prevent the flashing of the error LEDs of the F-CPUs you do not have to observe anything further. You cannot suppress diagnostics entries.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If configuration control is used, your actual configuration deviates from the configured maximum configuration. You identify F-I/Os that do not exist in the current option (station option) via control record as "not available".   If an F-I/O marked as "not available" is possibly nevertheless in the real system, it has to be ensured that substitute values (0) are provided for these F-I/Os in the safety program or output at the outputs. This is achieved by setting the DISABLE tag (S7-1200, S7-1500) or respectively PASS_ON tag (S7-300, S7-400) in the associated F-I/O DB to "1". (S077) |  |

#### Example

##### Introduction

The following example shows how you to

- Select/detect a station option
- Deactivate F-I/Os that are not present in a station option (S7-1200, S7-1500)
- Provide your safety program for various station options

##### Safe selection/detection of the station option

You carry out a safe selection/detection of a station option with inputs of an F-I/O wired fixed to M/L+.

For example, you can select up to 4 station options with 2 inputs of an F-I/O.

| Option | OptionSelection_Bit_0 | OptionSelection_Bit_1 |
| --- | --- | --- |
| Q | 0 | 0 |
| B | 0 | 1 |
| C | 1 | 0 |
| D | 1 | 1 |

Note when detecting the station option that substitute values (0) are used for the inputs of the F-I/O in certain situations, e.g. during startup of the F-system or when F-I/O channel errors occur.

In these situations, the present station option cannot be detected. You should therefore also evaluate the value status of inputs and only apply the station option one-time after startup of the F-system.

For one-time recognition of the station option, define a static local datum, for example, OptionSelectionRuns with default value "TRUE".

![Safe selection/detection of the station option](images/115694777099_DV_resource.Stream@PNG-en-US.png)

![Safe selection/detection of the station option](images/115694773259_DV_resource.Stream@PNG-en-US.png)

Correspondingly for options C and D.

As soon as a station option is detected, reset the static local datum for one-time detection of the station option:

![Safe selection/detection of the station option](images/115694781067_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> When you make the selection/detection of a station option only in the standard user program, only the "Station option" is available to you as a standard datum that is not secured.
>
> Make sure that no dangerous states arise from this.
>
> Read the section "[Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program)".

##### Disabling F-I/Os that are not present in a station option

If one or more F-I/Os are not present in a station option, you can prevent the blinking of the error LED of the F-CPU by disabling these F-I/Os.

In addition, diagnostic messages of the safety program that refer to these F-I/Os are suppressed.

> **Note**
>
> As long as the detection of the station option (during startup of the F-system) is not yet complete (OptionSelectionRuns = TRUE), you should disable all "optional" F-I/O devices.

![Disabling F-I/Os that are not present in a station option](images/115695450379_DV_resource.Stream@PNG-en-US.png)

##### Providing the safety program for various station options

In the following example, the EMERGENCY STOP signals of different plant units or machines are combined into a collective EMERGENCY STOP signal.

Machines I and III and the corresponding F-I/O with the EMERGENCY STOP signal for machines I and III are not present with station option A.

Machine II and the corresponding F-I/O with the EMERGENCY STOP signal for machine II is not present with station option B.

The substitute values (0) are therefore used in the safety program for the EMERGENCY STOP signals from the respective unavailable machines.

In order to prevent the collective EMERGENCY STOP from being triggered because machines / EMERGENCY STOP signals are not present with certain station options, you can suppress the evaluation of the EMERGENCY STOP signal for unavailable machines by taking into account the present station option.

![Providing the safety program for various station options](images/115695454091_DV_resource.Stream@PNG-en-US.png)

### Configuring shared device

To configure shared devices follow the procedure as in the standard. The configuration is described in the STEP 7 help under "Configuring shared devices" and in the function manual "[PROFINET with STEP 7](https://support.industry.siemens.com/cs/ww/en/view/49948856)" in the chapter "Shared Device".

#### F-destination addresses

Please also read the chapter "[Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment)" for assigning the F-destination address.

---

**See also**

[Assigning PROFIsafe address to an F-module in a shared device in multiple projects](#assigning-profisafe-address-to-an-f-module-in-a-shared-device-in-multiple-projects)
  
[Assigning PROFIsafe address to an F-module in a shared device in a common project](#assigning-profisafe-address-to-an-f-module-in-a-shared-device-in-a-common-project)

### Configuring isochronous mode (S7-1500)

To configure isochronous mode for F-I/Os that support this mode, e.g. "Profisafe Telgr 902" submodule of the SINAMICS S120 CU310-2 PN V5.1 drive, proceed as in the standard. The configuration is described in the STEP 7 help under "Configuring isochronous mode".

Note the following:

- Contrary to F-I/O operated in non-isochronous mode, you need to selected a process image partition, such as PIP 1 for F-I/O that is operated in isochronous mode.  
  This process image partition must contain only F-I/O operated in isochronous mode and no standard I/O.
- The assigned isochronous mode interrupt OB must first be generated as F-OB by specifying a F-runtime group (see [Procedure for defining an F‑runtime group (S7-1200, S7-1500)](#procedure-for-defining-an-f-runtime-group-s7-1200-s7-1500)). It is not possible to add an F-OB with event class "Synchronous Cycle" directly during the configuration of the isochronous mode.

#### Requirement

S7-1500 F-CPUs as of firmware V2.0 that support IRT.

#### Connection of F-I/O operated in isochronous mode to the isochronous mode interrupt OB

You access F-I/O operated in isochronous mode in the same way as you do standard I/O operated in isochronous mode, via the select process image partition.

Contrary to standard I/O that is operated in isochronous mode, the process image partition is updated by the F-system at the beginning or end of the F-OB (see [Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)).

No calling of the instructions SYNC_PI and SYNC_PO is required in the F-OB.

> **Note**
>
> With isochronously operated F-I/O, it is not ensured (fail-safe) that all input data of the F-I/Os assigned to the process image partition are consistently available at the beginning of the main safety block or all output data is transferred consistently to the F-I/Os, in other words, logically and temporally together. The consistency is only ensured within an F-I/O.
>
> The consistency of all isochronous F-I/Os of the process image partition usually depends on the number of isochronous F-I/Os and the scope of the safety program in the isochronous mode interrupt OB.
>
> If there are corresponding consistency requirements, you must check the consistency of the input and output data yourself. You can do this, for example, by additionally transferring and evaluating time stamps in the input and output data of the isochronous F-I/Os.

### Recommendation for PROFIsafe address assignment

Before inserting the F-I/O, specify an address range for each F-CPU for the F-destination addresses of the [F-I/O of PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1) that does not overlap with the address range of any other F-CPU network-wide or CPU-wide (system-wide). You define the range with the parameters "Low limit for F-destination addresses" and "High limit for F-destination addresses" (see also section [Configuring an F-CPU](#configuring-an-f-cpu)).

In a redundant S7-1500HF system, consider both F-CPUs of the redundant S7-1500HF system as one F-CPU with regard to the PROFIsafe addresses. The "Low/high limit for F-destination addresses" or the "Central F-source address" is therefore set identically by the system for both F-CPUs.

The F-destination addresses of [F-I/O of PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2) must not overlap with any address range of the F-I/O of PROFIsafe address type 1. The ranges of the F-destination addresses of the F-I/O of PROFIsafe address type 2 may overlap if the F-source addresses are different. This is the case for [supported configurations](#configurations-supported-by-the-simatic-safety-f-system) if the "Central F-source address" parameter has been set differently for each F-CPU.

Assign relatively low F-destination addresses for F-I/O of PROFIsafe address type 1 and relatively high F-destination addresses for F-I/O of PROFIsafe address type 2.

![Address assignment for F-I/O of PROFIsafe address types 1 and 2](images/166481240971_DV_resource.Stream@PNG-en-US.png)

Address assignment for F-I/O of PROFIsafe address types 1 and 2

The [safety summary](#completeness-of-the-safety-summary) lists the following information for each F-CPU:

- "Central F-source address" parameter (F-source address for F-I/O of PROFIsafe address type 2)
- Actually used range of the F-destination addresses of the assigned F-I/O of PROFIsafe address type 1
- Actually used range of the F-destination addresses of the assigned F-I/O of PROFIsafe address type 2

Any F-I/O configured using I-slave-slave communication is taken into account in the safety summary as part of the F-destination address range of the I-slave.

Any F-I/O configured in a shared device is indicated in the safety summary as part of the F-destination address range of the F-CPU to which this F-I/O is assigned.

### Configurations supported by the SIMATIC Safety F-system

#### Supported configurations

F-I/Os (see [Overview of Configuration](#overview-of-configuration)) are supported in the following configurations:

central configuration (also I-slave):

- The F-I/O is in the same rack as the associated F-CPU.
- The F-I/O is located in a subrack of the rack of the associated F-CPU.

distributed configuration (at integrated DP-/PN interface of the CPU or at CP/CM):

- PROFIBUS DP (also after IE/PB link)

  - The F-I/O is located on a DP Slave.
  - The F-I/O is located on a DP Slave and is addressed via I-slave-slave communication. The assigned DP master (of the assigned IO controller of the IE/PB link) can be a standard CPU or an F-CPU.
- PROFINET IO

  - The F-I/O is located on an IO Device.
  - The F-I/O is located in a shared I-device.
  - The F-I/O is located in a shared device.

    For a shared device in a common project, this applies only when no CP/CM is used and only for the ET 200SP, ET 200AL and ET 200MP product families.

For a redundant S7-1500HF system the only supported configuration is:

distributed configuration (on integrated PN interface of the HF-CPU)

- PROFINET IO

  - The F-I/O is located in an IO device that is assigned to the IO systems of both F-CPUs.

    More information on IO devices for R1, S1 and S2 redundancy is available in the [PROFINET Function Manual](https://support.industry.siemens.com/cs/ww/en/view/49948856) in section "PROFINET with the redundant S7-1500R/H system".

For F-I/O not listed in "[Overview of Configuration](#overview-of-configuration)", check the relevant documentation to see whether it is supported by the SIMATIC Safety F-system. If in doubt, treat these F-I/Os as part of a configuration that is not supported.

#### Checks performed by the SIMATIC Safety F-system

For supported configuration, the F-system checks:

- Whether the PROFIsafe operating mode parameter (F_Par_Version) is set to V2 mode in the PROFINET IO environment**.
- Whether the F-destination addresses have been assigned uniquely CPU-wide.   
  You yourself must ensure the network-wide uniqueness of the PROFIsafe address.
- Whether the F-source address for the F-I/O of PROFIsafe address type 2 corresponds to the "Central F-source address" parameter of the F-CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Note the following when using configurations that are not included in supported configurations:  - Make sure that the F-I/O of this configuration appears in the safety summary and that an F-I/O DB has been created for it. Otherwise, you cannot use the F-I/O in this configuration. - For F-I/O in the PROFINET IO environment**, you must check the safety summary for correctness of the PROFIsafe operating mode parameter (F_Par_Version). V2 mode must be set in the PROFINET IO environment. F-I/O which only support V1 mode must not be used in the PROFINET IO environment. - You must ensure that the PROFIsafe address assignment is unique CPU-wide*/**** and network-wide***:    - Check the safety summary for correctness of the PROFIsafe addresses.   - For F-I/O of PROFIsafe address type 2, check the safety summary to verify that the F-source address corresponds to the "Central F-source address" parameter of the F-CPU.   - For F-I/O of PROFIsafe address type 1 or if you cannot set the F-source address in accordance with the "Central F-source address" parameter of the F-CPU, you will have to ensure the uniqueness of the PROFIsafe address solely by assigning a unique F-destination address.In an unsupported configuration, you must check the uniqueness of the F-destination address individually for each F-I/O using the safety summary (see [Completeness and correctness of the hardware configuration](#completeness-and-correctness-of-the-hardware-configuration)) (S050) |  |

* "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.

** The F-I/O is located in the "PROFINET IO environment" if at least part of safety-related communication with the F-CPU takes place via PROFINET IO. If the F-I/O is connected via I-slave-slave communication, also keep in mind the communication line to the DP master/IO controller.

*** A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

**** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU with regard to the PROFIsafe addresses. Therefore, the "Central F-source address" is set identically by the system for both F-CPUs.

> **Note**
>
> For more information on the assignment of PROFIsafe addresses that are unique for the CPU and across the network, see this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109740240).

### PROFIsafe addresses for F-I/O of PROFIsafe address type 1

#### F-destination address

The uniqueness of the PROFIsafe address is ensured solely with the F-destination address. The F-source address is not displayed and has no effect on whether or not the PROFIsafe address is unique.

Therefore, the F-destination address must be unique network-wide and CPU-wide (see the following rules for address assignment).

To prevent incorrect parameter assignment, an F-destination address which is unique CPU-wide is automatically assigned during placement of the F-I/O in the work area of the device or network view as long as you only configure [supported configurations](#configurations-supported-by-the-simatic-safety-f-system).

To ensure a network-wide unique F-destination address assignment when multiple DP master systems and PROFINET IO systems are operated on one network, you must set the "Low limit for F-destination addresses" and "High limit for F-destination addresses" in the properties of the F-CPU in SIMATIC Safety F-systems appropriately, before placing the F-I/O (see section "Recommendations for address assignment") so that the F-destination address ranges do not overlap.

When you change the F-destination address of an F-I/O, the CPU-wide uniqueness of the F-destination address is checked automatically for supported configurations. You yourself must ensure the network-wide uniqueness of the F-destination address.

For ET 200S, ET 200eco (PROFIBUS), ET 200pro, ET 200iSP F-modules and S7-300 F-SMs:  
You must set the F-destination address at the F-I/O with the DIP switch before you install the F-I/O. You can assign up to 1022 different F-destination addresses.

> **Note**
>
> (S7-300, S7-400) For the following fail-safe S7-300 signal modules, the F-destination address is the start address of the F-SM divided by 8:
>
> - SM 326; DI 8 x NAMUR (as of article number 6ES7326‑1RF00‑0AB0)
> - SM 326; DO 10 x DC 24V/2A (article number 6ES7326‑2BF01‑0AB0)
> - SM 336; AI 6 x 13 Bit (article number 6ES7336‑1HE00‑0AB0)

You can show the columns "F-source address" and "F-destination address" in the device view of the device overview. The addresses displayed in these columns are for information purposes only. You must check the F-destination addresses in the safety summary during system acceptance.

#### Rules for address assignment

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| F-I/Os of PROFIsafe address type 1 are uniquely addressed by their F-destination address (e.g. with the switch setting on the address switch).  The F-destination address (and therefore also the switch setting on the address switch) of the F-I/O must be unique network-wide* and CPU-wide**/*** (system-wide) **for the entire** F-I/O. The F-I/O of PROFIsafe address type 2 must also be considered. (S051) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.

*** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU with regard to the PROFIsafe addresses. Therefore, the "Central F-source address" is set identically by the system for both F-CPUs.

Also note [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment).

> **Note**
>
> For more information on the assignment of PROFIsafe addresses that are unique for the CPU and across the network, see this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109740240).

---

**See also**

[Completeness of the safety summary](#completeness-of-the-safety-summary)

### PROFIsafe addresses for F-I/O of PROFIsafe address type 2

#### F-source address and F‑destination address

The uniqueness of the PROFIsafe address is ensured by the combination of F-source address and F-destination address.

The PROFIsafe address must be unique network-wide and CPU-wide. This is the case if the following two conditions are met:

- The F-source address ("Central F-source address" parameter) of the F-CPU is unique network-wide. Keep this in mind for changes.
- The F-destination address of the F-module is unique CPU-wide.

You define the F-source address using the "Central F-source address" parameter in the F-CPU. Provided you only configure [supported configurations](#configurations-supported-by-the-simatic-safety-f-system), this parameter is automatically applied as the F-source address and a CPU-wide unique F-destination address is assigned (usually in descending order starting with 65534).

When you change the F-destination address, the CPU-wide uniqueness of the F-destination address is checked automatically for supported configurations.

You must assign the F-source address and F-destination address to the F-I/O before you commission the F-I/O. You can find more information in [Assigning a PROFIsafe address of the F-I/Os with SIMATIC Safety](#assigning-a-profisafe-address-of-the-f-ios-with-simatic-safety).

You can show the columns "F-source address" and "F-destination address" in the device view of the device overview. The addresses displayed in these columns are for information purposes only. You must check the F-source and F-destination addresses in the safety summary during system acceptance.

#### Rules for address assignment

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| F-I/O of PROFIsafe address type 2 is uniquely addressed using a combination of F-source address ("Central F-source address" parameter of the assigned F-CPU) and F-destination address.   The combination of F-source address and F-destination address for each F-I/O must be unique network-wide* and CPU-wide**/*** (system-wide). In addition, the F-destination address must not be occupied by F-I/O of PROFIsafe address type 1.  If you use a [supported configuration](#configurations-supported-by-the-simatic-safety-f-system), you only have to ensure that the "Central F-source address" parameter of all F-CPUs is unique network-wide*. (S052) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.

*** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU with regard to the PROFIsafe addresses. Therefore, the "Central F-source address" is set identically by the system for both F-CPUs.

Also note [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment).

> **Note**
>
> For more information on the assignment of PROFIsafe addresses that are unique for the CPU and across the network, see this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109740240).

---

**See also**

[Completeness of the safety summary](#completeness-of-the-safety-summary)

### Setting the F-destination address for F-I/O with DIP switches

Information on how to set the F-destination address for F-I/O with DIP switches is available in the documentation of the respective F-I/O.

### Assigning a PROFIsafe address of the F-I/Os with SIMATIC Safety

This section contains information on the following topics:

- [Introduction](#introduction)
- [Identifying F-modules](#identifying-f-modules)
- [Assign PROFIsafe address](#assign-profisafe-address)
- [Assigning PROFIsafe address to an F-module in a shared device in multiple projects](#assigning-profisafe-address-to-an-f-module-in-a-shared-device-in-multiple-projects)
- [Assigning PROFIsafe address to an F-module in a shared device in a common project](#assigning-profisafe-address-to-an-f-module-in-a-shared-device-in-a-common-project)
- [Changing the PROFIsafe address](#changing-the-profisafe-address)

#### Introduction

##### Introduction

You assign the [PROFIsafe address](#profisafe-addresses-for-f-io-of-profisafe-address-type-2), consisting of F-source address and F-destination address, directly from STEP 7Safety for the following F-I/O:

- ET 200SP fail-safe modules
- S7-1500/ET 200MP fail-safe modules
- ET 200AL fail-safe I/O modules
- ET 200eco PN fail-safe I/O modules

The PROFIsafe addresses for S7-1200 F-modules are automatically assigned during download of the hardware configuration.

None of these F-I/O modules have a DIP switch for setting the unique F-destination address for each module.

In the following cases it is necessary to reassign the addresses for fail-safe ET 200SP modules, fail-safe S7-1500/ET 200MP modules, fail-safe ET 200AL I/O modules, and fail-safe ET 200eco PN I/O modules:

- Later placement of a fail-safe module during initial commissioning (not for ET 200eco PN)
- Intentional modification of the F-destination address
- Modification of the "Central F-source address" parameter for the associated F-CPU (changes the F-source address).
- Replacement of the coding element
- Commissioning of a mass-produced machine

In the following cases it is not necessary to reassign the addresses of the fail-safe ET 200SP and fail-safe S7-1500/ET 200MP modules:

- POWER OFF/POWER ON
- Replacement of an F-module (repair) without PG/PC
- Replacement of the BaseUnit (transferring the coding element with assigned F-source address and F-destination address to the new BaseUnit)
- Replacement of a BaseUnit without coding element
- Changes in the design in case a new BaseUnit is inserted in front of a fail-safe module
- Repair/replacement of the interface module

Reassignment is not required for fail-safe ET 200eco PN and ET 200AL I/O modules in the following cases:

- POWER OFF/POWER ON
- Replacement of the compact device (transferring the coding element with assigned F-source address and F-destination address to the new compact device)

##### Basic procedure

> **Note**
>
> **Assigning the PROFIsafe address for S7-1200 fail-safe modules**
>
> The procedure described below for identifying and assigning the PROFIsafe addresses is not required for S7-1200 fail-safe modules.
>
> Note that an S7-1200 must not include an additional unconfigured F-module.

1. [Set the F-destination address](#profisafe-addresses-for-f-io-of-profisafe-address-type-2) and [F-source address](#profisafe-addresses-for-f-io-of-profisafe-address-type-2) in the hardware configuration inSTEP 7 Safety.
2. Identify the fail-safe modules ET 200SP, S7-1500/ET 200MP, fail-safe I/O modules ET 200AL or the fail-safe I/O modules ET 200eco PN to which you want to assign the PROFIsafe address.
3. Assign the PROFIsafe address to the F-I/Os.

##### Assigning the PROFIsafe address for F-I/Os via a redundant S7-1500HF system

In the "Assign PROFIsafe address" dialog under "Select PLC of HF-System", select the HF-CPU of the redundant S7-1500HF system via which you want to assign the PROFIsafe address.

The following table uses the system status to show you via which HF-CPU of the redundant S7-1500HF system you can assign the PROFIsafe address.

| System status/F-CPU role | Primary | Backup |
| --- | --- | --- |
| RUN-Redundant | x | x |
| RUN-Solo | x | - |
| STOP | x | - |
| x: Assignment possible, -: Assignment not possible |  |  |

> **Note**
>
> **Use of R1 devices**
>
> Assigning the PROFIsafe address for F-I/Os in an R1 device is only possible via the left interface module of the R1 device. Therefore, the left interface module is always displayed in the "Assign PROFIsafe address" dialog. The left interface module must be supplied with voltage for the assignment of the PROFIsafe address.
>
> If the two HF-CPUs of the redundant S7-1500HF system are located in two separate subnets, the PG and the HF-CPU via which the assignment of the PROFIsafe address is to be performed must be located in the same subnet.

#### Identifying F-modules

##### Requirement

The following requirements must be met:

- The F-CPU and fail-safe modules are configured.
- When using an ET 200SP Open Controller, the hardware configuration of the ET 200SP Open Controller **and** of the fail-safe Software Controller must be downloaded.
- The F-CPU and fail-safe modules can be reached online.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Make sure that the latest hardware configuration has been downloaded to the F-CPU before identification. By clicking the "Identification" button and then clicking on "Assign PROFIsafe address", you confirm the correctness of the PROFIsafe addresses for the F-I/Os.   Therefore, proceed carefully when confirming the F-I/Os by LED flashing or the serial number of the F-CPU with central F-I/Os or the serial number of the interface module with F-I/Os.   To do this, you must read and write down the serial number directly at the F-CPU* or the interface module**. Reading out the serial number via the online and diagnostics view of the TIA Portal is not permitted.  A special rule applies for F-I/Os of the ET 200AL distributed I/O system. For these F-I/Os, only identification by LED flashing is permissible and only exactly one F-I/O may be selected for the assignment of the PROFIsafe address at a time.   * When an ET 200SP Open Controller is used, you must read and write down the serial number from the display of the S7-1500 Fail-safe Software Controller in menu "Overview > CPU".  ** When an R1 device is used, you must read and write down the serial number of the left interface module. (S046) |  |

##### Procedure

Proceed as follows to identify the F-modules:

1. Establish an online connection to the F-CPU to which the F-modules are assigned.
2. In the network view, select

   - the F-CPU with F-modules,
   - the interface module with F-modules,

   to which you want to assign PROFIsafe addresses.

   Alternatively, you can select only a single F-module.
3. Select "Assign PROFIsafe address" from the shortcut menu.

   > **Note**
   >
   > If you integrate a fail-safe ET 200AL module into a configuration of the ET 200SP distributed I/O system (mixed configuration ET 200AL/ET 200SP with ET connection), you must open the dialog "Assign PROFIsafe address" in the device view of the ET 200SP separately for each fail-safe ET 200AL module.
4. Under "Assign PROFIsafe address by", select the method to be used for identifying the F-modules.

   - "Identification by LED flashing"

     This is the default setting. The DIAG and STATUS LEDs of the F-modules to be identified flash upon identification.
   - "Identification by serial number"

     If you cannot see the fail-safe modules directly, you can identify the fail-safe modules by the noted serial number of the F-CPU or interface module.

     > **Note**
     >
     > The displayed serial number may be amended with a year number compared to the serial number printed on the F-CPU or the interface module. The serial numbers are nevertheless identical.
5. In case of "Identification by LED flashing", select all fail-safe modules to which you want to assign the PROFIsafe address in the "Assign" column.

   If you select the F-CPU or the interface module in the "Assign" column, all F-modules of the station are selected.
6. Click the "Identification" button. Check whether the DIAG and STATUS LEDs for the F-modules whose PROFIsafe address you want to assign are flashing green. If you identify using the serial number, compare the displayed serial number to the noted serial number of the F-CPU with central fail-safe modules or the interface module with fail-safe modules.

   Observe the following behavior for certain F-modules and configuration variants:

   - If you have configured more F-modules than actually exist, a dialog is displayed. In this dialog, enter the number of F-modules actually existing and confirm the dialog.
   - If you have configured fewer F-modules than are actually available, an online-offline difference is shown and the assignment of the PROFIsafe address is not possible.

#### Assign PROFIsafe address

##### Requirement

The F-modules have been successfully identified.

##### Procedure

To assign a PROFIsafe address, proceed as follows:

1. In the "Confirm" column, select all the fail-safe modules to which you want to assign the F-source address and F-destination address.
2. Use the "Assign PROFIsafe address" button to assign the PROFIsafe address to the fail-safe modules. You may have to enter the password of the F-CPU.

   To assign the PROFIsafe address, you must confirm the "Confirm PROFIsafe address assignment" dialog within 60 seconds.

#### Assigning PROFIsafe address to an F-module in a shared device in multiple projects

##### Introduction

The assignment of the PROFIsafe address for a F-module in a shared device in different projects can only take place after the selection of the IO Controller (F-CPU) to which the F-module is assigned

Therefore, only the F-modules that are assigned to an IO controller (F-CPU) of this project can be selected for assigning the PROFIsafe address in the "Assign PROFIsafe address" dialog.

##### Requirement

The following requirements must be met:

- All requirements from the sections "[Identifying F-modules](#identifying-f-modules)" and "[Assign PROFIsafe address](#assign-profisafe-address)".
- The hardware configuration of all IO controllers (F-CPUs) to which an F-module from the shared device has been assigned is loaded.
- All IO controllers (F-CPUs) to which an F-module from the shared device has been assigned and the shared device must be located in the same subnet.

##### Procedure

To identify the F-modules and assign the PROFIsafe address, proceed as described in sections "[Identifying F-modules](#identifying-f-modules)" and "[Assign PROFIsafe address](#assign-profisafe-address)".

If the F-modules in a shared device are assigned to several IO controllers (F-CPUs) in different projects, make the assignment from the different projects one after the other.

---

**See also**

[Configuring shared device](#configuring-shared-device)

#### Assigning PROFIsafe address to an F-module in a shared device in a common project

##### Introduction

The assignment of the PROFIsafe address for a F-module in a shared device in a common project can only take place after the selection of the IO Controller (F-CPU) to which the F-module is assigned.  
Therefore, only the F-modules that are assigned to the selected IO controller (F-CPU) can be selected for assigning the PROFIsafe address in the "Assign PROFIsafe address" dialog.

##### Requirement

The following requirements must be met:

- All requirements from the sections "[Identifying F-modules](#identifying-f-modules)" and "[Assign PROFIsafe address](#assign-profisafe-address)".
- The hardware configuration of all IO controllers (F-CPUs) to which an F-module from the shared device has been assigned is loaded.
- All IO controllers (F-CPUs) to which an F-module from the shared device has been assigned and the shared device must be located in the same subnet.

##### Procedure

To identify the F-modules and assign the PROFIsafe address, proceed as described in sections "[Identifying F-modules](#identifying-f-modules)" and "[Assign PROFIsafe address](#assign-profisafe-address)".

If the F-modules in a shared device in a common project are assigned to several IO controllers (F-CPUs), select an IO controller in the "Assign PROFIsafe address" dialog and first carry out the assignment for the F-modules that are assigned to the selected IO controller. Subsequently you select further IO controllers and proceed accordingly.

---

**See also**

[Configuring shared device](#configuring-shared-device)

#### Changing the PROFIsafe address

##### Changing the PROFIsafe address

> **Note**
>
> Keep in mind that after changing the PROFIsafe address of an F-I/O you must also carry out an [acceptance](#completeness-and-correctness-of-the-hardware-configuration) including a [check of your change](#acceptance-of-changes) in the [safety summary](#creating-a-safety-summary).

1. You change the PROFIsafe address (F-destination address, F-source address) in the hardware configuration.
2. Compile the hardware configuration.
3. Download the hardware configuration to the F-CPU.
4. Select "Assign PROFIsafe address" from the shortcut menu.
5. Proceed as described under [Identifying F-modules](#identifying-f-modules) and [Assign PROFIsafe address](#assign-profisafe-address).

### Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices

#### Requirement

In order to use fail-safe GSD based DP slaves for SIMATIC Safety, these GSD based slaves must be operated on PROFIBUS DP and support the PROFIsafe bus profile. When used in an S7-1200/1500 F-CPU, they must support the PROFIsafe bus profile in V2 mode.

Fail-safe GSD based DP slaves used in hybrid configurations on PROFIBUS DP and PROFINET IO downstream from a IE/PB link must support the PROFIsafe bus profile in V2 mode.

In order to use fail-safe GSD based I/O devices for SIMATIC Safety, the GSD based devices must be operated on PROFINET IO and support the PROFIsafe bus profile in V2 mode.

#### Configuration with GSD files

As is the case in a standard system, the basis for configuring fail-safe GSD based DP slaves/IO devices is the device specification in the GSD file (device master file).

A GSD file contains all of the properties of a GSD based DP slave or GSD based I/O device. For fail-safe GSD based DP slaves/GSD based I/O devices, certain parts are protected by a CRC.

The GSD files are supplied by the device manufacturers.

#### Protection of the data structure of the device in GSD files

The only GSD files supported are those that satisfy the requirements for protection defined as of PROFIsafe Specification V2.0 using a CRC stored in this file ("setpoint" for F_IO_StructureDescCRC).

The data structure described in the GSD file is checked when the F-I/O is added to the hardware configuration and when the hardware configuration is compiled. When an error is detected, you should clarify whether the GSD file provided by the device manufacturer contains the setpoint for F_IO_StructureDescCRC.

#### Assignment and setting of the PROFIsafe address

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Check the documentation for your fail-safe GSD based DP slaves / fail-safe GSD based I/O devices to find out the valid PROFIsafe address type. If you do not find the necessary information, assume PROFIsafe address type 1. Proceed as described under [PROFIsafe addresses for F-I/O of PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1) or [PROFIsafe addresses for F-I/O of PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2).  Set the F-source address for fail-safe GSD based DP slaves / fail-safe GSD based I/O devices according to the manufacturer's specifications. If the F-source address needs to correspond to the "Central F-source address" parameter of the F-CPU (PROFIsafe address type 2), you will find the latter in the "Properties" tab of the F-CPU. In this case, check the safety summary to verify that the value for the "Central F-source address" parameter corresponds to the value of the F-source address of the fail-safe GSD based DP slave/fail-safe GSD based I/O device. (S053) |  |

#### Configuration procedure with GSD files

You import the GSD files to your project (see Help on STEP 7 "GSD files").

1. Select the fail-safe GSD based DP slave / GSD based I/O device in the "Hardware catalog" task card and connect it to the relevant subnet in the network view.
2. Select the fail-safe GSD based DP slave/GSD based I/O device and insert the necessary F-modules, if this does not occur automatically.
3. Select the relevant F-module and open the "Properties" tab in the inspector window.

For fail-safe GSD based DP slaves/GSD based I/O devices (contrary to other F-I/O), the "Manual assignment of F-monitoring time" parameter is enabled. The result is that the value specified in the GSD file for the F-monitoring time is used as default value when the slaves/devices are plugged. You can change both values (time and type of assignment) later manually.

#### F-parameter "F_CRC_Seed" and "F_Passivation" for fail-safe GSD based I/O devices

The F-parameters "F_CRC_Seed" and "F_Passivation" influence the behavior of a fail-safe GSD based I/O device. The combination of the F-parameters cannot be set but is specified by selecting a corresponding F-module. Up to three F-module variants can be used, depending on the S7-300/400 or S7-1200/1500 F-CPU used.

| F-module variant | F_CRC_Seed | F_Passivation | Behavior of the fail-safe GSD based I/O device | Can be used with F-CPU |
| --- | --- | --- | --- | --- |
| 1 | Parameter does not exist | Parameter does not exist | The GSD based I/O device works with the Basic Protocol (BP) from PROFIsafe.  The "RIOforFA-Safety" profile is not supported. | S7-300/400/1200/1500* |
| 2 | CRC-Seed24/32 | Device/module | The GSD based I/O device works with the Expanded Protocol (XP) from PROFIsafe.  The "RIOforFA-Safety" profile is not supported. | S7-1200/1500 |
| 3 | CRC-Seed24/32 | Channel | The GSD based I/O device works with the Expanded Protocol (XP) from PROFIsafe.  The "RIOforFA-Safety" profile is supported. | S7-1200/1500 |
| * Only use the F-module variant 1 with S7-1200/1500 F-CPUs if neither F-module variant 2 nor 3 exists. |  |  |  |  |

#### More information

You can find the description of the parameters in the Help on fail-safe GSD based DP slaves and GSD based I/O devices.

## Safety Administration Editor

This section contains information on the following topics:

- [Safety Administration Editor](#safety-administration-editor-1)
- [Opening the Safety Administration Editor](#opening-the-safety-administration-editor)
- ["General" area](#general-area)
- ["F-runtime group" area](#f-runtime-group-area)
- ["F-blocks" area](#f-blocks-area)
- ["F-compliant PLC data types" area (S7-1200, S7-1500)](#f-compliant-plc-data-types-area-s7-1200-s7-1500)
- [“Web server F-Admins” area (S7-1200, S7-1500)](#web-server-f-admins-area-s7-1200-s7-1500)
- ["Settings" area](#settings-area)
- ["Flexible F-Link" area (S7-1200, S7-1500)](#flexible-f-link-area-s7-1200-s7-1500)

### Safety Administration Editor

#### Overview

The Safety Administration Editor supports you as follows:

- Displaying of status of safety mode
- Disabling safety mode
- (S7-1200, S7-1500) Displaying and changing the Fast Commissioning Status
- Displaying of status of the safety program
- Displaying of Collective F-Signature
- (S7-1200, S7-1500) Show Collective F-SW-Signature
- (S7-1200, S7-1500) Show Collective F-HW-Signature
- (S7-1200, S7-1500) F-communication address signature
- (S7-1200, S7-1500) Specify/change serial number for F-CPU identification
- Creating a safety summary
- Creating and organizing of F‑runtime groups
- Displaying information on the F-blocks
- Displaying information about F-compliant PLC data types (UDT)
- Specifying/changing access protection
- Information for users with F-Admin permission
- Set/modify settings for the safety program, e.g. Enable F-change history
- (S7-1200, S7-1500) Create/display/delete F-communications via Flexible F-Link

![Overview](images/171697354763_DV_resource.Stream@PNG-en-US.png)

The Safety Administration Editor is divided into the following areas:

- General

  Under "General" the following is displayed:

  - Safety mode status
  - Fast Commissioning Status
  - Safety program status
  - F-signatures
  - F-CPU identification
  - Safety summary

  More information on the "General" area can be obtained in "["General" area](#general-area)".
- F‑runtime group

  You define the blocks and properties of an F‑runtime under "F‑runtime group".

  You can find information on F‑runtime groups at "["F-runtime group" area](#f-runtime-group-area-1)".
- F-blocks

  Under "F‑blocks", you can find information on the F-blocks used in your safety program and their properties . More information on the "F-blocks" area can be obtained in "["F-blocks" area](#f-blocks-area)".
- F-compliant PLC data types

  Under "F-compliant PLC data types", you obtain information on the created F-compliant PLC data types (UDT). There you also obtain information whether or not an F-compliant PLC data type (UDT) is used in the safety program. More information on "F-compliant PLC data types" can be found in "["F-compliant PLC data types" area (S7-1200, S7-1500)](#f-compliant-plc-data-types-area-s7-1200-s7-1500)".
- Access protection

  Under "Access protection", you can set up, change, or revoke the password for the safety program. Alternatively, you can set up access protection for safety-related project data via project protection. Access protection is mandatory for productive operation. More information on access protection can be found in "[CPU-wide access protection for the safety-related project data](#cpu-wide-access-protection-for-the-safety-related-project-data)".
- Web server F-Admins

  Under "Web server F-admins", you obtain information on users with the F-Admin attribute for the Web server of the F-CPU. More information on the "Web server F-Admins" area can be obtained in "[“Web server F-Admins” area (S7-1200, S7-1500)](#web-server-f-admins-area-s7-1200-s7-1500)".
- Settings

  Under "Settings", you set the parameters for the safety program. Information on the settings for your safety program can be found in "["Settings" area](#settings-area)".
- Flexible F-Link

  In the "Flexible F-Link" area, you will find information about the configured F-communications via Flexible F-Link in tabular form and create F-communications. You can obtain information at "["Flexible F-Link" area (S7-1200, S7-1500)](#flexible-f-link-area-s7-1200-s7-1500)".

---

**See also**

[Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)
  
[Program structure of the safety program (S7-300, S7-400)](#program-structure-of-the-safety-program-s7-300-s7-400)
  
[Defining F-Runtime Groups](#defining-f-runtime-groups)

### Opening the Safety Administration Editor

#### Requirement

The Safety Administration Editor is visible as an element in the project tree, if you have configured a CPU as an F‑CPU in the project, which means the "F‑capability activated" option must be selected (in the properties of the F‑CPU).

#### Procedure

To open the Safety Administration Editor, follow these steps:

1. Open the folder for your F-CPU in the project tree.
2. Double-click on "Safety administration" or right-click and select the corresponding shortcut menu for the Safety Administration Editor.

#### Result

The Safety Administration Editor for your F-CPU opens in the work area.

### "General" area

#### "Safety mode status"

The "Safety mode status" shows the current status of safety mode. The prerequisite is an existing online connection to the selected F-CPU.

The following statuses are possible:

- "Safety mode is activated"
- "The safety mode is not activated"
- "F‑CPU is in STOP"
- "No active F-CPU available"
- "F‑runtime group was not called"
- "The safety program is not called"
- "(No online connection)"

#### "Disable safety mode"

For existing online connection and active safety mode operation, you have the option of using the "Disable safety mode" button to disable safety mode for the selected F-CPU. Safety mode can be deactivated only for the entire safety program and not for individual F-runtime groups.

For more information, refer to the section "[Disabling safety mode](#disabling-safety-mode-1)".

#### "Fast Commissioning Status"

To use the Fast Commissioning mode, make sure that the option "Safety mode can be disabled" is selected in the ["Settings" area](#settings-area) and that the safety program was compiled consistently. The Fast Commissioning mode can be executed with "Fast Compile" (default setting) or with "Consistent Compile". For more information, refer to the section "[Safety program in RUN mode (S7-1200, S7-1500)](#safety-program-in-run-mode-s7-1200-s7-1500)".

#### "Safety program status"

"Safety program status" displays the current status of your online and offline program.

The following statuses are possible:

- Consistent

  (With information if no password has been assigned. This information does not apply when project protection is used.)
- Inconsistent
- Modified
- Fast Commissioning mode is active

  (If Fast Commissioning mode was activated with "Fast Compile" and a change was made in the program)

If no connection to the online program could been established, the message "(no online connection)" will be shown.

#### "F-signatures"

**For a non-existing online connection**

Under "F-signatures" multiple signatures are displayed. Each signature is formed from different parts of the fail-safe project data.

- Collective F-Signature: This signature changes with each change of the fail-safe project data. It contains the signatures described below.
- Collective F-SW-Signature (S7-1200, S7-1500): This signature changes with each change of the safety program.
- Collective F-HW-Signature (S7-1200, S7-1500): This signature changes with each change of the fail-safe HW configuration.
- F-Communication address signature (S7-1200, S7-1500): This signature changes with each change of the name or the F-communication UUID of communication connections with Flexible F-Link.

The time of the last compilation process is displayed for the Collective F-Signature in the "Time stamp" column.

**For an existing online connection**

For an existing online connection, the following is displayed under the "Program signature":

- The status of safety program

  | Status | Meaning |
  | --- | --- |
  | !["F-signatures"](images/30303852043_DV_resource.Stream@PNG-de-DE.png) | The online and offline Collective F-Signatures match. |
  | !["F-signatures"](images/30304617483_DV_resource.Stream@PNG-de-DE.png) | The online and offline Collective F-Signatures do not match. |
  | — | The safety program status could not be determined. |
- The online and offline Collective F-Signatures
- When the Collective F‑signatures match: Information on whether the F-block versions are consistent online and offline.

  | Status | Version comparison | Statement |
  | --- | --- | --- |
  | !["F-signatures"](images/69410581259_DV_resource.Stream@PNG-de-DE.png) | Not relevant | The online and offline Collective F‑signatures do not match. |
  | !["F-signatures"](images/69409204235_DV_resource.Stream@PNG-de-DE.png) | !["F-signatures"](images/69410581259_DV_resource.Stream@PNG-de-DE.png) | The online and offline Collective F-Signatures match, but the online versions of F-blocks differ from the offline versions. |
  | !["F-signatures"](images/69409204235_DV_resource.Stream@PNG-de-DE.png) | !["F-signatures"](images/69409204235_DV_resource.Stream@PNG-de-DE.png) | The online and offline Collective F-Signatures match, identical versions of F-blocks are being used online and offline. |
  | Not relevant | — | The safety system versions could not be determined. |

You can find more information on the consistency of the online safety program at under [Identity of online and offline program](#identity-of-online-and-offline-program).

#### "F-CPU identification" (S7-1200, S7-1500)

The serial number of the F-CPU to which the safety program is to be downloaded is entered under "F-CPU identification". This serial number is used to ensure connection to the correct F-CPU in the network. If the serial number is not entered at the time of download to the F-CPU, you must confirm it in the "Load preview" dialog to be able to continue the download. The confirmed serial number is then automatically entered in this field.

#### "Safety summary"

Under "Safety summary", you have the option to create the [safety summary](#creating-a-safety-summary) for the F-CPU.

---

**See also**

[Program identification](#program-identification)

### "F-runtime group" area

This section contains information on the following topics:

- ["F-runtime group" area](#f-runtime-group-area-1)
- [Pre-/postprocessing (S7-1200, S7-1500)](#pre-postprocessing-s7-1200-s7-1500)

#### "F-runtime group" area

A safety program consists of one or two F‑runtime groups.

General information on F-runtime groups can be found in "[Program structure of the safety program (S7-300, S7-400)](#program-structure-of-the-safety-program-s7-300-s7-400)" and "[Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)".

You can find information on creating F‑runtime groups at [Defining F-Runtime Groups](#defining-f-runtime-groups)

##### (S7-1200, S7-1500) "Creating a global F-I/O status block"

You can create a standard block (FB) with the name "RTGx_GLOB_FIO_STATUS", which evaluates whether substitute values are output instead of process values for at least one F-I/O or at least one channel of an F-I/O of an F-runtime group x. The result of the evaluation is available at the "QSTATUS" output.

The following are not included:

- F-I/O that you disabled with the DISABLE tag in the F-I/O DB.
- Channel error of channels that you disabled when configuring an F-I/O.

The "RIOforFA_VALUE_STATUS" output is set to "1" if no substitute value is output for **any** F-I/O **with "RIOforFA-Safety"** profile of the F-runtime group x.

To generate this standard FB, you use the "Create global F-I/O status block" button. You can only create the standard FB when your safety program has been compiled. You can call the standard FB anywhere in your standard user program.

> **Note**
>
> When adding or deleting an F-I/O, you have to generate "RTGx_GLOB_FIO_STATUS" again.

---

**See also**

[Process Data or Fail-Safe Values](#process-data-or-fail-safe-values)

#### Pre-/postprocessing (S7-1200, S7-1500)

With preprocessing and postprocessing you have the option of calling standard blocks (FCs) directly before or after an F-runtime group, for example for data transfer with fail-safe communication via [Flexible F-Link](#configuring-and-programming-communication-with-flexible-f-link-s7-1200-s7-1500).

##### Requirement

- Only standard-FCs usable.
- Only temporary local data and constants are permitted in the block interface of a standard-FC.
- (S7-1500) If the F-runtime group is located in a Safety Unit and FCs are to be used outside the Safety Unit, these FCs must be published and their Software Unit must be connected to the Safety Unit via a relation.

##### Procedure

1. Create the standard-FCs for the preprocessing and the postprocessing.
2. Assign the standard-FCs in the Safety Administration Editor under "Pre-/postprocessing of the F-runtime group".

   ![Procedure](images/113842946699_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > When you delete an assigned FC or overwrite it by copying, its selection as a pre-processing / post-processing block is automatically reset.

##### Effect on the safety program

- The runtime of the F-runtime group is extended by the runtime of the standard FCs for pre-/postprocessing (influence on TRTG_CURR and TRTG_LONG in the F-runtime group information DB).
- Because the preprocessing / postprocessing does not change the functionality of the safety program, the Collective F-Signature remains unchanged after compilation.

##### Load behavior

The calls of the selected standard FCs are placed during compiling or after the call of the main safety block in the F-OB.  
This means that the STOP operating state is required during a subsequent download.

Changes in the contents at the selected standard FCs can take place in RUN.

Exceptions are changes of the block name and block numbers which also include the compilation of the safety program.

When a preprocessing/postprocessing block is uploaded individually by the F-CPU, it does not automatically connect to the F-runtime group in the Safety Administration Editor.

If consistent loading of the F-CPU into the PG/PC is performed instead, the settings for preprocessing and postprocessing are updated according to the online CPU.

### "F-blocks" area

#### Overview

The "F-Blocks" area helps you in the following tasks:

- Displaying the F-blocks used in your safety programs.
- Displaying the F-blocks used in the F-runtime groups.
- Displaying additional information about the F-blocks.

The F-blocks are hierarchically displayed as in the "Program blocks" folder.

A description of the F-blocks is available in "[Creating F-blocks in FBD / LAD](#creating-f-blocks-in-fbd-lad)".

#### Displayed information

The following information is displayed in offline mode:

- Have displayed F-blocks been compiled and used?
- Function of F-blocks in safety program
- Block signature
- Group signature
- Change time stamp of the F-blocks

The following information is displayed in online mode:

- Status (whether block has the same time stamp online and offline)
- Function of F-block in the safety program
- Block signature offline
- Group signature offline
- Block signature online
- Group signature online

> **Note**
>
> During the offline-online comparison, the comparison statuses may occasionally differ between the comparison editor and status display in the Safety Administration Editor. The decisive status is the result of the comparison in the comparison editor, since this is the only comparison that takes into account the contents of the F-blocks.

> **Note**
>
> Group signatures are formed from the signatures of the F-blocks contained in the group and in subgroups. Only F-blocks that are used in the safety program are taken into account. Only the group signatures up to the 6th hierarchy level are displayed.

#### Filter function

![Filter function](images/28209673483_DV_resource.Stream@PNG-en-US.png)

Using the filter function, you can select whether you want to view all F-blocks of a certain F-runtime group or the entire safety program.

- Select "All F-blocks " from the drop-down list to view all F-blocks.
- Select an F-runtime group from the drop-down list to see all F-blocks of this F-runtime group.

### "F-compliant PLC data types" area (S7-1200, S7-1500)

#### Overview

Under "F-compliant PLC Data Types" you obtain information on the F-compliant PLC data types (UDT) you have defined.

You can delete F-compliant PLC data types (UDT) from the shortcut menu.

A description of F-compliant PLC data types (UDT) is available in "[F-compliant PLC data types (UDT) (S7-1200, S7-1500)](#f-compliant-plc-data-types-udt-s7-1200-s7-1500-1)".

#### Displayed information

The following information is displayed for F-compliant PLC data types (UDT) in offline mode:

- Is the F-compliant PLC data type used in the safety program?
- Time stamp of the last change.

The following information is displayed for F-compliant PLC data types (UDT) in online mode:

- Status (whether the F-compliant PLC data types (UDT) have the same time stamp online and offline)

The F-compliant PLC data types (UDT) are displayed hierarchically as in the folder "PLC Data Types".

Double-click the F-compliant PLC data type (UDT) to open it for editing.

The description of the symbols in the "Status" column can be found in "[Comparing Safety Programs](#comparing-safety-programs)".

> **Note**
>
> During offline-online comparison, the comparison statuses between the comparison editor and status display in the Safety Administration Editor can be different under certain circumstances. The comparison result in the comparison editor is decisive, since this is the only comparison that takes into account the contents of the F-compliant PLC data types (UDT).

### “Web server F-Admins” area (S7-1200, S7-1500)

You need "F-admin" rights in order to [restore a backup](#restoring-a-backup-of-the-safety-program-to-an-f-cpu) via the Web server or Web API interface of your F-CPU. You assign the "F-admin" right in the hardware configuration of the F-CPU under the user management of the Web server.

In this section, you obtain information on which users have the "F-admin" right online or offline for F-CPUs that support this right. You can see from this whether a change to the "F-admin" right is active on the F-CPU. In order to make a change to the "F-admin" right effective, you have to load the configuration to the F-CPU.

If you are using local user management, this area is omitted

---

**See also**

[Completeness and correctness of the hardware configuration](#completeness-and-correctness-of-the-hardware-configuration)

### "Settings" area

#### "Number ranges of the generated F-system blocks"

The number ranges assigned here are used by the F-System for new, automatically generated F-blocks.

At this point, you can select whether the number ranges are managed by the F-system or if a fixed range specified by you is used.

- "F-system managed"

  The number ranges are managed automatically by the F-system, depending on the F-CPU used. The F-system selects an available number range. The start and end ranges of the number ranges are displayed.
- "Fixed range"

  You can select the start and end ranges of the number ranges from the available range. The available range depends on the F-CPU used.

  An invalid number range selection is indicated by an error message.

  The only check performed during configuration is whether the configured low limit is less than or equal to the high limit and within the available range of the F-CPU. The check as to whether the configured range is sufficiently large is first made during compiling. You need to ensure a sufficiently large range. Where the available range is insufficient, a compiling error occurs. Not all blocks are generated and the safety program is not executable.

Changes will become valid only during the next compilation. The automatically created F-blocks may be moved into the new area during compilation. The F-I/O DBs are an exception. They always retain their original number that you may change in the properties of the F-I/O.

#### "Safety system version"

This parameter is used to specify the safety system version (including version of the F-system blocks and automatically generated F-blocks, see [Overview of Programming](#overview-of-programming)).

A number of versions are available:

| Version<sup>3</sup> | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.6 | — | x | x | These versions have identical functions.  Depending on the set version, the result may be different runtimes of the F-runtime group(s) (see Excel file for response time calculation on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109783831)). |
| 2.0 | x | x<sup>1</sup> | x<sup>2</sup> |  |
| 2.1 | — | x<sup>1</sup> | x<sup>2</sup> | Additionally supports the variables "DISABLE" and "DISABLED" in the F-I/O DB |
| 2.2 | — | x<sup>1</sup> | x<sup>2</sup> | Supports the safety-related CPU-CPU communication and F-runtime group communication with Flexible F-Link. |
| 2.3 | — | x<sup>1</sup> | x<sup>2</sup> | This version has identical functions to version 2.2. |
| 2.4 | — | x<sup>1, 4</sup> | x<sup>2</sup> | Additionally supports:  - F-CPUs - Fast Commissioning mode with "Fast Compile" - Runtime for the deactivated safety mode |
| 2.5 | — | x | x<sup>5</sup> | Additionally supports:  - Fast Commissioning mode with "Consistent Compile" (S7-1500) - F-I/O with more than 13 bytes net data (e.g. F-AI 8xI 0(4)..20mA) |
| 2.6 | — | x | x | The functions of this version are identical to those of version 2.5. |
| <sup>1</sup> Supported as of firmware V4.2   <sup>2</sup> Supported as of firmware V2.0   <sup>3</sup> After the migration of projects that were created with S7 Distributed Safety V5.4 SP5, version 1.0 is set automatically in order to identify migrated projects which have not yet been compiled with STEP 7 Safety Advanced.   <sup>4</sup> Fast Commissioning mode with "Fast Compile" is supported as of firmware V4.5.   <sup>5</sup> Fast Commissioning mode with "Consistent Compile" is supported as of firmware V3.0. With the S7-1500 F-Software Controller, it is available only for approved IPCs as of firmware V30.0. |  |  |  |  |

Usually, you do not need to make any settings for this parameters.

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

#### "Local data used in safety program" (S7-300, S7-400)

You use this parameter to specify the amount of temporary local data (in bytes) that is available for the call hierarchy below the main safety block.

The setting applies to each F-runtime group of a safety program. More information on F-runtime groups can be found in "[Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)" and "[Program structure of the safety program (S7-300, S7-400)](#program-structure-of-the-safety-program-s7-300-s7-400)".

The **minimum possible amount** is determined by the local data requirement of the F-blocks generated automatically when the safety program is compiled.

For this reason, you must provide at least 440 bytes. However, the local data requirement for the automatically added F-blocks may be higher depending on the local data requirement of the F-blocks you created with FBD or LAD.

Therefore, provide as much local data as possible. If there is not enough local data available for the automatically added F‑blocks (440 bytes or more), the safety program will be compiled nevertheless.

Data in automatically added F-DBs are then used instead of local data. However, this increases the runtime of the F-runtime group(s). You will receive a notice when the automatically added F-blocks require more local data than configured.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The calculated maximum runtime of the F-runtime group using the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) is no longer correct in this case because the calculation assumes sufficient availability of F-local data.  In this case, use the value you configured for the maximum cycle time of the F‑runtime group (F‑monitoring time) as the maximum runtime of the F‑runtime group when calculating the maximum response times in the event of an error and for any runtimes of the standard system using the above-mentioned Excel file. (S004) |  |

The maximum possible amount depends on:

- Local data requirement of the main safety block and the higher-level standard user program. For this reason, you should call the main safety blocks directly in OBs (cyclic interrupt OBs, whenever possible), and additional local data should not be declared in these cyclic interrupt OBs.
- Maximum volume of local data of the utilized F‑CPU (see Technical Specifications in the product information for the utilized F‑CPU). For S7-400 F-CPUs, you can configure the local data for each priority class. Therefore, assign the largest possible local data volume for the priority classes in which the safety program (the main safety blocks) is called (e.g., OB 35).

#### Maximum possible amount of local data as a function of local data requirement of main safety block and higher-level standard user program (S7-300, S7-400):

**Case 1: Main safety block called directly from OBs**

![Maximum possible amount of local data as a function of local data requirement of main safety block and higher-level standard user program (S7-300, S7-400):](images/170239096331_DV_resource.Stream@PNG-en-US.png)

Set the "Local data used in safety program" parameter to the maximum amount of local data of the utilized F-CPU minus the local data requirement of the main safety block (if the main safety block has 2 F-runtime groups, use the largest local data requirement) and minus the local data requirement of the calling OBx (if there are 2 F-runtime groups, use the OB with the largest local data requirement).

**Note:** If you have not declared any temporary local data in the main safety blocks and calling OBx, the local data requirement of the main safety blocks is 6 bytes and the local data requirement of the calling OBx is 26 bytes. You can derive the local data requirement of the main safety blocks and calling OBx from the program structure.

Select the utilized F-CPU in the project tree and then "Tools > Call structure". The table gives the local data requirement in the path or for the individual blocks (see also the help on STEP 7).

**Case 2: Main safety block not called directly from OBs**

![Maximum possible amount of local data as a function of local data requirement of main safety block and higher-level standard user program (S7-300, S7-400):](images/170239165195_DV_resource.Stream@PNG-en-US.png)

Set the "Local data settings" parameter to the value calculated for Case 1, minus the local data requirement of standard user program A (if standard user program A has 2 F-runtime groups, use the largest local data requirement).

**Note:** You can derive the local data requirement of the standard user program A from the program structure.

Select the utilized F-CPU in the project tree and then "Tools > Call structure". The table gives the local data requirement in the path or for the individual blocks (see also the help on STEP 7).

#### "Advanced settings"

**"Safety mode can be disabled"**

With this option you can prevent the safety mode for a safety program from being disabled.

Under "Runtime for the deactivated safety mode", you set the time after which the F-CPU goes to STOP after safety mode is deactivated.

When you change the setting for this option, you need to recompile the safety program and download it to the F-CPU for the change to become effective. This changes the Collective F-Signature and the Collective F-SW-Signatures of your safety program.

To exclude an unintentional disabling of the safety mode, make sure that the option is disabled in productive operation.

**"Enable F-change history"**

Enable the logging of changes to the safety program by using the "Enable F-change history" option. For more information, refer to the section "[F-change history](#f-change-history)".

**"Enable consistent upload from the F-CPU" (S7-1500)**

This option allows you to load the loaded project data (including safety-related project data) consistently from the F-CPU to the PG/PC.

The option can only be activated if the F-CPU and the firmware of the F-CPU supports the loading of the project data (including safety-related project data).

F-CPUs S7-1500 as of firmware V2.1 are supported. S7-1500 F Software Controllers are not supported.

At every change to this option you have to load the project data to the F-CPU.

Note that the activation of this option extends the loading of the safety-related project data into the F-CPU.

**"Activate variable F-communication- IDs" (S7-1200, S7-1500)**

If you activate this option, you can supply the DP_DP_ID input of the SENDDP or RCVDP instructions with the variable values from a global F-DB.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide**** at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".

*** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase.

**** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one single F-CPU with regard to the DP_DP_ID.

#### "System-generated objects" (S7-1200, S7-1500)

**"**
**Creates F-I/O DBs without prefix**
**"**

When you select this option, the [names of the F-I/O DBs](#name-and-number-of-the-f-io-db) are created without prefix.

**"**
**Clean up**
**"**

The "Clean up" button is provided for service and support purposes and cleans up the result of the fail-safe compilation.

### "Flexible F-Link" area (S7-1200, S7-1500)

In the "Flexible F-Link" area, you create new F-communications, obtain information on existing F-communications and delete F-communications.

#### Requirement

- S7-1500 F-CPUs as of firmware V2.0
- S7-1200 F-CPUs as of firmware V4.2
- Safety system version as of V2.2

#### Information on created F-communications

In the "Flexible F-Link" area, you receive information on configured F-communications in tabular form:

- CPU-wide unique name of F-communication
- F-compliant PLC data type (UDT) for send/receive data
- Direction of F-communication: Transmitting/receiving
- F-monitoring time of F-communication
- F-Communication UUID
- Tag for send data
- Tag for receive data

#### Creating F-communication

1. In an empty row of the table click "<Add new>"
2. Assign a name to the communication connection.
3. Select an F-compliant PLC data type (UUID) for the communication connection.

   If you have not yet created an F-compliant PLC data type (UDT) for the communication connection or wish to create a new one, create a [new F-compliant PLC data type (UDT)](#f-compliant-plc-data-types-udt-s7-1200-s7-1500) with any structure. Note that the size can be a up to 100 bytes.
4. Select the direction of the communication connection ("Send" or "Receive").
5. Select the [F-monitoring time of the communication connection](#configuring-the-monitoring-times).

The UUID of the F-communication is displayed via Flexible F-Link in the "F communication UUID" column. The F-communication UUID ensures sufficient uniqueness of the safety-related communication ID even across network limits.

The "Tag for send data" column shows you the newly created tag for send data of the [F-communication DB](#f-communication-db-s7-1200-s7-1500).

The "Tag for receive data" column shows you the newly created tag for receive data of the [F-communication DB](#f-communication-db-s7-1200-s7-1500).

You can find the newly created F-communication DB for this F-communication under "Program blocks\System blocks\STEP 7 Safety\F-communication DBs".

#### Deleting F-communication

1. Select the entire row and confirm "Delete" in the shortcut menu. You can also delete multiple F-communications at the same time.

#### Copying F-communication

1. Select the entire row and confirm "Copy" in the shortcut menu. You can also copy multiple F-communications at the same time.
2. With the "Paste" menu command, you can paste the copied F-communications into the table as often as needed. The UUID for the respective F-communication is retained during copying. If necessary, re-generate the UUID.

#### Generating a new F-communication-UUID

1. Select the entire row and confirm "Generate UUID" in the shortcut menu. You can also generate multiple UUIDs at the same time.

---

**See also**

[Flexible F-Link](#flexible-f-link)
  
[F-runtime group communication (S7-1200, S7-1500)](#f-runtime-group-communication-s7-1200-s7-1500)

## Access protection

This section contains information on the following topics:

- [Introduction to access protection](#introduction-to-access-protection)
- [Overview of access protection](#overview-of-access-protection)
- [Access protection for the safety-related project data](#access-protection-for-the-safety-related-project-data)
- [Access protection for the F-CPU](#access-protection-for-the-f-cpu)
- [Access protection through organizational measures](#access-protection-through-organizational-measures)

### Introduction to access protection

#### Access protection is necessary for productive operation

Access protection to the SIMATIC Safety F‑system is mandatory for productive operation.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Access to the SIMATIC Safety F‑system without access protection is intended for test purposes, commissioning, etc., when the system is not in productive operation. Without access protection, you need to ensure the safety of the plant through other [organizational measures](#glossary).   **Before you transition into productive operation, you must have set up and activated access protection.**  (S005) |  |

> **Note**
>
> We recommend making the settings for access protection in the "PLC security settings" dialog when creating the project.

### Overview of access protection

#### Introduction

You can control access to the SIMATIC Safety F-system with the access protection for the safety-related project data and the password for the F‑CPU.

#### Access protection for the safety-related project data

[Access protection for the safety-related project data](#access-protection-for-the-safety-related-project-data) is available in two forms:

- Assignment of a password for the safety-related project data (F-CPU-granular), assigned in the Safety Administration Editor
- Setup of project protection for all safety-related project data in the TIA project

#### Access protection for the F‑CPU

The [access protection](#access-protection-for-the-f-cpu-1) is set at the F‑CPU level. To do so, you assign a password for the F‑CPU in the F-CPU configuration. For S7-300/400 F-CPUs, the password is also used to identify the F‑CPU and must therefore be unique network-wide. For S7-1200/1500 F-CPUs, the password no longer needs to be unique because the serial number is used for identification.

### Access protection for the safety-related project data

This section contains information on the following topics:

- [Access protection for the safety-related project data](#access-protection-for-the-safety-related-project-data-1)
- [CPU-wide access protection for the safety-related project data](#cpu-wide-access-protection-for-the-safety-related-project-data)
- [Project-wide access protection for the safety-related project data](#project-wide-access-protection-for-the-safety-related-project-data)

#### Access protection for the safety-related project data

The access protection for the safety-related project data is effective for all operations in which the safety-related project data can be changed offline, for example:

- When modifying the safety program
- When changing and deleting F-runtime groups
- When changing safety-related parameters of F-I/O
- When compiling

> **Note**
>
> Note that the access protection for the safety-related project data is only effective if you are making the changes in the TIA Portal. Although the TIA Portal detects changes to the project data made directly in the related files in the file system, these changes cannot be prevented or undone.

Safety program recompilation is required after changes to standard DBs to which the safety program has read or write access.

#### CPU-wide access protection for the safety-related project data

##### Requirement

The project does not use local user management.

##### Setting up CPU-wide access protection for safety-related project data

To set up CPU-wide access protection for safety-related project data, assign a password for the safety program. Proceed as follows:

1. Open the folder for your F-CPU in the project tree.
2. Select "Safety Administration" and select "Go to access protection" in the shortcut menu.

   Alternatively, double-click on "Safety Administration". The Safety Administration Editor of the F-CPU will open. Select "Access protection" in the navigation area.
3. Under "Offline safety program protection", click "Setup" and enter the password (max. 30 characters) for the safety program in the following dialog in the "New password" and "Confirm password" fields.
4. Confirm the assigned password with "OK".

You have set up CPU-wide access protection for safety-related project data and have gained access permission for the safety-related project data.

> **Note**
>
> Use different passwords for the F‑CPU and the safety program to optimize access protection.

##### Changing the password for safety-related project data

You can change the password for the safety-related project data as long as you have the necessary access permissions. It also takes place in the "Access protection" area (via "Change" button) and is carried out as usual under Windows through entry of the old and double entry of the new password.

##### Deleting CPU-wide access protection for safety-related project data

To delete CPU-wide access protection for safety-related project data, delete the password for the safety program. Proceed as follows:

1. Open the folder for your F-CPU in the project tree.
2. Select "Safety Administration" and select "Go to access protection" in the shortcut menu.

   Alternatively, double-click on "Safety Administration". The Safety Administration Editor of the F-CPU will open. Select "Access protection" in the navigation area.
3. Click the "Change" button.
4. Under "Old password", enter the password for the safety program.
5. Click "Revoke" and then on "OK".

##### Gaining access permission through login to the safety program

Log in to the safety program as follows:

1. Open the folder for your F-CPU in the project tree.
2. Select "Safety Administration" and select "Go to access protection" in the shortcut menu.

   Alternatively, double-click on "Safety Administration". The Safety Administration Editor of the F-CPU will open. Select "Access protection" in the navigation area.
3. Enter the password for the safety program in the "Password" input field.
4. Select the "Login" button.

##### Validity of access permission for safety-related project data

If access permission for safety-related project data was obtained by entering the password, this remains until the project is closed. When the TIA Portal is closed, any project that is still open is automatically closed and any access permission granted is canceled.

##### Cancelling access permission through logoff

The access permission for safety-related project data can be cancelled as follows:

- By clicking the "Log off" button in the "Access protection" area in the "Safety Administration Editor".
- In the shortcut menu for the Safety Administration Editor (access by right-clicking).
- By using the lock symbol in the line of the Safety Administration Editor.

The user will then be prompted to enter the password for the safety program again the next time an action requiring a password is performed.

##### Displaying the availability of access authorization

The status of the access authorization is displayed in the project tree as follows:

- The access authorization is available when the lock symbol in the line of the Safety Administration Editor is shown unlocked.
- The access permission is not available, if the lock symbol shows a closed lock.
- If no lock symbol is shown, no password was assigned.

#### Project-wide access protection for the safety-related project data

As an alternative to CPU-wide access protection for the safety-related project data with a password in the Safety Administration Editor, you can use the project protection for the TIA project.

To do this, assign the "Edit safety-related project data" function right to users who are allowed to edit safety-related project data. To do this, proceed as usual for function rights. You can find more information in the help for STEP 7 under "Managing users and roles".

> **Note**
>
> When project-wide project access protection is activated, any existing passwords for safety-related project data for all F-CPUs of the project are deleted.

Users who need the "Edit safety-related project data" function right may require additional function rights, for example:

- "Modify PLC program" to change the safety program
- "Downloading to PLC" to load the safety-related project data into the F-CPU
- "Modify hardware configuration" to make changes to the safety-related hardware configuration

### Access protection for the F-CPU

This section contains information on the following topics:

- [Access protection for the F-CPU](#access-protection-for-the-f-cpu-1)
- [Access protection through the use of protection levels](#access-protection-through-the-use-of-protection-levels)
- [Access protection through the use of local user management](#access-protection-through-the-use-of-local-user-management)

#### Access protection for the F-CPU

The access protection for the F-CPU is effective for all operations in which the safety-related project data can be changed online, for example:

- When downloading the safety program to the F-CPU
- (S7-300, S7-400) When downloading the hardware configuration to the F-CPU, also when changes are made to F-I/O not used in the safety program
- (S7-1200, S7-1500) When downloading a hardware configuration to the F-CPU containing safety-related changes
- When assigning the PROFIsafe address
- When loading or deleting F‑blocks used in the safety program
- When disabling safety mode or when resetting the remaining runtime (the password must always be entered, even if access permission for the F-CPU is still valid.)
- When restoring a backup of the F-CPU

  Exception with S7-1200/1500 F-CPUs: If neither the safety program nor the F-CPU password is changed by the restore process, you are not prompted for the F-CPU password.

#### Access protection through the use of protection levels

This section describes the access protection for F-CPUs through the use of protection levels.

You can use protection levels for S7-300/400/1200 F-CPUs and S7-1500 F-CPUs up to Firmware V3.0.

##### Setting up access protection for the F-CPU

To set up access protection for the F-CPU, assign a password in the F-CPU configuration.

Clicking on the link "Go to the "Protection" area of the F-CPU" in the "Access protection" area of the Safety Administration Editor takes you directly to the password for the F‑CPU. Proceed as described in the STEP 7 help under "Configuring access levels".

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) In productive operation, it must be prevented that changes to the standard user program are unintentionally made in the safety program as well. For this purpose, you must configure the protection level "Write protection for fail-safe blocks" and configure a password for the F‑CPU.  With the "Write protection" or "Write/read protection" protection level, the password would apply to the standard and the safety program. (S001) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) In productive operation, the safety-related project data must be protected against unintentional changes.  If you use local user management, the Runtime rights "F-Admin" and "Full access with fail-safe access" and the engineering right for user management may only be granted to authorized users. You must also limit the assignment of user rights to trained personnel.  If you are not using local user management or if legacy mode is enabled, then, at a minimum, configure protection level "Full access (no protection)" and assign a password under "Full access with fail-safe (no protection)". This protection level allows full access only to the standard user program and not the safety program.  If you select a higher protection level, for example to protect the standard user program, you must assign an additional password for "Full access (no protection)".   Assign different passwords for the individual access levels. (S041) |  |

You enable access protection by [downloading](#downloading-project-data) the hardware configuration to the F-CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) If **several F‑CPUs** can be reached via a network (such as Industrial Ethernet) by **the same programming device or PC**, you must take the following additional measures to ensure that the safety-related project data is downloaded to the correct F‑CPU:  Use passwords specific to each F‑CPU, such as a uniform password for the F‑CPUs with attached Ethernet address for each.  Note the following:  - A point-to-point connection must be used to activate the access protection of an F‑CPU when the hardware configuration is loaded for the first time (similar to assigning an MPI address to an F‑CPU for the first time). - Before downloading the safety-related project data to an F‑CPU, existing access permission for any other F‑CPU must first be cancelled. - The last download of the safety-related project data prior to switching to productive operation must be made with enabled access protection. (S021) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using tools for the automation or operation (of TIA Portal or web server) with which the access protection for the F-CPU can be removed, the safety-related project data may not be protected against unintentional changes anymore. When using corresponding tools, the requirements regarding access protection of the F-CPU must still be met. (S078) |  |

##### Changing the password for the F-CPU

For the new password to become valid after a password change for the F-CPU, you must download the changed configuration into the F-CPU. If necessary, you must enter the "old" password for the F-CPU for this load operation. The F-CPU must be in STOP mode.

##### Deleting access protection for the F-CPU

To delete access protection for the F-CPU, delete the password for the F-CPU. To do this, proceed as in the standard.

##### Obtaining access permission for the F‑CPU

You obtain access permission for the F‑CPU by entering the password for the F‑CPU, according to the configured protection level, prior to performing an action requiring a password.

##### Validity of access permission for the F‑CPU

Access permission for the F‑CPU remains valid until the project is closed in the TIA Portal or access permission is canceled.

##### Canceling access permission for the F‑CPU

You cancel the access permission with the menu command "Online > Delete access rights" auf.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The safety-related project data must be protected against unintentional changes.  For this you must cancel the access permission and the online connection for the F-CPU whenever you leave the PG/PC.   Alternatively, you can also take other [organizational measures](#glossary). (S006) |  |

#### Access protection through the use of local user management

This section describes the access protection for F-CPUs through the use of local user management and the function right for the F-CPU.

You can use local user management for S7-1500 F-CPUs as of Firmware V3.1.

##### Setting up access protection for the F-CPU

To set up access protection for the F-CPU, use the local user management with the function right for the F-CPU.

If the "Use legacy access control via access levels" option is selected in addition to "Enable access control", you must assign a password for the F‑CPU in the F-CPU configuration.

Clicking on the link "Go to the "Protection" area of the F-CPU" in the "Access protection" area of the Safety Administration Editor takes you directly to the password for the F‑CPU. Proceed as described in the STEP 7 help under "Settings for users and roles".

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) In productive operation, the safety-related project data must be protected against unintentional changes.  If you use local user management, the Runtime rights "F-Admin" and "Full access with fail-safe access" and the engineering right for user management may only be granted to authorized users. You must also limit the assignment of user rights to trained personnel.  If you are not using local user management or if legacy mode is enabled, then, at a minimum, configure protection level "Full access (no protection)" and assign a password under "Full access with fail-safe (no protection)". This protection level allows full access only to the standard user program and not the safety program.  If you select a higher protection level, for example to protect the standard user program, you must assign an additional password for "Full access (no protection)".   Assign different passwords for the individual access levels. (S041) |  |

You enable access protection by [downloading](#downloading-project-data) the hardware configuration to the F-CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using tools for the automation or operation (of TIA Portal or web server) with which the access protection for the F-CPU can be removed, the safety-related project data may not be protected against unintentional changes anymore. When using corresponding tools, the requirements regarding access protection of the F-CPU must still be met. (S078) |  |

##### Changing the password for the F-CPU

For the new users or the new password to become valid after a change in the users with F-right or a password change for the F‑CPU, you must download the changed configuration to the F‑CPU and select the "Download User Container" option in the "Load preview" dialog when downloading. For this download, you must legitimate yourself as a user with F-right or enter the existing password for the F‑CPU, if necessary. The F‑CPU must be in STOP mode.

##### Deleting access protection for the F-CPU

To delete access protection for the F-CPU, grant the F-right ("Full access including fail-safe") to the Anonymous user.

##### Obtaining access permission for the F‑CPU

You obtain access permission for the F‑CPU by legitimating yourself as a user with F-right or when legacy mode is enabled by entering the password for the F‑CPU prior to performing an action requiring a password.

##### Validity of access permission for the F‑CPU

Access permission for the F‑CPU remains valid until the project is closed in the TIA Portal, access permission is canceled or the maximum legitimation time is exceeded. A maximum legitimation time of up to 600 minutes can be set for each user.

##### Canceling access permission for the F‑CPU

You cancel the access permission with the menu command "Online > Delete access rights" auf.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The safety-related project data must be protected against unintentional changes.  For this you must cancel the access permission and the online connection for the F-CPU whenever you leave the PG/PC.   Alternatively, you can also take other [organizational measures](#glossary). (S006) |  |

### Access protection through organizational measures

To prevent a safety program from being swapped without authorization by exchanging removable media (e.g. flash card, SIMATIC Micro Memory Card or hard disk with S7-1500 F Software Controller), you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You must limit access to the F-CPU through [organizational measures](#glossary) to persons who are authorized to plug in removable devices. (S079) |  |

To ensure that an S7-1500 F Software Controller is not uninstalled or installed unintentionally, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You must limit access to an S7-1500 F Software Controller by [organizational measures](#glossary) to persons who are authorized to uninstall and install or repair an S7-1500 F Software Controller (e.g. via the Windows administrator privileges (ADMIN)). (S075) |  |

With an S7-1500 F-Software Controller with a PC station version up to incl. V2.1, the function "Delete Configuration" on the PC Station Panel is only offered when no access protection (no protection) is set up on the F-CPU.

With a PC station as of V2.2, it is checked whether the current Windows user is a member of the "Failsafe Operators" Windows user group. When the logged-on Windows user is a member of the group, he/she can execute the "Delete Configuration" function even when the F-password is set. If the logged-on Windows user is not a member of the group, the PC station behaves as up to V2.1.

We therefore recommend that you do not set up F-access protection until after commissioning.

To prevent unintentional restoration of the safety-related project data, formatting of the F-CPU and deletion of program folders via the display of an S7-1500 F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The password for the display of the F-CPU may only be disclosed to persons who are authorized to restore safety-related project data, to format the F-CPU and to delete program folders. If a password is not set up for the display, you must protect the display through [organizational measures](#glossary) against unauthorized operation. (S063) |  |

To prevent unintentional restoration of the safety-related project data of the safety program with the web server in an S7-1200/1500 F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The "F-Admin" authorization for the Web server (including Web server API) without password protection (user "Everybody", or user "Anonymous" when using local user management) is intended only for testing, commissioning, etc. This means only when the system is not in productive operation. In this case, you must ensure the safety of the system through other [organizational measures](#glossary).  Before the transition into productive operation, you must remove "F-Admin" rights and "Full access incl. fail-safe access" from the "Everybody" or "Anonymous" user.  The password Web server user with "F-Admin" right may only be disclosed to authorized persons. After downloading the hardware configuration, check whether only permitted users of the web server have the "F-Admin" right on the F-CPU. To do so, use the online mode of the Safety Administration Editor for an F-CPU without local user management, or the "Security setting\Users and roles" tab for an F-CPU with local user management.  Saving the login file and the password of the Web server in the browser is only permitted when usage by unauthorized persons is prevented through other [organizational measures](#glossary).   If you use the ticket mechanism, handling of the tickets must be just as restrictive as handling of the user password of the web server with the "F-Admin" right. (S064) |  |

## Programming

This section contains information on the following topics:

- [Overview of Programming](#overview-of-programming)
- [Defining F-Runtime Groups](#defining-f-runtime-groups)
- [Creating F-blocks in FBD / LAD](#creating-f-blocks-in-fbd-lad)
- [Information interface to the safety program](#information-interface-to-the-safety-program)
- [Programming startup protection](#programming-startup-protection)

### Overview of Programming

This section contains information on the following topics:

- [Overview of Programming](#overview-of-programming-1)
- [Program structure of the safety program (S7-300, S7-400)](#program-structure-of-the-safety-program-s7-300-s7-400)
- [Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)
- [Safety program in Software Unit (Safety Unit) (S7-1500)](#safety-program-in-software-unit-safety-unit-s7-1500)
- [Fail-Safe Blocks](#fail-safe-blocks)
- [Restrictions in the programming languages FBD/LAD](#restrictions-in-the-programming-languages-fbdlad)
- [F-compliant PLC data types (UDT) (S7-1200, S7-1500)](#f-compliant-plc-data-types-udt-s7-1200-s7-1500)
- [Named value data types (S7-1500)](#named-value-data-types-s7-1500)
- [Editing PLC tags with external editors](#editing-plc-tags-with-external-editors)
- [Using Multiuser engineering](#using-multiuser-engineering)
- [Deleting the safety program](#deleting-the-safety-program)

#### Overview of Programming

##### Introduction

A safety program consists of F-blocks that you create using the FBD or LAD programming language and F-blocks that are automatically added. Fault detection measures and fault reaction measures are automatically added to the safety program you create, and additional safety-related tests are performed. Moreover, you have the option to incorporate special ready-made safety functions in the form of instructions into your safety program.

An overview of the following is given below:

- The structure of the safety program
- The fail‑safe blocks
- Differences in the programming of the safety program with FBD/LAD compared to programming of standard user programs

#### Program structure of the safety program (S7-300, S7-400)

##### Representation of program structure

For structuring purposes, a safety program consists of one or two F-runtime groups.

Each F-runtime group contains:

- F-blocks that you create using FBD or LAD or that are inserted from the project library or global libraries
- F-blocks that are added automatically (F-system blocks, automatically generated F-blocks, and F-I/O DBs)

Below is a schematic diagram of a safety program or an F-runtime group for an S7-300/400 F-CPU.

![Representation of program structure](images/158713677067_DV_resource.Stream@PNG-en-US.png)

##### Main safety block

The main safety block is the first F-block of the safety program that you program yourself. During compiling, it is supplemented by additional invisible calls of F-system blocks.

You must assign the main safety block to an [F-runtime group](#defining-f-runtime-groups).

The main safety block in an S7‑300/400 F-CPU is called from any block in the standard user program. We recommend a call from an OB 3x.

![Main safety block](images/49221744651_DV_resource.Stream@PNG-en-US.png)

##### F-runtime groups

To improve handling, a safety program consists of one or two "F-runtime groups". An F-runtime group is a logical construct of several related F-blocks that is formed internally by the F-system.

An F-runtime group consists of the following:

- A main safety block (an F‑FB/F‑FC that you assign to the calling OB (FB/FC) as needed)
- Any additional F-FBs or F-FCs that you program using FBD or LAD and call from the main safety block
- One or more F-DBs, as needed
- F-I/O DBs
- F-blocks from the project library or global libraries
- F-system blocks F-SBs
- Automatically generated F-blocks

##### Structuring the safety program in two F-runtime groups

You can divide your safety program into two F-runtime groups. By having parts of the safety program (one F-runtime group) run in a faster priority class, you achieve faster safety circuits with shorter response times.

#### Program structure of the safety program (S7-1200, S7-1500)

##### Representation of program structure

For structuring purposes, a safety program consists of one or two F-runtime groups.

Each F-runtime group contains:

- F-blocks that you create using FBD or LAD or that are inserted from the project library or global libraries
- F-blocks that are added automatically (F-system blocks F-SBs, automatically generated F-blocks, F-runtime DB, and F-I/O DBs)

Below is a schematic diagram of a safety program or an F-runtime group for an S7-1200/1500 F-CPU.

![Representation of program structure](images/158700418955_DV_resource.Stream@PNG-en-US.png)

##### Main safety block

The main safety block is the first F-block of the safety program that you program yourself.

You must assign the main safety block to an [F-runtime group](#defining-f-runtime-groups).

The main safety block in an S7‑1200/1500 F-CPU is called by the F-OB assigned to the F-runtime group.

![Main safety block](images/66685903371_DV_resource.Stream@PNG-en-US.png)

##### F-runtime groups

To improve handling, a safety program consists of one or two "F-runtime groups". An F-runtime group is a logical construct of several related F-blocks that is formed internally by the F-system.

An F-runtime group consists of the following:

- An F-OB which calls the main safety block
- A main safety block (an F‑FB/F‑FC that you assign to the F-OB)
- Any additional F-FBs or F-FCs that you program using FBD or LAD and call from the main safety block
- One or more F-DBs, as needed
- F-I/O DBs
- F-runtime group information DB
- F-blocks from the project library or global libraries
- F-system blocks F-SBs
- Automatically generated F-blocks
- A preprocessing and/or postprocessing block, as needed (see [Pre-/postprocessing (S7-1200, S7-1500)](#pre-postprocessing-s7-1200-s7-1500))

##### Pre-/postprocessing of an F-runtime group

You have the option of calling blocks of the standard user program (FCs) directly before or after an F-runtime group, for example, for data transfer during fail-safe communication via Flexible F-Link. (see [Pre-/postprocessing (S7-1200, S7-1500)](#pre-postprocessing-s7-1200-s7-1500))

##### Structuring the safety program in two F-runtime groups

You can divide your safety program into two F-runtime groups. By having parts of the safety program (one F-runtime group) run in a faster priority class, you achieve faster safety circuits with shorter response times.

---

**See also**

[F-runtime group information DB (S7-1200, S7-1500)](#f-runtime-group-information-db-s7-1200-s7-1500)

#### Safety program in Software Unit (Safety Unit) (S7-1500)

##### Introduction

You can use Safety Units if you want to use the advantages of the Software Units for the safety program as well, e.g. independent compiling and loading.  
The blocks of the safety program are then located exclusively in the Safety Unit and can no longer be created in the "Program blocks" folder directly below the F-CPU.   
You must make the decision for the Safety Unit before creating the F-CPU. After creating the F-CPU, the decision for this F-CPU can no longer be changed.

##### Requirement

- F-CPU S7-1500 as of FW V2.6
- The check box "Manages safety program in 'Safety Units' environment" is selected under "Options/Settings/STEP 7 Safety".
- The F-CPU is newly created.

##### Safety program in the Safety Unit

After a new F-CPU has been created, the safety program is located in the Safety Unit.

![Safety program in the Safety Unit](images/147483328011_DV_resource.Stream@PNG-en-US.png)

For data exchange between the safety program and the standard user program, use a [transfer data block](#data-exchange-between-standard-user-program-and-safety-program) which you create as a global standard DB in the Safety Unit.

Information on Software Units is available in the help for STEP 7 under "Using Software Units".

##### Particularities

- You cannot store the Safety Unit in a library.
- System blocks in the Safety Unit cannot be published.

#### Fail-Safe Blocks

##### F-blocks of an F-runtime group

The following table shows the F-blocks that you use in an F-runtime group:

| F-block | Function | S7-300/400 F-CPUs | S7-1200/1500 F-CPUs |
| --- | --- | --- | --- |
| Main safety block | The first step in programming of the safety program is the main safety block.   The main safety block in S7-300/400 F-CPUs is an F-FC or F-FB (with instance DB), which is called by a standard block (recommendation: OB 35) from the standard user program.  The main safety block in S7-1200/1500 F-CPUs is an F-FC or F-FB (with instance DB), which is called by the F-OB. | X | X |
| F‑FB/F‑FC | Both in the main safety block as well as additional F-FBs and F-FCs, you can perform the following:  - Program the safety program with the instructions available for F-blocks in FBD or LAD - Call other created F-FBs/F-FCs for structuring the safety program - Insert F-blocks from the project library or global libraries | X | X |
| F-DB | Optional fail-safe data blocks that can be read- and write-accessed within the entire safety program. | X | X |
| F-I/O DB | An F-I/O DB is automatically generated for each F-I/O when it is configured. You can or you must access the tags of the F‑I/O DB in conjunction with F‑I/O accesses. | X | X |
| F-shared DB | The F‑shared DB is a fail-safe data block that contains all of the shared data of the safety program and additional information needed by the F‑system. | X | — |
| F-runtime group information DB | An F-runtime group information DB is created when you create an F-runtime group.  The F-runtime group information DB provides information on the F-runtime group and on the safety program as a whole. | — | X |

> **Note**
>
> You are not permitted to insert F-system blocks from the "System blocks" folder in a main safety block/F-FB/F-FC.

##### Instructions for the safety program

In the "Instructions" task card, you can find instructions for the F-CPU used and which you can to use program the safety program.

You can find instructions that you know from the standard user program, such as bit logic operations, mathematical functions, functions for program control, and word logic operations.

Moreover, there are instructions with safety functions, e.g., for two-hand monitoring, discrepancy analysis, muting, emergency STOP/emergency OFF, safety door monitoring, feedback monitoring and instructions for safety-related communication between F-CPUs.

##### More information

For a detailed description of the instructions for the safety program, refer to [Overview of instructions](STEP%207%20Safety%20V19%20instructions.md#overview-of-instructions).

##### Using instruction versions

As with the instructions for the standard user program, there may also be different versions of the instructions for the safety program.

More information on instruction versions can be found in the help on STEP 7 in "Basics for instruction versions".

More information on the differences of the individual versions of the instructions for the safety program can be found in the relevant chapter of the instructions.

> **Note**
>
> Note the following:
>
> - If you change the version of an instruction used in the safety program in the task card "Instructions" to a version which does not have identical functions, the functioning of your safety program may change after recompiling the safety program. In addition to the signature of the F-block that uses the instruction, the Collective F-Signature and the Collective F-SW-Signature of your safety program also change. You may have to perform an [acceptance test](#acceptance-of-changes).
> - (S7-300, S7-400) If you use a know-how protected F-block in your safety program which uses an instruction which is not the same version as that set in the task card "Instructions", when the program is compiled without entering the password for the know-how protected F-block, it is adjusted to the version set in the task card "Instructions". If the instruction versions do not have identical functions, the functioning of the know-how protected F-block may change and always its signature.

#### Restrictions in the programming languages FBD/LAD

##### LAD and FBD programming languages

The user program in the F-CPU typically consists of a standard user program and a safety program.

The standard user program is created using standard programming languages such as SCL, STL, LAD, or FBD.

For the safety program, LAD or FBD may be used with certain restrictions in the instructions and the applicable data types and operand areas. Also note the restrictions for the individual instructions.

##### Supported instructions

The instructions available depend on the F-CPU used. You can find the supported instructions in the description of the instructions (starting from [Overview of instructions](STEP%207%20Safety%20V19%20instructions.md#overview-of-instructions)).

> **Note**
>
> Enable input EN and enable output ENO cannot be connected.
>
> Exception:
>
> (S7-1200, S7-1500) With the following instructions you can program overflow detection by connecting the enable output ENO:
>
> - [ADD: Add (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#add-add-step-7-safety-v19)
> - [SUB: Subtract (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#sub-subtract-step-7-safety-v19)
> - [MUL: Multiply (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#mul-multiply-step-7-safety-v19)
> - [DIV: Divide (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#div-divide-step-7-safety-v19)
> - [NEG: Create two's complement (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#neg-create-twos-complement-step-7-safety-v19)
> - [ABS: Form absolute value (STEP 7 Safety V19) (S7-1200, S7-1500)](STEP%207%20Safety%20V19%20instructions.md#abs-form-absolute-value-step-7-safety-v19-s7-1200-s7-1500)
> - [CONVERT: Convert value (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#convert-convert-value-step-7-safety-v19)

##### Supported data types and parameter types

**Only** the following data types are supported:

- BOOL
- INT
- WORD
- DINT
- DWORD (S7-300, S7-400)
- TIME
- ARRAY, ARRAY[*] when using the instructions [RD_ARRAY_I: Read value from INT F-array (STEP 7 Safety V19) (S7-1500)](STEP%207%20Safety%20V19%20instructions.md#rd_array_i-read-value-from-int-f-array-step-7-safety-v19-s7-1500) and [RD_ARRAY_DI: Read value from DINT F-array (STEP 7 Safety V19) (S7-1500)](STEP%207%20Safety%20V19%20instructions.md#rd_array_di-read-value-from-dint-f-array-step-7-safety-v19-s7-1500).

  Restrictions:

  - ARRAY only in F-global DBs
  - ARRAY limits: 0 up to max. 10000
  - ARRAY[*] only as in-out parameter (InOut) in F-FCs and F-FBs
  - ARRAY of UDT is not permitted
  - ARRAY of Bool is not permitted
  - ARRAY of Word is not permitted
  - ARRAY of Time is not permitted
- [F-compliant PLC data type (UDT) (S7-1200, S7-1500)](#f-compliant-plc-data-types-udt-s7-1200-s7-1500)
- [Named value data types (S7-1500)](#named-value-data-types-s7-1500)

> **Note**
>
> If the result of an instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.  
> You must therefore ensure that the permitted range for the data type is observed when creating the program, or select a matching data type or use the ENO output.
>
> Note the description of the individual instructions.

##### Non-permitted data and parameter types

The following types are **not** permitted:

- All types not listed in the section "Supported data types and parameters types" (e.g. BYTE, REAL)
- Complex data types (e.g. STRING, ARRAY (S7-300, S7-400, S7-1200), STRUCT, PLC data type (UDT) (S7-300, S7-400), Named value data types (S7-300, S7-400, S7-1200))
- Parameter types (e.g. BLOCK_FB, BLOCK_DB, ANY)

##### Supported operand areas

The system memory of an F-CPU is divided into the same operand areas as the system memory of a standard CPU. You can access the operand areas listed in the table below from within the safety program.

Supported operand areas

| Operand area | Description |
| --- | --- |
| **Process image of the inputs** |  |
| - Of F-I/O | Only read-only access to input channels of F-I/O is possible.   Transfer to IN_OUT parameters of an F-FB or F-FC is therefore not valid either.  The process image of the inputs of F-I/O is updated prior to the start of the main safety block. |
| - Of standard I/O | Input channels of standard I/O can only be accessed read-only.   Transfer to IN_OUT parameters of an F-FB or F-FC is therefore not valid either.  In addition, a process-specific validity check is required.  See the STEP 7 help for the update times of the process image of the inputs of standard I/O. |
| **Process image of the outputs** |  |
| - Of F-I/O | Only write-only access to output channels of F-I/O is possible.   Transfer to IN_OUT parameters of an F-FB or F-FC is therefore not valid either.  In the safety program, the values for the outputs of the F-I/O are calculated and stored in the process image of the outputs.   The process image of the outputs for F-I/O is updated after the end of the main safety block. |
| - Of standard I/O | Output channels of standard I/O are write-only channels.   Transfer to IN_OUT parameters of an F-FB or F-FC is therefore not valid either.  In the safety program, the values for the outputs of the standard I/O are also calculated and stored in the process image of the outputs, if needed.  See the STEP 7 help for the update times of the process image of the outputs of standard I/O. |
| **Bit memory** | This area is used for data exchange with the standard user program.  In addition, read access requires a process-specific validity check.  A particular element of the bit memory can be either read- or write-accessed in the safety program.   Transfer to IN_OUT parameters of an F-FB or F-FC is therefore not valid either.  Note that it is only permitted to use bit memory for connecting the standard user program and the safety program; it must not be used as a buffer for F-data. |
| **Data blocks** |  |
| - F-DB | Data blocks store information for the program. They can either be defined as global data blocks such that all F-FBs, F-FCs, or main safety blocks can access them or assigned to a particular F-FB or main safety block (instance DB). A tag of a shared DB can only be accessed from one F-runtime group, and an instance DB only from the F-runtime group in which the corresponding F-FB/instruction is called. |
| - DB | This area is used for data exchange with the standard user program.  In addition, read access requires a process-specific validity check.  For a tag of a DB, either read access or write access is possible in the safety program.   Transfer to IN_OUT parameters of an F-FB or F-FC is therefore not valid either.  Note that the tags of a DB can only be used for transferring data between the standard user program and the safety program; DBs must not be used as a buffer for F-data. |
| **Temporary local data** | This memory area holds the temporary tags of a block (or F‑block) while the (F-) block is being executed. The local data stack also provides memory for transferring block parameters and for saving intermediate results. |

##### Data type conversion

As with the standard user program, there are two possibilities for data type conversion in the safety program:

- Implicit conversion

  The implicit conversion is executed as in the standard user program with the following restrictions: The bit length of the source data type has to match the bit length of the destination data type.
- Explicit conversion

  You use an explicit [conversion instruction](STEP%207%20Safety%20V19%20instructions.md#convert-convert-value-step-7-safety-v19) before the actual instruction is executed.

##### Slice access

Slice access is not possible in the safety program.

##### Non-permitted operand areas

Access via units other than those listed in the table above is **not** permitted. The same applies to access to operand areas not listed, in particular:

- Data blocks that were automatically added

  Exception: Certain tags in the [F-I/O DB](#f-io-db) and in the [F-shared DB (S7-300, S7-400)](#f-shared-db-s7-300-s7-400) or [F-runtime group information DB (S7-1200, S7-1500)](#f-runtime-group-information-db-s7-1200-s7-1500)
- I/O area: Inputs
- I/O area: Outputs

##### Boolean constants "0" or "FALSE" and "1" or "TRUE" (S7-300, S7-400)

The Boolean constants "0" or "FALSE" and "1" or "TRUE" are available for S7-300/400 F-CPUs as "Tags" "RLO0" and "RLO1" in the F-global DB. You access them through a fully qualified DB access ("F_GLOBDB".RLO0 or "F_GLOBDB".RLO1).

##### Boolean constants "0" or "FALSE" and "1" or "TRUE" (S7-1200, S7-1500)

The Boolean constants "0" or "FALSE" and "1" or "TRUE" are available for S7-1200/1500 F-CPUs to assign parameters during block calls. You can enter this directly in FBD or LAD at the respective block inputs.

Example FBD:

![Boolean constants "0" or "FALSE" and "1" or "TRUE" (S7-1200, S7-1500)](images/118282624395_DV_resource.Stream@PNG-de-DE.png)

Example LAD:

![Boolean constants "0" or "FALSE" and "1" or "TRUE" (S7-1200, S7-1500)](images/139051471115_DV_resource.Stream@PNG-de-DE.png)

As an alternative, as before you have the option to also set "1" or "TRUE" in a tag using the "[Assignment](STEP%207%20Safety%20V19%20instructions.md#assignment-step-7-safety-v19)" instruction.

To do so, do not interconnect the box input of the "Assignment" instruction in FBD. In LAD, you interconnect the input directly with the supply rail.

You obtain a tag with "0" or "FALSE" by subsequent inversion with the instruction "[Invert RLO](STEP%207%20Safety%20V19%20instructions.md#invert-rlo-step-7-safety-v19)".

Example FBD:

![Boolean constants "0" or "FALSE" and "1" or "TRUE" (S7-1200, S7-1500)](images/88406762251_DV_resource.Stream@PNG-de-DE.png)

Example LAD:

![Boolean constants "0" or "FALSE" and "1" or "TRUE" (S7-1200, S7-1500)](images/88406771083_DV_resource.Stream@PNG-de-DE.png)

##### Operand area of temporary local data: Particularities

> **Note**
>
> Note when using the operand area of temporary local data that the first access of a local data element in a main safety block/F‑FB/F‑FC must always be a write access. This initializes the local data element.
>
> Make sure that a temporary local data element is initialized prior to the first JMP, JMPN, or RET instruction.
>
> The "local data bit" should be initialized with the Assign ("=") (FBD) or ("‑‑( )") (LAD) instruction. Assign the local data bit a signal state of "0" or "1" as a Boolean constant.
>
> Local data bits cannot be initialized with the Flip Flop (SR, RS), Set Output (S) or Reset Output (R) instructions.
>
> The F-CPU can go to STOP if this is not observed. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

##### "Fully qualified DB access"

Access to tags of a data block in an F‑FB/F‑FC is "fully qualified DB access". This also applies to initial access to tags of a data block after a jump label.

For S7-300/400 F-CPUs, only initial access needs to be "fully qualified DB access". Alternatively, you can use the instruction "OPN".

##### Example of "fully qualified DB access":

Assign a name for the F-DB, e.g. "F_Data_1". Use the names assigned in the declaration of the F-DB instead of the absolute addresses.

![Example with fully-qualified access](images/131536892683_DV_resource.Stream@PNG-de-DE.png)

Example with fully-qualified access

##### Example of "non-fully qualified DB access" (S7-300, S7-400):

![Example without fully-qualified access](images/93479981195_DV_resource.Stream@PNG-en-US.png)

Example without fully-qualified access

##### Access to instance DBs

You can also access instance DBs of F-FBs with fully qualified access, e.g., for transfer of block parameters. It is not possible to access static local data in single/multi-instances of other F-FBs.

(S7-300, S7-400) Note that accessing instance DBs of F‑FBs that are not called in the safety program can cause the F‑CPU to go to STOP mode.

Note the following warning for S7-1200/1500 F-CPUs:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When you program global access to instance DBs of F-FBs, you must ensure that the associated F-FB is called in the safety program. (S096) |  |

#### F-compliant PLC data types (UDT) (S7-1200, S7-1500)

This section contains information on the following topics:

- [F-compliant PLC data types (UDT) (S7-1200, S7-1500)](#f-compliant-plc-data-types-udt-s7-1200-s7-1500-1)
- [Grouping PLC tags for inputs and outputs of F-I/O in structures (S7-1200, S7-1500)](#grouping-plc-tags-for-inputs-and-outputs-of-f-io-in-structures-s7-1200-s7-1500)
- [Example of structured PLC tags for inputs and outputs of F-I/O (S7-1200, S7-1500)](#example-of-structured-plc-tags-for-inputs-and-outputs-of-f-io-s7-1200-s7-1500)

##### F-compliant PLC data types (UDT) (S7-1200, S7-1500)

###### Introduction

You declare and use F-compliant PLC data types (UDT) ![Introduction](images/61221635723_DV_resource.Stream@PNG-de-DE.png) as you would standard PLC data types (UDT). You can use F-compliant PLC data types (UDT) in the safety program as well as in the standard user program.

Differences to standard PLC data types (UDT) are described in this chapter.

Information on the use and declaration of standard PLC data types (UDT) is available in the STEP 7 help under "Declaring PLC data types".

###### Declaring F-compliant PLC data types (UDT)

You declare F-compliant PLC data types (UDT) as you would PLC data types (UDT).

In F-compliant PLC data types (UDT), you can use all [data types](#restrictions-in-the-programming-languages-fbdlad) that you can also use in safety programs. Exception: ARRAY.

Proceed as follows for declaration:

1. Click on "Add new PLC data type" in the "PLC Data Types" folder in the project tree.
2. To create an F-compliant PLC data type (UDT), enable the option "Create F-compliant PLC data type" in the "Add new PLC data type" dialog.
3. Proceed as described in the STEP 7 help under "Programming structure of PLC data types".

You specify default values for F-compliant PLC data types (UDT) during the declaration.

###### Using F-compliant PLC data types (UDT)

You use F-compliant PLC data types as you would standard PLC data types (UDT).

###### Nesting depth for F-compliant PLC data types

For F-compliant PLC data types, the maximum nesting depth is limited compared to the standard PLC data types (maximum nesting depth = 8). There is a dependency on the call sequence of the block in which a tag of the nested F-compliant PLC data type is declared. Each call level of F-FCs or multi-instance F-FBs reduces the maximum nesting depth of the F-compliant PLC data type used. For multi-instance F-FBs, the caller counts as an additional level.

When a tag of a nested F-compliant PLC data type is declared in a global F-DB, its maximum nesting depth is 7.

**Example 1**

The main safety block (level 1) calls an F-FB as multi-instance (level 2) which, in turn, calls an F-FC (level 3) in which a tag of the type of a nested F-compliant PLC data type is declared. This means a maximum nesting depth of 5 is available for the fail-safe compliant PLC data type used by the tag.

**Example 2**

The main safety block calls an F-FB as a single instance (level 1) which, in turn, calls an F-FC (level 2) in which a tag of the type of a nested F-compliant PLC data type is declared. This means a maximum nesting depth of 6 is available for the fail-safe compliant PLC data type used by the tag.

###### Changes to F-compliant PLC data types (UDT)

You need the password for the safety program to change F-compliant PLC data types (UDT). Regardless if you are using the F-compliant PLC data type (UDT) in an F-block, in a standard block or not at all.

---

**See also**

["F-compliant PLC data types" area (S7-1200, S7-1500)](#f-compliant-plc-data-types-area-s7-1200-s7-1500)

##### Grouping PLC tags for inputs and outputs of F-I/O in structures (S7-1200, S7-1500)

You group PLC tags for inputs and outputs of F-I/O in structures (structured PLC tag) as you would for inputs and outputs of standard I/O.

Use F-compliant PLC data types (UDT).

###### Rules

When creating structured PLC tags for inputs and outputs of F-I/O, you must also observe the following rules in addition to the rules in the standard:

- You must not group inputs/outputs of standard I/O and F-I/O at the same time in a structured PLC tag.
- You may only group inputs/outputs of actually existing channels (channel value and value status) in a structured PLC tag.

  See also [Addressing F-I/O](#addressing-f-io)
- You may only group inputs/outputs of channels (channel value and value status) that are enabled in the hardware configuration in a structured PLC tag.

  See also [Addressing F-I/O](#addressing-f-io)
- You may only group inputs of channels (channel value and value status) that provide the result of the "1oo2 sensor evaluation" with set "1oo2 sensor evaluation".

  See also [Addressing F-I/O](#addressing-f-io)
- You should combine all inputs and outputs of an F-I/O in a structured PLC tag. When divided into several structured PLC tags, these can only begin with multiples of 16 bits. This also applies to nested F-compliant PLC data types (UDT). See rules in the standard.

  The F-CPU can go to STOP mode if this is disregarded. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
- A structured PLC tag that groups outputs of an F-I/O must not overlap with other PLC tags.

  The F-CPU can go to STOP mode if this is disregarded. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

> **Note**
>
> To observe these rules, you must declare the F-compliant PLC data type that is used for the structured PLC tag accordingly.

You can find the addresses allocated to a structured PLC tag in the "IO tags" tab of an F-I/O configuration.

##### Example of structured PLC tags for inputs and outputs of F-I/O (S7-1200, S7-1500)

###### Introduction

This example uses the F-module 4 F-DI/3 F-DO DC24V/2A with 1oo2 evaluation to demonstrate how you use structured PLC tags for access to F-I/O.

###### Channel structure of the 4 F-DI/3 F-DO DC24V/2A F-module

The table below sets out the channel structure and address assignment of the F-module 4 F-DI/3 F-DO DC24V/2A with 1oo2 evaluation. You may only access existing and enabled channels (addresses I15.0 to I15.3 and I16.0 to I16.3). These channels provide the result of 1oo2 evaluation generated internally in the F-module.

Channel structure and addresses of the channel values of inputs with 1oo2 evaluation

| Channel | Address |
| --- | --- |
| DI channel 0 channel value | I15.0 |
| DI channel 1 channel value | I15.1 |
| DI channel 2 channel value | I15.2 |
| DI channel 3 channel value | I15.3 |
| — | I15.4 |
| — | I15.5 |
| — | I15.6 |
| — | I15.7 |

Channel structure and addresses of the value status of the inputs with 1oo2 evaluation

| Channel | Address |
| --- | --- |
| DI channel 0 value status | I16.0 |
| DI channel 1 value status | I16.1 |
| DI channel 2 value status | I16.2 |
| DI channel 3 value status | I16.3 |
| — | I16.4 |
| — | I16.5 |
| — | I16.6 |
| — | I16.7 |

Channel structure and addresses of the value status of outputs

| Channel | Address |
| --- | --- |
| DO channel 0 value status | I17.0 |
| DO channel 1 value status | I17.1 |
| DO channel 2 value status | I17.2 |
| DO channel 3 value status | I17.3 |

Channel structure and addresses of the channel values of outputs

| Channel | Address |
| --- | --- |
| DO channel 0 channel value | Q15.0 |
| DO channel 1 channel value | Q15.1 |
| DO channel 2 channel value | Q15.2 |
| DO channel 3 channel value | Q15.3 |

###### Creating F-compliant PLC data types (UDT)

Create two F-compliant PLC data types (UDT), for example, for access to all channels.

The figure below shows an F-compliant PLC data type (UDT) for access to the channel values and value status of the inputs with 1oo2 evaluation:

![Creating F-compliant PLC data types (UDT)](images/95159539723_DV_resource.Stream@PNG-en-US.png)

The figure below shows the F-compliant PLC data type (UDT) for access to the channel values and value status of the outputs:

![Creating F-compliant PLC data types (UDT)](images/95159543435_DV_resource.Stream@PNG-en-US.png)

###### Using F-compliant PLC data types (UDT)

As demonstrated in the figure below, you can use the two F-compliant PLC data types (UDT) that you have created in an F-FC (e.g. "Motor"):

![Using F-compliant PLC data types (UDT)](images/95159892747_DV_resource.Stream@PNG-en-US.png)

###### Creating structured PLC tag for the F-module 4 F-DI/3 F-DO DC24V/2A

Create structured PLC tags for the F-module 4 F-DI/3 F-DO DC24V/2A:

![Creating structured PLC tag for the F-module 4 F-DI/3 F-DO DC24V/2A](images/95159896459_DV_resource.Stream@PNG-en-US.png)

###### Accessing the F-FC

Transfer the structured PLC tags you have created when you call the F-FC (e.g. "Motor"):

![Accessing the F-FC](images/95159492491_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Addressing F-I/O](#addressing-f-io)
  
[Value status (S7-1200, S7-1500)](#value-status-s7-1200-s7-1500)

#### Named value data types (S7-1500)

You use named value data types as in the standard.

In the case of named value data types in a safety program, you can only use the [data types supported by the safety program](#restrictions-in-the-programming-languages-fbdlad) as base data types.

> **Note**
>
> If you change Named value data types, this also changes the collective F signature.

> **Note**
>
> **Know-how protection**
>
> You cannot use Named value data types in know-how protected F-blocks.

Print out the named value data types that are used in your safety program. Mark the "PLC data types" folder in the project tree and call up the print function.  Supplement your safety documentation with this printout.

You can find more information on named value data types in the online help on STEP 7 under "Named value data types" and "Declaring named value data types".

#### Editing PLC tags with external editors

To edit PLC tags with external editors follow the procedure as in the standard. Additional information can be found in the STEP 7 help in "Editing PLC tags with external editors".

Note the following:

> **Note**
>
> After importing a tag table which contains tags used in the safety program, the collective F-signature of the safety program is reset.
>
> To form the collective F-signature again you have to recompile the project data. For this, with access protection set up for the safety program, you need a valid access authorization for the safety program.
>
> If you would like to edit PLC tags with external editors, we therefore recommend that you store PLC tags to be used in the safety program in a separate tag table.

#### Using Multiuser engineering

If you want to use Multiuser engineering, proceed as described in the STEP 7 help under "Using Multiuser engineering".

#### Deleting the safety program

##### Deleting individual F-blocks

To delete an F‑block, follow the same procedure as in STEP 7.

##### Deleting an F-runtime group

See [Deleting an F-runtime group](#deleting-an-f-runtime-group)

(S7-300, S7-400) Remove all calls that you have used to call the safety program (Main_Safety).

##### Deleting the entire safety program for S7-300/400 F‑CPUs with inserted memory card (SIMATIC Micro Memory Card or flash card)

To delete an entire safety program, proceed as follows:

1. Delete all F‑blocks (shown with yellow symbol) in the project tree.
2. Remove all calls that you have used to call the safety program (Main_Safety).
3. Select the F‑CPU in the hardware and network editor and clear the "F‑capability activated" option in the properties of the F‑CPU.
4. Compile the project data of the F-CPU

   The offline project no longer contains a safety program.
5. To delete a safety program on the Memory Card (SIMATIC Micro Memory Card or Flash Card), insert the Memory Card (SIMATIC Micro Memory Card or Flash Card) in the programming device or PC or in a SIMATIC USB prommer.
6. Select the menu command "Project > Card Reader/USB memory > Show Card Reader/USB memory" in the menu bar.
7. Open the "SIMATIC Card Reader" folder and delete the Memory Card.
8. Insert the Memory Card into the F-CPU.
9. Perform a memory reset of the F‑CPU (flashing of the STOP LED requests a memory reset).

You can then download the offline standard user program to the F‑CPU.

##### Deleting the entire safety program for S7-400 F‑CPUs without inserted flash card

To delete an entire safety program, proceed as follows:

1. Delete all F‑blocks (shown with yellow symbol) in the project tree.
2. Remove all calls that you have used to call the safety program (Main_Safety).
3. Select the F‑CPU in the hardware and network editor and clear the "F-capability activated" option in the properties of the F‑CPU.
4. Compile the project data of the F-CPU

   The offline project no longer contains a safety program.
5. Perform a memory reset on the F-CPU (in the "Online tools" task card of the F-CPU).

You can then download the offline standard user program to the F‑CPU.

##### Delete the entire safety program for SIMATIC S7-1200/1500 F‑CPUs

To delete an entire safety program, proceed as follows:

1. Delete all F‑blocks (shown with yellow symbol) in the project tree.
2. Select the F‑CPU in the hardware and network editor and clear the "F‑capability activated" option in the properties of the F‑CPU.
3. Compile the project data of the F-CPU

   The offline project no longer contains a safety program.

You can then download the offline standard user program to the F‑CPU.

### Defining F-Runtime Groups

This section contains information on the following topics:

- [Rules for F-Runtime Groups of the Safety Program](#rules-for-f-runtime-groups-of-the-safety-program)
- [Procedure for defining an F‑runtime group (S7-300, S7-400)](#procedure-for-defining-an-f-runtime-group-s7-300-s7-400)
- [Procedure for defining an F‑runtime group (S7-1200, S7-1500)](#procedure-for-defining-an-f-runtime-group-s7-1200-s7-1500)
- [F-runtime group communication (S7-300, S7-400)](#f-runtime-group-communication-s7-300-s7-400)
- [F-runtime group communication (S7-1200, S7-1500)](#f-runtime-group-communication-s7-1200-s7-1500)
- [Deleting an F-runtime group](#deleting-an-f-runtime-group)
- [Changing the F-runtime group (S7-300, S7-400)](#changing-the-f-runtime-group-s7-300-s7-400)
- [Changing the F-runtime group (S7-1200, S7-1500)](#changing-the-f-runtime-group-s7-1200-s7-1500)

#### Rules for F-Runtime Groups of the Safety Program

##### Rules

Note the following:

- The channels (channel values and value status) of an F-I/O can only be accessed from a single F-runtime group.
- Tags of the F‑I/O DB of an F‑I/O can only be accessed from one F‑runtime group and only from that F‑runtime group from which the channels or value status of this F‑I/O are also accessed (if access is made).
- F-FBs can be used in more than one F-runtime group but they must be called with different instance DBs.
- Instance DBs of F-FB can only be accessed from the F‑runtime group in which the associated F‑FB is called.
- A tag of a global F‑DB (except the F‑global DB) can only be accessed from one F‑runtime group (however, a global F‑DB can be used in more than one F‑runtime group).
- (S7-300, S7-400) A DB for F-runtime group communication can be read and write accessed by the F-runtime group to which it was assigned as "DB for runtime group communication", but only read-accessed by the "receiver" F-runtime group.
- (S7-300, S7-400) An F-communication DB can only be accessed from one F-runtime group.
- (S7-1200, S7-1500) You must not call the main safety block yourself. It is automatically called by the assigned F-OB.

  > **Note**
  >
  > F-OBs are protected by F-system know-how. The OB start information of F-OBs therefore cannot be evaluated.
- (S7-1200, S7-1500). The F-OB should be created with the highest priority of all OBs.

  > **Note**
  >
  > The cycle time/runtime of an F-OB can be prolonged by, among other things, communication load, the processing of higher-priority interrupts, as well as by test and commissioning functions. In a redundant S7-1500HF system, it is also dependent on the current system state.
- (S7-300, S7-400) The main safety block may only be called once from a standard block. Multiple calls can cause the F-CPU to go to STOP mode.
- (S7-300, S7-400) For optimal use of temporary local data, you must call the F-runtime group (the main safety block) directly in an OB (cyclic interrupt OB, if possible); you should not declare any additional temporary local data in this cyclic interrupt OB.
- (S7-300, S7-400) Within a cyclic interrupt OB, the F-runtime group should be executed **before** the standard user program; i.e. it should be called at the very beginning of the OB, so that the F-runtime group is always called at fixed time intervals, regardless of how long it takes to process the standard user program.

  For this reason, the cyclic interrupt OB should also not be interrupted by higher priority interrupts.
- The process image of the inputs and outputs of standard I/O, bit memory, and tags of DBs in the standard user program may be accessed either as read-only or read/write from more than one F‑runtime group. (see also [Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program))
- F-FCs can generally be called in more than one F-runtime group.

> **Note**
>
> You can improve performance by writing sections of the program that are not required for the safety function in the standard user program.
>
> When determining which elements to include in the standard user program and which to include in the safety program, you should keep in mind that the standard user program can be modified and downloaded to the F-CPU more easily. In general, changes in the standard user program do not require an acceptance.

#### Procedure for defining an F-runtime group (S7-300, S7-400)

##### Requirements

- You have inserted an S7-300/400 F-CPU in your project.
- In the "Properties" tab of the F-CPU, the "F-capability activated" check box is selected (default setting).

##### F-runtime group created by default

STEP 7 Safety inserts F-blocks for an F-runtime group in the project tree by default after an F-CPU has been added. When you open the "Program blocks" folder, you see the (F-)blocks of the F-runtime group (CYC_INT5 [OB 35], Main_Safety [FB 1], and Main_Safety_DB [DB1]) in the project tree.

![F-runtime group created by default](images/28209732491_DV_resource.Stream@PNG-en-US.png)

The following section describes how you modify the settings / parameters of the F-runtime group created by default or add and additional F-runtime group.

##### Procedure for defining an F-runtime group

Proceed as follows to define an F-runtime group:

1. Open the Safety Administration Editor by double-clicking in the project tree.
2. Select "F‑runtime group" in the area navigation.

   **Result:** The work area for defining an F-runtime group with the (default) settings for F-runtime group 1 opens.

   ![Procedure for defining an F-runtime group](images/115640159627_DV_resource.Stream@PNG-en-US.png)
3. Specify the block in which the main safety block is to be called.

   Cyclic interrupt OB 35 is suggested here by default. The advantage of cyclic interrupt OBs is that they interrupt the cyclic program processing in OB 1 of the standard user program at fixed intervals. This means that the safety program is called and run at fixed time intervals in a cyclic interrupt OB.

   In this input field, you can select only those blocks that were created in the LAD, FBD, or STL programming language. If you select a block here, the call is inserted automatically into the selected block and, if necessary, removed from a previously selected block.

   If you want to call the main safety block in a block that was created in another programming language, you must program this call itself. The input field is then not editable (grayed out), and you can change the call only in the calling block and not the Safety Administration Editor.
4. Assign the desired main safety block to the F-runtime group. If the main safety block is an FB, you must also assign an instance DB.

   Main_Safety [FB1] and Main_Safety_DB [DB1] are suggested by default.
5. The F-CPU monitors the F-cycle time of the F-runtime group. For "Maximum cycle time of F-runtime group", enter the maximum permitted time between two calls of the F-runtime group.

   | Symbol | Meaning |
   | --- | --- |
   |  | **Warning** |
   | The call interval of the F-runtime group is monitored for a maximum value. This means that monitoring is performed to determine whether the call is executed often enough, but not whether it is executed too often or, for example, isochronously. Fail-safe timers must therefore be implemented using the [TP, TON, or TOF instructions](STEP%207%20Safety%20V19%20instructions.md#timer-operations) from the "Instructions" task card and not using counters (OB calls). (S007) |  |

   | Symbol | Meaning |
   | --- | --- |
   |  | **Warning** |
   | The response time of your safety function depends, among other things, on the cycle time of the F-OB, the runtime of the F-runtime group and, when distributed F-I/O is used, the parameter assignment of PROFINET/PROFIBUS.  Therefore, the configuration/parameter assignment of the standard system influences the response time of your safety function.  Examples: - Increasing the priority of a standard OB compared to an F-OB can extend the cycle time of the F-OB or the runtime of the F-runtime group due to the higher-priority processing of the standard OB. Note that during the creation of technology objects, OBs with very high priority may be created automatically. - The change of the send clock cycle of PROFINET changes the cycle time of an F-OB with event class "Synchronous cycle". Note that the configuration / parameter assignment of the standard system is not subject to access protection for the safety-related project data and does not lead to a modification of the Collective F-Signature.  If you do not take organizational measures to prevent changes in the configuration / parameter assignment of the standard system with influence on the response time, you must always use the monitoring times for the calculation of the maximum response time of a safety function (see [Configuring monitoring times](#configuring-monitoring-times)).  The monitoring times are protected against change with the access protection of the safety-related project data and are captured by the Collective F-Signature as well as the Collective F-SW-Signature.  When calculating with the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) you need to consider the value that is specified for "Any standard system runtimes" as value for the maximum response time. (S085) |  |
6. If one F-runtime group is to provide tags for evaluation to another F-runtime group of the safety program, assign a DB for F-runtime group communication. Select an F-DB for "DB for F‑runtime group communication". (See also [F-runtime group communication (S7-300, S7-400)](#f-runtime-group-communication-s7-300-s7-400))
7. If you want to create a **second F-runtime group**, click the "Add new F-runtime group" button.
8. Assign an F-FB or F-FC as the main safety block to a calling block. This F‑FB or F‑FC is automatically generated in the project tree, if not already present.
9. If the main safety block is an F-FB, assign an instance DB to the main safety block. The instance DB is generated automatically in the project tree.
10. Follow steps 3 to 5 above to complete generation of the second F-runtime group.

#### Procedure for defining an F-runtime group (S7-1200, S7-1500)

##### Requirements

- You have inserted an S7-1200/1500 F-CPU in your project.
- In the "Properties" tab of the F-CPU, the "F-capability activated" check box is selected (default setting).

##### F-runtime group created by default

STEP 7 Safety inserts F-blocks for an F-runtime group in the project tree by default after an F-CPU has been added. When you open the "Program blocks", you see the (F-)blocks of the F-runtime group (FOB_RTG1 [OB123], Main_Safety_RTG1 [FB1] and Main_Safety_RTG1_DB [DB1]) in the project tree.

![F-runtime group created by default](images/113845385099_DV_resource.Stream@PNG-en-US.png)

The following section describes how you modify the settings / parameters of the F-runtime group created by default or add and additional F-runtime group.

##### Procedure for defining an F-runtime group

Proceed as follows to define an F-runtime group:

1. Open the Safety Administration Editor by double-clicking in the project tree.
2. Select "F‑runtime group" in the area navigation.

   **Result:** The work area for defining an F-runtime group with the (default) settings for F-runtime group 1 opens.

   ![Procedure for defining an F-runtime group](images/113845376011_DV_resource.Stream@PNG-en-US.png)
3. Assign a name for the F-OB under "F-OB".
4. Specify the event class of the F-OB when you create a new F-runtime group.

   For an F-OB you can select between the event classes "Program cycle", "Cyclic interrupt" or "Synchronous cycle".

   In the case of the F-runtime group created by default, the F-OB has the event class "Cyclic interrupt". To change the event class of the F-OB of an already created F-runtime group, you need to delete and F-runtime group and create a new one.

   > **Note**
   >
   > We recommend creating the F-OB with the event class "Cyclic interrupt". The safety program will then be called and executed at fixed time intervals.
   >
   > F-OBs with the event class "Synchronous cycle" are only recommended in conjunction with F-IOs that support isochronous mode, for example submodule "Profisafe Telgr 902" of drive SINAMICS S120 CU310-2 PN V5.1.
   >
   > F-OBs with the event class "Program cycle" are not recommended, as these have the lowest priority "1" (see below).

   > **Note**
   >
   > Note the maximum permissible number of OBs (incl. F-OBs) with event class "Synchronous cycle" (see technical specifications in the product manuals of the S7-1500 CPUs).
5. If required, you can manually change the number of the F-OB proposed by the system. To do so, note the number ranges valid for the relevant event class.
6. Assign cycle time, phase shift and priority parameters for F-OBs with event class "Cyclic interrupt".

   Assign the priority parameter for F-OBs with event class "Synchronous cycle".

   - Select a cycle time which is less than the "Maximum cycle time of F-runtime group" and less than the "Cycle time warning limit of F-runtime group".
   - Select a phase shift which is less than the cycle time.
   - If possible, select a priority that is higher than the priority of all other OBs.
   > **Note**
   >
   > Through a high priority of the F-OB you ensure that the run time of the safety program and the [reaction time of your safety functions](#configuring-monitoring-times) are influenced as little as possibly by the standard user program.

   > **Note**
   >
   > For F-OBs with event class "Synchronous cycle" you need to also assign parameters for application cycle (ms) and possibly delay time (ms) after defining the F-runtime group and the connection of the isochronous F-I/O to the isochronous mode interrupt OB. You can find these parameters in the "Properties" dialog box of the isochronous mode interrupt OB in the "Isochronous mode" group. Proceed as described in the STEP 7 help under "Configuring isochronous mode interrupt OBs".
7. Assign the calling main safety block to the F-OB. If the main safety block is an FB, you must also assign an instance DB.

   Main_Safety_RTG1 [FB1] and Main_Safety_RTG1_DB [DB1] are suggested by default.
8. The F-CPU monitors the F-cycle time of the F-runtime group. Two parameters are available:

   - If the "Warn cycle time of the F-runtime group" is exceeded, a maintenance demanded is written to the diagnostics buffer of the F-CPU and the MAINT LED of the F-CPU is activated. This parameter can, for example, be used to determine whether the cycle time exceeds a required value without the F-CPU switching to STOP mode.

     > **Note**
     >
     > The maintenance demanded is marked as an outgoing event by a STOP/RUN transition of the F-CPU. In an HF-system you must set both HF-CPUs or the redundant S7-1500HF system to STOP before you restart the HF-CPUs.
     >
     > As an alternative, you can mark the maintenance demanded as outgoing with the standard instruction "ACK_FCT_WARN". To do so, call the instruction "ACK_FCT_WARN" with a rising edge at the input parameter "ACK_WARN" in your standard user program.
     >
     > A renewed violation of the warning limit is not signaled until after a STOP/RUN transition of the F-CPU.
   - If the "Maximum cycle time of F-runtime group" is exceeded, the F-CPU will go to STOP. For "Maximum cycle time of F-runtime group", select the maximum permitted time between two calls of this F-runtime group (maximum of 20000000 µs).

     | Symbol | Meaning |
     | --- | --- |
     |  | **Warning** |
     | The call interval of the F-runtime group is monitored for a maximum value. This means that monitoring is performed to determine whether the call is executed often enough, but not whether it is executed too often or, for example, isochronously. Fail-safe timers must therefore be implemented using the [TP, TON, or TOF instructions](STEP%207%20Safety%20V19%20instructions.md#timer-operations) from the "Instructions" task card and not using counters (OB calls). (S007) |  |

     | Symbol | Meaning |
     | --- | --- |
     |  | **Warning** |
     | The response time of your safety function depends, among other things, on the cycle time of the F-OB, the runtime of the F-runtime group and, when distributed F-I/O is used, the parameter assignment of PROFINET/PROFIBUS.  Therefore, the configuration/parameter assignment of the standard system influences the response time of your safety function.  Examples: - Increasing the priority of a standard OB compared to an F-OB can extend the cycle time of the F-OB or the runtime of the F-runtime group due to the higher-priority processing of the standard OB. Note that during the creation of technology objects, OBs with very high priority may be created automatically. - The change of the send clock cycle of PROFINET changes the cycle time of an F-OB with event class "Synchronous cycle". Note that the configuration / parameter assignment of the standard system is not subject to access protection for the safety-related project data and does not lead to a modification of the Collective F-Signature.  If you do not take organizational measures to prevent changes in the configuration / parameter assignment of the standard system with influence on the response time, you must always use the monitoring times for the calculation of the maximum response time of a safety function (see [Configuring monitoring times](#configuring-monitoring-times)).  The monitoring times are protected against change with the access protection of the safety-related project data and are captured by the Collective F-Signature as well as the Collective F-SW-Signature.  When calculating with the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) you need to consider the value that is specified for "Any standard system runtimes" as value for the maximum response time. (S085) |  |

   The "Cycle time warning limit of F-runtime group" must be configured as less than or equal to the "Maximum cycle time of F-runtime group".
9. If necessary, you can change the name suggested by the system for the [F-runtime group information DB](#f-runtime-group-information-db-s7-1200-s7-1500) under "F-runtime group information DB".
10. If required, you can select blocks of the standard program (FCs) with regard to preprocessing or postprocessing of an F-runtime group (see [Pre-/postprocessing (S7-1200, S7-1500)](#pre-postprocessing-s7-1200-s7-1500))
11. If you want to create a **second F-runtime group**, click the "Add new F-runtime group" button. Follow steps 3 to 10 above.

#### F-runtime group communication (S7-300, S7-400)

##### Safety-related communication between F-runtime groups

Safety-related communication can take place between the two F-runtime groups of a safety program. This means fail-safe tags can be provided by one F-runtime group in an F-DB and read in another F-runtime group.

> **Note**
>
> A DB for F-runtime group communication can be read and write accessed by the F-runtime group to which it was assigned as "DB for runtime group communication", while it can only be read-accessed by the "receiver" F-runtime group.

**Tip:** You can improve performance by structuring your safety program in such a way that as few tags as possible are exchanged between the F‑runtime groups.

##### Procedure for defining a DB for F-runtime group communication

You define the DB for F-runtime group communication in the work area "F-runtime groups". Proceed as follows:

1. Click "F‑runtime groups" in "Safety Administration Editor".
2. Select an existing F‑DB in the "DB for F‑runtime group communication" field or assign a new one.
3. Assign a name to the F‑DB.

##### Up-to-dateness of tags read from another F-runtime group

> **Note**
>
> Tags read are up-to-date as at the time of the last completed processing cycle of the F-runtime group providing the tags prior to start-up of the F-runtime group reading the tags.

If the tags supplied undergo multiple changes during runtime of the F‑runtime group supplying the tags, the F-runtime group reading the tags only receives the last change (see figure below).

**Assignment of fail-safe values**

After F‑system start-up, fail-safe values are supplied to the F‑runtime group which has read access to tags in the DB for F‑runtime group communication of another F‑runtime group (for example, F‑runtime group 2). These are the values you specified as initial values in the DB for F-runtime group communication of F-runtime group 1.

F-runtime group 2 reads the fail-safe values the first time it is called. The second time the F-runtime group 2 is called, it reads the latest tags if F-runtime group 1 has been processed completely between the two calls of F-runtime group 2. If F‑runtime group 1 has not been processed completely, F‑runtime group 2 continues to read the fail-safe values until F‑runtime group 1 is completely processed.

The behavior is illustrated in the two figures below.

**Reading tags from F‑runtime group 1, which has a longer OB cycle and lower priority than F‑runtime group 2**

![Up-to-dateness of tags read from another F-runtime group](images/17836867339_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Startup of F-system |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837314315_DV_resource.Stream@PNG-de-DE.png) | Cycle time of the (F-)OB in which the F-runtime group is called. |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837441291_DV_resource.Stream@PNG-de-DE.png) | Runtime of the F-runtime group |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837453067_DV_resource.Stream@PNG-de-DE.png) | ... Tag of F-runtime group 1, written to DB for F-runtime group communication of F-runtime group 1 |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837503243_DV_resource.Stream@PNG-de-DE.png) | ...Tag of F-runtime group 2, read in DB for F-runtime group communication of F-runtime group 1 |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837720075_DV_resource.Stream@PNG-de-DE.png) | Initial value in the DB for F-runtime group communication |

**Reading tags from F-runtime group 1, which has a shorter OB cycle and higher priority than F-runtime group 2**

![Up-to-dateness of tags read from another F-runtime group](images/18414054539_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Startup of F-system |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837314315_DV_resource.Stream@PNG-de-DE.png) | Cycle time of the (F-)OB in which the F-runtime group is called. |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837441291_DV_resource.Stream@PNG-de-DE.png) | Runtime of the F-runtime group |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837453067_DV_resource.Stream@PNG-de-DE.png) | ... Tag of F-runtime group 1, written to DB for F-runtime group communication of F-runtime group 1 |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837503243_DV_resource.Stream@PNG-de-DE.png) | ... Tag of F-runtime group 2, read in DB for F-runtime group communication of F-runtime group 1 |
| ![Up-to-dateness of tags read from another F-runtime group](images/17837720075_DV_resource.Stream@PNG-de-DE.png) | Initial value in the DB for F-runtime group communication |

##### F-runtime group supplying tags is not processed

> **Note**
>
> If the F-runtime group whose DB for F-runtime group communication is to supply the tags is not processed (the main safety block of the F-runtime group is not called), the F-CPU goes to STOP mode. One of the following diagnostics events is then entered in the diagnostics buffer of the F-CPU:
>
> - Error in safety program: cycle time exceeded
> - Number of the relevant main safety block (of F-runtime group that is not processed)
> - Current cycle time in ms: "0"

#### F-runtime group communication (S7-1200, S7-1500)

##### Introduction

With the help of Flexible F-Link you realize a F-runtime group communication.

With Flexible F-Link a coded F-array is made available for the send data of the F-runtime group. The coded F-array is transferred to the other F-runtime group with standard instructions such as UNMOVE_BLK.

##### Requirement

- S7-1500 F-CPUs as of firmware V2.0
- S7-1200 F-CPUs as of firmware V4.2
- Safety system version as of V2.2

##### F-runtime group communication

![F-runtime group communication](images/170242287115_DV_resource.Stream@PNG-en-US.png)

If you want to send a data fail-safe from one F-runtime group to another F-runtime group, follow these steps:

1. Create a non-nested F-compliant PLC data type (UDT) for the F-runtime group communication. The size can be up to 100 bytes.
2. Create two F-communications for an F-runtime group communication in the Safety Administration Editor in the "Flexible F-Link" area. One F-communication each for the send and receive side.
3. Configure the same F-monitoring time and F-communication UUID for each F-runtime group communication relationship.

   Information on calculating the F-monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times).

   For example:

   ![F-runtime group communication](images/141852854411_DV_resource.Stream@PNG-en-US.png)
4. On the send side (e.g. RTG1) supply the data of the [F-communication DB](#f-communication-db-s7-1200-s7-1500) for the send direction with the data to be sent.

   For example:

   ![F-runtime group communication](images/116046378379_DV_resource.Stream@PNG-en-US.png)
5. On the receive side (e.g. RTG2), read the received data from the [F-communication DB](#f-communication-db-s7-1200-s7-1500) for the receive direction.

   For example:

   ![F-runtime group communication](images/113628940555_DV_resource.Stream@PNG-en-US.png)
6. Call the instruction "UMOVE_BLK" in the F-runtime group for the send data (e.g. RTG1) in the FC for [post processing](#pre-postprocessing-s7-1200-s7-1500).
7. Interconnect the "UMOVE_BLK" instruction for the data to be sent as follows:

   ![F-runtime group communication](images/113630195851_DV_resource.Stream@PNG-en-US.png)

   "Send" is the [F-communication DB](#f-communication-db-s7-1200-s7-1500) of the F-runtime group that sends the data.

   "Receive" is the [F-communication DB](#f-communication-db-s7-1200-s7-1500) of the F-runtime group that receives the data.
8. Call the instruction "UMOVE_BLK" in the F-runtime group for acknowledgment (e.g. RTG2) in the FC for [post processing](#flexible-f-link-area-s7-1200-s7-1500).
9. Interconnect the "UMOVE_BLK" instruction for the acknowledgment connection as follows:

   ![F-runtime group communication](images/113630203531_DV_resource.Stream@PNG-en-US.png)

   "Receive" is the [F-communication DB](#f-communication-db-s7-1200-s7-1500) of the F-runtime group that sends the acknowledgment telegram.

   "Send" is the [F-communication DB](#f-communication-db-s7-1200-s7-1500) of the F-runtime group that receives the acknowledgment telegram.
10. Compile the user program.
11. Download the user program to the F‑CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For each communication connection via Flexible F-Link, you must check that the offsets of the elements of the F-compliant PLC data type (UDT) used for the communication connection match on the transmit and receive sides when you accept the safety program.    You can find the offsets in the respective safety summary. To do this identify the communication connection by means of the UUID. (S088) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When a new Flexible F-Link communication is created in the Safety Administration Editor, a unique F-communication UUID for the communication is provided by the system. By copying communications in the Safety Administration Editor within the parameterization table or when copying to another F-CPU, the F-communication UUIDs are not regenerated and are therefore not unique anymore. If the copy is used to configure a new communication relationship, you yourself must ensure the uniqueness. To do this, select the affected UUIDs and regenerate via the "Generate UUID" shortcut menu. The uniqueness must be checked in the safety summary during acceptance. (S087) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |

##### Up-to-dateness of tags read from another F‑runtime group

The same statements as those in the section "[F-runtime group communication (S7-300, S7-400)](#f-runtime-group-communication-s7-300-s7-400)" apply (except for the storage locations written or read or initial values).

#### Deleting an F-runtime group

##### Deleting an F-runtime group

To delete an F-runtime group, proceed as follows:

1. In the area navigation of the Safety Administration Editor, click on the F‑runtime group to be deleted.
2. Select the "Delete F-runtime group" button in the work area.
3. Confirm the dialog with "Yes".
4. [Compile the safety program](#compiling-the-safety-program) (menu command "Edit > Compile") to put your changes into effect.

The assignment of the F-blocks to an F-runtime group (to the calling block of the main safety block) is deleted. However, the F-blocks continue to exist.

#### Changing the F-runtime group (S7-300, S7-400)

##### Changing an F-runtime group

You can make the following changes for each F-runtime group in your safety program in the corresponding "F-runtime group" work area:

- Specify another block as the calling block of the main safety block.
- Specify another F-FB or F-FC as main safety block.
- Enter a different or new I-DB for the main safety block.
- Change the value for the maximum cycle time of the F-runtime group
- Specify another DB as a data block for F-runtime group communication.

#### Changing the F-runtime group (S7-1200, S7-1500)

##### Changing an F-runtime group

You can make the following changes for each F-runtime group in your safety program in the corresponding "F-runtime group" work area:

- Change the name, number, cycle time, phase shift and priority of the F-OB.
- Specify another F-FB or F-FC as main safety block.
- Enter a different or new I-DB for the main safety block.
- Change the value for the maximum cycle time and the cycle time warning limit of the F-runtime group.
- Assign another name for the F-runtime group information DB.
- Specify an FC for the preprocessing and postprocessing.

### Creating F-blocks in FBD / LAD

This section contains information on the following topics:

- [Creating F-blocks](#creating-f-blocks)
- [Know-how protection](#know-how-protection)
- [Reuse of F-blocks](#reuse-of-f-blocks)

#### Creating F-blocks

##### Introduction

In order to create F-FBs, F-FCs, and F-DBs for the safety program, you should follow the same basic procedure as in the standard. In the following, only the deviations from the procedure for standard blocks are presented.

##### Creating F-FBs, F-FCs, and F-DBs

You create F-blocks in the same way as for standard blocks. Proceed as follows:

1. In the project tree of the F-CPU or the Safety Unit, double-click on "Add new block" under "Program blocks".
2. In the dialog that appears, specify the type, name, and language and select the "Create F-block" check box. (If you do not select the check box, a standard block is created.)
3. After the dialog is confirmed, the F-block is opened in the Program editor.

##### Note the following

Note the following important instructions:

> **Note**
>
> - You may not declare block parameters in the block interface of the main safety block because they cannot be supplied.
> - (S7-1200, S7-1500) You can edit start values in instance DBs.
> - The function "Apply actual values" is not supported.
> - You may not access static local data in single instances or multi-instances of other F-FBs.
> - You must always initialize outputs of F‑FCs.
>
>   The F‑CPU can go to STOP mode if the information above is not observed. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
> - (S7-300, S7-400) If you wish to assign an address from the data area (data block) to a formal parameter of an F‑FC as an actual parameter, you have to use fully qualified DB access.
> - Its inputs may only be accessed by a block in reading mode and its outputs only in writing mode.
>
>   Use an in/out if you wish to have both read and write access.
> - For greater clarity, assign meaningful names to the F‑blocks you have created.

##### Copying/pasting F-blocks

You can copy F-FBs, F-FCs, and F-DBs in exactly the same was as blocks of the standard user program.

**Exceptions:**

- (S7-1200, S7-1500) You may not copy an F-OB.
- You cannot copy blocks from the folder "Program blocks > System blocks".
- (S7-1500) F-blocks cannot be copied from the Safety Unit to a standard unit or between the Safety Unit and the "Program blocks" folder of the F-CPU.

---

**See also**

[Changing the F-runtime group (S7-1200, S7-1500)](#changing-the-f-runtime-group-s7-1200-s7-1500)

#### Know-how protection

For know-how protection of F-blocks, proceed as described in the STEP 7 help under "Protecting blocks".

##### Requirements

Note the following with regard to know-how protection of F-blocks for S7-1200/1500 F-CPUs:

- An F-block to which you wish to assign know-how protection must be called in the safety program.
- Before you can set up the know-how protection for an F-block, the safety program must be consistent. For this purpose, [compile](#compiling-the-safety-program) the safety program.

> **Note**
>
> No source code is output in the safety summary for know-how-protected F-blocks. Therefore, create the safety summary (for example, for carrying out a code review or for F-block acceptance) before you set up the know-how protection.

> **Note**
>
> If you want to edit the program code and/or the block interface of a know-how protected F-block, we recommend that you do not open the F-block by entering a password, but rather remove the know-how protection completely and set it up again after compiling.

> **Note**
>
> (S7-1200, S7-1500) When a know-how protected F-block or F-blocks called by it are renamed, the signature of the know-how protected F-block is not changed until the password is entered when opening or removing the know-how protection.

> **Note**
>
> When know-how protected F-blocks are used, warnings and error messages whose cause can lie in the know-how protected F-blocks can be displayed during compilation of the safety program. The warnings and error messages contain corresponding information. Example: In a know-how protected F-block, you perform read access to a tag of the standard user program to which write access is taking place in a different (know-how protected) F-block.
>
> For S7-1200/1500 F-CPUs, you can obtain additional information in the section "Know-how protected F-blocks in the safety program" of the safety summary.

> **Note**
>
> **Named value data types (S7-1500)**
>
> You cannot use Named value data types in know-how protected F-blocks.

---

**See also**

[Reuse of F-blocks](#reuse-of-f-blocks)

#### Reuse of F-blocks

##### Introduction

You can reuse F-blocks that you have already tested and, if applicable, approved, in other safety programs – without having to test and approve them again.

You can protect the content of the F-block by setting up the know-how protection. You may only set this protection after acceptance of the F-block to ensure that the safety summary contains this F-block in its entirety.

Like standard blocks, you can store F-blocks as master copies or types in global libraries or in the project library.

More information can be found in the STEP 7 help under "Using libraries".

##### Creating safety summary for the F-block to be reused

Create a safety summary with the following information for F-blocks that you want to reuse.

**S7-300/400 F-CPUs**

- Signature and initial value signature of the know-how protected F-block
- Versions of all the used versioned LAD/FBD instructions
- Signatures and initial value signatures of all called F-FBs and F-FCs
- Signatures of all F-DBs accessed by the fail-safe block to be reused.

**S7-1200/1500 F-CPUs**

- Signature of the know-how protected F-block
- Safety system version when setting up the know-how protection
- Versions of all the used versioned LAD/FBD instructions
- Signatures of all called F-FBs and F-FCs
- Signatures of all F-DBs accessed by the fail-safe block to be reused.

The safety summary should also contain a description of the functionality of the F-block, in particular if it is know-how protected.

The required information is obtained by creating the safety summary of the safety program in which you originally created, tested and approved the F-block to be reused.

This safety summary can also serve directly as the safety summary for the F-block to be reused.

##### Checks when using the F-block to be reused

When reusing the F-block, ensure the following:

- The signature and initial value signature (S7-300, S7-400) of the F-block are unchanged.
- (SIMATIC S7-1200, S7-1500) The documented safety system version is set.
- The documented (or functionally identical) versions of the versioned LAD/FBD instructions are set. You can find information about the instruction versions in the description of the instructions.
- (S7-1200, S7-1500) The called and accessed F-blocks with the documented signatures are used.
- (S7-300, S7-400) The called F-blocks with the documented signatures and initial value signatures are used.

If the version conflicts cannot be eliminated due to other dependencies, contact the author of the know-how protected block in order to obtain a compatible approved version.

---

**See also**

[Compliance of the know-how protected F-blocks used in the safety program with their safety summary.](#compliance-of-the-know-how-protected-f-blocks-used-in-the-safety-program-with-their-safety-summary)

### Information interface to the safety program

This section contains information on the following topics:

- [F-shared DB (S7-300, S7-400)](#f-shared-db-s7-300-s7-400)
- [F-runtime group information DB (S7-1200, S7-1500)](#f-runtime-group-information-db-s7-1200-s7-1500)

#### F-shared DB (S7-300, S7-400)

##### Function

The F‑shared DB is a fail-safe data block that contains all of the shared data of the safety program and additional information needed by the F‑system. The F-shared DB is automatically inserted when the hardware configuration is compiled.

Using its name F_GLOBDB, you can evaluate certain data elements of the safety program in the standard user program.

##### Reading an F‑shared DB in the standard user program

You can read out the following information in the F-shared DB in the standard user program or on an operator control and monitoring system:

- Operating mode: safety mode or disabled safety mode ("MODE" tag)
- Error information "Error occurred when executing safety program" ("ERROR" tag)
- Collective F-Signature ("F_PROG_SIG" tag)
- Compilation date of the safety program ("F_PROG_DAT" tag, DATE_AND_TIME data type)

You use fully qualified access to access these tags (e.g. ""F_GLOBDB".MODE").

#### F-runtime group information DB (S7-1200, S7-1500)

##### Introduction

The F-runtime group information DB provides key information on the corresponding F-runtime group and on the safety program as a whole.

The F-runtime group information DB is generated automatically when an F-runtime group is created. A symbol, for example, "RTG1SysInfo", is assigned for the F-runtime group information DB. You can change the name in the Safety Administration Editor.

You must not access the information in the "F_SYSINFO" parameter from the safety program.

##### Information in the F-runtime group information DB

The F-runtime group information DB provides the following information:

| Name |  | Data type | For processing in the safety program | For processing in the standard user program | Description |
| --- | --- | --- | --- | --- | --- |
| MODE |  | BOOL | x | x | 1 = Disabled safety mode |
| MODE_REMAINING_TIME |  | TIME | x | x | Remaining runtime in deactivated safety mode until the F-CPU switches to STOP * |
| F_SYSINFO |  |  |  |  |  |
|  | MODE | BOOL | — | x | 1 = Disabled safety mode |
| TCYC_CURR | DINT | — | x | Current cycle time of the F-runtime group, in ms |  |
| TCYC_LONG | DINT | — | x | Longest cycle time of the F-runtime group, in ms |  |
| TRTG_CURR | DINT | — | x | Current runtime of the F-runtime group, in ms |  |
| TRTG_LONG | DINT | — | x | Longest runtime of the F-runtime group, in ms |  |
| T1RTG_CURR | DINT | — | x | Not supported by STEP 7 Safety V19. |  |
| T1RTG_LONG | DINT | — | x | Not supported by STEP 7 Safety V19. |  |
| F_PROG_SIG | DWORD | — | x | Collective F-Signature of the safety program |  |
| F_PROG_DAT | DTL | — | x | Compilation date of the safety program |  |
| F_RTG_SIG | DWORD | — | x | F-runtime groups signature |  |
| F_RTG_DAT | DTL | — | x | Compilation date of the F-runtime group |  |
| VERS_S7SAF | DWORD | — | x | Version identifier for STEP 7 Safety |  |
| * When the F-CPU switches to STOP after the runtime for the deactivated safety mode has expired, the remaining time still present in the last cycle is displayed. |  |  |  |  |  |

You access the content of the F-runtime group information DB with fully qualified addressing. Either collectively with the F_SYSINFO PLC data type (UDT), for example, "RTG1SysInfo.F_SYSINFO", provided by the F-system or individual information, for example, "RTG1SysInfo.F_SYSINFO.MODE".

---

**See also**

[Program identification](#program-identification)

### Programming startup protection

#### Introduction

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unintentional restart**  In contrast to the standard user program, when the safety program starts up, all tags of the F-DBs are generally initialized with their start values. This means that saved error information is lost. The F-system performs automatic reintegration of the F‑I/O.  If an unintentional startup of your process is not allowed, you must program restart/startup protection in the safety program. For this, the output of process values must be blocked until user acknowledgment takes place (see "[Implementation of user acknowledgment](#implementation-of-user-acknowledgment)"). This user acknowledgment must not take place until safe output of process values is possible.  You must expect an unintentional restart in the following cases:  - After a STOP generated by PG/PC operation, mode switch, communication function or "STP" instruction - After an operating error - After a STOP caused by a fault reaction function    (S008) |  |

#### Example of restart/startup prevention

In order to implement a restart/startup prevention, it must be possible to detect a startup. To detect a startup, you declare a tag of data type BOOL with initial value "TRUE" in an F-DB.

Block the output of process data when this tag has the value "1," for example, by passivating F‑I/O using the PASS_ON tag in the F‑I/O DB.

If the output of the process values is safely possible and errors have been corrected, reset this tag by a user acknowledgment.

---

**See also**

[Implementing User Acknowledgment in the Safety Program of the F-CPU of a DP Master or IO controller](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-dp-master-or-io-controller)
  
[Implementing user acknowledgment in the safety program of the F-CPU of a I-slave or I-device](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-i-slave-or-i-device)
  
[F‑I/O DB](#f-io-db)

## F-I/O access

This section contains information on the following topics:

- [Introduction](#introduction-1)
- [Addressing F-I/O](#addressing-f-io)
- [Value status (S7-1200, S7-1500)](#value-status-s7-1200-s7-1500)
- [Process Data or Fail-Safe Values](#process-data-or-fail-safe-values)
- [F‑I/O DB](#f-io-db)
- [Passivation and reintegration of F-I/O](#passivation-and-reintegration-of-f-io)

### Introduction

The following sections contain a general description of F-I/O access.

The following sections are only valid to a limited extent for technology modules (e.g. F-TM Count 1x1Vpp sin/cos HF). You can find more detailed information in the respective equipment manuals.

### Addressing F-I/O

#### Overview

Below you will find a description of how to address the F-I/O in the safety program and which rules must be observed in the process.

#### Addressing via the process image

As with standard I/O, you access F‑I/O (e.g., S7-1500/ET 200MP fail-safe modules) via the **process image** (PII and PIQ).

Direct reading (with I/O identification ":P") of inputs or writing of outputs is not possible in the safety program.

#### Updating the process image

The process image of the inputs of F-I/O is updated at the start of the F-runtime group. The process image of the outputs of F-I/O is updated at the end of the F-runtime group (see [Program structure of the safety program (S7-300, S7-400)](#program-structure-of-the-safety-program-s7-300-s7-400) or [Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500)). For more information on updating the process image, refer to the note in [Data Transfer from the Safety Program to the Standard User Program](#data-transfer-from-the-safety-program-to-the-standard-user-program).

The communication required between the F‑CPU (process image) and the F‑I/O to update the process image uses a special safety protocol in accordance with PROFIsafe.

#### Rules

- You may only address a channel (channel value and value status) of an F-I/O in **one** F-runtime group. The first programmed addressing defines the assignment for the F-runtime group.
- You may only address a channel (channel value and value status) of an F-I/O with a unit that matches the data type of the channel.  
  Example: To access input channels of data type BOOL, you must use the "input (bit)" (I x.y) unit. Access to the 16 consecutive input channels of the data type BOOL via the unit "input word" (IW x) is not possible.
- Analog channels always need to be entered in the tag table with data type INT or DINT. The data types WORD, DWORD and TIME are not permissible.
- Address only inputs and outputs that reference an actually existing channel (channel value and value status) (e.g. for an F-DO 10xDC24V with start address 10 only the outputs Q10.0 to Q11.1 for the channel values and the inputs I10.0 to I11.1 for the value status). Keep in mind that due to the special safety protocol, the F-I/O occupies a larger area of the process image than is required for the existing and enabled channels on the F-I/O (channel values and value status). To find the area of the process image where the channels (channel values and value status) are stored (channel structure), refer to the relevant manuals for the F-I/O.
- Channels can be disabled for certain F-I/O (such as ET 200SP fail-safe modules or S7-1500/ET 200MP fail-safe modules). Address only channels (channel value and value status) that are enabled in the hardware configuration. When you address channels that are disabled in the hardware configuration, a warning may be output when compiling the safety program.
- For certain F-I/O (such as ET 200SP fail-safe modules or S7-1500/ET 200MP fail-safe modules), a "1oo2 (2v2) sensor evaluation" can be specified. Two channels are grouped into one channel pair in this case, and the result of the "1oo2 sensor evaluation" is usually provided under the address of the channel with the lower channel number (see relevant manuals of the F-I/O). Address only this channel (channel value and value status) of the channel pair. When you address a different channel, a warning may be output when compiling the safety program.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you use an additional component between the F-CPU (S7-300, S7-400) and the F-I/O that copies the safety message frame in accordance with PROFIsafe between the F-CPU (S7-300, S7-400) and F-I/O per user program, you must test all safety functions affected by the copy function whenever you change the user-programmed copy function. (S049) |  |

---

**See also**

[Safety-Related I-Slave-Slave Communication - F-I/O Access](#safety-related-i-slave-slave-communication---f-io-access)
  
[Value status (S7-1200, S7-1500)](#value-status-s7-1200-s7-1500)

### Value status (S7-1200, S7-1500)

#### Properties

The value status is additional binary information for the channel value of an F-I/O. The value status is entered in the process image input (PII).

The value status is supported by S7-1500/ET 200MP, ET 200SP, ET 200AL, ET 200eco PN, ET 200S, ET 200iSP, ET 200pro, S7-1200 fail-safe modules or S7-300 F-SMs, fail-safe I/O standard devices as well as fail-safe DP standard slaves that support the "RIOforFA-Safety" profile. Information about the value status can be found in the documentation of the respective F-I/O.

We recommend you amend the name of the channel value with "_VS" for the value status, for example, "TagIn_1_VS".

The value status provides information on the validity of the corresponding channel value:

- 1: A valid process value is output for the channel.
- 0: A fail-safe value is output for the channel.

The channel value and value status of an F-I/O can only be accessed from the same F-runtime group.

#### Location of value status bits in the PII for F-I/O with digital inputs

The value status bits come straight after the channel values in the PII.

Example: Address assignment in PII for F-I/O with 16 digital input channels

| Byte in the F-CPU | Assigned bits in F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | DI<sub>7</sub> | DI<sub>6</sub> | DI<sub>5</sub> | DI<sub>4</sub> | DI<sub>3</sub> | DI<sub>2</sub> | DI<sub>1</sub> | DI<sub>0</sub> |
| **x + 1** | DI<sub>15</sub> | DI<sub>14</sub> | DI<sub>13</sub> | DI<sub>12</sub> | DI<sub>11</sub> | DI<sub>10</sub> | DI<sub>9</sub> | DI<sub>8</sub> |
| **x + 2** | Value status DI<sub>7</sub> | Value status DI<sub>6</sub> | Value status DI<sub>5</sub> | Value status DI<sub>4</sub> | Value status DI<sub>3</sub> | Value status DI<sub>2</sub> | Value status DI<sub>1</sub> | Value status DI<sub>0</sub> |
| **x + 3** | Value status DI<sub>15</sub> | Value status DI<sub>14</sub> | Value status DI<sub>13</sub> | Value status DI<sub>12</sub> | Value status DI<sub>11</sub> | Value status DI<sub>10</sub> | Value status DI<sub>9</sub> | Value status DI<sub>8</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

The location of the channel values in the PII can be found in the device manual for the F-I/O.

#### Location of value status bits in the PII for F-I/O with digital outputs

The value status bits in the PII are mapped with the same structure as the channel values in the PIQ.

Example: Address assignment in PIQ for F-I/O with 4 digital output channels

| Byte in the F-CPU | Assigned bits in F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | — | — | — | — | DQ<sub>3</sub> | DQ<sub>2</sub> | DQ<sub>1</sub> | DQ<sub>0</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

Example: Address assignment in PII for F-I/O with 4 digital output channels

| Byte in the F-CPU | Assigned bits in F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | — | — | — | — | Value status DQ<sub>3</sub> | Value status DQ<sub>2</sub> | Value status DQ<sub>1</sub> | Value status DQ<sub>0</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

The location of the channel values in the PIQ can be found in the device manual for the F-I/O.

#### Location of value status bits in the PII for F-I/O with digital outputs and digital inputs

The value status bits come directly after the channel values in the PII in the following order:

- Value status bits for the digital inputs
- Value status bits for the digital outputs

Example: Address assignment in PIQ for F-I/O with 2 digital input channels and 1 digital output channel

| Byte in the F-CPU | Assigned bit in the F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | — | — | — | — | — | — | — | DQ<sub>0</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

Example: Address assignment in PII for F-I/O with 2 digital input channels and 1 digital output channel

| Byte in the F-CPU | Assigned bits in F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | — | — | — | — | — | — | DI<sub>1</sub> | DI<sub>0</sub> |
| **x + 1** | — | — | — | — | — | — | Value status DI<sub>1</sub> | Value status DI<sub>0</sub> |
| **x + 2** | — | — | — | — | — | — | — | Value status DQ<sub>0</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

The location of the channel values in the PII and PIQ can be found in the device manual for the F-I/O.

#### Location of value status bits in the PII for F-I/O with analog inputs

The value status bits come straight after the channel values in the PII.

Example: Address assignment in PII for F-I/O with 6 analog input channels (data type INT)

| Byte in the F-CPU | Assigned bytes/bits in the F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | Channel value AI<sub>0</sub> |  |  |  |  |  |  |  |
| **...** | ... |  |  |  |  |  |  |  |
| **x + 10** | Channel value AI<sub>5</sub> |  |  |  |  |  |  |  |
| **x + 12** | — | — | Value status AI<sub>5</sub> | Value status AI<sub>4</sub> | Value status AI<sub>3</sub> | Value status AI<sub>2</sub> | Value status AI<sub>1</sub> | Value status AI<sub>0</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

The location of the channel values in the PII can be found in the device manual for the F-I/O.

#### Location of value status bits in the PII for F-I/O with analog outputs

The value status bits are mapped in the PII.

Example: Address assignment in PIQ for F-I/O with 6 analog output channels (data type INT)

| Byte in the F-CPU | Assigned bytes in the F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | Channel value AO<sub>0</sub> |  |  |  |  |  |  |  |
| ... | ... |  |  |  |  |  |  |  |
| **x + 10** | Channel value AO<sub>5</sub> |  |  |  |  |  |  |  |
| x = Module start address |  |  |  |  |  |  |  |  |

Example: Address assignment in PII for F-I/O with 6 analog output channels (data type INT)

| Byte in the F-CPU | Assigned bits in F-CPU per F-I/O: |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |  |
| **x + 0** | — | — | Value status AO<sub>5</sub> | Value status AO<sub>4</sub> | Value status AO<sub>3</sub> | Value status AO<sub>2</sub> | Value status AO<sub>1</sub> | Value status AO<sub>0</sub> |
| x = Module start address |  |  |  |  |  |  |  |  |

The location of the channel values in the PIQ can be found in the device manual for the F-I/O.

### Process Data or Fail-Safe Values

#### When are fail-safe values used?

The safety function requires that fail-safe values (0) be used instead of process data for passivation of the entire F-I/O or individual channels of an F-I/O in the following cases. This applies both to digital channels (data type BOOL) as well as for analog channels (data type INT or DINT):

- When the F-system starts up
- When errors occur during safety-related communication (communication errors) between the F-CPU and F-I/O using the safety protocol in accordance with PROFIsafe
- When F-I/O faults and channel faults occur (such as wire break, short circuit, and discrepancy errors)
- As long as you enable passivation of the F-I/O with PASS_ON = 1 in the F-I/O DB (see below)
- As long as you disable the F-I/O with DISABLE = 1 in the F-I/O DB (see below)

#### Fail-safe value output for F-I/O/channels of an F-I/O

When **passivation** occurs for an **F-I/O with inputs**, the F-system provides the safety program with fail-safe values (0) in the PII instead of the process data pending at the fail-safe inputs of the F-I/O.

The overflow or underflow of a channel of the **SM 336; AI 6 x 13Bit** or **SM 336; F‑AI 6 x 0/4 ... 20 mA HART** is recognized by the F-system as an F-I/O/channel fault. The fail-safe value 0 is provided in place of 7FFF<sub>H</sub> (for overflow) or 8000<sub>H</sub> (for underflow) in the PII for the safety program.

If you want to process fail-safe values other than "0" in the safety program for an F‑I/O with inputs **for analog channels of data type** **INT** **or** **DINT**, you can assign individual fail-safe values for QBAD = 1 and value status = 0 or QBAD_I_xx/QBAD_O_xx = 1 (instructions JMP/JMPN, LABEL and MOVE). For details about the characteristics go to [QBAD/PASS_OUT/DISABLED/QBAD_I_xx/QBAD_O_xx and value status](#qbadpass_outdisabledqbad_i_xxqbad_o_xx-and-value-status).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For an F-I/O with digital input channels (data type BOOL), the value provided in the PII must always be processed in the safety program, regardless of the value status or QBAD/QBAD_I_xx. (S009) |  |

When **passivation** occurs in an **F‑I/O with outputs**, the F‑system outputs fail-safe values (0) at the fail-safe outputs instead of the output values provided by the safety program in the PIQ.

| State of associated PAA/PIQ by ... | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPUs | F-I/O without "RIOforFA-Safety" profile with S7-1200/1500 F-CPUs | F-I/O with S7-300/400 F-CPUs |
| --- | --- | --- | --- |
| Startup of F-system | The F-system overwrites the PII/PIQ with fail-safe values (0). |  |  |
| Communication errors |  |  |  |
| F-I/O faults | The F-system overwrites the PII with fail-safe values (0). In the PII the values formed in the safety program are retained. | The F-system overwrites the PII/PIQ with fail-safe values (0). |  |
| Channel faults in configuration of passivation for complete F-I/O |  |  |  |
| Channel faults during configuration of channel-granular passivation | For the affected channels: The F-system overwrites the PII/PIQ with fail-safe values (0). |  |  |
| As long as passivation of the F-I/O is activated in the F-I/O DB with PASS_ON = 1 | The F-system overwrites the PII/PIQ with fail-safe values (0). |  |  |
| As long as the F-I/O is deactivated in the F-I/O DB with DISABLE = 1 | The F-system overwrites the PII/PIQ with fail-safe values (0). |  | - |

#### Reintegration of F-I/O/channels of an F-I/O

The switchover from fail-safe values (0) to process data (**reintegration of an F-I/O**) takes place **automatically** or following **user acknowledgment** in the F-I/O DB. The reintegration method depends on the following:

- The reason for passivation of the F-I/O or channels of the F-I/O
- At F-I/Os without the "Channel failure acknowledge" channel parameter on the value of the ACK_NEC variable of the associated [F-IO data blocks](#f-io-db).
- At F-I/Os with the "Channel failure acknowledge" channel parameter (for example F-modules S7-1500 / ET 200 MP / F-modules SIMATIC S7-1200) on the value of the channel parameter.

For fail-safe GSD based DP slaves / GSD based I/O devices with "RIOforFA-Safety" profile, consult the respective documentation.

> **Note**
>
> Note that for channel faults in the F‑I/O, channel-granular passivation takes place if configured accordingly in the hardware and network editor. For the concerned channels, fail-safe values (0) are output.
>
> Reintegration after channel faults reintegrates all channels whose faults were eliminated; faulty channels remain passivated.

---

**See also**

[Configuring F-I/O](#configuring-f-io)

### F-I/O DB

This section contains information on the following topics:

- [F‑I/O DB](#f-io-db-1)
- [Name and number of the F‑I/O DB](#name-and-number-of-the-f-io-db)
- [Tags of the F-I/O DB](#tags-of-the-f-io-db)
- [Accessing tags of the F-I/O DB](#accessing-tags-of-the-f-io-db)

#### F-I/O DB

##### Introduction

An F-I/O DB is automatically generated for each F-I/O (in safety mode) when the F-I/O is configured in the hardware and network editor. The F-I/O DB contains tags that you can evaluate or can/must write to in the safety program. It is not permitted to change the initial values of the tags directly in the F-I/O DB. When an F-I/O is deleted, the associated F-I/O DB is also deleted.

##### Access to an F-I/O DB

You access tags of the F‑I/O DB for the following reasons:

- For reintegration of F-I/O after communication errors, F-I/O faults, or channel faults
- If you want to passivate the F‑I/O depending on particular states of your safety program (for example, group passivation)
- If you want to deactivate the F‑I/O (for example, configuration control)
- For changing parameters for fail-safe GSD based DP slaves/GSD based I/O devices
- If you want to evaluate whether fail-safe values or process data are output

#### Name and number of the F-I/O DB

The name of the F‑I/O DB is formed by:

- the fixed prefix "F"
- the start address of the F-I/O, and the names entered in the properties of the F-I/O in the hardware and network editor or in the device view (max. the first 24 characters)

Example: F00004_F-DI24xDC24V_1

The number is assigned within the number range defined in the "Settings" [area](#settings-area) of the Safety Administration Editor.

##### Option "Creates F-I/O DBs without prefix" (S7-1200, S7-1500)

When you select the option "Creates F-I/O DBs without prefix" in the "Settings" area in the Safety Administration Editor, the name is formed only from:

- the name entered in the properties of the F-I/O in the hardware and network editor or in the device view (max. 117 characters)

Example: F-DI24xDC24V_1

##### Changing the name and number of the F‑I/O DB

You change the name by changing the name entered in the properties of the F-I/O in the hardware and network editor or in the device view.

You change the number in the "Properties"/"F-parameters" tab of the associated F‑I/O.

#### Tags of the F-I/O DB

This section contains information on the following topics:

- [Tags of the F-I/O DB](#tags-of-the-f-io-db-1)
- [PASS_ON](#pass_on)
- [ACK_NEC](#ack_nec)
- [ACK_REI](#ack_rei)
- [IPAR_EN](#ipar_en)
- [DISABLE](#disable)
- [QBAD/PASS_OUT/DISABLED/QBAD_I_xx/QBAD_O_xx and value status](#qbadpass_outdisabledqbad_i_xxqbad_o_xx-and-value-status)
- [ACK_REQ](#ack_req)
- [IPAR_OK](#ipar_ok)
- [DIAG](#diag)

##### Tags of the F-I/O DB

The following table presents the variables of an F‑I/O DB:

|  | Tag | Data type | Function | Initial value |
| --- | --- | --- | --- | --- |
| **Tags that you can or must write** | PASS_ON | BOOL | 1=enable passivation | 0 |
| ACK_NEC | BOOL | 1=acknowledgment for reintegration required in the event of F-I/O or channel faults | 1 |  |
| ACK_REI | BOOL | 1=acknowledgment for reintegration | 0 |  |
| IPAR_EN | BOOL | Tag for parameter reassignment of fail-safe GSD based DP slaves/GSD based I/O devices or, in the case of SM 336; F‑AI 6 x 0/4 ... 20 mA HART, for enabling HART communication | 0 |  |
| DISABLE* | BOOL | 1=Deactivate F-I/O | 0 |  |
| **Tags that you can evaluate** | PASS_OUT | BOOL | Passivation output | 1 |
| QBAD | BOOL | 1=Fail-safe values are output | 1 |  |
| ACK_REQ | BOOL | 1=Acknowledgment request for reintegration | 0 |  |
| IPAR_OK | BOOL | Tag for parameter reassignment of fail-safe GSD based DP slaves/GSD based I/O devices or, in the case of SM 336; F‑AI 6 x 0/4 ... 20 mA HART, for enabling HART communication | 0 |  |
| DIAG | BYTE | Non-fail safe service information | 0 |  |
| DISABLED* | BOOL | 1=F-I/O is deactivated | 0 |  |
| QBAD_I_xx | BOOL | 1=Fail-safe values are output to input channel xx (S7-300, S7-400) | 1 |  |
| QBAD_O_xx | BOOL | 1=Fail-safe values are output to output channel xx (S7-300, S7-400) | 1 |  |
| * as of Safety system version V2.1 for S7-1200/1500 |  |  |  |  |

###### Differences in evaluation in S7-1200/1500 F-CPUs and S7-300/400

The following table describes the differences in the evaluation of tags of the F-I/O DB and the value status depending on the F-I/O and F-CPU used.

| Tag in the F-I/O DB or value status | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O without "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O with S7-300/400 F-CPU |
| --- | --- | --- | --- |
| ACK_NEC | —<sup>2</sup> | x | x |
| QBAD<sup>3</sup> | x | x | x |
| PASS_OUT<sup>3</sup> | x | x | x |
| QBAD_I_xx<sup>1</sup> | — | — | x |
| QBAD_O_xx<sup>1</sup> | — | — | x |
| Wertstatus<sup>1</sup> | x | x | — |
| <sup>1</sup> QBAD_I_xx and QBAD_O_xx display the validity of the channel value channel-granular and thus correspond to the inverted value status with S7-1200/1500. Value status or QBAD_I_xx and QBAD_O_xx are not available with fail-safe DP GSD based slaves or fail-safe GSD based I/O devices without the "RIOforFA-Safety" profile.   <sup>2</sup> In the case of F-I/Os that support the "Channel failure acknowledge" channel parameter (for example S7-1500/ET 200MP F-modules or S7-1200 F-modules), this replaces the ACK_NEC variable of the F-IO data block.    <sup>3</sup> For details about the characteristics, see "QBAD/PASS_OUT/DISABLED/QBAD_I_xx/QBAD_O_xx and value status" |  |  |  |

##### PASS_ON

The PASS_ON tag allows you to enable passivation of an F‑I/O, for example, depending on particular states in your safety program.

Using the PASS_ON tag in the F-I/O DB, you can passivate F-I/O; channel-granular passivation is not possible.

As long as PASS_ON = 1, **passivation** of the associated F-I/O occurs.

##### ACK_NEC

If an F-I/O fault is detected by the F-I/O, **passivation** of the relevant F-I/O occurs. If channel faults are detected and channel granular passivation is configured, the relevant channels are passivated. If passivation of the entire F-I/O is configured, all channels of the relevant F-I/O are passivated. Once the F-I/O fault or channel fault has been eliminated, **reintegration** of the relevant F-I/O occurs, depending on ACK_NEC:

- With ACK_NEC = 0, you can assign an **automatic reintegration**.
- With ACK_NEC = 1, you can assign a **reintegration** by **user acknowledgment**.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The parameter assignment of the ACK_NEC tag of the F-I/O DB with the value "0" is only allowed if automatic reintegration is permitted for the relevant process from a safety standpoint. (S010) |  |

> **Note**
>
> The initial value for ACK_NEC is 1 after creation of the F‑I/O DB. If you do not require automatic reintegration, you do not have to write ACK_NEC.

---

**See also**

[After F-I/O or channel faults](#after-f-io-or-channel-faults)

##### ACK_REI

When the F-system detects a communication error or an F-I/O fault for an F-I/O, the relevant F-I/O is passivated. If channel faults are detected and channel granular passivation is configured, the relevant channels are passivated. If passivation of the entire F-I/O is configured, all channels of the relevant F-I/O are passivated. **Reintegration** of the F‑I/O/channels of the F‑I/O after the fault has been eliminated requires a **user acknowledgment** with a positive edge at variable ACK_REI of the F‑I/O DB:

- After every communication error
- After F‑I/O or channel faults only with parameter assignment "Channel failure acknowledgement = manual" or ACK_NEC = 1

Reintegration after channel faults reintegrates all channels whose faults were eliminated.

Acknowledgment is not possible until tag ACK_REQ = 1.

In your safety program, you must provide a user acknowledgment by means of the ACK_REI tag for each F-I/O.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For the user acknowledgement, you must interconnect the ACK_REI tag of the F‑-I/O DB with a signal generated by an operator input. An interconnection with an automatically generated signal is not permitted. (S011) |  |

> **Note**
>
> Alternatively, you can use the "ACK_GL" instruction to carry out reintegration of the F-I/O following communication errors or F-I/O/channel faults ([ACK_GL: Global acknowledgment of all F-I/O in an F-runtime group (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#ack_gl-global-acknowledgment-of-all-f-io-in-an-f-runtime-group-step-7-safety-v19)).

##### IPAR_EN

The IPAR_EN tag corresponds to the iPar_EN_C tag in the PROFIsafe bus profile as of PROFIsafe Specification V1.20 and higher.

**Fail-safe GSD based DP slaves/GSD based I/O devices**

To find out when this tag must be set or reset when parameters of fail-safe GSD based DP slaves/GSD based I/O devices are reassigned, consult the PROFIsafe Specification V1.20 or higher or the documentation for the fail-safe GSD based DP slave/GSD based I/O device.

Note that IPAR_EN = 1 does not trigger passivation of the relevant F-I/O.

If passivation is to occur when IPAR_EN = 1, you must also set tag PASS_ON = 1.

**HART communication with** 
**SM 336; F‑AI 6 x 0/4 ... 20 mA HART**

If you set the IPAR_EN tag to "1" while parameter "HART_Tor" = "switchable" is assigned, the HART communication for the SM 336; F‑AI 6 x 0/4 ... 20 mA HART is enabled. Setting this tag to "0" disables the HART communication. The F‑SM acknowledges the enabled or disabled HART communication with tag IPAR_OK = 1 or 0.

Enable HART communication only when your system is in a status, in which any reassignment of parameters for an associated HART device can be done without any risk.

If you want to evaluate the "HART communication enabled" status in your safety program, e.g., for the purpose of programming interlocks, you must build up the information as shown in the following example. This is necessary to ensure that the information is properly available even if communication errors occur while the HART communication is enabled with IPAR_EN = 1. Only change the status of the IPAR_EN tag during this evaluation if there is no passivation due to a communication error or F-I/O or channel fault.

**Example of enabling HART communication**

![Figure](images/93482785163_DV_resource.Stream@PNG-en-US.png)

Additional information on HART communication with SM 336; F‑AI 6 x 0/4 ... 20 mA HART can be found in the [Automation System S7-300, ET 200M Distributed I/O System manual, Fail-Safe Signal Modules](http://support.automation.siemens.com/WW/view/en/19026151) manual and in the help on the F-module.

##### DISABLE

The DISABLE variable allows you to deactivate an F-I/O.

As long as DISABLE = 1, the associated F-I/Os are **passivated**.

Diagnostics entries of the safety program may no longer be entered in the diagnostics buffer of the F-CPU for this F-I/O (for example, due to communication error).

Existing diagnostics entries are marked as outgoing.

##### QBAD/PASS_OUT/DISABLED/QBAD_I_xx/QBAD_O_xx and value status

The following table set outs differences in the reaction of the channel values and QBAD, PASS_OUT, DISABLED, QBAD_I_xx/QBAD_O_xx variables and of the value status depending on the F-I/O and F-CPU used.

| Fail-safe value output after... | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O without profile  "RIOforFA-Safety" with S7-1200/1500 F-CPUs | F-I/O with S7-300/400 F-CPU |
| --- | --- | --- | --- |
| Startup of F-system | QBAD and PASS_OUT = 1  DISABLED **unchanged**  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| Communication errors |  |  |  |
| F-I/O faults |  |  |  |
| Channel faults in configuration of passivation for complete F-I/O |  |  |  |
| Channel faults during configuration of channel-granular passivation | QBAD, PASS_OUT and DISABLED **unchanged**  For the **affected** channels:   Channel value = fail-safe value (0)   Value status = 0 | QBAD and PASS_OUT = 1  DISABLED **unchanged**  For the **affected** channels:  Channel value = fail-safe value (0)  Value status = 0* | QBAD and PASS_OUT = 1  For the **affected** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| As long as passivation of the F-I/O is activated in the F-I/O DB with PASS_ON = 1 | QBAD = 1, PASS_OUT and DISABLED **unchanged**  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | QBAD = 1, PASS_OUT **unchanged**  For **all** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| As long as the F-I/O is deactivated in the F-I/O DB with DISABLE = 1 | QBAD, PASS_OUT and DISABLED = 1  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | - |
| * Value status or QBAD_I_xx and QBAD_O_xx are not available for fail-safe GSD based DP slaves and fail-safe GSD based I/O devices without the "RIOforFA-Safety" profile. |  |  |  |

##### ACK_REQ

When the F-system detects a communication error or an F-I/O fault or channel fault for an F‑I/O, the relevant F-I/O or individual channels of the F-I/O are passivated. ACK_REQ = 1 signals that **user acknowledgment** is required for reintegration of the relevant F-I/O or channels of the F-I/O.

The F-system sets ACK_REQ = 1 as soon as the fault has been eliminated and user acknowledgment is possible. For channel-granular passivation, the F-system sets ACK_REQ = 1 as soon as the channel fault is corrected. User acknowledgment is possible for this fault. Once acknowledgment has occurred, the F-system resets ACK_REQ to 0.

> **Note**
>
> For F-I/O with outputs, acknowledgment after F-I/O or channel faults may only be possible some minutes after the fault has been eliminated, until the necessary test signal is applied (see F-I/O manuals).

##### IPAR_OK

The IPAR_OK tag corresponds to the iPar_OK_S tag in the PROFIsafe bus profile, PROFIsafe Specification V1.20 and higher.

**Fail-safe GSD based DP slaves/GSD based I/O devices**

To find out how to evaluate this tag when parameters of fail-safe GSD based DP slaves or GSD based I/O devices are reassigned, consult the PROFIsafe Specification V1.20 or higher or the documentation for the fail-safe GSD based DP slave/GSD based I/O device.

**For HART communication with** 
**SM 336; F‑AI 6 x 0/4 ... 20 mA**
**HART see Chapter**
[IPAR_EN](#ipar_en).

##### DIAG

The DIAG tag provides non-fail-safe information (1 byte) about errors or faults that have occurred for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits are saved until you perform an acknowledgment with the ACK_REI tag or until automatic reintegration takes place.

###### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Timeout detected by F-I/O | The PROFIBUS/PROFINET connection between F‑CPU and F‑I/O is faulty.  The value of the F-monitoring time for the F-I/O is set too low.  The F-I/O are receiving invalid parameter assignment data  or | - Check the PROFIBUS/PROFINET connection and ensure that there are no external sources of interference. - Check the parameter assignment of the F-I/O. If necessary, set a higher value for the monitoring time. Recompile the hardware configuration, and download it to the F-CPU. Recompile the safety program. - Check the diagnostics buffer of the F-I/O. - Turn the power of the F-I/O off and back on. |
| Internal F-I/O fault  or | Replace F-I/O |  |  |
| Internal F-CPU fault | Replace F-CPU |  |  |
| Bit 1 | F-I/O fault or channel fault detected by F-I/O<sup>1</sup> | See F-I/O manuals | See F-I/O manuals |
| Bit 2 | CRC error or sequence number error detected by F-I/O | See description for bit 0 | See description for bit 0 |
| Bit 3 | Reserved | — | — |
| Bit 4 | Timeout detected by F-system | See description for bit 0 | See description for bit 0 |
| Bit 5 | Sequence number error detected by F-system<sup>2</sup> | See description for bit 0 | See description for bit 0 |
| Bit 6 | CRC-error detected by F-system | See description for bit 0 | See description for bit 0 |
| Bit 7 | Addressing error<sup>3</sup> | — | Contact Service & Support |
| <sup>1</sup> Not for F-I/O that support the "RIOforFA-Safety" profile.   <sup>2</sup> For S7-300/400 F-CPUs only   <sup>3</sup> For S7-1200/1500 F-CPUs only |  |  |  |

#### Accessing tags of the F-I/O DB

##### Rule for accessing tags of the F-I/O DB

Tags of the F‑I/O DB of an F‑I/O can only be accessed from the F‑runtime group from which the channels of this F‑I/O are accessed (if access is made).

##### "Fully qualified DB access"

You can access the tags of the F‑I/O DB via a "fully qualified DB access" (that is, by specifying the name of the F‑I/O DB and by specifying the name of the tag).

##### Example of evaluating the QBAD tag

![Example of evaluating the QBAD tag](images/93483273483_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[F‑I/O DB](#f-io-db-1)

### Passivation and reintegration of F-I/O

This section contains information on the following topics:

- [Passivation and reintegration of F-I/O](#passivation-and-reintegration-of-f-io-1)
- [After startup of F-system](#after-startup-of-f-system)
- [After communication errors](#after-communication-errors)
- [After F-I/O or channel faults](#after-f-io-or-channel-faults)
- [Group passivation](#group-passivation)

#### Passivation and reintegration of F-I/O

##### Overview

In the following you can find information on passivation and reintegration of F-I/O.

##### Signal sequence charts

The signal sequences presented below represent typical signal sequences for the indicated behavior.

Actual signal sequences and, in particular, the relative position of the status change of individual signals can deviate from the given signal sequences within the scope of known "fuzzy" cyclic program execution factors, depending on the following:

- The F-I/O used
- The F-CPU used
- The cycle time of the (F-)OB in which the associated F-runtime group is called
- The target rotation time of the PROFIBUS DP or the update time of the PROFINET IO

> **Note**
>
> The signal sequences shown refer to the status of signals in the user's safety program.

#### After startup of F-system

##### Behavior after a startup

| Fail-safe value output after startup of the F-system | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O without profile  "RIOforFA-Safety" with S7-1200/1500 F-CPU | Every F-I/O with S7-300/400 F-CPU |
| --- | --- | --- | --- |
| Passivation of the entire F-I/O occurs during startup. | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| * Value status or QBAD_I_xx and QBAD_O_xx are not available for fail-safe GSD based DP slaves and fail-safe GSD based I/O devices without the "RIOforFA-Safety" profile. |  |  |  |

##### Reintegration of F-I/O

**Reintegration** of the F‑I/O, i.e. the provision of process values in the PII or the output of process values provided in the PIQ at the fail-safe outputs, takes place **automatically**, regardless of the setting at the ACK_NEC tag or the configuration "Channel failure acknowledge", no sooner than the second cycle of the F-runtime group after F-system startup.

You can find more information on pending F-communication, F-I/O or channel errors during startup of the F-system in the sections [After communication errors](#after-communication-errors) and [After F-I/O or channel faults](#after-f-io-or-channel-faults).

For fail-safe GSD based DP slaves/GSD based I/O devices with "RIOforFA-Safety" profile, consult the respective documentation for the fail-safe GSD based DP slave/GSD based I/O device.

Depending on the F-I/O you are using and the cycle time of the F-runtime group and PROFIBUS DP/PROFINET IO, several cycles of the F-runtime group can elapse before reintegration occurs.

If communication between the F-CPU and F-I/O takes longer to establish than the F-monitoring time set in the properties for the F-I/O, automatic reintegration does not take place.

##### Signal sequence for passivation and reintegration of F-I/O after F-system startup

Example for an F‑I/O with inputs:

![Signal sequence for passivation and reintegration of F-I/O after F-system startup](images/166664531467_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Startup of F-system/passivation |
| ② | Automatic reintegration (e.g. third cycle) |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unintentional restart**  In contrast to the standard user program, when the safety program starts up, all tags of the F-DBs are generally initialized with their start values. This means that saved error information is lost. The F-system performs automatic reintegration of the F‑I/O.  If an unintentional startup of your process is not allowed, you must program restart/startup protection in the safety program. For this, the output of process values must be blocked until user acknowledgment takes place (see "[Implementation of user acknowledgment](#implementation-of-user-acknowledgment)"). This user acknowledgment must not take place until safe output of process values is possible (see "[Programming startup protection](#programming-startup-protection)").  You must expect an unintentional restart in the following cases:  - After a STOP generated by PG/PC operation, mode switch, communication function or "STP" instruction - After an operating error - After a STOP caused by a fault reaction function    (S008) |  |

#### After communication errors

##### Behavior after communication errors

| Fail-safe value output after communication errors | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O without profile  "RIOforFA-Safety" with S7-1200/1500 F-CPU | Every F-I/O with S7-300/400 F-CPU |
| --- | --- | --- | --- |
| If a communication error between the F-CPU and the F-I/O is detected, all channels of the entire F-I/O are passivated. | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| * Value status or QBAD_I_xx and QBAD_O_xx are not available for fail-safe GSD based DP slaves and fail-safe GSD based I/O devices without the "RIOforFA-Safety" profile. |  |  |  |

##### Reintegration of F-I/O

**Reintegration** of the relevant F‑I/O, that is, provision of process values in the PII or output of process data provided in the PIQ at the fail-safe outputs, takes place only when the following occurs:

- All communication errors have been eliminated and the F-system has set tag ACK_REQ = 1
- A **user acknowledgment** with a positive edge has occurred:

  - At the ACK_REI tag of the [F-I/O DB](#ack_rei) or
  - At the ACK_REI_GLOB input of the "ACK_GL" instruction ([ACK_GL: Global acknowledgment of all F-I/O in an F-runtime group (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#ack_gl-global-acknowledgment-of-all-f-io-in-an-f-runtime-group-step-7-safety-v19))

##### Signal sequence for passivation and reintegration of F-I/O after communication errors

Example for an F‑I/O with inputs:

![Signal sequence for passivation and reintegration of F-I/O after communication errors](images/89559199371_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Communication error/passivation |
| ② | All communication errors have been eliminated |
| ③ | Reintegration |

---

**See also**

[Implementing User Acknowledgment in the Safety Program of the F-CPU of a DP Master or IO controller](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-dp-master-or-io-controller)
  
[Implementing user acknowledgment in the safety program of the F-CPU of a I-slave or I-device](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-i-slave-or-i-device)

#### After F-I/O or channel faults

##### Behavior after F-I/O faults

| Fail-safe value output after F-I/O faults | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O without profile  "RIOforFA-Safety" with S7-1200/1500 F-CPU | Every F-I/O with S7-300/400 F-CPU |
| --- | --- | --- | --- |
| If an F-I/O fault is detected by the F-system, passivation of all channels of the entire F-I/O occurs. | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| * Value status or QBAD_I_xx and QBAD_O_xx are not available for fail-safe GSD based DP slaves and fail-safe GSD based I/O devices without the "RIOforFA-Safety" profile. |  |  |  |

##### Behavior after channel fault

| Fail-safe value output after channel faults | F-I/O with "RIOforFA-Safety" profile with S7-1200/1500 F-CPU | F-I/O without profile  "RIOforFA-Safety" with S7-1200/1500 F-CPU | Every F-I/O with S7-300/400 F-CPU |
| --- | --- | --- | --- |
| When passivation for **complete** F-I/O is configured:  If a channel fault is detected by the F-system, passivation of all channels of the entire F-I/O occurs. | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  Value status = 0* |  | QBAD and PASS_OUT = 1  For **all** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| With configuration of **channel-granular** passivation:  If a channel fault is detected by the F-system, passivation of all the affected channels of the entire F-I/O occurs. | QBAD and PASS_OUT **unchanged**  For the **affected** channels:  Channel value = fail-safe value (0)  Value status = 0 | QBAD and PASS_OUT = 1  For the **affected** channels:  Channel value = fail-safe value (0)  Value status = 0* | QBAD and PASS_OUT = 1  For the **affected** channels:  Channel value = fail-safe value (0)  QBAD_I_xx and QBAD_O_xx = 1* |
| * Value status or QBAD_I_xx and QBAD_O_xx are not available for fail-safe GSD based DP slaves and fail-safe GSD based I/O devices without the "RIOforFA-Safety" profile. |  |  |  |

##### Reintegration of F-I/O

**Reintegration** of the relevant F‑I/O or the relevant channels of the F‑I/O, that is, provision of process data in the PII or output of process data provided in the PIQ at the failsafe outputs, takes place only when the following occurs:

- All F-I/O or channel faults have been eliminated.

If you have configured channel-granular passivation for the F-I/O, the relevant channels are reintegrated once the fault is corrected; any faulty channels remain passivated.

Reintegration is performed depending on your setting for the ACK_NEC tag or the "Channel failure acknowledge" parameter (configuration of the S7-1500/ET 200MP F-module and S7-1200 F-module)

- With ACK_NEC = 0 or the configuration "Channel failure acknowledge = automatic", **automatic reintegration** is performed as soon as the F-system detects that the fault has been corrected. For F-I/O with inputs, reintegration takes place right away. For F-I/O with outputs or F-I/O with inputs and outputs, depending on the F-I/O you are using, reintegration can take several minutes, first after the necessary test signals have been applied, which are used by the F-I/O to determine that the fault has been eliminated.
- With ACK_NEC = 1 or the configuration "Channel failure acknowledge = manual", reintegration is performed only as a result of user acknowledgment with a positive edge at the ACK_REI tag of the F‑I/O DB or at the ACK_REI_GLOB input of the "ACK_GL" instruction. Acknowledgment can be made as soon as the F-system detects that the fault has been eliminated and tag ACK_REQ = 1 has been set.

  For fail-safe GSD based I/O devices with "RIOforFA-Safety" profile, consult the respective documentation for the fail-safe GSD based I/O device .

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | Following a supply voltage failure of the F-I/O lasting less than the F-monitoring time assigned for the F-I/O, automatic reintegration can occur regardless of the setting for the ACK_NEC tag or the "Channel failure acknowledge" configuration.  If automatic reintegration is not permitted for the relevant process in this case, you must program startup protection by evaluating tags QBAD or QBAD_I_xx and QBAD_O_xx or value status or PASS_OUT.  In the event of a supply voltage failure of the F‑I/O lasting longer than the specified F‑monitoring time for the F‑I/O, the F‑system detects a communication error. (S012) |  |

##### Signal sequence for passivation and reintegration of F‑I/O after F‑I/O faults or channel faults when ACK_NEC = 0 or configuration "Channel failure acknowledge = automatic" (for passivation of entire F‑I/O after channel faults)

Example for an F-I/O with inputs:

![Signal sequence for passivation and reintegration of F‑I/O after F‑I/O faults or channel faults when ACK_NEC  = 0 or configuration "Channel failure acknowledge = automatic" (for passivation of entire F‑I/O after channel faults)](images/166665518475_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | F-I/O or channel faults  Passivation |
| ② | F-I/O or channel faults corrected  Automatic reintegration |

##### Signal sequence for passivation and reintegration of F‑I/O after F‑I/O faults or channel faults when ACK_NEC = 1 or configuration "Channel failure acknowledge = manual" (for passivation of entire F‑I/O after channel faults)

For the signal sequence for passivation and reintegration of F‑I/O after F‑I/O or channel faults when ACK_NEC = 1 or configuration "Channel failure acknowledge = manual" (initial value), see [After communication errors](#after-communication-errors).

##### Signal sequence for passivation and reintegration of F‑I/O after channel faults when ACK_NEC = 1 or configuration "Channel failure acknowledge = manual" (for channel-granular passivation)

Example for an F-I/O with inputs:

![Signal sequence for passivation and reintegration of F‑I/O after channel faults when ACK_NEC = 1 or configuration "Channel failure acknowledge = manual" (for channel-granular passivation)](images/166666060811_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| ① | Channel fault for channel 0/passivation of channel 0 | ④ | Reintegration of channel 0 |
| ② | Channel fault for channel 1/passivation of channel 1 | ⑤ | Channel fault eliminated for channel 1 |
| ③ | Channel fault eliminated for channel 0 | ⑥ | Reintegration of channel 1 |

#### Group passivation

##### Programming a group passivation

If you want to enable passivation of additional F‑I/O when an F‑I/O or a channel of an F‑I/O is passivated by the F‑system, you can use the PASS_OUT/PASS_ON tags to perform **group passivation** of the associated F‑I/O.

Group passivation by means of PASS_OUT/PASS_ON can, for example, be used to force simultaneous reintegration of all F‑I/O after startup of the F‑system.

For group passivation, you must OR all PASS_OUT tags of the F‑I/O in the group and assign the result to all PASS_ON tags of the F‑I/O in the group.

During use of fail-safe values (0) due to group passivation by means of PASS_ON = 1, the QBAD tag of the F‑I/O of this group = 1.

> **Note**
>
> Note the different behavior of PASS_OUT for F-I/O with/without "RIOforFA-Safety" profile (see table in section [QBAD/PASS_OUT/DISABLED/QBAD_I_xx/QBAD_O_xx and value status](#qbadpass_outdisabledqbad_i_xxqbad_o_xx-and-value-status)).

##### Example of group passivation

![Example of group passivation](images/93483643531_DV_resource.Stream@PNG-de-DE.png)

##### Reintegration of F-I/O

**Reintegration** of F-I/O passivated by group passivation occurs **automatically**, if a reintegration (**automatic** or **through user acknowledgment**) occurs for the F-I/O that triggered the group passivation (PASS_OUT = 0).

##### Signal sequence for group passivation following communication error

Example for two F‑I/O with inputs:

![Signal sequence for group passivation following communication error](images/89560239115_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Communication error in F-I/O A  Passivation of F-I/O A |
| ② | Passivation of F-I/O B |
| ③ | Communication error in F-I/O A corrected and acknowledged |
| ④ | Reintegration F-I/O A and B |

## Implementation of user acknowledgment

This section contains information on the following topics:

- [Implementing User Acknowledgment in the Safety Program of the F-CPU of a DP Master or IO controller](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-dp-master-or-io-controller)
- [Implementing user acknowledgment in the safety program of the F-CPU of a I-slave or I-device](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-i-slave-or-i-device)

### Implementing User Acknowledgment in the Safety Program of the F-CPU of a DP Master or IO controller

#### Options for user acknowledgment

Depending on the result of the risk analysis, you have the following options for implementing a user acknowledgment:

- With an acknowledgment key that you connect to an F-I/O with inputs.
- With an operator control and monitoring system.
- With an acknowledgment key that you connect to a standard I/O with inputs.
- By other mechanisms for reading in the user acknowledgment.

#### User acknowledgment by means of acknowledgment key

> **Note**
>
> When you implement user acknowledgment by means of acknowledgment key, and a communication error, an F-I/O fault, or a channel fault occurs in the F-I/O to which the acknowledgment key is connected, then it will not be possible to acknowledge the reintegration of this F-I/O.
>
> This "blocking" can only be removed by a STOP-to-RUN transition of the F-CPU. In a redundant S7-1500HF system, you must set both HF CPUs or the redundant S7-1500HF system to STOP before you restart the HF CPUs.
>
> Consequently, it is recommended that you also provide for an acknowledgment by means of an operator control and monitoring system, in order to acknowledge reintegration of an F-I/O to which an acknowledgment key is connected.
>
> A user acknowledgment may be issued using an acknowledgment key connected to a standard I/O with inputs or other mechanisms for reading the user acknowledgment if the risk analysis allows this.

#### User acknowledgment by means of an operator control and monitoring system

For implementation of a user acknowledgment by means of an operator control and monitoring system, the [ACK_OP: Fail-safe acknowledgment (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#ack_op-fail-safe-acknowledgment-step-7-safety-v19) instruction is required.

#### Procedure for programming user acknowledgment by means of an operator control and monitoring system (S7-300, S7-400)

1. Select the "ACK_OP" instruction in the "Instructions" task card and place it in your safety program. The acknowledgment signal for evaluating user acknowledgments is provided at output OUT of ACK_OP.
2. On your operator control and monitoring system, set up a field for manual entry of an "acknowledgment value" of "6" (1st step in acknowledgment) and an "acknowledgment value" of "9" (2nd step in acknowledgment).

   or

   Assign function key 1 to transfer an "acknowledgment value" of "6" (1st step in acknowledgment) once, and function key 2 to transfer an "acknowledgment value" of "9" (2nd step in acknowledgment) once. You need to assign the in/out IN (in the data area of the ACK_OP instruction) to the field or the function keys.
3. Optional: In your operator control and monitoring system, evaluate output Q in the instance DB of ACK_OP to show the time frame within which the 2nd step in acknowledgment must occur or to indicate that the 1st step in acknowledgment has already occurred.

If you want to perform a user acknowledgment exclusively from a programming device or PC using the watch table (monitor/modify tag) without having to disable safety mode, then you must transfer an operand (memory word or DBW of a DB of the standard user program) at in/out IN when calling ACK_OP. You can then transfer "acknowledgment values" "6" and "9" on the programming device or PC by modifying the memory word or DBW of a DB once. The memory word or DBW of a DB must not be written by the program.

> **Note**
>
> If you connect the in/out IN to a memory word or DBW of a DB, you have use a separate memory word or DBW of a DB of the standard user program for each instance of the ACK_OP instruction at the in/out IN.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The two acknowledgment steps must **not** be triggered by one single operation, for example, by programming them including the time conditions and using one function key to trigger them.  The two separate acknowledgment steps also prevent an erroneous triggering of an acknowledgment, for example, by your non-fail-safe operator control and monitoring system. (S013) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you have operator control and monitoring systems and F‑CPUs that are interconnected and use the ACK_OP instruction for fail-safe acknowledgment, you need to ensure that the intended F‑CPU will be addressed **before** you perform the two acknowledgment steps.  - Store a network-wide* unique name for the F-CPU in a DB of your standard user program in each F-CPU. - In your operator control and monitoring system, set up a text box from which you can read out the F‑CPU name from the DB online before executing the two acknowledgment steps. - Optional:    In your operator control and monitoring system, set up a text box to permanently store the F‑CPU name. Then, you can determine whether the intended F-CPU is being addressed by simply comparing the F-CPU name read out online with the permanently stored name. (S014) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet.

> **Note**
>
> The configuration of your operator control and monitoring system does not have any effect on the Collective F-Signature.

#### Procedure for programming user acknowledgment by means of an operator control and monitoring system (S7-1200, S7-1500)

1. Select the "ACK_OP" instruction in the "Instructions" task card and place it in your safety program. The acknowledgment signal for evaluating user acknowledgments is provided at output OUT of ACK_OP.
2. Assign the ACK_ID input an identifier between 9 and 30000 for the acknowledgment.
3. Assign the in/out IN a memory word or DBW of a DB of the standard user program.
4. On your operator control and monitoring system, set up a field for manual entry of an "acknowledgment value" of "6" (1st step in acknowledgment) and the "Identifier" configured at the ACK_ID input (2nd step in acknowledgment).

   or

   Allocate a function key 1 for a one-time transfer of the "acknowledgment value" of "6" (1st step in acknowledgment) and a function key 2 for a one-time transfer of the "Identifier" set at the ACK_ID input (2nd step in acknowledgment).  
   You need to assign memory word or the DBW of the DB of the standard user program assigned to the in/out IN to the field or the function keys.
5. Optional: In your operator control and monitoring system, evaluate output Q in the instance DB of ACK_OP to show the time frame within which the 2nd step in acknowledgment must occur or to indicate that the 1st step in acknowledgment has already occurred.

**Note**

You need to provide the in/out parameter IN with a separate memory word or DBW of a DB of the standard user program for each instance of the ACK_OP instruction.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The two acknowledgment steps must not be triggered by one single operation, for example, by programming them including the time conditions and using one function key to trigger them.  The two separate acknowledgment steps also prevent an erroneous triggering of an acknowledgment, for example, by your non-fail-safe operator control and monitoring system. (S013) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you have operator control and monitoring systems and F‑CPUs that are interconnected and use the ACK_OP instruction for fail-safe acknowledgment, you need to ensure that the intended F‑CPU will be addressed **before** you perform the two acknowledgment steps.  Alternative 1:  - The value for each identifier of the acknowledgment (ACK_ID input; data type: INT) can be freely selected in the range from 9 to 30000, but must be unique network-wide* for all instances of the ACK_OP instruction. You must supply the ACK_ID input with constant values when calling the instruction. Direct read or write access to the ACK_ID tag in the associated instance DB is not permitted!   Alternative 2:  - Store a network-wide* unique name for the F-CPU in a DB of your standard user program in each F-CPU. - In your operator control and monitoring system, set up a text box from which you can read out the F‑CPU name from the DB online before executing the two acknowledgment steps. - Optional:    In your operator control and monitoring system, set up a text box to permanently store the F‑CPU name. Then, you can determine whether the intended F‑CPU is being addressed by simply comparing the F‑CPU name read out online with the permanently stored designation. (S047) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet.

> **Note**
>
> The supply of the IN input/output of the ACK_OP instruction as well as the configuration of your operator control and monitoring system do not have any effect on the Collective F-Signature, the Collective F-SW-Signature or the signature of the block that calls the ACK_OP instruction.
>
> Changes to the supply of the IN input/output or to the configuration of your operator control and monitoring system therefore do not result in a changed Collective F-Signature/Collective F-SW-Signature/signature of the calling block.

#### Example of procedure for programming a user acknowledgment for reintegrating an F-I/O

| Symbol | Meaning |
| --- | --- |
| 1. Optional: set the ACK_NEC tag in the respective [F-I/O DB](#ack_nec) to "0" if automatic reintegration (without user acknowledgment) is to take place after an F-I/O fault or a channel fault.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The parameter assignment of the ACK_NEC tag of the F-I/O DB with the value "0" is only allowed if automatic reintegration is permitted for the relevant process from a safety standpoint. (S010) |  | 2. Optional: Evaluate the QBAD or QBAD_I_xx/QBAD_O_xx (S7-300, S7-400) tags or value status (S7-1200, S7-1500) or DIAG in the respective F‑I/O DB to trigger an indicator light in the event of an error, and/or generate error messages on the operator control and monitoring system in your standard user program by evaluating the above tags or the value status. These messages can be evaluated before performing the acknowledgment operation. Alternatively, you can evaluate the diagnostic buffer of the F-CPU. 3. Optional: Evaluate the ACK_REQ tag in the respective F‑I/O DB, for example, in the standard user program or on the operator control and monitoring system, to query or to indicate whether user acknowledgment is required. 4. Assign the input of the acknowledgment key or the OUT output of the ACK_OP instruction to the ACK_REI tag in the respective F-I/O DB or the ACK_REI_GLOB input of the ACK_GL instruction (see above). |  |

### Implementing user acknowledgment in the safety program of the F-CPU of a I-slave or I-device

#### Options for user acknowledgment

You can implement a user acknowledgment by means of:

- An HMI system that you can use to access the F‑CPU of the I‑slave/I-Device
- An acknowledgment key that you connect to an F‑I/O with inputs that is assigned to the F‑CPU of the I‑slave/I-Device
- An acknowledgment key that you connect to an F‑I/O with inputs that is assigned to the F‑CPU of the DP master/IO controller

These three options are illustrated in the figure below.

![Options for user acknowledgment](images/86292829067_DV_resource.Stream@PNG-en-US.png)

#### 1. User acknowledgment by means of an HMI system with which you can access the F‑CPU of the I‑slave/I‑device

The [ACK_OP: Fail-safe acknowledgment (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#ack_op-fail-safe-acknowledgment-step-7-safety-v19) instruction is required to implement user acknowledgment with an HMI system that you can use to access the F‑CPU of the I‑slave/I-device.

**Programming procedure**

Follow the procedure described in "[Implementing User Acknowledgment in the Safety Program of the F-CPU of a DP Master or IO controller](#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-dp-master-or-io-controller)" under "Programming procedure ...".

From your HMI system, you can then directly access the instance DB of ACK_OP in the I‑slave/I‑Device.

#### 2. User acknowledgment by means of an acknowledgment key at an F‑I/O with inputs that are assigned to the F‑CPU of the I‑slave/I‑device

> **Note**
>
> In the event of a communication error, F-I/O fault, or channel fault in the F‑I/O to which the acknowledgment key is connected, an acknowledgment for reintegration of this F‑I/O is no longer possible.
>
> This "blocking" can only be removed by a STOP-to-RUN transition of the F‑CPU of the I‑slave/I-Device.
>
> Consequently, it is recommended that you also provide for an acknowledgment by means of an HMI system that you can use to access the F-CPU of the I‑slave/I-device, in order to acknowledge reintegration of an F-I/O to which an acknowledgment key is connected (see 1).

#### 3. User acknowledgment by means of an acknowledgment key at an F‑I/O with inputs that are assigned to the F‑CPU of the DP master/IO controller

If you want to use the acknowledgment key that is assigned to the F‑CPU at the DP master/IO controller to perform user acknowledgment in the safety program of the F‑CPU of an I‑slave/I-device as well, you must transmit the acknowledgment signal from the safety program in the F‑CPU of the DP master/IO controller to the safety program in the F‑CPU of the I‑slave/I-device using safety‑related master-I‑slave/IO controller-I-device communication.

**Programming procedure**

1. Place the [SENDDP](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) instruction in the safety program in the F‑CPU of the DP master/IO controller.
2. Place the [RCVDP](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) instruction in the safety program in the F‑CPU of the I-slave/I-Device.
3. Supply an input SD_BO_xx of SENDDP with the input of the acknowledgment key.
4. The acknowledgment signal for evaluating user acknowledgments is now available at the corresponding RD_BO_xx output of RCVDP.

   The acknowledgment signal can now be read in the program sections in which further processing is to take place with fully qualified access directly in the associated instance DB (for example, "RCVDP_DB".RD_BO_02).
5. Supply the corresponding input SUBBO_xx of RCVDP with FALSE (fail-safe value 0) to ensure that user acknowledgment is not accidentally triggered before communication is established for the first time after startup of the sending and receiving F‑systems, or in the event of a safety‑related communication error.

**Note**

If a communication error, an F‑I/O error, or a channel fault occurs at the F‑I/O to which the acknowledgment key is connected, then an acknowledgment for reintegration of this F‑I/O will no longer be possible.

This "blocking" can only be removed by a STOP-to-RUN transition of the F‑CPU of the DP master/IO controller.

Consequently, it is recommended that you also provide for an acknowledgment by means of an HMI system that you can use to access the F-CPU of the DP master/IO controller, in order to acknowledge reintegration of the F-I/O to which an acknowledgment key is connected.

If a safety‑related master-I‑slave/IO controller‑I‑Device communication error occurs, the acknowledgment signal cannot be transmitted, and an acknowledgment for reintegration of safety‑related communication is no longer possible.

This "blocking" can only be removed by a STOP-to-RUN transition of the F‑CPU of the I‑slave/I-Device.

Consequently, it is recommended that you also provide for an acknowledgment by means of an HMI system that you can use to access the F-CPU of the I-slave/I-Device, in order to acknowledge reintegration of the safety-related communication for transmission of the acknowledgment signal (see 1).

## Data exchange between standard user program and safety program

This section contains information on the following topics:

- [Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program-1)
- [Data Transfer from the Safety Program to the Standard User Program](#data-transfer-from-the-safety-program-to-the-standard-user-program)
- [Data Transfer from Standard User Program to Safety Program](#data-transfer-from-standard-user-program-to-safety-program)

### Data exchange between standard user program and safety program

You have the option of transferring data between the safety program and the standard user program. Tags can be transferred using DBs, F-DBs and bit memory:

|  | From the standard user program |  | From the safety program |  |
| --- | --- | --- | --- | --- |
| Read access | Write access | Read access | Write access |  |
| Tag from DB | Permitted | Permitted | A tag from the DB can be read-accessed or write-accessed |  |
| Tag from F-DB | Permitted | **Not permitted** | Permitted | Permitted |
| Bit memory | Permitted | Permitted | Bit memory can be read-accessed or write-accessed |  |

You can also access the process image of the standard I/O and F-I/O:

|  |  | From the standard user program |  | From the safety program |  |
| --- | --- | --- | --- | --- | --- |
| Read access | Write access | Read access | Write access |  |  |
| Process image of standard I/O | PII | Permitted | Permitted | Permitted | **Not permitted** |
| PIQ | Permitted | Permitted | **Not permitted** | Permitted |  |
| Process image of F‑I/O | PII | Permitted | **Not permitted** | Permitted | **Not permitted** |
| PIQ | Permitted | **Not permitted** | **Not permitted** | Permitted |  |

Note possible restrictions/particularities when using Software Units or a Safety Unit.

#### Decoupling of the safety program from the standard user program

For data exchange between standard user program and safety program, we recommend that you define special data blocks (transfer data blocks) in which the data to be exchanged is stored. This action allows you to decouple the blocks of the standard user program and the safety program. The changes in the standard user program do not affect the safety program (and vice versa) provided these data blocks are not modified.

### Data Transfer from the Safety Program to the Standard User Program

#### Reading data of the safety program in the standard user program

The standard user program can read all data of the safety program, for example using symbolic (fully qualified) accesses to the following:

- The instance DBs of the F-FBs ("Name of instance DB".Signal_x)
- F‑DBs (for example "Name of F_DB".Signal_1)
- The process image input and output of F‑I/O (for example "Emergency_Stop_Button_1" (I 5.0))

  > **Note**
  >
  > **For S7-300/400 F-CPUs**
  >
  > The process image input of F-I/O is updated not only at the start of the F-runtime group, but also by the standard operating system.
  >
  > To find the standard operating system update times, refer to the Help on STEP 7 under "Process image input and output". For F-CPUs that support process image partitions, also bear in mind the update times when process image partitions are used. For this reason, when the process image input of F-I/O is accessed in the standard user program, it is possible to obtain different values than in the safety program. The differing values can occur due to:
  >
  > - Different update times
  > - Use of fail-safe values in the safety program
  >
  > To obtain the same values in the standard user program as in the safety program, you must not access the process image input in the standard program until after execution of an F-runtime group. In this case, you can also evaluate the QBAD or QBAD_I_xx tag in the associated F-I/O DB in the standard user program, in order to find out whether the process image input is receiving fail-safe values (0) or process data. When using process image partitions, also make sure that the process image is not updated by the standard operating system or by the UPDAT_PI instruction between execution of an F-runtime group and evaluation of the process image input in the standard user program.

  > **Note**
  >
  > **For S7-1200/1500 F-CPUs**
  >
  > The process image input of F-I/O is updated prior to processing the main safety block.

During the data transfer from the safety program to the standard user program, the integrity of the safety program and the safety-related data is not checked (see also section "[Product Overview](#product-overview)").

#### Writing data from the safety program to the standard user program

You can also write safety program data directly in the safety program to the standard user program (see also the table of supported operand areas in: [Restrictions in the programming languages FBD/LAD](#restrictions-in-the-programming-languages-fbdlad)).

This is also true for non-fail-safe service information (e.g. outputs DIAG of the fail-safe instructions).

Note the table in section "[Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program-1)".

When writing to a tag of the ARRAY data type, the index can either be a constant or a tag.

### Data Transfer from Standard User Program to Safety Program

As a basic principle, only fail‑safe data or fail‑safe signals from F-I/O and other safety programs (in other F‑CPUs) can be processed in the safety program, as standard tags are unsafe.

If you have to process tags from the standard user program in the safety program, however, you can evaluate either bit memory from the standard user program, tags from a standard DB, or the process image input (PII) of standard I/O in the safety program (see table of supported operand areas in: [Restrictions in the programming languages FBD/LAD](#restrictions-in-the-programming-languages-fbdlad)).

Note the table in section "[Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program-1)".

When reading a tag of the ARRAY data type, the index must be a constant. Tags are not permitted as index.

Note that structural changes to standard data blocks which are used in the safety program lead to inconsistencies of the safety program and can therefore only be executed if access permission for the safety-related project data is available. In this case the Collective F-Signature is the same as the original again after compilation. To prevent this effect, use "transfer data blocks" between the standard user program and the safety program.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Because the values in these tags are not generated safely, you must program additional process‑specific plausibility checks in the safety program to ensure that no dangerous states can arise. If bit memory, a tag of a standard DB, or an input of standard I/O is used in both F‑runtime groups, you must perform the plausibility check separately in each F‑runtime group. (S015) |  |

To facilitate checks, all PLC tags from the standard user program that are evaluated in the safety program are printed out when [creating the safety summary.](#creating-a-safety-summary)

PLC tags from the standard user program that are evaluated in know-how-protected F-blocks are not included in the safety summary. The plausibility check must already be ensured by the creator of the know-how-protected F-blocks.

#### Examples: Programming plausibility checks

- Use [Comparison](STEP%207%20Safety%20V19%20instructions.md#comparator-operations) instructions to check whether tags from the standard user program exceed or fall below permitted high and low limits. You can then influence your safety function with the result of the comparison.
- Use the [---( S )---: Set output (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#s-----set-output-step-7-safety-v19), [---( R )---: Reset output (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#r-----reset-output-step-7-safety-v19) or [SR: Set/reset flip-flop (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#sr-setreset-flip-flop-step-7-safety-v19) instructions, for example, with tags from the standard user program to allow a motor to be switched off, but not switched on.
- For switch-on sequences, use the AND logic operation instruction, for example, to logically combine tags from the standard user program with switch-on conditions that you derive from fail-safe tags.

If you want to process tags from the standard user program in the safety program, bear in mind that there is not a sufficiently simple method of checking plausibility for all tags.

#### Reading tags from the standard user program that can change during the runtime of an F‑runtime group

If you want to read tags from the standard user program (bit memory, tags of a standard DB, or PII of standard I/O) in the safety program, and these tags can be changed - either by the standard user program or an operator control and monitoring system - during runtime of the F-runtime group in which they are read (for example because your standard user program is being processed by a higher-priority cyclic interrupt), you must use bit memory or tags of a standard DB for this purpose. We recommend using [standard FCs for preprocessing](#pre-postprocessing-s7-1200-s7-1500) for S7-1200/1500 F-CPUs.

(S7-300, S7-400) You must write the bit memory or tags of a standard DB with the tags from the standard user program immediately before calling the F‑runtime group.

You are then permitted to access only this bit memory or these tags of a standard DB in the safety program.

Also note that **clock memory** that you defined when configuring your F-CPU in the "Properties" tab can change during runtime of the F-runtime group, since clock memory runs asynchronously to the F-CPU cycle.

> **Note**
>
> The F-CPU can go to STOP if this is not observed. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

## Safety-related communication

This section contains information on the following topics:

- [Configuring and programming communication (S7-300, S7-400)](#configuring-and-programming-communication-s7-300-s7-400)
- [Configuring and programming communication (S7-1200, S7-1500)](#configuring-and-programming-communication-s7-1200-s7-1500)
- [Configuring and programming communication with Flexible F-Link (S7-1200, S7-1500)](#configuring-and-programming-communication-with-flexible-f-link-s7-1200-s7-1500)
- [Configuring and programming communication between S7-300/400 and S7-1200/1500 F-CPUs](#configuring-and-programming-communication-between-s7-300400-and-s7-12001500-f-cpus)
- [Configuring and programming communication in several projects](#configuring-and-programming-communication-in-several-projects)

### Configuring and programming communication (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of communication](#overview-of-communication)
- [Safety-related IO controller-IO controller communication](#safety-related-io-controller-io-controller-communication)
- [Safety-related master-master communication](#safety-related-master-master-communication)
- [Safety-related IO controller-I-device communication](#safety-related-io-controller-i-device-communication)
- [Safety-related master-I-slave communication](#safety-related-master-i-slave-communication)
- [Safety-related I-slave-I-slave communication](#safety-related-i-slave-i-slave-communication)
- [Safety-Related I-Slave-Slave Communication](#safety-related-i-slave-slave-communication)
- [Safety-related IO controller-I-slave communication](#safety-related-io-controller-i-slave-communication)
- [Safety-related communication via S7 connections](#safety-related-communication-via-s7-connections)
- [Safety-related communication with other S7 F-systems](#safety-related-communication-with-other-s7-f-systems)

#### Overview of communication

##### Introduction

This section gives an overview of the safety-related communication options in SIMATIC Safety F-systems.

##### Options for safety-related communication

| Safety-related communication | On subnet | Additional hardware required |
| --- | --- | --- |
| I-slave-slave communication | PROFIBUS DP | — |
| **Safety-related CPU-CPU communication:** |  |  |
| IO controller-IO controller communication | PROFINET IO | PN/PN coupler |
| Master‑master communication | PROFIBUS DP | DP/DP coupler |
| IO controller-I-device communication | PROFINET IO | — |
| Master-I-slave communication | PROFIBUS DP | — |
| I-slave-I-slave communication | PROFIBUS DP | — |
| IO controller-I-slave communication | PROFINET IO and PROFIBUS DP | IE/PB link |
| Safety-related communication via S7 connections | Industrial Ethernet | — |
| IO controller-IO controller communication for S7 Distributed Safety | PROFINET IO | PN/PN coupler |
| Master-master communication for S7 Distributed Safety | PROFIBUS DP | DP/DP coupler |
| Safety-related communication to S7 Distributed Safety or S7 F Systems via S7 connections | Industrial Ethernet | — |

##### Overview of safety-related communication via PROFIBUS DP

The figure below presents an overview of the 4 options for safety-related communication via PROFIBUS DP in SIMATIC Safety F‑systems with S7-300/400 F-CPUs.

![Overview of safety-related communication via PROFIBUS DP](images/166489783307_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Safety-related master-master communication |
| ② | Safety-related master-I-slave communication |
| ③ | Safety-related I-slave-I-slave communication |
| ④ | Safety-related I-slave-slave communication |

##### Overview of safety-related communication via PROFINET IO

The figure below presents an overview of the four options for safety-related communication via PROFINET IO in SIMATIC Safety F-systems with S7-300/400 F-CPUs. If an IE/PB‑link is used, safety-related communication is possible between assigned I‑slaves.

![Overview of safety-related communication via PROFINET IO](images/166664424587_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Safety-related IO controller-IO controller communication |
| ② | Safety-related IO controller-I-device communication |
| ③ | Safety-related IO controller-I-slave communication |
| ④ | Safety-related I-slave-I-slave communication integrating an IO controller |

##### Safety-related CPU-CPU communication via PROFIBUS DP or PROFINET IO

In safety-related CPU-CPU communication, a fixed amount of fail-safe data of the data type INT or BOOL is transmitted fail-safe between the safety programs in F-CPUs of DP masters/I-slaves or IO controllers/I-devices.

The data are transferred using the SENDDP instruction for sending and the RCVDP instruction for receiving. The data are stored in configured transfer areas of the devices. Each transfer area consists of one input and one output address area.

##### Safety-related I-slave-slave communication via PROFIBUS DP

Safety-related I‑slave-slave communication with F‑I/O is possible in a DP slave that supports safety-related I‑slave-slave communication, for example with all ET 200SP F-modules with IM 155-6 DP HF, firmware > V3.1, with all ET 200S F‑modules with IM 151-1 HF, with all fail-safe S7‑300 signal modules with IM 153‑2, as of article number 6ES7153‑2BA01‑0XB0, firmware > V4.0.0.

Safety-related communication between the safety program of the F-CPU of an I-slave and F-I/O of a DP slave takes place using direct data exchange, as in the standard program. The process image is used to access the channels of the F-I/O in the safety program of the F-CPU of the I-slave.

##### Safety-related CPU-CPU communication via Industrial Ethernet

Safety-related CPU-CPU communication via Industrial Ethernet is possible using S7 connections, both from and to the following:

- S7‑300 F‑CPUs via the integrated PROFINET interface
- S7‑400 F‑CPUs via the integrated PROFINET interface or a CP 443‑1 or CP 443‑1 Advanced‑IT

In safety-related communication via S7 connections, a specified amount of fail-safe data of data type BOOL, INT, WORD, DINT, DWORD, or TIME is transferred fail-safe between the safety programs of the F-CPUs linked by the S7 connection.

The data transfer makes use of the SENDS7 instruction for sending and the RCVS7 instruction for receiving. Data are exchanged using one F-DB ("F-communication DB") each at the sender and receiver ends.

##### Safety-related CPU-CPU communication with S7 Distributed Safety or S7 F-systems

Safety-related communication is possible from F-CPUs in SIMATIC Safety to F-CPUs in S7 Distributed Safety or S7 F-systems.

#### Safety-related IO controller-IO controller communication

This section contains information on the following topics:

- [Configure safety-related IO controller-IO controller communication](#configure-safety-related-io-controller-io-controller-communication)
- [Safety-related IO controller-IO controller communication via SENDDP and RCVDP](#safety-related-io-controller-io-controller-communication-via-senddp-and-rcvdp)
- [Program safety-related IO controller-IO controller communication](#program-safety-related-io-controller-io-controller-communication)
- [Safety-related IO controller-IO controller communication - Limits for data transfer](#safety-related-io-controller-io-controller-communication---limits-for-data-transfer)

##### Configure safety-related IO controller-IO controller communication

###### Introduction

Safety-related communication between safety programs of the F-CPUs of IO controllers takes place over a PN/PN coupler that you set up between the F-CPUs.

For 416F‑2 DP CPUs without an integrated PROFINET interface, use a CP 443‑1 or CP 443‑1 Advanced-IT.

> **Note**
>
> Deactivate the "Data validity display DIA" parameter in the properties for the PN/PN coupler in the hardware and network editor. This is the default setting. Otherwise, safety-related IO controller-IO controller communication is not possible.

###### Configuring transfer areas

You must configure one transfer area for output data and one transfer area for input data in the hardware and network editor for each safety-related communication connection between two F-CPUs in the PN/PN coupler. The figure below shows how both of the F-CPUs are able to send **and** receive data (bidirectional communication). One transfer area for output data and one transfer area for input data must be configured in the PN/PN coupler for each of the two communication connections.

![Configuring transfer areas](images/29583306123_DV_resource.Stream@PNG-en-US.png)

###### Rules for defining transfer areas

The transfer area for output data and the transfer area for input data for the **data to be sent** must begin with the same start address. A total of 12 bytes (consistent) is required for the transfer area for output data; 6 bytes (consistent) are required for the transfer area for input data.

The transfer area for input data and the transfer area for output data for the **data to be received** must begin with the same start address. A total of 12 bytes (consistent) is required for the transfer area for input data; 6 bytes (consistent) are required for the transfer area for output data.

###### Procedure for configuration

The procedure for configuring safety-related IO controller-IO controller communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Switch to the network view of the hardware and network editor.
3. Select a PN/PN Coupler X1 and a PN/PN Coupler X2 from "Other field devices\PROFINET IO\Gateway\Siemens AG\PN/PN Coupler" in the "Hardware catalog" task card and insert them into the network view of the hardware and network editor.
4. Connect the PN interface of the F-CPU 1 with the PN interface of the PN/PN Coupler X1 and the PN interface of the F-CPU 2 with the PN interface of PN/PN Coupler X2.

   ![Procedure for configuration](images/53118754443_DV_resource.Stream@PNG-en-US.png)
5. Switch to the device view of PN/PN Coupler X1 for bidirectional communication connections i.e. where each F‑CPU is both to send and to receive data. Select the following modules from "IN/OUT" in the "Hardware catalog" task card (with filter activated), and insert them in the "Device overview" tab:

   - One "IN/OUT 6 bytes / 12 bytes" module and
   - One "IN/OUT 12 bytes / 6 bytes" module
6. In the properties of the modules, assign the addresses outside the process image as follows:

   For the "IN/OUT 6 bytes / 12 bytes" module for sending data for example:

   - Input addresses: Start address 518
   - Output addresses: Start address 518

   For the "IN/OUT 12 bytes / 6 bytes" module for receiving data for example:

   - Input addresses: Start address 530
   - Output addresses: Start address 530
   > **Note**
   >
   > Make sure that you assign identical start addresses for the address areas of the output and input data.
   >
   > **Tip:** Make a note of the start addresses of the transfer areas. You need these to program the SENDDP and RCVDP blocks (LADDR input).

   ![Procedure for configuration](images/53119046411_DV_resource.Stream@PNG-en-US.png)
7. Select the following modules from "IN/OUT" in the device view of PN/PN coupler X2 and insert them in the "Device overview" tab:

   - One "IN/OUT 12 bytes / 6 bytes" module and
   - One "IN/OUT 6 bytes / 12 bytes" module
8. In the properties of the modules, assign the addresses outside the process image as follows:

   For the "IN/OUT 12 bytes / 6 bytes" module for receiving data for example:

   - Input addresses: Start address 516
   - Output addresses: Start address 516

   For the "IN/OUT 6 bytes / 12 bytes" module for sending data for example:

   - Input addresses: Start address 528
   - Output addresses: Start address 528

   ![Procedure for configuration](images/53143567371_DV_resource.Stream@PNG-en-US.png)

##### Safety-related IO controller-IO controller communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/22236741387_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F-CPUs of the IO controllers uses the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type INT or BOOL.

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Program safety-related IO controller-IO controller communication

###### Requirement for programming

The transfer areas for input and output data for the PN/PN coupler must be configured.

###### Programming procedure

You program safety-related IO controller-IO controller communication as follows:

| Symbol | Meaning |
| --- | --- |
| 1. In the safety program from which data is to be sent, call the [SENDDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for sending at the end of the main safety block. 2. In the safety program in which data is to be received, call the [RCVDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for receiving at the start of the main safety block. 3. Assign the start addresses of the output and input data transfer areas of the PN/PN coupler configured in the hardware and network editor to the respective LADDR inputs.    You must carry out this assignment for every communication connection for each of the F-CPUs involved. 4. Assign the value for the respective F-communication ID to the DP_DP_ID inputs. This establishes the communication relationship between the SENDDP instruction in one F-CPU and the RCVDP instruction in the other F-CPU: The associated instructions receive the same value for DP_DP_ID.    The figure below contains an example of how to specify the F-communication IDs at the inputs of the SENDDP and RCVDP instructions for 5 safety-related IO controller-IO controller communication relationships.               ![Programming procedure](images/166650545931_DV_resource.Stream@PNG-en-US.png)         ![Programming procedure](images/166650545931_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected; however, it must be unique network-wide* and CPU-wide at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program. You must supply constant values to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |     * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3). 5. Supply the SD_BO_xx and SD_I_xx inputs of SENDDP with the send signals. To cut down on intermediate signals when transferring block parameters, you can write the value directly to the instance DB of SENDDP using fully qualified access (for example, "Name SENDDP_1".SD_BO_02) before calling SENDDP. 6. Supply the RD_BO_xx and RD_I_xx outputs of RCVDP with the signals that you want to process further in other program sections or use fully qualified access to read the received signals directly in the associated instance DB in the program sections to be processed further (e.g., "Name RCVDP_1".RD_BO_02). 7. Supply the SUBBO_xx and SUBI_xx inputs of RCVDP with the fail-safe values that are to be output by RCVDP in place of the process data until communication is established for the first time after startup of the sending and receiving F-systems or in the event of an error in safety-related communication.    - Specification of constant fail-safe values:      For data of data type INT, you can enter constant fail-safe values directly as constants in the SUBI_xx input (initial value = "0"). If you want to specify a constant fail-safe value "TRUE" for data of the data type BOOL, provide the tag "F_GOBDB".VKE1 for the SUBBO_xx input (initial value = "FALSE").    - Specification of variable substitute values:      If you want to specify variable substitute values, define a tag that you calculate through your safety program in an F‑DB and specify this tag (fully qualified) in the SUBI_xx or SUBBO_xx input.        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | Note: The program logic for calculating variable substitute values can only be inserted after the RCVDP calls, because there must be no program logic before the RCVDP calls. This is why the initial values of the substitute values are active in all RCVDP instructions in the first cycle after a startup of the F-system. You must therefore assign appropriate initial values for these tags. (S017) |  | 8. Configure the TIMEOUT inputs of the RCVDP and SENDDP instructions with the required monitoring time.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |     Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times). 9. Optional: Evaluate the ACK_REQ output of the RCVDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether user acknowledgment is required. 10. Supply the ACK_REI input of the RCVDP instruction with the acknowledgment signal for reintegration. 11. Optional: Evaluate the SUBS_ON output of the RCVDP or SENDDP instruction in order to query whether the RCVDP instruction is outputting the fail-safe values assigned in the SUBBO_xx and SUBI_xx inputs. 12. Optional: Evaluate the ERROR output of the RCVDP or SENDDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether a communication error has occurred. 13. Optional: Evaluate the SENDMODE output of the RCVDP instruction in order to query whether the F-CPU with the associated SENDDP instruction is in [disabled safety mode](#disabling-safety-mode-1). |  |

##### Safety-related IO controller-IO controller communication - Limits for data transfer

> **Note**
>
> If the data quantities to be transmitted exceed the capacity of the SENDDP / RCVDP correlated instructions, a second (or third) SENDDP / RCVDP call can be used. This requires configuration of an additional communication connection via the PN/PN coupler. Whether or not this is possible with one single PN/PN coupler depends on the capacity restrictions of the PN/PN coupler.

#### Safety-related master-master communication

This section contains information on the following topics:

- [Configure safety-related master-master communication](#configure-safety-related-master-master-communication)
- [Safety-related master-master communication via SENDDP and RCVDP](#safety-related-master-master-communication-via-senddp-and-rcvdp)
- [Program safety-related master-master communication](#program-safety-related-master-master-communication)
- [Safety‑related master‑master communication:Limits for data transfer](#safety-related-master-master-communicationlimits-for-data-transfer)

##### Configure safety-related master-master communication

###### Introduction

Safety-related communication between safety programs of the F-CPUs of DP masters takes place via a DP/DP coupler.

> **Note**
>
> Switch the data validity indicator "DIA" on the DIP switch of the DP/DP coupler to "OFF". Otherwise, safety-related CPU-CPU communication is not possible.

###### Configuring transfer areas

You must configure one transfer area for output data and one transfer area for input data in the hardware and network editor for each safety-related communication connection between two F-CPUs in the DP/DP coupler. The figure below shows how both of the F-CPUs are able to send and receive data (bidirectional communication). One transfer area for output data and one transfer area for input data must be configured in the DP/DP coupler for each of the two communication connections.

![Configuring transfer areas](images/96163314443_DV_resource.Stream@PNG-en-US.png)

###### Rules for defining transfer areas

The transfer area for input data and the transfer area for output data for the **data to be sent** must begin with the same start address. A total of 6 bytes (consistent) is required for the transfer area for input data; 12 bytes (consistent) are required for the transfer area for output data.

The transfer area for input data and the transfer area for output data for the **data to be received** must begin with the same start address. A total of 12 bytes (consistent) is required for the transfer area for input data; 6 bytes (consistent) are required for the transfer area for output data.

###### Procedure for configuration

The procedure for configuring safety-related master-master communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Switch to the network view of the hardware and network editor.
3. Select a DP/DP coupler from "Other field devices\PROFIBUS DP\Gateways\Siemens AG\DP/DP Coupler" in the "Hardware catalog" task card and insert it into the network view of the hardware and network editor.
4. Insert a second DP/DP coupler.
5. Connect a DP interface of F-CPU 1 to the DP interface of a DP/DP coupler and a DP interface of F-CPU 2 to the DP interface of the other DP/DP coupler.

   ![Procedure for configuration](images/53117351307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/53117351307_DV_resource.Stream@PNG-en-US.png)
6. A free PROFIBUS address is assigned automatically in the properties of the DP/DP-coupler in the device view. You must set this address on the DP/DP coupler of PLC 1, either by using the DIP switch on the device or in the configuration of the DP/DP coupler (see [DP/DP Coupler](http://support.automation.siemens.com/WW/view/en/1179382) manual).
7. Switch to the device view of the DP/DP coupler for PLC1 for bidirectional communication connections i.e. where each F-CPU is both to send and to receive data. Select the following modules from the "Hardware catalog" task card (with filter activated), and insert them in the "Device overview" tab:

   - One "6 bytes I/12 bytes Q consistent" module, and
   - One "12 bytes I/6 bytes Q consistent" module
8. In the properties of the modules, assign the addresses outside the process image as follows:

   For "6 bytes I/12 bytes Q consistent" module for sending data for example:

   - Input addresses: Start address 530
   - Output addresses: Start address 530

   For "12 bytes I/6 bytes Q consistent" module for receiving data for example:

   - Input addresses: Start address 542
   - Output addresses: Start address 542

   ![Procedure for configuration](images/53143557003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/53143557003_DV_resource.Stream@PNG-en-US.png)
9. Select the following modules from the "Hardware catalog" task card (with filter activated) in the device view of DP/DP coupler PLC2, and insert them in the "Device overview" tab:

   - One "12 bytes I/6 bytes Q consistent" module, and
   - One "6 bytes I/12 bytes Q consistent" module
10. In the properties of the modules, assign the addresses outside the process image as follows:

    For "12 bytes I/6 bytes Q consistent" module for receiving data for example:

    - Input addresses: Start address 548
    - Output addresses: Start address 548

    For "6 bytes I/12 bytes Q consistent" module for sending data for example:

    - Input addresses: Start address 560
    - Output addresses: Start address 560

    ![Procedure for configuration](images/53143897611_DV_resource.Stream@PNG-en-US.png)

    ![Procedure for configuration](images/53143897611_DV_resource.Stream@PNG-en-US.png)

**Note**

Make sure that you assign identical start addresses for the address areas of the output and input data.

**Tip:** Make a note of the start addresses of the transfer areas. You need these to program the SENDDP and RCVDP blocks (LADDR input).

##### Safety-related master-master communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/22326143883_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F-CPUs of the DP master uses the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type INT or BOOL.

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Program safety-related master-master communication

###### Requirement for programming

The transfer areas for input and output data for the DP/DP coupler must be configured.

###### Programming procedure

You program safety-related master-master communication as follows:

| Symbol | Meaning |
| --- | --- |
| 1. In the safety program from which data is to be sent, call the [SENDDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for sending at the end of the main safety block. 2. In the safety program in which data is to be received, call the [RCVDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for receiving at the start of the main safety block. 3. Assign the start addresses of the transfer areas for output and input data of the DP/DP coupler configured in the hardware and network editor to the respective LADDR inputs.    You must carry out this assignment for every communication connection for each of the F-CPUs involved. 4. Assign the value for the respective F-communication ID to the DP_DP_ID inputs. This establishes the communication relationship between the SENDDP instruction in one F-CPU and the RCVDP instruction in the other F-CPU: The associated instructions receive the same value for DP_DP_ID.    The figure below contains an example of how to specify the F-communication IDs at the inputs of the SENDDP and RCVDP instructions for 5 safety-related master-master communications relationships.               ![Programming procedure](images/166649637515_DV_resource.Stream@PNG-en-US.png)         ![Programming procedure](images/166649637515_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected; however, it must be unique network-wide* and CPU-wide at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program. You must supply constant values to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |     * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3). 5. Supply the SD_BO_xx and SD_I_xx inputs of SENDDP with the send signals. To cut down on intermediate signals when transferring block parameters, you can write the value directly to the instance DB of SENDDP using fully qualified access (for example, "Name SENDDP_1".SD_BO_02) before calling SENDDP. 6. Supply the RD_BO_xx and RD_I_xx outputs of RCVDP with the signals that you want to process further in other program sections or use fully qualified access to read the received signals directly in the associated instance DB in the program sections to be processed further (e.g. "Name RCVDP_1".RD_BO_02). 7. Supply the SUBBO_xx and SUBI_xx inputs of RCVDP with the fail-safe values that are to be output by RCVDP in place of the process data until communication is established for the first time after startup of the sending and receiving F-systems or in the event of an error in safety-related communication.    - Specification of constant fail-safe values:      For data of data type INT, you can enter constant fail-safe values directly as constants in the SUBI_xx input (initial value = "0"). If you want to specify a constant fail-safe value for data of the data type BOOL, provide the tag "F_GLOBDB".VKE1 for the SUBBO_xx input (initial value = "FALSE").    - Specification of variable substitute values:      If you want to specify variable substitute values, define a tag that you calculate through your safety program in an F‑DB and specify this tag (fully qualified) in the SUBI_xx or SUBBO_xx input.        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | Note: The program logic for calculating variable substitute values can only be inserted after the RCVDP calls, because there must be no program logic before the RCVDP calls. This is why the initial values of the substitute values are active in all RCVDP instructions in the first cycle after a startup of the F-system. You must therefore assign appropriate initial values for these tags. (S017) |  | 8. Configure the TIMEOUT inputs of the RCVDP and SENDDP instructions with the required monitoring time.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |     Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times). 9. Optional: Evaluate the ACK_REQ output of the RCVDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether user acknowledgment is required. 10. Supply the ACK_REI input of the RCVDP instruction with the acknowledgment signal for reintegration. 11. Optional: Evaluate the SUBS_ON output of the RCVDP or SENDDP instruction in order to query whether the RCVDP instruction is outputting the fail-safe values assigned in the SUBBO_xx and SUBI_xx inputs. 12. Optional: Evaluate the ERROR output of the RCVDP or SENDDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether a communication error has occurred. 13. Optional: Evaluate the SENDMODE output of the RCVDP instruction in order to query whether the F-CPU with the associated SENDDP instruction is in [disabled safety mode](#disabling-safety-mode-1). |  |

##### Safety-related master-master communication:Limits for data transfer

> **Note**
>
> If the data quantities to be transmitted exceed the capacity of the SENDDP / RCVDP correlated instructions, a second (or third) SENDDP / RCVDP call can be used. This requires configuration of an additional connection via the DP/DP coupler. Whether or not this is possible with one single DP/DP coupler depends on the capacity restrictions of the DP/DP coupler.

#### Safety-related IO controller-I-device communication

This section contains information on the following topics:

- [Configuring safety-related communication between IO controller and I-device](#configuring-safety-related-communication-between-io-controller-and-i-device)
- [Safety-related IO controller-I-device communication via SENDDP and RCVDP](#safety-related-io-controller-i-device-communication-via-senddp-and-rcvdp)
- [Programming safety-related IO controller I-device communication](#programming-safety-related-io-controller-i-device-communication)
- [Safety-related IO-Controller-IO-Device communication - Limits for data transfer](#safety-related-io-controller-io-device-communication---limits-for-data-transfer)

##### Configuring safety-related communication between IO controller and I-device

###### Introduction

Safety-related communication between the safety program of the F‑CPU of an IO controller and the safety program(s) of the F‑CPU(s) of one or more I-devices takes place via IO controller-I‑device transfer areas (**F**‑CD) in PROFINET IO, as in standard systems.

You do not need any additional hardware for IO controller-I‑device communication.

The F-CPU to be used as an I-device must support the "IO-device" operating mode.

###### Configuring transfer areas

For every safety-related communication connection between two F-CPUs, you must configure transfer areas in the hardware and network editor. The figure below shows how both of the F-CPUs are able to send and receive data (bidirectional communication).

![Configuring transfer areas](images/166650387851_DV_resource.Stream@PNG-en-US.png)

The transfer area is assigned a label when it is created to identify it as the communication relationship. For example, "F-CD_PLC_2 PLC_1_1" for the first F-CD connection between IO controller F-CPU 1 and I-device F-CPU 2.

You assign the start addresses of the transfer areas to the LADDR input of the SENDDP and RCVDP instructions in the safety programs.

###### Procedure for configuration

The procedure for configuring safety-related IO controller-I-device communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Enable the "IO Device" mode for F-CPU 2 in the properties of its PN interface and assign this PN interface to a PN interface of F-CPU 1.
3. Select the PROFINET interface of F‑CPU 2. Under "Transfer areas", you create an F‑CD connection (type "F-CD") for sending to the IO controller (←). The F‑CD connection is shown in yellow in the table and the address areas in the I-device and IO controller assigned outside of the process image are displayed.

   In addition, an acknowledgment connection is created automatically for each F‑CD connection. (see "Transfer area details").
4. Create an additional F-CD connection for receiving from the IO controller.
5. In the transfer area you just created, click the arrow in order to change the transfer direction to receiving from IO controller (→).

   ![Procedure for configuration](images/90432221963_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/90432221963_DV_resource.Stream@PNG-en-US.png)

##### Safety-related IO controller-I-device communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/22300267403_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F‑CPUs of the IO controller and an I‑device makes use of the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type INT or BOOL.

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Programming safety-related IO controller I-device communication

###### Requirement for programming

The transfer areas must be configured.

###### Programming procedure

The procedure for programming safety-related IO controller-I‑device communication is the same as that for programming safety-related IO controller-IO controller communication (see [Program safety-related IO controller-IO controller communication](#program-safety-related-io-controller-io-controller-communication)).

The assignment of the start addresses of the transfer areas to the LADDR input of the SENDDP/RCVDP instructions can be obtained from the following table.

| Instruction | Start address LADDR |  |
| --- | --- | --- |
| From row | From column |  |
| SENDDP in the IO controller | → | Address in the IO controller |
| RCVDP in the IO controller | ← | Address in the IO controller |
| SENDDP in the I-device | ← | Address in the IO device |
| RCVDP in the I-device | → | Address in the IO device |

The figure below contains an example of how to specify the F-communication IDs for the inputs of the SENDDP and RCVDP instructions for 4 safety-related IO controller-I‑device communication relationships.

![Programming procedure](images/166650196491_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected; however, it must be unique network-wide* and CPU-wide at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time.(S018) |  |

Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times).

##### Safety-related IO-Controller-IO-Device communication - Limits for data transfer

###### Limits for data transfer

If the amount of data to be transferred is greater than the capacity of related SENDDP/RCVDP instructions, you can use additional SENDDP/RCVDP instructions. Configure additional transfer areas for this purpose. Remember the maximum limit of 1440 bytes of input data or 1440 bytes of output data for transfer between an I-device and a IO controller.

The following table shows the amount of output and input data assigned in safety-related communication connections:

| Safety-related communication | Communication connection | Assigned input and output data |  |  |  |
| --- | --- | --- | --- | --- | --- |
| In the IO controller |  | In the I-device |  |  |  |
| Output data | Input data | Output data | Input data |  |  |
| IO controller-I‑Device | **Sending:**   I‑Device 1 to IO controller | 6 bytes | 12 bytes | 12 bytes | 6 bytes |
| **Receiving:**   I‑Device 1 from IO controller | 12 bytes | 6 bytes | 6 bytes | 12 bytes |  |

Consider all additional configured safety-related and standard communication connections (transfer areas of type F‑CD and CD) for the maximum limit of 1440 bytes of input data or 1440 bytes of output data for transfer between an I-device and an IO controller. In addition, data are assigned for internal purposes such that the maximum limit may be reached sooner.

When the limit is exceeded, a corresponding error message is displayed.

#### Safety-related master-I-slave communication

This section contains information on the following topics:

- [Configuring safety-related master-I-slave communication](#configuring-safety-related-master-i-slave-communication)
- [Safety-related master-I-slave or I-slave-I-slave communication via SENDDP and RCVDP](#safety-related-master-i-slave-or-i-slave-i-slave-communication-via-senddp-and-rcvdp)
- [Program the safety-related master-I-slave or I-slave-I-slave communication](#program-the-safety-related-master-i-slave-or-i-slave-i-slave-communication)
- [Limits for data transfer of safety-related master-I-slave or I-slave-I-slave communication](#limits-for-data-transfer-of-safety-related-master-i-slave-or-i-slave-i-slave-communication)

##### Configuring safety-related master-I-slave communication

###### Introduction

Safety-related communication between the safety program of the F‑CPU of a DP master and the safety program(s) of the F‑CPU(s) of one or more I-slaves takes place via master-I‑slave transfer areas (**F‑**MS), as in standard systems.

You do not need a DP/DP coupler for master-I-slave communication.

###### Configuring transfer areas

For every safety-related communication connection between two F-CPUs, you must configure transfer areas in the hardware and network editor. The figure below shows how both of the F-CPUs are able to send and receive data (bidirectional communication).

![Configuring transfer areas](images/166479547787_DV_resource.Stream@PNG-en-US.png)

The transfer area is assigned a label when it is created to identify it as the communication relationship. For example, "F-MS_PLC_2-PLC_1_1" for the first F-MS connection between DP master F-CPU 1 and I-slave F-CPU 2.

You assign the start addresses of the transfer areas to the LADDR input of the SENDDP and RCVDP instructions in the safety programs.

###### Procedure for configuration

The procedure for configuring safety-related master-I-slave communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Activate the "DP slave" mode (I-slave) for F-CPU 2 in the properties of its DP interface and assign this DP interface to a DP interface of F-CPU 1.
3. Select the PROFIBUS interface of F‑CPU 2. Under "Transfer areas", you create an F‑MS connection (type "F‑MS") for sending to the DP master (←). The F‑MS connection is shown in yellow in the table and the transfer areas in the I-slave and DP master assigned outside of the process image are displayed.

   In addition, an acknowledgment connection is created automatically for each F‑MS connection. (see "Transfer area details").
4. Create an additional F-MS connection for receiving from the DP master.
5. In the transfer area you just created, click the arrow in order to change the transfer direction to receiving from DP master (→).

   ![Procedure for configuration](images/90435767307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/90435767307_DV_resource.Stream@PNG-en-US.png)

##### Safety-related master-I-slave or I-slave-I-slave communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/22426583947_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F‑CPUs of the DP master and an I‑slave or between the F‑CPUs of multiple I‑slaves makes use of the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type INT or BOOL.

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Program the safety-related master-I-slave or I-slave-I-slave communication

###### Requirements

The transfer areas must be configured.

###### Programming procedure

The procedure for programming safety-related master-I-slave communication or I-slave-I-slave communication is the same as that for programming safety-related master-master communication (see [Program safety-related master-master communication](#program-safety-related-master-master-communication)).

The assignment of the start addresses of the transfer areas to the LADDR input of the SENDDP/RCVDP instructions can be obtained from the following table.

| Instruction | Start address LADDR |  |
| --- | --- | --- |
| From row | From column |  |
| SENDDP in the DP master | → | Master address |
| RCVDP in the DP master | ← | Master address |
| SENDDP in the I-slave | ← | Slave address |
| RCVDP in the I-slave | → | Slave address |

The figure below contains an example of how to specify the F-communication IDs at the inputs of SENDDP and RCVDP instructions for four safety-related master-I-slave and two I-slave-I-slave communications relationships.

![Programming procedure](images/166654757259_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected; however, it must be unique network-wide* and CPU-wide at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |

Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times).

##### Limits for data transfer of safety-related master-I-slave or I-slave-I-slave communication

###### Limits for data transfer

If the amount of data to be transferred is greater than the capacity of related SENDDP/RCVDP instructions, you can use additional SENDDP/RCVDP instructions. Configure additional transfer areas for this purpose. Note the maximum limit of 244 bytes of input data or 244 bytes of output data for transfer between an I-slave and a DP master.

The following table shows the amount of output and input data assigned in safety-related communication connections:

| Safety-related communication | Communication connection | Assigned input and output data |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DP master |  | I-slave 1 |  | I-slave 2 |  |  |  |
| Output data | Input data | Output data | Input data | Output data | Input data |  |  |
| Master-I-slave | **Sending:**   I-slave 1 to DP master | 6 bytes | 12 bytes | 12 bytes | 6 bytes | — | — |
| **Receiving:**   I-slave 1 from DP master | 12 bytes | 6 bytes | 6 bytes | 12 bytes | — | — |  |
| I-slave-I-slave | **Sending:**   I-slave 1 to I-slave 2 | — | 18 bytes | 12 bytes | 6 bytes | 6 bytes | 12 bytes |
| **Receiving:**   I-slave 1 from I-slave 2 | — | 18 bytes | 6 bytes | 12 bytes | 12 bytes | 6 bytes |  |

Consider all additional configured safety-related and standard communication connections (transfer areas of type F‑MS-, F‑DX-, F‑DX-Mod., MS-, DX- and DX-Mod) for the maximum limit of 244 bytes of input data or 244 bytes of output data for transfer between an I-device and a DP master F‑MS, F‑DX, F‑DX-Mod., MS, DX). If the maximum limit of 244 bytes of input data or 244 bytes of output data is exceeded, you will receive a corresponding error message.

#### Safety-related I-slave-I-slave communication

This section contains information on the following topics:

- [Configure safety-related I-slave-I-slave communication](#configure-safety-related-i-slave-i-slave-communication)
- [Safety-related I-slave-I-slave communication via SENDDP and RCVDP](#safety-related-i-slave-i-slave-communication-via-senddp-and-rcvdp)
- [Programming safety‑related I‑slave-I‑slave communication](#programming-safety-related-i-slave-i-slave-communication)
- [Limits for data transfer of safety-related I-slave-I-slave communication](#limits-for-data-transfer-of-safety-related-i-slave-i-slave-communication)

##### Configure safety-related I-slave-I-slave communication

###### Introduction

Safety-related communication between the safety program of the F-CPUs of I-slaves takes place using direct data exchange (**F‑**DX) – same as in standard programs.

You do not need any additional hardware for I-slave-I-slave communication.

I-slave-I-slave communication is also possible:

- If the assigned DP master is a standard CPU that supports direct data exchange
- when instead of a DP master, an IO controller is networked with the I-slaves via an IE/PB link

###### Configuring transfer areas

For every safety-related communication connection between two I-slaves, you must configure transfer areas in the hardware and network editor. In the figure below, both of the I-slaves are to be able to send and receive data (bidirectional communication).

![Configuring transfer areas](images/94273236107_DV_resource.Stream@PNG-en-US.png)

The transfer area is assigned a label when it is created to identify it as the communication relationship. For example, "F-DX_PLC_2-PLC_1_1" for the first F-DX connection between F-CPU 1 and F-CPU 2.

You assign the start addresses of the transfer areas to the LADDR input of the SENDDP and RCVDP instructions in the safety programs.

###### Procedure for configuration

The procedure for configuring safety-related I-slave-I-slave communication is identical to that in the standard system. Proceed as follows:

1. Insert three F-CPUS from the "Hardware catalog" task card in the project.
2. Activate "DP slaves" mode (I-slave) for F-CPU 2 and F-CPU 3 in the properties of their DP interfaces and assign these DP interfaces to a DP interface of F-CPU 1.
3. Select the DP interface of F-CPU 3 in the network view.
4. Select the "I/O communication" tab.
5. Use a drag-and-drop operation in the network view to move F-CPU 2 to the "Partner 2" column on the "I/O-communication" tab.

   This creates a line with "Direct data exchange" mode for sending to the I-slave (F-CPU 2) (→).

   ![Procedure for configuration](images/90437909003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/90437909003_DV_resource.Stream@PNG-en-US.png)
6. Click in the newly created line (→).
7. In "Transfer areas" ("Direct data exchange" table), create an F-DX connection (type "F‑DX") for sending to the I-slave (F‑CPU 2) (→). The F‑DX connection is shown in yellow in the table and the transfer areas in the I-slaves assigned outside of the process image (PLC_2 and PLC_3) are displayed.

   In addition, a line with "Direct data exchange" mode for receiving from the I‑slave (F‑CPU 2) (←) is created automatically in the "I/O communication" tab, and an acknowledgment connection (→, transfer area x_Ack) is created automatically in the associated "Direct data exchange" table.

   One transfer area (type F‑MS) for the master CPU is created in the "I‑slave communication table" of each I‑slave.

   This completes the configuration for sending to F‑CPU 2.

   ![Procedure for configuration](images/90438520203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/90438520203_DV_resource.Stream@PNG-en-US.png)
8. In the "I/O communication" tab, select the automatically created line with "Direct data exchange" mode for receiving from the I‑slave (F‑CPU 2) (←).
9. In "Transfer areas" ("Direct data exchange" table), create another F-DX connection for receiving from the I-slave (F-CPU 3).

   In this case, as well, an acknowledgment connection (→, transfer area x_Ack) is created automatically in the "Direct data exchange table" and two transfer areas (type F‑MS) for the master CPU are created in the "I‑slave communication" table of both I‑slaves.

   This completes the configuration for receiving from F‑CPU 2.

   ![Procedure for configuration](images/54005509131_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/54005509131_DV_resource.Stream@PNG-en-US.png)

###### Changing disabled local address areas of the transfer areas

To change the disabled local address area of the "Transfer area x", you must change the start address of the address area of the corresponding acknowledgment connection "Transfer area x_Ack".

1. In "I/O communication", select the line with the arrow pointing in the same direction as the arrow of "Transfer area x" in the "Direct data exchange" table.
2. Then select the line with "Transfer area x_Ack" in the "Direct data exchange" table.
3. Change the start address of the address range there.

##### Safety-related I-slave-I-slave communication via SENDDP and RCVDP

###### Reference

The description of the communication via SENDDP and RCVDP for safety-related I-slave-I-slave communication can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Programming safety-related I-slave-I-slave communication

###### Reference

The description of the programming of safety-related I‑slave-I‑slave communication can be found in [Program the safety-related master-I-slave or I-slave-I-slave communication](#program-the-safety-related-master-i-slave-or-i-slave-i-slave-communication).

The assignment of the start addresses of the transfer areas to the LADDR input of the SENDDP/RCVDP instructions can be obtained from the following table.

| Instruction | Start address LADDR |  |
| --- | --- | --- |
| From row | From column |  |
| SENDDP in the 1st I-slave | → | Address in the <1st I-slave>   (in example column "Address in PLC_2") |
| RCVDP in the 1st I-slave | ← | Address in the <1st I-slave>   (in example column "Address in PLC_2") |
| SENDDP in the 2nd I-slave | ← | Address in the <2nd I-slave>   (in example column "Address in PLC_3") |
| RCVDP in the 2nd I-slave | → | Address in the <2nd I-slave>   (in example column "Address in PLC_3") |

##### Limits for data transfer of safety-related I-slave-I-slave communication

###### Limits for data transfer

The description of the limits for the data transfer of safety-related I-slave-I-slave communication can be found in [Limits for data transfer of safety-related master-I-slave or I-slave-I-slave communication](#limits-for-data-transfer-of-safety-related-master-i-slave-or-i-slave-i-slave-communication).

#### Safety-Related I-Slave-Slave Communication

This section contains information on the following topics:

- [Configuring Safety‑Related I‑Slave-Slave Communication](#configuring-safety-related-i-slave-slave-communication)
- [Safety-Related I-Slave-Slave Communication - F-I/O Access](#safety-related-i-slave-slave-communication---f-io-access)
- [Limits for data transfer of safety-related I-slave-I-slave communication](#limits-for-data-transfer-of-safety-related-i-slave-i-slave-communication-1)

##### Configuring Safety-Related I-Slave-Slave Communication

###### Introduction

Safety-related communication between the safety program of the F-CPU of an I-slave and F-I/O in a DP slave takes place using direct data exchange (**F‑**DX‑Mod), same as in standard programs.

You do not need any additional hardware for I-slave-slave communication.

I-slave-slave communication is also possible:

- when the assigned DP master is a standard CPU, if the standard CPU supports direct data exchange
- when instead of a DP master, an IO controller is networked with the I-slaves via an IE/PB link

An F-I/O DB is automatically generated for each F-I/O when it is configured in the hardware and network editor; this is required for the F-I/O access via safety-related I-slave-slave communication. The F‑I/O DB is initially created in the safety program of the DP master, provided it is an F-CPU with F-activation. Only with the setup of the F‑DX-Mod connection is the F‑I/O DB created in the safety program of the I‑slave and deleted in the safety program of the DP master.

The process image input is used to access the channels of the F-I/O in the safety program of the F-CPU of the I-slave (see description in [Safety-Related I-Slave-Slave Communication - F-I/O Access](#safety-related-i-slave-slave-communication---f-io-access)).

###### Restrictions

> **Note**
>
> Safety-related I‑slave-slave communication with F‑I/O is possible in a DP slave that supports safety-related I‑slave-slave communication, for example with all ET 200SP F-modules with IM 155-6 DP HF, firmware > V3.1, with all ET 200S F‑modules with IM 151-1 HF, with all fail-safe S7‑300 signal modules with IM 153‑2, as of article number 6ES7153‑2BA01‑0XB0, firmware > V4.0.0.

> **Note**
>
> With safety-related I-slave-slave communication, make sure that the CPU of the DP master is powered up before the F-CPU of the I-slave.
>
> Otherwise, depending on the F-monitoring time specified for the F-I/O, the F-system can detect an error in safety-related communication (communication error) between the F-CPU and the F-I/O assigned to the I-slave. This means that the F‑I/O are not reintegrated automatically after F‑system startup. They are instead only reintegrated after a user acknowledgment with a positive edge in the ACK_REI tag of the F‑I/O DB (see also [After communication errors](#after-communication-errors) and [After startup of F-system](#after-startup-of-f-system)).

###### Configuring transfer areas

For every safety-related communication connection between an I-slave and slave, you must configure transfer areas in the hardware and network editor.

The transfer area is assigned a label when it is created to identify it as the communication relationship. For example, "F-DX-Mod_PLC_2-PLC_1_1" for the first F-DX-Mod connection between F-CPU 1 and F-CPU 2.

![Configuring transfer areas](images/90438981131_DV_resource.Stream@PNG-en-US.png)

###### Configuration procedure using the example of an ET 200S with F-modules in the slave

The procedure for configuring safety-related I-slave-slave communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Insert a suitable DP slave, e.g. IM 151‑1 HF, article no. 6ES7151‑1BA0... from the "Hardware catalog" task card into the network view of the hardware and network editor.
3. Insert a power module, a 4/8 F‑DI module and a 4 F‑DQ module in the device view of the ET 200S.
4. Activate "DP slave" mode (I-slave) for F-CPU 2 in the properties of its DP interface and assign this to F-CPU 1.
5. Assign the DP interface of the IM 151‑1 HF to the DP master (F‑CPU 1).
6. Select the DP interface of F-CPU 2 (I-slave) in the network view.
7. Select the "I/O communication" tab.
8. Use a drag-and-drop operation in the network view to move the ET 200S to the "Partner 2" column in the "I/O-communication" tab.

   ![Configuration procedure using the example of an ET 200S with F-modules in the slave](images/53119743115_DV_resource.Stream@PNG-en-US.png)

   ![Configuration procedure using the example of an ET 200S with F-modules in the slave](images/53119743115_DV_resource.Stream@PNG-en-US.png)
9. Click in the newly created line (←).
10. In "Transfer areas", create an F-DX-Mod connection (type "F‑DX-Mod"). The F‑DX‑Mod connection is marked in yellow in the table. The addresses for the "partner module" 4/8 F‑DI in the I‑Slave (PLC_2) are displayed. You can change the addresses directly in the table, if required.

    This completes the configuration for the 4/8 F‑DI module.
11. In "Transfer areas", create another F-DX-Mod connection.
12. Change the partner module to the 4 F‑DO module, either directly in the "Transfer areas" table or in the details of transfer area 2, if the 4 F-DO module was not already selected.

    This completes the configuration for the 4 F‑DO module.

    ![Configuration procedure using the example of an ET 200S with F-modules in the slave](images/53120022283_DV_resource.Stream@PNG-en-US.png)

    ![Configuration procedure using the example of an ET 200S with F-modules in the slave](images/53120022283_DV_resource.Stream@PNG-en-US.png)

In the "I‑slave communication table" of the I‑slave, a transfer area (type F‑MS) for the master CPU is automatically created for each F‑DX-Mod connection:

![Configuration procedure using the example of an ET 200S with F-modules in the slave](images/53120250635_DV_resource.Stream@PNG-en-US.png)

###### Change in configuration of I-slave-slave communication

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you have added or deleted I-slave-slave communication for an F-I/O, you must compile and download the hardware configuration of the DP master as well as the hardware configuration of the I-slave.   The Collective F-Signature in the F-CPU of the I-slave and the Collective F-Signature in the F-CPU of the DP master (if a safety program exists there, too) are set to "0". You must then recompile the safety program(s). (S019) |  |

##### Safety-Related I-Slave-Slave Communication - F-I/O Access

###### Access via the process image

In safety-related I‑slave-slave communication, you use the process image (PII or PIQ) to access the F‑I/O in the safety program of the F‑CPU of the I‑slave. This is the same as F-I/O access to F-I/O that are directly assigned to an I-slave or DP master. In the I-slave you access the F-I/O with the addresses that were assigned for the F-DX-Mod connection in "Transfer areas" ("Direct data exchange" table).

In this case, ignore the displayed operand area. Access F-I/O with inputs using the PII and F-I/O with outputs using PIQ.

Information on I/O access can be found in [F-I/O access](#f-io-access).

##### Limits for data transfer of safety-related I-slave-I-slave communication

###### Limits for data transfer

Note the maximum limit of 244 bytes of input data or 244 bytes of output data for transfer between an I-slave and a DP master.

An example of the amount of output data and input data that are assigned for safety-related communication is shown in the table below for an ET 200S 4/8 F-DI and an ET 200S 4 F-DO:

| Safety-related communication | Communication connection | Assigned input and output data* |  |
| --- | --- | --- | --- |
| Between I-slave and DP master |  |  |  |
| Output Data in the I-slave | Input data in the I-slave |  |  |
| I-slave-slave | I-slave-slave communication with 4/8 F-DI | 4 bytes | 6 bytes |
| I-slave-slave communication with 4 F-DO | 5 bytes | 5 bytes |  |
| * Example for 4/8 F-DI and 4 F-DO of ET 200S |  |  |  |

Consider all additional configured safety-related and standard communication connections (F‑MS, F‑DX, F‑DX‑Mod., MS and DX connections) for the maximum limit of 244 bytes of input data or 244 bytes of output data for transfer between an I‑slave and a DP master. If the maximum limit of 244 bytes of input data or 244 bytes of output data is exceeded, you will receive a corresponding error message.

#### Safety-related IO controller-I-slave communication

This section contains information on the following topics:

- [Safety-related IO controller-I-slave communication](#safety-related-io-controller-i-slave-communication-1)

##### Safety-related IO controller-I-slave communication

###### Introduction

Safety-related communication between the safety program of the F‑CPU of an IO controller and the safety program(s) of the F‑CPU(s) of one or more I-slaves takes place via master‑I-slave transfer areas (**F‑**MS), as in standard systems.

###### IE/PB link

For the safety-related IO-controller-I-slave communication, the IE/PB link is mandatory. Each of the two F-CPUs is linked to the IE/PB link by means of its PROFIBUS DP or PROFINET-interface.

> **Note**
>
> If you are using an IE/PB link, you must take this into account when configuring the F-specific monitoring times and when calculating the maximum response time of your F-system (see also [Monitoring and response times](#monitoring-and-response-times)).
>
> Note that the [Excel file for calculating response times](https://support.industry.siemens.com/cs/ww/en/view/109783831) for S7-300/400 F-CPUs does not support all conceivable configurations.

###### Reference

The information on safety-related master-I-slave communication in [Safety-related master-I-slave communication](#safety-related-master-i-slave-communication) also applies.

#### Safety-related communication via S7 connections

This section contains information on the following topics:

- [Configuring safety-related communication via S7 connections](#configuring-safety-related-communication-via-s7-connections)
- [Communication via SENDS7, RCVS7, and F-Communication DB](#communication-via-sends7-rcvs7-and-f-communication-db)
- [Programming safety-related communication via S7 connections](#programming-safety-related-communication-via-s7-connections)
- [Safety‑related communication via S7 connections - Limits of data transfer](#safety-related-communication-via-s7-connections---limits-of-data-transfer)

##### Configuring safety-related communication via S7 connections

###### Introduction

Safety-related communication between the safety programs of F-CPUs via S7 connections takes place by means of established S7 connections that you create in the network view of the hardware and network editor - same as in standard programs.

###### Restrictions

> **Note**
>
> In SIMATIC Safety, S7 connections are generally permitted only via Industrial Ethernet.
>
> Safety-related communication via S7 connections is possible from and to the following CPUs:
>
> - S7‑300 F‑CPUs via the integrated PROFINET interface
> - S7‑400 F‑CPUs via the integrated PROFINET interface or a CP 443-1 or CP 443‑1 Advanced‑IT

###### Creating S7 connections

For each connection between two F-CPUs, you must create an S7 connection in the network view of the hardware and network editor.

For every end-point of a connection, a local and a partner ID is automatically assigned from the perspective of the end-point (the F-CPU). If necessary, you can change both IDs in the "Connections" tab. You assign the local ID to the "ID" input of the SENDS7 and RCVS7 instructions in the safety programs.

![Creating S7 connections](images/53118552075_DV_resource.Stream@PNG-en-US.png)

###### Procedure for configuring S7 connections

You configure the S7 connections for safety-related CPU-to-CPU communication in the same way as in STEP 7 Professional (see Help on STEP 7 Professional "S7 connections").

##### Communication via SENDS7, RCVS7, and F-Communication DB

###### Communication via the SENDS7 and RCVS7 instructions

![Communication via the SENDS7 and RCVS7 instructions](images/28305475467_DV_resource.Stream@PNG-en-US.png)

You use the **SENDS7** **and** **RCVS7** instructions for fail-safe sending and receiving of data via S7 connections.

These instructions can be used to transmit a specified amount of fail-safe data of data types BOOL, INT, WORD, DINT, DWORD, and TIME in a fail-safe manner. The fail-safe data are stored in F-DBs (F-communication DBs) that you have created.

You can find these instructions in the "Instructions" task card under "Communication". The RCVS7 instruction **must** be called at the start of the main safety block. The SENDS7 instruction **must** be called at the end of the main safety block.

Note that the send signals are sent only after calling the SENDS7 instruction at the end of the relevant F-runtime group execution.

A detailed description of the SENDS7 and RCVS7 instructions is found in [SENDS7 and RCVS7: Communication via S7 connections (STEP 7 Safety Advanced V19) (S7-300, S7-400)](STEP%207%20Safety%20V19%20instructions.md#sends7-and-rcvs7-communication-via-s7-connections-step-7-safety-advanced-v19-s7-300-s7-400).

###### F-communication DB

For each connection, send data are stored in an F-DB (F-communication DBx) and receive data are stored in an F‑DB (F‑communication DBy).

You can assign the F-communication DB numbers in the SENDS7 and RCVS7 instructions.

##### Programming safety-related communication via S7 connections

###### Introduction

The programming of safety-related CPU-CPU communication via S7 connections is described below. You must set up the following in the safety programs of the relevant F-CPUs:

- Create F-DBs (F‑Communication‑DBs) in which send/receive data for communication are stored.
- Call and assign parameters for instructions for communication from the "Instructions" Task Card in the safety program.

###### Requirement for programming

The S7 connections between the relevant F-CPUs must be configured in the network view in the "Connections" tab of the hardware and network editor.

###### Creating and Editing an F-Communication DB

F-communication DBs are F-DBs that you create and edit in the same way as other F-DBs in the project tree. You can assign the F-communication DB numbers in the SENDS7 and RCVS7 instructions.

> **Note**
>
> The length and structure of the F‑communication DB on the receiver side must match the length and structure of the associated F‑communication DB on the sender side.
>
> If the F-communication DBs do not match, the F-CPU can go to STOP mode. A diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> For this reason, we recommend that you use the following procedure:
>
>
>
> 1. Create an F-communication DB in the project tree in or below the "Program blocks" folder of the F-CPU at the sender end.
> 2. Specify the appropriate structure of the F‑communication DB, taking into account the data to be transferred.
> 3. Copy this F-communication DB to the project tree in or below the "Program blocks" folder of the F-CPU at the receiver end, and change the name, if necessary.

###### Other requirements for F-communication DBs

F-communication DBs must also conform to the following properties:

- They are not permitted to be instance DBs.
- Their length is not permitted to exceed 100 bytes.
- In F‑communication DBs, only the following data types may be declared: BOOL, INT, WORD, DINT, DWORD, and TIME.
- The data types must be arranged block-wise and in the following order: BOOL, data types with bit length of 16 bits (INT, WORD), and data types with bit length of 32 bits (DINT, DWORD, and TIME). Within the data blocks with lengths of 16 bits and 32 bits, the data types can be arranged in any order.
- No more than 128 data elements of data type BOOL are permitted to be declared.
- The amount of data of data type BOOL must always be an integer multiple of 16 (word limit). Reserve data must be added, if necessary.

If these criteria are not fulfilled, STEP 7 Safety Advanced outputs an error message during compilation.

###### Assignment of fail-safe values

Fail-safe values are made available at the receiver end:

- While the connection between the communication partners is being established the first time after startup of the F-systems
- Whenever a communication error occurs

The values you specified as initial values in the F-communication DB at the receiver end are made available as initial values.

###### Programming procedure

You program safety-related communication via S7 connections as follows:

| Symbol | Meaning |
| --- | --- |
| 1. Supply the tags in the F‑communication DB at the sender end with send signals using fully qualified access (e.g., "Name of F‑communication DB".tag name). 2. Read the tags in the F‑communication DB at the receiver end (receive signals) that you want to process further in other sections of the program using fully qualified access (e.g., "Name of F‑communication DB".tag name). 3. In the safety program from which data is to be sent, call the SENDS7 instruction for sending at the end of the main safety block. 4. In the safety program in which data is to be received, call the instruction RCVS7 for receiving at the start of the main safety block. 5. Assign F-communication DB numbers to the SEND_DB input of SENDS7 and the RCV_DB input of RCVS7. 6. Assign the local ID of the S7 connection (data type: WORD) from the perspective of the F‑CPU that was configured in the "Connections" tab of the network view to the ID input of SENDS7. 7. Assign the local ID of the S7 connection (data type: WORD) that was configured in the "Connections" tab of the network view to the ID input of RCVS7. 8. Assign an odd number (data type: DWORD) to the R_ID inputs of SENDS7 and RCVS7. This serves to specify that a SENDS7 instruction belongs to an RCVS7 instruction. The associated instructions receive the same value for R_ID.               ![Programming procedure](images/166649566219_DV_resource.Stream@PNG-en-US.png)         ![Programming procedure](images/166649566219_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The value of the respective F-communication ID (input R_ID; data type: DWORD) can be freely selected; however, it must be odd and unique for all safety-related communication connections network-wide* and CPU-wide. The value R_ID + 1 is internally assigned and must not be used. You must supply inputs ID and R_ID with constant values when calling the instruction. Direct read or write access to ID and R_ID in the associated instance DB is not permitted in the safety program. (S020) |  |     * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3). 9. Assign the TIMEOUT inputs of the SENDS7 and RCVS7 instructions with the required monitoring time.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |     Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times). 10. To reduce the bus load, you can temporarily shut down communication between the F-CPUs at input EN_SEND of the SENDS7 instruction. To do so, supply input EN_SEND (initial value = "TRUE") with 0. In this case, send data is no longer sent to the F-communication DB of the associated RCVS7 instruction and the receiver RCVS7 provides fail-safe values for this period (initial values in its F-communication DB). If communication was already established between the partners, a communication error is detected. 11. Optional: Evaluate the ACK_REQ output of RCVS7, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether user acknowledgment is required. 12. Supply the ACK_REI input of RCVS7 with the signal for the acknowledgment for reintegration. 13. Optional: evaluate the SUBS_ON output of RCVS7 or SENDS7 in order to query whether the RCVS7 instruction is outputting the fail-safe values you specified as initial values in the F-communication DB. 14. Optional: Evaluate the ERROR output of RCVS7 or SENDS7, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether a communication error has occurred. 15. Optional: evaluate the SENDMODE output of RCVS7 in order to query whether the F-CPU with the associated SENDS7 instruction is in [disabled safety mode](#disabling-safety-mode-1). |  |

###### Particularities for migrated projects

If you have migrated a project from S7 Distributed Safety V5.4 SP5 to STEP 7 Safety Advanced in which safety-related communication via S7 connections is programmed, you must note the following:

- Do not delete migrated instance DBs for the SENDS7 and RCVS7 instructions in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks".

Otherwise, communication errors may occur in the relevant communication connections.

A migrated instance DB for the SENDS7 and RCVS7 instructions has been deleted if, after compiling the safety program, the "User-defined ID" in the newly generated is not identical to "FRCVS7CL" or "FSNDS7CL".

You can find the "User-defined ID" of a block in its properties in the "Information" area.

##### Safety-related communication via S7 connections - Limits of data transfer

###### 

> **Note**
>
> If the amount of data to be transmitted exceeds the permitted length for the F‑communication DB (100 bytes), you can create another F‑communication DB that you transfer to additional SENDS7/RCVS7 instructions with modified R_ID.

Note that USEND and URCV instructions are called internally at each SENDS7 or RCVS7 call and use connection resources in the F‑CPU. This affects the maximum number of communication connections available (see manuals for F-CPUs).

Additional information on the data transfer limits for S7 connections of individual F-CPUs is available on the [Internet](http://support.automation.siemens.com/WW/view/en/38549114).

#### Safety-related communication with other S7 F-systems

This section contains information on the following topics:

- [Introduction](#introduction-2)
- [Communication with S7 Distributed Safety via PN/PN coupler (IO controller-IO controller communication)](#communication-with-s7-distributed-safety-via-pnpn-coupler-io-controller-io-controller-communication)
- [Communication with S7 Distributed Safety via DP/DP coupler (master-master communication)](#communication-with-s7-distributed-safety-via-dpdp-coupler-master-master-communication)
- [Communication with S7 Distributed Safety via S7 connections](#communication-with-s7-distributed-safety-via-s7-connections)
- [Communication with S7 F/FH Systems via S7 connections](#communication-with-s7-ffh-systems-via-s7-connections)

##### Introduction

Safety-related communication from F-CPUs in SIMATIC Safety to F‑CPUs in S7 Distributed Safety F-systems is possible via a PN/PN coupler or DP/DP coupler that you use between the two F-CPUs as IO controller-IO controller communication, master-master communication or communication via established S7 connections.

Safety-related communication from F-CPUs in SIMATIC Safety to F-CPUs in S7 F/FH Systems F-systems is possible via established S7 connections.

##### Communication with S7 Distributed Safety via PN/PN coupler (IO controller-IO controller communication)

Communication functions between SENDDP/RCVDP instructions at the STEP 7 Safety Advanced end and F-application blocks F_SENDDP/F_RCVDP at the S7 Distributed Safety end:

![Figure](images/60219702411_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the S7 Distributed Safety end

At the S7 Distributed Safety end, proceed as described in "Safety-related IO controller-IO controller communication" in the [S7 Distributed Safety - Configuring and Programming](http://support.automation.siemens.com/WW/view/en/22099875) manual.

###### Procedure at the STEP 7 Safety Advanced end

At the STEP 7 Safety Advanced end, proceed as described in [Safety-related IO controller-IO controller communication](#safety-related-io-controller-io-controller-communication).

##### Communication with S7 Distributed Safety via DP/DP coupler (master-master communication)

Communication functions between SENDDP/RCVDP instructions at the STEP 7 Safety Advanced end and F-application blocks F_SENDDP/F_RCVDP at the S7 Distributed Safety end:

![Figure](images/60219630091_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the S7 Distributed Safety end

At the S7 Distributed Safety end, proceed as described in "Safety-related master-master communication" in the [S7 Distributed Safety - Configuring and Programming](http://support.automation.siemens.com/WW/view/en/22099875) manual.

###### Procedure at the STEP 7 Safety Advanced end

At the STEP 7 Safety Advanced end, proceed as described in [Safety-related master-master communication](#safety-related-master-master-communication).

##### Communication with S7 Distributed Safety via S7 connections

Communication functions between SENDS7/RCVS7 instructions at the STEP 7 Safety Advanced end and F_SENDS7/F_RCVS7 F-application blocks at the S7 Distributed Safety end:

![Figure](images/60219536651_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the S7 Distributed Safety end

At the S7 Distributed Safety end, proceed as described in section "Safety-related communication via S7 communications" in the [S7 Distributed Safety - Configuring and Programming](http://support.automation.siemens.com/WW/view/en/22099875) manual.

Because safety-related communication via S7 connections is not possible with unspecified partners in S7 Distributed Safety, you must first create a "virtual" SIMATIC station in S7 Distributed Safety in which you configure an F-CPU as a proxy for the F-CPU in STEP 7 Safety Advanced with its IP address.

You then insert an S7 connection to this F-CPU in the connection table. Both the local connection and partner connection resources (hex) are thereby fixed. You must then set these in the associated, unspecified S7 connection that you created in STEP 7 Professional.

In addition, for all communication connections to this F‑CPU, you must transfer the F-communication ID that you assigned in the R_ID input of the associated calls of the F_SENDS7 and F_RCVS7 F-application blocks additionally to the CRC_IMP tag in the instance DB of F_SENDS7 and F_RCVS7, respectively, in the standard user program immediately before calling the F‑CALL.

Program example:

![Procedure at theS7 Distributed Safetyend](images/60219583371_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the STEP 7 Safety Advanced end

At the STEP 7 Safety Advanced end, proceed as described in [Safety-related communication via S7 connections](#safety-related-communication-via-s7-connections).

For the F-CPU in S7 Distributed Safety, you must create and specify an unspecified S7 connection. You can find information on this in the STEP 7 help, under "Creating an unspecified connection" or "Specifying and unspecified connection".

For these you must set the local and partner connection resources (hex) that are fixed as a result of the associated S7 connection that you have created in S7 Distributed Safety.

If the local connection resource (hex) is already occupied by an existing connection, you must change the connection resource (hex) for it.

If the instance DBs of the SENDS7 and RCVS7, instructions that you want to use for communication with S7 Distributed Safety were migrated from S7 Distributed Safety, you must delete them in the project tree in the "STEP 7 Safety" folder, under "Program blocks > System blocks" (contrary to the information in [Programming safety-related communication via S7 connections](#programming-safety-related-communication-via-s7-connections), section "Particularities for migrated projects").

##### Communication with S7 F/FH Systems via S7 connections

Communication functions between SENDS7/RCVS7 instructions at the STEP 7 Safety Advanced end and F_SDS_BO/F_RDS_BO F-blocks at the S7 F Systems end.

A maximum of 32 data elements of data type BOOL can be exchanged.

![Figure](images/60219807755_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the S7 F Systems end

At the S7 F systems end, proceed as described in section "Safety-related communication between F-CPUs" in the [S7 F/FH Systems - Configuring and Programming](http://support.automation.siemens.com/WW/view/en/16537972) manual.

Because safety-related communication via S7 connections is not possible with unspecified partners in S7 F/FH Systems, you must first create a "virtual" SIMATIC station in S7 F/FH Systems in which you configure an F-CPU as a proxy for the F-CPU in STEP 7 Safety Advanced with its IP address.

You then insert an S7 connection to this F-CPU in the connection table. Both the local connection and partner connection resources (hex) are thereby fixed. You must then set these in the associated, unspecified S7 connection that you created in STEP 7 Safety Advanced.

In addition, you must insert a function in your S7 program (in the area reserved in CFC for other applications), in which, for all communication connections for this F-CPU, you transfer the F-communication ID that you assigned in the R_ID input of the associated calls of the F_SDS_BO and F_RDS_BO F-blocks additionally to the CRC_IMP tag in the instance DB of the F_SDS_BO and F_RDS_BO, respectively. You obtain the number of the instance DB from the object properties of the block in CFC. Assign descriptive names for these instance DBs. If you perform a compress operation in CFC, you must check whether the numbers of these instance DBs have changed.

Program example:

![Procedure at theS7 F Systemsend](images/60219761035_DV_resource.Stream@PNG-en-US.png)

You must then import the function in CFC as block type and insert your standard user program in a chart. In the run sequence, make sure that the associated standard runtime group is processed before the F-runtime group.

###### Procedure at the STEP 7 Safety Advanced end

At the STEP 7 Safety Advanced  end, proceed as described in ["Safety-related communication via S7 connections"](#safety-related-communication-via-s7-connections).

**Particularity:** In STEP 7 Safety Advanced, you must create the F‑communication DB with exactly 32 data elements of data type BOOL.

For the F-CPU in S7 F/FH Systems, you must create and specify an unspecified S7 connection. You can find information on this in the STEP 7 help, under "Creating an unspecified connection" or "Specifying an unspecified connection".

For these you must set the local and partner connection resources (hex) that are fixed as a result of the associated S7 connection that you have created in S7 F Systems.

If the local connection resource (hex) is already occupied by an existing connection, you must change the connection resource (hex) for it.

### Configuring and programming communication (S7-1200, S7-1500)

This section contains information on the following topics:

- [Overview of communication](#overview-of-communication-1)
- [Safety-related IO controller-IO controller communication](#safety-related-io-controller-io-controller-communication-1)
- [Safety-related master-master communication](#safety-related-master-master-communication-1)
- [Safety-related IO controller-I-device communication](#safety-related-io-controller-i-device-communication-1)
- [Safety-related master-I-slave communication](#safety-related-master-i-slave-communication-1)
- [Safety-related IO controller-I-slave communication](#safety-related-io-controller-i-slave-communication-2)
- [Safety-related communication to S7 F-System S7 Distributed Safety](#safety-related-communication-to-s7-f-system-s7-distributed-safety)

#### Overview of communication

##### Introduction

This section gives an overview of the safety-related communication options in SIMATIC Safety F-systems.

##### Options for safety-related communication

| Safety-related communication | On subnet | Additional hardware required |
| --- | --- | --- |
| **Safety-related CPU-CPU communication:** |  |  |
| IO controller-IO controller communication | PROFINET IO | PN/PN coupler |
| Master‑master communication | PROFIBUS DP | DP/DP coupler |
| IO controller-I-device communication | PROFINET IO | — |
| Master-I-slave communication | PROFIBUS DP | — |
| IO controller-I-slave communication | PROFINET IO and PROFIBUS DP | IE/PB link |
| IO controller-IO controller communication for S7 Distributed Safety | PROFINET IO | PN/PN coupler |
| Master-master communication for S7 Distributed Safety | PROFIBUS DP | DP/DP coupler |

> **Note**
>
> The options for safety-related communication depend on the F-CPUs used.

> **Note**
>
> Safety-related communication with S7-1200 F-CPUs is only permitted as of firmware V4.1.2.

##### Overview of safety-related communication via PROFIBUS DP

The figure below provides an overview of the options for safety-related communication via PROFIBUS DP in SIMATIC Safety F‑systems with S7-1200/1500 F-CPUs.

![Overview of safety-related communication via PROFIBUS DP](images/166489612555_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Safety-related master-master communication |
| ② | Safety-related master-I-slave communication |

##### Overview of safety-related communication via PROFINET IO

The figure below provides an overview of the options for safety-related communication via PROFINET IO in SIMATIC Safety F‑systems with S7-1200/1500 F-CPUs.

![Overview of safety-related communication via PROFINET IO](images/172755273483_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Safety-related IO controller-IO controller communication |
| ② | Safety-related IO controller-I-device communication |
| ③ | Safety-related IO controller-I-slave communication |
| ④ | Safety-related IO controller-I-device communication (shared I-device) |

##### Safety-related CPU-CPU communication via PROFIBUS DP or PROFINET IO

In safety-related CPU-CPU communication, a fixed amount of data of the data type BOOL or INT (DINT as alternative) is transmitted fail-safe between the safety programs in F-CPUs of DP masters/I-slaves or IO controllers/I-devices.

The data are transferred using the SENDDP instruction for sending and the RCVDP instruction for receiving. The data are stored in configured transfer areas of the devices. The hardware identifier (HW identifier) defines the transfer areas configured.

##### Safety-related CPU-CPU communication for S7 Distributed Safety

Safety-related communication is possible from F-CPUs in SIMATIC Safety to F-CPUs in S7 Distributed Safety.

#### Safety-related IO controller-IO controller communication

This section contains information on the following topics:

- [Configure safety-related IO controller-IO controller communication](#configure-safety-related-io-controller-io-controller-communication-1)
- [Safety-related IO controller-IO controller communication via SENDDP and RCVDP](#safety-related-io-controller-io-controller-communication-via-senddp-and-rcvdp-1)
- [Program safety-related IO controller-IO controller communication](#program-safety-related-io-controller-io-controller-communication-1)
- [Safety-related IO controller-IO controller communication - Limits for data transfer](#safety-related-io-controller-io-controller-communication---limits-for-data-transfer-1)

##### Configure safety-related IO controller-IO controller communication

###### Introduction

Safety-related communication between safety programs of the F-CPUs of IO controllers takes place over a PN/PN coupler that you set up between the F-CPUs.

> **Note**
>
> Deactivate the "Data validity display DIA" parameter in the properties for the PN/PN coupler in the hardware and network editor. This is the default setting. Otherwise, safety-related IO controller-IO controller communication is not possible.

###### Configuring transfer areas

You must configure one transfer area for output data and one transfer area for input data in the hardware and network editor for each safety-related communication connection between two F-CPUs in the PN/PN coupler. The figure below shows how both of the F-CPUs are able to send **and** receive data (bidirectional communication).

![Configuring transfer areas](images/166480033419_DV_resource.Stream@PNG-en-US.png)

###### Rules for defining transfer areas

**Data to be sent:**

A total of 12 bytes (consistent) is required for the transfer area for output data; 6 bytes (consistent) are required for the transfer area for input data.

**Data to be received:**

A total of 12 bytes (consistent) is required for the transfer area for input data; 6 bytes (consistent) are required for the transfer area for output data.

> **Note**
>
> **PN/PN Coupler article number 6ES7158-3AD10-0XA0**
>
> When configuring the transfer areas for the output and input data, proceed as described in the "[SIMATIC bus links PN/PN coupler](https://support.industry.siemens.com/cs/ww/en/view/44319532)" manual, section "Configuring the PN/PN Coupler with STEP 7 TIA Portal".

###### Procedure for configuration

The procedure for configuring safety-related IO controller-IO controller communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Switch to the network view of the hardware and network editor.
3. Select a PN/PN Coupler X1 and a PN/PN Coupler X2 from "Other field devices\PROFINET IO\Gateway\Siemens AG\PN/PN Coupler" in the "Hardware catalog" task card and insert them into the network view of the hardware and network editor.
4. Connect the PN interface of the F-CPU 1 with the PN interface of the PN/PN Coupler X1 and the PN interface of the F-CPU 2 with the PN interface of PN/PN Coupler X2.

   ![Procedure for configuration](images/90982490507_DV_resource.Stream@PNG-en-US.png)
5. Switch to the device view of PN/PN Coupler X1 for bidirectional communication connections i.e. where each F‑CPU is both to send and to receive data. Select the following modules from "IN/OUT" in the "Hardware catalog" task card (with filter activated), and insert them in the "Device overview" tab:

   - One "IN/OUT 6 bytes / 12 bytes" module and
   - One "IN/OUT 12 bytes / 6 bytes" module
   > **Note**
   >
   > The transfer areas are assigned on the basis of the hardware identifier which is automatically assigned to the modules and devices. You need the HW identifier to program the SENDDP and RCVDP blocks (LADDR input). A system constant is created in the corresponding F-CPU for each hardware identifier of the transfer area. You can assign these system constants symbolically to the SENDDP and RCVDP blocks.

   ![Procedure for configuration](images/103741600907_DV_resource.Stream@PNG-en-US.png)
6. Select the following modules from "IN/OUT" in the device view of PN/PN coupler X2 and insert them in the "Device overview" tab:

   - One "IN/OUT 12 bytes / 6 bytes" module and
   - One "IN/OUT 6 bytes / 12 bytes" module

   ![Procedure for configuration](images/103742020363_DV_resource.Stream@PNG-en-US.png)

##### Safety-related IO controller-IO controller communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/50195203723_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F-CPUs of the IO controllers uses the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type BOOL or INT (DINT as alternative).

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

You can also call up the RCVDP and SENDDP instructions in separate F-FBs/F-FCs which you have to call at the start or end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Program safety-related IO controller-IO controller communication

###### Requirement for programming

The transfer areas for input and output data for the PN/PN coupler must be configured.

###### Programming procedure

You program safety-related IO controller-IO controller communication as follows:

| Symbol | Meaning |
| --- | --- |
| 1. In the safety program from which data is to be sent, call the [SENDDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for sending at the end of the main safety block. 2. In the safety program in which data is to be received, call the [RCVDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for receiving at the start of the main safety block. 3. Assign the HW identifiers (system constants in the default tag table) of the transfer areas for output and input data of the PN/PN coupler that are configured in the hardware and network editor to the respective LADDR inputs.    You must carry out this assignment for every communication connection for each of the F-CPUs involved. 4. Assign the value for the respective F-communication ID to the DP_DP_ID inputs. This establishes the communication relationship between the SENDDP instruction in one F-CPU and the RCVDP instruction in the other F-CPU: The associated instructions receive the same value for DP_DP_ID.    The figure below contains an example of how to specify the F-communication IDs at the inputs of the SENDDP and RCVDP instructions for 5 safety-related IO controller-IO controller communication relationships.               ![Programming procedure](images/166650691723_DV_resource.Stream@PNG-en-US.png)         ![Programming procedure](images/166650691723_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide**** at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program. You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |     * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).    ** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".    *** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase.     **** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one single F-CPU with regard to the DP_DP_ID. 5. Supply the SD_BO_xx and SD_I_xx inputs (SD_DI_00 as alternative) of SENDDP with the send signals. To cut down on intermediate signals when transferring block parameters, you can write the value directly to the instance DB of SENDDP using fully qualified access (for example, "Name SENDDP_1".SD_BO_02) before calling SENDDP. 6. Supply the RD_BO_xx and RD_I_xx outputs (RD_DI_00 as alternative) of RCVDP with the signals that you want to process further in other program sections or use fully qualified access to read the received signals directly in the associated instance DB in the program sections to be processed further (e.g., "Name RCVDP_1".RD_BO_02). 7. If you want to send the data at the SD_DI_00 input instead of the data at the SD_I_00 and SD_I_01 inputs, supply the DINTMODE input (initial value = "FALSE") of SENDDP with TRUE. 8. Supply the SUBBO_xx and SUBI_xx or alternatively SUBDI_00 inputs of RCVDP with the fail-safe values that are to be output by RCVDP in place of the process data until communication is established for the first time after startup of the sending and receiving F-systems or in the event of an error in safety-related communication.    - Specification of constant fail-safe values:      For data of data type INT/DINT, you can enter constant fail-safe values directly as constants in the SUBI_xx or alternatively SUBDI_00 input (initial value = "0"). If you want to specify a constant fail-safe value "TRUE" for data of the data type BOOL, set TRUE for the SUBBO_xx input (initial value = "FALSE").    - Specification of variable substitute values:      If you want to specify variable substitute values, define a tag that you calculate through your safety program in an F‑DB and specify this tag (fully qualified) in the SUBBO_xx or SUBI_xx or alternatively SUBDI_00 input.        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | Note: The program logic for calculating variable substitute values can only be inserted after the RCVDP calls, because there must be no program logic before the RCVDP calls. This is why the initial values of the substitute values are active in all RCVDP instructions in the first cycle after a startup of the F-system. You must therefore assign appropriate initial values for these tags. (S017) |  | 9. Configure the TIMEOUT inputs of the RCVDP and SENDDP instructions with the required monitoring time.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |     Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times). 10. Optional: Evaluate the ACK_REQ output of the RCVDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether user acknowledgment is required. 11. Supply the ACK_REI input of the RCVDP instruction with the acknowledgment signal for reintegration. 12. Optional: Evaluate the SUBS_ON output of the RCVDP or SENDDP instruction in order to query whether the RCVDP instruction is outputting the fail-safe values assigned in the SUBBO_xx and SUBI_xx or alternatively SUBDI_00 inputs. 13. Optional: Evaluate the ERROR output of the RCVDP or SENDDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether a communication error has occurred. 14. Optional: Evaluate the SENDMODE output of the RCVDP instruction in order to query whether the F-CPU with the associated SENDDP instruction is in [disabled safety mode](#disabling-safety-mode-1). |  |

##### Safety-related IO controller-IO controller communication - Limits for data transfer

> **Note**
>
> If the data quantities to be transmitted exceed the capacity of the SENDDP / RCVDP correlated instructions, a second (or third) SENDDP / RCVDP call can be used. This requires configuration of an additional communication connection via the PN/PN coupler. Whether or not this is possible with one single PN/PN coupler depends on the capacity restrictions of the PN/PN coupler.

#### Safety-related master-master communication

This section contains information on the following topics:

- [Configure safety-related master-master communication](#configure-safety-related-master-master-communication-1)
- [Safety-related master-master communication via SENDDP and RCVDP](#safety-related-master-master-communication-via-senddp-and-rcvdp-1)
- [Program safety-related master-master communication](#program-safety-related-master-master-communication-1)
- [Safety‑related master‑master communication:Limits for data transfer](#safety-related-master-master-communicationlimits-for-data-transfer-1)

##### Configure safety-related master-master communication

###### Introduction

Safety-related communication between safety programs of the F-CPUs of DP masters takes place via a DP/DP coupler.

> **Note**
>
> Switch the data validity indicator "DIA" on the DIP switch of the DP/DP coupler to "OFF". Otherwise, safety-related CPU-CPU communication is not possible.

###### Configuring transfer areas

You must configure one transfer area for output data and one transfer area for input data in the hardware and network editor for each safety-related communication connection between two F-CPUs in the DP/DP coupler. The figure below shows how both of the F-CPUs are able to send and receive data (bidirectional communication).

![Configuring transfer areas](images/166659937163_DV_resource.Stream@PNG-en-US.png)

###### Rules for defining transfer areas

**Data to be sent:**

A total of 12 bytes (consistent) is required for the transfer area for output data; 6 bytes (consistent) are required for the transfer area for input data.

**Data to be received:**

A total of 12 bytes (consistent) is required for the transfer area for input data; 6 bytes (consistent) are required for the transfer area for output data.

###### Procedure for configuration

The procedure for configuring safety-related master-master communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Switch to the network view of the hardware and network editor.
3. Select a DP/DP coupler from "Other field devices\PROFIBUS DP\Gateways\Siemens AG\DP/DP Coupler" in the "Hardware catalog" task card and insert it into the network view of the hardware and network editor.
4. Insert a second DP/DP coupler.
5. Connect a DP interface of F-CPU 1 to the DP interface of a DP/DP coupler and a DP interface of F-CPU 2 to the DP interface of the other DP/DP coupler.

   ![Procedure for configuration](images/90978556171_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/90978556171_DV_resource.Stream@PNG-en-US.png)
6. A free PROFIBUS address is assigned automatically in the properties of the DP/DP-coupler in the device view. You must set this address on the DP/DP coupler, either via the DIP switch on the device or in the configuration of the DP/DP coupler (see [DP/DP Coupler](http://support.automation.siemens.com/WW/view/en/1179382) manual).
7. Switch to the device view of the DP/DP coupler PLC1 for bidirectional communication connections i.e. where each F-CPU should both send and receive data. Select the following modules from the "Hardware catalog" task card (with filter activated), and insert them in the "Device overview" tab of the DP/DP coupler:

   - One "6 bytes I/12 bytes Q consistent" module, and
   - One "12 bytes I/6 bytes Q consistent" module

   ![Procedure for configuration](images/103743061643_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/103743061643_DV_resource.Stream@PNG-en-US.png)
8. Select the following modules from the "Hardware catalog" task card (with filter activated) in the device view of DP/DP coupler PLC2, and insert them in the "Device overview" tab:

   - One "12 bytes I/6 bytes Q consistent" module, and
   - One "6 bytes I/12 bytes Q consistent" module

   ![Procedure for configuration](images/103743095947_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/103743095947_DV_resource.Stream@PNG-en-US.png)

**Note**

The transfer areas are assigned on the basis of the hardware identifier which is automatically assigned to the modules and devices. You need the HW identifier to program the SENDDP and RCVDP blocks (LADDR input). A system constant is created in the corresponding F-CPU for each hardware identifier of the transfer area. You can assign these system constants symbolically to the SENDDP and RCVDP blocks.

##### Safety-related master-master communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/50195421323_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F-CPUs of the DP master uses the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type BOOL or INT (DINT as alternative).

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

You can also call up the RCVDP and SENDDP instructions in separate F-FBs/F-FCs which you have to call up at the start or the end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Program safety-related master-master communication

###### Requirement for programming

The address areas for input and output data for the DP/DP coupler must be configured.

###### Programming procedure

You program safety-related master-master communication as follows:

| Symbol | Meaning |
| --- | --- |
| 1. In the safety program from which data is to be sent, call the [SENDDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for sending at the end of the main safety block or a separate F-FC/F-FB. 2. In the safety program in which data is to be received, call the [RCVDP instruction](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) for receiving at the start of the main safety block or a separate F-FC/F-FB. 3. Assign the HW identifiers for the output and input data of the DP/DP coupler configured in the hardware and network editor (constant in the tag table) to the respective LADDR inputs.    You must carry out this assignment for every communication connection for each of the F-CPUs involved. 4. Assign the value for the respective F-communication ID to the DP_DP_ID inputs. This establishes the communication relationship between the SENDDP instruction in one F-CPU and the RCVDP instruction in the other F-CPU: The associated instructions receive the same value for DP_DP_ID.    The figure below contains an example of how to specify the F-communication IDs at the inputs of the SENDDP and RCVDP instructions for 5 safety-related master-master communications relationships.               ![Programming procedure](images/166649837067_DV_resource.Stream@PNG-en-US.png)         ![Programming procedure](images/166649837067_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program. You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |     * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).    ** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".    *** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase. 5. Supply the SD_BO_xx and SD_I_xx inputs (SD_DI_00 as alternative) of SENDDP with the send signals. To cut down on intermediate signals when transferring block parameters, you can write the value directly to the instance DB of SENDDP using fully qualified access (for example, "Name SENDDP_1".SD_BO_02) before calling SENDDP. 6. Supply the RD_BO_xx and RD_I_xx outputs (RD_DI_00 as alternative) of RCVDP with the signals that you want to process further in other program sections or use fully qualified access to read the received signals directly in the associated instance DB in the program sections to be processed further (e.g., "Name RCVDP_1".RD_BO_02). 7. If you want to send the data at the SD_DI_00 input instead of the data at the SD_I_00 and SD_I_01 inputs, supply the DINTMODE input (initial value = "FALSE") of SENDDP with TRUE. 8. Supply the SUBBO_xx and SUBI_xx or alternatively SUBDI_00 inputs of RCVDP with the fail-safe values that are to be output by RCVDP in place of the process data until communication is established for the first time after startup of the sending and receiving F-systems or in the event of an error in safety-related communication.    - Specification of constant fail-safe values:      For data of data type INT/DINT, you can enter constant fail-safe values directly as constants in the SUBI_xx or alternatively SUBDI_00 input (initial value = "0"). If you want to specify a constant fail-safe value "TRUE" for data of the data type BOOL, set TRUE for the SUBBO_xx input (initial value = "FALSE").    - Specification of variable substitute values:      If you want to specify variable substitute values, define a tag that you calculate through your safety program in an F‑DB and specify this tag (fully qualified) in the SUBBO_xx or SUBI_xx or alternatively SUBDI_00 input.        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | Note: The program logic for calculating variable substitute values can only be inserted after the RCVDP calls, because there must be no program logic before the RCVDP calls. This is why the initial values of the substitute values are active in all RCVDP instructions in the first cycle after a startup of the F-system. You must therefore assign appropriate initial values for these tags. (S017) |  | 9. Configure the TIMEOUT inputs of the RCVDP and SENDDP instructions with the required monitoring time.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |     Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times). 10. Optional: Evaluate the ACK_REQ output of the RCVDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether user acknowledgment is required. 11. Supply the ACK_REI input of the RCVDP instruction with the acknowledgment signal for reintegration. 12. Optional: Evaluate the SUBS_ON output of the RCVDP or SENDDP instruction in order to query whether the RCVDP instruction is outputting the fail-safe values assigned in the SUBBO_xx and SUBI_xx or alternatively SUBDI_00 inputs. 13. Optional: Evaluate the ERROR output of the RCVDP or SENDDP instruction, for example, in the standard user program or on the operator control and monitoring system in order to query or to indicate whether a communication error has occurred. 14. Optional: Evaluate the SENDMODE output of the RCVDP instruction in order to query whether the F-CPU with the associated SENDDP instruction is in [disabled safety mode](#disabling-safety-mode-1). |  |

##### Safety-related master-master communication:Limits for data transfer

> **Note**
>
> If the data quantities to be transmitted exceed the capacity of the SENDDP / RCVDP correlated instructions, a second (or third) SENDDP / RCVDP call can be used. This requires configuration of an additional connection via the DP/DP coupler. Whether or not this is possible with one single DP/DP coupler depends on the capacity restrictions of the DP/DP coupler.

#### Safety-related IO controller-I-device communication

This section contains information on the following topics:

- [Configuring safety-related communication between IO controller and I-device](#configuring-safety-related-communication-between-io-controller-and-i-device-1)
- [Safety-related IO controller-I-device communication via SENDDP and RCVDP](#safety-related-io-controller-i-device-communication-via-senddp-and-rcvdp-1)
- [Programming safety-related IO controller I-device communication](#programming-safety-related-io-controller-i-device-communication-1)
- [Safety-related IO-Controller-IO-Device communication - Limits for data transfer](#safety-related-io-controller-io-device-communication---limits-for-data-transfer-1)

##### Configuring safety-related communication between IO controller and I-device

###### Introduction

Safety-related communication between the safety program of the F‑CPU of an IO controller and the safety program(s) of the F‑CPU(s) of one or more I-devices takes place via IO controller-I‑device transfer areas (F**‑**CD) in PROFINET IO, as in standard systems.

You do not need any additional hardware for IO controller-I‑device communication.

###### Configuring transfer areas

For every safety-related communication connection between two F-CPUs, you must configure transfer areas in the hardware and network editor. The figure below shows how both of the F-CPUs are able to send and receive data (bidirectional communication).

![Configuring transfer areas](images/90463255947_DV_resource.Stream@PNG-en-US.png)

The transfer area is assigned a label when it is created to identify it as the communication relationship. For example, "F-CD_PLC_2 PLC_1_1" for the first F-CD connection between IO controller F-CPU 1 and I-device F-CPU 2.

When you create a transfer area, a system constant with the name of the transfer area is created in the F-CPU of the IO controller and in the F-CPU of the I-device. The system constant contains the hardware identifier of the transfer area for the corresponding F-CPU.

You assign the hardware identifier (system constant from the default tag table) of the transfer areas symbolically to the LADDR input of the SENDDP and RCVDP instructions in the safety programs.

###### Procedure for configuration

The procedure for configuring safety-related IO controller-I-device communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. Enable the "IO Device" mode for F-CPU 2 in the properties of its PN interface and assign this PN interface to a PN interface of F-CPU 1.
3. Select the PROFINET interface of F‑CPU 2. Under "Transfer areas", you create an F‑CD connection (type "F-CD") for receiving from the IO controller (←). The F‑CD connection is shown in yellow in the table and the address areas in the I-device and IO controller assigned are displayed.

   In addition, an acknowledgment connection is created automatically for each F‑CD connection. (see "Transfer area details").
4. Create an additional F-CD connection for sending to the IO controller.
5. In the transfer area you just created, click on the arrow to change the transfer direction to sending to the IO controller (←).

   ![Procedure for configuration](images/103743184907_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/103743184907_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> You can assign up to four IO controllers in separate projects to the shared I-device, as in standard systems. To do this, export the I-device as a GSD file and import the GSD file into the projects of the IO controllers. Proceed as described in the STEP 7 help under "Configuring an I-device as a shared device".

###### Procedure for configuring an S7-1500 F-CPU with firmware V3.1 or higher as an I-device

The procedure for configuring safety-related IO controller-I-device communication is identical to that in the standard system.

Proceed as follows:

1. Insert any SIMATIC S7-1200/1500 F-CPU from the "Hardware catalog" task card into the project as F-CPU 1.
2. Insert an S7-1500 F‑CPU with firmware V3.1 or higher from the "Hardware catalog" task card into the project as F-CPU 2 (I-device).
3. Enable the "IO Device" mode for F-CPU 2 in the properties of its PN interface and assign this PN interface to a PN interface of F-CPU 1.
4. Assign F-CPU 1 as an IO controller under "Assigned IO controllers".
5. Under "Transfer areas", you create an F‑CD connection (type "F-CD") for receiving from the IO controller (←). The F‑CD connection is shown in yellow in the table and the address areas in the I-device and IO controller assigned are displayed.

   In addition, an acknowledgment connection is created automatically for each F‑CD connection. (see "Transfer area details").
6. Create an additional F-CD connection for sending to the IO controller.
7. In the transfer area you just created, click on the arrow to change the transfer direction to sending to the IO controller (←).

   ![Procedure for configuring an S7-1500 F-CPU with firmware V3.1 or higher as an I-device](images/172670312203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuring an S7-1500 F-CPU with firmware V3.1 or higher as an I-device](images/172670312203_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Shared I-device**
>
> If you use S7-1500 F-CPUs with Firmware V3.1 or higher as an IO controller, you can share different transfer areas of an I-device (S7-1500 F-CPU with Firmware V3.1 or higher) between two IO controllers within the project.
>
> To do this, assign the I-device to a second IO controller under "Assigned IO controllers". Select the desired IO controller (partner) for each transfer area.
>
> More information can be found in the STEP 7 help.

> **Note**
>
> You can assign up to two more IO controllers in separate projects to the shared I-device, as in standard systems. To do this, export the I-device as a GSD file and import the GSD file into the projects of the IO controllers. Proceed as described in the STEP 7 help under "Configuring an I-device as a shared device".

##### Safety-related IO controller-I-device communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/50195564811_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F‑CPUs of the IO controller and an I‑device makes use of the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of data of the data type BOOL or INT (DINT as alternative).

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

You can also call up the RCVDP and SENDDP instructions in separate F-FBs/F-FCs which you have to call at the start or end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Programming safety-related IO controller I-device communication

###### Requirement for programming

The transfer areas must be configured.

###### Programming procedure

The procedure for programming safety-related IO controller-I‑device communication is the same as that for programming safety-related IO controller-IO controller communication (see [Program safety-related IO controller-IO controller communication](#program-safety-related-io-controller-io-controller-communication-1)).

The assignment of the HW identifiers (system constants in the standard tag table) of the transfer areas to the LADDR input of the SENDDP/RCVDP instructions can be obtained from the following table:

| Instruction | HW identifier |
| --- | --- |
| SENDDP in the IO controller | Hardware identifier of the transfer area in the IO controller |
| RCVDP in the IO controller | Hardware identifier of the transfer area in the IO controller |
| SENDDP in the I-device | Hardware identifier of the transfer area in the I-device |
| RCVDP in the I-device | Hardware identifier of the transfer area in the I-device |

The figure below contains an example of how to specify the F-communication IDs for the inputs of the SENDDP and RCVDP instructions for 4 safety-related IO controller-I‑device communication relationships.

![Programming procedure](images/166650268043_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide**** at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".

*** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase.

**** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one single F-CPU with regard to the DP_DP_ID.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time.(S018) |  |

Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times).

##### Safety-related IO-Controller-IO-Device communication - Limits for data transfer

###### Limits for data transfer

If the amount of data to be transferred is greater than the capacity of related SENDDP/RCVDP instructions, you can use additional SENDDP/RCVDP instructions. Configure additional transfer areas for this purpose. Remember the maximum limit of 1440 bytes of input data or 1440 bytes of output data for transfer between an I-device and a IO controller.

The following table shows the amount of output and input data assigned in safety-related communication connections:

| Safety-related communication | Communication connection | Assigned input and output data |  |  |  |
| --- | --- | --- | --- | --- | --- |
| In the IO controller |  | In the I-device |  |  |  |
| Output data | Input data | Output data | Input data |  |  |
| IO controller-I‑Device | **Sending:**   I‑Device 1 to IO controller | 6 bytes | 12 bytes | 12 bytes | 6 bytes |
| **Receiving:**   I‑Device 1 from IO controller | 12 bytes | 6 bytes | 6 bytes | 12 bytes |  |

Consider all additional configured safety-related and standard communication connections (transfer areas of type F‑CD and CD) for the maximum limit of 1440 bytes of input data or 1440 bytes of output data for transfer between an I-device and an IO controller. In addition, data are assigned for internal purposes such that the maximum limit may be reached sooner.

When the limit is exceeded, a corresponding error message is displayed.

You can find more information on the transfer areas in the STEP 7 help under "Rules for creating transfer areas".

#### Safety-related master-I-slave communication

This section contains information on the following topics:

- [Configuring safety-related master-I-slave communication](#configuring-safety-related-master-i-slave-communication-1)
- [Safety-related master-I-slave communication via SENDDP and RCVDP](#safety-related-master-i-slave-communication-via-senddp-and-rcvdp)
- [Programming safety‑related master-I‑slave communication](#programming-safety-related-master-i-slave-communication)
- [Limits for data transfer of safety-related master-I-slave communication](#limits-for-data-transfer-of-safety-related-master-i-slave-communication)

##### Configuring safety-related master-I-slave communication

###### Introduction

Safety-related communication between the safety program of the F‑CPU of a DP master and the safety program(s) of the F‑CPU(s) of one or more I-slaves takes place via master-I‑slave transfer areas (**F‑**MS), as in standard systems.

You do not need a DP/DP coupler for master-I-slave communication.

###### Configuring transfer areas

For every safety-related communication connection between two F-CPUs, you must configure transfer areas in the hardware and network editor. The figure below shows how both of the F-CPUs are able to send and receive data (bidirectional communication).

![Configuring transfer areas](images/166479364235_DV_resource.Stream@PNG-en-US.png)

The transfer area is assigned a label when it is created to identify it as the communication relationship. For example, "F-MS_PLC_2-PLC_1_1" for the first F-MS connection between DP master F-CPU 1 and I-slave F-CPU 2.

When you create a transfer area, a system constant with the name of the transfer area is created in the F-CPU of the DP master and in the F-CPU of the I-slave. The system constant contains the hardware identifier of the transfer area for the corresponding F-CPU.

You assign the hardware identifier (system constant from the default tag table) of the transfer areas symbolically to the LADDR input of the SENDDP and RCVDP instructions in the safety programs.

###### Procedure for configuration

The procedure for configuring safety-related master-I-slave communication is identical to that in the standard system.

Proceed as follows:

1. Insert two F-CPUS from the "Hardware catalog" task card into the project.
2. If the F-CPU which is to be operated as DP master (F-CPU 1) does not have an integrated PROFIBUS DP interface, insert an PROFIBUS-CM, for example.
3. From the device view of the F-CPUs which are to be operated as I-slaves (F-CPU 2), insert a suitable CM DP module or CP DP module.
4. If necessary, enable "DP‑slave" (I‑slave) mode in the properties for the CM/CP DP module.
5. Assign the DP interface of the CM/CP to a DP interface of F‑CPU 1.
6. Select the PROFIBUS interface of F‑CPU 2 or of the CM. Under "Transfer areas", you create an F‑MS connection (type "F‑MS") for sending to the DP master (←). The F‑MS connection is shown in yellow in the table and the assigned transfer areas in the I-slave and DP master are displayed.

   In addition, an acknowledgment connection is created automatically for each F‑MS connection. (see "Transfer area details").
7. Create an additional F-MS connection for receiving from the DP master.
8. In the transfer area you just created, click the arrow in order to change the transfer direction to receiving from DP master (→).

   ![Procedure for configuration](images/103743813259_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuration](images/103743813259_DV_resource.Stream@PNG-en-US.png)

##### Safety-related master-I-slave communication via SENDDP and RCVDP

###### Communication via SENDDP and RCVDP instructions

![Communication via SENDDP and RCVDP instructions](images/68477168907_DV_resource.Stream@PNG-en-US.png)

Safety-related communication between the F‑CPUs of the DP master and an I‑slave makes use of the SENDDP and RCVDP instructions for sending and receiving, respectively. These can be used to perform a fail-safe transfer of a fixed amount of fail-safe data of the data type BOOL or INT (DINT as alternative).

You can find these instructions in the "Instructions" task card under "Communication". The RCVDP instruction **must** be called at the start of the main safety block. The SENDDP instruction **must** be called at the end of the main safety block.

You can also call the RCVDP and SENDDP instructions in separate F-FBs/F-FCs which you have to call up at the beginning or end of the main safety block.

Note that the send signals are not sent until after the SENDDP instruction call at the end of execution of the relevant F-runtime group.

A detailed description of the SENDDP and RCVDP instructions can be found in [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19).

##### Programming safety-related master-I-slave communication

###### Requirements

The transfer areas must be configured.

###### Programming procedure

The procedure for programming safety-related master-I-slave communication is the same as that for programming safety-related master-master communication (see [Safety-related master-master communication](#safety-related-master-master-communication-1)).

The assignment of the HW identifiers of the transfer areas to the LADDR input of the SENDDP/RCVDP instructions can be obtained from the following table.

| Instruction | HW identifier |
| --- | --- |
| SENDDP in the DP master | Hardware identifier of the respective transfer area in the DP master |
| RCVDP in the DP master | Hardware identifier of the respective transfer area in the DP master |
| SENDDP in the I-slave | Hardware identifier of the transfer area in the I-slave |
| RCVDP in the I-slave | Hardware identifier of the transfer area in the I-slave |

The figure below contains an example of how to specify the F-communication IDs at the inputs of the SENDDP and RCVDP instructions for four safety-related master-I-slave communication relationships.

![Programming procedure](images/166655148811_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".

*** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |

Information on calculating the monitoring times can be found in [Monitoring and response times](#monitoring-and-response-times).

##### Limits for data transfer of safety-related master-I-slave communication

###### Limits for data transfer

If the amount of data to be transferred is greater than the capacity of related SENDDP/RCVDP instructions, you can use additional SENDDP/RCVDP instructions. Configure additional transfer areas for this purpose. Note the maximum limit of 244 bytes of input data or 244 bytes of output data for transfer between an I-slave and a DP master.

The following table shows the amount of output and input data assigned in safety-related communication connections:

| Safety-related communication | Communication connection | Assigned input and output data |  |  |  |
| --- | --- | --- | --- | --- | --- |
| DP master |  | I-slave |  |  |  |
| Output data | Input data | Output data | Input data |  |  |
| Master-I-slave | **Sending:**   I-slave 1 to DP master | 6 bytes | 12 bytes | 12 bytes | 6 bytes |
| **Receiving:**   I-slave 1 from DP master | 12 bytes | 6 bytes | 6 bytes | 12 bytes |  |

Consider all additional configured safety-related and standard communication connections (transfer areas of type F‑MS-, F‑DX-, F‑DX-Mod., MS-, DX- and DX-Mod) for the maximum limit of 244 bytes of input data or 244 bytes of output data for transfer between an I-device and a DP master F‑MS and MS). If the maximum limit of 244 bytes of input data or 244 bytes of output data is exceeded, you will receive a corresponding error message.

#### Safety-related IO controller-I-slave communication

This section contains information on the following topics:

- [Safety-related IO controller-I-slave communication](#safety-related-io-controller-i-slave-communication-3)

##### Safety-related IO controller-I-slave communication

###### Introduction

Safety-related communication between the safety program of the F‑CPU of an IO controller and the safety program(s) of the F‑CPU(s) of one or more I-slaves takes place via master‑I-slave transfer areas (**F‑**MS), as in standard systems.

###### IE/PB link

For the safety-related IO-controller-I-slave communication, the IE/PB link is mandatory. Each of the two F-CPUs is linked to the IE/PB link by means of its PROFIBUS DP or PROFINET-interface.

> **Note**
>
> If you are using an IE/PB link, you must take this into account when configuring the F-specific monitoring times and when calculating the maximum response time of your F-system (see also [Monitoring and response times](#monitoring-and-response-times)).
>
> Note that the [Excel file for calculating response times](https://support.industry.siemens.com/cs/ww/en/view/109783831) for S7-300/400 F-CPUs does not support all conceivable configurations.

###### Reference

The information on safety-related master-I-slave communication in [Safety-related master-I-slave communication](#safety-related-master-i-slave-communication-1) also applies.

#### Safety-related communication to S7 F-System S7 Distributed Safety

This section contains information on the following topics:

- [Introduction](#introduction-3)
- [Communication with S7 Distributed Safety via PN/PN coupler (IO controller-IO controller communication)](#communication-with-s7-distributed-safety-via-pnpn-coupler-io-controller-io-controller-communication-1)
- [Communication with S7 Distributed Safety via DP/DP coupler (master-master communication)](#communication-with-s7-distributed-safety-via-dpdp-coupler-master-master-communication-1)

##### Introduction

Safety-related communication from F-CPUs in SIMATIC Safety to F‑CPUs in S7 Distributed Safety F-systems is possible, via a PN/PN coupler or DP/DP coupler that you use between the two F-CPUs, as IO controller-IO controller communication or master-master communication.

##### Communication with S7 Distributed Safety via PN/PN coupler (IO controller-IO controller communication)

Communication functions between SENDDP/RCVDP instructions at the STEP 7 Safety end and F-application blocks F_SENDDP/F_RCVDP at the S7 Distributed Safety end:

![Figure](images/60219855883_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the S7 Distributed Safety end

At the S7 Distributed Safety end, proceed as described in "Safety-related IO controller-IO controller communication" in the [S7 Distributed Safety - Configuring and Programming](http://support.automation.siemens.com/WW/view/en/22099875) manual.

###### Procedure at the STEP 7 Safety end

At the STEP 7 Safety end, proceed as described in [Safety-related IO controller-IO controller communication](#safety-related-io-controller-io-controller-communication-1).

##### Communication with S7 Distributed Safety via DP/DP coupler (master-master communication)

Communication functions between SENDDP/RCVDP instructions at the STEP 7 Safety end and F-application blocks F_SENDDP/F_RCVDP at the S7 Distributed Safety end:

![Figure](images/60219888267_DV_resource.Stream@PNG-en-US.png)

###### Procedure at the S7 Distributed Safety end

At the S7 Distributed Safety end, proceed as described in "Safety-related master-master communication" in the [S7 Distributed Safety - Configuring and Programming](http://support.automation.siemens.com/WW/view/en/22099875) manual.

###### Procedure at the STEP 7 Safety end

At the STEP 7 Safety end, proceed as described in [Safety-related master-master communication](#safety-related-master-master-communication-1).

### Configuring and programming communication with Flexible F-Link (S7-1200, S7-1500)

This section contains information on the following topics:

- [Flexible F-Link](#flexible-f-link)
- [F-communication DB (S7-1200, S7-1500)](#f-communication-db-s7-1200-s7-1500)

#### Flexible F-Link

##### Introduction

The fail-safe CPU-CPU communication "Flexible F-Link" is available for S7-1200 and S7-1500 F-CPUs. This means fail-safe data can be easily exchanged as fail-safe arrays with standard communication mechanisms between F-CPUs.

Flexible F-Link offers a series of advantages for exchanging fail-safe data:

- Collection of fail-safe data to be transmitted in F-compliant PLC data types (UDTs)

  (Nested F-compliant PLC data types (UDT) are not supported.)
- Up to 100 bytes of fail-safe data per UDT
- Easy parameter assignment and automatic generation of fail-safe communication DBs
- Transmission of fail-safe data with standard communication blocks also across network limits
- [F-runtime group communication](#flexible-f-link-area-s7-1200-s7-1500) for F-CPUs 1200/1500
- System-integrated and globally sufficiently unique F-communication UUID
- Separate F-communication address signature for easy detection of changes to the F-communication UUID

##### Requirement

- S7-1500 F-CPUs as of firmware V2.0
- S7-1200 F-CPUs as of firmware V4.2
- As of safety system version V2.2

##### Principles of communication via Flexible F-Link

![Principles of communication via Flexible F-Link](images/170244467339_DV_resource.Stream@PNG-en-US.png)

Proceed as follows on the **send side**:

1. Create an F-compliant PLC data type (UDT) for the data to be sent. The size is up to 100 bytes.
2. Create safety-related communication with the "Send" direction in the [Safety Administration Editor](#flexible-f-link-area-s7-1200-s7-1500).

   A new [F-communication DB](#f-communication-db-s7-1200-s7-1500) is created for the safety-related communication under "Program blocks\System blocks\STEP 7 Safety\F-communication DBs".
3. Set the [F-monitoring time](#response-times-of-safety-functions) for the safety-related communication.
4. In the safety program, supply the tags for the send data (SEND_DATA) at the [F-communication DB](#f-communication-db-s7-1200-s7-1500) of the safety-related communication.
5. Create standard blocks in which the fail-safe arrays created automatically in the F-communication DB are sent with the send data and received with the acknowledgment data. For processing the process values in the correct chronological order, you can make use of the F-OB [Pre-/post-processing](#pre-postprocessing-s7-1200-s7-1500). When using the communication instructions, ensure that the fail-safe arrays are available consistently at the time of evaluation and that the [F-monitoring time](#response-times-of-safety-functions) is observed. Observe the note below.

Proceed as follows on the **receive side**:

1. Create an F-compliant PLC data type (UDT) with the same structure as on the send side.

   To do so, copy the F-compliant PLC data type (UDT) from the send side or use the project library or global library.
2. Create safety-related communication with the "Receive" direction in the [Safety Administration Editor](#flexible-f-link-area-s7-1200-s7-1500).

   A new F-communication DB is created for the safety-related communication under "Program blocks\System blocks\STEP 7 Safety\F-communication DBs".
3. Copy the F-communication UUID of the safety-related communication from the send side.
4. Set the same F-monitoring time as for the send side.
5. In the safety program, evaluate the tags for the receive data (RCV_DATA) at the [F-communication DB](#f-communication-db-s7-1200-s7-1500).
6. Create standard blocks in which the fail-safe arrays automatically created in the F-communication DB are received with the receive data and sent with the acknowledgment data. For processing the process values in the correct chronological order, you can make use of the F-OB [Pre-/post-processing](#flexible-f-link-area-s7-1200-s7-1500). When using the communication instructions, ensure that the fail-safe arrays are available consistently at the time of evaluation and that the [F-monitoring time](#response-times-of-safety-functions) is observed. Observe the note below.

> **Note**
>
> When using non-deterministic communication protocols (e.g. TCP/IP), you must take into account the following:
>
> - Increased communication load can fundamentally impair the availability of your application (runtime of the F-monitoring time of the F-communication connection). This holds true especially when OPC UA and Secure Open User Communication (OUC) are used in parallel.
> - Communication buffer overflows can adversely affect the availability of your application and should be avoided.
>
>   Refer to the following application example for more helpful information: "[Configuring Flexible F-Link Communication](https://support.industry.siemens.com/cs/ww/en/view/109768964)".

> **Note**
>
> During simulation with S7-PLCSIM, the timer that generates an error message after expiration when communication with real I/Os is interrupted (e.g. by setting a CPU to STOP) is not triggered. This is why no error message is displayed in this case. It is displayed as soon as the connection has been restored. Following user acknowledgment, the current values are once again sent and received.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When data is sent from an F-CPU simulated with S7-PLCSIM using safety-related CPU-CPU communication with Flexible F-Link, you can no longer assume that this data is generated safely. You can, for example, output safe substitute values in place of the received data in the receiving F-CPU by evaluating the SENDMODE tag.   (S086) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When a new Flexible F-Link communication is created in the Safety Administration Editor, a unique F-communication UUID for the communication is provided by the system. By copying communications in the Safety Administration Editor within the parameterization table or when copying to another F-CPU, the F-communication UUIDs are not regenerated and are therefore not unique anymore. If the copy is used to configure a new communication relationship, you yourself must ensure the uniqueness. To do this, select the affected UUIDs and regenerate via the "Generate UUID" shortcut menu. The uniqueness must be checked in the safety summary during acceptance. (S087) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For each communication connection via Flexible F-Link, you must check that the offsets of the elements of the F-compliant PLC data type (UDT) used for the communication connection match on the transmit and receive sides when you accept the safety program.    You can find the offsets in the respective safety summary. To do this identify the communication connection by means of the UUID. (S088) |  |

---

**See also**

[F-runtime group communication (S7-1200, S7-1500)](#f-runtime-group-communication-s7-1200-s7-1500)

#### F-communication DB (S7-1200, S7-1500)

##### F-communication DB for sending

The following table shows you the interface of the F-communication DB for the communication connection with the direction "Send":

| Section | Name | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| Input | SEND_DATA | F-compliant PLC data type (UDT) | As in the F-compliant PLC data type (UDT). | User data to be sent. |
| ACK_RCV_ARRAY | Array[0..n] of Byte | Each element with 16#0 | Array with the received raw data. |  |
| Output | ERROR | BOOL | False | Signals currently pending communication errors or communication errors not acknowledged yet at the receiver (not in the initial start).  1=Communication error |
| ACTIVATE_FV | BOOL | True | Communication passivated, in the initial start (for example receiver not started), or HOST sends ACTIVATE_FV. DEVICE sends status bit: FV_ACTVATED, but no 0-values.   1=The communication uses fail-safe values |  |
| DIAG | Byte | 16#0 | Error bits (Timeout or CRC error currently still pending, or communication after error not depassivated yet)   Bit 3: Acknowledgement request active at the receiver  Bit 4: Timeout detected  Bit 6: CRC error detected |  |
| SEND_ARRAY | Array[0..n] of Byte | Each element with 16#0 | Array with the raw data to be sent. |  |
| ACK_RCV_LENGTH | UInt | 0 | Length information to ACK_RCV_ARRAY in bytes |  |
| SEND_LENGTH | UInt | 0 | Length information to SEND_ARRAY in bytes |  |
| InOut | — | — | — | — |
| Static | — | — | — | — |

##### F-communication DB for receiving

The following table shows you the interface of the F-communication DB for the communication connection with the direction "Receive":

| Section | Name | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| Input | PASS_ON | BOOL | False | This way you can passivate the output data (output of the passivation values)  1=Enable passivation |
| ACK_REI | BOOL | False | Reintegration (in case of reintegration request) by means of positive edge  1=Acknowledgment for reintegration |  |
| RCV_ARRAY | Array[0..n] of Byte | Each element with 16#0 | Array with the received raw data |  |
| Output | RCV_DATA | F-compliant PLC data type (UDT) | As in the F-compliant PLC data type (UDT). | Output data (PASS_VALUES or data received). |
| ERROR | BOOL | False | Signals currently pending communication errors or communication errors not acknowledged yet (not in the initial start).   1=Communication error |  |
| PASS_OUT | BOOL | True | At PASS_OUT=1 the PASS_VALUES are output   Could be: ERROR, PASS_ON, in the initial start (e.g. sender not started), or ACK_REQ is pending (error not acknowledged) |  |
| ACK_REQ | BOOL | False | Reintegration requirement (communication stable again after error, substitute values are still output)   1=Acknowledgment request for reintegration |  |
| SENDMODE | BOOL | False | MOD_MODE is active or communication with PLCSIM Advanced on the sending F-CPU  1=F-CPU with a sender in the deactivated safety operation or on a simulated CPU |  |
| DIAG | Byte | 16#0 | Error bits (Timeout or CRC error)  Bit 0: Timeout detected by the sender   Bit 1: Communication error currently pending in the sender   Bit 2: CRC error detected by the sender   Bit 4: Timeout detected by the receiver   Bit 6: CRC error detected by the receiver |  |
| ACK_SEND_ARRAY | Array[0..n] of Byte | Each element with 16#0 | Array with the raw data to be sent. |  |
| RCV_LENGTH | UInt | 0 | Length information of RCV_ARRAY in bytes |  |
| ACK_SEND_LENGTH | UInt | 0 | Length information of ACK_SEND_ARRAY in bytes |  |
| InOut | — | — | — | — |
| Static | PASS_VALUES | F-compliant PLC data type (UDT) | Same as the F-compliant PLC data type (UDT) or in the I/O DB | Passivation or substitute values |

### Configuring and programming communication between S7-300/400 and S7-1200/1500 F-CPUs

This section contains information on the following topics:

- [Overview of communication](#overview-of-communication-2)

#### Overview of communication

##### Introduction

This section provides an overview of the options for safety-related communication between S7-300/400 and S7-1200/1500 F-CPUs in SIMATIC Safety F‑systems.

##### Options for safety-related communication

| Safety-related communication | On subnet | Additional hardware required |
| --- | --- | --- |
| **Safety-related CPU-CPU communication:** |  |  |
| Master‑master communication | PROFIBUS DP | DP/DP coupler |
| Master-I-slave communication | PROFIBUS DP | — |
| IO controller-IO controller communication | PROFINET IO | PN/PN coupler |
| IO controller-I-device communication | PROFINET IO | — |
| IO controller-I-slave communication | PROFINET IO and PROFIBUS DP | IE/PB link |

##### Basic procedure for configuring and programming

Configure and program safety-related communication between S7-300/400 F-CPUs and S7-1200/1500 F-CPUs as described in [Configuring and programming communication (S7-300, S7-400)](#configuring-and-programming-communication-s7-300-s7-400) and [Configuring and programming communication (S7-1200, S7-1500)](#configuring-and-programming-communication-s7-1200-s7-1500) for your application.

To program an S7-300/400 F-CPU, use the start addresses of the transfer areas. To program an S7-1200/1500 F-CPU, use the HW identifiers of the transfer areas.

### Configuring and programming communication in several projects

This section contains information on the following topics:

- [Safety-oriented IO Controller I device communication in several projects](#safety-oriented-io-controller-i-device-communication-in-several-projects)

#### Safety-oriented IO Controller I device communication in several projects

This section contains information on the following topics:

- [Configuring safety-related communication between IO controller and I-device](#configuring-safety-related-communication-between-io-controller-and-i-device-2)
- [Programming safety-related IO Controller I-device communication](#programming-safety-related-io-controller-i-device-communication-2)

##### Configuring safety-related communication between IO controller and I-device

###### Introduction

Safety-related communication between the safety program of the F‑CPU of an IO controller and the safety program(s) of the F‑CPU(s) of one or more I-devices takes place via IO controller-I‑device transfer areas (F**‑**CD) in PROFINET IO, as in standard systems.

The following section describes particular aspects when the IO Controller and the I-device are located in different projects.

###### Requirement

- The IO Controller is an S7-1200/1500 F-CPU that supports the IO Controller functionality.
- The I-device is an S7-300/400/1200/1500 F-CPU that supports the I-device functionality.
- The project in which the I-device is located, must have been created with S7 Distributed Safety V5.4, STEP 7 Safety V13 or later.

###### Configuring

1. Configure the safety-related communication in the project with the I-device as described under "[Configuring safety-related communication between IO controller and I-device](#configuring-safety-related-communication-between-io-controller-and-i-device)" (S7-300, S7-400) or "[Configuring safety-related communication between IO controller and I-device](#configuring-safety-related-communication-between-io-controller-and-i-device-1)" (S7-1200, S7-1500) respectively. In this case the F-CPU 1 (IO Controller) is only a placeholder for the F-CPU in the project of the IO Controller.
2. Export the I-device as a GSD file. Proceed as described in the STEP 7 help under "Configuring an I-device".
3. Import the GSD file in the project with the IO Controller. Proceed as described in the STEP 7 help under "Installing a GSD file".
4. Insert the I-device from the "Hardware catalog" task card into the project with the IO Controller.
5. Assign the F-CPU of the IO Controller to the I-device.

**Note**

When creating with STEP 7 Safety < V14 SP1 avoid a subsequent change from the transfer areas from CD to F-CD.

When creating with S7 Distributed SafetyV5.4 create the application transfer areas of the address type "Output" and "Input" directly after each other.

![Configuring](images/170246018187_DV_resource.Stream@PNG-en-US.png)

##### Programming safety-related IO Controller I-device communication

###### Programming procedure

To program the safety-related communication between the IO controller and I-device for an F-CPU S7-300/400, analogously follow the procedure described under "[Safety-related IO controller-I-device communication via SENDDP and RCVDP](#safety-related-io-controller-i-device-communication-via-senddp-and-rcvdp)" and "[Programming safety-related IO controller I-device communication](#programming-safety-related-io-controller-i-device-communication)". To program an S7-300/400 F-CPU, use the start addresses of the transfer areas.

To program the safety-related communication between the IO controller and I-device for an F-CPU S7-1200/1500, analogously follow the procedure described under "[Safety-related IO controller-I-device communication via SENDDP and RCVDP](#safety-related-io-controller-i-device-communication-via-senddp-and-rcvdp-1)" and "[Programming safety-related IO controller I-device communication](#programming-safety-related-io-controller-i-device-communication-1)". To program an S7-1200/1500 F-CPU, use the HW identifiers of the transfer areas.

## Compiling and commissioning a safety program

This section contains information on the following topics:

- [Compiling the safety program](#compiling-the-safety-program)
- [Safety program work memory requirements (S7-300, S7-400)](#safety-program-work-memory-requirements-s7-300-s7-400)
- [Downloading project data](#downloading-project-data)
- [Program identification](#program-identification)
- [Comparing Safety Programs](#comparing-safety-programs)
- [Creating a safety summary](#creating-a-safety-summary)
- [Testing the safety program](#testing-the-safety-program)
- [F-change history](#f-change-history)

### Compiling the safety program

To get a consistent safety program, follow these steps:

1. Select the "Program blocks" folder or the Safety Unit folder or a higher level.
2. Start the compile.

   To do this, proceed essentially in the same way as when compiling a standard user program. You can start at various points to accomplish this in STEP 7. The basics for compiling user programs can be found in the Help on STEP 7.

> **Note**
>
> Please note that following a safety-related change to the hardware configuration that not only this, but also the safety program has to be recompiled and downloaded. This also applies for changes to the F-I/O which are not used in the safety program.

> **Note**
>
> The following applies for S7-300/400 F-CPUs:
>
> If you want to compile a know-how-protected F-block after a change, you must remove the know-how protection for this F-block before compiling.

#### Reporting compiling errors

You can recognize whether or not the compilation was successful based on the message in the inspector window under "Info > Compile", error messages and warnings are output.

For information on the procedure you must follow to eliminate compiling errors, see "Eliminating compiling errors" in the Help on STEP 7.

### Safety program work memory requirements (S7-300, S7-400)

#### Estimation

You can estimate the work memory requirement for the safety program as follows:

**Work memory required for the safety program**

| Symbol | Meaning |
| --- | --- |
| 32 KB for F-system blocks |  |
| + | 4.4 KB for safety-related communication between F-runtime groups |
| + | 4.5 x work memory requirement for all F-FB/F-FCs/main safety blocks |
| + | 4.5 x work memory requirement of all utilized instructions, which are shown in the "Instructions" task card with the ![Estimation](images/28389156363_DV_resource.Stream@PNG-de-DE.PNG) block icon.  (except SENDDP, RCVDP, SENDS7, and RCVS7) |
| + | Work memory requirement of the utilized SENDDP and RCVDP instructions (4.3 KB each) |
| + | Work memory requirement of the utilized SENDS7 and RCVS7 instructions (8.5 KB each) |

**Work memory required for data**

| Symbol | Meaning |
| --- | --- |
| 5 x work memory requirement for all F-DBs (including F-communication DB, but excluding DB for F-runtime group communication) and I-DBs for main safety block/F-FB |  |
| + | 24 x work memory requirement for all DBs for F-runtime group communication |
| + | 2.3 x work memory requirement for all I-DBs of instructions (except SENDDP, RCVDP, SENDS7 and RCVS7) |
| + | Work memory requirement of all I-DBs of instructions SENDDP (0.2 KB), RCVDP(0.3 KB), SENDS7 (0.6 KB), and RCVS7 (1.0 KB) |
| + | 0.7 KB per F-FC |
| + | 0.7 KB per F-I/O (for F-I/O DBs, etc.) |
| + | 4.5 KB |

#### Block size of automatically generated F-blocks

Do not utilize the entire maximum size of an F-block, because the automatically generated F-blocks are larger and as a result, the maximum possible size may be exceeded in the F-CPU. If the block size is exceeded, this triggers a corresponding error message with information on which F-blocks are too large. These must be divided up, if necessary.

### Downloading project data

This section contains information on the following topics:

- [Downloading project data to an F-CPU](#downloading-project-data-to-an-f-cpu)
- [Downloading project data to an S7-300/400 F-CPU](#downloading-project-data-to-an-s7-300400-f-cpu)
- [Downloading project data into an F-CPU S7-1200](#downloading-project-data-into-an-f-cpu-s7-1200)
- [Downloading project data to an S7-1500 F-CPU](#downloading-project-data-to-an-s7-1500-f-cpu)
- [Restoring a backup of the safety program to an F-CPU](#restoring-a-backup-of-the-safety-program-to-an-f-cpu)
- [Specifics on creating and installing an image file of an S7-1500 F Software Controller](#specifics-on-creating-and-installing-an-image-file-of-an-s7-1500-f-software-controller)
- [Load project data (including safety-related project data) from an F-CPU into a PG/PC (S7-1500)](#load-project-data-including-safety-related-project-data-from-an-f-cpu-into-a-pgpc-s7-1500)
- [Load project data (including safety-related project data) from a memory card into a PG/PC (S7-1500)](#load-project-data-including-safety-related-project-data-from-a-memory-card-into-a-pgpc-s7-1500)
- [Loading PC station via the configuration file (only FW < V30.0)](#loading-pc-station-via-the-configuration-file-only-fw-v300)

#### Downloading project data to an F-CPU

##### Introduction

Once you have successfully compiled your safety program, you can download it together with the standard application program to the F‑CPU.

(S7-1500) If the safety program is in a Safety Unit, you can load the Safety Unit independently into the F-CPU.

To download a safety program, you follow essentially the same approach as for downloading a standard user program, via different starting points in STEP 7.

- In the "Load preview" dialog, enter data (e.g. password for the F-CPU) and set the requirements for downloading (e.g. that the F-CPU is switched to STOP mode before downloading).
- The "Load results" dialog shows the results after loading.

We will show you the options for downloading the safety program later. For basic information on downloading, refer to the Help on STEP 7.

##### Rules for downloading the project data into an F-CPU

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) If **several F‑CPUs** can be reached via a network (such as Industrial Ethernet) by **the same programming device or PC**, you must take the following additional measures to ensure that the safety-related project data is downloaded to the correct F‑CPU:  Use passwords specific to each F‑CPU, such as a uniform password for the F‑CPUs with attached Ethernet address for each.  Note the following:  - A point-to-point connection must be used to activate the access protection of an F‑CPU when the hardware configuration is loaded for the first time (similar to assigning an MPI address to an F‑CPU for the first time). - Before downloading the safety-related project data to an F‑CPU, existing access permission for any other F‑CPU must first be cancelled. - The last download of the safety-related project data prior to switching to productive operation must be made with enabled access protection. (S021) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) If **several F-CPUs** can be reached via a network (such as Industrial Ethernet) by the **same PG/PC**, you must take the following additional measures to ensure that the safety-related project data is downloaded to the correct F-CPU or that safety mode is deactivated in the correct F-CPU:  - Enter the serial number of the specific F-CPU in the Safety Administration Editor.   Depending on the respective CPU type (see documentation of the CPU), you have several possibilities for determining the serial number of an F-CPU:   - Print of the serial number on the housing of the F-CPU. - Scanning of the ID link on the F-CPU. - Display of the F-CPU - Web server* - TIA Portal (I&M data)*   Note the following when downloading:  - If the "Load preview" window does not contain a warning, the connection to the correct F-CPU has been established. You can confirm the download of the safety-related project data without an additional check. - If a serial number has not yet been entered in the Safety Administration Editor or if the connected F-CPU has a different serial number, check the proposed serial number of the F-CPU in the "Load preview" window or "Disable safety mode" window. If you determine an error, cancel the download or the disabling of safety mode. Otherwise, you can confirm the procedure. - When the serial number is confirmed (online), it is always applied in the Safety Administration Editor and any existing entry is overwritten.    (S099) |  |

* To make use of these possibilities, you must ensure a connection to the expected F-CPU. You achieve this through:

- A point-to-point connection to the respective F-CPU
- Verification of the flashing of the F-CPU after selecting the "Flash LED" check box in the online and diagnostics view of the F-CPU.
- Unplugging the network cable to the respective F-CPU

> **Note**
>
> You can perform the downloading of a consistent safety program only in STOP mode.

> **Note**
>
> If STEP 7 Safety detects an inconsistent safety program during startup of the F‑CPU, the F‑CPU startup is prevented, provided the F‑CPU supports this detection. (see product information for the respective S7-300/400 F‑CPU. This is always supported with S7-1200/1500 F-CPUs.) A corresponding diagnostics event is entered in the diagnostics buffer of the F‑CPU.
>
> If the F‑CPU does not support this detection function, the F‑CPU can go to STOP mode if an inconsistent safety program is executed in activated safety mode.
>
> The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

When downloading the safety program, ensure that the "Consistent download" action is set for the "Safety program" selection in the "Load preview" dialog.

Inconsistent downloading is only possible in disabled safety mode.

##### Password prompt before downloading to an F-CPU

Before the download or, at the latest, during the download (in the "Load preview" dialog), you must gain [access permission](#access-protection-for-the-f-cpu-1) through legitimation with a user with F-right.

##### Check of serial number before the download to an S7-1200/1500 F-CPU

Before loading, the serial number of the F-CPU to be loaded is compared with the serial number entered in the Safety Administration Editor. If the serial numbers match, you can continue loading. If the serial numbers do not match or no serial number was entered in the Safety Administration Editor, you must check whether the serial number of the expected F-CPU is shown. If this is the case, confirm this with a check box in the "Load preview" dialog. The serial number is entered in the Safety Administration Editor for subsequent load processes.

##### "Load preview" dialog

For an F‑CPU, the "Load preview" dialog also contains the section "Safety program".

!["Load preview" dialog](images/169159255307_DV_resource.Stream@PNG-en-US.png)

Make the following selection:

- In order to download a consistent safety program, select the "Consistent download" action under target "Safety program".
- (S7-300, S7-400) To [download individual F-blocks selectively](#downloading-individual-f-blocks-to-an-s7-300400-f-cpu), select the "Download selection" action under the target "Safety program", and then select the required F‑blocks. If necessary, you will be prompted to disable safety mode under "Disable safety mode". This setting is only suitable for the online test of individual F-blocks.
- (S7-300, S7-400) In order to download the safety program only, select the "Consistent download" action under target "Safety program" and the "Download selection" action under target" Standard software", and then select only the standard blocks that call the main safety block.
- (S7-300, S7-400) To download no safety program, for example, because you do not know the password of the F-CPU, select the "No action" action under target "Safety program".

For S7-1200/1500 F-CPUs, only the "Consistent download" value is possible as an action in the "Load preview" dialog. You cannot change the selection of program parts to be loaded in this dialog. The selection is made automatically based on the selection in the project tree when starting the loading process.

##### Dialog "Load results"

After downloading into the F‑CPU, the dialog "Load results" is opened. This dialog shows you the status and the necessary actions after downloading.

![Dialog "Load results"](images/169161354507_DV_resource.Stream@PNG-en-US.png)

Verify that the "Downloading to device completed without error" message appears in the "Load results" dialog. If not, repeat the download operation.

#### Downloading project data to an S7-300/400 F-CPU

This section contains information on the following topics:

- [Downloading project data to an S7-300/400 F-CPU with memory card inserted (SIMATIC Micro memory card or flash card)](#downloading-project-data-to-an-s7-300400-f-cpu-with-memory-card-inserted-simatic-micro-memory-card-or-flash-card)
- [Downloading project data to an S7-400 F-CPU without flash card inserted](#downloading-project-data-to-an-s7-400-f-cpu-without-flash-card-inserted)
- [Downloading individual F-blocks to an S7-300/400 F-CPU](#downloading-individual-f-blocks-to-an-s7-300400-f-cpu)
- [Downloading project data to a memory card or removable storage device and inserting a memory card](#downloading-project-data-to-a-memory-card-or-removable-storage-device-and-inserting-a-memory-card)

##### Downloading project data to an S7-300/400 F-CPU with memory card inserted (SIMATIC Micro memory card or flash card)

When you download project data to an S7-300/400 F-CPU with memory card inserted (SIMATIC Micro Memory Card for S7-300 or flash card for S7-400), you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must adhere to the following procedure when downloading the safety-related project data to the F‑CPU with a **PG/PC** to ensure that no "old" safety-related project data is stored in the F-CPUs:  - Download the safety-related project data to the F‑CPU. - Perform a program identification (i.e. check whether the collective F‑signatures match online and offline). - Perform a memory reset of the F‑CPU using the mode switch or via the PG/PC. During the reset, after the work memory has been deleted, the project data is again transferred from the load memory (memory card, SIMATIC Micro Memory Card for S7-300 F‑CPUs, flash card for S7-400 F‑CPUs) to the work memory. (S022) |  |

##### Downloading project data to an S7-400 F-CPU without flash card inserted

When you download project data to an S7-400 F-CPU without flash card inserted, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must adhere to the following procedure when downloading the safety-related project data to the F‑CPU with a **PG/PC** to ensure that the F‑CPU does not contain any "old" safety-related project data:  - Perform a memory reset of the F‑CPU using the **mode switch** or via the **PG/PC**. - Download the safety-related project data to the F‑CPU. - Perform a program identification (i.e. check whether the collective F‑signatures match online and offline). (S023) |  |

##### Downloading individual F-blocks to an S7-300/400 F-CPU

###### Download F-blocks in disabled safety mode.

You can download F-blocks and standard blocks simultaneously to the F-CPU via the project tree. However, as soon as F-blocks are to be downloaded, a check is carried out to determine whether or not the F-CPU is in STOP mode or disabled safety mode. If not, you have the option of switching to disabled safety mode or placing the F-CPU in STOP mode.

If you want to download individual F-blocks to the F-CPU, for example, to test changes, make sure that you have not selected the folder "Program blocks" or the F-CPU in the project tree but only the blocks you want to download.

Only then will you be prompted in the "Load preview" dialog to disable safety mode once you have changed the option from "Consistent download" to "Download selection" and have changed the option "Stop modules" to "No action”.

If you fail to observe this prompt, the blocks will be downloaded without disabling safety mode, which can lead to STOP of the F-CPU.

You can also deactivate the safety mode explicitly in the Safety Administration Editor before you start the download.

Be aware that the consistency of the safety program in the F-CPU cannot be guaranteed when individual F-blocks are downloaded. For a consistent safety program, always download the entire safety program to the F‑CPU.

###### Rules for downloading individual F‑blocks

The following rules apply to downloading of individual F-blocks:

- Downloading is only possible in disabled safety mode or when the F-CPU is in STOP mode.
- F-blocks can only be downloaded to an F-CPU to which a safety program has already been downloaded.

Consequently, you have to download the entire safety program when initially downloading the safety program and after changing the password for the safety program.

> **Note**
>
> If you are downloading F‑blocks only, the blocks in which the main safety blocks are called (e.g., cyclic interrupt OB 35) are not downloaded. To do so, select the "Selection" option under "Standard software" in the preview dialog, and select the necessary blocks.

> **Note**
>
> Downloading of individual F-blocks is only suitable for testing F-blocks. Prior to the transition to productive mode, you must download the safety program consistently to the F-CPU.

##### Downloading project data to a memory card or removable storage device and inserting a memory card

Follow the same procedure as for a standard CPU to load project data of an F-CPU to a memory card (flash card for S7-400, SIMATIC Micro Memory Card for S7-300) or save it to a file folder. You must also observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination CPU, you must ensure that the correct safety-related project data is on the memory card or in the file folder after loading or saving.  Follow these steps:  1. Always load or save the project data to an empty memory card or file folder. Existing project data must not be overwritten. 2. Label the memory card or file folder uniquely (e.g. with the collective F-signature).   You must limit access to the loaded or saved safety-related project data to authorized persons through [organizational measures](#glossary). (S043) |  |

When inserting a memory card (flash card for S7-400 or SIMATIC Micro Memory Card for S7-300) with project data of an F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must ensure through online program identification or other suitable measures (e.g. by checking the labeling of the memory card or removable disk) that the inserted memory card or removable disk contains the correct safety-related project data. (S025) |  |

When you insert a memory card (flash card for S7-400 or SIMATIC Micro Memory Card for S7-300) into S7-300/400 F-CPUs, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must adhere to the following procedure when inserting the memory card to ensure that no "old" safety-related project data is stored in the F-CPUs:  - Switch off the power to the F‑CPU. For F‑CPUs with battery backup (e.g. CPU 416F‑2), remove any battery. (To ensure that the F‑CPU is de-energized, wait for the buffer time of the power supply you are using or, if this is not known, remove the F‑CPU.) - Remove the memory card with the old safety-related project data from the F‑CPU. - Insert the memory card with the new safety-related project data into the F-CPU. - Switch on the F‑CPU again and reinsert the battery, if it was removed.    (S026) |  |

#### Downloading project data into an F-CPU S7-1200

This section contains information on the following topics:

- [Downloading project data to an S7-1200 F-CPU without program card inserted](#downloading-project-data-to-an-s7-1200-f-cpu-without-program-card-inserted)
- [Downloading project data to an S7-1200 F-CPU with program card inserted](#downloading-project-data-to-an-s7-1200-f-cpu-with-program-card-inserted)
- [Inserting a transfer card into an S7-1200 F-CPU](#inserting-a-transfer-card-into-an-s7-1200-f-cpu)
- [Downloading project data of an S7-1200 F-CPU from the internal load memory to an empty SIMATIC Memory Card](#downloading-project-data-of-an-s7-1200-f-cpu-from-the-internal-load-memory-to-an-empty-simatic-memory-card)
- [Updating project data on an S7-1200 F-CPU using a transfer card](#updating-project-data-on-an-s7-1200-f-cpu-using-a-transfer-card)
- [Downloading project data to a SIMATIC Memory Card and inserting the SIMATIC Memory Card](#downloading-project-data-to-a-simatic-memory-card-and-inserting-the-simatic-memory-card)

##### Downloading project data to an S7-1200 F-CPU without program card inserted

When you download project data to an S7-1200 F-CPU without program card inserted, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not carried out in the destination F‑CPU, you must adhere to the following procedure when downloading the safety-related project data to the F‑CPU with a **PG/PC** to ensure that the F‑CPU does not contain any "old" safety-related project data:  - Download the safety-related project data to the F‑CPU. - Perform a program identification (i.e. check whether the collective F‑signatures match online and offline). (S042) |  |

##### Downloading project data to an S7-1200 F-CPU with program card inserted

When you download project data to an S7-1200 F-CPU with program card inserted, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You must observe the following procedure to ensure that there is no "old" safety-related project data in the internal load memory of the F-CPU when you insert a program card into an S7-1200 F-CPU:   1. Check to see whether **the STOP/RUN LED (orange) and the maintenance LED flash during startup for 3 seconds on an F-CPU without memory card**.  If this is the case, the internal load memory of the F-CPU has already been deleted (for example, when the F-CPU has already been operated with a program card as external load memory) and you can skip step 3. 2. Insert the program card into the F-CPU.     If the F-CPU is in RUN, it will change to STOP. The maintenance LED on the F-CPU is flashing to indicate that the program card has to be evaluated or that the internal load memory has to be deleted. 3. Use one of the following methods to delete the internal load memory:     - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.After restart of the F-CPU and the deletion of the internal load memory, **the STOP/RUN LED (orange) and the maintenance LED must be flashing**. In this case, the internal load memory of the F-CPU is deleted and does not contain any "old" safety-related project data. 4. Use one of the following methods to trigger evaluation of the program card on the F-CPU:     - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.The F-CPU restarts and evaluates the program card.    The F-CPU then enters the startup mode (RUN or STOP) that has been set up for the F-CPU. (S061) |  |

For an S7-1200 F-CPU without inserted SIMATIC Memory Card and deleted internal load memory, the status LEDs have the status described in the table below.

| Description | STOP/RUN Orange/Green | ERROR Red | MAINT Orange |
| --- | --- | --- | --- |
| Internal load memory deleted and SIMATIC Memory Card **not** inserted. | Flashing (orange)  (for 3 seconds during startup) | Off | Flashing  (for 3 seconds during startup) |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you use a programming device/PC to download F-blocks to an S7-1200 F-CPU with inserted program card (external load memory), you must ensure that the transfer takes place to the external load memory. This can be accomplished by the following measures:   - Ensure that the program card is inserted correctly. - Insert a program card whose memory size is different from the size of the internal load memory. Check in the project tree under "Online & Diagnostics > Diagnostics > Memory" if the memory size displayed for the load memory matches the memory size of the program card. (S058) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must adhere to the following procedure when downloading the safety-related project data to the F‑CPU with a **PG/PC** to ensure that no "old" safety-related project data is stored in the F-CPUs:  - Download the safety-related project data to the F‑CPU. - Perform a program identification (i.e. check whether the collective F‑signatures match online and offline). (S042) |  |

##### Inserting a transfer card into an S7-1200 F-CPU

When you insert a transfer card into an S7-1200 F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You must observe the following procedure to ensure that there is no "old" safety-related project data in the internal load memory when you copy the safety-related project data to an S7-1200 F-CPU using a transfer card:   1. Check to see whether **the STOP/RUN LED (orange) and the maintenance LED flash during startup for 3 seconds on an F-CPU without memory card**.  If this is the case, the internal load memory of the F-CPU has already been deleted and you can skip step 3. 2. Insert the transfer card into the F-CPU.     If the F-CPU is in RUN, it will change to STOP. The maintenance LED on the F-CPU is flashing to indicate that the transfer card has to be evaluated or that the internal load memory has to be deleted. 3. Use one of the following methods to delete the internal load memory:     - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.After restart of the F-CPU and the deletion of the internal load memory, **the STOP/RUN LED (orange) and the maintenance LED must be flashing**. In this case, the internal load memory of the F-CPU is deleted and does not contain any "old" safety-related project data. 4. Use one of the following methods to evaluate the transfer card (transfer from the transfer card to the internal load memory):     - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.After restart of the F-CPU and evaluation of the SIMATIC Memory Card, the F-CPU copies the project data to the internal load memory of the F-CPU. Once the copy process is complete, the maintenance LED on the F-CPU is flashing to indicate that you can remove the transfer card. 5. Remove the transfer card from the F-CPU. 6. Use one of the following methods to trigger evaluation of the internal load memory on the F-CPU:    - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.The F-CPU then enters the startup mode (RUN or STOP) that has been set up for the F-CPU. (S059) |  |

For an S7-1200 F-CPU without inserted SIMATIC Memory Card and deleted internal load memory, the status LEDs have the status described in the table below.

| Description | STOP/RUN Orange/Green | ERROR Red | MAINT Orange |
| --- | --- | --- | --- |
| Internal load memory deleted and SIMATIC Memory Card **not** inserted. | Flashing (orange)  (for 3 seconds during startup) | Off | Flashing  (for 3 seconds during startup) |

##### Downloading project data of an S7-1200 F-CPU from the internal load memory to an empty SIMATIC Memory Card

When you download project data from the internal load memory of an S7-1200 F-CPU to an empty SIMATIC Memory Card, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| To ensure that the safety-related project data is transferred from the internal load memory of the F-CPU to the SIMATIC Memory Card when plugging an empty SIMATIC Memory Card into an S7-1200 F-CPU and that the internal load memory of the F-CPU is deleted afterward, you must observe the following procedure:   1. Make sure that you are using an empty SIMATIC Memory Card, for example, by checking in the Windows Explorer that the "SIMATIC.S7S" folder and the "S7_JOB.S7S" file are deleted. 2. Insert the empty SIMATIC Memory Card into the F-CPU.    If the F-CPU is in RUN, it will change to STOP. The maintenance LED on the F-CPU is flashing to indicate that the program can be copied from the internal load memory to the SIMATIC Memory Card and that the internal load memory is deleted afterward. 3. Use one of these methods to trigger copying from the internal load memory to the SIMATIC Memory Card and subsequent deletion of the internal load memory:     - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.After restart of the F-CPU and copying of the project data from the internal load memory to the SIMATIC Memory Card and subsequent deletion of the internal load memory, **the STOP/RUN LED (orange) and the maintenance LED must flash**. In this case, the internal load memory of the F-CPU is deleted and no longer contains any safety-related project data. The SIMATIC Memory Card is now a program card. 4. Use one of the following methods to trigger evaluation of the program card on the F-CPU:     - Turn the F-CPU off and back on.    - Switch the F-CPU from STOP to RUN.    - Execute the "Memory reset" (MRES) function.The F-CPU restarts and evaluates the program card.     The F-CPU then enters the startup mode (RUN or STOP) that has been set up for the F-CPU. (S057) |  |

> **Note**
>
> Also observe the setting "Disable copying from internal load memory to external load memory" in the hardware configuration of your F-CPU.

##### Updating project data on an S7-1200 F-CPU using a transfer card

When you want to update the project data on an S7-1200 F-CPU using a transfer card, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you run an update of the safety-related project data on an S7-1200 F-CPU using a transfer card, you must ensure that the transfer to the internal load memory took place correctly by means of a subsequent program identification. (S060) |  |

##### Downloading project data to a SIMATIC Memory Card and inserting the SIMATIC Memory Card

When loading project data of an F-CPU to a SIMATIC Memory Card or saving it to a file folder, follow the same procedure as for a standard CPU. You must also observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination CPU, you must ensure that the correct safety-related project data is on the memory card or in the file folder after loading or saving.  Follow these steps:  1. Always load or save the project data to an empty memory card or file folder. Existing project data must not be overwritten. 2. Label the memory card or file folder uniquely (e.g. with the collective F-signature).   You must limit access to the loaded or saved safety-related project data to authorized persons through [organizational measures](#glossary). (S043) |  |

When inserting a SIMATIC Memory Card with project data from an F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must ensure through online program identification or other suitable measures (e.g. by checking the labeling of the memory card or removable disk) that the inserted memory card or removable disk contains the correct safety-related project data. (S025) |  |

#### Downloading project data to an S7-1500 F-CPU

This section contains information on the following topics:

- [Downloading project data to an S7-1500 F-CPU](#downloading-project-data-to-an-s7-1500-f-cpu-1)
- [Downloading project data into a redundant S7-1500HF system](#downloading-project-data-into-a-redundant-s7-1500hf-system)
- [Downloading project data to an S7-1500 F Software Controller](#downloading-project-data-to-an-s7-1500-f-software-controller)
- [Project data and inserting the SIMATIC Memory Card or a removable storage device](#project-data-and-inserting-the-simatic-memory-card-or-a-removable-storage-device)

##### Downloading project data to an S7-1500 F-CPU

When you download project data to an S7-1500 F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not carried out in the destination F‑CPU, you must adhere to the following procedure when downloading the safety-related project data to the F‑CPU with a **PG/PC** to ensure that the F‑CPU does not contain any "old" safety-related project data:  - Download the safety-related project data to the F‑CPU. - Perform a program identification (i.e. check whether the collective F‑signatures match online and offline). (S042) |  |

##### Downloading project data into a redundant S7-1500HF system

With a redundant S7-1500HF system, a consistent safety program can only be downloaded in STOP mode of the redundant S7-1500HF system.

To do this, you must heed one of the following warnings:

- Loading the redundant S7-1500HF system in STOP.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | If the function test of the safety program is not performed in the redundant destination system S7-1500HF, you must adhere to the following procedure when downloading the safety-related project data to the HF-CPUs with a PG/PC. This way you ensure that no "old" safety-related project data is stored in the HF-CPUs:  1. Switch the two HF-CPUs to STOP. 2. If you did not program restart/startup protection in your previous safety program ([Programming startup protection](#programming-startup-protection)), you must format the SIMATIC Memory Card or delete the program, for example, via the display for both HF-CPUs. 3. Download the safety-related project data to one of the two HF-CPUs. 4. Switch the HF-CPU, to which you have downloaded the new safety-related project data, to RUN mode. 5. Switch the second HF-CPU to RUN mode. 6. As soon as the RUN-Redundant mode is reached, perform a program identification on one of the two HF-CPUs (i.e. check whether the Collective F-Signatures match online and offline).    If you have programmed restart/startup protection in your new safety program, you may only acknowledge this after successful program identification.(S090) |  |
- Loading the redundant S7-1500HF system with reduced STOP time.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | If the function test of the safety program is not performed in the redundant destination system S7-1500HF, you must adhere to the following procedure when downloading the safety-related project data to the HF-CPUs with a PG/PC. This way you ensure that no "old" safety-related project data is stored in the HF-CPUs:  1. Switch one of the two HF-CPUs to STOP. 2. If you did not program restart/startup protection in your previous safety program ([Programming startup protection](#programming-startup-protection)), you must format the SIMATIC Memory Card or delete the program, for example, via the display for the HF-CPU in STOP mode. 3. Download the safety-related project data to the HF-CPU, which is in STOP mode (to the backup CPU with the context menu command "Load into backup CPU"). 4. Switch the HF-CPU that is still in RUN mode to STOP mode. 5. If you did not program restart/startup protection in your previous safety program, you must format the SIMATIC Memory Card or delete the program, for example, via the display for the HF-CPU recently switched in STOP mode. 6. Switch the HF-CPU with the newly downloaded safety-related project data to RUN mode. 7. Switch the second HF-CPU to RUN mode. 8. As soon as the RUN-Redundant mode is reached, perform a program identification on one of the two HF-CPUs (i.e. check whether the Collective F-Signatures match online and offline).     If you have programmed restart/startup protection in your new safety program, you may only acknowledge this after successful program identification. (S091) |  |

##### Downloading project data to an S7-1500 F Software Controller

When you download project data to an S7-1500 F Software Controller, you must observe the following warnings:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not carried out in the destination F‑CPU, you must adhere to the following procedure when downloading the safety-related project data to the F‑CPU with a **PG/PC** to ensure that the F‑CPU does not contain any "old" safety-related project data:  - Download the safety-related project data to the F‑CPU. - Perform a program identification (i.e. check whether the collective F‑signatures match online and offline). (S042) |  |

The following warning applies to an S7-1500 F Software Controller with firmware ≤ V21.9.x on an IPC 627E, IPC 647E, IPC 677E, or IPC 847E:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When you download the safety program, you must perform a POWER OFF/POWER ON afterwards before you run a program identification for acceptance. (S097) |  |

The following warning applies to an S7-1500 F Software Controller with firmware < V30.1

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For safety reasons, the password of an S7-1500 F Software Controller is stored in a separate memory in addition to the load memory.   Unlike the load memory, this separate memory is not deleted. This means the previous passwords are once again active after deleting the S7-1500 F Software Controller followed by a start-up.  For this reason, note the following:  - The S7-1500 F Software Controller is deleted in case of the following download scenarios of the PC station:   - Downloading a PC station with revised interface assignment.   - Downloading a PC station with revised storage location for retentive data. - We recommend that you do not set up F-access protection until after commissioning. If you still have to change the interface assignment of the PC station or the storage location for retentive data, you do not have to enter the F-password during the subsequent mandatory download of the S7-1500 F Software Controller. - We recommend that you remove the F-access protection from an S7-1500 F Software Controller that is no longer in use. If you use the S7-1500 F Software Controller later and don't remember the password, the F-password can only be removed by performing an uninstall/install/repair, installing an image file or importing a configuration file. (S076) |  |

---

**See also**

[Downloading project data to an F-CPU](#downloading-project-data-to-an-f-cpu)
  
[Software Controller](http://support.automation.siemens.com/WW/view/en/109249299)

##### Project data and inserting the SIMATIC Memory Card or a removable storage device

When loading project data of an (H)F-CPU to a SIMATIC Memory Card or saving it to a file folder, follow the same procedure as for a standard CPU. You must also observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination CPU, you must ensure that the correct safety-related project data is on the memory card or in the file folder after loading or saving.  Follow these steps:  1. Always load or save the project data to an empty memory card or file folder. Existing project data must not be overwritten. 2. Label the memory card or file folder uniquely (e.g. with the collective F-signature).   You must limit access to the loaded or saved safety-related project data to authorized persons through [organizational measures](#glossary). (S043) |  |

When inserting a SIMATIC Memory Card or an S7-1500 F Software Controller removable disk with project data of an (H)F-CPU, you must observe the following warning:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the function test of the safety program is not performed in the destination F‑CPU, you must ensure through online program identification or other suitable measures (e.g. by checking the labeling of the memory card or removable disk) that the inserted memory card or removable disk contains the correct safety-related project data. (S025) |  |

###### Inserting SIMATIC Memory Cards in a redundant S7-1500HF system

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When inserting **two** new SIMATIC Memory Cards with new safety-related project data for a redundant S7-1500HF system, proceed as follows:  1. Switch the two HF-CPUs to STOP. 2. Replace the SIMATIC Memory Cards of both HF-CPUs with    - Two SIMATIC Memory Cards, each with the new safety-related project data, or    - One SIMATIC Memory Card with the new safety-related project data and one empty SIMATIC Memory Card   Procedure for ensuring correct safety-related project data through online program identification:   1. Check on both HF CPUs in STOP mode, e.g. via the display, whether the correct safety-related project data is located on the SIMATIC Memory Card and that the second SIMATIC Memory Card is empty. 2. After a successful check, switch the HF-CPUs to RUN mode. If the new safety-related project data is only available on one SIMATIC Memory Card, you must first switch the HF-CPU with the new safety-related project data to RUN mode and then the HF-CPU with the empty SIMATIC Memory Card.   Procedure when it is ensured with clear identifiers that the correct safety-related project data is stored on the SIMATIC Memory Cards:   1. Switch the F-CPUs to RUN mode. If the new safety-related project data is only available on one SIMATIC Memory Card, you must first switch the HF-CPU with the new safety-related project data to RUN mode and then the HF-CPU with the empty SIMATIC Memory Card. (S092) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When inserting **one** new SIMATIC Memory Card with new safety-related project data for a redundant S7-1500HF system, proceed as follows:   1. Switch the two HF-CPUs to STOP. 2. Remove the SIMATIC Memory Card on one of the two HF-CPUs. 3. Format the SIMATIC Memory Card or delete the program, for example via the display, for the HF-CPU that you did not remove. 4. Insert the SIMATIC memory card with the new safety-related project data into the HF-CPU without SIMATIC Memory Card. 5. If you cannot ensure by other suitable measures (e.g. by clear labeling of the SIMATIC Memory Card) that the correct safety-related project data is located on the SIMATIC Memory Card, you have to carry out a program identification on the HF-CPU with the new safety-related project data. 6. Switch the HF-CPU with the new safety-related project data to RUN mode. 7. Switch the second HF-CPU to RUN mode. (S093) |  |

#### Restoring a backup of the safety program to an F-CPU

You have the option of backing up an F-CPU in the same way as a standard CPU and then restoring it. You can find information on backing up a CPU in the help on STEP 7 under "Creating a backup of an S7-CPU". Saving an F-CPU S7-400 is only possible with an inserted flash card.

Note the following warnings when restoring the software and hardware configuration of an F-CPU:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Once you have restored a backup of an F-CPU, you must perform a program identification.  With a redundant S7-1500HF system, you must carry out the program identification in the RUN-Redundant mode. (S055) |  |

> **Note**
>
> We recommend that you use the Collective F-Signature that is included in the name of the backup file for program identification. You must not change the Collective F-Signature in the name in this case.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) If several F-CPUs with activated Web server can be reached from a PG/PC, you must take additional measures to ensure that the safety program is restored to the correct F-CPU. Use unique identifiers for this, such as the Collective F-signature, serial number, station name or plant designation. (S065) |  |

> **Note**
>
> When restoring, you must enter the previous password for the F-CPU.

#### Specifics on creating and installing an image file of an S7-1500 F Software Controller

##### Creating an image file

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When creating an image file (for example, of an image, a data storage medium snapshot, etc.) with safety-related project data, you must comply with the following points:  - You must take [organizational measures](#glossary) to limit access to an S7-1500 F Software Controller to persons who are authorized to create image files. - Before creating an image file, you must ensure through program identification that the correct safety-related project data is located in the S7-1500 F Software Controller. - Image files with safety-related project data must be created on an empty data storage medium (deleted or formatted). Existing image files on a data storage medium or in a file system must be explicitly deleted; you are not permitted to overwrite an existing image file. - After creating the image file, remove the data storage medium containing the image file or remove the image file from the file system. - Clearly label the data storage medium or image file (for example, with the Collective F-Signature). (S073) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| If the safety-related project data in the image file and the safety-related project data on the S7-1500 F Software Controller is different, the installed safety program would not start up. In this case, you must download the project data to the F-CPU once again. For example, with TIA Portal. Therefore, you should always keep up-to-date backups of the image file.  In the same way that you can start up a safety program from another CFast card, you can also install and run the image file created by another device or data storage medium. |  |

##### Installing an image file

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When installing an image file (for example, of an image, a data storage medium snapshot, etc.) with safety-related project data, you must comply with the following points:  - You must take [organizational measures](#glossary) to limit access to an S7-1500 F Software Controller to persons who are authorized to install image files. - When installing an image file via LAN, remote access or comparable access, you must ensure access protection (for example, using Windows administrator rights (ADMIN) or the Linux root user). Note, however, that only authorized persons are set up as users. - To ensure that the image file is written to the correct S7-1500 F Software Controller, you must make sure when installing that the safety-related project data is installed in the correct F-CPU (for example, by comparing the serial number or the hardware identification of the device determined by the operating system). - You must ensure that the image file contains the correct safety-related project data, for example, by checking the labeling of the data storage medium or image file. - Remove the image file and any copies of it once you have installed it in the S7-1500 F Software Controller.    **The following applies as of firmware version V30.0 of the S7-1500 F Software Controller:**   - After installing the image file, you must ensure that the correct safety-related project data is in the S7-1500 F Software Controller through a program identification, for example, by reading out the Collective F-signature with the command line command "GetCollectiveFSignature" or the display. - Then you must enter and confirm the expected Collective F-signature with the command line command "ConfirmCollectiveFSignature".    **The following applies to firmware versions < V30.0 of the S7-1500 F Software Controller:**   After installing the image file, you must ensure through a program identification that the correct safety-related project data is in the S7-1500 F Software Controller, for example, with the display. (S074) |  |

#### Load project data (including safety-related project data) from an F-CPU into a PG/PC (S7-1500)

The "Upload from device (software)" or "Upload device as new station (hardware and software)" function is only possible for S7-1500 F-CPUs if the "Enable consistent upload from the F-CPU" option is activated for the F-CPU in the Safety Administration Editor and the project data is loaded to the F-CPU afterwards.

To load the project data (including safety-related project data) to a programming device or PC, proceed as in the standard scenario.

If multiple F‑CPUs can be reached over a network (e.g. Industrial Ethernet) by the programming device / PC, you have to ensure that the project data is uploaded from the correct F‑CPU. For example with "Online & diagnostics" > "Online accesses " > "Flash LED".

After successful loading from the device you can continue working as with a project that was created offline.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you want to carry out an acceptance with the project data loaded to the programming device / PC or want to carry out changes to the safety-related project data, you must ensure that the safety program is executable before loading.  This is fulfilled when loading from an F-CPU if the F-CPU is in RUN mode and in activated safety mode or can be set to RUN before loading. If the F-CPU remains in STOP, you are not allowed to perform acceptance or changes with the safety-related project data.  When loading from a memory card, it must have been in a suitable S7-1500 CPU beforehand. The same conditions apply as for loading from an F-CPU. (S080) |  |

You can upload individual F-blocks into a PG/PC irrespective of the "Enable consistent upload from the F-CPU" option.

You cannot upload individual know-how protected F-blocks to a programming device / PC.

As of STEP 7 Safety V18, loading the project data from a memory card is possible as a new station (hardware and software) and device (software).

---

**See also**

["Settings" area](#settings-area)

#### Load project data (including safety-related project data) from a memory card into a PG/PC (S7-1500)

The "Upload from device (software)" or "Upload device as new station (hardware and software)" function is only possible for S7-1500 F-CPUs if the "Enable consistent upload from the F-CPU" option is activated for the F-CPU in the Safety Administration Editor and the project data is loaded to the memory card afterwards.

To load the project data (including safety-related project data) to a programming device or PC, proceed as in the standard scenario.

After successful loading from the memory card, you can continue working as with a project that was created offline.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you want to carry out an acceptance with the project data loaded to the programming device / PC or want to carry out changes to the safety-related project data, you must ensure that the safety program is executable before loading.  This is fulfilled when loading from an F-CPU if the F-CPU is in RUN mode and in activated safety mode or can be set to RUN before loading. If the F-CPU remains in STOP, you are not allowed to perform acceptance or changes with the safety-related project data.  When loading from a memory card, it must have been in a suitable S7-1500 CPU beforehand. The same conditions apply as for loading from an F-CPU. (S080) |  |

---

**See also**

["Settings" area](#settings-area)

#### Loading PC station via the configuration file (only FW < V30.0)

This section contains information on the following topics:

- [Loading PC station via the configuration file](#loading-pc-station-via-the-configuration-file)
- [Creating a configuration file](#creating-a-configuration-file)
- [Importing the configuration file](#importing-the-configuration-file)

##### Loading PC station via the configuration file

You have the option to save the system configuration of the PC system in a configuration file, transport it and load it to a target system. The entire configuration of your PC station is saved in a configuration file with the ending *.psc from the TIA Portal.

Saving and loading of the configuration file is supported as of:

- STEP 7 Safety V15
- S7-1500 F Software Controller V2.5

###### Example

You can find a detailed example on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109759142).

###### Identification parameters

The identification parameters include:

- File name
- Information in the project and the station that was stored from the TIA Portal in the PSC file in the metadata.

  For example:

  - Project version
  - Plant designation
  - Station comment

Save the identification parameters in a file, if necessary, that you store on the target system.

For evaluating and testing these identification parameters via script, you must store this information directly in the script or save the identification parameters in a separate file, if necessary, that you store on the target system.

##### Creating a configuration file

1. In TIA Portal create a new configuration file with "Project > Memory Card file > New > PC system configuration file (.psc)".

   The configuration file is created in the project tree under "Card Reader/USB memory".
2. Use the Collective F-Signature to check in the Safety Administration Editor that you have selected the correct project/station.
3. Use your mouse to drag the selected PC station to the configuration file.

   This loads the PC station to the configuration file.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Instead of online program identification, you can use a unique name for the configuration file *.psc (**P**C **S**tation **C**onfiguration) to ensure that the correct safety-related project data is located in the configuration file.  In addition, you have to observe the following when creating a configuration file:  When creating a configuration file with the safety-related project data, an existing file must not be used. You have to create a new file.  You should also delete configuration files with incorrect safety-related project data from the data storage.  You must limit access to the configuration file (*.psc) through [organizational measures](#glossary) to persons who are authorized to import and modify the configuration file. (S081) |  |

##### Importing the configuration file

This section contains information on the following topics:

- [Importing the configuration file](#importing-the-configuration-file-1)
- [Import via the PC Station Panel menu](#import-via-the-pc-station-panel-menu)
- [Import by means of a script](#import-by-means-of-a-script)

###### Importing the configuration file

You have the following options for importing the configuration file:

- Via the PC Station Panel menu (import configuration file)
- By means of a script

###### Import via the PC Station Panel menu

###### Requirement

If you want to start the import of the configuration file via the menu in the PC Station Panel of an S7-150xS(P) F, the executing user must be in the Windows user group "Failsafe Operators".

###### Procedure

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If the import operation was successful, you will receive a positive feedback. If you do not receive a positive message, you must assume that the import operation was not successful and that the old safety-related project data is still present.  When a configuration file with safety-related project data is imported, you must adhere to the following points:  - Use the unique name of the configuration file to check that you have selected the required configuration file. - To ensure that a configuration file imported via LAN is imported to the correct S7-1500 F Software Controller, use the following measures:   - Remove the physical connections and possible routings to other S7-1500 F Software Controllers.   - Use unique computer names and unique user logins or use other identification options. (S084) |  |

###### Import by means of a script

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You must check in the script based on the specified identification parameters whether the import of the configuration file is permitted for the respective target system (e.g. by evaluating the F-CPU name, project name or using the plant designation).  In addition, it may be necessary or useful to check the respective instance of the target system. This means a diversity check of your addressing and/or checking the version of the configuration file, for example, only higher versions or the exclusion of specific versions (block list).  Example of checking the respective version for validity:  - The script evaluates the information about the version and only allows configuration files of a higher version, for example.   As a machine manufacturer, you must ensure that the script is protected against manipulation (unauthorized change of content or name).  If, as a machine manufacturer, you only make available the configuration files, you have to ensure that no incorrect configuration file is imported during import. You achieve this through technical measures (extended checks in the script) and training of the machine operators. (S082) |  |

The script checks for:

- Matching machine ID
- Version ID greater than current one. If so, the new version is written to the txt file.
- Instance number

The figure below contains a systematic overview of checking the configuration file in the script with the help of an identification parameter stored in a separate file (shown in violet in the figure below):

![Figure](images/170246421387_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You must determine whether the safety-related project data was successfully imported via the script by evaluating the corresponding return value (0x51A3 or 20899). If the corresponding return value is not returned, the import has failed and the old safety-related project data may still be present.  If the import operation is triggered by a server, feedback about the positive return value must also be given.  For traceability we recommend that you document the import operation in a log file.   **The following applies as of firmware version V30.0 of the S7-1500 F Software Controller:**   To have the return value 0x51A3 displayed after the import, you must call the import command with extension "/v" for verbose.  After successful import, you must read out the Collective F-signature from the meta file (PSC file) and enter and confirm it with the command line command "ConfirmCollectiveFSignature". This confirmation is required to restart the safety program.   **The following applies to firmware versions < V30.0 of the S7-1500 F Software Controller:**   To ensure that the return value is not from the previous import, you must reset the return value to 0x3FF ("PCSystem_Control /ImportConfig" without entering a file name) before the import. Then check whether the return value was reset to 0x3FF (enter "PCSystem_Control/GetStatus /ImportConfig" and then enter "echo %errorlevel%". This instruction must deliver the return value 0x3FF).  If the configuration file is imported manually via the Windows command line (via script command), you need to do one of the following:  - Reset the return value to 0x3FF and check it before the import (see above).   - Carry out the import.   - Evaluate return value (enter "PCSystem_Control /GetStatus /ImportConfig" and then enter "echo %errorlevel%". This instruction must return the return value 0x51A3 or 20899). - Carry out the import.   - Perform manual program identification, e.g. via the display of the F-CPU. (S083) |  |

> **Note**
>
> The positive return value when importing a configuration file via script is "0x51A3” for an S7-1500 F Software Controller, in contrast to the S7-1500 Software Controller, in which case it is "0x0000".

When the file is imported via script, the authorization should be moved to the script. This means that the executing user does not need a higher authorization level, since the script that was made available to the user by the machine manufacturer contains the necessary authorizations (user group "Failsafe Operators").

The rights are assigned via script by assignment of the Windows service to the corresponding user group. This initial installation must be performed beforehand by the Windows administrator on every computer with S7-150xS(P) F. The Windows service can be called by the executing user and the Windows service executes the script.

### Program identification

You use the program identification to determine that the correct safety-related project data has been downloaded to the F-CPU To do so, you compare the Collective F-Signatures and the assignment of the "F-admin" rights online with an expected value. The expected value can be, for example, the offline Collective F-Signature from the Safety Administration Editor or from the safety summary. Check the assignment of the "F-admin" right in the Safety Administration Editor.

Use organizational measures to ensure that during the program identification the safety-related project data is not downloaded by any other TIA Portal (on a separate programming device or PC).

#### With the Safety Administration Editor

For a program identification using the Safety Administration Editor, follow these steps:

1. Open the Safety Administration Editor of the F-CPU you want to check.
2. Connect online with the F-CPU you want to check.
3. Compare the Collective F-Signature displayed online with the expected value in the "General" section.
4. Check whether the offline and online program are [consistent](#identity-of-online-and-offline-program).
5. Check whether the green symbol is displayed in the column "status" and "Version comparison".

   ![With theSafety Administration Editor](images/143223043723_DV_resource.Stream@PNG-en-US.png)
6. Check in the "Web server F-admins" section whether only authorized users have the "F-admin" right offline and online.   
   If you are using local user management, this step is omitted.

#### With HMI

For a program identification using the HMI, follow these steps:

1. Read the Collective F-Signature of the safety program from the F_PROG_SIG tag of the [F-global DB](#f-shared-db-s7-300-s7-400) (S7-300, S7-400) or the F_SYSINFO.F_PROG_SIG tag of the [F-runtime group information DB](#f-runtime-group-information-db-s7-1200-s7-1500) (S7-1200, S7-1500).
2. Compare the value of the F_PROG_SIG tag with the expected value.

#### With the display of an S7-1500 F-CPU

For a program identification using the display of an F-CPU, follow these steps:

1. In the display menu, go to "Overview > Fail-safe".
2. Compare the displayed Collective F-Signature with the expected value.

#### With the Web server of an S7-1200/1500 F-CPU

For a program identification using the Web server of an S7-1200/1500 F-CPU, follow these steps:

1. Read the Collective F-Signature on the homepage of the Web server.
2. Compare the displayed Collective F-Signature with the expected value.

---

**See also**

[Safety Administration Editor](#safety-administration-editor)

### Comparing Safety Programs

#### Compare safety programs as in standard

You can use the comparison editor in STEP 7 for offline-online or offline-offline comparison of safety programs. The procedure is the same as for standard user programs. The contents of F-blocks are also compared for the comparison of safety programs. As a result, an offline-offline comparison can also be used for an [acceptance of changes](#acceptance-of-changes). You enable this comparison by selecting the "Safety" comparison criterion and disabling all other comparison criteria.

> **Note**
>
> You must not use the Comparison editor to detect changes offline-online in the safety program/configuration of the F-IOs when accepting changes. Only the offline-offline comparison is suitable for this purpose. To accept changes, proceed as described under [Acceptance of Changes](#acceptance-of-changes).

#### Comparison result for safety programs

The representation of the comparison result corresponds to the representation of STEP 7.

If you click the "Program blocks" folder on the left of the comparison editor, you can see the Collective F-Signature of the safety program displayed under "Comparison result". You also receive information about whether the safety program is consistent.

![Comparison result for safety programs](images/83516172171_DV_resource.Stream@PNG-en-US.png)

If you click on an F-block, you can see the respective signatures and interface signatures in addition to the standard information.

> **Note**
>
> If you interrupt the connection to the F-CPU during the online/offline comparison, the comparison result will be incorrect.

#### Comparison filter options

You can use filters in the comparison editor to limit the comparison result to the following block groups:

- Compare only F-blocks
- Compare only F-blocks relevant for certification
- Compare only standard blocks

You also have the STEP 7  filter options "Show only objects with differences" and "Show identical and different objects".

For comparison of safety programs, F-blocks in the "System blocks" folder are also relevant.

#### Comparison criteria

Make sure that under ![Comparison criteria](images/83526989835_DV_resource.Stream@PNG-de-DE.png) only the comparison criterion "Safety" is enabled.

#### Classification of displayed changes

Regardless of whether you carried out an offline/online or offline/offline-comparison, the following changes could account for the indicated changes to the automatically generated F-blocks:

- Change in the maximum cycle time of F-runtime group and warn cycle time of F-runtime group
- (S7-1200, S7-1500) Timeout for the disabled safety mode
- Change in F-parameters of the F-CPU
- changed safety system version or change to the hardware configuration (S7-1200/1500: Displayed as change of the "F_SystemInfo_DB" block).
- (S7-1200, S7-1500) Changes in the group structure of the F-blocks. Displayed as change of the "F_SystemInfo_DB" block.
- (S7-300, S7-400) Change in the F‑runtime group communication, for example, change in the number of a DB for F‑runtime group communication
- Change in main safety block, F-FB, F-FC, F-DB
- Change of the hardware configuration for the F-I/O addressed in the safety program

It is possible that a block is displayed as changed, but no changes are displayed in the detailed comparison of the block content. This is not a display problem but means that changes of addresses in the tag table, for example, have an effect on this block. Test this block in case of doubt.

#### Document the result of the comparison

The comparison result can be printed via "Project > Print" in the menu bar or the "Print" icon in the toolbar or create a PDF file. Select "Print objects/area" "All" and "Properties" "All".

After printing, make sure that all pages were printed. Incomplete printouts (e.g. lines cut off, insufficient toner when printing to paper) must not be used for an acceptance of changes.

### Creating a safety summary

The documentation of the safety-related project data (safety summary) serves, in addition to other system documentation, as the basis for checking the correctness of the individual components of the system. Correctness is a prerequisite for system acceptance.

The Collective F-signature in the footer on the pages of the safety summary guarantees unambiguous assignment of the safety summary to a safety program.

The safety summary can be created in printed or electronic form, for example, as a PDF file.

#### Procedure for creating the safety summary

To create the safety summary, follow these steps:

1. [Open the Safety Administration Editor](#opening-the-safety-administration-editor) of the F-CPU whose safety summary you want to create.
2. Under "Safety summary" in the "General" section, press the "Create safety summary" button.

   In the displayed dialog, you can make layout settings for the printout and specify the scope of the printout (all/subset), among other things.

   Alternatively, you can select an F-CPU in the project tree and open the dialog using "Print" in the shortcut menu, "Project > Print" in the menu bar or the print button in the toolbar.
3. Under "Document information", select one of the ISO formats, e.g. "DocuInfo_ISO_A4_Portait".
4. Select the "All" option, if the F‑blocks and F-compliant PLC data types are to be shown in the printout. This is necessary, for example, to document the program code for the acceptance (see [Acceptance of system](#system-acceptance)). Select the "Compact" option to exclude the source code from the printout.
5. Click the "Print" button.

As a result, you receive the safety summary for the F‑CPU.

After printing, make sure that all pages were printed. Incomplete printouts (e.g. lines cut off, insufficient toner when printing to paper) must not be used for an acceptance.

#### Overview of the contents of the safety summary

The information included in the safety summary is summarized below:

- General information on program identification, signatures, software versions, access protection, settings of the safety program (from the "Settings" work area of the Safety Administration Editor), for example safety system version.
- System library elements used in safety program (from the "Instructions" task card) along with their versions
- Information about the F‑runtime groups (e.g. cycle time warning limit of the F-runtime group, maximum cycle time of the F-runtime group)
- List of the F‑blocks within the "Program blocks" folder (e.g. name, function, associated F‑runtime group, signature)
- (S7-1200, S7-1500) List of the know-how protected F-blocks used in the safety program (e.g., name, signature, used safety system version, used versioned instructions or called F-blocks).
- (S7-1200, S7-1500) List of F-compliant PLC data types (UDT), if these exist in the safety program.
- Data from the standard user program that are evaluated in the safety program
- Block parameters of the safety-related CPU‑CPU communication
- (S7-300, S7-400) Absolute addresses and names of the F-shared DB tags that can be accessed from the standard user program
- Information on the F-CPU used (e.g. firmware version, F-source address) information on the F-IOs used (e.g. firmware version, general and specific parameters)
- Information on the printout (print date, number of pages)

#### Content of the footer of the safety summary

Based on the footer of the safety summary, you can see whether the printed safety-related project data is consistent and whether all pages of the safety summary belong to the same safety program and the same version (the same Collective F-Signature in the footer of every page means that the safety summary belongs to the safety program with this Collective F-Signature).

The footer is only added to the source code of the F-blocks if the "All" option was selected when creating the safety program. If F‑blocks are printed by other means, the footer is omitted, and you can no longer easily identify whether the block printout belongs to the current safety program version.

#### Safety summary for a migrated project

You can only create the safety summary for a project migrated from S7 Distributed Safety V5.4 SP5 if the project was compiled with STEP 7 Safety Advanced, thereby applying the new program structure for safety programs (main safety block). Otherwise, the safety documentation cannot be created and you will receive a corresponding error message.

We recommend that you create a safety summary for your project in S7 Distributed Safety V5.4 SP5 before the migration.

### Testing the safety program

This section contains information on the following topics:

- [Overview of Testing the Safety Program](#overview-of-testing-the-safety-program)
- [Disabled safety mode](#disabled-safety-mode)
- [Testing the safety program](#testing-the-safety-program-1)
- [Testing the safety program with S7-PLCSIM](#testing-the-safety-program-with-s7-plcsim)
- [Changing the safety program in RUN mode (S7-300, S7-400)](#changing-the-safety-program-in-run-mode-s7-300-s7-400)
- [Safety program in RUN mode (S7-1200, S7-1500)](#safety-program-in-run-mode-s7-1200-s7-1500)

#### Overview of Testing the Safety Program

##### Complete function test or test of changes

After creating a safety program, you must carry out a complete function test in accordance with your automation task.

For changes made to a safety program that has already undergone a complete function test, only the changes and that there is no effect on the parts of the safety program that were not changed need be tested.

##### Monitoring

Read-only test functions (such as monitoring tags of the safety program) are available for safety programs as in the standard.

##### Modifying

Read and write test functions (such as controlling tags of the safety program) are only available to a limited extent for safety programs and only in disabled safety mode.

##### Simulation via S7‑PLCSIM

You can test the safety program using S7‑PLCSIM. You use S7-PLCSIM in the same way as for standard user programs.

You start the simulation with S7-PLCSIM using menu item "Online > Simulation > Start"

##### Rules for testing

- Forcing of F-I/O inputs and F-I/O outputs is not possible.
- Controlling F-I/O outputs in connection with the function "Enabling F-I/O outputs" is not possible.
- Setting breakpoints in the standard user program will cause errors in the safety program (see also [Testing the safety program](#testing-the-safety-program-1)).
- Changes in the configuration of F-I/O or safety-related CPU-CPU communication can only be tested after the hardware configuration has been saved and downloaded, and after the safety program has been compiled and downloaded to the F-CPU.

---

**See also**

[Disabling safety mode](#disabling-safety-mode-1)

#### Disabled safety mode

This section contains information on the following topics:

- [Disabling safety mode](#disabling-safety-mode)
- [Configuring the time limit for disabled safety mode (S7-1200, S7-1500)](#configuring-the-time-limit-for-disabled-safety-mode-s7-1200-s7-1500)
- [Disabling safety mode](#disabling-safety-mode-1)

##### Disabling safety mode

The safety program generally runs in the F‑CPU in safety mode after a STOP/RUN transition. This means that all fault control measures are activated. The safety program cannot be modified during operation (in RUN mode) in safety mode. You must disable safety mode of the safety program to, for example, modify tags in the safety program in RUN mode. Safety mode remains disabled until the F-CPU is next switched from STOP to RUN mode.

As of Safety system version V2.4, disabled safety mode for S7-1200/1500 CPUs is time-limited.

After the time limit has expired, the F-CPU or the redundant S7-1500HF system automatically goes to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

You can avoid an unplanned STOP of the F-CPU after the time limit has expired as follows:

- Ending the disabled safety mode through a targeted STOP/RUN transition.
- Resetting the remaining runtime. Resetting can be used as often as needed.

##### Configuring the time limit for disabled safety mode (S7-1200, S7-1500)

###### Introduction

You can configure the duration of the time limit.

###### Requirements

- In the Safety Administration Editor, the "Safety mode can be disabled" option is activated.
- The minimum Safety system version is set to V2.4.

###### Procedure for configuring the runtime

To configure the time limit, follow these steps:

1. Open the Safety Administration Editor of the F-CPU.
2. Open the "[Settings](#settings-area)" area in the area navigation.
3. Under "Runtime for the deactivated safety mode", configure the time limit for the safety mode. The default time is 4 hours. You have the option to configure the time limit to a maximum of 8 hours and a minimum of 1 minute.

> **Note**
>
> The value of the configured time is not included in the Collective F-Signature.

##### Disabling safety mode

###### Requirements

- In the Safety Administration Editor, the "Safety mode can be disabled" option is activated.
- (S7-1200, S7-1500) The [serial number of the F-CPU](#general-area) has been entered in the Safety Administration Editor.
- The project is loaded to the F-CPU.
- The F-CPU is in RUN.
- The safety program runs in safety mode.

###### Rules for disabling safety mode

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Because changes to the safety program can be made in RUN mode when safety mode is deactivated, you must take the following into account:   - Disabling of safety mode is intended for test purposes, commissioning, etc. While safety mode is disabled, plant safety must be ensured by [organizational measures](#glossary).   After the test or commissioning, safety mode must be enabled again. To do this, execute a STOP/RUN transition of the F-CPU.   In a redundant S7-1500HF system you have to set both HF-CPUs or the redundant system S7-1500HF to STOP before you restart the HF-CPUs. - A disabling of the safety mode must be displayed.   Use the MODE tag in the F‑global DB ("F_GLOBDB".MODE) for S7-300/400 F-CPUs or in the F-runtime group information DB (e.g. RTG1SysInfo.F_SYSINFO.MODE) for S7-1200/1500 F-CPUs, which you can evaluate to read the operating mode (1 = Disabled safety mode). - It must be possible to verify that safety mode has been disabled. A log is required, if possible by recording and, if applicable, archiving alarms to the operator control and monitoring system or, if need be, through organizational measures. In addition, it is recommended that a disabling of the safety mode be indicated on the operator control and monitoring system. - Disabling of safety mode is limited to one F-CPU. You must, however, take the following into account for safety-related CPU-CPU communication: If the F‑CPU that sends the data is in disabled safety mode, you can no longer assume that the data sent by this F‑CPU are generated safely. You must then also ensure safety in those parts of the plant that are influenced by the sent data. For example, by evaluating the SENDMODE* tag in the F-CPU that receives the data, you can output safe substitute values instead of the received data.   * SENDMODE is available to you as output of the RCVDP or RCVS7 instructions or in case of communication via Flexible F-Link as a tag in the F-communication DB.   (S027) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) If **several F-CPUs** can be reached via a network (such as Industrial Ethernet) by the **same PG/PC**, you must take the following additional measures to ensure that the safety-related project data is downloaded to the correct F-CPU or that safety mode is deactivated in the correct F-CPU:  - Enter the serial number of the specific F-CPU in the Safety Administration Editor.   Depending on the respective CPU type (see documentation of the CPU), you have several possibilities for determining the serial number of an F-CPU:   - Print of the serial number on the housing of the F-CPU. - Scanning of the ID link on the F-CPU. - Display of the F-CPU - Web server* - TIA Portal (I&M data)*   Note the following when downloading:  - If the "Load preview" window does not contain a warning, the connection to the correct F-CPU has been established. You can confirm the download of the safety-related project data without an additional check. - If a serial number has not yet been entered in the Safety Administration Editor or if the connected F-CPU has a different serial number, check the proposed serial number of the F-CPU in the "Load preview" window or "Disable safety mode" window. If you determine an error, cancel the download or the disabling of safety mode. Otherwise, you can confirm the procedure. - When the serial number is confirmed (online), it is always applied in the Safety Administration Editor and any existing entry is overwritten.    (S099) |  |

* To make use of these possibilities, you must ensure a connection to the expected F-CPU. You achieve this through:

- A point-to-point connection to the respective F-CPU
- Verification of the flashing of the F-CPU after selecting the "Flash LED" check box in the online and diagnostics view of the F-CPU.
- Unplugging the network cable to the respective F-CPU

###### Procedure for disabling safety mode

To disable safety mode, follow these steps:

1. Open the Safety Administration Editor of the corresponding F-CPU.
2. Open the "[General](#general-area)" area in the area navigation.
3. Click the "Disable safety mode" button.
4. If access protection is set up for the F-CPU, enter the password for the F-CPU or legitimate yourself again as a user with F-right.
5. Only for S7-300/400 F-CPUs for which access protection is **not** set up:   
   Make sure that you disable safety mode of the desired F-CPU by checking the Collective F-Signature in the dialog that is displayed next.
6. Confirm the deactivation.

Safety mode is then disabled.

The remaining runtime until an S7-1200/1500 F-CPU goes into STOP starts immediately after the safety mode is disabled. The remaining runtime is displayed in the Safety Administration Editor in the "[General](#general-area)" area in online mode. In addition, the remaining runtime is displayed in the web server of an S7-1500 F-CPU as of firmware V2.9.

###### Reset remaining runtime until the F-CPU goes to STOP

To avoid the expiration of the remaining runtime and the associated STOP of the F-CPU, you can reset the remaining runtime in the Safety Administration Editor. This resets the remaining runtime to the configured value and starts it running again immediately after that.

Proceed as follows:

1. Open the Safety Administration Editor of the corresponding F-CPU.
2. Open the "[General](#general-area)" area in the area navigation.
3. Click the "Reset remaining runtime" button.
4. If access protection is set up for the F-CPU, enter the password for the F-CPU or legitimate yourself again as a user with F-right.
5. Only for S7-300/400 F-CPUs for which access protection is **not** set up:   
   Make sure that you disable the remaining runtime of the correct F-CPU by checking the Collective F-Signature in the dialog that is displayed next.
6. Confirm the reset of the remaining runtime.

> **Note**
>
> The remaining runtime is also displayed in the [F-runtime group information DB](#f-runtime-group-information-db-s7-1200-s7-1500) of the respective F-runtime group in the MODE_REMAINING_TIME tag.
>
> In case of two F-runtime groups, different values may be displayed caused by different update times.
>
> The value "0" is not displayed after expiration of the remaining runtime, but the remaining runtime existing in the last cycle.

###### Enabling safety mode

> **Note**
>
> To enable safety mode, the F-CPU must be switched from STOP to RUN mode.
>
> In a redundant S7-1500HF system you have to set both HF-CPUs or the redundant system S7-1500HF to STOP before you restart the HF-CPUs.
>
> Switching the F-CPU from STOP to RUN mode always enables safety mode, even if the safety program has been modified or is not consistent.
>
> If you have changed your safety program, but have not recompiled and downloaded it, the F-CPU can revert to STOP mode.

###### Evaluating safety mode/disabled safety mode

If you wish to evaluate safety mode/disabled safety mode in the safety program, you can evaluate the "MODE" tag in the [F‑Global DB](#f-shared-db-s7-300-s7-400) for S7-300/400 F-CPUs or F-runtime group information DB for S7-1200/1500 F-CPUs (1 = Disabled safety mode). You use fully qualified access to access this tag (e.g. "F_GLOBDB".MODE or RTG1SysInfo.MODE).

You can use this evaluation, for example, to passivate F‑I/O when the safety program is in disabled safety mode. To do so, assign the "MODE" tag in the F-shared DB or F-runtime group information DB to all "PASS_ON" tags in the F-I/O DBs of the F-I/O that you wish to passivate.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When the safety program is in disabled safety mode, the "MODE" tag in the F-shared DB or F-runtime group information DB is also evaluated in disabled safety mode.   Even if the F-I/O is passivated in disabled safety mode by evaluating the "MODE" tag, the safety of the plant must be ensured during disabled safety mode by [organizational measures](#glossary). (S028) |  |

---

**See also**

[Configuring the time limit for disabled safety mode (S7-1200, S7-1500)](#configuring-the-time-limit-for-disabled-safety-mode-s7-1200-s7-1500)

#### Testing the safety program

##### Introduction

Tags of the safety program can be monitored at any time.

Controlling tags of the safety program is only possible in deactivated safety mode as some fault control measures of the safety program have to be disabled for this.

You can control the following tags of the safety program:

- Inputs and outputs of the F‑I/O (channel values and value status (S7-1200, S7-1500))
- Tags in F-global DB (except DB for F‑runtime group communication)
- Tags in instance DBs of F‑FBs
- Tags in F‑I/O DBs (for permitted tags see [F‑I/O DB](#f-io-db))

##### Procedure for monitoring tags of the safety program

Monitor the required tags of the safety program from an open watch table or from the program editor (program status).

1. Proceed as in the standard. More information can be found in the STEP 7help in "Testing user programs".

##### Procedure for controlling tags of the safety program

Control the required tags of the safety program from an open watch table:

1. For modifying, [deactivate the safety mode](#disabling-safety-mode-1) in the automatically shown dialog.
2. Terminate existing modify requests after testing is complete before activating safety mode.

Values in F-DBs can only be modified online in the F-CPU. If the value is also to be changed offline, you must do this by editing the start value offline and compiling the safety program.

Proceed as follows to control tags of F-I/O:

1. Create a separate row for each channel value and value status (S7-1200, S7-1500) to be modified. The control value must correspond to the channel value or value status.
2. Set "start of scan cycle" or "end of scan cycle" and "permanent" or "once".

   Regardless of the trigger point setting, requests to modify inputs (PII) of F-I/O always become effective before the main safety block is executed and requests to modify outputs (PIQ) always become effective after execution of the main safety block.
3. (S7-300, S7-400) Create an additional watch table if you want to control more than 5 inputs/outputs.

> **Note**
>
> F-I/O can only be modified in RUN mode of the F-CPU.
>
> You cannot modify a configured F-I/O from which neither a channel value or a value status (S7-1200, S7-1500), nor any tag from the associated F-I/O DB has been used in the safety program. In your safety program, you should therefore always use at least one tag from the associated F-I/O DB or at least one channel value or value status (S7-1200, S7-1500) of the F-I/O to be modified.
>
> For inputs (PII), modify requests take priority over fail-safe value output, while for outputs (PIQ), fail-safe value output takes priority over modify requests. For outputs (channels) that are not activated in the properties for the F-I/O, modify requests affect the PIQ only, and not the F-I/O.

> **Note**
>
> The following applies for S7-1200/1500 F-CPUs:
>
> To avoid invalid combinations of channel value and status value:
>
> - The value status is set by the F-system automatically to 1 when setting a channel value to a value <> fail-safe value 0
> - The fail-safe value 0 is automatically output when setting the value status to 0 for the associated channel value

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You need to specifically reset constant modify requests in the watch table in disabled safety mode.  Note that constant modify requests that are not correctly reset can remain active in the background even after a STOP/RUN transition of the F-CPU.  Because the F-CPU is in safety mode again after a STOP/RUN transition, the constant modify requests are no longer effective and are not shown in the watch table.  The requests become active again as soon as you disable safety mode again.  With a memory reset of the F-CPU, you can make sure that no constant modify requests are active in the background on the F-CPU. (S029) |  |

##### Wiring test using watch table

You can carry out a wiring test for an input by changing an input signal and verifying whether or not the new value arrives in the PII.

You can carry out a wiring test for an output by changing the output with the Modify function and verifying whether the required actuator responds.

For the wiring test, note that a safety program must be running on the F‑CPU, in which at least one channel value or value status (S7-1200, S7-1500) of the F‑I/O to be monitored or modified or one tag from the associated F‑I/O DB has been used.

For F-I/O that can also be operated as standard I/O (e.g., S7-300 fail-safe signal modules), you can also carry out the wiring test for outputs using the Modify function in STOP mode by operating the F-I/O as standard I/O rather than in safety mode.

##### Additional rules for testing (S7-300, S7-400, S7-1500)

Setting breakpoints in the standard user program will cause the following errors in the safety program:

- F-cycle time monitoring has expired
- Error during communication with the F-I/O

  (S7-1500) Fail-safe modules switch to safe mode after the configured F-monitoring time has expired.
- Error during safety-related CPU-CPU communication
- Internal CPU faults

If you nevertheless want to use breakpoints for testing, you must first disable safety mode. This will result in the following errors:

- Error during communication with the F-I/O
- Error during safety-related CPU-CPU communication

Difference between S7-1500 F-CPUs and S7-300/400 F-CPUs:

- If a breakpoint is activated and reached, the F-CPU goes directly to STOP after HOLD.
- If you want to switch to RUN again after HOLD to test your standard user program further, you can simulate this with S7-PLCSIM.

No access protection is initially necessary for test purposes, commissioning, etc. This means you can execute all offline and online actions without access protection, that is, without password prompt.

---

**See also**

[Changing the safety program in RUN mode (S7-300, S7-400)](#changing-the-safety-program-in-run-mode-s7-300-s7-400)
  
[Downloading project data to an F-CPU](#downloading-project-data-to-an-f-cpu)

#### Testing the safety program with S7-PLCSIM

You can test your safety program together with your standard program on a simulated CPU with S7-PLCSIM and without the need for hardware. Also observe warning S030 in the section "[Notes on Safety Mode of the Safety Program](#notes-on-safety-mode-of-the-safety-program)".

You use S7-PLCSIM for SIMATIC Safety F-systems as you would for S7 standard systems. Note the following special features:

##### Safety mode/disabled safety mode

We recommend that you test your safety program in safety mode to detect whether the F-CPU goes into STOP as early as in the test phase of your safety program in S7-PLCSIM as a result of, for example, that the results of instructions were outside the permitted range for the data type.

The following simulations can be run in S7-PLCSIM, just as on an actual F-CPU, in disabled safety mode only.

- Modifying tags in F-DBs and F-I/O DBs.

(S7-1200, S7-1500) To prevent unintentional modification of tags in F-DBs and F-I/O DBs in safety mode, we recommend that you do not select the "Activate/deactivate modification of non-inputs" button in S7-PLCSIM

During the simulation with S7-PLCSIM , monitoring of the maximum cycle time of the F-runtime group and the cycle time warning limit of the F-runtime group (S7-1200, S7-1500) are disabled.

##### Differences between a simulated F-CPU and real F-CPU

Note that S7-PLCSIM does not fully behave like a real F-CPU down to the individual details. In particular, the startup behavior of an F-I/O cannot be simulated exactly.

##### Input simulation of F-I/O

**Simulation of inputs (channel values) in S7-PLCSIM:**

You simulate inputs (channel values) of F-I/O in S7-PLCSIM as you would inputs (channel values) of standard I/O. Keep in mind the following notes/restrictions:

During the transition of the F-CPU from "STOP" to "RUN" mode in S7-PLCSIM, all inputs (channel values) of F-I/O are initialized with 0 in the process image input (PII).

The inputs (channel values) can be simulated starting from the 2nd cycle and are then available in the PII.

**Simulation of inputs (value status) in S7-PLCSIM:**

(S7-1200, S7-1500) By simulating inputs (value status) of F-I/O, you can simulate incoming and outgoing F-I/O / channel faults. Keep in mind the following notes/restrictions:

- To realistically simulate the behavior of the F-I/O, you must note the connection between channel value and value status on the real F-I/O. The combination value status = 0 and channel value <> fail-safe value (0) is invalid and can result in the simulation deviating from the behavior of the real F-CPU.
- During the transition of the F-CPU from "STOP" to "RUN" in S7-PLCSIM, all inputs (value status) of F-I/O are initialized with 1 in the process image input (PII). This means you can start with the simulation of inputs (channel values) immediately without simulation of the inputs (value status).
- The simulation of inputs (value status) in S7-PLCSIM does not have an effect on the QBAD and PASS_OUT tags in the F-I/O DB. Note that with real F-I/O, QBAD and PASS_OUT can be 1 as soon as the value status is 0 for at least one channel of the F-I/O (see tags of the F-I/O DB: [PASS_OUT/QBAD/QBAD_I_xx/QBAD_O_xx and value status](#qbadpass_outdisabledqbad_i_xxqbad_o_xx-and-value-status)).
- For F-I/O configured with "Behavior after channel fault" = "Passivation of the complete F-I/O", use the tag PASS_ON in the F-I/O DB for simulation of the passivation of the complete F-I/O for F-I/O / channel faults. If you limit the simulation to passivation of individual inputs (channel value including value status), the behavior of the simulation will deviate from that of the real F-CPU.
- You can also use the PASS_ON tag in the F-I/O DB for F-I/O without value status to simulate the passivation of the entire F-I/O in case of F-I/O or channel faults.
- To simulate an F-I/O / channel fault of the SM 336; AI 6 x 13Bit or SM 336; F-AI 6 x 0/4...20 mA HART with configuration "Behavior after channel fault" = "Passivate channel", you must simulate the inputs (channel values) with 7FFF<sub>H</sub> (for overflow) or 8000<sub>H</sub> (for underflow).
- For F-I/O which does not support the "RIOforFA-Safety" profile, you must run a user acknowledgment with a positive edge at the ACK_REI tag of the F-I/O DB as with a real F-I/O for reintegration after the value status has changed from 0 to 1 or when the channel value has changed from 7FFF<sub>H</sub>/8000<sub>H</sub> to unequal 7FFF<sub>H</sub>/8000<sub>H</sub> (see above) when ACK_NEC = 1 of the F-I/O DB. Reintegration takes place automatically in all other cases possibly deviating from the real F-I/O.

##### Update times

Keep in mind that the status of the inputs (channel values or value status (S7-1200, S7-1500)) that you are monitoring in the SIM table in S7-PLCSIM is only identical to the status being processed in the safety program if there is no passivation of the associated F-I/O.

With passivation of the F-I/O, the safety program operates with substitute values (channel value and value status (S7-1200, S7-1500) =0).

##### CPU-CPU-communication with SENDDP / RCVDP instructions

The following applies for SENDDP/RCVDP (S7-300, S7-400) instructions and SENDDP/RCVDP instructions with Version < 3.0 (S7-1200, S7-1500):

You cannot simulate communication between F-CPUs with the SENDDP and RCVDP instructions in S7-PLCSIM. You can, however, use the SENDDP and RCVDP instructions together with S7-PLCSIM. During simulation in S7-PLCSIM, the RCVDP instruction outputs the substitute values pending at its inputs SUBBO_xx and SUBI_xx ((S7-1200, S7-1500) or alternatively SUBDI_00). The SENDDP and RCVDP instructions signal this with 1 at output SUBS_ON.

For SENDDP/RCVDP instructions with Version >= 3.0 (S7-1200, S7-1500) the following applies:

During the simulation with S7-PLCSIM it is possible to simulate the received data and the information "Deactivated Safety Mode" (RCVDP) or respectively the information "Substitute value output" (SENDDP) in the corresponding transfer area for inputs. Note the following notes:

- The simulated values do not become active until you set the SIMULATION bit for the first time in the respective simulation control word (see the following table) after the F-system has started up. Before setting the SIMULATION bit, the RCVDP instruction outputs the fail-safe values that are pending at its inputs SUBBO_xx and SUBI_yy (or alternatively SUBDI_00).
- The setting of the SEND_MODE bit in the simulation control word causes a setting of the SENDMORE output for the RCVDP instruction.
- The setting of the STATUS_SUBS bit in the simulation control word causes a setting of the SUBS_ON output for the SENDDP instruction.
- Reserved bits in the simulation control word always have to be 0.
- During a STOP/RUN transition from S7-PLCSIM the most recently simulated values in the transfer area for inputs are kept.

The start address(es) of the configured transfer area for the input and output data can be found in the respective configuration (see also "[Configuring and programming communication (S7-1200, S7-1500)](#configuring-and-programming-communication-s7-1200-s7-1500)").

Structure of the relevant transfer area for inputs of the simulation control word (instruction RCVDP)

|  |  |  |
| --- | --- | --- |
| **Byte** | **Meaning** | **Comment** |
| 0 | RD_BO_15 … RD_BO_08 |  |
| 1 | RD_BO_07 … RD_BO_00 |  |
|  | **DINTMODE=0:** |  |
| 2 | RD_I_00 | Word RD_I_00, MSB<sup>1) </sup>first |
| 3 |  |  |
| 4 | RD_I_01 | Word RD_I_01, MSB<sup>1) </sup>first |
| 5 |  |  |
|  | **Alternative DINTMODE=1:** |  |
| 2 | RD_DI_00 | High Word from RD_DI_00, MSB<sup>1) </sup>first |
| 3 |  |  |
| 4 | Low Word from RD_DI_00 **XOR 0x8000**, MSB<sup>1) </sup>first |  |
| 5 |  |  |
|  |  |  |
| 6 | Simulation control word (High Byte) | Bit 0…6: Reserved  Bit 7: SIMULATION: Activating RCVDP simulation |
| 7 | Simulation control word (Low Byte) | Bit 0: SEND_MODE: Set output SENDMODE  Bit 1…7: Reserved |
| 8 … 11 | Reserved |  |
| <sup>1)</sup> MSB: most significant bit |  |  |

Structure of the relevant transfer area for inputs of the simulation control word (instruction SENDDP)

|  |  |  |
| --- | --- | --- |
| **Byte** | **Meaning** | **Comment** |
| 0 | Simulation control word (High Byte) | Bit 0: STATUS_SUBS: Set output SUBS_ON  Bit 1…6: Reserved  Bit 7: SIMULATION: Activating SENDDP simulation |
| 1 | Simulation control word (Low Byte) | Bit 0…7: Reserved |
| 2 … 5 | Reserved |  |

##### (S7-300, S7-400) CPU-CPU-communication with SENDS7/RCVS7 instructions

You cannot simulate communication between F-CPUs with the SENDS7 and RCVS7 instructions in S7-PLCSIM. You can, however, use the SENDS7 and RCVS7 instructions together with S7-PLCSIM.

During simulation in S7-PLCSIM, the RCVS7 instruction outputs the initial values specified in the communication DB as fail-safe values. The SENDS7 and RCVS7 instructions signal this with 1 at output SUBS_ON.

##### CPU-CPU communication with Flexible F-Link

If communication between F-CPUs is simulated with Flexible F-Link, then observe the following warning.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When data is sent from an F-CPU simulated with S7-PLCSIM using safety-related CPU-CPU communication with Flexible F-Link, you can no longer assume that this data is generated safely. You can, for example, output safe substitute values in place of the received data in the receiving F-CPU by evaluating the SENDMODE tag.   (S086) |  |

##### Inconsistent safety program (S7-1200, S7-1500)

If the CPU goes into STOP in S7-PLCSIM with the diagnostic entry "Safety program: inconsistent", the F-CPU is not initialized correctly in S7-PLCSIM yet. Perform a memory reset of the F-CPU in S7-PLCSIM and download the program once again to the CPU in S7-PLCSIM.

#### Changing the safety program in RUN mode (S7-300, S7-400)

##### Introduction

You make changes to F-blocks offline in the program editor in the same way as for a standard program. You download the changed F-blocks in RUN to the F-CPU in the "[disabled safety mode](#disabling-safety-mode-1)".

> **Note**
>
> If you do **not** want to make changes to the safety program during operation, see [Creating F‑blocks in FBD/LAD](#creating-f-blocks-in-fbd-lad).

##### Procedure for changing the safety program in RUN mode

To change the safety program, follow these steps:

1. Change the main safety block or F-FB and its associated instance DB, F-FC, or F-DB in the Program editor.
2. Download the changed F-block(s) to the F-CPU (for procedure, see [Downloading project data to an F-CPU](#downloading-project-data-to-an-f-cpu)). The entire program is then automatically compiled.
3. If safety mode is active, the "Load preview" dialog will prompt you to deactivate it and to enter the password for the safety program.

**Note**

When downloading in disabled safety mode, you can only download the fail‑safe blocks created by you (main safety blocks, F‑FB, F‑FC, or F‑DB), F‑application blocks, or standard blocks and their associated instance DBs. If you download automatically added F-blocks (F-SBs or automatically generated F-blocks and associated instance DBs, F-shared DB), the F-CPU can go to STOP mode or safety mode can be activated.

Therefore, always select individual blocks only when downloading in disabled safety mode.

##### Sequence for downloading changes

Changes in the safety program in RUN mode when safety mode is disabled can, for example, cause the status of an actuator to change as a result of program changes.

After changes, start by downloading the safety program and then the function of the standard user program monitored by the safety program.

##### Restrictions on safety-related CPU-CPU communication

During operation (in RUN mode), you cannot establish new safety-related CPU-CPU communication by means of new SENDDP/RCVDP or SENDS7/RCVS7 instructions.

To establish new safety-related CPU-CPU communication you must always download the relevant safety program consistently to the F-CPU while in STOP mode after inserting a new SENDDP, SENDS7, RCVDP, or RCVS7 instruction.

##### Restrictions on F‑runtime group communication

You cannot make any changes to the safety-related communication between F-runtime groups in RUN mode. This means that you cannot assign, delete, or change any DBs for F-runtime group communication of an F-runtime group.

Following changes in the F-runtime group communication, you must always download the safety program consistently to the F-CPU while in STOP mode.

##### Restrictions on F‑I/O access

If during operation (in RUN mode), you insert an F-I/O access to an F-I/O of which no single channel value or tag from the associated F-I/O DB has yet been used in the safety program, the F-I/O access only becomes effective when the safety program is downloaded consistently to the F-CPU.

##### Changing the standard user program

You can download changes in the standard user program when the F-CPU is in RUN mode, regardless of whether safety mode is enabled or disabled.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) In productive operation, it must be prevented that changes to the standard user program are unintentionally made in the safety program as well. For this purpose, you must configure the protection level "Write protection for fail-safe blocks" and configure a password for the F‑CPU.  With the "Write protection" or "Write/read protection" protection level, the password would apply to the standard and the safety program. (S001) |  |

##### Procedure for applying changes to the safety program

If you download individual F‑blocks to the F‑CPU during operation (in RUN mode), the F‑system blocks (F‑SBs) and the automatically generated F‑blocks are neither updated nor downloaded, resulting in an inconsistent safety program in the F‑CPU. Use the following procedure to apply changes to the safety program:

1. Download the safety program consistently to the F‑CPU, and activate safety mode by switching the F‑CPU from STOP to RUN mode (for procedure, see [Downloading project data to an F-CPU](#downloading-project-data-to-an-f-cpu)).
2. Follow the steps described in [Acceptance of Changes](#acceptance-of-changes).

#### Safety program in RUN mode (S7-1200, S7-1500)

##### Introduction

You make changes to F-blocks offline in the program editor in the same way as for a standard program. Loading the changed F-blocks in RUN to the F-CPU is done with the Fast Commissioning mode in [deactivated safety mode](#disabling-safety-mode-1).

The Fast Commissioning mode distinguishes between "Fast Compile" (default setting) and "Consistent Compile".

Fast Commissioning mode with "Fast Compile"can be used for minor software changes to the Safety program, e.g. for testing and commissioning. It enables a fast compile, as only the F-blocks created by the user are compiled here.

In contrast, the Fast Commissioning mode with "Consistent Compile" can be used, for example, at the end of commissioning to compile the safety program consistently and then download it consistently to the F-CPU. In this case, you forego the advantage of the fast compiling, but after downloading the safety program to the F-CPU, you can enable safety mode again immediately with a short STOP-RUN transition of the F-CPU.

> **Note**
>
> Do not switch the F-CPU to STOP in Fast Commissioning mode with "Fast Compile". Otherwise, the F-CPU does not restart afterwards because the F-CPU contains an inconsistent safety program.
>
> Solution:
>
> - Download a consistent safety program to the F-CPU and then carry out a STOP-RUN transition. The deactivated safety mode is hereby terminated.
> - If your F-CPU supports "Consistent Compile", select "Consistent Compile" and download the safety program consistently to your F-CPU. After that, a STOP-RUN transition is possible.

> **Note**
>
> Fast Commissioning mode with "Fast Compile" behaves differently with S7-PLCSIM than with a real F-CPU.
>
> An S7-PLCSIM restarts after a STOP.

##### Requirements

To activate and use Fast Commissioning mode, the following requirements must be met:

- You can use Fast Commissioning mode with "Fast Compile" as of Safety System version V2.4. It is available for S7-1200 F-CPUs as of firmware V4.5 and for S7-1500 F-CPUs as of firmware V2.0.
- You can use the Fast Commissioning mode with "Consistent Compile" from Safety System version V2.5. It is only available for F-CPUs S7-1500 as of firmware V3.0. With S7-1500 F-Software Controller, it is available as of Safety System version V2.5 only for approved IPCs as of firmware V30.0.

  > **Note**
  >
  > **S7-1500 F-Software Controller**
  >
  > The approved IPCs can be found in the table in the [Product information for the F-CPUs](https://support.industry.siemens.com/cs/ww/en/view/109478599).
  >
  > If IPCs that have not been approved are used, an error or restart of the F Software Controller occurs. The download must then be repeated in STOP.
- The "Safety mode can be disabled" option must be selected in the "Settings" area of the Safety Administration Editor.
- The offline Safety program must be consistent and identical to the online Safety program.
- The F-CPU is in RUN.

##### Enabling Fast Commissioning mode

You enable Fast Commissioning mode by clicking the "Enable Fast Commissioning" button in the "General" area of the Safety Administration Editor.

Here, "Fast Compile" is selected as the default setting.

Once Fast Commissioning mode with "Fast Compile" is active, the behavior when compiling changes (shortcut menu "Compile > Software (only changes)" and "Compile > Hardware and software (only changes)") switches to the behavior when compiling changes in Fast Commissioning mode with "Fast Compile".

As soon as you change to the "Consistent Compile" setting, you can also compile the safety program consistently and download it to the F-CPU in RUN.

> **Note**
>
> After enabling Fast Commissioning mode, all other areas in the Safety Administration Editor are grayed out except the "General" area. Write access in the Safety Administration Editor is not permitted, also not via Openness. Read access is still possible.
>
> While Fast Commissioning mode with "Fast Compile" is activated, the Safety Administration Editor displays the information "Fast Commissioning is activated" as the status of the safety program.
>
> No signatures are calculated in Fast Commissioning mode with "Fast Compile". Therefore, no statement can be made in this mode about the status of the safety program and the F-blocks with regard to the offline-online comparison. The status of the signature comparisons is displayed with the ![Enabling Fast Commissioning mode](images/154067906827_DV_resource.Stream@PNG-de-DE.png) icon in this case.

##### Downloading changes in Fast Commissioning mode

To download changes to the Safety program to the F-CPU in RUN in Fast Commissioning mode, the following 3 conditions must be met:

- The F-CPU is in RUN.
- Safety mode is deactivated.
- Fast Commissioning is enabled.

If at least one of these 3 conditions is not met, the "Download" dialog displays a note that download in RUN mode is not possible.

> **Note**
>
> In case of a connection abort between the PG/PC and the F-CPU during loading in RUN mode, loading to the F-CPU can **not** be completed properly. Even the indicators of the safety program on the display and in the web server of the F-CPU are no longer current.
>
> A subsequent loading in RUN is no longer possible in this case, even though all requirements for Fast Commissioning mode are being met.
>
> Solution: Switch the F-CPU to STOP mode and download a consistent safety program to the F-CPU.

> **Note**
>
> If the work memory utilization of the F-CPU is > 80%, a download in RUN mode with "Consistent Compile" may be aborted and the download to the F-CPU may not be properly completed. Even the indicators regarding the safety program on the display and in the web server of the F-CPU are no longer current.
>
> A subsequent download in RUN is no longer possible, even though all requirements for Fast Commissioning mode are met.
>
> Solution: Switch the F-CPU to STOP mode and download a consistent safety program to the F-CPU.

##### Supported changes in Fast Commissioning mode

While Fast Commissioning mode is enabled, you cannot arbitrarily change your Safety program. The following is an overview of the supported changes.

- Changes to F-FBs/F-FCs/F-DBs. See "Changes not supported" for exceptions.
- Changes to fail-safe-compliant PLC data types. See "Changes not supported" for exceptions.
- Changes to the standard user program that influence the safety program, for example, DBs used in both the standard user program and the safety program.
- Creating and using F-blocks. See "Changes not supported" for exceptions.

##### Unsupported changes in Fast Commissioning mode with "Fast Compile"

While Fast Commissioning mode with "Fast Compile" is activated, you cannot make changes to your safety program at will. The following is an overview of the changes **not** supported .

| Type of change | System response |
| --- | --- |
| All changes to the hardware configuration. | A STOP is required for the download to the F-CPU. |
| Change in an F-FB/F-FC: |  |
| - Insertion of a new call of a time-processing instruction (for example, TON, TOF, TP, MUT_P...) or an ACK_OP/ACK_GL instruction. (Time value parameters can be reassigned in existing calls). | Compiling errors |
| - Insertion of a new call of a SENDDP/RCVDP instruction. |  |
| - Insertion of a new access to an F-I/O (access to a tag of the F-I/O DB or to the process image) that has not yet been used in the F-runtime group. |  |
| - Insertion of a new access to a communication with Flexible F-Link (access to a tag of the F-communication DB) which has not yet been used in the F-runtime group. |  |
| Deleting in an F-FB/F-FC: |  |
| - Deletion of a call of a time-processing instruction (for example, TON, TOF, TP, MUT_P...) or an ACK_OP/ACK_GL instruction. | Compiling errors when the instances are also deleted |
| - Delete a call to a SENDDP/RCVDP instruction. | Compiling errors |
| - Deletion of the last access to an F-IO (access to a tag of the F-I/O DB or to the process image) so that it is no longer used in the F-runtime group. |  |
| - Deletion of the last access to a communication with Flexible F-Link (access to a tag of the F-communication DB) so that it is no longer used in the F-runtime group. |  |
| Deleting an F-FB or F-FC when it was called before Fast Commissioning mode was activated. However, a call can be deleted. | Compiling errors |
| Deleting an F-DB when tags of this F-DB were already being used before Fast Commissioning mode was activated. | Compiling errors |
| Deleting a standard DB when tags of this DB were already being used for reading before Fast Commissioning mode was activated. | Compiling errors |
| Deleting a tag from the standard user program when it was already being used for reading before Fast Commissioning mode was activated. | Compiling errors |
| Structural changes of fail-safe-compliant PLC data types that are referenced in a Flexible F-Link communication. | Compiling errors |
| Creating library types of blocks | Compiling errors |
| Adding/deleting of: |  |
| - F-OBs | Compiling errors |
| - Flexible F-Link communications | Blocking in the Safety Administration Editor |
| - F-runtime groups (including changes) |  |
| - F-CD/F-MS connections (including changes) |  |
| Inserting an F-FB/F-FC (e.g. from a library or a different F-CPU) with global access to an F-DB. | Compiling errors |
| Changing the instruction version in the "Instructions" task card. | Compiling errors |
| Creating and changing instruction profiles |  |
| Downloading a Safety program compiled in Fast Commissioning mode from the F-CPU to the PG/PC. | Interlocking by loading the station from the device |
| Changes in the "Settings" area of the Safety Administration Editor. | Blocking in the Safety Administration Editor |
| Changes to the password for the safety program. |  |
| Renaming of the F-OB | Errors during download |
| All changes with Openness. (Name area SafetyAdministration) | Are rejected with an exception. |

> **Note**
>
> For the changes marked with "Compiling errors", the compiling of the safety program is aborted in Fast Commissioning mode. An additional note is displayed in the inspector window under "Info > Compile" indicating the F-block containing the unsupported change.

> **Note**
>
> The table "Unsupported changes in Fast Commissioning mode with Fast Compile" serves as an aid. When you see errors during compiling that refer to blocks that you have not programmed yourself, an unsupported change was most likely made. In this case, undo the previous changes or exit Fast Commissioning mode and compile the entire safety program.

> **Note**
>
> Logging in the F-change history is incomplete when Fast Commissioning mode with "Fast Compile" is activated, the following entries are not recorded:
>
> - Collective F-Signature
> - Compiling time stamp
> - Compiled F-blocks with signature and time stamp

##### Unsupported changes in Fast Commissioning mode with "Consistent Compile"

In Fast Commissioning mode with "Consistent Compile", you also cannot change your safety program at will. Compared to "Fast Compile", however, many more changes to the safety program are possible. The following is an overview of the changes **not** supported .

> **Note**
>
> Note that the changes mentioned here must not be present when enabling Fast Commissioning mode with "Consistent Compile". Therefore, make sure that the offline safety program is consistent and identical to the online safety program. If you do not observe this, the F-CPU may STOP.

| Type of change | System response |
| --- | --- |
| All changes to the hardware configuration. | A STOP is required for the download to the F-CPU. |
| Adding/deleting of: |  |
| - Flexible F-Link communications | Blocking in the Safety Administration Editor |
| - F-runtime groups (including changes) |  |
| Changes in the "Settings" area of the Safety Administration Editor. |  |
| Changes to the password for the safety program. |  |
| Renaming of the F-OB | CPU goes to STOP |
| All changes with Openness. (Name area SafetyAdministration) | Are rejected with an exception. |
| Insertion of a new call of an ACK_GL instruction. | Possible, but results in passivation of all F-I/Os. Reintegration is only possible with a STOP-RUN transition. |
| Insertion of a new access to an F-I/O (access to a tag of the F-I/O DB or to the process image) that has not yet been used in the F-runtime group. | Possible, but results in passivation of the affected F-I/O. Reintegration is only possible with a STOP-RUN transition. |
| Deletion of a call of an ACK_GL instruction. | Possible, but results in passivation of all F-I/Os. Reintegration is only possible with a STOP-RUN transition. |
| Deletion of the last access to an F-IO (access to a tag of the F-I/O DB or to the process image) so that it is no longer used in the F-runtime group. | Possible, but results in a diagnostic buffer entry via a "Profisafe communication error". |

##### Exiting Fast Commissioning mode

To exit Fast Commissioning mode with "Fast Compile" and return to Safety mode, proceed as follows:

1. Click on the "Deactivate Fast Commissioning" button.
2. Compile the Safety program with Software (rebuild all).
3. Download the Safety program to the F‑CPU. The F-CPU is set to STOP mode by this.

   In a redundant S7-1500HF system, you have to select "Stop R/H system" in the "Load preview" dialog.

After that, the online Safety program is consistent again and the F-CPU can be switched to RUN with Safety mode enabled.

To exit Fast Commissioning mode with "Consistent Compile" and return to Safety mode, proceed as follows:

1. Click on the "Deactivate Fast Commissioning" button.
2. Perform a STOP-RUN transition to enable safety mode again.

### F-change history

Enable the logging of changes of the safety-related project data by using the option "Enable F-change history" in the Safety Administration Editor.

An F-change history is created for each F-CPU in the project navigation under "Common data/logs".

The following is logged in the F-change history:

- Collective F-Signature
- User name
- Compile time stamp
- Download of the safety-related project data with time stamp
- Compiled F-blocks with signature and time stamp

The F-change history can contain a maximum of 5000 entries per F-CPU. When the 5000 entries are exceeded, a new F-change history is created using the naming scheme "F-change history <CPU name> YYYY-MM-DD hh:mm:ss".

After a project upgrade, the "Go to" function is not supported anymore for the F-change history of the project for the entries which were created before STEP 7 Safety V15.1.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| The connection between the F-CPU and the associated F-change history is made through the name of the F-change history.  Therefore, do not rename the F-CPU and the F-change history. If you rename the F-CPU or the F-change history, a new F-change history with the current name of the F-CPU is started. |  |

> **Note**
>
> You are not permitted to use the F-change history to identify changes of the safety-related project data for acceptance of changes.
>
> To accept changes, proceed as described under [Acceptance of Changes](#acceptance-of-changes).

> **Note**
>
> We recommend activating the F-change history before changing over to productive operation.

## System acceptance

This section contains information on the following topics:

- [Overview of System Acceptance](#overview-of-system-acceptance)
- [Correctness of the safety program including hardware configuration (including testing)](#correctness-of-the-safety-program-including-hardware-configuration-including-testing)
- [Completeness of the safety summary](#completeness-of-the-safety-summary)
- [Compliance of the system library elements used in the safety program with Annex 1 of the Report for the TÜV certificate](#compliance-of-the-system-library-elements-used-in-the-safety-program-with-annex-1-of-the-report-for-the-tüv-certificate)
- [Compliance of the know-how protected F-blocks used in the safety program with their safety summary.](#compliance-of-the-know-how-protected-f-blocks-used-in-the-safety-program-with-their-safety-summary)
- [Completeness and correctness of the hardware configuration](#completeness-and-correctness-of-the-hardware-configuration)
- [Completeness and correctness of the communication configuration](#completeness-and-correctness-of-the-communication-configuration)
- [Identity of online and offline program](#identity-of-online-and-offline-program)
- [Other characteristics](#other-characteristics)
- [Acceptance of Changes](#acceptance-of-changes)

### Overview of System Acceptance

#### Introduction

When performing a system acceptance test, all the standards and guidelines (for example PROFINET Installation Guidelines) relevant to the specific application must be complied with. This also applies to systems that are not "subject to acceptance". For the acceptance, you must consider the requirements in the [Certification Report](http://support.automation.siemens.com/WW/view/en/49368678/134200).

As a general rule, the acceptance of an F-System is performed by an independent expert. The independence required of the expert must be defined in the safety plan and depends on the required PL/SIL.

Observe all warnings in this manual.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The configuration of F-CPUs and F-I/Os as well as the programming of F-blocks must be carried out in TIA Portal as described in this documentation.You must observe all aspects described in the section [System acceptance](#system-acceptance) to ensure safe operation with the SIMATIC Safety system. Any other procedures are not permitted. (S056) |  |

#### Proof of the correct implementation of the safety-related project data

In order for a system acceptance to be granted, you must assess and document the correctness of the individual components. For documentation of the component characteristics, you must create the safety summary.

The following characteristics must be covered:

- [Correctness of the safety program including hardware configuration (including testing)](#correctness-of-the-safety-program-including-hardware-configuration-including-testing)
- [Completeness of the safety summary](#completeness-of-the-safety-summary)
- [Compliance of the system library elements used in the safety program with Annex 1 of the Report for the TÜV certificate](#compliance-of-the-system-library-elements-used-in-the-safety-program-with-annex-1-of-the-report-for-the-tüv-certificate)
- [Compliance of the know-how protected F-blocks used in the safety program with their safety summary.](#compliance-of-the-know-how-protected-f-blocks-used-in-the-safety-program-with-their-safety-summary)
- [Completeness and correctness of the hardware configuration](#completeness-and-correctness-of-the-hardware-configuration)
- [Completeness and correctness of the communication configuration](#completeness-and-correctness-of-the-communication-configuration)
- [Identity of online and offline program](#identity-of-online-and-offline-program)
- [Other characteristics](#other-characteristics) such as software version, use of data from the standard user program

After the acceptance, you should archive all relevant documents and also the project data so as to make the accepted project available as a reference for a subsequent acceptance.

#### Safety summary

The [safety summary](#creating-a-safety-summary) is the documentation of the project that is required for system acceptance

### Correctness of the safety program including hardware configuration (including testing)

The correctness of software cannot only be ensure through tests and verifications during commissioning, but rather already requires the observance of a wide variety of measures during creation. Also see warning S062 on this in chapter "[Overview](#overview)".

#### Verification/function test

Already during the creation, you will [test](#testing-the-safety-program) your safety program and the associated hardware configuration. You must carry out these tests with regard to the specification of your safety functions and document them before you perform the system acceptance.

To allow you to perform a code review of your safety program and to document the accepted program code, the source code of all F-blocks is printed as part of the [safety summary](#creating-a-safety-summary), provided you have selected the option "All" for the printout.

If you want to carry out a function test after loading, you have to carry out program identification. More information is available in "[Downloading project data](#downloading-project-data)".

The correct function of the safety program must be guaranteed by complying with all steps from the "[Overview of System Acceptance](#overview-of-system-acceptance)" chapter before it can be used productively. When using configuration control (option handling), you must ensure correct operation of the safety program for all possible station options by performing appropriate functional tests. You should archive the test reports along with the safety summary and the acceptance documents.

Times, for example [monitoring times](#monitoring-and-response-times) and delay times, can only be verified to a limited extent with [functional tests](#downloading-project-data). For this reason, you should check these times selectively to determine whether they are dimensioned correctly, for example, using the safety summary.

Some of these times are itemized specifically in the safety summary, for example, the F‑monitoring time (for communication between F‑CPU and F‑I/O) and the monitoring time of the safety-related CPU‑CPU communication (TIMEOUT). To determine the monitoring times derived under normative conditions, the Excel file for response time calculation is available on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109783831). These have to be considered together with the practically determined conditions of the application. Note that these monitoring times have an impact on the response times of your safety functions.

#### Consistency of the safety program

Check in the "General information" section of the safety summary to determine whether the safety program was recognized as "consistent".

This is the case for S7-300/400 F-CPUs only if the following signatures are also identical:

- Collective F-Signature ("General information" section, "Collective F-Signature")
- "Signature of F-blocks with F-attribute" ("General information" section, "Current compilation")

Consistency of the safety program is required for the acceptance. If the signatures are not identical, you have the possibility to establish consistency by recompiling the safety program and re-creating the safety summary.

### Completeness of the safety summary

#### Introduction

When you have an acceptance-ready version of your safety-related project data, you must perform and document additional checks of the safety summary to prove that the safety summary is complete and belongs to the safety program to be accepted.

#### Creating a safety summary

Follow the procedures described in [Creating a safety summary](#creating-a-safety-summary) to create the safety summary. In so doing, use the option "All" to include the source code of your F-blocks in the documentation.

If you use named value data types or global constants in your safety program, you must document these separately. To do so, mark the "PLC data types" or "PLC tags" folder in the project tree and call up the print function.

#### Checking the safety summary for completeness

If you want to use an existing safety summary whose completeness is not exactly known, you must check to determine whether the same Collective F-Signature is contained in the footer on all pages of the safety summary. This allows you to prove that all included pages belong to the same project.

In section "Supplementary information", you can find the number of pages in the safety summary, among other things. With this, you can prove that all pages of the safety summary are present. You must not use incomplete safety summary (for example, from a printer low on toner) for an acceptance.

If you created the safety summary with the "All" option, the source code of all F-blocks will also be printed. The printout of this source code also contains the footer to enable you to easily assign the source code to safety summary.

The information "Number of pages in the safety summary" does not include the pages on which the source code of the F-blocks is output.

#### Association with the safety program

In the "General information" section of the safety summary, check whether the Collective F-Signature corresponds online and offline to the Collective F-Signature of the safety program to be accepted in the work area of the Safety Administration Editor under "General". If they are not the same, then the summary and safety program do not match.

### Compliance of the system library elements used in the safety program with Annex 1 of the Report for the TÜV certificate

#### Introduction

STEP 7 Safety contains LAD/FBD instructions for programming of your safety program as well as F-system blocks for creating an executable safety program that have been created and tested by SIEMENS and certified by TÜV. The F-system blocks used are automatically inserted by the F-system based on the set safety system version (see section ["Settings" area](#settings-area)).

To allow you to check whether the used versioned LAD/FBD instructions and F-system blocks correspond to Annex 1 of the Report for the TÜV certificate and to the versions you intend to use, these are listed in the safety summary.

#### Procedure

To check, download the current Annex 1 of the report for the TÜV certificate "SIMATIC Safety" from the [Internet](http://support.automation.siemens.com/WW/view/en/49368678/134200).

Proceed as follows for the check:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| - (S7-1200, S7-1500) The versions of the versioned LAD/FBD instructions listed in the safety summary in the section "System library elements used in safety program" must correspond to the versions in Annex 1 of the Report for the TÜV certificate. - (S7-300, S7-400) The versions, signatures and initial value signatures of the versioned LAD/FBD instructions and F‑system blocks listed in the safety summary in the section "System library elements used in safety program" must correspond to the versions, signatures and initial value signatures in Annex 1 of the Report for the TÜV certificate. - The versions of the versioned LAD/FBD instructions listed in the safety summary must meet the safety requirements of your application.   Keep in mind possible differences in functionality of different versions specified in the section for the respective instruction. - The safety system version listed in the safety summary under "Safety program settings" must match the versions in Annex 1 of the Report for the TÜV certificate. (S054) |  |

In case of discrepancies, recheck whether you have the correct versions.

(S7-300, S7-400) Differences can also arise when there are F-blocks / instructions in your safety program that are not used.

### Compliance of the know-how protected F-blocks used in the safety program with their safety summary.

If you use know-how protected F-blocks (for example, from libraries) to program your safety program, the source code for these is not printed in the safety summary.

Therefore, the author of the know-how protected F-block must already carry out acceptance of the F-block and provide the following information:

#### S7-300/400 F-CPUs

- Signature and initial value signature of the know-how protected F-block
- Versions of all the used versioned LAD/FBD instructions
- Signatures and initial value signatures of all called F-blocks
- Signatures of all F-DBs accessed by the fail-safe block to be reused.

For system acceptance, you must perform the following checks using the safety summary:

- The signature and initial value signature of each know-how protected F-block listed in the safety summary in the section "F-blocks in safety program" must correspond to the signature and initial value signature documented by the author.
- The versions of the versioned LAD/FBD instructions listed in the safety summary in the section "System library elements used in safety program" must correspond to the versions of each know-how protected F-block documented by the author or must be functionally identical with them.
- The signatures and initial value signatures of the F-blocks called in each know-how protected F-block listed in the safety summary in the section "F-blocks in safety program" must correspond to the signatures and initial value signatures (of the called F-blocks) documented by the author.

In case of differences, set the documented (or functionally identical) versions and use the F-blocks with the documented signatures and initial value signatures. If the version conflicts cannot be eliminated due to other dependencies, contact the author of the know-how protected block in order to obtain a compatible approved version.

#### S7-1200/1500 F-CPUs

- Signature of the know-how protected F-block
- Safety system version that was set while setting up the know-how protection
- Versions of all the used versioned LAD/FBD instructions
- Signatures of all called F-FBs/F-FCs in the know-how protected F-block.
- Signatures of all F-DBs accessed by the know-how protected F-block.

For system acceptance, you must perform the following checks using the safety summary:

- The signature of each know-how protected F-block listed in the safety summary in the section "Know-how protected F-blocks in the safety program" must correspond to the signature documented by the author.
- The safety system version of each know-how protected F-block listed in the safety summary under "Know-how protected F-blocks in the safety program" must correspond to one of the versions listed in Annex 1 of the Report for the TÜV certificate.
- The versions of the versioned LAD/FBD instructions of each know-how protected F-block listed in the safety summary in the section "Know-how protected F-blocks in the safety program" must correspond to the versions documented by the author or must be functionally identical with them.
- The signatures of the F-blocks called in each know-how protected F-block listed in the safety summary in the section "Know-how protected F-blocks in the safety program" must correspond to the signatures (of the called F-blocks) documented by the author.

In case of differences, set the documented (or functionally identical) versions and use the F-blocks with the documented signatures. If the version conflicts cannot be eliminated due to other dependencies, contact the author of the know-how protected block in order to obtain a compatible approved version.

### Completeness and correctness of the hardware configuration

#### Introduction

The hardware configuration is an essential component of the project to be accepted. With the configuration of the hardware, you have set properties that can influence the safety of signals. You must document these settings with the safety summary to prove that you fulfill the safety requirements of your application.

The section "Hardware configuration of F-I/O" is available in the safety summary for this. This section consists of several tables:

- A table with information about the F‑CPU and about the ranges of F‑destination addresses used and the "Central F-source address" of the F-CPU
- Overview tables with the F-I/O used
- A table for each F‑I/O with information on the F-I/O and all parameters of the F-I/O with the configured values

Because the user administration of the web server is also part of the hardware configuration, the assignment of the "F-Admin" right must be checked. You can only check the assignment of the "F-Admin" right in the Safety Administration Editor in the "Web server F-admins" area.

For S7-1500 F-CPUs as of Firmware V3.1, check the assignment of the "F-Admin" right in the Runtime rights of the respective F-CPU in the "Users and roles" area.

> **Note**
>
> Note that you will find F‑I/O that you address via safety-related I‑slave-slave communication in the safety summary of the F-CPU of the I-slave and not in the safety summary of the F-CPU of the assigned DP master.
>
> The safety summary of the F-CPU of the DP master contains a note in the overview table for this F-I/O indicating that it is not assigned to this F-CPU.

> **Note**
>
> **When using shared devices:**
>
> Note that F-I/O that you address in a shared device can be found in the safety summary of the F-CPU of the IO controller to which it is assigned.
>
> The safety summary of the other F-CPUs (IO controllers) that share the cross-project shared device contains a note in the overview table for this F-I/O indicating that it is not assigned to this F-CPU.

#### Procedure for checking that the hardware configuration is complete

Check whether the safety summary contains all the configured F-I/O. Also make sure that there is no F-I/O that you have not configured as belonging to this F-CPU.

> **Note**
>
> If configuration control (option handling) is used, the safety summary must contain all the F-I/O of the maximum configuration. The following checks are to be carried out for al the F-I/Os of the maximum configuration.

#### Procedure for checking the correctness of the hardware configuration using the safety summary

To check the hardware configuration for correctness, proceed as follows:

| Symbol | Meaning |
| --- | --- |
| 1. Check in the "Hardware configuration of F-IO" section to verify the uniqueness of the PROFIsafe addresses.    See sections [PROFIsafe addresses for F-I/O of PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1) or [PROFIsafe addresses for F-I/O of PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2), [Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices](#peculiarities-when-configuring-fail-safe-gsd-based-dp-slaves-and-fail-safe-gsd-based-io-devices) and [Recommendation for PROFIsafe address assignment](#recommendation-for-profisafe-address-assignment).    - Check if the "Central F-source address" parameter of the individual F-CPUs differs network-wide. F-CPUs to which solely F-IOs of the PROFIsafe address type 1 are assigned do not have to be considered during this check.    - For F-I/Os of PROFIsafe address type 1 check whether the F-destination addresses comply with the following warning:        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | F-I/Os of PROFIsafe address type 1 are uniquely addressed by their F-destination address (e.g. with the switch setting on the address switch). The F-destination address (and therefore also the switch setting on the address switch) of the F-I/O must be unique network-wide* and CPU-wide**/*** (system-wide) **for the entire** F-I/O. The F-I/O of PROFIsafe address type 2 must also be considered. (S051) |  |       * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).      ** "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.      *** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU with regard to the PROFIsafe addresses. Therefore, the "Central F-source address" is set identically by the system for both F-CPUs.        | Symbol | Meaning |      | --- | --- |      | **Note**  For more information on the assignment of PROFIsafe addresses that are unique for the CPU and across the network, see this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109740240). |  |    - For F-I/Os of PROFIsafe address type 2 check whether the F-destination addresses comply with the following warning:        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | F-I/O of PROFIsafe address type 2 is uniquely addressed using a combination of F-source address ("Central F-source address" parameter of the assigned F-CPU) and F-destination address.  The combination of F-source address and F-destination address for each F-I/O must be unique network-wide* and CPU-wide**/*** (system-wide). In addition, the F-destination address must not be occupied by F-I/O of PROFIsafe address type 1. If you use a [supported configuration](#configurations-supported-by-the-simatic-safety-f-system), you only have to ensure that the "Central F-source address" parameter of all F-CPUs is unique network-wide*. (S052) |  |       * A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).      ** "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.      *** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU with regard to the PROFIsafe addresses. Therefore, the "Central F-source address" is set identically by the system for both F-CPUs.        | Symbol | Meaning |      | --- | --- |      | **Note**  For more information on the assignment of PROFIsafe addresses that are unique for the CPU and across the network, see this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109740240). |  |    - Check whether the PROFIsafe addresses of fail-safe GSD based DP slaves / GSD based I/O devices comply with the following warning:        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | Check the documentation for your fail-safe GSD based DP slaves / fail-safe GSD based I/O devices to find out the valid PROFIsafe address type. If you do not find the necessary information, assume PROFIsafe address type 1. Proceed as described under [PROFIsafe addresses for F-I/O of PROFIsafe address type 1](#profisafe-addresses-for-f-io-of-profisafe-address-type-1) or [PROFIsafe addresses for F-I/O of PROFIsafe address type 2](#profisafe-addresses-for-f-io-of-profisafe-address-type-2). Set the F-source address for fail-safe GSD based DP slaves / fail-safe GSD based I/O devices according to the manufacturer's specifications. If the F-source address needs to correspond to the "Central F-source address" parameter of the F-CPU (PROFIsafe address type 2), you will find the latter in the "Properties" tab of the F-CPU. In this case, check the safety summary to verify that the value for the "Central F-source address" parameter corresponds to the value of the F-source address of the fail-safe GSD based DP slave/fail-safe GSD based I/O device. (S053) |  | 2. Check the safety-related parameters (including F-monitoring time or F_WD_Time) of all configured F-I/O.    You can find these parameters in the "Hardware configuration of F-I/O" section in the detailed tables for the F-I/O.     The table consists of two parts:     - The left part contains the parameters which refer to the F-I/O itself ("Module data").    - The right part contains the parameters of the individual channels ("Channel parameters")These parameters must be set as prescribed by the safety requirements of your application.    When using fail-safe GSD based DP slaves/GSD based I/O devices, note the relevant documents for the possible additional safety-related (technological) parameters.      | Symbol | Meaning |    | --- | --- |    | **Note**  F-I/O that are to be assigned the same safety-related parameters (except for PROFIsafe addresses) can be copied during configuration. Except for the PROFIsafe addresses, you no longer have to check the safety-related parameters individually. It is sufficient to compare the "F-parameter signature (without addresses)" in the "Hardware configuration of the F‑I/O" section in the overview table. This also applies to fail-safe GSD based DP slaves/GSD based I/O devices without i-parameters. For GSD based DP slaves/GSD based I/O devices with i-parameters, it might be that the "F-parameter signature (without addresses)" does not match, even though all safety-related parameters, except for the PROFIsafe addresses, do match. In this case, you need to compare all safety-related parameters. Exception: For F-I/Os that do not support the "RIOforFA-Safety" profile, you also need to compare the "Behavior after channel fault" parameter, if any, additionally to the "F-parameter signature (without addresses)". |  | 3. Check whether the article numbers of the F-I/O in the safety summary correspond to the article numbers of the F-I/O actually present in the system. If the article numbers are different, the F-I/O present must be compatible as a replacement part for the F-I/O listed in the safety summary. 4. For non-supported configuration, see [Configurations supported by the SIMATIC Safety F-system](#configurations-supported-by-the-simatic-safety-f-system).      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | Note the following when using configurations that are not included in supported configurations: - Make sure that the F-I/O of this configuration appears in the safety summary and that an F-I/O DB has been created for it. Otherwise, you cannot use the F-I/O in this configuration. - For F-I/O in the PROFINET IO environment**, you must check the safety summary for correctness of the PROFIsafe operating mode parameter (F_Par_Version). V2 mode must be set in the PROFINET IO environment. F-I/O which only support V1 mode must not be used in the PROFINET IO environment. - You must ensure that the PROFIsafe address assignment is unique CPU-wide*/**** and network-wide***:    - Check the safety summary for correctness of the PROFIsafe addresses.   - For F-I/O of PROFIsafe address type 2, check the safety summary to verify that the F-source address corresponds to the "Central F-source address" parameter of the F-CPU.   - For F-I/O of PROFIsafe address type 1 or if you cannot set the F-source address to match the "Central F-source address" parameter of the F-CPU, you must ensure the uniqueness of the PROFIsafe address through the unique assignment of the F-destination address alone.In an unsupported configuration, you must check the uniqueness of the F-destination address individually for each F-I/O using the safety summary.    (S050) |  |     * "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.    ** The F-I/O is located in the "PROFINET IO environment" if at least part of safety-related communication with the F-CPU takes place via PROFINET IO. If the F-I/O is connected via I-slave-slave communication, also keep in mind the communication line to the DP master/IO controller.    *** A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).    **** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU with regard to the PROFIsafe addresses. Therefore, the "Central F-source address" is set identically by the system for both F-CPUs.      | Symbol | Meaning |    | --- | --- |    | **Note**  For more information on the assignment of PROFIsafe addresses that are unique for the CPU and across the network, see this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109740240). |  | 5. Check in the Safety Administration Editor, the standard printout of the project data or the local user management that only authorized persons have "F-Admin" rights.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | The "F-Admin" authorization for the Web server (including Web server API) without password protection (user "Everybody", or user "Anonymous" when using local user management) is intended only for testing, commissioning, etc. This means only when the system is not in productive operation. In this case, you must ensure the safety of the system through other [organizational measures](#glossary). Before the transition into productive operation, you must remove "F-Admin" rights and "Full access incl. fail-safe access" from the "Everybody" or "Anonymous" user. The password Web server user with "F-Admin" right may only be disclosed to authorized persons. After downloading the hardware configuration, check whether only permitted users of the web server have the "F-Admin" right on the F-CPU. To do so, use the online mode of the Safety Administration Editor for an F-CPU without local user management, or the "Security setting\Users and roles" tab for an F-CPU with local user management. Saving the login file and the password of the Web server in the browser is only permitted when usage by unauthorized persons is prevented through other [organizational measures](#glossary).  If you use the ticket mechanism, handling of the tickets must be just as restrictive as handling of the user password of the web server with the "F-Admin" right. (S064) |  | |  |

---

**See also**

[“Web server F-Admins” area (S7-1200, S7-1500)](#web-server-f-admins-area-s7-1200-s7-1500)

### Completeness and correctness of the communication configuration

#### Introduction

Safety-related communication is based on the mechanisms of the standard communication of STEP 7.

To ensure that errors which standard communication does not discover are detected, safety-related communication connections between F-CPUs are secured. Further parameters are required for this, which you have to document and check on acceptance.

For this purpose, the "Block parameters for safety-related CPU‑CPU-communication" and "Communications via Flexible F-Link Overview" sections are available in the safety summary. The section "Block parameters for safety-related CPU‑CPU-communication" contains up to two tables (for communication via PROFIBUS DP or PROFINET IO and for communication via S7 connections). The section "Communications via Flexible F-Link Overview" contains a table with an overview of the connection configurations and a "Communications via Flexible F-Link for UDT" table for each used F-compliant PLC data type (UDT).

Not all safety-related communication is available for all F-CPUs. For more information, refer to the section "[Safety-related communication](#safety-related-communication)".

> **Note**
>
> The statements made regarding communication via Flexible F-Link in this section also apply when this communication is used between F-runtime groups.

#### Procedure for checking for correctness of the communication configuration

**Observe the following warning for safety-related communication with the SENDS7/RCVS7 instructions:**

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value of the respective F-communication ID (input R_ID; data type: DWORD) can be freely selected; however, it must be odd and unique for all safety-related communication connections network-wide* and CPU-wide. The value R_ID + 1 is internally assigned and must not be used.  You must supply inputs ID and R_ID with constant values when calling the instruction. Direct read or write access to ID and R_ID in the associated instance DB is not permitted in the safety program. (S020) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

**Observe the following warning for safety-related communication with the SENDDP/RCVDP instructions:**

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide**** at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".

*** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase.

**** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one single F-CPU with regard to the DP_DP_ID.

**Observe the following warnings for communication via Flexible F-Link:**

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When a new Flexible F-Link communication is created in the Safety Administration Editor, a unique F-communication UUID for the communication is provided by the system. By copying communications in the Safety Administration Editor within the parameterization table or when copying to another F-CPU, the F-communication UUIDs are not regenerated and are therefore not unique anymore. If the copy is used to configure a new communication relationship, you yourself must ensure the uniqueness. To do this, select the affected UUIDs and regenerate via the "Generate UUID" shortcut menu. The uniqueness must be checked in the safety summary during acceptance. (S087) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For each communication connection via Flexible F-Link, you must check that the offsets of the elements of the F-compliant PLC data type (UDT) used for the communication connection match on the transmit and receive sides when you accept the safety program.    You can find the offsets in the respective safety summary. To do this identify the communication connection by means of the UUID. (S088) |  |

### Identity of online and offline program

Once you have checked all properties of the offline safety program you must ensure that the safety program is identical on the F-CPU on which it is supposed to be run.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| In a redundant S7-1500HF system, you must perform the verification of identity of the online and offline program in RUN-Redundant mode. In so doing, it is sufficient to perform the verification only for one S7-1500 HF-CPU. (S098) |  |

1. Connect online with the F-CPU. If multiple F‑CPUs can be reached over a network (e.g. Industrial Ethernet) by the programming device / PC, you have to ensure that you are connected with the correct F‑CPU. For example with "Online & diagnostics" > "Online accesses " > "Flash LED".
2. Open the Safety Administration Editor.
3. Check whether the online and offline Collective F-Signatures correspond to the Collective F-Signature from the safety summary.
4. Now check in the "General" area under "Safety program status" whether the safety programs are identical online and offline.

   Use the "Status" and "Version comparison" display to check which situation you are dealing with and, if necessary, execute the recommended measure:

   | Status | Version comparison | Statement | Measure |
   | --- | --- | --- | --- |
   | ![Figure](images/69410581259_DV_resource.Stream@PNG-de-DE.png) | Not relevant | The safety programs are different. | - Ensure that you are connected with the desired F-CPU. - Download the safety program to the F‑CPU. |
   | ![Figure](images/69409204235_DV_resource.Stream@PNG-de-DE.png) | ![Figure](images/69410581259_DV_resource.Stream@PNG-de-DE.png) | The safety programs are identical but different versions of F-blocks are used. | The safety program must be downloaded to the F-CPU for the latest versions to become effective. |
   | ![Figure](images/69409204235_DV_resource.Stream@PNG-de-DE.png) | ![Figure](images/69409204235_DV_resource.Stream@PNG-de-DE.png) | The safety programs are identical. | None |

Keep in mind that only a change comparison will provide reliable information as to whether the safety programs are identical. The display of signatures is used for quick identification of changes.

### Other characteristics

#### Introduction

In addition, you must check a few more characteristics that are also relevant for the acceptance of the project.

#### Plausibility check for data transfer from the standard program to the safety program

Check to determine whether a plausibility check was programmed for all data transferred from the standard user program to the safety program. For this purpose, the "Data from the standard user program" section lists all tags of the standard user program that you are reading in the safety program. Tags of the standard user program that you are writing in the safety program are not listed here because a plausibility check is not required for them. For more information, refer to the S015 warning in section "[Data Transfer from Standard User Program to Safety Program](#data-transfer-from-standard-user-program-to-safety-program)".

#### Multiple call of an F-FB or an instruction with the same instance (single instance or multi-instance)

Check whether you used a separate instance for each call of an F-FB or an instruction.

Multiple calls with the same instance are usually not worthwhile and require special care:

For example, if you explicitly transfer an operand (for example, as a constant) in the 1st call to the instance, and there is no explicit transfer in the 2nd call (so that the start value is valid), you must verify which value in the 2nd call is valid for this operand. Also consider startup processes in this regard; higher priority OBs or similar in which the 1st call may be present.

#### Checking the program version

Check whether the version of STEP 7 Safety used to create the summary (in the footer of the printout) is as least as high as the version used to compile the safety program. You can find the latter version in the section "General information" of the safety summary under "Used versions". Both versions must be listed in Annex 1 of the Report for the TÜV certificate.

#### Ability to disable safety mode

Make sure that safety mode cannot be disabled. For information about this, refer to section "General information" under "Safety program settings". This setting ensures that the safety mode of the safety program cannot be disabled inadvertently. For more information, refer to the S027 warning in section "[Disabling safety mode](#disabling-safety-mode-1)".

#### Safety system version with an S7-1500 HF-CPU

Check whether the safety system version is V2.4 or higher when using an S7-1500 HF-CPU.

For information about this, refer to section "General information" under "Safety program settings".

#### Access protection

Check in the "General information" section under "Access protection" to determine whether the setting for access protection is permitted. Note the following warnings.

Otherwise, the project must not be accepted, because the safety program in the F-CPU is not protected against unauthorized accesses.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-300, S7-400) In productive operation, it must be prevented that changes to the standard user program are unintentionally made in the safety program as well. For this purpose, you must configure the protection level "Write protection for fail-safe blocks" and configure a password for the F‑CPU.  With the "Write protection" or "Write/read protection" protection level, the password would apply to the standard and the safety program. (S001) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| (S7-1200, S7-1500) In productive operation, the safety-related project data must be protected against unintentional changes.  If you use local user management, the Runtime rights "F-Admin" and "Full access with fail-safe access" and the engineering right for user management may only be granted to authorized users. You must also limit the assignment of user rights to trained personnel.  If you are not using local user management or if legacy mode is enabled, then, at a minimum, configure protection level "Full access (no protection)" and assign a password under "Full access with fail-safe (no protection)". This protection level allows full access only to the standard user program and not the safety program.  If you select a higher protection level, for example to protect the standard user program, you must assign an additional password for "Full access (no protection)".   Assign different passwords for the individual access levels. (S041) |  |

### Acceptance of Changes

#### Introduction

In general, you can adopt the same approach for the acceptance of changes as the initial acceptance (see [Overview of System Acceptance](#overview-of-system-acceptance)).

You have to check the entire safety-related project data (safety program and safety-related hardware configuration) for changes and determine the safety-related project data to be validated and approved as part of an impact analysis.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| In the case of acceptance of changes, you must check whether the intended changes were made correctly and completely.  You must also check whether unintentional changes may have been made at another location (for example, F-I/O or instructions that were added). (S072) |  |

To avoid the acceptance of the entire system in case of negligible changes, STEP 7 Safety helps you to identify those parts of your safety program that have changed.

To accept changes, proceed as follows:

1. Localize the changes in the safety-related project data:

   - changed or newly added F-blocks
   - changed or newly added instructions and F-system blocks
   - safety-related parameters of the changed or newly added F-I/O
   - structure of the safety-related hardware configuration (e.g. slot positions or start addresses of the F-I/Os)
   - changed safety-related communication via Flexible F-Link
2. From these changes, determine the safety-related project data affected by them (impact analysis). This can also be safety-related project data that has not been changed.
3. Then you carry out a validation and acceptance of the safety-related project data affected by the changes.

> **Note**
>
> Acceptance of changes is not possible after CPU migration.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When you make changes in which the assignment of input/output addresses and wiring can change, then you must perform a [wiring test](#testing-the-safety-program-1).  Examples for such changes are:  - Adding F-I/O - Changing the start address of F-I/O - Changing the slot position of F-I/O - Changing   - the rack   - the slave/device address   - the PROFIBUS DP/PROFINET IO subnet   - the IP address   - the device name    (S071) |  |

#### Localization of changes in the safety-related project data

To be able to localize relevant changes, you need two TIA projects:

- Reference project: Contains the initially accepted project data. They are the starting point for the upcoming comparison.
- Project to be accepted: Contains the current safety-related project data. It is the result of the reference project and the changes made in it.

To localize changes you have to compare the safety-related project data from the reference project with the safety-related data of the project to be accepted.

The Collective F-Signature is a quick first step to determine whether relevant changes have been made. If the signature has changed, relevant changes are present in the safety-related project data.

(S7-1200, S7-1500) You can now use the Collective F-SW-Signature, the Collective F-HW-Signature and the F-Communication Address Signature to narrow down whether these changes are contained in the safety program (Collective F-SW-Signature changed) and/or in the safety-related hardware configuration (Collective F-HW-Signature) and/or in the communication data (with Flexible F-Link, F-Communication Address Signature).

#### Localization of changes in the safety program

(S7-1200, S7-1500) A quick possibility to detect changes in the safety program is the comparison of the Collective F-SW-Signature of the safety-related project data in the reference project with the Collective F-SW-Signature in the safety-related project data in the project to be accepted. If they differ from each other, this means that there are changes in the safety program which need to be validated and, if necessary, accepted.

To localize changes in the safety program, perform an offline-offline comparison between the safety program to be accepted of the project to be accepted and the safety program of the reference project (see [Comparing Safety Programs](#comparing-safety-programs)). Use filter setting "Compare only F‑blocks relevant for certification". This limits the output of the comparison to the relevant F-blocks.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Make sure that the comparison criterion "Safety" is enabled so that the criteria relevant for an acceptance of changes are taken into consideration in the comparison. (S069) |  |

By disabling the remaining comparison criteria, you can deselect those differences that are irrelevant for the acceptance of changes (e.g. time stamp).

The status of the comparison helps you to identify which F‑blocks were changed.

(S7-1200, S7-1500) As an alternative to the offline-offline comparison, you can localize the changes in the safety program by comparing the group signatures. Use the safety summary of the reference project and of the project to be accepted for this purpose. Groups with an unchanged signature indicate that no F-blocks in them or lower-level groups have been changed. In groups with a changed group signature, you can localize the changed F-blocks using their changed block signature. Note that the assignment of fail-safe blocks to groups is not recorded by the Collective F-Signature.

#### Localization of changes in the safety-related hardware configuration

(S7-1200, S7-1500) A quick possibility to detect changes in the safety-related hardware configuration is the comparison of the Collective F-HW-Signature of the safety-related project data in the reference project with the Collective F-HW-Signature of the safety-related project data in the project to be accepted. If they differ from each other, this means that there are changes in the safety-related hardware configuration which need to be validated and, if necessary, accepted.

(S7-1200, S7-1500) If the Collective F-HW-Signature has changed and all F-IOs are unchanged, this indicates that safety-related parameters of the F-CPU have changed, or that the structure of the safety-related hardware configuration has changed, for example, slot positions.

There are two possible ways for localizing safety-related changes in the safety-related hardware configuration:

- Localization by offline-offline comparison
- Localization by comparison of two safety summaries

How to do this is described below.

**Localization by offline-offline comparison**

The reference project and the project to be accepted must be consistent and compiled for a comparison. To perform the comparison, see [Comparing Safety Programs](#comparing-safety-programs).

1. Navigate in the comparison result to the "System blocks > STEP 7 Safety > F-I/O DBs" folder. All data blocks listed in this folder are F-I/O-DBs and are each assigned to an F-I/O.

   - If the F-I/O-DBs in the comparison result are identical, this means that the safety-related configuration of the assigned F-I/O was also not changed. Standard-parameters might have changed.
   - If the F-I/O-DBs in the comparison result are not identical, this means that the safety-related configuration of the assigned F-I/O was also changed.
   - If F‑IO DBs in the comparison result are marked as "not existing", associated F-IOs might have been deleted or added or the name or start addresses of the F-IOs have been changed. In this case, you can find the assignment of an F-I/O DB to a specific F-I/O in the safety summary under "Hardware configuration of F-I/O".
2. If you have found changed F-I/O, you can check the changed parameters in the safety summary as described below.

**Localization by comparison of two safety summaries**

Carry out a comparison based on two safety summaries as follows:

1. In the section "Hardware configuration of the F-I/O" compare the start addresses (I/O addresses), the parameter "Behavior after channel fault" and the slot of the F-I/O.
2. In the "Hardware configuration of F-I/O" section in the overview table of the F-I/O used, compare the parameter CRCs of the F-I/O with those in the safety summary of the corresponding F-CPU from the reference project.

   - If the "Parameter signature (without addresses)" is different for an F-I/O, this indicates the existence of a change in the safety-related parameters of the F-I/O.

     In this case, check the corresponding detail table of the safety-related parameters of the F-I/O and verify the uniqueness of the PROFIsafe addresses.
   - If the "Parameter signature (w/o addresses)" is identical, only the PROFIsafe addresses have been changed.

     In this case it is sufficient to verify the uniqueness of the PROFIsafe addresses.

Check as described in section "[Completeness and correctness of the hardware configuration](#completeness-and-correctness-of-the-hardware-configuration)".

#### (S7-1200, S7-1500) Detecting changes in the communication with Flexible F-Link

A quick possibility to detect changes in the configuration of the communication with Flexible F-Link is the comparison of the F-communication address signature of the safety-related project data in the reference project with the F-communication address signature of the safety-related project data in the project to be accepted. If they differ from each other, this means that there are changes in the configuration of the communication (UUID only) with Flexible F-Link that must be validated and, if necessary, accepted. Other communication parameters such as timeout or transmission direction are covered by the Collective F-SW-Signature (see "Detection of changes in the safety program" above).

To localize changes in the configuration of the communication with Flexible F-Link, compare the table "Communications via Flexible F-Link Overview" of the reference project with that of the project to be accepted in the respective safety summary.

---

**See also**

[Accessing tags of the F-I/O DB](#accessing-tags-of-the-f-io-db)

## Operation and maintenance

This section contains information on the following topics:

- [Notes on startup of the F-system](#notes-on-startup-of-the-f-system)
- [Notes on Safety Mode of the Safety Program](#notes-on-safety-mode-of-the-safety-program)
- [Replacing Software and Hardware Components](#replacing-software-and-hardware-components)
- [Guide to diagnostics (S7-300, S7-400)](#guide-to-diagnostics-s7-300-s7-400)
- [Guide to diagnostics (S7-1500)](#guide-to-diagnostics-s7-1500)
- [Guide to diagnostics (S7-1200)](#guide-to-diagnostics-s7-1200)

### Notes on startup of the F-system

In "STARTUP" mode of an F-CPU, the startup of the standard user program occurs as usual.

In the safety program, all DB contents of the F-DBs are generally reset to their start values from the load memory.

An [automatic reintegration of the F-I/O](#passivation-and-reintegration-of-f-io) takes place starting from the 2nd cycle of the F-runtime group.

> **Note**
>
> Resetting the F-DBs to start values from the load memory also triggers the following:
>
> - Any stored error information is reset.
> - Edge memory bits in instructions or F-FBs with edge evaluations (e.g. TON instruction) are reset, so that for a signal that already has the "TRUE" state in the 1st cycle of an F-runtime group, a positive signal edge is detected immediately at a query for positive signal edge.

### Notes on Safety Mode of the Safety Program

#### Introduction

Pay attention to the following important notes on safety mode of the safety program.

#### Use of simulation devices/simulation programs

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Use of simulation devices/simulation programs in plants**  If you operate simulation devices or simulation programs that generate safety message frames, for example, based on PROFIsafe, and make them available to the SIMATIC Safety F-system via the bus system (such as PROFIBUS DP or PROFINET IO), you must ensure the safety of the plant through [organizational measures](#glossary).  Note, for example, that a protocol analyzer is not permitted to perform any function that reproduces recorded message frame sequences with correct time behavior.  - **S7-PLCSIM version < 15.1 or S7-PLCSIM Advanced version < 2.0 SP1 and Safety System version < V2.2**    If you use [S7-PLCSIM](#overview-of-testing-the-safety-program) to simulate safety programs, the measures mentioned above are not necessary because S7-PLCSIM cannot establish an online connection to a real component. - **S7-PLCSIM version ≥ 15.1 or S7-PLCSIM Advanced version ≥ 2.0 SP1 or Safety System version ≥ V2.2**    You must ensure the safety of the plant through organizational measures.   In addition, the loading of the safety-related project data with Safety System version V2.2 and higher onto an S7-PLCSIM is only permissible as of S7-PLCSIM V15.1 or S7-PLCSIM Advanced V2.0 SP1 and higher.    (S030) |  |

> **Note**
>
> For an S7-PLCSIM before V15.1 or S7-PLCSIM Advanced before V2.0 SP1 and a Safety system version V2.2 and higher, the safety program changes to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

#### Switching F‑CPU to STOP mode

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unintentional restart**  In contrast to the standard user program, when the safety program starts up, all tags of the F-DBs are generally initialized with their start values. This means that saved error information is lost. The F-system performs automatic reintegration of the F‑I/O.  If an unintentional startup of your process is not allowed, you must program restart/startup protection in the safety program. For this, the output of process values must be blocked until user acknowledgment takes place (see "[Implementation of user acknowledgment](#implementation-of-user-acknowledgment)"). This user acknowledgment must not take place until safe output of process values is possible (see "[Programming startup protection](#programming-startup-protection)").  You must expect an unintentional restart in the following cases:  - After a STOP generated by PG/PC operation, mode switch, communication function or "STP" instruction - After an operating error - After a STOP caused by a fault reaction function    (S008) |  |

#### CRC error in F-I/O or safety-related communication

> **Note**
>
> **CRC error in F-I/O or safety-related communication**
>
> If you observe that an F-CPU requests manual acknowledgement of a CRC error more than once within the space of 100 hours, and this occurs repeatedly, check whether the network technology installation guidelines have been followed.
>
> CRC errors are present:
>
> - For F-I/O access, the ACK_REQ tag of the F-I/O DB is set and the DIAG tag of the F-I/O DB indicates CRC errors with bit 2 or bit 6.
> - For safety-related communication with the SENDDP/RCVDP instructions, the ACK_REQ output of the RCVDP instruction is set and the DIAG output of the SENDDP/RCVDP instruction indicates CRC errors with bit 6.
> - For safety-related communication with the SENDS7/RCVS7 instructions, the ACK_REQ output of the RCVS7 instruction is set and the DIAG output of the SENDS7/RCVS7 instruction indicates CRC errors with bit 6.
> - For communication with Flexible F-Link, the ACK_REQ tag of the F-communication DB is set for receiving and the DIAG tag of the F-communication DB for sending/receiving indicates CRC errors with bit 6.
>
>   or
> - A CRC error is entered in the diagnostic buffer of the F-CPU.
>
> In this case, the [failure probability values](https://support.industry.siemens.com/cs/ww/en/view/109481784) (PFD<sub>avg</sub>/PFH) for safety-related communication no longer apply.
>
> Information on installation guidelines for PROFINET and PROFIBUS can be found in:
>
> - [PROFIBUS Installation Guidelines](http://www.profibus.com/PBInstallationGuide)
> - [PROFIBUS Interconnection Technology](http://www.profibus.com/nc/downloads/downloads/profibus-interconnection-technology/display/)
> - [PROFINET Installation Guidelines](http://www.profibus.com/PNInstallationGuide)
> - [PROFINET Cabling and Interconnection Technology](http://www.profibus.com/nc/downloads/downloads/profinet-cabling-and-interconnection-technology/display/)
> - [PROFIsafe Environment Requirements](http://www.profibus.com/PROFIsafeRequirements)
>
> When your review indicates that the configuration guidelines for PROFIBUS and PROFINET have been met, contact Customer Support.

### Replacing Software and Hardware Components

#### Introduction

Proceed as in the standard. Also note the following sections.

#### Replacement of software components

When replacing software components on your programming device or PC, e.g. with a new version of STEP 7, you must adhere to the information regarding upward and downward compatibility in the documentation and readme files for these products (e.g. STEP 7 Safety).

When replacing STEP 7 Safety, check whether the version of STEP 7 Safety is listed in Annex 1 of the Report for the TÜV certificate.

#### Replacement of hardware components

Hardware components for SIMATIC Safety (F‑CPU, F‑I/O, batteries, etc.) are replaced in the same way as in Standard automation systems.

If you replace an F-I/O with an F-I/O with a newer article number, which thus occupies more I/O addresses, the now larger I/O address range may already be occupied by another F-I/O.

For example, if you replace an F module F-DI 8x24VDC HF with part number 6ES7136-6BA00-0CA0 by an F module with 6ES7136-6BA01-0CA0. The end address of the input and output addresses is increased by 1 byte each by the exchange. In this case, STEP 7 assigns a new free I/O address range to the F module. The corresponding tag in the tag table must then be manually adapted to the new I/O addresses.

#### Replacement of an HF-CPU in the redundant S7-1500 HF system

Note the following warning when replacing an HF-CPU of a redundant S7-1500HF system:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you replace an F-CPU of a redundant S7-1500HF system (e.g. due to CPU failure, defect, etc.), you must put into operation the replacement F-CPU with the SIMATIC Memory Card of the previous F-CPU or with an empty SIMATIC Memory Card. This ensures that after successful SYNCUP of the replacement F-CPU, only the previous safety program is executed. (S094) |  |

#### Replacement of S7-1500 F Software Controllers

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **The following applies as of firmware version V30.0 of the S7-1500 F Software Controller:**   After a CPU module replacement (for example, new PC with data storage medium from old PC), a data storage medium replacement (for example, data storage medium with safety-related project data 1 is replaced by data storage medium with safety-related project data 2) or a UEFI update (if no NVRAM is present), you must ensure that the correct safety program is located in the S7-1500 F Software Controller by reading out the Collective F-signature with the command line command "GetCollectiveFSignature" or the display.  Then you must enter and confirm the expected Collective F-signature with the command line command "ConfirmCollectiveFSignature". This confirmation is required to restart the safety program.  For both command line commands, you must be a member of the "Software Controller Operators" (Windows) or "software_controller_operators" (Linux) user group and the "Failsafe Operators" (Windows) or "failsafe_operators" (Linux) user group.   **The following applies to firmware versions < V30.0 of the S7-1500 F Software Controller:**   After a CPU module replacement (e.g. new PC with data storage medium from old PC), a data storage medium replacement (e.g. data storage medium containing safety program 1 is replaced with data storage medium containing safety program 2) or a UEFI update, you must check via the display whether the correct collective F-signature is displayed or perform a program identification. (S066) |  |

#### Removing and inserting F-I/O during operation

If removing and inserting is possible for standard I/O during operation, it is also possible for the respective F‑I/O. However, be aware that replacing an F-I/O module during operation can cause a communication error in the F-CPU.

You must acknowledge the communication error in your safety program in the ACK_REI tag of the [F-I/O DB](#f-io-db) or, alternatively, by using the "[ACK_GL](STEP%207%20Safety%20V19%20instructions.md#ack_gl-global-acknowledgment-of-all-f-io-in-an-f-runtime-group-step-7-safety-v19)" instruction. Without an acknowledgment, the F-I/O will remain passivated.

#### CPU firmware update

Check of the CPU operating system for F-approval: When using a new CPU operating system (firmware update), you must check to see if the CPU operating system you are using is approved for use in an F-system.

The minimum CPU operating system versions with guaranteed F-capability are specified in the appendix of the Certificate. This information and any notes on the new CPU operating system must be taken into account.

#### Firmware update for interface module

When using a new operating system for an interface module, such as IM 151‑1 HIGH FEATURE for ET 200S (firmware update), you must observe the following:

If you have selected the "Activate firmware after update" option for the firmware update (see Help onSTEP 7, "Online & Diagnostics"), the interface module is automatically reset following a successful download operation and then runs on the new operating system. Note that the firmware update for interface modules during operation causes a communication error in the F‑CPU.

You must acknowledge the communication error in your safety program in the ACK_REI tag of the [F-I/O DB](#f-io-db) or, alternatively, by using the "[ACK_GL](STEP%207%20Safety%20V19%20instructions.md#ack_gl-global-acknowledgment-of-all-f-io-in-an-f-runtime-group-step-7-safety-v19)" instruction. Without an acknowledgment, the F-I/O will remain passivated.

#### Preventive maintenance (proof test)

Proof test for complex electronic components generally means replacement with new, unused components.

#### PFD<sub>avg</sub> and PFH values for S7-300/400 F-CPUs and F-I/O

You will find a list of the failure probability values (PFD<sub>avg</sub>, PFH values) for components that can be used in SIMATIC Safety on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109481784).

#### PFD<sub>avg</sub> and PFH values for S7-1200/1500 F-CPUs

Below are the probability of failure values (PFD<sub>avg</sub>, PFH values) for S7-1200/1500 F-CPUs with a service life of 20 years and an mission time of 100 hours:

| Low demand mode   **low demand mode**   According to IEC 61508:2010:  PFD<sub>avg</sub> = Average probability of dangerous failure on demand | High demand or continuous mode   **high demand/continuous mode**   According to IEC 61508:2010:  PFH = Average frequency of a dangerous failure [h<sup>-1</sup>] |
| --- | --- |
| < 2E-05 | < 1E-09 up to an operating altitude of 3 000 m or  < 2E-09 at an operating altitude greater than 3 000 m up to 5 000 m |

You can find more information on the operating conditions of the F-CPUs in the [PI F-CPUs](https://support.industry.siemens.com/cs/ww/en/view/109478599), and in the [PI of the PFD<sub>avg</sub>, PFH values](https://support.industry.siemens.com/cs/ww/en/view/109481784).

#### PFD<sub>avg</sub> and PFH values for safety-related communication

Below you will find the failure probability values (PFD<sub>avg</sub>, PFH values) for safety-related communication:

| Low demand mode   **low demand mode**   According to IEC 61508:2010:  PFD<sub>avg</sub> = Average probability of dangerous failure on demand | High demand or continuous mode   **high demand/continuous mode**   According to IEC 61508:2010:  PFH = Average frequency of a dangerous failure [h<sup>-1</sup>] |
| --- | --- |
| < 1E-05* | < 1E-09***** |

*** Note on S7-300/400 F-CPUs:**
  
The PFH value is valid under the assumption that a maximum of 100 F-I/Os are involved in a safety function. If you use more than 100 F-I/Os, you have to also add 4E-12 per F-I/O for the safety function.  
The PFD<sub>avg</sub> value is valid for a mission time of 20 years and under the assumption, that a maximum of 25 F-I/Os are involved in a safety function. If more than 25 F-I/Os are used, you need to add 3.5E-7 per F-I/O for this safety function.

### Guide to diagnostics (S7-300, S7-400)

#### Introduction

Here you find a compilation of diagnostic capabilities that can be evaluated for your system when an error occurs. Most of the diagnostic capabilities are the same as those in standard automation systems. The sequence of steps represents a recommendation.

#### Steps for evaluating diagnostic capabilities

The following table shows the steps you take to evaluate diagnostic capabilities.

| Step | Procedure | Reference |
| --- | --- | --- |
| 1 | **Evaluate LEDs on the hardware (F‑CPU, F‑I/O):**   - BUSF LED on the F-CPU: Flashes when a communication error occurs on PROFIBUS DP/PROFINET IO;   On if a programming error occurs when OB 85 and OB 121 are programmed (e.g. instance DB is not loaded) - STOP LED on the F-CPU: illuminates when the F-CPU is in STOP mode - Fault LEDs on the F-I/O: e.g. SF‑LED (group error LED) on if any fault occurs in the individual F‑I/O | Manuals for F‑CPU and F‑I/O |
| 2 | **Evaluate diagnostic buffer of the modules:**   You read the diagnostic buffer of a module (F-CPU, F-I/O, CP) in its online and diagnostic view in the "Diagnostic buffer" group under the "Online & Diagnostics" folder. | Help on STEP 7 and manuals for the F-CPU and F-I/O |
| 3 | **Evaluate stacks of the F‑CPU:**   when the F-CPU is in STOP mode, read the following successively:  - Block stack: Check whether STOP mode of the F‑CPU was triggered by an F‑block of the safety program - Interruption stack - Local data stack | Help on STEP 7 |
| 4 | **Evaluate diagnostic tag of the F‑I/O DB using testing and commissioning functions, by means of an operator control and monitoring system, or in the standard user program:**   Evaluate the DIAG tag in the F‑I/O DB | [F-I/O access](#addressing-f-io) |
| 5 | **Evaluate diagnostic outputs of the instance DBs of instructions using testing and commissioning functions, using an operator control and monitoring system, or in the standard user program:**   - Evaluate the following for MUTING, EV1oo2DI, TWO_H_EN, MUT_P, ESTOP1, FDBACK, SFDOOR in the assigned instance DB:   - Output DIAG - Evaluate the following for SENDDP or RCVDP in the assigned instance DB:   - Output RET_DPRD/RET_DPWR   - Output DIAG - Evaluate the following for SENDS7 or RCVS7 in the assigned instance DB:   - Output STAT_RCV   - Output STAT_SND   - Output DIAG | Instructions |

#### Tip on RET_DPRD/RET_DPWR

The diagnostic information of the RET_DPRD/RET_DPWR outputs of the SENDDP or RCVDP instructions corresponds to the diagnostic information of the RETVAL return value of the "DPRD_DAT" and "DPWR_DAT" instructions. You can find the description in the help on  STEP 7 for the "DPRD_DAT" and "DPWR_DAT" instructions.

#### Tip: STAT_RCV and STAT_SND

The diagnostic information of the STAT_RCV output of the SENDS7 or RCVS7 instructions corresponds to the diagnostic information of the STATUS output of the "URCV" instruction. The diagnostic information of the STAT_SND output of the SENDS7 or RCVS7 instructions corresponds to the diagnostic information of the STATUS output of the "USEND" instruction. You can find the description in the help on  STEP 7 for the instruction "UCRV" or "USEND" .

### Guide to diagnostics (S7-1500)

Detailed information on diagnostics for an S7-1500 F-CPU can be found in the [Diagnostics](http://support.automation.siemens.com/WW/view/en/59192926) function manual.

### Guide to diagnostics (S7-1200)

Detailed information on diagnostics for an S7-1200 F-CPU can be found in the [S7-1200 Functional Safety manual](http://support.automation.siemens.com/WW/view/en/104547552).

## Monitoring and response times

This section contains information on the following topics:

- [Introduction](#introduction-4)
- [Configuring monitoring times](#configuring-monitoring-times)
- [Response Times of Safety Functions](#response-times-of-safety-functions)

### Introduction

#### Introduction

In the following, you will learn:

- Which F-specific monitoring times you must configure
- Which rules must be followed when specifying monitoring times
- Where you enter the F-specific monitoring times
- Which rules must be followed with regard to the maximum response time of a safety function

#### Support for calculations

An Excel file is available on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109783831) to support you in the approximative calculation of the runtimes of the F-runtime groups, the F-specific minimum monitoring times and the maximum response times for your F-system.

#### Additional information

The monitoring and response times for the standard part are calculated in SIMATIC Safety in exactly the same way as for standard S7‑300, S7‑400, S7-1200 and S7‑1500 automation systems and are not addressed here. For a description of this calculation, refer to the hardware manuals for the CPUs. For redundant S7-1500HF systems, also observe the system manual "[Redundant System S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/109754833)".

### Configuring monitoring times

This section contains information on the following topics:

- [Configuring the monitoring times](#configuring-the-monitoring-times)
- [Minimum monitoring time for the F-runtime group cycle time](#minimum-monitoring-time-for-the-f-runtime-group-cycle-time)
- [Minimum monitoring time for safety-related communication between F-CPU and F-I/O](#minimum-monitoring-time-for-safety-related-communication-between-f-cpu-and-f-io)
- [Minimum monitoring time of safety-related CPU-CPU communication](#minimum-monitoring-time-of-safety-related-cpu-cpu-communication)
- [Monitoring Time for Safety-Related Communication between F-Runtime Groups](#monitoring-time-for-safety-related-communication-between-f-runtime-groups)

#### Configuring the monitoring times

##### Monitoring times to be configured

You must configure the following monitoring times:

| Monitoring... | Setting... | Parameters | See |
| --- | --- | --- | --- |
| F-cycle time or cycle time warning limit of the F-runtime groups that contain the safety program | in Safety Administration Editor:  - Dialog for definition of an F-runtime group | Maximum cycle time of the F-runtime group | - [Procedure for defining an F‑runtime group (S7-300, S7-400)](#procedure-for-defining-an-f-runtime-group-s7-300-s7-400) - [Procedure for defining an F‑runtime group (S7-1200, S7-1500)](#procedure-for-defining-an-f-runtime-group-s7-1200-s7-1500) |
| of the safety-related communication between F-CPU and F-I/O via PROFIsafe (PROFIsafe monitoring time) | In the hardware and network editor:  - Centrally when configuring the F-CPU; properties of the F-CPU; or - when configuring the F-I/O; properties of the F-I/O | F-monitoring time  F_WD_TIME | - [Configuring an F-CPU](#configuring-an-f-cpu) - [Configuring F-I/O](#configuring-f-io) - [Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices](#peculiarities-when-configuring-fail-safe-gsd-based-dp-slaves-and-fail-safe-gsd-based-io-devices) |
| of the safety-related CPU-CPU communication | At the TIMEOUT input of the instructions:  - SENDDP; RCVDP; SENDS7; RCVS7 | TIMEOUT | - [Communication](STEP%207%20Safety%20V19%20instructions.md#communication) |
| (S7-1200, S7-1500) Communication with Flexible F-Link | in Safety Administration Editor:  - "Flexible F-Link" area | F-monitoring time of F-communication | - ["Flexible F-Link" area (S7-1200, S7-1500)](#flexible-f-link-area-s7-1200-s7-1500) - [F-runtime group communication (S7-1200, S7-1500)](#f-runtime-group-communication-s7-1200-s7-1500) - [Configuring and programming communication with Flexible F-Link (S7-1200, S7-1500)](#configuring-and-programming-communication-with-flexible-f-link-s7-1200-s7-1500) |

(S7-300, S7-400) You do not have to configure the monitoring time for safety-related communication between F‑runtime groups.

##### Rules for configuring monitoring times

When configuring monitoring times, you must take into account the availability as well as the safety of the F-system as follows:

- Availability: Sufficiently large monitoring times must be selected so that time monitoring is not exceeded in an error-free scenario.
- Safety: Sufficiently small monitoring times must be selected so that the process safety time of the process is not exceeded.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| It can only be ensured (from a fail-safe standpoint) that a signal state to be transferred will be acquired and transferred to the receiver if the signal level is pending for at least as long as the assigned monitoring time. (S018) |  |

##### General procedure for configuring monitoring times

Use the following procedure for configuring monitoring times:

1. Configure the standard system.

   Refer to the applicable hardware manuals and Help on STEP 7 for the necessary information.
2. Configure the specific monitoring times of the F-System with respect to availability. You use the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) to calculate the approximate minimum monitoring time.
3. Use the Excel file for response time calculation to calculate the maximum response time and then verify that the process safety time of the process is not exceeded. If necessary, you must reduce the specific monitoring times of the F-System.

**Note**

To avoid a triggering of the time monitoring in the special operating and system states of the redundant S7-1500HF system in case of error-free operation, higher minimum monitoring times are required for a redundant S7-1500HF system with regard to availability. This is taken into account accordingly in the Excel file for the response time calculation.

---

**See also**

[Redundant System S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/109754833)

#### Minimum monitoring time for the F-runtime group cycle time

##### Parameter "Maximum cycle time of the F-runtime group"

You configure the monitoring time for the F-runtime group cycle time in the Safety Administration Editor in the work area for [definition of the F-runtime group](#defining-f-runtime-groups).

To prevent F-runtime group cycle time monitoring from being triggered when there are no pending faults and causing the F‑CPU to go to STOP, you must set the maximum cycle time of the F‑runtime group high enough.

Use the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) to determine the minimum monitoring time for the F-runtime group cycle time. Note also the comments in the Excel file.

For S7-1200/1500 F-CPUs, you can also use the tags [TCYC_CURR](#f-runtime-group-information-db-s7-1200-s7-1500) and [TCYC_LONG](#f-runtime-group-information-db-s7-1200-s7-1500) to determine the current and longest cycle time of the F-runtime group that occurred since the last STOP-RUN transition for dimensioning.

#### Minimum monitoring time for safety-related communication between F-CPU and F-I/O

##### Parameter "F-monitoring time"

You have two options for configuring the monitoring time of safety-related communication between the F-CPU and F-I/O:

- Centrally in the hardware and network editor during [parameter assignment of the F-CPU](#configuring-an-f-cpu); in the properties of the F-CPU, or
- During [parameter assignment of the F-I/O](#configuring-f-io) in the hardware and network editor; in the properties of the F-I/O

> **Note**
>
> Note that in a redundant S7-1500HF system and use of an IO device that does not support system redundancy S2, there is an interruption of PROFINET communication with this device when the primary CPU fails and thus a communication error in the F-I/Os of this IO device, which requires reintegration of the F-I/Os (see section "[After communication errors](#after-communication-errors)").
>
> For IO devices with system redundancy S2, the redundant S7-1500HF system switches to the backup CPU without interruption if the primary CPU fails. During the primary backup switchover, the fail-safe outputs remain active.

##### "F-monitoring time" = PROFIsafe monitoring time T<sub>PSTO</sub>

The specified PROFIsafe monitoring time T<sub>PSTO</sub> must be high enough to prevent tripping the F-cycle time monitoring when no faults are present.

Use the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) available for SIMATIC Safety to calculate the minimum monitoring time for safety-related communication between the F‑CPU and F‑I/O.

Note also the comments in the Excel file.

##### Check to determine whether configured PROFIsafe monitoring time is too short

> **Note**
>
> During commissioning of the F-system, you can perform a check while safety mode is active to determine whether the configured PROFIsafe monitoring time is too short.
>
> This check of the PROFIsafe monitoring time is useful if you want to ensure that the configured monitoring time exceeds the minimum monitoring time by a sufficient amount. In this way, you can avoid the possible occurrence of sporadic monitoring time errors.
>
> **Procedure:**
>
> 1. Insert an F-I/O (one that will not be needed later for system operation).
> 2. Assign a shorter monitoring time for this F-I/O than for the F-I/O of the system.
> 3. If the additional F-I/O fails and the "Monitoring time for safety message frame exceeded" diagnostic is signaled, you have fallen below the minimum possible PROFIsafe monitoring time.
> 4. Increase the monitoring time for the added F‑I/O just to the point where it no longer fails. This monitoring time corresponds approximately to the minimum possible monitoring time.
>
> **Conditions:**
>
> The F-I/O to be inserted additionally and the F-I/O whose PROFIsafe monitoring time is to be checked must have the following properties in common:
>
> - They must be inserted in the same rack
> - They must be nodes in the same subnet
>
> **Tip:**
>
> It may be useful to leave the additional F-I/O in place for systems that will be modified or expanded during operation after commissioning. This F‑I/O will then provide an early warning in the event of changes in the time behavior, enabling you to avoid a process shutdown triggered by the F‑I/O in the process.
>
> In a redundant S7-1500HF system, the check as to whether the configured PROFIsafe monitoring time is too short should be carried out in all operating and system states, because the response times there also depend on the respective operating and system state.

#### Minimum monitoring time of safety-related CPU-CPU communication

##### Input TIMEOUT at SENDDP and RCVDP or SENDS7 and RCVS7/F-monitoring time for communication via Flexible F-Link

The time monitoring is performed in the [SENDDP and RCVDP](STEP%207%20Safety%20V19%20instructions.md#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19) or [SENDS7 and RCVS7](STEP%207%20Safety%20V19%20instructions.md#sends7-and-rcvs7-communication-via-s7-connections-step-7-safety-advanced-v19-s7-300-s7-400) instructions of the communication partner. You must assign the time monitoring with identical monitoring time for both instructions at the TIMEOUT input.

You must specify a monitoring time TIMEOUT that is large enough so that monitoring is not initiated when no faults are present.

For communication via Flexible F-Link, you specify the F-monitoring time for the safety-related communication when [creating safety-related communication](#flexible-f-link-area-s7-1200-s7-1500).

Use the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) that is available for SIMATIC Safety to determine the minimum value for TIMEOUT or the F-monitoring time.

Note also the comments in the Excel file.

#### Monitoring Time for Safety-Related Communication between F-Runtime Groups

##### Monitoring time for safety-related communication between F-runtime groups (S7-300, S7-400)

The monitoring time for safety-related communication between F-runtime groups with Flexible F-Link is determined automatically from the values of the "Maximum cycle time of F-runtime group" (work area for [Definition of the F-runtime group](#defining-f-runtime-groups) in the Safety Administration Editor).

Monitoring time = (maximum cycle time of the 1st F-runtime group) + (maximum cycle time of the 2nd F-runtime group)

##### Monitoring time for safety-related communication between F-runtime groups (S7-1200, S7-1500)

You can calculate the monitoring time for safety-related communication between F-runtime groups from the values for the "Maximum cycle time of the F-runtime group" (area for [Definition of the F-runtime group](#defining-f-runtime-groups) in the Safety Administration Editor), if you place the default user program for the F-runtime group communication into [pre-/postprocessing](#pre-postprocessing-s7-1200-s7-1500).

Monitoring time = (Maximum cycle time of the 1st F-runtime group) + (Maximum cycle time of the 2nd F-runtime group).

### Response Times of Safety Functions

#### Definition of response time

The response time is the time from detection of an input signal until the linked output signal changes.

#### Fluctuation range

The actual response time lies between a minimum response time and maximum response time. You must always take the maximum response time into account in your system configuration.

Also note the comments in the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831).

> **Note**
>
> In a redundant S7-1500HF system, the current operating and system state influences the actual response time.

#### Rules for maximum response time of a safety function

The maximum response time of a safety function must be shorter than the process safety time of the process.

#### Definition for process safety time of a process

The process safety time of a process is the time interval between the occurrence of an error, within which the process can be left on its own without causing injury to operating personnel or damage to the environment, and the point in time the response is completed.

The controlling F-system can perform any control during the process safety time, this includes incorrectly or not at all. The process safety time of a process depends on the process type and must be determined on a case-by-case basis.

#### Procedure for response time calculation

The [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) is available for calculating the maximum response time of a safety function.

Use the Excel file to calculate the approximate maximum response time of the safety function and then check that the process safety time of the process is not exceeded.

If necessary, you must reduce the specific monitoring times of the F-system (see [Minimum monitoring time for safety-related communication between F-CPU and F-I/O](#minimum-monitoring-time-for-safety-related-communication-between-f-cpu-and-f-io)).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| You may only use the Excel file for response time calculation or for timeout calculation when using Flexible F-Link communication, if you have observed the following rules with regard to the standard instructions for consistent transfer of data:   [**CPU-CPU communication**](#flexible-f-link)   You must call the standard instruction for consistent sending of data and acknowledgment in the [post-processing of the F-runtime group](#pre-postprocessing-s7-1200-s7-1500). With the standard instructions for receiving data and acknowledgments consistently, you must differentiate whether or not the standard communication connection is deterministic. For deterministic connections (such as DPRD_DAT / DPWR_DAT), you need to call the standard instruction in the [pre-processing of the F-runtime group](#pre-postprocessing-s7-1200-s7-1500). If the connection is non-deterministic (e.g. S7 connection, TCP connections), you must call the standard instruction in a cyclic interrupt OB. This cyclic interrupt OB must be called at shorter intervals than the F-runtime group. A ratio of 1:5 is recommended for this.   [**F-runtime group communication**](#f-runtime-group-communication-s7-1200-s7-1500)   You have to call up the standard instruction UMOVE_BLK for transferring the data to be sent in the postprocessing of the sending F-runtime group. You have to call the standard instruction UMOVE_BLK for transferring the acknowledgment to be sent in the postprocessing of the receiving F-runtime group. (S089) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The response time of your safety function depends, among other things, on the cycle time of the F-OB, the runtime of the F-runtime group and, when distributed F-I/O is used, the parameter assignment of PROFINET/PROFIBUS.   Therefore, the configuration/parameter assignment of the standard system influences the response time of your safety function.  Examples:   - Increasing the priority of a standard OB compared to an F-OB can extend the cycle time of the F-OB or the runtime of the F-runtime group due to the higher-priority processing of the standard OB. Note that during the creation of technology objects, OBs with very high priority may be created automatically. - The change of the send clock cycle of PROFINET changes the cycle time of an F-OB with event class "Synchronous cycle".   Note that the configuration / parameter assignment of the standard system is not subject to access protection for the safety-related project data and does not lead to a modification of the Collective F-Signature.  If you do not take organizational measures to prevent changes in the configuration / parameter assignment of the standard system with influence on the response time, you must always use the monitoring times for the calculation of the maximum response time of a safety function (see [Configuring monitoring times](#configuring-monitoring-times)).   The monitoring times are protected against change with the access protection of the safety-related project data and are captured by the Collective F-Signature as well as the Collective F-SW-Signature.   When calculating with the [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831) you need to consider the value that is specified for "Any standard system runtimes" as value for the maximum response time. (S085) |  |

## Checklist

This section contains information on the following topics:

- [Checklist](#checklist-1)

### Checklist

#### Life cycle of fail-safe automation systems

The following table contains a checklist summarizing all activities in the life cycle of a fail-safe SIMATIC Safety system, including requirements and rules that must be observed for each activity.

#### Checklist

Legend:

- Stand-alone section references refer to this documentation.
- "F-SMs Manual" refers to the [Automation System S7-300, ET 200M Distributed I/O System, Fail-Safe Signal Modules](http://support.automation.siemens.com/WW/view/en/19026151) manual.
- "F-Modules Manual" refers to the [ET 200S Distributed I/O System, Fail-Safe Modules](http://support.automation.siemens.com/WW/view/en/27235629) manual.
- "ET 200eco Manual" refers to the [ET 200eco Distributed I/O Station, Fail-Safe I/O Module](http://support.automation.siemens.com/WW/view/en/19033850) manual.
- "ET 200eco PN Manual" refers to the [ET 200eco PN F-DI 8 x 24 VDC, 4xM12 / F-DQ 3 x 24 VDC/2.0A PM, 3xM12](https://support.industry.siemens.com/cs/ww/en/view/109765611) manual.
- "ET 200pro Manual" refers to the [ET 200pro Distributed I/O System, Fail-Safe I/O Module](http://support.automation.siemens.com/WW/view/en/22098524) manual.
- "ET 200iSP Manual" refers to the [ET 200iSP Distributed I/O Device, Fail-Safe Modules](http://support.automation.siemens.com/WW/view/en/47357221) manual.
- "ET 200SP Manual" refers to the [ET 200SP System](http://support.automation.siemens.com/WW/view/en/58649293) manual
- "ET 200AL Manual" refers to the [ET 200AL System Manual](https://support.industry.siemens.com/cs/ww/en/view/89254965)
- "ET 200MP Manual" refers to the [S7-1500/ET 200MP Distributed I/O System](http://support.automation.siemens.com/WW/view/en/59191792) manual
- "S7-1500R/H Manual" refers to the [S7-1500R/H System Manual](https://support.industry.siemens.com/cs/ww/en/view/109754833)
- "HB SIMATIC Drive Controller" refers to the [SIMATIC Drive Controller System Manual](https://support.industry.siemens.com/cs/ww/en/view/109766665) manual
- "ET 200SP Modules Manual" refers to the equipment manuals for [F-Modules of the ET 200SP Distributed I/O System](https://support.industry.siemens.com/cs/ww/en/ps/14059/man)
- "ET 200SP Modules Manual" refers to the equipment manuals for [F-Modules of the ET 200MP Distributed I/O System](https://support.industry.siemens.com/cs/ww/en/ps/14141/man)
- "ET 200AL Module Manual" refers to the equipment manual [F-Modules of the ET 200AL Distributed I/O System](https://support.industry.siemens.com/cs/ww/en/view/109798489)

| Phase | Note the following | Reference | Check |
| --- | --- | --- | --- |
| **Planning** |  |  |  |
| Requirement: "Safety requirements specification" available for the intended application | Process-dependent | — |  |
| Specification of system architecture | Process-dependent | — |  |
| Assignment of functions and subfunctions to system components | Process-dependent | under [Product Overview](#product-overview) |  |
| Selection of sensors and actuators | Requirements for actuators | F-SMs Manual, section 6.5;   F-Modules Manual, section 4.5;   ET 200eco Manual, section 5.5   ET 200eco PN Manual, section 5.2;   ET 200pro Manual, section 4.4   ET 200iSP Manual, section 4.5   ET 200SP Manual, section 6.2.2   ET 200MP Manual, section 6.2.2 |  |
| Specification of required safety properties for individual components | IEC 61508:2010 | — |  |
| **Configuration** |  |  |  |
| Installing license | Requirement for installation | under [Installing/uninstalling the STEP 7 Safety Basic V19 license](#installinguninstalling-the-step-7-safety-basic-v19-license) or[Installing/uninstalling the STEP 7 Safety Advanced V19 license](#installinguninstalling-the-step-7-safety-advanced-v19-license) |  |
| Selection of S7 components | Descriptions of configuration | under [Product Overview](#product-overview);   F-SMs Manual, section 3;   F-Modules Manual, section 3;   ET 200eco Manual, section 3   ET 200eco PN Manual, section 4;   ET 200pro Manual, section 2   ET 200iSP Manual, section 3   ET 200SP Manual, section 4   ET 200AL Manual, section 3   ET 200MP Manual, section 4   S7-1500R/H Manual, section 4   HB SIMATIC Drive Controller, section 4 |  |
| Configuration of hardware | - Description of F-systems - Verification of utilized hardware components based on Annex 1 of Report in the Certificate | under [Configuring](#configuring);  Annex 1 of Report on the Certificate |  |
| Configuration of F-CPU | - Protection level, "Write protection for F-blocks" (S7-300, S7-400) - Protection level, at least "Full access" (S7-1200, S7-1500) - Password - F-capability enabled - Definition/setting of F-specific parameters - Cycle time for the F-runtime group in which the safety program is to be executed, defined in accordance with the requirements and safety regulations - same as with standard system | under [Configuring an F-CPU](#configuring-an-f-cpu);   Standard‑S7‑300 Manual;    Standard‑S7‑400 Manual;    Standard-S7-1200 Manual;    Standard-S7-1500 Manual;   under [Monitoring and response times](#monitoring-and-response-times) |  |
| Configuration of F-I/O | - Settings for safety mode - Setting of passivation type - Configuring monitoring times - Defining sensor evaluation - Defining diagnostic behavior - Special F-parameters - Assigning names - Unique PROFIsafe address | under [Configuring F-I/O](#configuring-f-io) or[Peculiarities when configuring fail-safe GSD based DP slaves and fail-safe GSD based I/O devices](#peculiarities-when-configuring-fail-safe-gsd-based-dp-slaves-and-fail-safe-gsd-based-io-devices)  under [Monitoring and response times](#monitoring-and-response-times);   F-SMs Manual, sections 3, 9, 10;    F-Modules Manual, sections 2.4, 7;   ET 200eco Manual, sections 3, 8;   ET 200eco PN Manual, section 6;   ET 200pro Manual, Sections 2.4, 8;   ET 200iSP Manual, Sections 2.4, 7, 8   ET 200SP Modules Manual, section 4   ET 200MP Modules Manual, section 4   ET 200AL Module Manual, section 4 |  |
| **Programming** |  |  |  |
| Defining program design and structure | - Follow warnings and notes on programming | under [Overview of Programming](#overview-of-programming-1), [Program structure of the safety program (S7-300, S7-400)](#program-structure-of-the-safety-program-s7-300-s7-400), [Program structure of the safety program (S7-1200, S7-1500)](#program-structure-of-the-safety-program-s7-1200-s7-1500); [Programming startup protection](#programming-startup-protection); |  |
| Creating the F-runtime groups | - Assignment of F-FB or F-FC as main safety block to the calling block (S7-300, S7-400) or F-OB (S7-1200, S7-1500) - Setting maximum cycle time for the F-runtime group in accordance with requirements (dependent on process and safety regulations) - Creating DB for F-runtime group communication - (S7-300, S7-400) Call of main safety blocks directly in OBs (e.g. OB 35), FBs, or FCs - (S7-1200, S7-1500) Call of the main safety block from the F-OB | under [Defining F-Runtime Groups](#defining-f-runtime-groups)  under [Monitoring and response times](#monitoring-and-response-times) |  |
| Creating/inserting the F-blocks | - Generating, editing, and saving F-FBs, F-FCs, and F-DBs in accordance with the requirements of the program structure - Description:   - F-I/O access   - Passivation and reintegration of F-I/O   - Inserting F-blocks from global libraries   - Safety-related CPU-CPU communication   - Communication with the standard user program | under [Creating F-blocks in FBD / LAD](#creating-f-blocks-in-fbd-lad)  under [Addressing F-I/O](#addressing-f-io)  under [Implementation of user acknowledgment](#implementation-of-user-acknowledgment)  under [Reuse of F-blocks](#reuse-of-f-blocks)  under [Configuring and programming communication (S7-300, S7-400)](#configuring-and-programming-communication-s7-300-s7-400) and [Configuring and programming communication (S7-1200, S7-1500)](#configuring-and-programming-communication-s7-1200-s7-1500)  under [Data exchange between standard user program and safety program](#data-exchange-between-standard-user-program-and-safety-program) |  |
| Compiling the safety program | — | under [Compiling the safety program](#compiling-the-safety-program) |  |
| Implementing safety program call (S7-300, S7-400) | Check whether the main safety block is called directly in OBs (e.g., OB 35), FBs, or FCs. | under [Defining F-Runtime Groups](#defining-f-runtime-groups) |  |
| **Installation** |  |  |  |
| Hardware configuration | Description of  - Installation - Wiring | under [Overview of Configuration](#overview-of-configuration); [Particularities for configuring the F-System](#particularities-for-configuring-the-f-system);    F-SMs Manual, sections 5, 6;    F-Modules Manual, sections 3, 4;   ET 200eco Manual, sections 3, 4;   ET 200eco PN Manual, sections 4, 5;   ET 200pro Manual, Sections 2, 3;   ET 200iSP Manual, sections 3 and 4;   ET 200SP Manual, sections 5 and 6   ET 200AL Manual, sections 4, 5   ET 200MP Manual, sections 5 and 6   S7-1500R/H Manual, sections 5, 6   HB SIMATIC Drive Controller, section 5, 6 |  |
| **Commissioning, Testing** |  |  |  |
| Switching on | Description of commissioning – same as in standard | Standard‑S7‑300 Manual;    Standard‑S7‑400 Manual;    Standard-S7-1200 Manual;    Standard-S7-1500 Manual;    Standard-S7-1500 Software Controller Manual;    S7-1500R/H Module Manual    HB SIMATIC Drive Controller Manual |  |
| Downloading safety program and standard user program | Description  - Downloading - Program identification - Comparing safety programs | under [Downloading project data to an F-CPU](#downloading-project-data-to-an-f-cpu)  under [Comparing Safety Programs](#comparing-safety-programs) |  |
| Testing the safety program | - Description of disabling of safety mode - Procedures for changing safety program data | under [Downloading project data](#downloading-project-data); [Testing the safety program](#testing-the-safety-program-1); [Disabling safety mode](#disabling-safety-mode-1) |  |
| Changing the safety program | Description  - Disabling safety mode - Changing the safety program | under [Changing the safety program in RUN mode (S7-300, S7-400)](#changing-the-safety-program-in-run-mode-s7-300-s7-400), [Safety program in RUN mode (S7-1200, S7-1500)](#safety-program-in-run-mode-s7-1200-s7-1500), [Disabling safety mode](#disabling-safety-mode-1), [Deleting the safety program](#deleting-the-safety-program) |  |
| Testing the safety-related parameters | Description of configuration | under [Creating a safety summary](#creating-a-safety-summary);   F-SMs Manual, sections 4, 9, 10;   F-Modules Manual, sections 2.4, 7;   ET 200eco Manual, sections 3, 8;   ET 200eco Manual, section 6;   ET 200pro Manual, Sections 2.4, 8;   ET 200iSP Manual, Sections 2.4, 7, 8   ET 200SP Modules Manual, section 4   ET 200MP Modules Manual, section 4   ET 200AL Module Manual, section 4 |  |
| **System acceptance** |  |  |  |
| Acceptance | - Description and notes on acceptance - Printouts | under [System acceptance](#system-acceptance) |  |
| **Operation, maintenance** |  |  |  |
| General operation | Notes on operation | under [Notes on Safety Mode of the Safety Program](#notes-on-safety-mode-of-the-safety-program) |  |
| Access protection | — | under [Access protection](#access-protection) |  |
| Diagnostics | Responses to faults and events | under [Guide to diagnostics (S7-300, S7-400)](#guide-to-diagnostics-s7-300-s7-400); [Guide to diagnostics (S7-1200)](#guide-to-diagnostics-s7-1200); [Guide to diagnostics (S7-1500)](#guide-to-diagnostics-s7-1500); |  |
| Replacement of software and hardware components | Description   - Module replacement - Update of operating systems of F-CPU – same as in standard - Update of SW components   Notes   - Operating system update of IMs | under [Replacing Software and Hardware Components](#replacing-software-and-hardware-components); [Addressing F-I/O](#addressing-f-io);  Help on STEP 7 |  |
| Uninstalling the license,  Disassembly | - Notes for uninstalling the license - Notes for disassembling modules | under [Installing/uninstalling the STEP 7 Safety Basic V19 license](#installinguninstalling-the-step-7-safety-basic-v19-license); [Installing/uninstalling the STEP 7 Safety Advanced V19 license](#installinguninstalling-the-step-7-safety-advanced-v19-license); [Replacing Software and Hardware Components](#replacing-software-and-hardware-components); |  |

## Glossary

### Access protection

→ Fail-safe systems must be protected against dangerous, unauthorized access. Access protection for F‑systems is implemented by assigning a password for the → F‑CPU and a password or → project protection for the → safety program.

 

### Automatically generated F-blocks

→ F-blocks that are automatically generated and, if necessary, called when the → safety program is compiled, in order to generate an executable safety program from the safety program programmed by the user.

 

### Category

Category in accordance with ISO 13849-1:2015 or EN ISO 13849-1:2015

With SIMATIC Safety, use in → safety mode up to category 4 is possible.

 

### Channel fault

Channel-specific fault, such as a wire break or short circuit.

 

### Collective F-HW-Signature

The Collective F-HW-Signature uniquely identifies a particular state of safety-related hardware configuration. The Collective F-HW-Signature is important to document the change/non-change of the safety-related hardware configuration, for example in the context of an acceptance of changes.

 

### Collective F-Signature

The Collective F-Signature uniquely identifies a particular state of safety-related project data. It is important for the program identification as well as the on-site acceptance of the safety program, for example by → experts.

 

### Collective F-SW-Signature

The Collective F-SW-Signature uniquely identifies a particular state of the safety program. The Collective F-SW-Signature is important to document the change/non-change of the safety program, for example in the context of an acceptance of changes.

 

### CPU-wide

In the context of F-I/Os, "CPU-wide" means all F-I/Os assigned to an F-CPU: Central F-I/O of this F-CPU as well as F-I/Os for which the F-CPU is DP master/IO controller and assigned F-I/O in a shared device. An F-I/O that is addressed using I-slave-slave communication is assigned to the F-CPU of the I-slave and not to the F-CPU of the DP master / IO controller.

In the context of safety-related CPU-CPU communication, "CPU-wide" encompasses all the safety-related communication connections that are configured in an F-CPU.

With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one F-CPU.

 

### CRC

Cyclic Redundancy Check → CRC signature

 

### CRC signature

The validity of the process data in the → safety message frame, the correctness of the assigned address relationships, and the safety-related parameters are validated by means of a CRC signature contained in the safety message frame.

 

### DB for F-runtime group communication

-> F-DB for safety-related communication between F-runtime groups of a safety program.

 

### Depassivation

→ Reintegration

 

### Disabled safety mode

Temporary deactivation of → safety mode for test purposes, commissioning, etc.

A timer is started when the safety mode is disabled. After the timer has expired, the → F-CPU goes to STOP. The time for the timer is parameterizable.

The following actions are possible only in deactivated safety mode:

- Downloading changes of the → safety program to the -> F-CPU during operation (in RUN mode)
- Test functions such as "Modify" or other write access to data of the → safety program (with limitations)

Whenever safety mode is deactivated, the safety of the system must be ensured by other organizational measures, such as operation monitoring and manual safety shutdown.

 

### Discrepancy analysis

Discrepancy analysis for equivalence or non-equivalence is used for fail-safe inputs to detect errors caused by the time characteristic of two signals with the same functionality. The discrepancy analysis is initiated when different levels are detected in two associated input signals (when testing for non-equivalence: the same level). On expiration of an assignable period (→ discrepancy time), a check is made to determine whether the difference in levels (for non-equivalence testing, the same level) has disappeared after an assignable time period, the so-called discrepancy time. If not, there is a discrepancy error. The discrepancy analysis is performed between the two input signals of the 1oo2 evaluation of the sensors (→ sensor evaluation) in the fail-safe input.

 

### Discrepancy time

Assignable time for the → discrepancy analysis. If the discrepancy time is set too high, the fault detection time and → fault reaction time are prolonged unnecessarily. If the discrepancy time is set too low, availability is decreased unnecessarily because a discrepancy error is detected when, in reality, no error exists.

 

### DP/DP coupler

Device for coupling two PROFIBUS DP subnets required for master-master communication between → safety programs in different → F-CPUs in SIMATIC Safety and S7 Distributed Safety.

 

### Expert

The acceptance of a system, i.e., the safety-related acceptance test of the system, is usually carried out by an independent expert (for example, from TÜV).

 

### Fail-safe GSD based DP slaves

Fail-safe GSD based DP slaves are standard slaves that are operated on PROFIBUS with the DP protocol. They must operate in accordance with IEC 61784‑1:2010 (Fieldbus profiles) and the PROFIsafe bus profile. A GSD file is used for their configuration.

 

### Fail-safe GSD based I/O devices

Fail-safe GSD based I/O devices are standard devices that are operated on PROFINET with the I/O protocol. They must operate in accordance with IEC 61784‑1:2010 (Fieldbus profiles) and the PROFIsafe bus profile in V2‑MODE. A GSD file is used for their configuration.

 

### Fail-safe I/O modules

ET 200AL modules, ET 200eco modules and ET 200eco PN modules that can be used for safety-related operation (→ Safety mode). These modules are equipped with integrated → safety functions. They operate in accordance with IEC 61784‑1:2010 (Fieldbus profiles) and the PROFIsafe bus profile.

 

### Fail-safe modules

Fail-safe modules ET 200SP, ET 200S, ET 200pro, ET 200iSP that can be used in the ET 200SP, ET 200S, ET 200pro or ET 200iSP distributed I/O systems.

Fail-safe modules S7-1500/ET 200MP, which can be used centrally in an S7-1500 or in a distributed I/O ET 200MP system.

Fail-safe module S7-1200 which can be used centrally in an S7-1200 system.

These modules are equipped with integrated safety functions (→ Safety mode) for fail-safe operation (→ Fail-safe operation). They operate in accordance with the → PROFIsafe bus profile.

 

### Fail-safe systems

Fail‑safe systems (F‑systems) are systems that remain in a safe state or immediately switch to another safe state as soon as particular failures occur.

 

### Fault reaction function

→ User safety function

 

### Fault reaction time

The maximum fault reaction time for an F‑system specifies the time between the occurrence of any error and a safe reaction at all affected fail‑safe outputs.

 

### F-blocks

The following fail‑safe blocks are designated as F‑blocks:

- those created by the user in LAD or FBD
- those created by the user as → F-DBs
- those selected by the user from a global library
- those added automatically in the → safety program (→ F-SBs, → automatically generated F-blocks, → F-shared DB, → F-I/O DBs; instance DBs of F-FBs)

All F-blocks are shown in yellow in the project tree.

 

### F-CALL

"F-call blocks" for the → safety program in S7 Distributed Safety.

 

### F-Communication Address Signature

The F-communication address signature is formed from the names and the F-communication UUIDs of communication connections with Flexible F-Link that are used in the safety program.

 

### F-communication DBs

Fail-safe data blocks for the

- safety-related CPU‑CPU communication via S7 connections
- Communication with Flexible F-Link

 

### F-compliant PLC data type (UDT)

An F-compliant PLC data type (UDT) is a PLC data type (UDT) in which you can use all data types that can be used in safety programs.

 

### F‑CPU

An F-CPU is a central processing unit with fail-safe capability that is approved for use in SIMATIC Safety and in which a → safety program can run in addition to the → standard user program.

 

### F-cycle time

The F-cycle time is the time between two calls of an F-runtime group. It is monitored by the F-CPU. As soon as it exceeds the maximum F-cycle time (property of the F-runtime group), the F-CPU is set to the STOP operating state.

(S7-1200, S7-1500): The F-runtime group also has a warning limit. If the F-cycle time exceeds this warning limit, an entry is written to the diagnostic buffer.

 

### F-DBs

Optional fail-safe data blocks that can be read-/write-accessed from anywhere within the safety program (exception: DBs for F-runtime group communication).

 

### F-destination address

→ PROFIsafe address

 

### F-FBs

Fail-safe function blocks (with instance DBs), in which the user programs the → safety program in FBD or LAD.

 

### F-FCs

Fail-safe FCs, in which the user programs the → safety program in → FBD or → LAD.

 

### F‑I/O

Collective name for fail-safe inputs and outputs available in SIMATIC S7 for integration in SIMATIC Safety, among others. The following are available:

- → ET 200eco fail-safe I/O module
- → ET 200eco PN fail-safe I/O module
- → ET 200AL fail-safe I/O module
- → S7-300 fail-safe signal modules
- → Fail-safe modules for S7-1200
- → Fail-safe modules for ET 200MP
- → Fail-safe modules for ET 200SP
- → Fail-safe modules for ET 200S
- → Fail-safe modules for ET 200pro
- → Fail-safe modules for ET 200iSP
- → Fail-safe GSD based DP slaves
- → Fail-safe GSD based I/O devices

 

### F-I/O DB

Fail-safe data block for F-CPUs to an → F-I/O in STEP 7 Safety. An F-I/O DB is automatically created for each F-I/O when the F-I/O is configured in the hardware and network editor. The F-I/O DB contains tags that the user can or must evaluate or write in the safety program as follows:

- For reintegration of the F-I/O after communication errors
- For reintegration of F-I/O after F-I/O or channel faults
- If the F‑I/O must be passivated as a result of particular states of the safety program (for example, group passivation)
- For reassignment of parameters for fail-safe GSD based DP slaves/GSD based I/O devices or enabling HART communication for the F-I/O with the corresponding functionality
- In order to evaluate whether fail-safe values or process data are output

 

### F‑I/O faults

Module-related F‑I/O fault, such as a communication error or parameter assignment error

 

### F-I/Os of PROFIsafe address type 1

F-I/Os which ensure the uniqueness of the PROFIsafe address solely with the F-destination address, for example, ET 200S F-modules. The PROFIsafe address is usually assigned by DIP switches.

 

### F-I/Os of PROFIsafe address type 2

F-I/Os which can ensure the uniqueness of the PROFIsafe address with a combination of F-source address and F-destination address, for example, S7-1500/ET 200MP F-modules. The PROFIsafe address is usually assigned with STEP 7 Safety.

 

### F‑modules

→ Fail-safe modules

 

### F‑OB

The F‑OB calls the main safety block of an F-runtime group in S7‑1200/1500 F‑CPUs.

 

### F‑runtime group

The → safety program consists of one or two F-runtime groups. An F-runtime group is a logical construct of several associated → F-blocks. It is generated internally by the F-system. An F‑runtime group consists of the following F‑blocks:

→ Main safety block, F-OB (S7-1200, S7-1500), if applicable → F-FBs/ → F-FCs, if applicable → F-DBs, → F-I/O DBs, F-blocks of global libraries, instance DBs, → F-SBs, and → automatically generated F-blocks.

 

### F-runtime group information DB

The F-runtime group information DB provides key information on the corresponding → F-runtime group and on the → safety program as a whole.

 

### F‑shared DB

(S7-300, S7-400) Fail-safe data block that contains all of the shared data of the → safety program and more information needed by the F-system. The F-shared DB is automatically inserted and expanded when the hardware configuration is compiled. Using its name F_GLOBDB, the user can evaluate certain data of the → safety program.

 

### F‑SMs

→ S7-300 fail-safe signal modules

 

### F-source address

→ PROFIsafe address

 

### F‑system blocks

Fail-safe system blocks that are automatically inserted and called when the → safety program is compiled in order to generate an executable safety program from the user's safety program.

 

### F‑systems

→ Fail-safe systems

 

### Hardware configuration

The hardware configuration includes the configuration of standard CPUs and standard I/Os as well as the configuration of F-CPUs and F-I/Os.

 

### I-device

The functionality of the "I‑device" (intelligent I/O‑device) of a CPU allows data exchange with an I/O‑controller and thus, its use as an intelligent preprocessor of sub-processes, for example. In this case, the I-device is connected as an I/O-device to a "parent" I/O-controller.

 

### IE/PB link

Device for coupling PROFINET IO and PROFIBUS DP‑systems required, among other things, for IO‑controller-I‑slave communication between -> safety programs in different → F‑CPUs in SIMATIC Safety.

 

### i-parameter

Individual parameters of → fail-safe GSD based DP slaves and → fail-safe GSD based I/O devices

 

### I-slave

The functionality of the "I‑slave" (intelligent DP slave) of a CPU allows data exchange with a DP master and, thus, its use as an intelligent preprocessor of sub-processes, for example. In this case, the I-slave is connected as a DP slave to a "parent" DP master.

 

### Main safety block

"Introductory F-block" for fail-safe programming of the → safety program in STEP 7 Safety. The main safety block is an → F‑FB or → F‑FC that the user assigns to the calling F-OB (S7-1200, S7-1500) or block (OB, FC, FB) (S7-300, S7-400) of an → F‑runtime group.

The main safety block contains the safety program and any calls of other → F-FBs/F-FCs for program structuring.

 

### Network-wide

A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

 

### Organizational measures

For the SIMATIC Safety F-system, these are suitable measures to be defined by the operator of the plant:

- To ensure the safety of the plant in certain operating situations, for example:

  - Monitored operation with manual safety shutdown
  - Operating instructions
  - Regular instructions
- To protect the plant against unauthorized operation or access, for example:

  - Access control to the plant or to the F-CPU or to the PG/PC
  - Operating instructions
  - Regular instructions

 

### Passivation

When passivation occurs in an → F-I/O with inputs, the → F-system provides the safety program with fail-safe values (0) instead of the process data pending at the fail-safe inputs in the PII.

When passivation occurs in an F-I/O with outputs, the F-system transfers fail-safe values (0) to the fail-safe outputs instead of the output values in the PIQ provided by the safety program.

 

### PL

Performance Level (PL) in accordance with ISO 13849‑1:2015 or EN ISO 13849‑1:2015

With SIMATIC Safety, use up to Performance Level (PL) e is possible in → safety mode.

 

### PN/PN coupler

Device for coupling two PROFINET IO systems required for IO controller-IO controller communication between → safety programs in different → F-CPUs in SIMATIC Safety and S7 Distributed Safety.

 

### Productive operation

Operation of a plant in the specified runtime environment for which the safety requirements have been specified and in which all safety requirements must be observed.

By contrast, safety requirements in a test or simulation environment must only be implemented to a limited extent because the risk potential is not the same (for example, there are no physical actuators that could pose a risk).

 

### PROFIsafe

Safety-related bus profile of PROFIBUS DP and PROFINET IO for communication between the → safety program and the → F-I/O in an → F-system. See IEC 61784-3-3:2021 or PROFIsafe – Profile for Safety Technology on PROFIBUS DP and PROFINET IO; Order No: 3.192 (V2.6.1).

 

### PROFIsafe address

The PROFIsafe address (code name according to IEC 61784-3-3:2021) is used as a safety measure for standard addressing mechanisms, such as IP addresses. The PROFIsafe address consists of an F-source address and an F-destination address. Each → F‑I/O therefore has two address parts, an F-source address and an F-destination address.

The F-source address is automatically assigned and is displayed for fail-safe GDS based DP slaves/fail-safe GSD-based I/O devices and ET 200SP F-modules, ET 200MP F-modules, ET 200AL F-modules, ET 200eco PN and S7-1200 F-modules. The F-source address for F-modules ET 200S, ET 200eco, ET 200pro, ET 200iSP and F-SMs S7-300 is always 1. For ET 200SP F-modules, ET 200MP F-modules, ET 200AL F-modules and ET 200eco PN, the F-source address corresponds to the "Central F-source address" parameter of the assigned F-CPU.

You need to configure the F-destination address in the hardware and network editor. You assign the F-destination address for the ET 200S, ET 200eco, ET 200pro, ET 200iSP and F-SMs S7-300 F-modules with a switch. For ET 200SP F‑modules, ET 200MP F-modules, ET 200AL F-modules and ET 200eco PN assign the PROFIsafe address in the hardware and network editor. For S7-1200 F-modules, the F-destination address is automatically assigned by the F-system.

 

### Program signature

→ Collective F-Signature

 

### Project data

The project data includes the → hardware configuration and the → user program.

 

### Project protection

A user administration (UMAC - User Management and Access Control) to create and manage users and roles for projects. In addition, you can protect your project and determine which users are allowed to carry out which functions. For safety-related project data, you have the function right "Edit safety-related project data".

 

### Redundant systems

Redundant systems are characterized by the fact they contain important automation components present multiple times (redundantly). If a redundant component fails, control of the process is maintained.

 

### Reintegration

The switchover from fail-safe values (0) to process data (reintegration of an → F-I/O) takes place automatically or following user acknowledgment in the F-I/O DB. The reintegration method depends on the following:

- The reason for → passivation of the F-I/O/channels of the F-I/O
- The parameter assignment in the → F‑I/O DB or in the configuration itself (for example, ET 200MP fail-safe modules on an S7-1500 F-CPU and S7-1200 fail-safe modules on an S7-1200 F-CPU)

Following reintegration for an → F-I/O module with inputs, the process data pending at the inputs in the PII are provided again for the safety program. For an F-I/O with outputs, the F-system again transfers the output values provided in the PIQ in the safety program to the fail‑safe outputs.

 

### RIOforFA Safety

Remote IO for Factory Automation with PROFIsafe; profile for F-I/O

 

### S7-300 fail-safe signal modules

Fail-safe signal modules of the S7-300 module series that can be used for safety-related operation (→ Safety mode) as centralized modules in an S7-300 or as distributed modules in the ET 200M distributed I/O system. The fail-safe signal modules are equipped with integrated → safety functions. They operate in accordance with the → PROFIsafe bus profile.

 

### S7‑PLCSIM

The S7-PLCSIM application enables you to execute and test your program on a simulated automation system on your programming device or PC. Because the simulation takes place completely in your programming device or PC, you do not need any hardware (CPU, I/O).

 

### Safe state

The basic principle of the safety concept in → fail-safe systems is the existence of a safe state for all process variables. For digital → F‑I/O that conform to IEC 61508:2010, this is always the value "0".

 

### Safety Administration Editor

The Safety Administration Editor provides support for the main tasks of your safety program.

 

### Safety function

Mechanism integrated in the → F-CPU and → F-I/O that allows them to be used in -> fail-safe systems.

According to IEC 61508:2010, a function that is implemented by a safety device in order to maintain the system in the safe state or bring the system to a safe state in the event of a specific fault. (fault reaction function -> user safety function)

 

### Safety message frame

In → safety mode, data are transferred in a safety message frame between the → F-CPU and → F-I/O, or between the F-CPUs in safety-related CPU-CPU communication.

 

### Safety mode

1. Operating mode of → F-I/O in which → safety-related communication can take place using → safety message frames.
2. Operating mode of the safety program. In safety mode of the safety program, all safety mechanisms for error detection and fault reaction are enabled. In safety mode, the safety program cannot be modified during operation. Safety mode can be disabled by the user (→ disabled safety mode).

 

### Safety program

Safety-related user program

 

### Safety protocol

→ Safety message frame

 

### Safety summary

The safety summary is the documentation of the safety-related project data, which supports you during acceptance of the system. The safety summary can be created in printed or electronic form, for example, as a PDF file.

 

### Safety Unit

A Software Unit that contains the entire safety program of an F-CPU.

 

### Safety-related communication

Safety-related communication is used to exchange fail-safe data.

 

### Safety-related hardware configuration

The safety-related hardware configuration includes the safety-related parameters of the F-CPUs and F-I/Os.

 

### Safety-related project data

The safety-related project data includes the safety-related hardware configuration as well as the → safety program.

 

### Sensor evaluation

There are two types of sensor evaluation:

- 1oo1 evaluation – sensor signal is read once
- 1oo2 evaluation - sensor signal is read twice by the same → F-I/O and compared internally

 

### Shared device

The "Shared device" functionality enables modules of an IO device to be shared by different IO controllers. For more information, refer to the "PROFINET with STEP 7" Function Manual.

 

### Signature

→ Collective F-Signature

 

### SIL

Safety Integrity Level SIL in accordance with IEC 61508:2010. The higher the Safety Integrity Level, the more rigid the measures for prevention of systematic faults and for management of systematic faults and random hardware failures.

With SIMATIC Safety, up to Safety Integrity Level SIL3 is possible in safety mode.

 

### Standard communication

Communication used to exchange non-safety-related data

 

### Standard mode

Operating mode of → F-I/O in which → safety-related communication between the F-CPU and the F-I/O by means of → safety message frames is not possible; only → standard communication is possible in this operating mode.

 

### Standard project data

The standard project data includes the standard hardware configuration and the → standard user program.

 

### Standard user program

Non-safety-related user program

 

### Startup of F-system

See section "Notes on startup of the F-system".

 

### User program

The user program comprises the → standard user program and the → safety program.

 

### User safety function

The → safety function for the process can be provided through a user safety function or a fault reaction function. The user only has to program the user safety function. In the event of an error, if the → F-system can no longer execute its actual user safety function, it executes the fault reaction function: for example, the associated outputs are disabled, and the → F-CPU switches to STOP mode, if necessary.

 

### Value status

The value status is additional binary information for a channel value. The value status is entered in the process image input and provides information on the validity of the channel value.

1: A valid process data is output for the channel value.

0: A fail-safe value is output for the channel value.

 

### Versioned instruction

Instruction for which a version is displayed in the "Version" column of the "Instructions" task card:
