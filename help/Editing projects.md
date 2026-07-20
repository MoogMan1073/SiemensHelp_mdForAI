---
title: "Editing projects"
package: PEProject2MenUS
topics: 32
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Editing projects

This section contains information on the following topics:

- [Creating and managing projects](#creating-and-managing-projects)
- [Compatibility of projects](#compatibility-of-projects)
- [Archiving and retrieving projects](#archiving-and-retrieving-projects)
- [Using reference projects](#using-reference-projects)
- [Using TIA Portal Version Control Interface](Using%20TIA%20Portal%20Version%20Control%20Interface.md#using-tia-portal-version-control-interface)
- TIA Portal Teamcenter Gateway

## Creating and managing projects

This section contains information on the following topics:

- [The basics of projects](#the-basics-of-projects)
- [Creating a project](#creating-a-project)
- [Opening projects](#opening-projects)
- [Open recently used objects](#open-recently-used-objects)
- [Saving projects](#saving-projects)
- [Closing projects](#closing-projects)
- [Removing projects from the project list](#removing-projects-from-the-project-list)
- [Deleting projects](#deleting-projects)
- [Displaying properties of the project](#displaying-properties-of-the-project)
- [Using logs](#using-logs)
- [Security of industrial plants](#security-of-industrial-plants)
- [Importing and exporting CAx data](#importing-and-exporting-cax-data)

### The basics of projects

Projects contain data and programs resulting from the creation of an automation solution. The data assembled in a project include, for example:

- Configuration data on the hardware structure and parameter assignment data for modules
- Project engineering data for communication over networks
- Project engineering data for the devices
- Logs for important events in the life cycle of the project

#### Project version

The project version defines the version of the TIA Portal for which a project is compatible. A project that is compatible with the current version of the TIA Portal is provided in project version V19 of the TIA Portal.

You can view the project version of an already opened project in the project properties. To do so, select the "Software products in the project" entry in the "General" tab of the properties dialog. In the table, you can see all products and their versions, which are required for editing the open project.

#### Project hierarchy

Data is stored in a project in the form of objects. Within the project, the objects are arranged in a tree structure (project hierarchy).

The project hierarchy is based on the devices and stations along with the configuration data and programs belonging to them.

Common data of the project and online access, for example, are also displayed in the project tree.

#### Basic integrity check

The engineering software features a base-protective mechanism to detect changes in the essential custom project data (e.g. blocks, hardware configuration). Causes for changes to the project data, for example, can be tampering outside the engineering software or defects in the data storage medium.

The test of the configuration data is optional upon request, because, depending on the scope and application, it as can be time consuming, especially if you use multiuser engineering. You change the default for the test in the settings of the engineering software.

If a change is detected during a test, contact Siemens Customer Support. You can continue to work with the project data. Continue work at your own risk.

> **Note**
>
> **Reduced working speed when basic integrity check is activated**
>
> If you enable the basic integrity check in the settings of the engineering software, the operating speed of the engineering software is reduced.

#### Working with automatically synchronized network drives

A TIA Portal project consists of multiple files that are saved together in one directory. If you store a project that is automatically synchronized on a network drive or in a cloud directory (e.g. Dropbox, Syncplicity or Google Drive), this can lead to data loss if the synchronization only takes place partially or asynchronously. For this reason, we do not recommend editing TIA Portal projects directly on synchronized network drives or in cloud directories. Always close the TIA Portal project before synchronization and make sure that all directories and files from the project directory are synchronized together and completely. You might wish to disable automatic synchronization while working with the TIA Portal. The synchronization itself must be implemented in such a way that the current (local) project data replace the project data on the network drive or in the cloud directory.

#### Changing the storage path of open projects

A TIA Portal project consists of multiple files that are saved together in one directory.

If you change the name of the project directory or the storage path while the project is open and being edited, this could result in data loss.

Therefore, avoid making changes to the project directory and the storage path while projects are being edited, even if the storage environment you are using supports this.

#### Project protection

You can activate user management for a project and thereby protect your project. If protection is active for a project, you can only log on authorized users in the project and work with it.

See also: [Basics of user management property in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)

---

**See also**

[Overview of the program settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-program-settings)
  
[Changing the settings](Introduction%20to%20the%20TIA%20Portal.md#changing-the-settings)
  
[Overview of settings for the basic integrity check](Introduction%20to%20the%20TIA%20Portal.md#overview-of-settings-for-the-basic-integrity-check)
  
[Using logs](#using-logs)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)

### Creating a project

#### Procedure

To create a new project, follow these steps:

1. Select the "New" command in the "Project" menu.

   The "Create a new project" dialog opens.
2. Enter a project name and path or accept the suggested settings.
3. Click the "Create" button.

#### Result

The new project is created and displayed in the project tree.

---

**See also**

[Compatibility between TIA Portal versions](#compatibility-between-tia-portal-versions)
  
[The basics of projects](#the-basics-of-projects)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)

### Opening projects

You recognize projects of the TIA Portal by their file name extension ".ap[version number]". Projects of the current version have the file name extension ".ap19". Projects with the project version V19 can be opened immediately. Update projects with project version V13 SP1, V14, V14 SP1, V15, V15.1, V16, V17 and V18 before opening.

#### Procedure

To open an existing project, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog box opens and the list of recently used projects is displayed.
2. Select a project from the list and click "Open".
3. If the project you require is not included in the list, click the "Browse" button. Navigate to the desired project folder and open the project file.
4. To check whether the project has been changed without permission, select the check box "Activate basic integrity check". The basic integrity check may take some time to complete.
5. Click the "Open" button.

   If protection is active for the selected project, the "Login" dialog opens. Then perform the following steps:

   - Select the required user type.
   - Enter your user name.
   - Enter your password.
   - Click "OK".

   The project is opened if either project protection is not active or if you have logged on with a user account with the corresponding rights. Further information on user management can be found under "[Basics of user management property in TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)".

   If you have selected a project from the V13 SP1, V14, V14 SP1, V15, V15.1, V16, V17 or V18 version of the TIA Portal, the "Upgrade project" dialog opens. You can find more information on upgrading projects under "[Upgrading projects](#upgrading-projects-1)".

#### Checking for missing software components

When opening existing projects, an automatic check is made to determine if the appropriate software is installed for all modules used within the project. If you try to open a project with modules that are not supported by the current scope of installation of the TIA portal, a message appears on opening the project informing you of the missing software components. If the software components are not absolutely required to open the project, the project can still be opened.

If a project cannot be opened in the TIA Portal due to missing software components, you can download and install it as trial software from Siemens Industry online support. You can then open the project. Note that the trial software can only be used for a limited period of time.

Use the following link to open the page in Siemens Industry online support, where the various software products are available to you as trial software: [www.siemens.com/tia-portal-trial](http://www.siemens.com/tia-portal-trial)

#### Reaction to missing software components

Unsupported modules of a project are handled as follows:

- Display of the modules on the user interface

  - The unsupported modules are displayed in the project tree with all of their lower-level objects. However, the modules themselves cannot be processed in editors or in the inspector window. When possible, a replacement module is used that best matches the original module. Replacement modules are indicated by an exclamation mark.
  - Display of properties in tables is limited. This applies in particular to the display of network parameters, such as the IP address.
- Functional limitations

  - Unsupported modules cannot be printed out or compiled.
  - An online connection cannot be established to the modules. It is therefore also impossible to download.
  - To change the device type, the device must first be deleted and then re-inserted. The "Change device type" function is not supported.
  - Copying and inserting lower-level objects, such as blocks, is possible although the device itself cannot be copied and inserted.
  - The network configuration cannot be changed with replacement modules within the network view.
  - Cross-references can be displayed. However, the cross-references only reflect the status last saved within the project because on online comparison with the original module cannot be made.

---

**See also**

[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)
  
[Displaying the installed software](Installation.md#displaying-the-installed-software)
  
[Compiling project data](Editing%20project%20data.md#compiling-project-data-1)
  
[Opening a global library](Using%20libraries.md#opening-a-global-library)
  
[Modifying or updating installed products](Installation.md#modifying-or-updating-installed-products)
  
[Checking availability of updates and support packages and installing them](Installation.md#checking-availability-of-updates-and-support-packages-and-installing-them)

### Open recently used objects

The menu command "Edit &gt; Open last object used" can be used to display the objects recently used in the TIA Portal and to open them in the connected editors. This function allows users to quickly resume editing their recently used objects directly from the menu.

The list shows the 20 most recently used objects in the order of their last use.

The menu command "Clear list" can be used to remove all entries from the list.

The view of the list is linked to the currently active area, for example, to a navigation view or the editor used.

The lists are available for the following areas:

- Projects and project libraries
- Global libraries
- Multiuser local sessions and server projects
- Reference projects
- Online access

If multiple instances of the TIA Portal are open, the view of the last used objects is saved from the last closed instance.

The list of recently used objects is linked to the Windows user profile. Therefore, the list is retained even after the TIA Portal has been closed.

### Saving projects

You can save the project at any time either under the same or a different name. You can even save a project when it still contains elements with errors.

#### Saving a project

To save a project, follow these steps:

1. Select the "Save" command in the "Project" menu.

   All changes to the project are saved under the current project name.

#### Project Save as

To save a project under another name, follow these steps:

1. Select the "Save as" command in the "Project" menu.

   The "Save current project as" dialog opens.
2. Select the project folder in the "Save in" box.
3. Enter the new project name in the "File name" box.
4. Confirm your entry with "Save".

   The project is saved under the new name and opened.

> **Note**
>
> **Undoing actions**
>
> Keep in mind that you cannot undo actions once you have saved the project.

---

**See also**

[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)

### Closing projects

#### Procedure

To close a project, follow these steps:

1. Select the "Close" command in the "Project" menu.

   If you have made changes to the project since the last time you saved it, a message is displayed.
2. Decide whether or not you want to save the changes.

---

**See also**

[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)

### Removing projects from the project list

You can remove projects from the list of recently used projects. The project data is retained on the storage medium.

#### Procedure

To remove a project from the list of recently used projects, follow these steps:

1. Select the "Delete project" command in the "Project" menu.

   The "Delete project" dialog opens and includes the list of most recently used projects.
2. Select a project from the list.
3. Click the "Remove" button.
4. Click "Yes" to confirm the prompt in order to remove the project from the list.

#### Result

The project is no longer displayed in the list of recently used projects. If you open the project again, it will be added to the list again.

---

**See also**

[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Deleting projects](#deleting-projects)

### Deleting projects

Deleting removes the entire project data from the storage medium.

#### Requirement

The project you want to delete is not open.

#### Procedure

Follow the steps below to delete an existing project:

1. Select the "Delete project" command in the "Project" menu.

   The "Delete project" dialog opens and includes the list of most recently used projects.
2. Select a project from the list.

   If the project you require is not included in the list, click the "Browse" button. Navigate to the desired project folder, and open the project file.
3. Click the "Delete" button.
4. Click "Yes" to confirm. This starts the deletion of the project.

#### Result

The entire project folder is deleted from the file system.

---

**See also**

[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)

### Displaying properties of the project

You can display the properties of a project. In the "General" tab you find the following project properties in the area navigation:

- Metadata for the project

  This includes the following information: creation time, author, file path, project size, copyright, project languages, etc. Many of the properties can be changed.
- Project history

  The project history contains an overview with important events in the project life cycle. Here, for example, you can see the version of the TIA Portal used to create a project and whether it has been upgraded in the meantime. If a project was created during a migration, for example, this is also indicated in the project history table with the date and time of the migration. If a log was created for an event, you can also call the log directly.
- Support packages in the project

  An overview of the add-on software needed to work with all devices in the project is displayed. In addition, installed GSD files are listed (device description files for other devices in the hardware catalog).
- Software products in the project

  You can display an overview of all installed software products needed for the project. The "Version" column shows the project version of the respective software with which the project is stored.

In the "Protection" tab you specify that blocks can be simulated after the compilation with SIMATIC S7-PLCSIM Advanced. To do this, select the check box "Support simulation during block compilation". By default, the function is disabled.

If you want to use blocks from S7-1500 CPUs in virtual CPUs, select the "Allow use of S7-1500 blocks in virtual S7-1500 CPUs" check box in the "Protection" tab. By default, the function is disabled.

#### Procedure

To display the project properties, follow these steps:

1. Select the open project in the project tree.
2. Select "Properties" in the shortcut menu of the project.

   The dialog with the properties of the project opens.
3. Select the project properties in the area navigation that you want to have displayed.

---

**See also**

[Displaying the history of the migration](Migrating%20projects%20and%20programs.md#displaying-the-history-of-the-migration)
  
[Checking availability of updates and support packages and installing them](Installation.md#checking-availability-of-updates-and-support-packages-and-installing-them)
  
[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)

### Using logs

For some operations within the TIA Portal, logs are created automatically in the background. These logs document changes in the project. Logs are created automatically, for example, when you migrate projects and programs or when you update instances from the library.

Logs are displayed in the "Common data" folder in the project tree. They are stored in zip files together with the project in the project folder and can therefore be read as soon as you open the project independent of the programming device / PC used. The log can be filtered for errors, warnings, and information.

In addition to displaying them in the TIA Portal, logs can also be printed.

#### Displaying logs

To open a log, follow these steps:

1. Open the "Common data &gt; Logs" folder in the project tree.
2. Double-click the desired log in the list.

   The contents of the log are displayed in the work area.
3. Optional: To show or hide a particular category of alarms, activate or deactivate the button for "Errors", "Warnings", or "Information" in the toolbar.

#### Deleting logs

To delete a log, follow these steps:

1. Select the log in the project tree.
2. Press &lt;Del&gt;.

   The selected log is deleted from the project directory and removed from the project tree.

### Security of industrial plants

In addition to numerous advantages, the ongoing digitization of industrial automation is accompanied by increased vulnerability of industrial plants. The TIA Portal and the SIMATIC products already have several features that ensure secure operation of your plant, for example:

- Know-how protection of blocks
- Basic integrity protection for projects to protect projects against manipulation
- The protection and security functions of CPUs

Further information and the possibility for reporting security problems can be found online at the following link:

[Whitepapers and additional information](https://www.industry.siemens.com/topics/global/en/industrial-security/support/Pages/white-papers.aspx)

#### Industrial Security

Industrial Security goes beyond the security regulations and measures in office environments. Industrial Security is a comprehensive approach to protecting industrial plants. The approach is designed to protect against unauthorized access, sabotage, espionage and malicious tampering. Industrial security ensures the following factors:

- Availability

  Availability has highest priority in industrial plants. Downtime must be kept as low as possible.
- System and data integrity

  A third party should not be able to unlawfully modify the plant and any of its data.
- Confidentiality

  Information on the industrial plant and data must not fall into the hands of unauthorized third parties.

#### Comprehensive approach

In addition to the security features integrated in the TIA Portal, Industrial Security requires more comprehensive measures. Observe the following security aspects:

- Plant safety

  - Access protection against unauthorized persons
  - Physical access protection for critical components
- Network security

  - Controlled interfaces between an office and plant network, for example, through firewalls
  - Segmentation of the plant network
- System integrity

  - Use of anti-virus and whitelisting software
  - Compliance with maintenance and update processes
  - User authentication for the machine or plant operator
  - Integrated access protection in automation components

### Importing and exporting CAx data

CAx files are XML files that you create in the TIA Portal and that you can swap between different installations or with other tools such as ECAD systems. The files contain the following information:

- Hardware configuration of a single device or an entire project (without parameter assignment)
- Folder hierarchies (groups)

  The folder hierarchy is restored for the import.
- Association of a device to a subnet

  When importing, the devices stored in the CAx file are reconnected to the same subnet.
- Addresses of the devices
- Address areas of inputs and outputs
- Profinet I/O systems and PROFIBUS DP master systems

#### Requirements

- TIA Openness is installed.

  TIA Openness is installed automatically by the setup program of the TIA Portal. To do so, the check box for TIA Openness must be selected in the setup program under "Options" in the "Configuration" menu.
- A project is open.

#### Exporting the CAx file of a project

1. In the "Tools" menu, click on "Export CAx data...".
2. In the "CAx Export" dialog, select a directory for the file to be exported.
3. If necessary, change the file name and confirm with "Save".

   A dialog shows the export progress. If you need to cancel the export, click "Cancel".

   You see the status of the export in the "Info &gt; General" tab of the Inspector window. In addition, a log file is created in the directory that you entered as the storage location for log files under "Settings &gt; General &gt; Data exchange".

   The exported file receives the file extension ".aml".

#### Exporting the CAx file of a device

1. Highlight the exported devices in the project tree.
2. Select "Export CAx data ..." from the shortcut menu.
3. In the "CAx Export" dialog, select a directory for the file to be exported.
4. If necessary, change the file name and confirm with "Save".

   A dialog shows the export progress. If you need to cancel the export, click "Cancel".

   You see the status of the export in the "Info &gt; General" tab of the Inspector window. In addition, a log file is created in the directory that you entered as the storage location for log files under "Settings &gt; General &gt; Data exchange".

   The exported file receives the file extension ".aml".

#### Import CAx file of a device or a project

1. In the "Tools" menu, click on "Import CAx data...".
2. Select a CAx file in a directory in the "CAx Import" dialog.
3. Click the "Open" button.

   A dialog shows the import progress. If you need to cancel the import, click "Cancel".

   You receive feedback about the status of the import of devices, for example error messages, in the inspector window in the "Info &gt; General" tab. In addition, a log file is created in the directory that you entered as the storage location for log files under "Settings &gt; General &gt; Data exchange".

#### Permitted exchange formats for CAx data

The standardized data exchange format "AutomationML" is used to exchange CAx data. The exchange files receive the extension "*.aml". Exporting and importing files with the extension "*.xml" is not supported.

The log files generated during the data exchange receive the extension "*.log". Logs files with the extension ".txt" are not supported.

#### Exchanging CAx data with other applications

Plugged in submodules such as bus adapters can have a different hierarchical structure in the TIA Portal and in other applications. The AML files for exchanging CAx data therefore display the submodules in a customized hierarchy that can be read by all programs. During import, the hierarchy of submodules in the AML file does not affect the hierarchy of submodules in the TIA Portal.

> **Note**
>
> **Compatibility between different product versions.**
>
> If you want to exchange files with devices that contain bus adapters, note the following information on compatibility:
>
> AML files created with an older version of the TIA Portal can be imported with the current version.
>
> AML files created with the current version of the TIA Portal cannot be imported with older versions.

#### Import options with name conflicts of stations

If you want to import a CAx file and the currently open TIA Portal project included stations with identical names, a conflict arises. A dialog for setting the import options opens. Before you import the file, you select how the stations with the same name are to be merged. The stations from the CAx file can be optionally renamed and grouped together in a new folder.

> **Note**
>
> **Default name of the folder**
>
> The folder for the stations to be imported are named "ParkingLot" by default.
>
> You can specify the name of the new folder yourself. To do this, open the settings and navigate to the "CAx" item. Enter the name for the folder with "Settings for conflict resolution" in the "Name of store for devices that already exist in the project" field.

Optionally, you can also specify that the stations triggering a conflict are either not to be imported or replaced by stations of the same name in the currently open TIA Portal project.

---

**See also**

[Overview of the CAx settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-cax-settings)

## Compatibility of projects

This section contains information on the following topics:

- [Compatibility between TIA Portal versions](#compatibility-between-tia-portal-versions)
- [Using projects created with optional software](#using-projects-created-with-optional-software)
- [Upgrading projects](#upgrading-projects)
- [Compatibility with the plant configuration](#compatibility-with-the-plant-configuration)

### Compatibility between TIA Portal versions

With the TIA Portal V19, you can also open projects that were created with this version of the TIA Portal. You need to upgrade projects from previous versions of the TIA Portal to the current version before opening them.

#### Opening projects from previous versions of the product

The following table shows the response of the TIA Portal when opening projects from a previous version of the product:

| Version of the TIA Portal  (file extension of the respective version) | Response when opened with the current version of the TIA Portal |
| --- | --- |
| V10.5 (.ap10)  V11.x (.ap11)  V12 (.ap12)  V12 SP1 (.ap12)  V13 (.ap13) | Projects from previous versions of V13 SP1 of the TIA Portal cannot be directly opened with TIA Portal V18. When you attempt to open the project, a message prompts you to open the project with the version V13 SP1.   If you open the project with TIA Portal V13 SP1 version, the project is upgraded to the project version V13 SP1 after your confirmation and is assigned the file extension ".ap13". |
| V13 SP1 (.ap13)  V14 (.ap14)  V14 SP1 (.ap14)  V15 (.ap15)  V15.1 (.ap15_1)  V16 (.ap16)  V17 (.ap17)  V18 (.ap18) | Once you give your confirmation, the project is upgraded to project version V19 upon opening and gets the file extension ".ap19". |

#### Backward compatibility of the current version of the TIA Portal

Projects that you save in the current project version V19 are not backward compatible due to the expanded functionality over previous versions. Projects with the project version V19 can only be opened with TIA Portal V19 or higher.

#### Open projects with assigned function rights

If specific function rights were set up in the user management, the user management for this project can only be opened in the product versions that support these function rights.

#### Loading project data with TIA Portal V12 and V13 (S7-1200)

If you load the project data of an S7-1200 CPU with TIA Portal V13, you can no longer use TIA Portal V12 to access this data. To do this, first restore the factory settings of the CPU. Read the additional information on this in the online help under "How to reset a CPU to factory settings".

### Using projects created with optional software

A wide range of optional software is available for the TIA Portal. This includes hardware support packages, for example. When you open a project that was created with optional software but the optional software is not installed, the following will occur:

- Software components which are not absolutely required are missing:

  A dialog appears listing the missing software components. After the project is opened, its properties are displayed. You now have the opportunity to install missing components. All the devices contained in the project are available even if you do not install the missing components. However, you can only work with the devices that are supported by the currently installed software.

  Devices which are not supported because software components are missing are identified by the following symbol in the project tree:

  ![Figure](images/25794110603_DV_resource.Stream@PNG-de-DE.png)
- Essential software components are missing:

  A dialog appears listing the missing software components. The essential software components are marked. The project can only be opened if you install the missing software components.

  When objects of a specific software component are removed from a project, meta information remains in the project. If the software component is not currently installed, this meta information prevents opening of the project.

  You can remove unnecessary meta information with the "Clean up" function in the "Open project" dialog.

  The function creates and cleans up a copy of the project. The original project remains unchanged.

  When cleanup is successful, the cleaned-up copy of the project opens.

  When cleanup is not successful, an error message appears, and the copy of the project is deleted.

---

**See also**

[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Opening projects](#opening-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)
  
[Compatibility of global libraries](Using%20libraries.md#compatibility-of-global-libraries)
  
[Overview of Migration Options](Migrating%20projects%20and%20programs.md#overview-of-migration-options)

### Upgrading projects

This section contains information on the following topics:

- [General information on upgrading projects](#general-information-on-upgrading-projects)
- [Upgrading projects](#upgrading-projects-1)
- [Upgrading multiuser engineering projects](#upgrading-multiuser-engineering-projects)
- [Upgrading know-how protected blocks](#upgrading-know-how-protected-blocks)
- [Upgrading WinCC projects](#upgrading-wincc-projects)

#### General information on upgrading projects

A project from the version V13 SP1 of the TIA Portal can be opened only after they have upgraded the project to the current version of the TIA Portal. When you open the project, you are prompted to upgrade the project.

To learn about the options available with other product versions of the project, refer to the section "[Compatibility between TIA Portal versions](#compatibility-between-tia-portal-versions)".

##### Upgrading modules with know-how protection

Blocks with know-how protection are not automatically upgraded with the project.

In order to open and edit a block with know-how protection in the editor after upgrading the project, remove the know-how protection and then set it up again.

You can find additional information in the section "[Upgrading know-how protected blocks](#upgrading-know-how-protected-blocks)".

##### Upgrading protected projects

If you want to upgrade a project which is protected with the administration property from an earlier product version, you have to be registered in this project as a project administrator and need the access data for the project.

To upgrade a protected project, you require the "Upgrade project" function right. Additional function rights or roles are necessary depending on the version of the project to be upgraded.

When protected projects are upgraded, the "Login" dialog opens. To continue with the procedure select the user type and enter your user name and your password.

You can find additional information in the sections "[Basics of user management in TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)" and "["Upgrade project" function right](Managing%20users%20and%20roles.md#function-right-upgrade-project)".

##### Upgrading global libraries

Global libraries are not upgraded automatically together with the project because they are independent of projects. If you want to continue using global libraries from older versions of the TIA Portal, upgrade the global libraries as well. You can find more information on upgrading global libraries in the section "[Compatibility of global libraries](Using%20libraries.md#compatibility-of-global-libraries)".

##### Instruction version

The instructions that you use to create your user program may be in different versions. Different product versions of the TIA Portal can contain different instruction versions. You have the option to upgrade the project and instructions to the latest version. You can then use the new instruction versions. After upgrading, the new instruction versions are not automatically used in your program. You can update your program to use the new versions. You can find more about "Instruction versions" in the "Programming editor" section.

##### Multiuser Engineering

To upgrade multiuser engineering projects, read about the prescribed procedure in the section "[Upgrading multiuser engineering projects](#upgrading-multiuser-engineering-projects)".

##### Upgrading projects with a missing license

No license is required to upgrade projects. If you do not have a license or do not have a suitable license, you cannot use the full range of functions in the products.

With a STEP 7 Basic license, for example, you cannot use functions provided by a STEP 7 Professional license.

##### Device backups after upgrading a project

If your project contains backups of devices, they are not updated during upgrade of the project. If you compile your program data after upgrading your project and load the data to your devices, create a new backup of your devices afterwards.

To create backups of devices, follow the procedure described in the section "[Creating a backup of an S7 CPU](Creating%20a%20backup%20of%20an%20S7%20CPU.md#backup-options-for-s7-cpus)".

##### Online connection after upgrading a project

If no blocks were modified in an upgraded project, no online/offline difference is usually indicated for the blocks or PLC data types. The right-hand column in the project tree shows the following symbol: Online connection after project upgrade   
If no blocks or PLC data types were modified in an upgraded project, no online/offline difference is usually indicated for the blocks. The right-hand column in the project tree shows the following symbol: ![Online connection after upgrading a project](images/104479166731_DV_resource.Stream@PNG-de-DE.png)

If an online/offline difference is shown if no blocks or PLC data types were modified, the problem is most likely a checksum inconsistency. The right-hand column in the project tree shows the following symbol: ![Online connection after upgrading a project](images/165303527819_DV_resource.Stream@PNG-de-DE.png)

The blocks or PLC data types are compatible despite the checksum inconsistency, i.e. the program execution is not affected by the upgrade. You can establish an online connection and start monitoring immediately after upgrading.

For more information, refer to the Compare editor:

- Online/offline differences in the "Block properties" category are due to checksum inconsistency. The blocks are compatible.
- On the other hand, online/offline differences in the "Target data" category indicate actual differences in the program code and require you to recompile and reload the program.

See also: "[Overview of the compare editor](Editing%20project%20data.md#overview-of-the-compare-editor)".

---

**See also**

[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Upgrading projects](#upgrading-projects-1)
  
[Displaying properties of the project](#displaying-properties-of-the-project)

#### Upgrading projects

The following will show you how to upgrade projects from earlier versions of the TIA Portal.

##### Upgrading projects from TIA Portal V14 or higher

To upgrade a project from TIA Portal V14, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog box opens and the list of recently used projects is displayed.
2. Select a project from the list and click "Open".
3. If the project you require is not included in the list, click the "Browse" button. Navigate to the desired project folder and open the project file.

   The "Open project" dialog opens.
4. Click "Upgrade".

   The "Upgrade project/library" dialog box opens.
5. Click "OK".

   The project is upgraded and opened in the current version of the project.
6. Compile the hardware of all devices in the project by selecting the "Compile &gt; Hardware (rebuild all)" command in the shortcut menu of the devices.

##### Upgrading projects from TIA Portal V13 SP1

To upgrade a project from TIA Portal V13 SP1, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog box opens and the list of recently used projects is displayed.
2. Select a project from the list and click "Open".
3. If the project you require is not included in the list, click the "Browse" button. Navigate to the desired project folder and open the project file.

   The "Open project" dialog opens.
4. Click "Upgrade".

   The "Upgrade project/library" dialog box opens.
5. Click "OK".
6. Click "OK" to confirm the prompt window.

   The project is upgraded and opened in the current version of the project.
7. Compile the hardware and software of all devices in the project.

##### Upgrading TIA Portal V13 SP1 projects with master copies from TIA Portal V10.5

Before upgrading a project, check if the master copies created with TIA Portal V10.5 are contained in its project library. This is necessary, for example, if you receive a message during the upgrade about an S7-1200 CPU with firmware version V1.0 used in the project, even though you have not configured such a CPU. The CPU is a master copy in the project library in this case.

Before upgrading a project with master copies from TIA Portal V10.5, therefore, do the following:

1. Use each master copy created with the TIA Portal V10.5 once in the project.
2. Delete the affected master copies from the project library.
3. Create the master copy again with the objects from the project.
4. Save the project in TIA Portal V13 SP1.

You can then upgrade the project to the latest version.

##### Upgrading projects from the TIA Portal V13 or earlier

Projects of product version V13 or earlier cannot be upgraded and opened with the TIA Portal. First upgrade projects from TIA Portal V13 or earlier with the product version V13 SP1. Then, upgrade the projects with the current version of the TIA Portal again to the current project version.

You can find additional information on upgrading projects from earlier product versions in the [Siemens Industry online support](https://support.industry.siemens.com/cs/ww/en/view/109476392).

---

**See also**

[Upgrading know-how protected blocks](#upgrading-know-how-protected-blocks)
  
[General information on upgrading projects](#general-information-on-upgrading-projects)
  
[Upgrading multiuser engineering projects](#upgrading-multiuser-engineering-projects)
  
[Compatibility of global libraries](Using%20libraries.md#compatibility-of-global-libraries)
  
[The basics of projects](#the-basics-of-projects)
  
[Creating a project](#creating-a-project)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Opening projects](#opening-projects)
  
[Displaying properties of the project](#displaying-properties-of-the-project)
  
[Saving projects](#saving-projects)
  
[Closing projects](#closing-projects)
  
[Removing projects from the project list](#removing-projects-from-the-project-list)
  
[Deleting projects](#deleting-projects)
  
[Compiling project data](Editing%20project%20data.md#compiling-project-data-1)

#### Upgrading multiuser engineering projects

The following will show you how to upgrade multiuser engineering projects.

##### Procedure

To upgrade multiuser engineering projects, follow these steps:

1. Before upgrading, save all existing local sessions in the multi-user server project.
2. Save the multiuser server project as a single-user project.
3. Upgrade the single-user project.
4. After the upgrade, create a multiuser project again from the single-user project.
5. Create the local sessions again from the upgraded multiuser project for all workers.

---

**See also**

[Upgrading projects](#upgrading-projects-1)
  
[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)

#### Upgrading know-how protected blocks

For security reasons, the know-how protection of blocks is tied to the version of the TIA Portal with which the know-how protection was set up. This means blocks that were assigned know-how protection in an earlier product version cannot be opened and edited with the previous password after the upgrade. However, the blocks can be downloaded to the controller and are executable. If you want to open and edit the block after the upgrade, remove the know-how protection of the blocks and set it up again.

##### Procedure

To upgrade know-how protected blocks, follow these steps:

1. Remove the know-how protection of the blocks from the previous version in the "Edit" menu with the "Know-how protection" command.

   For more detailed information, refer to section "Removing know-how protection for blocks".
2. Upgrade the project as described in the section "[Upgrading projects](#upgrading-projects-1)".
3. Set up the know-how protection of the blocks from the current product version again in the "Edit" menu with the "Know-how protection" command.

   For more detailed information, refer to section "Setting up know-how protection for blocks".

---

**See also**

#### Upgrading WinCC projects

##### Error during upgrade

If a project contains devices or device versions that are no longer supported in the current version of WinCC, you get the error message "Open the project with an older version of WinCC and change the device or the device version in the project and the library." To upgrade the project to the current version, you need to open the project in an older version of WinCC and change the device type or version to a value supported by the current version of WinCC.

Unsupported devices may be present in a project in the following locations:

- Devices in the project tree
- Devices in the master copies of the project library

##### Changing the device type or the device version in the project tree

To change the device type or the device version of a device in the project tree, follow these steps:

1. In the project tree, select the "Change device/version" command in the shortcut menu of the outdated device.
2. In the "Change device" dialog, select as new device a device or device version that is supported in the current version of WinCC.

##### Changing the device type or device version in the library

To change the device type or the device version of a device in the project library, follow these steps:

1. Search for the outdated device in the master copies of the project library.
2. Copy the master copy from the project library to the project tree.
3. Make a note of the name of the master copy. Delete the master copy in the project library.
4. In the project tree, select the "Change device/version" command in the shortcut menu of the outdated device.
5. In the "Change device" dialog, select as new device a device or device version that is supported in the current version of WinCC.
6. Create a new master copy of the project library from this device.
7. Give the new master copy the same name as the deleted master copy.

##### Large version differences

For larger version jumps, e.g. upgrading from V13 to V17, it is possible that none of the device versions offered in V13 are still supported in V17. In this case, you need another WinCC version, e.g. V15.1, with which you first change the outdated devices in V15.1.

1. Upgrade the project to V15.1.
2. In V15.1, change the device type or the device versions of all outdated devices in the project tree and library.
3. Upgrade the project to V17.
4. Optional: In V17, change the device type or the device versions of all outdated devices in the project tree and library.

##### Devices and device versions not supported

|  | WinCC V16 | WinCC V17 | WinCC V18  WinCC V19 |
| --- | --- | --- | --- |
| KTP400 Basic 2nd Generation |  | 13.0.0.0, 14.0.0.0 | 13.0.0.0, 14.0.0.0 |
| KTP700 Basic 2nd Generation |  | 13.0.0.0, 14.0.0.0 | 13.0.0.0, 14.0.0.0 |
| KTP900 Basic 2nd Generation |  | 13.0.0.0, 14.0.0.0 | 13.0.0.0, 14.0.0.0 |
| KTP1200 Basic 2nd Generation |  | 13.0.0.0, 14.0.0.0 | 13.0.0.0, 14.0.0.0 |
| KTP400F Mobile | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP700 Mobile | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP700F Mobile | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP900 Mobile | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP900F Mobile | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| Mobile Panel 177 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| Mobile Panel 277 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| KP400 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP700 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP900 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP1200 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP1500 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 |
| KP1500 Comfort V2 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| KTP400 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP700 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP700 Comfort INOX PCT | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| TP700 Comfort Outdoor | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP900 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP900 Comfort INOX PCT | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1200 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP1200 Comfort INOX PCT | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1200 Comfort PRO | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1500 Comfort | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 |
| TP1500 Comfort Outdoor | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1500 Comfort V2 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| TP1900 Comfort PRO | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| TP2200 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 |
| TP2200 Comfort V2 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |
| WinCC Runtime Advanced | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 | 11.0.0.0, 12.0.0.0 |

You can find detailed compatibility lists of all HMI devices using the [compatibility tool](https://support.industry.siemens.com/kompatool/pages/main/index.jsf) in Industry Online Support.

### Compatibility with the plant configuration

To be able to use all the online functions, the plant configuration with TIA Portal V19 must be compatible with the project version of the opened project. The following factors for the compatibility are especially relevant when designing the plant:

- Hardware and its firmware version  
  The individual devices and their firmware version must be supported by the TIA Portal V19 and within the opened project.
- The user program on the respective devices

  All blocks and instructions on the devices must be available in TIA Portal V19 and ready for using with the project version of the opened project.

#### Influence of the project version on compatibility

With TIA Portal V19, you can edit projects for project version V19. You can only load the hardware configuration and software of the system which is compatible with your version of the TIA Portal.

With CPUs of the S7-1200 and S7-1500 product series, you see the project version with which the blocks on the CPU are compatible on the display, on the Web server and in the online and diagnostics view of the TIA Portal. Note, however, that a compatible version of the project alone is not enough to work with the CPU. The CPU itself and its firmware version must be compatible with the installed version of the TIA Portal and the various installed products.

You can see the project version of the currently open project in the project properties.

#### Online connection after upgrading a project

When you upgrade a project from Version V14, V14 SP1, V15, V15.1, V16, V17 or V18 to Version V19, you can then connect devices online that were loaded with Version V14, V14 SP1, V15, V15.1, V16, V17 or V18. The blocks of these devices remain functional and do not have to be recompiled. Bug fixes to the project during upgrading may require blocks to be recompiled.

You can this expand the plant configuration or add functionality to devices, for example, without the changes affecting other devices in the plant configuration.

The difference in the project version is indicated in the project tree and in the compare editor by an overlay symbol on the device.

The following symbol indicates the difference in project version when no program blocks have been modified: ![Online connection after upgrading a project](images/104479166731_DV_resource.Stream@PNG-de-DE.png)

If no blocks were modified, no online/offline difference is indicated for the blocks.

The following symbol indicates the difference in project version when blocks have been modified: ![Online connection after upgrading a project](images/104479175563_DV_resource.Stream@PNG-de-DE.png)

If blocks were modified, an online/offline difference is indicated for the blocks. You cannot load these blocks from the device because only blocks of the same version can be loaded to TIA Portal V19.

#### Incompatible blocks

An offline/online comparison is performed for the configured devices when an online connection exists. If the blocks that are only available online are incompatible with the project version of the open project, the incompatible blocks are labeled as incompatible in the project tree with the following symbol: ![Incompatible blocks](images/85778335115_DV_resource.Stream@PNG-de-DE.png)

A block comparison in the compare editor is not possible because the blocks that are available online cannot be displayed.

#### Loading software to a device

If you want to load the software to a device that was last loaded with TIA Portal V18 or an earlier version, then load the entire software to the device again. It is not possible in this case to only load the changes. On devices that were last loaded with TIA Portal V19 or a later version, you can also load only the changes to the software.

---

**See also**

[General information on loading](Editing%20project%20data.md#general-information-on-loading)
  
[The basics of projects](#the-basics-of-projects)
  
[General information on upgrading projects](#general-information-on-upgrading-projects)
  
[Upgrading projects](#upgrading-projects-1)
  
[Basics of project data comparison](Editing%20project%20data.md#basics-of-project-data-comparison)
  
[Displaying properties of the project](#displaying-properties-of-the-project)

## Archiving and retrieving projects

This section contains information on the following topics:

- [Working with project archives](#working-with-project-archives)
- [Creating a project archive](#creating-a-project-archive)
- [Retrieving compressed project](#retrieving-compressed-project)

### Working with project archives

#### Archiving and transferring projects

If you work for a long time with a project, large files may result, especially with extensive hardware configurations. Therefore, you may want to reduce the size of the project, for example, when you archive it to an external hard drive, or when you send it via e-mail and require a smaller file size.

You can create a project archive to reduce the size of the project. TIA Portal project archives are compressed or uncompressed files, each containing an entire project including the entire folder structure of the project. Before the project directory is compressed into the archive file, all files are reduced to their essential components to further decrease the size of the project.

Project archives have the file extension ".zap[version number of the TIA Portal]". Projects created with TIA Portal V19 have the file extension ".zap19".

To open a project archive, retrieve the project archive. By retrieving it, the archive file with the included project files is extracted to the original project directory structure.

---

**See also**

[Retrieving compressed project](#retrieving-compressed-project)
  
[Creating a project archive](#creating-a-project-archive)
  
[Protection concept for project data](Editing%20project%20data.md#protection-concept-for-project-data)

### Creating a project archive

Projects of the current product version can be archived as compressed or uncompressed files. The projects to be archived do not have to be open in TIA Portal to do this.

The storage space of projects can be reduced by archiving projects in compressed files.

> **Note**
>
> The most recently saved state of an open project is used for archiving. Therefore, save the project before using the archiving function. This will ensure that your most recent changes are included in the archived project.

#### Procedure

To archive a project, follow these steps:

1. Select the "Archive ..." command from the "Project" menu.

   The "Archive" dialog opens.
2. Select a project file with the extension ".ap19" in the "Source path" field.
3. To create a compressed archive file, select the "Archive as compressed file" option.
4. If you do not want to archive the search index and the HMI compile result, select the option "Discard restorable data".

   You can restore the discarded data if needed.
5. To add a date and time automatically, select the "Add date and time to the target name".
6. In the "Target path" field select the directory where you want to save the archive file or the new directory of the project.

   You can set the default directory under "Options &gt; General &gt; Archive settings &gt; Storage location for project archives".
7. Click "Archive".

#### Result

An archive of the project is created. Compressed projects have the file extension ".zap19". The archive file contains the complete project directory. The individual files of compressed archives are additionally reduced to the essential components in order to save space.

At uncompressed projects only a copy of the original project directory is created at the desired storage location.

---

**See also**

[Working with project archives](#working-with-project-archives)
  
[Retrieving compressed project](#retrieving-compressed-project)

### Retrieving compressed project

You extract project archives of the TIA Portal with the "Open" function. This restores the project directory structure including all project files.

#### Requirement

No project is open.

#### Procedure

To extract a project archive, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog opens.
2. Click "Browse".
3. Select the project archive.
4. Click "Open".
5. Select the target directory to which the archived project should be extracted.
6. Click "Select folder".

#### Result

The project is extracted to the selected directory and opened immediately. If you extract a project archive that includes a project from the product version V13 SP1, you may have to upgrade the project. You will automatically receive the corresponding prompt as soon as you open the project. The same rules apply that are described in the chapter "[Using projects created with optional software](#using-projects-created-with-optional-software)". The search index and HMI compile result are automatically restored in the background.

---

**See also**

[Working with project archives](#working-with-project-archives)
  
[Opening projects](#opening-projects)
  
[Using projects created with optional software](#using-projects-created-with-optional-software)
  
[Upgrading projects](#upgrading-projects-1)

## Using reference projects

This section contains information on the following topics:

- [Basics of reference projects](#basics-of-reference-projects)
- [Opening and closing a reference project](#opening-and-closing-a-reference-project)
- [Comparing reference projects](#comparing-reference-projects)

### Basics of reference projects

#### Introduction

In addition to the current project, you have the option to open other projects or local sessions as reference. You can use these reference projects as follows:

- You can drag individual objects from a reference project into the current project and then edit them.
- You can open specific objects, for example, code blocks from a reference project as read-only. But this is not possible for all elements.
- You can use an offline/offline comparison to compare devices of the reference project to devices from the current project.

Note that reference projects are read-only. You cannot change the objects of a reference project. Therefore pending changes, such as name changes for objects, cannot be applied to the referencing object until the project is opened as a normal project. After the changes were applied you can continue using the project as a reference project.

> **Note**
>
> **Stations with security settings**
>
> It is not possible to copy stations with security settings (e.g. VPN) from reference projects. If required, you can open the reference project as a normal project and remove the security settings from the station. If you then use this project as a reference project, you can copy the modified station to your project.

Projects that were created with an older version of the TIA Portal or with a different installation package can also be opened as reference projects. The same compatibility rules apply here as for normal opening of a project from an older version of the TIA Portal. Project archives can also be opened as reference projects.

See also: [Compatibility of projects](#using-projects-created-with-optional-software)

---

**See also**

[Comparing reference projects](#comparing-reference-projects)
  
[Opening and closing a reference project](#opening-and-closing-a-reference-project)
  
[Reference projects](Introduction%20to%20the%20TIA%20Portal.md#reference-projects)

### Opening and closing a reference project

#### Introduction

You can open projects and locally saved sessions as reference projects.

#### Opening a reference project

To open a reference project, follow these steps:

1. In the "View" menu, select the "Reference projects" check box.

   The "Reference projects" palette is displayed in the project tree.
2. In the "Reference projects" palette of the project tree, click on "Open reference project" in the toolbar.

   The "Open reference project" dialog box opens.
3. Navigate to the desired project folder and open the project file or the project archive.

   - TIA Portal V19 projects have the extension ".ap19". Older projects of the TIA Portal have the extension ".ap[version number]".
   - Project archives of the TIA Portal V19 have the extension ".zap19". Older project archives of the TIA Portal have the extension ".zap[version number]".
   - Projects from the Multiuser Engineering context have the extension ".als19".
   - Local sessions from the Multiuser Engineering context have the ending "..._LS.als19".
   - Local sessions from the Exclusive Engineering context have the ending "..._ES.als19".
4. Click "Open".

   The selected project or project archive is opened as a read-only reference project.

#### Closing a reference project

To close a reference project, follow these steps:

1. In the "Reference projects" palette of the project tree, select the reference project you want to close.
2. Click on "Close reference project" in the toolbar.

   The selected reference project is closed.

---

**See also**

[Basics of reference projects](#basics-of-reference-projects)
  
[Comparing reference projects](#comparing-reference-projects)
  
[Reference projects](Introduction%20to%20the%20TIA%20Portal.md#reference-projects)

### Comparing reference projects

#### Introduction

You can compare devices from reference projects with devices from both the current project as well as from the same or another reference project or from a library.

> **Note**
>
> Please note the following:
>
> - You cannot specify actions for the comparison objects, since the reference projects are write-protected.
> - You can perform a detailed comparison for the comparison objects, if the type of comparison object generally allows a detailed comparison.
> - When comparing reference projects, you can always switch between automatic and manual comparison.

#### Procedure

To compare the objects of a reference project to the device data of the current project, follow these steps:

1. In the project tree, select the device whose data you want to compare to the data of a reference project and which allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Open the "Reference projects" palette in the project tree.
4. Select the device of a reference project that you want to compare to the device data from the current project.
5. Drag the device from the reference project into the right drop area of the compare editor.

   You can identify the status of the objects based on the symbols in the status and action area. When you select an object, the object properties and the corresponding object of the assigned device are clearly shown in the property comparison.

   You can drag other devices into the drop areas from the current project, a library or from a reference point at any time to start a new comparison. It does not matter which device you drag into the drop area.
6. If needed, perform a detailed comparison of objects for which this type of comparison is possible.

**Note**

You can start the detailed comparison directly from the reference project for blocks, PLC tags and PLC data types. You can find additional information in the section "Comparing PLC programs".

---

**See also**

[Running a detailed comparison](Editing%20project%20data.md#running-a-detailed-comparison)
  
[Basics of reference projects](#basics-of-reference-projects)
  
[Reference projects](Introduction%20to%20the%20TIA%20Portal.md#reference-projects)
  
[Opening and closing a reference project](#opening-and-closing-a-reference-project)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
