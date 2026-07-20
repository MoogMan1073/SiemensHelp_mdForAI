---
title: "Startdrive"
package: ReadMeStartdriveenUS
topics: 37
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Startdrive

This section contains information on the following topics:

- [Safety instructions](#safety-instructions)
- [Notes on use](#notes-on-use)
- [Scope of delivery and supported devices](#scope-of-delivery-and-supported-devices)
- [Installation instructions](#installation-instructions)
- [General information](#general-information)
- [Security measures](#security-measures)

## Safety instructions

This section contains information on the following topics:

- [Fundamental safety instructions](#fundamental-safety-instructions)
- [Manuals on Industrial Cybersecurity](#manuals-on-industrial-cybersecurity)
- [Unsafe operating states due to manipulation of the Safety Integrated parameters after the acceptance test](#unsafe-operating-states-due-to-manipulation-of-the-safety-integrated-parameters-after-the-acceptance-test)
- [Protection of sensitive data in Startdrive project and drive configuration](#protection-of-sensitive-data-in-startdrive-project-and-drive-configuration)
- [Unsafe configuration after importing and downloading files from unknown or untrustworthy sources](#unsafe-configuration-after-importing-and-downloading-files-from-unknown-or-untrustworthy-sources)
- [Ports and protocols (from firmware V6.1)](#ports-and-protocols-from-firmware-v61)

### Fundamental safety instructions

This section contains information on the following topics:

- [General safety instructions](#general-safety-instructions)
- [Warranty and liability for application examples](#warranty-and-liability-for-application-examples)
- [Cybersecurity information](#cybersecurity-information)
- [Industrial cybersecurity](#industrial-cybersecurity)

#### General safety instructions

This section contains information on the following topics:

- [Danger to life if the safety instructions and residual risks are not observed](#danger-to-life-if-the-safety-instructions-and-residual-risks-are-not-observed)
- [Malfunctions of the machine as a result of incorrect or changed parameter settings](#malfunctions-of-the-machine-as-a-result-of-incorrect-or-changed-parameter-settings)

##### Danger to life if the safety instructions and residual risks are not observed

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life if the safety instructions and residual risks are not observed**   If the safety instructions and residual risks in the associated hardware documentation are not observed, accidents involving severe injuries or death can occur.  - Observe the safety instructions given in the hardware documentation. - Consider the residual risks for the risk evaluation. |  |

##### Malfunctions of the machine as a result of incorrect or changed parameter settings

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Malfunctions of the machine as a result of incorrect or changed parameter settings**  As a result of incorrect or changed parameterization, machines can malfunction, which in turn can lead to injuries or death.  - Protect the parameterization against unauthorized access. - Handle possible malfunctions by taking suitable measures, e.g. emergency stop or emergency off. |  |

#### Warranty and liability for application examples

Application examples are not binding and do not claim to be complete regarding configuration, equipment or any eventuality which may arise. Application examples do not represent specific customer solutions, but are only intended to provide support for typical tasks.

As the user you yourself are responsible for ensuring that the products described are operated correctly. Application examples do not relieve you of your responsibility for safe handling when using, installing, operating and maintaining the equipment.

#### Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines and networks.

In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens’ products and solutions constitute one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For additional information on industrial cybersecurity measures that may be implemented, please visit   
[https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html](https://www.siemens.com/industrialsecurity).

Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly recommends that product updates are applied as soon as they are available and that the latest product versions are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase customer’s exposure to cyber threats.

To stay informed about product updates, subscribe to the Siemens Industrial Cybersecurity RSS Feed under   
[https://new.siemens.com/global/en/products/services/cert.html](https://www.siemens.com/cert).

#### Industrial cybersecurity

Further information is provided on the Internet:

[Industrial Security Configuration Manual](https://support.industry.siemens.com/cs/ww/en/view/108862708)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unsafe operating states resulting from software manipulation**  Software manipulations, e.g. viruses, Trojans, or worms, can cause unsafe operating states in your system that may lead to death, serious injury, and property damage.  - Keep the software up to date. - Incorporate the automation and drive components into a state-of-the-art, integrated industrial cybersecurity concept for the installation or machine. - Make sure that you include all installed products in the integrated industrial cybersecurity concept. - Protect files stored on exchangeable storage media from malicious software by with suitable protection measures, e.g. virus scanners. - Carefully check all cybersecurity-related settings once commissioning has been completed. |  |

### Manuals on Industrial Cybersecurity

#### Detailed information on Industrial Cybersecurity

Additional detailed information on "Industrial security" is available in the following Configuration Manuals:

- [Configuration Manual "Industrial Cybersecurity"](https://support.industry.siemens.com/cs/ww/en/view/108862708)

  Here you can find detailed information on SINAMICS, SINUMERIK and SIMOTION products. The information for SINAMICS is applicable up to and including firmware V5.2.x.
- ["SINAMICS Industrial Cybersecurity" Configuration Manual](https://support.industry.siemens.com/cs/ww/en/view/109823969)

  Here you can find detailed information on the extended security functions of SINAMICS drives from firmware V6.1.

  This Configuration Manual also contains information about the secure operation of converters in the intended operating environments, about configuring security functions and about measures to support system hardening.

Both manuals are updated on a regular basis. Ensure that you always use the latest editions.

### Unsafe operating states due to manipulation of the Safety Integrated parameters after the acceptance test

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unsafe operating states due to manipulation of the Safety Integrated parameters after the acceptance test**  Incorrect parameter changes to Safety Integrated Functions after an acceptance test can result in unwanted motion with subsequent severe injury or death.  - To prevent access to your plants and systems by unauthorized persons, implement access restrictions and take the precautions described in the [security information](#industrial-cybersecurity). - To avoid incorrect changes to the configuration and parameters of the Safety Integrated Functions, take the precautions described in the "Acceptance test" chapter of the SINAMICS S120 Safety Integrated Function Manual. - Check the safety log book of SINAMICS Safety Integrated at regular intervals. Verify that no changes have been made to the parameters since the last acceptance test was performed. - If any changes have been made and they are intentional, repeat the acceptance test for the Safety Integrated Functions affected. The purpose of the acceptance test is to ensure and document safe operation of the plant. Correct any unintentional changes back to the original values and repeat the acceptance test. |  |

### Protection of sensitive data in Startdrive project and drive configuration

> **Note**
>
> **Extraction of sensitive data for unprotected transfer of projects**
>
> The parameters of the SINAMICS drives contain your know-how and sensitive configuration data as well as the configuration for protection against modifications for some drive functions like Safety Integrated. After an upload from the device this configuration is stored in the project. If a project is transferred unencrypted via unprotected channels (e.g. email) or stored in an unencrypted form (e.g. in cloud storage), unauthorized persons can extract this configuration from the project files.
>
> - Activate the [project protection](Managing%20users%20and%20roles.md#managing-users-and-roles) in SINAMICS Startdrive to encrypt all drive parameters in the Startdrive project.
> - Encrypt the exported files and project files with some other software.
> - To prevent access to relevant data memory by unauthorized persons, implement access restrictions (e.g. password protection) and take the precautions described in the [security information](#cybersecurity-information).

> **Note**
>
> **Project protection with UMC**
>
> Central user administration with the optional TIA Portal software package User Management Component (UMC) forms the basis for efficient and consistent management of personalized access authorizations within the system, which can significantly reduce the security risk. More information can be found in the "Central user administration with UMC" section in the "Configuring drives" chapter.

> **Note**
>
> For SINAMICS S210 drives with firmware 6.1, at the time that SINAMICS Startdrive V18 SP1 was released for delivery it was **not** possible to encrypt drive data.
>
> The corresponding descriptions on this topic provided in the TIA Portal Information System **cannot** be applied.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Protecting parameters in the SINAMICS drive memory**  The parameters stored in the SINAMICS drive can be read out by unauthorized third parties without protection. Unauthorized persons can therefore cause damage.  - In addition to the project protection or the specific encryption of project files, also activate the know-how protection of the SINAMICS drive. - If setting up know-how protection is not an option, as an alternative, prevent unauthorized persons from accessing your plants and systems. Implement access restrictions and take the precautions described in the [security information](#cybersecurity-information). |  |

---

**See also**

[Industrial cybersecurity](#industrial-cybersecurity)

### Unsafe configuration after importing and downloading files from unknown or untrustworthy sources

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unsafe configuration after importing and downloading files from unknown or untrustworthy sources**  If you use project files or files (e.g. from EPLAN, Microsoft Excel) from unknown or untrustworthy sources or import such files into your Startdrive project, inconsistencies in the project or malfunctions of Startdrive may result. If the appropriate safety precautions are not observed, any untested changes in the system can cause unsafe operating states in your system that may lead to death, serious injury, and property damage.  If project files or imported files are transferred unsigned via unprotected channels (e.g. email) or stored without access protection (e.g. in cloud memories or local memories), unauthorized persons can change the system configuration, thus causing unsafe operating states in your system that may lead to death, serious injury, and property damage.  - Only use projects and files from sources that you know to be trustworthy. - For the consistency check, use functions such as "Flash LED" in the "Go online" dialog or the parameter comparison in the parameter view. - Check whether the machine behavior with the changed system configuration meets your expectations and perform an acceptance test of the Safety Integrated Functions to ensure and document the safe operation of the system. - Take the precautions described in the [security information](#cybersecurity-information). |  |

### Ports and protocols (from firmware V6.1)

#### Overview

| Security setting for interfaces | Parameter | Factory setting | Details |  |
| --- | --- | --- | --- | --- |
| **Ports and protocols** |  |  |  |  |
| X150: Web server access via HTTPS (port 443) | c8997[1] | Inactive | Communication security via TLS 1.2 and TLS 1.3. |  |
| X127: Web server access via HTTPS (port 443) | c8995[1] | Active | Communication security via TLS 1.2 and TLS 1.3. |  |
| X127: Web server access via HTTP (port 80) | c8995[3] | Inactive | No encryption  With Man-in-the-Middle and Replay attacks, data can be intercepted and manipulated. |  |
| **Configuration of fieldbus and associated protocols** |  |  |  |  |
| X150: Fieldbus protocol |  | PROFINET | The PROFINET Context Manager provides an endpoint mapper in order to establish an application relationship (PROFINET AR).  The setting options are drive-specific: |  |
| PROFINET | G220, S210, S200 |  |  |  |
| Ethernet/IP | G220, S210 |  |  |  |
| Modbus TCP | G220 |  |  |  |
| No protocol | G220 |  |  |  |
| X127 and X150: DCP (always activated) |  | Always active Cannot be changed | Discovery and Configuration Protocol (DCP)  Identifies PROFINET devices and allows basic settings to be made. |  |
| X127 and X150: SNMP (port 161) |  | Inactive | The Simple Network Management Protocol (SNMP) enables the reading out and setting of network management data (SNMP managed Objects) by an SNMP manager. SNMP V1 is used. |  |
| **Configuration of the S7 commissioning protocol** |  |  |  |  |
| X150: Access via the S7 protocol PCS7 (port 102) | c8997[2] | Inactive | No encryption and no authentication protection.  The Siemens S7 commissioning protocol can be used in secure PCS7 environments. |  |
| X127: Access via the S7 protocol PCS7 (port 102) | c8995[2] | Inactive |  |  |
| X150: Access via the secure S7 protocol Startdrive (port 102) | c8997[0] | Active | Communication security via TLS 1.2 and TLS 1.3.  The secure S7 commissioning protocol is used for communication between the Startdrive engineering tool and the converter. |  |
| X127: Access via the secure S7 protocol Startdrive (port 102) | c8995[0] | Active |  |  |
| **DHCP configuration** |  |  |  |  |
| X150: DHCP (port 68) |  | Inactive | SINAMICS drives can be integrated into industrial networks using the Dynamic Host Configuration Protocol (DHCP). A DHCP server automatically assigns information that is required, such as IP address, subnet mask and gateway. |  |
| X127: DHCP (port 68) |  | Inactive |  |  |

## Notes on use

### Startdrive

These notes take precedence over statements in other documents.

Please read the notes carefully since important information for installation and use of the software is included for you.

### Associated product name

In the TIA Portal information system, the product "SINAMICS Startdrive" is referred to as "Startdrive".

### Constraints for use

According to the state of the art, it can admittedly not be excluded - given the complexity of the software products - that sporadic functional restrictions can occur under the greatly differing system and application conditions.

In this context, please observe the current limitations, functional restrictions and workarounds that you can find on the following website:

[Limitations for Startdrive](https://support.industry.siemens.com/cs/ww/en/view/55416849)

## Scope of delivery and supported devices

This section contains information on the following topics:

- [Scope of delivery](#scope-of-delivery)
- [Supported devices](#supported-devices)
- [Example of a firmware update for SINAMICS S120](#example-of-a-firmware-update-for-sinamics-s120)

### Scope of delivery

#### Scope of delivery

Startdrive software component

- DVD

  - Article number Startdrive Advanced V19: 6SL3072-4KA02-0XA5
  - Article number Startdrive Advanced V19 Upgrade: 6SL3072-4KA02-0XE5
- Online Software Delivery (OSD) download

  - Article number Startdrive Basic V19 (SW with basic license): 6SL3072-4KA02-0XG0
  - Article number Startdrive Advanced V19 (SW and license): 6SL3072-4KA02-0XG5
  - Article number Startdrive Advanced V19 Upgrade (SW and upgrade license V15..V18 -> V19): 6SL3072-4KA02-0XK5
- SUS (Software Update Service)

  - Article number Startdrive Advanced DVD: 6SL3072-4AA02-0XL8
  - Article number Startdrive Advanced OSD: 6SL3072-4AA02-0XY8
- UCL (Unlock Copy License)

  - Article number Startdrive Advanced current version, UCL OSD: 6SL3072-4AA02-0UG0
  - Article number Startdrive Advanced UCL SUS OSD with CoC: 6SL3072-4AA02-0UY8
  - Article number Startdrive Advanced UCL Upgrade current version OSD: 6SL3072-4AA02-0UK0
- EPL (Enterprise License Master) OSD

  - Article number Startdrive Advanced current version, EPL OSD (with MLK, with "SUS", without CoL): 6SL3072-4AA02-0XP0
  - Article number Startdrive Advanced Version OSD (only CoL, no software): 6SL3072-4AA02-0XQ0
  - Article number Startdrive Advanced Version Upgrade current version OSD (only CoL, no software): 6SL3072-4AA02-0XR0

### Supported devices

#### Supported devices

The Startdrive is the commissioning and diagnostic tool for the drives of the SINAMICS device family.

Startdrive supports the following SINAMICS drive units with the firmware versions specified below and all associated Power Modules that can be combined:

- SINAMICS G120 CU240x (V4.4, V4.5, V4.6 and V4.7)

  - CU240B-2
  - CU240B-2 DP
  - CU240E-2
  - CU240E-2 DP
  - CU240E-2 F
  - CU240E-2 DP-F
  - CU240E-2 PN
  - CU240E-2 PN-F
- SINAMICS G120C (V4.4, V4.5, V4.6 and V4.7)

  - G120C CAN
  - G120C DP
  - G120C PN
  - G120C (USS, ModBus)
- SINAMICS G120P (V4.4, V4.6 and V4.7)

  - G120P-2 CAN
  - G120P-2 DP
  - G120P-2 HVAC
  - G120P-2 PN
- SINAMICS G120P BT (V4.4, V4.6 and V4.7)
- SINAMICS G120D-2 (V4.5, V4.6 and V4.7)

  - CU240D-2 DP
  - CU240D-2 DP-F
  - CU240D-2 PN
  - CU240D-2 PN-F
  - CU250D-2 DP-F
  - CU250D-2 PN-F
- SINAMICS G120 CU250S-2 (V4.6 and V4.7)

  - CU250S-2
  - CU250S-2 DP
  - CU250S-2 PN
  - CU250S-2 CAN
- SINAMICS G110M (V4.6 and V4.7)

  - G110M (USS, ModBus)
  - G110M DP
  - G110M PN
- SINAMICS G115D (V4.7)

  - G115D
  - G115D AS-i
  - G115D PN
- SINAMICS G130 (V4.8, V5.1 and V5.2)

  - CU320-2 PN
- SINAMICS G150 (V4.8, V5.1 and V5.2)

  - CU320-2 PN
- SINAMICS G220 (V6.2)

  - G220
  - G220 Clean Power
- SINAMICS S120 (V4.8, V5.1 and V5.2)

  - CU320-2 PN
  - CU320-2 DP
  - CU310-2 PN
- SIMATIC drive controller

  - SINAMICS S120 Integrated (V5.2)  
    CU320-2 DP
- SINAMICS S150 (V4.8, V5.1 and V5.2)

  - CU320-2 PN
- SINAMICS S210 (V5.2)

  - S210 PN
- SINAMICS S200 (V6.2 and V6.3)

  - S200 PN
- SINAMICS S210 (V6.1 and V6.3)

  - S210 PN
- SINAMICS MV (V4.8, V5.1 and 5.2)

  - CU320-2 PN

### Example of a firmware update for SINAMICS S120

#### Overview

Upgrading older firmware releases to current releases requires a considerable amount of user experience, which is why we have provided a detailed description below.

In this example, a SINAMICS S120 drive equipped with a CU320-2 PN Control Unit is upgraded in the Startdrive project from firmware 4.8 to firmware 5.2 SP3.

![Example: Connection in the network view](images/159877824011_DV_resource.Stream@PNG-en-US.png)

Example: Connection in the network view

#### Requirement

- A SINAMICS S120 drive with firmware 4.8 is configured, which is connected to a SIMATIC S7-1516F-3 N/DP.
- You have the new firmware.

  You can find the firmware files here: [Firmware version 5.2 SP3](https://support.industry.siemens.com/cs/ww/en/view/109780844).
- The drive is in the factory setting.
- The drive is not connected to any other DRIVE-CLiQ participant (e.g. Line Module, Motor Module).
- The drive and its operating unit are connected with one another using a LAN cable via PROFINET interface X150.
- Your operating unit has a card slot for memory cards (or has a connected card reader).

#### Procedure (simplified)

- The offline configuration of a SINAMICS S120 drive is loaded into a drive from the Startdrive project.
- The memory card is taken from the device and is connected to the operating unit using a card reader.
- The USER and OEM directories on the memory card are temporarily backed up in the operating unit.
- The new firmware is copied to the memory card.
- The backed up USER and OEM directories are copied back to the memory card.
- The drive configuration is uploaded into a device newly inserted in the project.

After the backed up directories were copied back to the card, the Control Unit configuration is uploaded to a device newly inserted in the project.

#### Procedure (detailed)

Proceed as follows to upgrade a SINAMICS S120 drive from firmware 4.8 to firmware 5.2:

1. Connect the SINAMICS S120 drive (type: CU320-2 PN) to the power supply.
2. Search for the connected Control Unit in the TIA Portal under "Online access".
3. Open the "Online & diagnostics" screen form, and assign the IP address of the drive to be upgraded to the Control Unit.

   ![Example: Assign IP address](images/159883753611_DV_resource.Stream@PNG-en-US.png)

   ![Example: Assign IP address](images/159883753611_DV_resource.Stream@PNG-en-US.png)

   Example: Assign IP address
4. Load the drive configuration from the project into the device.

   ![Example: Extended loading](images/159885362699_DV_resource.Stream@PNG-en-US.png)

   ![Example: Extended loading](images/159885362699_DV_resource.Stream@PNG-en-US.png)

   Example: Extended loading
5. Activate the "Save parameterization retentively" option in the "Load preview" dialog box. Then click on "Load".

   ![Example: Load preview](images/159887836043_DV_resource.Stream@PNG-en-US.png)

   ![Example: Load preview](images/159887836043_DV_resource.Stream@PNG-en-US.png)

   Example: Load preview

   As a consequence, the parameterization is saved retentively in the ROM.
6. Switch off the drive by disconnecting the 24V supply.
7. Remove the control panel from the drive.

   The card slot is located behind the control panel.
8. Remove the memory card from the card slot.
9. Insert the memory card into the card slot of your operating unit.
10. Open the content of the memory card using the file Explorer.
11. Copy folders "USER" and "OEM" to a temporary directory on your operating unit.

    ![Example: Back up folder](images/161608523147_DV_resource.Stream@PNG-de-DE.png)

    ![Example: Back up folder](images/161608523147_DV_resource.Stream@PNG-de-DE.png)

    Example: Back up folder
12. If available, also back up the "KEYS" folder.

    This folder may contain licenses that are assigned to the memory card.
13. Delete the complete memory card content.
14. Copy the new firmware files to the memory card.
15. Delete folders "USER" and "OEM".
16. Copy backed up folders "USER" and "OEM" from the temporary directory to the memory card.
17. Remove the memory card from your operating unit once copying has been completed.
18. Insert the memory card into the card slot of the drive.
19. Re-attach the control panel.
20. Switch the drive on again.
21. In the Startdrive project, delete the drive with the existing firmware configuration.

    ![Example: Deleting a drive](images/159889221387_DV_resource.Stream@PNG-en-US.png)

    ![Example: Deleting a drive](images/159889221387_DV_resource.Stream@PNG-en-US.png)

    Example: Deleting a drive
22. In the network view, insert a new Control Unit with SINAMICS firmware version 5.2.

    ![Example: Inserting a drive](images/159889966987_DV_resource.Stream@PNG-en-US.png)

    ![Example: Inserting a drive](images/159889966987_DV_resource.Stream@PNG-en-US.png)

    Example: Inserting a drive
23. To connect the inserted device with the drive, adapt the IP address of the newly inserted device.

    ![Example: Correcting the IP](images/159907601931_DV_resource.Stream@PNG-en-US.png)

    ![Example: Correcting the IP](images/159907601931_DV_resource.Stream@PNG-en-US.png)

    Example: Correcting the IP
24. Load the configuration from the drive into the newly created device in the project.

    ![Example: Uploading the configuration](images/159908040075_DV_resource.Stream@PNG-en-US.png)

    ![Example: Uploading the configuration](images/159908040075_DV_resource.Stream@PNG-en-US.png)

    Example: Uploading the configuration
25. Assign the drive to the PLC.

    ![Example: Assigning the PLC](images/159908299019_DV_resource.Stream@PNG-en-US.png)

    ![Example: Assigning the PLC](images/159908299019_DV_resource.Stream@PNG-en-US.png)

    Example: Assigning the PLC

#### Result

You have upgraded the firmware from version 4.8 to firmware version 5.2.

## Installation instructions

This section contains information on the following topics:

- [System requirements](#system-requirements)
- [Installation and deinstallation of the software](#installation-and-deinstallation-of-the-software)

### System requirements

#### Minimum software and hardware requirements

The following table shows the minimum software and hardware requirements that have to be met for the installation of the "Startdrive" software package:

| Hardware/software | Requirement |
| --- | --- |
| Processor | Intel® Core™ i3-6100U, 2.30 GHz |
| RAM | 8 GB |
| Hard disk | S-ATA with at least 20 GB available storage space |
| Network | From 100 Mbit |
| Screen resolution | 1024 x 768 |
| Operating systems * | **Windows 10 (64-bit)**   - Windows 10 Professional Version 22H2 - Windows 10 Enterprise 21H2 - Windows 10 Enterprise 22H2 - Windows 10 Enterprise 2016 LTSC - Windows 10 Enterprise 2019 LTSC - Windows 10 Enterprise 2021 LTSC    **Windows 11 (64 bit)**   - Windows 11 Home Version 21H2 - Windows 11 Home Version 22H2 - Windows 11 Professional Version 21H2 - Windows 11 Professional Version 22H2 - Windows 11 Enterprise 21H2 - Windows 11 Enterprise 22H2    **Windows Server (64-bit)**   - Windows Server 2016 Standard (full installation) - Windows Server 2019 Standard (full installation) - Windows Server 2022 Standard (full installation) |

* Including all security updates up to Microsoft Security Bulletin Summary for August 2023 (MS23-AUG). For more information on the operating systems, refer to the help on Microsoft Windows or the Microsoft homepage.

Certain products may support additional Windows versions. For more information, see the product-specific system requirements or check compatibility with the compatibility tool. The compatibility tool can be found on the Internet at <https://support.industry.siemens.com/kompatool/pages/main/index.jsf?>.

#### Recommended PC hardware

The following table shows the recommended hardware for operating Startdrive.

| Hardware/software | Requirement |
| --- | --- |
| Computer | SIMATIC FIELD PG M6 Comfort or higher (or comparable PC) |
| Processor | Intel® Core™ i5-8400H (2.5 to 4.2 GHz; 4 cores + hyper-threading; 8 MB smart cache) |
| RAM | 16 GB or more (32 GB for larger projects) |
| Hard disk | SSD with at least 50 GB available storage space |
| Network | 1 Gbit (for Multiuser) |
| Monitor | 15.6" Full HD Display (1920 x 1080 or larger) |

#### Supported virtualization platforms

You can install the "Startdrive" software package on a virtual machine. For this purpose, use one of the following virtualization platforms in the specified version or a newer version:

- VMware vSphere Hypervisor (ESXi) 6.7 or higher
- VMware Workstation 15.5.0 or higher
- VMware Player 15.5.0 or higher
- Microsoft Hyper-V Server 2019 or higher

The following host and guest operating systems are recommended for these virtualization platforms:

| Operating system | VMware vSphere Hypervisor (ESXi) | VMware Workstation | VMware Player | Microsoft Hyper-V |
| --- | --- | --- | --- | --- |
| Windows Server 2016 Standard (full installation) | G | - | - | G |
| Windows Server 2019 Standard (full installation) | G | - | - | H/G |
| Windows Server 2022 Standard (full installation) | G | - | - | H/G |
| Windows 10 Professional Version 1909 | H/G | H/G | H/G | G |
| Windows 10 Professional Version 2004 | H/G | H/G | H/G | G |
| Windows 10 Professional Version 2009/20H2 | H/G | H/G | H/G | G |
| Windows 10 Enterprise Version 1909 | H/G | H/G | H/G | G |
| Windows 10 Enterprise Version 2004 | H/G | H/G | H/G | G |
| Windows 10 Enterprise Version 2009/20H2 | H/G | H/G | H/G | G |
| Windows 10 Enterprise 2016 LTSC | H/G | H/G | H/G | G |
| Windows 10 Enterprise 2019 LTSC | H/G | H/G | H/G | G |
| Windows 10 Enterprise 2021 LTSC | H/G | H/G | H/G | G |
| H: Can be used as host operating system  G: Can be used as guest operating system  H/G: Can be used as host and guest operating system  -: Cannot be used as host or guest operating system |  |  |  |  |

> **Note**
>
> - The same hardware requirements apply to the guest operating system as for the respective TIA products.
> - The plant operator must provide sufficient system resources for the guest operating systems.
> - It is recommended to use hardware that is certified by the manufacturers when using HyperV Server and ESXi.
> - When you use Microsoft Hyper-V, accessible stations cannot be displayed.

#### Supported security programs

The following security programs are compatible with "Startdrive":

- Virus scanners:

  - Symantec Endpoint Protection 14.3
  - Trend Micro Apex One
  - McAfee Endpoint Security (ENS) 10.7
  - Windows Defender
  - Qihoo 360 "Safe Guard 12.1" + "Virus scanner"

    | Symbol | Meaning |
    | --- | --- |
    |  | **Notice** |
    | **Insufficient virus protection due to outdated virus scanner**  A virus scanner that is not updated regularly only provides insufficient protection for your data. Your system may be damaged by infiltrating malware. - Make sure that your virus scanner and its databases are always up-to-date. Perform updates regularly. |  |

  The last virus pattern update was on September 13, 2023.
- Encryption software:

  - Microsoft Bitlocker
- Host-based Intrusion Detection System:

  - McAfee Application Control 8.3.6 (Trellix)

### Installation and deinstallation of the software

#### Installation

Before starting the Startdrive setup, close all applications (e.g. Microsoft Word and TIA Portal).

If WinCC Professional is installed after Startdrive, you must subsequently install the S7 block libraries separately.

#### Uninstallation

You have to remove Startdrive in accordance with the MS Windows guidelines.

For this purpose, remove your software package via the MS Windows "Programs and Features" application (in the MS Windows taskbar via "Start > Control Panel > Programs > Programs and Features").

1. Under "Programs and Features", select the "Siemens Totally Integrated Automation Portal" software package.
2. Press the right mouse button to perform "uninstallation".
3. In the first "General settings" dialog, click "Next".
4. In the "Configuration" dialog, from the list, select the software package that you want to uninstall, e.g. Startdrive.

## General information

This section contains information on the following topics:

- [Compliance with the General Data Protection Regulation](#compliance-with-the-general-data-protection-regulation)
- [SINAMICS network settings](#sinamics-network-settings)
- [Network settings TIA Portal](#network-settings-tia-portal)
- [Use of OpenSSL](#use-of-openssl)
- [Recycling and disposal of the USB flash drive](#recycling-and-disposal-of-the-usb-flash-drive)

### Compliance with the General Data Protection Regulation

Siemens complies with the principles of the **General Data Protection Regulation (EU),** in particular the principle of data minimization ("privacy by design"). For the SINAMICS Startdrive product – including the installed SINAMICS DCC option package – this means:

****Windows login, user management and access control (UMAC)****

The product processes or stores the following personal data:

- Windows login

  In the standard configuration, the product saves the login details of the Windows user together with technical function data (e.g. time stamp) in the project. The specified data is saved in order to trace changes in large configurations.

  For SINAMICS Startdrive and the SINAMICS DCC option package, reference to specific persons can be established via the project and all elements contained within it (e.g. devices and DCC charts).

  The specified data can be viewed in the properties of the project and the elements in SINAMICS Startdrive and the SINAMICS DCC option package ("Author" property) and, with the exception of the most recent change to the project, subsequently modified.
- Windows login in multiuser engineering

  For multi-user engineering, various items of technical function data (e.g. time stamp) are saved together with the login of the Windows user concerned in order to be able to trace project changes.
- User management and access control (UMAC)

  The product processes or stores the following personal data:

  - Login data for user management and access control:

    User name, group, password, role, rights.

The product stores personal data only in the project. The user is therefore responsible for ensuring compliance with the statutory data protection provisions. This applies in particular to the transfer of projects. Deleting the project will cause all personal data saved within it to be deleted too. The particularities of multi-user engineering should be taken into consideration here (e.g. that the project not only needs to be deleted locally from the user's PC, but also from the server used).

The data for user management and access control (UMAC) can also be stored explicitly by the user in a connected converter so that it can be checked during a subsequent authentication.

****Support data****

The product only sends personal data to SIEMENS AG if the user explicitly requests this. This occurs in the following cases:

- If the SINAMICS Startdrive program and the SINAMICS DCC option package end unexpectedly, then the user is given the opportunity to send diagnostics information to SIEMENS AG for analysis. If the user avails themselves of this option, then their email address will be collected, transmitted and saved so that they can be contacted in the event of queries.
- The TIA Administrator enables the user to check whether updates are available for SINAMICS Startdrive and the SINAMICS DCC option package and to install them. As the TIA Automation Update Server is used for verification and installation purposes, the IP address of the device used is transmitted for technical reasons.
- Feedback and diagnostics data is collected when using SINAMICS Startdrive and the SINAMICS DCC option package. This data, also including the IP address of the device used, is transmitted to a SIEMENS server. For more information on this topic, refer to the Online Help in the "Notes on the TIA Portal" chapter, keywords "Collecting feedback and diagnostics data".

The above-mentioned personal data and the associated use are required for Windows login, user management and access control (UMAC) and for the support function. The storage of this data is appropriate and limited to what is necessary, as it is essential to identify the authorized users and service contact.

The above-mentioned personal data cannot be stored anonymously or pseudonymized, as it serves the purpose of identifying the operating personnel. The anonymization or pseudonymization, e.g. of the login data, must be performed using suitable login names and contact data by the user of the product.

Our product does not provide any functions for automatically deleting personal data.

### SINAMICS network settings

SINAMICS converters support the communication protocols listed in the following table. The address parameters, the relevant communication layer, as well as the communication role and the communication direction are decisive for each protocol. You require this information to match the security measures for the protection of the automation system to the used protocols (e.g. firewall). The security measures are restricted to Ethernet and PROFINET networks.

The following table shows the various layers and protocols that are used.

#### PROFINET protocols

| PROFINET protocols | Port number | (2) Link layer  (4) Transport layer | Function | Description |
| --- | --- | --- | --- | --- |
| DCP   Discovery and Configuration Protocol | Not relevant | (2) Ethernet II and IEEE 802.1Q and Ethertype 0x8892 (PROFINET) | Accessible nodes,   PROFINET Discovery and configuration | DCP is used by PROFINET to determine PROFINET devices and to make basic settings.  DCP uses the special multicast MAC address:  xx-xx-xx-01-0E-CF,   xx-xx-xx = Organizationally Unique Identifier |
| LLDP   Link Layer Discovery Protocol | Not relevant | (2) Ethernet II and IEEE 802.1Q and Ethertype 0x88CC (PROFINET) | PROFINET Link Layer Discovery protocol | LLDP is used by PROFINET to determine and manage neighborhood relationships between PROFINET devices.  LLDP uses the special multicast MAC address:  01-80-C2-00-00-0E |
| MRP   Media Redundancy Protocol | Not relevant | (2) Ethernet II and IEEE 802.1Q and Ethertype 0x88E3 (PROFINET) | PROFINET medium redundancy | MRP enables the control of redundant routes through a ring topology.  MRP uses the special multicast MAC address:  xx-xx-xx-01-15-4E,   xx-xx-xx = Organizationally Unique  Identifier |
| PTCP   Precision Transparent Clock Protocol | Not relevant | (2) Ethernet II and IEEE 802.1Q and Ethertype 0x8892 (PROFINET) | PROFINET   send clock and time synchronisation, based on IEEE 1588 | PTC enables a time delay measurement  between RJ45 ports and therefore the send cycle synchronization and time synchronization.  PTCP uses the special multicast MAC address:  xx-xx-xx-01-0E-CF,   xx-xx-xx = Organizationally Unique Identifier |
| PROFINET IO data | Not relevant | (2) Ethernet II and IEEE 802.1Q and Ethertype 0x8892 (PROFINET) | PROFINET Cyclic IO data transfer | The PROFINET IO telegrams are used to cyclically transfer IO data between the PROFINET IO controller and IO devices via Ethernet. |
| PROFINET Context Manager | 34964 | (4) UDP | PROFINET connection less RPC | The PROFINET context manager provides an endpoint mapper in order to establish an application relationship (PROFINET AR). |
| Network Time Protocol (NTP) | Dynamic | (4) UDP | NTP client; time synchronization | NTP is only supported for onboard PROFINET (X150). An NTP client port (dynamic UDP port > 50000) is only open at this interface. |

#### Connection-oriented communication protocols

| Connection-oriented communication protocols | Port number | (2) Link layer  (4) Transport layer | Function | Description |
| --- | --- | --- | --- | --- |
| FTP  File Transfer Protocol | 21 | (4) TCP | Server/ incoming | FTP can be used for the first commissioning.  FTP can be activated/deactivated using parameter p8908. |
| DHCP  Dynamic Host Configuration Protocol | 68 | (4) UDP | Dynamic Host Configuration Protocol | Is used to query an IP address.  Is closed when delivered, and is opened when selecting the DHCP mode. |
| http   Hypertext Transfer Protocol | 80 | (4) TCP | Hypertext transfer protocol | http is used for the communication with the CU-internal web server.  Is open in the delivery state and can be deactivated. |
| ISO on TCP  (according to  RFC 1006) | 102 | (4) TCP | ISO-on-TCP protocol | ISO on TCP (according to RFC 1006) is used for the message-oriented data exchange to a remote CPU, WinAC, or devices of other suppliers.  Communication with ES, HMI, etc.  Is open in the delivery state and is always required. |
| SNMP   Simple Network Management Protocol | 161 | (4) UDP | Simple network management protocol | SNMP enables the reading out and setting of network management data (SNMP managed Objects) by the SNMP manager.  Is open in the delivery state and is always required. |
| https   Secure Hypertext Transfer Protocol | 443 | (4) TCP | Secure Hypertext transfer protocol | https is used for the communication with the CU-internal web server via Transport Layer Security(TLS).  Is open in the delivery state and can be deactivated. |
| Internal  protocol | 5188 | (4) TCP | Server/ incoming | Communication with commissioning tools for downloading project data. |
| Reserved | 49152...65535 | (4) TCP  (4) UDP | - | Dynamic port area that is used for the active connection endpoint if the application does not specify the local port. |

#### EtherNet/IP protocols

| EtherNet/IP protocols | Port number | (2) Link layer  (4) Transport layer | Function | Description |
| --- | --- | --- | --- | --- |
| Explicit messaging | 44818 | (4) TCP  (4) UDP | - | Is used for parameter access, etc.  Is closed when delivered, and is opened when selecting EtherNet/IP. |
| Implicit messaging | 2222 | (4) UDP | - | Is used for exchanging I/O data.  Is closed when delivered, and is opened when selecting EtherNet/IP. |
|  |  |  |  |  |

#### Modbus TCP protocols (server)

| Modbus TCP protocols (server) | Port number | (2) Link layer  (4) Transport layer | Function | Description |
| --- | --- | --- | --- | --- |
| Request & Response | 502 | (4) TCP | - | Is used for exchanging data packages.  Is closed when delivered, and is opened when selecting Modbus TCP. |

### Network settings TIA Portal

#### Network settings TIA Portal

The following tables show the network settings of each product you need to analyze the network security and to configure external firewalls:

| STEP 7 Professional and Startdrive |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| ALM | 4410* | TCP | Inbound/outbound | License service | This service provides the complete functionality for software licenses and is used by both the Automation License Manager as well as all license-related software products. |
| RFC 1006 | 102 | TCP | Outbound | S7 communication | Communication to the drive unit via Ethernet/PROFINET for commissioning and diagnostic purposes. |
| PROFIdrive | 34964 | UDP | Outbound | Data set communication | Establishment of communication to the drive unit via Ethernet/PROFINET for commissioning and diagnostic purposes. |
| PROFIdrive | 49152 to 65535 | UDP | Outbound | Data set communication | Communication to the drive unit via Ethernet/PROFINET for commissioning and diagnostic purposes. |
| DCP | --- | Ethernet | Outbound | PROFINET | The DCP protocol (Discovery and basic Configuration Protocol) is used by PROFINET and provides the basic functionality for locating and configuring PROFINET devices. |
| SNMP | 161 | UDP | Outbound | PROFINET | The SNMP client functionality is used by STEP 7 to read status information from PROFINET devices. |
| * Default port that can be changed by user configuration |  |  |  |  |  |

Information on communications services and port numbers of SINAMICS drives can be found under [SINAMICS network settings](#sinamics-network-settings).

### Use of OpenSSL

#### Use of OpenSSL

This product contains [software](https://www.openssl.org/) that has been developed by the OpenSSL project for use in the OpenSSL toolkit.

This product contains cryptographic software created by Eric Young.

This product contains software developed by Eric Young.

### Recycling and disposal of the USB flash drive

#### Recycling and disposal of the USB flash drive

For environmentally sustainable recycling and disposal of your WEEE, please contact a company certified for the disposal of electrical and electronic waste and arrange for the disposal of WEEE in accordance with the regulations in your country.

## Security measures

This section contains information on the following topics:

- [General](#general)
- [Compatibility](#compatibility)
- [Ports and protocols](#ports-and-protocols)
- [Product disposal](#product-disposal)
- [Guidelines for secure operation and secure user management](#guidelines-for-secure-operation-and-secure-user-management)
- [Securing the integrity of necessary data](#securing-the-integrity-of-necessary-data)
- [Security events](#security-events)
- [Security updates](#security-updates)

### General

This chapter discusses specific security measures when using the software.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unsafe operating states due to software manipulation**  Software manipulation, for example viruses, Trojans and malware can cause unsafe operating states in your system that may result in death, serious injury and material damage.  - Keep the software up-to-date. - Integrate the automation and drive components into a holistic, state-of-the-art Industrial Cybersecurity concept of the system or machine. - Take into consideration all of the products used in your holistic Industrial Cybersecurity concept. - Protect files stored on removable media from malware using appropriate protective measures, e.g. virus scanners. - Check all of the cybersecurity-relevant settings when completing commissioning. |  |

#### SINUMERIK / SIMOTION / SINAMICS Industrial Cybersecurity (up to SINAMICS firmware V5.2.x)

More information can be found on the Internet:

[SINUMERIK / SIMOTION / SINAMICS Industrial Cybersecurity Configuration Manual](https://support.industry.siemens.com/cs/ww/en/view/108862708)

Pay particular attention to the explanatory notes on protective zones in Section "General security measures > Network security > Network segmentation".

#### Industrial Cybersecurity (for SINAMICS firmware V6.1)

More information can be found on the Internet:

[Industrial Cybersecurity Configuration Manual (for SINAMICS firmware V6.1)](https://support.industry.siemens.com/cs/ww/en/view/109810578)

- A comprehensive overview of Industrial Cybersecurity is provided in Chapters 3 to 6.
- Pay particular attention to the explanatory notes regarding the cell protection concept in Section 6 "Operating environment and general security measures".

#### Industrial Cybersecurity (for SINAMICS firmware from V6.2)

More information can be found on the Internet:

[Industrial Cybersecurity Configuration Manual (for SINAMICS firmware from V6.2)](https://support.industry.siemens.com/cs/ww/en/view/109823969)

- A comprehensive overview of Industrial Cybersecurity is provided in Chapters 3 to 6.
- Pay particular attention to the explanatory notes regarding the cell protection concept in Section 6 "Operating environment and general security measures".

### Compatibility

#### Checking the compatibility

Before you install the product, you must check the compatibility with respect to additional products that are already installed in your system.

You can use the compatibility tool for this purpose:

[Compatibility tool](https://support.industry.siemens.com/compatool/#/main/start)

### Ports and protocols

#### Ports and protocols

For communications in a network, Startdrive opens the ports and the protocols used.

Ports and protocols depend on the devices that also use the software.

From firmware V6.1, Startdrive uses the following [ports and protocols](#ports-and-protocols-from-firmware-v61) in the TIA Portal.

#### SINUMERIK / SIMOTION / SINAMICS Industrial Cybersecurity

More information can be found on the Internet:

[SINUMERIK / SIMOTION / SINAMICS Industrial Cybersecurity Configuration Manual](https://support.industry.siemens.com/cs/ww/en/view/108862708)

Pay particular attention to the explanatory notes on services and ports in Section "General security measures > System integrity > System hardening > Services and ports".

#### Industrial Cybersecurity (for SINAMICS firmware V6.1)

More information can be found on the Internet:

[Industrial Cybersecurity Configuration Manual (for SINAMICS firmware V6.1)](https://support.industry.siemens.com/cs/ww/en/view/109810578)

Pay particular attention to the explanatory notes on ports and protocols:

- Section "Security functions > Reduction of the attack surface > Least functionality of ports and protocols".
- Section "System overview > Communication relationships".

#### Industrial Cybersecurity (for SINAMICS firmware from V6.2)

More information can be found on the Internet:

[Industrial Cybersecurity Configuration Manual (for SINAMICS firmware from V6.2)](https://support.industry.siemens.com/cs/ww/en/view/109823969)

Pay particular attention to the explanatory notes on ports and protocols:

- Section "Security functions > Reduction of the attack surface > Least functionality of ports and protocols".
- Section "System overview > Communication relationships".

### Product disposal

After the software has been uninstalled from the computer, the following files remain on the storage medium used:

- Empty basis folder of the installation at the storage location used.
- Installation log files under "C:\ProgramData\Siemens\Automation\Logfiles\Setup\".
- Software log files under "C:\ProgramData\Siemens\Automation".
- Software-specific project data and project settings:

  - for SINAMICS Startdrive under "C:\ProgramData\Siemens\Automation"
  - for SINAMICS Technology Extension under "C:\ProgramData\Siemens\Automation\Sinamics OA"
- Created or edited projects at the storage location used.

In addition, generated events remain in the Windows event protocol on the computer.

### Guidelines for secure operation and secure user management

#### Secure operation

The **TIA Portal** and the **Startdrive** application can only be installed or uninstalled by users that have administrator rights for this computer.

The user/administrator must apply the appropriate measures to ensure that the data in his projects created or edited with Startdrive can only be changed by authorized users (access control). To achieve this, he activates UMAC protection for the project and/or drive. And for authorized users, he configures access rights for their user accounts (user management).

An inactivity timeout can also be activated in Startdrive. A lock screen is displayed after a defined inactivity time has elapsed which requires users to log on again.

#### Secure user management

Startdrive utilizes the user management of the TIA Portal to access projects. From firmware V6.1, this user management can also be utilized to access the drive.

You can also use the User Account Control provided as standard in Microsoft Windows. However, this is only applicable for accessing the converter on which Startdrive is installed.

### Securing the integrity of necessary data

#### Securing the integrity of the data required for installation

When running the setup, the product checks the integrity of all data that are required for the installation.

You can only carry out a successful installation if the integrity of all data has been verified.

#### Securing the integrity of data during operation

As soon as you have successfully installed the product, the product continuously ensures the integrity and authenticity of the generated and transferred data.

From firmware V6.1, the S7PLUS (OMS+) protocol is used for secure communications between the software and connected devices.   
Previous firmware versions do not provide these secure communications.

The TIA Portal can also be used in a virtual environment (private cloud).   
In the information system, you can find details on this under keyword "Notes on using the TIA Portal in a virtual environment (private cloud)".

### Security events

The software does not generate any security events in the operating system.

### Security updates

- If you have installed the TIA Portal on your operating unit (PG/PC, notebook), then you can start to search for program updates in the TIA Portal at any time. New versions of individual TIA Portal applications are displayed and can be installed. Security vulnerabilities are also resolved when a new version is installed.

  - On the following Internet page, subscribe to the TIA Portal newsletter that is published on a regular basis: [Stay up to date: TIA Portal](https://www.siemens.com/de/de/produkte/automatisierung/industrie-software/automatisierungs-software/tia-portal.html)
  - Check the installed software in the portal view of the TIA Portal. Generally, a search can be made for updates in view "Installed software". If available, updates can then also be installed.
  - Alternatively, for program updates you can also use the TIA Updater or TIA Administrator (with a higher functional scope).   
    The TIA Updater is installed as standard with every TIA Portal, and can also be called via the search entry. The TIA Administrator must first be separately installed on the PC.  
    Detailed information on this is provided in the information system and keywords "Installing updates and support packages" or "Installing and uninstalling TIA Administrator".
- Subscribe for SIEMENS CERT messages on the following Internet page: [Siemens ProductCERT and Siemens CERT](https://www.siemens.com/global/en/products/services/cert.html) These messages regularly provide you with the latest information.
