---
title: "Migrating projects and programs"
package: PEMigrationenUS
topics: 19
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Migrating projects and programs

This section contains information on the following topics:

- [Overview of Migration Options](#overview-of-migration-options)
- [Migrating projects to a TIA Portal project](#migrating-projects-to-a-tia-portal-project)
- [Migrating PLC programs to a S7-1500 CPU / ET 200SP](Migrating%20PLC%20programs%20to%20a%20S7-1500%20CPU%20-%20ET%20200SP.md#migrating-plc-programs-to-a-s7-1500-cpu-et-200sp)
- [Migrating S7-1200 to firmware as of V4 (S7-1200)](Migrating%20S7-1200%20to%20firmware%20as%20of%20V4%20%28S7-1200%29.md#migrating-s7-1200-to-firmware-as-of-v4-s7-1200)

## Overview of Migration Options

### Migration paths

If you want to continue to use existing projects or programs with the latest version of the TIA Portal and the S7-1500, you have several options for migrating projects.

The following graphic provides an overview of the migration options:

![Migration paths](images/65310036619_DV_resource.Stream@PNG-en-US.png)

### Migrating projects to the TIA Portal

You use the "Migrate project" function to migrate projects that were created outside of the TIA Portal, for example, with STEP 7, WinCC, WinCC flexible, or SINUMERIK.

The result of the project migration is a TIA Portal project that you can use with your existing S7-300/400 series hardware and existing HMI devices.

### Migrating PLC programs from S7-300/400 to S7-1500

To migrate a PLC program within the TIA Portal from an S7-300/400 series device to an S7-1500, you use the PLC migration.

The result of the PLC migration is an executable PLC program that is automatically adapted to the new system architecture of the S7-1500 as far as possible.

### Optimizing PLC program for S7-1500

You also have the option to optimize your program for the S7-1500 by employing newly introduced programming methods. The optimization enables you to effectively use the higher performance, innovated memory technology and new features of the S7-1500 system.

### Upgrading projects

You can also continue to use projects from previous versions of the TIA Portal. However, these projects do not need to be migrated. You can upgrade projects from previous versions to the current version of the product. You can find additional information on compatibility and upgrading projects in the section "[Upgrading projects](Editing%20projects.md#upgrading-projects-1)".

> **Note**
>
> **Additional support for migration**
>
> You can find the latest information about PLC migration in the Siemens Industry online support:
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
> If you need further support, please contact SIMATIC Customer Support.

---

**See also**

[Using projects created with optional software](Editing%20projects.md#using-projects-created-with-optional-software)

## Migrating projects to a TIA Portal project

This section contains information on the following topics:

- [Migration of projects with the TIA Portal](#migration-of-projects-with-the-tia-portal)
- [Check migration readiness of hardware components](#check-migration-readiness-of-hardware-components)
- [Preparing projects with the migration tool](#preparing-projects-with-the-migration-tool)
- [Migrating projects](#migrating-projects)
- [Displaying the history of the migration](#displaying-the-history-of-the-migration)
- [Display migration log](#display-migration-log)
- [Migrating STEP 7 projects (S7-300, S7-400)](Migrating%20STEP%207%20projects%20%28S7-300%2C%20S7-400%29.md#migrating-step-7-projects-s7-300-s7-400)
- [Migrating WinCC flexible projects (Professional)](Migrating%20WinCC%20projects.md#migrating-wincc-projects)
- Migrating WinCC flexible projects (Advanced)
- Migrating WinCC flexible projects (Basic)
- Migrating SINUMERIK projects
- [Migrating integrated projects](#migrating-integrated-projects)

### Migration of projects with the TIA Portal

#### Migration of existing projects

You can migrate projects from earlier automation solutions to the TIA Portal. Each time you migrate, a new project is created for the migrated data with which you can then work. Any TIA Portal projects already open are closed first.

The migration is then displayed in the table of the project history. From there, you have access to the migration log that is created automatically for the migration.

After the migration of hardware configurations and program blocks from earlier automation solutions, first check the functionality of the migrated project before you use it in productive operation.

#### Supported products for migration

Refer to the chapter "System overview STEP 7 and WinCC" to find out which products are available for the TIA Portal. All products listed there are generally supported by the TIA Portal during migration.

Any additional requirements that must be met depend on the initial products that were used and the currently installed products. For more information on the migration options for your products, you can, for example, refer to the Siemens Industry Online Support and the documentation of your software products.

See also: [Scaling of products in TIA Portal](System%20overview%20TIA%20Portal.md#scaling-of-products-in-tia-portal)

#### Procedure during migration

The migration process is divided into the following basic steps:

1. Preparing the initial project

   If the software for editing the initial project is not installed or not fully installed on the programming device/PC with the TIA Portal, or if the initial project is an integrated project, you must first convert the initial project to a migration file. To do this, install the migration tool on a programming device/PC on which the required software for editing the initial project is installed. Then, use the migration tool to convert the initial project, and copy the file to the programming device/PC on which the TIA Portal is installed. You can omit this step if the initial project and its associated software are on the same programming device/PC as the TIA Portal, and if the initial project is not an integrated project.
2. Performing migration

   Perform the migration within the TIA Portal. For the migration, specify as source either the migration file which you created with the migration tool or the initial project when all required software has been installed.
3. Checking the migration log

   A migration log is created for each migration. It contains information about modified project parts. You can call the log under "Common data > Logs" in the project tree or in the project history. After completion of the migration, the migration log will be displayed in the TIA Portal. Check the log following completion of the migration.

   If the migration failed, an XML file is created as a log under "\Logs" in the project directory. You can use any XML editor to open this log and view the reasons why the migration failed.
4. Correcting the migrated project

   Because the configurations of the initial project may not always be completely compatible with the TIA Portal, all configurations may not be reproduced identically in the migrated project. You should therefore work through the points in the migration log systematically. If you have not included the hardware configuration in the migration, you also have to convert the unspecified devices to the appropriate hardware.

#### Including the hardware configuration in the migration

By default, only the software parts of the project are included in the migration. An unspecified device is generated in the migrated project for the devices contained in the initial project. The hardware and network configurations and the connection are not migrated. You therefore convert the unspecified devices into suitable devices after the migration and recreate any network configurations and connections manually.

If you are certain that the hardware used in the initial project has a corresponding equivalent in the TIA Portal, you can include the hardware configuration in the migration. In this case, both the hardware configuration and the software are migrated. You can check with a [tool](#check-migration-readiness-of-hardware-components) to see which hardware components are supported.

---

**See also**

[Display migration log](#display-migration-log)
  
[Scaling of products in TIA Portal](System%20overview%20TIA%20Portal.md#scaling-of-products-in-tia-portal)

### Check migration readiness of hardware components

#### Introduction

Siemens offers a tool that can be used to check whether the hardware configuration used in an initial project is ready for migration to the TIA Portal.

Components integrated via GSD or GSDML files cannot be checked. For such modules, check manually in the TIA Portal whether the modules are available in the hardware catalog. If the modules are not available there, install the required GSD or GSDML files in the TIA Portal. You can obtain the required files from the manufacturer of the components.

In the result you can also see which software products and licenses have to be available on the programming device/PC with the installation of the TIA Portal to perform a migration. You can also see as of which firmware version the individual modules of the initial project are supported in TIA Portal. The result of the check can be output in a Microsoft Excel file or in PDF format.

#### Download

The tool for checking the migration readiness is available for download in the [FAQs of the Siemens Industry Online Support under entry number 60162195](http://support.automation.siemens.com/WW/view/en/60162195).

#### Source files for the check

To check readiness, you require one of the following source files which contains the article number of the hardware used in the initial project:

- .cfg file

  You can export the .cfg file from HW Config (STEP 7) with the menu command "Export as .cfg file" in the "Station" menu. The .cfg file contains all MLFBs of the devices used in the currently open station.
- Microsoft Excel file (in .xls file format)

  Regardless of the initial project used, you can create a Microsoft Excel list containing all MLFBs of the devices you want to migrate.
- File in .csv format

  The article numbers that are to be checked can also be saved to a .csv file instead of a Microsoft Excel list. To do this, use a standard text editor and enter the MLFBs separated by comma and without space after the comma. Save the text file with the extension ".csv".

---

**See also**

[Tool for checking migration readiness](http://support.automation.siemens.com/WW/view/en/60162195)

### Preparing projects with the migration tool

This section contains information on the following topics:

- [Migrating projects with the migration tool](#migrating-projects-with-the-migration-tool)
- [Calling the migration tool](#calling-the-migration-tool)
- [Creating a migration file](#creating-a-migration-file)

#### Migrating projects with the migration tool

##### Preparation for migration

In many cases, a project that you wish to migrate will not be located on the same programming device/PC on which the latest version of TIA Portal is installed. Therefore, the initial project must first be converted to a compatible format for the migration. The same applies to integrated projects.

After creation of the migration file, you copy the migration file to the programming device/PC on which the current version of TIA Portal is installed. In TIA Portal, you enter the migration file as the source for the migration and can create a project in the current file format of TIA Portal.

##### Procedure for migration with the migration tool

The following steps are necessary to prepare a migration with the migration tool:

1. Install the migration tool on the programming device/PC where the source project is located. To do this, download the installation file from the Siemens Industry Online Support or install the migration tool from the setup DVD of TIA Portal.
2. Start the migration tool, and use it to convert the source project to the migration file format with the file extension ".am19".

   For this step, make sure that all software needed to process the source project is installed on the programming device/PC. This also includes all necessary service packs, hardware support packages and all expansion software that is needed to process the initial project. If individual products are not installed it might not be possible to perform the migration or the migration might be incomplete.
3. Copy the migration file to the target system on which a current version of TIA Portal is installed.

   Note that the target system must have been installed with all software needed to configure the complete set of devices contained in the migration.
4. Perform the migration within TIA Portal and specify the migration file with the extension ".am19" as the source.
5. Once migration is complete, check the migration log and systematically work through the information provided there for the newly created project. Read the information in the Inspector window with special care after the first compilation of the configuration.

##### Including the hardware configuration in the migration

By default, only the software parts of the project are included in the migration. An unspecified device is generated in the migrated project for the devices contained in the initial project. The hardware and network configurations and the connection are not migrated. You therefore convert the unspecified devices into suitable devices after the migration and recreate any network configurations and connections manually.

If you are certain that the hardware used in the initial project has a corresponding equivalent in TIA Portal, you can include the hardware configuration in the migration. In this case, both the hardware configuration and the software are migrated. You can check with a tool to see which modules are supported.

---

**See also**

[Migration of projects with the TIA Portal](#migration-of-projects-with-the-tia-portal)
  
[Migrating projects](#migrating-projects)
  
[Installing and uninstalling the migration tool](Installation.md#installing-and-uninstalling-the-migration-tool)
  
[Calling the migration tool](#calling-the-migration-tool)
  
[Creating a migration file](#creating-a-migration-file)

#### Calling the migration tool

##### Starting the migration tool

During the installation, a "Migration to TIA Portal V19" shortcut is created by default in the Start menu under "Siemens Automation > Migration Tool". Click this shortcut.

Alternatively, you can call the migration tool directly in Windows Explorer. During the installation, the migration tool is saved by default in one of the following folders:

- On a 64-bit operating system:

  C:\Program Files (x86)\Siemens\Automation\MIGTOOL_V19\Bin
- On a 32-bit operating system:

  C:\Program Files\Siemens\Automation\MIGTOOL_V19\Bin

To start the migration tool, click the "Siemens.Automation.MigrationApplication.exe" file in one of the directories.

---

**See also**

[Creating a migration file](#creating-a-migration-file)

#### Creating a migration file

The section below describes how you can use the migration tool to convert the initial project to a migration file that can be read by the TIA Portal. Following conversion, this file is transferred to the target system and migrated there.

You can specify whether the migration file should contain the entire project, including the complete hardware configuration and the associated software, or whether you want to migrate the software only.

##### Requirement

- The suitable, original software with a valid license is installed for all configurations used in the initial project.
- The initial project is not provided with access protection.
- The initial project must be consistent, otherwise problem-free migration cannot be assured.

##### Procedure

To create the migration file, proceed as follows:

1. Select the path of the source file for the migration in the "Storage Location (Path)" field.
2. Specify the project parts that are to be migrated:

   - Select the "Include HW and Network data during the migration" check box to migrate not only the software but also the complete hardware parts and the network configuration of the project.
   - Select the "Copy SCADA runtime data" check box if you also want to migrate the runtime data, such as alarm archives, tag archives and user archives, in addition to the data of the engineering system.
3. Select the path and the file name for the migration file in the "Intermediate file" field.
4. Click the "Migrate" button.

##### Result:

A migration file is created. You now copy this file to the target system and migrate this file in the TIA Portal.

---

**See also**

[Migrating projects](#migrating-projects)
  
[Calling the migration tool](#calling-the-migration-tool)
  
[Migrating projects with the migration tool](#migrating-projects-with-the-migration-tool)

### Migrating projects

#### Requirement

- A converted file in the format ".am19" is already available or the original software with a valid license is installed for all configurations used in the initial project.
- The initial project is not provided with access protection.
- The initial project must be consistent, otherwise problem-free migration cannot be assured.

Read the additional information on the requirements in the help for the respective products installed.

> **Note**
>
> **System hibernation during the migration**
>
> While a migration is running, the system should not be changed to the standby or hibernate mode. Otherwise the migration will be aborted.

#### Procedure

To migrate a project, follow these steps:

1. Select the "Migrate project" command in the "Project" menu.

   The "Migrate project" dialog opens.
2. Specify the path and the file name for the project to be migrated in the "Source path" field. Select a project either in the ".am19" migration format or in the format of the initial project.
3. To include the hardware configuration in the migration, select the "Include hardware configuration" check box.

   If you have selected a migration file that was created with the migration tool, the check box cannot be selected. In this case, you must specify if you wish to include the hardware configuration in the migration before the conversion with the migration tool .
4. Select the "Copy WinCC Runtime Professional data" check box, if you also want to migrate the runtime data, such as alarm archives, tag archives and user archives, in addition to the data of the engineering system.

   If you have selected a migration file that was created with the migration tool, the check box cannot be selected. In this case, you must specify if you wish to include the SCADA runtime data in the migration before the conversion with the migration tool .
5. Select a name for the new project in the "Project name" box.
6. Select a path in the "Target path" box where the new project is to be created.
7. Enter your name or the name of another person responsible for the project in the "Author" field.
8. Enter a comment in the "Comment" box, if you require one.
9. Click "Migrate".

#### Result

The initial project is converted and a message appears after conversion is complete. The newly created project is then opened in the project view, and the migration log is opened in TIA Portal.

Even if the migration failed, a project directory is created and a migration log in the form of an XML file is generated in this directory. The completion message that appears after the migration contains a link to this XML file. Click the link to open the XML file. Alternatively, you can find the XML file in the project directory under "\Logs".

---

**See also**

[Post-editing integrated projects](#post-editing-integrated-projects)
  
[Display migration log](#display-migration-log)
  
[Using logs](Editing%20projects.md#using-logs)
  
[Migrating projects with the migration tool](#migrating-projects-with-the-migration-tool)
  
[Creating a migration file](#creating-a-migration-file)

### Displaying the history of the migration

If a project was created by migration, the migration will be listed in the table of the project history. You can open the migration log in the table. The time of the migration is also shown.

#### Procedure

To display the migration in an overview table, follow these steps:

1. Select the open project in the project tree.
2. Select "Properties" in the shortcut menu of the project.

   The dialog with the properties of the project opens.
3. Select the "Project history" group in the area navigation.

   The overview table is displayed.

---

**See also**

[Displaying properties of the project](Editing%20projects.md#displaying-properties-of-the-project)

### Display migration log

A log is created for each successful migration. The log contains the following information:

- Migrated objects
- Modifications to objects made during migration
- Errors that occurred during migration
- In certain cases a link to more help with specific events.

  In this case, click the question mark to obtain more help.

#### Procedure

To display the log file of the migration, follow these steps:

1. Open the "Common data > Logs" folder in the project tree.
2. Double-click the desired log in the list.

   The contents of the log are displayed in the work area.

---

**See also**

[Migration of projects with the TIA Portal](#migration-of-projects-with-the-tia-portal)
  
[Using logs](Editing%20projects.md#using-logs)

### Migrating integrated projects

This section contains information on the following topics:

- [Migrating an integrated project (S7-300, S7-400)](#migrating-an-integrated-project-s7-300-s7-400)
- [Post-editing integrated projects](#post-editing-integrated-projects)
- [Converting unspecified CPUs into specified CPUs](#converting-unspecified-cpus-into-specified-cpus)
- [Creating an integrated HMI connection](#creating-an-integrated-hmi-connection)
- [Re-linking HMI tags](#re-linking-hmi-tags)
- [Delete non-integrated HMI connection](#delete-non-integrated-hmi-connection)

#### Migrating an integrated project (S7-300, S7-400)

##### Introduction

In integrated projects, you use SIMATIC controllers and WinCC components together in a project. When an integrated project is migrated, the complete project will be migrated with components from WinCC and STEP 7. Configured connections between control and visualization remain intact.

##### Migrating an integrated project

When migrating an integrated project, the same requirements apply for the STEP 7 component as for the migration of a non-integrated STEP 7 project. The objects and properties contained in the WinCC component must also be supported in WinCC (TIA Portal).

For an operating station (OS) to be migrated, it has to be located below a PC station and the WinCC application in the project tree of SIMATIC Manager. The following figure shows the assignment of the operating station within the initial project:

![Migrating an integrated project](images/66691444363_DV_resource.Stream@PNG-de-DE.png)

Additional migration requirements for integrated projects can be found in the documentation for WinCC.

Also note that the initial project must be compiled before the migration.

In order to fully migrate an integrated project, the following components must be installed on the programming device/PC for the migration:

- STEP 7 V5.4 SP5 or higher
- WinCC V7.5 with the latest update or WinCC Flexible 2008 SP2 or higher

To be able to fully post-edit an integrated project, the latest version of the following components must be installed on the PC for post-editing:

- STEP 7 Professional
- WinCC Basic, WinCC Comfort/Advanced or WinCC Professional, depending on the components used

##### Using the migration tool

It is necessary to use the migration tool under the following circumstances:

- The initial project is not located on the same programming device/PC as the installation of the TIA Portal.
- SCADA devices are included in the initial project. These can only be migrated with the migration tool.
- WinCC Professional V19 and STEP 7 with WinCC V7.5 cannot be installed on the same PG/PC. Therefore, integrated projects with WinCC V7.5 parts must be prepared for migration using the migration tool.

##### Migration of the STEP 7 part of an integrated project

An integrated project is always fully migrated. Individual components cannot be migrated on their own. You can only migrate the included STEP 7 project alone, if you have previously deleted all HMI stations in the SIMATIC stations in the SIMATIC Manager and then recompiled the project in NetPro.

Alternatively, you can open the project in an installation of STEP 7 V5.4 SP5 or higher without an installation of WinCC. Then, save the project again and select the "Reorganize" function during saving. The WinCC parts are then automatically removed when the copy is saved.

You can then migrate the STEP 7 project without the WinCC project.

##### Migration of an integrated project with the hardware configuration

In integrated projects, HMI devices are migrated even if the hardware configuration is not included in the migration. The STEP 7 component of the hardware configuration, including network configurations, connections and interrupts, is migrated only if you include the hardware configuration in the migration. Otherwise, unspecified modules will be created for the STEP 7 devices and you will need to convert them into suitable modules after the migration.

HMI modules that are plugged into a PC station are converted to a separate Station during the migration. If you perform the migration without including the hardware configuration, the migrated project then contains a non-specified SIMATIC PC Station and a SIMATIC PC Station with the HMI devices. References to HMI devices are not imported during migration. When the hardware configuration is included, the migrated project contains two separate stations: the HMI Station and the PC Station.

##### Storage location of an integrated WinCC project

If you migrate an integrated project, the HMI part of it must be on the same PG/PC as the STEP 7 part of the project. If the HMI part is on a different PG, then only the STEP 7 part will be migrated.

##### Unsupported objects

The following components are not supported for migration:

- STEP 7 multiproject  
  A STEP 7 multiproject cannot be migrated. Migration will be canceled.
- Central Archive Server - CAS  
  If a CAS is part of an integrated project, then the migration will be carried out but the CAS data will not be migrated.

---

**See also**

[Post-editing integrated projects](#post-editing-integrated-projects)

#### Post-editing integrated projects

If you have migrated an integrated project without hardware configuration, unspecified CPUs are used instead of the CPUs of the original project. Since no connection can exist between an unspecified CPU and an HMI device, connections from the source project are also imported only unspecified.

##### Procedure

To continue to use an integrated project after the migration, follow these steps:

1. Convert the unspecified devices into suitable devices again.
2. Restore the integrated HMI connection between the HMI device and the PLC.
3. Connect all HMI tags to the newly created integrated connection.
4. Restore the connection between HMI tags and PLC tags.
5. Delete the non-integrated HMI connection.

In the following chapters a sample project is used to describe the individual steps in more detail.

---

**See also**

[Converting unspecified CPUs into specified CPUs](#converting-unspecified-cpus-into-specified-cpus)
  
[Creating an integrated HMI connection](#creating-an-integrated-hmi-connection)
  
[Re-linking HMI tags](#re-linking-hmi-tags)
  
[Delete non-integrated HMI connection](#delete-non-integrated-hmi-connection)

#### Converting unspecified CPUs into specified CPUs

The first step after the migration without hardware configuration is the conversion of the unspecified CPUs into specified CPUs. Unspecified CPUs are placeholders for certain CPUs from the hardware catalog that are not currently known. You can define general parameters and home the CPUs already in the user program. However, the project is not fully functional until the unspecified CPU has been specified.

##### Specifying a CPU using module replacement

To use module replacement to specify an unspecified CPU, follow these steps:

1. Select the unspecified CPU in the network or device view.
2. Select the "Replace device" command in the shortcut menu.

   The "Replace device" dialog opens.

   ![Specifying a CPU using module replacement](images/90535132299_DV_resource.Stream@PNG-en-US.png)

   ![Specifying a CPU using module replacement](images/90535132299_DV_resource.Stream@PNG-en-US.png)
3. Under "New device" in the tree structure, select the module with which you want to replace the unspecified CPU. (Area 1)

   "Compatibility information" provides you with information on the extent to which the selected CPU is compatible with the configuration in source project. (Area 2)
4. Click "OK".
5. Perform the above-described steps for all unspecified CPUs.

---

**See also**

[Creating an integrated HMI connection](#creating-an-integrated-hmi-connection)

#### Creating an integrated HMI connection

After you have specified the unspecified CPU, establish the connection to the HMI-device.

##### Procedure

To create a connection graphically, follow these steps:

1. On the toolbar, click the "Connections" icon. This activates connection mode.

   ![Procedure](images/90539095563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/90539095563_DV_resource.Stream@PNG-en-US.png)
2. Select the connection type "HMI connection" in the adjacent drop-down list.

   The network view highlights in color all CPUs and HMI devices that can be used for an HMI connection.
3. You can now have the connection path automatically determined, or explicitly select a connection path via specific interfaces:

   - Allow connection path to be automatically determined

     Select the source CPU for a connection. Drag the mouse to the target components. Confirm the connection endpoint with another mouse click.

     Alternatively: While holding down the shift button, select the target components and with the right mouse button select the "Add new connection" command.
   - Selecting an explicit connection path from interface to interface

     Click on the subnet interface in the device for which you want to create a connection. Hold down the mouse button, drag the cursor to the relevant interface in the target device and then release the mouse button.

     ![Procedure](images/28160149643_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/28160149643_DV_resource.Stream@PNG-de-DE.png)

##### Result

The following figure shows the state after the integrated connection has been created:

![Result](images/90539848075_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | An integrated HMI connection is created and highlighted in the network view. |
| ② | The connection is shown in the connection table of the components. |
| ③ | The connection can be edited in the connection properties. |

---

**See also**

[Re-linking HMI tags](#re-linking-hmi-tags)

#### Re-linking HMI tags

When you have created a new HMI connection between the CPU and HMI device, you have to assign the existing HMI tags to the new connection. Perform the following steps for each line in the relevant tag table.

##### Procedure

To re-link HMI tags, follow these steps:

1. In the project tree, navigate to the HMI tags and double-click the relevant tag table to show this in the work area.

   The tag table opens.

   ![Procedure](images/28199889803_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/28199889803_DV_resource.Stream@PNG-en-US.png)
2. Click the " ... " button in the "Connection" column.

   A dialog box for selecting the connection opens.
3. Select the newly established HMI connection.

   ![Procedure](images/28196230667_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/28196230667_DV_resource.Stream@PNG-en-US.png)
4. Click the "✓" button to apply the selected connection.
5. On the toolbar, click the "Re-connect PLC tag" button.

   ![Procedure](images/28205455371_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/28205455371_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Delete non-integrated HMI connection](#delete-non-integrated-hmi-connection)

#### Delete non-integrated HMI connection

Finally, you can remove non-integrated HMI connections that still remain from the source project.

##### Procedure

To delete the non-integrated HMI connections, follow these steps:

1. In the project tree, open the HMI device and double-click the "Connections" entry.

   The connection table opens.

   ![Procedure](images/28229655691_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/28229655691_DV_resource.Stream@PNG-en-US.png)
2. Select the row with the old connection in the table.
3. Select the "Delete" command in the shortcut menu of the connection line.
4. Perform the above-described steps for all non-integrated HMI connections of the source project.
