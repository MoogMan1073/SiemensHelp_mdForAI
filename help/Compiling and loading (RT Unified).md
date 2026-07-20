---
title: "Compiling and loading (RT Unified)"
package: TransferWCCUenUS
topics: 96
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Compiling and loading (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Unified Comfort Panel (RT Unified)](#unified-comfort-panel-rt-unified)
- [WinCC Unified PC (RT Unified)](#wincc-unified-pc-rt-unified)
- [Simulating control with PLCSIM (RT Unified)](#simulating-control-with-plcsim-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified)
- [Power Tags (RT Unified)](#power-tags-rt-unified)
- [Workflow (RT Unified)](#workflow-rt-unified)
- [Secure communication (RT Unified)](#secure-communication-rt-unified)
- [Loading project encrypted (RT Unified)](#loading-project-encrypted-rt-unified)
- [Loading project unencrypted (RT Unified)](#loading-project-unencrypted-rt-unified)
- [Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)

### Overview (RT Unified)

#### Introduction

To generate an executable runtime project from the configuration data of an HMI device, you must compile the project. You can then transfer the runtime project to the HMI device. This section explains the terms used in this context.

#### Project

In the context of compiling and downloading, the term "project" is used as follows:

- WinCC project: Contains the configuration data of one or more HMI devices in the engineering system
- Runtime project: Contains the compiled configuration data of an HMI device.

#### Runtime

In runtime, you execute the project in process mode.

A distinction is made depending on the HMI device:

- Runtime on a panel

  The runtime software for process visualization runs on the HMI device.

  Before you run a runtime project on a panel, you have to transfer the runtime project to the panel.
- Runtime on a PC

  WinCC Unified PC RT is the runtime software for process visualization.

  If Runtime has been installed on the configuration PC, you can execute the runtime project directly on the configuration PC.

  If you want to execute the runtime project on a different PC, you have to transfer the runtime project to the PC.

#### Compiling and loading

To compile a project means generating a runtime project from the WinCC project.

Downloading a project means transferring the runtime project from WinCC to an HMI device.

#### Simulation

With a simulation, you test the configuration, for example, configured internal tags or a screen change. You simulate the project on the configuration PC.

---

**See also**

[Resources Monitor (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#resources-monitor-rt-unified)
  
[Using WinCC version compatibility (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#using-wincc-version-compatibility-rt-unified)

### Power Tags (RT Unified)

Tags that have a connection to the PLC are called Power Tags.

Information on the Power Tags used is helpful to

- Know when the limits of the system are reached
- Be able to estimate the performance
- Be able to estimate the system load through communication

#### Information on Power Tags used

The number of Power Tags used is displayed in the Inspector window during the following operations:

- A device is compiled.
- Only changes for a device are compiled.
- A device is loaded.
- Only changes for a device are loaded.

### Workflow (RT Unified)

#### Introduction

This section provides an overview of the work steps from creating the WinCC project to displaying runtime on the HMI device.

They work with various applications:

- WinCC Engineering System in the TIA Portal
- WinCC Runtime system on a Unified PC or Unified Comfort Panel
- If the HMI device is Unified PC:

  - SIMATIC Runtime Manager

    You manage the Runtime projects in Runtime Manager.

    You can find additional information in the runtime help in the "SIMATIC Runtime Manager" manual.
  - WinCC Unified - Configuration

    In WinCC Unified - Configuration, you check and manage the settings for secure communication in Runtime.
- If the HMI device is a Unified Comfort Panel:

  - Control Panel

    In the Control Panel, you can start and stop the Runtime project or define a time interval after which the Runtime project starts automatically. You manage the transfer settings in the Control Panel.

#### Configuration in the engineering system

You start the configuration in the engineering system.

1. Create a project.
2. Add one of the following HMI devices:

   - PC General with the HMI application WinCC Unified PC
   - Industrial PC with the HMI application WinCC Unified PC
   - SIMATIC Unified Comfort Panel
3. Configure the required contents of the HMI device.
4. Check the runtime settings of the HMI device, especially the settings for secure communication.

#### Compiling and loading

Then compile your WinCC project into a runtime project and download it to the target HMI device. Before you start the download, check to ensure that the settings for secure communication in the Engineering System and runtime are compatible.

1. Compile the WinCC project.
2. Download the runtime project directly to the HMI device:

   - When you first download the project, set up the connection to the HMI device before you start downloading.
   - When you download the project again, you can either download it completely or changes only.

   For Unified PC, you can also copy the project onto an external storage medium and transfer it to the HMI device via the storage medium. You can download the complete project or download only changes.

> **Note**
>
> Not all changes can be loaded in Runtime with the option "Download to device > Software (only changes)". A list of changes and actions that require complete compiling and complete download can be found under "[Restrictions in compiling and loading changes](#restrictions-in-compiling-and-loading-changes-rt-unified)".

![Compiling and loading](images/105080401931_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Compiling and loading](images/105150813323_DV_resource.Stream@PNG-de-DE.png) | The configuration data are compiled. |
| ![Compiling and loading](images/105151056779_DV_resource.Stream@PNG-de-DE.png) | The runtime project is loaded. |

#### Starting the runtime project

Before you start downloading the project, you specify in the "Load preview" dialog whether the project is started in runtime after the download.

Depending on the HMI device, you have the following options to start the project at a later time:

- Unified PC: To start the runtime of the project later, use the SIMATIC Runtime Manager.
- Unified Comfort Panel: Depending on the configuration, the project starts automatically after the delay time specified in the Control Panel.

  If the project does not start automatically, click "Start Runtime" in the Control Panel.

#### Displaying screens in runtime

Depending on the HMI device, runtime is displayed as follows:

- Unified PC: You can see Runtime in the browser. The user must be logged on in runtime.
- Unified Comfort Panel: Runtime is displayed on the HMI device after the start.

---

**See also**

[Loading project encrypted (RT Unified)](#loading-project-encrypted-rt-unified)
  
[Loading project unencrypted (RT Unified)](#loading-project-unencrypted-rt-unified)

### Secure communication (RT Unified)

#### Introduction

You download your Runtime projects encrypted and password protected using secure communication.

The following components are involved:

- Engineering System on the configuration PC: You manage the "Encrypted transfer" option under "Runtime settings" of the created HMI devices.
- Runtime on the HMI device

  - Unified PC: You manage the "Secure download" option during the installation of the runtime software or in the "WinCC Unified - Configuration" application.
  - Unified Comfort Panel: You set the password for encrypted transfer to the HMI device in the Control Panel under "Service and Commissioning > Transfer".
- SIMATIC Runtime Manager (only for Unified PC): The password is specified in the settings of the Runtime Manager under "General > Secure connection".

  If the "Secure download" option is enabled in Runtime, data exchange is only possible if the identical password is stored in the Runtime Manager.

  You can find more information in the runtime help in the "SIMATIC Runtime Manager" manual.

  > **Note**
  >
  > If the passwords in the Runtime Manager and Runtime do not match, the project cannot be managed in the Runtime Manager.

Runtime is encrypted and password-protected when the "Secure download" option is selected. The data exchange with Runtime is only possible in the engineering system if authentication was successful. The password must be available in the runtime settings of the HMI device and it must match the password in runtime.

#### Password

The password must meet the following criteria:

- A length of 8 to 120 characters
- At least one special character
- At least one number
- At least one lowercase letter
- At least one uppercase letter

#### Settings for encrypted transfer in the Engineering System

By default, the encrypted transfer is enabled in the runtime settings of the HMI device.

In the runtime settings of the HMI device under "General > Encrypted transfer", make the following settings:

- Entering a password in the engineering system
- Allow transfer of initial password via unencrypted loading
- Deactivate encrypted transfer

#### Multiple runtime projects in one runtime

When you download multiple runtime projects to one runtime with WinCC Unified PC, assign the same password in the runtime settings of the created HMI devices in the engineering system. This password must match the password stored in runtime.

---

**See also**

[Loading project encrypted (RT Unified)](#loading-project-encrypted-rt-unified)
  
[Loading project unencrypted (RT Unified)](#loading-project-unencrypted-rt-unified)

### Loading project encrypted (RT Unified)

#### Introduction

If you want to use secure communication, the encrypted transfer must be enabled in the runtime settings of the HMI device. The password must be entered once and confirmed.

Depending on the configuration of runtime, we distinguish between two cases:

- "Secure download" is configured in runtime.
- "Secure download" is not configured in runtime.

#### "Secure download" is configured in runtime

If the password was configured in WinCC Unified Configuration or during the installation of the runtime software, the option "Allow transfer of initial password via unencrypted loading" is not needed.

If the password in the engineering system matches the password configured in runtime, the project is loaded encrypted.

> **Note**
>
> **Deviating passwords**
>
> If the passwords in the runtime settings of the HMI device and in runtime are different, you will have the opportunity to enter the password stored in runtime in the "Load preview" dialog before you download the project. If the input was successful, the password in runtime is replaced by the password in the runtime settings of the HMI device.
>
> The project is loaded encrypted.
>
> To use the Runtime Manager, update the password in the settings of the Runtime Manager.

#### "Secure download" is not configured in runtime

If the option "Secure download" is not configured in runtime, you can activate the option "Allow transfer of initial password via unencrypted loading":

- The runtime project is initially loaded unencrypted.
- Secure download is activated.

  The password entered in the runtime settings of the HMI device is written to the runtime configuration.

  The change can be verified in WinCC Unified Configuration.
- The runtime project is loaded encrypted for all subsequent download operations. The option "Allow transfer of initial password via unencrypted loading" is no longer taken into account.
- To use the Runtime Manager, update the password in the settings of the Runtime Manager.

If the option "Allow transfer of initial password via unencrypted loading" is not enabled, the runtime project is not loaded. An error message is displayed in the "Load preview" dialog.

---

**See also**

[Secure communication (RT Unified)](#secure-communication-rt-unified)
  
[Loading project unencrypted (RT Unified)](#loading-project-unencrypted-rt-unified)

### Loading project unencrypted (RT Unified)

If encrypted transfer is disabled in the runtime settings of the HMI device, a distinction is made between two cases, depending on the configuration:

- "Secure download" is configured in runtime.

  The project is not loaded.

  An error message is displayed in the "Load preview" dialog.

  The encrypted transfer must be enabled in the runtime settings of the HMI device.
- "Secure download" is not configured in runtime.

  The project is loaded unencrypted.

---

**See also**

[Secure communication (RT Unified)](#secure-communication-rt-unified)
  
[Loading project encrypted (RT Unified)](#loading-project-encrypted-rt-unified)

### Restrictions in compiling and loading changes (RT Unified)

#### Compiling and loading changes

Many changes to the configuration can be compiled and loaded in Runtime with the options "Compile > Software (only changes)" or "Download to device > Software (only changes)". After some changes or actions, however, the project must be completely compiled or completely loaded.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Option to compile and load changes is lost**  Please note the following instructions for compiling and loading changes:  - A dialog is often displayed when the option to compile only changes is about to be lost. The change can be confirmed or rejected. When you reject the change, the option to compile and load changes is retained. - When you use the "Undo" button to undo a change that requires complete compiling or loading, the project must still be completely compiled or loaded. - For the relevant changes and actions, an alarm is displayed in the Inspector window when the option to load changes is already lost. The project must be downloaded completely. - Downloading changes is only possible if changes were made to the project beforehand. If no changes were made, only a complete download of the project is possible. |  |

Complete compilation or loading may be necessary under the following circumstances:

- Creating, changing or deleting configuration data
- Actions that directly affect the compiling and loading (e.g. starting a simulation)
- Differences caused by the system (for example, due to installation of an update that must update the resulting compilation data or due to a crash while compiling)

> **Note**
>
> Complete compilation always requires complete loading.

The following changes or actions require complete compilation or complete loading:

| Area of the change or action | Complete compilation required | Complete download required |
| --- | --- | --- |
| Tags | - All changes to the configuration of complex tags of the Array or Struct data type | - Renaming simple tags - Changing the data type for simple tags |
| Styles | - Creating styles - Changing styles - Deleting styles | - |
| Connections | - Creating connections - Changing connections - Deleting connections | - |
| Cycles | - Creating cycles - Changing cycles - Deleting cycles | - |
| Plant objects and plant views | - Creating plant objects and the plant view - Changing plant objects or the plant view - Deleting plant objects or the plant view | - |
| Logging | - Creating the first data log by creating system tags - Changing a data log - Deleting a data log - Creating an alarm log - Changing an alarm log - Deleting an alarm log | - Changing a log name - Changing the path when using the backup - Changing the data type of the tag to which the logging tag is linked. - Changing the logging mode - Changing the compression mode - Changing the source for using compression |
| Audit | - Changing the Audit Trail | - Activating the GMP-compliant configuration - Deactivating the GMP-compliant configuration - Changing the Audit Trail name - Changing the Audit Trail storage medium - Changing the Audit Trail storage directory |
| Unified Collaboration | - All changes in the Runtime settings under "Collaboration" | - |
| Language & font | - All changes in the runtime settings under "Language & Font" | - |
| Identification | - Renaming the WinCC Unified PC RT:   Renaming changes the Runtime ID. The Runtime ID can be viewed in the Runtime settings under "General". | - |
| UMC (User Management Component) |  | - Creating a local user - Changing a local user - Deleting a local user - Creating a role - Changing a role - Deleting a role - Switching between local and central user management |
| Alarms | - | - All changes to alarm classes - Changing the alarm class for discrete alarms or analog alarms - Changing the name, alarm class or the range for alarms from OPC UA A&C |
| Resource lists | - | - Renaming text lists - Renaming Graphic lists |
| Simulation | - | - When you load the project in runtime mode and then load the same project in simulation mode, the simulation must be loaded completely. - When you load the project in simulation mode and then load the same project in runtime mode, the project must be loaded completely. |
| Reporting |  | - Changing the Runtime settings for reporting |
| Dynamic SVG types |  | - Manual assignment of a version number to a type |

---

**See also**

[Compiling a project (RT Unified)](#compiling-a-project-rt-unified)

## Unified Comfort Panel (RT Unified)

This section contains information on the following topics:

- [Specifying runtime settings (RT Unified)](#specifying-runtime-settings-rt-unified)
- [Compiling a project (RT Unified)](#compiling-a-project-rt-unified)
- [Downloading projects (RT Unified)](#downloading-projects-rt-unified)
- [Compiling and loading with team engineering (RT Unified)](#compiling-and-loading-with-team-engineering-rt-unified)
- [Error messages during loading of projects (RT Unified)](#error-messages-during-loading-of-projects-rt-unified)
- [Starting runtime (RT Unified)](#starting-runtime-rt-unified)
- [Reducing the project size (RT Unified)](#reducing-the-project-size-rt-unified)
- [Maintenance of the HMI device (RT Unified)](#maintenance-of-the-hmi-device-rt-unified)

### Specifying runtime settings (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [General (RT Unified)](#general-rt-unified)
- [Alarms (RT Unified)](#alarms-rt-unified)
- [Services (RT Unified)](#services-rt-unified)
- [Language & font (RT Unified)](#language-font-rt-unified)
- [Remote access (RT Unified)](#remote-access-rt-unified)
- [Storage system (RT Unified)](#storage-system-rt-unified)
- [Settings for tags (RT Unified)](#settings-for-tags-rt-unified)
- [Good Manufacturing Practice (RT Unified)](#good-manufacturing-practice-rt-unified)
- [User management (RT Unified)](#user-management-rt-unified)
- [OPC UA server (RT Unified)](#opc-ua-server-rt-unified)
- [Layers (RT Unified)](#layers-rt-unified)
- [Reporting (Unified Comfort Panel) (RT Unified)](#reporting-unified-comfort-panel-rt-unified)

#### Introduction (RT Unified)

Before you compile and download a project, update the runtime settings of the HMI device. You specify the Runtime languages, for example, or activate collaboration.

To edit the runtime settings for an HMI device, open "Runtime settings" in the project tree below the HMI device.

#### General (RT Unified)

##### Identification

The runtime ID is the unique identification of a runtime project. Based on the runtime ID, you can determine whether a project has already been downloaded to the HMI device.

##### Encrypted transfer

To download the project encrypted, the same password must be stored in the runtime settings and in runtime. Alternatively, transfer the password unencrypted during the initial download.

##### Screen

Under "Screen", you specify the start screen and the style of the HMI device.

The start screen is displayed after runtime start.

Select the screen resolution. The setting of the HMI device is used by default.

> **Note**
>
> **Display of a changed start screen**
>
> You have defined a start screen in the project and started runtime. When you define another start screen and download only changes to the device, the last active screen is displayed in runtime.
>
> After reloading the project, refresh the screen in Runtime.

---

**See also**

[Secure communication (RT Unified)](#secure-communication-rt-unified)

#### Alarms (RT Unified)

##### Controller alarms and diagnostics

> **Note**
>
> WinCC only supports controller alarms of a SIMATIC S7-1500. WinCC only supports controller alarms that are automatically updated by the central alarm management in the PLC.

One or several HMI connections to a PLC are shown in "Controller alarms".

You can manage the following options:

- "Display classes":

  You filter the controller alarms via display classes. You specify for each connection which display classes are displayed on the HMI device.
- "Automatic update":

  Controller alarms are automatically updated on the HMI device.

  Requirement: The option "Central alarm management in the PLC" must be enabled.
- "System diagnostics":

  System diagnostic alarms can be displayed in runtime.

  Requirement: The "Automatic update" option must be enabled.
- "Security events":

  Security events can be displayed in runtime.

  Requirement: The "Automatic update" option must be enabled.

##### State texts

You specify the state texts of alarms in the runtime settings. The state texts are displayed in runtime in the alarm control.

Specify the state texts in other languages under "Languages & Resources > Project texts".

---

**See also**

[Configuring the display of security events (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-display-of-security-events-rt-unified)
  
[Configuring the status texts of alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-status-texts-of-alarms-rt-unified)
  
[Configuring the display of system diagnostics alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-display-of-system-diagnostics-alarms-rt-unified)
  
[Filtering PLCs alarm using display classes (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#filtering-plcs-alarm-using-display-classes-rt-unified)

#### Services (RT Unified)

##### SMTP communication

SMTP communication enables automatic sending of e-mails when events occur.

Specify the port for SMTP communication.

#### Language & font (RT Unified)

##### Runtime language and font selection

You configure project languages that are available as runtime languages for the respective device. You also define the order in which the languages are switched.

At Runtime start, the language that has the lowest number in the "Order" column under "Runtime settings > Language & font" in the TIA Portal is used. You change the order with ![Runtime language and font selection](images/134928713995_DV_resource.Stream@PNG-de-DE.png).

The fixed font 1 is always provided for the respective HMI device.

When you enable the option "Enable for logging" for a language, alarm texts are logged in the respective language. To keep the size of the log relatively small, log only alarm texts in the required languages.

---

**See also**

[Editing log contents with scripts and system functions (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#editing-log-contents-with-scripts-and-system-functions-rt-unified)
  
[Enabling the runtime language (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#enabling-the-runtime-language-rt-unified)

#### Remote access (RT Unified)

This section contains information on the following topics:

- [Collaboration (RT Unified)](#collaboration-rt-unified)
- [Web Client (RT Unified)](#web-client-rt-unified)
- [Smart Server (RT Unified)](#smart-server-rt-unified)

##### Collaboration (RT Unified)

###### General settings

- "Enable collaboration" option: Enables or disables Runtime Collaboration between HMI devices.

  > **Note**
  >
  > If this option is selected, Unified Runtime or a simulation only starts if the Runtime Collaboration certificate of the HMI device is installed on the device. If the certificate is missing, the project has the status "partly running".

###### Identification

The following information must be unique for all devices participating in a collaboration:

- System ID:

  The system IDmust be unique for each device participating in Unified Collaboration, as this ID is used for communication between the devices.
- Collaboration name:

  Assign a collaboration name or select "Generate collaboration name automatically".
- IP address / Host name

###### Connect actively to

A list of all HMI devices available for collaboration with system ID and IP address / host name is displayed. You select the HMI devices to which the current HMI device provides collaboration.

> **Note**
>
> **Collaboration is enabled in both directions**
>
> The HMI device that you selected under "Connect actively to" can display screens of the current HMI device and vice versa. Collaboration is always enabled in both directions, even if you only have the connection activated for one collaboration device.

---

**See also**

[Defining collaboration settings (RT Unified)](Using%20distributed%20systems%20%28RT%20Unified%29.md#defining-collaboration-settings-rt-unified)

##### Web Client (RT Unified)

###### Web client configuration

When you activate access via web client, you can access the runtime of the Unified Comfort Panel from any browser.

##### Smart Server (RT Unified)

###### Smart Server configuration (only available for Unified Comfort Panel)

When you activate the Smart Server, you enable remote access to the Unified Comfort Panel via the Smart Client application.

###### Users

You set passwords for up to two users and enable the users for remote access to the control panel of the Unified Comfort Panel.

###### Communication

- You enable or disable the use of self-signed certificates by selecting or clearing the check mark.
- Port configuration

  You enable or disable the automatic port configuration by selecting or clearing the check mark.

  If you want to specify a manual port for access from desktop applications, enter the port number.

---

**See also**

[WinCC Smart Server (RT Unified)](Using%20distributed%20systems%20%28RT%20Unified%29.md#wincc-smart-server-rt-unified)

#### Storage system (RT Unified)

##### Introduction

You specify the storage locations of the following databases:

- Database for tag persistency
- Database for data logging
- Database for alarm logging

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Different storage locations cannot be used for Unified Comfort Panel**  When you specify a different storage location for a log in the "Logs" editor other than the main database storage location defined in the runtime settings of the HMI device, the log cannot be used. |  |

You have the option of saving parameter set types on external storage media. If the databases for data logs or alarm logs and the parameter set types are stored on the same storage medium and the storage medium is changed while runtime is running, the parameter set types can be affected.

> **Note**
>
> Use different storage media for parameter set types and logging.

##### Database type

Unified Comfort Panel supports the "SQLite" database type.

##### Database storage location for tag persistency

You can specify tag persistency for internal tags. The last values of the persistent tags are used after Runtime has been started.

A separate database is used for tag persistency. The values of the tags are available again after restarting runtime or restarting or switching off the HMI device.

Specify the storage location of the database:

- Off
- SD-X51
- USB-X61
- USB-X62

If no storage medium is connected to the respective interface, an alarm is displayed in the alarm control.

If the log databases and the database for tag persistency are stored on the same storage medium and the storage medium is changed while runtime is running, tag persistency can be affected.

> **Note**
>
> Use different storage media for tag persistency and logging.

##### Location of the main database for data logging

Specify the storage location of the databases for data logging:

- Off
- SD-X51
- USB-X61
- USB-X62

You have the option of specifying a path on the storage medium.

If no storage medium is connected to the respective interface, an alarm is displayed in the alarm control.

##### Location of the main database for alarm logging

Specify the storage location of the databases for alarm logging:

- Off
- SD-X51
- USB-X61
- USB-X62

You have the option of specifying a path on the storage medium.

If no storage medium is connected to the respective interface, an alarm is displayed in the alarm control.

---

**See also**

[Specify tag persistency (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#specify-tag-persistency-rt-unified)
  
[Storage locations of logs (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#storage-locations-of-logs-rt-unified)

#### Settings for tags (RT Unified)

You have the option of synchronizing HMI tags with the connected PLC tags. The position of a data value in the structure of a data block is thus mapped in the HMI tag name. If necessary, the PLC name is set as a prefix. You synchronize the tags in the "HMI tags" editor.

You specify before the synchronization whether and under which conditions the names are synchronized.

##### Synchronization of the name of the PLC tag in the engineering station

To avoid conflicts within complex tag types, configure how the delimiters of the path specification from STEP 7 are replaced in WinCC during name synchronization:

- Replace delimiters

  Depending on your selection, the delimiters of all hierarchy levels are replaced during synchronization.
- Replace invalid characters
- PLC prefix

  The PLC name is set as a prefix to the HMI tag name. You set the option for each HMI connection.

> **Note**
>
> **Duplicate tag names**
>
> If the generated tag name is already in use, a number is added in parentheses, e.g. Datablock_1_Static_2{1}(1).

##### Example

The "PLC1" controller contains the structured data block "DB1". The "Db1.a[1].b.c[3]" data block element is used in a picture. Depending on your settings, the HMI tag name is generated as follows:

| Selected option | HMI tag name |
| --- | --- |
| PLC prefix | Plc1.Db1.a[1].b.c[3] |
| Replace dot and parenthesis with ; ( ) | Db1;a(1);b;c(3) |
| Replace dot and parenthesis with _ { }  PLC prefix | Plc1_Db1_a{10}_b_c{3} |

---

**See also**

[Synchronizing tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#synchronizing-tags-rt-unified)

#### Good Manufacturing Practice (RT Unified)

Traceability and therefore the documentation of production data is becoming increasingly important in many sectors such as the pharmaceutical industry, the food and beverage industry, and the related mechanical engineering industry.

Therefore, sector-specific and cross-industry standards have been developed for the electronic documentation of production data.

The most important set of regulations is the FDA guideline 21 CFR Part 11 for electronic data records and electronic signatures issued by the FDA, the US Food and Drug Administration. In addition, different EU regulations apply, such as EU 178/2002, depending on the industry.

Requirements for production systems in these industries have been developed on the basis of 21 CFR Part 11 and the corresponding layout to comply with GMP (Good Manufacturing Practice). They are also required for other industries.

The following main requirements are derived from these directives and regulations:

- Creation of an Audit Trail or operating trace in runtime

  Based on this document, it is possible to trace the user who carried out the operator action on the machine at what time.
- Important process steps must also be assigned to a clear responsibility, for example, via an electronic signature.

##### GMP (Good Manufacturing Practice)

1. Enable GMP-compliant configuration.
2. If necessary, select a text list entry that contains the reason for the GMP-relevant tags.

#### User management (RT Unified)

You specify whether you are using a local or a central user management. By default, the use of the local user management is specified in the engineering system.

Local users are only valid for this project.

You manage central users in the TIA User Management Component (UMC).

##### User administration configuration

- When you activate the local user management, you use the users and user roles that you have created under "Security settings > Users and roles" for management.
- When you activate the central user management, the users, user roles and their rights are applied from the TIA User Management Component (UMC). To access the UMC, you must specify the server address and the server ID.

---

**See also**

[Central user management (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#central-user-management-rt-unified)

#### OPC UA server (RT Unified)

This section contains information on the following topics:

- [General (RT Unified)](#general-rt-unified-1)
- [Options (RT Unified)](#options-rt-unified)
- [Security (RT Unified)](#security-rt-unified)

##### General (RT Unified)

OPC is a standardized manufacturer-independent software interface for data exchange in automation engineering. OPC UA is the technology succeeding OPC. OPC UA is platform-independent and supports different protocols as communication medium.

To work with OPC UA in WinCC Unified, the OPC UA server must be enabled in the TIA Portal in the Runtime settings of the HMI device.

###### Read/write tags and register tags/alarms

When you enable the "Operate as OPC UA server" option in the HMI device, the protection for unauthorized internal and external access is downgraded.

- Enable the "Operate as OPC UA server" option.

  A security note is displayed.

After enabling the option, all other settings of the OPC UA Server will become available.

###### Alarms and Conditions

- To display alarm conditions in the address range of the server, select the option "Enable Alarms and Conditions on the OPC UA server".
- To disable or acknowledge alarms on the OPC UA Client, for example, select the option "Allow operation of alarms on the OPC UA Client". To enable this option, the "Enable Alarms and Conditions on the OPC UA server" option must be enabled.

##### Options (RT Unified)

###### General

Define the following settings:

- Port

  Default value: 4890

  Do not use a port number that is already assigned to another application.
- Maximum session timeout (s)

  Default value: 600000 s
- Maximum number of OPC UA sessions

  Default value: 100

###### Subscriptions

Define the following settings:

- Minimum publication interval (ms)

  Default value: 100 ms
- Maximum number of monitored items

  Default value: 0

##### Security (RT Unified)

This section contains information on the following topics:

- [Secure connection (RT Unified)](#secure-connection-rt-unified)
- [User authentication (RT Unified)](#user-authentication-rt-unified)

###### Secure connection (RT Unified)

###### Security policies

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Reduced security**  When the option "No OPC UA Server Security" is enabled, any OPC UA client can connect to the OPC UA server regardless of the following settings. |  |

The following section contains a list of all security policies available on the server.

- Activate the required security policies.

###### User authentication (RT Unified)

###### Guest authentication

- To allow access by anonymous users to the OPC UA server, enable the option "Enable guest authentication".

  An authentication by means of user name and password is not required.

  Security is restricted to the degree that you determine by assigning rights to this user.

###### Authentication by means of user name and password

- To allow access by users with user name and password to the OPC UA server, enable the option "Authentication with user name and password".

  If access to the OPC UA server is to require the user name and password, the user must be assigned the role "HMI Administrator". The "HMI Administrator" role has the system-defined "OPC UA - read and write access" function right. The settings made must then be synchronized with the user management in runtime.

#### Layers (RT Unified)

##### Default names of the layers

Adjust the default names of the layers.

#### Reporting (Unified Comfort Panel) (RT Unified)

##### Report system

Make the reporting settings of the HMI device here.

|  |  |  |
| --- | --- | --- |
| "Enable Reporting" | You can create report templates based on this project or project report jobs and generate reports in Runtime only if reporting is enabled. |  |
| "Storage location for the Reporting database" | The Reporting database stores the actions and settings made in Runtime in the "Reports" control. |  |
| "Storage location" | Select a storage medium.  You cannot remove the storage medium during runtime. |  |
| "Folder" | Enter the path to a folder of the storage medium. Use an existing folder. Use the Linux notation.  The Reporting database is stored in the folder.  Default folder: The project folder |  |
| "Storage location for reports" | Select the local main storage location for the generated reports. |  |
| "Storage location" | Select a storage medium.  You can remove the storage medium during runtime, for example, by means of the system function "RemoveStorageMedium".   Ensure that, after calling the system function, no report jobs are pending which have this storage location as the target. If necessary, deactivate the corresponding report jobs in the "Reports" control. |  |
| "Folder" | Enter the path to a folder of the storage medium. Use an existing folder. Use the Linux notation.  The reports are stored in the folder.  Default folder: "`media/simatic/``<storage medium>``/Reports`​" |  |

> **Note**
>
> **Devices with a device version lower than V18**
>
> Unified Comfort Panels with a device version of lower than V18 always have the same settings:
>
> - Reporting is enabled.
> - The storage locations are predefined:
>
>   Storage location for reports: `media/simatic/X51/Reports` folder on the SD card inserted in the panel.
>
>   Storage location of the reporting database: The respective project folder under `media/simatic/X51` on the SD card plugged into the panel.
>
> ​You cannot change the settings.

### Compiling a project (RT Unified)

#### Basics

Compilation results in a runtime project that is executable on the respective HMI device.

A project can be compiled explicitly or implicitly:

- Explicit: The compilation is started manually. Compile the entire project or only changes.

  Explicit compiling is described in the following section.
- Implicit: The project is downloaded without previous manual compilation.

  The project is compiled in the background even as you are configuring it in WinCC.

  This reduces the compilation times before downloading the project.

> **Note**
>
> Changes to S7 blocks are not automatically compiled in the background. If you are using HMI tags in the project that are connected to PLC tags, you should also compile all changed S7 blocks before you compile the HMI device.

#### Requirement

- A project is open.

#### Compiling changes of a project

1. Select an HMI device in the "Project tree".
2. There are two ways to start compiling the changes:

   - Press the "Compile" button in the toolbar.
   - Select "Compile > Software (only changes)" from the shortcut menu.

#### Compiling a project completely

1. Select an HMI device in the "Project tree" area.
2. Select "Compile > Software (rebuild all)" from the shortcut menu.

> **Note**
>
> When a project was compiled completely, the project must also be downloaded completely afterward.

#### Compiling projects of multiple HMI devices simultaneously

1. Select the HMI devices using multiple selection in the project tree.
2. To compile the changes to the projects, select the "Compile" button in the toolbar.

   Alternatively, select "Download to device > Software (only changes)" from the shortcut menu.
3. To compile the projects completely, select "Download to device" > "Software (rebuild all)" from the shortcut menu.

#### Result

The configuration data of the selected HMI devices is being compiled. If errors occur during compilation, the errors are shown in the Inspector window under "Info > Compile". Correct the errors and recompile the project.

Load the compiled project.

---

**See also**

[Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)
  
[Simulate Unified Comfort Panel (RT Unified)](Simulate%20runtime%20%28RT%20Unified%29.md#simulate-unified-comfort-panel-rt-unified)
  
[Downloading projects (RT Unified)](#downloading-projects-rt-unified)

### Downloading projects (RT Unified)

This section contains information on the following topics:

- [Basics for downloading projects (RT Unified)](#basics-for-downloading-projects-rt-unified)
- [Initial download of a project (RT Unified)](#initial-download-of-a-project-rt-unified)
- [Complete reloading of a project (RT Unified)](#complete-reloading-of-a-project-rt-unified)
- [Download changes only (RT Unified)](#download-changes-only-rt-unified)
- [Loading projects of multiple HMI devices simultaneously (RT Unified)](#loading-projects-of-multiple-hmi-devices-simultaneously-rt-unified)
- [Using external storage medium (RT Unified)](#using-external-storage-medium-rt-unified)

#### Basics for downloading projects (RT Unified)

##### Introduction

During downloading, the compiled project is transferred to an HMI device. Only one project can be in runtime on an HMI device at a time.

Before the download, use the "Load preview" dialog to determine whether existing data is retained and whether logs are reset. The following data can be retained or overwritten:

- Runtime values:

  Tag values, active alarms and user data
- Logs:

  Data logs, alarm logs, Audit Trails and context logs

The HMI device name entered in the project tree is used for PROFINET communication. The use of the name corresponds to the default setting of the PROFINET interface of the HMI device. For devices with more than one PROFINET interface, the name of the IE CP is automatically added to the device name with a separating period. The name is written to the HMI device during download. If a device name for PROFINET communication has already been entered in the HMI device, it will be overwritten.

You can find additional information about these settings in the information system in the "Assigning a device name and IP address" section.

When TIA Portal detects incompatible Runtime versions during online loading, you have the option in the "Load Preview" dialog to install an image with a compatible, installed Runtime version to the Panel before the download.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the installed Runtime version deletes all data from the HMI device.**  Data is deleted on the target system when you change the installed Runtime version.   When the operating system is updated, the project, parameter sets and user administration on the HMI device are deleted.  Before updating the operating system, save the data on the HMI device, if required.  When the operating system is updated with a reset to factory settings, all data on the HMI device is deleted and all settings in the control panel are reset to the factory settings. |  |

The compilation of the project is checked before downloading and missing content is compiled. This ensures that the latest version of the project is always downloaded.

When you download a project again, you can decide whether you want to download only changes or the complete project. If you want to download only changes, a compilation of changes must be possible beforehand.

> **Note**
>
> **No data loss when loading is interrupted**
>
> Existing data on the HMI device is only deleted when the transfer is complete.

##### Runtime ID

At the start of the configuration, each project receives a runtime ID which is transferred to the HMI device during downloading. If you have already downloaded a project, the download process recognizes the project using the Runtime ID. If the HMI device name is changed in the configuration, the Runtime ID also changes.

> **Note**
>
> **Existing runtime projects on the HMI device**
>
> If a runtime project with the same Runtime ID is already available on the HMI device, the project is overwritten. In this case, the options "Software (only changes)" and "Software (all)" are available for loading.
>
> If a runtime project with a new runtime ID is downloaded to the HMI device, the existing runtime project is replaced by the new project. In this case, only the option "Software (all)" is available for the download.
>
> In both cases, existing project data on the HMI device is overwritten.

##### Controlling the transfer behavior on the HMI device

You enable the transfer on the HMI device in the Control Panel under "Transfer". When the transfer is activated, the project can be downloaded.

> **Note**
>
> **Disable transfer after commissioning**
>
> Disable the transfer after the commissioning phase so that no project can be loaded inadvertently.
>
> An inadvertent transfer mode can trigger unwanted responses in the plant.
>
> In order to restrict access to the transfer settings and thus avoid unauthorized changes, enter a password in the Control Panel.

For more information on the transfer settings, refer to the documentation of the HMI device.

##### Transferring Runtime add-ons in WinCC

Projects may contain Runtime add-ons in the form of controls or CSP (Communication Support Packages). These Runtime add-ons are automatically transferred with the project.

---

**See also**

[Complete reloading of a project (RT Unified)](#complete-reloading-of-a-project-rt-unified)
  
[Compiling a project (RT Unified)](#compiling-a-project-rt-unified)
  
[Initial download of a project (RT Unified)](#initial-download-of-a-project-rt-unified)
  
[Secure communication (RT Unified)](#secure-communication-rt-unified)
  
[Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)
  
[Simulate Unified Comfort Panel (RT Unified)](Simulate%20runtime%20%28RT%20Unified%29.md#simulate-unified-comfort-panel-rt-unified)
  
[Compiling and loading with team engineering (RT Unified)](#compiling-and-loading-with-team-engineering-rt-unified)
  
[Basics on version compatibility (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#basics-on-version-compatibility-rt-unified-1)

#### Initial download of a project (RT Unified)

##### Introduction

The first download of a project is different from any subsequent download processes:

- The connection to the HMI device must be set up before the download.
- The project is always downloaded completely during the first download.

  > **Note**
  >
  > **Runtime is stopped during a complete download**
  >
  > The project running in runtime is stopped when a project is executed in runtime while you are completely downloading the project.

##### Requirement

- The project has been compiled without errors.
- A user is configured.
- The HMI device is connected to the configuration PC.
- The Control Panel is started on the HMI device.
- The protocol by which the project is loaded is set on the HMI device in the Control Panel under "Settings".
- The transfer is activated on the HMI device.

##### Editing connection parameters before download

1. Select the HMI device in the project tree.
2. Select "Online > Extended download to device" in the menu.

   The "Extended download" dialog opens.
3. Configure the interface.
4. Click "Connect" and load the project.

   The Runtime project is downloaded with changed connection parameters.

##### Options when initially loading a project

**Runtime values: Tag values, active alarms and user data**

Select whether you want to keep the current values or reset the values to the start values.

Select "Reset to start values" at the time of initial loading.

**Reset logs: Data logs, alarm logs, Audit Trails and context logs**

Select whether you want to reset all logs or no log in Runtime.

##### Initial loading of a project

1. Select the HMI device in the project tree.
2. In the toolbar, select the "Download to device" button or select "Download to device" > "Software (all)" from the shortcut menu.

   The "Extended download" dialog opens.
3. Configure the interface. Make sure that the settings match the transfer settings in the HMI device:

   - Select the protocol used, for example, Ethernet.
   - Configure the relevant interface parameters on the configuration PC.
   - Make any interface-specific or protocol-specific settings required on the HMI device.
4. Click "Connect".

   The connection is established and a dialog is displayed.
5. Select "Load".

   The compilation of the project is checked and missing content is compiled.

   The compilation result is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed.
6. Check the displayed default settings and change the settings as necessary:

   - Specify whether runtime should start on the target system after the download.
   - Select "Reset to start values".
   - Specify whether all logs are reset in runtime.

     The setting is only accepted when you have selected "Start runtime".
7. Click "Download".

**Note**

When you select "Download to device" > "Software (only changes)" from the shortcut menu, the project is still downloaded completely during the initial download.

##### Result

The project is downloaded to the selected HMI device with the runtime extensions it contains.

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

On completion of the successful download of the project, you can execute it on the HMI device.

> **Note**
>
> **No data loss when loading is interrupted**
>
> Existing data on the HMI device is only deleted when the transfer is complete.

---

**See also**

[Loading projects of multiple HMI devices simultaneously (RT Unified)](#loading-projects-of-multiple-hmi-devices-simultaneously-rt-unified)
  
[Specify tag persistency (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#specify-tag-persistency-rt-unified)
  
[Basics for downloading projects (RT Unified)](#basics-for-downloading-projects-rt-unified)
  
[Secure communication (RT Unified)](#secure-communication-rt-unified)
  
[Compiling a project (RT Unified)](#compiling-a-project-rt-unified)

#### Complete reloading of a project (RT Unified)

##### Options when reloading a project

**Runtime values: Tag values, active alarms and user data**

Select whether you want to keep the current values or reset the values to the start values.

With the "Keep selected" option, you can specify which values you want to keep.

- Current values of tags and pending alarms
- Current user management data

**Reset logs: Data logs, alarm logs, Audit Trails and context logs**

Select whether you want to reset all logs or no log in Runtime.

##### Requirement

- The project has been compiled without errors.
- The project has been downloaded at least once before.

##### Reloading a project

1. Select the HMI device in the project tree.
2. Select "Download to device > Software (all)" from the shortcut menu.

   The compilation of the project is checked and content that has not been compiled is compiled.

   The compilation result is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed.
3. Check the displayed default settings and change the settings as necessary:

   - Specify whether runtime should start on the target system after the download.
   - Specify whether tag values, active alarms, and user data are retained.

     The setting is only accepted when you have selected "Start runtime".

     To retain internal tags, the persistency must be enabled in the settings of the respective tag.
   - Specify whether all logs are reset in runtime.

     The setting is only accepted when you have selected "Start runtime".
   - Specify whether the IDs of objects in the Engineering System and their relevant Runtime data should be synchronized.
4. Click "Download".

**Note**

**Runtime is stopped during a complete download**

The project running in runtime is stopped when a project is executed in runtime while you are completely downloading the project.

> **Note**
>
> To prevent the users created in the user management from being overwritten in runtime by the complete download of the project, activate the "Keep current user administration data in runtime" option.

##### Result

The project with the Runtime add-ons it contains is downloaded to the selected HMI devices.

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

On completion of the successful download of the project, you can execute it on the HMI device.

> **Note**
>
> **No data loss when loading is interrupted**
>
> Existing data on the HMI device is only deleted when the transfer is complete.

---

**See also**

[Updating the operating system of the HMI device (RT Unified)](#updating-the-operating-system-of-the-hmi-device-rt-unified)
  
[Error messages during loading of projects (RT Unified)](#error-messages-during-loading-of-projects-rt-unified)
  
[Basics for downloading projects (RT Unified)](#basics-for-downloading-projects-rt-unified)

#### Download changes only (RT Unified)

##### Introduction

When you only download changes to a project, the relevant project must be executed in runtime. Runtime is not closed when loading.

##### Requirement

- The project has been compiled without errors.
- The project has been downloaded at least once before.
- A compilation of changes must be possible or have been executed.
- The project was changed.
- The project that contains the changes is being executed in runtime.

##### Procedure

1. Select the HMI device in the project tree.
2. Select "Download to device" in the toolbar.

   Alternatively, select "Download to device > Software (only changes)" from the shortcut menu.

   The compilation of the project is checked and content that has not been compiled is compiled.

   The compilation result is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed.
3. Click "Download".

##### Result

The project with the Runtime add-ons it contains is downloaded to the selected HMI devices.

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

Runtime continues to be executed.

> **Note**
>
> **No data loss when loading is interrupted**
>
> Existing data on the HMI device is only deleted when the transfer is complete.

---

**See also**

[Basics for downloading projects (RT Unified)](#basics-for-downloading-projects-rt-unified)
  
[Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)

#### Loading projects of multiple HMI devices simultaneously (RT Unified)

##### Requirement

- Multiple HMI devices are configured.
- The individual projects have been compiled without errors.
- A user is configured.
- The HMI devices are connected to the configuration PC.
- The Control Panel has started on the Unified Comfort Panels.
- The protocol by which the project is loaded is set on the Unified Comfort Panel in the Control Panel under "Settings".
- "Automatic" or "Manual" is set as the transfer mode on the Unified Comfort Panels.

##### Connecting HMI devices to the configuration PC

1. Select an HMI device in the project tree.
2. Select "Online > Extended download to device".

   The "Extended download" dialog opens.
3. Configure the interface. Make sure that the settings match the transfer settings in the HMI device:

   - Select the protocol used, for example, Ethernet.
   - Configure the relevant interface parameters on the configuration PC.
   - Make any interface-specific or protocol-specific settings required on the HMI device.
4. Click "Connect".

   The connection is established and a dialog is displayed.
5. To connect additional HMI devices and load several projects at the same time, select "Cancel".
6. Repeat steps 1 to 5 for additional HMI devices.

##### Loading projects

1. Select the HMI devices using multiple selection in the project tree.
2. To download the changes to the projects, select the "Load" button in the toolbar.

   Alternatively, select "Download to device > Software (only changes)" from the shortcut menu.
3. To download the projects completely, select "Download to device" > "Software (all)" from the shortcut menu.

   The compilation of the projects is checked and content that has not been compiled is compiled.

   The result of the compilations is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed. All selected projects are listed in the dialog.
4. Check the displayed default settings and adjust the settings for each device:

   - Specify whether runtime should start on the target system after the download.
   - Specify whether tag values, active alarms, and user data are retained.

     Only available if you have selected "Start runtime".
   - Specify whether all logs are reset in runtime.

     Only available if you have selected "Start runtime".
5. Click "Download".

**Note**

**Runtime is stopped during a complete download**

The project running in runtime is stopped when a project is executed in runtime while you are completely downloading the project.

---

**See also**

[Initial download of a project (RT Unified)](#initial-download-of-a-project-rt-unified)
  
[Basics for downloading projects (RT Unified)](#basics-for-downloading-projects-rt-unified)

#### Using external storage medium (RT Unified)

##### Introduction

If you cannot establish a direct connection from the configuration PC to the HMI device, load the compiled runtime project onto an external storage medium. For example, use a USB flash drive or SD card.

As soon as you have connected the external storage medium to your HMI device, transfer the project to the HMI device.

##### Requirement

- An HMI device has been created.
- The project has been compiled without errors.

##### Loading project to external storage medium

1. Jump to the "Devices" tab in the project tree.
2. Double-click on
3. "Add user-defined card reader" in the "Card reader/USB storage" folder.

   A selection dialog opens.
4. Select a target directory to save the project.
5. Drag and drop the folder of the HMI device (e.g. "HMI_1 [<Device type>]") to the added folder.

   Alternatively, use copy and paste.

   The project is checked. If the project has contents that have not yet been compiled, a compile is performed.

   The "Load Preview" dialog opens.
6. Select the options for loading.
7. Click "Load" to confirm.

##### Result

Your project is stored as a compressed ZIP folder in the directory "[<Target directory>]\Simatic.HMI\RT_Projects". The file name is made up of the name of the HMI device, the project name and the time stamp, for example "HMI_RT_1[Project1] - Full 2020-04-03 - 14.51.41.zip".

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

You can find information about loading the project from the external storage medium to the Unified Comfort Panel in the operating instructions for the Unified Comfort Panel.

### Compiling and loading with team engineering (RT Unified)

This section contains information on the following topics:

- [Compiling and loading with team engineering (overview) (RT Unified)](#compiling-and-loading-with-team-engineering-overview-rt-unified)
- [Compiling in the server project view (RT Unified)](#compiling-in-the-server-project-view-rt-unified)

#### Compiling and loading with team engineering (overview) (RT Unified)

##### Introduction

You can compile and download to an HMI device in the server project view, in the exclusive session and the local session.

> **Note**
>
> **Unified objects cannot be selected in a local session**
>
> To edit an object using Multiuser Engineering, it must first be "selected". Only objects marked for check-in can be transferred into the server project after editing.
>
> Unified objects cannot be marked in a local session. Changes to these objects are not applied to the server project during check-in.
>
> You can edit unmarked objects in the server project view.

##### Basics

The options for compiling and downloading in the server project view, in the exclusive session or the local session are no different from the options in a single-user project. The most recent project is always compiled or loaded from the currently active view.

In principle, you can execute all commands for compiling and downloading in multiuser engineering and exclusive engineering:

- "Software (rebuild all)"
- "Compile > Software (only changes)"
- "Software (all)"
- "Download to device > Software (only changes)"

##### Rules

The following rules apply to compiling and downloading in multiuser engineering and exclusive engineering:

- The project that was changed in a local session always remains local and is not uploaded to the multiuser server.

  > **Note**
  >
  > A Unified project that was created or changed in a local session cannot be saved in the multiuser server project.
  >
  > Use the local session to test your configuration. When you update your local session, all changes to Unified objects are overwritten by the server project.
- Only projects that were created or changed in the server project view or in the exclusive session can be saved in the multiuser server project.

---

**See also**

[Compiling in the server project view (RT Unified)](#compiling-in-the-server-project-view-rt-unified)
  
[Downloading projects (RT Unified)](#downloading-projects-rt-unified)

#### Compiling in the server project view (RT Unified)

##### Basics

Compiling and downloading of projects in the server project view and the exclusive session is no different from compiling and downloading in a single-user project.

While you are compiling a project in the server project view or the exclusive session, the server project is blocked. Other users cannot edit the server project in the meantime. The compiled runtime project is saved with the WinCC project on the central server. Blocking the server project ensures that the configuration data and the runtime project remain synchronized.

> **Note**
>
> When you compile and save in the server project view or in the exclusive session, other users then obtain the Runtime project you have updated along with the WinCC project when they "refresh" their local session. Other users do not have to recompile the changes you have made after an update.

---

**See also**

[Compiling and loading with team engineering (overview) (RT Unified)](#compiling-and-loading-with-team-engineering-overview-rt-unified)

### Error messages during loading of projects (RT Unified)

#### Possible problems during the download

When a project is being downloaded to the HMI device, status messages regarding the download progress are displayed in the output window.

Problems arising during the download of the project to the HMI device are usually caused by one of the following errors:

- Wrong version of operating system on the HMI device
- Incorrect settings for downloading to the HMI device
- Incorrect HMI device type in the project
- The HMI device is not connected to the configuration PC.

Download failures and possible causes and remedies are listed below.

#### The download is canceled due to a compatibility conflict

| Possible cause | Remedy |
| --- | --- |
| Conflict between versions of the configuration software used and the operating system of the HMI device | - Synchronize the operating system of the HMI device with the version of the configuration software. - To update the operating system of the HMI device, select the command "Update operating system" in WinCC in the menu "Online > HMI device maintenance" or in the "Load preview" dialog.    You can also use ProSave.  For additional information, refer to the operating instructions for the HMI device. |
| The configuration PC is connected to a wrong device, e.g. a PLC. | - Check the cabling. - Correct the communication parameters. |

#### Project download fails

| Possible cause | Remedy |
| --- | --- |
| Connection to the HMI device cannot be established (alarm in the output window) | - Check the physical connection between the configuration PC and the HMI device. - Check that the HMI device is in transfer mode. Exception: Remote control |

#### The configuration is too complex

| Possible cause | Remedy |
| --- | --- |
| The configuration contains too many different objects or options for the HMI device selected. | - Reduce the project size. |

---

**See also**

[Reducing the project size (RT Unified)](#reducing-the-project-size-rt-unified)

### Starting runtime (RT Unified)

#### Introduction

You can start the project in runtime as soon as you have downloaded the project to the HMI device. By default, the project is started automatically on the HMI device.

The project settings defined in the "Runtime settings" of the HMI device are activated when the project is started in runtime.

> **Note**
>
> **Response of runtime when the HMI device is restarted**
>
> When the HMI device is restarted, the project is automatically restarted even if the project was stopped before the restart.

> **Note**
>
> **Closing Runtime automatically**
>
> If the transfer is activated on the HMI device and a transfer is started on the configuration PC, the running project is automatically terminated.
>
> The HMI device then automatically switches to "Transfer" mode.
>
> After the commissioning phase, disable the transfer so that the HMI device does not inadvertently switch to the "Transfer" mode.
>
> "Transfer" mode can trigger unwanted reactions in the plant.
>
> To restrict access to the transfer settings and thus avoid unauthorized changes, enter a password for access to the Control Panel.

#### Requirement

- The project has been downloaded to the HMI device.
- The Control Panel has been started.

#### Starting runtime on an HMI device

The Control Panel is displayed when the HMI device is switched on. Depending on the configuration, the loaded project starts automatically after the defined delay time.

If the project does not start automatically, click "Start" in the Control Panel.

Refer to the documentation for the HMI device for additional information on startup of projects.

#### Result

Runtime is started on the HMI device.

### Reducing the project size (RT Unified)

#### Introduction

When loading a large project to an HMI device, the HMI device may not have enough memory for the project.

#### Options for reducing the project size

There are several ways to reduce the size of the project and save space:

- Reduce the number of available runtime languages

  Check if all selected runtime languages are needed.

  If necessary, you can disable the languages that you do not need under "Runtime settings > Language & Font > Runtime language and font selection".
- "Software (rebuild all)"

  In order to optimize the project data and to clean up obsolete changes, compile the entire project using the "Compile > Software (rebuild all)" command from the shortcut menu of the HMI device.
- Reduce the number of fonts loaded

  Check if the number of user-defined downloaded fonts can be minimized.

  To save memory space, use fewer font groups for the configuration.
- Reduce the size of the graphics

  High-resolution graphic objects require a lot of memory and cause long loading times. They also reduce performance in Runtime.

  Check the size of the graphics that you use in the project. If necessary, reduce the size of the graphics by reducing the resolution or choose a higher compression format without noticeable loss of quality for the project graphics. Note the display resolution of the target device and the size in which the graphic object is displayed on the display of the target device.

  Select appropriate graphic formats for your screens: Use PNG images for drawings that are not vector graphics and JPEG images for photos.

---

**See also**

[Complete reloading of a project (RT Unified)](#complete-reloading-of-a-project-rt-unified)

### Maintenance of the HMI device (RT Unified)

This section contains information on the following topics:

- [Overview of the service for Unified Comfort Panels (RT Unified)](#overview-of-the-service-for-unified-comfort-panels-rt-unified)
- [ProSave (RT Unified)](#prosave-rt-unified)
- [Data backup of the HMI device (RT Unified)](#data-backup-of-the-hmi-device-rt-unified)
- [Backing up and restoring data of the HMI device (RT Unified)](#backing-up-and-restoring-data-of-the-hmi-device-rt-unified)
- [Updating the operating system (RT Unified)](#updating-the-operating-system-rt-unified)
- [Updating the operating system of the HMI device (RT Unified)](#updating-the-operating-system-of-the-hmi-device-rt-unified)
- [Updating the operating system of the HMI device from a data storage medium](#updating-the-operating-system-of-the-hmi-device-from-a-data-storage-medium)

#### Overview of the service for Unified Comfort Panels (RT Unified)

##### Structure

The following figure shows the software components of an HMI device and their relation to the engineering system.

![Structure](images/139314680587_DV_resource.Stream@PNG-en-US.png)

##### Logging data

Tags and alarms can be saved to logs. The log databases are stored on an external storage medium.

##### Runtime values

The runtime data is created during operation of the plant and stored on the HMI device. This data includes, for example, parameter sets and data for the user administration.

##### Runtime project

The runtime project contains the compiled configuration data for an HMI device.

##### Operating system and runtime software

The operating system of the HMI device is provided together with the runtime software in the form of an HMI device image. Suitable HMI device images are supplied with each WinCC version. Depending on the configuration, download the appropriate image along with the runtime project to the HMI device as required.

##### Firmware and hardware

The HMI device is delivered with preconfigured firmware and hardware.

#### ProSave (RT Unified)

##### Introduction

The "ProSave" service tool is included in the WinCC installation. The ProSave functions are accessed in WinCC with the menu "Online > HMI Device maintenance".

##### Functional scope

ProSave offers numerous functions for data transfer between the configuration PC and HMI device:

- Backing up and restoring data of the HMI device
- Updating the operating system of the HMI device
- Communication settings (transferred from WinCC)

---

**See also**

[Data backup of the HMI device (RT Unified)](#data-backup-of-the-hmi-device-rt-unified)
  
[Backing up and restoring data of the HMI device (RT Unified)](#backing-up-and-restoring-data-of-the-hmi-device-rt-unified)
  
[Updating the operating system (RT Unified)](#updating-the-operating-system-rt-unified)
  
[Updating the operating system of the HMI device (RT Unified)](#updating-the-operating-system-of-the-hmi-device-rt-unified)

#### Data backup of the HMI device (RT Unified)

##### Introduction

Data backup is used to create a backup of the data on the HMI device, e.g. before the update of the operating system. You can restore the backed-up data at a later time.

If an HMI device is connected to the configuration PC, you can back up and restore the data of the HMI device from the configuration PC using WinCC.

Alternatively, you can back up the data to an external storage medium supported by the HMI device. If the HMI device is networked, you can also back up the data to a server.

##### Scope of data backup

You have the option of performing a complete backup.

The following components are saved with this:

- Runtime
- Firmware
- Operating system
- Configuration
- Parameter sets
- User management
- Options

A backup includes several files. The master file has the extension ".brf". The number of additional files is variable, these files have the file name of the master file and a consecutive number (".0", ".1", ".2", ...) as extension.

> **Note**
>
> **Scope of data backup**
>
> The selected content of the flash memory is saved during data backup. Alarm logs and data logs are stored on the external storage medium and are therefore not saved using the "Save" function. If necessary, back up the contents of the memory card separately.
>
> Note the following for a complete backup and restore of the dataset:
>
> - A full backup includes all options installed. All data of the option that are still present after "Power off" are saved.
> - If the data is completely restored, all data previously on the device, including the operating system, will be irrevocably deleted.
> - If the recovery process cannot be completed due to a power failure or an interrupted data connection, for example, the HMI device starts in maintenance mode and must be reset to factory settings.
>
> Use an interface with high bandwidth, such as Ethernet, to back up and restore data via WinCC.

---

**See also**

[ProSave (RT Unified)](#prosave-rt-unified)
  
[Backing up and restoring data of the HMI device (RT Unified)](#backing-up-and-restoring-data-of-the-hmi-device-rt-unified)

#### Backing up and restoring data of the HMI device (RT Unified)

> **Note**
>
> Use the restore function for project data only on HMI devices which were configured using the same configuration software.

##### Requirement

- The HMI device is connected to the configuration PC.
- The HMI device is selected in the project tree.
- If a server is used for data backup: The configuration PC has access to the server.

##### Backing up data of the HMI device

To back up the HMI device data, follow these steps:

1. Select "Online > HMI device maintenance > Save" in the menu.

   The "Create backup" dialog box opens.
2. Select the type of the PG/PC interface and the target device, and click "Create".

   The "SIMATIC ProSave" dialog box opens.
3. Under "Data type", select the data to backup for the HMI device.
4. Enter the name of the backup file under "Save as".
5. Click "Start Backup".

This starts the data backup. The backup operation takes some time, depending on the connection selected.

##### Restoring data of the HMI device

To restore the data of the HMI device, follow these steps:

1. Select "Online > HMI device maintenance > Restore" in the menu.

   The "Restore backup" dialog box opens.
2. Select the type of the PG/PC interface and the target device, and click "Load".

   The "SIMATIC ProSave" dialog box opens.
3. Enter the name of the backup file under "Open...".

   Information about the selected backup file is displayed under "File information".
4. Click "Start Restore".

This starts the restoration. This operation takes some time, depending on the connection selected.

##### Backup/restore from the "Backup/Restore" dialog in the Control Panel of the HMI device

The "Backup / Restore" function is enabled for SD memory cards and USB memory media.

For more information, refer to the operating instructions of the HMI device.

---

**See also**

[ProSave (RT Unified)](#prosave-rt-unified)
  
[Data backup of the HMI device (RT Unified)](#data-backup-of-the-hmi-device-rt-unified)

#### Updating the operating system (RT Unified)

##### Introduction

If the image of an HMI device has a version status that does not match the configuration, update the image of the HMI device. The version of the image matches the installed Runtime version.

Update the operating system and the runtime software of the HMI device using the installed Runtime version. Depending on the protocol used, you may be prompted to run an automatic update of the installed Runtime version while loading the project.

Loading will then continue.

##### Update of the installed Runtime version

To update the installed Runtime version, connect the HMI device to the configuration PC. If possible, use the interface providing the highest bandwidth for this connection, e.g. Ethernet.

---

**See also**

[ProSave (RT Unified)](#prosave-rt-unified)
  
[Updating the operating system of the HMI device (RT Unified)](#updating-the-operating-system-of-the-hmi-device-rt-unified)

#### Updating the operating system of the HMI device (RT Unified)

If possible, use the interface providing the highest bandwidth for this connection, e.g. Ethernet. When you update the operating system, the runtime software on the HMI device is also updated and the installed Runtime version is changed.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Updating the operating system deletes all data on the HMI device**  When you update the operating system you delete data on the target system. For this reason, you should back up the following data beforehand:  - User management - Parameter sets - Project data |  |

##### Requirement

- The HMI device is connected to the configuration PC.
- The HMI device is selected in the project tree.

##### Updating the operating system

Proceed as follows to update the operating system:

1. Select "Online > HMI device maintenance > Update operating system" in the menu.

   The "Update operating system" dialog box opens.
2. Select the type of the PG/PC interface and the target device, and click "Update".

   The "SIMATIC ProSave [OS-Update]" dialog opens. The path to the image is preset.
3. If required, you can select a different path for the image that you want to transfer to the HMI device.
4. Click "Update OS".

This starts the update. The update operation can take time, depending on the connection selected.

##### Resetting the HMI device to factory settings

To reset the HMI device to factory settings, follow these steps:

1. Switch off the power supply for the HMI device.
2. Connect the HMI device to the configuration PC.
3. Select the "Update operating system" command from the menu under "Online > HMI Device maintenance" on the configuration PC in WinCC.

   The "Update operating system" dialog box opens.
4. Select the type of the PG/PC interface and the target device, and click "Update".

   The "SIMATIC ProSave [OS-Update]" dialog opens. The path to the image is preset.
5. If required, you can select a different path with a different image that you want to transfer to the HMI device.
6. Activate "Reset to factory settings".
7. Click "Update OS".
8. To reset to factory settings, switch on the power supply to the HMI device again.

   This operation can take time.

##### Result

The operating system of the HMI device is operational and up to date.

---

**See also**

[ProSave (RT Unified)](#prosave-rt-unified)
  
[Updating the operating system (RT Unified)](#updating-the-operating-system-rt-unified)
  
[Backing up and restoring data of the HMI device (RT Unified)](#backing-up-and-restoring-data-of-the-hmi-device-rt-unified)
  
[Basics for downloading projects (RT Unified)](#basics-for-downloading-projects-rt-unified)

#### Updating the operating system of the HMI device from a data storage medium

##### Introduction

You can update the operating system using a data storage medium. You can find the HMI device image files, for example, in the installation directory of WinCC under: "\Siemens\Automation\Portal V1x\Data\Hmi\Transfer\<HMI device image version>\Images".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data loss**  All data on the HMI device, including the project and HMI device password, is deleted during a restore operation.   Back up data before the restore operation. |  |

##### Requirement

- The HMI device image file is located in the "SIMATIC.HMI\Firmware\" directory on your data storage medium, e.g. a SIMATIC HMI Memory card or an industry-grade USB stick.
- The data storage medium with the relevant HMI devices image file including operating system is inserted in the HMI device.

##### Procedure

1. Open the Control Panel on the HMI device.
2. Select "Service & Commissioning > Update OS".
3. Select a storage medium under "Select storage media for OS update".
4. Select the required HMI device image file under "Firmware files on external storage".
5. Press "Update OS".

   The "Update OS Image" dialog opens.
6. To start restoring the operating system, press "Yes".

   The "Transfer" dialog opens. A progress bar shows the course of the restore. The HMI device then restarts.

**Note**

If there is no storage medium or a defective storage medium in the HMI device, the "0 devices found" alarm is displayed. Insert the storage medium or replace the storage medium.

> **Note**
>
> After the restore, it may be necessary to recalibrate the touch screen.

---

**See also**

[Updating the operating system of the HMI device (RT Unified)](#updating-the-operating-system-of-the-hmi-device-rt-unified)

## WinCC Unified PC (RT Unified)

This section contains information on the following topics:

- [Specifying runtime settings (RT Unified)](#specifying-runtime-settings-rt-unified-1)
- [Compiling a project (RT Unified)](#compiling-a-project-rt-unified-1)
- [Downloading projects (RT Unified)](#downloading-projects-rt-unified-1)
- [Compiling and loading with team engineering (RT Unified)](#compiling-and-loading-with-team-engineering-rt-unified-1)
- [Error messages during loading of projects (RT Unified)](#error-messages-during-loading-of-projects-rt-unified-1)
- [Starting and stopping runtime (RT Unified)](#starting-and-stopping-runtime-rt-unified)
- [Managing users in Runtime (RT Unified)](#managing-users-in-runtime-rt-unified)

### Specifying runtime settings (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-1)
- [General (RT Unified)](#general-rt-unified-2)
- [Alarms (RT Unified)](#alarms-rt-unified-1)
- [Process diagnostics (RT Unified)](#process-diagnostics-rt-unified)
- [Services (RT Unified)](#services-rt-unified-1)
- [Language & font (RT Unified)](#language-font-rt-unified-1)
- [Collaboration (RT Unified)](#collaboration-rt-unified-1)
- [Storage system (RT Unified)](#storage-system-rt-unified-1)
- [Settings for tags (RT Unified)](#settings-for-tags-rt-unified-1)
- [Good Manufacturing Practice (RT Unified)](#good-manufacturing-practice-rt-unified-1)
- [User management (RT Unified)](#user-management-rt-unified-1)
- [OPC UA server (RT Unified)](#opc-ua-server-rt-unified-1)
- [Layers (RT Unified)](#layers-rt-unified-1)
- [Reporting (Unified PC) (RT Unified)](#reporting-unified-pc-rt-unified)

#### Introduction (RT Unified)

Before you compile and download a project, update the runtime settings of the HMI device. You specify the Runtime languages, for example, or activate "Collaboration".

To edit the runtime settings for an HMI device, select "Runtime settings" in the project tree below the HMI device.

#### General (RT Unified)

##### Identification

The runtime ID is the unique identification of a runtime project. The runtime ID is also stored in the SIMATIC Runtime Manager. Based on the runtime ID, you can determine whether a project has already been downloaded to the HMI device.

> **Note**
>
> When you rename the WinCC Runtime of the Unified PC in the Engineering System, the Runtime ID changes. The project must be downloaded completely during the next download.

##### Encrypted transfer

To download the project encrypted, the same password must be stored in the runtime settings and in runtime. Alternatively, transfer the password unencrypted during the initial download.

When you manage an encrypted project in the Runtime Manager, the password must be stored in the Runtime Manager.

##### Screen

Under "Screen", you specify the start screen and the style of the HMI device.

The start screen is displayed after runtime start.

Select the screen resolution. The setting of the HMI device is used by default.

> **Note**
>
> **Display of a changed start screen**
>
> You have defined a start screen in the project and started runtime. When you define another start screen and download only changes to the device, the last active screen is displayed in runtime.
>
> After reloading, refresh runtime in the browser with the <F5> key or the "Update" button.

---

**See also**

[Secure communication (RT Unified)](#secure-communication-rt-unified)

#### Alarms (RT Unified)

##### Controller alarms and diagnostics

> **Note**
>
> WinCC only supports controller alarms of a SIMATIC S7-1500. In addition, WinCC only supports controller alarms that are automatically updated by the central alarm management in the PLC.

One or more HMI connections to a PLC are shown in "Controller alarms and diagnostics".

You can manage the following options:

- "Display classes": You filter the controller alarms via display classes. You specify for each connection which display classes are displayed on the HMI device.
- "Automatic update": Controller alarms are automatically updated on the HMI device.

  Requirement: The "Central message management in the PLC" option is enabled.
- "System diagnostics": System diagnostic alarms can be displayed in runtime.

  Requirement: The "Automatic update" option is enabled.
- "Security events": Security events can be displayed in runtime.

  Requirement: The "Automatic update" option is enabled.

##### State texts

You specify the state texts of alarms in the runtime settings. The state texts are displayed in runtime in the alarm control.

Specify the state texts in other languages under "Languages & Resources > Project texts".

---

**See also**

[Configuring the status texts of alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-status-texts-of-alarms-rt-unified)
  
[Configuring the display of system diagnostics alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-display-of-system-diagnostics-alarms-rt-unified)
  
[Configuring the display of security events (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-display-of-security-events-rt-unified)
  
[Filtering PLCs alarm using display classes (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#filtering-plcs-alarm-using-display-classes-rt-unified)

#### Process diagnostics (RT Unified)

##### General

Indicates whether the device participates in process diagnosis.

#### Services (RT Unified)

##### SMTP communication

SMTP communication enables automatic sending of e-mails when events occur.

Specify the port for SMTP communication.

#### Language & font (RT Unified)

##### Runtime language and font selection

You configure project languages that are available as runtime languages for the respective device. You also define the order in which the languages are switched.

When using central user management, runtime is displayed in the language that a user selected in the "User login" dialog during login. If this language is not configured in the runtime settings of the HMI device or if the language setting in the central user management was not set, runtime is displayed in the language that has the lowest number in the "Order" column in the runtime settings. You change the order with ![Runtime language and font selection](images/134928713995_DV_resource.Stream@PNG-de-DE.png).

If users do not select a language in the "User login" dialog, runtime is displayed in the language that is set for the browser.

The fixed font 1 is always provided for the respective HMI device.

When you enable the option "Enable for logging" for a language, alarm texts are logged in the respective language. To keep the size of the log relatively small, log only alarm texts in the required languages.

---

**See also**

[Enabling the runtime language (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#enabling-the-runtime-language-rt-unified)
  
[Editing log contents with scripts and system functions (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#editing-log-contents-with-scripts-and-system-functions-rt-unified)

#### Collaboration (RT Unified)

##### General settings

- Select the "Enable collaboration" check box.

##### Identification

The following information must be unique for all devices participating in a collaboration:

- System ID:

  The system ID must be unique for each device participating in Unified Collaboration, as this ID is used for communication between the devices.
- Collaboration name:

  Assign a collaboration name or select "Generate collaboration name automatically".
- IP address / Host name

##### Connect actively to

A list of all HMI devices available for collaboration with system ID and IP address / host name is displayed. You select the HMI devices to which the current HMI device provides collaboration.

> **Note**
>
> **Collaboration is enabled in both directions**
>
> The HMI device that you select under "Connect actively to" can display screens of the current HMI device and vice versa. Collaboration is always enabled in both directions, even if you only have the connection activated for one collaboration device.

---

**See also**

[Defining collaboration settings (RT Unified)](Using%20distributed%20systems%20%28RT%20Unified%29.md#defining-collaboration-settings-rt-unified)

#### Storage system (RT Unified)

You specify the storage locations of the following databases:

- Database for tag persistency
- Database for data logging
- Database for alarm logging

> **Note**
>
> **Logging on network drives**
>
> Do not save databases directly on a network drive. Power supply can be interrupted at any time. Reliable operation is therefore not guaranteed.
>
> For example, save the logs on your local hard drive or a USB stick.

If you have defined a storage location in the runtime settings of the HMI device, you can specify the database storage location for individual logs in the "Logs" editor under "Storage medium". You have the following options:

- Default:

  The database is saved according to the runtime settings of the HMI device.
- Local:

  Specify a path.

##### Restriction

If the Runtime project folder is configured as the storage location for a database and you change the storage location of the project folder, this leads to a loss of data.

To avoid data loss, select a storage location for databases that is not the project folder, or do not change the project folder.

##### Database type

Specify the database type. WinCC Unified PC supports the following database types:

- SQLite
- Microsoft SQL

  A separate installation is required for using Microsoft SQL. After installing Microsoft SQL, SQLite logging is no longer possible.

##### Database storage location for tag persistency

You can specify tag persistency for internal tags. The last values of the persistent tags are used after Runtime has been started.

A separate database is used for tag persistency. The values of the tags are available again after restarting runtime or restarting or switching off the HMI device.

Specify the storage location of the database:

- Off:

  Tag persistency is not used.
- Local:

  Specify a path.
- Project folder:

  The database is stored in a subfolder of the runtime project folder.

> **Note**
>
> Use different storage media for tag persistency and logging.

The tag persistency can be affected if the log databases and the database for tag persistency are stored on the same storage medium and the storage medium is changed while runtime is running.

##### Location of the main database for data logging

Specify the storage location of the databases for data logging:

- Off:

  Tags are not logged.
- Local:

  Specify a path.
- Project folder:

  The logs are stored in the "TLGDB" subfolder of the runtime project folder.
- Default:

  In WinCC Unified Configuration you store the path at which the logs are saved under "Log settings".

##### Location of the main database for alarm logging

Specify the storage location of the databases for alarm logging:

- Off:

  Alarms are not logged.
- Local:

  Specify a path.
- Project folder:

  The logs are stored in the "ALGDB" subfolder of the runtime project folder.
- Default:

  In WinCC Unified Configuration you store the path at which the logs are saved under "Log settings".

---

**See also**

[Specify tag persistency (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#specify-tag-persistency-rt-unified)
  
[Storage locations of logs (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#storage-locations-of-logs-rt-unified)

#### Settings for tags (RT Unified)

You have the option of synchronizing HMI tags with the connected PLC tags. The position of a data value in the structure of a data block is thus mapped in the HMI tag name. If necessary, the PLC name is set as a prefix. You synchronize the tags in the "HMI tags" editor.

You specify before the synchronization whether the names are matched and under which conditions.

##### Synchronization of the name of the PLC tag in the engineering station

To avoid conflicts within complex tag types, configure how the delimiters of the path statement from STEP 7 are replaced in WinCC similar to name matching:

- Replace delimiters

  Depending on your selection, the delimiters of all hierarchy levels are replaced during synchronization.
- Replace invalid characters
- PLC prefix

  The PLC name is set as a prefix to the HMI tag name. You set the option for each HMI connection.

> **Note**
>
> **Duplicate tag names**
>
> If the generated tag name is already in use, a number is added in parentheses, e.g. Datablock_1_Static_2{1}(1).

##### Example

The "PLC1" controller contains the structured data block "DB1". The "Db1.a[1].b.c[3]" data block element is used in a picture. Depending on your settings, the HMI tag name is generated as follows:

| Selected option | HMI tag name |
| --- | --- |
| PLC prefix | Plc1.Db1.a[1].b.c[3] |
| Replace dot and parenthesis with ; ( ) | Db1;a(1);b;c(3) |
| Replace dot and parenthesis with _ { }  PLC prefix | Plc1_Db1_a{10}_b_c{3} |

---

**See also**

[Synchronizing tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#synchronizing-tags-rt-unified)

#### Good Manufacturing Practice (RT Unified)

Traceability and therefore the documentation of production data is becoming increasingly important in many sectors such as the pharmaceutical industry, the food and beverage industry, and the related mechanical engineering industry.

Therefore, sector-specific and cross-industry standards have been developed for the electronic documentation of production data.

The most important set of regulations is the FDA guideline 21 CFR Part 11 for electronic data records and electronic signatures issued by the FDA, the US Food and Drug Administration. In addition, different EU regulations apply, such as EU 178/2002, depending on the industry.

Requirements for production systems in these industries have been developed on the basis of 21 CFR Part 11 and the corresponding layout to comply with GMP (Good Manufacturing Practice). They are also required for other industries.

The following main requirements are derived from these directives and regulations:

- Creation of an Audit Trail or operating trace in runtime

  Based on this document, it is possible to trace the user who carried out the operator action on the machine at what time.
- Important process steps must also be assigned to a clear responsibility, for example, via an electronic signature.

##### GMP (Good Manufacturing Practice)

1. Enable GMP-compliant configuration.
2. If necessary, select a text list entry that contains the reason for the GMP-relevant tags.

#### User management (RT Unified)

You specify whether you are using a local or a central user management. By default, the use of the local user management is specified in the engineering system.

Local users are only valid for this project.

You manage central users in the TIA User Management Component (UMC).

##### Configuration of user management

- When you activate the local user management, you use the users and user roles that you have created under "Security settings > Users and roles" for management.
- When you activate the central user management, the users, user roles and their rights are applied from the TIA User Management Component (UMC). To access the UMC, you must specify the server address and the server ID.

---

**See also**

[Central user management (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#central-user-management-rt-unified)

#### OPC UA server (RT Unified)

This section contains information on the following topics:

- [General (RT Unified)](#general-rt-unified-3)
- [Options (RT Unified)](#options-rt-unified-1)
- [Security (RT Unified)](#security-rt-unified-1)

##### General (RT Unified)

OPC is a standardized manufacturer-independent software interface for data exchange in automation engineering. OPC UA is the technology succeeding OPC. OPC UA is platform-independent and supports different protocols as communication medium.

To work with OPC UA in WinCC Unified, the OPC UA server must be enabled in the TIA Portal in the Runtime settings of the HMI device.

###### Read/write tags and register tags/alarms

When you enable the "Operate as OPC UA server" option in the HMI device, the protection for unauthorized internal and external access is downgraded.

- Enable the "Operate as OPC UA server" option.

  A security note is displayed.

After enabling the option, all other settings of the OPC UA Server will become available.

###### Alarms and Conditions

- To display alarm conditions in the address range of the server, select the option "Enable Alarms and Conditions on the OPC UA server".
- To disable or acknowledge alarms on the OPC UA Client, for example, select the option "Allow operation of alarms on the OPC UA Client". To enable this option, the "Enable Alarms and Conditions on the OPC UA server" option must be enabled.

##### Options (RT Unified)

###### General

Define the following settings:

- Port

  Default value: 4890

  Do not use a port number that is already assigned to another application.
- Maximum session timeout (s)

  Default value: 600000 s
- Maximum number of OPC UA sessions

  Default value: 100

###### Subscriptions

Define the following settings:

- Minimum publication interval (ms)

  Default value: 100 ms
- Maximum number of monitored items

  Default value: 0

##### Security (RT Unified)

This section contains information on the following topics:

- [Secure connection (RT Unified)](#secure-connection-rt-unified-1)
- [User authentication (RT Unified)](#user-authentication-rt-unified-1)

###### Secure connection (RT Unified)

###### Security policies

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Reduced security**  When the option "No OPC UA Server Security" is enabled, any OPC UA client can connect to the OPC UA server regardless of the following settings. |  |

The following section contains a list of all security policies available on the server.

- Activate the required security policies.

###### User authentication (RT Unified)

###### Guest authentication

- To allow access by anonymous users to the OPC UA server, enable the option "Enable guest authentication".

  An authentication by means of user name and password is not required for guests.

  Security is restricted to the degree that you determine by assigning rights to this user.

###### Authentication by means of user name and password

- To allow access by users with user name and password to the OPC UA server, enable the option "Authentication with user name and password".

  If access to the OPC UA server is to require the user name and password, the user must be assigned the role "HMI Administrator". The "HMI Administrator" role has the system-defined "OPC UA - read and write access" function right. The settings made must then be synchronized with the user management in runtime.

#### Layers (RT Unified)

##### Default names of the layers

Adjust the default names of the layers.

#### Reporting (Unified PC) (RT Unified)

##### Report system

Make the reporting settings of the HMI device here:

|  |  |  |
| --- | --- | --- |
| "Enable Reporting" | Enables Reporting.  You can create report templates based on this project or project report jobs and generate reports in Runtime only if reporting is enabled. |  |
| "Storage location for the Reporting database" | Configure the storage location of the Reporting database.  The Reporting database stores the actions and settings made in Runtime in the "Reports" control. |  |
| "Storage location" | "Default"  The database is in the folder that is selected during installation or later in the "Reporting" step in WinCC Unified Configuration. |  |
| "Project folder"  The database is in the project folder of the Runtime project. |  |  |
| "Local"  The database is in the device folder you entered under "Folder". |  |  |
| "Folder" | If you have selected the value "Local" under "Storage location", enter the path to the local folder here. |  |
| "Storage location for reports" | Configure the local main storage location for the generated reports.  In Runtime, the local main storage location is one of the possible storage locations for reports with the "File system" target type. |  |
| "Storage location" | "Default"  The folder defined during installation or later in WinCC Unified Configuration in "Reporting" step is used as the main local storage location. |  |
| "Project folder"  The project folder of the Runtime project is used as the main local storage location. |  |  |
| "Local"  The device folder you entered under "Folder" is used as the main local storage location. |  |  |
| "Folder" | If you have selected the value "Local" under "Storage location", enter the path to the local folder here. |  |

> **Note**
>
> **Devices with a device version lower than V18**
>
> Unified PCs with a device version of lower than V18 always have the same settings:
>
> - Reporting is always enabled.
> - The folder configured during the installation of Unified Runtime or later with WinCC Unified Configuration is always used as local main storage location for reports.
> - The Reporting database is always in the project folder.

### Compiling a project (RT Unified)

#### Basics

Compilation results in a runtime project that is executable on the respective HMI device.

A project can be compiled explicitly or implicitly:

- Explicit: The compilation is started manually. Compile the entire project or only changes.

  Explicit compiling is described in the following section.
- Implicit: The project is downloaded without previous manual compilation.

  The project is compiled in the background even as you are configuring it in WinCC.

  This reduces the compilation times before downloading the project.

> **Note**
>
> Changes to S7 blocks are not automatically compiled in the background. If you are using HMI tags in the project that are connected to PLC tags, you should also compile all changed S7 blocks before you compile the HMI device.

#### Requirement

- A project is open.

#### Compiling changes of a project

1. Select an HMI device in the project tree.
2. There are two ways to start compiling the changes:

   - Press the "Compile" button in the toolbar.
   - Select "Compile > Software (only changes)" from the shortcut menu.

#### Compiling a project completely

1. Select an HMI device in the "Project tree" area.
2. Select "Compile > Software (rebuild all)" from the shortcut menu.

> **Note**
>
> When a project was compiled completely, the project must also be downloaded completely afterward.

#### Compiling projects of multiple HMI devices simultaneously

1. Select the HMI devices using multiple selection in the project tree.
2. To compile the changes to the projects, select the "Compile" button in the toolbar.

   Alternatively, select "Download to device > Software (only changes)" from the shortcut menu.
3. To compile the projects completely, select "Download to device" > "Software (rebuild all)" from the shortcut menu.

#### Result

The configuration data of the selected HMI devices is being compiled.

If errors occur during compilation, the errors are shown in the Inspector window under "Info > Compile".

1. Correct the errors and recompile the projects.
2. Load the compiled projects.

---

**See also**

[Overview (RT Unified)](#overview-rt-unified)
  
[Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)
  
[Complete reloading of a project (RT Unified)](#complete-reloading-of-a-project-rt-unified-1)
  
[Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)

### Downloading projects (RT Unified)

This section contains information on the following topics:

- [Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)
- [Initial download of a project (RT Unified)](#initial-download-of-a-project-rt-unified-1)
- [Complete reloading of a project (RT Unified)](#complete-reloading-of-a-project-rt-unified-1)
- [Download changes only (RT Unified)](#download-changes-only-rt-unified-1)
- [Loading projects of multiple HMI devices simultaneously (RT Unified)](#loading-projects-of-multiple-hmi-devices-simultaneously-rt-unified-1)
- [Using external storage medium (RT Unified)](#using-external-storage-medium-rt-unified-1)

#### Basics of downloading projects (RT Unified)

##### Introduction

During downloading, the compiled project is transferred to an HMI device. The project can be downloaded either locally to the Unified Runtime of the configuration PC or a connected HMI device. If there is no connection, an external storage medium can be used for the transfer.

Before the download, use the "Load preview" dialog to determine whether existing data is retained and whether logs are reset. The following data can be retained or overwritten:

- Runtime values: Tag values, active alarms and user data
- Logs: Data logs, alarm logs, Audit Trails and context logs

The compilation of the project is checked before downloading and missing content is compiled. This ensures that the latest version of the project is always downloaded.

When you download a project again, you can decide whether you want to download only changes or the complete project. If you want to download only changes, a compilation of changes must be possible beforehand.

##### Ethernet connection

You download the project to the HMI device via an Ethernet connection. The connection uses Ethernet port 20008.

> **Note**
>
> **Ethernet port 20008**
>
> If an application already occupies Ethernet port 20008, loading is not possible.
>
> If no connection to the target can be established, check the port assignments. If another application is using Ethernet port 20008, close this application.

##### Runtime ID

At the start of the configuration, each project receives a runtime ID which is transferred to the HMI device during downloading. If you have already downloaded a project, the download process recognizes the project using the Runtime ID. When you rename the WinCC Runtime of the Unified PC, the Runtime ID changes as well.

> **Note**
>
> **Existing runtime projects on the target HMI device**
>
> If a runtime project with the same Runtime ID is already available on the HMI device, the project is overwritten.

##### Synchronization of IDs:

In runtime, objects and their relevant Runtime data are identified by IDs. If the Engineering data and Runtime data are not synchronized, conflicts may arise, which may lead to undesired reactions at runtime. This is the case, if, for example:

- the Engineering process is not linear, i.e. an earlier project version is enhanced with new objects and loaded to the device that is already running with a newer project version, for example, when using a backup or if the project was not saved after loading.
- the process of compiling and loading a project gets aborted unexpectedly.
- the Runtime data are reset.

To detect and rectify such application cases, the dialog "Load Preview" contains setting options for synchronizing IDs.

> **Note**
>
> Synchronization is not necessary when downloading changes since the linearity has already been selected.

##### Downloading various runtime projects onto one HMI device

If the runtime software "WinCC Unified PC RT" is installed on the PC, you can download multiple projects directly to the configuration PC. But you are only executing one runtime project in runtime. You can use the SIMATIC Runtime Manager to start and stop projects.

Example: The "Mixing" project is loaded to the configuration PC and is being executed in runtime. When you change the "Mixing" project, download the changes using "Download to device > Software (only changes)". Runtime continues running.

When you then download the "Bottling" project completely, the "Mixing" project Runtime is stopped. If you have selected the "Start runtime" option, the "Bottling" project is started.

##### Downloading a runtime project to multiple HMI devices

You can download a runtime project to several connected HMI devices one after the other and start runtime at the same time. Changes can only be downloaded for the first device.

---

**See also**

[Complete reloading of a project (RT Unified)](#complete-reloading-of-a-project-rt-unified-1)
  
[Overview (RT Unified)](#overview-rt-unified)
  
[Compiling a project (RT Unified)](#compiling-a-project-rt-unified-1)
  
[Secure communication (RT Unified)](#secure-communication-rt-unified)
  
[Download changes only (RT Unified)](#download-changes-only-rt-unified-1)
  
[Loading projects of multiple HMI devices simultaneously (RT Unified)](#loading-projects-of-multiple-hmi-devices-simultaneously-rt-unified-1)
  
[Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)
  
[Using external storage medium (RT Unified)](#using-external-storage-medium-rt-unified-1)
  
[Compiling and loading with team engineering (RT Unified)](#compiling-and-loading-with-team-engineering-rt-unified-1)
  
[Basics on version compatibility (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#basics-on-version-compatibility-rt-unified-1)

#### Initial download of a project (RT Unified)

##### Introduction

The first download of a project is different from any subsequent download processes:

- The connection to the HMI device must be set up before the download.
- The project is always downloaded completely during the first download.

  > **Note**
  >
  > **Runtime is stopped during a complete download**
  >
  > The project running in runtime is stopped when a project is executed in runtime while you are completely downloading the project.

##### Requirement

- The project has been compiled without errors.
- A user is configured.
- The HMI device is connected to the configuration PC or the configuration PC is the HMI device.
- The Runtime version of the target device corresponds to the configured Runtime version.
- Ethernet port 20008 in the network configuration is not allocated.

##### Editing connection parameters before download

1. Select the HMI device in the project tree.
2. Select "Online > Extended download to device".

   The "Extended download" dialog opens.
3. Enter the IP address or device name of the new target device.
4. Click "Connect" and load the project.

   The Runtime project is downloaded with changed connection parameters.

##### Options when initially loading a project

**Runtime values: Tag values, active alarms and user data**

Select whether you want to keep the current values or reset the values to the start values.

Select "Reset to start values" at the time of initial loading.

**Reset logs: Data logs, alarm logs, Audit Trails and context logs**

Select whether you want to reset all logs or no log in Runtime.

**Synchronizing IDs**

Select whether the IDs of objects in the Engineering System and their relevant Runtime data should be synchronized.

> **Note**
>
> At the time of initial loading, the IDs of objects in the Engineering System and their relevant Runtime data are not synchronized, regardless of the selected option.

- Synchronize: The synchronization of IDs is verified before loading. If inconsistencies are reported during the verification of the IDs, the IDs are synchronized. Then the project is completely loaded.
- Verifying the synchronization: The synchronization of IDs is verified before loading. If inconsistencies are reported during the verification of the IDs, loading is cancelled. The IDs are then not synchronized.
- Do not Sync: Synchronization of the IDs is not verified. The system cannot guarantee that the data loaded from the Engineering System match the data present in Runtime.

  > **Note**
  >
  > **Restart Runtime**
  >
  > To prevent data inconsistencies, restart Runtime when you select "Do not Sync".

##### Initial loading of a project

1. Select the HMI device in the project tree.
2. In the toolbar, select the "Download to device" button or select "Download to device" > "Software (all)" from the shortcut menu.

   The "Extended download" dialog opens.
3. Enter the address or the name of the target device. You have the following options:

   - "Configured IP address"
   - "Use other IP address"
   - "Use device name (DNS)"

   If you use your configuration PC as an HMI device, enter the IP address 127.0.0.1 or the device name "localhost".
4. Click "Connect".

   The connection is established and a dialog is displayed.
5. Select "Load".

   The compilation of the project is checked and missing content is compiled.

   The compilation result is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed.
6. Check the displayed default settings and change the settings as necessary:

   - Select the "Full download" option under "Load Runtime".
   - Under "Runtime start", specify whether Runtime should start on the target system after the download.
   - Under "Runtime values", select "Reset to start values" in the Options menu.
   - Under "Reset logs", specify whether all logs are reset in Runtime.

     The setting is only accepted when you have selected "Start runtime".
7. Click "Download".

**Note**

When you select "Download to device" > "Software (only changes)" from the shortcut menu, the project is still downloaded completely during the initial download.

##### Result

The project is downloaded onto the selected HMI device under the file path "C:\ProgramData\SCADAProjects".

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

On completion of the successful download of the project, you can execute it on the HMI device. If you have activated the start of runtime on the target system in the "Load Preview" dialog, the project is started in runtime after loading.

---

**See also**

[Specify tag persistency (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#specify-tag-persistency-rt-unified)
  
[Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)
  
[Compiling a project (RT Unified)](#compiling-a-project-rt-unified-1)
  
[Secure communication (RT Unified)](#secure-communication-rt-unified)
  
[Overview (RT Unified)](#overview-rt-unified)
  
[Loading projects of multiple HMI devices simultaneously (RT Unified)](#loading-projects-of-multiple-hmi-devices-simultaneously-rt-unified-1)

#### Complete reloading of a project (RT Unified)

##### Options when reloading a project

Make the following settings in the "Load preview" dialog during reloading:

- Load Runtime: Full download

  You cannot download if you keep the "No action" option.
- Runtime start: Specify whether Runtime should start on the target system after the download.
- Runtime values: Select whether you want to keep the current values for tags, active alarms and user administration data or if you want to reset the values to the start values.

  With the "Keep selected" option, you can specify the values you want to keep.

  - Current values of tags and pending alarms
  - Current user administration data: Disable "Keep current user administration data in runtime" during initial download.
- Reset logs: Select whether you want to reset data logs, alarm logs, Audit Trails and context logs or no log in Runtime.
- Synchronize IDs: Specifies the process to be followed for synchronizing the IDs of objects in the Engineering System and their relevant Runtime data.

  The following options are available:

  - Synchronize: The synchronization of IDs is verified before loading. If inconsistencies are reported during the verification of the IDs, the IDs are synchronized. Then the project is completely loaded.
  - Verifying the synchronization: The synchronization of IDs is verified before loading. If inconsistencies are reported during the verification of the IDs, loading is cancelled. The IDs are then not synchronized.
  - Do not Sync: Synchronization of the IDs is not verified. The system cannot guarantee that the data loaded from the Engineering System match the data present in Runtime.

    > **Note**
    >
    > **Restart Runtime**
    >
    > To prevent data inconsistencies, restart Runtime when you select "Do not Sync".

##### Requirement

- The project has been compiled without errors.
- The project has been downloaded at least once before.

##### Procedure

1. Select the HMI device in the project tree.
2. Select "Download to device > Software (all)" from the shortcut menu.

   The compilation of the project is checked and content that has not been compiled is compiled.

   The compilation result is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed.
3. Check the displayed default settings and change the settings as necessary:

   - Select the "Full download" option under "Load Runtime".
   - Specify whether Runtime should start on the target system after the download.
   - Specify whether tag values, active alarms, and user data are retained.

     The setting is only accepted when you have selected "Start runtime".

     To retain internal tags, the persistency must be enabled in the settings of the respective tag.
   - Specify whether all logs are reset in runtime.

     The setting is only accepted when you have selected "Start runtime".
   - Select the desired option under "Synchronize IDs" in the selection menu.
4. Click "Download".

**Note**

**Runtime is stopped during a complete download**

The project running in runtime is stopped when a project is executed in runtime while you are completely downloading the project.

**Note**

To prevent the users created in the user administration from being overwritten in runtime by the complete download of the project, activate the "Keep current user administration data in runtime" option.

##### Result

The project is downloaded onto the selected HMI device under the file path "C:\ProgramData\SCADAProjects".

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

After the successful download of the runtime project, you can execute it. If you have activated the start of runtime on the target system in the "Load Preview" dialog, the project is started in runtime after loading.

---

**See also**

[Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)
  
[Overview (RT Unified)](#overview-rt-unified)
  
[Compiling a project (RT Unified)](#compiling-a-project-rt-unified-1)
  
[Specify tag persistency (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#specify-tag-persistency-rt-unified)
  
[Secure communication (RT Unified)](#secure-communication-rt-unified)

#### Download changes only (RT Unified)

##### Introduction

When you only download changes to a project, the relevant project must be executed in runtime. Runtime is not closed when loading.

##### Requirement

- The project has been compiled without errors.
- The project has been downloaded at least once before.
- A compilation of changes must be possible or have been executed.
- The project was changed.
- The project that contains the changes is being executed in runtime.

##### Procedure

1. Select the HMI device in the project tree.
2. Press the "Download to device" button in the toolbar.

   Alternatively, select "Download to device > Software (only changes)" from the shortcut menu.

   The compilation of the project is checked and content that has not been compiled is compiled.

   The compilation result is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed.
3. Click "Download".

##### Result

The changes are downloaded onto the selected HMI device under the file path "C:\ProgramData\SCADAProjects".

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

Runtime continues to be executed.

Update Runtime in the browser with the <F5> key or by pressing the "Update" button to see the changes in runtime.

---

**See also**

[Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)
  
[Restrictions in compiling and loading changes (RT Unified)](#restrictions-in-compiling-and-loading-changes-rt-unified)

#### Loading projects of multiple HMI devices simultaneously (RT Unified)

##### Requirement

- Several WinCC Unified PCs are configured.
- The individual projects have been compiled without errors.
- A user is configured.
- Ethernet port 20008 in the network configuration is not allocated.

##### Connecting WinCC Unified PCs to the configuration PC

1. Select a WinCC Unified PC in the project tree.
2. Select "Online > Extended download to device".

   The "Extended download" dialog opens.
3. Enter the address or the name of the target device. You have the following options:

   - "Configured IP address"
   - "Use other IP address"
   - "Use device name (DNS)"
4. Click "Connect".

   The connection is established and a dialog is displayed.
5. To connect additional HMI devices and load several projects at the same time, select "Cancel".
6. Repeat steps 1 to 5 for additional WinCC Unified PCs.

##### Loading projects

1. Select the WinCC Unified PCs using multiple selection in the project tree.
2. To download the changes to the projects, select the "Load" button in the toolbar.

   Alternatively, select "Download to device > Software (only changes)" from the shortcut menu.
3. To download the projects completely, select "Download to device" > "Software (all)" from the shortcut menu.

   The compilation of the projects is checked and content that has not been compiled is compiled.

   The result of the compilations is displayed in the Inspector window under "Info > Compile".

   The "Load Preview" dialog is displayed. All selected projects are listed in the dialog.
4. Check the displayed default settings and adjust the settings for each device:

   - Specify whether runtime should start on the target system after the download.
   - Specify whether tag values, active alarms, and user data are retained.

     The setting is only accepted when you have selected "Start runtime".
   - Specify whether all logs are reset in runtime.

     The setting is only accepted when you have selected "Start runtime".
5. Click "Download".

**Note**

**Runtime is stopped during a complete download**

The project running in runtime is stopped when a project is executed in runtime while you are completely downloading the project.

---

**See also**

[Initial download of a project (RT Unified)](#initial-download-of-a-project-rt-unified-1)
  
[Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)

#### Using external storage medium (RT Unified)

This section contains information on the following topics:

- [Loading project to external storage medium (RT Unified)](#loading-project-to-external-storage-medium-rt-unified)
- [Load project from external storage medium (RT Unified)](#load-project-from-external-storage-medium-rt-unified)

##### Loading project to external storage medium (RT Unified)

###### Introduction

If you cannot establish a direct connection from the configuration PC to the HMI device, load the compiled runtime project onto an external storage medium. For example, use a USB flash drive or SD card.

You load either the complete runtime project or only changes of a runtime project.

As soon as you have connected the external storage medium to your HMI device, transfer the project to the HMI device.

###### Requirement

- An HMI device has been created.
- The project has been compiled without errors.
- A user is configured.

###### Procedure

1. Jump to the "Devices" tab in the project tree.
2. Double-click "Add user-defined card reader" in the "Card reader/USB storage" folder.

   A selection dialog opens.
3. Select a target directory to save the project.
4. Drag and drop the HMI device (e.g. "HMI_1 [<Device type>]") to the added folder.

   Alternatively, use copy and paste.

   The project is checked. If the project has contents that have not yet been compiled, a compile is performed.

   The "Load Preview" dialog opens.
5. In the selection menu you specify which project contents are downloaded:

   - "Full download": The project is downloaded completely.
   - "Delta download": Only changes of the project are downloaded.
6. Click "Load" to confirm.

###### Result

Your project is stored as a compressed ZIP folder in the directory "[<Target directory>]\Simatic.HMI\RT_Projects". The file name is made up of the name of the HMI device, the project name and the time stamp:

- Projects that were created with the option "Full download" receive as file name e.g. "HMI_RT_1[Project1] - Full 2020-04-03 - 14.51.41.zip".
- Projects that were created with the option "Delta download" receive as file name e.g. "HMI_RT_1[Project1] - Delta 2020-04-03 - 14.53.45.zip".

If errors or warnings occur during the download, corresponding alarms are output under "Info > General" in the Inspector window.

---

**See also**

[Basics of downloading projects (RT Unified)](#basics-of-downloading-projects-rt-unified)

##### Load project from external storage medium (RT Unified)

Use the SIMATIC Runtime Manager to download a project from an external storage medium.

---

**See also**

[Adding a project (RT Unified)](SIMATIC%20Runtime%20Manager%20%28RT%20Unified%29.md#adding-a-project-rt-unified)

### Compiling and loading with team engineering (RT Unified)

This section contains information on the following topics:

- [Basics on compiling and loading with team engineering (RT Unified)](#basics-on-compiling-and-loading-with-team-engineering-rt-unified)
- [Compiling in the server project view and in the exclusive session (RT Unified)](#compiling-in-the-server-project-view-and-in-the-exclusive-session-rt-unified)

#### Basics on compiling and loading with team engineering (RT Unified)

##### Introduction

You can compile and download to an HMI device in the server project view, in the exclusive session and the local session.

> **Note**
>
> **Unified objects cannot be selected in a local session**
>
> To edit an object using Multiuser Engineering, it must first be "selected". Only objects marked for check-in can be transferred into the server project after editing.
>
> Unified objects cannot be marked in a local session. Changes to these objects are not applied to the server project during check-in.
>
> You can edit unmarked objects in the server project view.

##### Basics

The options for compiling and downloading in the server project view, in the exclusive session or the local session are no different from the options in a single-user project. The most recent project is always compiled or loaded from the currently active view.

You can execute all commands for compiling and downloading in multiuser engineering and exclusive engineering:

- "Software (rebuild all)"
- "Compile > Software (only changes)"
- "Software (all)"
- "Download to device > Software (only changes)"

##### Rules

The following rules apply to compiling and downloading in multiuser engineering and exclusive engineering:

- The project that was changed in a local session always remains local and is not uploaded to the multiuser server.

  > **Note**
  >
  > A Unified project that was created or changed in a local session cannot be saved in the multiuser server project.
  >
  > Use the local session to test your configuration. When you update your local session, all changes to Unified objects are overwritten by the server project.
- Only projects that were created or changed in the server project view or in the exclusive session can be saved in the multiuser server project.

---

**See also**

[Compiling in the server project view and in the exclusive session (RT Unified)](#compiling-in-the-server-project-view-and-in-the-exclusive-session-rt-unified)
  
[Downloading projects (RT Unified)](#downloading-projects-rt-unified-1)
  
[YouTube](https://www.youtube.com/watch?v=n4oTZ2Gzg6U)

#### Compiling in the server project view and in the exclusive session (RT Unified)

##### Basics

Compiling and downloading of projects in the server project view and the exclusive session is no different from compiling and downloading in a single-user project.

While you are compiling a project in the server project view or the exclusive session, the server project is blocked. Other users cannot edit the server project in the meantime. The compiled runtime project is saved with the WinCC project on the central server. Blocking the server project ensures that the configuration data and the runtime project remain synchronized.

> **Note**
>
> When you compile and save in the server project view or in the exclusive session, other users then obtain the Runtime project you have updated along with the WinCC project when they "refresh" their local session. Other users do not have to recompile the changes you have made after an update.

---

**See also**

[Basics on compiling and loading with team engineering (RT Unified)](#basics-on-compiling-and-loading-with-team-engineering-rt-unified)

### Error messages during loading of projects (RT Unified)

#### Possible problems during the download

When a project is being downloaded to the HMI device, status messages regarding the download progress are displayed in the output window.

Problems arising during the download of the project to the HMI device are usually caused by one of the following errors:

- Wrong version of operating system on the HMI device
- Incorrect settings for downloading to the HMI device
- Incorrect HMI device type in the project
- The HMI device is not connected to the configuration PC.

The most common download failures and possible causes and remedies are listed below.

#### The download is canceled due to a compatibility conflict

| Possible cause | Remedy |
| --- | --- |
| The configuration PC is connected to a wrong device, e.g. a PLC. | Check the cabling.   Correct the communication parameters. |
| The database of the configured HMI device in the engineering system differs from the database type in runtime. | Runtime of the Unified PC uses Microsoft SQL.   Change the database type in the runtime settings of the HMI device under "Storage System" to "Microsoft SQL". |

#### Project download fails

| Possible cause | Remedy |
| --- | --- |
| The connection to the HMI device cannot be established. | Check the physical connection between the configuration PC and the HMI device. |

---

**See also**

[Downloading projects (RT Unified)](#downloading-projects-rt-unified-1)

### Starting and stopping runtime (RT Unified)

#### Introduction

You have two options for starting a project Runtime:

- Select the "Start runtime" option in the "Load preview" dialog before you download a runtime project.

  Runtime is started automatically after downloading the Runtime project.
- Use the "SIMATIC Runtime Manager".

#### Requirements

- The runtime project is downloaded to the HMI device.

#### Starting runtime

To start the Runtime of the downloaded Runtime project with the SIMATIC Runtime Manager, follow these steps:

1. Start the "SIMATIC Runtime Manager" tool.
2. Click on the project in the project list.
3. Click the "Start" ![Starting runtime](images/134448358411_DV_resource.Stream@PNG-de-DE.png) button.
4. Define whether project data is reset on startup.

   - To start the project in a state that existed when the project was first started, activate the options "Reset login data" or "Reset Runtime data".
   - Disable these options to start the project in a state that existed before the last project stop.
5. Select "Start".

#### Stop runtime

You have two options for stopping a project Runtime:

- Select the "Online > Stop runtime/simulation" button in the Engineering System.
- Select the "Stop" button in the "SIMATIC Runtime Manager".

---

**See also**

[Downloading projects (RT Unified)](#downloading-projects-rt-unified-1)

### Managing users in Runtime (RT Unified)

#### Requirement

- An administrator has been created.
- The IP address or the fully qualified name (name and domain) of the PC on which Runtime is installed is entered in the browser.

  If Runtime is installed on the same PC as the browser, the "localhost" designation can also be used.

#### Procedure

1. Select "User management".
2. Log on as an administrator.
3. Expand the selection menu at the top right.

   ![Procedure](images/127848814987_DV_resource.Stream@PNG-de-DE.png)
4. Select "Users".
5. You have the following options:

   - Create new users.
   - Change the properties of the users.

**Changing your password**

1. Expand the selection menu at the top right.
2. Select "User profile".
3. Enter your current password.
4. Assign a new password.
5. Enter the new password again.
6. Select "Change". The password is changed.

## Simulating control with PLCSIM (RT Unified)

This section contains information on the following topics:

- [Using PLCSIM (RT Unified)](#using-plcsim-rt-unified)
- [Starting simulation and simulating behavior (RT Unified)](#starting-simulation-and-simulating-behavior-rt-unified)
- [Preparing simulation with PLCSIM (RT Unified)](#preparing-simulation-with-plcsim-rt-unified)
- [Working with PLCSIM (RT Unified)](#working-with-plcsim-rt-unified)

### Using PLCSIM (RT Unified)

#### Introduction

With PLCSIM you can test the configuration of your HMI device without the PLC required for it. PLCSIM simulates a PLC to which you connect the HMI device. Process parameters can be changed, or specific hardware behavior can be triggered to test the reaction of the HMI device.

With PLCSIM, you can test the following functions of your HMI device:

1. Communication between HMI device and PLC

   - Read
   - Write
2. Process behavior

   - Changing PLC parameters
   - Sequential change of recorded changes to PLC parameters
3. Hardware behavior

   - Hardware alarm
   - Diagnostic error alarm
   - Pulling or plugging modules
   - Rack/station failure

![Introduction](images/147982079499_DV_resource.Stream@PNG-en-US.png)

#### Requirements for using PLCSIM

**Requirements in the software**

Install the corresponding version of PLCSIM for your WinCC. To use PLCSIM, you need a valid license for WinCC.

> **Note**
>
> **Installation**
>
> - Hardware and software of the programming device or PC meet the system requirements.
> - You must have administrator privileges on your computer.
> - All running programs have been closed.

**Requirements in the project**

No special preparations are necessary to use PLCSIM. You complete their configuration in the usual way. When you start the simulation, the communication runs with PLCSIM instead of a real PLC.

### Starting simulation and simulating behavior (RT Unified)

#### Requirement

The configuration is completed.

#### Procedure

To test the configuration in runtime, follow these steps:

1. Select the PLC in the project tree and select "Online > Start simulation" in the menu.

   PLCSIM starts and the "Extended download to device" dialog is displayed.
2. Start the search with "Start search".

   The simulated PLC is displayed as target device.
3. Select the simulated PLC and select the "Download" command.

   PLCSIM is now ready for operation.
4. Select the HMI device in the project tree and select "Online > Download to device" in the menu.

   The "Load Preview" dialog is displayed.
5. Select the desired settings and load the project into the HMI device.
6. Start runtime.
7. Use the editors of the project view of PLCSIM to test the behavior of the HMI device.

### Preparing simulation with PLCSIM (RT Unified)

#### Requirement

- The engineering project is open.
- PLCSIM has started.

#### Procedure

To prepare a project with PLCSIM, follow these steps:

1. Switch from the compact view to the project view of PLCSIM by clicking on the button in the upper right-hand corner.
2. Open the "New" command via the "Project" menu and create a new project via the dialog.
3. Load and organize the PLC tags from the project in the SIM tables.

   You can load all PLC tags from an active project using the "Load project tags" button.
4. If desired, create sequences by recording the parameter changes in the SIM tables or create events in the event table.
5. Save the project.

#### Result

The PLCSIM project is prepared and can be used.

### Working with PLCSIM (RT Unified)

#### User interface of PLCSIM

With PLCSIM, you can choose between two different user interfaces: Compact view and project view. The view you select depends on how you want to use PLCSIM in combination with TIA Portal.

#### Compact view - Operate PLC

You operate the CPU exclusively in the compact view. The basic operating functions of a CPU are available with the operator controls of the compact view: "RUN", "STOP", "PAUSE" and "MRES". The status displays inform you about the state of the CPU.

![Compact view - Operate PLC](images/148085378059_DV_resource.Stream@PNG-de-DE.PNG)

#### Project view - Simulate process behavior and hardware behavior

The project view offers the same functions as the compact view. Additionally, simulation projects are created and stored in the project view. In the simulation project, you define the CPU behavior that you want to simulate. Several editors are available for this:

- You import PLC parameters from the automation project in Sim tables. The parameters can be written and read there.
- You simulate the behavior of external processes in sequences. To do this, you start a recording and record parameter changes that you make in the SIM table. You can edit the recorded sequence afterwards and test your process with it.
- In result tables, you select from a list of hardware actions that you want to simulate. Triggerable events are alarms, pulling and plugging of modules as well as the failure of modules or stations.

![Project view - Simulate process behavior and hardware behavior](images/148146055563_DV_resource.Stream@PNG-en-US.PNG)

#### Further information

You can find more information on this topic in the PLCSIM user documentation.
