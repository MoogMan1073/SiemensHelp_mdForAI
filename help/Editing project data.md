---
title: "Editing project data"
package: PEProjectDataenUS
topics: 92
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Editing project data

This section contains information on the following topics:

- [Compiling and loading project data](#compiling-and-loading-project-data)
- [Comparing project data](#comparing-project-data)
- [Protecting project data](#protecting-project-data)
- [Printing project contents](#printing-project-contents)
- [Working with multi-language projects](#working-with-multi-language-projects)
- [Working with text lists](#working-with-text-lists)
- [Using memory cards](#using-memory-cards)
- [Using cross-references](#using-cross-references)
- [Providing user-defined documentation](#providing-user-defined-documentation)

## Compiling and loading project data

This section contains information on the following topics:

- [Compiling project data](#compiling-project-data)
- [Loading project data](#loading-project-data)

### Compiling project data

This section contains information on the following topics:

- [General information on compiling project data](#general-information-on-compiling-project-data)
- [Compiling project data](#compiling-project-data-1)

#### General information on compiling project data

##### Compiling project data

During compilation, project data is converted so that it can be read by the device. Hardware configuration data and program data can be compiled separately or together. You can compile the project data for one or more target systems at the same time.

The following project data must be compiled prior to loading:

- Hardware project data, for example, configuration data of the devices or networks and connections
- Software project data, for example, program blocks or process screens

> **Note**
>
> While a device is being compiled, no additional compiling process can be started. Note in this regard that you can not only perform a compiling process manually, but you can also trigger it automatically for operator control and monitoring devices.

##### Scope of the compilation

When you compile project data, you have the following options depending on the device involved:

- Hardware and software (only changes)
- Hardware (only changes)
- Hardware (rebuild completely)
- Software (only changes)
- Software (rebuild all)
- Software (reset memory reserve)

---

**See also**

[Compiling project data](#compiling-project-data-1)

#### Compiling project data

The following section describes the general procedure for compiling project data in the project tree. You will find details of how certain objects are compiled and any special points to note in the online help of the product.

##### Procedure

To compile project data, follow these steps:

1. In the project tree, select the devices whose project data you want to compile.
2. Select the option you require in "Compile" submenu of the shortcut menu.

   The project data is compiled. You can check whether or not the compilation was successful in the Inspector window with "Info &gt; Compile".

**Note**

Note that the options available to you depend on the selected device.

---

**See also**

[General information on compiling project data](#general-information-on-compiling-project-data)
  
[Inspector window](Configuring%20devices%20and%20networks.md#inspector-window)

### Loading project data

This section contains information on the following topics:

- [General information on loading](#general-information-on-loading)
- [Downloading project data to a device](#downloading-project-data-to-a-device)
- [Downloading project data to a memory card](#downloading-project-data-to-a-memory-card)
- [Uploading project data from a device](#uploading-project-data-from-a-device)
- [Loading project data from a memory card](#loading-project-data-from-a-memory-card)

#### General information on loading

##### Introduction

In order to set up your automation system, you need to load the project data you generated offline on the connected devices. This project data is generated, for example when configuring hardware, networks, and connections or when programming the user program or when creating recipes.

The first time you download, the entire project data is downloaded. During later loading operations, only changes are downloaded.

You can download the project data to devices and memory cards.

> **Note**
>
> As of TIA Portal V15 and an S7-1500 CPU as of firmware V2.5, tag tables are included when downloading to a device or to a memory card and when downloading from a device or from a memory card. This makes the tag tables available online on your CPU as well. The PLC tags are stored according to the tag tables configured offline. An online/offline comparison can be performed and tag tables can be downloaded by the device.

> **Note**
>
> While a device is being compiled, no additional download process can be started. Note in this regard that you can not only perform a compiling process manually, but you can also trigger it automatically for operator control and monitoring devices.

##### Possible options for downloading

Depending on the object you want to download, you have the following options:

- Hardware and software (only changes)

  Both the hardware configuration and software are downloaded to the destination if differences exist between the online and offline versions.
- Hardware configuration

  Only the hardware configuration is downloaded to the destination.
- Software (only changes)

  Only the objects that differ online and offline are downloaded to the destination.
- Software (all)

  The PLC program including all blocks, PLC data types and PLC tags is downloaded to the target and all values are reset to their initial values. Be aware that this also applies to retentive values.

You can also upload project data already contained in a device back to your project. You have the following options:

- Upload entire device as new station

  The hardware configuration of the device and the software on the device are loaded in the project.

  All relevant data of the device is uploaded to the project.
- Upload software of a device

  Only the blocks and parameters from the device are uploaded to an existing CPU in the project.

In both cases, during loading all instances of library types are connected again with the corresponding version of the type in the project library. If no suitable type is yet available for a loaded instance or the correct version of the type does not exist in the project library, the type or the version is added to the project library.

##### Downloading with synchronization

In team engineering, it is possible for several users to work on one project with several engineering systems at the same time and to access one S7-1500 CPU. To ensure consistency within the shared project, it is necessary to synchronize the changed data prior to loading so that nothing gets overwritten unintentionally.

If differences are detected between the online and offline data management within the shared project that were caused by a different engineering system, automatic synchronization of the data to be loaded is offered when loading.

In this case, the "Synchronization" dialog displays the data to be synchronized with the current status (online-offline comparison) and the possible actions.

| Use case | Recommendation | Synchronization |
| --- | --- | --- |
| One or more blocks on the CPU (online) are more recent than in the engineering system (offline). | These blocks should be uploaded from the CPU to the engineering system before downloading. | Automatic synchronization is possible:  The blocks in the engineering system are updated prior to loading. |
| One or more new blocks have been created and exist only on the CPU (online). | These blocks should be uploaded from the CPU to the engineering system before downloading. | Automatic synchronization is possible:  The new blocks are added to the engineering system prior to the download. |
| One or more blocks on the CPU have been deleted. | The blocks should also be deleted prior to the download in the engineering system. | Automatic synchronization is not possible.  The blocks deleted on the CPU should be manually deleted in the offline project in the engineering system. |
| One or more blocks on the CPU and in the engineering system are different.  This is the case when a different user has changed blocks to which you have also made corrections and has already downloaded them to the CPU. | These blocks with competing changes must be adapted manually. You decide in this case which changes you are going to accept.  If the blocks on the CPU are to be retained, you should adopt these blocks from the CPU in your engineering system before downloading to the CPU.  If the blocks that you have changed are to be applied, you can continue with the download without synchronization. | Automatic synchronization is not possible:  The affected blocks on the CPU or in the engineering system must be adapted manually. One of the existing block versions (online or offline) will be overwritten in the process. |
| There are differences in the hardware configuration on the CPU (online) and in the engineering system (offline). | Differences in the hardware configuration must be adapted manually. You decide in this case which hardware configuration you are going to accept.  If the existing hardware configuration on the CPU is to be retained, you should adopt this in your engineering system prior to downloading.  If you want to apply the hardware configuration you changed, you can continue downloading without synchronization. | Automatic synchronization is not possible:  The hardware configuration must be adapted manually.  One of the existing hardware configurations (online or offline) will be overwritten. |

If required, you can use the "Force download to device" command to download blocks without synchronization.

---

**See also**

[Compatibility with the plant configuration](Editing%20projects.md#compatibility-with-the-plant-configuration)
  
[Loading a configuration](Configuring%20devices%20and%20networks.md#loading-a-configuration)
  
[Downloading project data to a device](#downloading-project-data-to-a-device)
  
[Downloading project data to a memory card](#downloading-project-data-to-a-memory-card)
  
[Uploading project data from a device](#uploading-project-data-from-a-device)

#### Downloading project data to a device

The following section describes the general procedure for downloading project data to a device. You will find details of how certain objects are downloaded and any special points to note in the online help of the product.

##### Requirement

- The project data is consistent.
- Each device to which you want to download is accessible via an online access.

##### Procedure

To download the project data to the selected devices, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Select one or more devices systems in the project tree. 2. Right-click on a selected element.    The shortcut menu opens. 3. Select the option you require in the shortcut menu of the "Download to device" submenu.      | Symbol | Meaning |    | --- | --- |    | **Note**  Note that the options available to you depend on the selected device. |  |     When necessary, the project data is compiled.     - If you had previously established an online connection, the "Load preview" dialog opens. This dialog displays messages and proposes actions necessary for downloading.    - If you had not previously established an online connection, the "Extended download to device" dialog opens, and you must first select the interfaces via which you want to establish the online connection to the device. You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command.      See also: [Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection) 4. Check the messages in the "Load preview" dialog, and select the actions in the "Action" column, if necessary.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Preventing personal injury and material damage** Performing the proposed actions while the plant is in operation can cause serious bodily injury and property damage in the event of malfunctions or program errors. Make sure that no dangerous situations can arise before you start the actions. |  |     As soon as loading becomes possible, the "Load" button is enabled. 5. Click the "Load" button.    The loading operation is performed. If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are required for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. The "Load results" dialog then opens. In this dialog, you can check whether or not the loading operation was successful and take any further action that may be necessary. 6. Click the "Finish" button. |  |

##### Result

The selected project data was downloaded to the devices.

---

**See also**

[Downloading a configuration to a device](Configuring%20devices%20and%20networks.md#downloading-a-configuration-to-a-device)
  
[General information on loading](#general-information-on-loading)
  
[Downloading project data to a memory card](#downloading-project-data-to-a-memory-card)
  
[Uploading project data from a device](#uploading-project-data-from-a-device)
  
[Default setting online connection data](Using%20online%20and%20diagnostics%20functions.md#default-setting-online-connection-data)

#### Downloading project data to a memory card

You have the option of loading project data to a memory card. For CPUs of the S7-300/400 series you can also explicitly download the user program to a memory card inserted in the CPU.

To download project data to a memory card, you have the following options:

- Dragging project data to a memory card
- Writing project data to a memory card
- Downloading user program to a memory card that is inserted in a CPU of the S7-300/400 series

##### Requirement

A memory card is displayed.

See also: [Accessing memory cards](#accessing-memory-cards)

##### Downloading project data to a memory card

To download project data to a memory card, follow these steps:

1. In the project tree, drag the project data you want to download to the memory card.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays alarms and recommends actions needed for the loading operation.
2. Check the alarms and select the actions in the "Action" column, if necessary.

   As soon as downloading becomes possible, the "Load" button is enabled.
3. Click the "Load" button.

   The loading operation is performed.

Or:

1. In the project tree, select the project data that you want to download.
2. To do this, right-click the selection and select the "Copy" command from the shortcut menu. You can also use the key combination &lt;Ctrl+C&gt;.
3. Right-click the memory card and select the "Paste" command from the shortcut menu. You can also use the key combination &lt;Ctrl+V&gt;.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays alarms and recommends actions needed for the loading operation.
4. Check the alarms and select the actions in the "Action" column, if necessary.

   As soon as downloading becomes possible, the "Load" button is enabled.
5. Click the "Load" button.

   The loading operation is performed.

Or:

1. In the project tree, select the project data that you want to download.
2. Select the "Card Reader/USB memory &gt; Write to memory card" command in the "Project" menu.

   The "Select memory card" dialog opens.
3. Select a memory card that is compatible with the CPU.

   A button with a green check mark is activated at the bottom of the dialog.
4. Click the button with the green check mark.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays alarms and recommends actions needed for the loading operation.
5. Check the alarms and select the actions in the "Action" column, if necessary.

   As soon as downloading becomes possible, the "Load" button is enabled.
6. Click the "Load" button.

   The loading operation is performed.

##### Downloading the user program to a memory card in the CPU (S7-300/400 only)

To download the user program to a memory card in a CPU of the S7-300/400 series, follow the steps below:

1. Select a CPU of the S7-300/400 series in the project tree.
2. Select the "Download user program to memory card" command in the "Online" menu.

   The "Load preview" dialog opens. This dialog displays alarms and recommends actions needed for the loading operation.
3. Check the alarms and select the actions in the "Action" column, if necessary.

   As soon as downloading becomes possible, the "Load" button is enabled.
4. Click the "Load" button.

   The loading operation is performed and the "Load results" dialog is displayed. This dialog displays alarms and suggests possible actions.
5. Check the alarms and select the actions in the "Action" column, if necessary.
6. Click the "Finish" button.

---

**See also**

[General information on loading](#general-information-on-loading)
  
[Downloading project data to a device](#downloading-project-data-to-a-device)
  
[Uploading project data from a device](#uploading-project-data-from-a-device)

#### Uploading project data from a device

The following section describes the general procedure for uploading project data from a device. Which project data you can upload from a device depends on the products installed.

You have the following options for uploading project data from a device to your project:

- Uploading as a new station

  With this option you upload existing project data of a device to your project as a new station.
- Uploading project data of a device

  With this option you upload project data from the device to an existing CPU in the project. You will find the project data that can be loaded in the online help of the product.

In both cases, all instances of library types are connected again with the corresponding version of the type in the project library during uploading. If no suitable type is yet available for an uploaded instance or the correct version of the type does not exist in the project library, the type or the version is added to the project library. You can only upload library types in the state "in test" that are saved on the device to the project, if the released type version on which the test version is based is available in the project library.

##### Requirement

- A project is open.
- The hardware configuration and software to be uploaded must be compatible with the TIA Portal. If the data on the device was created with a previous program version or with a different configuration software, please make sure they are compatible.

##### Uploading as a new station

To upload the complete device to your project, follow these steps:

1. Select the project name in the project tree.
2. Select "Upload device as new station (hardware and software)" in the "Online" menu.

   The "Upload device to PG/PC" dialog opens.
3. Select the type of interface you want to use for the uploading operation in the "Type of the PG/PC interface" drop-down list.
4. Select the interface to be used from the "PG/PC interface" drop-down list.
5. Click the "Configure interface" button to the right of the "PG/PC interface" drop-down list to adapt the settings for the selected interface.

   See also: [Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
6. Display all compatible devices by selecting the relevant option and clicking the "Start search" command. In the accessible devices table, select the device from which you want to upload project data.
7. Click on "Load".

   Depending on the selected device, a dialog appears in which you have to enter additional information, such as the position of the module rack.

   The project data of the device is uploaded to the project. You can edit it offline and then download it to the device again.

##### Uploading project data of a device

To upload only project data from one device to your project, follow these steps:

1. Establish an online connection to the device from which you want to download the project data.

   See also: [Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
2. Select the device in the project tree.

   The "Upload from device (software)" command in the "Online" menu is enabled.
3. Select the "Upload from device (software)" command in the "Online" menu.

   The "Upload preview" dialog box opens.
4. Check the alarms in the "Upload preview" dialog, and select the necessary actions in the "Action" column.

   As soon as uploading becomes possible, the "Upload from device" button is enabled.
5. Click the "Upload from device" button.

   The loading operation is performed.

##### Loading of project data from a different project version from a device

When the commands "Upload from device (software)" and "Loading the device as new station (hardware and software)" are executed in the "Online" menu, it is checked whether the project data on the device was created with a different version than the opened version of the TIA Portal.

If the project data was created with a different project version, the "Upload preview" dialog provides you with information on whether all upload requirements are met.

Note the information on the requirements for loading and, if necessary, select a command in the selection menu in the "Action" column.

The "Upload from device" button is enabled as soon as the view has been updated and uploading is possible.

##### Special features when using data blocks from other product versions

Data blocks that were created with a different product version of the TIA Portal cannot be opened and edited with the current product version. You can find additional information in the section "[Using projects created with optional software](Editing%20projects.md#using-projects-created-with-optional-software)".

---

**See also**

[Displaying accessible devices](Using%20online%20and%20diagnostics%20functions.md#displaying-accessible-devices)
  
[General information on loading](#general-information-on-loading)
  
[Downloading project data to a device](#downloading-project-data-to-a-device)
  
[Downloading project data to a memory card](#downloading-project-data-to-a-memory-card)
  
[General information on loading to PG/PC](Configuring%20devices%20and%20networks.md#general-information-on-loading-to-pgpc)
  
[Loading a configuration](Configuring%20devices%20and%20networks.md#loading-a-configuration)

#### Loading project data from a memory card

You have the following options for uploading project data from a memory card to your project:

- Upload project data of the memory card as a new station

  With this option you upload the project data of a memory card to your project as a new station.
- Upload project data of the memory card to an existing device

  With this option you upload project data of a memory card to an existing device in your project. You will find the project data that can be loaded in the online help of the product.

In both cases, all instances of library types are connected again with the corresponding version of the type in the project library during loading. If no suitable type is yet available for a loaded instance or the correct version of the type does not exist in the project library, the type or the version is added to the project library.

##### Requirement

- A project is open.
- The memory card is displayed.

  See also: [Accessing memory cards](#accessing-memory-cards)
- The hardware configuration and software to be uploaded must be compatible with the TIA Portal. If the data on the memory card was created with a previous program version or with different configuration software, please make sure they are compatible.

##### Uploading project data as a new station

To upload project data from a memory card to your project, follow these steps:

1. In the project tree, select the project data you want to upload.
2. Select "Upload device as new station (hardware and software)" in the "Online" menu.

Or:

1. In the project tree, drag the memory card folder to the project.

Or:

1. Right-click on the memory card.
2. Select "Copy" in the shortcut menu.
3. Right-click on the project.
4. Select the "Paste" command in the shortcut menu.

##### Uploading project data to an existing device

To upload the project data of a memory card to an existing device, follow these steps:

1. In the project tree, drag the folder of the memory card to a device in the project or copy the memory card and paste the data into a device.

   The "Upload preview" dialog box opens.
2. Check the alarms in the "Upload preview" dialog, and select the necessary actions in the "Action" column.

   As soon as uploading becomes possible, the "Upload from device" button is enabled.
3. Click the "Upload from device" button.

   The loading operation is performed.

## Comparing project data

This section contains information on the following topics:

- [Basics of project data comparison](#basics-of-project-data-comparison)
- [Comparing offline/online](#comparing-offlineonline)
- [Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
- [Using the compare editor](#using-the-compare-editor)

### Basics of project data comparison

#### Function

You can compare project data of the same type in order to determine possible differences. In principle, the following comparison methods are available:

- Compare offline/online

  With this comparison method you can compare the software of objects of a device with the objects of a project. This is only possible when you establish an online connection to the device.
- Offline/offline comparison

  With this comparison method you can either compare the software or the hardware. When you compare the software, you can compare objects from projects or libraries. The hardware comparison is available for devices from the currently open project or from reference projects. You can decide for the software as well as the hardware comparison whether the comparison should be performed automatically for all objects or whether you want to compare individual objects manually.
- Detailed comparison

  For some objects, for example, blocks, you can also perform a detailed comparison in addition to the offline/online and offline/offline comparison. This involves opening the blocks to be compared beside each other and highlighting the differences.

A simple offline/online comparison is performed as soon as you establish an online connection. During this process, comparable objects in the project tree are marked with icons that represent the result of the comparison. You can also run a more comprehensive offline/online and offline/offline comparison in the compare editor. When you compare software, you can also select actions for non-identical objects in the comparison.

> **Note**
>
> - Not all objects allow all types of comparison. Which comparison method you can use for which project data depends on the products installed.
> - Compile your user program before you start a comparison or detailed comparison. After each change of the program during a comparison, repeat this step before you update the result of the comparison. This ensures that the comparison shows the current status.
> - When monitoring a module, note that a difference of the time stamp can also exist with an offline/online comparison if the block is recompiled with code change. The checksum remains unchanged. In this case download the block to the device and restart the monitoring.
> - In the following cases, the time stamps of the objects are used as comparison criteria:
>
>   - Export and re-import via the Openness interface
>   - Block calls
>   - Access to the global data of a data block (DB)
>
>   This can result in different checksums, even though the objects are identical.

#### Comparison using checksums

The offline/online and offline/offline comparison of software objects uses checksums that are generated for certain data of the objects. The objects are only the same if their checksums are identical.

> **Note**
>
> Time stamps continue to be used for offline/online comparison for CPUs of the S7-300/400 series.

The data of an object are divided into the following two categories:

- Source data

  Source data are all the data of an object which you can directly influence, such as the name of the object, source code, comments or programming language. The properties that you can edit here may differ depending on the object.
- Target data

  All compiler and runtime data are the target data. These data may have no direct influence, since they are produced by the system based on their source data. Once again here, the characteristics differ depending on the object.

The following table provides an overview of the areas of the property comparison:

| Category | Area | Description |
| --- | --- | --- |
| Source data | Safety | Checksum for safety objects  You can find additional information about the comparison of safety objects in the "Comparing safety programs" section of the online help for SIMATIC Safety. |
| Interface without comments | Checksum of all the tags of the block interface of the first layer. Comments of the tags are not part of the checksum. |  |
| Interface of published blocks without comments (software units) | Checksum of all interface checksums of published objects of a software unit. Comments are not part of the checksum. |  |
| Textual block interface | Checksum of all tags, comments and formatting in the textual block interface of SCL blocks. |  |
| Program code | Checksum that only takes the source code into account. Spaces, line breaks, tabs and comments of all types are not included in the checksum. The position of free comments in LAD and FBD and their assignment to graphic elements are also not included. This checksum is not available for GRAPH and CEM. |  |
| Program code (legacy) | Checksum of the source code. Block and network comments are not included in the checksum. Comments that are not multilingual in STL and SCL and the reassignment of free comments to other boxes in LAD and FBD are included in the checksum. |  |
| Comments (multi-language) | Checksum of all block comments and network comments |  |
| Language configuration | Compare offline/online: Shows the languages that are loaded to the device during the loading process.  Offline/offline comparison: Shows the enabled languages in the project. |  |
| Event | Checksum of all event-relevant data of an organization block (OB). |  |
| Properties | Checksum of all configurable properties of an object. |  |
| Extended properties of program elements in software units | Checksum of the publication status of objects in software units. |  |
| Configuration of technology objects | Checksum of the technology-specific settings of a technology object. |  |
| Alarm configuration | Checksum on all alarm-specific settings of an object. |  |
| Supervision configuration | Checksum of all supervision settings of an object. |  |
| Text lists | Checksum over all text lists of an object. |  |
| Tags without comments | Checksum over all tags of the selected PLC tag table. The "Retentivity" and "Monitoring" columns as well as the comments of the tags are not part of the checksum. |  |
| Constants without comments | Checksum over all user constants of the selected PLC tag table. System constants and the comments of the user constants are not part of the checksum. |  |
| Target data | Compilation and runtime data | Checksum of data for compiling and relevant for loading. |
| Time stamp | Time stamps for S7-300/400 CPUs that are created by the system for compiling and downloading. Only available when an online connection is available. |  |

> **Note**
>
> - Note that the object determines which checksums are actually used for the comparison.
> - The value settings of technology objects are also transferred to the checksum of the block interface.
> - For know-how protected blocks that were created in an older version, the checksums "Program code (legacy)" and "Comments (multi-language)" are not displayed under "Source data".

---

**See also**

[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Using the compare editor](#using-the-compare-editor)

### Comparing offline/online

The offline/online comparison lets you compare objects of a device with objects of a project.

#### Requirement

The project tree is open.

#### Procedure

To perform an offline/online comparison, follow these steps:

1. Select a device in the project tree that allows offline/online comparison.
2. Select the "Compare &gt; Offline/online" command in the shortcut menu.
3. If you have not already established an online connection to this device, the "Go online" dialog opens. In this case, set all the necessary parameters for the connection and click "Connect".

   The online connection is established and compare editor opens.

#### Result

All objects that exist online and offline are displayed. The symbols in the compare editor and in the project tree show you the status of the objects. In the compare editor, you can now define certain actions for the objects, depending on their status.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](#using-the-compare-editor)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)

### Carrying out offline/offline comparisons

With offline/offline comparison you have the option to compare the project data of two devices. You can carry out a software as well as a hardware comparison. When you compare the software, you can compare objects from projects or libraries. The hardware comparison is available for devices from the currently open project or from reference projects. You can decide whether the comparison should be performed automatically for all objects or whether you want to compare individual objects manually. For a software comparison, the following options are available as well:

- For objects that are not identical, you can specify actions to eliminate the differences.
- You can specify the criteria that should be used for the comparison.

You can drag any other device to the drop area at any time to perform further comparisons.

#### Requirement

The project tree is open.

#### Performing an offline/offline comparison for software

To perform an offline/offline comparison for software, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane.

   All existing objects of the selected devices are displayed depending on the settings of the compare editor in the "Software" tab and an automatic comparison is carried out. You can identify the status of the objects based on the symbols in the compare editor. If needed, specify an action for non-identical objects to eliminate the differences.
4. If needed, define the comparison criteria.
5. Select an object to display the details of the property comparison.
6. If you want to carry out a manual comparison, click on the button for switching between automatic and manual comparison in the status and action area. Then select the objects that you want to compare.

   The properties comparison is displayed. You can identify the status of the objects based on the symbols.

#### Performing an offline/offline comparison for hardware

To perform an offline/offline comparison for hardware, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane.
4. Open the "Hardware" tab.
5. If you want to carry out a manual comparison, click on the button for switching between automatic and manual comparison in the status and action area. Then select the objects that you want to compare.

   The properties comparison is displayed. You can identify the status of the objects based on the symbols.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Using the compare editor](#using-the-compare-editor)
  
[Running a detailed comparison](#running-a-detailed-comparison)

### Using the compare editor

This section contains information on the following topics:

- [Overview of the compare editor](#overview-of-the-compare-editor)
- [Show and hide table columns](#show-and-hide-table-columns)
- [Filtering the compare editor view](#filtering-the-compare-editor-view)
- [Running a detailed comparison](#running-a-detailed-comparison)
- [Updating the comparison results](#updating-the-comparison-results)
- [Set comparison criteria](#set-comparison-criteria)
- [Synchronizing non-identical objects](#synchronizing-non-identical-objects)
- [Changing the view](#changing-the-view)

#### Overview of the compare editor

##### Function

The compare editor gives an overview of the results of a comparison in a table. The appearance varies slightly depending on whether it is an offline/online comparison or a hardware/software comparison.

##### Layout of the compare editor

The following figure shows the layout of the compare editor for an offline/online comparison:

![Layout of the compare editor](images/87690796939_DV_resource.Stream@PNG-en-US.png)

① Compare editor toolbar

② Left comparison table

③ Status and action area

④ Right comparison table

⑤ Property comparison

The following figure shows the layout of the compare editor for an offline/offline comparison (software):

![Layout of the compare editor](images/87691446411_DV_resource.Stream@PNG-en-US.png)

① Compare editor toolbar

② Drop areas

③ Button to toggle between automatic and manual comparison

④ Left comparison table

⑤ Status and action area

⑥ Right comparison table

⑦ Property comparison

The following figure shows the layout of the compare editor for an offline/offline comparison (hardware):

![Layout of the compare editor](images/147390308107_DV_resource.Stream@PNG-en-US.png)

① Compare editor toolbar

② Drop areas

③ Button to toggle between automatic and manual comparison

④ Left comparison table

⑤ Status area

⑥ Right comparison table

⑦ Property comparison

The following figure shows the layout of the compare editor for a comparison of the project library with a global library:

![Layout of the compare editor](images/150727731979_DV_resource.Stream@PNG-en-US.png)

① Compare editor toolbar

② Drop areas

③ Button to toggle between automatic and manual comparison

④ Left comparison table

⑤ Status and action area

⑥ Right comparison table

⑦ Property comparison

##### Compare editor toolbar

With the toolbar, you can access the following compare editor functions:

- Show identical and different objects

  You can show identical objects if you want to view the comparison in full.
- Show only objects with differences

  You can hide identical objects to make the comparison easier to follow.
- Show additional filters available (only offline/online comparison and offline/offline comparison for software; not available for library comparison)

  You can define which objects are to be compared.
- Display available assignment criteria (only offline/offline comparison for hardware)

  You can specify the criterion according to which the modules are to be assigned to each other for the comparison.
- Change the view

  You can choose between a hierarchical and a flat view. In the hierarchical view, the devices are shown in their structure; in the flat view, the objects of the devices are listed without structure.
- Start detailed comparison (only for offline/online comparison, offline/offline comparison for software and library comparison)

  You can start a detailed comparison for objects to show the individual differences. This function is, however, not available for every object.
- Refresh the view

  After you have modified objects, you can update the comparison results using this function.
- Execute actions (only for offline/online comparison, offline/offline comparison for software and library comparison)

  You can synchronize non-identical objects using specific actions.
- Set comparison criteria (only for offline/online comparison, offline/offline comparison for software and library comparison)

  You can specify which criteria are to be used in the comparison. Disabled criteria do not affect the overall result of the comparison.
- Back (only offline/offline comparison for hardware)

  When you start the detailed comparison for a distributed I/O from a CPU device comparison, you can use this button to navigate back to the previous device comparison.
- Open library management (library comparison only)

  You can open a comparison object in the library management. This function is available for the "Types" folder, custom folders in the "Types" folder and types.

##### Drop areas

In the case of an offline/offline comparison, you can drag the devices you want to compare into the drop areas. In the case of a software comparison, the devices to be compared can originate from the opened project, from reference projects, from the project library or from global libraries. However, note that you can only drop complete libraries into the right drop area. In the case of a hardware comparison, you can compare devices from the opened project or from reference projects. In a library comparison that is started in the "Libraries" task card, the project library and global libraries can be dragged at will into the left or right drop area.

##### Button to toggle between automatic and manual comparison

With an offline/offline comparison, you can switch between automatic and manual comparison. In the case of automatic comparison, the objects to be compared are assigned automatically to each other. In the case of a manual comparison, you can select the objects that are to be compared.

##### Comparison tables

Comparison tables show the objects of the devices being compared to one another.

The following table shows the meaning of the columns of the comparison table:

| Column | Description |
| --- | --- |
| Name | Name of the compare object |
| Comment | Comment on the compare object |
| Title | Title of the compare object |
| Address | Address of the compare object |
| Numbering | Type of numbering for the comparison object |
| Type | Type of compare object |
| Language | Programming language set for the compare object. |
| Time stamp interface | Time of the last modification to the block interface |
| Time stamp code | Time of the last modification to the source code |
| Author | Name of the author of the compare object |
| Version | Version of the compare object |
| Uses | Usage locations of a type |
| Family | Name of the object family |
| Load memory | Memory usage of the load memory of the compare object |
| Work memory | Memory usage of the work memory of the compare object |
| Modified on | Time of last modification |
| Optimized block access | Indicates whether "Optimized block access" is enabled for a block. |
| Signature | Signature of the comparison object (SIMATIC Safety*) |
| Interface signature | Signature of the block interface of the comparison object (SIMATIC Safety *) |

* You can find additional information about the comparison of safety objects in the "Comparing safety programs" section of the online help for SIMATIC Safety.

Not all columns are available in every comparison method. In the case of a hardware comparison, for example, the comparison tables only contain the "Name" column. In the case of a library comparison, the comparison tables only contain the "Name", "Author", "Comment" and "Uses" columns.

Not all columns are shown in the default setting. However, as in all table editors, you can show or hide the columns as required and sort according to individual columns.

##### Status and action area

The status and action area offers the following options:

- You can view the results of automatic comparison. The results are displayed with symbols.
- In an offline/online comparison, an offline/offline comparison for software, and a library comparison, you can specify actions for non-identical objects.

##### Status and action symbols

The following table shows the symbols for the comparison results for an offline/online comparison:

| Symbol | Description |
| --- | --- |
| ![Status and action symbols](images/7350347275_DV_resource.Stream@PNG-de-DE.png) | Folder contains objects whose online and offline versions differ |
| ![Status and action symbols](images/7350393739_DV_resource.Stream@PNG-de-DE.png) | Result of comparison is either not known or cannot be displayed for the following reasons:  - No rights available for access to a protected CPU. - The loading process on the CPU was executed with a TIA Portal version earlier than V14. |
| ![Status and action symbols](images/13208514187_DV_resource.Stream@PNG-de-DE.png) | Online and offline versions of the object are identical |
| ![Status and action symbols](images/7350724107_DV_resource.Stream@PNG-de-DE.png) | Online and offline versions of the object are different |
| ![Status and action symbols](images/7350401803_DV_resource.Stream@PNG-de-DE.png) | Object only exists offline |
| ![Status and action symbols](images/7350435851_DV_resource.Stream@PNG-de-DE.png) | Object only exists online |
| ![Status and action symbols](images/84760362379_DV_resource.Stream@PNG-de-DE.png) | This comparison criterion is disabled and the associated checksum is not incorporated into the comparison result. |

The following table shows the symbols for the comparison results of an offline/offline comparison and a library comparison:

| Symbol | Description |
| --- | --- |
| ![Status and action symbols](images/20676123275_DV_resource.Stream@PNG-de-DE.PNG) | Reference program |
| ![Status and action symbols](images/20679650827_DV_resource.Stream@PNG-de-DE.PNG) | Version compared |
| ![Status and action symbols](images/20679696779_DV_resource.Stream@PNG-de-DE.PNG) | Folder contains objects of which the versions compared differ |
| ![Status and action symbols](images/20679704331_DV_resource.Stream@PNG-de-DE.PNG) | Results of the offline/offline comparison are not known |
| ![Status and action symbols](images/13208514187_DV_resource.Stream@PNG-de-DE.png) | The versions of the object compared are identical |
| ![Status and action symbols](images/20679763083_DV_resource.Stream@PNG-de-DE.PNG) | The versions of the object compared differ |
| ![Status and action symbols](images/20679770635_DV_resource.Stream@PNG-de-DE.PNG) | Object only exists in the reference program |
| ![Status and action symbols](images/20679790987_DV_resource.Stream@PNG-de-DE.PNG) | Object only exists in the version compared |
| ![Status and action symbols](images/58513235979_DV_resource.Stream@PNG-de-DE.png) | Only hardware comparison and library comparison: Although the lower-level objects of the container are identical, there are differences between the containers themselves. Such a container can be, for example, a rack or a library type. |
| ![Status and action symbols](images/58513227147_DV_resource.Stream@PNG-de-DE.png) | Only hardware comparison and library comparison: The lower-level objects of the container are different. There are also differences between the containers. Such a container can be, for example, a rack or a library type. |
| ![Status and action symbols](images/84760362379_DV_resource.Stream@PNG-de-DE.png) | This comparison criterion is disabled and the associated checksum is not incorporated into the comparison result. |

The following table shows the symbols for possible actions in a software comparison:

| Symbol | Description |
| --- | --- |
| ![Status and action symbols](images/20680132619_DV_resource.Stream@PNG-de-DE.png) | No action |
| ![Status and action symbols](images/20680140171_DV_resource.Stream@PNG-de-DE.png) | Overwrite the object of the compared version with the object from the reference program |
| ![Status and action symbols](images/20680429323_DV_resource.Stream@PNG-de-DE.png) | Overwrite the object of the output program with the object from the compared version |
| ![Status and action symbols](images/25497758091_DV_resource.Stream@PNG-de-DE.PNG) | Different actions for the compare objects in the folder (not available for library comparison) |

##### Property comparison

The property comparison compares the properties of the selected compare objects. The result is displayed with symbols. Only the property comparison is made with a manual comparison so that the status and action area remains empty. With automatic comparison, you can perform the property comparison in addition to the comparison in the comparison tables.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Set comparison criteria](#set-comparison-criteria)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)
  
[Changing the view](#changing-the-view)

#### Show and hide table columns

In a comparison, you can show or hide the columns of comparison tables as required.

##### Procedure

To show or hide table columns, follow these steps:

1. Click a column header.
2. Select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
3. To show a column, select the column's check box.
4. To hide a column, clear the column's check box.
5. In order to show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

##### Result

The columns in both the left and the right comparison table are shown or hidden.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Set comparison criteria](#set-comparison-criteria)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)
  
[Changing the view](#changing-the-view)

#### Filtering the compare editor view

You can improve the clarity of the compare editor using the following filters:

- Hiding identical comparison objects

  You can hide comparison objects which have identical offline/online or offline/offline versions. Any such comparison objects you have hidden can also be shown again at any time.
- Selecting displayed objects

  In an offline/online comparison or an offline/offline comparison for software, you can specify the objects for which the comparison results are to be shown.

##### Requirement

The compare editor is open.

##### Hiding identical comparison objects

To hide identical objects, follow these steps:

1. Click on the "Show only objects with differences" button in the toolbar.

   Only the elements that differ online and offline are displayed.

##### Showing identical comparison objects

To show identical objects again, follow these steps:

1. Click on the "Show identical and different objects" button in the toolbar.

   All elements will be displayed.

##### Selecting displayed objects

To select the objects for which comparison results should be displayed, follow these steps:

1. Perform an offline/online or an offline/offline comparison for software.
2. Click the arrow of the button "Show additional filters available" in the toolbar.
3. Select the required filter.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Set comparison criteria](#set-comparison-criteria)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)
  
[Changing the view](#changing-the-view)

#### Running a detailed comparison

> **Note**
>
> Please note the following:
>
> - Not all objects allow a detailed comparison. The project data for which you can perform a detailed comparison depends on the products installed. A detailed comparison of the hardware components is not available for hardware comparison.
> - For blocks, PLC tags and PLC data types, you can start the detail comparison directly from the project tree. You can find additional information in the section "Comparing PLC programs".
> - The detailed comparison is only available for blocks and types in the library comparison.

##### Procedure

Proceed as follows to perform a detailed comparison:

1. First, perform an offline/online comparison, an offline/offline comparison for software or a library comparison.

   The compare editor opens.
2. In the compare editor, select the object for which you want to perform a detailed comparison.
3. Click the "Start detailed comparison" button in the toolbar.

**Note**

You can only perform a detailed comparison for objects that are listed in the left as well as the right comparison table.

##### Result

The object and its associated comparison partners are opened in their appropriate editors. The editors are arranged next to each other to provide you with a quick overview of the differences. You can find more information with the description of the respective data type.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Set comparison criteria](#set-comparison-criteria)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)
  
[Changing the view](#changing-the-view)

#### Updating the comparison results

As soon as you change an object, the comparison results are no longer valid and must be updated.

> **Note**
>
> For offline/online comparisons, you should note that changes in the device may result in the system automatically updating the comparison editor if objects in the comparison are affected by the change. This can have the following results:
>
> - Some of the actions you have defined may become invalid, for example if the device no longer contains the object in question. Objects with such invalid actions will be highlighted so you can define new, valid actions.
> - The selection you made before the automatic update may also be cancelled.

##### Requirement

The comparison editor is open.

##### Procedure

To update the comparison results, follow these steps:

1. Click the "Refresh view" button in the toolbar.

   The comparison results are updated.

**Note**

Please note that the "Refresh view" button will not be available while the comparison editor is loading or synchronizing content.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Set comparison criteria](#set-comparison-criteria)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)
  
[Changing the view](#changing-the-view)

#### Set comparison criteria

You have the option to set to criteria to be taken into account for a comparison. The specified criteria are applied to all objects of a comparison, if they are available for an object. If a criterion for an object is not available, for example, "Code without comments" for data blocks, the comparison result for this checksum is considered to "match".

For a criterion that you disabled, you can still view the checksums for the overall comparison result although it is not used. Disabled comparison criteria for the property comparison are indicated by the filter icon. The filter symbol can also be displayed in the upper area of the comparison editor when no checksums should be used in the comparison result based on the selection of comparison criteria.

> **Note**
>
> With an offline/online comparison, the comparison criteria have no influence on the result of comparison in the project tree. Note that there may be different results in the project tree and comparison editor.

##### Procedure

To define the criteria to be taken into account for the comparison, follow these steps:

1. In the toolbar, click on the arrow of the "Display further comparison criteria" button.
2. Select all the criteria that should be considered for the comparison.
3. Clear all the criteria that should not be considered for the comparison.
4. Click the button with the green check mark at the bottom of the drop-down list.
5. Click on the button with the x to close the drop-down list without applying the changes.

##### Result

Only the enabled criteria are taken into account for the comparison.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)
  
[Changing the view](#changing-the-view)

#### Synchronizing non-identical objects

This section contains information on the following topics:

- [Specifying actions](#specifying-actions)
- [Synchronizing objects](#synchronizing-objects)

##### Specifying actions

If you have performed a comparison, you can specify the actions to be performed for non-identical objects in the compare editor. You cannot select any actions for identical objects. Note that you cannot execute any actions during hardware comparison.

In the case of an offline/online comparison, only synchronization actions in one direction are permitted, in order to retain program consistency. Thus, for example, you can load multiple blocks to a device or from a device, but you cannot perform a combination of loading actions in one synchronization action. In this case, the first action you set in the compare editor determines the synchronization direction. For example, if you specify for a block that the offline block is to be loaded to the device, then the other objects can also only be loaded to the device via a synchronization action. To load objects from the device again, first select the "No action" option. You can then specify the action settings again as required. Or, you can perform a new comparison.

> **Note**
>
> Note the following CPU-specific aspects when defining actions:
>
> - S7-300/400: You can define actions for the "Program blocks" folder, for folders you have created yourself or for individual blocks.
> - S7-1200/1500: You can define actions for the "Program blocks" folder, for folders you have created yourself or for individual blocks. If you have performed an offline/online comparison and select download to the device as action, a consistent download is executed. If you upload the object from the device to the project, however, you can also upload individual blocks.

###### Requirement

The compare editor is open.

###### Procedure

To select an action for a non-identical object, follow these steps:

1. In the status and action area, click in the "Action" column on the cell of the object for which you want to define an action.

   The cell changes to a drop-down list.
2. Click on the drop-down list.
3. Select the action you want.

   The action set will be carried out for the object in question the next time synchronization is performed.

   If you have accidentally changed the action you had selected, you can undo the change before the next synchronization.
4. To restore the previously set action selection, right-click the action in the status and action area that you want to restore.
5. Select the "Restore last selection" command in the shortcut menu.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Synchronizing objects](#synchronizing-objects)

##### Synchronizing objects

Synchronization executes the actions you have specified for non-identical objects. Note, however, that in the case of an offline/online comparison you can only perform actions in one direction in one synchronization action.

###### Requirement

- The compare editor is open.
- The desired actions have been selected.

###### Procedure

To synchronize objects, follow these steps:

1. Click the "Execute actions" button in the toolbar.

###### Result

The actions you specified for the objects are performed.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Specifying actions](#specifying-actions)

#### Changing the view

You can choose between a hierarchical and a flat view for the left comparison table. In the hierarchical view, the devices are shown in their structure; in the flat view, the objects of the devices are listed without structure. In the right comparison table, the objects are always displayed flat.

##### Setting the hierarchical view

To set the hierarchical view, follow these steps:

1. Click the "Display in hierarchical view" button in the toolbar of the compare editor.

##### Setting the flat view

To set the flat view, follow these steps:

1. Click the "Display in flat view" button in the toolbar of the compare editor.

---

**See also**

[Basics of project data comparison](#basics-of-project-data-comparison)
  
[Comparing offline/online](#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](#carrying-out-offlineoffline-comparisons)
  
[Overview of the compare editor](#overview-of-the-compare-editor)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Filtering the compare editor view](#filtering-the-compare-editor-view)
  
[Running a detailed comparison](#running-a-detailed-comparison)
  
[Updating the comparison results](#updating-the-comparison-results)
  
[Set comparison criteria](#set-comparison-criteria)
  
[Synchronizing non-identical objects](#synchronizing-non-identical-objects)

## Protecting project data

This section contains information on the following topics:

- [Protection concept for project data](#protection-concept-for-project-data)
- [Revoking access rights for devices](#revoking-access-rights-for-devices)

### Protection concept for project data

#### Introduction

You can protect your project data from unauthorized access. These include, for example:

- Access protection for devices
- Copy and display protection of objects
- Restrictions for printouts of know-how-protected objects

For objects with know-how protection, this protection is also retained after the object is pasted into a library. Note that every protection mechanism is not available for all objects. How to protect specific objects is described in the online help of the product.

Companies can also specify the use of a password provider to protect blocks. To do so, the central settings must be adjusted and all users must integrate the corresponding password providers in the TIA Portal. The passwords provided by a password provider can subsequently be used. You can find additional information in the section "Protecting blocks".

#### Revoking access rights for devices

If you want to execute a function that is password-protected by means of the device protection level, you are prompted to enter a password. When the password is entered correctly, you can execute the required function. The access right is retained on the device until you close the TIA Portal.

If you want to reactivate password protection while the TIA Portal is open, you can explicitly revoke the access rights for a device. As a result, certain functions for the protected device cannot be executed until the correct password is entered again. You specify the functions for which a password must be entered when you assign the device protection level.

#### Sharing protected project data

Always pass on the protected project data as project archive or library archive. In this way, you ensure that the protection measures cannot be bypassed.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Handling know-how-protected project data**  If you remove the know-how protection of an object and the TIA Portal is unexpectedly terminated before the next saving, the corresponding project data is stored unprotected in the "CrashDumpReport" and could be accessible to unauthorized persons.  To prevent access to data that is actually protected, proceed as follows:  1. Open the directory ..\Users\&lt;user_name&gt;\AppData\Roaming\Siemens\Automation\&lt;tia_version&gt;\UserDataDumps\&lt;project_name&gt; 2. Delete all files with the name extension "*.UDD". |  |

---

**See also**

[Printing project data](#printing-project-data)

### Revoking access rights for devices

#### Requirement

- A protection level has been set for the device.
- A protected function for the device has been enabled by entering the password.

#### Procedure

To revoke the access rights for the device, follow these steps:

1. Select the device for which you want to revoke access rights in the project tree.
2. Select the "Delete access rights" command in the "Online" menu.

#### Result

The access rights are revoked, and starting from now the user will be prompted to enter the password again to execute a password-protected function on the device. The function can only be executed if the correct password is entered.

If the device has an online connection, it will be disconnected.

---

**See also**

[Protection concept for project data](#protection-concept-for-project-data)

## Printing project contents

This section contains information on the following topics:

- [Printing project documentation](#printing-project-documentation)
- [Printing module labels](#printing-module-labels)

### Printing project documentation

This section contains information on the following topics:

- [Documentation settings](#documentation-settings)
- [Printout of project contents](#printout-of-project-contents)
- [Changing the print settings](#changing-the-print-settings)
- [Specifying the print layout](#specifying-the-print-layout)
- [Entering document information](#entering-document-information)
- [Managing cover pages and frames](#managing-cover-pages-and-frames)
- [Designing cover pages and frames](#designing-cover-pages-and-frames)
- [Displaying print preview](#displaying-print-preview)
- [Printing project data](#printing-project-data)

#### Documentation settings

##### Introduction

Once a project is created, the contents can be printed in an easy-to-read format. You may print the entire project or individual objects within the project. A well-structured printout is helpful when editing the project or performing service work. The printout can also be used for your customer presentations or as full system documentation.

You can prepare the project in the form of standardized circuit manuals and print it in a uniform layout. You can limit the scope of the printout. You have the option to print to the entire project, individual objects along with their properties, or a compact overview of the project. In addition, you can print the contents of an open editor.

##### Improving the printout with frames and cover pages

You can design the appearance of the printed pages according to your own requirements, for example, to add your own company logo or the corporate design of your company in the project documentation. You can create any number of design variants as frames and cover pages. The frames and cover pages are stored in the project tree under the item "Documentation settings" and are part of the project. You can insert placeholders for data from previously entered document information within the frames and cover pages. These will be filled automatically with the appropriate metadata during printing.

If you want to avoid designing your own template, there are ready-made frames and covers pages available. These include templates complying with the ISO standard for technical documentation.

##### Modular structure of a printout

An printout generally consists of the following components:

- Cover page (only when printing from the project tree)
- Table of contents (only when printing from the project tree)
- Name and path of an object within the project tree
- Object data

Printout of the cover page or the table of contents can be deactivated in the "Print" dialog.

---

**See also**

[Printing project data](#printing-project-data)
  
[Creating frames](#creating-frames)
  
[Creating a cover page](#creating-a-cover-page)
  
[Editing cover pages and frames](#editing-cover-pages-and-frames)
  
[Entering document information](#entering-document-information)
  
[Print function for module labels](#print-function-for-module-labels)

#### Printout of project contents

##### Availability of print function

The following contents can be printed:

- An entire project in the project tree
- One or more project-related objects in the project tree
- Contents of an editor
- Tables
- Libraries
- Diagnostics view of the Inspector window

It is not possible to print in the following areas:

- Portal view
- Detailed view
- Overview window
- Compare editor
- All tabs of the Inspector window, except the diagnostics view
- All task cards, except the libraries
- Most of the dialogs
- Properties and devices of the programming device/PC not related to the project, for example online portals and connected card readers.

##### Scope of printout

To be able to print, at least one printable element has to be selected.

If a selected object is printed, all subordinate objects are also printed. For example, if a device is selected in the project tree, all of its data is also printed. If you select the entire project in the project tree for printing, all project contents are printed with the exception of the graphical views. These have to be printed separately. Items in the project tree that are not part of the project cannot be printed. For example, this includes online portals and connected card readers and USB memory devices.

When table contents are printed, all lines in the table in which a cell is selected are printed. In order to print one or more table columns, the desired columns must be selected. If no individual cells or columns are selected, the entire table is printed.

##### Limitations when printing

In general, it is possible to print all objects that can be visualized on the user interface. Conversely, this means that you cannot print objects that you do not have access to. If a printout fails, possible reasons may include the following:

- A valid license does not exist for displaying an object.
- There is no device description for an object.
- A software component needed to display an object is not installed.

---

**See also**

[Printing project data](#printing-project-data)

#### Changing the print settings

##### Changing the print settings

You can specify general print settings that are retained even after the TIA Portal is closed and re-opened. Some settings are dependent on the products installed. The following settings are possible in every case:

##### Always print table data as pairs of values

If this option is selected, tables are not printed in tabular format but rather as a pairs of key and value.

Example:

| Object name | Property 1 | Property 2 |
| --- | --- | --- |
| Object A | Value A1 | Value A2 |
| Object B | Value B1 | Value B2 |

In this case, the printout has the following appearance:

**Object A**

Property 1: Value A1

Property 2: Value A2

**Object B**

Property 1: Value B1

Property 2: Value B2

##### Printing mask editors

- Always print data in tables

  All parameters of technology objects are printed in tabular format.
- Print mask graphics if possible

  If the utilized editor supports this function, the contents of the editor are not printed as a table but rather as a complete graphic as it appears on the screen.

##### Procedure

To change the print settings, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "General" group.
3. Select the desired default settings in the "Print settings" area.

   The changes are applied immediately and are retained for all projects, even after the TIA Portal is closed.

---

**See also**

[Overview of the print settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-print-settings)

#### Specifying the print layout

##### Specifying the print layout

If you do not want to rely on ready-made print templates, you can specify your own cover page or your own layout for the individual pages. Your designs are saved together with the respective project.

Your designs for the cover page and your templates for the page layout can be found in the project tree under the "Documentation information" group. You will also find metadata on the project there under the entry "Document information". For subsequent print operations, you can customize the appearance of the printout in the "Print" dialog using the saved cover pages and page layout templates and the available metadata.

##### Designing the cover page

The cover page can be customized. You can insert a background graphic and provide placeholders for text on the page. The placeholders are automatically filled with data from a documentation information during printing.

Cover pages are located in the project tree under the "Documentation information &gt; Cover pages" group.

##### Designing the content page

The regular pages of a printout can contain the following elements:

- Frame with static content, such as a company logo
- Placeholders for text, such as the name of the project, the page number, and the time the printout was started

  Several different values for the individual placeholders can be specified in the document information. Other values, such as the project name, are preassigned and are inserted automatically during printing.
- Footnote

  The footnote is always output below the content area.
- Content area

  You can specify an area where the printed content is to be embedded.

The design of the content pages is saved in Frames. The individual frames are located in the project tree under the "Documentation information &gt; Frames" group.

#### Entering document information

You can enter metadata in the document information for every project. In addition, a print frame and a cover page are specified in the document information. You can create different information, if required, to enable you to quickly switch between different document information containing different information, frames, cover pages, page sizes, and page orientations when printing. For example, this is useful if you want to generate printouts in different languages and different document information is provided for each language.

In the documentation editor, you can specify placeholders on the cover page or in the frame of the regular pages. These placeholders can be automatically replaced with metadata from the documentation information during printing.

The various document information are therefore part of the printing function and specify the print layout and print content.

##### Procedure

To add metadata, follow these steps:

1. To create new document information, double-click "Add new document information" under "Documentation information &gt; Document information" in the project tree.

   The new document information is created and opened immediately.
2. Enter a name for the set in the "Name" field.
3. Fill in the individual fields with the metadata for the project.

#### Managing cover pages and frames

This section contains information on the following topics:

- [Using cover pages and frames](#using-cover-pages-and-frames)
- [Creating frames](#creating-frames)
- [Creating a cover page](#creating-a-cover-page)
- [Using ready-made frames and cover pages](#using-ready-made-frames-and-cover-pages)

##### Using cover pages and frames

###### Uses for cover pages

You can give your plant documentation printouts a professional appearance by adding a cover page. You can design your own cover page or use ready-made cover pages. Ready-made cover pages can be adapted and stored again as a template.

Cover pages can be saved in global libraries where they are available for use across projects.

Cover pages are designed for use as a right printed page only.

###### Uses of frames

You can embed the regular pages of your plant documentation inside a consistently uniform page frame. The frame can contain placeholders for project metadata, which is stored in the document information. It can also contain graphic elements that you design yourself.

You can create your own frames or rely on ready-made page frames. You can adapt a ready-made page frame and then store it again as a new frame.

Like cover pages, frames can be saved in global libraries where they are available for use across projects.

Frames are designed for use on right printed pages only.

###### Cover pages and templates in the project tree

Cover pages and frames associated with the project are stored in the project tree under the entry "Documentation information". There are separate folders here for frames and cover pages.

The following actions are available in the project tree for cover pages and frames.

- Creating your own subfolders
- Copying and pasting
- Inserting cover pages and frames from the "Documentation templates" system library
- Copying cover pages and templates to a global library

###### Cover pages and templates in libraries

The "Documentation templates" system library contains a few cover pages and templates that are available in every project. The cover pages and templates can be moved from there to the project tree using a drag-and-drop operation. You can then adapt the cover pages and templates in the project tree according to the requirements of your project.

Cover pages and templates can be moved from the project tree to a global library. Afterwards, these are available in every project.

---

**See also**

[Library basics](Using%20libraries.md#library-basics)
  
[Overview of the "Libraries" task card](Using%20libraries.md#overview-of-the-libraries-task-card)
  
[Using ready-made frames and cover pages](#using-ready-made-frames-and-cover-pages)
  
[Designing cover pages and frames](#designing-cover-pages-and-frames)

##### Creating frames

You can create any number of frames for each project. The frames are stored in the project tree below the "Documentation information &gt; Frames" group. You can assign a frame to all document information. When you select document information for printing, its associated frame is used.

###### Procedure

To create a new frame, follow these steps:

1. Double-click the entry "Add new frame" below the "Documentation information &gt; Frames" group in the project tree.

   The "Creating frames" dialog opens.
2. Enter a name for the frame in the "Name" field.
3. Choose the paper size from the "Paper type" drop-down list.
4. Choose whether the page is to be created in portrait or landscape format in the "Orientation" drop-down list.

Click the "Add" button.

###### Result

A new frame is created. The frame is then opened automatically in the documentation editor where it can be edited.

---

**See also**

[Editing cover pages and frames](#editing-cover-pages-and-frames)
  
[Creating a cover page](#creating-a-cover-page)

##### Creating a cover page

You can create any number of cover pages for the printout for each project. The cover pages are stored in the project tree below the the "Documentation information &gt; Cover pages" group. You can assign a cover page to all document information. When you select specific document information for printing, its associated cover page is used.

###### Procedure

To create a new cover page, follow these steps:

1. Double-click the entry "Add new cover page" below the "Documentation information &gt; Cover pages" group in the project tree.

   The "Add new cover page" dialog box opens.
2. Enter a name for the cover page in the "Name" field.
3. Choose the paper size from the "Paper type" drop-down list.
4. Choose whether the page is to be created in portrait or landscape format in the "Orientation" drop-down list.

Click the "Add" button.

###### Result

A new cover page is created. The cover page is then opened automatically in the documentation editor where it can be edited.

---

**See also**

[Editing cover pages and frames](#editing-cover-pages-and-frames)
  
[Creating frames](#creating-frames)

##### Using ready-made frames and cover pages

The TIA Portal comes with some ready-made frames and cover pages. These can change according to your wishes.

###### Procedure

To create and edit the ready-made frames and cover pages, follow these steps:

1. Open the "Global libraries" pane in the "Libraries" task card.
2. In the "Templates" folder, open the "Cover Pages" or "Frames" folder.
3. Drag a cover page or a frame from one of the folders into the project tree and drop it into one of the following folders:

   - For frames: "Document information &gt; Frames"
   - For cover pages: "Document information &gt; Cover pages".

   The ready-made frame or cover page can now be used in the project.
4. Double-click on the new entry in the project tree click to edit the frame or the cover page.

---

**See also**

[Using cover pages and frames](#using-cover-pages-and-frames)
  
[Editing cover pages and frames](#editing-cover-pages-and-frames)

#### Designing cover pages and frames

This section contains information on the following topics:

- [Editing cover pages and frames](#editing-cover-pages-and-frames)
- [General operation of the documentation editor](#general-operation-of-the-documentation-editor)
- [Specifying the print area](#specifying-the-print-area)
- [Inserting placeholders for metadata](#inserting-placeholders-for-metadata)

##### Editing cover pages and frames

The documentation editor is a graphical editor which allows you to design frames and cover pages for your plant documentation. You can place images or text elements on the frame and the cover pages in the document editor. The text elements are either static or they are automatically filled during printing with the data from the document information that you have selected in the print dialog.

###### Procedure

To edit a cover page or a frame in the documentation editor, follow these steps:

1. In the project tree, double-click on the entry for an existing cover page or frame under the "Documentation information &gt; Frames " or "Documentation information &gt; Cover pages" group.

   The documentation editor opens.
2. Design the cover page or frame as desired.
3. Close the documentation editor.

   The changes to the cover page or frame are applied automatically.

---

**See also**

[Creating a cover page](#creating-a-cover-page)
  
[Creating frames](#creating-frames)
  
[General operation of the documentation editor](#general-operation-of-the-documentation-editor)

##### General operation of the documentation editor

###### Components of the documentation editor

The following figure provides an overview of the components of the documentation editor:

![Components of the documentation editor](images/75652310923_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar  The toolbar provides the following tools (from left to right):  - Arrow tool   Enables object selection. - Navigation tool   Allows shifting of the partial page. - Zoom-in button   Magnifies the page display incrementally. - Zoom-out button   Reduces the page display incrementally. - Zoom with selection   Adapts the page size to a selected work area. - Dynamic zoom   Adapts the page width to the work area. |
| ② | Work area  You can design the cover page or frame in the work area. |
| ③ | "Toolbox" task card  The "Toolbox" task card contains various types of placeholders that you can use on the cover sheet or frame. The placeholders can be placed in the work place using a drag-and-drop operation. |
| ④ | Properties in the Inspector window  You can display and modify the properties of the currently selected object in the "Properties" tab of the Inspector window. For example, you can modify the properties of the page, format text, specify the position of objects on the page, etc. |

###### Operation in the documentation editor

The following basic functions are available in the documentation editor:

- Drag-and-drop functionality

  The documentation editor is a graphic editor. which means you can place objects anywhere with the mouse. An image of the page is displayed in the work area. This image corresponds to the ultimate print layout.

  If you want to select objects on the page in order to move them or modify their properties, the arrow tool must be activated in the toolbar.
- Zoom function

  You can use the zoom function to change the size of the page display. You have two options for changing the page size:

  - Via the buttons in the toolbar

    Select the "Zoom in" or "Zoom out" magnifying glass button in the toolbar of the documentation editor. Then click on the page in order to magnify (zoom in) or reduce (zoom out) the page incrementally.

    To zoom in on a particular area, select the "Zoom with selection" tool and use the mouse to drag an outline around the area you want to focus on.

    To continuously zoom in or zoom out of the work area, use the "Dynamic zoom" tool. To magnify the page display, click anywhere on the work area, and then hold down the mouse button while dragging the mouse toward the top of the page. To reduce the page display, drag the mouse toward the bottom of the page.
  - Via the zoom bar

    You can also use the zoom bar (located in the bottom right corner of the work area) to change the display size. Select a percentage value from the drop-down list or enter a percentage value. Alternatively, you control the display size using the slider.
- Navigation over the page

  In addition to scrolling, you the option of changing the partial page with the navigation tool. To change the partial page with the navigation tool, select the Hand button in the toolbar. Then, click anywhere on the page and hold the mouse button down while moving the page to the desired position.

###### Using and adapting the positioning aids

You have various aids at your disposal to help you position elements on the page:

- Rulers

  Rulers are affixed to the page margins in the work area.
- Page grid

  A grid is placed underneath the page in the work area.

You can display, hide or adapt the positioning aids in the Inspector window under "Properties &gt; Rulers and grid". You can make the following settings:

- Units:

  Specify the unit of measurement for the grid and the rulers.
- Grid steps:

  Specify the width of the grid.
- Show grid:

  Specify whether the grid is to be displayed or hidden.
- Snap to grid:

  Specify whether objects are to be aligned automatically to the grid. If the option is selected, the grid lines function like a "magnet".
- Show rulers:

  Specify whether the rulers are to be displayed.

---

**See also**

[Editing cover pages and frames](#editing-cover-pages-and-frames)
  
[Specifying the print area](#specifying-the-print-area)
  
[Inserting placeholders for metadata](#inserting-placeholders-for-metadata)

##### Specifying the print area

An area within the frame is provided for the actual printed contents. The project data is then always inserted inside this defined and uniformly consistent area within the frame. You can adjust the size of the print area.

###### Requirement

A frame is open in the documentation editor.

###### Procedure

To define an area for the printed contents, follow these steps:

1. Click on the slightly darker area within the page display in the documentation editor to select the area for the print content.

   This opens the properties of the area to be printed in the Inspector window.
2. Enter the position of the print area on the X and Y axes in the Inspector window.
3. Specify the width and height of the print area in cm in the Inspector window.

Alternatively, you can change the width and position of the print area in the graphic display of the page. To do so, use the mouse to drag the margins of the print area until the desired size and position are achieved.

---

**See also**

[Creating frames](#creating-frames)
  
[General operation of the documentation editor](#general-operation-of-the-documentation-editor)

##### Inserting placeholders for metadata

You can provide placeholders on the cover page and in a frame. The placeholders are automatically filled with metadata from documentation information during printing, if they are placeholders for text. Alternatively, you can add non-modifiable data, such as free text or an image.

All elements are arranged in numbered Z-Orders. If objects overlap, you can determine in which sequence these are to be arranged.

###### Types of placeholders

The following types of placeholders are available to you:

- Text field

  The text field stands as a placeholder for a text element from a document information. In the properties of the text field, you set which text from a document information should be automatically inserted during printing.
- Field for date and time

  A date and time are inserted instead of the placeholder when printing. This can be the date of creation or the point in time when the last change was made to the project. In the properties of the Inspector window, you specify which date or time is printed.
- Page number

  The correct page number is automatically applied when printing.
- Free text

  You can enter freely selectable text in the properties of the text field. The text is static and is not influenced by the document information selected at the time of printing.
- Image

  Select the image file in the properties of the placeholder in the Inspector window. Images in the formats BMP, JPEG, PNG, EMF or GIF are possible.

###### Requirement

An cover page or frame is open in the documentation editor.

###### Procedure

To insert placeholders for metadata on the cover sheet or in a frame, follow these steps:

1. Drag a field from the "Toolbox &gt; Elements" task card to the work area of the documentation editor.

   The placeholder is inserted. The placeholder properties are shown in the Inspector window and can be edited there.
2. Select the metadata to be inserted during printing from the "Text" drop-down list in the Inspector window under "Properties &gt; General &gt; Text box". Alternatively, you have the option of entering free text or selecting an image depending on the type of placeholder.
3. In the Inspector window under "Properties &gt; General &gt; Position and size", specify the position of the placeholder on the X and Y axis and enter the width and height of the text box in cm. You specify the sequence of the objects in the "Z-Order" field, if these overlap. The smaller the value, the further down an object is located.
4. In the Inspector window, go to "Properties &gt; View" and select the font formatting and the orientation of the text as well as the alignment of the text. You cannot make this setting for images.

---

**See also**

[General operation of the documentation editor](#general-operation-of-the-documentation-editor)

#### Displaying print preview

This section contains information on the following topics:

- [Creating a print preview](#creating-a-print-preview)
- [Operation within the print preview](#operation-within-the-print-preview)

##### Creating a print preview

###### Creating a print preview

You can create a preview of the printout. Document information can be chosen for this, in the same way as for the actual printout. In this way, you preview the selected frame and, if applicable, the cover sheet. The settings are retained for later printing.

###### Procedure

To create a print preview and to set the scope of the later printout, follow these steps:

1. Select the "Print preview" command in the "Project" menu.

   The "Print preview" dialog opens.
2. Select the frame layout you want to use for the printout.

   - In the "Document information" drop-down list, select the documentation information you want to use later for the printout.
   - Select the "Print cover page" check box to print the cover page, which is specified in the selected document information.
   - Select the "Print table of contents" check box to add a table of contents to the printout.

   The check boxes for printing the cover page and the table of contents can only be selected if you have started the printout in the project tree.
3. Under "Print objects/area", select what is to be printed. The selection is only possible if you have started the printout from an editor that supports this function.

   - Select "All" to print out the entire content of the editor.
   - Choose "Selection" to print only the objects currently selected in the editor.
4. Select the print scope under "Properties".

   - Select "All" to print all configuration data of the selected objects.
   - Select "Visible" to print the information of an editor that is currently visible on the screen. This option can only be chosen if you have started the printout from an editor that supports this function.
   - Select "Compact" to print out an abbreviated version of the project data.
5. Click "Preview" to generate the preview.

   A print preview is created in the work area.

**Note**

**Wait time for extensive documents**

It can take several minutes to generate the print preview in the case of very extensive projects. You can continue working normally in the meantime on systems with adequate resources. The progress of the print preview is shown in the status bar.

---

**See also**

[Printing project data](#printing-project-data)
  
[Operation within the print preview](#operation-within-the-print-preview)

##### Operation within the print preview

###### Functions within the print preview

The print preview shows an exact image of the subsequent printout. You can use the buttons in the toolbar to modify the print preview display. The following functions are available (from left to right):

- Navigation mode

  Allows shifting of the partial page.

  To change the partial page with the navigation tool, select the arrow button in the toolbar. Then, click anywhere on the page and hold the mouse button down while moving the page to the desired position.
- Zoom function

  - "Zoom in" and "Zoom out"

    Magnifies or reduces the page display.

    To zoom in or zoom out the display incrementally, select the corresponding button. Then click on the page in order to magnify (zoom in) or reduce (zoom out) the page incrementally.

    To zoom in on a particular area, enable the "Zoom with selection" icon and use the mouse to drag an outline around the area you want to focus on.

    To zoom dynamically through the page, select the button "Zoom in / zoom out dynamically". With pressed mouse button, scroll down over the page to zoom in. Scroll up to zoom out.
  - Percentage value in the drop-down list

    Specifies the display size of the page in percent.

    Enter a percentage value or select a percentage value from the drop-down list. Alternatively, choose the "Fit to page" option from the drop-down list to adapt the page size to the work area. Or, choose "Fit to width" to adapt the page width to the work area.
- "Forward" and "Backward"

  Each change in the partial page, the page count, or the display size is saved in a history in the background. You can use the "Forward" or "Backward" button to return to the previous view or the next view.
- Page navigation

  - "First page"

    Jumps to the first page
  - "Previous page"

    Goes to the previous page.
  - "Page number" input field

    Shows the current page. To jump directly to a page, enter the page number of the page you want to view.
  - "Next page"

    Goes to the next page.
  - "Last page"

    Jumps to the last page.

---

**See also**

[Creating a print preview](#creating-a-print-preview)

#### Printing project data

You have two options for printing out project data:

- Print immediately using default settings by means of the "Print" button in the toolbar.

  The button is only active if a printable object is selected.
- Printout with additional setting options with the "Project &gt; Print" menu command.

  For example, you can choose a different printer or specific documentation information or you can specify whether a cover page and table of contents are to be printed. In addition, you can specify the print scope or display a print preview prior to printing.

##### Requirement

- At least one printer is configured.
- The objects to be printed are not protected.

  The print scope for protected objects is limited. Disable the know-how protection to print the objects in full.

##### Printing project data

To print out data from the current project or the entire project with additional setting options, follow these steps:

1. Select the entire project in the project tree in order to print out the entire project. To print only individual elements within a project, select them in the project tree.
2. Select the "Print" command in the "Project" menu.

   The "Print" dialog opens.
3. Select the printer in the "Name" box.
4. Click "Advanced" to modify the Windows printer settings.
5. Select the frame layout you want to use for the printout.

   - Select the documentation information in the "Document information" drop-down list.

     The frame stored in the document information is used for the printout. All placeholders within the chosen frame are filled with the metadata from the selected document information.
   - Select the "Print cover page" check box to print the cover page, which is stored in the selected document information.
   - Select the "Print table of contents" check box to add a table of contents to the printout.

   The check boxes for printing the cover page and the table of contents can only be selected if you have started the printout in the project tree.
6. Under "Print objects/area", select what is to be printed. The selection is only possible if you have started the printout from an editor that supports this function.

   - Select "All" to print out the entire content of the editor.
   - Select "Selection" to print only the objects currently selected in the editor.
7. Select the print scope under "Properties".

   - Select "All" to print all configuration data of the selected objects.
   - Select "Visible" to print the information of an editor that is currently visible on the screen. This option can only be chosen if you have started the printout from an editor.
   - Select "Compact" to print out an abbreviated version of the project data.
8. Click "Preview" to generate a print preview in advance.

   A print preview is created in the work area.
9. Click "Print" to start the printout.

> **Note**
>
> **Scope of the "Print" dialog**
>
> The options available in the "Print" dialog vary depending on the elements to be printed.

##### Result

The project data is prepared in the background for printing and then printed on the selected printer. The status bar shows the progress of the print operation. You can continue working normally while data is being prepared for printing.

The print results and any errors or warnings are listed in the Inspector window under "Info" at the conclusion of the print job.

##### Canceling a print job

To cancel an active print job, follow these steps:

1. Click the blue cross in the status bar next to the progress display for the printout.

   The printout is aborted.

---

**See also**

[Protection concept for project data](#protection-concept-for-project-data)
  
[Revoking access rights for devices](#revoking-access-rights-for-devices)
  
[Documentation settings](#documentation-settings)
  
[Printout of project contents](#printout-of-project-contents)
  
[Designing cover pages and frames](#designing-cover-pages-and-frames)

### Printing module labels

This section contains information on the following topics:

- [Print function for module labels](#print-function-for-module-labels)
- [Printing labels](#printing-labels)
- [Exporting labeling data as XML](#exporting-labeling-data-as-xml)
- [XML schema of the export file](#xml-schema-of-the-export-file)
- [Determining the print area offset](#determining-the-print-area-offset)

#### Print function for module labels

##### Printing of module labeling strips for hardware modules

You can print labeling strips for the modules in your project with the help of the TIA Portal. The labeling strips are custom-fit to each module and can contain the following printed information:

- Symbolic name of the input or output
- Absolute address of the input or output
- Symbolic name and additionally the absolute address of the input or output. The order of the information can be specified.

The modules are displayed graphically in the device view. If you set the zoom level in the device view to at least 200%, the labels for the individual modules will be visible. The printout on the labeling strip corresponds to the representation of the labeling in the device view.

The following figure shows an example of two modules in the device view on which the labeling of the inputs and outputs is visible:

![Printing of module labeling strips for hardware modules](images/69171534219_DV_resource.Stream@PNG-de-DE.png)

##### Export and further editing as Microsoft Word file

The labeling strips are first exported as a Microsoft Word file (.docx) before they are printed. The file can be further edited with commonly available word processing programs such as Microsoft Word. The individual labeling strips are represented as a table in the .docx file.

The character spacing of the text within the table is adapted by default, so that texts are not truncated. If you want to prevent this from stretching or compressing the text too much, change the character spacing of the text in the table cell properties.

##### Printing the labeling data to an XML file

As an alternative to printing the labeling strips, you can output the addresses of the inputs and outputs of a module to an XML file. You can use the export to an XML file for devices for which no ready-made labeling strips are available. You can also use the export to an XML file to create labeling strips with another program. The program must be able to transform the data of the XML file into an input format that is suitable for the labeling system. The schema of the XML file is available in the section "[XML schema of the export file](#xml-schema-of-the-export-file)".

##### Print media

You can print the labeling strips either on ready-made print sheets or on standard DIN A4 paper. You can separate the individual labeling strips from the ready-made print sheets and insert them in the designated labeling areas of your modules. If you print on standard paper, the individual labeling strips must be cut out. Cut marks are automatically included on the printout and serve as aids.

Because the paper feeds of printers differ slightly, the printout may be slightly offset on the paper. When the labeling strips are printed on ready-made sheets, printing that is accurate to the millimeter is important. Otherwise, the text will not be fit exactly inside the stamped area. In addition, if the printing is imprecise, the labeling of an input or output may no longer be congruent with the channel status displays of the module. To ensure precise printing, you can enter an offset value for your printer in the TIA Portal. For information on how to determine the proper offset value for your printer, refer to Chapter "[Determining the print area offset](#determining-the-print-area-offset)".

---

**See also**

[Exporting labeling data as XML](#exporting-labeling-data-as-xml)
  
[XML schema of the export file](#xml-schema-of-the-export-file)
  
[Printing labels](#printing-labels)
  
[Determining the print area offset](#determining-the-print-area-offset)
  
[Documentation settings](#documentation-settings)

#### Printing labels

You can print labeling strips for the modules in your project if provision has been made for attaching labels to the utilized modules. The labels are first exported to a Microsoft Word file (.docx). A separate .docx file is created for each module family (for example, for all selected S7-1500 modules). The labels are always printed from the word processing program.

##### Requirement

The following requirements apply to printing of labeling strips:

- The chosen modules must support the printing of labels. Otherwise, the data can only be output to an XML file.
- A word processing program that supports Microsoft Word DOCX files must be installed, e.g., Microsoft Word 2010 or later.
- You need the ready-made labels for your modules or commercially available DIN A4 paper.

##### Procedure

To print labeling strips for hardware modules, follow these steps:

1. In the project tree, select the modules for which you want to print labeling strips.

   - You can select one or more stations in order to print out labeling strips for all modules plugged into these stations.
   - Alternatively, select the desired modules below the stations in the "Local modules" folder.
2. Right-click one of the devices, and select the "Export labeling strips" command from the shortcut menu.

   The "Export labeling strips" dialog opens.
3. In the "Content of the labeling strip" area, select the data to be printed on the labeling strip:

   - Select "Symbolic name" in order to print the symbolic name of the input or output (corresponds to the contents of the "Name" column in the IO tag table).
   - Select "Absolute address" in order to print the absolute address of the input or output (corresponds to the contents of the "Address" column in the IO tag table).
   - Select "Absolute and symbolic address" or "Symbolic and absolute address" in order to print both addresses. Printing takes place according to the specified order.
4. In the "Export format" area, define how the labeling data will be output.

   - Select "Print on SIEMENS labeling sheet" if you are printing on a ready-made label sheet for your modules.
   - Select "Print on plain DIN A4 page" if you are printing on standard DIN A4 paper.
5. Select correction values for your printer in the "Offset print area", if required. The correction values are used for correct alignment of the print area. Correction values are only necessary if you are printing on ready-made labeling strips.

   - Enter a correction value, in millimeters, in the "Vertical offset" field. A negative value shifts the print area upward. A positive value shifts the print area downward.
   - Enter a correction value, in millimeters, in the "Horizontal offset" field. A negative value shifts the print area to the left. A positive value shifts the print area to the right.
6. In the "Path" field, select the path where the exported files will be stored.
7. Click the "Export" button to start the export.

   The export files are created.
8. Open the DOCX files with a conventional word processing program, such as Microsoft Word, and change the design of the labeling strips if necessary.
9. Print out the labeling strips from your word processing program. Use the paper that you specified in the Export dialog for this.
10. If you are using ready-made sheets, separate the labeling strips at the stamped lines provided for that purpose. When standard DIN A4 paper is used, you must cut out the labeling strips.

---

**See also**

[Determining the print area offset](#determining-the-print-area-offset)
  
[Exporting labeling data as XML](#exporting-labeling-data-as-xml)

#### Exporting labeling data as XML

The TIA Portal supports a large number of different modules and can be continually expanded using Hardware Support Packages, for example. Ready-made labeling strips are not available for every supported module. However, you can still use the TIA Portal to label inputs and outputs of modules that are not supported. First, you export the absolute and symbolic addresses of the inputs and outputs to a standardized XML file. Then, you import the XML file to an external program for printing the labels. In this program, you prepare the data to suit your modules and print out the labels.

##### Procedure

To export labeling data for hardware modules as XML, follow these steps:

1. In the project tree or network view, select the modules for which you need labeling strips.

   - You can select one or more stations in order to export the input and output addresses of all modules plugged into these stations.
   - Alternatively, select the desired modules below the stations in the "Local modules" folder.
2. Right-click one of the devices and select the "Export module labeling strips" command from the shortcut menu.

   The "Export labeling strips" dialog opens.
3. In the "Export format" area, select the "Export to XML file" option.
4. In the "Path" field, select the path where the XML file will be stored.
5. Click the "Export" button to start the export to an XML file.

   The XML file is created with the name "&lt;Project name&gt;_IO_Channels.xml".

---

**See also**

[XML schema of the export file](#xml-schema-of-the-export-file)
  
[Print function for module labels](#print-function-for-module-labels)
  
[Printing labels](#printing-labels)

#### XML schema of the export file

##### XML schema of an export file

The XML file for module labeling strips is structured according to the following schema:

&lt;?xml version="1.0" encoding="utf-8"?&gt;

&lt;xs:schema targetNamespace="http://tempuri.org/XMLSchema.xsd" elementFormDefault="qualified" xmlns:mstns="http://tempuri.org/XMLSchema.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema"&gt;

&lt;xs:element name="Stations"&gt;

  &lt;xs:complexType&gt;

   &lt;xs:sequence&gt;

    &lt;xs:element name="Station" maxOccurs="unbounded"&gt;

    &lt;xs:complexType&gt;

      &lt;xs:sequence&gt;

        &lt;xs:element name="Rack" maxOccurs="unbounded"&gt;

        &lt;xs:complexType&gt;

         &lt;xs:sequence&gt;

          &lt;xs:element name="Module" maxOccurs="unbounded"&gt;

          &lt;xs:complexType&gt;

          &lt;xs:sequence&gt;

           &lt;xs:element name="IOChannel" maxOccurs="unbounded"&gt;

           &lt;xs:complexType&gt;

           &lt;xs:sequence&gt;

            &lt;xs:element name="Address" type="xs:string"&gt;&lt;/xs:element&gt;

            &lt;xs:element name ="Tag" type="xs:string"&gt;&lt;/xs:element&gt;

           &lt;/xs:sequence&gt;

          &lt;xs:attribute name="Number" type="xs:int"&gt;&lt;/xs:attribute&gt;

          &lt;/xs:complexType&gt;

          &lt;/xs:element&gt;

         &lt;/xs:sequence&gt;

         &lt;xs:attribute name="Name"&gt;&lt;/xs:attribute&gt;

        &lt;/xs:complexType&gt;

         &lt;/xs:element&gt;

        &lt;/xs:sequence&gt;

       &lt;xs:attribute name="Name" type="xs:string"&gt;&lt;/xs:attribute&gt;

       &lt;/xs:complexType&gt;

      &lt;/xs:element&gt;

      &lt;/xs:sequence&gt;

       &lt;xs:attribute name="Name" type="xs:string"&gt;&lt;/xs:attribute&gt;

    &lt;/xs:complexType&gt;

  &lt;/xs:element&gt;

  &lt;/xs:sequence&gt;

  &lt;/xs:complexType&gt;

  &lt;/xs:element&gt;

&lt;/xs:schema&gt;

##### Example of an XML file

The following example shows an XML file that contains the labeling data for an S7-1500 CPU with a digital input module and an analog input module:

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;Stations&gt;

&lt;!-- The CPU is specified first --&gt;

  &lt;Station Name="S71500/ET200MP-Station_1"&gt;

    &lt;Rack Name="Rack_0"&gt; &lt;!-- Name of the rack --&gt;

      &lt;Module Name="Sample S7-1500" /&gt; &lt;!-- Name of the CPU --&gt;

      &lt;Module Name="DI 16x24VDC BA_1"&gt; &lt;!-- Name of the digital input module --&gt;

&lt;!-- The individual channels of the digital input module are specified --&gt;

        &lt;IOChannel Number="0"&gt;

          &lt;Address&gt;%I0.0&lt;/Address&gt;

          &lt;Tag&gt;Input Value 1&lt;/Tag&gt; &lt;!-- Symbolic address of input 0 --&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="1"&gt;

          &lt;Address&gt;%I0.1&lt;/Address&gt;

          &lt;Tag&gt;Input Value 2&lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="2"&gt;

          &lt;Address&gt;%I0.2&lt;/Address&gt;

          &lt;Tag&gt;Input Value 3&lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;!-- All other channels follow --&gt;

      &lt;/Module&gt;

      &lt;Module Name="AI 4xU/I/RTD/TC ST_1"&gt; &lt;!-- Name of the analog input module --&gt;

&lt;!-- The individual channels of the analog input module are specified --&gt;

        &lt;IOChannel Number="0"&gt;

          &lt;Address&gt;%IW2&lt;/Address&gt;

          &lt;Tag&gt; &lt;!-- Symbolic addresses are not specified for the analog input module. --&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="1"&gt;

          &lt;Address&gt;%IW4&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="2"&gt;

          &lt;Address&gt;%IW6&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="3"&gt;

          &lt;Address&gt;%IW8&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

      &lt;/Module&gt;

      &lt;Module Name="Sample S7-1500" /&gt;

      &lt;Module Name="DI 16x24VDC BA_1"&gt;

        &lt;IOChannel Number="0"&gt;

          &lt;Address&gt;%I0.0&lt;/Address&gt;

          &lt;Tag&gt;Input Value 1&lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="1"&gt;

          &lt;Address&gt;%I0.1&lt;/Address&gt;

          &lt;Tag&gt;Input Value 2&lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="2"&gt;

          &lt;Address&gt;%I0.2&lt;/Address&gt;

          &lt;Tag&gt;Input Value 3&lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;!-- All other channels follow --&gt;

      &lt;/Module&gt;

      &lt;Module Name="AI 4xU/I/RTD/TC ST_1"&gt;

        &lt;IOChannel Number="0"&gt;

          &lt;Address&gt;%IW2&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="1"&gt;

          &lt;Address&gt;%IW4&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="2"&gt;

          &lt;Address&gt;%IW6&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

        &lt;IOChannel Number="3"&gt;

          &lt;Address&gt;%IW8&lt;/Address&gt;

          &lt;Tag&gt;

          &lt;/Tag&gt;

        &lt;/IOChannel&gt;

      &lt;/Module&gt;

    &lt;/Rack&gt;

  &lt;/Station&gt;

&lt;/Stations&gt;

---

**See also**

[Exporting labeling data as XML](#exporting-labeling-data-as-xml)

#### Determining the print area offset

If you are using a ready-made label sheet, the printing on it must be applied precisely so that the text is properly oriented on the prestamped labels and will have the proper fit relative to the channel status displays of the module. However, the paper feeds vary slightly from one printer to another. For this reason, you must enter a suitable correction value for your printer in the TIA Portal, if necessary. The print area is then shifted in the exported .docx file in such a way that the printing fits precisely on the ready-made label sheet.

The settings for shifting the print area are stored for the specific Windows user. If you log on to Windows using a different user name, you have to enter the correction values again.

The procedure for determining the correction value for your printer is described below.

##### Requirement

- You require a ready-made label sheet.
- You must have access to the actual printer that you will use subsequently for the printout. The printer must be made ready for printing on standard DIN A4 paper.

##### Procedure

To determine the correction value for your printer, follow these steps:

1. Print out a label sheet on standard DIN A4 paper, as described in Chapter "[Printing labels](#printing-labels)".
2. Compare the printout on the DIN A4 paper with the ready-made label sheet.
3. If the print area is offset, you must use correction values.

   - Using a ruler, measure the horizontal offset relative to the ready-made label sheet. This will be entered later in the "Horizontal offset" field of the Export dialog box for the printing. If the print area is offset to the right, a negative correction value must be entered. If the print area is offset to the left , a positive correction value must be entered.
   - Using a ruler, measure the vertical offset relative to the ready-made label sheet. This will be entered later in the "Vertical offset" field of the Export dialog box for the printing. If the print area is offset downward, a negative correction value must be entered. If the print area is offset upward, a positive correction value must be entered.

## Working with multi-language projects

This section contains information on the following topics:

- [Project text basics](#project-text-basics)
- [Categories of user texts](#categories-of-user-texts)
- [Select project languages](#select-project-languages)
- [Setting the editing language](#setting-the-editing-language)
- [Translating all project texts in tabular form](#translating-all-project-texts-in-tabular-form)
- [Translating project texts of individual objects](#translating-project-texts-of-individual-objects)
- [Translating project texts using reference texts](#translating-project-texts-using-reference-texts)
- [Exporting project texts](#exporting-project-texts)
- [Importing project texts](#importing-project-texts)
- [Application examples for multilanguage projects](#application-examples-for-multilanguage-projects)

### Project text basics

#### Texts in different languages in the project

When you enter texts while working on a project, you would normally do this in your own language. If you then pass on the project to someone else who does not know this language, this person will require a translation of the relevant texts to a language they know. This is why all texts can be translated. In this way, you can ensure that anyone who is subsequently confronted with the texts sees the texts in his/her language of choice.

#### Project language

Project languages are all languages in which a project will later be used. Based on the editing language, all the texts can be translated to the various project languages. You specify the languages that will be available in the project tree under "Languages &amp; Resources &gt; Project languages".

#### Editing language

Every project has an editing language. When you enter texts, these are always created in the editing language. You should therefore make sure that the editing language set is the language in which you enter the texts. This avoids problems if you translate the texts later.

The editing language does not depend on the language of the user interface. You could, for example, set English as the user interface language, but use Italian as the editing language. If you enter texts, these will be created in the project language "Italian" in this case, although the user interface of the TIA Portal is displayed in English.

You set the editing language in the project tree under "Languages &amp; Resources &gt; Project languages &gt; Editing language".

#### Reference language

The reference language is used as a template for translation. The text is displayed in the reference language for each text box in the "Tasks &gt; Languages and resources" task card. You therefore know which text that belongs in a text box, even when no text is entered in the currently selected editing language.

You set the reference language in the project tree under "Languages &amp; Resources &gt; Project languages &gt; Reference language".

#### User texts and system texts

For clarification purposes, a distinction is made between user texts and system texts:

- User texts are texts that the user created.
- System texts are texts that are created automatically according to the configuration in the project.

You manage the project texts in the project tree under "Languages &amp; Resources &gt; Project texts".

#### Examples of multilingual project texts

You can, for example, manage the following project texts in more than one language:

- Block titles and block comments
- Network titles and network comments
- Comments in tables
- Alarm texts
- Operator-relevant texts
- Text lists
- Labels of buttons
- Display names of recipes

#### Translating texts

The following procedures are available to translate texts.

- Translate all texts used in the project in tabular form

  You can enter the translations for the individual project languages directly in the "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts".
- Specify text assigned to individual objects in the Inspector window

  In the Inspector window, you can translate the texts that are assigned to the currently selected objects. Columns are displayed in a table for all available project languages. You can enter the translations for each text in the columns.
- Translating texts using reference texts

  You can change the editing language for shorter texts. All the text cells are filled again with the default values and can be filled in the current language. As orientation, you can display what you last entered in the box in the reference language. To do this, select the "Tasks" task card and open the "Languages &amp; resources" pane.
- Exporting texts and translating them externally

  With larger volumes of text, you can export the texts to an Office Open XML file and translate them in a conventional table calculation program. You then import the translated list again into the TIA Portal.

> **Note**
>
> **Using East Asian project languages**
>
> You need Microsoft Windows at least in the Professional version or higher to display East Asian project languages. Microsoft Windows in the Professional version must be installed in the local language. With the "Ultimate" or "Enterprise" versions, it is sufficient to install the appropriate language pack.

---

**See also**

[Text lists](#text-lists)
  
[Select project languages](#select-project-languages)
  
[Translating all project texts in tabular form](#translating-all-project-texts-in-tabular-form)
  
[Setting the editing language](#setting-the-editing-language)
  
[Translating project texts of individual objects](#translating-project-texts-of-individual-objects)
  
[Overview of the program settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-program-settings)
  
[Changing the settings](Introduction%20to%20the%20TIA%20Portal.md#changing-the-settings)
  
[Application examples for multilanguage projects](#application-examples-for-multilanguage-projects)

### Categories of user texts

The following categories of user texts can be selected during export:

- Formatted alarm text
- HMI scree
- HMI comments
- HMI Runtime
- Category for text lists
- Multilingual text category
- Alarm class text
- Alarm text
- SiVArc configuration
- Other text categories

### Select project languages

All the texts can be displayed within a project in the same language that you selected for your software user interface. This means that all project texts must exist in the corresponding language. You can select the available project languages yourself.

#### Procedure

To select the project languages, follow these steps:

1. Click on the arrow symbol to the left of "Languages &amp; Resources" in the project tree.

   The elements below this are displayed.
2. Double-click on "Project languages".

   In the work area, you will see a list of languages that you can select.
3. Select the required languages.

#### Result

All texts can be displayed in the activated languages if there is already a translation for these languages.

### Setting the editing language

All the texts in the project are created in the editing language when they are entered. If you change the editing language, all future text input will be stored in the new editing language.

#### Procedure

To change the editing language, follow these steps:

1. Click on the arrow symbol to the left of "Languages &amp; Resources" in the project tree.

   The lower-level elements are displayed.
2. Double-click on "Project languages".

   The possible settings for the project languages are displayed in the work area.
3. Select the editing language in "General &gt; Editing language".

### Translating all project texts in tabular form

You can display and edit all project text used in the currently open project in a list. User and system texts are separated into two different lists for clarity. Both lists contain a column for each project language. Enter the translations of the texts in the respective columns.

#### Requirement

You have selected at least one further project language.

#### Procedure

To translate text in the project-wide list, follow these steps:

1. Click on the arrow symbol to the left of "Languages &amp; Resources" in the project tree.

   The elements below this are displayed.
2. Double-click "Project texts".

   A list with the user texts in the project is displayed in the work area.
3. Click on "System texts" if you you want to edit the list of system texts rather than the user texts.
4. You can improve the clarity of the lists if you have a lot of texts.

   - To group identical texts and to translate them all at once, click the "Switch on/off grouping" button in the toolbar.
   - To hide texts that do not have a translation, click the "Filter for empty texts on/off" button in the toolbar.
   - To further limit the displayed project texts to certain devices, select the devices for which you want to display project texts in the drop-down list.
5. Enter the translation of the project texts in the relevant column.

### Translating project texts of individual objects

If you want to edit the text of individual objects, it would be too difficult to locate the matching text in the table with all project texts. For this reason, there is a table in the Inspector window in which only the texts assigned to the currently selected objects are displayed. In the table, you can add missing translations for individual project languages or change existing texts.

#### Requirement

Enter a text in at least one project language for the texts to be translated.

#### Procedure

To edit the text of the currently selected object, follow these steps:

1. Select the object whose text you want to edit.
2. Open the "Properties" tab in the Inspector window.
3. Open the lower-level "Texts" tab in the inspector window.

   A table with all the texts that belong to the selected objects is displayed. The table contains one column for the currently selected editing language and the reference language, as well as additional columns for the other project languages.
4. Add or change the entries in the table for each project language.

---

**See also**

[Inspector window](Configuring%20devices%20and%20networks.md#inspector-window)
  
[Application examples for multilanguage projects](#application-examples-for-multilanguage-projects)

### Translating project texts using reference texts

#### Introduction

After changing the editing language, all texts are shown in input boxes in the new editing language. If there is not yet a translation available for the newly set language, the input boxes are empty.

If you enter text in an input box, this is saved in the current editing language. Following this, the texts exist in two project languages for this input field, in the previous editing language and in the current editing language. This makes it possible to create texts in several project languages.

You can display existing translations for an input box in other project languages. These serve as a comparison for text input in the current editing language and they are known as the reference language.

> **Note**
>
> The display of reference texts depends on the installed products and is not supported by every editor.

#### Requirement

There is at least one translation into a different project language for an input field.

#### Procedure

To display the translation of an input cell in a reference language, follow these steps:

1. In the "Tasks" task card, select the "Languages &amp; Resources" pane.
2. Select a reference language from the "Reference language" drop-down list.

#### Result

The reference language is preset. If you click in a text box, translations that already exist in other project languages are shown in the "Tasks &gt; Languages &amp; Resources" task card.

### Exporting project texts

You can export project texts for translation and then reimport them. The texts are exported to an Office Open XML file with the extension ".xlsx". This can be edited in Microsoft Excel or a number of other spreadsheet programs.

The following export options are available:

- Exporting individual project texts

  You can select individual texts in the project texts editor and then export the selected texts.
- Exporting project texts of a device

  When you have selected a device, the "Properties &gt; Texts" tab of the Inspector window includes all texts that are part of the respective device. Here you can export all texts that are part of the respective device.
- Exporting all user texts or system texts at once

  You can either export all texts in the project or further limit the export by categories.

> **Note**
>
> **Row limit in Microsoft Excel**
>
> Note that spreadsheet programs may be able to process only a certain number of rows. Microsoft Excel 2003 supports a maximum of 65536 rows, for example. Later versions of Microsoft Excel support significantly more rows.

#### Exporting individual project texts

To export individual project texts, follow these steps:

1. Open the "Languages &amp; Resources" folder in the project tree.

   The lower-level elements are displayed.
2. Double-click "Project texts".

   The project texts editor opens.
3. Choose the "User texts" or "System texts" tab in the editor, depending on which texts you want to export.
4. Select the project texts you want to export.
5. Click "Export project texts" on the editor toolbar.

   The "Export" dialog box opens.
6. In the "Source language" drop-down list, select the reference language from which you want to translate.
7. In the "Target language(s)", select the editing language into which you want to translate the texts. The dialog contains the project languages you specified previously.

   If the required language is missing, you must first specify it in the project languages editor.

   If you want to export all editing languages, select the "Select all" option.
8. Specify a file path and a file name for the export file in the "Select file for export" input box.
9. Click "Export".

#### Exporting project texts of a device

To export project texts that are part of a specific device, follow these steps:

1. Select the device and open the device properties in the Inspector window.
2. Open the "Texts" tab in the Inspector window.
3. From the drop-down list in the function list select the texts to be exported:

   - All texts
   - ProDiag / GRAPH: Alarm texts
   - ProDiag / GRAPH: Texts for HMI display
   - ProDiag / GRAPH: All texts
4. Click the "Export project texts" icon in the toolbar.

   The "Export" dialog box opens.
5. In the "Source language" drop-down list, select the reference language from which you want to translate.
6. In the "Target language(s)", select the editing language into which you want to translate the texts. The dialog contains the project languages you specified previously.

   If the required language is missing, you must first specify it in the project languages editor.

   If you want to export all editing languages, select the "Select all" option.
7. Specify a file path and a file name for the export file in the "Select file for export" input box.
8. Click "Export".

#### Exporting all system or user texts

To export all project texts, follow these steps:

1. Select the "Export project texts" command in the "Tools" menu.

   The "Export" dialog box opens.
2. In the "Source language" drop-down list, select the reference language from which you want to translate.
3. In the "Target language(s)", select the editing language into which you want to translate the texts. The dialog contains the project languages you specified previously.

   If the required language is missing, you must first specify it in the project languages editor.

   If you want to export all editing languages, select the "Select all" option.
4. In "Select content", select the check box "User texts" to export user texts. To export system texts, select "System texts". To export both user texts and system texts, select both check boxes.
5. In "Select content", select the required text categories for the user texts or the system texts.
6. In the "Export file" input field, specify a file name for the export file.
7. In the "Path" input field, select a path in the data system to which the export file is to be saved.
8. Click "Export".

---

**See also**

[Importing project texts](#importing-project-texts)
  
[Application examples for multilanguage projects](#application-examples-for-multilanguage-projects)

### Importing project texts

After external compilation in a table calculation program, you import the project texts into the TIA Portal. You can import the project texts at the following locations:

- The "Tools" menu
- In the toolbar of the project texts editor
- In the properties of a device

  When you have selected a device, the "Properties &gt; Texts" tab of the Inspector window includes all texts that are part of the respective device. You can also import the texts of the device at this location.

> **Note**
>
> **Importing source language**
>
> If you have exported project texts in the source language and want to import them again, enable the option "Import source language" in the "Import" dialog.

> **Note**
>
> **Importing project texts into protected projects**
>
> If your project is protected, you need the corresponding function rights to import projects. Additional information can be found at "[Basics of user management in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)" and "[Overview of function rights](Managing%20users%20and%20roles.md#overview-of-function-rights)".

> **Note**
>
> **Importing project texts after saving under a new project name**
>
> If you have saved a project under a different project name using the menu command "Project &gt; Save as...", previously exported project texts can no longer be imported into this project.

#### Importing project texts

To import a file containing project texts, follow these steps:

1. Select the "Import project texts" command in the "Tools" menu.

   Alternatives:

   - Click the "Import project texts" icon in the toolbar of the project texts editor.
   - Select a device and open its properties in the Inspector window. Open the "Texts" tab and click the "Import project texts" icon in the toolbar.
2. The "Import" dialog box opens.
3. Select the path and the file name of the import file from the "Select file for import" field.
4. Select the "Import source language" check box if you have made changes to the source language in the export file and you want to overwrite the entries in the project with the changes.
5. Click "Import".

---

**See also**

[Exporting project texts](#exporting-project-texts)

### Application examples for multilanguage projects

Let us assume you are working in a team with colleagues some of whom speak English, some French and some German. You have created a project with the TIA Portal and have already created a functioning configuration.

To allow your other colleagues to be able to keep track of the project, you would like all devices being used to have comments in English and German. First, you would like to enter the comments in German. Following this, to save time and costs, you want to have the texts translated into English in a spreadsheet program by an external translation office.

In addition to this, you also want a single comment for a particular device in French so that your French-speaking colleague can continue working on this device.

The section below describes an example of how you can achieve this with the tools of the TIA Portal.

#### Translating the project into English

To enter the comments in German and to have them translated into English later, follow these steps:

1. Set the editing language to "German" and fill all the comment boxes with the relevant texts in German.

   On the device selected from the French-speaking colleague, enter, for example "Unser neues Gerät" in German first.

   All the comments are now stored in German.
2. Export all user texts to an Office Open XML file with the extension ".xlsx".
3. Have the user texts contained in the file translated into English in a spreadsheet program such as Microsoft Excel.
4. Import the file into the TIA Portal after it has been translated.

   All texts are now available in German and English.

#### Translating a single comment field to French

To translate an individual comment field to French, follow these steps:

1. Open the comment box for the device on which the French-speaking colleague will be working.
2. Open the "Languages &amp; resources" pane in the "Tasks" task card.
3. Set "French" as the editing language in the "Languages &amp; Resources" pane. As the reference language, set, for example, "English".

   Since no translation has yet been installed in French, the comment box is empty. In the "Languages &amp; Resources" pane, the English translation "Our new device" is displayed as a reference.
4. Orientating yourself on the English reference text enter "Notre nouvel appareil" in the comment box.

   The comment for this device is now available in the languages German, English and French.

---

**See also**

[Project text basics](#project-text-basics)
  
[Exporting project texts](#exporting-project-texts)
  
[Translating project texts of individual objects](#translating-project-texts-of-individual-objects)

## Working with text lists

This section contains information on the following topics:

- [Text lists](#text-lists)
- [Creating user-defined text lists](#creating-user-defined-text-lists)
- [Editing user-defined text lists](#editing-user-defined-text-lists)
- [Editing system-defined text lists](#editing-system-defined-text-lists)
- [Copying or moving text lists](#copying-or-moving-text-lists)
- [Exporting text lists](#exporting-text-lists)
- [Importing text lists](#importing-text-lists)

### Text lists

#### Introduction

You can centrally manage texts to be referenced in alarms. All the texts are stored in text lists. Each text list has a unique name with which you can call up its content. A range of values is assigned to each text in a text list. If a value from a range of values occurs, the corresponding text is called up.

All the texts can be translated to all project languages. Here, you have two options available:

- You can enter the translation of the texts in a list. You will find the list in the project tree under "Languages &amp; Resources &gt; Project texts".
- You can export all texts to a file in Office Open XML format and enter the translation in a spreadsheet program. The translations can then be imported again. Only export the data to areas that are protected with appropriate access mechanisms. Only import files that originate from trusted sources.

Each device in a project can have its own text lists. Device-specific text lists relate to only one device in the project and are therefore only valid for this device. For this reason, they are arranged under a device in the project tree. Device-specific text lists can be user-defined or created by the system.

#### Text lists editor

The text lists editor is divided into a bottom and top area. The top area displays the individual text lists. As soon as you select a text list, the included texts and the associated value ranges are displayed in the lower area. You can sort the table columns in the text lists editor in ascending and descending order by clicking the table header of the respective column.

#### User-defined and system-defined text lists

There are two types of text lists:

- User-defined text lists

  You can create user-defined text lists yourself and fill them with texts; in other words, you can specify value ranges and the corresponding texts yourself. With user-defined text lists, the name of the text list begins with "USER" as default. You can change this name to any suitable name.
- System-defined text lists

  System-defined text lists are created by the system. These always involve texts relating to devices. They are automatically created as soon as you insert a device in the project. With system alarms, the name of the text list begins with "SYSTEM". The name of the text list and the ranges of values it contains cannot be modified. You can only edit texts assigned to individual value ranges.

| User-defined text lists | System-defined text lists |
| --- | --- |
| You can create new text lists and delete existing text lists. | You cannot create new text lists or delete text lists. |
| You can add and delete value ranges in the text lists. | You cannot add or delete value ranges in the text lists. |
| You can specify both the value ranges as well as the associated texts. | You can only edit the text associated with one value range. |

---

**See also**

[Project text basics](#project-text-basics)
  
[Creating user-defined text lists](#creating-user-defined-text-lists)
  
[Editing user-defined text lists](#editing-user-defined-text-lists)
  
[Editing system-defined text lists](#editing-system-defined-text-lists)
  
[Exporting project texts](#exporting-project-texts)

### Creating user-defined text lists

You can create user-defined text lists for individual devices.

#### Requirement

- You are in the project view.
- A project is open.
- The project includes a least one device.

#### Procedure

To create user-defined text lists, follow these steps:

1. Click on the arrow to the left of a device in the project tree.

   The elements arranged below the device are displayed.
2. Double-click on "PLC message text lists".

   All the text lists assigned to the device are displayed in the work area listed in a table.
3. Double-click on the first free row in the table.

   A new user-defined text list is created.
4. Enter a name for your new text list in the "Name" column.
5. Select if you want to specify the value ranges in decimal, binary or in bits from the drop-down list in the "Selection" column. Depending on the device, there may be further options available at this point.
6. Enter a comment in the "Comment" column.

   A new user-defined text list is created and you can now enter the value ranges and texts.

---

**See also**

[Editing user-defined text lists](#editing-user-defined-text-lists)

### Editing user-defined text lists

You can enter value ranges and the corresponding texts in user-defined text lists. User-defined text lists are always located below a device in the project tree.

#### Requirement

- You are in the project view.
- A project is open.
- The project includes a least one device.

#### Procedure

To add to user-defined text lists with value ranges and texts, follow these steps:

1. Click on the arrow to the left of a device in the project tree.

   The elements arranged below are displayed.
2. Double-click on "PLC message text lists".

   All the text lists assigned to the device are displayed in the work area listed in a table.
3. Select a text list in the table.

   The contents of the selected text list are displayed in the work area. There, you can enter a value range and assign texts to the individual value ranges.
4. Enter the value ranges you require in the "Range from" and " Range to" columns. The entry must be made in the numeric format selected for the text list.
5. Enter a text for each value range in the "Entry" column.

---

**See also**

[Editing system-defined text lists](#editing-system-defined-text-lists)
  
[Translating all project texts in tabular form](#translating-all-project-texts-in-tabular-form)

### Editing system-defined text lists

In system-defined text lists, you can modify the individual texts assigned to a value range.

System-defined text lists are always located below a device in the project tree.

#### Requirement

- You are in the project view.
- A project is open.
- The project includes a least one device.

#### Procedure

To edit texts in system-defined text lists that are assigned to a value range, follow these steps:

1. Click on the arrow to the left of a device in the project tree.

   The elements arranged below are displayed.
2. Double-click on "PLC message text lists".

   All the text lists assigned to the device are displayed in the work area listed in a table.
3. Select a text list in the table.

   The contents of the selected text list are displayed in the work area. Here, you can add to or edit the texts assigned to a value range.
4. Enter a text for each value range in the "Entry" column.

---

**See also**

[Editing user-defined text lists](#editing-user-defined-text-lists)
  
[Translating all project texts in tabular form](#translating-all-project-texts-in-tabular-form)

### Copying or moving text lists

You can copy and move text lists in a CPU or between different CPUs.

#### Copying text lists

To copy text lists, follow these steps:

1. In the project tree, double-click the "PLC alarm text lists" entry for which you want to copy a text list in the CPU.

   All the text lists assigned to the CPU are displayed in the work area listed in a table.
2. Right-click the text list that you want to copy.
3. Select the "Copy" command in the shortcut menu.
4. Position the cursor at the location where you want to insert the text list.
5. Select the "Paste" command in the shortcut menu.

   - If you paste the text list into the same CPU, the copy is pasted with the name extension "_&lt;consecutive number&gt;".
   - If you paste the text list into a different CPU where a text list of the same name already exists, the "Paste" dialog box opens. Select the desired option and confirm your selection with "OK".

Alternatively, you can also copy the text list via drag-and-drop while holding down the &lt;Ctrl&gt; key.

#### Moving text lists

Follow the steps below to move text lists:

1. In the CPU double-click the "PLC alarm text lists" entry in the project tree for which you want to move a text list.

   All the text lists assigned to the CPU are displayed in the work area listed in a table.
2. Drag the text list you want to move to the new position.

### Exporting text lists

You can export user-defined text lists for compilation and then reimport them. The texts are exported to an Office Open XML file with the extension ".xlsx". This can be edited in Microsoft Excel or a number of other spreadsheet programs.

> **Note**
>
> **Restrictions for export**
>
> Note that system-defined text lists cannot be exported.

#### Requirements

- A project is open.
- The project includes a least one device.
- Text lists have been created in the project.
- The text list editor is open.

#### Procedure

To export text lists follow these steps:

1. Click the arrow to the left of a device in the project tree.

   The elements arranged below the device are displayed.
2. Double-click "PLC alarm text lists".

   All the text lists assigned to the device are displayed in the work area listed in a table.
3. Select a text list in the table.

   The entries of the selected text list are displayed in the work area.
4. In the work area, select the text list that you want to export.
5. Click the "Export text lists" icon in the toolbar of the text list editor.

   The "Export text lists" dialog opens.
6. Specify a file path and a file name for the export file in the "Select file for export" input box.
7. Select the project languages that you want to import.
8. Click "Export".

   A message about the status of the export opens.

#### Result

The texts lists are exported to an Office Open XML file with the extension ".xlsx". The file is stored in the specified folder.

### Importing text lists

After external compilation in a spreadsheet program, you import the user-defined text lists into TIA Portal

> **Note**
>
> **Restrictions for import**
>
> Text lists which were exported to other editors cannot be imported in the text list editor.

#### Requirements

- A project is open.
- The project includes a least one device.
- Text lists have been created in the project.
- The text list editor is open.

#### Procedure

To import text lists, follow these steps:

1. Click the arrow to the left of a device in the project tree.

   The elements arranged below the device are displayed.
2. Double-click "PLC alarm text lists".

   All the text lists assigned to the device are displayed in the work area listed in a table.
3. Click the "Import text lists" icon in the toolbar of the text list editor.

   The "Import text lists" dialog opens.
4. Select the path and file name of the import file from the "Import file" field.
5. Click "Import".

   A message on the status of the import opens.

#### Result

The text lists are imported. The existing data in the text lists in the project is overwritten in the process and new data is added. Text lists are only imported in the languages that have been activated in the project.

## Using memory cards

This section contains information on the following topics:

- [Basics about memory cards](#basics-about-memory-cards)
- [Adding a user-defined card reader](#adding-a-user-defined-card-reader)
- [Accessing memory cards](#accessing-memory-cards)
- [Displaying properties of memory cards](#displaying-properties-of-memory-cards)
- [Show data on the memory card of a controller](#show-data-on-the-memory-card-of-a-controller)

### Basics about memory cards

#### Introduction

Memory cards are plug-in cards that come in a variety of types and can be used for a variety of purposes. Depending on the device type or device family, memory cards can be used for purposes, such as:

- Load memory of a CPU
- Storage medium for projects, firmware backups, or any other files
- Storage medium for performing a firmware update
- Storage medium for the PROFINET device name

For information regarding the technical variants of the respective memory cards and general information on their handling, refer to the respective documentation for the device. For information on handling memory cards in the TIA Portal, refer to the online help under the keyword "Memory Card".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| ****Memory card is unusable for SIMATIC devices****  If you use a SIMATIC memory card for non-SIMATIC purposes or you format it incorrectly, you will overwrite the internal structure of the SIMATIC memory card. The structure is not recoverable and the SIMATIC memory card becomes unusable for SIMATIC devices.  Do not use memory cards for non-SIMATIC-related purposes, and do not format SIMATIC memory cards with third-party devices or Windows tools. |  |

---

**See also**

[Adding a user-defined card reader](#adding-a-user-defined-card-reader)
  
[Accessing memory cards](#accessing-memory-cards)
  
[Displaying properties of memory cards](#displaying-properties-of-memory-cards)

### Adding a user-defined card reader

#### Introduction

If your card reader is not detected automatically, you can add it manually.

#### Requirement

The project view is open.

#### Procedure

To add a card reader, follow these steps:

1. Open the project tree.
2. Select the "Card Reader / USB memory &gt; Add user-defined Card Reader" command in the "Project" menu.

   The "Add user-defined Card Reader" dialog opens.
3. In the drop-down list box, select the path for the card reader.
4. Confirm your entries with "OK".

---

**See also**

[Basics about memory cards](#basics-about-memory-cards)
  
[Accessing memory cards](#accessing-memory-cards)
  
[Displaying properties of memory cards](#displaying-properties-of-memory-cards)

### Accessing memory cards

#### Requirement

- A memory card is inserted in the card reader.
- The project view is open.

> **Note**
>
> You cannot work with multiple memory cards at one time. Only insert one memory card into the card reader.

#### Procedure

To access memory cards, follow these steps:

1. Open the project tree.
2. Select the "Card Reader / USB memory &gt; Card Reader / Show USB memory" command in the "Project" menu.

   The "Card reader / USB memory" folder is displayed in the project tree.
3. Open the "Card Reader / USB memory" folder.

   You can now access the memory card.

**Note**

If data from a non-installed product is stored on the memory card, the folders that contain these data are shown in gray. You receive an error message when you attempt to access such a folder. Install the corresponding product if needed.

---

**See also**

[Basics about memory cards](#basics-about-memory-cards)
  
[Adding a user-defined card reader](#adding-a-user-defined-card-reader)
  
[Displaying properties of memory cards](#displaying-properties-of-memory-cards)

### Displaying properties of memory cards

You can display the properties for the utilized memory cards. Note that different memory cards with different properties must be used, depending on the device.

#### Requirement

- A memory card is inserted in the card reader.
- The project view is open.

#### Procedure

To display the properties of a memory card, follow these steps:

1. Right-click on the memory card for which you want to display the properties.
2. Select the "Properties" command in the shortcut menu.

   The "Memory Card &lt;name of the memory card&gt;" dialog opens. The properties are displayed in this dialog.

---

**See also**

[Basics about memory cards](#basics-about-memory-cards)
  
[Adding a user-defined card reader](#adding-a-user-defined-card-reader)
  
[Accessing memory cards](#accessing-memory-cards)

### Show data on the memory card of a controller

In addition to the configuration, data such as firmware updates of the controller, HMI images or HMI backups can be stored in the memory card in a controller. With an online connection to the controller, this data is displayed in the project tree in the "Online card data" folder under the controller.

#### Requirements

- A memory card is inserted in the card reader of the controller.
- The memory card contains data that can be displayed.
- The project view is open.
- There is an online connection to the controller.

#### Procedure

To show data on the memory card of a controller, follow these steps:

1. Open the device folder in the project tree.
2. Open the "Online card data" folder.

   The data is shown in subfolders.

## Using cross-references

This section contains information on the following topics:

- [Using cross-references](#using-cross-references-1)

### Using cross-references

#### Introduction to cross-references

The cross-reference list provides an overview of the use of objects within the project. You can see which objects are interdependent and where the individual objects are located. Cross-references are therefore part of the project documentation.

You can also jump directly to the point of use of an object.

Which objects you can display and localize in the cross-reference list depends on the installed products.

---

**See also**

[Displaying cross references of an instance](Using%20libraries.md#displaying-cross-references-of-an-instance)

## Providing user-defined documentation

This section contains information on the following topics:

- [Using user-defined documentation](#using-user-defined-documentation)
- [Specifying settings in the TIA Portal](#specifying-settings-in-the-tia-portal)
- [Specifying settings with an XML file](#specifying-settings-with-an-xml-file)
- [Creating a homepage](#creating-a-homepage)
- [Conventions for the creation](#conventions-for-the-creation)
- [Calling user-defined documentation](#calling-user-defined-documentation)
- [Displaying the call log](#displaying-the-call-log)
- [Creating user-defined documentation](#creating-user-defined-documentation)

### Using user-defined documentation

#### User-defined documentation for project or library contents

Over time, you create your own contents in a project or a library. Your own contents include, for example, blocks, tags or library types. While the functionality of the TIA Portal is described in the supplied help system, there is no help for the contents you have created yourself. You can create your own user-defined documentation to explain to other employees how your project works or how to use individual library types.

You can provide user-defined documentation in the available user interface languages. The default user interface languages in the TIA Portal are English, German, French, Spanish, Italian, and Chinese. You need to observe a few conventions when you create user-defined documentation so that the help matching an object can be opened.

You create the user-defined documentation either in one of the supported Office formats or as compiled HTML help in CHM format.

#### Possible areas for user-defined documentation

You can offer user-defined documentation in the following areas of the TIA Portal, for example:

- Project tree
- "Libraries" task card
- Some editors, depending on the products installed, for example:

  - Program editor

    The programming languages LAD, FBD, STL, SCL, GRAPH and CEM are supported. Block calls also support the connection of user-defined documentation.
  - "Screens" editor

    Uses of screens and instances of HMI faceplates are supported in the "Screens" editor.

#### Directories for user-defined documentation

Save the user-defined documentation in one of the following directories:

- Project folder

  If you create user-defined documentation for objects within a project, save this help in the project folder. The user-defined documentation is also included when you pass on the project.
- Directory of a global library

  If you create user-defined documentation for objects within a global library, save the user-defined documentation in the directory of the global library. The user-defined documentation is also included when you pass on the global library.
- Central directory on the hard drive or a network drive

  You can store the user-defined documentation in a central directory on the hard disk or on a network drive. In this way, you have access to the user-defined documentation in each project or you use the documentation on a network drive together in the team. You specify the central file directory for the user-defined documentation using an XML file or in the settings of the TIA Portal.

#### Homepage for the user-defined documentation

You can create a separate homepage for each language version of the user-defined documentation. The homepage for the user-defined documentation can contain general help for a project or for a library. The homepage must be saved in the central storage directory for user-defined documentation.

#### Calling the user-defined documentation

If user-defined documentation is available for an object, you call it with the keyboard shortcut &lt;Shift+F1&gt;. The user-defined documentation is always opened with the standard program specified for the respective file format in Microsoft Windows.

Once you have pressed &lt;Shift+F1&gt;, certain directories are searched in a fixed order for user-defined documentation. The search order is given below:

|  |  |  |
| --- | --- | --- |
| 1. | Search in the central directory for user-defined documentation |  |
|  | 1.1 | Search for a CHM file |
|  | 1.2 | Search for documentation in other file formats |
| 2. | Search in the project or library directory |  |
|  | 2.1 | Search for a CHM file |
|  | 2.2 | Search for documentation in other file formats |

The search is initially performed in the language directory for the currently set user interface language of the TIA Portal. If no help is contained in this language directory, the search for user-defined documentation is performed in the same order in the English language directory.

As soon as user-defined documentation is found in one location, the user-defined documentation is opened and the search is canceled. If no user-defined documentation is found in any of the directories, a search for a homepage for user-defined documentation is performed in the order presented above. The search for a homepage is again initially performed in the language directory for the currently set user interface language. If no homepage is found there, the English language directory is searched.

#### Call log

You can display a call log for the user-defined documentation for easier connection of the user-defined documentation. The alarms within the log indicate the directories in which documentation is searched for and whether the call of the user-defined documentation is successful. In addition, the file name that is expected for the file is indicated. This allows you to identify how you must name your documentation and the directories in which you must save the user-defined documentation. The call log has the same sequence as the one used to search for user-defined documentation or a homepage.

The log is displayed in the Inspector window in the "Info" tab. Before you can display the call log, you must first enable the call log in the settings of the TIA Portal. To do this, select the "Display call log for user-defined documentation" check box under "Settings &gt; General &gt; User documentation". Alternatively, activate the display of the call log using an XML file.

---

**See also**

[Conventions for the creation](#conventions-for-the-creation)
  
[Specifying settings with an XML file](#specifying-settings-with-an-xml-file)
  
[Creating a homepage](#creating-a-homepage)
  
[Creating user-defined documentation](#creating-user-defined-documentation)
  
[Calling user-defined documentation](#calling-user-defined-documentation)
  
[General remarks on the information system](Introduction%20to%20the%20TIA%20Portal.md#general-remarks-on-the-information-system)

### Specifying settings in the TIA Portal

You specify the following settings for user-defined documentation in the settings of the TIA Portal:

- Displaying the call log in the Inspector window

  A log of the call of user-defined documentation is displayed on the 'Info &gt; General' tab of the Inspector window. The log helps you to adhere to the conventions for calling user-defined documentation.
- Search for user-defined documentation in a central file directory

  You can save user-defined documentation in a directory outside the current project directory in order, for example, to make documentation available across projects.
- Central directory for user-defined documentation

  You store cross-project documentation in the central file directory for user-defined documentation.

> **Note**
>
> **XML configuration file takes precedence over the settings of the TIA Portal**
>
> If you use an XML configuration file and have specified settings for user-defined documentation there, the settings in the XML file take precedence. As soon as you refresh the XML configuration file or restart the TIA Portal, the settings from the XML file are applied. The settings that you have made in the TIA Portal lose their validity.

#### Procedure

To specify a central storage location for user help, follow these steps:

1. Select the "Settings" command in the "Options" menu.
2. Open the "General &gt; General" area.
3. Navigate to the "User documentation" section.
4. Select the "Display call log for user-defined documentation" check box in order to display a log of the call of the user-defined documentation in the Inspector window.
5. Select the "Search for user-defined documentation in a central directory" check box in order to store user-defined documentation in a cross-project directory.
6. Specify the path to where you save the cross-project documentation in the "Central directory for user-defined documentation" field.

---

**See also**

[Specifying settings with an XML file](#specifying-settings-with-an-xml-file)

### Specifying settings with an XML file

As an alternative to settings in the TIA Portal, you can make settings for the user-defined documentation in an XML file. The XML file is the same file you use for integrating corporate libraries.

If you use an XML configuration file and have specified settings for user-defined documentation there, the settings in the XML file take precedence. As soon as you refresh the XML configuration file or restart the TIA Portal, the settings from the XML file are applied. The settings that you have made in the TIA Portal lose their validity.

You can set the following options in the XML configuration file:

- Displaying the call log in the Inspector window

  A log of the call of user-defined documentation is displayed on the 'Info &gt; General' tab of the Inspector window. The log helps you to adhere to the conventions for calling user-defined documentation.
- Search for user-defined documentation in a central file directory

  You can save user-defined documentation in a directory outside the current project directory in order, for example, to make documentation available across projects.
- Central directory for user-defined documentation

  You store cross-project documentation in the central file directory for user-defined documentation.

#### Procedure

To specify settings for the user-defined documentation, follow these steps:

1. Create an XML file named "CorporateSettings.xml", if you are not yet using an XML configuration file for the integration of company libraries. If you are already using a configuration file, proceed with step 3.

   The configuration file must be saved with "UTF-8" coding.
2. Save the file in the following directory on your computer:

   C:\ProgramData\Siemens\Automation\Portal V19\CorporateSettings\
3. Enter the content listed below into the XML configuration file.
4. Adapt the attributes for display of the user-defined documentation. The meaning of the individual elements is available in the comments in the XML configuration file. Use the value "true" to activate a function. Use the value "false" to deactivate a function.

#### Content of the XML configuration file

The XML configuration file must have the following content:

XML

&lt;?xml version="1.0" encoding="utf-8"?&gt;

&lt;Document&gt;

&lt;Settings.Settings ID="0"&gt;

&lt;ObjectList&gt;

&lt;Settings.General ID="1" AggregationName="General"&gt;

&lt;!-- Here you find the settings for global company libraries, if available. --&gt;

&lt;ObjectList&gt;

&lt;!-- Section Corporate libraries --&gt;

&lt;Settings.General ID="1" AggregationName="General"&gt;

    &lt;AttributeList&gt;

     &lt;CorporateLibraryPaths&gt;

     &lt;!-- Example for two entries --&gt;

     &lt;Item&gt;F:\CorporateLibraries\Corporate_Library_1\Corporate_Library_1.al19&lt;/Item&gt;     &lt;Item&gt;F:\CorporateLibraries\Corporate_Library_2\CorporateLibraries.al19&lt;/Item&gt;

     &lt;!-- Here you enter additional global libraries, if any. --&gt;     &lt;/CorporateLibraryPaths&gt;

    &lt;/AttributeList&gt;

   &lt;/Settings.General&gt;

&lt;!-- Section Corporate libraries end --&gt;

&lt;!-- Section User-defined documentation --&gt;

     &lt;Settings.UserDocumentation ID="2" AggregationeName="UserDocumentation"&gt;

      &lt;!-- In the following section, you specify the values for display of the user-defined documentation. --&gt;

      &lt;AttributeList&gt;

       &lt;!-- Activates or deactivates the display of the access log. --&gt;

       &lt;DisplayLogInformation&gt;

        &lt;Value&gt;true&lt;/Value&gt;

       &lt;/DisplayLogInformation&gt;

       &lt;!-- Activates or deactivates the search for user-defined documentation in a central directory. --&gt;

       &lt;EnableLookupFromCentralStorageLocation&gt;

        &lt;Value&gt;true&lt;/Value&gt;

       &lt;/EnableLookupFromCentralStorageLocation&gt;

       &lt;!-- Specifies the central directory for user-defined documentation. --&gt;

       &lt;CentralStorageLocation&gt;

        &lt;Value&gt;D:\CorporateDocumentation\UserDocumentation\&lt;/Value&gt;

       &lt;/CentralStorageLocation&gt;

      &lt;/AttributeList&gt;

     &lt;/Settings.UserDocumentation&gt;

&lt;!-- Section User-defined documentation end --&gt;

    &lt;/ObjectList&gt;

&lt;/Settings.General&gt;

&lt;/ObjectList&gt;

&lt;/Settings.Settings&gt;

&lt;/Document&gt;

---

**See also**

[Using user-defined documentation](#using-user-defined-documentation)
  
[Specifying settings in the TIA Portal](#specifying-settings-in-the-tia-portal)
  
[Calling user-defined documentation](#calling-user-defined-documentation)
  
[Creating a homepage](#creating-a-homepage)
  
[Creating a configuration file for corporate libraries](Using%20libraries.md#creating-a-configuration-file-for-corporate-libraries)

### Creating a homepage

You can design a homepage for user-defined documentation. The homepage can be an HTML page that you save either within a CHM file or in the directory of the relevant language. You can also use other file formats approved for user-defined documentation. You design the homepage of the user-defined documentation outside the TIA Portal.

#### Procedure

To create a homepage, follow these steps:

1. Design a file in HTML format or in any other file format approved for user-defined help.
2. Name the file "Home".
3. Copy the file to the central directory for user-defined documentation on the hard disk or on a network drive:

   &lt;Central directory for user-defined documentation&gt;\&lt;Folder for the respective language&gt;
4. If the respective language folder does not exist yet, create the folder now.

   Alternative: If you are creating the homepage for a CHM file, place the homepage in the main directory of the CHM file.

#### Sample configuration for the homepage

Below you see the correct path for the following conditions:

- The user-defined documentation is in Spanish.
- The homepage is an HTML file.

The path for these conditions is as follows:

&lt;Central directory for user-defined documentation&gt;\es-ES\Home.html

---

**See also**

[Specifying settings with an XML file](#specifying-settings-with-an-xml-file)
  
[Using user-defined documentation](#using-user-defined-documentation)
  
[Conventions for the creation](#conventions-for-the-creation)
  
[Calling user-defined documentation](#calling-user-defined-documentation)
  
[Displaying the call log](#displaying-the-call-log)
  
[Creating user-defined documentation](#creating-user-defined-documentation)

### Conventions for the creation

You must observe some conventions to ensure that user-defined documentation is called at the correct location:

- the user-defined documentation must be saved in the correct directory.
- The file name must be exactly the same as the object name in the TIA Portal.

To prevent malicious code from being executed on your computer, only file formats that are considered as relatively safe are permitted.

#### Supported file formats

Create the user-defined documentation in one of the following file formats:

- Microsoft Word (.docx)
- Microsoft Excel (.xlsx)
- Microsoft PowerPoint (.pptx and .ppsx)
- HTML pages (.htm or .html)
- Microsoft XPS (.xps)
- Rich Text Format (.rtf)
- Text documents (.txt)
- Compiled HTML help (.chm)
- PDF documents (.pdf)

You save the homepage of the user-defined documentation in HTML format or save the homepage within a CHM file.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Infection of the computer with malicious code**  If the user-defined documentation contains malicious code, it can infect your computer. Especially HTML pages and CHM files can contain malicious code.  Make sure that the user-defined documentation comes from a trustworthy source. You should also use the standard security measures, such as the use of a firewall and an up-to-date virus scanner. |  |

#### Directories for user-defined documentation

Save the user-defined documentation in one of the following directories:

- Project folder:

  UserFiles\UserDocumentation\&lt;Folder for the respective language&gt;\&lt;Object category&gt;
- Directory of a global library:

  UserFiles\UserDocumentation\&lt;Folder for the respective language&gt;\&lt;Object category&gt;
- Central directory on the hard drive or a network drive:

  &lt;Central directory for user-defined documentation&gt;\&lt;Folder for the respective language&gt;\&lt;Object category&gt;\

The user-defined documentation must be located in the suitable subfolder for the respective language. The table below shows the respective language folders for the user languages installed as default:

| Language | Subfolder |
| --- | --- |
| German | \de-DE |
| English | \en-US |
| Spanish | \es-ES |
| French | \fr-FR |
| Italian | \it-IT |
| Chinese | \zh-CN |

The language folder must contain a separate subfolder for each object category. Create the corresponding subfolders for objects for which you are providing user-defined documentation. Always use the English designation of the object category. The table below shows the English designations of the most important object categories in the TIA Portal:

| Object category | English designation |
| --- | --- |
| HMI screens | Screens |
| Organization blocks (OB) | Organization Blocks |
| Function blocks (FBs) | Function Blocks |
| Functions (FCs) | Functions |
| Data blocks | Data Blocks |
| Types in the library | Library Types |
| Master copies in the library | Master Copies |
| The project node in the project tree | Projects |
| All types of folders in the project tree, in the project library or in global libraries | Folders |
| All types of links in the project tree, for example, "Add new block", "Add new device", etc. | ShortCut |
| Libraries in the "Libraries" task card | Libraries |

If you are not sure of the English designation for an object category, change the user interface language of the TIA Portal to English. Alternatively, open the user-defined documentation for an object with &lt;Shift+F1&gt; and check in the call log which designation is expected for the object category.

#### Permitted file names

The file name must be exactly the same as the object name in the TIA Portal.

There are, however, restrictions for file names under Microsoft Windows. The same restrictions apply to the file system used to format the hard drive. The file name may only include certain characters and must not exceed a specific length. The restrictions for file names differ depending on the Windows version and the file system used for the hard drive.

To ensure that the help call works, read up on possible restrictions in the Microsoft Windows documentation.

#### Special features of CHM files

You store CHM files directly in the respective language folder. The folder for the respective object category must be included in the actual CHM file. Within the compiled CHM file, the names of the individual HTML files must also be exactly the same as the object names in the TIA Portal.

> **Note**
>
> **Opening CHM files on network drives**
>
> If CHM files are saved on a network drive, the CHM files are not displayed correctly in more recent versions of Microsoft Windows. This behavior is determined by the security guidelines of the operating system. All versions of Microsoft Windows as of Windows Server 2003 SP1 are affected.
>
> You can bypass the security guidelines by changing the registry database in Microsoft Windows.
>
> To not compromise the security of your computer, save the CHM files only locally on your computer and do not change the registry database.

---

**See also**

[Using user-defined documentation](#using-user-defined-documentation)
  
[Creating a homepage](#creating-a-homepage)

### Calling user-defined documentation

The user-defined documentation is opened in the language that is currently set as the user interface language. If there is no user-defined documentation available in the currently set user interface language, the English version of the user-defined documentation opens. If no user-defined documentation exists, a homepage is searched for.

#### Requirement

You have already saved user-defined documentation or a homepage according to the conventions.

#### Procedure

To open the user-defined documentation, follow these steps:

1. Select the object for which you want to display the user-defined documentation.
2. Press &lt;Shift+F1&gt;.

   The suitable user-defined documentation or the homepage opens.

---

**See also**

[Using user-defined documentation](#using-user-defined-documentation)
  
[Opening the information system](Introduction%20to%20the%20TIA%20Portal.md#opening-the-information-system)
  
[Creating a homepage](#creating-a-homepage)
  
[Specifying settings with an XML file](#specifying-settings-with-an-xml-file)
  
[Displaying the call log](#displaying-the-call-log)

### Displaying the call log

Use the call log to check whether the user-defined documentation is connected correctly. The call log shows the directories in which the search is performed for user-defined documentation or a homepage. The call log also displays the names that the individual files must have in order to call the user-defined documentation.

#### Requirement

The call log is enabled in the settings of the TIA Portal or using an XML configuration file.

#### Procedure

To display the call log, follow these steps:

1. Open the "Info" tab in the Inspector window.
2. Open the "General" tab.
3. Select the object for which you want to call the help.
4. Press &lt;Shift+F1&gt;.

   If possible, the matching user-defined documentation or the homepage of the user-defined documentation is opened. In any case, you will be informed in the Inspector window about which user-defined documentation is opened. You may be shown the directories in which no user-defined documentation was found.

---

**See also**

[Calling user-defined documentation](#calling-user-defined-documentation)
  
[Creating a homepage](#creating-a-homepage)

### Creating user-defined documentation

You create user-defined documentation for individual elements within a project or global library outside the TIA Portal. You can create the user-defined documentation in all available user interface languages.

If you create the user-defined documentation as CHM file, the procedure for creating the help is somewhat different to the creation process for other file formats.

Note the information provided in chapter "[Conventions for the creation](#conventions-for-the-creation)".

#### Creating user-defined documentation as single file

To create user-defined documentation as a single file, follow these steps:

1. Create a file in a valid file format.
2. Name the file identically to the object for which you want to call the user-defined documentation.

   If you are offering help for a library type, for example, name the help file identical to the type.
3. Depending on whether you are creating the user-defined documentation for project contents or for contents of a global library, copy the file to one of the following storage locations:

   - project folder under "UserFiles\UserDocumentation\&lt;Folder for the respective language&gt;\&lt;Object category&gt;"
   - Directory of a global library under "UserFiles\UserDocumentation\&lt;Folder for the respective language&gt;\&lt;Object category&gt;"
   - Central directory on the hard drive or a network drive:

     &lt;Central directory for user-defined documentation&gt;\&lt;Folder for the respective language&gt;\&lt;Object category&gt;\

   If the respective language folder or the folder for the object category does not exist yet, create the required folders before copying the file.

#### Sample configuration for user-defined documentation

Below you see the correct path for the following conditions:

- The user-defined documentation is intended for a type in a global library.
- The user-defined documentation is in French.
- The type is called "commande de moteur".
- The user-defined documentation is supplied with the global library.
- The user-defined documentation is created in Microsoft PowerPoint format.

The path for these conditions is as follows:

&lt;Folder of the global library&gt;\UserFiles\UserDocumentation\fr-FR\Library Types\commande de moteur.pptx

#### Creating user-defined documentation as CHM file

To provide user-defined documentation in CHM format, follow these steps:

1. Create a folder in Windows Explorer for each object category for which you want to create user-defined documentation. Use the English designation for the object category.
2. Create an HTML file for each object for which you want to provide user-defined documentation. Name the HTML file identically to the object for which you want to call the user-defined documentation. If you want to provide user-defined documentation for a library type, for example, name the HTML file identically to the type.
3. Store the HTML files in the corresponding folders of the respective object category.
4. Use the Microsoft HTML Help Workshop to create the CHM file. Use the prepared folder structure with the HTML files.
5. Copy the CHM file to one of the following storage locations:

   - Project folder under "UserFiles\UserDocumentation\&lt;Folder for the respective language&gt;"
   - Directory of a global library under "UserFiles\UserDocumentation\&lt;Folder for the respective language&gt;"
   - Central directory on the hard drive or a network drive:

     &lt;Central directory for user-defined documentation&gt;\&lt;Folder for the respective language&gt;

   If the respective language folder does not exist yet, create the language folder before you copy the CHM file.

---

**See also**

[Creating a homepage](#creating-a-homepage)
  
[Conventions for the creation](#conventions-for-the-creation)
