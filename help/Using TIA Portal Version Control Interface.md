---
title: "Using TIA Portal Version Control Interface"
package: ProgVersionControlInterfaceenUS
topics: 30
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using TIA Portal Version Control Interface

This section contains information on the following topics:

- [TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
- [User interface of the Version Control Interface](#user-interface-of-the-version-control-interface)
- [Settings for the Version Control Interface](#settings-for-the-version-control-interface)
- [Creating and configuring a workspace](#creating-and-configuring-a-workspace)
- [Synchronization of the workspace with the project](#synchronization-of-the-workspace-with-the-project)
- [Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)
- [Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
- [Extending workspace functions with Add-Ins](#extending-workspace-functions-with-add-ins)

## TIA Portal Version Control Interface basics

### Introduction

The Version Control Interface of TIA Portal allows you to connect an external version control program to TIA Portal. This is an easy way to exchange your project data with your preferred versioning program. To do so, define one or more directories on your PC as workspaces. The version control program and TIA Portal then both access these workspaces. TIA Portal therefore does not interact directly with the version control program.

Symbols in TIA Portal indicate whether the objects of a workspace are identical with the objects in TIA Portal or whether there are differences. In the event of differences, you can run synchronization between workspace and TIA Portal. TIA Portal objects in the workspace can be versioned over the version management server.

> **Note**
>
> Check the help for your version control program for details of joint work on objects.

### Working with workspaces

A workspace serves as a synchronization point both to TIA Portal and to an external version management program. Once you have defined a new workspace and have connected it in TIA Portal to a directory in the file system, you can export your objects from TIA Portal into this workspace. In your external version control program, place this directory in the file system under version management. The specific procedure depends on the version control program used. In the future, you can synchronize both TIA Portal and the external version control program with this workspace. A workspace is therefore the key element in the TIA Portal Version Control Interface.

You can manage the following object types with an external version control program:

- Organization blocks (OB)
- Function blocks (FB)
- Functions (FC)
- Data blocks (DB)
- PLC data types
- PLC tag tables
- Technology objects

You can also use these as failsafe objects if no password was set for them or if you know the password.

The following objects, however, cannot be synchronized with an external version control program:

- CEM blocks
- Blocks with know-how protection
- Library types
- Fail-safe objects for which a password has been set, and you do not know the password.

The supported objects cannot be edited with the workspace editor. They can only be edited in the relevant editors such as the program editor. Changes to the above object types in the project are automatically applied in the workspace editor. The project area therefore always reflects the latest version of the project.

You have the option of configuring an external comparison program. You can use it in the workspace editor afterwards to determine the differences between an object in the project and a workspace file connected to it.

> **Note**
>
> Note that export and synchronization operations cannot be run for files or directories that have been checked in to an external version control program and are therefore write-protected. Check all files and directories out if you wish to access them via TIA Portal.

### Workspace language

You use the workspace language to specify the language in which the objects are to be exported and imported. The workspace language is independent of the set interface language of the TIA Portal. In a multilingual team, a unified workspace language enables the use of workspaces connected to a common version control program, even if different interface languages are used. The exported system folders are named in the specified workspace language. For example, with the English workspace language, the "Program blocks" folder is exported as "Program blocks" even though the interface language is set to German.

You specify the workspace language when you configure the workspace. After the first selection, however, you can no longer change the workspace language. This is to avoid inconsistencies.

### Connection options

After export of an object from TIA Portal to a workspace, the object is connected to the corresponding file in the workspace. You can connect this workspace file to no other object in the same device of the TIA Portal project. If there are, however, several devices in your project, you can connect the workspace file to other objects in different devices. You can re-use general objects in different places in the project in this way.

But as in the case of multiple use with synchronization, there is the risk of overwriting, you can use "Export" as a synchronization action for only one of the uses. If you have set "Export" for several objects, however, the synchronization action is not carried out and you will receive a message. This ensures that the workspace file is not changed from different objects.

### Installation of the Version Control Interface

You will receive the Version Control Interface when you install "TIA Portal Openness". No separate installation is required.

> **Note**
>
> **Note the following:**
>
> - The software supplied by Siemens does not contain any version control programs. The customer is therefore responsible for the installation, operation, and security of the version control program used.
> - The PC system on which the TIA Portal Version Control Interface is installed is the responsibility of the customer.

---

**See also**

[Notes on use](TIA%20Portal%20Version%20Control%20Interface.md#notes-on-use)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Configuring workspaces](#configuring-workspaces)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Synchronizing objects](#synchronizing-objects)
  
[Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

## User interface of the Version Control Interface

This section contains information on the following topics:

- [Overview of the workspace editor](#overview-of-the-workspace-editor)
- [Overview of the project area](#overview-of-the-project-area)
- [Overview of the workspace area](#overview-of-the-workspace-area)
- [Overview of the unlinked files view](#overview-of-the-unlinked-files-view)

### Overview of the workspace editor

#### Function of the workspace editor

Using the workspace editor, you can configure local workspaces and exchange objects between TIA Portal and a local workspace. The workspace editor also displays the status of the objects, meaning whether there are differences between the object in TIA Portal and the file connected with it in the workspace.

#### Structure of the workspace editor

The following figure shows the two main areas of the Workspace editor:

![Structure of the workspace editor](images/151995812619_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Project area |
| ② | Workspace area |

The view of the workspace area can be switched to show the unlinked objects.

---

**See also**

[Overview of the project area](#overview-of-the-project-area)
  
[Overview of the workspace area](#overview-of-the-workspace-area)
  
[Overview of the unlinked files view](#overview-of-the-unlinked-files-view)

### Overview of the project area

#### Project area

The project area hierarchically displays all elements of the project that you can version with an external version control program over the workspace. Additional information is provided for objects that you have already exported.

The figure below shows the project area:

![Project area](images/151888604683_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Project area |
| ② | Toolbar of the project area |
| ③ | Shortcut menu of the project area |

The table below shows the meaning of the columns in the project area:

| Column | Description |
| --- | --- |
| Name | Object name |
| Status | Comparison status that indicates whether there are differences between the version of the object in the project and the version in the workspace. |
| Action | Action that you can execute to eliminate differences between the version of the object in the project and the version in the workspace. |
| Workspace file | File name under which the object is saved in the workspace. |
| Access path | Relative path of the workspace file to the workspace directory |

#### Toolbar of the project area

You can access the following project area functions over the toolbar:

- Filter project area

  Specifies which objects are to be displayed in the project area.
- Update project area

  Updates the project area view.
- Import changes from workspace

  Sets the synchronization action for those objects whose connected files were changed to "Import". This means that the changes are imported from the workspace to the TIA Portal project during the next synchronization.
- Export changes to workspace

  Sets the synchronization action for those objects that were changed to "Export". This means that the changes are exported from the TIA Portal project during the next synchronization.
- Import all

  Sets the synchronization action for all importable objects to "Import". This means that the changes to the connected files are imported from the workspace to the TIA Portal project during the next synchronization.
- Export all

  Sets the synchronization action for all exportable objects to "Export". This means that the changes to these objects are exported from the TIA Portal project into the workspace during the next synchronization.
- Delete objects without assigned workspace file

  Sets the synchronization action for these objects whose connected files no longer exist to "Delete from the project". This means that these objects are deleted from the TIA Portal project during the next synchronization.
- Discard all actions

  Resets the selected synchronization actions to "No action".
- Synchronize

  Launches synchronization and executes the defined actions.

#### Shortcut menu of the project area

You can execute the following actions using the shortcut menu of the project area:

- Open

  Opens the selected object in its standard editor.
- Delete

  Deletes the selected object.
- Compile

  Compiles the selected object.
- Compare to the workspace file

  Supports the comparison of objects in the project with the linked workspace files. This shortcut menu entry exists only for objects that show differences to their linked workspace file. The entry contains the configured comparison programs and the "Configure" command you use to call the settings.
- Update synchronization status

  Updates the display in the "Status" column. This menu command is only available if the status is "Unknown".
- Synchronization

  Contains the following entries that you can use to specify and execute a variety of synchronization actions:

  - Set action for workspace changes to import

    Sets the synchronization action for the object to "Import". This means that the changes to the connected file are imported from the workspace to the TIA Portal project during the next synchronization.
  - Set action for project changes to export

    Sets the synchronization action for the object to "Export". This means that the changes to the object are exported from the TIA Portal project into the workspace during the next synchronization.
  - Set action for all changes to import

    Sets the synchronization action for all importable objects to "Import". This means that the changes to the connected files are imported from the workspace to the TIA Portal project during the next synchronization.
  - Set action for all changes to export

    Sets the synchronization action for all exportable objects to "Export". This means that the changes to these objects are exported from the TIA Portal project into the workspace during the next synchronization.
  - Reset actions

    Resets the selected synchronization actions to "No action".
  - Execute actions

    Launches synchronization and executes the defined actions.
- Export to workspace

  Exports the selected object to the workspace. If a workspace file is already linked with this object, the file is overwritten. Otherwise, a new workspace file is created.
- Import from the workspace

  Imports the workspace element into the project. If the project already contains an object that is linked to the workspace element, the object is overwritten during the import. Otherwise, a new object is created.
- Go to workspace file

  Shows the workspace file linked to the selected object in the workspace.
- Go to the object in the project tree

  Shows the selected object in the project tree.
- Disconnect

  Separates the connection between the object in the project and the workspace file linked with it.
- Connect object with workspace

  Connects the object in the project with the corresponding workspace file.

#### Display of the comparison status

The comparison status is displayed automatically for all objects that you have exported to a workspace. The comparison is based on checksums.

The table below shows the symbols for the results of a comparison between the objects in the project and the objects in the configured workspace:

| Symbol | Description |
| --- | --- |
| ![Display of the comparison status](images/170577462027_DV_resource.Stream@PNG-de-DE.png) | The object in the project and the connected file in the workspace are identical. |
| ![Display of the comparison status](images/170580362763_DV_resource.Stream@PNG-de-DE.png) | The object in the project and the connected file in the workspace differ. The TIA Portal object has been changed since the last synchronization operation. |
| ![Display of the comparison status](images/170580370699_DV_resource.Stream@PNG-de-DE.png) | The object in the project and the connected file in the workspace differ. The workspace file has been changed since the last synchronization operation. |
| ![Display of the comparison status](images/170582352779_DV_resource.Stream@PNG-de-DE.png) | The object in the project and the connected file in the workspace differ. Both the TIA Portal object and the workspace file have been changed since the last synchronization. |
| ![Display of the comparison status](images/170580898315_DV_resource.Stream@PNG-de-DE.png) | The comparison result is not known. |
| ![Display of the comparison status](images/170547433099_DV_resource.Stream@PNG-de-DE.png) | The linked workspace file does not exist. |

The following table shows the symbols for the comparison results for user-defined folders:

| Symbol | Description |
| --- | --- |
| ![Display of the comparison status](images/170577462027_DV_resource.Stream@PNG-de-DE.png) | All underlying elements are identical to the linked workspace files. |
| ![Display of the comparison status](images/170580890635_DV_resource.Stream@PNG-de-DE.png) | One or more lower-level elements are different to the linked workspace files. |

Many objects in the project structure are contained within other objects. The overlaid objects, referred to below as parent elements, have a large symbol to indicate their status. If one or more lower-level objects are different from their linked workspace files, the large symbol is overlaid with a small symbol indicating the "Different" status. If all lower-level objects are identical to their linked workspace files or there are no lower-level objects, no overlay symbol is displayed.

The following table shows the symbols for the comparison results for parent elements:

| Symbol | Description |
| --- | --- |
| ![Display of the comparison status](images/170547454475_DV_resource.Stream@PNG-de-DE.png) | The compared versions of the parent element in the project and the workspace are identical. However, at least one lower-level object is different from its linked workspace file. |
| ![Display of the comparison status](images/170547463051_DV_resource.Stream@PNG-de-DE.png) | The parent element is not linked to any file in the workspace. All lower-level objects are identical to the linked workspace files. |
| ![Display of the comparison status](images/170547561227_DV_resource.Stream@PNG-de-DE.png) | The parent element is not linked to any file in the workspace. However, at least one lower-level object is different from its linked workspace file. |
| ![Display of the comparison status](images/170547279371_DV_resource.Stream@PNG-de-DE.png) | The compared versions of the parent element in the project and the workspace are different. The TIA Portal object has been changed since the last synchronization operation. In addition, at least one lower-level object is different from its linked workspace file. |
| ![Display of the comparison status](images/170547185419_DV_resource.Stream@PNG-de-DE.png) | The compared versions of the parent element in the project and the workspace are different. The workspace file has been changed since the last synchronization operation. In addition, at least one lower-level object is different from its linked workspace file. |
| ![Display of the comparison status](images/170547023243_DV_resource.Stream@PNG-de-DE.png) | The compared versions of the parent element in the project and the workspace are different. Both the TIA Portal object and the workspace file have been changed since the last synchronization operation. In addition, at least one lower-level object is different from its linked workspace file. |

#### Actions

If there are differences between the objects in the project and the associated files in the workspace, you can tell by the comparison symbols. To eliminate the differences, you need to perform a synchronization. To do this, you can select actions for the objects in the project that are to be executed during synchronization.

The following table shows the possible actions you can select:

| Action | Description |
| --- | --- |
| ![Actions](images/170613155211_DV_resource.Stream@PNG-de-DE.png) | No action is taken during synchronization for the object. |
| ![Actions](images/170615894283_DV_resource.Stream@PNG-de-DE.png) | During synchronization, the selected workspace file is imported into the project. |
| ![Actions](images/170613261707_DV_resource.Stream@PNG-de-DE.png) | During synchronization, the object is exported from the project to the workspace. Specification of the access path is a requirement. |
| ![Actions](images/170613163531_DV_resource.Stream@PNG-de-DE.png) | During synchronization, the object is exported from the project to the workspace. The workspace paths are automatically assigned to the corresponding object paths in the project. Therefore, the access path does not have to be specified. |

---

**See also**

[Overview of the workspace editor](#overview-of-the-workspace-editor)
  
[Overview of the workspace area](#overview-of-the-workspace-area)
  
[Overview of the unlinked files view](#overview-of-the-unlinked-files-view)
  
[Basics of synchronization](#basics-of-synchronization)

### Overview of the workspace area

#### Workspace area

The workspace area displays all files in the directory that you have configured as the workspace. The files and folders are displayed flat without a hierarchy. You can double-click on a folder to open it and display the contents. To display higher-level files and folders, double-click on "..\".

If a file in the workspace directory is incompatible with TIA Portal, it is displayed in the workspace area but cannot be imported.

The figure below shows the workspace area:

![Workspace area](images/151896225547_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Workspace area |
| ② | Toolbar of the workspace area |
| ③ | Shortcut menu of the workspace area |

The table below shows the meaning of the columns in the workspace area:

| Column | Description |
| --- | --- |
| Name | File name |
| Content | Object contained in the file |
| Modified | Date of the last change |
| Size | Size of file in bytes |

You can sort the workspace by a column in ascending or descending order. To do so, click the table header of the column by which you want to sort. This sorts the column in ascending order. Click again on the table header of the column to sort the column in descending order. A third click on the table header of the same column cancels the sorting again.

#### Toolbar of the workspace area

You can access the following workspace area functions over the toolbar:

- Configure workspace

  Opens the dialog for configuring the workspace.
- Show unlinked files

  Opens a separate table view and displays all files that are not yet linked to any object in the project.
- Filter workspace area

  Specifies which objects are to be displayed in the workspace area.
- Refresh workspace

  Updates the workspace area view. You can alternatively press &lt;F5&gt; when the workspace area is in focus.
- Open Windows Explorer

  Opens Windows Explorer and displays the directory that is currently active in the workspace area.

#### Shortcut menu of the workspace area

You can use the shortcut menu command "Open" to display the selected workspace file in Windows Explorer.

---

**See also**

[Overview of the workspace editor](#overview-of-the-workspace-editor)
  
[Overview of the project area](#overview-of-the-project-area)
  
[Overview of the unlinked files view](#overview-of-the-unlinked-files-view)

### Overview of the unlinked files view

#### View for unlinked files

Using the toolbar of the workspace area, you can open a table view that shows all files that have not yet been linked to an object in the TIA Portal. In this view, you can also import the files into the project through a bulk operation.

The following figure shows the view for unlinked files:

![View for unlinked files](images/172615704971_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | View for unlinked files |
| ② | Toolbar of the view for unlinked files |
| ③ | Selection window for the project path |

The following table shows the meaning of the columns in the view for unlinked files:

| Column | Description |  |
| --- | --- | --- |
| Name | File name |  |
| Content | Object contained in the file |  |
| Project path | Automatically assigned project path. You can also select the project path in this column. |  |
| Status | Uses icons to show whether a project path has been selected for the object: |  |
| ![View for unlinked files](images/152249863307_DV_resource.Stream@PNG-de-DE.png) | No project path has been selected. |  |
| ![View for unlinked files](images/152265193483_DV_resource.Stream@PNG-de-DE.png) | The project path exists and can be generated automatically during the import. |  |
| File path | Relative path of the file in the file system |  |
| Modified | Date of the last change |  |
| Size | Size of file in bytes |  |

#### Toolbar of the view for unlinked files

With the toolbar, you can access the following functions:

- Configure workspace

  Opens the dialog for configuring the workspace.
- Show all files

  Shows the normal workspace area.
- Filter workspace area

  Specifies which objects are to be displayed.
- Refresh workspace

  Updates the view.
- Importing selected files into the project

  Imports the selected files to the location in the project that you specified via the project path.

---

**See also**

[Overview of the workspace editor](#overview-of-the-workspace-editor)
  
[Overview of the project area](#overview-of-the-project-area)
  
[Overview of the workspace area](#overview-of-the-workspace-area)

## Settings for the Version Control Interface

This section contains information on the following topics:

- [Overview of the settings for the Version Control Interface](#overview-of-the-settings-for-the-version-control-interface)
- [Setting the export format](#setting-the-export-format)
- [Configure external comparison program](#configure-external-comparison-program)

### Overview of the settings for the Version Control Interface

#### Overview

The following table shows the settings you can make for the Version Control Interface:

| Group | Setting | Description |
| --- | --- | --- |
| File format for the export | Code blocks  Data blocks  PLC data types  PLC tag tables  Technology objects | File formats in which the objects are saved during an export  See also:   [Overview of export formats](#overview-of-export-formats)    [Changing the export format](#changing-the-export-format) |
| SIMATIC ML import options | Disabled project languages are not enabled | When importing a SIMATIC ML file that contains languages deactivated in the project, the corresponding project languages are not activated, and the import will fail. |
| Disabled project languages are enabled | When importing a SIMATIC ML file that contains languages deactivated in the project, the corresponding project languages will be automatically activated. |  |
| Comparison program and parameters | Table of configured comparison programs | You can configure new comparison programs and view the already configured comparison programs using this table.  See also:   [Configuring the external comparison program](#configure-external-comparison-program) |
| Automatic assignment of workspace paths | Automatic assignment or updating of the assignment of the workspace paths to the corresponding object paths in the project through synchronization | New or changed objects are automatically assigned during synchronization  See also:   [Basics of synchronization](#basics-of-synchronization) |

### Setting the export format

This section contains information on the following topics:

- [Overview of export formats](#overview-of-export-formats)
- [Changing the export format](#changing-the-export-format)

#### Overview of export formats

When you export objects from the current project to a workspace, these objects are saved in a specific format. For most objects, the export formats are set and cannot be changed. However, for some object types you can choose from two formats.

##### Overview

The table below shows the formats used for the various different objects when they are exported to a workspace in the TIA Portal Version Control Interface:

| Setting | Description |
| --- | --- |
| Code blocks – LAD | Code blocks in the programming language LAD are always exported as XML files (".xml"). |
| Code blocks – FBD | Code blocks in the programming language FBD are always exported as XML files (".xml"). |
| Code blocks – SCL | Code blocks in the programming language SCL can be exported as XML files (".xml") or as SCL files (".scl"). |
| Code blocks – STL | Code blocks in the programming language STL can be exported as XML files (".xml") or as STL files (".scl"). |
| Code blocks – GRAPH | Code blocks in the programming language GRAPH are always exported as XML files (".xml"). |
| Data blocks | Data blocks can be exported as XML files (".xml") or DB files (".db"). |
| Safety data blocks (F-DBs) | F-DBs are always exported as XML files (".xml"). |
| PLC data types | PLC data types can be exported as XML files (".xml") or UDT files (".udt"). |
| F-compliant PLC data types (UDT) | F-compliant PLC data types are always exported as XML files (".xml"). |
| PLC tag tables | PLC tag tables are always exported as XML files (".xml"). |
| Technology objects | Technology objects are always exported as XML files (".xml"). |

> **Note**
>
> **Behavior when exporting objects in the Version Control Interface (VCI)**
>
> The SIMATIC ML files exported with Version Control Interface (VCI) no longer show default values. If a change was made to a default value, an entry is written to the exported XML file. This can lead to changes in the behavior when comparing the existing files with the objects in VCI. Run the export again to get the new export format.

---

**See also**

[Changing the export format](#changing-the-export-format)
  
[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Configuring workspaces](#configuring-workspaces)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Synchronizing objects](#synchronizing-objects)
  
[Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

#### Changing the export format

You can change the export format for the following object types:

- SCL blocks
- STL blocks
- Data blocks
- PLC data types

Please note that you can also re-import only the set formats.

##### Procedure

Proceed as follows to change the export format:

1. Select the "Settings" command from the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "Version Control Interface" group in the area navigation.
3. Change the export format for the desired object type.

##### Result

The change is applied and does not have to be saved separately. From now on, the objects are exported in the selected format. Objects that have already been exported retain their current format.

---

**See also**

[Overview of export formats](#overview-of-export-formats)

### Configure external comparison program

You can configure up to 100 external comparison programs in TIA Portal to use them in the workspace editor for a detailed comparison of the objects in the project area and the associated workspace files. You can assign specific file types to a comparison program or use it for all file types. You can also transfer the following parameters with the comparison program:

- $(Project.TempExportFile.Path)

  Path to the temporary exported file based on the object in the project
- $(Project.TempExportFile.Name)

  Name of the temporarily exported file based on the object in the project
- $(Project.LinkedObject.Path)

  Path to the object contained in the project
- $(Project.LinkedObject.Name)

  Name of the object contained in the project
- $(Workspace.RootPath)

  Root directory of the workspace
- $(Workspace.LinkedFile.Path)

  Path of the workspace file
- $(Workspace.LinkedFile.Name)

  Name of the workspace file
- $(Workspace.LinkedFile.RelativePath)

  Relative path to the workspace file

These parameters are used as placeholders. When starting the comparison program, the placeholder is replaced with the respective value by TIA Portal and transferred to the comparison program. To determine the parameters that are supported by the comparison program, see the documentation for your comparison program.

The configured comparison programs can be accessed in the workspace editor with a shortcut menu. The sequence of the displayed comparison programs in the shortcut menu corresponds to the sequence that you specified in the list of comparison programs.

You can edit or delete a configured comparison program at any time. If you have configured multiple comparison programs, you can also specify the sequence in the table.

In Siemens Industry Online Support under the following link, you can find an application which enables the graphical comparison of blocks in the languages LAD and FBD. This application can be configured as an external comparison program in TIA Portal in the settings for the Version Control Interface. Link to the application: [https://support.industry.siemens.com/cs/document/109797235](https://support.industry.siemens.com/cs/de/en/view/109797235)

#### Configuring the new comparison program

To configure an external comparison program, follow these steps:

1. Open the configuration dialog for the comparison programs:

   - To do so, select the "Settings &gt; Version control interface &gt; Compare" command in the "Options" menu.
   - Alternatively, you can also select an object in the workspace editor that differs from its connected workspace file, and click on the "Configure" command in the shortcut menu of the comparison.

   The list of comparison programs is displayed in the working area.
2. Double-click on "Add new" or select the "Add new" command from the shortcut menu.

   The "Add new comparison program" dialog opens.
3. From the "File extension" drop-down list, select the file type that is to be edited with this comparison program. Or leave the settings set to "All files".
4. Enter a name for the comparison program in the "Name" field. This name is displayed in the shortcut menu in the workspace editor. You should therefore select a meaningful name.
5. In the "Program path" field, enter the path to the executable file of the comparison program or click "..." to select the executable file from the file system. Note that you can only select files with the extension "*.exe", "*.com", "*.pif", "*.bat" or "*.cmd".
6. In the "Parameter" field, enter the parameters that are to be handed over to the comparison program at the start. The two parameters "$(Project.TempExportFile.Path)" and "$(Workspace.LinkedFile.Path)" already exist and are sufficient in most cases. To add additional parameters, click on the "+" button at the end of the field. A shortcut menu opens in which you can select the desired parameters. Alternatively, you can enter the parameters manually in the field or remove them from the field.
7. Click "Add" to add the comparison program to the list.

#### Editing configured comparison program

To change the settings of a comparison program that has already been configured, follow these steps:

1. Open the configuration dialog for the comparison programs:

   - To do so, select the "Settings &gt; Version control interface &gt; Compare" command in the "Options" menu.
   - Alternatively, you can also select an object in the workspace editor that differs from its connected workspace file, and click on the "Configure" command in the shortcut menu.
2. The list of comparison programs is displayed in the working area.
3. Select the comparison program whose settings you want to change from the list.
4. Click on the "Change selected comparison program" button at the bottom or select the "Edit" command from the shortcut menu.

   The "Edit comparison program" dialog opens.
5. Change the configuration to meet your requirements.
6. Click "Change".

#### Specify the sequence in the table.

To change the sequence of comparison programs in the list and thus also in the workspace editor in the "Compare to the workspace file" shortcut menu, follow these steps:

1. Open the configuration dialog for the comparison programs:

   - To do so, select the "Settings &gt; Version control interface &gt; Compare" command in the "Options" menu.
   - Alternatively, you can also select an object in the workspace editor that differs from its connected workspace file, and click on the "Configure" command in the shortcut menu.
2. The list of comparison programs is displayed in the working area.
3. Select the comparison program whose position you want to change.
4. Click "Up" to move the comparison program up in the list or select the "Up" command from the shortcut menu.
5. Click "Down" to move the comparison program down in the list or select the "Down" command from the shortcut menu.
6. Repeat this for all applications for which you want to change the sequence.

#### Delete configured comparison program

To delete a configured comparison program, follow these steps:

1. Open the configuration dialog for the comparison programs:

   - To do so, select the "Settings &gt; Version control interface &gt; Compare" command in the "Options" menu.
   - Alternatively, you can also select an object in the workspace editor that differs from its connected workspace file, and click on the "Configure" command in the shortcut menu.
2. The list of comparison programs is displayed in the working area.
3. Select the comparison program that you want to delete from the list.
4. Click on the "Delete selected comparison program" button at the bottom or select the "Delete" command from the shortcut menu.

   The selected comparison program is deleted from the list.

---

**See also**

[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configuring workspaces](#configuring-workspaces)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Synchronizing objects](#synchronizing-objects)
  
[Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

## Creating and configuring a workspace

This section contains information on the following topics:

- [Creating workspaces](#creating-workspaces)
- [Overview of the configuration options](#overview-of-the-configuration-options)
- [Basics of path offset](#basics-of-path-offset)
- [Configuring workspaces](#configuring-workspaces)

### Creating workspaces

To synchronize objects from TIA Portal with a version control program, you need at least one local workspace over which TIA Portal can synchronize these objects. You can also create multiple workspaces, but the name of each workspace must be unique in the project. You can change the name at any time.

#### Procedure

To create a new workspace, follow these steps:

1. Open the "Version control interface" folder in the project tree.
2. Double-click the "Add new workspace" command.

   A new workspace is created with the standard name.
3. Select the new workspace.
4. Select the "Rename" command in the shortcut menu.
5. Enter a unique name for the workspace.

---

**See also**

[Overview of the configuration options](#overview-of-the-configuration-options)
  
[Configuring workspaces](#configuring-workspaces)

### Overview of the configuration options

#### Overview

To work with the new workspace, you need to connect it to the version control program. You can also make additional settings that improve the cooperation of the version control program with TIA Portal.

The following table shows the configuration options for your workspace:

| Configuration | Description |
| --- | --- |
| Workspace path | You use the workspace path to configure the local directory that you want to use for version control.   If you want to use the Version Control Interface, this configuration is required. |
| Version Control Add-In | You can configure an Add-In for the workspace to run each time an export occurs. To be able to select the Add-In in the "Import Add-In" drop-down list, it must be activated in the "Add-Ins" task card.  This configuration is optional. |
| Import Add-In | In addition, you can configure your own import Add-Ins for a workspace. This is required for Add-Ins that extend the shortcut menu of the workspace area or specific import workflows. To be able to select the Add-In in the "Import Add-In" drop-down list, it must be activated in the "Add-Ins" task card.  This configuration is optional. |
| Path offset | You can use the path offset to specify the point in the project structure as of which synchronization with the workspace should take place. All other areas are not taken into account.   See also: [Basics of the path offset](#basics-of-path-offset)  This configuration is optional. |
| Workspace language | The workspace language defines in which language the system folders are exported and imported. This means that workspaces can also be used in a multilingual team.   The workspace language is selected the first time the workspace is created and cannot be changed afterwards, which avoids inconsistencies. Therefore, if you connect an existing workspace via the version control program, the workspace language is already set and the drop-down list is read-only.  To make collaboration in the team work, the TIA Portal creates the ".vci" folder and saves it in the local workspace path. Be sure to check this folder into your version control program as well so that it is available to all team members. |

---

**See also**

[Creating workspaces](#creating-workspaces)
  
[Configuring workspaces](#configuring-workspaces)

### Basics of path offset

#### Introduction

To work with the Version Control Interface in TIA Portal, the objects in the project must be exported to the workspace. The export creates files in the workspace, which are then transferred to the version control program. In addition, files may be stored in the workspace via the version control program in which new objects are contained. This must be imported into the project. To perform the export or import, you can exchange the objects and files using drag-and-drop operation.

However, you can also use the following functions of the TIA Portal for an easier export and import:

- Automatic assignment

  In the settings you can enable the option that the paths of the objects in the project are used as paths for the files in the workspace. This automatically sets the "Export (automatically assigned)" action for new objects and for objects whose name or path has been changed. For new objects, the corresponding files are then created in the workspace during the synchronization. The assigned files are adjusted for the changed objects.
- Import function in the view of the unassigned files

  You can open the view of unassigned files in the workspace. In this view you can see all the files that exist in the defined workspace but are not yet assigned to any objects in the project. TIA Portal tries to preset the possible project path for these files. If the project paths are correct, you can import all files with one click.

In order for the TIA Portal to be able to preset the paths for export and import for these functions, it is necessary that the structures in the project and in the workspace match. If this is not the case, TIA Portal cannot recognize the folders or files to be exported or imported. However, you can define a path offset to also work with different structures.

#### Path offset

If your workspace structure is different from the project structure, you can specify a path offset when configuring the workspace. The path offset is a part of the project path that is added to the elements of your workspace. If TIA Portal then presets the paths, the path offset is taken into account as follows:

- Export: TIA Portal subtracts the path offset from the project path of the object.
- Import: TIA Portal adds the path offset to the path of the workspace file.

In addition, the project is filtered according to the path offset. If you have, for example, multiple CPUs in your project, you only see the CPU in the project area that you have specified in the path offset. This makes the project area clearer.

An example of a path offset would be:

"PLC_1500\Software Units\Unit_1"

For changes in the project that affect the configured path offset, you must manually adapt the path offset to it.

See also: [Configuring workspaces](#configuring-workspaces)

### Configuring workspaces

To synchronize objects from TIA Portal with a version control program, you need a local directory that is shared between the TIA Portal and the version control program. You must configure this local directory in the workspace. You can also make other optional settings. You can change the settings again at any time, with the exception of the workspace language.

See also:

[Overview of the configuration options](#overview-of-the-configuration-options)

#### Requirement

- A project is open.
- A workspace has been created.

#### Configuring the workspace

Proceed as follows to configure a workspace:

1. Open the "Version control interface" folder in the project tree.
2. Double-click the workspace that you want to configure.

   The workspace editor opens.
3. Click "Configure workspace" in the workspace area toolbar.

   The "Configure workspace" dialog opens.
4. Enter the local directory that you want to subject to version control. You can alternatively select the directory using the "Search" function.
5. If you want to use specific Add-Ins for the export, select the corresponding Add-In from the "Version Control Add-In" drop-down list. Note that this is only possible if the Add-In was previously enabled in the "Add-Ins" task card.
6. If you want to use a specific Add-In for the import, select the corresponding Add-In from the "Import Add-In" drop-down list. Note that this is only possible if the Add-In was previously enabled in the "Add-Ins" task card.
7. If you want to specify a path offset, click the "..." button in the "Path offset" field. Then select the point in the project structure as of which synchronization with the workspace is to take place.
8. Only possible for the first configuration: If you want to change the workspace language, select the desired language in the "Workspace language" drop-down list.
9. Click "OK".

#### Terminating the connection to the configured workspace

Proceed as follows to terminate the connection to a configured workspace:

1. Open the "Version control interface" folder in the project tree.
2. Double-click the workspace for which you want to disconnect.

   The workspace editor opens.
3. Click "Configure workspace" in the workspace area toolbar.

   The "Configure workspace" dialog opens.
4. Remove the specified path.
5. Click "OK".

   The connection to the workspace is terminated and you can configure a new workspace if required. You might subsequently need to edit the workspace information for the objects if you configure a new workspace.

   See also: [Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

#### Removing configured Add-Ins

To remove a configured Add-In again for a workspace or the import, follow these steps:

1. Open the "Version control interface" folder in the project tree.
2. Double-click the workspace for which you want to remove an Add-In.

   The workspace editor opens.
3. Click "Configure workspace" in the workspace area toolbar.

   The "Configure workspace" dialog opens.
4. Select the top entry either in the "Version Control Add-In" drop-down list or in the "Import Add-In" drop-down list. This is an empty line.
5. Click "OK".

---

**See also**

[Creating workspaces](#creating-workspaces)
  
[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Synchronizing objects](#synchronizing-objects)

## Synchronization of the workspace with the project

This section contains information on the following topics:

- [Basics of synchronization](#basics-of-synchronization)
- [Exporting and importing objects](#exporting-and-importing-objects)
- [Connecting objects with workspace files](#connecting-objects-with-workspace-files)
- [Synchronizing objects](#synchronizing-objects)

### Basics of synchronization

#### Introduction

TIA Portal objects must be exported to a workspace before they can be managed by a version control program. You can either perform the export manually or use the synchronization. You can also use synchronization at any time to keep your workspace consistent with the project. Synchronization or export or import is required in the following cases:

- An object in the project has been changed.
- A file in the workspace has been changed.
- A new object has been created in the project.
- A new file has been added in the workspace.
- A file has been removed from the workspace.

You can see whether the workspace is still in sync with the project by the comparison symbols. You can also open the view for unlinked files. In it, you can see if there are files in the workspace that are not yet linked to any object in the project.

For a manual export or import, you can select the corresponding objects or files and drag-and-drop them into the project or workspace. During synchronization, you can select specific actions to be executed either for individual objects or for all objects.

Note that an object cannot be exported under the following circumstances:

- The object is not compiled.
- The object is a library type.
- The object is a CEM block.
- The object is a fail-safe object for which a password that is unknown to you was set.
- The object is know-how protected.
- The object is a system block or a PLC data type generated by the system.
- The target file for the object already exists and is connected with another object.
- The file name of the object contains invalid characters.
- The full name of the object or the path is too long.
- There is not enough free memory space available.

#### File formats

The objects are exported from the TIA Portal to the workspace in different file formats depending on their type and programming language:

- Code blocks (OBs, FBs and FCs) are always exported as XML files in the programming languages LAD, FBD and GRAPH. For STL and SCL code blocks, you can choose either XML or the block-specific formats as export format.
- Safety data blocks (F-DBs) are always exported as XML files. In the case of all other data blocks you can choose whether data blocks are to be exported as XML or DB files.
- F-compliant PLC data types (UDT) are always exported as XML files. For all other PLC data types you can choose whether they are to be exported as XML or UDT files.
- PLC tag tables are always exported as XML files.
- Technology objects are always exported as XML files.

If you export objects with a namespace from Software Units, the file name of the export file also gets the namespace. For example, the "Block" block with the namespace "BlockNamespace" is exported to the file "BlockNamespace.Block.xml".

#### Automatic assignment

In the TIA Portal settings, you can activate the option for automatic assignment of workspace paths. As a result, the TIA Portal automatically tries to assign objects in the project to files in the workspace. This applies both to the first export and to changes made to the objects in the project, such as by renaming or moving them. As far as possible, TIA Portal sets the action to "Export (automatically assigned)". But you can also select this action yourself. Conversely, you can also select other actions for objects for which the TIA Portal has set automatic assignment.

You can recognize elements to which this setting is applied by the ![Automatic assignment](images/170613163531_DV_resource.Stream@PNG-de-DE.png) symbol in the project area in the "Action" column. If this action is set for the synchronization, it has the following effects:

- The corresponding workspace file is created automatically for new objects in the project.
- For existing objects with a link to the workspace, changes to the name and path are automatically propagated to the workspace file.

If objects in the project are not connected with any workspace files, you can also connect these objects with workspaces files by means of a context menu command. Prerequisite is that corresponding workspace files exist for the objects that you want to connect. This means that the workspace files have the same name and are located at the same position as the objects in the project.

See also: [Connecting objects with workspace files](#connecting-objects-with-workspace-files)

#### Project languages

In the case of SIMATIC ML files it is possible that they contain languages that are not enabled as a project language. Importing is not possible for these files. However, you can activate the option "Enable inactive project languages during import" in the settings under "Version Control Interface &gt; Import". As a result such files can then also be imported.

For more information on the SIMATIC ML files, refer to the documentation on TIA Portal Openness.

---

**See also**

[Exporting and importing objects](#exporting-and-importing-objects)
  
[Synchronizing objects](#synchronizing-objects)

### Exporting and importing objects

#### Requirement

The workspace editor is open.

#### Exporting objects from TIA Portal to a workspace

Proceed as follows to export objects from TIA Portal to a workspace:

1. Check the names of the objects you want to export to ensure that they comply with the Windows file system naming conventions.
2. Check whether the target medium has enough free memory space.
3. In the project area, select the objects that you want to export. You can also select folders, groups, software units and entire devices as export objects. These will remain available in the workspace. When selecting more than one object, note that the objects that you want to export must be sibling elements in the same folder or in the same group. This means you cannot export a PLC tag table together with a block.
4. Drag the objects to the workspace area. Dragging the objects to the "...\" symbol exports them to the higher-level directory.

   If the selection contains objects that have not been compiled, the "Compiling required" dialog is displayed. To export these objects, click "Yes". These objects are then compiled. If you click "No", only the objects that have already been compiled are exported.
5. If the workspace area already contains objects with the same name, the "Export" dialog opens. Select the required option and confirm with "OK".

   The export is executed and a message appears when it is complete. If the export was successful, the exported objects are added to the workspace area. If the export could not be executed or not in full, an error message is output. To view the corresponding entry in the log, click the link in the message window.

   When you undo the export, the newly exported objects are not removed from the workspace. Only the connection between the last object exported is separated in the TIA Portal project and in the workspace.

#### Importing objects from a workspace to TIA Portal

Proceed as follows to import objects from a workspace to TIA Portal:

1. In the workspace area, select the objects that you want to import. You can also select folders as import objects. The folders remain available in the project area. When selecting more than one object, note that the objects that you want to import must all be sibling elements in the same folder.
2. Drag the objects to a valid position in the project area.
3. If the project area already contains objects with the same name, the "Import" dialog opens. Select the required option and confirm with "OK".

   The import is executed and a message appears when it is complete. If the import was successful, the imported objects are added to the project area. If the import could not be executed or not in full, an error message is output. To view the corresponding entry in the log, click the link in the message window.

You can also export objects from the view for unlinked files. The advantage of this is that the TIA Portal makes suggestions for the project path if the workspace structure does not differ too significantly from the project structure.

To import objects from the view for unassigned files into the TIA Portal, follow these steps:

1. In the workspace area, click on "Show unlinked files" in the toolbar.

   The view is switched and the additional columns "Project path", "Status" and "File path" are displayed. If possible, the TIA Portal makes suggestions for the project paths. The red error symbol in the "Status" column indicates files without a project path.
2. Check the project paths. If all project paths are present and correct, continue with Step 6.
3. To define or change the project path for a file, click the "..." button in the corresponding cell in the "Project path" column.

   A window containing the project structure opens.
4. Navigate to the desired folder and confirm the selection.
5. Repeat steps 3 and 4 for all files for which you want to define or change the project path.
6. To import the files, click on "Import all" in the toolbar.

---

**See also**

[Basics of synchronization](#basics-of-synchronization)
  
[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Configuring workspaces](#configuring-workspaces)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Synchronizing objects](#synchronizing-objects)
  
[Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

### Connecting objects with workspace files

#### Requirement

- Corresponding workspace files exist for the individual objects that you want to connect. This means that the workspace files have the same name and are located at the same position as the objects in the project.
- The objects in the project are not connected with any other workspace files.

#### Procedure

To connect one or more objects of the project with workspace files, follow these steps:

1. Select the objects in the project area that you want to connect with workspace files.

   You can also select folders, groups, software units and entire devices. In this case all the subordinate objects are connected with the corresponding workspaces files, in as far as this is possible. When selecting more than one object, note that the objects must be sibling elements in the same folder or in the same group.
2. Select the "Connect object with workspace" command in the context menu.

#### Result

The following data are displayed for the connected objects:

- Status
- Workspace file
- Access path

---

**See also**

[Basics of synchronization](#basics-of-synchronization)

### Synchronizing objects

If there are differences between the objects in the project and the associated files in the workspace, you can tell by the comparison symbols. To eliminate the differences, you need to perform a synchronization. To do this, you can select actions for the objects in the project that are to be executed during synchronization.

You have the following options when selecting actions:

- Specify individual actions:

  For each individual object, you can specify whether it is to be exported from the TIA Portal to the workspace or imported from the workspace to the TIA Portal. You can also specify that no actions are to be run for a specific object during synchronization.

  > **Note**
  >
  > Use the "Discard all actions" button in the project area toolbar to set the actions for all objects to "No action" if required.
- Specify same action for all objects:

  If you want to synchronize multiple objects, you can use the toolbar to specify one action for all objects. The selected action is then applied to all objects.

If you have activated the option for automatic assignment of workspace paths in the Version Control Interface settings, the action "Export (automatically assigned)" ![Figure](images/158509912203_DV_resource.Stream@PNG-de-DE.png) is preset for the following objects:

- New objects
- Existing objects with a link to the workspace for which changes have been made to the name or path.

You can change the action if required.

> **Note**
>
> Note the following:
>
> - You can only specify actions for objects whose TIA Portal project and workspace versions differ.
> - If you have connected a workspace file with several objects in different devices, you can only use "Export" as a synchronization action on one of the objects.

#### Requirement

The workspace editor is open.

#### Procedure

Proceed as follows to synchronize objects whose versions differ:

1. For each object, go to the "Action" column and from the drop-down list select the action that is to be executed for that object during synchronization, or click on one of the following buttons in the toolbar:

   - Import changes from workspace
   - Export changes to workspace
   - Import all
   - Export all
2. Click "Synchronize" in the toolbar.

#### Result

For objects with different versions, the selected actions are executed and you will receive a message once they are completed. If synchronization was successfully executed, the comparison status for these objects then indicates that the TIA Portal project and workspace versions are identical. If the synchronization could not be executed, an error message is output. Click on the link in the message window to display the corresponding entry in the log.

---

**See also**

[Basics of synchronization](#basics-of-synchronization)
  
[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Configuring workspaces](#configuring-workspaces)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

## Editing the workspace information of an object

If the name or the path of a file that is synchronized with the TIA Portal over the workspace is changed, the TIA Portal is then unable to find that file. In the "Workspace file" column in the project area, a message is output for the object that was linked to the modified file. You can change the workspace file or the access path manually so that the TIA Portal is once again able to synchronize the object with the workspace file.

You can also remove a TIA Portal object connection to a workspace file. The object is then no longer synchronized with the workspace.

### Requirement

The workspace editor is open.

### Changing the workspace file

Proceed as follows to change the workspace file:

1. Select the object for which you want to change the workspace file.
2. Click on the "Workspace file" field.
3. Enter the new file name or click "..." to select the file from the file system.

### Change the access path

To change the access path, follow these steps:

1. Select the object for which you want to change the access path.
2. Click on the "Access path" field.
3. Enter the new relative path.

### Removing an object connection to a workspace file

Proceed as follows to remove an object connection to a workspace file:

1. Double-click on the "Access path" field of the object whose connection to a workspace file you want to remove. You can alternatively select the field and press &lt;F2&gt;.
2. Remove the path.

   The access path and the workspace file for the object are deleted. The status of synchronization and the drop-down list for actions are also removed. The TIA Portal object is now once again independent of the workspace.

---

**See also**

[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Configuring workspaces](#configuring-workspaces)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Comparing objects in the project with the associated workspace files](#comparing-objects-in-the-project-with-the-associated-workspace-files)
  
[Synchronizing objects](#synchronizing-objects)

## Comparing objects in the project with the associated workspace files

Symbols in the TIA Portal indicate whether the objects of a workspace are identical with the objects in the TIA Portal or whether there are differences. Folders and other container elements show the status of the lower-level elements.

If objects in the project differ from the workspace files connected to them, you can run a comparison with an external comparison program. This allows you to determine the differences. The workspace editor contains an entry in the shortcut menu of objects that are different with which you can start the comparison. This shortcut menu entry depends on your configuration of the comparison programs. Only comparison programs that you have configured for the respective file type are offered. If your selection contains different file types, the comparison programs that you have selected for the "All files" setting are offered. The sequence of the comparison programs in the shortcut menu corresponds to the sequence in the list of comparison programs in the settings.

### Requirement

- You have configured at least one external comparison program for the required file extension.

  See also: [Configuring the external comparison program](#configure-external-comparison-program)
- SIMATIC Safety: You are logged into the Safety Administration editor.
- The workspace editor is open.

### Procedure

To compare objects in the project with the associated workspace files, follow these steps:

1. In the project area of the workspace editor, select the objects that you want to compare. You can select multiple files as well as folders.
2. Click the "Compare to the workspace file &gt;" command from the shortcut menu and select the submenu of the desired comparison program.
3. If your selection contains objects that have not been compiled yet, you will receive the message "Compiling required". To run the comparison, click "Yes".

   The configured comparison program opens. Depending on your selection and the comparison program, the comparison results are displayed in multiple tabs or instances of the comparison program.

---

**See also**

[TIA Portal Version Control Interface basics](#tia-portal-version-control-interface-basics)
  
[Overview of export formats](#overview-of-export-formats)
  
[Configure external comparison program](#configure-external-comparison-program)
  
[Configuring workspaces](#configuring-workspaces)
  
[Exporting and importing objects](#exporting-and-importing-objects)
  
[Synchronizing objects](#synchronizing-objects)
  
[Editing the workspace information of an object](#editing-the-workspace-information-of-an-object)

## Extending workspace functions with Add-Ins

This section contains information on the following topics:

- [Basics of Add-Ins in the workspace](#basics-of-add-ins-in-the-workspace)
- [Programming general shortcut menus](#programming-general-shortcut-menus)
- [Programming shortcut menus for Repository Add-Ins](#programming-shortcut-menus-for-repository-add-ins)
- [Expanding workflows](#expanding-workflows)

### Basics of Add-Ins in the workspace

#### Add-Ins in the TIA Portal

You can use C# and the TIA Portal Openness API to program your own Add-Ins for TIA Portal in order to extend its functionality. In certain areas of TIA Portal, you can add your functions to the existing shortcut menus. The following basic steps are required to create the Add-In:

1. Create the Add-In using C# and the TIA Portal Openness API.
2. Convert the dll file to an addin file using the provided software and a configuration file.
3. Copy the addin file to the TIA Portal installation directory.
4. Enable the Add-In in the "Add-Ins" task card.

You can find more information about each step and programming in the following two sections:

- [Extending TIA Portal functions with add-ins](Introduction%20to%20the%20TIA%20Portal.md#extending-tia-portal-functions-with-add-ins)
- Openness: [Functions for Version Control Interface (VCI)](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#functions-for-version-control-interface)

#### Add-Ins in the workspace editor

You can use Add-Ins as follows in the workspace editor of the version control interface:

- You can add general entries to the shortcut menu in the workspace area.
- You can add entries specific to a Repository Add-In to the shortcut menu in the workspace area.
- You can expand the workflows for drag-and-drop and synchronization in the workspace with additional functions.

Basically, you create these Add-Ins in the same way as other Add-Ins. This means that all the above steps must also be performed for the Add-Ins in the workspace editor. However, note the following differences:

- Add-Ins for workflows and Repository Add-Ins must also be configured for the workspace.

  See also: [Create and configure workspaces](#configuring-workspaces)
- Additional namespaces and the objects contained in them are used in the programming.

#### TIA Portal Add-In Development Tools

You can either create the C# project and the required classes and methods manually or use the TIA Portal Add-In Development Tools. The TIA Portal Add-In Development Tools make it easier for you to create the C# project and contain the following templates for the Version Control Interface:

- TIA Portal VCI Editor Add-In

  This template allows you to program Add-Ins that extend the shortcut menu of the workspace area with your own entries.
- TIA Portal VCI Import Add-In

  This template allows you to program Add-Ins with the following functionality:

  - Creation of new entries in the shortcut menu of the workspace area with specific import functions for files and directories
  - Enhancement of the import workflows for drag-and-drop operation and synchronization from the workspace area into the project

  The extensions of the "TIA Portal VCI Import Add-In" can only be used if you have selected the Add-In in the workspace editor as import Add-In.
- TIA Portal VCI Repository Export Add-In

  This template allows you to program Add-Ins with the following functionality:

  - Creation of new entries in the shortcut menu of the workspace area with specific repository functions for files and directories
  - Enhancement of the export workflows for drag-and-drop operation and synchronization from the project into the workspace area

  The extensions of the "TIA Portal VCI Repository Export Add-In" can only be used if you have selected the Add-In in the workspace editor as Version Control Add-In.

Use the TIA Portal Add-In Development Tools in Microsoft Visual Studio 2019 or 2022 or in Visual Studio Code.

You can find more information about the TIA Portal Add-In Development Tools and the required installation files on the DVD 2 of the TIA Portal Installation Package under "DVD &gt; Support &gt; TIA_Portal_Add-In_Tools &gt; Development".

---

**See also**

[Programming general shortcut menus](#programming-general-shortcut-menus)
  
[Programming shortcut menus for Repository Add-Ins](#programming-shortcut-menus-for-repository-add-ins)

### Programming general shortcut menus

The following two steps are required for programming general shortcut menus:

- Programming the View Provider "VciWorkspaceViewAddInProvider" and "VciEditorAddInProvider"
- Programming the shortcut menu

#### Requirement

A C# project exists for creating a class library.

#### Program View Provider "VciWorkspaceViewAddInProvider"

To program the View Provider"VciWorkspaceAddInProvider", proceed as follows:

1. Create a new class in your project and give it a meaningful name, e.g. "VciWorkspaceProvider.cs".
2. Add the following two using directives to the class:

   - `using Siemens.Engineering.AddIn.Menu;`
   - `using Siemens.Engineering.AddIn.VersionControl;`
3. Declare your class as "public" and make the class a subclass of "VciWorkspaceViewAddInProvider":

   `public class VciWorkspaceProvider : VciWorkspaceViewAddInProvider`
4. Enter "override" in the new class as text and select the entry "GetContextMenuAddIns" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
5. Remove the row "return base.GetContextMenuAddIns();" and enter the following code instead:

   `yield return new` 
   `<Your_Shortcut_Menu_Class_Name>("<Text of shortcut menu>");`

   If you program your shortcut menu in an "AddInContextMenu" class and the entry in the shortcut menu is to be called "My AddIn", the line would look as follows:

   `yield return new AddInContextMenu("My AddIn");`

   Specifying the text for the shortcut menu is optional and can also be specified when programming the shortcut menu.

#### Program View Provider "VciEditorAddInProvider"

To program the View Provider "VciEditorAddInProvider", proceed as follows:

1. Create a new class in your project and give it a meaningful name, e.g. "VciEditorProvider.cs".
2. Add the following using directive to the class:

   `using Siemens.Engineering.AddIn.VersionControl;`
3. Declare your class as "public" and make the class a subclass of "VciEditorAddInProvider":

   `public class` VciEditorProvider `: VciEditorAddInProvider`
4. Enter "override" in the new class as text and select the entry "GetVciWorkspaceViewAddInProvider" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
5. Remove the row "return base.GetVciWorkspaceViewAddInProvider();" and enter the following code instead:

   `return new GenericContextMenuAddInProvider();`

#### Programming the shortcut menu

To program a new shortcut menu, follow these steps:

1. Create a new class in your project and give it a meaningful name.
2. Add the following two using directives to the class:

   - using Siemens.Engineering.AddIn.Menu;
   - using Siemens.Engineering.AddIn.VersionControl;
3. If necessary, add additional using directives.
4. Declare your class as "public" and make the class a subclass of "ContextMenuAddIn":

   `public class GenericContextMenuAddIn : ContextMenuAddIn`
5. Add the following method to your class:

   `public GenericContextMenuAddIn(string displayName) : base(displayedAddinName)`

   `{`

   `}`

   Use the string variable "displayedAddinName" to hand over the title for your Add-In to the designer of the basic class. You can rename "displayedAddinName" as you like.

   You can also specify the title for the Add-In in a constant within the class and then use this constant. Then the code looks like this:

   `private const string s_DisplayName = "Generic Context Menu AddIn";`

   `public GenericContextMenuAddIn() : base(s_DisplayName)`

   `{`

   `}`
6. Add the following method to your class:

   `protected override void BuildContextMenuItems(ContextMenuAddInRoot addInRootSubmenu)`

   `{`

   `}`
7. Add the buttons for your shortcut menu to this method:

   `addInRootSubmenu.Items.AddActionItem<WorkspaceFile>("<Text des Kontextmenüeintrags>", Entry1_OnClick);`
8. Repeat step 7 for all other desired entries of the shortcut menu. Make sure that you call a separate method for each of your entries when using the OnClick method.
9. Create the executable code for your buttons either directly in the OnClick methods or create additional classes that you call in the OnClick methods.

#### Complete example of programming a general shortcut menu

View Provider "VciWorkspaceViewAddInProvider":

using Siemens.Engineering.AddIn.Menu;

using Siemens.Engineering.AddIn.VersionControl;

namespace VciWorkspaceContextMenu

{

public class VciWorkspaceProvider : VciWorkspaceViewAddInProvider

{

public override IEnumerable&lt;ContextMenuAddIn&gt; GetContextMenuAddIns()

{

yield return new GenericContextMenuAddIn();

}

}

}

View Provider "VciEditorAddInProvider":

using Siemens.Engineering.AddIn.VersionControl;

namespace VciWorkspaceContextMenu

{

public class VciEditorProvider : VciEditorAddInProvider

{

public override VciWorkspaceViewAddInProvider GetVciWorkspaceViewAddInProvider()

{

return new GenericContextMenuAddInProvider();

}

}

}

Shortcut menu:

using Siemens.Engineering.AddIn.Menu;

using Siemens.Engineering.AddIn.VersionControl;

namespace VciWorkspaceContextMenu

{

public class GenericContextMenuAddIn : ContextMenuAddIn

{

private const string s_DisplayName = "Generic Context Menu AddIn";

public GenericContextMenuAddIn() : base(s_DisplayName)

{

}

protected override void BuildContextMenuItems(ContextMenuAddInRoot addInRootSubmenu)

{

addInRootSubmenu.Items.AddActionItem&lt;WorkspaceFile&gt;("Generic Context Menu", LogClickDelegate);

}

private void LogClickDelegate(MenuSelectionProvider&lt;WorkspaceFile&gt; menuSelectionProvider)

{

//Executed program code for the first entry of the shortcut menu

}

}

}

---

**See also**

[Basics of Add-Ins in the workspace](#basics-of-add-ins-in-the-workspace)
  
[Programming shortcut menus for Repository Add-Ins](#programming-shortcut-menus-for-repository-add-ins)

### Programming shortcut menus for Repository Add-Ins

The following two steps are necessary for programming shortcut menus for Repository Add-Ins:

- Programming the specific Repository Provider "VciRepositoryAddInProvider"
- Programming the specific Repository Add-In

To use the Add-In for a workspace, it must be configured in the corresponding workspace in addition to being activated in the TIA Portal.

#### Requirement

A C# project exists for creating a class library.

#### Programming a specific "VciRepositoryAddInProvider" Repository Provider

To program the specific Repository Provider"VciRepositoryAddInProvider", proceed as follows:

1. Create a new class in your project and give it a meaningful name, e.g. "VciRepositoryProvider.cs".
2. Add the following two using directives to the class:

   - `using Siemens.Engineering.AddIn.VersionControl;`
   - using &lt;Name of your project&gt;;
3. Declare your class as "public" and make the class a subclass of "VciRepositoryAddInProvider":

   `public class WorkspaceSpecificRepositoryAddInProvider : VciRepositoryAddInProvider`
4. Enter "override" in the new class as text and select the entry "GetVciRepositoryAddIns" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
5. Remove the contents of the method and enter the following code instead:

   `yield return new` 
   `<Your_`
   `WorkspaceSpecificRepositoryAddIn`
   `_Class_name>("<Name of the Repository` 
   `Add-Ins`
   `>");`

#### Programming a specific Repository Add-In

To program a new specific Repository Add-In, proceed as follows:

1. Create a new class in your project and give it a meaningful name, e.g. "VciRepositoryAddIn.cs".
2. Add the following using directive to the class:

   using Siemens.Engineering.AddIn.VersionControl;
3. Declare your class as "public" and make the class a subclass of "VciRepositoryAddIn":

   public class RepositorySpecificAddIn : VciRepositoryAddIn
4. Enter "override" in the new class as text and select the entry "GetVciWorkspaceViewAddInProvider" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
5. Create a new class in your project and give it a meaningful name, e.g. "VciWorkspaceProvider.cs".
6. Add the following two using directives to the class:

   - `using Siemens.Engineering.AddIn.Menu;`
   - `using Siemens.Engineering.AddIn.VersionControl;`
7. Declare your class as "public" and make the class a subclass of "VciWorkspaceViewAddInProvider":

   `public class VciWorkspaceProvider : VciWorkspaceViewAddInProvider`
8. Enter "override" in the new class as text and select the entry "GetContextMenuAddIns" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
9. Remove the row "return base.GetContextMenuAddIns();" and enter the following code instead:

   `yield return new` 
   `<Your_`
   `ContextMenu`
   `_Class_ name>("<Text of the shortcut menu>");`

   If you program your shortcut menu in a "AddInContextMenu" class and the entry in the shortcut menu is to be called "My AddIn", the line would look as follows:

   `yield return new AddInContextMenu("My AddIn");`

Shortcut menus created using a Repository Add-In are only available if the Add-In was configured in the workspace. Otherwise there is no difference to the general shortcut menus.

#### Complete example for programming a workspace-specific shortcut menu

View Provider "VciRepositoryAddInProvider":

using System.Collections.Generic;

using Siemens.Engineering.AddIn.VersionControl;

using VCI.RepoSpecificContextMenu.AddIn;

namespace Vci.Git.AddIn

{

public class WorkspaceSpecificRepositoryAddInProvider : VciRepositoryAddInProvider

{

public override IEnumerable&lt;VciRepositoryAddIn&gt; GetVciRepositoryAddIns()

{

yield return new RepoSpecificAddIn();

}

}

}

The specific Repository Add-In consists of two different classes.

using Siemens.Engineering.AddIn.VersionControl;

namespace VCI.RepoSpecificContextMenu.AddIn

{

public class RepoSpecificAddIn : VciRepositoryAddIn

{

private const string s_DisplayName = "Repo Specific Context Menu AddIn";

public RepoSpecificAddIn() : base(s_DisplayName)

{

}

public override VciWorkspaceViewAddInProvider GetVciWorkspaceViewAddInProvider()

{

return new RepoSpecificWorkspaceViewAddInProvider();

}

}

}

using System.Windows.Forms;

using Siemens.Engineering.AddIn.Menu;

using Siemens.Engineering.AddIn.VersionControl;

namespace VCI.RepoSpecificContextMenu.AddIn

{

public class VCIContextMenuAddIn : ContextMenuAddIn

{

private const string s_DisplayName = "Repo Specific Context Menu AddIn";

public VCIContextMenuAddIn() : base(s_DisplayName)

{

}

protected override void BuildContextMenuItems(ContextMenuAddInRoot addInRootSubmenu)

{

addInRootSubmenu.Items.AddActionItem&lt;WorkspaceFile&gt;("Repo Specific Entry", LogClickDelegate);

}

private void LogClickDelegate(MenuSelectionProvider&lt;WorkspaceFile&gt; menuSelectionProvider)

{

MessageBox.Show("Repo Specific Context Menu Entry", "Repo Specific", MessageBoxButtons.OK, MessageBoxIcon.Information);

}

}

}

---

**See also**

[Basics of Add-Ins in the workspace](#basics-of-add-ins-in-the-workspace)
  
[Programming general shortcut menus](#programming-general-shortcut-menus)
  
[Configuring workspaces](#configuring-workspaces)

### Expanding workflows

You have the option to use Add-Ins to enhance the workflows for drag-and-drop in the workspace and to add functions to the synchronization. You can insert additional functions before and after the workflow.

Depending on the desired functions, the following classes are required for programming Add-Ins for the workflow:

- VCIWorkflowAddIn: Class for workflow support.
- VCIWorkflowAddInProvider: This class provides a provider for the workflow.
- VciWorkflowAddInSupport: This class provides the two members "VciInitialExportSupport**"** and "VciSyncExportSupport", which enable influencing of the workflows.
- InitialExportSupport: Class for the workflow for drag-and-drop into the workspace
- SyncExportSupport: Class for the workflow for synchronization.

You can also rename your classes. Then adjust the code below to match your names.

#### Requirement

A C# project exists for creating a class library.

#### Programming the "VCIWorkflowAddIn" class

To program the "VCIWorkflowAddIn" class, proceed as follows:

1. Create a new class in your project and give it the name "VCIWorkflowAddIn.cs".
2. Add the following two using directives to the class:

   - `using Siemens.Engineering.AddIn.VersionControl;`
   - `using VCI.WorkflowExtension.AddIn.Workflow;`
3. Declare your class as "public" and make the class a subclass of "VciRepositoryAddIn":

   `public class VCIWorkflowAddIn : VciRepositoryAddIn`
4. Add the following method to your class:

   `public VCIWorkflowAddIn(string displayName) : base(displayedAddinName)`

   `{`

   `}`

   Use the string variable "displayedAddinName" to hand over the title for your Add-In to the designer of the basic class. You can rename "displayedAddinName" as you like.

   You can also specify the title for the Add-In in a constant within the class and then use this constant. Then the code looks like this:

   `private const string s_DisplayName = "VCI Workflow Extension AddIn";`

   `public VCIWorkflowAddIn() : base(s_DisplayName)`

   `{`

   `}`
5. Enter "override" in the new class as text and select the entry "GetVciWorkflowAddInSupport" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
6. Remove the contents of the method and enter the following code instead:

   `return new VCIWorkflowAddInSupport();`

#### Programming the "VCIWorkflowAddInProvider" class

To program the "VCIWorkflowAddInProvider" class, proceed as follows:

1. Create a new class in your project and give it the name "VCIWorkflowAddInProvider.cs".
2. Add the following using directive to the class:

   `using Siemens.Engineering.AddIn.VersionControl;`
3. Declare your class as "public" and make the class a subclass of "VciRepositoryAddInProvider":

   `public class VCIWorkflowAddInProvider : VciRepositoryAddInProvider`
4. Enter "override" in the new class as text and select the entry "GetVciRepositoryAddIns" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
5. Remove the contents of the method and enter the following code instead:

   `yield return new VCIWorkflowAddIn();`

#### Programming the "VciWorkflowAddInSupport" class

To program the "VciWorkflowAddInSupport" class, proceed as follows:

1. Create a new class in your project and give it the name "VciWorkflowAddInSupport.cs".
2. Add the following using directive to the class:

   `using Siemens.Engineering.AddIn.VersionControl;`
3. Declare your class as "public" and make the class a subclass of "VciWorkflowAddInSupport":

   `public class VCIWorkflowAddInSupport : VciWorkflowAddInSupport`
4. Enter "override" in the new class as text and select the entry "CreateInitialExportSupport" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
5. Remove the contents of the method and enter the following code instead:

   `return new InitialExportSupport();`
6. Enter "override" in the new class as text and select the entry "CreateSyncExportSupport" in the displayed drop-down menu.

   The method is supplemented to include all relevant components.
7. Remove the contents of the method and enter the following code instead:

   `return new SyncExportSupport();`

#### Programming the "InitialExportSupport" class

To program the "InitialExportSupport" class, proceed as follows:

1. Create a new class in your project and give it the name "InitialExportSupport.cs".
2. Add the following using directive to the class:

   `using Siemens.Engineering.AddIn.VersionControl;`
3. Declare your class as "public" and make the class a subclass of "VciInitialExportSupport":

   `public class InitialExportSupport : VciInitialExportSupport`
4. To execute functions before exporting, enter the following code:

   `public override ExportResult PreExportExecute(IEnumerable<InitialPreExportInfo> itemsToExport,  
    VciInitialExportAddInContext vciInitialExportAddInContext)`

   `{`

   `//Program code for the function`

   `return ExportResult.Succeeded;`

   `}`
5. To execute functions after exporting, enter the following code:

   `public override ExportResult PostExportExecute(IEnumerable<InitialPostExportInfo> itemsToExport,  
    VciInitialExportAddInContext vciInitialExportAddInContext)`

   `{`

   `//Program code for the function`

   `return ExportResult.Succeeded;`

   `}`

Possible values for "Export Result" are "Succeeded", "Failed" and "Aborted".

#### Programming the "SyncExportSupport" class

To program the "SyncExportSupport" class, proceed as follows:

1. Create a new class in your project and give it the name "SyncExportSupport.cs".
2. Add the following using directive to the class:

   `using Siemens.Engineering.AddIn.VersionControl;`
3. Declare your class as "public" and make the class a subclass of "VciSyncExportSupport":

   `public class SyncExportSupport : VciSyncExportSupport`
4. To execute functions before synchronization, enter the following code:

   `public override ExportResult PreExportExecute(IEnumerable<SyncPreExportInfo> itemsToExport,  
    VciSyncExportAddInContext vciSyncExportAddInContext)`

   `{`

   `//Program code for the function`

   `return ExportResult.Succeeded;`

   `}`
5. To execute functions after synchronization, enter the following code:

   `public override ExportResult PostExportExecute(IEnumerable<SyncPostExportInfo> itemsToExport,  
    VciSyncExportAddInContext vciSyncExportAddInContext)`

   `{`

   `//Program code for the function`

   `return ExportResult.Succeeded;`

   `}`

Possible values for "Export Result" are "Succeeded", "Failed" and "Aborted".

#### Complete example for programming Add-Ins for workflows

"VCIWorkflowAddIn" class:

using Siemens.Engineering.AddIn.VersionControl;

using VCI.WorkflowExtension.AddIn.Workflow;

namespace VCI.WorkflowExtension.AddIn

{

public class VCIWorkflowAddIn : VciRepositoryAddIn

{

private const string s_DisplayName = "VCI Workflow Extension AddIn";

public VCIWorkflowAddIn() : base(s_DisplayName)

{

}

public override VciWorkflowAddInSupport GetVciWorkflowAddInSupport()

{

return new VCIWorkflowAddInSupport();

}

}

}

"VCIWorkflowAddInProvider" class:

using System.Collections.Generic;

using Siemens.Engineering.AddIn.VersionControl;

namespace VCI.WorkflowExtension.AddIn

{

public class VCIWorkflowAddInProvider : VciRepositoryAddInProvider

{

public override IEnumerable&lt;VciRepositoryAddIn&gt; GetVciRepositoryAddIns()

{

yield return new VCIWorkflowAddIn();

}

}

}

"VciWorkflowAddInSupport" class:

using Siemens.Engineering.AddIn.VersionControl;

namespace VCI.WorkflowExtension.AddIn.Workflow

{

public class VCIWorkflowAddInSupport : VciWorkflowAddInSupport

{

public override VciInitialExportSupport CreateInitialExportSupport()

{

return new InitialExportSupport();

}

public override VciSyncExportSupport CreateSyncExportSupport()

{

return new SyncExportSupport();

}

}

}

"InitialExportSupport" class:

using System.Collections.Generic;

using Siemens.Engineering.AddIn.VersionControl;

namespace VCI.WorkflowExtension.AddIn.Workflow

{

public class InitialExportSupport : VciInitialExportSupport

{

public override ExportResult PreExportExecute(IEnumerable&lt;InitialPreExportInfo&gt; itemsToExport,

VciInitialExportAddInContext vciInitialExportAddInContext)

{

// Program code for the function

return ExportResult.Succeeded;

}

public override ExportResult PostExportExecute(IEnumerable&lt;InitialPostExportInfo&gt; itemsToExport,

VciInitialExportAddInContext vciInitialExportAddInContext)

{

// Program code for the function

return ExportResult.Succeeded;

}

}

}

"SyncExportSupport" class:

using System.Collections.Generic;

using Siemens.Engineering.AddIn.VersionControl;

namespace VCI.WorkflowExtension.AddIn.Workflow

{

public class SyncExportSupport : VciSyncExportSupport

{

public override ExportResult PreExportExecute(IEnumerable&lt;SyncPreExportInfo&gt; itemsToExport,

VciSyncExportAddInContext vciSyncExportAddInContext)

{

// Program code for the function

return ExportResult.Succeeded;

}

public override ExportResult PostExportExecute(IEnumerable&lt;SyncPostExportInfo&gt; itemsToExport,

VciSyncExportAddInContext vciSyncExportAddInContext)

{

// Program code for the function

return ExportResult.Succeeded;

}

}

}
