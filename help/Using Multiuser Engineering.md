---
title: "Using Multiuser Engineering"
package: PEMuEnenUS
topics: 73
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using Multiuser Engineering

This section contains information on the following topics:

- [Introduction to Multiuser Engineering](#introduction-to-multiuser-engineering)
- [Overview of the mode of operation with Multiuser Engineering](#overview-of-the-mode-of-operation-with-multiuser-engineering)
- [Basics of the project server](#basics-of-the-project-server)
- [Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)
- [Requirements for working with Multiuser Engineering](#requirements-for-working-with-multiuser-engineering)
- [Supported objects for Multiuser Engineering](#supported-objects-for-multiuser-engineering)
- [Settings for working with Multiuser Engineering](#settings-for-working-with-multiuser-engineering)
- [Improvement of the Multiuser Engineering functionality](#improvement-of-the-multiuser-engineering-functionality)
- [Working offline with Multiuser Engineering](#working-offline-with-multiuser-engineering)
- [Operator controls in Multiuser Engineering](#operator-controls-in-multiuser-engineering)
- [Functionality of the multiuser editor](#functionality-of-the-multiuser-editor)
- [Notes on working with the TIA Project Server](#notes-on-working-with-the-tia-project-server)
- [Working with the local project server](#working-with-the-local-project-server)
- [Creating and managing server projects and server libraries](#creating-and-managing-server-projects-and-server-libraries)
- [Working in the local session](#working-in-the-local-session)
- [Working in the server project view](#working-in-the-server-project-view)

## Introduction to Multiuser Engineering

### Introduction

In the TIA Portal, you have the option of working with Multiuser Engineering.

The advantage of this is that you can work with multiple users simultaneously in server projects. This approach significantly reduces the configuring times for your projects. You can commission your plant faster and start production sooner.

In Multiuser Engineering, you can also use other functionalities of Team Engineering, such as working together on a CPU and exchanging data with Inter Project Engineering (IPE).

And this is how Multiuser Engineering works in the TIA Portal:

1. Project management is located either on a local or external TIA Project Server.
2. Different users work in local sessions, based on the projects managed by the server.
3. Users work independently from each other in local sessions.
4. The changes from the local sessions are transferred to the server project on check-in.
5. Checked-in changes from other editors are displayed and can be conveniently applied.

> **Note**
>
> **Working efficiently with Multiuser Engineering**
>
> When working in parallel in multiple local sessions, you should correct any errors that occur promptly so that the distributed work on a shared project stays efficient.
>
> Therefore, it is recommended to first compile pending changes before check-in in the multiuser editor. Several compiling options are available for this. If compiling errors are indicated, you should correct them remove before check-in.
>
> Compiling pending changed before check-in ensures that you are checking in and transferring an error-free project to other editors.

Different options are available for working simultaneously on a server project, as can be seen in the table below:

| Application scenarios for Multiuser Engineering |  |
| --- | --- |
| **Scenario 1:**   Several configuration engineers work across multiple devices  on different objects.    In this scenario, each configuration engineer works on the objects assigned to them on different devices. | ![Introduction](images/112867870859_DV_resource.Stream@PNG-de-DE.png) |
| **Scenario 2:**   Several configuration engineers work device-oriented  on different objects.    In this scenario, each configuration engineer works on the objects assigned to them on only one device. | ![Introduction](images/86428044043_DV_resource.Stream@PNG-de-DE.png) |
| **Scenario 3:**   Several configuration engineers work technology-based  on different objects.    In this scenario, each configuration engineer works on defined technological objects (e.g. Motor_1 or Motor_2) on all existing devices. | ![Introduction](images/86428040203_DV_resource.Stream@PNG-de-DE.png) |

You can make your configuration time more effective and shorten it considerably by editing multiple objects in parallel in one or more devices within a server project, for example:

- Variables
- Blocks
- PLC tags
- Global libraries
- Interrupts
- Screens
- Text and graphics lists
- Technology objects

---

**See also**

[Overview of the mode of operation with Multiuser Engineering](#overview-of-the-mode-of-operation-with-multiuser-engineering)
  
[Basics of the project server](#basics-of-the-project-server)
  
[Requirements for working with Multiuser Engineering](#requirements-for-working-with-multiuser-engineering)
  
[Supported objects for Multiuser Engineering](#supported-objects-for-multiuser-engineering)
  
[Working with asynchronous commissioning](Using%20Multiuser%20Commissioning.md#working-with-asynchronous-commissioning)

## Overview of the mode of operation with Multiuser Engineering

### Introduction

If you want to work with multiple users simultaneously in server projects, specific procedures must be observed.

Below you will find an overview of the general mode of operation with Multiuser Engineering.

### Application example

You can find an application example for working with Multiuser Engineering at:

[https://support.industry.siemens.com/cs/ww/en/view/109740141](https://support.industry.siemens.com/cs/ww/en/view/109740141)

### Requirements for working with Multiuser Engineering

The following rules and requirements apply to working in server projects:

- The projects to be edited should already contain the entire hardware configuration, the required blocks, connections and global settings before they are used as server projects.

  For more information on this topic, refer to: [Requirements for server projects](#requirements-for-server-projects)
- Avoid working on the same objects simultaneously by consulting beforehand with the other editors.
- You set all global settings should be made in the server project view, i.e. in the central server project, such as the changes within the device configuration.
- You can edit all objects of a project in the server project view.

  You can also edit objects that do not support the Multiuser Engineering functionality.

### Overview of the mode of operation with Multiuser Engineering

To use the functionality of Multiuser Engineering, follow these steps:

| Action | Example |
| --- | --- |
|  |  |
| **1. Create server project on the project server**     You install a project server and upload a single-user project to the server that is being used.  - The project should be structured in such a way that it meets the requirements of server projects.      **Result:**   By uploading a project to the project server, you generate a server project out of the single-user project. | ![Overview of the mode of operation with Multiuser Engineering](images/124593086987_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **2. Create local session for "Editor 1"**     Create a "local session" as copy of the server project on your computer.   - For each editor, the objects they are editing in their local session is automatically identified with a blue flag. - Various objects can be edited at the same time by different users in the various local sessions.      **Result:**   Objects edited in their own local session are identified with a blue flag.  The flags are also displayed in the project tree and the editors of the TIA Portal. | ![Overview of the mode of operation with Multiuser Engineering](images/124596317323_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **3. Create local session for "Editor 2"**     You create a second local session so that the second editor can edit their task in their own local session.  - For the second editor, too, the objects they are editing in their local session are automatically identified with a blue flag.      **Result:**   Objects marked in their own local session are identified with a blue flag.  Objects selected in another local session are automatically identified with a yellow flag in their own local session.  Therefore, each editor also sees which objects they are working on or which other editors are working on. | ![Overview of the mode of operation with Multiuser Engineering](images/124651509643_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **4. Checking in the changes by "Editor 1".**     As soon as the work in the local session has reached a certain working version, check the changes into the server project.   - The changes to marked objects are applied in the server project by the check-in. - After the check-in, "Editor 2" is shown in their local session that a object is "outdated".      **Result:**   The changes of "Editor 1" are transferred to the server project.  "Editor 2" can refresh its local session with the new server data, if required. | ![Overview of the mode of operation with Multiuser Engineering](images/124596322059_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **5. "Editor 2" updates their local session**     "Editor 2" is shown in their local session that an object is available in a newer version in the server project and updates their local session.  - The newer version is applied by the refresh and inserted in their own local session. - All unmarked objects are overwritten with the current server version. Marked objects remain unchanged.      **Result:**   The changes from the server project are transferred to the local session of "Editor 2". | ![Overview of the mode of operation with Multiuser Engineering](images/124596838795_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **6. "Editor 2" checks in changes to server project**     "Editor 2" has completed their changes in the local session and checks their blue-marked objects into the server project.  - The changes to marked objects are applied in the server project by the check-in. - After the check-in, "Editor 1" is shown in their local session that an object is "outdated".      **Result:**   The changes of "Editor 2" are transferred to the server project.  "Editor 1" can refresh their local session with the new server data, if required. | ![Overview of the mode of operation with Multiuser Engineering](images/124657906443_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **7. Processing is completed**     The processing of the various configuration tasks in the local sessions has been completed.     **Result:**   All changes are checked in to server project.  The local sessions and the server project are synchronized.  There are no more markings in the local sessions.     **Note**:  If required, you can export the local sessions as single-user project and continue to work on them as usual in the TIA Portal. | ![Overview of the mode of operation with Multiuser Engineering](images/124596843531_DV_resource.Stream@PNG-en-US.png) |

---

**See also**

[Requirements for working with Multiuser Engineering](#requirements-for-working-with-multiuser-engineering)
  
[Basics of the project server](#basics-of-the-project-server)
  
[Supported objects for Multiuser Engineering](#supported-objects-for-multiuser-engineering)
  
[Requirements for server projects](#requirements-for-server-projects)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)

## Basics of the project server

### Introduction

To work with Multiuser Engineering, Multiuser Commissioning or Exclusive Engineering, you need a project server that manages your server projects, server libraries and the local sessions.

Each version of the TIA Portal contains a version-specific project server with corresponding functionality.

With the help of the project server you can:

- Create new server projects and server libraries in which multiple users can work at the same time.
- Show and manage existing server projects and server libraries.
- Sort and manage server projects and server libraries in groups.
- Create and manage local sessions.

**Compatibility of the project server with the TIA Portal**

Communication between the project server and the TIA Portal is supported for various applications.

For more details, see: [Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)

### Requirement

To use the functionality of the project server, you need to install the appropriate software for the project server.

Alternatively, you can use the local project server installed by default with the TIA Portal.

### Possible server constellations

Different server constellations are available in the TIA Portal:

1. The project server as "dedicated server" that is implemented as external server for long-term collaboration.
2. The "temporary project server" in which the server functionality is implemented on a workstation.
3. The "local project server" that is automatically installed in the TIA Portal but only has limited functionality.

The table below provides an overview of working with the possible server constellations.

| Overview of possible server constellations for the project server |  |
| --- | --- |
| **1st project server as dedicated server**   - The project server can be installed with the TIA Portal or as a standalone product. - This configuration is usually the one that is used as "office network configuration". - The project server runs on a separate computer. - This server constellation can be reached at all times and supports integrated working "around the clock" by default. - The project server must be installed and configured. | ![Possible server constellations](images/124904147851_DV_resource.Stream@PNG-en-US.png) |
| **2. Temporary project server:**   - Editors of the server project can apply the server function to their computer. - This configuration is also a possible "office configuration". - You must install and configure the temporary project server. | ![Possible server constellations](images/86476331403_DV_resource.Stream@PNG-en-US.png) |
| **3. Local project server:**   - The local project server runs on the computer of the respective editor. - The local server is available immediately without additional installation and configuration because it is installed with the TIA Portal. - There is no license request for the local project server. - The local project server cannot be accessed from other computers. - The local project server is suitable for learning and testing the functionality of Multiuser Engineering, Multiuser Commissioning and Exclusive Engineering. No server installation and no configuration is required. - The local project server can also be used for separate project management with "rollback" function. | ![Possible server constellations](images/86476313995_DV_resource.Stream@PNG-en-US.png) |

---

**See also**

[Overview of the mode of operation with Multiuser Engineering](#overview-of-the-mode-of-operation-with-multiuser-engineering)
  
[Requirements for working with Multiuser Engineering](#requirements-for-working-with-multiuser-engineering)
  
[Supported objects for Multiuser Engineering](#supported-objects-for-multiuser-engineering)
  
[Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)

## Notes on the compatibility of the project server

### Introduction

To work with Multiuser Engineering, Multiuser Commissioning and Exclusive Engineering, you need a project server that manages your server projects, server libraries and the local sessions.

### Compatibility of the project server with the TIA Portal

Communication between the project server and the TIA Portal is supported for the following applications:

| Version of the project server | Version of the TIA Portal |
| --- | --- |
| TIA Project Server V1.2 | V19, V18, V17, V16, V15.1, V15 and V14 |
| TIA Project Server V1.1 | V18, V17, V16, V15.1, V15 and V14 |
| Server V17 / TIA Project Server V1.0 | V17, V16, V15.1, V15 and V14 |
| Server V16 | V16, V15.1, V15 and V14 |
| Server V15.1 | V15.1, V15 and V14 |
| Server V15 | V15 and V14 |
| Server V14 | V14 |

> **Note**
>
> **Notes on the compatibility of the project server**
>
> The newly added server functionality for the current version is only available if the current version of TIA Portal is also installed.
>
> If you are still working with an older version of TIA Portal or an older version of the project server, only the functionality included in the respective product version is available.
>
> Multiuser Engineering does not upgrade the project versions.

### Storage directory of the project server

Each TIA Portal version is delivered with the project server version released for it.

You can define a new storage directory for the new project server or continue using an existing storage directory of an older project server for the new server version, in which you have saved the V15 projects, for example.

The following rules apply:

- To use different servers at the same time and independent of each other, you must configure different ports and storage directories for the different servers during installation of the new server.
- To continue using an older server directory as storage for the newly installed project server, enter the existing directory during configuration of the new project server. The storage path is checked during installation of the project server, and you receive a corresponding message that this storage directory is already being used for a different server.

  You then have the following options:

  - You can cancel the installation and enter a new storage directory for the project server.
  - Or you can upgrade the storage directory for the project server.

  However, the upgraded directory becomes invalid for older server versions and can no longer be started with the older server.

  The upgrade of the storage directory does not impact the TIA Portal projects saved in the directory.

  An internal backup is executed prior to the upgrade so that you can undo any erroneous upgrade.

  If there are no errors during the upgrade, the "Undo" function is not offered.

  > **Note**
  >
  > **Storage directory of the server**
  >
  > The storage directory of the project server is locked during installation of the server.
  >
  > This is intended to prevent changes to a storage directory while it is actively being accessed.

## Requirements for working with Multiuser Engineering

### System requirements

The same hardware and software requirements as for working with TIA Portal apply to working with Multiuser Engineering .

For information about the regulations in place for the products you have installed, go to "Installation &gt; [System requirements for installation](Installation.md#system-requirements-for-installation)".

> **Note**
>
> **Identical software installation as requirement for working with Multiuser Engineering**
>
> To work with Multiuser Engineering without any restrictions, it is important that the same software products of the TIA Portal are installed with identical product versions on all Engineering Systems used.
>
> **Access to the project server**
>
> Users can only receive access to the project server if they are **not** included in the local administrator group of the project server.
>
> **Access to the server project and the server library**
>
> Users can only receive access to a server project or a server library if they are included at least as a "Member" in the user administration of the project server.

### Project server

To work with the full functionality of Multiuser Engineering, you need an installed project server.

You need administrator rights in part for installing, configuring and administering the project server.

You will find information on the compatibility of the project server under: "[Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)"

The project server is configured and administered with the supplied tools.

Two alternative procedures are available for this purpose:

- Using the graphical user interface
- Using the "Administrative Tools" and "Power Tools" which are executed with the command line.

You can configure and administer the project server using a convenient user interface or with command line commands. Both procedures lead to an identical result.

A detailed description of the procedure is available under "[Installing the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)" and under "[Configuring and administering the project server](Working%20with%20the%20TIA%20Project-Server.md#configuring-and-managing-the-project-server)".

### Network profiles for the project server

You have the option of setting the required performance capability for the network profile you are using in the settings for the TIA Portal.

To do so, select the required profile from the drop-down list in TIA Portal under "Options &gt; Settings &gt; Project server &gt; Server network profiles".

You will find a detailed description of the network profiles under: "[Set network profiles for project server](#set-network-profiles-for-project-server)"

### Licensing for Multiuser Engineering

For working with Multiuser Engineering , you only need a license for a specific version (Floating License) and an associated License Key when you are working with a project server.

As long as you are only using the local project server with limited functionality, you do not need an additional license for the installed TIA Portal.

You can either include the License Key in the installation of the TIA Portal or transfer it using the Automation License Manager after the installation. Multiuser Engineering checks whether a valid license key exists as soon as you open a local session to edit objects.

If a valid license key is found, the local session is opened and you can work in the local session without restrictions.

If a valid license key is not found, you will receive an error message.

You can temporarily activate a "Trial" license to work in a local session.

Once the "Trial" license has expired, you need a valid multiuser license to work in local sessions.

A license is not required for the following actions in the context of Multiuser Engineering:

- Configuring and starting the project server
- Opening the server project management
- Adding projects and global libraries to the project server
- Creating local sessions
- Deleting local sessions
- Exporting local sessions as single-user projects
- Working in an exclusive session

> **Note**
>
> **Handling licenses**
>
> Please observe the general information on handling licenses in the TIA Portal.
>
> This information is available in the "Installation" section of the respective products in the information system.

### Archiving and retrieving projects

The following restrictions apply to archiving and retrieving multiuser projects:

- You can only archive local sessions as single-user projects.
- You cannot archive or retrieve server projects.

### Opening a local session as reference project

When working with Multiuser Engineering, you can open a locally stored session as a reference project.

You can find additional information on working with reference projects here: "Edit projects &gt; [Use reference projects](Editing%20projects.md#using-reference-projects)"

### Length of the path and file names in Multiuser Engineering

If the path and file names have more than 259 characters in total, an error message is displayed when you are working with Multiuser Engineering. You are notified that the used names are too long and that the requested action cannot be performed for this reason.

Shorten the path names or file names in this case so that the required action can be performed.

---

**See also**

[Set network profiles for project server](#set-network-profiles-for-project-server)
  
[Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)
  
[Archiving a local session of a server project](#archiving-a-local-session-of-a-server-project)
  
[System requirements for installation](Installation.md#system-requirements-for-installation)
  
[Configuring and managing the project server](Working%20with%20the%20TIA%20Project-Server.md#configuring-and-managing-the-project-server)
  
[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)
  
[Using reference projects](Editing%20projects.md#using-reference-projects)

## Supported objects for Multiuser Engineering

### Introduction

The Multiuser Engineering functionality is available in the TIA Portal for the objects listed below.

Objects that do not support this functionality yet can be edited in the local session but cannot be marked.

This means they are **not** applied to the server project during check-in. The changes to such objects are again overwritten with the contents of the server project and lost after check-in and after a refresh in the local session.

You can edit these objects that cannot be marked in the server project view.

You should make version changes to instructions in the server project view.

In Multiuser Engineering, it is also possible to work with the Team Engineering functionality, such as working on a shared CPU and data exchange via Inter Project Engineering (IPE).

### STEP 7: Supported objects for Multiuser Engineering

The objects listed below for the STEP 7 product are supported:

- Blocks:

  OB, FB, FC, global DBs and instance DBs

  Exception: The "MC-Servo" and "MC-Interpolator" blocks are not supported for automark.
- Software-Units:

  Contained blocks, such as OBs, FBs, FCs, global DBs and instance DBs.

  Relations can only be edited in the server project view.
- PLC data types and constants:

  Exception: The system data types generated automatically by the system.
- Tags:

  Exception: System tags that are created and deleted by the system.
- Interrupts:

  Exception: System alarms

  Program interrupts can only be marked for editing together with the associated FB or DB.
- Interrupt classes:

  Exception: System alarm classes
- Text lists:

  Exception: System text lists
- Watch and force tables
- Library elements of the project libraries
- Library elements of the global libraries

  Global libraries can be configured as a multiuser server library and processed in local sessions.
- Technology objects:

  Exception: Technology objects for Motion Control on S7-1500 CPUs.
- Trace functionality:

  Exception: Online configurations
- TIA Portal Test Suite:

  Rule sets of the Test Suite
- ProDiag:

  Blocks supervised with ProDiag, such as FBs or global DBs, Software Units, PLC data types or PLC tags, are supported by Multiuser Engineering as of TIA Portal V17.

### WinCC (TIA Portal): Supported objects for Multiuser Engineering

The following objects for the WinCC product in TIA Portal are supported:

- Screens:

  Exception: Global screen, overview screen, slide-in screens and global filtering of the alarm view.
- Scripts:

  Exception: Header file "GlobalDefinitions.h".
- Tags:

  Exception: System tags, recipe tags, archive tags and raw data tags generated by the system.
- Alarms:

  Exception: System alarms, controller alarms, predefined system alarm classes (including "Safety Warnings" for KTP700F, KTP900F), system class groups and system alarm groups as well as message blocks.
- Text and graphic lists and C text list entries

### WinCC Unified: Supported objects for Multiuser Engineering

The following objects for the WinCC Unified product are supported:

- WinCC Unified screens
- HMI alarms
- HMI tags

### OPC UA: Supported objects for Multiuser Engineering

The objects listed below are supported for OPC UA communication:

- Server interfaces and client interfaces

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Editing unsupported objects in the local session**  Objects that are not supported can be edited in a local session but cannot be marked:  - Changes to unsupported objects are **not** applied to the server project during check-in.   Changes to such objects are lost after check-in and after an update in the local session, because these objects are once again overwritten with the contents of the server project.  You can, however, edit such objects that are not supported in the usual way in the server project view. |  |

### STEP 7 CFC: Supported objects for Multiuser Engineering

To edit STEP 7 CFC charts via Multiuser Engineering, use "Multiuser Commissioning" with the synchronous commissioning mode.

More information:

- "Programming PLC &gt; Creating and technologically configuring CFC charts &gt; Working with CFC charts for S7 &gt; Multiuser engineering in CFC."

**Online mode**

Before you edit CFC charts in online mode, the local session must match the version downloaded to the PLC.

Parameter changes are written directly to the PLC in online mode.

To apply the changed values to the server project, check in the data of the local session afterward.

**Supported objects**

The following objects are supported in CFC charts:

- CFC charts and interconnections
- Hierarchical CFC charts
- Interconnections across charts
- Run sequence
- Trend displays and value displays
- Instructions and blocks
- Block instances

## Settings for working with Multiuser Engineering

### Introduction

To work with Multiuser Engineering , you can make the following settings under "Extras &gt; Settings" in the "Multiuser" tab in TIA Portal:

- General
- Searching in the project
- Compilation settings

The individual setting options are described below.

### General

In the "General" settings you can select whether the editors opened in the local session are to be hidden when the server project view is opened.

This option is disabled by default.

### General: Displaying local sessions

As the default setting only local sessions which are on the local computer are displayed in the "Manage server projects" and "Manage server libraries" dialogs.

To also display local sessions from other systems, activate the option "Show local session created on other systems".

To sort the display in the management dialog according to the computer names, show the "Computer name" column.

### Searching in the project

The data for the search must be indexed in order for the global search to also work in local sessions.

This option is enabled by default so that the indexing for the search is always completed during check-in.

This is the recommended setting.

If you disable this option, the indexing is started during check-in, but not completed. The full indexing is performed at other times while working in the server project. If you check in many changes over a longer period of time without indexing, the duration of the complete indexing can increase noticeably.

As long as the indexing is not completed yet, the search results remain incomplete.

A search in the local session is only possible after indexing has been successfully completed. If no indexing was performed during check-in, this can lead to somewhat longer waiting times when searching. This can result in longer check-in times for other editors who have also enabled this option.

### Compilation settings

Define here the required compilation settings for your local sessions.

The settings made here are applied as defaults in the multiuser editor and can no longer be changed there.

Select the required settings:

- Compile before check-in

  This option is enabled by default and means that a compiling process is executed before the check-in.
- Compilation settings:

  This setting defines the extent to which the software changes are compiled.

  - Marked objects (changes only)

    The changes made to the marked objects for the selected device are compiled together with the device-specific objects.
  - Device software (changes only)

    The changes made to the marked objects are compiled together with the software version on the assigned devices.

    **Example**: You have marked and changed several objects that belong to more than one device (for example to CPU_1 and to CPU_2). These marked objects are compiled together with the software versions of both CPUs during compiling.
- Disable compilation settings in the multiuser editor

  If you activate the option, you can no longer change the compilation settings in the multiuser editor.

  The settings you made here then apply as default.

---

**See also**

[Set network profiles for project server](#set-network-profiles-for-project-server)
  
[Introduction to the project server](#introduction-to-the-project-server)

## Improvement of the Multiuser Engineering functionality

### Introduction

In TIA Portal, you have the option of working with multiple users simultaneously in multiuser projects within the framework of Multiuser Engineering.

Multiuser Engineering functionality has been further improved as described below.

### "Autoselect" function

- As of TIA Portal V15, objects edited with Multiuser Engineering are selected automatically.

  The "Autoselect" function automatically identifies newly created or changed objects in the local sessions for check-in by setting the corresponding multiuser selections. It is irrelevant here if the changes were made by the user or by the system.
- Deleted objects, too, are selected automatically so that these objects can also be deleted in the server project after check-in.
- In addition to autoselect, you still have the option of selecting objects manually during editing.
- When you work with Multiuser Engineering, there are no functional differences between objects marked automatically and those marked manually.
- The "Autoselect" function recognizes all changes made by the operator to objects that can be selected and supports you in preventing inconsistencies while sharing work with Multiuser Engineering by automatically selecting these objects.

More information:

- [Marking objects automatically or manually for editing](#marking-objects-automatically-or-manually-for-editing)

### Working offline with Multiuser Engineering

- As of TIA Portal V15, you can switch between "online mode and offline mode" when working with Multiuser Engineering.

  This means that it is possible to continue working in a local session even without an active server connection to a project server.
- Regardless of whether the server connection is interrupted while working in the local session or if you decided to "Work offline" from the very beginning, you can now continue working – with some restrictions – on your multiuser projects even without an active server connection.

More information:

- [Working offline with Multiuser Engineering](#working-offline-with-multiuser-engineering)

### Compatibility of the project server

- The current project server also supports older TIA Portal projects, with corresponding range of functions.
- In each case, the new server functionality added for a new version is only available if the latest TIA Portal version is installed and the latest project version is used.
- If you are still working with an older TIA Portal version or with an older server, only the functionality of the installed version is available.
- Up to TIA Portal V18, project servers from different versions can be used side by side.

  As of TIA Portal V18, TIA Project-Server as of V1.0 is supplied. The new installations of the TIA Project-Server replace the existing installation in each case.

  However, versions of the project server installed with TIA Portal versions prior to V18 can continue to run side-by-side on a PC and parallel to TIA Project-Server versions as of V1.0.

More information:

- [Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)

### Multiuser editors in the TIA Portal

- The multiuser editors were enhanced with comment functions for documentation of the type and scope of the changes made.
- When checking in, a filter is available for viewing objects with "conflicts".

More information:

- [Functionality of the multiuser editor](#functionality-of-the-multiuser-editor)

### Multiuser "Configuration Tool" and "Administration Tool"

- As of project server V15, the external multiuser tools for the configuration and administration of the project server are now available in all languages of the TIA Portal.
- The project server provides an extended project history with a restore function.

  This enables traceability of the project process on the project server. The milestones of a project can be commented on and saved.

  The project history can be exported for extended evaluation.

More information:

- [Using the graphic tools](Working%20with%20the%20TIA%20Project-Server.md#using-the-graphic-tools)

### Project Server Power Tools

- The Power Tools support the management of project groups and the extended user administration.
- In TIA Portal V18 and higher, the "Multiuser Power Tools" have been renamed "Project Server Power Tools".

  Use the command "pspt" in the commands.

  If you are working with project servers from versions prior to TIA Portal V18, use the command "mupt" in the commands.

More information:

- [Using the command line tools](Working%20with%20the%20TIA%20Project-Server.md#using-the-command-line-tools)

### Project Server Administrative Tools

- In TIA Portal V18 and higher, the "Multiuser Administrative Tools" have been renamed "Project Server Administrative Tools".

  Use the command "prjsrv" in the commands.

  If you are working with project servers from versions prior to TIA Portal V18, use the command "musrv" in the commands.

More information:

- [Using the command line tools](Working%20with%20the%20TIA%20Project-Server.md#using-the-command-line-tools)

### Global libraries in the Multiuser Engineering

As of TIA Portal V18 Multiuser Engineering also supports working with global libraries.

- You manage global libraries as objects on the project server, independent of the server projects.

  Use the "Manage server libraries" dialog for the managing. The function corresponds to the dialog "Manage server projects".
- As with server projects you create local sessions in which you process your library objects.
- You load changes in the local session into the server library.

  The changes are loaded from the server library into the other local library sessions.

More information:

- "[Managing global libraries as server libraries](#managing-global-libraries-as-server-libraries)"
- "[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)"
- "Using libraries &gt; Using global libraries &gt; [Using Multiuser Engineering for global libraries](Using%20libraries.md#managing-global-libraries-in-the-project-server)"

### Multiuser Engineering: Exclusive Multiuser mode

As of TIA Portal V19, the "Exclusive Multiuser mode" is also available when editing a local multiuser session:

You can temporarily edit a local multiuser session in the exclusive mutiuser mode and revert to the local multiuser mode after editing.

- The new Exclusive Multiuser mode allows quick changes to objects that cannot be edited in a local session, such as device configuration changes.
- When switching to the exclusive multiuser mode, all changes in the local session are retained.
- Requirements for switching quickly to the Exclusive Multiuser mode:

  - The local session is based on the current project state of the server project.
  - The server and the server project are not locked by another exclusive local session.

In addition, the performance when applying the changes to the TIA Project-Server in the Exclusive Multiuser mode has been significantly improved.

### User management with Multiuser Engineering in TIA Portal

- If you upload a single-user project that is protected with user administration to a project server, the resulting server project is also protected.

  The users and user groups contained in the server project continue to exist with their passwords and can therefore continue to log into the local sessions of the multiuser project, provided they have the corresponding user rights.
- If you protect a previously unprotected local session using the user administration, this protection is removed once again after checking-in and updating the local session, as the project on the server is not protected as a result. This also applies when several editors are protecting their local sessions.
- If you protect the project on the server using the user administration, the local sessions created by this server project are also protected as soon as these are updated.
- If during the processing of your unprotected local session, the project on the server is protected using the user administration and your user account was not assigned the "Open protect read/write" user right, you cannot check in any changes to your session and cannot update your local session.

  You can find additional information on user administration in TIA Portal in the section "Using user administration".
- From TIA Portal V18 you can combine the server projects of a project server into project groups.

  The authorizations of a project server also apply for the contained project groups and projects.

  The authorizations of a project group also apply for the contained projects and local sessions.

More information:

- [Specifying the user administration for a project server](Working%20with%20the%20TIA%20Project-Server.md#specifying-the-user-administration-for-a-project-server)

---

**See also**

[Marking objects automatically or manually for editing](#marking-objects-automatically-or-manually-for-editing)
  
[Working offline with Multiuser Engineering](#working-offline-with-multiuser-engineering)
  
[Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)
  
[Specifying the user administration for a project server](Working%20with%20the%20TIA%20Project-Server.md#specifying-the-user-administration-for-a-project-server)
  
[Managing global libraries in the project server](Using%20libraries.md#managing-global-libraries-in-the-project-server)
  
[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)
  
[Managing global libraries as server libraries](#managing-global-libraries-as-server-libraries)
  
[Using the graphic tools](Working%20with%20the%20TIA%20Project-Server.md#using-the-graphic-tools)
  
[Functionality of the multiuser editor](#functionality-of-the-multiuser-editor)
  
[Using the command line tools](Working%20with%20the%20TIA%20Project-Server.md#using-the-command-line-tools)

## Working offline with Multiuser Engineering

### Introduction

As of TIA Portal V15, you can also work "offline" with Multiuser Engineering.

This means you can continue working in a local session even without an active server connection to a project server with the restrictions listed below.

### Application cases for "Work offline"

The following application cases may occur when working without server connection:

- **A server connection cannot be established when opening the local session.**

  - A dialog with a corresponding message is displayed.
  - When you click "OK", the local session is opened without server connection and you can continue working offline.
- **An existing server connection is interrupted while you are working in a local session.**

  - A dialog with a corresponding message is displayed.
  - When you click "Restore", you can continue working offline.
- **An existing server connection is interrupted while the server project view is open.**

  - A dialog with a corresponding message is displayed.
  - When you click "Restore", an attempt is made to reestablish the server connection.
  - When you click "Discard", the changes you have made in the server project view are discarded and the local session opens.
  - Because there is no server connection when the local session opens, a dialog with a corresponding message is displayed.
  - When you click "Restore", you can continue working offline.
- **You have decided to "work offline" from the very beginning and have selected this option in the TIA Portal under "Project &gt; Multiuser &gt; Work offline".**

### Restrictions for "Work offline"

The following restrictions apply for working in offline mode:

- Only your own selections are displayed in your local session.
- Selections made by other users, i.e. those marked with yellow and red flags, and selections for outdated objects cannot be displayed without a server connection.
- The icon for the server status in the multiuser toolbar shows that you are working offline and that there is no server connection.
- You cannot check in your changes to the server project.
- You cannot update your local session.

### Switching between "Working online and offline"

You can use the command "Project &gt; Multiuser &gt; Work offline" to switch between online and offline mode when working with Multiuser Engineering .

The default is "Work online". If you click on the check box in front of the "Work offline" command, the system switches to offline mode. In the local session, the symbol for the active server connection changes from a green circle to a light-gray circle. When you clear the "Work offline" check box, the server connection is established once again. Once the server connection has been successfully established, the server status is again indicated with a green circle.

The respective setting is saved together with the local session.

If you have worked in "offline mode" in your local session and are switching to "online mode", the open local session is checked for possible selecting conflicts. The result of the check is displayed with a corresponding message.

If conflicts are found, you are prompted to open the change editor and use the filter setting "Show all conflicts" to display all existing conflicts.

Resolve the existing conflicts and continue working online as usual in your local session.

## Operator controls in Multiuser Engineering

This section contains information on the following topics:

- [Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface)
- [Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface-1)
- [Multiuser banner in the user interface](#multiuser-banner-in-the-user-interface)

### Multiuser icons in the user interface

#### Introduction

When you are working with Multiuser Engineering and a local session is open, you can see multiuser-specific icons in the TIA Portal user interface.

#### Multiuser icons in the toolbar

The Multiuser Engineering user interface shows the following icons in the toolbar when a local session is open:

![Multiuser icons in the toolbar](images/171998859403_DV_resource.Stream@PNG-en-US.png)

| Icon | Meaning |
| --- | --- |
| ![Multiuser icons in the toolbar](images/171998867723_DV_resource.Stream@PNG-de-DE.png) | **Multiuser mode**   The icon is enabled when a local session is open in multiuser mode.  To temporarily switch to the Exclusive Multiuser mode, click the "Exclusive multiuser mode" icon.  Requirements for the change:  - No other session is in progress or locked as an exclusive local session.   Before the mode change, the status of the local session and the server project is checked. If you need to refresh the session or server project before changing the mode, a corresponding message is displayed. |
| ![Multiuser icons in the toolbar](images/171998863627_DV_resource.Stream@PNG-de-DE.png) | **Exclusive multiuser mode**   The icon is activated when you edit a local session temporarily in the Exclusive Multiuser mode.  To return to multiuser mode, click the "Multiuser mode" icon. After that, other sessions can be opened as exclusive local sessions.  Before the mode change, the status of the local session and the server project is checked. If you need to refresh the session or server project before changing the mode, a corresponding message is displayed. |
| ![Multiuser icons in the toolbar](images/88369524235_DV_resource.Stream@PNG-de-DE.png) | **Check-in**   When you click this icon, the multiuser editor opens in the change view. In the modification view, all objects marked for check-in are displayed.  You can select and check-in the required objects. |
| ![Multiuser icons in the toolbar](images/88372490635_DV_resource.Stream@PNG-de-DE.png) | **Refresh**   When you click this icon, the multiuser editor opens in the "Refresh" view.  In this view, you refresh your local session with the new contents of the server project. |
| ![Multiuser icons in the toolbar](images/84889833355_DV_resource.Stream@PNG-de-DE.png) | **Open/close server project**   When you click this icon, the server project associated with your local session is opened for editing.  You can then make your changes directly in the server project. |
| ![Multiuser icons in the toolbar](images/112466890891_DV_resource.Stream@PNG-de-DE.png) | **Commissioning mode is not active**   This symbol indicates that commissioning mode is not activated.  You are working in engineering mode.  "Commissioning mode" is enabled and disabled in the Administration Tool. The mode set always applies for all local sessions of a server project. |
| ![Multiuser icons in the toolbar](images/112467326347_DV_resource.Stream@PNG-de-DE.png) | **Commissioning mode is active**   This symbol indicates that you are working in commissioning mode**.**  "Commissioning mode" is enabled and disabled in the Administration Tool. The mode set always applies for all local sessions of a server project. |
| ![Multiuser icons in the toolbar](images/88369528203_DV_resource.Stream@PNG-de-DE.png) | **Server status "connected"**   This icon indicates that the associated project server is available. |
| ![Multiuser icons in the toolbar](images/125655281931_DV_resource.Stream@PNG-de-DE.png) | **Server status "locked for other users"**   This icon indicates that the associated project server is "locked" for other users because you are currently using it. |
| ![Multiuser icons in the toolbar](images/88369531915_DV_resource.Stream@PNG-de-DE.png) | **Server status "locked"**   This icon indicates that the associated project server is currently being used by a user and is therefore locked.  The server is then also displayed as locked when a user is working in the server project view.  If you place the mouse pointer on this icon, you will receive additional information about the lock. |
| ![Multiuser icons in the toolbar](images/88369535627_DV_resource.Stream@PNG-de-DE.png) | **Server status "not connected"**   This icon indicates that the associated project server is not connected. |
| ![Multiuser icons in the toolbar](images/103395513995_DV_resource.Stream@PNG-de-DE.png) | **"Work offline" server status**   This symbol indicates that no connection is established to the project server, since you have enabled the "Work offline" function.  To re-establish a connection to the project server deactivate the check box under "Project &gt; Multiuser &gt; Work offline". |
| ![Multiuser icons in the toolbar](images/84859545739_DV_resource.Stream@PNG-de-DE.png) | This overlay icon shows that a newer version of the server project is available on the project server. |

#### "Libraries" task card

The toolbar of the "Global libraries" pane contains icons for working with server libraries and local library sessions:

!["Libraries" task card](images/159405145483_DV_resource.Stream@PNG-de-DE.png)

| Icon | Meaning |
| --- | --- |
| !["Libraries" task card](images/159368230923_DV_resource.Stream@PNG-de-DE.png) | **Managing global libraries on the server**   The "Manage server libraries" dialog opens when you click this icon.  Possible actions in the dialog:  - Starting the server project - Adding global libraries as server libraries - Creating new local sessions - Opening local sessions |
| !["Libraries" task card](images/159368772619_DV_resource.Stream@PNG-de-DE.png) | **Check-in marked changes**   When you click this icon, the multiuser editor opens in the change view. In the modification view, all objects marked for check-in are displayed.  You can select and check-in the required objects. |
| !["Libraries" task card](images/159368781067_DV_resource.Stream@PNG-de-DE.png) | **Refresh local session**   When you click this icon, the multiuser editor opens in the "Refresh" view.  In this view, you refresh your local session with the new contents of the server library. |
| !["Libraries" task card](images/159368751371_DV_resource.Stream@PNG-de-DE.png) | **Local session**   This icon indicates a local session that belongs to a Multiuser server library. |
| !["Libraries" task card](images/159405134987_DV_resource.Stream@PNG-de-DE.png) | **Local session with "?"**   The question mark identifies that the local session possibly does not correspond to the state of the server library.  To synchronize the state, update the local session. |

In the local sessions the first column of the library list contains the multiuser markings which identify the status of the objects.

More information: "[Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface-1)"

#### Displaying multiuser projects

The following icons are displayed for multiuser projects and local sessions in the user interface:

| Icon | Meaning |
| --- | --- |
| ![Displaying multiuser projects](images/125656947467_DV_resource.Stream@PNG-de-DE.png) | **Project server**   This icon identifies a project server. |
| ![Displaying multiuser projects](images/125655397643_DV_resource.Stream@PNG-de-DE.png) | **Server project**   This icon identifies a server project associated with a project server. |
| ![Displaying multiuser projects](images/125658816779_DV_resource.Stream@PNG-de-DE.png) | **Local session**   This icon indicates a local session that belongs to a Multiuser server project. |
| ![Displaying multiuser projects](images/172092701323_DV_resource.Stream@PNG-de-DE.png) | **Exclusive local session**   This icon indicates a local session which is being edited in the Exclusive Multiuser mode. |

---

**See also**

[Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface-1)
  
[Multiuser banner in the user interface](#multiuser-banner-in-the-user-interface)

### Multiuser icons in the user interface

#### Introduction

When working with Multiuser Engineering , multiuser-specific icons are displayed in the TIA Portal user interface which make it easier for multiple users to work at the same time.

A unique, user-specific visualization is intended to make collaboration within multiuser projects and in local sessions more effective and transparent.

#### Marking objects

To edit an object using Multiuser Engineering, it must first be "selected". Only objects that have been marked for check-in can be transferred to the server project or server library after editing.

Marking can only be added for "marked objects".

Objects that cannot be edited in the local session also cannot be marked. You can, however, edit such objects in the server project view.

The icons described below show you which objects were marked by you or other editors.

You can mark objects manually by clicking the gray flag in front of the respective object, or automatically. If an object not yet marked manually is opened in an editor in a local session, it is automatically marked with the "Autoselect" function.

#### Icons for marking in Multiuser Engineering

The following icons are used for marking in Multiuser Engineering :

| Icon | Meaning |
| --- | --- |
| ![Icons for marking in Multiuser Engineering](images/84845469195_DV_resource.Stream@PNG-de-DE.png) | **Markable object**   This object can be marked for check-in by clicking it. |
| ![Icons for marking in Multiuser Engineering](images/82716066059_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked in your own local session for check-in. |
| ![Icons for marking in Multiuser Engineering](images/84859083659_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked for check-in in a different session or in the server project view. |
| ![Icons for marking in Multiuser Engineering](images/84859302027_DV_resource.Stream@PNG-de-DE.png) | **Marked object**  **with conflict**   The object was marked for check-in in multiple local sessions or in a local session and in the server project view and causes a conflict.  An object should only be marked for check-in once within the entire multiuser working area.  An object marked in red can still be checked in despite the conflict. However, the check-in can lead to unintentional overwriting in the server project or in the server library, since only the last checked-in status in the server project or in the server library is transferred. |
| ![Icons for marking in Multiuser Engineering](images/84859545739_DV_resource.Stream@PNG-de-DE.png) | **Object is outdated**   If one of the icons mentioned above is also identified with this overlay, the object no longer corresponds to the latest version of the server project or server library and should be updated.  If the object is checked in without refresh, the editing of the other user is overwritten and thus cancelled.  The refresh ensures that all editors of a multiuser project have a consistent version. |

> **Note**
>
> **Objects without flags**
>
> Note that objects without flag may only be edited in the server project view and not in the local session.

#### Display of multiuser markings in the TIA Portal

When you are working with Multiuser Engineering in the local session, in the server project or in the server library, the multiuser-specific markings are displayed in the following views of TIA Portal in all editors:

- In the project tree
- In the detail view
- In the overview window under "Details"
- In the library views

An additional first table column is available in the table displays of the project tree and in the "Global libraries" pane when working with Multiuser Engineering. The first table column is reserved for the multiuser-specific markings described above.

The following figure shows an example of multiple selected objects in the project tree:

![Display of multiuser markings in the TIA Portal](images/104401534219_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface)
  
[Multiuser banner in the user interface](#multiuser-banner-in-the-user-interface)

### Multiuser banner in the user interface

#### Introduction

The display of multi-user-specific banner texts in the editors supports you when working with Multiuser Engineering.

Banner texts include notes and warnings on the further procedure which make your work easier.

Banner texts can be expanded and collapsed by clicking the yellow circle with the exclamation mark.

Example of a multiuser banner text:

![Introduction](images/170209110411_DV_resource.Stream@PNG-en-US.png)

#### Functionality of the multiuser banner texts

Banner texts are displayed both when working into the local session and when working in the server project view.

As soon as you need additional information to work with Multiuser Engineering , a yellow banner text appears.

The multiuser banner texts have the following function:

- Information about how to edit the opened object:

  - Banner texts point out, for example, that the opened object has not been marked for check-in and your changes have therefore not been applied to the server project.
  - The banner texts also inform you if you cannot edit a specific object in the local session but only in the server project view or in multi-user mode.
- Links make for easier execution of the further sequences required.

  - The links enable you to jump to further processing, e.g. marking for the opened object.

After the required work steps have been performed in the individual editors, the banner texts are partially removed again in the editor. You can continue working as usual.

---

**See also**

[Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface)
  
[Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface-1)

## Functionality of the multiuser editor

This section contains information on the following topics:

- [Introduction to the multiuser editor](#introduction-to-the-multiuser-editor)
- [Multiuser editor in the "Check-in" view](#multiuser-editor-in-the-check-in-view)
- [Multiuser editor in the "Refresh" view](#multiuser-editor-in-the-refresh-view)

### Introduction to the multiuser editor

#### Introduction

You open the multiuser editor using icons in the toolbar of Multiuser Engineering or in the toolbar of the "Global libraries" pane.

| Icon | Designation | Action |
| --- | --- | --- |
| ![Introduction](images/88369524235_DV_resource.Stream@PNG-de-DE.png) | Check in marked changes | Opens the "Check-in" view |
| ![Introduction](images/88372490635_DV_resource.Stream@PNG-de-DE.png) | Refresh local session | Opens the "Refresh" view |

#### Views of the multiuser editor

The multiuser editor has two different views, depending on the button with which the editor was started in the multiuser toolbar:

- "Check-in" view:

  To open, click the "Check-in" button in the toolbar of the project tree or the "Global libraries" pane.
- "Refresh" view:

  To open, click the "Refresh local session" button in the toolbar of the project tree or the "Global libraries" pane.

  The "Update" view can always be opened even if the local session does not contain any objects that can be updated.

The structure of the multiuser editor is the same in both views, but each view offers different buttons and options.

> **Note**
>
> **Displaying in the multiuser editor**
>
> If you have opened the multiuser editor and simultaneously make changes in your local session, these changes are only visible in the open editor after a "Refresh".
>
> To do this, click the "Refresh" button (circular arrow) in the open editor.

### Multiuser editor in the "Check-in" view

#### Introduction

You call the multiuser editor in the "Check-in" view with the "Check-in" button in the Multiuser Engineering toolbar.

> **Note**
>
> **Displaying in the multiuser editor**
>
> If you have opened the multiuser editor and simultaneously make changes in your local session, these changes are only visible in the open editor after a "Refresh".
>
> To do this, click the "Refresh" button (circular arrow) in the open editor.

#### Multiuser editor in the "Check-in" view

The figure below shows an example of the multiuser editor in the "Check-in" view:

![Multiuser editor in the "Check-in" view](images/104618902923_DV_resource.Stream@PNG-en-US.png)

#### Structure of the multiuser editor

The multiuser editor has the following structure:

**1. Toolbar**:

Displays following buttons:

- On the right side, the button for saving the layout settings.
- On the left side, the button "Collapse all", "Expand all" and "Show conflicts".

  When you click "Show conflicts", all selections with "Conflict" (red flag) are displayed in the editor.

**2. Button area:**

Shows the multiuser-specific buttons for the check-in.

**3. Comment line:**

The comment line is only available in the "Check-in" view.

Here you can enter a comment to document the changes made in the local session.

**4. Working area:**

Shows the change view prior to check-in.

- Shows all objects marked in the local session for check-in and refresh as these are also displayed in the project tree.
- Shows the status messages with the results for the check-in and the refresh.
- The "PLC_Variables" folder is displayed when tags have been marked for the check-in.

  Clicking on the tag table in the bottom window in the detail view shows the tags marked for check-in.
- The "Library objects" folder is displayed when library elements have been marked for the check-in.

  If the folder is selected, the selected library objects are displayed in the detailed view.
- The "Deleted objects" folder is displayed when objects were deleted in the local session.

  If the folder is selected, all objects that were deleted in the local session are displayed in the detailed view.

**5. Detailed view**:

Shows information on lower-level elements (in this case, the selected PLC tags) and status messages.

> **Note**
>
> **Updating the detailed view**
>
> To ensure that no changes have been made in the meantime to the displayed objects by other users, you update the display again before the check-in.
>
> Updating displays the current processing state of the objects.

> **Note**
>
> **Procedure for working with the multiuser editor**
>
> The procedures for working with the multiuser editor are described in detail in the sections below.

### Multiuser editor in the "Refresh" view

#### Introduction

You can call the multiuser editor in the "Refresh" view with the "Refresh local session" button in the Multiuser Engineering toolbar.

> **Note**
>
> **Displaying in the multiuser editor**
>
> If you have opened the multiuser editor and simultaneously make changes in your local session, these changes are only visible in the open editor after a "Refresh".
>
> To do this, click the "Refresh" button (circular arrow) in the open editor.

#### Multiuser editor in the "Refresh" view

The figure below shows an example of the multiuser editor in the "Refresh" view:

![Multiuser editor in the "Refresh" view](images/104618957835_DV_resource.Stream@PNG-en-US.png)

#### Structure of the multiuser editor

The multiuser editor has the following structure:

**1. Toolbar**:

Displays following buttons:

- On the right side, the button for saving the layout settings.
- On the left side, the button "Collapse all", "Expand all" and "Show conflicts".

  When you click "Show conflicts", all selections with "Conflict" (red flag) are displayed in the editor.

**2. Button area:**

Shows the multiuser-specific buttons for the check-in and refresh.

**3. Comment line:**

The comment line is only available in the "Check-in" view.

Here you can enter a comment to document the changes made in the local session.

**4. Working area:**

Shows the change view prior to refresh.

- Shows all objects marked in the local session for refresh as these are also displayed in the project tree.
- Shows the status messages with the results for the refresh.
- The "PLC_Variables" folder is displayed when tags have been marked for the check-in.

  Clicking on the tag table in the bottom window in the detail view shows the tags marked for check-in.
- The "Library objects" folder is only displayed when library objects were marked for the check-in.

  If the folder is selected, the selected library objects are displayed in the detailed view.
- The "Deleted objects" folder is only displayed if objects were deleted in the local session.

  If the folder is selected, all objects that were deleted in the local session are displayed in the detailed view.

**5. Detailed view**:

Shows information on lower-level elements (in this case, the selected PLC tags) and status messages.

> **Note**
>
> **Procedure for working with the multiuser editor**
>
> The procedures for working with the multiuser editor are described in detail in the sections below.

## Notes on working with the TIA Project Server

This section contains information on the following topics:

- [Introduction to the project server](#introduction-to-the-project-server)
- [Set network profiles for project server](#set-network-profiles-for-project-server)
- [Adding a new server connection to the project server](#adding-a-new-server-connection-to-the-project-server)
- [Display server connection](#display-server-connection)
- [Edit server connection](#edit-server-connection)
- [Restore server connection](#restore-server-connection)
- [Delete server connection](#delete-server-connection)

### Introduction to the project server

#### Introduction

The TIA Portal enables you to work conveniently with the TIA Project Server, hereinafter referred to as "Project Server".

You can use the functionality of the project server for working with Multiuser Engineering, with Multiuser Commissioning and with Exclusive Engineering.

In addition to the dedicated project server, a local project server with limited functionality is also available.

Using the project server, you manage the server projects and server libraries that you edit with Multiuser Engineering and Exclusive Engineering in the respective local sessions.

#### TIA Project Server: Installation

You can install the TIA Project Server from V1.0 as follows:

- Standalone via an independent installation process without the TIA Portal.
- As part of the TIA Portal installation.

  When installing with TIA Portal, the TIA Project Server version released for this purpose is always installed.

  TIA Project Server versions that are released afterwards are also released for this TIA Portal version as long as there are no new TIA Portal versions.

  Information for which TIA Portal versions a TIA Project Server version is released can be found in this section:

  "[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)"

The installation of the server requires specific ettings in the Windows firewall and may require a certificate.

You need administrator rights to install and configure the project server.

After the installation, you configure the project server using the Power-Tools and start the server.

More information:

- "[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)"
- "[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)"

#### Properties of the project server

The project server has the following properties:

- The project server is configured and administered by an administrator with the supplied power tools.
- The project server is available to all editors of a server project or a server library depending on their rights and it can also be accessed from the outside.
- The project server can be started and administered outside the TIA Portal.
- You configure and manage the connections from the project server to TIA Portal via the settings in the TIA Portal.

  In the TIA Portal, call the settings for the project server via the command "Options &gt; Settings &gt; Project server".
- The "alias" assigned as the name for the project server is used as an identifier and may not be changed at a later point in time.

#### Microsoft system account for project server

When the project server is installed, a Microsoft system account is created for the project server.

Microsoft changes the password cyclically for this account.

If the password for this account has expired, the password needs to be changed and then the project server needs to be restarted.

#### Quantity structure for the project server

To work efficiently with the project server, you can create up to 100 server connections.

When you have reached this number, you receive a message informing you that you cannot create any new server connections. Once you have deleted any server connections that are no longer required, you can once again create new connections up to the maximum number.

The following configuration limits are available for a project server depending on the respective hardware:

| Projects/libraries and revisions on the project server | Standard project server (use as temporary project server)  Hardware:   **Field PG M5 Advanced (or equivalent)**    **Intel® Core™ i5-6440EQ up to 3.4 GHz·,16 GB RAM (32 GB for large projects)**    **SSD with 50 GB of available disk space**    **Network 1 GBit**    **15.6" Full HD Display (1920 x 1080)** |
| --- | --- |
| Maximum number of server projects and server libraries per server: | 1000 |
| Maximum number of groups per server: | 1000 |
| Maximum number of active projects and libraries per server | 100 |
| Maximum number of active work areas per project | 63 |
| Maximum number of parallel load processes per server | 10 |
| Maximum number of saved revisions per server | Unlimited, number can be configured  Default setting = 10  Ensure there is sufficient memory space to save the revisions. |

> **Note**
>
> **Server hardware**
>
> When more powerful server hardware is used, even higher quantities are possible.
>
> To improve performance, use few folders for the storage structure of the administered projects. The more folders you use for the storage of projects and their objects, the more work memory is in use.

---

**See also**

[Display server connection](#display-server-connection)
  
[Edit server connection](#edit-server-connection)
  
[Delete server connection](#delete-server-connection)
  
[Set network profiles for project server](#set-network-profiles-for-project-server)
  
[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)
  
[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)
  
[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)

### Set network profiles for project server

#### Introduction

You can select between three different network profiles, depending on the performance capability of your own network.

The selected network profile determines the time until a timeout message is generated.

#### Available network profiles

The following network profiles are available for working with the project server:

| Network profile | Area of application |
| --- | --- |
| "Fast" | - Office environment - Gigabit-Ethernet - Stable and mostly interference-free network environment |
| "Medium" | - Office environment, small workgroup with fixed location - Fast Ethernet, WLAN, VPN connections - Good network environment, rare interference |
| "Slow" | - Commissioning, non-stationary workstations - WLAN connection - Interference possible (machines, electrical installations) |

#### Network profiles and compression for the project server

You have the option to select from the drop-down list the required network profile that matches the performance capability of the network you are using.

The selected network profile determines the time until a timeout message is generated.

Setting the network profile to "Middle" or "Slow" activates compression for the data transfer.

No compression is used for the network profile "Fast".

> **Note**
>
> A change to the network profile only takes effect after a restart of the multiuser client or the project server.

#### Set network profiles

To set the network profiles for the project server in TIA Portal, follow these steps:

1. In TIA Portal, select the command "Options &gt; Settings &gt; Project server".

   The settings displayed below contain the available options for the network profiles.
2. From the drop-down list for "Network profiles", select the desired profile.
3. Restart either the Multiuser client or the project server so that the changes to the network profile can be applied.

#### Result

The selected connection profile is activated.

The compression is activated depending on the profile selected.

> **Note**
>
> The timeout behavior of the current network profile is not affected at the changeover.

### Adding a new server connection to the project server

#### Introduction

After the installation of the project server, you can add up to 100 server connections to the project server in the TIA Portal.

#### Requirement

The TIA Portal and a project server are installed.

The project server must be configured and started with the help of the Configuration and Administration Tools.

More information:

- "Working with the TIA Project Server &gt; Configuring and managing the project server &gt; Using graphical tools &gt; [Configuring the project server with the Configuration Tool](Working%20with%20the%20TIA%20Project-Server.md#configuring-the-project-server-with-the-configuration-tool)"

#### Adding a new server connection to the project server

To add a new server connection, follow these steps:

1. In the TIA Portal, select the command "Options &gt; Settings &gt; Project server".

   The "Project server" tab is opened.

   All available server connections are displayed under "Connection".

   If no server connection has been configured yet, only the entry for the "Local project server" is available.
2. To add a new server connection, click in the first free line of the "Server name" column with the entry "Add server connection".

   Alternatively, select the command in the shortcut menu of the table cell.

   The "Add new project server connection" dialog opens.

   If the maximum number of 100 server connections has already been reached, you receive a message informing you that you first have to delete one of the existing server connections before you can add a new one.
3. Enter the path to the host and the port number in the "URL" field, for example:

   - https://&lt;computer name&gt;:&lt;port number&gt;/

   If possible, select "https" as the transmission protocol to ensure secure data exchange with encryption and certificate.
4. Enter the name for the server connection in the "Server name" field.

   You can use a maximum of 256 characters for the name and the path.

   The name can include letters, characters, numbers and commas.

   You will be notified if the entered name is already being used or if the path is longer than 256 characters in total.
5. Click "Add".

#### Result

The new server connection is added and displayed under "Options &gt; Settings &gt; Project server".

### Display server connection

#### Introduction

When you are working with the project server, you can display the existing server connections to the project server in the settings of the TIA Portal.

#### Requirement

The TIA Portal and a project server are installed.

The project server must be configured and started with the help of the Power Tools.

#### Displaying the multiuser server connection

To display the existing server connections, follow these steps:

1. In the TIA Portal, select the command "Options &gt; Settings &gt; Project server".

   All existing server connections are listed under "Connection".
2. Click the "Server name" or "Host" column headers to sort the contents and search for a specific server connection.

#### Result

The existing servers are displayed in the editor under "Options &gt; Settings &gt; Project server"

### Edit server connection

#### Introduction

When you are working with the project server you can edit the existing server connections to the project server and add new server connections in the settings of the TIA Portal.

> **Note**
>
> **Close local sessions**
>
> It is not permitted to edit a multiuser server connection that is used in a currently open local session.

#### Requirement

The TIA Portal and a project server are installed.

The project server must be configured and started with the help of the Power Tools.

#### Editing the multiuser server connection

1. In the TIA Portal, select the command "Options &gt; Settings &gt; Project server".

   All existing server connections are listed under "Connection".
2. Click the "Server name" or "Host" column headers to sort the contents.
3. Double-click the server connection that you wish to edit.

   Alternatively, select the "Edit server connection" command from the server connection shortcut menu.

   Result: The "Edit server connection" dialog opens.
4. Enter the changed URL here.

   If possible, select "https" as the transmission protocol to ensure secure data exchange with encryption and certificate.

   The "Server name" field cannot be edited.
5. Click "OK" for the changes to become effective.

#### Result

Your changes for the selected server connection are applied and displayed under "Options &gt; Settings &gt; Project server".

### Restore server connection

#### Introduction

When you are working with Multiuser Engineering the existing server connection to the project server can be interrupted.

If this is the case, you will receive a corresponding error message after about 30 seconds.

You have different options, depending on whether you are working in the local session or in the server project view.

You have the following options when you are working in the local session:

- Restore the server connection
- Save and close the local session
- Close the local session without saving

You have the following options when you are working in the server project view:

- Restore the server connection
- Discard changes

#### Possible procedure in the local session

To restore a project server connection, follow these steps:

1. Click "Restore" in the displayed dialog.

   If the server connection can be restored, the dialog closes and you can continue working without restrictions.
2. Click "Save and close the local session", if you are not continuing to work at the moment but want to save your changes.
3. Click "Close local session", if you want to exit the local session without storing it.

#### Possible procedure in the server project view

To restore a project server connection, follow these steps:

1. Click "Restore" in the displayed dialog.

   If the server connection can be restored, the dialog closes and you can continue working without restrictions.
2. Click "Discard changes", if you exit the server project view without saving it and want to discard any changes you may have made.

   The server project view closes.

### Delete server connection

#### Introduction

When you are working with Multiuser Engineering you can delete the existing server connections to the multiuser server in the settings of the TIA Portal.

You can create, edit and delete up to 100 multiuser server connections in the TIA Portal.

> **Note**
>
> **Close local sessions**
>
> Keep in mind that you can only delete a server connection if all existing local sessions for this server connection are closed beforehand.
>
> A connection from a local session to a deleted multiuser server connection is then no longer possible.

#### Requirement

You have installed TIA Portal and a multiuser server.

The multiuser server must be configured and started with the help of the multiuser tools.

#### Deleting the multiuser server connection

To delete an existing multiuser server connection, follow these steps:

1. In the TIA Portal, select the command "Options &gt; Settings &gt; Multiuser".

   All existing server connections are listed under "Connection".
2. Click the "Server name" or "Host" column headers to sort the contents.
3. Select one or more server connections that you wish to delete and click "Delete" in the shortcut menu.

   The "Delete" dialog box opens.
4. Click "Yes" to confirm the next message and to delete the selected server connection permanently.

#### Result

The selected multiuser server connection is deleted and is no longer displayed under "Options &gt; Settings &gt; Multiuser".

## Working with the local project server

This section contains information on the following topics:

- [Introduction to the local project server](#introduction-to-the-local-project-server)
- [Configuring the local project server](#configuring-the-local-project-server)
- [Displaying Local project server](#displaying-local-project-server)
- [Starting the local project server](#starting-the-local-project-server)
- [Exiting the local project server](#exiting-the-local-project-server)

### Introduction to the local project server

#### Introduction

To work with Multiuser Engineering , you need a project server that manages your multiuser projects and libraries.

A local project server is always installed automatically together with the installation of TIA Portal and cannot be deleted. It does not require a separate software installation.

The local project server is displayed as the first entry in the list of server connections in all languages under the name "Local Project Server", which cannot be changed. You open the list of server connections via the command "Options &gt; Settings &gt; Project server".

#### Advantages of the local project server

The local project server offers the following advantages:

- You can try out Multiuser Engineering without having to install a dedicated project server first.
- You can buffer your work progress on the local project server.
- You do not require a multiuser license to work with the local project server.

#### Requirement

TIA Portal must be installed before you can use the functionality of the local project server.

#### Properties of the local project server

Unlike a dedicated project server, the local project server offers only limited functionality.

The local project server has the following properties:

- It is only available to one user on their computer and cannot be deleted.
- It can only be started within the TIA Portal.
- It can only be called from the computer on which the local session is running that is assigned to this local project server.
- It does not support management tasks.
- Its settings do not have to be adapted for the firewall and it does not need certificates.
- Only the port can be edited; the server name and host cannot be changed.

---

**See also**

[Configuring the local project server](#configuring-the-local-project-server)
  
[Displaying Local project server](#displaying-local-project-server)
  
[Starting the local project server](#starting-the-local-project-server)
  
[Exiting the local project server](#exiting-the-local-project-server)

### Configuring the local project server

#### Introduction

A local project server is installed by default during installation of the TIA Portal by default.

It is displayed in the list of the servers as the first entry. To display the server list in the "Connections" field, select the command "Options &gt; Settings &gt; Project server".

> **Note**
>
> **No configuration at opened local sessions**
>
> It is not permitted to configure the local project server while it is connected to an open local session.
>
> If a local session has already been created and the local project server is only reconfigured afterwards, the server must first be stopped and then restarted to prevent the existing local session from becoming invalid.

#### Requirement

You have installed the TIA Portal.

#### Configuring the local multiuser server

To configure the local project server, follow these steps:

1. In the TIA Portal, select the command "Options &gt; Settings &gt; Project server".

   All existing servers are displayed under "Connections".
2. Click the "Server name" or "Host" column headers to sort the contents.
3. Position the mouse pointer in the "Local Project Server" line and select the "Edit server connection" command in the shortcut menu.

   - The "Server name" field cannot be edited.
   - If necessary, change the entry in the "URL" field.

     Add the desired port to the URL:

     &lt;computer name&gt;:&lt;port number&gt;.
4. Click "OK" for the changes to become effective.

**Result**

Your changes to the local project server are applied and displayed under "Options &gt; Settings &gt; Project server" under "Connections".

> **Note**
>
> **Local Project Server**
>
> The local project server cannot be deleted.
>
> The local project server is displayed with the uneditable server name (alias) "Local Project Server" in all languages.

---

**See also**

[Exiting the local project server](#exiting-the-local-project-server)

### Displaying Local project server

#### Introduction

A local project server is installed by default during the installation of the TIA Portal.

#### Requirement

You have installed the TIA Portal.

#### Displaying project servers

To display the local project server, follow these steps:

1. In the TIA Portal, select the command "Options &gt; Settings &gt; Project server".

   The local project server is displayed first under "Connection".

   The dedicated project servers you have created are listed below.

   If the local Project server is not displayed as the first entry, click on the "Server name" column to sort the displayed entries.

> **Note**
>
> **Local Project Server**
>
> The local project server cannot be deleted.
>
> The local project server is displayed with the uneditable server name (alias) "Local Project Server" in all languages.

### Starting the local project server

#### Introduction

A local project server is installed by default during the installation of the TIA Portal.

The local project server is displayed as the first entry in the list of server connections. You open the list of server connections via the command "Options &gt; Settings &gt; Project server".

#### Starting the local project server

To start the local project server, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".

   The "Server projects" dialog box opens.

   Alternatively, on the "Libraries" task card, click the "Manage server global libraries" icon in the toolbar of the "Global libraries" pane.

   The "Manage server libraries" dialog opens.
2. In the "Select server" box, select the local project server from the drop-down list.

   It is displayed under the name "Local Project Server".

   - Any existing server projects or server libraries are listed here.

     The individual columns include detailed information relating to path and date of change.

     If required, you can change the arrangement of the columns.
   - If the local project server has not yet been started, you will be asked if you want to start it now.
   - You will be informed if a connection to the selected server is not possible.
3. Confirm the next query as to whether the local project server is to be started on your computer with "Yes".

#### Result

The connection to the local project server is being established.

A command window opens and shows that the server is now activated.

> **Note**
>
> **Stopping the local project server**
>
> Although the connection to the local Project server is terminated by closing the TIA Portal, this server is not stopped automatically.
>
> To stop the local project server, close the DOS window with the command line displayed.

#### Local project server: Open assigned local session

As soon as you open a local session that is assigned to the local project server and when the local project server has not been started, you are asked if you want to start the local project server.

If you answer this query with "Yes", the local Project server is started and the local session is opened for editing.

You cancel the process with "No".

> **Note**
>
> **Deleting a server connection**
>
> Please note the following:
>
> - Keep in mind that you can only delete a server connection if all existing local sessions for this server connection are deleted beforehand.
> - Keep in mind that a connection from an existing local session to a deleted server project is no longer possible.

### Exiting the local project server

#### Introduction

When you open a local session that is assigned to the local project server, a prompt appears asking whether the local project server is to be started.

When the local session is ended or the TIA Portal is closed, the local Project server is not automatically ended.

The local project server must be explicitly ended.

#### Requirement

The local project server was started.

#### Procedure

To end the local project server, follow these steps:

1. Close the local project server by closing the window with the command line displayed.

#### Result

The connection to the local project server is terminated.

The local project server is stopped.

> **Note**
>
> **Closing TIA Portal does not terminate the project server**
>
> Although the connection to the local Project server is terminated by closing the TIA Portal, this server is not stopped automatically.
>
> To stop the local project server, close the DOS window with the command line displayed.

## Creating and managing server projects and server libraries

This section contains information on the following topics:

- [Requirements for server projects](#requirements-for-server-projects)
- [Introduction to working in server projects and server libraries](#introduction-to-working-in-server-projects-and-server-libraries)
- [Create a new server project](#create-a-new-server-project)
- [Managing global libraries as server libraries](#managing-global-libraries-as-server-libraries)
- [Deleting server projects and server libraries](#deleting-server-projects-and-server-libraries)
- [Export server projects and server libraries](#export-server-projects-and-server-libraries)
- [Import server projects and server libraries](#import-server-projects-and-server-libraries)
- [Upgrading server projects and server libraries](#upgrading-server-projects-and-server-libraries)

### Requirements for server projects

#### Introduction

To work with Multiuser Engineering simultaneously and in parallel, it is very important that the server project that serves as the work basis is clearly structured.

#### Requirements for server projects

To create multiuser capable server projects, start with a single-user project that fulfills the following requirements:

- The project already includes the hardware configuration with all required connections.
- Divide the user program into program parts that are independent of each other.
- Create a useful, technology-oriented project structure with folders and groups for the objects to be edited by the individual users.
- When structuring the project, make sure that multiple users can work with the different project directories simultaneously and exclusively.

  Example: One user edits the blocks in group 1 while another user simultaneously edits the blocks in group 2.
- Use a main OB and a central FB or FC for each program part which calls the functions of the subprogram.
- If possible, create a separate PLC tag table for each group.
- You should define in advance all needed project languages that are to be used by the engineering systems involved.
- Create all connections that are to be edited in the multiuser project.
- Define the screen resolution and specify the size of the HMI screens.
- Use global data blocks to save the data for the individual program parts, no bit memories.
- When you load a single-user project created according to these rules to a project server, the project becomes a server project.
- Edit the defined objects of the server project simultaneously with multiple users in the local sessions.

  When you create new objects in the local sessions, make sure that you use different symbolic names.
- Overarching changes, such as to the device configuration, are configured either in the server view in the server project, in an exclusive local session ("Exclusive Engineering"), or in the "Exclusive Multiuser mode" in a local multiuser session.
- If required, configure one or more "Global libraries" as multiuser server libraries.

  You work with the local sessions of a server library in the same way as with local sessions of a server project.

  Objects which you manage in a multiuser server library, are available to the users independent of the local sessions of the server project.

#### Example of a server project for multiple users

The figure below shows an example of a server project for multiple users with a clear structure that permits parallel editing of individual objects in the context of Multiuser Engineering.

Each program part contains a "main FB", which calls the specific lower-lever functions for this program part.

The program parts edited by the individual Engineering Systems are:

- Program part 1: "Conveyer"
- Program part 2: "Drill"
- Program part 3: "FurtherProgramPart"

In the "Conveyer" program part, the "ConveyerMainFB" calls the "ConveyerStartupFC" function.

![Example of a server project for multiple users](images/60248928779_DV_resource.Stream@PNG-en-US.png)

### Introduction to working in server projects and server libraries

#### Introduction

Once the project server has been installed and then configured and started with the help of the Power Tools, you can manage the server projects and server libraries in your TIA Portal.

#### Managing server projects and server libraries

When you execute the command "Project &gt; Project server &gt; Manage server projects", all server projects and local sessions for the existing server connections are displayed.

To display the server libraries open the "Managing server libraries" editor. On the "Libraries" task card, click the "Manage server global libraries" icon in the toolbar of the "Global libraries" pane: ![Managing server projects and server libraries](images/159368230923_DV_resource.Stream@PNG-de-DE.png)

From the drop-down list in the top part of the dialog, select the required server connection. In the table window the existing server projects or server libraries and the associated local sessions are listed.

If you have not added a server project or no global library yet, the list is empty. If server projects or server libraries have already been created, they are displayed.

You can perform the following actions:

|  |  |  |
| --- | --- | --- |
| "Select server": | Drop-down list | Contains the list of the created server connections. |
| "Update" | Icon | Updates the display in the dialog. |
| "Manage server" | Button | Opens the "Project server" view in the project settings.  Alternatively, in the shortcut menu of the table window select the entry "Manage project server". |
| "Add project to server" | Table window:  "Projects" column | Opens the "Add project to the project server &lt;Name of the server connection&gt;" dialog box.  Alternatively, in the shortcut menu of the table window select the entry "Add project to project server".  You have the following options:  - Adding a TIA Portal project as a new server project to the server connection - Add an existing server project - "Server project name" field: Enter new names for the server project - "Comment" field: Add information to the server project |
| "Add the global library to the server" | Table window:  "Global libraries" columns | Opens the "Add global library to project server &lt;Name of the server connection&gt;" dialog box.  Alternatively, in the shortcut menu of the table window select the entry "Add global library to project server".  You have the following options:  - Adding a "Global library" as a new server library to the server connection - Adding an existing server library - "Server library name" field: Entering new names for the server library - "Comment" field: Adding information about the server library |
| "Create local session" | Add dialog:  Check box | Creates a new local session when adding the server project or the server library. |
| "Add" | Add dialog:  Button | Add the new server project or the new server library. |
| "Cancel" | Add dialog:  Button | Cancels the action and closes the dialog. |
| "Add project to the group" | Table window:  "Projects" column | If you have created a group in the administration tool, further server projects can be created in the selected group. |
| "Add global library to group" | Table window:  "Global libraries" columns | If you have created a group in the administration tool, further server libraries can be created in the selected group. |
| "Create new local session" | Table window: "Projects" / "Global libraries" column | Creates a new local session under the opened server project or under the server library.  Alternatively, in the shortcut menu of the server library or the server project select the entry "Create new local session".  The shortcut menu of a local session offers further functions:  - Opening a local session - Delete local session - Removing the lock and deleting an exclusive session - Exporting as a single-user |
| "Open" | Button | Opens the selected local session. |
| "Close" | Button | Closes the dialog and applies the changes. |

> **Note**
>
> **Displaying server projects and server libraries**
>
> Server projects and server libraries can only be displayed if a connection to the project server exists and it has been started.
>
> You will be notified if a connection could not be established.
>
> **Deleting server projects and server libraries**
>
> To prevent inconsistencies in the project management, server projects and server libraries must not be deleted "manually" using the Explorer in the storage directory.
>
> Server projects and server libraries must always be deleted using the Power Tools.
>
> All associated local sessions must be deleted before a server project or a server library can be deleted.

#### Columns in table window

To show or hide columns in the table window, select the entry "Show/hide" or "Display all columns" in the shortcut menu of any column header.

- Projects / Global libraries
- Version
- Path
- Computer name
- Date of change
- Last changed by
- Created by
- Revision

---

**See also**

[Create a new server project](#create-a-new-server-project)

### Create a new server project

#### Introduction

When working with a project server, you must first create a server project.

A Server project is created by adding a standard project (single-user project) to the previously installed Project server and then be able to use this project as a Server project.

> **Note**
>
> **Server projects**
>
> Observe the requirements described under [Requirements for server projects](#requirements-for-server-projects), which a multiuser project has to fulfill.

#### Requirement

The TIA Portal and a project server are installed.

You have created a server connection for the project server.

#### Procedure

To create a Server project, follow these steps:

1. In TIA Portal, click the menu command "Project &gt; Project server &gt; Manage server projects".

   The "Manage server projects" dialog box opens.
2. Double-click in the "Projects" column in a field with the entry "Add project to the server".

   Alternatively, in the shortcut menu of the table window select the entry "Add project to project server".

   The dialog "Add project to project server &lt;Name of the server connection&gt;" opens.
3. Navigate via the button "..." to the source path of the single-user project which you want to add as a server project.

   Select the project file.
4. In the "Comment" field add information on the server project, if required.

   The information under "Project name" and "Published by" are always preassigned and cannot be edited.
5. If necessary, enter a new name for the server project.
6. To create a local session for the newly added server project at the same time as adding it, activate the button "Create local session".
7. Click "Add".

   If the selected project already exists as server project or is currently opened by another user, you will be notified.

#### Result

The selected single-user project is added as new Server project and displayed under "Project &gt; Project server &gt; Manage server projects".

If the option "Create local session" was selected, a new local session is created and opened.

---

**See also**

[Requirements for server projects](#requirements-for-server-projects)

### Managing global libraries as server libraries

#### Introduction

To use a "Global library" in Multiuser Engineering, create a server library.

The procedure is comparable with the creation of a server project:

- You create a global library and configure it as a server library under a server connection.

  The global libraries supplied in the TIA Portal cannot be configured as server libraries.
- For a server library create local sessions in which users work in a distributed manner.

  You load the changes of the local session via the "Check in" in the server library.

  With "Refresh" you apply the current status of the server library in the local session.
- You manage the server library independently of the server projects in the editor "Manage server libraries".
- You can use server libraries both in single-user projects as well as in the local sessions of server projects.

#### Requirement

The TIA Portal and a project server are installed.

You have created a server connection for the project server.

You have created a global library.

#### Procedure: Creating a server library

To create a server library, follow these steps:

1. Open the "Libraries" task card in TIA Portal.
2. Click the "Manage server global libraries" icon in the toolbar of the "Global libraries" pane: ![Procedure: Creating a server library](images/159368230923_DV_resource.Stream@PNG-de-DE.png)

   The "Manage server libraries" dialog opens.
3. If applicable, confirm the query whether the project server is to be started.
4. Under "Select server", select the server connection under which the global library is to be added.
5. Double-click in the "Global libraries" column in a field with the entry "Add the global library to the server".

   Alternatively, in the shortcut menu of the table window select the entry "Add global library to project server".

   The "Add global library to project server &lt;Name of the server connection&gt;" dialog opens.
6. Navigate via the button "..." to the source path of the global library which you want to add as a server library.

   Select the library file.
7. In the "Comment" field add information on the server library, if required.

   The information under "Server library name" and "Published by" are always preassigned and cannot be edited.
8. If applicable, enter a new name for the server library.
9. If you want to create a local session for the newly added server project, enable the "Create local session" button.
10. Click "Add".

    If the selected library already exists as a server library or is currently opened by another user, you will be notified.

#### Result

The selected global library is added as a new server library and displayed in the "Manage server libraries" dialog.

If the option "Create local session" was selected, a new local session is created and opened.

---

**See also**

[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)

### Deleting server projects and server libraries

#### Introduction

Once the project server has been installed and then configured and started with the help of the Power Tools, you can manage the server projects and server libraries in TIA Portal.

Server projects and server libraries can only be deleted via the Power Tools.

You delete a server connection in the TIA Portal under "Tools &gt; Settings &gt; Project Server" using the "Delete" command.

For more details, see: [Adding and deleting a new server connection](Working%20with%20the%20TIA%20Project-Server.md#adding-and-deleting-a-new-server-connection)

#### Requirement

The projects and libraries must not contain any local sessions.

You need administrator rights to configure the project server.

#### Deleting a server project / server library on the project server

To delete a server project or a server library on the project server, proceed as follows.

1. Open the Power Tools as a user interface or via the command line.
2. Use the commands to delete a server project or a server library.

   For more details, see: [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

#### Result

On the project server, the server project or the server library is deleted.

The TIA Portal project is available for further editing without multiuser.

---

**See also**

[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)
  
[Adding and deleting a new server connection](Working%20with%20the%20TIA%20Project-Server.md#adding-and-deleting-a-new-server-connection)

### Export server projects and server libraries

#### Introduction

Once the project server has been installed and then configured and started with the help of the Power Tools , you can manage the server projects and server libraries in TIA Portal.

For the export, use the tool "TIA Project Server - Administration".

Exporting is subject to the following rules:

- The server project or the server library is exported with all contents.
- The details of the local sessions are included in the export.
- The data of the local sessions are not exported.
- A maximum of 5 exports can be executed simultaneously.

See also: [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

#### Exporting a server project / server library

To export a server project or a server library, follow these steps.

1. To open the start menu, click the command "Start" &gt; "All Programs" &gt; "Siemens Automation".
2. To open the Administration Tool, click the entry "TIA Project Server - Administration".
3. In the navigation area on the left, select the server project or the server library that you want to export.
4. At the top right, click the "Export" button.
5. In the next dialog, select the desired storage path for the export and click "OK".

#### Result

The server project or the server library is exported to the target folder in the specified path.

---

**See also**

[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

### Import server projects and server libraries

#### Introduction

Once the project server has been installed and then configured and started with the help of the Power Tools , you can manage the server projects and server libraries in TIA Portal.

For the import, use the tool "TIA Project Server - Administration".

Importing is subject to the following rules:

- The server project or the server library is imported with all contents.
- The details of the local sessions are included in the import.
- The data of the local sessions are not imported because they were not part of the export.
- A maximum of 5 imports can be executed simultaneously.

See also: [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

#### Importing a server project / server library

To import a server project or a server library, follow these steps.

1. To open the start menu, click the command "Start" &gt; "All Programs" &gt; "Siemens Automation".
2. To open the Administration Tool, click the entry "TIA Project Server - Administration".
3. In the navigation area on the left, select the project server into which you want to import a server project or server library.
4. At the top right, click the "Import" button.
5. In the following dialog, select the location for the import.

   Click the folder name and click "OK".
6. After the import, refresh the view in the "Administration Tool" if necessary.

#### Result

The server project or server library has been imported into the project server administration and is displayed in the "Administration Tool".

---

**See also**

[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

### Upgrading server projects and server libraries

#### Introduction

As soon as you try to open a local session that was created with an older version of the TIA Portal with a more recent version of the TIA Portal, you receive a corresponding message.

To use older server projects, server libraries and local sessions with the current version of TIA Portal, these projects and libraries must first be updated.

#### Upgrading server projects and server libraries

To use older server projects and server libraries in the current TIA Portal version, follow these steps:

1. Open the local session with the older version of the TIA Portal with which this local session was created.
2. Make sure that all changes from the local sessions are saved in the associated server project or in the associated server library.
3. Export the server project or the server library with the created version as a single-user project.
4. Open the project or the library with the new TIA Portal version and run the suggested upgrade.
5. Add the upgraded project as a new server project or the current library as a new server library to the current project server.
6. Create new local sessions.

#### Result

The updated server project or the updated library can be edited as usual with Multiuser Engineering.

## Working in the local session

This section contains information on the following topics:

- [Creating and managing a local session](#creating-and-managing-a-local-session)
- [Editing objects in the local session](#editing-objects-in-the-local-session)

### Creating and managing a local session

This section contains information on the following topics:

- [Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
- [Displaying all local sessions](#displaying-all-local-sessions)
- [Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
- [Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
- [Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
- [Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
- [Creating a local session of a server library](#creating-a-local-session-of-a-server-library)
- [Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)
- [Deleting a local session of a server library](#deleting-a-local-session-of-a-server-library)
- [Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)
- [Archiving a local session of a server project](#archiving-a-local-session-of-a-server-project)

#### Creating a local session of a server project

##### Introduction

To work with Multiuser Engineering, you need to create a local session.

The local session is always assigned to a specific server project or a specific server library.

Information on working with local sessions of server libraries:

- "[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)"

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable Server project.

##### Procedure

To create a local session, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".

   The "Manage server projects" dialog box opens.

   The most recently used server project is displayed.
2. In the "Projects" column of the "Manage server projects" dialog, double-click in the cell with the text "Create new local session".

   Alternatively, select the "Create new local session" command in the shortcut menu of the server project.

   The "Create local session" dialog box opens.

   The author for the session is entered by default in this dialog box and cannot be edited.
3. Select the type of local session you want to create:

   - Multiuser Engineering:

     Several editors working in parallel.

     You can temporarily edit the local session as an exclusive local session in the Exclusive Multiuser mode if required.
   - Exclusive Engineering:

     An editor works exclusively in the local session.

     If you close the exclusive local session after finishing editing, it will be deleted automatically.
4. If necessary, change the name of the session.
5. To open the session immediately after it is created, select the "Open local session" option.
6. To create the session, click "Create".

##### Result

The local session is created and displayed in the dialog "Manage server projects" under the selected server project.

##### Changing the type of local session

When the local session is open, the type of local session is displayed as an active icon in the toolbar.

Click the disabled icon in each case to switch between the types of local session.

| Icon | Meaning |
| --- | --- |
| ![Changing the type of local session](images/171998867723_DV_resource.Stream@PNG-de-DE.png) | **Multiuser mode**   The icon is enabled when a local session is open in multiuser mode.  To temporarily switch to the Exclusive Multiuser mode, click the "Exclusive multiuser mode" icon.  Requirements for the change:  - No other session is in progress or locked as an exclusive local session.   Before the mode change, the status of the local session and the server project is checked. If you need to refresh the session or server project before changing the mode, a corresponding message is displayed. |
| ![Changing the type of local session](images/171998863627_DV_resource.Stream@PNG-de-DE.png) | **Exclusive multiuser mode**   The icon is activated when you edit a local session temporarily in the Exclusive Multiuser mode.  To return to multiuser mode, click the "Multiuser mode" icon. After that, other sessions can be opened as exclusive local sessions.  Before the mode change, the status of the local session and the server project is checked. If you need to refresh the session or server project before changing the mode, a corresponding message is displayed. |

---

**See also**

[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Displaying all local sessions](#displaying-all-local-sessions)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)
  
[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)

#### Displaying all local sessions

##### Introduction

You have the possibility to display all local sessions associated with a server project or with a server library in TIA Portal.

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable server project or a server library.

You have created at least one valid local session.

##### Displaying all local sessions

To display all local sessions belonging to a server project or to a server library, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".

   The "Manage server projects" dialog box opens and displays all available server connections for the project server.

   For server libraries you open the dialog "Manage server libraries" via the "Global libraries" pane.
2. Select the server connection you want to use.

   All server projects or server libraries associated with this server connection are listed.
3. Select the required server project or the required server library.
4. Expand the entry to display all associated local sessions.
5. To also display local sessions which were created on another computer, open the multiuser settings via "Options &gt; Settings &gt; Multiuser".

   Activate the option "Show local session created on other systems".

   Open the "Manage server projects" dialog again. To refresh the view, click the icon ![Displaying all local sessions](images/88372482443_DV_resource.Stream@PNG-de-DE.png).

   In the "Computer name" column you can sort according to the computer name.

##### Result

All available local sessions for the server project or the server library are displayed.

To open a local session, double-click the local session or select "Open local session" in the shortcut menu.

---

**See also**

[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)

#### Opening a local session of a server project

##### Introduction

You have different options for opening a local session:

- In TIA Portal with "Recently used projects"
- In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".
- When creating a local session via the dialog "Create local session".
- When TIA Portal is closed with the Microsoft Windows Explorer project.

As soon as you open a local session that is assigned to the local project server, a prompt appears asking if you want to start the local project server, if it has not yet been started.

Click "Yes" to start the local project server and to open the selected local session.

Information on working with local sessions of server libraries:

- "[Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)"

> **Note**
>
> **Instructions for opening local sessions:**
>
> - A renamed or deleted local session can no longer be opened.
> - You can also open a local session as a reference project.
>
> When opening a local session that meets one of the criteria listed above, you will see a note informing you that the session cannot be opened. In this case a prompt asks whether you want to export this local session as single-user project.

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable Server project and a valid local session.

##### Opening a local session

To open a recently used local session, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Open".

   The "Open project" dialog box opens with a list of recently used projects and sessions.
2. Select the preferred local session and click "Open".

**"Open project" dialog: Project icons**

The icons in the first column help you distinguish between single-user projects and multiuser projects.

| Symbol | Meaning |
| --- | --- |
| ![Opening a local session](images/172092479371_DV_resource.Stream@PNG-de-DE.png) | Single-user project |
| ![Opening a local session](images/172092692619_DV_resource.Stream@PNG-de-DE.png) | Multiuser project: Local session (Multiuser Engineering) |
| ![Opening a local session](images/172092701323_DV_resource.Stream@PNG-de-DE.png) | Multiuser project: Exclusive local session (Exclusive Engineering) |

##### Result

The selected local session is opened.

##### Opening a local session by means of the associated server project

To open a local session via the associated server project, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".

   The "Manage server projects" dialog box opens.
2. Select the required project server in the drop-down list.
3. Select the server project required and the local session from the list.
4. To also display local sessions which were created on another computer, open the multiuser settings via "Options &gt; Settings &gt; Multiuser".

   Activate the option "Show local session created on other systems".

   Open the "Manage server projects" dialog again. To refresh the view, click the icon ![Opening a local session by means of the associated server project](images/88372482443_DV_resource.Stream@PNG-de-DE.png).

   In the "Computer name" column you can sort according to the computer name.
5. Double-click the local session and select "Open local session" in the shortcut menu.
6. To open a new local session immediately during creation, activate the "Open local session" in the dialog "Create local session".

##### Result

All opened dialog boxes are closed and the selected local session is opened.

##### Opening a local session with the Microsoft Windows Explorer

To open a local session with the Microsoft Windows Explorer, follow these steps:

1. While TIA Portal is closed, navigate to the directory in which your local sessions are stored in Microsoft Windows Explorer.
2. Select the desired local session with the file extension ".als&lt;version&gt;" and double-click to open it.

##### Result

The TIA Portal is started and the selected local session is opened.

> **Note**
>
> You close a local session as you would a single-user project with the command "Project &gt; Close".

##### Opening a local session from a different storage location

To open a local session that has been moved to another storage location in the meantime, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Open".

   The "Open project" dialog box opens with a list of recently used projects and sessions.
2. Select the preferred local session and click "Open".

   You are notified that you are trying to open a local session from a different storage location.
3. Confirm this query with "OK" if you want to execute the action.

##### Result

The selected local session is opened from the new storage location.

The information about the new storage location is saved in the associated server.

##### Opening a local session without a server connection

A local session can also be opened when the associated server is currently not available.

In this case, when you open the local session, a message informs you that you can continue working offline in the local session with the following restrictions:

- You cannot see the changes made by other operators in your local session.

  Neither yellow or red flags nor "outdated" objects are displayed.
- You cannot check in your changes to the server project until the server connection has been restored.

If you confirm this message with "OK", you can continue working in your local session even without a server connection.

---

**See also**

[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Displaying all local sessions](#displaying-all-local-sessions)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)
  
[Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)

#### Saving a local session of a server project

##### Introduction

You have different options for saving a local session:

- As a "local session" with the file identifier ".als&lt;version&gt;", if you are working with Multiuser Engineering
- After an export as "Single-user project" with the file extension ".ap&lt;version&gt;".

When you export and save a local session as single-user project, you can continue to edit this project in the familiar way without multiuser functionality.

While working in the local session, you save this as usual as local session in order to continue to work in the context of Multiuser Engineering .

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable Server project and a valid local session.

##### Procedure

To save a local session, follow these steps:

1. Open the local session:
2. Make your required changes.
3. In the TIA Portal, select the command "Project &gt; Save".

##### Result

The local session is stored in the associated project server with the file identifier ".als&lt;version number of TIA Portal&gt;".

---

**See also**

[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Displaying all local sessions](#displaying-all-local-sessions)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)
  
[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)

#### Closing a local session of a server project

##### Introduction

You close a local session as you would a single-user project with the command "Project &gt; Close".

Information on working with local sessions of server libraries:

- "[Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)"

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable Server project and a valid local session that is open.

##### Procedure

To close a local session, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Close".
2. Confirm the next prompt with "Yes" if you want to save your changes.

##### Result

The local session is closed.

---

**See also**

[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Displaying all local sessions](#displaying-all-local-sessions)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)
  
[Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)

#### Deleting a local session of a server project

##### Introduction

To avoid inconsistencies in Server projects, you **cannot** delete a local session in the usual way with the command "Project &gt; Delete project...".

Local sessions can only be deleted in the context of the project server and depending on the associated server project.

Information on working with local sessions of server libraries:

- "[Deleting a local session of a server library](#deleting-a-local-session-of-a-server-library)"

> **Note**
>
> If you have manually deleted a local session with the Windows Explorer from the storage directory, it is still displayed in the "Local sessions" dialog box but can no longer be opened.
>
> Delete this local session again explicitly in the multiuser context as described in the procedure below.

Local sessions that exist in the Multiuser server can also be deleted using the Power Tools in the server management.

More information: "Working with the TIA Project Server &gt; Configuring and managing project server &gt; Using command line tools &gt; [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)"

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable multiuser server project and a valid local session.

The local session you wish to delete must not be open.

##### Procedure

To delete a local session in the TIA Portal, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".

   The "Manage server projects" dialog box opens with a list of sessions available for the selected server.
2. Select the required server.
3. Select the required server project from the list and click on the relevant local session that you want to delete.
4. Select the "Delete" command in the shortcut menu.
5. Confirm the next query regarding deletion with "Yes".

**Note**

A local session cannot be deleted if it is open; the delete command is inactive in this case.

In this case, close the local session first and click the "Delete" button once again.

##### Result

The selected local session is deleted and also removed from the list of existing local sessions.

---

**See also**

[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Displaying all local sessions](#displaying-all-local-sessions)
  
[Exporting a local session as a single-user](#exporting-a-local-session-as-a-single-user)
  
[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)
  
[Deleting a local session of a server library](#deleting-a-local-session-of-a-server-library)

#### Creating a local session of a server library

##### Introduction

With local sessions of global server libraries you work in a similar way as with local sessions of the server projects.

The local session is always assigned to a specific server library.

##### Requirement

The TIA Portal and a project server are installed.

You have created a server library.

##### Procedure

To create a local session, follow these steps:

1. Open the "Libraries" task card in TIA Portal.
2. Click the "Manage server global libraries" icon in the toolbar of the "Global libraries" pane: ![Procedure](images/159368230923_DV_resource.Stream@PNG-de-DE.png)

   The "Manage server libraries" dialog opens.

   The server library last used is displayed.
3. Expand the desired server library if necessary.
4. In the "Global libraries" column double-click in a field with the entry "Create new local session".

   Alternatively, select the entry "Create new local session" in the shortcut menu of the server library.

   The "Create local session" dialog box opens.

   The following specifications are preset and cannot be processed:

   - Author: The name of the user who creates the local session is applied.
   - "Contributor session" type for the local session: The setting depends on the server library settings.

     With this local session you use the global library on the server and can add your changes.

     A maximum of 63 contributor sessions are possible per server library.
5. Select the storage location for the local session in the "Path" field.
6. If required, change the name of the local session.
7. To open the local session immediately after it is created, select the "Open local session" option.
8. Click "Create" to create the local session.

##### Result

The local session is created and displayed in the dialog "Manage server libraries" under the selected server library.

---

**See also**

[Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)
  
[Deleting a local session of a server library](#deleting-a-local-session-of-a-server-library)
  
Managing global libraries as server libraries
  
[Managing global libraries as server libraries](#managing-global-libraries-as-server-libraries)
  
[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

#### Opening and closing a local session of a server library

##### Introduction

You have different options for opening or closing a local session:

- Via the dialog "Manage server libraries"
- Via the "Global libraries" pane of the "Libraries" task card

> **Note**
>
> **Renaming or removing a local session**
>
> A renamed or deleted local session can no longer be opened.
>
> When opening you will receive a notification that it cannot be opened.
>
> You can then decide if you want to export this local session as a single-user project.

##### Requirement

The TIA Portal and a project server are installed.

You have created a server library.

You have created one or more local sessions for the server library.

##### Opening a local session

You have different options for opening a local session.

**"Manage server libraries" dialog**

1. Open the "Libraries" task card in TIA Portal.
2. Click the "Manage server global libraries" icon in the toolbar of the "Global libraries" pane: ![Opening a local session](images/159368230923_DV_resource.Stream@PNG-de-DE.png)

   The "Manage server global libraries" dialog opens.

   The server library last used is displayed.
3. If the project server has not been started yet, a prompt appears during opening asking if you want to start the local project server.

   Click "Yes" to start the local project server.
4. If required, select a different server connection in the drop-down list.
5. Expand the required library in the list of the server libraries.

   The associated local sessions are displayed.
6. To also display local sessions which were created on another computer, open the multiuser settings via "Options &gt; Settings &gt; Multiuser".

   Activate the option "Show local session created on other systems".

   Open the "Manage server libraries" dialog again. To refresh the view, click the icon ![Opening a local session](images/88372482443_DV_resource.Stream@PNG-de-DE.png).

   In the "Computer name" column you can sort according to the computer name.
7. Double-click the local session and select "Open local session" in the shortcut menu.

**"Create local session" dialog**

If you activate the "Open local session" option while creating a local session, the session is opened after closing the dialog.

**"Global libraries" pane**

Local sessions which have already been opened once are displayed in the library list of the "Global libraries" pane on the "Libraries" task card.

As soon as you click a local session in the library list, the session is opened. If the project server has not been started yet, a prompt appears asking if you want to start the local project server.

To remove a local library session from the library list, close the local session.

When you close TIA Portal, these library sessions are also closed. When you reopen the TIA Portal, you have to open the library sessions again.

##### Closing a local session

You close a local library session via the "Global libraries" pane on the "Libraries" task card.

- Click the "Close global libraries" icon in the toolbar of the "Global libraries" pane.
- In the library list, select the "Close library" command in the shortcut menu of the local session.

If you have made changes to the global library, select whether or not you want to save the changes.

---

**See also**

[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)
  
[Deleting a local session of a server library](#deleting-a-local-session-of-a-server-library)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)

#### Deleting a local session of a server library

##### Introduction

To avoid inconsistencies it is not possible to delete a local library session via the shortcut menu of the library list in the "Global libraries" pane.

You always delete local sessions in the context of the project server and depending on the associated server library.

Local sessions that exist in the Multiuser server can also be deleted using the Power Tools in the server management.

More information: "Working with the TIA Project Server &gt; Configuring and managing project server &gt; Using command line tools &gt; [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)"

> **Note**
>
> **Do not delete in Windows Explorer**
>
> If you have manually deleted a local session with the Windows Explorer from the storage directory, it is still displayed in the "Local sessions" dialog box but can no longer be opened.
>
> Delete this local session again explicitly in the multiuser context in accordance with the described procedure below.

##### Requirement

The TIA Portal and a project server are installed.

You have created a server library.

The local session you wish to delete must not be open.

##### Procedure

To delete a local session, follow these steps:

1. Open the "Libraries" task card in TIA Portal.
2. Click the "Manage server global libraries" icon in the toolbar of the "Global libraries" pane: ![Procedure](images/159368230923_DV_resource.Stream@PNG-de-DE.png)

   The "Manage server global libraries" dialog opens.

   The server library last used is displayed.
3. If required, select a different server connection in the drop-down list.
4. Expand the required library in the list of the server libraries.

   The associated local sessions are displayed.
5. Select "Delete" in the shortcut menu of the local session.

   When the local session is opened, the delete command is inactive. Close the local session and try again.
6. Confirm the next query regarding deletion with "Yes".

##### Result

The local session is deleted and also removed from the list of existing local sessions.

---

**See also**

[Creating a local session of a server library](#creating-a-local-session-of-a-server-library)
  
[Opening and closing a local session of a server library](#opening-and-closing-a-local-session-of-a-server-library)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

#### Exporting a local session as a single-user

##### Introduction

When working with the project server, you have the option of exporting a local session as a single-user project or a single-user library.

This is beneficial when a local session can currently not be opened, for example, because the project server is not available.

However, a local session may also become invalid and can therefore no longer be opened.

A local session becomes invalid for the following reasons:

- When the local session was renamed.
- When the local session has been moved to a different storage location.
- When the settings for the associated server have been changed and the server is no longer available for this reason.

If a local session is detected to be invalid when opened, you will receive a query as to whether you want to export the session as a single-user project.

This means you can save the work results from the local session in a single-user project and still use them.

You can apply the changes from the exported local session into your server project or in the server library once again by copying them.

You also have the option of exporting a local session with the Project Server Power Tools.

More information: "Working with the TIA Project Server &gt; Configuring and managing the project server &gt; Using command line tools &gt; [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)"

##### Exporting a local session as a single-user

To export a local session as a single-user project or a single-user library, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Project server &gt; Manage server projects".

   The "Manage server projects" dialog box opens and displays all available server connections for the project server.

   To export local sessions of a server library, open the "Manage server libraries" dialog using the "Global libraries" pane.
2. Select the server connection you want to use.

   All server projects or server libraries associated with this server connection are listed.
3. Expand the required server project or the required server library in order to show all associated local sessions.
4. Select the local session and click "Export as single-user" in the shortcut menu.

   The "Export single-user project" dialog box opens.

   The name of the local session and the name of the export file are preset and cannot be edited.
5. Enter the desired export path or navigate to the desired storage location and click "Export".

   If the target directory is not empty, a corresponding message is output to this effect. Select a new, empty target directory and click "Export" again.

##### Result

The local session is exported as a single-user project or single-user library and saved under the set storage path.

You will receive a message that the export has been successfully completed.

If you click "OK", the export dialog box closes and the management dialog is displayed once again.

---

**See also**

[Creating a local session of a server project](#creating-a-local-session-of-a-server-project)
  
[Opening a local session of a server project](#opening-a-local-session-of-a-server-project)
  
[Saving a local session of a server project](#saving-a-local-session-of-a-server-project)
  
[Closing a local session of a server project](#closing-a-local-session-of-a-server-project)
  
[Deleting a local session of a server project](#deleting-a-local-session-of-a-server-project)
  
[Displaying all local sessions](#displaying-all-local-sessions)
  
[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

#### Archiving a local session of a server project

##### Introduction

Local sessions of the current product version can be archived as compressed or uncompressed single-user projects.

Archiving is independent of whether or not you have already transferred the changes you have made in the local session to the server project.

When archiving an open local session, the most recently saved state of the local session is used for archiving.

The local session archived as a single-user project has the file identifier ".zap&lt;version number of TIA Portal&gt;".

Archiving the local session offers the following advantages:

- Daily backup of your local session as a single-user project in TIA Portal.
- Use of the single-user project for testing and commissioning.
- Use of the single-user project as reference project for other projects.

> **Note**
>
> **Archiving local sessions**
>
> When the local session is archived, it is saved as a single-user project and can therefore no longer be used as a local session.

##### Archiving local session

To archive a local session as a single-user project, follow these steps:

1. Select the "Archive ..." command from the "Project" menu.

   The "Archive" dialog opens.
2. In the "Source path" field, the open local session is displayed with the extension ".als&lt;version&gt;" by default.

   You can also use the selection box to select a different local session for archiving.
3. To create a compressed archive file, select the "Archive as compressed file" option.
4. If you do not want to archive the search index and the HMI compile result, select the option "Discard restorable data".

   You can restore the discarded data if needed.
5. To add a date and time automatically, select the "Add date and time to the target name".
6. In the "Target path" field select the directory where you want to save the archive file or the new directory of the project.

   You can set the default directory under "Options &gt; Settings &gt; General &gt; Archive settings &gt; Storage location for project archives".
7. Click "Archive".

##### Result

The local session is archived as a single-user project.

An archive file of the local sessions with the file extension ".zap&lt;version&gt;" is created.

The archive file contains the complete project directory. The individual files of compressed archives are additionally reduced to the essential components to save space.

For uncompressed projects only a copy of the original project directory is created at the desired storage location.

### Editing objects in the local session

This section contains information on the following topics:

- [Introduction to working in local sessions](#introduction-to-working-in-local-sessions)
- [Working offline in the local session](#working-offline-in-the-local-session)
- [Rules for selecting objects](#rules-for-selecting-objects)
- [Marking objects automatically or manually for editing](#marking-objects-automatically-or-manually-for-editing)
- [Possible conflicts during autoselect](#possible-conflicts-during-autoselect)
- [Unmarking objects](#unmarking-objects)
- [Displaying usage info for marked objects](#displaying-usage-info-for-marked-objects)
- [Refresh local session](#refresh-local-session)
- [Restoring the local session after the refresh](#restoring-the-local-session-after-the-refresh)
- [Checking in objects](#checking-in-objects)
- [Possible conflicts during check-in](#possible-conflicts-during-check-in)
- [Possible error messages during check-in](#possible-error-messages-during-check-in)
- [Deleting objects in the local session](#deleting-objects-in-the-local-session)

#### Introduction to working in local sessions

##### Introduction

Within the context of Multiuser Engineering , to work simultaneously with multiple users in a multiuser project, each editor must create their own local session.

The respective editor can make changes in one or more local sessions, check them in to the server project or server library and thus publish them.

After check-in, the changes from the local session are once again available to all editors. They can be reused and modified once again in subsequent local sessions.

You can find detailed instructions on working with local sessions in the sections below.

##### Procedure when working in local sessions

The following steps are necessary to work as multiuser in the engineering tasks that have been assigned to you in a local session:

- The TIA Portal and a project server are installed.
- Alternatively, you can use the local project server installed by default.
- You have created an executable project for working with Multiuser Engineering.
- You have loaded the prepared project to the project server and thus created a server project.
- You have created a server library to work with a global library in multiuser engineering.
- You have coordinated the task and the configuration limits for working in the local sessions with the other editors.
- You have created a local session for each engineering task.

##### Rules for working in local sessions

The following rules apply to working in local sessions:

- A local session is always assigned to a defined project server and a defined server project or a defined server library.
- Each local session includes different tasks for different editors who are assigned to a multiuser server projects.
- A local session has the file identifier ".als&lt;version number of TIA Portal&gt;" when saved.

  In the "Source path" field, the open local session is displayed with the extension ".als&lt;version&gt;" by default.

  The file may not be renamed in Windows Explorer.
- While a local session is open, the associated server connection and the associated server project or server library must not be renamed, moved or deleted.
- Local sessions can no longer be opened and edited when the associated project server or the associated server project or server library have been deleted.
- As of TIA Portal V15, a local session can also be opened without a server connection.

  After confirming a corresponding message, you can continue working offline, that is without a server connection.
- You can also open a local session as a reference project.
- A local session can be exported as single-user project and edited further without multiuser functionality.
- A local session can only be archived or restored as a single-user project.

  You cannot use an archived local session as a local session once it has been restored.
- Working with external tools is not possible in the local session.

  Changes by external tools in local sessions are lost after the local session is checked in and refreshed.

  Permanent changes in the file structure are only possible when working in the Server project view.

  You use external tools that make changes to the file structure of a Server project only in the Server project view.
- User-defined documentation and custom files cannot be changed in the local session.

  Changes to existing user-defined documentation are lost after the local session is checked in and refreshed.

  Permanent changes in the file structure are only possible when working in the Server project view.

  To add files to the user-defined documentation, for example, work in the Server project view.

> **Note**
>
> **Renaming objects in local sessions**
>
> Objects should be renamed only in the server project view, since this does **not** cause any inconsistencies in the server project.
>
> When renaming objects in the local session, you must ensure that all objects affected by the renaming and their places of use are also marked and checked in the server project. Otherwise, you get compiling errors and an inconsistent server project due to partial renaming.
>
> Before checking the places of use of the renamed object, you should be careful not to create conflicts (red flags) when marking and you should not mark any outdated objects; otherwise, you will overwrite the work of another user when checking in.
>
> **Editing library objects in local sessions**
>
> Library objects from project libraries should be edited only in the server project view, since this does **not** cause any inconsistencies in the server project.
>
> With version changes to library objects in the local session, for example, when you create new versions of type instance objects, you must ensure that all relevant objects have been marked with a version change and checked into the server project.
>
> Otherwise, you get compiling errors and an inconsistent server project from creating new versions.

---

**See also**

[Displaying usage info for marked objects](#displaying-usage-info-for-marked-objects)
  
[Unmarking objects](#unmarking-objects)
  
[Checking in objects](#checking-in-objects)
  
[Possible conflicts during check-in](#possible-conflicts-during-check-in)
  
[Possible error messages during check-in](#possible-error-messages-during-check-in)
  
[Working offline in the local session](#working-offline-in-the-local-session)
  
[Rules for selecting objects](#rules-for-selecting-objects)
  
[Marking objects automatically or manually for editing](#marking-objects-automatically-or-manually-for-editing)
  
[Possible conflicts during autoselect](#possible-conflicts-during-autoselect)
  
[Refresh local session](#refresh-local-session)
  
[Restoring the local session after the refresh](#restoring-the-local-session-after-the-refresh)
  
[Deleting objects in the local session](#deleting-objects-in-the-local-session)

#### Working offline in the local session

##### Introduction

When you open a local session , the connection to the associated project server is automatically established.

As of TIA Portal V15, you have the option to work in a local session "offline" without a server connection. Up to V14, you could only work with an active server connection in the local session in the context of Multiuser Engineering .

If a server connection cannot be established when you open the local session, a dialog appears with a corresponding error message.

You are first be asked whether you want to export this local session as single-user project. If you confirm this option with "OK", a follow-up dialog appears informing you that a connection to the server could not be established.

If you also confirm this dialog with "OK", you can work in the local session even without a server connection with the following restrictions:

- Selections made by other users are not visible in your local offline session; no yellow or red flags and no outdated objects are displayed.
- Changes you are making in the local offline session cannot be checked in the server project or in the server library until a server connection is available once again.

> **Note**
>
> **Instructions for opening local sessions:**
>
> - A renamed or deleted local session can no longer be opened.
> - You can also open a local session as a reference project.
>
> When opening a local session that meets one of the criteria listed above, you will see a note informing you that the session cannot be opened. In this case a prompt asks whether you want to export this local session as single-user project.

##### Requirement

The TIA Portal and a project server are installed.

You have created an executable server project or a server library.

You have created at least one valid local session.

##### Opening a local session and working offline

To open a local session, follow these steps:

1. In the TIA Portal, select the command "Project &gt; Open".

   The "Open project" dialog box opens with a list of recently used projects and sessions.

   The icons in the first column help you distinguish between single-user projects and multiuser projects.
2. Select the preferred local session and click "Open".

   For server libraries you open the dialog "Manage server libraries" using the "Global libraries" pane and select "Open local session" in the shortcut menu.
3. If a server connection cannot be established to the associated project server, you receive a corresponding message.

   You are asked whether you want to export this local session as a single-user.
4. Click "OK".
5. A second dialog opens which informs you that a server connection could not be established.

   If you confirm this dialog with "OK", you can continue working in your local session even without a server connection with the restrictions listed above.

##### Result

The selected local session is opened offline.

You do not see any selections made by other users.

You cannot check in your changes until a server connection is available once again.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

#### Rules for selecting objects

##### Introduction

For objects to be edited in Multiuser Engineering at the same time, the objects to be edited must be selected in the local session.

There are two equivalent options for selecting objects:

- As of TIA Portal V15 the "Autoselect" function automatically selects all objects approved for editing.

  This means each permitted "selectable" object in the local session that you create, edit or delete is automatically selected.
- In addition, you can also select objects manually in the local session:

  - With the shortcut menu command "Mark objects for check-in".
  - By clicking the displayed gray flags in the project tree and in the individual editors of the TIA Portal.

  For manual selection of objects, multiple selections are also possible via the shortcut menu.

  A prerequisite for the marking is that the selection includes at least one object that can be marked. If the multiple selection does not include an object that can be marked, the shortcut menu commands are possibly not active.

There are some editing steps (e.g. changes to the HW configuration) that can only be executed in the server project view.

##### Rules for marking objects

The following rules apply to marking:

- The markings and the marking column in the project tree and in the individual editors are only displayed in the context of Multiuser Engineering.
- Objects that can be marked are identified by a gray flag in the project tree and in the editors.
- You can only mark objects that can be edited with Multiuser Engineering.
- If an object does **not** have a gray flag in front of it, this object cannot be marked and it should not be edited in the local session as the changes cannot be checked into the server project.

  Such objects that cannot be marked should be edited in the server project view.
- Some higher-level directories cannot be marked themselves, but the individual objects in the folder can be marked.

  Example: "PLC tag table": The PLC tag table itself cannot be marked, but the individual tags in the open tag table can be marked.
- Autoselect is done by the system when you edit an object that can be selected.
- Manual selection is done by clicking the gray flag or with the shortcut menu.

  The flag is shown in color as soon as an object has been marked.
- The color of the flags provides additional information about the marking:

  | Icon | Meaning |
  | --- | --- |
  | ![Rules for marking objects](images/84845469195_DV_resource.Stream@PNG-de-DE.png) | Object can be marked for check-in. |
  | ![Rules for marking objects](images/82716066059_DV_resource.Stream@PNG-de-DE.png) | Object is marked in own local session. |
  | ![Rules for marking objects](images/84859083659_DV_resource.Stream@PNG-de-DE.png) | Object is marked in a different local session that is part of the same multiuser server project or the same server library. |
  | ![Rules for marking objects](images/84859302027_DV_resource.Stream@PNG-de-DE.png) | Conflict: The object was marked in multiple sessions simultaneously. |

##### Special considerations for autoselect of objects

The following special considerations have to be noted for autoselect:

When working in the different editors of the TIA Portal and changes have been made, the effected objects in the lower-level or higher-level folders are also selected automatically. Some of the actions are listed as an example below.

- Autoselect of objects in Multiuser Engineering works in open editors as well as when working in the project tree.

  - If an object is renamed in the project tree, the new, renamed object is selected automatically.
  - If an object is moved to a different folder within the same device in the project tree, the moved object is selected automatically.
  - If, however, a folder that cannot be selected (e.g. the PLC tag table) is moved to a different location in the project tree, the lower-level objects are **not** selected automatically.
- When working in the project library, all newly created objects are selected automatically. If, however, a complete library folder is moved to a different location in the project tree, the types it contains are **not** selected automatically.
- When working with project texts, the selectable objects to which the project texts belong are selected automatically.

  - Example: In case of changes to a block comment, the associated block is selected automatically so that the changes are applied to the server project during the next check-in.
- When working with PLC message text lists, all changes to texts are selected automatically.

  - If a new entry is created in a text list, the associated text list is selected automatically.
  - If an existing text is edited in a text list, the associated text list is selected automatically.
- When editing PLC supervisions &amp; alarms all changes are selected automatically.

  - If a new entry is added or if existing entries are changed, the changed entry as well as the associated block are selected automatically.
- When editing HMI text and graphic lists all changes are selected automatically. However, the selections are only shown in the higher-level editor.
- When editing HMI tags, only the higher-level tags can be selected.

  - In case of changes to the lower-level tags, the associated higher-level tags are selected automatically.
  - In case of changes in the alarm editor, the alarms associated with these tags are automatically selected but not the tags themselves.
- When editing HMI screens and HMI scripts, there are special considerations regarding autoselect because not all actions performed here result in objects being selected automatically.

  - In case of changes in the script editor, autoselect is only performed when the executed action can be reversed with "Undo".
  - In changes are made to individual elements of a screen, the associated screen is automatically selected.
  - In changes are made to the global filter configuration in the screen properties, these are **not** automatically selected because this configuration is not part of a screen.
- When editing trace and logic analyzer functions, the following actions are **not** automatically selected:

  - Deleting the example OB (OB30) from the programming folder.
  - Changing the cycle time in OB 30.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

#### Marking objects automatically or manually for editing

##### Introduction

For objects to be edited in Multiuser Engineering at the same time, the objects to be edited must be marked in the local session.

There are two equivalent options for selecting objects:

- The "Automark" function which automatically marks the objects edited in the local session.

  As soon as you open, copy, add or delete an object in an editor of the TIA Portal in the local session, this object is automatically marked for check-in.

  This is also true for objects that are created by the system at a lower level during editing by the user (e.g. system blocks, etc.).
- Objects can still be selected manually:

  - With the shortcut menu command "Mark objects for check-in".
  - By clicking the displayed gray flags in the project tree and in the individual editors of the TIA Portal.

> **Note**
>
> **Changes to objects that cannot be marked**
>
> Changes to objects that cannot be marked - these are objects that do not have a gray flag - in the local session are possible but **cannot** be applied to the server project.
>
> These changes are lost after update of the local session, because they are once again overwritten with the contents of the server project.
>
> As soon as you want to edit an object that cannot be marked, a banner text is displayed in the open editor. This banner text contains information on the further procedure.

##### Procedure for automatic selection of objects

To mark objects in a local session automatically, follow these steps:

1. Open the required local session.
2. Edit the required object, for example, by opening, copying, adding or deleting it in an editor.

##### Result

The object is automatically marked during editing and deleting, and the corresponding blue or red flag is set in the own local session.

If a blue flag is displayed, the object can be edited in the local session.

If a red flag is displayed, you have a conflict that has to be resolved through coordination with the other editors.

If an automark conflict occurs when copying or adding objects, you receive an error message. The further procedure is partly controlled by a dialog in which you can select the required option.

##### Procedure for manual selection of objects

To mark objects in a local session, follow these steps:

1. Open the required local session and click on the displayed gray flag to mark an object for check-in.
2. Alternatively, you can select the required object and mark it with the shortcut menu command "Mark object for check-in".
3. Mark all objects in your local session that you currently want to edit.

   You can make multiple selections for marking.

   After marking, you can edit and save the objects as usual.

> **Note**
>
> **Multiple selections**
>
> Once &gt; = 50 objects are selected in the local session, both shortcut menu commands are active simultaneously: the command for marking the objects as well as the command for unmarking.

##### Result

The marked objects are displayed with a blue or red flag.

If a blue flag is displayed, the object can be edited in the local session.

If a red flag is displayed, you have a conflict that has to be resolved through coordination with the other editors.

> **Note**
>
> **Markings with conflict (red flag)**
>
> A marking conflict must be resolved by agreement of the editors, and a sequence for editing the marked objects must be specified.
>
> To solve the conflict, one editor must unmark the objects.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)
  
[Unmarking objects](#unmarking-objects)
  
[Displaying usage info for marked objects](#displaying-usage-info-for-marked-objects)

#### Possible conflicts during autoselect

##### Introduction

For objects to be edited in Multiuser Engineering at the same time, the objects to be edited must be selected in the local session. When automatically selecting objects in the local session, the following conflicts can occur:

- An automatically selected object can be "outdated".

  In this case, it is mandatory that you update the object prior to check-in so that the changes on the Project server can be applied.
- An automatically selected object can already have been selected by other users.

  A red flag is displayed during autoselect in this case and the conflict has to be resolved through coordination with the other editors.

> **Note**
>
> **Markings with conflict (red flag)**
>
> A marking conflict must be resolved by agreement of the editors, and a sequence for editing the marked objects must be specified.
>
> To solve the conflict, one editor must unmark the objects.

##### Displaying conflicts during autoselect

If an autoselect conflict occurs, you receive an error message in the "Info" tab of the Inspector window.

This error message provides information on the action for which the conflict has occurred and which type of conflict you are dealing with.

The further procedure is partly controlled by a dialog in which you can select the required option.

Example of an error message for autoselect:

The "Add new network" operation results in an autoselect conflict because one of the automatically selected objects is outdated.

##### Resolving conflicts during autoselect

All conflicts that might occur during autoselect must be resolved before check-in because there is a risk of loss of data otherwise. Changes are lost or overwritten when you check in outdated objects or objects "selected with conflict". Proceed as follows:

1. If an object is shown as "outdated" during autoselect, you must update this object in the local session prior to check-in and before you edit it further so that the changes on the multiuser server can be applied.
2. If an object is selected with a red flag during autoselect, this object is already being edited by another operator in a different local session.

   Resolve this conflict by having one of the editors manually remove their selection.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

#### Unmarking objects

##### Introduction

For objects to be edited in Multiuser Engineering, these objects must either be selected automatically or manually in the local sessions. The objects marked for check-in can also be unmarked.

This is necessary primarily in a conflict (indicated by a red flag) in which multiple editors have marked the same object for check-in in their respective local session.

> **Note**
>
> **Markings with conflict (red flag)**
>
> A marking conflict must be resolved by agreement of the editors, and a sequence for editing the marked objects must be specified.
>
> To solve the conflict, one editor must unmark the objects.

##### Procedure

To unmark objects in a local session, follow these steps:

1. Open the local session and click on the displayed blue or red flag to unmark an object.
2. Alternatively, you can also select the required object and delete the marking with the shortcut menu command "Unmark".

##### Result

The objects that are no longer marked and objects marked as conflict are displayed as follows:

| Icon before | Action | Icon after |
| --- | --- | --- |
| ![Result](images/82716066059_DV_resource.Stream@PNG-de-DE.png) | Unmark | ![Result](images/84845469195_DV_resource.Stream@PNG-de-DE.png) |
| ![Result](images/84859302027_DV_resource.Stream@PNG-de-DE.png) | Unmark | ![Result](images/84859083659_DV_resource.Stream@PNG-de-DE.png) |

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)
  
[Marking objects automatically or manually for editing](#marking-objects-automatically-or-manually-for-editing)
  
[Displaying usage info for marked objects](#displaying-usage-info-for-marked-objects)

#### Displaying usage info for marked objects

##### Introduction

For objects to be edited in Multiuser Engineering at the same time, each editor must mark the objects they want to edit in their local session.

To avoid multiple marking of objects and any marking conflicts caused by it, you receive the following information for marked objects:

- User: Indicates who has marked the object
- Computer: Indicates on which computer the object was marked.
- Storage location: Indicates where the object was marked: in a local session or in the server project view.

This information helps you coordinate the further procedure for marked objects or objects that are marked with a conflict with the other users.

##### Show usage info

To display the usage info for marked objects, follow these steps:

1. Select a yellow or red marked object in your local session or in the server project view.
2. Call the "Usage info" command from the shortcut menu.

##### Result

The "Usage info" dialog box opens and displays the above-mentioned information for the marked object.

> **Note**
>
> **Markings with conflict (red flag)**
>
> A marking conflict must be resolved by agreement of the editors, and a sequence for editing the marked objects must be specified.
>
> To solve the conflict, one editor must unmark the objects.

---

**See also**

[Multiuser icons in the user interface](#multiuser-icons-in-the-user-interface-1)
  
[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)
  
[Marking objects automatically or manually for editing](#marking-objects-automatically-or-manually-for-editing)
  
[Unmarking objects](#unmarking-objects)

#### Refresh local session

##### Introduction

For objects to be edited at the same time in Multiuser Engineering, these objects must either be selected automatically or manually in the local sessions.

If objects are more recent in the server project or in the server library than in the local session, these objects are identified as "outdated".

You can refresh these objects in the local session by clicking the "Refresh local session" icon in the multiuser toolbar.

Other users may have created new objects or deleted objects in the server project or in the server library that are not yet displayed in your local session.

These new objects are also displayed in your local session after a refresh.

The contents of "outdated" objects in the local session are overwritten with the more recent contents of the server project or the server library during the refresh.

> **Note**
>
> **Refresh local session**
>
> - The button to refresh the local session opens the view "Refresh", even if there are no objects to be refreshed in your local session.
>
>   When you click the "Start refresh" button, the local session is refreshed.
> - During the refresh, all changes to **unmarked objects** in your local session are overwritten with the contents of the server project or the server library.
>
>   The marked objects remain unchanged.
> - You can undo the refresh of the local session if required by clicking the "Restore" button.
>
>   Your local session will then be restored with the contents prior to the refresh.

##### Refresh procedure

To refresh objects in a local session, follow these steps:

1. Open the local session that contains the objects that are to be updated.
2. Click the "Refresh local session" button in the multiuser toolbar.

   The multiuser editor opens in the refresh view and shows all objects marked in your local session.

   - The objects you have marked are not overwritten during the refresh.
   - Unmarked objects are overwritten with the contents of the server project or the server library.
3. Click the "Start refresh" button to start the refresh.

   You are kept up-to-date on the progress of the refresh.

   You will receive an error message if an error occurs.
4. You receive the message that the refresh was completed successfully.

   Click "OK".

##### Result

All unmarked objects in your local session were refreshed.

The objects marked in your local session were not synchronized with the server version.

> **Note**
>
> **Online/offline differences after the refresh**
>
> After downloading to the device, the online information on the loaded objects is stored in the local session in the TIA Portal.
>
> This enables a comparison between the online and offline version.
>
> However, because this online information is not checked in on the server, this information is no longer available in the local session after a refresh.
>
> If you then work online on the device after the refresh, the TIA Portal cannot perform a comparison because of missing information. The objects are displayed with online/offline differences although the contents of the objects are identical.
>
> To correct this, perform a new complete download to the device after a refresh of the local session.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

#### Restoring the local session after the refresh

##### Introduction

Unmarked objects which have a newer version in the server project or in the server library can be updated in the local session.

The unmarked objects in the local session are overwritten with the more recent contents of the server project or the server library during the refresh.

You can undo the refresh of the local session if required:

To do this, click the "Restore" button in the multiuser editor after the refresh. Your local session will then be restored with the contents prior to the refresh.

> **Note**
>
> **"Restore" button**
>
> The "Restore" button is only active after a refresh has been performed as long as a restore of the contents of the local session with the last version is possible.
>
> The "Restore" button is inactive if no restore of the local session can be performed, for example because no refresh was performed.
>
> Closing and opening the editor has no impact on the "Restore" button. If a refresh is available that can be undone, the button is still active even if you close the editor and open it again.

##### Procedure to restore the local session

To restore the local session after the refresh, follow these steps:

1. Open the local session for which you have performed a refresh, if you have closed this in the meantime.

   Start with step 3 if the refresh view is still open.
2. Click the "Refresh local session" button in the multiuser toolbar to open the multiuser editor in the refresh view.
3. Click the "Restore" button to restore the version of the local session before the last refresh.
4. In the next dialog box, click "Yes" to answer the prompt.
5. When errors occur, you receive an error message that you have to acknowledge.
6. When the restore is successfully completed, you receive a message. Click "OK".

##### Result

Your local session was successfully restored with the version before the last refresh.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

#### Checking in objects

##### Introduction

After editing marked objects in the local session, you can check the changes into the server project or in the server library.

The following rules apply to check-in:

- Only changes to selected objects are applied during the check-in.
- If you have edited objects that cannot be selected in the local session, these changes are **not** applied during check-in.
- During the refresh of your local session after the check-in, changes to objects that cannot be selected are overwritten with the contents of the server project or the server library.
- You will receive an error message with additional information if an error occurs during check-in.

  Correct the errors that occurred as specified, either in your local session or in the server project view. Then start the check-in process again.
- During check-in and editing of objects in the Server project view, the respective user works exclusively on the Project server.

  The server is therefore locked for all other users. The server status is shown as "not available" in the toolbar during exclusive editing.

  You can nevertheless create a new local session and refresh local sessions.

##### Options for the check-in

**Compile**

You have the option to compile the changes made in the local session before check-in.

> **Note**
>
> **Options displayed for the compilation during check-in**
>
> The options displayed for the compilation during the check-in depend on the settings made in the TIA Portal under "Options &gt; Settings &gt; Multiuser" for "Compilation settings" .
>
> The compiling options may be deactivated in the multiuser editor based on these settings.

**Compile mode**

The compile mode defines the extent to which the software changes are compiled. You can select the following options from the drop-down list:

- Marked objects (changes only)

  The changes made to the marked objects for the selected device are compiled together with the device-specific objects.
- Device software (changes only)

  The changes made to the marked objects are compiled together with the software version on the assigned devices.

  **Example**: You have marked and changed several objects that belong to more than one device (for example to CPU_1 and to CPU_2). These marked objects are compiled together with the software versions of both CPUs during compiling.

**Display server project view**

When you enable this option, you have the possibility before check-in to again display your changes to the marked objects in the server project view together with the current contents of the server project.

You can mark and edit all objects in the server project view and unmark them.

After this, you can either save your changes in the server project or discard your changes and exit the server project view without further action.

##### Requirement

The connection to the project server exists and the server is available.

You have marked the objects edited in the local session for check-in.

##### Procedure for check-in of changes

To check-in the changes from the local session to the server project, follow these steps:

1. Open the local session that you want to check in.
2. Click the "Check-in" button in the multiuser toolbar.

   The multiuser editor opens in the "check-in" view and shows all objects marked in the local session that are applied to the server project or in the server library during check-in.
3. Open the displayed folders and check the objects displayed and marked for check-in.
4. In the toolbar, click on the button with the red flag to display any conflicts.

   Existing conflicts are displayed. To prevent data loss or unintended overwriting, resolve the displayed conflicts before checking in the project.

   If there are no conflicts, click on this button again to return to the previous "Check-in" view.
5. Select the preferred options for check-in.

   - "Compile": Select the required setting from the drop-down list.
   - "Open server project view": When you click this options, the server project view is opened in the project tree prior to check-in.
6. Enter a comment on the change history to document the changes you have made in the local session.
7. Click "Start check-in" after reviewing to check in the displayed objects.

   - If you have opened the server project view, you can check in your changes with the "Save changes" button.

     If you click "Discard changes", your changes are not applied in the server project.
   - If you want to keep the marking in the local session even after the check-in, you must select the option "Keep markings for objects".
   - If you have marked and checked in only some of your changes, you should perform **no refresh** to retain your changes to the unmarked objects.
8. If check-in was successful, you receive a final message.

   If you confirm this message with "OK", your local session is overwritten with the contents of the server project or the server library.

   If you want to keep your changes to the selected objects, click on the "Keep local session" button in the message.
9. If you want to retain your selections in the local session, select the "Keep markings" check box.
10. If check-in was unsuccessful and aborted due to errors, you receive a corresponding error message.

    Correct the specified errors in your local session or in the server project view.

    Then start the check-in process again.

**Note**

**Updating the detailed view**

To ensure that no changes have been made in the meantime to the displayed objects by other users, you should update the display again before check-in. Updating displays the current processing state of the objects.

##### Result

You receive a message that the check-in was completed successfully.

Your local session is refreshed and opened with the contents of the server project or the server library after successful check-in.

- The local session will include all changes after the refresh that have been checked in into the server project or into the server library in the meantime.
- If new objects were added to the server project or in the server library, these objects are now also visible in your local session.
- If objects were deleted in the server project or in the server library, these objects now no longer exist in your local session.
- Your markings in the local session are automatically deleted if you have not selected the option "Keep marking for objects".
- The server connection is released once again after check-in.

  The server status changes in the display within the toolbar from "busy" to "available".

---

**See also**

[Possible conflicts during check-in](#possible-conflicts-during-check-in)
  
[Possible error messages during check-in](#possible-error-messages-during-check-in)
  
[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)
  
[Introduction to working in the server project view](#introduction-to-working-in-the-server-project-view)
  
[Editing objects in the server project view](#editing-objects-in-the-server-project-view)

#### Possible conflicts during check-in

##### Introduction

Errors can occur during check-in of changes from the local session to the associated server project or the server library that may prevent a successful check-in.

You have the option of displaying existing errors in the multiuser editor prior to check-in.

To do this, click the red flag in the header of the multiuser editor and all conflicts in the local session are displayed. If there are no conflicts, a message to this effect is displayed.

If you want to check in your changes from the local session despite existing conflicts, you must confirm this action explicitly in a dialog because this procedure can result in a loss of data.

The error constellations listed below can be easily avoided through coordination between editors and by observing the recommended procedures.

##### Possible naming conflicts during check-in

Naming conflicts during check-in arise when identical names are used for different objects in different local sessions.

**Example**:

- Editor 1 creates the tag "Motor_1" in their local session.
- Editor 2 also creates a tag "Motor_1" in their local session.

**Result**:

Editor 1 can check in their changes without errors.

Editor 2 **cannot** check in their changes. When they want to check in their changes they receive an error message due to a naming conflict and the check-in is aborted. The error must be removed in the local session.

##### Possible conflicts when creating devices in the local session

If an editor adds new devices with marked objects in a local session, for example, a new CPU with blocks, the result will be a conflict during check-in.

**Example**:

- Editor 1 creates a new CPU with two function blocks in their local session.
- Editor 1 marks the blocks appropriately before editing them.

**Result**:

Editor 1 receives an error message during check-in because the newly created CPU cannot be found in the server project. The transfer of devices is currently not supported in Multiuser Engineering. Check-in is aborted in this case and the server project view opens. Editor 1 can copy their newly created objects directly to the server project. This means the editing work is not lost.

##### Possible conflicts when renaming objects in the local session

Objects should be renamed only in the server project view, since this does **not** cause any inconsistencies in the server project.

When renaming objects in the local session, you must ensure that all objects affected by the renaming and their places of use are also marked and checked in the server project. Otherwise, you get compiling errors and an inconsistent server project due to partial renaming.

Before checking the places of use of the renamed object, you should be careful not to create conflicts (red flags) when marking and you should not mark any outdated objects; otherwise, you will overwrite the work of another user when checking in.

**Server libraries**

This restriction does not apply for library objects of global libraries which were configured as a multiuser server library.

You change these library objects while working in the local library session in the "Global libraries" pane.

##### Possible conflicts when changing the device type in the local session

If a device type is changed in a local session, e.g. a "CPU_1" of the type S7-15xx is replaced or renamed, the objects marked in the "old" CPU may no longer be displayed in the local session.

##### Possible conflicts when deleting devices in the server project

If devices with included objects are deleted in the server project, it may result in a transfer error.

**Example**:

- Editor 1 works in their local session on marked objects that are part of "CPU_1".
- In the meantime, editor 2 deletes "CPU_1" in their server project view and saves the changes in the server project.

**Result**:

Editor 1 receives an error message during check-in because "CPU_1" no longer exists in the server project. In this case, editor 1 can add their edited objects in the server project view. The editor either copies "CPU_1" completely to the server project or they add the edited blocks to an existing CPU in the server project.

##### Possible scenarios during check-in of deleted objects

When you check in objects that are already deleted in the server project or in the server library, these objects are recreated.

**Example:**

- User 1 edits the marked tag "Tag_1" in their local session that is part of a group that includes a tag table with multiple tags.
- User 2 deletes this group with its entire tag table in the server project view and saves the changes in the server project.

**Result:**

User 1 ignores the display that "Tag_1" is outdated, continues working on it and checks in the changes.

The group with the tag table is created once again in the server project, but it now only includes the tag "Tag_1".

##### Renaming objects

You should avoid renaming objects in the local session of a server project as it results in naming conflicts during check-in.

If objects must be renamed, they should be renamed directly in the server project view. Any local session with marked objects that is associated with this server project must not be present at the same time.

##### Different project languages in server project and local session

If a project language is changed in a local session, these changes are lost in the local session after check-in and after refresh.

If a project language is subsequently deleted in the server project view, this project language no longer exists in the server project.

Changes to the project languages should always be made only directly in the server project view. Note that no local sessions with marking to this server project were edited or opened.

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)
  
[Opening and closing the server project view](#opening-and-closing-the-server-project-view)

#### Possible error messages during check-in

##### Introduction

The error messages described below can occur during check-in of marked changes from the local session to the server project or in the server library:

- Transfer error
- Compilation error

The procedure for dealing with these error messages is described below.

##### Transfer error

The following actions are automatically executed when transfer errors occur during check-in:

- An error message will inform you about the type of error that has occurred and the next steps.

  After acknowledgment, this message is closed.
- In the case of a critical transfer error, the status prior to the check-in is restored in the local session as well as in the server project or in the server library.

  Changes are not lost.

  Correct the error in your local session.
- If the transfer error can be corrected in the server project view, the server project view is opened.

  Correct the error in the server project view.
- The faulty objects are displayed and identified in the multiuser editor in the "Check-in" view.
- The Project server locked for check-in is released once again if the errors are corrected in the local session.
- The project server remains locked in the server project view during error correction.

  Note that no other user can check in their changes during this time period.

##### Correcting transfer errors

After occurrence of a transfer error, you have the following options for the action to take:

1. Correct the errors in your local session or in the server project view.
2. Then start the check-in process again so that an error-free project can be checked in.

##### Compilation error

If the option "Compile" is selected during check-in, a compilation process takes place after transfer of the marked changes to the server project with the selected option. The following compile modes are available:

- Marked objects (changes only)

  The changes made to the marked objects for the selected device are compiled together with the device-local objects.
- Device software (changes only)

  The changes made to the marked objects are compiled together with the software version on the assigned devices.

> **Note**
>
> **Options displayed for the compilation during check-in**
>
> The options for compiling that are displayed during check-in are dependent on the settings made in the TIA Portal under "Options &gt; Settings &gt; Multiuser" in "Compilation settings" .
>
> The compiling options may be deactivated in the multiuser editor due to these settings.

If the compiling process is completed successfully, the changes from the local session are automatically transferred to the server project.

The following actions are taken when a compilation error occurs:

- The progress indicator for check-in is closed, and the check-in is stopped.
- The faulty objects are displayed and identified in the multiuser editor in the "Check-in" view.
- The project server remains locked in the server project view during error correction.

  No other user can check in their changes during this period.

##### Correcting compilation errors

After occurrence of a compilation error, you have the following options for the action to take:

1. Correct the indicated errors in your local session or in the server project view.
2. Then start the check-in with compilation again so that an error-free project can be checked in.

##### Ignoring compilation errors

You also have the option of ignoring the indicated compilation errors and checking in a project with errors.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Check-in with compilation errors**  This action is possible but not recommended!   To enable efficient work to continue for all editors involved, you should check in only error-free projects on the Project server whenever possible. |  |

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

#### Deleting objects in the local session

##### Introduction

When working with Multiuser Engineering , you can delete objects in the local session.

The following rules apply to deleting objects:

- Deleted objects are no longer displayed in the local session.
- The "Undo" function can be use to undo the "Delete" action in the local session.
- Deleted objects are automatically marked by the system and displayed in the "Deleted objects" folder.
- If you unmark a deleted object in the multiuser editor, the deleted object is **not** checked-in in the server project or in the server library.

  This means that the object deleted in the local session is not deleted in the server project or in the server library.

  The now deleted but not checked-in object is only displayed after the next refresh.
- When deleting unmarked objects in the local session, these objects are once again present in your local session after the refresh.

  Only marked objects are transferred during check-in.

  Since the deleted objects could not be marked, the deletion is not applied in the server project or in the server library.

  During the next refresh of the local session, these objects are once again added to the local session.

##### Requirement

The connection to the project server exists and the server is available.

##### Procedure for deleting objects

To delete object in the local session, follow these steps:

1. Open the required local session.
2. Delete the requested marked object or delete an unmarked but markable object.
3. Click the "Check-in" button in the multiuser toolbar.

   The multiuser editor opens in the "check-in" view and shows all objects marked in the local session that are applied to the server project or in the server library during check-in.

   The objects deleted in the local session are displayed in the "Deleted objects" folder.
4. Check the objects displayed and marked for deletion.

   You can unmark any objects that are already marked if you do not want to delete them after all.
5. Select the preferred options for check-in:

   - "Compile":

     When you click this option, your changes are compiled with the option "Software, changes only" prior to check-in.

     This means that the software changes you have made are compiled with all their dependent objects in the server project.
   - "Open server project view":

     When you click this options, the server project view is opened in the project tree prior to check-in.

     The server project view shows you in advance the content of the current server project with your changes marked for check-in.

     You can mark and edit all objects in the server project view and unmark them.
6. Click the "Check-in" button to check in the displayed objects into the server project or in the server library.

   If you want to keep the markings in the local session even after check-in, you must select the option "Keep markings".
7. If check-in was unsuccessful and aborted due to errors, you will receive the corresponding error messages.

   Correct the errors in your local session or in the server project view.

   Then start the check-in process again.

##### Result

Your local session is refreshed and opened with the contents of the server project or the server library after successful check-in.

- The local session will include all changes after the refresh that have been checked in into the server project or into the server library in the meantime.
- If new objects were added, these objects are now also visible in your local session.
- The objects deleted in the server project or in the server library, now no longer exist in your local session.
- Your markings in the local session are automatically deleted if you have not selected the option "Keep objects marked".
- The server connection is released once again after check-in.

  The server status changes in the display within the toolbar from "busy" to "available".

---

**See also**

[Introduction to working in local sessions](#introduction-to-working-in-local-sessions)

## Working in the server project view

This section contains information on the following topics:

- [Introduction to working in the server project view](#introduction-to-working-in-the-server-project-view)
- [Opening and closing the server project view](#opening-and-closing-the-server-project-view)
- [Editing objects in the server project view](#editing-objects-in-the-server-project-view)
- [Renaming objects in the server project view](#renaming-objects-in-the-server-project-view)

### Introduction to working in the server project view

#### Introduction

In Multiuser Engineering , you have the option of working directly in the server project view in addition to working in local sessions.

The server project view can be opened for editing with the icon in the multiuser toolbar.

#### Structure of the server project view

The server project view shows the current content of the server project in the project tree below the local session against a yellow background.

The figure below shows an example of a multiuser project opened in the server project view:

![Structure of the server project view](images/90274713611_DV_resource.Stream@PNG-en-US.png)

#### Actions in the server project view

You can perform the following actions in the server project view:

- The server project view lets you work directly in the server project.
- All existing objects can be edited in the server project view, even those that could not be edited in the local session.
- In the server project view you can work with the functionality of Inter Project Engineering (IPE) and exchange data between CPU and HMI via a PLC proxy.
- Shared working on one CPU is also supported during shared commissioning.
- Blocks or larger program parts from a CPU should only be uploaded in the server project view.
- You can also make changes to the configuration with the help of external tools in the server project view. This function is not supported when working in the local sessions.
- Changes to user-defined documentation, such as adding new user texts or new HMI scripts, should only be made in the server project view.
- The objects that are to be edited must also be marked for editing in the server project view so that other editors see that these objects are being changed.
- You can save or discard the changes made in the server project view with the "Save changes" and "Discard changes" buttons.
- Any changes you have made will be saved directly in the server project with the save step.

> **Note**
>
> **Restrictions when working in the server project view**
>
> The following conditions apply as soon as the server project view is open:
>
> - The local session is locked to prevent editing.
> - The project server is locked for the other editors.
> - The icon for the server status is shown in yellow in the toolbar.
> - If the changes you have made cannot be saved when working in the server project view, you should additionally select and deselect another object so that the "Save changes" button is activated and saving is possible.

---

**See also**

[Opening and closing the server project view](#opening-and-closing-the-server-project-view)
  
[Editing objects in the server project view](#editing-objects-in-the-server-project-view)

### Opening and closing the server project view

#### Introduction

The server project view lets you edit all objects that are available in the server project.

You have the following options to open the server project view:

- Icon in the multiuser toolbar
- Button in the multiuser editor in the "Check-in" view

You will receive a message if the server project view cannot be opened because the server is currently in use by another editor and locked.

#### Displayed contents in the server project view

The server project view always shows the latest version of the server project.

If the server project view is opened in the "Check-in" view in the multiuser editor, it also shows the changes made in the local session in addition to the current content of the server project. This means it offers a preview of how the server project will look after check-in of the changes made in the local session.

#### Opening the server project view

To open the server project view, follow these steps:

1. Open the required local session.
2. In the multiuser toolbar, click the "Open/close server project view" icon.

   Alternatively, click "Check-in" in the multiuser toolbar and then click "Open server project view before check-in" in the multiuser editor.

#### Closing the server project view

To close the server project view, follow these steps:

1. In the multiuser toolbar, click the "Open/close server project view" icon once again.
2. If you have made changes in the server project view, you will be prompted as to whether you want to save or discard the changes.
3. Click "Yes" to save your changes or "No" to discard them.

   Alternatively, you can click on the corresponding buttons in the server project view before you close it to save or discard your changes.

#### Result

The server project view is closed.

The local session is opened once again for editing.

The server is released again and the server status is displayed in green.

#### Closing the complete project

To close the complete project in the server project view, follow these steps:

1. Save the changes made in the server project view by clicking the corresponding button.
2. In the TIA Portal command line, click on the "Close" menu command.

#### Result

The complete multiuser project is closed.

---

**See also**

[Introduction to working in the server project view](#introduction-to-working-in-the-server-project-view)
  
[Editing objects in the server project view](#editing-objects-in-the-server-project-view)

### Editing objects in the server project view

#### Introduction

In the context of Multiuser Engineering you can also edit objects directly in the server project view .

The server project view lets you edit all objects in the server project view, even those that must not be edited in the local session.

Working in the server project view is an exclusive working directly in the Server project. The project server is locked for other editors while you are working in the server project view. The associated local session cannot be edited during the working in the server project view.

The objects you want to check in also have to be selected in the server project view. This enables you to ensure that other editors in your local session can see that you are currently editing these objects. Marking conflicts can hereby be avoided.

You can also use the "Autoselect" function in the server project view or alternatively select the objects to be edited manually.

> **Note**
>
> **Marking of identical objects in the local session and in the server project view**
>
> Keep in mind that a marking conflict is displayed with red flag if you mark an object more than once, even if both markings belong to the same editor.

#### Editing objects in the server project view

You can, for example, perform the following actions in the server project view:

- Adding new objects that did not exist previously in the server project.
- Add or change hardware configuration and connections.
- Perform version changes on the instructions used.
- Working with Inter Project Engineering (IPE).
- Editing all objects regardless of whether these are marked or not.
- Renaming, moving and deleting objects.
- Establishing an online connection to a CPU and downloading or uploading objects.
- Executing all functions of the TIA Portal supported by Multiuser Engineering.

#### Procedure for editing objects in the server project view

To edit objects in the server project view, follow these steps:

1. Open the required local session.
2. In the multiuser toolbar, click the "Open/close server project view" icon.

   The server project view is then shown against a yellow background below the local session in the project tree.

   The server project view is closed again the next time you click this icon.
3. Select the objects you want to edit in the server project view by clicking on the flag in front of them, or use the "Autoselect" function by opening and editing the objects directly in the editor.
4. Make your required changes.
5. Save your changes by clicking the "Save changes" button.

   Or click "Discard changes" if you do not want to apply your changes to the server project.
6. Enter a comment on the change history to document the changes you have made in the server project view.
7. If you want to apply the changes from the server project view to the local session, click the "Refresh local session" button after saving the changes in the local session.

#### Result

The changes made in the server project view are saved in the server project.

- The server project view is closed and the local session is once again released for editing.
- The markings are removed in the server project view.
- The local session is **not** automatically refreshed with the new contents of the server project. The symbol for the project server shows that a more recent version of the server project is available.

#### Server project view is open and the server connection is interrupted

If you have already opened the server project view and the connection to the project server is subsequently interrupted, you receive a corresponding error message.

You then have the following options:

- Click the "Reconnect" button to establish a new connection to the associated Project server.
- Or click the "Discard" button to discard the changes made in the server project view.

If you cannot reestablish the interrupted server connection and you discard your changes, the local session is opened offline with an error message. The local session can also be opened when the associated server is currently not available.

You can continue working offline in the local session with the following restrictions:

- Selections made by other users are not visible in your local offline session; no yellow or red flags and no outdated objects are displayed.
- Changes you are making in the local offline session cannot be checked in until a server connection is available once again.

---

**See also**

[Introduction to working in the server project view](#introduction-to-working-in-the-server-project-view)
  
[Opening and closing the server project view](#opening-and-closing-the-server-project-view)

### Renaming objects in the server project view

#### Introduction

When you work with Multiuser Engineering , object can be renamed.

#### Rules for renaming objects

The following rules apply to renaming objects:

- You should avoid renaming objects in the local session as it can lead to naming conflicts during check-in.
- The renaming of objects should always be performed in the server project view.
- When objects are renamed in the server project view, the objects to be renamed must have no markings within local sessions.
- Name conflicts may occur due to the renaming. During renaming in the project, make sure that you do not again use an already used name.
- To avoid unintended references of objects, conflicts that occur during renaming are not automatically corrected.
- The renaming of devices does not create any conflicts for objects within a device, as devices are not identified by their name but by their ID.
- However the renaming of devices may create conflicts with any existing references between devices (PLC and HMI).
- After objects have been renamed, the other editors should refresh their local sessions.

#### Requirement

The connection to the project server exists and the server is available.

No other local session to this server project is open.

#### Renaming objects

To rename objects in the server project view:

1. Open the required local session.
2. In the multiuser toolbar, click the "Open/close server project view" icon.

   The server project view is then shown against a yellow background below the local session in the project tree.

   The server project view is closed again the next time you click this icon.
3. Mark the required objects in the server project view and rename these.
4. Click the "Save changes" button to apply the changes in the server project.

#### Result

The changes made in the server project view are saved in the server project.

- The server project view is closed and the local session is once again released for editing.
- The markings are removed in the server project view.
- The local session is **not** automatically refreshed with the new contents of the server project.
